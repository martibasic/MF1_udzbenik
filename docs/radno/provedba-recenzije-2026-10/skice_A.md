# Skice A — pog. 1–6 (datoteke u01–u07) i tiskovni sustav

Opseg: 44 referencirane skice `assets/print/u01_*` … `u07_*`, `tools/build_print_figures.mjs`,
`assets/figure-tokens.json`, `assets/figure-compositions.json` (samo indeksi mojih skica),
`tools/audit_print_figures.mjs`, `tools/audit_pdf_layout.py` (dio o veličini oznaka),
`tools/test_pdf_figure_labels.py` (nova regresija), `tools/check_u02_sketch_geometry.py`,
`docs/ispis-skica.md`, jedna rečenica u `protokol_prerade_zadataka_i_skica.md` i tri retka u `tools/README.md`.
Nisu dirani: `assets/print-layouts.json`, `assets/pdf-figures/`, `source/`, tuđe skice, git, render.

## 0. Što koordinator MORA napraviti prije provjera

1. U `assets/print-layouts.json` primijeniti `scratchpad/provedba/print_layouts_A_prijedlog.json`
   (svih 44 `source_sha1` + `panels`). Promijenjeni su paneli 18 skica: 17 jednoprizornih skica
   obrezano je odozgo nakon uklanjanja naslova (visina panela −dy, vidi tablicu u 2.), a
   `u07_fig_uvod_pregled.svg` složena je okomito (`[[12,12,459,395],[12,431,480,206]]`).
   Dok se to ne primijeni, `check_u03`/`check_u04` (`check_scene_canvas`) i
   `audit_sketch_design.py` padaju zbog **starog** panela izvan novog `viewBox`-a — očekivano.
2. Pokrenuti `node tools/build_print_figures.mjs` (tokeni, generator i 44 izvora su promijenjeni).
3. `node tools/audit_print_layouts.mjs`, render PDF-a, `python tools/audit_pdf_layout.py`.

Provjereno u izoliranoj kopiji (`tools/tmp/skiceA/env`, gitignorirano) s predloženim
`print-layouts.json`: generator za svih 44 skica, `audit_print_figures` → **PASS (44 figure,
56 redaka, 878 oznaka, 2016 geometrijskih elemenata; bez preklapanja i rezanja, oznake ≥ 9 pt,
indeksi ≥ 6,5 pt, drugi fluid razlučiv u sivoj)**; `audit_print_layouts` za u01–u07 bez nalaza;
`check_u01…u06` i `audit_sketch_design.py` PASS.

## 1. Tiskovni sustav (T8, U9)

**T8 — indeksi ~70 %.** Token `figure-index-size` = 6,65 pt (70 % od 9,5 pt) i zasebni minimum
`figure-index-min-size` = 6,5 pt; `figure-small-label-size` = 9 pt ostaje minimum oznaka.
Generator: `tspan` s `baseline-shift="sub|super"` (i ugniježđeni u njemu) dobiva index-size;
ostali `tspan`-ovi (kurzivni simboli, podebljani vektori) sada nasljeđuju veličinu oznake
(prije su dobivali 9 pt i uz 9,5 pt oznaku). Audit `audit_print_figures.mjs`: osnovni dijelovi
≥ 9 pt, indeksi ≥ 6,5 pt, uz kontrolu da index-min ≥ 6,5 i < 9. `audit_pdf_layout.py`: manji
minimum vrijedi samo za kratak niz bez razmaka koji neposredno dodiruje oznaku pune veličine
(`_index_spans`); izolirana sitna riječ i dalje pada (postojeći test i novi
`test_index_has_own_minimum_only_next_to_its_label`, 11/11 OK). Ispravljeno u generatoru i:
oznaka koja bi izašla iznad gornjeg ruba retka više se ne smatra „dobrom” (`box[1] >= 0`) —
pojavilo se nakon uklanjanja naslova (u03_ch1).

**U9 — drugi fluid u tisku.** `figure-tokens.json` → `"print-palette": {"second-fluid": "#d6c597"}`;
siva ≈ 197 prema vodi ≈ 231 (razlika 34 ≥ 25; ekran `#eadfc5` ≈ 224). Generator zamjenjuje ton
u ispuni/potezu klonirane geometrije i u `defs` (uzorci); kanonski/mrežni SVG nepromijenjeni.
Audit: razlika sive ≥ 25 i nijedan tiskovni redak ne smije sadržavati zaslonski ton.
Napomena: novi ton i `solution` (`#bdcfd2`, ≈ 202) u sivoj su bliski; u mojim skicama nisu
na istom panelu.

**Nelomljivi razmak.** Generator lomi samo na običnom razmaku; u skicama je broj + jedinica
spojen s U+00A0 (riješen „A = 0,18 / m²”, pdf #7, T7 za 2.3).

Dokumentacija: `docs/ispis-skica.md` (tokeni, odjeljci „Indeksi (T8)”, „Drugi fluid u tisku (U9)”,
nelomljivi razmak, opis audita), protokol (r. 452), `tools/README.md`. `AGENTS.md` ne mijenjam;
„najmanje 9 pt za oznake” i dalje vrijedi.

## 2. Izmjene skica po datoteci

Zajednički (svih 44, skripte `scratchpad/contentA.py`, `typoA.py`, `cropA.py`):
simboli veličina kurziv (tspan), riječi/tvari/jedinice/brojevi/indeksi uspravno; uklonjen kurziv
cijelih oznaka (npr. „*voda*”, „*os vrtnje*”); Unicode indeksi → `tspan sub` (u01 val1/val2/vjezbe,
u02 vjezbe/lezaj); numerički `baseline-shift` (−2,64) → `sub`; osnovna veličina 11–12 (u01_ch1
širine 831 → ×1,15, tj. 12,5–14; u03_ch1 namjerno ×1 zbog gustoće), nazivi panela 12–13; točke
(A, B, C, D, O, G, CP) i skalarne kote u u05 uvodu više nisu podebljane (podebljano = vektor);
broj–jedinica nelomljivim razmakom; title/desc: vertikaln→okomit, horizontal→vodoravn,
centroid→težište.

- **u01_fig_kocnica_vozila**: F_n→**F**_pap, F_M→F_gc, d_M→d_gc, F_f→F_pr, F_r→F_st (prema tekstu P6); desc F_gc.
- **u01_vjezbe_skice**: uklonjena proza Z2 („dijagonalni par…”; već u Napomenama).
- **u02_ch1**: „p_M = p_M,2” → „p_M > 0” (P4 ne računa p_M,2); stijenke kapilara puni obris.
- **u02_val2**: uklonjen naslov; podatkovni redak pomaknut na njegovo mjesto; „0,18 m²” nelomljivo.
- **u02_fig_kapilarni_uspon_etanol / kinematicka / lezaj**: uklonjeni naslovi; obrezano (dy 57/34/64);
  kapilara i uvećani detalj puni obris.
- **u02_fig_uvod_pregled, u02_vjezbe** (Z6 igla): stijenke kapilare/igle puni obris; desc F_1, F_2.
- **u03_fig_balastni_tank**: ρ_b→ρ_mv, ext→van, int→unu, T_g→T, H_t→H_tk, uklonjeno „neto na dno:
  prema gore”; odzračnik i sondna cijev puni obris; desc „Okomito mjerilo”.
- **u03_ch1**: ullage→ulaž/ulažna vrpca (oznake, title, desc); uklonjen „Teretni tank (presjek)”; dy 16.
- **u03_fig_zatvoreni_spremnik_tlak, u03_fig_pumpa_usis, u03_val1**: uklonjeni naslovi (dy 38/68/73);
  u03_val1 i u03 uvod: cijevi manometra puni obris (ista geometrija pojasa).
- **u03_balans_tlaka_i_geff**: title „Ravnoteža tlaka…”. **u03_fig_uvod_pregled**: title opisni.
- **u03_vjezbe**: U-cijevi Z3, Z5 i spojni vod Z6 puni obris (spremnici ostaju šrafirani).
- **u04_fig_rotirajuci_cilindar**: h_v→h_van, h_u→h_unu; uklonjena dva retka proze i naslov;
  dodana kratka oznaka „prividna sila” uz inače neoznačenu silu (vektor mora imati oznaku); dy 42.
- **u04_val2**: uklonjen naslov (proturječio potpisu); dy 11.
- **u04_ch1**: uklonjen naslov; oznaka h_0 premještena lijevo od stijenke u dva retka („h₀ =” /
  „0,60 m”) jer je presijecala paraboloide; dy 134.
- **u04_fig_autocisterna**: uklonjeno „otvoreni pravokutni model spremnika”.
- **u04_fig_uvod_pregled**: title opisni, desc „okomitom”. **u04_vjezbe**: Z3 „Okomito ubrzavanje i
  kočenje”; uklonjeno „shematski profil nakon smirivanja” (u Napomenama).
- **u05_ch1**: T→**F**_s; uklonjen naslov; A i „(zglob)” lijevo od zgloba, h_u/h_v kote bez
  presijecanja kotne crte; desc F_s, h-u/rho-u/h-v/rho-v, „Okomita”; dy 18.
- **u05_val3**: T→**F**_s, uklonjen naslov, A odmaknut od poklopca; desc; dy 56.
- **u05_vjezbe**: „sila T”→„sila F_s”, Z5 T→F_s (ID `u05vs_z5_T` zadržan), T_max→F_s,max; uklonjeno
  „sila okomita na crtež”, „parabola, tjeme A na površini”, „voda iznad pokrova”, „zglob u dnu;”
  (sve u tekstu zadatka/Napomenama); desc F_s.
- **u05_fig_uvod_pregled**: uklonjeno „rezultanta” (presijecala kotu H); title i desc.
- **u05_val1**: uklonjen naslov; title/desc „Okomita”; dy 30.
- **u06_ch1**: T→**F**_s; desc. **u06_val1, u06_val3**: desc okomit/vodoravnice.
- **u07_vjezbe**: Z3 m_s→m_k, Z6 m_a→m_k, Z4 „ulje”→„otopina” i ispuna `solution`; title „Zadatci”, desc m-k.
- **u07_fig_pumpno_kuciste**: title „…kućište crpke”; uklonjen naslov; dy 53.
- **u07_ch2**: uklonjen naslov; desc težište/Ekscentricitet/okomite; dy 140.
- **u07_val1, u07_val2**: uklonjeni naslovi (dy 32/83); u07_val2 title „ravnoteža u okomitom smjeru”.
- **u07_ch1**: desc težište; m_k odmaknut od ruba ormara.
- **u07_fig_uvod_pregled** (skice 16, pdf 21): paneli složeni okomito (samo translacija),
  viewBox 987×419 → 504×649; na webu oznake više nisu umanjene na ~8 px.

`figure-compositions.json`: u03_val1 (bez header_text, footer [6], pomaci −1), u04_ch1 (bez
header_text — h₀ više nije sudarna), u05_val1 (pomaci ≥ 6 → −1).

## 3. Neprovedeno / s ograničenjem

- **Pravilo 3 (cijevi puni obris) u u01**: hidraulički krugovi u u01 (kočnica, kormilarski stroj,
  preše) nacrtani su kao jedan neprekinut presječni zid cilindara i vodova; dijeljenje na „cijev”
  i „spremnik” traži novo crtanje spojeva, pa je ostavljeno (vizualni redizajn). Provedeno za
  samostalne cijevi: kapilare/igla (u02), U-cijevi i vodovi manometara (u03), odzračnik i sonda.
- `u03_fig_balastni_tank`: nadindeks A uz p_M,unu (skice 22) ostao kao `super` tspan.
- `u03_ch1`: „referentna točka ulaža” i „p_M,pl = 3,0 kPa” u tisku stoje blizu (bez preklapanja).
- Provjera tipografskog pravila u `audit_sketch_design.py` (U8) nije dodana: zajednički audit
  bi pao zbog tuđih skica (u08–u15); preporuka za koordinatora nakon druge faze.
- Nazivi panela u01–u07 vjezbe nisu izjednačeni s naslovima zadataka (osim „Okomito…”).

## 4. Rečenice za tekst

Nisu potrebne: sva uklonjena proza već stoji u tekstu zadatka, „Napomenama uz skice”,
„Veza s proračunom” ili potpisu (u04 cilindar, u01 Z2, u04 Z5, u05 Z1–Z3).

## 5. Checkeri

`tools/check_u02_sketch_geometry.py`: provjere „F₁=?”, „F₂=?”, „h₂=?” zamijenjene jednako strogima
„F1=?”, „F2=?”, „h2=?” uz zahtjev da je znamenka stvarni `tspan sub` (nova funkcija `subscripts`).
Ostali checkeri bez izmjena; ID-jevi koje čitaju zadržani.

## 6. Ograničenja

Vizualno pregledano na Edge renderima (mreža i tiskovni retci) svih 44 skica; sivi ispis nije
renderiran, razlika je provjerena tokenom i auditom. Didaktička kvaliteta i fizikalna točnost nisu
predmet ovih provjera.
