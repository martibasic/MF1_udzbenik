"""Zasebna provjera stvarne geometrije SVG skica javnog U07.

Provjerava normale/tangente, protočni otvor klipa, otvorene priključke,
omjere kota razina i promjere T-komada. Vizualni pregled ostaje potreban.
"""

from pathlib import Path
import math
import re
import xml.etree.ElementTree as ET

ASSETS = Path(__file__).resolve().parent.parent / 'assets/print'


def read(name):
    root = ET.parse(ASSETS/name).getroot()
    nodes = [n for n in root.iter() if n.get('id')]
    assert len(nodes) == len({n.get('id') for n in nodes})
    return root, {n.get('id'): n for n in nodes}


def close(a,b,tol=1e-8):
    assert abs(a-b) < tol, (a,b)


def vector(n):
    return float(n.get('x2'))-float(n.get('x1')), float(n.get('y2'))-float(n.get('y1'))


def polygon(n):
    """Read the actual absolute M/L/H/V/Z paths used by these fluid domains."""
    tokens = re.findall(r'[MLHVZ]|-?\d+(?:\.\d+)?',n.get('d'))
    result=[];x=y=0;i=0
    while i < len(tokens):
        cmd=tokens[i];i+=1
        if cmd in ('M','L'):
            x,y=map(float,tokens[i:i+2]);i+=2
        elif cmd=='H': x=float(tokens[i]);i+=1
        elif cmd=='V': y=float(tokens[i]);i+=1
        elif cmd=='Z': break
        else: raise ValueError(cmd)
        result.append((x,y))
    return result


def span(poly,coord,horizontal=True):
    # Intersections with a horizontal/vertical interior slice of a polygon.
    pts=poly if horizontal else [(y,x) for x,y in poly]
    hits=[]
    for (x,y),(u,v) in zip(pts,pts[1:]+pts[:1]):
        if min(y,v) < coord < max(y,v):
            hits.append(x+(u-x)*(coord-y)/(v-y))
    return sorted(hits)


def main():
    root,ns=read('u08_vjezbe_skice.svg');p='u08vs_fix_z2_'
    normal,plane,vel=[vector(ns[p+k]) for k in ('normal-vector','plane','velocity')]
    close(sum(a*b for a,b in zip(normal,plane)),0,1e-7)
    close(sum(a*b for a,b in zip(normal,vel))/(math.hypot(*normal)*math.hypot(*vel)),.5)
    assert vel[0] > 0 and normal[0] > 0
    print('PASS Z2: plane perpendicular to normal, velocity at 60 degrees')
    p='u08vs_fix_z5_'
    top,bottom=ns[p+'piston-top'],ns[p+'piston-bottom']
    y0=float(top.get('y'));yt=y0+float(top.get('height'))
    yb=float(bottom.get('y'));y1=yb+float(bottom.get('height'))
    close((yb-yt)/(y1-y0),20/100)
    fluid=polygon(ns[p+'fluid'])
    assert span(fluid,185,horizontal=False)==[yt,yb]
    assert span(fluid,100,horizontal=False)==[y0,y1]
    assert top.get('x') == bottom.get('x')
    print('PASS Z5: real central opening, d/D=0.2, sealed annular piston')
    p='u08vs_fix_z1_';fluid=polygon(ns[p+'fluid'])
    a=span(fluid,60,False);b=span(fluid,240,False)
    close((a[1]-a[0])/(b[1]-b[0]),100/160)
    assert root.get('viewBox')=='0 0 960 720'
    assert all('u08vs_fix_z'+str(i) in ns for i in range(1,7))
    print('PASS Z1 diameters and six original practice panels')

    _,ns=read('u08_fig_t_komad_hidraulika.svg');p='u08ftkh_fix_'
    fluid=polygon(ns[p+'fluid'])
    inlet=span(fluid,80,False);up=span(fluid,121);down=span(fluid,419)
    close(inlet[1]-inlet[0],48);close(up[1]-up[0],30);close(down[1]-down[0],37.2)
    # All three ports lie between endpoints of separate wall paths; no cap.
    walls=[polygon(ns[p+'wall-'+str(i)]) for i in range(3)]
    for wall in walls:
        for a,b in zip(wall,wall[1:]):
            assert not (a[0]==b[0]==65 and min(a[1],b[1])<270<max(a[1],b[1]))
            assert not (a[1]==b[1]==120 and min(a[0],b[0])<287<max(a[0],b[0]))
            assert not (a[1]==b[1]==420 and min(a[0],b[0])<285<max(a[0],b[0]))
    print('PASS T-piece: three open ports and 32:20:24.8 diameter ratio')

    for name,p,ratio,ports in [
        ('u08_val3_izjednacni_spremnik.svg','u08v3is_fix_',.45/1.20,[(105,150),(495,415)]),
        ('u08_ch1_mijesajuci_spremnik.svg','u08c1ms_fix_',.80/1.20,[(205,335),(205,380),(535,380)]),
    ]:
        root,ns=read(name);f=ns[p+'fluid'];s=ns[p+'surface'];t=ns[p+'target']
        close(float(s.get('y1')),float(s.get('y2')))
        close(float(t.get('y1')),float(t.get('y2')))
        floor=float(f.get('y'))+float(f.get('height'))
        close((floor-float(s.get('y1')))/(floor-float(t.get('y1'))),ratio)
        # Future rise lies above the sole tank fill, not in a second fluid layer.
        close(float(f.get('y')),float(s.get('y1')))
        solids=[n for n in root.iter() if n.tag.endswith('rect') and n.get('fill')==f'url(#{p}hatch)']
        for x,y in ports:
            assert not any(float(n.get('x'))<x<float(n.get('x'))+float(n.get('width'))
                           and float(n.get('y'))<y<float(n.get('y'))+float(n.get('height')) for n in solids)
        print('PASS',name,'level ratio, one tank fill, uncapped wall openings')

    _,ns=read('u08_fig_kinematika.svg');pts=polygon(ns['u08fk_streamline'])
    for i in range(4):
        n=ns['u08fk_tangent'+str(i)];x=float(n.get('x1'));y=float(n.get('y1'))
        a,b=next((a,b) for a,b in zip(pts,pts[1:]) if a[0]<=x<=b[0])
        slope=(b[1]-a[1])/(b[0]-a[0]);close(y,a[1]+slope*(x-a[0]))
        dx,dy=vector(n);close(dy,slope*dx)
    print('PASS kinematics: all four velocities tangent to the actual drawn curve')


if __name__=='__main__':
    main()
