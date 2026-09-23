# Autorski ugovor sadržaja MF1

Ovaj ugovor određuje javna i autorska sučelja udžbenika. CI smije odbiti promjenu koja ih krši.

## Semantički blokovi

- `Temelj` — najmanji model potreban za ishode MF1.
- `Izvod` — fizičko pitanje, bilanca, matematički koraci, rezultat i provjera.
- `Fizikalno značenje` — interpretacija bez uvođenja nove algebraičke obveze.
- `Granica modela` — zanemareni članovi, raspon valjanosti i zabranjeni zaključci.
- `Numerički pokus` — predviđanje, račun, provjera pogreške ili konvergencije.
- `Dublje` — sadržaj koji nije potreban za temeljni ishod poglavlja.

Odgovarajuće CSS klase su `.mf1-temelj`, `.mf1-izvod`, `.mf1-fizikalno-znacenje`, `.mf1-granica-modela`, `.mf1-numerika` i `.mf1-dublje`.

Riješeni primjeri i cjeloviti vođeni zadatci prikazuju se bez vertikalne crte
i bez lijeve uvlake cijelog bloka. Naslov izravno imenuje problem, primjerice
„Vrijeme odziva pneumatskog voda”, bez prefiksa „Riješeni primjer —”,
„Kratki primjer —” ili „Cjeloviti zadatak —”. Semantička klasa, stabilni ID
i oznaka razine ostaju uz primjer; ovo pravilo vrijedi za HTML i PDF.

Ispred prikazanog naslova primjera stoji P1, P2, … redom unutar poglavlja.
Oznake generira zajednički sadržajni model; ne upisuju se u izvorni naslov
niti su dio stabilnog ID-ja. `scripts/build_book.py --write` obnavlja indeks.
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

## Ugovor slike

Svaki SVG ima `viewBox`, `role="img"`, povezane `title` i `desc`, stabilan prefiks ID-jeva, relativnu širinu i čitljiv tekst pri konačnoj veličini. Boja nije jedini nositelj značenja, a alternativni opis govori o fizikalnoj poruci umjesto o internim oznakama izrade.
