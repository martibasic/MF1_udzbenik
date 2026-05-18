# Radna matrica sparivanja za U11-U13 i rezervni korpus

## Svrha dokumenta

Ovo je zavrsni radni dokument za sparivanje baznog sloja `skripta` i drugog sloja `530_540_150`. Njime se zatvara drugi sloj do kraja: `U11-U13` i svi trenutno preostali zadaci koji ostaju u rezervnom korpusu.

## Pravilo citanja ove matrice

1. Skripta ostaje kanonski prvi zapis.
2. `jedinstven` znaci da drugi sloj donosi novu scenu ili metodski vazan dodatak.
3. `varijanta` znaci da je jezgra ista, ali je formulacija ili geometrija drukcija.
4. `bliski_duplikat` se koristi samo kada bi drugi sloj vrlo vjerojatno natjecao isti prostor s baznim skriptnim zadatkom.
5. `rezervni` znaci da zadatak ostaje popisan, ali se zasad ne prisiljava u glavni tok knjige.

## U11 - Kolicina gibanja i sile strujanja

### Skriptna jezgra

- `v11_z97-v11_z103`

### Drugi sloj - preliminarna presuda

- `av05_01` | skriptna_obitelj: `v11_z100-v11_z101` | presuda: `jedinstven` | razlog: odvojak s tri presjeka i tlakovnim silama siri skriptni blok s koljenima i silama strujanja.
- `av05_02` | skriptna_obitelj: `v11_z102` | presuda: `bliski_duplikat` | razlog: mlaz na plocu vec postoji kao izravna skriptna jezgra.
- `av05_03` | skriptna_obitelj: `v11_z103, v12_z104` | presuda: `jedinstven` | razlog: raketni potisak je vazna prijelazna scena izmedu kolicine gibanja i potiska.
- `av05_04` | skriptna_obitelj: `v11_z100-v11_z101, v12_z105` | presuda: `jedinstven` | razlog: sila na tijelo sapnice spaja promjenu kolicine gibanja i reakciju konstrukcije na nacin koji skripta nema u tom obliku.

### Radni zakljucak za U11

U11 iz drugog sloja dobiva stvarno koristan prosireni blok. Jedini izrazito bliski duplikat je `av05_02`, dok ostala tri zadatka vrijedi cuvati kao nadogradnju.

## U12 - Pokretne lopatice i potisak

### Skriptna jezgra

- `v12_z104-v12_z112`

### Radni zakljucak za drugi sloj

U ovom prolazu nema obveznog cistog uvoza iz `530_540_150` koji bi se bez nasilnog sirenja opsega morao ugraditi u glavni tok `U12`. Hibridni aerodinamicki zadaci ostaju vidljivi, ali zasad `rezervni`.

## U13 - Cjevovodi

### Skriptna jezgra

- `v13_z121-v13_z124`

### Drugi sloj - preliminarna presuda

- `av08_01` | skriptna_obitelj: `v13_z121-v13_z124` | presuda: `jedinstven` | razlog: linijski gubici, hrapavost i Moodyjev pristup daju bazni cjevovodni zadatak koji skripta nema tako eksplicitno.

### Radni zakljucak za U13

U13 iz drugog sloja mora barem zadrzati `av08_01`, jer on popunjava jezgreni temelj za trenje i hrapavost cijevi.

## Rezervni korpus - zadrzati, ali ne gurati u glavni tok

### Jasno rezervni izvori

- `av07_01` | legacy_ref: `10.1` | presuda: `rezervni` | razlog: granicni sloj je izvan trenutne jezgre knjige.
- `av10_01-av10_05` | legacy_ref: `14.1`, `14.2`, `4.3`, `4.4`, `4.4` | presuda: `rezervni` | razlog: opstrujavanje i otpori su zanimljivi, ali prebrzo sire opseg glavnog toka.
- `av11_01-av11_06` | legacy_ref: `16.1-16.6` | presuda: `rezervni` | razlog: teorija slicnosti ostaje vrijedna, ali nije nuzna za osnovni MF1 tok.

### Hibridni kandidati koji zasad ostaju rezervni

- `av09_01` | skriptna_obitelj: `v13_z122-v13_z123, v12_z111` | presuda: `rezervni` | razlog: difuzor na izlazu turbine i kavitacijsko ogranicenje jesu kvalitetan zadatak, ali trenutno razvlace granicu izmedu U12 i U13.
- `av10_06` | skriptna_obitelj: `v12_z108-v12_z109` | presuda: `rezervni` | razlog: profil krila i katalogski koeficijenti uvode siri aerodinamicki aparat nego sto glavni tok trenutno trazi.
- `av10_07` | skriptna_obitelj: `v12_z108-v12_z109` | presuda: `rezervni` | razlog: performanse zrakoplova i optimalna brzina leta ostaju korisni, ali kao prosireni ili izborni blok.

## Zavrsna operativna odluka nakon ove matrice

1. U glavnoj evidenciji drugog sloja sada se mogu dopisati zavrsni `duplication_status` zapisi.
2. Nakon toga drugi sloj `530_540_150` postaje urednicki zatvoren i spreman za treci sloj dodatnih izvora.