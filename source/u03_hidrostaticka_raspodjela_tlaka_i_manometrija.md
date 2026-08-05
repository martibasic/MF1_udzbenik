![Pregled poglavlja pog. 3: Hidrostatika, raspodjela tlaka i manometrija](../assets/print/u03_fig_uvod_pregled.svg){#fig-uvod-u03 fig-align="center" fig-alt="Pregled poglavlja pog. 3: Hidrostatika, raspodjela tlaka i manometrija"}

## Hidrostatika kao prvi inženjerski test modela

Hidrostatika je prvo poglavlje u kojem model odmah mora dati i mjerenje.

Cilj nije samo zapisati relaciju za tlak, nego učvrstiti radni postupak koji se ponavlja kroz spremnike, piezometre, U-manometre i diferencijalne manometre.

::: {.mf1-application}
<p class="mf1-box-label">Inženjerski kontekst</p>

Ista hidrostatska logika čita se na piezometru uz spremnik, na U-manometru ventilacijskog voda i na diferencijalnom manometru koji provjerava pad tlaka preko filtra ili izmjenjivača topline. U građevini i brodogradnji ta se slika širi na tlak vode po dubini u spremnicima, kesonima i balastnim tankovima, pa je manometrija ovdje instrumentacijski nastavak hidrostatike, a ne novo pravilo.
:::

::: {.mf1-priprema}
<p class="mf1-box-label">Prije čitanja poglavlja</p>

**Predznanje koje se pretpostavlja:**

- definicija tlaka i razlikovanje sile od tlaka iz poglavlja <span class="mf1-ch-ref"><span class="mf1-ch-code">pog. 1</span><span class="mf1-ch-title">Osnove fluida i Pascalov zakon</span></span>;
- diferencijalni i integralni račun jedne varijable (Matematika I);
- pojam gradijenta i derivacije po koordinati;
- razumijevanje gravitacijskog polja kao homogenog ubrzanja.

**Ishodi učenja:**

- izvesti diferencijalnu jednadžbu hidrostatike $\mathrm{d}p/\mathrm{d}z = -\rho g$ i njezin integralni oblik za konstantnu gustoću;
- pratiti tlak kroz sustav od više povezanih fluida bez gubljenja predznaka;
- razlikovati apsolutni, manometarski i vakuumski tlak te ih međusobno povezati;
- čitati i postaviti U-manometar i diferencijalni manometar.

**Procijenjeno vrijeme rada uz udžbenik:** 9 sati.
:::

## Fizikalni uvod i matematički izvod

Fluid u mirovanju ne može nositi smična naprezanja povezana sa strujanjem, ali i dalje nosi raspodjelu normalnog naprezanja, odnosno tlaka. Svaki sloj fluida mora držati težinu slojeva iznad sebe, pa tlak raste s dubinom.

Za mirujući fluid u jednolikom gravitacijskom polju osnovna lokalna relacija je

$$\frac{dp}{dz} = -\rho g$$ {#eq-hidrostatika-fizikalni-uvod-i-matematicki-izvod-01}

::: {.mf1-fizikalno-znacenje}
<p class="mf1-box-label">Fizikalno značenje</p>
Ova diferencijalna jednadžba kaže jednu jednostavnu stvar: lokalni gradijent tlaka uravnotežuje težinu fluida. Negativan predznak govori da, kad idemo prema gore ($z$ raste), tlak pada. Relacija $dp/dz=-\rho(z)g$ vrijedi i kada se gustoća mijenja s visinom; tada se samo ne smije iz integrala izvući konstantna $\rho$. Linearni porast $\rho gh$ poseban je slučaj približno konstantnih $\rho$ i $g$.
:::

Ako je gustoće moguće uzeti konstantnom, to prelazi u radni zapis

$$p_2 - p_1 = \rho g (z_1 - z_2)$$ {#eq-hidrostatika-fizikalno-znacenje-01}

ili, za dubinu mjerenu od slobodne površine,

$$p = p_0 + \rho g h$$ {#eq-hidrostatika-fizikalno-znacenje-02}

::: {.mf1-fizikalno-znacenje}
<p class="mf1-box-label">Fizikalno značenje</p>
Ovo je radna jednadžba hidrostatike: poznati tlak na slobodnoj površini ($p_0$), a zatim dodamo "težinski porast" $\rho g h$ za svaki metar dubine. Za vodu ($\rho \approx 1000\ \text{kg/m}^3$) svaki metar dubine donosi oko $9{,}81\ \text{kPa}$. Za živu ($\rho \approx 13600\ \text{kg/m}^3$) isti metar daje $\approx 133\ \text{kPa}$. Ista jednadžba vrijedi i unazad: iz poznatog tlaka u jednoj točki računa se tlak na svakoj drugoj visini u istom spojenom fluidu.
:::

::: {.callout-note collapse="true" icon="false"}
## Numerički trag

Hidrostatska raspodjela $p=p_0+\rho gh$ prirodno je početno i referentno polje u mnogim numeričkim modelima s gravitacijom. Često se rješava modificirani tlak iz kojega je izdvojen poznati gravitacijski potencijal, ali definicija ovisi o koordinatnom sustavu, gustoći i odabranoj referenci. Ovdje se $h$ rabi kao pozitivna dubina, pa se zapis ne smije prepisati bez provjere predznaka.
:::

Ključno je da se ova relacija ne koristi mehanički. Diferencijalna jednadžba ovdje nije samo simboličan zapis, nego sažima jednu vrlo jednostavnu sliku: svaki niži sloj nosi težinu slojeva iznad sebe. Zato prije računa treba odrediti koji je tlak poznat, gdje je referentna točka i kojim se putem prolazi kroz fluid.

## Matematički izvod

Promatra se tanki horizontalni sloj mirujućega fluida površine $A$ i debljine $dz$. Os $z$ usmjerena je prema gore. Na donju plohu djeluje tlak $p(z)A$ prema gore, na gornju plohu tlak $p(z + dz)A$ prema dolje, a dodatno prema dolje djeluje težina sloja $\rho g A dz$. Budući da je fluid u mirovanju, zbroj vertikalnih sila mora biti jednak nuli:

$$
p(z)A - p(z + dz)A - \rho g A dz = 0.
$$ {#eq-hidrostatika-matematicki-izvod-01}

Kako je za mali pomak $dz$ moguće pisati $p(z + dz) = p(z) + dp$, uvrštavanjem slijedi

$$
p(z)A - [p(z) + dp]A - \rho g A dz = 0,
$$ {#eq-hidrostatika-matematicki-izvod-02}

odnosno nakon skraćivanja s $A$

$$
-dp - \rho g dz = 0.
$$ {#eq-hidrostatika-matematicki-izvod-03}

Time se dobiva diferencijalni zakon hidrostatike

$$
\frac{dp}{dz} = -\rho g.
$$ {#eq-hidrostatika-matematicki-izvod-04}

Negativan predznak samo kaže da tlak opada kad se ide prema gore, odnosno raste kad se ide prema dolje. Ako je gustoća homogena i može se smatrati konstantnom, jednadžba se integrira između dviju točaka 1 i 2:

$$
\int_{p_1}^{p_2} dp = -\rho g \int_{z_1}^{z_2} dz,
$$ {#eq-hidrostatika-matematicki-izvod-05}

pa slijedi

$$
p_2 - p_1 = -\rho g (z_2 - z_1) = \rho g (z_1 - z_2).
$$ {#eq-hidrostatika-matematicki-izvod-06}

::: {.callout-note}
## Razrada koraka
Korak: integrirani oblik s $z$ → praktični zapis s dubinom $h$

Neka je $z_1$ visina slobodne površine i $z_2$ visina promatrane točke (niže, dakle $z_2 < z_1$). Tada je $h = z_1 - z_2 > 0$ upravo dubina promatrane točke ispod slobodne površine. Uvrstimo u integrirani oblik:
$$
p_2 - p_1 = \rho g (z_1 - z_2) = \rho g h.
$$ {#eq-hidrostatika-razrada-koraka-01}
Ako je $p_1 = p_0$ (tlak na slobodnoj površini), dobivamo:
$$
p_2 = p_0 + \rho g h.
$$ {#eq-hidrostatika-razrada-koraka-02}
Promjena konvencije: $z$ je koordinata prema gore, $h$ je dubina prema dolje. Oba zapisa su ekvivalentni, ali $h$ je pozitivan prema dolje pa je oblik s $h$ intuitivniji za hidrostatička izračunavanja.
:::

Ako se umjesto koordinate $z$ uvede dubina $h$ mjerena prema dolje od poznate slobodne površine, dobiva se praktični zapis

$$
p = p_0 + \rho gh.
$$ {#eq-hidrostatika-razrada-koraka-03}

U tom konačnom obliku $p_0$ je referentni tlak na slobodnoj površini, a član $\rho gh$ hidrostatički porast tlaka zbog težine stupca fluida iznad promatrane točke.

::: {.mf1-izvod}
<p class="mf1-box-label">Matematički izvod — Vektorska generalizacija Eulerove jednadžbe hidrostatike</p>

Promatra se infinitezimalni kvadar fluida dimenzija $dx \times dy \times dz$ s težištem u točki $(x, y, z)$. Na njega djeluje težina i sile tlaka po svim šest plohama. Sila tlaka na lijevu plohu (okomita na os $x$) iznosi $p(x - dx/2)\,dy\,dz$ u smjeru $+x$, a na desnu $-p(x + dx/2)\,dy\,dz$ u smjeru $-x$. Neto sila po osi $x$ je

$$
dF_x = -\frac{\partial p}{\partial x}\,dx\,dy\,dz = -\frac{\partial p}{\partial x}\,dV.
$$ {#eq-hidrostatika-matematicki-izvod-vektorska-generalizacija-euler-01}

Analogno za osi $y$ i $z$. Ako je gravitacija usmjerena prema $-z$ ($\vec{g} = -g\hat{z}$), težina kvadra djeluje samo po osi $z$: $dG_z = -\rho g\,dV$.

Ravnoteža sila u mirujućem fluidu daje tri komponente

$$
\frac{\partial p}{\partial x} = 0, \qquad \frac{\partial p}{\partial y} = 0, \qquad \frac{\partial p}{\partial z} = -\rho g,
$$ {#eq-hidrostatika-matematicki-izvod-vektorska-generalizacija-euler-02}

što se može sažeti u vektorski oblik

$$
\nabla p = \rho \vec{g}.
$$ {#eq-hidrostatika-matematicki-izvod-vektorska-generalizacija-euler-03}

Ova vektorska Eulerova jednadžba hidrostatike vrijedi u mirujućem fluidu. U ovdje pretpostavljenom jednolikom gravitacijskom polju bez drugih volumnih sila pojedinačne komponente pokazuju da tlak ovisi **samo o visini** $z$, pa su plohe konstantnog tlaka horizontalne ravnine. U općenitom polju volumnih sila izobare ne moraju biti horizontalne. U <span class="mf1-ch-ref"><span class="mf1-ch-code">pog. 4</span><span class="mf1-ch-title">Relativno mirovanje fluida</span></span> gravitacija se za jednoliko ubrzani sustav zamjenjuje efektivnim poljem $\vec{g}_{eff}=\vec{g}-\vec{a}$.
:::

::: {.mf1-izvod}
<p class="mf1-box-label">Matematički izvod — Izotermalna atmosfera i karakteristična visina</p>

Pretpostavka konstantne gustoće $\rho$ vrijedi za tekućine (voda, ulje, živa), ali ne za plinove u kojima se gustoća mijenja s tlakom i temperaturom. Za **izotermalnu atmosferu** uz pretpostavku $T = T_0$ = konst. može se izvesti raspodjela tlaka po visini.

Iz jednadžbe stanja idealnog plina vrijedi

$$
p = \rho R T_0 \quad\Longrightarrow\quad \rho = \frac{p}{R T_0},
$$ {#eq-hidrostatika-matematicki-izvod-izotermalna-atmosfera-i-karakt-01}

gdje je $R$ specifična plinska konstanta za zrak ($R \approx 287\ \text{J/(kg K)}$). Uvrštenjem u hidrostatsku jednadžbu $dp/dz = -\rho g$ slijedi

$$
\frac{dp}{dz} = -\frac{p\,g}{R T_0},
$$ {#eq-hidrostatika-matematicki-izvod-izotermalna-atmosfera-i-karakt-02}

što je obična diferencijalna jednadžba prvog reda u kojoj se varijable mogu razdvojiti:

$$
\frac{dp}{p} = -\frac{g}{R T_0}\,dz \quad\Longrightarrow\quad \ln p = -\frac{g}{R T_0}\,z + C.
$$ {#eq-hidrostatika-matematicki-izvod-izotermalna-atmosfera-i-karakt-03}

Uz početni uvjet $p(0) = p_0$ na razini mora dobiva se

$$
\boxed{p(z) = p_0\,\exp\!\left(-\frac{z}{H}\right), \qquad H = \frac{R T_0}{g}}.
$$ {#eq-hidrostatika-matematicki-izvod-izotermalna-atmosfera-i-karakt-04}

Veličina $H$ naziva se **karakteristična visina atmosfere**. Za $T_0 = 288\ \text{K}$ (standardna prizemna temperatura) i $g = 9{,}81\ \text{m/s}^2$ slijedi

$$
H = \frac{287 \cdot 288}{9{,}81} \approx 8400\ \text{m} \approx 8{,}4\ \text{km}.
$$ {#eq-hidrostatika-matematicki-izvod-izotermalna-atmosfera-i-karakt-05}

U ovom izotermalnom modelu tlak pada za faktor $e\approx2{,}72$ nakon porasta visine za jednu skalnu visinu, ovdje oko $8{,}4\ \text{km}$. Na $z\approx8{,}8\ \text{km}$ model daje oko $35\ \text{kPa}$, odnosno približno trećinu tlaka na razini mora. Stvarna atmosfera nije izotermalna: za pouzdan atmosferski podatak koristi se odgovarajući standardni ili izmjereni profil temperature i tlaka, dok je ovaj izvod samo model reda veličine [@anderson2021].
:::

## Otvoreni i zatvoreni spremnici

Kod otvorenog spremnika tlak na slobodnoj površini jednak je atmosferskom tlaku. Zato je često praktično prijeći na manometarski tlak i atmosferu uzeti kao nultu razinu.

Kod zatvorenog spremnika to više nije automatski dopušteno. Ako je tlak na slobodnoj površini različit od atmosferskog, onda raspodjela nije samo $\rho g h$, nego

$$p = p_{pov} + \rho g h$$ {#eq-hidrostatika-otvoreni-i-zatvoreni-spremnici-01}

Najčešća greška ovdje nije u računu, nego u tome što se atmosfera mehanički uzme kao nula i kad za to nema fizikalnog opravdanja.

Iz manometarskog tlaka $p_M$ (indeks $M$ = manometarski; ista oznaka koristi se u ostatku udžbenika) odmah se može čitati i piezometarska visina

$$
h_p = \frac{p_M}{\rho g},
$$ {#eq-hidrostatika-otvoreni-i-zatvoreni-spremnici-02}

::: {.mf1-fizikalno-znacenje}
<p class="mf1-box-label">Fizikalno značenje</p>
Piezometarska visina je geometrijska reprezentacija tlaka: do koje bi visine voda (ili drugi fluid) narasla u otvorenoj cjevčici pričvršćenoj na to mjesto. Manometarski pretlak od $10\ \text{kPa}$ u vodi odgovara piezometarskoj visini oko $1{,}02\ \text{m}$. Piezometri zato daju izravno i pregledno mjerenje u spremnicima, geotehničkim istraživanjima i distribucijskim mrežama kada su ispunjeni njihovi mjerni uvjeti.
:::

odnosno visina stupca istoga fluida koji bi odgovarao tom pretlaku. Upravo zato piezometar nije novo pravilo, nego geometrijsko očitanje već postojećeg hidrostatskog tlaka.

Manometar nije novi zakon fizike, nego instrumentacijski zapis iste hidrostatske ravnoteže kroz više spojenih stupaca fluida. U praksi je dovoljno držati se jednoga slijeda: odabrati jednu referentnu točku ili jednu poznatu vrijednost tlaka, kretati se kroz stupce fluida jednim dosljednim smjerom, pri silasku dodavati $\rho g \Delta h$, pri penjanju oduzimati isti član te na istoj horizontalnoj razini istog mirujućeg fluida izjednačiti tlak.

::: {.mf1-interaktivno}
<p class="mf1-box-label">Interaktivni prikaz — Diferencijalni manometar</p>

Interaktivni prikaz omogućuje mijenjanje gustoća radnog i manometarskog fluida te razlike visine očitanja $\Delta h$ uz neposredno praćenje izmjerene razlike tlakova. Shema U-manometra vizualizira odnos između razlike visina i razlike gustoća.

<div class="mf1-interaktivno-akcija">
<a class="mf1-interaktivno-veza" href="https://martibasic.github.io/MF1_udzbenik/jlite/lab/index.html?path=u03_diferencijalni_manometar.ipynb">Pokreni u pregledniku</a>
<a class="mf1-interaktivno-veza" href="https://colab.research.google.com/github/martibasic/MF1_udzbenik/blob/main/notebooks/u03_diferencijalni_manometar.ipynb" target="_blank" rel="noopener">Pričuvno: otvori u Colabu</a>
<img class="mf1-interaktivno-qr" src="../assets/qr/u03_diferencijalni_manometar.svg" alt="QR kod za interaktivni prikaz diferencijalnog manometra"/>
</div>

<div class="mf1-interaktivno-pitanja">
**Pitanja za samostalno istraživanje:** (a) Što se događa s mjerenjem kada se gustoće dvaju fluida približe? (b) Zašto se za male razlike tlakova bira manometarski fluid bliže gustoći radnog fluida? (c) Kako se osnovna formula proširuje na manometarski put kroz tri fluida različitih gustoća?
</div>
:::

Ako se usred rješenja promijeni referentni smjer ili se preskoči promjena fluida, gotovo je sigurno da će predznaci otići u krivom smjeru.

Jednako je važno stalno razlikovati apsolutni, manometarski i vakuumski tlak: apsolutni se mjeri u odnosu na idealni vakuum, manometarski u odnosu na lokalni atmosferski tlak, a vakuumski opisuje koliko je apsolutni tlak ispod atmosferskoga.

Veza je uvijek

$$p_{aps} = p_{atm} + p_M$$ {#eq-hidrostatika-interaktivni-prikaz-diferencijalni-manometar-01}

::: {.mf1-fizikalno-znacenje}
<p class="mf1-box-label">Fizikalno značenje</p>
Apsolutni tlak referira se na idealni vakuum ($p=0$), dok je manometarski tlak razlika prema lokalnom atmosferskom tlaku. Vakuumski tlak opisuje koliko je apsolutni tlak ispod atmosferskoga ($p_{vak}=p_{atm}-p_{aps}$). Negativan rezultat za apsolutni tlak u uobičajenom modelu kapljevine ili plina nije „veći podtlak”, nego znak da su pretpostavke računa napuštene; kavitacijski se kriterij pritom uspoređuje s tlakom zasićene pare, a ne s nulom. Zamjena referenci jedna je od najtipičnijih pogrešaka u manometriji.
:::

pa za podtlak vrijedi i relacija

$$p_{vak} = p_{atm} - p_{aps} = -p_M \qquad (p_M<0)$$ {#eq-hidrostatika-fizikalno-znacenje-03}

Ako je $p_M < 0$, to ne znači da je tlak "negativan" u apsolutnom smislu, nego da je sustav pod podtlakom u odnosu na okolinu.

## Riješeni primjeri

::: {#ex-u03-tlak-u-prikljucku-zatvorenog-vodenog-spremnika-t1 .mf1-we}
<p class="mf1-box-label">Riješeni primjer — Tlak u priključku zatvorenog vodenog spremnika&nbsp;<span class="mf1-level">T1</span></p>

**Kontekst:** Zatvoreni spremnik ima pretlak u plinskom prostoru iznad vode, a priključna točka nalazi se na zadanoj dubini ispod slobodne površine. Treba odrediti apsolutni i manometarski tlak u plinskom prostoru i u priključku.

**Zadano**

- Gustoća vode: $\rho = 998\ \text{kg/m}^3$
- Manometarski tlak u plinskom prostoru: $p_{G,m} = 18\ \text{kPa}$
- Dubina priključne točke `A` ispod slobodne površine: $h = 1{,}40\ \text{m}$
- Lokalni atmosferski tlak: $p_{atm} = 100{,}8\ \text{kPa}$

**Traženo**

1. apsolutni tlak u plinskom prostoru spremnika.
2. apsolutni tlak u točki `A`.
3. manometarski tlak u točki `A`.

![Tlak u priključku zatvorenog vodenog spremnika (p_G=18 kPa, h=1,4 m)](../assets/print/u03_fig_zatvoreni_spremnik_tlak.svg){#fig-u03-zatvoreni-spremnik-tlak fig-align="center" fig-alt="Tlak u priključku zatvorenog vodenog spremnika (p_G=18 kPa, h=1,4 m)"}

**Pretpostavke i model**

Najprije treba zatvoriti tlak na slobodnoj površini. Tek se zatim kroz isti mirujući fluid silazi do točke `A` i dodaje hidrostatički doprinos $\rho g h$.

**Rješenje**

Apsolutni tlak u plinskom prostoru jednak je

$$
p_G = p_{atm} + p_{G,m} = 100{,}8 + 18{,}0 = 118{,}8\ \text{kPa} = 118800\ \text{Pa}.
$$ {#eq-hidrostatika-rijeseni-primjer-tlak-u-prikljucku-zatvorenog-vo-01}

Tlak u točki `A` dobiva se silaskom kroz vodu za dubinu $h$:

$$
p_A = p_G + \rho g h = 118800 + 998 \cdot 9{,}81 \cdot 1{,}40 = 132512\ \text{Pa} \approx 132{,}5\ \text{kPa}.
$$ {#eq-hidrostatika-rijeseni-primjer-tlak-u-prikljucku-zatvorenog-vo-02}

Manometarski tlak u točki `A` zato iznosi

$$
p_{A,m} = p_A - p_{atm} = 132512 - 100800 = 31712\ \text{Pa} \approx 31{,}7\ \text{kPa}.
$$ {#eq-hidrostatika-rijeseni-primjer-tlak-u-prikljucku-zatvorenog-vo-03}

**Provjera i komentar**

1. Tlak u točki `A` mora biti veći od tlaka u plinskom prostoru jer se do točke ide prema dolje kroz vodu.
2. Manometarski tlak u točki `A` mora biti veći od manometarskog tlaka plinskog prostora za iznos hidrostatičkog doprinosa vode.
3. Apsolutni tlak mora ostati pozitivan i veći od lokalnog atmosferskog tlaka.
:::

::: {#ex-u03-diferencijalni-manometar-izme-u-slatke-i-morske .mf1-we}
<p class="mf1-box-label">Riješeni primjer — Diferencijalni manometar između slatke i morske vode&nbsp;<span class="mf1-level">T3</span></p>

**Kontekst:** Dva paralelna horizontalna voda - jedan sa slatkom, drugi s morskom vodom - spojena su diferencijalnim manometrom sa živom i malim stupcem zraka. Treba odrediti razliku tlakova i procijeniti pogrešku zbog zanemarivanja zraka.

**Zadano**

- Gustoća slatke vode: $\rho_v = 1000\ \text{kg/m}^3$
- Gustoća morske vode: $\rho_{mv} = 1035\ \text{kg/m}^3$
- Gustoća žive: $\rho_{Hg} = 13600\ \text{kg/m}^3$
- Gustoća zraka: $\rho_{zr} = 1{,}2\ \text{kg/m}^3$
- Silazak od $p_1$ do lijeve granice voda-živa: $h_1 = 0{,}60\ \text{m}$
- Uspon između dviju razina žive: $h_2 = 0{,}10\ \text{m}$
- Visina malog stupca zraka: $h_3 = 0{,}70\ \text{m}$
- Silazak od desne granice do $p_2$ kroz morsku vodu: $h_4 = 0{,}40\ \text{m}$

**Traženo**

1. razliku tlakova $p_1 - p_2$.
2. kolika je pogreška ako se stupac zraka zanemari.

![diferencijalni manometar](../assets/print/u03_val1_diferencijalni_manometar.svg){#fig-u03-diferencijalni-manometar fig-alt="diferencijalni manometar"}

**Pretpostavke i model**

Najsigurniji pristup nije pamtiti gotovu formulu, nego pratiti tlak od jedne poznate točke do druge. Na svakom segmentu treba samo dosljedno zapisati raste li tlak ili pada i koji fluid taj segment pripada.

**Rješenje**

Krenimo od tlaka $p_1$ u lijevom vodu i pratimo sustav do tlaka $p_2$ u desnom vodu.

Ako se stupac zraka zanemari, radni zapis glasi:

1. idem dolje kroz slatku vodu: $+\rho_v g h_1$.
2. idem gore kroz živu: $-\rho_{Hg} g h_2$.
3. idem dolje kroz morsku vodu: $+\rho_{mv} g h_4$.

Zato vrijedi

$$
p_1 + \rho_v g h_1 - \rho_{Hg} g h_2 + \rho_{mv} g h_4 = p_2 \quad \Longrightarrow \quad p_1 - p_2 = g\left(\rho_{Hg} h_2 - \rho_{mv} h_4 - \rho_v h_1\right).
$$ {#eq-hidrostatika-rijeseni-primjer-diferencijalni-manometar-izme-u-01}

Uvrstavanjem podataka:

$$
p_1 - p_2 = 9{,}81\left(13600 \cdot 0{,}10 - 1035 \cdot 0{,}40 - 1000 \cdot 0{,}60\right) = 3394\ \text{Pa} \approx 3{,}39\ \text{kPa}.
$$ {#eq-hidrostatika-rijeseni-primjer-diferencijalni-manometar-izme-u-02}

Sada uključimo i mali stupac zraka. Tada se pri prolazu prema gore kroz zrak tlak još dodatno smanjuje za $\rho_{zr} g h_3$, pa vrijedi

$$
p_1 + \rho_v g h_1 - \rho_{Hg} g h_2 - \rho_{zr} g h_3 + \rho_{mv} g h_4 = p_2 \quad \Longrightarrow \quad p_1 - p_2 = g\left(\rho_{Hg} h_2 + \rho_{zr} h_3 - \rho_{mv} h_4 - \rho_v h_1\right).
$$ {#eq-hidrostatika-rijeseni-primjer-diferencijalni-manometar-izme-u-03}

Numerički:

$$
p_1 - p_2 = 9{,}81\left(13600 \cdot 0{,}10 + 1{,}2 \cdot 0{,}70 - 1035 \cdot 0{,}40 - 1000 \cdot 0{,}60\right) = 3402\ \text{Pa} \approx 3{,}40\ \text{kPa}.
$$ {#eq-hidrostatika-rijeseni-primjer-diferencijalni-manometar-izme-u-04}

Pogreška zanemarivanja zraka zato iznosi $\Delta p = 3402 - 3394 = 8\ \text{Pa}$, a relativna pogreška je

$$
\delta = \frac{8}{3402} \cdot 100\% \approx 0{,}24\%.
$$ {#eq-hidrostatika-rijeseni-primjer-diferencijalni-manometar-izme-u-05}

**Provjera i komentar**

U ovom zadatku tlak u lijevom vodu veći je od tlaka u desnom vodu za otprilike $3{,}4\ \text{kPa}$. Stupac zraka daje vrlo mali doprinos, pa je njegovo zanemarivanje ovdje inženjerski prihvatljivo.

1. Doprinos žive mora biti dominantan jer ima daleko najveću gustoću.
2. Doprinos zraka mora biti vrlo malen u odnosu na doprinose tekućina, što i brojčano dobivamo.
3. Ako se tijekom računa izgubi redoslijed prolaza kroz fluide, gotovo sigurno će se pojaviti pogrešan predznak ispred jednog od članova.
:::

Nakon otvorenih spremnika i diferencijalnog manometra treba zatvoriti još jedan osnovni tip čitanja: kako se iz vakuummetra ili otvorenog U-manometra vraća apsolutni tlak u plinskom prostoru, a zatim i tlak u tekućini ispod njega.

::: {#ex-u03-zatvoreni-vodeni-spremnik-s-uljnim-referentnim-spremnikom .mf1-ch}
<p class="mf1-box-label">Cjeloviti zadatak — Zatvoreni vodeni spremnik s uljnim referentnim spremnikom i živinim manometrom&nbsp;<span class="mf1-level">T3</span></p>

**Kontekst:** U procesnoj postaji zatvoreni vodeni spremnik povezan je diferencijalnim živinim manometrom s otvorenim uljnim referentnim spremnikom. Treba odrediti tlakove u priključnim točkama i u plinskom prostoru te ocijeniti je li sustav pod pretlakom ili podtlakom u odnosu na atmosferu.

**Zadano**

- Gustoća vode u zatvorenom spremniku `A`: $\rho_w = 1000\ \text{kg/m}^3$
- Dubina priključne točke `1` ispod slobodne površine vode: $h_1 = 0{,}80\ \text{m}$
- Gustoća ulja u otvorenom referentnom spremniku `B`: $\rho_o = 850\ \text{kg/m}^3$
- Dubina priključne točke `2` ispod slobodne površine ulja: $h_2 = 0{,}55\ \text{m}$
- Atmosferski tlak iznad ulja u `B`: $p_0 = 101325\ \text{Pa}$
- Gustoća žive u diferencijalnom U-manometru: $\rho_{Hg} = 13600\ \text{kg/m}^3$
- Visina vodenog stupca u lijevom kraku (točka `1` do granice voda-živa): $a = 0{,}30\ \text{m}$
- Visina uljnog stupca u desnom kraku (točka `2` do granice ulje-živa): $b = 0{,}25\ \text{m}$
- Razlika razina žive (lijevi krak niži od desnog za): $\Delta h = 0{,}18\ \text{m}$
- Dubina točke `C` u spremniku `A` ispod slobodne površine vode: $h_C = 1{,}20\ \text{m}$

**Traženo**

1. tlakove u priključnim točkama $p_1$ i $p_2$ te njihovu razliku.
2. apsolutni i manometarski tlak u plinskom prostoru spremnika `A`.
3. apsolutni i manometarski tlak u točki `C`.
4. protumači jesu li plinski prostor i točka `C` pod pretlakom ili podtlakom u odnosu na atmosferu.

Zanemari gustoće plinova u spojnim cijevima.

![zatvoreni vodeni spremnik i referentni uljni spremnik](../assets/print/u03_ch1_zatvoreni_spremnik_ulje_ziva.svg){#fig-u03-zatvoreni-vodeni-spremnik-i-referentni-uljni-spremnik fig-alt="zatvoreni vodeni spremnik i referentni uljni spremnik"}

**Pretpostavke i model**

Najsigurniji pristup i dalje nije pamtiti gotov izraz, nego tlak pratiti po segmentima. U otvorenom spremniku `B` tlak u točki `2` vraća se iz atmosfere i uljnog stupca. Zatim se preko diferencijalnog manometra dobije tlak u točki `1`, a tek se nakon toga iz točke `1` penje prema plinskom prostoru `A` ili silazi prema dubljoj točki `C`.

**Rješenje**

### 1. Tlak u točki `2` i relacija manometra

Kako je spremnik `B` otvoren, tlak u njegovoj slobodnoj površini jednak je atmosferskom. Zato je tlak u točki `2`

$$
p_2 = p_0 + \rho_o g h_2 = 101325 + 850 \cdot 9{,}81 \cdot 0{,}55 = 105911\ \text{Pa} \approx 105{,}9\ \text{kPa}.
$$ {#eq-hidrostatika-1-tlak-u-tocki-2-i-relacija-01}

Sada krenimo od točke `1` prema točki `2` kroz manometar:

1. prema dolje kroz vodu visine $a$ tlak raste za $\rho_w g a$.
2. kroz živu se ide prema gore za visinsku razliku $\Delta h$, pa tlak pada za $\rho_{Hg} g \Delta h$.
3. prema gore kroz ulje visine $b$ tlak pada za $\rho_o g b$.

Zato vrijedi

$$
p_1 + \rho_w g a - \rho_{Hg} g \Delta h - \rho_o g b = p_2,
$$ {#eq-hidrostatika-1-tlak-u-tocki-2-i-relacija-02}

odnosno

$$
p_1 = p_2 - \rho_w g a + \rho_{Hg} g \Delta h + \rho_o g b = 105911 - 1000 \cdot 9{,}81 \cdot 0{,}30 + 13600 \cdot 9{,}81 \cdot 0{,}18 + 850 \cdot 9{,}81 \cdot 0{,}25 = 129068\ \text{Pa} \approx 129{,}1\ \text{kPa}.
$$ {#eq-hidrostatika-1-tlak-u-tocki-2-i-relacija-03}

Razlika tlakova zato je

$$
p_1 - p_2 = 129068 - 105911 = 23157\ \text{Pa} \approx 23{,}16\ \text{kPa}.
$$ {#eq-hidrostatika-1-tlak-u-tocki-2-i-relacija-04}

#### 2. Tlak u plinskom prostoru spremnika `A`

U spremniku `A` točka `1` nalazi se na dubini $h_1$ ispod slobodne površine vode, pa iz $p_1 = p_G + \rho_w g h_1$ slijedi

$$
p_G = p_1 - \rho_w g h_1 = 129068 - 1000 \cdot 9{,}81 \cdot 0{,}80 = 121220\ \text{Pa} \approx 121{,}2\ \text{kPa}.
$$ {#eq-hidrostatika-2-tlak-u-plinskom-prostoru-spremnika-a-01}

Manometarski tlak plinskog prostora iznosi

$$
p_{G,m} = p_G - p_0 = 121220 - 101325 = 19895\ \text{Pa} \approx 19{,}9\ \text{kPa}.
$$ {#eq-hidrostatika-2-tlak-u-plinskom-prostoru-spremnika-a-02}

#### 3. Tlak u točki `C`

Točka `C` nalazi se dublje od slobodne površine za $h_C = 1{,}20\ \text{m}$, pa je njezin apsolutni tlak

$$
p_C = p_G + \rho_w g h_C = 121220 + 1000 \cdot 9{,}81 \cdot 1{,}20 = 132992\ \text{Pa} \approx 133{,}0\ \text{kPa}.
$$ {#eq-hidrostatika-3-tlak-u-tocki-c-01}

Manometarski tlak u točki `C` jest

$$
p_{C,m} = p_C - p_0 = 132992 - 101325 = 31667\ \text{Pa} \approx 31{,}7\ \text{kPa}.
$$ {#eq-hidrostatika-3-tlak-u-tocki-c-02}

#### 4. Tumačenje stanja

Kako je i $p_{G,m} > 0$ i $p_{C,m} > 0$, slijedi da su i plinski prostor i točka `C` pod pretlakom u odnosu na atmosferu. Točka `C` je pod većim pretlakom jer se nalazi dublje u vodi.

**Provjera i komentar**

Otvoreni uljni spremnik daje u točki `2` tlak oko $105{,}9\ \text{kPa}$, a diferencijalni manometar pokazuje da je tlak u točki `1` veći za oko $23{,}16\ \text{kPa}$. Iz toga slijedi da je apsolutni tlak plinskog prostora zatvorenog spremnika oko $121{,}2\ \text{kPa}$, odnosno da je spremnik pod manometarskim pretlakom od oko $19{,}9\ \text{kPa}$. U dubljoj točki `C` tlak dodatno raste na oko $133{,}0\ \text{kPa}$, odnosno na oko $31{,}7\ \text{kPa}$ manometarski.

1. Niža razina žive u lijevom kraku mora značiti da je tlak na lijevoj strani manometra veći.
2. Tlak u točki `1` mora biti veći od tlaka u plinskom prostoru jer se do nje dolazi silaskom kroz vodu.
3. Tlak u točki `C` mora biti veći od tlaka u plinskom prostoru i veći od tlaka u točki `1`, jer je `C` najdublja promatrana točka u vodi.
:::

Kao prijelaz prema <span class="mf1-ch-ref"><span class="mf1-ch-code">pog. 4</span><span class="mf1-ch-title">Relativno mirovanje fluida</span></span> korisno je usporediti ravnotežu tlaka u spojenim posudama s idejom efektivnog polja sila.

![statička zamjena za ravnotežu tlaka i efektivno polje sila](../assets/print/u03_balans_tlaka_i_geff.svg){#fig-u03-staticka-zamjena-za-ravnotezu-tlaka-i-efektivno fig-alt="statička zamjena za ravnotežu tlaka i efektivno polje sila"}

::: {#ex-u03-tlak-na-usisu-pumpe-za-cirkulaciju-ulja .mf1-we}
<p class="mf1-box-label">Riješeni primjer — Tlak na usisu pumpe za cirkulaciju ulja &nbsp;<span class="mf1-level">T2</span></p>

**Primjer za strojare**

**Kontekst:** U hidrauličnom sustavu preše pumpa za cirkulaciju ulja smještena je 2,4 m iznad razine ulja u otvorenom spremniku. Pumpa aspirira ulje podtlakom na svom usisu.

**Zadano**

- Visina pumpe iznad razine ulja: $H = 2{,}40\ \text{m}$
- Gustoća hidrauličnog ulja: $\rho = 870\ \text{kg/m}^3$
- Lokalni atmosferski tlak: $p_{atm} = 101{,}3\ \text{kPa}$

**Traženo**

1. Manometarski tlak na usisu pumpe.
2. Apsolutni tlak na usisu pumpe.
3. Odredi statičku gornju granicu visine stupca pri kojoj bi apsolutni tlak pao na zadani tlak pare $p_v \approx 200\ \text{Pa}$.

![Tlak na usisu pumpe za cirkulaciju ulja (H=2,4 m iznad razine, ρ=870 kg/m³)](../assets/print/u03_fig_pumpa_usis.svg){#fig-u03-pumpa-usis fig-align="center" fig-alt="Tlak na usisu pumpe za cirkulaciju ulja (H=2,4 m iznad razine, ρ=870 kg/m³)"}

**Pretpostavke i model**

Promatra se idealna granica bez protoka: zanemaruju se brzinska visina i svi gubici u usisnom vodu. Slobodna površina ulja u spremniku je na atmosferskom tlaku. Ovaj hidrostatski model nije dovoljan za provjeru usisa pumpe u radu.

**Rješenje**

Manometarski tlak na usisu pumpe (uspon od slobodne površine za $H$):

$$
p_M = -\rho g H = -870 \cdot 9{,}81 \cdot 2{,}40 = -20{,}49 \cdot 10^3\ \text{Pa}
$$ {#eq-hidrostatika-rijeseni-primjer-tlak-na-usisu-pumpe-za-01}

$$
p_M \approx -20{,}5\ \text{kPa}
$$ {#eq-hidrostatika-rijeseni-primjer-tlak-na-usisu-pumpe-za-02}

Apsolutni tlak na usisu:

$$
p_{aps} = p_{atm} + p_M = 101300 - 20490 = 80810\ \text{Pa} \approx 80{,}8\ \text{kPa}
$$ {#eq-hidrostatika-rijeseni-primjer-tlak-na-usisu-pumpe-za-03}

Statička granična visina stupca pri $p_{aps}=p_v$:

$$
H_{max} = \frac{p_{atm} - p_v}{\rho g} = \frac{101300 - 200}{870 \cdot 9{,}81} = \frac{101100}{8534} \approx 11{,}8\ \text{m}
$$ {#eq-hidrostatika-rijeseni-primjer-tlak-na-usisu-pumpe-za-04}

**Provjera i komentar**

U idealnoj statičkoj slici točka na visini $2{,}4\ \text{m}$ ima apsolutni tlak $80{,}8\ \text{kPa}$, a $11{,}8\ \text{m}$ samo je gornja granica stupca pri nultom protoku. Za pumpu u radu treba bilancu energije s brzinom i gubicima te usporedbu raspoložive neto pozitivne usisne visine $NPSH_A$ s proizvođačevim zahtjevom $NPSH_R$ za zadani protok, brzinu vrtnje i fluid. Zato se iz ovoga računa ne može propisati opća „sigurna usisna visina”.

:::

::: {#ex-u03-balastni-tank-broda-tlak-iznutra-i-izvana .mf1-we}
<p class="mf1-box-label">Riješeni primjer — Balastni tank broda: tlak iznutra i izvana &nbsp;<span class="mf1-level">T2</span></p>

**Primjer za strojare**

**Kontekst:** Brod nosi balastne tankove pri dnu trupa, koji se za prazno povratno putovanje pune slatkom (ili morskom) vodom radi stabilnosti, a pri teretnom putovanju se prazne. Stijenka tanka istovremeno odvaja **vanjsku** morsku vodu (koja pritišće prema unutra) od **unutarnje** balastne vode (koja pritišće prema van). Brodski strojar dimenzionira stijenku tanka prema **neto tlaku** – razlici dvaju hidrostatskih tlakova na istoj dubini – jer ona definira u koju stranu stijenka biva opterećena i koje je opterećenje veće (prazan vs pun tank).

**Zadano**

Brod plovi mirnom morskom vodom. Promatra se balastni tank u sredini trupa:

- Gaz broda (dubina kobilice ispod morske razine): $T_g = 8{,}5\ \text{m}$
- Visina tanka mjerena od dna broda prema gore: $H_t = 5{,}0\ \text{m}$
- Promatračev prozor postavljen je na visini $h_p = 2{,}0\ \text{m}$ iznad dna tanka
- Gustoća morske vode: $\rho_m = 1025\ \text{kg/m}^3$
- Gustoća balastne (slatke) vode: $\rho_b = 1000\ \text{kg/m}^3$
- Vrh tanka spojen je s atmosferom kroz odzračnik, pa je slobodna površina balasta na atmosferskom tlaku
- $g = 9{,}81\ \text{m/s}^2$

**Traženo**

Razmotrite dva stanja: **(A) tank pun** balastne vode do vrha; **(B) tank prazan**.

1. Manometarski tlak vanjske morske vode na razini **dna tanka**.
2. Manometarski tlak balastne vode na razini dna tanka (stanje A).
3. Neto manometarski tlak na dno tanka u stanju A i u stanju B; u oba slučaja navedite smjer u kojem stijenka biva tlačena.
4. Neto manometarski tlak na **promatračev prozor** u stanju A.

![Balastni tank u trupu broda na gazu $T_g = 8{,}5$ m: vanjska morska voda i unutarnja balastna voda do visine $H_t = 5{,}0$ m. Prozor je na $h_p = 2$ m iznad dna tanka.](../assets/print/u03_fig_balastni_tank.svg){#fig-u03-balastni-tank fig-align="center" fig-alt="Balastni tank u trupu broda na gazu $T_g = 8{,}5$ m: vanjska morska voda i unutarnja balastna voda do visine $H_t = 5{,}0$ m. Prozor je na $h_p = 2$ m iznad dna tanka."}

**Pretpostavke i model**

Brod miruje i ne valja se – razmatra se čista hidrostatika. Slobodna površina mora i (u stanju A) slobodna površina balasta su na atmosferskom tlaku, pa se sve može računati manometarski. Stijenka tanka je nepropusna i kruta. Razlika gustoće morske i balastne vode ne mijenja se s dubinom – obje su nestlačive.

**Rješenje**

Manometarski tlak vanjske morske vode na razini dna tanka (dubina od morske površine = $T_g$):

$$
p_{ext,dno} = \rho_m g T_g = 1025 \cdot 9{,}81 \cdot 8{,}5 \approx 85{,}5\ \text{kPa}
$$ {#eq-hidrostatika-rijeseni-primjer-balastni-tank-broda-tlak-iznutr-01}

**Stanje A – tank pun balastne vode.** Manometarski tlak balasta na dnu tanka (dubina od slobodne površine balasta = $H_t$):

$$
p_{int,dno}^{A} = \rho_b g H_t = 1000 \cdot 9{,}81 \cdot 5{,}0 \approx 49{,}1\ \text{kPa}
$$ {#eq-hidrostatika-rijeseni-primjer-balastni-tank-broda-tlak-iznutr-02}

Neto tlak na dno tanka u stanju A (vani veći – stijenka biva tlačena prema unutra):

$$
\Delta p_{dno}^{A} = p_{ext,dno} - p_{int,dno}^{A} \approx 85{,}5 - 49{,}1 \approx 36{,}4\ \text{kPa}
$$ {#eq-hidrostatika-rijeseni-primjer-balastni-tank-broda-tlak-iznutr-03}

**Stanje B – tank prazan.** Unutarnji tlak na dno tanka jednak je atmosferskom, pa je manometarski nula:

$$
p_{int,dno}^{B} = 0
$$ {#eq-hidrostatika-rijeseni-primjer-balastni-tank-broda-tlak-iznutr-04}

Neto tlak na dno tanka u stanju B (vani veći – stijenka i dalje biva tlačena prema unutra, ali jače):

$$
\Delta p_{dno}^{B} = p_{ext,dno} - 0 \approx 85{,}5\ \text{kPa}
$$ {#eq-hidrostatika-rijeseni-primjer-balastni-tank-broda-tlak-iznutr-05}

**Promatračev prozor u stanju A.** Prozor je na visini $h_p = 2$ m iznad dna, pa:

- s vanjske strane je na dubini $T_g - h_p = 8{,}5 - 2 = 6{,}5\ \text{m}$ ispod morske površine:

$$
p_{ext,proz} = \rho_m g (T_g - h_p) = 1025 \cdot 9{,}81 \cdot 6{,}5 \approx 65{,}3\ \text{kPa}
$$ {#eq-hidrostatika-rijeseni-primjer-balastni-tank-broda-tlak-iznutr-06}

- s unutarnje strane je na dubini $H_t - h_p = 5 - 2 = 3{,}0\ \text{m}$ ispod razine balasta:

$$
p_{int,proz}^{A} = \rho_b g (H_t - h_p) = 1000 \cdot 9{,}81 \cdot 3{,}0 \approx 29{,}4\ \text{kPa}
$$ {#eq-hidrostatika-rijeseni-primjer-balastni-tank-broda-tlak-iznutr-07}

Neto tlak na prozor (vani veći, prema unutra):

$$
\Delta p_{proz}^{A} \approx 65{,}3 - 29{,}4 \approx 35{,}9\ \text{kPa}
$$ {#eq-hidrostatika-rijeseni-primjer-balastni-tank-broda-tlak-iznutr-08}

**Provjera i komentar**

1. Razlika između dva slučaja ($\Delta p_{dno}^{B}-\Delta p_{dno}^{A}\approx49{,}1\ \text{kPa}$) jednaka je unutarnjem hidrostatskom doprinosu balasta $\rho_b gH_t$; vanjski je tlak u oba uspoređena stanja isti.
2. Prazno stanje u ovom nastavnom paru daje veći neto tlak na promatranu stijenku. Iz toga ne slijedi da je ono mjerodavno projektno stanje: dimenzioniranje mora obuhvatiti propisane kombinacije opterećenja, geometriju, dinamiku i konstrukcijski model.
3. Neto tlakovi na **dno** i **prozor** u stanju A iznose redom $36{,}4$ i $35{,}9\ \text{kPa}$. Mala promjena po dubini posljedica je razlike gustoća: nagib neto tlaka iznosi $(\rho_m-\rho_b)g$, ovdje približno $0{,}25\ \text{kPa/m}$.
4. Punjenje ili pražnjenje tanka mijenja neto hidrostatičko opterećenje, ali ovaj presjek ne opisuje konstrukciju dvostrukoga trupa, slijed balastiranja ni sigurnost broda.
:::

::: {#ex-u03-iot-tlacni-senzor-za-otkrivanje-propustanja-u .mf1-we}
<p class="mf1-box-label">Riješeni primjer — IoT tlačni senzor za otkrivanje propuštanja u distribucijskoj mreži vodoopskrbe &nbsp;<span class="mf1-level">T2</span></p>

**Kontekst:** U distribucijskoj se mreži tlačna očitanja na dvama čvorovima uspoređuju s očekivanom hidrostatičkom razlikom. Odstupanje je dijagnostički signal, ali samo po sebi ne određuje uzrok: treba ga usporediti s potrošnjom, radom crpki i ventila, drugim senzorima te mjernom nesigurnošću.

**Zadano**

- Manometarski tlak na nižem čvoru `A`: $p_{M,A} = 5{,}20\ \text{bar} = 520\ \text{kPa}$
- Razlika visine između čvorova: $\Delta z = z_B - z_A = 38\ \text{m}$ ($B$ je viši)
- Gustoća vode: $\rho = 998\ \text{kg/m}^3$
- Atmosferski tlak: $p_{atm} = 101{,}3\ \text{kPa}$
- Mreža u stanju nominalne potrošnje, strujanje zanemarivo (čitanje se vrši u doba mirovanja)

**Traženo**

1. Očekivani manometarski tlak na višem čvoru `B`;
2. Apsolutni tlak na čvoru `B`;
3. Procjena: ako bi senzor na `A` umjesto $5{,}20\ \text{bar}$ pokazao $4{,}70\ \text{bar}$, što to znači za stanje mreže?

**Pretpostavke i model**

Promatra se kvazistatičko stanje mreže u kojem se zanemaruju lokalni gubici trenja jer su brzine strujanja niske (noćno mjerenje). Voda se smatra nestlačivom, gustoća se ne mijenja s visinom. Sav put između čvorova `A` i `B` prolazi kroz istu povezanu vodenu masu bez prelaza preko atmosfere.

**Rješenje**

Manometarski tlak na višem čvoru slijedi iz hidrostatske bilance po putu od `A` prema `B`:

$$
p_{M,B} = p_{M,A} - \rho g \Delta z = 520 \cdot 10^3 - 998 \cdot 9{,}81 \cdot 38.
$$ {#eq-hidrostatika-rijeseni-primjer-iot-tlacni-senzor-za-otkrivanje-01}

Drugi član iznosi $998 \cdot 9{,}81 \cdot 38 \approx 372{,}1 \cdot 10^3\ \text{Pa}$, pa je

$$
p_{M,B} \approx 520 - 372{,}1 = 147{,}9\ \text{kPa} \approx 1{,}48\ \text{bar}.
$$ {#eq-hidrostatika-rijeseni-primjer-iot-tlacni-senzor-za-otkrivanje-02}

Apsolutni tlak na `B` iznosi

$$
p_{aps,B} = p_{M,B} + p_{atm} = 147{,}9 + 101{,}3 = 249{,}2\ \text{kPa}.
$$ {#eq-hidrostatika-rijeseni-primjer-iot-tlacni-senzor-za-otkrivanje-03}

Ako bi senzor na `A` izvijestio o tlaku od $4{,}70\ \text{bar}$ umjesto očekivanih $5{,}20\ \text{bar}$, pad od $\Delta p = 50\ \text{kPa}$ predstavlja gubitak hidrostatičke visine od

$$
\Delta h = \frac{\Delta p}{\rho g} = \frac{50 \cdot 10^3}{998 \cdot 9{,}81} \approx 5{,}11\ \text{m}.
$$ {#eq-hidrostatika-rijeseni-primjer-iot-tlacni-senzor-za-otkrivanje-04}

Očitano odstupanje od $50\ \text{kPa}$ ekvivalentno je približno $5{,}11\ \text{m}$ vodenog stupca. Ono zahtijeva provjeru, ali iz jednoga očitanja nije moguće razlikovati propuštanje, promjenu potrošnje ili pogona, položaj ventila i pogrešku senzora.

**Provjera i komentar**

Hidrostatička razlika tlakova od $372\ \text{kPa}$ između čvorova razmaknutih $38\ \text{m}$ po visini odgovara promjeni oko $9{,}8\ \text{kPa}$ po metru vodenog stupca. Dobivenih $1{,}48\ \text{bar}$ u točki `B` rezultat je zadanoga kvazistatičkog modela, a ne provjera uslužnog tlaka mreže. Alarmni prag mora proizaći iz mjerne nesigurnosti, prirodne varijabilnosti pogona i procjene posljedica, ne iz univerzalne vrijednosti $50\ \text{kPa}$.
:::

::: {.mf1-samoprovjera}
<p class="mf1-box-label">Provjeri sebe</p>

Sljedeća pitanja služe za samostalnu provjeru razumijevanja prije prelaska na zadatke za vježbu.

1. Zašto je za jednoznačan proračun tlaka u manometru ključno odabrati i pratiti referentni smjer kretanja?

::: {.callout-note collapse="true"}
### Odgovor
Pri silasku kroz fluid tlak raste za $\rho g \Delta h$, pri penjanju pada za isti iznos. Ako se referentni smjer mijenja usred proračuna, predznak člana mijenja se nedosljedno i krajnji rezultat odstupa od fizikalno ispravnog.
:::

2. Koja je razlika između apsolutnog, manometarskog i vakuumskog tlaka?

::: {.callout-note collapse="true"}
### Odgovor
Apsolutni tlak mjeri se u odnosu na idealan vakuum i uvijek je nenegativan. Manometarski tlak je razlika apsolutnog i atmosferskog tlaka, može biti pozitivan ili negativan. Vakuumski tlak je iznos kojim je apsolutni tlak ispod atmosferskog, definira se kao $p_{vak} = p_{atm} - p_{aps}$.
:::

3. Pri kojoj se gustoći manometarskog fluida postiže veća osjetljivost mjerenja za male razlike tlakova?

::: {.callout-note collapse="true"}
### Odgovor
Veća osjetljivost (veća razlika visine za isti $\Delta p$) postiže se kad je manometarski fluid samo malo gušći od radnog fluida; tada faktor $(\rho_2 - \rho_1)$ u izrazu $\Delta p = (\rho_2-\rho_1)g\Delta h$ postaje malen, pa $\Delta h$ za isto $\Delta p$ raste.
:::

4. Vrijedi li hidrostatička jednadžba $p = p_0 + \rho gh$ za fluid u kojem postoji značajno strujanje?

::: {.callout-note collapse="true"}
### Odgovor
Ne vrijedi izravno; uz prisutno strujanje tlak ovisi i o brzinama i o gubitcima, pa se rabe energijska jednadžba iz <span class="mf1-ch-ref"><span class="mf1-ch-code">pog. 8</span><span class="mf1-ch-title">Energijska jednadžba i Bernoulli</span></span> i, kada je potrebno, modeli iz <span class="mf1-ch-ref"><span class="mf1-ch-code">pog. 13</span><span class="mf1-ch-title">Gubitci, cjevovodi, crpke i mreže</span></span>. Hidrostatička jednadžba ostaje točna za fluid u mirovanju ili pri zanemarivim brzinama.
:::
:::

## Zadaci za vježbu

::::: {.mf1-vjezbe-list}
1. [**T1**]{#task-u03-otvoreni-spremnik-s-vodom-ima-slobodnu-povrsinu} Otvoreni spremnik s vodom ima slobodnu površinu na atmosferskom tlaku. Odredi apsolutni i manometarski tlak u točki koja se nalazi na dubini $h = 2{,}40\ \text{m}$ ako je $p_{atm} = 100{,}8\ \text{kPa}$ i $\rho = 998\ \text{kg/m}^3$.

   :::: {.content-visible .mf1-hint-online when-format="html"}
   ::: {.callout-note collapse="true" data-hint-key="true"}
   ### Naputak
   manometarski tlak je $p_M = \rho gh$, a apsolutni $p_{aps} = p_{atm} + p_M$.
   :::
   ::::
   :::: {.content-visible .mf1-answer-online when-format="html"}
   ::: {.callout-tip collapse="true" data-answer-key="true"}
   ### Kontrolni rezultat

   $p_M \approx 23{,}5\ \text{kPa}$; $p_{aps} \approx 124{,}3\ \text{kPa}$.
   :::
   ::::
   **Skica:** da - otvoreni spremnik, slobodna površina i jedna točka na dubini $h$.

2. [**T1**]{#task-u03-u-zatvorenom-spremniku-iznad-vode-vlada-manometarski} U zatvorenom spremniku iznad vode vlada manometarski tlak $p_m = 26\ \text{kPa}$. Odredi apsolutni i manometarski tlak u priključku koji se nalazi $1{,}80\ \text{m}$ ispod slobodne površine ako je lokalni atmosferski tlak $p_{atm} = 99{,}2\ \text{kPa}$, a gustoća vode $\rho = 998\ \text{kg/m}^3$.

   :::: {.content-visible .mf1-hint-online when-format="html"}
   ::: {.callout-note collapse="true" data-hint-key="true"}
   ### Naputak
   najprije tlak na slobodnoj površini, zatim kroz isti fluid dodaj $\rho gh$; tek na kraju razdvoji apsolutni i manometarski tlak.
   :::
   ::::
   :::: {.content-visible .mf1-answer-online when-format="html"}
   ::: {.callout-tip collapse="true" data-answer-key="true"}
   ### Kontrolni rezultat

   $p_M \approx 43{,}6\ \text{kPa}$; $p_{aps} \approx 142{,}8\ \text{kPa}$.
   :::
   ::::
   **Skica:** da - zatvoreni spremnik, plinski prostor iznad vode i priključak na dubini $h$.

3. [**T2**]{#task-u03-cjevovod-s-uljem-gustoce-spojen-je-na} Cjevovod s uljem gustoće $\rho_u = 860\ \text{kg/m}^3$ spojen je na otvoreni U-manometar sa živom gustoće $\rho_{Hg} = 13600\ \text{kg/m}^3$. Razlika razina žive iznosi $\Delta h = 0{,}185\ \text{m}$, a priključna točka u kraku s uljem nalazi se $0{,}12\ \text{m}$ iznad dodira ulja i žive. Odredi manometarski tlak u cjevovodu.

   :::: {.content-visible .mf1-hint-online when-format="html"}
   ::: {.callout-note collapse="true" data-hint-key="true"}
   ### Naputak
   kreni od slobodne površine otvorenog kraka; niz stupce piši promjene tlaka kao $\rho g\Delta h$ uz točan znak.
   :::
   ::::
   :::: {.content-visible .mf1-answer-online when-format="html"}
   ::: {.callout-tip collapse="true" data-answer-key="true"}
   ### Kontrolni rezultat

   $p_M \approx 23{,}7\ \text{kPa}$.
   :::
   ::::
   **Skica:** da - U-manometar s uljem i živom, razlika razina $\Delta h$ i priključna točka.

4. [**T2**]{#task-u03-diferencijalni-manometar-ispunjen-zivom-spaja-dvije-tocke} Diferencijalni manometar ispunjen živom spaja dvije točke u vodi, pri čemu je razlika razina žive $\Delta h = 0{,}145\ \text{m}$. Točka `A` nalazi se $0{,}30\ \text{m}$ ispod točke `B`. Odredi razliku tlakova $p_A - p_B$.

   :::: {.content-visible .mf1-hint-online when-format="html"}
   ::: {.callout-note collapse="true" data-hint-key="true"}
   ### Naputak
   napravi jednu zatvorenu putanju od `A` do `B`; kroz vodu i živu piši odvojene doprinose $\rho g\Delta h$ i tek na kraju zbroji.
   :::
   ::::
   :::: {.content-visible .mf1-answer-online when-format="html"}
   ::: {.callout-tip collapse="true" data-answer-key="true"}
   ### Kontrolni rezultat

   $p_A - p_B \approx 20{,}9\ \text{kPa}$.
   :::
   ::::
   **Skica:** da - dvije točke spojene diferencijalnim manometrom s označenim visinskim pomakom.

5. [**T3**]{#task-u03-vakuumski-spremnik-spojen-je-na-otvoreni-zivin} Vakuumski spremnik spojen je na otvoreni živin manometar koji pokazuje razliku razina $\Delta h = 0{,}230\ \text{m}$. Ako je lokalni atmosferski tlak $p_{atm} = 98{,}6\ \text{kPa}$, odredi apsolutni tlak plina u spremniku. Zatim odredi apsolutni tlak u točki koja se nalazi $0{,}90\ \text{m}$ ispod slobodne površine vode unutar istog spremnika.

   :::: {.content-visible .mf1-hint-online when-format="html"}
   ::: {.callout-note collapse="true" data-hint-key="true"}
   ### Naputak
   iz manometra najprije vrati tlak plina, a zatim u istom spremniku kroz vodu dodaj $\rho gh$ do tražene točke.
   :::
   ::::
   :::: {.content-visible .mf1-answer-online when-format="html"}
   ::: {.callout-tip collapse="true" data-answer-key="true"}
   ### Kontrolni rezultat

   $p_{gas} \approx 67{,}9\ \text{kPa}$ (aps.); na dubini $0{,}90\ \text{m}$: $p \approx 76{,}7\ \text{kPa}$.
   :::
   ::::
   **Skica:** da - vakuumski spremnik, otvoreni živin manometar i unutarnja točka na dubini $h$.

6. [**T4**]{#task-u03-zatvoreni-spremnik-s-vodom-ima-plinski-prostor} Zatvoreni spremnik s vodom ima plinski prostor nepoznatog apsolutnog tlaka. Bočni priključak na dubini $h_1 = 0{,}65\ \text{m}$ spojen je na otvoreni U-manometar sa živom gustoće $\rho_{Hg} = 13600\ \text{kg/m}^3$, pri čemu je razlika razina žive $\Delta h = 0{,}210\ \text{m}$, a razina žive na strani spremnika niža. Odredi apsolutni tlak plina u spremniku i apsolutni tlak u točki koja leži $h_2=1{,}30\ \text{m}$ ispod slobodne površine vode. Uzmite $\rho_w = 998\ \text{kg/m}^3$ i $p_{atm} = 100{,}9\ \text{kPa}$. Za izbor apsolutnoga pretvornika tlaka uzmi tolerancije $\Delta h\pm2\ \text{mm}$, $h_1\pm5\ \text{mm}$, $h_2\pm5\ \text{mm}$ i $p_{atm}\pm0{,}4\ \text{kPa}$. Odredi konzervativni najveći očekivani tlak u dubljoj točki i izaberi mjerno područje $0$--$140\ \text{kPa}$ ili $0$--$160\ \text{kPa}$ ako puna skala mora biti barem $5\ \%$ veća od najvećega očekivanog tlaka.

   :::: {.content-visible .mf1-hint-online when-format="html"}
   ::: {.callout-note collapse="true" data-hint-key="true"}
   ### Naputak
   iz otvorenog manometra najprije vrati tlak u priključku, zatim se penjanjem kroz vodu vrati na plinski prostor, a silaskom na dubinu $h_2$ dobije tlak u traženoj točki. Za konzervativnu gornju granicu istodobno uzmi najveće $p_{atm}$, $\Delta h$ i $h_2$, a najmanje $h_1$. Nakon toga primijeni zahtijevanu rezervu na mjerno područje; nominalna vrijednost sama nije dovoljna za izbor senzora.
   :::
   ::::
   :::: {.content-visible .mf1-answer-online when-format="html"}
   ::: {.callout-tip collapse="true" data-answer-key="true"}
   ### Kontrolni rezultat

   $p_{gas} \approx 122{,}6\ \text{kPa}$ (aps.); na dubini $1{,}30\ \text{m}$: $p \approx 135{,}3\ \text{kPa}$. Konzervativna gornja granica iznosi $p_{max}\approx136{,}05\ \text{kPa}$, pa uz rezervu od $5\ \%$ treba puna skala od najmanje $142{,}9\ \text{kPa}$. Pretvornik $0$--$140\ \text{kPa}$ nije dostatan; bira se područje $0$--$160\ \text{kPa}$.
   :::
   ::::
   **Skica:** da - zatvoreni vodeni spremnik, priključak na dubini $h_1$, otvoreni U-manometar sa živom i dublja unutarnja točka.
:::::

![Skice uz zadatke za vježbu — otvoreni i zatvoreni spremnici te U-manometri (poglavlje 3).](../assets/print/u03_vjezbe_skice.svg){#fig-u03-vjezbe fig-align="center" fig-alt="Skice uz zadatke za vježbu — otvoreni i zatvoreni spremnici te U-manometri (poglavlje 3)."}

::: {.mf1-zavrsni-okvir}
<p class="mf1-box-label">Za ponijeti iz poglavlja</p>

**Sažeta provjera prije računa**

- Treba jasno označiti referentnu točku i poznati tlak.
- Treba razlikovati gdje se radi s apsolutnim, a gdje s manometarskim tlakom.
- Kretanje gore ili dolje kroz svaki stupac treba pratiti bez miješanja znakova.
- Treba provjeriti mijenja li se fluid, pa s njim i gustoća u izrazu $\rho g \Delta h$.
- Treba odvojiti čistu hidrostatiku od relativnog mirovanja i uzgona.

**Najčešća pogreška**

Najčešća greška nije sama algebra, nego prerano skrivanje fizike u jednu dugu jednadžbu. Ako se ne vidi gdje tlak raste, gdje pada i koji je tlak poznat na početku putanje, treba se vratiti na skicu.

**Nakon ovoga poglavlja mora biti moguće**

1. pročitati raspodjelu tlaka u otvorenom ili zatvorenom spremniku.
2. razlikovati apsolutni, manometarski i vakuumski tlak.
3. dosljedno pročitati više-fluidni manometar bez gubitka predznaka.

**U tehnici to znači**

Piezometar uz spremnik, diferencijalni manometar na filtru i tlačni priključak na balastnom tanku svi se čitaju istom hidrostatikom. Tko zna pratiti tlak kroz stupce fluida i tipove tlaka, zna i ispravno tumačiti očitanje instrumenta na stvarnom sustavu.

**Granica modela**

Jednostavni zapis $p = p_0 + \rho gh$ vrijedi samo dok je fluid u mirovanju ili u režimu koji se može čitati kao hidrostatika. Čim značajno uđu strujanje, promjena gustoće ili jaka akceleracija sustava, treba prijeći na širi model od čistoga manometarskog puta.

<span class="mf1-ch-ref"><span class="mf1-ch-code">pog. 3</span><span class="mf1-ch-title">Hidrostatička raspodjela tlaka i manometrija</span></span> treba učvrstiti tri stabilne navike: crtanje referentne skice, praćenje promjene tlaka po koracima i razlikovanje tipova tlaka prije nego što račun uopće počne.
:::

::: {.mf1-numerika}
<p class="mf1-box-label">Numerički most</p>

**Gdje ovo živi u numerici.** Hidrostatsko stanje prirodan je referentni slučaj za numerički model s gravitacijom. Zakon $dp/dz=-\rho g$ vrijedi kada je vertikalna bilanca doista hidrostatska; u strujajućem fluidu lokalna ubrzanja i naprezanja općenito mijenjaju gradijent tlaka.

**Što numerički alat radi s tim.** Može se rješavati puni tlak ili modificirani tlak iz kojega je izdvojen gravitacijski potencijal. Pri povratku na apsolutni ili manometarski tlak treba dosljedno vratiti referencu, predznak gravitacije i, kod promjenjive gustoće, odgovarajuću gustoću po domeni.

**Tipičan scenarij.** Mirna posuda poznate gustoće dobar je verifikacijski test: rekonstruirani tlak mora slijediti zadanu hidrostatsku raspodjelu unutar očekivane diskretizacijske i iteracijske pogreške. Tek nakon toga ima smisla tumačiti dinamičko odstupanje od hidrostatike.

> *Nije gradivo MF1. Ključna veza jest razlika između hidrostatskoga referentnog polja i dodatne dinamike koju rješava numerički model.*
:::
