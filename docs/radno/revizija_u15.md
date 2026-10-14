# Revizija U15 — otvoreni tokovi

## Dijagnoza i matrica prije provedbe

Pročitani su kanonski izvor, svih pet primjera i šest zadataka, verifier
`verify_u15_open_channels.py`, notebook i jedina postojeća SVG referenca.
Kurikularni ishod traži kritičnu dubinu i hidraulički skok, uz kontrolni
presjek, granice 1D modela i numerički pokus.

| Mjesto | Postojeći ID i uloga | Odluka i didaktička korist | Razina | Završni ID | Povezane datoteke/provjere | Status |
| --- | --- | --- | --- | --- | --- | --- |
| P1 | `ex-rezim-retencijski-kanal`; v i Fr pravokutnog kanala | ZADRŽATI osnovni izravni račun i vezu s prijenosom poremećaja | T1 | isti | verifier | provedeno |
| P2 | `ex-kriticni-preljev`; minimum energije | ZADRŽATI; provjeriti zaokruživanje minimalne energije | T2 | isti | verifier | provedeno |
| P3 | `ex-dvije-dubine`; numerički korijeni E(y) | ZADRŽATI kao vođeni postupak dviju grana | T2 | isti | notebook, verifier | provedeno |
| P4 | `ex-hidraulicki-skok-bazen`; spregnute dubine i disipacija | ZADRŽATI; bilanca količine gibanja i ograničenje duljine bazena jasno su navedeni | T3 | isti | verifier | provedeno |
| P5 | `ex-manning-osjetljivost`; kapacitet i hrapavost | ZADRŽATI kao jednostavan uvod u osjetljivost n | T3 | isti | verifier | provedeno |
| Z1 | `task-otvoreni-fr`; v i Fr | ZADRŽATI osnovnu tehniku; dopuniti smjer i brzine obaju valova te naputak | T1 | isti | SVG, verifier, D06 | provedeno |
| Z2 | `task-kriticna-dubina`; yc i Emin | ZADRŽATI jednostavnu primjenu minimuma, jasno navesti pravokutni kanal i model | T1 | isti | SVG, verifier, D06 | provedeno |
| Z3 | `task-trapezni-presjek`; geometrija A/T/P i Fr | ZADRŽATI: razlikovanje Dh i Rh nije ponavljanje pravokutnih primjera; dodati stvarno kotiran trapez | T2 | isti | SVG, verifier, D06 | provedeno |
| Z4 | `task-alternativne-dubine`; ponovno dva korijena E(y) | ZAMIJENITI: podkritični dotok preko povišenog dna, dopuštena visina i izbor ostvarene grane | T2 | `task-kontrolni-presjek-na-pragu` | stari alias, SVG, notebook, verifier, D06 | provedeno |
| Z5 | `task-skok-mjerenje`; sintetička mjerenja, R i uR | ZADRŽATI dijagnostiku; naglasiti zajednički q u oba presjeka, sintetičke podatke i ograničenje zaključka | T3 | isti | SVG, notebook, verifier, D06 | provedeno |
| Z6 | `task-klimatski-kanal`; tri stanja održavanja, kapacitet i bazen | ZADRŽATI integraciju i kompromis; razjasniti kriterij n+2un, zadano ulazno stanje bazena i potpunost D06 | T4 | isti | SVG, notebook, verifier, D06 | provedeno |

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


## Revizija 12. 10. 2026.

Provedba nalaza neovisne stručne recenzije (odobreno od autorice). Opseg:
izvodi (kritična dubina, spregnute dubine iz bilance količine gibanja),
Granica modela, Fizikalno značenje (Froudeov broj kanala i broda), opći
kritični uvjet, kontrolne građevine, razine T, lektura i notacija ($y_h$, $T$,
$c$, impulsna funkcija $I$).

| Mjesto | Prije (ID, razina) | Odluka | Poslije (ID, razina) | Kontrolni rezultat | Provjere |
| --- | --- | --- | --- | --- | --- |
| teorija | $y_c$ izveden u prozi | OMOTAN u `.mf1-izvod` s drugom derivacijom i provjerom $Fr=1$; DODAN opći kritični uvjet `eq-opci-kriticni-uvjet` ($Q^2T/(gA^3)=1$) | — | — | čitanje |
| teorija | skok: relacije navedene | NOVI `.mf1-izvod` iz bilance količine gibanja: sile $\rho g b y^2/2$, tok $\rho b q^2/y$, impulsna funkcija $I/(\rho g b)$, dijeljenje s $(y_1-y_2)$, kvadratna za $y_2/y_1$, $\Delta E$; provjera $Fr_1\to1$ i $Fr_1<1$; NOVA Granica modela | zadržani `eq-spregnute-dubine`, `eq-gubitak-skoka`, ID funkcije | — | — |
| teorija | — | NOVI odjeljak `sec-kontrolne-gradevine`: `eq-istjecanje-ispod-ustave`, `eq-preljev-siroki` (empirijski $C_d$, $C_w$) | — | — | — |
| teorija | — | NOVI `.mf1-fizikalno-znacenje`: $Fr$ kanala vs $Fr$ broda, $Fr_h=v_s/\sqrt{gh}$, squat, blokada bazena | — | — | — |
| P4 | `ex-hidraulicki-skok-bazen`, T3 | DOPUNJEN odlukom o nizvodnom vodostaju (1,00 m → skok odnesen; 1,40 m → potopljen) | isti ID, T3 | $y_2=1{,}2353$ m; $1{,}00<y_2<1{,}40$ | `U15.P4.tailwater_decision` |
| P5 | `ex-manning-osjetljivost`, T3 | razina T2; lektura („Kapacitet”), $S_f=S_0$, ID jednadžbe | isti ID, T2 | isti | — |
| Z1–Z3 | — | ZADRŽANI; $y_h$ umjesto $D_h$ | isti | isti (`U15.Z3.yh`) | verifier |
| Z4 | `task-kontrolni-presjek-na-pragu`, T2 | razina T3 (izbor grane uz obrazloženje i rezidual); podatci nepromijenjeni | isti, T3 | isti | — |
| Z5 | `task-skok-mjerenje`, T3 | razina T4; rezidual $R=(I_2-I_1)/(\rho gb)$; naputak samo model i kriterij; `data-key-full` | isti, T4 | isti | verifier (ID-jevi bez „M”) |
| Z6 | `task-klimatski-kanal`, T4 | razina T2: traženo svedeno na kapacitet, normalnu dubinu i slobodni rub po stanju te bazen pri $Q_d$; podatci (uključujući $\pm u_n$, koje koristi bilježnica) nepromijenjeni | isti, T2 | $Q_{cap}=11{,}759/8{,}141/6{,}047$; $y_n=0{,}985/1{,}189/1{,}380$; $f=0{,}515/0{,}311/0{,}120$ (A, B da; C ne); $y_2(Q_d)=1{,}059$ m | verifier: uklonjeni `Qcap_conservative_*`, `y2_capacity_*`, `robust_state_count`, `basin_exceedance_count` |
| samoprovjera 3 | duplikat „Zastani” | ZAMIJENJENO pitanjem o položaju skoka pri premalom nizvodnom vodostaju | — | — | — |

Raspored razina nakon revizije: Z1 T1, Z2 T1, Z3 T2, Z4 T3, Z5 T4, Z6 T2
(2×T1, 2×T2, T3, T4). Bilježnica `u15_otvoreni_tokovi.ipynb` nije mijenjana
(podatci Z4–Z6 isti; njezin nastavak s $n+2u_n$ sada prelazi traženo Z6, što
tekst zadatka izričito kaže). Skica `u15_vjezbe_skice.svg`: samo natpis Z3
($y_h$); geometrija nepromijenjena.

Provjere: `verify_u15_open_channels.py` 73 rezultata, 0 FAIL;
`check_u15_sketch_geometry.py` PASS. Broj riječi 3354 → 4192 (izvodi,
granica, kontrolne građevine, Froude broda).
