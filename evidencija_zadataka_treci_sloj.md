# Evidencija zadataka treci sloj

## Svrha dokumenta

Ovo je radna evidencija treceg sloja dodatnih izvora. Dokument je krenuo kao inventura tekstualno citljivih izvora, a sada uz `duplication_status` cuva i prve konzervativne `migration_status` potvrde ondje gdje je veza prema javnom `source/` poglavlju stvarno obranjiva.

## Trenutni status

- source_layer: `dodatni`
- trenutno inventirani tekstualno citljivi izvori: `4`
- trenutno inventirane zadatkovne jedinice: `291`
- default duplication_status za jos neprocijenjene stavke: `za_procjenu`
- polazni inventurni default migration_status za jos neprocijenjene javne veze: `nije_uneseno`
- trenutno zatvoreni duplication_status blokovi: `DA-1` do `DA-15`, `HS-1` do `HS-40`, `RM-1` do `RM-16`, `BJ-1` do `BJ-14`, `IS-1` do `IS-9`, `CV-1` do `CV-36`, `VG-01-01` do `VG-01-25`, `VG-02-01` do `VG-02-11`, `VG-02-21` do `VG-02-89`, `VG-05-01` do `VG-05-26`, `VG-07-01` do `VG-07-29`

Nakon zavrsnog closure-prolaza izostanak `migration_status` u ovom dokumentu vise ne znaci otvorenu migracijsku vezu, nego dokumentiranu varijantu, rezervni blok ili eksplicitni preklop bez zasebnog javnog `1:1` pandana.

## Prvi potvrdeni javni sync treceg sloja

Treci sloj se sinkronizira konzervativno, istim nacelom kao i prva dva sloja: `migration_status` se dopisuje samo ondje gdje postoji jasan izvorni ID, stvarni javni `WE` i dovoljno cvrst trag kroz pilot/val dokumente ili izravno `source/` poglavlje.

Nakon prvog chapter-by-chapter sync-prolaza, taj prag zasad sigurno prelaze:

1. `VG-02-46` -> javna prerada u `U04` kao WE `Procesna kada na automatskoj platformi`
2. `VG-02-50` -> javna prerada u `U04` kao WE `Zatvoreni servisni modul s kosom inspekcijskom stijenkom`
3. `HS-37` -> javna prerada u `U05` kao WE `Servisni spremnik s tri vodoravne ukrute`
4. `VG-02-38` -> javna prerada u `U06` kao WE `Sklopiva servisna brana s zakrivljenim rubom`
5. `HS-13` -> javna prerada u `U07` kao WE `Plutajuca servisna platforma s pomaknutim kompresorom`
6. `VG-02-71` -> javna prerada u `U07` kao WE `Kalibracijski modul na granici ulja i vode`
7. `VG-05-23` -> javna prerada u `U12` kao WE `Vodilica mlaza na ispitnom stolu`
8. `VG-05-26` -> javna prerada u `U12` kao WE `Ukljestena zakrivljena lopatica`
9. `VG-07-08` -> javna prerada u `U13` kao WE `Nezatvoreni servisni ispust na rashladnom cjevovodu`

Za ostale stavke treceg sloja konacno je zadrzana konzervativna urednicka presuda umjesto nasilnog zatvaranja `migration_status`. Posebno vrijedi:

1. `VG-05-10` ima stvarni pilot-trag prema `U11`, ali se zasad ne vodi kao nova task-level potvrda treceg sloja jer je isti javni `WE` vec konzervativno zakljucan kroz drugi sloj (`av05_04`).

## Rezultat dodatnog pregleda preostalih javnih tragova `U11-U13`

Nakon dodatnog citanja stvarnih javnih `WE`-ova i preostalih pilot-tragova, ovdje je zakljucena jedna nova task-level potvrda treceg sloja, dok drugi rubni slucaj ostaje samo dokumentirani preklop.

1. `U11`: `VG-05-10` ostaje samo dokumentirani preklop, ne nova potvrda, jer je javni `WE` `Kalibracijska mlaznica na prirubnici` vec konzervativno zakljucan kroz drugi sloj `av05_04`.
2. `U13`: otvaranjem novog javnog `WE` `Nezatvoreni servisni ispust na rashladnom cjevovodu` `VG-07-08` vise ne ostaje samo preporuceni pilot, nego prelazi prag za `migration_status: validirano`.

## Sazeta matrica treceg sloja po poglavljima

| Poglavlje | Glavni treceslojni ulazi u ledgeru | Trenutni javni sync | Operativna napomena |
| --- | --- | --- | --- |
| `U03` | `HS`, `Virag 2.1-2.11` | nema task-level potvrde | zakljucen kao tematski staticki rub bez javnog `1:1` treceslojnog primjera |
| `U04` | `RM`, `Virag 2.1-2.11`, rubno `Virag 2.21-2.89` | `VG-02-46`, `VG-02-50` | `U04` sada ima i otvoreni i zatvoreni rubni treceslojni primjer; ostali kandidati relativnog mirovanja ostaju otvorene varijante ili kompoziti |
| `U05` | `HS`, `OBJ-5`, `Virag 2.21-2.89` | `HS-37` | projektni primjer s ukrutama zatvara prvi cisti treceslojni sync, a ostatak je dokumentiran kao varijantni korpus |
| `U06` | `Virag 2.21-2.89` | `VG-02-38` | drugi kandidati zakrivljenih ploha i dalje nisu javno zatvoreni 1:1 |
| `U07` | `HS`, `Virag 2.21-2.89` | `HS-13`, `VG-02-71` | `U07` sada ima i stabilnosni primjer plivanja i cisti dvafluidni uzgon; ostali kandidati ostaju dokumentirane varijante |
| `U09` | `BJ` | nema task-level potvrde | treci sloj je ovdje zakljucen kao rezervni ili rubni bernoullijev blok bez zasebnog `1:1` synca |
| `U10` | `BJ`, `IS`, `CV` | nema task-level potvrde | postoji chapter-level vrijednost, ali je korpus zakljucen kao varijantan i kompozitan bez cistog javnog `1:1` synca |
| `U11` | `Virag 5.x` | nema nove treceslojne potvrde | `VG-05-10` ostaje dokumentirani preklop s vec zatvorenim `av05_04` iz drugog sloja |
| `U12` | `Virag 5.x` | `VG-05-23`, `VG-05-26` | ovo je zasad najcistije javno zatvoren treceslojni blok s dvije potvrde |
| `U13` | `IS`, `CV`, `Virag 7.x` | `VG-07-08` | novi servisni ispust daje prvi cisti treceslojni `U13` sync; ostali `Virag 7.x` kandidati ostaju dokumentirani bez dodatnog `1:1` prijenosa |

## Pravilo ove faze

1. Ovo je finalna urednicka presuda tekstualno citljivog treceg sloja za trenutni javni udzbenik: veze su ili `validirano` potvrdene ili eksplicitno zakljucene bez `1:1` migracije.
2. `preliminarni_cilj` je ovdje namjerno grub i vodi se po tematskom bloku izvora.
3. `Virag` tekstualni blokovi su zatvoreni; izvan ovog closure-prolaza ostaju samo answers-only ili source-gap reference koje se ne vode kao otvorene migracijske veze.

## Inventirani izvori

### private/materials/SAVAR_sesija1_dimanzija_hidrostatika.md

- status: `inventirano po headingima`
- broj jedinica: `55`

#### Blok `DA` - preliminarni_cilj: `REZERVNI`

- `DA-1` | naslov: `Brzina tonjenja tijela u fluidu` | duplication_status: `rezervni`
- `DA-2` | naslov: `Sila otpora gibanja tijela u viskoznom fluidu` | duplication_status: `rezervni`
- `DA-3` | naslov: `Rotacija cilindra i pretvorba energije u toplinu` | duplication_status: `rezervni`
- `DA-4` | naslov: `Brzina tonjenja kuglice (Stokesov zakon)` | duplication_status: `jedinstven`
- `DA-5` | naslov: `Domet topovskog zrna` | duplication_status: `rezervni`
- `DA-6` | naslov: `Tlak u laminarnom toku kroz cijev` | duplication_status: `jedinstven`
- `DA-7` | naslov: `Brinkmanov broj` | duplication_status: `rezervni`
- `DA-8` | naslov: `Promjer kapljice iz sprej sapnice` | duplication_status: `rezervni`
- `DA-9` | naslov: `Pogonska sila potpuno potopljenog torpeda` | duplication_status: `rezervni`
- `DA-10` | naslov: `Sila otpora ravne ploce u toku` | duplication_status: `rezervni`
- `DA-11` | naslov: `Brzina sirenja tlacnog poremecaja kroz arteriju` | duplication_status: `rezervni`
- `DA-12` | naslov: `Sila otpora gibanja tijela (ponovljeni tip, drugi skup)` | duplication_status: `bliski_duplikat`
- `DA-13` | naslov: `Promjer kapljice iz sprej sapnice (varijanta)` | duplication_status: `bliski_duplikat`
- `DA-14` | naslov: `Brzina talozenja kuglice` | duplication_status: `varijanta`
- `DA-15` | naslov: `Brzina broda i kutna brzina propelera (teorija slicnosti)` | duplication_status: `rezervni`

#### Blok `HS` - preliminarni_cilj: `REV-U03/U07`

- `HS-1` | naslov: `Masa utega potrebna za ravnotezu brane` | duplication_status: `varijanta`
- `HS-2` | naslov: `Pretlak unutar cilindricne posude od aluminija` | duplication_status: `jedinstven`
- `HS-3` | naslov: `Sila na valjkasti zatvarac` | duplication_status: `varijanta`
- `HS-4` | naslov: `Tlak u nepokretnoj prikljucnoj cijevi` | duplication_status: `rezervni`
- `HS-5` | naslov: `Pretlak za otvaranje sigurnosnog ventila` | duplication_status: `rezervni`
- `HS-6` | naslov: `Horizontalna sila na pregradu OA` | duplication_status: `varijanta`
- `HS-7` | naslov: `Maksimalna masa pontona` | duplication_status: `jedinstven`
- `HS-8` | naslov: `Masa valjka zglobno vezanog u tocci A` | duplication_status: `varijanta`
- `HS-9` | naslov: `Masa valjka ispunjenog vodom do jedne trecine` | duplication_status: `jedinstven`
- `HS-10` | naslov: `Promjer otvora da bi kuglica zaplivala` | duplication_status: `jedinstven`
- `HS-11` | naslov: `Promjer balona za nosenje tereta` | duplication_status: `varijanta`
- `HS-12` | naslov: `Masa poklopca oblika plasta stosca` | duplication_status: `jedinstven`
- `HS-13` | naslov: `Masa tereta na pontonu nagnuta za kut` | duplication_status: `jedinstven` | migration_status: `validirano` | napomena: `javna prerada potvrdena u U07 WE Plutajuca servisna platforma s pomaknutim kompresorom`
- `HS-14` | naslov: `Sila za otvaranje poklopca trokutastog oblika` | duplication_status: `varijanta`
- `HS-15` | naslov: `Hvatiste sile i kut na ploci u kruznom cilindru` | duplication_status: `jedinstven`
- `HS-16` | naslov: `Sila na trokutasti poklopac AOB` | duplication_status: `varijanta`
- `HS-17` | naslov: `Sila na polukuglasti zatvarac` | duplication_status: `varijanta`
- `HS-18` | naslov: `Gustoca polucilindricnog materijala` | duplication_status: `jedinstven`
- `HS-19` | naslov: `Visina h2 ispunjenja desnog spremnika` | duplication_status: `jedinstven`
- `HS-20` | naslov: `Reakcija i moment u tocci A (kocka)` | duplication_status: `jedinstven`
- `HS-21` | naslov: `Visina H kod koje se otvara kuglasti zatvarac` | duplication_status: `varijanta`
- `HS-22` | naslov: `Masa polukuglaste posude s kuglicom unutra` | duplication_status: `jedinstven`
- `HS-23` | naslov: `Sila F na kvadratnu gredu` | duplication_status: `varijanta`
- `HS-24` | naslov: `Visina H za otvaranje polukuglastog poklopca (uteg i cijev)` | duplication_status: `jedinstven`
- `HS-25` | naslov: `Udaljenost utega za otvaranje poklopca` | duplication_status: `bliski_duplikat`
- `HS-26` | naslov: `Sila za pridrzavanje poklopca (polukrug + ravna ploca)` | duplication_status: `jedinstven`
- `HS-27` | naslov: `Gustoca kockastog utega za ravnotezu poklopca` | duplication_status: `varijanta`
- `HS-28` | naslov: `Masa valjka za zatvaranje otvora spremnika` | duplication_status: `varijanta`
- `HS-29` | naslov: `Visina gornjeg ruba kocke leda u Coca-Coli` | duplication_status: `varijanta`
- `HS-30` | naslov: `Minimalna udaljenost pregrade od zgloba` | duplication_status: `varijanta`
- `HS-31` | naslov: `Gustoca kvadratne grede u ravnotezi` | duplication_status: `jedinstven`
- `HS-32` | naslov: `Reakcija u tocci A (sila i moment) za pregradu` | duplication_status: `jedinstven`
- `HS-33` | naslov: `Sila za podizanje konusnog cepa` | duplication_status: `jedinstven`
- `HS-34` | naslov: `Sila F u rucici pumpe` | duplication_status: `rezervni`
- `HS-35` | naslov: `Promjena nivoa vode topljenja leda s kulicom` | duplication_status: `jedinstven`
- `HS-36` | naslov: `Tonjenje broda s pukotinom` | duplication_status: `jedinstven`
- `HS-37` | naslov: `Polozaji ojacanja valjkaste bacve` | duplication_status: `jedinstven` | migration_status: `validirano` | napomena: `javna prerada potvrdena u U05 WE Servisni spremnik s tri vodoravne ukrute`
- `HS-38` | naslov: `Hidraulicki amortizer: masa klipa i sila opterecenja` | duplication_status: `rezervni`
- `HS-39` | naslov: `Maksimalna tezina podizana dizalicom` | duplication_status: `jedinstven`
- `HS-40` | naslov: `Maksimalna visina razine fluida za drvenu pregradu` | duplication_status: `jedinstven`

### private/materials/SAVAR_sesija2_RM_Bernoulli_Istjecanje_Cjevovod.md

- status: `inventirano po headingima`
- broj jedinica: `75`

#### Blok `RM` - preliminarni_cilj: `U04`

- `RM-1` | naslov: `Udaljenost baze drvenog valjka od dna posude nakon rotacije` | duplication_status: `jedinstven`
- `RM-2` | naslov: `Pretlak u tocci A u posudi s dva fluida` | duplication_status: `varijanta`
- `RM-3` | naslov: `Sila na poklopac cilindricne posude (rotacija, pol. fluida ostaje)` | duplication_status: `varijanta`
- `RM-4` | naslov: `Udaljenost a2 valjka od dna polukuglaste posude` | duplication_status: `jedinstven`
- `RM-5` | naslov: `Tlak u tocci A na vanjskom plastu cilindricne posude` | duplication_status: `varijanta`
- `RM-6` | naslov: `Sila F na pregradu kolica koja ubrzavaju udesno` | duplication_status: `varijanta`
- `RM-7` | naslov: `Visine h1, h2, h3 u tri cjevcice nakon rotacije` | duplication_status: `varijanta`
- `RM-8` | naslov: `Maksimalna dozvoljena akceleracija kolica` | duplication_status: `varijanta`
- `RM-9` | naslov: `Kutna brzina omega za otvaranje poklopca` | duplication_status: `varijanta`
- `RM-10` | naslov: `Sila na straznju stranu AB kolica na kosini` | duplication_status: `varijanta`
- `RM-11` | naslov: `Akceleracija kockastog spremnika (3D problem)` | duplication_status: `jedinstven`
- `RM-12` | naslov: `Polozaj vertikalne osi rotacije kockastog spremnika` | duplication_status: `jedinstven`
- `RM-13` | naslov: `Sila F na pregradu kolica (varijanta s a = 7.2 m/s2)` | duplication_status: `bliski_duplikat`
- `RM-14` | naslov: `Vertikalni stozac: visina h fluida prije rotacije` | duplication_status: `jedinstven`
- `RM-15` | naslov: `Visina h podizanja kruznog poklopca` | duplication_status: `varijanta`
- `RM-16` | naslov: `Kutna brzina omega stosca da sila u vijcima bude 3x veca` | duplication_status: `jedinstven`

#### Blok `BJ` - preliminarni_cilj: `REV-U09/U10`

- `BJ-1` | naslov: `Protok Q kroz Venturijeve cijevi s Hg manometrom` | duplication_status: `varijanta`
- `BJ-2` | naslov: `Vrijeme spustanja cilindricne kape na stup` | duplication_status: `jedinstven`
- `BJ-3` | naslov: `Minimalna brzina camca za crpljenje vode venturimetrom` | duplication_status: `jedinstven`
- `BJ-4` | naslov: `Visine h1, h3, h5 unutar razgranatog spremnika` | duplication_status: `jedinstven`
- `BJ-5` | naslov: `Smjer strujanja i protoci izmedu tri rezervoara` | duplication_status: `jedinstven`
- `BJ-6` | naslov: `Razlika x nivoa vode u rezervoarima s izotermnom kompresijom` | duplication_status: `jedinstven`
- `BJ-7` | naslov: `Visina h nivoa u spremniku (sustav s donjim i gornjim izlazom)` | duplication_status: `varijanta`
- `BJ-8` | naslov: `Promjer d grla klepsidre (vodeni sat)` | duplication_status: `jedinstven`
- `BJ-9` | naslov: `Promjer d cjevovoda za konstantnu razinu u spremniku 2` | duplication_status: `jedinstven`
- `BJ-10` | naslov: `Kolicine fluida V1, V2, V3 u tri donja spremnika` | duplication_status: `jedinstven`
- `BJ-11` | naslov: `Protok Q za razgranati sustav vise spremnika` | duplication_status: `varijanta`
- `BJ-12` | naslov: `Promjeri D1 i D2 otvora izmedu spremnika (jednaki protoci)` | duplication_status: `varijanta`
- `BJ-13` | naslov: `Visine h1, h3, h5 u razgranatom spremniku (varijanta Q = 30 l/s)` | duplication_status: `bliski_duplikat`
- `BJ-14` | naslov: `Promjena visine x gornjeg spremnika (difuzor na izlazu)` | duplication_status: `varijanta`

#### Blok `IS` - preliminarni_cilj: `REV-U10/U13`

- `IS-1` | naslov: `Vremena praznjenja cilindricne posude (otvor na plastu i na dnu)` | duplication_status: `varijanta`
- `IS-2` | naslov: `Vrijeme izjednacavanja razine u dva kuglasta spremnika` | duplication_status: `jedinstven`
- `IS-3` | naslov: `Vrijeme praznjenja lijevka (trakture)` | duplication_status: `varijanta`
- `IS-4` | naslov: `Ukupno vrijeme punjenja posude kroz ventil` | duplication_status: `jedinstven`
- `IS-5` | naslov: `Praznjenje cilindricne posude s plutajucim valjem` | duplication_status: `jedinstven`
- `IS-6` | naslov: `Praznjenje cilindricnog spremnika s Hg manometrom` | duplication_status: `varijanta`
- `IS-7` | naslov: `Praznjenje pravokutnog spremnika zatvorenog prema atmosferi` | duplication_status: `jedinstven`
- `IS-8` | naslov: `Praznjenje paraboloidnog spremnika` | duplication_status: `jedinstven`
- `IS-9` | naslov: `Praznjenje posude do trenutka potapanja` | duplication_status: `jedinstven`

#### Blok `CV` - preliminarni_cilj: `U13/REV-U10/U13`

- `CV-1` | naslov: `Povecanje protoka serijskim i paralelnim spojem pumpe` | duplication_status: `jedinstven`
- `CV-2` | naslov: `Minimalni pretlak u sustavu (pumpa + sifon)` | duplication_status: `jedinstven`
- `CV-3` | naslov: `Snaga reverzibilnog agregata (pumpni i turbinski pogon)` | duplication_status: `jedinstven`
- `CV-4` | naslov: `Sirina klimatizacijskog voda (ekvivalentni promjer, rekonstrukcija)` | duplication_status: `jedinstven`
- `CV-5` | naslov: `Snaga pumpe (vodoopskrba, korozija povecava hrapavost)` | duplication_status: `varijanta`
- `CV-6` | naslov: `Snaga pumpe (vodoopskrba, plastificiranje cijevi)` | duplication_status: `bliski_duplikat`
- `CV-7` | naslov: `Pjescana hrapavost cijevi iz izmjerenog protoka i pada tlaka` | duplication_status: `varijanta`
- `CV-8` | naslov: `Visina h2 vode u spremniku (12% protoka skrece)` | duplication_status: `jedinstven`
- `CV-9` | naslov: `Odnos D/d za minimalne lokalne gubitke (naglo prosirenje)` | duplication_status: `varijanta`
- `CV-10` | naslov: `Odnos protoka 3 i 4 cijevi unutar zastitne cijevi (laminarno)` | duplication_status: `jedinstven`
- `CV-11` | naslov: `Promjer D3 cijevi za stabilan nivo u spremniku 3` | duplication_status: `jedinstven`
- `CV-12` | naslov: `Usteda (%) akumulacijom vode 8 sati na dan` | duplication_status: `jedinstven`
- `CV-13` | naslov: `Maksimalni domet L0 mlaza vode iz cjevovoda` | duplication_status: `jedinstven`
- `CV-14` | naslov: `Sila F za potiskivanje fluida hipodermalnom iglom` | duplication_status: `jedinstven`
- `CV-15` | naslov: `Radna tocka pumpe (vodoskok)` | duplication_status: `varijanta`
- `CV-16` | naslov: `Radna tocka pumpe (domet preljeva mlaza)` | duplication_status: `varijanta`
- `CV-17` | naslov: `Protok Q kroz sistem s turbinom` | duplication_status: `jedinstven`
- `CV-18` | naslov: `Povecanje protoka ugradnjom vece pumpe` | duplication_status: `varijanta`
- `CV-19` | naslov: `Povecanje stupnja djelovanja turbine ugradnjom difuzora` | duplication_status: `varijanta`
- `CV-20` | naslov: `Visina h2 u spremniku (razgranati sustav 3 spremnika)` | duplication_status: `bliski_duplikat`
- `CV-21` | naslov: `Promjer D okrugle cijevi (zamjena kvadratne)` | duplication_status: `jedinstven`
- `CV-22` | naslov: `Koliko puta se smanji protok pregradom (laminarno)` | duplication_status: `jedinstven`
- `CV-23` | naslov: `Promjer d novog cjevovoda za opskrbu vode (rekonstrukcija, 75% vise)` | duplication_status: `varijanta`
- `CV-24` | naslov: `Nagib kanala trapeznog presjeka` | duplication_status: `rezervni`
- `CV-25` | naslov: `Minimalni pretlak pM u kompenzacijskoj posudi` | duplication_status: `jedinstven`
- `CV-26` | naslov: `Razlika H nivoa akumulacijskog jezera i kompenzacione komore` | duplication_status: `jedinstven`
- `CV-27` | naslov: `Vrijeme t praznjenja case Coca-Cole slamkom` | duplication_status: `jedinstven`
- `CV-28` | naslov: `Pretlaci punjenja i praznjenja hidraulickog akumulatora` | duplication_status: `jedinstven`
- `CV-29` | naslov: `Koeficijent lokalnog gubitka ventila Kv` | duplication_status: `varijanta`
- `CV-30` | naslov: `Radna tocka pumpe (karakteristika hp = 12 - 10^5 Q^2)` | duplication_status: `varijanta`
- `CV-31` | naslov: `Izlazni promjer cijevi D2 (rezervoar, konstantna razina)` | duplication_status: `varijanta`
- `CV-32` | naslov: `Hidraulicke karakteristike pumpe (hidraulicki stol)` | duplication_status: `jedinstven`
- `CV-33` | naslov: `Sirina klimatizacijskog voda (varijanta, rekonstrukcija 2)` | duplication_status: `bliski_duplikat`
- `CV-34` | naslov: `Visina H2 u sustavu paralelnih cjevovoda` | duplication_status: `varijanta`
- `CV-35` | naslov: `Visina h vode u pravokutnom kanalu (transferom kroz kanal)` | duplication_status: `rezervni`
- `CV-36` | naslov: `Promjer dimnjaka za vruce dimne plinove` | duplication_status: `jedinstven`

### private/materials/Vjezbe/MF1-vjezba 5_objasnjeno (2).md

- status: `inventirano po headingima`
- broj jedinica: `3`
- preliminarni_cilj: `U05`

- `OBJ-5-1` | naslov: `Pravokutna vertikalna zaklopka`
- `OBJ-5-2` | naslov: `Nagnuta zaklopka (Ravnoteza momenata)`
- `OBJ-5-3` | naslov: `Ukupna sila (Hidrostatska + Atmosferska)`

## Izvori locirani, ali jos neinventirani po zadacima

### private/materials/zdravko-virag-mehanika-fluida.md

- status: `svi tekstualno citljivi Virag blokovi su inventirani i urednicki zatvoreni; answers-only / source-gap reference ostaju izvan ovog closure-prolaza i ne vode se kao otvorene migracijske veze`
- razlog: zadaci su ugradeni u veliki knjizni tekst, pa je inventura morala ici po stvarnim odjeljcima `Zadaci`; nakon tog rezanja zatvoreni su svi citljivi blokovi `1.x`, `2.x`, `5.x` i `7.x`.
- potvrdeni marker-zapisi: vise odvojenih `ZADACI` / `## Zadaci` / `### Zadaci` blokova.
- potvrden task-pattern: `^(**)?[1-7].[0-9]+` na stvarnim task-retcima vraca korisne pogotke.
- tekstualno zatvoreni Virag blokovi:
	- `1.1-1.25` dimenzijska analiza
	- `2.1-2.11` prvi staticki podblok prije `2.6 SILA UZGONA`
	- `2.21-2.89` kasni staticki blok vidljiv u markdownu, uz rupe u numeraciji koje su u ovom izvoru samo answers-only
	- `5.1-5.26` integralni pristup / kolicina gibanja
	- `7.1-7.29` cjevovodi
- preostali Virag source-gap / answers-only blokovi:
	- answers-only / source-gap refs unutar statike: `2.12-2.20`, `2.41`, `2.45`
- vazna napomena: isti regex zahvaca i dio rjesenja / pomocnih prijelaza, pa finalni extraction mora biti vezan uz granice pojedinih odjeljaka `Zadaci`, a ne samo uz globalni regex-popis.
- dodatna anomalija izvora: u trenutnom `zdravko-virag-mehanika-fluida.md` za `2.12-2.20`, `2.41` i `2.45` pojavljuju se odgovori u zavrsnom rjesenjskom bloku, ali se puni tekstovi zadataka ne pojavljuju kao citljivi task-retci u tijelu dokumenta.
- dodatna anomalija izvora: u trenutnom markdown-exportu `4.1-4.18` i `6.1-6.37` zasad su vidljivi samo kroz zavrsni rjesenjski blok; nisu pronadeni zasebni, citljivi task-markeri poput onih koji postoje za `1.x`, `2.x`, `5.x` i `7.x`.

#### Blok `Virag 1.x` - preliminarni_cilj: `REZERVNI`

- status: `inventirano iz stvarnog bloka ## Zadaci prije poglavlja 2; duplication_status zatvoren`
- broj jedinica: `25`

- `VG-01-01` | legacy_ref: `1.1` | naslov: `Dimenzionalno nezavisni skupovi fizikalnih velicina` | duplication_status: `rezervni`
- `VG-01-02` | legacy_ref: `1.2` | naslov: `Turbulentno strujanje uz cvrstu granicu i Pi-teorem` | duplication_status: `rezervni`
- `VG-01-03` | legacy_ref: `1.3` | naslov: `Sila tlaka na uronjenu ravnu povrsinu` | duplication_status: `rezervni`
- `VG-01-04` | legacy_ref: `1.4` | naslov: `Sila otpora povrsinskom gibanju broda` | duplication_status: `rezervni`
- `VG-01-05` | legacy_ref: `1.5` | naslov: `Brzina tonjenja tijela u fluidu` | duplication_status: `varijanta`
- `VG-01-06` | legacy_ref: `1.6` | naslov: `Maksimalna usisna visina pumpe` | duplication_status: `varijanta`
- `VG-01-07` | legacy_ref: `1.7` | naslov: `Varijanta maksimalne usisne visine pumpe` | duplication_status: `bliski_duplikat`
- `VG-01-08` | legacy_ref: `1.8` | naslov: `Sila otpora u viskoznom stlacivom fluidu` | duplication_status: `rezervni`
- `VG-01-09` | legacy_ref: `1.9` | naslov: `Visina dobave pumpe iz Pi-teorema` | duplication_status: `jedinstven`
- `VG-01-10` | legacy_ref: `1.10` | naslov: `Debljina granicnog sloja uz tijelo` | duplication_status: `rezervni`
- `VG-01-11` | legacy_ref: `1.11` | naslov: `Snaga gubitka trenja u lezaju` | duplication_status: `rezervni`
- `VG-01-12` | legacy_ref: `1.12` | naslov: `Brzina sirenja valova na slobodnoj povrsini` | duplication_status: `rezervni`
- `VG-01-13` | legacy_ref: `1.13` | naslov: `Sila uzgona projektila` | duplication_status: `rezervni`
- `VG-01-14` | legacy_ref: `1.14` | naslov: `Protok fluida koji povlaci remen` | duplication_status: `jedinstven`
- `VG-01-15` | legacy_ref: `1.15` | naslov: `Snaga vucenja hidraulicki glatke kugle` | duplication_status: `rezervni`
- `VG-01-16` | legacy_ref: `1.16` | naslov: `Moment u laminarnom strujanju izmedu koaksijalnih cilindara` | duplication_status: `varijanta`
- `VG-01-17` | legacy_ref: `1.17` | naslov: `Pad tlaka u laminarnom strujanju kroz cijev` | duplication_status: `jedinstven`
- `VG-01-18` | legacy_ref: `1.18` | naslov: `Volumenski protok preko mjerne brane` | duplication_status: `jedinstven`
- `VG-01-19` | legacy_ref: `1.19` | naslov: `Laminarni protok kroz trokutasti kanal` | duplication_status: `jedinstven`
- `VG-01-20` | legacy_ref: `1.20` | naslov: `Snaga Peltonove turbine i slicnost` | duplication_status: `jedinstven`
- `VG-01-21` | legacy_ref: `1.21` | naslov: `Razlika tlaka na izlazu i ulazu pumpe` | duplication_status: `jedinstven`
- `VG-01-22` | legacy_ref: `1.22` | naslov: `Dimenzijska analiza kosog hica` | duplication_status: `rezervni`
- `VG-01-23` | legacy_ref: `1.23` | naslov: `Brzina istjecanja nakon trenutnog otvaranja ventila` | duplication_status: `jedinstven`
- `VG-01-24` | legacy_ref: `1.24` | naslov: `Vrijeme praznjenja bacve kroz otvor na dnu` | duplication_status: `varijanta`
- `VG-01-25` | legacy_ref: `1.25` | naslov: `Sila fluida na elipsoid u funkciji brzine i povrsine` | duplication_status: `rezervni`

#### Blok `Virag 7.x` - preliminarni_cilj: `U13`

- status: `inventirano iz stvarnog bloka # Zadaci prije literature; duplication_status zatvoren`
- broj jedinica: `29`

- `VG-07-01` | legacy_ref: `7.1` | naslov: `Prepumpavanje preko brijega i tlak u najvisoj tocki` | duplication_status: `varijanta`
- `VG-07-02` | legacy_ref: `7.2` | naslov: `Potrebna visina razine za zadani protok u sustavu` | duplication_status: `varijanta`
- `VG-07-03` | legacy_ref: `7.3` | naslov: `Pretlak u spremniku za zadanu visinu mlaza` | duplication_status: `varijanta`
- `VG-07-04` | legacy_ref: `7.4` | naslov: `Manometarski tlak u spremniku 2 za zadani protok` | duplication_status: `jedinstven`
- `VG-07-05` | legacy_ref: `7.5` | naslov: `Visina dobave pumpe i protok bez pumpe` | duplication_status: `varijanta`
- `VG-07-06` | legacy_ref: `7.6` | naslov: `Promjena protoka pri zamjeni polovice cjevovoda` | duplication_status: `jedinstven`
- `VG-07-07` | legacy_ref: `7.7` | naslov: `Visina mlaza iz spremnika pod pretlakom` | duplication_status: `varijanta`
- `VG-07-08` | legacy_ref: `7.8` | naslov: `Procjena povrsine pukotine u cjevovodu` | duplication_status: `jedinstven` | migration_status: `validirano` | napomena: `javna prerada potvrdena u U13 WE Nezatvoreni servisni ispust na rashladnom cjevovodu`
- `VG-07-09` | legacy_ref: `7.9` | naslov: `Protok kroz lijevi krak cijevi` | duplication_status: `varijanta`
- `VG-07-10` | legacy_ref: `7.10` | naslov: `Protok nakon lokalne deformacije cjevovoda` | duplication_status: `varijanta`
- `VG-07-11` | legacy_ref: `7.11` | naslov: `Protok kroz prikljucni cjevovod nakon otvaranja` | duplication_status: `jedinstven`
- `VG-07-12` | legacy_ref: `7.12` | naslov: `Ustaljeni protok nakon potpunog zatvaranja ventila` | duplication_status: `varijanta`
- `VG-07-13` | legacy_ref: `7.13` | naslov: `Visina mlaza nakon zatvaranja jedne od dviju mlaznica` | duplication_status: `varijanta`
- `VG-07-14` | legacy_ref: `7.14` | naslov: `Protok kroz pumpu u razgranatom cjevovodnom sustavu` | duplication_status: `varijanta`
- `VG-07-15` | legacy_ref: `7.15` | naslov: `Protok nakon potpunog otvaranja ventila na horizontalnoj cijevi` | duplication_status: `varijanta`
- `VG-07-16` | legacy_ref: `7.16` | naslov: `Protok nakon zatvaranja jedne grane cjevovoda` | duplication_status: `varijanta`
- `VG-07-17` | legacy_ref: `7.17` | naslov: `Promjer cjevovoda za stalnu razinu u spremniku 2` | duplication_status: `varijanta`
- `VG-07-18` | legacy_ref: `7.18` | naslov: `Promjer cijevi za zadanu izlaznu brzinu mlaza` | duplication_status: `varijanta`
- `VG-07-19` | legacy_ref: `7.19` | naslov: `Promjer cjevovoda za trostruko veci protok` | duplication_status: `varijanta`
- `VG-07-20` | legacy_ref: `7.20` | naslov: `Promjer cjevovoda za zadani pretlak u tocki A` | duplication_status: `varijanta`
- `VG-07-21` | legacy_ref: `7.21` | naslov: `Promjer cjevovoda u sustavu hladenja` | duplication_status: `jedinstven`
- `VG-07-22` | legacy_ref: `7.22` | naslov: `Promjer izlazne cijevi iz spremnika 2 za jednake protoke` | duplication_status: `varijanta`
- `VG-07-23` | legacy_ref: `7.23` | naslov: `Promjer cijevi d za zadani pretlak u tocki A` | duplication_status: `varijanta`
- `VG-07-24` | legacy_ref: `7.24` | naslov: `Promjer cijevi za jednake protoke u dvjema granama` | duplication_status: `varijanta`
- `VG-07-25` | legacy_ref: `7.25` | naslov: `Promjer paralelnog cjevovoda za zadani protok` | duplication_status: `varijanta`
- `VG-07-26` | legacy_ref: `7.26` | naslov: `Protok, pretlak i snaga mlaza u dvjema konfiguracijama` | duplication_status: `jedinstven`
- `VG-07-27` | legacy_ref: `7.27` | naslov: `Protok u sustavu i pretlak u presjeku A-A` | duplication_status: `jedinstven`
- `VG-07-28` | legacy_ref: `7.28` | naslov: `Odnos viskoznog i neviskoznog protoka u sustavu` | duplication_status: `jedinstven`
- `VG-07-29` | legacy_ref: `7.29` | naslov: `Sila i snaga za pomicanje stapa s izlazom ulja` | duplication_status: `varijanta`

#### Blok `Virag 2.1-2.11` - preliminarni_cilj: `REV-U03/U04`

- status: `inventirano iz prvog statickog bloka prije 2.6 SILA UZGONA; duplication_status zatvoren`
- broj jedinica: `11`

- `VG-02-01` | legacy_ref: `2.1` | naslov: `Spojene cilindricne posude sa stapom` | duplication_status: `varijanta`
- `VG-02-02` | legacy_ref: `2.2` | naslov: `Cilindricna boca s dovodom zraka i ispusnim otvorom` | duplication_status: `jedinstven`
- `VG-02-03` | legacy_ref: `2.3` | naslov: `Ubrzanje zatvorene posude iz poznatih tlakova` | duplication_status: `jedinstven`
- `VG-02-04` | legacy_ref: `2.4` | naslov: `Akceleracija kolica za zadani pretlak u tocki A` | duplication_status: `varijanta`
- `VG-02-05` | legacy_ref: `2.5` | naslov: `Dvofluidni spremnik u jednoliko ubrzanom gibanju` | duplication_status: `jedinstven`
- `VG-02-06` | legacy_ref: `2.6` | naslov: `Kolica na kosini i jednakost tlakova u tockama A i B` | duplication_status: `varijanta`
- `VG-02-07` | legacy_ref: `2.7` | naslov: `Izlijevanje fluida iz posude na ubrzanim kolicima` | duplication_status: `jedinstven`
- `VG-02-08` | legacy_ref: `2.8` | naslov: `Dvokraka cjevcica u rotaciji` | duplication_status: `varijanta`
- `VG-02-09` | legacy_ref: `2.9` | naslov: `Rotacija cilindricne posude uz zadrzavanje trecine fluida` | duplication_status: `varijanta`
- `VG-02-10` | legacy_ref: `2.10` | naslov: `U-cijev sa stapom i jednaka visina u oba kraka` | duplication_status: `jedinstven`
- `VG-02-11` | legacy_ref: `2.11` | naslov: `Manometarski tlak u rotirajucoj cilindricnoj posudi` | duplication_status: `varijanta`

#### Blok `Virag 2.21-2.89` - preliminarni_cilj: `REV-U05/U06/U07`

- status: `inventirano iz kasnog statickog bloka Zadaci 127; duplication_status zatvoren`
- broj jedinica: `67`
- source_gap_refovi_u_numeraciji: `2.41`, `2.45`

- `VG-02-21` | legacy_ref: `2.21` | naslov: `Otvor na dnu posude zatvoren cepom s balonom na uzetu` | duplication_status: `jedinstven`
- `VG-02-22` | legacy_ref: `2.22` | naslov: `Rezultantna sila na horizontalni kruzni poklopac` | duplication_status: `jedinstven`
- `VG-02-23` | legacy_ref: `2.23` | naslov: `Promjer valjkastog plovka za otvaranje kruznog zatvaraca` | duplication_status: `jedinstven`
- `VG-02-24` | legacy_ref: `2.24` | naslov: `Pretlak u gornjem cilindru za ravnotezu stapa` | duplication_status: `rezervni`
- `VG-02-25` | legacy_ref: `2.25` | naslov: `Tlak p3 u spremniku 3 za ravnotezu stapa` | duplication_status: `rezervni`
- `VG-02-26` | legacy_ref: `2.26` | naslov: `Moment sile hidrostatskog tlaka na bocni kruzni poklopac` | duplication_status: `jedinstven`
- `VG-02-27` | legacy_ref: `2.27` | naslov: `Minimalna tezina poklopca jedinicne sirine` | duplication_status: `varijanta`
- `VG-02-28` | legacy_ref: `2.28` | naslov: `Podtlak pri otvaranju kruznog poklopca silom F` | duplication_status: `varijanta`
- `VG-02-29` | legacy_ref: `2.29` | naslov: `Visina razine pri kojoj je zatvarac OA jos zatvoren` | duplication_status: `varijanta`
- `VG-02-30` | legacy_ref: `2.30` | naslov: `Vertikalna sila za drzanje zatvaraca na zatvorenom spremniku` | duplication_status: `varijanta`
- `VG-02-31` | legacy_ref: `2.31` | naslov: `Sila za drzanje poklopca jedinicne sirine u tocki O` | duplication_status: `varijanta`
- `VG-02-32` | legacy_ref: `2.32` | naslov: `Sila u lancu brane OB` | duplication_status: `varijanta`
- `VG-02-33` | legacy_ref: `2.33` | naslov: `Pretlak za zatvoren kruzni poklopac zglobno vezan u tocki A` | duplication_status: `varijanta`
- `VG-02-34` | legacy_ref: `2.34` | naslov: `Rezultantna sila na stijenku ABCD zatvorenog prizmaticnog spremnika` | duplication_status: `jedinstven`
- `VG-02-35` | legacy_ref: `2.35` | naslov: `Rezultantna sila na poklopac AB i hvatiste` | duplication_status: `varijanta`
- `VG-02-36` | legacy_ref: `2.36` | naslov: `Rezultantna sila na pravokutni poklopac AO` | duplication_status: `varijanta`
- `VG-02-37` | legacy_ref: `2.37` | naslov: `Moment za drzanje poklopca u tocki O` | duplication_status: `varijanta`
- `VG-02-38` | legacy_ref: `2.38` | naslov: `Duljina L za nulnu vertikalnu silu na konstrukciju ABCD` | duplication_status: `jedinstven` | migration_status: `validirano` | napomena: `javna prerada potvrdena u U06 WE Sklopiva servisna brana s zakrivljenim rubom`
- `VG-02-39` | legacy_ref: `2.39` | naslov: `Pretlak u tocki D za otvaranje trokutastog poklopca ABC` | duplication_status: `jedinstven`
- `VG-02-40` | legacy_ref: `2.40` | naslov: `Sila za drzanje poklopca zanemarive tezine` | duplication_status: `varijanta`
- `VG-02-42` | legacy_ref: `2.42` | naslov: `Vertikalna sila u tocki C za ravnotezu konstrukcije OABC` | duplication_status: `jedinstven`
- `VG-02-43` | legacy_ref: `2.43` | naslov: `Pretlak za otvaranje brane u tocki O` | duplication_status: `varijanta`
- `VG-02-44` | legacy_ref: `2.44` | naslov: `Kvadratna prizma potpuno ispunjena fluidom (naslov trunciran u izvoru)` | duplication_status: `jedinstven`
- `VG-02-46` | legacy_ref: `2.46` | naslov: `Sila za guranje otvorene posude da ostane 75 posto vode` | duplication_status: `jedinstven` | migration_status: `validirano` | napomena: `javna prerada potvrdena u U04 WE Procesna kada na automatskoj platformi`
- `VG-02-47` | legacy_ref: `2.47` | naslov: `Obujam vode i ubrzanje kockastih kolica` | duplication_status: `jedinstven`
- `VG-02-48` | legacy_ref: `2.48` | naslov: `Rezultantna sila na stijenku CD nakon istjecanja iz kolica` | duplication_status: `jedinstven`
- `VG-02-49` | legacy_ref: `2.49` | naslov: `Akceleracija kolica niz kosinu i sila na prednju stijenku AB` | duplication_status: `varijanta`
- `VG-02-50` | legacy_ref: `2.50` | naslov: `Nagib spremnika da slobodna povrsina bude okomita na AB` | duplication_status: `jedinstven` | migration_status: `validirano` | napomena: `javna prerada potvrdena u U04 WE Zatvoreni servisni modul s kosom inspekcijskom stijenkom`
- `VG-02-51` | legacy_ref: `2.51` | naslov: `Sila fluida na dno kolica niz kosinu` | duplication_status: `varijanta`
- `VG-02-52` | legacy_ref: `2.52` | naslov: `Ubrzanje i sila na dno kolica niz kosinu` | duplication_status: `jedinstven`
- `VG-02-53` | legacy_ref: `2.53` | naslov: `Rezultirajuce sile na dno i poklopac rotirajuce posude` | duplication_status: `jedinstven`
- `VG-02-54` | legacy_ref: `2.54` | naslov: `Rezultantne sile na poklopac i dno uronjene cilindricne posude` | duplication_status: `jedinstven`
- `VG-02-55` | legacy_ref: `2.55` | naslov: `Visina H1 za ravnotezu brane izmedu dvaju fluida` | duplication_status: `jedinstven`
- `VG-02-56` | legacy_ref: `2.56` | naslov: `Visina fluida u brani za ravnotezu` | duplication_status: `varijanta`
- `VG-02-57` | legacy_ref: `2.57` | naslov: `Vertikalna sila za ravnotezu konstrukcije AB` | duplication_status: `jedinstven`
- `VG-02-58` | legacy_ref: `2.58` | naslov: `Ukupna masa brane i utega za ravnotezu` | duplication_status: `varijanta`
- `VG-02-59` | legacy_ref: `2.59` | naslov: `Masa utega za zatvoren poklopac OA` | duplication_status: `varijanta`
- `VG-02-60` | legacy_ref: `2.60` | naslov: `Horizontalna sila za ravnotezu zglobnog zatvaraca` | duplication_status: `varijanta`
- `VG-02-61` | legacy_ref: `2.61` | naslov: `Visina fluida za zadanu silu drzanja brane AO` | duplication_status: `varijanta`
- `VG-02-62` | legacy_ref: `2.62` | naslov: `Moment sile hidrostatskog tlaka na poklopac oko O` | duplication_status: `varijanta`
- `VG-02-63` | legacy_ref: `2.63` | naslov: `Reakcija u tocki A zbog hidrostatskog tlaka na branu` | duplication_status: `jedinstven`
- `VG-02-64` | legacy_ref: `2.64` | naslov: `Sila za drzanje poklopca da se ne otvori` | duplication_status: `varijanta`
- `VG-02-65` | legacy_ref: `2.65` | naslov: `Vertikalna sila za otvaranje poklopca` | duplication_status: `varijanta`
- `VG-02-66` | legacy_ref: `2.66` | naslov: `Sila kod koje je poklopac jos zatvoren` | duplication_status: `bliski_duplikat`
- `VG-02-67` | legacy_ref: `2.67` | naslov: `Sila za drzanje zatvaraca zanemarive tezine` | duplication_status: `varijanta`
- `VG-02-68` | legacy_ref: `2.68` | naslov: `Moment sile hidrostatskog tlaka na zatvarac OAB` | duplication_status: `varijanta`
- `VG-02-69` | legacy_ref: `2.69` | naslov: `Pretlak u ravnini kroz O za ravnotezu trokutastog zatvaraca` | duplication_status: `jedinstven`
- `VG-02-70` | legacy_ref: `2.70` | naslov: `Horizontalna sila za ravnotezu homogene grede` | duplication_status: `jedinstven`
- `VG-02-71` | legacy_ref: `2.71` | naslov: `Visina H da rezultantna sila na kocku bude nula` | duplication_status: `jedinstven` | migration_status: `validirano` | napomena: `javna prerada potvrdena u U07 WE Kalibracijski modul na granici ulja i vode`
- `VG-02-72` | legacy_ref: `2.72` | naslov: `Tlak p0 i duljina L za ponistenje sila na zatvaracu` | duplication_status: `jedinstven`
- `VG-02-73` | legacy_ref: `2.73` | naslov: `Pretlak ispod poklopca za ravnotezu tezine` | duplication_status: `jedinstven`
- `VG-02-74` | legacy_ref: `2.74` | naslov: `Sila za pridrzavanje poklopca s djelomicno zatvorenim zrakom` | duplication_status: `jedinstven`
- `VG-02-75` | legacy_ref: `2.75` | naslov: `Rezultantna sila na zatvarac i hvatiste` | duplication_status: `jedinstven`
- `VG-02-76` | legacy_ref: `2.76` | naslov: `Vertikalna sila na cilindricni zatvarac s uzgonom` | duplication_status: `jedinstven`
- `VG-02-77` | legacy_ref: `2.77` | naslov: `Dubina potonuca cilindricne posude nakon ispustanja zraka` | duplication_status: `jedinstven`
- `VG-02-78` | legacy_ref: `2.78` | naslov: `Promjena sile u vijcima nakon odzracivanja poklopca` | duplication_status: `jedinstven`
- `VG-02-79` | legacy_ref: `2.79` | naslov: `Rezultantna sila tlaka na kruzni cilindar` | duplication_status: `varijanta`
- `VG-02-80` | legacy_ref: `2.80` | naslov: `Horizontalna i vertikalna sila na cilindricni zatvarac` | duplication_status: `varijanta`
- `VG-02-81` | legacy_ref: `2.81` | naslov: `Horizontalna i vertikalna sila na poklopac jed. sirine` | duplication_status: `varijanta`
- `VG-02-82` | legacy_ref: `2.82` | naslov: `Horizontalna sila za drzanje polukruzne brane AO` | duplication_status: `varijanta`
- `VG-02-83` | legacy_ref: `2.83` | naslov: `Rezultantna sila vode na cilindricni poklopac` | duplication_status: `jedinstven`
- `VG-02-84` | legacy_ref: `2.84` | naslov: `Sila za drzanje poklopca zanemarive tezine oko O` | duplication_status: `varijanta`
- `VG-02-85` | legacy_ref: `2.85` | naslov: `Horizontalna i vertikalna sila na polucilindricni poklopac` | duplication_status: `jedinstven`
- `VG-02-86` | legacy_ref: `2.86` | naslov: `Rezultantna vanjska i unutarnja sila na poklopac na obodu posude` | duplication_status: `jedinstven`
- `VG-02-87` | legacy_ref: `2.87` | naslov: `Pretlak unutar kuglastog spremnika pri razdvajanju polovina` | duplication_status: `jedinstven`
- `VG-02-88` | legacy_ref: `2.88` | naslov: `Dubina otvaranja poklopca potopljene cilindricne posude` | duplication_status: `jedinstven`
- `VG-02-89` | legacy_ref: `2.89` | naslov: `Akceleracija otpadanja polukuglastog dna za fluidni nosac` | duplication_status: `jedinstven`

#### Blok `Virag 5.x` - preliminarni_cilj: `U11`

- status: `inventirano iz zasebnog odjeljka ### Zadaci prije poglavlja 6; duplication_status zatvoren`
- broj jedinica: `26`

- `VG-05-01` | legacy_ref: `5.1` | naslov: `Protok po jedinici sirine i sila na plocu AB` | duplication_status: `varijanta`
- `VG-05-02` | legacy_ref: `5.2` | naslov: `Obujam fluida u mlazu izmedu presjeka A i B` | duplication_status: `jedinstven`
- `VG-05-03` | legacy_ref: `5.3` | naslov: `Horizontalna sila fluida na mlaznicu` | duplication_status: `varijanta`
- `VG-05-04` | legacy_ref: `5.4` | naslov: `Rezultantna sila na mlaznicu s koljenom` | duplication_status: `varijanta`
- `VG-05-05` | legacy_ref: `5.5` | naslov: `Pretlak pri prevrtanju spremnika zbog istjecanja` | duplication_status: `jedinstven`
- `VG-05-06` | legacy_ref: `5.6` | naslov: `Rezultantna sila na luk AB za idealni i viskozni fluid` | duplication_status: `jedinstven`
- `VG-05-07` | legacy_ref: `5.7` | naslov: `Sila i moment na vijke u presjeku A-A luka` | duplication_status: `jedinstven`
- `VG-05-08` | legacy_ref: `5.8` | naslov: `Sudaranje dvaju osnosimetricnih mlazova` | duplication_status: `jedinstven`
- `VG-05-09` | legacy_ref: `5.9` | naslov: `Sila fluida na koljeno u horizontalnoj ravnini` | duplication_status: `varijanta`
- `VG-05-10` | legacy_ref: `5.10` | naslov: `Sila na vijke, protok i pretlak u presjeku A-A` | duplication_status: `jedinstven` | napomena: `stvarni U11 pilot postoji, ali javni WE Kalibracijska mlaznica na prirubnici je u konzervativnom syncu vec zakljucan kroz drugi sloj av05_04 pa se ovdje ne otvara drugo task-level validiranje`
- `VG-05-11` | legacy_ref: `5.11` | naslov: `Sila u vijcima mlaznice nakon otvaranja izlaza` | duplication_status: `varijanta`
- `VG-05-12` | legacy_ref: `5.12` | naslov: `Rezultantna sila vode na divergentnu mlaznicu` | duplication_status: `varijanta`
- `VG-05-13` | legacy_ref: `5.13` | naslov: `Sila fluida na simetricnu racvu pri otvorenom izlazu` | duplication_status: `varijanta`
- `VG-05-14` | legacy_ref: `5.14` | naslov: `Sila u vijcima mlaznice pricvrscene za postolje` | duplication_status: `varijanta`
- `VG-05-15` | legacy_ref: `5.15` | naslov: `Rezultantna sila na racvu i kut rezultante` | duplication_status: `varijanta`
- `VG-05-16` | legacy_ref: `5.16` | naslov: `Sila na racvu za zadani odnos protoka` | duplication_status: `varijanta`
- `VG-05-17` | legacy_ref: `5.17` | naslov: `Komponenta Fy sile fluida na racvu` | duplication_status: `jedinstven`
- `VG-05-18` | legacy_ref: `5.18` | naslov: `Rezultantna sila na racvu ABC s podijeljenim protocima` | duplication_status: `varijanta`
- `VG-05-19` | legacy_ref: `5.19` | naslov: `Rezultantna sila na racvu s poznatim pretlakom u presjeku 3` | duplication_status: `varijanta`
- `VG-05-20` | legacy_ref: `5.20` | naslov: `Protoci i komponente sile na racvu` | duplication_status: `jedinstven`
- `VG-05-21` | legacy_ref: `5.21` | naslov: `Rezultantna sila na racvu s manometarskim tlakom u presjeku B` | duplication_status: `varijanta`
- `VG-05-22` | legacy_ref: `5.22` | naslov: `Rezultantna sila ravninskog mlaza na plocu AB` | duplication_status: `bliski_duplikat`
- `VG-05-23` | legacy_ref: `5.23` | naslov: `Sila fluida na nepomicnu lopaticu` | duplication_status: `jedinstven` | migration_status: `validirano` | napomena: `javna prerada potvrdena u U12 WE Vodilica mlaza na ispitnom stolu`
- `VG-05-24` | legacy_ref: `5.24` | naslov: `Sila na lopaticu i optimum odnosa Q1/Q` | duplication_status: `jedinstven`
- `VG-05-25` | legacy_ref: `5.25` | naslov: `Protok mlaza koji drzi okretljivu plocu u ravnotezi` | duplication_status: `jedinstven`
- `VG-05-26` | legacy_ref: `5.26` | naslov: `Komponente sile i moment reakcije na ukljestenu lopaticu` | duplication_status: `jedinstven` | migration_status: `validirano` | napomena: `javna prerada potvrdena u U12 WE Ukljestena zakrivljena lopatica`

### PDF korpus

- `private/materials/cengel-Fluid Mechanics_ Fundamentals and Applications  .pdf`
- `private/materials/zdravko-virag-mehanika-fluida.pdf`
- `private/materials/Zbirka_zadataka_iz_MF_(Savar).pdf`
- `private/materials/Vjezbe/MF1-vjezba 1.pdf` do `MF1-vjezba 13.pdf`

status: `pending OCR / tekstualni extraction`

## Sto slijedi nakon ovog prvog prolaza

1. Virag je za tekstualno citljive blokove urednicki zatvoren; preostaju samo njegovi `source-gap / answers-only` segmenti `2.12-2.20`, `2.41`, `2.45`, `4.x` i `6.x`.
2. Sljedeci operativni korak vise nije extraction nego selektivna migracija zatvorenih treceslojnih kandidata u `source/*` poglavlja knjige.
3. PDF korpus ostaje zaseban kasniji posao za OCR ili ciljano spasavanje onih blokova koji nemaju dobar tekstualni backup.