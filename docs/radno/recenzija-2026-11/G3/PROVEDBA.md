# Provedba potvrđenih tekstnih ispravaka skupine G3 (pog. 9–12)

Provedba 8. 11. 2026. prema [PROVJERA.md](PROVJERA.md). Provedene su samo stavke sa
statusom POTVRĐENO, težinom P2 (ili P3 spuštenom iz P2) i vrstom TEKST. Kod
mješovitih stavki proveden je samo tekstni dio koji ne mijenja broj, rezultat ni
oznaku koju koriste ključ ili verifikator. Mijenjani su samo `source/u09`–`u12`.
Retci se odnose na stanje prije provedbe (kao u PROVJERA.md).

## Tablica stavki

| ID | Mjesto | Status | Napomena |
| --- | --- | --- | --- |
| G3-01 | `u10` Z5 | NEPRIMJENJIVO | Z5 je već preoblikovan u zadatak s kočenim kolicima (commit 5d10524). |
| G3-02 | `u10:857` P7 | NEPRIMJENJIVO | P1; već ispravljeno u commitu f6679af (440 W predaje dovod, 369 W nosi mlaz). |
| G3-03 | `u12:3` | NEPRIMJENJIVO | P1; već ispravljeno u commitu f6679af (konstitutivna veza za jednostavno smicanje). |
| G3-04 | `u10:224` P1 | PROVEDENO | Kut od 15° sada se mjeri „sa smjerom suprotnim dolaznom mlazu”; 165° i račun nepromijenjeni. |
| G3-05 | `u10` Z3, kontrolni rezultat | PROVEDENO | Dodan `data-key-full="true"`; tekst odgovora nepromijenjen, D06 treba obnoviti generatorom. |
| G3-06 | `u12` Z3 | PRESKOČENO | BROJ/MODEL. |
| G3-07 | `u09` Z2, Z4 | PRESKOČENO | AUTORSKA ODLUKA. |
| G3-08 | `u11` P6 | PRESKOČENO | AUTORSKA ODLUKA (proširenje opsega na primjere). |
| G3-09 | `u12` P4 | PRESKOČENO | AUTORSKA ODLUKA. |
| G3-10 | `u11` Z5, P5 | PRESKOČENO | AUTORSKA ODLUKA. |
| G3-11 | `u11:668`, `u11:707–710` P6 | PROVEDENO | $St\approx0{,}2$ označen kao nastavna projektna procjena, a u Provjeri dodan $Re\approx1{,}6\cdot10^6$ i $8{,}0\cdot10^5$ izvan potkritičnog područja; tvrdnja o normi (nepotvrdiva) nije unesena. |
| G3-12 | `u11:143–155` | PROVEDENO | Tablica ima potpis i `{#tbl-bezdimenzijski-brojevi}`, a tekst upućuje brojem. |
| G3-13 | `u11:143` | PROVEDENO | Ručni span zamijenjen s „u dodatku A”. |
| G3-14 | `u10:11` sl. 10.1 | PRESKOČENO | SKICA. |
| G3-15 | `u11:494` sl. 11.4 | PRESKOČENO | SKICA. |
| G3-16 | `u11` Z1 ($a$, $b$) | PRESKOČENO | Prijedlog traži i promjenu skice Z1; oznaka $a$ stoji i u zahtjevu 3, pa bi sama tekstna izmjena razdvojila tekst i skicu (K6). |
| G3-17 | `u10:122–133`, `u11:303` | PROVEDENO | Natuknice pog. 10 premještene ispred bloka, a blok ima dvije rečenice; zagrada o $1+k$ prenesena u tekst iza `eq-ittc-1957`. |
| G3-18 | `u12:683` Z6 | PROVEDENO | GCI raspisan pri prvom spomenu (engl. *grid convergence index*), a put `data/cfd/…` zamijenjen s „iz dodatka D”. |
| G3-19 | `u12:264`, `u12:527` | PROVEDENO | Uz jednadžbu navedeno da je $\tau_{st}$ naprezanje fluida na stijenku uz os $y$ od stijenke u fluid; napomena Z2 govori o iznosu. |
| G3-20 | `u10:712` P5 | PROVEDENO | „mogla bi biti usporediva s nesigurnošću mjerenja sile, koja ovdje nije zadana”. |
| G3-21 | `u11:91` | PRESKOČENO | NEPOTVRDIVO. |
| G3-22 | `u10:797` P7 | PRESKOČENO | NEPOTVRDIVO / AUTORSKA ODLUKA. |
| G3-23 | `u10:7` | PROVEDENO | „koljena i račve u cijevnim sustavima brodova i kopnenih postrojenja”. |
| G3-24 | `u12` P2 | PRESKOČENO | NEPOTVRDIVO / AUTORSKA ODLUKA. |
| G3-25 | `u10:159` | PROVEDENO | Navedeno da je $\dot m(v_j^2-v_s^2)/2$ u sustavu broda i da je u sustavu obale ista snaga $F_Tv_s+\dot m(v_j-v_s)^2/2$; učinkovitost nepromijenjena. |
| G3-26 | `u10:1063` Z6 | PROVEDENO | „RSS” zamijenjen s „ne zbrajaju se korijenom zbroja kvadrata”. |
| G3-27 | `u09:7`, `u09:132` | PROVEDENO | Uklonjena rečenica o pretpostavkama u uvodu (stoji u Granici modela `u09:460`) i drugi „4,4 %” u P2 (ostaje u `u09:106`). |
| G3-28 | `u09:106`, `u09:362` | PROVEDENO | „kalorički savršenog plina”. |
| G3-29 | `u09:137`, `u09:139` | PROVEDENO | Upućivanja na rashladni krug (pog. 7) i Venturijevu cijev (pog. 8) preko `mf1-chapter-ref`. |
| G3-30 | `u09:445` | PROVEDENO | „iteracija, zahtjevnija od razine ovog primjera”; autorica treba potvrditi značenje. |
| G3-31 | `u10:3`, `u10:27` | PROVEDENO (djelomično) | Uklonjena ponovljena rečenica o trećem Newtonovu zakonu u okviru; jednadžba u uvodu zadržana prema autorskoj odluci od 15. 10. 2026. |
| G3-32 | `u10:74` | PROVEDENO | „No oblik iz jednadžbe [-@eq-momentum-numericki-trag-01] nije dovoljan …”. |
| G3-33 | `u10:91`, `u10:452` | PROVEDENO | Odjeljak dobio `{#sec-u10-provjera-sile-na-koljeno}`; P3 upućuje brojem, u prvom licu množine. |
| G3-34 | `u10:708` | PROVEDENO | „proračunani režim”. |
| G3-35 | sl. 10.9 Z3 | PRESKOČENO | SKICA. |
| G3-36 | `u11:15`, `u12:15` | PROVEDENO | Naslovi „Svrha bezdimenzijskog opisa” i „Od integralne do lokalne bilance”; `sec-realni-tok-motivacija` zadržan. Jednorečenični okvir `u11:42` ostao je radi strukture blokova. |
| G3-37 | `u11:3`, `u11:5` | PROVEDENO (djelomično) | Iz uvoda uklonjena doslovno ponovljena definicija $n-k$ i rečenica „jedna grupa nije dovoljna” (ostaje u `u11:42`); definicije brojeva u uvodu zadržane prema autorskoj odluci. |
| G3-38 | `u11:34`, `u11:47` | PROVEDENO | Mjerilo tlačne sile je $F_{\Delta p}$; $F_p$ ostaje samo sila prototipa. |
| G3-39 | `u11:107` | PROVEDENO | „potkritičnom području”. |
| G3-40 | `u11:122` | PROVEDENO | „$K$ volumni modul”. |
| G3-41 | `u11:286`, `u12:306` | PROVEDENO | ITTC raspisan u pog. 11 (Međunarodna konferencija pokusnih bazena, engl. *International Towing Tank Conference*); u pog. 12 dodano upućivanje na pog. 11. Unos u pojmovnik je PREPUŠTENO G4. |
| G3-42 | `u11:541` | PROVEDENO | „kavitacijska rezerva ($NPSH$, pog. 13)”. |
| G3-43 | `u11:796` Z2 | PROVEDENO | Rečenica od 44 riječi podijeljena na tri; jednadžba ostaje u retku. |
| G3-44 | `u12:7` | PROVEDENO (djelomično) | U uvodu ostaje samo opća rečenica o pretpostavkama; jednadžbe u `u12:3` zadržane prema autorskoj odluci. |
| G3-45 | `u12:139` | PROVEDENO | Rečenica od 47 riječi podijeljena na tri. |
| G3-46 | `u12:366` | PROVEDENO | RANS pridružen osrednjenim jednadžbama punim nazivom; rečenica o modelima podijeljena. |
| G3-47 | `u12:368` | PROVEDENO | „$Re$ iz pog. 11” preko `mf1-chapter-ref`. |
| G3-48 | `u12:631` Z4 | PROVEDENO | $\tau_0=\mu\,(dv/dy)_{y=0}$. |
| G3-49 | `u10:95` | PROVEDENO | „može pokazati”. |
| G3-50 | `u10:1061`, `u10:1069`, `u11:945` | PROVEDENO | „nominalni” zamijenjen s „nazivni”. |
| G3-51 | `u12:304` P4 | PROVEDENO | Pri prvom spomenu „$\delta_B$ (Blasiusova procjena $\delta_{99}$)”. |
| G3-52 | `u11:826` Z3 | PRESKOČENO | NEPOTVRDIVO. |
| G3-53 | pog. 9–12 | PRESKOČENO | AUTORSKA ODLUKA. |
| G3-54 | `u12` Z3 | PRESKOČENO | ODBAČENO. |

Ukupno: PROVEDENO 36 (od toga 3 djelomično), PRESKOČENO 15, NEPRIMJENJIVO 3,
PREPUŠTENO G4 0 samostalnih stavki (unos ITTC u pojmovnik `d02` uz G3-41).

## Ispis `--usporedi HEAD` (sažeto)

`PYTHONUTF8=1 python tools/prirucnik_stats.py --usporedi HEAD` nad četirima izvorima:

| Izvor | Izgubljeni brojevi | Dodani brojevi | ID-jevi | Ocjena |
| --- | --- | --- | --- | --- |
| `u09` | 0,3; 4,4 | — | — | Namjerno (G3-27): ista tvrdnja ostaje u `u09:106`. |
| `u10` | — | 2; 2 | dodan `sec-u10-provjera-sile-na-koljeno` | Brojevi 2 iz $2v_s/(v_j+v_s)$ i $/2$ samo su premješteni u novu rečenicu (G3-25). |
| `u11` | — | 0,2; 12; 2; 3; 5; 5; 6; 6; 6,0; 8,0 | dodan `tbl-bezdimenzijski-brojevi` | Namjerno: $Re$ dimnjaka u P6 (G3-11), $F_{\Delta p}$, ITTC 1957/1978 premješten iz Granice modela. |
| `u12` | — | 99 | — | Indeks iz $\delta_{99}$ (G3-51). |

Prijavljene promjene nijekanja i ograda pročitane su i namjerne:

- `u10`: „može pokazati” (G3-49), „nije zadana” (G3-20), „ne zbrajaju se” (G3-26).
- `u11:5`: izgubljeni „nije” i „samo” iz „Jednaka vrijednost samo jedne grupe nije
  dovoljna”, jer ista tvrdnja ostaje u okviru `u11:42`; ograda „samo ako” u istoj
  rečenici je sačuvana.
- `u11:303`: izgubljena dva „ne” premještena su s rečenicom o $1+k$ iza `eq-ittc-1957`.
  „radna je hipoteza, a ne zakon” ostaje u bloku.
- `u12:7`: „bez” i „potpuno” izgubljeni su s popisom pretpostavki. Popis ostaje u
  `u12:114` (newtonski fluid, konstantni $\rho$ i $\mu$), `u12:225` (stacionaran,
  potpuno razvijen laminarni tok) i `u12:276` (glatka ravna ploha, nulti gradijent tlaka).

`--nalazi` za sva četiri izvora ne prijavljuje nijedan nalaz. Nijedna rečenica nije
dulja od 40 riječi.

## Izvršene provjere i preostali koraci

- `tools/audit_publication.py`: PASS.
- `tools/audit_architecture.py`: FAIL samo zbog zastarjelog `source/d06_kljuc_kontrolnih_rezultata.md`,
  što se očekuje nakon G3-05. Potrebno je `python scripts/build_book.py --write`.
- Generirani manifest (`tools/verification_manifest.json`) sadrži tekst zadataka
  (npr. pog. 10 Z6, pog. 11 Z2, pog. 12 Z4 i Z6) pa ga treba obnoviti generatorom.
  Isto vrijedi za `assets/content-index.json` (novi ID-jevi i naslovi odjeljaka).
- Verifikatori nisu pokretani jer nijedan broj zadatka ni ključa nije promijenjen.

## Otvorena pitanja za autoricu

- G3-30: značenje „zahtjevnija od razine ovog primjera” treba potvrditi.
- G3-19: `u12:518` piše $\tau_{st}=\mu\,dv/dr|_R$, s osi $r$ od osi cijevi prema stijenci.
  Uz konvenciju uvedenu kod jednadžbe za $\tau_{st}$ (os $y$ od stijenke u fluid) taj
  izraz ima suprotan predznak. Rezultat se ne mijenja jer se ondje rabi nagib.
  Predlaže se `|\mu\,dv/dr|_R|` ili napomena.
- G3-37 i G3-36: jednorečenični okvir **Fizikalno značenje** (`u11:42`) i dalje
  ponavlja smisao uvoda. Uklanjanje bloka mijenja strukturu i nije provedeno.
- G3-11: čitateljev podatak o EN 1991-1-4 ($St\approx0{,}18$) nije u tekstu i nije provjeren.
  Ako autorica želi normativni podatak umjesto oznake nastavne procjene, treba izvor iz dodatka E.
