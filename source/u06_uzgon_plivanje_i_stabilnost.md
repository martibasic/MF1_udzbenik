![Pregled poglavlja: Uzgon, plivanje i stabilitet](../assets/print/u07_fig_uvod_pregled.svg){#fig-uvod-u07 fig-align="center" fig-alt="Pregled poglavlja: Uzgon, plivanje i stabilitet"}

**Tumačenje skice.** Uzgon $F_U=\rho gV_{\mathrm{ist}}$ jest rezultanta tlakova na tijelo; ne dodaje se još jednom ako su tlačne sile već zbrojene. Za plivanje vertikalna ravnoteža daje $\rho gV_{\mathrm{ist}}=F_G=mg$, odnosno $V_{\mathrm{ist}}=m/\rho$.

Težinu, istisnuti volumen i momentni raspored sila treba promatrati odvojeno. Uzgon prolazi kroz centar uzgona B, a težina kroz težište G. Ako je metacentar M iznad G, moment pri malom nagibu vraća tijelo prema uspravnom položaju.

## Uzgon, plivanje i početni stabilitet

Analiza plivajućega tijela obuhvaća ukupnu težinu, istisnuti volumen te položaj i momente sila uzgona i težine.

::: {.mf1-application}
<p class="mf1-box-label">Inženjerski kontekst</p>

Za plovilo ili plutajuću platformu uz istisnuti volumen treba poznavati položaj težišta i centra uzgona. Pomak tereta mijenja moment tih sila i nagib tijela. Taj se račun primjenjuje pri rasporedu opreme na pontonu, provjeri početnog stabiliteta plovila i analizi plutajuće dizalice.
:::

**Procijenjeno vrijeme rada uz priručnik:** 10 sati.

## Sila uzgona

Za tijelo koje miruje u fluidu vrijedi da je sila uzgona jednaka težini istisnutog fluida:

$$F_U = \rho g V$$ {#eq-uzgon-stabilitet-fizikalni-uvod-i-matematicki-izvod-01}

Za plivajuće tijelo u ravnoteži ta sila mora biti jednaka ukupnoj težini tijela i svih tereta na njemu. Drugi je korak geometrija: gdje djeluju težina i uzgon i kakav moment nastaje ako je teret bočno pomaknut. Kod prizmatskih tijela s ravnim dnom vrlo se često može odvojiti srednji gaz od nagiba:

- srednji gaz dolazi iz ukupne težine
- razlika gazova po širini dolazi iz momentne ravnoteže

To je razdvajanje temelj početnih zadataka o plivanju i stabilitetu.

## Matematički izvod

Najjednostavniji put prema Arhimedovu zakonu polazi od potpuno uronjenoga prizmatičnog tijela vodoravne površine $A$. Neka na slobodnoj površini djeluje tlak $p_{pov}$. Na gornju plohu na dubini $h_1$ djeluje sila

$$
F_1 = p_1A = (p_{pov} + \rho gh_1)A
$$ {#eq-uzgon-stabilitet-matematicki-izvod-01}

prema dolje, a na donju plohu na dubini $h_2$ sila

$$
F_2 = p_2A = (p_{pov} + \rho gh_2)A
$$ {#eq-uzgon-stabilitet-matematicki-izvod-02}

prema gore. Neto vertikalna hidrostatička sila iznosi zato

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

::: {#ex-u07-uzgon-na-potonulo-pumpno-kuciste-pri-ispitivanju .mf1-we}
<p class="mf1-box-label">Uzgon na potonulo pumpno kućište pri ispitivanju &nbsp;<span class="mf1-level">T1</span></p>

**Tekst zadatka**

Pumpno kućište mase $m = 85\ \text{kg}$ i istisnutog volumena $V_{ist} = 0{,}045\ \text{m}^3$ potpuno je uronjeno u mirnu morsku vodu gustoće $\rho = 1025\ \text{kg/m}^3$, bez dodira s dnom.

**Traži se**

1. Odredi silu uzgona na kućište.
2. Odredi neto silu i silu držanja (iznos i smjer) potrebnu da kućište potpuno uronjeno miruje.

![Uzgon i težina potpuno uronjenoga pumpnog kućišta.](../assets/print/u07_fig_pumpno_kuciste.svg){#fig-u07-pumpno-kuciste-uzgon fig-align="center" fig-alt="Uzgon i težina potpuno uronjenoga pumpnog kućišta."}

**Veza s proračunom.** Sile djeluju na kućište, uz pozitivnu os $z$ prema gore. Skica prikazuje samo uzgon i težinu; silu držanja treba odrediti, a njezin predznak slijedi iz usporedbe uzgona i težine: ne treba unaprijed pretpostaviti smjer djelovanja držača.

**Rješenje**

$$
F_U = \rho g V_{ist} = 1025 \cdot 9{,}81 \cdot 0{,}045 = 452{,}5\ \text{N} \approx 0{,}453\ \text{kN}
$$ {#eq-uzgon-stabilitet-rijeseni-primjer-uzgon-na-potonulo-pumpno-kucist-01}

Težina kućišta:
$$
F_G = mg = 85 \cdot 9{,}81 = 833{,}9\ \text{N} \approx 0{,}834\ \text{kN}
$$ {#eq-uzgon-stabilitet-rijeseni-primjer-uzgon-na-potonulo-pumpno-kucist-02}

Neto sila (prema dolje, kućište tone samo):
$$
F_{neto} = F_G - F_U = 833{,}9 - 452{,}5 = 381{,}4\ \text{N}
$$ {#eq-uzgon-stabilitet-rijeseni-primjer-uzgon-na-potonulo-pumpno-kucist-03}

Kućište tone bez dodatne sile prema dolje. Za njegovo statičko pridržavanje ili ravnomjerno podizanje dok je potpuno uronjeno potrebna je sila od približno 381 N prema gore.

**Provjera i tumačenje**

Prosječna gustoća kućišta, $m/V_{ist}\approx1889\ \text{kg/m}^3$, veća je od gustoće mora, pa kućište tone. Materijal stijenke sam nije dovoljan za taj zaključak jer šuplje hermetičko tijelo može imati mnogo manju prosječnu gustoću.
:::

::: {.mf1-interaktivno}
<p class="mf1-box-label">Interaktivni prikaz — Gaz plivajućeg tijela</p>

**Predvidi.** Hoće li isti blok imati veći gaz u slatkoj ili morskoj vodi? Što se mijenja ako masa poraste za 10 %?

**Provjeri i protumači.** Usporedi formulu s numeričkom nulom bilance sila. Prepoznaj granicu pri dosezanju pune visine bloka; ovaj pokus gaza ne provjerava stabilitet.

<div class="mf1-interaktivno-akcija">
<a class="mf1-interaktivno-veza" href="https://martibasic.github.io/MF1_udzbenik/jlite/lab/index.html?path=u07_gaz_plivajuceg_tijela.ipynb">Pokreni u pregledniku</a>
<a class="mf1-interaktivno-veza" href="https://colab.research.google.com/github/martibasic/MF1_udzbenik/blob/main/notebooks/u07_gaz_plivajuceg_tijela.ipynb" target="_blank" rel="noopener">Pričuvno: otvori u Colabu</a>
<img class="mf1-interaktivno-qr" src="../assets/qr/u07_gaz_plivajuceg_tijela.svg" alt="QR kod za interaktivni prikaz gaza plivajućeg tijela"/>
</div>

:::

Isti rezultat vrijedi i za proizvoljan oblik tijela: neto hidrostatička sila jednaka je težini fluida koji bi ispunio istisnuti volumen. Pravac djelovanja te sile prolazi kroz centar uzgona, tj. kroz težište istisnutoga volumena. Obrazloženje je kratko: zamislimo da istisnuti volumen ispunjava isti fluid u mirovanju; na njega djeluju isti okolni tlakovi kao na tijelo, a on je u ravnoteži pod vlastitom težinom, pa rezultanta tlakova mora biti jednaka toj težini i prolaziti njezinim težištem.

Iz toga odmah slijedi i prvo pravilo stabiliteta. Kod potpuno uronjenog tijela stabilan je položaj onaj u kojem je težište tijela $G$ ispod centra uzgona $B$; ako se te dvije točke poklope, ravnoteža je neutralna, a ako je $G$ iznad $B$, mali poremećaj daje prevrtni moment. Kod plivajućeg tijela slika je drukčija jer se pri malom nagibu oblik istisnutoga volumena mijenja, pa se i centar uzgona pomiče. Tada se uvodi metacentar $M$, a znak metacentarske visine $GM$ odlučuje o početnom stabilitetu: $GM > 0$ znači povratni moment, $GM = 0$ neutralnost u linearnoj aproksimaciji, a $GM < 0$ nestabilan položaj.

Za plivajuće tijelo vertikalna ravnoteža tada daje

$$
\rho gV_{ist} = F_G = mg
$$ {#eq-uzgon-stabilitet-interaktivni-prikaz-gaz-plivajuceg-tijela-01}

odnosno

$$
V_{ist} = \frac{m}{\rho}.
$$ {#eq-uzgon-stabilitet-interaktivni-prikaz-gaz-plivajuceg-tijela-02}

::: {.mf1-fizikalno-znacenje}
<p class="mf1-box-label">Fizikalno značenje</p>
Plivajuće tijelo uranja toliko da masa istisnutog fluida bude jednaka masi tijela. Volumen istisnine $V_{ist}$ nije stalni geometrijski volumen tijela: isti brod u moru (~1025 kg/m³) istisne manji volumen nego u slatkoj vodi (~998 kg/m³), pa plovi nešto više.
:::

::: {#cfd-ponton-gaz-stabilitet .mf1-cfd title="Računalna dinamika fluida"}

**Ponton s baterijskim spremnikom na palubi.** Najprije tražimo gaz u mirnoj vodi. U CFD modelu zadamo oblik trupa, masu i položaj težišta, a vertikalno gibanje tijela povežemo sa silama fluida. Uzgon nastaje integracijom tlaka po trupu; ne dodajemo ga još jednom kao zasebnu silu $\rho gV_{ist}$. Ručni @ex-u07-koliki-gaz-ima-radni-ponton-pri-simetricnom provjerava gaz uz simetričan teret i uspravan ponton.

**Zastani i promisli.** Isti teret podignut je više na pontonu, a uspravni gaz ostao je jednak. Je li time potvrđen i jednak početni stabilitet?

Isti gaz nakon podizanja tereta ne potvrđuje isti stabilitet. Za isti trup i masu viši $KG$ smanjuje $GM$, premda uspravna slika ostaje jednaka. Zato sljedeći račun dopušta naginjanje: uspoređujemo momente i gibanje, odvojeno od ravnotežnog gaza.

[]{#kako-računalo-prati-plutanje}
:::

To je tek prvi dio fizikalne slike.[]{#postupak-rješenja} Jednoliki tlak na slobodnoj površini potpuno se poništio između gornje i donje plohe, pa uzgon ne ovisi o atmosferskom ni o apsolutnom tlaku, nego samo o razlici dubina. $V_{ist}$ ne određuje nagib: ako težište sustava ne leži na istoj okomici kao centar uzgona, pojavljuje se moment koji tijelo zakreće, pa mora biti zadovoljena i ravnoteža momenata.

::: {.mf1-izvod}
<p class="mf1-box-label">Matematički izvod — Bočni pomak centra uzgona pri linearnoj promjeni gaza</p>

Promatra se pravokutni ponton duljine $L$ i širine $b$ koji u nagnutom (ili nesimetrično opterećenom) položaju ima različite gazove na lijevoj i desnoj strani: $T_L$ uz lijevu i $T_D$ uz desnu stijenku, uz srednji gaz $T_m = (T_L + T_D)/2$.

Poprečni presjek istisnutoga volumena je trapez s okomicama duljina $T_L$ i $T_D$ na razmaku $b$. Taj se trapez razlaže na pravokutnik visine $T_D$ i trokut kateta $(T_L - T_D)$ i $b$ smješten uz lijevu stijenku. Pripadne površine i položaji težišta u poprečnom presjeku (mjereno od lijevog ruba) iznose

$$
A_1 = T_D b, \qquad \bar{x}_1 = \frac{b}{2},
$$ {#eq-uzgon-stabilitet-matematicki-izvod-bocni-pomak-centra-uzgona-pri-01}

$$
A_2 = \frac{1}{2}(T_L - T_D) b, \qquad \bar{x}_2 = \frac{b}{3}.
$$ {#eq-uzgon-stabilitet-matematicki-izvod-bocni-pomak-centra-uzgona-pri-02}

Težište cijelog trapeza, mjereno od lijevog ruba, dobiva se prvim momentom

$$
\bar{x} = \frac{A_1 \bar{x}_1 + A_2 \bar{x}_2}{A_1 + A_2} = \frac{T_D b \cdot \tfrac{b}{2} + \tfrac{1}{2}(T_L - T_D)b \cdot \tfrac{b}{3}}{b T_m}
= \frac{b(T_L + 2T_D)}{6 T_m}.
$$ {#eq-uzgon-stabilitet-matematicki-izvod-bocni-pomak-centra-uzgona-pri-03}

Bočni pomak centra uzgona od centra pontona (od ravnine simetrije, mjereno prema strani s većim gazom) iznosi

$$
y_B = \frac{b}{2} - \bar{x} = \frac{b}{2} - \frac{b(T_L + 2T_D)}{6 T_m}
= \frac{b\,(T_L - T_D)}{12\, T_m}.
$$ {#eq-uzgon-stabilitet-matematicki-izvod-bocni-pomak-centra-uzgona-pri-04}

Provjera: pri simetričnom gazu $T_L = T_D = T_m$ dobiva se $y_B = 0$, što znači da centar uzgona ostaje u središnjoj okomici. Pri tipičnoj razlici gazova $T_L - T_D = 0{,}05\ \text{m}$ na pontonu širine $b = 1{,}2\ \text{m}$ sa srednjim gazom $T_m = 0{,}2\ \text{m}$ pomak centra uzgona iznosi $y_B = 1{,}2 \cdot 0{,}05/(12 \cdot 0{,}2) = 0{,}025\ \text{m}$, dakle $2{,}5\ \text{cm}$.

Ta je veličina **geometrijski pomak centra uzgona u koordinatama tijela**, a nije sama po sebi poluga stabiliteta $GZ$ ni razmak pravaca djelovanja uzgona i ukupne težine. Trapez s okomitim krakovima slika je prvoga reda: kruti nagnuti pravokutnik ima i nagnute bokove, a razlika višeg reda u kutu obrađena je u okviru o granici modela. Iz geometrije rubnih gazova vrijedi

$$
\tan\varphi=\frac{T_L-T_D}{b},
$$ {#eq-uzgon-stabilitet-matematicki-izvod-bocni-pomak-centra-uzgona-pri-05}

a za pravokutnu vodnu liniju

$$
BM=\frac{b^2}{12T_m},\qquad y_B=BM\tan\varphi.
$$ {#eq-uzgon-stabilitet-matematicki-izvod-bocni-pomak-centra-uzgona-pri-06}

Položaj ukupnoga težišta ulazi zasebno preko $GM=KB+BM-KG$, a veza pomaka tereta i nagiba, $m_k e=\Delta\,GM\tan\varphi$, izvodi se u sljedećem okviru iz povratnog momenta (@eq-uzgon-stabilitet-matematicki-izvod-bocni-pomak-centra-uzgona-pri-07). Bez podatka o $KG$ rubni gazovi zato ne određuju jednoznačno položaj pomaknutoga tereta.
:::

::: {.mf1-izvod}
<p class="mf1-box-label">Matematički izvod — Metacentarski radijus $BM = I_T / V_{ist}$</p>

Promatra se plivajuće tijelo nagnuto za mali kut $\varphi$ oko uzdužne osi koja prolazi kroz njegovu vodnu liniju (presjek tijela s mirnom slobodnom površinom). Istisnuti volumen ostaje konstantan jer se masa tijela nije promijenila: pri nagibu jedna strana tijela dublje uranja, a druga izranja.

Geometrijski to znači da se s jedne strane osi rotacije pojavljuje klin dodatne istisnine (točke na udaljenosti $y > 0$ uranjaju se za $y\varphi$ dublje), a s druge strane nestaje jednak klin istisnine ($y < 0$, voda se povlači za $|y|\varphi$). Pomak centra uzgona $B \to B'$ u horizontalnom smjeru izračunava se prvim momentom preraspodjele volumena:

$$
V_{ist}\cdot BB' = \int_{A_{wl}} y \cdot (y\varphi)\, dA = \varphi \int_{A_{wl}} y^2\, dA = \varphi\, I_T,
$$ {#eq-uzgon-stabilitet-matematicki-izvod-metacentarski-radijus-01}

gdje je $A_{wl}$ površina vodne linije, a

$$
I_T = \int_{A_{wl}} y^2\, dA
$$ {#eq-uzgon-stabilitet-matematicki-izvod-metacentarski-radijus-02}

drugi moment površine vodne linije oko osi rotacije. Otud slijedi pomak centra uzgona

$$
BB' = \frac{I_T\, \varphi}{V_{ist}}.
$$ {#eq-uzgon-stabilitet-matematicki-izvod-metacentarski-radijus-03}

Metacentar $M$ definiran je kao točka u kojoj se sijeku okomica kroz novi centar uzgona $B'$ i prvotna os simetrije tijela. Za male kutove vrijedi geometrijski

$$
BB' = BM \cdot \varphi,
$$ {#eq-uzgon-stabilitet-matematicki-izvod-metacentarski-radijus-04}

pa izjednačavanjem dvaju izraza nastaje središnja relacija stabiliteta

$$
\boxed{BM = \frac{I_T}{V_{ist}}}.
$$ {#eq-uzgon-stabilitet-matematicki-izvod-metacentarski-radijus-05}

Za pravokutnu vodnu liniju širine $b$ i duljine $L$ vrijedi $I_T = L b^3/12$, pa je

$$
BM = \frac{L b^3}{12\, V_{ist}}.
$$ {#eq-uzgon-stabilitet-matematicki-izvod-metacentarski-radijus-06}

Za pravokutne, geometrijski usporedive vodne linije pri **fiksnim** $L$ i $V_{ist}$ vrijedi $BM\propto b^3$. Šira vodna linija tada snažno povećava metacentarski radijus. To samo po sebi nije potpuna tvrdnja o stabilitetu broda: konačni $GM$ ovisi i o visini težišta, obliku trupa, istisnini i stanju opterećenja.

**Dva fluida.** Ako tijelo pluta u sloju lakšeg fluida gustoće $\rho_o$ i debljine $\delta$ iznad težeg fluida gustoće $\rho_w$, a dno mu je u težem fluidu, pri nagibu nastaju dva para klinova: na slobodnoj površini klin lakšeg fluida s momentom $\rho_o I_T\varphi$ i na razdjelnici klin u kojem teži fluid zamjenjuje lakši, s momentom $(\rho_w-\rho_o)I_T\varphi$. Zbroj je $\rho_w I_T\varphi$, pa uz masu istisnine $\Delta=\rho_oV_o+\rho_wV_w$ vrijedi

$$
BM_{eq}=\frac{\rho_w I_T}{\rho_oV_o+\rho_wV_w}.
$$ {#eq-metacentarski-radijus-dva-fluida}

Gustoća gornjeg sloja ulazi samo preko $\Delta$: za $\rho_o\to\rho_w$ izraz prelazi u $I_T/V_{ist}$, a za $\rho_o\to0$ u $I_T/V_w$, kao da tijelo pluta samo u težem fluidu. Pripadni $KB_{eq}$ jest težište istisnute mase, težinjeno gustoćama slojeva, i $GM_{eq}=KB_{eq}+BM_{eq}-KG$. Model se primjenjuje u @ex-u07-plutajuca-servisna-platforma-na-granici-ulja-i i u zadatku Z6.

Robustan geometrijski zapis metacentarske visine jest

$$
GM=KM-KG
=KB+BM-KG.
$$ {#eq-uzgon-stabilitet-matematicki-izvod-metacentarski-radijus-07}

Ako se $G$ nalazi iznad $B$, tada se isti odnos može pisati $GM=BM-BG$. Zapis s $KM-KG$ ostaje jednoznačan i kada je $G$ ispod $B$.

**Ravnoteža pri pomaku tereta.** Pri malom nagibu $\varphi$ uzgon $\Delta g$ djeluje okomito kroz $B'$, a težina $\Delta g$ kroz $G$; vodoravni razmak tih pravaca jest poluga stabiliteta $GZ=GM\sin\varphi$, pa povratni moment iznosi $M_{pov}=\Delta g\,GM\sin\varphi$. Ako se teret mase $m_k$ pomakne poprečno za $e$ bez promjene visine, stvara nagibni moment $m_kg\,e\cos\varphi$. Izjednačavanje daje

$$
m_k e\cos\varphi=\Delta\,GM\sin\varphi
\quad\Longrightarrow\quad
\boxed{m_k e=\Delta\,GM\tan\varphi},
$$ {#eq-uzgon-stabilitet-matematicki-izvod-bocni-pomak-centra-uzgona-pri-07}

gdje je $\Delta=\rho V_{ist}$ masa istisnine, jednaka ukupnoj masi sustava, a $g$ se pokratio. Isti zapis vrijedi za pokus nagibanja: izmjereni $\varphi$ uz poznate $m_k$, $e$ i $\Delta$ daje $GM$. Izjednačavanje $\Delta y_B=m_ke$ bilo bi dopušteno samo u posebnom slučaju $KG=KB$, odnosno $BG=0$, kada je $GM=BM$.

Predznak $GM$ odlučuje o **početnom** stabilitetu uspravnoga položaja. Pri $GM>0$ mali nagib stvara povratni moment, pri $GM=0$ linearni je član neutralan, a pri $GM<0$ uspravni je položaj početno nestabilan. Negativan početni $GM$ ne dokazuje sam po sebi konačno prevrtanje: tijelo može prijeći u drugi ravnotežni položaj, što se provjerava punom krivuljom $GZ$ i geometrijom otvora.
:::

::: {.mf1-granica-modela}
<p class="mf1-box-label">Granica modela — Koliko je „mali” kut za pravokutni ponton?</p>

Za trup s okomitim bokovima, dok je dno uronjeno i paluba suha, pomak centra uzgona može se izračunati točno: vodoravno $BM\tan\varphi$, a vertikalno $\tfrac12BM\tan^2\varphi$. Poluga stabiliteta tada glasi

$$
GZ=\left(GM+\tfrac12BM\tan^2\varphi\right)\sin\varphi,
$$ {#eq-poluga-okomiti-bokovi}

pa je relativna pogreška linearne aproksimacije $GZ\approx GM\sin\varphi$ jednaka $\tfrac12BM\tan^2\varphi/GM$. Za platformu iz @ex-u07-plutajuca-servisna-platforma-s-pomaknutim-kompresorom-t2 ($GM=0{,}245\ \text{m}$, $BM=0{,}298\ \text{m}$, $\varphi=6{,}84^\circ$) korekcija iznosi $0{,}0021\ \text{m}$, oko $0{,}9\ \%$ od $GM$; pri $\varphi=5^\circ$ pada ispod $0{,}5\ \%$, što je razlog zadane granice $|\varphi|\le5^\circ$ u zadatcima Z3 i Z6. Granica stoga nije univerzalna: ovisi o omjeru $BM/GM$ i prestaje vrijediti čim rub palube uroni ili dno izroni. Za druge oblike trupa i veće kutove treba krivulja $GZ(\varphi)$ iz stvarne geometrije.
:::

::: {.mf1-cfd title="Računalna dinamika fluida"}

**Vraća li se ponton i koliko se dugo njiše?** Dvije izvedbe pontona s istom masom, ali različitom visinom težišta najprije držimo na malom zadanom nagibu. Nakon smirivanja vode iz tlaka dobijemo moment i usporedimo ga s početnim $GM$. To je statička provjera smjera i jačine vraćanja.

Zatim ponton pustimo iz tog nagiba i pratimo kut kroz vrijeme. Uz masu i težište sada trebamo moment tromosti tijela; voda dodaje pridruženu masu (dodatnu tromost fluida koji se giba s tijelom) i prigušenje, pa mijenja odziv. Iz zapisa procjenjujemo period i prigušenje njihanja. Pozitivan $GM$ sam ne određuje nijedno od toga. Za odziv na valove dodajemo dolazni val i granice koje ne vraćaju neželjene odraze. Prijenos pokusa s manjega modela na stvarni ponton razmatra se u []{.mf1-chapter-ref target="u11"}.
:::

::: {.mf1-izvod}
<p class="mf1-box-label">Matematički izvod — Krivulja stabiliteta $GZ(\varphi)$ i konačni nagib</p>

Metacentarski radijus $BM$ izveden je za **infinitezimalni nagib**. Za konačan nagib koristi se **krivulja statičkog stabiliteta** $GZ(\varphi)$.

Pri nagibu $\varphi$ centar uzgona pomakne se u $B_\varphi$ prema **stvarnoj geometriji uronjenoga dijela**, dok $G$ ostaje fiksiran u tijelu. Poluga stabiliteta $GZ$ vodoravna je udaljenost od $G$ do okomice kroz $B_\varphi$ i za svaki se konačni kut ponovno računa iz hidrostatske geometrije. Veza s početnom teorijom glasi

$$
GZ(0)=0,\qquad \left.\frac{dGZ}{d\varphi}\right|_{\varphi=0}=GM,
$$ {#eq-uzgon-stabilitet-matematicki-izvod-krivulja-stabilnosti-i-finitni-01}

pa je za dovoljno mali kut $GZ\approx GM\sin\varphi\approx GM\varphi$. Dodavanje neodređene korekcije $f(\varphi)$ nije postupak proračuna pri velikom nagibu.

Povratni moment para težine i uzgona iznosi

$$
M_{povratni}(\varphi) = \rho g V_{ist}\cdot GZ(\varphi),
$$ {#eq-uzgon-stabilitet-matematicki-izvod-krivulja-stabilnosti-i-finitni-02}

a prvi kut nakon pozitivnoga područja pri kojem $GZ$ ponovno postane nula naziva se **kut nestajanja stabiliteta** $\varphi_v$. Stvarno uporabljivo područje može završiti ranije, primjerice kutom naplavljivanja kroz nezaštićeni otvor.

Krivulja $GZ(\varphi)$ za određeno stanje opterećenja ima sljedeća osnovna svojstva:

- pri $\varphi = 0$ vrijedi $GZ = 0$ (uspravni položaj);
- nagib krivulje u ishodištu jednak je $GM$ — poveznica s metacentarskom teorijom;
- položaj i iznos maksimuma ovise o geometriji, otvorima i stanju opterećenja;
- pri $\varphi_v$ krivulja siječe nulu, ako naplavljivanje ili druga granica nije nastupila ranije.

**Integral ispod krivulje**

$$
A = \int_0^{\varphi_v} GZ(\varphi)\,d\varphi
$$ {#eq-uzgon-stabilitet-matematicki-izvod-krivulja-stabilnosti-i-finitni-03}

ima dimenziju $\text{m rad}$ i predstavlja energiju **normiranu težinom istisnine** $\Delta g$. Stvarni kvazistatički rad povratnoga momenta između dvaju kutova jest

$$
W=\rho gV_{ist}\int_{\varphi_1}^{\varphi_2}GZ(\varphi)\,d\varphi.
$$ {#eq-uzgon-stabilitet-matematicki-izvod-krivulja-stabilnosti-i-finitni-04}

Za brodove na koje se primjenjuju opći kriteriji IMO-ova *2008 Intact Stability Codea* provjerava se skup uvjeta, među ostalim: površina najmanje $0{,}055\ \text{m rad}$ do $30^\circ$; najmanje $0{,}09\ \text{m rad}$ do $40^\circ$ ili kuta naplavljivanja ako je manji; najmanje $0{,}03\ \text{m rad}$ između $30^\circ$ i te gornje granice; $GZ\ge0{,}20\ \text{m}$ pri kutu od najmanje $30^\circ$; maksimum $GZ$ pri kutu ne manjem od $25^\circ$; te početni $GM_0\ge0{,}15\ \text{m}$ [@imo-is-code-2008]. Primjenjivost, dodatni kriteriji i iznimke ovise o vrsti broda i mjerodavnoj administraciji, pa dvije površine same ne dokazuju usklađenost.

Metacentarska teorija opisuje samo početni odziv oko uspravnoga položaja. Stabilitet pri konačnom nagibu, na valovima ili nakon oštećenja zahtijeva odgovarajuću krivulju $GZ$, otvore i kut naplavljivanja, dinamičke utjecaje te posebne kriterije za neoštećeni ili oštećeni brod [@imo-damage-stability].
:::

::: {.mf1-dublje}
<p class="mf1-box-label">Učinak slobodne površine u tanku</p>

Ako tank nije pun, tekućina u njemu pri nagibu prelijeva prema nižoj strani i njezino se težište pomiče jednako kao centar uzgona u klinu vodne linije. Taj pomak djeluje kao prividno podizanje težišta sustava za

$$
\delta GM=-\frac{\rho_t\,i_t}{\rho\,V_{ist}},
$$ {#eq-ucinak-slobodne-povrsine}

gdje je $i_t$ drugi moment slobodne površine tanka oko njegove uzdužne osi, $\rho_t$ gustoća tekućine u tanku, a $\rho V_{ist}=\Delta$ masa istisnine. Učinak ne ovisi o količini tekućine u tanku dok slobodna površina postoji, nego o njezinoj širini na treću potenciju. Da je tank iz @ex-u07-izolirani-puni-bocni-tank-kao-dodana-masa napola pun morem, vrijedilo bi $i_t=L_tb_t^3/12=15\cdot6^3/12=270\ \text{m}^4$ i, pri istoj istisnini, $\delta GM=-270/4172\approx-0{,}065\ \text{m}$: $GM$ bi pao s $4{,}23$ na oko $4{,}16\ \text{m}$. Na malom pontonu s tankom preko cijele širine isti izraz može poništiti cijeli $GM$; zato se tankovi drže punima ili praznima, a slobodne površine ograničavaju uzdužnim pregradama.
:::


## Riješeni primjeri

::: {#ex-u07-koliki-gaz-ima-radni-ponton-pri-simetricnom .mf1-we}
<p class="mf1-box-label">Koliki gaz ima radni ponton pri simetričnom opterećenju&nbsp;<span class="mf1-level">T1</span></p>

**Tekst zadatka**

Pravokutni ponton duljine $L = 2{,}40\ \text{m}$, širine $b = 1{,}20\ \text{m}$, visine boka $H = 0{,}32\ \text{m}$ i mase $m_p = 420\ \text{kg}$ nosi simetrično postavljenu opremu mase $m_o = 180\ \text{kg}$. Pluta bez nagiba u mirnoj vodi gustoće $\rho = 998\ \text{kg/m}^3$.

**Traži se**

1. Odredi istisnuti volumen vode u ravnotežnom položaju.
2. Odredi srednji gaz pontona $T$.
3. Odredi koliku dodatnu masu još može primiti prije nego što gornji rub dođe do razine vode.

![Ponton i gaz pri simetričnom opterećenju](../assets/print/u07_val2_ponton_gaz.svg){#fig-u07-ponton-i-gaz-pri-simetricnom-opterecenju fig-alt="Ponton i gaz pri simetričnom opterećenju"}

**Veza s proračunom.** Duljina $L$ okomita je na presjek; pri simetričnom opterećenju težina i uzgon imaju isti pravac djelovanja.

**Rješenje**

Ukupna masa sustava iznosi

$$
m = m_p + m_o = 420 + 180 = 600\ \text{kg}.
$$ {#eq-uzgon-stabilitet-rijeseni-primjer-koliki-gaz-ima-radni-ponton-01}

Za plivanje u ravnoteži vrijedi $\rho g V_{ist} = mg$, pa je istisnuti volumen

$$
V_{ist} = \frac{m}{\rho} = \frac{600}{998} \approx 0{,}601\ \text{m}^3.
$$ {#eq-uzgon-stabilitet-rijeseni-primjer-koliki-gaz-ima-radni-ponton-02}

Za pravokutni ponton vrijedi $V_{ist} = LbT$, odakle slijedi srednji gaz

$$
T = \frac{V_{ist}}{Lb} = \frac{0{,}601}{2{,}40 \cdot 1{,}20} \approx 0{,}209\ \text{m} \approx 20{,}9\ \text{cm}.
$$ {#eq-uzgon-stabilitet-rijeseni-primjer-koliki-gaz-ima-radni-ponton-03}

Granični slučaj prije zalijevanja palube dobiva se kad je gaz jednak ukupnoj visini boka, tj. $T = H = 0{,}32\ \text{m}$. Tada je najveći mogući istisnuti volumen

$$
V_{max} = LbH = 2{,}40 \cdot 1{,}20 \cdot 0{,}32 \approx 0{,}922\ \text{m}^3,
$$ {#eq-uzgon-stabilitet-rijeseni-primjer-koliki-gaz-ima-radni-ponton-04}

pa odgovarajuća ukupna masa iznosi

$$
m_{max} = \rho V_{max} = 998 \cdot 0{,}922 \approx 920\ \text{kg}.
$$ {#eq-uzgon-stabilitet-rijeseni-primjer-koliki-gaz-ima-radni-ponton-05}

Zato je dodatna masa koju ponton još može primiti

$$
\Delta m = m_{max} - m = 920 - 600 = 320\ \text{kg} \approx 3{,}2 \cdot 10^2\ \text{kg}.
$$ {#eq-uzgon-stabilitet-rijeseni-primjer-koliki-gaz-ima-radni-ponton-06}

**Provjera i tumačenje**

Gaz $0{,}209\ \text{m}<H=0{,}32\ \text{m}$, pa ponton ima nadvođe $0{,}111\ \text{m}$; dodatnih $320\ \text{kg}$ geometrijska je, a ne dopuštena rezerva.
:::

::: {#ex-u07-plutajuca-servisna-platforma-s-pomaknutim-kompresorom-t2 .mf1-we}
<p class="mf1-box-label">Plutajuća servisna platforma s pomaknutim kompresorom&nbsp;<span class="mf1-level">T2</span></p>

**Tekst zadatka**

Kruta pravokutna platforma duljine $L = 3{,}10\ \text{m}$ i širine $b = 1{,}00\ \text{m}$ ima masu $m_p = 676\ \text{kg}$ i težište $KG_p = 0{,}14\ \text{m}$ iznad dna. Na nju je bočno postavljen kompresor mase $m_k = 190\ \text{kg}$, s težištem $KG_k = 0{,}38\ \text{m}$ iznad dna. U vodi gustoće $\rho = 998\ \text{kg/m}^3$ izmjereni su gazovi rubova $T_L = 0{,}34\ \text{m}$ i $T_D = 0{,}22\ \text{m}$. Dno je ravno, bokovi okomiti, a nagib dovoljno malen za početnu metacentarsku teoriju (granica se kvantificira u provjeri).

**Traži se**

1. Odredi ukupni istisnuti volumen vode u ravnotežnom položaju.
2. Odredi $KB$, $BM$, $KG$ i početni $GM$ sustava te udaljenost $e$ težišta kompresora od uzdužne osi simetrije platforme.
3. Odredi za koliko je srednji gaz platforme veći nego prije postavljanja kompresora.

![Plutajuća platforma s pomaknutim kompresorom](../assets/print/u07_val1_platforma_kompresor.svg){#fig-u07-plutajuca-platforma-s-pomaknutim-kompresorom fig-alt="Plutajuća platforma s pomaknutim kompresorom"}

**Veza s proračunom.** B označuje centar uzgona; uzgon i ukupna težina djeluju na cijeli sklop.

**Rješenje**

Srednji gaz iznosi

$$
T_m = \frac{T_L + T_D}{2} = \frac{0{,}34 + 0{,}22}{2} = 0{,}28\ \text{m},
$$ {#eq-uzgon-stabilitet-rijeseni-primjer-plutajuca-servisna-platforma-s-01}

pa je istisnuti volumen

$$
V_{ist} = L b T_m = 3{,}10 \cdot 1{,}00 \cdot 0{,}28 = 0{,}868\ \text{m}^3.
$$ {#eq-uzgon-stabilitet-rijeseni-primjer-plutajuca-servisna-platforma-s-02}

To odgovara istisnutoj masi vode od približno $998 \cdot 0{,}868 \approx 866\ \text{kg}$, što je u skladu s ukupnom masom platforme i kompresora.

Za pravokutnu platformu s linearnom promjenom gaza po širini bočni pomak centra uzgona glasi

$$
y_B = \frac{b(T_L - T_D)}{12T_m} = \frac{1{,}00\,(0{,}34 - 0{,}22)}{12 \cdot 0{,}28} \approx 0{,}0357\ \text{m}.
$$ {#eq-uzgon-stabilitet-rijeseni-primjer-plutajuca-servisna-platforma-s-03}

Razlika rubnih gazova daje $\tan\varphi=(T_L-T_D)/b=0{,}12$, odnosno $\varphi\approx6{,}84^\circ$. Za pravokutnu istisninu vrijedi

$$
KB=\frac{T_m}{2}=0{,}140\ \text{m},\qquad
BM=\frac{b^2}{12T_m}=0{,}2976\ \text{m}.
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

Momentna ravnoteža maloga nagiba $m_k e=(m_p+m_k)GM\tan\varphi$ sada daje

$$
e=\frac{m_p+m_k}{m_k}\,GM\tan\varphi
=\frac{866}{190}\cdot0{,}2450\cdot0{,}12
\approx0{,}134\ \text{m}.
$$ {#eq-uzgon-stabilitet-rijeseni-primjer-plutajuca-servisna-platforma-s-07}

Povećanje srednjeg gaza nakon postavljanja kompresora uzrokuje samo njegova masa, pa je

$$
\Delta T_m = \frac{m_k}{\rho L b} = \frac{190}{998 \cdot 3{,}10 \cdot 1{,}00} \approx 0{,}0614\ \text{m} \approx 6{,}14\ \text{cm}.
$$ {#eq-uzgon-stabilitet-rijeseni-primjer-plutajuca-servisna-platforma-s-08}

**Provjera i tumačenje**

1. $BM\tan\varphi=0{,}0357\ \text{m}=y_B$ samo je konzistentnost modela, ne neovisna provjera; poluga početnog stabiliteta određena je s $GM$, ne s $BM$. Neovisnu kontrolu daje točan izraz za okomite bokove, @eq-poluga-okomiti-bokovi: $e=\dfrac{m_p+m_k}{m_k}\left(GM+\tfrac12BM\tan^2\varphi\right)\tan\varphi=0{,}1352\ \text{m}$, $0{,}9\ \%$ više od linearnog rezultata — nagib od $6{,}84^\circ$ još je unutar početne teorije.
2. Pomak ukupnoga težišta $(m_k/(m_p+m_k))e\approx0{,}0294\ \text{m}$ jednak je $GM\tan\varphi$, a $e<b/2$, pa je položaj kompresora geometrijski moguć.
:::

::: {#ex-u07-plutajuca-servisna-platforma-na-granici-ulja-i .mf1-ch}
<p class="mf1-box-label">Plutajuća servisna platforma na granici ulja i vode&nbsp;<span class="mf1-level">T4</span></p>

**Tekst zadatka**

Hermetička pravokutna platforma duljine $L = 3{,}00\ \text{m}$, širine $b = 1{,}20\ \text{m}$, visine boka $H = 0{,}34\ \text{m}$ i mase $m_p = 648\ \text{kg}$ nosi ormar mase $m_k = 180\ \text{kg}$ na nepoznatoj bočnoj udaljenosti $e$. Težišta su na visinama $KG_p=0{,}12\ \text{m}$ i $KG_k=0{,}54\ \text{m}$ iznad dna.

Platforma pluta u ulju gustoće $\rho_o = 800\ \text{kg/m}^3$ i debljine $\delta = 0{,}10\ \text{m}$ iznad vode gustoće $\rho_w = 1000\ \text{kg/m}^3$. Gazovi rubova od površine ulja iznose $T_L = 0{,}30\ \text{m}$ i $T_D = 0{,}20\ \text{m}$. Kruto ravno dno i okomiti bokovi daju linearnu promjenu gaza. Primijeni ekvivalentni dvofluidni model za mali nagib; ne provodi se normativna provjera stabiliteta.

**Traži se**

1. Odredi srednji gaz $T_m$ i ukupni istisnuti volumen $V_{ist}$.
2. Odredi koliki se dio istisnine nalazi u ulju, a koliki u vodi.
3. Odredi bočni pomak rezultantnog centra uzgona $y_B$.
4. Odredi ekvivalentne $KB$, $BM$ i $GM$ za zadani dvofluidni model te udaljenost $e$ težišta ormara od osi simetrije platforme.
5. Odredi za koliko je srednji gaz veći nego prije postavljanja ormara.

![Plutajuća platforma na granici ulja i vode](../assets/print/u07_ch1_platforma_ulje_voda_ormar.svg){#fig-u07-plutajuca-platforma-na-granici-ulja-i-vode fig-alt="Plutajuća platforma na granici ulja i vode"}

**Veza s proračunom.** B označuje centar težinjen uzgonskim doprinosima ulja i vode, a ne geometrijski centar ukupnog istisnutog volumena. Gazovi se mjere od površine ulja.

**Rješenje**

Srednji gaz dobiva se iz sredine izmjerenih rubnih gazova:

$$
T_m = \frac{T_L + T_D}{2} = \frac{0{,}30 + 0{,}20}{2} = 0{,}25\ \text{m}.
$$ {#eq-uzgon-stabilitet-cjeloviti-zadatak-plutajuca-servisna-platforma-n-01}

Ukupni istisnuti volumen zato je

$$
V_{ist} = L b T_m = 3{,}00 \cdot 1{,}20 \cdot 0{,}25 = 0{,}900\ \text{m}^3.
$$ {#eq-uzgon-stabilitet-cjeloviti-zadatak-plutajuca-servisna-platforma-n-02}

Kako su oba ruba uronjena više od debljine uljnog sloja $\delta = 0{,}10\ \text{m}$, platforma cijelom tlocrtnom površinom presijeca uljni sloj debljine $\delta$. Zato je volumen istisnine u ulju

$$
V_o = L b \delta = 3{,}00 \cdot 1{,}20 \cdot 0{,}10 = 0{,}360\ \text{m}^3,
$$ {#eq-uzgon-stabilitet-cjeloviti-zadatak-plutajuca-servisna-platforma-n-03}

a volumen istisnine u vodi

$$
V_w = L b (T_m - \delta) = 3{,}00 \cdot 1{,}20 \cdot (0{,}25 - 0{,}10) = 0{,}540\ \text{m}^3.
$$ {#eq-uzgon-stabilitet-cjeloviti-zadatak-plutajuca-servisna-platforma-n-04}

Provjera vertikalne ravnoteže sada glasi

$$
\Delta=\rho_o V_o + \rho_w V_w = 800 \cdot 0{,}360 + 1000 \cdot 0{,}540 = 288 + 540 = 828\ \text{kg},
$$ {#eq-uzgon-stabilitet-cjeloviti-zadatak-plutajuca-servisna-platforma-n-05}

što se točno slaže s ukupnom masom sustava

$$
m_p + m_k = 648 + 180 = 828\ \text{kg}.
$$ {#eq-uzgon-stabilitet-cjeloviti-zadatak-plutajuca-servisna-platforma-n-06}

Dakle, vertikalna ravnoteža je zatvorena.

Za bočni pomak centra uzgona bitan je samo vodeni dio ispod granice fluida, jer je uljni dio simetričan po širini i ne daje bočni moment. Vodene dubine lijevo i desno iznose

$$
\begin{aligned}
T_{w,L} &= T_L - \delta = 0{,}30 - 0{,}10 = 0{,}20\ \text{m}, \\
T_{w,D} &= T_D - \delta = 0{,}20 - 0{,}10 = 0{,}10\ \text{m},
\end{aligned}
$$ {#eq-uzgon-stabilitet-cjeloviti-zadatak-plutajuca-servisna-platforma-n-07}

pa je srednja vodena dubina

$$
T_{w,m} = T_m - \delta = 0{,}15\ \text{m}.
$$ {#eq-uzgon-stabilitet-cjeloviti-zadatak-plutajuca-servisna-platforma-n-08}

Centar uzgona vodenog dijela za linearni nagib pravokutnog presjeka nalazi se na udaljenosti

$$
y_{B,w} = \frac{b(T_{w,L} - T_{w,D})}{12 T_{w,m}} = \frac{1{,}20(0{,}20 - 0{,}10)}{12 \cdot 0{,}15} \approx 0{,}0667\ \text{m}
$$ {#eq-uzgon-stabilitet-cjeloviti-zadatak-plutajuca-servisna-platforma-n-09}

od osi simetrije platforme, prema dublje uronjenoj strani.

Kako je samo vodeni dio asimetričan, rezultantni bočni pomak ukupnog centra uzgona dobiva se težinjenjem po uzgonskim doprinosima:

$$
y_B = \frac{\rho_w V_w}{\rho_o V_o + \rho_w V_w} y_{B,w} = \frac{540}{828} \cdot 0{,}0667 \approx 0{,}0435\ \text{m} \approx 4{,}35\ \text{cm}.
$$ {#eq-uzgon-stabilitet-cjeloviti-zadatak-plutajuca-servisna-platforma-n-10}

Pomak $y_B$ nije poluga stabiliteta, pa se ne smije pisati $(m_p+m_k)g y_B=m_kge$ bez poznavanja vertikalnoga položaja $G$. Neka je $K$ na dnu platforme. Vertikalni položaji centara uzgonskih doprinosa jesu $z_{B,o}=T_m-\delta/2=0{,}20\ \text{m}$ za uljni sloj i $z_{B,w}=(T_m-\delta)/2=0{,}075\ \text{m}$ za vodeni dio. Ekvivalentni $KB$ zato iznosi

$$
KB_{eq}=\frac{\rho_oV_oz_{B,o}+\rho_wV_wz_{B,w}}
{\rho_oV_o+\rho_wV_w}
=\frac{288\cdot0{,}20+540\cdot0{,}075}{828}
\approx0{,}1185\ \text{m}.
$$ {#eq-uzgon-stabilitet-cjeloviti-zadatak-plutajuca-servisna-platforma-n-11}

Prema @eq-metacentarski-radijus-dva-fluida klinovi na površini i na razdjelnici zajedno daju moment $\rho_wI_T\varphi$, pa za $I_T=Lb^3/12=0{,}432\ \text{m}^4$ slijedi

$$
BM_{eq}=\frac{\rho_w I_T}{\rho_oV_o+\rho_wV_w}
=\frac{1000\cdot0{,}432}{828}
\approx0{,}5217\ \text{m}.
$$ {#eq-uzgon-stabilitet-cjeloviti-zadatak-plutajuca-servisna-platforma-n-12}

Konzistentnost modela: $BM_{eq}\tan\varphi=0{,}5217(0{,}10/1{,}20)=0{,}0435\ \text{m}=y_B$, što je identitet po konstrukciji, a ne neovisna provjera. Ukupni položaj težišta jest

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

Budući da je $\tan\varphi=(T_L-T_D)/b=0{,}08333$, ispravna momentna ravnoteža maloga nagiba daje

$$
e=\frac{m_p+m_k}{m_k}\,GM_{eq}\tan\varphi
=\frac{828}{180}\cdot0{,}4289\cdot0{,}08333
\approx0{,}164\ \text{m}=16{,}4\ \text{cm}.
$$ {#eq-uzgon-stabilitet-cjeloviti-zadatak-plutajuca-servisna-platforma-n-15}

Prije postavljanja ormara platforma je bila simetrično opterećena, pa je i tada bila u ravnoteži bez nagiba. Neka je tadašnji srednji gaz $T_0$. Budući da je uljni sloj i dalje potpuno presijecao platformu, vrijedi

$$
\rho_o L b \delta + \rho_w L b (T_0 - \delta) = m_p,
$$ {#eq-uzgon-stabilitet-cjeloviti-zadatak-plutajuca-servisna-platforma-n-16}

odnosno $800 \cdot 3{,}00 \cdot 1{,}20 \cdot 0{,}10 + 1000 \cdot 3{,}00 \cdot 1{,}20 \cdot (T_0 - 0{,}10) = 648$, što daje $288 + 3600(T_0 - 0{,}10) = 648$, pa je

$$
T_0 = 0{,}20\ \text{m}.
$$ {#eq-uzgon-stabilitet-cjeloviti-zadatak-plutajuca-servisna-platforma-n-17}

Povećanje srednjeg gaza nakon postavljanja ormara zato iznosi

$$
\Delta T_m = T_m - T_0 = 0{,}25 - 0{,}20 = 0{,}05\ \text{m} = 5{,}0\ \text{cm}.
$$ {#eq-uzgon-stabilitet-cjeloviti-zadatak-plutajuca-servisna-platforma-n-18}

**Provjera i tumačenje**

Pomak $y_B=4{,}35\ \text{cm}$ zbog $KG\ne KB_{eq}$ nije poluga momenta težine i uzgona. Neovisna kontrola točnim izrazom za okomite bokove (@eq-poluga-okomiti-bokovi) daje $e=0{,}165\ \text{m}$, $0{,}4\ \%$ više od linearnog rezultata, uz nagib $\varphi=4{,}8^\circ$ unutar granice $5^\circ$. Oba ruba presijecaju uljni sloj ($T_D>\delta$), a $e<b/2=0{,}60\ \text{m}$.
:::

::: {#ex-u07-izolirani-puni-bocni-tank-kao-dodana-masa .mf1-ch}
<p class="mf1-box-label">Izolirani puni bočni tank metodom dodane težine: gaz, nagib i početni stabilitet&nbsp;<span class="mf1-level">T4</span></p>

**Tekst zadatka**

Kruti pravokutni trup duljine $L = 80\ \text{m}$, širine $b = 15\ \text{m}$ i visine $H = 8\ \text{m}$ ima početnu masu $m_b = 4000\ \text{t}$. Početno težište leži na osi simetrije, na visini $KG_b = 3{,}0\ \text{m}$ iznad kobilice. More miruje, gustoća mu je $\rho_{mv} = 1025\ \text{kg/m}^3$, a $g = 9{,}81\ \text{m/s}^2$.

Bočni tank u sredini trupa, uz lijevu stijenku, dug je $L_t = 15\ \text{m}$, širok $b_t = 6{,}0\ \text{m}$ i visok $H_t = 3{,}0\ \text{m}$ od kobilice. Napunjen je morem i potpuno izoliran, bez slobodne površine. Primijeni metodu dodane težine: vodu tretiraj kao ukrcanu masu s težištem u centroidu tanka. Vanjska vodonepropusna ovojnica ponovno je uspostavljena: uzgon i vodna linija pripadaju cijelom trupu. Pretpostavi mali bočni nagib. Model ne opisuje otvoreno naplavljivanje, gubitak uzgona ni preživljavanje oštećenja.

**Traži se**

1. Odredi volumen i masu morske vode koja je ušla u tank.
2. Odredi pomak težišta cijelog sustava (brod + voda u tanku): bočni pomak $e_G$ od osi simetrije i novu visinu težišta $KG'$.
3. Odredi novi srednji gaz $T_1$ ako bi brod ostao u uspravnom položaju, te porast gaza $\Delta T = T_1 - T_0$.
4. Odredi metacentarsku visinu $GM$ i donesi zaključak samo o početnom stabilitetu idealiziranoga modela.
5. Odredi ravnotežni kut poprečnog nagiba $\varphi$ (uz pretpostavku malog kuta).
6. Provedi geometrijsku provjeru spuštanja bočnoga ruba palube unutar istoga pravokutnog modela.

![Puni bočni tank u metodi dodane težine: zatvorena voda u tanku pomiče zajedničko težište broda.](../assets/print/u07_ch2_poplavljen_tank.svg){#fig-u07-poplavljen-tank fig-align="center" fig-alt="Puni bočni tank u metodi dodane težine: zatvorena voda u tanku pomiče zajedničko težište broda."}

**Veza s proračunom.** Voda u tanku ulazi u ukrcanu masu i zajedničko težište G; B ostaje centar vanjske istisnine. Skica ne prikazuje $L$, $L_t$, $H$, $H_t$ ni ekscentar tanka $e_t$ (definiran u koraku 2).

**Rješenje**

### 1. Volumen i masa ukrcane vode. {.mf1-step .unnumbered .unlisted}

$$
V_w = L_t b_t H_t = 15 \cdot 6 \cdot 3 = 270\ \text{m}^3,
$$ {#eq-uzgon-stabilitet-cjeloviti-zadatak-izolirani-puni-bocni-tank-kao-01}

$$
m_w = \rho_{mv} V_w = 1025 \cdot 270 \approx 277\,000\ \text{kg} \approx 277\ \text{t}.
$$ {#eq-uzgon-stabilitet-cjeloviti-zadatak-izolirani-puni-bocni-tank-kao-02}

### 2. Pomak težišta sustava. {.mf1-step .unnumbered .unlisted}

Centroid vode u punom tanku nalazi se $b_t/2=3{,}0$ m od lijeve stijenke broda, odnosno $e_t=b/2-b_t/2=4{,}5$ m lijevo od osi simetrije; $e_t$ je ekscentar tanka. Po visini je na $H_t/2=1{,}5$ m iznad kobilice.

Bočni pomak težišta cijelog sustava (ponderirano masom):

$$
e_G = \frac{m_w \cdot e_t}{m_b + m_w} = \frac{277 \cdot 4{,}5}{4000 + 277} = \frac{1247}{4277} \approx 0{,}291\ \text{m}.
$$ {#eq-uzgon-stabilitet-cjeloviti-zadatak-izolirani-puni-bocni-tank-kao-03}

Nova visina težišta sustava iznad kobilice:

$$
KG' = \frac{m_b \cdot KG_b + m_w \cdot (H_t/2)}{m_b + m_w} = \frac{4000 \cdot 3{,}0 + 277 \cdot 1{,}5}{4277} \approx 2{,}90\ \text{m}.
$$ {#eq-uzgon-stabilitet-cjeloviti-zadatak-izolirani-puni-bocni-tank-kao-04}

### 3. Novi gaz (uspravan položaj). {.mf1-step .unnumbered .unlisted}

Brod plovi kad je uzgon jednak ukupnoj težini, tj. istisnina $V_{ist} = (m_b + m_w)/\rho_{mv}$. Za pravokutni trup $V_{ist} = L \cdot b \cdot T$, pa:

$$
T_1 = \frac{m_b + m_w}{\rho_{mv} L b} = \frac{4277 \cdot 10^3}{1025 \cdot 80 \cdot 15} \approx 3{,}478\ \text{m}.
$$ {#eq-uzgon-stabilitet-cjeloviti-zadatak-izolirani-puni-bocni-tank-kao-05}

Početni gaz (samo $m_b$): $T_0 = m_b / (\rho_{mv} L b) = 4000\cdot 10^3 / (1{,}23 \cdot 10^6) \approx 3{,}252\ \text{m}$.

$$
\Delta T = T_1 - T_0 \approx 0{,}226\ \text{m}.
$$ {#eq-uzgon-stabilitet-cjeloviti-zadatak-izolirani-puni-bocni-tank-kao-06}

### 4. Metacentarska visina. {.mf1-step .unnumbered .unlisted}

Drugi moment površine vodne linije za pravokutni presjek:

$$
I_T = \frac{L b^3}{12} = \frac{80 \cdot 15^3}{12} = 22\,500\ \text{m}^4.
$$ {#eq-uzgon-stabilitet-cjeloviti-zadatak-izolirani-puni-bocni-tank-kao-07}

Volumen istisnine:

$$
V_{ist} = \frac{m_b + m_w}{\rho_{mv}} = \frac{4277 \cdot 10^3}{1025} \approx 4172\ \text{m}^3.
$$ {#eq-uzgon-stabilitet-cjeloviti-zadatak-izolirani-puni-bocni-tank-kao-08}

Metacentarski radijus (razmak centra uzgona $B'$ od metacentra $M$):

$$
BM = \frac{I_T}{V_{ist}} = \frac{22\,500}{4172} \approx 5{,}39\ \text{m}.
$$ {#eq-uzgon-stabilitet-cjeloviti-zadatak-izolirani-puni-bocni-tank-kao-09}

Visina centra uzgona iznad kobilice ($T_1/2$):

$$
KB = T_1/2 \approx 1{,}74\ \text{m}.
$$ {#eq-uzgon-stabilitet-cjeloviti-zadatak-izolirani-puni-bocni-tank-kao-10}

Razmak težišta od centra uzgona:

$$
BG = KG' - KB \approx 2{,}90 - 1{,}74 \approx 1{,}16\ \text{m}.
$$ {#eq-uzgon-stabilitet-cjeloviti-zadatak-izolirani-puni-bocni-tank-kao-11}

Metacentarska visina:

$$
GM = BM - BG \approx 5{,}39 - 1{,}16 \approx 4{,}23\ \text{m}.
$$ {#eq-uzgon-stabilitet-cjeloviti-zadatak-izolirani-puni-bocni-tank-kao-12}

Kako je $GM>0$, uspravni položaj ovoga idealiziranog modela dodane težine ima povratni moment pri dovoljno malim nagibima.

### 5. Ravnotežni kut nagiba. {.mf1-step .unnumbered .unlisted}

Za male kutove vrijedi:

$$
\tan\varphi = \frac{e_G}{GM} = \frac{0{,}291}{4{,}23} \approx 0{,}0689 \quad \Rightarrow \quad \varphi \approx 3{,}94^\circ.
$$ {#eq-uzgon-stabilitet-cjeloviti-zadatak-izolirani-puni-bocni-tank-kao-13}

### 6. Provjera bočnog ruba palube. {.mf1-step .unnumbered .unlisted}

Nadvođe pri uspravnom položaju s novim gazom:

$$
f = H - T_1 \approx 8 - 3{,}478 \approx 4{,}52\ \text{m}.
$$ {#eq-uzgon-stabilitet-cjeloviti-zadatak-izolirani-puni-bocni-tank-kao-14}

Spuštanje lijevog ruba palube zbog nagiba:

$$
\Delta z = (b/2) \sin\varphi \approx 7{,}5 \cdot \sin 3{,}94^\circ \approx 7{,}5 \cdot 0{,}0687 \approx 0{,}515\ \text{m}.
$$ {#eq-uzgon-stabilitet-cjeloviti-zadatak-izolirani-puni-bocni-tank-kao-15}

Preostalo nadvođe na lijevom rubu palube:

$$
f_L = f - \Delta z \approx 4{,}52 - 0{,}52 \approx 4{,}00\ \text{m}.
$$ {#eq-uzgon-stabilitet-cjeloviti-zadatak-izolirani-puni-bocni-tank-kao-16}

Granični kut pri kojem rub palube dotakne morsku razinu slijedi iz uvjeta $f\cos\varphi=(b/2)\sin\varphi$, jer se trup s okomitim bokovima pri stalnoj istisnini okreće oko sredine vodne linije:

$$
\tan\varphi_{lim} = \frac{2f}{b} = \frac{2\cdot4{,}52}{15} \approx 0{,}603, \qquad \varphi_{lim} \approx 31{,}1^\circ.
$$ {#eq-uzgon-stabilitet-cjeloviti-zadatak-izolirani-puni-bocni-tank-kao-17}

Vrijednost $31{,}1^\circ$ samo je geometrijska ekstrapolacija krutoga pravokutnika koji se zakreće oko uspravnoga položaja. Pri tako velikom kutu metacentarska aproksimacija za male kutove više nije dostatna, a stvarnu uronjenost ruba i kut naplavljivanja treba dobiti ponovnim određivanjem vodne linije, centra uzgona i stvarnih otvora za svaki kut.

**Provjera i tumačenje**

1. Bilanca: $\Delta T=m_w/(\rho_{mv}Lb)\approx0{,}226\ \text{m}$ i $e_G=GM\tan\varphi$ zatvaraju vertikalnu i momentnu ravnotežu; nagib od oko $4^\circ$ ostavlja približno $4\ \text{m}$ nadvođa na nižem rubu.
2. To je početna ravnoteža idealiziranoga trupa metodom dodane težine. Oštećeni stabilitet može zahtijevati metodu izgubljenoga uzgona, propusnosti prostora, progresivno naplavljivanje i probabilističke scenarije; ništa od toga nije sadržano ovdje. Da tank nije pun, slobodna površina smanjila bi $GM$ (blok „Učinak slobodne površine u tanku”).
:::

::: {#ex-u07-plutajuci-vjetroagregat-tipa-cilindricne-plovne-osnove-t3 .mf1-we}
<p class="mf1-box-label">Plutajući vjetroagregat tipa cilindrične plovne osnove &nbsp;<span class="mf1-level">T3</span></p>

**Tekst zadatka**

Vertikalna cilindrična plovna osnova (spar) promjera $D = 12{,}0\ \text{m}$ i duljine $H = 100\ \text{m}$ nosi vjetroagregat iznad mora. Ukupna masa sustava s čvrstim balastom u dnu iznosi $m_{uk} = 9\,000\ \text{t} = 9{,}00 \cdot 10^6\ \text{kg}$, a gustoća mora $\rho_{mv} = 1\,025\ \text{kg/m}^3$. Promatraj mirnu vodu bez vjetra i valova; vodna linija je kružna.

**Traži se**

1. Odredi površinu poprečnog presjeka i istisnuti volumen u ravnoteži.
2. Odredi gaz $T$ i nadvođe $f$ plovne osnove te promjenu gaza za $\pm5\,\%$ mase.
3. Odredi $KB$, $BM$ i $KM$ te uvjet za visinu težišta $KG$. Obrazloži koji član daje stabilitet ove plovne osnove i zašto balast mora biti u dnu.

**Rješenje**

### 1. Presjek i istisnina. {.mf1-step .unnumbered .unlisted}

$$
A = \frac{\pi D^2}{4} = \frac{\pi \cdot 12{,}0^2}{4} \approx 113{,}1\ \text{m}^2,\qquad
V_{ist} = \frac{m_{uk}}{\rho_{mv}} = \frac{9{,}00 \cdot 10^6}{1\,025} \approx 8\,780\ \text{m}^3.
$$ {#eq-uzgon-stabilitet-rijeseni-primjer-plutajuci-vjetroagregat-tipa-ci-01}

### 2. Gaz i nadvođe. {.mf1-step .unnumbered .unlisted}

$$
T = \frac{V_{ist}}{A} = \frac{8\,780}{113{,}1} \approx 77{,}6\ \text{m},\qquad
f = H - T = 100 - 77{,}6 \approx 22{,}4\ \text{m}.
$$ {#eq-uzgon-stabilitet-rijeseni-primjer-plutajuci-vjetroagregat-tipa-ci-02}

Promjena mase za $\pm 5\,\%$ (naslage i led, odnosno ispuštanje balasta) mijenja gaz linearno:

$$
T_{+5\%} \approx 1{,}05 \cdot 77{,}6 \approx 81{,}5\ \text{m}, \qquad
T_{-5\%} \approx 73{,}8\ \text{m}.
$$ {#eq-uzgon-stabilitet-rijeseni-primjer-plutajuci-vjetroagregat-tipa-ci-03}

### 3. Metacentar i uvjet za težište. {.mf1-step .unnumbered .unlisted}

Za uspravni valjak centar uzgona je na polovici gaza, a drugi moment kružne vodne linije iznosi $I_T=\pi D^4/64$:

$$
\begin{aligned}
KB &= \frac{T}{2} \approx 38{,}8\ \text{m}, \\
BM &= \frac{I_T}{V_{ist}} = \frac{\pi \cdot 12{,}0^4/64}{8\,780} = \frac{1\,018}{8\,780} \approx 0{,}116\ \text{m}, \\
KM &= KB + BM \approx 38{,}9\ \text{m}.
\end{aligned}
$$ {#eq-uzgon-stabilitet-rijeseni-primjer-plutajuci-vjetroagregat-tipa-ci-04}

Početni stabilitet zahtijeva $GM=KM-KG>0$, dakle $KG<38{,}9\ \text{m}$. Budući da je $BM$ zanemariv prema $KB$, uvjet se praktički svodi na $KG<KB$: težište mora ležati ispod centra uzgona. Gondola i rotor nalaze se oko $100\ \text{m}$ iznad kobilice, pa bez balasta težište sustava leži visoko (npr. $KG=45\ \text{m}$ daje $GM\approx-6{,}1\ \text{m}$). Čvrsti balast u dnu spušta $KG$: uz $KG=32\ \text{m}$ dobiva se $GM\approx6{,}9\ \text{m}$.

$$
\begin{aligned}
GM(KG=45\ \text{m})&\approx38{,}9-45=-6{,}1\ \text{m}, \\
GM(KG=32\ \text{m})&\approx38{,}9-32=6{,}9\ \text{m}.
\end{aligned}
$$ {#eq-uzgon-stabilitet-rijeseni-primjer-plutajuci-vjetroagregat-tipa-ci-05}

**Provjera i tumačenje**

Gaz od oko $78\ \text{m}$ i nadvođe od oko $22\ \text{m}$ odgovaraju redu veličine izvedenih plovnih osnova tipa spar. Izbor modela: kod pontona stabilitet daje široka vodna linija (velik $BM$), a kod spara uska vodna linija ne daje gotovo ništa ($BM\approx0{,}1\ \text{m}$) i cijeli stabilitet dolazi iz razmaka $KB-KG$, kao kod njihala. Zato spar bez balasta nije stabilan ni u mirnoj vodi. Za stvarnu plovnu osnovu treba još krivulja $GZ$, hidrodinamički odziv, sidrenje i konstrukcijska opterećenja.
:::

::: {.mf1-samoprovjera}
<p class="mf1-box-label">Provjeri sebe</p>

1. Što govori Arhimedov zakon o ovisnosti sile uzgona o materijalu i obliku tijela?

::: {.callout-note collapse="true"}
### Odgovor
U zadanom jednolikom gravitacijskom polju sila uzgona ovisi o istisnutom volumenu i gustoći fluida, a ne izravno o materijalu, masi ni unutarnjoj građi tijela. Tijela jednakoga istisnutog volumena u istom fluidu imaju jednak uzgon; za šuplje tijelo važno je može li fluid prodrijeti u njegovu unutrašnjost.
:::

2. Dva pontona imaju jednak $GM$, ali jedan ima velik $BM$ i visok $KG$, a drugi malen $BM$ i nizak $KG$. Hoće li jednako reagirati na isti pomak tereta?

::: {.callout-note collapse="true"}
### Odgovor
Pri vrlo malim kutovima da: nagib slijedi iz $m_ke=\Delta GM\tan\varphi$ i ovisi samo o $GM$. Pri većem kutu razlikuju se: član $\tfrac12BM\tan^2\varphi$ brže povećava polugu pontona s velikim $BM$, a gubitak nadvođa i uronjenje ruba palube nastupaju pri različitim kutovima. Jednak $GM$ jamči samo jednak početni odziv.
:::

3. Kako se mijenja gaz istog broda pri prelasku iz slatke u slanu vodu?

::: {.callout-note collapse="true"}
### Odgovor
Gustoća slane vode veća je od gustoće slatke vode, pa je za istu masu broda potreban manji istisnuti volumen i brod u slanoj vodi plovi s manjim gazom. Dopuštena masa tereta ipak se ne određuje samo gustoćom trenutačne vode, nego linijama opterećenja, uvjetima plovidbe, čvrstoćom i stabilnošću; iz Arhimedova zakona samoga ne slijedi dopuštenje za ukrcaj dodatnoga tereta.
:::

4. Vrijedi li Arhimedov zakon i u uljnom ili plinskom fluidu, ili samo u vodi?

::: {.callout-note collapse="true"}
### Odgovor
Vrijedi u bilo kojem fluidu, uključujući plinove. U zraku sila uzgona obično je mala zbog male gustoće zraka, ali treba je uračunati za balone, dirižable i precizna mjerenja mase u zraku. U idealnom vakuumu nema fluida ni uzgona. U uljnim sustavima Arhimedov zakon koristi se pri proračunu uzgona kliznih elemenata i u višefaznim separatorima.
:::
:::

## Zadaci za vježbu

U svim zadatcima uzmi $g=9{,}81\ \text{m/s}^2$. Plovci su nepropusni, fluidi miruju, a uzgon i težina označuju sile na promatrano tijelo.

::::: {.mf1-vjezbe-list}

### Uzgon potpuno uronjenog tijela {#task-u07-hermeticki-zatvoreno-tijelo-volumena-i-mase-potpuno .unnumbered .unlisted}

**Tekst zadatka**

Hermetički zatvoreno tijelo volumena $V = 0{,}085\ \text{m}^3$ i mase $m = 62\ \text{kg}$ potpuno je uronjeno u vodu gustoće $\rho = 998\ \text{kg/m}^3$.

**Traži se**

Odredi silu uzgona i silu koju treba primijeniti da tijelo ostane potpuno uronjeno i u mirovanju.

:::: {.content-visible .mf1-hint-online when-format="html"}
::: {.callout-note collapse="true" data-hint-key="true"}
### Naputak
Uzgon je $F_U = \rho gV$; potom usporedi $F_U$ i težinu $F_G = mg$ da dobiješ potrebnu dodatnu silu.
:::
::::
:::: {.content-visible .mf1-answer-online when-format="html"}
::: {.callout-tip collapse="true" data-answer-key="true"}
### Kontrolni rezultat

$F_U \approx 832\ \text{N}$; kako je $F_U > F_G = 608\ \text{N}$, treba dodatna sila prema dolje $\approx 224\ \text{N}$.
:::
::::

[Razina: T1]{.mf1-task-level}

### Gaz opterećenog pontona {#task-u07-pravokutni-radni-ponton-duljine-sirine-i-visine .unnumbered .unlisted}

**Tekst zadatka**

Pravokutni radni ponton duljine $L = 2{,}60\ \text{m}$, širine $b = 1{,}40\ \text{m}$ i visine boka $H = 0{,}38\ \text{m}$ ima vlastitu masu $m_p = 510\ \text{kg}$. Na njega se simetrično postavlja teret mase $m_t = 220\ \text{kg}$. Ponton pluta u vodi gustoće $\rho = 998\ \text{kg/m}^3$. To je geometrijska granica uspravnog modela, ne dopuštenje za ukrcaj toga tereta.

**Traži se**

Odredi istisnuti volumen, srednji gaz i preostalu dodatnu masu koju ponton može primiti prije nego što rub boka dođe do razine vode.

:::: {.content-visible .mf1-hint-online when-format="html"}
::: {.callout-note collapse="true" data-hint-key="true"}
### Naputak
Iz vertikalne ravnoteže vrijedi $\rho gV_{ist} = (m_p + m_t)g$; srednji gaz slijedi iz $V_{ist} = LbT$.
:::
::::
:::: {.content-visible .mf1-answer-online when-format="html"}
::: {.callout-tip collapse="true" data-answer-key="true"}
### Kontrolni rezultat

$V_{ist} \approx 0{,}73\ \text{m}^3$; srednji gaz $T \approx 0{,}20\ \text{m}$; dodatna masa do ruba $\approx 650\ \text{kg}$.
:::
::::

[Razina: T1]{.mf1-task-level}

<span id="task-u07-plutajuca-servisna-platforma-duljine-i-sirine-ima"></span>

### Metacentarska visina iz pokusa nagibanja {#task-metacentarska-visina-iz-pokusa-nagibanja .unnumbered .unlisted}

**Tekst zadatka**

Zatvoreni pravokutni ponton, balastiran u dnu, u mirnoj vodi stoji uspravno, s utegom na osi simetrije. Duljina je $L=3{,}00\ \text{m}$, širina $b=1{,}40\ \text{m}$ i visina boka $H=0{,}50\ \text{m}$. Ukupna masa, uključujući uteg, iznosi $m=1200\ \text{kg}$, a gustoća vode $\rho=998\ \text{kg/m}^3$.

Uteg mase $m_s=120\ \text{kg}$ pomakne se vodoravno $e=0{,}30\ \text{m}$ udesno, bez promjene svoje visine. Izmjeren je nagib $\varphi=3{,}00^\circ$ udesno. Zanemari mjernu nesigurnost. Zadana granica početnog modela jest $|\varphi|\le5^\circ$; nije univerzalna granica stabilnosti.

**Traži se**

1. Odredi srednji gaz, $GM$ iz pokusa i ukupni $KG$.
2. Provjeri da je desni rub dublje uronjen, da dno ostaje potpuno uronjeno i da paluba ostaje iznad vode.

:::: {.content-visible .mf1-hint-online when-format="html"}
::: {.callout-note collapse="true" data-hint-key="true"}
### Naputak
Iz momentne ravnoteže $m_s e=mGM\tan\varphi$ najprije odredi izmjereni $GM$. Zatim primijeni $KG=KB+BM-GM$, uz $KB=T_m/2$ i $BM=b^2/(12T_m)$. U linearnom modelu rubni gazovi su $T_m\pm(b/2)\tan\varphi$.
:::
::::
:::: {.content-visible .mf1-answer-online when-format="html"}
::: {.callout-tip collapse="true" data-answer-key="true"}
### Kontrolni rezultat

$T_m=0{,}2863\ \text{m}$; $GM=0{,}5724\ \text{m}$; $KG=0{,}1412\ \text{m}$. Gazovi su $T_L=0{,}2496\ \text{m}$ i $T_D=0{,}3230\ \text{m}$: oba su između $0$ i $H$. Kut $3^\circ<5^\circ$ zadovoljava zadani kriterij; pozitivan $GM$ dokazuje samo početni stabilitet.
:::
::::

[Razina: T2]{.mf1-task-level}

### Gustoća ulja iz očitanja areometra {#task-u07-areometar-mase-s-cilindricnim-vratom-promjera-pluta .unnumbered .unlisted}

**Tekst zadatka**

Areometar mase $m = 0{,}085\ \text{kg}$ s cilindričnim vratom promjera $d = 8\ \text{mm}$ pluta u referentnoj vodi gustoće $\rho_w=1000\ \text{kg/m}^3$ tako da je uronjena duljina cilindričnog vrata $h_1 = 82\ \text{mm}$, a u nepoznatom ulju $h_2 = 95\ \text{mm}$. Obje duljine mjere se od istog spoja vrata s potpuno uronjenim tijelom areometra do slobodne površine. Zanemari kapilarne sile.

**Traži se**

Odredi gustoću ulja i protumači zašto je uron u ulju veći nego u vodi.

:::: {.content-visible .mf1-hint-online when-format="html"}
::: {.callout-note collapse="true" data-hint-key="true"}
### Naputak
U oba fluida vrijedi $\rho gV_{ist} = mg$; razlika je samo u uronjenom volumenu vrata i tijela areometra.
:::
::::
:::: {.content-visible .mf1-answer-online when-format="html"}
::: {.callout-tip collapse="true" data-answer-key="true"}
### Kontrolni rezultat

$\rho_o \approx 992{,}4\ \text{kg/m}^3$; uron je veći jer ulje ima manju gustoću pa je za istu težinu potreban veći istisnuti volumen.
:::
::::

[Razina: T2]{.mf1-task-level}

<span id="task-u07-plutajuci-modul-istiskuje-volumen-vode-i-ima"></span>

### Spuštanje opreme ili dodavanje balasta {#task-spustanje-opreme-ili-dodavanje-balasta .unnumbered .unlisted}

**Tekst zadatka**

Za zatvoreni pravokutni ponton s nadgrađem i visoko postavljenom opremom razmotri dva zasebna plana povećanja početnog stabiliteta. Oprema i balast postavljaju se simetrično; ponton miruje uspravno. Ponton ima $L=3{,}00\ \text{m}$, $b=1{,}50\ \text{m}$, visinu boka $H=0{,}60\ \text{m}$, početnu ukupnu masu $m_0=1000\ \text{kg}$ i $KG_0=0{,}80\ \text{m}$; gustoća vode je $\rho=998\ \text{kg/m}^3$.

Plan A spušta postojeću opremu mase $150\ \text{kg}$ s visine $1{,}10\ \text{m}$ na $0{,}30\ \text{m}$ iznad dna. Plan B zadržava tu opremu i dodaje $600\ \text{kg}$ čvrstog balasta s težištem na $0{,}05\ \text{m}$ iznad dna. Vanjska geometrija pontona ostaje ista; nema djelomično punih tankova. Prihvati samo plan koji istodobno daje $GM\ge0{,}20\ \text{m}$ i nadvođe najmanje $0{,}25\ \text{m}$.

Navedeni su uvjeti nastavnog modela, a ne propisana provjera plovila.

**Traži se**

1. Odaberi potrebne bilance i za početno stanje te svaki plan odredi gaz, nadvođe, $KG$ i $GM$.
2. Objasni zašto niže težište samo po sebi ne jamči prihvatljiv plan.

:::: {.content-visible .mf1-hint-online when-format="html"}
::: {.callout-note collapse="true" data-hint-key="true"}
### Naputak
Za svaki plan ponovno zatvori ukupnu masu i njezin vertikalni moment. Spuštanje opreme čuva masu; dodani balast mijenja i istisninu, $KB$ i $BM$. Dva uvjeta provjeri zasebno.
:::
::::
:::: {.content-visible .mf1-answer-online when-format="html"}
::: {.callout-tip collapse="true" data-answer-key="true"}
### Kontrolni rezultat

Početno: $(T,f,KG,GM)=(0{,}2227;0{,}3773;0{,}8000;0{,}1534)\ \text{m}$. Plan A: $(0{,}2227;0{,}3773;0{,}6800;0{,}2734)\ \text{m}$, prihvatljiv. Plan B: $(0{,}3563;0{,}2437;0{,}5188;0{,}1857)\ \text{m}$, ne zadovoljava oba uvjeta. Balast snižava $KG$, ali smanjuje i $BM$ te nadvođe $f=H-T$.
:::
::::

[Razina: T3]{.mf1-task-level}

### Platforma na granici ulja i vode {#task-u07-pravokutna-servisna-platforma-duljine-i-sirine-pluta .unnumbered .unlisted}

**Tekst zadatka**

Pravokutna servisna platforma duljine $L = 2{,}80\ \text{m}$ i širine $b = 1{,}20\ \text{m}$ pluta na granici ulja gustoće $\rho_o = 820\ \text{kg/m}^3$ debljine $\delta = 0{,}08\ \text{m}$ i vode gustoće $\rho_w = 998\ \text{kg/m}^3$. Nakon pomaka akumulatora lijevi rub uronjen je $T_L = 0{,}26\ \text{m}$, a desni $T_D = 0{,}18\ \text{m}$. Akumulator ima $m_a=70\ \text{kg}$, a ukupno težište nalazi se na $KG=0{,}200\ \text{m}$ iznad dna.

Rubni gazovi imaju zadane granice pogreške $\pm3\ \text{mm}$, vrijedi $\rho_w=998\pm3\ \text{kg/m}^3$, $m_a=70\pm1\ \text{kg}$ i $KG=0{,}200\pm0{,}005\ \text{m}$; navedeni intervali su zajamčene granice, ne standardne nesigurnosti. Visina boka je $H=0{,}36\ \text{m}$; ostale podatke uzmi kao točne.

Zadana granica modela jest $|\varphi|\le5^\circ$, a montažni koridor dopušta udaljenost akumulatora najviše $0{,}34\ \text{m}$ od osi.

**Traži se**

1. Ukupnu masu platforme s opremom procijeni iz izmjerene istisnine u svakom računu. Odredi srednji gaz, volumene istisnine u ulju i vodi, bočni pomak rezultantnoga centra uzgona, ekvivalentne $KB$, $BM$ i $GM$ te udaljenost akumulatora od osi simetrije.
2. Provjeri da oba ruba presijecaju cijeli sloj ulja, ostaju ispod palube i zadovoljavaju granicu nagiba.
3. Konzervativno procijeni najveću moguću udaljenost akumulatora provjerom rubnih kombinacija ulaza i odluči stane li u zadani montažni koridor.

:::: {.content-visible .mf1-hint-online when-format="html"}
::: {.callout-note collapse="true" data-hint-key="true"}
### Naputak
Najprije uzmi $T_m=(T_L+T_D)/2$ i $\Delta=\rho_oV_o+\rho_wV_w$. Za položaje uzgonskih doprinosa vrijedi $z_{B,o}=T_m-\delta/2$ i $z_{B,w}=(T_m-\delta)/2$, pa izračunaj $KB_{eq}$ njihovim uzgonskim težinjenjem. U ovom modelu $BM_{eq}=\rho_w I_T/\Delta$, gdje je $I_T=Lb^3/12$, a $GM_{eq}=KB_{eq}+BM_{eq}-KG$. Tek zatim primijeni $m_a e=\Delta GM_{eq}\tan\varphi$ i $\tan\varphi=(T_L-T_D)/b$. Za konzervativni omotač izračunaj svih $2^5=32$ rubnih kombinacija pet nesigurnih skalarnih ulaza.
:::
::::
:::: {.content-visible .mf1-answer-online when-format="html"}
::: {.callout-tip collapse="true" data-answer-key="true"}
### Kontrolni rezultat

$T_m=0{,}220\ \text{m}$; $(V_o,V_w)=(0{,}269;0{,}470)\ \text{m}^3$; $\Delta=689{,}9\ \text{kg}$; $y_B=0{,}0389\ \text{m}$. $(KB_{eq},BM_{eq},GM_{eq})=(0{,}105;0{,}583;0{,}488)\ \text{m}$. $e=0{,}321\ \text{m}$ ulijevo; $e_{max}=0{,}3546\ \text{m}>0{,}34\ \text{m}$: raspored se ne prihvaća. Sve rubne kombinacije imaju $\delta<T_L,T_D<H$ i $|\varphi|<5^\circ$.
:::
::::

[Razina: T4]{.mf1-task-level}

:::::

![Skice uz zadatke za vježbu — pontoni, areometri i plutajuće platforme.](../assets/print/u07_vjezbe_skice.svg){#fig-u07-vjezbe fig-align="center" fig-alt="Skice uz zadatke za vježbu — pontoni, areometri i plutajuće platforme."}

**Napomene uz skice.** $F_G$ je težina tijela ili cijelog sklopa (točka $G$ je težište), $F_U$ uzgon kroz centar uzgona $B$, a $F_d$ tražena dodatna sila držanja u Z1; ona nije nacrtana, a $F_U$ i $F_G$ u Z1 imaju jednake shematske duljine. U Z2, Z3 i Z5 vodna linija nacrtana je shematski, a ne u mjerilu traženih gazova (oznake s „?”); u Z6 položaj akumulatora nije u mjerilu tražene udaljenosti $e$, a centar uzgona nije nacrtan jer se traži. Dvostrane strelice označuju kote. U Z3 pomični uteg već je uključen u ukupnu masu. U Z4 uroni $h_1$ i $h_2$ mjere se od spoja vrata s tijelom areometra. U Z5 presjek A prikazuje spuštenu opremu, a presjek B dodani čvrsti balast.


::: {.mf1-zavrsni-okvir}
<p class="mf1-box-label">Za ponijeti iz poglavlja</p>

**Sažeta provjera prije računa**

- Srednji gaz dolazi iz ukupne težine, a nagib iz ravnoteže momenata.
- Iz rubnih gazova najprije se dobiva $\tan\varphi$; za položaj tereta zatim trebaju $KB$, $BM$, $KG$ i $GM$.
- Za težinu i centar uzgona rabi se isti koordinatni smjer; predznak momenta mora odgovarati strani pomaknutog tereta.
- Dobiveni pomak tereta mora biti geometrijski moguć, a nagib unutar granice početne teorije.
- Slobodna površina u djelomično punom tanku smanjuje $GM$.

**Najčešća pogreška**

Izjednačiti geometrijski pomak centra uzgona $y_B=BM\tan\varphi$ s polugom stabiliteta: položaj tereta slijedi tek iz $m_k e=\Delta GM\tan\varphi$, nakon što je poznat $KG$.

**Nakon ovoga poglavlja mora biti moguće**

1. povezati Arhimedov zakon sa stvarnim istisnutim volumenom;
2. odvojiti ravnotežu vertikalnih sila od ravnoteže momenata plivajućeg tijela;
3. izračunati $GM=KB+BM-KG$ i iz nagiba odrediti pomak tereta, bez pretpostavke $BG=0$;
4. procijeniti granicu malog kuta i prepoznati kada treba krivulja $GZ$.
:::
