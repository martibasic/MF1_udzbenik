Svaki ronilac osjeća da tlak raste s dubinom. Fluid koji miruje ne preuzima smična naprezanja, pa svaki njegov sloj tlakom nosi težinu slojeva iznad sebe. Ta je ravnoteža polazište za proračun spremnika i tankova te za mjerenje tlaka stupcima tekućine. U []{.mf1-chapter-ref target="u01"} tlak je uveden kao skalarna veličina koja se prenosi kroz zatvoreni fluid; u ovom se poglavlju pokazuje kako se mijenja s visinom.

Za os $z$ usmjerenu prema gore ravnoteža tankog vodoravnog sloja daje diferencijalnu jednadžbu hidrostatike $dp/dz=-\rho g$. U homogenom fluidu, uz stalne $\rho$ i $g$, njezinim se integriranjem dobiva radni zapis $p=p_{pov}+\rho g h$. Pritom je $h$ dubina ispod slobodne površine, a $p_{pov}$ tlak na njoj: atmosferski u otvorenom, a tlak plina $p_{pl}$ u zatvorenom spremniku. Tlak dakle linearno raste s dubinom, za vodu oko $9{,}81\ \text{kPa}$ po metru, a na istoj razini istoga povezanog mirujućeg fluida tlakovi su jednaki.

Tlak se izražava prema dvjema referencama. Manometarski tlak $p_M=p-p_{atm}$ mjeri se prema lokalnom atmosferskom tlaku, a apsolutni prema vakuumu, $p_{aps}=p_{atm}+p_M$; negativan $p_M$ označuje podtlak. Manometarski se tlak može prikazati i piezometarskom visinom $h_p=p_M/(\rho g)$, do koje bi se fluid podignuo u otvorenoj cjevčici. Manometri primjenjuju istu ravnotežu kroz više spojenih stupaca: pri hodu kroz mirujući fluid silazak povećava tlak za $\rho g\Delta h$, a uspon ga smanjuje za isti iznos. Za U-manometar sa živom spojen s plinskim prostorom zatvorenog spremnika tako slijedi $p_{pl}=p_{atm}+\rho_{Hg}g\Delta h$, uz zanemariv stupac plina. Za diferencijalni manometar s jednakim visinama priključaka i istim fluidom gustoće $\rho$ u oba voda vrijedi $p_1-p_2=(\rho_{Hg}-\rho)g\Delta h$.

Takva se mjerenja primjenjuju u spremnicima i piezometrima te za određivanje razlike tlakova na filtru ili izmjenjivaču topline. U brodogradnji se iz tlaka na dnu tanka određuje razina tereta ili balasta. Poglavlje redom izvodi jednadžbu hidrostatike, razmatra izotermalnu atmosferu, otvorene i zatvorene spremnike te manometarski lanac. Model pretpostavlja fluid koji miruje u odnosu na stijenke i stalnu gustoću u svakom segmentu. Ubrzani i rotirajući spremnici obrađuju se u []{.mf1-chapter-ref target="u04"}, a sile tlaka na stijenke u []{.mf1-chapter-ref target="u05"}. Kad fluid struji, tlaku se pridružuju doprinosi brzine i gubitaka, obrađeni u []{.mf1-chapter-ref target="u08"}.

Slika [-@fig-uvod-u03] prikazuje tri primjene. Lijevo je otvoreni spremnik s vodom gustoće $\rho$: na slobodnoj površini je $p_{pov}=p_{atm}$, odnosno $p_M=0$, a strelice uz stijenku prikazuju tlačno opterećenje koje linearno raste s dubinom do vrijednosti $p_{M,A}$ u točki $A$ na dubini $h$. Gore desno U-manometar sa živom (Hg) spaja plinski prostor zatvorenog spremnika, tlaka $p_{pl}$, s atmosferom; $\Delta h$ je razlika razina žive u krakovima. Dolje desno diferencijalni manometar mjeri razliku tlakova $p_1$ u vodu 1 ispred filtra i $p_2$ u vodu 2 iza njega; kraci iznad žive gustoće $\rho_{Hg}$ ispunjeni su fluidom gustoće $\rho$, a $\Delta h$ je opet razlika razina žive.

![Otvoreni spremnik s linearnim porastom tlaka uz stijenku, U-manometar sa živom na plinskom prostoru zatvorenog spremnika i diferencijalni manometar preko filtra.](../assets/print/u03_fig_uvod_pregled.svg){#fig-uvod-u03 fig-align="center" fig-alt="Tri prizora: trokut tlaka uz stijenku otvorenog spremnika s vodom, živin U-manometar spojen na plinski prostor zatvorenog spremnika i živin diferencijalni manometar između vodova ispred i iza filtra."}

**Procijenjeno vrijeme rada uz priručnik:** 9 sati.

## Diferencijalna jednadžba hidrostatike

Fluid koji miruje ne može preuzeti smična naprezanja povezana sa strujanjem, ali i dalje preuzima normalno naprezanje, odnosno tlak. Svaki sloj fluida mora nositi težinu slojeva iznad sebe, pa tlak raste s dubinom.

::: {.mf1-izvod}
<p class="mf1-box-label">Matematički izvod — Ravnoteža tankog vodoravnog sloja</p>

Promatra se tanki vodoravni sloj mirujućega fluida površine $A$ i debljine $dz$. Os $z$ usmjerena je prema gore. Na donju plohu djeluje tlačna sila $p(z)A$ prema gore, na gornju plohu tlačna sila $p(z + dz)A$ prema dolje, a dodatno prema dolje djeluje težina sloja $\rho g A dz$. Budući da je fluid u mirovanju, zbroj okomitih sila mora biti jednak nuli:

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

Ako je fluid homogen i njegova se gustoća može smatrati konstantnom, jednadžba se integrira između dviju točaka 1 i 2:

$$
\int_{p_1}^{p_2} dp = -\rho g \int_{z_1}^{z_2} dz,
$$ {#eq-hidrostatika-matematicki-izvod-05}

pa slijedi

$$
p_2 - p_1 = -\rho g (z_2 - z_1) = \rho g (z_1 - z_2).
$$ {#eq-hidrostatika-matematicki-izvod-06}
:::

Neka je $z_1$ visina slobodne površine, a $z_2$ visina promatrane točke, pri čemu je $z_2<z_1$. Dubina promatrane točke iznosi $h=z_1-z_2>0$, pa iz integriranoga oblika uz tlak na slobodnoj površini $p_1=p_{pov}$ slijedi radni zapis

$$
p = p_{pov} + \rho g h.
$$ {#eq-hidrostatika-razrada-koraka-01}

Dubina $h$ pozitivna je prema dolje, a $p_{pov}$ je tlak na slobodnoj površini: atmosferski u otvorenom, tlak plina $p_{pl}$ u zatvorenom spremniku.

::: {.mf1-fizikalno-znacenje}
<p class="mf1-box-label">Fizikalno značenje</p>
Lokalni gradijent tlaka uravnotežuje težinu fluida; negativan predznak znači da tlak pada s porastom koordinate $z$. Poznatom tlaku na slobodnoj površini dodaje se hidrostatički porast $\rho g h$: za vodu ($\rho \approx 1000\ \text{kg/m}^3$) svaki metar dubine donosi oko $9{,}81\ \text{kPa}$, a za živu ($\rho \approx 13600\ \text{kg/m}^3$) oko $133\ \text{kPa}$. Ista jednadžba vrijedi i unazad: iz poznatog tlaka u jednoj točki računa se tlak na svakoj drugoj visini u istom spojenom fluidu. Relacija $dp/dz=-\rho(z)g$ vrijedi i pri promjenjivoj gustoći, ali se tada gustoća ne može izlučiti iz integrala; linearni porast $\rho gh$ poseban je slučaj kad su $\rho$ i $g$ približno konstantni.
:::

::: {.mf1-izvod}
<p class="mf1-box-label">Matematički izvod — Vektorska generalizacija Eulerove jednadžbe hidrostatike</p>

Promatra se infinitezimalni kvadar fluida dimenzija $dx \times dy \times dz$ s težištem u točki $(x, y, z)$. Na njega djeluju težina i sile tlaka na svih šest ploha. Sila tlaka na lijevu plohu (okomitu na os $x$) iznosi $p(x - dx/2)\,dy\,dz$ u smjeru $+x$, a na desnu $p(x + dx/2)\,dy\,dz$ u smjeru $-x$. Rezultantna sila tlaka u smjeru osi $x$ iznosi

$$
dF_x = -\frac{\partial p}{\partial x}\,dx\,dy\,dz = -\frac{\partial p}{\partial x}\,dV.
$$ {#eq-hidrostatika-matematicki-izvod-vektorska-generalizacija-euler-01}

Analogno se dobiva za osi $y$ i $z$. Ako je gravitacija usmjerena prema $-z$ ($\vec{g} = -g\hat{z}$), težina kvadra djeluje samo po osi $z$: $dF_{G,z} = -\rho g\,dV$.

Ravnoteža sila u mirujućem fluidu daje tri komponente

$$
\frac{\partial p}{\partial x} = 0, \qquad \frac{\partial p}{\partial y} = 0, \qquad \frac{\partial p}{\partial z} = -\rho g,
$$ {#eq-hidrostatika-matematicki-izvod-vektorska-generalizacija-euler-02}

što se može sažeti u vektorski oblik

$$
\nabla p = \rho \vec{g}.
$$ {#eq-hidrostatika-matematicki-izvod-vektorska-generalizacija-euler-03}

U jednolikom gravitacijskom polju bez drugih volumenskih sila iz tih komponenata slijedi da tlak ovisi **samo o visini** $z$, pa su plohe konstantnog tlaka vodoravne ravnine. U općenitom polju volumenskih sila izobare ne moraju biti vodoravne. U []{.mf1-chapter-ref target="u04"} gravitacija se za jednoliko ubrzani sustav zamjenjuje efektivnim poljem $\vec{g}_{eff}=\vec{g}-\vec{a}$.
:::

::: {.mf1-izvod}
<p class="mf1-box-label">Matematički izvod — Izotermalna atmosfera i karakteristična visina</p>

Pretpostavka konstantne gustoće $\rho$ vrijedi za tekućine (voda, ulje, živa), ali ne za plinove, u kojima se gustoća mijenja s tlakom i temperaturom. Za **izotermalnu atmosferu**, uz pretpostavku $T=T_0=\text{konst.}$, može se izvesti raspodjela tlaka po visini.

Iz jednadžbe stanja idealnog plina vrijedi

$$
p = \rho R T_0 \quad\Longrightarrow\quad \rho = \frac{p}{R T_0},
$$ {#eq-hidrostatika-matematicki-izvod-izotermalna-atmosfera-i-karakt-01}

gdje je $R$ specifična plinska konstanta za zrak ($R \approx 287\ \text{J/(kg K)}$). Uvrštenjem u hidrostatičku jednadžbu $dp/dz = -\rho g$ slijedi

$$
\frac{dp}{dz} = -\frac{p\,g}{R T_0},
$$ {#eq-hidrostatika-matematicki-izvod-izotermalna-atmosfera-i-karakt-02}

što je obična diferencijalna jednadžba prvog reda u kojoj se varijable mogu razdvojiti:

$$
\frac{dp}{p} = -\frac{g}{R T_0}\,dz \quad\Longrightarrow\quad \ln p = -\frac{g}{R T_0}\,z + C.
$$ {#eq-hidrostatika-matematicki-izvod-izotermalna-atmosfera-i-karakt-03}

Uz početni uvjet $p(0) = p_{atm,0}$, atmosferski tlak na razini mora, dobiva se

$$
p(z) = p_{atm,0}\,\exp\!\left(-\frac{z}{H}\right), \qquad H = \frac{R T_0}{g}.
$$ {#eq-hidrostatika-matematicki-izvod-izotermalna-atmosfera-i-karakt-04}

Veličina $H$ naziva se **karakteristična visina atmosfere**. Za $T_0 = 288\ \text{K}$ (standardna prizemna temperatura) i $g = 9{,}81\ \text{m/s}^2$ slijedi

$$
H = \frac{287 \cdot 288}{9{,}81} \approx 8400\ \text{m} \approx 8{,}4\ \text{km}.
$$ {#eq-hidrostatika-matematicki-izvod-izotermalna-atmosfera-i-karakt-05}

U ovom izotermalnom modelu tlak pada za faktor $e\approx2{,}72$ nakon porasta visine za jednu karakterističnu visinu, ovdje oko $8{,}4\ \text{km}$. Na $z\approx8{,}8\ \text{km}$ model daje oko $35\ \text{kPa}$, odnosno približno trećinu tlaka na razini mora. Stvarna atmosfera nije izotermalna: za pouzdan atmosferski podatak koristi se odgovarajući standardni ili izmjereni profil temperature i tlaka, dok je ovaj izvod samo model reda veličine [@anderson2021].
:::

::: {.mf1-cfd title="Računalna dinamika fluida"}

**Spremnik prije uključivanja crpke.** U otvorenom spremniku rashladnog sustava najprije uspostavimo mirnu tekućinu zadane razine. Zadajemo gustoću, gravitaciju i atmosferski tlak na slobodnoj površini, a početni tlak raspodijelimo hidrostatički. Provjera je jasna: tlak mora rasti s dubinom, a brzina ostati blizu nule. Tako ispitujemo ravnotežu težine i tlačnih sila prije složenijeg računa.

Zatim možemo uključiti usis crpke i pratiti snižavanje razine ili vrtlog iznad usisa. Da bi se opisalo uvlačenje zraka, treba pratiti i granicu vode i zraka. Uspoređujemo položaj usisa i razinu punjenja te tražimo uvjete pri kojima zrak dospijeva u vod. Hidrostatika daje početno stanje i graničnu provjeru; pojava vrtloga zahtijeva opis gibanja kroz vrijeme.
:::

## Otvoreni i zatvoreni spremnici

U otvorenom spremniku tlak na slobodnoj površini jednak je atmosferskom tlaku. Zato je često praktično prijeći na manometarski tlak i atmosferu uzeti kao nultu razinu.

U zatvorenom spremniku tlak na slobodnoj površini različit je od atmosferskog, pa raspodjela nije samo $\rho g h$: u jednadžbi [-@eq-hidrostatika-razrada-koraka-01] $p_{pov}$ je tlak plinskog prostora.

Najčešća je pogreška uzeti atmosferu kao nulu i kad za to nema fizikalnog opravdanja. Iz manometarskog tlaka $p_M$ odmah se čita piezometarska visina

$$
h_p = \frac{p_M}{\rho g},
$$ {#eq-hidrostatika-otvoreni-i-zatvoreni-spremnici-02}

::: {.mf1-fizikalno-znacenje}
<p class="mf1-box-label">Fizikalno značenje</p>
Piezometarska visina geometrijski je prikaz tlaka: pokazuje do koje bi se visine voda (ili drugi fluid) podignula u otvorenoj cjevčici priključenoj na to mjesto. Manometarski pretlak od $10\ \text{kPa}$ u vodi odgovara piezometarskoj visini oko $1{,}02\ \text{m}$. Piezometri zato daju izravno i pregledno mjerenje u spremnicima, geotehničkim istraživanjima i distribucijskim mrežama kad su ispunjeni njihovi mjerni uvjeti.
:::

Ni piezometar ni manometar ne uvode novi zakon, nego su instrumentacijski zapis iste hidrostatičke ravnoteže kroz jedan ili više spojenih stupaca fluida. U praksi je dovoljno držati se jednoga slijeda: odabrati jednu referentnu točku ili jednu poznatu vrijednost tlaka, kretati se kroz stupce fluida u jednom dosljednom smjeru, pri silasku dodavati $\rho g \Delta h$, pri usponu oduzimati isti član te na istoj vodoravnoj razini istog mirujućeg fluida izjednačiti tlakove.

::: {.mf1-cfd title="Računalna dinamika fluida"}

**Balastni tank prije početka balastiranja.** Inženjersko pitanje glasi: daje li CFD model bočnog balastnog tanka iz primjera [-@ex-u03-balastni-tank-broda-tlak-iznutra-i-izvana] ispravno neto opterećenje zajedničke oplate prije nego što uključimo punjenje? Fizikalni model jest mirujuća morska voda u tanku i uz oplatu, s gravitacijom te atmosferskim tlakom na vodnoj liniji i na odzračniku. Podatci su gustoća $1025\ \text{kg/m}^3$, gaz, visina tanka i početna razina; izlazi su tlak na dnu i na ploči $P$ s obiju strana oplate te brzina u svakoj ćeliji.

Provjera ima tri koraka. Tlak mora rasti linearno s dubinom, brzina ostati blizu nule, a neto tlak na oplatu punog tanka biti jednak ručnom računu $\rho_{mv} g(T-H_{tk})$. Rješavači koji pohranjuju $p_{rgh}=p-\rho g h$, tlak bez hidrostatičkog doprinosa, moraju u mirnoj vodi dati konstantan $p_{rgh}$; s mjeračem se uspoređuje tek obnovljeni $p$. Odluka: punjenje tanka i gibanje broda simuliraju se tek kad ovaj statički test prođe, jer se pogrešna referenca tlaka ili neuravnotežen početni uvjet poslije više ne mogu razlučiti od stvarnog odziva.
:::

::: {.mf1-interaktivno}
<p class="mf1-box-label">Numerički pokus — Diferencijalni manometar</p>

**Predvidi.** Kako udvostručenje razlike razina mijenja razliku tlakova? Što očekuješ kada su gustoće gotovo jednake?

**Provjeri i protumači.** Usporedi formulu s hodom po stupcima. Promijeni predznak očitanja i objasni osjetljivost instrumenta uz isti dogovor o smjeru razlike tlakova.

<div class="mf1-interaktivno-akcija">
<a class="mf1-interaktivno-veza" href="https://martibasic.github.io/MF1_udzbenik/jlite/lab/index.html?path=u03_diferencijalni_manometar.ipynb">Pokreni u pregledniku</a>
<a class="mf1-interaktivno-veza" href="https://colab.research.google.com/github/martibasic/MF1_udzbenik/blob/main/notebooks/u03_diferencijalni_manometar.ipynb" target="_blank" rel="noopener">Pričuvno: otvori u Colabu</a>
<img class="mf1-interaktivno-qr" src="../assets/qr/u03_diferencijalni_manometar.svg" alt="QR kod za numerički pokus s diferencijalnim manometrom"/>
</div>

:::

Nedosljedna promjena referentnoga smjera ili zanemarivanje promjene fluida uzrokuje pogrešan predznak u manometarskoj jednadžbi. Jednako je važno razlikovati apsolutni, manometarski i vakuumski tlak; veza je uvijek

$$p_{aps} = p_{atm} + p_M$$ {#eq-hidrostatika-interaktivni-prikaz-diferencijalni-manometar-01}

::: {.mf1-fizikalno-znacenje}
<p class="mf1-box-label">Fizikalno značenje</p>
Apsolutni tlak mjeri se u odnosu na idealni vakuum ($p=0$), dok je manometarski tlak razlika prema lokalnom atmosferskom tlaku. Vakuumski tlak opisuje koliko je apsolutni tlak ispod atmosferskoga ($p_{vak}=p_{atm}-p_{aps}$). Negativan rezultat za apsolutni tlak u uobičajenom modelu kapljevine ili plina nije „veći podtlak”, nego znak da su pretpostavke računa napuštene; kavitacijski se kriterij pritom uspoređuje s tlakom zasićene pare, a ne s nulom. Zamjena referenci jedna je od najtipičnijih pogrešaka u manometriji.
:::

Za podtlak vrijedi i relacija

$$p_{vak} = p_{atm} - p_{aps} = -p_M \qquad (p_M<0)$$ {#eq-hidrostatika-fizikalno-znacenje-03}

::: {.mf1-granica-modela}
<p class="mf1-box-label">Granica modela — Kada hidrostatički lanac prestaje vrijediti</p>

Sve relacije ovog poglavlja pretpostavljaju fluid koji miruje u odnosu na stijenke, stalnu gustoću u svakom segmentu i poznat tlak u jednoj referentnoj točki. Model prestaje vrijediti čim fluid struji: tada se javljaju doprinosi brzine i gubitaka, obrađeni u []{.mf1-chapter-ref target="u08"} i []{.mf1-chapter-ref target="u13"}. Pri promjenjivoj gustoći, kao u atmosferi, gustoća ostaje pod integralom; stupac plina zanemaruje se samo kad je $\rho_{pl} g \Delta h$ zanemariv prema traženoj točnosti. Ubrzani ili rotirajući spremnik zahtijeva efektivno polje sila iz []{.mf1-chapter-ref target="u04"}, a kapilarni učinci u uskim cjevčicama korekciju iz []{.mf1-chapter-ref target="u02"}. Manometarski i apsolutni tlak moraju se voditi s istom referencom do kraja računa.
:::


::: {.mf1-cfd title="Računalna dinamika fluida"}

**Što znači nizak tlak na usisu?** Neki rješavači pohranjuju tlak podijeljen gustoćom, a neki izdvajaju hidrostatički doprinos, kao OpenFOAMov $p_{rgh}$ [@openfoam-hydrostatic]. Prije usporedbe s mjeračem treba obnoviti tlak u paskalima i njegovu referencu. Za opterećenje stijenke važna je razlika tlakova s njezinih strana, a za mogućnost nastanka pare apsolutni tlak pri radnoj temperaturi.

**Zastani i promisli.** CFD na usisu pokazuje negativan manometarski tlak, a senzor pozitivan apsolutni tlak. Moraju li se rezultati razlikovati?

Ne moraju: negativan manometarski tlak u CFD-u i pozitivan apsolutni tlak senzora mogu opisivati isto stanje. Prije zaključka o neslaganju usporedi njihove reference. Ručni proračun u primjeru [-@ex-u03-tlak-na-usisu-pumpe-za-cirkulaciju-ulja] razmatra mirujući stupac i prije usporedbe s tlakom pare obnavlja apsolutni tlak. Negativan manometarski tlak sam po sebi ne dokazuje kavitaciju. Problem usisa nastavlja se, uz crpku, u []{.mf1-chapter-ref target="u13"}.
:::

## Riješeni primjeri

::: {#ex-u03-tlak-u-prikljucku-zatvorenog-vodenog-spremnika-t1 .mf1-we}
<p class="mf1-box-label">Tlak u priključku zatvorenog vodenog spremnika&nbsp;<span class="mf1-level">T1</span></p>

**Tekst zadatka**

Zatvoreni spremnik s mirujućom vodom gustoće $\rho_v = 998\ \text{kg/m}^3$ ima plinski pretlak $p_{M,pl} = 18\ \text{kPa}$. Priključak $A$ nalazi se na dubini $h = 1{,}40\ \text{m}$ ispod slobodne površine. Lokalni atmosferski tlak iznosi $p_{atm} = 100{,}8\ \text{kPa}$.

**Traži se**

1. Odredi apsolutni tlak u plinskom prostoru spremnika.
2. Odredi apsolutni tlak u točki $A$.
3. Odredi manometarski tlak u točki $A$.

![Zatvoreni vodeni spremnik: plinski pretlak i dubina priključka A.](../assets/print/u03_fig_zatvoreni_spremnik_tlak.svg){#fig-u03-zatvoreni-spremnik-tlak fig-align="center" fig-alt="Zatvoreni spremnik s plinskim prostorom iznad vode i bočnim priključkom A, s kotom njegove dubine ispod slobodne površine."}

**Veza s proračunom.** Referentna točka je plinski prostor; do $A$ se silazi kroz vodu, a plinski pretlak i hidrostatički doprinos prate se odvojeno.

**Rješenje**

Apsolutni tlak u plinskom prostoru jednak je

$$
p_{pl} = p_{atm} + p_{M,pl} = 100{,}8 + 18{,}0 = 118{,}8\ \text{kPa} = 118800\ \text{Pa}.
$$ {#eq-hidrostatika-rijeseni-primjer-tlak-u-prikljucku-zatvorenog-vo-01}

Tlak u točki $A$ dobiva se silaskom kroz vodu za dubinu $h$:

$$
p_A = p_{pl} + \rho_v g h = 118800 + 998 \cdot 9{,}81 \cdot 1{,}40 = 132506{,}532\ \text{Pa} \approx 132{,}5\ \text{kPa}.
$$ {#eq-hidrostatika-rijeseni-primjer-tlak-u-prikljucku-zatvorenog-vo-02}

Manometarski tlak u točki $A$ zato iznosi

$$
p_{M,A} = p_A - p_{atm} = 132506{,}532 - 100800 = 31706{,}532\ \text{Pa} \approx 31{,}7\ \text{kPa}.
$$ {#eq-hidrostatika-rijeseni-primjer-tlak-u-prikljucku-zatvorenog-vo-03}

**Provjera i tumačenje**

Razlika $p_{M,A}-p_{M,pl}=13{,}7\ \text{kPa}$ jednaka je hidrostatičkom doprinosu $\rho_v gh$; referenca tlaka ne mijenja tu razliku.
:::

::: {#ex-u03-diferencijalni-manometar-izme-u-slatke-i-morske .mf1-we}
<p class="mf1-box-label">Diferencijalni manometar između slatke i morske vode&nbsp;<span class="mf1-level">T2</span></p>

**Tekst zadatka**

Diferencijalni manometar povezuje vod slatke vode gustoće $\rho_v = 1000\ \text{kg/m}^3$ i vod morske vode gustoće $\rho_{mv} = 1035\ \text{kg/m}^3$. Sadrži živu gustoće $\rho_{Hg} = 13600\ \text{kg/m}^3$ i zračni most gustoće $\rho_{zr} = 1{,}2\ \text{kg/m}^3$, nastavnu konstrukciju u obliku obrnutog U-kraka sa zrakom.

Put od $p_1$ do $p_2$ prema skici čine silazak kroz slatku vodu $h_1 = 0{,}60\ \text{m}$, uspon kroz živu $h_2 = 0{,}10\ \text{m}$, neto uspon kroz zrak $h_3 = 0{,}70\ \text{m}$ i silazak kroz morsku vodu $h_4 = 0{,}40\ \text{m}$. Fluidi u manometru miruju.

**Traži se**

1. Odredi razliku tlakova $p_1 - p_2$.
2. Odredi kolika je pogreška ako se stupac zraka zanemari.

![Diferencijalni manometar sa živom i zračnim mostom između vodova slatke i morske vode.](../assets/print/u03_val1_diferencijalni_manometar.svg){#fig-u03-diferencijalni-manometar fig-alt="Živin U-manometar, obrnuti krak sa zrakom i silazni krak morske vode, s okomitim kotama četiriju segmenata na putu od tlaka p1 do tlaka p2."}

**Veza s proračunom.** Hod od $p_1$ do $p_2$ prolazi niz slatku vodu, uz živu, neto uz zrak i niz morsku vodu; okomite kote imaju zajedničko mjerilo.

**Rješenje**

Krenimo od tlaka $p_1$ u lijevom vodu i pratimo put do tlaka $p_2$ u desnom vodu.

Ako se stupac zraka zanemari, radni zapis glasi:

1. Silazak kroz slatku vodu: $+\rho_v g h_1$.
2. Uspon kroz živu: $-\rho_{Hg} g h_2$.
3. Silazak kroz morsku vodu: $+\rho_{mv} g h_4$.

Zato vrijedi

$$
\begin{aligned}
&p_1 + \rho_v g h_1 - \rho_{Hg} g h_2 + \rho_{mv} g h_4 = p_2 \\
\Longrightarrow\quad &p_1 - p_2 = g\left(\rho_{Hg} h_2 - \rho_{mv} h_4 - \rho_v h_1\right).
\end{aligned}
$$ {#eq-hidrostatika-rijeseni-primjer-diferencijalni-manometar-izme-u-01}

Uvrštavanjem podataka:

$$
\begin{aligned}
p_1 - p_2 &= 9{,}81\left(13600 \cdot 0{,}10 - 1035 \cdot 0{,}40 - 1000 \cdot 0{,}60\right) \\
&= 3394{,}26\ \text{Pa} \approx 3{,}39\ \text{kPa}.
\end{aligned}
$$ {#eq-hidrostatika-rijeseni-primjer-diferencijalni-manometar-izme-u-02}

Sada uključimo i mali stupac zraka. Pri usponu kroz zrak tlak se dodatno smanjuje za $\rho_{zr} g h_3$, pa vrijedi

$$
\begin{aligned}
p_1 + \rho_v g h_1 - \rho_{Hg} g h_2 - \rho_{zr} g h_3 + \rho_{mv} g h_4 &= p_2, \\
p_1 - p_2 &= g\left(\rho_{Hg} h_2 + \rho_{zr} h_3 - \rho_{mv} h_4 - \rho_v h_1\right).
\end{aligned}
$$ {#eq-hidrostatika-rijeseni-primjer-diferencijalni-manometar-izme-u-03}

Numerički:

$$
\begin{aligned}
p_1 - p_2 &= 9{,}81\left(13600 \cdot 0{,}10 + 1{,}2 \cdot 0{,}70 - 1035 \cdot 0{,}40 - 1000 \cdot 0{,}60\right) \\
&\approx 3402{,}50\ \text{Pa} \approx 3{,}40\ \text{kPa}.
\end{aligned}
$$ {#eq-hidrostatika-rijeseni-primjer-diferencijalni-manometar-izme-u-04}

Pogreška zanemarivanja zraka zato iznosi $\Delta p = \rho_{zr}gh_3 \approx 8{,}24\ \text{Pa}$, a relativna pogreška je

$$
\delta \approx \frac{8{,}24}{3402{,}50} \cdot 100\ \% \approx 0{,}24\ \%.
$$ {#eq-hidrostatika-rijeseni-primjer-diferencijalni-manometar-izme-u-05}

**Provjera i tumačenje**

Član žive ($13{,}3\ \text{kPa}$) dominira, a zrak mijenja rezultat za $0{,}24\ \%$, pa je njegovo zanemarivanje opravdano. Pozitivan $p_1-p_2$ znači da je tlak veći u vodu slatke vode.
:::

U brodskoj se praksi istim hodom kroz slojeve određuje razina tereta iz tlaka na dnu tanka, pretlaka plina i sondiranja vodenog taloga.<span id="ex-u03-zatvoreni-vodeni-spremnik-s-uljnim-referentnim-spremnikom"></span>

::: {#ex-sondiranje-teretnog-tanka-s-tlacnim-mjeracem-razine .mf1-ch}
<p class="mf1-box-label">Sondiranje teretnog tanka s tlačnim mjeračem razine&nbsp;<span class="mf1-level">T3</span></p>

**Tekst zadatka**

Teretni tank tankera za naftne proizvode ima na dnu tlačni mjerač razine, a prostor iznad tereta ispunjen je inertnim plinom. Mjerač na dnu pokazuje manometarski tlak $p_{M,dno} = 141{,}0\ \text{kPa}$, a manometar inertnog plina pretlak $p_{M,pl} = 3{,}0\ \text{kPa}$. Teret je plinsko ulje gustoće $\rho_u = 860\ \text{kg/m}^3$. Ručno sondiranje s pastom za otkrivanje vode pokazuje na dnu sloj morske vode gustoće $\rho_{mv} = 1025\ \text{kg/m}^3$ debljine $h_v = 0{,}35\ \text{m}$. Ulaž (engl. *ullage*) jest udaljenost od referentne točke do površine tereta. Referentna točka, rub ulažnog otvora na palubi, nalazi se $H_{ref} = 18{,}60\ \text{m}$ iznad dna tanka; ulažna vrpca pokazuje $U_m = 2{,}31\ \text{m}$ od referentne točke do površine ulja. Tlocrtna površina tanka iznosi $A_t = 600\ \text{m}^2$, atmosferski tlak $p_{atm} = 101{,}0\ \text{kPa}$, a gustoća inertnog plina $\rho_{pl} = 1{,}2\ \text{kg/m}^3$. Fluidi miruju, gustoće su stalne, a granica ulja i vode je ravna.

**Traži se**

1. Iz očitanja mjerača na dnu odredi visinu stupca ulja $h_u$ i ulaž $U$ te ih usporedi s očitanjem vrpce.
2. Odredi apsolutni tlak na dnu tanka.
3. Odredi pogrešku visine i volumena ulja ako se vodeni talog ne sondira, nego se cijeli stupac tekućine računa kao ulje, te pogrešku ako se zaboravi pretlak inertnog plina.
4. Procijeni smije li se stupac inertnog plina zanemariti i obrazloži koji model treba ugraditi u sustav daljinskog mjerenja razine.

![Teretni tank s inertnim plinom, uljem i vodenim talogom: ulažni otvor, sondiranje i tlačni mjerač na dnu.](../assets/print/u03_ch1_zatvoreni_spremnik_ulje_ziva.svg){#fig-sondiranje-teretnog-tanka fig-align="center" fig-alt="Presjek teretnog tanka: inertni plin iznad ulja, tanak sloj vode na dnu, ulažni otvor s referentnom točkom na palubi i tlačni mjerač razine na dnu, s kotama H_ref, U, h_u i h_v."}

**Veza s proračunom.** Ulaž se mjeri od referentne točke na palubi prema dolje, a sondiranje od dna prema gore. Mjerač na dnu i ulažna vrpca neovisno mjere istu razinu; sam tlak ne može razlučiti debljinu vode. Visine imaju zajedničko mjerilo; širina tanka je shematska.

**Rješenje**

### 1. Visina ulja i ulaž iz tlaka na dnu {.unnumbered .unlisted .mf1-step}

Hod od ulažnog otvora prema dnu najprije prolazi kroz inertni plin zanemarive gustoće, zatim kroz ulje i na kraju kroz vodeni talog:

$$
p_{M,dno} = p_{M,pl} + \rho_u g h_u + \rho_{mv} g h_v.
$$ {#eq-sondiranje-lanac-tlaka-na-dnu}

Doprinos vodenog taloga iznosi $\rho_{mv} g h_v = 1025 \cdot 9{,}81 \cdot 0{,}35 = 3519{,}3\ \text{Pa}$, pa je visina stupca ulja

$$
\begin{aligned}
h_u &= \frac{p_{M,dno} - p_{M,pl} - \rho_{mv} g h_v}{\rho_u g} = \frac{141000 - 3000 - 3519{,}3}{860 \cdot 9{,}81} \\
&= \frac{134480{,}7}{8436{,}6} = 15{,}940\ \text{m}.
\end{aligned}
$$ {#eq-sondiranje-visina-stupca-ulja}

Ulaž slijedi iz geometrije tanka:

$$
U = H_{ref} - h_v - h_u = 18{,}60 - 0{,}35 - 15{,}940 = 2{,}310\ \text{m}.
$$ {#eq-sondiranje-ullage-iz-geometrije}

Vrpca pokazuje $U_m = 2{,}31\ \text{m}$; dva neovisna mjerenja razine slažu se unutar $1\ \text{mm}$, što je bolje od razlučivosti vrpce.

### 2. Apsolutni tlak na dnu {.unnumbered .unlisted .mf1-step}

$$
p_{aps,dno} = p_{atm} + p_{M,dno} = 101{,}0 + 141{,}0 = 242{,}0\ \text{kPa}.
$$ {#eq-sondiranje-apsolutni-tlak-dna}

Pretvornik na dnu mjeri prema atmosferi; apsolutni je tlak potreban tek ako se ugradi apsolutni pretvornik ili se tlak uspoređuje s tlakom pare tereta.

### 3. Pogreške pojednostavljenih modela {.unnumbered .unlisted .mf1-step}

Ako se cijeli stupac tekućine računa kao ulje, iz istog očitanja slijedi

$$
h' = \frac{p_{M,dno} - p_{M,pl}}{\rho_u g} = \frac{138000}{8436{,}6} = 16{,}357\ \text{m}.
$$ {#eq-sondiranje-jednofluidni-model}

Stvarni stupac ulja iznosi $15{,}940\ \text{m}$, pa jednofluidni model precjenjuje ulje za $16{,}357-15{,}940=0{,}417\ \text{m}$, odnosno za

$$
\Delta V = 0{,}417 \cdot 600 = 250\ \text{m}^3
$$ {#eq-sondiranje-pogreska-volumena-ulja}

u količini tereta. Ako se zaboravi pretlak inertnog plina, a voda se sondira, slijedi $h''=(141000-3519{,}3)/8436{,}6=16{,}296\ \text{m}$, odnosno precjenjivanje za $0{,}356\ \text{m}$ ili oko $213\ \text{m}^3$.

### 4. Stupac inertnog plina i izbor modela {.unnumbered .unlisted .mf1-step}

Hidrostatički doprinos plina u ulažnom prostoru iznosi

$$
\rho_{pl} g U = 1{,}2 \cdot 9{,}81 \cdot 2{,}31 = 27{,}2\ \text{Pa},
$$ {#eq-sondiranje-stupac-inertnog-plina}

što je $0{,}02\ \%$ očitanja na dnu i manje od $1\ \%$ pretlaka plina; zanemaruje se. Sustav mjerenja razine mora, međutim, uzeti u obzir pretlak inertnog plina i sondiranu debljinu vode, odnosno primijeniti dvofluidni model s plinskim pretlakom.

**Provjera i tumačenje**

1. Tlak na dnu i vrpca daju isti ulaž, pa se dva neovisna mjerenja međusobno potvrđuju. Oba pojednostavljenja precjenjuju količinu ulja jer se pretlak plina i gušća voda pripisuju stupcu ulja.
2. Stupac plina od nekoliko desetaka paskala zanemariv je, ali pretlak plina od $3\ \text{kPa}$ nije: o zanemarivanju odlučuje red veličine člana, ne vrsta fluida. Pri ljuljanju, trimu ili emulgiranoj vodi mjerenje treba ponoviti u mirnim uvjetima ili korigirati.
:::

::: {#ex-u03-tlak-na-usisu-pumpe-za-cirkulaciju-ulja .mf1-we}
<p class="mf1-box-label">Tlak na usisu crpke za cirkulaciju ulja&nbsp;<span class="mf1-level">T2</span></p>


**Tekst zadatka**

Usis crpke nalazi se $H = 2{,}40\ \text{m}$ iznad površine otvorenog spremnika ulja gustoće $\rho_u = 870\ \text{kg/m}^3$. Atmosferski tlak iznosi $p_{atm} = 101{,}3\ \text{kPa}$, a zadani tlak pare ulja $p_v \approx 200\ \text{Pa}$. Promatraj statičku granicu bez protoka, brzinske visine i gubitaka u usisnom vodu.

**Traži se**

1. Odredi manometarski tlak na usisu crpke.
2. Odredi apsolutni tlak na usisu crpke.
3. Odredi statičku gornju granicu visine stupca pri kojoj bi apsolutni tlak pao na zadani tlak pare $p_v \approx 200\ \text{Pa}$.

![Statički stupac ulja između slobodne površine i usisnog priključka crpke.](../assets/print/u03_fig_pumpa_usis.svg){#fig-u03-pumpa-usis fig-align="center" fig-alt="Otvoreni spremnik ulja s uronjenim usisnim vodom i crpkom postavljenom na visini H iznad slobodne površine, bez protoka."}

**Veza s proračunom.** Prikazan je idealni statički stupac ulja, $Q=0$; tlak opada s usponom do crpke, a s tlakom pare uspoređuje se apsolutni tlak.

**Rješenje**

Manometarski tlak na usisu crpke (uspon od slobodne površine za $H$):

$$
p_M = -\rho_u g H = -870 \cdot 9{,}81 \cdot 2{,}40 = -20483{,}28\ \text{Pa} \approx -20{,}5\ \text{kPa}
$$ {#eq-hidrostatika-rijeseni-primjer-tlak-na-usisu-pumpe-za-01}

Apsolutni tlak na usisu:

$$
p_{aps} = p_{atm} + p_M = 101300 - 20483{,}28 = 80816{,}72\ \text{Pa} \approx 80{,}8\ \text{kPa}
$$ {#eq-hidrostatika-rijeseni-primjer-tlak-na-usisu-pumpe-za-03}

Statička granična visina stupca pri $p_{aps}=p_v$:

$$
H_{max} = \frac{p_{atm} - p_v}{\rho_u g} = \frac{101300 - 200}{870 \cdot 9{,}81} = \frac{101100}{8534{,}7} \approx 11{,}8\ \text{m}
$$ {#eq-hidrostatika-rijeseni-primjer-tlak-na-usisu-pumpe-za-04}

**Provjera i tumačenje**

$11{,}8\ \text{m}$ samo je gornja granica stupca pri nultom protoku. Za crpku u radu potrebni su bilanca energije s brzinom i gubitcima te usporedba $NPSH_a$ s proizvođačevim $NPSH_r$, pa se iz ovoga računa ne može propisati opća „sigurna usisna visina”.

:::

::: {#ex-u03-balastni-tank-broda-tlak-iznutra-i-izvana .mf1-we}
<p class="mf1-box-label">Bočni balastni tank broda: tlak iznutra i izvana&nbsp;<span class="mf1-level">T2</span></p>

**Tekst zadatka**

Bočni balastni tank tankera s dvostrukim trupom visok je $H_{tk} = 5{,}0\ \text{m}$; njegova je vanjska stijenka oplata boka, a dno oplata dna na razini kobilice. Gaz broda iznosi $T = 8{,}5\ \text{m}$. Promatra se ploča oplate boka $P$ na visini $z_P = 2{,}0\ \text{m}$ iznad dna tanka. Izvana je more gustoće $\rho_{mv} = 1025\ \text{kg/m}^3$, a tank se balastira istom morskom vodom. Tank je odzračnom cijevi otvoren prema atmosferi; razina balasta provjerava se sondiranjem kroz sondnu cijev. Razmotri stanje A, tank pun do vrha, i stanje B, tank prazan; za usporedbu uzmi i stanje C, u kojem sonda pokazuje razinu balasta $h_s = 3{,}0\ \text{m}$ iznad dna. Brod i fluidi miruju, stijenke su krute i nepropusne, gustoće stalne, a $g = 9{,}81\ \text{m/s}^2$.

**Traži se**

1. Odredi manometarski tlak mora na razini dna tanka i na razini ploče $P$.
2. Odredi manometarski tlak balasta na dnu tanka i na ploči $P$ u stanju A.
3. Odredi neto manometarski tlak na dno u stanjima A i B te na ploču $P$ u stanju A; navedi smjer u kojem je oplata tlačena.
4. Odredi ulaž i neto tlak na dno u stanju C.

![Bočni balastni tank: more izvana i balast iznutra opterećuju oplatu dna i ploču P; sondna cijev i odzračnik otvoreni su prema palubi.](../assets/print/u03_fig_balastni_tank.svg){#fig-u03-balastni-tank fig-align="center" fig-alt="Bočni balastni tank uz oplatu broda: more izvana, balastna voda iznutra, ploča oplate P, sondna cijev i otvoreni odzračnik; kote gaza, visine tanka i položaja ploče."}

**Veza s proračunom.** Neto opterećenje zajedničke oplate jest razlika vanjskog i unutarnjeg tlaka na istoj razini; vanjski se mjeri od vodne linije, unutarnji od razine balasta. Debljine stijenki su shematske.

**Rješenje**

Manometarski tlak mora na dnu tanka (dubina od vodne linije $T$) i na ploči $P$ (dubina $T-z_P$):

$$
\begin{aligned}
p_{M,van,dno} &= \rho_{mv} g T = 1025 \cdot 9{,}81 \cdot 8{,}5 = 85{,}47\ \text{kPa}, \\
p_{M,van,P} &= \rho_{mv} g (T - z_P) = 1025 \cdot 9{,}81 \cdot 6{,}5 = 65{,}36\ \text{kPa}.
\end{aligned}
$$ {#eq-hidrostatika-rijeseni-primjer-balastni-tank-broda-tlak-iznutr-01}

### 1. Stanje A – tank pun balasta {.mf1-step .unnumbered .unlisted}

Unutarnji manometarski tlak na dnu (dubina $H_{tk}$) i na ploči $P$ (dubina $H_{tk}-z_P$):

$$
\begin{aligned}
p_{M,unu,dno}^{A} &= \rho_{mv} g H_{tk} = 1025 \cdot 9{,}81 \cdot 5{,}0 = 50{,}28\ \text{kPa}, \\
p_{M,unu,P}^{A} &= \rho_{mv} g (H_{tk} - z_P) = 1025 \cdot 9{,}81 \cdot 3{,}0 = 30{,}17\ \text{kPa}.
\end{aligned}
$$ {#eq-hidrostatika-rijeseni-primjer-balastni-tank-broda-tlak-iznutr-02}

Neto tlak na dno (vani veći, dno je tlačeno prema gore, u tank) i na ploču $P$ (vani veći, ploča je tlačena prema unutra):

$$
\Delta p_{dno}^{A} = 85{,}47 - 50{,}28 = 35{,}19\ \text{kPa}, \qquad \Delta p_{P}^{A} = 65{,}36 - 30{,}17 = 35{,}19\ \text{kPa}.
$$ {#eq-hidrostatika-rijeseni-primjer-balastni-tank-broda-tlak-iznutr-03}

### 2. Stanje B – tank prazan {.mf1-step .unnumbered .unlisted}

Unutarnji tlak jednak je atmosferskom, pa je manometarski tlak jednak nuli i cijeli vanjski tlak opterećuje oplatu:

$$
\Delta p_{dno}^{B} = p_{M,van,dno} - 0 = 85{,}47\ \text{kPa}, \qquad \Delta p_{P}^{B} = 65{,}36\ \text{kPa}.
$$ {#eq-hidrostatika-rijeseni-primjer-balastni-tank-broda-tlak-iznutr-04}

### 3. Stanje C – razina iz sondiranja {.mf1-step .unnumbered .unlisted}

Sonda pokazuje $h_s = 3{,}0\ \text{m}$, pa je ulaž, udaljenost od vrha tanka do površine, $H_{tk} - h_s = 2{,}0\ \text{m}$. Neto tlak na dno iznosi

$$
\Delta p_{dno}^{C} = p_{M,van,dno} - \rho_{mv} g h_s = 85{,}47 - 30{,}17 = 55{,}30\ \text{kPa}.
$$ {#eq-hidrostatika-rijeseni-primjer-balastni-tank-broda-tlak-iznutr-05}

**Provjera i tumačenje**

1. Uz jednake gustoće neto tlak na cijeloj omočenoj oplati punog tanka iznosi $\rho_{mv} g (T - H_{tk}) = 1025 \cdot 9{,}81 \cdot 3{,}5 = 35{,}19\ \text{kPa}$, pa dno i ploča $P$ nose isti neto tlak. Razlika stanja B i A, $50{,}28\ \text{kPa}$, jednaka je $\rho_{mv} g H_{tk}$, a stanje C leži između njih.
2. Prazan tank ovdje najjače opterećuje oplatu, ali mjerodavno projektno stanje određuju propisane kombinacije opterećenja i konstrukcijski model. Tlak na dnu pretvara se u razinu samo uz poznatu gustoću, kao u primjeru [-@ex-sondiranje-teretnog-tanka-s-tlacnim-mjeracem-razine].
:::

::: {#ex-u03-iot-tlacni-senzor-za-otkrivanje-propustanja-u .mf1-we}
<p class="mf1-box-label">Tlak u mreži iz kote vodotornja i IoT senzor za otkrivanje propuštanja&nbsp;<span class="mf1-level">T2</span></p>

**Tekst zadatka**

Distribucijska mreža vodoopskrbe napaja se iz vodotornja. U noćnom minimumu potrošnje voda u mreži praktički miruje. IoT tlačni senzor u nižem čvoru $A$ pokazuje manometarski tlak $p_{M,A} = 5{,}20\ \text{bar} = 520\ \text{kPa}$. Priključak $B$ u podnožju vodotornja viši je za $\Delta z = z_B - z_A = 38\ \text{m}$, a spremnik vodotornja otvoren je prema atmosferi. Čvorove povezuje ista vodena masa gustoće $\rho_v = 998\ \text{kg/m}^3$, bez otvaranja prema atmosferi između njih. Atmosferski tlak je $p_{atm} = 101{,}3\ \text{kPa}$. Zanemari gubitke i promjenu gustoće. Za usporedbu razmotri i očitanje $4{,}70\ \text{bar}$ u $A$.

**Traži se**

1. Odredi očekivani manometarski tlak na priključku $B$.
2. Odredi apsolutni tlak na priključku $B$.
3. Odredi visinu slobodne površine vode u vodotornju iznad priključka $B$.
4. Procijeni što za stanje mreže znači ako bi senzor na $A$ umjesto $5{,}20\ \text{bar}$ pokazao $4{,}70\ \text{bar}$.

**Rješenje**

Manometarski tlak na višem priključku slijedi iz hidrostatičke bilance po putu od $A$ prema $B$:

$$
p_{M,B} = p_{M,A} - \rho_v g \Delta z = 520 \cdot 10^3 - 998 \cdot 9{,}81 \cdot 38.
$$ {#eq-hidrostatika-rijeseni-primjer-iot-tlacni-senzor-za-otkrivanje-01}

Drugi član iznosi $998 \cdot 9{,}81 \cdot 38 = 372{,}0 \cdot 10^3\ \text{Pa}$, pa je

$$
p_{M,B} = 520{,}0 - 372{,}0 = 148{,}0\ \text{kPa} \approx 1{,}48\ \text{bar}.
$$ {#eq-hidrostatika-rijeseni-primjer-iot-tlacni-senzor-za-otkrivanje-02}

Apsolutni tlak na $B$ iznosi

$$
p_{aps,B} = p_{M,B} + p_{atm} = 148{,}0 + 101{,}3 = 249{,}3\ \text{kPa}.
$$ {#eq-hidrostatika-rijeseni-primjer-iot-tlacni-senzor-za-otkrivanje-03}

Spremnik vodotornja otvoren je prema atmosferi, pa manometarski tlak u podnožju potječe samo od stupca vode iznad $B$:

$$
h_{vt} = \frac{p_{M,B}}{\rho_v g} = \frac{147{,}97 \cdot 10^3}{998 \cdot 9{,}81} = 15{,}11\ \text{m}.
$$ {#eq-vodotoranj-razina-iz-tlaka-podnozja}

Zato tlak u mreži određuje kota slobodne površine vodotornja, $z_B + h_{vt} = z_A + 53{,}1\ \text{m}$, a ne duljina ni promjer vodova, sve dok voda miruje.

Ako bi senzor na $A$ pokazao tlak od $4{,}70\ \text{bar}$ umjesto očekivanih $5{,}20\ \text{bar}$, pad od $\Delta p = 50\ \text{kPa}$ odgovarao bi gubitku piezometarske visine od

$$
\Delta h = \frac{\Delta p}{\rho_v g} = \frac{50 \cdot 10^3}{998 \cdot 9{,}81} = 5{,}11\ \text{m}.
$$ {#eq-hidrostatika-rijeseni-primjer-iot-tlacni-senzor-za-otkrivanje-04}

To odgovara padu razine u vodotornju s $15{,}11$ na $10{,}0\ \text{m}$ iznad $B$, što se izravno provjerava mjeračem razine u vodotornju. Ako je razina u tornju nepromijenjena, voda u mreži ne miruje: pad tlaka tada upućuje na potrošnju, propuštanje ili zatvoren ventil, a iz jednoga očitanja te uzroke nije moguće razlikovati.

**Provjera i tumačenje**

Bilanca se zatvara: $38 + 15{,}11 = 53{,}1\ \text{m}$ jest piezometarska visina u $A$, uz oko $9{,}8\ \text{kPa}$ po metru vodenog stupca. Alarmni prag mora proizaći iz mjerne nesigurnosti senzora, prirodne promjene razine u tornju i procjene posljedica, ne iz univerzalne vrijednosti $50\ \text{kPa}$.
:::


:::: {.mf1-samoprovjera}
<p class="mf1-box-label">Provjeri sebe</p>

1. Zašto je u spojenom mirujućem fluidu tlak na istoj dubini jednak?

::: {.callout-note collapse="true"}
### Odgovor
Kad bi tlakovi na istoj dubini bili različiti, mirujući fluid ne bi bio u ravnoteži.
:::

2. Dva pretvornika na istoj razini u balastnom tanku pokazuju $50{,}3\ \text{kPa}$ manometarski i $151{,}6\ \text{kPa}$ apsolutno. Jesu li očitanja u suprotnosti?

::: {.callout-note collapse="true"}
### Odgovor
Nisu: razlika $101{,}3\ \text{kPa}$ jest lokalni atmosferski tlak. Prije usporedbe očitanja uvijek ih svedi na istu referencu.
:::

3. Kada se relacija $p=p_{pov}+\rho gh$ ne smije primijeniti s jednom konstantnom gustoćom?

::: {.callout-note collapse="true"}
### Odgovor
Kad se gustoća mijenja ili kad je na putu više fluida: tada gustoća ostaje unutar odgovarajućeg integrala ili segmentnog zapisa.
:::

4. Zašto iz hidrostatičkoga računa ne slijedi automatski tlak u strujajućem sustavu?

::: {.callout-note collapse="true"}
### Odgovor
Strujanje uvodi doprinose brzine, gubitaka i, eventualno, nestacionarnosti, koji nisu sadržani u čistoj hidrostatici.
:::
::::

## Zadatci za vježbu {#sec-u03-zadatci}

::::: {.mf1-vjezbe-list}

U svim zadatcima uzmi $g = 9{,}81\ \text{m/s}^2$. Fluidi miruju, gustoće su stalne, a utjecaji kapilarnosti i težine plina zanemaruju se; iznimka je Z1, u kojem je promjenjiva gustoća zraka sam predmet računa. Granice tekućih slojeva u spremnicima su ravne. Podatci i mjerna ograničenja nastavne su pretpostavke; očitanja u Z1, Z2, Z3, Z4 i Z6 sintetička su, a ne zapisi stvarnog pokusa.

<span id="task-u03-otvoreni-spremnik-s-vodom-ima-slobodnu-povrsinu"></span>

### Visina leta iz barometarskog očitanja {#task-visina-iz-barometarskog-ocitanja .unnumbered .unlisted}

**Tekst zadatka**

Dron s barometarskim senzorom polijeće s baze na kojoj je tlak $p_0 = 101{,}3\ \text{kPa}$; na najvišoj točki leta senzor pokazuje $p = 84{,}5\ \text{kPa}$. Zrak smatraj izotermalnim idealnim plinom s $T_0 = 288\ \text{K}$ i $R = 287\ \text{J/(kg K)}$. Razlučivost senzora iznosi $10\ \text{Pa}$.

**Traži se**

1. Odredi karakterističnu visinu atmosfere i visinu leta iznad baze prema izotermalnom modelu.
2. Odredi visinu koju bi dao model stalne gustoće zraka $\rho_0=p_0/(RT_0)$ i relativno odstupanje od izotermalnog rezultata; obrazloži predznak odstupanja.
3. Kolikoj promjeni visine na vrhu leta odgovara razlučivost senzora?

:::: {.content-visible .mf1-hint-online when-format="html"}
::: {.callout-note collapse="true" data-hint-key="true"}
### Naputak
Iz izvoda izotermalne atmosfere slijedi $z=H\ln(p_0/p)$ s $H=RT_0/g$. Model stalne gustoće daje $z=(p_0-p)/(\rho_0g)$, kao za tekućinu. Za razlučivost upotrijebi lokalnu gustoću $\rho=p/(RT_0)$ na vrhu.
:::
::::
:::: {.content-visible .mf1-answer-online when-format="html"}
::: {.callout-tip collapse="true" data-answer-key="true"}
### Kontrolni rezultat

$H\approx8426\ \text{m}$; $z\approx1528\ \text{m}$. Stalna gustoća $\rho_0=1{,}226\ \text{kg/m}^3$ daje $z\approx1397\ \text{m}$, oko $8{,}5\,\%$ manje: gustoća s visinom pada, pa svaki paskal razlike u visini vrijedi više metara nego pri tlu. Razlučivost od $10\ \text{Pa}$ odgovara oko $1{,}0\ \text{m}$ na vrhu ($0{,}83\ \text{m}$ na bazi).
:::
::::

[Razina: T1]{.mf1-task-level}

<span id="task-u03-u-zatvorenom-spremniku-iznad-vode-vlada-manometarski"></span>

### Razina vode iz razlike tlakova {#task-razina-vode-iz-razlike-tlakova .unnumbered .unlisted}

**Tekst zadatka**

U zatvorenom spremniku s vodom gustoće $\rho_v = 998\ \text{kg/m}^3$ tlak se mjeri u točki $A$ uz dno i u plinskom prostoru $G$. Razlika tlakova iznosi $\Delta p = p_A-p_{pl} = 17{,}62\ \text{kPa}$. Oba se tlaka odnose izravno na označene točke, bez dodatnih stupaca tekućine u mjernim vodovima.

Za usporedbu razmotri porast plinskog tlaka za $5{,}0\ \text{kPa}$.

**Traži se**

1. Odredi visinu vode $h$ iznad točke $A$.
2. Bi li se razlika tlakova promijenila pri zadanom porastu tlaka plina, uz nepromijenjene razinu i gustoću vode?

:::: {.content-visible .mf1-hint-online when-format="html"}
::: {.callout-note collapse="true" data-hint-key="true"}
### Naputak
Zapiši tlak u $A$ polazeći od tlaka plina. Oduzmi $p_{pl}$ pa iz preostale hidrostatičke razlike odredi visinu.
:::
::::
:::: {.content-visible .mf1-answer-online when-format="html"}
::: {.callout-tip collapse="true" data-answer-key="true"}
### Kontrolni rezultat

$h \approx 1{,}80\ \text{m}$. Pri zadanoj promjeni tlaka plina oba tlaka porastu za $5{,}0\ \text{kPa}$, pa $\Delta p$ ostaje $17{,}62\ \text{kPa}$.
:::
::::

[Razina: T1]{.mf1-task-level}

<span id="task-u03-cjevovod-s-uljem-gustoce-spojen-je-na"></span>

### Nagnuti manometar na ventilacijskom kanalu {#task-nagnuti-manometar-ventilacijski-kanal .unnumbered .unlisted}

**Tekst zadatka**

Pretlak zraka u ventilacijskom kanalu mjeri se nagnutim manometrom. Posuda unutarnjeg promjera $D = 40\ \text{mm}$ spojena je na kanal, a iz njezina dna izlazi cjevčica unutarnjeg promjera $d = 5{,}0\ \text{mm}$, nagnuta za $\alpha = 15^\circ$ prema vodoravnici i otvorena prema atmosferi. Manometarska tekućina je ulje gustoće $\rho_u = 820\ \text{kg/m}^3$. Pri jednakim tlakovima meniskus u cjevčici stoji na nultoj oznaci; pri mjerenju se pomakne za $L = 185\ \text{mm}$ uzduž cjevčice. Gustoću zraka zanemari.

**Traži se**

1. Odredi pretlak u kanalu uz pretpostavku da se razina ulja u posudi ne mijenja.
2. Uključi spuštanje razine u posudi, odredi točan pretlak i relativnu pogrešku pojednostavljenja.
3. Odredi osjetljivost instrumenta, pomak očitanja po paskalu, i usporedi je s okomitim U-manometrom s istim uljem. Obrazloži zašto se kut ne smanjuje proizvoljno.

:::: {.content-visible .mf1-hint-online when-format="html"}
::: {.callout-note collapse="true" data-hint-key="true"}
### Naputak
Pretlak nosi okomita razlika razina ulja: $L\sin\alpha$ u cjevčici i spuštanje razine u posudi, koje slijedi iz jednakosti istisnutih volumena $aL=A\,\delta$ s $a/A=(d/D)^2$. Osjetljivost je $dL/dp_M$; u U-manometru očitanje je razlika razina dvaju krakova.
:::
::::
:::: {.content-visible .mf1-answer-online when-format="html"}
::: {.callout-tip collapse="true" data-answer-key="true"}
### Kontrolni rezultat

Bez spuštanja razine: $h=L\sin\alpha=47{,}9\ \text{mm}$, $p_M\approx385\ \text{Pa}$. S posudom: $\delta=L(d/D)^2=2{,}9\ \text{mm}$, $h=50{,}8\ \text{mm}$, $p_M\approx408\ \text{Pa}$; pojednostavljenje podcjenjuje tlak za $5{,}7\,\%$. Osjetljivost $1/[\rho_ug(\sin\alpha+a/A)]\approx0{,}45\ \text{mm/Pa}$, $3{,}6$ puta više od U-manometra ($0{,}124\ \text{mm/Pa}$). Pri vrlo malom kutu meniskus se razvlači i zaustavlja uz stijenku, a nagib postaje osjetljiv na horizontiranje, pa se u praksi ne ide ispod $5$–$10^\circ$.
:::
::::

[Razina: T2]{.mf1-task-level}

<span id="task-u03-diferencijalni-manometar-ispunjen-zivom-spaja-dvije-tocke"></span>

### Debljina sloja ulja iz tlaka {#task-debljina-sloja-ulja-iz-tlaka .unnumbered .unlisted}

**Tekst zadatka**

U otvorenom spremniku miruju dva nemješljiva sloja: ulje gustoće $\rho_u = 850\ \text{kg/m}^3$ iznad vode gustoće $\rho_v = 1000\ \text{kg/m}^3$. Ukupna visina tekućine iznad dna iznosi $H = 1{,}50\ \text{m}$, a manometarski tlak na dnu $p_{M,A} = 13{,}83\ \text{kPa}$.

**Traži se**

1. Odredi debljine sloja ulja $h_u$ i sloja vode $h_v$ te manometarski tlak na njihovoj granici.
2. Provjeri je li dobiveni raspored moguć i skiciraj kako tlak raste s dubinom: mijenja li se na granici tlak ili samo njegov nagib?

:::: {.content-visible .mf1-hint-online when-format="html"}
::: {.callout-note collapse="true" data-hint-key="true"}
### Naputak
Debljine slojeva moraju dati ukupnu visinu. Tlak na dnu dobiva se zbrajanjem dvaju hidrostatičkih doprinosa. Kao provjeru usporedi zadani tlak s tlakovima koje bi dala ista ukupna visina čistog ulja i čiste vode.
:::
::::
:::: {.content-visible .mf1-answer-online when-format="html"}
::: {.callout-tip collapse="true" data-answer-key="true"}
### Kontrolni rezultat

$h_u \approx 0{,}601\ \text{m}$; $h_v \approx 0{,}899\ \text{m}$; $p_{M,granica} \approx 5{,}015\ \text{kPa}$. Obje su debljine pozitivne, a $12{,}508 < 13{,}830 < 14{,}715\ \text{kPa}$. Tlak je na ravnoj granici kontinuiran; nagib $dp/dh$ raste s $8{,}339$ na $9{,}810\ \text{kPa/m}$ pri ulasku iz ulja u vodu.
:::
::::

[Razina: T2]{.mf1-task-level}

<span id="task-u03-vakuumski-spremnik-spojen-je-na-otvoreni-zivin"></span>

### Izbor manometra za podtlak {#task-izbor-manometra-za-podtlak .unnumbered .unlisted}

**Tekst zadatka**

U-manometrom otvorenim prema atmosferi treba mjeriti podtlak plina od nule do $p_{vak,max} = 6{,}00\ \text{kPa}$. Lokalni atmosferski tlak iznosi $p_{atm} = 98{,}6\ \text{kPa}$. Razmatraju se tri odvojene izvedbe ispunjene uljem gustoće $\rho_u = 860\ \text{kg/m}^3$, vodom gustoće $\rho_v = 998\ \text{kg/m}^3$ ili živom gustoće $\rho_{Hg} = 13600\ \text{kg/m}^3$. Najveća dopuštena **okomita razlika razina** iznosi $\Delta h_{max} = 0{,}650\ \text{m}$.

Zajamčena pogreška očitanja te razlike iznosi najviše $\varepsilon_h = 1{,}0\ \text{mm}$; to je pogreška već očitane razlike, ne svakog kraka zasebno. Pripadna pogreška izračunanog podtlaka ne smije premašiti $\varepsilon_{p,max} = 20\ \text{Pa}$. Gustoće i $g$ u ovom se proračunu smatraju točnima. Pri ocjeni razmotri samo zadane mjerne zahtjeve.

**Traži se**

1. Za svaku izvedbu odredi potrebnu razliku razina pri najvećem podtlaku i granicu tlačne pogreške.
2. Izaberi izvedbu koja zadovoljava oba uvjeta.
3. Koji je krak viši i koliki je apsolutni tlak plina pri najvećem podtlaku?
4. Objasni zašto najkraći stupac nije nužno najbolji izbor.

:::: {.content-visible .mf1-hint-online when-format="html"}
::: {.callout-note collapse="true" data-hint-key="true"}
### Naputak
Kreni od atmosferskog tlaka i uspona kroz manometarsku tekućinu prema strani podtlaka. Ista gustoća određuje i potrebnu visinu za zadani tlak i promjenu tlaka pri pogrešci visine. Provjeri oba ograničenja za svaki fluid.
:::
::::
:::: {.content-visible .mf1-answer-online when-format="html"}
::: {.callout-tip collapse="true" data-answer-key="true"}
### Kontrolni rezultat

Za ulje, vodu i živu redom: $\Delta h \approx 0{,}711$; $0{,}613$; $0{,}04497\ \text{m}$, a granice tlačne pogreške su $8{,}44$; $9{,}79$; $133{,}42\ \text{Pa}$. Bira se **voda**: ulje traži preveliku razliku razina, a živa daje preveliku tlačnu pogrešku. Razina je viša u kraku spojenom s plinom; $p_{pl} \approx 92{,}6\ \text{kPa}$ (aps.). Veća gustoća skraćuje stupac, ali pri istoj pogrešci očitanja povećava tlačnu pogrešku.
:::
::::

[Razina: T3]{.mf1-task-level}

### Tlak plina iz manometarskog mjerenja {#task-u03-zatvoreni-spremnik-s-vodom-ima-plinski-prostor .unnumbered .unlisted}

**Tekst zadatka**

Zatvoreni spremnik s vodom ima plinski prostor nepoznatog apsolutnog tlaka. Bočni priključak na dubini $h_1 = 0{,}65\ \text{m}$ spojen je na otvoreni U-manometar sa živom gustoće $\rho_{Hg} = 13600\ \text{kg/m}^3$, pri čemu je razlika razina žive $\Delta h = 0{,}210\ \text{m}$, a razina žive na strani spremnika niža.

Spojni vod od priključka do žive potpuno je ispunjen vodom; granica vode i žive nalazi se **na istoj visini kao priključak**. Dublja točka leži $h_2=1{,}30\ \text{m}$ ispod slobodne površine vode. Uzmi $\rho_v = 998\ \text{kg/m}^3$ i $p_{atm} = 100{,}9\ \text{kPa}$. Za izbor apsolutnoga pretvornika tlaka uzmi tolerancije $\Delta h\pm2\ \text{mm}$, $h_1\pm5\ \text{mm}$, $h_2\pm5\ \text{mm}$ i $p_{atm}\pm0{,}4\ \text{kPa}$.

Tolerancije su zajamčeni granični intervali, ne standardne nesigurnosti; dopuštena je svaka kombinacija njihovih vrijednosti. Geometrijski uvjet jednake visine priključka i granice vode i žive vrijedi u svim tim kombinacijama.

**Traži se**

1. Odredi apsolutni tlak plina u spremniku i apsolutni tlak u dubljoj točki.
2. Odredi konzervativni najveći očekivani tlak u dubljoj točki i izaberi mjerno područje $0$–$140\ \text{kPa}$ ili $0$–$160\ \text{kPa}$ ako puna skala mora biti barem $5\ \%$ veća od najvećega očekivanog tlaka.

:::: {.content-visible .mf1-hint-online when-format="html"}
::: {.callout-note collapse="true" data-hint-key="true"}
### Naputak
Iz otvorenog manometra najprije odredi tlak u priključku, zatim se usponom kroz vodu vrati do plinskog prostora, a silaskom na dubinu $h_2$ dobij tlak u traženoj točki. Za konzervativnu gornju granicu istodobno uzmi najveće $p_{atm}$, $\Delta h$ i $h_2$, a najmanje $h_1$. Nakon toga primijeni zahtijevanu rezervu na mjerno područje; nominalna vrijednost sama nije dovoljna za izbor senzora.
:::
::::
:::: {.content-visible .mf1-answer-online when-format="html"}
::: {.callout-tip collapse="true" data-answer-key="true"}
### Kontrolni rezultat

$p_{pl} \approx 122{,}6\ \text{kPa}$ (aps.); na dubini $1{,}30\ \text{m}$: $p \approx 135{,}3\ \text{kPa}$. Konzervativna gornja granica iznosi $p_{max}\approx136{,}05\ \text{kPa}$, pa uz rezervu od $5\ \%$ treba puna skala od najmanje $142{,}85\ \text{kPa}$. Pretvornik $0$–$140\ \text{kPa}$ nije dostatan; bira se područje $0$–$160\ \text{kPa}$.
:::
::::

[Razina: T4]{.mf1-task-level}

:::::

![Skice uz Z1–Z6: barometarska visina, spremnici, slojevi fluida i manometri.](../assets/print/u03_vjezbe_skice.svg){#fig-u03-vjezbe fig-align="center" fig-alt="Skice uz Z1–Z6: dron s barometarskim senzorom iznad baze, određivanje razine iz razlike tlakova, nagnuti manometar s posudom, slojevi ulja i vode, mjerenje podtlaka i izbor apsolutnog senzora."}

**Napomene uz skice.** U Z1 visina leta nije u mjerilu. U Z3 nagib cjevčice i spuštanje razine u posudi nisu u mjerilu; nulta oznaka vrijedi za jednake tlakove. U Z4 granica slojeva ulja i vode nacrtana je shematski i bez krute pregrade, Z5 prikazuje jednu od triju odvojenih izvedbi, a u Z6 točka $A$ i granica vode i žive leže na istoj visini.

Kao most prema []{.mf1-chapter-ref target="u04"} usporedimo ravnotežu tlaka u spojenim posudama s efektivnim poljem sila.

![Jednak tlak na istoj dubini u spojenim posudama i nagnuta slobodna površina okomita na efektivno polje u ubrzanom spremniku.](../assets/print/u03_balans_tlaka_i_geff.svg){#fig-u03-staticka-zamjena-za-ravnotezu-tlaka-i-efektivno fig-alt="Lijevo spojene posude s vodom i točkama A i B na istoj dubini h, desno ubrzani spremnik s nagnutom površinom i trokutom vektora g, minus a i g_eff s kutom theta."}

**Tumačenje skice.** U spojenim posudama isti mirujući fluid na istoj dubini ima jednak tlak: $p_A=p_B=p_{pov}+\rho gh$. U ubrzanom spremniku slobodna površina okomita je na efektivno polje $\vec g_{eff}=\vec g-\vec a$. Za vodoravno ubrzanje vrijede $\tan\theta=a/g$ i $g_{eff}=\sqrt{g^2+a^2}$, što povezuje hidrostatiku s relativnim mirovanjem u sljedećem poglavlju.

## Sažetak

::: {.mf1-zavrsni-okvir}
- U fluidu koji miruje gradijent tlaka uravnotežuje volumenske sile: u jednolikom gravitacijskom polju vrijedi $dp/dz=-\rho g$, pa su plohe stalnoga tlaka vodoravne.
- Uz stalnu gustoću tlak raste linearno s dubinom, $p=p_{pov}+\rho gh$, za vodu oko $9{,}81\ \text{kPa}$ po metru; na istoj razini istoga povezanog mirujućeg fluida tlakovi su jednaki.
- U otvorenom spremniku tlak na slobodnoj površini atmosferski je, a u zatvorenom ga određuje stanje plinskoga prostora.
- Apsolutni tlak mjeri se prema idealnom vakuumu, manometarski prema lokalnom atmosferskom tlaku, $p_{aps}=p_{atm}+p_M$; vakuumski tlak opisuje sniženje apsolutnoga tlaka ispod atmosferskoga.
- Manometar je hod kroz spojene stupce: silaskom tlak raste za $\rho g\Delta h$, usponom pada za isti iznos, a za svaki segment uzima se gustoća pripadnoga fluida.
- Pri promjenjivoj gustoći, kao u atmosferi, gustoća ostaje pod integralom; stupac plina zanemaruje se samo kad je $\rho_{pl}g\Delta h$ zanemariv prema traženoj točnosti.
- Model vrijedi za fluid koji miruje u odnosu na stijenke; strujanje uvodi doprinose brzine i gubitaka, a ubrzani ili rotirajući spremnik efektivno polje sila.

**Najčešća pogreška.** Miješanje apsolutnog i manometarskog tlaka, primjerice usporedba manometarskog tlaka na usisu s tlakom pare $p_v$, koji je apsolutan.

**Nakon ovoga poglavlja mora biti moguće**

1. izvesti $dp/dz=-\rho g$ iz ravnoteže sloja i primijeniti $p=p_{pov}+\rho gh$ u otvorenom i zatvorenom spremniku;
2. provesti manometarski hod kroz više fluida s ispravnim predznacima i gustoćama;
3. dosljedno prevoditi apsolutni, manometarski i vakuumski tlak te procijeniti smije li se zanemariti stupac plina;
4. izabrati instrument ili pretvornik iz potrebne visine stupca, tlačne pogreške očitanja i zajamčenih tolerancija.
:::
