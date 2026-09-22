"""Provjera geometrije istisnine u stvarnim SVG skicama javnog U06.

Pokrenuti zasebno: python tools/check_u06_sketch_geometry.py.
Integrira širinu potopljenog poligona po vodoravnim trakama, ne koristi
generator crteža. Dopunjuje numerički verifier i vizualni pregled.
"""

from pathlib import Path
import math
import xml.etree.ElementTree as ET

ASSETS = Path(__file__).resolve().parent.parent / "assets/print"


def read(name):
    root = ET.parse(ASSETS / name).getroot()
    ids = [n.get("id") for n in root.iter() if n.get("id")]
    assert len(ids) == len(set(ids)), name
    return root, {n.get("id"): n for n in root.iter() if n.get("id")}


def points(node):
    return [tuple(map(float, pair.split(','))) for pair in node.get('points').split()]


def integrate(poly, surface, interface=None, rho_o=1000, rho_w=1000):
    # On each interval between vertices/interfaces the polygon edges are
    # linear. Two-point Gauss quadrature integrates area and first moments.
    levels = sorted(set([surface] + [y for _, y in poly if y > surface]
                        + ([interface] if interface is not None else [])))
    mass = mx = my = 0
    for lo, hi in zip(levels, levels[1:]):
        for xi in (-1/math.sqrt(3), 1/math.sqrt(3)):
            y = (lo+hi)/2 + xi*(hi-lo)/2
            xs = []
            for (x1,y1),(x2,y2) in zip(poly,poly[1:]+poly[:1]):
                if min(y1,y2) < y < max(y1,y2):
                    xs.append(x1+(x2-x1)*(y-y1)/(y2-y1))
            if not xs:
                continue
            assert len(xs) == 2
            left, right = sorted(xs)
            rho = rho_o if interface is not None and y < interface else rho_w
            dm = rho*(right-left)*(hi-lo)/2
            mass += dm; mx += dm*(left+right)/2; my += dm*y
    return mx/mass, my/mass


def check_hull(nodes, prefix, width, height, angle, rho_o=1000, rho_w=1000):
    hull = nodes[prefix+'hull']
    assert hull.tag.endswith('polygon') and hull.get('fill') not in ('none', None)
    p = points(hull)
    assert len(p) == 4
    edges = [(q[0]-v[0], q[1]-v[1]) for v,q in zip(p,p[1:]+p[:1])]
    lengths = [math.hypot(*e) for e in edges]
    assert abs(lengths[0]/lengths[1]-width/height) < 1e-6
    for i in range(4):
        a,b = edges[i],edges[(i+1)%4]
        assert abs(a[0]*b[0]+a[1]*b[1])/(lengths[i]*lengths[(i+1)%4]) < 1e-7
    assert abs(math.degrees(math.atan2(-edges[0][1],edges[0][0]))-angle) < 1e-5
    surface = nodes[prefix+'free-surface']
    assert surface.get('y1') == surface.get('y2')
    y = float(surface.get('y1'))
    inter = nodes.get(prefix+'interface')
    yi = None
    if inter is not None:
        assert inter.get('y1') == inter.get('y2')
        yi = float(inter.get('y1')); assert yi > y
    # Both bottom corners are wet, both upper corners are dry.
    assert min(p[0][1],p[1][1]) > (yi if yi else y)
    assert max(p[2][1],p[3][1]) < y
    expected = integrate(p,y,yi,rho_o,rho_w)
    center = nodes[prefix+'buoyancy-center']
    assert math.dist(expected,(float(center.get('cx')),float(center.get('cy')))) < 2e-6


def main():
    cases = [
        ('u07_val2_ponton_gaz.svg','u07v2pg_fix_',1.2,.32,0,1000,1000),
        ('u07_val1_platforma_kompresor.svg','u07v1pk_fix_',1,.35,math.degrees(math.atan(.12)),1000,1000),
        ('u07_ch1_platforma_ulje_voda_ormar.svg','u07c1puf_fix_',1.2,.34,math.degrees(math.atan(.1/1.2)),800,1000),
        ('u07_ch2_poplavljen_tank.svg','u07c2pt_fix_',15,8,3.94,1000,1000),
        ('u07_fig_uvod_pregled.svg','u07fup_stab_',.7,.18,-8,1000,1000),
        ('u07_vjezbe_skice.svg','u07vs_fix_z2_',1.4,.38,0,1000,1000),
        ('u07_vjezbe_skice.svg','u07vs_fix_z3_',1.4,.5,-3,1000,1000),
        ('u07_vjezbe_skice.svg','u07vs_fix_z5_',1.5,.6,0,1000,1000),
        ('u07_vjezbe_skice.svg','u07vs_fix_z5_b_',1.5,.6,0,1000,1000),
        ('u07_vjezbe_skice.svg','u07vs_fix_z6_',1.2,.36,math.degrees(math.atan(.08/1.2)),820,998),
    ]
    for name,prefix,b,h,angle,ro,rw in cases:
        _,nodes = read(name)
        # P4 angle is verified against the published rounded 3.94 degrees.
        if prefix == 'u07c2pt_fix_':
            p = points(nodes[prefix+'hull'])
            angle = math.degrees(math.atan2(p[0][1]-p[1][1],p[1][0]-p[0][0]))
            assert abs(angle-3.94) < .005
            tank = points(nodes[prefix+'sealed-tank'])
            assert abs(math.dist(tank[0],tank[1])/math.dist(p[0],p[1])-.4) < 1e-8
            assert abs(math.dist(tank[1],tank[2])/math.dist(p[1],p[2])-3/8) < 1e-8
            assert math.dist(tank[0],p[0]) < 1e-6
        check_hull(nodes,prefix,b,h,angle,ro,rw)
        print('PASS',prefix,'rigid hull, horizontal surfaces, integrated buoyancy center')
    root,nodes = read('u07_vjezbe_skice.svg')
    assert root.get('viewBox') == '0 0 960 760'
    assert all('u07vs_fix_z'+str(i) in nodes for i in range(1,7))
    _,nodes = read('u07_fig_pumpno_kuciste.svg')
    body = nodes['u07fpk_fix_body']
    assert float(body.get('y')) > 115
    assert float(body.get('y'))+float(body.get('height')) < 393
    print('PASS six practice panels and fully submerged casing without bottom contact')


if __name__ == '__main__':
    main()
