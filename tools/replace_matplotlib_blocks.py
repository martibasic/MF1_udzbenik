"""Zamjeni 24 matplotlib ```{python} blokova u source/u*.md s SVG referencama.

Mapiranje matplotlib label -> SVG datoteka -> caption se nalazi u tablici ispod.
Svaki blok ide od ```` ```{python} ```` do prve linije s ```` ``` ```` koja zatvara blok.
Preuzima se postojeci `fig-cap` iz bloka kao caption za markdown referencu (ako postoji),
inace se koristi default caption iz tablice.

Idempotentno: ako blok vec ne postoji (npr. vec je zamijenjen), preskace se.
"""
from __future__ import annotations

import re
from pathlib import Path


# Mapiranje label -> (SVG filename, default caption)
MAPPING: list[tuple[str, str, str, str]] = [
    # (chapter, label, svg, default_caption)
    ("u07", "fig-uvod-u07", "u07_fig_uvod_pregled.svg",
     "U07 - Pregled poglavlja: uzgon, plivanje i stabilnost"),
    ("u07", "fig-u07-bocni-pomak-centra-uzgona", "u07_fig_bocni_pomak.svg",
     "U07 - Bocni pomak centra uzgona iz rubnih urona"),
    ("u07", "fig-u07-pumpno-kuciste-uzgon", "u07_fig_pumpno_kuciste.svg",
     "U07 - Uzgon na potonulo pumpno kuciste"),
    ("u07", "fig-u07-ponton-nagib", "u07_fig_ponton_nagib.svg",
     "U07 - Privezni ponton s pomaknutom opremom"),

    ("u08", "fig-uvod-u08", "u08_fig_uvod_pregled.svg",
     "U08 - Pregled poglavlja: kontrolni volumen i kontinuitet"),
    ("u08", "fig-u08-t-komad-hidraulika", "u08_fig_t_komad_hidraulika.svg",
     "U08 - T-komad hidraulike"),
    ("u08", "fig-u08-retencijski-bazen", "u08_fig_retencijski_bazen.svg",
     "U08 - Retencijski bazen s dva dotoka i ispustom"),

    ("u09", "fig-uvod-u09", "u09_fig_uvod_pregled.svg",
     "U09 - Pregled poglavlja: Bernoullijeva jednadzba idealnog fluida"),
    ("u09", "fig-u09-venturijeva-cijev", "u09_fig_venturijeva_cijev.svg",
     "U09 - Venturijeva cijev za mjerenje protoka"),
    ("u09", "fig-u09-brzina-istjecanja-propust", "u09_fig_propust_brana.svg",
     "U09 - Brzina istjecanja kroz propust u brani"),

    ("u10", "fig-uvod-u10", "u10_fig_uvod_pregled.svg",
     "U10 - Pregled poglavlja: realni Bernoulli i gubici"),
    ("u10", "fig-u10-usisni-tlak-crpka", "u10_fig_crpka_usisni_tlak.svg",
     "U10 - Usisni tlak na ulazu servisne crpke"),
    ("u10", "fig-u10-rashladni-cjevovod", "u10_fig_rashladni_cjevovod.svg",
     "U10 - Pad tlaka u rashladnom cjevovodu motora"),
    ("u10", "fig-u10-gravitacijska-odvodnja", "u10_fig_odvodnja_zgrade.svg",
     "U10 - Gravitacijska odvodnja zgrade"),

    ("u11", "fig-uvod-u11", "u11_fig_uvod_pregled.svg",
     "U11 - Pregled poglavlja: kolicina gibanja i sile strujanja"),
    ("u11", "fig-u11-koljeno-rashladni", "u11_fig_rashladni_koljeno.svg",
     "U11 - Sila na koljeno rashladnog cjevovoda"),
    ("u11", "fig-u11-mlaznica-vatrogasni-monitor", "u11_fig_vatrogasni_monitor.svg",
     "U11 - Sila mlaznice vatrogasnog monitora"),

    ("u12", "fig-uvod-u12", "u12_fig_uvod_pregled.svg",
     "U12 - Pregled poglavlja: pokretne lopatice i potisak"),
    ("u12", "fig-u12-relativni-dotok-lopatica", "u12_fig_relativni_dotok.svg",
     "U12 - Relativni dotok na pokretnu lopaticu"),
    ("u12", "fig-u12-pelton-lopatica", "u12_fig_pelton_lopatica.svg",
     "U12 - Snaga na Peltonovoj lopatici"),
    ("u12", "fig-u12-hidromlazni-pogon", "u12_fig_hidromlazni_pogon.svg",
     "U12 - Hidromlazni pogon"),

    ("u13", "fig-uvod-u13", "u13_fig_uvod_pregled.svg",
     "U13 - Pregled poglavlja: cjevovodi"),
    ("u13", "fig-u13-rashladni-cjevovod-peci", "u13_fig_rashladni_cjevovod_peci.svg",
     "U13 - Rashladni cjevovod rotacijske peci"),
    ("u13", "fig-u13-paralelne-grane-vodovod", "u13_fig_paralelne_grane_vodovod.svg",
     "U13 - Paralelna razvodna mreza vodovoda"),
]


ROOT = Path(__file__).resolve().parent.parent
SOURCE_DIR = ROOT / "source"

CHAPTER_TO_FILE = {
    "u07": "u07_uzgon_plivanje_i_stabilnost.md",
    "u08": "u08_kontrolni_volumen_i_kontinuitet.md",
    "u09": "u09_bernoullijeva_jednadzba_idealnog_fluida.md",
    "u10": "u10_realni_bernoulli_i_gubici.md",
    "u11": "u11_kolicina_gibanja_i_sile_strujanja.md",
    "u12": "u12_pokretne_lopatice_i_potisak.md",
    "u13": "u13_cjevovodi.md",
}


def find_block_by_label(content: str, label: str) -> tuple[int, int, str | None] | None:
    """Pronadi pocetak i kraj ```{python} bloka s zadanim labelom.

    Vraca (start_idx, end_idx, fig_cap_or_None) ili None ako blok ne postoji.
    end_idx je indeks IZA zatvarajuceg ```.
    """
    # Pattern: ```{python}\n#| label: fig-XXX ... ```
    pattern = re.compile(
        r"```\{python\}\s*\n"  # otvaranje bloka
        r"(?:#\|[^\n]*\n)*"     # YAML-style meta lines
        r"",  # placeholder; treba pronaci #| label: label
        re.DOTALL,
    )

    # Pravi pristup: iteriraj kroz sve ```{python} blokove, provjeri label
    block_pattern = re.compile(
        r"```\{python\}\s*\n(.*?)\n```",
        re.DOTALL,
    )

    for m in block_pattern.finditer(content):
        body = m.group(1)
        # provjeri ima li #| label: <label> unutar prvih ~20 linija
        first_lines = "\n".join(body.split("\n")[:20])
        if re.search(rf"^#\|\s*label:\s*{re.escape(label)}\b", first_lines, re.MULTILINE):
            # extract fig-cap if present
            cap_match = re.search(
                r"^#\|\s*fig-cap:\s*['\"]?(.+?)['\"]?\s*$",
                first_lines,
                re.MULTILINE,
            )
            cap = cap_match.group(1).strip() if cap_match else None
            return (m.start(), m.end(), cap)

    return None


def replace_in_file(chapter: str, label: str, svg: str, default_cap: str) -> bool:
    fpath = SOURCE_DIR / CHAPTER_TO_FILE[chapter]
    content = fpath.read_text(encoding="utf-8")

    result = find_block_by_label(content, label)
    if result is None:
        print(f"  [skip] {chapter} {label}: blok nije pronadjen (mozda je vec zamijenjen)")
        return False

    start, end, cap = result
    caption = cap if cap else default_cap

    # Sastavi novu markdown referencu
    new_ref = f"![{caption}](../assets/print/{svg}){{#{label} fig-align=\"center\"}}"

    new_content = content[:start] + new_ref + content[end:]
    fpath.write_text(new_content, encoding="utf-8")

    print(f"  [ok]   {chapter} {label} -> {svg}")
    return True


def main() -> None:
    print(f"Zamjena matplotlib blokova s SVG referencama (24 mapiranja)")
    print(f"Source dir: {SOURCE_DIR}")
    print()

    n_ok = 0
    n_skip = 0
    for chapter, label, svg, default_cap in MAPPING:
        if replace_in_file(chapter, label, svg, default_cap):
            n_ok += 1
        else:
            n_skip += 1

    print()
    print(f"Sazetak: {n_ok} zamjena, {n_skip} preskoceno")


if __name__ == "__main__":
    main()
