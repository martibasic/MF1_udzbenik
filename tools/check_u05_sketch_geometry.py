"""Provjera stvarnih SVG lukova, normala i pravaca sila u U05.

Pokrenuti iz korijena: python tools/check_u05_sketch_geometry.py.
Ovo dopunjuje numerički verifier; ne zamjenjuje vizualni pregled i provjeru
čitljivosti. Koordinate su SVG koordinate (y raste prema dolje).
"""

from pathlib import Path
import math
import re
import xml.etree.ElementTree as ET

from verify_u05_integrated import (quarter_cylinder, task_watertight_door,
                                   task_parabolic_cover)


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
    # Z1: pogled okomito na vrata; omjeri H/b i h1/H te oznaka sile u centru tlaka.
    door = nodes["u05vs_z1_door"]
    x, y, w, h = [float(door.get(k)) for k in ("x", "y", "width", "height")]
    z1 = task_watertight_door()
    surface = float(nodes["u05vs_z1_surface"].get("y1"))
    assert nodes["u05vs_z1_surface"].get("y1") == nodes["u05vs_z1_surface"].get("y2")
    close(h / w, 1.60 / 0.80)
    close((y - surface) / h, 1.40 / 1.60)
    mark = nodes["u05vs_z1_force_mark"]
    close(float(mark.get("cx")), x + w / 2)
    close((float(mark.get("cy")) - surface) / h * 1.60, z1["h_cp"], 2e-3)
    for dog, edge in (("u05vs_z1_dog_top", y), ("u05vs_z1_dog_bottom", y + h)):
        close(float(nodes[dog].get("cy")), edge)
        assert float(nodes[dog].get("cx")) > x + w
    for hinge in ("u05vs_z1_hinge_top", "u05vs_z1_hinge_bottom"):
        assert float(nodes[hinge].get("x")) + float(nodes[hinge].get("width")) <= x
    # Z2: kvadratna Bezierova krivulja s kontrolnom točkom na sjecištu tangenata
    # jest točna parabola s tjemenom A i vodoravnom tangentom u A.
    tokens = re.findall(r"[A-Za-z]|-?\d+(?:\.\d+)?", nodes["u05vs_z2_parabola"].get("d"))
    assert tokens[0] == "M" and tokens[3] == "Q" and len(tokens) == 8, tokens
    ax, ay, cx_, cy_, bx, by = map(float, tokens[1:3] + tokens[4:])
    close(cx_, (ax + bx) / 2)
    close(cy_, ay)
    close((by - ay) / (bx - ax), 0.90 / 1.20)
    scale = (bx - ax) / 1.20
    z2 = task_parabolic_cover()
    fh, fv = nodes["u05vs_z2_FH"], nodes["u05vs_z2_FV"]
    assert fh.get("y1") == fh.get("y2") and fv.get("x1") == fv.get("x2")
    close((float(fh.get("y1")) - ay) / scale, z2["depth_x"])
    close((float(fv.get("x1")) - ax) / scale, z2["x_z"])
    assert float(fh.get("x2")) < float(fh.get("x1"))      # prema stijenci
    assert float(fv.get("y2")) > float(fv.get("y1"))      # prema dolje
    # Voda je iznad pokrova: pravci F_H i F_V ne daju nulti moment oko A (nije kružni luk).
    assert abs(abs(z2["F_x"]) * z2["depth_x"] - abs(z2["F_z"]) * z2["x_z"]) > 500
    nx1, ny1, nx2, ny2 = [float(nodes["u05vs_z2_normal"].get(k)) for k in ("x1", "y1", "x2", "y2")]
    xs = (nx2 - ax) / scale
    close((ny2 - ay) / scale, 0.90 * (xs / 1.20) ** 2, 1e-3)          # vrh strelice na paraboli
    slope = 2 * 0.90 * xs / 1.20**2                                     # dy/dx u SVG smjeru
    close((nx2 - nx1) * 1 + (ny2 - ny1) * slope, 0, 0.15)             # okomito na tangentu
    assert nx2 < nx1 and ny2 > ny1                                      # iz vode u pokrov
    water = nodes["u05vs_z2_water-domain"].get("d")
    assert water.startswith("M48 50") and " Z" in water and f"Q{cx_:g} {cy_:g} {ax:g} {ay:g}" in water
    check_arc(nodes["u05vs_z5_arc"], 207, 103, 70)
    check_normal(nodes["u05vs_z5_normal"], 207, 103, 70)
    assert nodes["u05vs_z4_triangle"].get("d") == "M144.0 78 L218 190 H70 Z"
    for n in range(1, 7):
        assert f"u05vs_z{n}" in nodes
    print("PASS practice panels: Z1 door view, Z2 parabola and forces, Z5 arc and normal, triangular orientation, six panels")


if __name__ == "__main__":
    main()
