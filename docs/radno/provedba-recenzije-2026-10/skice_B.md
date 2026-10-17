# Provedba skica B — datoteke u08_*–u15_* (pog. 7–15)

Područje: 48 referenciranih SVG-ova s prefiksom u08–u15 u `assets/print/` i provjere
`tools/check_u08_sketch_geometry.py` i `tools/check_u10_sketch_geometry.py`. Tiskovni sustav,
`assets/print-layouts.json`, `assets/pdf-figures/`, `source/` i git nisu dirani.
Kopije izvornika prije izmjena: `scratchpad/skB/orig/`; renderi prije/poslije: `scratchpad/skB/before|after/`.

## 1. Serijske izmjene (svih 48 datoteka)

- **Kurziv simbola (pravilo 1).** Skriptom `scratchpad/skB/italic.py` pa ručnim pregledom svih ~450
  izmijenjenih oznaka: simboli veličina (latinična i grčka slova, *Re*, *Ma*, *Fr*, *We*, *St*, *NPSH*)
  dobili su `font-style="italic"`. Indeksi, jedinice, riječi, nazivi tvari, oznake točaka i presjeka
  (A, B, 1, 2, P, S, O), Z1–Z6, KV, EGL/HGL te operator d (u d*h*/d*t*, d*p*, d*τ*) i Δ, Σ ostali su
  uspravni. Vektori ostaju podebljani, a sada su i kurzivni. U podebljanim oznakama oblika „**v** = 24 m/s”
  (pog. 14) podebljan je samo simbol, a broj i jedinica više nisu. U pog. 7 (stariji „kurzivni dijalekt”)
  uklonjen je kurziv s cijelih rečenica („kontrolni volumen (KV)”, „voda: ρ = …”, „bilo koji proces”,
  „kontrolna ploha KP”), a indeksi su uspravni.
- **Unicode indeksi (pravilo 2):** u ovih 48 datoteka nije nađen nijedan Unicode indeks ₀–₉. Eksponenti ², ³, ⁻¹
  ostaju. U `u12_val3` sam tspan-eksponent „m<sup>3</sup>” zamijenio s „m³”.
- **Naslovi u jednoprizornim skicama uklonjeni** (prazan prostor obrezan `viewBox`-om, a `max-width` usklađen):
  u08_fig_t_komad („Razvod ulja”), u08_val1, u08_val3, u09_ch1, u09_egl_hgl („Idealni konfuzor”),
  u09_val2, u09_val3, u10_fig_hidroenergetsko_koljeno, u11_fig_uvod_pregled („Sile na fluid”), u11_val1,
  u11_val2, u11_val_rotirajuca_mlaznica, u12_fig_relativni_dotok, u12_val3, u13_ch1, u13_fig_uvod_pregled,
  u14_val1 („Voda i ulje”; „VODA/ULJE” → „voda/ulje”), u14_val3 (naslov sveden na oznaku „*Q* = 6,0 L/s”),
  u14_val4 („Kap vode u zraku”).
- **„tlocrt” u obliku „… (tlocrt)”**, mala uspravna oznaka umjesto velikog naslova: u11_ch1 „T-račva (tlocrt)”,
  u11_ch2 „Y-račva (tlocrt)”, u11_val3 „Koljeno 90° (tlocrt)”, u12_val1 „Vodilica (tlocrt)”,
  u11_vjezbe Z3 „*Q* = 0,026 m³/s (tlocrt)”. U skicama u10_hidro i u11_rot naslov je uklonjen jer potpis počinje riječju „Tlocrt”.
- **Nazivi panela** u višepanelnim skicama svedeni su s 15–18 na 14 (u09_fig_uvod_kompresibilni, u10_fig_uvod,
  u12_fig_uvod_pregled, u12_fig_uvod_realni_tok, u15_fig_uvod).

## 2. Ciljane izmjene po datoteci

- **u14_fig_uvod_pregled (Slika 11.1):** uklonjen je lijevi panel „Usporedi mehanizme” s praznim trakama i naslov
  „Model u aerotunelu”. Ostao je samo aerotunel (`viewBox="322 123 288 172"`), a `<title>`/`<desc>` su prepisani.
  Geometrija i ID-jevi koje provjerava `check_u11` nisu mijenjani.
  **Koordinator treba unijeti u `source/u11_*.md`** tekst iz `provedba/u11.md` §3: r. 9 → „Slika [-@fig-uvod-u14]
  prikazuje model automobila u aerotunelu s jednolikim dotokom, ispitan pri $Re_m=Re_p$, odnosno pri jednakom
  Reynoldsovu broju modela i prototipa.”; potpis → „Model automobila u aerotunelu pri jednakom Reynoldsovu broju
  modela i prototipa.”; `fig-alt` → „Model automobila u aerotunelu s jednolikim dotokom.”
- **u12_fig_uvod_pregled (Slika 14.1): lijevi panel NIJE uklonjen**, jer ga tekst izričito opisuje
  (`source/u14_*.md` r. 9: „Lijevi dio slike … prikazuje jednu pokretnu lopaticu …”, a potpis i fig-alt također).
  Uklanjanje bi tražilo promjenu teksta, a to je odluka autorice. Provedeno je samo „krug: simbol crpke” → „crpka”.
- **u08_fig_uvod_pregled (7.1):** komora je premještena uz desni rub KV-panela (i dalje „desno gore”, kako piše tekst),
  a naslov „Kontrolni volumen” uklonjen. Platno je smanjeno s 924×393 na 900×262. „bilo koji proces / uređaj” →
  „bilo koji proces ili uređaj” (lijevo poravnato, dalje od oznake KV), a „ρ1, A1, v1” odmaknuto od isprekidane granice (pdf #21).
- **u09_fig_uvod_pregled (8.1):** `<title>` „Energijska jednadžba i Bernoulli” → „Energijski stupci u suženju i
  uzlazni tlačni dovod”. U `desc` je „energetska” → „energijska”. Lijevi panel je zbijen (drugi stupac x 362 → 290)
  i dobio je brojčanu visinsku os 0–8 m (`u09intro_axis`, data-mf1-role="axis"), pa nalaz „bez brojčane osi”
  više ne vrijedi. Visine stupaca (8×36) nisu mijenjane. Desni panel je primaknut, a širina je 852 umjesto 934.
  Oznake z, p/(ρg), v²/(2g) više nisu podebljane (skalari).
- **u11_ch2_y_racva:** reakcija `u11ch2_reaction` i `u11ch2_reactiony` je s nagiba 625/664 prebačena na 625/665
  (y = 399,2105263); `desc` „horizontalne” → „vodoravne”.
- **u11_fig_uvod_pregled (10.1):** razmaknute su oznake **R**st→f,x (desno od vrha x-strelice) i **R**st→f,y (desno od vrha y-strelice).
- **u11_ch1:** `desc` „horizontalne T-račve” → „vodoravne”. **u11_val1:** „nepomicne” → „nepomične”.
- **u11_val_rotirajuca_mlaznica:** uklonjena je proza „mlazovi izlaze na atmosferski tlak; os vrtnje u točki dovoda”
  (već u tekstu zadatka, r. 797), a „glava; n = 60 min⁻¹ (reduktor koči)” → „*n* = 60 min⁻¹”.
- **u11_vjezbe:** „1” i „*p*M1 = 180 kPa” u Z3 više se ne preklapaju.
- **u09_ch1 (usisni vod):** „usisna košara (sea chest)” → „usisni koš (engl. *sea chest*)”, „otvorena” → „otvoren”.
  `desc` je usklađen („usisni koš otvoren je…”, „Rešetka koša”). Proza je skraćena: „mirna površina: … z = 0” →
  „*p*A = *p*atm, *v*A ≈ 0”; „vodna linija u balastu, 1,5 m niže” → „vodna linija u balastu”; „referenca z = 0 (vodna linija)”
  → „*z* = 0 (vodna linija)”; dva retka gubitka → „*h*g = 1,2 m (gubitak voda)”, jer je popis u tekstu r. 431.
  Riješeno je preklapanje „P” s „ulaz u crpku: paps,P = ?”, a oznaka je sad „*p*aps,P = ?”. Oznake više ne prelaze kotu *z*u.
- **u09_egl_hgl:** `<title>` „horizontalnom” → „vodoravnom”, a „u zajedničkoj skali” → „u zajedničkom mjerilu”.
- **u09_kompresibilni_vjezbe:** Z6 „Mjerenja prije i poslije vala” → „Mjerenja ispred i iza vala”, a u `desc` „prije vala”
  → „ispred vala”. Z5 „pb = 100 / kPa(abs)” → „*p*b =” / „100 kPa(abs)” (broj i jedinica u istom retku). Popravljena su dva
  zbijena para redaka (Z2, Z6).
- **u09_fig_uvod_kompresibilni (9.1):** „A*, Ma = 1” je odmaknut od stijenke grla, „p0, T0” od ulaznog ruba, a nazivi
  panela su svedeni na 14.
- **u12_fig_relativni_dotok:** uklonjeni su proza „Presjeci iz kontinuiteta; brzine u zajedničkom mjerilu.” (već u „Veza s
  proračunom” P5) i naslov.
- **u12_ch2:** „Radijus r” → „Polumjer r”. **u12_val1:** „dubinu 14 mm” → „visinu sapnice 14 mm”.
  **u12_vjezbe:** „u istoj skali” (2×) → „u istom mjerilu”, a Z6 „v = 36” / „m/s” u dva retka → „**v** = 36 m/s” u jednom retku.
- **u13_ch1 (13.3):** uklonjene su rečenica „Promjeri uvećani …; λ = 0,022 …” (već u tekstu, r. 492 i zadatak) i naslov.
  „obilazni smjer, Q > 0” sad je u dva retka unutar petlje, dalje od unutarnjeg ruba. Oznake *Q*D i *Q*C
  podignute su dalje od strelice i slova D/C.
- **u13_fig_uvod_pregled:** spremnici A i B sada imaju šrafuru presjeka na svijetloj podlozi (novi `u13net_wallhatch`)
  umjesto tamnog punog obrisa, a cijevi zadržavaju obris. Naslov „Serijsko-paralelna mreža” je uklonjen.
- **u13_mreze_vjezbe:** u Z6 oplata broda ima šrafuru presjeka (`u13ex_wallhatch`), vod zadržava obris, a „crpka (simbol)”
  → „crpka”. U Z2 „isti Q za A i B”: A i B su nazivi fluida, pa su ostali uspravni.
- **u14_val4:** `desc` „g je vertikalno prema dolje” → „g je usmjeren okomito prema dolje”, a „Početna kuglasta kap” → malo slovo.
- **u14_vjezbe:** razmaknuti su retci *b*m / *a*m.
- **u15_vjezbe (15.2):** Z1 „Tok i valovi prema obali” → „… u odnosu na obalu”, a Z4 „podkritični” → „potkritični”.
  Z6 je razdijeljen u dva retka: „bazen: *b*baz = 5,00 m (okomito na sliku)” i „*Q*d = 8,00 m³/s”, bez završne točke, pa
  „m³/s.” više ne može ostati sam u retku. „A” (površina) u Z3 promijenjen je iz podebljanog u kurziv. U Z1 *v* ± *c* više nisu podebljani (skalari).
- **u15_fig_uvod:** `desc` „nadkritični/podkritični” → „natkritični/potkritični” (kao u tekstu), a „istu vertikalnu skalu” → „isto okomito mjerilo”.
- **u08 (pog. 7):** u08_vjezbe `<title>` „Zadaci” → „Zadatci”, a „prebačajnom crpkom” → „crpkom za pretakanje”.
  U u08_ch1 je `<title>` „Izjednačni spremnik s miješanjem: …”. U u08_kontrolni_volumen_scene je „Miješajući spremnik ima” →
  „Spremnik s miješanjem ima”. U u08_val3 je proza skraćena („KV vezan uz brod”, „daleko od broda: *v* = 0”, „rešetka: ψ = 0,55 (shematski)”).

## 3. Neprovedeno / napomene za koordinatora

- u12_fig_uvod_pregled, lijevi panel: zadržan (vidi gore). Ako ga autorica želi ukloniti, treba prepisati r. 9, potpis i fig-alt u `source/u14_*.md`.
- `u08_fig_kinematika.svg` nije mijenjan, jer ga koristi naslovnica (izrez u `mf1-book.typ`). Nereferencirani SVG-ovi
  (u14_fig_odluka, u14_fig_pi_buckingham, u10_ch*, …) nisu uređivani.
- Skice pog. 7 (u08_vjezbe, osnovna veličina 9–10) i ploče Z1–Z6 nisu sustavno povećavane na 11–12, da se ne bi
  stvorile nove kolizije. Tiskovni generator ionako normalizira oznake na 9–9,5 pt.
- **Tiskovni rasporedi:** izmijenjenim skicama promijenio se SHA1, a mnogima i broj ili redoslijed `<text>`
  elemenata (uklonjeni naslovi i proza, Z6 u15 sada ima jedan redak više, u09_uvod ima 5 oznaka osi više) te
  `viewBox` (u14_fig_uvod, u08_fig_uvod, u09_fig_uvod i 17 obrezanih). Koordinator treba pregledati panele i
  indekse teksta u `assets/print-layouts.json` i kompozicijama te obnoviti izvedenice.
- Rečenice za tekst: nijedna nova nije potrebna. Sva uklonjena proza već postoji u tekstu zadatka ili u „Vezi s
  proračunom” (provjereno: u08 r. 431, u10 r. 797, u13 r. 492, u14 P5). Iznimka je Slika 11.1 (tekst iz u11.md, vidi gore).

## 4. Promjene u provjerama (jednako stroge)

- `tools/check_u08_sketch_geometry.py` r. 218: stupci u09_fig_uvod traže se na x `('145','290')` umjesto `('145','362')`,
  i dalje uz uvjet zbroja 8×36.
- `tools/check_u10_sketch_geometry.py` r. 212: nagib reakcije `625/665` umjesto `625/664` (tolerancija 1e-8 je zadržana).

## 5. Rezultati provjera

- `check_u07` … `check_u15_sketch_geometry.py`: svih 9 PASS.
- `audit_sketch_design.py`: PASS (exit 0; „SVG design PASS: 92 figures”). U jednom međuprolazu pao je
  `check_u02` (Unicode „F₁” u skici drugog agenta). To nije moje područje, a kasniji puni prolaz je čist.
- Provjera okvira teksta (Playwright/Edge, `scratchpad/skB/bbox.mjs`): u 48 datoteka nema preklopljenih oznaka ni
  teksta izvan `viewBox`-a. Vizualno su pregledani renderi svih izmijenjenih uvodnih slika, P-skica i ploča.
- Ograničenje: CI i geometrijske provjere ne dokazuju didaktičku kvalitetu. Kurziv je postavljen heuristikom i
  pregledan oznaku po oznaku u ispisu, ali tiskovni PDF nije renderiran (to je posao koordinatora).
