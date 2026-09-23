![Pregled poglavlja: turbostrojevi i propulzija kroz pokretne lopatice, moment i potisak.](../assets/print/u12_fig_uvod_pregled.svg){#fig-uvod-u12 fig-align="center" fig-alt="Pregled poglavlja: turbostrojevi i propulzija kroz pokretne lopatice, moment i potisak."}

## Turbostrojevi i propulzija

Analiza turbostrojeva i propulzijskih sustava temelji se na promjeni količine gibanja fluida u kontrolnom volumenu. Taj pristup određuje reakciju nosača, snagu na pokretnim lopaticama i mlazni potisak.

::: {.mf1-application}
<p class="mf1-box-label">Inženjerski kontekst</p>

Na Peltonovu kolu, vodomlaznom pogonu i mlaznici koja skreće tok isti zakoni povezuju silu, moment i snagu. Račun pokazuje koliko snage rotor prima, koliki je potisak i kako izlazni kut mijenja korisni učinak.
:::

**Procijenjeno vrijeme rada uz udžbenik:** 9 sati.

## Zakon količine gibanja za lopatice i vodilice

Kad mlaz promijeni smjer ili iznos brzine, mora postojati sila koja je uzrokovala tu promjenu količine gibanja. Za nepomični kontrolni volumen, stacionaran tok te jedan ulaz i izlaz osnovni zapis je

$$\sum \vec{F} = \dot{m}(\vec{V}_{izl} - \vec{V}_{ul})$$ {#eq-turbostrojevi-fizikalni-uvod-i-matematicki-izvod-01}

::: {.mf1-fizikalno-znacenje}
<p class="mf1-box-label">Fizikalno značenje</p>
Za vodilicu, a uz odgovarajući relativni protok i za pokretnu lopaticu, ovaj zakon kaže: sila potrebna za skretanje ili usporavanje mlaza proporcionalna je masenom protoku i promjeni vektora brzine. Za idealizirani Peltonov rotor s punim sapničkim protokom relativna brzina ulaza jest $w_1=c_1-u$. Snaga je umnožak tangencijalne sile i obodne brzine, pa pri $u=0$ postoji sila bez snage, a pri $u\to c_1$ relativna ulazna brzina teži nuli. Između tih granica model daje maksimum pri $u=c_1/2$.
:::

To je osnova za daljnju analizu u <span class="mf1-ch-ref"><span class="mf1-ch-code">pog. 14</span><span class="mf1-ch-title">Turbostrojevi i propulzija</span></span>: nepomična vodilica, pokretna lopatica, moment na rotoru i mlazni potisak. Zato predznake i smjerove treba odrediti prije uvrštavanja brojeva u jednadžbe.

## Matematički izvod

Za stacionarni tok kroz vodilicu ili lopaticu najprije se određuje maseni protok

$$
\dot m = \rho A v_n,
$$ {#eq-turbostrojevi-matematicki-izvod-01}

gdje je $v_n$ komponenta brzine okomita na ulazni presjek. Za nepomičnu vodilicu ili lopaticu, uz zanemarive razlike tlakova prema atmosferi i uz zanemarivu težinu u promatranoj ravnini, zakon količine gibanja daje

$$
\vec F_{okoline\to fluid} = \dot m(\vec c_2 - \vec c_1).
$$ {#eq-turbostrojevi-matematicki-izvod-02}

Najčešća pogreška u ovom postupku odnosi se na predznak: ta jednadžba najprije daje silu okoline na fluid. Suprotan predznak daje silu fluida na vodilicu; reakcija nosača na mirnu vodilicu ima suprotan smjer od te sile:

$$
\vec F_{fluid\to vodilicu} = -\dot m(\vec c_2 - \vec c_1).
$$ {#eq-turbostrojevi-matematicki-izvod-03}

U komponentnom zapisu odmah se vidi kako svaki izlazni zaokret ili pad brzine stvara novu reakciju po odgovarajućoj osi. Time ista jednadžba količine gibanja u <span class="mf1-ch-ref"><span class="mf1-ch-code">pog. 14</span><span class="mf1-ch-title">Turbostrojevi i propulzija</span></span> povezuje dva tipa primjene: ako fluid izgubi tangencijalnu komponentu brzine, rotor ili lopatica primaju silu, moment i snagu; ako fluid dobije brzinu prema dolje ili unatrag, cijeli sustav prima potisak.

Za pokretnu lopaticu prvi korak nije sila nego razdvajanje apsolutne i relativne brzine. Opći Reynoldsov transportni teorem iz <span class="mf1-ch-ref"><span class="mf1-ch-code">pog. 7</span><span class="mf1-ch-title">Kinematika, kontrolni volumen i kontinuitet</span></span> daje, u inercijskom okviru,

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
## Postupak rješenja
Od relativne brzine ($\vec{w}$) do sile na pokretnu lopaticu

**1. Relativni ulaz:** Lopatica se giba brzinom $u$, pa fluid prilazi lopatici relativnom brzinom $w_1 = c_1 - u$ (u 1D slučaju u smjeru mlaza). Maseni protok koji zaista prolazi kroz lopaticu:
$$\dot{m} = \rho A w_1.$$ {#eq-turbostrojevi-razrada-koraka-01}

**2. Relativni izlaz:** Lopatica skreće relativni tok za kut $\beta_2$. U relativnom okviru izlazna brzina je $w_2 = w_1$ (bez gubitaka). U apsolutnom okviru:
$$c_{2x} = u + w_2\cos\beta_2, \qquad c_{2y} = w_2\sin\beta_2.$$ {#eq-turbostrojevi-razrada-koraka-02}

**3. Promjena količine gibanja** (u apsolutnom okviru) najprije daje silu lopatice na fluid:
$$F_{lop\to f,x} = \dot{m}(c_{2x} - c_1) = \dot{m}w_1(\cos\beta_2 - 1).$$ {#eq-turbostrojevi-razrada-koraka-03}

Sila fluida na lopaticu ima suprotan predznak:
$$F_{f\to lop,x}=\dot m w_1(1-\cos\beta_2).$$ {#eq-turbostrojevi-razrada-koraka-04}

**4. Snaga koju fluid predaje lopatici:**
$$P_{f\to lop}=F_{f\to lop,x}u=\dot{m}w_1u(1-\cos\beta_2).$$ {#eq-turbostrojevi-razrada-koraka-05}

Za $\beta_2 = 180°$ (idealno skretanje u suprotni smjer) funkcija snage jedne lopatice glasi $P(u)=2\rho A(c_1-u)^2u$. Tek deriviranjem se pokazuje da joj je maksimum pri $u=c_1/3$. Za kolo s mnogo lopatica puni sapnički protok ostaje stalan, pa drugi model daje $u=c_1/2$.
:::

::: {.mf1-izvod}
<p class="mf1-box-label">Matematički izvod — Optimum obodne brzine za jednu lopaticu i za kolo</p>

Razlikuju se dva pedagoški važna granična slučaja koja daju različite optimalne obodne brzine, ovisno o tome kako se računa maseni protok kroz lopaticu.

**Slučaj 1: Jedna lopatica koja se udaljava u smjeru mlaza**

Pri pojedinačnoj lopatici koja se giba u smjeru mlaza, relativni dotok određuje koliko fluida u jedinici vremena dolazi do lopatice. Maseni protok koji efektivno djeluje na lopaticu je relativni protok

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

Ukupna tangencijalna sila na lopatice i snaga predana rotoru tada su

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

- Pri pojedinačnoj lopatici, $\dot m$ ovisi o $(c_1 - u)$, što daje kvadratnu ovisnost sile o relativnoj brzini. Optimum je niži ($u_{opt} = c_1/3$) jer veće $u$ smanjuje maseni protok.
- Pri kolu s mnogo lopatica $\dot m$ je konstantan, pa sila linearno opada s $(c_1 - u)$. Optimum je viši ($u_{opt} = c_1/2$) — klasičan rezultat za Peltonove turbine.

U oba slučaja idealni izlazni kut $\beta_2=180^\circ$ daje faktor $(1-\cos\beta_2)=2$. Ako geometrija, primjerice, ograniči skretanje na $\beta_2=165^\circ$, faktor pada na $(1-\cos165^\circ)\approx1{,}97$, odnosno za oko $1{,}7\,\%$ prema tom idealnom kutnom faktoru. To nije ukupni gubitak turbine: brzinski, volumetrijski i mehanički gubitci procjenjuju se zasebno.
:::

Kad je zanimljiv mehanički izlaz stroja, ključna više nije bilo koja komponenta sile nego tangencijalna komponenta, jer upravo ona predaje rad pri gibanju oboda:

$$
P = F_t u = M\omega
$$ {#eq-turbostrojevi-matematicki-izvod-optimum-obodne-brzine-za-jednu-09}

::: {.mf1-fizikalno-znacenje}
<p class="mf1-box-label">Fizikalno značenje</p>
Snaga $P = F_t u$ pokazuje da pri čistoj vrtnji rad rotoru predaje tangencijalna sila. Kada su ulaz i izlaz na istom polumjeru, ona se određuje iz promjene tangencijalne komponente brzine. Radijalna promjena brzine mijenja opterećenje ležajeva, ali ne i snagu. Promjena aksijalne komponente brzine mijenja aksijalne sile, ali tangencijalna komponenta je jedina koja djeluje u smjeru vrtnje. Zato je svaki kut lopatice — ulazni i izlazni — izravno uvjet za korisni učinak, a ne samo geometrijski detalj.
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

Komponenta momenta oko osi vrtnje rotora čita se iz vektorskog produkta: na zadanom radijusu $r$ doprinos momentu daje samo tangencijalna komponenta brzine $c_t$ jer ona jedina ima krak $r$ oko osi (radijalna komponenta prolazi kroz os, a aksijalna je paralelna s osi). Zato je predznačena komponenta momenta oko osi

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

Iz Eulerove jednadžbe odmah se vidi da korisni rad ne daje bilo koja komponenta brzine, nego promjena momenta količine gibanja oko osi rotora — to je razlog zašto su ulazni i izlazni kutovi lopatica središnji projektni parametri svakoga turbostroja.

::: {.callout-note collapse="true" icon="false"}
## Strujanje gledano s lopatice

Promatrač koji miruje uz crpku i promatrač koji se vrti s lopaticom vide različite brzine istog fluida. Računalo može iskoristiti pogled s lopatice: ona u tom prikazu miruje, a njezina vrtnja uzima se u obzir u jednadžbama gibanja. To olakšava procjenu prosječnog momenta i snage rotora.

Za promjene tlaka koje nastaju svaki put kada lopatica prođe pokraj nepomičnog dijela crpke treba pratiti gibanje kroz vrijeme. Izbor postupka zato ovisi o pitanju: tražimo li prosječnu snagu ili i promjene opterećenja tijekom jednog okreta?
:::

::: {.mf1-interaktivno}
<p class="mf1-box-label">Interaktivni prikaz — Trokuti brzina i snaga na Peltonovoj lopatici</p>

Interaktivni prikaz omogućuje mijenjanje apsolutne brzine mlaza, obodne brzine lopatice i izlaznog kuta uz neposredno praćenje trokuta brzina i krivulje snage. Optimalna obodna brzina i pripadna maksimalna snaga jasno se očituju na grafu. Nastavci reproduciraju obrnuti račun Z3, oba trokuta i Eulerov rad Z4 te usporedbu pogona Z5.

<div class="mf1-interaktivno-akcija">
<a class="mf1-interaktivno-veza" href="https://martibasic.github.io/MF1_udzbenik/jlite/lab/index.html?path=u12_pelton_lopatica.ipynb">Pokreni u pregledniku</a>
<a class="mf1-interaktivno-veza" href="https://colab.research.google.com/github/martibasic/MF1_udzbenik/blob/main/notebooks/u12_pelton_lopatica.ipynb" target="_blank" rel="noopener">Pričuvno: otvori u Colabu</a>
<img class="mf1-interaktivno-qr" src="../assets/qr/u12_pelton_lopatica.svg" alt="QR kod za interaktivni prikaz Peltonove lopatice"/>
</div>

<div class="mf1-interaktivno-pitanja">
**Pitanja za samostalno istraživanje:** (a) Zašto model rotora s punim sapničkim protokom daje maksimalnu snagu pri $u=c_1/2$ kada su $k$ i $\beta_2$ konstantni? (b) Kakva je teorijska maksimalna snaga pri $\beta_2=180°$ i zašto stvarne lopatice nemaju potpuni povrat mlaza? (c) Pri $u=0$, kolika je snaga predana rotoru iako sila postoji?
</div>
:::

Kod propulzije sustav predaje energiju fluidu. Ako vozilo ili platforma izbacuje mlaz dok je ulazna brzina okolnog fluida u smjeru potiska mala ili zanemariva, iz jednadžbe količine gibanja slijedi

$$
F_p = \dot m(v_{izl} - v_{ul}) \approx \dot m v = \rho A v^2.
$$ {#eq-turbostrojevi-interaktivni-prikaz-trokuti-brzina-i-snaga-na-01}

Za propelere i rotore koji stoje u mjestu i ubrzavaju okolni fluid (helikopter u visu, dron koji lebdi, brodski propeler pri statičkom potisku) koristi se nešto profinjeniji model — teorija aktuatorskog diska — koja vodi na izvod brzine kroz rotor pri zadanom potisku.

::: {.mf1-izvod}
<p class="mf1-box-label">Matematički izvod — Aktuatorski disk i Froudeov teorem</p>

Promatra se idealizirani rotor (propeler, dron, helikopter) kao tanki disk površine $A$ kroz koji fluid ulazi iz okoline i izlazi ubrzano u mlaznoj traci. Pretpostavlja se stacionarno, jednodimenzijsko, nestlačivo strujanje bez viskoznih gubitaka izvan idealiziranoga tlačnog skoka na disku; opterećenje je jednoliko po disku, nema vrtložne komponente brzine, vršnih ni glavinskih gubitaka, utjecaja tla ni međudjelovanja susjednih rotora. U modelu se definiraju četiri presjeka:

- presjek $\infty$ (daleko ispred diska): brzina $v_\infty$, atmosferski tlak $p_\infty$;
- presjek tik ispred diska: brzina $v_d$, tlak $p_d^-$;
- presjek tik iza diska: brzina $v_d$ (kontinuitet zahtijeva istu brzinu kroz disk), tlak $p_d^+ > p_d^-$;
- presjek $w$ (u dalekoj traci, gdje se tlak vraća na atmosferski): brzina $v_w$, tlak $p_\infty$.

Maseni protok kroz strujnu cijev je konstantan: $\dot m = \rho A v_d$.

**Zakon količine gibanja** za cijelu strujnu cijev daje potisak

$$
F_p = \dot m\,(v_w - v_\infty) = \rho A v_d (v_w - v_\infty).
$$ {#eq-turbostrojevi-matematicki-izvod-aktuatorski-disk-i-froudeov-te-01}

**Bernoullijeva jednadžba** primijenjena dva puta — ispred diska (od $\infty$ do $d^-$) i iza diska (od $d^+$ do $w$, jer je disk jedino mjesto predaje energije pa Bernoullijeva jednadžba vrijedi zasebno u području ispred i iza njega) — daje

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

**Lebdeći režim** ($v_\infty = 0$) — dron u visu, helikopter na mjestu, statički test propelera — daje $v_d = v_w/2$, pa potisak postaje

$$
F_p = \rho A v_d \cdot v_w = \rho A v_d \cdot 2 v_d = 2\rho A v_d^2.
$$ {#eq-turbostrojevi-matematicki-izvod-aktuatorski-disk-i-froudeov-te-08}

Iz toga slijedi i izravna formula koja se koristi u praksi:

$$
v_d = \sqrt{\frac{F_p}{2\rho A}}.
$$ {#eq-turbostrojevi-matematicki-izvod-aktuatorski-disk-i-froudeov-te-09}

Ova relacija pokazuje da je inducirana brzina kroz idealni rotor proporcionalna $\sqrt{F_p/A}$. Za isti potisak veća diskovna površina smanjuje induciranu brzinu i idealnu induciranu snagu $P_i=F_pv_d$. To ne jamči veću ukupnu korisnost stvarnog rotora, jer ona ovisi i o profilu lopatice, broju okretaja, vršnim gubitcima, motoru i drugim učincima koje ovaj model ne sadrži.
:::

Isti zakon zato vodi i Peltonov rotor i potisni sustav: u prvom slučaju fluid gubi korisnu tangencijalnu količinu gibanja i stroj prima rad, a u drugom slučaju fluidu se povećava količina gibanja u smjeru mlaza, a na platformu djeluje suprotno usmjeren potisak. Nova fizika nije u drugoj formuli, nego u tome tko preuzima reakciju i u kojem se referentnom okviru čita tok.

To je pravi strojarski smisao <span class="mf1-ch-ref"><span class="mf1-ch-code">pog. 14</span><span class="mf1-ch-title">Turbostrojevi i propulzija</span></span>. Na Peltonovu kolu loš odabir obodne brzine odmah smanjuje moment i snagu generatora. Na vodilici ili ispitnoj glavi pogrešno pročitan izlazni vektor znači pogrešnu reakciju nosača. Na propeleru ili vodomlaznome pogonu ista matematika povezuje ubrzanje fluida s potiskom sustava.

::: {.mf1-numerika .kompakt}
<p class="mf1-box-label">Numerički trag — referentni okvir rotora</p>

Brzina koju vidi lopatica razlikuje se od brzine u nepokretnom sustavu, pa se i numerički rezultat mora čitati u jasno navedenom okviru. Trokuti brzina, moment i snaga trebaju se provjeriti istim konvencijama na ulazu i izlazu; inače se može dobiti brojčano uredan, ali pogrešno protumačen rad stroja.
:::

::: {.mf1-numerika .kompakt}
<p class="mf1-box-label">Numerički trag — rotor i relativna brzina</p>

Numerički model turbostroja računa apsolutne i relativne brzine, tlak te moment na rotoru. MRF opisuje stacionarnu aproksimaciju u rotirajućem okviru, dok su klizajuća mreža ili drugi nestacionarni pristupi potrebni kada interakcija rotora i statora mijenja traženi odziv.

Moment, snaga, protok i promjena vrtložne komponente brzine čitaju se u dosljedno odabranom referentnom okviru. Korisna je neovisna provjera Eulerovom jednadžbom turbostroja pri istim presjecima, predznacima i obodnoj brzini lopatice.

Stacionarni model može dobro opisati srednju radnu točku, ali ne i pulsacije, prolaz lopatica ili nestacionarnu kavitaciju. Za takve pojave provjeravaju se vremenski korak, broj okretaja potrebnih za statistiku i osjetljivost momenta na mrežu uz lopatice.
:::

## Riješeni primjeri

Međurezultati u prikazu zaokruženi su radi čitljivosti. Završne sile, momenti i snage računaju se iz nezaokruženih vrijednosti.

::: {#ex-u12-vodilica-mlaza-na-ispitnom-stolu-t2 .mf1-we}
<p class="mf1-box-label">P1. Vodilica mlaza na ispitnom stolu&nbsp;<span class="mf1-level">T2</span></p>

**Kontekst:** Na hidrauličkom ispitnom stolu nepomična vodilica skreće pravokutni mlaz vode u horizontalnoj ravnini za određeni kut, pri čemu se brzina zbog gubitaka smanjuje. Iz promjene količine gibanja određuje se reakcijska sila na nosač vodilice, što je tipičan ulazni primjer za analizu sila na lopaticama.

**Zadano**

- Širina pravokutne sapnice: $b = 36\ \text{mm}$
- Visina pravokutne sapnice: $h = 14\ \text{mm}$
- Brzina mlaza na ulazu u vodilicu: $v_1 = 24\ \text{m/s}$
- Kut skretanja u horizontalnoj ravnini: $\beta = 120^\circ$
- Izlazna brzina mlaza (s gubicima): $v_2 = 19\ \text{m/s}$
- Gustoća vode: $\rho = 998\ \text{kg/m}^3$

**Traženo**

1. Odredi maseni protok vode kroz sapnicu.
2. Odredi horizontalne komponente sile koju fluid vrši na vodilicu.
3. Odredi iznos i smjer reakcije koju mora preuzeti nosač vodilice.

![Vodilica mlaza na ispitnom stolu](../assets/print/u12_val1_vodilica_mlaza.svg){#fig-u12-vodilica-mlaza-na-ispitnom-stolu fig-alt="Vodilica mlaza na ispitnom stolu"}

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
<p class="mf1-box-label">P2. Relativni dotok na pokretnu lopaticu&nbsp;<span class="mf1-level">T1</span></p>

**Kontekst:** Kada se lopatica giba u smjeru mlaza, kroz njezin pokretni kontrolni volumen ulazi samo relativni protok određen razlikom brzina mlaza i lopatice. Ovaj uvodni primjer pokazuje koliko se taj efektivni protok razlikuje od punog sapničkog protoka, što je važno za razlikovanje modela jedne pokretne lopatice i cijeloga višelopatičnog rotora.

**Zadano**

- Gustoća vode: $\rho = 998\ \text{kg/m}^3$
- Promjer sapnice: $d = 38\ \text{mm}$
- Apsolutna brzina mlaza na izlazu iz sapnice: $c_1 = 22\ \text{m/s}$
- Brzina lopatice (u istom smjeru): $u = 8\ \text{m/s}$
- Lopatica zahvaća cijeli mlaz.

**Traženo**

1. Odredi relativnu ulaznu brzinu $w_1$.
2. Odredi relativni maseni protok $\dot m_{rel}$ kroz pokretni kontrolni volumen.
3. Usporedi taj relativni protok s punim masenim protokom sapnice.

![Pokretna lopatica: c1=22 m/s, u=8 m/s, w1=14 m/s, relativni protok 63,6%](../assets/print/u12_fig_relativni_dotok.svg){#fig-u12-relativni-dotok-lopatica fig-align="center" fig-alt="Pokretna lopatica: c1=22 m/s, u=8 m/s, w1=14 m/s, relativni protok 63,6%"}

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
\frac{\dot m_{rel}}{\dot m} = \frac{c_1-u}{c_1} = \frac{14}{22} \approx 0{,}636
$$ {#eq-turbostrojevi-rijeseni-primjer-relativni-dotok-na-pokretnu-lop-05}

odnosno oko $63{,}6\%$ punog sapničkog protoka.

**Provjera i komentar**

1. Ako bi lopatica mirovala, moralo bi biti $w_1 = c_1$.
2. Kako se lopatica giba u istom smjeru kao mlaz, relativni protok mora biti manji od punog sapničkog protoka.
3. Kad bi bilo $u \to c_1$, relativni bi dotok težio nuli.
:::

::: {#ex-u12-pokretna-ravna-lopatica-u-mlazu-t2 .mf1-we}
<p class="mf1-box-label">P3. Pokretna ravna lopatica u mlazu&nbsp;<span class="mf1-level">T2</span></p>

**Kontekst:** Ravna lopatica koja se giba u smjeru mlaza mijenja količinu gibanja fluida i preuzima dio energije mlaza. Iz relativnog dotoka i promjene apsolutne brzine određuju se sila i snaga koje lopatica predaje nosaču, što je didaktička priprema za rotorne lopatice.

**Zadano**

- Gustoća vode: $\rho = 998\ \text{kg/m}^3$
- Promjer sapnice: $d = 40\ \text{mm}$
- Apsolutna brzina mlaza: $c_1 = 24\ \text{m/s}$
- Brzina lopatice (u istom smjeru kao mlaz): $u = 9\ \text{m/s}$
- Lopatica zahvaća cijeli mlaz; nakon udara voda u apsolutnom sustavu napušta lopaticu s vodoravnom brzinom jednakom $u$; gubitci zanemarivi.

**Traženo**

1. maseni protok koji stvarno ulazi u pokretni kontrolni volumen.
2. silu mlaza na lopaticu.
3. snagu koju mlaz predaje lopatici.

![Pokretna ravna lopatica](../assets/print/u12_val3_pokretna_lopatica.svg){#fig-u12-pokretna-ravna-lopatica fig-alt="Pokretna ravna lopatica"}

**Pretpostavke i model**

Za pokretni element presudan je relativni dotok $c_1-u$. Zato se kroz lopaticu ne vodi puni maseni protok sapnice, nego samo onaj koji u pokretnom sustavu stvarno presijeca kontrolnu površinu. Promjena količine gibanja po osi $x$ zato se zatvara upravo tim relativnim protokom.

**Rješenje**

Površina mlaza iznosi

$$
A = \frac{\pi d^2}{4} = \frac{\pi \cdot 0{,}04^2}{4} = 1{,}257 \cdot 10^{-3}\ \text{m}^2.
$$ {#eq-turbostrojevi-rijeseni-primjer-pokretna-ravna-lopatica-u-mlazu-01}

Relativna ulazna brzina prema lopatici je $c_r = c_1-u = 24-9 = 15\ \text{m/s}$, pa je maseni protok koji stvarno ulazi u pokretni kontrolni volumen

$$
\dot{m}_{rel} = \rho \frac{\pi d^2}{4} c_r = 998 \cdot \frac{\pi\cdot0{,}040^2}{4} \cdot 15 \approx 18{,}81\ \text{kg/s}.
$$ {#eq-turbostrojevi-rijeseni-primjer-pokretna-ravna-lopatica-u-mlazu-02}

Kako voda nakon udara u apsolutnom sustavu odlazi s vodoravnom brzinom $u$, promjena vodoravne komponente brzine iznosi $c_1-u = 15\ \text{m/s}$, pa sila lopatice na fluid glasi

$$
F_{l\to f} = \dot{m}_{rel}(u-c_1) \approx -282{,}2\ \text{N}.
$$ {#eq-turbostrojevi-rijeseni-primjer-pokretna-ravna-lopatica-u-mlazu-03}

Zato fluid na lopaticu djeluje silom suprotnog smjera, pa je traženi iznos sile $F = 282{,}2\ \text{N} \approx 282\ \text{N}$. Snaga predana lopatici iznosi

$$
P = Fu = 282{,}2 \cdot 9 \approx 2540\ \text{W} = 2{,}54\ \text{kW}.
$$ {#eq-turbostrojevi-rijeseni-primjer-pokretna-ravna-lopatica-u-mlazu-04}

**Provjera i komentar**

1. Ako bi lopatica mirovala, sila bi morala biti veća nego u ovom slučaju jer bi relativni dotok bio veći.
2. Ako bi se lopatica gibala brzinom jednakom brzini mlaza, relativni dotok pao bi na nulu i nestala bi i sila.
3. Snaga mora biti reda nekoliko kilovata jer se sila reda nekoliko stotina njutna prenosi na brzinu reda deset metara u sekundi.
:::

::: {#ex-u12-pokretna-zakrivljena-lopatica-s-relativnim-izlazom-t3 .mf1-ch}
<p class="mf1-box-label">P4. Pokretna zakrivljena lopatica s relativnim izlazom&nbsp;<span class="mf1-level">T3</span></p>

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

![Pokretna zakrivljena lopatica](../assets/print/u12_ch1_pokretna_zakrivljena_lopatica.svg){#fig-u12-pokretna-zakrivljena-lopatica fig-alt="Pokretna zakrivljena lopatica"}

**Pretpostavke i model**

Pokretni kontrolni volumen vezan je uz lopaticu, pa kroz njega ne prolazi puni sapnički protok nego samo relativni dotok definiran razlikom $c_1-u$. Iz relativnog izlaza najprije se odredi apsolutni izlazni vektor, a tek zatim jednadžba količine gibanja daje silu na lopaticu. Snaga se na kraju zatvara samo preko komponente sile u smjeru gibanja lopatice.

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
\vec{F}_{l \to f} = \dot{m}_{rel}(\vec{c}_2 - \vec{c}_1) \approx (-723{,}0,\ 182{,}9)\ \text{N}.
$$ {#eq-turbostrojevi-cjeloviti-zadatak-pokretna-zakrivljena-lopatica-05}

Zato fluid na lopaticu djeluje silom suprotnog smjera $\vec{F}_{f \to l} = (723{,}0,\ -182{,}9)\ \text{N}$, pa su komponente sile $F_x \approx 723\ \text{N}$, $F_y \approx -183\ \text{N}$, a rezultantni iznos

$$
F = \sqrt{723{,}0^2 + 182{,}9^2} = 746\ \text{N}.
$$ {#eq-turbostrojevi-cjeloviti-zadatak-pokretna-zakrivljena-lopatica-06}

Snagu predanu lopatici daje samo komponenta sile u smjeru gibanja:

$$
P = F_x u = 723{,}0 \cdot 10 = 7230\ \text{W} \approx 7{,}23\ \text{kW}.
$$ {#eq-turbostrojevi-cjeloviti-zadatak-pokretna-zakrivljena-lopatica-07}

**Provjera i komentar**

Ovaj cjeloviti zadatak zatvara puni prijelaz kroz <span class="mf1-ch-ref"><span class="mf1-ch-code">pog. 14</span><span class="mf1-ch-title">Turbostrojevi i propulzija</span></span>: relativni dotok daje $\dot{m}_{rel} \approx 25{,}4\ \text{kg/s}$, relativni izlaz mora se prevesti u apsolutni vektor $\vec{c}_2 \approx (-2{,}47,\ 7{,}20)\ \text{m/s}$, a tek tada se dobiva sila mlaza na lopaticu od oko $(723, -183)\ \text{N}$. Budući da rad proizvodi samo komponenta sile u smjeru gibanja, lopatica prima snagu od oko $7{,}23\ \text{kW}$.

1. Maseni protok kroz pokretni kontrolni volumen mora biti manji od punog sapničkog protoka jer je $w_1 = c_1-u < c_1$.
2. Komponenta $F_x$ mora ostati dominantna jer se ulazna i izlazna komponenta brzine u tom smjeru najviše razlikuju.
3. Kad bi se lopatica gibala brzinom jednakom brzini mlaza, relativni dotok bi nestao, pa bi nestale i sila i snaga.
:::

::: {#ex-u12-peltonov-rotor-s-jednim-mlazom-i-momentom .mf1-ch}
<p class="mf1-box-label">P5. Reprezentativna Peltonova lopatica i trenutačni moment&nbsp;<span class="mf1-level">T4</span></p>

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

Smjer osi $x$ odabran je tangencijalno u smjeru gibanja oboda. Pretpostavi da lopatica potpuno zahvaća mlaz te da su ulaz i izlaz na atmosferskom tlaku. Račun je lokalna kvazistacionarna aproksimacija: tijekom prolaza fluida smjer obodne brzine smatra se stalnim, a rotacijska akumulacija zanemarivom. To ograničava primjenu na kratak lokalni prolaz, ne na cijeli okret rotora.

**Traženo**

1. obodnu brzinu rotora $u$ i relativnu ulaznu brzinu $w_1$.
2. maseni protok kroz pokretni kontrolni volumen $\dot{m}_{rel}$ i apsolutni izlazni vektor $\vec{c}_2$.
3. komponente i iznos sile fluida na lopaticu.
4. moment na obodu rotora i snagu koju mlaz predaje rotoru.
5. usporedbu trenutačne idealizirane snage lopatice s traženom snagom generatora i objašnjenje zašto ta usporedba sama ne dokazuje pogonsku dostatnost rotora.

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
\vec{F}_{l \to f} = \dot{m}_{rel}(\vec{c}_2 - \vec{c}_1) \approx (-680{,}3,\ 113{,}5)\ \text{N}.
$$ {#eq-turbostrojevi-cjeloviti-zadatak-reprezentativna-peltonova-lopa-06}

Zato fluid na lopaticu djeluje silom suprotnog smjera $\vec{F}_{f \to l} = (680{,}3,\ -113{,}5)\ \text{N}$, pa su tražene komponente $F_x \approx 680\ \text{N}$, $F_y \approx -114\ \text{N}$, a rezultantni iznos sile je

$$
F = \sqrt{F_x^2 + F_y^2} \approx 689{,}7\ \text{N}.
$$ {#eq-turbostrojevi-cjeloviti-zadatak-reprezentativna-peltonova-lopa-07}

Tangencijalna komponenta $F_x$ stvara moment na obodu rotora:

$$
M = F_x r \approx 312{,}95\ \text{N m} \approx 313\ \text{N m}.
$$ {#eq-turbostrojevi-cjeloviti-zadatak-reprezentativna-peltonova-lopa-08}

Snaga koju mlaz predaje rotoru iznosi

$$
P = M\omega = 312{,}95 \cdot 33{,}51 = 10{,}49\ \text{kW},
$$ {#eq-turbostrojevi-cjeloviti-zadatak-reprezentativna-peltonova-lopa-09}

što odgovara i zapisu $P=F_xu=680{,}3\cdot15{,}41=10{,}49\ \text{kW}$. Trenutačna idealizirana vrijednost veća je od $9{,}50\ \text{kW}$ za $0{,}99\ \text{kW}$, ali iz toga se ne smije zaključiti da cijeli rotor može trajno pogoniti takav generator. Model koristi relativni dotok $\rho A(c_1-u)$ jedne pokretne lopatice; kontinuirani Peltonov rotor zahvaća puni sapnički protok slijedom lopatica i traži zasebnu bilancu cijeloga kola te hidrauličke, mehaničke i generatorske gubitke.

**Provjera i komentar**

Ovaj `T4` zadatak zatvara račun reprezentativne lopatice u <span class="mf1-ch-ref"><span class="mf1-ch-code">pog. 14</span><span class="mf1-ch-title">Turbostrojevi i propulzija</span></span>: dobivaju se trenutačna tangencijalna sila od oko $680\ \text{N}$, doprinos momentu od oko $313\ \text{N m}$ i idealizirana snaga od oko $10{,}5\ \text{kW}$. Granica modela namjerno je dio odgovora: maseni protok jedne pokretne lopatice ne smije se bez nove postavke proglasiti kontinuiranim protokom cijeloga rotora.

1. U ovom stanju je $u>c_1/3$, pa dodatno povećanje brzine smanjuje snagu lokalnog modela jedne lopatice. Općenito snaga najprije raste, a zatim pada; sila sama ne određuje položaj maksimuma.
2. U ovom stanju tangencijalna komponenta sile veća je od normalne. Moment oko osi u lokalnom modelu proizvodi tangencijalna komponenta; iz toga ne slijedi opći uvjet za omjer tih sila.
3. Ako se iz relativnog izlaza izravno pročita moment bez povratka na apsolutni vektor $\vec{c}_2$, pogrešno se računa promjena momenta količine gibanja.
:::

Posljednji primjer mijenja medij i uređaj, ali ne i metodu: Peltonov impulsni rotor zamjenjuje aktuatorski disk, a bilanca količine gibanja povezuje potisak, induciranu brzinu i snagu.

::: {#ex-u12-propeler-dronskog-kvadkoptera-u-stanju-visa-t2 .mf1-we}
<p class="mf1-box-label">P6. Propeler dronskog kvadkoptera u stanju visa &nbsp;<span class="mf1-level">T2</span></p>

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
t=\frac{74\ \text{Wh}}{227{,}47\ \text{W}}\approx0{,}325\ \text{h}\approx19{,}5\ \text{min}.
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

2. Zašto idealizirano Peltonovo kolo s punim sapničkim protokom ima maksimum snage pri $u=c_1/2$, a pojedinačna pravocrtno gibajuća lopatica pri $u=c_1/3$?

::: {.callout-note collapse="true"}
### Odgovor
Za kolo je $Q$ stalni sapnički protok. Iz izraza $P = \rho Q (c_1 - u) u (1 - \cos\beta_2)$ slijedi da derivacija po $u$ jednaka je nuli pri $u = c_1/2$. Pri toj vrijednosti umnožak $(c_1-u)u$ je maksimalan, pa je i snaga maksimalna. Pri $u = 0$ ili $u = c_1$ snaga je nula. Za jednu lopaticu maseni dotok je $\rho A(c_1-u)$, pa dodatni faktor daje maksimum pri $u=c_1/3$; ta dva kontrolna volumena ne smiju se zamijeniti.
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

![Skice vježbi: sile na ploču i vodilicu, obrnuti račun izlaza lopatice, dva trokuta brzina, vodomlazni pogon i razdjelnik s četirima izlazima.](../assets/print/u12_vjezbe_skice.svg){#fig-u12-vjezbe fig-align="center" fig-alt="Slobodni mlazovi završavaju na prednjoj strani ploče ili prate otvorenu vodilicu. Kote mjere unutarnje presjeke; relativne i apsolutne brzine odvojene su od sila. Voda u razdjelnik platforme ulazi kroz dva otvorena vodoravna priključka."}

::::: {.mf1-vjezbe-list}

### Z1. Sila mlaza na nepomičnu ploču {#task-u12-vodeni-mlaz-brzine-izlazi-iz-kruzne-sapnice .unnumbered .unlisted}

Vodeni mlaz udara okomito na nepomičnu ravnu ploču i slobodno se razlijeva uz njezinu prednju stranu. Odredi maseni protok i silu fluida na ploču u smjeru ulaznog mlaza.

Zadano je $\rho=998\ \mathrm{kg/m^3}$, brzina $v=24\ \mathrm{m/s}$ i promjer slobodnog mlaza $d=22\ \mathrm{mm}$. Ploča zahvaća cijeli mlaz. Tok je stacionaran, tlak na slobodnim granicama atmosferski, a izlazna komponenta brzine okomita na ploču jednaka nuli. Težinu fluida u smjeru udara zanemari.

:::: {.content-visible .mf1-hint-online when-format="html"}
::: {.callout-note collapse="true" data-hint-key="true"}
### Naputak
Izračunaj $\dot m=\rho Av$. Bilanca količine gibanja daje silu ploče na fluid; za silu fluida na ploču promijeni predznak. Provjeri da nepomična ploča ne prima mehaničku snagu.
:::
::::
:::: {.content-visible .mf1-answer-online when-format="html"}
::: {.callout-tip collapse="true" data-answer-key="true"}
### Kontrolni rezultat
$\dot m\approx9{,}10\ \mathrm{kg/s}$ i $F_x\approx219\ \mathrm{N}$ u smjeru ulaznog mlaza. Ploča miruje, pa je predana mehanička snaga $P=0$ unatoč nenultoj sili.
:::
::::

[Razina: T1]{.mf1-task-level}

### Z2. Zakretanje mlaza u vodilici {#task-u12-vodeni-mlaz-brzine-izlazi-iz-pravokutne-sapnice .unnumbered .unlisted}

Nepomična vodilica zakreće pravokutni mlaz u vodoravnoj ravnini. Odredi predznačene komponente sile fluida na vodilicu te suprotnu reakciju nosača i njezin iznos.

Voda gustoće $\rho=998\ \mathrm{kg/m^3}$ ulazi brzinom $v=26\ \mathrm{m/s}$ kroz presjek širine $b=30\ \mathrm{mm}$ u tlocrtu i visine $h=16\ \mathrm{mm}$ okomito na njega. Ulaz je u smjeru $+x$, a izlazni kut $\beta=110^\circ$ mjeri se od $+x$ prema $+y$. Iznos brzine ostaje jednak. Tlakovi slobodnog mlaza su atmosferski, tok stacionaran, a težina ne doprinosi horizontalnim komponentama.

:::: {.content-visible .mf1-hint-online when-format="html"}
::: {.callout-note collapse="true" data-hint-key="true"}
### Naputak
Najprije $\dot m=\rho bhv$. Rastavi izlaznu brzinu u istim osima kao ulaznu. Za ravnotežu vodilice vrijedi $\vec R=-\vec F_{f\to v}$; veća pozitivna izlazna komponenta duž osi y znači negativan $F_y$.
:::
::::
:::: {.content-visible .mf1-answer-online when-format="html"}
::: {.callout-tip collapse="true" data-answer-key="true"}
### Kontrolni rezultat
$\dot m\approx12{,}46\ \mathrm{kg/s}$; sila fluida je $(F_x,F_y)\approx(435;-304)\ \mathrm{N}$. Reakcija nosača na vodilicu je $(R_x,R_y)\approx(-435;304)\ \mathrm{N}$, a njezin iznos $R\approx531\ \mathrm{N}$.
:::
::::

[Razina: T1]{.mf1-task-level}

<span id="task-u12-na-pokretnu-lopaticu-dolazi-mlaz-vode-apsolutnom"></span>

### Z3. Izlaz lopatice iz izmjerene sile {#task-izlaz-lopatice-iz-izmjerene-sile .unnumbered .unlisted}

Iz sile izmjerene na pokretnoj vodilici rekonstruiraj izlazni tok. Provjeri dopušta li rezultat pasivnu lopaticu s gubitkom relativne brzine te zatvori bilancu predane snage i gubitka mehaničke energije.

Lopatica se pravocrtno giba stalnom brzinom $u=12\ \mathrm{m/s}$ u smjeru $+x$. Apsolutna ulazna brzina je $\vec c_1=(32;0)\ \mathrm{m/s}$, a maseni protok kroz kontrolni volumen koji se giba s lopaticom jest $\dot m_{rel}=18\ \mathrm{kg/s}$. Sintetički istodobni podatci sile **fluida na lopaticu** jesu $F_x=625{,}0\ \mathrm{N}$ i $F_y=-153{,}0\ \mathrm{N}$; koristi ih kao zadane vrijednosti, bez analize mjerne nesigurnosti. Tok je stacionaran u tom okviru, presjeci imaju jednolike brzine, tlakovi su atmosferski, a težinu zanemari.

Odredi $\vec c_2$, $\vec w_2$, omjer $k=|\vec w_2|/|\vec w_1|$, kut izlaza $\beta_2$ od $+x$ prema $+y$, snagu lopatice $P$ i stopu gubitka mehaničke energije $\dot E_g$. Za pasivnu lopaticu bez drugog energetskog ulaza mora vrijediti $0\le k\le1$ i $\dot E_g\ge0$.

:::: {.content-visible .mf1-hint-online when-format="html"}
::: {.callout-note collapse="true" data-hint-key="true"}
### Naputak
Iz $\vec F_{f\to l}=\dot m_{rel}(\vec c_1-\vec c_2)$ dobiješ apsolutni izlaz. Zatim $\vec w_2=\vec c_2-(u,0)$ i kut funkcijom atan2. Provjeri $P=F_xu$ i $\dot E_g=\dot m_{rel}(|\vec c_1|^2-|\vec c_2|^2)/2-P$.
:::
::::
:::: {.content-visible .mf1-answer-online when-format="html"}
::: {.callout-tip collapse="true" data-answer-key="true"}
### Kontrolni rezultat
$\vec c_2\approx(-2{,}722;8{,}500)\ \mathrm{m/s}$, $\vec w_2\approx(-14{,}722;8{,}500)\ \mathrm{m/s}$; $k\approx0{,}850$ i $\beta_2\approx150{,}00^\circ$. Vrijedi $P=7{,}500\ \mathrm{kW}$ i $\dot E_g\approx0{,}999\ \mathrm{kW}$. Oba uvjeta pasivnosti su zadovoljena.
:::
::::

[Razina: T2]{.mf1-task-level}

<span id="task-u12-peltonova-lopatica-na-rotoru-radijusa-prima-mlaz"></span>

### Z4. Dva radijusa i rad rotora {#task-dva-radijusa-i-rad-rotora .unnumbered .unlisted}

Na dvama presjecima rotora zadane su apsolutne brzine. Nacrtaj oba trokuta brzina, odredi predznak momenta i snage te zaključi predaje li rotor rad fluidu ili prima rad od njega. Razlikuj lokalne komponente brzine na ulazu i izlazu te odredi koja komponenta sudjeluje u prijenosu momenta oko osi.

Zadano je $r_1=0{,}060\ \mathrm{m}$, $r_2=0{,}140\ \mathrm{m}$, $\omega=200\ \mathrm{rad/s}$ i ukupni stacionarni maseni protok kroz rotor $\dot m=3{,}00\ \mathrm{kg/s}$. Komponente u lokalnim osima (tangencijalno, radijalno prema van) jesu $\vec c_1=(5;4)\ \mathrm{m/s}$ i $\vec c_2=(20;6)\ \mathrm{m/s}$. Pozitivan tangencijalni smjer prati vrtnju; pri crtanju oba lokalna trokuta postavi ga udesno, a radijalni prema gore. Tlak i volumne sile nemaju moment oko osi, a akumulacija momenta količine gibanja izostaje.

Izračunaj $u_1$, $u_2$, oba relativna vektora, moment $M_{r\to f}$ i snagu $P_{r\to f}$ rotora na fluid te specifični rad $e_{r\to f}$. Navedi suprotni moment fluida na rotor i provjeri isti rezultat snage iz momenta i Eulerove jednadžbe.

:::: {.content-visible .mf1-hint-online when-format="html"}
::: {.callout-note collapse="true" data-hint-key="true"}
### Naputak
Za svaki presjek zasebno $u_i=\omega r_i$ i $\vec w_i=\vec c_i-(u_i,0)$. Pozitivan moment rotora na fluid jest $M_{r\to f}=\dot m(r_2c_{2t}-r_1c_{1t})$. Provjeri $P=M\omega=\dot m(u_2c_{2t}-u_1c_{1t})$.
:::
::::
:::: {.content-visible .mf1-answer-online when-format="html"}
::: {.callout-tip collapse="true" data-answer-key="true"}
### Kontrolni rezultat
$(u_1,u_2)=(12;28)\ \mathrm{m/s}$; $\vec w_1=(-7;4)\ \mathrm{m/s}$, $\vec w_2=(-8;6)\ \mathrm{m/s}$. $M_{r\to f}=+7{,}50\ \mathrm{N\,m}$, $M_{f\to r}=-7{,}50\ \mathrm{N\,m}$, $P_{r\to f}=+1{,}500\ \mathrm{kW}$ i $e_{r\to f}=+500\ \mathrm{J/kg}$. Rotor predaje rad fluidu; odgovara crpnom režimu.
:::
::::

[Razina: T2]{.mf1-task-level}

<span id="task-u12-potisni-modul-ima-tri-jednake-sapnice-promjera"></span>

### Z5. Vodomlazni pogon uz ograničenu snagu {#task-vodomlazni-pogon-uz-ogranicenu-snagu .unnumbered .unlisted}

Usporedi dva nastavna kandidata vodomlaznog pogona za jednak potisak pri zadanoj brzini broda. Izaberi izvedivu varijantu prema raspoloživoj električnoj snazi i objasni zašto veća izlazna brzina sama ne znači povoljniji pogon.

Brod se jednoliko giba brzinom $U=8{,}0\ \mathrm{m/s}$ kroz mirujuću vodu gustoće $\rho=1000\ \mathrm{kg/m^3}$. Potreban potisak je $T=2{,}00\ \mathrm{kN}$. U brodskom okviru voda ulazi brzinom $V_0=U$, a kandidati A i B izbacuju je unatrag brzinama $V_{j,A}=20{,}0\ \mathrm{m/s}$ i $V_{j,B}=30{,}0\ \mathrm{m/s}$. Svaki kandidat ima jednu kružnu izlaznu sapnicu. Zanemari razliku geodetskih visina, vanjske tlačne doprinose potisku, utjecaj traga trupa i gubitke u dovodu i sapnici. Referentne presjeke uzmi s jednakim atmosferskim tlakom. Tok je stacionaran u brodskom okviru, uz jednak ulazni i izlazni maseni protok.

Za obje varijante zadana učinkovitost pretvorbe električne u hidrauličku snagu pogona jest $\eta=0{,}80$, a dostupno je najviše $P_{el,max}=40{,}0\ \mathrm{kW}$. Odredi potreban $Q$, unutarnji promjer izlaza, snagu predanu fluidu $P_h$, električnu snagu i propulzijsku učinkovitost $\eta_{prop}=TU/P_h$. Zatvori bilancu korisne snage i kinetičke energije daleke trake te obrazloži izbor. Ne poistovjećuj $\eta_{prop}$ sa zadanom učinkovitošću pogona.

:::: {.content-visible .mf1-hint-online when-format="html"}
::: {.callout-note collapse="true" data-hint-key="true"}
### Naputak
U bilanci potiska zadrži ulazni tok količine gibanja: $T=\rho Q(V_j-U)$. Energijska bilanca brodskog okvira daje $P_h=\rho Q(V_j^2-U^2)/2$, a $P_{el}=P_h/\eta$. Površina sapnice je $Q/V_j$. Neovisno: $P_h=TU+\rho Q(V_j-U)^2/2$.
:::
::::
:::: {.content-visible .mf1-answer-online when-format="html"}
::: {.callout-tip collapse="true" data-answer-key="true"}
### Kontrolni rezultat
Za A/B: $Q\approx(166{,}67;90{,}91)\ \mathrm{L/s}$, $d\approx(103{,}01;62{,}12)\ \mathrm{mm}$, $P_h=(28;38)\ \mathrm{kW}$, $P_{el}=(35;47{,}5)\ \mathrm{kW}$ i $\eta_{prop}\approx(0{,}571;0{,}421)$. Obje varijante daju $TU=16\ \mathrm{kW}$; u traci ostaje 12 odnosno 22 kW. Granicu 40 kW zadovoljava samo A.
:::
::::

[Razina: T3]{.mf1-task-level}

### Z6. Podizanje mlazne platforme {#task-u12-mlazna-platforma-ukupne-mase-ima-cetiri-jednake .unnumbered .unlisted}

Procijeni potisak idealizirane mlazne platforme i najveću masu prema zadanom statičkom kriteriju. Odvojeno prikaži nazivni rezultat i najnepovoljniji slučaj dopuštenih ulaza te navedi granice takve procjene.

Trenutačna ukupna masa platforme, uključujući zadržani fluid, jest $m=110\ \mathrm{kg}$. Četiri jednake sapnice unutarnjeg promjera $d=28\ \mathrm{mm}$ izbacuju vodu gustoće $\rho=998\ \mathrm{kg/m^3}$ okomito dolje brzinom $v=36\ \mathrm{m/s}$ prema platformi. Vanjski dovodi su simetrični i vodoravni: njihov ulazni vertikalni tok količine gibanja i ukupna vertikalna sila dovodne instalacije uzimaju se jednakima nuli. Izlazi su na atmosferskom tlaku. Primijeni kvazistacionarni model u trenutku kad platforma miruje, uz zanemarenu akumulaciju relativne količine gibanja u razdjelniku.

Odredi ukupni potisak, najveću ukupnu masu lebdenja i trenutačno vertikalno ubrzanje pri zadanoj masi. Stvarni promjer svake sapnice može biti do $0{,}3\ \mathrm{mm}$ manji, a brzina do $1{,}5\ \mathrm{m/s}$ manja od nazivnih vrijednosti; to su zadane granice, ne standardne nesigurnosti. Za zahtjev najmanje $10\ \%$ rezerve potiska iznad težine odredi najveću masu koja zadovoljava cijeli interval ulaza. Objasni zašto rezultat nije certificirana nosivost niti opis kasnijeg ubrzanog gibanja.

:::: {.content-visible .mf1-hint-online when-format="html"}
::: {.callout-note collapse="true" data-hint-key="true"}
### Naputak
Zbroji četiri izlazne površine. Uz zadane pretpostavke $F_p=\rho Av^2$, masa lebdenja je $F_p/g$, a trenutačno $a=(F_p-mg)/m$. Za zadani kriterij koristi $d_{min}$ i $v_{min}$ te zahtijevaj $F_{p,min}\ge1{,}10\,mg$.
:::
::::
:::: {.content-visible .mf1-answer-online when-format="html"}
::: {.callout-tip collapse="true" data-answer-key="true"}
### Kontrolni rezultat
$F_p\approx3{,}186\ \mathrm{kN}$, masa lebdenja $324{,}7\ \mathrm{kg}$ i početno $a\approx19{,}15\ \mathrm{m/s^2}$. Za $d_{min}=27{,}7\ \mathrm{mm}$ i $v_{min}=34{,}5\ \mathrm{m/s}$: $F_{p,min}\approx2{,}863\ \mathrm{kN}$ i $m_{krit}\approx265{,}3\ \mathrm{kg}$. Zaključak vrijedi u zadanom modelu; nedostaju stvarne sile dovoda, dinamika, stabilnost, konstrukcijska i upravljačka provjera.
:::
::::

[Razina: T4]{.mf1-task-level}
:::::


::: {.mf1-numerika}
<p class="mf1-box-label">Numerički most</p>

**Veza s numeričkim proračunom.** Numerički modeli turbostrojeva računaju apsolutnu i relativnu brzinu, tlak te moment na rotoru. MRF je stacionarna aproksimacija u rotirajućem okviru; klizajuća mreža ili drugi nestacionarni pristupi potrebni su kada je važna vremenska interakcija rotora i statora.

**Postupak numeričkog proračuna.** Iz polja tlaka i viskoznih naprezanja integriraju se sila, moment i snaga. Rezultat ovisi o domeni, mreži, vremenskom koraku, rubnim uvjetima i odabranim modelima turbulencije ili višefaznosti.

**Tipičan scenarij.** Simulacija može pokazati zone niskog tlaka i, uz izričito odabran višefazni model, procijeniti opseg parne faze. Sama po sebi ne dokazuje kavitacijsku otpornost ni vijek bez erozije; za takve zaključke trebaju verifikacija, odgovarajući eksperimentalni podatci i zaseban materijalni model [@nasa-cfd-vv; @asme-vv20-2009].

> *Nije gradivo MF1. Veza s ručnim računom ostaje bilanca momenta i snage, ali složeniji numerički model uvodi dodatne pretpostavke koje treba zasebno provjeriti.*
:::

::: {.mf1-zavrsni-okvir}
<p class="mf1-box-label">Za ponijeti iz poglavlja</p>

**Sažeta provjera prije računa**

- Prije pisanja jednadžbi nacrtaj kontrolni volumen i osi.
- Treba jasno razlikovati koju silu daje jednadžba količine gibanja: silu okoline na fluid ili silu fluida na okolinu.
- Treba rastaviti izlaznu brzinu na komponente u istom koordinatnom sustavu kao ulaznu.
- Maseni protok računaj iz površine i normalne brzine istoga presjeka, uz relativnu brzinu za pomičnu kontrolnu plohu.
- Treba razdvojiti silu fluida na vodilicu od reakcije nosača.

**Najčešća pogreška**

Najčešća pogreška nije u masenom protoku, nego u tome što se bez promjene predznaka uzme sila vodilice na fluid kao konačan odgovor. Taj korak treba uvijek jasno označiti prije iskazivanja konačnog rezultata.

**Nakon ovoga poglavlja mora biti moguće**

1. postaviti kontrolni volumen za mlaz i vodilicu.
2. iz promjene vektora brzine odrediti komponente sile, reakcije i osnovni moment u uklještenju.
3. koristiti istu bilancu količine gibanja kao osnovu za lopatice, moment i mlazni potisak.

**U tehnici to znači**

Peltonovo kolo, vodomlazni pogon i mlazna ispitna glava rade dobro samo ako je ispravno pročitano koliko količine gibanja fluid predaje lopatici ili konstrukciji. Iz iste jednadžbe zato ovdje proizlaze sila, moment, snaga i potisak, ovisno o tome što se promatra kao radni izlaz sustava.

**Granica modela**

Maksimalna sila nije isto što i maksimalna snaga, a idealizirana promjena vektora brzine nije dovoljna ako su važni gubitci u lopatici, neujednačen profil brzine ili složenija geometrija mlaza. U stvarnom stroju izbor kuta i brzine uvijek treba čitati zajedno s učinkovitošću, a ne samo sa silom.

<span class="mf1-ch-ref"><span class="mf1-ch-code">pog. 14</span><span class="mf1-ch-title">Turbostrojevi i propulzija</span></span> počinje kontrolnim volumenom, ne turbinom. Jasno čitanje promjene količine gibanja na mirnoj vodilici daje stabilnu osnovu i za reakcije nosača i za kasnije pokretne lopatice.
:::
