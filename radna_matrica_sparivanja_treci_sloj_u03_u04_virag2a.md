# Radna matrica sparivanja treci sloj za U03-U04 (Virag 2.1-2.11)

## Svrha dokumenta

Ovo je deseti radni dokument za sparivanje treceg sloja. Fokus je samo na prvom statickom podbloku `Virag 2.1-2.11` iz izvora `zdravko-virag-mehanika-fluida.md`.

## Pravilo citanja ove matrice

1. Skripta ostaje kanonski prvi zapis.
2. Drugi sloj ostaje vec zatvoren prvi sloj dopune.
3. Ovaj podblok se cita kao prijelaz `U03-U04`: dio zadataka pripada klasicnoj hidrostatici i spojenim posudama, a dio relativnom mirovanju pri translaciji i rotaciji.
4. `jedinstven` znaci novu inverznu postavu, novu kombinaciju fluida i plina ili novu geometriju relativnog mirovanja koju nizi slojevi nemaju u tom obliku.
5. `varijanta` znaci da zadatak ostaje unutar vec zatvorenih obitelji tlakova u spremnicima, ubrzanih kolica i rotirajucih posuda.

## U03-U04 blok - postojeca jezgra

### Skriptna jezgra

- `v02_z19-v03_z29` za hidrostaticki tlak i manometriju
- `v03_z31-v04_z39` za relativno mirovanje pri translaciji i rotaciji

### Drugi sloj

- `av02_07-av02_16` za `U03`
- `av03_13-av03_16` za `U04`

## Treci sloj Virag 2.1-2.11 - preliminarna presuda

- `VG-02-01` | skriptna_obitelj: `v03_z25, v02_z19-v03_z29` | druga_slojna_veza: `av02_01-av02_06` | presuda: `varijanta` | razlog: spojene cilindricne posude sa stapom ostaju ista obitelj hidraulicko-hidrostatickog balansa i ravnoteze klipa.
- `VG-02-02` | skriptna_obitelj: `v03_z27-v03_z29` | druga_slojna_veza: `av02_12-av02_13` | presuda: `jedinstven` | razlog: boca s dovodom zraka, ispusnim otvorom i izotermickim ustaljenjem podtlaka daje bogatiju spregu hidrostatike i plinskog volumena nego nizi slojevi.
- `VG-02-03` | skriptna_obitelj: `v03_z31-v03_z33` | druga_slojna_veza: `av03_13` | presuda: `jedinstven` | razlog: poznati tlakovi u trima tockama i trazeno ubrzanje daju cisti inverzni translatorni problem koji baza nema ovako eksplicitno.
- `VG-02-04` | skriptna_obitelj: `v03_z32-v04_z34` | druga_slojna_veza: `av03_13` | presuda: `varijanta` | razlog: zadano ubrzanje kolica za trazeni tlak u tocki A ostaje klasicna varijanta relativnog mirovanja pri translaciji.
- `VG-02-05` | skriptna_obitelj: `v03_z27-v03_z29, v03_z31-v04_z34` | druga_slojna_veza: `av02_12-av02_13, av03_13` | presuda: `jedinstven` | razlog: dvofluidni spremnik u jednoliko ubrzanom gibanju uvodi spoj visefluidne hidrostatike i translacije koji je nizi sloj samo dodirnuo.
- `VG-02-06` | skriptna_obitelj: `v04_z34` | druga_slojna_veza: `av03_13` | presuda: `varijanta` | razlog: kolica na kosini i jednakost tlakova u dvjema tockama ostaju bliska bazna obitelj zadataka s ubrzanjem na kosini.
- `VG-02-07` | skriptna_obitelj: `v03_z32-v04_z34` | druga_slojna_veza: `av03_13` | presuda: `jedinstven` | razlog: izlijevanje fluida iz posude na ubrzanim kolicima uvodi granicni uvjet prelijevanja, a ne samo raspodjelu tlaka.
- `VG-02-08` | skriptna_obitelj: `v04_z37` | druga_slojna_veza: `av03_14-av03_16` | presuda: `varijanta` | razlog: dvokraka cjevcica u rotaciji ostaje tipicna rotacijska U-cijevna varijanta.
- `VG-02-09` | skriptna_obitelj: `v04_z35-v04_z38` | druga_slojna_veza: `av03_14-av03_16` | presuda: `varijanta` | razlog: rotacija cilindricne posude uz zadrzavanje dijela fluida ostaje ista rotacijska obitelj kao skriptni mokro-sukho dno scenarij.
- `VG-02-10` | skriptna_obitelj: `v04_z37-v04_z38` | druga_slojna_veza: `av03_14-av03_16` | presuda: `jedinstven` | razlog: U-cijev sa stapom i uvjetom jednakih visina pri rotaciji uvodi novu kombinaciju rotacije i mehanicke ravnoteze klipa.
- `VG-02-11` | skriptna_obitelj: `v04_z35-v04_z38` | druga_slojna_veza: `av03_14-av03_16` | presuda: `varijanta` | razlog: manometarski tlak u rotirajucoj cilindricnoj posudi ostaje standardna rotacijska raspodjela tlaka s bocnim krakom.

## Radni zakljucak za U03-U04 (Virag 2.1-2.11)

Prvi staticki podblok `Virag 2.1-2.11` je vrijedan, ali nije nosivi blok za glavni tok. Najjaci novi kandidati su `VG-02-02`, `VG-02-03`, `VG-02-05`, `VG-02-07` i `VG-02-10`, dok ostale stavke uglavnom ostaju `varijanta` vec zatvorene jezgre hidrostatike i relativnog mirovanja.

## Prva operativna odluka nakon ove matrice

1. U glavnoj evidenciji treceg sloja mogu se dopisati `duplication_status` oznake za `VG-02-01` do `VG-02-11`.
2. Nakon toga preostaje jos samo veliki staticki blok `VG-02-21` do `VG-02-89`.