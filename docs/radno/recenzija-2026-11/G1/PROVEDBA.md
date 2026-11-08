# Provedba potvrđenih tekstnih ispravaka — skupina G1 (pog. 1–4)

Provedeno 8. 11. 2026. prema `PROVJERA.md` iz ove mape. Opseg: stavke sa
statusom POTVRĐENO, težinom P2 (ili P3 sniženom iz P2) i vrstom ispravka
TEKST; kod mješovitih stavki samo tekstni dio koji ne mijenja broj, rezultat
ni oznaku iz ključa ili verifikatora. Mijenjani su samo
`source/u01_…`, `source/u02_…`, `source/u03_…` i `source/u04_…`
(završetci redaka CRLF sačuvani). Generatori s `--write` nisu pokretani, a
commit nije napravljen.

**Sažetak statusa:** PROVEDENO 32 (od toga djelomično 2: G1-10, G1-11),
PRESKOČENO 13, PREPUŠTENO G4 1 (dio G1-20), NEPRIMJENJIVO 0.

## Tablica

| ID | Mjesto | Status | Što je učinjeno ili zašto nije |
| --- | --- | --- | --- |
| G1-01 | `u04` Z2, skica | PRESKOČENO | P1, autorska odluka i skica. |
| G1-02 | `u01:7`, `u01:183` | PROVEDENO | U uvodu i izvodu piše da je porast tlaka isti točno, za bilo koji $\Delta z$, a $\rho g\Delta z$ se zanemaruje samo u ravnoteži ukupnih sila na klipovima; „praktički” uklonjen. |
| G1-03 | `u02:68` | PROVEDENO | „Gradijent ne mora biti stalan” zamijenjen: gradijent je stalan ako naprezanje ovisi samo o lokalnom gradijentu; newtonski model tvrdi isti omjer pri svim brzinama. |
| G1-04 | `u03` P5 (Traži se 4, korak 4) | PROVEDENO | „Ulaž” u balastnom tanku zamijenjen s „visina praznog prostora iznad balasta”; vrijednost 2,0 m ostaje. |
| G1-05 | `u04` Granica modela | PROVEDENO | Upućivanje na kapilarnu duljinu premješteno s pog. 2 na pog. 11 i dodatak A. |
| G1-06 | `u01` Z2, Traži se 2 | PROVEDENO | Dodano „u srednjem položaju kormila”; ključ i verifikator nisu dirani. |
| G1-07 | Z1–Z6 više poglavlja | PRESKOČENO | Autorska odluka (ciklus revizije zadataka). |
| G1-08 | `u01`, `u02`, `u03`, `u04` Granica modela | PROVEDENO | u01: teorija modula $K$ s jednadžbom `eq-modul-stlacivosti-volumna-promjena` (ID nepromijenjen) premještena kao običan tekst neposredno ispred bloka, bez novog bloka ili naslova; blok ima tri rečenice. u02: četiri pretpostavke dane kao popis. u03 i u04: uvodna rečenica i popis uvjeta prestanka; sadržaj nije skraćen. |
| G1-09 | `u01:141`, `u03:206`, `u04:179` | PROVEDENO | Naslovi „Utjecaj stlačivosti na pomak klipa”, „Nizak tlak na usisu i referenca tlaka”, „Coriolisova sila u relativnom mirovanju”. |
| G1-10 | `u03` P1 i P4 (međurezultati) | PROVEDENO (djelomično) | Međurezultati u u03 na četiri značajne znamenke (132 500 Pa, 31 700 Pa, −20 480 Pa, 80 820 Pa); konačni rezultati nepromijenjeni. Dio za ključ u04 (Z5, Z6) je BROJ/MODEL i preskočen. |
| G1-11 | `u04:3`, `u04:9` | PROVEDENO (djelomično) | U uvodu i opisu sl. 4.1 piše „mjera spremnika prema središtu zavoja” umjesto „duljina”; oznaka $L$ zadržana jer stoji na slici, a zamjena s $b_t$ i skica ostaju za SKICA. |
| G1-12 | `u02` P5 | PRESKOČENO | BROJ/MODEL. |
| G1-13 | `u02` P5 | PRESKOČENO | NEPOTVRDIVO, autorska odluka. |
| G1-14 | `u04` P3 (r. 389, 400, Provjera 2) | PROVEDENO | Dodano „uz pretpostavku broda bez nagiba”; Provjera 2 podijeljena na tri rečenice: u ustaljenom zavoju nagib prema van zbraja se s 1,24° i povećava razliku razina, uz uputu na pog. 6. |
| G1-15 | `u01` P1–P6 | PRESKOČENO | Autorska odluka (proširenje opsega na P1–P6). |
| G1-16 | `u03` P2, korak 1 | PROVEDENO | Slaganje „unutar 1 mm” zamijenjeno slaganjem unutar nesigurnosti pretvornika (nekoliko centimetara) i napomenom da je podudaranje na milimetar posljedica složenih podataka. |
| G1-17 | `u03` P2, Provjera 2 | PROVEDENO | Dodana rečenica o gustoći $\rho_u$ pri temperaturi tereta (koeficijent reda $8\cdot10^{-4}$ 1/K, 10 K daje oko 0,1 m), označena kao nastavna procjena. |
| G1-18 | `u03` P2 | PRESKOČENO | NEPOTVRDIVO (ISGOTT bez izvora). |
| G1-19 | `u03` P5 | PROVEDENO | Tank nazvan „donji bočni balastni tank (nastavno pojednostavnjenje)” u tekstu zadatka (naslov i ID nepromijenjeni); u Provjeri 1 dodana rečenica da bi iznad vodne linije neto tlak $\rho_{mv}g(H_{tk}-z)$ tlačio oplatu prema van. |
| G1-20 | `u02:577`, `u03:416`, `u03:712` | PROVEDENO | Tvrdnje o praksi označene kao nastavna procjena (ulje statvene cijevi, postupak pri ljuljanju i trimu, kut 5–10°). |
| G1-20 (dio) | `d05_literatura.md` | PREPUŠTENO G4 | Dodavanje McGeorgea i Taylora u dodatak E nakon provjere izdanja. |
| G1-21 | `u01` P2 | PROVEDENO | „upravljački klip” → „crpni klip”. |
| G1-22 | `u01:5`, `u02:23`, `u03:65`, `u03:190`, `u04:19` | PROVEDENO | Izbrisane doslovno ponovljene rečenice i zagrada s $p_{vak}$ (jednadžba `eq-hidrostatika-fizikalno-znacenje-03` ostaje); formule u uvodu nisu dirane (autorska odluka). |
| G1-23 | `u01` izvod; `u04:23`; `u04:114` | PROVEDENO | Ponovljene istaknute formule pretvorene u formulu u retku s upućivanjem na preostalu jednadžbu. Uklonjeni ID-jevi `eq-svojstva-tlak-matematicki-izvod-pascalov-zakon-i-ocuvanje-rada-03`, `eq-relativno-mirovanje-fizikalni-uvod-i-matematicki-izvod-01` i `eq-relativno-mirovanje-razrada-koraka-03` nemaju upućivanja u `source/` (javljaju se samo u generiranom `assets/content-index.json`). Citirani `…-fizikalno-znacenje-08` zadržan. |
| G1-24 | `u02:340`, `u03:821`, `u04:232` | PROVEDENO | „kasnije” i „u sljedećem poglavlju” zamijenjeni oznakama poglavlja (u11, u04); treća najava pog. 5 u `u04:232` izbrisana. |
| G1-25 | `u01:169` | PROVEDENO | „usporedi” → „usporedimo”. |
| G1-26 | `u01` P1, P2, P3; `u04` P2 | PROVEDENO | Četiri potpisa slika zamijenjena opisnim rečenicama koje ne ponavljaju `fig-alt`. |
| G1-27 | `u02:176` | PROVEDENO | „…daje referentni test za takav CFD model:”. |
| G1-28 | `u02:333`, `u02:625`, `u02:780` | PROVEDENO | „nadtlak” → „pretlak” (u r. 780 u kontrolnom rezultatu Z4, bez promjene broja). Pog. 5 i dodatci nisu dirani. |
| G1-29 | `u03:160`, `u04:181`, `u04:413` | PROVEDENO | Pravilo hoda i tri člana prividnih sila dani kao popis; `u04:413` podijeljen na tri rečenice (s G1-14). Alat sada nalazi 0 rečenica iznad 40 riječi u pog. 1–4. |
| G1-30 | `u02` $h_{cap}$ | PRESKOČENO | TEKST + SKICA: oznaka stoji u skici i ključu; zamjena samo u tekstu narušila bi K6. |
| G1-31 | `u03:149`, `u03:190` | PROVEDENO | „Najčešća” → „Česta” uz primjer (zatvoreni spremnik, usporedba s $p_v$); rečenica o piezometarskoj visini odvojena u novi odlomak; zadnja rečenica r. 190 izbrisana. |
| G1-32 | `u03:68`, `u03:156`, `u03:189`; `u04:40`, `u04:95` | PROVEDENO | Podnaslovi „Gradijent tlaka i težina fluida”, „Piezometarska visina”, „Reference tlaka”, „Efektivno polje sila”, „Tlak u rotirajućem fluidu”. |
| G1-33 | `u03:166` | PROVEDENO | Uz $\rho_{mv}g(T-H_{tk})$ dodano upućivanje na primjer i značenje $T$ i $H_{tk}$. |
| G1-34 | `u03:329` | PROVEDENO | „…u vodu kojim teče slatka voda”. |
| G1-35 | `u03:459` | PROVEDENO | $NPSH_a$ i $NPSH_r$ imenovani pri spomenu, s upućivanjem na pog. 13. |
| G1-36 | `u03:534`, `u03:538` | PROVEDENO | „IoT” → „umreženi tlačni senzor” u naslovu i tekstu; ID `ex-u03-iot-…` nepromijenjen. |
| G1-37 | `u03:712` (ključ Z3) | PROVEDENO | „horizontiranje” → „vodoravno postavljanje instrumenta”. |
| G1-38 | adapter `filters/mf1-components.lua` | PRESKOČENO | Izmjena adaptera, izvan dopuštenih datoteka. |
| G1-39 | `u03` Z3, Traži se 3 | PROVEDENO | Dodano „(očitanje je razlika razina dvaju krakova)”. |
| G1-40 | `u03` Z6 | PRESKOČENO | BROJ/MODEL. |
| G1-41 | `u03:143–211` | PRESKOČENO | Autorska odluka (novi odjeljak i ID). |
| G1-42 | `u03:817–821` | PRESKOČENO | Autorska odluka. |
| G1-43 | `u03` P2 | PRESKOČENO | BROJ/MODEL. |
| G1-44 | `u03:459` | PROVEDENO | Rečenica o izdvajanju otopljenoga zraka i potopljenom usisu, označena kao nastavna procjena. |
| G1-45 | `u02` P5 | PRESKOČENO | NEPOTVRDIVO. |

## Ispis `--usporedi HEAD` (sažeto)

Naredba: `PYTHONUTF8=1 python tools/prirucnik_stats.py --usporedi HEAD source/u01_… source/u02_… source/u03_… source/u04_…`.

| Izvor | Izgubljeni brojevi | Dodani brojevi | ID-jevi i formule |
| --- | --- | --- | --- |
| u01 | — | — | izgubljen `eq-…-ocuvanje-rada-03` (G1-23); istaknute formule 51 → 50 |
| u02 | — | — | — |
| u03 | 132506,532 (2×), 31706,532, 20483,28 (alat prijavljuje i „28”), 80816,72 (G1-10); 1 (mm, G1-16) | 132500 (2×), 31700, 20480, 80820 (G1-10); 0,1, 10 i 8 (G1-17); 2, 3, 4 su brojevi stavki popisa (G1-29) | — |
| u04 | 2, 2 (eksponent i nazivnik iz formule pretvorene u formulu u retku, G1-23) | 1,24 (G1-14, ponavlja postojeći kut) | izgubljeni `eq-relativno-mirovanje-fizikalni-uvod-i-matematicki-izvod-01`, `eq-relativno-mirovanje-razrada-koraka-03` (G1-23); istaknute formule 50 → 49 |

Prijavljene promjene nijekanja i ograda pročitane su i namjerne: izbrisane
ponovljene rečenice (G1-22), ispravljena tvrdnja „ne mora biti” (G1-03),
dodano „ne mijenja” (G1-02), „samo do prvog praga” sada glasi „prestaje
vrijediti nakon prvog praga” (G1-08) i dodano „bez nagiba” (G1-14). Konačni
rezultati, kontrolni rezultati i podatci zadataka nisu promijenjeni.

`--nalazi` za sva četiri izvora: 0 nalaza. Profil: 0 rečenica iznad 40 riječi,
sve istaknute formule numerirane (201/201).

## Ograničenja i preostali koraci

- Ovo je autorska procjena jednog agenta; alat ne dokazuje da je značenje sačuvano.
- Tekst samostalnih zadataka i kontrolnih rezultata promijenjen je u u01 Z2, u02 Z4
  (ključ), u03 Z3 (zahtjev i ključ). Manifest, D06, indeks objekata i omotače treba
  obnoviti generatorima (`scripts/build_book.py --write` i generator manifesta),
  a zatim pokrenuti puni objavni CI. To nije učinjeno.
- Ostale nesigurnosti: G1-08 za u03 i u04 provedeno popisom umjesto skraćivanja
  na tri rečenice; G1-19 počiva na fizici, a tipičnost tanka ostaje nepotvrdiva;
  G1-11 ostaje nedovršen dok se ne uskladi sl. 4.1.
- Render (web i PDF) nije pokretan, pa prikaz popisa u blokovima i formula u
  retku nije vizualno provjeren.
