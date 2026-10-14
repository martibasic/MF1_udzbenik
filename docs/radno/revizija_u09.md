# Revizija U09 — kompresibilni idealni tok

## Opseg i dijagnoza prije provedbe

Korisnički zahtjev od 22. rujna 2026.: sljedeće poglavlje prema pravilima
prethodnih revizija, s naglaskom na točne zadatke i fizikalno jasne skice.
Kanonski izvor je `source/u09_kompresibilni_idealni_tok.md`, verifier
`tools/verify_u09_compressible.py`, namespace `U09.COMP`. Omotač se ne mijenja.
Pet riješenih primjera ostaje za usporedbu; šest vježbi ostaje T1/T1/T2/T2/T3/T4.

Z1 i Z2 opravdano uvježbavaju osnovnu računsku tehniku. Z3 ponavlja P3 i dva
puta istu energetsku relaciju, bez stvarne odluke razine T2. Z4 je dosad bio
samo jedan račun kritičnog tlaka, također bez odluke T2. Z5 ima vrijedan
problem razdvajanja geometrije i koeficijenta, ali nepotrebno preuzima
propagaciju nesigurnosti od Z6. Z6 zahtijeva ispravak mjernog lanca:
nekorigirana Pitotova sonda u nadzvučnom toku ne očitava ukupni tlak ispred
svog udarnog vala. Sintetičke podatke i standardne nesigurnosti treba imenovati.

Uvodna slika ima nacrtane krute završne plohe preko ulaza i izlaza sapnice i
kanala. Jedan uzdužni gradijent dodatno stvara neobjašnjenu promjenu nijanse
istoga plina. U poglavlju nema drugih statičkih skica. Nova zajednička slika
vježbi preuzima raspored 2 × 3 i stil prethodnih poglavlja. Naziv
`u09_kompresibilni_vjezbe_skice.svg` namjerno se razlikuje od naslijeđenog
`u09_vjezbe_skice.svg`, koji pripada javnom poglavlju 8.

## Matrica odluka

| P/Z | Postojeći ID, princip i aktivnost | Odluka i didaktička korist | Razina | Završni ID | Datoteke i provjere | Status |
| --- | --- | --- | --- | --- | --- | --- |
| P1 | `ex-akusticko-vrijeme`; a=√γRT, t=L/a; izravan račun i granica odziva | ZADRŽATI; osnovni izravni problem | T1 | isti | izvor, postojeći golden | zadržano |
| P2 | `ex-odabir-modela-kompresibilnosti`; Q/A, Mach; prag nakon promjene Q | ZADRŽATI; odluka o modelu | T2 | isti | izvor, postojeći golden | zadržano |
| P3 | `ex-stagnacijski-zrak`; T0/T i p0/p; pretvorba statičkih veličina | ZADRŽATI; referentni energetski račun | T2 | isti | izvor, postojeći golden | zadržano |
| P4 | `ex-priguseni-ventil`; kritični omjer i maksimalni protok | ZADRŽATI; povezivanje uvjeta prigušenja i kapaciteta | T3 | isti | izvor, postojeći golden | zadržano |
| P5 | `ex-normalni-udar`; M2 i p2/p1; izbor entropijski dopuštenog smjera | ZADRŽATI; izravni model vala | T3 | isti | izvor, postojeći golden | zadržano |
| Z1 | `task-brzina-zvuka-helium`; brzina zvuka, neodređen smjer poremećaja | PREPRAVITI samo pretpostavku mirovanja i dva uzdužna smjera | T1 | isti | izvor, panel Z1, verifier | provedeno |
| Z2 | `task-mach-ventilacija`; Q/A i Ma; rutina slična P2 | ZADRŽATI račun; navesti lokalni volumenski protok, konstante i granice početne procjene | T1 | isti | izvor, panel Z2, verifier | provedeno |
| Z3 | `task-stagnacijska-temperatura`; dva zapisa iste energetske relacije | ZAMIJENITI; iz uzvodnog/nizvodnog vremena odabrati predznake, razdvojiti a i v te odrediti T | T2 | `task-akusticko-mjerenje-toka` | izvor, panel Z3, novi golden i invarijante | provedeno |
| Z4 | `task-priguseni-protok`; izravan p* | PREPRAVITI; dva manometarska protutlaka, apsolutni omjeri, izbor režima i izlaznog tlaka/Macha | T2 | isti | izvor, panel Z4, verifier, notebook | provedeno |
| Z5 | `task-sapnica-model`; produkt površine i koeficijenta, RSS | PREPRAVITI; nominalna i neovisno izmjerena stvarna površina, provjera objašnjava li sama geometrija manji protok | T3 | isti | izvor, panel Z5, verifier, notebook | provedeno |
| Z6 | `task-udarni-val-podaci`; inverzija modela i slaganje uz nesigurnost | PREPRAVITI mjerni lanac; p01 iz mirne komore, p02 iz podzvučne Pitotove sonde; zadržati neovisnu usporedbu | T4 | isti | izvor, panel Z6, verifier, D03 | provedeno |

## Provenijencija i vezani izvori

Nova scena Z3 autorska je konstrukcija: promijenjeni su kontekst, podatci,
tražene veličine i strategija (4/5), a prvi korak postaje odabir referentnog
sustava. Stari ID ostaje jednokratni HTML span prije novog naslova, kao u
prethodnim poglavljima; provjeriti da manifest i D06 i dalje imaju šest zadataka.

`rewrite_status`: completed; `rewrite_level`: selective (Z3 substantial).
`sketch_requirement`: obavezna za Z3–Z6 (više mjernih točaka/presjeka),
preporučena za Z1–Z2 radi smjerova i promjera. Skice prikazuju zadano, bez
otkrivanja svih odgovora. Debljina stijenki i veličina mjernih elemenata su
shematske; stvarne kotirane razdaljine i otvoreni presjeci moraju biti dosljedni.

Provjera fizikalnih relacija prema primarnim izvorima (22. rujna 2026.):

- NASA Glenn, [Normal Shock Wave Equations](https://www.grc.nasa.gov/WWW/k-12/airplane/normal.html).
- NASA Glenn, [Pitot–Static Tube](https://www1.grc.nasa.gov/beginners-guide-to-aeronautics/pitot-static-tube-speedometer/).
- NASA Glenn, [Mass Flow Choking](https://www.grc.nasa.gov/www/k-12/BGP/mflchk.html).

To su izvori provjere relacija, a ne provenijencija izmišljenih mjerenja.
Notebook ostaje eksperiment sapnice; dopuniti ga radnim točkama Z4/Z5 i
stvarnom usporedbom s nestlačivim modelom, koju njegov postojeći opis obećava.
D03 dopuniti konkretnim pogreškama. D06 i manifest regenerirati alatima.

## Neovisne provjere i prikaz

Provedeno 22. rujna 2026. Sve odluke u matrici provedene su. Usporedba s
početnom snimkom potvrđuje da su teorija i svih pet riješenih primjera tekstualno
nepromijenjeni. Stari Z3 anchor ostaje dostupan, a kanonski manifest i D06
upućuju na `task-akusticko-mjerenje-toka`.

Neovisno ponovno računanje daje:

- Z3: a=350 m/s, v=50 m/s, T=304,878 K, Ma=1/7; laboratorijski signali
  +400 i −300 m/s. Zamjena vremena mijenja samo predznak v, jednaka vremena
  daju mirovanje plina.
- Z4: p*=4,226254 bar(abs); I ima pe=5 bar i Ma=0,847705; II ima pe=p*
  i Ma=1. Neovisni račun rho_e v_e potvrđuje plato masenog toka.
- Z5: Cd Ag=42,495898 mm²; idealno 0,0672065 kg/s kroz stvarnih 48 mm²,
  Cd=0,885331. Sama razlika nazivnog i stvarnog otvora nije dovoljna.
- Z6: M1=2, u(M1)=0,006819; G=0,720874, r0=0,720447,
  u(G−r0)=0,008495, normirana razlika 0,050213. Drugi oblik relacije
  ukupnog tlaka, očuvanje količine gibanja/energije i granica M1→1
  provjereni su odvojeno od objavljenih golden rezultata.

Izvršene provjere:

- `verify_u09_compressible.py`: 64 rezultata, bez pada.
- `verify_all.py`: 1188 rezultata (1025 golden, 163 invarijante), još 22
  neovisne fizikalne provjere, 90/90 ugovora; bez rupa ili tautologija.
- `check_u09_sketch_geometry.py`: otvoreni prolazi i uzorkovani profili
  sapnica, kota A–B i unutarnji promjer, smjerovi signala, okomitost vala,
  Pitotov otvor i stvarni prolazi mjernih vodova kroz stijenke. Ukupno 930
  provjera, uključujući ponovljene presjeke istih geometrijskih uvjeta.
- Audit publikacije: 87 primjera i 90 vježbi; točne razine svih poglavlja.
  Normalizacija, generator D06, manifest i Typst audit prolaze.
- Notebook U09 izvršen od početka u čistom kernelu. Dodana je usporedba
  nestlačive i izentropske karakteristike s provjerom granične pogreške,
  a Z4/Z5 koriste iste podatke i rezultate kao tekst/verifier.
- Cijeli HTML i nativni PDF generirani su redom. Nakon povećanja natpisa
  obnovljeni su statički HTML resursi i PDF. PDF ima 311 A4 stranica;
  audit prolazi. Pregledani su uvod (163), slika vježbi (167), zadatci
  (168–169) i ključ (301–302). Str. 170 sadržava samo zaglavlje/podnožje
  prije sljedećeg dijela; globalni predložak prijeloma nije mijenjan.
- Edge: 320/768/1440 px, šest zadataka, razine, stari anchor, jedinstveni
  ID-jevi, otvaranje/zatvaranje 12 naputaka i odgovora tipkovnicom,
  bez vodoravnog prelijevanja. Automatizirana WCAG A/AA provjera bez nalaza.
  Svih šest povratnih poveznica D06 valjano je.
- Vizualno pregledana oba SVG-a i stvarni PDF. Završni natpisi ne izlaze
  iz svojih panela i ne preklapaju se međusobno. Šrafure ostaju na krutim
  stijenkama; plin i mjerni vodovi Z6 dijele isti prostorni gradijent.
- `git diff --check` prolazi. Izvan U09 mijenjaju se samo povezani D03,
  generirani D06/manifest i dokumentacija alata.

Nije ponovljen cijeli objavni CI (svih 17 notebookova, JupyterLite i 72
viewport slučaja), jer ovaj korak uređuje poglavlje bez objave. Prije
sljedećeg commit/push koraka slijedi objavna provjera prema workflowu.
Lokalna numerička provjera, geometrijski i vizualni pregled te CI nisu
zamjena za vanjsku stručnu recenziju ili studentski pilot.

## Dopuna prije objave (22. rujna 2026.)

Na zajedničkom završnom stanju U09/U10 izvršeno je svih 17 notebookova.
QR, CFD V&V, JupyterLite (17 notebookova, Pyodide), audit 24 HTML stranice
i 1924 poveznice te 72 viewport/WCAG slučaja uz A4 ispis prolaze.
JupyterLite u pregledniku doseže Python (Pyodide) / Idle. Završni PDF nakon
U10 ima 313 A4 stranica i prolazi audit; primjerak za preuzimanje identičan
je datoteci u `_book/`. Izvršene su i brojčane, strukturne i geometrijske
provjere. Za QR/JupyterLite korišten je postojeći `tools/tmp/publish-env`;
zadani lokalni Python nema te dvije ovisnosti. Poslužiteljski CI zasebno
izvršava zaključane ovisnosti na Pythonu 3.12.


## Revizija 12. 10. 2026. (provedba recenzentskih nalaza)

Izvor: stručna recenzija od 12. 10. 2026. i brief koordinatora. Opseg obuhvaća kanonski izvor, verifier `verify_u09_compressible.py`, skice `u09_fig_uvod_kompresibilni_tok.svg` i `u09_kompresibilni_vjezbe_skice.svg` te checker `check_u09_sketch_geometry.py`. Bilježnica `u09_kompresibilna_sapnica.ipynb` nije dirana jer su Z4 i Z5 ostali nepromijenjeni. Prema planu knjige poglavlje dobiva jedan riješeni primjer više (5 → 6).

### Matrica zamjena

| P/Z | Stari ID i stanje | Odluka | Razina | Završni ID | Kontrolni rezultat | Status |
| --- | --- | --- | --- | --- | --- | --- |
| P1 | `ex-akusticko-vrijeme` | ZADRŽATI; κ umjesto γ | T1 | isti | 343 m/s; 0,248 s | provedeno |
| P2 | `ex-odabir-modela-kompresibilnosti`; nerealna brzina | PREPRAVITI kontekst u usisni vod kompresora turbopuhala (80–110 m/s realno); brojevi isti | T2 → T1 | isti | 83,6 m/s; Ma 0,244; +30 %: 0,317 | provedeno |
| P3 | `ex-stagnacijski-zrak` | PREPRAVITI provjeru: brojčana pogreška nestlačivog modela (24,6 prema 28,8 kPa, −15 %) | T2 → T1 | isti | T0 293,3 K; p0 83,8 kPa | provedeno |
| P4 | `ex-priguseni-ventil` | ZADRŽATI; kritični omjeri premješteni u teoriju; nazivlje zagušenje | T3 → T2 | isti | 0,0700 kg/s; 317 kPa | provedeno |
| P5 | `ex-normalni-udar` | ZADRŽATI; dodana Prandtlova provjera | T3 → T2 | isti | Ma2 0,577; p2/p1 4,50 | provedeno |
| P6 | novo | DODATI režim K-D sapnice (Ae/A* = 1,6, tri karakteristična protutlaka, odluka za 100 i 350 kPa, položaj vala) | T3 | `ex-kd-sapnica-rezim` | Ma_e 0,397/1,935; p_e,I 448,5, p_e,II 297, p_e,III 70,7 kPa; ṁ 0,117 kg/s; val pri A/A* = 1,39 | provedeno |
| Z1 | `task-brzina-zvuka-helium` | ZADRŽATI; κ | T1 | isti | 1019 m/s | provedeno |
| Z2 | `task-mach-ventilacija`; klon P2 | ZAMIJENITI zrakom za upućivanje brodskog dizelskog motora (boca 30 bar, zagušeni ventil) | T1 | `task-zrak-za-upucivanje-motora` | pb/p0 0,267, zagušeno; 0,850 kg/s; 2,94 s | provedeno |
| Z3 | `task-akusticko-mjerenje-toka` | ZADRŽATI; κ | T2 | isti | nepromijenjen | provedeno |
| Z4 | `task-priguseni-protok` | ZADRŽATI; nazivlje zagušen | T2 | isti | nepromijenjen | provedeno |
| Z5 | `task-sapnica-model` | ZADRŽATI; κ, zagušenje | T3 | isti | nepromijenjen | provedeno |
| Z6 | `task-udarni-val-podaci` | ZADRŽATI; Ma umjesto M, zaustavni tlak | T4 | isti | nepromijenjen | provedeno |

Stari anchor Z2 ostaje kao `<span id="task-mach-ventilacija">`.

### Teorija i notacija

- Dodani blokovi `.mf1-izvod`:
  - brzina zvuka iz bilance preko tankog vala;
  - A/A* (`eq-omjer-povrsina`) i zagušeni protok iz ṁ = ρ*a*A*;
  - Prandtlova relacija (`eq-prandtlova-relacija`), `eq-normalni-skok` (sada i T2/T1) i entropija (`eq-entropija-udar`, Δs = +94 J/(kg K) pri Ma1 = 2).
- Kritični omjeri (`eq-kriticni-omjeri`) premješteni su u teoriju.
- Dodan je novi blok `.mf1-granica-modela` za idealni 1D model.
- Nazivlje i oznake: κ, Ma, zaustavne veličine, kalorički savršen plin, zagušenje, CFL.
- Zadržani su ID-jevi `eq-priguseni-protok`, `cfd-sapnica-prigusenje`, `cfd-sapnica-udarni-val`, `ex-normalni-udar` i `sec-sapnica-prigusenje`.
- Duplicirano pitanje u „Provjeri sebe” zamijenjeno je novim.

### Skice i provjere

- `u09_kompresibilni_vjezbe_skice.svg`:
  - panel Z2 (boca, ventil kao kritični presjek, vod prema motoru) unutar istog okvira;
  - natpisi Z6 promijenjeni u Ma₁ i Ma₂.
- `u09_fig_uvod_kompresibilni_tok.svg`: dodan izlazni presjek `u09fukt_exit` s natpisima p₀, T₀ i Aₑ, pᵦ. Nova datoteka nije bila potrebna.
- `check_u09_sketch_geometry.py`: dodane su provjere ventila Z2, izlaza u uvodnoj skici i oznake Ma. Rezultat: PASS, 1246 provjera.
- `verify_u09_compressible.py`: 100/100. Uklonjeni su stari ID-jevi U09.COMP.Z2.Ma i Z2.v.
- Nije pokrenuto: generatori s `--write` i render. To radi koordinator.
