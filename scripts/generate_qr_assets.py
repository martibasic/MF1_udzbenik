"""Deterministički generiraj pristupačne QR SVG-ove za sve JupyterLite pokuse.

Bez ``--write`` skripta je CI provjera zastarjelih ili nedostajucih izlaza.
"""

from __future__ import annotations

import argparse
from pathlib import Path

import qrcode
from qrcode.constants import ERROR_CORRECT_M


ROOT = Path(__file__).resolve().parents[1]
QR_DIR = ROOT / "assets" / "qr"
SITE_ROOT = "https://martibasic.github.io/MF1_udzbenik/jlite/lab/index.html?path="

ASSETS = {
    "u01_hidraulicna_presa.svg": (
        "u01_hidraulicna_presa.ipynb",
        "QR kod za numerički pokus hidraulične preše u JupyterLiteu",
    ),
    "u02_kapilarni_uspon.svg": (
        "u02_kapilarni_uspon.ipynb",
        "QR kod za numerički pokus kapilarnog uspona u JupyterLiteu",
    ),
    "u03_diferencijalni_manometar.svg": (
        "u03_diferencijalni_manometar.ipynb",
        "QR kod za numerički pokus diferencijalnog manometra u JupyterLiteu",
    ),
    "u04_paraboloidna_povrsina.svg": (
        "u04_paraboloidna_povrsina.ipynb",
        "QR kod za numerički pokus rotirajuće slobodne površine u JupyterLiteu",
    ),
    "u05_sila_na_ravnu_plohu.svg": (
        "u05_sila_na_ravnu_plohu.ipynb",
        "QR kod za numerički pokus sile na ravnu plohu u JupyterLiteu",
    ),
    "u06_zakrivljena_ploha.svg": (
        "u06_zakrivljena_ploha.ipynb",
        "QR kod za numerički pokus sile na zakrivljenu plohu u JupyterLiteu",
    ),
    "u07_gaz_plivajuceg_tijela.svg": (
        "u07_gaz_plivajuceg_tijela.ipynb",
        "QR kod za numerički pokus gaza plivajućeg tijela u JupyterLiteu",
    ),
    "u08_kontinuitet_suzenje.svg": (
        "u08_kontinuitet_suzenje.ipynb",
        "QR kod za numerički pokus kontinuiteta i spremnika u JupyterLiteu",
    ),
    "u09_kompresibilna_sapnica_jlite.svg": (
        "u09_kompresibilna_sapnica.ipynb",
        "QR kod za numericki pokus kompresibilne sapnice u JupyterLiteu",
    ),
    "u09_venturi.svg": (
        "u09_venturi.ipynb",
        "QR kod za numerički pokus Venturijeve cijevi u JupyterLiteu",
    ),
    "u10_moody_dijagram.svg": (
        "u10_moody_dijagram.ipynb",
        "QR kod za Colebrookov i Moodyjev numerički pokus u JupyterLiteu",
    ),
    "u11_sila_na_koljeno.svg": (
        "u11_sila_na_koljeno.ipynb",
        "QR kod za numerički pokus sile na koljeno u JupyterLiteu",
    ),
    "u12_pelton_lopatica.svg": (
        "u12_pelton_lopatica.ipynb",
        "QR kod za numerički pokus Peltonove lopatice u JupyterLiteu",
    ),
    "u12_poiseuille_konvergencija_jlite.svg": (
        "u12_poiseuille_konvergencija.ipynb",
        "QR kod za Poiseuilleov pokus konvergencije u JupyterLiteu",
    ),
    "u13_paralelne_grane.svg": (
        "u13_paralelne_grane.ipynb",
        "QR kod za numerički pokus nelinearne cjevovodne mreže u JupyterLiteu",
    ),
    "u14_cd_re_kugla.svg": (
        "u14_cd_re_kugla.ipynb",
        "QR kod za numerički pokus koeficijenta otpora kugle u JupyterLiteu",
    ),
    "u15_otvoreni_tokovi_jlite.svg": (
        "u15_otvoreni_tokovi.ipynb",
        "QR kod za numericki pokus otvorenih tokova u JupyterLiteu",
    ),
}


def render_svg(url: str, description: str) -> str:
    qr = qrcode.QRCode(error_correction=ERROR_CORRECT_M, box_size=1, border=4)
    qr.add_data(url)
    qr.make(fit=True)
    matrix = qr.get_matrix()
    size = len(matrix)
    commands: list[str] = []
    for y, row in enumerate(matrix):
        for x, dark in enumerate(row):
            if dark:
                commands.append(f"M{x} {y}h1v1H{x}z")
    path = "".join(commands)
    return (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {size} {size}" '
        'role="img" aria-labelledby="qr-title qr-desc" '
        'preserveAspectRatio="xMidYMid meet">\n'
        f'  <title id="qr-title">{description}</title>\n'
        f'  <desc id="qr-desc">Poveznica: {url}</desc>\n'
        f'  <rect width="{size}" height="{size}" fill="#ffffff"/>\n'
        f'  <path d="{path}" fill="#111827"/>\n'
        '</svg>\n'
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    stale: list[Path] = []
    for filename, (notebook, description) in ASSETS.items():
        path = QR_DIR / filename
        expected = render_svg(SITE_ROOT + notebook, description)
        actual = path.read_text(encoding="utf-8") if path.exists() else None
        if actual != expected:
            stale.append(path)
            if args.write:
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(expected, encoding="utf-8", newline="\n")
    if stale:
        verb = "ažuriran" if args.write else "zastario ili nedostaje"
        for path in stale:
            print(f"{verb}: {path.relative_to(ROOT)}")
        return 0 if args.write else 1
    print("QR SVG-ovi za svih 17 JupyterLite pokusa su aktualni.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
