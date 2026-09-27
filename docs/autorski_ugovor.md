# Autorski ugovor sadržaja MF1

Ovaj ugovor određuje javna i autorska sučelja udžbenika. CI smije odbiti promjenu koja ih krši.

## Semantički blokovi

- `Temelj` — najmanji model potreban za ishode MF1.
- `Izvod` — fizičko pitanje, bilanca, matematički koraci, rezultat i provjera.
- `Fizikalno značenje` — interpretacija bez uvođenja nove algebraičke obveze.
- `Računalna dinamika fluida` — kratak primjer primjene CFD-a povezan s temom poglavlja: inženjersko pitanje, fizikalni model, potrebni podatci, očekivani izlazi i njihova provjera. Formule se tumače unutar širega problema.
- `Granica modela` — zanemareni članovi, raspon valjanosti i zabranjeni zaključci.
- `Numerički pokus` — predviđanje, račun, provjera pogreške ili konvergencije.
- `Dublje` — sadržaj koji nije potreban za temeljni ishod poglavlja.

Odgovarajuće CSS klase su `.mf1-temelj`, `.mf1-izvod`, `.mf1-fizikalno-znacenje`, `.mf1-cfd`, `.mf1-granica-modela`, `.mf1-numerika` i `.mf1-dublje`.

Odlomci `Računalna dinamika fluida` umeću se uz pripadnu fiziku kroz sva glavna
poglavlja. Imaju zajednički naslov i konkretan tematski uvod, obično jedan
ili dva odlomka. Objašnjavaju što želimo saznati o uređaju ili pojavi, što
zadajemo, što računamo i kako rezultat podupire odluku. Mogu povezivati više
formula i najaviti potrebnu fiziku iz kasnijih poglavlja uz kratko objašnjenje.
Povezani primjeri zadržavaju prepoznatljiv sustav i jasno navode novo pitanje
ili proširenje modela: primjerice od podjele protoka u rashladnoj ploči do
njezina toplinskog rada i radne točke crpke. Ne ostaju samo prijevod neposredno
prethodne formule i ne predstavljaju svaki računalni pokus kao CFD.
Novi pojam objašnjava se pri prvom spomenu; opis primjene ne predstavlja
izmišljene brojčane rezultate kao izvedenu simulaciju ili mjerenje.
Komponenta `CFDContext` u registru određuje prikaz u webu, PDF-u i ispisu.

Riješeni primjeri i cjeloviti vođeni zadatci prikazuju se bez vertikalne crte
i bez lijeve uvlake cijelog bloka. Naslov izravno imenuje problem, primjerice
„Vrijeme odziva pneumatskog voda”, bez prefiksa „Riješeni primjer —”,
„Kratki primjer —” ili „Cjeloviti zadatak —”. Semantička klasa, stabilni ID
i oznaka razine ostaju uz primjer; ovo pravilo vrijedi za HTML i PDF.

Ispred prikazanog naslova primjera stoji P1, P2, … redom unutar poglavlja.
Oznake generira zajednički sadržajni model; ne upisuju se u izvorni naslov
niti su dio stabilnog ID-ja. `scripts/build_book.py --write` obnavlja indeks.

### Jedinstveni obrazac zadavanja i rješavanja

U svih 15 poglavlja riješeni primjeri imaju zasebna polja **Tekst zadatka**,
**Traži se**, **Rješenje** i **Provjera i tumačenje**, tim redom.
Tekst zadatka objedinjuje kratak opis sustava, zadane veličine s vrijednostima
i nužne pretpostavke. Ne dodaju se zasebni odlomci **Kontekst**, **Zadano**
i **Pretpostavke i model** koji ponavljaju iste informacije. Obrazloženje
izbora jednadžbi pripada rješenju.
Samostalni zadatci imaju **Tekst zadatka** i **Traži se**; naputak i kontrolni
rezultat ostaju zasebne komponente prema pravilima njihove vidljivosti.

Oznake polja pišu se podebljano u vlastitom odlomku, bez točke i dvotočke.
Podatci i uvjeti modela pišu se u kratkim smislenim rečenicama, bez dodatnog
popisa istih veličina. Tablice zadržavaju mjerne nizove i usporedive varijante.
Za alternativna stanja
jasno se navodi na koje se stanje zahtjev odnosi. Više zahtjeva piše se
kao numerirani popis, a jedan zahtjev kao kratki odlomak. Izbjegava se
ponavljanje istog zahtjeva u uvodu i u popisu.

Skica zadatka prikazuje geometriju, zadane veličine, smjerove i nepoznanice.
U skici ostaju samo kote, oznake veličina i kratki opisi prizora. Osnovne
relacije, ključni principi, upute i dulja objašnjenja pišu se kao obični
odlomci neposredno ispod slike, s prirodnom oznakom poput „Veza s proračunom”,
„Tumačenje skice” ili „Napomene uz skice”. Ne dodaju se bočni tekstni paneli.
Brojčane zamjene, međurezultati i kontrolni rezultati pripadaju rješenju, pa se
ne ponavljaju u bočnom računskom panelu ni u opisu skice. Dijagrami koji
uspoređuju modele ili prikazuju traženu fizikalnu ovisnost zadržavaju svoje
osi i podatke; trokuti brzina, dimenzijska matrica i dijagram odluke zadržavaju
oznake potrebne za čitanje njihovih odnosa. Skice samostalnih zadataka ne
otkrivaju njihov postupak.

Dulji postupak rješenja dijeli se na korake klase `.mf1-step`, izvan
brojanja sekcija. Provjera i tumačenje sadrže stvarno provedenu provjeru,
značenje rezultata ili ograničenje modela; ne dopisuju se prazne rubrike.
PDF koristi zajednički razmak odlomaka i stavki za primjere i zadatke;
oznake polja ostaju uz sljedeći sadržaj. Završna oznaka razine ostaje uz
posljednji zahtjev, a dulji se blok smije prelomiti na više stranica.
Koraci rješenja imaju istu razinu naslova i klase
`.unnumbered .unlisted .mf1-step`, pa zadržavaju samo svoj broj 1., 2., 3.
i ne mijenjaju numeraciju ni sadržaj poglavlja.

Kratke napomene o računalnim proračunima imaju opisni naslov i polaze od
fizikalnog primjera. Novi pojam odmah se objašnjava običnim jezikom; nazivi
algoritama i detalji numeričkih metoda pripadaju dodatnom gradivu.

## Stabilni identifikatori

ID opisuje fizikalni sadržaj, a ne trenutačni broj retka ili redni broj unutar poglavlja:

- primjer: `ex-priguseni-ventil`;
- zadatak: `task-priguseni-protok`;
- jednadžba: `eq-priguseni-protok`;
- slika: `fig-kompresibilni-pregled`;
- odjeljak: `sec-sapnica-prigusenje`.

Premještanje sadržaja ne mijenja ID. Ako se javni URL poglavlja promijeni, stari URL ostaje kao preusmjerenje najmanje kroz jedno glavno izdanje.

Naslijeđeni identifikatori koji sadržavaju oznaku `uNN` ne preimenuju se
retroaktivno: čuvaju se radi postojećih javnih poveznica, bilježaka i QR kodova.
Svaki novi identifikator mora biti čisto semantički i ne smije kodirati broj
poglavlja ni trenutačni položaj sadržaja.

## Ugovor zadatka i verifikatora

Samostalni zadatci nose oznake Z1–Z6 unutar poglavlja i kratak naslov problema.
Razina T1–T4 navodi se na kraju zadatka, sitno i desno poravnata, odvojeno
od lijeve numeracije. Naslov se zapisuje kao
`### Naslov problema {#task-stabilni-id .unnumbered .unlisted}`,
a oznaka razine kao `[Razina: T1]{.mf1-task-level}`. Time zadatak ne dobiva
dodatni broj odjeljka niti ulazi u sadržaj knjige. Iste oznake i naslovi
automatski se prenose u ključ rezultata; generator izvodi neprekinuti
redoslijed Z1–Z6. Skice koriste oznake Z1–Z6. Pri upućivanju na zadatak
izvan njegova poglavlja navodi se i broj poglavlja.

Nove komponente koriste zajedničke predloške iz
[arhitekturnog vodiča](arhitektura.md), bez vlastitog HTML-a i CSS-a.
Razina zadatka ulazi u indeks kao podatak, a sve prikaze oblikuje isti
adapter. Numeriranje ne zamjenjuje provjeru podudarnosti teksta i skice:
ako se promijeni redoslijed zadataka, moraju se uskladiti i oznake u SVG-u.

Manifest zadataka koristi **shemu v2**. Kanonski dio reproducibilno se generira
iz `source/`; ručna izmjena generiranih polja nije dopuštena. Za svaki od 90
samostalnih zadataka manifest mora navesti:

- stabilni ID, izvorni dokument i autoritativni tekst zadatka;
- ulaze, SI jedinice i pretpostavke;
- objavljene izlaze i tolerancije;
- barem jednu neovisnu provjeru: dimenzije, bilancu, predznak, granični slučaj ili red veličine;
- pripadajući verifier ID i funkciju verifikatora koja rezultat ne uspoređuje sa samim sobom.

Svaki zadatak pripada točno jednoj skupini `golden` ili `invariant`; skupine
`gap` i `self-comparison` nisu dopuštene. Tekst, odgovor, slika, notebook i
verifikator koriste isti skup podataka.

## Ugovor notebooka

Notebook mora:

1. biti determinističan ili imati fiksno sjeme;
2. započeti studentskim predviđanjem;
3. sadržavati barem dvije neovisne izvršive numeričke tvrdnje (`assert`/`isclose`);
4. obuhvatiti analizu pogreške, konvergencije, osjetljivosti, reziduala ili
   nesigurnosti primjerenu problemu;
5. završiti pitanjima interpretacije;
6. izvršiti se od početka u CI-ju bez ručne intervencije.

Tri ogledna interaktivna laboratorija (rotirajući spremnik, Venturi i
Poiseuille) dodatno koriste `ipywidgets`, `IPython.display` te standardne
module `html` i `inspect` za sučelje i prikaz stvarnog izvornog koda.
Označena početna ćelija smije preko `piplite` asinkrono učitati pinane
widgete kada nedostaju u Pyodideu; ostale ćelije ostaju običan Python.
Računski modeli ostaju odvojeni od sučelja, uz postojeće znanstvene ovisnosti
NumPy/Matplotlib. Bilježnice su samostalne i ne uvoze lokalne pomoćne module
koji nedostaju pri pojedinačnom otvaranju u Colabu.

Svaki laboratorij sadrži označene ćelije pripreme, modela, zajedničkog sučelja i
prikaza. Zadržava prethodne računske provjere, jasno razlikuje nevaljan ulaz
od granice fizikalnog modela te omogućuje usporedbu i resetiranje. Uz
izvršenje bilježnice CI provjerava stvarnu promjenu kontrola i rezultata u
JupyterLiteu; sama spremnost kernela nije dokaz interaktivnosti.

## Ugovor slike

Svaki SVG ima `viewBox`, `role="img"`, povezane `title` i `desc`, stabilan prefiks ID-jeva, relativnu širinu i čitljiv tekst pri konačnoj veličini. Boja nije jedini nositelj značenja, a alternativni opis govori o fizikalnoj poruci umjesto o internim oznakama izrade.
