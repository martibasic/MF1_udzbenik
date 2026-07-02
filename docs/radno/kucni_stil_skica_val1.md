# Kucni stil skica - Val 1

> Status u svibnju 2026.: ovaj dokument ostaje povijesna baza za prvi vizualni prag projekta. Pravila su i dalje korisna, ali Val 1 vise nije aktivna radna faza; stvarni aktualni status vodi se u `pilot_batch_prerade_zadataka.md` i `status_izrade_udzbenika.md`.

## Svrha dokumenta

Ovaj dokument zakljucava prvi mali skup skicnih pravila za tri javne prerade iz `val1_javne_prerade_zadataka.md`. Cilj nije crtacki perfekcionizam, nego dosljedna, print-first skica koja studentu odmah otkriva sto je fizikalno bitno.

## Opca pravila

1. Skica mora biti citljiva i kad se isprinta crno-bijelo.
2. Svaka skica mora imati jednu dominantnu poruku. Ako pokusava pokazati sve, pokazuje premalo.
3. Oznacava se samo ono sto stvarno ulazi u rjesenje.
4. Linije konstrukcije, razina i sila moraju se razlikovati debljinom ili tipom linije, ne bojom.
5. U istoj skici ne smiju se mijesati fizikalne velicine i geometrijske pomocne crtice bez jasne hijerarhije.

## Linijska hijerarhija

- `puna debela linija`: kruta stijenka, granica tijela, lopatica, spremnik
- `puna srednja linija`: slobodna povrsina, presjek, stvarna granica fluida
- `tanka puna linija`: mjere, kote, pomocne geometrijske veze
- `isprekidana linija`: referentna razina, os simetrije, produzenje smjera
- `strelica srednje debljine`: sila, brzina, ubrzanje, reakcija

## Pravilo oznaka

1. Geometrija se pise uz skicu: `L`, `H`, `B`, `R`, `a`, `e`.
2. Fizikalne velicine se odvajaju od geometrije: `F_R`, `R_x`, `R_y`, `a`, `rho`.
3. Jedna oznaka ima jedno znacenje u cijelom zadatku.
4. Ako ista scena trazi i tlocrt i bokocrt, oznake se ne dupliciraju bez razloga.

## Zabranjene stvari

1. sjenčanje samo radi estetike
2. precrtavanje izvornog rasporeda slova i mjernih linija
3. vise od jednog neovisnog koordinatnog sustava u istoj skici
4. dekorativni detalji koji ne ulaze u model
5. oznake koje se ne koriste u tekstu zadatka ili rjesenja

---

## Predlozak A - U04 - otvoreni spremnik u relativnom mirovanju

### Obavezni elementi

- bocni pogled spremnika
- jasno oznacena prednja i straznja stijenka
- strelica ubrzanja `a`
- nagnuta slobodna povrsina
- dvije karakteristicne visine na stijenkama
- jedna rezultanta sile na stijenci samo ako je to trazeno u zadatku

### Sto se ne crta

- valovi ili povrsinski nabori
- vise medupolozaja slobodne povrsine
- reakcije podloge ako nisu dio zadatka

### Minimalni raspored

1. spremnik zauzima sredisnji dio skice
2. strelica `a` ide iznad ili ispod spremnika, ne preko fluida
3. slobodna povrsina mora biti prva stvar koju oko cita
4. ako se crta efektivno polje sila, ide u mali izdvojeni inset, ne u glavnu skicu

### Kucna poruka ove skice

Student mora odmah vidjeti da je problem geometrija slobodne povrsine u efektivnom polju sila, a ne samo racun tlaka.

---

## Predlozak B - U07 - plivanje prizmatskog tijela s bocno pomaknutim teretom

### Obavezni elementi

- poprecni presjek platforme u vodi
- lijevi i desni uron `h_L` i `h_D`
- uzduzna os simetrije
- tezina platforme u osi simetrije
- tezina dodatnog tereta s bocnim pomakom `e`
- sila uzgona kroz teziste istisnine ili barem njezin pravac djelovanja

### Kad dodati tlocrtni inset

Tlocrtni inset se dodaje samo ako je bocni pomak tereta kljucna nepoznanica ili ako bez njega nije jasno s koje je strane teret postavljen.

### Sto se ne crta

- puni trodimenzijski ponton u perspektivi
- metacentar, ako zadatak stvarno ne radi s metacentarskom visinom
- detalji oplata, rubnjaka i opreme koji ne ulaze u model

### Minimalni raspored

1. vodna linija mora biti stabilna referenca preko cijele skice
2. nagib platforme ne smije biti pretjeran; skica ne smije sugerirati prevrtanje ako to nije zadano
3. tezine se crtaju odvojeno i citko, bez preklapanja s kotama urona

### Kucna poruka ove skice

Student mora odmah vidjeti da se ravnoteza rjesava kroz spoj uzgona, tezina i geometrije urona, a ne kroz "osjecaj" na koju je stranu platforma nagnuta.

---

## Predlozak C - U12 - vodilica mlaza i reakcija nosaca

### Obavezni elementi

- tlocrt ili horizontalni pogled
- ulazni vektor brzine `v_1`
- izlazni vektor brzine `v_2`
- kut skretanja `beta`
- granica kontrolnog volumena oko vodilice
- osi `x` i `y`
- reakcijske komponente nosaca `R_x` i `R_y`, ako se traze

### Sto se ne crta

- detaljna geometrija sapnice ako nije bitna za proracun osim presjeka
- trodimenzijski prikaz lopatice
- unutarnji tok s vise strujnica ako je dovoljan jedan reprezentativni smjer

### Minimalni raspored

1. ulazni smjer uvijek dolazi s lijeve strane, osim ako postoji jak razlog za obrat
2. izlazni smjer mora biti geometrijski cist i citljiv, ne "slobodno rukom"
3. kontrolni volumen mora ostati jednostavan i ne smije pratiti svaki rub vodilice
4. osi `x` i `y` idu izvan glavne putanje mlaza, da ne zaguše skicu

### Kucna poruka ove skice

Student mora odmah vidjeti da je jezgra zadatka promjena kolicine gibanja i rastav sila po koordinatnim osima.

---

## Pravilo prije izrade pune skice

Prije nego se skica nacrta u finalnom obliku, treba odgovoriti na tri pitanja:

1. Koja je jedna stvar koju student mora prvo uociti?
2. Koja je najmanja kolicina geometrije potrebna da zadatak bude jednoznacan?
3. Koje se oznake u skici moraju doslovno poklapati s tekstom zadatka i rjesenja?

Ako na bilo koje od ta tri pitanja nema jasnog odgovora, skica jos nije spremna za finalni layout.

---

## Izvedeni radni asseti

- `U04`: `assets/print/u04_val1_procesna_kada.svg`
- `U07`: `assets/print/u07_val1_platforma_kompresor.svg`
- `U12`: `assets/print/u12_val1_vodilica_mlaza.svg`

Ovi asseti su sada ugradeni u `source` poglavlja `U04`, `U07` i `U12` i zakljucavaju prvi radni vizualni jezik za Val 1.