## Tipične pogreške i preventivni filtar prije računa

Ovdje možeš provjeriti odabir modela, referentnog tlaka, kontrolnog volumena i predznaka. Vrati se odgovarajućem poglavlju ovog pregleda prije računa, kad dobiješ neočekivan rezultat i prije predaje zadatka. Natuknice opisuju opće pogreške; oznaka u zagradi (npr. Z6) upućuje na zadatak u pripadnom poglavlju u kojem se pogreška najčešće pojavi.

## Globalna provjera prije računa

::: {.mf1-checklist}
<p class="mf1-box-label">Brza provjera</p>

- Odaberi model: hidrostatiku, relativno mirovanje, kontinuitet, energijsku bilancu ili bilancu količine gibanja.
- Provjeri pretpostavke i granice primjene modela.
- Nacrtaj skicu, strujnicu ili kontrolni volumen prije prve jednadžbe.
- Uskladi jedinice prije uvrštavanja: Pa i kPa, W i kW, m i mm, L/s i m³/s.
- Provjeri predznak, jedinicu i red veličine rezultata.
- Kad su zadani intervali ili nesigurnosti, razlikuj zajamčene granice (provjera svih rubnih kombinacija) od standardnih nesigurnosti (korijen zbroja kvadrata, RSS); preklapanje intervala nije dokaz male pogreške.
:::

<p class="mf1-signal-note">Vizualni tragovi za brzo listanje dodatka: <span class="mf1-signal-chip">ρ / γ / p</span> osnovne veličine, <span class="mf1-signal-chip">μ / ν / σ</span> svojstva fluida, <span class="mf1-signal-chip">F / M</span> sile i momenti, <span class="mf1-signal-chip">Q / ṁ / h<sub>w</sub></span> protoci i gubitci.</p>

## Pregled po poglavljima {#tablica-tipičnih-pogrešaka-po-poglavljima}

### 1 · Osnove fluida i Pascalov zakon {#pogreske-tlak .unnumbered .unlisted}

<span class="mf1-signal-chip">ρ / γ / p</span> <span class="mf1-signal-chip">F / A</span>

:::: {.mf1-error-pair}
::: {.mf1-error-column}
**Česta pogreška**

Miješanje mase fluida i posude (tara), gustoće $\rho$ i specifične težine $\gamma$; zamjena omjera površina omjerom promjera (sila raste s $d^2$); očekivanje da preša istodobno povećava silu i pomak; zanemarivanje stlačivosti samo zato što je promjena gustoće mala (Z4); tumačenje zbroja poteza crpke kao jednog hoda ili zbroja iznosa sila kao rezultantnog vektora (Z5).
:::

::: {.mf1-error-column}
**Što provjeriti**

Oduzmi taru, provjeri površine, volumen i rad: $F_1s_1=F_2s_2$. Za pogrešku pomaka usporedi volumen stlačivanja $V_0\Delta p/K$ s istisnutim volumenom. Razlikuj puni i djelomični zadnji potez. Izbor ručne crpke mora zadovoljiti i silu i zbroj hodova; provjeri krajeve zadanih intervala. Pascalov kvazistatički model ne znači trenutačno širenje tlaka.
:::
::::

### 2 · Reologija, viskoznost i međupovršinske pojave {#pogreske-viskoznost .unnumbered .unlisted}

<span class="mf1-signal-chip">μ / ν / σ</span> <span class="mf1-signal-chip">$\cos\theta$</span>

:::: {.mf1-error-pair}
::: {.mf1-error-column}
**Česta pogreška**

Miješanje dinamičke i kinematičke viskoznosti i njihovih jedinica; isti tlačni skok za kapljicu ($4\sigma/d$) i sapunasti mjehur ($8\sigma/d$); spajanje dvaju procjepa u jedan gradijent (Z3); zaključak o newtonskom ponašanju iz jedne mjerne točke (Z5); istodobno računanje konkavnoga meniskusa i izlazne kapljice kao neovisnih međupovršina (Z6); faktor 4 iz kapilare promjera $d$ primijenjen na procjep širine $b$, gdje vrijedi $h=2\sigma\cos\theta/(\rho gb)$.
:::

::: {.mf1-error-column}
**Što provjeriti**

Utvrdi odgovaraju li pojavi $\mu$, $\nu$ ili $\sigma$. Prebroji međupovršine; na objema stranama pokretne ploče odredi smjer otpora i zbroji iznose sila. Newtonski model provjeri na svim mjernim točkama pri istoj temperaturi: omjer $\tau/(dv/dy)$ mora biti stalan. Odvoji stanje punjenja kapilare od stanja s formiranom kapljicom i ograniči zaključak na zadani statički model.
:::
::::

### 3 · Hidrostatička raspodjela tlaka i manometrija {#pogreske-hidrostatika .unnumbered .unlisted}

<span class="mf1-signal-chip">$p_{aps}$</span> <span class="mf1-signal-chip">$p_M$</span> <span class="mf1-signal-chip">$p_v$</span>

:::: {.mf1-error-pair}
::: {.mf1-error-column}
**Česta pogreška**

Miješanje apsolutnog, manometarskog i vakuumskog tlaka; pogrešni predznaci pri hodanju po stupcima i izostavljen spojni stupac (Z3); jedna gustoća za dva sloja (Z4); izbor manometra samo prema visini stupca bez tlačne pogreške očitanja (Z5); uporaba statičke usisne visine $p_{atm}/(\rho g)$ kao provjere crpke u radu; usporedba manometarskog tlaka s tlakom pare $p_v$, koji je apsolutan; računanje vodenog taloga u teretnom tanku kao ulja (bez sondiranja) i izostavljanje pretlaka inertnog plina $p_{M,pl}$ pri preračunu tlačnog mjerača razine.
:::

::: {.mf1-error-column}
**Što provjeriti**

Odredi referencu i sve visinske razlike, uključujući položaj granice fluida u manometru; prema dolje tlak raste, prema gore pada. Za slojeve zatvori i ukupnu visinu i tlak. Pri izboru instrumenta provjeri visinu stupca, tlačnu pogrešku $\rho g\,\delta h$ i rezervu skale. Za teretni tank zapiši $p_{M,dno}=p_{M,pl}+\rho_ogh_o+\rho_{mv}gh_w$ i debljinu vode uzmi iz sondiranja. Za usis crpke u radu trebaju gubitci, brzinska visina i usporedba $NPSH_a$ s proizvođačevim $NPSH_r$, oboje s apsolutnim tlakom.
:::
::::

### 4 · Relativno mirovanje fluida {#pogreske-relativno-mirovanje .unnumbered .unlisted}

<span class="mf1-signal-chip">a / g</span> <span class="mf1-signal-chip">$\vec g_{eff}$</span>

:::: {.mf1-error-pair}
::: {.mf1-error-column}
**Česta pogreška**

Zamjena smjera ubrzanja smjerom brzine (pri kočenju je $a<0$ iako je brzina pozitivna); linearna umjesto kvadratne ovisnosti o polumjeru pri vrtnji; zaključak o smirivanju fluida iz jednog očitanja (Z5); nastavak formule za puni paraboloid nakon prelijevanja ili ogoljavanja dna (Z6); prividna sila u zavoju usmjerena prema središtu zavoja umjesto od njega, pa viša razina na pogrešnom boku tanka.
:::

::: {.mf1-error-column}
**Što provjeriti**

Najprije odredi $\vec g_{eff}$ i provjeri očuvanje volumena. Pri vrtnji usporedi oba kritična praga (rub i dno); nakon prvoga mijenja se domena ili volumen. Iz podataka odvojeno provjeri blizinu referentnim razinama i promjenu kroz vrijeme. Provjera dubine u ustaljenom stanju sa zatvorenim usisom nije provjera rada s protokom.
:::
::::

### 5 · Hidrostatičke sile na plohe {#pogreske-sile-na-plohe .unnumbered .unlisted}

<span class="mf1-signal-chip">$F / h_{CP}$</span> <span class="mf1-signal-chip">$F_H / F_V$</span>

:::: {.mf1-error-pair}
::: {.mf1-error-column}
**Česta pogreška**

Stavljanje hvatišta u težište plohe: kad tlak raste s dubinom, centar tlaka leži ispod težišta, $h_{CP}=h_C+I_G/(h_CA)$; uporaba te formule bez provjere referentnog tlaka (dodatni pretlak traži momentiranje cijele raspodjele); tretiranje zakrivljene plohe kao ravne; određivanje predznaka $F_V$ samo iz pomoćnoga volumena; zbrajanje suprotnih tlakova bez predznaka (Z3); zamjena težišta i $I_G$ trokuta vrijednostima za pravokutnik (Z4); poistovjećivanje osi u središtu kružnice sa zglobom na kraju luka (Z5); pretpostavka da rezultanta na bilo kojoj zakrivljenoj plohi prolazi kroz jednu točku, što vrijedi samo za kružni luk; za nagnutu plohu $\sin\theta$ umjesto $\sin^2\theta$ u dubini centra tlaka.
:::

::: {.mf1-error-column}
**Što provjeriti**

Zadaj orijentaciju plohe i referentni tlak, zasebno zatvori silu i moment te za zakrivljenu plohu nacrtaj lokalnu normalu od stvarnoga fluida prema stijenci. Projekcija daje $F_H$, pomoćni volumen iznos $\lvert F_V\rvert$, a geometrija stvarnoga fluida njegov smjer. Za dvije razine vode oduzmi sile i njihove momente oko iste točke. Za radijalni poklopac sve tlačne normale prolaze kroz središte kružnice; moment težine i kapacitet spojnice provjeravaju se zasebno.
:::
::::

### 6 · Uzgon, plivanje i početni stabilitet {#pogreske-uzgon .unnumbered .unlisted}

<span class="mf1-signal-chip">$F_U$</span> <span class="mf1-signal-chip">$V_{ist}$</span> <span class="mf1-signal-chip">GM / GZ</span>

:::: {.mf1-error-pair}
::: {.mf1-error-column}
**Česta pogreška**

Zamjena volumena tijela istisninom; miješanje ravnoteže sila s početnim stabilitetom; proglašavanje pozitivnoga $GM$ dokazom stabiliteta pri velikim kutovima ili u oštećenom stanju; zanemarivanje slobodne površine djelomično punih tankova, koja smanjuje efektivni $GM$ za $\rho_ti_t/(\rho V_{ist})$; zaključivanje samo iz sniženja $KG$ bez promjene $KB$, $BM$ i nadvođa (Z5); morski balast računan gustoćom slatke vode ($1000$ umjesto $1025\ \text{kg/m}^3$); poprečni pomak centra uzgona $y_B$ proglašen polugom stabiliteta $GZ$; $\sin\varphi_{lim}=2f/b$ umjesto $\tan\varphi_{lim}=2f/b$ za kut uronjenja ruba palube; fiksiranje mase neovisno o nesigurnim gazovima (Z6).
:::

::: {.mf1-error-column}
**Što provjeriti**

Računaj stvarnu istisninu i odvoji bilancu sila od momenata. Pri pokusu nagibanja uteg ulazi u ukupnu masu istisnine. Za dodani balast ponovno računaj gaz, $KB$, $BM$ i nadvođe. Za svaki djelomično puni tank dodaj korekciju slobodne površine. $GM$ vrijedi za početni mali nagib; konačni i oštećeni stabilitet traže krivulju $GZ$, otvore, naplavljivanje i mjerodavne kriterije.
:::
::::

### 7 · Kinematika, kontrolni volumen i kontinuitet {#pogreske-kontinuitet .unnumbered .unlisted}

<span class="mf1-signal-chip">$\vec v\!\cdot\!\vec n$</span> <span class="mf1-signal-chip">$\vec v-\vec v_{KP}$</span>

:::: {.mf1-error-pair}
::: {.mf1-error-column}
**Česta pogreška**

Mehaničko pisanje $A_1v_1=A_2v_2$ bez kontrolnog volumena; zamjena kuta prema normali kutom prema plohi (Z2); zaboravljena akumulacija; uporaba apsolutne brzine kroz gibajuću plohu (Z5); pretpostavka jednakih brzina u granama samo zbog promjera (Z4); nastavak računa porasta razine nakon prelijevanja (Z6).
:::

::: {.mf1-error-column}
**Što provjeriti**

Označi vanjsku normalu, ulaze, izlaze i akumulaciju. Za kosu plohu koristi normalnu komponentu $v\cos\theta$; za gibajući klip tok računaj relativno prema otvoru i zasebno zatvori promjenu volumena komore. Omjer brzina u granama dolazi iz otpora grana ili zadanog režima, ne iz samih promjera. Nakon dosezanja ruba dodaj preljevni izlaz.
:::
::::

### 8 · Energijska jednadžba i Bernoulli {#pogreske-energija .unnumbered .unlisted}

<span class="mf1-signal-chip">$p/(\rho g)$</span> <span class="mf1-signal-chip">$\alpha v^2/(2g)$</span> <span class="mf1-signal-chip">z</span>

:::: {.mf1-error-pair}
::: {.mf1-error-column}
**Česta pogreška**

Pisanje Bernoullija bez odabira presjeka i strujnice; poistovjećivanje brzine mirne površine s izlaznim mlazom; uporaba $\alpha=1$ bez provjere profila (za laminarni tok $\alpha=2$); miješanje tlačne visine $p/(\rho g)$ s piezometarskom visinom $z+p/(\rho g)$ (Z3); zanemarivanje hidrostatičke korekcije senzora smještenog na drugoj visini (Z4); provjera samo jednog od dvaju pogonskih zahtjeva pri izboru elementa (Z5); primjena idealnog modela na sifon bez gubitaka i bez provjere najnižeg apsolutnog tlaka u tjemenu (Z6).
:::

::: {.mf1-error-column}
**Što provjeriti**

Odvoji brzinu na površini od izlazne brzine; piezometarsku crtu računaj kao $z+p/(\rho g)$, a energijsku dodavanjem $\alpha v^2/(2g)$. Očitanje senzora prenesi hidrostatički na visinu mjerne točke. Provjeri obje nejednakosti i rubne kombinacije zadanih intervala. U sifonu apsolutni tlak u tjemenu mora ostati iznad $p_v$.
:::
::::

### 9 · Kompresibilni idealni tok {#pogreske-kompresibilni-tok .unnumbered .unlisted}

<span class="mf1-signal-chip">$a / (v\pm a)$</span> <span class="mf1-signal-chip">$Ma / p_0$</span>

:::: {.mf1-error-pair}
::: {.mf1-error-column}
**Česta pogreška**

Miješanje brzine zvuka $a$ i brzine signala prema laboratoriju $v\pm a$ (Z3); omjeri manometarskih umjesto apsolutnih tlakova; poistovjećivanje protutlaka $p_b$ s izlaznim tlakom zagušene sapnice (Z4); brkanje zagušenja (choking, $Ma=1$ u najužem presjeku) s prigušenjem ventilom; izentropska relacija kroz udarni val ili nekorigirana nadzvučna Pitotova sonda (Z6); temperatura u °C u $a=\sqrt{\kappa RT}$; kriterij zagušenja $p_b/p_0<0{,}528$ s manometarskim tlakovima; izbor podzvučnog ili nadzvučnog korijena $A/A^*$ bez provjere protutlaka.
:::

::: {.mf1-error-column}
**Što provjeriti**

Razlikuj $a$ i $v\pm a$, koristi apsolutne tlakove i apsolutnu temperaturu te odaberi režim iz rubnih uvjeta: ako je $p_b/p_0$ ispod kritičnog omjera, izlaz ima $Ma=1$ i $p_e=p^*>p_b$. Kroz normalni udarni val očuvaj masu, količinu gibanja i ukupnu entalpiju, uz pad zaustavnog tlaka. Zaustavni tlak $p_{01}$ mjeri se u mirnoj komori uz izentropski dovod, a $p_{02}$ podzvučnom sondom iza vala.
:::
::::

### 10 · Količina i moment količine gibanja {#pogreske-kolicina-gibanja .unnumbered .unlisted}

<span class="mf1-signal-chip">$F / R / M$</span> <span class="mf1-signal-chip">$\beta$</span>

:::: {.mf1-error-pair}
::: {.mf1-error-column}
**Česta pogreška**

Zamjena sile na fluid silom na konstrukciju i reakcijom oslonca (predznak sile na koljeno); tlačne sile $p_MA$ s pogrešnim smjerom (moraju biti usmjerene u kontrolni volumen) ili s apsolutnim umjesto manometarskim tlakom kad je okolina atmosferska (Z3); uporaba $\beta=1$ za nejednolik profil; neoznačena ravnina skretanja; kosi razmak umjesto okomitog kraka u momentu (Z4); sav protok sapnice u bilanci jedne pomične ploče (Z5); apsolutna umjesto relativne brzine u dotoku kroz pomičnu plohu, ili relativna umjesto apsolutne brzine u toku količine gibanja i energije; RSS nad zajamčenim granicama (Z6).
:::

::: {.mf1-error-column}
**Što provjeriti**

Označi tlocrt i osi te tlačne sile usmjeri prema KV-u. Razlikuj $\vec F$ (fluid na konstrukciju) i $\vec R=-\vec F$ (oslonac na konstrukciju); moment računaj iz $\vec r\times\vec F$, a dotok kroz pomičnu plohu iz $v-u$ uz apsolutne brzine u bilancama količine gibanja i energije. Tlačne i impulsne doprinose zapiši po komponentama.
:::
::::

### 11 · Dimenzijska analiza i sličnost {#pogreske-slicnost .unnumbered .unlisted}

<span class="mf1-signal-chip">Re / Fr / Ma</span> <span class="mf1-signal-chip">Π</span>

:::: {.mf1-error-pair}
::: {.mf1-error-column}
**Česta pogreška**

Pretlak umjesto apsolutnog tlaka u kavitacijskom broju (Z3); prijenos sile faktorom $\lambda_L^3$ bez Froudeove sličnosti ili uz različite gustoće (Z4, Z6); zahtjev da model istodobno zadovolji $Re$ i $Fr$ istim fluidom pri drugom mjerilu, što nije moguće; brojčana vrijednost $St$ izvedena samo iz dimenzijske analize (Z5); izmjereni otpor modela broda pomnožen s $\lambda_L^3$ umjesto prijenosa preko $C_T=C_F+C_R$; promjer umjesto hidrauličkog promjera $D_h=4A/P$ kao karakteristična duljina nekružnog presjeka; miješanje koeficijenta otpora $C_D$ i koeficijenta istjecanja $C_d$; preklapanje intervala kao dokaz male mjerilne pogreške.
:::

::: {.mf1-error-column}
**Što provjeriti**

Provjeri apsolutni referentni tlak, rang dimenzijske matrice i relevantne grupe. Silu prenesi iz jednakosti bezdimenzijskog koeficijenta, s gustoćom, kvadratom brzine i površinom. Odaberi dominantni broj ($Fr$ za slobodnu površinu, $Re$ za viskozni otpor) i drugi korigiraj (Froudeova hipoteza $C_T=C_F+C_R$, stimulator turbulencije). Odvoji granice mjerenja od pogreške modela.
:::
::::

### 12 · Diferencijalni opis realnog toka {#pogreske-realni-tok .unnumbered .unlisted}

<span class="mf1-signal-chip">$D\vec v/Dt$</span> <span class="mf1-signal-chip">NS</span> <span class="mf1-signal-chip">V&amp;V</span>

:::: {.mf1-error-pair}
::: {.mf1-error-column}
**Česta pogreška**

Gubitak nestacionarnoga ili konvektivnoga člana (Z1); miješanje strujnice i putanje čestice; rješavanje Navier–Stokesovih jednadžbi bez početnih i rubnih uvjeta; tumačenje vremenskog mjerila $H^2/\nu$ kao točnog vremena uspostave profila (Z2); tumačenje lokalnog povratnog toka kao prolaza kroz stijenku (Z4); primjena Blasiusova rješenja uz gradijent tlaka ili hrapavost (Z5); poistovjećivanje numeričke konvergencije s validacijom (Z6); ulazna specifična disipacija $\omega$ proglašena „izmjerenom” iako senzor daje samo intenzitet $I_t$, a duljinska skala $\ell$ je pretpostavka.
:::

::: {.mf1-error-column}
**Što provjeriti**

Zadrži lokalno i konvektivno ubrzanje dok pretpostavke ne uklone članove, zadaj materijalni model i rubne uvjete (prianjanje: $v=0$ na stijenci) te odvojeno provjeri jednadžbe, diskretizaciju, očuvanje i usporedbu s mjerenjem ili referentnim rješenjem. Provjeri uvjete korelacije prije uvrštavanja.
:::
::::

### 13 · Gubitci, cjevovodi, crpke i mreže {#pogreske-cjevovodi .unnumbered .unlisted}

<span class="mf1-signal-chip">Re / λ / ξ</span> <span class="mf1-signal-chip">$H_p(Q)$</span> <span class="mf1-signal-chip">NPSH</span>

:::: {.mf1-error-pair}
::: {.mf1-error-column}
**Česta pogreška**

Uporaba $\lambda=64/Re$ bez provjere da je tok laminaran, ili turbulentne korelacije pri $Re<2300$ (Z2); zadržavanje istog $\lambda$ pri promjeni protoka (Z4) ili isti $\lambda$ za sve ponuđene promjere, iako se mijenjaju $Re$ i $k_s/D$; zbrajanje koeficijenata $\xi$ definiranih uz različite referentne brzine (proširenje, grananje) kao da vrijede za istu brzinu; prigušivanje već otpornijeg ogranka radi jednakih protoka (Z3); miješanje razina snage $P_h$, $P_{vr}$, $P_{el}$ i jedinica (kW i W; $h_w$ u m i $\Delta p$ u Pa); manometarski tlak u $NPSH_a$; primjena istog $NPSH_r$ pri različitim brzinama vrtnje (Z6).
:::

::: {.mf1-error-column}
**Što provjeriti**

Najprije $Re$ i režim, zatim $\lambda$; zatvori kontinuitet i gubitke grana. Pri traženju radne točke ponovno računaj $Re$ i $\lambda$ te provjeri reziduale. Svaki $\xi$ veži uz svoju referentnu brzinu. Odvoji hidrauličku, vratilnu i električnu snagu; godišnju energiju računaj iz električne. Za usis trebaju $NPSH_a$ s apsolutnim tlakom, $NPSH_r$ pri odgovarajućem protoku i brzini, kriterij margine i dopušteno radno područje.
:::
::::

### 14 · Turbostrojevi i propulzija {#pogreske-turbostrojevi .unnumbered .unlisted}

<span class="mf1-signal-chip">c / w / u</span> <span class="mf1-signal-chip">$M / P / F_T$</span>

:::: {.mf1-error-pair}
::: {.mf1-error-column}
**Česta pogreška**

Zamjena relativnog dotoka jedne lopatice punim protokom kola; prihvaćanje rekonstruiranog izlaza bez provjere gubitka i pasivnosti lopatice (Z3); isti radijus u oba člana Eulerove jednadžbe (Z4); izostavljen ulazni tok količine gibanja $\dot mv_A$ u bilanci potiska (Z5); poistovjećivanje učinkovitosti pogona i propulzijske učinkovitosti; kut lopatice $\beta_2$ zamijenjen korekcijskim faktorom $\beta$; snaga Peltonova kola s protokom jedne lopatice $\rho A(c_1-u)$ umjesto cijelog sapničkog protoka $\rho Ac_1$; relativna umjesto apsolutne brzine u energijskoj ili momentnoj provjeri rotora.
:::

::: {.mf1-error-column}
**Što provjeriti**

Odaberi kontrolni volumen i tijelo na koje sila djeluje. Provjeri $\vec c=\vec u+\vec w$, pasivnost lopatice i bilancu energije. Za cijeli rotor koristi oba radijusa i provjeri $M\omega$ Eulerovim radom. U bilanci potiska zadrži ulazni tok količine gibanja; odvoji $F_Tv_A$, snagu fluida i električnu snagu. Statički kriterij nije certificirana nosivost.
:::
::::

### 15 · Otvoreni tokovi {#pogreske-otvoreni-tokovi .unnumbered .unlisted}

<span class="mf1-signal-chip">$Fr / y_h$</span> <span class="mf1-signal-chip">E / I</span> <span class="mf1-signal-chip">n</span>

:::: {.mf1-error-pair}
::: {.mf1-error-column}
**Česta pogreška**

Zamjena hidrauličke dubine $y_h=A/T$ hidrauličkim radijusom $R_h=A/P$ ili hidrauličkim promjerom $D_h=4A/P$ u $Fr$ kanala (Z3); izostavljanje povišenja dna ili proizvoljan izbor korijena energije (Z4); uporaba Bernoullija bez gubitaka kroz skok (Z5); $\alpha=1$ i $\beta=1$ bez navođenja pretpostavke; neovisno tretiranje istog izmjerenog protoka u oba presjeka; poistovjećivanje kapaciteta kanala sa stvarnim dotokom bazenu (Z6).
:::

::: {.mf1-error-column}
**Što provjeriti**

Razdvoji $A$, širinu slobodne površine $T$ i omočeni opseg $P$. Na pragu provjeri raspoloživu energiju, kritičnu granicu i nastavak uzvodne grane. Skok opiši bilancom količine gibanja (impulsnom funkcijom) uz hidrostatičke sile; nesigurnost propagiraj iz zajedničkog $q=Q/b$. Provjeri nadvišenje, ulazno stanje bazena, nizvodni vodostaj i kalibraciju hrapavosti.
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
