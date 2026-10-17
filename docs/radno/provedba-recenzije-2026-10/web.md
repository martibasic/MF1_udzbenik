# Provedba — mrežno izdanje i zajedničke komponente (web)

## 1. Provedeni nalazi

- **W1 (široke jednadžbe)** — `web/math.js`: numerirana display-jednadžba koja ne stane u stupac prelazi u kompaktni raspored (oznaka broja ispod jednadžbe, desno; uklanja se simetrična rezerva za broj). MathML za čitače zaslona nepromijenjen. `styles/components.css`: znak pomicanja bez JavaScripta (sjene na rubu koje se pojave samo na strani gdje je dio formule skriven) za `.math.display` i široku inline-formulu. `responsive.css.in`: ≤768 px display-formule 0,92 em. Izmjereno na 390 px: pog. 6 — 65 → 32 jednadžbe šire od stupca (ostale imaju znak pomicanja i vidljiv broj); pog. 10 — 34 od 77; na 820 px pog. 6 i 10 po 1. MathJax 3 (koji Quarto 1.9 učitava) ne podržava `displayOverflow: 'linebreak'` (to je MathJax 4), pa pravo prelamanje nije uključeno.
- **W3** — `content/book.json`: „Numerika i CFD V&V” (generator HTML-a escapira jednom; dodano i escapiranje opisa kartice). Naslov pog. 5 → „Hidrostatičke sile na ravne i zakrivljene plohe”; ID i put isti, stari naslov dodan u `title_aliases` (stare `mf1-ch-ref` reference i dalje se razrješavaju). D06 i omotači obnovljeni s `build_book.py --write`.
- **W4** — `_language.yml`: `crossref-apx-prefix: "Dodatak"`; naslovi su „Dodatak A — …” (H1, `<title>`, OG). Reference u tekstu („dodatak D”, „dodatku F”) običan su tekst u izvorima i ostaju malim slovom. Prefiks vrijedi i za Typst ako ga Quarto ondje koristi.
- **W5** — `.mf1-ch-ref` je `display:inline`, bez paddinga; u zajedničkom filtru „pog.“ i broj spaja neprekidni razmak (u PDF-u `pog.~5`).
- **W6** — ≤768 px: kompozitne skice (`data-figure-kind="composite"`: sve ploče Z1–Z6 i 12 uvodnih pregleda) prikazuju se kao postojeći tiskovni retci naslagani jedan ispod drugoga i skalirani zajedno; „Povećaj skicu” i dalje otvara cijelu ploču. Grupa redaka dobiva `role="img"` i alt originala. Tiskovni retci sada koriste CSS varijable (`--mf1-row-width/height`) umjesto inline stilova; u ispisu su i dalje u prirodnoj veličini (audit_print_site PASS). `figure img {max-height:70vh; object-fit:contain}` samo za zaslon.
- **V10** — `a{border-bottom}` sveden na `main a` (uz iznimke breadcrumb, anchor, poveznica slike); bočna traka/navbar bez podcrtavanja (provjereno: 0 px). TOC sakriven ≤992 px (glavni stupac na 820 px 607 → 633 px). Uklonjen `min-width:32rem` referentnih tablica (sve su 3-stupčane); 42rem ostaje samo za tablice s ≥4 stupca; dodani rubni prijelazi (mask) kao znak pomicanja, upravljani JS-om prema položaju pomaka. Fontovi lokalno: `assets/fonts/web/` (Source Serif 4 opsz+wght, normalni i kurziv; Inter wght; podskupovi latin, latin-ext, greek; woff2 iz `@fontsource-variable/*` 5.2.9/5.2.8 s cdn.jsdelivr.net, OFL licence priložene). `design-system/tokens.json`: `web_font_import` zamijenjen s `web_fonts`, `build_book.py` generira `@font-face` u `styles/tokens.css`. Uklonjen i Bootswatch (flatly) Google Fonts import (`$web-font-path: false` u generiranom temu). Provjereno: nema zahtjeva prema googleapis, fontovi učitani. Meta „Autorica” na stranicama poglavlja/dodataka stvarno skrivena (selektor jednake težine kao Quartov), početna je zadržava. `.mf1-eyebrow` sakriven preko registra (`HomeEyebrow`, vidljiv samo u `pdf`) i uklonjen CSS; prva stavka bočne trake (naslov knjige) skrivena.
- **QR / dodatak C** — registar: `NotebookQR` (`mf1-interaktivno-qr`, vidljivost `pdf`, `print`), `SignalChip` (`mf1-signal-chip`, `mf1-signal-note`, samo `web`). Zajednički filtar `mf1-components.lua` proširen tako da registarska vidljivost vrijedi i za inline-komponente (Span) i sirove HTML elemente (`<img class>`, `<p class>`): HTML dobiva `mf1-hidden-*`, Typst ih uklanja (s blokovima između otvorene i zatvorene oznake). Adapteri nemaju nove popise klasa. (Napomena: čipovi su u međuvremenu uklonjeni iz izvora d03 radom drugog agenta; pravilo ostaje bezopasno.)
- **V11** — četiri poruke pretrage u `_language.yml`. Naslovi riješenih primjera su `<h3 class="mf1-component-title mf1-box-label">` (isti stil; sadržaj bez `<p>`). Sklopivi blokovi: novi filtar `filters/mf1-html-callouts.lua` (post-render) već u HTML-u upisuje `role="button"`, `tabindex="0"` i hrvatsku oznaku „Prikaži ili sakrij odjeljak: …” umjesto „Toggle callout”.
- **V12** — `book.json` `book.description` (jedna rečenica) i `open-graph: true` → `<meta name="description">` i OG na svim stranicama. Bočna navigacija `aria-label="Navigacija kroz poglavlja"` (JS, Quarto nema opciju). Komponentama se više ne prepisuje `title="…"` u HTML (bio je razlog istih imena CFD blokova).
- **Dodatak F** — „Vrati se na zadatak” postaje strelica ↩ u naslovu zadatka (HTML adapter), s `aria-label`/`title` „Vrati se na zadatak”; 90 poveznica.
- **U5 (HTML)** — razina Z1–Z6 kao čip uz naslov (isti `.mf1-level` kao kod P); redak „Razina: T1” je registarska komponenta `TaskLevel` vidljiva samo u PDF-u. Čipovima P i Z dodano skriveno „razina” za čitače zaslona.
- **Sažetak** — zajednički filtar više ne nameće labelu „Sažetak” u `.mf1-zavrsni-okvir`; okvir bez vlastite labele nema naslov.
- **Uredničko normaliziranje** — `mf1-editorial-normalization.lua` radi s oba oblika („Zadaci” ispravlja, „Zadatci” propušta).
- **Povećaj skicu** — poveznica je izvan `figcaption`, s `aria-label`, strelica `aria-hidden`.
- **Tipke** — prva poveznica bloka bilježnice ostaje tipka; svaka sljedeća (Colab) je tiša tekstna poveznica, isti stil u svim poglavljima.

## 2. Nalazi koje nisam proveo

- W1 (c) dijeljenje najduže jednadžbe `A ⟹ B` u dva retka — izmjena izvora (`source/*.md`), nije moje područje.
- Pravo prelamanje formula (MathJax 4) — zahtijeva promjenu verzije MathJaxa i fonta; nije učinjeno zbog rizika za cijeli prikaz.
- Web P2 #22 (naslov „0. Kako koristiti priručnik”), P3 #25 (naslov stranice za ispis „MF1 — …”), #28 (relativne poveznice na bilježnice), #29 (tamni način), #15 (širina retka) i #24 (catalog_title ≠ naslov) — nisu bili u mojem zadatku; #22 i #25 su u `build_book.py` i mogu se riješiti u jednom retku ako autorica želi.
- Typst adapter (`mf1-typst-author-blocks.lua`, PDF agent) i dalje nameće labelu „Sažetak” u `.mf1-zavrsni-okvir` (r. ~202); u PDF-u će nakon `## Sažetak` biti dvostruki naslov dok se ne ukloni.
- `docs/arhitektura.md` r. 222 spominje `web_font_import`; treba zamijeniti s `web_fonts` (dokument nije u mojem popisu).
- GitHub ikona u bočnoj traci ima englesko „Source Code” (Quarto UI, nema ključa u `_language.yml`).
- 2-stupčane tablice dodatka A i dalje su na 390 px šire od stupca zbog nelomljivih formula; sada imaju znak pomicanja i napomenu, ali ne mogu se prelomiti.

## 3. Potrebne izmjene skica

Nema.

## 4. Promijenjeni brojevi i verifikatori

Nema promjena brojeva. D06 je obnovljen generatorom (naslov pog. 5 i promjene izvora drugih agenata).

## 5. Rezultat provjera

Nakon zadnjeg `build_book.py --render web` (objavljeno u `_site`, pregled http://127.0.0.1:8000/):

- `audit_viewports.mjs _site` PASS (72 prikaza 320/768/1440 + A4 print, axe WCAG 2.2 AA, tipkovnica, JupyterLite Idle). Prvi prolaz pao je na `link-in-text-block` jer sam crossref poveznicama (`.quarto-xref`) uklonio podcrtu; ispravljeno, crossrefi zadržavaju podcrtu.
- `audit_rendered_site.py` PASS; `audit_rendered_model.py` PASS (2108 objekata); `audit_print_site.mjs` PASS (184 zaslonske skice, 248 tiskovnih redaka u prirodnoj veličini); `audit_architecture.py` PASS; `test_component_visibility.py` OK (3); `test_render_workspace.py` OK (5).
- Vlastita mjerenja u Edgeu (Playwright): nema vodoravnog pomaka stranice ni na jednoj širini; nema zahtjeva prema Google Fonts; meta „Autorica” skrivena na poglavljima/dodatcima; QR nevidljiv na zaslonu; 6–7 h3-naslova primjera po poglavlju; 6 čipova razine Z po poglavlju; 90 strelica u D06; H1 „Dodatak A — …”.
- Ograničenje: didaktička i vizualna kvaliteta procijenjena je na pregledanim snimkama (pog. 1, 6, 10, dodatci A i F), ne na svim stranicama. Kompaktni brojevi jednadžbi i naslagani retci rade samo s JavaScriptom (bez njega vrijedi dosadašnji prikaz sa znakom pomicanja).
