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


## Revizija 12. 10. 2026. (provedba recenzentskih nalaza)

Izvor: stručna recenzija od 12. 10. 2026. i brief koordinatora. Opseg obuhvaća kanonski izvor, `verify_u11.py` (U11), skice `u11_val1_mlaz_na_plocu.svg`, `u11_val3_koljeno_reakcija.svg` i `u11_vjezbe_skice.svg`, novu skicu `u11_val_rotirajuca_mlaznica.svg`, checker `check_u10_sketch_geometry.py` i bilježnicu `u11_sila_na_koljeno.ipynb`. Prema planu knjige poglavlje dobiva jedan riješeni primjer više (6 → 7).

### Matrica zamjena

| P/Z | Stari ID i stanje | Odluka | Razina | Završni ID | Kontrolni rezultat | Status |
| --- | --- | --- | --- | --- | --- | --- |
| P1 | `ex-u11-mlaz-vode-na-mirnu-ravnu-plocu-t2`; trivijalan, klon Z1 | ZAMIJENITI Peltonovom lopaticom u gibanju (pomični KV, θ = 165°, energetska provjera, kolo, u = v/2) | T2 | `ex-peltonova-lopatica-u-gibanju`, slika `fig-peltonova-lopatica-u-gibanju` (ista datoteka) | ṁ_rel 35,3 kg/s; F 1248 N; P 14,98 kW; kolo 2080 N i 24,96 kW; P_max 26,0 kW | provedeno |
| P2 | `ex-u11-kalibracijska-mlaznica-na-prirubnici-t2` | ZADRŽATI; konvencija R_{st→f} | T2 | isti | nepromijenjen | provedeno |
| P3 | `ex-u11-servisno-koljeno-na-sidrenom-nosacu-t2`; ξ ≈ 3,5 | PREPRAVITI p_M2 s 18 na 43 kPa (ξ ≈ 0,34); dodan brojčani β (1,02 i 4/3) | T2 | isti | F = (1402, −665) N; 1,55 kN | provedeno |
| P4 | `ex-u11-t-racva-na-sidrenoj-konzoli-t3` | PREPRAVITI lanac zaokruživanja | T3 | isti | v1 4,48; 891/503 N; 1023 N | provedeno |
| P5 | `ex-u11-y-racva-s-mjerenom-reakcijom-konzole-t4` | PREPRAVITI konvenciju R; p/(ρg) | T4 | isti | 912 N | provedeno |
| P6 | `ex-u11-sila-na-koljeno-tlacnog-voda-male-hidroelektrane` | PREPRAVITI: θ, vektorska bilanca, impulsna funkcija I | T2 | isti | 9,83 kN; 60° | provedeno |
| P7 | novo | DODATI rotirajuću mlaznicu za pranje tanka | T2 | `ex-rotirajuca-mlaznica-pranje-tanka`, `fig-rotirajuca-mlaznica` | w 17,8 m/s; M 11,4 N m; P 71 W; M0 12,4 N m; n_max ≈ 680 min⁻¹ | provedeno |
| Z1 | `task-u11-vodeni-mlaz-promjera-izlazi-iz-sapnice-brzinom` | ZAMIJENITI potiskom vodomlaznog pogona | T1 | `task-vodomlazni-potisak-broda` | ṁ 1845 kg/s; F_T 25,8 kN; P_T 465 kW; η 0,72 | provedeno |
| Z2 | `task-u11-mlaz-vode-udara-okomito-na-nepomicnu-plocu` | ZAMIJENITI propelerom kao aktuatorskim diskom | T1 | `task-propeler-aktuatorski-disk` | v_d 7,00 m/s; F_T 180 kN; P_T 1,08 MW; η_i 0,857 | provedeno |
| Z3 | `task-u11-horizontalno-koljeno-zakrece-tok-vode-za-bez`; ξ ≈ 5,5 | PREPRAVITI p_M2 sa 150 na 175 kPa (ξ ≈ 0,91) | T2 | isti | (1,500, −1,460) kN; 2,093 kN | provedeno |
| Z4–Z6 | `task-moment-ekscentricnog-mlaza`, `task-mlaz-na-pomicnu-plocu`, `task-u11-vodoravna-y-racva-prima-vodu-kroz-ulaz` | ZADRŽATI | T2/T3/T4 | isti | nepromijenjeni | provedeno |

Stari ID-jevi Z1 i Z2 ostaju kao `<span id>`.

### Teorija, notacija, skice i provjere

- Teorija:
  - `.mf1-temelj` za moment količine gibanja (`eq-moment-kolicine-gibanja`);
  - mlazni pogon (`eq-potisak-mlaznog-pogona`);
  - `.mf1-izvod` aktuatorskog diska;
  - `.mf1-granica-modela` s četiri stavke.
- Blok „Dublje” skraćen je na polovicu. Uklonjene su jednadžbe 02–04 i 06; nemaju vanjskih referenci.
- Notacija: v⃗ posvuda (u⃗ samo u „Dublje”); kut θ; F⃗, R⃗_{st→f} i R⃗; I = pA + ṁv; „u ovom poglavlju”.
- Duplicirano pitanje u „Provjeri sebe” zamijenjeno je novim.
- Skice:
  - P1 preuređena u Peltonovu lopaticu;
  - nova `u11_val_rotirajuca_mlaznica.svg` (viewBox 0 0 520 420);
  - paneli Z1 i Z2 u istim okvirima;
  - natpisi p_M2 = 43 kPa (P3) i 175 kPa (Z3).
- `check_u10_sketch_geometry.py` sada provjerava devet SVG-ova. Rezultat: PASS.
- `verify_u11.py`: 115/115. Stari P1/Z1/Z2 ID-jevi uklonjeni su.
- Bilježnica:
  - Z3 sada koristi 175 kPa, a zlatne komponente su (1499,616; −1460,346);
  - oznaka kuta je θ;
  - izlazi ćelija su ispražnjeni (izvršava koordinator).
- Nova SVG datoteka nema unos u `assets/print-layouts.json` (dodaje koordinator).

## Revizija 19. 10. 2026. — didaktičko pojačanje (odobreno u razgovoru)

Zahtjev autorice: zadatci su prelagani i prečesto ponavljaju riješene primjere; kroz poglavlja uvesti po koji zahtjevniji zadatak ili zakomplicirati primjer, ne dodavati tekst. Zahvat unutar šest mjesta Z1–Z6 i raspodjele T1, T1, T2, T2, T3, T4; broj primjera ostaje. Stari ID-jevi zamijenjenih zadataka ostaju kao prazni `<span>` aliasi.

| Mjesto | Staro | Novo | Razina | Didaktička korist |
| --- | --- | --- | --- | --- |
| Z3 | Koljeno 90° u tlocrtu (ponavljanje P3) | Koljeno u okomitoj ravnini s težinom (`task-koljeno-u-okomitoj-ravnini-tezina`): $D=200$ mm, $Q=0{,}090$ m³/s, $p_{M1}=150$ kPa, $\Delta z=0{,}40$ m, $V=0{,}030$ m³, $\xi=0{,}30$: $p_{M2}=144{,}9$ kPa, $F_x=+4{,}97$, $F_z=-5{,}10$, $|F|=7{,}12$ kN; težina 5,8 %; vodoravni model $F_z=-4{,}97$ kN | T2 | Volumne sile i pad tlaka s visinom ulaze u bilancu količine gibanja; student uspoređuje s vodoravnim modelom i odlučuje kada je težina zanemariva. |

Skica Z3: geometrija zadržana, kota $\Delta z$, strelica $g$, os $z$, $p_{M2}=?$. `verify_u11.py`: `zadatak_3`, `U11.Z3.weight_and_elevation_terms`. D03 §10 dopunjen.

Prošlo nakon zahvata: pripadni `verify_*`, `verify_all`, `audit_publication`, `qa_audit`, `audit_sketch_design` (s `check_u*_sketch_geometry`), `audit_print_layouts`; D06 i manifest regenerirani generatorima, `print-layouts.json` hash obnovljen. Vizualna provjera skice obavljena headless renderom u PNG. Didaktička procjena je autorska; studentski pilot nije proveden.
