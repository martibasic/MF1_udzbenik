# Provedba ispravaka G4: pog. 14, pog. 15, pog. 0 i dodatci A–E

Provedeno 8. 11. 2026. prema `PROVJERA.md` u ovoj mapi, uz odobrenje autorice.
Provedene su samo stavke sa statusom POTVRĐENO, težinom P2 (ili P3 sniženom iz
P2) i vrstom TEKST. Kod mješovitih stavki proveden je samo tekstni dio koji ne
mijenja broj, rezultat ni oznaku koju koriste ključ ili verifikator.

Mijenjani su samo `source/u14_turbostrojevi_i_propulzija.md`,
`source/u15_otvoreni_tokovi.md`, `source/u00_kako_koristiti_udzbenik.md` i
`source/d01`–`d04`. Datoteka `d05` nije mijenjana. `references.bib`, `d06`, alati, skice i
bilježnice nisu dirani. Generatori nisu pokretani s `--write` i nije napravljen
commit. Završetci redaka su sačuvani: CRLF u u00, d01, d02 i d04, a LF u u14,
u15 i d03, kao prije izmjena.

Kratice mjesta jednake su onima u `PROVJERA.md`. Brojevi redaka odnose se na stanje prije izmjena.

## Tablica provedbe

| ID | Mjesto | Status | Napomena |
|---|---|---|---|
| G4-01 | u14 Z1/Z2 | NEPRIMJENJIVO | Pog. 14 Z1 već je zamijenjen zadatkom „Isti potisak, dva promjera propelera”. Stavka je P1 i autorska odluka, pa ne pripada ovom zahvatu. |
| G4-02 | u15:481 | NEPRIMJENJIVO | Obrazloženje pada $C_d$ već je ispravljeno izvan ovog zahvata. |
| G4-03 | u15:586 | NEPRIMJENJIVO | Definicija $y_{2,dop}$ već je unesena izvan ovog zahvata. Napomena uz skicu (u15:421) i dalje kaže „samo podatak” i nije dirana jer pripada SKICI. |
| G4-04 | u15:177, 183 | PROVEDENO | Raspon $C_d$ i vrijednost $C_{pr}$ označeni su kao nastavna procjena, uz rečenicu da $C_d$ opada s porastom $a/y_0$. Izvor nije dodan jer traži `references.bib`. |
| G4-05 | u14:584 | PROVEDENO (djelomično) | $\eta_0\approx0{,}55$–$0{,}70$ označen je kao orijentacijska nastavna procjena. Izvori za turbostrojeve i propelere u dodatku E su PRESKOČENI (`references.bib`). |
| G4-06 | u14:478, 496, 532 | PROVEDENO | Dodana je definicija meridijanske (ovdje radijalne) komponente i faktora klizanja; 0,82 je označen kao nastavna pretpostavka. |
| G4-07 | u14:379–380, 440 | PROVEDENO | Stavka 4 sada se odnosi na jednu lopaticu koja se udaljava od sapnice, a stavka 5 izrijekom traži usporedbu s $P_G$. Razina T4 ostaje autorska odluka. |
| G4-08 | u14:462 | PROVEDENO | Izostavljena je posljednja rečenica r. 462. Vrijednost 10,49 kW ostaje u r. 443 i 446, a 0,497 u r. 466. |
| G4-09 | sl. 14.5 | PRESKOČENO | Vrsta je SKICA. |
| G4-10 | u14:5, 207 | PROVEDENO | Disk se sada pripisuje samo propeleru. Za vodomlazni pogon izrijekom stoji $v_A=v_s$ u uvodu i u provjeri. |
| G4-11 | u14:193 | PROVEDENO (djelomično) | Uvodna rečenica sada upućuje na izvod u pog. 10 (`eq-aktuatorski-disk-potisak`). Jednadžba `eq-idealna-ucinkovitost-propelera` zadržana je jer je koriste P6 i Z5, a uklanjanje istaknute jednadžbe bilo bi strukturna izmjena. |
| G4-12 | u14:584 | PROVEDENO | Pravilo „bira se najveći propeler” zamijenjeno je zaključkom unutar modela i navedena su stvarna ograničenja: gaz, brzina vrtnje, zračnost i uron vrha. |
| G4-13 | u14:99 | PROVEDENO | Dodano je: „$c_t$ i moment pozitivni su u smjeru vrtnje rotora”, uz os vrtnje. |
| G4-14 | u14:584 | PROVEDENO | Uz $\tfrac12\dot m(v_j-v_A)^2$ dodano je „u okviru mirne vode”. |
| G4-15 | u14 Z2, u15 Z2 | PROVEDENO | Dodan je `data-key-full="true"`, a tekst odgovora nije mijenjan. U u14 i u15 samo ta dva odgovora prelaze 500 znakova (601 i 620). D06 treba obnoviti generatorom. |
| G4-16 | u15 Z4 | PRESKOČENO | Promjena $y_1\to y_0$ zahvaća oznaku u ključu, skici i verifikatoru. |
| G4-17 | d04:7–10 | PROVEDENO | Uz svaku poveznicu u tablici dodano je „(pog. N)”. |
| G4-18 | d04:183 | PRESKOČENO | Traži unos u `references.bib`, koji je izvan dopuštenog opsega. Izdanja treba provjeriti. |
| G4-19 | pog. 15 | PRESKOČENO | Autorska odluka. |
| G4-20 | u14 Z6 | PRESKOČENO | Autorska odluka; stavka je i BROJ/MODEL. |
| G4-21 | pog. 14 | PRESKOČENO | Stavka je ODBAČENA, P3 i autorska odluka. |
| G4-22 | d04, CFD odlomci | PRESKOČENO | Autorska odluka, P3. |
| G4-23 | u14:17 | PROVEDENO (djelomično) | Izostavljena je rečenica „Oznake slijede turbostrojarski standard …”, koja doslovno ponavlja r. 3. Formule u uvodu ostaju prema autorskoj odluci od 15. 10. 2026. |
| G4-24 | u14:3, 79, 85–88 | PRESKOČENO | Prijedlog briše cijeli okvir `:::` (strukturna izmjena), a ponavljanja su parafraze, ne doslovne rečenice. |
| G4-25 | u14:76 | PRESKOČENO | Stavka je P3, a prijedlog izrijekom kaže „samo ako autorica želi”. |
| G4-26 | u14:290, 587 | PROVEDENO | „u sljedećem primjeru” i „Posljednji primjer” zamijenjeni su upućivanjima `[-@ex-…]`. |
| G4-27 | u14:17 | PROVEDENO | Rečenica od 47 riječi podijeljena je na tri, prema prijedlogu urednika. |
| G4-28 | u14:127 | PROVEDENO | Rečenica je podijeljena na dvije, a nijekanje „a ne za jednu lopaticu” je sačuvano. |
| G4-29 | u14:136, 594; u15:56 | PROVEDENO | MRF je uveden punim nazivom uz „engl.”. Dodan je „engl.” uz *figure of merit* i *squat*. |
| G4-30 | u14, u10, d02 | PRESKOČENO | Autorska odluka o nazivlju. |
| G4-31 | u14:240, 308, 382 | PROVEDENO (djelomično) | Potpisi su sada opisne rečenice. `fig-alt` nije preoblikovan jer je riječ o atributu, koji ovaj zahvat ne mijenja. |
| G4-32 | u14:448 | PROVEDENO | Iz naslova koraka uklonjen je broj „5.”. Naslov i njegove klase zadržani su, a nije pretvoren u podebljani uvod. |
| G4-33 | u14:148 | PRESKOČENO | Stavka je ODBAČENA kao P2. |
| G4-34 | u14:698 | PROVEDENO | „crta student” zamijenjeno je s „nacrtaj sam”. |
| G4-35 | u14:218, u15:230 | PRESKOČENO | Pitanje kao uvod CFD odlomka obrazac je knjige. |
| G4-36 | u15:7 | PROVEDENO (djelomično) | Izostavljena je rečenica o empirijskim koeficijentima, koja gotovo doslovno ponavlja r. 183. Formule u r. 3 ostaju prema autorskoj odluci. |
| G4-37 | u15:15 | PROVEDENO | Novi naslov je „Slobodna površina kao granica toka”, a ID `sec-otvoreni-tok-motivacija` je zadržan. |
| G4-38 | u15:244 | PROVEDENO | Valjak je definiran pri prvoj uporabi. |
| G4-39 | u15:328, 564 | PROVEDENO (djelomično) | VOF i GUM uvedeni su punim nazivom uz „engl.”. Naputak Z5 ostaje unutar 500 znakova ključa (481). Unos GUM-a u dodatak E je PRESKOČEN (`references.bib`). |
| G4-40 | u15:165 | PROVEDENO | Upućivanje sada glasi `(odjeljak [-@sec-kontrolne-gradevine])`. |
| G4-41 | u15:90 | PROVEDENO | „obje informacije” zamijenjeno je s „oba rubna podatka”. |
| G4-42 | u15:232 | PROVEDENO | Rečenica sada imenuje objekt usporedbe, a nijekanje je sačuvano. |
| G4-43 | u00:7 | PROVEDENO | CFD je uveden punim nazivom uz „engl.”. |
| G4-44 | u00:71 | PROVEDENO | Naslov je ispravljen u „Dodatci”. Dosadašnji automatski ID `dodaci-za-brzo-snalaženje` zadržan je izričitim atributom. |
| G4-45 | u00:38 | PROVEDENO | „poglavlje 3, Z2” zamijenjeno je s „pog. 3, Z2”. |
| G4-46 | d01:50–192 | PROVEDENO | Deset naslova sada počinje s „Pog.”. Naslovi su u izvoru, ne u generiranoj datoteci, a automatski ID-jevi se ne mijenjaju jer ih Pandoc piše malim slovima. |
| G4-47 | d02:20, 80, 105, 112 | PROVEDENO | Pojmovnik sada daje pune nazive uz „engl.” za CFD, MRF, RANS, SST, SIMPLE i PISO. Novih tvrdnji nema. |
| G4-48 | d04:154 | PROVEDENO | Naslov sada glasi „Pripremljeni paketi za verifikaciju i validaciju (V&V)”, a ID je zadržan. LES/DNS je izvorni P3, pa je PRESKOČEN. |
| G4-49 | d04:156, 167, 173 | PROVEDENO | Validator, putanja `data/cfd/` i `teaching_comparison.json` zamijenjeni su opisom onoga što student radi. Poveznica na repozitorij je zadržana. |
| G4-50 | `references.bib` | PRESKOČENO | Traži provjeru izdanja i unos u `references.bib`. |
| G4-51 | d03:325 | PROVEDENO | $\dot mv_A$ zamijenjen je s $\dot mv_s$. |
| G4-52 | d03:280 | PROVEDENO | Natuknica je razdvojena u dvije, obje s oznakom (Z2). |

Zbroj: 36 PROVEDENO (od toga 7 djelomično), 13 PRESKOČENO, 3 NEPRIMJENJIVO.

## Ispis `--usporedi HEAD` (sažetak)

Naredba: `PYTHONUTF8=1 python tools/prirucnik_stats.py --usporedi HEAD` nad svih
sedam promijenjenih izvora.

| Izvor | Izgubljeni brojevi | Dodani brojevi | Ocjena |
|---|---|---|---|
| u14 | 10,49; 5; 50 | — | Sve je namjerno. 10,49 pripada rečenici uklonjenoj prema G4-08 i ostaje u r. 443 i 446. „5” je broj koraka uklonjen prema G4-32. „50” dolazi iz $u/c_1\approx0{,}50$ (G4-08), a 0,497 ostaje u r. 466. |
| u15 | — | — | Uklonjena je jedna rečenica s „samo” (G4-36). Ista ograda ostaje u r. 183 i u Sažetku, a za Manningov $n$ u r. 339. |
| u00, d01, d02 | — | — | Nema promijenjenih rečenica s brojem, nijekanjem ili ogradom. |
| d03 | — | — | Nijekanje „bez” prešlo je u novu natuknicu (G4-52). |
| d04 | — | 1, 4, 5, 6, 7, 8, 9, 9, 11, 12, 13, 14, 15, 15 | To su brojevi poglavlja dodani prema G4-17. |

Ostale prijave alata:

- u14 „Provjera”: nijekanje „ne” prijavljeno je kao izgubljeno, ali ostaje u
  drugoj rečenici („a ne za jednu lopaticu”).
- u14 „Provjera” i η₀: „samo” je dodan namjerno, kao ograda.
- u14: alat bilježi izgubljen citat `ex-peltonova-lopatica-u-gibanju`. Uzrok je
  promjena `@ex-…` u `[-@ex-…]`, koju alat ne broji; upućivanje i dalje postoji.
- u14: nova rečenica s jakom tvrdnjom je definicija meridijanske komponente (G4-06).

`--nalazi` nad istim izvorima prijavljuje samo u14:136 (K3, 44 riječi,
„Provjera je obvezna u oba slučaja …”). Taj nalaz postoji od prije i nije stavka P2 u `PROVJERA.md`.
Nalazi u14:17 (K3) i u14:290 (K12) su uklonjeni.

## Izvršene provjere i ograničenja

- Duljine odgovora i naputaka u ključu provjerene su funkcijom
  `tasks_from_source` iz `scripts/generate_exercise_key.py`. Tu je funkciju
  uvezla privremena skripta, a ključ nije zapisan. Nakon izmjena se ni jedan
  odgovor ni naputak u u14 i u15 ne skraćuje.
- `tools/audit_architecture.py` javlja samo zastarjeli D06. Treba ga obnoviti s
  `python scripts/build_book.py --write`. Isti postupak obnavlja i
  `assets/content-index.json`, u kojem su zastarjeli promijenjeni naslovi i potpisi.
- Render, verifikatori i puni objavni CI nisu pokretani.
- Ocjena da preoblikovani tekst čuva značenje autorska je procjena agenta
  koji je proveo izmjene. Didaktička kvaliteta time nije dokazana.
