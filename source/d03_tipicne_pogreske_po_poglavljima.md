## Tipične pogreške i preventivni filtar prije računa

Ovdje možeš provjeriti odabir modela, referentnog tlaka, kontrolnog volumena i predznaka. Vrati se odgovarajućem poglavlju ovog pregleda prije računa, kad dobiješ neočekivan rezultat i prije predaje zadatka.

## Globalna provjera prije računa

::: {.mf1-checklist}
<p class="mf1-box-label">Brza provjera</p>

- Odaberi model: hidrostatiku, relativno mirovanje, kontinuitet, energijsku bilancu ili bilancu količine gibanja.
- Provjeri pretpostavke i granice primjene modela.
- Nacrtaj skicu, strujnicu ili kontrolni volumen prije prve jednadžbe.
- Uskladi jedinice prije uvrštavanja.
- Provjeri predznak, jedinicu i red veličine rezultata.
:::

<p class="mf1-signal-note">Vizualni tragovi za brzo listanje dodatka: <span class="mf1-signal-chip">ρ / γ / p</span> osnovne veličine, <span class="mf1-signal-chip">μ / ν / σ</span> svojstva fluida, <span class="mf1-signal-chip">F / M</span> sile i momenti, <span class="mf1-signal-chip">Q / ṁ / h<sub>w</sub></span> protoci i gubici.</p>

## Pregled po poglavljima {#tablica-tipičnih-pogrešaka-po-poglavljima}

### 1 · Osnove fluida i Pascalov zakon {#pogreske-tlak .unnumbered .unlisted}

<span class="mf1-signal-chip">ρ / γ / p</span> <span class="mf1-signal-chip">F / A</span>

:::: {.mf1-error-pair}
::: {.mf1-error-column}
**Česta pogreška**

Miješanje mase ulja i posude, gustoće i specifične težine; zamjena omjera površina omjerom promjera; porast sile i pomaka istodobno; zanemarivanje stlačivosti samo zato što je promjena gustoće mala; tumačenje zbroja poteza kao jednog hoda ili zbroja iznosa sila kao rezultantnog vektora.
:::

::: {.mf1-error-column}
**Što provjeriti**

Oduzmi taru, provjeri površine, volumen i rad. Za pogrešku pomaka usporedi volumen stlačivanja s istisnutim volumenom pumpe. Razlikuj puni i djelomični zadnji potez. Izbor pumpe mora zadovoljiti silu i zbroj tlačnih hodova; provjeri krajeve zadanih intervala. Pascalov kvazistatički model ne znači trenutačno širenje tlaka.
:::
::::

### 2 · Reologija, viskoznost i međupovršinske pojave {#pogreske-viskoznost .unnumbered .unlisted}

<span class="mf1-signal-chip">μ / ν / σ</span> <span class="mf1-signal-chip">$\cos\theta$</span>

:::: {.mf1-error-pair}
::: {.mf1-error-column}
**Česta pogreška**

Miješanje dinamičke i kinematičke viskoznosti i njihovih jedinica; isti tlačni skok za kapljicu i sapunasti mjehur; spajanje dvaju procjepa u jedan; zaključak o stalnoj viskoznosti iz jedne mjerne točke; istodobno računanje konkavnoga meniskusa i izlazne kapljice kao neovisnih međupovršina.
:::

::: {.mf1-error-column}
**Što provjeriti**

Utvrdi odgovaraju li pojavi $\mu$, $\nu$ ili $\sigma$. Prebroji međupovršine, na objema stranama pokretne ploče odredi smjer otpora i zbroji sile. Newtonski model provjeri na svim mjernim točkama pri istoj temperaturi. Odvoji punjenje igle od stanja s kapljicom, provjeri granice promjera i usporedi rezervu regulatora sa skalom zanemarenog tlaka kroz kapljicu te ograniči izbor na zadani statički model.
:::
::::

### 3 · Hidrostatička raspodjela tlaka i manometrija {#pogreske-hidrostatika .unnumbered .unlisted}

<span class="mf1-signal-chip">$p_{aps}$</span> <span class="mf1-signal-chip">$p_M$</span> <span class="mf1-signal-chip">$p_v$</span>

:::: {.mf1-error-pair}
::: {.mf1-error-column}
**Česta pogreška**

Miješanje apsolutnog, manometarskog i vakuumskog tlaka; pogrešni predznaci i izostavljen spojni stupac; jedna gustoća za dva sloja; izbor manometra samo prema visini; uporaba statičke usisne visine kao provjere pumpe u radu.
:::

::: {.mf1-error-column}
**Što provjeriti**

Odredi referencu i sve visinske razlike, uključujući položaj granice u manometru. Za slojeve zatvori i ukupnu visinu i tlak. Pri izboru instrumenta provjeri visinu stupca, tlačnu pogrešku i rezervu skale; razlikuj zajamčene granice od standardne nesigurnosti. Za usis pumpe u radu trebaju gubici i brzinska visina te usporedba $NPSH_A$ s proizvođačevim $NPSH_R$, a ne samo $p_{atm}/(\rho g)$.
:::
::::

### 4 · Relativno mirovanje fluida {#pogreske-relativno-mirovanje .unnumbered .unlisted}

<span class="mf1-signal-chip">a / g</span> <span class="mf1-signal-chip">$g_{eff}$</span>

:::: {.mf1-error-pair}
::: {.mf1-error-column}
**Česta pogreška**

Zamjena smjera ubrzanja smjerom brzine; linearna umjesto kvadratne ovisnosti o polumjeru; zaključak o smirivanju iz jednog očitanja; nastavak formule za puni paraboloid nakon prelijevanja ili ogoljavanja.
:::

::: {.mf1-error-column}
**Što provjeriti**

Najprije odredi $\vec g_{eff}$ i provjeriti volumen. Pri vrtnji usporedi oba kritična praga; nakon prvoga mijenja se domena ili volumen. Iz podataka odvojeno provjeri blizinu referentnim razinama i promjenu kroz vrijeme. Uključi granično odstupanje brzine; provjera dubine u ustaljenom stanju sa zatvorenim usisom nije provjera rada s protokom.
:::
::::

### 5 · Hidrostatske sile na plohe {#pogreske-sile-na-plohe .unnumbered .unlisted}

<span class="mf1-signal-chip">$F / y_{CP}$</span> <span class="mf1-signal-chip">$F_H / F_V$</span>

:::: {.mf1-error-pair}
::: {.mf1-error-column}
**Česta pogreška**

Uporaba formule centra tlaka bez provjere referentnog tlaka; tretiranje zakrivljene plohe kao ravne; određivanje predznaka $F_V$ samo iz pomoćnoga volumena; zbrajanje suprotnih tlakova bez predznaka; zamjena težišta trokuta težištem pravokutnika; poistovjećivanje osi u središtu kružnice sa zglobom na kraju luka.
:::

::: {.mf1-error-column}
**Što provjeriti**

Potrebno je zadati orijentaciju plohe i referentni tlak, zasebno zatvoriti silu i moment te za zakrivljenu plohu nacrtati lokalnu normalu od stvarnoga fluida prema stijenci. Projekcija daje $F_H$, pomoćni volumen iznos $|F_V|$, a geometrija stvarnoga fluida njegov smjer. Za dvije razine vode oduzmi sile i njihove momente oko iste točke. Za radijalni poklopac sve normale prolaze kroz središte kružnice; moment težine i kapacitet spojnice provjeravaju se zasebno.
:::
::::

### 6 · Uzgon, plivanje i početni stabilitet {#pogreske-uzgon .unnumbered .unlisted}

<span class="mf1-signal-chip">$F_U$</span> <span class="mf1-signal-chip">$V_{ist}$</span> <span class="mf1-signal-chip">GM / GZ</span>

:::: {.mf1-error-pair}
::: {.mf1-error-column}
**Česta pogreška**

Zamjena volumena tijela istisninom; miješanje ravnoteže s početnom stabilnošću; proglašavanje pozitivnoga $GM$ dokazom konačne ili oštećene stabilnosti; zaključivanje samo iz sniženja $KG$; fiksiranje mase neovisno o nesigurnim uronima.
:::

::: {.mf1-error-column}
**Što provjeriti**

Potrebno je računati stvarnu istisninu i odvojiti bilancu sila od momenata. Pri pokusu nagibanja uteg ulazi u ukupnu masu. Za dodani balast ponovno računaj gaz, $KB$, $BM$ i slobodni bok. U intervalnoj procjeni masa i moment moraju odgovarati istom skupu ulaza. $GM$ vrijedi za početni mali nagib; konačni i oštećeni slučaj traže krivulju $GZ$, otvore, naplavljivanje i mjerodavne kriterije.
:::
::::

### 7 · Kinematika, kontrolni volumen i kontinuitet {#pogreske-kontinuitet .unnumbered .unlisted}

<span class="mf1-signal-chip">$\vec v\!\cdot\!\vec n$</span> <span class="mf1-signal-chip">$\vec v-\vec v_{KP}$</span>

:::: {.mf1-error-pair}
::: {.mf1-error-column}
**Česta pogreška**

Mehaničko pisanje $A_1v_1=A_2v_2$ bez kontrolnog volumena; zamjena kuta prema normali kutom prema plohi; zaboravljena akumulacija; uporaba apsolutne brzine kroz gibajuću plohu; nastavak računa porasta razine nakon prelijevanja.
:::

::: {.mf1-error-column}
**Što provjeriti**

Označi vanjsku normalu, ulaze, izlaze i akumulaciju. Za kosu plohu koristi normalnu komponentu; za gibajući klip tok računaj relativno prema otvoru i zasebno zatvori promjenu volumena komore. Zadani omjer brzina u granama nije posljedica samih promjera. Razlikuj zajamčene intervale od standardne nesigurnosti; nakon dosezanja ruba dodaj preljevni izlaz.
:::
::::

### 8 · Energijska jednadžba i Bernoulli {#pogreske-energija .unnumbered .unlisted}

<span class="mf1-signal-chip">$p/(\rho g)$</span> <span class="mf1-signal-chip">$v^2/(2g)$</span> <span class="mf1-signal-chip">z</span>

:::: {.mf1-error-pair}
::: {.mf1-error-column}
**Česta pogreška**

Pisanje Bernoullija bez odabira presjeka; poistovjećivanje mirne površine s izlaznim mlazom; miješanje tlačne visine i HGL-a; zanemarivanje hidrostatičke korekcije senzora ili jednog od pogonskih zahtjeva.
:::

::: {.mf1-error-column}
**Što provjeriti**

Potrebno je odvojiti brzinu na površini od izlazne brzine, računati HGL kao z+p/(ρg), očitanje senzora prenijeti na visinu mjerne točke te provjeriti obje nejednakosti i krajnje kombinacije zadanih intervala.
:::
::::

### 9 · Kompresibilni idealni tok {#pogreske-kompresibilni-tok .unnumbered .unlisted}

<span class="mf1-signal-chip">$a / (v\pm a)$</span> <span class="mf1-signal-chip">$Ma / p_0$</span>

:::: {.mf1-error-pair}
::: {.mf1-error-column}
**Česta pogreška**

Miješanje brzine zvuka i brzine signala prema laboratoriju; omjeri manometarskih tlakova; poistovjećivanje protutlaka s izlaznim tlakom prigušene sapnice; izentropska relacija kroz udar ili nekorigirana nadzvučna Pitotova sonda.
:::

::: {.mf1-error-column}
**Što provjeriti**

Razlikuj a i v±a, koristi apsolutne tlakove i apsolutnu temperaturu te odaberi režim iz rubnih uvjeta. Kroz normalni udarni val očuvaj masu, količinu gibanja i ukupnu entalpiju, uz pad ukupnog tlaka. Za Z6 mjeri p01 u mirnoj komori uz izentropski dovod, a p02 podzvučnom sondom; usporedi omjere uz kombiniranu standardnu nesigurnost.
:::
::::

### 10 · Količina i moment količine gibanja {#pogreske-kolicina-gibanja .unnumbered .unlisted}

<span class="mf1-signal-chip">$F / R / M$</span>

:::: {.mf1-error-pair}
::: {.mf1-error-column}
**Česta pogreška**

Zamjena sile na fluid silom na konstrukciju; neoznačena ravnina skretanja; kosi razmak umjesto okomitog kraka; sav protok sapnice u bilanci jedne pomične ploče; RSS nad zajamčenim granicama.
:::

::: {.mf1-error-column}
**Što provjeriti**

Označi tlocrt i osi te tlačne sile usmjeri prema KV-u. Razlikuj F i R, moment računaj iz r×F, a dotok kroz pomičnu plohu iz v−u uz apsolutne brzine u bilancama količine gibanja i energije. Provjeri granice maksimuma i puni zadani kriterij nosača. Tlačne i impulsne doprinose zapiši po komponentama; reakcija na konstrukciju ima suprotan predznak od sile konstrukcije na fluid.
:::
::::

### 11 · Dimenzijska analiza i sličnost {#pogreske-slicnost .unnumbered .unlisted}

<span class="mf1-signal-chip">Re / Fr / Ma</span> <span class="mf1-signal-chip">Π</span>

:::: {.mf1-error-pair}
::: {.mf1-error-column}
**Česta pogreška**

Pretlak u kavitacijskom broju; prijenos sile s λ³ bez Froudeove sličnosti; brojčani St izveden samo iz dimenzija; preklapanje intervala kao dokaz male mjerilne pogreške.
:::

::: {.mf1-error-column}
**Što provjeriti**

Provjeri apsolutni referentni tlak, rang matrice i relevantne grupe. Silu prenesi iz jednakosti koeficijenta, provjeri ostvarivost sličnosti te odvoji granice mjerenja od pogreške modela.
:::
::::

### 12 · Diferencijalni opis realnog toka {#pogreske-realni-tok .unnumbered .unlisted}

<span class="mf1-signal-chip">$D\vec v/Dt$</span> <span class="mf1-signal-chip">NS</span> <span class="mf1-signal-chip">V&amp;V</span>

:::: {.mf1-error-pair}
::: {.mf1-error-column}
**Česta pogreška**

Gubitak nestacionarnoga člana; miješanje strujnice i putanje čestice; rješavanje Navier–Stokesovih jednadžbi bez početnih i rubnih uvjeta; poistovjećivanje numeričke konvergencije s validacijom; tumačenje vremenskog mjerila kao točnog vremena uspostave profila ili lokalnog povrata kao prolaza kroz stijenku.
:::

::: {.mf1-error-column}
**Što provjeriti**

Potrebno je zadržati lokalno i konvektivno ubrzanje dok pretpostavke ne uklone članove, zadati materijalni model i rubne uvjete te odvojeno provjeriti jednadžbe, diskretizaciju, očuvanje i usporedbu s mjerenjem ili referentnim rješenjem.
:::
::::

### 13 · Gubitci, cjevovodi, crpke i mreže {#pogreske-cjevovodi .unnumbered .unlisted}

<span class="mf1-signal-chip">Re / λ / ξ</span> <span class="mf1-signal-chip">$H_p(Q)$</span> <span class="mf1-signal-chip">NPSH</span>

:::: {.mf1-error-pair}
::: {.mf1-error-column}
**Česta pogreška**

Zadržavanje istog faktora trenja pri promjeni protoka bez provjere; prigušivanje već otpornijeg ogranka radi jednakih protoka; miješanje razina snage; primjena istog $NPSH_R$ pri različitim brzinama vrtnje.
:::

::: {.mf1-error-column}
**Što provjeriti**

Zatvori kontinuitet i gubitke grana. Pri traženju radne točke ponovno računaj $Re$ i $\lambda$ te provjeri reziduale. Odvoji električnu, vratilnu i hidrauličku snagu; godišnju energiju računaj iz električne. Za usis trebaju $NPSH_R$ pri odgovarajućem protoku i brzini, kriterij margine i dopušteno radno područje.
:::
::::

### 14 · Turbostrojevi i propulzija {#pogreske-turbostrojevi .unnumbered .unlisted}

<span class="mf1-signal-chip">c / w / u</span> <span class="mf1-signal-chip">$M / P / F_p$</span>

:::: {.mf1-error-pair}
::: {.mf1-error-column}
**Česta pogreška**

Zamjena relativnog dotoka jedne lopatice punim protokom kola; prihvaćanje rekonstruiranog izlaza bez provjere gubitka; isti radijus u oba člana momenta; izostavljen ulazni tok količine gibanja vodomlaznog pogona; poistovjećivanje učinkovitosti pogona i propulzijske učinkovitosti.
:::

::: {.mf1-error-column}
**Što provjeriti**

Odaberi kontrolni volumen i tijelo na koje sila djeluje. Provjeri $\vec c=\vec u+\vec w$, pasivnost lopatice i bilancu energije. Za cijeli rotor koristi oba radijusa i provjeri $M\omega$ Eulerovim radom. U bilanci potiska zadrži ulazni tok količine gibanja; odvoji $TU$, snagu fluida i električnu snagu. Za platformu navedi sile dovoda i granice ulaza; statički kriterij nije certificirana nosivost.
:::
::::

### 15 · Otvoreni tokovi {#pogreske-otvoreni-tokovi .unnumbered .unlisted}

<span class="mf1-signal-chip">$Fr / D_h$</span> <span class="mf1-signal-chip">E / M</span> <span class="mf1-signal-chip">n</span>

:::: {.mf1-error-pair}
::: {.mf1-error-column}
**Česta pogreška**

Zamjena $D_h$ s $R_h$; izostavljanje povišenja dna ili proizvoljan izbor korijena energije; uporaba Bernoullija bez gubitaka kroz skok; neovisno tretiranje istog izmjerenog protoka u oba presjeka; poistovjećivanje kapaciteta kanala sa stvarnim dotokom bazenu.
:::

::: {.mf1-error-column}
**Što provjeriti**

Razdvoji $A$, širinu slobodne površine i omočen opseg. Na pragu provjeri raspoloživu energiju, kritičnu granicu i nastavak uzvodne grane. Skok opiši bilancom količine gibanja uz hidrostatičke sile; nesigurnost propagiraj iz zajedničkog $Q/b$. Kriterij $n+2u_n$ nije zajamčeni interval. Provjeri slobodni rub, ulazno stanje bazena, nizvodni vodostaj i kalibraciju hrapavosti.
:::
::::

## Kako koristiti pregled {#namjena-tablice}

Pregled koristi u tri faze rješavanja:

1. prije postavljanja početne jednadžbe, radi odabira odgovarajućeg modela;
2. tijekom računa, kada broj ili predznak odstupaju od očekivanoga reda veličine;
3. pri tumačenju rezultata, kao provjera fizikalnog smisla i granica modela.

Nesklad s ovim kriterijima upućuje na potrebu ponovnoga razmatranja skice, geometrije, referentnih veličina i pretpostavki prije nastavka algebarskog postupka.

## Kriteriji provjere rješenja

::: {.mf1-decision-grid}
::: {.mf1-decision-step}
<span class="mf1-step-index">1</span>

<p class="mf1-box-label">Model i pretpostavke</p>

Hidrostatika nije Bernoulli, a cjevovod nije samo jedan Darcy–Weisbachov zapis bez geometrije i režima strujanja.
:::

::: {.mf1-decision-step}
<span class="mf1-step-index">2</span>

<p class="mf1-box-label">Zadane veličine</p>

Velik broj pogrešaka nastaje jer se miješaju tlak i sila, maseni i volumenski protok ili apsolutni i manometarski tlak.
:::

::: {.mf1-decision-step}
<span class="mf1-step-index">3</span>

<p class="mf1-box-label">Smjer i geometrija</p>

Provjeri predznake, projekcije, vektorske komponente, istisnuti volumen i položaje referentnih točaka.
:::

::: {.mf1-decision-step}
<span class="mf1-step-index">4</span>

<p class="mf1-box-label">Fizikalni smisao rezultata</p>

Ako broj nema fizikalni smisao, uredna algebra ne spašava pogrešan model.
:::
:::

::: {.mf1-warning}
<p class="mf1-box-label">Najčešća pogreška</p>

Najčešća završna pogreška nastaje kada se račun prihvati samo zato što je algebra uredna. Broj bez fizikalnog smisla obično pokazuje da su model, geometrija ili referentni tlak pogrešno postavljeni prije završnog retka.
:::

::: {.mf1-mini-summary}
<p class="mf1-box-label">Operativna namjena dodatka</p>

<span class="mf1-ch-ref"><span class="mf1-ch-code">dod. C</span><span class="mf1-ch-title">Tipične pogreške po poglavljima</span></span> služi završnoj provjeri rezultata. Služi za brzo prepoznavanje tipičnih pogrešaka modela, predznaka, geometrije i jedinica prije nego što pogreška postane „uredno” rješenje.
:::




