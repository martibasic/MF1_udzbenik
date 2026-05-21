![U07 – Pregled poglavlja: uzgon, plivanje i stabilnost](../assets/print/u07_fig_uvod_pregled.svg){width="95%"}

## Uzgon kao spoj istisnine, težine i geometrije urona

Arhimedov zakon sam po sebi nije dovoljan za čitanje plivajućeg tijela.

Zato se već na početku razdvajaju tri stvari: ukupna težina, istisnuti volumen i momentni raspored tih sila.

::: {.mf1-application}
<p class="mf1-box-label">Inženjerski kontekst</p>

U brodogradnji, lučnim pontonima i plutajućim radnim platformama nije dovoljno znati samo koliko je vode istisnuto; jednako je važno gdje su težište i centar uzgona te kakav moment nastaje kad se teret pomakne. Zato ovo poglavlje izravno ulazi u stabilnost plovila, raspored opreme na pontonu, sigurnost plutajuće dizalice i svaku tehničku situaciju u kojoj mali bočni pomak tereta može otvoriti veliki nagib.
:::

## Fizikalni uvod i matematički izvod

Za tijelo koje miruje u fluidu vrijedi da je sila uzgona jednaka težini istisnutog fluida:

$$F_U = \rho g V$$

Za plivajuće tijelo u ravnoteži ta sila mora biti jednaka ukupnoj težini tijela i svih tereta na njemu. To je tek prvi korak. Drugi korak je geometrija: gdje djeluje težina, gdje djeluje uzgon i kakav moment nastaje ako je teret bočno pomaknut. Matematika zato mora odvojiti ukupni volumen istisnine od rasporeda sile i momenata, inače plivanje i nagib ostaju pomiješani u istoj brojci.

Kod prizmatskih tijela s ravnim dnom vrlo se često može odvojiti srednja uronjenost od nagiba:

- srednja uronjenost dolazi iz ukupne težine
- razlika urona po širini dolazi iz momentne ravnoteze

Ta razdvojenost je jezgra gotovo svih prvih zadataka plivanja i stabilnosti.

## Matematički izvod

Najjednostavniji put prema Arhimedovu zakonu polazi od potpuno uronjenoga prizmatičnog tijela vodoravne površine $A$. Na gornju plohu na dubini $h_1$ djeluje sila

$$
F_1 = p_1A = (p_0 + \rho gh_1)A
$$

prema dolje, a na donju plohu na dubini $h_2$ sila

$$
F_2 = p_2A = (p_0 + \rho gh_2)A
$$

prema gore. Neto vertikalna hidrostatska sila iznosi zato

$$
F_U = F_2 - F_1 = \rho g(h_2-h_1)A.
$$

Budući da je $(h_2-h_1)A = V_{ist}$, odnosno istisnuti volumen fluida, slijedi opći zapis uzgona

$$
F_U = \rho gV_{ist}.
$$

::: {.callout-note}
## 📐 Fizikalno značenje
Sila uzgona ne ovisi o obliku tijela, materijalu ni gustoći — ovisi isključivo o volumenu fluida koji tijelo istisne i gustoći tog fluida. Kilogram čelika i kilogram pluta istisnu isti volumen vode ako su iste veličine, pa imaju isti uzgon — ali čelik tone jer je teži od istisnute vode, a pluta pliva jer je lakši. Uzgon je uvijek vertikalan prema gore i prolazi kroz težište istisnutog volumena, a ne kroz težište samog tijela.
:::

Isti rezultat vrijedi i za proizvoljan oblik tijela: neto hidrostatska sila jednaka je težini fluida koji bi ispunio istisnuti volumen. Pravac djelovanja te sile prolazi kroz centar uzgona, tj. kroz težište istisnutoga volumena.

Iz toga odmah slijedi i prvo pravilo stabilnosti. Kod potpuno uronjenog tijela stabilan je položaj onaj u kojem je težište tijela $G$ ispod centra uzgona $B$; ako se te dvije točke poklope, ravnoteža je neutralna, a ako je $G$ iznad $B$, mali poremećaj daje prevrtni moment. Kod plivajućeg tijela slika je drukčija jer se pri malom nagibu oblik istisnutoga volumena mijenja, pa se i centar uzgona pomiče. Tada se uvodi metacentar $M$, a znak metacentarske visine $GM$ odlučuje o početnoj stabilnosti: $GM > 0$ znači povratni moment, $GM = 0$ neutralnu ravnotežu, a $GM < 0$ nestabilan položaj.

Za plivajuće tijelo vertikalna ravnoteža tada daje

$$
\rho gV_{ist} = G = mg
$$

odnosno

$$
V_{ist} = \frac{m}{\rho}.
$$

::: {.callout-note}
## 📐 Fizikalno značenje
Ova jednadžba kaže da plivajuće tijelo potapa se točno toliko da istisne svoju vlastitu masu fluida. Ako se teret doda, tijelo se potapa dublje; ako se teret ukloni, izroni. Volumen istisnine $V_{ist}$ nije fizička veličina tijela — on ovisi o gustoći fluida: isti brod u slanoj vodi (gustoća ~1025 kg/m³) istisne manji volumen nego u slatkoj vodi (~998 kg/m³), pa u slanoj vodi plovi nešto više.
:::

::: {.callout-note}
## 📝 Razrada koraka
Korak: od tlakova na gornju i donju plohu → $F_U = \rho g V_{ist}$

Na gornjoj plohi prizma na dubini $h_1$: $F_1 = (p_0 + \rho g h_1)A$ prema dolje.
Na donjoj plohi na dubini $h_2$: $F_2 = (p_0 + \rho g h_2)A$ prema gore.
Neto sila:
$$
F_U = F_2 - F_1 = \rho g(h_2 - h_1)A.
$$
Budući da je $(h_2 - h_1)A$ upravo volumen istisnine $V_{ist}$:
$$
F_U = \rho g V_{ist}.
$$
Jednolikni tlak $p_0$ potpuno se poniješta između gornje i donje plohe — zato uzgon ne ovisi o atmosferskom tlaku ni o apsolutnom tlaku u fluidu, nego samo o razlici dubina gornje i donje plohe.
:::

To je tek prvi dio fizikalne slike. Član $V_{ist}$ određuje koliko fluida mora biti istisnuto da bi se tijelo održalo na površini, ali ne određuje još i njegov nagib. Ako težište ukupne težine ne leži na istoj okomici kao centar uzgona, pojavljuje se moment koji tijelo zakreće. Zato za plivanje nisu dovoljne samo sile; mora biti zadovoljena i ravnoteža momenata.

Za pravokutnu platformu s linearnom promjenom urona po širini srednja uronjenost određena je vertikalnom ravnotežom, dok raspodjela urona po rubovima proizlazi iz momentne ravnoteže oko uzdužne osi. Upravo se tu vidi cjelovito značenje poglavlja: uzgon nije samo jedna brojka, nego rezultat istisnine, položaja centra uzgona i njihove geometrijske veze s ukupnom težinom sustava.

## Riješeni primjeri

::: {.mf1-we}
<p class="mf1-box-label">Riješeni primjer - Koliki gaz ima radni ponton pri simetričnom opterećenju <span class="mf1-level">T2</span></p>

**Zadano**

Pravokutni radni ponton duljine $L = 2{,}40\ \text{m}$, širine $B = 1{,}20\ \text{m}$ i ukupne visine boka $H = 0{,}32\ \text{m}$ ima vlastitu masu $m_p = 420\ \text{kg}$. Na njega se simetrično postavlja oprema mase $m_o = 180\ \text{kg}$. Ponton pluta u vodi gustoće $\rho = 998\ \text{kg/m}^3$.

**Traženo**

1. istisnuti volumen vode u ravnoteznom položaju.
2. srednji gaz pontona $h$.
3. koliku dodatnu masu još može primiti prije nego što gornji rub dođe do razine vode.

![U07 Val 2 - ponton i gaz pri simetričnom opterećenju](../assets/print/u07_val2_ponton_gaz.svg)

**Pretpostavke i model**

Kako je opterećenje postavljeno simetrično, ovdje nema bočnog nagiba ni momentne neravnoteze. Zadatak se zatvara samo vertikalnom ravnotezom: težina pontona i tereta mora biti jednaka uzgonu, odnosno težini istisnute vode.

**Rješenje**

Ukupna masa sustava iznosi

$$
m = m_p + m_o = 420 + 180 = 600\ \text{kg}
$$

Za plivanje u ravnotezi vrijedi

$$
\rho g V = mg
$$

pa je istisnuti volumen

$$
V = \frac{m}{\rho} = \frac{600}{998} = 0{,}601\ \text{m}^3
$$

Za pravokutni ponton vrijedi

$$
V = LBh
$$

odakle slijedi srednji gaz

$$
h = \frac{V}{LB} = \frac{0{,}601}{2{,}40 \cdot 1{,}20} = 0{,}209\ \text{m}
$$

odnosno

$$
h \approx 20{,}9\ \text{cm}
$$

granični slučaj prije zalijevanja palube dobiva se kad je uron jednak ukupnoj visini boka, tj. $h = H = 0{,}32\ \text{m}$. Tada je najveći mogući istisnuti volumen

$$
V_{max} = LBH = 2{,}40 \cdot 1{,}20 \cdot 0{,}32 = 0{,}922\ \text{m}^3
$$

pa odgovarajuća ukupna masa iznosi

$$
m_{max} = \rho V_{max} = 998 \cdot 0{,}922 \approx 920\ \text{kg}
$$

Zato je dodatna masa koju ponton još može primiti

$$
\Delta m = m_{max} - m = 920 - 600 = 320\ \text{kg}
$$

odnosno približno

$$
\Delta m \approx 3{,}2 \cdot 10^2\ \text{kg}
$$

**Provjera i komentar**

1. Veća ukupna masa mora značiti veći istisnuti volumen i veći gaz.
2. Dobiveni gaz mora biti manji od ukupne visine boka dok ponton još ima slobodni bok.
3. U simetričnom slučaju nema razloga za razliku urona lijevo i desno.
:::

 Kad je ta osnovna vertikalna ravnoteza zatvorena, korisno je najprije odvojiti još jedan međukorak: što sami rubni uroni govore o srednjem gazu i o bočnom pomaku centra uzgona, još bez traženja položaja tereta.

::: {.mf1-we}
<p class="mf1-box-label">Riješeni primjer - Bočni pomak centra uzgona iz rubnih urona <span class="mf1-level">T1</span></p>

**Zadano**

Pravokutna plutajuća platforma širine

$$
B = 1{,}20\ \text{m}
$$

ima izmjeren uron lijevog ruba

$$
h_L = 0{,}32\ \text{m}
$$

i uron desnog ruba

$$
h_D = 0{,}24\ \text{m}.
$$

Pretpostavi linearan nagib plivajućeg presjeka.

**Traženo**

1. srednji gaz platforme $h_m$.
2. bočni pomak centra uzgona $y_B$ od osi simetrije.

![Bočni pomak centra uzgona: B=1,20 m, h_L=0,32 m, h_D=0,24 m](../assets/print/u07_fig_bocni_pomak.svg){width="50%"}

**Pretpostavke i model**

Za pravokutnu platformu s linearnom promjenom urona srednji gaz dobiva se kao aritmetička sredina lijevog i desnog urona. Tek nakon toga bočni pomak centra uzgona slijedi iz geometrije nagnutog presjeka.

**Rješenje**

Srednji gaz iznosi

$$
h_m = \frac{h_L + h_D}{2} = \frac{0{,}32 + 0{,}24}{2} = 0{,}28\ \text{m}.
$$

Za pravokutnu platformu s linearnim nagibom bočni pomak centra uzgona glasi

$$
y_B = \frac{B(h_L - h_D)}{12h_m}
$$

odnosno

$$
y_B = \frac{1{,}20(0{,}32 - 0{,}24)}{12 \cdot 0{,}28} = 0{,}0286\ \text{m}.
$$

Dakle,

$$
y_B \approx 2{,}86\ \text{cm}
$$

prema dublje uronjenoj strani.

**Provjera i komentar**

1. Srednji gaz mora ležati između lijevog i desnog urona.
2. Centar uzgona mora se pomaknuti prema dublje uronjenoj strani.
3. Ako su rubni uroni jednaki, mora biti i $y_B = 0$.
:::

 Kad je taj geometrijski međukorak zatvoren, tek tada ima smisla prijeći na složeniji slučaj u kojem se teret bočno pomiče i uz ravnotezu sila treba zatvoriti i ravnotezu momenata.

::: {.mf1-we}
<p class="mf1-box-label">Riješeni primjer - Plutajuća servisna platforma s pomaknutim kompresorom <span class="mf1-level">T2</span></p>

**Zadano**

Pravokutna plutajuća servisna platforma duljine $L = 3{,}10\ \text{m}$ i širine $B = 1{,}00\ \text{m}$ ima masu $m_p = 676\ \text{kg}$ i pluta u vodi gustoće $\rho = 998\ \text{kg/m}^3$. Na platformu je postavljen prijenosni kompresor mase $m_k = 190\ \text{kg}$, ali nije poznato na kojoj se udaljenosti $e$ od uzdužne osi simetrije nalazi njegovo težište.

Nakon postavljanja kompresora izmjereno je da je uron lijevog ruba platforme $h_L = 0{,}34\ \text{m}$, a uron desnog ruba $h_D = 0{,}22\ \text{m}$. Pretpostavite da je platforma kruta, da joj je dno ravno, a bočne stijenke okomite.

**Traženo**

1. Odredite ukupni istisnuti volumen vode u ravnoteznom položaju.
2. Odredite udaljenost $e$ težišta kompresora od uzdužne osi simetrije platforme.
3. Odredite za koliko je srednja uronjenost platforme veća nego prije postavljanja kompresora.

![U07 Val 1 - plutajuća platforma s pomaknutim kompresorom](../assets/print/u07_val1_platforma_kompresor.svg)

**Pretpostavke i model**

Platforma se promatra kao kruto prizmatsko tijelo pravokutnog tlocrta i ravnog dna. Srednja uronjenost dobiva se iz aritmetičke sredine lijevog i desnog urona, a bočni pomak centra uzgona iz linearnog nagiba plivajućeg presjeka.

**Rješenje**

Srednja uronjenost iznosi

$$h_m = \frac{h_L + h_D}{2} = \frac{0{,}34 + 0{,}22}{2} = 0{,}28\ \text{m}$$

pa je istisnuti volumen

$$V = L B h_m = 3{,}10 \cdot 1{,}00 \cdot 0{,}28 = 0{,}868\ \text{m}^3$$

To odgovara istisnutoj masi vode od približno $998 \cdot 0{,}868 \approx 866\ \text{kg}$, što je u skladu s ukupnom masom platforme i kompresora.

Za pravokutnu platformu s linearnom promjenom urona po širini bočni pomak centra uzgona glasi

$$y_B = \frac{B(h_L - h_D)}{12h_m} = \frac{1{,}00\,(0{,}34 - 0{,}22)}{12 \cdot 0{,}28} = 0{,}0357\ \text{m}$$

Momentna ravnoteza oko uzdužne osi simetrije tada daje

$$F_U y_B = m_k g e$$

a kako je $F_U = (m_p + m_k)g$, slijedi

$$e = \frac{m_p + m_k}{m_k} y_B = \frac{676 + 190}{190} \cdot 0{,}0357 = 0{,}1628\ \text{m}$$

odnosno

$$e \approx 0{,}163\ \text{m}$$

Povećanje srednje uronjenosti nakon postavljanja kompresora uzrokuje samo njegova masa, pa je

$$\Delta h_m = \frac{m_k}{\rho L B} = \frac{190}{998 \cdot 3{,}10 \cdot 1{,}00} = 0{,}0614\ \text{m}$$

odnosno

$$\Delta h_m \approx 6{,}14\ \text{cm}$$

**Provjera i komentar**

1. Dublje uronjena strana mora biti ona na koju je kompresor pomaknut, a dobiveni rezultat to potvrduje.
2. Dobiveni pomak kompresora manji je od polovice širine platforme, pa je geometrijski moguć.
3. Povećanje srednjeg gaza reda nekoliko centimetara razumno je za dodatnih $190\ \text{kg}$ na ovakvoj platformi.
:::

Plutajuća platforma nije jedini tipičan ulaz u <span class="mf1-ch-ref"><span class="mf1-ch-code">U07</span><span class="mf1-ch-title">Uzgon, plivanje i stabilnost</span></span>. Jednako je važno znati zatvoriti vertikalnu ravnotezu i za potpuno uronjeno tijelo koje presiječa granicu dvaju fluida, jer se tada ukupni uzgon čita kao zbroj dviju istisnina različitih gustoća.

::: {.mf1-we}
<p class="mf1-box-label">Riješeni primjer - Kalibracijski modul na granici ulja i vode <span class="mf1-level">T2</span></p>

**Zadano**

Hermetički zatvoreni kalibracijski modul pravokutnog tlocrta ima dimenzije

$$
b = 0{,}32\ \text{m}, \qquad l = 0{,}20\ \text{m}, \qquad t = 0{,}22\ \text{m}
$$

**Traženo**

1. Odredite koliki dio visine modula mora biti u donjem, gušćem fluidu da modul bude neutralno uronjen.
2. Odredite silu koju mora prenijeti vodilica ako je modul pogrešno postavljen tako da je u donjem fluidu samo $x = 0{,}050\ \text{m}$ njegove visine.

![Kalibracijski modul na granici ulja i vode](../assets/print/u07_val3_dva_fluida_modul.svg){width="45%"}

**Pretpostavke i model**

Modul se promatra kao kruto tijelo stalnog poprečnog presjeka. Budući da je potpuno uronjen, slobodni bok i nagib ovdje nisu tema; cijeli zadatak zatvara se vertikalnom ravnotežom između težine i zbroja uzgona gornjeg i donjeg fluida.

**Rješenje**

Površina vodoravnog presjeka modula iznosi

$$
A = b l = 0{,}32 \cdot 0{,}20 = 0{,}064\ \text{m}^2
$$

Ako je `x` dio modula u donjem fluidu, tada je visina dijela u gornjem fluidu jednaka $t - x$. Za neutralnu vertikalnu ravnotezu mora vrijediti

$$
F_U = G
$$

odnosno

$$
\rho_1 g A (t - x) + \rho_2 g A x = mg
$$

Nakon skraćivanja s $g$ i uvrstavanja podataka dobiva se

$$
820 \cdot 0{,}064 \cdot (0{,}22 - x) + 1030 \cdot 0{,}064 \cdot x = 12{,}8
$$

što daje

$$
0{,}064 \left[820(0{,}22 - x) + 1030x\right] = 12{,}8
$$

pa slijedi

$$
820 \cdot 0{,}22 + (1030 - 820)x = \frac{12{,}8}{0{,}064}
$$

$$
180{,}4 + 210x = 200
$$

odakle je

$$
x = \frac{19{,}6}{210} = 0{,}0933\ \text{m}
$$

odnosno

$$
x \approx 9{,}33\ \text{cm}
$$

visina modula u gornjem fluidu tada je

$$
t - x = 0{,}22 - 0{,}0933 = 0{,}1267\ \text{m}
$$

odnosno približno

$$
t - x \approx 12{,}7\ \text{cm}
$$

Sada provjerimo pogrešno postavljen modul s visinom u donjem fluidu $x = 0{,}050\ \text{m}$. Tada je ukupni uzgon

$$
F_U = \rho_1 g A (0{,}22 - 0{,}05) + \rho_2 g A \cdot 0{,}05
$$

$$
F_U = 9{,}81 \cdot 0{,}064 \left(820 \cdot 0{,}17 + 1030 \cdot 0{,}05\right)
$$

$$
F_U \approx 119{,}9\ \text{N}
$$

Težina modula iznosi

$$
G = mg = 12{,}8 \cdot 9{,}81 \approx 125{,}6\ \text{N}
$$

Kako je $G > F_U$, vodilica mora prenijeti dodatnu silu prema gore:

$$
F_V = G - F_U = 125{,}6 - 119{,}9 = 5{,}7\ \text{N}
$$

Dakle,

$$
F_V \approx 5{,}7\ \text{N}
$$

prema gore.

**Provjera i komentar**

1. Dobivena vrijednost `x` mora biti između $0$ i ukupne visine $t$, što je ovdje zadovoljeno.
2. Kako je gustoće modula između $\rho_1$ i $\rho_2$, neutralni položaj mora stvarno presiječati granicu dvaju fluida.
3. Ako je dio modula u gušćem fluidu premalen, ukupni uzgon pada i vodilica mora preuzeti preostalu težinu prema gore.
:::

::: {.mf1-ch}
<p class="mf1-box-label">Cjeloviti zadatak - Plutajuća servisna platforma na granici ulja i vode <span class="mf1-level">T4</span></p>

**Zadano**

Hermetički zatvorena pravokutna servisna platforma duljine

$$
L = 3{,}00\ \text{m}
$$

i širine

$$
B = 1{,}20\ \text{m}
$$

ima visinu boka

$$
H = 0{,}34\ \text{m}
$$

i vlastitu masu

$$
m_p = 648\ \text{kg}
$$

Platforma pluta u separacijskom spremniku koji ima gornji sloj ulja gustoće

$$
\rho_o = 800\ \text{kg/m}^3
$$

debljine

$$
\delta = 0{,}10\ \text{m}
$$

i donji sloj vode gustoće

$$
\rho_w = 1000\ \text{kg/m}^3
$$

Na platformu je postavljen ormar instrumentacije mase

$$
m_k = 180\ \text{kg}
$$

na nepoznatoj udaljenosti $e$ od uzdužne osi simetrije. Nakon postavljanja ormara izmjereni su uroni lijevog i desnog ruba platforme, mjerene od slobodne površine ulja:

$$
h_L = 0{,}30\ \text{m}, \qquad h_D = 0{,}20\ \text{m}
$$

Pretpostavi da je platforma kruta, da su bočne stijenke okomite, da je dno ravno i da je promjena urona po širini linearna.

**Traženo**

1. srednji uron $h_m$ i ukupni istisnuti volumen $V$.
2. koliki se dio istisnine nalazi u ulju, a koliki u vodi.
3. bočni pomak rezultantnog centra uzgona $y_B$.
4. udaljenost $e$ težišta ormara od osi simetrije platforme.
5. za koliko je srednja uronjenost veća nego prije postavljanja ormara.

![U07 CH 1 - plutajuća platforma na granici ulja i vode](../assets/print/u07_ch1_platforma_ulje_voda_ormar.svg)

**Pretpostavke i model**

Ovdje se platforma još uvijek čita kao prizmatsko tijelo, ali uzgon više ne dolazi iz jedne jedine gustoće. Gornji uljni sloj daje simetrični doprinos uzgonu, dok donji vodeni dio nosi i preostalu vertikalnu ravnotezu i bočni pomak centra uzgona pri nagibu. Zato se najprije mora zatvoriti podjela istisnine po fluidima, a tek zatim momentna ravnoteza s pomaknutim teretom.

**Rješenje**

Srednja uronjenost dobiva se iz sredine izmjerenih rubnih urona:

$$
h_m = \frac{h_L + h_D}{2} = \frac{0{,}30 + 0{,}20}{2} = 0{,}25\ \text{m}
$$

Ukupni istisnuti volumen zato je

$$
V = L B h_m = 3{,}00 \cdot 1{,}20 \cdot 0{,}25 = 0{,}900\ \text{m}^3
$$

Kako su oba ruba uronjena više od debljine uljnog sloja, cijela platforma kroz puni tlocrt presiječa svih

$$
\delta = 0{,}10\ \text{m}
$$

ulja. Zato je volumen istisnine u ulju

$$
V_o = L B \delta = 3{,}00 \cdot 1{,}20 \cdot 0{,}10 = 0{,}360\ \text{m}^3
$$

a volumen istisnine u vodi

$$
V_w = L B (h_m - \delta) = 3{,}00 \cdot 1{,}20 \cdot (0{,}25 - 0{,}10) = 0{,}540\ \text{m}^3
$$

Provjera vertikalne ravnoteze sada glasi

$$
\rho_o V_o + \rho_w V_w = 800 \cdot 0{,}360 + 1000 \cdot 0{,}540 = 288 + 540 = 828\ \text{kg}
$$

što se točno slaže s ukupnom masom sustava

$$
m_p + m_k = 648 + 180 = 828\ \text{kg}
$$

Dakle, vertikalna ravnoteza je zatvorena.

Za bočni pomak centra uzgona bitan je samo vodeni dio ispod granice fluida, jer je uljni dio simetričan po širini i ne daje bočni moment. Vodene dubine lijevo i desno iznose

$$
h_{w,L} = h_L - \delta = 0{,}30 - 0{,}10 = 0{,}20\ \text{m}
$$

$$
h_{w,D} = h_D - \delta = 0{,}20 - 0{,}10 = 0{,}10\ \text{m}
$$

pa je srednja vodena dubina

$$
h_{w,m} = h_m - \delta = 0{,}15\ \text{m}
$$

Centar uzgona vodenog dijela za linearni nagib pravokutnog presjeka nalazi se na udaljenosti

$$
y_{B,w} = \frac{B(h_{w,L} - h_{w,D})}{12 h_{w,m}} = \frac{1{,}20(0{,}20 - 0{,}10)}{12 \cdot 0{,}15} = 0{,}0667\ \text{m}
$$

od osi simetrije platforme, prema dublje uronjenoj strani.

Kako je samo vodeni dio asimetričan, rezultantni bočni pomak ukupnog centra uzgona dobiva se težinjenjem po uzgonskim doprinosima:

$$
y_B = \frac{\rho_w V_w}{\rho_o V_o + \rho_w V_w} y_{B,w} = \frac{540}{828} \cdot 0{,}0667 = 0{,}0435\ \text{m}
$$

odnosno

$$
y_B \approx 4{,}35\ \text{cm}
$$

Momentna ravnoteza oko uzdužne osi simetrije sada daje

$$
(m_p + m_k) g y_B = m_k g e
$$

odakle slijedi

$$
e = \frac{m_p + m_k}{m_k} y_B = \frac{828}{180} \cdot 0{,}0435 = 0{,}200\ \text{m}
$$

odnosno

$$
e = 20{,}0\ \text{cm}
$$

Prije postavljanja ormara platforma je bila simetrično opterećena, pa je i tada bila u ravnotezi bez nagiba. Neka je tadašnji srednji uron $h_0$. Budući da je uljni sloj i dalje potpuno presijecao platformu, vrijedi

$$
\rho_o L B \delta + \rho_w L B (h_0 - \delta) = m_p
$$

odnosno

$$
800 \cdot 3{,}00 \cdot 1{,}20 \cdot 0{,}10 + 1000 \cdot 3{,}00 \cdot 1{,}20 \cdot (h_0 - 0{,}10) = 648
$$

što daje

$$
288 + 3600(h_0 - 0{,}10) = 648
$$

pa je

$$
h_0 = 0{,}20\ \text{m}
$$

Povećanje srednje uronjenosti nakon postavljanja ormara zato iznosi

$$
\Delta h_m = h_m - h_0 = 0{,}25 - 0{,}20 = 0{,}05\ \text{m}
$$

odnosno

$$
\Delta h_m = 5{,}0\ \text{cm}
$$

**Provjera i komentar**

Ovaj `CH` zatvara tri jezgre <span class="mf1-ch-ref"><span class="mf1-ch-code">U07</span><span class="mf1-ch-title">Uzgon, plivanje i stabilnost</span></span> u jednom zadatku: srednji uron platforme je $0{,}25\ \text{m}$, ukupna istisnina iznosi $0{,}900\ \text{m}^3$, od čega je $0{,}360\ \text{m}^3$ u ulju, a $0{,}540\ \text{m}^3$ u vodi. Rezultantni centar uzgona pomaknut je oko $4{,}35\ \text{cm}$ prema dubljoj strani, pa ormar mora biti postavljen oko $20\ \text{cm}$ od osi simetrije. Njegovo postavljanje povećalo je srednji uron za $5\ \text{cm}$.

1. Srednji uron mora biti između izmjerenih rubnih urona i manji od visine boka, što ovdje vrijedi.
2. Dublje uronjena strana mora biti ona na koju je pomaknut ormar, pa znak momenta mora biti fizikalno smislen.
3. Dobiveni pomak ormara mora biti manji od polovice širine platforme; ovdje je $e = 0{,}20\ \text{m} < B/2 = 0{,}60\ \text{m}$.
:::

::: {.mf1-we}
<p class="mf1-box-label">Riješeni primjer – Uzgon na potonulo pumpno kućište pri ispitivanju &nbsp;<span class="mf1-level">T2</span></p>

🔩 **Primjer za strojare**

**Kontekst:** Pumpa u podvodnom prihvatnom bazenu ima čelično kućište koje se ispravlja ronjenjem. Serviseri trebaju znati koliku tegežu (lančanu vezu prema dnu) trebaju koristiti da kućište ostane na dnu dok se montira priključak.

**Zadano**

- Volumen kućišta pumpe: $V = 0{,}045\ \text{m}^3$
- Masa kućišta: $m = 85\ \text{kg}$
- Gustoća morske vode: $\rho = 1025\ \text{kg/m}^3$

**Traženo**

1. Sila uzgona na kućište.
2. Neto sila i potrebna tegeba (sila držanja prema dnu).

![Potonulo pumpno kućište: uzgon i neto sila](../assets/print/u07_fig_pumpno_kuciste.svg){width="40%"}

**Rješenje**

$$
F_U = \rho g V = 1025 \cdot 9{,}81 \cdot 0{,}045 = 452{,}5\ \text{N} \approx 0{,}453\ \text{kN}
$$

Težina kućišta:
$$
G = mg = 85 \cdot 9{,}81 = 833{,}9\ \text{N} \approx 0{,}834\ \text{kN}
$$

Neto sila (prema dolje, kućište tone samo):
$$
F_{neto} = G - F_U = 833{,}9 - 452{,}5 = 381{,}4\ \text{N}
$$

Kućište se samo potapa — nema potrebe za tegebom; ali ronioci trebaju silu od ~381 N za podizanje kućišta na površinu.

**Provjera i komentar**

Gustoća čelika (~7850 kg/m³) >> gustoća morske vode, pa je potpuno uronjeno čelično kućište uvijek teže od istisnute vode. Uzgon ($452\ \text{N}$) ipak znatno olakšava podizanje — bez uzgona trebalo bi podici 834 N, a uz uzgon samo 381 N. U dubokim bazinima sa slojima različite slanosti gustoća se mijenja s dubinom, pa se uzgon mijenja za svaki metar.

:::

::: {.mf1-we}
<p class="mf1-box-label">Riješeni primjer – Gaz i nagib priveznog pontona za plovni put &nbsp;<span class="mf1-level">T2</span></p>

🏗️ **Primjer za građevinare**

**Kontekst:** Privezni ponton za brodove na rijeci dimenzionira se za vlastitu težinu plus težinu servisnog čelika. Projektant provjerava gaz i ima li nesimetrično postavljena servisna oprema prekomjeran bočni nagib.

**Zadano**

- Dimenzije pontona: $L = 6{,}00\ \text{m}$, $B = 2{,}40\ \text{m}$, visina boka $H = 0{,}60\ \text{m}$
- Vlastita masa: $m_p = 1800\ \text{kg}$
- Servisna oprema masa: $m_o = 600\ \text{kg}$, postavljena $e = 0{,}60\ \text{m}$ od osi simetrije
- Gustoća: $\rho = 998\ \text{kg/m}^3$

**Traženo**

1. Srednji gaz.
2. Bočni nagib (razlika urona s jedne i druge strane).

![Privezni ponton s pomaknutom opremom: gaz i bočni nagib](../assets/print/u07_fig_ponton_nagib.svg){width="55%"}

**Pretpostavke i model**

Vertikalna ravnoteža → srednji gaz. Momentna ravnoteža oko uzdužne osi → nagib.

**Rješenje**

Ukupna masa: $m = 1800 + 600 = 2400\ \text{kg}$

$$
h_{sr} = \frac{m}{\rho L B} = \frac{2400}{998 \cdot 6{,}00 \cdot 2{,}40} = \frac{2400}{14371} = 0{,}167\ \text{m}
$$

Moment opreme oko osi: $M = m_o \cdot g \cdot e = 600 \cdot 9{,}81 \cdot 0{,}60 = 3531{,}6\ \text{N\,m}$

Uzgonski moment otpora (za linearni nagib): $M_U = \rho g L h_{sr} \cdot \frac{B^2}{6} = 998 \cdot 9{,}81 \cdot 6{,}00 \cdot 0{,}167 \cdot \frac{2{,}40^2}{6}$

Razlika urona između strana:
$$
\Delta h = \frac{m_o \cdot e}{\rho \cdot L \cdot B^2 / 6} \cdot \frac{B}{2}... \approx \frac{6 m_o e}{\rho L B^2} = \frac{6 \cdot 600 \cdot 0{,}60}{998 \cdot 6{,}00 \cdot 5{,}76} = \frac{2160}{34507} = 0{,}0626\ \text{m}
$$

Ponton se naginje ~6,3 cm na stranu tereta.

**Provjera i komentar**

Srednji gaz $16{,}7\ \text{cm}$ od visine boka $60\ \text{cm}$ — ponton ima dovoljno rezerve nebouka. Nagib $6{,}3\ \text{cm}$ je prihvatljiv (< 5° u ovom slučaju) ali bi se trebao projektno ograničiti na max ~3 cm za udobnost pješačke komunikacije. Postavljanjem opreme simetričnije ili dodavanjem protutereta nagib se eliminira.

:::

## Usporedna tablica: strojarstvo i građevinarstvo

| Koncept | Strojarstvo – gdje se pojavljuje | Građevinarstvo – gdje se pojavljuje |
|---------|----------------------------------|--------------------------------------|
| $F_U = \rho g V_{ist}$ | Uzgon na pumpu u bazenu; olakšanje pri izvlačenju cilindra iz vode | Uzgon na temelje i podrumske ploče ispod razine podzemnih voda; sila na pilote |
| Ravnoteža $\rho g V_{ist} = mg$ | Gaz plivajućeg posude s opremom; regulacija plovnosti podmornicy | Gaz plovnog mosnog stupa; uporedbena dubina pontona lučnog skele |
| Nesimetrično opterećenje | Bočni nagib pontona s ekscentričnom pumpom; stabilnost plutajuće dizalice | Nagib priveznog pontona s ekscentričnom opremom; nagibi plovne platforme vodogradnje |
| Stabilnost: $GM > 0$ | Provjera stabilnosti plovne procesne opreme pri ekscentričnom teretu | Provjera nagiba pontona ili plovnog skele pri nesimetričnom rasporedu tereta |
| Višeslojni fluidi | Uzgon na tijelo koje se dijelom nalazi u ulju, dijelom u vodi | Uzgon na pilote ili podrumske ploče u slojevitom tlu s vodom i blatoviom |

## Zadaci za vježbu

::: {.mf1-vjezbe-list}
1. **T1** Hermetički zatvoreno tijelo volumena $V = 0{,}085\ \text{m}^3$ i mase $m = 62\ \text{kg}$ potpuno je uronjeno u vodu gustoće $\rho = 998\ \text{kg/m}^3$. Odredi silu uzgona i silu koju treba primijeniti da tijelo ostane potpuno uronjeno i u mirovanju.

	**Natuknica:** uzgon je $F_U = \rho gV$; potom usporedi $F_U$ i težinu $G = mg$ da dobiješ potrebnu dodatnu silu.

	**Skica:** da - potpuno uronjeni blok, volumen $V$, smjerovi $F_U$, $G$ i dodatne sile držanja.

2. **T1** Pravokutni radni ponton duljine $L = 2{,}60\ \text{m}$, širine $B = 1{,}40\ \text{m}$ i visine boka $H = 0{,}38\ \text{m}$ ima vlastitu masu $m_p = 510\ \text{kg}$. Na njega se simetrično postavlja teret mase $m_t = 220\ \text{kg}$. Ponton pluta u vodi gustoće $\rho = 998\ \text{kg/m}^3$. Odredi istisnuti volumen, srednji gaz i preostalu dodatnu masu koju ponton može primiti prije nego što rub boka dođe do razine vode.

	**Natuknica:** iz vertikalne ravnoteže vrijedi $\rho gV_{ist} = (m_p + m_t)g$; srednji gaz slijedi iz $V_{ist} = LBh$.

	**Skica:** da - ponton pravokutnog presjeka, srednji gaz $h$ i slobodni bok $H-h$.

3. **T2** Plutajuća servisna platforma duljine $L = 2{,}20\ \text{m}$ i širine $B = 1{,}00\ \text{m}$ ima ukupnu masu s opremom $m = 560\ \text{kg}$. Kompresor mase $85\ \text{kg}$ pomakne se za $e = 0{,}24\ \text{m}$ udesno od središnje osi. Ako platforma pluta u vodi i ostaje u linearnom režimu malog nagiba, odredi srednji gaz te razliku urona lijevoga i desnoga ruba.

	**Natuknica:** srednji gaz dolazi iz ukupne težine, a razlika urona iz momentne ravnoteže oko uzdužne osi; ne miješaj te dvije jednadžbe.

	**Skica:** da - platforma, pomaknuti kompresor, lijevi i desni uron te širina $B$.

4. **T2** Areometar mase $m = 0{,}085\ \text{kg}$ s cilindričnim vratom promjera $d = 8\ \text{mm}$ pluta tako da mu je u vodi uronjena duljina $h_1 = 82\ \text{mm}$, a u nepoznatom ulju $h_2 = 95\ \text{mm}$. Odredi gustoću ulja i protumači zašto je uron u ulju veći nego u vodi.

	**Natuknica:** u oba fluida vrijedi $\rho gV_{ist} = mg$; razlika je samo u uronjenom volumenu vrata i tijela areometra.

	**Skica:** da - areometar s cilindričnim vratom i dvije razine urona $h_1$, $h_2$.

5. **T3** Plutajući modul istiskuje volumen vode $V_{ist} = 0{,}62\ \text{m}^3$ i ima metacentarsku visinu $GM = 0{,}18\ \text{m}$. Ako se pri malom nagibu zakrene za $\varphi = 7^\circ$, odredi povratni moment stabilnosti i procijeni je li ravnoteža stabilna.

	**Natuknica:** deplasman je $\Delta = \rho gV_{ist}$, a za male nagibe povratni moment je $M_r = \Delta GM\sin\varphi$; znak $GM$ odlučuje o stabilnosti.

	**Skica:** da - presjek tijela s težištem, metacentrom, nagibom $\varphi$ i ramenom povratnog momenta.

6. **T3** Pravokutna servisna platforma duljine $L = 2{,}80\ \text{m}$ i širine $B = 1{,}20\ \text{m}$ pluta na granici ulja gustoće $\rho_o = 820\ \text{kg/m}^3$ debljine $\delta = 0{,}08\ \text{m}$ i vode gustoće $\rho_w = 998\ \text{kg/m}^3$. Nakon pomaka akumulatora lijevi rub uronjen je $h_L = 0{,}26\ \text{m}$, a desni $h_D = 0{,}18\ \text{m}$. Ukupna masa platforme s opremom je $640\ \text{kg}$, od čega akumulator ima $70\ \text{kg}$. Odredi srednji uron, volumene istisnine u ulju i vodi, bočni pomak centra uzgona i udaljenost akumulatora od osi simetrije platforme.

	**Natuknica:** najprije uzmi $h_m = (h_L + h_D)/2$, podijeli istisninu na uljni i vodeni dio preko granice $\delta$, zatim iz linearnog nagiba vrati bočni pomak centra uzgona i zatvori momentnu ravnotežu s pomaknutim akumulatorom.

	**Skica:** da - platforma na granici ulja i vode, rubni uroni $h_L$ i $h_D$, granica fluida i bočni pomak akumulatora.
:::

![U07 zadaci za vježbu - minimalne grayscale tehničke skice uz zadatke.](../assets/print/u07_vjezbe_skice.svg)

::: {.mf1-zavrsni-okvir}
<p class="mf1-box-label">Za ponijeti iz poglavlja</p>

**Sažeta provjera prije računa**

- Treba razdvojiti ukupni istisnuti volumen od raspodjele tog volumena po širini tijela.
- Srednju uronjenost treba računati iz ukupne težine, a ne iz momentne ravnoteže.
- Prije pisanja znakova u momentima treba jasno odrediti na koju je stranu pomaknut teret.
- Treba provjeriti koristi li se isti koordinatni smjer za položaj težine i za položaj centra uzgona.
- Treba provjeriti je li dobiveni pomak tereta uopće geometrijski moguć.

**Najčešća pogreška**

Najčešća greška je pokušati iz razlike urona odmah dobiti ukupni volumen istisnine. Razlika urona govori o nagibu i momentnoj ravnoteži, dok ukupni volumen najprije dolazi iz srednje uronjenosti i ukupne težine.

**Nakon ovoga poglavlja mora biti moguće**

1. povezati Arhimedov zakon s realnim istisnutim volumenom.
2. odvojiti ravnotežu vertikalnih sila od ravnoteže momenata plivajućeg tijela.
3. iz geometrije urona pročitati što govori o težištu tereta, a što o ukupnoj težini.

**U tehnici to znači**

Ponton, plutajuća dizalica ili radna platforma mogu zadovoljiti uvjet uzgona, a ipak ostati loše raspoređeni i skloni nagibu. Zato ovo poglavlje izravno ulazi u raspored tereta, procjenu gaza i sigurnost plovila ili plutajuće konstrukcije pri stvarnom opterećenju.

**Granica modela**

Ovdje se promatra statička ravnoteža ili mala odstupanja od nje. U valovima, pri slobodnoj površini unutar spremnika ili pri većim kutovima nagiba stvarna stabilnost može biti bitno drukčija od slike dobivene iz jednostavne ravnoteže sila i momenata.

<span class="mf1-ch-ref"><span class="mf1-ch-code">U07</span><span class="mf1-ch-title">Uzgon, plivanje i stabilnost</span></span> lomi se na dvije stabilne navike: uzgon uvijek dolazi iz istisnine, a nagib iz momenta. Miješanje te dvije stvari gotovo sigurno ruši fizikalni smisao zadatka.
:::







