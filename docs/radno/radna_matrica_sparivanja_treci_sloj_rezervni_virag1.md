# Radna matrica sparivanja treci sloj za rezervni blok (Virag 1.x)

## Svrha dokumenta

Ovo je deveti radni dokument za sparivanje treceg sloja. Fokus je samo na bloku `Virag 1.x` iz izvora `zdravko-virag-mehanika-fluida.md`.

## Pravilo citanja ove matrice

1. Skripta ostaje kanonski prvi zapis.
2. Drugi sloj ostaje vec zatvoren prvi sloj dopune.
3. Blok `Virag 1.x` se cita prvenstveno kao `REZERVNI`, jer je jezgra bloka dimenzijska analiza i teorija slicnosti, a ne glavni MF1 tok.
4. `rezervni` se koristi kad zadatak jest koristan, ali urednicki pripada dodatku o slicnosti ili rubnim aplikacijama, a ne glavnom nizu poglavlja.
5. `jedinstven` se koristi samo za one stavke koje i unutar rezervnog korpusa otvaraju novu primjenu koja bi se mogla kasnije selektivno izvuci.
6. `varijanta` i `bliski_duplikat` se koriste kad dimenzijska analiza samo prepakira vec postojecu nizu obitelj iz nizih slojeva.

## Rezervni blok - postojeca jezgra

### Skriptna i drugoslojna sidrista

- `v01_z06-v02_z18` za viskoznost, kapilarnost i smicajne modele
- `v09_z80-v10_z95` za pumpe, istjecanje i gubitke
- `v12_z111` za Peltonovu turbinu
- `DA-1-DA-15` kao vec zatvoren rezervni treceslojni most prema dimenzijskoj analizi
- `av07_01` i `av11_01-av11_06` kao vec zatvoren rezervni drugi sloj

## Treci sloj Virag 1.x - preliminarna presuda

- `VG-01-01` | skriptna_obitelj: `nema bliskog para` | druga_slojna_veza: `av11_01-av11_06` | presuda: `rezervni` | razlog: cisti zadatak o dimenzionalnoj nezavisnosti skupova je koristan za dodatak o slicnosti, ali nije dio glavnog toka udzbenika.
- `VG-01-02` | skriptna_obitelj: `nema bliskog para` | druga_slojna_veza: `av11_01-av11_06` | presuda: `rezervni` | razlog: Pi-teorem uz turbulentni rubni sloj i tangencijalno naprezanje ostaje teorijsko-metodski rezervni zapis.
- `VG-01-03` | skriptna_obitelj: `v05_z41-v05_z48` | druga_slojna_veza: `av03_01-av03_04` | presuda: `rezervni` | razlog: sila tlaka na uronjenu ravnu povrsinu ovdje se koristi samo kao podloga za Pi-teorem, pa je urednicki slabiji od izravnih hidrostatskih zadataka.
- `VG-01-04` | skriptna_obitelj: `nema bliskog para` | druga_slojna_veza: `av10_01-av10_04` | presuda: `rezervni` | razlog: otpor gibanja broda dolazi kao teorija slicnosti i bolje ostaje u prosirenom aplikacijskom korpusu.
- `VG-01-05` | skriptna_obitelj: `v01_z07-v01_z09` | druga_slojna_veza: `DA-4, DA-14` | presuda: `varijanta` | razlog: tonjenje tijela u fluidu ostaje bliska rezerva vec zatvorenoj obitelji Stokesova tonjenja i talozenja.
- `VG-01-06` | skriptna_obitelj: `v09_z80, v10_z86` | druga_slojna_veza: `av06_01-av06_02` | presuda: `varijanta` | razlog: maksimalna usisna visina pumpe ostaje dimenzijsko-analiticka varijanta vec postojecih pumpnih i kavitacijskih rubnih zadataka.
- `VG-01-07` | skriptna_obitelj: `v09_z80, v10_z86` | druga_slojna_veza: `av06_01-av06_02` | presuda: `bliski_duplikat` | razlog: zadatak samo ponavlja `VG-01-06` s drugim izborom dimenzionalno nezavisnog skupa.
- `VG-01-08` | skriptna_obitelj: `nema bliskog para` | druga_slojna_veza: `av10_01-av10_07` | presuda: `rezervni` | razlog: otpor u viskoznom stlacivom fluidu je vrijedan, ali rubno aerodinamicki i teorijsko-slicnosni zapis.
- `VG-01-09` | skriptna_obitelj: `v09_z81, v13_z121-v13_z124` | druga_slojna_veza: `av08_02-av08_03` | presuda: `jedinstven` | razlog: visina dobave pumpe iz Pi-teorema daje cisti most izmedu slicnosti i pumpne karakterizacije koji nizi slojevi nemaju ovako eksplicitno.
- `VG-01-10` | skriptna_obitelj: `v01_z06` | druga_slojna_veza: `av07_01` | presuda: `rezervni` | razlog: debljina granicnog sloja ostaje rubni teorijski zapis izvan glavne MF1 jezgre.
- `VG-01-11` | skriptna_obitelj: `v01_z08, v02_z10-v02_z11` | druga_slojna_veza: `nema bliskog para` | presuda: `rezervni` | razlog: snaga gubitka trenja u lezaju jest korisna aplikacija, ali urednicki ide u dodatni blok triboloskih i slicnosnih primjena.
- `VG-01-12` | skriptna_obitelj: `nema bliskog para` | druga_slojna_veza: `nema bliskog para` | presuda: `rezervni` | razlog: valovi na slobodnoj povrsini izlaze iz glavnog opsega ove knjige i bolje ostaju u prosirenom dodatku.
- `VG-01-13` | skriptna_obitelj: `nema bliskog para` | druga_slojna_veza: `av10_06-av10_07` | presuda: `rezervni` | razlog: uzgon projektila je aerodinamicki i slicnosni rubni slucaj, ne osnovni MF1 tok.
- `VG-01-14` | skriptna_obitelj: `v01_z06-v01_z09` | druga_slojna_veza: `nema bliskog para` | presuda: `jedinstven` | razlog: remen koji povlaci film fluida daje novu viskoznu transportnu scenu koju nizi slojevi nemaju.
- `VG-01-15` | skriptna_obitelj: `nema bliskog para` | druga_slojna_veza: `av10_01-av10_05` | presuda: `rezervni` | razlog: snaga vucenja glatke kugle ostaje teorijsko-slicnosna varijanta otpora opstrujavanja.
- `VG-01-16` | skriptna_obitelj: `v02_z10-v02_z11` | druga_slojna_veza: `nema bliskog para` | presuda: `varijanta` | razlog: moment izmedu koaksijalnih cilindara ostaje bliska viskozna rotacijska obitelj koju skripta vec ima.
- `VG-01-17` | skriptna_obitelj: `v09_z82` | druga_slojna_veza: `DA-6` | presuda: `jedinstven` | razlog: laminarni pad tlaka kroz cijev preko Pi-teorema daje cisti most izmedu viskoznog modela i cjevovodnog pada tlaka.
- `VG-01-18` | skriptna_obitelj: `v10_z89-v10_z94` | druga_slojna_veza: `nema bliskog para` | presuda: `jedinstven` | razlog: mjerna brana kao slicnosni zadatak uvodi protok preko preljeva koji nizi slojevi nemaju kao zasebnu jezgru.
- `VG-01-19` | skriptna_obitelj: `v01_z06, v09_z82` | druga_slojna_veza: `DA-6` | presuda: `jedinstven` | razlog: laminarni protok kroz trokutasti kanal daje novu nekruznu viskoznu geometriju u rezervnom korpusu.
- `VG-01-20` | skriptna_obitelj: `v12_z111` | druga_slojna_veza: `av11_01-av11_06` | presuda: `jedinstven` | razlog: Peltonova turbina kroz teoriju slicnosti daje vrijedan most prema turbinama koji baza nema u tom obliku.
- `VG-01-21` | skriptna_obitelj: `v09_z81` | druga_slojna_veza: `av08_02-av08_03` | presuda: `jedinstven` | razlog: razlika tlaka na ulazu i izlazu pumpe iz Pi-teorema otvara strojniji pumpni zapis od baznih gubitkovnih zadataka.
- `VG-01-22` | skriptna_obitelj: `nema bliskog para` | druga_slojna_veza: `av11_01-av11_06` | presuda: `rezervni` | razlog: kosi hitac je didakticki koristan za slicnost, ali nije fluidni zadatak i ne pripada glavnom korpusu.
- `VG-01-23` | skriptna_obitelj: `v10_z89, v11_z97` | druga_slojna_veza: `IS-1` | presuda: `jedinstven` | razlog: trenutno otvaranje dugog cjevovoda i bezdimenzijska tocka proracuna daju prijelazni nestiacionarni zapis koji nizim slojevima nedostaje.
- `VG-01-24` | skriptna_obitelj: `v11_z97, v10_z89` | druga_slojna_veza: `IS-1, IS-3` | presuda: `varijanta` | razlog: vrijeme praznjenja bacve kroz otvor na dnu ostaje slicnosna varijanta vec postojece obitelji praznjenja spremnika.
- `VG-01-25` | skriptna_obitelj: `nema bliskog para` | druga_slojna_veza: `av10_01-av10_07` | presuda: `rezervni` | razlog: sila na elipsoid s empirijskom eksponentnom ovisnoscu ostaje rubna teorijsko-opstrujavacka aplikacija.

## Radni zakljucak za rezervni blok (Virag 1.x)

`Virag 1.x` se zatvara kao izrazito rezervni blok. Vecina zadataka ostaje u dodatku o dimenzijskoj analizi i slicnosti, dok su najkorisniji izdvojeni mostovi `VG-01-09`, `VG-01-14`, `VG-01-17`, `VG-01-18`, `VG-01-20`, `VG-01-21` i `VG-01-23`. Najbliza unutarnja kompresija bloka je `VG-01-07` prema `VG-01-06`, a `VG-01-24` ostaje samo varijantni nastavak vec zatvorenog praznjenja spremnika.

## Prva operativna odluka nakon ove matrice

1. U glavnoj evidenciji treceg sloja mogu se dopisati `duplication_status` oznake za `VG-01-01` do `VG-01-25`.
2. Nakon toga Virag ostaje otvoren samo jos na statickom bloku `2.x`.