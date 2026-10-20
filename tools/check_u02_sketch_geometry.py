"""Read the seven public U02 SVGs; check fluid domains, interfaces and vectors.

The checks use the actual SVG elements, independently of the drawing helper.
They complement, rather than replace, inspection at the final print size.
"""
from pathlib import Path
import math
import re
import xml.etree.ElementTree as ET
from check_u10_sketch_geometry import check, node, path, line, delta, distance_to_path
from check_u13_sketch_geometry import close, rect
from check_u01_sketch_geometry import inside, sample_segment, dimension

from sketch_style import check_uniform_fluid

ROOT = Path(__file__).resolve().parents[1] / 'assets' / 'print'


def subscripts(e):
    """Index runs written as SVG subscripts (Unicode subscript digits are not used)."""
    return [''.join(t.itertext()) for t in e.iter() if t.get('baseline-shift') == 'sub']


def interface(root, id, convex=False):
    """Read a circular SVG arc; equal-height lips and the stated sweep matter."""
    e=node(root,id)
    t=re.findall(r'[A-Za-z]|[-+]?(?:\d*\.\d+|\d+)(?:[eE][-+]?\d+)?',e.get('d'))
    check(len(t)==11 and t[0]=='M' and t[3]=='A',id+': circular arc required')
    x1,y1,r1,r2,rotation,large,sweep,x2,y2=map(float,[*t[1:3],*t[4:]])
    close(y1,y2,id+': same-height lips');close(r1,r2,id+': circular curvature')
    check(rotation==0 and large==sweep==int(convex),id+': wrong concavity/sweep')
    a=(x2-x1)/2;check(0<a<=r1+1e-10,id+': radius must span the bore')
    cy=y1-math.sqrt(max(0,r1*r1-a*a));cx=(x1+x2)/2
    theta=math.degrees(math.acos(min(1,a/r1)))
    return (cx,cy,r1,theta,(x1,y1),(x2,y2))


def capillary(root, prefix, count=1, convex=False):
    e=node(root,prefix+'fluid');fluid=path(e)
    check(e.get('stroke')=='none' and e.get('d').count('M')==1 and e.get('d').count('Z')==1,
          prefix+': one connected fill without a stroke over the openings')
    check_uniform_fluid(e, 'fill')
    bottom=max(y for x,y in fluid);left=min(x for x,y in fluid)
    surface=line(node(root,prefix+'surface0'))[0][1]
    walls=[rect(e) for e in root.iter() if re.fullmatch(re.escape(prefix)+r'(?:tube\d+(?:left|right)|tank(?:left|right|bottom)|roof\d+|airwall\d+)',e.get('id',''))]
    check(len(walls)>=5,prefix+': real walls required')
    for x,y,w,h in walls:
        for p in sample_segment((x+w/2,y+1),(x+w/2,y+h-1)):
            check(not inside(p,fluid),prefix+': a solid wall overlaps liquid')
    results=[]
    for i in range(count):
        ar=interface(root,prefix+f'interface{i}',convex)
        cx,cy,r,theta,a,b=ar
        wl=rect(node(root,prefix+f'tube{i}left'));wr=rect(node(root,prefix+f'tube{i}right'))
        close(wl[0]+wl[2],a[0],prefix+': left contact on inner wall')
        close(wr[0],b[0],prefix+': right contact on inner wall')
        check(surface<wl[1]+wl[3]<bottom-5,prefix+': open mouth must be immersed above tank floor')
        if convex:
            close(a[1],wl[1],prefix+': drop must meet the outlet lip')
            close(b[1],wr[1],prefix+': drop must meet the outlet lip')
        upper=cy if convex else cy+r+4
        route=[(left+10,bottom-9),(cx,bottom-9),(cx,upper)]
        for start,end in zip(route,route[1:]):
            for p in sample_segment(start,end,101):
                check(inside(p,fluid) and distance_to_path(p,fluid)>1,
                      prefix+': liquid path closed or cut off')
        results.append((ar,wl,wr,surface))
    return results


def tangent_forces(root,prefix,arc,theta,tip_at_contact=False,fluid=None):
    """Surface force on the liquid along the meniscus tangent, up and toward the wall.

    With theta > 0 an arrow starting on the contact line would cross the thin wall,
    so it is drawn with its tip on the contact line and its tail in the liquid.
    """
    cx,cy,r,measured,a,b=arc
    close(measured,theta,prefix+': contact angle from actual arc',tol=1e-5)
    for i,p in enumerate((a,b)):
        e=node(root,prefix+f'sigma{i}');u,v=line(e)
        if tip_at_contact:
            close(math.dist(v,p),0,prefix+': surface-force tip on the contact line')
            check(inside(u,fluid) and distance_to_path(u,fluid)>1,prefix+': surface-force tail lies in the liquid, not across the wall')
        else:
            close(math.dist(u,p),0,prefix+': surface force starts on contact line')
        dx,dy=delta(e)
        close(math.degrees(math.atan2(abs(dx),-dy)),theta,prefix+': tangent direction',tol=1e-5)
        check(dy<0 and dx*(-1 if i==0 else 1)>=-1e-10,prefix+': liquid pulled up and toward wall')


def shear(root,prefix,forces=True):
    x,y,w,h=rect(node(root,prefix+'fluid'))
    moving=rect(node(root,prefix+'moving'));fixed=rect(node(root,prefix+'fixed'))
    close(moving[1]+moving[3],y,prefix+': upper plate touches liquid')
    close(fixed[1],y+h,prefix+': lower plate touches liquid')
    a,b=line(node(root,prefix+'profile'))
    close(a[1],y+h,prefix+': zero velocity at stationary wall')
    close(b[1],y,prefix+': prescribed velocity at moving wall')
    check(x<a[0]<b[0]<x+w,prefix+': profile remains in the fluid')
    for i in range(1,5):
        u,v=line(node(root,prefix+f'velocity{i}'))
        close(u[0],a[0],prefix+': common velocity origin')
        check(y<u[1]<y+h and v[0]>u[0] and u[1]==v[1],prefix+': fluid velocity direction')
        close(distance_to_path(v,[a,b]),0,prefix+': arrow head on linear profile')
    dimension(root,prefix+'gap',(x-18,y),(x-18,y+h))
    check(delta(node(root,prefix+'speed'))[0]>0,prefix+': plate speed')
    # The plate-speed arrow shows the same u as the fluid velocity at the moving wall.
    close(delta(node(root,prefix+'speed'))[0],b[0]-a[0],prefix+': plate speed arrow equals profile velocity u',tol=1e-6)
    if forces:
        # Steady motion: pull and oil resistance on the plate have equal magnitude.
        close(-delta(node(root,prefix+'drag'))[0],delta(node(root,prefix+'pull'))[0],prefix+': F equals F_v in steady motion',tol=1e-6)
        check(delta(node(root,prefix+'drag'))[0]<0<delta(node(root,prefix+'pull'))[0],prefix+': resistance opposes motion')
        for id in ('drag','pull'):
            yy=line(node(root,prefix+id))[0][1]
            check(moving[1]<=yy<=y,prefix+': force is on the moving plate')


def main():
    names=['u02_fig_uvod_pregled','u02_fig_rotirajuci_disk','u02_val2_viskoznost_kapilarnost',
           'u02_fig_kapilarni_uspon_etanol','u02_ch1_kapilarni_mikrodozator_kapljica',
           'u02_fig_lezaj_temperatura','u02_vjezbe_skice']
    roots=[ET.parse(ROOT/(n+'.svg')).getroot() for n in names]
    for name,root in zip(names,roots):
        ids=[e.get('id') for e in root.iter() if e.get('id')]
        check(len(ids)==len(set(ids)),name+': unique IDs')
        check(not any(e.tag.endswith('filter') for e in root.iter()),name+': no shadow filter')
    intro,disk,combined,ethanol,micro,bearing,z=roots
    for root,p in [(intro,'u02fup_'),(combined,'u02v2vk_')]:shear(root,p+'shear')
    # P1: disk na uljnom filmu. Film lezi tocno izmedu diska i nepomicne ploce,
    # prsten r < R u tlocrtu, obodna brzina tangencijalna na prsten, a kutna
    # brzina ima otvoren vrh (standard vektora).
    film=node(disk,'u02rd_film');plate=node(disk,'u02rd_plate');dsc=node(disk,'u02rd_disc')
    fy,fh=float(film.get('y')),float(film.get('height'))
    close(fy,float(dsc.get('y'))+float(dsc.get('height')),'disk: film starts at disc underside')
    close(fy+fh,float(plate.get('y')),'disk: film ends at fixed plate')
    check(float(dsc.get('x'))>=float(film.get('x')) and float(dsc.get('x'))+float(dsc.get('width'))<=float(film.get('x'))+float(film.get('width')),'disk: film covers whole disc')
    cx,cy,Rp=[float(node(disk,'u02rd_plan_disc').get(k)) for k in ('cx','cy','r')]
    ro,ri=float(node(disk,'u02rd_ring_outer').get('r')),float(node(disk,'u02rd_ring_inner').get('r'))
    check(0<ri<ro<Rp,'disk: ring inside disc')
    u=node(disk,'u02rd_u_plan');ux1,uy1,ux2,uy2=[float(v) for v in re.findall(r'-?\d+(?:\.\d+)?',u.get('d'))]
    r_mid=(ri+ro)/2
    close(uy1,cy-r_mid,'disk: velocity drawn on the ring');close(uy2,uy1,'disk: velocity tangential at top of ring')
    check(ux2>ux1,'disk: velocity sense matches clockwise omega')
    for vid in ('u02rd_omega_side','u02rd_omega_plan'):
        check(node(disk,vid).get('data-mf1-vector')=='angular-velocity',vid+': angular velocity declared')
    # P2 now shows only its Couette problem. Capillarity has a dedicated P3
    # figure and remains independently checked there and in the overview.
    check(not any((e.get('id') or '').startswith('u02v2vk_cap') for e in combined.iter()),
          'P2: no unrelated capillarity scene beside the shear problem')
    for root,p in [(intro,'u02fup_'),(ethanol,'u02fku_')]:
        ar,wl,wr,surface=capillary(root,p+'cap')[0]
        tangent_forces(root,p+'cap',ar,18,tip_at_contact=True,fluid=path(node(root,p+'capfluid')))
        hline=line(node(root,p+'height'))
        close(hline[0][1],ar[1]+ar[2],p+': height starts at meniscus apex')
        close(hline[1][1],surface,p+': height ends at free surface')
        dline=line(node(root,p+'diameter'))
        close(dline[0][0],wl[0]+wl[2],p+': diameter inside left wall')
        close(dline[1][0],wr[0],p+': diameter inside right wall')
    zoom=interface(ethanol,'u02fku_zoominterface')
    close(zoom[3],18,'Zoom: contact angle 18 degrees')
    dx,dy=delta(node(ethanol,'u02fku_zoomtangent'))
    close(math.degrees(math.atan2(dx,dy)),18,'Zoom: tangent measured through liquid')
    natural=capillary(micro,'u02ch1_state0')[0]
    formed=capillary(micro,'u02ch1_state1',convex=True)[0]
    tangent_forces(micro,'u02ch1_start',natural[0],0)
    h=math.dist(*line(node(micro,'u02ch1_capHeight')))
    H=math.dist(*line(node(micro,'u02ch1_outletHeight')))
    close(h/H,(4*.072/(998*9.81*.0008))/.060,'P4: natural rise versus outlet height')
    close(math.dist(*line(node(micro,'u02ch1_dropDiameter'))),2*formed[0][2],'P4: drop diameter')
    close(2*formed[0][2]/(formed[2][0]-formed[1][0]-formed[1][2]),3,'P4: D/d=3')
    shear(z,'u02vs_z1');shear(z,'u02vs_z5',forces=False)
    check(delta(node(z,'u02vs_z5drag'))[0]<0<delta(node(z,'u02vs_z5pull'))[0],'Z5: dynamometer pulls opposite oil resistance')
    close(-delta(node(z,'u02vs_z5drag'))[0],delta(node(z,'u02vs_z5pull'))[0],'Z5: steady pull equals resistance',tol=1e-6)
    for i in range(2):
        circle=node(z,f'u02vs_z2outer{i}')
        close(math.dist(*line(node(z,f'u02vs_z2diameter{i}'))),2*float(circle.get('r')),'Z2: true diameter')
    check(float(node(z,'u02vs_z2inner').get('r'))<float(node(z,'u02vs_z2outer1').get('r')),'Z2: two separate soap-film interfaces')
    up=rect(node(z,'u02vs_z3upperFluid'));down=rect(node(z,'u02vs_z3lowerFluid'));plate=rect(node(z,'u02vs_z3moving'))
    close(down[3]/up[3],2,'Z3: gap ratio 2')
    # Z3 asks for the direction of each resistance: the sketch names F1 and F2 as unknowns only.
    ids={e.get('id') for e in z.iter()}
    check(not any((i or '').startswith('u02vs_z3drag') for i in ids),'Z3: resistance arrows would reveal the asked directions')
    for k,(lo,hi) in ((1,(up[1],up[1]+up[3])),(2,(down[1],down[1]+down[3]))):
        lab=node(z,f'u02vs_z3label{k}')
        check(''.join(lab.itertext()).replace(' ','')==f'F{k}=?','Z3: unknown resistance labelled with ?')
        check(subscripts(lab)==[str(k)],'Z3: resistance index is a true subscript')
        check(lo<float(lab.get('y'))<hi,'Z3: each unknown sits in its own gap')
    check(delta(node(z,'u02vs_z3pull'))[0]>0,'Z3: pull acts in the direction of motion')
    p0=line(node(z,'u02vs_z3profile0'));close(delta(node(z,'u02vs_z3speed'))[0],p0[1][0]-p0[0][0],'Z3: plate speed arrow equals u',tol=1e-6)
    for i,(a,b) in enumerate((line(node(z,'u02vs_z3profile0')),line(node(z,'u02vs_z3profile1')))):
        if i==0:close(a[1],up[1],'Z3 upper zero');close(b[1],plate[1],'Z3 upper moving wall')
        else:close(a[1],plate[1]+plate[3],'Z3 lower moving wall');close(b[1],down[1]+down[3],'Z3 lower zero')
        dimension(z,f'u02vs_z3gap{i+1}',(26 if i==0 else 278,up[1] if i==0 else down[1]),(26 if i==0 else 278,up[1]+up[3] if i==0 else down[1]+down[3]))
    # Z4: two equal plate gaps in sea water; clean steel rises (concave, 30 deg),
    # hydrophobic coating depresses (shallow convex meniscus below the free surface, 105 deg).
    ar,wl,wr,surface=capillary(z,'u02vs_z4',1)[0]
    close(ar[3],30,'Z4: contact angle 30 degrees on clean steel')
    ln=line(node(z,'u02vs_z4height0'))
    close(ln[0][1],ar[1]+ar[2],'Z4: rise measured from meniscus apex');close(ln[1][1],surface,'Z4: rise measured to free surface')
    rise=math.dist(*ln);gap0=wr[0]-wl[0]-wl[2]
    check(abs(rise/gap0-62.873/0.20)>100,'Z4: h1 must not be drawn at the result scale of the gap width b')
    dimension(z,'u02vs_z4gap0',(wl[0]+wl[2],61),(wr[0],61))
    # Coated gap: h2 and its sign are asked, so neither meniscus nor level is shown;
    # a "?" window hides the gap around the free-surface level (only theta_2 is given).
    ids={e.get('id') for e in z.iter()}
    check('u02vs_z4interface1' not in ids and 'u02vs_z4height1' not in ids,'Z4: coated-gap meniscus and h2 must not be drawn')
    wl1=rect(node(z,'u02vs_z4tube1left'));wr1=rect(node(z,'u02vs_z4tube1right'))
    close(wr1[0]-wl1[0]-wl1[2],gap0,'Z4: both gaps have the same width b')
    check(surface<wl1[1]+wl1[3]<284-5,'Z4: coated gap mouth immersed above the floor')
    hx,hy,hw,hh=rect(node(z,'u02vs_z4hidden'))
    check(hx<=wl1[0] and hx+hw>=wr1[0]+wr1[2],'Z4: window covers the whole coated gap')
    check(hy<surface-15 and hy+hh>surface+15,'Z4: window hides any level near the free surface')
    texts=[(''.join(e.itertext()).strip(),e) for e in z.iter() if e.tag.endswith('text')]
    check(any(s=='?' and hx<float(e.get('x'))<hx+hw and hy<float(e.get('y'))<hy+hh for s,e in texts),'Z4: unknown level marked with ?')
    check(any(s.replace(' ','')=='h2=?' and subscripts(e)==['2'] for s,e in texts),'Z4: h2 named as unknown')
    fluid=path(node(z,'u02vs_z4fluid'));cx=wl1[0]+wl1[2]+gap0/2
    for p in sample_segment((cx,275),(cx,hy+hh+2),101):
        check(inside(p,fluid) and distance_to_path(p,fluid)>1,'Z4: liquid continuous from tank into the coated gap')
    top=min(y for x,y in fluid if wl1[0]+wl1[2]-1e-9<=x<=wr1[0]+1e-9)
    check(hy<top<hy+hh,'Z4: liquid boundary in the coated gap stays hidden')
    dimension(z,'u02vs_z4gap1',(wl1[0]+wl1[2],61),(wr1[0],61))
    ar,wl,wr,surface=capillary(z,'u02vs_z6',convex=True)[0]
    close(2*ar[2]/(wr[0]-wl[0]-wl[2]),1.8/.5,'Z6: D/d nominal ratio')
    dimension(z,'u02vs_z6height',(269,wl[1]),(269,surface))
    close(math.dist(*line(node(z,'u02vs_z6dropDiameter'))),2*ar[2],'Z6: actual drop diameter')
    for i in range(2):
        x,y,w,h=rect(node(bearing,f'u02flt_b{i}fluid'));a,b=line(node(bearing,f'u02flt_b{i}profile'))
        close(a[1],y,'Bearing: zero at bushing');close(b[1],y+h,'Bearing: speed at shaft')
        check(delta(node(bearing,f'u02flt_b{i}drag'))[0]<0<delta(node(bearing,f'u02flt_b{i}speed'))[0],'Bearing: oil opposes shaft motion')
        close(delta(node(bearing,f'u02flt_b{i}speed'))[0],b[0]-a[0],'Bearing: shaft speed arrow equals u at the shaft',tol=1e-6)
    check(-delta(node(bearing,'u02flt_b0drag'))[0]>-delta(node(bearing,'u02flt_b1drag'))[0],'Bearing: tau1 (0 C) longer than tau2 (90 C)')
    dimension(bearing,'u02flt_gap',(335,142),(335,214))
    shaft=node(bearing,'u02flt_shaftSection')
    close(math.dist(*line(node(bearing,'u02flt_shaftDiameter'))),2*float(shaft.get('r')),'Bearing: shaft diameter')
    for id,sign in [('rotation',1),('resistance',-1)]:
        pts=path(node(bearing,'u02flt_'+id))
        cross=sum((a[0]-123)*(b[1]-410)-(a[1]-410)*(b[0]-123) for a,b in zip(pts,pts[1:]))
        check(sign*cross>0,'Bearing: resisting moment opposite angular speed')
    for name,root in zip(names,roots):
        for t in root.iter():
            if t.tag.endswith('text'):
                txt=''.join(t.itertext())
                check(not re.search(r'(stijenka|čahura): u = 0',txt),name+': u is the moving-wall speed; use v = 0 at a fixed wall')
                check('p₀' not in txt,name+': p_0 is reserved for stagnation pressure')
    print('U02 SVG PASS: 7 images; open immersed mouths, continuous liquid, circular menisci and 18° tangents (tips on the contact line), no-slip profiles, force directions, unknowns not revealed in Z3/Z4, true dimensions and ratios.')


if __name__=='__main__':main()
