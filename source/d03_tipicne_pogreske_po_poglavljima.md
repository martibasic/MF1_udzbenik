## Tipične pogreške i preventivni filtar prije računa

Ovaj dodatak nije pasivni prilog, nego radni sloj za provjeru modela prije računa, tijekom računa i prije predaje zadatka. Većina pogrešaka u zadacima mehanike fluida ne nastaje u zadnjem retku algebre, nego mnogo ranije: pri izboru modela, referentne točke, kontrolnog volumena, predznaka ili tipa protoka.

## Globalna provjera prije računa

::: {.mf1-checklist}
<p class="mf1-box-label">Brza provjera</p>

- Potrebno je odrediti model problema: hidrostatika, relativno mirovanje, kontinuitet, Bernoulli, količina gibanja ili cjevovod.
- Potrebno je provjeriti vrijede li pretpostavke modela ili je granica njihove primjene već prijeđena.
- Potrebno je nacrtati skicu, strujnicu ili kontrolni volumen prije prve jednadžbe.
- Potrebno je potvrditi da su jedinice konzistentne i u istom sustavu.
- Potrebno je provjeriti ima li rezultat fizikalnog smisla i razumnog reda veličine.
:::

<p class="mf1-signal-note">Vizualni tragovi za brzo listanje dodatka: <span class="mf1-signal-chip">ρ / γ / p</span> osnovne veličine, <span class="mf1-signal-chip">μ / ν / σ</span> svojstva fluida, <span class="mf1-signal-chip">F / M</span> sile i momenti, <span class="mf1-signal-chip">Q / ṁ / h_w</span> protoci i gubici.</p>

## Tablica tipičnih pogrešaka po poglavljima

| Poglavlje | Signal | Tipičan lom modela | Što provjeriti prije računa |
| --- | --- | --- | --- |
| <span class="mf1-ch-ref"><span class="mf1-ch-code">pog. 1</span><span class="mf1-ch-title">Osnove fluida i Pascalov zakon</span></span> | <span class="mf1-signal-chip">ρ / γ / p</span> <span class="mf1-signal-chip">F / A</span> | Miješanje gustoće, specifične težine i tlaka; zamjena istoga tlaka istom silom na oba klipa; tretiranje kvazistatičkoga Pascalova modela kao trenutačne propagacije ili stvaranja rada niotkuda. | Potrebno je jasno odvojiti $\rho$, $\gamma$ i $p$, razlikovati isti tlak od iste sile, provjeriti visinske razlike i gubitke te zapamtiti da stvarni tlačni poremećaj putuje konačnom brzinom. |
| <span class="mf1-ch-ref"><span class="mf1-ch-code">pog. 2</span><span class="mf1-ch-title">Reologija, viskoznost i međupovršinske pojave</span></span> | <span class="mf1-signal-chip">μ / ν / σ</span> <span class="mf1-signal-chip">\cos\theta</span> | Miješanje dinamičke i kinematičke viskoznosti; zaboravljena pretvorba $\text{mm}^2/\text{s}$ u $\text{m}^2/\text{s}$; korištenje pogrešnoga mehanizma za kapilarnost ili smičanje. | Potrebno je utvrditi govori li zadatak o unutarnjem trenju, površinskoj napetosti ili kontaktnom kutu te treba li koristiti $\mu$, $\nu$ ili njihov odnos s gustoćom. |
| <span class="mf1-ch-ref"><span class="mf1-ch-code">pog. 3</span><span class="mf1-ch-title">Hidrostatička raspodjela tlaka i manometrija</span></span> | <span class="mf1-signal-chip">p_{aps}</span> <span class="mf1-signal-chip">p_M</span> <span class="mf1-signal-chip">p_v</span> | Miješanje apsolutnog, manometarskog i vakuumskog tlaka; nekonzistentni predznaci; uporaba statičke usisne visine kao provjere pumpe u radu. | Potrebno je odrediti referentni tlak i smjer promjene s visinom. Za usis pumpe u radu trebaju gubici i brzinska visina te usporedba $NPSH_A$ s proizvođačevim $NPSH_R$, a ne samo $p_{atm}/(\rho g)$. |
| <span class="mf1-ch-ref"><span class="mf1-ch-code">pog. 4</span><span class="mf1-ch-title">Relativno mirovanje fluida</span></span> | <span class="mf1-signal-chip">a / g</span> <span class="mf1-signal-chip">g_{eff}</span> | Primjena obične hidrostatike bez efektivnog ubrzanja; pogrešan smjer nagiba; nastavak formule za puni paraboloid nakon prelijevanja ili ogoljavanja. | Potrebno je prvo odrediti $\vec g_{eff}$, zatim usporediti oba kritična praga. Nakon prvoga prelijevanja ili ogoljavanja mijenja se domena ili volumen, pa treba postaviti novu geometrijsku bilancu. |
| <span class="mf1-ch-ref"><span class="mf1-ch-code">pog. 5</span><span class="mf1-ch-title">Hidrostatske sile na plohe</span></span> | <span class="mf1-signal-chip">F / y_{CP}</span> <span class="mf1-signal-chip">F_H / F_V</span> | Uporaba formule centra tlaka bez provjere referentnog tlaka; tretiranje zakrivljene plohe kao ravne; određivanje predznaka $F_V$ samo iz pomoćnoga volumena. | Potrebno je zadati orijentaciju plohe i referentni tlak, zasebno zatvoriti silu i moment te za zakrivljenu plohu nacrtati lokalnu normalu od stvarnoga fluida prema stijenci. Projekcija daje $F_H$, pomoćni volumen iznos $|F_V|$, a geometrija stvarnoga fluida njegov smjer. |
| <span class="mf1-ch-ref"><span class="mf1-ch-code">pog. 6</span><span class="mf1-ch-title">Uzgon, plivanje i početni stabilitet</span></span> | <span class="mf1-signal-chip">F_U</span> <span class="mf1-signal-chip">V_{ist}</span> <span class="mf1-signal-chip">GM / GZ</span> | Zamjena volumena tijela istisninom; miješanje ravnoteže s početnom stabilnošću; proglašavanje pozitivnoga $GM$ dokazom konačne ili oštećene stabilnosti. | Potrebno je računati stvarnu istisninu, odvojiti bilancu sila od momenata i koristiti $GM$ samo za početni mali nagib. Konačni i oštećeni slučaj traže krivulju $GZ$, otvore, naplavljivanje i mjerodavne kriterije. |
| <span class="mf1-ch-ref"><span class="mf1-ch-code">pog. 7</span><span class="mf1-ch-title">Kinematika, kontrolni volumen i kontinuitet</span></span> | <span class="mf1-signal-chip">$\vec v\!\cdot\!\vec n$</span> <span class="mf1-signal-chip">$\vec v-\vec v_{KP}$</span> | Mehaničko pisanje $A_1v_1=A_2v_2$ bez kontrolnog volumena; zaboravljena akumulacija; uporaba apsolutne umjesto relativne brzine kroz gibajuću kontrolnu plohu. | Potrebno je označiti vanjsku normalu, ulaze i izlaze, odlučiti radi li se s $Q$ ili $\dot m$ te za gibajuću plohu računati tok preko $(\vec v-\vec v_{KP})\cdot\vec n$. |
| <span class="mf1-ch-ref"><span class="mf1-ch-code">pog. 8</span><span class="mf1-ch-title">Energijska jednadžba i Bernoulli</span></span> | <span class="mf1-signal-chip">p/(\rho g)</span> <span class="mf1-signal-chip">v^2/(2g)</span> <span class="mf1-signal-chip">z</span> | Pisanje Bernoullija bez provjere strujnice i stacionarnosti; miješanje apsolutnoga, manometarskoga, statičkoga i stagnacijskoga tlaka; prikriveno zanemarivanje gubitaka. | Potrebno je odabrati sustav i dvije točke, navesti referencu tlaka, odlučiti je li potreban nestacionarni ili rotirajući oblik te prije zaključka o kavitaciji usporediti apsolutni tlak s tlakom pare. |
| <span class="mf1-ch-ref"><span class="mf1-ch-code">pog. 9</span><span class="mf1-ch-title">Kompresibilni idealni tok</span></span> | <span class="mf1-signal-chip">Ma</span> <span class="mf1-signal-chip">p_0 / T_0</span> <span class="mf1-signal-chip">A/A^*</span> | Miješanje statičkih i zaustavnih veličina; izbor pogrešne grane relacije površina–Mach; primjena izentropskih relacija kroz udarni val. | Potrebno je koristiti apsolutni tlak i temperaturu, provjeriti je li tok prigušen, odabrati podzvučnu ili nadzvučnu granu iz rubnih uvjeta te preko udara primijeniti očuvanje mase, količine gibanja i ukupne energije, ali ne entropije. |
| <span class="mf1-ch-ref"><span class="mf1-ch-code">pog. 10</span><span class="mf1-ch-title">Količina i moment količine gibanja</span></span> | <span class="mf1-signal-chip">$\sum\vec F$</span> <span class="mf1-signal-chip">$\dot m\vec v$</span> | Korištenje samo iznosa brzine; zaboravljene tlačne sile; zamjena sile na fluid silom fluida na konstrukciju ili pogrešan predznak momenta. | Potrebno je nacrtati kontrolni volumen i osi, zapisati tlakne i impulsne doprinose po komponentama, odrediti sustav na koji djeluje sila te reakciju dobiti promjenom predznaka. |
| <span class="mf1-ch-ref"><span class="mf1-ch-code">pog. 11</span><span class="mf1-ch-title">Dimenzijska analiza i sličnost</span></span> | <span class="mf1-signal-chip">Re / Fr / Ma</span> <span class="mf1-signal-chip">Π</span> | Proglašavanje svakoga broja omjerom sila; pokušaj istodobnog očuvanja Reynoldsove i Froudeove sličnosti; prikaz orijentacijskog praga kao univerzalne granice. | Potrebno je iz jednadžbi i rubnih uvjeta odrediti relevantne grupe, njihove referentne veličine i ostvarivost sličnosti te navesti područje valjanosti svakoga empirijskog praga. |
| <span class="mf1-ch-ref"><span class="mf1-ch-code">pog. 12</span><span class="mf1-ch-title">Diferencijalni opis realnog toka</span></span> | <span class="mf1-signal-chip">$D\vec v/Dt$</span> <span class="mf1-signal-chip">NS</span> <span class="mf1-signal-chip">V&amp;V</span> | Gubitak nestacionarnoga člana; miješanje strujnice i putanje čestice; rješavanje Navier–Stokesa bez početnih i rubnih uvjeta; poistovjećivanje numeričke konvergencije s validacijom. | Potrebno je zadržati lokalno i konvektivno ubrzanje dok pretpostavke ne uklone članove, zadati materijalni model i rubne uvjete te odvojeno provjeriti jednadžbe, diskretizaciju, očuvanje i usporedbu s mjerenjem ili referentnim rješenjem. |
| <span class="mf1-ch-ref"><span class="mf1-ch-code">pog. 13</span><span class="mf1-ch-title">Gubitci, cjevovodi, crpke i mreže</span></span> | <span class="mf1-signal-chip">Re / λ / ξ</span> <span class="mf1-signal-chip">H_p(Q)</span> <span class="mf1-signal-chip">NPSH</span> | Računanje gubitaka prije režima; primjena afinitetnih zakona bez nove radne točke sustava; miješanje električne, vratilne i hidrauličke snage; zamjena $NPSH_A$ i $NPSH_R$. | Potrebno je zatvoriti kontinuitet mreže, odrediti $Re$ i faktor trenja, presjeći krivulje crpke i sustava te voditi zaseban energetski ledger električna → vratilna → hidraulička → korisna i disipirana snaga. |
| <span class="mf1-ch-ref"><span class="mf1-ch-code">pog. 14</span><span class="mf1-ch-title">Turbostrojevi i propulzija</span></span> | <span class="mf1-signal-chip">c / w / u</span> <span class="mf1-signal-chip">M / P / F_p</span> | Korištenje apsolutne brzine gdje treba relativna; zamjena relativnog dotoka jedne lopatice punim sapničkim protokom rotora; poistovjećivanje maksimuma sile s maksimumom snage ili idealnog potiska s certificiranom nosivošću. | Potrebno je jasno odabrati nepomični ili gibajući kontrolni volumen, razlikovati $\vec c$, $\vec w$ i $\vec u$, utvrditi obrađuje li se jedna lopatica ili cijelo kolo te odvojiti hidraulički izlaz od mehaničkih, električnih i konstrukcijskih provjera. |
| <span class="mf1-ch-ref"><span class="mf1-ch-code">pog. 15</span><span class="mf1-ch-title">Otvoreni tokovi</span></span> | <span class="mf1-signal-chip">Fr / D_h</span> <span class="mf1-signal-chip">E / M</span> <span class="mf1-signal-chip">n</span> | Zamjena hidrauličke dubine hidrauličkim promjerom; uporaba energijske bilance bez gubitaka kroz hidraulički skok; tretiranje Manningova $n$ kao svojstva fluida. | Potrebno je odrediti $A$, širinu slobodne površine i omočen opseg, razlikovati energijsku od količinske funkcije te Manningov koeficijent vezati uz izvor, stanje kanala i područje valjanosti. |

## Kako koristiti ovu tablicu bez lutanja

Najkorisnija je u tri trenutka:

1. prije početka zadatka, da potvrdiš da si u pravom modelu
2. usred računa, kad broj ili predznak počnu izgledati šumnjivo
3. na kraju, kao kratka samoprovjera prije zaključivanja rješenja

Ako se rezultat raspadne već na ovoj tablici, bolje je vratiti se na početnu skicu nego produžavati algebarski lanac.

## Brza završna provjera prije predaje rješenja

::: {.mf1-decision-grid}
::: {.mf1-decision-step}
<span class="mf1-step-index">1</span>

<p class="mf1-box-label">Provjeri model</p>

Hidrostatika nije Bernoulli, a cjevovod nije samo jedan Darcy-Weisbachov zapis bez geometrije i režima strujanja.
:::

::: {.mf1-decision-step}
<span class="mf1-step-index">2</span>

<p class="mf1-box-label">Provjeri što je zadano</p>

Velik broj pogrešaka nastaje jer se miješaju tlak i sila, maseni i volumenski protok ili apsolutni i manometarski tlak.
:::

::: {.mf1-decision-step}
<span class="mf1-step-index">3</span>

<p class="mf1-box-label">Provjeri smjer i geometriju</p>

Predznači, projekcije, vektorske komponente, istisnuti volumen i odabir točaka često odlučuju više od same numerike.
:::

::: {.mf1-decision-step}
<span class="mf1-step-index">4</span>

<p class="mf1-box-label">Tek onda vjeruj rezultatu</p>

Ako broj nema fizikalni smisao, uredna algebra ne spašava pogrešan model.
:::
:::

::: {.mf1-warning}
<p class="mf1-box-label">Najčešća pogreška</p>

Najčešća završna pogreška jest preskočiti samoprovjeru zato što račun "izgleda uredno". U MF1 uredan broj bez fizikalnog smisla obično znači da je model, geometrija ili referentni tlak bio krivo postavljen mnogo prije zadnjeg retka.
:::

::: {.mf1-mini-summary}
<p class="mf1-box-label">Operativna namjena dodatka</p>

<span class="mf1-ch-ref"><span class="mf1-ch-code">dod. C</span><span class="mf1-ch-title">Tipične pogreške po poglavljima</span></span> je završni filtar prije povjerenja rezultatu. Služi za brzo prepoznavanje tipičnih kvarova modela, predznaka, geometrije i jedinica prije nego što pogreška postane "uredno" rješenje.
:::




