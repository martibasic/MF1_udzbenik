# Revizija U14 — turbostrojevi i propulzija

## Dijagnoza i matrica prije provedbe

Kanonski izvor je `source/u14_turbostrojevi_i_propulzija.md`, a stvarni
verifier `verify_u12.py` s namespaceom U12. Notebook i svih sedam postojećih
skica također imaju naslijeđeni prefiks u12; provjerene su stvarne reference.

P1–P5 grade slijed od mirne vodilice preko relativnog dotoka do momenta
reprezentativne lopatice. P6 donosi aktuatorski disk. Z1/Z2 treba sačuvati
kao jednostavnu tehniku. Z3 ponavlja izravni račun P4, Z4 račun momenta P5,
a Z5 je samo zbroj triju jednakih mlazova i ne opravdava T3. Z6 ima korisnu
odluku s granicama ulaza, ali dovod i referentno stanje platforme nisu jasni.

| Mjesto | Postojeći ID i uloga | Odluka / studentska aktivnost | Razina | Završni ID | Povezane provjere | Status |
| --- | --- | --- | --- | --- | --- | --- |
| P1 | `ex-u12-vodilica-mlaza-na-ispitnom-stolu-t2`; sila i reakcija | ZADRŽATI račun; popraviti tlocrt, širinu izlaza i kotu izvan SVG-a | T2 | isti | SVG, verifier | provedeno |
| P2 | `ex-u12-relativni-dotok-na-pokretnu-lopaticu-t1`; relativni protok | ZADRŽATI; nacrtati otvorenu sapnicu, pravu kotu promjera i izlaz fluida uz lopaticu | T1 | isti | SVG, verifier | provedeno |
| P3 | `ex-u12-pokretna-ravna-lopatica-u-mlazu-t2`; sila i snaga | ZADRŽATI; fluid ostaje ispred krute ploče, izlazni apsolutni vektori uključuju u | T2 | isti | SVG, verifier | provedeno |
| P4 | `ex-u12-pokretna-zakrivljena-lopatica-s-relativnim-izlazom-t3`; k i trokut brzina | ZADRŽATI; uskladiti stvarni izlaz i zatvaranje vektorskog trokuta | T3 | isti | SVG, verifier | provedeno |
| P5 | `ex-u12-peltonov-rotor-s-jednim-mlazom-i-momentom`; lokalni doprinos lopatice | ZADRŽATI račun; izričita lokalna aproksimacija, ukloniti tvrdnju sa skice o dostatnosti generatora | T4 | isti | SVG, verifier | provedeno |
| P6 | `ex-u12-propeler-dronskog-kvadkoptera-u-stanju-visa-t2`; disk i snaga | ZADRŽATI: korisna promjena modela i jasna granica trajanja leta | T2 | isti | verifier | provedeno |
| Z1 | `task-u12-vodeni-mlaz-brzine-izlazi-iz-kruzne-sapnice`; nepomična ploča | ZADRŽATI; gustoća, referentni tlak i slobodno razlijevanje | T1 | isti | SVG, verifier, D06 | provedeno |
| Z2 | `task-u12-vodeni-mlaz-brzine-izlazi-iz-pravokutne-sapnice`; komponente sile | ZADRŽATI; horizontalna ravnina, osi i kut, reakcija na određeno tijelo | T1 | isti | SVG, verifier, D06 | provedeno |
| Z3 | `task-u12-na-pokretnu-lopaticu-dolazi-mlaz-vode-apsolutnom`; izravni račun sile | ZAMIJENITI: iz sintetičke sile rekonstruirati c2, w2, kut i k te provjeriti energetsku mogućnost | T2 | `task-izlaz-lopatice-iz-izmjerene-sile` | stari alias, SVG, notebook, verifier, D06 | provedeno |
| Z4 | `task-u12-peltonova-lopatica-na-rotoru-radijusa-prima-mlaz`; Ft i M | ZAMIJENITI: dva radijusa, dva trokuta brzina i predznak Eulerova rada | T2 | `task-dva-radijusa-i-rad-rotora` | stari alias, SVG, notebook, verifier, D06 | provedeno |
| Z5 | `task-u12-potisni-modul-ima-tri-jednake-sapnice-promjera`; zbroj mlazova | ZAMIJENITI: izbor vodomlaznog pogona pri brzini broda uz ulazni impuls i ograničenje električne snage | T3 | `task-vodomlazni-pogon-uz-ogranicenu-snagu` | stari alias, SVG, notebook, verifier, D06 | provedeno |
| Z6 | `task-u12-mlazna-platforma-ukupne-mase-ima-cetiri-jednake`; najgori slučaj | ZADRŽATI odluku; definirati dovod, trenutačno stanje i granice ulaza, bez tvrdnje o certificiranoj nosivosti | T4 | isti | SVG, verifier, D06 | provedeno |

`rewrite_status`: complete; `rewrite_level`: selective;
`sketch_requirement`: svih sedam postojećih skica.
Novi zadatci i podatci autorski su nastavni primjeri; mjerni podatci Z3 su
sintetički, a kandidati Z5 nisu specifikacije stvarnog proizvoda.

## Fizikalni nalazi na skicama

- Uvod i P2 imaju privid zatvorenog izlaza sapnice i tok kroz tijelo lopatice;
  vodomlazni prikaz ne definira dovoljno jasno referentni okvir.
- P1 ima kotu izvan slike, nepotpuno spojene tokove i izlazni presjek koji
  ne prati smanjenje brzine pri istom masenom protoku.
- P3 crta vodu unutar čvrste ploče; P4 ima vodoravnu kotu promjera i
  nepovezanu geometriju povratnog toka. Trokute treba provjeriti iz koordinata.
- P5 prikazuje izlazni mlaz odvojen od zatvorene zdjelice, a rezultat
  pogrešno proglašava dostatnim za generator, suprotno granici modela u tekstu.
- Zajednička slika pogrešno ponavlja Z1/Z2/Z3 umjesto Z1–Z6, ima zatvorene
  sapnice, obrnutu reakciju Z2 i pogrešan smjer pozitivnog izlaznog vrtloga Z4.
  Dovod Z6 nije prikazan. U D06 se postojeći sažetak Z4 prekida usred formule.

## Neovisni račun prije pisanja

- Z3: c1 = 32 m/s, u = 12 m/s, relativni protok 18 kg/s; sintetička sila
  fluida na lopaticu (625,0; −153,0) N. Dobiva se c2 = (−2,72222; 8,5) m/s,
  w2 = (−14,72222; 8,5) m/s, k ≈ 0,84999, kut ≈ 150°, P = 7,500 kW.
  Gubitak mehaničke energije u modelu iznosi približno 0,999 kW i nije negativan.
- Z4: r1 = 0,060 m, r2 = 0,140 m, omega = 200 rad/s, protok 3 kg/s;
  c1 = (5; 4), c2 = (20; 6) m/s u lokalnim osima (t, r). Obodne brzine
  su 12 i 28 m/s; w1 = (−7; 4), w2 = (−8; 6) m/s. Rotor na fluid daje
  M = 7,50 N m i P = 1,500 kW, odnosno 500 J/kg; suprotan moment prima rotor.
- Z5: pri U = 8 m/s i T = 2000 N, izlazi 20/30 m/s u brodskom okviru
  traže Q = 0,166667/0,090909 m³/s. Hidrauličke snage su 28/38 kW;
  za zadanu električnu–hidrauličku učinkovitost 0,80 električne su 35/47,5 kW.
  Granicu 40 kW zadovoljava prvi kandidat. Korisna snaga TU = 16 kW,
  propulzijske učinkovitosti su 0,57143 i 0,42105.

## Rezultati

Provedeno 22. rujna 2026. Z1, Z2 i Z6 zadržani su uz jasnije pretpostavke;
Z3–Z5 zamijenjeni su prema gornjoj matrici. Sva tri stara ID-ja ostala su
pojedinačni HTML aliasi uz nove naslove. U14 i dalje ima šest riješenih
primjera i šest vježbi T1/T1/T2/T2/T3/T4.

Svih sedam postojećih SVG-ova prilagođeno je sadržaju uz zadržane panele,
paletu, šrafure i tipografiju. Sapnice su otvorene, razlijevanje ostaje
ispred ploča, krak rotora završava na poleđini lopatice i ne ulazi u vodu.
Kote širina/promjera poprečne su na tok; kutovi imaju dva referentna kraka.
Trokuti brzina nacrtani su iz podataka u navedenoj zajedničkoj skali.
Vodomlazni vodovi imaju stvarne omjere kružnih presjeka iz kontinuiteta,
a platforma dva simetrična horizontalna dovoda i četiri otvorena izlaza.
Duljine uređaja i oblik razlijevanja ostaju shematski prikazi.

U postojećim primjerima ispravljene su pogreške zaokruživanja (P2: 63,6 %;
P3: 282,2 N i 2,540 kW; P4: 723,0 N i 7,230 kW; P5: 680,3 N,
689,7 N i 312,95 N m). Završni se račun temelji na nezaokruženim podacima.
Uklonjena je opća tvrdnja da tangencijalna sila mora biti veća od normalne.
Samoprovjera razlikuje optimum jedne lopatice od optimuma kola s punim
protokom. P5 izričito ograničava lokalni model i ne dokazuje kontinuiranu
snagu generatora.

Usklađeni su D03, generirani D06, notebook i stvarni verifier `verify_u12.py`.
Notebook ima obrnuti račun izlaza, provjeru energetske mogućnosti, oba
lokalna trokuta, Eulerov rad i usporedbu kandidata Z5 te završna pitanja.
Brojevi u izvoru ručno su uspoređeni s funkcijama i notebookom, uključujući
vektore i parove kandidata koje konzervativni parser manifesta ne rastavlja
potpuno. Manifest je obnovljen generatorom.

Za provjeru referentnog okvira Z5 korištene su primarne nastavne bilješke
[MIT OCW 2.611 — Waterjet propulsion](https://www.ocw.mit.edu/courses/2-611-marine-power-and-propulsion-fall-2006/3b26401197d2c93c660289c51fa8e7bb_04waterjet.pdf).
Jednaki tlakovi i visine te zanemareni trag trupa i gubitci eksplicitne su
pretpostavke novog autorskog zadatka; iz njih slijedi korištena bilanca
snage s ulaznim impulsom. Nisu preuzeti podatci stvarnog proizvoda.

Izvršene provjere:

- `check_u14_sketch_geometry.py`: PASS za sedam stvarnih SVG-ova; prolazi,
  nepropusne ploče, presjeci, kutovi, vektori, radijus/vrtnja i kontinuitet.
  Stvarne rasterizacije pregledane su; tekst ne izlazi iz njihovih granica.
- `verify_u12.py`: 80 rezultata; cijeli `verify_all.py`: 1296 rezultata,
  1092 golden usporedbe, 204 invarijante, 22 dodatne fizikalne provjere i
  90/90 ugovora zadataka; PASS.
- Struktura, Typst, normalizacija, QR, generirani D06 i manifest te CFD
  podatci: PASS. Nema promjene ugovorenih 87 primjera i 90 vježbi.
- Izmijenjeni notebook izvršen je u čistom kernelu: PASS (4,94 s).
- Cijeli HTML obnovljen, zatim ciljano obnovljeni završni U14, D06 i
  `za_ispis`. Ispravljen je nedostajući prazni red prije sklopivog odgovora
  samoprovjere; konačni prikaz nema sirovih ograda `:::`.
- U14 na 320/768/1440 px: šest zadataka i razina, tri stara aliasa,
  jedinstveni ID-jevi, 12 odgovora/naputaka dostupnih tipkovnicom, bez
  vodoravnog prelijevanja; WCAG A/AA: PASS. D06 ima šest povratnih veza
  i cjelovite formule; posebno je uklonjen prekid sažetka Z4 usred formule.
- Nativni PDF: 315 A4 stranica, 6 995 064 bajta; audit PASS. Izvučene su
  stranice U14 235–254; vizualno pregledani prikaz rotora, vježbe i ključ
  na stranicama 248, 251–252 i 312–313. Aktualni PDF kopiran je u downloads.
- JupyterLite obnovljen s aktualnim notebookovima; audit 17 notebookova
  i četiri ekstenzije: PASS. Audit 24 HTML stranice, 220 slika, 1930 veza
  i 446 sklopivih blokova: PASS.

Autorska procjena: nove vježbe uvode rekonstrukciju, odluku o smjeru rada
i izbor pogona uz ograničenje, umjesto još triju izravnih računa iste sile.
Automatizirane provjere potvrđuju navedena svojstva, ne cijelu didaktičku
kvalitetu. Zajednička provjera svih notebookova i 72 prikaza za konačno
izdanje slijedi nakon U15 i povratnog pregleda U01/U02.
