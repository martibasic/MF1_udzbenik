# Revizija U08 — 22. rujna 2026.

## Matrica prije provedbe

Opseg: šest vježbi i svih sedam SVG skica kanonskog U08. Datoteke `u09_*`
i verifier `verify_u09`, namespace `U09`, pripadaju ovomu poglavlju.
Korisnik posebno zahtijeva fizikalnu i matematičku točnost, pravilne kote,
oznake, neprekinut fluid te uklanjanje lažnih sjena. Postojeći rasporedi,
paleta, tipografija i šrafure ostaju polazište. Omotači se ne uređuju.

| P/Z | Princip, postupak i studentska aktivnost | Odluka i korist | Razina / ID |
| --- | --- | --- | --- |
| P1 | Kontinuitet i pad tlaka u horizontalnom konfuzoru | Zadržati; osnovna usporedba za Z2; ispraviti skalu EGL/HGL, označavanje površina i zaokruživanje tlaka na 523,62 Pa | T2; postojeći |
| P2 | Torricelli, balistika i optimum visine otvora | Zadržati; ispraviti fizičke otvore skice i provjeriti parabole | T2; postojeći |
| P3 | Brzina i tlak u sifonu, apsolutna referenca | Nužan ispravak: B mora biti slobodan izlaz, ne mirna površina donjeg bazena; HGL u C je −3,6 m, a tlačna visina −5,8 m | T2; postojeći |
| P4 | Sifon sa suženjem i putanja mlaza | Zadržati; skica ima prolaz kroz stijenku bazena, pogrešan tlačni broj i neusklađen vrh | T3; postojeći |
| P5 | Diferencijalni manometar, kontinuitet, obrnuti Bernoulli | Zadržati; popraviti račun razlike tlakova i izvedene rezultate, otvorene tlačne priključke i jedinstveno polje ulja | T2; postojeći |
| P6 | Pitot, korekcija gustoće, ograničenje Reynoldsove procjene | Zadržati; nema zasebnog SVG-a | T2; postojeći |
| Z1 | Izravni Torricelli, volumenski i maseni protok | ZADRŽATI; eksplicitno navesti gustoću i kvazistacionarni trenutak | T1; postojeći |
| Z2 | Kontinuitet i pad statičkog tlaka, kao P1 | ZADRŽATI jednostavnu tehniku; eksplicitno navesti idealizaciju | T1; postojeći |
| Z3 | Inverzni Venturi, ponavljanje P5 s manje odluka | ZAMIJENITI silaznim suženjem: rast tlaka unatoč ubrzanju, uloga geodetske visine | T2; `task-tlak-u-silaznom-suzenju` |
| Z4 | Izravni Pitot, stvarno T1 premda nosi T2 | ZAMIJENITI očitanjem izdignutog senzora: hidrostatička korekcija prije Pitota | T2; `task-pitot-s-izdignutim-senzorom` |
| Z5 | Još jedan izravni sifon, ponavljanje P3 i dijela Z6 | ZAMIJENITI odabirom grla iz dvije nejednakosti: minimalni apsolutni tlak i minimalni mjerni signal | T3; `task-odabir-grla-prema-tlaku` |
| Z6 | Sifon, mlaz, intervali gubitaka i odluka o zahtjevima | PREPRAVITI pretpostavke, označiti zadano proširenje modela gubicima i dopuniti tlačni interval | T4; postojeći |

Novi Z3–Z5 autorske su nastavne konstrukcije, `rewrite_status=preradeno`,
`rewrite_level=P3`, `sketch_requirement=obavezna`. Mijenjaju geometriju,
ulaze/izlaze i studentsku odluku. Ostali zadatci ne trebaju rekonstrukciju.
Nove skice također su potrebne zbog više presjeka, visina i referenci tlaka.
Broj i raspodjela mjesta ostaju 2×T1, 2×T2, T3, T4; izvodi teorije ostaju isti.
P1/P3/P5 dobivaju nužne ispravke postojećih računa i fizikalne nedosljednosti
kako bi se tekst, račun i skica uskladili s korisnikovim zahtjevom za točnost.
Opis povezanog notebooka ispravlja se jer je ranije obećavao interaktivni
EGL/HGL prikaz koji taj notebook ne sadrži.

Staro → novo (stari ID-jevi ostaju span aliasi, ne novi naslovi zadataka):

- `task-u09-idealna-venturijeva-cijev-za-vodu-ima-ulazni` → Z3 gore.
- `task-u09-pitotova-cijev-uronjena-je-u-vodeni-tok` → Z4 gore.
- `task-u09-idealni-sifon-prazni-otvoreni-spremnik-razlika-razina` → Z5 gore.

## Plan provjera

Neovisno ponovno računanje i energetske bilance, granični slučajevi,
intervalni kutovi i provjera nejednakosti za odabir grla. Provjeriti stvarnu
SVG geometriju, rubove fluida, položaje kota, parabole i tlačne visine, uz
zaseban vizualni pregled. Uskladiti D03, generatorski D06 i manifest; provjeriti
povezani Venturi notebook, HTML, povratne poveznice i nativni PDF.

## Provedeno

Z1/Z2 zadržavaju temeljne računske postupke. Novi Z3 pokazuje porast tlaka
7,680 kPa pri ubrzanju u silaznom suženju; spuštanje od 2 m nadmašuje
porast brzinske visine. Z4 prije Pitotove jednadžbe prenosi očitanje senzora
1,20 m prema dolje: stagnacijski tlak 35,772 kPa manometarski, brzina
6,288 m/s, nasuprot pogrešnih 4,000 m/s bez hidrostatičke korekcije.
Z5 iz oba kriterija određuje 43,183–52,328 mm i odabire uložak 50 mm;
rubovi su provjereni i izvornim nejednakostima, bez oslanjanja na zaokruženje.

Z6 zadržava intervalni problem, s izričito zadanim proširenjem bilance
gubitcima i zajamčenim rasponima. Protok je nominalno 15,869 L/s i pripada
intervalu 14,692–17,384 L/s. Tlak u vrhu nominalno je 65,919 kPa apsolutno,
a interval je 59,117–70,777 kPa. Tlačni uvjet prolazi, dok zadani protok
nije zajamčen. U PDF pregledu otkriveno je da generator D06 skraćuje predugi
odgovor prije zaključka o uvjetima; odgovor je sažet ispod postojećeg limita
od 500 znakova, uz očuvanje svih brojčanih rezultata i kriterija.

P3 sada ima otvoreni izlaz B i nezanemarivu brzinu u B; manometarska tlačna
visina u C ostaje −5,8 m, dok je HGL pravilno −3,6 m prema površini A.
P5 daje Δp = 22,478634 kPa, v1 = 1,856071 m/s, v2 = 7,424286 m/s i
Q = 5,247919 L/s. Raniji rezultat 22,74 kPa prolazio je preširoku toleranciju
od 2 %; za taj račun sada se provjerava precizni iznos. Notebook sadrži
izvršivu neovisnu provjeru istog idealnog primjera; odvojeni postojeći pokus
nesigurnosti za vodu ostaje jasno označen drugim podatcima.

Svih sedam SVG-ova je dorađeno. Zadržane su dimenzije njihovih okvira i
osnovna podjela panela. Otvori sifona i sapnica nemaju čepove, osi fluida
i cijevi su iste, ulaz P4 je unutar bazena, a sifoni prelaze iznad krutih
rubova. Isti fluid koristi zajedničku gradaciju bez prozirnih preklopljenih
slojeva. U P5 živa i ulje imaju fizička sučelja te otvorene mjerne priključke;
promjeri i razlika razina žive imaju istu duljinsku skalu. P1 prikazuje stvarni
omjer brzinskih visina; P2/P4/Z6 koriste provjerene parabole s vodoravnom
početnom tangentom. Uvećani promjeri sapnica i sifona izričito su označeni.

## Izvršene provjere

- `verify_u09`: 65 rezultata (54 brojčane usporedbe, 11 invarijanti), bez
  pada. `verify_all`: 1166 rezultata, od toga 1011 brojčanih usporedbi i
  155 invarijanti, uz 22 dodatne fizikalne provjere; 90/90 ugovora bez rupa.
- `check_u08_sketch_geometry.py`: 133 geometrijske provjere prolaze.
  Svih sedam SVG-ova zasebno je pregledano; tekst ostaje unutar okvira.
- Notebook `u09_venturi.ipynb` izvršen u čistom kernelu; idealni primjer
  i postojeći pokus nesigurnosti prolaze. Početni dodatni import standardne
  biblioteke zamijenjen je već podržanim NumPyjem radi pregledničkog ugovora.
- Strukturni audit: 87 primjera, 90 vježbi; raspodjela U08 ostaje
  T1/T1/T2/T2/T3/T4. Normalizacija, Typst audit, D06 i manifest prolaze.
- Puni HTML render; pregled U08 na 320/768/1440 px, bez vodoravnog
  prelijevanja, 12 sklopivih blokova dostupnih tipkovnicom, jedinstveni ID-jevi,
  sva tri stara aliasa i šest povratnih poveznica D06. Automatski WCAG A/AA
  pregled stranice U08 prolazi.
- Puni PDF render i audit: 309 A4 stranica. Pregledane skice i matematički
  zapisi, osobito P3 na 154, P5 na 158, vježbe na 160–161 i ključ na 298–299.
  Konačni ključ sadrži potpuni zaključak Z6. PDF kopiran u `_site/downloads/`.
- Audit stranice: 24 HTML stranice, 212 slika, 1918 poveznica i 434 sklopiva
  bloka. Sadržaj P2/P4/P6 uspoređen s početnom kopijom i ostao isti; QMD
  omotači imaju samo prethodno zatečene razlike završetaka redaka, bez
  sadržajnog diffa.

Ograničenja: crteži su shematski; gdje su promjeri radi čitljivosti uvećani,
to je napisano na slici. Duljine vektora ne predstavljaju zajedničku skalu
svih scena. Fizikalni zaključci vrijede uz zadane idealizacije; didaktička
raznolikost ostaje autorska procjena, a ne posljedica prolaza CI-ja.
Postojeća Typst upozorenja `times.circle` iz U10 ostaju. Puni JupyterLite
build, svih 17 notebookova i audit svih stranica na svim širinama pripadaju
sljedećoj provjeri prije objave. U ovoj reviziji nisu rađeni commit ni push.

### Dopuna prije objave

Na korisnikov zahtjev za commit i push izvršeno je svih 17 notebookova u
čistim kernelima; svi prolaze. Puni JupyterLite build i audit prolaze
(17 notebookova, četiri proširenja, Python/Pyodide). Ponovljene brojčane,
geometrijske i strukturne provjere prolaze, kao i provjere CFD paketa,
QR kodova, generiranog ključa te poveznica renderiranog udžbenika.
