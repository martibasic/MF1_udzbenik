## Mehanika fluida i numerika — pregled

Ovaj dodatak nije gradivo Mehanike fluida 1 niti je uvod u računalnu dinamiku fluida. On služi kao **mostovni pregled** — sažima sve numeričke pojmove iz „Numeričkih tragova" i „Numeričkih mostova" u poglavljima pog. 1–13 i postavlja ih u jednu cjelinu.

Cilj nije osposobljavanje za pokretanje CFD simulacije. Cilj je da se u kasnijim kolegijima posvećenima **računalnoj dinamici fluida** prepoznaju pojmovi i odmah jasno vidi *gdje* je svaka jednadžba iz MF1 sjela u toj disciplini.

::: {.callout-tip icon="false"}
## Što se ovdje neće dogoditi

- **Neće biti diskretizacije** — nema upwind, central differencing, ni rješavanja sustava.
- **Neće biti koda** — nema OpenFOAM kontrolnih datoteka ni Python skripti.
- **Neće biti formula s indeksima ćelija** — sve ostaje na konceptualnoj razini.

To je gradivo posebnih kolegija.
:::

## Pojmovnik numeričkih metoda

Sljedeća tablica objedinjuje numeričke metode i alate spomenute kroz udžbenik, s pokazateljem na poglavlje gdje se prvi put pojavljuju.

| Kratica | Puno ime | Što radi | Gdje se pojavila u MF1 |
|---|---|---|---|
| **CFD** | Computational Fluid Dynamics | Računalno rješavanje Navier-Stokesovih jednadžbi | Svuda — kao šira disciplina |
| **FVM** | Finite Volume Method | Domena se rastavlja na kontrolne volumene; bilanca mase i KG po svakoj ćeliji | pog. 8 (kontinuitet), pog. 11 (KG) |
| **FEM** | Finite Element Method | Domena se rastavlja na elemente; rješava se varijacijski oblik PDJ | Strukturno-fluidne interakcije |
| **VOF** | Volume of Fluid | Praćenje slobodne površine preko polja $\alpha \in [0,1]$ | pog. 2 (kapilarnost), pog. 7 (uzgon) |
| **CSF** | Continuum Surface Force | Površinska napetost kao volumna sila u VOF-u | pog. 2 |
| **DNS** | Direct Numerical Simulation | Rješava sve, čak i najmanje vrtloge — najtočnije i najskuplje | pog. 10 (gubici, turbulencija) |
| **LES** | Large Eddy Simulation | Rješava velike vrtloge, modelira male | pog. 10 |
| **RANS** | Reynolds-Averaged Navier-Stokes | Računa srednje polje, modelira sve turbulentne fluktuacije | pog. 10, pog. 13 |
| **k-ε** / **k-ω SST** | turbulentni modeli | Dvije dodatne jednadžbe za turbulentnu energiju i disipaciju | pog. 10 (gubici), pog. 13 (cjevovodi) |
| **SIMPLE** / **PISO** / **PIMPLE** | algoritmi sprege $p$–$v$ | Iterativno usklađivanje tlaka i brzine da $\nabla\cdot\vec{v}=0$ | pog. 1 (Pascal), pog. 8 (kontinuitet) |
| **MRF** | Multiple Reference Frame (više referentnih okvira) | Rotacijske domene (pumpe, turbine) bez fizičke rotacije mreže | pog. 4 (relativno mirovanje), pog. 12 (lopatice) |
| **Klizajuća mreža** *(engl. sliding mesh)* | rotor i stator s međusobnim klizanjem | Rotor i stator fizički kližu jedan uz drugi | pog. 12 |
| **Zidne funkcije** *(engl. wall functions)* | analitička premosnica uz zid | Premošćuju grube zidne ćelije analitičkim turbulentnim profilom | pog. 13 |
| **y+** | $y^+$ kriterij | Bezdimenzijska udaljenost prve ćelije od zida; kontrolira rezoluciju graničnog sloja | pog. 13 |
| **Panel metoda** | Panel Method | Potencijalno strujanje + granični sloj na vanjskim oblicima | (vanjska aerodinamika) |

## Pregled alata

Sljedeći alati su industrijski standard i otvorene platforme spomenute u udžbeniku.

| Alat | Vrsta | Licenca | Tipično se koristi za |
|---|---|---|---|
| **OpenFOAM** | FVM CFD okvir | otvorena (GPL) | Akademija, istraživanje, prilagodljivi industrijski projekti |
| **ANSYS Fluent** | FVM CFD paket | komercijalna | Industrijski opći CFD: automobilska industrija, energetika, HVAC |
| **Star-CCM+ (Simcenter)** | FVM CFD paket | komercijalna | Automobilska industrija, brodogradnja, multifazno strujanje |
| **COMSOL Multiphysics** | FEM multifizika | komercijalna | Multifizika: interakcija fluida i konstrukcije, akustika, elektromagnetizam i fluidi |
| **SU2** | FVM CFD okvir | otvorena | Aeronautika, optimizacija oblika (adjoint metoda) |
| **AFT Fathom** / **Pipe-Flo** | 1D cjevovodne mreže | komercijalna | Inženjerski cjevovodni sustavi (industrija, vodoopskrba) |
| **EPANET** | 1D vodoopskrbne mreže | otvorena | Distributivne mreže vode |
| **ParaView** | post-procesor / vizualizacija | otvorena | Vizualizacija polja, integracije po plohama, animacije |

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
| Reynoldsov broj | Bezdimenzijski kriterij izbora turbulentnog modela |
| Froudeov, Weberov, Machov broj (pog. 14) | Skaliranje slobodne površine (VOF), raspršivanje, granica stlačivosti |
| Bezdimenzioniranje jednadžbi, Π teorem (pog. 14) | Bezdimenzionirane Navier-Stokesove jednadžbe; $Re$ kao jedini parametar nestlačivog toka |
| Moodyjev dijagram i koeficijent $\lambda$ | Zidne funkcije (`wallFunctions`) u RANS modelu |
| Bernoullijeva jednadžba (validacija) | Probna linija (`sampleDict`) duž strujnice |
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
| Bernoullijeva jednadžba | Validacija CFD-a; Euler solveri |
| Eulerova diferencijalna jednadžba | Euler solver za neviskozno strujanje |
| Disipacija, $h_l = \lambda(L/D)(v^2/2g)$ | Turbulentni modeli $k$-$\varepsilon$, $k$-$\omega$ SST; zidne funkcije |
| Integralni zakon količine gibanja | **Srce svakog CFD solvera** — FVM |
| Moment količine gibanja, $\vec{w} = \vec{c} - \vec{u}$ | MRF metoda, klizajuća mreža (sliding mesh) za rotore |
| Reynoldsov broj $Re = vD/\nu$ | Izbor turbulentnog modela, $y^+$ kriterij |
| Bezdimenzijski brojevi $Re, Fr, We, Ma$ (pog. 14) | Bezdimenzionirane jednadžbe; ulazni parametri i kriteriji izbora modela |

## Kada CFD ne treba: granice primjenjivosti

Računalna dinamika fluida nije univerzalno sredstvo. U svakom inženjerskom projektu prvo se postavlja pitanje **može li se problem riješiti analitički ili tabličnim podacima** — tek ako odgovor nije zadovoljavajući, primjenjuje se CFD. Sljedeći su tipični slučajevi u kojima CFD ne donosi vrijednost iznad ručnog proračuna:

::: {.mf1-warning}
<p class="mf1-box-label">Slučajevi u kojima analitika dostaje</p>

- **Pascalov prijenos sile u hidrauličnim sustavima** — analitičke formule $\Delta p = F/A$ i $A_1 s_1 = A_2 s_2$ daju cjelovit odgovor; CFD bi numerički reproducirao isti rezultat uz mnogo veći trošak.
- **Hidrostatika u mirnim spremnicima** — $p = p_0 + \rho g h$ vrijedi egzaktno; CFD donosi vrijednost tek pri dinamičkim uvjetima poput zapljuskivanja ili prelijevanja.
- **Sila na ravnu plohu pri poznatoj hidrostatici** — integral $F = \rho g z_T A$ je egzaktan za stacionarni slučaj; CFD je potreban tek pri valovima ili turbulentnoj struji uz plohu.
- **1D proračun cjevovoda u stacionarnom režimu** — Darcy-Weisbach uz tablične koeficijente $\xi$ daje rješenje s pogreškom $5{-}15\%$ u djeliću sekunde; 3D CFD vrijedi tek za detaljnu analizu pojedinih kritičnih elemenata.
- **Statička stabilnost broda u mirnoj vodi** — metacentarska teorija ($\overline{GM}$) daje točan kriterij; CFD je potreban tek pri valnoj eksitaciji ili nesimetričnom poplavljenju trupa.
:::

Pravilo prakse: **CFD se uvodi tek kad ručni proračun ne razrešava prostornu raspodjelu ili dinamiku**. Za sve drugo analitika je brža, jeftinija i jednako pouzdana.

## Orijentacijski troškovi CFD simulacije

Veliki dio inženjerskog odabira CFD pristupa ovisi o vremenu i opremi koju simulacija zahtijeva. Sljedeća tablica daje grube redove veličine koji pomažu u procjeni je li određena vrsta analize uopće izvediva u zadanom roku:

| Vrsta analize | Tipično vrijeme | Tipična oprema | Tipičan problem |
|---|---|---|---|
| 1D mrežni alat (EPANET, AFT Fathom) | sekunde – minute | običan laptop | Cijela vodoopskrbna mreža grada ili procesni sustav |
| 2D Euler ili stacionarni RANS | minute – sati | radna stanica | Predprojektna procjena profila krila ili lopatice |
| 3D stacionarni RANS, $\sim 10^6$ ćelija | sati – dan | radna stanica | Crpka, koljeno, vanjska aerodinamika automobila |
| 3D stacionarni RANS, $\sim 10^7$ ćelija | dan – tjedan | klaster | Detalj brodskog trupa s lokalnim profilom granične razine |
| 3D nestacionarni RANS ili LES | tjedan – mjesec | klaster | Aeroakustika, izgaranje, valni udar, rotor-stator interakcija |
| DNS | mjesec – godina | superkompjuter | Istraživanje turbulencije u kanalu pri umjerenom $Re$ |

Pravilo prakse: za studente koji prvi put pokreću CFD, **prvih nekoliko tjedana ide u laminarnim ili jednostavnim 2D problemima** koji konvergiraju u minutama; tek kad je radni tijek u alatu postao rutina, prelazi se na turbulentne 3D simulacije.

## Tipičan CFD tijek na primjeru iz MF1: Venturijeva cijev

Kako bi se konkretno vidjelo što sve CFD analiza obuhvaća, pokazat će se uobičajenih pet koraka na primjeru za koji su studenti već vidjeli analitičko rješenje u poglavlju <span class="mf1-ch-ref"><span class="mf1-ch-code">pog. 9</span><span class="mf1-ch-title">Bernoullijeva jednadžba idealnog fluida</span></span> — na Venturijevoj cijevi.

### Korak 1 — Geometrija

Iz CAD modela ili izravno u alatu konstruira se trodimenzijska geometrija cijevi sa suženjem. Za simetrične probleme često je dovoljna polovica geometrije s ravninom simetrije, što prepolavlja troškove simulacije. Ulazni presjek, izlazni presjek, ravnina simetrije i unutarnji zid cijevi označavaju se kao zasebne patcheve.

### Korak 2 — Mreža

Geometrija se diskretizira u mrežu kontrolnih volumena. Ključne odluke:

- **Gustoća mreže** — gušće u suženju gdje gradijenti brzine i tlaka rastu;
- **Sloj uz zid** — prizmatski elementi uz zid radi razrešavanja graničnog sloja;
- **$y^+$ vrijednost** — za $k$-$\omega$ SST model ciljano $y^+ \approx 1$ s razrešenim slojem ili $y^+ \approx 30$ uz zidne funkcije.

Za jednostavnu Venturijevu cijev dovoljno je oko $10^5$ ćelija.

### Korak 3 — Rubni uvjeti

Svakoj plohi geometrije pridružuje se odgovarajući uvjet:

- **Ulaz** — zadan volumenski protok ili profil brzine (`fixedValue`);
- **Izlaz** — zadan tlak (`fixedValue` ili `totalPressure`);
- **Zid** — uvjet ljepljivosti `noSlip` na unutarnjoj plohi cijevi;
- **Ravnina simetrije** (ako se koristi) — uvjet `symmetry`.

Pravilan izbor rubnih uvjeta najčešći je izvor pogrešaka kod prvih CFD simulacija.

### Korak 4 — Solver i konvergencija

Za nestlačivi stacionarni problem bira se `simpleFoam` (OpenFOAM) ili *Pressure-Based Steady-State Solver* (Fluent). Solver iterativno usklađuje polje brzine i tlaka algoritmom SIMPLE; svaki iterativni korak smanjuje rezidualne pogreške. Tipično se traži pad reziduala za $3{-}5$ redova veličine, uz potvrdu da se globalne veličine (protok, sila, pad tlaka) više ne mijenjaju među iteracijama.

### Korak 5 — Validacija ručnim računom

**Ovo je korak koji se ne smije preskočiti.** Iz simulacije se očita pad tlaka $\Delta p_{CFD}$ između ulaznog i izlaznog presjeka; ručno se izračuna $\Delta p_{Bernoulli} = (\rho/2)(v_2^2 - v_1^2)$ iz kontinuiteta i ulaznog protoka. Razlika mora biti unutar $5{-}10\%$ za nestlačivi, niskoviskozni tok. Ako odstupa više, problem je u mreži, rubnim uvjetima ili konvergenciji — ne u Bernoullijevoj jednadžbi.

Tek nakon validacije rezultati simulacije postaju dostatan temelj za projektnu odluku.

## Što čitati dalje

Sljedeći izvori su klasični uvodi u numeričku mehaniku fluida i CFD. Nije ih potrebno čitati prije RDF kolegija, ali su dobri za usmjerenje.

- **Versteeg, H. K., Malalasekera, W.** — *An Introduction to Computational Fluid Dynamics: The Finite Volume Method*. Pearson. Klasičan udžbenik FVM-a.
- **Ferziger, J. H., Perić, M., Street, R. L.** — *Computational Methods for Fluid Dynamics*. Springer. Standardna referenca, hrvatski autor.
- **Anderson, J. D.** — *Computational Fluid Dynamics: The Basics with Applications*. McGraw-Hill. Pristupačan uvod.
- **OpenFOAM User Guide** — službena dokumentacija (otvorena, besplatna). Najbolji praktični uvod u otvoreni FVM solver.
- **CFD-Online wiki** — zajednička baza znanja s detaljnim opisima turbulentnih modela, rubnih uvjeta i alata.

::: {.callout-note icon="false"}
## Sažetak

Mehanika fluida 1 daje **fizikalni jezik**: tlak, brzina, gustoća, kontinuitet, Bernoulli, količina gibanja. Računalna dinamika fluida daje **računalni alat** koji taj jezik rješava na milijunima točaka istovremeno. Numerika nije zamjena za fiziku, niti je viša razina iste discipline — to je drugi rakurs istog problema.

Pri prvim CFD simulacijama prvih nekoliko tjedana protječe u radu s mrežama, rubnim uvjetima i konvergencijom. No svaka jednadžba koja se tamo pojavi — već je upoznata ovdje.
:::
