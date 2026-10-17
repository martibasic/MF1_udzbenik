# Provedba — PDF lanac (Typst)

Uređene datoteke: `filters/mf1-typst-author-blocks.lua`, `assets/typst/mf1-author-blocks.typ`,
`mf1-book.typ`, `mf1-reading.typ`, `mf1-figures.typ`, `typst-show.typ`, `design-system/tokens.json`
(samo odjeljak `pdf`), `config/publication.json` (samo odjeljak `typst`), generirani
`_quarto-pdf.yml` i `assets/typst/mf1-tokens.typ` (preko `build_book.py --write`) te jedna
tvrdnja u `tools/test_book_model.py` (obrazloženje u t. 5). Nijedan `source/*.md`, SVG,
registar ni web filtar nije diran.

## 1. Provedeni nalazi

- **T1 decimalni zarez**: `{,}` između znamenki u TeX-u filtar označi, a u Typstu ga ispisuje kao
  `math.class("normal", ",")`: nema razmaka („9,81”, „0,0500 m³/s”). Obični zarezi (popisi
  `(26, 0)`) namjerno zadržavaju razmak. Prije: 3042 pojave „d, d” u PDF-u; poslije 110, i sve su
  stvarni popisi (`(v(y), 0, 0)`, `i = 1, 2, 3`, `(24, 0)`), koje odluka 8 ionako prevodi u `;`.
  Pregledane stranice s uzorcima iz recenzije (str. 20, 48, 103, 155, 168, 327 starog PDF-a).
- **T1 jedinice**: uklonjen razmak oko `\/` u matematici (`m³/ s`, `m³/ h` → `m³/s`). Prije 93,
  poslije 0 pravih pojava (ostaju `/ tan β`, `/ ln λ` — razmak operatora, ispravno).
- **T2 „kPa .”**: uzrok je u lancu, ne u izvorima. Pandoc piše `upright("kPa") .`, a Typst
  razmak između tekstnog atoma i točke ispisuje. Filtar uklanja razmak prije `.`/`,` iza
  tekstnog atoma ili zagrade te prije završne točke formule. Prije 198 pojava, poslije 0.
  Skripta za izvore nije potrebna (provjerom nađen samo jedan izvorni ` .` u u07 r. 126, koji
  isti filtar sada ispravlja).
- **V7**: neprekidni razmak „pog.␣N” (i broj–prva riječ naslova u upućivanjima na poglavlje)
  te „dodatak/dodatku␣C”. Prije 9 prijeloma iza „pog.” i 1 iza „dodatak”; poslije 0.
- **T5 siročad naslova**: `mf1-needspace` (nevidljiva nelomljiva proba visine
  `keep_with_next_em` = 4,5 em, pa negativni razmak) ispred svake oznake „Traži se/Rješenje/…”
  i (5,5 em) ispred naslova razina 2–4, uključujući naslove u dodatcima. Preostali pogodci
  heuristike su cjeloviti zadatci čiji je „Traži se” jedna rečenica na kraju zadatka.
- **T4**: unutarnji okomiti razmak završnog okvira 8 → 6 pt (token `panel_inset_y_pt`);
  razdjelnica „Dodaci” dobila je lokalni sadržaj dodataka A–F (kao stranice dijelova).
  Prazne završne stranice poglavlja koje nastaju jer nelomljiva tiskovna skica zadataka ne
  stane ostaju (vidi t. 2).
- **V3**: razmak odlomaka 0,6 → 1,15 em. Stari je razmak bio *manji* od proreda (0,75 em),
  pa su odlomci izgledali kao jedan blok. Razmak stavki popisa 0,35 → 0,9 em (globalno i u
  okvirima): stavke više nisu bliže od običnih redaka, pa vektori i indeksi ne dodiruju redak iznad.
- **U5 (PDF)**: razina Z1–Z6 sada je oznaka uz naslov (`Z2. … T1`, isti `mf1-level` kao P1–P6);
  redak „Razina: Tn” ispod zadatka uklonjen je samo u PDF-u. Ispred svakog Zn dodano je 22 pt
  (token `exercise_gap_pt`).
- **Završni okvir**: `.mf1-zavrsni-okvir` više ne dobiva nametnuti naslov „Sažetak”; bez
  vlastite labele okvir nema redak naslova (`title: none`).
- **T6 naslovnica i redoslijed**: str. 1 naslovnica (spacionirano „SVEUČILIŠNI PRIRUČNIK”,
  naslov, podnaslov s razmakom 22 pt, autorica, motiv, „Sveučilište u Splitu / Fakultet
  elektrotehnike, strojarstva i brodogradnje (FESB) / Split, 2026.”), str. 2 impresum, sadržaj od
  str. 3. Motiv je lijevi panel postojeće skice `u08_fig_kinematika.svg` (strujnica s vektorima
  brzine), pri renderu prebojen u jednu boju (`mf1-accent`), bez oznaka; SVG nije mijenjan.
  Impresum se i dalje piše u `source/index.md` (`## Impresum`): filtar taj odjeljak premješta
  u Typst stanje koje se ispisuje na poleđini, a uz vanjske poveznice ispisuje i adresu u zagradi.
  Ustanova, mjesto i godina zapisani su kao metapodatci `mf1-institution`, `mf1-place-year`
  u `config/publication.json` → `typst`.
- **V4**: „Vrati se na zadatak” u ključu F dobiva zaseban sivi dodatak „(str. N)” (Typst
  `query` + `counter(page).at`). Ako cilj ne postoji, dodatak se ne ispisuje. U okvirima s QR-om
  PDF sada piše „Skeniraj QR kod ili otvori:” i vidljivu adresu bilježnice. Prijelom je dopušten
  iza `/`, a Colab ostaje kao pričuvna poveznica.
- **W4 (PDF)**: naslov dodatka „Dodatak A — Sažetak formula i oznaka” (i u živom zaglavlju);
  numeracija A.1… i PDF bookmarks nepromijenjeni.
- **V8**: u bibliografiji se „“” zamjenjuje s „””. Prije 13 pogrešnih zatvarajućih navodnika,
  poslije 0. Riješeno pravilom `show bibliography` u `mf1-reading.typ`, bez vlastitog CSL-a.
- **V12**: PDF metapodatci `subject`/`description` i `keywords` (iz `config/publication.json`);
  `alt` za sve tiskovne skice iz `fig-alt` (redci višedijelne slike dobivaju „(dio i od n)”).
  Prije 17/144 `/Figure` s `/Alt`, poslije 145/145, uključujući motiv naslovnice.
- **Dodatak C, vizualne oznake**: u radnom stablu agent za sadržaj već je uklonio
  `mf1-signal-chip`/`mf1-signal-note` iz `d03`. Typst filtar zato za to ne treba posebno pravilo.

## 2. Nalazi koje nisam proveo i zašto

- **T4 djelomično**: kratke završne stranice (npr. sažetak sam na stranici iza velike skice
  Z1–Z6) nastaju jer je tiskovna skica nelomljiva i nema plutanja. Plutanje slika
  (`placement: auto`, P2 #9) nisam uveo jer mijenja položaj slike prema tekstu i auditima opisa.
  Kandidat za zaseban zahvat.
- **T3, T8, P2 #12, #18, #20, #21, #27**: ne pripadaju Typst lancu (izvori, SVG, tiskovne
  izvedenice, `build_print_figures.mjs`).
- **P2 #17** (QR uz tekst bez praznog pojasa): nisam posebno prepravljao. Novi tekst s
  adresom ispunjava stupac pored QR-a.
- **P2 #24, #26, P3 #30** (sadržaj do dvije razine, recto/verso, nenumerirano pog. 0):
  nisu bili u zadatku. Sadržaj je već `toc-depth: 2`.
- **Kratka adresa uz QR**: kratke adrese (npr. preusmjeravanja) ne postoje u repozitoriju,
  pa se ispisuje puna adresa JupyterLitea bez `https://`.
- **Dokumentacija** (nije u mom popisu datoteka; treba je uskladiti): `docs/pdf-tipografija.md`
  (razmak odlomaka 0,6 em → 1,15 em, stavke 0,9 em, razdjelnica „Dodaci” sada ima lokalni
  sadržaj, naslovnica/impresum/sadržaj od str. 3, razina Z uz naslov) i `docs/arhitektura.md`
  r. ~255 („veže završnu razinu uz posljednju stavku” → razina je uz naslov Zn u PDF-u).

## 3. Potrebne izmjene skica

Nema. Motiv naslovnice čita `assets/print/u08_fig_kinematika.svg` i izrezuje lijevi panel
(`viewBox="20 128 345 128"` u `mf1-book.typ`). Ako se ta skica geometrijski promijeni,
treba provjeriti izrez.

## 4. Promijenjeni brojevi i verifikatori

Nema promjena brojeva u primjerima ni zadatcima. Verifikatori nisu pokretani jer nisu dotaknuti.

## 5. Rezultat provjera

- Zbog tuđih izmjena koje su još u tijeku, render nad aktualnim izvorima **ne prolazi**:
  `scripts/build_book.py --render pdf` pada u `filters/mf1-components.lua:256: No PDF destination
  for chapters/d02_pojmovnik.qmd`. To je filtar i izvor agenta za web/strukturu, a uzrok nije
  u Typst lancu.
- Moje sam izmjene zato provjerila u vlastitoj izoliranoj mapi `tools/tmp/pdfagent`
  (izvori iz HEAD-a, preko njih moje datoteke, `build_book.py --write`, Quarto 1.9.37 iz
  `tools/tmp/ci`). Skripta: `scratchpad/pdfwork.py` (`MINE=1 … render`).
  - `tools/audit_pdf.py`: **PASS** (353 str.; A4, metapodatci, podnaslov na str. 1, sadržaj).
  - `tools/audit_pdf_layout.py`: **PASS** u prethodnom prolazu (17 QR-ova, jednadžbe, E.7,
    P/Z oznake, oznake skica). U posljednjem prolazu ostaje jedan nalaz: „str. 215: opis slike
    bez panela iznad njega: Slika 11.2”. Riječ je o dimenzijskoj matrici kao SVG-u bez
    pravokutnih crteža, koja je zbog novih razmaka pala na vrh stranice; heuristika audita
    takvu „tablicu kao sliku” ne prepoznaje kao panel. Prijelom se mijenja s tuđim
    izmjenama, a recenzija (R9) tu sliku ionako predlaže pretvoriti u tablicu. Audit nisam mijenjala.
  - `tools/audit_typst.py` PASS; `tools/test_component_visibility.py` OK;
    `tools/test_render_workspace.py` OK; `tools/audit_architecture.py` PASS.
  - `tools/test_book_model.py`: `test_exercise_fields_in_both_formats` sam prilagodila. Test je
    tražio `#mf1-task-level`, a namjerna promjena U5 to uklanja; nova tvrdnja provjerava
    `#mf1-level([T2])` u naslovu Z1 i odsutnost „Razina:”, dakle nije slabija.
    `test_pdf_document_links_follow_canonical_sections` pada u `mf1-components.lua`
    (ista greška d02, tuđa).
- **Broj stranica**: 335 → 353 na izvorima iz HEAD-a; gornja granica audita je 355. Približno
  12 stranica donosi V3 (razmak odlomaka), oko 2 razmak ispred Zn i 1 poleđina s impresumom.
  Uklanjanja koja provode drugi agenti (okvir „Inženjerski kontekst”, R2–R8) trebala bi to
  smanjiti. Ako završni render prijeđe 355, zbog V3 treba ili ponovno odrediti raspon
  (`docs/pdf-tipografija.md`, isto načelo ±10 %) ili smanjiti `paragraph_spacing_em` na 1,05
  (−1 str.).
- Kontrolni znakovi u uređenim datotekama: 0.
- Ova procjena je vizualna i automatska (stranice 1–3, 15, 24–25, 65–66, 85, 128–129, 150,
  214–215, 298–300, 333, 335). Nije pregledan cijeli PDF, a nije ni didaktička ocjena.
