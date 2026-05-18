# SVG TODO za Codex — Faza 1.5 (obogaćivanje primjera)

Kreirano: 2026-05-18

Ovaj dokument popisuje **11 novih SVG datoteka** koje treba dizajnirati za primjere uvedene u Fazi 1.5 (didaktičko obogaćivanje). Svaka stavka opisuje:
- naziv datoteke u `assets/print/`
- ID figure-bloka (`#fig-...`) referenciran iz source markdowna
- ključne **vizualne elemente** koje skica treba prikazati
- **kanonsku paletu** (boje, kote, srafura) – kao u dosadašnjim SVG-ovima poglavlja

Svi SVG-i moraju pratiti standard iz [`protokol_prerade_zadataka_i_skica.md`](protokol_prerade_zadataka_i_skica.md):
- bez SVG-level naslova (caption u Markdownu)
- prefiksirani ID-evi (npr. `u01k...`, `u02lt...`, itd.) – može se naknadno provesti `tools/svg_normalize.py`
- font `'Segoe UI',Arial,sans-serif`, responsive root atributi
- paleta: ulazna sila crvena `#c0392b`, izlazna zelena `#1e8449`, tlak plava `#1565c0`, kote smeđa `#b7600c`, srafura siva `#7a8a96` (45°)

---

## 1. U01 — Hidraulična kočnica vozila

- **Datoteka**: `assets/print/u01_fig_kocnica_vozila.svg`
- **ID**: `#fig-u01-kocnica-vozila`
- **Tekst zadatka**: source/u01_*.md, P "Hidraulična kočnica vozila"

**Što skica mora pokazati**:
- Kočna papučica s polugom prijenosa $i = 5$ (lijevo) – F_n = 300 N crvena strelica
- Glavni kočni cilindar (d_M = 20 mm) – tlak p plava strelica
- Dvije razvodne grane od glavnog cilindra: prednje (2× d_f = 35 mm) i stražnje (2× d_r = 30 mm)
- 4 kočna cilindra prikazana sa kočnim diskovima, F_f i F_r zelene strelice (izlazne sile)
- Brojevi: F_n = 300 N (crvena), p ≈ 4,77 MPa, F_f ≈ 4,59 kN, F_r ≈ 3,38 kN, F_uk ≈ 15,9 kN
- Naglasak: jedan ulaz → 4 izlaza različitih veličina (poruka razdvajanja)

---

## 2. U02 — Klizni ležaj pri dvije temperature

- **Datoteka**: `assets/print/u02_fig_lezaj_temperatura.svg`
- **ID**: `#fig-u02-lezaj-temperatura`
- **Tekst zadatka**: source/u02_*.md, P "Hladni start i radna temperatura"

**Što skica mora pokazati**:
- Dva panela rame-uz-rame: lijevo "Hladni start" ($T = 0°$C, $\mu_1 = 0{,}40$ Pa·s), desno "Radna temperatura" ($T = 90°$C, $\mu_2 = 0{,}040$ Pa·s)
- Svaki panel: presjek kliznog ležaja (vratilo + uljni procjep δ = 0,30 mm + kućište)
- Profil brzine u procjepu (linearno od 0 do v na svakom panelu) – istim nagibom (iste geometrije!)
- Vektorske strelice smičnih naprezanja τ, **različitih duljina** (lijevo 10× dulja od desne)
- Iznosi: $\tau_1 \approx 8{,}38$ kPa, $\tau_2 \approx 838$ Pa; $P_1 \approx 578$ W, $P_2 \approx 58$ W
- Naglasak: ista geometrija, faktor 10 u $\mu$ daje faktor 10 u snazi trenja

---

## 3. U03 — Balastni tank broda

- **Datoteka**: `assets/print/u03_fig_balastni_tank.svg`
- **ID**: `#fig-u03-balastni-tank`

**Što skica mora pokazati**:
- Presjek trupa broda u sredini broda (poprečni rez)
- Vanjska morska voda na gazu $T_g = 8{,}5$ m (s desne i lijeve strane trupa)
- Unutarnji balastni tank visine $H_t = 5$ m (otvoren prema atmosferi gore, srafiran ili svjetloplavi)
- Promatračev prozor na visini $h_p = 2$ m iznad dna tanka
- Plave strelice tlaka koje upadaju u stijenku iz oba smjera (vanjska veće za faktor $T_g/H_t$)
- Brojevi: $p_{ext,dno} \approx 85{,}5$ kPa (vani), $p_{int,dno} \approx 49{,}1$ kPa (iznutra)
- Naglasak: razlika tlakova (neto opterećenje stijenke) razlikuje se za **prazno** vs **puno** stanje tanka

---

## 4. U05 — Tri sloja fluida na vertikalnoj plohi

- **Datoteka**: `assets/print/u05_fig_tri_sloja.svg`
- **ID**: `#fig-u05-tri-sloja`

**Što skica mora pokazati**:
- Vertikalna pravokutna ploha širine $b = 0{,}80$ m, visine $L = 1{,}50$ m, gornji rub na dubini $h_0 = 0{,}30$ m
- Tri sloja fluida različitih boja: ulje (svijetlo žuto-zlatno, $\rho_u = 820$), voda (plavo, $\rho_w = 998$), glicerin (tamnije, $\rho_g = 1260$)
- **Profil tlaka** desno od plohe – izlomljena linija s 3 segmenta, različitih nagiba (ključna vizualna poruka)
- Slobodna površina ulja, granica ulje/voda (na 0,80 m), granica voda/glicerin (na 1,50 m)
- Iznosi sila po sloju: $F_1 \approx 1{,}77$ kN, $F_2 \approx 5{,}52$ kN, $F_3 \approx 3{,}63$ kN, $F \approx 10{,}9$ kN
- Hvatište $h_{CP} \approx 1{,}25$ m od slobodne površine

---

## 5. U06 — Plinski jastuk iznad četvrtkruga

- **Datoteka**: `assets/print/u06_fig_plinski_jastuk.svg`
- **ID**: `#fig-u06-plinski-jastuk`

**Što skica mora pokazati**:
- Zatvoreni cilindrični spremnik (presjek)
- Gornji dio: **plinski jastuk** (svjetla siva ili svjetla žuta) pri pretlaku $p_g = 200$ kPa, s oznakom $p_g$
- Slobodna površina ulja unutar spremnika
- Donji dio: ulje ($\rho = 860$, svijetlo žuto)
- **Četvrtcilindrični poklopac** na bočnoj stijenci, $R = 0{,}50$ m, $b = 1{,}20$ m (vidljiv u presjeku)
- Strelice ulja koje pritišću plohu **plus** dodatne ravnomjerne strelice plinskog tlaka (preneseni kroz ulje)
- $F_H$ i $F_V$ označene zasebno, s razdvojenim doprinosima ulja i plina: $F_{H,o} \approx 1{,}27$ kN + $F_{H,g} = 120$ kN
- Rezultanta $F \approx 172$ kN pod kutom $\approx 45^\circ$

---

## 6. U07 — Asimetrično poplavljen tank broda (CH T4)

- **Datoteka**: `assets/print/u07_ch2_poplavljen_tank.svg`
- **ID**: `#fig-u07-poplavljen-tank`

**Što skica mora pokazati**:
- Brod poprečni rez: $L = 80$ m (u tlocrtu manje važan; rez je poprečni), $B = 15$ m, $H = 8$ m
- Originalan gaz $T_0 = 3{,}25$ m i novi gaz $T_1 = 3{,}48$ m (oba prikazana)
- Lijevi balastni tank (dimenzije 15 × 6 × 3 m) – poplavljen, s oznakom $m_w = 277$ t
- Težište broda $G_b$ na osi (zelena točka)
- Novo težište sustava $G'$ pomaknuto $e_G \approx 0{,}29$ m lijevo od osi (crvena točka)
- Centar uzgona $B'$ na novom gazu
- Metacentar $M$ iznad $B'$, s GM = 4,23 m
- Bočni nagib $\theta \approx 4°$ prikazan na cijelom trupu (lijevo niže, desno više)
- Brojevi: $e_G$, GM, $\theta$, novi gaz $T_1$, freeboard na lijevoj strani

---

## 7. U09 — Difuzor (povratak tlaka)

- **Datoteka**: `assets/print/u09_fig_difuzor.svg`
- **ID**: `#fig-u09-difuzor`

**Što skica mora pokazati**:
- Vodoravni difuzor: uži ulaz $A_1 = 0{,}010$ m² (lijevo), širi izlaz $A_2 = 0{,}035$ m² (desno)
- Strujnice koje pokazuju usporavanje toka (raščlanjuju se i ravnaju)
- Profil brzine ulaz/izlaz (lijevo brzo $v_1 = 15$ m/s, desno sporije $v_2 = 4{,}29$ m/s)
- Profil tlaka **inverzno** – ulaz nizak $p_1$, izlaz visok $p_2$, razlika $\Delta p \approx 103$ kPa (idealno)
- Brojevi: $Q = 150$ L/s, $\Delta p_{ideal} \approx 103$ kPa, $\Delta p_{real} \approx 82{,}6$ kPa (uz $\eta = 0{,}80$)
- Naglasak: pretvorba kinetičke energije u statički tlak (simetrija konfuzora iz prvog primjera)

---

## 8. U10 — Starenje cijevi i $\lambda$

- **Datoteka**: `assets/print/u10_fig_starenje_cijevi.svg`
- **ID**: `#fig-u10-starenje-cijevi`

**Što skica mora pokazati**:
- Dva panela: lijevo "Svježa cijev" ($\varepsilon = 0{,}045$ mm), desno "Nakon 10 godina" ($\varepsilon = 0{,}20$ mm)
- Svaki panel: presjek cijevi $D = 80$ mm, $L = 150$ m (skraćeno za prikaz)
- Lijevi panel: glatka unutarnja stijenka; desni panel: korodirana, hrapava, taloženja
- Detalji povećanja u "lupi" koja pokazuje $\varepsilon$ (visina hrapavosti) na svakoj cijevi
- Po jedan mali Moodyjev dijagram (ili kvalitativna karta $\lambda$ vs $\varepsilon/D$ za isti Re) gdje je istaknuto $\lambda_{nova} \approx 0{,}020$ i $\lambda_{stara} \approx 0{,}026$
- Brojevi: $\Delta E \approx 1000$ kWh/god dodatne energije
- Naglasak: ista geometrija, ista brzina – razlika **samo** u $\lambda$ → dovodi do +30% gubitka snage

---

## 9. U11 — Vodeni udar (CH T3)

- **Datoteka**: `assets/print/u11_ch3_vodeni_udar.svg`
- **ID**: `#fig-u11-vodeni-udar`

**Što skica mora pokazati**:
- Dugačka horizontalna cijev $D = 150$ mm, $L = 200$ m (skraćeno)
- Ventil na desnom kraju, prikazan u tri faze zatvaranja (paneli)
- Lijevo: stupac ulja koji teče brzinom $v_0 = 2{,}83$ m/s (plava strelica)
- Tlačni val (crveni "front") koji putuje natrag brzinom $c = 1200$ m/s
- Prirubnica na ventilu s 4 vijka M16, na kojima se vidi naprezanje
- Graf na strani: $\Delta p$ vs $\Delta t$ (Joukowsky linija + Michaud krivulja), s tri točke za $\Delta t = 0{,}20$, $1{,}0$ i $5{,}0$ s
- Brojevi: $\Delta p_a = 2{,}95$ MPa (brzo), $\Delta p_c = 197$ kPa (sporo), F_a = 52 kN, T_ref = 0{,}33 s
- Naglasak: 15× razlika sile zbog brzine zatvaranja

---

## 10. U12 — Krivulja snage $P(u)$ Peltonove turbine (CH T3)

- **Datoteka**: `assets/print/u12_ch4_krivulja_snage.svg`
- **ID**: `#fig-u12-krivulja-snage`

**Što skica mora pokazati**:
- **Glavni element**: graf $P(u)$ vs $u$ (parabola s maksimumom)
- Apscisa: $u$ od 0 do $c_1 = 30$ m/s, ordinata: $P$ od 0 do $P_{max} \approx 24{,}7$ kW
- Označen $u_{opt} = c_1/2 = 15$ m/s, $P_{max}$
- Tri suboptimalne točke: $u/c_1 = 1/4, 1/3, 2/3$
- Dva ruba: $u = 0$ (lopatica stoji) i $u = c_1$ (lopatica "bježi") – oba P = 0
- Mali insert: shema Peltonove lopatice s $\beta_2 = 165°$, mlazom $c_1$
- Brojevi: $u_{opt}$, $P_{max}$, $\eta_{max} = 93{,}6\%$, $n_{opt} \approx 716$ min⁻¹
- Naglasak: univerzalan oblik krivulje – izbor $n$ rotora prirodno slijedi iz $c_1$

---

## 11. U13 — Radna točka crpka⇄cjevovod (CH T4)

- **Datoteka**: `assets/print/u13_ch2_radna_tocka.svg`
- **ID**: `#fig-u13-radna-tocka`

**Što skica mora pokazati**:
- **Glavni element**: graf $H$ vs $Q$ s dvije krivulje
  - $H_p(Q) = 25 - 0{,}0175 Q^2$ (parabola crpke, pada s $Q$)
  - $H_{s,0}(Q) = 6 + 0{,}0303 Q^2$ (parabola sustava, otvoren ventil, raste s $Q$)
  - $H_{s,1}(Q) = 6 + 0{,}0464 Q^2$ (parabola sustava, zatvoren ventil)
- Apscisa $Q$: 0 do 40 L/s; ordinata $H$: 0 do 30 m
- Dvije radne točke: točka 1 na presjecištu $H_p$ i $H_{s,0}$ ($Q_{op,1} \approx 20$ L/s, $H_{op,1} \approx 18$ m); točka 2 na presjecištu $H_p$ i $H_{s,1}$ ($Q_{op,2} \approx 17{,}2$ L/s, $H_{op,2} \approx 19{,}8$ m)
- Strelica koja pokazuje pomak radne točke "ulijevo i uvis" kad se zatvori ventil
- Mali insert: shema sustava (spremnik → cijev → potrošač, s regulacijskim ventilom istaknutim)
- Brojevi: $Q_{op,1}$, $H_{op,1}$, $P_{el,1} \approx 4{,}70$ kW; $Q_{op,2}$, $H_{op,2}$, $P_{disip,vent} \approx 0{,}81$ kW

---

## Sažeti popis datoteka

| # | Datoteka | Razina | Vrsta | Primarna poruka |
|---|----------|--------|-------|-----------------|
| 1 | `u01_fig_kocnica_vozila.svg` | T2 P | strojarski | Pascalov zakon na 4 cilindra različitih veličina |
| 2 | `u02_fig_lezaj_temperatura.svg` | T2 P | strojarski | Viskoznost ovisi o temperaturi (faktor 10) |
| 3 | `u03_fig_balastni_tank.svg` | T2 P | strojarski | Neto tlak na stijenku tanka (vanjski vs unutarnji) |
| 4 | `u05_fig_tri_sloja.svg` | T2 P | osnovni | Tlak izlomljena linija kroz 3 sloja |
| 5 | `u06_fig_plinski_jastuk.svg` | T2 P | osnovni | Plinski tlak + hidrostatika na zakrivljenoj plohi |
| 6 | `u07_ch2_poplavljen_tank.svg` | T4 CH | brodogradnja | Stabilnost broda nakon asimetričnog poplavljenja |
| 7 | `u09_fig_difuzor.svg` | T2 P | osnovni | Inverz konfuzora – pretvorba brzine u tlak |
| 8 | `u10_fig_starenje_cijevi.svg` | T2 P | strojarski | $\lambda$ raste s vremenom, snaga crpke s njom |
| 9 | `u11_ch3_vodeni_udar.svg` | T3 CH | strojarski | Brzo vs sporo zatvaranje, 15× razlike u tlaku |
| 10 | `u12_ch4_krivulja_snage.svg` | T3 CH | energetika | $P(u)$ parabola, $u_{opt} = c_1/2$, $\eta_{max}$ |
| 11 | `u13_ch2_radna_tocka.svg` | T4 CH | strojarski | Presjecište karakteristika crpka⇄sustav |

---

## Postupak nakon kreiranja SVG-a

Nakon što Codex dizajnira SVG, izvršiti:

1. Pokrenuti `tools/svg_normalize.py` da se prefiksiraju ID-evi, popravi font i aria – idempotentno, neće ništa dirati ako je već čisto.
2. Verifikacija u `tools/preview_server.py` (http://localhost:8765/preview.html).
3. `quarto render` puni build (kad Quarto CLI postane dostupan).
