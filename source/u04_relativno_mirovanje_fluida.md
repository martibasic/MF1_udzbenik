![Pregled poglavlja U04: Relativno mirovanje fluida](../assets/print/u04_fig_uvod_pregled.svg){#fig-uvod-u04 fig-align="center"}

## Relativno mirovanje kao hidrostatika u novom polju sila

Relativno mirovanje počinje ondje gdje se tekućina prema stijenkama spremnika smiri, iako se cijeli sustav i dalje ubrzava.

Središnja ideja poglavlja nije samo da se slobodna površina naginje, nego da obična hidrostatika prelazi u hidrostatiku u novom, efektivnom polju sila.

::: {.mf1-application}
<p class="mf1-box-label">Inženjerski kontekst</p>

Relativno mirovanje vidi se svaki put kad se tekućina "smiri" u spremniku koji ipak ubrzava: pri kočenju autocisterne, pri promjeni kursa broda, u gorivnom spremniku vozila i u procesnoj kadi na ubrzanoj platformi. Isti model vrijedi i za rotaciju, pa iz ovog poglavlja izravno vode centrifuge, separatori i svi sklopovi u kojima slobodna površina i tlak ovise o efektivnom polju sila, a ne samo o gravitaciji.
:::

## Fizikalni uvod i matematički izvod

Ako se spremnik giba stalnim translatornim ubrzanjem i ako se nakon prolaznih oscilacija fluid smiri u odnosu na stijenke, onda se problem može čitati kao hidrostatika u neinercijskom sustavu. U tom sustavu na fluid djeluje efektivno polje sila koje je rezultat gravitacije i inercijske sile.

U tom stanju fluid se prema spremniku giba kao kruto tijelo: nema relativnog klizanja slojeva ni smičnih naprezanja koja bi nastajala zbog deformacije profila brzine. Upravo zato relativno mirovanje nije nastavak strujanja s gradijentom brzine, nego novi statički problem u promijenjenom polju sila.

Za gibanje spremnika ubrzanjem $a$ udesno, slobodna površina ostaje okomita na $\vec{g}_{eff}$, pa za bočni presjek pravokutnog spremnika vrijedi radna relacija

$$\Delta h = \frac{aL}{g}$$

::: {.callout-note}
## 📐 Fizikalno značenje
Razlika razina $\Delta h$ je izravna mjera koliko ubrzanje "naginje" slobodnu površinu. Veće ubrzanje ili dulji spremnik daje veći nagib jer inercijska pseudo-sila ima više prostora za djelovanje. Gravitacija $g$ u nazivniku je stabilizirajući član: što je veća sila teže, to manji kut postignuća pri istom ubrzanju. Formula vrijedi samo dok se površina ne prelije ili dok ne ogoli dno: ispod tih graničnih stanja vrijedi pretpostavka o ravnoj slobodnoj površini.
:::

gdje je $\Delta h$ razlika razina slobodne površine na krajevima spremnika.

Najvažnija promjena u odnosu na <span class="mf1-ch-ref"><span class="mf1-ch-code">U03</span><span class="mf1-ch-title">Hidrostatička raspodjela tlaka i manometrija</span></span> jest to da tlak više ne raste samo po dubini mjerene okomito prema dolje. Najprije treba odrediti smjer efektivnog polja sila, a tek zatim čitati geometriju slobodne površine i lokalnu dubinu.

Matematika zato ne prati "nagnutu vodu" kao poseban slučaj, nego uvodi novi vektor efektivne gravitacije. Kad se taj vektor jednom odredi, geometrija slobodne površine i raspodjela tlaka opet postaju čitljive kao u hidrostatici.

## Matematički izvod

Promatra se spremnik koji se giba stalnim translatornim ubrzanjem $\vec a$ te sustav koordinata vezan uz spremnik. U tom neinercijskom sustavu mirujući fluid mora zadovoljavati ravnotežu između gradijenta tlaka, gravitacije i inercijskoga člana. Po jedinici volumena vrijedi

$$
-\nabla p + \rho\vec g - \rho\vec a = 0,
$$

odnosno

$$
\nabla p = \rho(\vec g - \vec a) = \rho\vec g_{eff}.
$$

::: {.callout-note}
## 📐 Fizikalno značenje
Efektivno polje sila $\vec{g}_{eff}$ je vektorski zbroj gravitacije i inercijskog člana: fluid se u akceleriranom sustavu "ne zna" razlikovati je li u gravitacijskom polju ili u ubrzanom okviru. Upravo to je razlog zašto slobodna površina u ubrzanom spremniku ostaje okomita na $\vec{g}_{eff}$ – ista fizika kao i u običnoj hidrostatici, samo s novim "gravitacijskim" vektorom. U slobodnom padu ($\vec{a} = \vec{g}$) vrijedi $\vec{g}_{eff} = 0$ i hidrostatski tlak nestaje: astronauti u orbiti ne osjećaju težinu kolone tekucine.
:::

Time se uvodi efektivno polje sila $\vec g_{eff}$: fluid se u akceleriranom spremniku ponaša kao da se nalazi u novom gravitacijskom polju koje je vektorski zbroj stvarne gravitacije i suprotno usmjerene inercijske akceleracije. Za translatorno gibanje spremnika s komponentama ubrzanja $a_x$ i $a_z$, uz os $x$ vodoravno i os $z$ prema gore, slijede komponente

$$\frac{\partial p}{\partial x} = -\rho a_x, \qquad \frac{\partial p}{\partial z} = -\rho(g+a_z)$$

Klasična hidrostatika iz <span class="mf1-ch-ref"><span class="mf1-ch-code">U03</span><span class="mf1-ch-title">Hidrostatička raspodjela tlaka i manometrija</span></span> samo je poseban slučaj za $a_x = 0$ i $a_z = 0$. Jednako tako, pri slobodnom padu s $a_z = -g$ nestaje hidrostatički porast tlaka po visini, jer cijeli fluidni stupac ubrzava zajedno sa spremnikom. U najčešćem slučaju vodoravnog ubrzanja udesno vrijedi $a_x = a$ i $a_z = 0$, pa se relacija svodi na poznati zapis

$$\frac{\partial p}{\partial x} = -\rho a, \qquad \frac{\partial p}{\partial z} = -\rho g$$

Na slobodnoj površini tlak je konstantan, pa diferencijal promjene tlaka po samoj površini mora biti jednak nuli:

$$dp = \frac{\partial p}{\partial x}dx + \frac{\partial p}{\partial z}dz = 0$$

Uvrštavanjem parcijalnih derivacija dobiva se

$$-\rho a_x\,dx - \rho (g+a_z)\,dz = 0$$

odnosno nakon skraćivanja s $\rho$

$$\frac{dz}{dx} = -\frac{a_x}{g+a_z}$$

Za čisti vodoravni slučaj ponovno slijedi

$$\frac{dz}{dx} = -\frac{a}{g}$$

što znači da je slobodna površina okomita na vektor $\vec g_{eff}$. Za pravokutni spremnik duljine $L$ integracija nagiba preko cijele duljine daje

$$
\Delta h = \frac{aL}{g}.
$$

Fizikalno značenje relacije jest neposredno: što je spremnik dulji i što je ubrzanje veće, to je veća razlika razina između krajeva, dok gravitacija $g$ djeluje kao stabilizirajući član koji površinu vraća prema vodoravnom položaju.

## Riješeni primjeri

::: {.mf1-we}
<p class="mf1-box-label">Riješeni primjer - Otvoreni spremnik na laboratorijskim kolicima <span class="mf1-level">T2</span></p>

**Zadano**

Pravokutni otvoreni spremnik duljine $L = 1{,}60\ \text{m}$ i širine $B = 0{,}80\ \text{m}$ djelomično je ispunjen vodom do početne mirne visine $h_0 = 0{,}42\ \text{m}$. Spremnik se zatim giba vodoravno udesno stalnim ubrzanjem

$$
a = 1{,}35\ \text{m/s}^2
$$

**Traženo**

1. razliku razina slobodne površine između stražnje i prednje stijenke.
2. visinu vode uz stražnju i prednju stijenku.
3. kut nagiba slobodne površine prema vodoravnici.

![U04 Val 2 - otvoreni spremnik na laboratorijskim kolicima](../assets/print/u04_val2_laboratorijska_kolica.svg)

**Pretpostavke i model**

Promatra se translatorno ubrzanje bez prelijevanja i bez ogoljavanja dna. Zato je slobodna površina ravna, a srednja visina tekućine ostaje jednaka početnoj vrijednosti $h_0$.

**Rješenje**

Za vodoravno ubrzani spremnik vrijedi osnovna relacija

$$
\Delta h = \frac{aL}{g}
$$

pa numerički dobivamo

$$
\Delta h = \frac{1{,}35 \cdot 1{,}60}{9{,}81} = 0{,}220\ \text{m}
$$

odnosno

$$
\Delta h \approx 22{,}0\ \text{cm}
$$

Kako nema gubitka volumena, srednja visina ostaje

$$
\frac{h_{stražnja} + h_{prednja}}{2} = h_0 = 0{,}42\ \text{m}
$$

a razlika visina je

$$
h_{stražnja} - h_{prednja} = \Delta h = 0{,}220\ \text{m}
$$

Rješavanjem tog sustava slijedi

$$
h_{stražnja} = h_0 + \frac{\Delta h}{2} = 0{,}42 + 0{,}110 = 0{,}530\ \text{m}
$$

$$
h_{prednja} = h_0 - \frac{\Delta h}{2} = 0{,}42 - 0{,}110 = 0{,}310\ \text{m}
$$

Kut nagiba slobodne površine dobiva se iz efektnog polja sila:

$$
{}\tan\theta = \frac{a}{g} = \frac{1{,}35}{9{,}81} = 0{,}138
$$

pa je

$$
{}\theta = \arctan(0{,}138) \approx 7{,}9^\circ
$$

**Provjera i komentar**

Pri zadanom ubrzanju slobodna površina povisi se na stražnjoj strani za oko $11\ \text{cm}$ i jednako toliko padne na prednjoj strani. To je upravo najjednostavniji ulaz u relativno mirovanje prije nego što se uključe granični uvjeti prelijevanja ili sila na stijenci.

1. Ako je ubrzanje nula, mora biti i $\Delta h = 0$.
2. Kod gibanja udesno razina mora biti viša na stražnjoj strani spremnika.
3. Dobivene dubine moraju ostati pozitivne ako nema ogoljavanja dna, što je ovdje zadovoljeno.
:::

::: {.mf1-we}
<p class="mf1-box-label">Riješeni primjer - Procesna kada na automatskoj platformi <span class="mf1-level">T2</span></p>

**Zadano**

Pravokutna otvorena kada unutarnjih dimenzija $L = 1{,}80\ \text{m}$, $H = 0{,}72\ \text{m}$ i $B = 0{,}95\ \text{m}$ prevozi rashladnu tekućinu gustoće $\rho = 970\ \text{kg/m}^3$. U mirovanju je tekućina u kadi do visine $h_0 = 0{,}54\ \text{m}$. Kada se platforma počne gibati stalnim ubrzanjem udesno, tekućina se postavi u relativno mirovanje.

**Traženo**

1. Odredite najveće dopušteno ubrzanje $a_{max}$ pri kojem tekućina još ne prelijeva preko ruba kade.
2. Za to granično stanje odredite visinu tekućine uz stražnju i prednju stijenku.
3. Odredite rezultantnu silu fluida na stražnju vertikalnu stijenku po punoj širini kade.

Zanemarite valjanje, površinsku napetost i prolazne oscilacije.

![U04 Val 1 - procesna kada na ubrzanoj platformi](../assets/print/u04_val1_procesna_kada.svg)

**Pretpostavke i model**

Slobodna površina je ravna, a u graničnom stanju prelijevanja dodiruje gornji rub stražnje stijenke. Sve dok tekućina još ne prelijeva, srednja visina ostaje jednaka početnoj vrijednosti $h_0$.

**Rješenje**

Za granično stanje vrijedi

$$h_{stražnja} = H = 0{,}72\ \text{m}$$

te iz očuvanja srednje visine slijedi

$$\frac{h_{stražnja} + h_{prednja}}{2} = h_0$$

odakle je

$$h_{prednja} = 2h_0 - h_{stražnja} = 2 \cdot 0{,}54 - 0{,}72 = 0{,}36\ \text{m}$$

Razlika razina slobodne površine tada iznosi

$$\Delta h = h_{stražnja} - h_{prednja} = 0{,}36\ \text{m}$$

pa je maksimalno ubrzanje

$$a_{max} = g \frac{\Delta h}{L} = 9{,}81 \cdot \frac{0{,}36}{1{,}80} = 1{,}962\ \text{m/s}^2$$

odnosno

$$a_{max} \approx 1{,}96\ \text{m/s}^2$$

Za stražnju stijenku raspodjela tlaka je trokutasta, jer slobodna površina prolazi kroz njezin gornji rub. Rezultantna sila po punoj širini stijenke zato glasi

$$F_R = \frac{1}{2} \rho g B h_{stražnja}^2$$

Numerički:

$$F_R = \frac{1}{2} \cdot 970 \cdot 9{,}81 \cdot 0{,}95 \cdot 0{,}72^2 = 2343\ \text{N}$$

pa je

$$F_R \approx 2{,}34\ \text{kN}$$

Ako se želi i položaj hvatišta rezultante, ono je za trokutastu raspodjelu na visini $h_{stražnja}/3 = 0{,}24\ \text{m}$ od dna.

**Provjera i komentar**

1. Dobiveno ubrzanje je reda $0{,}20g$, što je fizikalno razumno za granično stanje bez prelijevanja.
2. Prednja dubina ostaje pozitivna, pa nema ogoljavanja dna uz prednju stijenku.
3. Sila reda nekoliko kilonjutna razumna je za gotovo metar široku stijenku i dubinu fluida oko $0{,}7\ \text{m}$.
:::

::: {.mf1-we}
<p class="mf1-box-label">Riješeni primjer - Zatvoreni servisni modul s kosom inspekcijskom stijenkom <span class="mf1-level">T2</span></p>

**Zadano**

Zatvoreni transportni modul jedinične širine prevozi tehnološku tekućinu gustoće $\rho = 960\ \text{kg/m}^3$. Iznad slobodne površine održava se jednoliki pretlak

$$
p_{M0} = 16\ \text{kPa}
$$

Tijekom probnog gibanja modul se ubrzava vodoravno udesno stalnim ubrzanjem

$$
a = 3{,}4\ \text{m/s}^2
$$

Unutar modula nalazi se ravna inspekcijska stijenka `AB`. Želi se da u radnom režimu slobodna površina bude okomita na stijenku `AB`, a gornji rub `A` neka bude točka dodira stijenke i slobodne površine. Vertikalna visina od ruba `A` do dna modula u točki `B` iznosi

$$
H = 0{,}55\ \text{m}
$$

**Traženo**

1. kut ${}\alpha$ pod kojim stijenku `AB` treba postaviti prema vodoravnici.
2. duljinu stijenke `AB`.
3. rezultantnu silu fluida na stijenku `AB` po jediničnoj širini modula.
4. udaljenost hvatišta rezultante od gornjeg ruba `A`, mjerenu po stijenci.

Zanemari prolazne oscilacije i promjenu gustoće plina iznad tekućine.

![U04 Val 3 - zatvoreni servisni modul s kosom inspekcijskom stijenkom](../assets/print/u04_val3_kosa_stijenka.svg)

**Pretpostavke i model**

Slobodna površina i u zatvorenom modulu mora biti okomita na efektivno polje sila $\vec{g}_{eff}$. Budući da je u plinskom prostoru iznad tekućine tlak jednolik, na gornjem rubu `A` tlak je jednak $p_{M0}$, a duž stijenke `AB` zatim linearno raste zbog efektivne težine fluida.

**Rješenje**

Najprije odredimo kut nagiba slobodne površine iz osnovne relacije relativnog mirovanja:

$$
{}\tan\theta = \frac{a}{g} = \frac{3{,}4}{9{,}81} = 0{,}347
$$

pa je

$$
{}\theta = \arctan(0{,}347) \approx 19{,}1^\circ
$$

Ako slobodna površina mora biti okomita na stijenku `AB`, tada stijenka mora zatvarati s vodoravnicom kut

$$
{}\alpha = 90^\circ - {}\theta = 90^\circ - 19{,}1^\circ = 70{,}9^\circ
$$

odnosno približno

$$
{}\alpha \approx 71^\circ
$$

Duljina stijenke slijedi iz zadane vertikalne projekcije $H$:

$$
s = \frac{H}{\sin\alpha} = \frac{0{,}55}{\sin 70{,}9^\circ} \approx 0{,}582\ \text{m}
$$

Efektivna težina po jedinici mase ima iznos

$$
g_{eff} = \sqrt{g^2 + a^2} = \sqrt{9{,}81^2 + 3{,}4^2} \approx 10{,}38\ \text{m/s}^2
$$

Na stijenci `AB` djeluju dvije komponente sile po jediničnoj širini modula:

1. jednolika komponenta zbog plinskog pretlaka.
2. linearno rastuća komponenta zbog raspodjele tlaka u tekućini uz $g_{eff}$.

Ploha stijenke po jediničnoj širini modula iznosi

$$
A_{AB} = s \cdot 1 = 0{,}582\ \text{m}^2
$$

Jednolika komponenta sile zato glasi

$$
F_0 = p_{M0} A_{AB} = 16\,000 \cdot 0{,}582 = 9312\ \text{N}
$$

Hidrostatski porast uz stijenku daje trokutastu komponentu

$$
F_h = \frac{1}{2} \rho g_{eff} s^2 \cdot 1 = \frac{1}{2} \cdot 960 \cdot 10{,}38 \cdot 0{,}582^2 \approx 1688\ \text{N}
$$

Ukupna rezultantna sila po jediničnoj širini modula iznosi

$$
F_R = F_0 + F_h = 9312 + 1688 = 11\,000\ \text{N}
$$

odnosno

$$
F_R \approx 11{,}0\ \text{kN/m}
$$

Za položaj hvatišta mjerimo udaljenost $y_R$ od ruba `A` po stijenci. Jednolika komponenta djeluje u polovini duljine $s/2$, a trokutasta u točki $2s/3$ od `A`, pa je

$$
y_R = \frac{F_0 \cdot (s/2) + F_h \cdot (2s/3)}{F_R}
$$

Numerički:

$$
y_R = \frac{9312 \cdot 0{,}291 + 1688 \cdot 0{,}388}{11\,000} \approx 0{,}306\ \text{m}
$$

Dakle, hvatište rezultante nalazi se približno

$$
y_R \approx 0{,}31\ \text{m}
$$

ispod ruba `A`, mjereno uzduž stijenke.

**Provjera i komentar**

1. Budući da je $a < g$, kut ${}\alpha$ mora ostati veći od $45^\circ$, što je ovdje zadovoljeno.
2. Da nema plinskog pretlaka, hvatište bi bilo dublje prema $2s/3$; ovdje ga jednolika komponenta vraća bliže sredini stijenke.
3. Ukupna sila mora biti veća od same hidrostatske komponente, a razumna je i to da pretlak ovdje nosi veći dio opterećenja.
:::

::: {.mf1-we}
<p class="mf1-box-label">Riješeni primjer - Rotirajući cilindrični spremnik bez prelijevanja <span class="mf1-level">T2</span></p>

**Zadano**

Otvoreni cilindrični spremnik polumjera

$$
R = 0{,}35\ \text{m}
$$

sadrži vodu početne srednje visine

$$
h_0 = 0{,}28\ \text{m}.
$$

Spremnik se zatim vrti stalnom kutnom brzinom

$$
\omega = 6{,}0\ \text{rad/s}.
$$

**Traženo**

1. razliku razina slobodne površine između stijenke i osi spremnika $\Delta h$.
2. visinu slobodne površine uz stijenku $h_{rub}$.
3. visinu slobodne površine na osi spremnika $h_{osa}$.

Zanemari prelijevanje i pretpostavi da volumen vode ostaje isti.

![Rotirajući cilindrični spremnik: paraboloidna slobodna površina (R=0,35 m, ω=6,0 rad/s)](../assets/print/u04_fig_rotirajuci_cilindar.svg){#fig-u04-rotirajuci-cilindar fig-align="center"}

**Pretpostavke i model**

U relativnom mirovanju pri rotaciji slobodna površina prelazi u paraboloid, ali se za osnovni proračun najprije može čitati razlika razina između ruba i osi. Kako nema prelijevanja, srednja visina ostaje jednaka početnoj vrijednosti $h_0$.

**Rješenje**

Razlika razina između stijenke i osi iznosi

$$
\Delta h = \frac{\omega^2 R^2}{2g} = \frac{6{,}0^2 \cdot 0{,}35^2}{2 \cdot 9{,}81}
$$

pa slijedi

$$
\Delta h = 0{,}225\ \text{m}
$$

odnosno

$$
\Delta h \approx 22{,}5\ \text{cm}.
$$

Kako volumen ostaje isti, srednja visina ostaje

$$
h_0 = \frac{h_{rub} + h_{osa}}{2}.
$$

Zato je visina uz stijenku

$$
h_{rub} = h_0 + \frac{\Delta h}{2} = 0{,}28 + \frac{0{,}225}{2} = 0{,}3925\ \text{m}
$$

pa je

$$
h_{rub} \approx 0{,}393\ \text{m}.
$$

Visina na osi spremnika iznosi

$$
h_{osa} = h_0 - \frac{\Delta h}{2} = 0{,}28 - \frac{0{,}225}{2} = 0{,}1675\ \text{m}
$$

odnosno

$$
h_{osa} \approx 0{,}168\ \text{m}.
$$

**Provjera i komentar**

1. Veća kutna brzina mora povećati razliku razina jer je $\Delta h \propto \omega^2$.
2. Ako nema prelijevanja, visina uz rub i visina u osi moraju ostati simetrične oko srednje visine $h_0$.
3. Visina na osi mora pasti, a visina uz stijenku porasti u odnosu na početnu ravnu razinu.
:::

::: {.mf1-ch}
<p class="mf1-box-label">Cjeloviti zadatak - rotirajući cilindrični spremnik s granicom prelijevanja <span class="mf1-level">T3</span></p>

**Zadano**

Otvoreni cilindrični kalibracijski spremnik unutarnjeg polumjera

$$
R = 0{,}40\ \text{m}
$$

i unutarnje visine

$$
H = 0{,}78\ \text{m}
$$

ispunjen je vodom gustoće

$$
\rho = 1000\ \text{kg/m}^3
$$

do mirne razine

$$
h_0 = 0{,}60\ \text{m}
$$

Spremnik se potom zavrti oko svoje okomite osi stalnom kutnom brzinom

$$
\omega = 5{,}20\ \text{rad/s}
$$

i nakon prolaznog razdoblja voda se postavi u relativno mirovanje kao kruto rotirajuće tijelo.

**Traženo**

1. razliku razina slobodne površine između stijenke i osi spremnika $\Delta h$.
2. dubinu vode na osi spremnika $h_C$ i uz stijenku $h_R$.
3. manometarski tlak na dnu u središnjoj točki `C` i u rubnoj točki `D`.
4. najveći dopušteni broj okretaja prije prelijevanja, izražen kao $\omega_{max}$ i $n_{max}$ u okr/min.

Zanemari površinsku napetost, valjanje i otpor zraka.

![U04 CH 1 - rotirajući cilindrični spremnik](../assets/print/u04_ch1_rotirajuci_spremnik_paraboloid.svg)

**Pretpostavke i model**

U stanju relativnog mirovanja pri vrtnji fluid se opet giba kao kruto tijelo, ali sada s konstantnom kutnom brzinom $\omega$. Zato u cilindričnim koordinatama vrijedi da tlak radijalno raste prema stijenci, a po visini i dalje opada zbog gravitacije:

$$
\frac{\partial p}{\partial r} = \rho \omega^2 r, \qquad \frac{\partial p}{\partial z} = -\rho g
$$

::: {.callout-note}
## 📐 Fizikalno značenje
Prva jednadžba kaže da tlak radijalno raste prema stjenci jer centrifugalna pseudo-sila gura fluid prema van: više $r$, više tlaka. Druga jednadžba je ista stara hidrostatika po visini. Zajedno definiraju "dvosmjerni" tlak u rotirajućem spremniku: po radijusu raste, po visini pada. Zato na slobodnoj površini mora postojati parabolični kompromis između tih dviju tendencija.
:::

Iz toga slijedi da slobodna površina i druge plohe stalnog tlaka više nisu ravnine nego paraboloidi revolucije. U aksijalnom presjeku zato vrijedi parabola

$$
h(r) = h_C + \frac{\omega^2 r^2}{2g}
$$

::: {.callout-note}
## 📐 Fizikalno značenje
Parabola $h(r) = h_C + \omega^2 r^2/(2g)$ opisuje oblik slobodne površine: na osi vrtnje površina je najniža ($h_C$), a prema stjenci raste kvadratno. Veća kutna brzina $\omega$ ili veći polumjer $R$ daju strmiji paraboloid. Faktor $2g$ u nazivniku dolazi od integracije centrifugalnog ubrzanja $\omega^2 r$ po radijusu – isti tip kao $v^2/(2g)$ u Bernoullijevoj jednadžbi koja slijedi u <span class="mf1-ch-ref"><span class="mf1-ch-code">U09</span><span class="mf1-ch-title">Bernoullijeva jednadžba idealnog fluida</span></span>.
:::

::: {.callout-note}
## 📝 Razrada koraka
Korak: $\partial p/\partial r = \rho\omega^2 r$ i $\partial p/\partial z = -\rho g$ $\;\Rightarrow\;$ $h(r) = h_C + \omega^2 r^2/(2g)$

Na slobodnoj površini vrijedi $dp = 0$, pa:
$$
0 = \frac{\partial p}{\partial r}\,dr + \frac{\partial p}{\partial z}\,dz = \rho\omega^2 r\,dr - \rho g\,dz.
$$
Dijeljenje s $\rho g$ i premještanje članova:
$$
\frac{dz}{dr} = \frac{\omega^2 r}{g}.
$$
Integracija od osi ($r = 0$, $z = h_C$) do radijusa $r$:
$$
z(r) = h_C + \frac{\omega^2}{g}\int_0^r r'\,dr' = h_C + \frac{\omega^2 r^2}{2g}.
$$
:::

gdje je $r$ udaljenost od osi vrtnje. Budući da nema prelijevanja pri zadanom režimu, ukupni volumen vode ostaje isti pa je srednja visina i dalje jednaka početnoj vrijednosti $h_0$.

**Rješenje**

#### 1. Razlika razina slobodne površine

Iz izraza za paraboloidnu slobodnu površinu razlika između stijenke i osi spremnika iznosi

$$
\Delta h = h_R - h_C = \frac{\omega^2 R^2}{2g}
$$

Numerički:

$$
\Delta h = \frac{5{,}20^2 \cdot 0{,}40^2}{2 \cdot 9{,}81} = 0{,}2205\ \text{m}
$$

odnosno

$$
\Delta h \approx 0{,}221\ \text{m} = 22{,}1\ \text{cm}
$$

#### 2. Dubina na osi i uz stijenku

Kako se volumen nije promijenio, srednja visina ostaje

$$
h_0 = \frac{h_C + h_R}{2}
$$

uz relaciju

$$
h_R - h_C = \Delta h
$$

Zato je

$$
h_C = h_0 - \frac{\Delta h}{2} = 0{,}60 - \frac{0{,}2205}{2} = 0{,}4897\ \text{m}
$$

$$
h_R = h_0 + \frac{\Delta h}{2} = 0{,}60 + \frac{0{,}2205}{2} = 0{,}7103\ \text{m}
$$

odnosno približno

$$
h_C \approx 0{,}490\ \text{m}, \qquad h_R \approx 0{,}710\ \text{m}
$$

#### 3. Tlak na dnu u točkama `C` i `D`

Na dnu spremnika lokalni manometarski tlak dobiva se iz lokalne dubine ispod slobodne površine. U osi spremnika vrijedi

$$
p_{M,C} = \rho g h_C = 1000 \cdot 9{,}81 \cdot 0{,}4897 = 4804\ \text{Pa}
$$

pa je

$$
p_{M,C} \approx 4{,}80\ \text{kPa}
$$

Uz stijenku je dubina veća, pa je

$$
p_{M,D} = \rho g h_R = 1000 \cdot 9{,}81 \cdot 0{,}7103 = 6968\ \text{Pa}
$$

odnosno

$$
p_{M,D} \approx 6{,}97\ \text{kPa}
$$

#### 4. Granica prelijevanja

Do prelijevanja dolazi kada slobodna površina uz stijenku dosegne rub spremnika, odnosno kada je

$$
h_R = H
$$

Kako za rotaciju bez gubitka volumena vrijedi

$$
h_R = h_0 + \frac{\omega^2 R^2}{4g}
$$

granična kutna brzina zadovoljava

$$
H = h_0 + \frac{\omega_{max}^2 R^2}{4g}
$$

pa je

$$
\omega_{max} = \sqrt{\frac{4g(H-h_0)}{R^2}} = \sqrt{\frac{4 \cdot 9{,}81 \cdot (0{,}78-0{,}60)}{0{,}40^2}} = 6{,}64\ \text{rad/s}
$$

Broj okretaja tada iznosi

$$
n_{max} = \frac{60\omega_{max}}{2\pi} = \frac{60 \cdot 6{,}64}{2\pi} = 63{,}4\ \text{okr/min}
$$

**Provjera i komentar**

Pri radnoj brzini vrtnje slobodna površina podigne se uz stijenku za oko $22{,}1\ \text{cm}$ u odnosu na os spremnika. Time dubina u osi padne na oko $0{,}490\ \text{m}$, a uz stijenku naraste na oko $0{,}710\ \text{m}$. Zato je manometarski tlak na dnu u središtu oko $4{,}80\ \text{kPa}$, a uz stijenu oko $6{,}97\ \text{kPa}$. Granica prelijevanja nastupa tek pri oko $6{,}64\ \text{rad/s}$, odnosno oko $63{,}4\ \text{okr/min}$.

1. Uz stijenku dubina mora biti veća nego na osi, jer se slobodna površina pri vrtnji podiže prema rubu.
2. Ako je $\omega = 0$, paraboloid se mora vratiti na ravnu slobodnu površinu i opet vrijedi $h_C = h_R = h_0$.
3. Budući da je pri radnom režimu $h_R < H$, spremnik još ne prelijeva, što je u skladu s dobivenom sigurnosnom rezervom do ruba.
:::

::: {.mf1-we}
<p class="mf1-box-label">Riješeni primjer – Nagib goriva u spremniku autocisterne pri kočenju &nbsp;<span class="mf1-level">T2</span></p>

🔩 **Primjer za strojare**

**Kontekst:** Autocisterna za gorivo s pravokutnim spremnikom kočenjem usporava. Posuje li gorivo na gornji rubnik stijenke i hoće li se pumpa za pražnjenje na stražnjoj stijenci izložiti zraku?

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

![Nagib goriva u autocisterni pri kočenju (L=1,2 m, h₀=0,45 m, a=3,8 m/s²)](../assets/print/u04_fig_autocisterna_kocenje.svg){#fig-u04-autocisterna-kocenje fig-align="center"}

**Pretpostavke i model**

Kočenje je jednoliko usporavanje (a = konst.). Fluid se smatra nestlačivim, bez prelaznih valova. Srednja visina goriva ostaje $h_0$ jer nema prelijevanja.

**Rješenje**

Razlika razina (gorivo se pri kočenju giba prema naprijed, tj. prema prednjoj stijenci):

$$
\Delta h = \frac{aL}{g} = \frac{3{,}8 \cdot 1{,}20}{9{,}81} = 0{,}465\ \text{m}
$$

Visina uz prednju stijenku (podignut nivo):

$$
h_{prednja} = h_0 + \frac{\Delta h}{2} = 0{,}45 + 0{,}233 = 0{,}683\ \text{m}
$$

Visina uz stražnju stijenku (snižen nivo):

$$
h_{stražnja} = h_0 - \frac{\Delta h}{2} = 0{,}45 - 0{,}233 = 0{,}217\ \text{m}
$$

**Provjera i komentar**

Prednja stijenka dostiže $h = 0{,}683\ \text{m}$ što je ispod vrha ($H = 0{,}80\ \text{m}$) – nema prelijevanja. Stražnja stijenka zadržava $0{,}217\ \text{m}$ – pumpa za pražnjenje nije izložena zraku. Pri strožem kočenju ($a > 5{,}0\ \text{m/s}^2$) prednji zid bi bio natopljeniji od ruba, a pri $a > 7{,}4\ \text{m/s}^2$ dno stražnje strane bi se ogolilo. Ova analiza opravdava ograničenja brzine punjenja i kočenja kod autocisterni.

:::

::: {.mf1-we}
<p class="mf1-box-label">Riješeni primjer – Vodena cisterna vatrogasnog vozila pri naglom zaustavljanju &nbsp;<span class="mf1-level">T2</span></p>

🏗️ **Primjer za građevinare**

**Kontekst:** Vatrogasno vozilo s pravokutnim cisternama za vodu naglo se zaustavlja da bi zauzelo položaj. Projektant provjerava hoće li sile na prednju stjenku cisterne i stanje razine ostati u prihvatljivim granicama.

**Zadano**

- Duljina cisterne: $L = 2{,}40\ \text{m}$
- Mirna razina vode: $h_0 = 1{,}20\ \text{m}$
- Visina cisterne: $H = 1{,}60\ \text{m}$
- Usporenje: $a = 4{,}5\ \text{m/s}^2$

**Traženo**

1. Razlika razina slobodne površine.
2. Visina vode uz prednju i stražnju stijenku.
3. Kut nagiba slobodne površine prema vodoravnici.

![Vodena cisterna vatrogasnog vozila pri zaustavljanju (L=2,4 m, h₀=1,2 m, a=4,5 m/s²)](../assets/print/u04_fig_vatrogasna_cisterna.svg){#fig-u04-vatrogasna-cisterna fig-align="center"}

**Pretpostavke i model**

Jednoliko usporavanje, ravna slobodna površina, bez prelijevanja.

**Rješenje**

$$
\Delta h = \frac{aL}{g} = \frac{4{,}5 \cdot 2{,}40}{9{,}81} = 1{,}101\ \text{m}
$$

$$
h_{prednja} = 1{,}20 + \frac{1{,}101}{2} = 1{,}751\ \text{m}
$$

$$
h_{stražnja} = 1{,}20 - \frac{1{,}101}{2} = 0{,}650\ \text{m}
$$

$$
\tan\theta = \frac{a}{g} = \frac{4{,}5}{9{,}81} = 0{,}459 \quad\Rightarrow\quad \theta \approx 24{,}7^\circ
$$

**Provjera i komentar**

Prednja stijenka doseže $1{,}751\ \text{m}$ – blizu vrha $H = 1{,}60\ \text{m}$! Dolazi do prelijevanja: pretpostavka ravne površine bez prelijevanja nije zadovoljena. U stvarnosti dizajn ovakve cisterne treba uključiti bafle (pregradne ploče) koje ograničavaju nagib slobodne površine i dinamičke sile na stijenke.

:::

## Usporedna tablica: strojarstvo i građevinarstvo

| Koncept | Strojarstvo – gdje se pojavljuje | Građevinarstvo – gdje se pojavljuje |
|---------|----------------------------------|--------------------------------------|
| Δh = aL/g (translacijsko ubrzanje) | Nagib goriva u spremniku autocisterne i rezervoaru motocikla; kondenzat u horizontalnoj cijevi cijevovoda | Voda u cisterni vatrogasnog vozila ili mobilne mješalice betona; mjerenje ubrzanja senzorima nagiba slobodne površine |
| Efektivno polje sila $\vec{g}_{eff}$ | Separacija smjese u centrifugalnom separatoru ulje-voda; raspodjela tlaka u rotirajućem pumpanom sustavu | Centrifugalni efekti pri kompaktiranju betona vibratorom; fluid u zakrivljenom turbinskom tunelu |
| Paraboloidna slobodna površina | Centrifugalne pumpe i turbine: oblik slobodne površine u rotirajućem uljnom bazenu ležaja | Laboratorijski testovi stabilnosti pri vrtnji; vodeni prsten u centrifugalnoj bušaćoj koloni |
| Granično stanje prelijevanja | Sigurnosni volumen u hydrauličnom rezervoaru vozila pri ubrzanju/kočenju | Projektiranje bafelnih ploča u cisternama (IACS / EN standardi za plovila) |

## Zadaci za vježbu

::: {.mf1-vjezbe-list}
1. **T1** Otvoreni pravokutni spremnik duljine $L = 1{,}80\ \text{m}$ i početne dubine vode $h_0 = 0{,}34\ \text{m}$ giba se vodoravno stalnim ubrzanjem $a = 1{,}20\ \text{m/s}^2$. Odredi razliku razina između krajeva spremnika, lokalne dubine uz stražnju i prednju stijenku te provjeri dolazi li do prelijevanja ako je visina boka $H = 0{,}46\ \text{m}$.

	**Natuknica:** $\Delta h = aL/g$; zatim $h_{str} = h_0 + \Delta h/2$ i $h_{pred} = h_0 - \Delta h/2$; usporedi $h_{str}$ s $H$.

	**Skica:** da - pravokutni spremnik, vektor $a$, kosa slobodna ploha, kote $L$, $h_0$ i $H$.

2. **T1** Otvoreni spremnik duljine $L = 1{,}40\ \text{m}$ napunjen je do visine $h_0 = 0{,}30\ \text{m}$, a visina boka je $H = 0{,}42\ \text{m}$. Odredi najveće vodoravno ubrzanje prije početka prelijevanja.

	**Natuknica:** u graničnom stanju vrijedi $h_{str} = H$ i $\Delta h = 2(H-h_0)$; nakon toga $a = g\Delta h/L$.

	**Skica:** da - spremnik s rubom prelijevanja, kosa slobodna ploha i kote $L$, $h_0$, $H$.

3. **T2** Zatvoreni vertikalni cilindar potpuno ispunjen uljem gustoće $\rho = 870\ \text{kg/m}^3$ ima visinu stupca fluida $h = 0{,}75\ \text{m}$. Sustav se giba prema gore ubrzanjem $a_z = 2{,}3\ \text{m/s}^2$. Odredi razliku tlaka između dna i vrha cilindra te usporedi rezultat s mirovnim stanjem.

	**Natuknica:** koristi efektivnu težinu fluida: $\Delta p = \rho (g+a_z)h$; za usporedbu u mirovanju uzmi $\Delta p_0 = \rho gh$.

	**Skica:** da - vertikalni cilindar, smjer $a_z$, kote $h$ te tlakovi na vrhu i dnu.

4. **T2** Ubrzani otvoreni spremnik širine stijenke $b = 0{,}75\ \text{m}$ i duljine $L = 1{,}60\ \text{m}$ s početnom dubinom $h_0 = 0{,}36\ \text{m}$ nosi na stražnjoj stijenci hidrostatsku silu $F = 820\ \text{N}$. Odredi ubrzanje spremnika ako nema prelijevanja.

	**Natuknica:** iz sile vrati lokalnu dubinu preko $F = \rho g b h_{str}^2/2$; zatim $h_{str} = h_0 + \Delta h/2$ i $a = g\Delta h/L$.

	**Skica:** da - spremnik, stražnja stijena s rezultantom $F$, slobodna ploha i vektor $a$.

5. **T3** Cilindrična posuda radijusa $R = 0{,}28\ \text{m}$ s početnom dubinom vode $h_0 = 0{,}22\ \text{m}$ vrti se stalnom kutnom brzinom $\omega = 5{,}5\ \text{rad/s}$. Odredi porast razine uz stijenku, spuštanje razine u osi i procijeni ostaje li dno u osi potpuno prekriveno vodom.

	**Natuknica:** razlika razina je $\Delta h = \omega^2 R^2/(2g)$; uz očuvanje volumena vrijedi $h_{rub} = h_0 + \Delta h/2$ i $h_{osa} = h_0 - \Delta h/2$.

	**Skica:** da - aksijalni presjek posude, parabolična slobodna ploha, kote $R$, $h_0$, $h_{rub}$ i $h_{osa}$.

6. **T3** Otvoreni cilindrični spremnik polumjera $R = 0{,}32\ \text{m}$ i visine $H = 0{,}62\ \text{m}$ ispunjen je vodom do početne srednje visine $h_0 = 0{,}46\ \text{m}$. Odredi najveću kutnu brzinu pri kojoj još nema prelijevanja. Zatim za radni režim $\omega = 0{,}80\,\omega_{max}$ odredi dubinu vode u osi i uz stijenu te manometarske tlakove na dnu u tim dvjema točkama.

	**Natuknica:** u graničnom stanju vrijedi $h_{rub} = H = h_0 + \omega_{max}^2 R^2/(4g)$; za radni režim najprije nađi $\Delta h = \omega^2 R^2/(2g)$, zatim $h_{osa}$ i $h_{rub}$, a tlakove iz $p_M = \rho gh$.

	**Skica:** da - aksijalni presjek cilindra, paraboloidna slobodna ploha, točke na osi i uz stijenu te kote $R$, $H$ i $h_0$.
:::

![U04 zadaci za vježbu - minimalne grayscale tehničke skice uz zadatke.](../assets/print/u04_vjezbe_skice.svg)

::: {.mf1-zavrsni-okvir}
<p class="mf1-box-label">Za ponijeti iz poglavlja</p>

**Sažeta provjera prije računa**

- Treba najprije odrediti smjer efektivnog polja sila, a ne odmah krenuti na tlak.
- Treba razlikovati znači li zadano stanje očuvanje volumena, prelijevanje ili ogoljavanje dna.
- Relacija $\Delta h = aL/g$ koristi se tek nakon što je geometrija spremnika jasna.
- Sila na stijenci treba se računati iz lokalne dubine uz tu stijenu, a ne iz početne mirne razine.
- Translaciju, vertikalno ubrzanje i rotaciju treba razdvojiti kao tri različita fizikalna scenarija.

**Najčešća pogreška**

Najčešća greška je pročitati granično stanje samo jednim uvjetom. U zadacima prelijevanja treba istodobno zadovoljiti dodir slobodne površine s rubom spremnika i očuvanje srednje visine sve dok nema gubitka volumena.

**Nakon ovoga poglavlja mora biti moguće**

1. odrediti smjer i ulogu efektivnog polja sila u translatorno ubrzanom spremniku.
2. pročitati nagib slobodne površine i iz njega izvesti lokalne dubine uz stijene.
3. spojiti geometriju slobodne površine s raspodjelom tlaka i rezultantnom silom.

**U tehnici to znači**

Gorivni spremnik vozila pri kočenju, autocisterna u zavoju i centrifuga u radnom režimu svi traže isto čitanje: gdje se u novom polju sila nalazi slobodna površina i kakav tlak zbog toga nastaje uz stijenke. Na toj se osnovi procjenjuju prelijevanje, ogoljavanje usisa i promjena opterećenja konstrukcije.

**Granica modela**

Ovaj model vrijedi kad se tekućina prema spremniku zaista smirila, odnosno kad su prolazne oscilacije zanemarive. Ako su valjanje, udari, prskanje ili slobodno njihanje tekućine bitni, slika relativnog mirovanja više nije dovoljna sama za sebe.

<span class="mf1-ch-ref"><span class="mf1-ch-code">U04</span><span class="mf1-ch-title">Relativno mirovanje fluida</span></span> nije samo nastavak hidrostatike, nego promjena referentnog okvira. Prvo se određuje kako izgleda efektivno polje sila, zatim slobodna površina, a tek onda tlak i sila na stijenkama.
:::

::: {.mf1-numerika}
<p class="mf1-box-label">🖥️ Numerički most</p>

**Gdje ovo živi u numerici.** Promjena referentnog okvira iz ovog poglavlja je upravo *jezgra* numeričkih pristupa rotirajućim domenama: pumpe, ventilatori, vodne i plinske turbine, centrifuge. Umjesto da mreža fizički rotira (skupo!), CFD solver dodaje **prividne sile** — centrifugalnu i Coriolisovu — točno onako kako si ti u zadacima dodavao $a_{cf} = \omega^2 r$.

**Što numerički alat radi s tim.** **MRF (Moving Reference Frame)** definira zonu u mreži koja se "vrti" matematički — rješavanjem Navier-Stokesa u rotirajućem sustavu s dopisanim Coriolisovim i centrifugalnim članom. Za pune nestacionarne simulacije postoji i **sliding mesh** gdje se rotor i stator fizički kližu jedan uz drugog.

**Alati gdje ćeš to sresti:** `OpenFOAM` (`MRFZone`, `simpleFoam` s rotacijom) · `ANSYS Fluent` (*Frame Motion*, *Sliding Mesh*) · `Star-CCM+` (*Rotating Reference Frame*).

> *Nije gradivo MF1. Paraboloidnu slobodnu površinu iz centrifuge ovdje, u CFD-u ćeš vidjeti kao polje koje solver sam izračuna.*
:::








