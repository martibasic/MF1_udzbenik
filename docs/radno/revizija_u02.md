# Revizija zadataka za vježbu U02 — 22. rujna 2026.

## Opseg i odluke prije provedbe

Isti uvjeti kao za U01: mijenjaju se samo potrebni zadatci Z1–Z6 uz očuvanje
raspodjele T1, T1, T2, T2, T3, T4. P1–P6, teorija, notebooki i omotači ostaju
izvan ove revizije. Polazište je U02 u commitu `a5ce9f6`; postojeće lokalne
izmjene U01 i omotača U02/U11 čuvaju se.

| Mjesto | Postojeća aktivnost i sličnost | Odluka i nova korist | Razina |
| --- | --- | --- | --- |
| Z1 | Izravni Newtonov zakon kao P2 | ZADRŽATI osnovnu samostalnu vježbu; pretpostavke u uvodu | T1 |
| Z2 | Obrnuti račun iste jednadžbe kao P2/Z1 | ZAMIJENITI usporedbom kapljice i sapunastog mjehura; broj međupovršina | T1 |
| Z3 | Smicanje na vratilu kao P5, s manje koraka | ZAMIJENITI pločom s dva različita procjepa; zbroj sila i analiza pogreške | T2 |
| Z4 | Kapilarni uspon kao P3, ali i omjer promjera | ZADRŽATI jednostavan račun i provjeru skaliranja | T2 |
| Z5 | Dva uzastopna uvrštavanja iz P3/P4 | ZAMIJENITI mjernim nizovima; prihvaćanje ili odbacivanje Newtonskog modela | T3 |
| Z6 | Izbor regulatora, dva oblika međupovršine | PREPRAVITI tlačnu bilancu odvojenih stanja i dodati interval promjera kapljice | T4 |

P1 pretvara μ u ν; P2 uvodi Couetteovo smicanje; P3 ravnotežu kapilarnog
uspona; P4 povezuje uspon i kapljicu; P5 geometriju ležaja i temperaturnu
ovisnost otpora; P6 utjecaj kontaktnog kuta. Usporedba pokazuje da je račun
ležaja dobro zastupljen, a izbor konstitutivnog modela iz podataka nedostaje
među zadatcima. Z5 zato izravno pokriva obvezni ishod kurikularne matrice.

Z2/Z3/Z5 su autorske nastavne konstrukcije (`rewrite_status=preradeno`,
`rewrite_level=P3`): mijenjaju se geometrija ili scenarij, ulazi, izlazi i
studentska odluka. Z1/Z4 su `nije_potrebno`; kod Z6 radi se o ispravku modela
i proširenju odluke unutar istog scenarija, pa prag 3/5 nije uvjet popravka.
Nizovi u Z5 sintetički su; ne predstavljaju stvarna mjerenja ni komercijalne fluide.

## Poveznice i skice

Z1/Z4/Z6 čuvaju svoje ID-jeve. Zamjene dobivaju semantičke ID-jeve:

| Stari ID | Novi ID |
| --- | --- |
| `task-u02-klizna-ploca-povrsine-giba-se-brzinom-kroz` | `task-kapljica-i-sapunasti-mjehur` |
| `task-u02-vratilo-promjera-i-duljine-vrti-se-tako` | `task-ploca-izmedu-dva-procjepa` |
| `task-u02-staklena-kapilara-promjera-uronjena-je-u-vodu` | `task-newtonski-model-iz-mjerenja` |

Stari HTML ID-jevi ostaju kao prazni span elementi uz zamjenska mjesta;
stare poveznice vode na novi problem. Povijesni sadržaj ostaje u Gitu.
`sketch_requirement`: Z1/Z2/Z4/Z5 preporučena, Z3/Z6 potrebna radi geometrije
i razlikovanja stanja. Zadržavaju se postojeći raspored šest panela, njihove
dimenzije, naslovne trake, šrafure, gradijenti, font i boje. Paneli Z1 i Z4
ostaju isti; mijenja se sadržaj panela Z2/Z3/Z5/Z6.

## Kontrolni račun i granice modela

- Z1: 270,833 s⁻¹, 227,5 Pa, 50,05 N; neovisno Fδ = μvA.
- Z2: jedna međupovršina 100 Pa, tanki sapunasti film s dvije 200 Pa.
  Omjer 2; dvostruki promjer prepolovi oba skoka.
- Z3: gradijenti po iznosu 300 i 150 s⁻¹; naprezanja 36 i 18 Pa;
  otpori 0,72 i 0,36 N, ukupno 1,08 N. Pogrešno spajanje razmaka daje
  0,24 N. Oba otpora suprotstavljaju se brzini; kod jednakih procjepa daju
  dvostruki doprinos jedne strane, a udaljavanje jedne stijenke uklanja njen doprinos.
- Z4: 17,9985 i 8,9993 mm; omjer uspona 2 pri omjeru promjera 1/2.
- Z5: gradijenti 100/200/400 s⁻¹. Uzorak A daje 20/40/80 Pa i stalnih
  0,20 Pa·s. B daje 30/45/60 Pa i 0,30/0,225/0,15 Pa·s. Newtonski model
  prihvatljiv je za A u ispitanom rasponu: na 0,30 m/s daje 0,60 N. Prva
  točka B ne daje univerzalnu viskoznost: na 0,40 m/s predvidjela bi 1,20 N,
  dok tablica daje 0,60 N. Tri točke ne određuju jedinstven nenewtonski zakon.
- Z6: ρgH = 411,196 Pa; 4σ/d = 576 Pa; hcap = 58,834 mm.
  Punjenje do izlaza bez kapljice ne traži pozitivan statički pretlak.
  Sferna kapljica od 1,8 mm traži 571,196 Pa. Za D od 1,6 do 2,0 mm
  zahtjev iznosi 555,196–591,196 Pa; 0,50 kPa nije dovoljno, 0,60 kPa
  pokriva zadani statički raspon uz najmanju rezervu 8,804 Pa.
  To nije provjera prijelaznog oblikovanja kapljice ni gubitaka pri protoku.

Za Z6 izvedene su dvije odvojene bilance: konkavni meniskus pri punjenju i
konveksna izlazna kapljica ne daju istodobno dva neovisna tlačna skoka.
Stručna podloga za zakrivljenost i kapilarni uspon:
[MIT, Surface Tension](https://web.mit.edu/2.25/www/225_sect_11.html) i
[MIT, Capillarity and Gravity](https://web.mit.edu/nnf/education/wettability/gravity.html).
Primjena na dvije zadane konfiguracije naš je izvod, ne preuzeti zadatak.

**Otvoreno izvan opsega:** P4 već sadrži napomenu za stručnu provjeru
zbrajanja kapilarnog doprinosa i tlaka kapljice. Njegov model i rezultat
347 Pa zahtijevaju zasebnu reviziju; Z6 ne prenosi tu idealizaciju. P4 i
njegove provjere ovim zahvatom nisu mijenjani niti su ponovno fizički potvrđeni.

## Povezane izmjene i validacija

Usklađeni su izvor U02, skica, `verify_u02.py`, generirani D06 i manifest te
stavka U02 u D03. D01/D02 već sadržavaju potrebne odnose. Notebook
`notebooks/u02_kapilarni_uspon.ipynb` ne upućuje na zamijenjene Z2/Z3/Z5
ni na njihov račun i nije mijenjan.

- `verify_u02.py`: 69 provjera prolazi. `verify_all.py`: 19 modula, 1055
  rezultata (965 usporedbi s fiksnim ciljevima i 90 invarijanti), još 22
  fizikalne golden provjere; 90/90 ugovora i bez rupa. To su provjere
  implementiranih modela, ne potvrda otvorenog stručnog pitanja u P4.
- `audit_publication.py`: prolazi, svih 15 poglavlja čuva zadanu raspodjelu;
  87 riješenih primjera i 90 zadataka. `audit_typst.py`, provjera manifesta,
  generiranog ključa, normalizacije i `git diff --check`: prolaze.
- Puni HTML render te konačni render U02 i D06: uspješni. Naputci i odgovori
  U02 provjereni su tipkama Enter i Space na 320, 768 i 1440 px; 12 sklopivih
  blokova radi, nema vodoravnog prelijevanja stranice ni duplih ID-jeva.
  Tri stara odredišta postoje, a svih šest veza iz D06 vodi na aktualne zadatke.
- Puni Typst render i `audit_pdf.py`: prolaze, 299 A4 stranica. Pregledani su
  zadatci na stranicama 45–46, skica na 47 i pripadni ključ na 283. Sažeci,
  naputci i odgovori U02 u D06 imaju zatvorene matematičke oznake i zadržane
  kriterije odgovora. Postojeća upozorenja `times.circle` u drugom poglavlju
  knjige nisu dio ovog zahvata.
- Usporedba izvora prije/poslije potvrđuje da su teorija, P1–P6 i sažetak
  nepromijenjeni te da su blokovi Z1 i Z4 sačuvani. Izvorne grafičke komponente
  panela Z1 i Z4 preuzete su bez promjene; svi SVG tekstovi stanu u kadar.

Nije ponovno izvršen puni objavni postupak s notebookovima, JupyterLiteom i
auditom cijelog objavljenog weba; ovo je lokalna revizija sadržaja i rendera.
Nije napravljen commit ni push. Ranije lokalne izmjene U01 i korisničkih
omotača nisu uključivane u opseg revizije U02 ni poništavane.

## Fizikalna dorada skica — 22. rujna 2026.

Na dodatni zahtjev korisnice dorađeni su svi paneli uz očuvanje rasporeda,
plavih traka, šrafura, gradijenata i tipografije. Ova dorada zamjenjuje raniju
odluku o doslovnom zadržavanju panela Z1/Z4; zadatci i njihovi računi ostaju isti.

- Z1/Z5: nepomična podloga označena je šrafurom; profili i vektori brzine
  zadovoljavaju nulu na podlozi i brzinu ploče na gornjoj granici. Brzina je
  tamna strelica, vučna sila crvena, a sila fluida na ploču zelena i suprotnog
  smjera. Dinamometar u Z5 povezan je s pločom u liniji vučne sile.
- Z3: dva zasebna linearna profila završavaju na odgovarajućim plohama
  pokretne ploče; nijedna kosa crta profila više ne prolazi kroz krutu ploču.
  Obje sile ulja djeluju ulijevo, vučna sila udesno. Duljine strelica F1/F2
  slijede omjer 2:1, a duljina vučne sile njihov zbroj.
- Z2: tlakovi su skalarne oznake, bez strelica koje bi tlak prikazivale kao
  vektor. Film mjehura ostaje jasno omeđen dvjema međupovršinama.
- Z4: staklene stijenke prikazane su zasebno od lumena; oba kraja cijevi su
  otvorena. Donji otvori uronjeni su iznad dna, a meniskusi omeđuju stvarno
  obojeni fluid. Slobodna površina posude ne presijeca staklene stijenke.
- Z6: donji otvor igle uronjen je ispod razine vode. Poklopac se sastoji od
  odvojenih krutih dijelova oko zabrtvljene igle, bez krute plohe preko lumena.
  Kontura kapljice otvorena je na spoju s lumenom, bez pune kružnice koja bi
  presijecala spoj. Nema unutarnjeg meniskusa ni nacrtanog protoka u statičkom
  stanju. Visinska kota polazi od izlaza igle do slobodne površine spremnika.

U AGENTS.md dodano je pravilo provjere povezanosti fluidnih domena, krutih
stijenki i fizikalne uloge strelica.

Provjera ove dorade: SVG pregledan u Edgeu, svi tekstovi unutar kadra;
HTML render U02 i puni Typst render uspješni. Konačna skica pregledana je
na stranici 47 PDF-a. `audit_publication.py` i `audit_pdf.py` prolaze (299
A4 stranica), kao i provjere normalizacije, aktualnosti manifesta/ključa i
`git diff --check`. Brojčani sadržaj nije mijenjan pa numerički testovi nisu
ponavljani. Ovim zahvatom mijenjaju se samo SVG i interne uredničke upute;
nije napravljen commit ni push.

## Ponovni pregled nakon U15 — 22. rujna 2026.

Polazište: `2a447bf`. Pročitani su kanonski P1–P6 i Z1–Z6, verifier i notebook;
vizualno je pregledano svih sedam referenciranih SVG-ova. Ovaj prošireni
pregled obuhvaća i stvarne pogreške primjera i objašnjenja.

### Matrica prije provedbe

| Mjesto | Postojeći ID i uloga | Odluka i korist | Razina | ID nakon dorade | Veze | Status |
| --- | --- | --- | --- | --- | --- | --- |
| P1 | `ex-u02-pretvorba-dinamicke-u-kinematicku-viskoznost-t1`; pretvorba μ/ρ | ZADRŽATI; osnovni račun; sile na skici vezati uz ploču | T1 | isti | izvor, SVG, verifier, notebook; D06 za Z | provedeno |
| P2 | `ex-u02-smicno-naprezanje-u-tankom-uljnom-sloju-t2`; Couetteov gradijent i sila | ZADRŽATI; prianjanje, sile otpora i odvojen kapilarni prizor | T2 | isti | izvor, SVG, verifier, notebook; D06 za Z | provedeno |
| P3 | `ex-u02-kapilarni-uspon-etanola-u-staklenoj-cjevcici-t1`; kapilarni uspon s θ | ZADRŽATI; stvarni kut 18°, otvoreni uronjeni ulaz i kota razine | T1 | isti | izvor, SVG, verifier, notebook; D06 za Z | provedeno |
| P4 | `ex-u02-kapilarni-mikrodozator-s-izlaznom-kapljicom-t3`; punjenje i izlazna kapljica | PREPRAVITI; odvojiti stanja jedne međupovršine, ukloniti dvostruki kapilarni doprinos i ograničiti statički model | T3 | isti | izvor, SVG, verifier, notebook; D06 za Z | provedeno |
| P5 | `ex-u02-hladni-start-i-radna-temperatura-koliko-kosta`; temperatura i viskozni otpor | ZADRŽATI; popraviti zaokruživanje iz punog računa, sile otpora i prikaz tankog procjepa | T2 | isti | izvor, SVG, verifier, notebook; D06 za Z | provedeno |
| P6 | `ex-u02-mikrofluidicki-kanal-u-lab-on-chip-ure`; kvašenje mikrokanala | ZADRŽATI; definirati predznak tlačnog skoka i granicu idealnog uspona | T2 | isti | izvor, SVG, verifier, notebook; D06 za Z | provedeno |
| Z1 | `task-u02-izme-u-dviju-paralelnih-ploca-nalazi-se`; osnovno smicanje | ZADRŽATI; nužna temeljna tehnika, smjer sila i prianjanje | T1 | isti | izvor, SVG, verifier, notebook; D06 za Z | provedeno |
| Z2 | `task-kapljica-i-sapunasti-mjehur`; kapljica nasuprot filmu | ZADRŽATI; broj međupovršina i stvarna kota promjera | T1 | isti | izvor, SVG, verifier, notebook; D06 za Z | provedeno |
| Z3 | `task-ploca-izmedu-dva-procjepa`; dvije strane ploče | ZADRŽATI; zasebni gradijenti, omjer procjepa i oba otpora | T2 | isti | izvor, SVG, verifier, notebook; D06 za Z | provedeno |
| Z4 | `task-u02-kapilara-promjera-uronjena-je-u-etanol-za`; usporedba dviju kapilara | ZADRŽATI; omjeri promjera i uspona 2:1, isti fluid bez zakrpa | T2 | isti | izvor, SVG, verifier, notebook; D06 za Z | provedeno |
| Z5 | `task-newtonski-model-iz-mjerenja`; izbor konstitutivnog modela iz podataka | ZADRŽATI; obvezni ishod pokriven mjerenjima, uskladiti notebook | T3 | isti | izvor, SVG, verifier, notebook; D06 za Z | provedeno |
| Z6 | `task-u02-kapilarna-igla-unutarnjeg-promjera-spojena-je-na`; intervalna odluka o regulatoru | PREPRAVITI dopunom procjene zanemarenog tlaka unutar kapljice; rezerva idealnog modela ne potvrđuje stvarni uređaj | T4 | isti | izvor, SVG, verifier, notebook; D06 za Z | provedeno |

`rewrite_status=complete`; `rewrite_level=selective`;
`sketch_requirement=provjera i ciljana dorada svih sedam postojećih SVG-ova`.

Ponavljanja su opravdana u Z1/Z4 kao temeljna vježba. Z2 uspoređuje fizikalne
modele, Z3 dijagnosticira pogrešan račun, Z5 ispituje model iz više podataka,
a Z6 provjerava interval i granicu modela. Nije potrebna nova banka zamjena.

Početni nalazi: kapilarni prizor u uvodnoj slici nedostaje; neke oznake sila
nemaju jasno tijelo ili smjer; kut 18° nije geometrijski provjeren. P4 sadrži
pogrešan rezultat 347 Pa jer pribraja izlaznu kapljicu uz još prisutan
konkavni meniskus. P5 računa snage iz prerano zaokruženih međurezultata.
Notebook nije usklađen s aktualnim Z i ne završava pitanjima interpretacije.
Protokol ima obrnuto pravilo konkavnosti za SVG koordinatu y; ispravak pravila
spriječit će ponavljanje iste pogreške.

Fizikalne definicije provjerene su prema MIT 2.25 (Young–Laplace, kontaktni
kut i kapilarni uspon) i MIT NNF (kapilarnost nasuprot gravitaciji):
https://web.mit.edu/2.25/www/225_sect_11.html i
https://web.mit.edu/nnf/education/wettability/gravity.html.
Brojčana procjena tlaka kroz kapljicu autorska je dopuna postojećih podataka,
a ne novi pokus ili specifikacija proizvođača.

### Provedba i provjere

Zadržani su svih šest primjera, šest vježbi, razine i ID-jevi. Osnovne
vježbe ostaju kratke. Z5 i dalje provjerava konstitutivni model na svim
sintetičkim mjernim točkama; Z6 dopunjen je procjenom zanemarenog tlaka
kroz kapljicu. Za Z6 model daje raspon 555,196–591,196 Pa i rezervu
8,804 Pa, dok je skala ρgDmax = 19,581 Pa: pozitivna rezerva u tom modelu
ne potvrđuje stvarni uređaj.

P4 sada odvaja konkavni meniskus pri punjenju od pune igle s formiranom
kapljicom. Pretlaci su 227,423 i 707,423 Pa; prethodni rezultat 347 Pa
nepravilno je oduzimao nepostojeći dodatni meniskus. Izričito su zadani
okolni tlak, zadržavanje kontaktne linije na rubu, zanemarena težina kapljice
i ograničenje na odvojena statička stanja. P5 računa iz punih međurezultata
(579 W i 57,9 W), uz suprotan smjer sile ulja i brzine vratila. U definiciji
površinske sile razdvojene su komponente po obodu; ispravljena je formulacija
kvašenja i preciziran predznak skoka tlaka na konkavnom meniskusu.

Sedam postojećih SVG datoteka zadržava viewBox i sustav panela, paletu,
šrafure i tipografiju. Uvod ponovno sadrži stvarni kapilarni prizor.
Kapilarni fluid ima jednu prostornu ispunu i stvarne uronjene otvore.
Kružni SVG lukovi i vektori imaju provjerene tangente; detalj kontakta mjeri
18° kroz tekućinu. Z3 čuva omjer dvaju procjepa 1:2, Z4 omjer promjera 1:2
i uspona 2:1, a kapljica Z6 spojena je s punom iglom bez unutarnjeg meniskusa.
Promjeri, hod visine i omjeri označeni su uz navedena mjerila. Protokol je
ispravljen tako da konkavnost poštuje SVG os y i stvarni kontaktni kut.

Notebook sada koristi etanol iz Z4, zasebno označenu nastavnu propagaciju
standardne nesigurnosti, Z3, izbor modela Z5 i tlačne bilance P4/Z6.
Sadrži neovisnu provjeru analitičkih derivacija, inverznog rješenja,
energetske bilance smicanja, izmijenjene mjerne točke i granica regulatora;
završava pitanjima interpretacije. Usklađeni su D01, D03, generirani D06,
verifier i manifest. Pri proširenju nisu dodane nove javne task oznake.

Izvršene provjere:

- `verify_u02.py`: 80 provjera, PASS. Tolerancije zaokruženih rezultata
  vezane su uz objavljenu preciznost, uz strojnu toleranciju na polovici
  posljednje znamenke; dodane su provjere predznaka, bilanci i granica.
- `verify_all.py`: 1332 rezultata (1113 golden usporedbi i 219 invarijanti),
  22 dodatne fizikalne provjere, 90/90 ugovora i bez rupa ili tautologija.
- `check_u02_sketch_geometry.py`: PASS za svih sedam stvarnih SVG-ova.
  Vizualno su pregledane i izvorne i konačne rasterizacije; nema teksta
  izvan kadra. Provjera geometrije ne ovisi o privremenom generatoru.
- Notebook izvršen u čistom kernelu: ciljani prolaz 7,05 s; zajednički
  prolaz svih 17 notebookova također PASS (ukupno 55,53 s).
- Struktura publikacije, Typst, normalizacija, manifest, D06, QR i CFD
  paketi: PASS; 87 primjera i 90 vježbi ostaju očuvani.
- HTML U02 na 320/768/1440 px: šest zadataka, tri stara aliasa, jedinstveni
  ID-jevi, 12 sklopivih naputaka/odgovora preko tipkovnice i bez prelijevanja;
  automatizirani WCAG A/AA PASS. D06 ima šest cjelovitih odgovora i povratnih
  poveznica; formule nisu odrezane generatorom.
- Puni HTML i nativni PDF obnovljeni. PDF ima 319 A4 stranica; audit PASS.
  Slike su pregledane na stranicama 33, 36, 40, 41, 42, 44 i 49, tlačna
  bilanca na stranici 43, formula u D01 na 269 i odgovori Z3–Z6 na 301.
- JupyterLite obnovljen; audit potvrđuje aktualnih 17 notebookova,
  četiri ekstenzije i Pyodide. Audit HTML-a: 24 stranice, 222 slike,
  1932 poveznice i 450 sklopivih blokova, PASS.

Fizikalne aproksimacije ostaju izričito označene; ovo nije tvrdnja da je
statička kapljica vjeran model cijeloga procesa doziranja. Završni prolaz kroz
72 prikaza, A4 ispis, WCAG i JupyterLite Python do stanja Idle prošao je
23. rujna 2026.; zajednička evidencija sadrži dovršeni pregled svih zahtjeva.
