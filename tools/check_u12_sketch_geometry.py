"""Provjera stvarnih SVG-ova U12: stijenke, priključci, kote i grafovi.

Čita objavljene geometrije, ne privremeni generator. Ne zamjenjuje
vizualni pregled ni neovisni numerički verifier zadataka.
"""
import math
from pathlib import Path
import xml.etree.ElementTree as ET

from check_u10_sketch_geometry import (
    check, node, path, line, delta, distance_to_path, wall_and_openings,
)

ROOT = Path(__file__).resolve().parents[1] / 'assets' / 'print'


def close(a, b, message, tol=2e-5):
    check(abs(a-b) <= tol, message)


def rect(element):
    return tuple(float(element.get(k)) for k in ('x', 'y', 'width', 'height'))


def plate_gap(root, prefix, dimension):
    x,y,w,h = rect(node(root,prefix+'fluid'))
    top, bottom = rect(node(root,prefix+'top')),rect(node(root,prefix+'bottom'))
    check(top[0] == bottom[0] == x and top[2] == bottom[2] == w,
          prefix+': ploče moraju pokrivati isti razmak, bez čelnih pregrada')
    close(top[1]+top[3],y,prefix+': gornji rub fluida dodiruje ploču')
    close(bottom[1],y+h,prefix+': donji rub fluida dodiruje ploču')
    a,b=line(node(root,dimension))
    close(a[0],b[0],dimension+': kota je normalna na ploče')
    close(a[1],y,dimension+': gornji kraj je unutarnja ploha')
    close(b[1],y+h,dimension+': donji kraj je unutarnja ploha')


def main():
    intro=ET.parse(ROOT/'u12_fig_uvod_realni_tok.svg').getroot()
    tasks=ET.parse(ROOT/'u12_realni_tok_vjezbe_skice.svg').getroot()
    for root in (intro,tasks):
        ids=[e.get('id') for e in root.iter() if e.get('id')]
        check(len(ids)==len(set(ids)), 'Duplicirani SVG ID')
        check(not any(e.tag.endswith('filter') for e in root.iter()),'Nema sjena ni filtara')
        for e in root.iter():
            if e.get('id','').lower().endswith('fluid'):
                check(e.get('stroke')=='none','Fluid nije omeđen lažnom krutom stijenkom')
                if e.tag.endswith('path'):
                    check(e.get('d').count('M')==1 and e.get('d').count('Z')==1,
                          'Jedna povezana ispuna za svaki povezani fluid')
                grad=node(root,e.get('fill')[5:-1])
                check(grad.get('x1')==grad.get('x2')
                      and grad.get('gradientUnits')=='userSpaceOnUse',
                      'Vertikalni prostorni gradijent bez skoka boje na priključcima')
    p='u12rt_'
    element=node(intro,p+'element')
    check(element.get('stroke-dasharray') is not None,'Zamišljeni element nije kruti spremnik')
    for name,sign in [('pressureLeft',1),('pressureRight',-1),('shearTop',1),('shearBottom',-1)]:
        e=node(intro,p+name);dx,dy=delta(e)
        check(sign*dx>0 and dy==0,name+': ispravne x-komponente naprezanja')
        marker_id=e.get('marker-end')[5:-1]
        marker=node(intro,marker_id)
        arrow_head=next(k for k in marker if k.tag.endswith('path'))
        check(arrow_head.get('fill')==e.get('stroke'),name+': glava i tijelo iste boje')
    corners=path(element)
    close(delta(node(intro,p+'dx'))[0],corners[1][0]-corners[0][0],'dx mjeri element')
    close(delta(node(intro,p+'dy'))[1],corners[2][1]-corners[1][1],'dy mjeri element')
    fluid=rect(node(intro,p+'layerFluid'));plate=rect(node(intro,p+'plate'))
    close(fluid[1]+fluid[3],plate[1],'Nema praznine između sloja i stijenke')
    curve=node(intro,p+'deltaCurve');points=path(curve)
    check(curve.get('fill')=='none' and bool(curve.get('stroke-dasharray')),
          'Debljina je unutarnja oznaka, a ne granica dvaju fluida')
    x0,y0=points[0];length=points[-1][0]-x0;depth=y0-points[-1][1]
    for x,y in points:
        close((y0-y)/depth,math.sqrt((x-x0)/length),'Laminarna debljina raste kao korijen iz x')
    a,b=line(node(intro,p+'delta'))
    close(b[1],plate[1],'Debljina počinje na stijenci')
    close((y0-a[1])/depth,math.sqrt((a[0]-x0)/length),'Kota završava na krivulji debljine')
    xdim=line(node(intro,p+'layerX'))
    close(xdim[0][0],x0,'x počinje na prednjem rubu ploče')
    close(xdim[1][0],a[0],'x i debljina odnose se na isti presjek')
    signal=path(node(intro,p+'signal'))
    # Exact integral of the plotted piecewise-linear signal over its displayed time.
    mean_y=sum((a[1]+b[1])/2*(b[0]-a[0]) for a,b in zip(signal,signal[1:]))/(signal[-1][0]-signal[0][0])
    mean_line=line(node(intro,p+'signalMean'))
    close(mean_y,mean_line[0][1],'U mora biti stvarna srednja vrijednost prikazane krivulje')
    close(mean_line[0][1],160,'Označena srednja brzina odgovara osi 8 m/s')
    check(all(signal[i+1][0]>signal[i][0] for i in range(len(signal)-1)),'Vrijeme mora rasti udesno')
    p='u12vs_'
    for n in range(1,7):node(tasks,p+f'z{n}')
    arrows=[line(node(tasks,p+f'z1velocity{i}')) for i in range(3)]
    # Coordinate tick spacing is 100 px/m, while velocity has its own scale.
    for i,(a,b) in enumerate(arrows):
        x=(a[0]-arrows[0][0][0])/100
        close((b[0]-a[0])/16,2*2+x*x,'Z1: lokalne brzine moraju slijediti at+bx²')
        close(a[1],b[1],'Z1: aksijalne brzine')
    dim=line(node(tasks,p+'z1x'));A=node(tasks,p+'z1A')
    close(dim[0][0],arrows[0][0][0],'Z1: početak kote x=0')
    close(dim[1][0],float(A.get('cx')),'Z1: kraj kote je položaj A')
    close(dim[1][0]-dim[0][0],100,'Z1: zadani 1 metar')
    for n in (2,4):
        plate_gap(tasks,p+f'z{n}',p+f'z{n}H')
        dx,dy=delta(node(tasks,p+f'z{n}plateVelocity'))
        check(dx>0 and dy==0,f'Z{n}: ploča klizi, ne prodire u fluid')
    check(delta(node(tasks,p+'z4pressureDrive'))[0]<0,'Z4: nepovoljan tlak pokreće suprotno ploči')
    wall_and_openings(tasks,p+'z3',[(43,158),(392,158)])
    walls=[node(tasks,p+f'z3wall{i}') for i in range(4)]
    fluid=path(node(tasks,p+'z3fluid'))
    sensors=[]
    for i in (1,2):
        x,y,w,h=rect(node(tasks,p+f'z3sensor{i}'));cx=x+w/2
        sensors.append(cx)
        close(y+h,92,'Z3: zatvoreni senzor naliježe na vrh ogranka')
        for z in (100,120,136):
            check(all(distance_to_path((cx,z),path(wall))>float(wall.get('stroke-width'))/2 for wall in walls),
                  'Z3: tlačni priključak mora ostati stvarno otvoren')
            check(distance_to_path((cx,z),fluid)>=4.9,'Z3: neprekinuta fluidna veza s cijevi')
    dim=line(node(tasks,p+'z3L'))
    check([a[0] for a in dim]==sensors,'Z3: L mjeri razmak priključaka, ne cijelu cijev')
    a,b=line(node(tasks,p+'z3D'))
    close(a[0],b[0],'Z3: unutarnji promjer normalan na os')
    close(b[1]-a[1],44,'Z3: promjer odgovara unutarnjoj širini')
    p5=rect(node(tasks,p+'z5plate'));f5=rect(node(tasks,p+'z5fluid'))
    close(f5[1]+f5[3],p5[1],'Z5: fluid dodiruje nominalnu plohu')
    section=line(node(tasks,p+'z5section'));dim=line(node(tasks,p+'z5x'))
    close(dim[0][0],p5[0],'Z5: kota počinje na prednjem rubu')
    close(dim[1][0],section[0][0],'Z5: kota završava u promatranom presjeku')
    previous=None
    for j in range(3):
        x,y,w,h=rect(node(tasks,p+f'z6domain{j}'))
        lines=[e for e in tasks.iter() if e.get('id','').startswith(p+f'z6grid{j}v')]
        horizontals=[e for e in tasks.iter() if e.get('id','').startswith(p+f'z6grid{j}h')]
        locations=sorted(float(e.get('x1')) for e in lines)
        rows=sorted(float(e.get('y1')) for e in horizontals)
        check(all(e.get('stroke-dasharray') for e in lines+horizontals),'Z6: numeričke mreže se razlikuju od stijenki')
        step=locations[1]-locations[0]
        close(rows[1]-rows[0],step,'Z6: isti korak u oba smjera')
        check(all(abs(b-a-step)<1e-12 for a,b in zip(locations,locations[1:])),'Z6: pravilni koraci mreže')
        close(locations[0],x,'Z6: rub domene');close(locations[-1],x+w,'Z6: isti cijeli raspon')
        if previous:
            close(previous[0],w,'Z6: ne mijenjaj fizičku duljinu domene')
            close(previous[1],h,'Z6: ne mijenjaj fizičku širinu domene')
            close(previous[2]/step,2,'Z6: oba koraka se prepolavljaju')
        previous=w,h,step
    print('U12 SVG PASS: 2 slike; povezan fluid, otvoreni priključci, nepropusne ploče, kote, smjerovi, rast sloja, srednji signal i pročišćenje mreže.')


if __name__=='__main__':
    main()
