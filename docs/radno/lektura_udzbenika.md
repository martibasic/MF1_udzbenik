# Lektura udžbenika

Zahtjev: „Sada kreni na lekturu udžbenika.” Polazište: `521c0ad`,
23. rujna 2026. Rad je u tijeku.

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
| D06 | Obnovljen prema dosadašnjoj lekturi | Pregledana razlika; formule svih 90 kontrolnih odgovora očuvane |
| Tekst u skicama | Proveden prvi prolaz kroz 94 korištene skice | Jezične izmjene u 46 SVG-ova; geometrija i brojčane oznake očuvane |
| Markdown u bilježnicama | Proveden prvi prolaz kroz 17 bilježnica | Izmjene u 11 bilježnica; programske ćelije i formule očuvane |
| Ostale čitateljske upute i programski natpisi bilježnica | U tijeku | Predstoji dovršetak pregleda i zajedničko ujednačavanje |

## Završne provjere

Predstoje usporedba matematičkih izraza i identifikatora s polazištem,
provjere generatora, numerike i strukture te pregled obnovljenog HTML-a i PDF-a.

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
