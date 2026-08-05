![Pregled poglavlja: tri lica iste ideje — režim strujanja (laminarno/turbulentno), ključni omjeri sila (Re, Fr, Eu, We, Ma) i modelsko ispitivanje broda u vučnom bazenu po Froudeovoj sličnosti](../assets/print/u14_fig_uvod_pregled.svg){#fig-uvod-u14 fig-align="center" fig-alt="Pregled poglavlja: tri lica iste ideje — režim strujanja (laminarno/turbulentno), ključni omjeri sila (Re, Fr, Eu, We, Ma) i modelsko ispitivanje broda u vučnom bazenu po Froudeovoj sličnosti"}

## Sile kao zajednički jezik cijele knjige

Cijeli je udžbenik bio niz sila: tlačna sila u <span class="mf1-ch-ref"><span class="mf1-ch-code">pog. 1</span><span class="mf1-ch-title">Osnove fluida i Pascalov zakon</span></span>, viskozna sila u <span class="mf1-ch-ref"><span class="mf1-ch-code">pog. 2</span><span class="mf1-ch-title">Reologija, viskoznost i međupovršinske pojave</span></span>, gravitacijska sila kroz hidrostatiku i uzgon u <span class="mf1-ch-ref"><span class="mf1-ch-code">pog. 6</span><span class="mf1-ch-title">Uzgon, plivanje i početni stabilitet</span></span>, inercijska sila u <span class="mf1-ch-ref"><span class="mf1-ch-code">pog. 10</span><span class="mf1-ch-title">Količina i moment količine gibanja</span></span> te viskozni gubitci i Reynoldsov broj u <span class="mf1-ch-ref"><span class="mf1-ch-code">pog. 13</span><span class="mf1-ch-title">Gubitci, cjevovodi, crpke i mreže</span></span>.

Ovo poglavlje **ne uvodi nijednu novu silu** — ono postojeće mehanizme uspoređuje bezdimenzijskim grupama. Mnogi važni brojevi mogu se povezati s omjerima karakterističnih sila, ali neki prirodnije predstavljaju omjere vremenskih skala, brzina ili normirane izlazne veličine. Zadatak dimenzijske analize nije unaprijed proglasiti jednu silu „vladarom”, nego utvrditi koje grupe mogu utjecati na promatrani rezultat.

::: {.mf1-application}
<p class="mf1-box-label">Inženjerski kontekst</p>

Brod se prije gradnje ispituje kao model u vučnom bazenu, automobil i zrakoplovno krilo u aerotunelu, a brodski vijak i centrifugalna crpka provjeravaju se na kavitaciju. Model i prototip ponašaju se jednako u bezdimenzijskom smislu samo ako su im jednaki **svi mjerodavni** brojevi te bezdimenzijski rubni i početni uvjeti. Kad to nije moguće, bira se prioritetna sličnost i kvantificira učinak neusklađenih grupa. Isti jezik povezuje vrtložno otpuštanje, raspad mlaza, stlačivost i prijenos rezultata iz laboratorija u pogon.
:::

::: {.mf1-priprema}
<p class="mf1-box-label">Prije čitanja poglavlja</p>

**Predznanje koje se pretpostavlja:**

- pojam viskoznosti i Reynoldsovog broja iz poglavlja <span class="mf1-ch-ref"><span class="mf1-ch-code">pog. 2</span><span class="mf1-ch-title">Reologija, viskoznost i međupovršinske pojave</span></span> i <span class="mf1-ch-ref"><span class="mf1-ch-code">pog. 13</span><span class="mf1-ch-title">Gubitci, cjevovodi, crpke i mreže</span></span>;
- linijski gubitci i koeficijent trenja $\lambda$ iz poglavlja <span class="mf1-ch-ref"><span class="mf1-ch-code">pog. 13</span><span class="mf1-ch-title">Gubitci, cjevovodi, crpke i mreže</span></span>;
- površinska napetost $\sigma$ i kapilarnost iz poglavlja <span class="mf1-ch-ref"><span class="mf1-ch-code">pog. 2</span><span class="mf1-ch-title">Reologija, viskoznost i međupovršinske pojave</span></span>;
- pojam inercijske sile iz poglavlja <span class="mf1-ch-ref"><span class="mf1-ch-code">pog. 10</span><span class="mf1-ch-title">Količina i moment količine gibanja</span></span>; SI jedinice i dimenzije iz <span class="mf1-ch-ref"><span class="mf1-ch-code">pog. 1</span><span class="mf1-ch-title">Osnove fluida i Pascalov zakon</span></span>.

**Ishodi učenja:**

- fizikalno protumačiti bezdimenzijske brojeve kao omjere sila, vremenskih skala ili normirane rezultate te prepoznati relevantne mehanizme problema;
- provesti Buckinghamovu dimenzijsku analizu i dobiti bezdimenzijske grupe ($\Pi$-grupe) iz popisa varijabli;
- primijeniti uvjete geometrijske, kinematičke i dinamičke sličnosti na modelsko ispitivanje;
- objasniti zašto se Reynoldsova i Froudeova sličnost u pravilu ne mogu zadovoljiti istovremeno i kako se ta nepotpunost rješava;
- odabrati mjerodavne grupe na temelju jednadžbi, geometrije i rubnih uvjeta te obrazložiti zanemarene učinke.

**Procijenjeno vrijeme rada uz udžbenik:** 9 sati.
:::

## Dimenzije, jedinice i sila inercije kao referenca

Svaka fizikalna veličina u mehanici fluida izražava se preko tri **primarne dimenzije**: mase $\mathsf{M}$, duljine $\mathsf{L}$ i vremena $\mathsf{T}$. Tako brzina ima dimenziju $\mathsf{L}\,\mathsf{T}^{-1}$, gustoća $\mathsf{M}\,\mathsf{L}^{-3}$, a tlak i naprezanje $\mathsf{M}\,\mathsf{L}^{-1}\,\mathsf{T}^{-2}$. Načelo **dimenzijske homogenosti** kaže da svaki ispravan fizikalni izraz mora s obje strane imati istu dimenziju — to je ujedno prva i najjeftinija provjera svake jednadžbe.

Bezdimenzijski broj nastaje kombiniranjem veličina tako da se dimenzije pokrate. U mehanici fluida osobito su korisna karakteristična mjerila sila jer omogućuju usporedbu fizikalnih mehanizama. Za mnoge tokove polazi se od sljedećih mjerila:

$$
F_i \sim \rho v^2 L^2 \quad(\text{inercija}), \qquad
F_\mu \sim \mu v L \quad(\text{viskoznost}), \qquad
F_g \sim \rho g L^3 \quad(\text{gravitacija}),
$$ {#eq-slicnost-dimenzije-jedinice-i-sila-inercije-kao-referenca-01}

$$
F_p \sim \Delta p\, L^2 \quad(\text{tlak}), \qquad
F_\sigma \sim \sigma L \quad(\text{površinska napetost}).
$$ {#eq-slicnost-dimenzije-jedinice-i-sila-inercije-kao-referenca-02}

Ovdje je $L$ karakteristična duljina problema (promjer cijevi, duljina trupa, promjer kapi), a $v$ karakteristična brzina. **Inercijska sila** $F_i \sim \rho v^2 L^2$ uzima se kao prirodna referenca jer je prisutna u gotovo svakom strujanju — čim se fluid giba, ima inerciju. Zato se većina važnih bezdimenzijskih brojeva može pročitati kao omjer inercijske sile prema nekoj drugoj sili.

::: {.mf1-fizikalno-znacenje}
<p class="mf1-box-label">Fizikalno značenje</p>
Bezdimenzijski broj nije puka matematička kratica. Omjeri sila poput $Re$, $Fr^2$ i $We$ pokazuju relativnu važnost mehanizama; $St$ uspoređuje vremenske skale, $Ma$ brzinu toka i širenja zvuka, a $C_p$ i $C_d$ normiraju mjerene odzive. Jednaka vrijednost jedne grupe nije dovoljna ako su u problemu aktivne i druge grupe.
:::

## Bezdimenzijske grupe kao omjeri mehanizama

Slika [-@fig-u14-omjer-sila] prikazuje skup karakterističnih sila iz kojih nastaju brojni važni omjeri. Strouhalov i Machov broj u nastavku uvode i dvije druge interpretacije — vremensku i brzinsku.

![Čestica fluida i pet karakterističnih sila; njihovi omjeri daju Reynoldsov, Froudeov, Eulerov, Weberov i Bondov broj.](../assets/print/u14_fig_omjer_sila.svg){#fig-u14-omjer-sila fig-align="center" fig-alt="Čestica fluida i pet karakterističnih sila; njihovi omjeri daju Reynoldsov, Froudeov, Eulerov, Weberov i Bondov broj."}

**Reynoldsov broj** uspoređuje inerciju i viskoznost:

$$
Re = \frac{F_i}{F_\mu} = \frac{\rho v L}{\mu} = \frac{v L}{\nu}.
$$ {#eq-slicnost-bezdimenzijske-grupe-kao-omjeri-mehanizama-01}

Mali $Re$ obično znači da viskoznost snažno prigušuje poremećaje. Veliki $Re$ znači da su inercijski učinci jaki, ali **ne jamči sam po sebi turbulenciju**: prijelaz ovisi o geometriji, stabilnosti osnovnog toka, hrapavosti i ulaznim poremećajima. Za razvijeno strujanje u kružnoj cijevi $Re\lesssim2300$ obično je laminarno, prijelazno je približno između 2300 i 4000, a iznad toga u tehničkim uvjetima najčešće turbulentno [@white2011].

**Froudeov broj** uspoređuje inerciju i gravitaciju:

$$
Fr = \frac{v}{\sqrt{gL}}, \qquad Fr^2 = \frac{F_i}{F_g}.
$$ {#eq-slicnost-bezdimenzijske-grupe-kao-omjeri-mehanizama-02}

Froudeov broj važan je kada dinamiku slobodne površine određuju gravitacijski valovi, primjerice kod broda, otvorenog kanala ili preljeva. U otvorenom kanalu, kada je za $L$ odabrana hidraulička dubina $A/T$, $Fr=1$ označuje kritično strujanje: karakteristična brzina plitkovodnog vala jednaka je srednjoj brzini toka.

**Eulerov broj i koeficijent tlaka** uspoređuju tlačnu i inercijsku silu:

$$
Eu = \frac{\Delta p}{\rho v^2}, \qquad C_p = \frac{p - p_\infty}{\tfrac{1}{2}\rho v^2}.
$$ {#eq-slicnost-bezdimenzijske-grupe-kao-omjeri-mehanizama-03}

U nestlačivom, neviskoznom toku s referentnim stanjem u neporemećenoj struji Bernoullijeva jednadžba daje $C_p=1$ u stagnacijskoj točki. U realnom ili stlačivom toku, uz drukčiji izbor referentnog tlaka ili gubitke, ta vrijednost nije univerzalna. Negativan $C_p$ samo znači da je statički tlak manji od odabranoga referentnog tlaka.

**Kavitacijski broj** je posebni Eulerov broj koji normira tlačnu rezervu referentnog toka iznad tlaka zasićene pare:

$$
\sigma_{kav} = \frac{p_{ref} - p_v}{\tfrac{1}{2}\rho v_{ref}^2}.
$$ {#eq-slicnost-bezdimenzijske-grupe-kao-omjeri-mehanizama-04}

Referentni tlak, brzina i kritična vrijednost moraju biti definirani za konkretnu napravu i konvenciju. Kavitacija lokalno počinje kada apsolutni tlak dosegne $p_v$; na razini cijelog propelera ili crpke to se često opisuje eksperimentalnim $\sigma_{kr}$. Zato sama brojčana vrijednost $\sigma_{kav}$ bez karakteristike uređaja nije dovoljna za tvrdnju „sigurno” ili „kavitira”.

**Weberov broj** uspoređuje inerciju i površinsku napetost:

$$
We = \frac{\rho v^2 L}{\sigma}, \qquad We = \frac{F_i}{F_\sigma}.
$$ {#eq-slicnost-bezdimenzijske-grupe-kao-omjeri-mehanizama-05}

Pri malom $We$ površinska napetost snažno se opire deformaciji, a pri velikom su inercijska naprezanja relativno veća. Prag raspada nije univerzalan: ovisi o vrsti raspada, omjeru gustoća i viskoznosti, Ohnesorgeovu broju, početnoj deformaciji i vremenu djelovanja. Vrijednost reda $We\approx12$ može služiti kao orijentir za određene režime aerodinamičkog raspada pojedinačne kapi, ali ne kao opći kriterij kvalitete atomizacije [@white2011].

**Bondov (Eötvösov) broj** uspoređuje gravitaciju i površinsku napetost:

$$
Bo = \frac{\Delta\rho\,g L^2}{\sigma}.
$$ {#eq-slicnost-bezdimenzijske-grupe-kao-omjeri-mehanizama-06}

Ovdje je $\Delta\rho$ razlika gustoća dviju faza; za granicu voda–zrak često se aproksimira gustoćom vode. Pri $Bo\sim1$ gravitacija i površinska napetost usporedive su, a kapilarna duljina glasi $L_c=\sqrt{\sigma/(\Delta\rho g)}$.

**Strouhalov broj** opisuje nestacionarno, periodičko strujanje:

$$
St = \frac{f L}{v},
$$ {#eq-slicnost-bezdimenzijske-grupe-kao-omjeri-mehanizama-07}

gdje je $f$ frekvencija pojave. To je omjer konvektivne vremenske skale $L/v$ i perioda $1/f$, a ne izravan omjer sila. Za kružni cilindar u određenom subkritičnom području Reynoldsova broja često je $St$ reda $0{,}2$; vrijednost ovisi o geometriji i režimu [@white2011].

**Machov broj** uspoređuje inerciju i stlačivost (elastičnost) fluida:

$$
Ma = \frac{v}{a}, \qquad \text{Cauchyjev broj} = \frac{\rho v^2}{K} = Ma^2,
$$ {#eq-slicnost-bezdimenzijske-grupe-kao-omjeri-mehanizama-08}

gdje je $a$ brzina zvuka, a $K$ modul stlačivosti. Za plinska strujanja bez velikog zagrijavanja i snažnih tlačnih promjena, $Ma<0{,}3$ često je uporabljiv kriterij da su promjene gustoće male. To je inženjerski prag, ne matematička granica: iznad njega stlačivost postupno postaje važna, a i pri malom $Ma$ gustoća se može mijenjati zbog temperature ili sastava [@anderson2021].

**Koeficijent trenja, otpora i tlaka kao bezdimenzijski rezultati.** Konačni rezultati otpora nisu sile nego njihove bezdimenzijske, normirane vrijednosti:

$$
\lambda = \lambda\!\left(Re, \frac{\varepsilon}{D}\right), \qquad
C_d = \frac{F_D}{\tfrac{1}{2}\rho v^2 A}.
$$ {#eq-slicnost-bezdimenzijske-grupe-kao-omjeri-mehanizama-09}

Darcyjev $\lambda$ i koeficijent otpora $C_d$ jesu bezdimenzijski odzivi. Jedna izmjerena krivulja može se prenositi samo unutar iste bezdimenzijske geometrije, rubnih uvjeta i skupa relevantnih grupa; primjerice $C_d$ osim o $Re$ može ovisiti o hrapavosti, $Ma$, slobodnoj turbulenciji i blizini stijenke.

::: {.callout-note collapse="true" icon="false"}
## Numerički trag

Za jednofazni, nestlačivi Newtonov fluid konstantnih svojstava, bez dodatnih aktivnih mehanizama, bezdimenzioniranje jednadžbi uvodi Reynoldsov broj. Jednaki $Re$ daje isto bezdimenzijsko rješenje tek uz jednaku bezdimenzijsku geometriju te iste početne i rubne uvjete. Slobodna površina, površinska napetost, rotacija, uzgon ili nestacionarno pobuđivanje uvode dodatne grupe poput $Fr$, $We$, Rossbyjeva ili Strouhalova broja.
:::

Tablica sažima sve brojeve poglavlja; ista tablica u skraćenom obliku ulazi u <span class="mf1-ch-ref"><span class="mf1-ch-code">dod. A</span><span class="mf1-ch-title">Sažetak formula i oznaka</span></span>.

| Broj | Definicija | Fizikalno tumačenje | Prag ili uvjet | Gdje je važan |
| --- | --- | --- | --- | --- |
| $Re$ | $\rho vL/\mu=vL/\nu$ | inercija / viskoznost | granice ovise o geometriji; za cijev približno 2300–4000 | režim, otpor |
| $Fr$ | $v/\sqrt{gL}$ | $Fr^2=$ inercija / gravitacija | $Fr=1$ za kritično strujanje u otvorenom kanalu | brod, kanal, preljev |
| $Eu,\ C_p$ | $\Delta p/(\rho v^2)$; $(p-p_\infty)/(\tfrac12\rho v^2)$ | tlak / inercija; normirani tlak | $C_p=1$ samo za idealnu nestlačivu stagnaciju uz odgovarajuću referencu | raspodjela tlaka |
| $\sigma_{kav}$ | $(p_{ref}-p_v)/(\tfrac12\rho v_{ref}^2)$ | normirana tlačna rezerva | usporedba s uređajno i konvencijski definiranim $\sigma_{kr}$ | vijak, crpka |
| $We$ | $\rho v^2L/\sigma$ | inercija / površinska napetost | prag raspada ovisi o režimu i drugim grupama | kap, mlaz, sprej |
| $Bo$ | $\Delta\rho gL^2/\sigma$ | gravitacija / površinska napetost | $Bo\sim1$, $L_c=\sqrt{\sigma/(\Delta\rho g)}$ | oblik kapi i mjehura |
| $\lambda,\ C_d$ | bezdimenzijski koeficijenti | normirani odzivi otpora | vrijede uz definiranu geometriju i relevantne grupe | unutarnji i vanjski otpor |
| $St$ | $fL/v$ | omjer vremenskih skala | $St$ reda $0{,}2$ samo za određene tokove oko cilindra | vrtložno otpuštanje |
| $Ma$ | $v/a$ | omjer brzine toka i zvuka; $Ma^2$ povezan s inercijom/stlačivošću | $Ma<0{,}3$ je čest, uvjetan nestlačivi prag | stlačivost |

## Buckinghamov Π teorem

Dimenzijska analiza odgovara na pitanje: ako problem ovisi o $n$ fizikalnih veličina, koliko **neovisnih bezdimenzijskih grupa** ga zaista određuje? Odgovor daje Buckinghamov $\Pi$ teorem:

$$
\text{broj } \Pi\text{-grupa} = n - k,
$$ {#eq-slicnost-buckinghamov-teorem-01}

gdje je $n$ broj fizikalnih veličina, a $k$ broj neovisnih primarnih dimenzija (u mehanici fluida najčešće $k = 3$: $\mathsf{M}, \mathsf{L}, \mathsf{T}$). Postupak je uvijek isti:

1. popiši sve fizikalne veličine koje ulaze u problem i njihove dimenzije;
2. odredi $k$ — broj neovisnih dimenzija;
3. izaberi $k$ **ponavljajućih varijabli** koje zajedno pokrivaju sve dimenzije i same ne tvore bezdimenzijsku grupu (tipično $\rho, v, L$);
4. svaku preostalu varijablu kombiniraj s ponavljajućima u jednu $\Pi$-grupu i odredi eksponente tako da izraz bude bezdimenzijski;
5. prepoznaj svaku grupu kao poznati broj (Re, Fr, …).

Slika [-@fig-u14-pi-buckingham] prikazuje taj postupak shematski na primjeru otpora kugle.

![Shema Buckinghamova postupka: popis varijabli {F, ρ, v, D, μ}, dimenzijska matrica M-L-T i tvorba dviju Π-grupa Π₁ = F/(ρv²D²) i Π₂ = Re](../assets/print/u14_fig_pi_buckingham.svg){#fig-u14-pi-buckingham fig-align="center" fig-alt="Shema Buckinghamova postupka: popis varijabli {F, ρ, v, D, μ}, dimenzijska matrica M-L-T i tvorba dviju Π-grupa Π₁ = F/(ρv²D²) i Π₂ = Re"}

::: {.mf1-izvod}
<p class="mf1-box-label">Matematički izvod — Dimenzijska analiza pada tlaka u cijevi</p>

Ukupni pad tlaka na ravnoj cijevnoj dionici može ovisiti o gustoći $\rho$, srednjoj brzini $v$, promjeru $D$, duljini $L$, viskoznosti $\mu$ i hrapavosti stijenke $\varepsilon$. Skup od $n = 7$ veličina ($\Delta p,\rho,v,D,L,\mu,\varepsilon$) ima $k = 3$ neovisne dimenzije, pa nastaju četiri $\Pi$-grupe.

Uz ponavljajuće varijable $\rho, v, D$ tvore se grupe:

$$
\Pi_1 = \frac{\Delta p}{\rho v^2}, \qquad
\Pi_2 = \frac{\rho v D}{\mu} = Re, \qquad
\Pi_3 = \frac{L}{D}, \qquad
\Pi_4 = \frac{\varepsilon}{D}.
$$ {#eq-slicnost-matematicki-izvod-dimenzijska-analiza-pada-tlaka-01}

Iz teorema slijedi da su sve grupe povezane jednom funkcijom:

$$
\frac{\Delta p}{\rho v^2} = \phi\!\left(Re, \frac{L}{D}, \frac{\varepsilon}{D}\right).
$$ {#eq-slicnost-matematicki-izvod-dimenzijska-analiza-pada-tlaka-02}

::: {.callout-note}
## Razrada koraka
Korak: traženje eksponenata za $\Pi_1 = \Delta p\, \rho^a v^b D^c$.

Dimenzije: $[\Delta p] = \mathsf{M}\mathsf{L}^{-1}\mathsf{T}^{-2}$, $[\rho] = \mathsf{M}\mathsf{L}^{-3}$, $[v] = \mathsf{L}\mathsf{T}^{-1}$, $[D] = \mathsf{L}$. Da $\Pi_1$ bude bezdimenzijski:

$$
\mathsf{M}:\ 1 + a = 0,\qquad
\mathsf{T}:\ -2 - b = 0,\qquad
\mathsf{L}:\ -1 - 3a + b + c = 0.
$$ {#eq-slicnost-razrada-koraka-01}

Odatle $a = -1$, $b = -2$, $c = 0$, pa je $\Pi_1 = \Delta p/(\rho v^2)$, što je Eulerov broj.
:::

Dimenzijska analiza sama ne određuje oblik funkcije $\phi$ niti dokazuje linearnost s $L$. Dodatna fizikalna pretpostavka glasi: strujanje je potpuno razvijeno u jednolikoj ravnoj cijevi, pa je srednji gradijent tlaka konstantan i jednake se dionice mogu zbrajati. Tek tada je $\Delta p\propto L$, pa se funkcija može zapisati u Darcy–Weisbachovu obliku

$$
\Delta p = \lambda\,\frac{L}{D}\,\frac{\rho v^2}{2}, \qquad \lambda = \lambda\!\left(Re, \frac{\varepsilon}{D}\right),
$$ {#eq-slicnost-razrada-koraka-02}

Dimenzijska analiza tako ograničava dopuštenu ovisnost, a pretpostavka potpuno razvijenoga toka izdvaja $L/D$. Sama funkcija $\lambda(Re,\varepsilon/D)$ dobiva se analitički u laminarnom toku ili empirijski/numerički u turbulentnom.
:::

::: {.mf1-izvod}
<p class="mf1-box-label">Matematički izvod — Otpor kugle daje Cd(Re)</p>

Za izoliranu glatku kuglu u jednolikoj, nestlačivoj struji daleko od stijenki, uz zanemarivu slobodnu turbulenciju i stlačivost, sila otpora $F_D$ ovisi o $\rho$, $v$, $D$ i $\mu$. Tada iz pet veličina nastaju dvije $\Pi$-grupe:

$$
\Pi_1 = \frac{F_D}{\rho v^2 D^2}, \qquad \Pi_2 = \frac{\rho v D}{\mu} = Re.
$$ {#eq-slicnost-matematicki-izvod-otpor-kugle-daje-cd-re-01}

Time je cijeli problem otpora sveden na jednu funkciju jedne varijable:

$$
\frac{F_D}{\rho v^2 D^2} = f(Re) \quad\Longleftrightarrow\quad C_d = \frac{F_D}{\tfrac{1}{2}\rho v^2 A} = \Phi(Re),
$$ {#eq-slicnost-matematicki-izvod-otpor-kugle-daje-cd-re-02}

Unutar navedenih pretpostavki jedna krivulja $C_d(Re)$ obuhvaća Stokesov režim $C_d=24/Re$ pri vrlo malom $Re$ i područje otporne krize. Hrapavost, blizina stijenke, slobodna turbulencija ili stlačivost uveli bi dodatne parametre i promijenili krivulju.
:::

## Sličnost i modelska ispitivanja

Da bi se rezultati ispitivanja modela mogli prenijeti na stvarni objekt (prototip), mora vrijediti **sličnost** na tri razine:

- **geometrijska sličnost** — model i prototip imaju isti oblik, sve duljine u istom mjerilu $\lambda_L = L_p/L_m$;
- **kinematička sličnost** — polja brzina su geometrijski slična (iste linije strujanja, brzine u istom omjeru);
- **dinamička sličnost** — sile na model i prototip u istom su omjeru, što znači da su **mjerodavni bezdimenzijski brojevi jednaki**.

Dinamička sličnost je cilj: ako su jednaki svi relevantni brojevi, model i prototip ponašaju se identično u bezdimenzijskom smislu, pa se izmjereni koeficijenti ($C_d$, $C_p$, $\lambda$) izravno prenose.

::: {.mf1-fizikalno-znacenje}
<p class="mf1-box-label">Fizikalno značenje</p>
Praktičan problem je što se svi brojevi rijetko mogu izjednačiti istovremeno. Za model broda u istom fluidu jednak $Fr$ traži $v_m=v_p/\sqrt{\lambda_L}$, dok jednak $Re$ traži $v_m=v_p\lambda_L$. Ti su zahtjevi za $\lambda_L\ne1$ međusobno nespojivi. U vučnom bazenu zato se prioritetno čuva Froudeova sličnost, a viskozni doprinos procjenjuje zasebno odgovarajućim korekcijskim postupkom. Drugi fluid ili promijenjeni tlak/temperatura mogu približiti dodatnu sličnost, ali uvode praktična ograničenja i nove provjere.
:::

Skaliranje veličina slijedi iz odabranog broja. Pri Froudeovoj sličnosti, uz jednako gravitacijsko ubrzanje i mjerilo $\lambda_L=L_p/L_m$, vrijedi:

$$
\frac{v_p}{v_m} = \sqrt{\lambda_L}, \qquad
\frac{Q_p}{Q_m} = \lambda_L^{5/2}, \qquad
\frac{F_p}{F_m} = \frac{\rho_p}{\rho_m}\lambda_L^{3}.
$$ {#eq-slicnost-fizikalno-znacenje-01}

Posljednji se izraz svodi na $\lambda_L^3$ samo kada model i prototip imaju jednaku referentnu gustoću.

## Kako odlučiti što bezdimenzionirati

Srž ovog poglavlja nije zapamtiti devet formula, nego prepoznati **skup** relevantnih grupa. Najprije se definiraju izlazna veličina, geometrija, fluid te početni i rubni uvjeti; zatim se iz jednadžbi ili Buckinghamova postupka izdvoje mogući mehanizmi. Procjena reda veličine pokazuje koje se grupe mogu zanemariti, a koje treba očuvati. Ako dvije važne grupe nije moguće istodobno uskladiti, odabire se prioritetna sličnost i procjenjuje mjerilna pogreška.

![Dijagram pitanja za prepoznavanje mogućih relevantnih grupa: slobodna površina upućuje na Fr, viskoznost na Re, kapljice na We i Bo, kavitacija na σ, periodičnost na St, a stlačivost na Ma. U jednom problemu može biti važno više grupa.](../assets/print/u14_fig_odluka.svg){#fig-u14-odluka fig-align="center" fig-alt="Dijagram pitanja za prepoznavanje mogućih relevantnih grupa: slobodna površina upućuje na Fr, viskoznost na Re, kapljice na We i Bo, kavitacija na σ, periodičnost na St, a stlačivost na Ma. U jednom problemu može biti važno više grupa."}

::: {.mf1-decision-grid}
::: {.mf1-decision-step}
<span class="mf1-step-index">1</span>

<p class="mf1-box-label">Postoji li slobodna površina ili valovi?</p>

Ako da, u igri je gravitacija → mjerodavan je **Froudeov broj** $Fr$ (brod, kanal, preljev, hidraulički skok).
:::

::: {.mf1-decision-step}
<span class="mf1-step-index">2</span>

<p class="mf1-box-label">Je li bitan režim ili trenje uz stijenku?</p>

Izračunaj **Reynoldsov broj** $Re$ (cijev, granični sloj, ležaj) i protumači ga za konkretnu geometriju. On mjeri relativnu važnost inercije i viskoznosti, ali prijelaz ne određuje bez podataka o stabilnosti toka i poremećajima.
:::

::: {.mf1-decision-step}
<span class="mf1-step-index">3</span>

<p class="mf1-box-label">Ima li kapljica, mlaza ili mjehura?</p>

Tada je važna napetost → **Weberov broj** $We$ (inercija vs napetost) i **Bondov broj** $Bo$ (gravitacija vs napetost). Usporedi $L$ s kapilarnom duljinom $L_c$.
:::

::: {.mf1-decision-step}
<span class="mf1-step-index">4</span>

<p class="mf1-box-label">Može li tlak pasti do isparavanja?</p>

U suženjima, na vijku i usisu crpke → **kavitacijski broj** $\sigma_{kav}$. Usporedba s kritičnom vrijednošću vrijedi samo za jednako definirane referentne veličine i odgovarajuću karakteristiku iste vrste uređaja.
:::

::: {.mf1-decision-step}
<span class="mf1-step-index">5</span>

<p class="mf1-box-label">Postoje li periodičke sile ili vibracije?</p>

Vrtložno otpuštanje iza tijela → **Strouhalov broj** $St$. Provjeri može li nastupiti rezonancija s konstrukcijom.
:::

::: {.mf1-decision-step}
<span class="mf1-step-index">6</span>

<p class="mf1-box-label">Je li brzina plina velika?</p>

Ako se $v$ približava brzini zvuka → provjeri **Machov broj** $Ma$. Za $Ma<0{,}3$ nestlačiva aproksimacija često je dobra ako nema velikih toplinskih, tlačnih ni sastavnih promjena; pretpostavku ipak treba provjeriti za konkretan problem.
:::

::: {.mf1-decision-step}
<span class="mf1-step-index">7</span>

<p class="mf1-box-label">Što tražiš kao izlaz?</p>

Otpor tijela → **koeficijent otpora** $C_d$; pad tlaka u cijevi → **koeficijent trenja** $\lambda$; raspodjela tlaka po plohi → **koeficijent tlaka** $C_p$.
:::
:::

## Riješeni primjeri

::: {#ex-u14-reynoldsov-broj-u-dva-sustava-iste-geometrije .mf1-we}
<p class="mf1-box-label">Riješeni primjer — Reynoldsov broj u dva sustava iste geometrije&nbsp;<span class="mf1-level">T1</span></p>

**Kontekst:** Mikrohladnjak za snažnu elektroniku ima kanal istog promjera kojim nekad teče rashladna voda, a nekad hidrauličko ulje. Iako je geometrija identična, režim strujanja je posve drukčiji jer ga ne određuje geometrija nego omjer sila.

**Zadano**

- Promjer kanala: $D = 6\ \text{mm}$ (zajednički)
- Voda: $v_A = 1{,}2\ \text{m/s}$, $\nu_v = 1{,}0 \cdot 10^{-6}\ \text{m}^2/\text{s}$
- Ulje: $v_B = 0{,}30\ \text{m/s}$, $\nu_u = 4{,}0 \cdot 10^{-5}\ \text{m}^2/\text{s}$

**Traženo**

1. Reynoldsov broj i režim u oba slučaja.
2. brzinu vode koja odgovara orijentacijskoj vrijednosti $Re=2300$.

![Isti kanal, dva fluida: voda daje turbulentni režim (Re = 7200), ulje izrazito laminarni (Re = 45) jer veća viskoznost guši inerciju](../assets/print/u14_val1_reynolds_kanal.svg){#fig-u14-val1-reynolds fig-align="center" fig-alt="Isti kanal, dva fluida: voda daje turbulentni režim (Re = 7200), ulje izrazito laminarni (Re = 45) jer veća viskoznost guši inerciju"}

**Pretpostavke i model**

Strujanje je razvijeno u ravnoj cijevi kružnog presjeka. Koristi se $Re = vD/\nu$; vrijednost $Re=2300$ uzima se kao orijentacijska donja granica prijelaznoga područja, a ne kao univerzalna točka prijelaza [@white2011].

**Rješenje**

Za vodu:

$$
Re_A = \frac{v_A D}{\nu_v} = \frac{1{,}2 \cdot 0{,}006}{1{,}0 \cdot 10^{-6}} = 7200 \quad (>4000 \Rightarrow \text{turbulentno}).
$$ {#eq-slicnost-rijeseni-primjer-reynoldsov-broj-u-dva-sustava-01}

Za ulje:

$$
Re_B = \frac{v_B D}{\nu_u} = \frac{0{,}30 \cdot 0{,}006}{4{,}0 \cdot 10^{-5}} = 45 \quad (\ll 2300 \Rightarrow \text{izrazito laminarno}).
$$ {#eq-slicnost-rijeseni-primjer-reynoldsov-broj-u-dva-sustava-02}

Brzina vode koja odgovara $Re=2300$:

$$
v_{kr} = \frac{Re_{kr}\,\nu_v}{D} = \frac{2300 \cdot 1{,}0 \cdot 10^{-6}}{0{,}006} \approx 0{,}383\ \text{m/s}.
$$ {#eq-slicnost-rijeseni-primjer-reynoldsov-broj-u-dva-sustava-03}

**Provjera i komentar**

1. Pri istom $D$ i sličnom redu veličine brzine, $Re$ se razlikuje oko 160 puta — režim određuje omjer sila, ne oblik kanala.
2. Pri zadanoj brzini ulje ima vrlo malen $Re$, pa viskozni učinci snažno prigušuju poremećaje. Pri dovoljno većoj brzini i njegov bi se režim mogao promijeniti.
3. Za vodu je $Re=7200$ iznad uobičajenoga prijelaznog područja razvijenog toka u kružnoj cijevi, pa se u tehničkim ulaznim uvjetima očekuje turbulentan tok. Posljedice za prijenos topline traže i toplinsku analizu.
:::

::: {#ex-u14-froudeova-slicnost-model-broda-u-vucnom-bazenu .mf1-we}
<p class="mf1-box-label">Riješeni primjer — Froudeova sličnost: model broda u vučnom bazenu&nbsp;<span class="mf1-level">T2</span></p>

**Kontekst:** Brod se prije gradnje ispituje kao umanjeni model u vučnom bazenu. Otpor valova ovisi o Froudeovom broju, pa se brzina modela bira tako da Froudeov broj modela bude jednak onom prototipa.

**Zadano**

- Duljina broda: $L_s = 150\ \text{m}$
- Projektna brzina broda: $v_s = 9{,}0\ \text{m/s}$
- Mjerilo modela: $\lambda_L = 25$
- $\nu = 1{,}0 \cdot 10^{-6}\ \text{m}^2/\text{s}$, $g = 9{,}81\ \text{m/s}^2$

**Traženo**

1. duljinu i brzinu modela iz uvjeta $Fr_m = Fr_s$.
2. Froudeov broj te omjer Reynoldsovih brojeva prototipa i modela.
3. objašnjenje zašto se Reynoldsova sličnost ne može istovremeno zadovoljiti.

![Model broda (Lₘ = 6 m, vₘ = 1,8 m/s) i prototip (Lₛ = 150 m, vₛ = 9 m/s) pri istom Froudeovom broju Fr = 0,235; Reynoldsov broj se razlikuje 125 puta](../assets/print/u14_val2_brod_bazen.svg){#fig-u14-val2-brod fig-align="center" fig-alt="Model broda (Lₘ = 6 m, vₘ = 1,8 m/s) i prototip (Lₛ = 150 m, vₛ = 9 m/s) pri istom Froudeovom broju Fr = 0,235; Reynoldsov broj se razlikuje 125 puta"}

**Pretpostavke i model**

Dominira otpor valova → bira se Froudeova sličnost, $Fr_m = Fr_s$. Geometrijska sličnost daje $L_m = L_s/\lambda_L$.

**Rješenje**

Duljina modela:

$$
L_m = \frac{L_s}{\lambda_L} = \frac{150}{25} = 6{,}0\ \text{m}.
$$ {#eq-slicnost-rijeseni-primjer-froudeova-slicnost-model-broda-01}

Iz $Fr_m = Fr_s$, tj. $v_m/\sqrt{gL_m} = v_s/\sqrt{gL_s}$, slijedi $v_m = v_s/\sqrt{\lambda_L}$:

$$
v_m = \frac{v_s}{\sqrt{\lambda_L}} = \frac{9{,}0}{\sqrt{25}} = 1{,}8\ \text{m/s}.
$$ {#eq-slicnost-rijeseni-primjer-froudeova-slicnost-model-broda-02}

Froudeov broj (jednak na modelu i prototipu):

$$
Fr = \frac{v_s}{\sqrt{g L_s}} = \frac{9{,}0}{\sqrt{9{,}81 \cdot 150}} \approx 0{,}235.
$$ {#eq-slicnost-rijeseni-primjer-froudeova-slicnost-model-broda-03}

Reynoldsovi brojevi: $Re_s = v_s L_s/\nu = 1{,}35 \cdot 10^{9}$, $Re_m = v_m L_m/\nu = 1{,}08 \cdot 10^{7}$, pa je

$$
\frac{Re_s}{Re_m} = \lambda_L^{3/2} = 25^{1{,}5} = 125.
$$ {#eq-slicnost-rijeseni-primjer-froudeova-slicnost-model-broda-04}

**Provjera i komentar**

1. Model je kraći (mjerilo 25) i sporiji ($\sqrt{25} = 5$ puta) — to je posljedica Froudeove sličnosti.
2. Za jednak $Re$ model bi morao ići $v_m = v_s\,\lambda_L = 225\ \text{m/s}$, što je praktično neostvarivo i neprikladno za ovakav bazenski pokus; Froudeova i Reynoldsova sličnost ne mogu se zadovoljiti istovremeno istim fluidom i ovim mjerilom.
3. Zato se otpor razdvaja: valni se doprinos prenosi prvenstveno Froudeovom sličnošću, a viskozni se doprinos procjenjuje odgovarajućim korekcijskim postupkom [@ittc].
:::

::: {#ex-u14-kavitacija-u-venturijevom-suzenju-t2 .mf1-we}
<p class="mf1-box-label">Riješeni primjer — Kavitacija u Venturijevom suženju&nbsp;<span class="mf1-level">T2</span></p>

**Kontekst:** U usisnom vodu crpke ugrađen je Venturijev mjerač. Pri velikom protoku tlak u grlu može pasti do tlaka isparavanja, pa nastaje kavitacija — buka, erozija i pad protoka.

**Zadano**

- Promjer ulaza: $D_1 = 60\ \text{mm}$, promjer grla: $D_2 = 20\ \text{mm}$
- Protok: $Q = 6{,}0\ \text{L/s}$
- Ulazni (apsolutni) tlak: $p_1 = 101{,}3\ \text{kPa}$
- Voda: $\rho = 1000\ \text{kg/m}^3$, $p_v = 2340\ \text{Pa}$

**Traženo**

1. brzine $v_1$ i $v_2$.
2. tlak u grlu prema Bernoulliju i zaključak o kavitaciji.
3. kavitacijski broj i idealizirani granični protok prema uvjetu $p_2=p_v$.

![Venturijevo suženje s idealiziranim kriterijem dosezanja tlaka pare u grlu; jednofazni Bernoullijev model pri Q = 6 L/s daje nefizikalan tlak, a procjena praga iznosi Q približno 4,45 L/s.](../assets/print/u14_val3_venturi_kavitacija.svg){#fig-u14-val3-venturi fig-align="center" fig-alt="Venturijevo suženje s idealiziranim kriterijem dosezanja tlaka pare u grlu; jednofazni Bernoullijev model pri Q = 6 L/s daje nefizikalan tlak, a procjena praga iznosi Q približno 4,45 L/s."}

**Pretpostavke i model**

Strujanje je idealno do grla (Bernoulli bez gubitaka), vodoravna os ($z_1 = z_2$). Kontinuitet daje brzine, a uvjet $p_2=p_v$ služi kao idealizirani ravnotežni kriterij početka isparavanja; stvarna kavitacijska incipijencija ovisi i o gubitcima, jezgrama kavitacije, geometriji i trajanju izloženosti.

**Rješenje**

Površine i brzine:

$$
A_1 = \frac{\pi D_1^2}{4} = 2{,}827 \cdot 10^{-3}\ \text{m}^2, \qquad v_1 = \frac{Q}{A_1} = 2{,}12\ \text{m/s},
$$ {#eq-slicnost-rijeseni-primjer-kavitacija-u-venturijevom-suzen-01}

$$
A_2 = \frac{\pi D_2^2}{4} = 3{,}142 \cdot 10^{-4}\ \text{m}^2, \qquad v_2 = \frac{Q}{A_2} = 19{,}10\ \text{m/s}.
$$ {#eq-slicnost-rijeseni-primjer-kavitacija-u-venturijevom-suzen-02}

Tlak u grlu iz Bernoullija:

$$
p_2 = p_1 + \tfrac{1}{2}\rho\,(v_1^2 - v_2^2) = 101\,300 + 500\,(2{,}12^2 - 19{,}10^2) \approx -78{,}8\ \text{kPa}.
$$ {#eq-slicnost-rijeseni-primjer-kavitacija-u-venturijevom-suzen-03}

Predviđeni apsolutni tlak je negativan — fizikalno nemoguć i jasan znak sloma jednofaznoga idealnog modela. Idealizirani granični protok prema uvjetu $p_2=p_v$ slijedi uz $v_1=(A_2/A_1)v_2$:

$$
v_{2,\max} = \sqrt{\frac{p_1 - p_v}{\tfrac{1}{2}\rho\,(1 - (A_2/A_1)^2)}} \approx 14{,}16\ \text{m/s}, \qquad
Q_{\max} = A_2 v_{2,\max} \approx 4{,}45\ \text{L/s}.
$$ {#eq-slicnost-rijeseni-primjer-kavitacija-u-venturijevom-suzen-04}

Kavitacijski broj pri radnom protoku ($v_2 = 19{,}10\ \text{m/s}$):

$$
\sigma_{kav} = \frac{p_1 - p_v}{\tfrac{1}{2}\rho v_2^2} = \frac{101\,300 - 2340}{500 \cdot 19{,}10^2} \approx 0{,}543.
$$ {#eq-slicnost-rijeseni-primjer-kavitacija-u-venturijevom-suzen-05}

**Provjera i komentar**

1. Suženje 9 puta (po površini) daje 9 puta veću brzinu u grlu, pa kvadratni član u Bernoulliju naglo obara tlak.
2. Negativan apsolutni tlak pokazuje da jednofazni Bernoullijev rezultat pri $6\ \text{L/s}$ nije fizički ostvariv; u stvarnom toku treba očekivati promjenu režima i provjeriti pojavu kavitacije odgovarajućim modelom ili mjerenjem.
3. Vrijednost $\approx4{,}4\ \text{L/s}$ samo je prag idealiziranoga kriterija za zadane ulazne podatke, a ne zajamčen dopušteni protok crpke. Pogonska provjera traži stvarne gubitke, temperaturu, karakteristiku incipijencije i odgovarajući NPSH.
:::

::: {#ex-u14-weberov-i-bondov-broj-raspad-kapi-u .mf1-we}
<p class="mf1-box-label">Riješeni primjer — Weberov i Bondov broj: raspad kapi u struji zraka&nbsp;<span class="mf1-level">T2</span></p>

**Kontekst:** Mlaznica raspršuje kap koja se relativnom brzinom giba kroz zrak. Hoće li se kap raspasti ovisi o tome nadvlada li inercija struje zraka silu površinske napetosti koja drži kap na okupu.

**Zadano**

- Promjer kapi: $d = 3\ \text{mm}$, relativna brzina: $v = 25\ \text{m/s}$
- Zrak: $\rho_{zr} = 1{,}2\ \text{kg/m}^3$; voda: $\rho_v = 1000\ \text{kg/m}^3$, $\sigma = 0{,}072\ \text{N/m}$
- Orijentacijski kritični Weberov broj za odabrani pojednostavljeni režim raspada: $We_{kr}=12$

**Traženo**

1. Weberov broj (s gustoćom zraka) i prosudbu raspada.
2. Bondov broj i usporedbu gravitacije s napetošću.
3. kritičnu brzinu pri kojoj počinje raspad.

![Kap promjera d = 3 mm u struji zraka: zadani kriterij We_kr = 12 predviđa početak raspada pri We = 31,3; Bo je reda jedan.](../assets/print/u14_val4_kap_raspad.svg){#fig-u14-val4-kap fig-align="center" fig-alt="Kap promjera d = 3 mm u struji zraka: zadani kriterij We_kr = 12 predviđa početak raspada pri We = 31,3; Bo je reda jedan."}

**Pretpostavke i model**

Aerodinamičko opterećenje kapi normira se gustoćom zraka, pa ona ulazi u Weberov broj. U ovom se primjeru početak raspada prosuđuje samo prema zadanom pragu $We_{kr}=12$; zanemaruju se viskoznost, vremenski razvoj deformacije i različiti režimi sekundarnog raspada.

**Rješenje**

Weberov broj:

$$
We = \frac{\rho_{zr}\,v^2\,d}{\sigma} = \frac{1{,}2 \cdot 25^2 \cdot 0{,}003}{0{,}072} \approx 31{,}3 \quad (>12 \Rightarrow \text{zadani kriterij predviđa početak raspada}).
$$ {#eq-slicnost-rijeseni-primjer-weberov-i-bondov-broj-raspad-01}

Bondov broj:

$$
Bo = \frac{(\rho_v-\rho_{zr})g\,d^2}{\sigma}
= \frac{(1000-1{,}2)\cdot9{,}81\cdot0{,}003^2}{0{,}072}
\approx1{,}22.
$$ {#eq-slicnost-rijeseni-primjer-weberov-i-bondov-broj-raspad-02}

Kapilarna duljina $L_c=\sqrt{\sigma/[(\rho_v-\rho_{zr})g]}\approx2{,}71\ \text{mm}$ blizu je $d$, pa je $Bo$ reda jedan. Kritična brzina prema **zadanom** kriteriju $We=12$ glasi:

$$
v_{kr} = \sqrt{\frac{We_{kr}\,\sigma}{\rho_{zr}\,d}} = \sqrt{\frac{12 \cdot 0{,}072}{1{,}2 \cdot 0{,}003}} \approx 15{,}5\ \text{m/s}.
$$ {#eq-slicnost-rijeseni-primjer-weberov-i-bondov-broj-raspad-03}

**Provjera i komentar**

1. $We\approx31$ premašuje zadani prag, pa pojednostavljeni kriterij predviđa početak raspada. Ne daje veličinu ni raspodjelu nastalih kapljica i zato sam ne dokazuje „bolju atomizaciju”.
2. $Bo\approx1$ pokazuje da gravitacija može utjecati na statičku deformaciju kapi te veličine; stvarni dinamički oblik ovisi i o aerodinamičkom i viskoznom opterećenju.
3. Vrijednost $15{,}5\ \text{m/s}$ granica je samo ovoga kriterija. Stvarna granica ovisi o dodatnim grupama i početnim uvjetima. Skok tlaka u približno sfernoj kapi povezan je izrazom $\Delta p=4\sigma/d$ iz <span class="mf1-ch-ref"><span class="mf1-ch-code">pog. 2</span><span class="mf1-ch-title">Reologija, viskoznost i međupovršinske pojave</span></span>.
:::

::: {#ex-u14-buckinghamova-analiza-otpora-kugle-i-krivulja-cd .mf1-ch}
<p class="mf1-box-label">Cjeloviti zadatak — Buckinghamova analiza otpora kugle i krivulja Cd(Re)&nbsp;<span class="mf1-level">T3</span></p>

**Kontekst:** Za izoliranu glatku kuglu u jednolikoj nestlačivoj struji dimenzijska analiza pokazuje da se, unutar zadanih pretpostavki, koeficijent otpora može prikazati krivuljom $C_d(Re)$. Hrapavost, blizina stijenke, slobodna turbulencija ili stlačivost tražili bi dodatne parametre.

**Zadano**

- Promjer kugle: $D = 20\ \text{mm}$, brzina struje: $v = 30\ \text{m/s}$
- Zrak: $\rho = 1{,}2\ \text{kg/m}^3$, $\nu = 1{,}5 \cdot 10^{-5}\ \text{m}^2/\text{s}$
- Izmjereni koeficijent otpora u radnom području: $C_d = 0{,}45$ (vrijedi za $Re \sim 10^4$–$10^5$)

**Traženo**

1. popis varijabli i broj $\Pi$-grupa po Buckinghamovom teoremu.
2. Reynoldsov broj struje.
3. silu otpora i vrijednost grupe $\Pi_1 = F_D/(\rho v^2 D^2)$.

![Kugla u struji i krivulja C_d(Re) za zadanu glatku, izoliranu geometriju, s označenom radnom točkom.](../assets/print/u14_ch1_kugla_struja.svg){#fig-u14-ch1-kugla fig-align="center" fig-alt="Kugla u struji i krivulja C_d(Re) za zadanu glatku, izoliranu geometriju, s označenom radnom točkom."}

**Pretpostavke i model**

Kugla je glatka, struja ustaljena i nestlačiva ($Ma < 0{,}3$). Koristi se $\Pi$-rezultat $C_d = f(Re)$ s izmjerenom vrijednošću.

**Rješenje**

### 1. Dimenzijska analiza

Varijable $\{F_D, \rho, v, D, \mu\}$ daju $n = 5$, dimenzije $\mathsf{M}, \mathsf{L}, \mathsf{T}$ daju $k = 3$, pa nastaju $\Pi = 5 - 3 = 2$ grupe:

$$
\Pi_1 = \frac{F_D}{\rho v^2 D^2}, \qquad \Pi_2 = \frac{\rho v D}{\mu} = Re \quad\Rightarrow\quad C_d = f(Re).
$$ {#eq-slicnost-1-dimenzijska-analiza-01}

#### 2. Reynoldsov broj

$$
Re = \frac{v D}{\nu} = \frac{30 \cdot 0{,}020}{1{,}5 \cdot 10^{-5}} = 4{,}0 \cdot 10^{4}.
$$ {#eq-slicnost-2-reynoldsov-broj-01}

#### 3. Sila otpora i grupa Π₁

Čeona površina $A = \pi D^2/4 = 3{,}142 \cdot 10^{-4}\ \text{m}^2$. Sila otpora:

$$
F_D = C_d\,\tfrac{1}{2}\rho v^2 A = 0{,}45 \cdot \tfrac{1}{2} \cdot 1{,}2 \cdot 30^2 \cdot 3{,}142 \cdot 10^{-4} \approx 0{,}0763\ \text{N} \approx 76{,}3\ \text{mN}.
$$ {#eq-slicnost-3-sila-otpora-i-grupa-1-01}

Vrijednost prve grupe:

$$
\Pi_1 = \frac{F_D}{\rho v^2 D^2} = \frac{0{,}0763}{1{,}2 \cdot 30^2 \cdot 0{,}020^2} \approx 0{,}177 = C_d \cdot \frac{\pi}{8}.
$$ {#eq-slicnost-3-sila-otpora-i-grupa-1-02}

**Provjera i komentar**

1. $\Pi$-teorem reducira problem s pet varijabli na funkciju jedne varijable ($Re$) unutar navedenih pretpostavki. Time se mjerenja organiziraju u prenosivu krivulju, ali samu krivulju i njezinu nesigurnost i dalje treba odrediti podatcima.
2. Veza $\Pi_1 = C_d\,\pi/8$ pokazuje da su $\Pi_1$ i $C_d$ ista informacija, samo različito normirana (čeona površina umjesto $D^2$).
3. Granica modela: za glatku kuglu u struji male slobodne turbulencije otporna kriza javlja se približno pri $Re$ reda nekoliko $10^5$, kada prijelaz graničnog sloja odgađa odvajanje i $C_d$ naglo pada. Položaj krize osjetljiv je na hrapavost i poremećaje, pa zadani konstantni $C_d=0{,}45$ vrijedi samo u radnom području zadatka.
:::

::: {.mf1-interaktivno}
<p class="mf1-box-label">Interaktivni prikaz — Krivulja otpora glatke izolirane kugle</p>

Interaktivni prikaz crta krivulju $C_d(Re)$ za zadani model glatke izolirane kugle i pomiče radnu točku s promjenom brzine, promjera, viskoznosti i gustoće. Mala kugla u ulju i veća kugla u zraku mogu ležati na istoj krivulji kada, uz jednak $Re$, dijele i ostale pretpostavke modela.

<div class="mf1-interaktivno-akcija">
<a class="mf1-interaktivno-veza" href="https://martibasic.github.io/MF1_udzbenik/jlite/lab/index.html?path=u14_cd_re_kugla.ipynb">Pokreni u pregledniku</a>
<a class="mf1-interaktivno-veza" href="https://colab.research.google.com/github/martibasic/MF1_udzbenik/blob/main/notebooks/u14_cd_re_kugla.ipynb" target="_blank" rel="noopener">Pričuvno: otvori u Colabu</a>
<img class="mf1-interaktivno-qr" src="../assets/qr/u14_cd_re_kugla.svg" alt="QR kod za interaktivni prikaz krivulje Cd(Re) za glatku izoliranu kuglu"/>
</div>

<div class="mf1-interaktivno-pitanja">
**Pitanja za samostalno istraživanje:** (a) Kako namjestiti vodu i zrak da postignu isti $Re$, i zašto im je tada $C_d$ jednak iako su sile otpora različite? (b) Ispod kojeg $Re$ krivulja prelazi u Stokesov režim $C_d = 24/Re$ i što to znači za taloženje sitnih čestica? (c) Pri fiksnom $C_d$, zašto udvostručenje brzine daje četverostruku silu otpora?
</div>
:::

::: {#ex-u14-machov-i-strouhalov-broj-stlacivost-i-vrtlozno .mf1-we}
<p class="mf1-box-label">Riješeni primjer — Machov i Strouhalov broj: stlačivost i vrtložno otpuštanje&nbsp;<span class="mf1-level">T2</span></p>

**Kontekst:** Dva pitanja koja statički $Re$ i $Fr$ ne hvataju: smije li se brzi protok zraka računati kao nestlačiv (Mach), i kojom frekvencijom dimnjak otpušta vrtloge na vjetru (Strouhal), uz rizik rezonancije.

**Zadano**

- Zrak u vodu promjera $D = 80\ \text{mm}$; protoci $Q_1 = 0{,}40\ \text{m}^3/\text{s}$ i $Q_2 = 0{,}80\ \text{m}^3/\text{s}$; brzina zvuka $a = 340\ \text{m/s}$
- Dimnjak promjera $D_d = 2{,}0\ \text{m}$ na vjetru $v = 12\ \text{m/s}$; $St \approx 0{,}2$; vlastita frekvencija konstrukcije $f_n = 0{,}6\ \text{Hz}$

**Traženo**

1. Machov broj pri oba protoka i granični protok za $Ma = 0{,}3$.
2. frekvenciju otpuštanja vrtloga iza dimnjaka i opasnu brzinu vjetra (rezonancija).

![Lijevo: plinski vod s Ma₁ = 0,234, pri kojem je nestlačiva aproksimacija često prihvatljiva, i Ma₂ = 0,468, pri kojem stlačivost treba uključiti. Desno: dimnjak s procijenjenom frekvencijom vrtložnog otpuštanja.](../assets/print/u14_val5_mach_strouhal.svg){#fig-u14-val5-mach fig-align="center" fig-alt="Lijevo: plinski vod s Ma₁ = 0,234, pri kojem je nestlačiva aproksimacija često prihvatljiva, i Ma₂ = 0,468, pri kojem stlačivost treba uključiti. Desno: dimnjak s procijenjenom frekvencijom vrtložnog otpuštanja."}

**Pretpostavke i model**

Mach: $Ma=v/a$, uz $Ma=0{,}3$ kao čest orijentacijski prag za utjecaj promjene gustoće zbog brzine. Strouhal: $f=St\,v/D$; podudaranje s vlastitom frekvencijom upozorava na moguću rezonanciju, čiji odziv ovisi i o prigušenju, pobudi te području sinkronizacije vrtloga.

**Rješenje**

Površina voda $A = \pi D^2/4 = 5{,}027 \cdot 10^{-3}\ \text{m}^2$. Brzine i Machovi brojevi:

$$
v_1 = \frac{Q_1}{A} = 79{,}6\ \text{m/s}, \quad Ma_1 = \frac{v_1}{a} = 0{,}234 \quad (\text{nestlačiva aproksimacija često je prihvatljiva}),
$$ {#eq-slicnost-rijeseni-primjer-machov-i-strouhalov-broj-stlaci-01}

$$
v_2 = \frac{Q_2}{A} = 159{,}2\ \text{m/s}, \quad Ma_2 = \frac{v_2}{a} = 0{,}468 \quad (\text{stlačivost treba uključiti}).
$$ {#eq-slicnost-rijeseni-primjer-machov-i-strouhalov-broj-stlaci-02}

Granični protok za $Ma = 0{,}3$ ($v = 102\ \text{m/s}$): $Q_{lim} = A \cdot 102 \approx 0{,}513\ \text{m}^3/\text{s}$.

Frekvencija otpuštanja vrtloga iza dimnjaka:

$$
f = \frac{St\,v}{D_d} = \frac{0{,}2 \cdot 12}{2{,}0} = 1{,}2\ \text{Hz}.
$$ {#eq-slicnost-rijeseni-primjer-machov-i-strouhalov-broj-stlaci-03}

Opasna (rezonantna) brzina vjetra, kad je $f = f_n$:

$$
v_{rez} = \frac{f_n\,D_d}{St} = \frac{0{,}6 \cdot 2{,}0}{0{,}2} = 6{,}0\ \text{m/s}.
$$ {#eq-slicnost-rijeseni-primjer-machov-i-strouhalov-broj-stlaci-04}

**Provjera i komentar**

1. Udvostručenje zadanoga lokalnog protoka povećava $Ma$ iz 0,234 na 0,468. U prvom je stanju aproksimacija konstantne gustoće često prihvatljiva ako nema velikih toplinskih ni tlačnih promjena; u drugom se stlačivost ne smije zanemariti. To nije kriterij opće valjanosti Bernoullijeve jednadžbe, nego kriterij modeliranja gustoće.
2. Pri vjetru oko $6\ \text{m/s}$ procijenjena se frekvencija vrtloga poklapa s vlastitom frekvencijom dimnjaka, pa postoji mogućnost rezonantnog odziva i zamora. Spiralne trake ili prigušivači mogu ga ublažiti, ali izbor mjere traži aeroelastičku i konstrukcijsku provjeru.
3. Strouhalov broj povezuje brzinu, veličinu i frekvenciju, pa služi i kao princip vrtložnog mjerača protoka (iz izmjerene frekvencije računa se brzina).
:::

::: {.mf1-samoprovjera}
<p class="mf1-box-label">Provjeri sebe</p>

Sljedeća pitanja služe za samostalnu provjeru prije zadataka za vježbu. Preporučuje se prvo samostalno odgovoriti, a tek zatim otvoriti sklopivi blok.

1. Zašto se inercijska sila uzima kao referenca u većini bezdimenzijskih brojeva?

::: {.callout-note collapse="true"}
### Odgovor
Inercija je prisutna u gotovo svakom gibanju fluida, pa je prirodna referenca za $Re$, $Fr^2$, $Eu$, $We$ i srodne omjere. Ipak, nije svaki broj izravan omjer sila: $St$ uspoređuje vremenske skale, $Ma$ brzine, a $C_d$ je normirani odziv.
:::

2. Brod i njegov model ispituju se pri jednakom Froudeovom broju. Zašto se istovremeno ne može osigurati i jednak Reynoldsov broj?

::: {.callout-note collapse="true"}
### Odgovor
Za isti fluid jednak Froude traži da model bude sporiji ($v_m=v_p/\sqrt{\lambda_L}$), a jednak Reynolds da bude brži ($v_m=v_p\lambda_L$). Zato se za valni problem prioritetno čuva $Fr$, a učinak nejednakog $Re$ procjenjuje korekcijskim postupkom i ispitivanjem osjetljivosti.
:::

3. Koliko $\Pi$-grupa daje problem s 6 fizikalnih veličina i 3 neovisne dimenzije, i što to znači?

::: {.callout-note collapse="true"}
### Odgovor
Daje $6-3=3$ bezdimenzijske grupe. Problem se zato može opisati funkcijom triju bezdimenzijskih parametara umjesto šest dimenzijskih varijabli. Rezultat je prenosiv samo unutar pretpostavki i raspona u kojima su odabrane varijable potpune.
:::

4. U kojem se području Machovog broja strujanje smije računati kao nestlačivo i zašto je to važno za MF1?

::: {.callout-note collapse="true"}
### Odgovor
Za mnoga plinska strujanja bez velikog zagrijavanja i tlačnih promjena $Ma<0{,}3$ znači da su promjene gustoće zbog brzine male, pa je nestlačiva aproksimacija često prihvatljiva. To nije dovoljan uvjet ako se gustoća znatno mijenja zbog temperature, sastava ili nametnutoga tlaka.
:::

5. Kako se odlučuje koje brojeve treba očuvati pri modelskom ispitivanju?

::: {.callout-note collapse="true"}
### Odgovor
Najprije se popišu svi mehanizmi i bezdimenzijski rubni uvjeti koji mogu utjecati na traženi rezultat. Procjenom reda veličine izdvajaju se grupe koje nisu zanemarive. Kod slobodne površine često je prioritetan $Fr$, u cijevi su važni $Re$ i $\varepsilon/D$, a kod kapljica uz $We$ često treba provjeriti i viskozni učinak. Jedna dominantna grupa dovoljna je samo ako su ostale doista zanemarive ili jednake.
:::
:::

## Zadaci za vježbu

Šest zadataka napreduje od izravnog računanja dviju grupa, preko izbora referentnih veličina, do samostalne Buckinghamove analize i procjene mjerilnog učinka u modelskom ispitivanju.

::::: {.mf1-vjezbe-list}
1. [**T1**]{#task-u14-krv-tece-arteriolom-promjera-brzinom-a-voda} Krv teče arteriolom promjera $D = 0{,}3\ \text{mm}$ brzinom $v = 5\ \text{mm/s}$ ($\nu = 3{,}3 \cdot 10^{-6}\ \text{m}^2/\text{s}$), a voda gradskim vodom promjera $D = 0{,}3\ \text{m}$ brzinom $v = 1{,}5\ \text{m/s}$ ($\nu = 1{,}0 \cdot 10^{-6}\ \text{m}^2/\text{s}$). Odredi Reynoldsov broj u oba slučaja i prosudi koja sila dominira.

   :::: {.content-visible .mf1-hint-online when-format="html"}
   ::: {.callout-note collapse="true" data-hint-key="true"}
   ### Naputak
   $Re = vD/\nu$; za kružnu cijev usporedi s orijentacijskim područjima režima, bez prijenosa praga $2300$ na geometriju arteriole.
   :::
   ::::
   :::: {.content-visible .mf1-answer-online when-format="html"}
   ::: {.callout-tip collapse="true" data-answer-key="true"}
   ### Kontrolni rezultat

   $Re_{krv} \approx 0{,}45$ — viskoznost dominira; $Re_{voda} \approx 4{,}5 \cdot 10^5$ — inercija dominira.
   :::
   ::::
   **Skica:** da - dva presjeka cijevi vrlo različitih veličina s označenim $D$, $v$.

2. [**T1**]{#task-u14-zrak-struji-vodom-promjera-lokalnim-volumenskim-protokom} Zrak struji vodom promjera $D = 100\ \text{mm}$ lokalnim volumenskim protokom $Q = 0{,}5\ \text{m}^3/\text{s}$; brzina zvuka $a = 340\ \text{m/s}$. Odredi brzinu i Machov broj te prosudi je li, bez velikih toplinskih i tlačnih promjena, aproksimacija konstantne gustoće razumna.

   :::: {.content-visible .mf1-hint-online when-format="html"}
   ::: {.callout-note collapse="true" data-hint-key="true"}
   ### Naputak
   $v=Q/A$, $Ma=v/a$; vrijednost $0{,}3$ uzmi kao orijentacijski prag.
   :::
   ::::
   :::: {.content-visible .mf1-answer-online when-format="html"}
   ::: {.callout-tip collapse="true" data-answer-key="true"}
   ### Kontrolni rezultat

   $v\approx63{,}7\ \text{m/s}$, $Ma\approx0{,}19$; prema zadanom kriteriju nestlačiva je aproksimacija razumna uz navedene dodatne pretpostavke.
   :::
   ::::
   **Skica:** da - vod zraka s presjekom, oznake $D$, $Q$.

3. [**T2**]{#task-u14-na-referentnom-presjeku-usisa-crpke-apsolutni-tlak} Na referentnom presjeku usisa crpke apsolutni tlak iznosi $p_{ref}=80\ \text{kPa}$, brzina $v_{ref}=4\ \text{m/s}$, gustoća vode $\rho=1000\ \text{kg/m}^3$, a tlak zasićene pare $p_v=2340\ \text{Pa}$. Ispitivanje iste crpke, pri istoj definiciji referentnog presjeka, daje početak kavitacije pri $\sigma_{kr}=3{,}0$. Odredi kavitacijski broj i usporedi ga s kritičnim.

   :::: {.content-visible .mf1-hint-online when-format="html"}
   ::: {.callout-note collapse="true" data-hint-key="true"}
   ### Naputak
   koristi iste referentne veličine kao u definiciji kritične vrijednosti.
   :::
   ::::
   :::: {.content-visible .mf1-answer-online when-format="html"}
   ::: {.callout-tip collapse="true" data-answer-key="true"}
   ### Kontrolni rezultat

   $\sigma_{kav}\approx9{,}7>\sigma_{kr}=3{,}0$; prema zadanoj karakteristici crpka ima rezervu u toj radnoj točki.
   :::
   ::::
   **Skica:** da - usisni vod crpke s označenim $p$, $v$ i razinom $p_v$.

4. [**T2**]{#task-u14-kap-goriva-promjera-izlozena-je-relativnoj-struji} Kap goriva promjera $d=0{,}15\ \text{mm}$ izložena je relativnoj struji zraka brzine $v=80\ \text{m/s}$ ($\rho_{zr}=1{,}2\ \text{kg/m}^3$, $\sigma=0{,}025\ \text{N/m}$). Za ovaj pojednostavljeni slučaj zanemari viskozne učinke i kao orijentacijski prag početka aerodinamičkog raspada uzmi $We_{kr}=12$. Odredi Weberov broj i prosudi predviđa li taj kriterij početak raspada. Objasni zašto iz toga još ne slijedi veličina nastalih kapljica.

   :::: {.content-visible .mf1-hint-online when-format="html"}
   ::: {.callout-note collapse="true" data-hint-key="true"}
   ### Naputak
   izračunaj $We=\rho_{zr}v^2d/\sigma$ i usporedi ga sa zadanim pragom, ali odvoji „početak raspada” od „kvalitete atomizacije”.
   :::
   ::::
   :::: {.content-visible .mf1-answer-online when-format="html"}
   ::: {.callout-tip collapse="true" data-answer-key="true"}
   ### Kontrolni rezultat

   $We\approx46>12$; pojednostavljeni kriterij predviđa raspad, ali bez viskoznosti, omjera gustoća i modela sekundarnog raspada ne određuje raspodjelu veličina kapljica.
   :::
   ::::
   **Skica:** da - mlaznica s kapi u struji zraka, oznake $d$, $v$.

5. [**T3**]{#task-u14-frekvencija-otpustanja-vrtloga-iza-geometrijski-slicnog-tijela} Frekvencija otpuštanja vrtloga $f$ iza geometrijski sličnog tijela ovisi o brzini neporemećene struje $v$, karakterističnoj duljini $D$, gustoći $\rho$ i dinamičkoj viskoznosti $\mu$. Buckinghamovim postupkom, uz ponavljajuće varijable $\rho$, $v$ i $D$, odredi broj $\Pi$-grupa i pokaži da se rezultat može zapisati kao $St=\Phi(Re)$. Zatim za cilindar promjera $D=0{,}050\ \text{m}$ u zraku gustoće $\rho=1{,}20\ \text{kg/m}^3$ i viskoznosti $\mu=1{,}80\cdot10^{-5}\ \text{Pa s}$ pri $v=12{,}0\ \text{m/s}$ izračunaj $Re$ i frekvenciju ako mjerenje za geometrijski sličan slučaj pri tom režimu daje $St=0{,}190$. Objasni zašto vrijednost $St$ nije izvedena samo dimenzijskom analizom.

   :::: {.content-visible .mf1-hint-online when-format="html"}
   ::: {.callout-note collapse="true" data-hint-key="true"}
   ### Naputak
   u popis uključi i zavisnu varijablu $f$; tek potom primijeni $n-k$. Nemoj unaprijed uvrstiti gotove definicije $St$ i $Re$.
   :::
   ::::
   :::: {.content-visible .mf1-answer-online when-format="html"}
   ::: {.callout-tip collapse="true" data-answer-key="true"}
   ### Kontrolni rezultat

   $n=5$, $k=3$, pa nastaju dvije grupe; izborom ponavljajućih varijabli dobivaju se $\Pi_1=fD/v=St$ i $\Pi_2=\rho vD/\mu=Re$, odnosno $St=\Phi(Re)$. Za zadani slučaj $Re=4{,}00\cdot10^4$ i $f=St\,v/D=45{,}6\ \text{Hz}$. Dimenzijska analiza određuje oblik ovisnosti, ali broj $St=0{,}190$ dolazi iz mjerenja ili odgovarajućega modela, ne iz samog Buckinghamova postupka.
   :::
   ::::
   **Skica:** da - tijelo u struji, karakteristična duljina $D$, brzina $v$ i periodična vrtložna staza frekvencije $f$.

6. [**T4**]{#task-u14-preljev-brane-ispituje-se-vodenim-modelom-u} Preljev brane ispituje se vodenim modelom u mjerilu $\lambda_L=30$, pri istom gravitacijskom ubrzanju i gustoći kao prototip. Prototip pri projektnom protoku ima brzinu preljeva $v_p=6{,}0\ \text{m/s}$ i protok $Q_p=480\ \text{m}^3/\text{s}$, a odgovarajuća vodoravna sila iznosi $F_p=220\ \text{kN}$. (a) Iz Froudeove sličnosti odredi brzinu i protok modela. (b) Odredi silu na modelu. (c) Za dubinu na modelu $h_m=0{,}25\ \text{m}$ i $\nu=1{,}0\cdot10^{-6}\ \text{m}^2/\text{s}$ izračunaj $Re_m$. Navedi što velik $Re_m$ sugerira, ali i zašto ne dokazuje da je mjerilna pogreška zbog nejednakog $Re$ mala.

   :::: {.content-visible .mf1-hint-online when-format="html"}
   ::: {.callout-note collapse="true" data-hint-key="true"}
   ### Naputak
   čuvaj $Fr$ te koristi $v_m=v_p/\sqrt{\lambda_L}$, $Q_m=Q_p/\lambda_L^{5/2}$ i, zbog jednake gustoće, $F_m=F_p/\lambda_L^3$. Zatim izračunaj $Re_m=v_mh_m/\nu$.
   :::
   ::::
   :::: {.content-visible .mf1-answer-online when-format="html"}
   ::: {.callout-tip collapse="true" data-answer-key="true"}
   ### Kontrolni rezultat

   $v_m\approx1{,}10\ \text{m/s}$; $Q_m\approx97{,}4\ \text{L/s}$; $F_m\approx8{,}15\ \text{N}$; $Re_m\approx2{,}7\cdot10^5$. Model je vjerojatno turbulentan, ali veličina viskozne mjerilne pogreške mora se provjeriti korekcijom otpora, nizom modelskih mjerila ili podatcima — ne slijedi samo iz oznake „turbulentno”.
   :::
   ::::
   **Skica:** da - preljev brane s modelom i prototipom, slobodna površina, mjerilo $\lambda_L$ i kote $v$, $h_m$.

:::::

![Skice uz zadatke za vježbu — modelska ispitivanja i bezdimenzijski brojevi.](../assets/print/u14_vjezbe_skice.svg){#fig-u14-vjezbe fig-align="center" fig-alt="Skice uz zadatke za vježbu — modelska ispitivanja i bezdimenzijski brojevi."}

::: {.mf1-zavrsni-okvir}
<p class="mf1-box-label">Za ponijeti iz poglavlja</p>

**Sažeta provjera prije računa**

- Treba definirati izlaznu veličinu, geometriju te početne i rubne uvjete.
- Treba popisati sve relevantne bezdimenzijske grupe, procijeniti njihov red veličine i obrazložiti koje se zanemaruju.
- Reynoldsov broj važan je za relativni utjecaj viskoznosti, ali sam ne određuje režim u svakoj geometriji.
- Karakteristična duljina $L$ i brzina $v$ moraju biti dosljedno izabrane.
- Za plin treba provjeriti $Ma$ te moguće toplinske, tlačne i sastavne promjene prije pretpostavke konstantne gustoće.

**Najčešća pogreška**

Najčešća pogreška nije aritmetika nego pokušaj da se istovremeno zadovolje dva broja koja se isključuju (npr. Reynolds i Froude na istom modelu) ili pogrešan izbor karakteristične duljine. Druga je miješanje dvaju $C_d$: koeficijenta otpora tijela i koeficijenta istjecanja otvora iz <span class="mf1-ch-ref"><span class="mf1-ch-code">pog. 13</span><span class="mf1-ch-title">Gubitci, cjevovodi, crpke i mreže</span></span>.

**Nakon ovoga poglavlja mora biti moguće**

1. razlikovati omjere sila, omjere vremenskih ili brzinskih skala i normirane odzive te navesti područje njihove primjene.
2. provesti Buckinghamovu analizu i dobiti $\Pi$-grupe iz popisa varijabli.
3. odlučiti koji broj treba očuvati pri modelskom ispitivanju i objasniti zašto sličnost često nije potpuna.

**U tehnici to znači**

Modelska ispitivanja u bazenu, aerotunelu i na crpkama traže očuvanje relevantnih bezdimenzijskih grupa ili dokumentiranu korekciju neusklađenih grupa. Krivulje poput $C_d(Re)$ i $\lambda(Re,\varepsilon/D)$ mogu se prenositi između veličina i fluida samo uz jednaku bezdimenzijsku geometriju, rubne uvjete i sve ostale važne parametre.

**Granica modela**

Bezdimenzijski brojevi sažimaju fiziku, ali ne zamjenjuju je. Kad dva broja istovremeno postanu važna (npr. $Re$ i $Fr$ kod broda, ili $We$ i $Re$ kod mlaza), potpuna sličnost nije ostvariva i nužne su korekcije ili rastav doprinosa.

**Kamo dalje nakon MF1**

Ovaj kolegij namjerno ostaje u području **integralne** analize nestlačivog strujanja. Teme koje se prirodno nastavljaju, a izlaze iz opsega MF1, spominju se ovdje samo kao putokaz za sljedeće kolegije:

- **granični sloj i otpor tijela** — kako viskoznost uz stijenku stvara otpor i uzgon (koeficijent $C_d$, „otporna kriza" iz ovog poglavlja detaljno se obrađuje u aerodinamici i hidrodinamici);
- **strujanje u otvorenim kanalima** — gdje vlada Froudeov broj, hidraulički skok i preljevi;
- **stlačivo strujanje** — plinodinamika, mlaznice i udarni valovi; $Ma\approx0{,}3$ samo je čest orijentir za procjenu promjene gustoće zbog brzine, a ne granica područja;
- **diferencijalna i računalna dinamika fluida** — Navier-Stokesove jednadžbe po točkama i njihovo numeričko rješavanje (najavljeno kroz oznake *Numerički most* i sažeto u <span class="mf1-ch-ref"><span class="mf1-ch-code">dod. D</span><span class="mf1-ch-title">Numerička mehanika fluida</span></span>).

<span class="mf1-ch-ref"><span class="mf1-ch-code">pog. 11</span><span class="mf1-ch-title">Dimenzijska analiza i sličnost</span></span> zatvara kolegij zajedničkim jezikom omjera mehanizama i normiranih odziva. Ispravno bezdimenzioniranje ne počinje pogađanjem jednoga broja, nego jasnim popisom varijabli, jednadžbi i rubnih uvjeta te obrazloženim izborom relevantnih grupa.
:::

::: {.mf1-numerika}
<p class="mf1-box-label">Numerički most</p>

**Gdje ovo živi u numerici.** Bezdimenzioniranje pokazuje koje parametre numerički model mora očuvati. U najjednostavnijem jednofaznom, nestlačivom toku Newtonova fluida konstantnih svojstava pojavljuje se $Re$; dodatna fizika i rubni uvjeti uvode dodatne grupe. Jednaki brojevi daju jednako bezdimenzijsko polje samo uz jednaku bezdimenzijsku geometriju te iste početne i rubne uvjete.

**Što numerički alat radi s tim.** $Re$ je jedan od ulaza u odluku o laminarnom, RANS, LES ili drugom pristupu, zajedno s geometrijom, nestacionarnošću i traženim rezultatom. Veličina $y^+$ provjerava usklađenost prve ćelije sa zidnom obradom; nije samostalna mjera kvalitete cijele mreže. Koeficijenti $C_d$, $C_p$ i $\lambda$ mogu se izračunati iz numeričkog rješenja kao normirani izlazi.

**Tipičan scenarij.** Pri slobodnoj površini (brod, preljev) dodaje se Froudeov broj i metoda VOF za praćenje granice voda–zrak; kod kapljica i mlaza ulazi Weberov broj. Izbor relevantnih brojeva prije simulacije izravno određuje koja se fizika uopće razrješava.

> *Nije gradivo MF1. U kasnijim kolegijima posvećenima računalnoj dinamici fluida opisani sadržaj postat će poznat teren.*
:::
