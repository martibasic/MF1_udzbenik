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
