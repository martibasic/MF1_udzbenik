# Radna matrica sparivanja za U04-U07

## Svrha dokumenta

Ovo je drugi radni dokument za sparivanje baznog sloja `skripta` i drugog sloja `530_540_150`. Ovdje se zatvara staticki blok `U04-U07` dovoljno precizno da se `duplication_status` moze vratiti u glavnu evidenciju.

## Pravilo citanja ove matrice

1. Skripta ostaje kanonski prvi zapis.
2. `jedinstven` znaci da drugi sloj donosi novu scenu ili vazan rubni slucaj koji skripta nema u toj formi.
3. `varijanta` znaci ista fizikalna obitelj, ali drukcija formulacija, geometrija ili trazena velicina.
4. `bliski_duplikat` znaci da drugi sloj vrlo vjerojatno ne treba ostati u istom glavnom toku zajedno sa skriptnim parom bez jasnog urednickog razloga.

## U04 - Relativno mirovanje fluida

### Skriptna jezgra

- `v03_z31-v03_z33`
- `v04_z34-v04_z39`

### Drugi sloj - preliminarna presuda

- `av03_13` | skriptna_obitelj: `v03_z31-v03_z32, v04_z34` | presuda: `varijanta` | razlog: isti translacijski blok, ali s drugim pitanjima i detaljnijim izvodom sile na pregradu.
- `av03_14` | skriptna_obitelj: `v04_z35-v04_z38` | presuda: `varijanta` | razlog: otvoreni rotirajuci spremnik je ista jezgra, ali ne isti zadatak.
- `av03_15` | skriptna_obitelj: `v04_z35-v04_z39` | presuda: `jedinstven` | razlog: sila na poklopac centrifugalnog kalupa donosi novu inzenjersku scenu unutar rotacije.
- `av03_16` | skriptna_obitelj: `v04_z35-v04_z38` | presuda: `jedinstven` | razlog: paraboloidni spremnik i potpuno praznjenje nisu pokriveni skriptnim baznim zadacima.

### Radni zakljucak za U04

U04 je dobar primjer dopune, ne zamjene. Drugi sloj ne potiskuje skriptu, ali korisno siri rotacijski podblok s dva scenarija koje skripta nema u istom obliku.

## U05 - Hidrostatske sile na ravne plohe

### Skriptna jezgra

- `v05_z37-v05_z48`

### Drugi sloj - preliminarna presuda

- `av03_01` | skriptna_obitelj: `v05_z41, v05_z45` | presuda: `bliski_duplikat` | razlog: pravokutni poklopac i hvatiste sile gotovo izravno ponavljaju bazni ravnoplosni obrazac.
- `av03_02` | skriptna_obitelj: `v05_z42, v05_z47` | presuda: `varijanta` | razlog: kosa kruzna ploha s trenjem prosiruje istu obitelj, ali ne mora biti glavni kanonski zapis.
- `av03_03` | skriptna_obitelj: `v05_z39-v05_z44` | presuda: `varijanta` | razlog: vise tekućina, pretlak i poluga daju slozeniju varijantu ravne plohe.
- `av03_04` | skriptna_obitelj: `v05_z42-v05_z48` | presuda: `varijanta` | razlog: dvoslojna tekućina i zadrzavanje zatvaraca su dodatna primjena iste jezgre.

### Radni zakljucak za U05

U05 vec ima jak skriptni temelj. Iz drugog sloja treba zadrzati barem jednu slozeniju varijantu s vise fluida ili pretlakom, ali ne i gomilati vise gotovo istih baznih ravnoplosnih zadataka.

## U06 - Zakrivljene plohe i rastav sila

### Skriptna jezgra

- `v06_z49-v06_z53`
- `v06_z54-v06_z55`
- `v07_z01-v07_z02` kao granicni par prema `U07`

### Drugi sloj - preliminarna presuda

- `av03_05` | skriptna_obitelj: `v06_z50-v06_z52` | presuda: `varijanta` | razlog: tezina zamišljenog stupca nad poluloptom jest ista jezgra zakrivljene plohe, ali s drugom geometrijom.
- `av03_06` | skriptna_obitelj: `v06_z50-v06_z52` | presuda: `varijanta` | razlog: poluloptasto dno spremnika ostaje unutar iste metode, ali nije preslika skriptnih zadataka.
- `av03_07` | skriptna_obitelj: `v07_z01-v07_z02` | presuda: `varijanta` | razlog: cilindar u otvoru i rastav na `Fx/Fz` vrlo je blizak krugu zadataka s cilindricnim zatvaracima.
- `av03_08` | skriptna_obitelj: `v06_z49-v06_z53` | presuda: `jedinstven` | razlog: vijke, dvije tekućine i kombinacija vlacne/smicne sile skripta nema u toj formi.
- `av03_09` | skriptna_obitelj: `v06_z49-v06_z53` | presuda: `jedinstven` | razlog: poluloptasti poklopac na kosoj podlozi s pretlakom donosi novi rubni slucaj.
- `av03_10` | skriptna_obitelj: `v06_z50-v07_z02` | presuda: `varijanta` | razlog: zakrivljeno okno i hvatiste rezultante su naprednija, ali jos uvijek ista obitelj.

### Radni zakljucak za U06

U06 je pravo prosirenje, ne cisti duplikat. Najvredniji novi ulazi su `av03_08` i `av03_09`, jer uvode konstrukcijski smisao zakrivljenih ploha, a ne samo cisti proračun rezultante.

## U07 - Uzgon, plivanje i stabilnost

### Skriptna jezgra

- `v02_z15`
- `v03_z30`
- `v06_z54-v06_z55`

### Drugi sloj - preliminarna presuda

- `av03_11` | skriptna_obitelj: `v03_z30, v06_z55` | presuda: `jedinstven` | razlog: uzgon u atmosferi i koristan teret balona otvaraju drugu fizikalnu scenu od skriptnih kapljevinskih primjera.
- `av03_12` | skriptna_obitelj: `v06_z54` | presuda: `varijanta` | razlog: stabilnost plivanja jest ista obitelj, ali s ozbiljnijom geometrijom i metacentricnim kriterijem.

### Radni zakljucak za U07

U07 iz drugog sloja ne treba puno, ali `av03_11` vrijedi cuvati kao jasan novi slucaj uzgona izvan vode, a `av03_12` kao ozbiljniju stabilnosnu varijantu.

## Prva operativna odluka nakon ove matrice

1. U glavnoj evidenciji drugog sloja sada se mogu dopisati `duplication_status` oznake za `av03_01-av03_16`.
2. Nakon toga staticki blok `U01-U07` postaje dovoljno stabilan da se prelazi na prvi dinamicki blok `U08-U10`.