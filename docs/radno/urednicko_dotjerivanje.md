# Uredničko dotjerivanje cijelog udžbenika

Zahtjev: „Sada se ponašaj kao editor i polišaj knjigu. Make it modern and sleek
and easy to read.” Početno stanje: `573a0d3`, 23. rujna 2026.

## Opseg i kriteriji dovršetka

Rad obuhvaća početnu stranicu, uvod, svih 15 poglavlja i šest dodataka,
u mrežnom i nativnom PDF izdanju. Cilj je lakše čitanje i snalaženje:
jasna hijerarhija, odmjereni razmaci, čitljive formule i tablice, sažetiji
uvodi i dosljedan urednički glas. Sačuvati provjerene modele, podatke,
stabilne ID-jeve, javne URL-ove, raspored P/Z i postojeći stil fizikalnih skica.

| Područje | Potreban dokaz dovršetka | Status |
| --- | --- | --- |
| Inventar i početni prikaz | Pregled svih izvora; snimke HTML-a i reprezentativnih PDF stranica | Provedeno |
| Tipografija i raspored HTML-a | Usklađeni naslovi, tekst, formule, tablice i autorski blokovi; vizualni pregled | Provedeno |
| Početna stranica i snalaženje | Jasni ulazi u gradivo, vježbe i dodatke; navigacija provjerena tipkovnicom i na mobitelu | Provedeno |
| Urednički prolaz teksta | Evidencija po svakom poglavlju i dodatku; ciljane dorade jasnoće i uklanjanje suvišnog ponavljanja | Provedeno |
| PDF | Obnovljena knjiga, pregled naslovnice, kazala, početaka poglavlja, izvoda, zadataka i dodataka | Provedeno; 321 stranica |
| Očuvani ugovori | Numeričke, strukturne i generativne provjere; usporedba ID-jeva i modela | PASS |
| Završni prikaz | Sve stranice na 320/768/1440 px, WCAG, tipkovnica, poveznice, A4 i aktualni PDF | PASS: 72 prikaza i A4 |

## Početni nalazi

- HTML ima topao, odmjeren kolorit, ali širok tekst, velik broj kurzivnih
  podnaslova, oznake velikim slovima i nekoliko konkurentnih naglasaka.
- Sadržaj dugih poglavlja nije prikazan; čitatelj teško brzo dolazi do odjeljka.
- Početna stranica daje pun katalog, ali slabo razlikuje početak čitanja,
  vježbanje i traženje formule ili rezultata.
- Uvodni tekstovi mjestimice ponavljaju opis svrhe matematike, modela i primjene;
  kratke izravne formulacije mogu jasnije usmjeriti na fizikalno pitanje.
- Nativni PDF ima zasebna tipografska pravila. Treba provjeriti stvarne prijelome,
  a ne pretpostaviti da izmjena HTML-a poboljšava i tiskanu knjigu.

Ovo je radna evidencija. Prolaz postojećih testova sam po sebi ne dokazuje
uredničku kvalitetu ni dovršetak ovoga zahtjeva.

## Urednički prolaz po sadržaju

| Sadržaj | Odluka i provedena dorada |
| --- | --- |
| Početna | Ispravljen CSS koji je cijeloj sekciji zadavao veličinu h1; sažeta uvodna poruka, ulaz u prvo poglavlje, PDF i brze poveznice; kompaktniji katalog |
| U00 | Izravnije upute za prvo čitanje; predznanje opisano bez upućivanja na skriveni blok |
| U01 | Jasnije uvodno pitanje; Z6 podijeljen na podatke, model i zahtjeve |
| U02 | Uklonjeno udvostručeno „poglavlja pog.” u opisu slike; nedavno dorađeni tekst zadržan |
| U03 | Ispravljena gramatička pogreška, jasnija uputa za praćenje tlaka, podijeljen Z6, ujednačeno obraćanje |
| U04 | Zadržan jasan uvod; podijeljen Z6 i skraćen opis pregledne slike |
| U05 | Ujednačena oznaka inženjerskog konteksta i obraćanje u primjerima i vježbama |
| U06 | Kraći i precizniji opis primjene; ispravljeni pontoni; razdvojen opsežni Z6 |
| U07 | Sažet kontekst kontrolnog volumena; jasniji prijelaz iz difuzora u spremnik; uklonjena gramatička pogreška; odlomci u Z6 |
| U08 | Kraći povijesni i inženjerski uvod, izravniji opis pretvorbe jedinica i značenja članova; odlomci u Z6 |
| U09 | Sažet opis primjena i cilja; modeli i obrađeni primjeri zadržani |
| U10 | Sažet kontekst opterećenja nosača i ujednačeno obraćanje |
| U11 | Pregledano; postojeći uvod, pretpostavke sličnosti i razlomljeni zadatci zadržani |
| U12 | Pregledano; postojeći sažeti uvod, granice modela i podjela zadataka zadržani |
| U13 | Uvod odmah povezuje kontinuitet, energiju i radnu točku; skraćen popis primjena |
| U14 | Izravan opis sile, momenta i snage; uklonjena suvišna najava važnosti gradiva; ujednačeno obraćanje |
| U15 | Sažet opis primjene kroz kapacitet, valove i skok; sačuvani izvori i ograničenja modela |
| D01 | Tekst zadržan; širine stupaca raspodijeljene prema duljini definicija |
| D02 | Kraći uvod; više prostora definicijama, manje oznakama poglavlja |
| D03 | Gusta tablica zamijenjena pregledom od 15 parova „pogreška / provjera”; ispravljene zamijenjene ćelije U09/U10 i doslovno ispisan TeX; stari ID-jevi odjeljaka sačuvani |
| D04 | Jasno naveden opseg i pozitivno formulirane provjere; zadržan stari ID promijenjenog naslova |
| D05 | Kraća uputa za uporabu literature; citati i izvori nepromijenjeni |
| D06 | Uvod i završna napomena dorađeni u generatoru; ključ ponovno generiran iz aktualnih iskaza |

## Dokazi i završne ispravke

- Početne snimke: `tools/tmp/editorial/before/`; međuprikazi u `layout/` i `current/`.
- U svim U00–U15 uspoređeni su svi matematički izrazi i eksplicitni ID-jevi
  s `573a0d3`: identični su i istim redoslijedom. SVG i notebook izvori nisu mijenjani.
- `verify_all.py`, `audit_publication.py`, `audit_typst.py`, normalizacija i
  generator manifesta prolaze: 87 primjera, 90 zadataka i izvorna raspodjela razina.
- Probni PDF potvrdio je uklanjanje okvira i hrvatsko zaglavlje. Otkriveno je
  zaobilaženje Quartoova resetiranja posebnih brojača slika; ispravljeno je i
  stvarna numeracija svih 94 slika ponovno je 1–N unutar pripadnog poglavlja.
  Taj je uvjet dodan trajnom `audit_pdf.py`.
- Završni PDF koristi 11 pt i margine 26/22 mm. Pregledani su naslovnica,
  kazalo, početci svih 15 poglavlja, reprezentativni izvodi i zadatci te
  dodaci. Širine stupaca D01/D02 zadane su izvornim `tbl-colwidths` atributom,
  koji vrijedi i za HTML i za Typst. Oznake pogreške i provjere ostaju uz tekst.
- Pregled PDF-a otkrio je pogrešan Pandocov prijevod TeX-ova `\!` u
  `#h(-1em)`. Typst filtar sada iz prikaznog stabla uklanja samo taj razmak.
  Ponovni render potvrdio je pravilan redoslijed i razmak vektorskih simbola;
  izvorne formule ostaju iste. Zasebna proba potvrđuje da obični faktorijel `!`
  ostaje očuvan.
- Funkcionalno su otvoreni početno poglavlje, odjeljak vježbi, SVG u novoj
  kartici i odgovarajući kontrolni rezultat. Za rezultat se uzima aktualni
  naslov zadatka, a ne sačuvani prazni anchor stare poveznice. Na mobitelu
  je stvarno izvršeno vodoravno pomicanje pojmovnika tipkom sa strelicom.
- PDF audit prolazi; analiza svih 321 stranica nije našla tekst izvan granica
  stranice. PDF u `_site/downloads/` jednak je knjizi bajt po bajt:
  7.062.201 B, SHA-256
  `ac405a65752ca29a6ddc44a2c22e6bc1779ba8dd83bd49e09f2456d34dd632ed`.
- Konačne snimke HTML-a nalaze se u `tools/tmp/editorial/release/`, a PDF
  pregledi i izvještaj u `tools/tmp/editorial/final-pdf/` (lokalni QA izlazi).
- Završni automatizirani pregled prolazi: 24 stranice na tri širine, WCAG,
  tipkovnički fokus, odredišta novih poveznica, povećanje skica i lokalno
  pomicanje tablica; A4 prikaz i učitan notebook s Python kernelom u stanju
  Idle. Audit konačnog HTML-a provjerio je 222 slike i 2.091 poveznicu.
- Numerički izvještaj: 1.332 rezultata (1.113 usporedbi s neovisnim ciljem
  i 219 invarijanti), 22 dodatne fizikalne provjere, 90/90 ugovora zadataka,
  bez deklariranih rupa i tautologija. Generirani ključ, manifest i svih
  17 QR poveznica aktualni su. CFD V&V inventar prolazi postojeće kriterije.

Urednički prolaz dovršen je 23. rujna 2026. Automatizirane provjere potvrđuju
navedene tehničke ugovore; procjena čitljivosti temelji se i na opisanom
vizualnom pregledu stvarnih izlaza.

Zajedničke uredničke odluke opisane su u [uredničkom stilu](../urednicki_stil.md).
