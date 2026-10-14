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

from sketch_style import check_uniform_fluid

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
            if e.get('id', '').endswith('fluid') and e.get('fill') != 'none':
                check(e.get('d').count('M') == 1 and e.get('stroke') == 'none', 'Jedna povezana ispuna bez unutarnjih pregrada')
                check_uniform_fluid(e)
    intro, p1, p2, p3, p4, p5, ex = roots
    guide(intro, 'u14intro_flow', 150)
    triangle(intro, 'u14intro_inletTriangle', 8, (16, 0), 5)
    duct(intro, 'u14intro_duct', 8, 20)
    direction(intro, 'u14intro_thrust', 180)
    direction(intro, 'u14intro_shipMotion', 180)
    close(guide(p1, 'u14p1_flow', 120, 24/19), delta(node(p1, 'u14p1_b'))[1], 'P1: kota stvarne širine ulaza')
    direction(p1, 'u14p1_outflow', 120)
    angle(p1, 'u14p1_turnAngle', 120)
    # P2 (datoteka fig_relativni_dotok): aktuatorski disk propelera u napredovanju.
    rho, FT, vA, D = 1025.0, 160e3, 6.0, 3.2
    CT = FT/(0.5*rho*vA*vA*math.pi*D*D/4)
    vd = vA*(1+math.sqrt(1+CT))/2
    vw = 2*vd-vA
    tube = path(node(p2, 'u14p2_tubefluid'))
    check(node(p2, 'u14p2_controlVolume').get('d') == node(p2, 'u14p2_tubefluid').get('d'),
          'P2: kontrolni volumen obuhvaća točno strujnu cijev')
    def width_at(x):
        ys = [y for px, y in tube if abs(px-x) < 1e-6]
        check(len(ys) >= 2, 'P2: presjek strujne cijevi na x=%g' % x)
        return max(ys)-min(ys)
    disk = line(node(p2, 'u14p2_disk'))
    close(disk[0][0], disk[1][0], 'P2: disk je okomit na os')
    w_inf, w_disk, w_w = width_at(60), width_at(disk[0][0]), width_at(400)
    close(w_disk, disk[1][1]-disk[0][1], 'P2: disk završava na rubu strujne cijevi')
    close((w_inf/w_disk)**2, vd/vA, 'P2: uzvodni presjek iz kontinuiteta', tol=2e-5)
    close((w_w/w_disk)**2, vd/vw, 'P2: presjek dalekog traga iz kontinuiteta', tol=2e-5)
    check(w_inf > w_disk > w_w, 'P2: strujna cijev se sužava nizvodno')
    check(all(y > disk[0][1]-1e-9 and y < disk[1][1]+1e-9 for px, y in tube if abs(px-disk[0][0]) < 1e-6),
          'P2: fluid prolazi kroz cijeli propusni disk')
    lengths = {}
    for name in ('vA', 'vd', 'vw'):
        dx, dy = delta(node(p2, 'u14p2_'+name))
        close(dy, 0, 'P2: brzina duž osi')
        check(dx > 0, 'P2: brzina prema krmi')
        lengths[name] = dx
    close(lengths['vd']/lengths['vA'], vd/vA, 'P2: v_d iz Froudeova teorema u zajedničkom mjerilu', tol=2e-5)
    close(lengths['vw']/lengths['vA'], vw/vA, 'P2: v_j (oznaka u14p2_vw) iz bilance količine gibanja', tol=2e-5)
    close(lengths['vd'], (lengths['vA']+lengths['vw'])/2, 'P2: brzina u disku je aritmetička sredina', tol=2e-5)
    direction(p2, 'u14p2_thrust', 180)
    close(delta(node(p2, 'u14p2_D'))[1], w_disk, 'P2: kota D mjeri promjer diska')

    # P3 (datoteka val3_pokretna_lopatica): radijalno kolo crpke i trokuti brzina.
    om = 2*math.pi*1450/60
    r1, r2, b1, b2, Q = .060, .130, .035, .020, .045
    u1, u2 = om*r1, om*r2
    cm1, cm2 = Q/(2*math.pi*r1*b1), Q/(2*math.pi*r2*b2)
    beta1, beta2 = math.atan2(cm1, u1), math.radians(25)
    rim, eye, hub = node(p3, 'u14p3_rim'), node(p3, 'u14p3_eye'), node(p3, 'u14p3_hub')
    centre = tuple(float(rim.get(k)) for k in ('cx', 'cy'))
    same_point(centre, tuple(float(eye.get(k)) for k in ('cx', 'cy')), 'P3: koncentrični rub i oko kola')
    same_point(centre, tuple(float(hub.get(k)) for k in ('cx', 'cy')), 'P3: koncentrična glavina')
    R2, R1, Rh = float(rim.get('r')), float(eye.get('r')), float(hub.get('r'))
    close(R2/R1, r2/r1, 'P3: omjer polumjera 130:60')
    check(eye.get('fill') == '#dcebf1', 'P3: oko kola (aksijalni ulaz) prikazano je kao fluid, ne kao krutina')
    check(0 < Rh <= 0.35*R1, 'P3: glavina na vratilu znatno je manja od r1 i ne zatvara oko kola')
    check(hub.get('fill', '').startswith('url(#u14p3_hatch'), 'P3: glavina je šrafirana krutina')
    import re as _re
    blades = [e for e in p3.iter() if _re.fullmatch(r'u14p3_blade\d+', e.get('id', ''))]
    check(len(blades) == 6, 'P3: šest lopatica')
    for blade in blades:
        nums = list(map(float, _re.findall(r'-?\d+(?:\.\d+)?', blade.get('d'))))
        P0, P1, P2 = (nums[0], nums[1]), (nums[2], nums[3]), (nums[4], nums[5])
        close(math.dist(P0, centre), R1, 'P3: lopatica počinje na r1 (rub oka kola)')
        close(math.dist(P2, centre), R2, 'P3: lopatica završava na rubu kola')
        for point, d, beta in ((P0, (P1[0]-P0[0], P1[1]-P0[1]), beta1), (P2, (P2[0]-P1[0], P2[1]-P1[1]), beta2)):
            phi = math.atan2(point[1]-centre[1], point[0]-centre[0])
            t = (-math.sin(phi), math.cos(phi))   # smjer vrtnje (u smjeru kazaljke na zaslonu)
            rad = (math.cos(phi), math.sin(phi))
            ang = math.atan2(d[0]*rad[0]+d[1]*rad[1], -(d[0]*t[0]+d[1]*t[1]))
            close(ang, beta, 'P3: kut lopatice od smjera -u iz podataka', tol=1e-6)
    rotation = path(node(p3, 'u14p3_rotation'))
    a, b = rotation[-2:]
    check((a[0]-centre[0])*(b[1]-a[1])-(a[1]-centre[1])*(b[0]-a[0]) > 0, 'P3: vrtnja u smjeru kazaljke, kao pozitivni tangencijalni smjer')
    spoke = line(node(p3, 'u14p3_r2'))
    same_point(spoke[0], centre, 'P3: kota r2 od osi'); close(math.dist(spoke[1], centre), R2, 'P3: kota r2 do ruba')
    spoke = line(node(p3, 'u14p3_r1'))
    same_point(spoke[0], centre, 'P3: kota r1 od osi'); close(math.dist(spoke[1], centre), R1, 'P3: kota r1 do ruba oka kola')
    triangle(p3, 'u14p3_inletTriangle', u1, (-u1, cm1), 8)
    triangle(p3, 'u14p3_outletTriangle', u2, (-cm2/math.tan(beta2), cm2), 8)
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
    # Krak tangencijalne sile M = F_x r: r završava na osi mlaza (mlaz tangencijalan na kružnicu r).
    jet_axis = (path(node(p5, 'u14p5_flowwall0'))[0][1]+path(node(p5, 'u14p5_flowwall1'))[0][1])/2
    close(rim_point[1], jet_axis, 'P5: B i kota r na osi mlaza, ne na dnu lopatice')
    close(line(node(p5, 'u14p5_inflow'))[0][1], jet_axis, 'P5: c1 na osi mlaza')
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
    print('U14 SVG PASS: 7 slika; otvoreni tokovi, strujna cijev diska, radijalno kolo, kote/kutovi, stvarni trokuti brzina, radijus i vrtnja, reakcije, kontinuitet i četiri mlaza.')


if __name__ == '__main__':
    main()
