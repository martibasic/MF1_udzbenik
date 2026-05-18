# Radna matrica sparivanja treci sloj za U04 (RM)

## Svrha dokumenta

Ovo je prvi radni dokument za sparivanje treceg sloja s vec zatvorenim slojevima u poglavlju `U04`. Fokus je samo na bloku `RM` iz izvora `SAVAR_sesija2_RM_Bernoulli_Istjecanje_Cjevovod.md`.

## Pravilo citanja ove matrice

1. Skripta ostaje kanonski prvi zapis.
2. Drugi sloj ostaje prvi filtrirani sloj dopune koji je vec zatvoren.
3. `jedinstven` znaci da treci sloj donosi novu scenu, geometriju ili pitanje koje ni skripta ni drugi sloj nemaju u istom obliku.
4. `varijanta` znaci da zadatak ostaje u istoj fizikalnoj obitelji, ali s drukcijim trazenim velicinama, geometrijom ili rubnim uvjetom.
5. `bliski_duplikat` znaci da je urednicki tesko opravdati jos jedan gotovo isti zapis u glavnom toku.

## U04 - Relativno mirovanje fluida

### Postojeca jezgra

- skripta: `v03_z31-v03_z33`, `v04_z34-v04_z39`
- drugi sloj: `av03_13-av03_16`

### Treci sloj RM - preliminarna presuda

- `RM-1` | skriptna_obitelj: `v04_z35-v04_z38` | druga_slojna_veza: `av03_14-av03_16` | presuda: `jedinstven` | razlog: plivajuci drveni valjak u rotirajucem spremniku uvodi spoj relativnog mirovanja i uzgona koji kanonska jezgra nema u toj formi.
- `RM-2` | skriptna_obitelj: `v04_z37, v04_z39` | druga_slojna_veza: `av03_14` | presuda: `varijanta` | razlog: dva fluida i tlak u tocki A ostaju ista rotacijska obitelj, ali s drukcijim trazenim izlazom.
- `RM-3` | skriptna_obitelj: `v04_z35-v04_z38` | druga_slojna_veza: `av03_15` | presuda: `varijanta` | razlog: sila na poklopac nakon rotacije pripada istoj centrifugalnoj obitelji kao vec postojeci zadaci s poklopcem.
- `RM-4` | skriptna_obitelj: `v04_z35-v04_z38` | druga_slojna_veza: `av03_16` | presuda: `jedinstven` | razlog: polukuglasta posuda i plivajuci valjak daju novu geometriju i novi spoj rotacije i uzgona.
- `RM-5` | skriptna_obitelj: `v04_z35-v04_z36` | druga_slojna_veza: `av03_14` | presuda: `varijanta` | razlog: lokalni tlak na plastu rotirajuce posude ostaje bazni rotacijski obrazac bez bitno nove scene.
- `RM-6` | skriptna_obitelj: `v03_z31-v03_z32, v04_z34` | druga_slojna_veza: `av03_13` | presuda: `varijanta` | razlog: sila na pregradu u ubrzanim kolicima prosiruje isti translacijski podblok koji je vec dobro pokriven.
- `RM-7` | skriptna_obitelj: `v04_z37` | druga_slojna_veza: `av03_14` | presuda: `varijanta` | razlog: visine u vise cjevcica nakon rotacije ostaju ista obitelj raspodjele tlaka po radijusu.
- `RM-8` | skriptna_obitelj: `v03_z31, v04_z34` | druga_slojna_veza: `av03_13` | presuda: `varijanta` | razlog: maksimalna akceleracija prije prelijevanja jest standardna translacijska varijanta bez novog metodskog jezgra.
- `RM-9` | skriptna_obitelj: `v04_z35-v04_z38` | druga_slojna_veza: `av03_15` | presuda: `varijanta` | razlog: otvaranje poklopca rotacijom ostaje blisko povezano sa silom na poklopac u drugom sloju.
- `RM-10` | skriptna_obitelj: `v04_z34` | druga_slojna_veza: `av03_13` | presuda: `varijanta` | razlog: sila na straznju stijenu kolica na kosini mijenja geometriju, ali ne otvara novu fizikalnu obitelj.
- `RM-11` | skriptna_obitelj: `v03_z31-v03_z33` | druga_slojna_veza: `nema bliskog para` | presuda: `jedinstven` | razlog: trodimenzijski inverzni problem akceleracije iz prostornih razlika tlakova nije pokriven kanonskom jezgrom.
- `RM-12` | skriptna_obitelj: `v04_z35-v04_z39` | druga_slojna_veza: `nema bliskog para` | presuda: `jedinstven` | razlog: trazenje polozaja osi rotacije iz tlakova u kockastom spremniku uvodi drugu vrstu inverznog problema.
- `RM-13` | skriptna_obitelj: `v03_z31-v03_z32, v04_z34` | druga_slojna_veza: `av03_13, RM-6` | presuda: `bliski_duplikat` | razlog: to je prakticno ista pregrada-u-kolicima obitelj kao `RM-6`, samo s drugom ispunom i bez dovoljno nove urednicke vrijednosti.
- `RM-14` | skriptna_obitelj: `v04_z35-v04_z38` | druga_slojna_veza: `av03_16` | presuda: `jedinstven` | razlog: vertikalni stozac i tangencija slobodne povrsine na plast daju novu geometrijsku scenu rotacije.
- `RM-15` | skriptna_obitelj: `v04_z35-v04_z38` | druga_slojna_veza: `av03_15` | presuda: `varijanta` | razlog: podizanje kruznog poklopca pri rotaciji ostaje bliski konstrukcijski derivat vec postojece obitelji poklopaca.
- `RM-16` | skriptna_obitelj: `v04_z35-v04_z38` | druga_slojna_veza: `av03_15` | presuda: `jedinstven` | razlog: konusna posuda i kriterij trostruko vece sile u vijcima daju dovoljno specifican konstrukcijski rubni slucaj.

### Radni zakljucak za U04 (RM)

Blok `RM` ne potiskuje skriptu ni drugi sloj, ali je koristan kao treci sloj selektivne dopune. Najvredniji novi ulazi su `RM-1`, `RM-4`, `RM-11`, `RM-12`, `RM-14` i `RM-16`, dok je `RM-13` trenutno najbolji kandidat za rezanje ili rezervni status.

## Prva operativna odluka nakon ove matrice

1. U glavnoj evidenciji treceg sloja mogu se naknadno dopisati `duplication_status` oznake za `RM-1` do `RM-16`.
2. Nakon toga isti obrazac sparivanja moze se nastaviti na `BJ` i `CV`, ili paralelno na `Virag 7.x` za `U13`.