# Pregled NE-SVG crteža: bilježnice i inline crteži (13. 10. 2026.)

Opseg: 17 bilježnica `notebooks/*.ipynb` (matplotlib grafovi, sheme i tri interaktivna
laboratorija: `u04_paraboloidna_povrsina`, `u09_venturi`, `u12_poiseuille_konvergencija`)
te inline crteži u `web/`, `filters/`, `includes/`, `components/`.

## Inline crteži izvan bilježnica

Grep (`canvas|<svg|getContext|createElementNS|mermaid|tikz`) nad `web/`, `filters/`,
`includes/`, `components/` i `source/` ne nalazi nijedan crtež. `web/reading.js` spominje
„print canvases” samo u komentaru o skaliranju. `filters/mf1-typst-author-blocks.lua` čita
SVG samo radi provjere SHA-1 sažetka. Mermaid i TikZ ne postoje. **Status: nema što pregledati.**

## Način rada i provjere

- Bilježnice su spremljene **bez izlaza**; izvornici nisu prepisani izlazima. Izvršene kopije
  su u `$S/skice/nb_out/{orig,new}`, PNG-ovi u `$S/skice/png_nb/{orig,new}`. Laboratoriji su
  renderirani izravnim pozivom `draw_*` funkcija (`$S/skice/render_labs.py`), za početni i
  granični slučaj te slučaj s usporedbom A.
- Prije izmjene provjereno: `test_interactive_labs.py` uspoređuje zajedničku ćeliju
  `mf1-lab-common` u tri laboratorija (nije dirana), a `test_experimental_reference.py`
  provjerava podatke `backstep` u u12 (nisu dirani).
- Izmjene su napravljene skriptom koja čuva izvorni JSON format: provjereno je da prolaz kroz
  JSON bez izmjene daje bajt-identičnu datoteku (indent=1, UTF-8, LF/CRLF, završni redak).
  Recenzentske izmjene u u01, u02, u11 i u13 ostale su netaknute. Razlika prema sigurnosnoj
  kopiji `$S/skice/nb_backup` sadrži samo navedene retke crteža.
- Stanje nakon izmjena: `tools/test_interactive_labs.py` 12/12 OK;
  `tools/execute_notebooks.py --validate-only` 17/17; `tools/execute_notebooks.py` (puno
  izvršenje u čistim kernelima) ok=17, fail=0; `tools/test_experimental_reference.py` 7/7 OK.
  Sve izmijenjene slike pregledane su nakon ponovnog izvršenja.
- Brojevi, modeli, `assert` provjere i markdown tekst bilježnica nisu mijenjani. Promijenjene su
  samo oznake osi i legendi, legende, boje jedne crte, debljine strelica i položaj strelica u
  shemi Venturija.
- Stil vektora: u bilježnicama vektori (u11 poligon, u12 trokuti brzina, Venturi) koriste
  postojeće matplotlib boje po vrsti (u/w/c; tlak/stijenka/tok količine gibanja). Standard
  `#356b83` vrijedi za SVG pa nova shema boja nije uvedena. Brzine i sile razlikuju se samo
  oznakom i bojom unutar pojedinog grafa.

---

### u01_hidraulicna_presa — U01 — osnovni scenarij Z3 i Z4

**c04, `u01-osjetljivost` (F₂/F₁ i s₂/s₁ prema D₂/D₁, dvostruka os)**
- a) Graf prikazuje dobitak sile (raste s kvadratom) i omjer pomaka (pada s kvadratom). Tekst:
  $F_2=F_1A_2/A_1$, $s_2=s_1A_1/A_2$.
- b) Problem: dvije krivulje i dvije osi bez legende. Obje oznake su postavljene u kodu, ali se
  ne prikazuju, a imena osi nemaju simbole. Iz slike se ne vidi koja krivulja pripada kojoj osi.
- c) Pri D₂/D₁=3 graf daje 9 i 1/9 (Z3: 900 N, 10 mm) ✓.
- e) Oznake: `F_2/F_1`, `s_2/s_1`, `D_2/D_1` = tekst ✓.
- **Ispravak:** obojene oznake osi sa simbolima i zajednička legenda. **Provjera:** PNG pogledan ✓.
  **Status: ispravljeno.**

**c08, `u01-review-08` (pogreška pomaka prema početnom volumenu)**: točka Z4 (250 cm³; 2 %) i
kriterij 1 % odgovaraju tekstu (r. 741) ✓. **Status: provjereno, bez promjene.**

### u02_kapilarni_uspon — U02 — P3, Z5, Z6

- **c04 (konvergencija bisekcije)**: os pogreške u m ✓. **Bez promjene.**
- **c11, Z5 (τ prema dv/dy)**: podatci A i B odgovaraju tablici u tekstu (r. 807–808); linija
  pogrešne ekstrapolacije prolazi ishodištem ✓. Problem: osi bez simbola, a tekst koristi
  $\tau$ i $dv/dy$ (r. 27). **Ispravak:** `smično naprezanje $\tau$`, `gradijent brzine $dv/dy$`.
  **Ispravljeno.**
- **c13, Z6 (pretlak prema promjeru kapljice)**: tekst (r. 848) navodi regulatore 0–0,50 kPa i
  0–0,60 kPa. Legenda je glasila „gornja granica regulatora” i „drugi regulator”, što je
  dvosmisleno i neravnopravno. Osi nisu imale simbole $p_{M,2}$ i $D$ (r. 860). Krivulja 555–591 Pa
  odgovara rezultatu (r. 866) ✓. **Ispravak:** obje granice imenovane rasponom; dodani
  simboli $D$ i $p_{M,2}$. **Ispravljeno.**

| oznaka na grafu (prije → poslije) | tekst | status |
|---|---|---|
| naprezanje → smično naprezanje $\tau$ | $\tau$ | ispravljeno |
| gradijent brzine → … $dv/dy$ | $dv/dy$ | ispravljeno |
| drugi regulator → gornja granica regulatora 0–0,50 kPa | 0–0,50 kPa | ispravljeno |
| pretlak spremnika → … $p_{M,2}$; promjer kapljice → … $D$ | $p_{M,2}$, $D$ | ispravljeno |

### u03_diferencijalni_manometar — U03

**c04 (p_A−p_B prema Δh za tri gustoće)**: pravci kroz ishodište s nagibom $(\rho_2-\rho_1)g$.
Predznak odgovara dogovoru ($\Delta h>0$ kada je desna razdjelnica viša, $p_A>p_B$). Hod po
stupcima je provjeren ručno ✓. Problem: legenda je koristila $\rho_m$, dok markdown bilježnice
piše $\Delta p=(\rho_2-\rho_1)g\Delta h$. U poglavlju U03 $\rho_m$ znači gustoću **mora**
(r. 489), pa je oznaka dvoznačna. **Ispravak:** $\rho_m$ → $\rho_2$. **Status: ispravljeno.**

### u04_paraboloidna_povrsina — U04 (laboratorij „rotation”)

- **c09 (konvergencija integracije)**: prvi red, osi i jedinice ✓. **Bez promjene.**
- **Laboratorij `draw_rotation`**: stijenke na ±R, dno, paraboloid
  $z=h_0-\omega^2R^2/(4g)+\omega^2r^2/(2g)$. Volumen je očuvan, a za stanje „limit” oblik se ne
  crta ✓. Donji graf prikazuje razinu na osi i uz rub do prve granice ✓.
  Problem: presjek nije u jednakom mjerilu osi. Vodoravno je oko 0,24 m/in, okomito oko
  0,75 m/in, pa je visina sabijena otprilike 3× i nagib paraboloida izgleda blaži. Osi su
  brojčane, pa to nije fizikalna pogreška. Promjena bi ipak mijenjala raspored laboratorija koji
  se provjerava na 320/768/1280 px. → **treba odluku** (prijedlog:
  `ax.set_aspect('equal', adjustable='datalim')` na gornjem panelu).
- Oznake: „razina na osi/uz rub” su riječi. Tekst za istu veličinu koristi $z_C$ (r. 5) i
  $h_C$ (r. 147, 445), pa simbol nije dodan dok autorica ne odluči (vidi popis odluka).
  **Status: provjereno, bez promjene (1 stavka za odluku).**

### u05_sila_na_ravnu_plohu — U05

**c04 (p(y) niz plohu, centar tlaka; konvergencija y_CP)**: tlak raste linearno s dubinom.
Os $y$ je okrenuta prema dolje. $y_{CP}=1{,}07\ \text{m}>b/2$, dakle ispod težišta ✓; drugi red ✓.
Notacija markdowna i modela odstupa od teksta: kut α mjeren od vertikale prema θ od vodoravnice
u tekstu (r. 124), a α je prema standardu korekcijski faktor. Uloge `b` i `L` su zamijenjene:
u bilježnici je b duljina niz plohu, a L širina, dok tekst (r. 236) koristi b za širinu i L za
duljinu. Dubina gornjeg ruba je $h_t$ prema $h_0$/$h_A$ u tekstu. Graf te oznake ne prikazuje
→ **treba odluku** (izmjena markdowna i modela, ne crteža). **Status: crtež provjeren, bez promjene.**

### u06_zakrivljena_ploha — U05

**c04 (konvergencija vektorske integracije)**: provjeren je i smjer. Normala iz vode je
$(\cos\theta,\sin\theta)$ prema središtu, voda je na konveksnoj donjoj lijevoj strani, pa je
$F_x>0$ i $F_z>0$. Pomoćni volumen $R h_t+\pi R^2/4$ potvrđuje $F_z$ ✓. **Bez promjene.**

### u07_gaz_plivajuceg_tijela — U06

**c04 (gaz prema masi za dvije gustoće, crta H)**: veća gustoća daje manji gaz ✓, a potpuno
uranjanje nastupa pri $m=\rho LBH$ ✓. Markdown i kod koriste gaz $d$, uzgon $F_B$ i
„slobodni bok”; standard propisuje $T$, $F_U$ i nadvođe $f$. Graf tu oznaku ne prikazuje
(„gaz (m)”) → **treba odluku**. **Status: provjereno, bez promjene.**

### u08_kontinuitet_suzenje — U07

**c04 (h(t) za tri Δt; pogreška prema Δt)**: približavanje ravnoteži $(Q_{in}/k)^2=0{,}36$ m ✓;
prvi red ✓. Problem: crta „ravnoteža” (#2e7d32) bila je gotovo iste boje kao krivulja Δt = 5 s
(zadana zelena). **Ispravak:** crta ravnoteže je sivoplava #536577. Krivulje Δt namjerno se
preklapaju (razlike oko 10⁻⁴ m). Markdown koristi $Q_{in}$, $Q_{out}$, a standard indekse
ul, iz → **treba odluku**. **Status: ispravljeno.**

### u09_kompresibilna_sapnica — U09

**c05 (ṁ prema p_b/p₀; histogram ṁ_max)**: plato ispod $p^*/p_0=0{,}528$ ✓. Nestlačiva procjena
s gustoćom komore leži iznad i približava se pri $p_b/p_0\to1$ ✓. Problemi: oznaka „M=1”
(standard: $Ma$) i glavna krivulja bez oznake u legendi. **Ispravak:** `$Ma=1$ u grlu`;
dodana oznaka „izentropski model”. Markdown i kod koriste $M$ i `gamma`, a standard
$Ma$ i $\kappa$ → **treba odluku**. **Status: ispravljeno.**

### u09_venturi — U08 (laboratorij „venturi”)

**Laboratorij `draw_venturi`: shema prolaza, brzine, udjeli varijance**
- a) Shema: ulaz D₁, suženje, grlo D₂, difuzor. Presjek 1 je u ulaznom dijelu (x=0,15),
  presjek 2 u grlu (x=0,5); strelice toka su slijeva udesno.
- b) Problemi: (1) sve tri strelice toka bile su jednake duljine, iako je $v_2=v_1(D_1/D_2)^2$,
  dakle 4× za uljni primjer. (2) Ulazna strelica (0,085–0,155) presijecala je crtu presjeka 1.
  (3) Brojevi presjeka „1” i „2” preklapali su naslov. (4) Stupac „Cd” nije zapisan kao $C_d$.
- d) Tablica vektora (shema):

| oznaka | veličina | očekivani smjer | nacrtani smjer | očekivana rel. duljina | nacrtana duljina (osi x) | status |
|---|---|---|---|---|---|---|
| strelica ulaz | $v_1$ | +x | +x | 1 | 0,06 (prije 0,07) | ✓ |
| strelica grlo | $v_2$ | +x | +x | $(D_1/D_2)^2$ = 4 (ulje, voda) | 0,11 (prije 0,07) | poredak ✓, omjer nije u mjerilu (raspon klizača do ≈ 500× ne stane u grlo); zabilježeno u komentaru koda |
| strelica izlaz | $v_1$ | +x | +x | 1 | 0,06 | ✓ |

- e) Oznake: presjeci 1, 2 = tekst ($p_1$, $p_2$, $v_1$, $v_2$) ✓; `D₂`, `Δp` ✓; `Cd` → $C_d$ ispravljeno.
- **Ispravak:** strelica u grlu je dulja (poredak brzina); ulazna strelica pomaknuta na
  x=0,04–0,10; naslov dobio razmak `pad=14`; $C_d$ i matematičke oznake na stupcima.
- **c12 (histogram Q; udjeli varijance)**: oznake stupaca bile su imena varijabli (`delta_p`,
  `rho`, `Cd`). **Ispravak:** $D_1$, $D_2$, $\Delta p$, $\rho$, $C_d$.
- **Provjera:** PNG laboratorija (voda, s usporedbom A) i c12 pogledani; test laboratorija OK.
  **Status: ispravljeno.**

### u10_moody_dijagram — U13

- **c05**: naslov je glasio „Re=1e+05” (računalni zapis). **Ispravak:** $Re=1\cdot10^5$ izveden
  iz `Re0`. λ raste s ε/D ✓.
- **c09, Z4**: radna točka 19,03 L/s i 19,14 m na presjeku krivulja ✓. Dvostruka ε pomiče
  krivulju sustava prema gore ✓. Oznaka „|Hp − Hs|” bila je obični tekst. **Ispravak:**
  $|H_p-H_s|$; dodana legenda „radna točka”. **Status: ispravljeno.**

### u11_sila_na_koljeno — U10

**c05: sila prema kutu θ i poligon zatvaranja sila (Z3: Q=0,026 m³/s, D=100 mm, p_M1=180 kPa,
p_M2=175 kPa, θ=90°)**
- c) Ručno: $A=7{,}854\cdot10^{-3}$ m², $v=3{,}31$ m/s, $\dot m=25{,}95$ kg/s;
  $\vec F_p=(1413{,}7;\,-1374{,}4)$ N, $\dot m(\vec v_2-\vec v_1)=(-85{,}9;\,85{,}9)$ N,
  $\vec R_{st\to f}=(-1499{,}6;\,1460{,}3)$ N. Sila fluida na koljeno je $(1499{,}6;\,-1460{,}3)$ N
  = `assert` ✓. Pri θ=0 i $p_1\ne p_2$ vrijedi $F_x=(p_1-p_2)A=39$ N ✓; pri 180° je $F_x$ najveći ✓.
- d) Tablica vektora (poligon, nadovezivanje od ishodišta):

| oznaka | veličina | očekivani smjer | nacrtani smjer | očekivana rel. duljina | nacrtana duljina | status |
|---|---|---|---|---|---|---|
| $\vec F_p$ | tlačna sila na fluid (KP) | +x, −y (ulaz +x, izlazna normala +y) | (1413,7; −1374,4) | 1971 N → 1 | 1 | ✓ |
| $\vec R_{st\to f}$ | sila stijenke na fluid | −x, +y | (−1499,6; 1460,3) | 2093 N → 1,06 | 1,06 | ✓ |
| $-\dot m(\vec v_2-\vec v_1)$ | negativni tok količine gibanja | +x, −y | (85,9; −85,9) | 121 N → 0,06 | 0,06 | ✓ zatvara poligon |

  Problem: crtež je točan, ali je trokut zbog prevlasti tlaka gotovo degeneriran. Strelica tlaka
  bila je potpuno skrivena ispod strelice stijenke, a oznake su bile riječi bez simbola iz
  bilance $\vec F_p+\vec R_{st\to f}=\dot m(\vec v_2-\vec v_1)$.
- e) `tlak` → $\vec F_p$; `stijenka` → $\vec R_{st\to f}$ (tekst r. 2/markdown) ✓;
  `x (N)` → „komponenta x (N)”.
- **Ispravak:** šira podložna strelica $\vec F_p$, uže strelice stijenke i toka količine gibanja,
  manje glave; oznake iz bilance.
- **c07, Z5 (snaga ploče prema u)**: optimum $u=v/3$ i $P_{max}=1{,}486$ kW = tekst (r. 1075) ✓;
  P = 0 pri u = 0 i u = v ✓. Oznake „F u” i „u = v/3” bile su obični tekst. **Ispravak:**
  $P=F_x\,u$, $u=v/3$; simboli $u$ i $P$ na osima.
- **Provjera:** PNG pogledan; poligon je čitljiv (plavo ispod crvenog, zelena zatvara).
  **Status: ispravljeno.**

### u12_pelton_lopatica — U14

- **c05**: optimum $u/c_1=0{,}5$ za cijeli rotor ✓. Legenda je imala decimalnu točku („k=0.80”),
  a oznaka „u/c1=0,5” nije bila matematička. **Ispravak:** $k=0{,}80$ itd., $u/c_1=0{,}5$,
  simboli $P$ i $\varphi$.
- **c07, Z3**: k = 0,85 pri $F_x=625$ N; granica k = 1 ✓. **Ispravak:** oznake $F_x$ i $k$.
- **c09, Z4: trokuti brzina**

| oznaka | veličina | očekivani smjer | nacrtani smjer | očekivana duljina (m/s) | nacrtano | status |
|---|---|---|---|---|---|---|
| $\vec u_1$ | obodna brzina, $\omega r_1$ | +t | (12; 0) | 12 | 12 | ✓ |
| $\vec w_1$ | relativna | od vrha $\vec u_1$ | (−7; 4) | 8,06 | 8,06 | ✓ |
| $\vec c_1$ | apsolutna | od ishodišta | (5; 4) | 6,40 | 6,40 | ✓ $\vec c=\vec u+\vec w$ |
| $\vec u_2$ | $\omega r_2$ | +t | (28; 0) | 28 | 28 | ✓ |
| $\vec w_2$ | relativna | od vrha $\vec u_2$ | (−8; 6) | 10 | 10 | ✓ |
| $\vec c_2$ | apsolutna | od ishodišta | (20; 6) | 20,9 | 20,9 | ✓ |

  Isto mjerilo za oba trokuta i `aspect='equal'` = tekst (r. 698) ✓. Problemi: oznake „u, w, c”
  bez vektora i indeksa presjeka; osi „t (m/s)” i „r (m/s)”, pri čemu je r u tekstu polumjer
  (m); naslov „r = 0.060 m” s decimalnom točkom. **Ispravak:** $\vec u_i$, $\vec w_i$, $\vec c_i$;
  osi „tangencijalna komponenta” i „radijalna komp.”; naslov $r_1=0{,}060$ m.
- **c11, Z5**: A (20 m/s; 35 kW) izvediv, B (30 m/s; 47,5 kW) nije ✓. Oznake „T”, „Vj” i
  „dostupno 40 kW” nisu bile u notaciji teksta (r. 822–824: $F_T$, $v_j$, $P_{el,max}$).
  **Ispravak:** $F_T=2{,}00$ kN, $v_j$ u brodskom okviru, $P_{el,max}=40{,}0$ kW, $P_{el}$.
  Markdown Z5 i dalje piše T, U i „TU” → **treba odluku**. **Status: ispravljeno.**

### u12_poiseuille_konvergencija — U12 (laboratorij „poiseuille”)

- **Laboratorij `draw_poiseuille`**: parabola, $u(R)=0$ (prianjanje), najveća brzina na osi i
  nulti gradijent na osi ✓. Ćelije: središta su Δr/2 od stijenke ✓; drugi red ✓. Os „|Q − Qref|”
  bila je obični tekst. **Ispravak:** $|Q-Q_{ref}|$. Brzina fluida označena je s $u$ u cijeloj
  bilježnici (jednadžbe u markdownu, kod, osi), a u knjizi je brzina fluida $v$ i brzina stijenke
  $u$ (r. 623) → **treba odluku**. Tekst „os: simetrija” presijecaju crte ploha (manja čitljivost).
- **c10**: os „$|Q_h-Q|$” bez jedinice → dodano (m³/s).
- **c14, Z4 (dva profila)**: $v(0)=0$, $v(H)=u=2$ m/s ✓. Pri 1,10 $G_{krit}$ povratni tok je u
  $0<y<H/11$ ✓; $\tau_0=\pm20{,}0$ Pa = tekst (r. 623) ✓. Problemi: os „u (m/s)” je u knjizi
  oznaka brzine **ploče**; legenda je bila obični tekst „G/Gkrit”, „tau0” s decimalnom točkom.
  **Ispravak:** os „brzina fluida $v$”, legenda $G/G_{krit}=0{,}90$; $\tau_0=+20{,}0$ Pa.
  Markdown Z4 i dalje piše $U=2{,}00$ m/s, a tekst $u$ → **treba odluku**.
- **c16, Z6 (GCI)**: os „(h/h_f)²” bila je obični tekst → $(h/h_f)^2$. Q u mL/s = 10⁻⁶ m³/s ✓.
- **c18, Z6 b)**: oznake na osi y „u_m = …” i „E ± U_E” bile su obični tekst. Crvena crta
  imala je oznaku, ali legenda nije bila pozvana, pa crta nije bila objašnjena.
  **Ispravak:** $u_m=0{,}00020$, $E\pm U_E$ i `ax.legend()`. Intervali: osnovni ne sadrži 0,
  alternativni sadrži = tekst (r. 686) ✓. **Status: ispravljeno (1 stavka za odluku).**

### u13_paralelne_grane — U13

- **c05**: legenda je doslovno ispisivala „Q_A”. **Ispravak:** $Q_A$, $Q_B$, $Q_C$. Zbroj
  protoka je stalan (30 L/s); $Q_B$ raste s $D_B$, a ostali protoci padaju ✓.
- **c09, Z6 (stupci energije)**: 8,19 i 5,54 MWh/god = `assert` ✓. **Bez promjene.**
- Kod koristi ključ `K` za lokalni koeficijent, a standard rezervira $K$ za volumni modul
  ($\xi$ za lokalni gubitak). Na grafu se ne vidi → **treba odluku**. **Status: ispravljeno.**

### u14_cd_re_kugla — U11

- **c05**: naslov „Model samo u označenom rasponu”, a raspon nije bio označen. Os „Re” bila je
  obični tekst. **Ispravak:** točkaste crte `granice modela` na 0,1 i 2·10⁵; $Re$ na objema osima.
- **c12, Z6**: intervali 1:20 (224 ± 4,8 kN) i 1:30 (216 ± 5,4 kN), presjek 219,2–221,4 kN =
  `assert` ✓. Os „Mjerilo λL” bila je obični tekst → $\lambda_L$ (standard). **Status: ispravljeno.**

### u15_otvoreni_tokovi — U15

- **c05, E(y)**: minimum u $y_c=0{,}612$ m i $E_{min}=1{,}5y_c$ ✓; alternativne dubine 0,37 i
  1,11 m na zadanoj E = 1,20 m ✓. Problem: crvene točke i crtkana crta nisu bile objašnjene, a
  oznake osi i histograma „y2” bile su obični tekst. **Ispravak:** legenda „zadana E = 1,20 m” i
  „alternativne dubine”; $y$, $E$, $y_2$.
- **c07, Z4 (dubina na tjemenu prema Δz)**: podkritična grana pada do $y_c$ pri $\Delta z_{max}$ ✓.
  **Ispravak:** $y_t$ i $\Delta z$ (tekst r. 504, 509), legenda $\Delta z_{max}$ i „zadani prag”.
- **c09, Z5**: os „rezidual M₂ − M₁”, a tekst (r. 539) definira $R=(I_2-I_1)/(\rho g b)$ preko
  impulsne funkcije $I$. Matematički je izraz isti (provjereno). **Ispravak:** oznaka prema tekstu.
- **c11, Z6**: krivulje A/B/C nisu imale vrijednosti n, a crte $Q_d$ i $H-f_{min}$ ni točke
  kapaciteta nisu bile objašnjene. **Ispravak:** $n_A=0{,}018$ itd., $Q_d=8{,}00$ m³/s,
  $H-f_{min}=1{,}20$ m, $y_{2,dop}=1{,}40$ m, „kapaciteti A, B, C”, $y_2$ (tekst r. 564–570).
  Jedino stanje A zadovoljava uvjet; $y_2$ pri $Q_d$ manji je od 1,40 m ✓. **Status: ispravljeno.**

---

## Sažetna tablica

| crtež | problem | ispravak | status |
|---|---|---|---|
| u01 c04 | dvije osi bez legende | legenda i obojene oznake sa simbolima | ispravljeno |
| u01 c08 | — | — | provjereno |
| u02 c04 | — | — | provjereno |
| u02 c11 (Z5) | osi bez $\tau$, $dv/dy$ | simboli iz teksta | ispravljeno |
| u02 c13 (Z6) | „drugi regulator” dvosmislen; nema $p_{M,2}$, $D$ | rasponi regulatora i simboli | ispravljeno |
| u03 c04 | $\rho_m$ prema $\rho_2$ (ρ_m = more u U03) | $\rho_2$ | ispravljeno |
| u04 c09 | — | — | provjereno |
| u04 laboratorij | presjek nije u jednakom mjerilu (≈ 3×) | — | treba odluku |
| u05 c04 | (notacija markdowna α/b/L/h_t) | — | provjereno; notacija → odluka |
| u06 c04 | — | — | provjereno |
| u07 c04 | (notacija d/F_B) | — | provjereno; notacija → odluka |
| u08 c04 | boja ravnoteže kao Δt = 5 s | sivoplava crta | ispravljeno |
| u09k c05 | „M=1”; glavna krivulja bez oznake | $Ma=1$, „izentropski model” | ispravljeno |
| u09 Venturi laboratorij | jednake strelice (kontinuitet), preklapanje „1/2” i naslova, Cd | dulja strelica u grlu, pad, $C_d$ | ispravljeno |
| u09 Venturi c12 | imena varijabli na stupcima | simboli | ispravljeno |
| u10 c05, c09 | „1e+05”; „Hp − Hs” | $Re=1\cdot10^5$, $H_p-H_s$, radna točka | ispravljeno |
| u11 c05 | poligon: tlak skriven; oznake riječima | širine i glave strelica, $\vec F_p$, $\vec R_{st\to f}$ | ispravljeno |
| u11 c07 (Z5) | oznake obični tekst | $P=F_xu$, $u=v/3$ | ispravljeno |
| u12p c05, c07, c09, c11 | decimalna točka, t/r osi, oznake bez vektora, T/Vj | oznake prema tekstu U14 | ispravljeno |
| u12 Poiseuille laboratorij | „Qref” obični tekst; $u$ za brzinu fluida | $Q_{ref}$; $u$/$v$ → odluka | ispravljeno + odluka |
| u12 c10, c14, c16, c18 | bez jedinice; $u$ (ploča) za fluid; nedostaje legenda | (m³/s), $v$, $G_{krit}$, $\tau_0$, legenda | ispravljeno |
| u13 c05 | „Q_A” doslovno | $Q_A$ | ispravljeno |
| u13 c09 | — | — | provjereno |
| u14 c05 | raspon „označen”, a nije | granice modela, $Re$ | ispravljeno |
| u14 c12 | „λL” | $\lambda_L$ | ispravljeno |
| u15 c05, c07, c09, c11 | neobjašnjene crte i točke; M umjesto I; bez n | legende i oznake prema tekstu | ispravljeno |
| web/filters/includes/components | nema crteža | — | — |

## Treba odluku autorice

1. **u04 laboratorij, mjerilo presjeka.** Gornji panel „Presjek otvorenog spremnika” nema
   jednako mjerilo osi; okomito je sabijen oko 3×, pa paraboloid izgleda plići. Prijedlog:
   `ax.set_aspect('equal', adjustable='datalim')`. To mijenja izgled laboratorija; nakon izmjene
   treba pokrenuti `audit_interactive_labs.mjs`.
2. **u12_poiseuille, brzina fluida $u$.** Markdown laboratorija (
   $\frac{d}{dr}(r\,du/dr)$ …), kod i osi koriste $u$ za brzinu fluida. Knjiga (u12, r. 623)
   koristi $v(r)$, $v(y)$, a $u$ za brzinu ploče. Z4 markdown piše „$U=2{,}00$ m/s”, a tekst $u$.
   Graf Z4 je usklađen s knjigom ($v$), ostatak nije. Prijedlog: preimenovati u cijeloj bilježnici
   ($u\to v$, $U\to u$).
3. **u05_sila_na_ravnu_plohu, notacija modela.** Markdown: „Kut $\alpha$ ovdje je izričito mjeren
   **od vertikale**; gornji rub nalazi se na dubini $h_t$”. Tekst (r. 124, 236): $\theta$ prema
   vodoravnici, $h_0$/$h_A$, b širina i L duljina niz plohu. Bilježnica ima obrnute uloge b i L,
   a α je prema standardu korekcijski faktor. Prijedlog: prijeći na θ od vodoravnice, $h_0$, b i L
   kao u tekstu (mijenja `analiticka_ploha` i markdown).
4. **u07, u08, u09_kompresibilna, u12_pelton (Z5), u13: notacija markdowna i koda.**
   u07 $d$ → $T$, $F_B$ → $F_U$, „slobodni bok” → nadvođe $f$; u08 $Q_{in}$/$Q_{out}$ →
   $Q_{ul}$/$Q_{iz}$; u09k $M$, `gamma` → $Ma$, $\kappa$; u12p Z5 „T, U, TU” → $F_T$, $v_s$,
   $F_Tv_s$; u13 ključ `K` (lokalni koeficijent) → $\xi$. Grafovi su usklađeni gdje te oznake
   prikazuju; tekst bilježnica nisam mijenjao jer je izvan opsega crteža.
5. **Izvor U04, dvije oznake za istu veličinu (ne pogađam).** r. 5: „paraboloid
   $z(r)=z_C+\omega^2r^2/(2g)$”, a r. 147 i 445: „$h_C$ visina površine na osi”. Zato u u04
   grafu nije dodan simbol razine na osi.
6. **Izvor U15, ista oznaka za dvije veličine.** $y_t$ je nizvodni vodostaj u r. 294 i 313
   („nizvodni vodostaj kanala iznosi $y_t=1{,}00$ m”) i dubina na tjemenu praga u r. 509
   („odaberi dubinu $y_t$ te njezin $Fr_t$”). Graf Z4 koristi $y_t$ za tjeme prema Z4.
7. **Decimalni zarez na osima.** Matplotlib na svim grafovima prikazuje decimalnu točku na
   oznakama osi (npr. 0.25). Oznake u legendama i naslovima koje sam mijenjao imaju zarez.
   Globalna promjena (npr. `axes.formatter.use_locale` uz hr_HR ili vlastiti formatter u svih
   17 bilježnica) zasebna je odluka.
8. **u11 poligon sila.** Trokut je fizikalno gotovo degeneriran (121 N prema oko 2000 N). Sada je
   čitljiv. Ako treba naglasiti zatvaranje, moguć je umetak s uvećanim vrhom ili tekstualni
   iznos $|\dot m\Delta\vec v|$.

## Preostala ograničenja

- Provjera potvrđuje izvršivost, prolaz testova i vizualnu ispravnost pregledanih slika (početni
  slučajevi i nekoliko graničnih stanja laboratorija), ne svih kombinacija klizača.
- `audit_interactive_labs.mjs` (JupyterLite u pregledniku) i obnova `_site/jlite` (hashovi
  bilježnica) nisu pokrenuti. Pokreću se centralno nakon izgradnje.
