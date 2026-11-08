# Urednički i lektorski pregled — pog. 13 (Gubitci, cjevovodi, crpke i mreže)

Recenzent: neovisni urednik i lektor (agent bez konteksta pisanja), 8. 11. 2026.

**Materijal.** Izvor `source/u13_gubici_cjevovodi_crpke_i_mreze.md` (912 redaka), PDF
poglavlja (izvorne str. 245–262, pregledane str. 245, 247, 258 i 259 kao slika, ostalo
kao tekst), `docs/konvencije_pisanja.md`, odjeljci „Tekst”, „Notacija i nazivlje” i
„Odluke završne recenzije” iz `docs/urednicki_stil.md`. Radi provjere upućivanja
pretraženi su i `source/u07…`, `source/u08…`, `source/u12…` te bilježnica
`notebooks/u13_paralelne_grane.ipynb`.

**Izlaz alata.** `prirucnik_stats.py --nalazi` za ovo poglavlje ne javlja nijedan nalaz
(K1, K3, K4, K5, K7, K8, K12, K13), pa nema alatnih nalaza K7 za potvrdu ili odbacivanje.
Profil: 293 rečenice, prosjek 14,1 riječi, 2,0 % rečenica iznad 30 riječi, nijedna iznad 40
(alat razdvaja r. 115 i r. 301 drukčije od ručnog brojenja; r. 115 ima 40 riječi).
`--nacrt` je upotrijebljen za provjeru ponavljanja po odlomcima.

**Opseg.** Fiziku ne procjenjujem. Nalazi su autorska procjena urednika; nijedan nije
proveden u datotekama. Potvrđeni oblici (zadatci, podatci, gubitci, izračunan-,
oplakan-, crpka) nisu nalazi. Mjesta su u izvoru; `u13:N` znači
`source/u13_gubici_cjevovodi_crpke_i_mreze.md:N`.

## Tablica nalaza

| Mjesto | Pravilo | Sadašnji tekst | Prijedlog | Težina |
| --- | --- | --- | --- | --- |
| u13:1 | K3 | „Bernoullijeva jednadžba iz []{u08} zato se proširuje …, a lokalni opis viskoznog toka i Hagen–Poiseuilleov rezultat iz []{u12} sažimaju se …” — u PDF-u: „iz pog. 8 Energijska jednadžba i Bernoulli zato se proširuje”, „iz pog. 12 Diferencijalni opis realnog toka sažimaju se” | Uputu staviti u zagradu da umetnuti naslov ne prekida rečenicu: „Zato se Bernoullijeva jednadžba ([]{u08}) proširuje članovima crpke, turbine i gubitaka, a lokalni opis viskoznog toka i Hagen–Poiseuilleov rezultat ([]{u12}) sažimaju se u koeficijente gubitaka.” | P3 |
| u13:3 | K10 | Cijeli odlomak: $v=4Q/(\pi D^2)$, $Re$, $\lambda(Re,k_s/D)$, $h_g=(\lambda L/D+\sum\xi)v^2/(2g)$ …; „Uz stalan $\lambda$ linijski je gubitak razmjeran omjeru $Q^2/D^5$, pa je promjer najjača geometrijska poluga.” | Isti niz formula stoji u jedn. 13.7 i 13.9; posljednja rečenica doslovno se ponavlja u Sažetku (r. 899), a teza je i naslov 13.2.1 (r. 101). Prijedlog: odlomak zamijeniti jednom rečenicom „U svakoj dionici protok određuje brzinu i Reynoldsov broj, a oni koeficijent trenja i gubitak.” Uvjeti koji iz uvoda nestaju ostaju u poglavlju: ista referentna brzina (r. 89, 97), prijelazni režim (r. 194), $Q^2/D^5$ uz stalan $\lambda$ (r. 106–109, 899). | P2 |
| u13:5 | K10 (i K5) | „Mreža se razlaže na dionice. Kroz serijske dionice prolazi isti protok … $R_{eq}=R_1+R_2$ … $1/\sqrt{R_{eq}}=…$ Otpori i njihove jedinice moraju pripadati istom modelu.” | Isto odmah ponavlja r. 9 (isti $Q$ u seriji, $Q=Q_1+Q_2$, isti pad energije), zatim r. 221–242, 255 i 900. Uz to $R_i$, $h_i$ i $R_{eq}$ ovdje se rabe prije definicije (r. 226), a iznimka $R$ prema uredničkom stilu uvodi se uz definiciju pri prvom spomenu. Prijedlog: odlomak izbrisati; rečenicu „Otpori i njihove jedinice moraju pripadati istom modelu.” premjestiti na kraj r. 242. | P2 |
| u13:7 (i r. 29) | K5 | „te usisnu rezervu $NPSH_a$”; r. 29 „u računu NPSH-a” | Kratica se rabi prije punog naziva (r. 339). „… te raspoloživu neto pozitivnu usisnu visinu $NPSH_a$ (uvedenu u []{u08})”. | P3 |
| u13:7 | K10 | „Model je jednodimenzijski i stacionaran: vodeni udar, brze promjene ventila i izrazito stlačiv tok traže proširen model, …” | Isti popis stoji u Granici modela (r. 72, ondje „snažno stlačivi tok”) i Sažetku (r. 903). Prijedlog: „Model je jednodimenzijski i stacionaran, a njegove granice navodi odjeljak [-@sec-realna-energijska-bilanca]; strujanje kroz rotor crpke obrađuje se u []{u14}.” Popis ostaje u Granici modela. | P3 |
| u13:9 | K6 | „Kota $H$ povezuje slobodne površine spremnika i za prikazanu mrežu jest ukupna raspoloživa visina …: $H=h_{AC}+h_{CD}+h_{DB}$.” | $H$ je u jedn. 13.1 i r. 42 ukupna energijska visina, a ista razlika razina kasnije je $\Delta z$ (r. 286) i $H_{stat}$ (r. 292). Prijedlog: „Kota $\Delta z$ … $\Delta z=h_{AC}+h_{CD}+h_{DB}$” uz istu promjenu oznake na slici 13.1. | P2 |
| u13:11 | K13 | Potpis sl. 13.1: „Od pojedine dionice do serijsko-paralelne mreže: protok određuje brzinu i režim, a gubitci zatvaraju energijsku bilancu.” | Potpis je teza i ne kaže što slika pokazuje. „Serijsko-paralelna mreža između spremnika A i B: dovodna i odvodna dionica u seriji, dvije paralelne grane između čvorova C i D i energijska crta koja pada duž triju dionica.” | P3 |
| u13:13 | K10 | „U cjevovodnom sustavu kontinuitet povezuje … Radna točka nastaje ondje gdje crpka daje upravo onu energijsku visinu koju sustav zahtijeva pri tom protoku.” | Odlomak stoji između slike i retka „Procijenjeno vrijeme rada” i ponavlja definiciju radne točke iz r. 295–299. Prijedlog: izbrisati. | P3 |
| u13:29 | Pravopis i stil | „Svi članovi imaju jedinicu metra promatranog fluida.” | „Svi su članovi visine u metrima stupca promatranog fluida.” | P3 |
| u13:62, u13:162 | K7 | „ne uklanja potrebu za mrežnom konvergencijom”; „ili mreža nije dovoljno fina” | U poglavlju o cjevovodnim mrežama „mreža” bez dodatka zbunjuje; r. 278 sam razlikuje „CFD mreža ćelija” i „cjevovodna mreža”. „… za konvergencijom po mreži ćelija …”; „… ili mreža ćelija nije dovoljno fina”. | P2 |
| u13:62, u13:113 | K5 | „u RANS proračunu”; „RANS račun” | Kratica se u poglavlju javlja dvaput; definirana je u pog. 12. Prijedlog: „u RANS proračunu ([]{u12})” pri prvom spomenu ili puni naziv „Reynoldsovo osrednjen proračun”. | P3 |
| u13:65 (sl. 13.2) | K13 | Oznaka na skici „ventil (simbol)” ispod presjeka 2, daleko od znaka ventila | „(simbol)” je oznaka izrade. Na skici samo „ventil”, uz sam znak ventila. | P3 |
| u13:67 | K10 (i K1) | „Bez stroja vrijedi $H_1=H_2+h_g$: EGL pada zbog linijskih i lokalnih gubitaka, HGL prikazuje zbroj tlačne i geodetske visine, a uz $\alpha=1$ razmak je $EGL-HGL=v^2/(2g)$. Prikazani laminarni profil zadovoljava prianjanje uz stijenke; koljeno mijenja smjer toka bez pregrade ili prekida prolaza.” | Prva rečenica ponavlja okvir r. 42. Druga je potvrda ispravnosti skice, dakle trag izrade, a ne fizika. Prijedlog: „Ventil na skici daje nagli pad EGL-a, a ravne dionice jednoličan. Uz $\alpha=1$ razmak EGL–HGL jednak je $v^2/(2g)$. Profil brzine u ravnoj dionici prianja uz stijenke.” | P2 |
| u13:77, 99, 142, 162, 447, 685, 815 | K7 | „Darcy–Weisbachov zapis”, „Darcy–Weisbachova korelacija” (r. 99), „Darcy–Weisbachove jednadžbe”, „Darcyjeve formule”, „Darcyjev zapis”, „Darcy–Weisbachov model” | Jedan naziv: „Darcy–Weisbachova jednadžba”. Na r. 99 „korelacija” je pogrešan naziv jer je jednadžba definicija $\lambda$ (korelacije su Colebrook–White, Swamee–Jain): „Darcy–Weisbachova jednadžba i Moodyjev dijagram standardni su prikaz …”. | P2 |
| u13:99 | K10 | „Oba doprinosa sažimaju nepovratnu pretvorbu mehaničke energije u unutarnju energiju zbog viskoznih naprezanja i miješanja.” | Isto kaže r. 1 i okvir Dublje (r. 56–62). „Linijski i lokalni doprinosi nisu dvije nove sile, nego sažetak iste disipacije iz jednadžbe [-@eq-cjevovodi-disipacija-kao-izvor-gubitka-02].” | P3 |
| u13:113 | K3 (i K2) | „Izlaz je razlika tokova mehaničke energije …, uz kote i nejednolike profile ($\alpha\neq1$), iz koje se za svaki put kroz razdjelnik izvodi koeficijent $\xi$ …” (36 riječi) | „Izlaz je razlika tokova mehaničke energije između ulaza i svakog izlaza, uz kote i nejednolike profile ($\alpha\neq1$). Iz nje za svaki put kroz razdjelnik izvodimo koeficijent $\xi$ s jasno navedenom referentnom brzinom i podjelom protoka.” Prvo lice izjednačuje okvir s ostala tri CFD okvira. | P3 |
| u13:113, 214, 276 | K4 | Uvodni podebljani upiti CFD okvira: „Kako CFD rezultat postaje podatak za cjevovod?”, „Koliki dio otpora dolazi iz ravnih vodova?”, „Hoće li bolji razdjelnik povećati protok u stvarnom sustavu?” | Četvrti okvir (r. 368) ima izjavni podnaslov, pa su okviri neujednačeni. Prijedlog: „Koeficijent gubitka razdjelnika iz CFD-a.”, „Udio otpora ravnih vodova.”, „Bolji razdjelnik i protok stvarnog sustava.” | P3 |
| u13:115 | K12 (i K3) | „Provjera: sam statički pad tlaka nije uvijek gubitak jer se u proširenju dio kinetičke energije vraća u tlak, pa se, kao u ranijem Venturijevu primjeru, zadržava cijela energijska bilanca; izvedeni $\xi$ mora …” (40 riječi) | Primjer je u pog. 8 i treba mu broj. „Provjera: sam statički pad tlaka nije uvijek gubitak jer se u proširenju dio kinetičke energije vraća u tlak. Zato, kao u primjeru [-@ex-u09-venturijeva-cijev-za-mjerenje-protoka-ulja-t2], zadržavamo cijelu energijsku bilancu. Izvedeni $\xi$ mora u turbulentnom području biti približno neovisan o protoku.” | P2 |
| u13:134, 174 | K2 | „Promatra se odsječak fluida …”; „pa se odabere početna procjena … i ponavlja se iteracija” | Izlaganje drugdje ide u prvom licu množine („Promatrajmo”, r. 19). Prijedlog: „Promatramo odsječak fluida …”; „pa odaberemo početnu procjenu, primjerice $\lambda_0=0{,}02$, i ponavljamo iteraciju”. | P3 |
| u13:148 | Pravopis i stil | „dakle $\lambda$ nije ništa drugo nego bezdimenzijsko smično naprezanje stijenke” | „dakle je $\lambda$ bezdimenzijsko smično naprezanje stijenke” | P3 |
| u13:162, 214 | K10 | r. 162: „Isti zapis vrijedi i u CFD-u: integral $\tau_{st}$ … mora vratiti $64/Re$, inače …”; r. 214: „Laminarni test treba vratiti $64/Re$” | Isti laminarni CFD test stoji na dva mjesta. Zadržati ga u CFD okviru (r. 214) i dodati mu uvjet „inače tok u domeni nije razvijen ili mreža ćelija nije dovoljno fina”; rečenicu na r. 162 izbrisati. | P3 |
| u13:162, 214, 415 | K7 | „mora vratiti $64/Re$”, „treba vratiti”, „vraća ukupni gubitak” | Programerski kalk. Prijedlog: „mora dati $64/Re$”, „treba dati”, „daje ukupni gubitak”. | P3 |
| u13:205–207 | K1 | Vidljiva adresa u PDF-u: „…?path=u10_moody_dijagram.ipynb”; QR i Colab upućuju na `u10_…` | Unutarnja oznaka „u10” stoji u pog. 13 i ne odgovara numeraciji poglavlja. Ne predlažem zamjenu teksta jer preimenovanje bilježnice mijenja poveznice i provjere. Autorica odlučuje o preimenovanju ili skraćenom prikazu poveznice. | P3 |
| u13:202 | K12 | „U nastavku provjeri i Colebrookov i energijski rezidual” | Nije jasno odnosi li se na tekst ili na bilježnicu. „U drugom dijelu bilježnice provjeri i Colebrookov i energijski rezidual”. | P3 |
| u13:216 | K5 (i K2, K7) | „dobro opisani 1D relacijom”; „Za zidni model treba uskladiti definiciju ekvivalentne hrapavosti” | „1D” se rabi samo ovdje (drugdje „jednodimenzijski”). „Zidni model” nije naziv iz pog. 12 („model stijenke”, „zidna funkcija”). Prijedlog: „… dobro opisani jednodimenzijskom relacijom …”; „Za zidnu funkciju ([]{u12}) usklađujemo definiciju ekvivalentne hrapavosti; ona nije automatski jednaka svakoj izmjerenoj visini neravnina.” | P3 |
| u13:219 | K4 | Naslov „Serijske i paralelne mreže” | Odjeljak obrađuje i petlje (Hardy–Cross), kako najavljuje r. 7. „Serijske, paralelne i petljaste mreže” (ID ostaje). | P3 |
| u13:223 | K5 | „korisno je uvesti $h_g=RQ^2$, $R=…$” | $R$ nigdje nije imenovan, a iznimka oznake mora se uvesti uz definiciju. „… korisno je uvesti hidraulički otpor dionice $R$ (u ovom poglavlju $R$ nije polumjer):” | P2 |
| u13:232 (jedn. 13.18) | K6 | „Za paralelne grane između čvorova A i B vrijedi …, $R_iQ_i^2=h_{AB}$”; $R_{eq}$ | Na sl. 13.1 A i B su spremnici, a paralelne grane spajaju čvorove C i D. Prijedlog: „između čvorova C i D (slika [-@fig-cjevovodna-mreza-pregled])” i $h_{CD}$. Engleski indeks „eq” odstupa od hrvatskih indeksa (gubitak, stijenka); autorica odlučuje o $R_{ekv}$. | P3 |
| u13:253 | K4 | Naslov okvira „Fizikalno značenje — Što se izjednačuje?” | Naslov okvira ne postavlja pitanje. „Fizikalno značenje — Jednak pad energije paralelnih grana”. | P2 |
| u13:255, 265 | K10 | r. 265: „Nije: jednak pad energije slijedi iz zajedničkih krajnjih čvorova, a protoci ovise o otporima grana; kontinuitet traži samo …” | Prvi dio ponavlja okvir r. 255. „Nije: protoci ovise o otporima grana, a kontinuitet traži samo da njihov zbroj odgovara dotoku.” | P3 |
| u13:261 | Pravopis i stil | „Koja grana preuzima najveći protok?” | Grane su dvije (r. 263), pa treba komparativ: „Koja grana preuzima veći protok?” | P3 |
| u13:265 | K3 | „Pokus vrijedi za turbulentne grane; nastavci zasebno obrađuju Z3 i Z6.” | „Nastavci” je nejasno; bilježnica ima zasebne odjeljke za Z3 i Z6. „Pokus vrijedi za turbulentne grane. Zasebni odjeljci iste bilježnice obrađuju Z3 i Z6.” | P2 |
| u13:276 | K12 (i K3) | „Ručni @ex-radna-tocka-vfd određuje protok … Zato nakon promjene otpora razdjelnika ne zadržavamo automatski dotok iz []{u07}.” — u PDF-u „dotok iz pog. 7 Kinematika, kontrolni volumen i kontinuitet. Model …” | Ne kaže se koji je dotok iz pog. 7 (riječ je o ukupnom protoku pretpostavljenom za rashladni krug). „Primjer [-@ex-radna-tocka-vfd] ručno određuje protok presjecištem karakteristika crpke i sustava. Zato nakon promjene otpora razdjelnika ne zadržavamo automatski ukupni dotok pretpostavljen za rashladni krug u []{u07}.” | P2 |
| u13:292 | K5 (i K6) | „često se piše $H_s(Q)=H_{stat}+RQ^2$.” | $H_{stat}$ nije definiran, a ista je veličina u r. 286 $\Delta z$. „… često se piše $H_s(Q)=H_{stat}+RQ^2$, gdje je $H_{stat}=\Delta z$ statička visina.” | P2 |
| u13:301 | K7 | „pomiče crpkinu krivulju”; „na crpkinim krivuljama” | „pomiče krivulju crpke”; „na krivuljama crpke”. Uz to u istoj rečenici $H$ i $P$ stoje bez indeksa ($H_p$, $P_{vr}$); autorica odlučuje. | P3 |
| u13:317 | K5 | „Ako motor i pretvarač imaju učinkovitosti $\eta_m$ i $\eta_f$” | Prvi spomen, a vrsta pretvarača navodi se tek u P5. „Ako motor i frekvencijski pretvarač imaju …”. | P3 |
| u13:337 | K4 | Naslov „Usis i $NPSH$: nužan, ali ne konačan kriterij” | Formula bez indeksa u naslovu stoji prije definicije (r. 339). „Usisna rezerva NPSH: nužan, ali ne konačan kriterij”. | P3 |
| u13:344–355 | K5 (i K6) | Jedn. 13.27–13.28 uvode $p_{aps,s}$, $v_s$ i $h_{g,s}$; r. 348 definira samo $p_v$, a r. 355 samo $z_s$. | Urednički stil izričito traži da se iznimka $v_s$ (u pog. 13 brzina u usisnom presjeku, inače brzina broda) uvede uz definiciju. r. 348: „gdje su $p_{aps,s}$ apsolutni tlak i $v_s$ srednja brzina u usisnom presjeku S (u ovom poglavlju $v_s$ nije brzina broda), a $p_v$ tlak zasićene pare pri radnoj temperaturi.” r. 355 dopuniti: „… a $h_{g,s}$ gubitak u usisnom vodu od slobodne površine do presjeka S.” | P1 |
| u13:357, 362, 370, 671 | K10 | Upozorenje da $NPSH_a$ sam ne dokazuje rad bez kavitacije stoji na šest mjesta: r. 357, Granica modela r. 362, CFD r. 370 („Pozitivan $NPSH_a$ sam ne potvrđuje prihvatljiv rad.”), P6 r. 671, Provjeri sebe 4 (r. 701–706) i Sažetak r. 903. | Glavno mjesto ostaje r. 357, a uz njega Granica modela, Provjeri sebe i Sažetak. Izbrisati rečenicu na r. 370. Izbrisati i posljednju rečenicu P6 (r. 671), jer odmah iza nje Provjeri sebe 4 postavlja isto pitanje. Ograda o $NPSH_r$ i margini ostaje na r. 357 i 706. | P2 |
| u13:368 | K12 (i K3) | „U istom rashladnom krugu sniženje razine …”; „za procjenu nastanka pare koristimo apsolutni statički tlak pri toj temperaturi” | Nije jasno koji je krug „isti”, a „tlak pri toj temperaturi” zvuči kao da se tlak mjeri pri temperaturi. Ako je namjera usporedba s tlakom pare: „U rashladnom krugu s razdjelnikom iz odjeljka [-@sec-linijski-lokalni-gubitci] …”; „… apsolutni statički tlak uspoređujemo s tlakom pare pri toj temperaturi.” Autorica treba potvrditi da značenje ostaje isto. | P3 |
| u13:370 | K12 | „Time povezujemo razinu spremnika iz hidrostatike s lokalnim tokom u rotoru, koji obrađuje sljedeće poglavlje.” | Na drugo poglavlje upućuje se brojem. „… razinu spremnika iz []{u03} s lokalnim tokom u rotoru, koji obrađuje []{u14}.” | P2 |
| u13:415 | K8 (i stil) | „$\Delta p/(\rho g)=37\,400/(1000\cdot9{,}81)=3{,}81\ \mathrm{m}$ vraća ukupni gubitak; …” | Rečenica počinje formulom, a 3,81 m i 3,82 m su isti rezultat iz istog primjera. „Provjera unatrag daje $\Delta p/(\rho g)=37\,400/(1000\cdot9{,}81)=3{,}81\ \mathrm{m}$, što je do zaokruživanja ukupni gubitak $h_g=3{,}82\ \mathrm{m}$; lokalni elementi daju trećinu ukupnog gubitka, pa se u kratkom vodu ne smiju zanemariti.” | P3 |
| u13:423 | K6 | „Rashladna smjesa gustoće $1050\ \mathrm{kg/m^3}$ i kinematičke viskoznosti $\nu=…$” | Gustoća nema oznaku, iako se poslije rabi $\rho$ (r. 455, 459). „… gustoće $\rho=1050\ \mathrm{kg/m^3}$ …”. | P3 |
| u13:459 | Pravopis i stil | „$\mu=\rho\nu=5{,}25\cdot10^{-3}\ \mathrm{Pa\,s}$, pa jednadžba … daje” | Rečenica ne počinje simbolom. „Dinamička viskoznost iznosi $\mu=\rho\nu=5{,}25\cdot10^{-3}\ \mathrm{Pa\,s}$, pa jednadžba [-@eq-poiseuille-u13] daje”. | P3 |
| u13:500 | K3 | „Početna raspodjela koja zadovoljava čvorne bilance: $Q_{AB}=22{,}0$, …” | Rečenica bez glagola. „Za početnu raspodjelu koja zadovoljava čvorne bilance uzimamo $Q_{AB}=22{,}0$, $Q_{BC}=10{,}0$, $Q_{CD}=-6{,}0$ i $Q_{DA}=-18{,}0\ \mathrm{L/s}$ (…).” | P3 |
| u13:515 | K8 | „Novi protoci su $19{,}08$, $7{,}08$, $-8{,}92$ i $-20{,}92\ \mathrm{L/s}$.” | Zarez između brojeva s decimalnim zarezom čita se dvoznačno. „Novi protoci su $Q_{AB}=19{,}08$, $Q_{BC}=7{,}08$, $Q_{CD}=-8{,}92$ i $Q_{DA}=-20{,}92\ \mathrm{L/s}$.” | P2 |
| u13:521 | K6 | „$h_{AB}=2{,}56$, $h_{BC}=2{,}16$, $h_{DC}=0{,}99$ i $h_{AD}=3{,}73\ \mathrm{m}$” | Indeksi gubitaka (DC, AD) razlikuju se od indeksa protoka (CD, DA) bez objašnjenja. Dodati: „(indeksi gubitaka slijede stvarni smjer toka)”. | P3 |
| u13:533 | K7 | „Karakteristike crpke pri nazivnoj brzini vrtnje i otvorenog sustava, s protokom $Q$ u $\mathrm{L/s}$, glase:” | „Otvoreni sustav” je dvoznačan (otvoreni spremnici ili otvoren ventil), a jedinica visine nije navedena (u Z6 jest). Ako se misli na ventil, kako sugerira r. 541: „Karakteristika crpke pri nazivnoj brzini vrtnje i karakteristika sustava s otvorenim ventilom, s protokom $Q$ u $\mathrm{L/s}$ i visinama u metrima, glase:” | P3 |
| u13:566, 866, 868, 873, 874, 879 | K7 | „omjer brzina $s=n_2/n_1$”, „pri nazivnoj brzini”, „na sniženu brzinu” | U poglavlju u kojem je „brzina” brzina fluida treba pisati „brzina vrtnje”: „omjer brzina vrtnje”, „pri nazivnoj brzini vrtnje”, „na sniženu brzinu vrtnje”. | P3 |
| u13:589 | K8 (i K5) | „visina dobave pada na $H_p=10\ \mathrm{m}$”; „Nakon čišćenja izmjenjivača”; r. 620 $E_{el}=P_{el}t$ | Različita točnost uz $H_p=12{,}0$ m; $t$ i vrsta izmjenjivača nisu uvedeni. „… pada na $H_p=10{,}0\ \mathrm{m}$”; „Nakon čišćenja izmjenjivača topline”; „Rashladni krug radi $t=7000\ \mathrm{h/god}$ …”. | P3 |
| u13:623 | Pravopis i stil | „Nakon čišćenja potrošnja pada na $5{,}92\ \mathrm{MWh/god}$, odnosno štedi se oko $1{,}18\ \mathrm{MWh/god}$.” | „Odnosno” ne uvodi istovrijednost nego posljedicu. „…, pa ušteda iznosi oko $1{,}18\ \mathrm{MWh/god}$.” | P3 |
| u13:635 | Pravopis i stil | „protječe usisom promjera $D=80\ \mathrm{mm}$” | „protječe usisnim vodom promjera $D=80\ \mathrm{mm}$” | P3 |
| u13:712 (sl. 13.4) | K13 | Naslovi panela: „Isti vod, dva fluida”, „Uravnoteženje dvaju ogranaka”, „Radna točka uz promjenjivo trenje”, „Balastna crpka: napunjen usis”; panel Z5: „λ(Re, k_s/D) računaj.”; u panelu Z2 redak podataka u drugom (serifnom) pismu | Naslovi panela razlikuju se od naslova zadataka (Z2, Z3, Z4, Z6), pa ih treba uskladiti. Panel Z5 sadrži uputu za postupak, a skica samostalnog zadatka ne otkriva postupak; dovoljno je „$k_s=0{,}15$ mm (nova), $0{,}50$ mm (stara)”. Pismo u panelu Z2 treba uskladiti s ostalim panelima. | P3 |
| u13:714 | K10 (i K1) | „U Z4 krivulja sustava i radna točka traženi su rezultat, pa nisu nacrtane. U Z6 kota daje dubinu referentnog usisnog presjeka S ispod vodne linije, pa je $z_s=-1{,}8\ \mathrm{m}$; zadani $NPSH_r(Q)$ vrijedi samo za nazivnu brzinu vrtnje.” | Rečenica o Z4 obrazlaže izradu skice, a panel već piše „$H_s(Q)$ i radna točka = ?”. Podatci o Z6 ($z_s=-1{,}8$ m, $NPSH_r$ samo pri nazivnoj brzini) stoje još na skici, u tekstu zadatka (r. 868, podebljano), u Traži se 3 i u naputku (r. 879). Prijedlog: obje rečenice izbrisati, a prvu („U Z1 ventil je lokalni otpor s otvorenim prolazom.”) zadržati. Svi brojevi i uvjeti ostaju u r. 868. Napomena za autoricu: višestruko isticanje uvjeta za $NPSH_r$ djelomično otkriva odluku T4 zadatka (K15). | P2 |
| u13:751 | Pravopis i stil | „Promatrani razmak $L=4{,}0\ \mathrm{m}$ nalazi se u potpuno razvijenom toku” | „Promatrana dionica duljine $L=4{,}0\ \mathrm{m}$ nalazi se u potpuno razvijenom toku” | P3 |
| u13:779 | K6 | „novi ventil dodaje $h_{g,V}=R_vQ_i^2$ s $R_v\ge0$” | Ventil ima indeks $V$ u $h_{g,V}$ (i u Z6: $H_V$, $E_V$), a $v$ u $R_v$; $v$ u knjizi znači vodu ($\rho_v$) i tlak pare ($p_v$). Prijedlog: $R_V$, uz isto u naputku, kontrolnom rezultatu, ključu i verifikatoru. | P2 |
| u13:784 | K7 | „Zatim zatvori kontinuitet i usporedi gubitke na obama putovima.” | „Zatim provjeri kontinuitet i usporedi gubitke na obama putovima.” | P3 |
| u13:854 | K8 | „$\lambda\approx0{,}0238/0{,}0228/0{,}0221$ i $h_g\approx33{,}1/10{,}8/3{,}56\ \mathrm{m}$ za 80/100/125 mm” | Kosa crta u formuli čita se kao dijeljenje. „Za $D=80$; $100$ i $125\ \mathrm{mm}$: $\lambda\approx(0{,}0238;\,0{,}0228;\,0{,}0221)$ i $h_g\approx(33{,}1;\,10{,}8;\,3{,}56)\ \mathrm{m}$” (isti oblik kao u ključu Z6). | P2 |
| u13:868 | K3 | „Referentni usisni presjek S crpke nalazi se 1,8 m **ispod** vodne linije, tj. $z_s=-1{,}8$ m (napunjen usis), atmosferski tlak je …, usisni gubitak … $h_{g,s}=1{,}4$ m, a tlak pare … $p_v=4{,}2$ kPa.” (50 riječi) | Samostalne tvrdnje spojene su zarezom. „Referentni usisni presjek S crpke nalazi se $1{,}8\ \mathrm{m}$ **ispod** vodne linije, tj. $z_s=-1{,}8\ \mathrm{m}$ (napunjen usis). Atmosferski tlak je $p_{atm}=101{,}3\ \mathrm{kPa}$, a usisni gubitak koša, filtra i armature pri protoku prigušenog sustava iznosi $h_{g,s}=1{,}4\ \mathrm{m}$. Tlak pare morske vode pri $30\ \mathrm{^\circ C}$ iznosi $p_v=4{,}2\ \mathrm{kPa}$.” | P2 |
| u13:873 | K6 | „godišnju energiju $E_s$” | Indeks $s$ u istom zadatku znači sustav ($H_s$), usis ($z_s$, $h_{g,s}$) i regulaciju brzinom vrtnje ($E_s$). Autorica bira jednoznačan indeks (npr. $E_n$), uz ključ i verifikator; ne predlažem zamjenu bez te provjere. | P3 |
| u13:874 | K3 | „Zatim odluči koji podatci nedostaju …, kad je presjek S samo $0{,}4$ m ispod vodne linije ($z_s=-0{,}4$ m); zadani $NPSH_r$ nemoj nekritički prenijeti na sniženu brzinu.” (38 riječi) | „… ($z_s=-0{,}4\ \mathrm{m}$). Zadani $NPSH_r$ nemoj nekritički prenijeti na sniženu brzinu vrtnje.” | P3 |
| u13:885 | K8 | „$(H_V,H_s)\approx(17{,}00;11{,}50)$”, „$(NPSH_a,NPSH_r,NPSH_a-NPSH_r)\approx(…)$” | Oznake u n-torki odvojene su zarezom, a vrijednosti točkom-zarezom. Radi dosljednosti: „$(H_V;\,H_s)$”, „$(NPSH_a;\,NPSH_r;\,NPSH_a-NPSH_r)$” i isto u $(E_V;\,E_s;\,\Delta E)$. | P3 |
| u13:898 | K3 | „a prijelazno područje $2300\lesssim Re\lesssim4000$ nije pouzdano” | Nepouzdana je korelacija, a ne područje (r. 194: „jedna univerzalna korelacija ondje nije pouzdana”). „…, a u prijelaznom području $2300\lesssim Re\lesssim4000$ jedna univerzalna korelacija nije pouzdana.” | P2 |
| u13:903 | K3 | „ni $NPSH_a>0$ ni jednodimenzijski stacionarni model ne opisuju lokalnu kavitaciju ni vodeni udar” | Spoj sugerira da $NPSH_a$ opisuje (ili ne) vodeni udar. „…; $NPSH_a>0$ ne opisuje lokalnu kavitaciju, a jednodimenzijski stacionarni model ne opisuje ni lokalnu kavitaciju ni vodeni udar.” | P2 |
| u13:9, 72, 97, 311, 317, 525, 811, 838, 868 | Pravopis i stil | „jest ukupna raspoloživa visina”, „jest jednodimenzijska”, „jest ukupni koeficijent”, „vratilna snaga jest”, „snaga … jest”, „jest pojednostavnjenje”, „Interval … jest”, „gubitak visine jest”, „model … jest” | Naglašeni oblik „jest” u neutralnom položaju zvuči kao prijevod matematičkog „is”. Prijedlog: „je” ili „iznosi” (npr. „Interval traženja radne točke je …”, „Dopušteni gubitak visine je $h_g\le15\ \mathrm{m}$”, „vratilna snaga iznosi”). | P3 |

## Zbroj nalaza

| Pravilo | P1 | P2 | P3 | Ukupno |
| --- | ---: | ---: | ---: | ---: |
| K1 registar | 0 | 0 | 1 | 1 |
| K2 glas | 0 | 0 | 1 | 1 |
| K3 rečenice | 0 | 4 | 4 | 8 |
| K4 naslovi | 0 | 1 | 3 | 4 |
| K5 pojmovi i kratice | 1 | 2 | 4 | 7 |
| K6 oznake (urednički stil) | 0 | 2 | 4 | 6 |
| K7 nazivlje | 0 | 2 | 5 | 7 |
| K8 brojevi | 0 | 2 | 3 | 5 |
| K10 ponavljanje | 0 | 5 | 5 | 10 |
| K12 upućivanja | 0 | 3 | 2 | 5 |
| K13 slike | 0 | 0 | 3 | 3 |
| Pravopis i stil | 0 | 0 | 8 | 8 |
| **Ukupno** | **1** | **21** | **43** | **65** |

Nalazi s dvije oznake pravila broje se jednom, pod prvim navedenim pravilom.
Nalaza P0 nema.

## Tri najčešća obrasca

1. **Ponavljanje istog sadržaja na četiri do šest mjesta (K10).** Uvod (r. 3, 5, 7, 13)
   unaprijed iznosi formule i pravila koja odjeljci ponovno izvode. Upozorenja o
   referentnoj brzini za $\xi$, o paralelnim granama i o tome da $NPSH_a$ nije dovoljan
   vraćaju se u okvirima, napomenama uz skice, rješenjima i Sažetku. Mjestimice se
   ponavljaju doslovno (r. 3 i r. 899).
2. **Oznake i pojmovi bez definicije pri prvoj uporabi (K5, K6).** Bez definicije pri
   prvoj uporabi ostaju $R$, $H_{stat}$, $v_s$, $p_{aps,s}$, $h_{g,s}$ i NPSH. Ista
   razlika razina ima tri oznake ($H$, $\Delta z$, $H_{stat}$), a indeksi su dvoznačni
   ($R_v$ prema $h_{g,V}$; $s$ za sustav, usis i regulaciju). Uz to se kolebaju nazivi
   (Darcy–Weisbachova jednadžba, zapis, korelacija, formula, model; „mreža” za
   cjevovod i za računalnu mrežu; „brzina” za brzinu vrtnje).
3. **Upućivanja i rečenice teške za praćenje (K12, K3).** Upućivanja su opisna, bez broja
   („ranijem Venturijevu primjeru”, „sljedeće poglavlje”, „dotok iz pog. 7”, „u
   nastavku”, „nastavci”), a umetnuti naslov poglavlja prekida rečenicu u PDF-u.
   Pojedine rečenice spajaju samostalne tvrdnje zarezom ili točkom-zarezom (r. 115,
   868, 874), a dvije spajaju tvrdnje koje mijenjaju smisao (r. 898, 903).

## Ograničenja

- Ovo je autorska procjena urednika; nalazi nisu provjereni prijelomom niti provedeni.
  Prijedlozi koji diraju oznake ($\Delta z$ na sl. 13.1, $R_V$, indeks $E_s$) traže
  usklađivanje skice, ključa (dodatak F), bilježnice i verifikatora.
- PDF je pregledan kao tekst, a kao slika samo na str. 245, 247, 258 i 259. Izvlačenje
  teksta gubi dijakritike i formule, pa pravopis formula u PDF-u nije provjeren znak po znak.
- Prijedlozi na r. 368 i r. 533 tumače namjeru teksta; autorica treba potvrditi da je
  značenje sačuvano.
