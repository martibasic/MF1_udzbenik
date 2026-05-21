![Pregled poglavlja 13: cjevovodi](../assets/print/u13_fig_uvod_pregled.svg){#fig-uvod-u13 fig-align="center"}

Jedan cjevovod ovdje zatvara gotovo cijeli kolegij.

<span class="mf1-ch-ref"><span class="mf1-ch-code">U13</span><span class="mf1-ch-title">Cjevovodi</span></span> nije samo još jedno poglavlje o gubicima. U cjevovodima se na jednom mjestu spajaju kontinuitet, realni Bernoulli, izbor modela trenja i logika spajanja više grana. Zato cjevovodni zadatak vrlo brzo otkrije je li redoslijed modeliranja doista razumljen ili se samo prepoznaju pojedine formule.

::: {.mf1-application}
<p class="mf1-box-label">Inženjerski kontekst</p>

Cjevovodi su stvarni završetak kolegija jer se u njima na jednom mjestu sastaju izbor promjera, Reynoldsov broj, trenje, lokalni gubici i raspodjela protoka po mreži. Takav se račun svakodnevno pojavljuje u industrijskim vodovima, brodskim rashladnim i balastnim mrežama, hidrantskim granama, kotlovnicama i rashladnim krugovima vozila, gdje pogrešan redoslijed modeliranja brzo znači pogrešnu radnu točku sustava.
:::

## Fizikalni uvod i matematički izvod

U cjevovodima se račun ne smije početi od Darcy-Weisbacha ili Moodyjeva dijagrama naslijepo. Redoslijed mora biti strogo zatvoren: iz geometrije i protoka najprije se dobiva brzina, iz brzine i promjera Reynoldsov broj, a tek nakon toga koeficijent trenja i gubitci. Taj redoslijed nije administrativna disciplina, nego fizikalna nužnost: bez brzine nema režima strujanja, a bez režima nema ni vjerodostojnoga otpora cijevi. Temeljna veza između protoka i srednje brzine jest

$$
v = \frac{Q}{A},
$$

pa iz nje odmah slijedi Reynoldsov broj

$$
Re = \frac{\rho vD}{\mu} = \frac{vD}{\nu}.
$$

Taj broj nije samo klasifikacijska oznaka: on pokazuje dominira li u cijevi uređeno viskozno strujanje ili razvijena turbulencija. U laminarnom području otpor proizlazi izravno iz viskoznoga mehanizma, pa vrijedi

$$
\lambda = \frac{64}{Re},
$$

dok u turbulentnom području $\lambda$ više ne ovisi samo o $Re$, nego i o relativnoj hrapavosti, pa se čita iz Moodyjeva dijagrama ili iz odgovarajuće aproksimacije.

::: {.callout-note}
## 📝 Razrada koraka
Korak: od geometrije i protoka → $Re$ → $\lambda$ → $h_w$ (redoslijed koji se ne smije preskočiti)

**1. Brzina iz protoka:**
$$v = \frac{Q}{A} = \frac{Q}{\pi D^2/4} = \frac{4Q}{\pi D^2}.$$

**2. Reynoldsov broj:**
$$Re = \frac{vD}{\nu}.$$
Ako $Re < 2300$ → laminarno; ako $Re > 4000$ → turbulentno.

**3. Koeficijent trenja:**
- Laminarno: $\lambda = 64/Re$ (egzaktno, bez dijagrama).
- Turbulentno (razvijeno, hrapave cijevi): Colebrook-Whiteova jednadžba ili Moodijev dijagram s $\varepsilon/D$ i $Re$.
- Turbulentno hidraulički glatke: Blaziusova aproksimacija $\lambda \approx 0{,}316\, Re^{-1/4}$ za $Re < 10^5$.

**4. Linijski gubitak:**
$$h_f = \lambda \frac{L}{D}\frac{v^2}{2g}.$$

**5. Lokalni gubici (suma):**
$$h_{loc} = \sum \xi \frac{v^2}{2g}.$$

**6. Ukupni gubitak:**
$$h_w = h_f + h_{loc}.$$

Tipična greška: korak 3 se pogodi (npr. $\lambda = 0{,}02$ po osjećaju) bez provjere $Re$ i $\varepsilon/D$. To vodi na pogrešnu radnu točku, posebno pri promjeni protoka.
:::

Kad je koeficijent trenja određen, ukupna energijska bilanca između presjeka $A$ i $B$ piše se kao

$$
H_A + h_p - h_t = H_B + h_w,
$$

pri čemu je ukupna specifična mehanička energija fluida

$$
H = \frac{p_M}{\rho g} + z + \alpha\frac{v^2}{2g},
$$

a gubitci se rastavljaju na linijski i lokalni dio

$$
h_w = \lambda \frac{L}{D}\frac{v^2}{2g} + \sum \xi \frac{v^2}{2g}.
$$

::: {.callout-note}
## 📐 Fizikalno značenje
Darcy-Weisbachov linijski gubitak $\lambda (L/D)(v^2/2g)$ govori da je energijski trošak trenja proporcionalan duljini, obrnutno proporcionalan promjeru i kvadratno ovisi o brzini. Udvostručenjem promjera uz isti protok brzina se smanjuje četiri puta, a gubitak šesnaest puta — to je razlog zašto se za duljine transportnih vodova biraju što veći promjeri. Lokalni gubitak $\xi v^2/2g$ opisuje disipaciju u elementima poput ventila, koljena i T-račvi: $\xi$ sažima svu geometrijsku složenost u jednu bezdimenzijsku konstantu, a korisnik treba samo brzinu u referentnom presjeku.
:::

U tim je zapisima $p_M/(\rho g)$ tlačna visina, $z$ geodetska visina, $\alpha v^2/(2g)$ koregirana brzinska visina, $h_p$ energija koju u sustav unosi crpka, $h_t$ energija koju oduzima turbina, a $h_w$ nepovratno izgubljena mehanička energija zbog trenja, vrtloženja i lokalnih poremećaja strujanja. Tako se prvi put potpuno jasno vidi da "gubitci" nisu sporedna korekcija nego glavni jezik sustava: svaki član govori gdje energija još postoji, a gdje je već izgubljena.

Kad se cjevovod grana, energijska jednadžba više nije dovoljna sama. Tada se moraju zatvoriti i topološka pravila mreže. U čvoru vrijedi bilanca protoka

$$
Q = \sum_i Q_i,
$$

a za paralelne grane između istih čvorova mora vrijediti jednak pad ukupne energije

$$
h_{w,1}(Q_1) = h_{w,2}(Q_2) = \dots
$$

Razlog nije proizvoljno pravilo nego činjenica da obje grane polaze iz istoga uzvodnog čvora i završavaju u istome nizvodnom čvoru. To znači da je ukupna energijska visina na početku svake grane ista, a ista mora biti i na njezinu kraju. Zato ni pad energije između ta dva čvora ne može biti različit po granama. Kad bi jedna grana između istih čvorova trošila manji $h_w$ od druge, to bi značilo da bi na zajedničkom nizvodnom čvoru dvije grane završavale s različitom energijskom visinom, što je fizikalno nemoguće za isti čvor.

Zato se u paraleli ne izjednačava protok nego se protok sam raspodjeljuje tako da svaka grana, sa svojom vlastitom geometrijom i otporom, "sjedne" na isti zajednički pad energije. Upravo je to razlog zašto šira ili hidraulički povoljnija grana spontano preuzima veći dio ukupnog protoka: ne zato što joj je propisan veći protok, nego zato što na istom dopuštenom padu energije može propustiti više tekućine.

::: {.callout-note}
## 📐 Fizikalno značenje
U paralelnoj mreži postoji jedan "budžet" energije između dvaju čvorova: sva grana mora trošiti taj isti iznos $h_w$. Grana s manjim otporom (veći promjer, manja hrapavost, manji lokalni gubici) može pri tom padu energije propustiti više tekućine. Zato je dodavanje nove grane paralelno uvijek smanjenje ukupnog otpora mreže — poput otpora u paralelnoj el. mreži. U serijskom spoju vrijedi suprotno: svaka nova dionica dodaje otpor, a protok ostaje isti kroz sve. Tu analogiju s el. kolom vrijedi imati u glavi pri svakom proračunu mreže.
:::

To je glavni fizikalni smisao mreže: u seriji svi dijelovi nose isti protok, a u paraleli sve grane "plaćaju" isti pad ukupne energije između zajedničkih čvorova. Zbog toga svaka promjena promjera, hrapavosti, otvora ventila ili nove grane odmah mijenja radnu točku cijeloga sustava.

U <span class="mf1-ch-ref"><span class="mf1-ch-code">U10</span><span class="mf1-ch-title">Realni Bernoulli i gubici</span></span> već je bilo jasno da realni fluid troši energiju. U <span class="mf1-ch-ref"><span class="mf1-ch-code">U13</span><span class="mf1-ch-title">Cjevovodi</span></span> ta se slika širi na cijeli sustav dionica i čvorova, pa redoslijed modeliranja mora ostati stabilan: najprije mreža i dionice, zatim brzina i Reynoldsov broj, pa tek onda $\lambda$ i ukupni gubitci.

Zato u serijskom spoju isti protok prolazi kroz sve dionice, a u paralelnom je između istih čvorova jednak pad ukupne energije.

Tu nastaje najčešća zabuna: u seriji je isti $Q$, a u paraleli isti $h_w$. Tko to pomiješa, može dobiti račun koji je numerički uredan, ali fizikalno nemoguć.

Zato se većina osnovnih cjevovodnih zadataka može svesti na tri tipa: za zadanu geometriju i protok treba odrediti gubitak, za zadanu geometriju i raspoloživu energijsku visinu treba odrediti protok, a za zadani protok i dopušteni gubitak treba odabrati potreban promjer. Ta podjela ne uvodi novu fiziku, ali pomaže da se odmah prepozna što je poznato, što je nepoznato i gdje će račun biti izravan, a gdje iterativan.

## Riješeni primjeri

::: {.mf1-we}
<p class="mf1-box-label">Riješeni primjer - Od Reynoldsovog broja do ukupnog gubitka u jednoj dionici <span class="mf1-level">T2</span></p>

**Zadatak**

Voda struji cijevi promjera $D = 0{,}09\ \text{m}$ protokom $Q = 0{,}018\ \text{m}^3/\text{s}$. Duljina cijevi je $L = 42\ \text{m}$, apsolutna hrapavost $\varepsilon = 0{,}15\ \text{mm}$, a zbroj lokalnih koeficijenata iznosi $\sum \xi = 5{,}2$. Kinematička viskoznost vode je $\nu = 1{,}0 \cdot 10^{-6}\ \text{m}^2/\text{s}$. Moodyjev dijagram za dobiveni $Re$ i $\varepsilon / D$ daje približno $\lambda \approx 0{,}027$.

Odredi:

1. srednju brzinu strujanja.
2. Reynoldsov broj i režim strujanja.
3. ukupni gubitak energije $h_w$.

![U13 Val 1 - cjevovod, Reynolds i gubici](../assets/print/u13_val1_reynolds_i_gubici.svg)

**Pretpostavke i model**

Promatra se jedna dionica cjevovoda s poznatim protokom. Najprije treba zatvoriti geometriju i brzinu, zatim iz Reynoldsovog broja odrediti režim strujanja, a tek onda prihvatiti vrijednost $\lambda$ i složiti ukupne gubitke.

**Rješenje**

Površina presjeka cijevi iznosi

$$
A = \frac{\pi D^2}{4} = \frac{\pi \cdot 0{,}09^2}{4} \approx 6{,}36 \cdot 10^{-3}\ \text{m}^2
$$

pa je srednja brzina strujanja

$$
v = \frac{Q}{A} = \frac{0{,}018}{6{,}36 \cdot 10^{-3}} \approx 2{,}83\ \text{m/s}
$$

Reynoldsov broj tada glasi

$$
Re = \frac{vD}{\nu} = \frac{2{,}83 \cdot 0{,}09}{1{,}0 \cdot 10^{-6}} \approx 2{,}55 \cdot 10^5
$$

Takva vrijednost jasno pokazuje da je strujanje turbulentno, pa izraz $64/Re$ više nije dopušten. Zato uz zadani Moodyjev rezultat uzimamo

$$
\lambda \approx 0{,}027
$$

Brzinska visina iznosi

$$
\frac{v^2}{2g} = \frac{2{,}83^2}{2 \cdot 9{,}81} \approx 0{,}408\ \text{m}
$$

Linijski gubitak je

$$
h_l = \lambda \frac{L}{D} \frac{v^2}{2g} = 0{,}027 \cdot \frac{42}{0{,}09} \cdot 0{,}408 \approx 5{,}14\ \text{m}
$$

a lokalni gubitak

$$
\sum h_{loc} = \sum \xi \frac{v^2}{2g} = 5{,}2 \cdot 0{,}408 \approx 2{,}12\ \text{m}
$$

Ukupni gubitak energije zato je

$$
h_w = h_l + \sum h_{loc} \approx 5{,}14 + 2{,}12 = 7{,}26\ \text{m}
$$

odnosno približno

$$
h_w \approx 7{,}3\ \text{m}
$$

**Provjera i komentar**

1. Za $Re \approx 2{,}55 \cdot 10^5$ strujanje ne može biti laminarno.
2. Ukupni gubitak mora biti veći od svakog pojedinačnog doprinosa.
3. Ako je $\lambda$ odabran prije nego što je poznat $Re$, redoslijed rješavanja je kriv.
:::

::: {.mf1-we}
<p class="mf1-box-label">Riješeni primjer - Raspodjela ukupnog protoka u dvjema paralelnim granama <span class="mf1-level">T2</span></p>

**Zadatak**

Voda temperature oko $20^\circ$C teče iz spremnika `A` prema spremniku `B` kroz dvije paralelne cijevi jednake duljine $L = 36\ \text{m}$. Ukupni volumenski protok sustava iznosi

$$
Q_{tot} = 30\ \text{L/s} = 0{,}03\ \text{m}^3/\text{s}
$$

Promjeri grana su $d_1 = 40\ \text{mm}$ i $d_2 = 80\ \text{mm}$. Zanemari lokalne gubitke na račvi i sastavištu. Nakon preliminarnog proračuna otpora za obje grane uzmi da uvjet jednakog gubitka energije daje odnos brzina

$$
v_2 \approx 1{,}56\, v_1
$$

Odredi:

1. brzine $v_1$ i $v_2$.
2. protoke $Q_1$ i $Q_2$.

![U13 Val 2 - paralelne grane](../assets/print/u13_val2_paralelne_grane.svg)

**Pretpostavke i model**

U paralelnim granama ne izjednačava se protok nego gubitak energije između istih čvorova. Ovdje je taj uvjet već sažet u odnos brzina $v_2 \approx 1{,}56 v_1$, pa zadatak služi da se jasno vidi kako se iz ukupnog protoka dobiva raspodjela na dvije grane.

**Rješenje**

Površine presjeka grana iznose

$$
A_1 = \frac{\pi d_1^2}{4} = \frac{\pi \cdot 0{,}04^2}{4} \approx 1{,}257 \cdot 10^{-3}\ \text{m}^2
$$

$$
A_2 = \frac{\pi d_2^2}{4} = \frac{\pi \cdot 0{,}08^2}{4} \approx 5{,}027 \cdot 10^{-3}\ \text{m}^2
$$

Ukupni protok mora biti jednak zbroju protoka po granama:

$$
Q_{tot} = Q_1 + Q_2 = A_1 v_1 + A_2 v_2
$$

Kako je $v_2 = 1{,}56 v_1$, slijedi

$$
0{,}03 = A_1 v_1 + A_2 (1{,}56 v_1)
$$

odnosno

$$
0{,}03 = \left(1{,}257 \cdot 10^{-3} + 1{,}56 \cdot 5{,}027 \cdot 10^{-3}\right) v_1
$$

pa je

$$
v_1 \approx 3{,}29\ \text{m/s}
$$

te zatim

$$
v_2 = 1{,}56 v_1 \approx 5{,}14\ \text{m/s}
$$

Protok prve grane iznosi

$$
Q_1 = A_1 v_1 \approx 1{,}257 \cdot 10^{-3} \cdot 3{,}29 = 4{,}14 \cdot 10^{-3}\ \text{m}^3/\text{s}
$$

odnosno

$$
Q_1 \approx 4{,}1\ \text{L/s}
$$

Za drugu granu dobiva se

$$
Q_2 = Q_{tot} - Q_1 = 30 - 4{,}1 = 25{,}9\ \text{L/s}
$$

odnosno provjerom iz $A_2 v_2$:

$$
Q_2 \approx 25{,}9\ \text{L/s}
$$

**Provjera i komentar**

1. Šira grana mora preuzeti veći dio ukupnog protoka.
2. U paralelnom spoju ne mora vrijediti isti protok kroz obje grane.
3. Ako je izračun dao $Q_1 + Q_2 \neq Q_{tot}$, kontinuitet je negdje izgubljen.
:::

::: {.mf1-we}
<p class="mf1-box-label">Riješeni primjer - Nezatvoreni servisni ispust na rashladnom cjevovodu <span class="mf1-level">T2</span></p>

**Zadatak**

Rashladna voda teče iz otvorenog spremnika `1` u otvoreni spremnik `2` kroz cjevovod promjera

$$
D = 0{,}16\ \text{m}
$$

i ukupne duljine

$$
L = 520\ \text{m}
$$

Razlika slobodnih razina spremnika iznosi

$$
H = 6{,}3\ \text{m}
$$

U urednom režimu, bez gubitka kroz servisni priključak, protok kroz cjevovod je

$$
Q_0 = 0{,}030\ \text{m}^3/\text{s}
$$

Nakon kvara ostao je otvoren servisni ispust u točki `C`, udaljenoj

$$
L_{1C} = 340\ \text{m}
$$

od prvog spremnika, pa je preostala duljina do drugog spremnika

$$
L_{C2} = 180\ \text{m}
$$

Mjerenjem je utvrđeno da u spremnik `2` sada dotječe samo

$$
Q_2 = 0{,}025\ \text{m}^3/\text{s}
$$

a piezometarska visina tlaka u presjeku `C` tijekom oštećenog režima iznosi

$$
\frac{p_C}{\gamma} = 1{,}40\ \text{m}
$$

Pretpostavi da Darcyjev koeficijent trenja ostaje isti kao i u urednom režimu, da su lokalni gubici zanemarivi i da je koeficijent istjecanja servisnog ispušta

$$
C_d = 0{,}62
$$

Odredi:

1. Darcyjev koeficijent trenja $\lambda$ iz urednog režima.
2. ukupni protok $Q_C$ u dionici od spremnika `1` do točke `C` tijekom oštećenog režima.
3. protok gubitka kroz otvoreni servisni ispust.
4. ekvivalentnu površinu $A_p$ i promjer $d_p$ servisnog ispušta.

![U13 Val 3 - nezatvoreni servisni ispust na rashladnom cjevovodu](../assets/print/u13_val3_servisni_ispust.svg)

**Pretpostavke i model**

Promatra se jedan glavni cjevovod s neželjenim gubitkom kroz bočni ispust. Uredni režim služi da se odredi $\lambda$, a oštećeni režim se zatvara kombinacijom jedne Bernoullijeve jednadžbe do presjeka `C`, kontinuiteta i zakona istjecanja kroz otvoreni ispust.

**Rješenje**

Površina presjeka cijevi iznosi

$$
A = \frac{\pi D^2}{4} = \frac{\pi \cdot 0{,}16^2}{4} \approx 2{,}011 \cdot 10^{-2}\ \text{m}^2
$$

U urednom režimu brzina u cijevi je

$$
v_0 = \frac{Q_0}{A} = \frac{0{,}030}{2{,}011 \cdot 10^{-2}} \approx 1{,}49\ \text{m/s}
$$

Kako su oba spremnika otvorena i lokalni gubici se zanemaruju, između njihovih slobodnih razina vrijedi

$$
H = \lambda \frac{L}{D} \frac{v_0^2}{2g}
$$

pa je

$$
\lambda = \frac{2gHD}{L v_0^2} = \frac{2 \cdot 9{,}81 \cdot 6{,}3 \cdot 0{,}16}{520 \cdot 1{,}49^2} \approx 0{,}0171
$$

U ostecenom režimu neka je $v_C$ srednja brzina u dionici od spremnika `1` do presjeka `C`. Bernoullijeva jednadžnba od slobodne razine spremnika `1` do presjeka `C` glasi

$$
H = \frac{p_C}{\gamma} + \frac{v_C^2}{2g} + \lambda \frac{L_{1C}}{D} \frac{v_C^2}{2g}
$$

odnosno

$$
6{,}3 = 1{,}40 + \left(1 + 0{,}0171 \cdot \frac{340}{0{,}16}\right) \frac{v_C^2}{2g}
$$

što daje

$$
6{,}3 = 1{,}40 + 37{,}3 \frac{v_C^2}{2g}
$$

pa je

$$
\frac{v_C^2}{2g} = \frac{4{,}9}{37{,}3} = 0{,}131
$$

i zato

$$
v_C = \sqrt{2g \cdot 0{,}131} \approx 1{,}60\ \text{m/s}
$$

Ukupni protok u gornjoj dionici sada je

$$
Q_C = A v_C = 2{,}011 \cdot 10^{-2} \cdot 1{,}60 \approx 0{,}0323\ \text{m}^3/\text{s}
$$

odnosno

$$
Q_C \approx 32{,}3\ \text{L/s}
$$

Kontinuitet u točki `C` daje

$$
Q_C = Q_2 + Q_p
$$

pa je protok gubitka kroz servisni ispust

$$
Q_p = Q_C - Q_2 = 0{,}0323 - 0{,}0250 = 0{,}0073\ \text{m}^3/\text{s}
$$

odnosno

$$
Q_p \approx 7{,}3\ \text{L/s}
$$

Za istjecanje kroz servisni ispust vrijedi

$$
Q_p = C_d A_p \sqrt{2g \frac{p_C}{\gamma}}
$$

pa je tražena površina

$$
A_p = \frac{Q_p}{C_d \sqrt{2g (p_C/\gamma)}} = \frac{0{,}0073}{0{,}62 \sqrt{2 \cdot 9{,}81 \cdot 1{,}40}} \approx 2{,}25 \cdot 10^{-3}\ \text{m}^2
$$

Ekvivalentni promjer otvora zato je

$$
d_p = \sqrt{\frac{4A_p}{\pi}} = \sqrt{\frac{4 \cdot 2{,}25 \cdot 10^{-3}}{\pi}} \approx 0{,}0535\ \text{m}
$$

odnosno

$$
d_p \approx 53{,}5\ \text{mm}
$$

**Provjera i komentar**

1. Ukupni protok u dionici `1-C` mora biti veći od isporuke prema spremniku `2`, jer dio vode odlazi kroz ispušt.
2. Vrijednost $p_C/\gamma + v_C^2/(2g)$ mora biti reda gubitka energije u dionici `C-2`, što ovdje i jest.
3. Dobiveni promjer reda nekoliko centimetara odgovara otvorenom servisnom priključku, a ne sitnoj mikropukotini.
:::

::: {.mf1-ch}
<p class="mf1-box-label">Cjeloviti zadatak - Serijsko-paralelna mreža između dvaju spremnika <span class="mf1-level">T4</span></p>

**Zadatak**

Voda pri radnom režimu teče iz otvorenog spremnika `A` u otvoreni spremnik `B` kroz sustav koji se sastoji od:

1. zajedničkog dovodnog voda `A-C`.
2. dviju paralelnih grana `C-D`.
3. zajedničkog odvodnog voda `D-B`.

Razlika slobodnih razina spremnika iznosi

$$
H = 12{,}0\ \text{m}
$$

Za promatrani režim uzmi da su Darcyjevi koeficijenti trenja već određeni s Moodyjeva dijagrama, pa vrijedi:

- dovodni vod `A-C`: $D_0 = 100\ \text{mm}$, $L_0 = 28\ \text{m}$, $\lambda_0 = 0{,}024$, $\sum \xi_0 = 1{,}8$
- grana `1`: $D_1 = 80\ \text{mm}$, $L_1 = 32\ \text{m}$, $\lambda_1 = 0{,}026$, $\sum \xi_1 = 2{,}4$
- grana `2`: $D_2 = 60\ \text{mm}$, $L_2 = 26\ \text{m}$, $\lambda_2 = 0{,}028$, $\sum \xi_2 = 3{,}1$
- odvodni vod `D-B`: $D_3 = 100\ \text{mm}$, $L_3 = 18\ \text{m}$, $\lambda_3 = 0{,}024$, $\sum \xi_3 = 1{,}2$

Odredi:

1. odnos brzina $v_2/v_1$ iz uvjeta jednakog gubitka energije u paralelnim granama.
2. ukupni protok sustava $Q$ te protoke po granama $Q_1$ i $Q_2$.
3. gubitke energije u dovodnom vodu $h_0$, u paralelnim granama $h_p$ i u odvodnom vodu $h_3$.
4. snagu koju sustav disipira na hidrauličkim gubicima.

![U13 CH 1 - serijsko-paralelna mreža](../assets/print/u13_ch1_serijsko_paralelna_mreza.svg)

**Pretpostavke i model**

Ovaj `CH` ne vraća se na izbor `\lambda`, jer je taj korak već zatvoren na razini pojedinih dionica. Ovdje je fokus na logici mreže: u paraleli je isti gubitak energije između istih čvorova, a u seriji se gubici zbrajaju pri istom ukupnom protoku. Zato se najprije svaka dionica prevede u svoj koeficijent otpora, zatim se zatvara raspodjela po granama, a tek onda ukupna energijska bilanca sustava.

**Rješenje**

Za svaku dionicu najprije uvedimo ukupni koeficijent otpora

$$
K = \lambda \frac{L}{D} + \sum \xi
$$

pa dobivamo

$$
K_0 = 0{,}024 \cdot \frac{28}{0{,}10} + 1{,}8 = 8{,}52
$$

$$
K_1 = 0{,}026 \cdot \frac{32}{0{,}08} + 2{,}4 = 12{,}8
$$

$$
K_2 = 0{,}028 \cdot \frac{26}{0{,}06} + 3{,}1 = 15{,}23
$$

$$
K_3 = 0{,}024 \cdot \frac{18}{0{,}10} + 1{,}2 = 5{,}52
$$

U paralelnim granama mora vrijediti isti gubitak energije između čvorova `C` i `D`:

$$
K_1 \frac{v_1^2}{2g} = K_2 \frac{v_2^2}{2g}
$$

odakle slijedi

$$
v_2 = \sqrt{\frac{K_1}{K_2}} v_1 = \sqrt{\frac{12{,}8}{15{,}23}} v_1 = 0{,}917 v_1
$$

Površine presjeka iznose

$$
A_0 = A_3 = \frac{\pi \cdot 0{,}10^2}{4} = 7{,}854 \cdot 10^{-3}\ \text{m}^2
$$

$$
A_1 = \frac{\pi \cdot 0{,}08^2}{4} = 5{,}027 \cdot 10^{-3}\ \text{m}^2
$$

$$
A_2 = \frac{\pi \cdot 0{,}06^2}{4} = 2{,}827 \cdot 10^{-3}\ \text{m}^2
$$

Ukupni protok u mreži je

$$
Q = Q_1 + Q_2 = A_1 v_1 + A_2 v_2
$$

pa uz prethodni odnos brzina vrijedi

$$
Q = \left(5{,}027 \cdot 10^{-3} + 0{,}917 \cdot 2{,}827 \cdot 10^{-3}\right) v_1
$$

odnosno

$$
Q = 7{,}618 \cdot 10^{-3} v_1
$$

Zbog jednakih promjera zajedničkih vodova slijedi

$$
v_0 = v_3 = \frac{Q}{A_0} = \frac{7{,}618 \cdot 10^{-3}}{7{,}854 \cdot 10^{-3}} v_1 = 0{,}970 v_1
$$

Sada se ukupni raspoloživi pad energije između spremnika zatvara kao zbroj gubitaka u seriji:

$$
H = K_0 \frac{v_0^2}{2g} + K_1 \frac{v_1^2}{2g} + K_3 \frac{v_3^2}{2g}
$$

pa uz $v_0 = v_3 = 0{,}970 v_1$ dobivamo

$$
12{,}0 = \left[8{,}52 \cdot 0{,}970^2 + 12{,}8 + 5{,}52 \cdot 0{,}970^2\right] \frac{v_1^2}{2g}
$$

odnosno

$$
12{,}0 = 26{,}0 \frac{v_1^2}{2g}
$$

iz cega slijedi

$$
v_1 = 3{,}01\ \text{m/s}
$$

pa je

$$
v_2 = 0{,}917 v_1 = 2{,}76\ \text{m/s}
$$

Ukupni protok sustava iznosi

$$
Q = 7{,}618 \cdot 10^{-3} \cdot 3{,}01 = 2{,}292 \cdot 10^{-2}\ \text{m}^3/\text{s}
$$

odnosno

$$
Q \approx 22{,}9\ \text{L/s}
$$

Protok po prvoj grani je

$$
Q_1 = A_1 v_1 = 5{,}027 \cdot 10^{-3} \cdot 3{,}01 = 1{,}512 \cdot 10^{-2}\ \text{m}^3/\text{s}
$$

odnosno

$$
Q_1 \approx 15{,}1\ \text{L/s}
$$

Za drugu granu dobiva se

$$
Q_2 = A_2 v_2 = 2{,}827 \cdot 10^{-3} \cdot 2{,}76 = 7{,}80 \cdot 10^{-3}\ \text{m}^3/\text{s}
$$

odnosno

$$
Q_2 \approx 7{,}8\ \text{L/s}
$$

Brzina u zajedničkim vodovima sada je

$$
v_0 = v_3 = \frac{Q}{A_0} = 2{,}92\ \text{m/s}
$$

Gubitak u dovodnom vodu iznosi

$$
h_0 = K_0 \frac{v_0^2}{2g} = 8{,}52 \cdot \frac{2{,}92^2}{2 \cdot 9{,}81} = 3{,}70\ \text{m}
$$

Gubitak u paralelnom dijelu mreže jednak je u obje grane:

$$
h_p = K_1 \frac{v_1^2}{2g} = 12{,}8 \cdot \frac{3{,}01^2}{2 \cdot 9{,}81} = 5{,}91\ \text{m}
$$

a provjerom po drugoj grani dobiva se ista vrijednost unutar zaokruzenja.

Za odvodni vod slijedi

$$
h_3 = K_3 \frac{v_3^2}{2g} = 5{,}52 \cdot \frac{2{,}92^2}{2 \cdot 9{,}81} = 2{,}40\ \text{m}
$$

Provjera ukupne bilance sada glasi

$$
h_0 + h_p + h_3 = 3{,}70 + 5{,}91 + 2{,}40 = 12{,}01\ \text{m} \approx H
$$

Snaga koja se u tom režimu disipira na hidrauličkim gubicima iznosi

$$
P_{gub} = \rho g QH = 1000 \cdot 9{,}81 \cdot 0{,}0229 \cdot 12{,}0 = 2{,}70 \cdot 10^3\ \text{W}
$$

odnosno

$$
P_{gub} \approx 2{,}70\ \text{kW}
$$

**Provjera i komentar**

Ovaj primjer zatvara mrežni sloj <span class="mf1-ch-ref"><span class="mf1-ch-code">U13</span><span class="mf1-ch-title">Cjevovodi</span></span> u jednom sustavu: iz uvjeta jednakog gubitka energije slijedi $v_2 \approx 0{,}917 v_1$, ukupni protok mreže je oko $22{,}9\ \text{L/s}$, a raspodjela po granama iznosi oko $15{,}1\ \text{L/s}$ i $7{,}8\ \text{L/s}$. Gubici se tada uredno slažu kao serijski zbroj $h_0 + h_p + h_3 \approx 12\ \text{m}$, pa cijeli sustav disipira oko $2{,}70\ \text{kW}$ hidrauličke snage.

1. Šira grana mora nositi veći dio ukupnog protoka, pa ovdje mora biti $Q_1 > Q_2$.
2. U paralelnim granama ne izjednačava se protok nego gubitak energije između istih čvorova.
3. Ukupni pad između spremnika mora biti jednak zbroju gubitaka u dovodu, paralelnom dijelu i odvodu; ako taj zbroj ne vrati $H$, mreža nije zatvorena.
:::

Prije zadataka vrijedi držati na okupu osnovna pravila mreže:

- u seriji se zbrajaju gubici pri istom protoku
- u paraleli se protok raspodjeljuje pri istom gubitku između čvorova

::: {.mf1-we}
<p class="mf1-box-label">Riješeni primjer – Rashladni cjevovod rotacijske peći &nbsp;<span class="mf1-level">T2</span></p>

🔩 **Primjer za strojare**

**Kontekst:** Rashladni krug rotacijske peći u cementari vodi vodu kroz dovodnu i odvodnu cijev duljine $L = 85\ \text{m}$ (svaka), promjera $D = 100\ \text{mm}$, hrapavosti $\varepsilon = 0{,}1\ \text{mm}$. Krug uključuje jedan nepovratni ventil ($\xi = 3{,}5$), četiri koljena ($\xi = 0{,}9$ svako) i jedan regulacijski ventil ($\xi = 6{,}0$). Protok je $Q = 0{,}025\ \text{m}^3/\text{s}$, $\nu = 1{,}0 \cdot 10^{-6}\ \text{m}^2/\text{s}$, $\lambda = 0{,}022$ (Moody). Odredi ukupni gubitak i potrebnu dopremnu visinu crpke.

**Zadano**

- $L_{uk} = 2 \times 85 = 170\ \text{m}$, $D = 0{,}100\ \text{m}$, $\varepsilon/D = 0{,}001$
- $Q = 0{,}025\ \text{m}^3/\text{s}$, $\lambda = 0{,}022$
- Lokalni: $\Sigma\xi = 3{,}5 + 4 \cdot 0{,}9 + 6{,}0 = 13{,}1$
- Geodetska razlika između usisa i potiska crpke: $\Delta z = 0$ (isti nivo)
- Na ulazu i izlazu rashladnika: $p_1 = p_2$ (isti nadtlak)

![Rashladni cjevovod rotacijske peci: D=100 mm, L=170 m, h_w=26,07 m](../assets/print/u13_fig_rashladni_cjevovod_peci.svg){#fig-u13-rashladni-cjevovod-peci fig-align="center"}

**Rješenje**

$$
A = \frac{\pi \cdot 0{,}100^2}{4} = 7{,}854 \cdot 10^{-3}\ \text{m}^2, \quad v = \frac{0{,}025}{7{,}854 \cdot 10^{-3}} = 3{,}183\ \text{m/s}
$$

$$
Re = \frac{3{,}183 \cdot 0{,}100}{1{,}0 \cdot 10^{-6}} = 3{,}18 \cdot 10^5 \quad \text{(turbulentno)}
$$

$$
h_f = 0{,}022 \cdot \frac{170}{0{,}100} \cdot \frac{3{,}183^2}{2 \cdot 9{,}81} = 0{,}022 \cdot 1700 \cdot 0{,}5164 = 19{,}31\ \text{m}
$$

$$
h_{loc} = 13{,}1 \cdot \frac{3{,}183^2}{2 \cdot 9{,}81} = 13{,}1 \cdot 0{,}5164 = 6{,}76\ \text{m}
$$

$$
h_w = 19{,}31 + 6{,}76 = 26{,}07\ \text{m}
$$

Crpka mora savladati gubitke u krugu, pa je potrebna dopremna visina crpke: $H_p = h_w = 26{,}07\ \text{m}$.

**Provjera i komentar**

Lokalni gubici čine $26\%$ ukupnih — značajan udio zbog regulacijskog ventila ($\xi = 6$). Ako se ventil zatvori na $\xi = 12$, lokalni gubici rastu na $12{,}2\ \text{m}$, ukupni na $31{,}5\ \text{m}$ — +21%. To pokazuje zašto regulacijski ventili moraju biti u proračunu crpne instalacije, ne naknadno dodani.

:::

::: {.mf1-we}
<p class="mf1-box-label">Riješeni primjer – Paralelna razvodna mreža vodovoda &nbsp;<span class="mf1-level">T2</span></p>

🏗️ **Primjer za građevinare**

**Kontekst:** Vodovodna mreža u stambenoj zoni ima dvije paralelne dionice između čvorova A i B. Dionica 1 je čelična cijev $D_1 = 150\ \text{mm}$, $L_1 = 250\ \text{m}$, $\lambda_1 = 0{,}020$. Dionica 2 je PVC cijev $D_2 = 100\ \text{mm}$, $L_2 = 300\ \text{m}$, $\lambda_2 = 0{,}018$. Bez lokalnih gubitaka. Ukupni protok je $Q = 0{,}050\ \text{m}^3/\text{s}$.

**Traženo**

Distribucija protoka $Q_1$ i $Q_2$ te zajednički pad tlaka između A i B.
![Paralelna vodovodna mreza: D1=150 mm, D2=100 mm, Q1=37,0 L/s, Q2=13,0 L/s, h_w=7,5 m](../assets/print/u13_fig_paralelne_grane_vodovod.svg){#fig-u13-paralelne-grane-vodovod fig-align="center"}
**Rješenje**

Koeficijent otpora svake grane: $R_i = \lambda_i \frac{L_i}{D_i} \frac{1}{2g A_i^2}$ (iz $h_{w,i} = R_i Q_i^2$).

$$
A_1 = \frac{\pi \cdot 0{,}150^2}{4} = 1{,}767 \cdot 10^{-2}\ \text{m}^2, \quad R_1 = 0{,}020 \cdot \frac{250}{0{,}150} \cdot \frac{1}{2 \cdot 9{,}81 \cdot (1{,}767 \cdot 10^{-2})^2} = \frac{0{,}020 \cdot 1666{,}7}{6{,}119 \cdot 10^{-3}} = 5449
$$

$$
A_2 = \frac{\pi \cdot 0{,}100^2}{4} = 7{,}854 \cdot 10^{-3}\ \text{m}^2, \quad R_2 = 0{,}018 \cdot \frac{300}{0{,}100} \cdot \frac{1}{2 \cdot 9{,}81 \cdot (7{,}854 \cdot 10^{-3})^2} = \frac{0{,}018 \cdot 3000}{1{,}209 \cdot 10^{-3}} = 44\,665
$$

Uvjet iste energetske razlike: $R_1 Q_1^2 = R_2 Q_2^2$, tj. $\sqrt{R_1}\, Q_1 = \sqrt{R_2}\, Q_2$:
$$\frac{Q_1}{Q_2} = \sqrt{\frac{R_2}{R_1}} = \sqrt{\frac{44665}{5449}} = \sqrt{8{,}197} = 2{,}863$$

S $Q_1 + Q_2 = 0{,}050$:
$$Q_1 = \frac{2{,}863}{3{,}863} \cdot 0{,}050 = 0{,}03704\ \text{m}^3/\text{s}, \quad Q_2 = 0{,}01296\ \text{m}^3/\text{s}$$

Zajednički pad energije:
$$h_w = R_1 Q_1^2 = 5449 \cdot (0{,}03704)^2 = 5449 \cdot 1{,}372 \cdot 10^{-3} = 7{,}47\ \text{m}$$

**Provjera:** $R_2 Q_2^2 = 44665 \cdot (0{,}01296)^2 = 44665 \cdot 1{,}680 \cdot 10^{-4} = 7{,}50\ \text{m}$ ✓ (razlika zbog zaokruživanja)

**Provjera i komentar**

Dionica 1 (šira) nosi $74\%$ protoka uz $7{,}5\ \text{m}$ pada, dionica 2 nosi samo $26\%$. Ako se dionica 2 zatvori (kvar), cijeli protok ide kroz dionicu 1, a pad energije pada na $R_1 \cdot 0{,}050^2 = 13{,}6\ \text{m}$ — pumpa mora biti dimenzioniranana za tu rezervu.

:::

## Usporedna tablica: strojarstvo i građevinarstvo

| Koncept | Strojarstvo – gdje se pojavljuje | Građevinarstvo – gdje se pojavljuje |
|---------|----------------------------------|--------------------------------------|
| $v = Q/A \to Re \to \lambda \to h_w$ | Rashladni krug motora, kompresora, peći | Cjevovod vodovoda ili odvodnje u stambenom bloku |
| Linijski gubitak $\lambda L/D \cdot v^2/2g$ | Duge transportne cijevi goriva u brodogradnji | Magistralni vodovod; dovodni kanal HE |
| Lokalni gubitak $\xi v^2/2g$ | Regulacijski ventili, nepovratni ventili u strojarnici | Priključci, zasuni i hidrantski ogranci u vodovodnoj mreži |
| Serijski spoj: isti $Q$, zbrajaju se $h_w$ | Rashladni krug s više izmjenjivača u nizu | Vodovodna mreža s dva sekcijska ventila u nizu |
| Paralelni spoj: isti $h_w$, raspodjela $Q$ | Paralelni rashladni ogranci industrijskog postrojenja | Razvodna mreža ulica; dvostruka vodovodna petlja |

## Zadaci za vježbu

::: {.mf1-vjezbe-list}
1. **T1** Voda struji cijevi promjera $D = 75\ \text{mm}$ protokom $Q = 0{,}013\ \text{m}^3/\text{s}$. Duljina cijevi je $L = 34\ \text{m}$, apsolutna hrapavost $\varepsilon = 0{,}12\ \text{mm}$, a zbroj lokalnih koeficijenata iznosi $\sum\xi = 4{,}1$. Za vodu uzmi $\nu = 1{,}0 \cdot 10^{-6}\ \text{m}^2/\text{s}$ i Moodyjev koeficijent $\lambda = 0{,}026$. Odredi srednju brzinu, Reynoldsov broj i ukupni gubitak energije.

	**Natuknica:** redoslijed je $Q \rightarrow v \rightarrow Re \rightarrow h_w$; ukupni gubitak je zbroj linijskog i lokalnog dijela.

	**Skica:** da - jedna cijevna dionica s duljinom $L$, promjerom $D$ i lokalnim elementima.

2. **T1** Voda struji cijevi promjera $D = 18\ \text{mm}$ protokom $Q = 1{,}0\times10^{-4}\ \text{m}^3/\text{s}$. Odredi srednju brzinu, Reynoldsov broj i zaključak je li tok laminaran. Ako je laminaran, izračunaj koeficijent trenja.

	**Natuknica:** prvo $v = Q/A$, zatim $Re = vD/\nu$; za laminarni tok vrijedi $\lambda = 64/Re$.

	**Skica:** da - kratka cijev s jednim presjekom i označenim protokom $Q$.

3. **T2** Cjevovodni sustav sastoji se od dviju serijski spojenih dionica. Prva dionica ima $D_1 = 80\ \text{mm}$, $L_1 = 28\ \text{m}$, $\lambda_1 = 0{,}030$ i $\sum\xi_1 = 2{,}4$, a druga $D_2 = 60\ \text{mm}$, $L_2 = 16\ \text{m}$, $\lambda_2 = 0{,}034$ i $\sum\xi_2 = 3{,}1$. Ako je protok kroz sustav $Q = 0{,}010\ \text{m}^3/\text{s}$, odredi ukupni gubitak energije.

	**Natuknica:** u seriji je isti protok kroz obje dionice; zato svaku dionicu računaj zasebno i na kraju zbroji gubitke.

	**Skica:** da - dvije serijski spojene cijevne dionice različitih promjera.

4. **T2** U ravnoj cijevi vrijedi ukupni koeficijent $K = \lambda L/D + \sum\xi = 68$. Ako je zadani ukupni gubitak energije $h_w = 5{,}4\ \text{m}$, a promjer cijevi $D = 90\ \text{mm}$, odredi potrebni protok vode.

	**Natuknica:** iz $h_w = K v^2/(2g)$ vrati $v$, a zatim protok iz $Q = Av$.

	**Skica:** da - jedna cijevna dionica s označenim ukupnim gubitkom $h_w$.

5. **T3** Dvije paralelne grane imaju aproksimativne relacije gubitka energije $h_{w1} = 1450Q_1^2$ i $h_{w2} = 2400Q_2^2$, pri čemu su $h_w$ u metrima, a protoci u $\text{m}^3/\text{s}$. Ako je ukupni protok kroz razdjelnik $Q = 0{,}032\ \text{m}^3/\text{s}$, odredi protoke $Q_1$ i $Q_2$ te zajednički gubitak energije između čvorova.

	**Natuknica:** u paraleli mora biti $h_{w1} = h_{w2}$ uz uvjet $Q = Q_1 + Q_2$; riješi te dvije jednadžbe zajedno.

	**Skica:** da - razdjelnik s dvjema paralelnim granama i zajedničkim ulaznim/izlaznim čvorovima.

6. **T3** Voda teče iz spremnika `A` u spremnik `B` kroz zajednički dovodni vod $D_0 = 100\ \text{mm}$, $L_0 = 20\ \text{m}$, $\lambda_0 = 0{,}025$, $\sum\xi_0 = 1{,}6$, zatim kroz dvije paralelne grane: grana `1` ima $D_1 = 80\ \text{mm}$, $L_1 = 24\ \text{m}$, $\lambda_1 = 0{,}028$, $\sum\xi_1 = 2{,}0$, a grana `2` ima $D_2 = 60\ \text{mm}$, $L_2 = 18\ \text{m}$, $\lambda_2 = 0{,}030$, $\sum\xi_2 = 2{,}6$. Nakon spajanja tok odlazi kroz vod $D_3 = 100\ \text{mm}$, $L_3 = 14\ \text{m}$, $\lambda_3 = 0{,}025$, $\sum\xi_3 = 1{,}0$. Razlika slobodnih razina spremnika iznosi $H = 9{,}5\ \text{m}$. Odredi odnos brzina u granama, protoke $Q_1$ i $Q_2$ te ukupni protok sustava.

	**Natuknica:** u paralelnim granama izjednači $h_{w1}$ i $h_{w2}$, kontinuitetom zbroji $Q_1 + Q_2 = Q$, a ukupni pad energije zatvori kao serijski zbroj dovoda, paralelnog dijela i odvoda.

	**Skica:** da - jedan dovodni vod, dvije paralelne grane i jedan odvodni vod između dvaju spremnika.
:::

![U13 zadaci za vježbu - minimalne grayscale tehničke skice uz zadatke.](../assets/print/u13_vjezbe_skice.svg)

::: {.mf1-zavrsni-okvir}
<p class="mf1-box-label">Za ponijeti iz poglavlja</p>

**Sažeta provjera prije računa**

- Treba najprije zaključati geometriju mreže i lokalne elemente.
- Treba iz protoka dobiti brzinu prije odabira $\lambda$.
- Treba utvrditi vrijedi li $64/Re$ ili treba koristiti Moodyjev dijagram.
- Treba razlikovati pravilo serije od pravila paralelnih grana.
- Treba zbrajati sve gubitke u istom energijskom obliku.

**Najčešća pogreška**

Najčešća greška u <span class="mf1-ch-ref"><span class="mf1-ch-code">U13</span><span class="mf1-ch-title">Cjevovodi</span></span> nije sama algebra nego krivi redoslijed. Čest je kvar kad račun krene od koeficijenta trenja ili čak od ukupnog gubitka, a da još nisu određeni brzina, režim strujanja i logika mreže. Drugi česti kvar je primjena pravila istog protoka na paralelne grane, gdje zapravo mora biti isti gubitak energije.

**Nakon ovoga poglavlja mora biti moguće**

1. odrediti brzinu, Reynoldsov broj i režim strujanja u cijevi.
2. odabrati ili pročitati odgovarajući koeficijent trenja $\lambda$.
3. složiti linijske i lokalne gubitke u ukupni $h_w$.
4. razlikovati osnovna pravila serijskog i paralelnog spoja cjevovoda.

**U tehnici to znači**

Industrijski vod, brodska rashladna mreža ili kotlovnički razvod ne mogu se projektirati samo iz jedne cijevi, nego iz cijele mreže međusobno povezanih dionica. Tek kad su redoslijed računa, režim strujanja i logika čvorova ispravno zatvoreni, dobiva se vjerodostojna radna točka sustava.

**Granica modela**

Koeficijent trenja nije konstanta neovisna o protoku, a raspodjela po paralelnim granama ne čita se jednom zauvijek. Promjena hrapavosti, položaja ventila, onečišćenje ili dodatni ispust mogu pomaknuti cijeli sustav, pa mrežu uvijek treba čitati kao osjetljiv i međusobno povezan model.

<span class="mf1-ch-ref"><span class="mf1-ch-code">U13</span><span class="mf1-ch-title">Cjevovodi</span></span> zatvara osnovni dinamički niz: od protoka i energije dolazi se do stvarnog sustava cijevi u kojem su režim strujanja, trenje i logika mreže jednako važni. Kad je ovdje jasan redoslijed $Q \to v \to Re \to \lambda \to h_w$, kasnije se sigurnije čitaju i složeniji cjevovodni sustavi.
:::








