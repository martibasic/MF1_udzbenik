# Radna matrica sparivanja za U08-U10

## Svrha dokumenta

Ovo je treci radni dokument za sparivanje baznog sloja `skripta` i drugog sloja `530_540_150`. Njime se zatvara prvi dinamicki blok `U08-U10` dovoljno precizno da se `duplication_status` vrati u glavnu evidenciju.

## Pravilo citanja ove matrice

1. Skripta ostaje kanonski prvi zapis.
2. `jedinstven` znaci da drugi sloj donosi novu scenu, poseban model ili vazan rubni slucaj koji skripta nema u toj formi.
3. `varijanta` znaci ista fizikalna obitelj, ali drukcija formulacija ili drukciji operativni scenarij.
4. `bliski_duplikat` se koristi samo kada bi dva zadatka vrlo vjerojatno konkurirala za isto mjesto u glavnom toku poglavlja.

## U08 - Kontrolni volumen i kontinuitet

### Skriptna jezgra

- `v08_z70-v08_z75`

### Drugi sloj - preliminarna presuda

- `av04_01` | skriptna_obitelj: `nema bliskog para` | presuda: `jedinstven` | razlog: raketni motor i maseni gubitak uvode kontrolni volumen za stlacivi plin, sto skripta nema u tom obliku.
- `av04_02` | skriptna_obitelj: `nema bliskog para` | presuda: `jedinstven` | razlog: protok kroz zracnost izmedu ploca daje drugu geometriju kontinuiteta od skriptnih spremnika i difuzora.
- `av04_03` | skriptna_obitelj: `v08_z71-v08_z73` | presuda: `varijanta` | razlog: spremnik s vise dotoka i jednim istokom ostaje ista kontinuitetska obitelj, ali s drugim numerickim scenarijem.

### Radni zakljucak za U08

U08 iz drugog sloja stvarno dobiva dva nova tipa scene, ne samo paralelne racunske primjere. Zato ovdje drugi sloj vrijedi kao pravo prosirenje baznog korpusa.

## U09 - Bernoullijeva jednadzba idealnog fluida

### Skriptna jezgra

- `v09_z76-v09_z79`

### Drugi sloj - preliminarna presuda

- `av04_04` | skriptna_obitelj: `v09_z78-v09_z79` | presuda: `jedinstven` | razlog: rasplinjac i usis goriva preko podtlaka u suzenju daju klasicnu Bernoullijevu primjenu koju skripta nema kao zasebnu baznu scenu.

### Radni zakljucak za U09

U09 je kraci skriptni blok pa mu `av04_04` dobro dodaje prepoznatljiv i didakticki jak primjer bez gubitaka.

## U10 - Realni Bernoulli i gubici

### Skriptna jezgra

- `v09_z80-v09_z85`
- `v10_z86-v10_z95`

### Drugi sloj - preliminarna presuda

- `av06_01` | skriptna_obitelj: `v09_z85, v10_z86, v10_z89` | presuda: `varijanta` | razlog: kavitacija na preljevu ostaje u istoj obitelji pada tlaka i ogranicenja strujanja, ali s drugom geometrijom.
- `av06_02` | skriptna_obitelj: `v09_z80-v09_z85` | presuda: `varijanta` | razlog: najveca smjestajna visina crpke bez kavitacije prirodno dopunjuje skriptni blok usisa i kavitacije.
- `av08_02` | skriptna_obitelj: `v09_z81-v10_z88` | presuda: `varijanta` | razlog: pumpa, razlika energija i gubici su ista jezgra, ali sa znatno eksplicitnijim razdvajanjem usisne i tlacne dionice.
- `av08_03` | skriptna_obitelj: `v09_z81, v10_z95` | presuda: `jedinstven` | razlog: mreza s dva potrosaca i izbor nepovoljnijeg kraka prelazi baznu skriptnu jezgru i otvara prijelaz prema cjevovodnom razmisljanju.

### Radni zakljucak za U10

U10 je uglavnom varijantno prosirenje, ali `av08_03` vrijedi cuvati kao jaci prijelazni zadatak izmedu realnog Bernoullija i kasnijih cjevovodnih mreza.

## Prva operativna odluka nakon ove matrice

1. U glavnoj evidenciji drugog sloja sada se mogu dopisati `duplication_status` oznake za `av04_01-av04_04`, `av06_01-av06_02` i `av08_02-av08_03`.
2. Nakon toga ce `U01-U10` biti dovoljno stabilan da se otvori `U11-U13` i rezervni korpus.