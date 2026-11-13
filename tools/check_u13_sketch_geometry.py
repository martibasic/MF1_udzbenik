"""Čita četiri stvarna SVG-a U13: topologija toka, petlja, kote, profili i prizori vježbi.

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


def inside(point,poly):
    """Točka unutar zatvorenog poligona (pravilo parnosti presjeka)."""
    x,y=point;hit=False
    for (x0,y0),(x1,y1) in zip(poly,poly[1:]):
        if (y0>y)!=(y1>y) and x<x0+(y-y0)*(x1-x0)/(y1-y0):hit=not hit
    return hit


def ground_y(ground,x):
    for (x0,y0),(x1,y1) in zip(ground,ground[1:]):
        if min(x0,x1)<=x<=max(x0,x1) and x1!=x0:
            return y0+(y1-y0)*(x-x0)/(x1-x0)
    return None


def sample(points,step=2.0):
    out=[]
    for a,b in zip(points,points[1:]):
        n=max(1,int(math.dist(a,b)/step))
        out+=[(a[0]+(b[0]-a[0])*i/n,a[1]+(b[1]-a[1])*i/n) for i in range(n+1)]
    return out


def submerged(end,fluid_poly,surface_y,bore,message):
    check(inside(end,fluid_poly),message+': kraj cijevi leži u fluidu')
    check(end[1]-surface_y>=bore,message+': kraj je uronjen ispod slobodne površine')
    bottom=max(y for _,y in fluid_poly)
    check(bottom-end[1]>=bore,message+': kraj je odmaknut od dna')


def above_ground(c,pipe_id,ground_ids,outer,message):
    pts=[pt for part in subpaths(node(c,pipe_id+'fluid')) for pt in sample(part)]
    for gid in ground_ids:
        g=path(node(c,gid))
        for x,y in pts:
            yg=ground_y(g,x)
            if yg is not None and not (x in (g[0][0],g[-1][0])):
                check(y+outer/2<=yg+0.6,message+f': vod ne smije prolaziti kroz tlo ({x:.0f}, {y:.0f})')


def on_pipe(c,pipe_id,point,message):
    parts=subpaths(node(c,pipe_id+'fluid'))
    check(min(distance_to_path(point,part) for part in parts)<0.02,message)


def labels_clear(c,group,pipe_id,outer,message):
    parts=subpaths(node(c,pipe_id+'fluid'))
    for t in node(c,group).iter():
        if t.tag.endswith('text') and t.get('x'):
            pt=(float(t.get('x')),float(t.get('y')))
            check(all(distance_to_path(pt,part)>outer/2 for part in parts),
                  message+': oznaka ne leži na vodu: '+''.join(t.itertext()))


def circle_centre(e):return float(e.get('cx')),float(e.get('cy'))


def check_exercise_scenes(c,p):
    """Prizori Z1, Z2, Z4, Z5 i Z6: otvoreni uronjeni krajevi, tok iznad tla i razine."""
    # Z1: jezero -> crpka -> uz brdo do kuća; točka 2 na vodu.
    parts,bore=graph(c,p+'z1pipe');outer=float(node(c,p+'z1pipeouter').get('stroke-width'))
    lake=path(node(c,p+'z1lake'));ys=line(node(c,p+'z1lakeSurface'))[0][1]
    close(min(y for _,y in lake),ys,'Z1: slobodna površina jezera je gornji rub vode')
    submerged(parts[0][0],lake,ys,bore,'Z1 usis')
    above_ground(c,p+'z1pipe',[p+'z1ground'],outer,'Z1')
    on_pipe(c,p+'z1pipe',circle_centre(node(c,p+'z1point2')),'Z1: točka 2 leži na osi voda')
    on_pipe(c,p+'z1pipe',circle_centre(node(c,p+'z1pumpSymbol')),'Z1: crpka leži na vodu')
    check(node(c,p+'z1pumpSymbol').get('fill')=='none','Z1: simbol crpke ne zatvara vod')
    check(circle_centre(node(c,p+'z1point2'))[1]<ys,'Z1: točka 2 je iznad razine jezera')
    a,b=line(node(c,p+'z1velocity'));seg=(parts[0][2],parts[0][3])
    angle=lambda u,v:math.atan2(v[1]-u[1],v[0]-u[0])
    check(abs(angle(a,b)-angle(*seg))<math.radians(0.5) and (b[0]-a[0])>0,
          'Z1: strelica protoka usporedna je s vodom uz brdo i pokazuje prema kućama')
    labels_clear(c,p+'z1',p+'z1pipe',outer,'Z1')

    # Z2: ulje iz donjeg u gornji spremnik; oba kraja uronjena.
    parts,bore=graph(c,p+'z2pipe');outer=float(node(c,p+'z2pipeouter').get('stroke-width'))
    low=path(node(c,p+'z2lowfluid'));up=path(node(c,p+'z2upfluid'))
    yl=line(node(c,p+'z2lowsurface'))[0][1];yu=line(node(c,p+'z2upsurface'))[0][1]
    submerged(parts[0][0],low,yl,bore,'Z2 usis')
    submerged(parts[0][-1],up,yu,bore,'Z2 izlaz')
    for t in ('low','up'):
        wall_and_openings_free(c,p+'z2'+t)
    dim=line(node(c,p+'z2dz'))
    close(dim[0][1],yu,'Z2: Δz počinje na slobodnoj površini taložnog tanka')
    close(dim[1][1],yl,'Z2: Δz završava na slobodnoj površini donjeg spremnika')
    on_pipe(c,p+'z2pipe',circle_centre(node(c,p+'z2pumpSymbol')),'Z2: crpka leži na vodu')
    check(node(c,p+'z2pipefluid').get('stroke')=='#eadfc5','Z2: vod je ispunjen istim uljem kao spremnici')
    labels_clear(c,p+'z2',p+'z2pipe',outer,'Z2')

    # Z4: jezero -> crpka -> vodosprema; izlaz uronjen, vod iznad tla i iznad stijenke.
    parts,bore=graph(c,p+'z4pipe');outer=float(node(c,p+'z4pipeouter').get('stroke-width'))
    lake=path(node(c,p+'z4lake'));ys=line(node(c,p+'z4lakeSurface'))[0][1]
    submerged(parts[0][0],lake,ys,bore,'Z4 usis')
    tank=path(node(c,p+'z4tankfluid'));yt=line(node(c,p+'z4tanksurface'))[0][1]
    submerged(parts[0][-1],tank,yt,bore,'Z4 izlaz u vodospremu')
    top=path(node(c,p+'z4tankwall0'))[0][1]
    check(min(y for _,y in parts[0])+outer/2<top,'Z4: vod prelazi iznad ruba vodospreme')
    above_ground(c,p+'z4pipe',[p+'z4ground'],outer,'Z4')
    g=path(node(c,p+'z4ground'))
    close(ground_y(g,(tank[0][0]+tank[1][0])/2),max(y for _,y in tank),'Z4: vodosprema leži na tlu brda')
    check(yt<ys,'Z4: razina vodospreme iznad razine jezera')
    on_pipe(c,p+'z4pipe',circle_centre(node(c,p+'z4pumpSymbol')),'Z4: crpka leži na vodu')
    labels_clear(c,p+'z4',p+'z4pipe',outer,'Z4')

    # Z5: potopna crpka u bunaru, dugi vod do ulaza N.
    parts,bore=graph(c,p+'z5pipe');outer=float(node(c,p+'z5pipeouter').get('stroke-width'))
    well=path(node(c,p+'z5well'));yw=line(node(c,p+'z5wellSurface'))[0][1]
    pump=node(c,p+'z5pumpSymbol');pc=circle_centre(pump);r=float(pump.get('r'))
    check(inside(pc,well) and pc[1]-r>yw and pc[1]+r<max(y for _,y in well),'Z5: potopna crpka je cijela pod vodom i iznad dna')
    close(math.dist(parts[0][0],pc),0,'Z5: tlačni vod počinje na crpki')
    x0,x1=min(x for x,_ in well),max(x for x,_ in well)
    check(x0+outer/2<parts[0][0][0]<x1-outer/2,'Z5: vod prolazi oknom bunara bez dodira stijenki')
    above_ground(c,p+'z5pipe',[p+'z5groundR'],outer,'Z5')
    N=circle_centre(node(c,p+'z5pointN'))
    on_pipe(c,p+'z5pipe',N,'Z5: ulaz N leži na vodu');check(N[1]<yw,'Z5: N je iznad razine u bunaru')
    labels_clear(c,p+'z5',p+'z5pipe',outer,'Z5')

    # Z6: jezero, vodosprema i naselje; omjer razina 62 : 20 i otvoren izlaz L3.
    parts,bore=graph(c,p+'z6pipe');outer=float(node(c,p+'z6pipeouter').get('stroke-width'))
    lake=path(node(c,p+'z6lake'));ys=line(node(c,p+'z6lakeSurface'))[0][1]
    submerged(parts[0][0],lake,ys,bore,'Z6 usis')
    tank=path(node(c,p+'z6tankfluid'));yt=line(node(c,p+'z6tanksurface'))[0][1]
    submerged(parts[1][-1],tank,yt,bore,'Z6 izlaz L1 u vodospremu')
    w0=path(node(c,p+'z6tankwall0'));w1=path(node(c,p+'z6tankwall1'))
    xr=max(x for x,_ in tank);start=parts[3][0]
    close(start[0],xr,'Z6: L3 počinje na desnoj stijenci vodospreme')
    close(w0[-1][1]-w1[-1][1],bore,'Z6: otvor u stijenci ima puni provrt L3')
    close((w0[-1][1]+w1[-1][1])/2,start[1],'Z6: otvor je centriran na os L3')
    check(yt<start[1]<max(y for _,y in tank),'Z6: izlaz L3 je ispod razine vode i iznad dna')
    N=circle_centre(node(c,p+'z6pointN'))
    on_pipe(c,p+'z6pipe',N,'Z6: ulaz N leži na vodu')
    close((ys-yt)/(ys-N[1]),62/20,'Z6: visine vodospreme i naselja u omjeru 62 : 20',tol=1e-3)
    above_ground(c,p+'z6pipe',[p+'z6groundA',p+'z6groundC'],outer,'Z6')
    on_pipe(c,p+'z6pipe',circle_centre(node(c,p+'z6pumpSymbol')),'Z6: crpka leži na vodu')
    labels_clear(c,p+'z6',p+'z6pipe',outer,'Z6')


def wall_and_openings_free(c,prefix):
    """Otvoreni spremnik: stijenke prate rub fluida, a vrh ostaje otvoren."""
    fluid=path(node(c,prefix+'fluid'));ys=line(node(c,prefix+'surface'))[0][1]
    xs=[x for x,_ in fluid];bottom=max(y for _,y in fluid)
    w0=path(node(c,prefix+'wall0'));w1=path(node(c,prefix+'wall1'))
    close(w0[0][0],min(xs),prefix+': lijeva stijenka na rubu fluida')
    close(w1[0][0],max(xs),prefix+': desna stijenka na rubu fluida')
    check(w0[0][1]<ys and w1[0][1]<ys,prefix+': stijenke se nastavljaju iznad slobodne površine')
    close(w0[1][1],bottom,prefix+': dno spremnika na rubu fluida')


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
    # Kote padova EGL (uvod poglavlja: H = h_AC + h_CD + h_DB) između razina EGL u A, C, D i B.
    cx,dx_=float(node(a,p+'nodeC').get('cx')),float(node(a,p+'nodeD').get('cx'))
    levels=[egl[0][1]]+[next(y for x,y in egl if abs(x-xx)<1e-6) for xx in (cx,dx_)]+[egl[-1][1]]
    total=0
    for name,(y0,y1) in zip(('hAC','hCD','hDB'),zip(levels,levels[1:])):
        k0,k1=line(node(a,p+name))
        close(k0[0],k1[0],name+': kota je okomita')
        close(k0[1],y0,name+': počinje na razini EGL uzvodnog mjesta')
        close(k1[1],y1,name+': završava na razini EGL nizvodnog mjesta')
        total+=k1[1]-k0[1]
    close(total,dim[1][1]-dim[0][1],'h_AC + h_CD + h_DB = H')

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
    check_exercise_scenes(c,p)
    parts,_=graph(c,p+'z3pipe')
    for name,x in [('A',106),('B',340)]:
        e=node(c,p+'z3'+name);point=float(e.get('cx')),float(e.get('cy'))
        close(point[0],x,'Z3: čvor je u stvarnom spoju')
        check(sum(distance_to_path(point,part)<1e-6 for part in parts)>=2,'Z3: čvor spaja dovod/odvod i oba ogranka')
    # P3: petlja gradske mreže.
    d=ET.parse(ROOT/'u13_ch1_serijsko_paralelna_mreza.svg').getroot()
    ids=[e.get('id') for e in d.iter() if e.get('id')]
    check(len(ids)==len(set(ids)),'P3: jedinstveni ID-jevi')
    p='u13hc_'
    nodes={k:(float(node(d,p+'node'+k).get('cx')),float(node(d,p+'node'+k).get('cy'))) for k in 'ABCD'}
    # Svaka cijev ima vlastiti provrt razmjeran zadanom D (tablica P3), a stijenka
    # ostaje izvan provrta. Krajevi se produžuju točno do vanjskog ruba susjedne
    # cijevi istog sloja, pa kutovi ostaju zatvoreni bez izbočenja provrta u stijenku.
    diam={'AB':150,'BC':100,'CD':125,'DA':150}
    pipes=list(diam)
    fluid={k:node(d,p+'fluid'+k) for k in pipes}
    outer={k:node(d,p+'outer'+k) for k in pipes}
    fw={k:float(fluid[k].get('stroke-width')) for k in pipes}
    ow={k:float(outer[k].get('stroke-width')) for k in pipes}
    for k in pipes:
        check(fluid[k].get('stroke')=='#dcebf1','P3: provrt '+k+' je jednolika fluidna ispuna')
        close(fw[k]/fw['AB'],diam[k]/diam['AB'],'P3: širina provrta '+k+' razmjerna D',tol=1e-4)
        close(ow[k]-fw[k],9,'P3: stijenka '+k+' iste debljine, izvan provrta',tol=1e-4)
    check(node(d,p+'networkfluid').get('stroke-linecap')=='butt' and node(d,p+'networkouter').get('stroke-linecap')=='butt',
          'P3: bez zaobljenih kapa preko spojeva')
    def neighbour(k,n):return next(q for q in pipes if q!=k and n in q)
    parts=[]
    for k in pipes:
        a,b=nodes[k[0]],nodes[k[1]]
        for layer,widths in ((fluid[k],fw),(outer[k],ow)):
            s0,s1=line(layer)
            L=math.dist(a,b);u=((b[0]-a[0])/L,(b[1]-a[1])/L)
            for pt,nd,sgn in ((s0,a,-1),(s1,b,1)):
                ext=widths[neighbour(k,k[0] if sgn<0 else k[1])]/2
                close(math.dist(pt,(nd[0]+sgn*ext*u[0],nd[1]+sgn*ext*u[1])),0,
                      'P3: cijev '+k+' spaja čvor i završava na rubu susjedne cijevi',tol=1e-3)
        parts.append(line(fluid[k]))
    width=max(fw.values())
    dx,dy=delta(node(d,p+'inflowA'));check(dx>0 and dy==0,'P3: dotok ulazi u A')
    close(line(node(d,p+'inflowA'))[1][0]+16,nodes['A'][0],'P3: dotok završava na čvoru A, izvan oznake čvora')
    for k,sign in (('B',1),('C',1),('D',-1)):
        a,b=line(node(d,p+'outflow'+k));check((b[0]-a[0])*sign>0 and b[1]==a[1]==nodes[k][1],'P3: potrošnja izlazi iz čvora '+k)
    arc=path(node(d,p+'loopDirection'))
    centre=(sum(nodes[k][0] for k in nodes)/4,sum(nodes[k][1] for k in nodes)/4)
    a,b=arc[-2:]
    check((a[0]-centre[0])*(b[1]-a[1])-(a[1]-centre[1])*(b[0]-a[0])>0,'P3: obilazni smjer A-B-C-D je u smjeru kazaljke')
    check(all(distance_to_path(pt,line(outer[k]))>ow[k]/2+2.5 for pt in arc for k in pipes),'P3: strelica obilaznog smjera ne prelazi preko cijevi')
    for t in d.iter():
        if t.tag.endswith('text') and t.get('x'):
            pt=(float(t.get('x')),float(t.get('y')))
            check(all(distance_to_path(pt,line(outer[k]))>ow[k]/2 for k in pipes),'P3: oznaka ne leži na cijevi: '+''.join(t.itertext()))
    print('U13 SVG PASS: 4 slike; otvoreni spojeni vodovi, petlja gradske mreže, kote, profili, kružno koljeno, EGL/HGL te prizori vježbi Z1–Z6: uronjeni usisi i izlazi, vodovi iznad tla, otvoren izlaz vodospreme i omjer razina 62 : 20.')


if __name__=='__main__':main()
