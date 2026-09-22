"""Provjera stvarnih SVG presjeka, povezanosti i kvantitativnih grafova U11.

Čita objavljene datoteke; nije ovisna o privremenom autorskom generatoru.
Ne zamjenjuje vizualni pregled oznaka i pedagošku procjenu.
"""
from pathlib import Path
import math
import xml.etree.ElementTree as ET

from check_u10_sketch_geometry import (
    check, node, path, line, delta, distance_to_path, wall_and_openings,
)

ROOT = Path(__file__).resolve().parents[1] / 'assets' / 'print'


def svg(name):
    return ET.parse(ROOT / name).getroot()


def close(a, b, message, tol=2e-5):
    check(math.isclose(a, b, rel_tol=tol, abs_tol=tol), message)


def rect(e):
    return tuple(float(e.get(k)) for k in ('x', 'y', 'width', 'height'))


def points(e):
    return [tuple(map(float, p.split(','))) for p in e.get('points').split()]


def diameter(root, circle_id, dim_id, vertical):
    body = node(root, circle_id)
    cx, cy, radius = (float(body.get(k)) for k in ('cx', 'cy', 'r'))
    a, b = line(node(root, dim_id))
    if vertical:
        close(a[0], b[0], dim_id + ': promjer mora biti poprečan toku')
        close(a[1], cy-radius, dim_id + ': prvi kraj promjera')
        close(b[1], cy+radius, dim_id + ': drugi kraj promjera')
    else:
        close(a[1], b[1], dim_id + ': pravac kote')
        close(a[0], cx-radius, dim_id + ': prvi kraj promjera')
        close(b[0], cx+radius, dim_id + ': drugi kraj promjera')


def pipe_rect(root, prefix, dimension):
    x,y,w,h = rect(node(root,prefix+'fluid'))
    top, bottom = rect(node(root,prefix+'top')), rect(node(root,prefix+'bottom'))
    close(top[1]+top[3],y,prefix+': gornja stijenka na rubu fluida')
    close(bottom[1],y+h,prefix+': donja stijenka na rubu fluida')
    check(top[0]==bottom[0]==x and top[2]==bottom[2]==w,prefix+': isti otvoreni raspon')
    a,b=line(node(root,dimension))
    close(a[1],y,dimension+': unutarnji promjer, gornji kraj')
    close(b[1],y+h,dimension+': unutarnji promjer, donji kraj')


def circulation(root, prefix, count):
    previous = None
    for i in range(count):
        e=node(root,prefix+str(i));xy=points(e)
        # Signed polygon area of the nearly complete circular arc measures
        # rotation independently of the author's sampled angle convention.
        area=sum(a[0]*b[1]-b[0]*a[1] for a,b in zip(xy,xy[1:]+xy[:1]))
        check(area>0 if i%2==0 else area<0,prefix+': gornji vrtlog udesno, donji suprotno')
        check(e.get('marker-end') is not None,prefix+': nedostaje tangencijalni smjer')
        if previous is not None:check(area*previous<0,prefix+': izmjenična vrtnja')
        previous=area


def main():
    r=svg('u14_fig_uvod_pregled.svg')
    walls=path(node(r,'u14fup_tunnelwalls'))
    check(walls==[(680,150),(936,150),(680,290),(936,290)],'Aerotunel: samo pod i strop, bez čelnih pregrada')
    wheels=[e for e in r.iter() if e.tag.endswith('circle')]
    for wheel in wheels:close(float(wheel.get('cy'))+float(wheel.get('r')),290,'Kotači moraju dodirivati pod')

    r=svg('u14_val1_reynolds_kanal.svg')
    for n in (1,2):pipe_rect(r,f'u14re_p{n}',f'u14re_p{n}D')
    xy=points(node(r,'u14re_oilprofile'))
    x_origin=xy[0][0];yc=(xy[0][1]+xy[-1][1])/2;radius=(xy[-1][1]-xy[0][1])/2
    umax=max(x for x,y in xy)-x_origin
    for x,y in xy:close((x-x_origin)/umax,1-((y-yc)/radius)**2,'Ulje: parabolični profil s prianjanjem')
    close(xy[-1][0],x_origin,'Ulje: u=0 na obje stijenke')
    for i in range(5):
        a,b=line(node(r,f'u14re_oilvelocity{i}'))
        close(a[1],b[1],'Lokalna brzina mora biti aksijalna')
        close((b[0]-a[0])/umax,1-((a[1]-yc)/radius)**2,'Lokalna brzina mora završiti na profilu')

    r=svg('u14_val2_brod_bazen.svg');normal=[]
    for prefix in ('p','m'):
        hull=path(node(r,'u14ship_'+prefix+'hull'));a,b=line(node(r,'u14ship_'+prefix+'length'))
        span=max(x for x,y in hull)-min(x for x,y in hull)
        close(b[0]-a[0],span,'Brod: kota odgovara cijeloj duljini trupa')
        normal.append([((x-hull[0][0])/span,(y-hull[0][1])/span) for x,y in hull])
        fluid=path(node(r,'u14ship_'+prefix+'fluid'))
        # Both underwater corners belong to the same connected water boundary.
        for corner in hull[2:4]:close(distance_to_path(corner,fluid),0,'Brod: nema vode kroz uronjeni trup')
        for suffix in ('freeleft','freeright'):
            surface=line(node(r,'u14ship_'+prefix+suffix))
            close(surface[0][1],surface[1][1],'Brod: vodoravna slobodna površina')
            endpoint=surface[1] if suffix=='freeleft' else surface[0]
            close(distance_to_path(endpoint,hull),0,'Površina mora stati na vanjskoj stijenci trupa')
    for a,b in zip(*normal):
        close(a[0],b[0],'Geometrijska sličnost trupova x');close(a[1],b[1],'Geometrijska sličnost trupova y')

    r=svg('u14_val3_venturi_kavitacija.svg');prefix='u14vent_'
    wall_and_openings(r,prefix+'pipe',[(80,150),(820,150)])
    top=path(node(r,prefix+'pipewall0'));bottom=path(node(r,prefix+'pipewall1'))
    for name in ('D1','D2'):
        a,b=line(node(r,prefix+name))
        if name=='D2':
            close(distance_to_path(a,top),0,'Venturi: kota grla mora biti u grlu')
            close(distance_to_path(b,bottom),0,'Venturi: kota grla mora dosegnuti obje unutarnje stijenke')
    close(delta(node(r,prefix+'D1'))[1]/delta(node(r,prefix+'D2'))[1],3,'Venturi: omjer promjera 3:1')
    for name in ('validleft','invalid','validright'):
        e=node(r,prefix+name)
        check(bool(e.get('stroke-dasharray'))==(name=='invalid'),'Neostvariv tlak mora biti jasno isprekidan')
        for x,y in points(e):
            # Interpolate the actual wall polyline at the graph's x position.
            def ordinate(poly):
                for a,b in zip(poly,poly[1:]):
                    if a[0]-1e-5<=x<=b[0]+1e-5:return a[1]+(b[1]-a[1])*(x-a[0])/(b[0]-a[0])
                raise AssertionError('Graf izvan geometrije')
            d=(ordinate(bottom)-ordinate(top))*.060/120
            velocity=.006/(math.pi*d*d/4)
            p_abs=101300+1000/2*((.006/(math.pi*.060**2/4))**2-velocity**2)
            plotted=(370-y)/.55*1000
            check(abs(plotted-p_abs)<.03,'Venturi: krivulja mora zadovoljiti kontinuitet i Bernoulli do 0,03 Pa')
            check(p_abs<=2340+.02 if name=='invalid' else p_abs>=2340-.02,'Krivulja pogrešno razvrstana prema tlaku pare')
    a,b=line(node(r,prefix+'v2'));check(360<a[0]<b[0]<520 and a[1]==b[1]==150,'v₂ mora biti u osi grla')

    r=svg('u14_val4_kap_raspad.svg');diameter(r,'u14drop_drop','u14drop_diameter',True)
    check(not any('forceMarker' in e.get('marker-end','') for e in r.iter()),'Kap: površinska napetost nije radijalna sila')

    r=svg('u14_ch1_kugla_struja.svg');diameter(r,'u14ball_sphere','u14ball_diameter',False)
    check(delta(node(r,'u14ball_drag'))[0]>0 and delta(node(r,'u14ball_drag'))[1]==0,'Otpor kugle mora biti u smjeru struje')
    for x,y in points(node(r,'u14ball_correlation')):
        re=10**(2+4*(x-540)/(918-540));cd_plot=10**(-1+2*(373-y)/(373-123))
        check(100-1e-4<=re<=2e5+1,'Korelacija ne smije ući u izostavljeno područje krize otpora')
        cd=24/re*(1+.15*re**.687)+.42/(1+4.25e4/re**1.16)
        close(cd_plot,cd,'Cᴅ: logaritamske osi i zadana korelacija',tol=1e-6)
    e=node(r,'u14ball_givenpoint')
    close(10**(2+4*(float(e.get('cx'))-540)/378),4e4,'P5: zasebna zadana radna točka Re')
    close(10**(-1+2*(373-float(e.get('cy')))/250),.45,'P5: zadani Cᴅ ne smije biti zamijenjen korelacijom')

    r=svg('u14_val5_mach_strouhal.svg')
    pipe_rect(r,'u14ma_duct','u14ma_diameter');diameter(r,'u14ma_cylinder','u14ma_chimneyd',True);circulation(r,'u14ma_wake',5)

    r=svg('u14_vjezbe_skice.svg')
    for n in range(1,7):node(r,f'u14vs_z{n}')
    for p in ('a','v'):diameter(r,f'u14vs_{p}fluid',f'u14vs_{p}diameter',False)
    pipe_rect(r,'u14vs_z2pipe','u14vs_z2D')
    wall_and_openings(r,'u14vs_z3pipe',[(28,172),(264,172)])
    # The pressure port is intentionally narrower than a main-flow opening.
    # Its actual clear width must exceed both wall half-strokes.
    walls=[node(r,f'u14vs_z3pipewall{i}') for i in range(3)]
    for w in walls:
        check(distance_to_path((170,120),path(w))>float(w.get('stroke-width'))/2,
              'Tlačni priključak: stijenke ne smiju zatvarati otvor senzora')
    fluid=path(node(r,'u14vs_z3pipefluid'))
    check(distance_to_path((170,147),fluid)>=5,'Tlačni priključak mora imati otvor u gornjoj stijenci')
    forms=[]
    for p in ('p','m'):
        f=path(node(r,f'u14vs_{p}foil'));a,b=line(node(r,f'u14vs_{p}chord'));chord=b[0]-a[0]
        close(chord,max(x for x,y in f)-min(x for x,y in f),'Hidroprofil: kota tetive')
        forms.append([((x-f[0][0])/chord,(y-f[0][1])/chord) for x,y in f])
    for a,b in zip(*forms):
        close(a[0],b[0],'Hidroprofil: sličnost x');close(a[1],b[1],'Hidroprofil: sličnost debljine')
    close(delta(node(r,'u14vs_pchord'))[0]/delta(node(r,'u14vs_mchord'))[0],3,'Hidroprofil: isto grafičko mjerilo 3:1')
    diameter(r,'u14vs_z5cylinder','u14vs_z5D',True);circulation(r,'u14vs_z5wake',4)
    geometry=[]
    for p,lam in [('a',20),('b',30)]:
        x,y,w,h=rect(node(r,f'u14vs_{p}water'));geometry.append((w,h))
        l=rect(node(r,f'u14vs_{p}leftwall'));rr=rect(node(r,f'u14vs_{p}rightwall'));bed=rect(node(r,f'u14vs_{p}bed'))
        close(l[0]+l[2],x,'Kanal: lijeva stijenka izvan fluida');close(rr[0],x+w,'Kanal: desna stijenka izvan fluida');close(bed[1],y+h,'Kanal: dno na granici')
        close(delta(node(r,f'u14vs_{p}depth'))[1],h,'Kanal: kota dubine');close(delta(node(r,f'u14vs_{p}width'))[0],w,'Kanal: kota širine')
        depth_m=7.5/lam;width_m=w/h*depth_m
        flow=6/math.sqrt(lam)*width_m*depth_m
        close(flow,480/lam**2.5,'Presjek modela mora zadovoljiti kontinuitet i Froudeovo skaliranje',tol=1e-10)
    close(geometry[0][0]/geometry[1][0],1.5,'Dva kanala: omjer širina');close(geometry[0][1]/geometry[1][1],1.5,'Dva kanala: omjer dubina')
    print('PASS U11: devet izmijenjenih SVG-ova; otvoreni prolazi, povezani fluidi, geometrijska sličnost, stvarne kote, profili, vektori i kvantitativni grafovi.')


if __name__ == '__main__':
    main()
