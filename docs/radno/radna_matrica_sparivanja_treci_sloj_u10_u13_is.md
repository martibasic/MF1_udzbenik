# Radna matrica sparivanja treci sloj za U10-U13 (IS)

## Svrha dokumenta

Ovo je treci radni dokument za sparivanje treceg sloja u prijelaznom bloku izmedu `U10` i `U13`. Fokus je samo na bloku `IS` iz izvora `SAVAR_sesija2_RM_Bernoulli_Istjecanje_Cjevovod.md`.

## Pravilo citanja ove matrice

1. Skripta ostaje kanonski prvi zapis.
2. Drugi sloj ostaje vec zatvoren prvi sloj dopune.
3. `jedinstven` znaci da treci sloj donosi novu geometriju, rubni uvjet ili tranzijentni scenarij koji nizi slojevi nemaju u tom obliku.
4. `varijanta` znaci da zadatak ostaje u istoj obitelji istjecanja, praznjenja ili energetskog priblizenja, ali s drukcijim spremnikom ili trazenom velicinom.
5. `bliski_duplikat` se koristi samo kad novi zapis konkurira za isto mjesto bez dovoljno nove urednicke vrijednosti.

## U10-U13 prijelaz - Istjecanje i praznjenje spremnika

### Postojeca jezgra

- skripta: `v10_z89-v10_z95`, uz rubni pomocni par `v11_z97`
- drugi sloj: `av06_01-av06_02`, `av08_02-av08_03`

### Treci sloj IS - preliminarna presuda

- `IS-1` | skriptna_obitelj: `v10_z89, v11_z97` | druga_slojna_veza: `nema bliskog para` | presuda: `varijanta` | razlog: vrijeme praznjenja cilindricne posude kroz otvor na plastu ili dnu ostaje bazna obitelj kvazistacionarnog istjecanja.
- `IS-2` | skriptna_obitelj: `nema bliskog para` | druga_slojna_veza: `nema bliskog para` | presuda: `jedinstven` | razlog: izjednacavanje razine u dva kuglasta spremnika daje novu tranzijentnu scenu s dvama spremnicima i promjenjivom geometrijom.
- `IS-3` | skriptna_obitelj: `v10_z89, v11_z97` | druga_slojna_veza: `nema bliskog para` | presuda: `varijanta` | razlog: praznjenje lijevka ostaje ista obitelj vremena praznjenja, ali s drugacijom geometrijom spremnika.
- `IS-4` | skriptna_obitelj: `nema bliskog para` | druga_slojna_veza: `nema bliskog para` | presuda: `jedinstven` | razlog: ukupno vrijeme punjenja posude kroz ventil nije bazni skriptni motiv i didakticki dobro nadopunjuje praznjenje obratnim procesom.
- `IS-5` | skriptna_obitelj: `nema bliskog para` | druga_slojna_veza: `nema bliskog para` | presuda: `jedinstven` | razlog: plutajuci valjak uvodi gibajucu granicu i spregu uzgona s praznjenjem spremnika.
- `IS-6` | skriptna_obitelj: `v10_z89` | druga_slojna_veza: `nema bliskog para` | presuda: `varijanta` | razlog: cilindricni spremnik s Hg manometrom i efektivnim koeficijentom brzine ostaje ista praznjenjska obitelj, ali s dodatnim mjernim slojem.
- `IS-7` | skriptna_obitelj: `v10_z89-v10_z91` | druga_slojna_veza: `nema bliskog para` | presuda: `jedinstven` | razlog: zatvoreni pravokutni spremnik s odusnom cijevi uvodi novu kombinaciju istjecanja i rada zraka u spremniku.
- `IS-8` | skriptna_obitelj: `v10_z89, v10_z88-v10_z93` | druga_slojna_veza: `av08_02-av08_03` | presuda: `jedinstven` | razlog: paraboloidni spremnik s realnim gubicima i konstantnim `lambda` daje jak prijelaz izmedu istjecanja i cjevovodnog razmisljanja.
- `IS-9` | skriptna_obitelj: `nema bliskog para` | druga_slojna_veza: `nema bliskog para` | presuda: `jedinstven` | razlog: potapanje posude zbog kompresije zraka i istjecanja kroz mali otvor je izrazito rubni i originalan tranzijentni problem.

### Radni zakljucak za U10-U13 (IS)

Blok `IS` nije dobar kandidat za masovno uvlacenje u glavni tok, ali sadrzi nekoliko vrijednih prijelaznih scenarija. Najjaci kandidati za zadrzavanje su `IS-2`, `IS-4`, `IS-5`, `IS-7`, `IS-8` i `IS-9`, dok `IS-1`, `IS-3` i `IS-6` vise djeluju kao korisne varijante postojece obitelji praznjenja.

## Prva operativna odluka nakon ove matrice

1. U glavnoj evidenciji treceg sloja mogu se dopisati `duplication_status` oznake za `IS-1` do `IS-9`.
2. Nakon toga isti obrazac sparivanja moze se nastaviti na `CV` ili na `Virag 7.x` kao cisti `U13` blok.