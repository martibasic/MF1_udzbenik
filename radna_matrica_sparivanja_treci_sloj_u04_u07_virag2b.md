# Radna matrica sparivanja treci sloj za U04-U07 (Virag 2.21-2.89)

## Svrha dokumenta

Ovo je jedanaesti radni dokument za sparivanje treceg sloja. Fokus je samo na velikom statickom bloku `Virag 2.21-2.89` iz izvora `zdravko-virag-mehanika-fluida.md`.

## Pravilo citanja ove matrice

1. Skripta ostaje kanonski prvi zapis.
2. Drugi sloj ostaje vec zatvoren prvi sloj dopune.
3. Ovaj blok se cita primarno kao `U05-U07`, uz manji rubni prijelaz prema `U04` i nekoliko uredajnih stavki koje je bolje ostaviti `rezervni`.
4. `jedinstven` znaci novu geometriju, novu kombinaciju pretlaka i hidrostatike, ili novu konstrukcijsku reakciju koju nizi slojevi nemaju u tom obliku.
5. `varijanta` znaci da zadatak ostaje u vec zatvorenoj obitelji ravnih ili zakrivljenih poklopaca, brana, plovaka i relativnog mirovanja.
6. `rezervni` se koristi kad se scena vise vraca na hidraulicke uredaje i stapne mehanizme nego na glavni staticki tok.
7. `bliski_duplikat` se koristi samo kad novi zapis gotovo ponavlja vec prisutnu urednicku poziciju.

## U04-U07 blok - postojeca jezgra

### Skriptna jezgra

- `v03_z31-v04_z39` za relativno mirovanje
- `v05_z37-v05_z48` za ravne plohe
- `v06_z49-v06_z55` i `v07_z01-v07_z02` za zakrivljene plohe i prijelaz prema uzgonu
- `v02_z15` i `v03_z30` za uzgon i mjerenje gustoce

### Drugi sloj

- `av03_01-av03_04` za `U05`
- `av03_05-av03_10` za `U06`
- `av03_11-av03_12` za `U07`
- `av03_13-av03_16` za `U04`

## Treci sloj Virag 2.21-2.89 - preliminarna presuda

### Rubni prijelazi i uredajni staticki zapisi

- `VG-02-21` | skriptna_obitelj: `v02_z15, v06_z55` | druga_slojna_veza: `av03_11-av03_12` | presuda: `jedinstven` | razlog: cep pridrzavan balonom na uzetu spaja hidrostatiku zatvaraca i uzgon u jedan nov urednicki scenarij.
- `VG-02-23` | skriptna_obitelj: `v02_z15, v06_z49-v07_z02` | druga_slojna_veza: `av03_11-av03_12` | presuda: `jedinstven` | razlog: valjkasti plovak koji otvara kruzni zatvarac daje pravi prijelaz izmedu plovnosti i zatvaracke mehanike.
- `VG-02-24` | skriptna_obitelj: `v01_z01-v01_z02, v03_z25` | druga_slojna_veza: `av02_01-av02_06` | presuda: `rezervni` | razlog: pretlak u gornjem cilindru za ravnotezu stapa urednicki vise pripada stapno-hidraulickom bloku nego glavnom nizu hidrostatickih sila.
- `VG-02-25` | skriptna_obitelj: `v01_z01-v01_z02, v03_z25` | druga_slojna_veza: `av02_01-av02_06` | presuda: `rezervni` | razlog: tlak u trecem spremniku za ravnotezu stapa ostaje ista uredajna stapna obitelj i ne treba ulaziti u glavni tok `U05-U07`.

### U05 - Hidrostatske sile na ravne plohe

- `VG-02-22` | skriptna_obitelj: `v05_z39-v05_z45` | druga_slojna_veza: `av03_01-av03_04` | presuda: `jedinstven` | razlog: horizontalni kruzni poklopac s pretlakom u spremniku i dodatnim manometarskim podacima daje bogatiji zatvoreni-sustav scenarij od bazne jezgre.
- `VG-02-26` | skriptna_obitelj: `v05_z39-v05_z48` | druga_slojna_veza: `av03_01-av03_04` | presuda: `jedinstven` | razlog: moment sile hidrostatskog tlaka na bocni kruzni poklopac u odnosu na teziste poklopca daje korisnu analiticku dopunu koja nije izravno prisutna u nizim slojevima.
- `VG-02-27` | skriptna_obitelj: `v05_z41-v05_z44` | druga_slojna_veza: `av03_02-av03_04` | presuda: `varijanta` | razlog: minimalna tezina poklopca za zatvorenost ostaje klasicna momentna varijanta zglobnog ravnog poklopca.
- `VG-02-28` | skriptna_obitelj: `v05_z41-v05_z44` | druga_slojna_veza: `av03_02-av03_04` | presuda: `varijanta` | razlog: podtlak pri otvaranju kruznog poklopca silom F ostaje ista ravnoplosna obitelj otvaranja i pridrzavanja.
- `VG-02-29` | skriptna_obitelj: `v05_z41-v05_z44` | druga_slojna_veza: `av03_02-av03_04` | presuda: `varijanta` | razlog: visina razine pri kojoj je zatvarac OA jos zatvoren ostaje standardna granicna verzija ravnoplosnog zatvaraca.
- `VG-02-30` | skriptna_obitelj: `v05_z41-v05_z44` | druga_slojna_veza: `av03_02-av03_04` | presuda: `varijanta` | razlog: vertikalna sila za drzanje zatvaraca na zatvorenom spremniku ostaje bliska obitelj ravnoplosne momentne ravnoteze.
- `VG-02-31` | skriptna_obitelj: `v05_z41-v05_z44` | druga_slojna_veza: `av03_02-av03_04` | presuda: `varijanta` | razlog: sila za drzanje poklopca jedinične sirine u tocki O ostaje tipicna varijanta iste geometrije.
- `VG-02-32` | skriptna_obitelj: `v05_z43-v05_z44` | druga_slojna_veza: `av03_02-av03_04` | presuda: `varijanta` | razlog: sila u lancu brane OB ostaje konstrukcijska varijanta ravne brane u ravnotezi.
- `VG-02-33` | skriptna_obitelj: `v05_z39-v05_z44` | druga_slojna_veza: `av03_01-av03_04` | presuda: `varijanta` | razlog: pretlak za zatvoren kruzni poklopac zglobno vezan u A ostaje jos jedna varijanta istog ravnoplosnog bloka.
- `VG-02-34` | skriptna_obitelj: `v05_z41-v05_z47` | druga_slojna_veza: `av03_01-av03_04` | presuda: `jedinstven` | razlog: zatvoreni prismaticni spremnik s podtlakom i trazenom rezultantom na stijenci ABCD uvodi dvostruki doprinos uniformnog i hidrostatickog tlaka.
- `VG-02-35` | skriptna_obitelj: `v05_z41-v05_z47` | druga_slojna_veza: `av03_01-av03_04` | presuda: `varijanta` | razlog: rezultantna sila na poklopac AB i njezino hvatiste ostaju osnovna ravnoplosna obitelj.
- `VG-02-36` | skriptna_obitelj: `v05_z41-v05_z47` | druga_slojna_veza: `av03_01-av03_04` | presuda: `varijanta` | razlog: pravokutni poklopac AO i udaljenost rezultante od brida A ostaju tipicna varijanta centra tlaka.
- `VG-02-37` | skriptna_obitelj: `v05_z42-v05_z47` | druga_slojna_veza: `av03_02-av03_04` | presuda: `varijanta` | razlog: moment potreban za drzanje poklopca u tocki O ostaje bliska operativna varijanta istog bloka.
- `VG-02-38` | skriptna_obitelj: `v05_z43-v05_z48` | druga_slojna_veza: `nema bliskog para` | presuda: `jedinstven` | razlog: uvjet nulne vertikalne sile na konstrukciju ABCD pa zatim pridrzna horizontalna sila daju projektni zadatak vise razine od baznih primjera.
- `VG-02-39` | skriptna_obitelj: `v05_z46-v05_z48` | druga_slojna_veza: `av03_02-av03_04` | presuda: `jedinstven` | razlog: trokutasti poklopac s trazenim pretlakom u tocki D uvodi zatvoreni sustav i uvjet otvaranja u novoj geometriji.
- `VG-02-40` | skriptna_obitelj: `v05_z41-v05_z44` | druga_slojna_veza: `av03_02-av03_04` | presuda: `varijanta` | razlog: sila za drzanje zanemarivo teskog poklopca ostaje osnovna varijanta zglobnog ravnog poklopca.
- `VG-02-42` | skriptna_obitelj: `v05_z43-v05_z48` | druga_slojna_veza: `nema bliskog para` | presuda: `jedinstven` | razlog: vertikalna sila u tocki C za ravnotezu konstrukcije OABC uvodi reakcijski, a ne samo rezultantni pogled na ravnu konstrukciju.
- `VG-02-43` | skriptna_obitelj: `v05_z43-v05_z48` | druga_slojna_veza: `av03_02-av03_04` | presuda: `varijanta` | razlog: pretlak za otvaranje brane u tocki O ostaje jos jedna momentna branska varijanta.
- `VG-02-44` | skriptna_obitelj: `v05_z41-v05_z48` | druga_slojna_veza: `nema bliskog para` | presuda: `jedinstven` | razlog: iako je naslov trunciran u trenutnom source-exportu, odgovor pokazuje da zadatak trazi silovni rastav na dvjema stijenkama potpuno ispunjene kvadratne prizme, sto donosi novu zatvoreno-spremnicku scenu.

### U04 - Relativno mirovanje

- `VG-02-46` | skriptna_obitelj: `v03_z32-v04_z34` | druga_slojna_veza: `av03_13` | presuda: `jedinstven` | razlog: sila za guranje otvorene posude tako da ostane tocno 75 posto vode uvodi prepoznatljiv rubni uvjet prelijevanja i preostalog volumena.
- `VG-02-47` | skriptna_obitelj: `v03_z32-v04_z34` | druga_slojna_veza: `av03_13` | presuda: `jedinstven` | razlog: istodobno trazenje preostalog obujma vode i ubrzanja kockastih kolica daje jaci inverzni zadatak od bazne jezgre.
- `VG-02-48` | skriptna_obitelj: `v04_z34-v04_z39` | druga_slojna_veza: `av03_13` | presuda: `jedinstven` | razlog: rezultantna sila na stijenku nakon istjecanja iz kolica povezuje relativno mirovanje s promijenjenom geometrijom slobodne povrsine.
- `VG-02-49` | skriptna_obitelj: `v04_z34` | druga_slojna_veza: `av03_13` | presuda: `varijanta` | razlog: akceleracija kolica niz kosinu i sila na prednju stijenku ostaju bliska varijanta poznate kosinske obitelji.
- `VG-02-50` | skriptna_obitelj: `v03_z31-v04_z39` | druga_slojna_veza: `av03_13` | presuda: `jedinstven` | razlog: nagib spremnika tako da slobodna povrsina bude okomita na AB, uz trazeno hvatiste i silu, daje bogatiji geometrijski uvjet od nizih slojeva.
- `VG-02-51` | skriptna_obitelj: `v04_z34` | druga_slojna_veza: `av03_13` | presuda: `varijanta` | razlog: sila fluida na dno kolica niz kosinu uz paralelnu slobodnu povrsinu ostaje standardna izvedba relativnog mirovanja na kosini.
- `VG-02-52` | skriptna_obitelj: `v04_z34-v04_z39` | druga_slojna_veza: `av03_13` | presuda: `jedinstven` | razlog: trazenje i smjera i iznosa ubrzanja, pa zatim sile na dno, daje puniji inverzni scenarij nego baza.
- `VG-02-53` | skriptna_obitelj: `v04_z35-v04_z38` | druga_slojna_veza: `av03_14-av03_16` | presuda: `jedinstven` | razlog: rezultirajuce sile na dno i poklopac rotirajuce posude prosiruju rotacijski blok sa silama na oba krajnja elementa konstrukcije.
- `VG-02-54` | skriptna_obitelj: `v06_z55, v03_z30` | druga_slojna_veza: `nema bliskog para` | presuda: `jedinstven` | razlog: potpuno uronjena cilindricna posuda sa stlacenim zrakom i trazenim silama na poklopac i dno uvodi spoj uzgona, kompresije zraka i raspodjele tlaka.

### U05-U07 prijelaz: ravne brane, uzgon i stabilnost

- `VG-02-55` | skriptna_obitelj: `v05_z43-v05_z48` | druga_slojna_veza: `av03_01-av03_04` | presuda: `jedinstven` | razlog: brana izmedu dvaju fluida iste gustoce daje obostrano opterecenje koje nizi slojevi nemaju kao zaseban zapis.
- `VG-02-56` | skriptna_obitelj: `v05_z43-v05_z48` | druga_slojna_veza: `av03_02-av03_04` | presuda: `varijanta` | razlog: visina fluida za ravnotezu masivne brane ostaje klasicna branska varijanta.
- `VG-02-57` | skriptna_obitelj: `v05_z43-v05_z48` | druga_slojna_veza: `nema bliskog para` | presuda: `jedinstven` | razlog: vertikalna sila potrebna za ravnotezu konstrukcije AB uvodi izravnu oslonacku reakciju na element bez vlastite tezine i volumena.
- `VG-02-58` | skriptna_obitelj: `v05_z43-v05_z48` | druga_slojna_veza: `av03_02-av03_04` | presuda: `varijanta` | razlog: ukupna masa brane i utega za ravnotezu ostaje u istoj obitelji brana s dodatnim opterecenjem.
- `VG-02-59` | skriptna_obitelj: `v05_z43-v05_z48` | druga_slojna_veza: `av03_02-av03_04` | presuda: `varijanta` | razlog: masa utega za zatvoren poklopac OA ostaje bliska operativna varijanta poklopca s utezima.
- `VG-02-60` | skriptna_obitelj: `v05_z43-v05_z48` | druga_slojna_veza: `av03_02-av03_04` | presuda: `varijanta` | razlog: horizontalna sila za ravnotezu zglobnog zatvaraca ostaje u standardnoj ravnoplosnoj obitelji.
- `VG-02-61` | skriptna_obitelj: `v05_z43-v05_z48` | druga_slojna_veza: `av03_02-av03_04` | presuda: `varijanta` | razlog: visina fluida za zadanu silu drzanja brane AO ostaje jos jedna uvjetna varijanta brane u ravnotezi.
- `VG-02-62` | skriptna_obitelj: `v05_z42-v05_z48` | druga_slojna_veza: `av03_02-av03_04` | presuda: `varijanta` | razlog: moment sile hidrostatskog tlaka na poklopac oko O ostaje metodski blizak postojecem ravnoplosnom bloku.
- `VG-02-63` | skriptna_obitelj: `v05_z43-v05_z48` | druga_slojna_veza: `nema bliskog para` | presuda: `jedinstven` | razlog: reakcija u tocci A zbog hidrostatskog tlaka na branu otvara cist oslonacki zadatak kojeg baza nema.
- `VG-02-64` | skriptna_obitelj: `v05_z41-v05_z44` | druga_slojna_veza: `av03_02-av03_04` | presuda: `varijanta` | razlog: sila za drzanje poklopca da se ne otvori ostaje osnovna ravnoplosna varijanta.
- `VG-02-65` | skriptna_obitelj: `v05_z41-v05_z44` | druga_slojna_veza: `av03_02-av03_04` | presuda: `varijanta` | razlog: vertikalna sila za otvaranje poklopca je bliska izvedba istog mehanizma otvaranja.
- `VG-02-66` | skriptna_obitelj: `v05_z41-v05_z44` | druga_slojna_veza: `av03_02-av03_04` | presuda: `bliski_duplikat` | razlog: sila kod koje je poklopac jos zatvoren zauzima gotovo isto urednicko mjesto kao standardni zadaci drzanja ravnog poklopca.
- `VG-02-67` | skriptna_obitelj: `v05_z41-v05_z44` | druga_slojna_veza: `av03_02-av03_04` | presuda: `varijanta` | razlog: sila za drzanje zatvaraca zanemarive tezine ostaje bliska, ali ne identicna, koso postavljenoj ravnoplosnoj obitelji.
- `VG-02-68` | skriptna_obitelj: `v05_z42-v05_z48` | druga_slojna_veza: `av03_02-av03_04` | presuda: `varijanta` | razlog: moment sile hidrostatskog tlaka na zatvarac OAB ostaje trenutna varijanta momentnog racuna na ravnoj plohi.
- `VG-02-69` | skriptna_obitelj: `v05_z46-v05_z48` | druga_slojna_veza: `nema bliskog para` | presuda: `jedinstven` | razlog: pretlak u ravnini kroz O za ravnotezu trokutastog zatvaraca s vanjskom silom daje novu kombinaciju zatvorenog sustava i trokutaste geometrije.
- `VG-02-70` | skriptna_obitelj: `v05_z48` | druga_slojna_veza: `nema bliskog para` | presuda: `jedinstven` | razlog: homogena greda trokutastog presjeka uvodi spoj tezine tijela i hidrostatskog opterecenja u novom poprecnom presjeku.
- `VG-02-71` | skriptna_obitelj: `v02_z15, v03_z30` | druga_slojna_veza: `av03_11-av03_12` | presuda: `jedinstven` | razlog: visina razine drugog fluida za nulnu rezultantu na kocku daje lijep zadatak uzgona na granici dvaju fluida.
- `VG-02-72` | skriptna_obitelj: `v05_z43-v05_z48` | druga_slojna_veza: `nema bliskog para` | presuda: `jedinstven` | razlog: istodobno trazenje tlaka i duljine za ponistenje sila i momenta na zatvaracu daje jaci projektni uvjet od baznih primjera.
- `VG-02-73` | skriptna_obitelj: `v06_z49-v06_z55` | druga_slojna_veza: `nema bliskog para` | presuda: `jedinstven` | razlog: pretlak ispod poklopca koji vertikalnom komponentom rezultante uravnotezuje tezinu otvara prijelaz prema zakrivljenim plohama i zatvorenim volumenima.
- `VG-02-74` | skriptna_obitelj: `v05_z43-v05_z48, v06_z53-v06_z55` | druga_slojna_veza: `nema bliskog para` | presuda: `jedinstven` | razlog: poklopac s djelomicno zarobljenim zrakom daje spoj hidrostatike i zatvorenog plinskog jastuka koji baza nema.
- `VG-02-75` | skriptna_obitelj: `v05_z41-v05_z48` | druga_slojna_veza: `av03_01-av03_04` | presuda: `jedinstven` | razlog: rezultantna sila i hvatiste na zatvaracu uz zadani podtlak daju zatvoreni-sustav varijantu dovoljno razlicitu od obicnih otvorenih ploca.

### U06-U07 - Zakrivljene plohe, uzgon i stabilnost

- `VG-02-76` | skriptna_obitelj: `v06_z49-v07_z02` | druga_slojna_veza: `av03_08-av03_10` | presuda: `jedinstven` | razlog: cilindricni zatvarac koji drzi otvor uzgonom daje cistu novu scenu spoja zakrivljene plohe i plovnosti.
- `VG-02-77` | skriptna_obitelj: `v06_z54-v06_z55` | druga_slojna_veza: `av03_11-av03_12` | presuda: `jedinstven` | razlog: dubina potonuca cilindricne posude nakon ispustanja zraka je pravi kompozitni zadatak plivanja i zarobljenog zraka.
- `VG-02-78` | skriptna_obitelj: `v06_z53-v06_z55` | druga_slojna_veza: `nema bliskog para` | presuda: `jedinstven` | razlog: promjena sile u vijcima nakon odzracivanja poklopca oblika plasta stosca daje konstrukcijski odgovor na zakrivljenoj plohi.
- `VG-02-79` | skriptna_obitelj: `v06_z49-v07_z02` | druga_slojna_veza: `av03_05-av03_10` | presuda: `varijanta` | razlog: rezultantna sila tlaka na kruzni cilindar ostaje bazna obitelj zakrivljene plohe.
- `VG-02-80` | skriptna_obitelj: `v06_z49-v07_z02` | druga_slojna_veza: `av03_05-av03_10` | presuda: `varijanta` | razlog: horizontalna i vertikalna sila na cilindricni zatvarac ostaju klasicni rastav `F_H/F_V`.
- `VG-02-81` | skriptna_obitelj: `v06_z49-v07_z02` | druga_slojna_veza: `av03_05-av03_10` | presuda: `varijanta` | razlog: horizontalna i vertikalna sila na poklopac jed. sirine ostaju u istoj metodskoj obitelji rastava sila.
- `VG-02-82` | skriptna_obitelj: `v07_z02` | druga_slojna_veza: `av03_05-av03_10` | presuda: `varijanta` | razlog: horizontalna sila za drzanje polukruzne brane AO ostaje bliska polucilindricna zatvaracka scena.
- `VG-02-83` | skriptna_obitelj: `v06_z49-v07_z02` | druga_slojna_veza: `nema bliskog para` | presuda: `jedinstven` | razlog: rezultantna sila vode na cilindricni poklopac uz dodatni tezi fluid daje novu slojevitu zakrivljenu scenu.
- `VG-02-84` | skriptna_obitelj: `v06_z49-v07_z02` | druga_slojna_veza: `av03_05-av03_10` | presuda: `varijanta` | razlog: sila za drzanje poklopca zanemarive tezine oko O ostaje jos jedna izvedba zakrivljenog zatvaraca.
- `VG-02-85` | skriptna_obitelj: `v06_z49-v07_z02` | druga_slojna_veza: `nema bliskog para` | presuda: `jedinstven` | razlog: polucilindricni poklopac spojen s ravnom stijenkon na zatvorenom spremniku trazi stvarni spoj zakrivljenog i ravnog doprinosa.
- `VG-02-86` | skriptna_obitelj: `v06_z49-v07_z02` | druga_slojna_veza: `nema bliskog para` | presuda: `jedinstven` | razlog: vanjska i unutarnja sila na poklopac na obodu posude uvode dvostrano opterecenje zakrivljene plohe koje baza nema.
- `VG-02-87` | skriptna_obitelj: `v06_z53-v06_z55` | druga_slojna_veza: `nema bliskog para` | presuda: `jedinstven` | razlog: pretlak unutar kuglastog spremnika pri razdvajanju polovina daje izrazito konstrukcijski i geometrijski nov zadatak.
- `VG-02-88` | skriptna_obitelj: `v06_z49-v06_z55` | druga_slojna_veza: `nema bliskog para` | presuda: `jedinstven` | razlog: dubina otvaranja poklopca potopljene cilindricne posude daje prijelaz izmedu zakrivljenih ploha i potopljenih spremnika s pretlakom.
- `VG-02-89` | skriptna_obitelj: `v06_z54-v06_z55` | druga_slojna_veza: `nema bliskog para` | presuda: `jedinstven` | razlog: akceleracija otpadanja polukuglastog dna za fluidni nosac daje vrlo rijedak spoj uzgona, inercije i zakrivljene geometrije.

## Radni zakljucak za U04-U07 (Virag 2.21-2.89)

Veliki staticki blok `Virag 2.21-2.89` je vrijedan, ali urednicki izrazito selektivan. Ravnoplosni dio je pretezno `varijanta`, uz nekoliko jakih `jedinstven` kandidata poput `VG-02-22`, `VG-02-26`, `VG-02-34`, `VG-02-38`, `VG-02-39`, `VG-02-42`, `VG-02-55`, `VG-02-63`, `VG-02-69`, `VG-02-71`, `VG-02-72`, `VG-02-73`, `VG-02-74` i `VG-02-75`. Relativno mirovanje daje niz novih rubnih scenarija (`VG-02-46` do `VG-02-54`), a zakrivljene plohe i uzgon su najjaci dio bloka kroz `VG-02-76`, `VG-02-77`, `VG-02-78`, `VG-02-83`, `VG-02-85`, `VG-02-86`, `VG-02-87`, `VG-02-88` i `VG-02-89`. `VG-02-24` i `VG-02-25` najbolje ostaju `rezervni`, a `VG-02-66` je najbliza ravnoplosna kompresija kao `bliski_duplikat`.

## Prva operativna odluka nakon ove matrice

1. U glavnoj evidenciji treceg sloja mogu se dopisati `duplication_status` oznake za `VG-02-21` do `VG-02-89`, uz vec poznate source-gap rupe `2.41` i `2.45`.
2. Nakon toga su svi tekstualno citljivi Virag blokovi urednicki zatvoreni.