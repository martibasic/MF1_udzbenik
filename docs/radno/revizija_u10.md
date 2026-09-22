# Revizija U10 — količina i moment količine gibanja

## Opseg i početna dijagnoza (22. rujna 2026.)

Korisnik traži sljedeće poglavlje prema prethodnim pravilima. Uređuje se
`source/u10_kolicina_i_moment_kolicine_gibanja.md`, uz povijesni verifier
`tools/verify_u11.py` i namespace `U11`. Postojeći SVG-ovi i notebook također
nose naslijeđeni prefiks u11; ne pripadaju javnom poglavlju 11.

Zadržava se šest primjera i šest vježbi T1/T1/T2/T2/T3/T4. Z1–Z2 čine
koristan izravni/inverzni par osnovnog računa. Z3 uvježbava vektorsku bilancu.
Z4 ponavlja P4 i pretežan dio Z6; Z5 ponavlja P2, a oznaka T3 nije opravdana
samim duljim izravnim računom. Nedostaju moment zbog ekscentrične sile i
primjena već uvedenog pomičnog kontrolnog volumena uz energetsku provjeru.

Uvodni SVG ima krutu pregradu kroz koljeno i prirubnicu preko izlaza.
P2 ima nacrtan pun prirubnički čep kroz fluid. P3–P5 i slika vježbi imaju
višestruke ispune koje stvaraju neobjašnjene promjene nijanse, zatvorene
presjeke ili preklapanje stijenki račve. Kote promjera na nekim sapnicama
ne mjere presjek označen u zadatku. Sve se skice pregledavaju; čuvaju se
postojeći raspored panela, paleta, šrafure i tipografija.

## Matrica prije provedbe

| Mjesto | Postojeći ID i aktivnost | Odluka i korist | Razina | Završni ID | Povezani izvori/provjere | Status |
| --- | --- | --- | --- | --- | --- | --- |
| P1 | `ex-u11-mlaz-vode-na-mirnu-ravnu-plocu-t2`; F=ṁv, promjena predznaka | ZADRŽATI račun; popraviti prikaz razdvajanja mlaza uz ploču | T2 | isti | izvor, P1 SVG, verifier | provedeno |
| P2 | `ex-u11-kalibracijska-mlaznica-na-prirubnici-t2`; sila ploče → Q → p → prirubnica | ZADRŽATI; otvoriti prirubnicu i očuvati stvaran omjer D:d | T2 | isti | P2 SVG, verifier | provedeno |
| P3 | `ex-u11-servisno-koljeno-na-sidrenom-nosacu-t2`; vektorski tlak i impuls | ZADRŽATI račun; ispraviti proturječnu pretpostavku bez gubitaka uz zadane tlakove | T2 | isti | izvor, P3 SVG, energetska provjera | provedeno |
| P4 | `ex-u11-t-racva-na-sidrenoj-konzoli-t3`; Bernoulli, kontinuitet, sila | ZADRŽATI; jedna povezana ispuna i tri otvorena presjeka | T3 | isti | P4 SVG, verifier | provedeno |
| P5 | `ex-u11-y-racva-s-mjerenom-reakcijom-konzole-t4`; inverzna reakcija → radni režim | ZADRŽATI; razjasniti poprečnu os y u horizontalnoj ravnini; skica ne smije proglasiti punu nosivost dokazanom | T4 | isti | izvor, P5 SVG, verifier | provedeno |
| P6 | `ex-u11-sila-na-koljeno-tlacnog-voda-male-hidroelektrane`; simetrično koljeno, kut rezultante | ZADRŽATI; jasno zadati izlaz prema −y koji odgovara objavljenom pozitivnom Fy; dodati potrebnu skicu | T2 | isti | izvor, novi SVG, verifier/notebook | provedeno |
| Z1 | `task-u11-vodeni-mlaz-promjera-izlazi-iz-sapnice-brzinom`; izravan impuls | ZADRŽATI; potpune pretpostavke, sila na ploču i reakcija | T1 | isti | izvor, panel Z1, golden | provedeno |
| Z2 | `task-u11-mlaz-vode-udara-okomito-na-nepomicnu-plocu`; inverzni račun | ZADRŽATI; razjasniti što mjeri zadana sila | T1 | isti | izvor, panel Z2, golden | provedeno |
| Z3 | `task-u11-horizontalno-koljeno-zakrece-tok-vode-za-bez`; dvije komponente | PREPRAVITI oznake ravnine, sila i reakcije; zadržati podatke | T2 | isti | izvor, panel Z3, golden | provedeno |
| Z4 | `task-u11-t-racva-prima-vodu-kroz-ulaz-promjera`; ponovljen račun račve | ZAMIJENITI; ekscentričan mlaz i moment oko oslonca, izbor okomitog kraka umjesto udaljenosti | T2 | `task-moment-ekscentricnog-mlaza` | izvor, panel Z4, novi golden/invarijante | provedeno |
| Z5 | `task-u11-konvergentna-mlaznica-ima-ulazni-promjer-izlazni-promjer`; izravan račun P2 | ZAMIJENITI; jedna pomična ploča, relativni dotok mase, apsolutni impuls i snaga | T3 | `task-mlaz-na-pomicnu-plocu` | izvor, panel Z5, verifier/notebook | provedeno |
| Z6 | `task-u11-vodoravna-y-racva-prima-vodu-kroz-ulaz`; granice podataka i izbor nosača | ZADRŽATI; eksplicitni zajamčeni intervali i dokaz položaja maksimuma, potpuna odluka u D06 | T4 | isti | izvor, panel Z6, verifier | provedeno |

## Provenijencija i granice zahvata

Z4/Z5 su autorske konstrukcije, bez vanjskog donora. Mijenjaju se najmanje
četiri od pet elemenata (scena/geometrija/podatci/traženo/strategija).
Stari ID-jevi ostaju jednokratni spanovi prije novih naslova; D06 i manifest
generiraju se alatima i moraju zadržati šest kanonskih zadataka.

`rewrite_status`: complete; `rewrite_level`: selective, Z4/Z5 substantial.
`sketch_requirement`: obavezna za smjerove i referentne presjeke; Z4 posebno
za krak momenta, Z5 za razliku apsolutne i relativne brzine.

Riješeni primjeri nisu novi didaktički zahvat. Dopušteni sitni ispravci služe
traženoj fizikalnoj točnosti: P3 ne može istodobno imati zadane tlakove,
protoke i nulte gubitke; P5 opisuje poprečnu komponentu u tlocrtu, a ne
visinsku razliku; P6 treba jednoznačan smjer zakretanja. Ostali podatci i
računski postupci ostaju. Ne uvodi se teorija turbostrojeva: Z4 koristi
moment sile krute konstrukcije, a Z5 već uveden pomični KV i energiju iz U08.

Povezani izvori: D03, generirani D06 i manifest, notebook
`u11_sila_na_koljeno.ipynb`, SVG-ovi i alat za geometrijsku provjeru.
Nezavršene lokalne izmjene dovršenog U09 čuvaju se. Ovaj zahtjev ne uključuje
commit/push.

## Rezultati provjera

- `verify_u11.py`: **70/70 PASS**. Rezultati svih šest vježbi uspoređeni su
  s neovisno izračunatim brojčanim vrijednostima; apsolutne tolerancije
  prate objavljeno zaokruživanje. Novi Z4 provjerava ravnotežu sile i
  momenta te neovisnost o vodoravnom pomaku b. Z5 uspoređuje mehaničku
  snagu s apsolutnim tokom kinetičke energije za šest brzina ploče,
  provjerava maseni dotok, unutarnji maksimum i rubove intervala.
- `verify_all.py`: **1210** sirovih rezultata, od toga 1034 usporedbe s
  unaprijed zadanim vrijednostima i 176 invarijanti, uz **22** neovisne
  fizikalne golden provjere. Pokriveno 90/90 ugovora zadataka; nema rupa
  ni samousporedbi. Ti brojevi nisu broj neovisnih fizikalnih modela.
- Z6: maksimum nad zajamčenim intervalima nije pretpostavljen samo na
  temelju osam uglova. Za Fx=pA1+ρQ²f(s), Fy=ρQ²g(s) u cijelom području
  vrijede Fx>0, Fy<0, f<0, f′<0 i g′>0. Zato F² raste s p i pada sa s.
  Gornja granica izraza Fx f+Fy g negativna je, pa F² pada i s Q.
  Globalni maksimum **2918,3 N** nastaje pri **190 kPa, 39,2 L/s,
  s=0,57**. Nakon faktora 1,15 zahtjev je **3356,1 N**, pa zadani
  statički kriterij zadovoljava samo ponuđena nosivost **3,5 kN**.
- `check_u10_sketch_geometry.py`: PASS za osam SVG-ova. Čita stvarne
  objavljene putanje: stijenke moraju ležati na rubu fluida, otvori
  ostati slobodni, a fluid ne smije prijeći prednju stranu ploče.
  Provjereni su otvor prirubnice P2, monoton profil sapnice, stalni ili
  postupno promjenjivi normalni promjeri kroz zavoje, kut 60° i normalne
  kote grana, isti prostorni gradijent, krakovi b/e i smjerovi vektora.
  Z5 izlazne strelice imaju apsolutne komponente u i ±(v−u).
- Audit publikacije: 87 riješenih primjera, 90 vježbi i očuvane razine
  T1/T1/T2/T2/T3/T4. Normalizacija, D06, manifest i Typst audit prolaze.
  Naputci i odgovori U10 stanu unutar granice generatora od 500 znakova;
  nijedan nije odrezan. Sažeci ne prekidaju matematičke izraze.
- Notebook `u11_sila_na_koljeno.ipynb` izvršen je od početka u čistom
  kernelu. Osnovni slučaj koristi Z3; dodani su P6 sa zakretom −60°,
  Z4 s momentom oko uklještenja te Z5 s energetskom provjerom i grafom
  snage jedne ploče. Običan NumPy/Matplotlib, bez novih ovisnosti.
- Cijeli HTML uspješno je generiran; nakon završnog usklađivanja teksta
  i oznaka obnovljeni su U10 i D06. Potom je izrađen cijeli nativni PDF.
  Završni PDF ima **313 A4 stranica** i prolazi audit. Vizualno su
  pregledani uvod (171), P1–P6 (176, 177, 179, 181, 183, 185), zadatci
  i zajednička skica (186–188), te kontrolni rezultati (305–306).
  Skice ostaju vektorske; nema rasterizacije ni filtara sjene.
- Edge na 320/768/1440 px: šest zadataka i točne razine, jedinstveni
  ID-jevi, oba stara sidra, svih 12 naputaka/odgovora otvara se i zatvara
  tipkovnicom, nema vodoravnog prelijevanja. Automatizirani WCAG A/AA
  audit bez nalaza. Svih šest povratnih poveznica iz D06 valjano je.
- Vizualno pregledano svih osam SVG-ova u pregledniku i u stvarnom PDF-u.
  Natpisi ne izlaze iz panela; oznake presjeka, promjera i sila odvojene
  su od susjednih natpisa. Crveni izdvojeni dijagrami prikazuju vektore
  sile, a ne izmišljena hvatišta. Prirubnica P2 ostaje označena A–A;
  presjek 1 nalazi se neposredno prije nje.
- `git diff --check` prolazi. Prijašnje lokalne izmjene U09 sačuvane su.

Za dodatnu provjeru modela jedne pomične ploče korišten je primarni
nastavni izvor [NPTEL — Force exerted by a jet on a moving flat plate](https://archive.nptel.ac.in/content/storage2/courses/112104118/lecture-11/11-4_force_moving_surface.htm).
Izvor služi provjeri modela; Z5 je autorski zadatak s vlastitim podatcima,
zahtjevom energetske provjere i obrazloženjem relativnog masenog dotoka.

Nije ponovljen cijeli objavni CI (17 notebookova, JupyterLite i 72 viewport
slučaja), jer ovaj korak uređuje poglavlje bez objave. Prije sljedećeg
commit/push koraka slijedi objavna provjera prema workflowu.
Autorska procjena raznolikosti, lokalni numerički i geometrijski testovi
te vizualni pregled nisu zamjena za vanjsku stručnu recenziju ili
studentski pilot.

## Dopuna prije objave (22. rujna 2026.)

Za zajednički commit U09/U10 dovršene su objavne provjere: svih 17
notebookova, QR, CFD V&V, JupyterLite build/audit, 24 HTML stranice,
1924 poveznice, 72 viewport/WCAG slučaja i A4 ispis. JupyterLite kernel
u stvarnom pregledniku doseže Python (Pyodide) / Idle. PDF ima 313 A4
stranica; audit i usporedba kopije za preuzimanje prolaze. Zasebni
geometrijski testovi U09/U10 također prolaze. Poslužiteljski CI nakon
pusha provjerava isto stanje na propisanom Pythonu 3.12 i Quarto 1.9.37.
