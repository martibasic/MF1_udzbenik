# Pregled svih skica U03 — 22. rujna 2026.

**Status nakon odobrenog popravka:** nalazi ispod opisuju početno stanje.
Ispravci svih osam uključenih skica provedeni su; završna evidencija nalazi
se u [reviziji U03](revizija_u03.md#popravak-svih-skica-nakon-pregleda).
Izvorni nalaz ostaje sačuvan radi usporedbe.

## Opseg i metoda

Pregledano je osam SVG datoteka koje stvarno uključuje aktualni kanonski
izvor `source/u03_hidrostaticka_raspodjela_tlaka_i_manometrija.md`, uključujući
svih šest panela Z1–Z6. QR kod i stare, neuključene ilustracije nisu fizikalne
skice aktualnog poglavlja i nisu predmet ovog nalaza.

Uspoređeni su prikaz u Edgeu, SVG koordinate i redoslijed crtanja, tekst
primjera/zadataka te ponovno izračunane vrijednosti. Izvorne skice i sadržaj
knjige u ovom pregledu nisu mijenjani. Evidencija opisuje zatečeno stanje,
uključujući prethodne lokalne revizije U03/U04.

**Zaključak: skice nisu sve fizikalno i grafički dosljedne.** Potrebni su
popravci povezanosti manometara, slaganja slike s modelom, vektorskog
dijagrama i prikaza balastnog tanka. Suženja i gradijenti zaseban su problem:
u hidrostatici bez kapilarnosti promjena promjera sama ne mijenja bilancu
tlaka, ali nenamjerno suženje ne treba prikazivati kao dio zadanog uređaja.

## 1. Uvodni pregled — `u03_fig_uvod_pregled.svg`

**Potrebna fizikalna i grafička dorada.**

- U gornjem srednjem panelu puna crta od `(502,146)` do `(524,146)`
  zatvara vrh lijevog kraka U-manometra. Plinski spoj dolazi iznad te
  crte; treba izvesti stvarno otvoreno koljeno, bez pregrade između plina
  spremnika i plina nad živom (redak 140).
- U donjem srednjem panelu donji rubovi dvaju pravokutnika vodova ostaju
  preko otvora manometarskih ogranaka na `y=318` (retci 169 i 172).
  Ogranci trebaju biti otvoreni u glavne vodove, bez pune poprečne crte.
- Trokut tlaka počinje nulom na površini, ali nosi oznake apsolutnog tlaka
  `p0 = patm` i `p = p0 + rho*g*h`. Trokut može predstavljati manometarski
  prirast `pM = rho*g*h`; apsolutni tlak zahtijeva nenulti pomak za `p0`.
  Treba uskladiti naziv i oznake dijagrama (retci 67, 245–253).
- Gradijenti žive i vode ponovno počinju na svakom pravokutniku. To stvara
  svijetle spojeve, a vodoravni dijelovi cijevi uži su od okomitih bez
  posebnog razloga. Upotrijebiti kontinuiranu domenu i zajedničku ispunu.
- Predznaci dviju manometarskih formula odgovaraju prikazanim razlikama
  razina, uz isti radni fluid i jednaku visinu priključaka za donji panel.
  Kota `h` i kota razlike razina postavljene su na odgovarajuće razine.

## 2. P1 — `u03_fig_zatvoreni_spremnik_tlak.svg`

**Osnovna fizika i kotiranje dobri; potrebna manja dorada.**

- Kota `h` ide od vode na `y=170` do osi priključka na `y=310`, u skladu
  s naznačenom vertikalnom skalom 100 SVG jedinica/m i dubinom 1,40 m.
  Priključak je otvoren kroz bočnu stijenku; nisam našao punu pregradu.
- Ispuna vode ponovno započinje u uskoj priključnoj cijevi. Zbog toga
  priključak izgleda svjetlije od vode na istoj visini u spremniku.
- Točan račun iz zadanih podataka daje `pA = 132506,532 Pa` i
  `pA,m = 31706,532 Pa`, a ne 132512 Pa i 31712 Pa (retci 148–152).
  Zaokruženi rezultati 132,5 kPa i 31,7 kPa ostaju točni. Isti sitni
  aritmetički nesklad postoji u kanonskom tekstu pa ga treba uskladiti.
- Strelica `+rho*g*h` objašnjava računski silazak, ne strujanje vode;
  postojeći natpis to razjašnjava.

## 3. P2 — `u03_val1_diferencijalni_manometar.svg`

**Visoki prioritet: nacrtani uređaj ne odgovara objavljenoj bilanci.**

- Put od `p1` do `p2` na desnoj strani završava usponom kroz morsku vodu:
  granica je na `y=241`, a `p2` na `y=202`. Formula i donji opis navode
  silazak kroz morsku vodu, odnosno doprinos `+rho_mv*g*h4` u hodu tlaka.
  Strelica u desnom vodu također pokazuje suprotno od završnog hoda prema
  `p2` (retci 96, 131, 145–146, 198).
- Nacrtana su dva odvojena živina U-stupca i zračni most. U desnom U-stupcu
  obje granice žive imaju istu visinu; njegov neto doprinos je nula. To nije
  put tekućina opisan jednostavnim redoslijedom u tekstu. Geometriju treba
  konstruirati iz zadanog hoda, a ne samo promijeniti smjer strelice.
- Slijedimo li kotirane iznose i stvarno nacrtani uspon u morskoj vodi,
  dobivamo `p1-p2 = g*(13600*0,10 + 1,2*0,70 + 1035*0,40 - 1000*0,60)`
  odnosno **11,525 kPa**, umjesto objavljenih približno 3,40 kPa.
- Za objavljeni tekst formule daju 3394,26 Pa bez zraka i 3402,5004 Pa sa
  zrakom. Razlika je 8,2404 Pa, odnosno oko 0,242 %. Prikazanih 3394 i
  3402 Pa valja ujednačiti po pravilu zaokruživanja; to je manji problem
  od pogrešnog predznaka koji proizlazi iz slike.
- Kota `h2` ima samo 7 SVG jedinica visine, uz velike vrhove strelica;
  strelice se preklapaju. Donja koljena imaju uočljive ponovne početke
  gradijenta, koji izgledaju kao unutarnje trake ili dodatni slojevi.

## 4. P3 — `u03_ch1_zatvoreni_spremnik_ulje_ziva.svg`

**Visoki prioritet: pregrade preko priključaka i nedosljedne kote.**

- Puna siva stijenka `x=254..258` prolazi preko vodenog priključka
  `y=240..252`, a stijenka `x=452..456` preko uljnog priključka
  `y=209..221`. Crtaju se nakon vodoravnih ispuna pa presijecaju oba
  prolaza u manometar (retci 189 i 194).
- Kote `a` i `b` polaze od gornjih rubova cijevi (`y=240`, `209`), dok su
  tlačne točke u osima na `y=246`, `215`. Kote moraju polaziti od tlačnih
  točaka do razdjelnica, ne od vanjskog ruba priključka (retci 277–287).
- Sve zadane visine zajedno zahtijevaju da točka 2 bude 0,13 m iznad
  točke 1, a slobodna površina ulja 0,12 m ispod slobodne površine vode:
  `z2-z1 = Delta_h+b-a = 0,13 m`;
  `zB-zA = 0,13+h2-h1 = -0,12 m`.
  Slika obje slobodne površine postavlja na isto `y=160`, što tu vezu
  pogrešno sugerira. Različite visine nisu nacrtane dosljednom skalom.
- Cijev mijenja unutarnju širinu približno 12 → 24 → 16 SVG jedinica.
  Nema zadane redukcije promjera. Svaki pravokutnik vode, ulja i žive ima
  vlastiti početak gradijenta, što proizvodi izrazite lažne svijetle trake.
- Bilanca i glavni rezultati u desnom panelu odgovaraju tekstu:
  `p2=105911,175 Pa`, `p1=129067,68 Pa`, `pG=121219,68 Pa`,
  `pC=132991,68 Pa`. Treba popraviti prikaz, zadržavajući taj problem.

## 5. Spojene posude i efektivno polje — `u03_balans_tlaka_i_geff.svg`

**Lijevi model valjan; desni vektorski dijagram pogrešan.**

- Lijevo su iste površinske reference tlaka i jednaka dubina A/B ispravno
  povezane s `pA=pB=p0+rho*g*h`. Donji spoj otvoren je prekrivanjem dijelova
  stijenki ispunom vode. Međutim, zaseban gradijent u spoju visine 20
  jedinica stvara izrazito svijetlu traku između tamnijih dna posuda.
- Nagib površine desno iznosi `100/270`, odnosno oko **20,32°**.
  Vektori imaju omjer `a/g=52/66`, odnosno oko **38,23°**. Zato nacrtani
  `g_eff` nije okomit na površinu, premda natpis tvrdi upravo to.
  Skalarni produkt smjera površine `(270,100)` i rezultante `(-52,66)`
  jest `-7440`, a za okomitost bi morao biti nula (retci 101, 125–129).
- Vektorski zbroj nacrtanih `g` i `-a` jest interno točan, ali ih treba
  uskladiti s površinom i s oba označena kuta alfa.
- Kutni lukovi nisu uredno usidreni na odgovarajuće pravce. Donji okvir
  prekriva nacrtanu strelicu ubrzanja, a natpis ubrzanja preklapa formulu
  (retci 166 i 178). Pozivanje na „CH1” također je stara oznaka sadašnjeg P3.

## 6. P4 — `u03_fig_pumpa_usis.svg`

**Visoki prioritet: prikaz toka proturječi statičkom modelu.**

- Tekst izričito razmatra `Q=0` i zanemaruje brzinsku visinu i gubitke.
  Na slici su brojne strelice toka kroz usis i tlačni vod te legenda
  „smjer strujanja”. Treba prikazati statički stupac ili jasno odvojiti
  prikaz rada pumpe od izračunane statičke granice.
- Tamni pravokutnik na ulazu pumpe (`x=186..220`, `y=158..166`) prelazi
  preko cijelog usisnog presjeka i izgleda kao čep. Presjek priključka
  mora biti otvoren ili kućište jasno označeno kao shematski simbol.
- Usisni otvor je uronjen, no odmak od dna iznosi samo oko 5 SVG jedinica
  uz širinu ulaza oko 26 jedinica. Bez potrebe se sugerira jako prigušen
  ulaz. Isprekidana crta preko cijelog otvora dodatno izgleda kao mrežica.
- Kota `H` ispravno povezuje slobodnu površinu i točku usisa. Odvojene
  ispune spremnika i cijevi stvaraju granicu boje unutar istog ulja.
- Točan račun daje `pM=-20483,28 Pa`, `paps=80816,72 Pa`,
  `Hmax=11,84576 m`. Zaokruženi -20,5 kPa, 80,8 kPa i 11,8 m dobri su;
  međurezultati -20,49 kPa i 80810 Pa nisu točno izvedeni iz zadanih ulaza.

## 7. P5 — `u03_fig_balastni_tank.svg`

**Visoki prioritet: morski tlak nacrtan na stijenci koja nije uz more.**

- Vanjski bok broda je na `x=130`, a lijeva stijenka tanka/prozor na
  `x=200`. Između je prikazan suh prostor trupa. Strelice morskoga tlaka
  ipak djeluju na taj unutarnji prozor. Za zadani model prozor mora biti
  na zajedničkoj stijenci tanka i vanjske oplate, izravno između mora i
  balasta. Sadašnja slika predstavlja drugu fizikalnu situaciju.
- Tlakovi označeni kao tlakovi „na dnu” prikazani su vodoravnim strelicama
  uz bok (`y=378`). Na vodoravno dno tlak mora djelovati okomito: more
  odozdo prema gore, balast iznutra prema dolje. Neto opterećenje dna je
  prema unutrašnjosti, tj. prema gore; vodoravni simbol nije dovoljan.
- Odzračnik je nacrtan kao puni sivi stup s kapom i završava pod palubom,
  bez jasnog otvorenog prolaza kroz krov tanka. Atmosferski rubni uvjet
  treba pokazati otvorenim spojem s atmosferskim prostorom.
- `Tg` i `hp` imaju dosljedne razine. Zadana skala 36 jedinica/m daje
  visinu 5 m kao 180 jedinica, ali voda je od `y=214` do `386`, tj. 172
  jedinice. Kota `Ht` prati donju plohu krova, dok je nominalni vrh tanka
  na `y=206`. Visinu stupca vode i debljinu krova treba dosljedno razdvojiti.
- Glavni rezultati 85,5; 49,1; 36,4; 35,9 kPa odgovaraju tekstu.
  Vanjski tlak kod prozora iznosi 65,359125 kPa pa zaokruženje na jednu
  decimalu treba biti 65,4 kPa, ne 65,3 kPa. Neto tlak je 35,929125 kPa.

## 8. Z1–Z6 — `u03_vjezbe_skice.svg`

| Panel | Fizika i kote | Preostali problem |
| --- | --- | --- |
| Z1 | Dubina ide od površine do A; tlakovi i otvoren spremnik ispravni | Voda doseže `y=294`, a unutarnji pod je `y=292`: ispuna ulazi 2 jedinice u šrafirano dno. Jedinica m odvojena je u novi red uz rub panela. |
| Z2 | Ispravno: kota do mjerne točke A, ne do samog dna; plinski tlak G i razlika tlakova su usklađeni | Nije nađen značajan fizikalni ili geometrijski nedostatak. |
| Z3 | Ispravne razdjelnice, otvoreni krak viši, kote a i Delta_h na odgovarajućim visinama | Donji vod ima visinu 8 jedinica, a krakovi oko 20–22: izraženo nenamjerno suženje (retci 84–87). |
| Z4 | Ulje iznad vode, h_u+h_w=H; granica nije kruta pregrada; omjer slojeva približno odgovara rješenju | Nije nađen značajan fizikalni ili geometrijski nedostatak. |
| Z5 | Viša površina na strani podtlaka; siva ispuna izričito označuje jednu od alternativa, ne tri sloja | Donji spoj ima visinu 8 jedinica prema širini krakova 20; suženje nije zadano (retci 149–151). |
| Z6 | A i granica voda–Hg na istoj visini; h1:h2 i Delta_h dosljedni; niža živa uz spremnik | Obris debljine 7 jedinica uz razmak dviju crta 8 ostavlja prolaz od približno 1 jedinice. Glavni krak ima prolaz oko 11, a donji spoj oko 5. Ispuna vode u priključku ponovno počinje gradijentom i izgleda kao drugi fluid (retci 181–188). |

U Z3/Z5/Z6 nisam našao potpunu poprečnu pregradu poput onih u P3, ali
prolazi nisu nacrtani ujednačeno. Posebno je suženje u Z6 pri smanjenju za
tiskano izdanje gotovo nečitljivo. Natpis „skice nisu u mjerilu” ne rješava
nenamjerni čep, pogrešan redoslijed fluida ili pogrešnu okomitost vektora.

## Provjere i prioritet popravaka

- `python tools/verify_u03.py`: 59 uspješnih provjera, bez FAIL-a.
  To potvrđuje račun unutar zadanih tolerancija; verifier ne čita SVG
  geometriju i ne otkriva sitne aritmetičke razlike unutar tolerancije.
- Svih osam SVG-ova otvoreno je i vizualno pregledano. Nema teksta izvan
  vanjskih SVG granica; to ne isključuje unutarnja preklapanja poput onoga
  u dijagramu efektivnog polja.
- Ručno su provjereni put kroz fluide, položaji razdjelnica, polazišta kota,
  širine prolaza i smjerovi opterećenja. Brojke i vektorski kutovi iz ovog
  izvještaja ponovno su izračunani neovisno o slikama.
- Knjiga nije ponovno renderirana jer pregled nije mijenjao njezine izvore.

Redoslijed popravaka: (1) P2/P3 i zatvoreni spojevi uvodnog pregleda;
(2) kontakt mora i tanka te smjer sila na dnu; (3) statički prikaz pumpe i
okomitost efektivne gravitacije; (4) ujednačeni presjeci Z3/Z5/Z6 i
kontinuirane ispune; (5) polazišta kota, čitljivost i sitna zaokruživanja.
Sačuvati postojeću paletu, raspored panela i tipografiju. Za isti fluid
upotrijebiti jednu spojenu ispunu ili zajednički koordinatni gradijent,
a stijenke oblikovati s pravim otvorima umjesto naknadnih prekrivanja.
