"""Čita stvarne SVG-ove U15: geometrija, valovi, energija i skok.

Oblik valjka i vodoravne duljine nisu predviđanje 1D modela. Bilance se
provjeravaju u rubnim presjecima, a otvorenost i spojeni fluid cijelim tokom.
"""
import math
from pathlib import Path
import xml.etree.ElementTree as ET
from check_u10_sketch_geometry import check, node, path, line, delta, distance_to_path, wall_and_openings
from check_u13_sketch_geometry import close

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
                grad=node(root,e.get('fill')[5:-1])
                check(grad.get('gradientUnits')=='userSpaceOnUse' and grad.get('x1')==grad.get('x2'),
                      'Prostorni vertikalni gradijent ne prekida tok')

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

    p='u15ex_'
    for n in range(1,7):node(ex,p+'z'+str(n))
    trapezoid(ex,p+'z1section',1.5,0,.86,.6,90)
    close(delta(node(ex,p+'z1b'))[0],1.5*90,'Z1: poprečna širina')
    close(delta(node(ex,p+'z1y'))[1],.6*90,'Z1: dubina')
    v=1.2/(1.5*.6);c=math.sqrt(G*.6)
    for name,value in (('upstreamWave',v-c),('downstreamWave',v+c),('velocity',v)):
        dx,dy=delta(node(ex,p+'z1'+name))
        close(dx/25,value,'Z1: stvarna potpisana brzina prema obali')
        close(dy,0,'Z1: uzdužno širenje poremećaja')
    for x,y in path(node(ex,p+'z2energyCurve')):
        depth=(x-46)/166;E=(254-y)/57
        close(E,energy(depth,3),'Z2: stvarna energijska krivulja',tol=1e-7)
    minimum=node(ex,p+'z2minimum')
    depth=(float(minimum.get('cx'))-46)/166;E=(254-float(minimum.get('cy')))/57
    close(3/math.sqrt(G*depth**3),1,'Z2: minimum daje Fr=1')
    close(E,1.5*depth,'Z2: minimum energije')
    for x,y in path(node(ex,p+'z2depthAsymptote')):
        close((254-y)/57,(x-46)/166,'Z2: pomoćni pravac E=y')
    trapezoid(ex,p+'z3section',2.4,1.5,1.3,.9,50)
    close(delta(node(ex,p+'z3T'))[0],5.1*50,'Z3: T završava na stvarnim rubovima vode')
    close(delta(node(ex,p+'z3b'))[0],2.4*50,'Z3: b je unutarnja širina dna')
    close(delta(node(ex,p+'z3y'))[1],.9*50,'Z3: y od dna do površine')
    key=path(node(ex,p+'z3slopeKey'))
    close((key[1][0]-key[0][0])/(key[2][1]-key[1][1]),1.5,'Z3: ključ pokosa u istom omjeru')
    bed,surface=flow(ex,p+'z4channel');base,scale,q=238,100,2.2
    for (x,yb),(xx,yt) in zip(bed,surface):
        depth=(yb-yt)/scale;z=(base-yb)/scale
        close(z+energy(depth,q),energy(1.2,q),'Z4: bilanca između stvarnih presjeka',tol=1e-7)
        check(depth>(q*q/G)**(1/3),'Z4: čitav tok ostaje podkritičan')
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
    close(M(y1),M(y2),'Z6: spregnute dubine pri projektnom protoku',tol=1e-7)
    close((base-line(node(ex,p+'z6allowedDepthLine'))[0][1])/scale,1.4,'Z6: dopuštena dubina mjerena od dna bazena')
    close(delta(node(ex,p+'z6y2'))[1],scale*y2,'Z6: kota stvarne nizvodne dubine')
    vectors_inside(ex,p,['z6flow'],bed,surface)
    print('U15 SVG PASS: 2 slike; otvoreni tokovi, neprekinuto dno, valovi, E(y), trapezni presjeci, kritičnost, kota praga, sile skoka i granica bazena.')


if __name__=='__main__':main()
