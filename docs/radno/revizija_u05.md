# Revizija U05 — 22. rujna 2026.

## Odluke prije provedbe

Polazište: `16ab5e4`. Uređuju se samostalni zadatci i skice poglavlja;
teorija i šest riješenih primjera služe usporedbi. Ostaje šest mjesta
T1, T1, T2, T2, T3, T4. Postojeće lokalne promjene omotača U02/U03/U11
čuvaju se. Kanonski provjeravatelj je `verify_u05_integrated`, ne `verify_u05`.

| Primjeri | Princip i postupak | Usporedba sa zadatcima |
| --- | --- | --- |
| P1 | Pravokutna ploha, sila iz dubine težišta, drugi moment površine | Z1 je potrebna osnovna samostalna vježba T1 |
| P2 | Kosa ploha, normalna sila i moment oko gornjeg zgloba | Stari Z3 ponavlja iste korake i odluke |
| P3 | Dva sloja, zbroj triju tlačnih dijagrama i njihovih momenata | Stari Z4 ponavlja račun sile i hvatišta |
| P4/P5 | Projekcija i pomoćni volumen, suprotne okupane strane | Z2 čuva osnovni rastav i određivanje predznaka |
| P6 | Dvije komponente i zbroj momenata oko krajnje točke luka | Stari Z5 opet traži iste korake uz drugi predznak i dubinu |

| Mjesto | Odluka i nova aktivnost | Razina | Provenijencija |
| --- | --- | --- | --- |
| Z1 | Zadržati osnovni račun; dodati čitljivu skicu | T1 | `rewrite_status=nije_potrebno` |
| Z2 | Zadržati; jasno prikazati stvarnu vodu, luk i pozitivne smjerove | T1 | `rewrite_status=nije_potrebno` |
| Z3 | Zamijeniti neto silom i momentom na pregradi između dviju razina vode | T2 | Autorska nastavna konstrukcija, P3 |
| Z4 | Zamijeniti najvećom dopuštenom širinom trokutastog poklopca i provjerom ponuđene širine | T2 | Autorska nastavna konstrukcija, P3 |
| Z5 | Zamijeniti radijalnim poklopcem s osi u središtu kružnice; prepoznati nulti moment tlaka i uključiti težinu | T3 | Autorska nastavna konstrukcija, P3 |
| Z6 | Zadržati propagaciju standardne nesigurnosti i ograničeno tumačenje podudarnosti | T4 | `rewrite_status=nije_potrebno` |

Za Z3–Z5 vrijedi `rewrite_status=preradeno`, `rewrite_level=P3`: promijenjeni
su geometrija/oslanjanje, scenarij, zadani i traženi podatci (najmanje 3/5).
Z3 povezuje dva opterećenja suprotnih smjerova; Z4 obrće problem na geometrijski
parametar; Z5 traži izbor momentne točke, lokalnu normalu i statiku cijelog
sklopa. Z6 zadržava jedinu razinu T4. To je autorska procjena, ne studentski pilot.

Stari ID-jevi ostaju kao prazni HTML span aliasi:

| Stari ID | Novi ID |
| --- | --- |
| `task-u05-kosi-poklopac-sa-zglobom` | `task-pregrada-izmedu-dviju-razina-vode` |
| `task-u05-dvoslojna-vertikalna-stijena` | `task-sirina-trokutastog-poklopca` |
| `task-u05-zglobni-zakrivljeni-poklopac-model` | `task-radijalni-poklopac-s-tezinom` |

## Nalazi o skicama i plan

Pregledano svih sedam postojećih SVG-ova. Uvod ima neusklađeno težište i
kotiranje te prazninu između vode i inspekcijskog poklopca. P1 ima pogrešno
zaokruženu silu. P2 ima odgovarajući kut i normale. P3 treba odmaknuti kote
od ruba. P4/P5 imaju lukove koji ne odgovaraju četvrtini kruga iz računa i
pogrešno prikazanu okupanu stranu/pomoćni volumen. P6 ima neusklađen povratni
luk pomoćnog volumena i oslonac zgloba. Ispraviti geometriju uz isti raspored,
paletu, šrafure i fontove; ne zamjenjivati stil udžbenika.

U kanonski izvor uključiti dosad nepovezanu datoteku `u05_vjezbe_skice.svg`,
koja je prikazivala staru zbirku samo ravnih ploha. Prilagoditi je novim
zadatcima uz raspored 2×3 i stil prethodnih poglavlja: Z1/Z6 bočni presjek i sila
na panel, Z2/Z5 stvarni kružni luk i okupana strana, Z3 nepropusna pregrada
dvaju odvojenih spremnika, Z4 pogled okomito na trokutastu plohu. Sve sile
označuju djelovanje na kruti sklop. Skice nisu prikaz strujanja.

Provjere: neovisna integracija tlakova i momenata, granični slučajevi,
geometrija stvarnih SVG-ova, vizualni pregled, manifest, D06, HTML i PDF.
Notebookovi za ravnu/zakrivljenu plohu ostaju konceptualni primjeri;
provjeriti da ne opisuju zamijenjene zadatke. D03 uskladiti, D06 i manifest
obnoviti generatorima. Povezane skice s imenima `u06_*` pripadaju kanonskom U05.

## Provedeno i provjereno

- Zamijenjeni Z3–Z5; Z1, Z2 i Z6 sadržajno su identični polazištu. Teorija
  i tekstovi P1–P6 ostali su identični. Sačuvani su svi korisnički QMD omotači
  (provjera SHA-256), šest mjesta i njihove razine.
- Pregledano osam skica sada uključenih u U05. P2 je zadržan; u uvodu su
  ispravljeni C/CP, tlačne strelice i kontakt vode s poklopcem; u P1 zaokruživanje
  sile; u P3 rubne kote; u P4–P6 kružni lukovi, pomoćni volumeni, oslonci,
  lokalne normale i pravci sila. Zajednička skica vježbi sada opisuje svih šest
  aktualnih zadataka. Sile djeluju na poklopac/sklop, ne označuju strujanje.
- P4: xV se mjeri ulijevo od okomice kroz O; u P6 se momentni krak mjeri
  udesno od zgloba A. U P5 voda stvarno ispunjava četvrtinu valjka iznad luka.
  Pomoćni volumeni na suhoj strani P4/P6 imaju samo isprekidanu konturu.
- `verify_u05_integrated.py`: 84 uspješne provjere (69 golden, 15 invariant).
  U novim zadatcima uspoređuju se neovisni integrali i analitičke formule;
  provjereni su predznaci, jednakost/zamjena razina, promjena širine, granična
  dubina vrha trokuta, nulti moment tlaka, ravnoteža oslonaca, kapacitet
  spojnice, promjena dubine i granica bez težine.
- `check_u05_sketch_geometry.py` čita stvarne SVG putanje i strelice:
  provjerava polumjere, središta i smjer lukova P4/P5/P6/Z2/Z5, normale,
  položaj pravaca FH/FV i njihovo poništavanje momenata oko središta kružnice.
  To je zasebna lokalna provjera, nije dodana u workflow.
- `verify_all.py`: 1111 zapisa iz 19 modula (987 golden i 124 invariant),
  dodatna 22 fizikalna testa, 90/90 javnih ugovora, bez FAIL-ova ili rupa.
  Prošli su normalizator, generator ključa, generator manifesta,
  `audit_publication.py`, `audit_typst.py` i `git diff --check`.
- D03 je dopunjen. D06 i manifest obnovljeni su generatorima. Svi rezultati
  i kriteriji novih zadataka sačuvani su u ključu; sažetak Z5 više ne reže
  inline matematički izraz. Stari task ID-jevi ostaju funkcionalni aliasi.
- Notebookovi `u05_sila_na_ravnu_plohu.ipynb` i `u06_zakrivljena_ploha.ipynb`
  pregledani su i uspješno izvršeni u čistim kernelima bez promjene izvora.
  Prvi izričito definira kut od vertikale; drugi samostalno provjerava nulti
  moment kružnog luka. Nisu preslike zamijenjenih zadataka.
- Puni HTML i nativni PDF izgrađeni su lokalno. PDF audit potvrđuje 307 A4
  stranica i sadržaj; vizualno pregledane skice i stranice zadataka/ključa U05.
  HTML pregled na 320, 768 i 1440 px: šest zadataka, propisane razine,
  jedinstveni ID-jevi, tri stara aliasa, 12 tipkovnicom dostupnih sklopivih
  naputaka/odgovora, bez vodoravnog prelijevanja; šest D06 povratnih poveznica.
  Site audit: 24 stranice, 212 slika, 1918 poveznica i 434 sklopiva bloka.

## Ograničenja

Ovo nije neovisna stručna recenzija ni studentski pilot. SVG koordinate i
vizualni pregled pokrivaju različite vrste grešaka; prolaz numerike sam ne
dokazuje grafičku ni didaktičku kvalitetu. Na uskom zaslonu zajedničku skicu
treba povećati za čitanje sitnih oznaka, kao u prethodnim poglavljima.

Nije pokrenut novi JupyterLite build, svih 17 notebookova ni puni CI/WCAG
workflow; zadatak nije uključivao objavu. Lokalni Quarto je 1.9.32 (CI 1.9.37).
Postojeća upozorenja Typsta za `times.circle` u U10 ostaju izvan opsega.
Promjene nisu commitane niti poslane na GitHub.
