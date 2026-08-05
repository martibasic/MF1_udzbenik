## Mehanika fluida i numerika — pregled

Ovaj dodatak nije samostalan uvod u računalnu dinamiku fluida. On služi kao **mostovni pregled**: sažima numeričke pojmove iz poglavlja 1–15 i uvodi minimalni jezik kojim se rezultat simulacije provjerava prije inženjerske uporabe.

Cilj nije osposobiti čitatelja za pokretanje CFD simulacije, nego pokazati gdje jednadžbe MF1 ulaze u numerički model i zašto slika obojenog polja još nije dokaz točnosti.

::: {.callout-tip icon="false"}
## Što se ovdje neće dogoditi

- **Neće biti izvoda diskretizacijskih shema** — nema formula po ćelijama ni rješavanja linearnih sustava.
- **Neće biti koda** — nema OpenFOAM kontrolnih datoteka ni Python skripti.
- **Bit će osnovne provjere rezultata** — bilanca mase, iteracijska konvergencija, usporedba mreža te razlika između verifikacije i validacije.

To je gradivo posebnih kolegija.
:::

## Pojmovnik numeričkih metoda

Sljedeća tablica objedinjuje numeričke metode i alate spomenute kroz udžbenik, s pokazateljem na poglavlje gdje se prvi put pojavljuju.

| Kratica | Puno ime | Što radi | Gdje se pojavila u MF1 |
|---|---|---|---|
| **CFD** | Computational Fluid Dynamics | Računalno rješavanje Navier-Stokesovih jednadžbi | Svuda — kao šira disciplina |
| **FVM** | Finite Volume Method | Domena se rastavlja na kontrolne volumene; bilanca mase i KG po svakoj ćeliji | pog. 7 (kontinuitet), pog. 10 (KG) |
| **FEM** | Finite Element Method | Domena se rastavlja na elemente; rješava se varijacijski oblik PDJ | Strukturno-fluidne interakcije |
| **VOF** | Volume of Fluid | Praćenje slobodne površine preko polja $\alpha \in [0,1]$ | pog. 2 (kapilarnost), pog. 6 (uzgon), pog. 15 (otvoreni tokovi) |
| **CSF** | Continuum Surface Force | Površinska napetost kao volumna sila u VOF-u | pog. 2 |
| **DNS** | Direct Numerical Simulation | Bez turbulencijskog modela razrješava sve dinamički relevantne skale, uz dovoljno finu mrežu i vremenski korak | pog. 12 (diferencijalni opis i turbulencija) |
| **LES** | Large Eddy Simulation | Rješava velike vrtloge, modelira male | pog. 12 |
| **RANS** | Reynolds-Averaged Navier-Stokes | Računa osrednjeno polje i modelira učinak nerazrijeđenih turbulentnih fluktuacija | pog. 12, pog. 13 |
| **k-ε** / **k-ω SST** | turbulentni modeli | Dodatne transportne jednadžbe za veličine kojima se zatvara učinak turbulencije | pog. 12, pog. 13 |
| **SIMPLE** / **PISO** / **PIMPLE** | algoritmi sprege $p$–$v$ | Iterativno usklađivanje tlaka i brzine da $\nabla\cdot\vec{v}=0$ | pog. 7 (kontinuitet) |
| **MRF** | Multiple Reference Frame (više referentnih okvira) | Rotacijske domene (pumpe, turbine) bez fizičke rotacije mreže | pog. 4 (rotirajući okvir), pog. 14 (turbostrojevi) |
| **Klizajuća mreža** *(engl. sliding mesh)* | rotor i stator s međusobnim klizanjem | Rotor i stator fizički kližu jedan uz drugi | pog. 14 |
| **Zidne funkcije** *(engl. wall functions)* | modelska veza između prve ćelije i stijenke | Zatvaraju područje uz zid kada mreža ne razlučuje cijeli viskozni podsloj | pog. 12, pog. 13 |
| **y+** | $y^+$ kriterij | Bezdimenzijska udaljenost prve ćelije od zida; jedan od kriterija prikladnosti zidne rezolucije | pog. 12, pog. 13 |
| **Panel metoda** | Panel Method | Potencijalno strujanje + granični sloj na vanjskim oblicima | (vanjska aerodinamika) |

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
| Granica kontrolnog volumena | Patch (`boundaryField` u OpenFOAM-u, *Named Selection* u Fluentu) |
| Rubni uvjet na skici (strelica, hvatišna točka) | Postavka tipa `inlet`, `outlet`, `wall`, `symmetry` na patchu |
| Pretpostavka nestlačivosti | Izbor nestlačivog solvera (`simpleFoam`, `pisoFoam`) |
| Slobodna površina | Iso-ploha polja $\alpha = 0{,}5$ u VOF simulaciji |
| Težište istisnutog volumena (centar uzgona) | Integracija polja $\alpha$ po cijeloj domeni |
| Hidrostatska raspodjela tlaka | Polje `p_rgh` (tlak umanjen za hidrostatski dio) |
| Profil brzine $v(r)$ u cijevi | Polje `U` kao funkcija položaja (uzorkovanje po liniji s alatom `sample`) |
| Sila na zid | Funkcijski objekt `forces` ili `forceCoeffs` |
| Centar tlaka na plohi | Težište raspodjele tlaka po zidnom patchu |
| Reynoldsov broj | Jedan od kriterija za procjenu režima, razlučivosti i izbora modela; nije dovoljan sam |
| Froudeov, Weberov i Machov broj (pog. 9, 11 i 15) | Skaliranje stlačivosti, međupovršinskih pojava i slobodne površine |
| Bezdimenzioniranje jednadžbi, Π teorem (pog. 11) | Popis mjerodavnih parametara modela; samo u najjednostavnijem jednofaznom nestlačivom toku može ostati prvenstveno $Re$ |
| Moodyjev dijagram i koeficijent $\lambda$ | Neovisna 1D referenca za ukupni otpor cijevi; zidne funkcije su zaseban način zatvaranja toka uz zid u RANS-u |
| Bernoullijeva jednadžba (referentno rješenje idealnog modela) | Probna linija (`sampleDict`) duž strujnice; verifikacijska usporedba istih presjeka |
| Mlaz koji udara o plohu (sila) | Zidni patch s integracijom tlaka i smičnih naprezanja |
| Pokretna lopatica | MRF zona (`MRFZone`) ili klizajuća mreža |
| Trokuti brzina | Polja apsolutne i relativne brzine ($\vec{c} = \vec{w} + \vec{u}$) u MRF zoni |
| Linijski gubici | Integral disipacije po dionici domene |
| Lokalni gubici | Razrešavanje strujanja na geometrijskim singularitetima (koljeno, ventil) |
| Metacentar | 6-DOF rješavač gibanja u VOF simulaciji s brodskim trupom |

## Kako se MF1 jednadžbe slažu u CFD slici

Ova tablica sažima glavne jednadžbe iz udžbenika i pokazuje njihovu izravnu ulogu u CFD-u.

| MF1 jednadžba / koncept | Numerička uloga |
|---|---|
| $p = F_n/A$, Pascalov zakon | Tlak kao polje; inicijalni uvjet tlaka |
| $dp/dz = -\rho g$, $p = p_0 + \rho gh$ | Inicijalni uvjet i temeljna razina polja `p_rgh` |
| $\tau = \mu\,dv/dy$ | Konstitutivni zakon u solveru (Newtonian model) |
| Površinska napetost $\sigma$, kontaktni kut | VOF + CSF za multifazno strujanje |
| $F_U = \rho g V_{ist}$ (uzgon) | VOF metoda; `interFoam` solver |
| Integracija tlaka $F = \int_A p\,dA$ | Funkcionalni objekti `forces`, *Force Reports* |
| $\nabla\cdot\vec{v} = 0$ (kontinuitet) | Sprega tlaka i brzine (SIMPLE/PISO/PIMPLE) |
| Bernoullijeva jednadžba | Referentno rješenje za verifikaciju idealiziranoga Eulerova modela |
| Eulerova diferencijalna jednadžba | Euler solver za neviskozno strujanje |
| Disipacija, $h_l = \lambda(L/D)(v^2/2g)$ | Pad mehaničke energije iz polja tlaka i brzine; turbulentni model i zidna obrada utječu na predviđeni otpor |
| Integralni zakon količine gibanja | Izravna polazna formulacija metode konačnih volumena (FVM) |
| Moment količine gibanja, $\vec{w} = \vec{c} - \vec{u}$ | MRF metoda, klizajuća mreža (sliding mesh) za rotore |
| Reynoldsov broj $Re = vD/\nu$ | Procjena relativne važnosti viskoznosti; jedan od ulaza u odabir modela i mreže |
| Bezdimenzijski brojevi $Re, Fr, We, Ma$ (pog. 9, 11 i 15) | Bezdimenzionirane jednadžbe; ulazni parametri i kriteriji izbora modela |

## Kada CFD ne treba: granice primjenjivosti

Računalna dinamika fluida nije univerzalno sredstvo. U svakom inženjerskom projektu prvo se postavlja pitanje **može li se problem riješiti analitički ili tabličnim podacima** — tek ako odgovor nije zadovoljavajući, primjenjuje se CFD. Sljedeći su tipični slučajevi u kojima CFD ne donosi vrijednost iznad ručnog proračuna:

::: {.mf1-warning}
<p class="mf1-box-label">Slučajevi u kojima analitika dostaje</p>

- **Pascalov prijenos sile u hidrauličnim sustavima** — analitičke formule $\Delta p = F/A$ i $A_1 s_1 = A_2 s_2$ daju cjelovit odgovor; CFD bi numerički reproducirao isti rezultat uz mnogo veći trošak.
- **Hidrostatika u mirnim spremnicima** — $p = p_0 + \rho g h$ vrijedi egzaktno; CFD donosi vrijednost tek pri dinamičkim uvjetima poput zapljuskivanja ili prelijevanja.
- **Sila na ravnu plohu pri poznatoj hidrostatici** — integral $F = \rho g z_T A$ je egzaktan za stacionarni slučaj; CFD je potreban tek pri valovima ili turbulentnoj struji uz plohu.
- **1D proračun cjevovoda u stacionarnom režimu** — Darcy–Weisbach uz dokumentirane koeficijente često daje odgovor primjeren projektnoj odluci. Nesigurnost nije univerzalnih $5{-}15\,\%$, nego ovisi o podatcima o hrapavosti, lokalnim elementima, režimu i mjerenju protoka.
- **Početna statička stabilnost broda u mirnoj vodi** — metacentarska teorija daje mali-kutni kriterij početne stabilnosti. Konačni kutovi, valna eksitacija, slobodne površine i poplavljivanje traže širi hidrostatički ili hidrodinamički model.
:::

Pravilo prakse: najprije se bira najjednostavniji model koji odgovara odluci i potrebnoj nesigurnosti. CFD donosi vrijednost kada su prostorna raspodjela, složena geometrija ili nestacionarnost bitne, ali i tada 1D račun ostaje važna neovisna provjera reda veličine.

## Kako procijeniti računski trošak

Vrijeme izvođenja nije svojstvo samoga naziva metode. Ovisi barem o broju ćelija i jednadžbi, broju vremenskih koraka, nelinearnoj konvergenciji, hardveru, paralelizaciji, spremanju izlaza i broju varijanti. Zato se bez definiranoga slučaja ne navodi univerzalna pretvorba „vrsta modela → sati računanja”.

Za nastavni i projektni rad koristan je redoslijed:

1. započeti najjednostavnijim modelom koji može odgovoriti na ciljano pitanje;
2. procijeniti trošak kratkim probnim izvođenjem na gruboj mreži, bez zaključivanja o konačnom rezultatu;
3. planirati najmanje tri sustavno profinjene mreže i, za nestacionarni slučaj, provjeru vremenskoga koraka;
4. tek nakon zatvaranja bilanci i monitora dodavati složeniju geometriju ili fizikalni model.

Laminarni referentni slučaj s poznatim rješenjem zato je bolji prvi korak od složene turbulentne simulacije: istodobno provjerava postavke, mrežu, bilance i način izvještavanja pogreške.

## Tipičan CFD tijek na primjeru iz MF1: Venturijeva cijev

Kako bi se konkretno vidjelo što sve CFD analiza obuhvaća, prikazuje se šest koraka na Venturijevoj cijevi. Presjeci usporedbe moraju biti unaprijed definirani: presjek 1 u razvijenom ulaznom toku i presjek 2 u grlu.

### Korak 1 — Geometrija

Iz CAD modela ili izravno u alatu konstruira se trodimenzijska geometrija cijevi sa suženjem. Za simetrične probleme često je dovoljna polovica geometrije s ravninom simetrije, što prepolavlja troškove simulacije. Ulazni presjek, izlazni presjek, ravnina simetrije i unutarnji zid cijevi označavaju se kao zasebne patcheve.

### Korak 2 — Mreža

Geometrija se diskretizira u mrežu kontrolnih volumena. Ključne odluke:

- **Gustoća mreže** — gušće u suženju gdje gradijenti brzine i tlaka rastu;
- **Sloj uz zid** — prizmatski elementi uz zid radi razrešavanja graničnog sloja;
- **$y^+$ vrijednost** — cilj mora odgovarati odabranoj zidnoj obradi; razriješeni sloj i zidne funkcije imaju različite zahtjeve, a prijelazno područje treba izbjegavati prema dokumentaciji konkretnog modela.

Broj ćelija sam po sebi nije kriterij dostatnosti. Potrebna je najmanje gruba, srednja i fina mreža s usporedivim obrascem profinjenja, a mjerodavne izlazne veličine moraju pokazati konvergenciju.

### Korak 3 — Rubni uvjeti

Svakoj plohi geometrije pridružuje se odgovarajući uvjet:

- **Ulaz i izlaz** — konzistentan par uvjeta, primjerice zadan profil/protok na ulazu i statički tlak na izlazu; ne smiju se istodobno prepisati međusobno nespojivi protok i tlak;
- **Zid** — klizni zid za idealni Eulerov referentni slučaj ili uvjet ljepljivosti `noSlip` za viskozni model;
- **Ravnina simetrije** (ako se koristi) — uvjet `symmetry`.

Rubni uvjeti moraju odgovarati fizičkom eksperimentu i analitičkom modelu s kojim će se rezultat usporediti.

### Korak 4 — Solver i iteracijska konvergencija

Za nestlačivi stacionarni problem bira se odgovarajući stacionarni solver i sprega tlaka s brzinom. Pad reziduala potreban je, ali nije dovoljan dokaz konvergencije. Istodobno se prate protok kroz svaki otvor, relativna neravnoteža mase, $\Delta p_{12}$, sile i druge izlazne veličine. Kriteriji se zadaju prema namjeni modela; ne postoji univerzalan broj redova veličine koji jamči ispravan rezultat.

### Korak 5 — Verifikacija numeričkog rješenja

**Verifikacija pita: rješavamo li odabrane jednadžbe dovoljno točno?** Najprije se zatvara globalna bilanca mase. Zatim se na najmanje tri sustavno profinjene mreže uspoređuju $\Delta p_{12}$, brzina u grlu i druga projektno važna veličina. Treba izvijestiti relativne promjene među mrežama i, kada je red profinjenja dovoljno uredan, procijeniti diskretizacijsku nesigurnost. Za nestacionarni model analogno se provjerava vremenski korak. Reziduali, bilanca i mrežna/vremenska konvergencija tri su odvojena dokaza.

Za idealni Eulerov slučaj s kliznim zidom dodatna je verifikacijska provjera Bernoullijev rezultat između **ulaza i grla**:

$$
\Delta p_{12,B}=\frac{\rho}{2}\left(v_2^2-v_1^2\right).
$$ {#eq-cfd-vv-korak-5-verifikacija-numerickog-rjesenja-01}

Razlika bi se trebala smanjivati s konvergencijom rješenja. Ne zadaje se unaprijed univerzalna tolerancija od $5$ ili $10\,%$; prihvatljivost ovisi o potrebnoj nesigurnosti projektne odluke.

### Korak 6 — Validacija fizikalnog modela

**Validacija pita: opisuju li odabrane jednadžbe stvarni sustav dovoljno dobro?** Viskozni model s uvjetom ljepljivosti validira se prema mjerenom $\Delta p_{12}$, koeficijentu protoka ili drugom eksperimentalnom podatku pri istim geometrijskim i radnim uvjetima. Mjerna i numerička nesigurnost moraju se prikazati uz usporedbu.

Razlika viskoznog CFD-a prema idealnom Bernoulliju nije automatski pogreška: dio je stvarna disipacija. Posebno, usporedba tlaka između ulaza i izlaza jednake površine s idealnim Bernoullijem dala bi idealno nultu razliku, dok realni tok ima trajan gubitak tlaka. Zato se uvijek uspoređuju iste mjerne stanice i modeli s usklađenim pretpostavkama.

Tek kada su dokumentirane i verifikacija i validacija, rezultat može biti temelj za projektnu odluku unutar navedenog područja primjene.

## Tri pripremljena V&V paketa

Repozitorij sadrži male strojno čitljive pakete u `data/cfd/`. Oni ne zahtijevaju lokalnu instalaciju solvera i služe učenju revizijskog traga: svaka vrijednost ima izvor, jedinicu i ograničenje.

| Paket | Što je stvarno dostupno | Što se smije zaključiti |
|---|---|---|
| [`poiseuille_laminar`](../data/cfd/poiseuille_laminar/README.md) | analitičko rješenje, tri sintetičke mreže, reziduali, monitor protoka, masena bilanca i GCI | provjera V&V postupka prema poznatom rješenju; nije test određenog solvera |
| [`venturi_diffuser`](../data/cfd/venturi_diffuser/README.md) | tri sintetičke mreže, zadani 1D referentni model, reziduali, monitor gubitka, bilanca i GCI | pedagoška verifikacija obrade rezultata; nije eksperimentalna validacija Venturija |
| [`hydrofoil_experiment`](../data/cfd/hydrofoil_experiment/README.md) | Ladsonove javne mjerne sile [@ladson1988] i stvarni FUN3D rezultati NASA TMR-a na tri mreže [@nasa-tmr-naca0012] | usporedba $C_L$ i $C_D$ i mrežni trend; bez arhivskih reziduala, masene bilance i mjernog budžeta nema konačne validacijske presude |

Validator `python tools/validate_cfd_vv.py` ne uspoređuje podatke samo s njima samima: ponovno računa analitičke vrijednosti, bilance, rastav otpora, opaženi red i GCI. Za profilni slučaj dodatno mora prepoznati da $C_D$ monotono konvergira, a $C_L$ na odabrane tri mreže oscilira. Nedostupne arhivske dijagnostike namjerno ostaju označene kao praznina umjesto da se popune umjetnim brojevima.

::: {.mf1-granica-modela}
<p class="mf1-box-label">Aeroprofil nije automatski hidroprofil</p>

Bezdimenzijski koeficijenti profilnog uzgona i otpora prenose istu osnovnu bilancu, ali NACA 0012 pokus u zraku ne validira slobodnu površinu, kavitaciju, hrapavost ni učinke svojstava vode. Za takvu odluku potreban je zaseban vodeni eksperiment s odgovarajućim $Re$, kavitacijskim i, prema potrebi, Froudeovim brojem.
:::

## Što čitati dalje

Sljedeći izvori su klasični uvodi u numeričku mehaniku fluida i CFD. Nije ih potrebno čitati prije RDF kolegija, ali su dobri za usmjerenje.

- **Versteeg, H. K., Malalasekera, W.** — *An Introduction to Computational Fluid Dynamics: The Finite Volume Method*. Pearson. Klasičan udžbenik FVM-a.
- **Ferziger, J. H., Perić, M., Street, R. L.** — *Computational Methods for Fluid Dynamics*. Springer. Standardna referenca, hrvatski autor.
- **Anderson, J. D.** — *Computational Fluid Dynamics: The Basics with Applications*. McGraw-Hill. Pristupačan uvod.
- **OpenFOAM User Guide** — službena dokumentacija koju treba čitati za konkretnu instaliranu inačicu.
- **CFD-Online wiki** — zajednička baza znanja s detaljnim opisima turbulentnih modela, rubnih uvjeta i alata.

::: {.callout-note icon="false"}
## Sažetak

Mehanika fluida 1 daje **fizikalni jezik**: tlak, brzina, gustoća, kontinuitet, Bernoulli, količina gibanja. Računalna dinamika fluida daje **računalni alat** koji taj jezik rješava na milijunima točaka istovremeno. Numerika nije zamjena za fiziku, niti je viša razina iste discipline — to je drugi rakurs istog problema.

Pri prvim CFD simulacijama prvih nekoliko tjedana protječe u radu s mrežama, rubnim uvjetima i konvergencijom. No svaka jednadžba koja se tamo pojavi — već je upoznata ovdje.
:::
