# Provedba nalaza recenzije na skicama (studeni 2026.)

Izmijenjeni su samo kanonski SVG-ovi u `assets/print/`, logički izrezi i hashevi
u `assets/print-layouts.json`, tri recepta u `assets/figure-compositions.json`
i tri provjere geometrije. Tiskovne izvedenice u `assets/pdf-figures/` obnovljene
su generatorom. `source/`, `tools/verify_*`, `notebooks/` i `scripts/` nisu dirani.
Commit nije napravljen.

## Zajedničke provjere (nakon svih izmjena)

| Provjera | Rezultat |
|---|---|
| `node tools/build_print_figures.mjs` (puni prolaz) | 92 figure obnovljene, `manifest.json` obnovljen, zastarjela `u05_vjezbe_skice--4.svg` uklonjena |
| `node tools/audit_print_layouts.mjs` | PASS: 92 kanonska SVG-a, 190 izreza, 2027 oznaka; bez preklapanja oznaka i odsijecanja, oznake ≥ 9 pt, indeksi ≥ 6,5 pt |
| `python tools/audit_sketch_design.py` | PASS: 92 figure, 39 kontrolnih granica |
| `check_u02`, `u04`, `u05`, `u08`, `u10`, `u11`, `u13`, `u14`, `u15` `_sketch_geometry.py` | svi PASS |

Generator mjeri samo preklapanje teksta s tekstom, ne teksta s crtama. Zato sam
za svaku izmijenjenu izvedenicu dodatno pokrenuo pomoćnu skriptu u scratchpadu.
Ona iscrta skicu bez teksta i u okviru svake oznake broji tamne piksele crta,
šrafura i kota. Sve izmijenjene skice pregledao sam i kao PNG, i kanonski SVG
i tiskovnu izvedenicu. Puni render PDF-a i `scripts/check_publication.py` nisu
pokrenuti. Dvije figure prelaze u WIDE format (stavke 1 i 3), pa treba provjeriti
broj stranica konačnog PDF-a prema rasponu 290–355.

## 1. G2-39: preklapanja oznaka (sl. 5.8, 8.5, 8.7)

**Uzrok.** Generator zadržava oznake od 9 pt dok se geometrija smanjuje. Dugi
retci podataka zato se uz desni rub guraju ulijevo preko kota i stijenki. Kad
jedan panel u retku ima sukob oznaka, susjedni panel pada u MINI širinu.

**sl. 5.8, `assets/print/u05_vjezbe_skice.svg`**

- U Z1 je u polovičnoj širini nastajao sukob, pa je Z2 bio stisnut u MINI.
  Popravak u Z1: podatci su u kraćim retcima (`b`, `H`, `ρ`, `h₁`, `Fₓ = ?`).
  „pogled s naplavljene strane; suha strana: zrak” prelazi u napomenu ispod
  skice, a izrez Z1 je produljen.
- Z2: podatci su u kraćim retcima, a stupac je odmaknut od kote `H`. Iz retka
  `b = 1,50 m` uklonjeno je „(okomito)” jer to već kaže napomena
  „b: okomito na presjek”. Ta je napomena spuštena ispod dna, a izrez produljen.
- Z4: stupac podataka pomaknut je desno od kote `H`, a izrez proširen.
- Z6: kota `H` prenesena je na lijevu stranu kao lančana kota uz `h₁`; mjeri
  iste razine kao prije. Podatci su u zasebnim retcima s većim razmakom.
- Z5: oznaka `F_s` pomaknuta je s dna posude uz vrh svoje strelice.
- Rezultat: sva tri retka imaju po dva panela polovične širine. Preklapanja s
  crtama nema. Slike pregledane.

**sl. 8.5, `assets/print/u09_ch1_bypass_sifon_suzenje_mlaz.svg`**

- Recept `rows: [["wide"]]` u `figure-compositions.json`, s obrazloženjem.
  U STANDARD formatu ova složena shema imala je oko 10 oznaka preko crta.
- Kota `z_P` premještena je na istu okomicu kao kota balasta (lančana kota na
  x = 620). Oznake obiju kota stoje lijevo od kotne crte.
- `Q = 180 m³/h` stoji iznad izlazne strelice crpke, a „u rashladni sustav”
  ispod nje, ne više preko kote `z_P`.
- „dno trupa” odmaknut je od napomene o usisnom košu i više ne leži na limu.
- Slike pregledane (kanonska i tiskovna); preklapanja nema.

**sl. 8.7, `assets/print/u09_vjezbe_skice.svg`**

- Z2: podatci imaju veći razmak redaka. „otvoren spremnik” prelazi u napomenu
  ispod spremnika, a izrez je produljen. Z1 tako više nije stisnut u MINI.
- Z1: `H` i `3,20 m` poravnati su desno uz kotnu crtu.
- Z6: `z_C =` / `1,7 m` poravnati su desno uz kotu. `Δz = 2,6 m` stoji lijevo
  od kote. `p_atm =` / `101,3 kPa` ima dva retka, desno od posude i lijevo od
  silazne grane cijevi. `D = 70 mm (uvećano)` spušten je ispod dna.
- Z4: oznake kote `Δz_S` stoje lijevo od kotne crte, iznad dna trupa.
- Z3: `v₂` je malo spušten. U receptu `spatial_text` [25, 26, 28, 29] drži
  `v₂`, „1”, `D₁` i `D₂` uz njihove presjeke; prije su postajali naslov ili
  podnožje panela.
- Recept: `canvas_insets_pt` lijevo 16 pt za Z1 i Z6, s obrazloženjem. Indeksi
  u `spatial_text` vrijede za sadašnji redoslijed `<text>` elemenata.
- Slike pregledane; preostaje dodir od oko 3 u² između `p_atm =` i desne
  stijenke posude u Z6, vizualno prihvatljiv.

## 2. G3-14: sl. 10.1, `assets/print/u11_fig_uvod_pregled.svg`

- Oznaka „1” stoji uz donji kraj isprekidanog ulaznog presjeka. Iznad presjeka
  generator ju je pretvarao u naslov na sredini slike.
- `F_G`: provjerio sam da je nacrtana točka (226,2; 222,4) stvarno težište
  L-ispune fluida u KV. Ona leži uz unutarnju stijenku zavoja, zato se činilo
  da strelica polazi sa stijenke. Hvatište i cijela strelica sada su na istom
  okomitom pravcu kroz težište (x = 226,2), unutar fluida (y od 160 do 217),
  a oznaka `F_G` je uz strelicu. Moment težine ostaje isti.
- `<desc>` sada navodi da `F_G` djeluje na okomitom pravcu kroz težište i da je
  hvatište nacrtano unutar fluida.
- `tools/check_u10_sketch_geometry.py` je pojačan. Provjerava da strelica `F_G`
  leži na pravcu kroz izračunato težište, polazi iz označenog hvatišta i gleda
  prema dolje. Hvatište i vrh moraju biti u fluidu, odmaknuti od stijenke
  (stara skica ne bi prošla). PASS. Slike pregledane.

## 3. G3-15: sl. 11.4, `assets/print/u14_val3_venturi_kavitacija.svg`

- Recept `rows: [["wide"]]`, s obrazloženjem. U STANDARD formatu razmak oznaka
  osi bio je manji od visine oznake, pa je generator razmicao „50” i „0” na isti
  redak. U WIDE formatu podjela osi je ravnomjerna.
- Isprekidana crta `p_v` već je bila na stvarnoj razini 2,34 kPa, neposredno
  iznad 0. Oznaka sada glasi `p_v = 2,34 kPa` i stoji iznad crte unutar grafa,
  pa se ne čita kao razina 0.
- „p₂ prema modelu” i „izvan jednofaznog modela” premješteni su izvan krivulje,
  desno od isprekidanog dijela.
- Oznaka `D₂ = 20 mm` stoji ispod grla, a ne na stijenci difuzora. `D₁ = 60 mm`
  je odmaknut od gornje stijenke. Kotna crta `D₂` i dalje točno spaja unutarnje
  stijenke, kako traži provjera.
- `check_u11_sketch_geometry.py` PASS. Slike pregledane.

## 4. G3-35: sl. 10.9, Z3, `assets/print/u11_vjezbe_skice.svg`

- Uklonjena je neoznačena tlačna strelica na izlazu 2, u skladu s napomenom
  „izlazni tlak nije nacrtan”. `<desc>` sada kaže da je izlazni tlak označen
  upitnikom i da nije nacrtan strelicom.
- `v₂` stoji lijevo uz svoju strelicu, na sredini.
- Strelica `g` premještena je u gornji desni kut, daleko od kote `Δz` i oznake
  `p_M2`. Izrez Z3 je neznatno proširen.
- `check_u10_sketch_geometry.py` PASS. Slike pregledane.
- Ostala preklapanja u Z1, Z4 i Z6 ispravljena su naknadno (stavka 11).

## 5. G1-11: sl. 4.1, `assets/print/u04_fig_uvod_pregled.svg`

- Na lijevom panelu oznaka kote `L` zamijenjena je s `b_t` (indeks `tspan`).
- `<desc>`: „b_t je širina tanka mjerena prema središtu zavoja.”
- `check_u04` PASS. Slika pregledana.

## 6. G1-12: skica ležaja, `assets/print/u02_fig_lezaj_temperatura.svg`

- Oznake su promijenjene s „0 °C” na „10 °C” i s „90 °C” na „50 °C”, uz
  zadržani nelomljivi razmak. Viskoznosti i ostali brojevi nisu mijenjani.
- `<desc>`: „pri 10 °C deset je puta veće”.
- `check_u02` PASS. Slika pregledana. Natpis „nepomična čahura” na šrafuri
  ispravljen je naknadno (stavka 11).

## 7. G1-30: `assets/print/u02_ch1_kapilarni_mikrodozator_kapljica.svg`

- Indeks oznake `h_cap` promijenjen je u `h_kap`. ID-jevi elemenata
  (`u02ch1_capHeight`) zadržani su kao stabilni.
- `<desc>` dosad nije imao oznaku visine. Sada glasi „prirodni uspon h_kap”.
- `check_u02` PASS. Slika pregledana.

## 8. G4-16: sl. 15.2, Z4, `assets/print/u15_vjezbe_skice.svg`

- Uzvodna dubina `y₁ = 1,200 m` sada je `y₀ = 1,200 m`. Radi dosljednosti s
  uvodnom slikom, uzvodna brzina `v₁` sada je `v₀`. `E₁` na skici ne postoji.
  Dubine skoka u Z5 nisu dirane. ID-jevi (`u15ex_z4y1`) su zadržani.
- `tools/check_u15_sketch_geometry.py`: dodana je provjera da Z4 ima `y0` i
  `v0`, a nema oznaka `y1` ni `v1`. PASS. Slika pregledana.

## 9. Sl. 13.2, `assets/print/u10_fig_uvod_pregled.svg`

- **Uzrok.** Generator tekst ispod donjeg ruba geometrije razvrstava kao
  podnožje i centrira ga ispod panela. Oznake „2” i `p_M,2 = 0` bile su ispod
  dna spremnika (y = 326), pa su završile pod sredinom cijevi.
- **Popravak.** Dodana je tanka vodilica (`data-mf1-role="leader"`) od donjeg
  ruba izlaznog presjeka prema dolje. Ona produljuje geometriju, a „2” desno i
  `p_M,2 = 0` lijevo od nje sada ostaju prostorne oznake uz izlaz. Oznake `v`
  u glavnoj cijevi i u koljenu premještene su uz rep strelice, sa stijenke.
- `check_u13` PASS. Slike pregledane.

## 10. G4-09: sl. 14.5, `assets/print/u12_val3_pokretna_lopatica.svg`

- **Prije.** Stare lopatice imale su kontrolnu točku na 0,8 % tetive od kraja.
  Kut na samom kraju bio je formalno točan, ali je lopatica izgledala ravno,
  pod oko 64°.
- **Sada.** Šest lopatica je kvadratnih Bézierovih krivulja u istom stilu
  (crta 2,2, ista boja), unatrag zakrivljenih i namotanih 85° suprotno vrtnji.
  Tangenta na r₁ daje β₁ = 20,52° iz podataka (atan(c_m1/u₁)), a na r₂ daje
  β₂ = 25°. Polumjer raste monotono, a kut duž lopatice ostaje između 20° i
  34°. Za usporedbu, logaritamsko-linearna spirala s istim kutovima namotava
  se oko 107°.
- Izlazni trokut nije mijenjan; provjera potvrđuje `w₂` pod β₂ = 25°. Mala
  strelica „radijalno ↑” odmaknuta je od teksta.
- `tools/check_u14_sketch_geometry.py` je pojačan. Oba kraka kontrolnog
  poligona moraju biti dulja od 0,25 tetive, a namatanje unatrag 60–120°.
  Polumjer duž lopatice mora monotono rasti. Stare lopatice imale bi omjer
  krakova 0,008 i ne bi prošle. PASS. Slike pregledane.

## 11. Dopuna: preostala preklapanja (na zahtjev koordinatora)

**sl. 10.9, `assets/print/u11_vjezbe_skice.svg`**

Z5 nije diran (`F_o = 120 N`, `u = ?`). Između `u = ?` i strelice ostaje
dodir od 2,3 u², vizualno prihvatljiv.

- **Z1.** `v_j = 32 m/s` premješten je desno od krmenog zrcala, ispod strelice
  mlaza; više ne leži na stijenci ni na crti VL. „sapnica” je ispod njega.
  „dno trupa” i „krma” spušteni su ispod lima, a „krma” je poravnata desno.
  `v_s = 18 m/s` odmaknut je od svoje strelice.
- **Z4.** `y_C = 0,35 m` zakrenut je uz okomitu kotu, između nosača i kotne
  crte. Tekst oznake ostaje isti, kako traži `check_u10`. „O” je poravnat
  desno uz točku O, uz šrafirano uklještenje. „uklještenje” je malo podignut.
- **Z6.** `D₃ = 80 mm` poravnat je desno, lijevo od kote. `p_M3 = 0` premješten
  je lijevo od izlaznog presjeka 3, s osi `y`. „60°” stoji ispod-lijevo od
  vrha kuta, a ne na stijenci. `v₁` je lijevo od svoje strelice, kao `v₂`.
  `D₁` i `D₂` stoje na istoj visini ispod stijenki, pa ih generator čuva kao
  prostorne oznake.

**Skica ležaja, `assets/print/u02_fig_lezaj_temperatura.svg`**

- Naslovi `10 °C` / `50 °C` podignuti su na y = 80. „nepomična čahura: v = 0”
  je na y = 106, iznad šrafure. Prije je generator zbog sukoba s naslovom
  spuštao natpis na čahuru.
- Usput je uklonjeno preklapanje „osovina” sa strelicom `u` (oznaka je
  poravnata ulijevo). Uklonjeno je i preklapanje `M₁, M₂` s kružnom strelicom
  momenta (oznaka je desno od strelice).

**Provjere.** Puni `build_print_figures.mjs` je prošao, kao i
`audit_print_layouts.mjs` (PASS, oznake ≥ 9 pt) i `audit_sketch_design.py`
(PASS). `check_u02` i `check_u10` su PASS; `check_u10` je nepromijenjen.
Pomoćna provjera ne nalazi tekst preko crta u ove dvije figure, osim navedenog
dodira. Slike su pregledane (kanonske i tiskovne).

## 12. Sl. 14.7 i sl. 10.9 (glavni agent, nakon pregleda PDF-a)

- Sl. 14.7 Z1 i sl. 10.9 Z2: `v_A` pomaknut udesno, više ne leži na rubu strujne cijevi.
- Sl. 14.7 Z2: `v = 30 m/s` ispod mlaza, ne na njegovu rubu.
- Sl. 14.7 Z6: uklonjen natpis „dva vodoravna dovoda” jer je ležao na nosačima;
  dovode pokazuju strelice prema unutra, a tekst zadatka (simetrični vodoravni dovodi)
  i opis skice to navode. `v = 36 m/s` stoji ispod trećeg mlaza (brzina je jednaka u svim
  mlazovima), jer generator ne pušta oznaku preko desnog ruba panela.
- Ostavljeno: `u = 10 m/s` u sl. 14.7 Z2 dodiruje crtkanu ploču kola; između ploča nema
  prostora za pomak.

## Napomene za tekst (drugi agent)

- Sl. 5.8 Z2 više ne piše „(okomito)” uz `b = 1,50 m`; to kaže napomena ispod
  skice. U Z1 su „pogled s naplavljene strane” i „suha strana: zrak” spojeni u
  jednu napomenu.
- Sl. 15.2 Z4 sada koristi `v₀` uz `y₀`. Tekst Z4 ne spominje `v₁`, pa usklađivanje
  nije potrebno.
- Sl. 11.4 sada navodi brojčanu vrijednost `p_v = 2,34 kPa`, jednaku podatku u
  tekstu (2340 Pa).

## Ograničenja

- CI i provjere potvrđuju geometriju, minimalne veličine i preklapanja oznaka.
  Didaktičku kvalitetu i ukupni dojam treba pregledati u konačnom PDF-u.
- Generator gubi kurziv kad je postavljen na samom `<text>`, a ne na `tspan`;
  to se vidi npr. na `v` i `h_g` u sl. 13.2. To je postojeće ograničenje
  generatora i nije mijenjano.
