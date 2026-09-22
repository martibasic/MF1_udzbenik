# Revizija U13 — gubitci, cjevovodi, crpke i mreže

## Dijagnoza prije provedbe

Šest primjera pokriva ravnu dionicu, laminarni vod, serijsko-paralelnu mrežu,
radnu točku s promjenom brzine, godišnju energiju i NPSH. Z1 i Z2 treba
zadržati kao jednostavnu računsku tehniku. Z3 ponavlja izravnu podjelu
protoka iz P3, a Z4 ponavlja presjek unaprijed zadanih kvadratnih krivulja
iz P4 i tri snage iz P5. Z5 i Z6 već imaju vrijedne odluke o najgorem
otporu, regulaciji, energiji i granici usisnog zaključka.

Z3 se mijenja u obrnuti problem uravnoteženja grana prigušnim ventilom.
Z4 umjesto unaprijed izračunatog otpora sustava dobiva geometriju cijevi
i hrapavost: student iterira Re, Darcyjev faktor i radnu točku. Modeli su
unaprijed odabrani i dopušten je notebook; to ostaje standardan problem T2,
bez optimiranja ili dodatne analize nesigurnosti. Time se stvarno pokriva
obvezni ishod iterativne radne točke, uz odvojene razine snage.

Postojeće dvije referencirane slike imaju stare nazive. Uvodna mreža ima
prekid na dnu gornjeg spremnika, nesklad ispuna na granama i kotu H izvan
slike. Druga slika prikazuje proizvoljno položene EGL/HGL krivulje koje
ne završavaju na slobodnom izlazu i ne zatvaraju prikazanu bilancu; profil
brzine ne prikazuje jasno prianjanje, a simboli smicanja nisu tangencijalni.
Treba sačuvati raspored i panele, ali ponovno zadati fizikalnu geometriju.
U kanonskom izvoru nema zajedničke slike vježbi; nova dobiva jedinstveno
opisno ime koje neće prepisati stare slike drugih sadržaja.

## Matrica prije provedbe

| Mjesto | Postojeći ID i uloga | Odluka i didaktička korist | Razina | Završni ID | Povezane provjere | Status |
| --- | --- | --- | --- | --- | --- | --- |
| P1 | `ex-gubitci-jedne-dionice`; Darcy i lokalni gubitci | ZADRŽATI: temeljni izravni račun | T1 | isti | verifier | provedeno |
| P2 | `ex-laminarni-rashladni-vod`; izbor režima i dva zapisa | ZADRŽATI: laminarni granični slučaj | T2 | isti | verifier | provedeno |
| P3 | `ex-serijsko-paralelna-mreza`; zajednički pad i kontinuitet | ZADRŽATI: potpuna serijsko-paralelna bilanca | T3 | isti | verifier, uvodna skica | provedeno |
| P4 | `ex-radna-tocka-vfd`; afinitet uz statičku visinu | ZADRŽATI: razlikovanje omjera brzine i radnog protoka | T3 | isti | verifier | provedeno |
| P5 | `ex-energijski-ledger-hladenja`; tri razine snage | ZADRŽATI: temeljni energetski račun | T2 | isti | verifier | provedeno |
| P6 | `ex-npsha-usisne-crpke`; dva zapisa NPSH | ZADRŽATI: bez nedopuštene presude o kavitaciji | T3 | isti | verifier | provedeno |
| Z1 | `task-gubitci-ravne-dionice`; pojedinačni gubitci | PREPRAVITI sitno: vodoravna cijev i referentna brzina lokalnih koeficijenata | T1 | isti | SVG, verifier | provedeno |
| Z2 | `task-laminarna-cijev-smjese`; λ=64/Re | ZADRŽATI; jasno zadati potpuno razvijen Newtonski tok i isključeno ulazno područje | T1 | isti | SVG, verifier | provedeno |
| Z3 | `task-raspodjela-paralelnih-grana`; izravna raspodjela | ZAMIJENITI: mjesto i otpor ventila za jednake protoke | T2 | `task-uravnotezenje-paralelnih-grana` | stari alias, SVG, notebook, verifier, D06 | provedeno |
| Z4 | `task-radna-tocka-tri-snage`; dvije zadane parabole | ZAMIJENITI: geometrija i Colebrook u iteraciji radne točke, tri snage | T2 | `task-radna-tocka-hrapavog-voda` | stari alias, SVG, notebook, verifier, D06 | provedeno |
| Z5 | `task-robustan-izbor-promjera`; gornja granica otpora | ZADRŽATI; raspon je zadana granica, a ne standardna nesigurnost | T3 | isti | SVG, verifier, D06 | provedeno |
| Z6 | `task-regulacija-energija-npsh`; regulacija i godišnja energija | ZADRŽATI problem; sintetičke krivulje, gustoća, potpune godišnje energije i NPSH pri određenoj brzini | T4 | isti | SVG, notebook, verifier, D06 | provedeno |

`rewrite_status`: complete; `rewrite_level`: selective;
`sketch_requirement`: obje postojeće slike i nova zajednička slika vježbi.
Izvor novih problema i podataka: autorski nastavni primjeri.

## Neovisno riješeno prije pisanja

- Z3: za Q = 0,020 m³/s jednake grane nose po 0,010 m³/s. Ventil treba
  u granu R1 = 12000 s²/m⁵, s dodatnim Rv = 36000 s²/m⁵. Ukupni pad
  između čvorova je 4,80 m, od čega ventil troši 3,60 m. Grana većeg
  otpora ne može se uravnotežiti dodatnim nenegativnim otporom samo u njoj.
- Z4: Hp = 30 − 30000 Q², Q u m³/s; Δz = 8 m, D = 0,100 m, L = 150 m,
  ε = 0,100 mm, Σξ = 6, ν = 1e-6 m²/s, ρ = 1000 kg/m³. Colebrook i
  bisekcija na 0,005–0,030 m³/s daju Q = 19,02964471 L/s,
  Re = 242292,96, λ = 0,02081203223 i H = 19,13617866 m.
  Za ηp = 0,76 i ηm = 0,92: Ph = 3,57235742 kW,
  Pvr = 4,70047029 kW, Pel = 5,10920684 kW.
- Z6 zadržava stare brojčane ulaze; godišnje energije s punom preciznošću
  jesu 25,54338634 MWh (ventil) i 18,40626369 MWh (brzina), razlika
  7,13712265 MWh. NPSHr = 3,09615 m odnosi se na nazivnu brzinu;
  za konačnu odluku o sniženoj brzini treba odgovarajuća druga krivulja.

## Rezultati

Provedene su odluke iz matrice. Svih šest riješenih primjera zadržano je.
Z1/Z2 ostaju jednostavni računski zadatci; Z3 je novi obrnuti problem
uravnoteženja, Z4 iterativna radna točka, a Z5/Z6 zadržavaju izbor i
integraciju uz preciznije pretpostavke. Stari ID-jevi Z3/Z4 sačuvani su kao
jedinstveni sirovi HTML spanovi. Omotači se ne mijenjaju.

Uz zadatke su usklađeni oba notebooka, verifier, D03, generirani D06 i
manifest. U teoriji su ciljano ispravljeni indeks otpora paralelnog ogranka
te naziv ukupne učinkovitosti crpke kao omjera hidrauličke i vratilne snage.
Obje postojeće slike i nova zajednička slika vježbi čuvaju postojeći stil.
Otvoreni su spojevi spremnika i cijevi, grane imaju zajedničku ispunu bez
sjena, usis je uronjen i odmaknut od dna, a koljeno ima stalnu normalnu
širinu. Energijska i piezometrijska crta zatvaraju bilancu slobodnog izlaza;
krivulje Z4 izračunane su iz stvarnih podataka zadatka.

Izvršene provjere 22. rujna 2026.:

- Kanonski verifier U13: 89 rezultata bez FAIL-a. Tolerancije svih Z1–Z6
  usklađene su s objavljenom preciznošću; provjereni su kontinuitet, oba
  reziduala radne točke, osjetljivost na hrapavost i bilanca godišnje energije.
- `verify_all.py`: 1257 rezultata (1062 golden i 195 invarijanti), 22 dodatne
  fizikalne provjere, 90/90 ugovora zadataka, bez rupa ili tautologija.
- Oba izmijenjena notebooka izvršena od početka: PASS. Colebrookov notebook
  koristi drukčiji unutarnji iterativni postupak od bisekcije u verifieru;
  notebook mreže eksplicitno ograničava svoj model na turbulentni režim.
- Geometrijska provjera svih triju stvarnih SVG-ova i vizualni pregled: PASS.
  Suhi dijelovi stijenki provjeravaju se zasebno od omočenog ruba; provjera
  ne traži da cijela stijenka spremnika bude pod vodom. Nema oznaka izvan SVG-a.
- Audit strukture, Typsta, normalizacije, manifesta, ključa, QR kodova i CFD
  paketa: PASS; knjiga ima 87 primjera i 90 zadataka propisanih razina.
- Stvarni HTML U13 na 320/768/1440 px: šest zadataka, razine, oba stara
  anchora, jedinstveni ID-jevi i 12 tipkovničkih otvaranja naputaka/odgovora
  prolaze, bez vodoravnog prelijevanja. Automatizirani WCAG A/AA: PASS.
- D06 ima šest ažurnih rezultata i povratnih poveznica; matematički zapisi
  nisu odrezani. Posebno su provjereni svi izlazi i kriteriji Z4 i Z6.
- Nativni PDF: 315 stranica A4, audit PASS. Vizualno pregledane stranice
  223 i 225 (uvodne skice), 232–234 (skice i svi zadatci), 311–312 (ključ).

Provjere ne zamjenjuju neovisnu stručnu recenziju ni studentski pilot.
Zajednički završni build cijelog višepoglavnog cilja slijedi nakon U02;
provjera trenutačne objave vodi se u zajedničkoj evidenciji.
