## Mehanika fluida i numerika — pregled

Ovaj dodatak povezuje numeričke pojmove iz poglavlja 1–15 i pokazuje kako provjeriti rezultat simulacije prije inženjerske uporabe.

Naglasak je na vezi između fizikalne jednadžbe, numeričkog modela i provjere rezultata. Za samostalno postavljanje CFD simulacija potrebno je dodatno gradivo.

::: {.callout-tip icon="false"}
## Opseg dodatka {#što-se-ovdje-neće-dogoditi}

- **Očuvanje:** provjera bilance mase i drugih relevantnih veličina.
- **Konvergencija:** praćenje iteracija i usporedba rezultata na različitim mrežama.
- **Vjerodostojnost:** razlikovanje verifikacije numeričkog postupka i validacije fizikalnog modela.

Izvodi diskretizacijskih shema, rješavanje linearnih sustava i programske upute pripadaju posebnim kolegijima.
:::

## Pojmovnik numeričkih metoda

Sljedeća tablica objedinjuje numeričke metode i alate spomenute u udžbeniku, s upućivanjem na povezana poglavlja.

| Kratica | Puno ime | Što radi | Gdje se pojavila u MF1 |
|---|---|---|---|
| **CFD** | Computational Fluid Dynamics | Računalno rješavanje Navier–Stokesovih jednadžbi | Svuda — kao šira disciplina |
| **FVM** | Finite Volume Method | Domena se rastavlja na kontrolne volumene; bilance mase i količine gibanja po ćelijama | pog. 7 (kontinuitet), pog. 10 (KG) |
| **FEM** | Finite Element Method | Domena se rastavlja na elemente; rješava se varijacijski oblik parcijalnih diferencijalnih jednadžbi | Međudjelovanje fluida i konstrukcije |
| **VOF** | Volume of Fluid | Praćenje slobodne površine preko polja $\alpha \in [0,1]$ | pog. 2 (kapilarnost), pog. 6 (uzgon), pog. 15 (otvoreni tokovi) |
| **CSF** | Continuum Surface Force | Površinska napetost kao volumna sila u VOF-u | pog. 2 |
| **DNS** | Direct Numerical Simulation | Bez turbulencijskog modela razrješava sve dinamički relevantne skale, uz dovoljno finu mrežu i vremenski korak | pog. 12 (diferencijalni opis i turbulencija) |
| **LES** | Large Eddy Simulation | Rješava velike vrtloge, modelira male | pog. 12 |
| **RANS** | Reynolds-Averaged Navier-Stokes | Računa osrednjeno polje i modelira učinak nerazlučenih turbulentnih fluktuacija | pog. 12, pog. 13 |
| **k-ε** / **k-ω SST** | turbulentni modeli | Dodatne transportne jednadžbe za veličine kojima se zatvara učinak turbulencije | pog. 12, pog. 13 |
| **SIMPLE** / **PISO** / **PIMPLE** | algoritmi sprege $p$–$v$ | Iterativno usklađivanje tlaka i brzine da $\nabla\cdot\vec{v}=0$ | pog. 7 (kontinuitet) |
| **MRF** | Multiple Reference Frame (više referentnih okvira) | Stacionarna aproksimacija rotirajućih područja (pumpe, turbine) bez gibanja mreže | pog. 4 (rotirajući okvir), pog. 14 (turbostrojevi) |
| **Klizajuća mreža** *(engl. sliding mesh)* | gibanje dijelova mreže | Rotirajući i nepomični dio mreže razmjenjuju podatke preko klizajućeg sučelja | pog. 14 |
| **Zidne funkcije** *(engl. wall functions)* | modelska veza između prve ćelije i stijenke | Zatvaraju područje uz zid kada mreža ne razlučuje cijeli viskozni podsloj | pog. 12, pog. 13 |
| **y+** | $y^+$ kriterij | Bezdimenzijska udaljenost prve ćelije od zida; jedan od kriterija prikladnosti razlučivosti uz stijenku | pog. 12, pog. 13 |
| **Panelna metoda** | Panel Method | Potencijalno strujanje oko tijela; prema potrebi se spaja s modelom graničnog sloja | (vanjska aerodinamika) |

## Primjeri alata

Nazivi u nastavku služe samo za prepoznavanje vrsta alata, a ne kao preporuka proizvoda ni tvrdnja o mogućnostima pojedine inačice. Funkcije, licenciranje i podržani modeli mijenjaju se; prije uporabe treba provjeriti aktualnu službenu dokumentaciju.

| Primjer | Opća uloga u radnom tijeku |
|---|---|
| **OpenFOAM**, **ANSYS Fluent**, **Simcenter STAR-CCM+**, **SU2** | diskretizacija i rješavanje modela strujanja, ovisno o odabranoj inačici i modulu |
| **COMSOL Multiphysics** | spregnuti numerički modeli više fizikalnih polja |
| **EPANET**, **AFT Fathom**, **Pipe-Flo** | jednodimenzijski modeli cjevovoda ili mreža |
| **ParaView** | postprocesiranje i vizualizacija numeričkih podataka |

## Rječnik MF1 → CFD: prijevod pojmova

Sljedeća tablica izravno povezuje pojmove iz ovoga udžbenika s pripadnim pojmovima u računalnoj dinamici fluida. Cilj je olakšati prelazak na kasnije CFD kolegije, kada se isti koncept pojavi pod drugim imenom u alatu.

| Pojam u MF1 | CFD ekvivalent ili alat |
|---|---|
| Kontrolni volumen | Ćelija mreže (engl. *cell*, *control volume*) |
| Granica kontrolnog volumena | Plohe koje omeđuju ćeliju; vanjske plohe domene grupiraju se u rubna područja (*patches*) |
| Fizikalni rubni uvjet na granici domene | Postavka tipa `inlet`, `outlet`, `wall`, `symmetry` na patchu |
| Pretpostavka nestlačivosti | Izbor nestlačivog rješavača (npr. `simpleFoam` ili `pisoFoam` u inačicama koje ih sadrže) |
| Slobodna površina | Izoploha polja $\alpha = 0{,}5$ u VOF simulaciji |
| Težište istisnutog volumena (centar uzgona) | Geometrijski momenti istisnutog volumena tijela; polje $\alpha$ pomaže odrediti slobodnu površinu i uronjeni dio |
| Hidrostatska raspodjela tlaka | Hidrostatski dio fizičkog tlaka; `p_rgh` označuje tlak iz kojega je taj dio izdvojen |
| Profil brzine $v(r)$ u cijevi | Polje `U` kao funkcija položaja (uzorkovanje po liniji s alatom `sample`) |
| Sila na zid | Integracija tlačnih i viskoznih naprezanja (`forces`); `forceCoeffs` daje njihove bezdimenzijske koeficijente |
| Centar tlaka na plohi | Omjer momenta i rezultantne tlačne sile na ravnoj plohi, uz zadanu referencu tlaka |
| Reynoldsov broj | Jedan od kriterija za procjenu režima, razlučivosti i izbora modela; nije dovoljan sam |
| Froudeov, Weberov i Machov broj (pog. 9, 11 i 15) | Skaliranje stlačivosti, međupovršinskih pojava i slobodne površine |
| Bezdimenzioniranje jednadžbi, Π teorem (pog. 11) | Popis mjerodavnih parametara modela; samo u najjednostavnijem jednofaznom nestlačivom toku može ostati prvenstveno $Re$ |
| Moodyjev dijagram i koeficijent $\lambda$ | Neovisna 1D referenca za ukupni otpor cijevi; zidne funkcije su zaseban način zatvaranja toka uz zid u RANS-u |
| Bernoullijeva jednadžba (referentno rješenje idealnog modela) | Probna linija (`sampleDict`) duž strujnice; verifikacijska usporedba istih presjeka |
| Mlaz koji udara o plohu (sila) | Zidni patch s integracijom tlaka i smičnih naprezanja |
| Pokretna lopatica | MRF zona (`MRFZone`) ili klizajuća mreža |
| Trokuti brzina | Polja apsolutne i relativne brzine ($\vec{c} = \vec{w} + \vec{u}$) u MRF zoni |
| Linijski gubitci | Integral disipacije po dionici domene |
| Lokalni gubitci | Razrješavanje strujanja oko lokalnih elemenata (koljeno, ventil) |
| Metacentar | Hidrostatička referenca početne stabilnosti; 6-DOF rješavač u VOF simulaciji zasebno opisuje gibanje trupa |

## Kako se MF1 jednadžbe slažu u CFD slici

Ova tablica sažima glavne jednadžbe iz udžbenika i pokazuje njihovu izravnu ulogu u CFD-u.

| MF1 jednadžba / koncept | Numerička uloga |
|---|---|
| $p = F_n/A$, Pascalov zakon | Tlak kao polje; inicijalni uvjet tlaka |
| $dp/dz = -\rho g$, $p = p_0 + \rho gh$ | Inicijalni uvjet i temeljna razina polja `p_rgh` |
| $\tau = \mu\,dv/dy$ | Konstitutivni zakon u rješavaču (newtonski model) |
| Površinska napetost $\sigma$, kontaktni kut | VOF + CSF za višefazno strujanje |
| $F_U = \rho g V_{ist}$ (uzgon) | Referentna hidrostatička provjera numeričkog modela slobodne površine, primjerice VOF-a |
| Integracija tlaka na ravnoj plohi $F = \int_A p\,dA$ | Funkcijski objekti `forces`, *Force Reports* |
| $\nabla\cdot\vec{v} = 0$ (kontinuitet) | Sprega tlaka i brzine (SIMPLE/PISO/PIMPLE) |
| Bernoullijeva jednadžba | Referentno rješenje za verifikaciju idealiziranoga Eulerova modela |
| Eulerova diferencijalna jednadžba | Eulerov rješavač za neviskozno strujanje |
| Disipacija, $h_l = \lambda(L/D)(v^2/2g)$ | Pad mehaničke energije iz polja tlaka i brzine; turbulentni model i model strujanja uz stijenku utječu na predviđeni otpor |
| Integralni zakon količine gibanja | Izravna polazna formulacija metode konačnih volumena (FVM) |
| Relativna brzina, $\vec{w} = \vec{c} - \vec{u}$ | MRF metoda, klizajuća mreža (sliding mesh) za rotore |
| Reynoldsov broj $Re = vD/\nu$ | Procjena relativne važnosti viskoznosti; jedan od ulaza u odabir modela i mreže |
| Bezdimenzijski brojevi $Re, Fr, We, Ma$ (pog. 9, 11 i 15) | Bezdimenzionirane jednadžbe; ulazni parametri i kriteriji izbora modela |

## Kada CFD ne treba: granice primjenjivosti

Računalna dinamika fluida nije univerzalno sredstvo. U svakom inženjerskom projektu prvo se postavlja pitanje **može li se problem riješiti analitički ili tabličnim podatcima** — tek ako odgovor nije zadovoljavajući, primjenjuje se CFD. U sljedećim idealiziranim slučajevima analitički ili jednodimenzijski račun može biti dovoljan:

::: {.mf1-warning}
<p class="mf1-box-label">Slučajevi u kojima analitika dostaje</p>

- **Pascalov prijenos sile u hidrauličnim sustavima** — analitičke formule $\Delta p = F/A$ i $A_1 s_1 = A_2 s_2$ daju odgovor za idealni nestlačivi model bez gubitaka; CFD bi numerički reproducirao isti rezultat uz mnogo veći trošak.
- **Hidrostatika u mirnim spremnicima** — $p = p_0 + \rho g h$ vrijedi za homogeni fluid u jednolikom gravitacijskom polju; CFD donosi vrijednost tek pri dinamičkim uvjetima poput zapljuskivanja ili prelijevanja.
- **Sila na ravnu plohu pri poznatoj hidrostatici** — izraz $F = \rho g z_T A$ vrijedi za homogeni fluid, jednoliku gravitaciju i poništene atmosferske doprinose; pri valovima ili strujanju uz plohu može biti potreban složeniji model.
- **1D proračun cjevovoda u stacionarnom režimu** — Darcy–Weisbach uz dokumentirane koeficijente često daje odgovor primjeren projektnoj odluci. Nesigurnost nije univerzalnih $5{-}15\,\%$, nego ovisi o podatcima o hrapavosti, lokalnim elementima, režimu i mjerenju protoka.
- **Početna statička stabilnost broda u mirnoj vodi** — metacentarska teorija daje kriterij za male kutove početne stabilnosti. Veći kutovi, valna pobuda, slobodne površine i poplavljivanje traže širi hidrostatički ili hidrodinamički model.
:::

Pravilo prakse: najprije se bira najjednostavniji model koji odgovara odluci i potrebnoj nesigurnosti. CFD donosi vrijednost kada su prostorna raspodjela, složena geometrija ili nestacionarnost bitne, ali i tada 1D račun ostaje važna neovisna provjera reda veličine.

## Kako procijeniti računski trošak

Vrijeme izvođenja nije svojstvo samoga naziva metode. Ovisi barem o broju ćelija i jednadžbi, broju vremenskih koraka, nelinearnoj konvergenciji, hardveru, paralelizaciji, spremanju izlaza i broju varijanti. Zato se bez definiranoga slučaja ne navodi univerzalna pretvorba „vrsta modela → sati računanja”.

Za nastavni i projektni rad koristan je redoslijed:

1. započeti najjednostavnijim modelom koji može odgovoriti na ciljano pitanje;
2. procijeniti trošak kratkim probnim izvođenjem na gruboj mreži, bez zaključivanja o konačnom rezultatu;
3. planirati najmanje tri sustavno profinjene mreže i, za nestacionarni slučaj, provjeru vremenskoga koraka;
4. tek nakon provjere bilanci i konvergencije praćenih veličina dodavati složeniju geometriju ili fizikalni model.

Laminarni referentni slučaj s poznatim rješenjem zato je bolji prvi korak od složene turbulentne simulacije: istodobno provjerava postavke, mrežu, bilance i način izvještavanja pogreške.

## Tipičan CFD tijek na primjeru iz MF1: Venturijeva cijev

Kako bi se konkretno vidjelo što sve CFD analiza obuhvaća, prikazuje se šest koraka na Venturijevoj cijevi. Presjeci usporedbe moraju biti unaprijed definirani: presjek 1 u razvijenom ulaznom toku i presjek 2 u grlu.

### Korak 1 — Geometrija {.unnumbered .unlisted .mf1-step}

Iz CAD modela ili izravno u alatu konstruira se trodimenzijska geometrija cijevi sa suženjem. Za simetrične probleme često je dovoljna polovica geometrije s ravninom simetrije, što smanjuje broj ćelija i računski trošak. Ulazni presjek, izlazni presjek, ravnina simetrije i unutarnja stijenka cijevi označavaju se kao zasebna rubna područja (*patches*).

### Korak 2 — Mreža {.unnumbered .unlisted .mf1-step}

Geometrija se diskretizira u mrežu kontrolnih volumena. Ključne odluke:

- **Gustoća mreže** — gušće u suženju gdje gradijenti brzine i tlaka rastu;
- **Sloj uz stijenku** — prizmatski elementi uz stijenku radi razrješavanja graničnog sloja;
- **$y^+$ vrijednost** — cilj mora odgovarati odabranom modelu strujanja uz stijenku; razriješeni sloj i zidne funkcije imaju različite zahtjeve, a prijelazno područje treba izbjegavati prema dokumentaciji konkretnog modela.

Broj ćelija sam po sebi nije kriterij dostatnosti. Potrebna je najmanje gruba, srednja i fina mreža s usporedivim obrascem profinjenja, a mjerodavne izlazne veličine moraju pokazati konvergenciju.

### Korak 3 — Rubni uvjeti {.unnumbered .unlisted .mf1-step}

Svakoj plohi geometrije pridružuje se odgovarajući uvjet:

- **Ulaz i izlaz** — konzistentan par uvjeta, primjerice zadan profil/protok na ulazu i statički tlak na izlazu; ne smiju se istodobno propisati međusobno nespojivi protok i tlak;
- **Stijenka** — nepropusnost uz dopušteno klizanje za idealni Eulerov referentni slučaj ili uvjet prianjanja `noSlip` za viskozni model;
- **Ravnina simetrije** (ako se koristi) — uvjet `symmetry`.

Rubni uvjeti moraju odgovarati fizičkom eksperimentu i analitičkom modelu s kojim će se rezultat usporediti.

### Korak 4 — Rješavač i iteracijska konvergencija []{#korak-4-rješavač-i-iteracijska-konvergencija} {#korak-4-solver-i-iteracijska-konvergencija .unnumbered .unlisted .mf1-step}

Za nestlačivi stacionarni problem bira se odgovarajući stacionarni rješavač i sprega tlaka s brzinom. Pad reziduala potreban je, ali nije dovoljan dokaz konvergencije. Istodobno se prate protok kroz svaki otvor, relativna neravnoteža mase, $\Delta p_{12}$, sile i druge izlazne veličine. Kriteriji se zadaju prema namjeni modela; ne postoji univerzalan broj redova veličine koji jamči ispravan rezultat.

### Korak 5 — Verifikacija numeričkog rješenja {.unnumbered .unlisted .mf1-step}

**Verifikacija pita: rješavamo li odabrane jednadžbe dovoljno točno?** Najprije se zatvara globalna bilanca mase. Zatim se na najmanje tri sustavno profinjene mreže uspoređuju $\Delta p_{12}$, brzina u grlu i druga projektno važna veličina. Treba izvijestiti relativne promjene među mrežama i, kada je red profinjenja dovoljno uredan, procijeniti diskretizacijsku nesigurnost. Za nestacionarni model analogno se provjerava vremenski korak. Reziduali, bilanca i mrežna/vremenska konvergencija tri su odvojena dokaza.

Za idealni Eulerov slučaj s nepropusnom stijenkom uz dopušteno klizanje dodatna je verifikacijska provjera Bernoullijev rezultat između **ulaza i grla**:

$$
\Delta p_{12,B}=\frac{\rho}{2}\left(v_2^2-v_1^2\right).
$$ {#eq-cfd-vv-korak-5-verifikacija-numerickog-rjesenja-01}

Razlika bi se trebala smanjivati s konvergencijom rješenja. Ne zadaje se unaprijed univerzalna tolerancija od $5$ ili $10\,%$; prihvatljivost ovisi o potrebnoj nesigurnosti projektne odluke.

### Korak 6 — Validacija fizikalnog modela {.unnumbered .unlisted .mf1-step}

**Validacija pita: opisuju li odabrane jednadžbe stvarni sustav dovoljno dobro?** Viskozni model s uvjetom prianjanja validira se prema mjerenom $\Delta p_{12}$, koeficijentu protoka ili drugom eksperimentalnom podatku pri istim geometrijskim i radnim uvjetima. Mjerna i numerička nesigurnost moraju se prikazati uz usporedbu.

Razlika viskoznog CFD-a prema idealnom Bernoulliju nije automatski pogreška: dio je stvarna disipacija. Posebno, usporedba tlaka između ulaza i izlaza jednake površine s idealnim Bernoullijem dala bi idealno nultu razliku, dok realni tok ima trajan gubitak tlaka. Zato se uvijek uspoređuju iste mjerni presjeci i modeli s usklađenim pretpostavkama.

Tek kada su dokumentirane i verifikacija i validacija, rezultat može biti temelj za projektnu odluku unutar navedenog područja primjene.

## Tri pripremljena V&V paketa

Repozitorij sadrži male strojno čitljive pakete u `data/cfd/`. Oni ne zahtijevaju lokalnu instalaciju rješavača i služe učenju revizijskog traga: svaka vrijednost ima izvor, jedinicu i ograničenje.

| Paket | Što je stvarno dostupno | Što se smije zaključiti |
|---|---|---|
| [`poiseuille_laminar`](../data/cfd/poiseuille_laminar/README.md) | analitičko rješenje, tri sintetičke mreže, reziduali, monitor protoka, masena bilanca i GCI | provjera V&V postupka prema poznatom rješenju; nije test određenog rješavača |
| [`venturi_diffuser`](../data/cfd/venturi_diffuser/README.md) | tri sintetičke mreže, zadani 1D referentni model, reziduali, monitor gubitka, bilanca i GCI | pedagoška verifikacija obrade rezultata; nije eksperimentalna validacija Venturija |
| [`hydrofoil_experiment`](../data/cfd/hydrofoil_experiment/README.md) | Ladsonove javne mjerne sile [@ladson1988], stvarni FUN3D rezultati NASA TMR-a na tri mreže [@nasa-tmr-naca0012] i zasebna nastavna dopuna nesigurnosti za Z6 u 12. poglavlju | mrežni trend i uvjetna brojčana usporedba otpora; nastavne pretpostavke ne nadomještaju izvorne dokaze za validaciju arhivskog proračuna |

Validator `python tools/validate_cfd_vv.py` ponovno računa analitičke vrijednosti, bilance, rastav otpora, opaženi red i GCI. Na trima odabranim najfinijim mrežama $C_D$ monotono opada, a $C_L$ monotono raste. To omogućuje tro-mrežnu procjenu GCI-ja, ali samo po sebi ne dokazuje asimptotsko područje. Validator provjerava i podrijetlo te račun nastavne dopune; izvorne arhivske dijagnostike ostaju označene kao nedostupne.

**Kako su odabrane približne vrijednosti u Z6?** Najfinija FUN3D mreža daje $C_D=0{,}01222408822$, zaokruženo na $0{,}01222$. U Ladsonovoj seriji s prisilnim prijelazom (120 grit) pri $Re_c=6\cdot10^6$ i $Ma=0{,}15$ susjedne su točke $(\alpha;C_D)=(8{,}08^\circ;0{,}00995)$ i $(10{,}10^\circ;0{,}01175)$. Linearna interpolacija na CFD kut $10{,}00^\circ$ daje $C_{D,ref}\approx0{,}01166089$, zaokruženo na $0{,}01166$. Time se uklanja izravna usporedba dvaju različitih kutova; interpolirana vrijednost ostaje procjena između mjerenja.

**Zašto baš takve nesigurnosti?** Za nastavni račun zadano je $u_m=0{,}00020$ (oko 1,7 % referentnog otpora), $u_n=0{,}00010$ (oko 0,8 % CFD otpora) i $u_v=0{,}00010$. To su obrazloženi odabiri reda veličine, a ne utvrđene nesigurnosti stvarnog pokusa ili rješavača. Lokalni nagib mjerne krivulje iznosi približno $0{,}000891$ po stupnju: preostala nesigurnost kuta reda $0{,}1^\circ$ proizvela bi doprinos oko $0{,}00009$, što motivira red veličine $u_v$ za usklađivanje uvjeta i interpolaciju. Ladsonove razlike ponovljenih mjerenja blizu nultoga kuta ne pretvaramo u dokaz standardne nesigurnosti pri $10^\circ$.

Numerička nesigurnost $u_n$ ovdje je ukupna pretpostavka, koja uključuje diskretizaciju i iteracijske učinke. GCI nije automatski standardna nesigurnost; ne pribraja se ponovno tom doprinosu. Za neovisne standardne doprinose scenarija zbrajaju se varijance. Faktor $k=2$ daje približno 95 % pokrivanja uz pretpostavljenu normalnu raspodjelu i poznate standardne nesigurnosti. Kriterij $|E|\le U_E$ ispituje slaganje na jednoj radnoj točki; nije dokaz prikladnosti modela za svaki inženjerski zahtjev. Promjena $u_m$ s $0{,}00020$ na $0{,}00030$ u Z6 pokazuje osjetljivost odluke bez promjene samog CFD rezultata. Sve pretpostavke sačuvane su u `teaching_comparison.json` uz podatkovni paket.

::: {.mf1-granica-modela}
<p class="mf1-box-label">Aeroprofil nije automatski hidroprofil</p>

Bezdimenzijski koeficijenti profilnog uzgona i otpora prenose istu osnovnu bilancu, ali NACA 0012 pokus u zraku ne validira slobodnu površinu, kavitaciju, hrapavost ni učinke svojstava vode. Za takvu odluku potreban je zaseban vodeni eksperiment s odgovarajućim $Re$, kavitacijskim i, prema potrebi, Froudeovim brojem.
:::

## Što čitati dalje

Sljedeći izvori su klasični uvodi u numeričku mehaniku fluida i CFD. Nisu preduvjet za kolegij Mehanika fluida 1, nego izvori za daljnje učenje.

- **Versteeg, H. K., Malalasekera, W.** — *An Introduction to Computational Fluid Dynamics: The Finite Volume Method*. Pearson. Klasičan udžbenik FVM-a.
- **Ferziger, J. H., Perić, M., Street, R. L.** — *Computational Methods for Fluid Dynamics*. Springer. Referentni udžbenik numeričkih metoda.
- **Anderson, J. D.** — *Computational Fluid Dynamics: The Basics with Applications*. McGraw-Hill. Pristupačan uvod.
- **OpenFOAM User Guide** — službena dokumentacija koju treba čitati za konkretnu instaliranu inačicu.
- **CFD-Online wiki** — zajednička baza znanja s detaljnim opisima turbulentnih modela, rubnih uvjeta i alata.

::: {.callout-note icon="false"}
## Sažetak

Mehanika fluida 1 daje **fizikalni jezik**: tlak, brzina, gustoća, kontinuitet, Bernoulli, količina gibanja. Računalna dinamika fluida daje **računalni alat** za približno rješavanje pripadnih jednadžbi na diskretnoj mreži. Fizikalni model i numerički postupak zato treba provjeravati zasebno.

Pri prvim CFD simulacijama mnogo rada zahtijevaju mreže, rubni uvjeti i konvergencija. Temeljne bilance uvedene u ovom udžbeniku ostaju oslonac, dok dodatni modeli i numerički postupci traže zasebno učenje.
:::
