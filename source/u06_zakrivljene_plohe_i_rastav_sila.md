![Pregled poglavlja: Zakrivljene plohe i rastav sila](../assets/print/u06_fig_uvod_pregled.svg){#fig-uvod-u06 fig-align="center" style="width:100%;max-width:980px;"}

## Zakrivljena ploha — nova geometrija razlaganja sile

Na zakrivljenoj stijenci fizika tlaka ostaje ista, ali geometrija sile postaje složenija.

Poglavlje zato ne uvodi novu fiziku, nego dvije stabilne radne navike: horizontalna komponenta sile čita se preko projekcije, a vertikalna preko težine zamišljenog volumena fluida.

::: {.mf1-application}
<p class="mf1-box-label">Inženjerski kontekst</p>

Zakrivljene površine pojavljuju se na segmentnim ustavama, zaobljenim poklopcima spremnika, procesnim revizijskim otvorima i brodskim oplatama koje ne rade s ravnom stijenkom. U takvim sklopovima rezultat ne daje jedna zapamćena formula, nego rastav na projekciju i volumen, jer se tek tada može ispravno pročitati što opterećuje nosač vodoravno, a što ga gura ili rasterećuje okomito.
:::

::: {.mf1-priprema}
<p class="mf1-box-label">Prije čitanja poglavlja</p>

**Predznanje koje se pretpostavlja:**

- sila na uronjenu ravnu plohu iz poglavlja <span class="mf1-ch-ref"><span class="mf1-ch-code">U05</span><span class="mf1-ch-title">Hidrostatske sile na ravne plohe</span></span>;
- vektorska analiza, projekcije vektora na koordinatne osi;
- integracija po krivuljama i plohama, pojam težišta volumena;
- osnove statike krutog tijela.

**Ishodi učenja:**

- rastaviti hidrostatičku silu na zakrivljenu plohu na horizontalnu i vertikalnu komponentu;
- odrediti horizontalnu komponentu preko sile na vertikalnu projekciju plohe;
- odrediti vertikalnu komponentu preko težine imaginarnog volumena fluida između plohe i slobodne površine;
- ispravno utvrditi smjer vertikalne komponente (prema gore ili prema dolje).

**Procijenjeno vrijeme:** 5–6 sati za teoriju i izvode, 4 sata za rješavanje primjera i zadataka.
:::

## Fizikalni uvod i matematički izvod

Na zakrivljenoj plohi tlak i dalje djeluje okomito na svaki lokalni element površine, ali rezultantu više nije praktično tražiti izravno integracijom po svim smjerovima. Zato se sila rastavlja na dvije komponente:

$$F_H = \rho g A_x h_{Cx}$$

::: {.callout-note}
## Fizikalno značenje
Horizontalna komponenta sile na zakrivljenu plohu jednaka je sili na zamišljenu ravnu (vertikalnu) plohu iste projekcije. Zakrivljenost plohe horizontalnu silu ne mijenja — ona ovisi samo o tome koliko je „široka" sjena plohe u vodoravnom smjeru i na kojoj je dubini njezino težište. Intuitivno: zakrivljenost preraspoređuje smjer lokalnih sila, ali ne mijenja ukupnu vodoravnu komponentu.
:::

gdje je $A_x$ vertikalna projekcija zakrivljene površine, a $h_{Cx}$ dubina težišta te projekcije, te

$$F_V = \rho gV^*$$

::: {.callout-note}
## Fizikalno značenje
Vertikalna komponenta sile na zakrivljenu plohu jednaka je težini imaginarnog volumena fluida između plohe i slobodne površine. Taj volumen ne mora biti fizički ispunjen fluidom — može biti prazni prostor ili dio iznad slobodne površine. Ključno je da volumen definira koliki bi bio vertikalni tlačni teret da je taj prostor ispunjen fluidom do slobodne površine. Smjer ($\uparrow$ ili $\downarrow$) ovisi o tome je li taj zamišljeni stupac fluida ispod ili iznad plohe.
:::

gdje je $V^*$ volumen fluida između zakrivljene površine i slobodne površine.

::: {.mf1-interaktivno}
<p class="mf1-box-label">Interaktivni prikaz — Sila na zakrivljenu plohu</p>

Interaktivni prikaz omogućuje mijenjanje polumjera krivulje, dubine vrha i širine plohe (četvrtina kruga uronjena u vodu) uz neposredno praćenje horizontalne i vertikalne komponente sile te rezultante s pripadnim kutom. Vektori sila pomažu intuitivno razumijevanje smjera djelovanja.

<div class="mf1-interaktivno-akcija">
<a class="mf1-interaktivno-veza" href="https://colab.research.google.com/github/martibasic/MF1_udzbenik/blob/main/notebooks/u06_zakrivljena_ploha.ipynb" target="_blank" rel="noopener">Otvori interaktivni prikaz</a>
<img class="mf1-interaktivno-qr" src="../assets/qr/u06_zakrivljena_ploha.svg" alt="QR kod za interaktivni prikaz sile na zakrivljenu plohu"/>
</div>

<div class="mf1-interaktivno-pitanja">
**Pitanja za samostalno istraživanje:** (a) Kako se omjer $F_V/F_H$ mijenja kada dubina vrha $h_t$ teži k nuli? (b) Što se događa s istim omjerom pri velikim dubinama ($h_t \gg R$)? (c) Pri kojoj kombinaciji $R$ i $h_t$ rezultanta sile prolazi kroz središte krivulje?
</div>
:::

Najvažniji detalj nije sama formula, nego znak komponente $F_V$. Ako je zamišljeni volumen ispod slobodne površine, vertikalna komponenta tipično djeluje prema gore. Ako je dio tog volumena iznad slobodne površine, pojavljuje se podtlačni doprinos i $F_V$ može djelovati prema dolje. Matematika time razdvaja ono što geometrija na prvi pogled miješa: projekcija daje vodoravnu sliku opterećenja, a zamišljeni volumen njegov vertikalni smisao.

## Matematički izvod

Na lokalnom elementu zakrivljene plohe površine $dA$ tlak djeluje okomito na plohu, pa je elementarna sila

$$
dF = p\,dA.
$$

Ako normala na plohu zatvara kut $\varphi$ s vodoravnicom, horizontalna komponenta elementarne sile iznosi

$$
dF_H = dF\cos\varphi = p\,dA\cos\varphi.
$$

Kako je $dA\cos\varphi = dA_x$, odnosno upravo vertikalna projekcija lokalnoga elementa, slijedi

$$
F_H = \int p\,dA_x.
$$

Time horizontalna komponenta poprima isti matematički oblik kao sila na ravnu vertikalnu plohu projekcije $A_x$:

$$
F_H = \rho g A_x h_{Cx}.
$$

Vertikalnu komponentu nije najčišće čitati preko lokalnih kutova, nego preko ravnoteže zamišljenoga volumena fluida iznad ili ispod zakrivljene plohe. Za taj imaginarni fluidni blok vertikalna ravnoteža pokazuje da vertikalna komponenta hidrostatske sile mora biti jednaka težini tog volumena:

$$
F_V = \rho gV^*.
$$

Ovdje je $V^*$ volumen između zakrivljene plohe i slobodne površine, odnosno između plohe i zamišljene zatvarajuće plohe kad je tlak iznad fluida drugačiji od atmosferskoga. To je drugi temeljni rezultat: vertikalna komponenta nije posljedica projekcije nego težine zamišljenoga stupca fluida koji bi "sjedio" na zakrivljenoj plohi.

Jednako je važno znati i gdje te komponente djeluju. Horizontalna komponenta ima isti pravac djelovanja kao sila na vertikalnu projekciju zakrivljene plohe, pa se njezino hvatište dobiva kao centar tlaka te projekcije. Vertikalna komponenta prolazi kroz težište zamišljenoga volumena $V^*$, jer po ulozi odgovara njegovoj težini. Tek nakon toga komponente se smiju spojiti u jednu rezultantu i uključiti u momentnu ravnotežu poklopca, brane ili zatvarača.

Predznak komponente $F_V$ nosi puni fizikalni smisao zadatka. Ako zamišljeni volumen fluida doista leži iznad plohe, vertikalna komponenta najčešće djeluje prema gore. Ako geometrija ili tlakovi iznad plohe mijenjaju raspored zamišljenoga volumena, ista komponenta može djelovati i prema dolje. Nakon što su određene obje komponente, rezultanta se dobiva iz vektorskoga zbroja

$$
F_R = \sqrt{F_H^2 + F_V^2},
$$

a smjer rezultante određuje se iz odgovarajućeg omjera $F_V/F_H$. Ako je ploha dio cilindrične površine, pravac djelovanja rezultante dodatno prolazi središtem zakrivljenosti, što je često presudan geometrijski podatak za momentnu ravnotežu zatvarača i poklopaca.

::: {.callout-note}
## Razrada koraka
Korak: od $dF = p\,dA$ → rastav na $F_H = \rho g A_x h_{Cx}$ i $F_V = \rho g V^*$

Elementarna sila $dF = p\,dA$ djeluje okomito na element zakrivljene plohe. Ako normala tog elementa zatvara kut $\varphi$ s vodoravnicom:
$$
dF_H = dF\cos\varphi = p\,dA\cos\varphi = p\,dA_x,
$$
jer je $dA_x = dA\cos\varphi$ upravo vertikalna projekcija elementa. Integriranjem:
$$
F_H = \int p\,dA_x = \int \rho g y\,dA_x = \rho g h_{Cx} A_x.
$$
Za vertikalnu komponentu $dF_V = p\,dA\sin\varphi = p\,dA_y$ gdje je $dA_y$ horizontalna projekcija. Umjesto integriranja po kutovima, koristimo ravnotežu imaginarnog fluidnog stupca iznad zakrivljene plohe: vertikalna sila koju ploha osjeća jednaka je težini tog stupca, pa $F_V = \rho g V^*$.
:::

::: {.mf1-izvod}
<p class="mf1-box-label">Matematički izvod — Vertikalna sila na zakrivljenu plohu — ravnoteža imaginarnog volumena fluida</p>

Da bi se odredila vertikalna komponenta sile koju fluid vrši na zakrivljenu plohu, uvodi se zamišljeni volumen fluida $V^*$ omeđen samom zakrivljenom plohom i njezinom vertikalnom projekcijom na slobodnu površinu (ili na drugu poznatu ravninu na kojoj se tlak može odrediti).

Pretpostavlja se da bi taj zamišljeni volumen, da postoji kao stvarni fluid, bio u ravnoteži. Na njega djeluju tri vertikalne sile:

- vlastita težina: $W^* = \rho g V^*$, usmjerena prema dolje;
- sila tlaka na gornju (vodoravnu zatvarajuću) plohu $A_t$: $F_t = p_t A_t$, usmjerena prema dolje (tlak gura prema unutra);
- sila tlaka kojom okolni fluid djeluje na zakrivljenu plohu $A_z$ (sa strane zakrivljene plohe prema imaginarnom volumenu): označi se s $F_z$ i traži se njezin smjer i iznos.

Iz uvjeta ravnoteže $\sum F_z = 0$ slijedi

$$
F_z = W^* + F_t = \rho g V^* + p_t A_t.
$$

Pri **otvorenom spremniku** sa slobodnom površinom na visini $A_t$ vrijedi $p_t = 0$ (manometarski), pa se izraz reducira na klasični

$$
F_V = \rho g V^*.
$$

Pri **zatvorenom spremniku s plinom pod tlakom $p_g$** iznad fluida dodatno se pojavljuje član $p_g A_t$:

$$
F_V = \rho g V^* + p_g A_t.
$$

Newtonov treći zakon daje obrnutu silu fluida na samu zakrivljenu plohu (i samim time na konstrukciju koja je drži): $F_{fluid\to ploha} = -F_z$, dakle prema dolje ako je $V^*$ "iznad" plohe (fluid je iznad), a prema gore ako je "ispod" (fluid je ispod plohe i $V^*$ je samo geometrijski pomoćni volumen). Predznak vertikalne komponente $F_V$ time je strogo posljedica geometrije konkretne plohe i ne treba ga "pogađati" iz iskustva.

Alternativno se ista sila može računati izravnim integralom

$$
F_V = \int_{A_z} p\,dA_y = \int_{A_z} p\,dA \cdot \cos\theta_v,
$$

gdje je $\theta_v$ kut između normale na plohu i vertikale, a $dA_y$ vertikalna projekcija elementa plohe. Oba pristupa daju identičan rezultat — argument preko imaginarnog volumena samo nudi geometrijski intuitivnu sliku iste matematike.
:::

## Riješeni primjeri

::: {.mf1-we}
<p class="mf1-box-label">Riješeni primjer — Potopljena četvrtina kruga&nbsp;<span class="mf1-level">T2</span></p>

**Kontekst:** U bočnoj stijenci spremnika potopljena je zakrivljena ploha oblika četvrtine kruga, ispod slobodne površine vode. Treba rastaviti hidrostatsku silu na horizontalnu i vertikalnu komponentu i odrediti iznos rezultante.

**Zadano**

- Polumjer četvrtine kruga zakrivljene površine `AB`: $R = 1{,}22\ \text{m}$
- Duljina spremnika okomito na presjek: $b = 1{,}83\ \text{m}$
- Dubina gornje točke zakrivljene površine ispod slobodne površine: $h_1 = 2{,}44\ \text{m}$
- Gustoća vode: $\rho = 998\ \text{kg/m}^3$

**Traženo**

1. horizontalnu komponentu sile $F_H$ i dubinu njezina hvatišta.
2. vertikalnu komponentu sile $F_V$ i vodoravni položaj njezina pravca djelovanja.
3. iznos rezultante $F_R$.

![U06 Val 1 - potopljena četvrtina kruga](../assets/print/u06_val1_cetvrtina_kruga.svg)

**Pretpostavke i model**

Horizontalna komponenta čita se preko vertikalne projekcije zakrivljene površine, a vertikalna preko težine zamišljenog volumena vode iznad te plohe. U ovom primjeru taj imaginarni volumen leži potpuno ispod slobodne površine, pa je $F_V$ usmjerena prema gore.

**Rješenje**

#### 1. Horizontalna komponenta

Vertikalna projekcija zakrivljene površine jest pravokutnik površine

$$
A_x = Rb = 1{,}22 \cdot 1{,}83 = 2{,}233\ \text{m}^2.
$$

Dubina težišta te projekcije iznosi

$$
h_{Cx} = h_1 + \frac{R}{2} = 2{,}44 + 0{,}61 = 3{,}05\ \text{m}.
$$

Zato je horizontalna komponenta sile

$$
F_H = \rho g A_x h_{Cx} = 998 \cdot 9{,}81 \cdot 2{,}233 \cdot 3{,}05 \approx 6{,}67 \cdot 10^4\ \text{N} = 66{,}7\ \text{kN}.
$$

Dubina hvatišta horizontalne komponente dobiva se kao centar tlaka vertikalne projekcije:

$$
h_{FH} = h_{Cx} + \frac{I_G}{h_{Cx}A_x},
$$

pri čemu je za pravokutnik

$$
I_G = \frac{bR^3}{12} = \frac{1{,}83 \cdot 1{,}22^3}{12} = 0{,}277\ \text{m}^4.
$$

Zato je

$$
h_{FH} = 3{,}05 + \frac{0{,}277}{3{,}05 \cdot 2{,}233} \approx 3{,}09\ \text{m}.
$$

#### 2. Vertikalna komponenta

Vertikalna komponenta jednaka je težini zamišljenog volumena vode iznad plohe `AB`. Taj volumen sastoji se od:

1. pravokutnog bloka volumena $V_1 = h_1Rb$.
2. četvrtine cilindra volumena $V_2 = \frac{\pi R^2}{4}b$.

Numerički:

$$
V_1 = 2{,}44 \cdot 1{,}22 \cdot 1{,}83 = 5{,}448\ \text{m}^3,
$$

$$
V_2 = \frac{\pi \cdot 1{,}22^2}{4} \cdot 1{,}83 = 2{,}139\ \text{m}^3,
$$

pa je ukupni volumen

$$
V^* = V_1 + V_2 = 7{,}587\ \text{m}^3.
$$

Odakle slijedi

$$
F_V = \rho g V^* = 998 \cdot 9{,}81 \cdot 7{,}587 \approx 7{,}43 \cdot 10^4\ \text{N} = 74{,}3\ \text{kN}.
$$

Smjer sile je **prema gore**, jer zamišljeni volumen predstavlja stvarni stupac vode iznad zakrivljene površine.

Vodoravni položaj pravca djelovanja dobiva se iz težišta tog volumena:

$$
x_{FV} = \frac{V_1 x_1 + V_2 x_2}{V_1 + V_2},
$$

gdje je za pravokutni dio $x_1 = R/2 = 0{,}61\ \text{m}$, a za četvrtinu kruga $x_2 = \frac{4R}{3\pi} = 0{,}518\ \text{m}$. Zato je

$$
x_{FV} = \frac{5{,}448 \cdot 0{,}61 + 2{,}139 \cdot 0{,}518}{7{,}587} \approx 0{,}584\ \text{m}.
$$

#### 3. Rezultanta

Kako su komponente okomite jedna na drugu, iznos rezultante je

$$
F_R = \sqrt{F_H^2 + F_V^2} = \sqrt{66{,}7^2 + 74{,}3^2}\ \text{kN} \approx 99{,}8\ \text{kN}.
$$

**Provjera i komentar**

1. Ovdje je $F_V$ prema gore jer se imaginarni volumen nalazi ispod slobodne površine; to je suprotan slučaj od podtlačnog doprinosa u složenijim geometrijama.
2. Horizontalna komponenta mora se dobiti iz projekcije, pa je razumno reda sile na ravnu vertikalnu plohu sličnih dimenzija.
3. Rezultanta mora biti veća od svake pojedine komponente, ali manja od njihova aritmetičkog zbroja.
:::

Tek nakon tog baznog rastava ima smisla prijeći na složeniji zatvarač u kojem se na zakrivljeni dio nadovezuju još ravni segment, vlastita težina konstrukcije i momentna ravnoteža.

::: {.mf1-we}
<p class="mf1-box-label">Riješeni primjer — Sklopiva servisna brana s zakrivljenim rubom&nbsp;<span class="mf1-level">T2</span></p>

**Kontekst:** U hidrotehničkom objektu sklopiva servisna brana s ravnim i zakrivljenim segmentom okretljivo je vezana pri slobodnoj površini. Treba odrediti hidrostatske komponente na pojedinim dijelovima i silu držanja koja drži branu zatvorenom.

**Zadano**

- Jedinična širina servisne brane: $B = 1{,}00\ \text{m}$
- Brana je okretljivo vezana u točki `O` na razini slobodne površine
- Ravni segment `OA` nagnut je pod kutom $45^\circ$ prema dolje; zakrivljeni rub `ABD` nadovezuje se na njega (vidjeti skicu)
- Masa brane: $m = 580\ \text{kg}$
- Gustoća vode: $\rho = 998\ \text{kg/m}^3$
- Geometrija presjeka: $H = 2{,}10\ \text{m}$, $h = 1{,}92\ \text{m}$, $a = 0{,}46\ \text{m}$
- Duljina ravnog dijela: $L = (h-a)\sqrt{2}$
- Pomoćna mjera zakrivljenog ruba: $y = H + a - h$
- Brana se pridržava vodoravnom silom $F$ u donjoj točki `D`

**Traženo**

1. Odredite silu hidrostatskog tlaka na ravni dio `OA` i položaj njezina hvatišta.
2. Odredite vertikalnu komponentu sile hidrostatskog tlaka na zakrivljeni dio `ABD` i navedite njezin smjer.
3. Odredite silu $F$ potrebnu da brana ostane u ravnotezi.

Zanemarite debljinu stijenke i mali uzgon na dvostruko okupanom tankom dijelu konstrukcije.

![U06 Val 2 - sklopiva servisna brana s zakrivljenim rubom](../assets/print/u06_val2_sklopiva_brana.svg)

**Pretpostavke i model**

Ravni dio `OA` tretira se kao klasična ravna ploha nagnuta pod $45^\circ$, dok se zakrivljeni rub `ABD` čita preko vertikalne komponente sile. Za taj zakrivljeni dio nije potreban detaljan lokalni rastav tlakova; dovoljan je zamišljeni volumen fluida koji ga definira.

**Rješenje**

Najprije se iz geometrije dobiva duljina ravnog dijela:

$$
L = (h-a)\sqrt{2} = (1{,}92 - 0{,}46)\sqrt{2} \approx 2{,}065\ \text{m},
$$

te pomoćna mjera zakrivljenog ruba:

$$
y = H + a - h = 2{,}10 + 0{,}46 - 1{,}92 = 0{,}64\ \text{m}.
$$

#### 1. Sila na ravni dio `OA`

Težište ravnog dijela nalazi se na dubini

$$
h_C = \frac{h-a}{2} = \frac{1{,}92 - 0{,}46}{2} = 0{,}73\ \text{m},
$$

pa je sila hidrostatskog tlaka na taj segment

$$
F_{OA} = \rho g h_C A = \rho g \frac{h-a}{2} \cdot L \cdot B = 998 \cdot 9{,}81 \cdot 0{,}73 \cdot 2{,}065 \cdot 1{,}00 \approx 14757\ \text{N} \approx 14{,}76\ \text{kN}.
$$

Kako gornji rub ravnog segmenta leži na slobodnoj površini, pomak hvatišta od težišta po ravnini iznosi

$$
\Delta y = \frac{I_{\xi\xi}}{h_C A} = \frac{L}{6} \approx 0{,}344\ \text{m}.
$$

Zato je krak sile $F_{OA}$ u odnosu na zglob `O`

$$
\frac{L}{2} - \Delta y = \frac{L}{3} \approx 0{,}688\ \text{m}.
$$

#### 2. Vertikalna komponenta na zakrivljeni rub `ABD`

Vertikalna komponenta jednaka je težini zamišljenog volumena fluida koji definira zakrivljeni rub. U ovoj geometriji taj se volumen svodi na pravokutni blok volumena $V^* = y^2 B$, pa je

$$
F_V = \rho g y^2 B = 998 \cdot 9{,}81 \cdot 0{,}64^2 \cdot 1{,}00 \approx 4010\ \text{N} \approx 4{,}01\ \text{kN}.
$$

Smjer ove sile je **prema dolje**, jer zamišljeni volumen koji je definira u ovoj sceni leži iznad slobodne površine, pa zakrivljeni rub zapravo osjeća podtlačni doprinos, a ne klasični uzgonski potisak prema gore.

#### 3. Sila držanja u točki `D`

Težina brane iznosi

$$
W = mg = 580 \cdot 9{,}81 = 5689{,}8\ \text{N}.
$$

Iz ravnoteze momenata oko točke `O` slijedi

$$
F \cdot H + F_{OA}\left(\frac{L}{2} - \Delta y\right) - (W + F_V)\cdot H = 0,
$$

pa je tražena sila držanja

$$
F = \frac{(W + F_V)H - F_{OA}(L/2 - \Delta y)}{H} = \frac{(5689{,}8 + 4010)\cdot 2{,}10 - 14756{,}7 \cdot 0{,}688}{2{,}10} \approx 4864\ \text{N} \approx 4{,}86\ \text{kN}.
$$

**Provjera i komentar**

1. Vertikalna komponenta nije golema, ali nije ni zanemariva: reda je nekoliko kilonjutna, što je sasvim razumno za geometriju s pomoćnom mjerom $y = 0{,}64\ \text{m}$.
2. Sila na ravni dio mora biti veća od vertikalne komponente zakrivljenog ruba jer je ravna opločena površina veća i nalazi se dublje.
3. Sila držanja manja je od zbroja nizvodnih sila jer dio opterećenja već preuzima moment sile na ravnom segmentu.
:::

Za zatvaranje poglavlja korisno je vratiti se i na čistu referentnu geometriju u kojoj je zakrivljena površina neposredno vezana uz slobodnu površinu. Tada se najjasnije vidi kako projekcija daje $F_H$, imaginarni volumen daje $F_V$, a rezultanta se dobiva tek na kraju.

::: {.mf1-we}
<p class="mf1-box-label">Riješeni primjer — Četvrtcilindrični revizijski poklopac uz slobodnu površinu&nbsp;<span class="mf1-level">T2</span></p>

**Kontekst:** Na bočnoj stijenci spremnika ugrađen je četvrtcilindrični revizijski poklopac čiji gornji rub leži upravo na slobodnoj površini vode. Treba rastaviti hidrostatsku silu na komponente i odrediti iznos i smjer rezultante.

**Zadano**

- Širina četvrtcilindričnog poklopca (jedinična osi): $b = 1{,}20\ \text{m}$
- Polumjer zakrivljenosti poklopca: $R = 0{,}90\ \text{m}$
- Gornja točka zakrivljene površine nalazi se na slobodnoj površini vode
- Gustoća vode: $\rho = 998\ \text{kg/m}^3$

**Traženo**

1. horizontalnu komponentu sile $F_H$ i dubinu njezina pravca djelovanja.
2. vertikalnu komponentu sile $F_V$ i vodoravni položaj njezina pravca djelovanja.
3. iznos rezultante $F_R$ i kut koji zatvara s horizontalom.

![U06 Val 3 - četvrtcilindrični poklopac](../assets/print/u06_val3_cetvrtcilindricni_poklopac.svg)

**Pretpostavke i model**

Kako gornji rub poklopca leži na slobodnoj površini, vertikalna projekcija je jednostavan pravokutnik visine $R$, a imaginarni volumen iznad zakrivljene plohe točno je četvrtina valjka. Zato se obje komponente mogu pročitati bez dodatnih geometrijskih korekcija.

**Rješenje**

#### 1. Horizontalna komponenta

Vertikalna projekcija zakrivljene plohe jest pravokutnik površine

$$
A_x = Rb = 0{,}90 \cdot 1{,}20 = 1{,}08\ \text{m}^2.
$$

Dubina težišta te projekcije iznosi

$$
h_{Cx} = \frac{R}{2} = 0{,}45\ \text{m},
$$

pa je horizontalna komponenta sile

$$
F_H = \rho g A_x h_{Cx} = 998 \cdot 9{,}81 \cdot 1{,}08 \cdot 0{,}45 \approx 4758\ \text{N} \approx 4{,}76\ \text{kN}.
$$

Kako projekcija počinje na slobodnoj površini, dubina pravca djelovanja horizontalne komponente jednaka je centru tlaka tog pravokutnika:

$$
h_H = \frac{2R}{3} = 0{,}60\ \text{m}.
$$

#### 2. Vertikalna komponenta

Vertikalna komponenta jednaka je težini imaginarnog volumena vode iznad zakrivljene plohe. Ovdje je taj volumen četvrtina valjka:

$$
V^* = \frac{\pi R^2}{4} b = \frac{\pi \cdot 0{,}90^2}{4} \cdot 1{,}20 \approx 0{,}763\ \text{m}^3.
$$

Zato je

$$
F_V = \rho g V^* = 998 \cdot 9{,}81 \cdot 0{,}763 \approx 7474\ \text{N} \approx 7{,}47\ \text{kN}.
$$

Smjer je **prema dolje** jer imaginarni volumen vode leži iznad zakrivljene plohe. Pravac djelovanja te sile prolazi težištem četvrtine kruga, pa je vodoravna udaljenost od okomite stijenke

$$
x_V = \frac{4R}{3\pi} = \frac{4 \cdot 0{,}90}{3\pi} \approx 0{,}382\ \text{m}.
$$

#### 3. Rezultanta

Kako su komponente okomite jedna na drugu, iznos rezultante je

$$
F_R = \sqrt{F_H^2 + F_V^2} = \sqrt{4{,}76^2 + 7{,}47^2}\ \text{kN} \approx 8{,}86\ \text{kN}.
$$

Kut rezultante prema horizontalnoj osi glasi

$$
\alpha = \arctan\left(\frac{F_V}{F_H}\right) = \arctan\left(\frac{7{,}47}{4{,}76}\right) \approx 57{,}5^\circ
$$

prema dolje u odnosu na horizontalu.

**Provjera i komentar**

1. Vertikalna komponenta mora biti veća od horizontalne jer je imaginarni volumen ovdje razmjerno velik u odnosu na projekciju.
2. Pravac djelovanja $F_H$ mora biti dublje od težišta projekcije, pa je $h_H > R/2$ fizikalno očekivan rezultat.
3. Rezultanta mora biti veća od svake pojedine komponente, ali manja od njihova zbroja.
:::

::: {.mf1-we}
<p class="mf1-box-label">Riješeni primjer — Četvrtcilindrični poklopac u zatvorenom spremniku s plinskim jastukom&nbsp;<span class="mf1-level">T2</span></p>

**Kontekst:** U zatvorenom hidropneumatskom servisnom spremniku iznad slobodne površine ulja djeluje plinski jastuk pod manometarskim pretlakom. Treba razdvojiti doprinose hidrostatskog tlaka ulja i ravnomjernog plinskog tlaka na zakrivljenom poklopcu i usporediti rezultantu s otvorenim slučajem.

**Zadano**

Hidropneumatski servisni spremnik ima oblik zatvorenog cilindra. Donji dio spremnika ispunjen je uljem do slobodne površine; iznad nje nalazi se plinski jastuk (dušik) pod **manometarskim** pretlakom. Na bočnoj stijenci nalazi se četvrtcilindrični inspekcijski poklopac, oblika i orijentacije identičnih kao u prvom primjeru ovog poglavlja (potopljena četvrtina kruga), ali je sada slobodna površina ulja u **zatvorenom** spremniku pod nadtlakom plinskog jastuka.

- Polumjer zakrivljenosti poklopca: $R = 0{,}50\ \text{m}$
- Širina poklopca uzduž osi zakrivljenja: $b = 1{,}20\ \text{m}$
- Gornji rub poklopca poklapa se s razinom slobodne površine ulja
- Gustoća ulja: $\rho = 860\ \text{kg/m}^3$
- Manometarski tlak plinskog jastuka: $p_g = 200\ \text{kPa}$
- Vanjska strana poklopca je na atmosferskom tlaku
- $g = 9{,}81\ \text{m/s}^2$

**Traženo**

1. Horizontalna komponenta sile na poklopac $F_H$ s razdvojenim doprinosima ulja i plina.
2. Vertikalna komponenta $F_V$ s razdvojenim doprinosima.
3. Iznos i smjer rezultantne sile $F$ na poklopac.
4. Usporediti s otvorenim spremnikom (kad bi $p_g = 0$): za koliko se mijenjaju $F_H$, $F_V$, kut nagiba rezultante?

![Četvrtcilindrični poklopac u zatvorenom spremniku s plinskim jastukom pod tlakom $p_g = 200$ kPa iznad slobodne površine ulja ($\rho = 860$ kg/m³). Plinski jastuk dodaje uniformni pomak tlaka na cijelu plohu.](../assets/print/u06_fig_plinski_jastuk.svg){#fig-u06-plinski-jastuk fig-align="center"}

**Pretpostavke i model**

Sustav je u mirovanju – razmatra se čista hidrostatika. Plin je dovoljno laganog hidrostatičkog stupca da se njegova vlastita "težina" zanemari, pa je tlak plina **jednak na cijeloj slobodnoj površini ulja**. Plin svojim tlakom djeluje ravnomjerno na slobodnu površinu, a Pascalov princip prenosi taj tlak kroz mirujuće ulje na cijelu unutarnju stijenku spremnika – uključujući i poklopac. Zato se tlak u dubini $h$ ispod slobodne površine ulja računa kao $p(h) = p_g + \rho g h$.

To znači da na svaku komponentu sile postoje **dva aditivna doprinosa**: jedan od hidrostatskog tlaka ulja kao i u otvorenom spremniku, te drugi od plinskog jastuka kao da je plin svojim tlakom $p_g$ uniformno pritisnuo plohu. Komponente sila zbog plina prirodno se pišu preko **projekcija** plohe – jer uniformni tlak na zakrivljenoj plohi daje silu na njezinim projekcijama.

**Rješenje**

**Projekcije plohe.** Vertikalna projekcija plohe (na vertikalnu ravninu okomitu na os zakrivljenja) je pravokutnik visine $R$ i širine $b$. Horizontalna projekcija (na horizontalnu ravninu) je pravokutnik dimenzija $R \cdot b$ – iste površine kao vertikalna, jer kod četvrtkruga te dvije projekcije imaju iste dimenzije.

$$
A_{proj,v} = A_{proj,h} = R \cdot b = 0{,}50 \cdot 1{,}20 = 0{,}60\ \text{m}^2.
$$

**Horizontalna komponenta $F_H$.** Doprinos ulja ($F_{H,o}$) preko težišta vertikalne projekcije, koje je na dubini $h_C = R/2 = 0{,}25$ m:

$$
F_{H,o} = \rho g h_C A_{proj,v} = 860 \cdot 9{,}81 \cdot 0{,}25 \cdot 0{,}60 \approx 1265\ \text{N} \approx 1{,}27\ \text{kN}.
$$

Doprinos plina ($F_{H,g}$) – uniformni tlak $p_g$ na istu projekciju:

$$
F_{H,g} = p_g A_{proj,v} = 200\,000 \cdot 0{,}60 = 120\,000\ \text{N} = 120\ \text{kN}.
$$

Ukupno:

$$
F_H = F_{H,o} + F_{H,g} \approx 1{,}27 + 120 \approx 121{,}3\ \text{kN}.
$$

**Vertikalna komponenta $F_V$.** Doprinos ulja ($F_{V,o}$) jednak je težini ulja koje bi zauzimalo imaginarni četvrtkružni volumen iznad plohe (kao u potopljenoj četvrtini kruga):

$$
V_{imag} = \frac{\pi R^2}{4} \cdot b = \frac{\pi \cdot 0{,}50^2}{4} \cdot 1{,}20 \approx 0{,}2356\ \text{m}^3,
$$

$$
F_{V,o} = \rho g V_{imag} = 860 \cdot 9{,}81 \cdot 0{,}2356 \approx 1{,}99\ \text{kN}.
$$

Doprinos plina ($F_{V,g}$) – uniformni tlak $p_g$ na horizontalnu projekciju:

$$
F_{V,g} = p_g A_{proj,h} = 200\,000 \cdot 0{,}60 = 120\,000\ \text{N} = 120\ \text{kN}.
$$

Ukupno:

$$
F_V = F_{V,o} + F_{V,g} \approx 1{,}99 + 120 \approx 122{,}0\ \text{kN}.
$$

**Iznos i smjer rezultante:**

$$
F = \sqrt{F_H^2 + F_V^2} \approx \sqrt{121{,}3^2 + 122{,}0^2} \approx 172{,}0\ \text{kN},
$$

$$
\alpha = \arctan\frac{F_V}{F_H} = \arctan\frac{122{,}0}{121{,}3} \approx 45{,}2^\circ.
$$

**Usporedba s otvorenim spremnikom** ($p_g = 0$):

$$
F_{H,open} = 1{,}27\ \text{kN}, \quad F_{V,open} = 1{,}99\ \text{kN},
$$

$$
F_{open} = \sqrt{1{,}27^2 + 1{,}99^2} \approx 2{,}36\ \text{kN}, \quad \alpha_{open} \approx 57{,}5^\circ.
$$

Omjer rezultanti $F / F_{open} \approx 73$.

**Provjera i komentar**

1. Plinski jastuk dodaje **isti** iznos sile (120 kN) na obje komponente, jer su projekcije plohe na vertikalnu i horizontalnu ravninu identične za četvrtinu kruga ($R \cdot b$). Zato pri dominantnom $p_g$ smjer rezultante teži ka $45^\circ$, neovisno o geometriji ploche.
2. Zakrivljenost plohe i tip fluida postaju **sekundarni** ako je $p_g \gg \rho g R$. Pri ulja na dubini $R = 0{,}50$ m hidrostatski tlak iznosi svega $\rho g R \approx 4{,}2$ kPa – pedeset puta manje od plinskog $p_g$. Zato hidrostatski doprinos čini manje od $1\%$ ukupne sile.
3. Inženjerska poruka: pri **dimenzioniranju stijenki i vijaka zatvorenih hidropneumatskih spremnika** glavni teret podnosi plinski tlak. To je razlog zašto kotlovi pod tlakom (PVC – pressure vessels) imaju različitu konstrukciju od otvorenih spremnika iste dubine: zakrivljene plohe i polusferne kape biraju se ne radi smanjenja hidrostatske sile, nego radi optimalnog raspodjeljivanja **plinskog/parnog tlaka** po stijenci.
4. Hvatišta dvaju doprinosa $F_V$ nisu ista: $F_{V,o}$ djeluje u centroidu imaginarnog četvrtkružnog volumena ($x_o = 4R/3\pi \approx 0{,}212$ m od osi simetrije), a $F_{V,g}$ djeluje u centroidu horizontalne projekcije, pravokutnika ($x_g = R/2 = 0{,}25$ m). Pri momentnom proračunu vijaka treba računati sa zbirnim hvatištem, ne s jednim "prosjekom".
:::

::: {.mf1-ch}
<p class="mf1-box-label">Cjeloviti zadatak — Četvrtcilindrični poklopac s vodoravnom spojnicom&nbsp;<span class="mf1-level">T3</span></p>

**Kontekst:** U servisnom spremniku četvrtcilindrični poklopac zglobno je vezan u gornjoj točki, a donji rub pridržava vodoravna spojnica. Treba odrediti komponente hidrostatske sile, rezultantu i silu koju spojnica mora preuzeti da poklopac ostane zatvoren.

**Zadano**

- Širina četvrtcilindričnog servisnog poklopca: $b = 1{,}40\ \text{m}$
- Polumjer zakrivljenosti poklopca: $R = 1{,}10\ \text{m}$
- Gornja točka `A` poklopca nalazi se na slobodnoj površini vode
- Poklopac je okretljivo vezan u točki `A`; u donjoj točki `D` pridržava se vodoravnom spojnicom
- Gustoća vode: $\rho = 998\ \text{kg/m}^3$
- Zanemaruju se vlastita težina poklopca i trenje u zglobu

**Traženo**

1. horizontalnu komponentu sile $F_H$ i dubinu njezina pravca djelovanja $h_H$.
2. vertikalnu komponentu sile $F_V$ i vodoravni položaj njezina pravca djelovanja $x_V$.
3. iznos rezultante $F_R$ i kut koji zatvara s horizontalom.
4. silu spojnice $T$ potrebnu da poklopac ostane zatvoren.

![U06 CH 1 - četvrtcilindrični poklopac s vodoravnom spojnicom](../assets/print/u06_ch1_poklopac_spojnica.svg)

**Pretpostavke i model**

Ovo je i dalje čista hidrostatska sila na zakrivljenoj plohi, ali sada komponente više nisu konačni odgovor. Horizontalna komponenta čita se preko vertikalne projekcije, vertikalna preko težine imaginarnog volumena vode iznad poklopca, a tek se zatim iz ravnoteze momenata oko zgloba `A` dobiva potrebna sila držanja spojnice.

**Rješenje**

#### 1. Horizontalna komponenta

Vertikalna projekcija zakrivljene plohe jest pravokutnik površine

$$
A_x = Rb = 1{,}10 \cdot 1{,}40 = 1{,}54\ \text{m}^2.
$$

Dubina težišta te projekcije iznosi

$$
h_{Cx} = \frac{R}{2} = 0{,}55\ \text{m},
$$

pa je horizontalna komponenta sile

$$
F_H = \rho g A_x h_{Cx} = 998 \cdot 9{,}81 \cdot 1{,}54 \cdot 0{,}55 \approx 8292\ \text{N} \approx 8{,}29\ \text{kN}.
$$

Kako projekcija počinje na slobodnoj površini, dubina pravca djelovanja horizontalne komponente jednaka je centru tlaka tog pravokutnika:

$$
h_H = \frac{2R}{3} = \frac{2 \cdot 1{,}10}{3} \approx 0{,}733\ \text{m}.
$$

#### 2. Vertikalna komponenta

Vertikalna komponenta jednaka je težini imaginarnog volumena vode iznad zakrivljene plohe. Ovdje je taj volumen četvrtina valjka:

$$
V^* = \frac{\pi R^2}{4} b = \frac{\pi \cdot 1{,}10^2}{4} \cdot 1{,}40 \approx 1{,}331\ \text{m}^3.
$$

Zato je

$$
F_V = \rho g V^* = 998 \cdot 9{,}81 \cdot 1{,}331 \approx 13026\ \text{N} \approx 13{,}03\ \text{kN}.
$$

Smjer je **prema dolje** jer imaginarni volumen vode leži iznad zakrivljene plohe. Pravac djelovanja te sile prolazi tezistem četvrtine kruga, pa je vodoravna udaljenost od vertikale kroz zglob `A`

$$
x_V = \frac{4R}{3\pi} = \frac{4 \cdot 1{,}10}{3\pi} \approx 0{,}467\ \text{m}.
$$

#### 3. Rezultanta

Kako su komponente okomite jedna na drugu, iznos rezultante je

$$
F_R = \sqrt{F_H^2 + F_V^2} = \sqrt{8{,}29^2 + 13{,}03^2}\ \text{kN} \approx 15{,}44\ \text{kN}.
$$

Kut rezultante prema horizontalnoj osi glasi

$$
\alpha = \arctan\left(\frac{F_V}{F_H}\right) = \arctan\left(\frac{13{,}03}{8{,}29}\right) \approx 57{,}5^\circ
$$

prema dolje u odnosu na horizontalu.

#### 4. Sila spojnice

Obje hidrostatske komponente otvaraju poklopac oko zgloba `A`, pa iz ravnoteze momenata oko te točke vrijedi

$$
T R = F_H h_H + F_V x_V \quad \Rightarrow \quad T = \frac{F_H h_H + F_V x_V}{R}.
$$

Uvrstavanjem brojeva dobiva se potrebna sila spojnice

$$
T = \frac{8292 \cdot 0{,}733 + 13026 \cdot 0{,}467}{1{,}10} \approx 11057\ \text{N} \approx 11{,}06\ \text{kN}.
$$

**Provjera i komentar**

Ovaj `CH` zatvara puni radni luk <span class="mf1-ch-ref"><span class="mf1-ch-code">U06</span><span class="mf1-ch-title">Zakrivljene plohe i rastav sila</span></span> u jednom zatvaraču: projekcija daje $F_H \approx 8{,}29\ \text{kN}$ na dubini $0{,}733\ \text{m}$, imaginarni volumen daje $F_V \approx 13{,}03\ \text{kN}$ prema dolje s krakom $0{,}467\ \text{m}$, a njihova rezultanta iznosi oko $15{,}44\ \text{kN}$. Da bi poklopac ostao zatvoren, vodoravna spojnica mora preuzeti silu od oko $11{,}06\ \text{kN}$.

1. Kako je imaginarni volumen ovdje iznad zakrivljene plohe, $F_V$ mora biti prema dolje, a ne prema gore.
2. Sila spojnice mora biti manja od rezultante, ali istog reda veličine, jer djeluje s punim krakom $R$.
3. Ako se pri momentu oko `A` uzme krak $F_H$ jednak polumjeru umjesto dubine $h_H$, geometrija pravca djelovanja nije dobro pročitana.
:::

::: {.mf1-we}
<p class="mf1-box-label">Riješeni primjer — Hidrostatska sila na zaobljeni poklopac procesnog kotla &nbsp;<span class="mf1-level">T2</span></p>

**Primjer za strojare**

**Kontekst:** Cilindrični tlačni kotao u kemijskom postrojenju ima zaobljeni prijelaz boka u dno (četvrtina kruga). Projektant provjerava hidrostatske komponente na taj segment pri ispitivanju vodom.

**Zadano**

- Polumjer zakrivljenja: $R = 0{,}60\ \text{m}$
- Širina kotla (okomito): $b = 1{,}50\ \text{m}$
- Slobodna površina je $h_1 = 1{,}20\ \text{m}$ iznad vrha zaobljenog segmenta
- Gustoća vode: $\rho = 998\ \text{kg/m}^3$

**Traženo**

Horizontalna i vertikalna komponenta sile te iznos rezultante.

![Zaobljeni poklopac procesnog kotla: R=0,60 m, b=1,50 m, h₁=1,20 m, F_H=13,22 kN, F_V=14,74 kN](../assets/print/u06_fig_zaobljeni_poklopac_kotla.svg){#fig-u06-zaobljeni-poklopac-kotla fig-align="center" style="width:100%;max-width:940px;"}

**Pretpostavke i model**

Zaobljeni segment = četvrtina kruga. $F_H$ po vertikalnoj projekciji, $F_V$ po imaginarnom volumenu (pravokutnik + četvrtina kruga) iznad segmenta.

**Rješenje**

$$
A_x = R\cdot b = 0{,}60 \cdot 1{,}50 = 0{,}90\ \text{m}^2, \quad h_{Cx} = h_1 + R/2 = 1{,}20 + 0{,}30 = 1{,}50\ \text{m}
$$

$$
F_H = 998 \cdot 9{,}81 \cdot 0{,}90 \cdot 1{,}50 = 13{,}22\ \text{kN}
$$

$$
V^* = b\!\left(h_1 R + \tfrac{\pi R^2}{4}\right) = 1{,}50\!\left(1{,}20 \cdot 0{,}60 + \tfrac{\pi \cdot 0{,}36}{4}\right) = 1{,}50 \cdot 1{,}003 = 1{,}505\ \text{m}^3
$$

$$
F_V = 998 \cdot 9{,}81 \cdot 1{,}505 = 14{,}74\ \text{kN}\quad(\uparrow)
$$

$$
F_R = \sqrt{13{,}22^2 + 14{,}74^2} \approx 19{,}8\ \text{kN}
$$

**Provjera i komentar**

$F_V$ je prema gore jer zamišljeni volumen leži ispod slobodne površine — ploha „osjeća" njegovu težinu prema gore. Rezultanta $19{,}8\ \text{kN}$ realna je za kotao tog gabarita. Smjer rezultante zatvara kut $\arctan(14{,}74/13{,}22) \approx 48°$ s horizontalom.

:::

::: {.mf1-we}
<p class="mf1-box-label">Riješeni primjer — Sile na zaobljeno dno retencijskog jezerca &nbsp;<span class="mf1-level">T2</span></p>

**Primjer za građevinare**

**Kontekst:** Na kraju kanala za odvodnju oborinske vode nalazi se retencijsko jezerce s polukružnim dnom. Projektant određuje hidrostatske sile na zaobljeni segment pri puni razini za dimenzioniranje temeljne ploče.

**Zadano**

- Polumjer zakrivljenja dna: $R = 1{,}00\ \text{m}$
- Duljina sekcije (okomito): $b = 4{,}00\ \text{m}$
- Slobodna površina $h_1 = 2{,}50\ \text{m}$ iznad vrha zaobljenog segmenta
- Gustoća vode: $\rho = 998\ \text{kg/m}^3$

**Traženo**

Horizontalna i vertikalna komponenta sile te rezultanta i smjer.

![Zaobljeno dno retencijskog jezerca: R=1,00 m, b=4,00 m, h₁=2,50 m, F_H=117,6 kN, F_V=128,6 kN](../assets/print/u06_fig_zaobljeno_dno_jezerca.svg){#fig-u06-zaobljeno-dno-jezerca fig-align="center" style="width:100%;max-width:940px;"}

**Rješenje**

$$
A_x = 1{,}00 \cdot 4{,}00 = 4{,}00\ \text{m}^2, \quad h_{Cx} = 2{,}50 + 0{,}50 = 3{,}00\ \text{m}
$$

$$
F_H = 998 \cdot 9{,}81 \cdot 4{,}00 \cdot 3{,}00 = 117{,}6\ \text{kN}
$$

$$
V^* = 4{,}00\!\left(2{,}50 \cdot 1{,}00 + \tfrac{\pi \cdot 1{,}00^2}{4}\right) = 4{,}00 \cdot 3{,}285 = 13{,}14\ \text{m}^3
$$

$$
F_V = 998 \cdot 9{,}81 \cdot 13{,}14 = 128{,}6\ \text{kN}\quad(\uparrow)
$$

$$
F_R = \sqrt{117{,}6^2 + 128{,}6^2} \approx 174{,}0\ \text{kN}
$$

**Provjera i komentar**

$F_V = 128{,}6\ \text{kN}$ znači da zaobljeno dno „nosi" imaginarni stupac vode prema gore. U proračunu temeljne ploče to je uzgon koji mora biti nadoknađen vlastitom težinom ploče ili ankerima. Kut rezultante: $\arctan(128{,}6/117{,}6) \approx 47{,}6°$ od horizontale.

:::

::: {.mf1-we}
<p class="mf1-box-label">Riješeni primjer — Zakrivljena pregrada u spremniku za skladištenje stlačenog CO₂ &nbsp;<span class="mf1-level">T3</span></p>

**Kontekst:** U postrojenju za hvatanje i skladištenje ugljika (engl. *carbon capture and storage*, CCS) jedan je od ključnih elemenata cilindrični skladišni spremnik za stlačeni CO₂. Prije puštanja u rad provodi se obavezna hidrostatička provjera čvrstoće: spremnik se ispuni vodom i opterećenje na njegove strukturne elemente mjeri se u kontroliranom uvjetu. Unutar spremnika nalazi se zakrivljena pregrada u obliku četvrtine cilindra koja razdvaja dva odjeljka.

**Zadano**

- Polumjer zakrivljene pregrade: $R = 1{,}20\ \text{m}$
- Dubina vrha pregrade ispod slobodne površine: $h_t = 2{,}50\ \text{m}$
- Širina pregrade (dimenzija u smjeru osi spremnika): $L = 3{,}50\ \text{m}$
- Testni medij: voda, $\rho = 998\ \text{kg/m}^3$
- Konveksna strana pregrade okrenuta je prema fluidu pod opterećenjem

**Traženo**

1. Horizontalna komponenta sile na pregradu;
2. Vertikalna komponenta sile;
3. Iznos rezultante i kut prema horizontali.

**Pretpostavke i model**

Promatra se statičko stanje s vodom kao testnim medijem. Pregrada je vertikalno postavljena, vrh joj je na zadanoj dubini, a četvrtina kruga proteže se prema dolje i u stranu. Horizontalna komponenta sile jednaka je sili na vertikalnu projekciju plohe; vertikalna komponenta jednaka je težini imaginarnog volumena fluida između plohe i slobodne površine. Atmosferski tlak djeluje s obje strane spremnika, pa se njegov doprinos poništava.

**Rješenje**

Vertikalna projekcija pregrade ima dimenzije $R \times L$, a dubina težišta te projekcije iznosi $h_t + R/2$:

$$
F_H = \rho g L R \left(h_t + \frac{R}{2}\right) = 998 \cdot 9{,}81 \cdot 3{,}50 \cdot 1{,}20 \cdot \left(2{,}50 + \frac{1{,}20}{2}\right).
$$

Uvrštavanjem $h_t + R/2 = 3{,}10\ \text{m}$:

$$
F_H = 998 \cdot 9{,}81 \cdot 3{,}50 \cdot 1{,}20 \cdot 3{,}10 \approx 127{,}4\ \text{kN}.
$$

Imaginarni volumen fluida iznad četvrtine cilindra iznosi

$$
V_{imag} = L\left(h_t R + R^2 - \frac{\pi R^2}{4}\right) = 3{,}50 \cdot \left(2{,}50 \cdot 1{,}20 + 1{,}20^2 - \frac{\pi \cdot 1{,}20^2}{4}\right).
$$

Računaju se redom $2{,}50 \cdot 1{,}20 = 3{,}00\ \text{m}^2$, $1{,}20^2 = 1{,}44\ \text{m}^2$ i $\pi \cdot 1{,}44 / 4 \approx 1{,}131\ \text{m}^2$:

$$
V_{imag} = 3{,}50 \cdot (3{,}00 + 1{,}44 - 1{,}131) = 3{,}50 \cdot 3{,}309 \approx 11{,}58\ \text{m}^3.
$$

Vertikalna komponenta sile zato iznosi

$$
F_V = \rho g V_{imag} = 998 \cdot 9{,}81 \cdot 11{,}58 \approx 113{,}4\ \text{kN}.
$$

Iznos rezultante:

$$
F_R = \sqrt{F_H^2 + F_V^2} = \sqrt{127{,}4^2 + 113{,}4^2} \approx \sqrt{16\,231 + 12\,860} \approx 170{,}5\ \text{kN}.
$$

Kut rezultante prema horizontali:

$$
\varphi = \arctan\frac{F_V}{F_H} = \arctan\frac{113{,}4}{127{,}4} \approx 41{,}7^\circ.
$$

**Provjera i komentar**

Rezultanta od $170{,}5\ \text{kN}$ predstavlja opterećenje koje pregrada mora podnijeti u testnom uvjetu s vodom. Pri stvarnoj eksploataciji s tekućim CO₂ (gustoća približno $780\ \text{kg/m}^3$ pri uobičajenim CCS uvjetima), istovjetne sile bile bi za oko $22\,\%$ niže — što je razlog zašto se test čvrstoće provodi vodom, kao najgorem scenariju za hidrostatičko opterećenje. Kut djelovanja rezultante od $41{,}7^\circ$ govori projektantu nosivih veza pregrade da konstrukcijski elementi moraju jednako podnijeti horizontalnu i vertikalnu komponentu. Pri stvarnoj eksploataciji uz CO₂ pojavljuje se i dodatno opterećenje plinskim tlakom, koje treba zasebno superponirati u proračunu sigurnosti — to nije obuhvaćeno ovim hidrostatičkim testom.
:::

::: {.mf1-samoprovjera}
<p class="mf1-box-label">Provjeri sebe</p>

Sljedeća pitanja služe za samostalnu provjeru razumijevanja prije prelaska na zadatke za vježbu.

1. Zašto se horizontalna komponenta sile na zakrivljenu plohu računa preko vertikalne projekcije plohe, a ne preko njezine stvarne zakrivljene površine?

::: {.callout-note collapse="true"}
### Odgovor
Komponenta sile u smjeru osi $x$ jednaka je integralu tlaka pomnoženog s projekcijom plohe na smjer okomit na os $x$. Ta projekcija je upravo vertikalna ravna projekcija plohe, pa horizontalna komponenta sile ne ovisi o zakrivljenosti same plohe nego samo o njezinoj projekciji.
:::

2. Što fizikalno predstavlja "imaginarni volumen" pri izračunu vertikalne komponente sile?

::: {.callout-note collapse="true"}
### Odgovor
To je volumen koji bi zauzela tekućina ako bi se prostor između zakrivljene plohe i slobodne površine ispunio istom tekućinom. Njezina težina jednaka je vertikalnoj komponenti sile koju ploha osjeća — neovisno o tome je li taj volumen u stvarnosti ispunjen tekućinom, zrakom ili je dio izrezan iz konstrukcije.
:::

3. Kako se određuje smjer vertikalne komponente: prema gore ili prema dolje?

::: {.callout-note collapse="true"}
### Odgovor
Smjer se određuje iz orijentacije plohe i položaja imaginarnog volumena. Ako je imaginarni volumen iznad plohe (ploha čini "dno" volumena), vertikalna komponenta djeluje prema gore. Ako je imaginarni volumen ispod plohe, komponenta djeluje prema dolje.
:::

4. Vrijedi li ovaj rastav sile na horizontalnu i vertikalnu komponentu i za plohe složenog (nepravilnog) oblika?

::: {.callout-note collapse="true"}
### Odgovor
Da, vrijedi neovisno o obliku zakrivljenosti sve dok se ploha može opisati zatvorenom geometrijom. Za nepravilne plohe horizontalna komponenta i dalje se računa preko vertikalne projekcije, a vertikalna komponenta preko volumena između plohe i slobodne površine — premda izračuni postaju složeniji i u praksi se često rješavaju numerički.
:::
:::

## Zadaci za vježbu

::: {.mf1-vjezbe-list}
1. **T1** Zakrivljeni poklopac presjeka četvrtine kruga polumjera $R = 0{,}65\ \text{m}$ i širine $b = 1{,}20\ \text{m}$ nalazi se u vodi. Gornja točka poklopca na dubini je $h_1 = 1{,}10\ \text{m}$ ispod slobodne površine. Odredi horizontalnu komponentu sile, vertikalnu komponentu sile i iznos rezultante.

	**Natuknica:** $F_H$ čitaj preko vertikalne projekcije, $F_V$ preko težine zamišljenog volumena, a rezultantu iz $F_R = \sqrt{F_H^2 + F_V^2}$.

	**Skica:** da - četvrtina kruga, slobodna površina, projekcija i zamišljeni volumen $V^*$.

2. **T1** Polucilindrični poklopac radijusa $R = 0{,}30\ \text{m}$ i širine $b = 0{,}90\ \text{m}$ potpuno je uronjen u vodu. Odredi komponente $F_H$ i $F_V$ te pravac rezultante ako ona prolazi središtem zakrivljenosti.

	**Natuknica:** projekcija daje $F_H$, zamišljeni volumen $F_V$; smjer rezultante zatvara odnos $\tan\alpha = F_V/F_H$.

	**Skica:** da - polucilindrična ploha, središte zakrivljenosti i pravac rezultante.

3. **T2** Polucilindrični revizijski poklopac radijusa $R = 0{,}40\ \text{m}$ i širine $b = 1{,}00\ \text{m}$ zglobno je ovješen na gornjem rubu. Voda doseže slobodnu površinu $0{,}85\ \text{m}$ iznad najviše točke zakrivljene plohe. Odredi silu rezultante i moment oko zgloba potreban za zadržavanje poklopca u zatvorenom položaju.

	**Natuknica:** prvo odredi $F_H$ i $F_V$ s njihovim pravcima djelovanja, a tek zatim prenesi svaku komponentu u moment oko zgloba.

	**Skica:** da - zakrivljeni poklopac sa zglobom, komponentama i krakovima momenata.

4. **T2** Zakrivljeni zatvarač presjeka četvrtine kruga polumjera $R = 0{,}55\ \text{m}$ zatvara spremnik s vodom, ali je iznad plohe zatvoren zračni prostor s jednolikim nadtlakom $p_0 = 18\ \text{kPa}$. Odredi kako se mijenjaju $F_H$ i $F_V$ u odnosu na slučaj bez nadtlaka.

	**Natuknica:** nadtlak dodaj na projekciju i na zamišljeni volumen kao jednoliki dodatni tlak; smjer $F_V$ provjeri iz stvarnog rasporeda fluida iznad plohe.

	**Skica:** da - zakrivljena ploha, slobodna površina ili zatvoreni zračni jastuk i označeni nadtlak $p_0$.

5. **T3** Zakrivljena ploha na dnu servisnog kanala zatvara volumen vode ispod stlačenog zračnog jastuka. Zamišljeni volumen koji određuje $F_V$ ima obujam $V^* = 0{,}42\ \text{m}^3$, a horizontalna projekcija plohe daje silu $F_H = 18{,}5\ \text{kN}$. Odredi vertikalnu komponentu sile, procijeni njezin smjer i izračunaj iznos rezultante.

	**Natuknica:** iz $F_V = \rho gV^*$ najprije dobij iznos, smjer odredi iz zamišljenog volumena i rasporeda tlaka, a rezultantu zatvori vektorskim zbrojem.

	**Skica:** da - podna zakrivljena ploha, zamišljeni volumen $V^*$, projekcija za $F_H$ i smjerovi komponenti.

6. **T3** Četvrtcilindrični poklopac polumjera $R = 0{,}75\ \text{m}$ i širine $b = 1{,}10\ \text{m}$ nalazi se tako da mu je gornja točka na dubini $h_1 = 0{,}45\ \text{m}$ ispod slobodne površine vode. Poklopac je zglobno vezan u gornjoj točki, a na donjem rubu pridržava ga vodoravna spojnica. Odredi horizontalnu komponentu sile, vertikalnu komponentu sile, iznos rezultante i silu spojnice potrebnu da poklopac ostane zatvoren.

	**Natuknica:** za $F_H$ koristi vertikalnu projekciju na dubini $h_1 + R/2$; za $F_V$ uzmi težinu imaginarnog volumena koji sada uključuje i pravokutni dio iznad četvrtine kruga; na kraju zatvori momente oko zgloba.

	**Skica:** da - četvrtcilindrični poklopac sa slobodnom površinom iznad njega, dubinom $h_1$, zglobom i spojnicom.
:::

![U06 zadaci za vježbu - minimalne grayscale tehničke skice uz zadatke.](../assets/print/u06_vjezbe_skice.svg)

::: {.mf1-zavrsni-okvir}
<p class="mf1-box-label">Za ponijeti iz poglavlja</p>

**Sažeta provjera prije računa**

- Treba jasno odvojiti koja se sila računa na ravnoj, a koja na zakrivljenoj plohi.
- Za horizontalnu komponentu treba koristiti projekciju, a ne stvarnu zakrivljenu površinu.
- Treba utvrditi nalazi li se zamišljeni volumen za $F_V$ ispod ili iznad slobodne površine.
- Prije momentne ravnoteže potrebno je točno odrediti gdje prolaze pravci djelovanja pojedinih sila.
- Treba provjeriti ima li dobivena vertikalna komponenta fizikalno smislen smjer.

**Najčešća pogreška**

Najčešća greška je mehanički pretpostaviti da je vertikalna komponenta na zakrivljenoj plohi uvijek prema gore. To vrijedi samo dok zamišljeni volumen koji definira $F_V$ stvarno predstavlja tekućinu ispod slobodne površine. Kad geometrija nametne podtlačni dio, smjer se mijenja.

**Nakon ovoga poglavlja mora biti moguće**

1. rastaviti silu na zakrivljenoj plohi na horizontalnu i vertikalnu komponentu.
2. koristiti projekciju za $F_H$ i zamišljeni volumen za $F_V$.
3. prevesti dobivene komponente u rezultantu ili u momentnu ravnotežu zatvarača.

**U tehnici to znači**

Na segmentnoj ustavi, zaobljenom poklopcu ili zakrivljenom brodskom otvoru nije presudno samo kolika je ukupna sila, nego kako je ona raspoređena po smjerovima. Horizontalna komponenta opterećuje oslonce drukčije od vertikalne, pa rastav sile izravno ulazi u čitanje reakcija, momenata i sigurnosti zatvarača.

**Granica modela**

Najveći rizik ovdje nije algebarska pogreška, nego pogrešan odabir zamišljenog volumena i smjera vertikalne komponente. Ako geometrija uključuje plinski jastuk, podtlak ili složeniju prostornu plohu, treba vrlo pažljivo provjeriti vrijedi li jednostavni 2D rastav bez dodatnih korekcija.

<span class="mf1-ch-ref"><span class="mf1-ch-code">U06</span><span class="mf1-ch-title">Zakrivljene plohe i rastav sila</span></span> nije poglavlje novih formula, nego novih pogleda na istu silu. Horizontalna komponenta čita projekciju, vertikalna težinu zamišljenog volumena, a najveći rizik nije algebra nego pogrešan smjer sile.
:::

::: {.mf1-numerika}
<p class="mf1-box-label">Numerički most</p>

**Gdje ovo živi u numerici.** Zakrivljene plohe su upravo razlog zašto CFD postoji kao alat. Za analitički nedostupne geometrije — segmentna ustava, vodena turbinska lopatica, krilo zrakoplova, brodski trup — više nije moguće rastavljati silu na ručne projekcije i zamišljene volumene. Numerika to radi *automatski*: za svaku ćeliju zna vektor površine $\vec{A}_i$ i tlak $p_i$, a sila je vektorska suma $\vec{F} = \sum_i p_i \vec{A}_i$.

**Što numerički alat radi s tim.** Mreža mora dobro razlučiti zakrivljenost — to je zadatak generatora mreže (`snappyHexMesh`, *Fluent meshing*). Što je veća krivina lokalno, to gušća mreža mora biti uz zid. Rezultati izlaze kao horizontalna, vertikalna i ukupna sila *izravno*, bez ručnog rastavljanja.

**Tipičan scenarij.** Krilo zrakoplova, lopatica turbine, propeler ili brodski trup imaju zakrivljenu mokru plohu na kojoj se ne može unaprijed napisati raspodjela tlaka. CFD daje cjelovito trodimenzijsko polje $p(x,y,z)$ na zidu, a integracijom po patchu istovremeno se dobivaju uzgon, otpor i moment — sve tri komponente bez ručnog rastavljanja na projekcije i imaginarne volumene.

**Alati u kojima se to susreće:** `OpenFOAM` (`snappyHexMesh`, `forces`, `forceCoeffs`) · `ANSYS Fluent` (*Fluent Meshing*, *Force Report*) · `Star-CCM+` (*Surface Wrapper*, *Force Reports*).

> *Nije gradivo MF1. Ono što se ovdje radi mukotrpno za segmentnu ustavu, CFD radi za bilo koju trodimenzijsku geometriju u istom potezu.*
:::







