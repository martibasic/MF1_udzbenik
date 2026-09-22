"""Provjera stvarnih SVG lukova, normala i pravaca sila u U05.

Pokrenuti iz korijena: python tools/check_u05_sketch_geometry.py.
Ovo dopunjuje numerički verifier; ne zamjenjuje vizualni pregled i provjeru
čitljivosti. Koordinate su SVG koordinate (y raste prema dolje).
"""

from pathlib import Path
import math
import re
import xml.etree.ElementTree as ET

from verify_u05_integrated import quarter_cylinder


ROOT = Path(__file__).resolve().parent.parent
ASSETS = ROOT / "assets/print"


def close(a, b, tol=1e-7):
    assert abs(a - b) < tol, (a, b)


def read(name):
    root = ET.parse(ASSETS / name).getroot()
    return root, {n.get("id"): n for n in root.iter() if n.get("id")}


def check_arc(node, cx, cy, radius, right=False):
    # Check the actual path, not only its descriptive data-* attributes.
    tokens = re.findall(r"[A-Za-z]|-?\d+(?:\.\d+)?", node.get("d"))
    assert len(tokens) == 11 and tokens[0] == "M" and tokens[3] == "A", tokens
    sx, sy = map(float, tokens[1:3])
    rx, ry, rotation, large, sweep, ex, ey = map(float, tokens[4:])
    for a, b in [(rx, radius), (ry, radius), (rotation, 0), (large, 0),
                 (sweep, 1 if right else 0), (sx, cx + radius if right else cx-radius),
                 (sy, cy), (ex, cx), (ey, cy+radius)]:
        close(a, b)


def check_normal(node, cx, cy, radius, outward=False):
    x1, y1, x2, y2 = [float(node.get(k)) for k in ("x1", "y1", "x2", "y2")]
    rx, ry, dx, dy = x2-cx, y2-cy, x2-x1, y2-y1
    close(math.hypot(rx, ry), radius)
    close(rx*dy-ry*dx, 0)
    assert (rx*dx+ry*dy > 0) == outward


def main():
    cases = [
        ("u06_val1_cetvrtina_kruga.svg", "u05p4_", 370, 245, 100, 45, 1.22, 1.83, 2.44, 1),
        ("u06_val3_cetvrtcilindricni_poklopac.svg", "u05p5_", 135, 105, 175, 105, .90, 1.20, 0, -1),
        ("u06_ch1_poklopac_spojnica.svg", "u05p6_", 355, 150, 145, 150, 1.10, 1.40, 0, 1),
    ]
    for name, prefix, cx, cy, radius, surface, R, b, h1, sign in cases:
        _, nodes = read(name)
        check_arc(nodes[prefix+"arc"], cx, cy, radius, right=sign < 0)
        check_normal(nodes[prefix+"normal-vector"], cx, cy, radius, outward=sign < 0)
        close((cy-surface)/radius, h1/R)
        force = quarter_cylinder(R, b, h1, sign)
        fh, fv = nodes[prefix+"FH"], nodes[prefix+"FV"]
        yh = float(fh.get("y1")); xv = float(fv.get("x1"))
        close(float(fh.get("y2")), yh)
        close(float(fv.get("x2")), xv)
        close((yh-surface)*R/radius, force["h_H"])
        close(abs(xv-cx)*R/radius, force["x_from_wall"])
        assert float(fh.get("x2")) > float(fh.get("x1"))
        assert (float(fv.get("y2")) < float(fv.get("y1"))) == (sign > 0)
        # Force lines must produce zero total moment about the circle center.
        close((xv-cx)*(-force["F_V"])-(yh-cy)*force["F_H"], 0, 1e-5)
        water = nodes[prefix+"water-domain"].get("d")
        assert " Z" in water and f"A{radius} {radius}" in water
        if sign > 0:
            auxiliary = nodes[prefix+"aux-volume"]
            assert auxiliary.get("fill") == "none"
            assert auxiliary.get("d").startswith(nodes[prefix+"arc"].get("d"))
        print(f"PASS {name}: circular arc, normal, pressure arms and moment")

    _, nodes = read("u05_vjezbe_skice.svg")
    check_arc(nodes["u05vs_z2_arc"], 210, 125, 44)
    check_arc(nodes["u05vs_z5_arc"], 207, 103, 70)
    check_normal(nodes["u05vs_z5_normal"], 207, 103, 70)
    assert nodes["u05vs_z4_triangle"].get("d") == "M144.0 78 L218 190 H70 Z"
    for n in range(1, 7):
        assert f"u05vs_z{n}" in nodes
    print("PASS practice panels: Z2/Z5 arcs, Z5 normal, triangular orientation, six panels")


if __name__ == "__main__":
    main()
