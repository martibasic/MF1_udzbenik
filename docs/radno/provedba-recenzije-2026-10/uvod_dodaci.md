# Provedba: uvodni dio, dodatci i urednički dokumenti (`uvod_dodaci`)

Datoteke: `source/index.md`, `source/u00_kako_koristiti_udzbenik.md`, `source/d01…d05*.md`,
`references.bib`, `docs/urednicki_stil.md`. `docs/autorski_ugovor.md` nije trebalo mijenjati
(odluka o jednom sažetku već je zapisana u r. 18–20). D06 nije diran.

## 1. Provedeni nalazi

### Početak knjige (D2; struktura #3, #24, #25; jezik #9, #23; pdf #6, #23)
- `index.md`: uklonjeni „O priručniku” (`#sec-o-prirucniku`), „Numerički pokusi”
  (`#lajtmotivi-i-numerika`) i prazno sidro `<span id="o-udžbeniku">` (bilo je duplikat
  sidra iz u00). `git grep` ne nalazi upućivanja na njih (osim generiranog `assets/content-index.json`).
- Typst-only odlomak sveden na jednu rečenicu ispod naslova.
- Impresum: autorica; naslov; **Ustanova:** Sveučilište u Splitu, Fakultet elektrotehnike,
  strojarstva i brodogradnje (FESB); **Verzija:** 1.0 (rukopis za recenziju), listopad 2026.;
  licenca; ISBN / DOI: u pripremi. Uklonjen redak „Status” i poveznice na protokol recenzije i
  pilota; zadržana errata u jednoj rečenici („Potvrđene … pogreške te njihovi ispravci vode se uz
  stabilni ID sadržaja u javnoj errati.”).
- u00 „O priručniku” sada je jedino mjesto s publikom i primjenama (preneseno iz indexa, bez
  ponavljanja); uklonjen redak „CFD put” (#24); „osnovno gradivo MF1” → „osnovno gradivo priručnika”.
- u00 (stari r. 69): „Smjernice i kontrolni rezultati nalaze se u dodatku F; mrežno izdanje ih
  prikazuje i uz sam zadatak.” (#35)
- u00 (stari r. 74): uklonjena rečenica o „kratkim primjerima / cjelovitim zadatcima” (#23).
- u00: naslovi dodataka usklađeni s `book.json` (C „Tipične pogreške po poglavljima”, E „Literatura”).
- u00 dodatno (bez novog sadržaja): stavka 5 opisuje novi oblik sažetka (odluka 1); stavka 3 kaže
  da primjeri stoje uz teoriju ili u zasebnom odjeljku (struktura #38, pdf #28); odlomak o
  bilježnicama navodi „Interaktivni prikaz” / „Numerički pokus” (odluka 5) i da prvo pokretanje
  traži mrežu i minutu-dvije (skice_i_interaktivno #21).

### Dodatak A (D01)
- Uklonjen prvi `##` (ponavljao naslov); uvodni odlomak dobio rečenicu da A ne zamjenjuje postupke
  zadataka.
- Jedinice $k$, $\varepsilon$, $\omega$, $I_t$, $\ell$, $m$: m²/s²; m²/s³; s⁻¹; -; m; - (P1 #7 / S11).
- Uklonjeno sedam zadatkovnih redaka (#16): kormilarski stroj $M=2Fr$, $V=2As$; igla $p_{M,1}$,
  $p_{M,2}$; tlačni mjerač + ullage $U=H_{ref}-h_v-h_u$; tank u zavoju $\Delta h=v_s^2b_t/(R_zg)$;
  separator $r_i^2$; parabolični segment $A=HL/3$; $BM_{eq}$.
- Dodano (#17): $p=\rho RT$, $p/\rho^\kappa=\text{konst.}$ (pog. 9); $I_G$ pravokutnika, kruga i
  trokuta (pog. 3–6).
- Iznimke oznaka (U12; sadrzaj_u06_u10 #38; u11_u15 #10, #43): $K$ (kobilica u pog. 6) — „samo to
  značenje” uklonjeno; $M$ (metacentar u pog. 6); novi redak „$k$ (iznimke)”: rang matrice i
  $(1+k)$ ITTC (pog. 11), $w_2=kw_1$ (pog. 14); $R$ hidraulički otpor $h_g=RQ^2$ (pog. 13);
  $v_s$ brzina u usisnom presjeku (pog. 13).
- Novi redak $p_b$; $p_e$; $p_{0,M}$ (#29).
- $\sigma_{kr}$: referentno mjesto $p_{ref}=p_1$ (ulaz), $v_{ref}=v_2$ (grlo) — provjereno prema u11 r. 538
  i izvodu ($1-(A_2/A_1)^2$ vrijedi samo uz $v_{ref}=v_2$) (#29).
- Froudeova sličnost: snaga u istom smjeru, $P_m/P_p=(\rho_m/\rho_p)\lambda_L^{-7/2}$ (#28).
- $m_se$ → $m_ke$, uz opis „uteg mase $m_k$ pomaknut poprečno za $e$” (#18; odluka 8).
- „podkritični” → „potkritični” (#6); „vertikalno ubrzanje/vertikalna” → „okomito/okomita” (#21);
  „Bernoulli” → „Bernoullijeva jednadžba” (2×); ullage → „ulaž (engl. *ullage*)…”;
  ustava $\sqrt{2gy_1}$ → $\sqrt{2gy_0}$ uz $y_0$ u tablici oznaka (odluka 8, S5);
  α=2 uz ogradu „razvijeni laminarni profil u kružnoj cijevi”; $\alpha,\beta$ opisani nazivima iz
  poglavlja (korekcijski faktor kinetičke energije / količine gibanja).

### Dodatak B (D02)
- Uklonjen prvi `## Pojmovnik`.
- Abeceda (#13): „No-slip uvjet” → „Uvjet prianjanja (no-slip)” pod U; „Reynoldsov broj” i RTT ispred
  „Rezidual”; ispravljen i „Afinitetni” ispred „Aktuatorski”, „Korekcijski…” ispred „Korelacijska”.
- Rubni pojmovi (#14): „Boussinesqov koeficijent” → „Korekcijski faktor količine gibanja”
  (naziv iz u10/u14; Boussinesq u zagradi u definiciji; odredište 10, 14 — u15 ga ne imenuje);
  „Coriolisov koeficijent” → „Korekcijski faktor kinetičke energije” (naziv iz u08/u15);
  „Preekspandirani i podekspandirani mlaz” → „Preekspandirani mlaz” (podekspandirani se u knjizi ne
  pojavljuje); „MRF i klizajuća mreža” → „MRF i klizna mreža (engl. *sliding mesh*)”; „Odbitak potiska”,
  „Pridružena masa”, „Statvena cijev”, „Inertni plin”, „Stimulator”, „Metoda dodane težine” ostavljeni jer
  se u poglavljima pojavljuju.
- Dodano šest jednorečeničnih natuknica (#15): Bernoullijeva jednadžba (8), Darcy–Weisbachova
  jednadžba (13), Peltonovo kolo (10, 14), Sifon (8), Meniskus (2), Afinitetni zakoni (13).
- „Zahvatni usis (sea chest)” → „Usisni koš (engl. *sea chest*)” s napomenom da je otvor u oplati
  zahvatni usis (odluka 7); odredišta 7, 8, 13. „Ullage” → „Ulaž (engl. *ullage*)”, „ulažnog otvora”.
- „Vertikalna komponenta…” → „Okomita komponenta…” (pod O); „vertikalnu plohu/sondnu cijev” → „okomitu”.
- Validacija / Verifikacija: jedna rečenica; uputa premještena u stupac Odredište
  (`d04…qmd#sec-cfd-venturi`) (#30).
- „Kormilarski stroj”: uklonjeni $M=2Fr$, $V=2As$ (isti postupak zadatka kao uklonjeni redak u A).
- Naziv datoteke `u05_hidrostatske_…qmd` u poveznicama ostaje (ime datoteke se ne mijenja); u tekstu
  B nema „hidrostatske”.

### Dodatak C (D03)
- Uklonjen prvi `##` i svi „čipovi” (15 redaka) te rečenica koja ih najavljuje (#11, V6). CSS
  `.mf1-signal-chip/.mf1-signal-note` u `styles/components.css` ostaje mrtav — nije moje područje.
- Uklonjeni „Kako koristiti pregled” (`#namjena-tablice`, nema upućivanja), okvir „Najčešća
  pogreška” i „Operativna namjena dodatka”; zadržani „Kriteriji provjere rješenja”, u četvrti korak
  prenesena jedina nova misao (vrati se skici, geometriji, referentnim veličinama, pretpostavkama) (#12).
- α=2 uz ogradu „za razvijeni laminarni tok u kružnoj cijevi”.
- Naslovi pog. 2 i 5 usklađeni s naslovima poglavlja („Viskoznost, površinska napetost i
  kapilarnost”; „Hidrostatičke sile na ravne i zakrivljene plohe”); ID-jevi nepromijenjeni.
- „centar uzgona” već dosljedan; `h<sub>g</sub>` nestao zajedno s čipovima.

### Dodatak D (D04)
- Uklonjen prvi `##` „Mehanika fluida i numerika — pregled”.
- Pojmovnik kratica (#27): naslov „Dodatne kratice numeričkih metoda”; zadržani FVM, LES/DNS, VOF,
  zidne funkcije / $y^+$, GCI; uklonjeni FEM, RANS, $k$–$\varepsilon$/SST, SIMPLE/PISO/PIMPLE, MRF uz
  uputu na B.
- Brojevi na 4 značajne (#31): $C_D\approx0{,}01222$ i $C_D\approx0{,}01166$ (10-znamenkasti zapisi
  uklonjeni; provenijencija ostaje u `teaching_comparison.json` i `tools/validate_cfd_vv.py`).
- README poveznice (#31): stupac piše „paket `…`”; uvodna rečenica upućuje na mapu `data/cfd/` u
  GitHub repozitoriju (apsolutna poveznica, radi i u PDF-u).
- „Veza sa Z6 u []{.mf1-chapter-ref target="u12"}”; točka-zarez s razmakom u parovima.
- Bernoulli u rječniku: $p/(\rho g)+v^2/(2g)+z=\text{konst.}$ (`\text`, #20), redak „Bernoullijeva jednadžba”.
- „MF1” u tekućem tekstu i naslovima (V9): „Rječnik priručnik → CFD”, „Pojam iz priručnika”,
  „jednadžbe priručnika”, „primjeru iz priručnika”, „gradiva kolegija Mehanika fluida 1”,
  „preduvjet za ovaj priručnik”, „Priručnik uči…”. Eksplicitni ID-jevi i stara sidra ostaju.
- „horizontalni” → „vodoravni”. Završni okvir: callout zadržan s vlastitim naslovom
  „Završna poruka dodatka” (više nije „Sažetak”).

### Dodatak E (D05) i `references.bib`
- Uklonjen prvi `##` „Literatura i izvori”.
- Dopune: `anderson2021` address New York; `schlichting2017` address Berlin, Heidelberg;
  `pope2000` address Cambridge; `imo-is-code-2008` note: „IMO ga izdaje i u konsolidiranom izdanju 2020.”

### `docs/urednicki_stil.md`
- „$B$ samo središte istisnine” → „$B$ samo centar uzgona”; „$K$ samo volumni modul” → s iznimkom.
- Novi odjeljak „Odluke završne recenzije (16. listopada 2026.)”: oblik sažetka, početak poglavlja,
  odjeljak zadataka, „Provjeri sebe”, blokovi uz bilježnice, pravopis i nazivlje (potkritični/
  natkritični, vodoravno/okomito, min⁻¹, ulaž, usisni koš, klizna mreža, Bernoullijeva jednadžba,
  `\text{konst.}`, bez „MF1”), notacija ($A$, HGL/EGL, točka-zarez, $m_k$, $y_0$, $p_{0,M}$), poznate
  iznimke $K$, $M$, $k$, $R$, $v_s$, pravilo za dodatke.

## 2. Nalazi koje nisam proveo i zašto
- Izdanja White/Munson/Çengel (#22, V8) — ostavljeno autorici (odluka 11).
- Godine za `virag`, `nasa-wind-boundaries`, `tmr-backstep` i mjesto izdanja za `streeter` — ne
  znam ih sigurno; ostavljeno autorici.
- CSL navodnici „…“ (V8, jezik #7), redoslijed citata (P3 #37) — izvan područja.
- `book.json` (naslov pog. 5 „Hidrostatske”, „V&amp;V”), `_language.yml` „dodatak” malim slovom,
  „0. Kako koristiti” u omotaču, naslovnica i raspored impresuma u Typstu (T6) — izvan područja.
- Izotermna atmosfera i Youngova jednadžba u A (#17 „po želji”) — nisu dodane (brief traži samo
  navedene relacije).
- P3 #36 (tip `Temelj` u ugovoru) — autorska odluka; ugovor nije mijenjan.
- P3 #32 (poveznice na D iz CFD blokova poglavlja), #34 (ID-jevi uvodnih slika u `docs/arhitektura.md`)
  — izvan mojih datoteka.
- Za ostale agente (usklađivanje s izmjenama u dodatcima):
  - u14 r. 142 „klizajuća mreža” → „klizna mreža” (B i D sada pišu „klizna”).
  - u08 „usisna košara” → „usisni koš (engl. *sea chest*)” (odluka 7); B to već koristi; u07
    „zahvatni usis” B opisuje kao otvor usisnog koša.
  - Sukob oznake: odluka 8 uvodi $H_s$ za visinu stepenice (u12 P6), a A (pog. 13) koristi
    $H_s(Q)$ za karakteristiku sustava u radnoj točki. Preporuka: za stepenicu $h_{step}$ ili $H_{stp}$,
    ili u u12 izričito uvesti $H_s$ kao lokalnu oznaku.
  - u06/D06 trebaju $m_k$ (A sada piše $m_k e$).
  - u15 i D06: $y_0$ za uzvodnu dubinu ustave (A sada piše $\sqrt{2gy_0}$).
  - `styles/components.css` `.mf1-signal-chip`/`.mf1-signal-note` više se ne koriste.

## 3. Potrebne izmjene skica
Nema (dodatci i uvod nemaju SVG skica).

## 4. Promijenjeni brojevi i verifikatori
- D04: samo prikaz zaokruživanja ($0{,}01222408822$ → $\approx0{,}01222$; $0{,}01166089$ →
  $\approx0{,}01166$). Rezultat Z6 pog. 12 i `tools/validate_cfd_vv.py` nepromijenjeni; verifikator
  poglavlja nije pogođen.
- D01: nijedan brojčani rezultat nije promijenjen (samo oblik omjera snage i referentno mjesto $\sigma_{kr}$).

## 5. Rezultat provjera
- Kontrolni znakovi (ord < 32): nema ni u jednoj od 9 uređenih datoteka.
- `tools/audit_publication.py`: FAIL samo zbog „duplicirani stabilni ID #zadaci-za-: U02…U14” —
  posljedica izmjena naslova zadataka u poglavljima (drugi agenti; vjerojatno regex ID-ja reže
  `vježbu` na dijakritiku), nije od mojih datoteka. Struktura: 90 primjera, 90 zadataka, 23 citata, 145 sati.
- `tools/audit_architecture.py`: FAIL „Generated book files are stale: d06…, styles/tokens.css” —
  očekivano (D06 i generatori na kraju).
- `tools/test_book_model.py`: 1 neuspjeh (`#mf1-task-level` u Typst izlazu) — posljedica tuđe izmjene
  filtra, ne mojih datoteka.
- `git grep` za uklonjena sidra (`sec-o-prirucniku`, `lajtmotivi-i-numerika`, `namjena-tablice`,
  auto-ID-jevi uklonjenih naslova): upućivanja nema osim u generiranom `assets/content-index.json`.
- Render nije pokretan (nije dopušteno briefom).
