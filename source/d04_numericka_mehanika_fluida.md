## Mehanika fluida i numerika — pregled

Ovaj dodatak nije gradivo Mehanike fluida 1 niti je uvod u Računalnu dinamiku fluida. On služi kao **mostovni pregled** — sažima sve numeričke pojmove na koje si nailazio kroz „🖥️ Numeričke tragove" i „🖥️ Numeričke mostove" u poglavljima U01–U13, i postavlja ih u jednu cjelinu.

Cilj nije da znaš pokrenuti CFD simulaciju nakon ovog dodatka. Cilj je da, kad u trećoj godini upišeš kolegij **Računalna dinamika fluida**, prepoznaš pojmove i imaš dojam *gdje* je svaka jednadžba iz MF1 sjela u toj disciplini.

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
| **FVM** | Finite Volume Method | Domena se rastavlja na kontrolne volumene; bilanca mase i KG po svakoj ćeliji | U08 (kontinuitet), U11 (KG) |
| **FEM** | Finite Element Method | Domena se rastavlja na elemente; rješava se varijacijski oblik PDJ | Strukturno-fluidne interakcije |
| **VOF** | Volume of Fluid | Praćenje slobodne površine preko polja $\alpha \in [0,1]$ | U02 (kapilarnost), U07 (uzgon) |
| **CSF** | Continuum Surface Force | Površinska napetost kao volumna sila u VOF-u | U02 |
| **DNS** | Direct Numerical Simulation | Rješava sve, čak i najmanje vrtloge — najtočnije i najskuplje | U10 (gubici, turbulencija) |
| **LES** | Large Eddy Simulation | Rješava velike vrtloge, modelira male | U10 |
| **RANS** | Reynolds-Averaged Navier-Stokes | Računa srednje polje, modelira sve turbulentne fluktuacije | U10, U13 |
| **k-ε** / **k-ω SST** | turbulentni modeli | Dvije dodatne jednadžbe za turbulentnu energiju i disipaciju | U10 (gubici), U13 (cjevovodi) |
| **SIMPLE** / **PISO** / **PIMPLE** | algoritmi sprege $p$–$v$ | Iterativno usklađivanje tlaka i brzine da $\nabla\cdot\vec{v}=0$ | U01 (Pascal), U08 (kontinuitet) |
| **MRF** | Multiple Reference Frame | Rotacijske domene (pumpe, turbine) bez fizičke rotacije mreže | U04 (relativno mirovanje), U12 (lopatice) |
| **Sliding mesh** | klizajuća mreža | Rotor i stator fizički kližu jedan uz drugi | U12 |
| **Wall functions** | zidne funkcije | Premošćuju grube zidne ćelije s analitičkim turbulentnim profilom | U13 |
| **y+** | $y^+$ kriterij | Bezdimenzijska udaljenost prve ćelije od zida; kontrolira rezoluciju graničnog sloja | U13 |
| **Panel metoda** | Panel Method | Potencijalno strujanje + granični sloj na vanjskim oblicima | (vanjska aerodinamika) |

## Pregled alata

Sljedeći alati su industrijski standard i otvorene platforme spomenute u udžbeniku.

| Alat | Vrsta | Licenca | Tipično se koristi za |
|---|---|---|---|
| **OpenFOAM** | FVM CFD framework | otvorena (GPL) | Akademija, istraživanje, prilagodljivi industrijski projekti |
| **ANSYS Fluent** | FVM CFD paket | komercijalna | Industrijski opći CFD: automotive, energetika, HVAC |
| **Star-CCM+ (Simcenter)** | FVM CFD paket | komercijalna | Automotive, marine, multifazno |
| **COMSOL Multiphysics** | FEM multiphysics | komercijalna | Multifizika: FSI, akustika, elektromagnetizam + fluidi |
| **SU2** | FVM CFD framework | otvorena | Aerospace, optimizacija oblika (adjoint metoda) |
| **AFT Fathom** / **Pipe-Flo** | 1D cjevovodne mreže | komercijalna | Inženjerski cjevovodni sustavi (industrija, vodoopskrba) |
| **EPANET** | 1D vodoopskrbne mreže | otvorena | Distributivne mreže vode |
| **ParaView** | post-procesor / vizualizacija | otvorena | Vizualizacija polja, integracije po plohama, animacije |

## Kako se MF1 jednadžbe slažu u CFD slici

Ova tablica sažima glavne jednadžbe iz udžbenika i pokazuje njihovu izravnu ulogu u CFD-u.

| MF1 jednadžba / koncept | Numerička uloga |
|---|---|
| $p = F_n/A$, Pascalov zakon | Tlak kao polje; inicijalni uvjet tlaka |
| $dp/dz = -\rho g$, $p = p_0 + \rho gh$ | Inicijalni uvjet i baseline (polje `p_rgh`) |
| $\tau = \mu\,dv/dy$ | Konstitutivni zakon u solveru (Newtonian model) |
| Površinska napetost $\sigma$, kontaktni kut | VOF + CSF za multifazno strujanje |
| $F_U = \rho g V_{ist}$ (uzgon) | VOF metoda; `interFoam` solver |
| Integracija tlaka $F = \int_A p\,dA$ | Funkcionalni objekti `forces`, *Force Reports* |
| $\nabla\cdot\vec{v} = 0$ (kontinuitet) | Pressure-velocity coupling (SIMPLE/PISO/PIMPLE) |
| Bernoullijeva jednadžba | Validacija CFD-a; Euler solveri |
| Eulerova diferencijalna jednadžba | Euler solver za neviskozno strujanje |
| Disipacija, $h_l = \lambda(L/D)(v^2/2g)$ | Turbulentni modeli k-ε, k-ω SST; wall functions |
| Integralni zakon količine gibanja | **Srce svakog CFD solvera** — FVM |
| Moment količine gibanja, $\vec{w} = \vec{c} - \vec{u}$ | MRF metoda, sliding mesh za rotore |
| Reynoldsov broj $Re = vD/\nu$ | Izbor turbulentnog modela, $y^+$ kriterij |

## Što čitati dalje

Sljedeći izvori su klasični uvodi u numeričku mehaniku fluida i CFD. Nije ih potrebno čitati prije RDF kolegija, ali su dobri za usmjerenje.

- **Versteeg, H. K., Malalasekera, W.** — *An Introduction to Computational Fluid Dynamics: The Finite Volume Method*. Pearson. Klasičan udžbenik FVM-a.
- **Ferziger, J. H., Perić, M., Street, R. L.** — *Computational Methods for Fluid Dynamics*. Springer. Standardna referenca, hrvatski autor.
- **Anderson, J. D.** — *Computational Fluid Dynamics: The Basics with Applications*. McGraw-Hill. Pristupačan uvod.
- **OpenFOAM User Guide** — službena dokumentacija (otvorena, besplatna). Najbolji praktični uvod u otvoreni FVM solver.
- **CFD-Online wiki** — zajednička baza znanja s detaljnim opisima turbulentnih modela, rubnih uvjeta i alata.

::: {.callout-note icon="false"}
## Sažetak

Mehanika fluida 1 daje ti **fizikalni jezik**: tlak, brzina, gustoća, kontinuitet, Bernoulli, količina gibanja. Računalna dinamika fluida daje ti **računalni alat** koji taj jezik rješava na milijunima točaka istovremeno. Numerika nije zamjena za fiziku, niti je viša razina iste discipline — to je drugi rakurs istog problema.

Kad u trećoj godini počneš pokretati CFD simulaciju, prvih nekoliko tjedana ćeš se nositi s mrežama, rubnim uvjetima i konvergencijom. Ali svaka jednadžba koju ćeš tamo vidjeti — već si je upoznao ovdje.
:::
