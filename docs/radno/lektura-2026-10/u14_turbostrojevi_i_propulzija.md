# Lektura: source/u14_turbostrojevi_i_propulzija.md (pog. 14)

Pregledana je cijela datoteka (900 redaka): uvod, teorija, tri izvoda, CFD blokovi,
interaktivni prikaz, granica modela, šest riješenih primjera, samoprovjera, Z1–Z6 s
naputcima i kontrolnim rezultatima, napomene uz skice, fig-alt opisi i završni okvir.
Izmijenjeno je oko 90 redaka u otprilike 95 zahvata. Svi su zahvati jezični.

## 1. Vrste izmjena

- **Upućivanja s krivim padežom ili bez imenice (11):** `@eq-…`/`[-@eq-…]` iza prijedloga
  ili u kosom padežu zamijenjeno je oblikom „jednadžba/jednadžbe/jednadžbi [-@…]”, a
  `@ex-propeler-u-napredovanju` oblikom „u primjeru [-@…]”. Dva nominativna `@ex-…`
  (r. 25 i 136, subjekt nakon točke sa zarezom) ostala su nepromijenjena.
- **Sročnost i padeži:** „se izvode ono što” → „se izvodi ono što”; „koje su plohe i
  gubitci” → „koje su plohe i koji gubitci”; „pri crtanju oba lokalna trokuta” → „pri
  crtanju obaju lokalnih trokuta”; „nije certificirana nosivost niti opis” → „nije ni … ni”.
- **Pravopis i tipfeleri:** „Ni jedan od dvaju” → „Nijedan od dvaju”; „u traci ostaje
  12 odnosno 22 kW” → „u tragu ostaje” (Z5, kontrolni rezultat); suvišan razmak prije
  `&nbsp;` u naslovu primjera s dronom; zarez ispred „jer” iza glavne rečenice uklonjen
  je na dva mjesta.
- **Red riječi i enklitike:** „Trokut brzina … je isti” → „… isti je”; „Oba uvjeta …
  su zadovoljena” → „Oba su uvjeta … zadovoljena”; „Vanjski dovodi su” → „Vanjski su
  dovodi”; „rotacijska akumulacija zanemaruje” → „rotacijska se akumulacija zanemaruje”.
- **Kalkovi i nespretni izrazi:** „sila koju fluid vrši” → „sila kojom fluid djeluje”;
  „turbinski izlaz” → „snaga koju fluid predaje rotoru”; „koliko snage stoji potisak” →
  „koliku snagu zahtijeva potisak”; „statički test” → „statičko ispitivanje”; „diskovna
  površina” → „površina diska”; „kompatibilni uvjeti” → „međusobno usklađeni uvjeti”;
  „predstavlja omjer” → „jest omjer”; „bez drugog energetskog ulaza” → „bez drugog dovoda
  energije”; „Relativni/Apsolutni izlaz (vektor)” → „relativna/apsolutna izlazna brzina”
  (5×); „rezultantni iznos” → „iznos rezultante” (2×); „kandidati A i B” → „varijante A
  i B” (usklađeno s „Za obje varijante” u istom zadatku); „u istoj skali” → „u istom mjerilu”.
- **Metafore i stil:** „velika brzina mlaza kupuje potisak” → „potisak dobiven velikom
  brzinom mlaza plaća se skupom kinetičkom energijom traga” (2×); „nastavak priče o
  plutanju” → „gradivo o plutanju”.
- **Rečenice bez glagola prije formula** („Površina diska pojedinog propelera:”,
  „Idealna mehanička snaga …:”, „Ukupna snaga …:”, „Računaju se redom …:”) pretvorene su
  u rečenice s „iznosi”, „slijedi” ili „dobiva se”.
- **Razbijene ili preslagane duge rečenice (4):** Provjera u izvodu aktuatorskog diska,
  Provjera i tumačenje u primjeru s propelerom, odgovor 2 u samoprovjeri i rečenica
  „Rezultat: dva optimuma”.

### Reprezentativni primjeri (prije → poslije)

1. „Ovdje se iz iste bilance izvode ono što je specifično za turbostrojeve” →
   „Ovdje se iz iste bilance izvodi ono što je specifično za turbostrojeve”
2. „Moment količine gibanja @eq-moment-kolicine-gibanja iz pog. 10 vrijedi s apsolutnom
   brzinom” → „Jednadžba momenta količine gibanja [-@eq-moment-kolicine-gibanja] iz
   pog. 10 primjenjuje se s apsolutnom brzinom”
3. „Što ulazi u $\dot m$, odlučuje o položaju maksimuma snage.” → „Položaj maksimuma
   snage ovisi o tome što ulazi u $\dot m$.”
4. „Ručni @ex-propeler-u-napredovanju koristi jednoliko opterećen disk” → „Ručni proračun
   u primjeru [-@ex-propeler-u-napredovanju] koristi jednoliko opterećen disk”
5. „Kolika je brzina kroz disk i koliko snage stoji zadani potisak” → „… i koliku snagu
   zahtijeva zadani potisak”
6. „Odredi horizontalne komponente sile koju fluid vrši na vodilicu.” → „… sile kojom
   fluid djeluje na vodilicu.”
7. „Uz $\beta_2=30^\circ$ [-@eq-…-04] daje $F_x=…$, isto kao komponentni račun.” →
   „Uz $\beta_2=30^\circ$ jednadžba [-@eq-…-04] daje $F_x=…$, jednako kao račun po komponentama.”
8. „Obje varijante daju … ; u traci ostaje 12 odnosno 22 kW” → „… u tragu ostaje 12 odnosno 22 kW”

### Jezične izmjene blizu sadržaja (radi provjere)

- R. 181 (izvod aktuatorskog diska): „Daleko ispred voda ima brzinu $v_A$” → „Daleko
  ispred diska fluid ima brzinu $v_A$”. Izvod je opći i u nastavku se primjenjuje na
  zrak (dron), pa je naziv „voda” zamijenjen nazivom „fluid”.
- Z6: „izbacuju vodu … brzinom $v=36$ m/s prema platformi” → „u odnosu na platformu”.
  Izvorni „prema” mogao se čitati kao smjer prema platformi, a smisao je relativna
  brzina, što potvrđuje i model $F_T=\rho Av^2$.
- Z2, Naputak: „veća pozitivna izlazna komponenta duž osi y” → „pozitivan prirast
  komponente brzine duž osi y” (ulazna je komponenta nula, pa je smisao isti).

## 2. Sadržajni nalazi koji nisu ispravljeni

1. **R. 133 (Provjera u Eulerovu izvodu):** „To je isti izraz kao umnožak $F_xu$ sile na
   pokretnu lopaticu iz jednadžbe [-@eq-turbostrojevi-razrada-koraka-04] …”.
   Jednadžba -04 sadrži $\dot m_{rel}$, a Eulerov izraz -05 sadrži puni $\dot m$. Izrazi su
   jednaki samo kad se $\dot m_{rel}$ zamijeni sapničkim protokom, tj. za kolo, a ne za jednu
   lopaticu. Predlažem da se to u tekstu kaže izričito, jer je upravo to središnja
   poruka poglavlja.
2. **R. 142 (CFD, crpka):** „razlika otkriva nekonvergiranu mrežu ili propuštanje kroz
   spoj okvira”. Mreža ne konvergira, nego rješenje, a na mreži se provjerava neovisnost
   rješenja. Osim toga, $P=M\omega$ integriran po rotoru i Eulerov tok između presjeka
   razlikuju se i fizikalno (trenje diska, propuštanje kroz procjepe), ne samo zbog
   numeričke pogreške.
3. **R. 536 (radijalno kolo):** „stvarnu visinu reda $0{,}82\cdot27{,}8\approx22{,}8$ m”.
   Faktor 0,82 uveden je bez izvora i bez imena (hidraulička učinkovitost i faktor
   klizanja zajedno?). Predlažem da se imenuje ili izričito označi kao pretpostavljen.
4. **R. 644 (dron):** oznaka $P_{st}$ za stvarnu snagu na vratilu. Indeks „st” je u
   tablici notacije zauzet za stijenku ($\tau_{st}$). Sukob je blag, ali vrijedi
   razmotriti oznaku poput $P_{vr}$ ili $P_{stv}$ (formula nije mijenjana).
5. **R. 655 (dron, provjera):** $1{,}045\cdot0{,}0616\cdot6{,}76\cdot13{,}5$ uz prikazane
   zaokružene faktore daje 5,87 N, a ne 5,89 N. Vrijednost 5,89 dobiva se samo iz
   nezaokruženih podataka. Uvodna napomena o zaokruživanju to pokriva, ali čitatelj koji
   ponovi račun dobit će drukčiju zadnju znamenku.
6. **R. 236 / r. 246 (vodilica mlaza):** u tekstu zadatka sapnica je „visoka
   $h = 14$ mm”, a u bilješci „Veza s proračunom” ista se veličina zove „Dubina
   $h=14\,\mathrm{mm}$”. Riječ je o sitnoj terminološkoj nedosljednosti koja nije mijenjana,
   jer bilješka opisuje skicu.
7. **R. 154 (interaktivni prikaz):** „Nastavci obrađuju Z3–Z5”. Bez bilježnice
   `u12_pelton_lopatica.ipynb` nisam mogao provjeriti odgovaraju li nastavci stvarno
   zadatcima Z3 (izlaz lopatice iz sile), Z4 (dva polumjera) i Z5 (vodomlazni pogon).
8. **Informativno:** u pog. 14 i dalje se koriste ID-jevi i datoteke s prefiksom `u12_`
   (`fig-uvod-u12`, `u12_*.svg`, `u12_pelton_lopatica.ipynb`, `task-u12-…`). To je
   naslijeđe iz prijašnje numeracije, a ID-jevi su stabilni, pa ništa nije mijenjano.
   Naslov Z4 „Dva radijusa i rad rotora” mogao bi postati „Dva polumjera …”, kako tekst
   inače piše. Nije mijenjan jer bi tražio regeneraciju D06 i indeksa.

Svi računski rezultati u primjerima i kontrolnim rezultatima (P1–P6, Z1–Z6) ručno su
provjereni i podudaraju se s podatcima, uz odstupanja samo u zadnjoj znamenci zbog
zaokruživanja.

## 3. Provjere

- `lektura_check.py source/u14_turbostrojevi_i_propulzija.md`: **ok** (bez redaka STROGO,
  numbers i refs).
- `tools/check_u14_sketch_geometry.py`: **U14 SVG PASS** (7 slika).
- `tools/audit_publication.py`: **Publication audit PASS** (U14: primjeri=6, zadatci=6
  [T1,T1,T2,T2,T3,T4]).
