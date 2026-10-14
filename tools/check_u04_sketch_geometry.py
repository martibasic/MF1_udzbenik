"""Provjera geometrije izmijenjenih SVG skica U04 (revizija 12. 10. 2026.).

Pokrenuti zasebno: python tools/check_u04_sketch_geometry.py.
Čita stvarne koordinate: brod u kružnom zavoju (P3) i kosa stijenka bez
sile i hvatišta (P2). Dopunjuje numerički verifier i vizualni pregled.
"""

from pathlib import Path
import math
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
    # Kote odgovaraju nacrtanim razinama.
    assert abs(f(n["u04frc_dim-bt"], "x2") - f(n["u04frc_dim-bt"], "x1") - B * scale) < 1e-9
    assert abs(f(n["u04frc_dim-hv"], "y1") - yr) < 1e-9 and abs(f(n["u04frc_dim-hu"], "y1") - yl) < 1e-9
    assert abs(f(n["u04frc_dim-h"], "y2") - f(n["u04frc_dim-h"], "y1") - H * scale) < 1e-9
    labels = " | ".join(texts(root))
    for needed in ("180 m", "12 čv", "9,0 m", "2,20 m", "1025"):
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
    assert any("M,B" in t for t in labels) and any("φ" in t for t in labels) and not any("α" in t for t in labels)
    assert any("M,pl" in t for t in labels)
    print("PASS u04 inclined wall: pressure arrows normal to AB and increasing, no resultant force elements")


def main():
    check_ship_turn()
    check_inclined_wall()


if __name__ == "__main__":
    main()
