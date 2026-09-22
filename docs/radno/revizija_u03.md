# Revizija zadataka za vježbu U03 — 22. rujna 2026.

## Opseg i analiza prije provedbe

Polazište je commit `51b21b9`. Mijenjaju se samo potrebni zadatci Z1–Z6,
njihova zajednička skica i povezani kontrolni izvori. Ostaje raspodjela
T1, T1, T2, T2, T3, T4. Postojeće lokalne promjene omotača U02/U11 čuvaju se.

| Primjer | Princip i postupak | Aktivnost, razina i preklapanje |
| --- | --- | --- |
| P1, zatvoreni spremnik | p = pG + ρgh; zbrajanje i promjena reference | Izravni račun T1; stari Z2 gotovo ponavlja cijeli postupak |
| P2, slatka/morska voda i Hg | Segmentni hod po stupcima i doprinos zraka | T3, izbor zanemarenog člana; Z3/Z4 vježbaju jednostavnije manometre |
| P3, vodeni/uljni spremnik i Hg | Više spojenih stupaca, povrat na tlak plina | T3, lanac tlakova; sličnost sa starim Z5 i nominalnim dijelom Z6 |
| P4, usis uljne pumpe | Uspon kroz fluid, apsolutni tlak i granica pri tlaku pare | T2, predznak i granica statičkog modela; dio vakuumske tehnike starog Z5 |
| P5, balast | Razlika unutarnjih i vanjskih tlakova | T2, geometrija dubina i smjer opterećenja; nema potrebe za još jednom preslikom |
| P6, senzori u vodovodu | Korekcija tlaka zbog visine, ekvivalentni stupac | T2, tumačenje odstupanja uz ograničen zaključak o uzroku |

P1–P6 i teorija ostaju nepromijenjeni. Raznolikost se povećava obrnutim
računom razine, rekonstrukcijom slojeva i izborom mjernog fluida prema dvama
zahtjevima, uz zadržavanje osnovnog računa i T4 s nesigurnošću.

| Mjesto | Postojeća uloga | Odluka i nova didaktička korist | Razina | ID i veze | Status prije provedbe |
| --- | --- | --- | --- | --- | --- |
| Z1 | Otvoreni spremnik, izravni ρgh | ZADRŽATI temeljnu samostalnu vježbu i dvije reference tlaka | T1 | Stari ID; SVG, verifier, D06 | Odabrano |
| Z2 | Zatvoreni spremnik kao P1 | ZAMIJENITI razinom iz razlike tlakova; tlak plina se poništava | T1 | `task-razina-vode-iz-razlike-tlakova` | Odabrano |
| Z3 | Otvoreni U-manometar ulje/Hg | ZADRŽATI; izričito zadati koji je stupac žive viši | T2 | Stari ID; SVG, verifier | Odabrano |
| Z4 | Diferencijalni manometar kao pojednostavljen P2 | ZAMIJENITI rekonstrukcijom debljine sloja ulja; geometrijska veza i provjera izvedivosti | T2 | `task-debljina-sloja-ulja-iz-tlaka` | Odabrano |
| Z5 | Dva rutinska računa vakuumskog spremnika | ZAMIJENITI izborom fluida U-manometra prema visini stupca i pogrešci očitanja; stvarna odluka T3 | T3 | `task-izbor-manometra-za-podtlak` | Odabrano |
| Z6 | Apsolutni senzor, intervali i skala | PREPRAVITI neodređenu geometriju; zadržati kvalitetan izbor senzora i brojeve | T4 | Stari ID; SVG, verifier, D06 | Odabrano |

Z2/Z4/Z5: autorske nastavne konstrukcije, `rewrite_status=preradeno`,
`rewrite_level=P3`; mijenjaju se scenarij/geometrija, ulazi, traženi izlazi
i studentska odluka (najmanje 3/5). Izvor ideje je ova didaktička analiza,
ne preuzeti vanjski zadatak. Z1/Z3: `rewrite_status=nije_potrebno` uz
preciziranje Z3. Z6 je ispravak fizikalne određenosti, ne nova konstrukcija.

## Geometrija, poveznice i neovisne provjere

Stari HTML ID-jevi Z2/Z4/Z5 ostaju kao prazni span elementi neposredno ispred
novih naslova; vode na zamjenska mjesta. Povijesni sadržaj ostaje u Gitu.

| Stari ID | Novi ID |
| --- | --- |
| `task-u03-u-zatvorenom-spremniku-iznad-vode-vlada-manometarski` | `task-razina-vode-iz-razlike-tlakova` |
| `task-u03-diferencijalni-manometar-ispunjen-zivom-spaja-dvije-tocke` | `task-debljina-sloja-ulja-iz-tlaka` |
| `task-u03-vakuumski-spremnik-spojen-je-na-otvoreni-zivin` | `task-izbor-manometra-za-podtlak` |

`sketch_requirement`: Z1 preporučena; Z2/Z3/Z4/Z5/Z6 potrebna radi točaka
mjerenja, razdjelnica i predznaka. Zadržavaju se šest panela, postojeći
svijetli okviri, plave oznake zadataka, šrafure, gradijenti i tipografija.
Tlak je skalarna oznaka, bez izmišljenih vektora protoka u mirujućem fluidu.

U starom Z6 račun implicitno pretpostavlja da je dodir vode i žive na
visini priključka, dok skica prikazuje niži dodir bez zadane visinske razlike.
Ta je pretpostavka sada izričita i skica je mora poštovati. Time ostaju stari
brojčani rezultati, ali nestaje nedostajući hidrostatički član. Rasponi ±
znače zadane zajamčene granice, a ne standardne nesigurnosti.

Neovisne provjere: Z1 pomak tlakovne reference; Z2 poništavanje zajedničke
promjene tlaka plina; Z3 hod od atmosfere do priključka; Z4 ponovno slaganje
visina i tlakova te granice čistog ulja/vode; Z5 visinska i tlačna nejednakost
za svaki fluid, uz promjenu odluke kada se promijene ograničenja; Z6 svih
16 rubnih kombinacija četiriju ulaza i zahtjev rezerve skale.

Notebook `u03_diferencijalni_manometar.ipynb` zaseban je numerički pokus za
priključke na istoj visini (Δh = 42 mm), bez pozivanja na zamijenjeni Z4.
Ostaje primjeren teoriji i ne mijenja se. D03 treba uskladiti s novim tipičnim
pogreškama; D06 i manifest obnavljaju se isključivo generatorima.

## Provedeno i kontrolni račun

Sve odluke iz matrice provedene su. Z1 i Z3 čuvaju problem i rezultat, a Z3
dobiva izričit položaj više razine žive. Z2/Z4/Z5 zamijenjeni su uz očuvane
stare HTML poveznice. Z6 sada izričito navodi geometriju koju pretpostavlja
njegov račun. U zajedničkom uvodu zadani su g, mirovanje, stalne gustoće,
zanemarivi kapilarni/plinski doprinosi i sintetičko podrijetlo očitanja.

- Z2: h = 1,79972585 m; zajedničko povećanje tlakova za 5 kPa ne mijenja
  njihovu razliku 17,62 kPa.
- Z4: hu = 0,601427 m, hw = 0,898573 m, tlak granice 5015 Pa. Granični
  tlakovi za samo ulje/vodu iznose 12507,75 i 14715 Pa; nagibi 8338,5 i
  9810 Pa/m. Tlak ostaje kontinuiran kroz ravnu granicu bez krute pregrade.
- Z5: potrebne razlike razina za ulje/vodu/Hg iznose 0,711187 / 0,612846 /
  0,0449721 m, a granice pogreške 8,4366 / 9,79038 / 133,416 Pa. Jedino
  voda zadovoljava oba uvjeta; pgas,aps = 92,6 kPa. Promjena visinskog
  odnosno tlačnog ograničenja u verifikatoru mijenja prihvatljive izvedbe.
- Z6: pG = 122,553613 kPa, pC = 135,281107 kPa, pmax = 136,045843 kPa;
  potrebna puna skala = 142,848135 kPa. Kontrolni rezultat skale preciziran
  je sa 142,9 na konzervativno zaokruženih 142,85 kPa. Izbor 0–160 kPa ostaje.

Skice imaju stvarne prolaze bez zatvaranja donjeg voda šrafiranom stijenkom.
Z3 pokazuje ispravnu orijentaciju uljnog manometra, Z5 višu razinu uz
podtlak, a Z6 vodom ispunjen spoj koji se podiže i vraća na visinu priključka.
Neutralno siva tekućina u Z5 predstavlja jednu od alternativa, što je
obrazloženo komentarom; tri se fluida ne prikazuju kao tri sloja.

## Završna provjera

- `verify_all.py`: svih 19 modula prolazi; 1076 rezultata (976 usporedbi s
  fiksnim ciljevima i 100 invarijanti), još 22 neovisne fizikalne provjere;
  90/90 ugovora zadataka, bez rupa i tautologija. U03 ima 59 provjera.
- `audit_publication.py` i `audit_typst.py` prolaze. Ostaje 87 riješenih
  primjera i 90 zadataka, uz šest mjesta i propisane razine u U03.
- Prolaze provjere aktualnosti manifesta/ključa, normalizacije javnog teksta
  i `git diff --check`. Manifest i D06 obnovljeni su generatorima.
- Puni HTML render i puni Typst render uspješni; PDF audit prolazi za
  301 A4 stranicu. Vizualno pregledane stranice zadataka 65–67, zajednička
  skica i ključ na stranici 286. Nema odrezanih oznaka ni izgubljenih pitanja.
- Edge na 320, 768 i 1440 px: šest zadataka i ispravne razine; stari HTML
  aliasi prisutni, bez duplikata ID-jeva i vodoravnog prelijevanja. Svih 12
  naputaka/odgovora otvara se Enterom i zatvara razmaknicom. Svih šest
  odredišta i povratnih poveznica iz D06 prisutno je u generiranom HTML-u.
- Usporedba s polazištem potvrđuje da su P1–P6, teorija i završetak U03
  izvan odjeljka zadataka nepromijenjeni; druga poglavlja nisu uređivana.

Ovo je lokalna validacija sadržaja i rendera. Notebooki nisu mijenjani ni
ponovno izvršavani; JupyterLite i cijeli objavni CI nisu pokrenuti. Postojeća
Typst upozorenja za `times.circle` u U10 ostaju izvan ove revizije. Lokalni
Quarto je 1.9.32, CI koristi 1.9.37. Commit i push nisu napravljeni.

## Popravak svih skica nakon pregleda

Na korisnički zahtjev nakon zasebnog pregleda svih skica opseg je proširen
na svih osam SVG-ova uključenih u U03, uključujući riješene primjere.
Prethodni odjeljci dokumentiraju raniju zamjenu vježbi; ova dopuna opisuje
naknadni popravak. Sačuvani su paleta, tipografija, šrafure i raspored panela.

| Skica | Provedeni popravak |
| --- | --- |
| Uvodni pregled | Otvoreni plinski spoj i T-spojevi dvaju vodova; trokut izričito prikazuje manometarski tlak. |
| P1, zatvoreni spremnik | Zajednički gradijent vode u spremniku i priključku; popravljena aritmetika i zaokruživanja. |
| P2, diferencijalni manometar | Jedan U-stupac žive, zračni most i silazni morski stupac; visine u zajedničkom vertikalnom mjerilu 200 jedinica/m. h3 je neto uspon između razdjelnica. |
| P3, vodeni i uljni spremnik | Stvarni otvori u bočnim stijenkama i jedinstveni prolaz; svih šest kota prati zadane razine pri 180 jedinica/m. Ulje i voda imaju kontinuirane gradijente u svojim spojenim prostorima. |
| Ravnoteža i efektivna gravitacija | Otvorene spojene posude; vektorski zbroj g i −a točno daje g_eff, koji je okomit na slobodnu površinu; oba kuta odgovaraju tom nagibu. |
| P4, usis pumpe | Otvoren uronjeni kraj i spoj sa simbolom pumpe; jedinstvena ispuna ulja; jasno naznačen statički model Q=0, bez strelica strujanja. |
| P5, balastni tank | Prozor je u zajedničkoj oplati između mora i balasta; odzračnik je otvoren, vode odvojene stijenkama. Sile na dno okomite su i suprotne, neto prema gore. Kote 8,5/5/2 m imaju isto mjerilo; debljine stijenki su shematske. |
| Z1–Z6 | Voda u Z1 završava na unutarnjem dnu; popravljena oznaka dubine. Z3/Z5 imaju ujednačene prolaze; Z6 otvoren spoj bez gotovo zatvorenog suženja i zajednički gradijent vode. Z2/Z4 zadržani. |

Povezani tekst i brojčane provjere usklađeni su s prikazima:

- P1: pA = 132506,532 Pa, pA,m = 31706,532 Pa.
- P2: 3394,26 Pa bez zraka; 3402,5004 Pa sa zrakom; razlika 8,2404 Pa.
- P4: pM = −20483,28 Pa; paps = 80816,72 Pa; ρg = 8534,7 Pa/m.
- P5: vanjski tlak na prozoru 65,359125 kPa i unutarnji 29,43 kPa.
  Tekst sada izričito navodi zajedničku oplatu koju model pretpostavlja.
- Dvije duge jednadžbe u P2/P3 prelomljene su radi čitljivog PDF-a;
  njihove stabilne oznake sačuvane su.

Verifikator U03 sada ima 61 provjeru: pooštrene su tolerancije uz ispravljene
vrijednosti i dodane dvije provjere tlakova na prozoru. Nije oslabljen audit.
Manifest je obnovljen generatorom; generator potvrđuje aktualnost D06.
Zadaci Z1–Z6, njihovi podatci, razine, naputci i odgovori nisu mijenjani
u ovom popravku. Hash usporedba potvrđuje očuvanje ranijih promjena U04
i nepovezanih QMD datoteka.

Provjera SVG koordinata potvrđuje vektorski zbroj i okomitost te mjerila
i krajeve kota u P2, P3 i balastnom tanku. Dodatna rasterska provjera
prolaza potvrđuje spojene manometre i odvojeno more/balast. Mjereni prolazi
Z3/Z5 su po 18 piksela na krakovima i dnu, a Z6 po 12 na priključku,
kraku i dnu, pri izvornom SVG mjerilu. Rasterska provjera tretira zaglađene
rubove razdjelnica kao rubove fluida, a ne kao krute stijenke.

Svih osam SVG-ova vizualno je pregledano u Edgeu; oznake su unutar granica.
HTML provjera na 320/768/1440 px potvrđuje šest zadataka, propisane razine,
stare aliase, jedinstvene ID-jeve, 12 tipkovnicom dostupnih sklopivih blokova
i poveznice D06. Uspješno su provedeni puni HTML i Typst render te provjere
publikacijske strukture i nativnih Typst blokova. Završni PDF pregled
obuhvaća sve slike 3.1–3.8. Ovo je lokalna validacija; objavni CI i
JupyterLite nisu ponovno pokretani. Commit i push nisu napravljeni.

Završni `verify_all.py`: 1096 uspješnih zapisa (986 usporedbi s ciljevima,
110 invarijanti), još 22 neovisne fizikalne provjere; 90/90 ugovora zadataka.
PDF audit prolazi za 305 A4 stranica. Audit konačne stranice, nakon kopiranja
PDF-a u mapu za preuzimanje, prolazi: 24 HTML stranice, 210 slika, 1916 veza
i 434 sklopiva bloka. Manifest, ključ i normalizacija javnog teksta aktualni
su; `git diff --check` prolazi. Dodatno je vizualno potvrđen novi prijelom
jednadžbi (3.30) i (3.35) na stranicama 57 i 59, bez sudara s brojevima.
