# Kurikularna matrica MF1 v2

Ovaj dokument je normativna urednička matrica. Kanonski tekst ostaje u `source/`, a matrica određuje redoslijed preduvjeta, minimalnu provjeru ishoda i planirano studentsko opterećenje. Ukupno ciljano opterećenje iznosi **145 sati rada uz udžbenik**; ne poistovjećuje se s cijelim ECTS opterećenjem kolegija.

| Pog. | Jezgra i glavni ishod | Obvezna provjera ishoda | Lajtmotiv | Sati |
|---:|---|---|---|---:|
| 0 | Odabrati radni tok i razinu pomoći | dijagnostički izbor T1–T4 | metoda rada | 2 |
| 1 | Kontinuum, svojstva, tlak i Pascal | procjena modela stlačivosti | rashladni/hidraulični sustav | 8 |
| 2 | Reologija, viskoznost i međupovršine | izbor konstitutivnog modela | rashladno sredstvo i mikrodoziranje | 9 |
| 3 | Hidrostatičko polje i manometrija | senzor s mjernom nesigurnošću | vodotoranj i balast | 9 |
| 4 | Relativno mirovanje | granica kvazistacionarne aproksimacije | cisterna i rotacijski separator | 8 |
| 5 | Sile na ravne i zakrivljene plohe | potpisani vektor sile i moment | poplavna vrata i brodski otvor | 11 |
| 6 | Uzgon i početni stabilitet | izračun GM i granica maloga kuta | ponton i offshore platforma | 10 |
| 7 | Kinematika, RTT i kontinuitet | fiksni/gibajući kontrolni volumen | razdjelnik rashladnog sustava | 10 |
| 8 | Energijska jednadžba i Bernoulli | izbor referentnih presjeka i tlaka | sifon, Venturi i pogonski dovod | 10 |
| 9 | Kompresibilni idealni tok | Mach, prigušenje i udarni val | dovod zraka i sigurnosni ventil | 9 |
| 10 | Količina i moment količine gibanja | sila, predznak i energetska provjera | koljeno, mlaz i pomični rotor | 10 |
| 11 | Dimenzijska analiza i sličnost | puni Buckinghamov postupak | model broda i hidroprofila | 9 |
| 12 | Diferencijalni realni tok | granični slučaj Poiseuille + mrežna konvergencija | granični sloj trupa i hlađenje | 10 |
| 13 | Gubitci, cjevovodi, crpke i mreže | iterativna radna točka i energetski ledger | hlađenje i urbana mreža | 12 |
| 14 | Turbostrojevi i propulzija | znak rada, trokut brzina i raspoloživa snaga | pumpa, turbina i propeler | 9 |
| 15 | Otvoreni tokovi | kritična dubina i hidraulički skok | klimatski otporan vodni grad | 9 |

## Minimalno poravnanje svakog ishoda

Svaki red matrice mora u studentskom izdanju imati:

1. temeljno objašnjenje ili izvod;
2. riješeni primjer s neovisnom provjerom;
3. kratko konceptualno pitanje;
4. samostalni zadatak bez unaprijed zadane formule;
5. eksplicitnu granicu modela;
6. poveznicu na numerički pokus kada numerika donosi novu spoznaju.

## Matrica samostalnih zadataka

Svako glavno poglavlje ima šest zadataka: `2 × T1`, `2 × T2`, `1 × T3` i `1 × T4`. T1 provjerava jedan zakon, T2 uvodi geometrijsku ili jediničnu odluku, T3 traži izbor/kombiniranje modela, a T4 uključuje podatke, nesigurnost, kompromis ili obrazloženu odluku. Modernizacija se provodi zamjenom slabijih zadataka, ne nekontroliranim dodavanjem.

## Graf preduvjeta

`U01–U02 → U03–U06 → U07 → U08 → U09/U10 → U11 → U12 → U13/U14/U15`

- Reynoldsov broj uvodi se kvalitativno u U02, formalizira u U11 i primjenjuje u U12–U14.
- Gibajući kontrolni volumen uvodi se u U07 prije lopatica i turbostrojeva.
- Korekcijski faktori količine gibanja i energije definiraju se prije prve brojčane uporabe.
- Otvoreni tokovi dolaze nakon Froudeove sličnosti i energijske/količinske bilance.

## Tri uzdužna lajtmotiva

Svaka ponovna pojava mora jasno navesti što se iz ranijeg modela zadržava i koja nova fizika ulazi:

- pomorska i offshore dekarbonizacija;
- hlađenje elektrificiranih i digitalnih sustava;
- klimatski otporan vodni grad.

Zajednički ritual je `izmjeri → idealiziraj → izračunaj → numerički provjeri → procijeni valjanost`.
