"""Fizikalne geometrijske provjere stvarnih SVG izvora kanonskog U08.

Pokrenuti nakon promjene skica; nije zamjena za pregled konačnog PDF/HTML-a.
Brojevi zadataka koriste naslijeđene SVG prefikse u09, kao i kanonski izvor.
"""
from pathlib import Path
import math
import re
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1] / "assets" / "print"
NS = {"s": "http://www.w3.org/2000/svg"}
CHECKS = []


def check(condition, message):
    if not condition:
        raise AssertionError(message)
    CHECKS.append(message)


def near(value, expected, message, tolerance=1e-6):
    check(abs(value-expected) <= tolerance, message)


def svg(name, prefix):
    root = ET.parse(ROOT / name).getroot()
    ids = [n.get("id") for n in root.iter() if n.get("id")]
    check(len(ids) == len(set(ids)), name + ": jedinstveni ID-jevi")
    check(all(i.startswith(prefix) for i in ids), name + ": izolirani ID-jevi")
    check(not root.findall('.//s:filter', NS), name + ": nema sjena iz SVG filtara")
    return root


def element(root, id):
    found = root.find(f'.//*[@id="{id}"]')
    if found is None:
        raise AssertionError("Nedostaje geometrijski element " + id)
    return found


def numbers(node):
    return [float(x) for x in re.findall(r'-?\d+(?:\.\d+)?', node.get('d', ''))]


def dimension(root, id):
    values = numbers(element(root, id))
    check(len(values) == 4, id + ": jedna ravna kota")
    return values


def length(root, id):
    x1,y1,x2,y2 = dimension(root,id)
    return math.hypot(x2-x1,y2-y1)


def dot(root, id):
    e=element(root,id)
    return float(e.get('cx')),float(e.get('cy'))


def pipe(root, prefix):
    wall,fluid=(element(root,prefix+part) for part in ('wall','water'))
    check(wall.get('d') == fluid.get('d'), prefix+": stijenka i fluid imaju istu os")
    check(wall.get('stroke-linecap') == fluid.get('stroke-linecap') == 'butt',
          prefix+": otvori nemaju čep od zaobljenog završetka")
    check(float(wall.get('stroke-width')) > float(fluid.get('stroke-width')) > 0,
          prefix+": pozitivna debljina stijenke i otvor fluida")


def parabola(root,id,scale,head,fall):
    e=element(root,id)
    check(re.sub(r'[-\d.\s,]','',e.get('d')) == 'MQ', id+": kvadratna putanja")
    x0,y0,xc,yc,x1,y1=numbers(e)
    near(yc,y0,id+": vodoravna početna tangenta")
    near(xc,(x0+x1)/2,id+": x je linearan u vremenu leta")
    near((y1-y0)/scale,fall,id+": pad do kote tla")
    near((x1-x0)/scale,2*math.sqrt(head*fall),id+": Bernoulli i balistički domet")
    # At an interior point the curve must also satisfy y=g*x²/(2*v0²).
    t=.37
    xt=2*(1-t)*t*xc+(t*t)*x1+(1-t)**2*x0
    yt=2*(1-t)*t*yc+(t*t)*y1+(1-t)**2*y0
    near((yt-y0)/scale,((xt-x0)/scale)**2/(4*head),id+": unutarnja točka parabole")


def run():
    z=svg('u09_vjezbe_skice.svg','u09vs_')
    near(length(z,'u09vs_z3D1')/length(z,'u09vs_z3D2'),120/70,
         "Z3: omjer poprečnih promjera 120:70")
    # Both inlet and outlet tangents are horizontal; the bend never closes.
    top=element(z,'u09vs_z3top').get('d')
    bottom=element(z,'u09vs_z3bottom').get('d')
    check(top.endswith('H365') and bottom.endswith('H365'),"Z3: vodoravni izlaz")
    a=length(z,'u09vs_z6zc')/1.7
    near(length(z,'u09vs_z6dz')/2.6,a,"Z6: zajednička skala visinskih kota")
    near(length(z,'u09vs_z6height')/1.2,a,"Z6: visina izlaza prema tlu")
    A,C,B=(dot(z,'u09vs_z6'+name)[1] for name in ('A','C','B'))
    near((A-C)/a,1.7,"Z6: vrh C se kotira na osi")
    near((B-A)/a,2.6,"Z6: pogonska visina A–B")
    parabola(z,'u09vs_z6jet',a,2.6,1.2)
    pipe(z,'u09vs_z6pipe');pipe(z,'u09vs_z4probe')
    # Sensor height is read from the actual closed instrument body, not its label.
    sensor=next(e for e in element(z,'u09vs_z4').findall('s:rect',NS)
                if e.get('x')=='265')
    dz=dimension(z,'u09vs_z4dz')
    near(dz[1],float(sensor.get('y'))+float(sensor.get('height')),
         "Z4: gornja kota na priključku senzora")
    near(dz[3],numbers(element(z,'u09vs_z4probewater'))[1],"Z4: donja kota na Pitotovu otvoru")

    p2=svg('u09_val2_slobodni_mlaz.svg','u09v2_')
    scale=length(p2,'u09v2_H')/4
    for i,h in enumerate((1,2,3),1):
        near(length(p2,f'u09v2_h{i}')/scale,h,f"P2: kota h{i}")
        parabola(p2,f'u09v2_jet{i}',scale,4-h,h)
        y=numbers(element(p2,f'u09v2_jet{i}'))[1]
        walls=[e for e in p2.findall('.//s:rect',NS) if e.get('x')=='220' and e.get('stroke')=='#3a4a56']
        check(all(not float(e.get('y'))<y<float(e.get('y'))+float(e.get('height')) for e in walls),
              f"P2: otvor {i} nije prekriven stijenkama")

    p3=svg('u09_val3_idealni_sifon.svg','u09v3is_')
    A,C,B=(dot(p3,'u09v3is_'+name)[1] for name in ('A','C','B'))
    scale=length(p3,'u09v3is_dz')/3.6
    near((A-C)/scale,2.2,"P3: kota vrha od površine")
    near((B-A)/scale,3.6,"P3: kota slobodnog izlaza od površine")
    pipe(p3,'u09v3is_pipe')
    tube=element(p3,'u09v3is_pipewater')
    near(length(p3,'u09v3is_diameter'),float(tube.get('stroke-width')),
         "P3: D je unutarnji promjer")
    jet=numbers(element(p3,'u09v3is_jet'))
    check(min(jet[1::2])==B and max(jet[1::2])>B,"P3: slobodan mlaz počinje na izlazu B")
    # Tank A right rim is lower than the pipe's outer lower edge at the crossing.
    check(C+(float(tube.get('stroke-width'))+4)/2<149,"P3: cijev iznad krutog ruba bazena")

    p4=svg('u09_ch1_bypass_sifon_suzenje_mlaz.svg','u09ch1_')
    scale=length(p4,'u09ch1_heightA')/4.2
    for id,value in [('heightC',1.5),('dropAB',2.8),('heightB',1.4)]:
        near(length(p4,'u09ch1_'+id)/scale,value,"P4: dosljedna kota "+id)
    near(length(p4,'u09ch1_dC')/length(p4,'u09ch1_D'),.8,"P4: grlo 80:100")
    near(float(element(p4,'u09ch1_leftwater').get('stroke-width')),
         length(p4,'u09ch1_D'),"P4: D je unutarnji otvor cijevi")
    pipe(p4,'u09ch1_left');pipe(p4,'u09ch1_right')
    check(95 < numbers(element(p4,'u09ch1_leftwater'))[0] < 220,
          "P4: ulazna os unutar bazena")
    check(dot(p4,'u09ch1_C')[1]+12<251,"P4: sifon prolazi iznad ruba")
    parabola(p4,'u09ch1_jet',scale,2.8,1.4)

    p5=svg('u09_fig_venturijeva_cijev.svg','u09vent_')
    near(length(p5,'u09vent_D1')/length(p5,'u09vent_D2'),2,"P5: omjer promjera 2:1")
    yl=float(element(p5,'u09vent_leftinterface').get('y1'))
    yr=float(element(p5,'u09vent_rightinterface').get('y1'))
    check(yl>yr,"P5: živa niže na strani većeg tlaka")
    near(yl-yr,length(p5,'u09vent_dh'),"P5: kota završava na sučeljima")
    near(length(p5,'u09vent_dh')/length(p5,'u09vent_D1'),180/60,
         "P5: razlika razina i promjeri imaju jednaku duljinsku skalu")
    # Read the actual lower wall path gaps around the two open ports.
    path=element(p5,'u09vent_bottom').get('d')
    check('H98 M110' in path and 'H264 M276' in path,"P5: otvoreni tlačni priključci")
    pipe(p5,'u09vent_mercury')

    p1=svg('u09_egl_hgl_schema.svg','u09egl_')
    near(length(p1,'u09egl_head2')/length(p1,'u09egl_head1'),(.070/.0185)**2,
         "P1: omjer brzinskih visina jednak kvadratu omjera površina")
    for id,area in [('head1',.070),('head2',.0185)]:
        near(length(p1,'u09egl_'+id)/5,(.68/1.2/area)**2/(2*9.81),"P1: skala "+id)

    intro=svg('u09_fig_uvod_pregled.svg','u09intro_')
    for x in ('145','362'):
        stack=[e for e in intro.findall('.//s:rect',NS) if e.get('x')==x]
        near(sum(float(e.get('height')) for e in stack),8*36,"Uvod: jednaka ukupna energija stupca "+x)
    print(f'U08 SVG geometry PASS: {len(CHECKS)} provjera; potreban i vizualni pregled.')


if __name__ == '__main__':
    run()
