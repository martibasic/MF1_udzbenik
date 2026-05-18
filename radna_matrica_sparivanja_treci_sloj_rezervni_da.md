# Radna matrica sparivanja treci sloj za rezervni blok (DA)

## Svrha dokumenta

Ovo je sedmi radni dokument za sparivanje treceg sloja. Fokus je samo na bloku `DA` iz izvora `SAVAR_sesija1_dimanzija_hidrostatika.md`.

## Pravilo citanja ove matrice

1. Skripta ostaje kanonski prvi zapis.
2. Drugi sloj ostaje vec zatvoren prvi sloj dopune.
3. Ovaj blok se cita stroze od prethodnih jer vecina zapisa siri opseg prema dimenzijskoj analizi, otporu strujanja i teoriji slicnosti.
4. `jedinstven` se ovdje koristi samo kad zadatak donosi jasan, koristan most prema `U02` koji nizi slojevi nemaju.
5. `varijanta` znaci da zadatak ostaje u istoj obitelji viskoznosti ili skaliranja, ali bez razloga da postane novi glavni kanonski zapis.
6. `bliski_duplikat` se koristi i za unutarnju kompresiju kada se ista ideja ponavlja unutar samog `DA` bloka.
7. `rezervni` se koristi kad zadatak jest koristan, ali urednicki pripada prosirenom ili izbornom korpusu, a ne glavnom toku knjige.

## Rezervni blok DA - postojeca jezgra

### Skriptna jezgra

- `v01_z06-v01_z09` i `v02_z10-v02_z18` za `U02`

### Drugi sloj i rezervni korpus

- `av01_11-av01_17` za `U02`
- `av07_01`, `av10_01-av10_07` i `av11_01-av11_06` kao vec zatvoren rezervni korpus granicnog sloja, opstrujavanja i teorije slicnosti

## Treci sloj DA - preliminarna presuda

### Cista dimenzijska analiza i slicnost

- `DA-1` | skriptna_obitelj: `nema bliskog para` | druga_slojna_veza: `nema bliskog para` | presuda: `rezervni` | razlog: opci Pi-teorem za tonjenje tijela je metodski vrijedan, ali siri knjigu prema zasebnom bloku dimenzijske analize.
- `DA-2` | skriptna_obitelj: `nema bliskog para` | druga_slojna_veza: `av10_01-av10_05` | presuda: `rezervni` | razlog: sila otpora tijela u viskoznom stlacivom fluidu urednicki vise pripada prosirenom bloku otpora i opstrujavanja.
- `DA-3` | skriptna_obitelj: `v02_z10-v02_z11` | druga_slojna_veza: `nema bliskog para` | presuda: `rezervni` | razlog: pretvorba mehanicke energije u toplinu pri rotaciji cilindra ostaje izdvojena primjena viskoznog disipiranja, ali ne nosi glavni tok `U02`.
- `DA-5` | skriptna_obitelj: `nema bliskog para` | druga_slojna_veza: `nema bliskog para` | presuda: `rezervni` | razlog: domet topovskog zrna je cista demonstracija Pi-teorema i kosog hica, izvan glavne jezgre mehanike fluida.
- `DA-7` | skriptna_obitelj: `nema bliskog para` | druga_slojna_veza: `nema bliskog para` | presuda: `rezervni` | razlog: Brinkmanov broj je koristan pojam, ali uvodi toplinski transport i specijalizirani aparat koji glavni tok ne treba.
- `DA-9` | skriptna_obitelj: `nema bliskog para` | druga_slojna_veza: `av10_01-av10_05` | presuda: `rezervni` | razlog: pogonska sila torpeda pripada sirim problemima otpora i opstrujavanja, koje vec drzimo u rezervnom korpusu.
- `DA-10` | skriptna_obitelj: `nema bliskog para` | druga_slojna_veza: `av10_01-av10_05` | presuda: `rezervni` | razlog: sila otpora ravne ploce u toku je korisna, ali urednicki ide u isti prosireni blok otpora kao i drugi rezervni aerodinamicki zadaci.
- `DA-11` | skriptna_obitelj: `nema bliskog para` | druga_slojna_veza: `nema bliskog para` | presuda: `rezervni` | razlog: brzina pulsa u arteriji otvara biofluidni i elasticni aparat koji je predaleko od osnovne MF1 jezgre.
- `DA-12` | skriptna_obitelj: `DA-2` | druga_slojna_veza: `av10_01-av10_05` | presuda: `bliski_duplikat` | razlog: prakticki ponavlja isti zadatak kao `DA-2` s istom fizikalnom idejom i istim skupom velicina.
- `DA-13` | skriptna_obitelj: `DA-8` | druga_slojna_veza: `nema bliskog para` | presuda: `bliski_duplikat` | razlog: promjer kapljice iz sprej sapnice je gotovo isti urednicki zapis kao `DA-8`.
- `DA-15` | skriptna_obitelj: `nema bliskog para` | druga_slojna_veza: `av11_01-av11_06` | presuda: `rezervni` | razlog: brod i propeler izrijekom prelaze u teoriju slicnosti, koja je vec urednicki zatvorena kao prosireni rezervni korpus.

### Rubni U02 kandidati

- `DA-4` | skriptna_obitelj: `v01_z07-v01_z09` | druga_slojna_veza: `av01_13-av01_16` | presuda: `jedinstven` | razlog: tonjenje kuglice po Stokesovoj logici daje cist, koristan most izmedu viskoznosti i skaliranja kojeg nizi slojevi nemaju u tom obliku.
- `DA-6` | skriptna_obitelj: `v01_z06` | druga_slojna_veza: `nema bliskog para` | presuda: `jedinstven` | razlog: tlak na kraju cijevi u laminarnom toku preko dimenzijske analize dobro povezuje unutarnje strujanje i viskozno smicanje.
- `DA-8` | skriptna_obitelj: `v02_z12-v02_z18` | druga_slojna_veza: `av01_17` | presuda: `rezervni` | razlog: kapljica iz sprej sapnice iako dodiruje povrsinsku napetost, ipak vise pripada prosirenom atomizacijskom bloku nego osnovnom `U02`.
- `DA-14` | skriptna_obitelj: `v01_z07-v01_z09` | druga_slojna_veza: `av01_13-av01_16` | presuda: `varijanta` | razlog: brzina talozenja kuglice ostaje bliska obitelj zadatka `DA-4`, ali s drugacijim parametriranjem i bez potrebe za drugim glavnim zapisom.

## Radni zakljucak za rezervni blok (DA)

Blok `DA` nije dobar kandidat za masovni ulazak u glavni tok knjige. Najveci dio treba ostati `rezervni`, uz unutarnju kompresiju `DA-2/DA-12` i `DA-8/DA-13`. Najjaci kandidati za stvarno zadrzavanje kao prosirene, ali korisne dopune su `DA-4` i `DA-6`, dok `DA-14` dobro radi kao njihova `varijanta`.

## Prva operativna odluka nakon ove matrice

1. U glavnoj evidenciji treceg sloja mogu se dopisati `duplication_status` oznake za `DA-1` do `DA-15`.
2. Nakon toga `SAVAR sesija 1` postaje urednicki zatvorena kao tekstualno citljiv izvor treceg sloja.