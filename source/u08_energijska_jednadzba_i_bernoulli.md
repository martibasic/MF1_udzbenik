![Pregled poglavlja: energijska jednadžba i Bernoulli.](../assets/print/u09_fig_uvod_pregled.svg){#fig-uvod-u09 fig-align="center" fig-alt="Pregled poglavlja: energijska jednadžba i Bernoulli."}

## Energijska jednadžba i Bernoullijeva jednadžba

Bernoullijeva jednadžba opisuje preraspodjelu mehaničke energije između tlaka, brzine i geodetske visine duž strujnice idealiziranoga toka. Uz bilancu mase omogućuje analizu Venturijeve cijevi, slobodnoga mlaza i Pitotove sonde.

Torricellijev zakon istjecanja povezuje brzinu mlaza s visinom stupca tekućine. Bernoullijeva jednadžba proširuje tu sliku uključivanjem tlačne energije.

::: {.mf1-application}
<p class="mf1-box-label">Inženjerski kontekst</p>

Bernoullijeva jednadžba povezuje tlak i brzinu u Venturijevoj cijevi, Pitotovoj sondi, mlaznici i sifonu. Za svaki primjer najprije odabiremo presjeke i provjeravamo mogu li se gubitci zanemariti.
:::

**Procijenjeno vrijeme rada uz udžbenik:** 10 sati.

## Mehanička energija idealnoga toka

Bernoullijeva jednadžba u ovom poglavlju predstavlja bilancu mehaničke energije po jedinici težine u idealiziranom strujanju. Tri osnovna člana su:

1. tlačna visina $p/(\rho g)$.
2. brzinska visina $v^2/(2g)$.
3. geodetska visina $z$.

Najčešći zapis glasi

$$
\frac{p}{\rho g} + \frac{v^2}{2g} + z = \text{const.}
$$ {#eq-energijska-bilanca-fizikalni-uvod-i-matematicki-izvod-01}

Za dvije točke na istoj strujnici to prelazi u

$$
\frac{p_1}{\rho g} + \frac{v_1^2}{2g} + z_1 = \frac{p_2}{\rho g} + \frac{v_2^2}{2g} + z_2
$$ {#eq-energijska-bilanca-fizikalni-uvod-i-matematicki-izvod-02}

::: {.mf1-interaktivno}
<p class="mf1-box-label">Interaktivni prikaz — Venturijeva cijev</p>

U bilježnici pokreni sve ćelije, zatim odaberi idealni primjer s uljem ili zasebni nastavni slučaj s vodom. Kontrole povezuju geometriju, brzine, razliku tlakova i procijenjeni protok; slučaj A možeš spremiti za usporedbu. Kartice *Provjeri* i *Pogledaj kod* otkrivaju pretpostavke i račun. Kontrole nesigurnosti prikazuju doprinose promjera grla, razlike tlakova i koeficijenta istjecanja; potpuni budžet pet ulaza te usporedba linearne procjene i uzorkovanja slijede u ćelijama `base` i `sigma`.

<div class="mf1-interaktivno-akcija">
<a class="mf1-interaktivno-veza" href="https://martibasic.github.io/MF1_udzbenik/jlite/lab/index.html?path=u09_venturi.ipynb">Pokreni u pregledniku</a>
<a class="mf1-interaktivno-veza" href="https://colab.research.google.com/github/martibasic/MF1_udzbenik/blob/main/notebooks/u09_venturi.ipynb" target="_blank" rel="noopener">Pričuvno: otvori u Colabu</a>
<img class="mf1-interaktivno-qr" src="../assets/qr/u09_venturi.svg" alt="QR kod za interaktivni prikaz Venturijeve cijevi"/>
</div>

:::

Ako jedan član raste, barem jedan od preostala dva mora pasti. Upravo je to fizikalna srž Venturija, Pitota, mlaza i sifona bez gubitaka.

Iz istih članova odmah proizlaze i dvije korisne linije za prikaz energije toka. Hidraulička linija ili `HGL` jednaka je zbroju tlačne i geodetske visine,

$$
HGL = \frac{p}{\rho g} + z,
$$ {#eq-energijska-bilanca-interaktivni-prikaz-venturijeva-cijev-01}

dok energetska linija ili `EGL` sadrži i brzinski član,

$$
EGL = \frac{p}{\rho g} + \frac{v^2}{2g} + z.
$$ {#eq-energijska-bilanca-interaktivni-prikaz-venturijeva-cijev-02}

::: {.mf1-fizikalno-znacenje}
<p class="mf1-box-label">Fizikalno značenje</p>
`HGL` (hidraulička linija) vizualizira piezometarsku visinu $z+p/(\rho g)$, a `EGL` (energetska linija) iznad nje leži za brzinsku visinu $v^2/(2g)$. Pri crtanju otvorenih vodnih sustava uobičajeno je koristiti **manometarski tlak**, pa slobodna površina otvorenog spremnika leži na HGL-u. U idealnom toku `EGL` je horizontalna, dok `HGL` pada gdje fluid ubrzava i raste gdje usporava. Ako je HGL ispod osi cijevi, manometarski tlak je negativan, ali apsolutni tlak i dalje može biti daleko iznad tlaka zasićene pare. Kavitacija je moguća tek kad lokalni **apsolutni** tlak dosegne tlak zasićene pare pri promatranoj temperaturi.
:::

U idealnom toku `EGL` ostaje konstantna duž iste strujnice, a `HGL` je od nje niže upravo za brzinsku visinu $v^2/(2g)$. Zato su Venturijeva cijev i Pitotova sonda već u ovom poglavlju prirodni vizualni modeli preraspodjele energije.

Tlak zadan u paskalima ili kilopaskalima u Bernoullijevoj se jednadžbi često izražava tlačnom visinom, u metrima fluida:

$$
\frac{p}{\gamma} = \frac{p}{\rho g}.
$$ {#eq-energijska-bilanca-fizikalno-znacenje-01}

Za vodu to znači da je približno $1\ \text{m}$ tlačne visine oko $9{,}81\ \text{kPa}$, odnosno da je $10\ \text{kPa}$ približno $1{,}02\ \text{m}$ vodenog stupca. Kad se u horizontalnom idealnom vodu brzina poveća, `EGL` ostaje ista, a `HGL` pada upravo za onoliko koliko se poveća brzinska visina. Zato pad statičkog tlaka od, primjerice, $\Delta p$ nije samo broj u kilopaskalima nego i pad `HGL` za $\Delta p/(\rho g)$ metara fluida.

Ista logika vrijedi i obrnuto: tlačna se visina množenjem s $\rho g$ pretvara u tlak, ali prije toga mora biti jasno je li visina apsolutna ili manometarska. Atmosferski se tlak dodaje samo pri prijelazu iz manometarske u apsolutnu referencu.

Svaki član ima izravno fizikalno značenje. Član $p/(\rho g)$ govori koliku bi visinu fluida dao tlak, član $v^2/(2g)$ koliki je udio energije vezan uz gibanje, a član $z$ koliko energije dolazi iz samoga položaja u gravitacijskom polju. Bernoullijeva jednadžba zato stalno prevodi jednu istu mehaničku energiju iz jednoga oblika u drugi.

::: {.mf1-izvod}
<p class="mf1-box-label">Matematički izvod — Eulerova jednadžba duž strujnice iz Newtonova zakona</p>

Bernoullijeva jednadžba nije zaseban zakon, nego integrirani oblik Eulerove jednadžbe — Newtonova drugoga zakona primijenjenoga na element fluida koji se giba duž strujnice u idealnom (neviskoznom, nestlačivom, stacionarnom) strujanju.

Promatra se element strujne cijevi duljine $ds$ i poprečnog presjeka $A$ koji se giba uz strujnicu brzinom $v$ u smjeru $s$. Masa elementa je $dm = \rho A\,ds$. Na njega djeluju tri vrste sila u smjeru osi $s$:

- sila tlaka na ulaznoj plohi: $p A$ u smjeru $+s$;
- sila tlaka na izlaznoj plohi: $-(p + dp) A$ u smjeru $+s$ (predznak: tlak gura natrag);
- komponenta težine duž osi $s$: $-\rho g A\,ds \cdot \sin\theta$, gdje je $\theta$ kut između strujnice i horizontalne ravnine. Korištenjem $\sin\theta = dz/ds$ (porast visine po duljini strujnice) komponenta se zapisuje kao $-\rho g A\,ds \cdot dz/ds$.

Zbroj sila na element iznosi

$$
dF_s = pA - (p + dp)A - \rho g A\,ds\,\frac{dz}{ds} = -A\,dp - \rho g A\,dz.
$$ {#eq-energijska-bilanca-matematicki-izvod-eulerova-jednadzba-duz-strujni-01}

Newtonov drugi zakon povezuje to s ubrzanjem $a_s = dv/dt$. Za stacionarno strujanje vrijedi materijalna derivacija $dv/dt = v\,dv/ds$ (čista konvektivna komponenta jer je $\partial v/\partial t = 0$), pa je

$$
dm \cdot a_s = \rho A\,ds \cdot v\,\frac{dv}{ds} = -A\,dp - \rho g A\,dz.
$$ {#eq-energijska-bilanca-matematicki-izvod-eulerova-jednadzba-duz-strujni-02}

Kraćenjem s $A$ i dijeljenjem s $ds$ slijedi **Eulerova jednadžba duž strujnice**

$$
\rho v\,\frac{dv}{ds} = -\frac{dp}{ds} - \rho g\,\frac{dz}{ds},
$$ {#eq-energijska-bilanca-matematicki-izvod-eulerova-jednadzba-duz-strujni-03}

odnosno u kompaktnijem zapisu

$$
\rho\,v\,dv + dp + \rho g\,dz = 0.
$$ {#eq-energijska-bilanca-matematicki-izvod-eulerova-jednadzba-duz-strujni-04}

Integriranje ovoga diferencijalnog oblika uz pretpostavku konstantne gustoće dat će Bernoullijevu jednadžbu — što je tema izvoda koji slijedi.
:::

::: {.mf1-izvod}
<p class="mf1-box-label">Matematički izvod — Bernoullijeva jednadžba iz Eulerove</p>

Promatra se element idealnoga fluida koji se giba duž strujnice s koordinatom $s$. Za stacionarno, nestlačivo i neviskozno strujanje projekcija jednadžbe količine gibanja na strujnicu daje Eulerov zapis

$$
\rho v\frac{dv}{ds} = -\frac{dp}{ds} - \rho g\frac{dz}{ds}.
$$ {#eq-energijska-bilanca-matematicki-izvod-bernoullijeva-jednadzba-iz-eul-01}


Nakon množenja s $ds/\rho$ slijedi

$$
v\,dv + \frac{dp}{\rho} + g\,dz = 0.
$$ {#eq-energijska-bilanca-numericki-trag-01}

::: {.callout-note}
## Postupak rješenja
Korak: od Eulerove jednadžbe gibanja → Bernoullijeva jednadžba integriranjem

Eulerova jednadžba: $\rho v\frac{dv}{ds} = -\frac{dp}{ds} - \rho g\frac{dz}{ds}$.

Korak 1 – dijeli s $\rho$ i pomnoži s $ds$:
$$v\,dv + \frac{dp}{\rho} + g\,dz = 0.$$ {#eq-energijska-bilanca-razrada-koraka-01}

Korak 2 – prepoznaj integrabilne oblike: $v\,dv = d(v^2/2)$, $dp/\rho = dp/\rho$ (za $\rho = \text{const.}$: $= d(p/\rho)$), $g\,dz = d(gz)$.

Korak 3 – integriraj od točke 1 do točke 2:
$$\frac{v_2^2 - v_1^2}{2} + \frac{p_2 - p_1}{\rho} + g(z_2 - z_1) = 0.$$ {#eq-energijska-bilanca-razrada-koraka-02}

Korak 4 – presloži: premjesti sve s indeksom 2 nadesno i s indeksom 1 nalijevo:
$$\frac{p_1}{\rho} + \frac{v_1^2}{2} + gz_1 = \frac{p_2}{\rho} + \frac{v_2^2}{2} + gz_2.$$ {#eq-energijska-bilanca-razrada-koraka-03}

Korak 5 – podijeli s $g$ da dobiješ metre fluida: $\frac{p}{\rho g} + \frac{v^2}{2g} + z = \text{const.}$
:::

Integriranjem između točaka 1 i 2 dobiva se

$$
\int_{v_1}^{v_2} v\,dv + \int_{p_1}^{p_2} \frac{dp}{\rho} + g\int_{z_1}^{z_2} dz = 0.
$$ {#eq-energijska-bilanca-razrada-koraka-04}

Za nestlačiv fluid gustoća je konstantna, pa integracija daje

$$
\frac{v_2^2-v_1^2}{2} + \frac{p_2-p_1}{\rho} + g(z_2-z_1) = 0,
$$ {#eq-energijska-bilanca-razrada-koraka-05}

odnosno

$$
\frac{p_1}{\rho} + \frac{v_1^2}{2} + gz_1 = \frac{p_2}{\rho} + \frac{v_2^2}{2} + gz_2 = \text{const.}
$$ {#eq-energijska-bilanca-razrada-koraka-06}

Dijeljenjem s $g$ nastaje klasični Bernoullijev oblik u metrima fluida:

$$
\frac{p}{\rho g} + \frac{v^2}{2g} + z = \text{const.}
$$ {#eq-energijska-bilanca-razrada-koraka-07}

::: {.mf1-fizikalno-znacenje}
<p class="mf1-box-label">Fizikalno značenje</p>
Ova jednadžba kaže da mehanička energija po jedinici težine ostaje konstantna duž strujnice idealnog fluida — ona se samo premješta između tlačne visine, brzinske visine i geodetske visine. Tlačni član ne predstavlja komprimiranje nestlačivoga fluida, nego mehanički doprinos **tlačnog rada** okolnog fluida. Kad se cijev sužava i brzina raste, energija dolazi od pada tlaka; kad se tok uspori, dio kinetičke energije može se vratiti u tlak. Bernoulli je zakon o preraspodjeli, a ne o stvaranju energije.
:::

Svaki član ima jasno fizikalno značenje: $p/(\rho g)$ je tlačna visina, tj. mehanička energija vezana uz tlak; $v^2/(2g)$ brzinska visina, odnosno energija gibanja po jedinici težine; a $z$ geodetska visina, tj. položajna energija po jedinici težine. Bernoullijeva jednadžba zato nije samo formula za račun, nego integralna izjava da se u idealnom toku mehanička energija ne gubi, nego se samo preraspodjeljuje između ta tri oblika.
:::

## Kada se trenje može zanemariti

Eulerove jednadžbe opisuju tok u kojem zanemarujemo viskozne sile. Računalo tada može procijeniti, primjerice, kako se brzina i tlak mijenjaju u glatkom suženju ako su gubitci mali.

Takav proračun nije dovoljan kada nas zanima otpor duge cijevi ili sila trenja na stijenci: izostavili bismo upravo pojavu koju želimo izračunati. Prije odabira modela zato treba odrediti što tražimo i koje sile na taj rezultat najviše utječu.


::: {.mf1-izvod}
<p class="mf1-box-label">Matematički izvod — Alternativni izvod Bernoullija iz rada i energije</p>

Bernoullijeva jednadžba može se izvesti i iz **teorema rada i energije**. U stacionarnom, nestlačivom i neviskoznom strujanju rad sila tlaka i sile teže povezuje se s promjenom kinetičke energije elementa fluida. Pretpostavlja se da između promatranih točaka nema strojnog rada.

Promatra se cilindrični element strujne cijevi duljine $ds$, poprečnog presjeka $A$ i mase $dm = \rho A\,ds$ koji se duž strujnice giba brzinom $v$. Tijekom diferencijalnog vremena $dt$ element prelazi udaljenost $ds = v\,dt$, podignuvši se za visinski element $dz = \sin\theta\,ds$.

Na element djeluju dvije vrste sila koje vrše rad:

- **Sile tlaka** na ulaznoj i izlaznoj plohi. Rad neto sile tlaka u smjeru gibanja iznosi

$$
dW_{tlak} = pA\,ds - (p+dp)\,A\,ds = -A\,dp\,ds = -\frac{dp}{\rho}\,dm.
$$ {#eq-energijska-bilanca-matematicki-izvod-alternativni-izvod-bernoullija-01}

- **Sila teže** koja djeluje vertikalno prema dolje i vrši negativan rad pri uspinjanju:

$$
dW_{grav} = -dm\,g\,dz.
$$ {#eq-energijska-bilanca-matematicki-izvod-alternativni-izvod-bernoullija-02}

Promjena kinetičke energije elementa je

$$
dE_k = d\!\left(\frac{1}{2}\,dm\,v^2\right) = dm\,v\,dv.
$$ {#eq-energijska-bilanca-matematicki-izvod-alternativni-izvod-bernoullija-03}

Teorem rada i energije ($\sum dW = dE_k$) daje

$$
-\frac{dp}{\rho}\,dm - dm\,g\,dz = dm\,v\,dv,
$$ {#eq-energijska-bilanca-matematicki-izvod-alternativni-izvod-bernoullija-04}

odakle se nakon dijeljenja s $dm$ dobiva diferencijalni oblik

$$
\frac{dp}{\rho} + g\,dz + v\,dv = 0.
$$ {#eq-energijska-bilanca-matematicki-izvod-alternativni-izvod-bernoullija-05}

Za nestlačivi fluid ($\rho$ = konst.) ova se jednadžba integrira između dviju točaka duž iste strujnice:

$$
\frac{p_1 - p_2}{\rho} + g(z_1 - z_2) + \frac{v_1^2 - v_2^2}{2} = 0,
$$ {#eq-energijska-bilanca-matematicki-izvod-alternativni-izvod-bernoullija-06}

što se preraspodjelom svodi na **Bernoullijevu jednadžbu**

$$
\frac{p}{\rho g} + \frac{v^2}{2g} + z = \text{const.}
$$ {#eq-energijska-bilanca-matematicki-izvod-alternativni-izvod-bernoullija-07}

Ovaj izvod izravno potvrđuje da je **Bernoullijeva jednadžba zakon očuvanja mehaničke energije po jediničnoj težini fluida**. Tri člana sada se čitaju iz energetske perspektive:

- $p/(\rho g)$ je **tlačna visina** — doprinos tlačnog rada okolnog fluida po jedinici težine;
- $v^2/(2g)$ je **brzinska visina** — kinetička energija po jediničnoj težini;
- $z$ je **geodetska visina** — gravitacijska potencijalna energija po jediničnoj težini.

Time se dobiva dvostruki uvid u istu jednadžbu: prvi izvod polazi od **bilance sila** na elementu strujne cijevi, a drugi od **bilance rada i kinetičke energije**. Oba su izvoda utemeljena na istom mehaničkom modelu. U []{.mf1-chapter-ref target="u13"} bilanci se dodaje pozitivan gubitak mehaničke energije $h_w$ zbog ireverzibilnih procesa.
:::

Uz izvod treba jasno navesti i pretpostavke modela. U []{.mf1-chapter-ref target="u08"} Bernoulli vrijedi samo kad su dovoljno dobro opravdane sljedeće pretpostavke:

- strujanje je stacionarno
- fluid se može uzeti nestlačivim
- viskozni gubitci su zanemarivi
- između promatranih točaka nema strojnog rada ni druge vanjske mehaničke dobave energije
- dvije točke leže na istoj strujnici ili na aproksimaciji gdje je takva primjena dopuštena

To nije formalnost. Česta pogreška nastaje kada se Bernoullijeva jednadžba automatski zapiše samo zato što su zadani tlak i brzina, bez prethodne provjere modela.

Riješeni primjeri i zadatci za vježbu pokazuju kako isti Bernoullijev zapis opisuje pad statičkog tlaka u suženju, brzinu slobodnog mlaza, tlak u sifonu i Pitotovo lokalno mjerenje.

::: {.mf1-numerika .kompakt}
<p class="mf1-box-label">Numerički most — Bernoulli kao referenca</p>

**Fizikalna poveznica.** Bernoulli slijedi iz Eulerove jednadžbe uz ovdje navedene pretpostavke. U CFD-u rješavamo lokalne bilance; Bernoulli služi kao analitička referenca, a ne kao zaseban obvezan korak rješavača.

**Račun i provjera.** Za Venturi kontinuitet iz []{.mf1-chapter-ref target="u07"} povezuje brzine, a Bernoulli predviđa razliku tlakova ulaza i grla. Numeričko polje provjeravamo duž iste strujnice ili na presjecima s usklađenim profilima i kotama. U idealnom Eulerovu slučaju neželjeni pad ukupne mehaničke visine može biti numerička pogreška. U viskoznom modelu pad uključuje i stvarnu disipaciju; finija mreža ne uklanja fizikalne gubitke.

**Primjena.** Za protok često dostaje ručni ili 1D model s gubitcima; mreža cjevovoda slijedi u []{.mf1-chapter-ref target="u13"}. CFD postaje koristan za lokalno polje i odvajanje u difuzoru. Isti Venturi povezuje te razine u @sec-cfd-venturi.

[]{#provjera-cfd-a-analitičkim-rješenjem}
:::

## Riješeni primjeri

::: {#ex-u09-pad-statickog-tlaka-u-konfuzoru-ventilacijskog-kanala .mf1-we}
<p class="mf1-box-label">Pad statičkog tlaka u konfuzoru ventilacijskog kanala&nbsp;<span class="mf1-level">T2</span></p>

**Kontekst:** U sustavu prisilne ventilacije konfuzor (suženje) ubrzava struju zraka prije ulaska u uži dio kanala. Projektant iz masenog protoka i geometrije presjeka određuje pad statičkog tlaka koji se javlja zbog ubrzanja zraka u suženju.

**Zadano**

- Ulazni poprečni presjek horizontalnog ventilacijskog kanala: $A_1 = 0{,}07\ \text{m}^2$
- Izlazni poprečni presjek: $A_2 = 0{,}0185\ \text{m}^2$
- Maseni protok zraka: $\dot{m} = 0{,}68\ \text{kg/s}$
- Gustoća zraka: $\rho = 1{,}2\ \text{kg/m}^3$
- Gubici strujanja se zanemaruju

**Traženo**

1. Odredi pad statičkog tlaka $\Delta p$ između presjeka 1 i 2.

![Kontinuitet i energijske visine u horizontalnom konfuzoru](../assets/print/u09_egl_hgl_schema.svg){#fig-u09-staticka-zamjena-za-egl-i-hgl fig-alt="Horizontalni konfuzor: otvoreni presjeci, stalni EGL i pad HGL-a pri ubrzanju zraka."}

**Pretpostavke i model**

Promatra se horizontalni kanal bez gubitaka. Zato najprije iz kontinuiteta treba odrediti brzine u oba presjeka, a zatim iz idealnog Bernoullija procijeniti koliki pad statičkog tlaka odgovara tom ubrzanju.

**Rješenje**

Najprije iz masenog protoka dobivamo volumenski protok:

$$
Q = \frac{\dot{m}}{\rho} = \frac{0{,}68}{1{,}2} \approx 0{,}5667\ \text{m}^3/\text{s}.
$$ {#eq-energijska-bilanca-rijeseni-primjer-pad-statickog-tlaka-u-konfuzoru-01}

Iz toga slijede brzine u oba presjeka:

$$
v_1 = \frac{Q}{A_1} = \frac{0{,}5667}{0{,}07} \approx 8{,}10\ \text{m/s},
$$ {#eq-energijska-bilanca-rijeseni-primjer-pad-statickog-tlaka-u-konfuzoru-02}

$$
v_2 = \frac{Q}{A_2} = \frac{0{,}5667}{0{,}0185} \approx 30{,}63\ \text{m/s}.
$$ {#eq-energijska-bilanca-rijeseni-primjer-pad-statickog-tlaka-u-konfuzoru-03}

Kako je kanal horizontalan, vrijedi $z_1 = z_2$. Za idealni model bez gubitaka Bernoulli daje

$$
\frac{p_1}{\rho g} + \frac{v_1^2}{2g} = \frac{p_2}{\rho g} + \frac{v_2^2}{2g} \quad \Rightarrow \quad p_1 - p_2 = \frac{\rho}{2}(v_2^2 - v_1^2).
$$ {#eq-energijska-bilanca-rijeseni-primjer-pad-statickog-tlaka-u-konfuzoru-04}

Uvrštavanjem brojeva dobiva se

$$
\Delta p = \frac{1{,}2}{2}(30{,}63063^2 - 8{,}09524^2) \approx 523{,}62\ \text{Pa} \approx 0{,}524\ \text{kPa}.
$$ {#eq-energijska-bilanca-rijeseni-primjer-pad-statickog-tlaka-u-konfuzoru-05}

**Provjera i komentar**

1. Kako je $A_2 < A_1$, mora biti $v_2 > v_1$.
2. U idealnom konfuzoru porast brzine mora pratiti pad statičkog tlaka.
3. Ako je račun dao porast tlaka u užem presjeku, zamijenjene su točke ili predznak razlike.
:::

U suženju se kinetički i tlačni član razmjenjuju unutar voda. Kod slobodnog mlaza ista bilanca najprije daje izlaznu brzinu, a zatim se nastavlja običnom kinematikom čestice.

::: {#ex-u09-domet-slobodnog-mlaza-iz-velikog-spremnika-t2 .mf1-we}
<p class="mf1-box-label">Domet slobodnog mlaza iz velikog spremnika&nbsp;<span class="mf1-level">T2</span></p>

**Kontekst:** Iz bočne stijenke velikog otvorenog spremnika voda istječe kroz malu rupicu i tvori slobodni mlaz koji pada na tlo (Torricellijev problem). Treba odrediti vodoravni domet mlaza za nekoliko položaja otvora te onaj položaj koji daje najveći domet.

**Zadano**

- Visina slobodne površine vode iznad tla u velikom otvorenom spremniku: $H = 4{,}0\ \text{m}$
- Položaji male rupice na bočnoj stijenci za usporedbu: $h = 1{,}0\ \text{m}$, $h = 2{,}0\ \text{m}$, $h = 3{,}0\ \text{m}$
- Gubici se zanemaruju

**Traženo**

1. Izračunaj domet mlaza za sva tri zadana položaja otvora.
2. Odredi položaj otvora koji daje najveći domet.

![Domet slobodnog mlaza](../assets/print/u09_val2_slobodni_mlaz.svg){#fig-u09-domet-slobodnog-mlaza fig-alt="Domet slobodnog mlaza"}

**Pretpostavke i model**

Spremnik je dovoljno velik da je brzina na slobodnoj površini zanemariva, a i slobodna površina i otvor su na atmosferskom tlaku. Zato Bernoulli između slobodne površine i otvora prelazi u Torricellijev zapis za izlaznu brzinu. Nakon izlaza mlaz se dalje giba kao vodoravno izbačeno tijelo.

**Rješenje**

Iz Bernoullija između slobodne površine i otvora slijedi $v_0 = \sqrt{2g(H-h)}$, a vrijeme pada mlaza s visine $h$ do tla glasi $t = \sqrt{2h/g}$, pa je horizontalni domet

$$
x = v_0 t = \sqrt{2g(H-h)}\,\sqrt{\frac{2h}{g}} = 2\sqrt{h(H-h)}.
$$ {#eq-energijska-bilanca-rijeseni-primjer-domet-slobodnog-mlaza-iz-veliko-01}

Sada izračunajmo domet za tri zadana položaja.

Za $h = 1{,}0\ \text{m}$:

$$
x = 2\sqrt{1{,}0(4{,}0 - 1{,}0)} = 2\sqrt{3} \approx 3{,}46\ \text{m}.
$$ {#eq-energijska-bilanca-rijeseni-primjer-domet-slobodnog-mlaza-iz-veliko-02}

Za $h = 2{,}0\ \text{m}$:

$$
x = 2\sqrt{2{,}0(4{,}0 - 2{,}0)} = 2\sqrt{4} = 4{,}00\ \text{m}.
$$ {#eq-energijska-bilanca-rijeseni-primjer-domet-slobodnog-mlaza-iz-veliko-03}

Za $h = 3{,}0\ \text{m}$:

$$
x = 2\sqrt{3{,}0(4{,}0 - 3{,}0)} = 2\sqrt{3} \approx 3{,}46\ \text{m}.
$$ {#eq-energijska-bilanca-rijeseni-primjer-domet-slobodnog-mlaza-iz-veliko-04}

Vidimo da je domet najveći kad je otvor postavljen na polovicu visine slobodne površine iznad tla, odnosno za $h = H/2$. Tada vrijedi $x_{max} = H$, pa je u ovom primjeru maksimalni domet jednak

$$
x_{max} = 4{,}0\ \text{m}.
$$ {#eq-energijska-bilanca-rijeseni-primjer-domet-slobodnog-mlaza-iz-veliko-05}

**Provjera i komentar**

Slobodni mlaz ne dobiva najveći domet ni iz najviše ni iz najniže postavljenog otvora. Maksimum nastaje točno na polovici ukupne visine, gdje se najpovoljnije uravnoteže izlazna brzina i vrijeme leta.

1. Ako je otvor prenisko, vrijeme leta je kratko i domet pada iako je brzina velika.
2. Ako je otvor previsoko, vrijeme leta je dugo, ali izlazna brzina pada jer je visinska razlika do slobodne površine mala.
3. Položaji $h$ i $H-h$ daju isti domet jer se u izrazu pojavljuje njihov umnožak.
:::

::: {#ex-u09-privremeni-sifon-za-praznjenje-servisnog-bazena-t2 .mf1-we}
<p class="mf1-box-label">Privremeni sifon za pražnjenje servisnog bazena&nbsp;<span class="mf1-level">T2</span></p>

**Kontekst:** Pri privremenom pražnjenju servisnog bazena postavlja se sifon koji premošćuje rub bazena i odvodi vodu u niži ispustni kanal. Operater iz visinske razlike određuje brzinu i protok sifona te provjerava tlak u njegovoj najvišoj točki kako bi se isključila opasnost od isparavanja.

**Zadano**

- Promjer idealiziranog sifona: $D = 80\ \text{mm}$
- Visinska razlika od slobodne površine bazena A do otvorenog izlaznog presjeka cijevi B: $\Delta z = 3{,}6\ \text{m}$
- Visina najviše točke sifona `C` iznad slobodne površine bazena: $z_C = 2{,}2\ \text{m}$
- Atmosferska tlačna visina: $10{,}2\ \text{m}$ vodenog stupca
- Tlačna visina zasićene pare: $0{,}25\ \text{m}$ vodenog stupca
- Gubici u sifonu se zanemaruju; bazen je velik i otvoren, a cijev B završava slobodnim mlazom u zraku iznad ispustnog kanala. Sifon je napunjen vodom i ulaz je uronjen; promatra se kvazistacionarni trenutak.

**Traženo**

1. brzinu strujanja $v$ u sifonskoj cijevi.
2. volumenski protok $Q$.
3. tlačnu visinu $p_C/\gamma$ u najvišoj točki `C` i idealiziranu razliku apsolutne tlačne visine prema zadanoj visini tlaka pare ako je atmosferska visina $10{,}2\ \text{m}$ vodenog stupca, a visina tlaka pare $0{,}25\ \text{m}$ vodenog stupca.

![Idealni sifon sa slobodnim izlazom B iznad prihvatnog kanala.](../assets/print/u09_val3_idealni_sifon.svg){#fig-u09-idealni-sifon-izme-u-dviju-razina fig-alt="Napunjen sifon: ulaz je uronjen u bazen A, vrh je C, a izlaz B otvoren prema atmosferi."}

**Pretpostavke i model**

Slobodna površina A i slobodni izlaz B na atmosferskom su tlaku. Brzina na površini A je zanemariva, dok je u B jednaka brzini u cijevi stalnog promjera. Bernoulli između A i B daje idealnu brzinu sifona; između A i C daje tlačnu visinu u vrhu. Slobodna površina prihvatnog kanala nije izlazni presjek ove bilance.

**Rješenje**

Iz Bernoullija između slobodne površine bazena `A` i izlaznog presjeka cijevi `B` slijedi

$$
\frac{p_A}{\gamma} + \frac{v_A^2}{2g} + z_A = \frac{p_B}{\gamma} + \frac{v_B^2}{2g} + z_B.
$$ {#eq-energijska-bilanca-rijeseni-primjer-privremeni-sifon-za-praznjenje-01}

Kako su $p_A = p_B = p_{atm}$, $v_A \approx 0$ i $v_B=v$, ostaje $z_A - z_B = v^2/(2g) = \Delta z$, pa je brzina u sifonskoj cijevi

$$
v = \sqrt{2g\Delta z} = \sqrt{2 \cdot 9{,}81 \cdot 3{,}6} \approx 8{,}40\ \text{m/s}.
$$ {#eq-energijska-bilanca-rijeseni-primjer-privremeni-sifon-za-praznjenje-02}

Površina presjeka cijevi iznosi

$$
A = \frac{\pi D^2}{4} = \frac{\pi \cdot 0{,}08^2}{4} \approx 5{,}03 \cdot 10^{-3}\ \text{m}^2,
$$ {#eq-energijska-bilanca-rijeseni-primjer-privremeni-sifon-za-praznjenje-03}

zato je volumenski protok

$$
Q = Av = 5{,}03 \cdot 10^{-3} \cdot 8{,}40 \approx 4{,}22 \cdot 10^{-2}\ \text{m}^3/\text{s} \approx 42{,}2\ \text{L/s}.
$$ {#eq-energijska-bilanca-rijeseni-primjer-privremeni-sifon-za-praznjenje-04}

Sada zapišimo Bernoullija između slobodne površine bazena `A` i vrha sifona `C`. Uzmimo $z_A = 0$, pa je $z_C = 2{,}2\ \text{m}$:

$$
\frac{p_{atm}}{\gamma} = \frac{p_C}{\gamma} + \frac{v^2}{2g} + z_C.
$$ {#eq-energijska-bilanca-rijeseni-primjer-privremeni-sifon-za-praznjenje-05}

Ako radimo s manometarskim tlakom u odnosu na atmosferu, to prelazi u $0 = p_C/\gamma + 3{,}6 + 2{,}2$, pa je

$$
\frac{p_C}{\gamma} = -5{,}8\ \text{m}.
$$ {#eq-energijska-bilanca-rijeseni-primjer-privremeni-sifon-za-praznjenje-06}

Manometarska tlačna visina u C iznosi $-5{,}8\ \text{m}$. Lokalni HGL uključuje i geodetsku visinu: $HGL_C=z_C+p_{C,man}/\gamma=2{,}2-5{,}8=-3{,}6\ \text{m}$, pa je 3,6 m ispod slobodne površine bazena. Tlačna visina mjeri se od osi cijevi, a HGL od odabrane referentne ravnine.

To znači da je apsolutna tlačna visina u točki `C`

$$
\left(\frac{p_C}{\gamma}\right)_{abs} = 10{,}2 - 5{,}8 = 4{,}4\ \text{m}.
$$ {#eq-energijska-bilanca-rijeseni-primjer-privremeni-sifon-za-praznjenje-07}

Ako rezultat želimo vratiti u tlak, tada slijedi

$$
p_{C,man} = \rho g\left(\frac{p_C}{\gamma}\right) = 1000 \cdot 9{,}81 \cdot (-5{,}8) \approx -56{,}9\ \text{kPa},
$$ {#eq-energijska-bilanca-rijeseni-primjer-privremeni-sifon-za-praznjenje-08}

te apsolutni tlak

$$
p_{C,abs} = \rho g\left(\frac{p_C}{\gamma}\right)_{abs} = 1000 \cdot 9{,}81 \cdot 4{,}4 \approx 43{,}2\ \text{kPa}.
$$ {#eq-energijska-bilanca-rijeseni-primjer-privremeni-sifon-za-praznjenje-09}

Kako je visina tlaka pare $p_v/\gamma=0{,}25\ \text{m}$, idealni model daje razliku $4{,}4-0{,}25=4{,}15\ \text{m}$ vodenog stupca prema tomu lokalnom kriteriju.

**Provjera i komentar**

Idealni sifon daje brzinu od oko $8{,}4\ \text{m/s}$ i protok od oko $42\ \text{L/s}$. U vrhu sifona tlak pada na $-5{,}8\ \text{m}$ manometarske visine, dok je apsolutna tlačna visina oko $4{,}4\ \text{m}$ vode. Dobivena razlika prema tlaku pare pripada idealnom modelu; stvarna provjera mora uključiti gubitke, temperaturu, prolazne pojave, otopljene plinove i lokalne minimume tlaka. To je prijelaz iz []{.mf1-chapter-ref target="u08"} prema []{.mf1-chapter-ref target="u13"}.

1. Što je donja razina dublje ispod gornje, to idealna brzina sifona mora biti veća.
2. Tlak u vrhu sifona mora biti manji od atmosferskog jer se dio ukupne energije troši na visinu vrha i na brzinski član.
3. Ako bi izračunana apsolutna tlačna visina pala ispod tlačne visine zasićene pare, čisti idealni model više ne bi bio dovoljan za fizikalno uvjerljiv odgovor.
:::

::: {#ex-u09-idealni-bypass-sifon-sa-suzenjem-u-vrhu .mf1-ch}
<p class="mf1-box-label">Idealni obilazni sifon sa suženjem u vrhu i mlaznim ispustom&nbsp;<span class="mf1-level">T3</span></p>

**Kontekst:** Idealizirani obilazni sifon premošćuje rub bazena, ima suženje u najvišoj točki i završava slobodnim vodoravnim mlazom iznad podloge. Traže se protok, brzina i tlak u suženju, modelska razlika prema tlaku pare te vodoravni domet mlaza.

**Zadano**

- Glavni promjer sifonske cijevi: $D = 100\ \text{mm}$
- Promjer suženja u najvišoj točki `C`: $d_C = 80\ \text{mm}$
- Visina slobodne površine bazena `A` iznad podloge: $4{,}2\ \text{m}$
- Visina vodoravnog izlaza `B` iznad podloge: $1{,}4\ \text{m}$
- Visina najviše točke sifona `C` iznad slobodne površine bazena: $z_C = 1{,}5\ \text{m}$
- Tlak na slobodnoj površini i na izlazu je atmosferski; brzina na slobodnoj površini je zanemariva
- Atmosferska tlačna visina: $10{,}2\ \text{m}$ vodenog stupca
- Tlačna visina zasićene pare: $0{,}25\ \text{m}$ vodenog stupca
- Gubici se zanemaruju

**Traženo**

1. brzinu strujanja $v_B$ u glavnoj cijevi na izlazu i volumenski protok $Q$.
2. brzinu $v_C$ u suženju pri vrhu sifona.
3. manometarsku i apsolutnu tlačnu visinu u točki `C`.
4. razliku apsolutne tlačne visine prema visini tlaka pare ako je atmosferska visina $10{,}2\ \text{m}$ vodenog stupca, a visina tlaka pare $0{,}25\ \text{m}$ vodenog stupca.
5. vodoravni domet mlaza nakon izlaza iz točke `B`.

![Idealni obilazni sifon sa suženjem](../assets/print/u09_ch1_bypass_sifon_suzenje_mlaz.svg){#fig-u09-idealni-bypass-sifon-sa-suzenjem fig-alt="Idealni obilazni sifon sa suženjem"}

**Pretpostavke i model**

Ovdje se isti idealni tok analizira u trima referentnim presjecima. Bernoulli između slobodne površine `A` i izlaza `B` daje glavnu izlaznu brzinu. Kontinuitet zatim iz te iste vrijednosti vraća veću brzinu u suženju `C`, a Bernoulli između `A` i `C` pokazuje koliko pritom mora pasti statički tlak. Nakon izlaza iz `B` mlaz više ne pripada unutarnjem strujanju cijevi nego gibanju vodoravno izbačenog tijela.

**Rješenje**

Najprije iz geometrije sustava slijedi visinska razlika između slobodne površine i izlaza:

$$
\Delta z_{AB} = 4{,}2 - 1{,}4 = 2{,}8\ \text{m}.
$$ {#eq-energijska-bilanca-cjeloviti-zadatak-idealni-bypass-sifon-sa-suzenj-01}

Bernoulli između slobodne površine `A` i izlaza `B` daje

$$
\frac{p_A}{\gamma} + \frac{v_A^2}{2g} + z_A = \frac{p_B}{\gamma} + \frac{v_B^2}{2g} + z_B.
$$ {#eq-energijska-bilanca-cjeloviti-zadatak-idealni-bypass-sifon-sa-suzenj-02}

Kako su $p_A = p_B = p_{atm}$ i $v_A \approx 0$, ostaje

$$
v_B = \sqrt{2g\Delta z_{AB}} = \sqrt{2 \cdot 9{,}81 \cdot 2{,}8} \approx 7{,}41\ \text{m/s}.
$$ {#eq-energijska-bilanca-cjeloviti-zadatak-idealni-bypass-sifon-sa-suzenj-03}

Površina glavne cijevi iznosi

$$
A = \frac{\pi D^2}{4} = \frac{\pi \cdot 0{,}10^2}{4} \approx 7{,}854 \cdot 10^{-3}\ \text{m}^2,
$$ {#eq-energijska-bilanca-cjeloviti-zadatak-idealni-bypass-sifon-sa-suzenj-04}

pa je volumenski protok

$$
Q = Av_B = 7{,}854 \cdot 10^{-3} \cdot 7{,}41 \approx 5{,}82 \cdot 10^{-2}\ \text{m}^3/\text{s} \approx 58{,}2\ \text{L/s}.
$$ {#eq-energijska-bilanca-cjeloviti-zadatak-idealni-bypass-sifon-sa-suzenj-05}

Površina suženja pri vrhu sifona je

$$
A_C = \frac{\pi d_C^2}{4} = \frac{\pi \cdot 0{,}08^2}{4} \approx 5{,}027 \cdot 10^{-3}\ \text{m}^2,
$$ {#eq-energijska-bilanca-cjeloviti-zadatak-idealni-bypass-sifon-sa-suzenj-06}

pa iz kontinuiteta slijedi

$$
v_C = \frac{Q}{A_C} = \frac{5{,}82 \cdot 10^{-2}}{5{,}027 \cdot 10^{-3}} \approx 11{,}58\ \text{m/s}.
$$ {#eq-energijska-bilanca-cjeloviti-zadatak-idealni-bypass-sifon-sa-suzenj-07}

Sada pišemo Bernoullija između slobodne površine `A` i točke `C`. Uzmemo li manometarski tlak u odnosu na atmosferu, vrijedi $0 = p_C/\gamma + v_C^2/(2g) + z_C$, pa je manometarska tlačna visina u vrhu sifona

$$
\frac{p_C}{\gamma} = -\left(\frac{11{,}58^2}{2 \cdot 9{,}81} + 1{,}5\right) = -(6{,}84 + 1{,}5) = -8{,}34\ \text{m}.
$$ {#eq-energijska-bilanca-cjeloviti-zadatak-idealni-bypass-sifon-sa-suzenj-08}

Apsolutna tlačna visina u točki `C` zato iznosi

$$
\left(\frac{p_C}{\gamma}\right)_{abs} = 10{,}2 - 8{,}34 = 1{,}86\ \text{m}.
$$ {#eq-energijska-bilanca-cjeloviti-zadatak-idealni-bypass-sifon-sa-suzenj-09}

Modelska razlika prema visini tlaka pare tada je $1{,}86-0{,}25=1{,}61\ \text{m}$. To je provjera idealnog stacionarnog računa, ne sigurnosna margina izvedenoga sifona.

Nakon izlaza iz točke `B` mlaz se giba kao vodoravno izbačeno tijelo s početnom visinom $h_B = 1{,}4\ \text{m}$. Vrijeme pada do podloge iznosi

$$
t = \sqrt{\frac{2h_B}{g}} = \sqrt{\frac{2 \cdot 1{,}4}{9{,}81}} \approx 0{,}534\ \text{s},
$$ {#eq-energijska-bilanca-cjeloviti-zadatak-idealni-bypass-sifon-sa-suzenj-10}

pa je vodoravni domet mlaza

$$
x = v_B t = 7{,}41 \cdot 0{,}534 \approx 3{,}96\ \text{m}.
$$ {#eq-energijska-bilanca-cjeloviti-zadatak-idealni-bypass-sifon-sa-suzenj-11}

**Provjera i komentar**

Ovaj zadatak povezuje postupke idealnog modela iz []{.mf1-chapter-ref target="u08"} u jednom sustavu: Bernoulli između slobodne površine i izlaza daje brzinu oko $7{,}41\ \text{m/s}$ i protok oko $58{,}2\ \text{L/s}$, kontinuitet povećava brzinu u suženju vrha na oko $11{,}58\ \text{m/s}$, a tlak u točki `C` pada na oko $-8{,}34\ \text{m}$ manometarske visine. Ipak, apsolutna tlačna visina ostaje oko $1{,}86\ \text{m}$ vode, što je još oko $1{,}61\ \text{m}$ iznad tlačne visine zasićene pare. Nakon izlaza mlaz doseže vodoravni domet od oko $3{,}96\ \text{m}$.

1. U suženju mora biti $v_C > v_B$ jer isti protok prolazi kroz manji presjek.
2. Tlak u vrhu sifona mora biti manji od atmosferskog, a u suženju pada još više zbog veće brzine.
3. Ako se pri računu dometa koristi $v_C$ umjesto izlazne brzine $v_B$, pomiješani su unutarnji presjek sifona i stvarni izlazni mlaz.
:::

U []{.mf1-chapter-ref target="u08"} još ne treba crtati komplicirane energetske sheme, ali treba razumjeti osnovnu logiku: `EGL` prati ukupnu mehaničku energiju po jedinici težine, `HGL` zbroj tlačne i geodetske visine, a u idealnom toku `EGL` ostaje vodoravna dok se `HGL` spušta kad raste brzinski član. Takav prikaz u Venturijevoj cijevi i Pitotovoj sondi pokazuje odnos promjene tlaka i brzine.

::: {#ex-u09-venturijeva-cijev-za-mjerenje-protoka-ulja-t2 .mf1-we}
<p class="mf1-box-label">Venturijeva cijev za mjerenje protoka ulja &nbsp;<span class="mf1-level">T2</span></p>


**Kontekst:** U industrijskom maznom sustavu Venturijeva cijev mjeri protok ulja. Diferencijalnim manometrom (živa u U-cijevi) mjeri se razlika tlakova između ulaza i grla. Iz te razlike se računa protok.

**Zadano**

- Promjer ulaza: $D_1 = 60\ \text{mm}$
- Promjer grla: $D_2 = 30\ \text{mm}$
- Razlika očitanja diferencijalnog manometra: $\Delta h_m = 0{,}18\ \text{m}$ žive ($\rho_{Hg} = 13600\ \text{kg/m}^3$)
- Gustoća ulja: $\rho_{ul} = 870\ \text{kg/m}^3$
- Cijev je horizontalna; zanemari gubitke

**Traženo**

Volumenski protok ulja $Q$.

![Venturijeva cijev: D1=60 mm, D2=30 mm, Δh_m=0,18 m žive, Q≈5,248 L/s](../assets/print/u09_fig_venturijeva_cijev.svg){#fig-u09-venturijeva-cijev fig-align="center" fig-alt="Venturijeva cijev: D1=60 mm, D2=30 mm, Δh_m=0,18 m žive, Q≈5,248 L/s"}

**Rješenje**

Razlika tlakova između presjeka 1 i 2 iz diferencijalnog manometra:
$$
\Delta p = (\rho_{Hg} - \rho_{ul})\,g\,\Delta h_m = (13600 - 870) \cdot 9{,}81 \cdot 0{,}18 \approx 22{,}479\ \text{kPa}
$$ {#eq-energijska-bilanca-rijeseni-primjer-venturijeva-cijev-za-mjerenje-p-01}

Za horizontalnu cijev ($z_1 = z_2$) iz Bernoullija:
$$
\Delta p = \frac{\rho_{ul}}{2}(v_2^2 - v_1^2)
$$ {#eq-energijska-bilanca-rijeseni-primjer-venturijeva-cijev-za-mjerenje-p-02}

Iz kontinuiteta: $v_2 = v_1(A_1/A_2) = v_1(D_1/D_2)^2 = 4 v_1$

$$
\Delta p = \frac{\rho_{ul}}{2}(16 v_1^2 - v_1^2) = \frac{15\rho_{ul}}{2} v_1^2
$$ {#eq-energijska-bilanca-rijeseni-primjer-venturijeva-cijev-za-mjerenje-p-03}

$$
v_1 = \sqrt{\frac{2\Delta p}{15\rho_{ul}}} = \sqrt{\frac{2 \cdot 22478{,}634}{15 \cdot 870}} \approx \sqrt{3{,}445} \approx 1{,}856\ \text{m/s}
$$ {#eq-energijska-bilanca-rijeseni-primjer-venturijeva-cijev-za-mjerenje-p-04}

$$
Q = A_1 v_1 = \frac{\pi D_1^2}{4}v_1 \approx 0{,}005248\ \text{m}^3/\text{s} = 5{,}248\ \text{L/s}
$$ {#eq-energijska-bilanca-rijeseni-primjer-venturijeva-cijev-za-mjerenje-p-05}

**Provjera i komentar**

Brzina u grlu iznosi $v_2=7{,}424\ \text{m/s}$, a `HGL` je ondje za $\Delta p/(\rho g)=2{,}634\ \text{m}$ niže nego na ulazu. Diferencijalni manometar daje samo razliku tlakova: bez apsolutnog ulaznog tlaka, temperature i tlaka pare ulja iz ovoga se računa ne može zaključiti postoji li kavitacijska rezerva.

::: {.mf1-numerika .kompakt}
<p class="mf1-box-label">Od ručnog Venturija do polja</p>

Ovaj idealni račun daje referencu za @sec-cfd-venturi. Ondje se isti problem proširuje poljem brzine i tlaka, uz jasno odvajanje fizikalnih gubitaka od numeričke pogreške.
:::

:::

Venturijevom cijevi protok se određuje iz razlike statičkih tlakova. U sljedećem se primjeru Pitotovom sondom brzina određuje iz razlike stagnacijskog i statičkog tlaka.

::: {#ex-u09-pitot-staticka-sonda-na-bespilotnoj-letjelici-za .mf1-we}
<p class="mf1-box-label">Pitot-statička sonda na bespilotnoj letjelici za mjerenje brzine leta &nbsp;<span class="mf1-level">T2</span></p>

**Kontekst:** Bespilotne letjelice (dronovi) korištene u geodetskim, poljoprivrednim i inspekcijskim mjerenjima opremljene su Pitot-statičkom sondom za mjerenje vlastite brzine u odnosu na okolni zrak. Sonda mjeri razliku između stagnacijskog tlaka na čelu sonde i statičkog tlaka okolnog strujanja, iz čega se Bernoullijevom jednadžbom izračunava brzina leta.

**Zadano**

- Razlika izmjerenih tlakova: $\Delta p = p_{st} - p_{\infty} = 380\ \text{Pa}$
- Gustoća zraka na visini leta od $500\ \text{m}$ pri temperaturi $12^\circ\text{C}$: $\rho = 1{,}115\ \text{kg/m}^3$
- Sonda je orijentirana paralelno s pravcem leta
- Promjer otvora sonde: $D_s = 5\ \text{mm}$
- Kinematička viskoznost zraka: $\nu = 1{,}5 \cdot 10^{-5}\ \text{m}^2/\text{s}$

**Traženo**

1. Brzina leta letjelice prema očitanju sonde;
2. Procjena: kako bi se promijenila preračunata brzina u gušćem zraku ($\rho = 1{,}25\ \text{kg/m}^3$) uz isti $\Delta p$;
3. Red veličine Reynoldsova broja sonde i što se iz njega smije zaključiti.

**Pretpostavke i model**

Strujanje zraka oko sonde smatra se stacionarnim i nestlačivim (Machov broj $\ll 0{,}3$). Zanemaruje se viskozni efekt na samoj sondi, kao i utjecaj smjera vjetra koji nije paralelan s osi letjelice. Točka 1 odgovara neporemećenom strujanju daleko od sonde, a točka 2 stagnacijskoj točki na čelu sonde u kojoj se zrak zaustavlja ($v_2 = 0$). Leti se na konstantnoj visini, pa članovi geodetske visine otpadaju.

**Rješenje**

Bernoullijeva jednadžba između neporemećene struje i stagnacijske točke daje:

$$
p_{\infty} + \frac{\rho v^2}{2} = p_{st}.
$$ {#eq-energijska-bilanca-rijeseni-primjer-pitot-staticka-sonda-na-bespilo-01}

Iz toga slijedi izraz za brzinu leta:

$$
v = \sqrt{\frac{2\,\Delta p}{\rho}} = \sqrt{\frac{2 \cdot 380}{1{,}115}}.
$$ {#eq-energijska-bilanca-rijeseni-primjer-pitot-staticka-sonda-na-bespilo-02}

Računaju se redom $2 \cdot 380 = 760$ i $760/1{,}115 \approx 681{,}6$:

$$
v = \sqrt{681{,}6} \approx 26{,}1\ \text{m/s}.
$$ {#eq-energijska-bilanca-rijeseni-primjer-pitot-staticka-sonda-na-bespilo-03}

U gušćem zraku, uz $\rho = 1{,}25\ \text{kg/m}^3$ i isti izmjereni $\Delta p$, brzina bi se preračunala na:

$$
v_o = \sqrt{\frac{2 \cdot 380}{1{,}25}} = \sqrt{608} \approx 24{,}7\ \text{m/s}.
$$ {#eq-energijska-bilanca-rijeseni-primjer-pitot-staticka-sonda-na-bespilo-04}

Razlika u izračunatoj brzini iznosi približno $1{,}4\ \text{m/s}$ ili $5{,}4\,\%$ — značajna pogreška ako se ne primjenjuje korekcija prema lokalnoj gustoći zraka.

Reynoldsov broj oko sonde:

$$
Re_s = \frac{v\,D_s}{\nu} = \frac{26{,}1 \cdot 0{,}005}{1{,}5 \cdot 10^{-5}} \approx 8\,700.
$$ {#eq-energijska-bilanca-rijeseni-primjer-pitot-staticka-sonda-na-bespilo-05}

Vrijednost $Re_s$ reda $10^4$ samo određuje omjer inercijskih i viskoznih učinaka za odabranu karakterističnu duljinu. Granice $2300/4000$ vrijede za razvijeno strujanje u kružnoj cijevi i ne smiju se prenijeti na vanjsko strujanje oko Pitotove sonde. Sam $Re_s$ zato ne dokazuje ni „turbulentnost sonde” ni točnost mjerenja; za to su potrebni geometrija, kut nastrujavanja i kalibracijska karakteristika sonde.

**Provjera i komentar**

Brzina od $26{,}1\ \text{m/s}$ odgovara približno $94\ \text{km/h}$. Promjena pretpostavljene gustoće od oko $12\,\%$ mijenja preračunatu brzinu za oko $5\,\%$, pa mjerenje koje traži malu nesigurnost mora koristiti lokalnu procjenu gustoće i kalibraciju cijelog mjernog lanca. Pri maloj brzini dinamički tlak pada s $v^2$, pa odnos signala i šuma postaje lošiji; konkretna donja mjerna granica ovisi o senzoru, sondi i obradi signala, a ne o jednoj univerzalnoj brzini.
:::

::: {.mf1-samoprovjera}
<p class="mf1-box-label">Provjeri sebe</p>

Sljedeća pitanja služe za samostalnu provjeru razumijevanja prije prelaska na zadatke za vježbu.

1. Pod kojim sve uvjetima vrijedi klasična Bernoullijeva jednadžba u obliku iz ovog poglavlja?

::: {.callout-note collapse="true"}
### Odgovor
Vrijedi za stacionarno strujanje, nestlačivi fluid (gustoća konstantna), neviskozno strujanje (bez disipacije), bez strojnog rada (bez pumpe ili turbine) i između točaka na istoj strujnici. Ako neki od tih uvjeta nije zadovoljen, treba primijeniti model koji uključuje relevantne učinke. Gubitci i strojni rad obrađuju se u poglavlju 13.
:::

2. Po čemu se razlikuju energetska linija (EGL) i hidraulička linija (HGL) i kako se one ponašaju u idealnom strujanju?

::: {.callout-note collapse="true"}
### Odgovor
EGL je zbroj tlačne, brzinske i geodetske visine, a HGL samo tlačne i geodetske. U idealnom strujanju EGL ostaje konstantna duž strujnice (energija je očuvana), dok HGL pada gdje brzina raste i obratno, jer se razlikuju upravo za brzinsku visinu $v^2/(2g)$.
:::

3. Zašto se Torricellijeva formula $v = \sqrt{2gH}$ izvodi izravno iz Bernoullijeve jednadžbe?

::: {.callout-note collapse="true"}
### Odgovor
Postavljanjem Bernoullija između slobodne površine velikog spremnika (brzina nula, tlak atmosferski, visina $H$) i izlaznog presjeka male sapnice (tlak atmosferski, visina nula) poništavaju se jednaki tlačni članovi, a ostaje razlika geodetskih visina i ostaje $v^2/(2g) = H$, odakle slijedi $v = \sqrt{2gH}$.
:::

4. Kada se Bernoulli koristi za istjecanje, je li dobiveni rezultat za $v$ pretežno gornja ili donja granica stvarne brzine?

::: {.callout-note collapse="true"}
### Odgovor
Gornja granica. Stvarna brzina je manja jer u idealnom modelu nisu uračunati gubitci trenja, lokalne disipacije na ulazu u sapnicu i mogući viskozni profil brzina. Pri računanju protoka primjenjuje se koeficijent istjecanja $C_d < 1$, koji obuhvaća i smanjenje brzine i kontrakciju mlaza. Zato taj koeficijent ne treba automatski tumačiti kao omjer stvarne i idealne brzine.
:::
:::

## Zadaci za vježbu

Za sve vježbe uzmi $g=9{,}81\ \text{m/s}^2$.

::::: {.mf1-vjezbe-list}

### Istjecanje iz otvorenog spremnika {#task-u09-veliki-otvoreni-spremnik-sadrzi-vodu-do-visine .unnumbered .unlisted}

Veliki otvoreni spremnik sadrži vodu do visine $H = 3{,}20\ \text{m}$ iznad osi male bočne sapnice promjera $d = 26\ \text{mm}$. Za vodu uzmi $\rho=998\ \text{kg/m}^3$. Promatraj kvazistacionarni trenutak dok se razina velikog spremnika zanemarivo mijenja. Zanemari gubitke i odredi izlaznu brzinu mlaza, volumenski protok i maseni protok vode.

:::: {.content-visible .mf1-hint-online when-format="html"}
::: {.callout-note collapse="true" data-hint-key="true"}
### Naputak
Između slobodne površine i izlaza vrijedi Torricelli: $v = \sqrt{2gH}$; nakon toga $Q = Av$ i $\dot m = \rho Q$.
:::
::::
:::: {.content-visible .mf1-answer-online when-format="html"}
::: {.callout-tip collapse="true" data-answer-key="true"}
### Kontrolni rezultat

$v \approx 7{,}92\ \text{m/s}$; $Q \approx 4{,}21\ \text{L/s}$; $\dot m \approx 4{,}20\ \text{kg/s}$.
:::
::::

[Razina: T1]{.mf1-task-level}

### Tlak u suženju ventilacijskog kanala {#task-u09-horizontalnim-ventilacijskim-kanalom-smanjuje-se-presjek-s .unnumbered .unlisted}

U horizontalnom ventilacijskom kanalu presjek se smanjuje s $A_1 = 0{,}060\ \text{m}^2$ na $A_2 = 0{,}020\ \text{m}^2$. Volumenski protok zraka iznosi $Q = 0{,}42\ \text{m}^3/\text{s}$, a gustoća zraka je $\rho = 1{,}20\ \text{kg/m}^3$. Pretpostavi stacionarni nestlačivi tok bez gubitaka i bez strojnog rada. Odredi pad statičkog tlaka.

:::: {.content-visible .mf1-hint-online when-format="html"}
::: {.callout-note collapse="true" data-hint-key="true"}
### Naputak
Iz kontinuiteta dobij $v_1$ i $v_2$, a za horizontalni kanal bez gubitaka vrijedi $p_1 + \rho v_1^2/2 = p_2 + \rho v_2^2/2$.
:::
::::
:::: {.content-visible .mf1-answer-online when-format="html"}
::: {.callout-tip collapse="true" data-answer-key="true"}
### Kontrolni rezultat

$v_1 = 7{,}0\ \text{m/s}$, $v_2 = 21{,}0\ \text{m/s}$; $\Delta p \approx 235\ \text{Pa}$.
:::
::::

[Razina: T1]{.mf1-task-level}

<span id="task-u09-idealna-venturijeva-cijev-za-vodu-ima-ulazni"></span>

### Tlak u silaznom suženju {#task-tlak-u-silaznom-suzenju .unnumbered .unlisted}

Voda gustoće $\rho=1000\ \text{kg/m}^3$ stacionarno teče kroz glatko silazno suženje. U vodoravnom ulaznom presjeku 1 promjer je $D_1=120\ \text{mm}$, a u vodoravnom izlaznom presjeku 2 $D_2=70\ \text{mm}$. Os presjeka 1 nalazi se $z_1-z_2=2{,}00\ \text{m}$ iznad osi presjeka 2. Volumenski protok je $Q=20{,}0\ \text{L/s}$. Zanemari gubitke, pretpostavi jednolike brzine u referentnim presjecima i odredi obje brzine te razliku $p_2-p_1$. Provjeri tvrdnju: „U svakom suženju tlak mora pasti.”

:::: {.content-visible .mf1-hint-online when-format="html"}
::: {.callout-note collapse="true" data-hint-key="true"}
### Naputak
Najprije iz protoka odredi obje brzine. U Bernoulliju zadrži razliku geodetskih visina. Usporedi doprinos spuštanja s doprinosom ubrzanja; tlak i HGL nisu ista veličina.
:::
::::
:::: {.content-visible .mf1-answer-online when-format="html"}
::: {.callout-tip collapse="true" data-answer-key="true"}
### Kontrolni rezultat

$v_1\approx1{,}768\ \text{m/s}$; $v_2\approx5{,}197\ \text{m/s}$; $p_2-p_1\approx+7{,}680\ \text{kPa}$. Tlak raste jer doprinos spuštanja $19{,}620\ \text{kPa}$ nadmašuje doprinos ubrzanja $11{,}940\ \text{kPa}$. Tvrdnja nije općenito točna: u ovom idealnom toku pada HGL, dok statički tlak raste.
:::
::::

[Razina: T2]{.mf1-task-level}

<span id="task-u09-pitotova-cijev-uronjena-je-u-vodeni-tok"></span>

### Pitot s izdignutim senzorom {#task-pitot-s-izdignutim-senzorom .unnumbered .unlisted}

Pitotova sonda okrenuta je otvorom prema jednolikoj struji vode gustoće $\rho=1000\ \text{kg/m}^3$. U neporemećenoj struji A, na visini otvora sonde, statički manometarski tlak iznosi $p_{M,A}=16{,}0\ \text{kPa}$. Sonda je potpuno ispunjena mirujućom vodom i spojena na senzor S koji se nalazi $\Delta z_S=1{,}20\ \text{m}$ iznad njezina otvora. Senzor očitava $p_{M,S}=24{,}0\ \text{kPa}$ prema istoj atmosferskoj referenci. Odredi stagnacijski tlak na otvoru i lokalnu brzinu neporemećene struje. Koliku bi brzinu dao račun koji zanemari visinsku razliku senzora? Zanemari gubitke pri zaustavljanju struje i kapilarne učinke; u mjernom vodu nema zraka ni protoka.

:::: {.content-visible .mf1-hint-online when-format="html"}
::: {.callout-note collapse="true" data-hint-key="true"}
### Naputak
Očitanje u S prvo hidrostatički prenesi na visinu otvora sonde. Tek tada oduzmi statički tlak u A i primijeni Bernoullija između neporemećene struje i stagnacijske točke.
:::
::::
:::: {.content-visible .mf1-answer-online when-format="html"}
::: {.callout-tip collapse="true" data-answer-key="true"}
### Kontrolni rezultat

Stagnacijski manometarski tlak je $p_{M,st}=35{,}772\ \text{kPa}$, a razlika prema statičkom tlaku $19{,}772\ \text{kPa}$. Lokalna brzina je $v\approx6{,}288\ \text{m/s}$. Zanemarivanje visine senzora dalo bi $v_{pog}=4{,}000\ \text{m/s}$, odnosno podcijenjenu brzinu.
:::
::::

[Razina: T2]{.mf1-task-level}

<span id="task-u09-idealni-sifon-prazni-otvoreni-spremnik-razlika-razina"></span>

### Odabir grla prema tlaku i mjernom signalu {#task-odabir-grla-prema-tlaku .unnumbered .unlisted}

Kroz vodoravni mjerni sklop prolazi zadani stalni protok vode $Q=20{,}0\ \text{L/s}$ pri gustoći $\rho=1000\ \text{kg/m}^3$. Ulazni promjer je $D_1=100\ \text{mm}$, a apsolutni ulazni tlak $p_{1,abs}=150\ \text{kPa}$. Glatki zamjenjivi ulošci imaju promjere grla $d=40$, $50$ ili $60\ \text{mm}$. U idealnom modelu bez gubitaka potrebno je istodobno ostvariti apsolutni tlak u grlu $p_{C,abs}\ge60\ \text{kPa}$ i razliku statičkih tlakova za mjerenje $p_1-p_C\ge40\ \text{kPa}$. Izvedi dopušteni interval promjera grla, odaberi uložak i provjeri oba uvjeta za sve tri ponuđene izvedbe. Pretpostavi jednolike brzine u referentnim presjecima; zadani protok i ulazni tlak održavaju se za svaki uložak. Tlačni prag je zadani pogonski kriterij, a ne tlak pare vode.

:::: {.content-visible .mf1-hint-online when-format="html"}
::: {.callout-note collapse="true" data-hint-key="true"}
### Naputak
Iz kontinuiteta izrazom za brzinu u grlu prijeđi s promjera na pad tlaka. Minimalni apsolutni tlak ograničava najveći dopušteni pad, a minimalni mjerni signal najmanji pad. Tek nakon određivanja obaju rubova intervala usporedi ponuđene promjere.
:::
::::
:::: {.content-visible .mf1-answer-online when-format="html"}
::: {.callout-tip collapse="true" data-answer-key="true"}
### Kontrolni rezultat

Dopušteno je $43{,}183\ \text{mm}\le d\le52{,}328\ \text{mm}$, pa odgovara uložak od $50\ \text{mm}$. Za promjere $40$, $50$ i $60\ \text{mm}$ apsolutni tlakovi u grlu redom su $26{,}591$, $101{,}366$ i $128{,}225\ \text{kPa}$, a padovi tlaka $123{,}409$, $48{,}634$ i $21{,}775\ \text{kPa}$. Uložak od 40 mm krši tlačni prag, a onaj od 60 mm nema dovoljan mjerni signal. Granice su zaokružene; odluka se provjerava izvornim nejednakostima.
:::
::::

[Razina: T3]{.mf1-task-level}

### Sifon i putanja izlaznog mlaza {#task-u09-idealni-sifon-promjera-prazni-otvoreni-spremnik-tako .unnumbered .unlisted}

Sifon je prethodno napunjen vodom, a ulaz je uronjen. U kvazistacionarnom trenutku uzmi gustoću vode $\rho=1000\ \text{kg/m}^3$. Idealni sifon promjera $D = 70\ \text{mm}$ prazni otvoreni spremnik tako da je izlaz vodoravan i nalazi se $\Delta z = 2{,}6\ \text{m}$ ispod slobodne površine. Vrh sifona je $z_C = 1{,}7\ \text{m}$ iznad slobodne površine, a izlaz se nalazi $1{,}2\ \text{m}$ iznad tla.

Najprije zanemari gubitke i odredi brzinu i volumenski protok u sifonu, apsolutni tlak u vrhu sifona te vodoravni domet mlaza nakon izlaza ako je $p_{atm} = 101{,}3\ \text{kPa}$.

Zatim primijeni zadano proširenje energijske bilance: gubitak visine modelira se s $h_L=K v^2/(2g)$. Za izvedeni sustav ukupni koeficijent gubitaka od spremnika do izlaza iznosi $K_\Sigma=2{,}0\pm0{,}5$, a do vrha sifona $K_C=1{,}2\pm0{,}3$; oba su definirana uz brzinu u sifonu.

Oznake ± ovdje daju zajamčene intervale, ne standardne nesigurnosti; dopuštene su sve njihove kombinacije. Primijeni bilance $\Delta z=(1+K_\Sigma)v^2/(2g)$ i $p_{C,abs}=p_{atm}-\rho g[z_C+(1+K_C)v^2/(2g)]$.

Odredi nominalni protok prema modelu s gubitcima i konzervativne granice protoka i tlaka u vrhu. Može li se zajamčiti zahtjev $Q\ge15{,}0\ \text{L/s}$ i $p_C\ge30\ \text{kPa}$ apsolutno?

:::: {.content-visible .mf1-hint-online when-format="html"}
::: {.callout-note collapse="true" data-hint-key="true"}
### Naputak
Bernoullijevom jednadžbom između slobodne površine i izlaza odredi idealni $v$, a između slobodne površine i vrha sifona odredi tlak. Domet mlaza izračunaj prema modelu vodoravnog hica s visine $1{,}2\ \text{m}$. Za izvedeni sustav koristi $v=\sqrt{2g\Delta z/(1+K_\Sigma)}$ i $p_C=p_{atm}-\rho g[z_C+(1+K_C)v^2/(2g)]$. Najmanji protok daje najveći $K_\Sigma$; najmanji tlak u vrhu provjeri rubnim kombinacijama zadanih intervala, ne samo nominalnim koeficijentima.
:::
::::
:::: {.content-visible .mf1-answer-online when-format="html"}
::: {.callout-tip collapse="true" data-answer-key="true"}
### Kontrolni rezultat

Idealno: $v\approx7{,}14$ m/s, $Q\approx27{,}5$ L/s, $p_{C,abs}\approx59{,}1$ kPa, $x\approx3{,}53$ m. Uz gubitke nominalno je $Q\approx15{,}9$ L/s i $p_{C,abs}\approx65{,}9$ kPa; intervali su $Q\in[14{,}7;17{,}4]$ L/s i $p_{C,abs}\in[59{,}1;70{,}8]$ kPa. Tlačni zahtjev prolazi, ali protok od 15,0 L/s nije zajamčen. Smanjiti gubitke, povećati promjer ili suziti interval mjerenjem.
:::
::::

[Razina: T4]{.mf1-task-level}

:::::

![Skice vježbi: istjecanje, konfuzor, silazno suženje, izdignuti Pitotov senzor, izbor grla i sifon s mlazom.](../assets/print/u09_vjezbe_skice.svg){#fig-u09-vjezbe fig-align="center" fig-alt="Skice vježbi: istjecanje, konfuzor, silazno suženje, izdignuti Pitotov senzor, izbor grla i sifon s mlazom."}


::: {.mf1-zavrsni-okvir}
<p class="mf1-box-label">Za ponijeti iz poglavlja</p>

**Sažeta provjera prije računa**

- Jesu li dvije točke odabrane fizikalno smisleno?
- Vrijedi li idealni model ili je zadatak već ušao u gubitke i realni Bernoulli?
- Prije Bernoullija treba zatvoriti kontinuitet ako se mijenja presjek.
- Treba provjeriti koriste li se tlak, brzina i visina u istom sustavu jedinica.
- Treba znati koji član mora pasti ako drugi raste.

**Najčešća pogreška**

Najčešća pogreška u []{.mf1-chapter-ref target="u08"} nije algebra nego mehaničko prepisivanje Bernoullija bez provjere pretpostavki. Često se zaboravlja i da porast brzine ne stvara novu energiju, nego je u promatranom idealnom modelu praćen padom tlačne ili geodetske visine.

**Nakon ovoga poglavlja mora biti moguće**

1. provjeriti jesu li pretpostavke idealnog modela zadovoljene.
2. čitati tlak, brzinu i visinu kao tri oblika iste mehaničke energije.
3. spojiti kontinuitet i Bernoulli u jednostavnom problemu promjene presjeka.
4. prepoznati kada zadatak više ne pripada idealnom nego realnom modelu.

**U tehnici to znači**

Venturijeve cijevi, Pitotove sonde i mlaznice rade upravo zato što se ista mehanička energija može očitati kao tlak, brzina ili visina. U praksi taj prijelaz omogućuje mjerenje protoka, procjenu brzine strujanja i projektiranje mlaznih sustava za pranje, hlađenje ili raspršivanje.

**Granica modela**

Idealni Bernoulli prestaje biti dovoljan čim trenje, vrtloženje ili lokalni otpori daju mjerljiv gubitak, odnosno kad se predviđeni apsolutni tlak približi području promjene faze. Tada problem traži modele iz []{.mf1-chapter-ref target="u13"}.

[]{.mf1-chapter-ref target="u08"} zatvara idealnu energetsku sliku strujanja: brzina ne raste niotkuda, nego na račun tlaka ili geodetske visine. Kad se to učvrsti, prijelaz prema []{.mf1-chapter-ref target="u13"} postaje prirodan.
:::
