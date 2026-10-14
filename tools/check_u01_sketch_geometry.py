"""Read all seven public U01 SVGs and check actual geometry and force directions.

Complements visual review. It does not import the ignored drawing generator.
"""
from pathlib import Path
import math
import re
import xml.etree.ElementTree as ET
from check_u10_sketch_geometry import check, node, path, line, delta, distance_to_path
from check_u13_sketch_geometry import close, rect

from sketch_style import check_uniform_fluid

ROOT = Path(__file__).resolve().parents[1] / 'assets' / 'print'


def inside(point, polygon):
    x,y=point
    crossings=0
    for (xa,ya),(xb,yb) in zip(polygon,polygon[1:]):
        if (ya>y)!=(yb>y) and x<xa+(y-ya)*(xb-xa)/(yb-ya):
            crossings+=1
    return crossings%2==1


def sample_segment(a,b,count=51):
    return [tuple(a[k]+i/(count-1)*(b[k]-a[k]) for k in (0,1)) for i in range(count)]


def connected_fluid(root,prefix,routes):
    element=node(root,prefix+'fluid');poly=path(element)
    check(element.get('d').count('M')==1 and element.get('d').count('Z')==1,
          prefix+': jedna povezana fluidna domena')
    check(element.get('stroke')=='none',prefix+': ispuna ne dodaje kapu na otvor')
    check_uniform_fluid(element, 'fill')
    walls=[path(e) for e in root.iter() if re.fullmatch(re.escape(prefix)+r'wall\d+',e.get('id',''))]
    check(bool(walls),prefix+': stvarne stijenke moraju biti označene')
    for w in walls:
        for a,b in zip(w,w[1:]):
            for p in sample_segment(a,b):
                check(not inside(p,poly) or distance_to_path(p,poly)<1e-7,
                      prefix+': stijenka presijeca fluid')
    for route in routes:
        for a,b in zip(route,route[1:]):
            for p in sample_segment(a,b,101):
                check(inside(p,poly) and distance_to_path(p,poly)>1,
                      prefix+': predviđeni prolaz nije u fluidu')
                check(min(distance_to_path(p,w) for w in walls)>1,
                      prefix+': stijenka zatvara spoj')
    return poly,walls


def comb(root,prefix,count,ratios):
    pistons=[rect(node(root,prefix+f'piston{i}')) for i in range(count)]
    poly=path(node(root,prefix+'fluid'))
    bottom=max(y for x,y in poly)
    # Read the manifold's top from the horizontal edges between adjacent bores.
    gaps=[]
    for left,right in zip(pistons,pistons[1:]):
        xmid=(left[0]+left[2]+right[0])/2
        levels=[a[1] for a,b in zip(poly,poly[1:]) if a[1]==b[1]
                and min(a[0],b[0])<xmid<max(a[0],b[0])]
        check(len(levels)==2,prefix+': točno dvije stijenke između komora')
        gaps.append(sum(levels)/2)
    routes=[]
    for i,(a,b) in enumerate(zip(pistons,pistons[1:])):
        xa=a[0]+a[2]/2;xb=b[0]+b[2]/2;ym=gaps[i]
        routes.append([(xa,a[1]+a[3]+4),(xa,ym),(xb,ym),(xb,b[1]+b[3]+4)])
    poly,walls=connected_fluid(root,prefix,routes)
    for i,(x,y,w,h) in enumerate(pistons):
        close(w/pistons[0][2],ratios[i],prefix+': omjer promjera mora odgovarati podatcima',tol=1e-9)
        for xx in (x+w*.1,x+w*.5,x+w*.9):
            close(distance_to_path((xx,y+h),poly),0,prefix+': tlačna ploha klipa dodiruje tekućinu')
        rx,ry,rw,rh=rect(node(root,prefix+f'rod{i}'))
        close(rx+rw/2,x+w/2,prefix+': klipnjača i klip imaju istu os')
        close(ry+rh,y,prefix+': klipnjača završava na klipu')
        check(0<rw<w and ry<y,prefix+': klipnjača ostaje izvan tekućine')
        check(all(not inside(p,poly) for p in sample_segment((x+1,y+h/2),(x+w-1,y+h/2))),
              prefix+': fluid ne prolazi kroz tijelo klipa')
    return pistons


def steering(root,prefix):
    """Z2: two rams on a double-ended tiller; same oil, opposite thrusts, one torque sense."""
    poly,walls=connected_fluid(root,prefix+'system',[[(60,260),(60,272),(262,272),(262,62),(240,62),(240,110)]])
    tiller=rect(node(root,prefix+'tiller'));stock=node(root,prefix+'stock')
    cx,cy=float(stock.get('cx')),float(stock.get('cy'))
    close(cx,tiller[0]+tiller[2]/2,'Z2: struk kormila u sredini ruda');close(cy,tiller[1]+tiller[3]/2,'Z2: struk na osi ruda')
    arms=[];bores=[];thrusts=[]
    for i in range(2):
        x,y,w,h=rect(node(root,prefix+f'systempiston{i}'))
        rx,ry,rw,rh=rect(node(root,prefix+f'systemrod{i}'))
        close(rx+rw/2,x+w/2,'Z2: klipnjača i klip imaju istu os');check(0<rw<w,'Z2: klipnjača tanja od klipa')
        face=(y+h) if i==0 else y            # lijevi klip gura prema gore, desni prema dolje
        for xx in (x+w*.1,x+w*.5,x+w*.9):close(distance_to_path((xx,face),poly),0,'Z2: tlačna ploha klipa dodiruje ulje')
        check(all(not inside(p,poly) for p in sample_segment((rx+1,ry+1),(rx+1,ry+rh-1))),'Z2: klipnjača ostaje izvan ulja')
        end=(tiller[1]+tiller[3]) if i==0 else tiller[1]
        close(ry if i==0 else ry+rh,end,'Z2: klipnjača dodiruje rudo');close(ry+rh if i==0 else ry,y if i==0 else y+h,'Z2: klipnjača završava na klipu')
        dx,dy=delta(node(root,prefix+f'force{i}'))
        check(abs(dx)<1e-9 and dy*(-1 if i==0 else 1)>0,'Z2: sila ulja gura klip prema rudu')
        a,b=line(node(root,prefix+f'force{i}'));check(inside(a,poly),'Z2: sila ulja počinje u ulju')
        arms.append(rx+rw/2-cx);bores.append(w);thrusts.append(dy)
    close(bores[0],bores[1],'Z2: oba cilindra istoga promjera')
    # Krakovi jednaki, na suprotnim stranama struka; vertikalne sile daju moment istoga smisla.
    torque=[arm*dy for arm,dy in zip(arms,thrusts)]   # >0: satni smisao na zaslonu (y prema dolje)
    check(abs(abs(arms[0])-abs(arms[1]))<1e-9 and arms[0]*arms[1]<0,'Z2: jednaki krakovi na suprotnim stranama')
    check(torque[0]>0 and torque[1]>0,'Z2: oba cilindra daju moment istoga smisla')
    e=node(root,prefix+'moment');tk=re.findall(r'[A-Za-z]|[-+]?(?:[0-9]*[.][0-9]+|[0-9]+)',e.get('d'))
    check(len(tk)==11 and tk[0]=='M' and tk[3]=='A' and tk[7]=='0' and tk[8]=='1','Z2: luk momenta u satnom smislu kao sile')
    x1,y1,r1,x2,y2=map(float,(tk[1],tk[2],tk[4],tk[9],tk[10]))
    close(math.dist((x1,y1),(cx,cy)),r1,'Z2: luk momenta oko struka');close(math.dist((x2,y2),(cx,cy)),r1,'Z2: luk momenta oko struka')
    dimension(root,prefix+'arm0',(60,186),(150,186));dimension(root,prefix+'arm1',(150,186),(240,186))
    close(abs(arms[0]),90,'Z2: kota kraka odgovara klipnjači');close(abs(arms[1]),90,'Z2: kota kraka odgovara klipnjači')
    dimension(root,prefix+'d',(228,141),(252,141));close(bores[1],24,'Z2: kota promjera odgovara provrtu')


def vertical(root,id,sign):
    dx,dy=delta(node(root,id));check(abs(dx)<1e-9 and sign*dy>0,id+': pogrešan smjer sile ili pomaka')


def dimension(root,id,start,end):
    e=node(root,id);a,b=line(e)
    close(math.dist(a,start),0,id+': početna kota');close(math.dist(b,end),0,id+': konačna kota')
    check(e.get('marker-start') and e.get('marker-end'),id+': dvostrana kota')


def main():
    names=['u01_fig_uvod_pregled','u01_fig_gustoca_sr','u01_val1_klip_manometar',
           'u01_val2_hidraulicna_dizalica','u01_ch1_dvostruka_platforma_manometar',
           'u01_fig_kocnica_vozila','u01_vjezbe_skice']
    roots=[ET.parse(ROOT/(n+'.svg')).getroot() for n in names]
    for name,root in zip(names,roots):
        ids=[e.get('id') for e in root.iter() if e.get('id')]
        check(len(ids)==len(set(ids)),name+': jedinstveni ID-jevi')
        check(not any(e.tag.endswith('filter') for e in root.iter()),name+': bez sjena')
    intro,density,p2,p3,p4,brakes,z=roots
    comb(intro,'u01fup_press',2,[1,90/35])
    element=rect(node(intro,'u01fup_element'))
    for i in range(4):
        a,b=line(node(intro,f'u01fup_elementForce{i}'))
        center=(element[0]+element[2]/2,element[1]+element[3]/2)
        check(math.dist(b,center)<math.dist(a,center),'Uvod: tlak sabija mali element')
    vertical(intro,'u01fup_input',1);vertical(intro,'u01fup_output',-1)
    # P1 tekst nema dubinu h: kota je uklonjena; tezina mora ostati unutar ulja.
    check(not any(e.get('id')=='u01fgs_h' for e in density.iter()),'P1: bez kote h koje nema u tekstu')
    weight=line(node(density,'u01fgs_weight'))
    oil=rect(node(density,'u01fgs_oil'))
    for pt in weight:check(oil[0]<pt[0]<oil[0]+oil[2] and oil[1]<pt[1]<oil[1]+oil[3],'P1: tezina ostaje unutar ulja')
    close(math.dist(weight[0],((144+290)/2,(110+290)/2)),0,'P1: težina djeluje kroz težište ulja')
    vertical(density,'u01fgs_weight',1)
    pi=comb(p2,'u01v1km_system',2,[1,math.sqrt(.045/(math.pi*.16**2/4))])
    dimension(p2,'u01v1km_diameter',(pi[0][0],215),(pi[0][0]+pi[0][2],215))
    vertical(p2,'u01v1km_load',1);vertical(p2,'u01v1km_oilForce',-1)
    close(math.dist(*line(node(p2,'u01v1km_oilForce')))/math.dist(*line(node(p2,'u01v1km_load'))),.045/(math.pi*.16**2/4),'P2: F_2/G = A_2/A_k',tol=0.02)
    pi=comb(p3,'u01v2hd_system',2,[1,math.sqrt(35)])
    dimension(p3,'u01v2hd_inputStroke',(152,190),(152,330))
    dimension(p3,'u01v2hd_outputStroke',(655,330),(655,334))
    close(math.dist(*line(node(p3,'u01v2hd_inputStroke')))/math.dist(*line(node(p3,'u01v2hd_outputStroke'))),35,'P3: hodovi su u omjeru 35')
    for i,id in enumerate(('inputInitial','outputInitial')):
        a,b=line(node(p3,'u01v2hd_'+id))
        close(b[0]-a[0],pi[i][2],'P3: početni presjek pripada istom klipu')
    vertical(p3,'u01v2hd_input',1);vertical(p3,'u01v2hd_output',-1)
    comb(p4,'u01ch1_system',3,[1,1,1/math.sqrt(30)])
    dimension(p4,'u01ch1_liftStroke',(611,358),(611,358+100*25/180))
    dimension(p4,'u01ch1_pumpStroke',(777,258),(777,358))
    close(math.dist(*line(node(p4,'u01ch1_pumpStroke')))/math.dist(*line(node(p4,'u01ch1_liftStroke'))),180/25,'P4: kote s_h i s_L u istom mjerilu (180:25)',tol=1e-4)
    lens={k:math.dist(*line(node(p4,'u01ch1_'+k))) for k in ('load','liftForce0','liftForce1','pumpForce')}
    close(lens['load'],2*lens['liftForce0'],'P4: G=2F_L u duljinama strelica',tol=1e-6)
    check(lens['liftForce0']==lens['liftForce1']>lens['pumpForce'],'P4: poredak F_L > F_p')
    for id,sign in [('load',1),('pumpForce',1),('liftForce0',-1),('liftForce1',-1)]:vertical(p4,'u01ch1_'+id,sign)
    # True perpendicular moment arms from the same pivot for vertical forces.
    lever=line(node(brakes,'u01fkv_lever'))
    pivot=(60,94);close(math.dist(lever[0],pivot),0,'P5: početak poluge je zglob')
    master=line(node(brakes,'u01fkv_pushrod'))[0]
    close((lever[1][0]-pivot[0])/(master[0]-pivot[0]),5,'P5: mehanički omjer poluge 5:1')
    close(distance_to_path(master,lever),0,'P5: potisna šipka dodiruje polugu')
    dimension(brakes,'u01fkv_shortArm',(60,47),(105,47))
    dimension(brakes,'u01fkv_longArm',(60,20),(285,20))
    master_rect=rect(node(brakes,'u01fkv_masterPiston'))
    dimension(brakes,'u01fkv_masterDiameter',(master_rect[0],249),(master_rect[0]+master_rect[2],249))
    routes=[[(105,217),(105,347),(x,347),(x,455)] for x in (128,242,362,485)]
    poly,walls=connected_fluid(brakes,'u01fkv_system',routes)
    for i,diameter in enumerate((35,30,30,35)):
        x,y,w,h=rect(node(brakes,f'u01fkv_workPiston{i}'))
        close(h/master_rect[2],diameter/20,'P5: svi provrti u istom mjerilu')
        face=x if i<2 else x+w
        close(distance_to_path((face,y+h/2),poly),0,'P5: radni klip zatvara fluid')
        dx,dy=delta(node(brakes,f'u01fkv_workForce{i}'))
        check(abs(dy)<1e-9 and dx*(1 if i<2 else -1)>0,'P5: sila ulja prema klipu')
    vertical(brakes,'u01fkv_foot',1);vertical(brakes,'u01fkv_masterForce',1)
    # Arrow lengths keep the order F_n < F_M < F_r < F_f and the exact F_f/F_r=(35/30)^2.
    L={k:math.dist(*line(node(brakes,'u01fkv_'+k))) for k in ('foot','masterForce','workForce0','workForce1','workForce2','workForce3')}
    check(L['foot']<L['masterForce']<L['workForce1']<L['workForce0'],'P5: poredak duljina F_n < F_M < F_r < F_f')
    close(L['workForce0'],L['workForce3'],'P5: jednake sile prednjih klipova');close(L['workForce1'],L['workForce2'],'P5: jednake sile stražnjih klipova')
    close(L['workForce0']/L['workForce1'],(35/30)**2,'P5: F_f/F_r=(d_f/d_r)^2',tol=0.01)
    steering(z,'u01vs_z2')
    for num,ratio in [(3,3),(5,math.sqrt(4*.003/math.pi)/.009)]:
        pi=comb(z,f'u01vs_z{num}system',2,[1,ratio])
        if num<5:
            for i in (0,1):dimension(z,f'u01vs_z{num}d{i+1}',(pi[i][0],259),(pi[i][0]+pi[i][2],259))
        vertical(z,f'u01vs_z{num}input',1)
        vertical(z,f'u01vs_z{num}motion0',1);vertical(z,f'u01vs_z{num}motion1',-1)
    connected_fluid(z,'u01vs_z4system',[[(16,165),(180,165),(200,165)]])
    dimension(z,'u01vs_z4stroke',(138,101),(204,101))
    close(line(node(z,'u01vs_z4initial'))[0][0],138,'Z4: početna tlačna ploha')
    close(rect(node(z,'u01vs_z4piston'))[0],204,'Z4: konačna tlačna ploha')
    comb(z,'u01vs_z6system',4,[1,1,1,.022/math.sqrt(4*.0095/math.pi)])
    vertical(z,'u01vs_z6load',1);vertical(z,'u01vs_z6pumpForce',1);vertical(z,'u01vs_z6lift',-1)
    # Equal cup areas: doubled measured liquid volume must double its height.
    h1=rect(node(z,'u01vs_z1fluid1'))[3];h2=rect(node(z,'u01vs_z1fluid2'))[3]
    close(h2/h1,2,'Z1: punjenja 50 i 100 cm³ u istoj posudi')
    print('U01 SVG PASS: 7 slika; povezani fluidi, otvoreni priključci, klipovi, sile, promjeri, kote hodova, poluga 5:1 i kormilarski stroj Z2.')


if __name__=='__main__':main()
