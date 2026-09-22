"""Stvarna SVG geometrija U14: otvoreni tokovi, kote i trokuti brzina.

Čita sedam objavljenih SVG-ova s naslijeđenim prefiksom u12. Ne ovisi o
autorskom generatoru. Vizualni pregled oznaka i numerički verifier ostaju
zasebne provjere.
"""
import math
from pathlib import Path
import xml.etree.ElementTree as ET
from check_u10_sketch_geometry import check, node, path, line, delta, plate, wall_and_openings
from check_u13_sketch_geometry import close, graph, rect

ROOT = Path(__file__).resolve().parents[1] / 'assets' / 'print'


def same_point(a, b, message):
    close(math.dist(a, b), 0, message)


def triangle(root, prefix, u, w, scale):
    """Check actual arrow lengths, signs and endpoint closure against SI data."""
    arrows = {k: line(node(root, prefix+k)) for k in ('c', 'u', 'w')}
    values = {'u': (u, 0), 'w': w, 'c': (u+w[0], w[1])}
    for name, expected in values.items():
        actual = delta(node(root, prefix+name))
        same_point(actual, (scale*expected[0], -scale*expected[1]),
                   prefix+': pogrešan vektor '+name)
    same_point(arrows['u'][1], arrows['w'][0], prefix+': u završava gdje w počinje')
    if w[1]:
        same_point(arrows['u'][0], arrows['c'][0], prefix+': isti početak u i c')
        same_point(arrows['w'][1], arrows['c'][1], prefix+': c = u + w')
    else:
        close(arrows['u'][0][0], arrows['c'][0][0], prefix+': projekcija početka kolinearnih vektora')
        close(arrows['w'][1][0], arrows['c'][1][0], prefix+': projekcija kraja kolinearnih vektora')


def direction(root, id, degrees):
    dx, dy = delta(node(root, id))
    error = (math.degrees(math.atan2(-dy, dx))-degrees+180) % 360-180
    close(error, 0, id+': smjer vektora', tol=2e-5)


def guide(root, prefix, degrees, width_ratio=None):
    inner = path(node(root, prefix+'freeEdge'))
    outer = path(node(root, prefix+'outerEdge'))
    center = path(node(root, prefix+'centerline'))
    check(len(inner) == len(outer) == len(center)+1, prefix+': rubovi i os opisuju isti zavoj')
    widths = []
    for a, b, c in zip(inner, outer, center):
        same_point(tuple((a[k]+b[k])/2 for k in (0, 1)), c, prefix+': širina centrirana na os')
        widths.append(math.dist(a, b))
    check(min(widths) > 0, prefix+': tok se ne smije zatvoriti')
    check(all(b+2e-5 >= a for a, b in zip(widths, widths[1:])), prefix+': bez lokalnih suženja')
    if width_ratio is not None:
        close(widths[-1]/widths[0], width_ratio, prefix+': kontinuitet pravokutnog presjeka stalne dubine')
    vi = tuple(inner[-1][k]-inner[-2][k] for k in (0, 1))
    vo = tuple(outer[-1][k]-outer[-2][k] for k in (0, 1))
    same_point(vi, vo, prefix+': paralelni rubovi slobodnog izlaza')
    close(math.degrees(math.atan2(-vi[1], vi[0])), degrees, prefix+': stvarni kut izlaza')
    section = line(node(root, prefix+'outletSection'))
    same_point(section[0], inner[-2], prefix+': presjek na unutarnjem rubu')
    same_point(section[1], outer[-2], prefix+': presjek na vanjskom rubu')
    normal = tuple(section[1][k]-section[0][k] for k in (0, 1))
    close(sum(normal[k]*vi[k] for k in (0, 1)), 0, prefix+': izlazni presjek normalan na tok')
    wall0, wall1 = (path(node(root, prefix+'wall'+str(i))) for i in (0, 1))
    inlet = tuple((wall0[0][k]+wall1[0][k])/2 for k in (0, 1))
    outlet = tuple((inner[-1][k]+outer[-1][k])/2 for k in (0, 1))
    wall_and_openings(root, prefix, [inlet, outlet])
    return widths[0]


def angle(root, prefix, degrees):
    a, b = line(node(root, prefix+'startRay')), line(node(root, prefix+'endRay'))
    same_point(a[0], b[0], prefix+': oba kraka imaju isti vrh')
    direction(root, prefix+'startRay', 0)
    direction(root, prefix+'endRay', degrees)
    arc = path(node(root, prefix))
    for point in arc:
        close(math.dist(a[0], point), math.dist(a[0], arc[0]), prefix+': kružna kota kuta')
    for point, ray in ((arc[0], a), (arc[-1], b)):
        va = tuple(point[k]-ray[0][k] for k in (0, 1))
        vb = tuple(ray[1][k]-ray[0][k] for k in (0, 1))
        close(va[0]*vb[1]-va[1]*vb[0], 0, prefix+': luk završava na kraku')


def duct(root, prefix, vi, vo):
    top, bottom = (path(node(root, prefix+'wall'+str(i))) for i in (0, 1))
    di, do = bottom[-1][1]-top[0][1], bottom[0][1]-top[-1][1]
    close((di/do)**2, vo/vi, prefix+': kružni presjeci zatvaraju kontinuitet')
    wall_and_openings(root, prefix, [(top[0][0], top[0][1]+di/2), (top[-1][0], top[-1][1]+do/2)])
    check(node(root, prefix+'pumpSymbol').get('fill') == 'none', prefix+': simbol stroja nije pregrada')
    return di, do


def inside(point, polygon):
    x, y = point
    crossings = 0
    for (xa, ya), (xb, yb) in zip(polygon, polygon[1:]):
        if (ya > y) != (yb > y) and x < xa+(y-ya)*(xb-xa)/(yb-ya):
            crossings += 1
    return crossings % 2 == 1


def main():
    names = ('fig_uvod_pregled', 'val1_vodilica_mlaza', 'fig_relativni_dotok',
             'val3_pokretna_lopatica', 'ch1_pokretna_zakrivljena_lopatica',
             'ch2_pelton_rotor_moment', 'vjezbe_skice')
    roots = [ET.parse(ROOT/('u12_'+name+'.svg')).getroot() for name in names]
    for root in roots:
        ids = [e.get('id') for e in root.iter() if e.get('id')]
        check(len(ids) == len(set(ids)), 'SVG ID-jevi moraju biti jedinstveni')
        check(not any(e.tag.endswith('filter') for e in root.iter()), 'Nema sjena preko povezanog fluida')
        for e in root.iter():
            if e.get('id', '').endswith('fluid') and e.get('fill', '').startswith('url('):
                check(e.get('d').count('M') == 1 and e.get('stroke') == 'none', 'Jedna povezana ispuna bez unutarnjih pregrada')
                gradient = node(root, e.get('fill')[5:-1])
                check(gradient.get('gradientUnits') == 'userSpaceOnUse', 'Isti prostorni gradijent kroz cijeli tok')
    intro, p1, p2, p3, p4, p5, ex = roots
    guide(intro, 'u14intro_flow', 150)
    triangle(intro, 'u14intro_inletTriangle', 8, (16, 0), 5)
    duct(intro, 'u14intro_duct', 8, 20)
    direction(intro, 'u14intro_thrust', 180)
    direction(intro, 'u14intro_shipMotion', 180)
    close(guide(p1, 'u14p1_flow', 120, 24/19), delta(node(p1, 'u14p1_b'))[1], 'P1: kota stvarne širine ulaza')
    direction(p1, 'u14p1_outflow', 120)
    angle(p1, 'u14p1_turnAngle', 120)
    for r, prefix, c1, u in ((p2, 'u14p2_', 22, 8), (p3, 'u14p3_', 24, 9)):
        plate(r, prefix+'jet')
        triangle(r, prefix+'inletTriangle', u, (c1-u, 0), 5)
        top, bottom = line(node(r, prefix+'jettop')), line(node(r, prefix+'jetbottom'))
        close(bottom[0][1]-top[0][1], delta(node(r, prefix+'d'))[1], prefix+': d normalan na ulazni mlaz')
        for name, sign in (('outTop', -1), ('outBottom', 1)):
            dx, dy = delta(node(r, prefix+name))
            close(dx, 3*u, prefix+': apsolutni izlaz ima komponentu u')
            close(dy, sign*3*(c1-u), prefix+': relativni izlaz duž ploče')
            arrow = line(node(r, prefix+name))
            solid = rect(node(r, prefix+'jetplate'))
            check(arrow[0][1] < solid[1] if sign == -1 else arrow[0][1] > solid[1]+solid[3],
                  prefix+': apsolutni izlaz počinje izvan ruba ploče')
    width = guide(p4, 'u14p4_flow', 150)
    close(width, delta(node(p4, 'u14p4_d'))[1], 'P4: stvarna poprečna kota d')
    triangle(p4, 'u14p4_inletTriangle', 10, (16, 0), 7)
    triangle(p4, 'u14p4_outletTriangle', 10, (-14.4*math.cos(math.pi/6), 7.2), 7)
    direction(p4, 'u14p4_relativeExit', 150)
    width = guide(p5, 'u14p5_flow', 160)
    close(width, delta(node(p5, 'u14p5_d'))[1], 'P5: stvarna poprečna kota d')
    u = 2*math.pi*320/60*.46
    w = (-.9*(31-u)*math.cos(math.radians(20)), .9*(31-u)*math.sin(math.radians(20)))
    triangle(p5, 'u14p5_inletTriangle', u, (31-u, 0), 4)
    triangle(p5, 'u14p5_outletTriangle', u, w, 4)
    orbit = node(p5, 'u14p5_orbit')
    center = tuple(float(orbit.get(k)) for k in ('cx', 'cy'))
    rim = node(p5, 'u14p5_rimPoint')
    rim_point = tuple(float(rim.get(k)) for k in ('cx', 'cy'))
    radius = float(orbit.get('r'))
    same_point(rim_point, (center[0], center[1]-radius), 'P5: B na vrhu kružne putanje')
    dim = line(node(p5, 'u14p5_radius'))
    close(dim[0][1], rim_point[1], 'P5: početak kote na obodu')
    close(dim[1][1], center[1], 'P5: kraj kote na osi')
    fluid = path(node(p5, 'u14p5_flowfluid'))
    spoke = line(node(p5, 'u14p5_spoke'))
    for j in range(41):
        y = spoke[0][1]+j/40*(spoke[1][1]-spoke[0][1])
        for x in (center[0]-3, center[0], center[0]+3):
            check(not inside((x, y), fluid), 'P5: kruti krak rotora ne smije ući u vodu')
    rotation = path(node(p5, 'u14p5_rotation'))
    a, b = rotation[-2:]
    check((a[0]-center[0])*(b[1]-a[1])-(a[1]-center[1])*(b[0]-a[0]) > 0, 'P5: vrtnja u smjeru kazaljke')
    direction(p5, 'u14p5_motion', 0)
    for r, prefix in ((p1, 'u14p1_'), (p4, 'u14p4_'), (p5, 'u14p5_'), (ex, 'u14ex_z3')):
        direction(r, prefix+'forceX', 0)
        direction(r, prefix+'forceY', -90)
    for n in range(1, 7):
        node(ex, 'u14ex_z'+str(n))
    plate(ex, 'u14ex_z1')
    close(delta(node(ex, 'u14ex_z1d'))[1], 26, 'Z1: poprečna kota mlaza')
    guide(ex, 'u14ex_z2', 110, 1)
    angle(ex, 'u14ex_z2angle', 110)
    fx, fy = 26*26*.03*.016*998*(1-math.cos(math.radians(110))), -26*26*.03*.016*998*math.sin(math.radians(110))
    direction(ex, 'u14ex_z2reaction', math.degrees(math.atan2(-fy, -fx)))
    direction(p1, 'u14p1_reaction', math.degrees(math.atan2(198.635, -404.406)))
    guide(ex, 'u14ex_z3', math.degrees(math.atan2(8.5, 32-625/18-12)))
    triangle(ex, 'u14ex_z4one', 200*.06, (5-200*.06, 4), 5)
    triangle(ex, 'u14ex_z4two', 200*.14, (20-200*.14, 6), 5)
    for i, vj in enumerate((20, 30)):
        di, do = duct(ex, 'u14ex_z5duct'+str(i), 8, vj)
        Q = 2000/(1000*(vj-8))
        close(do, 280*math.sqrt(4*Q/(math.pi*vj)), 'Z5: promjer iz potiska i kontinuiteta u zajedničkoj skali')
        close(delta(node(ex, 'u14ex_z5d'+str(i)))[1], do, 'Z5: kota završava na unutarnjim rubovima')
        close(delta(node(ex, 'u14ex_z5inflow'+str(i)))[0], 3*8, 'Z5: zajednička skala ulaznih brzina')
        close(delta(node(ex, 'u14ex_z5outflow'+str(i)))[0], 3*vj, 'Z5: zajednička skala izlaznih brzina')
    parts, width = graph(ex, 'u14ex_z6manifold')
    check(len(parts) == 5, 'Z6: glavni dovod i četiri izlazna ogranka')
    for i, part in enumerate(parts[1:]):
        x, y, w, h = rect(node(ex, 'u14ex_z6jet'+str(i)))
        same_point(part[-1], (x+w/2, y), 'Z6: slobodni mlaz počinje na kraju otvorene sapnice')
        close(w, width, 'Z6: nema suženja ili proširenja na spoju')
        direction(ex, 'u14ex_z6outflow'+str(i), -90)
    close(delta(node(ex, 'u14ex_z6d'))[0], width, 'Z6: kota stvarnoga provrta')
    direction(ex, 'u14ex_z6inletLeft', 0)
    direction(ex, 'u14ex_z6inletRight', 180)
    direction(ex, 'u14ex_z6thrust', 90)
    direction(ex, 'u14ex_z6weight', -90)
    print('U14 SVG PASS: 7 slika; otvoreni tokovi, nepropusne ploče, kote/kutovi, stvarni trokuti brzina, radijus i vrtnja, reakcije, kontinuitet i četiri mlaza.')


if __name__ == '__main__':
    main()
