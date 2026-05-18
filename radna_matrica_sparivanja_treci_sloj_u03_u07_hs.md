# Radna matrica sparivanja treci sloj za U03-U07 (HS)

## Svrha dokumenta

Ovo je sesti radni dokument za sparivanje treceg sloja u statickom bloku `U03-U07`. Fokus je samo na bloku `HS` iz izvora `SAVAR_sesija1_dimanzija_hidrostatika.md`.

## Pravilo citanja ove matrice

1. Skripta ostaje kanonski prvi zapis.
2. Drugi sloj ostaje vec zatvoren prvi sloj dopune.
3. `jedinstven` znaci da treci sloj donosi novu geometriju, novu inzenjersku primjenu ili rubni slucaj koji nizi slojevi nemaju u tom obliku.
4. `varijanta` znaci da zadatak ostaje u istoj obitelji ravnih ploha, zakrivljenih ploha, uzgona ili hidrostatickog balansa, ali s drukcijom formulacijom ili trazenom velicinom.
5. `bliski_duplikat` se koristi samo kad novi zapis zauzima gotovo isto urednicko mjesto kao drugi vec zatvoren zapis.
6. `rezervni` se koristi za zadatke koji jesu korisni, ali urednicki vise pripadaju hidraulickim uredajima ili ranijem bloku `U01-U03` nego glavnoj jezgri `U05-U07`.

## Staticki blok U03-U07 - postojeca jezgra

### Skriptna jezgra

- `v02_z19-v03_z29` za hidrostaticki tlak i manometriju
- `v05_z37-v05_z48` za ravne plohe
- `v06_z49-v06_z55` i rubni par `v07_z01-v07_z02` za zakrivljene plohe i prijelaz prema uzgonu
- `v02_z15` i `v03_z30` za uzgon i mjerenje gustoce

### Drugi sloj

- `av02_07-av02_16` za `U03`
- `av03_01-av03_04` za `U05`
- `av03_05-av03_10` za `U06`
- `av03_11-av03_12` za `U07`

## Treci sloj HS - preliminarna presuda

### Rubni U03 i hidraulicki uredaji

- `HS-2` | skriptna_obitelj: `v02_z19-v03_z29` | druga_slojna_veza: `av02_07-av02_13` | presuda: `jedinstven` | razlog: uronjena cilindricna posuda s izotermnom kompresijom zraka spaja hidrostaticki tlak i plinski volumen na nacin kojeg nizi slojevi nemaju.
- `HS-4` | skriptna_obitelj: `v01_z01-v01_z02` | druga_slojna_veza: `av02_01-av02_03` | presuda: `rezervni` | razlog: viseklipni hidraulicki prijenos vraca se na Pascalov uredajni blok i ne treba ga gurati u glavni tok hidrostatickih sila.
- `HS-5` | skriptna_obitelj: `v01_z01-v01_z02, v02_z19-v03_z29` | druga_slojna_veza: `av02_01-av02_06` | presuda: `rezervni` | razlog: sigurnosni ventil sa silom opruge jest zanimljiv, ali urednicki vise pripada uredajnoj hidraulici nego glavnom bloku `U05-U07`.
- `HS-19` | skriptna_obitelj: `v03_z27-v03_z29` | druga_slojna_veza: `av02_12-av02_13` | presuda: `jedinstven` | razlog: dva spremnika povezana ventilom s komprimiranim plinom u jednom spremniku daju bogatiji hidrostaticki balans od baznih manometarskih scena.
- `HS-34` | skriptna_obitelj: `v01_z01-v01_z02` | druga_slojna_veza: `nema bliskog para` | presuda: `rezervni` | razlog: sila u rucici pumpe spada u primijenjeni hidraulicki uredaj, a ne u glavni niz ploha, uzgona i stabilnosti.
- `HS-38` | skriptna_obitelj: `v01_z01-v01_z02` | druga_slojna_veza: `nema bliskog para` | presuda: `rezervni` | razlog: hidraulicki amortizer s masom klipa i silom opterecenja je vrijedan aplikacijski zadatak, ali urednicki izlazi iz trenutnog statickog toka poglavlja.

### U05 - Hidrostatske sile na ravne plohe

- `HS-1` | skriptna_obitelj: `v05_z41-v05_z44` | druga_slojna_veza: `av03_02-av03_04` | presuda: `varijanta` | razlog: ravnoteza brane s utegom ostaje ista obitelj zglobnog ravnog poklopca i momenata sila.
- `HS-14` | skriptna_obitelj: `v05_z46-v05_z48` | druga_slojna_veza: `av03_02-av03_04` | presuda: `varijanta` | razlog: trokutasti poklopac i sila za otvaranje ostaju klasicna varijanta skriptnog ravnoplosnog bloka.
- `HS-16` | skriptna_obitelj: `v05_z46-v05_z48` | druga_slojna_veza: `av03_02-av03_04` | presuda: `varijanta` | razlog: trokutasti poklopac AOB sa silom normalnom na poklopac ostaje u istoj obitelji ravnih ploca i drzanja u ravnotezi.
- `HS-23` | skriptna_obitelj: `v05_z41-v05_z47` | druga_slojna_veza: `av03_01-av03_04` | presuda: `varijanta` | razlog: kvadratna greda zglobno ucvrscena i zadana sila F ostaje jos jedna momentna varijanta ravnoplosnog pritiska.
- `HS-30` | skriptna_obitelj: `v05_z41-v05_z44` | druga_slojna_veza: `av03_02-av03_04` | presuda: `varijanta` | razlog: minimalna udaljenost pregrade od zgloba i dalje koristi istu jezgru sile na ravnu pregradu i uvjeta otvaranja.
- `HS-37` | skriptna_obitelj: `v05_z39-v05_z46` | druga_slojna_veza: `nema bliskog para` | presuda: `jedinstven` | razlog: raspored tri ojacanja tako da svako nosi jednaku silu pretvara raspodjelu tlaka u pravi projektni zadatak konstrukcijskog dimenzioniranja.
- `HS-40` | skriptna_obitelj: `v05_z41-v05_z43` | druga_slojna_veza: `av03_02-av03_04` | presuda: `jedinstven` | razlog: drvena pregrada koja se moze prevrnuti uvodi tezinu materijala i kriterij prevrtanja, a ne samo izracun rezultante na plohu.

### U06 - Zakrivljene plohe i rastav sila

- `HS-3` | skriptna_obitelj: `v06_z49-v07_z02` | druga_slojna_veza: `av03_05-av03_10` | presuda: `varijanta` | razlog: valjkasti zatvarac koji treba pridrzavati ostaje tipicna obitelj cilindricnih i zakrivljenih zatvaraca.
- `HS-6` | skriptna_obitelj: `v06_z50-v06_z52` | druga_slojna_veza: `av03_05-av03_10` | presuda: `varijanta` | razlog: horizontalna sila na pregradu OA ostaje isti metodski rastav rezultante na zakrivljenoj geometriji.
- `HS-12` | skriptna_obitelj: `v06_z53-v06_z55` | druga_slojna_veza: `av03_08-av03_09` | presuda: `jedinstven` | razlog: poklopac oblika plasta stosca sa stlacenim zrakom otvara novu kombinaciju zakrivljene plohe i kompresibilnog zatvorenog volumena.
- `HS-15` | skriptna_obitelj: `v05_z39-v05_z48, v06_z50-v06_z52` | druga_slojna_veza: `nema bliskog para` | presuda: `jedinstven` | razlog: trazenje kuta za najdublje hvatiste i maksimalnu silu na ploci u cilindru uvodi analiticku optimizaciju koju nizi slojevi nemaju.
- `HS-17` | skriptna_obitelj: `v06_z50-v07_z02` | druga_slojna_veza: `av03_05-av03_10` | presuda: `varijanta` | razlog: polukuglasti zatvarac i trazenje smjera rezultante ostaju u istoj obitelji rastava sila na zakrivljenim plohama.
- `HS-21` | skriptna_obitelj: `v06_z49-v07_z02` | druga_slojna_veza: `av03_07-av03_10` | presuda: `varijanta` | razlog: kuglasti zatvarac s polugom i utegom ostaje konstrukcijska varijanta vec zatvorene obitelji zakrivljenih zatvaraca.
- `HS-24` | skriptna_obitelj: `v06_z49-v07_z02` | druga_slojna_veza: `av03_08-av03_09` | presuda: `jedinstven` | razlog: polukuglasti poklopac s utegom i dodatnom cijevi daje jaci inzenjerski scenarij otvaranja nego bazne skriptne scene.
- `HS-25` | skriptna_obitelj: `v06_z49-v07_z02` | druga_slojna_veza: `av03_08-av03_09` | presuda: `bliski_duplikat` | razlog: isti je urednicki mehanizam kao `HS-24`, samo s drugom trazenom velicinom i parametrima.
- `HS-26` | skriptna_obitelj: `v06_z50-v07_z02` | druga_slojna_veza: `av03_08-av03_10` | presuda: `jedinstven` | razlog: kombinirani poklopac polukrug plus ravna ploca trazi stvarni spoj `FH/FV` razmisljanja i ravnoplosnog doprinosa.
- `HS-27` | skriptna_obitelj: `v06_z49-v07_z02` | druga_slojna_veza: `av03_08-av03_10` | presuda: `varijanta` | razlog: gustoce utega za ravnotezu poklopca ostaju ista poluga-zatvarac obitelj bez dovoljno novog urednickog skoka.
- `HS-28` | skriptna_obitelj: `v06_z49, v07_z01-v07_z02` | druga_slojna_veza: `av03_07-av03_10` | presuda: `varijanta` | razlog: masa valjka za zatvaranje otvora spremnika ostaje jos jedna cilindricna zatvaracka varijanta.
- `HS-32` | skriptna_obitelj: `v06_z49-v06_z52` | druga_slojna_veza: `av03_08-av03_09` | presuda: `jedinstven` | razlog: reakcija u tocci A kao sila i moment uvodi konstrukcijski odgovor oslonca, a ne samo vanjsku silu pridrzavanja.
- `HS-33` | skriptna_obitelj: `v06_z52-v07_z02` | druga_slojna_veza: `av03_08-av03_10` | presuda: `jedinstven` | razlog: konusni cep na dnu posude s uljem i pretlakom uvodi novu geometriju zatvaraca koju bazni korpus nema.

### U07 - Uzgon, plivanje i stabilnost

- `HS-7` | skriptna_obitelj: `v06_z54` | druga_slojna_veza: `av03_12` | presuda: `jedinstven` | razlog: ponton koji se izvlaci na obalu bez prelijevanja vode otvara jasan prijelaz izmedu uzgona, geometrije i granicnog kontakta s obalom.
- `HS-8` | skriptna_obitelj: `v07_z01-v07_z02` | druga_slojna_veza: `av03_07-av03_10` | presuda: `varijanta` | razlog: masa valjka zglobno vezanog u A ostaje bliska obitelj polucilindricnih i cilindricnih plovnih zatvaraca.
- `HS-9` | skriptna_obitelj: `v02_z15, v03_z30` | druga_slojna_veza: `nema bliskog para` | presuda: `jedinstven` | razlog: valjak djelomicno ispunjen vodom i odredena izronjena visina daju novu kompozitnu plovnost koju nizi slojevi nemaju.
- `HS-10` | skriptna_obitelj: `v02_z15, v06_z55` | druga_slojna_veza: `nema bliskog para` | presuda: `jedinstven` | razlog: kuglica koja zapliva tek kad otvor dosegne odredeni promjer spaja uzgon i geometriju prolaza u novu rubnu scenu.
- `HS-11` | skriptna_obitelj: `v03_z30` | druga_slojna_veza: `av03_11` | presuda: `varijanta` | razlog: balon za nosenje tereta ostaje ista atmosferska uzgonska obitelj koju je drugi sloj vec otvorio.
- `HS-13` | skriptna_obitelj: `v06_z54` | druga_slojna_veza: `av03_12` | presuda: `jedinstven` | razlog: masa i polozaj tereta na pontonu za zadani nagib daju stvarni stabilnosni proracun, a ne samo osnovni uzgon.
- `HS-18` | skriptna_obitelj: `v07_z01-v07_z02, v06_z54-v06_z55` | druga_slojna_veza: `av03_07-av03_12` | presuda: `jedinstven` | razlog: polucilindricna greda zglobno vezana u vodi spaja uzgon, geometriju tijela i momentnu ravnotezu na nacin koji je novi.
- `HS-20` | skriptna_obitelj: `v06_z54-v07_z02` | druga_slojna_veza: `nema bliskog para` | presuda: `jedinstven` | razlog: djelomicno uronjena kocka s reakcijom i momentom u osloncu uvodi hibrid uzgona i oslonacke statike.
- `HS-22` | skriptna_obitelj: `v06_z54-v06_z55` | druga_slojna_veza: `av03_11-av03_12` | presuda: `jedinstven` | razlog: polukuglasta posuda s plutajucom kuglicom unutra daje slozenu kompozitnu plovnost koja nije pokrivena nizim slojevima.
- `HS-29` | skriptna_obitelj: `v02_z15, v03_z30` | druga_slojna_veza: `av03_11` | presuda: `varijanta` | razlog: kocka leda u Coca-Coli ostaje didakticki simpaticna, ali fizikalno jos uvijek bazna varijanta plivanja tijela u guscoj tekucini.
- `HS-31` | skriptna_obitelj: `v07_z01-v07_z02, v06_z54-v06_z55` | druga_slojna_veza: `av03_12` | presuda: `jedinstven` | razlog: gustoce kvadratne grede iz uvjeta ravnoteze spajaju plovnost, nagib i momentnu ravnotezu u cistu novu scenu.
- `HS-35` | skriptna_obitelj: `v02_z15, v06_z54` | druga_slojna_veza: `nema bliskog para` | presuda: `jedinstven` | razlog: topljenje leda s gustim umetkom zadrzava klasicnu ideju topljenja, ali dodaje skriveni teret i promjenu nivoa kao jasan rubni slucaj.
- `HS-36` | skriptna_obitelj: `v06_z54` | druga_slojna_veza: `nema bliskog para` | presuda: `jedinstven` | razlog: tonjenje broda s pukotinom i vremenom potapanja znatno siri uzgonski blok prema stvarnoj sigurnosti plovila.
- `HS-39` | skriptna_obitelj: `v06_z54` | druga_slojna_veza: `av03_12` | presuda: `jedinstven` | razlog: maksimalna tezina koju ponton-dizalica jos moze podizati daje jak stabilnosni i nosivostni scenarij kojeg nizi slojevi nemaju.

## Radni zakljucak za U03-U07 (HS)

Blok `HS` je najvredniji kao selektivna dopuna `U05-U07`, a ne kao monolitni uvoz. Ravne plohe su uglavnom `varijanta`, zakrivljene plohe daju nekoliko jakih `jedinstven` kandidata (`HS-12`, `HS-15`, `HS-24`, `HS-26`, `HS-32`, `HS-33`), a uzgon i stabilnost su najbogatiji dio bloka (`HS-7`, `HS-9`, `HS-10`, `HS-13`, `HS-18`, `HS-20`, `HS-22`, `HS-31`, `HS-35`, `HS-36`, `HS-39`). Cisti uredajni hidraulicki zapisi `HS-4`, `HS-5`, `HS-34` i `HS-38` najbolje ostaju `rezervni`, a `HS-25` je najjaci kandidat za unutarnju kompresiju kao `bliski_duplikat` prema `HS-24`.

## Prva operativna odluka nakon ove matrice

1. U glavnoj evidenciji treceg sloja mogu se dopisati `duplication_status` oznake za `HS-1` do `HS-40`.
2. Nakon toga `SAVAR sesija 1` ostaje otvoren samo jos na bloku `DA`.