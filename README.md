# MF1_udzbenik - kanonski radni folder

Ovo je glavni radni folder projekta. Aktualni MF1 udzbenik razvija se ovdje i samo ovdje.

## Gdje se stvarno radi

- `source/` – kanonski tekstovi poglavlja i dodataka
- `chapters/` – Quarto omotači za web i print tok
- `assets/print/` – statičke SVG ilustracije i skice (jedini dopušteni format za figure)
- `status_izrade_udzbenika.md` – kratki status projekta
- `protokol_prerade_zadataka_i_skica.md` – **autoritativan dokument** za protokol prerade zadataka i kanonski SVG dizajnerski standard
- `pravila_svg.md` – konsolidirani cheat-sheet SVG pravila
- `docs/radno/` – arhiva radnih dokumenata (matrice sparivanja, evidencije prijenosa, QA log, plan prijenosa, val1 prerade); nije dio studentskog teksta niti build-toka

## Što je ovdje već zaključano

1. `U00`, `U01-U13` i `D01-D03` postoje kao stvarna knjiga.
2. Teorija, izvodi, riješeni primjeri i zadaci nalaze se u istom toku čitanja.
3. Legacy prijenos zadataka više nije otvoreni radni dug.
4. Daljnji rad ide kao održavanje i selektivno jačanje, a ne kao nova masovna migracija.
5. Sve matplotlib/Python figure-blokove zamjenjuju statičke SVG datoteke u `assets/print/`; kanonski SVG standard naveden je u `protokol_prerade_zadataka_i_skica.md`.
6. U01–U04 su potpuno konvertirani; ostala poglavlja selektivno po potrebi.

## SVG standard – sažetak pravila

Detaljna pravila su u `protokol_prerade_zadataka_i_skica.md` (odjeljak **SVG standard za skice i ilustracije**). Ovdje su najvažnija:

### Paleta boja (obavezna)

| Svrha | Boja |
|---|---|
| Voda / opći fluid (gradient) | `#aed6f1` → `#5b9ec9` |
| Gorivo / ulje (gradient) | `#fde68a` → `#d4a017` |
| Stijenka / kućište | `#909fa8` → `#5d6d7e` |
| Sila ulaz / opterećenje | `#c0392b` (crvena) |
| Sila izlaz / rezultat | `#1e8449` (zelena) |
| Tlak / dubina | `#1565c0` (plava) |
| Kota / dimenzija | `#b7600c` (smeđa) |
| Efektivno polje (g_eff) | `#8e44ad` (ljubičasta) |
| Srafura linija | `#7a8a96` |

### Obveze svakog SVG-a

- `viewBox`, `role="img"`, `aria-labelledby`, `preserveAspectRatio="xMidYMid meet"`, `style="display:block;width:100%;max-width:XXXpx;height:auto;"`
- `<title>` i `<desc>` unutar `<defs>` za pristupačnost
- Svi `id` atributi s jedinstVenim prefiksom po datoteci (sprječava koliziju u HTML-u)
- Font: `'Segoe UI', Arial, sans-serif`
- Decimalni separator: zarez (`1,2 m`, ne `1.2 m`)
- Srafura stijenki: 45° dijagonala, 7×7 px pattern
- Kote: dvo-smjerni markeri + tik-crte + tekst izvan geometrije
- Strelice sila: `<marker>` elementi, ne samo debljina linije

### Zabrane

- Matplotlib/Python kod u Quarto izvoru
- Isti vizualni motiv u više figura istog poglavlja
- Globalni (ne-prefiksani) `id`
- Decimalna točka u brojevima
- Tekst koji se naslanja na geometriju ili vektore

## Što ovdje nije cilj

1. Ne dirati `vjezba_01.qmd` do `vjezba_13.qmd` iz roota repoa u ovom ciklusu.
2. Ne otvarati zasebni paralelni teorijski proizvod kao konkurentski glavni smjer.
3. Ne tretirati radne matrice i evidencije kao studentski tekst.
4. Ne koristiti matplotlib/Python za generiranje figura u finalnoj knjizi.

## Završna provjera

Iz ovog foldera standardni proizvodni check je:

```powershell
quarto render
```