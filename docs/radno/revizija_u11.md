# Revizija U11 — dimenzijska analiza i sličnost

## Opseg i dijagnoza prije provedbe (22. rujna 2026.)

Nakon korisnikova zahtjeva izvršen je commit/push dovršenih U09/U10
(`f12187b`). Nastavlja se U11, kanonski izvor
`source/u11_dimenzijska_analiza_i_slicnost.md`, verifier `verify_u14.py`,
namespace `U14`, notebook `u14_cd_re_kugla.ipynb`. Povijesna imena datoteka
nisu brojevi aktualnih poglavlja. Omotač ostaje nepromijenjen.

Čuvaju se šest primjera i šest vježbi T1/T1/T2/T2/T3/T4. Z1 i Z2 korisni su
kratki računi uz SI pretvorbe i provjeru modela gustoće. Z3 ima opravdanu
temu izbora referentnog tlaka, ali treba stvarnu odluku s pretlakom i
obrnutim računom granice. Z4 gotovo potpuno ponavlja P4: izračunati We i
usporediti isti prag. Z5 čuva obvezni puni Buckinghamov postupak. Z6 zasad
izravno primjenjuje skaliranje P2, uz kvalitativnu napomenu; T4 se ojačava
stvarnom usporedbom sintetičkih podataka i odabirom izvedivog pokusa.

Zajednički SVG još ima osam starih mjesta i ne odgovara Z1–Z6. Uvodni
caption opisuje brod, a crtež aerotunel; zatvoreni rubovi tunela izgledaju
kao pregrade. P1 prikazuje kružiće nalik mjehurićima i nepotpun prikaz
laminarnog profila. P2 nema geometrijski jednake trupove ni oznaku odvojenih
grafičkih mjerila. P3 smješta oznaku brzine grla u difuzor, a ilustrativna
krivulja tlaka ne razlikuje neostvarivi jednofazni rezultat od stvarnog
tlaka. P4 prikazuje površinsku napetost kao dvije radijalne sile i ne kotira
početni promjer. P5 preklapa kotu i silu, a krivulja otpora zahtijeva jasno
naveden model i pravilne logaritamske osi. P6 dimnjak je prikazan kao ravna
pregrada, bez jasne projekcije kružnog presjeka i smjerova vrtloga.

## Matrica zamjena prije provedbe

| Mjesto | Postojeći ID i uloga | Odluka i didaktička korist | Razina | Završni ID | Povezane provjere | Status |
| --- | --- | --- | --- | --- | --- | --- |
| P1 | `ex-u14-reynoldsov-broj-u-dva-sustava-iste-geometrije`; dva Re i prijelaz | ZADRŽATI račun; popraviti prikaz jednoga fluida i prianjanja uz stijenke | T1 | isti | SVG, verifier | provedeno |
| P2 | `ex-u14-froudeova-slicnost-model-broda-u-vucnom-bazenu`; Fr i nesklad Re | ZADRŽATI; isti oblik trupa, stvarne kote, izričito odvojena mjerila crteža | T2 | isti | SVG, verifier | provedeno |
| P3 | `ex-u14-kavitacija-u-venturijevom-suzenju-t2`; kontrola valjanosti Bernoullija | ZADRŽATI; jedan otvoreni fluid, brzina na pravom presjeku i izračunata krivulja tlaka | T2 | isti | SVG, geometrija, verifier | provedeno |
| P4 | `ex-u14-weberov-i-bondov-broj-raspad-kapi-u`; We/Bo i granica modela | ZADRŽATI; početni promjer i sučelje bez izmišljenih sila ili raspodjele kapljica | T2 | isti | SVG, verifier | provedeno |
| P5 | `ex-u14-buckinghamova-analiza-otpora-kugle-i-krivulja-cd`; Pi i otpor | ZADRŽATI; razdvojiti zadanu radnu točku i ilustrativnu korelaciju, ispravne logaritamske osi | T3 | isti | SVG, notebook, verifier | provedeno |
| P6 | `ex-u14-machov-i-strouhalov-broj-stlacivost-i-vrtlozno`; Ma i rezonantna frekvencija | ZADRŽATI; otvoreni vod i tlocrt kružnog cilindra s naizmjeničnim vrtlozima | T2 | isti | SVG, verifier | provedeno |
| Z1 | `task-u14-krv-tece-arteriolom-promjera-brzinom-a-voda`; dva Re | ZADRŽATI; razjasniti efektivnu viskoznost i SI pretvorbe | T1 | isti | izvor, SVG Z1, golden | provedeno |
| Z2 | `task-u14-zrak-struji-vodom-promjera-lokalnim-volumenskim-protokom`; Q → Ma | ZADRŽATI; izričito lokalni volumenski protok i unutarnji promjer | T1 | isti | izvor, SVG Z2, golden | provedeno |
| Z3 | `task-u14-na-referentnom-presjeku-usisa-crpke-apsolutni-tlak`; kavitacijska rezerva | PREPRAVITI; pretlak → apsolutni tlak, dva režima i potreban granični pretlak | T2 | isti | izvor, SVG Z3, golden/invarijante | provedeno |
| Z4 | `task-u14-kap-goriva-promjera-izlozena-je-relativnoj-struji`; ponavljanje P4 | ZAMIJENITI; Reynoldsova sličnost u različitim fluidima, površina bc i prijenos sile uz provjeru Ma | T2 | `task-reynoldsova-slicnost-hidroprofila` | izvor, SVG Z4, notebook, verifier | provedeno |
| Z5 | `task-u14-frekvencija-otpustanja-vrtloga-iza-geometrijski-slicnog-tijela`; samostalni Buckingham | ZADRŽATI; račun ranga i eksponenata, dopustiti ekvivalentne Re/1/Re grupe | T3 | isti | izvor, SVG Z5, stvarna dimenzijska provjera | provedeno |
| Z6 | `task-u14-preljev-brane-ispituje-se-vodenim-modelom-u`; Fr skaliranje | PREPRAVITI; dva mjerila, prijenos zajamčenih intervala, ograničenja laboratorija i uvjetan zaključak | T4 | isti | izvor, SVG Z6, notebook, verifier | provedeno |

## Provenijencija i granice

`rewrite_status`: complete; `rewrite_level`: selective, Z4 substantial;
`sketch_requirement`: svih šest mjesta mora odgovarati tekstu; skice
razlikuju referentni presjek, tetivu/raspon i odvojena mjerila.

Z4 je autorska konstrukcija: nova scena, geometrija, podatci, traženo i
strategija. Z6 koristi izričito sintetička očitanja i zajamčene intervale,
bez tvrdnje da predstavljaju stvarni pokus ili standardne nesigurnosti.
Stari Z4 URL ostaje kao jednokratni span ispred novog naslova. D06 i
manifest obnavljaju se generatorima; D03 i povezani notebook usklađuju se.

Za provjeru pretpostavki sličnosti korišten je primarni izvor
[NASA Glenn — Similarity Parameters](https://www1.grc.nasa.gov/beginners-guide-to-aeronautics/similarity-parameters/).
Za granice Froudeova prijenosa relevantan je
[ITTC Resistance Committee](https://ittc.info/media/5516/03.pdf).
Ti izvori podupiru fizikalni model, nisu donori novih zadataka.

Riješeni računi ne preoblikuju se didaktički. Ispravljaju se fizikalne
poruke skica i njihovi opisi. Dimenzijska matrica i shema odabira grupa
pregledavaju se; kvalitetne figure ne treba precrtavati.

## Rezultati provjera

Dovršeno 22. rujna 2026. Z1, Z2 i Z5 zadržani su uz preciznije oznake,
naputke i rezultate; Z3 i Z6 nadograđeni su stvarnim odlukama, a Z4 je nova
fizikalna cjelina. Svih šest razina ostaje T1/T1/T2/T2/T3/T4.

Od 11 pregledanih slika izmijenjeno je devet; Buckinghamova matrica i
shema odabira grupa zadržane su. Zajednička skica ima šest aktualnih
panela. Provjereni su omjer promjera Venturija 3:1, kota u grlu, stvarna
krivulja tlaka, logaritamska krivulja Cᴅ i odvojeni zadani podatak P5.
Trupovi i hidroprofili geometrijski su slični, a dva modelska presjeka
zadovoljavaju kontinuitet i omjer duljina 1,5.

Riješeni računi ostaju isti. Dugi komentari uz We u P4 i Ma u P6 premješteni
su iz jednadžbi u prozu jer su u PDF-u preklapali brojeve jednadžbi. Svi
njihovi ID-jevi sačuvani su. D03, D06, manifest i notebook usklađeni su.
Matematički izrazi u generiranim sažecima i odgovorima U11 nisu odrezani;
stari Z4 URL sačuvan je jednokratnim sidrom uz novi naslov.

Izvršene provjere:

- `verify_all.py`: 1242 rezultata = 1054 usporedbe s neovisnim ciljem i
  188 invarijanti, uz 22 dodatna fizikalna golden testa. Svih 90/90
  zadataka ima ugovor; nema self-comparison provjera, tautologija ni rupa.
  U11 provjerava `verify_u14.py`: 71 rezultat bez pada.
- `check_u11_sketch_geometry.py`: PASS za devet izmijenjenih SVG-ova.
  Čita stvarne putanje i kote, provjerava otvorene vodove i tlačni
  priključak, profil ulja s prianjanjem, geometrijsku sličnost, vrtnju
  vrtloga, kontinuitet modelskih presjeka te izračunate grafove.
  Za krivulju tlaka dopušta 0,03 Pa odstupanja zbog zapisa koordinata.
- `audit_publication.py` i `audit_typst.py`: PASS; 87 primjera, 90 vježbi,
  postojeća poglavlja i razine ostaju očuvani.
- Povezani notebook izvršen je u čistom kernelu: PASS (5,28 s).
  Dodani su odvojeni podatak P5, prijenos hidroprofila Z4 i Z6 s grafom
  zajamčenih intervala i pitanjima za tumačenje. Izvori nemaju spremljene
  izlaze. JupyterLite je ponovno izgrađen; audit potvrđuje 17 notebookova,
  četiri ekstenzije i Pyodide. Hash lokalno poslužene kopije notebooka
  jednak je izvorniku.
- HTML render svih 24 stranice i završno osvježavanje U11/D06: PASS.
  Audit stranice: 216 slika, 1926 lokalnih veza, 442 sklopiva bloka.
- Edge na 320/768/1440 px: šest zadataka i točne razine, svi aktualni
  ID-jevi i stari Z4 alias, bez dvostrukih ID-jeva ili vodoravnog
  prelijevanja. Svih 12 naputaka/odgovora upravljivo je tipkovnicom.
  Automatizirani WCAG A/AA audit prolazi; D06 ima šest valjanih povratnih
  veza. Granice SVG teksta provjerene su nakon svih transformacija.
- Nativni PDF ponovno je izgrađen nakon HTML-a: 313 A4 stranica,
  `audit_pdf.py` PASS. Vizualno pregledani: uvod (193), mjerila sila (194),
  P1–P6 (201, 202, 203, 205, 206, 208), vježbe i skice (209–210), D06
  (306–307). Stranice 205 i 208 ponovno su pregledane nakon ispravka
  preklapanja komentara i brojeva jednadžbi. Kopija za preuzimanje
  jednaka je konačnom PDF-u iz `_book`.
- `git diff --check`: PASS. Postojeće razlike završetaka redaka u šest
  omotača nisu sadržajno mijenjane.

Prethodni U09/U10 commit `f12187b` poslan je na `origin/main` prije ove
revizije. Njegov [GitHub Actions run](https://github.com/martibasic/MF1_udzbenik/actions/runs/35761400388)
završio je uspješno, uključujući objavu. Po završetku revizije izmjene U11 ostale su lokalne,
u skladu sa slijedom zahtjeva: prvo commit/push postojećeg rada, zatim
uređivanje sljedećeg poglavlja.

Pri lokalnoj reviziji U11 nije ponovno pokrenut cijeli objavni skup od 17 izvršenja
notebookova i 72 viewport slučaja; taj je skup prošao za prethodni
commit. Sada su izvršeni promijenjeni notebook, JupyterLite build,
audit svih HTML stranica i ciljani pregled U11. Preostale Typst poruke
odnose se na postojeće zastarjelo ime `times.circle` u neizmijenjenim
jednadžbama; render završava uspješno.

Računske i geometrijske provjere potkrepljuju navedene modele. Didaktička
procjena raznolikosti ostaje autorska procjena, uz izričito navedene
granice sličnosti i sintetičko podrijetlo podataka u Z4/Z6.

## Dopuna prije objave (22. rujna 2026.)

Na naknadni korisnikov zahtjev za commit/push izvršeni su svi objavni
notebookovi: 17/17 PASS (56,54 s). Ponovno prolaze brojčane provjere
(1054 ciljne usporedbe, 188 invarijanti i 22 fizikalna golden testa),
geometrija U11, struktura publikacije, Typst, QR, CFD V&V, generirani
ključ, JupyterLite i audit svih 24 HTML stranica. Nativni PDF ima 313
A4 stranica i prolazi audit; kopija za preuzimanje identična je PDF-u
iz `_book`. Provjera pripremljenog diff-a ne nalazi pogreške.

Završni viewport/WCAG audit prolazi za svih 72 prikaza na 320/768/1440 px
i A4 ispis. JupyterLite u stvarnom pregledniku pokreće Python (Pyodide)
i doseže stanje Idle. Time je dopunjena objavna provjera koja nije bila
izvršena u prethodnom koraku lokalne revizije.
