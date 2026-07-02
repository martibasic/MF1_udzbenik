# Radna matrica sparivanja treci sloj za U11-U12 (Virag 5.x)

## Svrha dokumenta

Ovo je osmi radni dokument za sparivanje treceg sloja. Fokus je samo na bloku `Virag 5.x` iz izvora `zdravko-virag-mehanika-fluida.md`.

## Pravilo citanja ove matrice

1. Skripta ostaje kanonski prvi zapis.
2. Drugi sloj ostaje vec zatvoren prvi sloj dopune.
3. Ovaj blok se cita primarno kao `U11`, uz rubni prijelaz prema `U12` kad zadaci prelaze s kontrole volumena na reakciju lopatice ili konstrukcije.
4. `jedinstven` znaci da novi zapis uvodi novu geometriju, novu inverznu postavu ili novu potpornu reakciju koju nizi slojevi nemaju u tom obliku.
5. `varijanta` znaci da zadatak ostaje u istoj obitelji koljena, mlaznice, racve ili mlaza na ploci, ali s drukcijim trazenim velicinama.
6. `bliski_duplikat` se koristi samo kad novi zapis gotovo izravno ponavlja vec zatvoreni kanonski primjer.

## U11-U12 prijelaz - postojeca jezgra

### Skriptna jezgra

- `v11_z97-v11_z103`
- rubni pomocni par `v12_z105-v12_z106`

### Drugi sloj

- `av05_01-av05_04`

## Treci sloj Virag 5.x - preliminarna presuda

### Mlaz, mlaznica i koljeno

- `VG-05-01` | skriptna_obitelj: `v11_z102` | druga_slojna_veza: `av05_02` | presuda: `varijanta` | razlog: ravninski mlaz na plocu AB ostaje ista obitelj sile mlaza na prepreku, ali s drukcijom geometrijom i protocnim zadavanjem.
- `VG-05-02` | skriptna_obitelj: `v11_z98` | druga_slojna_veza: `nema bliskog para` | presuda: `jedinstven` | razlog: obujam fluida u slobodnom mlazu izmedu dvaju presjeka daje cisti kontrolno-volumni zadatak koji baza nema.
- `VG-05-03` | skriptna_obitelj: `v12_z105` | druga_slojna_veza: `av05_04` | presuda: `varijanta` | razlog: horizontalna sila fluida na mlaznicu ostaje ista obitelj reakcije na mlaznicu i prirubnicu.
- `VG-05-04` | skriptna_obitelj: `v11_z100-v11_z101` | druga_slojna_veza: `av05_04` | presuda: `varijanta` | razlog: mlaznica s koljenom i rezultantna sila ostaju izravna varijanta skriptnog koljena cijevi.
- `VG-05-05` | skriptna_obitelj: `nema bliskog para` | druga_slojna_veza: `nema bliskog para` | presuda: `jedinstven` | razlog: prevrtanje spremnika zbog istjecanja uvodi jaku spregu kolicine gibanja i stabilnosti krutog tijela koju baza nema.
- `VG-05-06` | skriptna_obitelj: `v11_z100-v11_z101` | druga_slojna_veza: `nema bliskog para` | presuda: `jedinstven` | razlog: usporedba idealnog i viskoznog fluida na luku AB daje novu inzenjersku scenu reakcije cjevovoda.
- `VG-05-07` | skriptna_obitelj: `v12_z106` | druga_slojna_veza: `av05_04` | presuda: `jedinstven` | razlog: sile i moment na vijke u presjeku A-A otvaraju konstrukcijsku reakciju i momentnu ravnotezu koju nizi slojevi nemaju ovako jasno.
- `VG-05-08` | skriptna_obitelj: `v11_z98` | druga_slojna_veza: `nema bliskog para` | presuda: `jedinstven` | razlog: sudaranje dvaju osnosimetricnih mlazova je nova osnovna scena promjene kolicine gibanja.
- `VG-05-09` | skriptna_obitelj: `v11_z100-v11_z101` | druga_slojna_veza: `av05_04` | presuda: `varijanta` | razlog: sila fluida na koljeno u horizontalnoj ravnini ostaje tipicna koljenasta varijanta.
- `VG-05-10` | skriptna_obitelj: `v11_z102, v12_z105-v12_z106` | druga_slojna_veza: `av05_04` | presuda: `jedinstven` | razlog: iz sile na plocu vraca se na silu na vijke, protok i pretlak, pa zadatak postaje jaci inverzni spoj vise nepoznanica.
- `VG-05-11` | skriptna_obitelj: `v12_z105` | druga_slojna_veza: `av05_04` | presuda: `varijanta` | razlog: sila u vijcima mlaznice nakon otvaranja izlaza ostaje u istoj obitelji kao reakcije na mlaznicu i prirubnicu.
- `VG-05-12` | skriptna_obitelj: `v12_z105` | druga_slojna_veza: `av05_04` | presuda: `varijanta` | razlog: divergentna mlaznica i rezultantna sila jos su jedna izvedba istog reakcijskog bloka.
- `VG-05-14` | skriptna_obitelj: `v12_z105-v12_z106` | druga_slojna_veza: `av05_04` | presuda: `varijanta` | razlog: sila u vijcima mlaznice pricvrscene za postolje ostaje bliska konstrukcijska varijanta prethodnih mlaznickih zadataka.
- `VG-05-22` | skriptna_obitelj: `v11_z102` | druga_slojna_veza: `av05_02` | presuda: `bliski_duplikat` | razlog: ravninski mlaz na plocu AB najizravnije konkurira skriptnom mlazu na plocu i vec zatvorenom drugom sloju.

### Racve i visegrane kontrole volumena

- `VG-05-13` | skriptna_obitelj: `v11_z100-v11_z101` | druga_slojna_veza: `av05_01` | presuda: `varijanta` | razlog: simetricna racva pri otvorenom izlazu ostaje ista obitelj sila na odvojak i promjene kolicine gibanja.
- `VG-05-15` | skriptna_obitelj: `v11_z100-v11_z101` | druga_slojna_veza: `av05_01` | presuda: `varijanta` | razlog: rezultantna sila na racvu i kut rezultante ostaju u istoj obitelji trokrakog odvojka.
- `VG-05-16` | skriptna_obitelj: `v11_z100-v11_z101` | druga_slojna_veza: `av05_01` | presuda: `varijanta` | razlog: zadani odnos protoka u racvi i trazena sila jesu jos jedna izvedba vec zatvorenog granatog bloka.
- `VG-05-17` | skriptna_obitelj: `v11_z100-v11_z101` | druga_slojna_veza: `av05_01` | presuda: `jedinstven` | razlog: uvjet `F_x = 0` i trazena komponenta `F_y` daju inverzni silovni zadatak koji baza nema u tom obliku.
- `VG-05-18` | skriptna_obitelj: `v11_z100-v11_z101` | druga_slojna_veza: `av05_01` | presuda: `varijanta` | razlog: racva ABC s podijeljenim protocima ostaje cista varijanta iste granate obitelji.
- `VG-05-19` | skriptna_obitelj: `v11_z100-v11_z101` | druga_slojna_veza: `av05_01` | presuda: `varijanta` | razlog: poznati pretlak u jednom presjeku racve i rezultantna sila ostaju u istoj metodskoj obitelji.
- `VG-05-20` | skriptna_obitelj: `v11_z100-v11_z101` | druga_slojna_veza: `av05_01` | presuda: `jedinstven` | razlog: istodobno trazenje protoka i obje komponente sile na racvu daje jaci, visekoracni inverzni zadatak od bazne jezgre.
- `VG-05-21` | skriptna_obitelj: `v11_z100-v11_z101` | druga_slojna_veza: `av05_01` | presuda: `varijanta` | razlog: racva s poznatim manometarskim tlakom u presjeku B ostaje jos jedna bliska varijanta granate kontrole volumena.

### Lopatice i prijelaz prema U12

- `VG-05-23` | skriptna_obitelj: `v11_z102, v12_z105` | druga_slojna_veza: `nema bliskog para` | presuda: `jedinstven` | razlog: sila fluida na nepomicnu lopaticu otvara prijelaz iz ravne ploce prema geometriji lopatice.
- `VG-05-24` | skriptna_obitelj: `v11_z102, v12_z105` | druga_slojna_veza: `nema bliskog para` | presuda: `jedinstven` | razlog: lopatica s optimumom odnosa `Q1/Q` uvodi optimizacijski problem kakav nizi slojevi nemaju.
- `VG-05-25` | skriptna_obitelj: `v11_z102` | druga_slojna_veza: `nema bliskog para` | presuda: `jedinstven` | razlog: protok mlaza koji drzi okretljivu plocu u ravnotezi daje novu spregu mlaza i krutog tijela.
- `VG-05-26` | skriptna_obitelj: `v12_z106` | druga_slojna_veza: `nema bliskog para` | presuda: `jedinstven` | razlog: komponente sile i moment reakcije na ukljestenu lopaticu daju jasan prijelaz prema konstrukcijskom opterecenju lopatica.

## Radni zakljucak za U11-U12 (Virag 5.x)

Blok `Virag 5.x` je vrijedan, ali nije za nekriticni masovni uvoz. Najveci broj zadataka o racvama, koljenima i mlaznicama ostaje `varijanta` vec zatvorenih obitelji, dok stvarni novi kandidati dolaze iz inverznih i reakcijskih scena poput `VG-05-02`, `VG-05-05`, `VG-05-06`, `VG-05-07`, `VG-05-08`, `VG-05-10`, `VG-05-17`, `VG-05-20` te prijelaznog lopaticnog niza `VG-05-23` do `VG-05-26`. Najblizi duplikacijski sudar u bloku je `VG-05-22` prema kanonskom mlazu na plocu.

## Prva operativna odluka nakon ove matrice

1. U glavnoj evidenciji treceg sloja mogu se dopisati `duplication_status` oznake za `VG-05-01` do `VG-05-26`.
2. Nakon toga preostaje otvoriti jos `Virag 2.x` kao najvecu preostalu staticku cjelinu iz tekstualno citljivog korpusa.