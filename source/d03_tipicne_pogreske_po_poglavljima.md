Ovaj pregled služi za provjeru odabira modela, referentnog tlaka, kontrolnog volumena i predznaka. Vrati se odgovarajućem odjeljku prije računa, kad dobiješ neočekivan rezultat i prije predaje zadatka. Natuknice opisuju opće pogreške, a oznaka u zagradi (npr. Z6) upućuje na zadatak pripadnog poglavlja u kojem se pogreška najčešće pojavljuje.

## Globalna provjera prije računa

::: {.mf1-checklist}
<p class="mf1-box-label">Brza provjera</p>

- Odaberi model: hidrostatiku, relativno mirovanje, kontinuitet, energijsku bilancu ili bilancu količine gibanja.
- Provjeri pretpostavke i granice primjene modela.
- Nacrtaj skicu, strujnicu ili kontrolni volumen prije prve jednadžbe.
- Uskladi jedinice prije uvrštavanja: Pa i kPa, W i kW, m i mm, L/s i m³/s.
- Provjeri predznak, jedinicu i red veličine rezultata.
- Kad su zadani intervali ili nesigurnosti, razlikuj zajamčene granice (provjeravaju se sve rubne kombinacije) od standardnih nesigurnosti (korijen zbroja kvadrata, RSS); preklapanje intervala nije dokaz male pogreške.
:::

## Pregled po poglavljima {#tablica-tipičnih-pogrešaka-po-poglavljima}

### 1 · Osnove fluida i Pascalov zakon {#pogreske-tlak .unnumbered .unlisted}

:::: {.mf1-error-pair}
::: {.mf1-error-column}
**Česta pogreška**

Miješanje mase fluida s masom posude (tarom) te gustoće $\rho$ sa specifičnom težinom $\gamma$; zamjena omjera površina omjerom promjera (sila raste s $d^2$); očekivanje da preša istodobno povećava i silu i pomak; zanemarivanje stlačivosti samo zato što je promjena gustoće mala (Z4); tumačenje zbroja poteza crpke kao jednog hoda ili zbroja iznosa sila kao rezultantnog vektora (Z5).
:::

::: {.mf1-error-column}
**Što provjeriti**

Oduzmi taru, provjeri površine, volumen i rad: $F_1s_1=F_2s_2$. Za pogrešku pomaka usporedi volumen stlačivanja $V_0\Delta p/K$ s istisnutim volumenom. Razlikuj pune poteze od djelomičnoga zadnjeg poteza. Odabrana ručna crpka mora zadovoljiti i uvjet sile i uvjet zbroja hodova; provjeri krajeve zadanih intervala. Pascalov kvazistatički model ne znači trenutačno širenje tlaka.
:::
::::

### 2 · Viskoznost, površinska napetost i kapilarnost {#pogreske-viskoznost .unnumbered .unlisted}

:::: {.mf1-error-pair}
::: {.mf1-error-column}
**Česta pogreška**

Miješanje dinamičke i kinematičke viskoznosti i njihovih jedinica; pretpostavka jednakoga tlačnog skoka za kapljicu ($4\sigma/d$) i sapunasti mjehur ($8\sigma/d$); spajanje dvaju procjepa u jedan gradijent (Z3); zaključak o newtonskom ponašanju iz jedne mjerne točke (Z5); istodobno računanje konkavnoga meniskusa i izlazne kapljice kao neovisnih međupovršina (Z6); faktor 4 iz kapilare promjera $d$ primijenjen na procjep širine $b$, gdje vrijedi $h=2\sigma\cos\theta/(\rho gb)$.
:::

::: {.mf1-error-column}
**Što provjeriti**

Utvrdi koja od veličina $\mu$, $\nu$ i $\sigma$ odgovara pojavi. Prebroji međupovršine; na objema stranama pokretne ploče odredi smjer otpora i zbroji iznose sila. Newtonski model provjeri na svim mjernim točkama pri istoj temperaturi: omjer $\tau/(dv/dy)$ mora biti stalan. Odvoji stanje punjenja kapilare od stanja s oblikovanom kapljicom i ograniči zaključak na zadani statički model.
:::
::::

### 3 · Hidrostatička raspodjela tlaka i manometrija {#pogreske-hidrostatika .unnumbered .unlisted}

:::: {.mf1-error-pair}
::: {.mf1-error-column}
**Česta pogreška**

Miješanje apsolutnog, manometarskog i vakuumskog tlaka; pogrešni predznaci pri prijelazu sa stupca na stupac; model stalne gustoće za stupac zraka visok stotine metara (Z1); kod nagnutog manometra očitanje uzduž cjevčice bez $\sin\alpha$ ili bez spuštanja razine u posudi (Z3); jedna gustoća za dva sloja (Z4); izbor manometra samo prema visini stupca, bez procjene tlačne pogreške očitanja (Z5); uporaba statičke usisne visine $p_{atm}/(\rho g)$ kao provjere crpke u radu; usporedba manometarskog tlaka s tlakom pare $p_v$, koji je apsolutan; računanje vodenog taloga u teretnom tanku kao da je ulje (bez sondiranja) i izostavljanje pretlaka inertnog plina $p_{M,pl}$ pri preračunu očitanja tlačnog mjerača razine.
:::

::: {.mf1-error-column}
**Što provjeriti**

Odredi referencu i sve visinske razlike, uključujući položaj granice fluida u manometru; prema dolje tlak raste, prema gore pada. Kod slojevitog punjenja zatvori bilancu i ukupne visine i tlaka. Pri izboru instrumenta provjeri visinu stupca, tlačnu pogrešku $\rho g\,\delta h$ i rezervu skale; kod nagnute cjevčice okomitu visinu daje $L\sin\alpha$ uvećano za spuštanje razine u posudi. Za plin dulji od nekoliko desetaka metara gustoću ostavi pod integralom. Za teretni tank zapiši $p_{M,dno}=p_{M,pl}+\rho_ugh_u+\rho_{mv}gh_v$ a debljinu vodenog sloja uzmi iz sondiranja. Za usis crpke u radu potrebni su gubitci, brzinska visina i usporedba $NPSH_a$ s proizvođačevim $NPSH_r$, oboje na osnovi apsolutnog tlaka.
:::
::::

### 4 · Relativno mirovanje fluida {#pogreske-relativno-mirovanje .unnumbered .unlisted}

:::: {.mf1-error-pair}
::: {.mf1-error-column}
**Česta pogreška**

Zamjena smjera ubrzanja smjerom brzine (pri kočenju je $a<0$ iako je brzina pozitivna); linearna umjesto kvadratne ovisnosti o polumjeru pri vrtnji; zanemarivanje okomitog ubrzanja u nagibu i u efektivnoj težini, $\tan\theta=a_x/(g+a_z)$ (Z2); u potpuno punom zatvorenom spremniku razinu tlaka određuje položaj odzračnika, a ne gornji rub (P1); zaključak o smirivanju fluida iz jednog očitanja (Z5); daljnja primjena formule za puni paraboloid nakon prelijevanja ili ogoljenja dna (Z6); prividna sila u zavoju usmjerena prema središtu zavoja umjesto od njega, pa se viša razina pojavi na pogrešnom boku tanka.
:::

::: {.mf1-error-column}
**Što provjeriti**

Najprije odredi $\vec g_{eff}$ i provjeri očuvanje volumena. Pri vrtnji usporedi oba kritična praga (rub i dno); nakon dosezanja prvoga mijenja se domena ili volumen. Iz podataka odvojeno provjeri koliko su očitanja blizu referentnih razina i kako se mijenjaju u vremenu. Provjera dubine u ustaljenom stanju sa zatvorenim usisom nije provjera rada s protokom.
:::
::::

### 5 · Hidrostatičke sile na ravne i zakrivljene plohe {#pogreske-sile-na-plohe .unnumbered .unlisted}

:::: {.mf1-error-pair}
::: {.mf1-error-column}
**Česta pogreška**

Smještanje hvatišta u težište plohe: kad tlak raste s dubinom, centar tlaka leži ispod težišta, $h_{CP}=h_C+I_G/(h_CA)$; uporaba te formule bez provjere referentnog tlaka (dodatni pretlak zahtijeva računanje momenta cijele raspodjele); računanje zakrivljene plohe kao ravne; određivanje predznaka $F_V$ samo iz pomoćnoga volumena; uvjet otvaranja zaklopke postavljen s težištem umjesto s centrom tlaka (Z3); primjena $h_{CP}=h_C+I_G/(Ah_C)$ u zatvorenom spremniku s nadtlakom plina; zamjena težišta i $I_G$ trokuta vrijednostima za pravokutnik (Z4); poistovjećivanje osi u središtu kružnice sa zglobom na kraju luka (Z5); pretpostavka da rezultanta na bilo kojoj zakrivljenoj plohi prolazi kroz jednu točku, što vrijedi samo za kružni luk; $\sin\theta$ umjesto $\sin^2\theta$ u dubini centra tlaka nagnute plohe.
:::

::: {.mf1-error-column}
**Što provjeriti**

Utvrdi orijentaciju plohe i referentni tlak, zasebno zatvori bilancu sila i bilancu momenata te za zakrivljenu plohu nacrtaj lokalnu normalu od stvarnoga fluida prema stijenci. Projekcija daje $F_H$, pomoćni volumen iznos $\lvert F_V\rvert$, a geometrija stvarnoga fluida njegov smjer. Kod zaklopke koja se sama otvara uvjet je položaj centra tlaka u osi vrtnje; s nadtlakom plina sila i hvatište računaju se iz cijele raspodjele $p_{pl}+
ho gh$. Na radijalnom poklopcu sve tlačne normale prolaze kroz središte kružnice; moment težine i kapacitet spojnice provjeri zasebno.
:::
::::

### 6 · Uzgon, plivanje i početni stabilitet {#pogreske-uzgon .unnumbered .unlisted}

:::: {.mf1-error-pair}
::: {.mf1-error-column}
**Česta pogreška**

Zamjena volumena tijela istisninom; ista istisnina (umjesto iste mase) pri prelasku broda iz mora u rijeku (Z1); kod homogenog bloka zaključak o stabilitetu samo iz širine, bez usporedbe $KB+BM$ s $KG$ (Z2); miješanje ravnoteže sila s početnim stabilitetom; proglašavanje pozitivnoga $GM$ dokazom stabiliteta pri velikim kutovima ili u oštećenom stanju; zanemarivanje slobodne površine djelomično punih tankova, koja smanjuje efektivni $GM$ za $\rho_ti_t/(\rho V_{ist})$; zaključivanje samo iz sniženja $KG$, bez praćenja promjene $KB$, $BM$ i nadvođa (Z5); morski balast računan gustoćom slatke vode ($1000$ umjesto $1025\ \text{kg/m}^3$); poprečni pomak centra uzgona $y_B$ proglašen polugom stabiliteta $GZ$; $\sin\varphi_{lim}=2f/b$ umjesto $\tan\varphi_{lim}=2f/b$ za kut uronjenja ruba palube; masa uzeta kao nepromjenjiva neovisno o nesigurnim gazovima (Z6).
:::

::: {.mf1-error-column}
**Što provjeriti**

Računaj stvarnu istisninu i odvoji bilancu sila od bilance momenata. Pri pokusu nagibanja uteg ulazi u ukupnu masu istisnine. Nakon dodavanja balasta ponovno izračunaj gaz, $KB$, $BM$ i nadvođe. Za svaki djelomično puni tank dodaj korekciju slobodne površine. $GM$ vrijedi za mali početni nagib; za stabilitet pri velikim nagibima i u oštećenom stanju potrebni su krivulja $GZ$, podatci o otvorima i naplavljivanju te mjerodavni kriteriji.
:::
::::

### 7 · Kinematika, kontrolni volumen i kontinuitet {#pogreske-kontinuitet .unnumbered .unlisted}

:::: {.mf1-error-pair}
::: {.mf1-error-column}
**Česta pogreška**

Mehaničko pisanje $A_1v_1=A_2v_2$ bez kontrolnog volumena; zamjena kuta prema normali kutom prema plohi (Z2); zaboravljena akumulacija; uporaba apsolutne brzine kroz pomičnu plohu (Z5); vršna brzina u osi uzeta kao srednja ili profil integriran bez težine $2\pi r$ prstena (Z4); računanje porasta razine i nakon početka prelijevanja (Z6).
:::

::: {.mf1-error-column}
**Što provjeriti**

Označi vanjsku normalu, ulaze, izlaze i akumulaciju. Za kosu plohu koristi normalnu komponentu $v\cos\theta$; kod pomičnoga klipa protok kroz otvor računaj brzinom relativnom prema otvoru i zasebno zatvori bilancu promjene volumena komore. Za izmjereni profil protok je $\int v\,2\pi r\,dr$: vanjski prstenovi nose najveći opseg, pa ih ne smiješ izostaviti. Nakon dosezanja ruba dodaj preljevni izlaz.
:::
::::

### 8 · Energijska jednadžba i Bernoulli {#pogreske-energija .unnumbered .unlisted}

:::: {.mf1-error-pair}
::: {.mf1-error-column}
**Česta pogreška**

Pisanje Bernoullijeve jednadžbe bez odabira presjeka i strujnice; poistovjećivanje brzine mirne površine s brzinom izlaznog mlaza; vrijeme pražnjenja spremnika iz početnog protoka kao da je stalan, iako protok pada sa $\sqrt h$ (Z2); uporaba $\alpha=1$ bez provjere profila (za razvijeni laminarni tok u kružnoj cijevi $\alpha=2$); miješanje tlačne visine $p/(\rho g)$ s piezometarskom visinom $z+p/(\rho g)$ (Z3); zanemarivanje hidrostatičke korekcije senzora smještenog na drugoj visini (Z4); provjera samo jednog od dvaju pogonskih zahtjeva pri izboru elementa (Z5); primjena idealnog modela bez gubitaka na sifon, bez provjere najnižega apsolutnog tlaka u tjemenu (Z6).
:::

::: {.mf1-error-column}
**Što provjeriti**

Odvoji brzinu na površini od izlazne brzine; piezometarsku crtu računaj kao $z+p/(\rho g)$, a energijsku crtu dobij dodavanjem $\alpha v^2/(2g)$. Očitanje senzora prenesi hidrostatički na visinu mjerne točke. Provjeri obje nejednakosti i rubne kombinacije zadanih intervala. U sifonu apsolutni tlak u tjemenu mora ostati iznad $p_v$.
:::
::::

### 9 · Kompresibilni idealni tok {#pogreske-kompresibilni-tok .unnumbered .unlisted}

:::: {.mf1-error-pair}
::: {.mf1-error-column}
**Česta pogreška**

Miješanje brzine zvuka $a$ i brzine signala u odnosu na laboratorij $v\pm a$ (Z3); omjeri manometarskih umjesto apsolutnih tlakova; poistovjećivanje protutlaka $p_b$ s izlaznim tlakom zagušene sapnice (Z4); brkanje zagušenja (choking, $Ma=1$ u najužem presjeku) s prigušenjem ventilom; izentropska relacija primijenjena kroz udarni val ili nekorigirano očitanje Pitotove sonde u nadzvučnom toku (Z6); temperatura u °C uvrštena u $a=\sqrt{\kappa RT}$; kriterij zagušenja $p_b/p_0<0{,}528$ primijenjen s manometarskim tlakovima; izbor podzvučnog ili nadzvučnog korijena relacije $A/A^*$ bez provjere protutlaka.
:::

::: {.mf1-error-column}
**Što provjeriti**

Razlikuj $a$ i $v\pm a$, koristi apsolutne tlakove i apsolutnu temperaturu te režim odredi iz rubnih uvjeta: ako je $p_b/p_0$ ispod kritičnog omjera, na izlazu je $Ma=1$ i $p_e=p^*>p_b$. Pri prolasku kroz normalni udarni val očuvaj masu, količinu gibanja i ukupnu entalpiju; zaustavni tlak pritom pada. Zaustavni tlak $p_{01}$ mjeri se u mirnoj komori uz izentropski dovod, a $p_{02}$ podzvučnom sondom iza vala.
:::
::::

### 10 · Količina i moment količine gibanja {#pogreske-kolicina-gibanja .unnumbered .unlisted}

:::: {.mf1-error-pair}
::: {.mf1-error-column}
**Česta pogreška**

Miješanje sile na fluid, sile na konstrukciju i reakcije oslonca (predznak sile na koljeno); tlačne sile $p_MA$ s pogrešnim smjerom (moraju biti usmjerene u kontrolni volumen) ili s apsolutnim umjesto manometarskim tlakom kad je okolina atmosferska; u okomitoj ravnini zaboravljena težina vode u elementu i pad tlaka zbog visine (Z3); uporaba $\beta=1$ za nejednolik profil; neoznačena ravnina skretanja; kosi razmak umjesto okomitog kraka u momentu (Z4); cijeli protok sapnice uzet u bilancu jedne pomične ploče (Z5); apsolutna umjesto relativne brzine u dotoku kroz pomičnu plohu ili relativna umjesto apsolutne brzine u toku količine gibanja i energije; RSS primijenjen na zajamčene granice (Z6).
:::

::: {.mf1-error-column}
**Što provjeriti**

Nacrtaj tlocrt, označi osi i tlačne sile usmjeri prema KV-u. Razlikuj $\vec F$ (fluid na konstrukciju) i $\vec R=-\vec F$ (oslonac na konstrukciju). Moment računaj iz $\vec r\times\vec F$, a dotok kroz pomičnu plohu iz relativne brzine $v-u$; u bilancama količine gibanja i energije ostaju apsolutne brzine. Tlačne i impulsne doprinose zapiši po komponentama.
:::
::::

### 11 · Dimenzijska analiza i sličnost {#pogreske-slicnost .unnumbered .unlisted}

:::: {.mf1-error-pair}
::: {.mf1-error-column}
**Česta pogreška**

Empirijska jednadžba s dimenzijskim koeficijentom ($n$ u Manningovoj jednadžbi) uzeta kao homogena, pa se ista brojka uvrsti u drugim jedinicama (Z2); pretlak umjesto apsolutnog tlaka u kavitacijskom broju (Z3); prijenos sile faktorom $\lambda_L^3$ bez Froudeove sličnosti ili uz različite gustoće (Z4, Z6); zahtjev da model s istim fluidom pri drugom mjerilu istodobno zadovolji $Re$ i $Fr$, što nije moguće; brojčana vrijednost $St$ izvedena samo iz dimenzijske analize (Z5); izmjereni otpor modela broda pomnožen s $\lambda_L^3$ umjesto prijenosa preko $C_T=C_F+C_R$; promjer umjesto hidrauličkog promjera $D_h=4A/P$ kao karakteristična duljina nekružnog presjeka; miješanje koeficijenta otpora $C_D$ i koeficijenta istjecanja $C_d$; preklapanje intervala uzeto kao dokaz male mjerilne pogreške.
:::

::: {.mf1-error-column}
**Što provjeriti**

Najprije provjeri dimenzijsku homogenost i jedinicu svakog empirijskog koeficijenta, zatim apsolutni referentni tlak, rang dimenzijske matrice i mjerodavne grupe. Silu prenesi preko jednakosti bezdimenzijskog koeficijenta, uzimajući u obzir gustoću, kvadrat brzine i površinu. Odaberi dominantni broj ($Fr$ za slobodnu površinu, $Re$ za viskozni otpor), a utjecaj drugoga korigiraj (Froudeova hipoteza $C_T=C_F+C_R$, stimulator turbulencije). Odvoji granice mjerenja od pogreške modela.
:::
::::

### 12 · Diferencijalni opis realnog toka {#pogreske-realni-tok .unnumbered .unlisted}

:::: {.mf1-error-pair}
::: {.mf1-error-column}
**Česta pogreška**

Izostavljanje nestacionarnoga ili konvektivnoga člana (Z1); miješanje strujnice i putanje čestice; rješavanje Navier–Stokesovih jednadžbi bez početnih i rubnih uvjeta; tumačenje vremenskog mjerila $H^2/\nu$ kao točnog vremena uspostave profila; Hagen–Poiseuilleov izraz primijenjen na turbulentni tok ili bilanca sila $\tau_{st}=\Delta p\,D/(4L)$ pogrešno ograničena na laminarni režim, visina prve ćelije odabrana bez brzine trenja (Z2); tumačenje lokalnog povratnog toka kao prolaza kroz stijenku (Z4); primjena Blasiusova rješenja uz gradijent tlaka ili hrapavost (Z5); poistovjećivanje numeričke konvergencije s validacijom (Z6); ulazna specifična disipacija $\omega$ proglašena „izmjerenom” iako senzor daje samo intenzitet $I_t$, a duljinska skala $\ell$ samo je pretpostavka.
:::

::: {.mf1-error-column}
**Što provjeriti**

Zadrži lokalno i konvektivno ubrzanje dok ih pretpostavke izričito ne uklone te zadaj materijalni model i rubne uvjete (prianjanje: $v=0$ na stijenci). Zatim odvojeno provjeri jednadžbe, diskretizaciju, očuvanje i usporedbu s mjerenjem ili referentnim rješenjem. Prije uvrštavanja u korelaciju provjeri uvjete njezine primjene; visinu prve ćelije uskladi s $u_\tau$ i odabranim modelom stijenke.
:::
::::

### 13 · Gubitci, cjevovodi, crpke i mreže {#pogreske-cjevovodi .unnumbered .unlisted}

:::: {.mf1-error-pair}
::: {.mf1-error-column}
**Česta pogreška**

Uporaba $\lambda=64/Re$ bez provjere da je tok laminaran, ili turbulentne korelacije pri $Re<2300$ (Z2); zadržavanje istog $\lambda$ pri promjeni protoka (Z4) ili istog $\lambda$ za sve ponuđene promjere, iako se mijenjaju $Re$ i $k_s/D$; zbrajanje koeficijenata $\xi$ definiranih uz različite referentne brzine (proširenje, grananje) kao da vrijede za istu brzinu; prigušivanje već otpornijeg ogranka radi izjednačavanja protoka (Z3); miješanje razina snage $P_h$, $P_{vr}$, $P_{el}$ i jedinica (kW i W; $h_g$ u m i $\Delta p$ u Pa); manometarski tlak uvršten u $NPSH_a$; primjena istog $NPSH_r$ pri različitim brzinama vrtnje (Z6).
:::

::: {.mf1-error-column}
**Što provjeriti**

Najprije odredi $Re$ i režim, zatim $\lambda$; zatvori bilancu kontinuiteta i gubitaka po granama. Pri traženju radne točke ponovno računaj $Re$ i $\lambda$ te provjeri reziduale. Svaki $\xi$ veži uz svoju referentnu brzinu. Odvoji hidrauličku, vratilnu i električnu snagu; godišnju energiju računaj iz električne. Za provjeru usisa potrebni su $NPSH_a$ izračunan s apsolutnim tlakom, $NPSH_r$ pri odgovarajućem protoku i brzini vrtnje, kriterij rezerve i dopušteno radno područje.
:::
::::

### 14 · Turbostrojevi i propulzija {#pogreske-turbostrojevi .unnumbered .unlisted}

:::: {.mf1-error-pair}
::: {.mf1-error-column}
**Česta pogreška**

Zamjena relativnog dotoka na jednu lopaticu ili ploču punim protokom kola, pa pogrešan optimum $u=v/2$ umjesto $u=v/3$ za jednu ploču (Z2); prihvaćanje rekonstruiranog izlaza bez provjere gubitka i pasivnosti lopatice (Z3); isti polumjer u oba člana Eulerove jednadžbe (Z4); izostavljen ulazni tok količine gibanja $\dot mv_A$ u bilanci potiska (Z5); poistovjećivanje učinkovitosti pogona s propulzijskom učinkovitošću; kut lopatice $\beta_2$ zamijenjen korekcijskim faktorom $\beta$; snaga Peltonova kola računana s protokom jedne lopatice $\rho A(c_1-u)$ umjesto cijelog sapničkog protoka $\rho Ac_1$; relativna umjesto apsolutne brzine u energijskoj ili momentnoj provjeri rotora.
:::

::: {.mf1-error-column}
**Što provjeriti**

Odaberi kontrolni volumen i tijelo na koje sila djeluje. Provjeri $\vec c=\vec u+\vec w$, pasivnost lopatice i bilancu energije. Za cijeli rotor koristi oba polumjera, a umnožak $M\omega$ provjeri Eulerovim radom. U bilanci potiska zadrži ulazni tok količine gibanja; odvoji $F_Tv_A$, snagu fluida i električnu snagu. Statički kriterij nije isto što i certificirana nosivost.
:::
::::

### 15 · Otvoreni tokovi {#pogreske-otvoreni-tokovi .unnumbered .unlisted}

:::: {.mf1-error-pair}
::: {.mf1-error-column}
**Česta pogreška**

Zamjena hidrauličke dubine $y_h=A/T$ hidrauličkim radijusom $R_h=A/P$ ili hidrauličkim promjerom $D_h=4A/P$ u $Fr$ kanala (Z3); koeficijent kontrakcije $C_c$ (geometrija mlaza) poistovjećen s koeficijentom protoka $C_d$ ili zanemarena brzina dolaska uzvodno od ustave (Z2); izostavljanje povišenja dna ili proizvoljan izbor korijena energijske jednadžbe (Z4); primjena Bernoullijeve jednadžbe bez gubitaka kroz skok (Z5); $\alpha=1$ i $\beta=1$ bez navođenja te pretpostavke; tretiranje istog izmjerenog protoka u oba presjeka kao dviju neovisnih veličina; poistovjećivanje kapaciteta kanala sa stvarnim dotokom u bazen (Z6).
:::

::: {.mf1-error-column}
**Što provjeriti**

Razdvoji $A$, širinu slobodne površine $T$ i omočeni opseg $P$. Ispod ustave poveži uzvodni presjek i suženi mlaz energijom, pa tek onda očitaj $C_d$. Na pragu provjeri raspoloživu energiju, kritičnu granicu i nastavak uzvodne grane. Skok opiši bilancom količine gibanja (impulsnom funkcijom) uz hidrostatičke sile; nesigurnost propagiraj iz zajedničkog $q=Q/b$. Provjeri nadvišenje, ulazno stanje bazena, nizvodni vodostaj i kalibraciju hrapavosti.
:::
::::

## Kriteriji provjere rješenja

::: {.mf1-decision-grid}
::: {.mf1-decision-step}
<span class="mf1-step-index">1</span>

<p class="mf1-box-label">Model i pretpostavke</p>

Hidrostatika nije Bernoullijeva jednadžba, a cjevovod nije samo jedan Darcy–Weisbachov izraz bez geometrije i režima strujanja.
:::

::: {.mf1-decision-step}
<span class="mf1-step-index">2</span>

<p class="mf1-box-label">Zadane veličine</p>

Mnoge pogreške nastaju zato što se miješaju tlak i sila, maseni i volumenski protok ili apsolutni i manometarski tlak.
:::

::: {.mf1-decision-step}
<span class="mf1-step-index">3</span>

<p class="mf1-box-label">Smjer i geometrija</p>

Provjeri predznake, projekcije, vektorske komponente, istisnuti volumen i položaje referentnih točaka.
:::

::: {.mf1-decision-step}
<span class="mf1-step-index">4</span>

<p class="mf1-box-label">Fizikalni smisao rezultata</p>

Ako broj nema fizikalni smisao, uredna algebra ne spašava pogrešan model: vrati se skici, geometriji, referentnim veličinama i pretpostavkama.
:::
:::
