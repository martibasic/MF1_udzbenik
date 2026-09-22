# Revizija U15 — otvoreni tokovi

## Dijagnoza i matrica prije provedbe

Pročitani su kanonski izvor, svih pet primjera i šest zadataka, verifier
`verify_u15_open_channels.py`, notebook i jedina postojeća SVG referenca.
Kurikularni ishod traži kritičnu dubinu i hidraulički skok, uz kontrolni
presjek, granice 1D modela i numerički pokus.

| Mjesto | Postojeći ID i uloga | Odluka i didaktička korist | Razina | Završni ID | Povezane datoteke/provjere | Status |
| --- | --- | --- | --- | --- | --- | --- |
| P1 | `ex-rezim-retencijski-kanal`; v i Fr pravokutnog kanala | ZADRŽATI osnovni izravni račun i vezu s prijenosom poremećaja | T1 | isti | verifier | planirano |
| P2 | `ex-kriticni-preljev`; minimum energije | ZADRŽATI; provjeriti zaokruživanje minimalne energije | T2 | isti | verifier | planirano |
| P3 | `ex-dvije-dubine`; numerički korijeni E(y) | ZADRŽATI kao vođeni postupak dviju grana | T2 | isti | notebook, verifier | planirano |
| P4 | `ex-hidraulicki-skok-bazen`; spregnute dubine i disipacija | ZADRŽATI; bilanca količine gibanja i ograničenje duljine bazena jasno su navedeni | T3 | isti | verifier | planirano |
| P5 | `ex-manning-osjetljivost`; kapacitet i hrapavost | ZADRŽATI kao jednostavan uvod u osjetljivost n | T3 | isti | verifier | planirano |
| Z1 | `task-otvoreni-fr`; v i Fr | ZADRŽATI osnovnu tehniku; dopuniti smjer i brzine obaju valova te naputak | T1 | isti | SVG, verifier, D06 | planirano |
| Z2 | `task-kriticna-dubina`; yc i Emin | ZADRŽATI jednostavnu primjenu minimuma, jasno navesti pravokutni kanal i model | T1 | isti | SVG, verifier, D06 | planirano |
| Z3 | `task-trapezni-presjek`; geometrija A/T/P i Fr | ZADRŽATI: razlikovanje Dh i Rh nije ponavljanje pravokutnih primjera; dodati stvarno kotiran trapez | T2 | isti | SVG, verifier, D06 | planirano |
| Z4 | `task-alternativne-dubine`; ponovno dva korijena E(y) | ZAMIJENITI: podkritični dotok preko povišenog dna, dopuštena visina i izbor ostvarene grane | T2 | `task-kontrolni-presjek-na-pragu` | stari alias, SVG, notebook, verifier, D06 | planirano |
| Z5 | `task-skok-mjerenje`; sintetička mjerenja, R i uR | ZADRŽATI dijagnostiku; naglasiti zajednički q u oba presjeka, sintetičke podatke i ograničenje zaključka | T3 | isti | SVG, notebook, verifier, D06 | planirano |
| Z6 | `task-klimatski-kanal`; tri stanja održavanja, kapacitet i bazen | ZADRŽATI integraciju i kompromis; razjasniti kriterij n+2un, zadano ulazno stanje bazena i potpunost D06 | T4 | isti | SVG, notebook, verifier, D06 | planirano |

Matrica iznad čuva odluke zapisane prije provedbe; sve su provedene i
provjerene kako je navedeno u rezultatima ispod.

`rewrite_status`: complete; `rewrite_level`: selective;
`sketch_requirement`: popravak uvoda i nova zajednička skica šest vježbi.
Novi Z4 je autorski nastavni primjer. Izvorni P/Z i SVG spremljeni su prije
izmjena u ignoriranu radnu kopiju radi usporedbe.

## Početni nalazi

- Z4 ponavlja P3 u zakonu, izboru korijena i matematičkom postupku; nova
  visina dna uvodi vezu geodetske i specifične energije i granicu uspora.
- Ostali Z imaju smislene različite uloge. Nema razloga za njihovu potpunu
  zamjenu samo radi novosti. Ostaje pet primjera i šest ugovorenih mjesta.
- Uvodna skica ima brzinsku strelicu preko uzdignutog dna i crvenu krivulju
  skoka koja izlazi u zrak bez fizikalnog značenja. Presjeci, dubine i
  režimi nisu potvrđeni istim q i energijskom bilancom.
- Za trapezni kanal i skok nedostaju skice: nužno je razlikovati slobodnu
  širinu od omočenog opsega i nacrtati suprotne hidrostatičke sile.
- Z1/Z2 nemaju naputke, a odgovor Z1 ne daje traženi smjer poremećaja.
- D06 sažima duge formulacije i kontrolne rezultate; potrebno je sačuvati
  cijeli zaključak Z6 i provjeriti da se formule ne prekidaju.
- Notebook ima dobru jezgru P3/P4 i neovisnu propagaciju nesigurnosti,
  ali završava tvrdnjom umjesto interpretacijskim pitanjima i ne reproducira
  podatke mjernog Z5 ni odluku Z6. Zadržati jezgru i povezati nastavke.

## Rezultati

Zadržano je pet riješenih primjera i šest vježbi raspodjele
T1/T1/T2/T2/T3/T4. P2 dobiva ispravno zaokruženu minimalnu energiju
1,112 m iz nezaokružene kritične dubine. Z4 zamijenjen je autorskim zadatkom
o povišenju dna; stara poveznica `task-alternativne-dubine` ostaje alias.
Ostale vježbe zadržavaju svoje računske jezgre uz jasnije pretpostavke,
potpune naputke i tumačenje rezultata.

Za Z4, uz q = 2,20 m²/s, uzvodnu dubinu 1,200 m i prag 0,120 m,
granično je povišenje 0,186042 m, a ostvarena dubina na tjemenu
1,009009 m i Fr = 0,6930. Provjereni su energijski rezidual objavljenog
zaokruživanja, nulti prag, kritična granica i odbijanje previsokog praga.
Z5 propagira nesigurnost iz zajedničkog Q/b; Z6 odvojeno provjerava
kapacitet kanala, slobodni rub i zadano ulazno stanje bazena.

Uvodna skica ima izračunane grane energije, kritični presjek i spregnute
dubine. Nova zajednička skica vježbi prikazuje stvarne trapezne presjeke,
kote i pokose, brzine valova prema obali, krivulju E(y), povišenje dna,
suprotne hidrostatičke sile na fluid te granicu dubine bazena. Dno i voda
su neprekinuti, a duljine prijelaza i oblik valjka izričito su shematski.
Notebook zadržava postojeću jezgru i dodaje Z4–Z6, neovisne numeričke
provjere, propagaciju nesigurnosti i završna interpretacijska pitanja.
D03, D06 i generirani manifest usklađeni su s konačnim tekstom.

Provedene provjere prije commita:

- `verify_all.py`: 1307 rezultata (1096 golden i 211 invarijanti),
  22 dodatne fizikalne provjere i 90/90 ugovora zadataka; PASS.
  Sam U15 ima 80 rezultata.
- Struktura publikacije, Typst, normalizacija javnih referenci i
  aktualnost generiranog ključa: PASS; ostaje 87 primjera i 90 vježbi.
- `check_u15_sketch_geometry.py`: oba SVG-a PASS; provjerene su stvarne
  putanje, otvoreni presjeci, kote, smjerovi i odgovarajuće bilance.
- Notebook U15 izvršen je u čistom kernelu: PASS (5,48 s).
- HTML U15 i D06 pregledani su na 320, 768 i 1440 px: šest vježbi,
  razine, alias, jedinstveni ID-jevi, 12 sklopivih blokova dostupnih
  tipkovnicom i povratne poveznice prolaze. Automatizirani WCAG A/AA
  prolazi; nema vodoravnog prelijevanja stranice.
- Cijeli nativni PDF obnovljen je: 317 A4 stranica, PDF audit PASS.
  Vizualno su pregledane uvodna skica na str. 255, skice vježbi na
  str. 259 i ključ rezultata na str. 316. Kote, oznake i formule ostaju
  čitljive; potpuni kontrolni rezultati Z4–Z6 nisu odrezani.
- `git diff --check`: bez pogrešaka bjeline.

Provjere modela oslonjene su i na primarne tehničke izvore:
[USBR — long-throated flumes](https://www.usbr.gov/tsc/techreferences/mands/wmm/chap08_08.html)
i [HEC-RAS — critical depth determination](https://www.hec.usace.army.mil/confluence/rasdocs/ras1dtechref/6.0/theoretical-basis-for-one-dimensional-and-two-dimensional-hydrodynamic-calculations/1d-steady-flow-water-surface-profiles/critical-depth-determination).
Brojčani podatci novog zadatka autorski su, a nisu prepisani iz tih izvora.

Ovo je lokalna provjera U15. Zajednički završni HTML/PDF/JupyterLite build
cijeloga ciklusa slijedi nakon ponovnog pregleda U01 i U02. Geometrijske
i numeričke provjere dopunjuju autorski pregled; same ne dokazuju
didaktičku kvalitetu ni valjanost izvan navedenih pretpostavki modela.
