"""Generiranje QR kodova za interaktivne prikaze u udžbeniku.

Ova skripta čita popis veza definiran u rječniku VEZE i za svaku
generira SVG datoteku u mapi assets/qr/. Iste SVG datoteke koriste
se u tiskanoj inačici udžbenika u okvirima `.mf1-interaktivno`.

Pokretanje:
    python scripts/generiraj_qr.py

Ovisnosti:
    pip install qrcode[pil]
"""

from __future__ import annotations

import sys
from pathlib import Path

try:
    import qrcode
    import qrcode.image.svg
except ImportError:
    print("Potrebna je knjižnica 'qrcode'. Instalacija:")
    print("    pip install qrcode[pil]")
    sys.exit(1)


# Korijen repozitorija na GitHubu — koristi se za izradu Colab veza.
GITHUB_KORISNIK = "martibasic"
GITHUB_REPOZITORIJ = "MF1_udzbenik"
GITHUB_GRANA = "main"

COLAB_PREDLOZAK = (
    "https://colab.research.google.com/github/"
    f"{GITHUB_KORISNIK}/{GITHUB_REPOZITORIJ}/blob/{GITHUB_GRANA}/notebooks/"
)


# Popis svih interaktivnih prikaza u udžbeniku.
# Ključ je oznaka prikaza (koristi se kao ime SVG datoteke),
# vrijednost je ime notebook datoteke u mapi notebooks/.
VEZE: dict[str, str] = {
    "u01_hidraulicna_presa": "u01_hidraulicna_presa.ipynb",
    "u02_kapilarni_uspon": "u02_kapilarni_uspon.ipynb",
    "u03_diferencijalni_manometar": "u03_diferencijalni_manometar.ipynb",
    "u04_paraboloidna_povrsina": "u04_paraboloidna_povrsina.ipynb",
    "u05_sila_na_ravnu_plohu": "u05_sila_na_ravnu_plohu.ipynb",
    "u06_zakrivljena_ploha": "u06_zakrivljena_ploha.ipynb",
    "u07_gaz_plivajuceg_tijela": "u07_gaz_plivajuceg_tijela.ipynb",
    "u08_kontinuitet_suzenje": "u08_kontinuitet_suzenje.ipynb",
    "u09_venturi": "u09_venturi.ipynb",
    "u10_moody_dijagram": "u10_moody_dijagram.ipynb",
    "u11_sila_na_koljeno": "u11_sila_na_koljeno.ipynb",
    "u12_pelton_lopatica": "u12_pelton_lopatica.ipynb",
    "u13_paralelne_grane": "u13_paralelne_grane.ipynb",
}


def izlazna_mapa() -> Path:
    """Vraća apsolutnu putanju do mape u koju se zapisuju SVG datoteke."""
    korijen = Path(__file__).resolve().parent.parent
    mapa = korijen / "assets" / "qr"
    mapa.mkdir(parents=True, exist_ok=True)
    return mapa


def generiraj_jedan(oznaka: str, ime_notebooka: str, mapa: Path) -> Path:
    """Generira jednu SVG QR datoteku za zadani notebook.

    Parametri
    ---------
    oznaka : kratka oznaka prikaza, ujedno ime izlazne datoteke
    ime_notebooka : ime .ipynb datoteke u mapi notebooks/
    mapa : ciljna mapa za SVG izlaz

    Vraća
    -----
    Put do generirane SVG datoteke.
    """
    veza = COLAB_PREDLOZAK + ime_notebooka

    qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=10,
        border=2,
    )
    qr.add_data(veza)
    qr.make(fit=True)

    tvornica = qrcode.image.svg.SvgPathImage
    slika = qr.make_image(image_factory=tvornica)

    put = mapa / f"{oznaka}.svg"
    slika.save(str(put))
    return put


def main() -> int:
    """Glavna ulazna točka skripte."""
    mapa = izlazna_mapa()

    if not VEZE:
        print("Popis VEZE je prazan — nema QR kodova za generirati.")
        return 0

    print(f"Mapa za izlaz: {mapa}")
    print(f"Broj prikaza:  {len(VEZE)}")
    print()

    for oznaka, ime in VEZE.items():
        put = generiraj_jedan(oznaka, ime, mapa)
        veza = COLAB_PREDLOZAK + ime
        print(f"  [OK] {put.name}")
        print(f"       {veza}")

    print()
    print("Gotovo. SVG QR kodovi spremljeni su u assets/qr/.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
