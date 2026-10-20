"""Čita stvarne SVG-ove U15: geometrija, valovi, energija i skok.

Oblik valjka i vodoravne duljine nisu predviđanje 1D modela. Bilance se
provjeravaju u rubnim presjecima, a otvorenost i spojeni fluid cijelim tokom.
"""
import math
import re
from pathlib import Path
import xml.etree.ElementTree as ET
from check_u10_sketch_geometry import check, node, path, line, delta, distance_to_path, wall_and_openings
from check_u13_sketch_geometry import close

from sketch_style import check_uniform_fluid, check_arrow_semantics

ROOT=Path(__file__).resolve().parents[1]/'assets'/'print'
G=9.81


def energy(y,q):return y+q*q/(2*G*y*y)


def flow(root,prefix):
    surface=path(node(root,prefix+'surface'))
    bed=path(node(root,prefix+'wall0'))
    check(all(x2>x1 for (x1,y1),(x2,y2) in zip(surface,surface[1:])), prefix+': površina ne smije imati povrat ili preskok')
    check(all(x2>x1 for (x1,y1),(x2,y2) in zip(bed,bed[1:])), prefix+': dno ne smije imati povrat ili pregradu')
    ports=[(surface[i][0],(surface[i][1]+bed[i][1])/2) for i in (0,-1)]
    wall_and_openings(root,prefix,ports)
    return bed,surface


def at(points,x):
    for a,b in zip(points,points[1:]):
        if a[0]<=x<=b[0]:
            return a[1]+(b[1]-a[1])*(x-a[0])/(b[0]-a[0])
    raise AssertionError('Točka je izvan profila')


def vectors_inside(root,prefix,names,bed,surface):
    for name in names:
        a,b=line(node(root,prefix+name))
        for j in range(31):
            x,y=(a[k]+j/30*(b[k]-a[k]) for k in (0,1))
            check(at(surface,x)<y<at(bed,x), prefix+name+': vektor mora ostati u fluidu iznad dna')


def trapezoid(root,prefix,b,z,H,y,scale):
    wall=path(node(root,prefix+'wall'))
    check(len(wall)==4, prefix+': dvije bočne stijenke i dno; bez poklopca')
    fluid=path(node(root,prefix+'fluid'))
    left,right,xr,xl=fluid[:4]
    close(xr[0]-xl[0],b*scale,prefix+': širina dna')
    close(xl[1]-left[1],y*scale,prefix+': stvarna dubina')
    close(right[0]-left[0],(b+2*z*y)*scale,prefix+': širina slobodne površine')
    for i,j in ((0,1),(3,2)):
        dx,dy=wall[i][0]-wall[j][0],wall[i][1]-wall[j][1]
        close(abs(dx),z*abs(dy),prefix+': stvarni pokos')
        close(abs(dy),H*scale,prefix+': visina stijenke')
    area=abs(sum(x1*y2-x2*y1 for (x1,y1),(x2,y2) in zip(fluid,fluid[1:])))/2/scale**2
    close(area,y*(b+z*y),prefix+': integrirana površina SVG poligona')
    wetted=math.dist(left,xl)+math.dist(xl,xr)+math.dist(xr,right)
    close(wetted/scale,b+2*y*math.hypot(1,z),prefix+': omočen opseg bez slobodne površine')
    surface=line(node(root,prefix+'surface'))
    close(surface[0][1],left[1],prefix+': površina na stvarnoj dubini')
    for x in (left,right):
        close(distance_to_path(x,wall),0,prefix+': voda doseže unutarnju stijenku')
    return wall,fluid


def texts(root):
    return [''.join(e.itertext()) for e in root.iter() if e.tag.endswith('text')]


def absent(root,id,message):
    check(not any(e.get('id')==id for e in root.iter()),message)


def main():
    intro=ET.parse(ROOT/'u15_fig_uvod_otvoreni_tok.svg').getroot()
    ex=ET.parse(ROOT/'u15_vjezbe_skice.svg').getroot()
    for root in (intro,ex):
        ids=[e.get('id') for e in root.iter() if e.get('id')]
        check(len(ids)==len(set(ids)), 'Jedinstveni ID-jevi')
        check(not any(e.tag.endswith('filter') for e in root.iter()), 'Bez sjena i filtera preko vode')
        for e in root.iter():
            if e.get('id','').endswith('fluid'):
                check(e.get('d').count('M')==1 and e.get('stroke')=='none','Jedna povezana ispuna po fluidnoj domeni')
                check_uniform_fluid(e, 'fill')
        issues=check_arrow_semantics(root)
        check(not issues,'Stil vektora: '+'; '.join(issues))

    p='u15intro_';q,yup,base,scale=1.4,1.3,245,90
    bed,surface=flow(intro,p+'channel')
    E0=energy(yup,q);yc=(q*q/G)**(1/3)
    for (x,yb),(xx,yt) in zip(bed,surface):
        close(x,xx,'Uvod: dno i površina pripadaju istom presjeku')
        y=(yb-yt)/scale;z=(base-yb)/scale
        check(y>0,'Uvod: pozitivan otvor toka kroz cijeli kanal')
        if x<=640:
            close(z+energy(y,q),E0,'Uvod: ista energija i protok do skoka',tol=1e-7)
            check(y>=yc-1e-7 if x<=430 else y<=yc+1e-7,'Uvod: ispravna grana prije/poslije tjemena')
    critical=line(node(intro,p+'criticalSection'))
    close(critical[1][1]-critical[0][1],scale*yc,'Uvod: kritična dubina na stvarnom presjeku')
    close(critical[1][1],at(bed,430),'Uvod: donji kraj kritičnog presjeka na dnu')
    close(critical[0][1],at(surface,430),'Uvod: gornji kraj na površini')
    ys=(at(bed,640)-at(surface,640))/scale
    y2=(bed[-1][1]-surface[-1][1])/scale
    M=lambda y:y*y/2+q*q/(G*y)
    close(M(ys),M(y2),'Uvod: skok zatvara količinu gibanja',tol=1e-7)
    loss=(y2-ys)**3/(4*ys*y2)
    close(energy(ys,q)-energy(y2,q),loss,'Uvod: ispravan gubitak energije',tol=1e-7)
    check(loss>0 and ys<yc<y2,'Uvod: siloviti tok prelazi u mirni uz disipaciju')
    for name,depth in (('upstreamDepth',yup),('downstreamDepth',y2)):
        close(delta(node(intro,p+name))[1],scale*depth,'Uvod: kote stvarnih dubina')
    vectors_inside(intro,p,['inletVelocity','criticalVelocity','superVelocity','outletVelocity'],bed,surface)
    # Oznake: početna mirna dubina/brzina s indeksom 0, silovit presjek ispred skoka 1, mirni iza skoka 2;
    # v_s je u knjizi brzina broda i ne smije označavati silovit tok.
    labels=texts(intro)
    check('vs' not in labels and 'y1' not in labels,'Uvod: bez v_s i bez y_1 za početnu mirnu dubinu')
    check(all(t in labels for t in ('v0','vc','v1','v2','y0','y2')),'Uvod: oznake v0, vc, v1, v2, y0, y2')

    p='u15ex_'
    for n in range(1,7):node(ex,p+'z'+str(n))
    trapezoid(ex,p+'z1section',1.5,0,.86,.6,90)
    close(delta(node(ex,p+'z1b'))[0],1.5*90,'Z1: poprečna širina')
    close(delta(node(ex,p+'z1y'))[1],.6*90,'Z1: dubina')
    # Z1 traži smjer i predznak v - c i v + c: valovi se ne crtaju, samo nepoznanice.
    for name in ('upstreamWave','downstreamWave'):
        absent(ex,p+'z1'+name,'Z1: skica ne smije crtati traženi smjer vala')
    z1=node(ex,p+'z1')
    check([e.get('id') for e in z1.iter() if e.get('data-mf1-vector')]==[p+'z1velocity'],'Z1: jedini vektor je smjer toka v')
    dx,dy=delta(node(ex,p+'z1velocity'))
    check(dx>0,'Z1: tok nizvodno (+x)');close(dy,0,'Z1: uzdužni tok')
    check('v − c = ?' in texts(z1) and 'v + c = ?' in texts(z1),'Z1: nepoznanice v − c = ? i v + c = ?')
    # Z2: ustava s otvorenim prolazom ispod ruba; voda povezana od uzvodnog presjeka do mlaza; y1 shematski (< a, ne Cc a).
    wall_and_openings(ex,p+'z2',[(46,180),(378,231)])
    poly=path(node(ex,p+'z2fluid'))
    def inside(pt):
        x,y=pt;hit=False
        for (x1,y1),(x2,y2) in zip(poly,poly[1:]+poly[:1]):
            if (y1>y)!=(y2>y) and x<x1+(y-y1)*(x2-x1)/(y2-y1):hit=not hit
        return hit
    gx,gy,gw,gh=(float(node(ex,p+'z2gate').get(k)) for k in ('x','y','width','height'))
    close(gy+gh,240-.4*60,'Z2: donji rub ustave na visini otvora a = 0,400 m (mjerilo 60 px/m)')
    check(inside((gx+gw/2,(gy+gh+240)/2)),'Z2: fluid prolazi ispod ustave')
    check(not inside((gx+gw/2,gy+gh/2)),'Z2: fluid ne prolazi kroz ploču ustave')
    close(delta(node(ex,p+'z2y0'))[1],2.0*60,'Z2: uzvodna dubina y0 u mjerilu')
    close(delta(node(ex,p+'z2a'))[1],.4*60,'Z2: otvor a u mjerilu')
    y1px=delta(node(ex,p+'z2y1'))[1]
    check(0<y1px<.4*60 and abs(y1px-.61*.4*60)>1.5,'Z2: dubina mlaza manja od otvora, ali shematska (ne otkriva Cc a)')
    dx,dy=delta(node(ex,p+'z2inflow'));check(dx>0,'Z2: dotok nizvodno');close(dy,0,'Z2: vodoravan dotok')
    z2=node(ex,p+'z2')
    check(any(t.endswith('= ?') and t.startswith('y1') for t in texts(z2)),'Z2: nepoznanica y1 = ?')
    check(any(t.startswith('q = ?') for t in texts(z2)),'Z2: nepoznanica q = ?')
    trapezoid(ex,p+'z3section',2.4,1.5,1.3,.9,50)
    close(delta(node(ex,p+'z3T'))[0],5.1*50,'Z3: T završava na stvarnim rubovima vode')
    close(delta(node(ex,p+'z3b'))[0],2.4*50,'Z3: b je unutarnja širina dna')
    close(delta(node(ex,p+'z3y'))[1],.9*50,'Z3: y od dna do površine')
    key=path(node(ex,p+'z3slopeKey'))
    close((key[1][0]-key[0][0])/(key[2][1]-key[1][1]),1.5,'Z3: ključ pokosa u istom omjeru')
    bed,surface=flow(ex,p+'z4channel');base,scale,q=238,100,2.2
    # Z4 traži y_t: zadane visine (y1, dz) su u mjerilu, a površina nad pragom shematska (ravna),
    # pa nacrtana dubina na tjemenu nije izračunati korijen.
    E1=energy(1.2,q);Et=E1-.12;yc=(q*q/G)**(1/3)
    lo,hi=yc,1.2
    for _ in range(200):
        mid=(lo+hi)/2
        lo,hi=(lo,mid) if energy(mid,q)<Et else (mid,hi)
    yt_result=(lo+hi)/2
    for (x,yb),(xx,yt) in zip(bed,surface):
        check(abs(yt-surface[0][1])<1e-6,'Z4: shematska ravna slobodna površina')
    crest_depth=(at(bed,248)-at(surface,248))/scale
    check(abs(crest_depth-yt_result)>.05*yt_result,'Z4: nacrtana dubina na tjemenu nije traženi y_t')
    check(any(t=='yt = ?' for t in texts(node(ex,p+'z4'))),'Z4: nepoznanica y_t = ?')
    close(math.hypot(*delta(node(ex,p+'z4inflow'))),math.hypot(*delta(node(ex,p+'z4crestVelocity'))),
          'Z4: shematske jednake brzine ne otkrivaju omjer v_t/v_1')
    crest=line(node(ex,p+'z4crestSection'))
    close(crest[0][1],at(surface,248),'Z4: presjek počinje na površini')
    close(crest[1][1],at(bed,248),'Z4: presjek završava na tjemenu dna')
    close(delta(node(ex,p+'z4yt'))[1],crest[1][1]-crest[0][1],'Z4: kota dubine na tjemenu')
    close(delta(node(ex,p+'z4rise'))[1],.12*scale,'Z4: povišenje dna 0,120 m')
    close(delta(node(ex,p+'z4y1'))[1],1.2*scale,'Z4: uzvodna dubina 1,200 m')
    vectors_inside(ex,p,['z4inflow','z4crestVelocity'],bed,surface)
    bed,surface=flow(ex,p+'z5channel');base,scale=234,83
    for name,depth in (('z5y1',.25),('z5y2',1.22)):
        close(delta(node(ex,p+name))[1],scale*depth,'Z5: kote mjerenih dubina')
    for name,depth,sign in (('z5pressureIn',.25,1),('z5pressureOut',1.22,-1)):
        a,b=line(node(ex,p+name))
        close(a[1],base-scale*depth/3,'Z5: rezultanta hidrostatičkog tlaka na trećini dubine od dna')
        check((b[0]-a[0])*sign>0,'Z5: suprotne tlačne sile na fluid')
    fluid=path(node(ex,p+'z5channelfluid'))
    for point in path(node(ex,p+'z5controlVolume')):
        x,y=point
        check(abs(y-base)<1e-6 or abs(y-at(surface,x))<1e-6,'Z5: KV zatvara stvarnu fluidnu domenu')
    vectors_inside(ex,p,['z5inflow','z5outflow'],bed,surface)
    trapezoid(ex,p+'z6section',3,2,1.5,1.2,26)
    close(delta(node(ex,p+'z6H'))[1],1.5*26,'Z6: konstrukcijska dubina')
    close(delta(node(ex,p+'z6freeboard'))[1],.3*26,'Z6: slobodni rub do stvarne razine')
    close(delta(node(ex,p+'z6b'))[0],3*26,'Z6: širina dna')
    bed,surface=flow(ex,p+'z6basin');base,scale,q=265,48,8/5
    y1=(bed[0][1]-surface[0][1])/scale;y2=(bed[-1][1]-surface[-1][1])/scale
    close(y1,.35,'Z6: propisana ulazna dubina bazena')
    M=lambda y:y*y/2+q*q/(G*y)
    # Z6 traži spregnutu dubinu i usporedbu s y_2,dop: nizvodna dubina je shematska,
    # nije spregnuta, a crta dopuštene dubine ne stoji uz vodu.
    check(abs(M(y1)-M(y2))>.02*M(y1),'Z6: nacrtana nizvodna dubina nije izračunata spregnuta dubina')
    check(y2>y1,'Z6: skok podiže razinu')
    absent(ex,p+'z6allowedDepthLine','Z6: bez crte dopuštene dubine uz nacrtanu vodu')
    z6=texts(node(ex,p+'z6'))
    check('y2 = ?' in z6 and any('y2,dop = 1,40 m' in t for t in z6),'Z6: y2 = ? i y_2,dop samo kao podatak')
    close(delta(node(ex,p+'z6y2'))[1],scale*y2,'Z6: kota stvarne nizvodne dubine')
    vectors_inside(ex,p,['z6flow'],bed,surface)
    print('U15 SVG PASS: 2 slike; otvoreni tokovi, neprekinuto dno, valovi, E(y), trapezni presjeci, kritičnost, kota praga, sile skoka i granica bazena.')


if __name__=='__main__':main()
