"""Provjera geometrije izmijenjenih SVG skica U03 (revizija 12. 10. 2026.).

Pokrenuti zasebno: python tools/check_u03_sketch_geometry.py.
Čita stvarne koordinate iz SVG-ova: teretni tank sa sondiranjem (P3),
bočni balastni tank sa sondnom cijevi (P5) i oznake prijelazne skice.
Dopunjuje numerički verifier i vizualni pregled.
"""

from pathlib import Path
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


def texts(root):
    return [" ".join("".join(t.itertext()).split()) for t in root.iter() if t.tag.endswith("text")]


def check_cargo_tank():
    name = "u03_ch1_zatvoreni_spremnik_ulje_ziva.svg"
    root, n = read(name)
    check_scene_canvas(name, root, 1)
    scale = 20.0  # jedinica po metru
    gas, oil, water = n["u03c1zsuz_gas"], n["u03c1zsuz_oil"], n["u03c1zsuz_water"]
    for layer in (gas, oil, water):
        check_uniform_fluid(layer)
    # Slojevi se dodiruju bez praznina i bez preklapanja: plin iznad ulja iznad vode.
    assert abs(f(gas, "y") + f(gas, "height") - f(oil, "y")) < 1e-9
    assert abs(f(oil, "y") + f(oil, "height") - f(water, "y")) < 1e-9
    bottom = n["u03c1zsuz_bottom"]
    assert abs(f(water, "y") + f(water, "height") - f(bottom, "y")) < 1e-9
    assert f(gas, "x") == f(oil, "x") == f(water, "x") and f(gas, "width") == f(oil, "width") == f(water, "width")
    # Kote u zajedničkom mjerilu prema podatcima zadatka.
    ref_y = f(n["u03c1zsuz_ref-mark"], "y1")
    assert abs((f(bottom, "y") - ref_y) - 18.60 * scale) < 0.05
    assert abs(f(water, "height") - 0.35 * scale) < 0.05
    assert abs((f(oil, "y") - ref_y) - 2.31 * scale) < 0.05
    assert abs(f(oil, "height") - 15.94 * scale) < 0.1
    for dim, (y1, y2) in (("u03c1zsuz_dim-href", (ref_y, f(bottom, "y"))),
                          ("u03c1zsuz_dim-u", (ref_y, f(oil, "y"))),
                          ("u03c1zsuz_dim-ho", (f(oil, "y"), f(water, "y")))):
        d = n[dim]
        assert abs(f(d, "y1") - y1) < 1e-9 and abs(f(d, "y2") - y2) < 1e-9, dim
    # Slobodna površina ulja i razdjelnica crtaju se na stvarnim razinama.
    assert abs(f(n["u03c1zsuz_oil-surface"], "y1") - f(oil, "y")) < 1e-9
    assert abs(f(n["u03c1zsuz_interface"], "y1") - f(water, "y")) < 1e-9
    # Ullage otvor je stvarno otvoren: palubne ploče ostavljaju prolaz između cijevi.
    left, right = n["u03c1zsuz_deck-left"], n["u03c1zsuz_deck-right"]
    gap_l, gap_r = f(left, "x") + f(left, "width"), f(right, "x")
    assert gap_l < gap_r
    sl, sr = n["u03c1zsuz_standpipe-left"], n["u03c1zsuz_standpipe-right"]
    assert f(sl, "x") >= gap_l - 1e-9 and f(sr, "x") + f(sr, "width") <= gap_r + 1e-9
    assert f(sr, "x") - (f(sl, "x") + f(sl, "width")) > 10
    # Vrpce prolaze kroz otvor; sonda doseže dno, ullage vrpca samo površinu ulja.
    ul, so = n["u03c1zsuz_ullage-tape"], n["u03c1zsuz_sounding-tape"]
    for tape in (ul, so):
        assert gap_l < f(tape, "x1") < gap_r
    assert abs(f(ul, "y2") - f(oil, "y")) < 1e-9 and abs(f(so, "y2") - f(bottom, "y")) < 1e-9
    # Tlačni mjerač je na dnu unutar tanka, manometar plina iznad palube u plinu.
    g = n["u03c1zsuz_bottom-gauge"]
    assert f(oil, "x") < f(g, "cx") < f(oil, "x") + f(oil, "width")
    assert f(water, "y") <= f(g, "cy") <= f(bottom, "y") + f(bottom, "height")
    gg = n["u03c1zsuz_gas-gauge"]
    assert f(gg, "cy") < f(gas, "y")
    labels = " | ".join(texts(root))
    for needed in ("860", "ρmv = 1025", "3,0 kPa", "18,60", "2,31", "0,35", "M,dno"):
        assert needed in labels, needed
    assert "kPa</" not in labels and "15,94" not in labels, "rezultati ne idu u skicu"
    print("PASS u03 cargo tank: layered fluids, 20 px/m dimensions, open ullage hatch, bottom gauge")


def check_ballast_tank():
    name = "u03_fig_balastni_tank.svg"
    root, n = read(name)
    check_scene_canvas(name, root, 1)
    scale = 36.0
    ballast, sea = n["u03fbt_ballast"], n["u03fbt_sea"]
    check_uniform_fluid(ballast)
    check_uniform_fluid(sea)
    assert ballast.get("fill") == sea.get("fill"), "ista morska voda iznutra i izvana"
    bottom = n["u03fbt_tank-bottom"]
    tg, ht, hp = n["u03fbt_dim-tg"], n["u03fbt_dim-ht"], n["u03fbt_dim-hp"]
    assert abs((f(tg, "y2") - f(tg, "y1")) - 8.5 * scale) < 1e-9
    assert abs((f(ht, "y2") - f(ht, "y1")) - 5.0 * scale) < 1e-9
    assert abs((f(hp, "y2") - f(hp, "y1")) - 2.0 * scale) < 1e-9
    assert abs(f(tg, "y2") - f(bottom, "y")) < 1e-9 and abs(f(ht, "y2") - f(bottom, "y")) < 1e-9
    assert abs(f(ballast, "y") - f(ht, "y1")) < 1e-9 and abs(f(ballast, "y") + f(ballast, "height") - f(bottom, "y")) < 1e-9
    # Ploča P leži u oplati boka na koti h_p i unutar oba susjedna segmenta oplate.
    plate = n["u03fbt_plate-p"]
    assert f(plate, "y") < f(hp, "y1") < f(plate, "y") + f(plate, "height")
    assert abs(f(n["u03fbt_shell-upper"], "y") + f(n["u03fbt_shell-upper"], "height") - f(plate, "y")) < 1e-9
    assert abs(f(n["u03fbt_shell-lower"], "y") - (f(plate, "y") + f(plate, "height"))) < 1e-9
    # Sondna cijev: otvorena iznad dna, proteže se iznad palube, unutar tanka.
    w1, w2 = n["u03fbt_sonda-w1"], n["u03fbt_sonda-w2"]
    for w in (w1, w2):
        assert f(w, "y") + f(w, "height") < f(bottom, "y") - 5, "sondna cijev ne smije dodirivati dno"
        assert f(w, "y") < 40
        assert f(ballast, "x") < f(w, "x") < f(ballast, "x") + f(ballast, "width")
    assert f(w2, "x") - (f(w1, "x") + f(w1, "width")) >= 8
    air = n["u03fbt_sonda-air"]
    assert abs(f(air, "y") + f(air, "height") - f(ballast, "y")) < 1e-9, "razina u sondi jednaka razini u tanku"
    labels = " | ".join(texts(root))
    assert labels.count("1025") == 2 and "1000" not in labels
    # Gustoća mora ρ_mv (indeks m samo model), kota ploče z_P (h_p je piezometarska visina).
    assert "ρmv = 1025" in labels and "ρm = " not in labels
    assert "zP" in labels.split(" | ") and "hp" not in labels.split(" | ")
    assert "ploča P" in labels and "sondna cijev" in labels and "prozor" not in labels
    print("PASS u03 ballast tank: equal seawater densities, 36 px/m dimensions, plate P in shell, open sounding pipe")


def check_bridge_labels():
    root, _ = read("u03_balans_tlaka_i_geff.svg")
    labels = texts(root)
    assert sum("p pov" in t or "ppov" in t or t == "p pov" for t in labels) + sum(t.endswith("pov") for t in labels) >= 3
    assert not any("p₀" in t for t in labels)
    print("PASS u03 bridge sketch: free-surface pressure labelled p_pov")


def check_exercises():
    """Skice zadataka ne smiju otkrivati rezultat (načelo odobreno 14. 10. 2026.)."""
    root, n = read("u03_vjezbe_skice.svg")
    oil, water, iface = n["u03vs_z4_oil"], n["u03vs_z4_water"], n["u03vs_z4_interface"]
    top, bottom = f(oil, "y"), f(water, "y") + f(water, "height")
    # Slojevi se dodiruju na nacrtanoj granici.
    assert abs(f(oil, "y") + f(oil, "height") - f(iface, "y1")) < 1e-9 and abs(f(water, "y") - f(iface, "y1")) < 1e-9
    assert abs(f(n["u03vs_z4_dim-ho"], "y2") - f(iface, "y1")) < 1e-9 and abs(f(n["u03vs_z4_dim-hw"], "y1") - f(iface, "y1")) < 1e-9
    # Granica NIJE u omjeru rezultata h_o/H (Z4: H = 1,50 m, p_M,A = 13,83 kPa).
    g, H, rho_o, rho_w, p = 9.81, 1.50, 850.0, 1000.0, 13.83e3
    h_o = (rho_w * g * H - p) / ((rho_w - rho_o) * g)
    ratio = (f(iface, "y1") - top) / (bottom - top)
    assert 0 < ratio < 1 and abs(ratio - h_o / H) > 0.05, (ratio, h_o / H)
    # Točke koje tekst ne imenuje nisu označene (Z1, Z3; u Z6 samo A iz napomene).
    for group, banned in (("u03vs_z1", {"A", "a"}), ("u03vs_z3", {"A", "a"}), ("u03vs_z6", {"C"})):
        labels = {" ".join("".join(t.itertext()).split()) for t in n[group].iter() if t.tag.endswith("text")}
        assert not labels & banned, (group, labels & banned)
    print("PASS u03 exercises: Z4 interface not at result ratio, unnamed points unlabelled")


def main():
    check_cargo_tank()
    check_ballast_tank()
    check_bridge_labels()
    check_exercises()


if __name__ == "__main__":
    main()
