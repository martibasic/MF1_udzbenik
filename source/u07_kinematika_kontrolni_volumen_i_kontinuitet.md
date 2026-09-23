![Pregled poglavlja: kinematika, kontrolni volumen i kontinuitet.](../assets/print/u08_fig_uvod_pregled.svg){#fig-uvod-u08 fig-align="center" fig-alt="Pregled poglavlja: kinematika, kontrolni volumen i kontinuitet."}

## Kinematika, kontrolni volumen i kontinuitet

Kinematika strujanja može se opisati praćenjem pojedine čestice fluida ili promatranjem odabranoga dijela prostora kroz koji fluid protječe. Zapis $A_1 v_1 = A_2 v_2$ samo je poseban slučaj opće bilance mase, odnosno jednadžbe kontinuiteta.

::: {.mf1-application}
<p class="mf1-box-label">Inženjerski kontekst</p>

Kontrolni volumen omogućuje praćenje mase koja ulazi, izlazi i ostaje u odabranom prostoru. Tako se analiziraju rashladni razdjelnici, ventilacijske komore i spremnici tijekom punjenja ili pražnjenja. Granicu biramo tako da obuhvati sve relevantne ulaze i izlaze.
:::

**Procijenjeno vrijeme rada uz udžbenik:** 10 sati.

## Kinematika strujanja

Gibanje pojedine čestice može se pratiti njezinim položajem tijekom vremena. Za opis strujanja koriste se dva komplementarna pristupa:

- **Lagrangeov opis** prati pojedinu česticu fluida te njezin položaj i brzinu u vremenu.
- **Eulerov opis** određuje brzinu fluida u nepomičnim točkama prostora u funkciji vremena.

U inženjerskim se proračunima pretežno primjenjuje Eulerov opis jer određuje stanje strujanja na odabranom mjestu, primjerice u presjeku cijevi ili na ulazu u crpku.

### Polje brzine

U Eulerovu pogledu brzina je **polje** — vektor pridružen svakoj točki prostora i svakom trenutku:

$$
\vec{v} = \vec{v}(x, y, z, t).
$$ {#eq-kinematika-kv-polje-brzine-01}

To je središnji objekt cijele dinamike fluida: iz njega se određuje protok, a uz tlak i svojstva fluida računaju se sile i gubitci. Sva poglavlja koja slijede zapravo su načini da se to polje (ili barem njegova srednja vrijednost na nekom presjeku) odredi iz poznatih uvjeta.

::: {.mf1-fizikalno-znacenje}
<p class="mf1-box-label">Fizikalno značenje</p>
Polje brzine nije brzina jedne čestice, nego „snimka” brzina svih čestica odjednom. Ako u presjeku cijevi izmjerimo brzinu u svakoj točki, dobili smo dio polja brzine u tom trenutku. Zato senzor na fiksnom mjestu (Eulerov pogled) mjeri kako se mijenja brzina *tamo*, a ne što se događa s jednom određenom česticom koja je već prošla pokraj senzora.
:::

### Strujnica, trajektorija i strujna cijev

Iz polja brzine izvode se dvije krivulje koje se lako pomiješaju:

- **Strujnica** (linija strujanja) je krivulja koja je u **jednom trenutku** u svakoj svojoj točki tangentna na vektor brzine. To je trenutna „slika smjera” strujanja.
- **Trajektorija** (putanja) je stvarni put koji **jedna čestica** fluida prijeđe **kroz vrijeme**.

![Strujnica je tangentna na vektore brzine u istom trenutku; trajektorija je putanja jedne čestice kroz vrijeme. U stacionarnom strujanju obje krivulje imaju isti oblik.](../assets/print/u08_fig_kinematika.svg){#fig-u08-kinematika fig-align="center" fig-alt="Strujnica je tangentna na vektore brzine u istom trenutku; trajektorija je putanja jedne čestice kroz vrijeme. U stacionarnom strujanju obje krivulje imaju isti oblik."}

::: {.mf1-fizikalno-znacenje}
<p class="mf1-box-label">Fizikalno značenje</p>
U **stacionarnom** strujanju polje brzine se ne mijenja kroz vrijeme, pa čestica koja krene po strujnici zauvijek ostaje na njoj — strujnica i trajektorija se **podudaraju**. U **nestacionarnom** strujanju polje se mijenja dok čestica putuje, pa njezina trajektorija općenito ne prati trenutnu strujnicu i dvije se krivulje ne moraju podudarati. U MF1 gotovo uvijek radimo sa stacionarnim strujanjem, pa smijemo govoriti jednostavno o „strujnici”.
:::

Skup strujnica koje prolaze rubom neke male zatvorene krivulje tvori **strujnu cijev**. U stacionarnom strujanju fluid ne prolazi kroz njezin plašt jer je brzina na njega tangentna; tako dobivamo zamišljenu cijev omeđenu strujnicama. Upravo je strujna cijev geometrijska podloga za kontinuitet i za Bernoullijevu jednadžbu u <span class="mf1-ch-ref"><span class="mf1-ch-code">pog. 8</span><span class="mf1-ch-title">Energijska jednadžba i Bernoulli</span></span>.

### Stacionarno i nestacionarno strujanje

Strujanje je **stacionarno** ako se polje brzine (i tlak, gustoća…) u svakoj *fiksnoj točki* ne mijenja kroz vrijeme:

$$
\frac{\partial \vec{v}}{\partial t} = 0 \quad (\text{u svakoj točki prostora}).
$$ {#eq-kinematika-kv-stacionarno-i-nestacionarno-strujanje-01}

Pozor: stacionarno **ne znači** da se čestica ne ubrzava. Voda u suženju ustaljeno struji (slika se ne mijenja), ali svaka čestica koja uđe u suženje ubrzava jer prelazi u područje veće brzine. Nestacionarno strujanje javlja se pri pokretanju i zaustavljanju crpke, zatvaranju ventila ili pri punjenju i pražnjenju spremnika, gdje član akumulacije $dm_{CV}/dt$ nije nula.

### Od stvarnog profila do srednje brzine (1D model)

U potpuno razvijenom strujanju kroz ravnu kružnu cijev brzina nije jednaka po presjeku: uz stijenku pada na nulu zbog uvjeta prianjanja, a najveća je u osi. U općem presjeku profil ne mora biti osnosimetričan niti mu maksimum mora ležati u osi. Predznačeni volumenski protok kroz orijentiranu plohu računa se iz **normalne komponente** brzine:

$$
Q = \int_A \vec v\cdot\vec n\,dA = \int_A v_n\,dA .
$$ {#eq-kinematika-kv-od-stvarnog-profila-do-srednje-brzine-1d-01}

Da ne bismo u svakom zadatku integrirali cijeli profil, uvodi se **srednja (1D) brzina** — jedna brzina koja kroz isti presjek daje isti protok:

$$
\bar v_n = \frac{Q}{A} = \frac{1}{A}\int_A \vec v\cdot\vec n\,dA .
$$ {#eq-kinematika-kv-od-stvarnog-profila-do-srednje-brzine-1d-02}

Time složeni dvo- ili trodimenzijski profil zamjenjujemo jednim brojem po presjeku. To je **jednodimenzijski (1D) model** na kojem počiva cijela integralna analiza u MF1: kad god pišemo $Q = A\bar v$ ili $A_1\bar v_1 = A_2\bar v_2$, podrazumijevamo da je presjek okomit na glavni smjer strujanja i koristimo srednju normalnu, a ne vršnu brzinu. U nastavku se, radi kraćeg zapisa, crtica nad srednjom brzinom izostavlja.

::: {#ex-u08-srednja-brzina-iz-profila-brzine-t2 .mf1-we}
<p class="mf1-box-label">P1. Srednja brzina iz profila brzine&nbsp;<span class="mf1-level">T2</span></p>

**Kontekst:** U cijevi je brzina najveća u osi, a nula uz stijenku. Da bismo mogli koristiti jednostavni 1D kontinuitet, treba iz stvarnog profila odrediti srednju brzinu.

**Zadano**

- Polumjer cijevi: $R = 25\ \text{mm}$
- Profil brzine: $v(r) = v_{max}\left(1 - (r/R)^2\right)$, $v_{max} = 3{,}0\ \text{m/s}$

**Traženo**

1. srednju brzinu $v$ i njezin odnos prema $v_{max}$.
2. volumenski protok $Q$.

**Pretpostavke i model**

Strujanje je osnosimetrično i stacionarno; protok je $Q = \int_A v\,dA$ uz prstenasti element $dA = 2\pi r\, dr$.

**Rješenje**

Protok se dobiva integracijom profila po presjeku:

$$
Q = \int_0^R v_{max}\left(1 - \frac{r^2}{R^2}\right) 2\pi r\, dr = 2\pi v_{max}\left[\frac{R^2}{2} - \frac{R^2}{4}\right] = v_{max}\,\frac{\pi R^2}{2}.
$$ {#eq-kinematika-kv-rijeseni-primjer-srednja-brzina-iz-profila-brzin-01}

Srednja brzina je protok podijeljen površinom $A = \pi R^2$:

$$
v = \frac{Q}{A} = \frac{v_{max}\,\pi R^2/2}{\pi R^2} = \frac{v_{max}}{2} = 1{,}5\ \text{m/s}.
$$ {#eq-kinematika-kv-rijeseni-primjer-srednja-brzina-iz-profila-brzin-02}

Uz $A = \pi R^2 = \pi \cdot 0{,}025^2 = 1{,}963 \cdot 10^{-3}\ \text{m}^2$ slijedi

$$
Q = vA = 1{,}5 \cdot 1{,}963 \cdot 10^{-3} \approx 2{,}95 \cdot 10^{-3}\ \text{m}^3/\text{s} = 2{,}95\ \text{L/s}.
$$ {#eq-kinematika-kv-rijeseni-primjer-srednja-brzina-iz-profila-brzin-03}

**Provjera i komentar**

1. Za ovaj (parabolični) profil srednja je brzina točno **pola** vršne — koristan orijentir.
2. U 1D modelu cijeli profil zamjenjuje jedan broj $v = 1{,}5\ \text{m/s}$; upravo taj broj ulazi u $Q = Av$ i u kontinuitet.
3. Da smo pogrešno uzeli $v_{max}$ umjesto srednje brzine, protok bismo precijenili dvostruko.
:::

### Materijalna derivacija: ubrzanje čestice

Kad nas zanima ubrzanje **čestice** (a ono ulazi u Newtonov zakon i u sve dinamičke jednadžbe), ne smijemo samo derivirati polje po vremenu u fiksnoj točki. Čestica se ubrzava iz dva razloga: jer se polje s vremenom mijenja i jer čestica putuje u područje druge brzine. Oba doprinosa spaja **materijalna (supstancijalna) derivacija**:

$$
\vec{a} = \frac{D\vec{v}}{Dt} = \underbrace{\frac{\partial \vec{v}}{\partial t}}_{\text{lokalno}} + \underbrace{(\vec{v}\cdot\nabla)\vec{v}}_{\text{konvektivno}} .
$$ {#eq-kinematika-kv-materijalna-derivacija-ubrzanje-cestice-01}

::: {.mf1-fizikalno-znacenje}
<p class="mf1-box-label">Fizikalno značenje</p>
**Lokalni** član $\partial\vec{v}/\partial t$ opisuje ubrzanje zbog promjene brzine s vremenom u promatranoj točki (npr. pri pokretanju crpke). **Konvektivni** član $(\vec{v}\cdot\nabla)\vec{v}$ opisuje ubrzanje jer čestica putuje u područje druge brzine — točno ono što se događa u suženju gdje je strujanje stacionarno ($\partial\vec{v}/\partial t = 0$), a čestica ipak ubrzava. Zato voda u mlaznici ubrzava iako je „slika” strujanja nepromjenjiva: sav doprinos dolazi iz konvektivnog člana.
:::

Tu se materijalna derivacija zaustavlja na razini pojma. Eulerova jednadžba pojavljuje se u <span class="mf1-ch-ref"><span class="mf1-ch-code">pog. 8</span><span class="mf1-ch-title">Energijska jednadžba i Bernoulli</span></span>, integralna bilanca količine gibanja u <span class="mf1-ch-ref"><span class="mf1-ch-code">pog. 10</span><span class="mf1-ch-title">Količina i moment količine gibanja</span></span>, a puni lokalni izvod u <span class="mf1-ch-ref"><span class="mf1-ch-code">pog. 12</span><span class="mf1-ch-title">Diferencijalni opis realnog toka</span></span>.

## Kontrolni volumen i bilanca mase

Kad fluid struji, više nije praktično pratiti putanju iste čestice kroz vrijeme. Umjesto toga uvodi se kontrolni volumen: odabrani dio prostora kroz koji fluid može ulaziti, izlaziti i po potrebi se akumulirati.

Tu je korisno odmah razlikovati dva pogleda. Sustav ili kontrolna masa znači da se prati ista količina tvari i ne dopušta prijelaz mase preko granice. Kontrolni volumen znači da se prati odabrani dio prostora, dok masa smije prelaziti preko njegove granice.

U fluidnim uređajima poput difuzora, komore miješanja ili spremnika s promjenom razine upravo je drugi pogled prirodan, jer su ulazi, izlazi i akumulacija važniji od identiteta pojedine čestice. Formalni most između ta dva pogleda daje Reynoldsov teorem prijenosa, a kontinuitet u ovom poglavlju može se čitati kao njegova masena bilanca.

Najopćenitiji zapis je

$$\sum \dot{m}_{ulaz} - \sum \dot{m}_{izlaz} = \frac{dm_{CV}}{dt}$$ {#eq-kinematika-kv-fizikalni-uvod-i-matematicki-izvod-01}

::: {.mf1-fizikalno-znacenje}
<p class="mf1-box-label">Fizikalno značenje</p>
Ova bilanca mase pokazuje da je brzina promjene mase u kontrolnom volumenu jednaka razlici ulaznog i izlaznog masenog protoka. Ako ulazi više nego što izlazi, razina raste ili se masa skuplja. Ako izlazi više nego što ulazi, volumen se prazni. Kada nema akumulacije (stacionarno strujanje), masa koja uđe mora i izaći — ništa se ne može ni stvoriti ni izgubiti.
:::

Ako je strujanje stacionarno i nema akumulacije, to prelazi u

$$\sum \dot{m}_{ulaz} = \sum \dot{m}_{izlaz}$$ {#eq-kinematika-kv-fizikalno-znacenje-01}

Tu je važno ne pomiješati dvije različite veličine. Maseni protok $\dot m$ mjeri koliko mase prolazi u sekundi i uvijek je primarni zapis kontinuiteta, dok volumenski protok $Q$ mjeri koliko volumena prolazi u sekundi. Povezuje ih relacija

$$
\dot m = \rho Q,
\qquad
Q = Av.
$$ {#eq-kinematika-kv-fizikalno-znacenje-02}

Tek kad je riječ o istom nestlačivom fluidu kroz sve presjeke i kad je gustoća praktično ista, masena bilanca može se podijeliti s $\rho$ i prijeći u volumensku bilancu. Zato je u običnoj cijevi prirodno pisati $Q_1 = Q_2$, ali u miješanju dviju struja različitih gustoća najprije treba zatvoriti masenu bilancu, pa tek onda iz nje čitati gustoću ili volumenski protok mješavine.

Tek za jednu ulaznu i jednu izlaznu granu nestlačivoga fluida dobiva se poznati oblik

$$A_1 v_1 = A_2 v_2$$ {#eq-kinematika-kv-fizikalno-znacenje-03}

::: {.mf1-fizikalno-znacenje}
<p class="mf1-box-label">Fizikalno značenje</p>
Jednadžba $A_1 v_1 = A_2 v_2$ kaže da se pri stacionarnom toku kroz jednu strujnu cijev nestlačivoga fluida **srednja brzina** povećava kad se raspoloživa površina presjeka smanji. Zato se tok ubrzava u suženju cijevi. Za rijeku nije dovoljna sama dubina: mjerodavna je cijela površina poprečnog presjeka, koja ovisi i o širini korita, te raspodjela brzine po tom presjeku.
:::

::: {.mf1-interaktivno}
<p class="mf1-box-label">Interaktivni prikaz — Kontinuitet u suženju cijevi</p>

Interaktivni prikaz omogućuje mijenjanje ulaznog i izlaznog promjera te volumenskog protoka uz neposredno praćenje brzine fluida duž cijevi. Profil brzine jasno pokazuje koliko se brzina povećava u suženju u odnosu na ulazni presjek.

<div class="mf1-interaktivno-akcija">
<a class="mf1-interaktivno-veza" href="https://martibasic.github.io/MF1_udzbenik/jlite/lab/index.html?path=u08_kontinuitet_suzenje.ipynb">Pokreni u pregledniku</a>
<a class="mf1-interaktivno-veza" href="https://colab.research.google.com/github/martibasic/MF1_udzbenik/blob/main/notebooks/u08_kontinuitet_suzenje.ipynb" target="_blank" rel="noopener">Pričuvno: otvori u Colabu</a>
<img class="mf1-interaktivno-qr" src="../assets/qr/u08_kontinuitet_suzenje.svg" alt="QR kod za interaktivni prikaz kontinuiteta u suženju cijevi"/>
</div>

:::

::: {.mf1-izvod}
<p class="mf1-box-label">Matematički izvod — Bilanca mase u kontrolnom volumenu</p>

Opći kontinuitet nije nova formula nego integralni zapis očuvanja mase na kontrolnom volumenu $KV(t)$ omeđenom kontrolnom plohom $KP(t)$ s vanjskom normalom $\vec n$. Ako se kontrolna ploha lokalno giba brzinom $\vec v_{KP}$, masa je presijeca relativnom brzinom $\vec v-\vec v_{KP}$:

$$
\frac{d}{dt}\int_{KV(t)} \rho\,dV
+ \int_{KP(t)} \rho\bigl[(\vec v-\vec v_{KP})\cdot\vec n\bigr]\,dA = 0.
$$ {#eq-kinematika-kv-matematicki-izvod-bilanca-mase-u-kontrolnom-volu-01}

Prvi član predstavlja brzinu promjene mase unutar trenutačnoga kontrolnog volumena. Drugi predstavlja neto tok mase **kroz njegovu granicu**: predznak određuje skalarni produkt relativne brzine i vanjske normale. Za nepomičnu kontrolnu plohu vrijedi $\vec v_{KP}=0$, pa se dobiva oblik koji se koristi u spremnicima i nepomičnim cijevnim elementima:

$$
\frac{d}{dt}\int_{KV} \rho\,dV + \int_{KP} \rho(\vec v\cdot\vec n)\,dA=0.
$$ {#eq-kinematika-kv-matematicki-izvod-bilanca-mase-u-kontrolnom-volu-02}

Ako se kontrolna ploha rastavi na konačan broj presjeka na kojima se profil može čitati jednodimenzijski, površinski integral prelazi u zbroj članova

$$
\sum_k \rho_k A_k v_{n,k}.
$$ {#eq-kinematika-kv-matematicki-izvod-bilanca-mase-u-kontrolnom-volu-03}

Tada se opći zakon može zapisati kao

$$
\frac{dm_{CV}}{dt} + \sum \dot m_{izlaz} - \sum \dot m_{ulaz} = 0,
$$ {#eq-kinematika-kv-matematicki-izvod-bilanca-mase-u-kontrolnom-volu-04}

odnosno u poznatijem obliku

$$
\sum \dot m_{ulaz} - \sum \dot m_{izlaz} = \frac{dm_{CV}}{dt}.
$$ {#eq-kinematika-kv-matematicki-izvod-bilanca-mase-u-kontrolnom-volu-05}

Kad je tok stacionaran, član akumulacije nestaje pa slijedi

$$
\sum \dot m_{ulaz} = \sum \dot m_{izlaz}.
$$ {#eq-kinematika-kv-matematicki-izvod-bilanca-mase-u-kontrolnom-volu-06}

Tek ako je fluid pritom nestlačiv i ako postoji samo jedan ulazni i jedan izlazni presjek, maseni protoci prelaze u volumenske, pa dobiva se poseban slučaj

$$
\rho A_1v_1 = \rho A_2v_2
\qquad \Longrightarrow \qquad
A_1v_1 = A_2v_2.
$$ {#eq-kinematika-kv-matematicki-izvod-bilanca-mase-u-kontrolnom-volu-07}

Time se vidi puno fizikalno značenje kontinuiteta: jednadžba ne tvrdi da se dvije površine moraju „mehanički” poništiti, nego da se ukupna masa ne može izgubiti ni stvoriti između ulaza, izlaza i eventualne akumulacije unutar kontrolnog volumena.
:::

::: {.mf1-izvod}
<p class="mf1-box-label">Matematički izvod — Reynoldsov transportni teorem — opći okvir</p>

Sve integralne zakone mehanike fluida — očuvanje mase, količine gibanja i energije — povezuje jedinstveni matematički okvir poznat kao **Reynoldsov transportni teorem (RTT)**. On povezuje promjenu ekstenzivne veličine sustava, čija je pripadna specifična veličina $\eta$, s akumulacijom i protokom kroz proizvoljan kontrolni volumen. Kontrolni volumen može mirovati, gibati se ili deformirati.

Za proizvoljnu specifičnu veličinu $\eta$ RTT glasi

$$
\frac{d}{dt}\int_{sustav} \rho\eta\,dV
= \frac{d}{dt}\int_{KV(t)} \rho\eta\,dV
+ \int_{KP(t)} \rho\eta\bigl[(\vec v-\vec v_{KP})\cdot\vec n\bigr]\,dA.
$$ {#eq-kinematika-kv-matematicki-izvod-reynoldsov-transportni-teorem-01}

Prvi član s desne strane je **akumulacija** unutar kontrolnog volumena, drugi je **neto izlazni protok** kroz kontrolnu plohu. U članu protoka uvijek stoji brzina fluida **relativna prema plohi**. Za fiksni volumen $\vec v_{KP}=0$; za kontrolni volumen vezan uz lopaticu lokalno je $\vec v_{KP}=\vec u$, pa se u protoku pojavljuje relativna brzina $\vec w=\vec v-\vec u$. Sva tri osnovna zakona slijede iz RTT-a uz odgovarajući izbor $\eta$:

- **Očuvanje mase** ($\eta = 1$): $d/dt\int_{sustav}\rho\,dV = 0$, što daje jednadžbu kontinuiteta.
- **Količina gibanja** ($\eta = \vec{v}$): $d/dt\int_{sustav}\rho\vec{v}\,dV = \sum\vec{F}$, što daje integralni zakon iz <span class="mf1-ch-ref"><span class="mf1-ch-code">pog. 10</span><span class="mf1-ch-title">Količina i moment količine gibanja</span></span>.
- **Energija** ($\eta = e$, ukupna specifična energija): $d/dt\int_{sustav}\rho e\,dV = \dot{Q}-\dot{W}$, što vodi na energijsku jednadžbu u <span class="mf1-ch-ref"><span class="mf1-ch-code">pog. 8</span><span class="mf1-ch-title">Energijska jednadžba i Bernoulli</span></span>.

Zakoni se tako pojavljuju kao primjene istoga teorema na različite veličine. Član relativnoga protoka postaje presudan za pokretne lopatice u <span class="mf1-ch-ref"><span class="mf1-ch-code">pog. 14</span><span class="mf1-ch-title">Turbostrojevi i propulzija</span></span>.
:::

::: {.mf1-izvod}
<p class="mf1-box-label">Matematički izvod — Diferencijalni oblik kontinuiteta — iz integralnog preko teorema o divergenciji</p>

Integralni oblik kontinuiteta vrijedi za **proizvoljan** kontrolni volumen. Iz toga slijedi i **lokalni (diferencijalni) oblik** koji vrijedi u svakoj točki fluida — što je polazna jednadžba svake CFD analize.

Polazi se od integralnog zapisa

$$
\frac{d}{dt}\int_{KV}\rho\,dV + \int_{KP}\rho(\vec{v}\cdot\vec{n})\,dA = 0.
$$ {#eq-kinematika-kv-matematicki-izvod-diferencijalni-oblik-kontinuit-01}

Primjenom **teorema o divergenciji** površinski integral pretvara se u volumenski:

$$
\int_{KP}\rho(\vec{v}\cdot\vec{n})\,dA = \int_{KV}\nabla\cdot(\rho\vec{v})\,dV.
$$ {#eq-kinematika-kv-matematicki-izvod-diferencijalni-oblik-kontinuit-02}

Spajanjem dvaju članova pod jedan integral dobiva se

$$
\int_{KV}\!\left[\frac{\partial\rho}{\partial t} + \nabla\cdot(\rho\vec{v})\right]dV = 0.
$$ {#eq-kinematika-kv-matematicki-izvod-diferencijalni-oblik-kontinuit-03}

Kako ovaj integral mora iščeznuti za svaki kontrolni volumen, podintegralna funkcija sama mora biti nula u svakoj točki:

$$
\frac{\partial\rho}{\partial t} + \nabla\cdot(\rho\vec{v}) = 0.
$$ {#eq-kinematika-kv-matematicki-izvod-diferencijalni-oblik-kontinuit-04}

To je **diferencijalna jednadžba kontinuiteta** u najopćenitijem obliku — vrijedi i za stlačive i za nestlačive fluide. Za **nestlačivi fluid** ($\rho = \text{const.}$, pa $\partial\rho/\partial t = 0$ i $\nabla\rho = 0$) ona se reducira na

$$
\nabla\cdot\vec{v} = 0.
$$ {#eq-kinematika-kv-matematicki-izvod-diferencijalni-oblik-kontinuit-05}

Ova lokalna jednadžba čini polaznu točku diskretizacije u programima za CFD: u algoritmima SIMPLE i PISO tlak i brzina korigiraju se kako bi diskretni oblik uvjeta $\nabla\cdot\vec{v} = 0$ bio zadovoljen u svakoj ćeliji do zadane tolerancije.
:::

Sljedeći primjeri obuhvaćaju tri osnovne situacije: suženje ili difuzor, miješanje više struja i spremnik s promjenom razine. Zato se prije bilo koje jednadžbe najprije bira kontrolni volumen, pa se provjerava piše li se masena ili volumenska bilanca, radi li se o stacionarnom ili nestacionarnom problemu te postoji li jedna grana ili više ulaza i izlaza.

Preskakanje tih koraka može dovesti do neopravdanog pojednostavnjivanja zadatka.

::: {.mf1-numerika .kompakt}
<p class="mf1-box-label">Numerički trag — granice računskog volumena</p>

Ulaz, izlaz, stijenka i pokretna granica u simulaciji imaju istu ulogu kao granica ručnog kontrolnog volumena: određuju što preko nje može prijeći. Maseni protok zato se ne provjerava samo na jednom presjeku, nego na svim otvorenim granicama i zajedno s mogućom akumulacijom u domeni.
:::

::: {.mf1-numerika .kompakt}
<p class="mf1-box-label">Numerički trag — ćelija mreže</p>

Kontrolni volumen ručnoga računa u metodi konačnih volumena postaje jedna ćelija mreže. Zbroj tokova kroz njezine plohe i promjena mase u ćeliji moraju se zatvoriti lokalno, a zbroj preko cijele domene mora odgovarati svim otvorenim granicama.

Za stacionaran slučaj promatra se razlika ukupnih ulaznih i izlaznih masenih tokova, a za nestacionaran i promjena mase u domeni. Ta se neravnoteža iskazuje uz mjerilo protoka i promatranu izlaznu veličinu; univerzalni postotak prihvatljivosti nema fizikalni smisao.

Lokalno zatvaranje ćelija omogućuje otkrivanje izvora pogreške, ali ne jamči točnost vrtloga, pada tlaka ili slobodne površine. Zato se bilanca mase kombinira s mrežnom konvergencijom i neovisnom analitičkom ili mjernom usporedbom.
:::

## Riješeni primjeri

::: {#ex-u08-voda-struji-kroz-difuzor-t2 .mf1-we}
<p class="mf1-box-label">P2. Voda struji kroz difuzor&nbsp;<span class="mf1-level">T2</span></p>

**Kontekst:** U cjevovodu vodoopskrbnog sustava difuzor postupno proširuje presjek kako bi se smanjila brzina vode prije ulaska u sljedeći element. Projektant iz zadanih dimenzija i izlazne brzine određuje ulaznu brzinu te volumenski i maseni protok.

**Zadano**

- Ulazni promjer difuzora: $D_1 = 120\ \text{mm}$
- Izlazni promjer difuzora: $D_2 = 180\ \text{mm}$
- Srednja brzina na izlazu: $v_2 = 16\ \text{m/s}$
- Gustoća vode: $\rho = 998\ \text{kg/m}^3$

**Traženo**

1. srednju brzinu na ulazu $v_1$.
2. volumenski protok $Q$.
3. maseni protok $\dot{m}$.

![Difuzor i kontinuitet](../assets/print/u08_val1_difuzor_kontinuitet.svg){#fig-u08-difuzor-i-kontinuitet fig-alt="Difuzor i kontinuitet"}

**Pretpostavke i model**

Promatra se jedan kontrolni volumen s jednom ulaznom i jednom izlaznom granom. Kako je tok stacionaran, a voda se može uzeti nestlačivom, kroz oba presjeka mora prolaziti isti volumenski protok.

**Rješenje**

Za stacionarni tok nestlačivog fluida vrijedi $Q_1 = Q_2$, odnosno $A_1 v_1 = A_2 v_2$. Površine presjeka su

$$
A_1 = \frac{\pi D_1^2}{4} = \frac{\pi \cdot 0{,}12^2}{4} \approx 0{,}01131\ \text{m}^2,
$$ {#eq-kinematika-kv-rijeseni-primjer-voda-struji-kroz-difuzor-t2-01}

$$
A_2 = \frac{\pi D_2^2}{4} = \frac{\pi \cdot 0{,}18^2}{4} \approx 0{,}02545\ \text{m}^2.
$$ {#eq-kinematika-kv-rijeseni-primjer-voda-struji-kroz-difuzor-t2-02}

Iz kontinuiteta slijedi ulazna brzina

$$
v_1 = \frac{A_2}{A_1} v_2 = \left(\frac{0{,}18}{0{,}12}\right)^2 \cdot 16 = 36\ \text{m/s}.
$$ {#eq-kinematika-kv-rijeseni-primjer-voda-struji-kroz-difuzor-t2-03}

Volumenski protok može se sada izračunati iz bilo kojeg presjeka. Najjednostavnije je s izlaznog:

$$
Q = A_2 v_2 = 0{,}02545 \cdot 16 \approx 0{,}407\ \text{m}^3/\text{s}.
$$ {#eq-kinematika-kv-rijeseni-primjer-voda-struji-kroz-difuzor-t2-04}

Maseni protok zato iznosi

$$
\dot{m} = \rho Q = 998 \cdot 0{,}407 \approx 406\ \text{kg/s} \approx 4{,}06 \cdot 10^2\ \text{kg/s}.
$$ {#eq-kinematika-kv-rijeseni-primjer-voda-struji-kroz-difuzor-t2-05}

**Provjera i komentar**

U užem ulaznom presjeku brzina mora biti veća nego na izlazu, jer isti protok prolazi kroz manju površinu. U ovom difuzoru to daje ulaznu brzinu od $36\ \text{m/s}$, volumenski protok od oko $0{,}407\ \text{m}^3/\text{s}$ i maseni protok od oko $406\ \text{kg/s}$.

1. Kako je $D_2 > D_1$, mora biti $A_2 > A_1$ i zato $v_2 < v_1$.
2. Isti volumenski protok mora se dobiti i iz izraza $A_1 v_1$ i iz izraza $A_2 v_2$.
3. Ako brzina ispadne veća u širem presjeku, onda je odnos površina obrnut.
:::


U prethodnom primjeru difuzora ulazni i izlazni protok bili su jednaki. U spremniku iz sljedećeg primjera njihova razlika mijenja količinu fluida u kontrolnom volumenu.

::: {#ex-u08-izjednacni-spremnik-tijekom-ispiranja-filtra-t2 .mf1-we}
<p class="mf1-box-label">P3. Izjednačni spremnik tijekom ispiranja filtra&nbsp;<span class="mf1-level">T2</span></p>

**Kontekst:** Tijekom ispiranja filtra u sustavu za pripremu vode izjednačni spremnik prima više vode nego što se odvodi servisnim ispustom, pa razina postupno raste. Operater procjenjuje brzinu porasta razine, vrijeme dosizanja gornje radne granice i pripadnu akumuliranu masu.

**Zadano**

- Duljina pravokutnog izjednačnog spremnika: $L = 3{,}0\ \text{m}$
- Širina spremnika: $b = 1{,}8\ \text{m}$
- Stalni ulazni volumenski protok vode: $Q_{in} = 22\ \text{L/s} = 0{,}022\ \text{m}^3/\text{s}$
- Stalni izlazni protok kroz servisni odvod: $Q_{out} = 8\ \text{L/s} = 0{,}008\ \text{m}^3/\text{s}$
- Početna dubina vode: $h_0 = 0{,}45\ \text{m}$
- Gornja dopuštena radna razina: $h_1 = 1{,}20\ \text{m}$
- Gustoća vode: $\rho = 998\ \text{kg/m}^3$

**Traženo**

1. brzinu porasta razine vode $dh/dt$.
2. vrijeme potrebno da razina poraste od $h_0$ do $h_1$.
3. kolika se masa vode akumulira u spremniku do tog trenutka.

![Izjednačni spremnik s akumulacijom](../assets/print/u08_val3_izjednacni_spremnik.svg){#fig-u08-izjednacni-spremnik-s-akumulacijom fig-alt="Izjednačni spremnik s akumulacijom"}

**Pretpostavke i model**

Promatra se kontrolni volumen koji obuhvaća cijeli spremnik. Tekućina je ista na ulazu i izlazu, gustoća se uzima konstantnom, a tlocrtna površina spremnika ne mijenja se s visinom. Zato se član akumulacije može zapisati preko promjene volumena, odnosno preko promjene razine.

**Rješenje**

Tlocrtna površina spremnika iznosi

$$
A_T = Lb = 3{,}0 \cdot 1{,}8 = 5{,}40\ \text{m}^2.
$$ {#eq-kinematika-kv-rijeseni-primjer-izjednacni-spremnik-tijekom-isp-01}

Za nestacionarno stanje u spremniku vrijedi $Q_{in} - Q_{out} = dV/dt$. Kako je $V = A_T h$, slijedi

$$
\frac{dh}{dt} = \frac{Q_{in} - Q_{out}}{A_T} = \frac{0{,}022 - 0{,}008}{5{,}40} \approx 2{,}59 \cdot 10^{-3}\ \text{m/s} \approx 0{,}155\ \text{m/min}.
$$ {#eq-kinematika-kv-rijeseni-primjer-izjednacni-spremnik-tijekom-isp-02}

Porast razine koji nas zanima iznosi

$$
\Delta h = h_1 - h_0 = 1{,}20 - 0{,}45 = 0{,}75\ \text{m},
$$ {#eq-kinematika-kv-rijeseni-primjer-izjednacni-spremnik-tijekom-isp-03}

pa je pripadni akumulirani volumen

$$
\Delta V = A_T \Delta h = 5{,}40 \cdot 0{,}75 = 4{,}05\ \text{m}^3.
$$ {#eq-kinematika-kv-rijeseni-primjer-izjednacni-spremnik-tijekom-isp-04}

Vrijeme potrebno za takvu akumulaciju je

$$
t = \frac{\Delta V}{Q_{in} - Q_{out}} = \frac{4{,}05}{0{,}014} \approx 289\ \text{s} \approx 4{,}82\ \text{min}.
$$ {#eq-kinematika-kv-rijeseni-primjer-izjednacni-spremnik-tijekom-isp-05}

Masa vode koja se do tada akumulira iznosi

$$
\Delta m = \rho \Delta V = 998 \cdot 4{,}05 \approx 4{,}04 \cdot 10^3\ \text{kg} \approx 4040\ \text{kg}.
$$ {#eq-kinematika-kv-rijeseni-primjer-izjednacni-spremnik-tijekom-isp-06}

**Provjera i komentar**

Razina vode u spremniku raste brzinom od oko $0{,}155\ \text{m/min}$, do gornje radne razine dolazi za oko $4{,}8$ minuta, a u tom se vremenu u spremniku akumulira oko $4{,}04\ \text{t}$ vode. To je tipičan primjer <span class="mf1-ch-ref"><span class="mf1-ch-code">pog. 7</span><span class="mf1-ch-title">Kinematika, kontrolni volumen i kontinuitet</span></span> u kojem razlika protoka postaje porast mase unutar kontrolnog volumena.

1. Kako je $Q_{in} > Q_{out}$, razina mora rasti, a ne padati.
2. Neto protok od $14\ \text{L/s}$ na spremniku tlocrtne površine $5{,}4\ \text{m}^2$ mora dati spor, ali mjerljiv rast razine reda nekoliko desetina metra u minuti.
3. Kad bi bilo $Q_{in} = Q_{out}$, član akumulacije bi nestao i problem bi se vratio na stacionarni slučaj.
:::

::: {#ex-u08-mijesajuci-izjednacni-spremnik-s-porastom-razine-t3 .mf1-ch}
<p class="mf1-box-label">P4. Izjednačni spremnik s miješanjem i porastom razine&nbsp;<span class="mf1-level">T3</span></p>

**Kontekst:** U procesnom postrojenju miješajući izjednačni spremnik prima vodu i slanu otopinu iz dvaju ulaznih vodova, a homogenizirana mješavina izlazi kroz zajednički vod sporije nego što ulazi, pa razina postupno raste. Procesnom inženjeru trebaju izlazni protok, gustoća mješavine, brzina porasta razine te masa koja se akumulira u radnom rasponu.

**Zadano**

- Tlocrtne dimenzije pravokutnog miješajućeg izjednačnog spremnika: $L = 4{,}2\ \text{m}$, $b = 1{,}5\ \text{m}$
- Gustoća vode (ulazna struja A): $\rho_A = 1000\ \text{kg/m}^3$
- Volumenski protok vode: $Q_A = 18\ \text{L/s} = 0{,}018\ \text{m}^3/\text{s}$
- Relativna gustoća slane otopine (ulazna struja B): $s_B = 1{,}10$
- Volumenski protok slane otopine: $Q_B = 6\ \text{L/s} = 0{,}006\ \text{m}^3/\text{s}$
- Promjer izlaznog voda: $D_3 = 100\ \text{mm}$
- Trenutna srednja izlazna brzina: $v_3 = 1{,}80\ \text{m/s}$
- Spremnik je dobro izmiješan, gustoća u spremniku jednaka je gustoći mješavine ulaznih struja
- Početna razina: $h_0 = 0{,}80\ \text{m}$; razmatra se porast do $h_1 = 1{,}20\ \text{m}$

**Traženo**

1. izlazni volumenski protok $Q_3$.
2. gustoću homogenizirane mješavine u spremniku i izlaznom vodu $\rho_3$.
3. brzinu porasta razine $dh/dt$.
4. vrijeme potrebno da razina poraste od $h_0$ do $h_1$.
5. masu tekućine koja se akumulira u spremniku tijekom tog porasta.

![Miješajući izjednačni spremnik](../assets/print/u08_ch1_mijesajuci_spremnik.svg){#fig-u08-mijesajuci-izjednacni-spremnik fig-alt="Miješajući izjednačni spremnik"}

**Pretpostavke i model**

Ovdje jedan kontrolni volumen obuhvaća cijeli spremnik. Izlazni tok zatvara se preko relacije $Q_3 = A_3 v_3$, gustoća homogenizirane mješavine dobiva se iz masene bilance ulaza, a porast razine dolazi iz volumenske akumulacije. U promatranom intervalu protoci su stalni, volumeni se pri miješanju zbrajaju, a početni sadržaj spremnika ima isti sastav kao spojeni dotoci. Ključ nije formula nego redoslijed: izlazni tok, zatim gustoća mješavine, pa tek onda član akumulacije.

**Rješenje**

Najprije od relativne gustoće dobivamo gustoću slane otopine:

$$
\rho_B = s_B \rho_A = 1{,}10 \cdot 1000 = 1100\ \text{kg/m}^3.
$$ {#eq-kinematika-kv-cjeloviti-zadatak-mijesajuci-izjednacni-spremnik-01}

Površina izlaznog presjeka iznosi

$$
A_3 = \frac{\pi D_3^2}{4} = \frac{\pi \cdot 0{,}10^2}{4} \approx 7{,}854 \cdot 10^{-3}\ \text{m}^2,
$$ {#eq-kinematika-kv-cjeloviti-zadatak-mijesajuci-izjednacni-spremnik-02}

zato je izlazni volumenski protok

$$
Q_3 = A_3 v_3 = 7{,}854 \cdot 10^{-3} \cdot 1{,}80 \approx 1{,}414 \cdot 10^{-2}\ \text{m}^3/\text{s} \approx 14{,}1\ \text{L/s}.
$$ {#eq-kinematika-kv-cjeloviti-zadatak-mijesajuci-izjednacni-spremnik-03}

Za homogeniziranu mješavinu najprije zatvaramo masenu bilancu dviju ulaznih struja. Ukupni ulazni maseni protok je

$$
\dot{m}_{in} = \rho_A Q_A + \rho_B Q_B = 1000 \cdot 0{,}018 + 1100 \cdot 0{,}006 = 18 + 6{,}6 = 24{,}6\ \text{kg/s}.
$$ {#eq-kinematika-kv-cjeloviti-zadatak-mijesajuci-izjednacni-spremnik-04}

Ukupni ulazni volumenski protok iznosi

$$
Q_{in} = Q_A + Q_B = 0{,}018 + 0{,}006 = 0{,}024\ \text{m}^3/\text{s},
$$ {#eq-kinematika-kv-cjeloviti-zadatak-mijesajuci-izjednacni-spremnik-05}

pa je gustoća homogenizirane mješavine

$$
\rho_3 = \frac{\dot{m}_{in}}{Q_{in}} = \frac{24{,}6}{0{,}024} = 1025\ \text{kg/m}^3.
$$ {#eq-kinematika-kv-cjeloviti-zadatak-mijesajuci-izjednacni-spremnik-06}

Tlocrtna površina spremnika iznosi

$$
A_T = Lb = 4{,}2 \cdot 1{,}5 = 6{,}30\ \text{m}^2.
$$ {#eq-kinematika-kv-cjeloviti-zadatak-mijesajuci-izjednacni-spremnik-07}

Za volumensku akumulaciju vrijedi $Q_A + Q_B - Q_3 = A_T \,dh/dt$, odnosno

$$
\frac{dh}{dt} = \frac{0{,}024 - 0{,}01414}{6{,}30} \approx 1{,}57 \cdot 10^{-3}\ \text{m/s} \approx 0{,}094\ \text{m/min}.
$$ {#eq-kinematika-kv-cjeloviti-zadatak-mijesajuci-izjednacni-spremnik-08}

Porast razine iznosi

$$
\Delta h = h_1 - h_0 = 1{,}20 - 0{,}80 = 0{,}40\ \text{m},
$$ {#eq-kinematika-kv-cjeloviti-zadatak-mijesajuci-izjednacni-spremnik-09}

pa je akumulirani volumen

$$
\Delta V = A_T \Delta h = 6{,}30 \cdot 0{,}40 = 2{,}52\ \text{m}^3.
$$ {#eq-kinematika-kv-cjeloviti-zadatak-mijesajuci-izjednacni-spremnik-10}

Vrijeme potrebno za takav porast razine iznosi

$$
t = \frac{\Delta V}{Q_A + Q_B - Q_3} = \frac{2{,}52}{0{,}024 - 0{,}01414} \approx 255\ \text{s} \approx 4{,}26\ \text{min}.
$$ {#eq-kinematika-kv-cjeloviti-zadatak-mijesajuci-izjednacni-spremnik-11}

Masa koja se u tom intervalu akumulira u spremniku iznosi

$$
\Delta m = \rho_3 \Delta V = 1025 \cdot 2{,}52 \approx 2583\ \text{kg} \approx 2{,}58\ \text{t}.
$$ {#eq-kinematika-kv-cjeloviti-zadatak-mijesajuci-izjednacni-spremnik-12}

**Provjera i komentar**

Ovaj zadatak povezuje postupke iz <span class="mf1-ch-ref"><span class="mf1-ch-code">pog. 7</span><span class="mf1-ch-title">Kinematika, kontrolni volumen i kontinuitet</span></span> u jednom kontrolnom volumenu: izlazni vod daje $Q_3 \approx 14{,}1\ \text{L/s}$, mješavina u spremniku ima gustoću oko $1025\ \text{kg/m}^3$, razina raste brzinom oko $0{,}094\ \text{m/min}$, a do porasta od $0{,}40\ \text{m}$ treba oko $4{,}3$ minute. U tom se vremenu akumulira oko $2{,}58$ t homogenizirane tekućine.

1. Gustoća mješavine mora biti između gustoće vode i gustoće slane otopine.
2. Kako je ukupni ulazni protok veći od izlaznog, razina mora rasti, a ne padati.
3. Ako se u ovom zadatku odmah napiše samo jedna formula kontinuiteta bez razdvajanja ulazne mase, izlaznog toka i akumulacije, gotovo sigurno će se izgubiti barem jedna fizikalna veza.
:::

Kao sažetak poglavlja korisno je usporediti tri reprezentativna slučaja: suženje, difuzor i kontrolni volumen s više tokova. Uz njih prirodno stoji i standardna shema bilance mase s označenim ulazima, izlazima i akumulacijom.

![Kontrolni volumen i kontinuitet](../assets/print/u08_kontrolni_volumen_scene.svg){#fig-u08-staticka-zamjena-za-kontrolni-volumen-i-kontinuitet fig-alt="Kontrolni volumen i kontinuitet"}

::: {#ex-u08-kontinuitet-kroz-razvodni-t-komad-hidraulicnog-sustava .mf1-we}
<p class="mf1-box-label">P5. Kontinuitet kroz razvodni T-komad hidrauličnog sustava &nbsp;<span class="mf1-level">T2</span></p>


**Kontekst:** U hidrauličnom sustavu strojnice T-komad dijeli ulazni tok ulja iz crpke u dva ogranka: jedan za radni cilindar, drugi za hladnjak ulja. Projektant provjerava brzine u ograncima.

**Zadano**

- Ulazna cijev: $D_1 = 32\ \text{mm}$, $v_1 = 4{,}5\ \text{m/s}$
- Ogranak 1 (radni cilindar): $D_2 = 20\ \text{mm}$, volumni udio $60\%$ ulaznog toka
- Ogranak 2 (hladnjak): $D_3 = ?$ mm, dobiva preostalih $40\%$
- Gustoća ulja: $\rho = 870\ \text{kg/m}^3$

**Traženo**

1. Volumni protok $Q_1$ na ulazu.
2. Protoci $Q_2$ i $Q_3$ u ograncima.
3. Brzina $v_2$ u ogranku 1 i potrebni promjer $D_3$ ako je $v_3 = 3{,}0\ \text{m/s}$.

![Razvodni T-komad: D1=32 mm, D2=20 mm, v1=4,5 m/s, 60%/40% raspodjela](../assets/print/u08_fig_t_komad_hidraulika.svg){#fig-u08-t-komad-hidraulika fig-align="center" fig-alt="Razvodni T-komad: D1=32 mm, D2=20 mm, v1=4,5 m/s, 60%/40% raspodjela"}

**Rješenje**

$$
A_1 = \frac{\pi D_1^2}{4} = \frac{\pi \cdot 0{,}032^2}{4} = 8{,}042 \cdot 10^{-4}\ \text{m}^2
$$ {#eq-kinematika-kv-rijeseni-primjer-kontinuitet-kroz-razvodni-t-kom-01}

$$
Q_1 = A_1 v_1 = 8{,}042 \cdot 10^{-4} \cdot 4{,}5 = 3{,}619 \cdot 10^{-3}\ \text{m}^3/\text{s} = 3{,}62\ \text{L/s}
$$ {#eq-kinematika-kv-rijeseni-primjer-kontinuitet-kroz-razvodni-t-kom-02}

$$
Q_2 = 0{,}60 \cdot Q_1 = 2{,}17\ \text{L/s}, \quad Q_3 = 0{,}40 \cdot Q_1 = 1{,}45\ \text{L/s}
$$ {#eq-kinematika-kv-rijeseni-primjer-kontinuitet-kroz-razvodni-t-kom-03}

$$
A_2 = \frac{\pi \cdot 0{,}020^2}{4} = 3{,}142 \cdot 10^{-4}\ \text{m}^2, \quad v_2 = \frac{Q_2}{A_2} = \frac{2{,}17 \cdot 10^{-3}}{3{,}142 \cdot 10^{-4}} = 6{,}9\ \text{m/s}
$$ {#eq-kinematika-kv-rijeseni-primjer-kontinuitet-kroz-razvodni-t-kom-04}

$$
A_3 = \frac{Q_3}{v_3} = \frac{1{,}45 \cdot 10^{-3}}{3{,}0} = 4{,}83 \cdot 10^{-4}\ \text{m}^2 \Rightarrow D_3 = \sqrt{\frac{4 A_3}{\pi}} = 24{,}8\ \text{mm}
$$ {#eq-kinematika-kv-rijeseni-primjer-kontinuitet-kroz-razvodni-t-kom-05}

**Provjera i komentar**

Provjera: $Q_2 + Q_3 = 2{,}17 + 1{,}45 = 3{,}62\ \text{L/s} = Q_1$. Brzina $v_2 = 6{,}9\ \text{m/s}$ može se smanjiti povećanjem promjera. Ako se za usporedbu zada cilj manji od 6 m/s, povećanje $D_2$ na primjerice 22 mm zadovoljava taj cilj pri istom protoku. To je ilustracija izbora promjera, a ne univerzalna preporuka za hidraulične vodove.

:::

Razdjelnik rashladnog kruga primjenjuje istu višegransku bilancu, ali dodaje odluku o posljedicama blokade jedne grane.

::: {#ex-u08-rashladni-krug-baterijskog-paketa-elektricnog-vozila-t2 .mf1-we}
<p class="mf1-box-label">P6. Rashladni krug baterijskog paketa električnog vozila &nbsp;<span class="mf1-level">T2</span></p>

**Kontekst:** Rashladni kolektor baterijskog paketa razdjeljuje zadani protok na više paralelnih kanala. Primjer ispituje samo volumensku bilancu pri zatvaranju jedne grane; temperatura ćelija i upravljačka logika nisu dio modela.

**Zadano**

- Promjer glavnog voda: $D_1 = 20\ \text{mm}$
- Promjer pojedinog rashladnog kanala uz modul: $d = 6\ \text{mm}$
- Broj paralelnih kanala: $n = 16$
- Ukupni volumenski protok rashladnog medija: $Q = 25\ \text{L/min}$

**Traženo**

1. Srednja brzina rashladnog medija u glavnom vodu;
2. Srednja brzina u jednom paralelnom kanalu;
3. Procjena: što se događa s brzinom u preostalim kanalima ako se jedan začepi?

**Pretpostavke i model**

Rashladni medij smatra se nestlačivim, gustoća se ne mijenja s temperaturom u promatranom radnom rasponu. Strujanje je stacionarno, profili brzina u presjecima aproksimirani su jednodimenzijskim srednjim vrijednostima. Svi paralelni kanali imaju iste dimenzije i isti hidraulički otpor, pa se ukupni protok raspoređuje jednoliko na sve aktivne kanale.

**Rješenje**

Pretvorba protoka u SI jedinice:

$$
Q = 25\ \text{L/min} = \frac{25 \cdot 10^{-3}}{60} = 4{,}167 \cdot 10^{-4}\ \text{m}^3/\text{s}.
$$ {#eq-kinematika-kv-rijeseni-primjer-rashladni-krug-baterijskog-pake-01}

Površina glavnog voda:

$$
A_1 = \frac{\pi D_1^2}{4} = \frac{\pi \cdot 0{,}020^2}{4} \approx 3{,}142 \cdot 10^{-4}\ \text{m}^2.
$$ {#eq-kinematika-kv-rijeseni-primjer-rashladni-krug-baterijskog-pake-02}

Srednja brzina u glavnom vodu:

$$
v_1 = \frac{Q}{A_1} = \frac{4{,}167 \cdot 10^{-4}}{3{,}142 \cdot 10^{-4}} \approx 1{,}326\ \text{m/s}.
$$ {#eq-kinematika-kv-rijeseni-primjer-rashladni-krug-baterijskog-pake-03}

Površina pojedinog kanala:

$$
A_d = \frac{\pi d^2}{4} = \frac{\pi \cdot 0{,}006^2}{4} \approx 2{,}827 \cdot 10^{-5}\ \text{m}^2.
$$ {#eq-kinematika-kv-rijeseni-primjer-rashladni-krug-baterijskog-pake-04}

Ukupna površina svih paralelnih kanala:

$$
A_{n} = n \cdot A_d = 16 \cdot 2{,}827 \cdot 10^{-5} \approx 4{,}524 \cdot 10^{-4}\ \text{m}^2.
$$ {#eq-kinematika-kv-rijeseni-primjer-rashladni-krug-baterijskog-pake-05}

Srednja brzina u pojedinom kanalu:

$$
v_d = \frac{Q}{A_{n}} = \frac{4{,}167 \cdot 10^{-4}}{4{,}524 \cdot 10^{-4}} \approx 0{,}921\ \text{m/s}.
$$ {#eq-kinematika-kv-rijeseni-primjer-rashladni-krug-baterijskog-pake-06}

Pri začepljenju jednog od kanala broj aktivnih kanala pada na $n' = 15$, ukupna površina iznosi $A_n' = 15 \cdot 2{,}827 \cdot 10^{-5} = 4{,}241 \cdot 10^{-4}\ \text{m}^2$, a brzina u preostalim kanalima raste na

$$
v_d' = \frac{Q}{A_{n}'} = \frac{4{,}167 \cdot 10^{-4}}{4{,}241 \cdot 10^{-4}} \approx 0{,}982\ \text{m/s},
$$ {#eq-kinematika-kv-rijeseni-primjer-rashladni-krug-baterijskog-pake-07}

što je porast od približno $6{,}6\,\%$.

**Provjera i komentar**

Zatvaranje jedne od šesnaest jednakih grana u zadanom modelu povećava brzinu u ostalima za približno $6{,}6\,\%$. Iz toga se ne može zaključiti da je kvar toplinski ili sigurnosno prihvatljiv: blokirana grana nema protok, a procjena temperature zahtijeva toplinsku bilancu, svojstva ćelija, kontaktne otpore, senzore i konkretnu strategiju zaštite.
:::

::: {.mf1-samoprovjera}
<p class="mf1-box-label">Provjeri sebe</p>

Sljedeća pitanja služe za samostalnu provjeru razumijevanja prije prelaska na zadatke za vježbu.

1. U kojem slučaju vrijedi pojednostavljeni oblik $A_1 v_1 = A_2 v_2$, a kada ga treba zamijeniti općim integralnim oblikom bilance mase?

::: {.callout-note collapse="true"}
### Odgovor
Pojednostavljeni oblik vrijedi za stacionarno strujanje jednog nestlačivog fluida kroz jedan ulaz i jedan izlaz uz uporabu srednjih normalnih brzina po presjecima. U slučaju više ulaza i izlaza, akumulacije u kontrolnom volumenu ili miješanja fluida različitih gustoća, treba primijeniti opću masenu bilancu $\sum \dot{m}_{ul} = \sum \dot{m}_{iz} + \mathrm{d}m/\mathrm{d}t$.
:::

2. Po čemu se razlikuje masena bilanca od volumenske, i kada njihova razlika postaje važna?

::: {.callout-note collapse="true"}
### Odgovor
Masena bilanca koristi protoke izražene preko $\dot{m} = \rho Q$, dok volumenska bilanca uspoređuje izravno $Q$. Pri nestlačivom strujanju jednog fluida obje su ekvivalentne, ali pri miješanju fluida različitih gustoća (slatka i slana voda, ulje i voda) ili pri različitim gustoćama na ulazu i izlazu treba najprije postaviti masenu bilancu; zbrajanje volumenskih protoka zahtijeva dodatne pretpostavke.
:::

3. Što fizikalno predstavlja član $\mathrm{d}m/\mathrm{d}t$ u općem zakonu kontinuiteta?

::: {.callout-note collapse="true"}
### Odgovor
Predstavlja brzinu promjene ukupne mase fluida unutar kontrolnog volumena. Ako je veći od nule, masa se akumulira (spremnik se puni); ako je manji od nule, masa u kontrolnom volumenu se smanjuje; ako je nula, nema neto akumulacije mase, što samo po sebi ne dokazuje da je cijelo strujanje stacionarno.
:::

4. Zašto je za pravilan proračun nužno najprije nacrtati kontrolni volumen?

::: {.callout-note collapse="true"}
### Odgovor
Najprije zatvori kontrolnu plohu i označi sve ulaze i izlaze. Zatim provjeri postoji li akumulacija. Izostavljena grana ili zanemarena promjena mase u spremniku dovodi do pogrešne bilance i kad je račun algebarski točan.
:::
:::

## Zadaci za vježbu

U cijevima i nepomičnim komorama Z1, Z3 i Z4 tok je stacionaran, voda nestlačiva i gustoće $\rho=998\ \text{kg/m}^3$, a brzine su srednje po presjeku.

::::: {.mf1-vjezbe-list}

### Z1. Protok kroz proširenje cijevi {#task-u08-voda-struji-kroz-cijev-koja-se-siri .unnumbered .unlisted}

Voda struji kroz cijev koja se širi s promjera $D_1 = 0{,}10\ \text{m}$ na $D_2 = 0{,}16\ \text{m}$. Ako je ulazna srednja brzina $v_1 = 4{,}8\ \text{m/s}$, a gustoća vode $\rho = 998\ \text{kg/m}^3$, odredi izlaznu brzinu, volumenski protok i maseni protok.

:::: {.content-visible .mf1-hint-online when-format="html"}
::: {.callout-note collapse="true" data-hint-key="true"}
### Naputak
Najprije izračunaj $Q = A_1 v_1$, zatim $v_2 = Q/A_2$ i na kraju $\dot m = \rho Q$.
:::
::::
:::: {.content-visible .mf1-answer-online when-format="html"}
::: {.callout-tip collapse="true" data-answer-key="true"}
### Kontrolni rezultat

$Q \approx 37{,}7\ \text{L/s}$; $v_2 \approx 1{,}88\ \text{m/s}$; $\dot m \approx 37{,}6\ \text{kg/s}$.
:::
::::

[Razina: T1]{.mf1-task-level}

<span id="task-u08-voda-ulazi-u-sapnicu-promjera-srednjom-brzinom"></span>

### Z2. Protok kroz kosu kontrolnu plohu {#task-protok-kroz-kosu-kontrolnu-plohu .unnumbered .unlisted}

U širokom toku vode odabrana je nepomična zamišljena ravna ploha površine $A=0{,}0040\ \text{m}^2$. Brzina vode jednolika je na toj plohi i iznosi $v=3{,}0\ \text{m/s}$. Kut između brzine i odabrane jedinične normale $\vec n$ iznosi $\alpha=60^\circ$, a gustoća vode je $\rho=998\ \text{kg/m}^3$. Ploha nije kruta stijenka i ne ometa strujanje.

Odredi predznačeni volumenski i maseni protok kroz plohu. Što se mijenja ako istu plohu orijentiramo suprotnom normalom?

:::: {.content-visible .mf1-hint-online when-format="html"}
::: {.callout-note collapse="true" data-hint-key="true"}
### Naputak
Protok određuje normalna komponenta brzine: $Q=Av\cos\alpha$. Kut je zadan prema normali, a ne prema samoj plohi.
:::
::::
:::: {.content-visible .mf1-answer-online when-format="html"}
::: {.callout-tip collapse="true" data-answer-key="true"}
### Kontrolni rezultat

$v_n=1{,}50\ \text{m/s}$; $Q=+6{,}00\ \text{L/s}$; $\dot m=+5{,}988\ \text{kg/s}$. Za suprotnu normalu protoci su $-6{,}00\ \text{L/s}$ i $-5{,}988\ \text{kg/s}$; fizički tok ostaje isti.
:::
::::

[Razina: T1]{.mf1-task-level}

### Z3. Bilanca komore za miješanje {#task-u08-u-komoru-za-mijesanje-ulaze-dvije-vodene .unnumbered .unlisted}

U stacionarnu komoru ulaze dvije vodene struje protoka $Q_1=12\ \text{L/s}$ i $Q_2=8\ \text{L/s}$. Jedini izlaz ima promjer $D_3=120\ \text{mm}$. Odredi izlaznu srednju brzinu i napiši masenu bilancu; nema akumulacije ni drugih priključaka.

:::: {.content-visible .mf1-hint-online when-format="html"}
::: {.callout-note collapse="true" data-hint-key="true"}
### Naputak
Za stacionarnu komoru za miješanje vrijedi $\dot m_1 + \dot m_2 = \dot m_3$; za vodu je dovoljno računati preko volumenskih protoka.
:::
::::
:::: {.content-visible .mf1-answer-online when-format="html"}
::: {.callout-tip collapse="true" data-answer-key="true"}
### Kontrolni rezultat

$Q_3 = 20\ \text{L/s}$; $v_3 \approx 1{,}77\ \text{m/s}$.
:::
::::

[Razina: T2]{.mf1-task-level}

### Z4. Raspodjela protoka u dvije grane {#task-u08-u-razdjelnu-glavu-ulazi-voda-protokom-kroz .unnumbered .unlisted}

U razdjelnu glavu ulazi voda protokom $Q = 0{,}030\ \text{m}^3/\text{s}$ kroz cijev promjera $D_1 = 140\ \text{mm}$. Voda izlazi kroz dvije grane promjera $D_2 = 90\ \text{mm}$ i $D_3 = 70\ \text{mm}$, pri čemu je zadano da je brzina u izlaznoj grani 2 dvostruko veća od brzine u izlaznoj grani 3. Taj omjer određuje radni režim, a ne slijedi samo iz promjera. Odredi protoke u granama.

:::: {.content-visible .mf1-hint-online when-format="html"}
::: {.callout-note collapse="true" data-hint-key="true"}
### Naputak
Postavi $Q = Q_2 + Q_3$ i vezu brzina $v_2 = 2v_3$; preko $Q = Av$ zatvori sustav za dvije nepoznanice.
:::
::::
:::: {.content-visible .mf1-answer-online when-format="html"}
::: {.callout-tip collapse="true" data-answer-key="true"}
### Kontrolni rezultat

$v_3 \approx 1{,}81\ \text{m/s}$, $v_2 \approx 3{,}62\ \text{m/s}$; $Q_2 \approx 23{,}0\ \text{L/s}$, $Q_3 \approx 7{,}0\ \text{L/s}$.
:::
::::

[Razina: T2]{.mf1-task-level}

<span id="task-u08-cilindricni-spremnik-promjera-puni-se-dotokom-dok"></span>

### Z5. Klip s protočnim otvorom {#task-klip-s-protocnim-otvorom .unnumbered .unlisted}

Vodom ispunjena vodoravna dozirna komora ima nepomični cilindar i klip koji se pomiče udesno. Voda ulazi kroz nepomični lijevi priključak, a izlazi kroz središnji otvor u klipu. Klip brtvi uz cilindar; nema drugih tokova ni zračnog džepa.

Unutarnji promjer cilindra je $D=100\ \text{mm}$, promjer otvora $d=20\ \text{mm}$, stalni dotok $Q_{in}=1{,}00\ \text{L/s}$ i gustoća vode $\rho=998\ \text{kg/m}^3$. Srednja izlazna brzina vode u odnosu na klip održava se na $w=1{,}50\ \text{m/s}$ udesno. Početna duljina vodene komore je $\ell_0=0{,}20\ \text{m}$, a raspoloživi hod klipa $s=0{,}12\ \text{m}$. Model je jednodimenzijski, voda nestlačiva, a debljina klipa zanemariva za volumen komore.

Odaberi kontrolni volumen omeđen nepomičnim cilindrom i gibajućim klipom. Iz bilance mase odredi brzinu klipa $u$, apsolutnu izlaznu brzinu, vrijeme do kraja hoda i porast mase u komori. Objasni zašto se na izlazu koristi brzina relativna prema klipu. Ako klip zaustavimo uz isti dotok, kolika bi morala postati relativna izlazna brzina da se nestlačivi model i dalje može održati? Ne računaju se sile potrebne za gibanje ili zaustavljanje.

:::: {.content-visible .mf1-hint-online when-format="html"}
::: {.callout-note collapse="true" data-hint-key="true"}
### Naputak
Promjenjivi volumen komore je $V=A_p\ell(t)$, gdje je $A_p=\pi D^2/4$. Kroz izlaznu plohu vezanu uz klip prolazi $Q_{out,rel}=A_o w$, uz $A_o=\pi d^2/4$. Zatvori akumulaciju mase u komori; zatim poveži apsolutnu i relativnu brzinu. Za zaustavljeni klip akumulacija mora nestati.
:::
::::
:::: {.content-visible .mf1-answer-online when-format="html"}
::: {.callout-tip collapse="true" data-answer-key="true"}
### Kontrolni rezultat

$Q_{out,rel}=0{,}4712\ \text{L/s}$; $u=0{,}06732\ \text{m/s}$ udesno; $v_{out}=1{,}5673\ \text{m/s}$. Vrijeme hoda $t=1{,}7824\ \text{s}$; porast mase $\Delta m=0{,}9406\ \text{kg}$. Za $u=0$ nužno je $w=3{,}1831\ \text{m/s}$; isti dotok i prvotna vrijednost $w$ ne mogu se zadržati bez promjene modela.
:::
::::

[Razina: T3]{.mf1-task-level}

### Z6. Bilanca spremnika s dvama fluidima {#task-u08-mijesajuci-spremnik-tlocrtne-povrsine-prima-vodu-gustoce .unnumbered .unlisted}

U spremniku za pripremu slane otopine dva dotoka ulaze u homogenu mješavinu. Izlazni je protok manji od ukupnog dotoka pa razina raste. Treba provjeriti koliko se tekućine zadrži u spremniku i dopušta li raspoloživi slobodni bok šest minuta rada uz zadane granice mjerenja.

Miješajući spremnik tlocrtne površine $A_T = 4{,}8\ \text{m}^2$ prima vodu gustoće $\rho_A=1000\ \text{kg/m}^3$ protokom $Q_A = 0{,}011\ \text{m}^3/\text{s}$ i slanu otopinu gustoće $\rho_B = 1080\ \text{kg/m}^3$ protokom $Q_B = 0{,}004\ \text{m}^3/\text{s}$. Homogena mješavina izlazi kroz cijev promjera $D = 80\ \text{mm}$ srednjom brzinom $v_3 = 1{,}6\ \text{m/s}$.

Pretpostavi aditivnost volumena, savršeno miješanje i da je spremnik na početku već napunjen mješavinom istog sastava kao spojeni dotoci; gustoća sadržaja i izlaza zato tijekom promatranih $6\ \text{min}$ ostaje jednaka omjeru ukupnoga ulaznog masenog i volumnog protoka.

Odredi izlazni volumenski protok, gustoću mješavine, brzinu porasta razine i masu akumuliranu u spremniku tijekom $6\ \text{min}$.

Za intervalnu procjenu protoci su stalni unutar svake promatrane kombinacije, a navedene granice zajamčeni su intervali, ne standardne nesigurnosti. Mjerila ulaznih protoka imaju granice $\pm2\ \%$ za $Q_A$ i $\pm3\ \%$ za $Q_B$, a izlazna brzina $v_3$ granicu $\pm0{,}08\ \text{m/s}$. Početni slobodni bok iznosi $0{,}560\ \text{m}$.

Konzervativno procijeni najveći porast razine, provjeri ostaje li šestominutni rad unutar geometrijskog kriterija slobodnog boka i odredi najdulje trajanje prije idealiziranog prelijevanja bez regulatora razine. Nakon dosezanja ruba prelijevanje je dodatni izlaz: linearni porast razine više ne vrijedi.

:::: {.content-visible .mf1-hint-online when-format="html"}
::: {.callout-note collapse="true" data-hint-key="true"}
### Naputak
Najprije izračunaj $Q_3 = A_3 v_3$, zatim gustoću mješavine iz masene bilance ulaza, a član akumulacije zatvori preko $Q_A + Q_B - Q_3 = A_T\,dh/dt$. Za najveći porast razine uzmi oba ulazna protoka na gornjoj, a izlaznu brzinu na donjoj granici. Najdulje trajanje slijedi iz $t_{max}=h_{slob}/(dh/dt)_{max}$.
:::
::::
:::: {.content-visible .mf1-answer-online when-format="html"}
::: {.callout-tip collapse="true" data-answer-key="true"}
### Kontrolni rezultat

$Q_3=8{,}042\ \text{L/s}$; $\rho_{mix}=1021{,}3\ \text{kg/m}^3$; $dh/dt=1{,}450\ \text{mm/s}$; $\Delta m\approx2558\ \text{kg}$ za 6 min nominalno. Najveći rast prije ruba je $1{,}604\ \text{mm/s}$, a vrijeme do ruba $349{,}0\ \text{s}$. Šest minuta ne zadovoljava kriterij. Ekstrapoliranih $0{,}5774\ \text{m}>0{,}560\ \text{m}$ pokazuje manjak boka $17{,}4\ \text{mm}$; nakon ruba voda se prelijeva.
:::
::::

[Razina: T4]{.mf1-task-level}

:::::

![Skice uz zadatke za vježbu — cijevi, mješalice i razdjelnici protoka.](../assets/print/u08_vjezbe_skice.svg){#fig-u08-vjezbe fig-align="center" fig-alt="Skice uz zadatke za vježbu — cijevi, mješalice i razdjelnici protoka."}

::: {.mf1-numerika}
<p class="mf1-box-label">Numerički most</p>

**Veza s numeričkim proračunom.** U metodi konačnih volumena kontrolni volumen koji se ovdje rabi za jedan spremnik postaje ćelija mreže. Diskretizirani tokovi kroz plohe moraju zatvoriti lokalnu i globalnu bilancu mase; druge numeričke metode istu fizikalnu bilancu mogu diskretizirati drukčije.

**Postupak numeričkog proračuna.** Diskretizirani kontinuitet spreže tlak i brzinu. Neravnoteža masenih protoka zato se prati zajedno s rezidualima i odabranim izlaznim veličinama; prihvatljiv rezultat mora pokazati očuvanje razmjerno mjerilu protoka i svrsi računa.

**Tipičan scenarij.** Protok se integrira na svim otvorenim granicama i uspoređuje s akumulacijom u domeni. Ne postoji univerzalna prihvatna granica od $1\,\%$: tolerancija ovisi o zatvorenosti bilance, diskretizaciji, vremenskoj statistici i potrebnoj nesigurnosti izlaza. Provjera jednadžbi i numeričke konvergencije prethodi validaciji prema podatcima [@nasa-cfd-vv; @asme-vv20-2009].

> *Nije gradivo MF1. Bilanca ručno odabranoga kontrolnog volumena primjenjuje se i na pojedine ćelije velike računske mreže.*
:::

::: {.mf1-zavrsni-okvir}
<p class="mf1-box-label">Za ponijeti iz poglavlja</p>

**Sažeta provjera prije računa**

- Treba nacrtati granicu kontrolnog volumena.
- Treba jasno odrediti što ulazi, što izlazi i postoji li akumulacija.
- Treba provjeriti koristi li se maseni protok kad je gustoća bitna, a volumenski samo kad je to opravdano.
- Ako se spremnik puni ili prazni, potrebno je zadržati član akumulacije.
- Treba provjeriti nije li zadatak višegranski prije nego što se napiše $A_1 v_1 = A_2 v_2$.

**Najčešća pogreška**

Česta je pogreška izbor neodgovarajućeg modela. Bilanca se pogrešno postavlja kada se preskoči izbor kontrolnog volumena i poseban slučaj jedne cijevi primijeni na spremnik, komoru za miješanje ili višegranski sustav.

**Nakon ovoga poglavlja mora biti moguće**

1. nacrtati kontrolni volumen prije bilo koje jednadžbe.
2. odabrati ispravan oblik bilance mase.
3. razlikovati suženje jedne cijevi od višegranskog ili nestacionarnog problema.

**U tehnici to znači**

Mješalica, ventilacijska komora, razdjelnik rashladne vode ili spremnik koji se puni ne mogu se analizirati promatranjem samo jedne cijevi. Tek kad se jasno odredi što ulazi, što izlazi i što se akumulira, model daje fizikalno smislen protok i vrijeme punjenja ili pražnjenja.

**Granica modela**

Pojednostavljeni zapis $A_1 v_1 = A_2 v_2$ vrijedi samo za vrlo poseban slučaj jedne ulazne i jedne izlazne grane nestlačivoga fluida. Čim sustav ima više grana, stlačivost ili akumulaciju, treba se vratiti punoj bilanci mase.

<span class="mf1-ch-ref"><span class="mf1-ch-code">pog. 7</span><span class="mf1-ch-title">Kinematika, kontrolni volumen i kontinuitet</span></span> treba ostaviti jednu pouzdanu radnu naviku: prije svake jednadžbe prvo se crta kontrolni volumen, a tek zatim se piše bilanca mase.
:::
