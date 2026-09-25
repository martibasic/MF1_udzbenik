"""Čita tri stvarna SVG-a U13: topologija toka, kote, profili i krivulje.

Ne ovisi o privremenom generatoru skica. Kvantitativne krivulje provjerava
iz njihovih nacrtanih koordinata i izvornih jednadžbi zadatka.
"""
import math
from copy import deepcopy
from pathlib import Path
import re
import xml.etree.ElementTree as ET
from check_u10_sketch_geometry import check,node,path,line,delta,distance_to_path,wall_and_openings

from sketch_style import check_uniform_fluid

ROOT=Path(__file__).resolve().parents[1]/'assets'/'print'


def close(a,b,message,tol=2e-5):
    check(abs(a-b)<=tol,message)


def rect(e):return tuple(float(e.get(k)) for k in ('x','y','width','height'))


def subpaths(e):
    return [path(ET.Element('path',d=d)) for d in re.split(r'(?=M)',e.get('d')) if d.strip()]


def graph(root,prefix):
    fluid=node(root,prefix+'fluid');wall=node(root,prefix+'outer')
    check(fluid.get('d')==wall.get('d'),'Stijenka i fluid moraju pratiti istu os bez zatvorenih kapa')
    check(fluid.get('stroke-linecap')==wall.get('stroke-linecap')=='butt','Otvor ne smije dobiti zaobljenu zatvorenu kapu')
    width=float(fluid.get('stroke-width'))
    check(float(wall.get('stroke-width'))>width>0,'Stijenka mora ostati izvan predviđenog provrta')
    parts=subpaths(fluid)
    connected={0}
    while True:
        extra={i for i,a in enumerate(parts) if i not in connected
               and any(min(distance_to_path(p,parts[j]) for p in a)<1e-5 for j in connected)}
        if not extra:break
        connected|=extra
    check(len(connected)==len(parts),'Sve grane moraju biti stvarno povezane fluidom')
    check_uniform_fluid(fluid, 'stroke')
    return parts,width


def reservoir_wall_and_openings(root, prefix, surface_id, ports):
    """Check dry vertical walls separately, then all wetted walls and ports."""
    wet = deepcopy(root)
    surface = line(node(root, surface_id))
    y_surface = surface[0][1]
    close(surface[1][1], y_surface, 'Spremnik ima vodoravnu slobodnu površinu')
    for e in wet.iter():
        if not re.fullmatch(re.escape(prefix)+r'wall\d+', e.get('id','')):
            continue
        points = path(e)
        if points[0][1] < y_surface:
            start, end = points[:2]
            close(start[0], end[0], 'Suha stijenka spremnika mora ostati okomita')
            check(end[1] > y_surface, 'Suha stijenka nastavlja se ispod površine')
            check(any(abs(start[0]-p[0]) < 2e-5 for p in surface),
                  'Suha stijenka leži na bočnom rubu slobodne površine')
            points[0] = (start[0], y_surface)
        check(all(y >= y_surface for x,y in points),
              'Svi preostali dijelovi stijenke moraju biti omočen rub')
        e.set('d', 'M'+' L'.join(f'{x} {y}' for x,y in points))
    wall_and_openings(wet, prefix, ports)


def main():
    a=ET.parse(ROOT/'u13_fig_uvod_pregled.svg').getroot()
    b=ET.parse(ROOT/'u10_fig_uvod_pregled.svg').getroot()
    c=ET.parse(ROOT/'u13_mreze_vjezbe_skice.svg').getroot()
    for r in (a,b,c):
        ids=[e.get('id') for e in r.iter() if e.get('id')]
        check(len(ids)==len(set(ids)),'SVG ID-jevi moraju biti jedinstveni')
        check(not any(e.tag.endswith('filter') for e in r.iter()),'Nema sjena/filtra preko povezanog fluida')
    p='u13net_';parts,width=graph(a,p+'network')
    # Floor opening A must have the same bore as the pipe below it.
    left=path(node(a,p+'tankAwall0'))[-1]
    right=path(node(a,p+'tankAwall1'))[0]
    close(right[0]-left[0],width,'A: pod spremnika ne smije zatvoriti ili suziti dovod')
    close((right[0]+left[0])/2,parts[0][0][0],'A: otvor je centriran na dovod')
    HA=line(node(a,p+'surfaceA'))[0][1]
    HB=line(node(a,p+'surfaceBleft'))[0][1]
    dim=line(node(a,p+'H'))
    close(dim[0][1],HA,'H polazi od slobodne površine A')
    close(dim[1][1],HB,'H završava na slobodnoj površini B')
    outlet=parts[0][-1];tank=rect(node(a,p+'tankBfluid'))
    check(HB<outlet[1]<tank[1]+tank[3]-width/2,'B: otvor uronjen i odmaknut od dna')
    left=rect(node(a,p+'outletWall501'));right=rect(node(a,p+'outletWall525'))
    close(right[0]-(left[0]+left[2]),width,'B: dvije stijenke ostavljaju puni unutarnji otvor')
    close(left[1]+left[3],outlet[1],'B: stijenke završavaju na otvoru, ne na dnu spremnika')
    egl=path(node(a,p+'egl'))
    close(egl[0][1],HA,'EGL polazi sa slobodne površine')
    close(egl[-1][1],HB,'EGL završava na slobodnoj površini')
    check(all(y2>y1 for (_,y1),(_,y2) in zip(egl,egl[1:])),'EGL pada u smjeru toka bez stroja')

    p='u13loss_';reservoir_wall_and_openings(b,p+'pipe',p+'surface',[(340,300)])
    egl,hgl=path(node(b,p+'egl')),path(node(b,p+'hgl'))
    for e,h in zip(egl[1:],hgl):
        close(e[0],h[0],'HGL i EGL pripadaju istim presjecima')
        close(h[1]-e[1],40,'Jednaka brzinska visina u vodu stalnog promjera')
    close(hgl[-1][1],line(node(b,p+'axis'))[0][1],'Otvoreni izlaz: HGL na osi, manometarski tlak nula')
    close(egl[-1][1]+delta(node(b,p+'velocityHead'))[1],hgl[-1][1],'Na izlazu EGL ostaje iznad HGL za brzinsku visinu')
    close(delta(node(b,p+'lossHead'))[1]+delta(node(b,p+'velocityHead'))[1],
          hgl[-1][1]-line(node(b,p+'surface'))[0][1],
          'Ukupni pad geodetske visine jednak je gubitku i izlaznoj brzinskoj visini')
    profile=path(node(b,p+'laminarProfile'));yc=149;R=37
    for x,y in profile:close((x-741)/52,1-((y-yc)/R)**2,'Stvarni parabolični profil')
    for i in range(5):
        u0,u1=line(node(b,p+f'laminarVelocity{i}'))
        close(u1[0]-u0[0],52*(1-((u0[1]-yc)/R)**2),'Vektor brzine završava na stvarnom profilu')
        close(u1[1],u0[1],'Lokalna brzina paralelna stijenkama')
    for name in ('shearTop','shearBottom'):
        dx,dy=delta(node(b,p+name));check(dx<0 and dy==0,'Sile stijenke na fluid tangencijalne i suprotne toku')
    close(delta(node(b,p+'D'))[1],74,'D je razmak unutarnjih ploha')
    wall_and_openings(b,p+'elbow',[(716,339),(854,424)])
    outer=path(node(b,p+'elbowwall0'))[2:-1]
    inner=path(node(b,p+'elbowwall1'))[2:-1]
    check(len(outer)==len(inner)==91,'Provjeri cijeli luk koljena')
    for o,i in zip(outer,inner):
        close(math.dist(o,i),28,'Koljeno ima stalnu širinu normalno na os')
        close(math.dist(o,(822,371)),46,'Vanjski rub koljena je kružni luk')
        close(math.dist(i,(822,371)),18,'Unutarnji rub koljena je kružni luk')

    p='u13ex_'
    for n in range(1,7):node(c,p+f'z{n}')
    for n in (1,2):
        wall_and_openings(c,p+f'z{n}',[(46,151),(392,151)])
        close(delta(node(c,p+f'z{n}D'))[1],48,'Z1/Z2: D je unutarnji razmak')
        dim=line(node(c,p+f'z{n}L'))
        for j in (1,2):close(dim[j-1][0],line(node(c,p+f'z{n}section{j}'))[0][0],'L spaja referentne presjeke')
    parts,_=graph(c,p+'z3pipe')
    for name,x in [('A',106),('B',340)]:
        e=node(c,p+'z3'+name);point=float(e.get('cx')),float(e.get('cy'))
        close(point[0],x,'Z3: čvor je u stvarnom spoju')
        check(sum(distance_to_path(point,part)<1e-6 for part in parts)>=2,'Z3: čvor spaja dovod/odvod i oba ogranka')
    # Recover SI inputs from actual plotted q (L/s), H (m) coordinates.
    def inverse(point):return (point[0]-61)/10*1e-3,(239-point[1])/4.1
    for x,y in path(node(c,p+'z4pump')):
        Q,H=inverse((x,y));close(H,30-30000*Q*Q,'Z4: crpkina krivulja i jedinice osi',tol=1e-6)
    for x,y in path(node(c,p+'z4system')):
        Q,H=inverse((x,y));v=4*Q/(math.pi*.1**2);Re=v*.1/1e-6
        lam=((H-8)*2*9.81/v**2-6)*.1/150
        residual=1/math.sqrt(lam)+2*math.log10(.001/3.7+2.51/(Re*math.sqrt(lam)))
        check(Re>4000 and abs(residual)<2e-6,'Z4: svaka točka krivulje zatvara Colebrook i energiju')
    close(inverse((61,line(node(c,p+'z4staticHead'))[0][1]))[1],8,'Z4: stvarna statička visina 8 m')
    op=node(c,p+'z4operatingPoint');Q,H=inverse((float(op.get('cx')),float(op.get('cy'))))
    close(Q*1000,19.029644713,'Z4: nacrtano presjecište odgovara neovisnom korijenu',tol=1e-6)
    close(H,19.136178663,'Z4: visina presjecišta',tol=1e-6)
    radii=[]
    for i,D in enumerate((80,100,125)):
        e=node(c,p+f'z5bore{i}');radius=float(e.get('r'));cx=float(e.get('cx'));radii.append(radius)
        dim=line(node(c,p+f'z5D{i}'))
        close(dim[0][0],cx-radius,'Z5: prvi kraj unutarnjeg promjera')
        close(dim[1][0],cx+radius,'Z5: drugi kraj unutarnjeg promjera')
        close(radius/D,.29,'Z5: točan međusobni omjer ponuđenih promjera')
    parts,width=graph(c,p+'z6pipe');inlet=parts[0][0]
    surface=line(node(c,p+'z6surfaceLeft'))[0][1]
    tank=rect(node(c,p+'z6reservoirFluid'))
    check(surface+width/2<inlet[1]<tank[1]+tank[3]-width,
          'Z6: otvor dovoljno uronjen i ne dodiruje dno')
    S=node(c,p+'z6S');dim=line(node(c,p+'z6zs'))
    close(dim[0][1],float(S.get('cy')),'Z6: kota završava na visini referentnog usisa')
    close(dim[1][1],surface,'Z6: druga granica je slobodna površina')
    close(dim[1][1]-dim[0][1],2*38,'Z6: usisni uspon 2 m')
    left=line(node(c,p+'z6surfaceLeft'))[-1];right=line(node(c,p+'z6surfaceRight'))[0]
    outerwidth=float(node(c,p+'z6pipeouter').get('stroke-width'))
    close(right[0]-left[0],outerwidth,'Z6: slobodna površina se prekida na vanjskim stijenkama cijevi')
    print('U13 SVG PASS: 3 slike; otvoreni spojeni vodovi, uronjen usis, kote, profili, kružno koljeno, EGL/HGL i kvantitativne crpne krivulje.')


if __name__=='__main__':main()
