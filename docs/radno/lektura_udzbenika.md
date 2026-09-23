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
| U04 | Predstoji | |
| U05 | Predstoji | |
| U06 | Predstoji | |
| U07 | Predstoji | |
| U08 | Predstoji | |
| U09 | Predstoji | |
| U10 | Predstoji | |
| U11 | Predstoji | |
| U12 | Predstoji | |
| U13 | Predstoji | |
| U14 | Predstoji | |
| U15 | Predstoji | |
| D01–D05 | Predstoji | |
| D06 | Predstoji | Generiranje i pregled nakon lekture izvora |
| Tekst u skicama i čitateljske upute | Predstoji | |

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
Ovaj međukommit obuhvaća početnu stranicu i prvi jezični prolaz kroz U00–U03;
lektura ostatka udžbenika i završni zajednički prolaz još predstoje.

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
