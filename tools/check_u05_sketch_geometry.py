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
                                   task_parabolic_cover, task_triangle,
                                   task_radial_gate, task_flap_gate)


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


def unknown_not_drawn(nodes, panel, label_id, allowed_vectors=()):
    """Skica zadatka ne smije nacrtati traženu silu: u panelu nema vektora
    sile osim zadanih, a nepoznanica je označena upitnikom."""
    for node in nodes[panel].iter():
        kind = node.get("data-mf1-vector")
        if kind == "force":
            assert node.get("id") in allowed_vectors, (panel, node.get("id"))
    text = "".join(nodes[label_id].itertext())
    assert "?" in text, (label_id, text)


def main():
    cases = [
        ("u06_val1_cetvrtina_kruga.svg", "u05p4_", 370, 245, 100, 45, 1.22, 1.83, 2.44, 1, 0.0),
        # P5: zatvoreni spremnik s nadtlakom plina 20 kPa; hvatišta pomaknuta prema težištima.
        ("u06_val3_cetvrtcilindricni_poklopac.svg", "u05p5_", 135, 105, 175, 105, .90, 1.20, 0, -1, 20e3),
        ("u06_ch1_poklopac_spojnica.svg", "u05p6_", 355, 150, 145, 150, 1.10, 1.40, 0, 1, 0.0),
    ]
    for name, prefix, cx, cy, radius, surface, R, b, h1, sign, p_gas in cases:
        _, nodes = read(name)
        check_arc(nodes[prefix+"arc"], cx, cy, radius, right=sign < 0)
        check_normal(nodes[prefix+"normal-vector"], cx, cy, radius, outward=sign < 0)
        close((cy-surface)/radius, h1/R)
        force = quarter_cylinder(R, b, h1, sign, p_gas=p_gas)
        if p_gas:
            # Zatvoreni spremnik: poklopac iznad plina i stijenka do poklopca.
            lid = nodes[prefix+"lid"]
            assert float(lid.get("y")) + float(lid.get("height")) < surface
            assert float(lid.get("x")) <= cx and float(lid.get("x")) + float(lid.get("width")) >= cx + radius
            assert any("nadtlak" in "".join(n.itertext()) for n in nodes[prefix+"geometry"].iter() if n.tag.endswith("text"))
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
    # Tražena sila i njezino hvatište (centar tlaka) ne smiju biti nacrtani.
    assert "u05vs_z1_force_mark" not in nodes
    for node in nodes["u05vs_z1"].iter():
        if node.tag.endswith("circle") and node.get("stroke") == "#356b83":
            cy = float(node.get("cy"))
            assert abs((cy - surface) / h * 1.60 - z1["h_cp"]) > 0.05, "CP mark"
    unknown_not_drawn(nodes, "u05vs_z1", "u05vs_z1_unknown")
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
    # Skica zadatka ne otkriva rezultat: nema strelica F_H/F_V u hvatištima
    # ni s predznakom; nacrtana je samo lokalna tlačna sila dF (postavljanje modela).
    assert "u05vs_z2_FH" not in nodes and "u05vs_z2_FV" not in nodes
    vectors = [n for n in nodes["u05vs_z2"].iter() if n.get("data-mf1-vector")]
    assert [n.get("id") for n in vectors] == ["u05vs_z2_normal"], vectors
    assert vectors[0].get("data-mf1-vector") == "pressure"
    unknown_not_drawn(nodes, "u05vs_z2", "u05vs_z2_unknown")
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
    # Z3: kosa zaklopka pod 60°, os na a/L = 0,40 duljine ploče od donjeg ruba na pragu,
    # voda samo uzvodno; tražena dubina otvaranja nije nacrtana u mjerilu.
    gate = nodes["u05vs_z3_gate"]
    gx1, gy1, gx2, gy2 = [float(gate.get(k)) for k in ("x1", "y1", "x2", "y2")]
    close(math.degrees(math.atan2(gy1 - gy2, gx2 - gx1)), 60.0, 1e-6)
    close(gy1, 190.0)                                   # donji rub na dnu kanala
    scale = math.hypot(gx2 - gx1, gy2 - gy1) / 2.00      # px po metru uzduž ploče
    axis = nodes["u05vs_z3_axis"]
    ax_, ay_ = float(axis.get("cx")), float(axis.get("cy"))
    close(math.hypot(ax_ - gx1, ay_ - gy1) / scale, 0.80, 1e-6)
    close((ax_ - gx1) * (gy2 - gy1) - (ay_ - gy1) * (gx2 - gx1), 0, 0.05)   # os na ploči
    sill = nodes["u05vs_z3_sill"]
    assert float(sill.get("x")) > gx1 and float(sill.get("y")) + float(sill.get("height")) == 190.0
    z3 = task_flap_gate()
    y_drawn = (gy1 - float(nodes["u05vs_z3_surface"].get("y1"))) / scale
    assert abs(y_drawn - z3["y_open"]) > 0.3 and abs(y_drawn - 1.80) > 0.1, y_drawn
    unknown_not_drawn(nodes, "u05vs_z3", "u05vs_z3_unknown")
    vectors = [n for n in nodes["u05vs_z3"].iter() if n.get("data-mf1-vector")]
    assert vectors and all(n.get("data-mf1-vector") == "pressure" for n in vectors)
    for n in vectors:   # tlačne strelice iz vode (lijevo-gore) na ploču, okomito na nju
        x1, y1, x2, y2 = [float(n.get(k)) for k in ("x1", "y1", "x2", "y2")]
        close((x2 - x1) * (gx2 - gx1) + (y2 - y1) * (gy2 - gy1), 0, 0.05)
        assert x2 > x1 and y2 > y1
    water = nodes["u05vs_z3_water-domain"].get("d")
    assert water.startswith("M48 ") and " Z" in water and f"L{gx1:g} {gy1:g}" in water
    check_arc(nodes["u05vs_z5_arc"], 207, 103, 70)
    check_normal(nodes["u05vs_z5_normal"], 207, 103, 70)
    assert nodes["u05vs_z4_triangle"].get("d") == "M144.0 78 L218 190 H70 Z"
    # Z4: nacrtana širina (nepoznanica) nije u mjerilu b_max ni ponuđenih 1,20 m.
    b_drawn = (218 - 70) / (190 - 78) * 1.50
    for b_ref in (task_triangle()["b_max"], 1.20):
        assert abs(b_drawn - b_ref) > 0.10, (b_drawn, b_ref)
    # Z5: duljina strelice T (iznos se traži) nije u mjerilu težine F_G.
    fg, t = nodes["u05vs_z5_FG"], nodes["u05vs_z5_T"]
    l_fg = abs(float(fg.get("y2")) - float(fg.get("y1")))
    l_t = abs(float(t.get("x2")) - float(t.get("x1")))
    z5 = task_radial_gate()
    assert abs(l_t / l_fg - z5["T"] / 2.40e3) > 0.2, (l_t, l_fg)
    # Z6: tražena sila F nije nacrtana (ni u centru tlaka).
    unknown_not_drawn(nodes, "u05vs_z6", "u05vs_z6_unknown")
    assert not any(n.get("marker-end") for n in nodes["u05vs_z6"].iter()
                   if n.get("data-mf1-role") != "dimension")
    for n in range(1, 7):
        assert f"u05vs_z{n}" in nodes
    print("PASS practice panels: Z1 door view, Z2 parabola and local normal, Z3 flap gate angle/axis/sill, Z1/Z2/Z3/Z6 unknown forces not drawn, Z5 arc and normal, triangular orientation, six panels")


if __name__ == "__main__":
    main()
