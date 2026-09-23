# Rješavanje preostalih problema

Zahtjev: „Molim te kreni riješavati neriješene probleme. redom kreni sve riješiti.”
Polazište: `d0a0043`, 23. rujna 2026.

## 1. Zaštita arhivskog generatora bilježnica

Stari predlošci ostaju dostupni za usporedbu, ali više ne mogu obnoviti
aktualni `notebooks/`. CLI zahtijeva `--archive-output`; prihvaća samo novu
mapu izvan repozitorija ili unutar `tools/tmp/`. Postojeća odredišta odbija,
a datoteke otvara isključivo za novo stvaranje. Upute u `notebooks/README.md`
i `tools/README.md` usklađene su s tim ponašanjem. Ispravljena je i netočna
tvrdnja da stari QR CLI prepisuje izlaze: on već prosljeđuje poziv aktualnom
generatoru koji bez `--write` samo provjerava datoteke.

Integracijske provjere `tools/test_legacy_notebook_generator.py` pokrivaju
poziv bez argumenata, zabranjena odredišta, postojeći izvoz i zaseban novi
izvoz. U svakom slučaju uspoređuju hashove aktualnih bilježnica. Provjera
je uključena u GitHub Actions.

Status: dovršeno. Sve četiri integracijske provjere prolaze; hashovi 17
aktualnih bilježnica ostali su jednaki. Kompatibilni QR CLI potvrđuje
aktualnost svih 17 izlaza bez promjena datoteka.

## 2. Pregled svih stranica završnog PDF-a

Pregled obuhvaća cijeli dokument, detaljnije provjere sumnjivih mjesta i
ponovljeni pregled nakon obnove. Evidencija je vezana uz hash PDF-a.

Pregledano je svih 321 stranica izvornog PDF-a, SHA-256
`295fc447a5728124112d8b64d0c902df34a66d5bccdadf98bf7ca148c7b73b2f`.
Rasterski listovi i popis stranica nalaze se u zanemarenom
`tools/tmp/pdf-full-review/`. Pronađeno:

- duge jednadžbe dodiruju/preklapaju broj (3.31, 6.48, 10.10, 10.28,
  10.34, 10.46–47, 10.58, 10.62, 10.64, 11.1, 14.16, 14.55, 14.63);
- dio oznaka u skupnim SVG skicama tiska se veličinom 4–6 pt;
- HTML QR slike i poveznice nisu nativno prenesene u PDF;
- naslovi odjeljaka U08/U10/U11 ostali su unutar numeričkih napomena;
- U11 i D03: brojevi koraka odvajaju se od svog sadržaja;
- pojedini tablični retci prelaze na drugu stranicu (npr. 200–201,
  274–275, 281–282, 283–284, 291–292);
- bibliografski zapisi stoje na str. 321 umjesto pod naslovom E.7;
- završni mali naslov U11 ostaje sam pri dnu stranice.

Prazne parne stranice prije početka poglavlja jesu namjeran knjižni prijelom.
Status: popravci i pregled završnog PDF-a dovršeni.

Provedeno:

- prelomljeno 17 dugih jednadžbi; strojna usporedba svih matematičkih
  izraza s početnim commitom potvrđuje iste tokene nakon izuzimanja
  `aligned`, poravnanja, prijeloma i razmaka;
- ispravljene granice napomena U08/U10/U11; Eulerov izvod ostaje u jednom
  slijedu prije odjeljka o zanemarivanju trenja;
- HTML poveznice i QR slike prenose se u nativni PDF, interaktivni blok
  čuva naslov, opis i QR na istoj stranici;
- tablične ćelije više se ne dijele između stranica, bibliografija je
  vraćena pod E.7, a brojevi koraka i mali naslovi ostaju uz tekst;
- uveden PDF raspored iz `assets/print-layouts.json`: Typst čita
  izvorne SVG-ove i uvećava postojeće panele. Napomene koje prelaze granicu
  panela čitaju se iz istih SVG tekstnih elemenata i prelamaju nativno.
  Kanonska geometrija i mrežni prikaz ostaju isti. Za tri široka povezana
  prikaza (dijagram odluke, Venturi s grafom, otvoreni tok) uveden je
  zakrenuti prikaz kako fizički povezana cjelina ne bi bila razrezana.

Vizualno su pregledane i sve 94 pojedinačne skice. Privremeni DOM popis
graničnih pravokutnika teksta i geometrije nalazi se u
`tools/tmp/svg-layout-review/inventory.json`; služi provjeri novih izreza.
Trajni DOM audit prolazi za 94 SVG-a, 256 panela i 3363 tekstna elementa,
uz najmanje 7 pt za oznake. Pomaknuta je samo oznaka D na uvodnoj skici
gubitaka cjevovoda, za 5 SVG jedinica od lijeve stijenke. Geometrija ostaje ista.

PDF nakon popravaka prijeloma ima **420 stranica**, SHA-256
`3f79961791b4170c0a39f086c66cdbe97345d2980a913f815172b4c8dd906e5d`.
Vizualno je pregledano svih 418 stranica međurezultata
`ebeea58f5582823f6c5972315c5879e3ccaec72b210fff6e5e1ede493656b191`,
a nakon posljednjih popravaka svih 31 promijenjenih stranica završnog PDF-a.
Preostalih 389 ima potpuno jednake rasterske piksele sadržaja kao već
pregledane stranice (usporedba izuzima tekuća zaglavlja i folije).
Evidencija usporedbe: `tools/tmp/pdf-corrected-review/comparison.json`;
listovi pregleda: `tools/tmp/pdf-final-review/` i `tools/tmp/pdf-corrected-review/`.

Posljednji pregled dodatno je ispravio odvojeni QR opis U09 i opise slika
10.6, 11.2 i 15.1. QR napomene ostaju zajedno, ali višestranični primjer
koji ih sadrži ostaje prelomiv. Novi `audit_pdf_layout.py` provjerava svih
17 QR uzoraka iz rastera stvarnog PDF-a, obje poveznice, razmak jednadžbi,
18 bibliografskih zapisa u E.7 te odvojene opise i sadržaj izvan stranice.
Na završnom PDF-u prolazi, a na sačuvanom međurezultatu odbija upravo
četiri navedena odvajanja. Na izvornom PDF-u odbio je nestale QR-ove,
preklapanja brojeva jednadžbi i pogrešan položaj literature.

Promjena opsega 321 → 420 i tehničkog regresijskog raspona na 380–460
objašnjena je u `docs/ispis-skica.md`; strogi brojevi sadržaja ostaju
90 zadataka, 87 primjera, 795 jednadžbi, 1216 ID-jeva, 94 SVG-a i 18 citata.

`verify_all.py` nakon obnove manifesta: PASS, 1332 numeričke provjere,
22 neovisne fizikalne provjere i 90/90 ugovora zadataka. Publication i
Typst audit te provjera generiranog ključa: PASS.

Obnovljeni HTML i JupyterLite: 24 stranice, 222 slike, 2094 poveznice,
17 bilježnica i četiri ekstenzije; auditi prolaze. Preglednik potvrđuje
72 prikaza na 320/768/1440 px, A4 ispis i stanje Python kernela Idle.
Kopija PDF-a u `_site/downloads/` bajtno je jednaka pregledanom `_book/`
PDF-u. Novi CFD resursi u `_site/data/cfd/` jednaki su lokalnim izvorima.
Promjene nisu commitane ni poslane na GitHub u ovom koraku.

## 3. Dopuna CFD validacijskog primjera

Potrebno je provjeriti primarne izvore za dijagnostiku arhivskih proračuna
i mjernu nesigurnost. Nije dopušteno izmišljati reziduale, bilance ili
nesigurnosti niti podatke iz drugog proračuna pripisati postojećim mrežama.
Ako izvori ne sadrže potrebne podatke, treba iscrpiti izvedive mogućnosti
novog reproducibilnog proračuna i jasno evidentirati stvarnu prepreku.

Status nakon pregleda javnih izvora: podaci su dopunjeni i ispravljeni, ali
dovršetak potpune validacije bio je blokiran nedostajućim vanjskim podacima.
Ista je prepreka potvrđena u tri uzastopna radna koraka. Naknadni korisnički
zahtjev izričito je dopustio obrazložene približne vrijednosti za dovršetak
nastavnog zadatka; provedba i završni status opisani su u stavci 4.

Pregledani su NASA TMR definicija slučaja, mreže, obje primarne tablice,
potpuno javno Git stablo relevantnih mapa, Ladsonov izvještaj NASA TM 4074
i Diskinov rad AIAA 2015-1746. Točne poveznice, hashovi i popis datoteka
nalaze se u `data/cfd/hydrofoil_experiment/source_review.json`.

- Ispravljena je pogrešna oznaka broja ćelija: NASA-in N u tablici jest
  umnožak strukturiranih dimenzija mreže, odnosno broj točaka.
- Dodane su izvorne male tablice i provjera svih 18 eksperimentalnih redaka
  te svih sedam objavljenih vrijednosti na svakoj od tri CFD mreže.
- Dopunjeni su podaci o točnosti instrumenata i ponovljivosti iz Ladsona
  (tiskana str. 2, PDF str. 4), uz jasnu zabranu njihove zamjene standardnom
  nesigurnošću pri 10,10°.
- Razlikovan je objavljeni sažetak duboke iteracijske konvergencije od
  stvarnih povijesti proračuna. Graf reziduala ravne ploče iz istog rada
  nije preuzet kao dokaz za NACA profil.
- Tro-mrežni GCI označen je kao uvjetna procjena; monotoni podskup ne
  dokazuje asimptotsko područje, što naglašava i izvorni rad.

Validator prolazi. Četiri negativne provjere odbijaju zamjenu točaka
ćelijama, izmjenu druge mjerne točke, neutemeljenu tvrdnju o potpunoj
nesigurnosti i izmjenu izvornog arhiva; nakon vraćanja podataka opet prolazi.

Nisu pronađene sirove povijesti reziduala/sila ni masene bilance za te
tri mreže, a nedostaje i potpuna mjerna nesigurnost usporedne točke.
U lokalnom PATH-u nema FUN3D/SU2/OpenFOAM rješavača, a WSL nije instaliran.
FUN3D zahtijeva NASA-in postupak izdavanja; novi proračun drugim kodom
mogao bi dati vlastitu dijagnostiku, ali ne bi rekonstruirao stare zapise
ni nedostajuću eksperimentalnu nesigurnost. Zato nije uvedena izmišljena
validacijska presuda. Korisnici je poslano pitanje ima li dodatne podatke
i gdje su dostupni. Za preostali dio potrebna je promjena dostupnih podataka.

Dodatni pregled rada Freeman i Roy (2014.) pronašao je navod o 2,5 %
mjerne nesigurnosti otpora, ali za napadni kut 0°. Nije primijenjen na
odabranu točku 10,10° niti proglašen njezinim potpunim budžetom.
Pregledan je i NASA-in sažetak kasnijeg Diskinova rada iz 2016.; on
ponavlja ograničenje asimptotskog reda. Puni časopisni tekst nije bio
dostupan kroz provjereni izdavačev pristup, pa se ne tvrdi da je njegov
cijeli sadržaj ili dodatni materijal pregledan. Opseg pregleda, izvori
i hash dostupnog PDF-a dodani su u `source_review.json`.

## 4. Dovršetak Z6 uz odobrene nastavne procjene

Korisnički zahtjev: „Ispravi i dovrši taj zadatak nakorektnije kako možeš,
da uzmeš tipa približne vrijednosti, ne moraju biti točne eksperimentalne
ili neke vrijednosti koje su uz obrazloženje najbliže istini.”

Status: dovršeno prema tom zahtjevu. Nastavni zadatak ima sve ulaze,
izvršiv račun i oba zaključka; ne tvrdi se da su pronađene izvorne
dijagnostike ili provedena nova eksperimentalna validacija.

- Z6 zadržava izbor mreže i dobiva uvjetnu usporedbu otpora profila.
  Središnji koeficijenti proizlaze iz postojećih javnih podataka: najfiniji
  CFD rezultat zaokružuje se na 0,01222, a mjerenja se interpoliraju na
  isti kut 10,00° i zaokružuju na 0,01166.
- Tri standardne nesigurnosti 0,00020 / 0,00010 / 0,00010 jasno su
  označene i obrazložene kao nastavne pretpostavke. Osnovni kriterij
  slaganja nije zadovoljen: razlika 0,00056 prelazi proširenu nesigurnost
  0,000490. Uz mjernu nesigurnost 0,00030 interval raste na 0,000663 i
  kriterij jest zadovoljen, bez poboljšanja CFD središnje vrijednosti.
- D.9 ispravno opisuje monotoni rast CL i pad CD te pokazuje podrijetlo
  aproksimacija. `teaching_comparison.json` odvaja pretpostavke od izvornog
  arhiva; izvorne tablice i oznake nedostajućih dijagnostika ostaju istinite.
- Ažurirani su notebook, verifikator, podatkovni validator, generirani
  manifest i ključ D06. Generator ključa dobio je izričitu mogućnost
  `data-key-full="true"` kako ovaj višedijelni odgovor ne bi izgubio završnu
  odluku pri skraćivanju. Ostali odgovori nisu promijenjeni.
- Zadržani su stabilni ID, razina T4 i šest zadataka. Postojeća skica
  profinjenja iste domene i dalje odgovara dijelu a); za dio b) notebook
  prikazuje razliku i dva intervala nesigurnosti, bez nove dekorativne skice.

Provjere: 1340 numeričkih rezultata, 22 neovisne fizikalne provjere i
90/90 ugovora zadataka prolaze. CFD validator provjerava i interpolaciju
prema izvornim redcima, zaokruživanje i oba kriterija. Četiri negativna
pokušaja odbijena su: lažna tvrdnja o validaciji arhiva, referenca s
neusklađenog kuta, prikaz pretpostavke kao mjerenja i izmijenjena numerička
nesigurnost. Izvršen je cijeli ažurirani notebook; svi njegovi izračuni i
tvrdnje prolaze. Zaštita arhivskog generatora ponovno prolazi četiri testa.

Obnovljeni HTML/JupyterLite prolazi audit 24 stranice, 222 slike, 2094
poveznice i svih 17 distribuiranih bilježnica. Nakon ove sadržajne izmjene
ponovljen je viewport/WCAG audit triju zahvaćenih HTML stranica na trima
širinama: devet prikaza, A4 ispis i otvaranje ažuriranog U12 notebooka s
Python kernelom Idle prolaze. Prethodni pregled 72 prikaza ostaje zaseban
dokaz ranijih izmjena, ne tvrdi se da je ovdje ponovno izvršen.

Završni PDF ostaje na 420 stranica, SHA-256
`a97558feaafefcc9d3d5d4d777b5c7cce755abff7c882d39cb1336d4e8dcb6ed`.
Oba PDF audita prolaze. Pregledano je svih 14 promijenjenih stranica
(7, 8, 302–306, 397–398, 416–420); preostalih 406 ima iste piksele sadržaja
kao ranije pregledani PDF. Dokaz usporedbe i prikazi nalaze se u
`tools/tmp/pdf-cfd-teaching-review/`. Potpunost odgovora dodatno je
provjerena u generiranom ključu, HTML-u i PDF-u na str. 416. Zadatak je
na str. 305–306, a obrazloženje aproksimacija na str. 397–398.

Kopije PDF-a i CFD podataka u `_site/` jednake su završnim lokalnim izvorima.
Promjene nisu commitane ni poslane na GitHub.
