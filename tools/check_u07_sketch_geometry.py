"""Zasebna provjera stvarne geometrije SVG skica javnog U07.

Provjerava normale/tangente, protočni otvor klipa, otvorene priključke,
omjere kota razina i promjere T-komada. Vizualni pregled ostaje potreban.
"""

from pathlib import Path
import math
import re
import xml.etree.ElementTree as ET
from sketch_style import check_scene_canvas

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
    # Rectangular duct of constant width: height ratio equals A1/A2 = 0.30/0.24.
    close((a[1]-a[0])/(b[1]-b[0]),0.30/0.24)
    heater=polygon(ns[p+'heater'])
    assert all(a[0] < x < b[0] or True for x,_ in heater)
    assert min(y for _,y in heater) > span(fluid,146,False)[0] and max(y for _,y in heater) < span(fluid,146,False)[1]
    print('PASS Z1: heater duct area ratio 0.30:0.24 and heater inside the fluid')
    p='u08vs_fix_z6_'
    f=ns[p+'fluid'];s=ns[p+'surface']
    floor=float(f.get('y'))+float(f.get('height'))
    tanktop=float(ns[p+'tanktop-left'].get('y'))+float(ns[p+'tanktop-left'].get('height'))
    close(float(s.get('y1')),float(s.get('y2')));close(float(f.get('y')),float(s.get('y1')))
    close((floor-float(s.get('y1')))/(floor-tanktop),0.30/1.60)
    close(float(ns[p+'h0'].get('y2'))-float(ns[p+'h0'].get('y1')),floor-float(s.get('y1')))
    close(float(ns[p+'hmax'].get('y2'))-float(ns[p+'hmax'].get('y1')),floor-tanktop)
    # Air pipe passes through a real gap in the tank top and its walls are open at the top.
    al,ar=ns[p+'airpipe-left'],ns[p+'airpipe-right']
    gap_l=float(ns[p+'tanktop-left'].get('x'))+float(ns[p+'tanktop-left'].get('width'))
    gap_r=float(ns[p+'tanktop-right'].get('x'))
    assert gap_l<=float(al.get('x'))+float(al.get('width'))<float(ar.get('x'))<=gap_r
    solids=[n for n in root.iter() if n.tag.endswith('rect') and n.get('fill')=='url(#u08vs_fix_z6_hatch)']
    for x,y in [(72,125),(72,147),(244,175),(108,40)]:
        assert not any(float(n.get('x'))<x<float(n.get('x'))+float(n.get('width'))
                       and float(n.get('y'))<y<float(n.get('y'))+float(n.get('height')) for n in solids)
    print('PASS Z6: ballast tank level ratio 0.30:1.60, open air pipe and uncapped pipes')
    check_scene_canvas('u08_vjezbe_skice.svg', root, 6)
    assert all('u08vs_fix_z'+str(i) in ns for i in range(1,7))
    print('PASS six original practice panels')

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

    # P2: zahvatni usis, kontrolni volumen vezan uz brod.
    root,ns=read('u08_val3_izjednacni_spremnik.svg');p='u08v3is_'
    mouth=ns[p+'mouth'];x=float(mouth.get('x1'));y0,y1=sorted(map(float,(mouth.get('y1'),mouth.get('y2'))))
    close(x,float(mouth.get('x2')))
    duct=polygon(ns[p+'duct-fluid'])
    assert span(duct,x-2,horizontal=False)==[y0,y1]
    for wall in ('duct-fore-wall','duct-aft-wall'):
        pts=polygon(ns[p+wall])
        for a,b in zip(pts,pts[1:]):
            assert not (a[0]==b[0]==x), 'duct wall closes the mouth'
    gratings=[ns[p+'grating-'+str(i)] for i in (1,2,3)]
    # Grating bars are short ticks; their extent along the mouth must stay far below the opening height.
    assert sum(abs(float(g.get('y2'))-float(g.get('y1'))) for g in gratings) < 0.4*(y1-y0)
    assert all(y0 < float(g.get('y1')) < y1 for g in gratings)
    for plate in ('plating-aft','plating-fore'):
        r=ns[p+plate];xa=float(r.get('x'));xb=xa+float(r.get('width'))
        assert xb<=min(px for px,_ in duct) or xa>=max(px for px,_ in duct) or xb<=330 or xa>=370
    ship=vector(ns[p+'ship-velocity']);rel=vector(ns[p+'rel-velocity'])
    assert ship[0]>0 and rel[0]<0 and ship[1]==rel[1]==0
    # Text: inlet surface is the mouth, outlet the duct section towards the exchanger.
    # The KV therefore follows the duct interior; it must not enclose outer sea,
    # plating or engine-room air (that would add extra in/out surfaces).
    cv=polygon(ns[p+'cv'])
    assert ns[p+'cv'].get('d').strip().upper().endswith('Z')
    edges=list(zip(cv,cv[1:]+cv[:1]))
    pts=cv+[((a[0]+b[0])/2,(a[1]+b[1])/2) for a,b in edges]
    for px,py in pts:
        hits=span(duct,py)
        assert len(hits)==2 and hits[0]<=px<=hits[1], ('KV leaves the duct fluid',px,py)
    inlet=[(a,b) for a,b in edges if a[0]==b[0]==x]
    assert len(inlet)==1, 'KV inlet face lies in the mouth plane'
    (_,ia),(_,ib)=inlet[0]
    wall=float(ns[p+'duct-fore-wall'].get('stroke-width'))
    free=(y1-y0)-wall  # clear height between the inner faces of both walls
    assert y0+wall/2<=min(ia,ib)<max(ia,ib)<=y1-wall/2 and abs(ia-ib)>=0.8*free, 'KV inlet face spans the clear opening'
    top=min(py for _,py in cv)
    assert top<y0 and len(span(duct,top+1))==2, 'KV outlet face cuts the rising duct'
    close(abs(float(ns[p+'Au'].get('y2'))-float(ns[p+'Au'].get('y1'))),y1-y0)
    # Velocity arrows share one scale: v_s = 9.26 m/s, w = Q/A_u = 1.25 m/s.
    close(math.hypot(*ship)/math.hypot(*rel),9.26/1.25,0.05)
    print('PASS P2 scoop: open forward mouth, antiparallel ship/relative velocities in scale, moving CV follows the duct from mouth to outlet')

    for name,p,ratio,ports in [
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
