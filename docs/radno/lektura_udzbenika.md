# Lektura udžbenika

Zahtjev: „Sada kreni na lekturu udžbenika.” Polazište: `521c0ad`,
23. rujna 2026. Lektura je dovršena; završne dorade i obnovljena izdanja
spremljeni su lokalno.

Lektura obuhvaća javni tekst početne stranice, U00–U15, dodatke D01–D06,
opise i tekst korištenih skica te pripadajuće upute čitatelju. Provjeravaju se
pravopis, gramatika, interpunkcija, jasnoća i dosljednost stručnih naziva.
Čuvaju se sadržaj modela, brojčani podatci, formule, stabilni identifikatori,
poveznice, raspored primjera i zadataka te grafička geometrija.

Kanonski se tekst uređuje u `source/`; ključ D06 i manifest obnavljaju se
generatorima. Jezični pregled i tehničke provjere evidentiraju se zasebno.

## Evidencija pregleda

| Sadržaj | Jezični pregled | Napomena |
| --- | --- | --- |
| Početna i U00 | Proveden prvi prolaz | Impresum, slaganje imenica i pridjeva, upute za PDF i upućivanja |
| U01 | Proveden prvi prolaz | Padeži, rečenice uz formule, navodnici, tlačni doprinosi i fizikalna točnost |
| U02 | Proveden prvi prolaz | Nazivi viskoznih modela, tlačni skok, dvojnina, opisi opne, međupovršina i mreže |
| U03 | Proveden prvi prolaz | Tlačne sile, slaganje, dijakritici, obraćanje u jednini, jasniji postupci manometrije |
| U04 | Proveden prvi prolaz | Razlika razina i nagib, brzina vrtnje, stijenke, slaganje i opisi relativnog mirovanja |
| U05 | Proveden prvi prolaz | Obraćanje u jednini, kvašene plohe, iznosi sila, stručni nazivi i preciziranje numeričkih provjera |
| U06 | Proveden prvi prolaz | Dijakritici, slaganje, nazivi slobodnog boka, opis uzgona i metacentarske aproksimacije |
| U07 | Proveden prvi prolaz | Navodnici, stručni nazivi, kontrolni volumen, akumulacija i srednje brzine |
| U08 | Proveden prvi prolaz | Dijakritici, tlačna visina, opisi rada i energije, sifona i neporemećene struje |
| U09 | Proveden prvi prolaz | Slaganje, kompresibilni račun, Machov broj i upute za bilježnicu |
| U10 | Proveden prvi prolaz | Tlačne sile, dijakritici, Newtonov zakon, smjerovi i jezično razlikovanje sile i toka količine gibanja |
| U11 | Proveden prvi prolaz | Bezdimenzijske skupine, slaganje, usporedbe, upućivanja i aktualni opseg kolegija |
| U12 | Proveden prvi prolaz | Nazivi modela, uvjet prianjanja, granični sloj, mrežna konvergencija i opisi nesigurnosti |
| U13 | Proveden prvi prolaz | Slaganje, bilanca pretvorbe energije, radna točka, opisi grana i upute za bilježnicu |
| U14 | Proveden prvi prolaz | Relativni protok, sile, tok količine gibanja, dijakritici i slaganje |
| U15 | Proveden prvi prolaz | Nazivi presjeka, rubovi kontrolnog volumena, kritičnost i upute za bilježnicu |
| D01–D05 | Proveden prvi prolaz | Stručni nazivi, pretpostavke formula, pojmovnik i opisi CFD postupaka |
| D06 | Obnovljen i pregledan | Formule svih 90 kontrolnih odgovora očuvane; provjeren prikaz sažetaka i odgovora |
| Tekst u skicama | Proveden prvi prolaz kroz 94 korištene skice | Jezične izmjene u 46 SVG-ova; geometrija i brojčane oznake očuvane |
| Markdown u bilježnicama | Proveden prvi prolaz kroz 17 bilježnica | Izmjene u 11 bilježnica; programske ćelije i formule očuvane |
| Ostale čitateljske upute i programski natpisi bilježnica | Pregledano | Omotači, navigacija, ispis, QR opisi, upute za bilježnice i četiri opisa CFD paketa; ispravljeni natpisi u šest bilježnica |

## Završne provjere

Provedene su usporedbe s polazištem, provjere generatora, numerike i
strukture te pregled obnovljenog HTML-a i PDF-a. Međuprovjere ispod slijede
redoslijed rada; završni rezultat naveden je na kraju evidencije.

Međuprovjera nakon U03: svih 5.306 matematičkih izraza i eksplicitni stabilni
identifikatori kanonskih izvora ostali su jednaki polazištu (generirani D06
provjerava se nakon obnove). To je provjera očuvanja, a ne dokaz jezične kvalitete.

### Provjere prije međukommita U00–U03

Na zahtjev za commit i push obnovljeni su D06 i manifest za svih 90 zadataka.
Prošli su numerički verifieri (1.113 usporedbi s neovisnim ciljevima,
219 invarijanti i 22 dodatne fizikalne provjere), audit strukture publikacije,
audit autorskih blokova za Typst, provjere javnih referenci, alternativnog
teksta, QR poveznica, ključa zadataka i CFD podataka te `git diff --check`.
Matematički izrazi i stabilni identifikatori ostali su sačuvani.
Izgradnja i provjere objavljenih izdanja pokreću se u GitHub Actions nakon pusha.
Za commit `81b19cc` uspješno su završili izgradnja i objava u
[GitHub Actions](https://github.com/martibasic/MF1_udzbenik/actions/runs/35838723142),
uključujući notebooke, HTML, PDF, JupyterLite i pregled prikaza na više širina.
Taj rezultat odnosi se na objavljeni U00–U03, ne na kasnije lokalne dorade.
Ovaj međukommit obuhvaća početnu stranicu i prvi jezični prolaz kroz U00–U03;
lektura ostatka udžbenika i završni zajednički prolaz još predstoje.

### Provjere prije međukommita U04–U13

Na zahtjev za commit i push obnovljeni su D06 i manifest. Prošli su svi
numerički verifieri (1.113 usporedbi s neovisnim ciljevima, 219 invarijanti
i 22 dodatne fizikalne provjere), audit publikacije i Typsta, provjere javnog
teksta, QR poveznica, ključa i CFD podataka te `git diff --check`.
Očuvano je svih 5.306 matematičkih izraza i stabilni identifikatori izvora.

Pri regeneraciji D06 pronađeno je rezanje sažetka usred formule. Generator
sada dovršava cijeli izraz prije trotočke, čak i kada time prelazi poželjnu
duljinu sažetka. Provjereni su prijelomi prije, unutar i nakon formula,
izraz na početku teksta i doslovni znak dolara. Generirani ključ nema
nezatvorenih matematičkih oznaka; formule svih 90 kontrolnih odgovora
jednake su prethodnom commitu. HTML, PDF i cjelovite provjere objave
izvršit će GitHub Actions nakon pusha.

Ovaj međukommit obuhvaća prvi prolaz U04–U13. U14–U15, dodatci,
tekst u skicama i završni zajednički pregled još predstoje.

### Provjere prije međukommita U14–U15, dodataka i natpisa

Na zahtjev za commit i push obnovljeni su D06 i manifest svih 90 zadataka.
Prošli su numerički verifieri (1.113 usporedbi s neovisnim ciljevima,
219 invarijanti i 22 dodatne fizikalne provjere), audit publikacije i Typsta,
provjere javnog teksta, QR poveznica, ključa i CFD podataka. Svih 17
bilježnica uspješno je izvršeno u čistim kernelima.

Sačuvano je svih 5.306 matematičkih izraza i eksplicitnih identifikatora
kanonskih izvora u odnosu na polazište. U odnosu na prethodni commit
sačuvane su formule ključa D06, uključujući svih 90 kontrolnih odgovora,
te programske ćelije i formule svih bilježnica. U 46 izmijenjenih SVG-ova
sačuvani su elementi, atributi, geometrija i brojčane oznake. Provjera
tekstualnih okvira u pregledniku prije i nakon izmjena nije pronašla
međusobna preklapanja natpisa ni izlazak teksta iz okvira skice.

Ovo je međukommit prvog prolaza kroz U14–U15, D01–D05, tekst svih
94 korištenih skica i Markdown svih 17 bilježnica. Završni zajednički
jezični pregled, preostale čitateljske upute i pregled obnovljenih izdanja
još predstoje. Izgradnju HTML-a i PDF-a te provjere objave pokreće
GitHub Actions nakon pusha; prethodni render nije dokaz za ove izmjene.

## Zajedničke odluke za završni prolaz

- Zadržati hrvatski stručni naziv „newtonski fluid”; odnosni pridjev pisati
  malim početnim slovom, osim na početku rečenice. „Newtonov zakon” ostaje
  posvojni pridjev s velikim slovom. Ujednačiti varijante u javnim tekstovima.
- Ispraviti pogrešno izvedene oblike „tlakni/tlakna” u „tlačni/tlačna”.
- Za provjeru fizikalnog modela rabiti „fizikalni”; „fizički” zadržati kada
  označuje stvarnu, materijalnu granicu ili predmet.
- Dosljedno primijeniti postojeće obraćanje u jednini i nazive „zadatci”,
  „podatci” i „gubitci” u uredničkom tekstu; ne mijenjati citirane naslove,
  identifikatore ni programske nazive.
- Pregledati početna slova naputaka, navodnike, crtice i rečenice razdvojene
  umetnutim autorskim blokovima. Ne prepisivati ispravne rečenice bez potrebe.

Jezične nedoumice provjeravaju se prema [Hrvatskom pravopisu](https://pravopis.hr/)
i stručnom nazivlju [Tehničke enciklopedije — mehanika fluida](https://tehnika.lzmk.hr/tehnickaenciklopedija/mehanika_fluida_dinamika_fluida.pdf).

## Sadržajna pojašnjenja uočena pri lekturi

- U04: u sažetoj tvrdnji s duljinom spremnika raste razlika razina, a ne nagib.
  Ispravljena je imenica; izvod i sve jednadžbe ostaju isti. Broj okretaja u
  jedinici vremena naziva se brzinom vrtnje, uz razlikovanje kutne brzine.
- U05: usporedba s analitičkim rješenjem naziva se verifikacijom, a ne
  validacijom. Postojećih 2 % pojašnjeno je kao mogući kriterij nastavne
  usporedbe, a ne univerzalni prag. Stabilizacija sile sama ne dokazuje
  konvergenciju ni fizikalnu točnost. Opisi izlaza CFD-a razlikuju sile,
  momente i njihove koeficijente te tlačne i viskozne doprinose.
  Provjereno prema [dokumentaciji OpenFOAM-a za `forces`](https://doc.openfoam.com/2606/tools/post-processing/function-objects/forces/forces/)
  i [NASA-inim uputama za verifikaciju i validaciju CFD-a](https://www.grc.nasa.gov/www/wind/valid/tutorial/tutorial.html).

- U06: uklonjena je tvrdnja o uzgonu u idealnom vakuumu; razjašnjeno je da
  šuplje tijelo mora isključiti prodor fluida za istu vanjsku istisninu.
  U P5 sila podizanja odnosi se na potpuno uronjeno kućište, što odgovara
  postojećoj skici bez dodira s dnom. Negativni početni GM opisan je kao
  povećanje malog nagiba, bez tvrdnje o nužnom konačnom prevrtanju.
- U07: nulta akumulacija mase nije poistovjećena sa stacionarnošću cijeloga
  strujanja. Za kontinuitet se koriste srednje brzine; nije potreban jednolik
  profil. U P4 izričito su navedene pretpostavke stalnih protoka, aditivnosti
  volumena i početnog sastava koje koristi postojeći račun. Primjer brzine
  u hidrauličnom vodu označen je kao ilustrativan izbor, a ne opća preporuka.

- U08: uspoređuju se tlakovi međusobno ili tlačne visine međusobno.
  Torricellijev izvod zadržava razliku geodetskih visina. U alternativnom
  izvodu Bernoullijeve jednadžbe pojašnjeni su rad tlaka i bilanca kinetičke
  energije. Koeficijent istjecanja odnosi se na protok i uključuje kontrakciju;
  nije automatski samo korekcija brzine. Ispravljeno je upućivanje na poglavlje
  13 i dodatak D te ograničena provjera Bernoullija na pripadne strujnice.

- U10: u objašnjenju Eulerove jednadžbe materijalno ubrzanje odnosi se na
  izraz u zagradi, dok cijela lijeva strana uključuje gustoću. Razlikuju se
  sila konstrukcije na fluid, ukupna vanjska sila i tok količine gibanja.
  Atmosferski tlak u primjeru mlaza odnosi se na slobodne presjeke, ne na
  svaku točku udarne zone.
- U11: uklonjene su zaostale tvrdnje da kolegij završava ovim poglavljem i
  obuhvaća samo integralni nestlačivi opis. Upućivanja prate aktualna poglavlja
  o stlačivom toku, diferencijalnom opisu i otvorenim tokovima. Dvije važne
  bezdimenzijske skupine ne znače automatski nemogućnost potpune sličnosti;
  naglašena je provjera mogućnosti njihova istodobnog očuvanja.

Međuprovjera nakon U13: svih 5.306 matematičkih izraza i eksplicitni stabilni
identifikatori kanonskih izvora i dalje su jednaki polazištu.

- U14: razlikuju se relativni protok kroz pomični kontrolni volumen i
  protok cijelog mlaza kroz rotor. Sile i momenti imaju predznak, a tok
  količine gibanja razlikuje se od impulsa sile. Nisu mijenjane jednadžbe.
- U15: rubni presjeci kontrolnog volumena hidrauličkog skoka nalaze se
  izvan valjka; sam kontrolni volumen obuhvaća skok. Kalibracija hrapavosti
  odvojena je od provjere geometrije, dotoka i rubnih vodostaja.
- D04: razjašnjeni su tlak bez hidrostatičkog doprinosa, vanjske granice
  mreže, MRF i klizajuća mreža te razlika sila i njihovih koeficijenata.
  Centar uzgona vezan je uz istisnuti volumen tijela. Dokumentacijska podloga:
  [OpenFOAM — p_rgh](https://doc.openfoam.com/2212/tools/processing/solvers/algorithm-p-rgh/),
  [granice mreže](https://www.openfoam.com/documentation/user-guide/4-mesh-generation-and-conversion/4.2-boundaries)
  i [forceCoeffs](https://doc.openfoam.com/2306/tools/post-processing/function-objects/forces/forceCoeffs/).

## Zajednički jezični pregled i obnova izdanja

Pregledani su preostali čitateljski tekstovi u Quarto omotačima, navigaciji,
HTML alatnoj traci, opisima QR kodova, bibliografskim bilješkama, uputama za
bilježnice i četiri README opisa CFD paketa. Pregled obuhvaća i tekst u
sirovim HTML blokovima te jezične oznake unutar matematičkih izraza.
Ujednačeni su nazivi, obraćanje čitatelju i početna slova 24 opisa slika;
usklađen je i pripadajući alternativni tekst. Zastarjele upute za generiranje
bilježnica zamijenjene su postupkom koji čuva aktualne izvore.

Prikaz naslova „Zadatci za vježbu” i „Zadatci za samostalan rad” ujednačen
je postojećim uredničkim filtrom. Izvorni naslovi zadržavaju oblik „Zadaci”
da njihove automatski izvedene oznake i postojeće poveznice ostanu iste.
Oba su oblika pravopisno dopuštena; riječ je o dosljednosti javnog prikaza.

Vidljivi natpisi u 17 bilježnica pregledani su zasebno od Markdown teksta.
Devet programskih ćelija u šest bilježnica ima izmjene isključivo tekstualnih
literala (nazivi, padeži i zapis jedinica); usporedba sintaksnih stabala s
polazištem potvrđuje očuvanje računskih izraza. U kanonskom rukopisu
sačuvano je svih 5.306 matematičkih izraza i eksplicitnih identifikatora.
Razlike brojčanih oznaka izvan matematike odnose se samo na nazive i
upućivanja na poglavlja te preciziranje postojećih oznaka izlaznih grana 2 i 3.

Vizualno su pregledani izmijenjeni natpisi svih 31 SVG-a s razlikom u
prikazanim pikselima. U ostalih 15 mijenjan je samo pristupačni naslov ili
opis; prikaz je jednak prethodnom. Mjerenje tekstualnih okvira svih 46
izmijenjenih skica nije pronašlo međusobna preklapanja natpisa ni izlazak
iz okvira slike. Geometrija i brojčane oznake ostale su sačuvane.

Pri usporedbi obnovljenog HTML-a vraćene su dvije stare automatske oznake
naslova (tlačni skok u U02 i korak rješavača u D04). Sada su eksplicitne;
inačice iz međukommita ostale su kao dodatna odredišta istih naslova.
Stara i nova poveznica tako vode na isti sadržaj. Urednički filtar dopunjen
je za numerirana zaglavlja, uz očuvanje njihovih oznaka i brojeva.

Vizualni pregled otkrio je nečitljivo uske stupce CFD pojmovnika na mobitelu.
Za tu tablicu dodana je minimalna širina samo na uskim zaslonima; postojeća
regija omogućuje vodoravno pomicanje. PDF i prikaz na širokom zaslonu time
se ne mijenjaju.

PDF profil sada izričito uključuje isti urednički filtar kao HTML. Time se
ujednačen oblik naslova zadataka prikazuje i u PDF-u i u njegovu sadržaju.
Vizualni uzorak obuhvatio je 38 stranica PDF-a: naslovnicu, sadržaj, uvod,
početke svih 15 poglavlja, zahtjevnije odlomke U14–U15, tablice formula i
pojmovnika, dodatke C–E te ključ odgovora. Pri tome je naziv uz izraz
relativne brzine u tablici D04 ispravljen iz „Moment količine gibanja” u
„Relativna brzina”; formula ostaje ista.

Commit `fc241d0` uspješno je izgrađen i objavljen u
[GitHub Actions](https://github.com/martibasic/MF1_udzbenik/actions/runs/35842824195).
To je potvrda prethodnog međukommita; kasnije završne dorade provjeravaju
se lokalno i nisu uključene u taj rezultat.

Cjelovita lokalna izgradnja pokrenuta je naredbom `scripts/izgradi.ps1`.
Nakon navedenih nalaza obnovljeni su izlazi i ponovljene relevantne provjere.
Raniji pregledi prikaza namjerno su prekinuti jer nisu obuhvaćali završne
ispravke; njihov nepotpun rezultat ne računa se kao prolaz.

## Završni rezultat — 23. rujna 2026.

Lektura javnog rukopisa, opisa i natpisa korištenih skica, bilježnica i
pripadajućih uputa je dovršena. Prvi prolaz po cjelinama dopunjen je
zajedničkim pregledom nazivlja, obraćanja, početnih slova, uputa i prikaza.

| Provjera | Rezultat |
| --- | --- |
| Numerika i pokrivenost | 19 modula; 1.113 usporedbi s neovisnim ciljevima, 219 invarijanti i 22 dodatne fizikalne provjere; 90/90 ugovora, bez rupa i tautologija |
| Struktura i resursi | 15 poglavlja, 87 riješenih primjera, 90 zadataka, šest dodataka, 795 prikazanih jednadžbi, 94 skice i 17 bilježnica; audit prolazi |
| Očuvanje sadržaja | 5.306 matematičkih izraza, formule 90 kontrolnih odgovora, stari identifikatori, računska sintaksna stabla bilježnica te SVG geometrija i brojčane oznake sačuvani |
| Generirani sadržaj | Ključ, manifest i QR kodovi aktualni; javne reference, alternativni tekst, Typst blokovi i CFD podatkovni paketi prolaze provjere |
| Bilježnice | Svih 17 uspješno izvršeno u čistim kernelima |
| HTML | 24 stranice, 222 prikaza slika, 2.091 poveznica i 450 sklopivih blokova; audit prolazi; sačuvana odredišta naslova i ujednačeni naslovi zadataka |
| Pristupačnost i širine | 72 prikaza na 320/768/1.440 px, A4 ispis, tipkovnica, lokalno pomicanje tablica, povećavanje skica i JupyterLite Python `Idle`: prolaz |
| PDF | 321 A4 stranica; audit metapodataka, sadržaja i slika prolazi; nijedan tekstualni blok nije izvan stranice; vizualno pregledano 38 odabranih stranica |
| Završna ispravka D04 | Obnovljeni D04, pregled za ispis i PDF; ponovljeni audit PDF-a, resursa JupyterLitea, HTML-a i očuvanja sadržaja; provjeren naziv relativne brzine i prikaz D04 na 320 i 1.440 px |
| Datoteke | `git diff --check` prolazi; PDF u `_book/` i njegova kopija u `_site/downloads/` imaju jednak SHA-256 |

Nakon posljednje ispravke u vizualnom uzorku promijenila se samo stranica
295; ponovno je pregledana. Ostalih 37 rastera ostalo je jednako.
JupyterLite datoteke pri posljednjoj ciljanoj obnovi nisu ponovno građene;
njihov je inventar ponovno provjeren, a uspješno pokretanje kernela potvrđeno
je prethodnim cjelovitim pregledom istih bilježnica.

Završni PDF: `_book/mehanika-fluida-1.pdf`.
SHA-256: `295fc447a5728124112d8b64d0c902df34a66d5bccdadf98bf7ca148c7b73b2f`.
Radni logovi i rasteri nalaze se u ignoriranoj mapi `tools/tmp/lektura/`.
Jezični pregled nije zamjena za zasebnu vanjsku stručnu recenziju modela
i nastavnu evaluaciju udžbenika.
