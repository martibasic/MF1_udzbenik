# Radna matrica sparivanja treci sloj za U09-U10 (BJ)

## Svrha dokumenta

Ovo je drugi radni dokument za sparivanje treceg sloja s vec zatvorenim slojevima u dinamickom bloku `U09-U10`. Fokus je samo na bloku `BJ` iz izvora `SAVAR_sesija2_RM_Bernoulli_Istjecanje_Cjevovod.md`.

## Pravilo citanja ove matrice

1. Skripta ostaje kanonski prvi zapis.
2. Drugi sloj ostaje vec zatvoren prvi sloj dopune.
3. `jedinstven` znaci da treci sloj donosi novu scenu, model ili inzenjersku postavu koju nizi slojevi nemaju u tom obliku.
4. `varijanta` znaci da zadatak ostaje u istoj Bernoulli/istjecanje obitelji, ali s drukcijim uredajem, geometrijom ili trazenom velicinom.
5. `bliski_duplikat` znaci da bi zadatak vrlo vjerojatno konkurirao za isto mjesto kao vec postojeci zapis iz istog ili viseg sloja.

## U09 - Bernoullijeva jednadzba idealnog fluida

### Postojeca jezgra

- skripta: `v09_z76-v09_z79`
- drugi sloj: `av04_04`

### Treci sloj BJ - preliminarna presuda

- `BJ-1` | skriptna_obitelj: `v10_z92, v10_z94` | druga_slojna_veza: `av04_04` | presuda: `varijanta` | razlog: Venturijeva cijev s Hg manometrom ostaje klasicna Bernoullijeva mjerna scena, ali nije ista postava kao skriptni Venturi s podizanjem tekucine.
- `BJ-2` | skriptna_obitelj: `nema bliskog para` | druga_slojna_veza: `nema bliskog para` | presuda: `jedinstven` | razlog: spustanje cilindricne kape uz idealno brtvljenje uvodi neuobicajenu inverznu Bernoullijevu primjenu koju nizi slojevi nemaju.
- `BJ-3` | skriptna_obitelj: `v10_z94` | druga_slojna_veza: `av04_04` | presuda: `jedinstven` | razlog: venturimetar pricvrscen na camac kao uredaj za crpljenje vode donosi novu i vrlo prepoznatljivu primjenu podtlaka u suzenju.
- `BJ-4` | skriptna_obitelj: `nema bliskog para` | druga_slojna_veza: `nema bliskog para` | presuda: `jedinstven` | razlog: razgranati spremnik s izotermnom kompresijom zraka prosiruje idealni Bernoulli prema slozenijem sustavu s vise nepoznatih nivoa.
- `BJ-5` | skriptna_obitelj: `nema bliskog para` | druga_slojna_veza: `nema bliskog para` | presuda: `jedinstven` | razlog: odredjivanje smjera strujanja i protoka izmedu tri rezervoara daje novu mrežnu scenu izmedu cistog Bernoullija i cjevovodnog razmisljanja.
- `BJ-6` | skriptna_obitelj: `nema bliskog para` | druga_slojna_veza: `nema bliskog para` | presuda: `jedinstven` | razlog: rezervoari s izotermnom kompresijom i trazenim nivoom `x` nisu pokriveni baznim korpusom.
- `BJ-7` | skriptna_obitelj: `v10_z89` | druga_slojna_veza: `nema bliskog para` | presuda: `varijanta` | razlog: stacionarni nivo u spremniku s gornjim i donjim izlazom prirodno se naslanja na skriptni obrazac istjecanja iz velikog spremnika.
- `BJ-8` | skriptna_obitelj: `v09_z76-v09_z79` | druga_slojna_veza: `nema bliskog para` | presuda: `jedinstven` | razlog: klepsidra kao vodeni sat daje novu dizajnersku Bernoullijevu primjenu, a ne samo standardni proracun brzine ili tlaka.
- `BJ-9` | skriptna_obitelj: `v10_z95` | druga_slojna_veza: `av08_03` | presuda: `jedinstven` | razlog: projektiranje promjera za stalnu razinu u meduspremniku jest prijelazna scena prema `U13`, ali nije preslika skriptnih ili drugoslojnih zapisa.
- `BJ-10` | skriptna_obitelj: `v10_z89-v10_z91` | druga_slojna_veza: `nema bliskog para` | presuda: `jedinstven` | razlog: raspodjela obujma iz gornjeg u tri donja spremnika uvodi vise ishoda iz jednog istjecanja, sto skripta nema u tom obliku.
- `BJ-11` | skriptna_obitelj: `v10_z95` | druga_slojna_veza: `av08_03` | presuda: `varijanta` | razlog: razgranati sustav vise spremnika pripada istoj prijelaznoj obitelji kao slozeniji razvodni zadaci, ali s idealnim fluidom i bez gubitaka.
- `BJ-12` | skriptna_obitelj: `v10_z95` | druga_slojna_veza: `av08_03` | presuda: `varijanta` | razlog: odredjivanje otvora za jednake protoke ostaje ista razvodna obitelj, ali s drugacijim dizajnerskim izlazom.
- `BJ-13` | skriptna_obitelj: `BJ-4` | druga_slojna_veza: `nema bliskog para` | presuda: `bliski_duplikat` | razlog: to je prakticno ista razgranata postava kao `BJ-4`, samo s drugim protocnim parametrima i bez dovoljno nove urednicke vrijednosti za glavni tok.
- `BJ-14` | skriptna_obitelj: `v09_z78-v09_z79` | druga_slojna_veza: `av04_04` | presuda: `varijanta` | razlog: difuzor na izlazu spremnika ostaje cista Bernoullijeva geometrijska varijanta na temu konfuzor-difuzor promjene energije i tlaka.

### Radni zakljucak za U09-U10 (BJ)

Blok `BJ` je vrijedan kao selektivna dopuna, ali ne treba ga unositi cijelog u glavni tok. Najjaci novi kandidati su `BJ-2`, `BJ-3`, `BJ-4`, `BJ-5`, `BJ-6`, `BJ-8`, `BJ-9` i `BJ-10`, dok je `BJ-13` zasad najbolji kandidat za rezanje kao bliski duplikat `BJ-4`.

## Prva operativna odluka nakon ove matrice

1. U glavnoj evidenciji treceg sloja mogu se dopisati `duplication_status` oznake za `BJ-1` do `BJ-14`.
2. Nakon toga isti obrazac sparivanja moze se nastaviti na `IS` i `CV`, ili paralelno na `Virag 7.x` za `U13`.