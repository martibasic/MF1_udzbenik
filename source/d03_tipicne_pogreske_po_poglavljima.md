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
| <span class="mf1-ch-ref"><span class="mf1-ch-code">pog. 1</span><span class="mf1-ch-title">Osnove fluida i Pascalov zakon</span></span> | <span class="mf1-signal-chip">ρ / γ / p</span> <span class="mf1-signal-chip">F / A</span> | Miješanje mase ulja i posude, gustoće i specifične težine; zamjena omjera površina omjerom promjera; porast sile i pomaka istodobno; zanemarivanje stlačivosti samo zato što je promjena gustoće mala; tumačenje zbroja poteza kao jednog hoda ili zbroja iznosa sila kao rezultantnog vektora. | Oduzmi taru, provjeri površine, volumen i rad. Za pogrešku pomaka usporedi volumen stlačivanja s istisnutim volumenom pumpe. Razlikuj puni i djelomični zadnji potez. Izbor pumpe mora zadovoljiti silu i zbroj tlačnih hodova; provjeri krajeve zadanih intervala. Pascalov kvazistatički model ne znači trenutačno širenje tlaka. |
| <span class="mf1-ch-ref"><span class="mf1-ch-code">pog. 2</span><span class="mf1-ch-title">Reologija, viskoznost i međupovršinske pojave</span></span> | <span class="mf1-signal-chip">μ / ν / σ</span> <span class="mf1-signal-chip">\cos\theta</span> | Miješanje dinamičke i kinematičke viskoznosti i njihovih jedinica; isti tlačni skok za kapljicu i sapunasti mjehur; spajanje dvaju procjepa u jedan; zaključak o stalnoj viskoznosti iz jedne mjerne točke; istodobno računanje konkavnoga meniskusa i izlazne kapljice kao neovisnih međupovršina. | Utvrditi odgovaraju li pojavi $\mu$, $\nu$ ili $\sigma$. Prebrojiti međupovršine, na objema stranama pokretne ploče odrediti smjer otpora i zbrojiti sile. Newtonski model provjeriti na svim mjernim točkama pri istoj temperaturi. Odvojiti punjenje igle od stanja s kapljicom, provjeriti granice promjera i ograničiti izbor regulatora na zadani statički model. |
| <span class="mf1-ch-ref"><span class="mf1-ch-code">pog. 3</span><span class="mf1-ch-title">Hidrostatička raspodjela tlaka i manometrija</span></span> | <span class="mf1-signal-chip">p_{aps}</span> <span class="mf1-signal-chip">p_M</span> <span class="mf1-signal-chip">p_v</span> | Miješanje apsolutnog, manometarskog i vakuumskog tlaka; pogrešni predznaci i izostavljen spojni stupac; jedna gustoća za dva sloja; izbor manometra samo prema visini; uporaba statičke usisne visine kao provjere pumpe u radu. | Odrediti referencu i sve visinske razlike, uključujući položaj granice u manometru. Za slojeve zatvoriti i ukupnu visinu i tlak. Pri izboru instrumenta provjeriti visinu stupca, tlačnu pogrešku i rezervu skale; razlikovati zajamčene granice od standardne nesigurnosti. Za usis pumpe u radu trebaju gubici i brzinska visina te usporedba $NPSH_A$ s proizvođačevim $NPSH_R$, a ne samo $p_{atm}/(\rho g)$. |
| <span class="mf1-ch-ref"><span class="mf1-ch-code">pog. 4</span><span class="mf1-ch-title">Relativno mirovanje fluida</span></span> | <span class="mf1-signal-chip">a / g</span> <span class="mf1-signal-chip">g_{eff}</span> | Zamjena smjera ubrzanja smjerom brzine; linearna umjesto kvadratne ovisnosti o polumjeru; zaključak o smirivanju iz jednog očitanja; nastavak formule za puni paraboloid nakon prelijevanja ili ogoljavanja. | Najprije odrediti $\vec g_{eff}$ i provjeriti volumen. Pri vrtnji usporediti oba kritična praga; nakon prvoga mijenja se domena ili volumen. Iz podataka odvojeno provjeriti blizinu referentnim razinama i promjenu kroz vrijeme. Uključiti granično odstupanje brzine; provjera dubine u ustaljenom stanju sa zatvorenim usisom nije provjera rada s protokom. |
| <span class="mf1-ch-ref"><span class="mf1-ch-code">pog. 5</span><span class="mf1-ch-title">Hidrostatske sile na plohe</span></span> | <span class="mf1-signal-chip">F / y_{CP}</span> <span class="mf1-signal-chip">F_H / F_V</span> | Uporaba formule centra tlaka bez provjere referentnog tlaka; tretiranje zakrivljene plohe kao ravne; određivanje predznaka $F_V$ samo iz pomoćnoga volumena; zbrajanje suprotnih tlakova bez predznaka; zamjena težišta trokuta težištem pravokutnika; poistovjećivanje osi u središtu kružnice sa zglobom na kraju luka. | Potrebno je zadati orijentaciju plohe i referentni tlak, zasebno zatvoriti silu i moment te za zakrivljenu plohu nacrtati lokalnu normalu od stvarnoga fluida prema stijenci. Projekcija daje $F_H$, pomoćni volumen iznos $|F_V|$, a geometrija stvarnoga fluida njegov smjer. Za dvije razine vode oduzeti sile i njihove momente oko iste točke. Za radijalni poklopac sve normale prolaze kroz središte kružnice; moment težine i kapacitet spojnice provjeravaju se zasebno. |
| <span class="mf1-ch-ref"><span class="mf1-ch-code">pog. 6</span><span class="mf1-ch-title">Uzgon, plivanje i početni stabilitet</span></span> | <span class="mf1-signal-chip">F_U</span> <span class="mf1-signal-chip">V_{ist}</span> <span class="mf1-signal-chip">GM / GZ</span> | Zamjena volumena tijela istisninom; miješanje ravnoteže s početnom stabilnošću; proglašavanje pozitivnoga $GM$ dokazom konačne ili oštećene stabilnosti; zaključivanje samo iz sniženja $KG$; fiksiranje mase neovisno o nesigurnim uronima. | Potrebno je računati stvarnu istisninu i odvojiti bilancu sila od momenata. Pri pokusu nagibanja uteg ulazi u ukupnu masu. Za dodani balast ponovno računati gaz, $KB$, $BM$ i slobodni bok. U intervalnoj procjeni masa i moment moraju odgovarati istom skupu ulaza. $GM$ vrijedi za početni mali nagib; konačni i oštećeni slučaj traže krivulju $GZ$, otvore, naplavljivanje i mjerodavne kriterije. |
| <span class="mf1-ch-ref"><span class="mf1-ch-code">pog. 7</span><span class="mf1-ch-title">Kinematika, kontrolni volumen i kontinuitet</span></span> | <span class="mf1-signal-chip">$\vec v\!\cdot\!\vec n$</span> <span class="mf1-signal-chip">$\vec v-\vec v_{KP}$</span> | Mehaničko pisanje $A_1v_1=A_2v_2$ bez kontrolnog volumena; zamjena kuta prema normali kutom prema plohi; zaboravljena akumulacija; uporaba apsolutne brzine kroz gibajuću plohu; nastavak računa porasta razine nakon prelijevanja. | Označiti vanjsku normalu, ulaze, izlaze i akumulaciju. Za kosu plohu koristiti normalnu komponentu; za gibajući klip tok računati relativno prema otvoru i zasebno zatvoriti promjenu volumena komore. Zadani omjer brzina u granama nije posljedica samih promjera. Razlikovati zajamčene intervale od standardne nesigurnosti; nakon dosezanja ruba dodati preljevni izlaz. |
| <span class="mf1-ch-ref"><span class="mf1-ch-code">pog. 8</span><span class="mf1-ch-title">Energijska jednadžba i Bernoulli</span></span> | <span class="mf1-signal-chip">p/(\rho g)</span> <span class="mf1-signal-chip">v^2/(2g)</span> <span class="mf1-signal-chip">z</span> | Pisanje Bernoullija bez odabira presjeka; poistovjećivanje mirne površine s izlaznim mlazom; miješanje tlačne visine i HGL-a; zanemarivanje hidrostatičke korekcije senzora ili jednog od pogonskih zahtjeva. | Potrebno je odvojiti brzinu na površini od izlazne brzine, računati HGL kao z+p/(ρg), očitanje senzora prenijeti na visinu mjerne točke te provjeriti obje nejednakosti i krajnje kombinacije zadanih intervala. |
| <span class="mf1-ch-ref"><span class="mf1-ch-code">pog. 9</span><span class="mf1-ch-title">Kompresibilni idealni tok</span></span> | Miješanje brzine zvuka i brzine signala prema laboratoriju; omjeri manometarskih tlakova; poistovjećivanje protutlaka s izlaznim tlakom prigušene sapnice; izentropska relacija kroz udar ili nekorigirana nadzvučna Pitotova sonda. | Razlikovati a i v±a, koristiti apsolutne tlakove i temperaturu te odabrati režim iz rubnih uvjeta. Kroz normalni val očuvati masu, količinu gibanja i ukupnu entalpiju, uz pad ukupnog tlaka. Za Z6 mjeriti p01 u mirnoj komori uz izentropski dovod, a p02 podzvučnom sondom; usporediti omjere uz kombiniranu standardnu nesigurnost. | Potrebno je koristiti apsolutni tlak i temperaturu, provjeriti je li tok prigušen, odabrati podzvučnu ili nadzvučnu granu iz rubnih uvjeta te preko udara primijeniti očuvanje mase, količine gibanja i ukupne energije, ali ne entropije. |
| <span class="mf1-ch-ref"><span class="mf1-ch-code">pog. 10</span><span class="mf1-ch-title">Količina i moment količine gibanja</span></span> | Zamjena sile na fluid silom na konstrukciju; neoznačena ravnina skretanja; kosi razmak umjesto okomitog kraka; sav protok sapnice u bilanci jedne pomične ploče; RSS nad zajamčenim granicama. | Označiti tlocrt i osi te tlakove usmjeriti prema KV-u. Razlikovati F i R, moment računati iz r×F, a pomični dotok iz v−u uz apsolutne brzine u impulsu i energiji. Provjeriti granice maksimuma i puni zadani kriterij nosača. | Potrebno je nacrtati kontrolni volumen i osi, zapisati tlakne i impulsne doprinose po komponentama, odrediti sustav na koji djeluje sila te reakciju dobiti promjenom predznaka. |
| <span class="mf1-ch-ref"><span class="mf1-ch-code">pog. 11</span><span class="mf1-ch-title">Dimenzijska analiza i sličnost</span></span> | <span class="mf1-signal-chip">Re / Fr / Ma</span> <span class="mf1-signal-chip">Π</span> | Pretlak u kavitacijskom broju; prijenos sile s λ³ bez Froudeove sličnosti; brojčani St izveden samo iz dimenzija; preklapanje intervala kao dokaz male mjerilne pogreške. | Provjeri apsolutni referentni tlak, rang matrice i relevantne grupe. Silu prenesi iz jednakosti koeficijenta, provjeri ostvarivost sličnosti te odvoji granice mjerenja od pogreške modela. |
| <span class="mf1-ch-ref"><span class="mf1-ch-code">pog. 12</span><span class="mf1-ch-title">Diferencijalni opis realnog toka</span></span> | <span class="mf1-signal-chip">$D\vec v/Dt$</span> <span class="mf1-signal-chip">NS</span> <span class="mf1-signal-chip">V&amp;V</span> | Gubitak nestacionarnoga člana; miješanje strujnice i putanje čestice; rješavanje Navier–Stokesa bez početnih i rubnih uvjeta; poistovjećivanje numeričke konvergencije s validacijom; tumačenje vremenskog mjerila kao točnog vremena uspostave profila ili lokalnog povrata kao prolaza kroz stijenku. | Potrebno je zadržati lokalno i konvektivno ubrzanje dok pretpostavke ne uklone članove, zadati materijalni model i rubne uvjete te odvojeno provjeriti jednadžbe, diskretizaciju, očuvanje i usporedbu s mjerenjem ili referentnim rješenjem. |
| <span class="mf1-ch-ref"><span class="mf1-ch-code">pog. 13</span><span class="mf1-ch-title">Gubitci, cjevovodi, crpke i mreže</span></span> | <span class="mf1-signal-chip">Re / λ / ξ</span> <span class="mf1-signal-chip">H_p(Q)</span> <span class="mf1-signal-chip">NPSH</span> | Zadržavanje istog faktora trenja pri promjeni protoka bez provjere; prigušivanje već otpornijeg ogranka radi jednakih protoka; miješanje razina snage; primjena istog $NPSH_R$ pri različitim brzinama vrtnje. | Zatvori kontinuitet i gubitke grana. Pri traženju radne točke ponovno računaj $Re$ i $\lambda$ te provjeri reziduale. Odvoji električnu, vratilnu i hidrauličku snagu; godišnju energiju računaj iz električne. Za usis trebaju $NPSH_R$ pri odgovarajućem protoku i brzini, kriterij margine i dopušteno radno područje. |
| <span class="mf1-ch-ref"><span class="mf1-ch-code">pog. 14</span><span class="mf1-ch-title">Turbostrojevi i propulzija</span></span> | <span class="mf1-signal-chip">c / w / u</span> <span class="mf1-signal-chip">M / P / F_p</span> | Zamjena relativnog dotoka jedne lopatice punim protokom kola; prihvaćanje rekonstruiranog izlaza bez provjere gubitka; isti radijus u oba člana momenta; izostavljen ulazni impuls vodomlaznog pogona; poistovjećivanje učinkovitosti pogona i propulzijske učinkovitosti. | Odaberi kontrolni volumen i tijelo na koje sila djeluje. Provjeri $\vec c=\vec u+\vec w$, pasivnost lopatice i bilancu energije. Za cijeli rotor koristi oba radijusa i provjeri $M\omega$ Eulerovim radom. U potisku zadrži ulazni impuls; odvoji $TU$, snagu fluida i električnu snagu. Za platformu navedi sile dovoda i granice ulaza; statički kriterij nije certificirana nosivost. |
| <span class="mf1-ch-ref"><span class="mf1-ch-code">pog. 15</span><span class="mf1-ch-title">Otvoreni tokovi</span></span> | <span class="mf1-signal-chip">Fr / D_h</span> <span class="mf1-signal-chip">E / M</span> <span class="mf1-signal-chip">n</span> | Zamjena $D_h$ s $R_h$; izostavljanje povišenja dna ili proizvoljan izbor korijena energije; uporaba Bernoullija bez gubitaka kroz skok; neovisno tretiranje istog izmjerenog protoka u oba presjeka; poistovjećivanje kapaciteta kanala sa stvarnim dotokom bazenu. | Razdvoji $A$, slobodnu širinu i omočen opseg. Na pragu provjeri raspoloživu energiju, kritičnu granicu i nastavak uzvodne grane. Skok zatvori količinom gibanja uz hidrostatičke sile; nesigurnost propagiraj iz zajedničkog $Q/b$. Kriterij $n+2u_n$ nije zajamčeni interval. Provjeri slobodni rub, ulazno stanje bazena, nizvodni vodostaj i kalibraciju hrapavosti. |

## Namjena tablice

Tablica služi provjeri modela, računa i tumačenja rezultata u tri faze rješavanja:

1. prije postavljanja početne jednadžbe, radi odabira odgovarajućeg modela;
2. tijekom računa, kada broj ili predznak odstupaju od očekivanoga reda veličine;
3. pri tumačenju rezultata, kao provjera fizikalnog smisla i granica modela.

Nesklad s ovim kriterijima upućuje na potrebu ponovnoga razmatranja skice, geometrije, referentnih veličina i pretpostavki prije nastavka algebarskog postupka.

## Kriteriji provjere rješenja

::: {.mf1-decision-grid}
::: {.mf1-decision-step}
<span class="mf1-step-index">1</span>

<p class="mf1-box-label">Model i pretpostavke</p>

Hidrostatika nije Bernoulli, a cjevovod nije samo jedan Darcy-Weisbachov zapis bez geometrije i režima strujanja.
:::

::: {.mf1-decision-step}
<span class="mf1-step-index">2</span>

<p class="mf1-box-label">Zadane veličine</p>

Velik broj pogrešaka nastaje jer se miješaju tlak i sila, maseni i volumenski protok ili apsolutni i manometarski tlak.
:::

::: {.mf1-decision-step}
<span class="mf1-step-index">3</span>

<p class="mf1-box-label">Smjer i geometrija</p>

Predznači, projekcije, vektorske komponente, istisnuti volumen i odabir točaka često odlučuju više od same numerike.
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

<span class="mf1-ch-ref"><span class="mf1-ch-code">dod. C</span><span class="mf1-ch-title">Tipične pogreške po poglavljima</span></span> je završni filtar prije povjerenja rezultatu. Služi za brzo prepoznavanje tipičnih kvarova modela, predznaka, geometrije i jedinica prije nego što pogreška postane "uredno" rješenje.
:::




