# Evidencija zadataka iz Vjezbe_530_540_150

## Svrha dokumenta

Ovo je drugi sloj radne evidencije zadataka, uveden tek nakon bazne evidencije skripte. Dokument cuva sve heading-definirane zadatkovne jedinice iz markdown korpusa `private/materials/Vjezbe_530_540_150`.

## Status baze

- source_layer: `530_540_150`
- obuhvat: `11` markdown datoteka
- stvarni broj trenutno evidentiranih jedinica: `77`
- polazni inventurni default za sve stavke: `duplication_status = za_procjenu`, `migration_status = nije_uneseno`

Nakon zavrsnog closure-prolaza izostanak `migration_status` u ovom dokumentu vise ne znaci dodatni posao, nego svjesnu urednicku odluku da jedinica ostaje dokumentirana kao `varijanta`, `hibrid`, teorijski prosireni blok ili rezerva bez zasebnog javnog `1:1` pandana.

## Prvi potvrdeni javni sync drugog sloja

Ovaj sloj se sinkronizira stroze od skriptnog korpusa. `migration_status` se u prvom prolazu dopisuje samo ondje gdje je javna veza prema jednoj jedinici drugog sloja dovoljno jasna, a ne samo na razini sire teorijske obitelji ili tematike poglavlja.

Nakon dosadasnjih konzervativnih sync-prolaza, taj prag zasad sigurno prelazi:

1. `av01_14` -> javna prerada u `U02` kao WE `Smicno naprezanje u tankom uljnom sloju`
2. `av05_04` -> javna prerada u `U11` kao WE `Kalibracijska mlaznica na prirubnici`
3. `av08_01` -> javna prerada u `U13` kao WE `Od Reynoldsovog broja do ukupnog gubitka u jednoj dionici`

Za ostale stavke `U01-U03` radne matrice vec daju konacnu urednicku presudu po `duplication_status`; izostanak task-level `migration_status` ondje je namjerna zavrsna odluka, a ne dodatni backlog.

## Rezultat prvog prosirenog pregleda `U04-U10`

Prvi siri sync-prolaz pokazao je da drugi sloj nije "prazan", ali ni da se moze mehanicki prepisati u `migration_status` polje samo zato sto je tematski blizak javnom chapteru.

1. Za `U04-U07` radna matrica dobro razdvaja `varijanta` i `jedinstven`, ali trenutni javni chapteri i nakon closure-prolaza ne daju dovoljno cistu `1:1` vezu prema pojedinoj auditornoj jedinici kao sto je to slucaj za `av01_14`.
2. Za `U08-U10` matrica otkriva vise jakih kandidata (`av04_01`, `av04_02`, `av04_04`), ali oni se zakljucuju kao prosirenje ili paralelni varijantni korpus, ne kao vec potvrden task-level prijenos; `av08_03` se pritom zakljucuje kao dokumentirani hibrid bez `1:1` javne prerade u danasnjem `U10/U13`.
3. Za `U11-U13` prvi konzervativni task-level sync sigurno prelaze `av05_04` i `av08_01`, dok `U12` ostaje urednicki valjan bez obveznog cistog uvoza iz drugog sloja.
4. Zato je u ovom dokumentu bolje imati malo `migration_status` potvrda koje su stvarno obranjive nego puno proizvoljnih upisa koji bi kasnije morali biti vracani.

## Rezultat dodatnog konzervativnog pregleda `U03`, `U05` i `U08`

Nakon dodatnog usporednog citanja javnih chaptera i najblizih donor-zadataka drugog sloja, ni u ovim blokovima nije dodana nova task-level `migration_status` potvrda; preostale veze zakljucene su kao tematske ili varijantne, bez prisilnog `1:1` upisa.

1. `U03`: zadaci `av02_07-av02_16` ostaju na razini tematske ili teorijske blizine; trenutni javni `U03` ima konkretne `WE`-ove o diferencijalnom manometru i ravnotezi klipa, dok drugi sloj ovdje uglavnom vodi opce hidrostatske formule, atmosferu ili drukcije manometarske postave.
2. `U05`: blok `av03_01-av03_04` ostaje urednicki koristan, ali ne i 1:1 javno potvrden; trenutni javni `U05` je oslonjen na skriptni bazni pravokutni poklopac i na projektni primjer s ukrutama, ne na pojedinu auditornu jedinicu drugog sloja.
3. `U08`: kandidati `av04_01-av04_03` ostaju dobri kao prosirenje kontinuiteta, ali ne kao vec potvrden task-level prijenos; raketni maseni protok, obodno istjecanje izmedu ploca i spremnik s konstantnom razinom nisu isti javni primjeri kao danasnji difuzor i komora za mijesanje.

## Rezultat dodatnog konzervativnog pregleda hibridnih blokova `U04-U07` i `U10/U13`

Nakon citanja stvarnih javnih `WE`-ova u `U04`, `U06`, `U07`, `U10` i `U13` te usporedbe s najblizim donor-stavkama drugog sloja, ni ovdje nije dodana nova task-level `migration_status` potvrda; hibridni i kompozitni blokovi zakljuceni su bez lazne `1:1` migracije.

1. `U04`: blok `av03_13-av03_16` ostaje vazan kao obitelj relativnog mirovanja, ali trenutni javni `U04` sigurno ima samo skriptno potvrdenu vezu preko `v03_z32`; drugi `WE` je urednicki kompozit s prelijevanjem i silom na stijenci, pa ga ne treba vezati 1:1 uz jednu auditornu jedinicu.
2. `U06-U07`: blok `av03_05-av03_12` ostaje koristan hibrid zakrivljenih ploha, uzgona i stabilnosti, ali trenutni javni `U06` vec pociva na skriptno potvrdenom `v06_z50`, dok javni `U07` sada ima tri urednicki prihvacena primjera bez dovoljno jake veze prema jednoj auditornoj jedinici drugog sloja; blok se zato zakljucuje kao hibrid bez `1:1` `migration_status` potvrde.
3. `U10/U13`: `av08_03` se zakljucuje kao dokumentirani hibrid zato sto u jednoj sceni spaja dobavu crpke, dvije potrosne grane i snagu motora, dok danasnji javni `U10` i `U13` te motive obrađuju odvojeno; zato ga i dalje ne treba nasilno rastaviti u lazni `1:1` sync.

## Kljuicne urednicke napomene

1. Ovaj korpus ne koristi `### Zadatak ...` nego top-level naslove `# ...` kao granice zadataka.
2. Datoteka `2019_KMF_MFL_Auditorne_vjezbe_2_Statika_-_hidraulika_Ver.1.12.md` stvarno se cijepa preko `U01` i `U03`, pa je ne treba voditi kao cisti ulaz za `U02`.
3. Datoteka `2021_KMF_MFL_Auditorne_vjezbe_1_Statika_-_svojstva_Ver.1.13.md` stvarno se cijepa preko `U01` i `U02`.
4. Datoteka `2019_KMF_MFL_Auditorne_vjezbe_3_Statika_-_hidrostatika_Ver.1.12.md` nije 1:1 poglavlje nego se raspada preko `U05`, `U06`, `U07` i `U04`.
5. Datoteka `2019_KMF_MFL_Auditorne_vjezbe_8._Din._real._-_gubici_Ver.1.03.md` sadrzi treci heading bez brojcane oznake; u evidenciji ostaje kao `bez_oznake_u_headingu`.
6. Datoteka `2019_KMF_MFL_Auditorne_vjezbe_10._Din._real._-_aerodinamika_Ver.1.04.md` ima ocitu anomaliju legacy numeracije (`14.1`, `14.2`, `4.3`, `4.4`, `4.4`, `14.6`, `14.7`); evidencija to cuva bez samovoljnog ispravljanja.
7. Datoteka `2019_KMF_MFL_Auditorne_vjezbe_11._Din._real._-_teorija_slicnosti_Ver.1.06.md` sadrzi izvorni tipfeler `Premet` u naslovima `16.5` i `16.6`; tipfeler se ne ispravlja u `legacy_ref` sloju.

## Popis po izvornoj datoteci

### 2021_KMF_MFL_Auditorne_vjezbe_1_Statika_-_svojstva_Ver.1.13.md

- `av01_01` | legacy_ref: `1.1` | naslov: `fizikalna svojstva fluida - gustoca, kineticka interpretacija` | preliminarni_cilj: `U01` | duplication_status: `jedinstven`
- `av01_02` | legacy_ref: `1.2` | naslov: `fizikalna svojstva fluida - gustoca` | preliminarni_cilj: `U01` | duplication_status: `jedinstven`
- `av01_03` | legacy_ref: `1.3` | naslov: `fizikalna svojstva fluida - gustoca` | preliminarni_cilj: `U01` | duplication_status: `jedinstven`
- `av01_04` | legacy_ref: `1.4` | naslov: `fizikalna svojstva fluida - tlak, kineticka interpretacija` | preliminarni_cilj: `U01` | duplication_status: `jedinstven`
- `av01_05` | legacy_ref: `1.5` | naslov: `fizikalna svojstva fluida - koeficijent stlacivosti i modul elasticnosti` | preliminarni_cilj: `U01` | duplication_status: `varijanta`
- `av01_06` | legacy_ref: `1.6` | naslov: `fizikalna svojstva fluida - koeficijent stlacivosti i modul elasticnosti` | preliminarni_cilj: `U01` | duplication_status: `varijanta`
- `av01_07` | legacy_ref: `1.7` | naslov: `fizikalna svojstva fluida - koeficijent stlacivosti i modul elasticnosti` | preliminarni_cilj: `U01` | duplication_status: `varijanta`
- `av01_08` | legacy_ref: `1.8` | naslov: `fizikalna svojstva fluida - koeficijent stlacivosti i modul elasticnosti` | preliminarni_cilj: `U01` | duplication_status: `bliski_duplikat`
- `av01_09` | legacy_ref: `1.9` | naslov: `fizikalna svojstva fluida - toplinska rastezljivost` | preliminarni_cilj: `U01` | duplication_status: `bliski_duplikat`
- `av01_10` | legacy_ref: `1.10` | naslov: `fizikalna svojstva fluida - toplinska rastezljivost` | preliminarni_cilj: `U01` | duplication_status: `varijanta`
- `av01_11` | legacy_ref: `1.11` | naslov: `fizikalna svojstva fluida - viskoznost, kineticka interpretacija` | preliminarni_cilj: `U02` | duplication_status: `jedinstven`
- `av01_12` | legacy_ref: `1.12` | naslov: `fizikalna svojstva fluida - viskoznost` | preliminarni_cilj: `U02` | duplication_status: `jedinstven`
- `av01_13` | legacy_ref: `1.13` | naslov: `fizikalna svojstva fluida - viskoznost` | preliminarni_cilj: `U02` | duplication_status: `varijanta`
- `av01_14` | legacy_ref: `1.14` | naslov: `fizikalna svojstva fluida - viskoznost` | preliminarni_cilj: `U02` | duplication_status: `jedinstven` | migration_status: `validirano` | napomena: `javna prerada potvrdena u U02 WE Smicno naprezanje u tankom uljnom sloju`
- `av01_15` | legacy_ref: `1.15` | naslov: `fizikalna svojstva fluida - viskoznost` | preliminarni_cilj: `U02` | duplication_status: `bliski_duplikat`
- `av01_16` | legacy_ref: `1.16` | naslov: `fizikalna svojstva fluida - viskoznost` | preliminarni_cilj: `U02` | duplication_status: `bliski_duplikat`
- `av01_17` | legacy_ref: `1.17` | naslov: `fizikalna svojstva fluida - koeficijent povrsinske napetosti i kut kvasenja` | preliminarni_cilj: `U02` | duplication_status: `bliski_duplikat`

### 2019_KMF_MFL_Auditorne_vjezbe_2_Statika_-_hidraulika_Ver.1.12.md

- `av02_01` | legacy_ref: `2.1` | naslov: `statika fluida - hidraulicki tlak` | preliminarni_cilj: `U01` | duplication_status: `bliski_duplikat`
- `av02_02` | legacy_ref: `2.2` | naslov: `statika fluida - hidraulicki tlak` | preliminarni_cilj: `U01` | duplication_status: `bliski_duplikat`
- `av02_03` | legacy_ref: `2.3` | naslov: `statika fluida - hidraulicki tlak` | preliminarni_cilj: `U01` | duplication_status: `varijanta`
- `av02_04` | legacy_ref: `2.4` | naslov: `statika fluida - apsolutni tlak` | preliminarni_cilj: `U01` | duplication_status: `varijanta`
- `av02_05` | legacy_ref: `2.5` | naslov: `statika fluida - apsolutni tlak` | preliminarni_cilj: `U01` | duplication_status: `varijanta`
- `av02_06` | legacy_ref: `2.6` | naslov: `relativni tlak` | preliminarni_cilj: `U01` | duplication_status: `varijanta`
- `av02_07` | legacy_ref: `2.7` | naslov: `hidrostatski tlak` | preliminarni_cilj: `U03` | duplication_status: `varijanta`
- `av02_08` | legacy_ref: `2.8` | naslov: `hidrostatski tlak` | preliminarni_cilj: `U03` | duplication_status: `varijanta`
- `av02_09` | legacy_ref: `2.9` | naslov: `hidrostatski tlak` | preliminarni_cilj: `U03` | duplication_status: `varijanta`
- `av02_10` | legacy_ref: `2.10` | naslov: `hidrostatski tlak` | preliminarni_cilj: `U03` | duplication_status: `varijanta`
- `av02_11` | legacy_ref: `2.11` | naslov: `hidrostatski tlak` | preliminarni_cilj: `U03` | duplication_status: `varijanta`
- `av02_12` | legacy_ref: `2.12` | naslov: `hidrostatski tlak` | preliminarni_cilj: `U03` | duplication_status: `varijanta` | napomena: `diferencijalni manometar postoji tematski, ali postava zatvorenog i otvorenog spremnika s podtlakom nije 1:1 s javnim U03 WE`
- `av02_13` | legacy_ref: `2.13` | naslov: `hidrostatski i hidraulicki tlak` | preliminarni_cilj: `U03` | duplication_status: `varijanta` | napomena: `zatvoreni cilindri s klipom, podtlakom i silom na poklopcu ostaju siri zadatak od javnog U03 WE o ravnotezi klipa i tlaku u komorama`
- `av02_14` | legacy_ref: `2.14` | naslov: `ravnoteza atmosfere - teoretske formule` | preliminarni_cilj: `U03` | duplication_status: `varijanta`
- `av02_15` | legacy_ref: `2.15` | naslov: `ravnoteza atmosfere - iskustvene formule` | preliminarni_cilj: `U03` | duplication_status: `varijanta`
- `av02_16` | legacy_ref: `2.16` | naslov: `atmosferska strujanja (iskustvene formule)` | preliminarni_cilj: `U03` | duplication_status: `jedinstven` | napomena: `jedinstven je unutar drugog sloja, ali nema 1:1 javni pandan u trenutnom U03 koji ne obrađuje iskustveni profil vjetra`

### 2019_KMF_MFL_Auditorne_vjezbe_3_Statika_-_hidrostatika_Ver.1.12.md

- `av03_01` | legacy_ref: `Z 3.16` | naslov: `tlak na ravne povrsine` | preliminarni_cilj: `U05` | duplication_status: `bliski_duplikat` | napomena: `vrlo je blizu baznom U05 primjeru, ali javni WE je vec konzervativno vezan uz skriptni donor v05_z41 pa se ovdje ne otvara drugi task-level prijenos`
- `av03_02` | legacy_ref: `Z 3.17` | naslov: `tlak na ravne kose povrsine` | preliminarni_cilj: `U05` | duplication_status: `varijanta`
- `av03_03` | legacy_ref: `Z 3.18` | naslov: `tlak na ravne povrsine` | preliminarni_cilj: `U05` | duplication_status: `varijanta`
- `av03_04` | legacy_ref: `Z 3.19` | naslov: `tlak na ravne kose povrsine` | preliminarni_cilj: `U05` | duplication_status: `varijanta`
- `av03_05` | legacy_ref: `Z 3.20` | naslov: `hidrostatski tlak - sila na zakrivljenu povrsinu` | preliminarni_cilj: `U06` | duplication_status: `varijanta`
- `av03_06` | legacy_ref: `Z 3.21` | naslov: `hidrostatski tlak - sila na zakrivljenu povrsinu` | preliminarni_cilj: `U06` | duplication_status: `varijanta`
- `av03_07` | legacy_ref: `Z 3.22` | naslov: `hidrostatski tlak - sila na zakrivljenu povrsinu` | preliminarni_cilj: `U06` | duplication_status: `varijanta`
- `av03_08` | legacy_ref: `Z 3.23` | naslov: `hidrostatski tlak - sila na zakrivljenu povrsinu` | preliminarni_cilj: `U06` | duplication_status: `jedinstven`
- `av03_09` | legacy_ref: `Z 3.24` | naslov: `hidrostatski tlak - sila na zakrivljenu povrsinu` | preliminarni_cilj: `U06` | duplication_status: `jedinstven`
- `av03_10` | legacy_ref: `Z 3.25` | naslov: `hidrostatski tlak - sila na zakrivljenu povrsinu` | preliminarni_cilj: `U06` | duplication_status: `varijanta`
- `av03_11` | legacy_ref: `Z 3.26` | naslov: `uzgon` | preliminarni_cilj: `U07` | duplication_status: `jedinstven`
- `av03_12` | legacy_ref: `Z 3.28` | naslov: `plivanje - stabilnost` | preliminarni_cilj: `U07` | duplication_status: `varijanta`
- `av03_13` | legacy_ref: `Z 3.29` | naslov: `relativno mirovanje - translacija` | preliminarni_cilj: `U04` | duplication_status: `varijanta`
- `av03_14` | legacy_ref: `Z 3.31` | naslov: `statika-relativno mirovanje-rotacija` | preliminarni_cilj: `U04` | duplication_status: `varijanta`
- `av03_15` | legacy_ref: `Z 3.32` | naslov: `statika-relativno mirovanje-rotacija` | preliminarni_cilj: `U04` | duplication_status: `jedinstven`
- `av03_16` | legacy_ref: `Z 3.33` | naslov: `relativno mirovanje-rotacija` | preliminarni_cilj: `U04` | duplication_status: `jedinstven`

### 2019_KMF_MFL_Auditorne_vjezbe_4._Din._ideal._-_kontinuitet_i_energija_Ver.1.12.md

- `av04_01` | legacy_ref: `7.1` | naslov: `dinamika idealnog fluida - maseni protok` | preliminarni_cilj: `U08` | duplication_status: `jedinstven` | napomena: `raketni maseni protok nije 1:1 s javnim U08 primjerima difuzora i komore za mijesanje`
- `av04_02` | legacy_ref: `7.2` | naslov: `dinamika idealnog fluida - volumni protok` | preliminarni_cilj: `U08` | duplication_status: `jedinstven` | napomena: `obodno istjecanje ulja izmedu ploca ostaje posebna volumenska varijanta bez javnog 1:1 WE u U08`
- `av04_03` | legacy_ref: `7.3` | naslov: `dinamika idealnog fluida - kontinuitet strujanja` | preliminarni_cilj: `U08` | duplication_status: `varijanta` | napomena: `spremnik s konstantnom razinom nije isti javni primjer kao danasnji U08 WE-ovi o difuzoru i mjesanju`
- `av04_04` | legacy_ref: `7.4` | naslov: `dinamika idealnog fluida - energija` | preliminarni_cilj: `U09` | duplication_status: `jedinstven`

### 2019_KMF_MFL_Auditorne_vjezbe_5._Din._ideal._-_kolicina_gibanja_Ver.1.12.md

- `av05_01` | legacy_ref: `9.1` | naslov: `promjena kolicine gibanja` | preliminarni_cilj: `U11` | duplication_status: `jedinstven`
- `av05_02` | legacy_ref: `9.2` | naslov: `promjena kolicine gibanja` | preliminarni_cilj: `U11` | duplication_status: `bliski_duplikat`
- `av05_03` | legacy_ref: `9.3` | naslov: `promjena kolicine gibanja` | preliminarni_cilj: `U11` | duplication_status: `jedinstven`
- `av05_04` | legacy_ref: `9.4` | naslov: `promjena kolicine gibanja` | preliminarni_cilj: `U11` | duplication_status: `jedinstven` | migration_status: `validirano` | napomena: `javna prerada potvrdena u U11 WE Kalibracijska mlaznica na prirubnici`

### 2019_KMF_MFL_Auditorne_vjezbe_6._Din._ideal._-_kavitacija_Ver.1.12.md

- `av06_01` | legacy_ref: `8.1` | naslov: `dinamika idealnog fluida - kavitacija` | preliminarni_cilj: `U10` | duplication_status: `varijanta`
- `av06_02` | legacy_ref: `8.2` | naslov: `dinamika idealnog fluida - kavitacija` | preliminarni_cilj: `U10` | duplication_status: `varijanta`

### 2019_KMF_MFL_Auditorne_vjezbe_7._Din._real._-_granicni_sloj_Ver.1.02.md

- `av07_01` | legacy_ref: `10.1` | naslov: `granicni sloj - otpor strujanja` | preliminarni_cilj: `REZERVNI` | duplication_status: `rezervni`

### 2019_KMF_MFL_Auditorne_vjezbe_8._Din._real._-_gubici_Ver.1.03.md

- `av08_01` | legacy_ref: `12.1` | naslov: `dinamika realnog fluida - gubici strujanja: hidraulicka hrapavost i linijski gubici` | preliminarni_cilj: `U13` | duplication_status: `jedinstven` | migration_status: `validirano` | napomena: `javna prerada potvrdena u U13 WE Od Reynoldsovog broja do ukupnog gubitka u jednoj dionici`
- `av08_02` | legacy_ref: `12.2` | naslov: `dinamika realnog fluida - gubici strujanja - crpke, razlika energija` | preliminarni_cilj: `U10` | duplication_status: `varijanta`
- `av08_03` | legacy_ref: `bez_oznake_u_headingu` | naslov: `gubici strujanja - crpke, dobava i kapacitet` | preliminarni_cilj: `REV-U10/U13` | duplication_status: `jedinstven` | napomena: `treci source heading nema brojcanu oznaku; zakljucen je kao dokumentirani hibrid izmedu U10 i U13 jer trenutni javni chapteri motive dobave crpke, dviju grana i snage motora obraduju odvojeno, a ne u jednoj `1:1` preradi`

### 2019_KMF_MFL_Auditorne_vjezbe_9._Din._real._-_protjecanje_Ver.1.03.md

- `av09_01` | legacy_ref: `11.1` | naslov: `dinamika realnog fluida - protjecanje i opstrujavanje` | preliminarni_cilj: `REV-U12/U13` | duplication_status: `rezervni`

### 2019_KMF_MFL_Auditorne_vjezbe_10._Din._real._-_aerodinamika_Ver.1.04.md

- `av10_01` | legacy_ref: `14.1` | naslov: `opstrujavanje - otpor oblika` | preliminarni_cilj: `REZERVNI` | duplication_status: `rezervni`
- `av10_02` | legacy_ref: `14.2` | naslov: `opstrujavanje - otpor oblika` | preliminarni_cilj: `REZERVNI` | duplication_status: `rezervni`
- `av10_03` | legacy_ref: `4.3` | naslov: `opstrujavanje - otpor oblika` | preliminarni_cilj: `REZERVNI` | duplication_status: `rezervni` | napomena: `legacy_ref ocito izlazi iz serije 14.x, ali se cuva kao izvorni zapis`
- `av10_04` | legacy_ref: `4.4` | naslov: `opstrujavanje - otpor oblika` | preliminarni_cilj: `REZERVNI` | duplication_status: `rezervni` | napomena: `legacy_ref dijeljen s iducom jedinicom`
- `av10_05` | legacy_ref: `4.4` | naslov: `opstrujavanje - otpor trenja` | preliminarni_cilj: `REZERVNI` | duplication_status: `rezervni` | napomena: `dvostruki legacy_ref unutar iste datoteke`
- `av10_06` | legacy_ref: `14.6` | naslov: `uzgon i otpor` | preliminarni_cilj: `REV-U12` | duplication_status: `rezervni`
- `av10_07` | legacy_ref: `14.7` | naslov: `opstrujavanje - uzgon i otpor` | preliminarni_cilj: `REV-U12` | duplication_status: `rezervni`

### 2019_KMF_MFL_Auditorne_vjezbe_11._Din._real._-_teorija_slicnosti_Ver.1.06.md

- `av11_01` | legacy_ref: `16.1` | naslov: `teorija slicnosti` | preliminarni_cilj: `REZERVNI` | duplication_status: `rezervni`
- `av11_02` | legacy_ref: `16.2` | naslov: `teorija slicnosti` | preliminarni_cilj: `REZERVNI` | duplication_status: `rezervni`
- `av11_03` | legacy_ref: `16.3` | naslov: `teorija slicnosti` | preliminarni_cilj: `REZERVNI` | duplication_status: `rezervni`
- `av11_04` | legacy_ref: `16.4` | naslov: `teorija slicnosti` | preliminarni_cilj: `REZERVNI` | duplication_status: `rezervni`
- `av11_05` | legacy_ref: `16.5` | naslov: `teorija slicnosti` | preliminarni_cilj: `REZERVNI` | duplication_status: `rezervni` | napomena: `u source headingu stoji tipfeler Premet`
- `av11_06` | legacy_ref: `16.6` | naslov: `teorija slicnosti` | preliminarni_cilj: `REZERVNI` | duplication_status: `rezervni` | napomena: `u source headingu stoji tipfeler Premet`

## Sto slijedi nakon ove evidencije

1. Usporediti ovaj drugi sloj sa skriptnim slojem iz `evidencija_zadataka_skripta.md` po ciljnim poglavljima.
2. Oznaciti svaku stavku kao `jedinstven`, `varijanta`, `bliski_duplikat` ili `rezervni`.
3. Tek nakon tog sparivanja krenuti na treci sloj dodatnih izvora.