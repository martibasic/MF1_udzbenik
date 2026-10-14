"""Provjera stvarne geometrije skica kompresibilnog U09 (zasebno pokretanje).

Provjerava otvorene prolaze, monotonost sapnica, kotu između mjernih točaka,
smjerove zvuka i prolaze mjernih vodova. Ne zamjenjuje vizualni pregled.
"""
from pathlib import Path
import re
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1] / "assets" / "print"
CHECKS = []


def check(condition, message):
    if not condition:
        raise AssertionError(message)
    CHECKS.append(message)


def element(root, id):
    node = root.find(f'.//*[@id="{id}"]')
    if node is None:
        raise AssertionError("Nedostaje geometrijski element: " + id)
    return node


def numbers(node):
    return [float(x) for x in re.findall(r"-?\d+(?:\.\d+)?", node.get("d", ""))]


def polygon(node):
    """Sample actual absolute SVG paths, retaining connected curve geometry."""
    tokens = re.findall(r"[MLHVCQZ]|-?\d+(?:\.\d+)?", node.get("d", ""))
    result, i, current = [], 0, (0.0, 0.0)
    while i < len(tokens):
        command = tokens[i]
        i += 1
        if command == 'Z':
            result.append(result[0])
            continue
        count = {'M': 2, 'L': 2, 'H': 1, 'V': 1, 'C': 6, 'Q': 4}[command]
        values = list(map(float, tokens[i:i+count]))
        i += count
        if command in ('M', 'L'):
            current = tuple(values)
        elif command == 'H':
            current = (values[0], current[1])
        elif command == 'V':
            current = (current[0], values[0])
        else:
            points = [current] + list(zip(values[::2], values[1::2]))
            for j in range(1, 101):
                t, points_t = j/100, points
                while len(points_t) > 1:
                    points_t = [tuple((1-t)*a+t*b for a,b in zip(p,q))
                                for p,q in zip(points_t,points_t[1:])]
                result.append(points_t[0])
            current = points[-1]
            continue
        result.append(current)
    return result


def vertical_intersections(poly, x):
    return sorted(a[1]+(b[1]-a[1])*(x-a[0])/(b[0]-a[0])
                  for a,b in zip(poly,poly[1:]) if min(a[0],b[0]) <= x < max(a[0],b[0]))


def nozzle(root, prefix, convergent, area_ratio=None):
    gas = element(root,prefix+'gas')
    check(gas.get('stroke') == 'none',prefix+': rub ispune ne zatvara ulaz/izlaz')
    gas_poly = polygon(gas)
    walls = [polygon(element(root,prefix+part)) for part in ('top','bottom')]
    left, right = min(x for x,y in gas_poly), max(x for x,y in gas_poly)
    widths = []
    for j in range(1,100):
        x = left+(right-left)*j/100
        edges = vertical_intersections(gas_poly,x)
        check(len(edges)==2 and edges[1]>edges[0],prefix+': jedan povezan otvor na presjeku '+str(j))
        center = sum(edges)/2
        widths.append(edges[1]-edges[0])
        for wall in walls:
            cuts=vertical_intersections(wall,x)
            check(not (min(cuts)<center<max(cuts)),prefix+': stijenka ne presijeca os toka '+str(j))
    if convergent:
        check(all(b <= a+1e-7 for a,b in zip(widths,widths[1:])),prefix+': otvor se postupno smanjuje bez ponovnog širenja')
    else:
        mid=len(widths)//2
        check(all(b<a for a,b in zip(widths[:mid+1],widths[1:mid+1]))
              and all(b>a for a,b in zip(widths[mid:],widths[mid+1:])),prefix+': točno jedno grlo između konvergentnog i divergentnog dijela')
        if area_ratio is not None:
            # Osnosimetrična sapnica: omjer površina izlaza i grla jednak je
            # kvadratu omjera nacrtanih promjera.
            exit_cuts = vertical_intersections(gas_poly, right-1e-6)
            ratio = ((exit_cuts[1]-exit_cuts[0])/min(widths))**2
            check(abs(ratio/area_ratio-1) < 0.01, prefix+': omjer površina izlaza i grla Ae/A* prema tekstu')


def shock(root,front_id,before_id,after_id,top,bottom):
    front=element(root,front_id)
    check(float(front.get('x1'))==float(front.get('x2')),front_id+': val okomit na os kanala')
    check(float(front.get('y1'))==top and float(front.get('y2'))==bottom,front_id+': val između unutarnjih ploha stijenki')
    check(front.get('stroke-dasharray') is not None,front_id+': razlikovanje vala od pune krute stijenke')
    for id in (before_id,after_id):
        x1,y1,x2,y2=numbers(element(root,id))
        check(x2>x1 and y2==y1 and top<y1<bottom,id+': tok udesno i okomit na val')


def run():
    intro=ET.parse(ROOT/'u09_fig_uvod_kompresibilni_tok.svg').getroot()
    tasks=ET.parse(ROOT/'u09_kompresibilni_vjezbe_skice.svg').getroot()
    for root in (intro,tasks):
        ids=[e.get('id') for e in root.iter() if e.get('id')]
        check(len(ids)==len(set(ids)),'Jedinstveni identifikatori')
        check(not any(e.tag.endswith('filter') for e in root.iter()),'Nema filtara sjene')
    nozzle(intro,'u09fukt_nozzle',False,area_ratio=160/100)
    intro_gas=polygon(element(intro,'u09fukt_nozzlegas'))
    exit_line=element(intro,'u09fukt_exit')
    check(float(exit_line.get('x1'))==float(exit_line.get('x2'))==max(x for x,y in intro_gas)
          and sorted(vertical_intersections(intro_gas,float(exit_line.get('x1'))-1e-6))
          and exit_line.get('stroke-dasharray') is not None,
          'Uvod: izlazni presjek Ae označen je na stvarnom otvorenom izlazu sapnice, ne kao stijenka')
    for prefix in ('u09kvs_z2','u09kvs_z4','u09kvs_z5'):
        nozzle(tasks,prefix,True)
        x1,y1,x2,y2=numbers(element(tasks,prefix+'outflow'))
        exit=element(tasks,prefix+'exit')
        check(x1<float(exit.get('x1'))<x2 and y1==y2,prefix+': strelica prolazi otvorenim izlaznim presjekom')
    # Z2: boca, ventil (konvergentni kritični presjek) i vod prema motoru dijele
    # neprekinut plin; kruti rubovi ne zatvaraju ni ulaz ventila ni njegov izlaz.
    z2gas=polygon(element(tasks,'u09kvs_z2gas'))
    z2left,z2right=min(x for x,y in z2gas),max(x for x,y in z2gas)
    inlet=vertical_intersections(z2gas,z2left+1e-6); outlet=vertical_intersections(z2gas,z2right-1e-6)
    bottle=element(tasks,'u09kvs_z2bottlegas'); pipe=element(tasks,'u09kvs_z2pipegas')
    bx,by,bw,bh=(float(bottle.get(k)) for k in ('x','y','width','height'))
    px,py,pw,ph=(float(pipe.get(k)) for k in ('x','y','width','height'))
    check(bx+bw==z2left and by<=inlet[0] and by+bh>=inlet[1],'Z2: boca se otvara izravno u ulaz ventila')
    check(px==z2right and py<outlet[0] and py+ph>outlet[1],
          'Z2: vod prema motoru širi je od kritičnog presjeka i obuhvaća cijeli izlaz ventila')
    top_cuts=vertical_intersections(polygon(element(tasks,'u09kvs_z2top')),z2right-1e-6)
    bottom_cuts=vertical_intersections(polygon(element(tasks,'u09kvs_z2bottom')),z2right-1e-6)
    check(min(top_cuts)<=py and max(bottom_cuts)>=py+ph,
          'Z2: stijenka ventila zatvara stepenicu prema širem vodu, bez procjepa')
    check(bottle.get('fill')==pipe.get('fill')==element(tasks,'u09kvs_z2gas').get('fill'),'Z2: isti plin u boci, ventilu i vodu')
    check(outlet[1]-outlet[0]<inlet[1]-inlet[0]<=bh,'Z2: kritični presjek je najmanji otvor na putu zraka')
    for wall_id in ('u09kvs_z2bottletop','u09kvs_z2bottlebottom','u09kvs_z2bottleleft','u09kvs_z2pipetop','u09kvs_z2pipebottom'):
        wall=element(tasks,wall_id)
        wx,wy,ww,wh=(float(wall.get(k)) for k in ('x','y','width','height'))
        for gx,gy,gw,gh in ((bx,by,bw,bh),(px,py,pw,ph)):
            check(wx+ww<=gx or wx>=gx+gw or wy+wh<=gy or wy>=gy+gh,wall_id+': stijenka ne ulazi u plin')
    shock(intro,'u09fukt_shockfront','u09fukt_before','u09fukt_after',60,175)
    shock(tasks,'u09kvs_z6shock','u09kvs_z6before','u09kvs_z6after',109,183)
    for id,direction in [('z1left',-1),('z1right',1),('z3downstream',1),('z3upstream',-1)]:
        x1,y1,x2,y2=numbers(element(tasks,'u09kvs_'+id))
        check((x2-x1)*direction>0 and y1==y2,id+': ispravan uzdužni smjer signala')
    a,b=(element(tasks,'u09kvs_z3'+x+'section') for x in ('A','B'))
    x1,y1,x2,y2=numbers(element(tasks,'u09kvs_z3length'))
    check(x1==float(a.get('x1')) and x2==float(b.get('x1')) and y1==y2,
          'Z3: kota obuhvaća točno nepomične mjerne točke A i B')
    for text in tasks.iter():
        label=''.join(text.itertext()).strip() if text.tag.endswith('text') else ''
        if re.match(r'^M[₁₂]',label) or label.startswith('Ma'):
            check(label.startswith('Ma'),'Machov broj označen je kao Ma, ne M')
    gas=element(tasks,'u09kvs_z6gas')
    wall_rects=[e for e in element(tasks,'u09kvs_z6') if e.tag.endswith('rect')
                and (e.get('id','').startswith('u09kvs_z6top') or e.get('id','').startswith('u09kvs_z6bottom'))]
    for id in ('z6p1','z6p2','z6pitot'):
        pipe,wall=(element(tasks,'u09kvs_'+id+name) for name in ('water','wall'))
        check(pipe.get('d')==wall.get('d') and pipe.get('stroke-linecap')=='butt',
              id+': ista os fluida i stijenke, bez završnog čepa')
        check(pipe.get('stroke')==gas.get('fill'),id+': ista neprekinuta ispuna plina')
        vals=numbers(pipe)
        if id=='z6pitot':
            x, y=polygon(pipe)[-1][0],109.0
            check(209<vals[0]<vals[2] and 109<vals[1]<183,
                  'Pitot: otvor iza vala okrenut uzvodno, unutar toka')
        else:
            x,y=vals[0],183.0
        r=float(wall.get('stroke-width'))/2
        intersecting=[e for e in wall_rects if float(e.get('y'))<=y<=float(e.get('y'))+float(e.get('height'))]
        check(all(x+r<=float(e.get('x')) or x-r>=float(e.get('x'))+float(e.get('width')) for e in intersecting),
              id+': cijeli mjerni priključak prolazi kroz otvor u krutoj stijenci')
    print(f'PASS U09: {len(CHECKS)} provjera stvarne geometrije skica.')


if __name__=='__main__':
    run()
