# Vizualna recenzija mrežnog izdanja (web)

Pregledano u Playwrightu (Edge) na http://127.0.0.1:8000/ pri širinama 390, 820 i 1440 px:
početna stranica, „0. Kako koristiti priručnik”, poglavlja 1, 6, 9 i 13, dodatci A i F te stranica
`za_ispis.html`. Uz snimke zaslona (mapa `recenzija/web/`, datoteke `<stranica>_<širina>_*.png`)
proveden je i automatski prolaz kroz sva 22 poglavlja/dodatka na 390 i 1440 px koji je izmjerio
horizontalno prelijevanje, širine formula i tablica, nazive blokova, vrste callouta i naslove
odjeljaka (`recenzija/web/consistency.json`, `metrics_*.json`). U repozitoriju ništa nije mijenjano.

## 1. Sažetak

Mrežno izdanje izgleda zrelo i suzdržano: serifni tekst, sans naslovi, tanke lijeve crte uz obojene
blokove i mirna bočna traka daju dojam suvremenog akademskog priručnika, a ne „web-stranice”.
Stranica se ni na jednoj širini ne pomiče horizontalno kao cjelina (scrollWidth = širina prozora na
svim 22 stranicama), fontovi se učitavaju, formule se renderiraju, poveznice na JupyterLite i Colab
postoje u svakom poglavlju. Za završetak ipak treba riješiti tri skupine stvari. Prvo, na mobitelu
(390 px) velik broj numeriranih jednadžbi širi je od zaslona (u pog. 6 njih 70, u pog. 10 njih 73)
pa se desni dio i broj jednadžbe odrežu bez vizualnog znaka da se može pomicati; isto se na 820 px
događa u pog. 6 i 13. Drugo, među poglavljima postoje stvarne neujednačenosti istog elementa:
u pog. 13 „Smjernica” i „Kontrolni rezultat” imaju zamijenjene boje u odnosu na svih ostalih 14
poglavlja, isti interaktivni blok nosi tri različita naziva i dvije različite oznake tipki, a sažetak
poglavlja postoji u tri varijante (samo odjeljak, samo okvir, oboje). Treće, nekoliko sitnih, ali
vidljivih grešaka u prikazu: `V&amp;V` ispisan doslovno na početnoj stranici, naslovi dodataka pišu
„dodatak A” malim slovom, unakrsne reference `pog. 3 …` lome se u zaseban redak s razmakom ispred
točke, a autorica se ponavlja na vrhu svake stranice iako CSS to pokušava sakriti. Sve navedeno
rješivo je bez novog sadržaja: nekoliko pravila u CSS-u, jedna oznaka u `_language.yml`, jedan
entitet u `book.json` i usklađivanje oznaka u izvorima.

## 2. Tablica nalaza

Oznake: P1 — ispraviti prije završetka; P2 — vrijedi napraviti; P3 — opcionalno.
„Provjereno” znači da je nalaz izmjeren ili viđen na snimci; „dojam” je autorska procjena.

### P1

| # | Gdje | Što | Zašto je problem | Prijedlog |
|---|------|-----|------------------|-----------|
| 1 | Sva poglavlja na 390 px (npr. `u01…#eq-1.7`, `u06` P1 jedn. 6.6–6.8, izvod u `u13`); snimke `u01_390_el_we.png`, `u13_390_el_izvod.png`. Izmjereno: broj display-formula širih od zaslona po poglavlju — u01 33, u02 28, u03 38, u04 40, u05 36, u06 70, u07 51, u08 47, u09 20, u10 73, u11 43, u12 24, u13 44, u14 54, u15 16; na 820 px u06 12, u13 3. | Numerirane jednadžbe (`\gamma=\rho g=860\cdot 9{,}81=8436{,}6\ \mathrm{N/m^3}`, `F_1/A_1=F_2/A_2 \Rightarrow F_2=…`) odrezane su s desne strane; broj jednadžbe u zagradi nestaje. `.math.display` ima `overflow-x:auto`, ali nema nikakvog vizualnog znaka da se sadržaj može pomicati. | Student na mobitelu ne vidi rezultat ni broj jednadžbe; izgleda kao greška prijeloma. | (a) U MathJax konfiguraciji uključiti prelamanje (`output: { displayOverflow: 'linebreak', linebreaks: { inline: true } }`, MathJax ≥ 3.2) ili na ≤ 768 px sakriti oznaku broja (`mjx-labels { display:none }`) i smanjiti `font-size` formula na 0,92 em; (b) dodati desni gradijent kao znak pomicanja (`.math.display { mask-image: linear-gradient(…) }`) ili tanak `scrollbar`; (c) u izvorima najduže jednadžbe oblika `A ⟹ B` podijeliti u dva retka (`\\`) — ne mijenja sadržaj. |
| 2 | `source/u13_gubici_cjevovodi_crpke_i_mreze.md:746, 752, 774, 780, …` (svih šest Z) naspram `source/u01…md:649, 655` i svih ostalih poglavlja. Snimke `u13_1440_el_problem.png` i `u01_1440_el_problem.png`. | U pog. 13 „Smjernica” je `.callout-tip` (zelena), a „Kontrolni rezultat” `.callout-note` (plava); u svim ostalih 14 poglavlja obrnuto (Smjernica plava, Kontrolni rezultat zelena). Izmjereno u `consistency.json`. | Boja je jedini brzi signal koji od dva sklopiva bloka otvoriti; u jednom poglavlju signal se okreće. | U `u13` zamijeniti `.callout-tip`↔`.callout-note` na šest parova (ostaje `data-hint-key`/`data-answer-key`). |
| 3 | `source/u01…md:829`, `u02:874`, `u03:833`, `u04:848` (samo `## Sažetak`); `u05:889+891` i `u13:909+911` (`## Sažetak` i `.mf1-zavrsni-okvir`); u06–u12, u14, u15 (samo `.mf1-zavrsni-okvir` bez odjeljka). | Sažetak poglavlja pojavljuje se u tri oblika: kao numerirani odjeljak u sadržaju (1.6 Sažetak), kao okvir „SAŽETAK” s gornjom/donjom crtom bez stavke u sadržaju, ili oboje (pog. 5 i 13 imaju naslov „5.8 Sažetak” pa unutra još okvir s labelom „SAŽETAK”). | Posljednji commit najavljuje „jedan sažetak po poglavlju”; student u sadržaju „Na ovoj stranici” u pola poglavlja ne vidi da sažetak postoji, a u pog. 5 i 13 vidi dvostruki naslov. | Odabrati jedan oblik za svih 15 poglavlja. Najjednostavnije: svuda `## Sažetak` (ulazi u TOC) i unutar njega okvir bez vlastite labele, ili svuda okvir bez odjeljka. |
| 4 | Blok uz bilježnice: `source/u01…md:142` („Interaktivni prikaz — Hidraulička preša”, `.mf1-interaktivno`, prefiks ▶), `u05:160,433` i `u13:207,271` („Numerički pokus — …” u `.mf1-interaktivno`), `u09:690`, `u12`, `u15` („Numerički pokus — …” u `.mf1-numerika`, prefiks →, drugačija boja), `u10:490` („Numerička perspektiva”, `.mf1-numerika.kompakt`, ljubičasta crta). Tipke: u13 „Pokreni u JupyterLiteu / Pričuvno: Google Colab”, ostala poglavlja „Pokreni u pregledniku / Pričuvno: otvori u Colabu”. Snimke `u01_1440_el_interaktivno.png`, `u09_1440_el_num.png`, `u13_1440_el_interaktivno.png`. | Isti element (poziv na bilježnicu s pitanjima Predvidi/Provjeri) ima tri naziva, dva prefiksa (▶/→), dva stila okvira i dva para oznaka tipki. | Student ne prepoznaje da je riječ o istoj vrsti aktivnosti; recenzent to vidi kao nedovršeno. | Jedan naziv („Numerički pokus — …” je točniji od „Interaktivni prikaz”), jedan razred (`.mf1-interaktivno`), jedan prefiks, iste oznake tipki u svim poglavljima; `.mf1-numerika` zadržati samo za kratke numeričke napomene bez tipki (kao u u10). |
| 5 | `content/book.json:372` (`"catalog_title": "Numerika i CFD V&amp;V"`); prikaz na početnoj stranici, snimka `index_1440_t02.png`, `index_390_t01.png`. | Na početnoj stranici kartica D glasi doslovno „Numerika i CFD V&amp;V”. | Vidljiva tehnička greška na naslovnici. | U `book.json` upisati `V&V` (generator sam escapira) ili, ako generator ne escapira, `&amp;` zamijeniti pravim znakom i provjeriti `scripts/build_book.py`. |
| 6 | `_language.yml:55` (`crossref-apx-prefix: "dodatak"`); naslovi `chapters/d01…html` „dodatak A — Sažetak formula i oznaka”, `d06` „dodatak F — Ključ kontrolnih rezultata”; snimke `d01_1440_top.png`, `d06_390_top.png`. | Naslov stranice dodatka počinje malim slovom. | Naslov H1 malim slovom izgleda kao greška; u PDF-u se vjerojatno isto događa. | Ako se prefiks koristi i u tekstu („vidi dodatak A”), zadržati malo slovo u referencama, a za naslov dodati u `styles/typography.css`: `h1.title::first-letter { text-transform: uppercase; }` samo za stranice dodataka (ili u generatoru omotača naslov dodataka pisati izravno „Dodatak A — …”). |
| 7 | `styles/components.css` `.mf1-ch-ref { display:inline-flex; padding:0 0.3rem; border-bottom:1px dotted }`; primjeri `u06` uvod („… određene su u ␣pog. 5 Hidrostatske sile na ravne i zakrivljene plohe␣; uzgon …”), `u01` („obrađuje se u ␣pog. 3 Hidrostatička raspodjela tlaka i manometrija␣ .”), `u00` „CFD put”. Snimke `u06_1440_top.png`, `u06_390_top.png`, `u01_820_top.png`. Ukupno 95 takvih referenci u knjizi. | Referenca je atomarni inline-flex okvir: ne može se prelomiti pa na 390 i 820 px pada u zaseban redak (ostaje sam „.” ili „; uzgon je …” u novom retku); i na 1440 px ima razmak ispred točke i zarez odvojen od riječi. | Ružan prijelom u svakom poglavlju, osobito na mobitelu; interpunkcija odvojena od riječi. | `.mf1-ch-ref { display:inline; padding:0; }` (ukloniti `gap` i `inline-flex`), a `mf1-ch-code` i `mf1-ch-title` ostaviti kao obične inline spanove; interpunkciju će tada tekst „povući” uz riječ. |

### P2

| # | Gdje | Što | Zašto je problem | Prijedlog |
|---|------|-----|------------------|-----------|
| 8 | `styles/layout.css:10` (`#title-block-header .quarto-title-meta { display:none }`) — pravilo ne djeluje: izmjereno `display != none` na svih 22 stranica; snimke `u01_1440_top.png`, `u06_390_top.png`. | Na vrhu svakog poglavlja i dodatka stoji „AUTORICA / Martina Bašić” iako CSS to želi sakriti. | Na stranici poglavlja ime autorice ponavlja se ispod naslova, u bočnoj traci i u podnožju; troši prostor iznad prvog retka teksta na mobitelu. Nesklad dokumenta (CSS) i rezultata. | Provjeriti zašto pravilo ne pogađa (vjerojatno Quarto ubacuje `style` ili drugo pravilo s većom specifičnošću); riješiti npr. `#title-block-header .quarto-title-meta { display:none !important }` ili u `_quarto.yml` isključiti `author` iz naslovnog bloka poglavlja. Na početnoj stranici meta može ostati. |
| 9 | Početna stranica, vrh: naslovni blok (naslov + podnaslov + AUTORICA/OBJAVLJENO) + `.mf1-eyebrow` „Sveučilišni priručnik · Martina Bašić” + `.mf1-hero` „Razumjeti fluid. …” + bočna traka s naslovom knjige i prvom stavkom istog naslova; snimke `index_1440_top.png`, `index_390_top.png`. | Iznad prvog poziva na akciju ime autorice stoji dva puta, a naslov knjige tri puta (navbar/sidebar, naslov stranice, prva stavka bočne trake). | Dojam natrpanosti; na mobitelu treba 1,5 zaslona do tipke „Počni s osnovama”. | Ukloniti `.mf1-eyebrow` (podatak već postoji u meta bloku) i prvu stavku bočne trake (naslov knjige već je poveznica na početnu). |
| 10 | `styles/base.css` globalno `a { border-bottom: 1px solid … }` — curi u Quarto UI: naslov knjige u navbaru (390/820) i u bočnoj traci (svaki redak podcrtan), GitHub ikona, chevroni za sklapanje grupa u bočnoj traci (narančasta crtica ispod strelice), breadcrumb; snimke `index_390_menu.png`, `index_1440_top.png`, `u01_820_top.png`. | Elementi sučelja izgledaju kao „podcrtane poveznice iz 2005.” | Najvidljiviji detalj koji kvari dojam suvremenosti bočne trake. | Ograničiti pravilo na sadržaj: `main a, #quarto-document-content a { border-bottom… }` i eksplicitno `#quarto-sidebar a, .navbar a, .sidebar-item-toggle, .quarto-page-breadcrumbs a { border-bottom:0 }`. |
| 11 | Razina zadatka: primjeri P1–P6 imaju čip `T1` uz naslov (`.mf1-level`), zadatci Z1–Z6 tekst „Razina: T1” sitno desno ispod callouta (`.mf1-task-level`); snimke `u01_1440_el_we.png`, `u01_1440_el_problem.png`. | Ista informacija prikazana na dva načina; kod Z je najmanje uočljiva, a upravo tamo student bira zadatak po razini. | Neujednačenost P/Z; razina Z zapravo se vidi tek nakon što se zadatak pročita. | Kod Z koristiti isti čip uz naslov (`Z1. Gustoća ulja iz vaganja [T1]`), `.mf1-task-level` ukloniti ili ostaviti samo u ispisu. |
| 12 | Skice-pregledi `assets/…/uNN_fig_uvod_pregled.svg` (prirodna veličina 300×119 do 300×127, prikazane na 607–774 px) naspram skica primjera, npr. `u07_fig_pumpno_kuciste.svg` (139×150 → 774×835 px). Snimke `u06_820_el_figure.png` (oznake `p₁A`, `h₁` ≈ 6–7 px), `u06_1440_t02.png` (naslov u skici ≈ 26 px, skica visoka 835 px). | Oznake na pregledima poglavlja nečitljive su već na 820 px, a na 390 px potpuno (slika široka 300 px); istodobno su portretne skice primjera razvučene preko cijelog stupca pa im je unutarnji naslov veći od H1 stranice i zauzimaju gotovo cijeli zaslon. | Isti element (skica) ima oznake od ~6 px do ~26 px; student na mobitelu mora otvarati „Povećaj skicu” za svaku preglednu skicu. | U `styles/components.css` ograničiti `figure img { max-height: 70vh; width:auto; max-width:100% }` (portretne skice prestaju biti divovske) i za pregledne skice koristiti isti sustav skaliranja tipografije kao u tiskovnim izvedenicama (`docs/ispis-skica.md`: odvojeno skaliranje geometrije i tipografije, min. 9 pt). Za web verziju preglednih skica ponuditi `--1.svg` varijantu s većim oznakama ispod 768 px (već postoji kao `mf1-print-figure`, samo je skrivena). |
| 13 | Potpis `Slika 6.1: Pregled poglavlja: Uzgon, plivanje i stabilitet` (`u06`), analogno u ostalim poglavljima s preglednom skicom. | Dvostruka dvotočka u istom potpisu; skice primjera uz to imaju naslov u samoj slici i u potpisu („Potpuno uronjeno kućište” + „Slika 6.2: Uzgon i težina potpuno uronjenoga…”). | Sitno, ali ponavlja se u 15 poglavlja. | „Slika 6.1: Pregled poglavlja — uzgon, plivanje i stabilitet” (crta umjesto druge dvotočke). |
| 14 | 820 px: desni sadržaj „Na ovoj stranici” prikazuje se u stupcu širokom ~130 px, naslovi se lome u 3–4 retka („1.1 Fluid / kao / kontinuum”), glavni stupac sužen na 607 px; snimke `u01_820_top.png`, `u06_820_top.png`. Pri 820 px i `mathOver` raste (u06: 12). | Na tabletu TOC više smeta nego pomaže. | Uzak stupac s razlomljenim naslovima izgleda neuredno; oduzima širinu formulama. | U `_quarto.yml` ili CSS-u sakriti TOC ispod ~1000 px (`@media (max-width: 999px) { #quarto-margin-sidebar { display:none } }`) ili ga prebaciti u sklopivi gumb kao na 390 px. |
| 15 | 1440 px: stupac teksta 774 px pri 17,5 px serifa; izmjereno ~90–95 znakova u retku (npr. prvi redak uvoda pog. 1 ima 91 znak). (dojam) | Reci su dulji od uobičajenih 65–80 znakova za duži tekst. | Umara pri čitanju dugih odlomaka izvoda. | `--mf1-content-width: 720px` ili `--mf1-font-size: 18.5px` (jedna vrijednost u `design-system/tokens.json`). Provjeriti da široke skice i dalje stanu. |
| 16 | Nazivi obojenih blokova među poglavljima (izmjereno iz `.mf1-box-label`): „Granica modela — Kada stlačivost…” (u01, veliko slovo) / „Granica modela — kad kontinuitet…” (u07, malo) / „Granica modela” bez podnaslova (u13); „Fizikalno značenje” bez podnaslova (u02–u12) / s podnaslovom (u13, u15); blok `.mf1-dublje` bez prefiksa („Izotropnost tlaka: Cauchyjev tetraedar” u01, „Učinak slobodne površine u tanku” u06) / s prefiksom „Dublje — …” (u10) / s prefiksom „Fizikalni temelj — …” (u13); jedini `.mf1-temelj` u u10. | Isti blok nekad nosi prefiks, nekad ne; iza crte nekad veliko, nekad malo slovo. | Student ne može po naslovu prepoznati vrstu bloka (osobito `Dublje`, kojemu je naziv jedini signal uz boju). | Dogovoriti obrazac „Vrsta bloka — Podnaslov” (podnaslov velikim početnim slovom) i primijeniti na sve; blok `.mf1-dublje` uvijek s prefiksom „Dublje —”. |
| 17 | Samoprovjera: `source/u13…md:688` „Konceptualna provjera” naspram „Provjeri sebe” u ostalih 14; odgovori kao jedan callout „Odgovori” (u01–u05, u09, u12, u15) naspram zasebnog callouta „Odgovor” ispod svakog pitanja (u06, u07, u08, u10, u11, u13, u14). | Dva naziva i dva rasporeda istog bloka. | Neujednačenost na kraju svakog poglavlja, gdje se student vraća najčešće. | Jedan naziv („Provjeri sebe”) i jedan raspored (po pitanju „Odgovor” je praktičniji na mobitelu). |
| 18 | `source/u10…md:139` i `u11` (dva mjesta): nesklopivi `.callout-note` s naslovom „Postupak rješenja” u glavnom tekstu. | Plavi callout koji nigdje drugdje ne postoji; u ostalim poglavljima postupak je polje „Rješenje” unutar primjera ili tekst izvoda. | Novi vizualni element samo u dva poglavlja. | Pretvoriti u običan odlomak s podnaslovom `h3.mf1-step` ili u `.mf1-izvod`. |
| 19 | Naslovi odjeljaka: „Zadatci za samostalan rad” (u05, u13) naspram „Zadatci za vježbu” (ostali); u09, u12, u15 nemaju odjeljak „Riješeni primjeri” (primjeri su raspršeni po odjeljcima, pa ih TOC ne pokazuje). | Isti odjeljak s dva naziva; u tri poglavlja TOC ne vodi do primjera, a alatna traka poglavlja („Zadatci za vježbu”) vodi samo do zadataka. | Navigacija nije predvidljiva. | Ujednačiti naslov; za u09/u12/u15 ostaviti raspored, ali u alatnoj traci dodati poveznicu na prvi primjer ili u TOC uključiti razinu primjera. |
| 20 | Tablice na 390 px: `styles/responsive.css` `.mf1-table-scroll .mf1-wide-table { min-width:42rem }` (u04, u07, u11, u12, d04 → tablice široke 693 px), `.mf1-reference-table { min-width:32rem }` (d01, d02 → 528 px); dvostupčana tablica oznaka u dodatku A također se reže (snimka `d01_390_top.png`, stupac „Značenje” odrezan). | Horizontalno pomicanje tablica unutar stranice bez ikakve naznake; u dodatku A, koji je studentu referentan, drugi stupac nije vidljiv. | Na mobitelu najkorisniji dodatak traži vodoravno pomicanje po svakom retku. | Za 2–3 stupčane tablice ukloniti `min-width` (tekst se može prelomiti), `mf1-table-hint` prikazati samo kad tablica doista prelazi širinu; dodati desni gradijent kao znak pomicanja. |
| 21 | QR kod `.mf1-interaktivno-qr` prikazan i na webu uz dvije tipke (snimke `u01_1440_el_interaktivno.png`, `u01_390_el_interaktivno.png`). | QR kod služi tisku; na zaslonu je besmislen (student je već u pregledniku) i razbija redak s tipkama na mobitelu. | Zastarjeli dojam; smanjuje preglednost bloka. | U registru komponenti postaviti vidljivost QR-a samo za `pdf`/`print` (ne uređivati adaptere ručno, prema AGENTS.md). |
| 22 | `chapters/u00_kako_koristiti_udzbenik.qmd:8` „# 0. Kako koristiti priručnik” naspram automatskih „1  Osnove fluida…” (bez točke, s razmakom); vidljivo u bočnoj traci, navigaciji prethodno/sljedeće (`u01_1440_el_nav.png`) i naslovu. | Jedini naslov s „0.” i točkom; ostali brojevi su bez točke. | Sitna, ali stalno vidljiva neujednačenost u navigaciji. | Naslov bez broja („Kako koristiti priručnik”, poglavlje je `.unnumbered`) ili `0  Kako…` istim formatom kao Quarto. |
| 23 | Google Fonts preko `@import` u `styles/tokens.css` (generirano iz `design-system/tokens.json`). | Font se vuče s `fonts.googleapis.com` pri svakom otvaranju. | Bez mreže (ili uz blokadu) tipografija pada na Charter/Georgia; slanje IP-a Googleu nije u duhu CC-BY-NC-SA priručnika za nastavu (GDPR). | Samostalno poslužiti dva fonta (woff2) iz `assets/fonts/` i `@font-face` u tokens.css; nema promjene izgleda. |

### P3

| # | Gdje | Što | Zašto | Prijedlog |
|---|------|-----|-------|-----------|
| 24 | Početna stranica, katalog: `catalog_title` u `content/book.json` („Fluid, svojstva i tlak”, „Reologija i međupovršine”, „Hidrostatika i manometrija”) razlikuje se od naslova poglavlja u bočnoj traci („Osnove fluida i Pascalov zakon”, „Viskoznost, površinska napetost i kapilarnost”…). (dojam) | Student na naslovnici klikne „Reologija i međupovršine”, a stigne u „Viskoznost, površinska napetost…”. | Svjesna odluka, ali zbunjuje. | Ili ujednačiti s naslovima, ili u kartici prikazati pravi naslov, a kratki opis ostaviti u retku ispod. |
| 25 | `chapters/za_ispis.html`: naslov „MF1 — pregled za ispis u pregledniku”, podnaslov „Za pripremljen prijelom stranica preuzmi PDF priručnika” i prvi odlomak iste rečenice; snimke `ispis_1440_top.png`. | Ista rečenica dvaput; kratica „MF1” nigdje drugdje nije u naslovima. | Sitna redundancija. | Zadržati samo odlomak s poveznicom; naslov „Pregled za ispis”. |
| 26 | Dodatak F: „Vrati se na zadatak” ispod svakog od 90 naslova Z (snimka `d06_1440_t06.png`). | Ponavljanje iste poveznice 90 puta kao zaseban redak. | Vizualni šum. | Pretvoriti u malu strelicu/ikonu uz naslov Z (`Z3. Metacentarska visina ↩`). |
| 27 | Tipke „Pokreni u pregledniku” i „Pričuvno: otvori u Colabu” jednako istaknute. (dojam) | Primarni i rezervni put izgledaju jednako. | Student ne zna koji je preporučen. | Rezervni put kao tekstna poveznica ispod tipke. |
| 28 | Poveznice na bilježnice apsolutne (`https://martibasic.github.io/MF1_udzbenik/jlite/…`, npr. `source/u01…md:144`), dok početna stranica koristi lokalni `jlite/lab/`. | Lokalni pregled i svaka kopija stranice odvode na produkcijski URL. | Otežava provjeru prije objave. | Relativna putanja `../jlite/lab/index.html?path=…` (QR i dalje može biti apsolutan). |
| 29 | Nema tamnog načina. (dojam) | Suvremeni Quarto priručnici obično nude svjetlo/tamno. | Nije nužno; tokeni su već centralizirani pa bi bilo jeftino. | Opcionalno `prefers-color-scheme` iz `tokens.json`. |

## 3. Što je dobro i treba ostati

- Paleta i hijerarhija blokova: zelena „Fizikalno značenje”, ljubičasta „Računalna dinamika fluida”,
  smeđa „Granica modela”, narančasta „Matematički izvod”, tanka lijeva crta bez pozadine — blokovi su
  prepoznatljivi, a stranica ostaje mirna (snimke `u06_1440_t06.png`, `u06_1440_t12.png`).
- Primjeri i zadatci bez okvira, s jednakim poljima „Tekst zadatka / Traži se / Rješenje / Provjera i
  tumačenje” u svim poglavljima; sklopivi „Smjernica” i „Kontrolni rezultat” s chevronom rade i na dodir.
- Alatna traka poglavlja („Zadatci za vježbu · Formule i oznake · Kontrolni rezultati”) i „Povećaj skicu”
  uz svaki potpis — koristan, diskretan obrazac.
- Bočna traka s grupama velikim slovima (TEMELJI, STATIKA FLUIDA …) i aktivnom stavkom na blijedoj
  podlozi; navigacija prethodno/sljedeće na dnu.
- Tablice u sans-serifu s tabularnim brojkama i zebrom; jednadžbe centrirane s brojem desno na 1440 px.
- Stranica se na 390 px ne pomiče horizontalno kao cjelina ni na jednoj od 22 stranice; tekst 16,5 px
  sa širinom retka ~45 znakova čita se ugodno (`u01_390_top.png`).
- Početna stranica kao „akademski katalog” (brojevi u narančastoj, naslov sans, opis serif) djeluje
  suvremeno i knjigoliko; impresum i status izdanja jasno su navedeni.

## 4. Što bi se moglo ukloniti ili skratiti bez gubitka

- QR kod u blokovima s bilježnicama (web).
- `.mf1-eyebrow` „Sveučilišni priručnik · Martina Bašić” i meta „AUTORICA” na stranicama poglavlja.
- Prva stavka bočne trake (ponavlja naslov knjige).
- Druga rečenica/podnaslov na stranici za ispis; kratica „MF1” u njezinu naslovu.
- 90 redaka „Vrati se na zadatak” u dodatku F (zamijeniti ikonom).
- Dvostruki sažetak u pog. 5 i 13 (naslov odjeljka + okvir s labelom „SAŽETAK”).
- Naslov unutar SVG-a skice primjera kad je isti kao potpis slike (npr. „Potpuno uronjeno kućište”).

## 5. Provjere i ograničenja

Provjereno: snimke na tri širine za 9 stranica (vrh, cijela stranica u pločama, pojedinačni blokovi,
otvoreni meni na 390 px), automatske mjere na svim 22 stranicama pri 390 i 1440 px (prelijevanje,
formule, tablice, nazivi blokova, vrste callouta, naslovi odjeljaka), ručna provjera izvora za sve
nalaze s brojem retka. Nije provjereno: ponašanje tražilice, tipkovnička navigacija i čitači zaslona,
Safari/iOS (korišten je Edge/Chromium), stvarni rad JupyterLite bilježnica, PDF (druga recenzija).
Snimke cijelih stranica dulje od ~30 000 px (pog. 1 na 390 px) sadrže artefakt spajanja — ponovljeni
vrh stranice pri dnu slike; to nije greška weba. Nalazi 15, 24, 27 i 29 su dojam, ne izmjerena greška.
