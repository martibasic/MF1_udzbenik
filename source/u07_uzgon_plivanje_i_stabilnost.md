![Pregled poglavlja: Uzgon, plivanje i stabilnost](../assets/print/u07_fig_uvod_pregled.svg){#fig-uvod-u07 fig-align="center" fig-alt="Pregled poglavlja: Uzgon, plivanje i stabilnost"}

## Uzgon kao spoj istisnine, težine i geometrije urona

Arhimedov zakon sam po sebi nije dovoljan za čitanje plivajućeg tijela.

Zato se već na početku razdvajaju tri stvari: ukupna težina, istisnuti volumen i momentni raspored tih sila.

::: {.mf1-application}
<p class="mf1-box-label">Inženjerski kontekst</p>

U brodogradnji, lučnim pontonima i plutajućim radnim platformama nije dovoljno znati samo koliko je vode istisnuto; jednako je važno gdje su težište i centar uzgona te kakav moment nastaje kad se teret pomakne. Zato ovo poglavlje izravno ulazi u stabilnost plovila, raspored opreme na pontonu, sigurnost plutajuće dizalice i svaku tehničku situaciju u kojoj mali bočni pomak tereta može otvoriti veliki nagib.
:::

::: {.mf1-priprema}
<p class="mf1-box-label">Prije čitanja poglavlja</p>

**Predznanje koje se pretpostavlja:**

- hidrostatička raspodjela tlaka iz poglavlja <span class="mf1-ch-ref"><span class="mf1-ch-code">pog. 3</span><span class="mf1-ch-title">Hidrostatička raspodjela tlaka i manometrija</span></span>;
- sile na plohe iz <span class="mf1-ch-ref"><span class="mf1-ch-code">pog. 5</span><span class="mf1-ch-title">Hidrostatske sile na plohe</span></span>;
- osnovni pojmovi statike krutog tijela: ravnoteža sila, ravnoteža momenata, položaj težišta;
- integralni račun više varijabli (težište volumena).

**Ishodi učenja:**

- primijeniti Arhimedov zakon na potpuno i djelomično uronjeno tijelo;
- razlikovati uvjet plovnosti od uvjeta stabilnosti plivajućeg tijela;
- izračunati gaz pravokutnog ili nepravilno oblikovanog plivajućeg tijela;
- procijeniti početnu stabilnost preko metacentarske visine i prepoznati granične slučajeve.

**Procijenjeno vrijeme rada uz udžbenik:** 10 sati.
:::

## Fizikalni uvod i matematički izvod

Za tijelo koje miruje u fluidu vrijedi da je sila uzgona jednaka težini istisnutog fluida:

$$F_U = \rho g V$$ {#eq-uzgon-stabilitet-fizikalni-uvod-i-matematicki-izvod-01}

Za plivajuće tijelo u ravnoteži ta sila mora biti jednaka ukupnoj težini tijela i svih tereta na njemu. To je tek prvi korak. Drugi korak je geometrija: gdje djeluje težina, gdje djeluje uzgon i kakav moment nastaje ako je teret bočno pomaknut. Matematika zato mora odvojiti ukupni volumen istisnine od rasporeda sile i momenata, inače plivanje i nagib ostaju pomiješani u istoj brojci.

Kod prizmatskih tijela s ravnim dnom vrlo se često može odvojiti srednja uronjenost od nagiba:

- srednja uronjenost dolazi iz ukupne težine
- razlika urona po širini dolazi iz momentne ravnoteze

Ta razdvojenost je jezgra gotovo svih prvih zadataka plivanja i stabilnosti.

## Matematički izvod

Najjednostavniji put prema Arhimedovu zakonu polazi od potpuno uronjenoga prizmatičnog tijela vodoravne površine $A$. Na gornju plohu na dubini $h_1$ djeluje sila

$$
F_1 = p_1A = (p_0 + \rho gh_1)A
$$ {#eq-uzgon-stabilitet-matematicki-izvod-01}

prema dolje, a na donju plohu na dubini $h_2$ sila

$$
F_2 = p_2A = (p_0 + \rho gh_2)A
$$ {#eq-uzgon-stabilitet-matematicki-izvod-02}

prema gore. Neto vertikalna hidrostatska sila iznosi zato

$$
F_U = F_2 - F_1 = \rho g(h_2-h_1)A.
$$ {#eq-uzgon-stabilitet-matematicki-izvod-03}

Budući da je $(h_2-h_1)A = V_{ist}$, odnosno istisnuti volumen fluida, slijedi opći zapis uzgona

$$
F_U = \rho gV_{ist}.
$$ {#eq-uzgon-stabilitet-matematicki-izvod-04}

::: {.mf1-fizikalno-znacenje}
<p class="mf1-box-label">Fizikalno značenje</p>
U jednolikom gravitacijskom polju uzgon ovisi o istisnutom volumenu i gustoći fluida, a ne izravno o materijalu tijela. Dva potpuno uronjena tijela jednakoga vanjskog volumena imaju jednak uzgon; njihove se težine mogu razlikovati, pa jedno može tonuti, a drugo se dizati. Jedan kilogram čelika i jedan kilogram pluta nemaju jednak volumen, pa nisu primjer jednakoga uzgona. Uzgon je suprotan gravitaciji i prolazi kroz težište istisnutoga volumena, a ne nužno kroz težište tijela.
:::

::: {.callout-note collapse="true" icon="false"}
## Numerički trag

U jednoj čestoj numeričkoj metodi za dvije faze, VOF-u (*Volume of Fluid*), polje $\alpha\in[0,1]$ predstavlja udio faze u ćeliji. Uz dosljedno polje gustoće i gravitacijski član model može reproducirati hidrostatski uzgon, dok gibanje plutajućega tijela zahtijeva dodatnu spregu sila i momenata s jednadžbama gibanja tijela. To treba provjeriti na mirnom plutanju prije valova ili složenoga toka.
:::

::: {.mf1-interaktivno}
<p class="mf1-box-label">Interaktivni prikaz — Gaz plivajućeg tijela</p>

Interaktivni prikaz omogućuje mijenjanje mase tijela i gustoće fluida uz neposredno praćenje ravnotežnog gaza i preostale visine iznad razine vode. Pri prekoračenju granice plovnosti prikaz signalizira da tijelo tone.

<div class="mf1-interaktivno-akcija">
<a class="mf1-interaktivno-veza" href="https://martibasic.github.io/MF1_udzbenik/jlite/lab/index.html?path=u07_gaz_plivajuceg_tijela.ipynb">Pokreni u pregledniku</a>
<a class="mf1-interaktivno-veza" href="https://colab.research.google.com/github/martibasic/MF1_udzbenik/blob/main/notebooks/u07_gaz_plivajuceg_tijela.ipynb" target="_blank" rel="noopener">Pričuvno: otvori u Colabu</a>
<img class="mf1-interaktivno-qr" src="../assets/qr/u07_gaz_plivajuceg_tijela.svg" alt="QR kod za interaktivni prikaz gaza plivajućeg tijela"/>
</div>

<div class="mf1-interaktivno-pitanja">
**Pitanja za samostalno istraživanje:** (a) Kako se gaz mijenja kada isti blok prelazi iz slatke u slanu vodu? (b) Pri kojoj masi tijelo upravo počinje tonuti? (c) Što bi se dogodilo s gazom istog tijela u ulju gustoće $800$ kg/m³, a što u glicerinu gustoće $1260$ kg/m³?
</div>
:::

Isti rezultat vrijedi i za proizvoljan oblik tijela: neto hidrostatska sila jednaka je težini fluida koji bi ispunio istisnuti volumen. Pravac djelovanja te sile prolazi kroz centar uzgona, tj. kroz težište istisnutoga volumena.

Iz toga odmah slijedi i prvo pravilo stabilnosti. Kod potpuno uronjenog tijela stabilan je položaj onaj u kojem je težište tijela $G$ ispod centra uzgona $B$; ako se te dvije točke poklope, ravnoteža je neutralna, a ako je $G$ iznad $B$, mali poremećaj daje prevrtni moment. Kod plivajućeg tijela slika je drukčija jer se pri malom nagibu oblik istisnutoga volumena mijenja, pa se i centar uzgona pomiče. Tada se uvodi metacentar $M$, a znak metacentarske visine $GM$ odlučuje o početnoj stabilnosti: $GM > 0$ znači povratni moment, $GM = 0$ neutralnu ravnotežu, a $GM < 0$ nestabilan položaj.

Za plivajuće tijelo vertikalna ravnoteža tada daje

$$
\rho gV_{ist} = G = mg
$$ {#eq-uzgon-stabilitet-interaktivni-prikaz-gaz-plivajuceg-tijela-01}

odnosno

$$
V_{ist} = \frac{m}{\rho}.
$$ {#eq-uzgon-stabilitet-interaktivni-prikaz-gaz-plivajuceg-tijela-02}

::: {.mf1-fizikalno-znacenje}
<p class="mf1-box-label">Fizikalno značenje</p>
Ova jednadžba kaže da plivajuće tijelo potapa se točno toliko da istisne svoju vlastitu masu fluida. Ako se teret doda, tijelo se potapa dublje; ako se teret ukloni, izroni. Volumen istisnine $V_{ist}$ nije fizička veličina tijela — on ovisi o gustoći fluida: isti brod u slanoj vodi (gustoća ~1025 kg/m³) istisne manji volumen nego u slatkoj vodi (~998 kg/m³), pa u slanoj vodi plovi nešto više.
:::

::: {.callout-note}
## Razrada koraka
Korak: od tlakova na gornju i donju plohu → $F_U = \rho g V_{ist}$

Na gornjoj plohi prizma na dubini $h_1$: $F_1 = (p_0 + \rho g h_1)A$ prema dolje.
Na donjoj plohi na dubini $h_2$: $F_2 = (p_0 + \rho g h_2)A$ prema gore.
Neto sila:
$$
F_U = F_2 - F_1 = \rho g(h_2 - h_1)A.
$$ {#eq-uzgon-stabilitet-razrada-koraka-01}
Budući da je $(h_2 - h_1)A$ upravo volumen istisnine $V_{ist}$:
$$
F_U = \rho g V_{ist}.
$$ {#eq-uzgon-stabilitet-razrada-koraka-02}
Jednolikni tlak $p_0$ potpuno se poniješta između gornje i donje plohe — zato uzgon ne ovisi o atmosferskom tlaku ni o apsolutnom tlaku u fluidu, nego samo o razlici dubina gornje i donje plohe.
:::

To je tek prvi dio fizikalne slike. Član $V_{ist}$ određuje koliko fluida mora biti istisnuto da bi se tijelo održalo na površini, ali ne određuje još i njegov nagib. Ako težište ukupne težine ne leži na istoj okomici kao centar uzgona, pojavljuje se moment koji tijelo zakreće. Zato za plivanje nisu dovoljne samo sile; mora biti zadovoljena i ravnoteža momenata.

Za pravokutnu platformu s linearnom promjenom urona po širini srednja uronjenost određena je vertikalnom ravnotežom, dok raspodjela urona po rubovima proizlazi iz momentne ravnoteže oko uzdužne osi. Upravo se tu vidi cjelovito značenje poglavlja: uzgon nije samo jedna brojka, nego rezultat istisnine, položaja centra uzgona i njihove geometrijske veze s ukupnom težinom sustava.

::: {.mf1-izvod}
<p class="mf1-box-label">Matematički izvod — Bočni pomak centra uzgona pri linearnoj promjeni urona</p>

Promatra se pravokutni ponton duljine $L$ i širine $B$ koji u nagnutom (ili nesimetrično opterećenom) položaju ima različite urone na lijevoj i desnoj strani: $h_L$ uz lijevu i $h_D$ uz desnu stijenku, uz srednji uron $h_m = (h_L + h_D)/2$.

Poprečni presjek istisnutoga volumena je trapez s okomicama duljina $h_L$ i $h_D$ na razmaku $B$. Taj se trapez razlaže na pravokutnik visine $h_D$ i trokut katetа $(h_L - h_D)$ i $B$ smješten uz lijevu stijenku. Pripadne površine i položaji težišta u poprečnom presjeku (mjereno od lijevog ruba) iznose

$$
A_1 = h_D B, \qquad \bar{x}_1 = \frac{B}{2},
$$ {#eq-uzgon-stabilitet-matematicki-izvod-bocni-pomak-centra-uzgona-pri-01}

$$
A_2 = \frac{1}{2}(h_L - h_D) B, \qquad \bar{x}_2 = \frac{B}{3}.
$$ {#eq-uzgon-stabilitet-matematicki-izvod-bocni-pomak-centra-uzgona-pri-02}

Težište cijelog trapeza, mjereno od lijevog ruba, dobiva se prvim momentom

$$
\bar{x} = \frac{A_1 \bar{x}_1 + A_2 \bar{x}_2}{A_1 + A_2} = \frac{h_D B \cdot \tfrac{B}{2} + \tfrac{1}{2}(h_L - h_D)B \cdot \tfrac{B}{3}}{B h_m}
= \frac{B(h_L + 2h_D)}{6 h_m}.
$$ {#eq-uzgon-stabilitet-matematicki-izvod-bocni-pomak-centra-uzgona-pri-03}

Bočni pomak centra uzgona od centra pontona (od ravnine simetrije, mjereno prema strani s većim uronom) iznosi

$$
y_B = \frac{B}{2} - \bar{x} = \frac{B}{2} - \frac{B(h_L + 2h_D)}{6 h_m}
= \frac{B\,(h_L - h_D)}{12\, h_m}.
$$ {#eq-uzgon-stabilitet-matematicki-izvod-bocni-pomak-centra-uzgona-pri-04}

Provjera: pri simetričnom uronu $h_L = h_D = h_m$ dobiva se $y_B = 0$, što znači da centar uzgona ostaje u središnjoj okomici. Pri tipičnoj razlici urona $h_L - h_D = 0{,}05\ \text{m}$ na pontonu širine $B = 1{,}2\ \text{m}$ sa srednjim uronom $h_m = 0{,}2\ \text{m}$ pomak centra uzgona iznosi $y_B = 1{,}2 \cdot 0{,}05/(12 \cdot 0{,}2) = 0{,}025\ \text{m}$, dakle $2{,}5\ \text{cm}$.

Ta je veličina **geometrijski pomak centra uzgona u koordinatama tijela**, a nije sama po sebi krak stabilnosti $GZ$ ni razmak pravaca djelovanja uzgona i ukupne težine. Iz geometrije rubnih urona vrijedi

$$
\tan\theta=\frac{h_L-h_D}{B},
$$ {#eq-uzgon-stabilitet-matematicki-izvod-bocni-pomak-centra-uzgona-pri-05}

a za pravokutnu vodnu liniju

$$
BM=\frac{B^2}{12h_m},\qquad y_B=BM\tan\theta.
$$ {#eq-uzgon-stabilitet-matematicki-izvod-bocni-pomak-centra-uzgona-pri-06}

Položaj ukupnoga težišta ulazi zasebno preko $GM=KB+BM-KG$. Ako se težina komponente $w$ pomakne poprečno za $e$, dok je ukupna težina deplasmana $\Delta$, ravnoteža malih nagiba daje

$$
w e\cos\theta=\Delta\,GM\sin\theta
\quad\Longrightarrow\quad
\boxed{w e=\Delta\,GM\tan\theta}.
$$ {#eq-uzgon-stabilitet-matematicki-izvod-bocni-pomak-centra-uzgona-pri-07}

U zapisu s masama faktor $g$ poništi se: $m_k e=m\,GM\tan\theta$. Izjednačavanje $\Delta y_B=w e$ bilo bi dopušteno samo u posebnom slučaju $KG=KB$, odnosno $BG=0$, kada je $GM=BM$. Bez podatka o $KG$ rubni uroni zato ne određuju jednoznačno položaj pomaknutoga tereta.
:::

Pri vrlo malim kutovima nagiba uvodi se još jedna apstraktna, ali fizikalno duboka veličina — metacentar. Iz njega proizlazi kriterij stabilnosti, koji je vrlo jasno povezan s geometrijom vodne linije plivajućeg tijela.

::: {.mf1-izvod}
<p class="mf1-box-label">Matematički izvod — Metacentarski radijus $\overline{BM} = I_T / V_{displ}$</p>

Promatra se plivajuće tijelo nagnuto za mali kut $\theta$ oko uzdužne osi koja prolazi kroz njegovu vodnu liniju (presjek tijela s mirnom slobodnom površinom). Istisnuti volumen ostaje konstantan jer s jedne strane voda "ulazi" u tijelo, a s druge "izlazi" — masa tijela se nije promijenila.

Geometrijski to znači da se s jedne strane osi rotacije pojavljuje klin dodatne istisnine (točke na udaljenosti $y > 0$ uranjaju se za $y\theta$ dublje), a s druge strane jednak klin nestaje istisnine ($y < 0$, voda se povlači za $|y|\theta$). Pomak centra uzgona $B \to B'$ u horizontalnom smjeru izračunava se prvim momentom volumna preslagivanja:

$$
V_{displ}\cdot \overline{BB'} = \int_{A_{wl}} y \cdot (y\theta)\, dA = \theta \int_{A_{wl}} y^2\, dA = \theta\, I_T,
$$ {#eq-uzgon-stabilitet-matematicki-izvod-metacentarski-radijus-01}

gdje je $A_{wl}$ površina vodne linije, a

$$
I_T = \int_{A_{wl}} y^2\, dA
$$ {#eq-uzgon-stabilitet-matematicki-izvod-metacentarski-radijus-02}

drugi moment površine vodne linije oko osi rotacije. Otud slijedi pomak centra uzgona

$$
\overline{BB'} = \frac{I_T\, \theta}{V_{displ}}.
$$ {#eq-uzgon-stabilitet-matematicki-izvod-metacentarski-radijus-03}

Metacentar $M$ definiran je kao točka u kojoj se sjeku okomica kroz novi centar uzgona $B'$ i prvotna osa simetrije tijela. Za male kutove vrijedi geometrijski

$$
\overline{BB'} = \overline{BM} \cdot \theta,
$$ {#eq-uzgon-stabilitet-matematicki-izvod-metacentarski-radijus-04}

pa izjednačavanjem dvaju izraza nastaje središnja relacija stabilnosti

$$
\boxed{\overline{BM} = \frac{I_T}{V_{displ}}}.
$$ {#eq-uzgon-stabilitet-matematicki-izvod-metacentarski-radijus-05}

Za pravokutnu vodnu liniju širine $B$ i duljine $L$ vrijedi $I_T = L B^3/12$, pa je

$$
\overline{BM} = \frac{L B^3}{12\, V_{displ}}.
$$ {#eq-uzgon-stabilitet-matematicki-izvod-metacentarski-radijus-06}

Za pravokutne, geometrijski usporedive vodne linije pri **fiksnim** $L$ i $V_{displ}$ vrijedi $\overline{BM}\propto B^3$. Šira vodna linija tada snažno povećava metacentarski radijus. To samo po sebi nije potpuna tvrdnja o stabilnosti broda: konačni $GM$ ovisi i o visini težišta, obliku trupa, istisnini i stanju opterećenja.

Robustan geometrijski zapis metacentarske visine jest

$$
\overline{GM}=\overline{KM}-\overline{KG}
=\overline{KB}+\overline{BM}-\overline{KG}.
$$ {#eq-uzgon-stabilitet-matematicki-izvod-metacentarski-radijus-07}

Ako se $G$ nalazi iznad $B$, tada se isti odnos može pisati $GM=BM-BG$. Zapis s $KM-KG$ ostaje jednoznačan i kada je $G$ ispod $B$.

Predznak $\overline{GM}$ odlučuje o **početnoj** stabilnosti uspravnoga položaja. Pri $GM>0$ mali nagib stvara povratni moment, pri $GM=0$ linearni je član neutralan, a pri $GM<0$ uspravni je položaj početno nestabilan. Negativan početni $GM$ ne dokazuje sam po sebi konačno prevrtanje: tijelo može prijeći u drugi ravnotežni položaj, što se provjerava punom krivuljom $GZ$ i geometrijom otvora.
:::

::: {.mf1-izvod}
<p class="mf1-box-label">Matematički izvod — Krivulja stabilnosti $GZ(\theta)$ i finitni nagib</p>

Metacentarski radijus $\overline{BM}$ izveden je za **infinitezimalni nagib**. Ne postoji univerzalni kut do kojega je aproksimacija dovoljno točna: granica ovisi o geometriji vodne linije i traženoj točnosti. Za konačan nagib koristi se **krivulja statičke stabilnosti** $GZ(\theta)$.

Pri nagibu $\theta$ centar uzgona pomakne se u $B_\theta$ prema **stvarnoj geometriji uronjenoga dijela**, dok $G$ ostaje fiksiran u tijelu. Krak $GZ$ vodoravna je udaljenost od $G$ do okomice kroz $B_\theta$ i za svaki se konačni kut ponovno računa iz hidrostatske geometrije. Veza s početnom teorijom glasi

$$
GZ(0)=0,\qquad \left.\frac{dGZ}{d\theta}\right|_{\theta=0}=GM,
$$ {#eq-uzgon-stabilitet-matematicki-izvod-krivulja-stabilnosti-i-finitni-01}

pa je za dovoljno mali kut $GZ\approx GM\sin\theta\approx GM\theta$. Dodavanje neodređene korekcije $f(\theta)$ nije postupak proračuna pri velikom nagibu.

Povratni moment para težine i uzgona iznosi

$$
M_{povratni}(\theta) = \rho g V_{displ}\cdot GZ(\theta),
$$ {#eq-uzgon-stabilitet-matematicki-izvod-krivulja-stabilnosti-i-finitni-02}

a prvi kut nakon pozitivnoga područja pri kojem $GZ$ ponovno postane nula naziva se **kut iščezavajuće stabilnosti** $\theta_v$. Stvarno uporabljivo područje može završiti ranije, primjerice kutom naplavljivanja kroz nezaštićeni otvor.

Krivulja $GZ(\theta)$ za određeno stanje opterećenja ima sljedeća osnovna svojstva:

- pri $\theta = 0$ vrijedi $GZ = 0$ (uspravni položaj);
- nagib krivulje u ishodištu jednak je $\overline{GM}$ — poveznica s metacentarskom teorijom;
- položaj i iznos maksimuma ovise o geometriji, otvorima i stanju opterećenja;
- pri $\theta_v$ krivulja siječe nulu, ako naplavljivanje ili druga granica nije nastupila ranije.

**Integral ispod krivulje**

$$
A = \int_0^{\theta_v} GZ(\theta)\,d\theta
$$ {#eq-uzgon-stabilitet-matematicki-izvod-krivulja-stabilnosti-i-finitni-03}

ima dimenziju $\text{m rad}$ i predstavlja energiju **normiranu težinom deplasmana**. Stvarni kvazistatički rad povratnoga momenta između dvaju kutova jest

$$
W=\rho gV_{displ}\int_{\theta_1}^{\theta_2}GZ(\theta)\,d\theta.
$$ {#eq-uzgon-stabilitet-matematicki-izvod-krivulja-stabilnosti-i-finitni-04}

Za brodove na koje se primjenjuju opći kriteriji IMO-ova *2008 Intact Stability Codea* provjerava se skup uvjeta, među ostalim: površina najmanje $0{,}055\ \text{m rad}$ do $30^\circ$; najmanje $0{,}09\ \text{m rad}$ do $40^\circ$ ili kuta naplavljivanja ako je manji; najmanje $0{,}03\ \text{m rad}$ između $30^\circ$ i te gornje granice; $GZ\ge0{,}20\ \text{m}$ pri kutu od najmanje $30^\circ$; maksimum $GZ$ pri kutu ne manjem od $25^\circ$; te početni $GM_0\ge0{,}15\ \text{m}$ [@imo-is-code-2008]. Primjenjivost, dodatni kriteriji i iznimke ovise o vrsti broda i mjerodavnoj administraciji, pa dvije površine same ne dokazuju usklađenost.

Metacentarska teorija opisuje samo početni odziv oko uspravnoga položaja. Stabilnost pri konačnom nagibu, na valovima ili nakon oštećenja zahtijeva odgovarajuću krivulju $GZ$, otvore i kut naplavljivanja, dinamičke utjecaje te posebne neoštećene ili oštećene kriterije [@imo-damage-stability].
:::

## Riješeni primjeri

::: {#ex-u07-koliki-gaz-ima-radni-ponton-pri-simetricnom .mf1-we}
<p class="mf1-box-label">Riješeni primjer — Koliki gaz ima radni ponton pri simetričnom opterećenju&nbsp;<span class="mf1-level">T2</span></p>

**Kontekst:** Pravokutni radni ponton nosi simetrično postavljenu opremu na mirnoj vodi. Treba odrediti istisnuti volumen, srednji gaz i preostalu nosivost prije nego što razina vode dosegne gornji rub boka.

**Zadano**

- Duljina pravokutnog radnog pontona: $L = 2{,}40\ \text{m}$
- Širina pontona: $B = 1{,}20\ \text{m}$
- Ukupna visina boka: $H = 0{,}32\ \text{m}$
- Vlastita masa pontona: $m_p = 420\ \text{kg}$
- Simetrično postavljena oprema mase: $m_o = 180\ \text{kg}$
- Gustoća vode: $\rho = 998\ \text{kg/m}^3$

**Traženo**

1. istisnuti volumen vode u ravnoteznom položaju.
2. srednji gaz pontona $h$.
3. koliku dodatnu masu još može primiti prije nego što gornji rub dođe do razine vode.

![ponton i gaz pri simetričnom opterećenju](../assets/print/u07_val2_ponton_gaz.svg){#fig-u07-ponton-i-gaz-pri-simetricnom-opterecenju fig-alt="ponton i gaz pri simetričnom opterećenju"}

**Pretpostavke i model**

Kako je opterećenje postavljeno simetrično, ovdje nema bočnog nagiba ni momentne neravnoteze. Zadatak se zatvara samo vertikalnom ravnotezom: težina pontona i tereta mora biti jednaka uzgonu, odnosno težini istisnute vode.

**Rješenje**

Ukupna masa sustava iznosi

$$
m = m_p + m_o = 420 + 180 = 600\ \text{kg}.
$$ {#eq-uzgon-stabilitet-rijeseni-primjer-koliki-gaz-ima-radni-ponton-01}

Za plivanje u ravnotezi vrijedi $\rho g V = mg$, pa je istisnuti volumen

$$
V = \frac{m}{\rho} = \frac{600}{998} \approx 0{,}601\ \text{m}^3.
$$ {#eq-uzgon-stabilitet-rijeseni-primjer-koliki-gaz-ima-radni-ponton-02}

Za pravokutni ponton vrijedi $V = LBh$, odakle slijedi srednji gaz

$$
h = \frac{V}{LB} = \frac{0{,}601}{2{,}40 \cdot 1{,}20} \approx 0{,}209\ \text{m} \approx 20{,}9\ \text{cm}.
$$ {#eq-uzgon-stabilitet-rijeseni-primjer-koliki-gaz-ima-radni-ponton-03}

Granični slučaj prije zalijevanja palube dobiva se kad je uron jednak ukupnoj visini boka, tj. $h = H = 0{,}32\ \text{m}$. Tada je najveći mogući istisnuti volumen

$$
V_{max} = LBH = 2{,}40 \cdot 1{,}20 \cdot 0{,}32 \approx 0{,}922\ \text{m}^3,
$$ {#eq-uzgon-stabilitet-rijeseni-primjer-koliki-gaz-ima-radni-ponton-04}

pa odgovarajuća ukupna masa iznosi

$$
m_{max} = \rho V_{max} = 998 \cdot 0{,}922 \approx 920\ \text{kg}.
$$ {#eq-uzgon-stabilitet-rijeseni-primjer-koliki-gaz-ima-radni-ponton-05}

Zato je dodatna masa koju ponton još može primiti

$$
\Delta m = m_{max} - m = 920 - 600 = 320\ \text{kg} \approx 3{,}2 \cdot 10^2\ \text{kg}.
$$ {#eq-uzgon-stabilitet-rijeseni-primjer-koliki-gaz-ima-radni-ponton-06}

**Provjera i komentar**

1. Veća ukupna masa mora značiti veći istisnuti volumen i veći gaz.
2. Dobiveni gaz mora biti manji od ukupne visine boka dok ponton još ima slobodni bok.
3. U simetričnom slučaju nema razloga za razliku urona lijevo i desno.
:::

 Kad je ta osnovna vertikalna ravnoteza zatvorena, korisno je najprije odvojiti još jedan međukorak: što sami rubni uroni govore o srednjem gazu i o bočnom pomaku centra uzgona, još bez traženja položaja tereta.

 Kad je taj geometrijski međukorak zatvoren, tek tada ima smisla prijeći na složeniji slučaj u kojem se teret bočno pomiče i uz ravnotezu sila treba zatvoriti i ravnotezu momenata.

::: {#ex-u07-plutajuca-servisna-platforma-s-pomaknutim-kompresorom-t2 .mf1-we}
<p class="mf1-box-label">Riješeni primjer — Plutajuća servisna platforma s pomaknutim kompresorom&nbsp;<span class="mf1-level">T2</span></p>

**Kontekst:** Na plutajućoj servisnoj platformi prijenosni kompresor postavljen je izvan osi simetrije, što izaziva mjerljiv bočni nagib. Treba odrediti istisnuti volumen, položaj težišta kompresora i porast srednjeg gaza nakon njegova postavljanja.

**Zadano**

- Duljina pravokutne plutajuće servisne platforme: $L = 3{,}10\ \text{m}$
- Širina platforme: $B = 1{,}00\ \text{m}$
- Masa platforme: $m_p = 676\ \text{kg}$
- Gustoća vode: $\rho = 998\ \text{kg/m}^3$
- Masa prijenosnog kompresora: $m_k = 190\ \text{kg}$
- Visina težišta platforme iznad dna: $KG_p = 0{,}14\ \text{m}$
- Visina težišta kompresora iznad dna: $KG_k = 0{,}38\ \text{m}$
- Izmjereni uron lijevog ruba platforme nakon postavljanja kompresora: $h_L = 0{,}34\ \text{m}$
- Izmjereni uron desnog ruba: $h_D = 0{,}22\ \text{m}$
- Platforma je kruta, ravnog dna i okomitih bočnih stijenki

**Traženo**

1. Odredite ukupni istisnuti volumen vode u ravnoteznom položaju.
2. Odredite $KB$, $BM$, $KG$ i početni $GM$ sustava te udaljenost $e$ težišta kompresora od uzdužne osi simetrije platforme.
3. Odredite za koliko je srednja uronjenost platforme veća nego prije postavljanja kompresora.

![plutajuća platforma s pomaknutim kompresorom](../assets/print/u07_val1_platforma_kompresor.svg){#fig-u07-plutajuca-platforma-s-pomaknutim-kompresorom fig-alt="plutajuća platforma s pomaknutim kompresorom"}

**Pretpostavke i model**

Platforma se promatra kao kruto prizmatsko tijelo pravokutnog tlocrta i ravnog dna. Srednja uronjenost dobiva se iz aritmetičke sredine lijevog i desnog urona, a bočni pomak centra uzgona iz linearnog nagiba plivajućeg presjeka. Kut je dovoljno malen za početnu metacentarsku teoriju; položaj tereta zato se određuje iz $m_k e=(m_p+m_k)GM\tan\theta$, a ne iz samoga $y_B$.

**Rješenje**

Srednja uronjenost iznosi

$$
h_m = \frac{h_L + h_D}{2} = \frac{0{,}34 + 0{,}22}{2} = 0{,}28\ \text{m},
$$ {#eq-uzgon-stabilitet-rijeseni-primjer-plutajuca-servisna-platforma-s-01}

pa je istisnuti volumen

$$
V = L B h_m = 3{,}10 \cdot 1{,}00 \cdot 0{,}28 = 0{,}868\ \text{m}^3.
$$ {#eq-uzgon-stabilitet-rijeseni-primjer-plutajuca-servisna-platforma-s-02}

To odgovara istisnutoj masi vode od približno $998 \cdot 0{,}868 \approx 866\ \text{kg}$, što je u skladu s ukupnom masom platforme i kompresora.

Za pravokutnu platformu s linearnom promjenom urona po širini bočni pomak centra uzgona glasi

$$
y_B = \frac{B(h_L - h_D)}{12h_m} = \frac{1{,}00\,(0{,}34 - 0{,}22)}{12 \cdot 0{,}28} \approx 0{,}0357\ \text{m}.
$$ {#eq-uzgon-stabilitet-rijeseni-primjer-plutajuca-servisna-platforma-s-03}

Razlika rubnih urona daje $\tan\theta=(h_L-h_D)/B=0{,}12$, odnosno $\theta\approx6{,}84^\circ$. Za pravokutnu istisninu vrijedi

$$
KB=\frac{h_m}{2}=0{,}140\ \text{m},\qquad
BM=\frac{B^2}{12h_m}=0{,}2976\ \text{m}.
$$ {#eq-uzgon-stabilitet-rijeseni-primjer-plutajuca-servisna-platforma-s-04}

Ukupno težište nakon postavljanja kompresora nalazi se na visini

$$
KG=\frac{m_pKG_p+m_kKG_k}{m_p+m_k}
=\frac{676\cdot0{,}14+190\cdot0{,}38}{866}
\approx0{,}1927\ \text{m},
$$ {#eq-uzgon-stabilitet-rijeseni-primjer-plutajuca-servisna-platforma-s-05}

pa je početna metacentarska visina

$$
GM=KB+BM-KG\approx0{,}140+0{,}2976-0{,}1927
=0{,}2450\ \text{m}.
$$ {#eq-uzgon-stabilitet-rijeseni-primjer-plutajuca-servisna-platforma-s-06}

Momentna ravnoteža maloga nagiba $m_k e=(m_p+m_k)GM\tan\theta$ sada daje

$$
e=\frac{m_p+m_k}{m_k}\,GM\tan\theta
=\frac{866}{190}\cdot0{,}2450\cdot0{,}12
\approx0{,}134\ \text{m}.
$$ {#eq-uzgon-stabilitet-rijeseni-primjer-plutajuca-servisna-platforma-s-07}

Povećanje srednje uronjenosti nakon postavljanja kompresora uzrokuje samo njegova masa, pa je

$$
\Delta h_m = \frac{m_k}{\rho L B} = \frac{190}{998 \cdot 3{,}10 \cdot 1{,}00} \approx 0{,}0614\ \text{m} \approx 6{,}14\ \text{cm}.
$$ {#eq-uzgon-stabilitet-rijeseni-primjer-plutajuca-servisna-platforma-s-08}

**Provjera i komentar**

1. Dublje uronjena strana mora biti ona na koju je kompresor pomaknut, a dobiveni rezultat to potvrduje.
2. Geometrijska provjera daje $BM\tan\theta=0{,}0357\ \text{m}=y_B$, ali je krak početne stabilnosti određen s $GM$, ne s $BM$.
3. Pomak ukupnoga težišta iznosi $(m_k/(m_p+m_k))e\approx0{,}0294\ \text{m}$, jednako $GM\tan\theta$; time je momentna bilanca neovisno zatvorena.
4. Dobiveni pomak kompresora manji je od polovice širine platforme, pa je geometrijski moguć, a povećanje srednjeg gaza reda nekoliko centimetara razumno je za dodatnih $190\ \text{kg}$.
:::

Plutajuća platforma nije jedini tipičan ulaz u <span class="mf1-ch-ref"><span class="mf1-ch-code">pog. 6</span><span class="mf1-ch-title">Uzgon, plivanje i početni stabilitet</span></span>. Jednako je važno znati zatvoriti vertikalnu ravnotezu i za potpuno uronjeno tijelo koje presiječa granicu dvaju fluida, jer se tada ukupni uzgon čita kao zbroj dviju istisnina različitih gustoća.

::: {#ex-u07-plutajuca-servisna-platforma-na-granici-ulja-i .mf1-ch}
<p class="mf1-box-label">Cjeloviti zadatak — Plutajuća servisna platforma na granici ulja i vode&nbsp;<span class="mf1-level">T4</span></p>

**Kontekst:** Hermetička servisna platforma pluta na stratificiranom mediju u kojem sloj ulja leži iznad vode, a na njoj se nepoznato bočno postavlja ormar s instrumentacijom. Treba podijeliti istisninu po fluidima, naći bočni pomak centra uzgona i položaj ormara koji uravnotežuje izmjerene rubne urone.

**Zadano**

- Duljina hermetičke pravokutne servisne platforme: $L = 3{,}00\ \text{m}$
- Širina platforme: $B = 1{,}20\ \text{m}$
- Visina boka: $H = 0{,}34\ \text{m}$
- Vlastita masa platforme: $m_p = 648\ \text{kg}$
- Gustoća gornjeg sloja ulja: $\rho_o = 800\ \text{kg/m}^3$
- Debljina uljnog sloja: $\delta = 0{,}10\ \text{m}$
- Gustoća donjeg sloja vode: $\rho_w = 1000\ \text{kg/m}^3$
- Masa ormara instrumentacije na platformi: $m_k = 180\ \text{kg}$ na nepoznatoj udaljenosti $e$ od uzdužne osi simetrije
- Visina težišta platforme iznad dna: $KG_p=0{,}12\ \text{m}$
- Visina težišta ormara iznad dna: $KG_k=0{,}54\ \text{m}$
- Nagib je malen; dvofluidni se slučaj svodi na navedeni ekvivalentni hidrostatički model, ne na normativnu provjeru stabiliteta
- Izmjereni uroni rubova platforme (od slobodne površine ulja): $h_L = 0{,}30\ \text{m}$, $h_D = 0{,}20\ \text{m}$
- Platforma je kruta, bočne stijenke okomite, dno ravno, promjena urona po širini linearna

**Traženo**

1. srednji uron $h_m$ i ukupni istisnuti volumen $V$.
2. koliki se dio istisnine nalazi u ulju, a koliki u vodi.
3. bočni pomak rezultantnog centra uzgona $y_B$.
4. ekvivalentne $KB$, $BM$ i $GM$ za zadani dvofluidni model te udaljenost $e$ težišta ormara od osi simetrije platforme.
5. za koliko je srednja uronjenost veća nego prije postavljanja ormara.

![plutajuća platforma na granici ulja i vode](../assets/print/u07_ch1_platforma_ulje_voda_ormar.svg){#fig-u07-plutajuca-platforma-na-granici-ulja-i-vode fig-alt="plutajuća platforma na granici ulja i vode"}

**Pretpostavke i model**

Ovdje se platforma još uvijek čita kao prizmatsko tijelo, ali uzgon više ne dolazi iz jedne jedine gustoće. Gornji uljni sloj daje simetrični doprinos uzgonu, dok donji vodeni dio nosi i preostalu vertikalnu ravnotezu i bočni pomak centra uzgona pri nagibu. Zato se najprije mora zatvoriti podjela istisnine po fluidima, a tek zatim momentna ravnoteza s pomaknutim teretom.

**Rješenje**

Srednja uronjenost dobiva se iz sredine izmjerenih rubnih urona:

$$
h_m = \frac{h_L + h_D}{2} = \frac{0{,}30 + 0{,}20}{2} = 0{,}25\ \text{m}.
$$ {#eq-uzgon-stabilitet-cjeloviti-zadatak-plutajuca-servisna-platforma-n-01}

Ukupni istisnuti volumen zato je

$$
V = L B h_m = 3{,}00 \cdot 1{,}20 \cdot 0{,}25 = 0{,}900\ \text{m}^3.
$$ {#eq-uzgon-stabilitet-cjeloviti-zadatak-plutajuca-servisna-platforma-n-02}

Kako su oba ruba uronjena više od debljine uljnog sloja $\delta = 0{,}10\ \text{m}$, cijela platforma kroz puni tlocrt presiječa svih $\delta$ ulja. Zato je volumen istisnine u ulju

$$
V_o = L B \delta = 3{,}00 \cdot 1{,}20 \cdot 0{,}10 = 0{,}360\ \text{m}^3,
$$ {#eq-uzgon-stabilitet-cjeloviti-zadatak-plutajuca-servisna-platforma-n-03}

a volumen istisnine u vodi

$$
V_w = L B (h_m - \delta) = 3{,}00 \cdot 1{,}20 \cdot (0{,}25 - 0{,}10) = 0{,}540\ \text{m}^3.
$$ {#eq-uzgon-stabilitet-cjeloviti-zadatak-plutajuca-servisna-platforma-n-04}

Provjera vertikalne ravnoteze sada glasi

$$
\rho_o V_o + \rho_w V_w = 800 \cdot 0{,}360 + 1000 \cdot 0{,}540 = 288 + 540 = 828\ \text{kg},
$$ {#eq-uzgon-stabilitet-cjeloviti-zadatak-plutajuca-servisna-platforma-n-05}

što se točno slaže s ukupnom masom sustava

$$
m_p + m_k = 648 + 180 = 828\ \text{kg}.
$$ {#eq-uzgon-stabilitet-cjeloviti-zadatak-plutajuca-servisna-platforma-n-06}

Dakle, vertikalna ravnoteza je zatvorena.

Za bočni pomak centra uzgona bitan je samo vodeni dio ispod granice fluida, jer je uljni dio simetričan po širini i ne daje bočni moment. Vodene dubine lijevo i desno iznose

$$
h_{w,L} = h_L - \delta = 0{,}30 - 0{,}10 = 0{,}20\ \text{m}, \qquad h_{w,D} = h_D - \delta = 0{,}20 - 0{,}10 = 0{,}10\ \text{m},
$$ {#eq-uzgon-stabilitet-cjeloviti-zadatak-plutajuca-servisna-platforma-n-07}

pa je srednja vodena dubina

$$
h_{w,m} = h_m - \delta = 0{,}15\ \text{m}.
$$ {#eq-uzgon-stabilitet-cjeloviti-zadatak-plutajuca-servisna-platforma-n-08}

Centar uzgona vodenog dijela za linearni nagib pravokutnog presjeka nalazi se na udaljenosti

$$
y_{B,w} = \frac{B(h_{w,L} - h_{w,D})}{12 h_{w,m}} = \frac{1{,}20(0{,}20 - 0{,}10)}{12 \cdot 0{,}15} \approx 0{,}0667\ \text{m}
$$ {#eq-uzgon-stabilitet-cjeloviti-zadatak-plutajuca-servisna-platforma-n-09}

od osi simetrije platforme, prema dublje uronjenoj strani.

Kako je samo vodeni dio asimetričan, rezultantni bočni pomak ukupnog centra uzgona dobiva se težinjenjem po uzgonskim doprinosima:

$$
y_B = \frac{\rho_w V_w}{\rho_o V_o + \rho_w V_w} y_{B,w} = \frac{540}{828} \cdot 0{,}0667 \approx 0{,}0435\ \text{m} \approx 4{,}35\ \text{cm}.
$$ {#eq-uzgon-stabilitet-cjeloviti-zadatak-plutajuca-servisna-platforma-n-10}

Pomak $y_B$ nije krak stabilnosti, pa se ne smije pisati $(m_p+m_k)g y_B=m_kge$ bez poznavanja vertikalnoga položaja $G$. Neka je $K$ na dnu platforme. Vertikalni položaji centara uzgonskih doprinosa jesu $z_{B,o}=h_m-\delta/2=0{,}20\ \text{m}$ za uljni sloj i $z_{B,w}=(h_m-\delta)/2=0{,}075\ \text{m}$ za vodeni dio. Ekvivalentni $KB$ zato iznosi

$$
KB_{eq}=\frac{\rho_oV_oz_{B,o}+\rho_wV_wz_{B,w}}
{\rho_oV_o+\rho_wV_w}
=\frac{288\cdot0{,}20+540\cdot0{,}075}{828}
\approx0{,}1185\ \text{m}.
$$ {#eq-uzgon-stabilitet-cjeloviti-zadatak-plutajuca-servisna-platforma-n-11}

U zadanom modelu uljni pojas ostaje poprečno simetričan, a promjenu bočnoga uzgonskog momenta daje vodeni dio. Za $I_T=LB^3/12=0{,}432\ \text{m}^4$ slijedi

$$
BM_{eq}=\frac{\rho_w I_T}{\rho_oV_o+\rho_wV_w}
=\frac{1000\cdot0{,}432}{828}
\approx0{,}5217\ \text{m}.
$$ {#eq-uzgon-stabilitet-cjeloviti-zadatak-plutajuca-servisna-platforma-n-12}

Ovaj rezultat daje i neovisnu geometrijsku provjeru: $BM_{eq}\tan\theta=0{,}5217(0{,}10/1{,}20)=0{,}0435\ \text{m}=y_B$. Ukupni položaj težišta jest

$$
KG=\frac{m_pKG_p+m_kKG_k}{m_p+m_k}
=\frac{648\cdot0{,}12+180\cdot0{,}54}{828}
\approx0{,}2113\ \text{m},
$$ {#eq-uzgon-stabilitet-cjeloviti-zadatak-plutajuca-servisna-platforma-n-13}

pa je početna ekvivalentna metacentarska visina

$$
GM_{eq}=KB_{eq}+BM_{eq}-KG
\approx0{,}1185+0{,}5217-0{,}2113
=0{,}4289\ \text{m}.
$$ {#eq-uzgon-stabilitet-cjeloviti-zadatak-plutajuca-servisna-platforma-n-14}

Budući da je $\tan\theta=(h_L-h_D)/B=0{,}08333$, ispravna momentna ravnoteža maloga nagiba daje

$$
e=\frac{m_p+m_k}{m_k}\,GM_{eq}\tan\theta
=\frac{828}{180}\cdot0{,}4289\cdot0{,}08333
\approx0{,}164\ \text{m}=16{,}4\ \text{cm}.
$$ {#eq-uzgon-stabilitet-cjeloviti-zadatak-plutajuca-servisna-platforma-n-15}

Prije postavljanja ormara platforma je bila simetrično opterećena, pa je i tada bila u ravnotezi bez nagiba. Neka je tadašnji srednji uron $h_0$. Budući da je uljni sloj i dalje potpuno presijecao platformu, vrijedi

$$
\rho_o L B \delta + \rho_w L B (h_0 - \delta) = m_p,
$$ {#eq-uzgon-stabilitet-cjeloviti-zadatak-plutajuca-servisna-platforma-n-16}

odnosno $800 \cdot 3{,}00 \cdot 1{,}20 \cdot 0{,}10 + 1000 \cdot 3{,}00 \cdot 1{,}20 \cdot (h_0 - 0{,}10) = 648$, što daje $288 + 3600(h_0 - 0{,}10) = 648$, pa je

$$
h_0 = 0{,}20\ \text{m}.
$$ {#eq-uzgon-stabilitet-cjeloviti-zadatak-plutajuca-servisna-platforma-n-17}

Povećanje srednje uronjenosti nakon postavljanja ormara zato iznosi

$$
\Delta h_m = h_m - h_0 = 0{,}25 - 0{,}20 = 0{,}05\ \text{m} = 5{,}0\ \text{cm}.
$$ {#eq-uzgon-stabilitet-cjeloviti-zadatak-plutajuca-servisna-platforma-n-18}

**Provjera i komentar**

Ovaj cjeloviti zadatak zatvara tri jezgre <span class="mf1-ch-ref"><span class="mf1-ch-code">pog. 6</span><span class="mf1-ch-title">Uzgon, plivanje i početni stabilitet</span></span> u jednom zadatku: srednji uron platforme je $0{,}25\ \text{m}$, ukupna istisnina iznosi $0{,}900\ \text{m}^3$, od čega je $0{,}360\ \text{m}^3$ u ulju, a $0{,}540\ \text{m}^3$ u vodi. Rezultantni centar uzgona pomaknut je oko $4{,}35\ \text{cm}$ prema dubljoj strani, ali zbog $KG\ne KB_{eq}$ to nije krak momenta težine i uzgona. Ekvivalentni početni $GM$ iznosi oko $0{,}429\ \text{m}$, pa ormar mora biti postavljen oko $16{,}4\ \text{cm}$ od osi. Njegovo postavljanje povećalo je srednji uron za $5\ \text{cm}$.

1. Srednji uron mora biti između izmjerenih rubnih urona i manji od visine boka, što ovdje vrijedi.
2. Dublje uronjena strana mora biti ona na koju je pomaknut ormar, pa znak momenta mora biti fizikalno smislen.
3. Dobiveni pomak ormara mora biti manji od polovice širine platforme; ovdje je $e = 0{,}164\ \text{m} < B/2 = 0{,}60\ \text{m}$.
4. Zaključak vrijedi samo za početnu ravnotežu pojednostavljenoga dvofluidnog modela; nije normativna provjera stabiliteta platforme.
:::

::: {#ex-u07-izolirani-puni-bocni-tank-kao-dodana-masa .mf1-ch}
<p class="mf1-box-label">Cjeloviti zadatak — Izolirani puni bočni tank kao dodana masa: gaz, nagib i početna stabilnost&nbsp;<span class="mf1-level">T4</span></p>

**Kontekst:** Na pojednostavljenom pravokutnom trupu bočni se tank tijekom izvanrednoga događaja napunio morskom vodom, nakon čega je dotok zaustavljen i tank izoliran. Tank je potpuno pun, pa se voda u ovom nastavnom modelu može tretirati kao nepomična dodana masa bez slobodne površine. Treba procijeniti novi gaz, bočni nagib i početni $GM$.

**Zadano**

Pojednostavljeni pravokutni trup miruje u mirnoj morskoj vodi. Jedan lijevi bočni tank sada je potpuno pun, izoliran i nosi se zajedno s brodom. Zadatak je odrediti odgovor unutar **added-mass** modela. Rezultat se neće tumačiti kao provjera propisa ni kao dokaz preživljavanja oštećenja.

**Glavni podaci broda**

- Duljina: $L = 80\ \text{m}$, širina: $B = 15\ \text{m}$, visina trupa: $H = 8\ \text{m}$
- Ukupna masa broda s teretom (prije oštećenja): $m_b = 4000\ \text{t}$
- Visina težišta broda iznad kobilice: $K\bar G_b = 3{,}0\ \text{m}$
- Gustoća morske vode: $\rho_m = 1025\ \text{kg/m}^3$
- $g = 9{,}81\ \text{m/s}^2$

**Geometrija punoga izoliranog tanka**

Lijevi bočni tank u sredini trupa, napunjen pa izoliran:

- Duljina tanka: $L_t = 15\ \text{m}$
- Širina tanka u poprečnom presjeku: $B_t = 6{,}0\ \text{m}$ (uz lijevu bočnu stijenku trupa)
- Visina tanka od kobilice prema gore: $H_t = 3{,}0\ \text{m}$

Nakon punjenja otvor je zatvoren ili je dotok drukčije pouzdano izoliran. Tank ostaje potpuno pun, bez slobodne površine.

**Traženo**

1. Volumen i masa morske vode koja je ušla u tank.
2. Pomak težišta cijelog sustava (brod + voda u tanku): bočni pomak $e_G$ od osi simetrije i nova visina težišta $K\bar G'$.
3. Novi srednji gaz $T_1$ ako bi brod ostao u uspravnom položaju, te porast gaza $\Delta T = T_1 - T_0$.
4. Metacentarska visina $\overline{GM}$ i zaključak samo o početnoj stabilnosti idealiziranoga modela.
5. Ravnotežni bočni kut nagiba $\theta$ (uz pretpostavku malog kuta).
6. Geometrijska provjera spuštanja bočnoga ruba palube unutar istoga pravokutnog modela.

![Izolirani puni bočni tank u modelu dodane mase: trup $80\times15\times8$ m i tank $15\times6\times3$ m uz lijevu stijenku. Težište vode u tanku pomaknuto je 4,5 m od osi simetrije.](../assets/print/u07_ch2_poplavljen_tank.svg){#fig-u07-poplavljen-tank fig-align="center" fig-alt="Izolirani puni bočni tank u modelu dodane mase: trup $80\times15\times8$ m i tank $15\times6\times3$ m uz lijevu stijenku. Težište vode u tanku pomaknuto je 4,5 m od osi simetrije."}

**Pretpostavke i model**

Brod se modelira kao kruti pravokutni trup s konstantnom raspodjelom mase; težište početnoga broda $G_b$ nalazi se na osi simetrije i zadanoj visini. More miruje, a valovi se zanemaruju. Voda u potpuno punom i izoliranom tanku dodaje se masi broda s fiksnim težištem u centroidu tanka. Vanjska vodonepropusna ovojnica smatra se ponovno uspostavljenom, pa se uzgon i vodna linija računaju za cijeli pravokutni trup.

Bočni nagib pretpostavlja se dovoljno malim da se može koristiti $\tan\theta\approx e_G/\overline{GM}$. Drugi moment vodne linije računa se za pravokutni trup $L\times B$. Model ne obuhvaća otvorenu komunikaciju s morem, izgubljeni uzgon oštećenoga prostora, propusnost sadržaja, promijenjenu vodnu liniju, progresivno naplavljivanje ni dinamiku valova.

**Rješenje**

**1. Volumen i masa dodane vode.**

$$
V_w = L_t B_t H_t = 15 \cdot 6 \cdot 3 = 270\ \text{m}^3,
$$ {#eq-uzgon-stabilitet-cjeloviti-zadatak-izolirani-puni-bocni-tank-kao-01}

$$
m_w = \rho_m V_w = 1025 \cdot 270 \approx 277\,000\ \text{kg} \approx 277\ \text{t}.
$$ {#eq-uzgon-stabilitet-cjeloviti-zadatak-izolirani-puni-bocni-tank-kao-02}

**2. Pomak težišta sustava.**

Centroid vode u punom tanku nalazi se $B_t/2=3{,}0$ m od lijeve stijenke broda, odnosno $B/2-B_t/2=4{,}5$ m lijevo od osi simetrije. Po visini je na $H_t/2=1{,}5$ m iznad kobilice.

Bočni pomak težišta cijelog sustava (pondrirano masom):

$$
e_G = \frac{m_w \cdot e_t}{m_b + m_w} = \frac{277 \cdot 4{,}5}{4000 + 277} = \frac{1247}{4277} \approx 0{,}291\ \text{m}.
$$ {#eq-uzgon-stabilitet-cjeloviti-zadatak-izolirani-puni-bocni-tank-kao-03}

Nova visina težišta sustava iznad kobilice:

$$
K\bar G' = \frac{m_b \cdot K\bar G_b + m_w \cdot (H_t/2)}{m_b + m_w} = \frac{4000 \cdot 3{,}0 + 277 \cdot 1{,}5}{4277} \approx 2{,}90\ \text{m}.
$$ {#eq-uzgon-stabilitet-cjeloviti-zadatak-izolirani-puni-bocni-tank-kao-04}

**3. Novi gaz (uspravan položaj).** Brod plovi kad uzgon = ukupna težina, tj. istisnina $V_{displ} = (m_b + m_w)/\rho_m$. Za pravokutni trup $V_{displ} = L \cdot B \cdot T$, pa:

$$
T_1 = \frac{m_b + m_w}{\rho_m L B} = \frac{4277 \cdot 10^3}{1025 \cdot 80 \cdot 15} \approx 3{,}478\ \text{m}.
$$ {#eq-uzgon-stabilitet-cjeloviti-zadatak-izolirani-puni-bocni-tank-kao-05}

Originalni gaz (samo $m_b$): $T_0 = m_b / (\rho_m L B) = 4000\cdot 10^3 / 1{,}23 \cdot 10^6 \approx 3{,}252\ \text{m}$.

$$
\Delta T = T_1 - T_0 \approx 0{,}226\ \text{m}.
$$ {#eq-uzgon-stabilitet-cjeloviti-zadatak-izolirani-puni-bocni-tank-kao-06}

**4. Metacentarska visina.** Drugi moment površine vodne linije za pravokutni presjek:

$$
I_T = \frac{L B^3}{12} = \frac{80 \cdot 15^3}{12} = 22\,500\ \text{m}^4.
$$ {#eq-uzgon-stabilitet-cjeloviti-zadatak-izolirani-puni-bocni-tank-kao-07}

Volumen istisnine:

$$
V_{displ} = \frac{m_b + m_w}{\rho_m} = \frac{4277 \cdot 10^3}{1025} \approx 4172\ \text{m}^3.
$$ {#eq-uzgon-stabilitet-cjeloviti-zadatak-izolirani-puni-bocni-tank-kao-08}

Metacentarski radijus (razmak centra uzgona $B'$ od metacentra $M$):

$$
\overline{BM} = \frac{I_T}{V_{displ}} = \frac{22\,500}{4172} \approx 5{,}39\ \text{m}.
$$ {#eq-uzgon-stabilitet-cjeloviti-zadatak-izolirani-puni-bocni-tank-kao-09}

Visina centra uzgona iznad kobilice ($T_1/2$):

$$
K\bar B = T_1/2 \approx 1{,}74\ \text{m}.
$$ {#eq-uzgon-stabilitet-cjeloviti-zadatak-izolirani-puni-bocni-tank-kao-10}

Razmak težišta od centra uzgona:

$$
\overline{BG} = K\bar G' - K\bar B \approx 2{,}90 - 1{,}74 \approx 1{,}16\ \text{m}.
$$ {#eq-uzgon-stabilitet-cjeloviti-zadatak-izolirani-puni-bocni-tank-kao-11}

Metacentarska visina:

$$
\overline{GM} = \overline{BM} - \overline{BG} \approx 5{,}39 - 1{,}16 \approx 4{,}23\ \text{m}.
$$ {#eq-uzgon-stabilitet-cjeloviti-zadatak-izolirani-puni-bocni-tank-kao-12}

Kako je $\overline{GM}>0$, uspravni položaj ovoga idealiziranog added-mass modela ima povratni moment pri dovoljno malim nagibima.

**5. Ravnotežni kut nagiba.** Za male kutove vrijedi:

$$
\tan\theta = \frac{e_G}{\overline{GM}} = \frac{0{,}291}{4{,}23} \approx 0{,}0689 \quad \Rightarrow \quad \theta \approx 3{,}94^\circ.
$$ {#eq-uzgon-stabilitet-cjeloviti-zadatak-izolirani-puni-bocni-tank-kao-13}

**6. Provjera bočnog ruba palube.** Originalni nadboj (freeboard) pri uspravnom položaju s novim gazom:

$$
F_b = H - T_1 \approx 8 - 3{,}478 \approx 4{,}52\ \text{m}.
$$ {#eq-uzgon-stabilitet-cjeloviti-zadatak-izolirani-puni-bocni-tank-kao-14}

Spuštanje lijevog ruba palube zbog nagiba:

$$
\Delta z = (B/2) \sin\theta \approx 7{,}5 \cdot \sin 3{,}94^\circ \approx 7{,}5 \cdot 0{,}0687 \approx 0{,}515\ \text{m}.
$$ {#eq-uzgon-stabilitet-cjeloviti-zadatak-izolirani-puni-bocni-tank-kao-15}

Preostali nadboj na lijevom rubu palube:

$$
F_{b,L} = F_b - \Delta z \approx 4{,}52 - 0{,}52 \approx 4{,}00\ \text{m}.
$$ {#eq-uzgon-stabilitet-cjeloviti-zadatak-izolirani-puni-bocni-tank-kao-16}

Granični kut prije nego što paluba dotakne morsku razinu:

$$
\sin\theta_{lim} = \frac{F_b}{B/2} = \frac{4{,}52}{7{,}5} \approx 0{,}603, \qquad \theta_{lim} \approx 37{,}1^\circ.
$$ {#eq-uzgon-stabilitet-cjeloviti-zadatak-izolirani-puni-bocni-tank-kao-17}

Vrijednost $37{,}1^\circ$ samo je geometrijska ekstrapolacija krutoga pravokutnika koji se zakreće oko uspravnoga položaja. Pri tako velikom kutu mala-kutna metacentarska aproksimacija više nije dostatna, a stvarnu uronjenost ruba i kut naplavljivanja treba dobiti ponovnim određivanjem vodne linije, centra uzgona i stvarnih otvora za svaki kut.

**Provjera i komentar**

1. Unutar zadanoga modela dobiveni su $GM\approx4{,}2\ \text{m}$, ravnotežni nagib oko $4^\circ$ i približno $4\ \text{m}$ nadvoja na nižem rubu. To znači samo početnu ravnotežu idealiziranoga pravokutnog trupa; ne dokazuje preživljavanje oštećenja ni usklađenost s propisom.
2. Veliki $BM$ ovdje proizlazi iz široke pravokutne vodne linije pri zadanoj istisnini. Konačna stabilnost i sigurnost ovise i o $KG$, stvarnom obliku trupa, otvorima, valovima i stanju opterećenja.
3. Stvarni proračun oštećene stabilnosti može zahtijevati metodu izgubljenoga uzgona ili drugi odobreni postupak, propusnosti prostora, promijenjenu vodnu liniju, asimetrično i progresivno naplavljivanje, kutove naplavljivanja te probabilističke scenarije. Ti učinci nisu sadržani u ovome added-mass primjeru.
4. Ako tank nije pun, slobodna površina tekućine pri nagibu smanjuje efektivni $GM$. Stvarna ograničenja punjenja i upravljanja tankovima određuju dokumentacija broda i operativni postupci; iz ovog se primjera ne izvodi univerzalno pravilo rada.
5. Rezultat je zato koristan kao provjera bilance mase, težišta i početnoga momenta, ali ne kao regulatorna ili operativna odluka.
:::

::: {#ex-u07-uzgon-na-potonulo-pumpno-kuciste-pri-ispitivanju .mf1-we}
<p class="mf1-box-label">Riješeni primjer — Uzgon na potonulo pumpno kućište pri ispitivanju &nbsp;<span class="mf1-level">T2</span></p>

**Primjer za strojare**

**Kontekst:** Pumpa u podvodnom prihvatnom bazenu ima čelično kućište koje se ispravlja ronjenjem. Serviseri trebaju znati koliku tegežu (lančanu vezu prema dnu) trebaju koristiti da kućište ostane na dnu dok se montira priključak.

**Zadano**

- Volumen kućišta pumpe: $V = 0{,}045\ \text{m}^3$
- Masa kućišta: $m = 85\ \text{kg}$
- Gustoća morske vode: $\rho = 1025\ \text{kg/m}^3$

**Traženo**

1. Sila uzgona na kućište.
2. Neto sila i potrebna tegeba (sila držanja prema dnu).

![Potonulo pumpno kućište: V=0,045 m³, m=85 kg, F_U≈453 N, G≈834 N](../assets/print/u07_fig_pumpno_kuciste.svg){#fig-u07-pumpno-kuciste-uzgon fig-align="center" fig-alt="Potonulo pumpno kućište: V=0,045 m³, m=85 kg, F_U≈453 N, G≈834 N"}

**Rješenje**

$$
F_U = \rho g V = 1025 \cdot 9{,}81 \cdot 0{,}045 = 452{,}5\ \text{N} \approx 0{,}453\ \text{kN}
$$ {#eq-uzgon-stabilitet-rijeseni-primjer-uzgon-na-potonulo-pumpno-kucist-01}

Težina kućišta:
$$
G = mg = 85 \cdot 9{,}81 = 833{,}9\ \text{N} \approx 0{,}834\ \text{kN}
$$ {#eq-uzgon-stabilitet-rijeseni-primjer-uzgon-na-potonulo-pumpno-kucist-02}

Neto sila (prema dolje, kućište tone samo):
$$
F_{neto} = G - F_U = 833{,}9 - 452{,}5 = 381{,}4\ \text{N}
$$ {#eq-uzgon-stabilitet-rijeseni-primjer-uzgon-na-potonulo-pumpno-kucist-03}

Kućište se samo potapa — nema potrebe za tegebom; ali ronioci trebaju silu od ~381 N za podizanje kućišta na površinu.

**Provjera i komentar**

Za zadanu masu i vanjski istisnuti volumen prosječna gustoća kućišta iznosi oko $1889\ \text{kg/m}^3$, pa je veća od gustoće morske vode i kućište tone. Materijal stijenke sam nije dovoljan za taj zaključak jer šuplje hermetičko tijelo može imati mnogo manju prosječnu gustoću. Uzgon smanjuje potrebnu statičku silu podizanja s oko $834$ na $381\ \text{N}$; u slojevitom fluidu treba rabiti lokalnu raspodjelu gustoće po istisnutom volumenu.

:::

::: {#ex-u07-plutajuci-vjetroagregat-tipa-cilindricne-plovne-osnove-t3 .mf1-we}
<p class="mf1-box-label">Riješeni primjer — Plutajući vjetroagregat tipa cilindrične plovne osnove &nbsp;<span class="mf1-level">T3</span></p>

**Kontekst:** Pojednostavljena cilindrična plovna osnova tipa *spar* nosi vjetroagregat. Ovdje se računa samo vertikalna ravnoteža i promjena gaza; stabilnost, gibanje na valovima, sidrenje i položaj rotora ostaju izvan modela.

**Zadano**

- Ukupna masa konstrukcije s turbinom: $m_{uk} = 1\,100\ \text{t} = 1{,}10 \cdot 10^6\ \text{kg}$
- Promjer cilindra plovne osnove: $D = 9{,}0\ \text{m}$
- Ukupna duljina cilindra: $H = 95\ \text{m}$
- Gustoća morske vode: $\rho_{m} = 1\,025\ \text{kg/m}^3$
- Plovna osnova orijentirana vertikalno, turbina iznad razine mora

**Traženo**

1. Površina poprečnog presjeka plovne osnove;
2. Istisnuti volumen u ravnoteži;
3. Gaz (dubina urona) plovne osnove;
4. Visina nadvodnog dijela (rezerva slobodnog boka).

**Pretpostavke i model**

Promatra se vertikalna ravnoteža u mirnoj vodi, bez vjetra i valova. Promjer cilindra konstantan je po visini, a ukupna masa i vanjski volumen zadani su. Položaj težišta nije zadan, pa se iz ovoga računa ne izvodi metacentarska ni konačna stabilnost. Atmosferski tlak djeluje s obje strane plovne osnove, pa se njegov doprinos poništava.

**Rješenje**

Površina poprečnog presjeka iznosi

$$
A = \frac{\pi D^2}{4} = \frac{\pi \cdot 9{,}0^2}{4} \approx 63{,}62\ \text{m}^2.
$$ {#eq-uzgon-stabilitet-rijeseni-primjer-plutajuci-vjetroagregat-tipa-ci-01}

Iz Arhimedovog zakona istisnuti volumen u ravnoteži jednak je masi konstrukcije podijeljenoj s gustoćom mora:

$$
V_{ist} = \frac{m_{uk}}{\rho_{m}} = \frac{1{,}10 \cdot 10^6}{1\,025} \approx 1\,073{,}2\ \text{m}^3.
$$ {#eq-uzgon-stabilitet-rijeseni-primjer-plutajuci-vjetroagregat-tipa-ci-02}

Gaz plovne osnove (dubina urona cilindra) slijedi iz omjera istisnutog volumena i površine presjeka:

$$
d = \frac{V_{ist}}{A} = \frac{1\,073{,}2}{63{,}62} \approx 16{,}87\ \text{m}.
$$ {#eq-uzgon-stabilitet-rijeseni-primjer-plutajuci-vjetroagregat-tipa-ci-03}

Visina nadvodnog dijela iznosi

$$
H - d = 95 - 16{,}87 \approx 78{,}13\ \text{m}.
$$ {#eq-uzgon-stabilitet-rijeseni-primjer-plutajuci-vjetroagregat-tipa-ci-04}

Promjena mase za $\pm 5\,\%$ (prirast od taloga, ledenice ili korozije; gubitak od ispražnjenog balasta) mijenja gaz na

$$
d_{+5\%} \approx \frac{1{,}155 \cdot 10^6}{1\,025 \cdot 63{,}62} \approx 17{,}71\ \text{m}, \qquad
d_{-5\%} \approx 16{,}02\ \text{m}.
$$ {#eq-uzgon-stabilitet-rijeseni-primjer-plutajuci-vjetroagregat-tipa-ci-05}

U idealiziranom cilindričnom modelu promjena gaza po iznosu je manja od $0{,}9\ \text{m}$. To ne dokazuje rezervu plovnosti, slobodni bok u valovima ni razmak lopatica od mora.

**Provjera i komentar**

Dane veličine daju gaz oko $17\ \text{m}$ i geometrijsku duljinu cilindra iznad mirne vodne linije oko $78\ \text{m}$. To nisu projektne vrijednosti visine glavine, slobodnog boka ili odziva na valove. Za stvarnu plovnu osnovu treba zasebno odrediti $KG$, $GM$ i krivulju $GZ$, hidrodinamički odziv, sidrenje, konstrukcijska opterećenja i sve mjerodavne radne slučajeve.
:::

::: {.mf1-samoprovjera}
<p class="mf1-box-label">Provjeri sebe</p>

Sljedeća pitanja služe za samostalnu provjeru razumijevanja prije prelaska na zadatke za vježbu.

1. Što govori Arhimedov zakon o ovisnosti sile uzgona o materijalu i obliku tijela?

::: {.callout-note collapse="true"}
### Odgovor
Sila uzgona ovisi isključivo o istisnutom volumenu fluida i njegovoj gustoći, a ne o materijalu, masi ni unutarnjoj građi uronjenog tijela. Tijela jednake vanjske geometrije, neovisno o tome jesu li čvrsta ili šuplja, imaju jednaku silu uzgona.
:::

2. Zašto plivajuće tijelo može biti u vertikalnoj ravnoteži, a istovremeno nestabilno na nagib?

::: {.callout-note collapse="true"}
### Odgovor
Vertikalna ravnoteža traži jednakost težine i sile uzgona, dok stabilnost traži da metacentar leži iznad težišta tijela. Tijelo može zadovoljiti prvi uvjet (pliva pravilno), ali pri malom nagibu može imati negativnu metacentarsku visinu pa moment nastaje koji ga prevrće.
:::

3. Kako se mijenja gaz istog broda pri prelasku iz slatke u slanu vodu?

::: {.callout-note collapse="true"}
### Odgovor
Gustoća slane vode veća je od slatke, pa je za istu masu broda potreban manji istisnuti volumen i brod u slanoj vodi plovi s manjim gazom. Dopuštena masa tereta ipak se ne određuje samo gustoćom trenutačne vode, nego linijama opterećenja, uvjetima plovidbe, čvrstoćom i stabilnošću; iz Arhimedova zakona samoga ne slijedi dopuštenje za ukrcaj dodatnoga tereta.
:::

4. Vrijedi li Arhimedov zakon i u uljnom ili plinskom fluidu, ili samo u vodi?

::: {.callout-note collapse="true"}
### Odgovor
Vrijedi u bilo kojem fluidu, uključujući plinove. U zraku sila uzgona je obično zanemariva zbog male gustoće zraka, ali za balone, dirižable i precizna mjerenja mase u vakuumu treba je uračunati. U uljnim sustavima Arhimedov zakon koristi se pri proračunu uzgona kliznih elemenata i u multifaznim separatorima.
:::
:::

## Zadaci za vježbu

::::: {.mf1-vjezbe-list}
1. [**T1**]{#task-u07-hermeticki-zatvoreno-tijelo-volumena-i-mase-potpuno} Hermetički zatvoreno tijelo volumena $V = 0{,}085\ \text{m}^3$ i mase $m = 62\ \text{kg}$ potpuno je uronjeno u vodu gustoće $\rho = 998\ \text{kg/m}^3$. Odredi silu uzgona i silu koju treba primijeniti da tijelo ostane potpuno uronjeno i u mirovanju.

   :::: {.content-visible .mf1-hint-online when-format="html"}
   ::: {.callout-note collapse="true" data-hint-key="true"}
   ### Naputak
   uzgon je $F_U = \rho gV$; potom usporedi $F_U$ i težinu $G = mg$ da dobiješ potrebnu dodatnu silu.
   :::
   ::::
   :::: {.content-visible .mf1-answer-online when-format="html"}
   ::: {.callout-tip collapse="true" data-answer-key="true"}
   ### Kontrolni rezultat

   $F_U \approx 832\ \text{N}$; kako je $F_U > G = 608\ \text{N}$, treba dodatna sila prema dolje $\approx 224\ \text{N}$.
   :::
   ::::
   **Skica:** da - potpuno uronjeni blok, volumen $V$, smjerovi $F_U$, $G$ i dodatne sile držanja.

2. [**T1**]{#task-u07-pravokutni-radni-ponton-duljine-sirine-i-visine} Pravokutni radni ponton duljine $L = 2{,}60\ \text{m}$, širine $B = 1{,}40\ \text{m}$ i visine boka $H = 0{,}38\ \text{m}$ ima vlastitu masu $m_p = 510\ \text{kg}$. Na njega se simetrično postavlja teret mase $m_t = 220\ \text{kg}$. Ponton pluta u vodi gustoće $\rho = 998\ \text{kg/m}^3$. Odredi istisnuti volumen, srednji gaz i preostalu dodatnu masu koju ponton može primiti prije nego što rub boka dođe do razine vode.

   :::: {.content-visible .mf1-hint-online when-format="html"}
   ::: {.callout-note collapse="true" data-hint-key="true"}
   ### Naputak
   iz vertikalne ravnoteže vrijedi $\rho gV_{ist} = (m_p + m_t)g$; srednji gaz slijedi iz $V_{ist} = LBh$.
   :::
   ::::
   :::: {.content-visible .mf1-answer-online when-format="html"}
   ::: {.callout-tip collapse="true" data-answer-key="true"}
   ### Kontrolni rezultat

   $V_{ist} \approx 0{,}73\ \text{m}^3$; srednji gaz $h \approx 0{,}20\ \text{m}$; dodatna masa do ruba $\approx 650\ \text{kg}$.
   :::
   ::::
   **Skica:** da - ponton pravokutnog presjeka, srednji gaz $h$ i slobodni bok $H-h$.

3. [**T2**]{#task-u07-plutajuca-servisna-platforma-duljine-i-sirine-ima} Plutajuća servisna platforma duljine $L = 2{,}20\ \text{m}$ i širine $B = 1{,}00\ \text{m}$ ima ukupnu masu s opremom $m = 560\ \text{kg}$ i ukupno težište na visini $KG=0{,}18\ \text{m}$ iznad dna. Kompresor mase $85\ \text{kg}$ pomakne se za $e = 0{,}24\ \text{m}$ udesno od središnje osi. Ako platforma pluta u vodi gustoće $998\ \text{kg/m}^3$ i ostaje u linearnom režimu malog nagiba, odredi srednji gaz, $KB$, $BM$, $GM$ te razliku urona rubova.

   :::: {.content-visible .mf1-hint-online when-format="html"}
   ::: {.callout-note collapse="true" data-hint-key="true"}
   ### Naputak
   srednji gaz dolazi iz ukupne težine. Zatim upotrijebi $KB=h_m/2$, $BM=B^2/(12h_m)$, $GM=KB+BM-KG$ i $m_k e=mGM\tan\theta$, uz $|h_L-h_D|=B\tan\theta$; nemoj izjednačiti geometrijski $y_B$ s krakom $GZ$.
   :::
   ::::
   :::: {.content-visible .mf1-answer-online when-format="html"}
   ::: {.callout-tip collapse="true" data-answer-key="true"}
   ### Kontrolni rezultat

   $h_m\approx0{,}255\ \text{m}$; $KB\approx0{,}128\ \text{m}$; $BM\approx0{,}327\ \text{m}$; $GM\approx0{,}274\ \text{m}$; $|h_L-h_D|\approx0{,}133\ \text{m}$, pri čemu je desni rub dublje uronjen.
   :::
   ::::
   **Skica:** da - platforma, pomaknuti kompresor, lijevi i desni uron te širina $B$.

4. [**T2**]{#task-u07-areometar-mase-s-cilindricnim-vratom-promjera-pluta} Areometar mase $m = 0{,}085\ \text{kg}$ s cilindričnim vratom promjera $d = 8\ \text{mm}$ pluta tako da mu je u vodi uronjena duljina $h_1 = 82\ \text{mm}$, a u nepoznatom ulju $h_2 = 95\ \text{mm}$. Odredi gustoću ulja i protumači zašto je uron u ulju veći nego u vodi.

   :::: {.content-visible .mf1-hint-online when-format="html"}
   ::: {.callout-note collapse="true" data-hint-key="true"}
   ### Naputak
   u oba fluida vrijedi $\rho gV_{ist} = mg$; razlika je samo u uronjenom volumenu vrata i tijela areometra.
   :::
   ::::
   :::: {.content-visible .mf1-answer-online when-format="html"}
   ::: {.callout-tip collapse="true" data-answer-key="true"}
   ### Kontrolni rezultat

   $\rho_{ulje} \approx 990\ \text{kg/m}^3$; uron je veći jer je ulje rjeđe pa je za istu težinu potreban veći istisnuti volumen.
   :::
   ::::
   **Skica:** da - areometar s cilindričnim vratom i dvije razine urona $h_1$, $h_2$.

5. [**T3**]{#task-u07-plutajuci-modul-istiskuje-volumen-vode-i-ima} Plutajući modul istiskuje volumen vode $V_{ist} = 0{,}62\ \text{m}^3$ i ima metacentarsku visinu $GM = 0{,}18\ \text{m}$. Ako se pri malom nagibu zakrene za $\varphi = 7^\circ$, odredi povratni moment stabilnosti i procijeni je li ravnoteža stabilna.

   :::: {.content-visible .mf1-hint-online when-format="html"}
   ::: {.callout-note collapse="true" data-hint-key="true"}
   ### Naputak
   deplasman je $\Delta = \rho gV_{ist}$, a za male nagibe povratni moment je $M_r = \Delta GM\sin\varphi$; znak $GM$ odlučuje o stabilnosti.
   :::
   ::::
   :::: {.content-visible .mf1-answer-online when-format="html"}
   ::: {.callout-tip collapse="true" data-answer-key="true"}
   ### Kontrolni rezultat

   $\Delta \approx 6{,}07\ \text{kN}$; $M_r \approx 133\ \text{N·m}$; $GM > 0$ pa je ravnoteža stabilna.
   :::
   ::::
   **Skica:** da - presjek tijela s težištem, metacentrom, nagibom $\varphi$ i ramenom povratnog momenta.

6. [**T4**]{#task-u07-pravokutna-servisna-platforma-duljine-i-sirine-pluta} Pravokutna servisna platforma duljine $L = 2{,}80\ \text{m}$ i širine $B = 1{,}20\ \text{m}$ pluta na granici ulja gustoće $\rho_o = 820\ \text{kg/m}^3$ debljine $\delta = 0{,}08\ \text{m}$ i vode gustoće $\rho_w = 998\ \text{kg/m}^3$. Nakon pomaka akumulatora lijevi rub uronjen je $h_L = 0{,}26\ \text{m}$, a desni $h_D = 0{,}18\ \text{m}$. Ukupna masa platforme s opremom je $m=690\ \text{kg}$, od čega akumulator ima $m_a=70\ \text{kg}$, a ukupno težište nalazi se na $KG=0{,}200\ \text{m}$ iznad dna. Odredi srednji uron, volumene istisnine u ulju i vodi, bočni pomak rezultantnoga centra uzgona, ekvivalentne $KB$, $BM$ i $GM$ te udaljenost akumulatora od osi simetrije. Rubni uroni mjere se s nesigurnošću $\pm3\ \text{mm}$, vrijedi $\rho_w=998\pm3\ \text{kg/m}^3$, $m_a=70\pm1\ \text{kg}$ i $KG=0{,}200\pm0{,}005\ \text{m}$; ostale podatke uzmi kao točne. Konzervativno procijeni najveću moguću udaljenost akumulatora provjerom rubnih kombinacija ulaza i odluči smije li se raspored prihvatiti ako montažni koridor dopušta najviše $0{,}34\ \text{m}$ od osi.

   :::: {.content-visible .mf1-hint-online when-format="html"}
   ::: {.callout-note collapse="true" data-hint-key="true"}
   ### Naputak
   najprije uzmi $h_m=(h_L+h_D)/2$ i $m_\Delta=\rho_oV_o+\rho_wV_w$. Za položaje uzgonskih doprinosa vrijedi $z_{B,o}=h_m-\delta/2$ i $z_{B,w}=(h_m-\delta)/2$, pa izračunaj $KB_{eq}$ njihovim uzgonskim težinjenjem. U ovom modelu $BM_{eq}=\rho_w I_T/m_\Delta$, gdje je $I_T=LB^3/12$, a $GM_{eq}=KB_{eq}+BM_{eq}-KG$. Tek zatim primijeni $m_a e=mGM_{eq}\tan\theta$ i $\tan\theta=(h_L-h_D)/B$. Za konzervativni omotač izračunaj svih $2^5=32$ rubnih kombinacija pet nesigurnih skalarnih ulaza.
   :::
   ::::
   :::: {.content-visible .mf1-answer-online when-format="html"}
   ::: {.callout-tip collapse="true" data-answer-key="true"}
   ### Kontrolni rezultat

   $h_m=0{,}220\ \text{m}$; $V_o\approx0{,}269\ \text{m}^3$; $V_w\approx0{,}470\ \text{m}^3$; $m_\Delta\approx689{,}9\ \text{kg}$. Geometrijski su $y_{B,w}\approx0{,}0571\ \text{m}$ i $y_B\approx0{,}0389\ \text{m}$, ali $y_B$ nije $GZ$. Dobiva se $KB_{eq}\approx0{,}105\ \text{m}$, $BM_{eq}\approx0{,}583\ \text{m}$, $GM_{eq}\approx0{,}488\ \text{m}$ i $e\approx0{,}321\ \text{m}$. Najveća rubna vrijednost nastaje za $h_L=0{,}263\ \text{m}$, $h_D=0{,}177\ \text{m}$, $\rho_w=1001\ \text{kg/m}^3$, $m_a=69\ \text{kg}$ i $KG=0{,}195\ \text{m}$ te iznosi $e_{max}\approx0{,}354\ \text{m}$. Nominalni račun prolazi, ali raspored se uz zadanu nesigurnost ne prihvaća za koridor od $0{,}34\ \text{m}$ bez preciznijega mjerenja ili pomicanja akumulatora prema osi. To je odluka unutar zadanoga početnog modela, ne normativna provjera stabiliteta.
   :::
   ::::
   **Skica:** da - platforma na granici ulja i vode, rubni uroni $h_L$ i $h_D$, granica fluida i bočni pomak akumulatora.
:::::

![Skice uz zadatke za vježbu — pontoni, areometri i plutajuće platforme.](../assets/print/u07_vjezbe_skice.svg){#fig-u07-vjezbe fig-align="center" fig-alt="Skice uz zadatke za vježbu — pontoni, areometri i plutajuće platforme."}

::: {.mf1-zavrsni-okvir}
<p class="mf1-box-label">Za ponijeti iz poglavlja</p>

**Sažeta provjera prije računa**

- Treba razdvojiti ukupni istisnuti volumen od raspodjele tog volumena po širini tijela.
- Srednju uronjenost treba računati iz ukupne težine, a ne iz momentne ravnoteže.
- Iz rubnih urona najprije se dobiva $\tan\theta$; za položaj tereta zatim trebaju $KB$, $BM$, $KG$ i $GM$.
- Prije pisanja znakova u momentima treba jasno odrediti na koju je stranu pomaknut teret.
- Treba provjeriti koristi li se isti koordinatni smjer za položaj težine i za položaj centra uzgona.
- Treba provjeriti je li dobiveni pomak tereta uopće geometrijski moguć.

**Najčešća pogreška**

Najčešće su dvije povezane greške: pokušati iz razlike urona dobiti ukupni volumen istisnine te izjednačiti geometrijski pomak centra uzgona $y_B=BM\tan\theta$ s krakom stabilnosti. Razlika urona govori o nagibu; položaj pomaknutoga tereta slijedi tek iz $w e=\Delta GM\tan\theta$, nakon što je zadan ili izračunan $KG$.

**Nakon ovoga poglavlja mora biti moguće**

1. povezati Arhimedov zakon s realnim istisnutim volumenom.
2. odvojiti ravnotežu vertikalnih sila od ravnoteže momenata plivajućeg tijela.
3. iz geometrije urona i $GM$ odrediti što nagib govori o pomaku tereta, bez implicitne pretpostavke $BG=0$.

**U tehnici to znači**

Ponton, plutajuća dizalica ili radna platforma mogu zadovoljiti uvjet uzgona, a ipak ostati loše raspoređeni i skloni nagibu. Zato ovo poglavlje daje početne procjene rasporeda tereta, gaza i maloga nagiba, ali ne zamjenjuje cjelovitu provjeru stabilnosti i konstrukcije.

**Granica modela**

Ovdje se promatra statička ravnoteža ili mala odstupanja od nje. U valovima, pri slobodnoj površini unutar spremnika ili pri većim kutovima nagiba stvarna stabilnost može biti bitno drukčija od slike dobivene iz jednostavne ravnoteže sila i momenata.

<span class="mf1-ch-ref"><span class="mf1-ch-code">pog. 6</span><span class="mf1-ch-title">Uzgon, plivanje i početni stabilitet</span></span> lomi se na dvije stabilne navike: uzgon uvijek dolazi iz istisnine, a nagib iz momenta. Miješanje te dvije stvari gotovo sigurno ruši fizikalni smisao zadatka.
:::

::: {.mf1-numerika}
<p class="mf1-box-label">Numerički most</p>

**Gdje ovo živi u numerici.** Slobodna površina može se opisivati metodom hvatanja međupovršine poput VOF-a, ali i drugim modelima, primjerice potencijalnim ili plitkovodnim, ovisno o skali i pitanju. Nije svaki problem otvorenoga toka nužno VOF simulacija.

**Što numerički alat radi s tim.** Kod potpuno spregnutoga modela polje strujanja daje tlakne i viskozne sile, a jednadžbe gibanja tijela vraćaju novi položaj i nagib. Očuvanje mase faza, hidrostatska ravnoteža, položaj slobodne površine i bilanca sila moraju se provjeravati odvojeno.

**Tipičan scenarij.** Numerički valni bazen može procjenjivati dinamički gaz, nagib i opterećenja u zadanom valnom polju. Takav rezultat ne predstavlja automatski „stvarno more” i ne zamjenjuje propisanu stabilitetnu provjeru; traži mrežnu i vremensku konvergenciju te validaciju za ciljane odzive [@nasa-cfd-vv; @asme-vv20-2009]. Početni $GM$ ostaje koristan mali-kutni referentni test, ne kriterij cijele dinamičke stabilnosti.

> *Nije gradivo MF1. Ručna ravnoteža uzgona i težine daje osnovni test kojem se složeniji numerički model mora vratiti u mirnom graničnom slučaju.*
:::
