![Pregled poglavlja: turbostrojevi i propulzija kroz pokretne lopatice, moment i potisak.](../assets/print/u12_fig_uvod_pregled.svg){#fig-uvod-u12 fig-align="center" fig-alt="Pregled poglavlja: turbostrojevi i propulzija kroz pokretne lopatice, moment i potisak."}

## Turbostrojevi i propulzija — račun u relativnom okviru

Količina gibanja je ovdje izravni ulaz u lopatice i mlazni potisak.

Naslov poglavlja vodi prema turbinama, vodilicama i potisku, ali temelj ostaje isti kao i u prethodnom poglavlju: jasan kontrolni volumen i ispravno pročitana promjena količine gibanja.

Na toj se osnovi zatim grade reakcija nosača, snaga na pokretnim lopaticama i mlazni potisak.

::: {.mf1-application}
<p class="mf1-box-label">Inženjerski kontekst</p>

Pokretne lopatice i potisak nisu školski dodatak, nego jezgra rada Peltonova kola, vodomlaznog pogona, mlaznih čistača i svake ispitne glave koja skreće mlaz radi sile ili momenta. U strojarstvu i brodogradnji isti račun odlučuje koliko snage rotor stvarno prima, koliki potisak ostaje na nosaču i kako izbor izlaznog kuta mijenja korisni učinak stroja.
:::

::: {.mf1-priprema}
<p class="mf1-box-label">Prije čitanja poglavlja</p>

**Predznanje koje se pretpostavlja:**

- zakon količine gibanja iz poglavlja <span class="mf1-ch-ref"><span class="mf1-ch-code">pog. 10</span><span class="mf1-ch-title">Količina i moment količine gibanja</span></span>;
- pojam relativne i apsolutne brzine, vektor brzine i njegove komponente;
- kinematika kružnog gibanja, kutna i obodna brzina;
- pojam mehaničkog rada i snage u rotacijskom gibanju.

**Ishodi učenja:**

- razlikovati apsolutnu, relativnu i obodnu brzinu te ih ispravno kombinirati u trokutima brzina;
- izračunati silu i snagu koju fluid predaje pokretnoj lopatici;
- odrediti optimalnu obodnu brzinu za maksimalan korisni rad rotora;
- primijeniti istu logiku količine gibanja na potisak (vodomlazni pogoni, sustavi reakcijskog tipa).

**Procijenjeno vrijeme rada uz udžbenik:** 9 sati.
:::

## Fizikalni uvod i matematički izvod

Kad mlaz promijeni smjer ili iznos brzine, mora postojati sila koja je uzrokovala tu promjenu količine gibanja. Za nepomični kontrolni volumen, stacionaran tok te jedan ulaz i izlaz osnovni zapis je

$$\sum \vec{F} = \dot{m}(\vec{V}_{izl} - \vec{V}_{ul})$$ {#eq-turbostrojevi-fizikalni-uvod-i-matematicki-izvod-01}

::: {.mf1-fizikalno-znacenje}
<p class="mf1-box-label">Fizikalno značenje</p>
Za pokretnu lopaticu ili vodilicu ovaj zakon kaže: sila potrebna za skretanje ili usporavanje mlaza proporcionalna je masenom protoku i promjeni vektora brzine. Za idealizirani Peltonov rotor s punim sapničkim protokom relativna brzina ulaza jest $w_1=c_1-u$. Snaga je umnožak tangencijalne sile i obodne brzine, pa pri $u=0$ postoji sila bez snage, a pri $u\to c_1$ nestaje relativni dotok. Između tih granica model daje maksimum pri $u=c_1/2$.
:::

To je najjači radni most prema svemu što kasnije dolazi u <span class="mf1-ch-ref"><span class="mf1-ch-code">pog. 14</span><span class="mf1-ch-title">Turbostrojevi i propulzija</span></span>: nepomična vodilica, pokretna lopatica, moment na rotoru i mlazni potisak. Ako se u tom osnovnom obliku ne učvrste znakovi i smjerovi, kasniji zadaci vrlo brzo postaju samo algebra bez fizike.

## Matematički izvod

Za stacionarni tok kroz vodilicu ili lopaticu najprije se određuje maseni protok

$$
\dot m = \rho A v_n,
$$ {#eq-turbostrojevi-matematicki-izvod-01}

gdje je $v_n$ komponenta brzine okomita na ulazni presjek. Za nepomičnu vodilicu ili lopaticu, uz zanemarive tlakne razlike prema atmosferi i uz zanemarivu težinu u promatranoj ravnini, zakon količine gibanja daje

$$
\vec F_{okoline\to fluid} = \dot m(\vec c_2 - \vec c_1).
$$ {#eq-turbostrojevi-matematicki-izvod-02}

Najčešći lom zadatka nije račun površine ili protoka, nego znak: ta jednadžba najprije daje silu okoline na fluid. Tek suprotan predznak daje silu fluida na vodilicu i reakciju nosača,

$$
\vec F_{fluid\to vodilicu} = -\dot m(\vec c_2 - \vec c_1).
$$ {#eq-turbostrojevi-matematicki-izvod-03}

U komponentnom zapisu odmah se vidi kako svaki izlazni zaokret ili pad brzine stvara novu reakciju po odgovarajućoj osi. Time ista jednadžba količine gibanja u <span class="mf1-ch-ref"><span class="mf1-ch-code">pog. 14</span><span class="mf1-ch-title">Turbostrojevi i propulzija</span></span> počinje raditi dva posla odjednom: ako fluid izgubi tangencijalnu komponentu brzine, rotor ili lopatica primaju silu, moment i snagu; ako fluid dobije brzinu prema dolje ili unatrag, cijeli sustav prima potisak.

Za pokretnu lopaticu prvi korak nije sila nego razdvajanje apsolutne i relativne brzine. Opći RTT iz poglavlja <span class="mf1-ch-ref"><span class="mf1-ch-code">pog. 7</span><span class="mf1-ch-title">Kinematika, kontrolni volumen i kontinuitet</span></span> daje, u inercijskom okviru,

$$
\frac{d}{dt}\int_{KV(t)}\rho\vec c\,dV
+\int_{KP(t)}\rho\vec c\bigl[(\vec c-\vec v_{KP})\cdot\vec n\bigr]\,dA
=\sum\vec F.
$$ {#eq-turbostrojevi-matematicki-izvod-04}

Količina gibanja u integrandu računa se apsolutnom brzinom $\vec c$, dok masu kroz gibajuću plohu prenosi relativna brzina $\vec c-\vec v_{KP}$. Ako je kontrolna ploha vezana uz lopaticu koja se lokalno giba brzinom $\vec u$, tada je $\vec v_{KP}=\vec u$ i

$$
\vec w_1 = \vec c_1 - \vec u, \qquad \dot m_{rel} = \rho A w_{1n}.
$$ {#eq-turbostrojevi-matematicki-izvod-05}

Ako je akumulacija količine gibanja u tako odabranom volumenu jednaka nuli i postoje jedan ulaz i izlaz s 1D profilima, bilanca se reducira na

$$
\vec F_{okoline\to fluid} = \dot m_{rel}(\vec c_2 - \vec c_1),
\qquad
\vec F_{fluid\to lopaticu} = -\vec F_{okoline\to fluid}.
$$ {#eq-turbostrojevi-matematicki-izvod-06}

Za pojedinačnu lopaticu koja se pravocrtno giba stalnom brzinom to je izravan radni model. Za cijeli rotor sigurnije je primijeniti moment količine gibanja na nepomični prstenasti kontrolni volumen; ako se prati pojedinačni rotirajući volumen, član akumulacije odnosno članovi neinercijskoga okvira ne smiju se prešutjeti.

::: {.callout-note}
## Razrada koraka
Korak: od relativne brzine ($\vec{w}$) → apsolutna sila na pokretnu lopaticu

**1. Relativni ulaz:** Lopatica se giba brzinom $u$, pa mlaz „vidi" lopaticu s relativnom brzinom $w_1 = c_1 - u$ (u 1D slučaju u smjeru mlaza). Maseni protok koji zaista prolazi kroz lopaticu:
$$\dot{m} = \rho A w_1.$$ {#eq-turbostrojevi-razrada-koraka-01}

**2. Relativni izlaz:** Na lopatici brzina prelazi lom kuta $\beta_2$. U relativnom okviru izlazna brzina je $w_2 = w_1$ (bez gubitaka). U apsolutnom okviru:
$$c_{2x} = u + w_2\cos\beta_2, \qquad c_{2y} = w_2\sin\beta_2.$$ {#eq-turbostrojevi-razrada-koraka-02}

**3. Promjena količine gibanja** (u apsolutnom okviru) najprije daje silu lopatice na fluid:
$$F_{lop\to f,x} = \dot{m}(c_{2x} - c_1) = \dot{m}w_1(\cos\beta_2 - 1).$$ {#eq-turbostrojevi-razrada-koraka-03}

Sila fluida na lopaticu ima suprotan predznak:
$$F_{f\to lop,x}=\dot m w_1(1-\cos\beta_2).$$ {#eq-turbostrojevi-razrada-koraka-04}

**4. Snaga koju fluid predaje lopatici:**
$$P_{f\to lop}=F_{f\to lop,x}u=\dot{m}w_1u(1-\cos\beta_2).$$ {#eq-turbostrojevi-razrada-koraka-05}

Za $\beta_2 = 180°$ (idealni U-lom) funkcija snage jedne lopatice glasi $P(u)=2\rho A(c_1-u)^2u$. Tek deriviranjem se pokazuje da joj je maksimum pri $u=c_1/3$. Za kolo s mnogo lopatica puni sapnički protok ostaje stalan, pa drugi model daje $u=c_1/2$.
:::

::: {.mf1-izvod}
<p class="mf1-box-label">Matematički izvod — Optimum obodne brzine za jednu lopaticu i za kolo</p>

Razlikuju se dva pedagoški važna granična slučaja koja daju različite optimalne obodne brzine, ovisno o tome kako se računa maseni protok kroz lopaticu.

**Slučaj 1: Jedna lopatica koja bježi pred mlazom**

Pri pojedinačnoj lopatici koja se giba u smjeru mlaza, mlaz mora "stići" lopaticu prije nego što na nju djeluje. Maseni protok koji efektivno djeluje na lopaticu je relativni protok

$$
\dot m = \rho A (c_1 - u),
$$ {#eq-turbostrojevi-matematicki-izvod-optimum-obodne-brzine-za-jednu-01}

pa se sila i snaga zapisuju kao

$$
F = \dot m\,(c_1 - u)(1 - \cos\beta_2) = \rho A (c_1 - u)^2 (1 - \cos\beta_2),
$$ {#eq-turbostrojevi-matematicki-izvod-optimum-obodne-brzine-za-jednu-02}

$$
P = F\,u = \rho A (1 - \cos\beta_2)(c_1 - u)^2 u.
$$ {#eq-turbostrojevi-matematicki-izvod-optimum-obodne-brzine-za-jednu-03}

Uvjet maksimuma snage je $dP/du = 0$. Deriviranjem se dobiva

$$
\frac{dP}{du} = \rho A (1 - \cos\beta_2)\Bigl[(c_1 - u)^2 - 2(c_1 - u)u\Bigr] = \rho A (1 - \cos\beta_2)(c_1 - u)(c_1 - 3u).
$$ {#eq-turbostrojevi-matematicki-izvod-optimum-obodne-brzine-za-jednu-04}

Netrivijalno rješenje ($c_1 - u \ne 0$) daje **$u_{opt} = c_1/3$**.

**Slučaj 2: Kolo s mnogo lopatica (Peltonov rotor)**

Pri rotoru s velikim brojem lopatica mlaz uvijek nalazi sljedeću lopaticu, pa cijeli protok kroz sapnicu sudjeluje u izmjeni količine gibanja:

$$
\dot m = \rho A c_1.
$$ {#eq-turbostrojevi-matematicki-izvod-optimum-obodne-brzine-za-jednu-05}

Sila na lopaticu i snaga predani rotoru su tada

$$
F = \dot m\,(c_1 - u)(1 - \cos\beta_2) = \rho A c_1 (c_1 - u)(1 - \cos\beta_2),
$$ {#eq-turbostrojevi-matematicki-izvod-optimum-obodne-brzine-za-jednu-06}

$$
P = F\,u = \rho A c_1 (1 - \cos\beta_2)(c_1 - u)\,u.
$$ {#eq-turbostrojevi-matematicki-izvod-optimum-obodne-brzine-za-jednu-07}

Uvjet $dP/du = 0$ daje

$$
\frac{dP}{du} = \rho A c_1 (1 - \cos\beta_2)\bigl[(c_1 - u) - u\bigr] = \rho A c_1 (1 - \cos\beta_2)(c_1 - 2u) = 0,
$$ {#eq-turbostrojevi-matematicki-izvod-optimum-obodne-brzine-za-jednu-08}

odakle slijedi **$u_{opt} = c_1/2$**.

**Fizikalna interpretacija razlike:**

Ključna razlika između dvaju slučajeva leži u tome koji maseni protok ulazi u proračun:

- Pri pojedinačnoj lopatici, $\dot m$ samo ovisi o $(c_1 - u)$, što daje kvadratnu ovisnost sile o relativnoj brzini. Optimum je niži ($u_{opt} = c_1/3$) jer veće $u$ smanjuje maseni protok.
- Pri kolu s mnogo lopatica $\dot m$ je konstantan, pa sila linearno opada s $(c_1 - u)$. Optimum je viši ($u_{opt} = c_1/2$) — klasičan rezultat za Peltonove turbine.

U oba slučaja idealni izlazni kut $\beta_2=180^\circ$ daje faktor $(1-\cos\beta_2)=2$. Ako geometrija, primjerice, ograniči skretanje na $\beta_2=165^\circ$, faktor pada na $(1-\cos165^\circ)\approx1{,}97$, odnosno za oko $1{,}7\,\%$ prema tom idealnom kutnom faktoru. To nije ukupni gubitak turbine: brzinski, volumetrijski i mehanički gubitci procjenjuju se zasebno.
:::

Kad je zanimljiv mehanički izlaz stroja, ključna više nije bilo koja komponenta sile nego tangencijalna komponenta, jer upravo ona radi na brzini oboda:

$$
P = F_t u = M\omega
$$ {#eq-turbostrojevi-matematicki-izvod-optimum-obodne-brzine-za-jednu-09}

::: {.mf1-fizikalno-znacenje}
<p class="mf1-box-label">Fizikalno značenje</p>
Snaga $P = F_t u$ kaže da rotor prima rad samo od tangencijalne sile, a ta sila postoji jedino ako fluid mijenja tangencijalnu komponentu brzine. Radijalna promjena brzine mijenja opterećenje ležajeva, ali ne i snagu. Aksijalna promjena (usisni-tlačni stupanj) mijenja aksijalne sile, ali tangencijalna komponenta je jedina koja „gura" rotor u smjeru vrtnje. Zato je svaki kut lopatice — ulazni i izlazni — izravno uvjet za korisni učinak, ne samo geometrijska detalj.
:::

Kad se ulaz i izlaz rotora čitaju na različitim radijusima $r_1$ i $r_2$, više nije dovoljno gledati silu — treba krenuti od **momenta količine gibanja**, što vodi na klasičnu Eulerovu turbinsku jednadžbu.

::: {.mf1-izvod}
<p class="mf1-box-label">Matematički izvod — Eulerova turbinska jednadžba iz momenta količine gibanja</p>

Polazi se od integralnog oblika momenta količine gibanja za stacionarni kontrolni volumen koji obuhvaća rotor. Pozitivan moment u sljedećem zapisu znači moment **rotora na fluid**. Pri svođenju ukupnoga vanjskog momenta na moment rotora pretpostavlja se da momenti tlaka i volumnih sila oko osi nemaju doprinos, odnosno da su zasebno uračunani:

$$
\sum \vec M = \int_{KP} \rho\,(\vec r \times \vec c)\,(\vec c\cdot\vec n)\,dA,
$$ {#eq-turbostrojevi-matematicki-izvod-eulerova-turbinska-jednadzba-i-01}

gdje je $\vec r$ vektor položaja točke na kontrolnoj plohi od osi rotacije, a $\vec c$ apsolutna brzina fluida u toj točki.

Za rotor s jednim ulaznim presjekom na polumjeru $r_1$ i jednim izlaznim presjekom na polumjeru $r_2$, s jednolikom raspodjelom brzine u svakom presjeku, integral se svodi na razliku doprinosa izlaza i ulaza:

$$
\vec M = \dot m\,(\vec r_2 \times \vec c_2) - \dot m\,(\vec r_1 \times \vec c_1).
$$ {#eq-turbostrojevi-matematicki-izvod-eulerova-turbinska-jednadzba-i-02}

Komponenta momenta oko osi vrtnje rotora čita se iz vektorskog produkta: na zadanom radijusu $r$ doprinos momentu daje samo tangencijalna komponenta brzine $c_t$ jer ona jedina ima krak $r$ oko osi (radijalna komponenta prolazi kroz os, a aksijalna je paralelna s osi). Zato je iznos osnog momenta

$$
M_{r\to f} = \dot m\,(r_2 c_{2t} - r_1 c_{1t}).
$$ {#eq-turbostrojevi-matematicki-izvod-eulerova-turbinska-jednadzba-i-03}

Reakcijski moment fluida na rotor ima suprotan predznak, $M_{f\to r}=-M_{r\to f}$. To je jezgra **Eulerove jednadžbe turbostrojarstva** za pumpe, ventilatore, turbine i kompresore.

Množenjem s kutnom brzinom $\omega$ dobivaju se dvije jednako valjane, ali suprotno orijentirane bilance snage:

$$
P_{r\to f}=\dot m\,(u_2c_{2t}-u_1c_{1t}),
\qquad
P_{f\to r}=\dot m\,(u_1c_{1t}-u_2c_{2t}).
$$ {#eq-turbostrojevi-matematicki-izvod-eulerova-turbinska-jednadzba-i-04}

Pozitivan $P_{r\to f}$ opisuje rad koji rotor predaje fluidu, kao u pumpi ili ventilatoru. Pozitivan $P_{f\to r}$ opisuje rad koji fluid predaje rotoru, kao u turbini. Ovdje je $u_i=\omega r_i$. Za Peltonov rotor vrijedi $r_1=r_2=r$ i $u_1=u_2=u$, pa turbinski izlaz postaje

$$
P_{f\to r} = \dot m\,u\,(c_{1t} - c_{2t}),
$$ {#eq-turbostrojevi-matematicki-izvod-eulerova-turbinska-jednadzba-i-05}

što je upravo izraz koji se ranije dobio za sile na pokretnoj lopatici — sad u jeziku komponenti brzine umjesto izlaznog kuta.
:::

Iz Eulerove jednadžbe odmah se vidi da korisni rad ne daje bilo koja komponenta brzine, nego promjena tangencijalne količine gibanja — to je razlog zašto su ulazni i izlazni kutovi lopatica središnji projektni parametri svakoga turbostroja.

::: {.callout-note collapse="true" icon="false"}
## Numerički trag

Moment količine gibanja na rotoru i razdvajanje apsolutne i relativne brzine ($\vec{c} = \vec{w} + \vec{u}$) jezgra je **rotacijskog CFD-a** za pumpe, ventilatore, kompresore i turbine. **MRF metoda** (Multiple Reference Frame) rješava Navier-Stokesa u rotirajućem sustavu — gleda fluid očima lopatice, jednako kao u izvodu u ovom poglavlju — i dodaje Coriolisovu i centrifugalnu silu kao izvorne članove. Za nestacionarne fenomene (interakcija rotor-stator, pulsacije) koristi se **klizajuća mreža (engl. sliding mesh)**: rotorska mreža fizički kliže uz statorsku.
:::

::: {.mf1-interaktivno}
<p class="mf1-box-label">Interaktivni prikaz — Trokuti brzina i snaga na Peltonovoj lopatici</p>

Interaktivni prikaz omogućuje mijenjanje apsolutne brzine mlaza, obodne brzine lopatice i izlaznog kuta uz neposredno praćenje trokuta brzina i krivulje snage. Optimalna obodna brzina i pripadna maksimalna snaga jasno se očituju na grafu.

<div class="mf1-interaktivno-akcija">
<a class="mf1-interaktivno-veza" href="https://martibasic.github.io/MF1_udzbenik/jlite/lab/index.html?path=u12_pelton_lopatica.ipynb">Pokreni u pregledniku</a>
<a class="mf1-interaktivno-veza" href="https://colab.research.google.com/github/martibasic/MF1_udzbenik/blob/main/notebooks/u12_pelton_lopatica.ipynb" target="_blank" rel="noopener">Pričuvno: otvori u Colabu</a>
<img class="mf1-interaktivno-qr" src="../assets/qr/u12_pelton_lopatica.svg" alt="QR kod za interaktivni prikaz Peltonove lopatice"/>
</div>

<div class="mf1-interaktivno-pitanja">
**Pitanja za samostalno istraživanje:** (a) Zašto model rotora s punim sapničkim protokom daje maksimalnu snagu pri $u=c_1/2$ kada su $k$ i $\beta_2$ konstantni? (b) Kakva je teorijska maksimalna snaga pri $\beta_2=180°$ i zašto stvarne lopatice nemaju potpuni povrat mlaza? (c) Pri $u=0$, kolika je snaga predana rotoru iako sila postoji?
</div>
:::

Kod potiska se priča obrće. Ako vozilo ili platforma izbacuje mlaz dok je ulazna brzina okolnog fluida u smjeru potiska mala ili zanemariva, iz jednadžbe količine gibanja slijedi

$$
F_p = \dot m(v_{izl} - v_{ul}) \approx \dot m v = \rho A v^2.
$$ {#eq-turbostrojevi-interaktivni-prikaz-trokuti-brzina-i-snaga-na-01}

Za propelere i rotore koji stoje u mjestu i ubrzavaju okolni fluid (helikopter u visu, dron koji lebdi, brodski propeler pri statičkom potisku) koristi se nešto profinjeniji model — teorija aktuatorskog diska — koja vodi na izvod brzine kroz rotor pri zadanom potisku.

::: {.mf1-izvod}
<p class="mf1-box-label">Matematički izvod — Aktuatorski disk i Froudeov teorem</p>

Promatra se idealizirani rotor (propeler, dron, helikopter) kao tanki disk površine $A$ kroz koji fluid ulazi iz okoline i izlazi ubrzano u mlaznoj traci. Pretpostavlja se stacionarno, jednodimenzijsko, nestlačivo strujanje bez viskoznih gubitaka izvan idealiziranoga tlačnog skoka na disku; opterećenje je jednoliko po disku, nema vrtložne komponente brzine, vršnih ni glavinskih gubitaka, utjecaja tla ni međudjelovanja susjednih rotora. Modelu se postavljaju četiri presjeka:

- presjek $\infty$ (daleko ispred diska): brzina $v_\infty$, atmosferski tlak $p_\infty$;
- presjek tik ispred diska: brzina $v_d$, tlak $p_d^-$;
- presjek tik iza diska: brzina $v_d$ (kontinuitet zahtjeva istu brzinu kroz disk), tlak $p_d^+ > p_d^-$;
- presjek $w$ (u dalekoj traci, gdje se tlak vraća na atmosferski): brzina $v_w$, tlak $p_\infty$.

Maseni protok kroz strujnu cijev je konstantan: $\dot m = \rho A v_d$.

**Zakon količine gibanja** za cijelu strujnu cijev daje potisak

$$
F_p = \dot m\,(v_w - v_\infty) = \rho A v_d (v_w - v_\infty).
$$ {#eq-turbostrojevi-matematicki-izvod-aktuatorski-disk-i-froudeov-te-01}

**Bernoullijeva jednadžba** primijenjena dva puta — ispred diska (od $\infty$ do $d^-$) i iza diska (od $d^+$ do $w$, jer disk je jedino mjesto gdje se predaje energija pa Bernoulli vrijedi posebno u svakoj poludomeni) — daje

$$
p_\infty + \tfrac{1}{2}\rho v_\infty^2 = p_d^- + \tfrac{1}{2}\rho v_d^2,
$$ {#eq-turbostrojevi-matematicki-izvod-aktuatorski-disk-i-froudeov-te-02}

$$
p_d^+ + \tfrac{1}{2}\rho v_d^2 = p_\infty + \tfrac{1}{2}\rho v_w^2.
$$ {#eq-turbostrojevi-matematicki-izvod-aktuatorski-disk-i-froudeov-te-03}

Oduzimanjem prve jednadžbe od druge dobiva se tlačni skok preko diska

$$
\Delta p_d = p_d^+ - p_d^- = \tfrac{1}{2}\rho (v_w^2 - v_\infty^2).
$$ {#eq-turbostrojevi-matematicki-izvod-aktuatorski-disk-i-froudeov-te-04}

Potisak se može alternativno izračunati i kao tlačna sila na disku:

$$
F_p = \Delta p_d \cdot A = \tfrac{1}{2}\rho A (v_w^2 - v_\infty^2).
$$ {#eq-turbostrojevi-matematicki-izvod-aktuatorski-disk-i-froudeov-te-05}

Izjednačavanjem dvaju izraza za $F_p$ (preko količine gibanja i preko tlaka) dobiva se **Froudeov teorem**:

$$
\rho A v_d (v_w - v_\infty) = \tfrac{1}{2}\rho A (v_w - v_\infty)(v_w + v_\infty),
$$ {#eq-turbostrojevi-matematicki-izvod-aktuatorski-disk-i-froudeov-te-06}

odakle nakon kraćenja s $\rho A (v_w - v_\infty)$ slijedi

$$
\boxed{v_d = \tfrac{1}{2}(v_\infty + v_w)},
$$ {#eq-turbostrojevi-matematicki-izvod-aktuatorski-disk-i-froudeov-te-07}

što znači da je brzina kroz disk **aritmetička sredina** brzine ispred diska i u dalekoj traci.

**Lebdeći režim** ($v_\infty = 0$) — dron u visi, helikopter na mjestu, statički test propelera — daje $v_d = v_w/2$, pa potisak postaje

$$
F_p = \rho A v_d \cdot v_w = \rho A v_d \cdot 2 v_d = 2\rho A v_d^2.
$$ {#eq-turbostrojevi-matematicki-izvod-aktuatorski-disk-i-froudeov-te-08}

Iz toga slijedi i izravna formula koja se koristi u praksi:

$$
v_d = \sqrt{\frac{F_p}{2\rho A}}.
$$ {#eq-turbostrojevi-matematicki-izvod-aktuatorski-disk-i-froudeov-te-09}

Ova relacija pokazuje da je inducirana brzina kroz idealni rotor proporcionalna $\sqrt{F_p/A}$. Za isti potisak veća diskovna površina smanjuje induciranu brzinu i idealnu induciranu snagu $P_i=F_pv_d$. To ne jamči veću ukupnu korisnost stvarnog rotora, jer ona ovisi i o profilu lopatice, broju okretaja, vršnim gubitcima, motoru i drugim učincima koje ovaj model ne sadrži.
:::

Isti zakon zato vodi i Peltonov rotor i potisni sustav: u prvom slučaju fluid gubi korisnu tangencijalnu količinu gibanja i stroj prima rad, a u drugom slučaju fluid dobiva izlazni impuls i platforma prima uzgon ili pogon. Nova fizika nije u drugoj formuli, nego u tome tko preuzima reakciju i u kojem se referentnom okviru čita tok.

To je pravi strojarski smisao <span class="mf1-ch-ref"><span class="mf1-ch-code">pog. 14</span><span class="mf1-ch-title">Turbostrojevi i propulzija</span></span>. Na Peltonovu kolu loš odabir obodne brzine odmah smanjuje moment i snagu generatora. Na vodilici ili ispitnoj glavi pogrešno pročitan izlazni vektor znači pogrešnu reakciju nosača. Na propeleru ili vodomlaznome pogonu ista matematika povezuje ubrzanje fluida s potiskom sustava.

## Riješeni primjeri

::: {#ex-u12-vodilica-mlaza-na-ispitnom-stolu-t2 .mf1-we}
<p class="mf1-box-label">Riješeni primjer — Vodilica mlaza na ispitnom stolu&nbsp;<span class="mf1-level">T2</span></p>

**Kontekst:** Na hidrauličkom ispitnom stolu nepomična vodilica skreće pravokutni mlaz vode u horizontalnoj ravnini za određeni kut, pri čemu se brzina zbog gubitaka smanjuje. Iz promjene količine gibanja određuje se reakcijska sila na nosač vodilice, što je tipičan ulazni primjer za analizu sila na lopaticama.

**Zadano**

- Širina pravokutne sapnice: $b = 36\ \text{mm}$
- Visina pravokutne sapnice: $h = 14\ \text{mm}$
- Brzina mlaza na ulazu u vodilicu: $v_1 = 24\ \text{m/s}$
- Kut skretanja u horizontalnoj ravnini: $\beta = 120^\circ$
- Izlazna brzina mlaza (s gubicima): $v_2 = 19\ \text{m/s}$
- Gustoća vode: $\rho = 998\ \text{kg/m}^3$

**Traženo**

1. Odredite maseni protok vode kroz sapnicu.
2. Odredite horizontalne komponente sile koju fluid vrši na vodilicu.
3. Odredite iznos i smjer reakcije koju mora preuzeti nosač vodilice.

![vodilica mlaza na ispitnom stolu](../assets/print/u12_val1_vodilica_mlaza.svg){#fig-u12-vodilica-mlaza-na-ispitnom-stolu fig-alt="vodilica mlaza na ispitnom stolu"}

**Pretpostavke i model**

Promatra se stacionarni kontrolni volumen oko vodilice u horizontalnoj ravnini. Tlak na ulazu i izlazu jednak je atmosferskom, a težina vode unutar vodilice zanemariva je u odnosu na horizontalne sile.

**Rješenje**

Površina pravokutnog izlaza sapnice iznosi

$$
A = bh = 0{,}036 \cdot 0{,}014 = 5{,}04 \cdot 10^{-4}\ \text{m}^2,
$$ {#eq-turbostrojevi-rijeseni-primjer-vodilica-mlaza-na-ispitnom-stol-01}

pa je maseni protok

$$
\dot{m} = \rho A v_1 = 998 \cdot 5{,}04 \cdot 10^{-4} \cdot 24 \approx 12{,}07\ \text{kg/s}.
$$ {#eq-turbostrojevi-rijeseni-primjer-vodilica-mlaza-na-ispitnom-stol-02}

Ulazna brzina je $\vec{v}_1 = (24, 0)\ \text{m/s}$, a izlazna

$$
\vec{v}_2 = (19\cos 120^\circ, 19\sin 120^\circ) = (-9{,}5, 16{,}45)\ \text{m/s}.
$$ {#eq-turbostrojevi-rijeseni-primjer-vodilica-mlaza-na-ispitnom-stol-03}

Sila vodilice na fluid zato glasi

$$
\vec{F}_{v\to f} = \dot{m}(\vec{v}_2 - \vec{v}_1) = (-404{,}4, 198{,}6)\ \text{N},
$$ {#eq-turbostrojevi-rijeseni-primjer-vodilica-mlaza-na-ispitnom-stol-04}

ali zadatak traži silu fluida na vodilicu, pa treba promijeniti predznak:

$$
\vec{F}_{f\to v} = (404{,}4, -198{,}6)\ \text{N} \implies F_x \approx 404\ \text{N},\ F_y \approx -199\ \text{N}.
$$ {#eq-turbostrojevi-rijeseni-primjer-vodilica-mlaza-na-ispitnom-stol-05}

Reakcija nosača mora biti jednaka po iznosu i suprotna po smjeru, $\vec{R} = (-404{,}4, 198{,}6)\ \text{N}$, pa je njezin iznos

$$
R = \sqrt{404{,}4^2 + 198{,}6^2} \approx 450{,}6\ \text{N} \approx 451\ \text{N}.
$$ {#eq-turbostrojevi-rijeseni-primjer-vodilica-mlaza-na-ispitnom-stol-06}

Kut reakcije iznad negativnog smjera osi $x$ iznosi

$$
\alpha = \arctan\left(\frac{198{,}6}{404{,}4}\right) = 26{,}2^\circ.
$$ {#eq-turbostrojevi-rijeseni-primjer-vodilica-mlaza-na-ispitnom-stol-07}

**Provjera i komentar**

1. Maseni protok reda desetak kilograma u sekundi razuman je za ovakav presjek i brzinu mlaza.
2. Komponenta po osi $x$ mora biti dominantna jer ulazna projekcija brzine po toj osi znatno nadmašuje izlaznu.
3. Reakcija reda nekoliko stotina njutna razumna je za mlaz brzine reda dvadesetak metara u sekundi.
:::


::: {#ex-u12-relativni-dotok-na-pokretnu-lopaticu-t1 .mf1-we}
<p class="mf1-box-label">Riješeni primjer — Relativni dotok na pokretnu lopaticu&nbsp;<span class="mf1-level">T1</span></p>

**Kontekst:** Kada se lopatica giba u smjeru mlaza, kroz njezin pokretni kontrolni volumen ulazi samo relativni protok određen razlikom brzina mlaza i lopatice. Ovaj uvodni primjer pokazuje koliko se taj efektivni protok razlikuje od punog sapničkog protoka, što je osnovna postavka za rad svake turbine s djelomično zahvaćenim mlazom.

**Zadano**

- Gustoća vode: $\rho = 998\ \text{kg/m}^3$
- Promjer sapnice: $d = 38\ \text{mm}$
- Apsolutna brzina mlaza na izlazu iz sapnice: $c_1 = 22\ \text{m/s}$
- Brzina lopatice (u istom smjeru): $u = 8\ \text{m/s}$
- Lopatica zahvaća cijeli mlaz.

**Traženo**

1. Odrediti relativnu ulaznu brzinu $w_1$.
2. Odrediti relativni maseni protok $\dot m_{rel}$ kroz pokretni kontrolni volumen.
3. Usporediti taj relativni protok s punim masenim protokom sapnice.

![Pokretna lopatica: c1=22 m/s, u=8 m/s, w1=14 m/s, relativni protok 63,7%](../assets/print/u12_fig_relativni_dotok.svg){#fig-u12-relativni-dotok-lopatica fig-align="center" fig-alt="Pokretna lopatica: c1=22 m/s, u=8 m/s, w1=14 m/s, relativni protok 63,7%"}

**Pretpostavke i model**

Za pokretnu lopaticu ulazni presjek treba čitati u sustavu koji se giba s lopaticom. Zato mlaz ne ulazi relativnom brzinom $c_1$, nego razlikom $w_1 = c_1-u$. Tek taj relativni dotok određuje koliko mase stvarno ulazi u pokretni kontrolni volumen.

**Rješenje**

Površina sapnice iznosi

$$
A = \frac{\pi d^2}{4} = \frac{\pi \cdot 0{,}038^2}{4} = 1{,}134 \cdot 10^{-3}\ \text{m}^2.
$$ {#eq-turbostrojevi-rijeseni-primjer-relativni-dotok-na-pokretnu-lop-01}

Relativna ulazna brzina prema lopatici je

$$
w_1 = c_1-u = 22-8 = 14\ \text{m/s}.
$$ {#eq-turbostrojevi-rijeseni-primjer-relativni-dotok-na-pokretnu-lop-02}

Zato relativni maseni protok iznosi

$$
\dot m_{rel} = \rho A w_1 = 998 \cdot 1{,}134 \cdot 10^{-3} \cdot 14 = 15{,}85\ \text{kg/s}.
$$ {#eq-turbostrojevi-rijeseni-primjer-relativni-dotok-na-pokretnu-lop-03}

Puni maseni protok sapnice bio bi

$$
\dot m = \rho A c_1 = 998 \cdot 1{,}134 \cdot 10^{-3} \cdot 22 = 24{,}90\ \text{kg/s}.
$$ {#eq-turbostrojevi-rijeseni-primjer-relativni-dotok-na-pokretnu-lop-04}

Dakle, kroz pokretni kontrolni volumen stvarno ulazi samo

$$
\frac{\dot m_{rel}}{\dot m} = \frac{15{,}85}{24{,}90} = 0{,}637
$$ {#eq-turbostrojevi-rijeseni-primjer-relativni-dotok-na-pokretnu-lop-05}

odnosno oko $63{,}7\%$ punog sapničkog protoka.

**Provjera i komentar**

1. Ako bi lopatica mirovala, moralo bi biti $w_1 = c_1$.
2. Kako se lopatica giba u istom smjeru kao mlaz, relativni protok mora biti manji od punog sapničkog protoka.
3. Kad bi bilo $u \to c_1$, relativni bi dotok težio nuli.
:::

::: {#ex-u12-pokretna-ravna-lopatica-u-mlazu-t2 .mf1-we}
<p class="mf1-box-label">Riješeni primjer — Pokretna ravna lopatica u mlazu&nbsp;<span class="mf1-level">T2</span></p>

**Kontekst:** Ravna pokretna lopatica koja se giba u smjeru mlaza prima samo dio impulsa fluida i time crpi snagu iz mlaza. Iz relativnog dotoka i promjene apsolutne brzine određuju se sila i snaga koje lopatica predaje nosaču, što je didaktička priprema za rotorne lopatice.

**Zadano**

- Gustoća vode: $\rho = 998\ \text{kg/m}^3$
- Promjer sapnice: $d = 40\ \text{mm}$
- Apsolutna brzina mlaza: $c_1 = 24\ \text{m/s}$
- Brzina lopatice (u istom smjeru kao mlaz): $u = 9\ \text{m/s}$
- Lopatica zahvaća cijeli mlaz; nakon udara voda u apsolutnom sustavu napušta lopaticu s vodoravnom brzinom jednakom $u$; gubici zanemarivi.

**Traženo**

1. maseni protok koji stvarno ulazi u pokretni kontrolni volumen.
2. silu mlaza na lopaticu.
3. snagu koju mlaz predaje lopatici.

![pokretna ravna lopatica](../assets/print/u12_val3_pokretna_lopatica.svg){#fig-u12-pokretna-ravna-lopatica fig-alt="pokretna ravna lopatica"}

**Pretpostavke i model**

Za pokretni element presudan je relativni dotok $c_1-u$. Zato se kroz lopaticu ne vodi puni maseni protok sapnice, nego samo onaj koji u pokretnom sustavu stvarno presiječa kontrolnu površinu. Promjena količine gibanja po osi $x$ zato se zatvara upravo tim relativnim protokom.

**Rješenje**

Površina mlaza iznosi

$$
A = \frac{\pi d^2}{4} = \frac{\pi \cdot 0{,}04^2}{4} = 1{,}257 \cdot 10^{-3}\ \text{m}^2.
$$ {#eq-turbostrojevi-rijeseni-primjer-pokretna-ravna-lopatica-u-mlazu-01}

Relativna ulazna brzina prema lopatici je $c_r = c_1-u = 24-9 = 15\ \text{m/s}$, pa je maseni protok koji stvarno ulazi u pokretni kontrolni volumen

$$
\dot{m}_{rel} = \rho A c_r = 998 \cdot 1{,}257 \cdot 10^{-3} \cdot 15 \approx 18{,}82\ \text{kg/s}.
$$ {#eq-turbostrojevi-rijeseni-primjer-pokretna-ravna-lopatica-u-mlazu-02}

Kako voda nakon udara u apsolutnom sustavu odlazi s vodoravnom brzinom $u$, promjena vodoravne komponente brzine iznosi $c_1-u = 15\ \text{m/s}$, pa sila lopatice na fluid glasi

$$
F_{l\to f} = \dot{m}_{rel}(u-c_1) = 18{,}82 \cdot (9-24) = -282{,}3\ \text{N}.
$$ {#eq-turbostrojevi-rijeseni-primjer-pokretna-ravna-lopatica-u-mlazu-03}

Zato fluid na lopaticu djeluje silom suprotnog smjera, pa je traženi iznos sile $F = 282{,}3\ \text{N} \approx 282\ \text{N}$. Snaga predana lopatici iznosi

$$
P = Fu = 282{,}3 \cdot 9 \approx 2541\ \text{W} = 2{,}54\ \text{kW}.
$$ {#eq-turbostrojevi-rijeseni-primjer-pokretna-ravna-lopatica-u-mlazu-04}

**Provjera i komentar**

1. Ako bi lopatica mirovala, sila bi morala biti veća nego u ovom slučaju jer bi relativni dotok bio veći.
2. Ako bi se lopatica gibala brzinom jednakom brzini mlaza, relativni dotok pao bi na nulu i nestala bi i sila.
3. Snaga mora biti reda nekoliko kilovata jer se sila reda nekoliko stotina njutna prenosi na brzinu reda deset metara u sekundi.
:::

::: {#ex-u12-pokretna-zakrivljena-lopatica-s-relativnim-izlazom-t3 .mf1-ch}
<p class="mf1-box-label">Cjeloviti zadatak — Pokretna zakrivljena lopatica s relativnim izlazom&nbsp;<span class="mf1-level">T3</span></p>

**Kontekst:** Zakrivljena lopatica koja se giba u smjeru mlaza skreće relativni tok pod određenim kutom, a izlazna relativna brzina je manja od ulazne zbog gubitaka u kanalu lopatice. Iz vektorskog zbrajanja relativnih i transportnih brzina određuju se sila i snaga koje fluid predaje lopatici, što je radni model jedne lopatice rotorskog stroja.

**Zadano**

- Gustoća vode: $\rho = 998\ \text{kg/m}^3$
- Promjer sapnice: $d = 45\ \text{mm}$
- Apsolutna brzina mlaza iz sapnice: $c_1 = 26\ \text{m/s}$
- Brzina lopatice u smjeru mlaza: $u = 10\ \text{m/s}$
- Koeficijent relativnog izlaza: $w_2 = k w_1$, $k = 0{,}90$
- Kut relativnog izlaza iznad negativnog smjera osi $x$: $\beta = 30^\circ$

Pretpostavi da lopatica zahvaća cijeli mlaz, da je tok stacionaran u pokretnom sustavu i da su tlakovi na ulazu i izlazu jednaki atmosferskom.

**Traženo**

1. maseni protok koji stvarno ulazi u pokretni kontrolni volumen $\dot{m}_{rel}$.
2. apsolutni vektor izlazne brzine $\vec{c}_2$.
3. komponente i iznos sile mlaza na lopaticu.
4. snagu koju mlaz predaje lopatici.

![pokretna zakrivljena lopatica](../assets/print/u12_ch1_pokretna_zakrivljena_lopatica.svg){#fig-u12-pokretna-zakrivljena-lopatica fig-alt="pokretna zakrivljena lopatica"}

**Pretpostavke i model**

Pokretni kontrolni volumen vezan je uz lopaticu, pa kroz njega ne prolazi puni sapnicki protok nego samo relativni dotok definiran razlikom $c_1-u$. Iz relativnog izlaza najprije se odredi apsolutni izlazni vektor, a tek zatim jednadžba količine gibanja daje silu na lopaticu. Snaga se na kraju zatvara samo preko komponente sile u smjeru gibanja lopatice.

**Rješenje**

Površina mlaza iznosi

$$
A = \frac{\pi d^2}{4} = \frac{\pi \cdot 0{,}045^2}{4} = 1{,}590 \cdot 10^{-3}\ \text{m}^2.
$$ {#eq-turbostrojevi-cjeloviti-zadatak-pokretna-zakrivljena-lopatica-01}

Relativna ulazna brzina prema lopatici je $w_1 = c_1-u = 26-10 = 16\ \text{m/s}$, pa je maseni protok koji stvarno ulazi u pokretni kontrolni volumen

$$
\dot{m}_{rel} = \rho A w_1 = 998 \cdot 1{,}590 \cdot 10^{-3} \cdot 16 = 25{,}4\ \text{kg/s}.
$$ {#eq-turbostrojevi-cjeloviti-zadatak-pokretna-zakrivljena-lopatica-02}

Iz koeficijenta relativnog izlaza slijedi $w_2 = k w_1 = 0{,}90 \cdot 16 = 14{,}4\ \text{m/s}$. Relativni izlazni vektor glasi

$$
\vec{w}_2 = (-w_2 \cos \beta,\ w_2 \sin \beta) = (-14{,}4 \cos 30^\circ,\ 14{,}4 \sin 30^\circ) = (-12{,}47,\ 7{,}20)\ \text{m/s}.
$$ {#eq-turbostrojevi-cjeloviti-zadatak-pokretna-zakrivljena-lopatica-03}

Apsolutna izlazna brzina dobiva se dodavanjem transportne brzine lopatice:

$$
\vec{c}_2 = (u,0) + \vec{w}_2 = (10-12{,}47,\ 7{,}20) = (-2{,}47,\ 7{,}20)\ \text{m/s}.
$$ {#eq-turbostrojevi-cjeloviti-zadatak-pokretna-zakrivljena-lopatica-04}

Ulazna apsolutna brzina je $\vec{c}_1 = (26,0)\ \text{m/s}$. Sila lopatice na fluid glasi

$$
\vec{F}_{l \to f} = \dot{m}_{rel}(\vec{c}_2 - \vec{c}_1) = 25{,}4 \cdot (-28{,}47,\ 7{,}20) = (-723{,}3,\ 182{,}9)\ \text{N}.
$$ {#eq-turbostrojevi-cjeloviti-zadatak-pokretna-zakrivljena-lopatica-05}

Zato fluid na lopaticu djeluje silom suprotnog smjera $\vec{F}_{f \to l} = (723{,}3,\ -182{,}9)\ \text{N}$, pa su komponente sile $F_x \approx 723\ \text{N}$, $F_y \approx -183\ \text{N}$, a rezultantni iznos

$$
F = \sqrt{723{,}3^2 + 182{,}9^2} = 746\ \text{N}.
$$ {#eq-turbostrojevi-cjeloviti-zadatak-pokretna-zakrivljena-lopatica-06}

Snagu predanu lopatici daje samo komponenta sile u smjeru gibanja:

$$
P = F_x u = 723{,}3 \cdot 10 = 7233\ \text{W} \approx 7{,}23\ \text{kW}.
$$ {#eq-turbostrojevi-cjeloviti-zadatak-pokretna-zakrivljena-lopatica-07}

**Provjera i komentar**

Ovaj cjeloviti zadatak zatvara puni prijelaz kroz <span class="mf1-ch-ref"><span class="mf1-ch-code">pog. 14</span><span class="mf1-ch-title">Turbostrojevi i propulzija</span></span>: relativni dotok daje $\dot{m}_{rel} \approx 25{,}4\ \text{kg/s}$, relativni izlaz mora se prevesti u apsolutni vektor $\vec{c}_2 \approx (-2{,}47,\ 7{,}20)\ \text{m/s}$, a tek tada se dobiva sila mlaza na lopaticu od oko $(723, -183)\ \text{N}$. Budući da rad proizvodi samo komponenta sile u smjeru gibanja, lopatica prima snagu od oko $7{,}23\ \text{kW}$.

1. Maseni protok kroz pokretni kontrolni volumen mora biti manji od punog sapničkog protoka jer je $w_1 = c_1-u < c_1$.
2. Komponenta $F_x$ mora ostati dominantna jer upravo promjena tangencijalne brzine proizvodi rad i snagu.
3. Kad bi se lopatica gibala brzinom jednakom brzini mlaza, relativni dotok bi nestao, pa bi nestale i sila i snaga.
:::

::: {#ex-u12-peltonov-rotor-s-jednim-mlazom-i-momentom .mf1-ch}
<p class="mf1-box-label">Cjeloviti zadatak — Reprezentativna Peltonova lopatica i trenutačni moment&nbsp;<span class="mf1-level">T4</span></p>

**Kontekst:** Jedna reprezentativna Peltonova lopatica prolazi kroz mlaz pri zadanoj obodnoj brzini. Iz tangencijalne komponente sile izvode se njezin trenutačni doprinos momentu i snazi. Budući da se koristi maseni protok kroz kontrolni volumen vezan uz jednu lopaticu, rezultat nije kontinuirana snaga cijeloga višelopatičnog rotora.

**Zadano**

- Gustoća vode: $\rho = 998\ \text{kg/m}^3$
- Promjer sapnice: $d = 44\ \text{mm}$
- Apsolutna brzina mlaza iz sapnice: $c_1 = 31\ \text{m/s}$
- Srednji polumjer rotora: $r = 0{,}46\ \text{m}$
- Stalna brzina vrtnje rotora: $n = 320\ \text{min}^{-1}$
- Koeficijent relativnog izlaza: $w_2 = k w_1$, $k = 0{,}90$
- Kut relativnog izlaza iznad negativnog smjera osi $x$: $\beta = 20^\circ$
- Tražena snaga pomoćnog generatora: $P_G = 9{,}5\ \text{kW}$

Smjer osi $x$ odabran je tangencijalno u smjeru gibanja oboda. Pretpostavi da lopatica potpuno zahvaća mlaz te da su ulaz i izlaz na atmosferskom tlaku.

**Traženo**

1. obodnu brzinu rotora $u$ i relativnu ulaznu brzinu $w_1$.
2. maseni protok kroz pokretni kontrolni volumen $\dot{m}_{rel}$ i apsolutni izlazni vektor $\vec{c}_2$.
3. komponente i iznos sile fluida na lopaticu.
4. moment na obodu rotora i snagu koju mlaz predaje rotoru.
5. usporediti trenutačnu idealiziranu snagu lopatice s traženom snagom generatora i objasniti zašto ta usporedba sama ne dokazuje pogonsku dostatnost rotora.

![Peltonov rotor s jednim mlazom](../assets/print/u12_ch2_pelton_rotor_moment.svg){#fig-u12-peltonov-rotor-s-jednim-mlazom fig-alt="Peltonov rotor s jednim mlazom"}

**Pretpostavke i model**

Promatra se pokretni kontrolni volumen vezan uz jednu reprezentativnu lopaticu na obodu rotora. U taj kontrolni volumen ulazi samo relativni dotok definiran brzinom $w_1 = c_1-u$. Iz relativnog izlaza najprije treba vratiti apsolutni izlazni vektor, zatim iz promjene količine gibanja odrediti tangencijalnu silu, a tek na kraju iz te sile zatvoriti moment i snagu na radijusu $r$.

**Rješenje**

Površina mlaza iznosi

$$
A = \frac{\pi d^2}{4} = \frac{\pi \cdot 0{,}044^2}{4} = 1{,}521 \cdot 10^{-3}\ \text{m}^2.
$$ {#eq-turbostrojevi-cjeloviti-zadatak-reprezentativna-peltonova-lopa-01}

Kutna brzina rotora je

$$
\omega = \frac{2\pi n}{60} = \frac{2\pi \cdot 320}{60} = 33{,}51\ \text{rad/s},
$$ {#eq-turbostrojevi-cjeloviti-zadatak-reprezentativna-peltonova-lopa-02}

pa je obodna brzina $u = \omega r = 33{,}51 \cdot 0{,}46 = 15{,}41\ \text{m/s}$. Relativna ulazna brzina prema lopatici sada je $w_1 = c_1-u = 31 - 15{,}41 = 15{,}59\ \text{m/s}$. Maseni protok koji stvarno ulazi u pokretni kontrolni volumen zato je

$$
\dot{m}_{rel} = \rho A w_1 = 998 \cdot 1{,}521 \cdot 10^{-3} \cdot 15{,}59 = 23{,}65\ \text{kg/s}.
$$ {#eq-turbostrojevi-cjeloviti-zadatak-reprezentativna-peltonova-lopa-03}

Iz koeficijenta relativnog izlaza slijedi $w_2 = k w_1 = 0{,}90 \cdot 15{,}59 = 14{,}03\ \text{m/s}$. Relativni izlazni vektor glasi

$$
\vec{w}_2 = (-w_2 \cos \beta,\ w_2 \sin \beta) = (-14{,}03 \cos 20^\circ,\ 14{,}03 \sin 20^\circ) = (-13{,}18,\ 4{,}80)\ \text{m/s}.
$$ {#eq-turbostrojevi-cjeloviti-zadatak-reprezentativna-peltonova-lopa-04}

Apsolutni izlazni vektor dobiva se dodavanjem transportne brzine oboda:

$$
\vec{c}_2 = (u,0) + \vec{w}_2 = (15{,}41-13{,}18,\ 4{,}80) = (2{,}23,\ 4{,}80)\ \text{m/s}.
$$ {#eq-turbostrojevi-cjeloviti-zadatak-reprezentativna-peltonova-lopa-05}

Ulazna apsolutna brzina je $\vec{c}_1 = (31,0)\ \text{m/s}$. Sila lopatice na fluid sada glasi

$$
\vec{F}_{l \to f} = \dot{m}_{rel}(\vec{c}_2 - \vec{c}_1) = 23{,}65 \cdot (-28{,}77,\ 4{,}80) = (-680{,}4,\ 113{,}5)\ \text{N}.
$$ {#eq-turbostrojevi-cjeloviti-zadatak-reprezentativna-peltonova-lopa-06}

Zato fluid na lopaticu djeluje silom suprotnog smjera $\vec{F}_{f \to l} = (680{,}4,\ -113{,}5)\ \text{N}$, pa su tražene komponente $F_x \approx 680\ \text{N}$, $F_y \approx -114\ \text{N}$, a rezultantni iznos sile je

$$
F = \sqrt{680{,}4^2 + 113{,}5^2} = 689{,}8\ \text{N}.
$$ {#eq-turbostrojevi-cjeloviti-zadatak-reprezentativna-peltonova-lopa-07}

Tangencijalna komponenta $F_x$ stvara moment na obodu rotora:

$$
M = F_x r = 680{,}4 \cdot 0{,}46 = 312{,}98\ \text{N m} \approx 313\ \text{N m}.
$$ {#eq-turbostrojevi-cjeloviti-zadatak-reprezentativna-peltonova-lopa-08}

Snaga koju mlaz predaje rotoru iznosi

$$
P = M\omega = 312{,}98 \cdot 33{,}51 = 10{,}49\ \text{kW},
$$ {#eq-turbostrojevi-cjeloviti-zadatak-reprezentativna-peltonova-lopa-09}

što je ekvivalentno i zapisu $P=F_xu=680{,}4\cdot15{,}41=10{,}49\ \text{kW}$. Trenutačna idealizirana vrijednost veća je od $9{,}50\ \text{kW}$ za $0{,}99\ \text{kW}$, ali iz toga se ne smije zaključiti da cijeli rotor može trajno pogoniti takav generator. Model koristi relativni dotok $\rho A(c_1-u)$ jedne pokretne lopatice; kontinuirani Peltonov rotor zahvaća puni sapnički protok slijedom lopatica i traži zasebnu bilancu cijeloga kola te hidrauličke, mehaničke i generatorske gubitke.

**Provjera i komentar**

Ovaj `T4` zadatak zatvara račun reprezentativne lopatice u <span class="mf1-ch-ref"><span class="mf1-ch-code">pog. 14</span><span class="mf1-ch-title">Turbostrojevi i propulzija</span></span>: dobivaju se trenutačna tangencijalna sila od oko $680\ \text{N}$, doprinos momentu od oko $313\ \text{N m}$ i idealizirana snaga od oko $10{,}5\ \text{kW}$. Granica modela namjerno je dio odgovora: maseni protok jedne pokretne lopatice ne smije se bez nove postavke proglasiti kontinuiranim protokom cijeloga rotora.

1. Ako se rotor vrti brze, relativni dotok $w_1$ pada, pa pri istom mlazu padaju i sila i predana snaga.
2. Tangencijalna komponenta sile mora biti mnogo veća od normalne jer upravo ona proizvodi moment na osovini.
3. Ako se iz relativnog izlaza izravno pročita moment bez povratka na apsolutni vektor $\vec{c}_2$, gubi se pravi impulsni skok koji rotor stvarno preuzima.
:::

Posljednji primjer mijenja medij i uređaj, ali ne i metodu: Peltonov impulsni rotor zamjenjuje aktuatorski disk, a bilanca količine gibanja povezuje potisak, induciranu brzinu i snagu.

::: {#ex-u12-propeler-dronskog-kvadkoptera-u-stanju-visa-t2 .mf1-we}
<p class="mf1-box-label">Riješeni primjer — Propeler dronskog kvadkoptera u stanju visa &nbsp;<span class="mf1-level">T2</span></p>

**Kontekst:** Kvadkopterski dron za potrebe geodetske izmjere i inspekcije infrastrukture ima četiri istovjetna propelera. U stacionarnom visu (zadržavanju nepomičnog položaja u zraku) propeleri moraju razviti ukupni potisak jednak težini cijelog drona. Pojednostavljeni proračun potiska iz teorije aktuatorskog diska omogućuje procjenu mehaničke snage svakog propelera, što je ključno za određivanje trajanja leta na jednom punjenju baterije.

**Zadano**

- Masa drona s teretom: $m = 2{,}4\ \text{kg}$
- Broj propelera: $4$
- Promjer pojedinog propelera: $D = 280\ \text{mm}$
- Visina leta: $1\,500\ \text{m}$, temperatura zraka $5^\circ\text{C}$
- Gustoća zraka na toj visini: $\rho = 1{,}045\ \text{kg/m}^3$
- Faktor učinka rotora, ovdje definiran kao omjer idealne inducirane i potrebne snage na vratilu: $\eta = 0{,}70$

**Traženo**

1. Potreban potisak po pojedinom propeleru u stacionarnom visu;
2. Srednja brzina protoka zraka kroz propeler prema teoriji aktuatorskog diska;
3. Idealna i stvarna mehanička snaga po propeleru;
4. Ukupna snaga svih četiriju propelera.

**Pretpostavke i model**

Svaki se propeler zamjenjuje idealiziranim aktuatorskim diskom. U stacionarnom visu ulazna brzina daleko ispred propelera iznosi nula, a daleko iza njega dvostruka je srednja brzina kroz disk. Zrak se smatra nestlačivim, opterećenje diska jednolikim, a međudjelovanje četiriju mlaznih traka i utjecaj trupa zanemaruju se. Odstupanje stvarnog rotora od idealne inducirane snage sažeto je faktorom $\eta$; gubitci motora, regulatora i baterije nisu uključeni. Težina drona uravnotežena je ukupnim potiskom.

**Rješenje**

Iz ravnoteže sila u visu, potisak po pojedinom propeleru:

$$
F_p = \frac{m\,g}{4} = \frac{2{,}4 \cdot 9{,}81}{4} \approx 5{,}886\ \text{N}.
$$ {#eq-turbostrojevi-rijeseni-primjer-propeler-dronskog-kvadkoptera-u-01}

Površina diska pojedinog propelera:

$$
A = \frac{\pi D^2}{4} = \frac{\pi \cdot 0{,}280^2}{4} \approx 6{,}158 \cdot 10^{-2}\ \text{m}^2.
$$ {#eq-turbostrojevi-rijeseni-primjer-propeler-dronskog-kvadkoptera-u-02}

Prema teoriji aktuatorskog diska, srednja brzina protoka zraka kroz disk u stacionarnom visu iznosi:

$$
v = \sqrt{\frac{F_p}{2\rho A}} = \sqrt{\frac{5{,}886}{2 \cdot 1{,}045 \cdot 6{,}158 \cdot 10^{-2}}}.
$$ {#eq-turbostrojevi-rijeseni-primjer-propeler-dronskog-kvadkoptera-u-03}

Računaju se redom $2\rho A \approx 0{,}1287$ i $5{,}886 / 0{,}1287 \approx 45{,}73$:

$$
v = \sqrt{45{,}73} \approx 6{,}76\ \text{m/s}.
$$ {#eq-turbostrojevi-rijeseni-primjer-propeler-dronskog-kvadkoptera-u-04}

Idealna mehanička snaga koju propeler predaje zraku:

$$
P_{id} = F_p \cdot v = 5{,}886 \cdot 6{,}76 \approx 39{,}8\ \text{W}.
$$ {#eq-turbostrojevi-rijeseni-primjer-propeler-dronskog-kvadkoptera-u-05}

Potrebna mehanička snaga na vratilu uz zadani faktor učinka:

$$
P_{st} = \frac{P_{id}}{\eta} = \frac{39{,}8}{0{,}70} \approx 56{,}9\ \text{W}.
$$ {#eq-turbostrojevi-rijeseni-primjer-propeler-dronskog-kvadkoptera-u-06}

Ukupna snaga svih četiriju propelera:

$$
P_{uk} = 4 \cdot P_{st} \approx 227\ \text{W}.
$$ {#eq-turbostrojevi-rijeseni-primjer-propeler-dronskog-kvadkoptera-u-07}

**Provjera i komentar**

Dobivenih $6{,}76\ \text{m/s}$ idealna je inducirana brzina kroz disk za zadano opterećenje. Veći disk pri istom potisku smanjio bi induciranu brzinu i idealnu snagu, ali stvarni izbor propelera mora uključiti i profilne, vršne i pogonske gubitke. Baterija kapaciteta $5\,000\ \text{mAh}$ pri $14{,}8\ \text{V}$ nominalno sadrži $74\ \text{Wh}$, pa bi gornja procjena samo iz dobivenih $227\ \text{W}$ bila

$$
t=\frac{74\ \text{Wh}}{227\ \text{W}}\approx0{,}326\ \text{h}\approx19{,}6\ \text{min}.
$$ {#eq-turbostrojevi-rijeseni-primjer-propeler-dronskog-kvadkoptera-u-08}

To nije predviđanje stvarnog trajanja leta: treba uračunati iskoristivu, ne nominalnu energiju baterije, učinkovitost motora i regulatora, pomoćne potrošače, manevarsku rezervu te međudjelovanje rotora i trupa. Manja gustoća zraka povećava idealnu induciranu snagu za isti potisak i diskovnu površinu, ali njezin učinak na stvarno trajanje također ovisi o radnoj točki cijelog pogona.
:::

::: {.mf1-samoprovjera}
<p class="mf1-box-label">Provjeri sebe</p>

Sljedeća pitanja služe za samostalnu provjeru razumijevanja prije prelaska na zadatke za vježbu.

1. Po čemu se razlikuju apsolutna, relativna i obodna brzina u problemu pokretne lopatice?

::: {.callout-note collapse="true"}
### Odgovor
Apsolutna brzina $\vec{c}$ promatra se u nepomičnom (zemaljskom) okviru. Obodna brzina $\vec{u}$ je brzina same lopatice u istom okviru. Relativna brzina $\vec{w} = \vec{c} - \vec{u}$ je brzina fluida u okviru koji se giba s lopaticom. Maseni protok kroz lopaticu računa se iz relativne brzine, a promjena količine gibanja u apsolutnim brzinama.
:::

2. Zašto se maksimalna snaga na Peltonovoj lopatici postiže pri obodnoj brzini koja je polovica apsolutne brzine mlaza?

::: {.callout-note collapse="true"}
### Odgovor
Iz izraza za snagu $P = \rho Q (c_1 - u) u (1 - \cos\beta_2)$ slijedi da derivacija po $u$ pada na nulu pri $u = c_1/2$. Pri toj vrijednosti umnožak $(c_1-u)u$ je maksimalan, pa je i snaga maksimalna. Pri $u = 0$ ili $u = c_1$ snaga je nula.
:::

3. Što se događa s mlazom iza Peltonove lopatice pri optimalnoj obodnoj brzini i idealnom izlaznom kutu od $180^\circ$?

::: {.callout-note collapse="true"}
### Odgovor
Uz dodatne idealizacije $k=1$, $u=c_1/2$ i $\beta_2=180^\circ$, apsolutna izlazna brzina mlaza teoretski je nula. Ako se samo kut promijeni na $165^\circ$, kutni faktor postaje $(1-\cos165^\circ)/2\approx0{,}983$, odnosno oko $98{,}3\,\%$ idealne vrijednosti. Ostali hidraulički i mehanički gubitci odvojeno smanjuju stvarni korisni rad.
:::

4. Vrijedi li isti pristup (trokut brzina, relativna brzina) i kod aksijalnih lopatica vjetroagregata ili samo kod hidroturbina?

::: {.callout-note collapse="true"}
### Odgovor
Vrijedi za rotirajuće lopatične strojeve u kojima fluid mijenja smjer ili iznos brzine u relativnom okviru lopatice. Vjetroagregati, hidroturbine, ventilatori, kompresori i propeleri koriste analognu kinematiku trokuta brzina; razlikuju se radnim medijem, smjerom prijenosa energije i oblikom lopatica.
:::
:::

## Zadaci za vježbu

::::: {.mf1-vjezbe-list}
1. [**T1**]{#task-u12-vodeni-mlaz-brzine-izlazi-iz-kruzne-sapnice} Vodeni mlaz brzine $v = 24\ \text{m/s}$ izlazi iz kružne sapnice promjera $d = 22\ \text{mm}$ i udara okomito na nepomičnu ravnu ploču. Odredi silu na ploču.

   :::: {.content-visible .mf1-hint-online when-format="html"}
   ::: {.callout-note collapse="true" data-hint-key="true"}
   ### Naputak
   $\dot m = \rho Av$, a za potpuno kočenje komponente brzine na ploči vrijedi $F = \dot m v$.
   :::
   ::::
   :::: {.content-visible .mf1-answer-online when-format="html"}
   ::: {.callout-tip collapse="true" data-answer-key="true"}
   ### Kontrolni rezultat

   $\dot m \approx 9{,}1\ \text{kg/s}$; $F \approx 219\ \text{N}$.
   :::
   ::::
   **Skica:** da - sapnica, ravna ploča i os mlaza sa silom reakcije.

2. [**T1**]{#task-u12-vodeni-mlaz-brzine-izlazi-iz-pravokutne-sapnice} Vodeni mlaz brzine $v = 26\ \text{m/s}$ izlazi iz pravokutne sapnice širine $b = 30\ \text{mm}$ i visine $h = 16\ \text{mm}$ te udara u nepomičnu vodilicu koja tok zakreće za $110^\circ$ bez promjene iznosa brzine. Odredi komponente sile fluida na vodilicu i iznos reakcije nosača.

   :::: {.content-visible .mf1-hint-online when-format="html"}
   ::: {.callout-note collapse="true" data-hint-key="true"}
   ### Naputak
   iz presjeka dobij $\dot m$, a zatim razliku ulazne i izlazne komponente brzine u x i y smjeru.
   :::
   ::::
   :::: {.content-visible .mf1-answer-online when-format="html"}
   ::: {.callout-tip collapse="true" data-answer-key="true"}
   ### Kontrolni rezultat

   $\dot m \approx 12{,}5\ \text{kg/s}$; $F_x \approx 435\ \text{N}$, $F_y \approx -304\ \text{N}$; reakcija nosača $\approx 531\ \text{N}$.
   :::
   ::::
   **Skica:** da - zakrenuta nepomična vodilica, ulazni i izlazni vektor brzine.

3. [**T2**]{#task-u12-na-pokretnu-lopaticu-dolazi-mlaz-vode-apsolutnom} Na pokretnu lopaticu dolazi mlaz vode apsolutnom brzinom $v_1 = 32\ \text{m/s}$, dok se lopatica giba brzinom $u = 12\ \text{m/s}$ u smjeru mlaza. Pretpostavi da je relativna izlazna brzina po iznosu jednaka ulaznoj i zakrenuta za $150^\circ$ u odnosu na ulazni relativni smjer. Ako je maseni protok $\dot{m} = 18\ \text{kg/s}$, odredi tangencijalnu silu na lopaticu i snagu koju mlaz predaje lopatici.

   :::: {.content-visible .mf1-hint-online when-format="html"}
   ::: {.callout-note collapse="true" data-hint-key="true"}
   ### Naputak
   prijeđi na relativne brzine, zatim vrati apsolutnu izlaznu brzinu i iz tangencijalne promjene količine gibanja dobij silu; snaga je $P = Fu$.
   :::
   ::::
   :::: {.content-visible .mf1-answer-online when-format="html"}
   ::: {.callout-tip collapse="true" data-answer-key="true"}
   ### Kontrolni rezultat

   $w_1 = 20\ \text{m/s}$; $F_t \approx 672\ \text{N}$; $P \approx 8{,}06\ \text{kW}$.
   :::
   ::::
   **Skica:** da - pokretna lopatica, brzina lopatice $u$, ulazni i izlazni trokut brzina.

4. [**T2**]{#task-u12-peltonova-lopatica-na-rotoru-radijusa-prima-mlaz} Peltonova lopatica na rotoru radijusa $R = 0{,}42\ \text{m}$ prima mlaz vode masenog protoka $\dot m = 24\ \text{kg/s}$. Tangencijalna komponenta apsolutne brzine na ulazu iznosi $v_{u1} = 28\ \text{m/s}$, a na izlazu $v_{u2} = 6\ \text{m/s}$. Odredi tangencijalnu silu na lopaticu i moment na vratilu.

   :::: {.content-visible .mf1-hint-online when-format="html"}
   ::: {.callout-note collapse="true" data-hint-key="true"}
   ### Naputak
   tangencijalna sila slijedi iz $F_t = \dot m (v_{u1} - v_{u2})$, a moment je $M = F_t R$.
   :::
   ::::
   :::: {.content-visible .mf1-answer-online when-format="html"}
   ::: {.callout-tip collapse="true" data-answer-key="true"}
   ### Kontrolni rezultat

   $F_t = 528\ \text{N}$; $M \approx 222\ \text{N·m}$.
   :::
   ::::
   **Skica:** da - rotor, polumjer $R$, mlaz i tangencijalne komponente brzine na ulazu i izlazu.

5. [**T3**]{#task-u12-potisni-modul-ima-tri-jednake-sapnice-promjera} Potisni modul ima tri jednake sapnice promjera $d = 30\ \text{mm}$. Iz svake sapnice voda izlazi brzinom $v = 42\ \text{m/s}$ u suprotnom smjeru od gibanja platforme. Odredi ukupni potisak modula i hidrauličku snagu mlaza ako je gustoća vode $\rho = 998\ \text{kg/m}^3$.

   :::: {.content-visible .mf1-hint-online when-format="html"}
   ::: {.callout-note collapse="true" data-hint-key="true"}
   ### Naputak
   za jednu sapnicu vrijedi $F = \dot m v$ i $P = \dot m v^2/2$; ukupni rezultat je trostruki zbroj.
   :::
   ::::
   :::: {.content-visible .mf1-answer-online when-format="html"}
   ::: {.callout-tip collapse="true" data-answer-key="true"}
   ### Kontrolni rezultat

   ukupni potisak $\approx 3{,}73\ \text{kN}$; hidraulička snaga $\approx 78{,}4\ \text{kW}$.
   :::
   ::::
   **Skica:** da - platforma s tri sapnice, smjer mlaza i rezultantni potisak.

6. [**T4**]{#task-u12-mlazna-platforma-ukupne-mase-ima-cetiri-jednake} Mlazna platforma ukupne mase $m = 110\ \text{kg}$ ima četiri jednake sapnice promjera $d = 28\ \text{mm}$. Voda gustoće $\rho=998\ \text{kg/m}^3$ iz svake sapnice izlazi okomito prema dolje brzinom $v = 36\ \text{m/s}$. Odredi ukupni potisak, najveću ukupnu masu koju takav sustav može držati u lebdenju i vertikalno ubrzanje platforme pri zadanoj masi sustava. Stvarni promjer svake sapnice može biti $0{,}3\ \text{mm}$ manji od nazivnoga, a regulirana brzina mlaza do $1{,}5\ \text{m/s}$ manja od zadane. Ako zadani statički kriterij traži najmanje $10\ \%$ rezerve potiska iznad težine, odredi najveću masu koja ga zadovoljava i objasni zašto se ta vrijednost ne smije nazvati certificiranom nosivošću platforme.

   :::: {.content-visible .mf1-hint-online when-format="html"}
   ::: {.callout-note collapse="true" data-hint-key="true"}
   ### Naputak
   najprije zbroji izlazne površine svih sapnica; zatim koristi $F_p = \rho A v^2$, uvjet lebdenja $F_p = mg$ i za zadanu masu Newtonov zakon $a = (F_p - mg)/m$. Za masu prema zadanom kriteriju izračunaj najmanji potisak s $d_{min}$ i $v_{min}$ te postavi $F_{p,min}=1{,}10\,m_{krit}g$.
   :::
   ::::
   :::: {.content-visible .mf1-answer-online when-format="html"}
   ::: {.callout-tip collapse="true" data-answer-key="true"}
   ### Kontrolni rezultat

   $F_p \approx 3{,}19\ \text{kN}$; najveća masa lebdenja $\approx 325\ \text{kg}$; pri $m = 110\ \text{kg}$ ubrzanje $a \approx 19{,}2\ \text{m/s}^2$. Za $d_{min}=27{,}7\ \text{mm}$ i $v_{min}=34{,}5\ \text{m/s}$ najmanji je potisak približno $2{,}86\ \text{kN}$, pa zadani kriterij daje $m_{krit}\approx265\ \text{kg}$. To je rezultat idealiziranoga statičkog modela, ne certificirana nosivost; nedostaju dinamika, stabilnost, konstrukcija, upravljanje i mjerodavni propisi.
   :::
   ::::
   **Skica:** da - platforma s četiri sapnice, smjerovi mlazova, ukupni potisak i težina sustava.
:::::

![Skice uz zadatke za vježbu — ploče, pokretne lopatice i sapnice.](../assets/print/u12_vjezbe_skice.svg){#fig-u12-vjezbe fig-align="center" fig-alt="Skice uz zadatke za vježbu — ploče, pokretne lopatice i sapnice."}

::: {.mf1-zavrsni-okvir}
<p class="mf1-box-label">Za ponijeti iz poglavlja</p>

**Sažeta provjera prije računa**

- Treba najprije nacrtati kontrolni volumen i osi prije pisanja jednadžbi.
- Treba jasno razlikovati koju silu daje jednadžba količine gibanja: silu okoline na fluid ili obrat.
- Treba rastaviti izlaznu brzinu na komponente u istom koordinatnom sustavu kao ulaznu.
- Treba provjeriti koristi li se maseni protok iz stvarne izlazne površine i zadane ulazne brzine.
- Treba razdvojiti silu fluida na vodilicu od reakcije nosača.

**Najčešća pogreška**

Najčešća greška nije u masenom protoku, nego u tome što se bez promjene predznaka uzme sila vodilice na fluid kao konačan odgovor. Taj korak treba uvijek jasno označiti prije nego što se zapis zaključa.

**Nakon ovoga poglavlja mora biti moguće**

1. postaviti kontrolni volumen za mlaz i vodilicu.
2. iz promjene vektora brzine odrediti komponente sile, reakcije i osnovni moment u uklještenju.
3. koristiti isti aparat količine gibanja kao bazu za lopatice, moment i mlazni potisak.

**U tehnici to znači**

Peltonovo kolo, vodomlazni pogon i mlazna ispitna glava rade dobro samo ako je ispravno pročitano koliko količine gibanja fluid predaje lopatici ili konstrukciji. Iz iste jednadžbe zato ovdje proizlaze sila, moment, snaga i potisak, ovisno o tome što se promatra kao radni izlaz sustava.

**Granica modela**

Maksimalna sila nije isto što i maksimalna snaga, a idealizirana promjena vektora brzine nije dovoljna ako su važni gubici u lopatici, neujednačen profil brzine ili složenija geometrija mlaza. U stvarnom stroju izbor kuta i brzine uvijek treba čitati zajedno s učinkovitošću, a ne samo sa silom.

<span class="mf1-ch-ref"><span class="mf1-ch-code">pog. 14</span><span class="mf1-ch-title">Turbostrojevi i propulzija</span></span> počinje kontrolnim volumenom, ne turbinom. Jasno čitanje promjene količine gibanja na mirnoj vodilici daje stabilnu osnovu i za reakcije nosača i za kasnije pokretne lopatice.
:::

::: {.mf1-numerika}
<p class="mf1-box-label">Numerički most</p>

**Gdje ovo živi u numerici.** Numerički modeli turbostrojeva računaju apsolutnu i relativnu brzinu, tlak te moment na rotoru. MRF je stacionarna aproksimacija u rotirajućem okviru; klizajuća mreža ili drugi nestacionarni pristupi potrebni su kada je važna vremenska interakcija rotora i statora.

**Što numerički alat radi s tim.** Iz polja tlaka i viskoznih naprezanja integriraju se sila, moment i snaga. Rezultat ovisi o domeni, mreži, vremenskom koraku, rubnim uvjetima i odabranim modelima turbulencije ili višefaznosti.

**Tipičan scenarij.** Simulacija može pokazati zone niskog tlaka i, uz izričito odabran višefazni model, procijeniti opseg parne faze. Sama po sebi ne dokazuje kavitacijsku otpornost ni vijek bez erozije; za takve zaključke trebaju verifikacija, odgovarajući eksperimentalni podatci i zaseban materijalni model [@nasa-cfd-vv; @asme-vv20-2009].

> *Nije gradivo MF1. Veza s ručnim računom ostaje bilanca momenta i snage, ali složeniji numerički model uvodi dodatne pretpostavke koje treba zasebno provjeriti.*
:::
