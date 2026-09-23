![Pregled poglavlja: Relativno mirovanje fluida](../assets/print/u04_fig_uvod_pregled.svg){#fig-uvod-u04 fig-align="center" fig-alt="Pregled poglavlja: Relativno mirovanje fluida"}

## Relativno mirovanje fluida

Relativno mirovanje nastupa kada se fluid u odnosu na stijenke spremnika smiri, premda se spremnik translatorno ubrzava ili rotira. Takvo se stanje opisuje hidrostatikom u efektivnom polju sila.

::: {.mf1-application}
<p class="mf1-box-label">Inženjerski kontekst</p>

Relativno mirovanje javlja se pri kočenju autocisterne, u gorivnom spremniku vozila, u procesnoj kadi na ubrzanoj platformi te pri rotaciji centrifuga i separatora. Slobodna površina i tlak tada ovise o efektivnom polju sila, a ne samo o gravitaciji.
:::

**Procijenjeno vrijeme rada uz udžbenik:** 8 sati.

### Translatorno ubrzanje

Ako se spremnik giba stalnim translatornim ubrzanjem i ako se nakon prolaznih oscilacija fluid smiri u odnosu na stijenke, onda se problem može promatrati kao hidrostatika u neinercijskom sustavu. U tom sustavu na fluid djeluje efektivno polje sila koje je rezultat gravitacije i inercijske sile.

U tom stanju fluid se giba zajedno sa spremnikom kao kruto tijelo: nema relativnog klizanja slojeva ni smičnih naprezanja koja bi nastajala zbog deformacije profila brzine. Upravo zato relativno mirovanje nije nastavak strujanja s gradijentom brzine, nego novi statički problem u promijenjenom polju sila.

Za gibanje spremnika ubrzanjem $a$ udesno, slobodna površina ostaje okomita na $\vec{g}_{eff}$, pa za bočni presjek pravokutnog spremnika vrijedi radna relacija

$$\Delta h = \frac{aL}{g}$$ {#eq-relativno-mirovanje-fizikalni-uvod-i-matematicki-izvod-01}

Razlika razina $\Delta h$ povećava se s ubrzanjem i duljinom spremnika, a smanjuje s gravitacijskim ubrzanjem $g$. Relacija vrijedi dok nema prelijevanja ni ogoljavanja dna, kada je slobodna površina ravna.

Pritom je $\Delta h$ razlika razina slobodne površine na krajevima spremnika.

Za razliku od hidrostatike u mirujućem spremniku, tlak ne raste samo s okomitom dubinom. Smjer efektivnog polja sila određuje geometriju slobodne površine, lokalnu dubinu i raspodjelu tlaka.

<!-- [NOVA PEDAGOŠKA DOPUNA] Postojeći numerički trag -->
::: {.mf1-numerika .kompakt}
<p class="mf1-box-label">Numerički trag — gibanje spremnika</p>

Numerički opis ubrzanoga ili rotirajućeg spremnika uvodi odgovarajuće neinercijske volumenske članove ili rješava gibanje u inercijskom okviru s pokretnom mrežom. Mirna slobodna površina u stalnom ubrzanju, odnosno paraboloid pri vrtnji krutoga tijela, ostaju provjerljivi referentni slučajevi prije proračuna prolaznih valova i zalijevanja stijenki.

U toj se provjeri uspoređuju visina slobodne površine, tlak na stijenci i očuvani volumen, a ne samo izgled prikazane površine. Stacionarni rezultat pri zadanom ubrzanju može biti ispravan i kada nije prikladan za naglo pokretanje ili zaustavljanje spremnika.

Za prolazni problem dodatno se prati vremenska konvergencija nagiba, sile na stijenci i eventualnoga prelijevanja. Potrebna duljina simulacije određuje se fizikalnim vremenom odziva, ne samo time što su reziduali pali ispod zadanog broja.
:::

## Matematički izvod

Promatra se spremnik koji se giba stalnim translatornim ubrzanjem $\vec a$ te sustav koordinata vezan uz spremnik. U tom neinercijskom sustavu mirujući fluid mora zadovoljavati ravnotežu između gradijenta tlaka, gravitacije i inercijskoga člana. Po jedinici volumena vrijedi

$$
-\nabla p + \rho\vec g - \rho\vec a = 0,
$$ {#eq-relativno-mirovanje-matematicki-izvod-01}

odnosno

$$
\nabla p = \rho(\vec g - \vec a) = \rho\vec g_{eff}.
$$ {#eq-relativno-mirovanje-matematicki-izvod-02}

::: {.mf1-fizikalno-znacenje}
<p class="mf1-box-label">Fizikalno značenje</p>
Efektivno polje sila $\vec{g}_{eff}$ vektorski je zbroj gravitacijskog i inercijskog člana. Slobodna je površina u ubrzanom spremniku okomita na $\vec{g}_{eff}$. U slobodnom padu, kada je $\vec{a}=\vec{g}$, vrijedi $\vec{g}_{eff}=0$ te nestaje hidrostatski gradijent tlaka.
:::

Time se uvodi efektivno polje sila $\vec g_{eff}$: fluid se u ubrzanom spremniku ponaša kao da se nalazi u novom gravitacijskom polju koje je vektorski zbroj stvarne gravitacije i suprotno usmjerenog inercijskog ubrzanja. Za translatorno gibanje spremnika s komponentama ubrzanja $a_x$ i $a_z$, uz os $x$ vodoravno i os $z$ prema gore, slijede komponente

$$\frac{\partial p}{\partial x} = -\rho a_x, \qquad \frac{\partial p}{\partial z} = -\rho(g+a_z)$$ {#eq-relativno-mirovanje-fizikalno-znacenje-01}

Klasična hidrostatika iz <span class="mf1-ch-ref"><span class="mf1-ch-code">pog. 3</span><span class="mf1-ch-title">Hidrostatička raspodjela tlaka i manometrija</span></span> samo je poseban slučaj za $a_x = 0$ i $a_z = 0$. Jednako tako, pri slobodnom padu s $a_z = -g$ nestaje hidrostatički porast tlaka po visini, jer cijeli fluidni stupac ubrzava zajedno sa spremnikom. U najčešćem slučaju vodoravnog ubrzanja udesno vrijedi $a_x = a$ i $a_z = 0$, pa se relacija svodi na poznati zapis

$$\frac{\partial p}{\partial x} = -\rho a, \qquad \frac{\partial p}{\partial z} = -\rho g$$ {#eq-relativno-mirovanje-fizikalno-znacenje-02}

Na slobodnoj površini tlak je konstantan, pa diferencijal promjene tlaka po samoj površini mora biti jednak nuli:

$$dp = \frac{\partial p}{\partial x}dx + \frac{\partial p}{\partial z}dz = 0$$ {#eq-relativno-mirovanje-fizikalno-znacenje-03}

Uvrštavanjem parcijalnih derivacija dobiva se

$$-\rho a_x\,dx - \rho (g+a_z)\,dz = 0$$ {#eq-relativno-mirovanje-fizikalno-znacenje-04}

odnosno nakon skraćivanja s $\rho$

$$\frac{dz}{dx} = -\frac{a_x}{g+a_z}$$ {#eq-relativno-mirovanje-fizikalno-znacenje-05}

Za čisti vodoravni slučaj ponovno slijedi

$$\frac{dz}{dx} = -\frac{a}{g}$$ {#eq-relativno-mirovanje-fizikalno-znacenje-06}

što znači da je slobodna površina okomita na vektor $\vec g_{eff}$. Za pravokutni spremnik duljine $L$ integracija nagiba preko cijele duljine daje

$$
\Delta h = \frac{aL}{g}.
$$ {#eq-relativno-mirovanje-fizikalno-znacenje-07}

Fizikalno značenje relacije jest neposredno: što je spremnik dulji i što je ubrzanje veće, to je veća razlika razina između krajeva, dok gravitacija $g$ djeluje kao stabilizirajući član koji površinu vraća prema vodoravnom položaju.

::: {.mf1-izvod}
<p class="mf1-box-label">Matematički izvod — Coriolisova sila u relativnom mirovanju — zašto nestaje</p>

Pri rotirajućem spremniku puni oblik prividnih sila u neinercijskom (rotirajućem) okviru sadrži tri člana: centrifugalnu silu $-\rho\vec{\omega}\times(\vec{\omega}\times\vec{r})$, Eulerovu silu $-\rho\dot{\vec{\omega}}\times\vec{r}$ (koja iščezava pri konstantnoj kutnoj brzini) i **Coriolisovu silu** $-2\rho\vec{\omega}\times\vec{v}_{rel}$, koja djeluje samo kad fluid ima brzinu u rotirajućem okviru.

U stanju relativnog mirovanja $\vec{v}_{rel} = 0$, pa Coriolisov član automatski iščezava

$$
-2\rho\vec{\omega}\times\vec{v}_{rel} = 0.
$$ {#eq-relativno-mirovanje-matematicki-izvod-coriolisova-sila-u-relativnom-01}

Ravnoteža sila po jedinici volumena svodi se zato na

$$
\nabla p = \rho\vec{g}_{eff} = \rho\vec{g} - \rho\vec{\omega}\times(\vec{\omega}\times\vec{r}),
$$ {#eq-relativno-mirovanje-matematicki-izvod-coriolisova-sila-u-relativnom-02}

a centrifugalni član u cilindričnim koordinatama (kutna brzina $\vec{\omega} = \omega\hat{z}$, vektor položaja $\vec{r} = r\hat{r}$) daje radijalnu komponentu efektivnog ubrzanja $a_{cf} = \omega^2 r$. Coriolisova sila ponovno se pojavljuje čim fluid ima relativnu brzinu u rotirajućem okviru, primjerice pri radijalnom toku u turbostroju. Tada je jedan od članova koji oblikuju zakretanje relativnoga toka; odvajanje i učinkovitost ovise i o gradijentu tlaka, geometriji, viskoznosti, turbulenciji i drugim trodimenzijskim učincima.
:::

::: {.mf1-izvod}
<p class="mf1-box-label">Matematički izvod — Očuvanje volumena u rotirajućem spremniku — eksplicitan izvod</p>

Za rotirajući cilindrični spremnik polumjera $R$, ispunjen vodom do početne visine $h_0$, pretpostavlja se da je nakon dovoljno dugoga vremena fluid dosegnuo vrtnju krutoga tijela s konstantnom kutnom brzinom $\omega$. Zanemaruju se prijelazno zavrtavanje, valovi i utjecaj meniska. Dok još nema prelijevanja ni ogoljavanja dna, slobodna površina poprima oblik paraboloida $h(r)=h_C+\omega^2r^2/(2g)$, gdje je $h_C$ visina u središtu. Vrijednosti $h_C$ i $h_R$ (uz stijenku) povezuju se zakonom očuvanja volumena vode prije i poslije početka vrtnje.

Volumen vode u rotirajućem spremniku računa se integralom

$$
V = \int_0^R 2\pi r \cdot h(r)\,dr = \int_0^R 2\pi r\!\left(h_C + \frac{\omega^2 r^2}{2g}\right)dr.
$$ {#eq-relativno-mirovanje-matematicki-izvod-volumno-ocuvanje-paraboloida-e-01}

Integracija po članovima daje

$$
V = 2\pi\!\left[\frac{h_C r^2}{2} + \frac{\omega^2 r^4}{8g}\right]_0^R = \pi R^2 h_C + \frac{\pi \omega^2 R^4}{4g}.
$$ {#eq-relativno-mirovanje-matematicki-izvod-volumno-ocuvanje-paraboloida-e-02}

Volumen vode u mirovanju je $V_0 = \pi R^2 h_0$, a zakon očuvanja $V = V_0$ daje

$$
\pi R^2 h_C + \frac{\pi \omega^2 R^4}{4g} = \pi R^2 h_0,
$$ {#eq-relativno-mirovanje-matematicki-izvod-volumno-ocuvanje-paraboloida-e-03}

odakle slijedi visina u središtu

$$
h_C = h_0 - \frac{\omega^2 R^2}{4g}.
$$ {#eq-relativno-mirovanje-matematicki-izvod-volumno-ocuvanje-paraboloida-e-04}

Iz definicije paraboloida $h_R = h_C + \omega^2 R^2/(2g)$ izravno se dobiva visina uz stijenku

$$
h_R = h_0 + \frac{\omega^2 R^2}{4g}.
$$ {#eq-relativno-mirovanje-matematicki-izvod-volumno-ocuvanje-paraboloida-e-05}

Zbroj i srednja vrijednost daju karakterističnu jednakost $(h_C + h_R)/2 = h_0$ — porast razine uz stijenku jednak je padu razine u središtu, što je geometrijska posljedica simetrije paraboloida i očuvanja mase.

Granični uvjet **ogoljavanja dna** dolazi iz $h_C = 0$:

$$
\left(\omega_{crit}^{ogol}\right)^2 R^2 = 4 g h_0 \quad\Longrightarrow\quad \omega_{crit}^{ogol} = \frac{2\sqrt{g h_0}}{R},
$$ {#eq-relativno-mirovanje-matematicki-izvod-volumno-ocuvanje-paraboloida-e-06}

dok granični uvjet **prelijevanja** preko ruba spremnika visine $H$ slijedi iz $h_R = H$:

$$
\omega_{crit}^{prel} = \frac{2\sqrt{g(H - h_0)}}{R}.
$$ {#eq-relativno-mirovanje-matematicki-izvod-volumno-ocuvanje-paraboloida-e-07}

Prva se javlja pojava s manjom kritičnom kutnom brzinom. Budući da se uspoređuju $h_0$ i $H-h_0$, vrijedi: za $h_0<H/2$ prvo se ogoljava dno, za $h_0>H/2$ prvo nastupa prelijevanje, a za $h_0=H/2$ pragovi se podudaraju. Nakon prvoga praga mijenja se domena fluida ili volumen u spremniku, pa gornje formule za puni paraboloid više ne vrijede bez nove geometrijske bilance.
:::

<!-- [NOVA PEDAGOŠKA DOPUNA] Postojeći numerički trag -->
::: {.mf1-numerika .kompakt}
<p class="mf1-box-label">Numerički trag — slobodna površina kao provjera</p>

Ravnina slobodne površine pri stalnom ubrzanju i paraboloid pri stalnoj vrtnji poznata su rješenja koja se mogu usporediti s poljem iz simulacije. Time se odvojeno provjeravaju gravitacija, ubrzanje, tlak i geometrijsko praćenje površine prije modeliranja prolaznoga valjanja, prskanja ili punjenja spremnika.
:::

## Riješeni primjeri

::: {#ex-u04-otvoreni-spremnik-na-laboratorijskim-kolicima-t2 .mf1-we}
<p class="mf1-box-label">P1. Otvoreni spremnik na laboratorijskim kolicima&nbsp;<span class="mf1-level">T2</span></p>

**Kontekst:** Otvoreni pravokutni spremnik na laboratorijskim kolicima giba se vodoravno stalnim ubrzanjem. U relativnom mirovanju treba odrediti nagib slobodne površine i visine uz stijenke.

**Zadano**

- Duljina spremnika: $L = 1{,}60\ \text{m}$
- Širina spremnika: $B = 0{,}80\ \text{m}$
- Početna mirna visina vode: $h_0 = 0{,}42\ \text{m}$
- Vodoravno ubrzanje udesno: $a = 1{,}35\ \text{m/s}^2$

**Traženo**

1. razliku razina slobodne površine između stražnje i prednje stijenke.
2. visinu vode uz stražnju i prednju stijenku.
3. kut nagiba slobodne površine prema vodoravnici.

![otvoreni spremnik na laboratorijskim kolicima](../assets/print/u04_val2_laboratorijska_kolica.svg){#fig-u04-otvoreni-spremnik-na-laboratorijskim-kolicima fig-alt="otvoreni spremnik na laboratorijskim kolicima"}

**Pretpostavke i model**

Promatra se translatorno ubrzanje bez prelijevanja i bez ogoljavanja dna. Zato je slobodna površina ravna, a srednja visina tekućine ostaje jednaka početnoj vrijednosti $h_0$.

**Rješenje**

Za vodoravno ubrzani spremnik vrijedi osnovna relacija

$$
\Delta h = \frac{aL}{g} = \frac{1{,}35 \cdot 1{,}60}{9{,}81} = 0{,}220\ \text{m} \approx 22{,}0\ \text{cm}.
$$ {#eq-relativno-mirovanje-rijeseni-primjer-otvoreni-spremnik-na-laboratori-01}

Kako nema gubitka volumena, srednja visina ostaje $(h_{stražnja} + h_{prednja})/2 = h_0 = 0{,}42\ \text{m}$, a razlika visina je $h_{stražnja} - h_{prednja} = \Delta h = 0{,}220\ \text{m}$. Rješavanjem tog sustava slijedi

$$
h_{stražnja} = h_0 + \frac{\Delta h}{2} = 0{,}42 + 0{,}110 = 0{,}530\ \text{m},
$$ {#eq-relativno-mirovanje-rijeseni-primjer-otvoreni-spremnik-na-laboratori-02}

$$
h_{prednja} = h_0 - \frac{\Delta h}{2} = 0{,}42 - 0{,}110 = 0{,}310\ \text{m}.
$$ {#eq-relativno-mirovanje-rijeseni-primjer-otvoreni-spremnik-na-laboratori-03}

Kut nagiba slobodne površine dobiva se iz efektivnog polja sila:

$$
{}\tan\theta = \frac{a}{g} = \frac{1{,}35}{9{,}81} = 0{,}138 \quad \Longrightarrow \quad {}\theta = \arctan(0{,}138) \approx 7{,}9^\circ.
$$ {#eq-relativno-mirovanje-rijeseni-primjer-otvoreni-spremnik-na-laboratori-04}

**Provjera i komentar**

Pri zadanom ubrzanju slobodna površina povisi se na stražnjoj strani za oko $11\ \text{cm}$ i jednako toliko padne na prednjoj strani. To je upravo najjednostavniji ulaz u relativno mirovanje prije nego što se uključe granični uvjeti prelijevanja ili sila na stijenci.

1. Ako je ubrzanje nula, mora biti i $\Delta h = 0$.
2. Kod ubrzanja udesno razina mora biti viša na stražnjoj strani spremnika; sam smjer brzine ne određuje nagib.
3. Dobivene dubine moraju ostati pozitivne ako nema ogoljavanja dna, što je ovdje zadovoljeno.
:::

::: {#ex-u04-zatvoreni-servisni-modul-s-kosom-inspekcijskom-stijenkom .mf1-we}
<p class="mf1-box-label">P2. Zatvoreni servisni modul s kosom inspekcijskom stijenkom&nbsp;<span class="mf1-level">T2</span></p>

**Kontekst:** Zatvoreni transportni modul s tehnološkom tekućinom i plinskim pretlakom ubrzava se vodoravno. Treba postaviti inspekcijsku stijenku tako da bude okomita na slobodnu površinu te odrediti silu i hvatište rezultante.

**Zadano**

- Gustoća tehnološke tekućine: $\rho = 960\ \text{kg/m}^3$
- Jednoliki pretlak iznad slobodne površine: $p_{M0} = 16\ \text{kPa}$
- Vodoravno ubrzanje modula: $a = 3{,}4\ \text{m/s}^2$
- Vertikalna visina od ruba `A` do dna `B`: $H = 0{,}55\ \text{m}$
- Širina modula: $b = 1\ \text{m}$ (jedinična)

**Traženo**

1. kut ${}\alpha$ pod kojim stijenku `AB` treba postaviti prema vodoravnici.
2. duljinu stijenke `AB`.
3. rezultantnu silu fluida na stijenku `AB` po jediničnoj širini modula.
4. udaljenost hvatišta rezultante od gornjeg ruba `A`, mjerenu po stijenci.

Zanemari prolazne oscilacije i promjenu gustoće plina iznad tekućine.

![zatvoreni servisni modul s kosom inspekcijskom stijenkom](../assets/print/u04_val3_kosa_stijenka.svg){#fig-u04-zatvoreni-servisni-modul-s-kosom-inspekcijskom-stijenkom fig-alt="zatvoreni servisni modul s kosom inspekcijskom stijenkom"}

**Pretpostavke i model**

Slobodna površina i u zatvorenom modulu mora biti okomita na efektivno polje sila $\vec{g}_{eff}$. Nepropusna vanjska stijenka `AB` odvaja tekućinu od prostora na atmosferskom tlaku; njezin se gornji nastavak spaja s poklopcem i zatvara plinski prostor. Slobodna površina završava u `A`. Budući da je u plinskom prostoru tlak jednolik, na gornjem rubu `A` manometarski tlak jednak je $p_{M0}$, a duž stijenke `AB` zatim linearno raste zbog efektivne težine fluida. Rezultanta neto tlaka djeluje okomito na `AB`, prema van.

**Rješenje**

Najprije odredimo kut nagiba slobodne površine iz osnovne relacije relativnog mirovanja:

$$
{}\tan\theta = \frac{a}{g} = \frac{3{,}4}{9{,}81} = 0{,}347 \quad \Longrightarrow \quad {}\theta = \arctan(0{,}347) \approx 19{,}1^\circ.
$$ {#eq-relativno-mirovanje-rijeseni-primjer-zatvoreni-servisni-modul-s-koso-01}

Ako slobodna površina mora biti okomita na stijenku `AB`, tada stijenka mora zatvarati s vodoravnicom kut

$$
{}\alpha = 90^\circ - {}\theta = 90^\circ - 19{,}1^\circ = 70{,}9^\circ \approx 71^\circ.
$$ {#eq-relativno-mirovanje-rijeseni-primjer-zatvoreni-servisni-modul-s-koso-02}

Duljina stijenke slijedi iz zadane vertikalne projekcije $H$:

$$
s = \frac{H}{\sin\alpha} = \frac{0{,}55}{\sin 70{,}9^\circ} \approx 0{,}582\ \text{m}.
$$ {#eq-relativno-mirovanje-rijeseni-primjer-zatvoreni-servisni-modul-s-koso-03}

Efektivna težina po jedinici mase ima iznos

$$
g_{eff} = \sqrt{g^2 + a^2} = \sqrt{9{,}81^2 + 3{,}4^2} \approx 10{,}38\ \text{m/s}^2.
$$ {#eq-relativno-mirovanje-rijeseni-primjer-zatvoreni-servisni-modul-s-koso-04}

Na stijenci `AB` djeluju dvije komponente sile po jediničnoj širini modula:

1. jednolika komponenta zbog plinskog pretlaka.
2. linearno rastuća komponenta zbog raspodjele tlaka u tekućini uz $g_{eff}$.

Površina stijenke po jediničnoj širini modula iznosi $A_{AB} = s \cdot 1 = 0{,}582\ \text{m}^2$. Jednolika komponenta sile zato glasi

$$
F_0 = p_{M0} s b \approx 9313{,}55\ \text{N}, \qquad b=1\ \text{m}.
$$ {#eq-relativno-mirovanje-rijeseni-primjer-zatvoreni-servisni-modul-s-koso-05}

Hidrostatski porast uz stijenku daje trokutastu komponentu

$$
F_h = \frac{1}{2} \rho g_{eff} s^2 b \approx 1688{,}62\ \text{N}.
$$ {#eq-relativno-mirovanje-rijeseni-primjer-zatvoreni-servisni-modul-s-koso-06}

Ukupna rezultantna sila po jediničnoj širini modula iznosi

$$
F_R = F_0 + F_h \approx 11\,002{,}17\ \text{N}, \qquad \frac{F_R}{b} \approx 11{,}0\ \text{kN/m}.
$$ {#eq-relativno-mirovanje-rijeseni-primjer-zatvoreni-servisni-modul-s-koso-07}

Za položaj hvatišta mjerimo udaljenost $y_R$ od ruba `A` po stijenci. Jednolika komponenta djeluje u polovini duljine $s/2$, a trokutasta u točki $2s/3$ od `A`, pa je

$$
y_R = \frac{F_0 \cdot (s/2) + F_h \cdot (2s/3)}{F_R} \approx 0{,}30594\ \text{m} \approx 0{,}306\ \text{m}
$$ {#eq-relativno-mirovanje-rijeseni-primjer-zatvoreni-servisni-modul-s-koso-08}

ispod ruba `A`, mjereno uzduž stijenke. U računu sila i hvatišta koriste se nezaokružene vrijednosti $s$ i $g_{eff}$.

**Provjera i komentar**

1. Budući da je $a < g$, kut ${}\alpha$ mora ostati veći od $45^\circ$, što je ovdje zadovoljeno.
2. Da nema plinskog pretlaka, hvatište bi bilo dublje prema $2s/3$; ovdje ga jednolika komponenta vraća bliže sredini stijenke.
3. Ukupna sila mora biti veća od same hidrostatske komponente, a razumno je i to da pretlak ovdje nosi veći dio opterećenja.
:::

::: {#ex-u04-rotirajuci-cilindricni-spremnik-bez-prelijevanja-t2 .mf1-we}
<p class="mf1-box-label">P3. Rotirajući cilindrični spremnik bez prelijevanja&nbsp;<span class="mf1-level">T2</span></p>

**Kontekst:** Otvoreni cilindrični spremnik s vodom vrti se oko svoje osi konstantnom kutnom brzinom. Slobodna površina prelazi u paraboloid, a treba odrediti razliku razina i visine uz rub i u osi.

**Zadano**

- Polumjer spremnika: $R = 0{,}35\ \text{m}$
- Početna srednja visina vode: $h_0 = 0{,}28\ \text{m}$
- Kutna brzina vrtnje: $\omega = 6{,}0\ \text{rad/s}$

**Traženo**

1. razliku razina slobodne površine između stijenke i osi spremnika $\Delta h$.
2. visinu slobodne površine uz stijenku $h_{rub}$.
3. visinu slobodne površine na osi spremnika $h_{osa}$.

Zanemari prelijevanje i pretpostavi da volumen vode ostaje isti.

![Rotirajući cilindrični spremnik: paraboloidna slobodna površina (R=0,35 m, ω=6,0 rad/s)](../assets/print/u04_fig_rotirajuci_cilindar.svg){#fig-u04-rotirajuci-cilindar fig-align="center" fig-alt="Rotirajući cilindrični spremnik: paraboloidna slobodna površina (R=0,35 m, ω=6,0 rad/s)"}

**Pretpostavke i model**

U relativnom mirovanju pri rotaciji slobodna površina prelazi u paraboloid, ali se za osnovni proračun najprije može čitati razlika razina između ruba i osi. Kako nema prelijevanja, srednja visina ostaje jednaka početnoj vrijednosti $h_0$.

**Rješenje**

Razlika razina između stijenke i osi iznosi

$$
\Delta h = \frac{\omega^2 R^2}{2g} = \frac{6{,}0^2 \cdot 0{,}35^2}{2 \cdot 9{,}81} = 0{,}225\ \text{m} \approx 22{,}5\ \text{cm}.
$$ {#eq-relativno-mirovanje-rijeseni-primjer-rotirajuci-cilindricni-spremnik-01}

Kako volumen ostaje isti, srednja visina ostaje $h_0 = (h_{rub} + h_{osa})/2$. Zato je visina uz stijenku

$$
h_{rub} = h_0 + \frac{\omega^2 R^2}{4g} \approx 0{,}392385\ \text{m} \approx 0{,}392\ \text{m}.
$$ {#eq-relativno-mirovanje-rijeseni-primjer-rotirajuci-cilindricni-spremnik-02}

Visina na osi spremnika iznosi

$$
h_{osa} = h_0 - \frac{\omega^2 R^2}{4g} \approx 0{,}167615\ \text{m} \approx 0{,}168\ \text{m}.
$$ {#eq-relativno-mirovanje-rijeseni-primjer-rotirajuci-cilindricni-spremnik-03}

**Provjera i komentar**

1. Veća kutna brzina mora povećati razliku razina jer je $\Delta h \propto \omega^2$.
2. Ako nema prelijevanja, visina uz rub i visina u osi moraju ostati simetrične oko srednje visine $h_0$.
3. Visina na osi mora pasti, a visina uz stijenku porasti u odnosu na početnu ravnu razinu.
:::

::: {#ex-u04-rotirajuci-cilindricni-spremnik-s-granicom-prelijevanja-t3 .mf1-ch}
<p class="mf1-box-label">P4. Rotirajući cilindrični spremnik s granicom prelijevanja&nbsp;<span class="mf1-level">T3</span></p>

**Kontekst:** U procesnom postrojenju otvoreni cilindrični spremnik s vodom vrti se oko vertikalne osi konstantnom kutnom brzinom. Treba odrediti oblik paraboloidne slobodne površine, dubinske tlakove na dnu te graničnu brzinu vrtnje prije prelijevanja preko ruba.

**Zadano**

- Unutarnji polumjer otvorenog cilindričnog spremnika: $R = 0{,}40\ \text{m}$
- Unutarnja visina spremnika: $H = 0{,}78\ \text{m}$
- Gustoća vode: $\rho = 1000\ \text{kg/m}^3$
- Mirna razina vode: $h_0 = 0{,}60\ \text{m}$
- Kutna brzina vrtnje oko okomite osi: $\omega = 5{,}20\ \text{rad/s}$

Nakon prolaznog razdoblja voda se postavi u relativno mirovanje kao kruto rotirajuće tijelo.

**Traženo**

1. razliku razina slobodne površine između stijenke i osi spremnika $\Delta h$.
2. dubinu vode na osi spremnika $h_C$ i uz stijenku $h_R$.
3. manometarski tlak na dnu u središnjoj točki `C` i u rubnoj točki `D`.
4. graničnu kutnu brzinu pri kojoj prema geometrijskom modelu počinje prelijevanje, $\omega_{max}$, te pripadnu brzinu vrtnje $n_{max}$ u okr/min.

Zanemari površinsku napetost, valjanje i otpor zraka.

![rotirajući cilindrični spremnik](../assets/print/u04_ch1_rotirajuci_spremnik_paraboloid.svg){#fig-u04-rotirajuci-cilindricni-spremnik fig-alt="rotirajući cilindrični spremnik"}

**Pretpostavke i model**

U stanju relativnog mirovanja pri vrtnji fluid se opet giba kao kruto tijelo, ali sada s konstantnom kutnom brzinom $\omega$. Zato u cilindričnim koordinatama vrijedi da tlak radijalno raste prema stijenci, a po visini i dalje opada zbog gravitacije:

$$
\frac{\partial p}{\partial r} = \rho \omega^2 r, \qquad \frac{\partial p}{\partial z} = -\rho g
$$ {#eq-relativno-mirovanje-cjeloviti-zadatak-rotirajuci-cilindricni-spremni-01}

::: {.mf1-fizikalno-znacenje}
<p class="mf1-box-label">Fizikalno značenje</p>
Prva jednadžba pokazuje da tlak raste prema stijenci s porastom $r$, zbog centrifugalne pseudosile. Druga opisuje hidrostatsku raspodjelu po visini. Zajedno određuju raspodjelu tlaka u dvama smjerovima: tlak raste s radijusom, a pada s visinom. Slobodna površina zato u aksijalnom presjeku poprima paraboličan oblik.
:::

Iz toga slijedi da slobodna površina i druge plohe stalnog tlaka više nisu ravnine nego paraboloidi revolucije. U aksijalnom presjeku zato vrijedi parabola

$$
h(r) = h_C + \frac{\omega^2 r^2}{2g}
$$ {#eq-relativno-mirovanje-fizikalno-znacenje-08}

::: {.mf1-fizikalno-znacenje}
<p class="mf1-box-label">Fizikalno značenje</p>
Parabola $h(r) = h_C + \omega^2 r^2/(2g)$ opisuje oblik slobodne površine: na osi vrtnje površina je najniža ($h_C$), a prema stijenci raste kvadratno. Veća kutna brzina $\omega$ ili veći polumjer $R$ daju strmiji paraboloid. Faktor $2g$ u nazivniku dolazi od integracije centrifugalnog ubrzanja $\omega^2 r$ po radijusu – isti tip kao $v^2/(2g)$ u Bernoullijevoj jednadžbi koja slijedi u <span class="mf1-ch-ref"><span class="mf1-ch-code">pog. 8</span><span class="mf1-ch-title">Energijska jednadžba i Bernoulli</span></span>.
:::

::: {.mf1-interaktivno}
<p class="mf1-box-label">Interaktivni prikaz — Paraboloidna slobodna površina</p>

Interaktivni prikaz omogućuje mijenjanje kutne brzine $\omega$, polumjera spremnika $R$ i početne visine $h_0$ uz neposredno praćenje paraboloidne slobodne površine. Visine u središtu i na rubu spremnika prikazuju se u stvarnom vremenu.

<div class="mf1-interaktivno-akcija">
<a class="mf1-interaktivno-veza" href="https://martibasic.github.io/MF1_udzbenik/jlite/lab/index.html?path=u04_paraboloidna_povrsina.ipynb">Pokreni u pregledniku</a>
<a class="mf1-interaktivno-veza" href="https://colab.research.google.com/github/martibasic/MF1_udzbenik/blob/main/notebooks/u04_paraboloidna_povrsina.ipynb" target="_blank" rel="noopener">Pričuvno: otvori u Colabu</a>
<img class="mf1-interaktivno-qr" src="../assets/qr/u04_paraboloidna_povrsina.svg" alt="QR kod za interaktivni prikaz paraboloidne slobodne površine"/>
</div>

:::

::: {.callout-note}
## Postupak rješenja
Korak: $\partial p/\partial r = \rho\omega^2 r$ i $\partial p/\partial z = -\rho g$ $\;\Rightarrow\;$ $h(r) = h_C + \omega^2 r^2/(2g)$

Na slobodnoj površini vrijedi $dp = 0$, pa:
$$
0 = \frac{\partial p}{\partial r}\,dr + \frac{\partial p}{\partial z}\,dz = \rho\omega^2 r\,dr - \rho g\,dz.
$$ {#eq-relativno-mirovanje-razrada-koraka-01}
Dijeljenje s $\rho g$ i premještanje članova:
$$
\frac{dz}{dr} = \frac{\omega^2 r}{g}.
$$ {#eq-relativno-mirovanje-razrada-koraka-02}
Integracija od osi ($r = 0$, $z = h_C$) do radijusa $r$:
$$
z(r) = h_C + \frac{\omega^2}{g}\int_0^r r'\,dr' = h_C + \frac{\omega^2 r^2}{2g}.
$$ {#eq-relativno-mirovanje-razrada-koraka-03}
:::

gdje je $r$ udaljenost od osi vrtnje. Budući da nema prelijevanja pri zadanom režimu, ukupni volumen vode ostaje isti pa je srednja visina i dalje jednaka početnoj vrijednosti $h_0$.

**Rješenje**

### 1. Razlika razina slobodne površine {.unnumbered .unlisted .mf1-step}

Iz izraza za paraboloidnu slobodnu površinu razlika između stijenke i osi spremnika iznosi

$$
\Delta h = h_R - h_C = \frac{\omega^2 R^2}{2g} = \frac{5{,}20^2 \cdot 0{,}40^2}{2 \cdot 9{,}81} = 0{,}2205\ \text{m} \approx 22{,}1\ \text{cm}.
$$ {#eq-relativno-mirovanje-1-razlika-razina-slobodne-povrsine-01}

### 2. Dubina na osi i uz stijenku {.unnumbered .unlisted .mf1-step}

Kako se volumen nije promijenio, srednja visina ostaje $h_0 = (h_C + h_R)/2$, uz relaciju $h_R - h_C = \Delta h$. Zato je

$$
h_C = h_0 - \frac{\Delta h}{2} = 0{,}60 - \frac{0{,}2205}{2} = 0{,}4897\ \text{m} \approx 0{,}490\ \text{m},
$$ {#eq-relativno-mirovanje-2-dubina-na-osi-i-uz-stijenku-01}

$$
h_R = h_0 + \frac{\Delta h}{2} = 0{,}60 + \frac{0{,}2205}{2} = 0{,}7103\ \text{m} \approx 0{,}710\ \text{m}.
$$ {#eq-relativno-mirovanje-2-dubina-na-osi-i-uz-stijenku-02}

### 3. Tlak na dnu u točkama `C` i `D` {.unnumbered .unlisted .mf1-step}

Na dnu spremnika lokalni manometarski tlak dobiva se iz lokalne dubine ispod slobodne površine. U osi spremnika vrijedi

$$
p_{M,C} = \rho g h_C = 1000 \cdot 9{,}81 \cdot 0{,}4897 = 4804\ \text{Pa} \approx 4{,}80\ \text{kPa}.
$$ {#eq-relativno-mirovanje-3-tlak-na-dnu-u-tockama-c-01}

Uz stijenku je dubina veća, pa je

$$
p_{M,D} = \rho g h_R = 1000 \cdot 9{,}81 \cdot 0{,}7103 = 6968\ \text{Pa} \approx 6{,}97\ \text{kPa}.
$$ {#eq-relativno-mirovanje-3-tlak-na-dnu-u-tockama-c-02}

### 4. Granica prelijevanja {.unnumbered .unlisted .mf1-step}

Do prelijevanja dolazi kada slobodna površina uz stijenku dosegne rub spremnika, odnosno kada je

$$
h_R = H
$$ {#eq-relativno-mirovanje-4-granica-prelijevanja-01}

Kako za rotaciju bez gubitka volumena vrijedi $h_R = h_0 + \omega^2 R^2/(4g)$, granična kutna brzina zadovoljava $H = h_0 + \omega_{max}^2 R^2/(4g)$, pa je

$$
\omega_{max} = \sqrt{\frac{4g(H-h_0)}{R^2}} = \sqrt{\frac{4 \cdot 9{,}81 \cdot (0{,}78-0{,}60)}{0{,}40^2}} = 6{,}64\ \text{rad/s}.
$$ {#eq-relativno-mirovanje-4-granica-prelijevanja-02}

Brzina vrtnje tada iznosi

$$
n_{max} = \frac{60\omega_{max}}{2\pi} = \frac{60 \cdot 6{,}64}{2\pi} = 63{,}4\ \text{okr/min}.
$$ {#eq-relativno-mirovanje-4-granica-prelijevanja-03}

**Provjera i komentar**

Pri radnoj brzini vrtnje slobodna površina podigne se uz stijenku za oko $22{,}1\ \text{cm}$ u odnosu na os spremnika. Time dubina u osi padne na oko $0{,}490\ \text{m}$, a uz stijenku naraste na oko $0{,}710\ \text{m}$. Zato je manometarski tlak na dnu u središtu oko $4{,}80\ \text{kPa}$, a uz stijenku oko $6{,}97\ \text{kPa}$. Granica prelijevanja nastupa tek pri oko $6{,}64\ \text{rad/s}$, odnosno oko $63{,}4\ \text{okr/min}$.

1. Uz stijenku dubina mora biti veća nego na osi, jer se slobodna površina pri vrtnji podiže prema rubu.
2. Ako je $\omega = 0$, paraboloid se mora vratiti na ravnu slobodnu površinu i opet vrijedi $h_C = h_R = h_0$.
3. Budući da je pri radnom režimu $h_R<H$, spremnik još ne prelijeva; razlika $H-h_R$ samo je geometrijski slobodni rub u zadanom stacionarnom modelu.
:::

::: {#ex-u04-nagib-goriva-u-spremniku-autocisterne-pri-kocenju .mf1-we}
<p class="mf1-box-label">P5. Nagib goriva u spremniku autocisterne pri kočenju &nbsp;<span class="mf1-level">T2</span></p>


**Kontekst:** Pri kočenju autocisterne gorivo se podiže uz prednju stijenku. Za nastavnu procjenu promatra se idealizirani otvoreni pravokutni spremnik na vozilu. Doseže li gorivo gornji rub i ostaje li dno uz stražnju stijenku pokriveno?

**Zadano**

- Duljina spremnika: $L = 1{,}20\ \text{m}$ (u smjeru vožnje)
- Početna mirna visina goriva: $h_0 = 0{,}45\ \text{m}$
- Visina spremnika: $H = 0{,}80\ \text{m}$
- Usporenje pri kočenju: $a = 3{,}8\ \text{m/s}^2$
- Gustoća goriva: $\rho = 750\ \text{kg/m}^3$

**Traženo**

1. Razlika razina između prednje i stražnje stijenke.
2. Visina goriva uz svaku stijenku.
3. Hoće li doći do prelijevanja ili ogoljavanja dna?

![Nagib goriva u autocisterni pri kočenju (L=1,2 m, h₀=0,45 m, a=3,8 m/s²)](../assets/print/u04_fig_autocisterna_kocenje.svg){#fig-u04-autocisterna-kocenje fig-align="center" fig-alt="Nagib goriva u autocisterni pri kočenju (L=1,2 m, h₀=0,45 m, a=3,8 m/s²)"}

**Pretpostavke i model**

Kočenje je jednoliko usporavanje (a = konst.). Promatra se ustaljena relativna ravnoteža nestlačivog fluida, uz zanemarene prolazne valove i bez istjecanja. Gornji rub idealiziranog spremnika otvoren je na atmosferu. Srednja visina goriva ostaje $h_0$ dok nema prelijevanja.

**Rješenje**

Razlika razina (pri kočenju razina goriva viša je uz prednju stijenku):

$$
\Delta h = \frac{aL}{g} = \frac{3{,}8 \cdot 1{,}20}{9{,}81} = 0{,}465\ \text{m}
$$ {#eq-relativno-mirovanje-rijeseni-primjer-nagib-goriva-u-spremniku-autoci-01}

Visina uz prednju stijenku (povišena razina):

$$
h_{prednja} = h_0 + \frac{aL}{2g} \approx 0{,}682416\ \text{m} \approx 0{,}682\ \text{m}
$$ {#eq-relativno-mirovanje-rijeseni-primjer-nagib-goriva-u-spremniku-autoci-02}

Visina uz stražnju stijenku (snižena razina):

$$
h_{stražnja} = h_0 - \frac{aL}{2g} \approx 0{,}217584\ \text{m} \approx 0{,}218\ \text{m}
$$ {#eq-relativno-mirovanje-rijeseni-primjer-nagib-goriva-u-spremniku-autoci-03}

**Provjera i komentar**

Razina goriva uz prednju stijenku doseže $h\approx0{,}682\ \text{m}$, što je ispod vrha ($H=0{,}80\ \text{m}$), pa u zadanom stacionarnom modelu nema prelijevanja. Uz stražnju stijenku dubina goriva iznosi približno $0{,}218\ \text{m}$ te dno ondje nije ogoljeno. Iz uvjeta $h_{pred}=H$ slijedi početak prelijevanja pri $a\approx5{,}72\ \text{m/s}^2$, a iz $h_{str}=0$ formalni prag ogoljavanja bez gubitka volumena bio bi $a\approx7{,}36\ \text{m/s}^2$. Prvo nastupa prelijevanje; nakon njega za ogoljavanje treba novi račun s promijenjenim volumenom. To su geometrijski pragovi relativnog mirovanja, ne operativna ograničenja autocisterne pri prolaznom kočenju.

:::

::: {#ex-u04-laboratorijska-centrifuga-za-odvajanje-plazme-od-eritrocita .mf1-we}
<p class="mf1-box-label">P6. Laboratorijska centrifuga za odvajanje plazme od eritrocita &nbsp;<span class="mf1-level">T2</span></p>

**Kontekst:** U laboratorijskoj centrifugi cijev s uzorkom postavlja se približno radijalno, pa relativno mirovanje daje tlačni porast prema većem polumjeru. Uzorak se u ovome računu namjerno tretira kao homogen fluid zadane gustoće; razdvajanje njegovih sastojaka nije dio modela.

**Zadano**

- Brzina vrtnje rotora: $n = 4000$ okr/min
- Polumjer dna cijevi od osi rotacije: $r_d = 95\ \text{mm}$
- Polumjer vrha cijevi od osi rotacije: $r_v = 25\ \text{mm}$
- Gustoća uzorka pune krvi: $\rho = 1060\ \text{kg/m}^3$

**Traženo**

1. Kutna brzina $\omega$ u rad/s;
2. Centrifugalno ubrzanje na dnu cijevi izraženo u jedinicama $g$;
3. Razlika tlakova između dna i vrha cijevi unutar uzorka.

**Pretpostavke i model**

U rotirajućem okviru fluid se nalazi u stanju relativnog mirovanja. Efektivno ubrzanje u radijalnom smjeru iznosi $a_{cf}(r) = \omega^2 r$, pa se hidrostatički zakon primjenjuje s tim radijalnim ubrzanjem umjesto gravitacije. Gravitacijski doprinos zanemaruje se jer je centrifugalno ubrzanje za nekoliko redova veličine veće. Uzorak se promatra kao homogen u trenutku početka centrifugiranja (još nije došlo do potpunog razdvajanja).

**Rješenje**

Kutna brzina iznosi

$$
\omega = \frac{2\pi n}{60} = \frac{2\pi \cdot 4000}{60} \approx 418{,}9\ \text{rad/s}.
$$ {#eq-relativno-mirovanje-rijeseni-primjer-laboratorijska-centrifuga-za-od-01}

Centrifugalno ubrzanje na dnu cijevi:

$$
a_{cf} = \omega^2 r_d = 418{,}9^2 \cdot 0{,}095 \approx 1{,}666 \cdot 10^4\ \text{m/s}^2.
$$ {#eq-relativno-mirovanje-rijeseni-primjer-laboratorijska-centrifuga-za-od-02}

Izraženo u jedinicama gravitacijskog ubrzanja:

$$
\frac{a_{cf}}{g} = \frac{1{,}666 \cdot 10^4}{9{,}81} \approx 1{,}699 \cdot 10^3,
$$ {#eq-relativno-mirovanje-rijeseni-primjer-laboratorijska-centrifuga-za-od-03}

dakle približno $1{,}70 \cdot 10^3\ g$ (oko 1700 puta veće od Zemljina gravitacijskog ubrzanja).

Razlika tlakova između dna i vrha cijevi u rotirajućem fluidu jednaka je integralu radijalnog tlačnog gradijenta:

$$
\Delta p = \int_{r_v}^{r_d} \rho\omega^2 r\,\mathrm{d}r = \frac{1}{2}\rho\omega^2 (r_d^2 - r_v^2).
$$ {#eq-relativno-mirovanje-rijeseni-primjer-laboratorijska-centrifuga-za-od-04}

Uvrštavanjem:

$$
\Delta p = \frac{1}{2} \cdot 1060 \cdot 418{,}9^2 \cdot (0{,}095^2 - 0{,}025^2).
$$ {#eq-relativno-mirovanje-rijeseni-primjer-laboratorijska-centrifuga-za-od-05}

Računaju se redom $0{,}095^2 - 0{,}025^2 = 9{,}025 \cdot 10^{-3} - 6{,}25 \cdot 10^{-4} = 8{,}40 \cdot 10^{-3}\ \text{m}^2$ i $418{,}9^2 \approx 1{,}754 \cdot 10^5\ \text{rad}^2/\text{s}^2$:

$$
\Delta p = 0{,}5 \cdot 1060 \cdot 1{,}754 \cdot 10^5 \cdot 8{,}40 \cdot 10^{-3} \approx 7{,}81 \cdot 10^5\ \text{Pa}.
$$ {#eq-relativno-mirovanje-rijeseni-primjer-laboratorijska-centrifuga-za-od-06}

Razlika tlakova zato iznosi otprilike

$$
\Delta p \approx 781\ \text{kPa} \approx 7{,}81\ \text{bar}.
$$ {#eq-relativno-mirovanje-rijeseni-primjer-laboratorijska-centrifuga-za-od-07}

**Provjera i komentar**

Izračunano ubrzanje na dnu iznosi oko $1700\,g$, a razlika tlakova u homogenom stupcu oko $7{,}8\ \text{bar}$. Gravitacijski doprinos preko iste radijalne duljine bio bi oko $0{,}73\ \text{kPa}$, pa je njegovo zanemarivanje konzistentno s redom veličine. Ovaj račun ne predviđa vrijeme separacije ni dopušteno opterećenje cijevi i rotora; za njih su potrebni model čestica, stvarna geometrija te upute i dopuštenja proizvođača.
:::

::: {.mf1-samoprovjera}
<p class="mf1-box-label">Provjeri sebe</p>

1. Zašto fluid može mirovati u odnosu na spremnik koji se ubrzava?
2. Zašto slobodna površina ostaje okomita na efektivno polje sila?
3. Zašto tlak u rotirajućem fluidu raste s radijusom?
4. Zašto rezultat relativnoga mirovanja nije dovoljan za procjenu prolaznog zalijevanja spremnika?

::: {.callout-note collapse="true"}
### Odgovori

U neinercijskom opisu ravnotežu daje zbroj gravitacije i inercijske volumenske sile pa fluid može mirovati u odnosu na spremnik. Slobodna se površina postavlja tako da je tangencijalna komponenta efektivnog polja po njoj nula. Veći radijus nosi veće centrifugalno ubrzanje pa zato treba veći gradijent tlaka. Prolazno zalijevanje ovisi o vremenskom odzivu, valovima i prigušenju, a ne samo o konačnom statičkom položaju površine.
:::
:::

::: {.mf1-zavrsni-okvir}
<p class="mf1-box-label">Za ponijeti iz poglavlja</p>

- Relativno mirovanje prevodi ubrzani problem u hidrostatiku s efektivnim poljem sila.
- Slobodna površina i tlak određuju se iz smjera i iznosa $\vec g_{eff}$.
- Pri translatornom ubrzanju razlika razina slobodne površine raste s $a/g$ i duljinom spremnika.
- Pri rotaciji tlak raste s radijusom jer centrifugalni doprinos raste s $r$.
- Ovaj statički model ne opisuje prolazne valove, prskanje ni dinamičko zalijevanje.
:::

## Zadaci za vježbu

::::: {.mf1-vjezbe-list}

Uzmi $g = 9{,}81\ \text{m/s}^2$ i, gdje nije drukčije zadano, gustoću vode $\rho = 1000\ \text{kg/m}^3$. U Z1–Z4 i Z6 promatraju se ustaljena stanja relativnog mirovanja, bez protoka kroz spremnik; Z5 provjerava opravdanost te pretpostavke. Gustoće i geometrija smatraju se stalnima, a površinska napetost zanemaruje se. Očitanja u Z4 i Z5 sintetički su nastavni podatci.

### Z1. Slobodna površina pri ubrzanju {#task-u04-otvoreni-pravokutni-spremnik-duljine-i-pocetne-dubine .unnumbered .unlisted}

Otvoreni pravokutni spremnik duljine $L = 1{,}80\ \text{m}$ i početne dubine vode $h_0 = 0{,}34\ \text{m}$ giba se vodoravno stalnim ubrzanjem $a = 1{,}20\ \text{m/s}^2$. Odredi razliku razina između krajeva spremnika, lokalne dubine uz stražnju i prednju stijenku te provjeri dolazi li do prelijevanja ako je visina boka $H = 0{,}46\ \text{m}$.

:::: {.content-visible .mf1-hint-online when-format="html"}
::: {.callout-note collapse="true" data-hint-key="true"}
### Naputak
$\Delta h = aL/g$; zatim $h_{str} = h_0 + \Delta h/2$ i $h_{pred} = h_0 - \Delta h/2$; usporedi $h_{str}$ s $H$.
:::
::::
:::: {.content-visible .mf1-answer-online when-format="html"}
::: {.callout-tip collapse="true" data-answer-key="true"}
### Kontrolni rezultat

$\Delta h \approx 0{,}22\ \text{m}$; $h_{str} \approx 0{,}45\ \text{m}$, $h_{pred} \approx 0{,}23\ \text{m}$; nema prelijevanja jer je $h_{str} < H$.
:::
::::

[Razina: T1]{.mf1-task-level}

### Z2. Ubrzanje na granici prelijevanja {#task-u04-otvoreni-spremnik-duljine-napunjen-je-do-visine .unnumbered .unlisted}

Otvoreni pravokutni spremnik duljine $L = 1{,}40\ \text{m}$ napunjen je do visine $h_0 = 0{,}30\ \text{m}$, a visina boka je $H = 0{,}42\ \text{m}$. Odredi najveće vodoravno ubrzanje prije početka prelijevanja.

:::: {.content-visible .mf1-hint-online when-format="html"}
::: {.callout-note collapse="true" data-hint-key="true"}
### Naputak
U graničnom stanju vrijedi $h_{str} = H$ i $\Delta h = 2(H-h_0)$; nakon toga $a = g\Delta h/L$.
:::
::::
:::: {.content-visible .mf1-answer-online when-format="html"}
::: {.callout-tip collapse="true" data-answer-key="true"}
### Kontrolni rezultat

$a_{max} \approx 1{,}68\ \text{m/s}^2$.
:::
::::

[Razina: T1]{.mf1-task-level}

### Z3. Tlak pri vertikalnom ubrzanju {#task-u04-zatvoreni-vertikalni-cilindar-potpuno-ispunjen-uljem-gustoce .unnumbered .unlisted}

Zatvoreni vertikalni cilindar potpuno ispunjen uljem gustoće $\rho = 870\ \text{kg/m}^3$ ima visinu stupca fluida $h = 0{,}75\ \text{m}$. Sustav ubrzava prema gore s $a_z = 2{,}3\ \text{m/s}^2$. Odredi razliku tlakova između dna i vrha cilindra te usporedi rezultat s mirovnim stanjem. Zatim razmotri zasebno stanje u kojem se cilindar još giba prema gore, ali usporava uz ubrzanje iznosa $2{,}3\ \text{m/s}^2$ prema dolje. Kolika je tada razlika tlakova? Objasni određuje li je smjer brzine ili smjer ubrzanja.

:::: {.content-visible .mf1-hint-online when-format="html"}
::: {.callout-note collapse="true" data-hint-key="true"}
### Naputak
Koristi efektivnu težinu fluida: $\Delta p = \rho (g+a_z)h$; za usporedbu u mirovanju uzmi $\Delta p_0 = \rho gh$. Os $z$ usmjeri prema gore; pri kočenju je $a_z<0$ iako je brzina još pozitivna.
:::
::::
:::: {.content-visible .mf1-answer-online when-format="html"}
::: {.callout-tip collapse="true" data-answer-key="true"}
### Kontrolni rezultat

$\Delta p \approx 7{,}90\ \text{kPa}$; u mirovanju $\Delta p_0 \approx 6{,}40\ \text{kPa}$ — oko 23 % više. Pri gibanju prema gore uz kočenje $a_z=-2{,}3\ \text{m/s}^2$ dobiva se $\Delta p \approx 4{,}90\ \text{kPa}$. Gradijent određuje ubrzanje, a ne smjer brzine.
:::
::::

[Razina: T2]{.mf1-task-level}

<span id="task-u04-ubrzani-otvoreni-spremnik-sirine-stijenke-i-duljine"></span>

### Z4. Brzina vrtnje iz razlike tlakova {#task-vrtnja-iz-radijalne-razlike-tlakova .unnumbered .unlisted}

Zatvorena cilindrična posuda potpuno je ispunjena vodom gustoće $\rho = 1000\ \text{kg/m}^3$ i vrti se stalnom brzinom oko okomite osi. Voda je dosegnula vrtnju krutoga tijela. Dva senzora u točkama `A` i `B` nalaze se na istoj visini, na polumjerima $r_A = 80\ \text{mm}$ i $r_B = 240\ \text{mm}$. Mjere manometarske tlakove $p_{M,A} = 12{,}40\ \text{kPa}$ i $p_{M,B} = 14{,}00\ \text{kPa}$ prema istoj referenci; očitanja se odnose izravno na označene točke.

Odredi iznos kutne brzine i broj okretaja u minuti. Bi li se izračun promijenio kada bi oba očitanja zbog zajedničkog pomaka reference porasla za $3{,}0\ \text{kPa}$? Može li se iz tih dvaju tlakova odrediti smjer vrtnje?

:::: {.content-visible .mf1-hint-online when-format="html"}
::: {.callout-note collapse="true" data-hint-key="true"}
### Naputak
Na istoj visini poništava se gravitacijski doprinos. Integriraj radijalni gradijent tlaka između $r_A$ i $r_B$, vodeći računa o kvadratu polumjera i pretvorbi milimetara u metre.
:::
::::
:::: {.content-visible .mf1-answer-online when-format="html"}
::: {.callout-tip collapse="true" data-answer-key="true"}
### Kontrolni rezultat

$p_B-p_A = 1{,}60\ \text{kPa}$; $|\omega| \approx 7{,}91\ \text{rad/s}$; $n \approx 75{,}5\ \text{okr/min}$. Zajednički pomak reference ne mijenja razliku tlakova ni rezultat. Smjer vrtnje nije odrediv jer tlak ovisi o $\omega^2$.
:::
::::

[Razina: T2]{.mf1-task-level}

<span id="task-u04-cilindricna-posuda-radijusa-s-pocetnom-dubinom-vode"></span>

### Z5. Je li se fluid smirio nakon ubrzanja? {#task-provjera-smirivanja-ubrzanog-fluida .unnumbered .unlisted}

Otvoreni pravokutni spremnik na vozilu ima duljinu $L = 1{,}50\ \text{m}$, početnu dubinu vode $h_0 = 0{,}300\ \text{m}$ i visinu boka $H = 0{,}550\ \text{m}$. Vozilo nakon pokretanja ubrzava stalno udesno s $a = 2{,}00\ \text{m/s}^2$. Za stanje bez gubitka vode izračunaj dubine uz stražnju i prednju stijenku koje predviđa relativno mirovanje. Zatim usporedi taj model sa sintetičkim očitanjima u dva vremenska niza:

```{=typst}
#block(breakable: false)[
```

| Niz | Vrijeme $t$ (s) | $h_{str}$ (m) | $h_{pred}$ (m) |
| --- | ---: | ---: | ---: |
| I | 0,5 | 0,520 | 0,080 |
| I | 1,0 | 0,380 | 0,220 |
| I | 1,5 | 0,500 | 0,100 |
| II | 8,0 | 0,454 | 0,146 |
| II | 8,5 | 0,452 | 0,148 |
| II | 9,0 | 0,453 | 0,147 |

```{=typst}
]
```

Za ovu nastavnu provjeru niz se smatra sukladnim približnom relativnom mirovanju samo ako **svako očitanje** odstupa od pripadne računske dubine najviše $\varepsilon_h = 5\ \text{mm}$ i ako raspon očitanja uz **svaku stijenku** (najveće minus najmanje) ne premašuje $s_h = 4\ \text{mm}$. To su zadani kriteriji ove vježbe, ne univerzalni pragovi smirivanja.

Za svaki niz odredi najveće odstupanje od modela i veći od dvaju raspona očitanja te donesi odluku. Jamči li stacionarni račun da pri naglom pokretanju nije bilo prelijevanja? Je li prolazak ove provjere dokaz da cijeli fluid miruje u odnosu na spremnik?

:::: {.content-visible .mf1-hint-online when-format="html"}
::: {.callout-note collapse="true" data-hint-key="true"}
### Naputak
Najprije upotrijebi nagib slobodne površine i očuvanje volumena. Zatim odvojeno provjeri blizinu predviđenim razinama i promjenjivost kroz vrijeme; jedna podudarna točka ili prosjek nisu dovoljni.
:::
::::
:::: {.content-visible .mf1-answer-online when-format="html"}
::: {.callout-tip collapse="true" data-answer-key="true"}
### Kontrolni rezultat

Referentne dubine: $h_{str}\approx0{,}45291$ m, $h_{pred}\approx0{,}14709$ m. Niz I: najveće odstupanje 72,91 mm, raspon 140 mm; ne prolazi. Niz II: odstupanje 1,095 mm, raspon 2,0 mm; prolazi oba kriterija. Referentni profil je ispod boka. Očitanja ipak ne dokazuju mirovanje cijelog fluida ni izostanak prolaznog prelijevanja; treba pratiti slobodnu površinu i relativno gibanje kroz vrijeme.
:::
::::

[Razina: T3]{.mf1-task-level}

### Z6. Rotirajući spremnik i prelijevanje {#task-u04-otvoreni-cilindricni-spremnik-polumjera-i-visine-ispunjen .unnumbered .unlisted}

Otvoreni cilindrični spremnik polumjera $R = 0{,}32\ \text{m}$ i visine $H = 0{,}62\ \text{m}$ ispunjen je vodom do početne srednje visine $h_0 = 0{,}46\ \text{m}$. Odredi najveću kutnu brzinu pri kojoj još nema prelijevanja.

Zatim za radni režim $\omega = 0{,}80\,\omega_{max}$ odredi dubinu vode u osi i uz stijenku te manometarske tlakove na dnu u tim dvjema točkama. Za ovu geometrijsku provjeru središnji je usis zatvoren, pa nema protoka.

Pretvarač frekvencije može stvarnu brzinu vrtnje povisiti do $5\ \%$ iznad zadane, a zahtijevana dubina iznad usisa u osi u ustaljenom stanju iznosi najmanje $0{,}350\ \text{m}$. Tih 5 % zadana je gornja granica odstupanja brzine, ne standardna nesigurnost.

Provjeri zadani režim pri najnepovoljnijem dopuštenom odstupanju, odredi najveći dopušteni zadani omjer $\alpha=\omega_{zad}/\omega_{max}$ i preporuči radnu postavku za taj model. Zaključak ne proširuj na usis tijekom protoka ili prijelaznog zavrtavanja.

:::: {.content-visible .mf1-hint-online when-format="html"}
::: {.callout-note collapse="true" data-hint-key="true"}
### Naputak
U graničnom stanju vrijedi $h_{rub} = H = h_0 + \omega_{max}^2 R^2/(4g)$; za radni režim najprije nađi $\Delta h = \omega^2 R^2/(2g)$, zatim $h_{osa}$ i $h_{rub}$, a tlakove iz $p_M = \rho gh$. U provjeri tolerancije koristi $\omega=1{,}05\alpha\omega_{max}$ i iz uvjeta $h_{osa}\ge0{,}350\ \text{m}$ riješi gornju granicu za $\alpha$.
:::
::::
:::: {.content-visible .mf1-answer-online when-format="html"}
::: {.callout-tip collapse="true" data-answer-key="true"}
### Kontrolni rezultat

$\omega_{max}\approx7{,}83$ rad/s. Za $\alpha=0{,}80$: dubine (os, rub) ≈ (0,3576; 0,5624) m, tlakovi ≈ (3,51; 5,52) kPa. Uz +5 % brzine: omjer 0,84, dubine ≈ (0,3471; 0,5729) m; nema prelijevanja, ali dubina u osi nije dovoljna. $\alpha_{max}\approx0{,}790$. Preporuka $\alpha=0{,}78$: pri najvećem odstupanju dubine ≈ (0,35268; 0,56732) m, rezerva 2,68 mm. Vrijedi za ustaljeni model sa zatvorenim usisom.
:::
::::

[Razina: T4]{.mf1-task-level}

:::::

![Skice uz Z1–Z6: nagib pri ubrzanju, granica prelijevanja, vertikalno ubrzavanje i kočenje, tlakovi u rotirajućoj vodi, provjera smirivanja i rotacijski spremnik s ograničenjem dubine.](../assets/print/u04_vjezbe_skice.svg){#fig-u04-vjezbe fig-align="center" fig-alt="Skice uz Z1–Z6: nagib pri ubrzanju, granica prelijevanja, vertikalno ubrzavanje i kočenje, tlakovi u rotirajućoj vodi, provjera smirivanja i rotacijski spremnik s ograničenjem dubine."}

## Sažetak

Fluid se nalazi u relativnom mirovanju kada se u odnosu na ubrzani ili rotirajući spremnik ne giba. Raspodjela tlaka tada se određuje iz efektivnog polja sila $\vec g_{eff}=\vec g-\vec a$. U translatorno ubrzanom spremniku slobodna je površina ravnina okomita na efektivno polje sila, a pri vodoravnom ubrzanju razlika razina iznosi $\Delta h=aL/g$.

U spremniku koji rotira stalnom kutnom brzinom tlak raste s radijalnom udaljenošću, a slobodna površina poprima paraboloidni oblik $h(r)=h_C+\omega^2r^2/(2g)$. Očuvanje volumena određuje visine u središtu i uz stijenku, dok se granice primjene osnovnog modela određuju uvjetima prelijevanja i ogoljavanja dna.

Model pretpostavlja da su prolazne oscilacije, valjanje, prskanje i relativno strujanje fluida zanemarivi. Pri promjenjivom ubrzanju ili značajnom relativnom gibanju potrebna je nestacionarna analiza.

<!-- [RESTAURACIJA] Tekst doslovno preuzet iz c417e9f: source/u04_relativno_mirovanje_fluida.md -->
::: {.mf1-numerika .kompakt}
<p class="mf1-box-label">Numerički most</p>

**Veza s numeričkim proračunom.** Promjena referentnog okvira iz ovog poglavlja temelj je numeričkih pristupa rotirajućim domenama u pumpama, ventilatorima, vodnim i plinskim turbinama te centrifugama. Umjesto računski zahtjevne rotacije mreže, program za CFD dodaje **prividne sile** — centrifugalnu i Coriolisovu — točno onako kako se u zadacima dodavalo $a_{cf} = \omega^2 r$.

**Postupak numeričkog proračuna.** **MRF (Moving Reference Frame)** definira zonu u mreži koja se "vrti" matematički — rješavanjem Navier–Stokesovih jednadžbi u rotirajućem sustavu s dodatnim Coriolisovim i centrifugalnim članom. Za pune nestacionarne simulacije postoji i **klizajuća mreža (engl. sliding mesh)** u kojoj se dijelovi mreže vezani uz rotor i stator gibaju relativno jedan prema drugome.

**Tipičan scenarij.** Stacionarni MRF model može dati početnu procjenu srednjih veličina rotirajućega stroja. Kada su važni prolaz rotora kraj statora, pulsacije ili akustika, potreban je odgovarajući nestacionarni model. Računski trošak i potrebna razlučivost ovise o geometriji, mreži, vremenskom koraku i traženoj izlaznoj veličini.

> *Nije gradivo MF1. Paraboloidna slobodna površina iz ovoga poglavlja u CFD-u dobiva se numeričkim proračunom.*
:::

<!-- [NOVA PEDAGOŠKA DOPUNA] -->
::: {.mf1-numerika .kompakt}
<p class="mf1-box-label">Numerička poveznica — od gibanja spremnika do provjere</p>

**Što je zadano, a što se traži.** Za relativno miran fluid poznati su geometrija i početni volumen tekućine, gustoća, gravitacija i stalno ubrzanje spremnika ili kutna brzina. Traže se položaj slobodne površine, raspodjela tlaka i opterećenje stijenki. U okviru vezanom uz spremnik zadano se gibanje pojavljuje kao efektivno polje $\vec g_{eff}=\vec g-\vec a$; u inercijskom okviru isti se problem može opisati gibajućim stijenkama. Oba zapisa predstavljaju istu fiziku, ali model relativnog mirovanja vrijedi tek nakon što su prolazni valovi zanemarivi.

**Slobodna površina i granice.** Slobodna površina je granica tekućine i plina na kojoj je za otvoreni spremnik tlak jednak atmosferskom, odnosno zadanom referentnom tlaku. U računalnom modelu može se voditi kao poznata mirna granica u referentnom slučaju ili pratiti pokazateljem faze kada se njezin položaj mijenja. Tekućina ne prolazi kroz stijenke spremnika; u inercijskom zapisu brzina fluida na stijenci prati zadano gibanje stijenke, a u okviru spremnika stijenka je mirna. Te granice i početni volumen određuju gdje se može nalaziti površina, pa nagib nije slobodno odabrana geometrija.

**Diskretni račun i kontrola.** Domena se dijeli u ćelije u kojima se predstavljaju tlak i faza, a susjedne vrijednosti povezuju se diskretnom bilancom tlačnih, gravitacijskih i inercijskih doprinosa. Za stalno translatorno ubrzanje provjeravaju se ravnina i nagib slobodne površine, a za vrtnju paraboloid; dodatno se uspoređuju očuvani volumen i tlak na stijenkama s analitičkim referentnim slučajem. Pad reziduala pokazuje samo da je numerički postupak dosegnuo svoj kriterij, dok fizikalnu ispravnost pokazuju ta podudarnost, zanemariva relativna brzina i stabilnost rezultata pri profinjenju mreže. Tek nakon toga mogu se tumačiti valjanje, prskanje ili prelijevanje.

Detalji praćenja međupovršine, rubnih uvjeta, vremenske diskretizacije i verifikacije obrađuju se u <span class="mf1-ch-ref"><span class="mf1-ch-code">pog. 12</span><span class="mf1-ch-title">Diferencijalni opis realnog toka</span></span> i <span class="mf1-ch-ref"><span class="mf1-ch-code">dod. D</span><span class="mf1-ch-title">Numerička mehanika fluida</span></span>.
:::
