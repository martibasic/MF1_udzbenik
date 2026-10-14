"""Provjera geometrije izmijenjenih SVG skica U04 (revizija 12. 10. 2026.).

Pokrenuti zasebno: python tools/check_u04_sketch_geometry.py.
Čita stvarne koordinate: brod u kružnom zavoju (P3) i kosa stijenka bez
sile i hvatišta (P2). Dopunjuje numerički verifier i vizualni pregled.
"""

from pathlib import Path
import math
import re
import xml.etree.ElementTree as ET
from sketch_style import check_scene_canvas, check_uniform_fluid

ASSETS = Path(__file__).resolve().parent.parent / "assets/print"


def read(name):
    root = ET.parse(ASSETS / name).getroot()
    ids = [n.get("id") for n in root.iter() if n.get("id")]
    assert len(ids) == len(set(ids)), name
    return root, {n.get("id"): n for n in root.iter() if n.get("id")}


def f(node, attr):
    return float(node.get(attr))


def points(node):
    return [tuple(map(float, pair.split(","))) for pair in node.get("points").split()]


def texts(root):
    return [" ".join("".join(t.itertext()).split()) for t in root.iter() if t.tag.endswith("text")]


def check_ship_turn():
    name = "u04_fig_rotirajuci_cilindar.svg"
    root, n = read(name)
    check_scene_canvas(name, root, 1)
    scale = 40.0
    v, R, B, h0, H, g = 6.17, 180.0, 9.0, 1.60, 2.20, 9.81
    a = v * v / R
    water = n["u04frc_water"]
    check_uniform_fluid(water)
    (xl, yl), (xr, yr), (xr2, yb), (xl2, yb2) = points(water)
    assert xl == xl2 and xr == xr2 and yb == yb2
    assert abs((xr - xl) - B * scale) < 1e-9
    # Vanjska (desna) strana zavoja viša je; nagib odgovara a/g bez uvećanja.
    assert yr < yl
    slope = (yl - yr) / (xr - xl)
    assert abs(slope - a / g) / (a / g) < 2e-3, slope
    hu, hv = (yb - yl) / scale, (yb - yr) / scale
    assert abs((hu + hv) / 2 - h0) < 1e-9, "srednja razina mora ostati h_0"
    assert abs(hv - hu - a * B / g) < 1e-3
    top = n["u04frc_tank-top-1"]
    assert abs((yb - (f(top, "y") + f(top, "height"))) - H * scale) < 1e-9
    assert yr > f(top, "y") + f(top, "height"), "bez prelijevanja"
    surf = n["u04frc_free-surface"]
    assert (f(surf, "x1"), f(surf, "y1"), f(surf, "x2"), f(surf, "y2")) == (xl, yl, xr, yr)
    rest = n["u04frc_rest-level"]
    assert abs(f(rest, "y1") - (yb - h0 * scale)) < 1e-9 and f(rest, "y1") == f(rest, "y2")
    # Sondne cijevi: unutar tanka, otvorene iznad dna, razina u cijevi jednaka lokalnoj površini.
    for side, x_expected in (("left", None), ("right", None)):
        w1, w2, fl = n[f"u04frc_sonda-{side}-w1"], n[f"u04frc_sonda-{side}-w2"], n[f"u04frc_sonda-{side}-fluid"]
        for w in (w1, w2):
            assert f(w, "y") + f(w, "height") < yb - 5
            assert xl < f(w, "x") < xr
        xc = (f(w1, "x") + f(w1, "width") + f(w2, "x")) / 2
        y_local = yl + (yr - yl) * (xc - xl) / (xr - xl)
        assert abs(f(fl, "y") - y_local) < 0.6, side
        assert abs(f(fl, "y") + f(fl, "height") - (f(w1, "y") + f(w1, "height"))) < 1e-9
    # Strelica prema središtu zavoja pokazuje ulijevo, prividna sila udesno.
    turn, app = n["u04frc_turn-arrow"], n["u04frc_apparent-arrow"]
    assert f(turn, "x2") < f(turn, "x1") and f(app, "x2") > f(app, "x1")
    # Ubrzanje i prividna sila razlikuju se vrstom vektora (standard 14. 10. 2026.).
    assert turn.get("data-mf1-vector") == "acceleration" and app.get("data-mf1-vector") == "force"
    # Kote odgovaraju nacrtanim razinama.
    assert abs(f(n["u04frc_dim-bt"], "x2") - f(n["u04frc_dim-bt"], "x1") - B * scale) < 1e-9
    assert abs(f(n["u04frc_dim-hv"], "y1") - yr) < 1e-9 and abs(f(n["u04frc_dim-hu"], "y1") - yl) < 1e-9
    assert abs(f(n["u04frc_dim-h"], "y2") - f(n["u04frc_dim-h"], "y1") - H * scale) < 1e-9
    labels = " | ".join(texts(root))
    for needed in ("Rz = 180 m", "12 čv", "bt = 9,0 m", "2,20 m", "ρmv = 1025"):
        assert needed in labels, needed
    assert "1,70" not in labels and "1,50" not in labels, "rezultati ne idu u skicu"
    print("PASS u04 ship in turn: true a/g slope, volume conserved, open sounding pipes, outer side higher")


def check_inclined_wall():
    name = "u04_val3_kosa_stijenka.svg"
    root, n = read(name)
    check_scene_canvas(name, root, 1)
    wall, surf = n["u04v3ks_wall-ab"], n["u04v3ks_free-surface"]
    wx, wy = f(wall, "x2") - f(wall, "x1"), f(wall, "y2") - f(wall, "y1")
    sx, sy = f(surf, "x2") - f(surf, "x1"), f(surf, "y2") - f(surf, "y1")
    assert abs(wx * sx + wy * sy) / (math.hypot(wx, wy) * math.hypot(sx, sy)) < 1e-6, "AB okomita na površinu"
    # Inklinacija pravca AB prema vodoravnici mora biti phi = 90 - theta (A je gore desno, B dolje lijevo).
    assert wx < 0 < wy
    assert abs(math.degrees(math.atan2(abs(wy), abs(wx))) - (90 - math.degrees(math.atan(3.4 / 9.81)))) < 0.05
    lengths = []
    for i in range(1, 6):
        p = n[f"u04v3ks_p{i}"]
        px, py = f(p, "x2") - f(p, "x1"), f(p, "y2") - f(p, "y1")
        assert abs(px * wx + py * wy) / (math.hypot(px, py) * math.hypot(wx, wy)) < 1e-3, "tlak okomit na AB"
        lengths.append(math.hypot(px, py))
    assert all(b > a for a, b in zip(lengths, lengths[1:])), "tlak raste od A prema B"
    labels = texts(root)
    assert not any(t.startswith("F") or t.startswith("y") for t in labels), "bez sile i hvatišta"
    # Kut stijenke je θ_AB (φ je prema standardu samo poprečni nagib), visinska razlika Δz_AB.
    assert any("M,B" in t for t in labels) and any(t == "θAB" for t in labels)
    assert not any("φ" in t or "α" in t for t in labels)
    assert any(t.startswith("ΔzAB") for t in labels) and not any(t.startswith("H =") for t in labels)
    for i in range(1, 6):
        assert n[f"u04v3ks_p{i}"].get("data-mf1-vector") == "pressure"
    assert any("M,pl" in t for t in labels)
    print("PASS u04 inclined wall: pressure arrows normal to AB and increasing, no resultant force elements")


def check_exercises():
    """Skice zadataka ne smiju otkrivati rezultat (načelo odobreno 14. 10. 2026.).

    Zadane visine (H, h_0) ostaju u mjerilu; nagnute površine Z1/Z5 i radni
    paraboloid Z6 moraju biti shematski, tj. dovoljno daleko od rezultata.
    """
    root, n = read("u04_vjezbe_skice.svg")
    g = 9.81

    def tilted(prefix, scale, bottom, h0, L, a):
        s = n[f"{prefix}_surface"]
        rear, front = (bottom - f(s, "y1")) / scale, (bottom - f(s, "y2")) / scale
        dh = a * L / g
        assert rear > front, "viša razina straga (ubrzanje udesno)"
        assert abs((rear + front) / 2 - h0) < 1e-3, "očuvan volumen u shemi"
        assert abs(rear - (h0 + dh / 2)) > 0.03 and abs(front - (h0 - dh / 2)) > 0.03, (prefix, rear, front)
        d = n[f"{prefix}_fluid"].get("d").replace(",", " ").split()
        assert float(d[1]) == f(s, "y1") and float(d[3]) == f(s, "y2"), "ispuna prati površinu"
        return rear

    rear1 = tilted("u04vs_z1", 200.0, 174.0, 0.34, 1.80, 1.20)
    assert rear1 < 0.46
    tilted("u04vs_z5", 145.0, 178.0, 0.300, 1.50, 2.00)
    # Graf Z5 ne smije sadržavati referentnu crtu modela h_str = 0,4529 m (400 px/m, 0,38 m na y = 148).
    y_ref = 148.0 - (0.300 + 2.00 * 1.50 / (2 * g) - 0.38) * 400.0
    for line in n["u04vs_z5"].iter():
        if line.tag.endswith("line") and line.get("y1") == line.get("y2"):
            assert abs(f(line, "y1") - y_ref) > 2.0, "referentni model ucrtan u graf"
    # Z6: radni paraboloid ω = 0,80 ω_max nije u mjerilu rezultata h_C = 0,3576 m.
    R, H, h0, scale, bottom = 0.32, 0.62, 0.46, 170.0, 180.0
    w_max = math.sqrt(4 * g * (H - h0)) / R
    h_c = h0 - (0.80 * w_max) ** 2 * R ** 2 / (4 * g)
    m = re.fullmatch(r"M60 ([\d.]+) Q148 ([\d.]+) 236 ([\d.]+)", n["u04vs_z6_working"].get("d"))
    rim, ctrl, rim2 = map(float, m.groups())
    vertex = (rim + ctrl) / 2
    drawn_c, drawn_r = (bottom - vertex) / scale, (bottom - rim) / scale
    assert rim == rim2 and abs(drawn_c - h_c) > 0.03, (drawn_c, h_c)
    assert drawn_r < H and drawn_c > 0
    assert abs(f(n["u04vs_z6_dim-hc"], "y1") - vertex) < 1e-6
    print("PASS u04 exercises: Z1/Z5 slopes and Z6 paraboloid schematic, no model line in Z5 graph")


def main():
    check_ship_turn()
    check_inclined_wall()
    check_exercises()


if __name__ == "__main__":
    main()
