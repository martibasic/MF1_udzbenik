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
paletu, šrafure i fontove; ne zamjenjivati stil sveučilišnog priručnika.

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

## Revizija 12. 10. 2026.

Provedba nalaza stručne recenzije (recenzent mehanike fluida i brodske
hidrostatike), odobrene od autorice. Opseg: tekst teorije, skice Z1/Z2,
verifikator `verify_u05_integrated` i checker geometrije. Razine Z ostaju
T1, T1, T2, T2, T3, T4; broj primjera ostaje 6 (zamjene 1:1, bez dodavanja).

| Nalaz recenzije | Provedeno | Mjesto |
| --- | --- | --- |
| Brodograđevni lajtmotiv (brodski otvor) nije realiziran; Z1 klon P1 | Z1 zamijenjen vodonepropusnim vratima naplavljenog odjeljka (morska voda 1025 kg/m³, šarke i dva zasuna; sila, h_CP, moment oko osi šarki, sile zasuna) | `task-vodonepropusna-vrata-naplavljenog-odjeljka`, T1 |
| Pet četvrtcilindričnih ploha; Z2 klon P4; tekst tvrdi da rezultanta kroz O ne vrijedi općenito, a nikad to ne pokazuje | Z2 zamijenjen paraboličnim pokrovom suhog kanala (voda iznad pokrova, F_x, F_z, pravci, F_R, moment oko A; normale nemaju zajedničku točku) | `task-parabolicni-pokrov-suhog-kanala`, T1 |
| $\|F_V\|=\rho gV^*$ naveden, ne izveden | Dopisana bilanca sila na stupac fluida (težina, tlak na zatvarajućoj plohi, bočni tlakovi, reakcija plohe) | izvod „Vertikalna komponenta iz bilance stupca fluida” |
| Pog. 5 bez `.mf1-izvod`, `.mf1-fizikalno-znacenje`, `.mf1-granica-modela` | Pet izvoda omotano s pitanjem i provjerom; dodano „Fizikalno značenje” uz centar tlaka i „Granica modela” za zakrivljene plohe | odjeljci ravne i zakrivljene plohe |
| P4: referentna vertikala za $x_V$; P6: $M_A=F_V R$ | Navedeno „od vertikale kroz O”; u provjerama P4 i P6 iskorišteno da rezultanta kružnog luka prolazi kroz O (skica P4 već ima kotu $x_V$ od vertikale kroz O, bez izmjene) | P4, P6 |
| CFD okvir ustave nije vezan uz konkretan P/Z | Vezan uz Z3 i P3; navedeni ulazi, izlazi, provjera i odluka | `#cfd-ustava-opterecenje` (ID zadržan) |
| Dvostruko „Zastani i promisli” | Četvrto pitanje samoprovjere zamijenjeno pitanjem o $\sin^2\theta$ naspram $\sin\theta$ | „Provjeri sebe” |
| Notacija i nazivlje | $s\to y$ (koordinata duž plohe, $y_{CP}$), $p_0\to p_{pl}$, „hidrostatički” u tekstu, gramatika r. 343; P1 označen T1 | cijelo poglavlje |

Matrica zamjena (staro → novo):

| Mjesto | Stari ID (ostaje kao `<span>` alias) | Novi ID | Razina | Kontrolni rezultat |
| --- | --- | --- | --- | --- |
| Z1 | `task-u05-ravna-pravokutna-zaklopka` | `task-vodonepropusna-vrata-naplavljenog-odjeljka` | T1 | $F_x=+28{,}31$ kN; $h_{CP}=2{,}297$ m; $M_{\text{šarke}}=11{,}33$ kN m; zasuni 14,16 kN (donji 7,94, gornji 6,22 kN) |
| Z2 | `task-u05-zakrivljeni-poklopac-cetvrtine-kruga` | `task-parabolicni-pokrov-suhog-kanala` | T1 | $F_x=-5{,}948$ kN na 0,600 m; $F_z=-5{,}287$ kN na 0,900 m; $F_R=7{,}958$ kN; $M_A=-8{,}327$ kN m |

Provjere: `verify_u05_integrated.py` 100/100 (Z1: integral tlaka, ravnoteža
zasuna, utjecaj gustoće; Z2: izravna integracija $p\,\mathbf n\,dA$ po paraboli,
predznaci, nepostojanje zajedničke točke normala, skaliranje s $H$; P4: moment
oko O). `check_u05_sketch_geometry.py` PASS: Z1 omjeri vrata, položaj oznake
sile u centru tlaka, zasuni i šarke; Z2 kvadratna Bézierova krivulja kao točna
parabola (kontrolna točka na sjecištu tangenata), pravci $F_H$/$F_V$ i lokalna
normala. Skica `u05_vjezbe_skice.svg`: paneli Z1 i Z2 nacrtani unutar postojećih
okvira; `<desc>` ažuriran. Notebookovi nisu mijenjani (ne opisuju Z1/Z2).
D06 i manifest obnavlja koordinator generatorima; `print-layouts.json` (sha skice)
također. Didaktička procjena ostaje autorska, ne dokaz CI-ja.

## Revizija 19. 10. 2026. — didaktičko pojačanje (odobreno u razgovoru)

Zahtjev autorice: zadatci su prelagani, a u poglavlju nema samostalnog zadatka s
nagnutom plohom iako studenti miješaju težište plohe i centar tlaka. Zahvat
unutar šest mjesta i raspodjele T1, T1, T2, T2, T3, T4; broj primjera ostaje 6.

| Mjesto | Staro | Novo | Razina | Didaktička korist |
| --- | --- | --- | --- | --- |
| Z3 | Pregrada između dviju razina vode (`task-pregrada-izmedu-dviju-razina-vode`, ostaje kao alias `<span>`) | Samootvarajuća kosa zaklopka kanala (`task-samootvarajuca-kosa-zaklopka`) | T2 | Uvjet otvaranja je položaj centra tlaka u osi, ne težišta; student mora odlučiti je li ploča pri otvaranju djelomično ili potpuno uronjena (pravilo trećine daje 3a > L), riješiti uvjet po h_C i zatim postaviti moment oko osi s krakom uzduž ploče. Treći zahtjev izričito traži obrazloženje zašto težište daje pogrešan zaključak. |
| P5 | Četvrtcilindrični poklopac uz slobodnu površinu (ponavljao geometriju P6) | Isti poklopac u zatvorenom spremniku s nadtlakom plina 20 kPa | T3 | Jedini primjer u knjizi koji provodi upozorenje iz odjeljka o referentnom tlaku: jednoliki član mijenja silu i pomiče hvatišta prema težištima projekcija; rezultanta i dalje prolazi kroz O. |

Kontrolni rezultati Z3: $y_{otv}=2{,}309$ m ($h_C=1{,}443$ m, gornji rub 0,577 m
ispod površine); pri 1,80 m $F=27{,}43$ kN, hvatište 0,691 m od donjeg ruba,
$M=2{,}99$ kN m, sila praga 3,74 kN. P5: $F_H=26{,}36$ kN na 0,477 m,
$F_V=-29{,}07$ kN na 0,432 m, $F_R=39{,}24$ kN, $-47{,}8^\circ$.

Povezane izmjene: CFD okvir ustave sada upućuje na nagnutu ustavu i moment oko
osi (Z3); D03 (pogreške Z3 i nadtlak); skica Z3 u `u05_vjezbe_skice.svg`
(nacrtano unutar postojećeg okvira, panel proširen na 390 px) i skica P5
(poklopac spremnika, plin, pomaknuta hvatišta); `print-layouts.json` hash;
`verify_u05_integrated.py` (Z3: integracija tlaka, promjena predznaka momenta
upravo pri $y_{otv}$, bilanca praga, granični slučaj niže osi; P5: izravna
integracija $p\,\vec n\,dA$ s nadtlakom, prolaz kroz O, pomak hvatišta);
`check_u05_sketch_geometry.py` (kut 60°, os na 0,40 L, prag, nenacrtana
nepoznanica; P5 poklopac i oznaka nadtlaka). Prošlo: verify_all, audit_publication,
qa_audit, audit_sketch_design, audit_print_layouts; D06 i manifest regenerirani.
Didaktička procjena je autorska; studentski pilot nije proveden.
