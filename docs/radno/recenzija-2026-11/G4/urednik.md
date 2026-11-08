# Urednički i lektorski pregled — G4: pog. 14, 15, uvodno poglavlje 0 i dodatci A–E

Pregledano 8. 11. 2026. prema `.claude/skills/recenzija-prirucnika/references/urednik.md`,
`docs/konvencije_pisanja.md` (K1–K16) i odjeljcima „Tekst”, „Notacija i nazivlje” i
„Odluke završne recenzije” iz `docs/urednicki_stil.md`. Pročitani su kanonski izvori
i PDF-ovi `G4.pdf`, `pog00.pdf` i `dodatci_A_E.pdf`. Fizika nije procjenjivana, osim
kad jezična promjena dira tvrdnju. Nijedna datoteka osim ovog izvještaja nije mijenjana.

Kratice mjesta: `u14` = `source/u14_turbostrojevi_i_propulzija.md`, `u15` =
`source/u15_otvoreni_tokovi.md`, `u00` = `source/u00_kako_koristiti_udzbenik.md`,
`d01`–`d05` = odgovarajući `source/d0N_….md`. Broj iza dvotočke je redak izvora.
Riješeni primjeri pog. 14 u PDF-u: P1 vodilica (r. 227), P2 pokretna lopatica (r. 294),
P3 Peltonova lopatica (r. 365), P4 radijalno kolo (r. 469), P5 propeler (r. 535), P6 dron (r. 589).

## Nalazi alata `prirucnik_stats.py --nalazi`

| Mjesto | Pravilo | Ocjena |
| --- | --- | --- |
| u14:17 | K3, 47 riječi | potvrđeno, prijedlog u tablici pog. 14 |
| u14:136 | K3, 44 riječi | potvrđeno, P3 (podjela na dvotočki i točki-zarezu) |
| u14:290 | K12, „u sljedećem primjeru” | potvrđeno, tablica pog. 14 |
| u15:9 | K3, 42 riječi | djelomično lažno: točka završava unutar formule (`\text{konst.}$`), pa alat spaja dvije rečenice; druga („Indeksi 1 i 2 …”) ipak ima oko 35 riječi i točku-zarez, P3 |
| d04:183 | K3, 48 riječi | odbačeno: alat broji URL poveznice; rečenica ima 17 riječi |

## Pog. 14 — Turbostrojevi i propulzija

| Mjesto | Pravilo | Sadašnji tekst | Prijedlog | Težina |
| --- | --- | --- | --- | --- |
| u14:3, 5, 7, 17 | K10 | Uvod navodi $\dot m_{rel}=\rho A(c_1-u)$, oba optimuma $u=c_1/3$ i $u=c_1/2$, Eulerovu jednadžbu s predznakom, $\eta_i=2v_A/(v_A+v_j)$ i ogradu „daju gornju granicu učinkovitosti; hidrauličke, mehaničke i generatorske gubitke treba procijeniti zasebno”. Sve se zatim izvodi (r. 51–72, 113–121, 193–197), a ograda stoji u Granici modela (r. 213). r. 17 ponavlja „Oznake slijede turbostrojarski standard: $c$ apsolutna, $u$ obodna i $w$ relativna brzina” iz r. 3. | Uvod svesti na fizikalno pitanje i model: zadržati r. 1, prvu rečenicu r. 3 (oznake $c$, $u$, $w$ i $\vec c=\vec u+\vec w$), prvu rečenicu r. 5 bez formule te prve dvije rečenice r. 7. Formule i optimumi ostaju u izvodima i Sažetku, a ograda o gornjoj granici u r. 213. U r. 17 izostaviti posljednju rečenicu. | P2 |
| u14:3, 49, 79, 87, 130 | K10 | Tvrdnja „rad daje samo promjena tangencijalne komponente …, pa su kutovi lopatica … izravni (središnji) projektni parametri” stoji pet puta: u uvodu, u izvodu, u rečenici ispred jednadžbe $P=F_tu=M\omega$, u okviru *Fizikalno značenje* i iza Eulerova izvoda. | Zadržati r. 49 (izvod sile: $F_y$ opterećuje ležajeve) i r. 130 (iza Eulerove jednadžbe, gdje je tvrdnja dokazana). Okvir r. 85–88 izostaviti jer r. 79 i r. 49 nose isto; rečenicu iz r. 3 ukloniti prema prethodnom retku. | P2 |
| u14:31, 76 | K10 | „**Konvencija kuta.** U cijelom poglavlju … kutovi lopatica $\beta_1$, $\beta_2$ mjere se od smjera suprotnog gibanju lopatice ($-u$) … za pokretnu lopaticu vrijedi $\theta=180^\circ-\beta_2$.” ponavlja definiciju iz r. 31. | „**Konvencija kuta.** Ta konvencija vrijedi u cijelom poglavlju, u izvodu, riješenim primjerima i zadatcima, kao u konstrukciji turbostrojeva. Skretanje u nepomičnoj vodilici također se označuje s $\theta$, mjerenim od $+x$. Kutovi lopatica ne smiju se miješati s korekcijskim faktorom količine gibanja $\beta$ iz drugih poglavlja.” | P2 |
| u14:446, 462, 466 (P3) | K10, K8 | U istom primjeru tri puta stoji da snaga jedne lopatice nije snaga kola, a optimum dvaput, s različitim zaokruživanjem: „kolo s $u/c_1\approx0{,}50$ radi upravo u optimumu” (r. 462) i „kolo s $u/c_1=0{,}497$ radi u svojem optimumu” (r. 466). | Izostaviti posljednju rečenicu r. 462 („Usporedba s $10{,}49\ \text{kW}$ jedne lopatice bila bi pogrešna: … s punim protokom.”). Vrijednost $10{,}49\ \text{kW}$ i razlog ostaju u r. 446, a optimum s $u/c_1=0{,}497$ u r. 466. | P2 |
| u14:290, 587 | K12 | „… pokretna lopatica u sljedećem primjeru dio te energije pretvara u rad.”; „Posljednji primjer prenosi aktuatorski disk iz mora u zrak: …” | „… pokretna lopatica u primjeru [-@ex-u12-pokretna-zakrivljena-lopatica-s-relativnim-izlazom-t3] dio te energije pretvara u rad.”; „Primjer [-@ex-u12-propeler-dronskog-kvadkoptera-u-stanju-visa-t2] prenosi aktuatorski disk iz mora u zrak: …” | P2 |
| u14:17 | K3 | Jedna rečenica od 47 riječi: „Bilanca količine gibanja … izvedena je u pog. 10 …: u kontrolnom volumenu koji prati lopaticu masa ulazi relativnom brzinom $\vec w=\vec c-\vec u$, $\dot m_{rel}=\rho Aw_n$, a sila na fluid slijedi iz promjene apsolutne brzine; @ex-… pokazuje taj račun na Peltonovoj lopatici.” | „Bilanca količine gibanja na nepomičnoj vodilici i na lopatici koja se giba stalnom brzinom izvedena je u []{.mf1-chapter-ref target="u10"}. U kontrolnom volumenu koji prati lopaticu masa ulazi relativnom brzinom $\vec w=\vec c-\vec u$, $\dot m_{rel}=\rho Aw_n$, a sila na fluid slijedi iz promjene apsolutne brzine. Primjer [-@ex-peltonova-lopatica-u-gibanju] pokazuje taj račun na Peltonovoj lopatici.” | P2 |
| u14:127 | K3 | „Izraz ima isti oblik kao umnožak $F_xu$ sile na pokretnu lopaticu iz jednadžbe [-@…-04] i obodne brzine, zapisan komponentama brzine umjesto izlaznog kuta, ali s punim protokom $\dot m$ umjesto $\dot m_{rel}$: Eulerov zapis vrijedi za kolo, a ne za jednu lopaticu.” (oko 45 riječi, „umnožak … sile … i obodne brzine” rastavljen umetkom) | „Izraz ima isti oblik kao umnožak $F_xu$ sile na pokretnu lopaticu iz jednadžbe [-@eq-turbostrojevi-razrada-koraka-04] i obodne brzine, samo je zapisan komponentama brzine umjesto izlaznog kuta. Razlika je u protoku: Eulerov zapis s punim protokom $\dot m$ vrijedi za kolo, a zapis s $\dot m_{rel}$ za jednu lopaticu.” | P2 |
| u14:136 | K5 | „Za procjenu srednjeg rada prikladan je MRF (*Multiple Reference Frame*, više referentnih okvira): …” — engleski izraz bez „engl.”, kratica se u poglavlju javlja jednom. | „Za procjenu srednjeg rada prikladan je model s više referentnih okvira (engl. *Multiple Reference Frame*, MRF): …” (kratica ostaje radi pojmovnika). | P2 |
| u14:594 | K5 | „Faktor učinka (*figure of merit*) $FM = 0{,}70$ …” | „Faktor učinka (engl. *figure of merit*) $FM = 0{,}70$ …” | P2 |
| u14:478, 532 (P4) | K5 | „meridijanske komponente $c_{m1}$, $c_{m2}$” i „uz pretpostavljeni umnožak faktora klizanja i hidrauličke učinkovitosti $\approx0{,}82$” — oba pojma bez definicije u poglavlju. | r. 496: „Kontinuitet kroz cilindrične presjeke daje meridijanske komponente, u radijalnom kolu radijalne komponente apsolutne brzine,”; r. 532: „… umnožak faktora klizanja (konačan broj lopatica ne skreće tok točno pod kutom $\beta_2$) i hidrauličke učinkovitosti $\approx0{,}82$ …”. | P2 |
| u14:3, 95, 111; d02:28 | K7 | Isti zakon ima tri naziva: „Eulerova jednadžba turbostrojarstva” (r. 3, 111), „Eulerova turbinska jednadžba” (naslov izvoda, r. 95; tako i pog. 10) i „Eulerova jednadžba turbostroja” (pojmovnik). | Odabrati jedan naziv za pog. 14 i dodatak B, npr. „Eulerova jednadžba turbostrojarstva”. Naslov izvoda tada glasi „Matematički izvod — Eulerova jednadžba turbostrojarstva iz momenta količine gibanja”. Ako pog. 10 zadrži „turbinska”, navesti sinonim pri prvom spomenu u pog. 14. | P2 |
| u14:240, 308, 382 | K13 | Potpisi „Vodilica mlaza na ispitnom stolu.”, „Pokretna zakrivljena lopatica.”, „Peltonov rotor s jednim mlazom.” samo ponavljaju naslov primjera i ne kažu što slika pokazuje. | Npr. „Nepomična vodilica skreće pravokutni mlaz za $120^\circ$ od smjera ulaza; prikazana je sila fluida na vodilicu.”, „Mlaz prati lopaticu koja se giba u smjeru $+x$; ulazni i izlazni trokut brzina nacrtani su u zajedničkom mjerilu.”, „Jedna Peltonova lopatica zahvaća tangencijalni mlaz na vrhu putanje rotora; prikazani su trokuti brzina i sila fluida na lopaticu.” Postojeći `fig-alt` tada preoblikovati tako da opisuje raspored crteža, a ne ponavlja potpis. | P2 |
| u14:448 (P3) | dosljednost koraka (u00:36) | Samo peti korak rješenja ima naslov „5. Cijelo kolo s punim sapničkim protokom”; koraci 1–4 nemaju ni naslov ni broj, pa se „5.” u PDF-u pojavljuje bez prethodnika. | Zamijeniti naslov podebljanim uvodom bez broja: „**Cijelo kolo s punim sapničkim protokom.** Kolo zahvaća …”, ili dodati naslove svim koracima. | P2 |
| u14:148 | K3 | „Nastavci obrađuju Z3–Z5.” — nije jasno čiji su nastavci. | „Nastavci bilježnice obrađuju Z3–Z5.” | P2 |
| u14:698 | K2 | „U Z4 nacrtane su samo zadane apsolutne brzine; trokute $\vec c=\vec u+\vec w$ crta student.” | „U Z4 nacrtane su samo zadane apsolutne brzine; trokute $\vec c=\vec u+\vec w$ nacrtaj sam.” | P2 |
| u14:218 | K4 | Podebljani naslov CFD odlomka u obliku pitanja: „**Propeler iza trupa: kad trebamo pojedine lopatice?**” | „**Propeler iza trupa: kada su potrebne pojedine lopatice.**” | P2 |

## Pog. 15 — Otvoreni tokovi

| Mjesto | Pravilo | Sadašnji tekst | Prijedlog | Težina |
| --- | --- | --- | --- | --- |
| u15:3, 7 | K10 | Uvod daje $Fr=v/\sqrt{gy_h}$, $c=\sqrt{gy_h}$, $q=vy$, $E=y+q^2/(2gy^2)$, $y_c=(q^2/g)^{1/3}$, $E_{min}=\tfrac32y_c$, $I_1=I_2$, $E_2<E_1$ i „Zato se skok računa bilancom količine gibanja, a ne Bernoullijevom jednadžbom”. Sve se izvodi u odjeljcima 15.3–15.6, a posljednja tvrdnja ponavlja se u r. 237. r. 7 ponavlja ograde iz r. 183, 284 i 636. | Uvod svesti na pitanje i režime riječima: r. 1, r. 3 bez formula (mirni i siloviti tok, kritični tok ih razdvaja, skok kao nagli prijelaz), r. 5 i prva rečenica r. 7. Ograde „ne opisuje unutrašnjost skoka ni tok preko kratkoga zakrivljenog praga” i „Koeficijenti … vrijede samo u ispitanom rasponu” ostaju u Granici modela (r. 284), r. 183 i Sažetku (r. 633–636). | P2 |
| u15:15 | K4 | „## Otvoreni tokovi” (15.1) ponavlja naslov poglavlja; odjeljak od tri rečenice ponavlja r. 1 („gornja granica … izložena atmosferi”, „pokreće gravitacija”). | Izjavni naslov teme, npr. „## Slobodna površina kao nepoznata granica {#sec-otvoreni-tok-motivacija}”, ili odlomak pripojiti uvodu uz zadržani ID. | P2 |
| u15:56 | K5 | „… a pad tlaka pod trupom povećava gaz i trim (*squat*).” | „… a pad tlaka pod trupom povećava gaz i trim (engl. *squat*).” | P2 |
| u15:244 | K5 | „… s rubnim presjecima 1 i 2 izvan valjka, gdje je raspodjela tlaka hidrostatička.” — prvi spomen valjka (dalje 8 puta) bez definicije. | „… s rubnim presjecima 1 i 2 izvan valjka, vrtložnog područja povratnog toka na površini skoka, gdje je raspodjela tlaka hidrostatička.” | P2 |
| u15:328, 564 | K5 | „Metoda VOF pritom prati volumenski udio vode u ćeliji …”; „linearna propagacija standardnih nesigurnosti (GUM)” — obje kratice po jednom u poglavlju, bez punog naziva. | „Metoda volumena fluida (engl. *Volume of Fluid*, VOF; dodatak D) pritom prati …”; „linearna propagacija standardnih nesigurnosti prema međunarodnim uputama (engl. *Guide to the Expression of Uncertainty in Measurement*, GUM)”, uz zapis u dodatku E. | P2 |
| u15:165 | K12 | „Za stvarni preljev dodaje se empirijski koeficijent $C_{pr}$ (vidi odjeljak o kontrolnim građevinama).” | „… empirijski koeficijent $C_{pr}$ (odjeljak [-@sec-kontrolne-gradevine]).” | P2 |
| u15:90 | K3 | „U natkritičnom režimu obje informacije dolaze s uzvodne strane, pa se mijenja i način zadavanja rubnih uvjeta.” — „obje informacije” nema prethodnika. | „U natkritičnom režimu oba karakteristična vala putuju nizvodno, pa oba rubna podatka dolaze s uzvodne strane i mijenja se način zadavanja rubnih uvjeta.” | P2 |
| u15:232 | K3 | „S hidrostatičkim modelom ne uspoređujemo ondje gdje izrazita zakrivljenost toka ruši njegovu osnovnu pretpostavku.” — nije rečeno što se ne uspoređuje. | „Rezultate prostornog modela ne uspoređujemo s hidrostatičkim modelom ondje gdje izrazita zakrivljenost toka ruši njegovu osnovnu pretpostavku.” | P2 |
| u15:230 | K4 | Podebljani naslov CFD odlomka u obliku pitanja: „**Hoće li prag uzvodno podići vodu?**” | „**Utjecaj praga na uzvodnu razinu.**” | P2 |

## Pog. 0 — Kako koristiti priručnik

| Mjesto | Pravilo | Sadašnji tekst | Prijedlog | Težina |
| --- | --- | --- | --- | --- |
| u00:7 | K5 | „… osnovno gradivo priručnika možeš pratiti i bez učenja CFD postupaka.” — prvi spomen kratice u knjizi, bez punog naziva (dalje u r. 29, 67). | „Blokovi *Dublje* i odlomci *Računalna dinamika fluida* (engl. *Computational Fluid Dynamics*, CFD) dodatno su štivo: …” | P2 |
| u00:71 | K7 | „## Dodaci za brzo snalaženje” | „## Dodatci za brzo snalaženje” (oblik iz uredničkog stila i naziva dodataka) | P2 |
| u00:38 | K1, K12 | „Upućivanje na zadatak uključuje i oznaku poglavlja, primjerice „poglavlje 3, Z2”.” — knjiga upućuje oblikom „pog. 3”. | „…, primjerice „pog. 3, Z2”.” | P2 |

## Dodatci A–E

| Mjesto | Pravilo | Sadašnji tekst | Prijedlog | Težina |
| --- | --- | --- | --- | --- |
| d01:50, 63, 86, 101, 119, 131, 147, 163, 181, 192 | K4, pravopis | Deset naslova počinje malim slovom; u PDF-u „A.2 pog. 1–2: Osnovne veličine, tlak, viskoznost i kapilarnost”. | Naziv teme naprijed, oznaka u zagradi: „A.2 Osnovne veličine, tlak, viskoznost i kapilarnost (pog. 1–2)”, ili „Pog. 1–2: …”. | P2 |
| d04:26; d02:80, 105, 112 | K5 | d04: „CFD, FEM, RANS s modelima $k$–$\varepsilon$ i $k$–$\omega$ SST, SIMPLE i PISO, MRF i klizna mreža … definirani su u pojmovniku.” Pojmovnik razrješuje CFD i FEM, a MRF, RANS, SST, SIMPLE i PISO samo opisuje, bez punog naziva. | U pojmovniku dodati pune nazive, npr. „MRF (engl. *Multiple Reference Frame*) i klizna mreža”, „RANS (engl. *Reynolds-Averaged Navier–Stokes*) i modeli zatvaranja ($k$–$\varepsilon$, $k$–$\omega$ SST, engl. *Shear Stress Transport*)”, „SIMPLE i PISO (engl. *Semi-Implicit Method for Pressure-Linked Equations*; *Pressure-Implicit with Splitting of Operators*)”. Tvrdnja u d04:26 tada postaje točna. | P2 |
| d04:31, 154, 183 | K5 | „LES / DNS” u tablici kratica bez punog naziva; „V&V” (naslov D.8 i r. 183) nigdje u dodatku D nije razriješen. | „LES / DNS — *Large Eddy Simulation* / *Direct Numerical Simulation*” uz postojeći opis; „## Pripremljeni paketi za verifikaciju i validaciju (V&V) {#sec-cfd-vv-paketi}”. | P2 |
| d04:167, 173 | K1 | „Validator `python tools/validate_cfd_vv.py` provjerava reference, bilance, podrijetlo, opaženi red i GCI.”; „Pretpostavke i podrijetlo podataka sačuvani su u `teaching_comparison.json`.” — interni alat i datoteka u vidljivom tekstu. | „Uz pakete je priložena skripta koja provjerava reference, bilance, podrijetlo, opaženi red i GCI; upute su u opisu paketa.”; „Pretpostavke i podrijetlo podataka zapisani su u opisu paketa.” Rečenica „**GCI nije automatski standardna nesigurnost** …” ostaje. | P2 |
| d04:183 | K14 | „… Versteeg i Malalasekera, *An Introduction to Computational Fluid Dynamics: The Finite Volume Method*, ili Ferziger, Perić i Street, *Computational Methods for Fluid Dynamics*.” — bez izdanja, godine i zapisa u dodatku E. | Dodati oba djela u `references.bib` s izdanjem, izdavačem i godinom i citirati ih ([@…]); tada se pojavljuju i u E.6. | P2 |
| d05:5 (`references.bib`, `virag`) | K14 | Zapis „Virag, Z., *Mehanika fluida — odabrana poglavlja*, FSB, Zagreb” nema godinu ni izdanje. | Dopuniti godinom i izdanjem (ili oznakom skripte s godinom). | P2 |
| d03:325 | K6 | „Izostavljen ulazni tok količine gibanja $\dot mv_A$ u bilanci potiska (Z5).” — Z5 pog. 14 je vodomlazni pogon i računa s $v_s$ („bez sustrujanja”), kao i A.6. | „Izostavljen ulazni tok količine gibanja $\dot mv_s$ u bilanci potiska (Z5).” | P2 |
| d03:280 | K3 | „Hagen–Poiseuilleov izraz primijenjen na turbulentni tok ili bilanca sila $\tau_{st}=\Delta p\,D/(4L)$ pogrešno ograničena na laminarni režim, visina prve ćelije odabrana bez brzine trenja (Z2).” — dvije pogreške spojene golim zarezom. | Dvije natuknice: „Hagen–Poiseuilleov izraz primijenjen na turbulentni tok ili bilanca sila $\tau_{st}=\Delta p\,D/(4L)$ pogrešno ograničena na laminarni režim (Z2).” i „Visina prve ćelije odabrana bez brzine trenja (Z2).” | P2 |

P1: nema nalaza.

## Nalazi P3 (skupno)

1. **K8, previše znamenaka u kontrolnim rezultatima** (6): u14:779 ($30{,}00^\circ$, $7{,}500\ \mathrm{kW}$), u14:841 ($103{,}01$ mm), u15:449, 510, 572; u15:542 (šest decimala) opravdan je zahtjevom reziduala $10^{-6}$ m.
2. **K5, engleski izraz bez „engl.”** (6): u00:67 (*Jupyter notebooks*), d01:35 (*discharge*, *drag*), d04:30, 32, 34 (*Finite Volume Method* …), d04:169 („120 grit”).
3. **K5, nerazriješene ili rijetke kratice** (5): d02:45 NPSH, d02:77 FEM, d03:13 i 236 RSS (2×), d04:162–163 CFL3D/SSTm, FUN3D, NASA TMR.
4. **K7, „knjiga” umjesto „priručnik”** (6): d01:41, 138; d02:27; d04:3, 44; u00:31.
5. **K1/K12, oblik upućivanja** (5): u00:31 „dodatak o numeričkoj mehanici fluida” i d04:26 „pojmovniku” umjesto „dodatak D/B”; d05:9, 17 „u poglavlju 9”, „iz poglavlja 12”, „u poglavlju 6” umjesto „pog. N”. Usput: chapter-ref ispisuje puni naslov, pa „pog. 10 Količina i moment količine gibanja” stoji četiri puta na prve dvije stranice pog. 14 (u14:1, 17, 29, 99).
6. **K7, sitne nedosljednosti nazivlja** (4 obrasca): „lebdenje / lebdeći režim” (u14:170, 179, 857) uz „vis” (u14:5, 207, 589); „radijus” (d01:188) uz „polumjer”; „preljev širokog praga” (d01:199) uz „široki preljev”; „jedinični protok” (u15:153, 207) uz „protok po jedinici širine”.
7. **K10, manja ponavljanja** (3): u14:21 i 74 (sila bez snage pri $u=0$); u15:278 i 326–328 (energija se gubi, bilanca količine gibanja zatvorena); u14:5 i 191 (veći disk, manja inducirana brzina).
8. **K10/K13, dugi uvodni opisi slike koji prepričavaju `fig-alt`** (2): u14:9, u15:9; u u15:9 rečenicu „Indeksi 1 i 2 …” podijeliti na točki-zarezu.
9. **K4, naslovi-pretinci i pitanja** (5): d02:3 „Pojmovi od A do Ž” (jedini pododjeljak), d04:186 „Završna poruka dodatka”, d01:204 „… koje treba zaustaviti odmah” (nejasno); d04:128, 150 podebljana pitanja kao uvod definicije.
10. **K2, bezlični „treba” u izlaganju u 1. licu množine** (4): u14:7, 165, 532; u15:17.
11. **Oznake blokova bez obrasca „Vrsta — Podnaslov”** (2): d02:145 „Kako čitati pragove”, d04:176 „Aeroprofil nije automatski hidroprofil” (oba su blok Granica modela).
12. **d03, oznake zadataka** (2): (P1) u r. 92 nije najavljen u r. 1, koji spominje samo Zn; u r. 350 nedostaje (Z5).
13. **d01, stupac jedinica ne prati skupine oznaka** (2): r. 20 (četiri skupine, tri jedinice); r. 22 ($a$ je i ubrzanje i visina otvora, a jedinica je samo m/s).
14. **Ostalo** (4): u14:136 alat K3 (podijeliti na dvotočki i točki-zarezu); d04:165 „promjere 100/50 mm” → „100 mm i 50 mm”; u14:589 „dronskog kvadkoptera” (pleonazam); numerički pokus pog. 15 stoji iza zadataka (u15:613), a u pog. 14 u teoriji (u14:141).
15. **K14, izdanja** (3): White 2011 (7. izd.), Munson 2009 (6. izd.) i Çengel i Cimbala 2014 (3. izd.) imaju novija izdanja. Provjeriti i uskladiti s pravilom o aktualnim izdanjima.

## Tri najčešća obrasca

1. **Ponavljanje (K10).** Uvodi pog. 14 i 15 unaprijed donose formule, optimume i ograde. Isti se zaključci zatim ponavljaju u izvodu, okviru *Fizikalno značenje*, Granici modela i primjeru (tangencijalna komponenta 5×, dva optimuma, konvencija kuta, bilanca skoka).
2. **Kratice i engleski izrazi bez definicije (K5).** MRF, VOF, GUM, LES/DNS, V&V; *figure of merit* i *squat* bez „engl.”; CFD pri prvom spomenu u pog. 0. Dodatak D se oslanja na pojmovnik koji te kratice ne razrješuje.
3. **Upućivanja i naslovi (K12, K13, K4).** Javljaju se opisna upućivanja („u sljedećem primjeru”, „Posljednji primjer”, „vidi odjeljak o …”) i potpisi slika jednaki naslovu primjera. Neki naslovi su u obliku pitanja ili ponavljaju naslov (15.1 „Otvoreni tokovi”, A.2–A.11 s malim početnim slovom).

## Ograničenja

Ocjene težine i prijedlozi autorska su procjena urednika. Izvršene provjere su:
čitanje cijelih izvora, `prirucnik_stats.py --nalazi` i pretraga teksta PDF-ova.
PDF-ovi nisu vizualno pregledani stranicu po stranicu, pa prijelom, slike i tablice nisu ocijenjeni.
Blok „Provjeri sebe” i ključ (dodatak F) izvan su opsega, prema zadatku.
Prijedlozi pod K14 (izdanja, Virag) traže provjeru bibliografskih podataka.
