"""Stvarna SVG geometrija U10: prolazi, presjeci, vektori i krak momenta.

Provjera čita objavljene vektorske putanje, ne autorski generator.
Ne zamjenjuje vizualni pregled ni neovisnu provjeru numeričkih rezultata.
"""
from pathlib import Path
import math
import re
import xml.etree.ElementTree as ET

from sketch_style import check_uniform_fluid

ROOT = Path(__file__).resolve().parents[1] / 'assets' / 'print'
NS = '{http://www.w3.org/2000/svg}'


def check(condition, message):
    if not condition:
        raise AssertionError(message)


def node(root, id):
    found = root.find(f'.//*[@id="{id}"]')
    check(found is not None, 'Nedostaje element ' + id)
    return found


def path(element):
    """Sample absolute M/L/H/V/Q paths; reject unsupported commands."""
    tokens = re.findall(r'[A-Za-z]|-?\d+(?:\.\d+)?', element.get('d', ''))
    points, i, current = [], 0, (0., 0.)
    while i < len(tokens):
        command = tokens[i]
        i += 1
        if command == 'Z':
            points.append(points[0])
            continue
        check(command in ('M', 'L', 'H', 'V', 'Q'), 'Nepodržana naredba ' + command)
        count = {'M': 2, 'L': 2, 'H': 1, 'V': 1, 'Q': 4}[command]
        values = list(map(float, tokens[i:i+count]))
        i += count
        if command in ('M', 'L'):
            current = tuple(values)
        elif command == 'H':
            current = (values[0], current[1])
        elif command == 'V':
            current = (current[0], values[0])
        else:
            start = current
            for j in range(1, 101):
                t = j / 100
                current = tuple((1-t)**2*start[k]+2*t*(1-t)*values[k]+t*t*values[k+2] for k in (0, 1))
                points.append(current)
            continue
        points.append(current)
    return points


def segment_distance(p, a, b):
    ab = tuple(y-x for x,y in zip(a,b))
    length2 = sum(x*x for x in ab)
    t = max(0., min(1., sum((p[k]-a[k])*ab[k] for k in (0,1))/length2)) if length2 else 0.
    return math.dist(p, tuple(a[k]+t*ab[k] for k in (0,1)))


def distance_to_path(p, poly):
    return min(segment_distance(p,a,b) for a,b in zip(poly,poly[1:]))


def line(element):
    if element.tag == NS+'line':
        return [(float(element.get('x'+i)), float(element.get('y'+i))) for i in ('1','2')]
    points = path(element)
    check(len(points) == 2, 'Očekivana ravna strelica ili kota')
    return points


def delta(element):
    a,b = line(element)
    return b[0]-a[0], b[1]-a[1]


def wall_and_openings(root, prefix, ports):
    fluid = node(root,prefix+'fluid')
    poly = path(fluid)
    walls = [path(e) for e in root.iter() if re.fullmatch(re.escape(prefix)+r'wall\d+', e.get('id',''))]
    check(bool(walls), prefix+': nedostaju unutarnje plohe stijenki')
    check(all(distance_to_path(p,poly)<2e-5 for w in walls for p in w),
          prefix+': kruta stijenka mora slijediti rub, bez pregrade u fluidu')
    for p in ports:
        check(distance_to_path(p,poly)<2e-5, prefix+': otvor mora pripadati rubu fluida')
        check(min(distance_to_path(p,w) for w in walls)>5, prefix+': kruta stijenka zatvara otvor')


def elbow_width(root, prefix, inlet_width, outlet_width):
    inner = path(node(root,prefix+'wall0'))[1:-1]
    outer = list(reversed(path(node(root,prefix+'wall1'))[1:-1]))
    check(len(inner)==len(outer)==91,prefix+': mora se provjeriti cijeli kružni zavoj')
    for i,(a,b) in enumerate(zip(inner,outer)):
        expected = inlet_width+(outlet_width-inlet_width)*i/90
        check(abs(math.dist(a,b)-expected)<2e-6,prefix+': pogrešan promjer kroz zavoj')
        # Normal to the actual circular centerline tangent at this station.
        t=math.radians(i)
        dx,dy=b[0]-a[0],b[1]-a[1]
        check(abs(abs(dx)-expected*math.sin(t))<2e-6
              and abs(abs(dy)-expected*math.cos(t))<2e-6,
              prefix+': promjer nije okomit na os toka')


def plate(root, prefix):
    solid=node(root,prefix+'plate')
    poly=path(node(root,prefix+'fluid'))
    face=float(solid.get('x'))
    check(max(x for x,y in poly)==face, prefix+': fluid ne prolazi kroz ploču')
    check(min(y for x,y in poly)<float(solid.get('y')) and
          max(y for x,y in poly)>float(solid.get('y'))+float(solid.get('height')),
          prefix+': razlijevanje mora dosegnuti otvorene izlazne rubove')


def branch(root, prefix, velocity_id, diameter_id):
    section=line(node(root,prefix+'section3'))
    vx,vy=delta(node(root,velocity_id))
    sx,sy=(section[1][i]-section[0][i] for i in (0,1))
    check(vx>0 and abs(vy/vx+math.sqrt(3))<1e-8, prefix+': smjer grane mora biti +60° u xy')
    check(abs(vx*sx+vy*sy)<1e-8, prefix+': izlazni presjek nije okomit na tok')
    dx,dy=delta(node(root,diameter_id))
    check(abs(dx-sx)<1e-8 and abs(dy-sy)<1e-8, prefix+': kota ne mjeri stvaran poprečni promjer')
    check(abs(vx*dx+vy*dy)<1e-8,prefix+': kosa kota mora biti normalna na granu')
    return tuple(sum(p[i] for p in section)/2 for i in (0,1))


def run():
    names=('u11_fig_uvod_pregled','u11_val1_mlaz_na_plocu','u11_val2_mlaznica_prirubnica',
           'u11_val3_koljeno_reakcija','u11_ch1_t_racva_konzola','u11_ch2_y_racva_reakcija',
           'u10_fig_hidroenergetsko_koljeno','u11_vjezbe_skice')
    roots=[ET.parse(ROOT/(name+'.svg')).getroot() for name in names]
    for root,name in zip(roots,names):
        ids=[e.get('id') for e in root.iter() if e.get('id')]
        check(len(ids)==len(set(ids)),name+': duplicirani ID')
        check(not any(e.tag==NS+'filter' for e in root.iter()),name+': sjena/filtri nisu dopušteni')
        for fluid in (e for e in root.iter() if e.get('id','').endswith('fluid')):
            check(fluid.get('stroke')=='none' and fluid.get('d').count('M')==1
                  and fluid.get('d').count('Z')==1,name+': jedna povezana ispuna bez zatvorenih stijenki na otvorima')
            check_uniform_fluid(fluid, 'fill')
    intro,p1,p2,p3,p4,p5,p6,z=roots
    wall_and_openings(intro,'u11intro_pipe',[(58,187),(321,379)])
    elbow_width(intro,'u11intro_pipe',82,56)
    check(node(intro,'u11intro_cv').get('d')==node(intro,'u11intro_pipefluid').get('d'),
          'Uvod: granica KV mora obuhvaćati točno fluid i stvarne kontrolne presjeke')
    for id,sign in [('u11intro_pressure2',-1),('u11intro_outflow',1)]:
        dx,dy=delta(node(intro,id));check(dx==0 and dy*sign>0,id+': izlazni tlak i brzina su suprotni')
    check(float(node(intro,'u11intro_flangeleft').get('x'))+float(node(intro,'u11intro_flangeleft').get('width'))<=293
          and float(node(intro,'u11intro_flangeright').get('x'))>=349,
          'Uvod: prirubnica mora ostaviti cijeli otvor 56 px')
    plate(p1,'u11v1_jet')
    wall_and_openings(p2,'u11v2_nozzle',[(45,250)])
    top,bottom=(node(p2,'u11v2_flange'+x) for x in ('top','bottom'))
    check(float(top.get('y'))+float(top.get('height'))<=189.5 and float(bottom.get('y'))>=310.5,
          'P2: prirubnica ne smije premostiti fluid')
    check(abs(math.dist(*line(node(p2,'u11v2_D')))/math.dist(*line(node(p2,'u11v2_d')))-220/90)<1e-10,
          'P2: kote moraju očuvati omjer 220:90')
    nozzle_poly=path(node(p2,'u11v2_nozzlefluid'))
    widths=[]
    for x in range(46,410):
        cuts=sorted(a[1]+(b[1]-a[1])*(x-a[0])/(b[0]-a[0]) for a,b in zip(nozzle_poly,nozzle_poly[1:])
                    if min(a[0],b[0])<=x<max(a[0],b[0]))
        check(len(cuts)==2 and cuts[1]>cuts[0],'P2: neprekinut otvor duž sapnice')
        widths.append(cuts[1]-cuts[0])
    check(all(b<=a+1e-9 for a,b in zip(widths,widths[1:])), 'P2: bez lažnog suženja i ponovnog širenja')
    check(max(x for x,y in nozzle_poly)==float(node(p2,'u11v2_plate').get('x')),
          'P2: slobodni mlaz završava na prednjoj strani ploče')
    wall_and_openings(p3,'u11v3_pipe',[(54,274),(310,101)])
    elbow_width(p3,'u11v3_pipe',72,48)
    wall_and_openings(p4,'u11ch1_tee',[(56,270),(533,270),(300,103)])
    check([math.dist(*line(node(p4,'u11ch1_D'+str(i)))) for i in (1,2,3)]==[72,36,32],
          'P4: promjeri 180:90:80 u istom mjerilu')
    out=branch(p5,'u11ch2_pipe','u11ch2_branchvelocity','u11ch2_D3')
    wall_and_openings(p5,'u11ch2_pipe',[(53,283),(529,283),out])
    dx,dy=delta(node(p5,'u11ch2_reaction'))
    check(dx<0 and dy<0 and abs(dy/dx-625/664)<1e-8,'P5: reakcija mora biti ulijevo i prema +y')
    outlet=line(node(p6,'u10he_section2'))
    wall_and_openings(p6,'u10he_pipe',[(49,178),tuple(sum(p[i] for p in outlet)/2 for i in (0,1))])
    vx,vy=delta(node(p6,'u10he_outflow'));sx,sy=delta(node(p6,'u10he_section2'))
    check(vx>0 and abs(vy/vx-math.sqrt(3))<1e-9 and abs(vx*sx+vy*sy)<1e-8,
          'P6: tok mora izlaziti pod −60°, normalno na otvor')
    check(abs(math.hypot(sx,sy)-46)<1e-9,'P6: otvor čuva ulazni promjer')
    a=path(node(p6,'u10he_pipewall0'))[1:-1]
    b=list(reversed(path(node(p6,'u10he_pipewall1'))[1:-1]))
    check(len(a)==len(b)==61 and all(abs(math.dist(x,y)-46)<2e-6 for x,y in zip(a,b)),
          'P6: stalni promjer kroz cijeli zavoj od 60°')
    px,py=delta(node(p6,'u10he_pressure2'))
    check(px<0 and py<0 and abs(px*vy-py*vx)<1e-8,'P6: izlazni tlak djeluje suprotno brzini')
    for n in (1,2,4,5):plate(z,'u11vs_z'+str(n))
    wall_and_openings(z,'u11vs_z3',[(36,187),(230,75)])
    elbow_width(z,'u11vs_z3',60,60)
    O,C=(node(z,'u11vs_z4'+x) for x in ('O','C'))
    bx=float(C.get('cx'))-float(O.get('cx'));ey=float(O.get('cy'))-float(C.get('cy'))
    check(abs(bx/ey-.20/.35)<1e-10,'Z4: krakovi b i e moraju biti u istom mjerilu')
    check(math.dist(*line(node(z,'u11vs_z4b')))==bx and math.dist(*line(node(z,'u11vs_z4e')))==ey,
          'Z4: kote moraju mjeriti stvarne koordinate O i C')
    for id,sign in [('u11vs_z5outtop',-1),('u11vs_z5outbottom',1)]:
        dx,dy=delta(node(z,id))
        check(dx>0 and abs(dy/dx-sign*(20-8)/8)<1e-9,id+': apsolutna izlazna brzina mora imati v₂x=u i |v₂y|=v−u')
    out=branch(z,'u11vs_z6','u11vs_z6branchvelocity','u11vs_z6D3')
    wall_and_openings(z,'u11vs_z6',[(36,199),(412,199),out])
    check([math.dist(*line(node(z,'u11vs_z6D'+str(i)))) for i in (1,2)]==[56,36]
          and abs(math.dist(*line(node(z,'u11vs_z6D3')))-32)<1e-9,
          'Z6: promjeri 140:90:80 u istom mjerilu')
    print('PASS U10: osam SVG-ova; otvorene granice, stijenke, omjeri i normalni presjeci, krak momenta i smjerovi vektora.')


if __name__ == '__main__':
    run()
