# `tools/` — pomoćne skripte

Skripte za numeričku verifikaciju sadržaja i za obradu SVG skica u `assets/print/`.
Sve se pokreću iz korijena projekta, npr. `python tools/verify_all.py`.
Ovisnosti: samo standardna biblioteka Pythona (verifikacija) odnosno standardna
biblioteka + lokalne SVG datoteke (SVG alati). Ne trebaju `numpy`/`sympy`.

## Numerička verifikacija (trajno — koristi CI)

| Skripta | Namjena |
|---|---|
| `verify_all.py` | Runner koji pokreće sve `verify_uXX.py` i ispisuje zbroj `ok/fail`; izlazni kod 1 ako ijedna provjera padne. Ovaj korak vrti se u CI-ju (`.github/workflows/publish.yml`) prije rendera. |
| `verify_u01.py` … `verify_u14.py` | Po jedna datoteka po poglavlju; ponovno izvode brojčane rezultate riješenih primjera i zadataka te ih uspoređuju s vrijednostima u tekstu (relativna tolerancija). Kod dodavanja/mijenjanja primjera treba dopuniti odgovarajući `verify_uXX.py`. |

Trenutno stanje: **498/498 PASS**. Pri svakoj izmjeni brojeva u `source/uXX_*.md`
pokrenuti `python tools/verify_all.py` i po potrebi uskladiti provjeru.

## SVG obrada i QA (trajno)

| Skripta | Namjena |
|---|---|
| `svg_normalize.py` | Strukturni normalizator: prefiksira `id`-eve po datoteci, postavlja kanonski font, `aria`/`role` atribute i root atribute. Jednokratno proveden nad svih 139 SVG-ova; ponovno primjenjiv na nove skice. |
| `strip_svg_titles.py` | Uklanja vidljive top-level naslove iz SVG-ova (naslov pokriva Markdown caption). |
| `fix_svg_xml.py`, `fix_svg_ns.py` | Popravci XML konformanse i namespacea SVG datoteka. |
| `detect_box_geometry_overlap.py`, `scan_label_format.py` | Dijagnostika: preklapanje teksta i geometrije, format oznaka (bez izmjena — samo izvještaj). |
| `preview_server.py` | Lagani lokalni server koji poslužuje projekt i generira indeks svih SVG-ova po poglavlju za brzi vizualni pregled. |

## Jednokratni migracijski/popravni skriptovi (arhiva)

Korišteni u prošlim fazama; zadržani radi ponovljivosti, ne pokreću se rutinski:
`replace_matplotlib_blocks.py` (matplotlib→SVG konverzija), `fix_u01_skice.py`
(sistemski popravci U01 skica), te per-detalj popravci
`bring_dims_to_front.py`, `bring_text_to_front.py`, `fix_dim_arrow_refx.py`,
`fix_kv_fill.py`, `fix_label_single_line.py`, `fix_text_overflow.py`,
`remove_white_panels.py`, `undo_label_y_move.py`.

Logovi jednokratnih prolaza: `svg_normalize.log`, `strip_svg_titles.log`.
Privremeni radni izlazi idu u `tools/tmp/` (git-ignorirano).

> Napomena: generatori interaktivnih notebooka i QR kodova nisu ovdje nego u
> `scripts/` (`generiraj_notebooke.py`, `generiraj_qr.py`).
