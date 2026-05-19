"""Generiranje interaktivnih Jupyter notebooka za udžbenik.

Svaki notebook prati istu akademsku strukturu (naslov, cilj,
pretpostavke, računski model, interaktivni prikaz, pitanja, veza
s teorijom). Definicije pojedinog notebooka nalaze se u rječniku
NOTEBOOKS na dnu ove datoteke. Skripta iz tih definicija stvara
gotove .ipynb datoteke u mapi notebooks/.

Pokretanje:
    python scripts/generiraj_notebooke.py

Ovisnosti:
    Samo standardna knjižnica (json).
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

KORIJEN = Path(__file__).resolve().parent.parent
MAPA_NOTEBOOKA = KORIJEN / "notebooks"

STANDARDNI_METADATA: dict[str, Any] = {
    "kernelspec": {
        "display_name": "Python 3 (ipykernel)",
        "language": "python",
        "name": "python3",
    },
    "language_info": {
        "codemirror_mode": {"name": "ipython", "version": 3},
        "file_extension": ".py",
        "mimetype": "text/x-python",
        "name": "python",
        "nbconvert_exporter": "python",
        "pygments_lexer": "ipython3",
        "version": "3.10",
    },
}

STANDARDNI_IMPORTI = (
    "import numpy as np\n"
    "import matplotlib.pyplot as plt\n"
    "from ipywidgets import interact, FloatSlider, Layout\n"
    "\n"
    "plt.rcParams['figure.dpi'] = 110\n"
    "plt.rcParams['font.size'] = 10"
)


def _redovi(tekst: str) -> list[str]:
    """Pretvara tekst u listu redaka kakvu očekuje nbformat."""
    if not tekst:
        return []
    linije = tekst.splitlines(keepends=True)
    return linije


def md(tekst: str) -> dict[str, Any]:
    """Markdown ćelija."""
    return {"cell_type": "markdown", "metadata": {}, "source": _redovi(tekst)}


def code(tekst: str) -> dict[str, Any]:
    """Code ćelija."""
    return {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": _redovi(tekst),
    }


def izgradi_notebook(
    naslov: str,
    poglavlje: str,
    uvod: str,
    cilj: str,
    pretpostavke: str,
    model_md: str,
    kod_funkcije: str,
    prikaz_md: str,
    kod_prikaz: str,
    pitanja: str,
    teorija: str,
) -> dict[str, Any]:
    """Slaže cjelovit notebook iz strukturiranih dijelova."""
    naslov_blok = md(
        f"# {naslov}\n"
        "\n"
        f"**{poglavlje}**\n"
        "\n"
        f"{uvod}"
    )
    cilj_blok = md(
        "## Cilj\n"
        "\n"
        f"{cilj}\n"
        "\n"
        "## Pretpostavke modela\n"
        "\n"
        f"{pretpostavke}"
    )
    model_blok = md(
        "## Računski model\n"
        "\n"
        f"{model_md}"
    )
    prikaz_uvod_blok = md(
        "## Interaktivni prikaz\n"
        "\n"
        f"{prikaz_md}"
    )
    pitanja_blok = md(
        "## Pitanja za istraživanje\n"
        "\n"
        f"{pitanja}"
    )
    teorija_blok = md(
        "## Veza s teorijom poglavlja\n"
        "\n"
        f"{teorija}"
    )

    return {
        "cells": [
            naslov_blok,
            cilj_blok,
            code(STANDARDNI_IMPORTI),
            model_blok,
            code(kod_funkcije),
            prikaz_uvod_blok,
            code(kod_prikaz),
            pitanja_blok,
            teorija_blok,
        ],
        "metadata": STANDARDNI_METADATA,
        "nbformat": 4,
        "nbformat_minor": 5,
    }


# ============================================================================
# Definicije notebooka — svaki ulaz daje jedan .ipynb
# ============================================================================

NOTEBOOKS: dict[str, dict[str, str]] = {}


# ---------------------------------------------------------------------------
# U01 — Hidraulična preša
# ---------------------------------------------------------------------------
NOTEBOOKS["u01_hidraulicna_presa"] = dict(
    naslov="Hidraulična preša — pojačanje sile i pomak klipa",
    poglavlje="Poglavlje U01: Osnove fluida i Pascalov zakon",
    uvod=(
        "Ovaj interaktivni prikaz nadopunjuje Pascalov zakon za zatvoreni "
        "mirujući fluid. Mijenjanjem promjera dvaju klipova i sile na ulazu "
        "prati se međusobna veza pojačanja sile i smanjenja pomaka u "
        "skladu s očuvanjem istisnutog volumena."
    ),
    cilj=(
        "U hidrauličnoj preši mali ulazni klip stvara tlak koji se prenosi "
        "kroz nestlačivi fluid do velikog izlaznog klipa. Pascalov zakon "
        "povezuje promjenu sile s promjenom pomaka. Prikaz omogućuje:\n"
        "\n"
        "1. mijenjanje promjera ulaznog $D_1$ i izlaznog $D_2$ klipa;\n"
        "2. mijenjanje ulazne sile $F_1$;\n"
        "3. praćenje izlazne sile $F_2$ i omjera pomaka $s_1/s_2$."
    ),
    pretpostavke=(
        "- nestlačivi fluid (hidraulično ulje);\n"
        "- klipovi na istoj razini (bez hidrostatičke razlike);\n"
        "- zanemarivo trenje i propuštanje;\n"
        "- statičko stanje, bez ubrzanja klipova."
    ),
    model_md=(
        "Iz Pascalova zakona tlak u zatvorenom fluidu jednak je na oba klipa:\n"
        "\n"
        "$$p = \\frac{F_1}{A_1} = \\frac{F_2}{A_2}.$$\n"
        "\n"
        "Iz toga slijedi izlazna sila:\n"
        "\n"
        "$$F_2 = F_1\\,\\frac{A_2}{A_1} = F_1\\left(\\frac{D_2}{D_1}\\right)^2.$$\n"
        "\n"
        "Očuvanje istisnutog volumena daje omjer pomaka:\n"
        "\n"
        "$$\\frac{s_1}{s_2} = \\frac{A_2}{A_1} = \\left(\\frac{D_2}{D_1}\\right)^2.$$\n"
        "\n"
        "Mehanički rad ulaza i izlaza ostaje jednak: $F_1 s_1 = F_2 s_2$."
    ),
    kod_funkcije=(
        "def presa(D1_mm, D2_mm, F1):\n"
        "    D1 = D1_mm / 1000.0\n"
        "    D2 = D2_mm / 1000.0\n"
        "    A1 = np.pi * D1**2 / 4\n"
        "    A2 = np.pi * D2**2 / 4\n"
        "    p = F1 / A1\n"
        "    F2 = p * A2\n"
        "    omjer_pomaka = A2 / A1\n"
        "    return {'p': p, 'F2': F2, 'A1': A1, 'A2': A2, 'omjer': omjer_pomaka}"
    ),
    prikaz_md=(
        "Klizačima u nastavku biraju se promjeri ulaznog i izlaznog klipa "
        "te sila na ulazu. Gornji graf prikazuje proporcije klipova, "
        "donji prikazuje pojačanje sile i pripadno smanjenje pomaka."
    ),
    kod_prikaz=(
        "def presa_prikaz(D1_mm, D2_mm, F1):\n"
        "    r = presa(D1_mm, D2_mm, F1)\n"
        "\n"
        "    fig, (ax_geo, ax_omjer) = plt.subplots(\n"
        "        1, 2, figsize=(10, 4.5),\n"
        "        gridspec_kw={'width_ratios': [1.2, 1]}\n"
        "    )\n"
        "\n"
        "    # Geometrija klipova\n"
        "    polumjer1 = D1_mm / 2\n"
        "    polumjer2 = D2_mm / 2\n"
        "    ax_geo.add_patch(plt.Rectangle(\n"
        "        (-polumjer1, 0), 2*polumjer1, 80,\n"
        "        fc='#aed6f1', ec='#1565c0', lw=1.5\n"
        "    ))\n"
        "    ax_geo.add_patch(plt.Rectangle(\n"
        "        (250-polumjer2, 0), 2*polumjer2, 80,\n"
        "        fc='#aed6f1', ec='#1565c0', lw=1.5\n"
        "    ))\n"
        "    ax_geo.annotate(\n"
        "        '', xy=(0, 90), xytext=(0, 130),\n"
        "        arrowprops=dict(arrowstyle='->', color='#c62828', lw=2)\n"
        "    )\n"
        "    ax_geo.text(\n"
        "        0, 140, f'$F_1$ = {F1:.0f} N',\n"
        "        ha='center', color='#c62828', fontsize=10\n"
        "    )\n"
        "    ax_geo.annotate(\n"
        "        '', xy=(250, 90), xytext=(250, 130),\n"
        "        arrowprops=dict(arrowstyle='->', color='#2e7d32', lw=2)\n"
        "    )\n"
        "    ax_geo.text(\n"
        "        250, 140, f'$F_2$ = {r[\"F2\"]:.0f} N',\n"
        "        ha='center', color='#2e7d32', fontsize=10\n"
        "    )\n"
        "    # Spojni vod između klipova\n"
        "    ax_geo.plot([polumjer1, 250-polumjer2], [20, 20],\n"
        "                color='#1565c0', lw=3)\n"
        "    ax_geo.text(125, 30, f'p = {r[\"p\"]/1000:.1f} kPa',\n"
        "                ha='center', fontsize=9, color='#1565c0')\n"
        "    ax_geo.set_xlim(-150, 400)\n"
        "    ax_geo.set_ylim(-10, 170)\n"
        "    ax_geo.set_aspect('equal')\n"
        "    ax_geo.axis('off')\n"
        "    ax_geo.set_title(f'$D_1$ = {D1_mm:.0f} mm,  '\n"
        "                     f'$D_2$ = {D2_mm:.0f} mm')\n"
        "\n"
        "    # Stupčasti prikaz omjera\n"
        "    oznake = ['sila $F_2/F_1$', 'pomak $s_2/s_1$']\n"
        "    vrijednosti = [r['omjer'], 1 / r['omjer']]\n"
        "    boje = ['#2e7d32', '#c62828']\n"
        "    ax_omjer.bar(oznake, vrijednosti, color=boje, alpha=0.8)\n"
        "    ax_omjer.set_ylabel('omjer (–)')\n"
        "    ax_omjer.set_title(f'Pojačanje  $A_2/A_1$ = {r[\"omjer\"]:.1f}')\n"
        "    ax_omjer.grid(axis='y', ls=':', alpha=0.5)\n"
        "    for i, v in enumerate(vrijednosti):\n"
        "        ax_omjer.text(i, v + max(vrijednosti) * 0.02,\n"
        "                      f'{v:.2f}', ha='center', fontsize=10)\n"
        "\n"
        "    plt.tight_layout()\n"
        "    plt.show()\n"
        "\n"
        "\n"
        "interact(\n"
        "    presa_prikaz,\n"
        "    D1_mm=FloatSlider(min=10, max=60, step=2, value=20,\n"
        "                       description='$D_1$ (mm)',\n"
        "                       layout=Layout(width='420px')),\n"
        "    D2_mm=FloatSlider(min=40, max=240, step=5, value=120,\n"
        "                       description='$D_2$ (mm)',\n"
        "                       layout=Layout(width='420px')),\n"
        "    F1=FloatSlider(min=50, max=1000, step=10, value=300,\n"
        "                    description='$F_1$ (N)',\n"
        "                    layout=Layout(width='420px'))\n"
        ");"
    ),
    pitanja=(
        "1. **Granični slučaj jednakih klipova.** Što se događa s pojačanjem "
        "sile kada $D_1$ postaje jednako $D_2$? Ima li smisla govoriti o "
        "preši u tom slučaju?\n"
        "\n"
        "2. **Teorijska granica pojačanja.** Postoji li gornja granica "
        "omjera $D_2/D_1$ koju propisuje sam Pascalov zakon? Što u praksi "
        "ograničava pojačanje (otpornost materijala, stvarni hod pumpnog "
        "klipa, prihvatljiva sila operatera)?\n"
        "\n"
        "3. **Bilanca rada.** Provjeri za nekoliko kombinacija parametara "
        "umnožak $F_1 \\cdot s_1$ i $F_2 \\cdot s_2$ uz pretpostavku "
        "konstantnog volumena. Zašto se mehanički rad ne pojačava jednako "
        "kao sila?"
    ),
    teorija=(
        "Ovaj prikaz materijalizira temeljni Pascalov zakon iz poglavlja U01: "
        "promjena tlaka u zatvorenom mirujućem fluidu prenosi se jednako u "
        "svim smjerovima. Pojačanje sile dolazi iz razlike površina, a "
        "smanjenje pomaka iz očuvanja istisnutog volumena. Mehanička "
        "energija ostaje očuvana — hidraulična preša nije izvor rada, nego "
        "pretvarač između male sile s velikim pomakom i velike sile s malim "
        "pomakom."
    ),
)


# ---------------------------------------------------------------------------
# U02 — Kapilarni uspon
# ---------------------------------------------------------------------------
NOTEBOOKS["u02_kapilarni_uspon"] = dict(
    naslov="Kapilarni uspon u tankoj cijevi",
    poglavlje="Poglavlje U02: Viskoznost, površinska napetost i kapilarnost",
    uvod=(
        "Ovaj interaktivni prikaz nadopunjuje izvod kapilarnog uspona "
        "tekućine u tankoj cijevi. Mijenjanjem površinske napetosti, "
        "kontaktnog kuta i promjera kapilare prati se međusobna ovisnost "
        "tih veličina s ravnotežnom visinom."
    ),
    cilj=(
        "U tankoj kapilari ravnoteža između sile površinske napetosti i "
        "težine podignutog stupca tekućine određuje visinu uspona. Prikaz "
        "omogućuje:\n"
        "\n"
        "1. mijenjanje površinske napetosti $\\sigma$;\n"
        "2. mijenjanje kontaktnog kuta $\\theta$;\n"
        "3. mijenjanje promjera kapilare $d$;\n"
        "4. praćenje ravnotežne visine $h$ i predznaka uspona."
    ),
    pretpostavke=(
        "- vertikalna kapilara konstantnog promjera;\n"
        "- statičko stanje (ravnoteža sila);\n"
        "- gustoća tekućine: voda, $\\rho = 998$ kg/m³;\n"
        "- zanemarivi otpori i isparavanje na meniskusu."
    ),
    model_md=(
        "Iz ravnoteže sile površinske napetosti i težine stupca tekućine:\n"
        "\n"
        "$$h = \\frac{4\\sigma\\cos\\theta}{\\rho g d}.$$\n"
        "\n"
        "Za $\\theta < 90°$ rezultat je pozitivan (tekućina kvasi stijenku, "
        "razina se penje), za $\\theta > 90°$ negativan (tekućina ne kvasi "
        "stijenku, razina se spušta)."
    ),
    kod_funkcije=(
        "RHO = 998.0    # gustoća vode (kg/m^3)\n"
        "G = 9.81       # gravitacijska konstanta (m/s^2)\n"
        "\n"
        "def kapilarni_uspon(sigma, theta_deg, d_mm):\n"
        "    theta = np.radians(theta_deg)\n"
        "    d = d_mm / 1000.0\n"
        "    h = 4 * sigma * np.cos(theta) / (RHO * G * d)\n"
        "    return h"
    ),
    prikaz_md=(
        "Klizačima u nastavku biraju se površinska napetost, kontaktni "
        "kut i promjer kapilare. Lijevi prikaz pokazuje presjek kapilare "
        "s pripadnom ravnotežnom razinom, desni prikazuje krivulju "
        "$h(d)$ za odabrane $\\sigma$ i $\\theta$."
    ),
    kod_prikaz=(
        "def kapilara_prikaz(sigma, theta_deg, d_mm):\n"
        "    h = kapilarni_uspon(sigma, theta_deg, d_mm)\n"
        "\n"
        "    fig, (ax_kap, ax_kriv) = plt.subplots(\n"
        "        1, 2, figsize=(10, 5),\n"
        "        gridspec_kw={'width_ratios': [1, 1.4]}\n"
        "    )\n"
        "\n"
        "    # Lijevo: presjek kapilare\n"
        "    r = d_mm / 2\n"
        "    razina = h * 1000  # u mm radi prikaza\n"
        "    visina_okvira = max(60, abs(razina) + 30)\n"
        "    ax_kap.add_patch(plt.Rectangle(\n"
        "        (-r-1, -visina_okvira/2), 1, visina_okvira,\n"
        "        fc='#9e9e9e'\n"
        "    ))\n"
        "    ax_kap.add_patch(plt.Rectangle(\n"
        "        (r, -visina_okvira/2), 1, visina_okvira,\n"
        "        fc='#9e9e9e'\n"
        "    ))\n"
        "    if razina >= 0:\n"
        "        ax_kap.add_patch(plt.Rectangle(\n"
        "            (-r, -visina_okvira/2), 2*r, visina_okvira/2 + razina,\n"
        "            fc='#aed6f1', alpha=0.7\n"
        "        ))\n"
        "    else:\n"
        "        ax_kap.add_patch(plt.Rectangle(\n"
        "            (-r, -visina_okvira/2), 2*r, visina_okvira/2 + razina,\n"
        "            fc='#aed6f1', alpha=0.7\n"
        "        ))\n"
        "    ax_kap.axhline(0, color='#1565c0', ls='--', lw=0.8,\n"
        "                   label='razina izvan kapilare')\n"
        "    ax_kap.axhline(razina, color='#c62828', lw=1.5,\n"
        "                   label=f'meniskus  $h$ = {h*1000:.1f} mm')\n"
        "    ax_kap.set_xlim(-3*r - 5, 3*r + 5)\n"
        "    ax_kap.set_ylim(-visina_okvira/2, visina_okvira/2)\n"
        "    ax_kap.set_aspect('equal')\n"
        "    ax_kap.set_ylabel('visina (mm)')\n"
        "    ax_kap.set_title('Presjek kapilare')\n"
        "    ax_kap.legend(loc='lower right', fontsize=9)\n"
        "    ax_kap.set_xticks([])\n"
        "\n"
        "    # Desno: krivulja h(d) za zadane sigma i theta\n"
        "    d_niz = np.linspace(0.1, 10, 200)\n"
        "    h_niz = kapilarni_uspon(sigma, theta_deg, d_niz) * 1000\n"
        "    ax_kriv.plot(d_niz, h_niz, color='#1565c0', lw=2)\n"
        "    ax_kriv.axhline(0, color='gray', lw=0.5)\n"
        "    ax_kriv.axvline(d_mm, color='#c62828', ls=':', lw=1.2)\n"
        "    ax_kriv.scatter([d_mm], [h*1000], color='#c62828', s=80, zorder=3)\n"
        "    ax_kriv.set_xlabel('promjer kapilare $d$ (mm)')\n"
        "    ax_kriv.set_ylabel('uspon $h$ (mm)')\n"
        "    ax_kriv.set_title(\n"
        "        f'$\\\\sigma$ = {sigma*1000:.0f} mN/m,  '\n"
        "        f'$\\\\theta$ = {theta_deg:.0f}°'\n"
        "    )\n"
        "    ax_kriv.grid(ls=':', alpha=0.5)\n"
        "    ax_kriv.set_xscale('log')\n"
        "\n"
        "    plt.tight_layout()\n"
        "    plt.show()\n"
        "\n"
        "\n"
        "interact(\n"
        "    kapilara_prikaz,\n"
        "    sigma=FloatSlider(min=0.02, max=0.075, step=0.001, value=0.0728,\n"
        "                       description='$\\\\sigma$ (N/m)',\n"
        "                       readout_format='.3f',\n"
        "                       layout=Layout(width='420px')),\n"
        "    theta_deg=FloatSlider(min=0, max=180, step=5, value=0,\n"
        "                           description='$\\\\theta$ (°)',\n"
        "                           layout=Layout(width='420px')),\n"
        "    d_mm=FloatSlider(min=0.1, max=10.0, step=0.1, value=1.0,\n"
        "                      description='$d$ (mm)',\n"
        "                      layout=Layout(width='420px'))\n"
        ");"
    ),
    pitanja=(
        "1. **Granica kvašenja.** Što se događa s uspomon kada $\\theta = 90°$? "
        "Što se događa kada $\\theta > 90°$? Koji fluid-stijenka par bi imao "
        "$\\theta$ veći od $90°$?\n"
        "\n"
        "2. **Ciljana visina.** Pri $\\sigma = 0{,}073$ N/m i $\\theta = 0°$ "
        "(voda u staklenoj kapilari), koji promjer $d$ daje uspon točno "
        "$1{,}0$ mm? A koji $10$ mm?\n"
        "\n"
        "3. **Granica primjenjivosti modela.** Zašto je kapilarni uspon "
        "značajan u porama betona ili tla (promjeri reda $10\\mu$m), ali "
        "praktički zanemariv u cijevima centimetarskog promjera?\n"
        "\n"
        "4. **Skaliranje s promjerom.** Krivulja $h(d)$ na desnom grafu "
        "prikazana je u logaritamskoj skali. Kakvog je oblika ta krivulja "
        "i koji eksponent ovisnosti $h \\propto d^{?}$ slijedi iz formule?"
    ),
    teorija=(
        "Ovaj prikaz materijalizira formulu kapilarnog uspona iz poglavlja "
        "U02. Sve četiri ulazne veličine — površinska napetost, kontaktni "
        "kut, promjer i gustoća — pojavljuju se u ravnoteži težine stupca "
        "tekućine i sile površinske napetosti uzduž oboda meniskusa. U "
        "stvarnim sustavima na rezultat dodatno utječu onečišćenje "
        "stijenke, hrapavost i kemija površine, što ovaj idealizirani "
        "model ne obuhvaća."
    ),
)


# ---------------------------------------------------------------------------
# U03 — Diferencijalni manometar s dva fluida
# ---------------------------------------------------------------------------
NOTEBOOKS["u03_diferencijalni_manometar"] = dict(
    naslov="Diferencijalni manometar s dva fluida",
    poglavlje="Poglavlje U03: Hidrostatička raspodjela tlaka i manometrija",
    uvod=(
        "Ovaj interaktivni prikaz nadopunjuje rad s manometrima u "
        "poglavlju U03. Mijenjanjem gustoća dvaju fluida i razlike "
        "visine njihovih razina u U-cijevi prati se izmjerena razlika "
        "tlakova."
    ),
    cilj=(
        "U diferencijalnom manometru s dva fluida različitih gustoća "
        "razlika tlakova između dvaju priključaka mjeri se preko razlike "
        "visina manometarskog fluida u U-cijevi. Prikaz omogućuje:\n"
        "\n"
        "1. mijenjanje gustoće radnog fluida $\\rho_1$;\n"
        "2. mijenjanje gustoće manometarskog fluida $\\rho_2$;\n"
        "3. mijenjanje razlike visina očitanja $\\Delta h$;\n"
        "4. praćenje pripadne razlike tlakova $\\Delta p$."
    ),
    pretpostavke=(
        "- statičko stanje u svim fluidima;\n"
        "- jednolike gustoće u svakom fluidu;\n"
        "- jednake referentne razine na oba priključka;\n"
        "- nema miješanja fluida na granici."
    ),
    model_md=(
        "Iz hidrostatičke bilance po manometarskom putu slijedi razlika "
        "tlakova između dvaju priključaka:\n"
        "\n"
        "$$\\Delta p = (\\rho_2 - \\rho_1)\\,g\\,\\Delta h.$$\n"
        "\n"
        "Manometarski fluid mora biti gušći od radnog ($\\rho_2 > \\rho_1$) "
        "da bi razlika visine bila pozitivno mjerljiva."
    ),
    kod_funkcije=(
        "G = 9.81       # gravitacijska konstanta (m/s^2)\n"
        "\n"
        "def manometar(rho1, rho2, dh_mm):\n"
        "    dh = dh_mm / 1000.0\n"
        "    dp = (rho2 - rho1) * G * dh\n"
        "    return dp"
    ),
    prikaz_md=(
        "Klizačima u nastavku biraju se gustoće dvaju fluida i razlika "
        "visine očitanja. Prikaz pokazuje shematski U-manometar i pripadnu "
        "razliku tlakova izraženu u kilopaskalima."
    ),
    kod_prikaz=(
        "def manometar_prikaz(rho1, rho2, dh_mm):\n"
        "    dp = manometar(rho1, rho2, dh_mm)\n"
        "\n"
        "    fig, ax = plt.subplots(figsize=(8, 6))\n"
        "\n"
        "    # U-manometar\n"
        "    # Lijevi i desni stupac\n"
        "    sirina = 30\n"
        "    visina = 200\n"
        "    razmak = 100\n"
        "\n"
        "    # Donja krivina U-cijevi (poluellipsa)\n"
        "    theta = np.linspace(np.pi, 2*np.pi, 50)\n"
        "    radius = razmak / 2\n"
        "    x_donji = razmak/2 + radius * np.cos(theta)\n"
        "    y_donji = -radius * np.abs(np.sin(theta)) * 0.6\n"
        "\n"
        "    # Lijevi stupac (radni fluid 1)\n"
        "    razina_lijevo = visina - dh_mm/2\n"
        "    ax.fill_between([-sirina/2, sirina/2], 0, razina_lijevo,\n"
        "                     fc='#aed6f1', alpha=0.7)\n"
        "    ax.fill_between([-sirina/2, sirina/2], razina_lijevo, visina,\n"
        "                     fc='#f4cccc', alpha=0.4)\n"
        "\n"
        "    # Desni stupac (radni fluid 1 iznad, fluid 2 ispod)\n"
        "    razina_desno = visina + dh_mm/2\n"
        "    ax.fill_between([razmak-sirina/2, razmak+sirina/2], 0, razina_desno,\n"
        "                     fc='#aed6f1', alpha=0.7)\n"
        "    ax.fill_between([razmak-sirina/2, razmak+sirina/2], razina_desno, visina,\n"
        "                     fc='#f4cccc', alpha=0.4)\n"
        "\n"
        "    # Granice cijevi\n"
        "    for x in [-sirina/2, sirina/2, razmak-sirina/2, razmak+sirina/2]:\n"
        "        ax.plot([x, x], [0, visina], color='#444', lw=2)\n"
        "\n"
        "    # Razine i oznake\n"
        "    ax.plot([-sirina/2-10, sirina/2+10], [razina_lijevo, razina_lijevo],\n"
        "             color='#c62828', lw=1.2)\n"
        "    ax.plot([razmak-sirina/2-10, razmak+sirina/2+10],\n"
        "             [razina_desno, razina_desno],\n"
        "             color='#c62828', lw=1.2)\n"
        "\n"
        "    # Oznaka Δh\n"
        "    ax.annotate('', xy=(razmak + 60, razina_desno),\n"
        "                xytext=(razmak + 60, razina_lijevo),\n"
        "                arrowprops=dict(arrowstyle='<->', color='#c62828'))\n"
        "    ax.text(razmak + 70, (razina_desno + razina_lijevo)/2,\n"
        "            f'$\\\\Delta h$\\n{dh_mm:.0f} mm',\n"
        "            color='#c62828', fontsize=10, va='center')\n"
        "\n"
        "    # Oznake priključaka\n"
        "    ax.text(0, visina + 20, 'priključak A', ha='center', fontsize=10)\n"
        "    ax.text(razmak, visina + 20, 'priključak B', ha='center', fontsize=10)\n"
        "\n"
        "    # Legenda fluida\n"
        "    ax.text(-80, visina/2, 'radni\\nfluid 1\\n$\\\\rho_1$',\n"
        "            ha='center', fontsize=9, color='#1565c0')\n"
        "    ax.text(razmak/2, -25, 'manometarski fluid 2  $\\\\rho_2$',\n"
        "            ha='center', fontsize=9, color='#c62828')\n"
        "\n"
        "    ax.set_xlim(-120, razmak + 130)\n"
        "    ax.set_ylim(-50, visina + 50)\n"
        "    ax.set_aspect('equal')\n"
        "    ax.axis('off')\n"
        "    ax.set_title(\n"
        "        f'$\\\\rho_1$ = {rho1:.0f} kg/m³,  $\\\\rho_2$ = {rho2:.0f} kg/m³\\n'\n"
        "        f'$\\\\Delta p$ = $p_A - p_B$ = {dp/1000:.2f} kPa',\n"
        "        fontsize=11\n"
        "    )\n"
        "\n"
        "    plt.tight_layout()\n"
        "    plt.show()\n"
        "\n"
        "\n"
        "interact(\n"
        "    manometar_prikaz,\n"
        "    rho1=FloatSlider(min=500, max=1500, step=50, value=998,\n"
        "                      description='$\\\\rho_1$ (kg/m³)',\n"
        "                      layout=Layout(width='420px')),\n"
        "    rho2=FloatSlider(min=1000, max=13600, step=100, value=13600,\n"
        "                      description='$\\\\rho_2$ (kg/m³)',\n"
        "                      layout=Layout(width='420px')),\n"
        "    dh_mm=FloatSlider(min=10, max=300, step=5, value=80,\n"
        "                       description='$\\\\Delta h$ (mm)',\n"
        "                       layout=Layout(width='420px'))\n"
        ");"
    ),
    pitanja=(
        "1. **Identične gustoće.** Što se događa s razlikom tlakova kada "
        "$\\rho_1 \\approx \\rho_2$? Zašto je u praksi tada manometar "
        "neupotrebljiv?\n"
        "\n"
        "2. **Izbor manometarskog fluida.** Za male razlike tlakova "
        "(reda $100$ Pa) traži se velika razlika visine očitanja $\\Delta h$. "
        "Koja kombinacija gustoća daje veću $\\Delta h$ pri istom "
        "$\\Delta p$ — voda i živa ili voda i tetraklor-ugljik "
        "($\\rho \\approx 1590$ kg/m³)?\n"
        "\n"
        "3. **Pravilo zbroja.** U realnom manometru put od priključka A "
        "do B može prolaziti kroz tri fluida različitih gustoća. Kako se "
        "iz osnovne formule ovog prikaza dobiva slučaj s tri fluida?"
    ),
    teorija=(
        "Ovaj prikaz materijalizira ideju da se razlika tlakova između "
        "dvije točke u mirujućim spojenim fluidima može pročitati iz "
        "razlike visine i razlike gustoća. To je radni princip svakog "
        "manometra s tekućinom, od jednostavnog U-manometra do "
        "diferencijalnog manometra na filtru ili Venturijevoj cijevi. "
        "Načelo se proširuje na više fluida zbrajanjem doprinosa po "
        "svakom segmentu manometarskog puta."
    ),
)


# ---------------------------------------------------------------------------
# U04 — Paraboloidna slobodna površina rotirajućeg spremnika
# ---------------------------------------------------------------------------
NOTEBOOKS["u04_paraboloidna_povrsina"] = dict(
    naslov="Paraboloidna slobodna površina u rotirajućem spremniku",
    poglavlje="Poglavlje U04: Relativno mirovanje fluida",
    uvod=(
        "Ovaj interaktivni prikaz nadopunjuje izvod oblika slobodne "
        "površine fluida u cilindričnom spremniku koji rotira oko vlastite "
        "osi konstantnom kutnom brzinom. Mijenjanjem kutne brzine, "
        "polumjera spremnika i početne visine fluida prati se ravnotežni "
        "paraboloid."
    ),
    cilj=(
        "U cilindričnom spremniku koji rotira oko vlastite osi, slobodna "
        "površina fluida poprima oblik paraboloida. Centrifugalna sila u "
        "rotirajućem sustavu zajedno s gravitacijom daje efektivno polje "
        "sila koje određuje taj profil. Prikaz omogućuje:\n"
        "\n"
        "1. mijenjanje kutne brzine $\\omega$;\n"
        "2. mijenjanje polumjera spremnika $R$;\n"
        "3. mijenjanje početne visine fluida $h_0$ pri mirovanju;\n"
        "4. praćenje visine fluida u središtu i na rubu spremnika."
    ),
    pretpostavke=(
        "- spremnik rotira konstantnom kutnom brzinom $\\omega$;\n"
        "- fluid je dosegao stacionarno stanje u rotirajućem okviru;\n"
        "- nema isparavanja, gubitaka, niti gubljenja fluida preko ruba;\n"
        "- ukupni volumen fluida ostaje očuvan."
    ),
    model_md=(
        "U rotirajućem okviru efektivno ubrzanje u radijalnom smjeru "
        "iznosi $\\omega^2 r$. Profil slobodne površine je paraboloid:\n"
        "\n"
        "$$z(r) = z_d + \\frac{\\omega^2 r^2}{2g},$$\n"
        "\n"
        "gdje je $z_d$ visina fluida u središtu (na osi rotacije). "
        "Iz očuvanja volumena:\n"
        "\n"
        "$$z_d = h_0 - \\frac{\\omega^2 R^2}{4g}.$$\n"
        "\n"
        "Visina fluida na rubu spremnika je $z_R = h_0 + \\omega^2 R^2 / (4g)$. "
        "Kada $z_d < 0$, dno se ogoljava i dolazi do gubitka fluida preko "
        "ruba (zadaća se mijenja, pa ovaj model više ne vrijedi)."
    ),
    kod_funkcije=(
        "G = 9.81\n"
        "\n"
        "def paraboloid(omega, R_mm, h0_m):\n"
        "    R = R_mm / 1000.0\n"
        "    z_d = h0_m - (omega**2 * R**2) / (4 * G)\n"
        "    z_R = h0_m + (omega**2 * R**2) / (4 * G)\n"
        "    return {'z_d': z_d, 'z_R': z_R, 'R': R}"
    ),
    prikaz_md=(
        "Klizačima u nastavku biraju se kutna brzina, polumjer spremnika "
        "i početna visina fluida pri mirovanju. Prikaz pokazuje aksijalni "
        "presjek spremnika s pripadnim paraboloidom."
    ),
    kod_prikaz=(
        "def paraboloid_prikaz(omega, R_mm, h0_m):\n"
        "    r = paraboloid(omega, R_mm, h0_m)\n"
        "    R = r['R']\n"
        "    z_d = r['z_d']\n"
        "    z_R = r['z_R']\n"
        "\n"
        "    fig, ax = plt.subplots(figsize=(8, 6))\n"
        "\n"
        "    # Profil paraboloida\n"
        "    r_niz = np.linspace(-R, R, 200)\n"
        "    z_niz = z_d + (omega**2 * r_niz**2) / (2 * G)\n"
        "\n"
        "    # Visina spremnika (uzet ćemo 1.5 × h0)\n"
        "    H_sprem = max(1.5 * h0_m, z_R + 0.1)\n"
        "\n"
        "    # Stijenke spremnika\n"
        "    ax.plot([-R, -R], [0, H_sprem], color='#444', lw=2.5)\n"
        "    ax.plot([R, R], [0, H_sprem], color='#444', lw=2.5)\n"
        "    ax.plot([-R, R], [0, 0], color='#444', lw=2.5)\n"
        "\n"
        "    # Fluid (ispod paraboloida)\n"
        "    if z_d >= 0:\n"
        "        ax.fill_between(r_niz, 0, z_niz, fc='#aed6f1', alpha=0.7)\n"
        "        upozorenje = ''\n"
        "    else:\n"
        "        # Dno je ogoljeno: fluid samo gdje je z_niz > 0\n"
        "        z_mask = np.maximum(z_niz, 0)\n"
        "        ax.fill_between(r_niz, 0, z_mask, fc='#aed6f1', alpha=0.7)\n"
        "        upozorenje = '   (dno ogoljeno — model više ne vrijedi)'\n"
        "\n"
        "    # Linija paraboloida\n"
        "    ax.plot(r_niz, z_niz, color='#1565c0', lw=2.2,\n"
        "             label='slobodna površina')\n"
        "\n"
        "    # Linija početne razine pri mirovanju\n"
        "    ax.axhline(h0_m, color='gray', ls='--', lw=1, alpha=0.7,\n"
        "                label=f'$h_0$ = {h0_m:.2f} m (mirovanje)')\n"
        "\n"
        "    # Oznake\n"
        "    ax.annotate('', xy=(0, z_d), xytext=(0, h0_m),\n"
        "                 arrowprops=dict(arrowstyle='<->', color='#c62828'))\n"
        "    ax.text(0.02, (z_d + h0_m)/2,\n"
        "             f'$h_0 - z_d$ = {h0_m - z_d:.3f} m',\n"
        "             color='#c62828', fontsize=9)\n"
        "\n"
        "    ax.set_xlim(-R*1.5, R*1.5)\n"
        "    ax.set_ylim(-H_sprem*0.1, H_sprem*1.1)\n"
        "    ax.set_xlabel('radijalna koordinata r (m)')\n"
        "    ax.set_ylabel('visina z (m)')\n"
        "    ax.set_title(\n"
        "        f'$\\\\omega$ = {omega:.1f} rad/s,  $R$ = {R*1000:.0f} mm\\n'\n"
        "        f'$z_d$ = {z_d:.3f} m,  $z_R$ = {z_R:.3f} m{upozorenje}'\n"
        "    )\n"
        "    ax.legend(loc='upper center', fontsize=9)\n"
        "    ax.grid(ls=':', alpha=0.5)\n"
        "\n"
        "    plt.tight_layout()\n"
        "    plt.show()\n"
        "\n"
        "\n"
        "interact(\n"
        "    paraboloid_prikaz,\n"
        "    omega=FloatSlider(min=0, max=20, step=0.2, value=8,\n"
        "                       description='$\\\\omega$ (rad/s)',\n"
        "                       layout=Layout(width='420px')),\n"
        "    R_mm=FloatSlider(min=50, max=400, step=10, value=150,\n"
        "                      description='$R$ (mm)',\n"
        "                      layout=Layout(width='420px')),\n"
        "    h0_m=FloatSlider(min=0.1, max=0.8, step=0.02, value=0.30,\n"
        "                      description='$h_0$ (m)',\n"
        "                      layout=Layout(width='420px'))\n"
        ");"
    ),
    pitanja=(
        "1. **Granica ogoljavanja dna.** Pri kojoj kombinaciji $\\omega$ "
        "i $R$ središte spremnika počinje ogoljavati ($z_d = 0$)? "
        "Izvodom iz formule pokaži tu vezu.\n"
        "\n"
        "2. **Skala s polumjerom.** Ako se polumjer spremnika udvostruči "
        "uz konstantne $\\omega$ i $h_0$, kako se mijenja razlika "
        "$z_R - z_d$? Koji je eksponent ovisnosti?\n"
        "\n"
        "3. **Volumno očuvanje.** Provjeri za nekoliko kombinacija da je "
        "volumen paraboloida iznad osnovne razine $h_0$ jednak volumenu "
        "praznog prostora ispod te razine u središtu spremnika.\n"
        "\n"
        "4. **Tehnička primjena.** Centrifuga laboratorijskog stripa "
        "rotira pri $\\omega \\approx 100$ rad/s. Koliki bi bio paraboloid "
        "u cijevi polumjera $10$ mm? Što to govori o pretpostavkama ovog "
        "modela u stvarnoj centrifugi?"
    ),
    teorija=(
        "Ovaj prikaz materijalizira ravnotežu u rotirajućem fluidu iz "
        "poglavlja U04. Paraboloidni oblik slobodne površine izravna je "
        "posljedica linearne ovisnosti centrifugalnog ubrzanja o "
        "radijalnoj udaljenosti. Isti se model koristi pri analizi "
        "centrifuga, rotirajućih spremnika za miješanje, ali i pri "
        "procjeni ponašanja goriva u spremniku autocisterne u zavoju."
    ),
)


# ---------------------------------------------------------------------------
# U05 — Sila i hvatište na pravokutnu plohu pod vodom
# ---------------------------------------------------------------------------
NOTEBOOKS["u05_sila_na_ravnu_plohu"] = dict(
    naslov="Sila i hvatište na pravokutnu plohu pod vodom",
    poglavlje="Poglavlje U05: Hidrostatske sile na ravne plohe",
    uvod=(
        "Ovaj interaktivni prikaz nadopunjuje izvod hidrostatičke sile na "
        "ravnu uronjenu plohu. Mijenjanjem dubine gornjeg ruba, visine "
        "plohe i kuta nagiba prati se ukupna sila i položaj hvatišta."
    ),
    cilj=(
        "Na ravnoj uronjenoj plohi hidrostatička sila proizlazi iz "
        "integralnog dijela tlaka po plohi, a njezino hvatište spušteno "
        "je ispod težišta plohe. Prikaz omogućuje:\n"
        "\n"
        "1. mijenjanje dubine gornjeg ruba plohe $h_t$;\n"
        "2. mijenjanje visine plohe $b$;\n"
        "3. mijenjanje kuta plohe prema vertikali $\\alpha$;\n"
        "4. praćenje sile, dubine težišta i položaja hvatišta."
    ),
    pretpostavke=(
        "- jednolika gustoća vode, $\\rho = 998$ kg/m³;\n"
        "- pravokutna ploha jedinične širine ($L = 1$ m);\n"
        "- statičko stanje, bez strujanja;\n"
        "- na slobodnoj površini atmosferski tlak (manometarski tlak nula)."
    ),
    model_md=(
        "Dubina težišta uronjene plohe iznosi:\n"
        "\n"
        "$$h_c = h_t + \\frac{b}{2}\\cos\\alpha.$$\n"
        "\n"
        "Ukupna sila na plohu:\n"
        "\n"
        "$$F = \\rho g A h_c, \\qquad A = b \\cdot L.$$\n"
        "\n"
        "Položaj hvatišta sile, mjeren po plohi od slobodne površine:\n"
        "\n"
        "$$y_{CP} = \\frac{h_c}{\\cos\\alpha} + \\frac{I_{xc}\\cos\\alpha}{A\\,h_c},$$\n"
        "\n"
        "gdje je $I_{xc} = L b^3 / 12$ aksijalni moment tromosti "
        "pravokutnika oko vlastite težišne osi."
    ),
    kod_funkcije=(
        "RHO = 998.0\n"
        "G = 9.81\n"
        "L = 1.0  # jedinična širina plohe (m)\n"
        "\n"
        "def ploha(h_t, b, alpha_deg):\n"
        "    alpha = np.radians(alpha_deg)\n"
        "    h_c = h_t + (b / 2) * np.cos(alpha)\n"
        "    A = b * L\n"
        "    F = RHO * G * A * h_c\n"
        "    I_xc = L * b**3 / 12\n"
        "    if h_c > 0 and np.cos(alpha) != 0:\n"
        "        y_cp = h_c / np.cos(alpha) + (I_xc * np.cos(alpha)) / (A * h_c)\n"
        "    else:\n"
        "        y_cp = float('nan')\n"
        "    return {'F': F, 'h_c': h_c, 'y_cp': y_cp, 'A': A}"
    ),
    prikaz_md=(
        "Klizačima u nastavku biraju se dubina gornjeg ruba, visina "
        "plohe i kut nagiba. Prikaz pokazuje bočni presjek plohe pod "
        "vodom uz dijagram tlaka i položaj hvatišta sile."
    ),
    kod_prikaz=(
        "def ploha_prikaz(h_t, b, alpha_deg):\n"
        "    r = ploha(h_t, b, alpha_deg)\n"
        "    alpha = np.radians(alpha_deg)\n"
        "\n"
        "    fig, ax = plt.subplots(figsize=(9, 6))\n"
        "\n"
        "    # Slobodna površina\n"
        "    ax.axhline(0, color='#1565c0', lw=2, label='slobodna površina')\n"
        "    ax.fill_between([-1, 3], 0, -max(2*(h_t+b), 2),\n"
        "                     fc='#aed6f1', alpha=0.3)\n"
        "\n"
        "    # Ploha — bočni presjek\n"
        "    x_top = 1.0\n"
        "    y_top = -h_t\n"
        "    x_bot = x_top + b * np.sin(alpha)\n"
        "    y_bot = -h_t - b * np.cos(alpha)\n"
        "    ax.plot([x_top, x_bot], [y_top, y_bot],\n"
        "             color='#c62828', lw=4, label='ploha')\n"
        "\n"
        "    # Dijagram tlaka uz plohu\n"
        "    n = 30\n"
        "    s = np.linspace(0, b, n)  # koordinata uz plohu\n"
        "    h_uz = h_t + s * np.cos(alpha)\n"
        "    p_uz = RHO * G * h_uz / 1000  # u kPa\n"
        "    x_p = x_top + s * np.sin(alpha)\n"
        "    y_p = y_top - s * np.cos(alpha)\n"
        "    # Strelice tlaka (normalne na plohu)\n"
        "    skala = 0.005  # m po kPa\n"
        "    for i in range(0, n, 3):\n"
        "        n_x = np.cos(alpha)  # normala plohe (vanjska)\n"
        "        n_y = np.sin(alpha)\n"
        "        L_str = p_uz[i] * skala\n"
        "        ax.annotate('', xy=(x_p[i], y_p[i]),\n"
        "                     xytext=(x_p[i] + L_str * n_x,\n"
        "                              y_p[i] + L_str * n_y),\n"
        "                     arrowprops=dict(arrowstyle='->',\n"
        "                                       color='#c62828', alpha=0.6))\n"
        "\n"
        "    # Hvatište sile\n"
        "    if not np.isnan(r['y_cp']):\n"
        "        s_cp = r['y_cp'] - h_t / np.cos(alpha)\n"
        "        if 0 <= s_cp <= b:\n"
        "            x_cp = x_top + s_cp * np.sin(alpha)\n"
        "            y_cp = y_top - s_cp * np.cos(alpha)\n"
        "            ax.scatter([x_cp], [y_cp], color='#2e7d32',\n"
        "                        s=120, zorder=5, marker='X',\n"
        "                        label='hvatište $y_{CP}$')\n"
        "\n"
        "    ax.set_xlim(-0.3, 3)\n"
        "    ax.set_ylim(-(h_t + b + 0.5), 0.5)\n"
        "    ax.set_aspect('equal')\n"
        "    ax.set_xlabel('horizontalna koordinata (m)')\n"
        "    ax.set_ylabel('dubina (m)')\n"
        "    ax.set_title(\n"
        "        f'$h_t$ = {h_t:.2f} m,  $b$ = {b:.2f} m,  '\n"
        "        f'$\\\\alpha$ = {alpha_deg:.0f}°\\n'\n"
        "        f'$F$ = {r[\"F\"]/1000:.2f} kN,  '\n"
        "        f'$h_c$ = {r[\"h_c\"]:.3f} m,  '\n"
        "        f'$y_{{CP}}$ = {r[\"y_cp\"]:.3f} m'\n"
        "    )\n"
        "    ax.legend(loc='lower right', fontsize=9)\n"
        "    ax.grid(ls=':', alpha=0.5)\n"
        "\n"
        "    plt.tight_layout()\n"
        "    plt.show()\n"
        "\n"
        "\n"
        "interact(\n"
        "    ploha_prikaz,\n"
        "    h_t=FloatSlider(min=0, max=4, step=0.1, value=0.5,\n"
        "                     description='$h_t$ (m)',\n"
        "                     layout=Layout(width='420px')),\n"
        "    b=FloatSlider(min=0.2, max=3, step=0.1, value=1.5,\n"
        "                   description='$b$ (m)',\n"
        "                   layout=Layout(width='420px')),\n"
        "    alpha_deg=FloatSlider(min=0, max=80, step=5, value=30,\n"
        "                           description='$\\\\alpha$ (°)',\n"
        "                           layout=Layout(width='420px'))\n"
        ");"
    ),
    pitanja=(
        "1. **Položaj hvatišta.** Hvatište sile uvijek leži ispod težišta "
        "plohe. Kako se ta razlika mijenja kada $h_t$ raste, a $b$ i "
        "$\\alpha$ ostaju nepromijenjeni? Zašto se hvatište približava "
        "težištu pri velikim dubinama?\n"
        "\n"
        "2. **Vertikalna i nagnuta ploha.** Pri istoj površini i istoj "
        "dubini težišta, daje li okomita ploha veću ili manju silu od "
        "nagnute? A drukčiji položaj hvatišta?\n"
        "\n"
        "3. **Skala s visinom plohe.** Provjeri da pri udvostručenoj "
        "visini $b$ (uz konstantne $h_t$ i $\\alpha$) sila raste više od "
        "dva puta. Koji je razlog?\n"
        "\n"
        "4. **Inženjerska procjena.** Za vrata brane s $h_t = 0$ i "
        "$b = 5$ m, okomito uronjena, kolika je sila po metru širine? "
        "Gdje leži hvatište?"
    ),
    teorija=(
        "Ovaj prikaz materijalizira dva temeljna rezultata iz poglavlja "
        "U05: ukupna hidrostatička sila ovisi o površini i dubini "
        "težišta plohe, dok je hvatište te sile uvijek spušteno ispod "
        "težišta zbog linearnog rasta tlaka s dubinom. U poglavlju U06 "
        "isti se aparat proširuje na zakrivljene plohe gdje se sila "
        "razlaže na horizontalnu i vertikalnu komponentu."
    ),
)


# ---------------------------------------------------------------------------
# U06 — Razlaganje sile na zakrivljenu plohu (četvrtina kruga)
# ---------------------------------------------------------------------------
NOTEBOOKS["u06_zakrivljena_ploha"] = dict(
    naslov="Sila na zakrivljenu plohu — četvrtina kruga",
    poglavlje="Poglavlje U06: Zakrivljene plohe i rastav sila",
    uvod=(
        "Ovaj interaktivni prikaz nadopunjuje izvod hidrostatičke sile na "
        "zakrivljenu plohu kroz primjer četvrtine kruga uronjene u vodu. "
        "Mijenjanjem polumjera krivulje, dubine vrha i širine plohe prati "
        "se rastav sile na horizontalnu i vertikalnu komponentu."
    ),
    cilj=(
        "Na zakrivljenoj plohi hidrostatička sila razlaže se na "
        "horizontalnu komponentu (jednaku sili na vertikalnu projekciju "
        "plohe) i vertikalnu komponentu (jednaku težini imaginarnog "
        "volumena fluida iznad ili ispod plohe). Prikaz omogućuje:\n"
        "\n"
        "1. mijenjanje polumjera plohe $R$;\n"
        "2. mijenjanje dubine vrha plohe $h_t$;\n"
        "3. mijenjanje širine plohe $L$;\n"
        "4. praćenje komponenti $F_H$ i $F_V$ te rezultante $F_R$."
    ),
    pretpostavke=(
        "- jednolika gustoća vode, $\\rho = 998$ kg/m³;\n"
        "- ploha je četvrtina kruga polumjera $R$ s vrhom na dubini $h_t$;\n"
        "- konveksna strana plohe okrenuta je prema fluidu;\n"
        "- statičko stanje, bez strujanja."
    ),
    model_md=(
        "Horizontalna komponenta sile jednaka je sili na vertikalnu "
        "projekciju plohe — pravokutnik visine $R$ i širine $L$:\n"
        "\n"
        "$$F_H = \\rho g L R \\left(h_t + \\frac{R}{2}\\right).$$\n"
        "\n"
        "Vertikalna komponenta jednaka je težini imaginarnog volumena "
        "fluida iznad zakrivljene plohe:\n"
        "\n"
        "$$F_V = \\rho g L \\left(h_t R + R^2 - \\frac{\\pi R^2}{4}\\right).$$\n"
        "\n"
        "Iznos rezultante i kut prema horizontali:\n"
        "\n"
        "$$F_R = \\sqrt{F_H^2 + F_V^2}, \\qquad "
        "\\tan\\varphi = \\frac{F_V}{F_H}.$$"
    ),
    kod_funkcije=(
        "RHO = 998.0\n"
        "G = 9.81\n"
        "\n"
        "def zakrivljena(R, h_t, L):\n"
        "    F_H = RHO * G * L * R * (h_t + R/2)\n"
        "    V_imag = L * (h_t * R + R**2 - np.pi * R**2 / 4)\n"
        "    F_V = RHO * G * V_imag\n"
        "    F_R = np.sqrt(F_H**2 + F_V**2)\n"
        "    phi = np.degrees(np.arctan2(F_V, F_H))\n"
        "    return {'F_H': F_H, 'F_V': F_V, 'F_R': F_R, 'phi': phi}"
    ),
    prikaz_md=(
        "Klizačima u nastavku biraju se polumjer, dubina vrha i širina "
        "plohe. Prikaz pokazuje bočni presjek četvrtine kruga uronjene u "
        "vodu s vektorima komponenti sile."
    ),
    kod_prikaz=(
        "def zakrivljena_prikaz(R, h_t, L):\n"
        "    r = zakrivljena(R, h_t, L)\n"
        "\n"
        "    fig, ax = plt.subplots(figsize=(8, 6))\n"
        "\n"
        "    # Slobodna površina\n"
        "    ax.axhline(0, color='#1565c0', lw=2)\n"
        "    ax.fill_between([-2, 2], 0, -h_t - 1.5*R,\n"
        "                     fc='#aed6f1', alpha=0.3)\n"
        "\n"
        "    # Četvrtina kruga (vrh u (0, -h_t), središte kruga u (R, -h_t))\n"
        "    theta = np.linspace(np.pi, 1.5*np.pi, 60)\n"
        "    x_arc = R + R * np.cos(theta)\n"
        "    y_arc = -h_t + R * np.sin(theta)\n"
        "    ax.plot(x_arc, y_arc, color='#c62828', lw=4, label='ploha')\n"
        "    ax.fill_between(x_arc, y_arc, -h_t,\n"
        "                     fc='#f4cccc', alpha=0.3,\n"
        "                     label='imaginarni volumen')\n"
        "\n"
        "    # Hvatište — približno u težištu četvrtine kruga\n"
        "    x_h = R - 4*R/(3*np.pi)\n"
        "    y_h = -h_t - 4*R/(3*np.pi)\n"
        "\n"
        "    # Vektor F_H\n"
        "    skala = 0.001 / max(r['F_H'], r['F_V']) * R\n"
        "    LH = r['F_H'] * skala\n"
        "    LV = r['F_V'] * skala\n"
        "    ax.annotate('', xy=(x_h - LH, y_h), xytext=(x_h, y_h),\n"
        "                 arrowprops=dict(arrowstyle='->',\n"
        "                                   color='#1976d2', lw=2.2))\n"
        "    ax.text(x_h - LH/2, y_h + 0.05,\n"
        "             f'$F_H$ = {r[\"F_H\"]/1000:.1f} kN',\n"
        "             color='#1976d2', fontsize=10, ha='center')\n"
        "\n"
        "    # Vektor F_V\n"
        "    ax.annotate('', xy=(x_h, y_h - LV), xytext=(x_h, y_h),\n"
        "                 arrowprops=dict(arrowstyle='->',\n"
        "                                   color='#2e7d32', lw=2.2))\n"
        "    ax.text(x_h - 0.05, y_h - LV/2,\n"
        "             f'$F_V$ = {r[\"F_V\"]/1000:.1f} kN',\n"
        "             color='#2e7d32', fontsize=10, ha='right')\n"
        "\n"
        "    # Vektor rezultante\n"
        "    ax.annotate('', xy=(x_h - LH, y_h - LV), xytext=(x_h, y_h),\n"
        "                 arrowprops=dict(arrowstyle='->',\n"
        "                                   color='#c62828', lw=2.5))\n"
        "    ax.text(x_h - LH - 0.05, y_h - LV - 0.05,\n"
        "             f'$F_R$ = {r[\"F_R\"]/1000:.1f} kN\\n'\n"
        "             f'$\\\\varphi$ = {r[\"phi\"]:.1f}°',\n"
        "             color='#c62828', fontsize=10, ha='right')\n"
        "\n"
        "    ax.set_xlim(-0.5, R*1.5 + 0.5)\n"
        "    ax.set_ylim(-(h_t + R + 0.3), 0.3)\n"
        "    ax.set_aspect('equal')\n"
        "    ax.set_xlabel('horizontalna koordinata (m)')\n"
        "    ax.set_ylabel('dubina (m)')\n"
        "    ax.set_title(\n"
        "        f'$R$ = {R:.2f} m,  $h_t$ = {h_t:.2f} m,  $L$ = {L:.2f} m'\n"
        "    )\n"
        "    ax.legend(loc='lower right', fontsize=9)\n"
        "    ax.grid(ls=':', alpha=0.5)\n"
        "\n"
        "    plt.tight_layout()\n"
        "    plt.show()\n"
        "\n"
        "\n"
        "interact(\n"
        "    zakrivljena_prikaz,\n"
        "    R=FloatSlider(min=0.2, max=2.0, step=0.1, value=0.8,\n"
        "                   description='$R$ (m)',\n"
        "                   layout=Layout(width='420px')),\n"
        "    h_t=FloatSlider(min=0, max=5, step=0.1, value=1.0,\n"
        "                     description='$h_t$ (m)',\n"
        "                     layout=Layout(width='420px')),\n"
        "    L=FloatSlider(min=0.5, max=5.0, step=0.1, value=2.0,\n"
        "                   description='$L$ (m)',\n"
        "                   layout=Layout(width='420px'))\n"
        ");"
    ),
    pitanja=(
        "1. **Granični slučaj plitke vode.** Što se događa s omjerom "
        "$F_V/F_H$ kada $h_t \\to 0$? Zašto vertikalna komponenta postaje "
        "značajnija u plitkoj vodi?\n"
        "\n"
        "2. **Granični slučaj duboke vode.** Za $h_t \\gg R$, što vrijedi "
        "za omjer $F_V/F_H$? Postoji li gornja granica?\n"
        "\n"
        "3. **Smjer rezultante.** Pri kojoj kombinaciji $R$ i $h_t$ "
        "rezultanta sile prolazi kroz središte krivulje? Što tehnički "
        "znači ta razdvojnica?\n"
        "\n"
        "4. **Inženjerska primjena.** Brodska vrata u doku imaju "
        "zakrivljenu donju polovicu polumjera $R \\approx 1$ m, vrh na "
        "dubini $h_t \\approx 4$ m i širinu $L = 8$ m. Kolika je "
        "rezultanta sile po vratima i pod kojim kutem djeluje?"
    ),
    teorija=(
        "Ovaj prikaz materijalizira ključno opažanje iz poglavlja U06: "
        "sila na zakrivljenu plohu rastavlja se na horizontalnu "
        "komponentu (jednaku sili na vertikalnu projekciju) i vertikalnu "
        "komponentu (jednaku težini imaginarnog volumena fluida iznad "
        "plohe). Taj rastav vrijedi neovisno o obliku krivulje sve dok "
        "se geometrija plohe može pratiti zatvorenim volumenom."
    ),
)


# ---------------------------------------------------------------------------
# U07 — Gaz plivajućeg tijela
# ---------------------------------------------------------------------------
NOTEBOOKS["u07_gaz_plivajuceg_tijela"] = dict(
    naslov="Gaz plivajućeg tijela",
    poglavlje="Poglavlje U07: Uzgon, plivanje i stabilnost",
    uvod=(
        "Ovaj interaktivni prikaz nadopunjuje Arhimedov zakon i izvod gaza "
        "pravokutnog plivajućeg bloka. Mijenjanjem mase tijela i gustoće "
        "fluida prati se ravnotežna dubina urona i sigurnosna margina do "
        "preplavljivanja."
    ),
    cilj=(
        "Plivajuće tijelo u stanju ravnoteže potapa se točno toliko da "
        "težina istisnutog fluida bude jednaka težini tijela. Prikaz "
        "omogućuje:\n"
        "\n"
        "1. mijenjanje mase tijela $m$;\n"
        "2. mijenjanje gustoće fluida $\\rho_f$;\n"
        "3. mijenjanje dimenzija pravokutnog bloka;\n"
        "4. praćenje gaza $d$ i preostale visine iznad razine vode."
    ),
    pretpostavke=(
        "- pravokutni blok dimenzija $L \\times B \\times H$;\n"
        "- masa tijela jednoliko raspoređena (težište u geometrijskom "
        "središtu);\n"
        "- mirna voda bez valova;\n"
        "- statičko stanje, bez vertikalnog ubrzanja."
    ),
    model_md=(
        "Iz Arhimedovog zakona ravnotežna sila uzgona jednaka je težini "
        "tijela:\n"
        "\n"
        "$$\\rho_f g V_{ist} = m g.$$\n"
        "\n"
        "Za pravokutni blok s istisnutim volumenom $V_{ist} = L B d$, gaz "
        "iznosi:\n"
        "\n"
        "$$d = \\frac{m}{\\rho_f L B}.$$\n"
        "\n"
        "Tijelo pliva (uvjet plovnosti) sve dok je $d < H$; preostala "
        "visina iznad razine je $H - d$."
    ),
    kod_funkcije=(
        "G = 9.81\n"
        "\n"
        "def gaz(m, rho_f, L, B, H):\n"
        "    V_potrebno = m / rho_f\n"
        "    d = V_potrebno / (L * B)\n"
        "    plovi = d < H\n"
        "    margina = H - d if plovi else 0\n"
        "    return {'d': d, 'plovi': plovi, 'margina': margina,\n"
        "             'V_ist': V_potrebno}"
    ),
    prikaz_md=(
        "Klizačima u nastavku biraju se masa tijela i gustoća fluida "
        "(uz fiksne dimenzije bloka $L = 2$ m, $B = 1$ m, $H = 0{,}8$ m). "
        "Prikaz pokazuje bočni izgled bloka s ravnotežnim gazom."
    ),
    kod_prikaz=(
        "L = 2.0\n"
        "B = 1.0\n"
        "H = 0.8\n"
        "\n"
        "def gaz_prikaz(m, rho_f):\n"
        "    r = gaz(m, rho_f, L, B, H)\n"
        "    d = r['d']\n"
        "\n"
        "    fig, ax = plt.subplots(figsize=(9, 5.5))\n"
        "\n"
        "    # Slobodna površina (na visini 0)\n"
        "    ax.axhline(0, color='#1565c0', lw=2)\n"
        "    ax.fill_between([-0.5, L + 0.5], 0, -d - 0.5,\n"
        "                     fc='#aed6f1', alpha=0.5)\n"
        "\n"
        "    # Blok\n"
        "    if r['plovi']:\n"
        "        # Tijelo plovi: gaz d ispod površine, ostatak iznad\n"
        "        ax.add_patch(plt.Rectangle(\n"
        "            (0, -d), L, H,\n"
        "            fc='#8d6e63', ec='#3e2723', lw=2,\n"
        "            label='tijelo'\n"
        "        ))\n"
        "        status = f'PLOVI    gaz d = {d*1000:.0f} mm   '\\\n"
        "                 f'iznad vode = {(H-d)*1000:.0f} mm'\n"
        "        boja_naslov = '#2e7d32'\n"
        "    else:\n"
        "        # Tone: cijeli ispod površine\n"
        "        ax.add_patch(plt.Rectangle(\n"
        "            (0, -H - 0.05), L, H,\n"
        "            fc='#8d6e63', ec='#3e2723', lw=2,\n"
        "            label='tijelo (potonulo)'\n"
        "        ))\n"
        "        status = f'TONE    potrebni gaz d = {d*1000:.0f} mm > H = {H*1000:.0f} mm'\n"
        "        boja_naslov = '#c62828'\n"
        "\n"
        "    # Oznake\n"
        "    if r['plovi']:\n"
        "        # Strelica gaza\n"
        "        ax.annotate('', xy=(L + 0.15, -d), xytext=(L + 0.15, 0),\n"
        "                     arrowprops=dict(arrowstyle='<->', color='#c62828'))\n"
        "        ax.text(L + 0.25, -d/2, f'$d$ = {d*1000:.0f} mm',\n"
        "                 color='#c62828', fontsize=10, va='center')\n"
        "        # Strelica preostale visine\n"
        "        ax.annotate('', xy=(L + 0.15, H - d), xytext=(L + 0.15, 0),\n"
        "                     arrowprops=dict(arrowstyle='<->', color='#2e7d32'))\n"
        "        ax.text(L + 0.25, (H - d)/2,\n"
        "                 f'$H - d$ = {(H-d)*1000:.0f} mm',\n"
        "                 color='#2e7d32', fontsize=10, va='center')\n"
        "\n"
        "    ax.set_xlim(-0.5, L + 1.2)\n"
        "    ax.set_ylim(-max(d + 0.3, H + 0.3), H + 0.3)\n"
        "    ax.set_aspect('equal')\n"
        "    ax.set_xlabel('horizontalna koordinata (m)')\n"
        "    ax.set_ylabel('visina (m)')\n"
        "    ax.set_title(\n"
        "        f'$m$ = {m:.0f} kg,  $\\\\rho_f$ = {rho_f:.0f} kg/m³,  '\n"
        "        f'blok $L\\\\times B\\\\times H$ = '\n"
        "        f'{L}×{B}×{H} m\\n{status}',\n"
        "        color=boja_naslov, fontsize=10\n"
        "    )\n"
        "    ax.grid(ls=':', alpha=0.5)\n"
        "\n"
        "    plt.tight_layout()\n"
        "    plt.show()\n"
        "\n"
        "\n"
        "interact(\n"
        "    gaz_prikaz,\n"
        "    m=FloatSlider(min=50, max=2000, step=20, value=600,\n"
        "                   description='$m$ (kg)',\n"
        "                   layout=Layout(width='420px')),\n"
        "    rho_f=FloatSlider(min=800, max=1200, step=10, value=998,\n"
        "                       description='$\\\\rho_f$ (kg/m³)',\n"
        "                       layout=Layout(width='420px'))\n"
        ");"
    ),
    pitanja=(
        "1. **Slatka i slana voda.** Pri istoj masi, kako se mijenja gaz "
        "kada se isti blok prebaci iz slatke vode ($\\rho = 998$ kg/m³) "
        "u slanu ($\\rho = 1025$ kg/m³)? Zašto brodovi u luci tonu "
        "dublje nego na otvorenom moru?\n"
        "\n"
        "2. **Granica plovnosti.** Pri kojoj masi blok upravo počinje "
        "tonuti u zadanom fluidu? Što ta granica predstavlja u "
        "klasifikaciji broda kao plovila?\n"
        "\n"
        "3. **Nehomogeni fluidi.** Što bi se dogodilo s gazom istoga "
        "tijela ako bi se ono spustilo u ulje gustoće $800$ kg/m³? "
        "Što s glicerinom gustoće $1260$ kg/m³?\n"
        "\n"
        "4. **Praktična procjena.** Drveni splav $L = 4$ m, $B = 2$ m, "
        "$H = 0{,}30$ m s vlastitom masom $300$ kg nosi opremu mase "
        "$200$ kg. Koliki je gaz i kolika je rezerva plovnosti?"
    ),
    teorija=(
        "Ovaj prikaz materijalizira Arhimedov zakon iz poglavlja U07: gaz "
        "plivajućeg tijela proizlazi iz uvjeta da težina istisnutog "
        "fluida bude jednaka težini tijela. Promjena gustoće fluida ili "
        "promjena ukupne mase mijenjaju gaz, ali ne i samu plovnost dok "
        "je $d < H$. U istom poglavlju razmatra se i stabilnost — uvjet "
        "koji zahtijeva da metacentar leži iznad težišta tijela, što "
        "ovaj jednostavni model još ne obuhvaća."
    ),
)


# ---------------------------------------------------------------------------
# U08 — Kontinuitet u suženju cijevi
# ---------------------------------------------------------------------------
NOTEBOOKS["u08_kontinuitet_suzenje"] = dict(
    naslov="Kontinuitet u suženju cijevi",
    poglavlje="Poglavlje U08: Kontrolni volumen i kontinuitet",
    uvod=(
        "Ovaj interaktivni prikaz nadopunjuje jednadžbu kontinuiteta za "
        "nestlačivi fluid u cijevi sa suženjem. Mijenjanjem promjera ulaza "
        "i izlaza te volumenskog protoka prati se promjena brzine "
        "strujanja duž cijevi."
    ),
    cilj=(
        "U cijevi s promjenjivim presjekom volumenski protok ostaje "
        "konstantan duž cijevi, dok se brzina mijenja obrnuto "
        "proporcionalno površini presjeka. Prikaz omogućuje:\n"
        "\n"
        "1. mijenjanje promjera ulaza $D_1$;\n"
        "2. mijenjanje promjera izlaza $D_2$;\n"
        "3. mijenjanje protoka $Q$;\n"
        "4. praćenje brzina $v_1$ i $v_2$ te promjene brzine duž cijevi."
    ),
    pretpostavke=(
        "- nestlačivi fluid (voda);\n"
        "- stacionarno strujanje;\n"
        "- jednodimenzijski profil brzina u svakom presjeku;\n"
        "- bez gubitaka po cijeloj cijevi."
    ),
    model_md=(
        "Iz jednadžbe kontinuiteta za nestlačivi fluid:\n"
        "\n"
        "$$Q = A_1 v_1 = A_2 v_2,$$\n"
        "\n"
        "iz čega slijedi izlazna brzina:\n"
        "\n"
        "$$v_2 = v_1\\,\\frac{A_1}{A_2} = v_1\\left(\\frac{D_1}{D_2}\\right)^2.$$\n"
        "\n"
        "Brzina raste tamo gdje se cijev sužava i pada tamo gdje se širi. "
        "Jednadžba ne ovisi o tlaku ni o energiji — to su posebne teme "
        "narednih poglavlja."
    ),
    kod_funkcije=(
        "def kontinuitet(D1_mm, D2_mm, Q_Lpsek):\n"
        "    D1 = D1_mm / 1000.0\n"
        "    D2 = D2_mm / 1000.0\n"
        "    Q = Q_Lpsek / 1000.0  # m^3/s\n"
        "    A1 = np.pi * D1**2 / 4\n"
        "    A2 = np.pi * D2**2 / 4\n"
        "    v1 = Q / A1\n"
        "    v2 = Q / A2\n"
        "    return {'v1': v1, 'v2': v2, 'A1': A1, 'A2': A2}"
    ),
    prikaz_md=(
        "Klizačima u nastavku biraju se promjeri ulaza i izlaza te "
        "ukupni protok. Gornji prikaz pokazuje presjek cijevi, donji "
        "pokazuje brzinu duž osi cijevi."
    ),
    kod_prikaz=(
        "def kontinuitet_prikaz(D1_mm, D2_mm, Q_Lpsek):\n"
        "    r = kontinuitet(D1_mm, D2_mm, Q_Lpsek)\n"
        "\n"
        "    fig, (ax_geo, ax_v) = plt.subplots(\n"
        "        2, 1, figsize=(9, 6.5),\n"
        "        gridspec_kw={'height_ratios': [1, 1.4]}\n"
        "    )\n"
        "\n"
        "    # Geometrija cijevi (suženje 0.3 do 0.5 m)\n"
        "    x = np.linspace(0, 1.0, 400)\n"
        "    D = np.full_like(x, D1_mm, dtype=float)\n"
        "    maska = (x >= 0.3) & (x < 0.5)\n"
        "    D[maska] = D1_mm + (D2_mm - D1_mm) * (x[maska] - 0.3) / 0.2\n"
        "    D[x >= 0.5] = D2_mm\n"
        "    A = np.pi * (D / 1000)**2 / 4\n"
        "    v = (Q_Lpsek / 1000) / A\n"
        "\n"
        "    # Cijev (presjek)\n"
        "    ax_geo.fill_between(x, -D/2, D/2, color='#aed6f1', alpha=0.7)\n"
        "    ax_geo.plot(x, D/2, color='#1565c0', lw=2)\n"
        "    ax_geo.plot(x, -D/2, color='#1565c0', lw=2)\n"
        "    ax_geo.set_xlim(0, 1.0)\n"
        "    ax_geo.set_ylim(-max(D1_mm, D2_mm)*0.7,\n"
        "                     max(D1_mm, D2_mm)*0.7)\n"
        "    ax_geo.set_ylabel('polumjer (mm)')\n"
        "    ax_geo.set_xticks([])\n"
        "    ax_geo.set_title(\n"
        "        f'$D_1$ = {D1_mm:.0f} mm,  $D_2$ = {D2_mm:.0f} mm,  '\n"
        "        f'$Q$ = {Q_Lpsek:.1f} L/s'\n"
        "    )\n"
        "\n"
        "    # Brzina\n"
        "    ax_v.plot(x, v, color='#c62828', lw=2.2)\n"
        "    ax_v.fill_between(x, 0, v, color='#c62828', alpha=0.2)\n"
        "    ax_v.set_xlabel('osna koordinata (m)')\n"
        "    ax_v.set_ylabel('brzina (m/s)')\n"
        "    ax_v.grid(ls=':', alpha=0.5)\n"
        "    ax_v.axhline(r['v1'], color='gray', ls=':', lw=0.8)\n"
        "    ax_v.text(0.02, r['v1'], f'$v_1$ = {r[\"v1\"]:.2f} m/s',\n"
        "              color='gray', fontsize=9, va='bottom')\n"
        "    ax_v.axhline(r['v2'], color='gray', ls=':', lw=0.8)\n"
        "    ax_v.text(0.98, r['v2'], f'$v_2$ = {r[\"v2\"]:.2f} m/s',\n"
        "              color='gray', fontsize=9, va='bottom', ha='right')\n"
        "\n"
        "    plt.tight_layout()\n"
        "    plt.show()\n"
        "\n"
        "\n"
        "interact(\n"
        "    kontinuitet_prikaz,\n"
        "    D1_mm=FloatSlider(min=30, max=200, step=5, value=100,\n"
        "                       description='$D_1$ (mm)',\n"
        "                       layout=Layout(width='420px')),\n"
        "    D2_mm=FloatSlider(min=10, max=150, step=5, value=40,\n"
        "                       description='$D_2$ (mm)',\n"
        "                       layout=Layout(width='420px')),\n"
        "    Q_Lpsek=FloatSlider(min=0.5, max=30, step=0.5, value=8,\n"
        "                         description='$Q$ (L/s)',\n"
        "                         layout=Layout(width='420px'))\n"
        ");"
    ),
    pitanja=(
        "1. **Skala s omjerom presjeka.** Za $D_2 = D_1 / 2$, koliko je "
        "puta veća izlazna brzina od ulazne? A za $D_2 = D_1 / 4$? Što "
        "je vidljivo iz formule i grafa?\n"
        "\n"
        "2. **Granični slučaj jednakog presjeka.** Pri $D_1 = D_2$, "
        "kakva je raspodjela brzine duž cijevi? Vrijedi li tada još uvijek "
        "jednadžba kontinuiteta?\n"
        "\n"
        "3. **Energetske posljedice.** Iako jednadžba kontinuiteta ne "
        "spominje tlak, povećanje brzine u suženju u idealnom fluidu "
        "neminovno znači pad tlaka. Što kaže Bernoullijeva jednadžba o "
        "tome (poglavlje U09)?\n"
        "\n"
        "4. **Stvarni profil brzina.** Zašto u stvarnoj cijevi profil "
        "brzina nije jednolik nego približno parabolan (laminarno) ili "
        "polako-jednolik (turbulentno)? Što to znači za točnost "
        "predviđanja $v_2$ iz ovog modela?"
    ),
    teorija=(
        "Ovaj prikaz materijalizira jednadžbu kontinuiteta iz poglavlja "
        "U08 — najjednostavniji oblik bilance mase za nestlačivi fluid "
        "u jednoj cijevi. Ista logika proširuje se na čvorove (zbroj "
        "ulaznih protoka jednak zbroju izlaznih) i na spremnike s "
        "akumulacijom (razlika ulaza i izlaza jednaka brzini promjene "
        "volumena). U poglavlju U09 se na ovu osnovu dodaje energetska "
        "bilanca preko Bernoullija."
    ),
)


# ---------------------------------------------------------------------------
# U10 — Moodyjev dijagram
# ---------------------------------------------------------------------------
NOTEBOOKS["u10_moody_dijagram"] = dict(
    naslov="Moodyjev dijagram — koeficijent trenja",
    poglavlje="Poglavlje U10: Realni Bernoulli i gubici",
    uvod=(
        "Ovaj interaktivni prikaz nadopunjuje rad s Moodyjevim "
        "dijagramom u poglavlju U10. Mijenjanjem Reynoldsovog broja i "
        "relativne hrapavosti cijevi prati se pripadni koeficijent "
        "trenja $\\lambda$ na klasičnom dijagramu."
    ),
    cilj=(
        "Koeficijent trenja $\\lambda$ ovisi o Reynoldsovom broju i "
        "relativnoj hrapavosti cijevi $\\varepsilon/D$. Moodyjev dijagram "
        "objedinjuje laminarno područje, prijelaz, gladke cijevi i "
        "potpuno hrapavo turbulentno područje na jednom prikazu. Prikaz "
        "omogućuje:\n"
        "\n"
        "1. mijenjanje Reynoldsovog broja $Re$;\n"
        "2. mijenjanje relativne hrapavosti $\\varepsilon/D$;\n"
        "3. praćenje pripadnog $\\lambda$ i režima strujanja."
    ),
    pretpostavke=(
        "- razvijeno strujanje u kružnoj cijevi konstantnog presjeka;\n"
        "- jednolika hrapavost stijenke;\n"
        "- za turbulentno područje koristi se Swamee-Jainova "
        "eksplicitna aproksimacija Colebrook-Whiteove jednadžbe;\n"
        "- za laminarno područje vrijedi egzaktna relacija "
        "$\\lambda = 64/Re$."
    ),
    model_md=(
        "U laminarnom području ($Re < 2300$):\n"
        "\n"
        "$$\\lambda = \\frac{64}{Re}.$$\n"
        "\n"
        "U turbulentnom području ($Re > 4000$) Swamee-Jainova aproksimacija "
        "Colebrook-Whiteove jednadžbe:\n"
        "\n"
        "$$\\lambda = \\frac{0{,}25}"
        "{\\left[\\log_{10}\\!\\left("
        "\\dfrac{\\varepsilon/D}{3{,}7} + \\dfrac{5{,}74}{Re^{0{,}9}}\\right)\\right]^2}.$$\n"
        "\n"
        "U prijelaznom području ($2300 < Re < 4000$) ponašanje strujanja "
        "je nestabilno i $\\lambda$ se obično interpolira ili se područje "
        "izbjegava u projektiranju."
    ),
    kod_funkcije=(
        "def lambda_trenja(Re, eps_D):\n"
        "    if Re < 2300:\n"
        "        return 64 / Re, 'laminarno'\n"
        "    elif Re < 4000:\n"
        "        # Interpolacija za prijelazno područje\n"
        "        lam_lam = 64 / 2300\n"
        "        lam_turb = 0.25 / (np.log10(eps_D/3.7 + 5.74/4000**0.9))**2\n"
        "        t = (Re - 2300) / (4000 - 2300)\n"
        "        return lam_lam * (1 - t) + lam_turb * t, 'prijelazno'\n"
        "    else:\n"
        "        lam = 0.25 / (np.log10(eps_D/3.7 + 5.74/Re**0.9))**2\n"
        "        return lam, 'turbulentno'"
    ),
    prikaz_md=(
        "Klizačima u nastavku biraju se Reynoldsov broj i relativna "
        "hrapavost. Prikaz je Moodyjev dijagram u logaritamskim "
        "koordinatama s istaknutom točkom koja odgovara odabranim "
        "vrijednostima."
    ),
    kod_prikaz=(
        "def moody_prikaz(log_Re, eps_D):\n"
        "    Re = 10**log_Re\n"
        "    lam, rezim = lambda_trenja(Re, eps_D)\n"
        "\n"
        "    fig, ax = plt.subplots(figsize=(10, 6))\n"
        "\n"
        "    # Laminarna linija\n"
        "    Re_lam = np.logspace(2.5, np.log10(2300), 50)\n"
        "    ax.loglog(Re_lam, 64/Re_lam, color='#1565c0', lw=2,\n"
        "              label='laminarno  $\\\\lambda = 64/Re$')\n"
        "\n"
        "    # Turbulentne krivulje za nekoliko ε/D\n"
        "    eps_D_niz = [1e-6, 1e-5, 1e-4, 5e-4, 1e-3, 5e-3, 1e-2, 5e-2]\n"
        "    Re_turb = np.logspace(np.log10(4000), 8, 100)\n"
        "    for e in eps_D_niz:\n"
        "        lam_kr = 0.25 / (np.log10(e/3.7 + 5.74/Re_turb**0.9))**2\n"
        "        ax.loglog(Re_turb, lam_kr, color='#888', lw=0.8, alpha=0.6)\n"
        "        ax.text(Re_turb[-1] * 1.1, lam_kr[-1], f'{e:.0e}',\n"
        "                 fontsize=8, color='#666', va='center')\n"
        "\n"
        "    # Krivulja za odabrani ε/D\n"
        "    lam_odab = 0.25 / (np.log10(eps_D/3.7 + 5.74/Re_turb**0.9))**2\n"
        "    ax.loglog(Re_turb, lam_odab, color='#2e7d32', lw=2.2,\n"
        "              label=f'odabrano $\\\\varepsilon/D$ = {eps_D:.1e}')\n"
        "\n"
        "    # Prijelazno područje\n"
        "    ax.axvspan(2300, 4000, color='#fff3e0', alpha=0.5)\n"
        "    ax.text(3000, 0.005, 'prijelazno', rotation=90, fontsize=9,\n"
        "             ha='center', color='#e65100')\n"
        "\n"
        "    # Točka\n"
        "    ax.scatter([Re], [lam], color='#c62828', s=140,\n"
        "                zorder=5, marker='o',\n"
        "                label=f'$Re$ = {Re:.1e},  $\\\\lambda$ = {lam:.4f}')\n"
        "    ax.annotate(f'  {rezim}', xy=(Re, lam),\n"
        "                 fontsize=10, color='#c62828', va='center')\n"
        "\n"
        "    ax.set_xlabel('Reynoldsov broj  $Re$')\n"
        "    ax.set_ylabel('koeficijent trenja  $\\\\lambda$')\n"
        "    ax.set_xlim(500, 1e8)\n"
        "    ax.set_ylim(0.005, 0.1)\n"
        "    ax.grid(which='both', ls=':', alpha=0.5)\n"
        "    ax.legend(loc='upper right', fontsize=9)\n"
        "    ax.set_title(f'Moodyjev dijagram   |   režim: {rezim}',\n"
        "                  fontsize=11)\n"
        "\n"
        "    plt.tight_layout()\n"
        "    plt.show()\n"
        "\n"
        "\n"
        "interact(\n"
        "    moody_prikaz,\n"
        "    log_Re=FloatSlider(min=2.5, max=8, step=0.1, value=5,\n"
        "                        description='log$_{10}$ Re',\n"
        "                        readout_format='.2f',\n"
        "                        layout=Layout(width='420px')),\n"
        "    eps_D=FloatSlider(min=1e-6, max=5e-2, step=1e-5, value=1e-4,\n"
        "                       description='$\\\\varepsilon/D$',\n"
        "                       readout_format='.1e',\n"
        "                       layout=Layout(width='420px'))\n"
        ");"
    ),
    pitanja=(
        "1. **Potpuno hrapavo područje.** Pri visokim Reynoldsovim "
        "brojevima krivulje $\\lambda(Re)$ za zadanu hrapavost prelaze "
        "u horizontalne pravce. U kojem trenutku $Re$ više ne utječe na "
        "$\\lambda$? Što to fizikalno znači?\n"
        "\n"
        "2. **Hidraulički gladke cijevi.** Za vrlo malu hrapavost "
        "$\\varepsilon/D < 10^{-5}$, kako se $\\lambda$ ponaša s "
        "porastom $Re$ u turbulentnom području? Zašto se cijevi te "
        "klase nazivaju 'hidraulički gladke'?\n"
        "\n"
        "3. **Prijelazno područje.** U području $2300 < Re < 4000$ "
        "$\\lambda$ je teško predvidljiv. Zašto se u inženjerskoj praksi "
        "izbjegava projektirati radne točke u tom području?\n"
        "\n"
        "4. **Inverzni zadatak.** Za $\\lambda \\approx 0{,}025$, koje "
        "kombinacije $Re$ i $\\varepsilon/D$ ga daju? Postoji li više "
        "rješenja i što govore o različitim radnim režimima cijevi?"
    ),
    teorija=(
        "Ovaj prikaz materijalizira Moodyjev dijagram iz poglavlja U10 — "
        "klasično grafičko rješenje Colebrook-Whiteove jednadžbe koje "
        "objedinjuje sve režime strujanja u cijevi. Iako se danas "
        "$\\lambda$ često računa eksplicitnim aproksimacijama "
        "(Swamee-Jain, Haaland), Moodyjev dijagram ostaje neprocjenjiv "
        "kao alat za razumijevanje međusobne ovisnosti hrapavosti, "
        "Reynoldsovog broja i koeficijenta trenja."
    ),
)


# ---------------------------------------------------------------------------
# U11 — Sila na koljeno
# ---------------------------------------------------------------------------
NOTEBOOKS["u11_sila_na_koljeno"] = dict(
    naslov="Sila na koljeno — promjena smjera strujanja",
    poglavlje="Poglavlje U11: Količina gibanja i sile strujanja",
    uvod=(
        "Ovaj interaktivni prikaz nadopunjuje izvod sile fluida na "
        "horizontalno koljeno. Mijenjanjem kuta zakretanja, protoka i "
        "promjera cijevi prati se vektorska sila koju nosač mora "
        "preuzeti."
    ),
    cilj=(
        "Kada fluid u koljenu mijenja smjer, na konstrukciju djeluje "
        "sila koja proizlazi iz promjene količine gibanja i iz tlakova "
        "na ulaznom i izlaznom presjeku. Prikaz omogućuje:\n"
        "\n"
        "1. mijenjanje kuta zakretanja koljena $\\beta$;\n"
        "2. mijenjanje volumenskog protoka $Q$;\n"
        "3. mijenjanje promjera cijevi $D$ (isti na ulazu i izlazu);\n"
        "4. praćenje komponenti sile $F_x$, $F_y$ i ukupne rezultante."
    ),
    pretpostavke=(
        "- horizontalno koljeno (težina fluida zanemarena);\n"
        "- isti promjer cijevi na ulazu i izlazu ($D_1 = D_2 = D$);\n"
        "- jednodimenzijski profil brzina u presjecima;\n"
        "- jednak manometarski tlak na ulazu i izlazu ($p_1 = p_2 = p$);\n"
        "- voda gustoće $\\rho = 998$ kg/m³."
    ),
    model_md=(
        "Iz jednadžbe količine gibanja primijenjene na kontrolni volumen "
        "koji obuhvaća cijelo koljeno, ulazna strana u smjeru osi $x$ i "
        "izlazna strana pod kutem $\\beta$ od osi $x$:\n"
        "\n"
        "$$F_x = (\\rho Q v + p A)(1 - \\cos\\beta),$$\n"
        "$$F_y = (\\rho Q v + p A)\\sin\\beta,$$\n"
        "\n"
        "gdje je $v = Q/A$. Iznos rezultante i kut prema osi $x$:\n"
        "\n"
        "$$F_R = \\sqrt{F_x^2 + F_y^2}, \\qquad "
        "\\tan\\varphi = \\frac{F_y}{F_x}.$$\n"
        "\n"
        "Ovo je sila fluida na koljeno; nosač mora preuzeti jednaku silu "
        "suprotnog smjera."
    ),
    kod_funkcije=(
        "RHO = 998.0\n"
        "P_REL = 200_000.0  # manometarski tlak (Pa)\n"
        "\n"
        "def koljeno(beta_deg, Q_Lpsek, D_mm):\n"
        "    beta = np.radians(beta_deg)\n"
        "    D = D_mm / 1000.0\n"
        "    Q = Q_Lpsek / 1000.0  # m^3/s\n"
        "    A = np.pi * D**2 / 4\n"
        "    v = Q / A\n"
        "    F_inten = RHO * Q * v + P_REL * A\n"
        "    F_x = F_inten * (1 - np.cos(beta))\n"
        "    F_y = F_inten * np.sin(beta)\n"
        "    F_R = np.sqrt(F_x**2 + F_y**2)\n"
        "    phi = np.degrees(np.arctan2(F_y, F_x))\n"
        "    return {'F_x': F_x, 'F_y': F_y, 'F_R': F_R, 'phi': phi,\n"
        "             'v': v, 'F_inten': F_inten}"
    ),
    prikaz_md=(
        "Klizačima u nastavku biraju se kut zakretanja, protok i "
        "promjer cijevi. Prikaz pokazuje shemu koljena u "
        "horizontalnoj ravnini s vektorima brzina ulaza i izlaza te "
        "rezultantnom silom na konstrukciju."
    ),
    kod_prikaz=(
        "def koljeno_prikaz(beta_deg, Q_Lpsek, D_mm):\n"
        "    r = koljeno(beta_deg, Q_Lpsek, D_mm)\n"
        "    beta = np.radians(beta_deg)\n"
        "\n"
        "    fig, ax = plt.subplots(figsize=(8, 7))\n"
        "\n"
        "    # Ulazna cijev (po osi x prema točki 0,0)\n"
        "    L_cijevi = 0.8\n"
        "    polumjer = D_mm / 2000.0  # za prikaz\n"
        "    ax.plot([-L_cijevi, 0], [polumjer, polumjer],\n"
        "             color='#1565c0', lw=2)\n"
        "    ax.plot([-L_cijevi, 0], [-polumjer, -polumjer],\n"
        "             color='#1565c0', lw=2)\n"
        "\n"
        "    # Izlazna cijev (pod kutem beta od osi x)\n"
        "    x_kraj = L_cijevi * np.cos(beta)\n"
        "    y_kraj = L_cijevi * np.sin(beta)\n"
        "    # Perpendikularne offsete\n"
        "    dx = -polumjer * np.sin(beta)\n"
        "    dy = polumjer * np.cos(beta)\n"
        "    ax.plot([0 + dx, x_kraj + dx], [0 + dy, y_kraj + dy],\n"
        "             color='#1565c0', lw=2)\n"
        "    ax.plot([0 - dx, x_kraj - dx], [0 - dy, y_kraj - dy],\n"
        "             color='#1565c0', lw=2)\n"
        "\n"
        "    # Spojni dio koljena\n"
        "    theta_spoj = np.linspace(np.pi/2, np.pi/2 - beta + np.pi, 30)\n"
        "    ax.fill_between([], [], [])\n"
        "\n"
        "    # Strelica ulazne brzine\n"
        "    ax.annotate('', xy=(0, 0), xytext=(-0.5, 0),\n"
        "                 arrowprops=dict(arrowstyle='->',\n"
        "                                   color='#1565c0', lw=3))\n"
        "    ax.text(-0.55, 0.08, f'$v_1$ = {r[\"v\"]:.2f} m/s',\n"
        "             color='#1565c0', fontsize=10)\n"
        "\n"
        "    # Strelica izlazne brzine\n"
        "    ax.annotate('', xy=(0.5*np.cos(beta), 0.5*np.sin(beta)),\n"
        "                 xytext=(0, 0),\n"
        "                 arrowprops=dict(arrowstyle='->',\n"
        "                                   color='#1565c0', lw=3))\n"
        "    ax.text(0.55*np.cos(beta) + 0.05, 0.55*np.sin(beta),\n"
        "             f'$v_2$ = {r[\"v\"]:.2f} m/s',\n"
        "             color='#1565c0', fontsize=10)\n"
        "\n"
        "    # Vektor rezultante sile (skala)\n"
        "    skala = 0.6 / max(r['F_R'], 1)\n"
        "    Lx = r['F_x'] * skala\n"
        "    Ly = r['F_y'] * skala\n"
        "    ax.annotate('', xy=(Lx, Ly), xytext=(0, 0),\n"
        "                 arrowprops=dict(arrowstyle='->',\n"
        "                                   color='#c62828', lw=3))\n"
        "    ax.text(Lx + 0.05, Ly + 0.05,\n"
        "             f'$F_R$ = {r[\"F_R\"]/1000:.2f} kN\\n'\n"
        "             f'$\\\\varphi$ = {r[\"phi\"]:.1f}°',\n"
        "             color='#c62828', fontsize=11)\n"
        "\n"
        "    # Os x i y\n"
        "    ax.axhline(0, color='gray', lw=0.5, alpha=0.5)\n"
        "    ax.axvline(0, color='gray', lw=0.5, alpha=0.5)\n"
        "    ax.text(1.3, -0.05, 'x', color='gray', fontsize=10)\n"
        "    ax.text(-0.05, 1.3, 'y', color='gray', fontsize=10)\n"
        "\n"
        "    ax.set_xlim(-1.0, 1.5)\n"
        "    ax.set_ylim(-0.5, 1.5)\n"
        "    ax.set_aspect('equal')\n"
        "    ax.set_title(\n"
        "        f'$\\\\beta$ = {beta_deg:.0f}°,  '\n"
        "        f'$Q$ = {Q_Lpsek:.1f} L/s,  $D$ = {D_mm:.0f} mm\\n'\n"
        "        f'$F_x$ = {r[\"F_x\"]/1000:.2f} kN,  '\n"
        "        f'$F_y$ = {r[\"F_y\"]/1000:.2f} kN'\n"
        "    )\n"
        "    ax.grid(ls=':', alpha=0.5)\n"
        "\n"
        "    plt.tight_layout()\n"
        "    plt.show()\n"
        "\n"
        "\n"
        "interact(\n"
        "    koljeno_prikaz,\n"
        "    beta_deg=FloatSlider(min=15, max=170, step=5, value=90,\n"
        "                          description='$\\\\beta$ (°)',\n"
        "                          layout=Layout(width='420px')),\n"
        "    Q_Lpsek=FloatSlider(min=1, max=50, step=1, value=20,\n"
        "                         description='$Q$ (L/s)',\n"
        "                         layout=Layout(width='420px')),\n"
        "    D_mm=FloatSlider(min=50, max=250, step=10, value=120,\n"
        "                      description='$D$ (mm)',\n"
        "                      layout=Layout(width='420px'))\n"
        ");"
    ),
    pitanja=(
        "1. **Pravokutno koljeno.** Pri $\\beta = 90°$, koje su "
        "vrijednosti $F_x$ i $F_y$? Pod kojim kutom djeluje rezultanta i "
        "kako mora biti orijentiran nosač?\n"
        "\n"
        "2. **Potpuni U-okret.** Pri $\\beta \\to 180°$, što se događa s "
        "$F_x$ i $F_y$? Zašto je to najveća moguća sila pri zadanom $Q$ "
        "i $D$?\n"
        "\n"
        "3. **Tlakni i impulsni doprinos.** Provjeri za nekoliko "
        "kombinacija parametara koliki je relativni udjel "
        "$\\rho Q v$ (impulsno) prema $p A$ (tlačno) u ukupnom članu "
        "$F_{int}$. Kada dominira impulsni dio, a kada tlačni?\n"
        "\n"
        "4. **Skala s promjerom.** Pri konstantnom $Q$, kako $D$ utječe "
        "na ukupnu silu? Postoji li promjer pri kojem je sila minimalna?"
    ),
    teorija=(
        "Ovaj prikaz materijalizira primjenu zakona količine gibanja iz "
        "poglavlja U11 na klasičnom inženjerskom problemu — sili na "
        "koljeno cjevovoda. Promjena smjera strujanja stvara silu na "
        "konstrukciju neovisno o gubicima u zavoju. U realnim sustavima "
        "gubici (poglavlje U10) doprinose razlici tlakova između ulaza "
        "i izlaza koljena, ali osnovna struktura sile ostaje ista."
    ),
)


# ---------------------------------------------------------------------------
# U12 — Trokuti brzina za Peltonovu lopaticu
# ---------------------------------------------------------------------------
NOTEBOOKS["u12_pelton_lopatica"] = dict(
    naslov="Trokuti brzina i snaga na Peltonovoj lopatici",
    poglavlje="Poglavlje U12: Pokretne lopatice i potisak",
    uvod=(
        "Ovaj interaktivni prikaz nadopunjuje izvod sile i snage na "
        "Peltonovoj lopatici. Mijenjanjem apsolutne brzine mlaza, "
        "obodne brzine lopatice i izlaznog kuta prati se snaga koju "
        "rotor prima."
    ),
    cilj=(
        "Na Peltonovoj lopatici relativna brzina mlaza ulazi pod određenim "
        "kutem, mijenja smjer i izlazi tako da fluid predaje rotoru "
        "tangencijalnu količinu gibanja. Prikaz omogućuje:\n"
        "\n"
        "1. mijenjanje apsolutne brzine mlaza $c_1$;\n"
        "2. mijenjanje obodne brzine lopatice $u$;\n"
        "3. mijenjanje izlaznog kuta $\\beta_2$;\n"
        "4. praćenje snage $P$ i njezine ovisnosti o obodnoj brzini."
    ),
    pretpostavke=(
        "- jedna reprezentativna lopatica (pojednostavljeni model);\n"
        "- mlaz dolazi paralelno s osi obodne brzine;\n"
        "- bez gubitaka u lopatici ($|w_2| = |w_1|$);\n"
        "- voda gustoće $\\rho = 998$ kg/m³, protok mlaza $Q = 0{,}05$ m³/s "
        "(pretpostavljen)."
    ),
    model_md=(
        "Relativna brzina na ulazu (mlaz minus lopatica):\n"
        "\n"
        "$$w_1 = c_1 - u.$$\n"
        "\n"
        "Bez gubitaka u lopatici, iznos relativne brzine zadržava se "
        "($|w_2| = w_1$), ali smjer se mijenja prema izlaznom kutu "
        "$\\beta_2$ (mjereno od smjera ulaznog $w_1$). Tangencijalna sila "
        "na rotor:\n"
        "\n"
        "$$F_t = \\rho Q\\,w_1\\,(1 - \\cos\\beta_2).$$\n"
        "\n"
        "Snaga predana rotoru (sila puta obodna brzina):\n"
        "\n"
        "$$P = F_t \\cdot u = \\rho Q\\,(c_1 - u)\\,u\\,(1 - \\cos\\beta_2).$$\n"
        "\n"
        "Maksimalna snaga uz idealni $\\beta_2 = 180°$ postiže se za "
        "$u = c_1/2$."
    ),
    kod_funkcije=(
        "RHO = 998.0\n"
        "Q = 0.05  # m^3/s\n"
        "\n"
        "def pelton(c1, u, beta2_deg):\n"
        "    beta2 = np.radians(beta2_deg)\n"
        "    w1 = c1 - u\n"
        "    F_t = RHO * Q * w1 * (1 - np.cos(beta2))\n"
        "    P = F_t * u\n"
        "    P_max_idealno = RHO * Q * c1**2 / 2  # pri u = c1/2, beta=180\n"
        "    eta = P / P_max_idealno if P_max_idealno > 0 else 0\n"
        "    return {'w1': w1, 'F_t': F_t, 'P': P, 'eta': eta}"
    ),
    prikaz_md=(
        "Klizačima u nastavku biraju se apsolutna brzina mlaza, obodna "
        "brzina lopatice i izlazni kut. Lijevi prikaz pokazuje trokute "
        "brzina, desni krivulju snage u ovisnosti o obodnoj brzini s "
        "istaknutom radnom točkom."
    ),
    kod_prikaz=(
        "def pelton_prikaz(c1, u, beta2_deg):\n"
        "    r = pelton(c1, u, beta2_deg)\n"
        "    beta2 = np.radians(beta2_deg)\n"
        "\n"
        "    fig, (ax_tr, ax_P) = plt.subplots(1, 2, figsize=(11, 5))\n"
        "\n"
        "    # Trokut brzina na ulazu\n"
        "    ax_tr.annotate('', xy=(c1, 0), xytext=(0, 0),\n"
        "                    arrowprops=dict(arrowstyle='->',\n"
        "                                      color='#c62828', lw=2.2))\n"
        "    ax_tr.text(c1/2, -3, f'$c_1$ = {c1:.1f} m/s',\n"
        "                color='#c62828', ha='center', fontsize=10)\n"
        "    ax_tr.annotate('', xy=(u, 0), xytext=(0, 0),\n"
        "                    arrowprops=dict(arrowstyle='->',\n"
        "                                      color='#1565c0', lw=2.2))\n"
        "    ax_tr.text(u/2, 1.5, f'$u$ = {u:.1f} m/s',\n"
        "                color='#1565c0', ha='center', fontsize=10)\n"
        "    ax_tr.annotate('', xy=(c1, 0), xytext=(u, 0),\n"
        "                    arrowprops=dict(arrowstyle='->',\n"
        "                                      color='#2e7d32', lw=2.2))\n"
        "    ax_tr.text((c1 + u)/2, 3, f'$w_1$ = {r[\"w1\"]:.1f} m/s',\n"
        "                color='#2e7d32', ha='center', fontsize=10)\n"
        "\n"
        "    ax_tr.set_xlim(-2, max(c1, 1) + 2)\n"
        "    ax_tr.set_ylim(-8, 8)\n"
        "    ax_tr.set_xlabel('brzina (m/s)')\n"
        "    ax_tr.set_title('Trokut brzina na ulazu  '\n"
        "                     '$\\\\vec{c}_1 = \\\\vec{u} + \\\\vec{w}_1$')\n"
        "    ax_tr.set_aspect('equal')\n"
        "    ax_tr.grid(ls=':', alpha=0.5)\n"
        "    ax_tr.axhline(0, color='gray', lw=0.5)\n"
        "\n"
        "    # Krivulja P(u) za zadani c1 i beta2\n"
        "    u_niz = np.linspace(0, c1, 100)\n"
        "    P_niz = RHO * Q * (c1 - u_niz) * u_niz * (1 - np.cos(beta2))\n"
        "    ax_P.plot(u_niz, P_niz/1000, color='#1565c0', lw=2.2)\n"
        "    ax_P.scatter([u], [r['P']/1000], color='#c62828',\n"
        "                  s=140, zorder=5)\n"
        "    ax_P.axvline(c1/2, color='gray', ls=':', lw=0.8)\n"
        "    ax_P.text(c1/2, max(P_niz)*1.05/1000,\n"
        "               '$u = c_1/2$  (optimum)', color='gray', fontsize=9,\n"
        "               ha='center')\n"
        "    ax_P.set_xlabel('obodna brzina  $u$ (m/s)')\n"
        "    ax_P.set_ylabel('snaga  $P$ (kW)')\n"
        "    ax_P.set_title(\n"
        "        f'$\\\\beta_2$ = {beta2_deg:.0f}°,  '\n"
        "        f'$P$ = {r[\"P\"]/1000:.2f} kW,  '\n"
        "        f'$\\\\eta$ = {r[\"eta\"]*100:.0f}%'\n"
        "    )\n"
        "    ax_P.grid(ls=':', alpha=0.5)\n"
        "\n"
        "    plt.tight_layout()\n"
        "    plt.show()\n"
        "\n"
        "\n"
        "interact(\n"
        "    pelton_prikaz,\n"
        "    c1=FloatSlider(min=10, max=80, step=2, value=40,\n"
        "                    description='$c_1$ (m/s)',\n"
        "                    layout=Layout(width='420px')),\n"
        "    u=FloatSlider(min=0, max=80, step=1, value=20,\n"
        "                   description='$u$ (m/s)',\n"
        "                   layout=Layout(width='420px')),\n"
        "    beta2_deg=FloatSlider(min=90, max=180, step=2, value=170,\n"
        "                           description='$\\\\beta_2$ (°)',\n"
        "                           layout=Layout(width='420px'))\n"
        ");"
    ),
    pitanja=(
        "1. **Optimalna obodna brzina.** Provjeri grafom da maksimum "
        "snage pada točno na $u = c_1/2$ neovisno o izlaznom kutu. "
        "Zašto upravo polovica brzine mlaza, a ne nula ili $c_1$?\n"
        "\n"
        "2. **Granica $\\beta_2 = 180°$.** Pri potpunom U-okretu (mlaz "
        "se vraća unatrag), kakva je teorijska maksimalna snaga? Zašto "
        "stvarne lopatice imaju $\\beta_2 \\approx 165°$, a ne $180°$?\n"
        "\n"
        "3. **Lopatica u mirovanju.** Pri $u = 0$ (lopatica miruje), "
        "kolika je snaga predana rotoru? Zašto, iako sila na lopaticu "
        "postoji?\n"
        "\n"
        "4. **Tehnička procjena.** Za malu hidroelektranu s mlazem "
        "$c_1 = 50$ m/s i protokom $Q = 0{,}05$ m³/s, kolika je "
        "teorijska maksimalna snaga? Što ograničava stvarni iznos?"
    ),
    teorija=(
        "Ovaj prikaz materijalizira trokute brzina i radni princip "
        "Peltonove turbine iz poglavlja U12. Razdvajanje apsolutne i "
        "relativne brzine, te izlazni kut lopatice, izravno određuju "
        "snagu predanu rotoru. Ista logika prevodi se na sve "
        "akcijske turbine i pumpe — razlika je samo u smjeru prijenosa "
        "energije."
    ),
)


# ---------------------------------------------------------------------------
# U13 — Paralelne grane cjevovoda
# ---------------------------------------------------------------------------
NOTEBOOKS["u13_paralelne_grane"] = dict(
    naslov="Paralelne grane cjevovoda — raspodjela protoka",
    poglavlje="Poglavlje U13: Cjevovodi",
    uvod=(
        "Ovaj interaktivni prikaz nadopunjuje rad s paralelnim spojem "
        "cijevi. Mijenjanjem geometrije dvije grane i ukupnog protoka "
        "prati se kako se taj protok dijeli između grana uz uvjet "
        "jednakog pada ukupne energije."
    ),
    cilj=(
        "U paralelnom spoju dvije ili više cijevi između istih čvorova, "
        "raspodjela protoka po granama nije slobodna nego je određena "
        "uvjetom da svaka grana 'plati' isti pad energije. Prikaz "
        "omogućuje:\n"
        "\n"
        "1. mijenjanje duljine i promjera grane 1;\n"
        "2. mijenjanje duljine i promjera grane 2;\n"
        "3. mijenjanje ukupnog protoka $Q$;\n"
        "4. praćenje raspodjele $Q_1, Q_2$ i pripadnog gubitka "
        "energije."
    ),
    pretpostavke=(
        "- razvijeno turbulentno strujanje u obje grane;\n"
        "- konstantni koeficijent trenja $\\lambda = 0{,}025$ za obje "
        "grane (uprošćeno);\n"
        "- bez lokalnih gubitaka osim onih koje uključuje $\\lambda$;\n"
        "- voda kao radni fluid;\n"
        "- grane povezuju iste ulazne i izlazne čvorove."
    ),
    model_md=(
        "Gubitak energije u svakoj grani:\n"
        "\n"
        "$$h_{w,i} = \\lambda\\,\\frac{L_i}{D_i}\\,\\frac{v_i^2}{2g} = "
        "k_i\\,Q_i^2, \\quad "
        "k_i = \\frac{8\\lambda L_i}{\\pi^2 g D_i^5}.$$\n"
        "\n"
        "Uvjet paralelnog spoja: jednak pad energije u obje grane:\n"
        "\n"
        "$$k_1 Q_1^2 = k_2 Q_2^2 \\quad \\Rightarrow \\quad "
        "\\frac{Q_1}{Q_2} = \\sqrt{\\frac{k_2}{k_1}}.$$\n"
        "\n"
        "Uz uvjet $Q_1 + Q_2 = Q$, raspodjela se može zatvoriti analitički."
    ),
    kod_funkcije=(
        "G = 9.81\n"
        "LAMBDA = 0.025\n"
        "\n"
        "def k_grane(L, D_mm):\n"
        "    D = D_mm / 1000.0\n"
        "    return 8 * LAMBDA * L / (np.pi**2 * G * D**5)\n"
        "\n"
        "def paralelne(L1, D1_mm, L2, D2_mm, Q_Lpsek):\n"
        "    Q = Q_Lpsek / 1000.0  # m^3/s\n"
        "    k1 = k_grane(L1, D1_mm)\n"
        "    k2 = k_grane(L2, D2_mm)\n"
        "    # Q1/Q2 = sqrt(k2/k1), Q1+Q2=Q\n"
        "    omjer = np.sqrt(k2 / k1)\n"
        "    Q2 = Q / (1 + omjer)\n"
        "    Q1 = Q - Q2\n"
        "    h_w = k1 * Q1**2\n"
        "    return {'Q1': Q1, 'Q2': Q2, 'h_w': h_w,\n"
        "             'udio1': Q1/Q, 'udio2': Q2/Q}"
    ),
    prikaz_md=(
        "Klizačima u nastavku biraju se duljine i promjeri obje grane "
        "te ukupni protok. Prikaz pokazuje shemu paralelnog spoja s "
        "pripadnom raspodjelom protoka."
    ),
    kod_prikaz=(
        "def paralelne_prikaz(L1, D1_mm, L2, D2_mm, Q_Lpsek):\n"
        "    r = paralelne(L1, D1_mm, L2, D2_mm, Q_Lpsek)\n"
        "\n"
        "    fig, ax = plt.subplots(figsize=(10, 5.5))\n"
        "\n"
        "    # Ulazni čvor (lijevo) i izlazni (desno)\n"
        "    x_lijevo, x_desno = 0, 8\n"
        "    y_grana1, y_grana2 = 1.5, -1.5\n"
        "\n"
        "    # Ulazna i izlazna cijev\n"
        "    ax.plot([-1.5, x_lijevo], [0, 0], color='#1565c0', lw=3)\n"
        "    ax.plot([x_desno, x_desno + 1.5], [0, 0], color='#1565c0', lw=3)\n"
        "\n"
        "    # Grane (debljina linije ovisi o D)\n"
        "    debljina1 = max(1.5, D1_mm / 30)\n"
        "    debljina2 = max(1.5, D2_mm / 30)\n"
        "    ax.plot([x_lijevo, x_lijevo, x_desno, x_desno],\n"
        "             [0, y_grana1, y_grana1, 0],\n"
        "             color='#2e7d32', lw=debljina1, label='grana 1')\n"
        "    ax.plot([x_lijevo, x_lijevo, x_desno, x_desno],\n"
        "             [0, y_grana2, y_grana2, 0],\n"
        "             color='#c62828', lw=debljina2, label='grana 2')\n"
        "\n"
        "    # Oznake protoka i geometrije\n"
        "    ax.text(x_desno/2, y_grana1 + 0.4,\n"
        "             f'$L_1$ = {L1:.0f} m,  $D_1$ = {D1_mm:.0f} mm\\n'\n"
        "             f'$Q_1$ = {r[\"Q1\"]*1000:.2f} L/s  ({r[\"udio1\"]*100:.0f}%)',\n"
        "             ha='center', color='#2e7d32', fontsize=10)\n"
        "    ax.text(x_desno/2, y_grana2 - 0.4,\n"
        "             f'$L_2$ = {L2:.0f} m,  $D_2$ = {D2_mm:.0f} mm\\n'\n"
        "             f'$Q_2$ = {r[\"Q2\"]*1000:.2f} L/s  ({r[\"udio2\"]*100:.0f}%)',\n"
        "             ha='center', color='#c62828', fontsize=10, va='top')\n"
        "\n"
        "    # Strelice protoka\n"
        "    ax.annotate('', xy=(-0.5, 0), xytext=(-1.2, 0),\n"
        "                 arrowprops=dict(arrowstyle='->',\n"
        "                                   color='#1565c0', lw=2))\n"
        "    ax.text(-1.4, 0.3, f'$Q$ = {Q_Lpsek:.1f} L/s',\n"
        "             color='#1565c0', fontsize=10)\n"
        "\n"
        "    ax.set_xlim(-2, x_desno + 2)\n"
        "    ax.set_ylim(-3, 3)\n"
        "    ax.set_aspect('equal')\n"
        "    ax.set_title(f'Pad energije u obje grane:  '\n"
        "                  f'$h_w$ = {r[\"h_w\"]:.3f} m')\n"
        "    ax.axis('off')\n"
        "\n"
        "    plt.tight_layout()\n"
        "    plt.show()\n"
        "\n"
        "\n"
        "interact(\n"
        "    paralelne_prikaz,\n"
        "    L1=FloatSlider(min=10, max=200, step=5, value=80,\n"
        "                    description='$L_1$ (m)',\n"
        "                    layout=Layout(width='420px')),\n"
        "    D1_mm=FloatSlider(min=20, max=200, step=5, value=80,\n"
        "                       description='$D_1$ (mm)',\n"
        "                       layout=Layout(width='420px')),\n"
        "    L2=FloatSlider(min=10, max=200, step=5, value=80,\n"
        "                    description='$L_2$ (m)',\n"
        "                    layout=Layout(width='420px')),\n"
        "    D2_mm=FloatSlider(min=20, max=200, step=5, value=120,\n"
        "                       description='$D_2$ (mm)',\n"
        "                       layout=Layout(width='420px')),\n"
        "    Q_Lpsek=FloatSlider(min=1, max=30, step=0.5, value=10,\n"
        "                         description='$Q$ (L/s)',\n"
        "                         layout=Layout(width='420px'))\n"
        ");"
    ),
    pitanja=(
        "1. **Identične grane.** Što se događa s raspodjelom protoka "
        "kada su obje grane potpuno jednake ($L_1 = L_2$, $D_1 = D_2$)? "
        "Zašto je rezultat 50:50 neovisno o samom protoku?\n"
        "\n"
        "2. **Utjecaj promjera.** Pri $L_1 = L_2$ ali $D_2 = 2 D_1$, "
        "kako se raspoređuje protok? Koja je eksponentna ovisnost "
        "$Q_1/Q_2$ o omjeru promjera?\n"
        "\n"
        "3. **Utjecaj duljine.** Pri istim promjerima i $L_2 = 4 L_1$, "
        "kako se raspoređuje protok? Zašto duljina ima manju polugu od "
        "promjera?\n"
        "\n"
        "4. **Treća grana.** Ako se na ovaj sustav doda i treća "
        "paralelna grana, što se događa s ukupnim padom energije pri "
        "istom $Q$? Zašto se paralelni spoj uspoređuje s otpornicima u "
        "električnom krugu?"
    ),
    teorija=(
        "Ovaj prikaz materijalizira temeljni princip paralelnog "
        "cjevovodnog spoja iz poglavlja U13: protok se raspoređuje tako "
        "da svaka grana ima isti pad ukupne energije između zajedničkih "
        "čvorova. Šira ili kraća grana spontano preuzima veći dio "
        "protoka — ne zato što joj je propisan, nego zato što na istom "
        "dopuštenom padu energije može propustiti više tekućine. "
        "Princip se proširuje na cijele cjevovodne mreže gdje se sustav "
        "rješava iterativno (Hardy-Crossova metoda)."
    ),
)


# ============================================================================
# Glavna funkcija
# ============================================================================

def main() -> int:
    MAPA_NOTEBOOKA.mkdir(parents=True, exist_ok=True)
    print(f"Mapa za izlaz: {MAPA_NOTEBOOKA}")
    print(f"Broj notebooka: {len(NOTEBOOKS)}")
    print()

    for ime, podaci in NOTEBOOKS.items():
        nb = izgradi_notebook(**podaci)
        put = MAPA_NOTEBOOKA / f"{ime}.ipynb"
        with put.open("w", encoding="utf-8") as f:
            json.dump(nb, f, indent=1, ensure_ascii=False)
            f.write("\n")
        print(f"  [OK] {put.name}")

    print()
    print("Gotovo. Notebooci su spremljeni u notebooks/.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
