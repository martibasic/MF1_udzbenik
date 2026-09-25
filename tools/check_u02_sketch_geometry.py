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


def tangent_forces(root,prefix,arc,theta):
    cx,cy,r,measured,a,b=arc
    close(measured,theta,prefix+': contact angle from actual arc',tol=1e-5)
    for i,p in enumerate((a,b)):
        e=node(root,prefix+f'sigma{i}');u,v=line(e)
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
    if forces:
        check(delta(node(root,prefix+'drag'))[0]<0<delta(node(root,prefix+'pull'))[0],prefix+': resistance opposes motion')
        for id in ('drag','pull'):
            yy=line(node(root,prefix+id))[0][1]
            check(moving[1]<=yy<=y,prefix+': force is on the moving plate')


def main():
    names=['u02_fig_uvod_pregled','u02_fig_kinematicka_viskoznost','u02_val2_viskoznost_kapilarnost',
           'u02_fig_kapilarni_uspon_etanol','u02_ch1_kapilarni_mikrodozator_kapljica',
           'u02_fig_lezaj_temperatura','u02_vjezbe_skice']
    roots=[ET.parse(ROOT/(n+'.svg')).getroot() for n in names]
    for name,root in zip(names,roots):
        ids=[e.get('id') for e in root.iter() if e.get('id')]
        check(len(ids)==len(set(ids)),name+': unique IDs')
        check(not any(e.tag.endswith('filter') for e in root.iter()),name+': no shadow filter')
    intro,kin,combined,ethanol,micro,bearing,z=roots
    for root,p in [(intro,'u02fup_'),(kin,'u02fkv_'),(combined,'u02v2vk_')]:shear(root,p+'shear')
    for root,p in [(intro,'u02fup_'),(combined,'u02v2vk_'),(ethanol,'u02fku_')]:
        ar,wl,wr,surface=capillary(root,p+'cap')[0]
        tangent_forces(root,p+'cap',ar,18)
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
    for i in range(2):
        circle=node(z,f'u02vs_z2outer{i}')
        close(math.dist(*line(node(z,f'u02vs_z2diameter{i}'))),2*float(circle.get('r')),'Z2: true diameter')
    check(float(node(z,'u02vs_z2inner').get('r'))<float(node(z,'u02vs_z2outer1').get('r')),'Z2: two separate soap-film interfaces')
    up=rect(node(z,'u02vs_z3upperFluid'));down=rect(node(z,'u02vs_z3lowerFluid'));plate=rect(node(z,'u02vs_z3moving'))
    close(down[3]/up[3],2,'Z3: gap ratio 2')
    for i,(a,b) in enumerate((line(node(z,'u02vs_z3profile0')),line(node(z,'u02vs_z3profile1')))):
        if i==0:close(a[1],up[1],'Z3 upper zero');close(b[1],plate[1],'Z3 upper moving wall')
        else:close(a[1],plate[1]+plate[3],'Z3 lower moving wall');close(b[1],down[1]+down[3],'Z3 lower zero')
        check(delta(node(z,f'u02vs_z3drag{i}'))[0]<0,'Z3: both resistances point left')
        dimension(z,f'u02vs_z3gap{i+1}',(26 if i==0 else 278,up[1] if i==0 else down[1]),(26 if i==0 else 278,up[1]+up[3] if i==0 else down[1]+down[3]))
    cap=capillary(z,'u02vs_z4',2)
    widths=[r[2][0]-r[1][0]-r[1][2] for r in cap]
    close(widths[1]/widths[0],2,'Z4: diameter ratio 2')
    heights=[]
    for i,(ar,wl,wr,surface) in enumerate(cap):
        close(ar[3],18,'Z4: each angle is 18 degrees')
        ln=line(node(z,f'u02vs_z4height{i}'))
        close(ln[0][1],ar[1]+ar[2],'Z4: meniscus endpoint');close(ln[1][1],surface,'Z4: free-surface endpoint')
        heights.append(math.dist(*ln))
    close(heights[0]/heights[1],2,'Z4: inverse height ratio')
    ar,wl,wr,surface=capillary(z,'u02vs_z6',convex=True)[0]
    close(2*ar[2]/(wr[0]-wl[0]-wl[2]),1.8/.5,'Z6: D/d nominal ratio')
    dimension(z,'u02vs_z6height',(269,wl[1]),(269,surface))
    close(math.dist(*line(node(z,'u02vs_z6dropDiameter'))),2*ar[2],'Z6: actual drop diameter')
    for i in range(2):
        x,y,w,h=rect(node(bearing,f'u02flt_b{i}fluid'));a,b=line(node(bearing,f'u02flt_b{i}profile'))
        close(a[1],y,'Bearing: zero at bushing');close(b[1],y+h,'Bearing: speed at shaft')
        check(delta(node(bearing,f'u02flt_b{i}drag'))[0]<0<delta(node(bearing,f'u02flt_b{i}speed'))[0],'Bearing: oil opposes shaft motion')
    dimension(bearing,'u02flt_gap',(335,142),(335,214))
    shaft=node(bearing,'u02flt_shaftSection')
    close(math.dist(*line(node(bearing,'u02flt_shaftDiameter'))),2*float(shaft.get('r')),'Bearing: shaft diameter')
    for id,sign in [('rotation',1),('resistance',-1)]:
        pts=path(node(bearing,'u02flt_'+id))
        cross=sum((a[0]-123)*(b[1]-410)-(a[1]-410)*(b[0]-123) for a,b in zip(pts,pts[1:]))
        check(sign*cross>0,'Bearing: resisting moment opposite angular speed')
    print('U02 SVG PASS: 7 images; open immersed mouths, continuous liquid, circular menisci and 18° tangents, no-slip profiles, force directions, true dimensions and ratios.')


if __name__=='__main__':main()
