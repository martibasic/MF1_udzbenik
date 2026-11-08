# Stručna recenzija pog. 13 (Gubitci, cjevovodi, crpke i mreže), drugi model

Izvor: `source/u13_gubici_cjevovodi_crpke_i_mreze.md`; PDF str. 245–262; ključ F.14 (knjiga str. 350–351).
Oznake težine prema `docs/konvencije_pisanja.md` (P0–P3).

## Sažetak

Poglavlje je fizikalno točno i dobro ograđeno: izvodi (13.10)–(13.15), (13.17)–(13.19) i lanac snaga (13.23)–(13.26) ispravni su, a svi brojevi riješenih primjera P1–P6 i ključa Z1–Z6 poklapaju se s mojim ponovnim izračunom. Nisam našao P0 ni P1 nalaz; preostali nalazi su pogrešno upućivanje, nejednoznačno „Traži se” u P3, nekoliko preciznosti u izlaganju i prijedlozi o razini i naputcima.

## Brojevi: provjera (moj račun, Python)

| Stavka | Tekst/ključ | Moj račun |
| --- | --- | --- |
| P1 | v²/2g=0,294; hl=2,47; hloc=1,35; hg=3,82 m; Δp=37,4 kPa | 0,2936; 2,466; 1,351; 3,817; 37,44 kPa |
| P2 | v=0,637; Re=509; λ=0,1257; hl=1,298 m; 13,37 kPa (obje formule) | 0,6366; 509,3; 0,1257; 1,300; 13,37 kPa |
| P3 | R=7181/45445/11913/8378; ΔQ1=−2,92; ΔQ2=−0,19; h=2,56/2,16/0,99/3,73 | 7181/45445/11913/8378; −2,921; −0,186; 2,563/2,158/0,988/3,733; konvergira na 18,89/6,89/−9,11/−21,11 L/s |
| P4 | Qop=19,94; Hop=18,04; Hs(17,24)=15,01; s=0,899 | Q²=19/0,0478=397,5, Q=19,94; 18,04; 15,01; s²=0,8084, s=0,899 |
| P5 | Ph=0,706; Pvr=0,906; Pel=1,015 kW; 7,10 MWh; 5,92; 1,18 | 0,7063; 0,9055; 1,0147 (1,0153 sa zaokruženim 0,906); 7,10; 5,92; 1,18 |
| P6 | v=2,785; hgs=1,453; p/ρg=5,847 m; 57,36 kPa; NPSHa=6,00 m | 2,785; 1,453; 5,847; 57,36; 6,00 |
| Z1 (ključ) | hg=2,554; ζ=16,5; v=1,743; Q=13,69 L/s; 75,8 % | 2,5535; 16,5; 1,743; 13,69; 75,76 % |
| Z2 | Re=796/4775; λ=0,0804/0,0381; 7,73/3,38 kPa; 2Q: 15,5/≈11,4 | 795,8/4774,6; 0,0804/0,0381; 7,73/3,38; 15,5/11,38 |
| Z3 | Rv=36000; 10,00 L/s; hAB=4,80; hgV=3,60 | isto |
| Z4 | Qop=19,030; Hop=19,136; Re=2,423e5; λ=0,020812; 3,572/4,700/5,109 kW | 19,0296; 19,1362; 2,4229e5; 0,020812; 3,5724/4,7005/5,1092 |
| Z5 (ključ, Swamee–Jain) | λ=0,0238/0,0228/0,0221; hg=33,1/10,8/3,56 m; stara, 100 mm: 0,0309; 14,0 m | SJ: 0,0238/0,0228/0,0221; 33,13/10,78/3,56; 0,0309; 14,03. Colebrook: hg=32,95/10,71/3,54 (razlika oko 0,5 %) |
| Z6 | Q=22,36; (17,00; 11,50); s=0,866; (8,19; 5,54; 2,65) MWh/god; NPSHa 10,06; NPSHr 4,50; balast 8,66 | Q²=500, Q=22,36; 17,00; 11,50; s²=0,75; EV=8,19; NPSHa=10,057; balast 8,656 |

Dimenzijska homogenost i redovi veličine su u redu. (13.17) provjereno izvodom: R = 8/(π²g)·(λL/D⁵ + Σξ/D⁴).

## Nalazi

### P0
Nema.

### P1
Nema.

### P2

**P2-1. Pogrešno upućivanje na zadatke u numeričkom pokusu o paralelnim granama.**
Mjesto: `u13_…md:265`; PDF str. 251 („nastavci zasebno obrađuju Z3 i Z6”).
Opis: Z6 je balastna crpka i NPSH, ne paralelne grane ni promjer cijevi; pokus „promijeni promjer jedne grane” nastavlja se u Z3 (uravnoteženje) i Z5 (izbor promjera). Nisam siguran što je autorica mislila (možda ostatak starog numeriranja).
Prijedlog: „Z3 i Z5”; provjeriti sadržaj bilježnice `u13_paralelne_grane`.

**P2-2. Nerazriješena poveznica u ključu F.14.**
Mjesto: ključ Z5 i Z6 (str. 350–351): „λ iz jednadžbe odgovarajući izraz”, „prema jednadžbi odgovarajući izraz”.
Opis: umjesto broja jednadžbe stoji tekst rezervnog mjesta, pa rečenica nema smisla (K12).
Prijedlog: upiši `[-@eq-swamee-jain]` (Z5) i `[-@eq-npsha-spremnik]` (Z6); provjeri generator ključa.

**P2-3. P3, „Traži se” 1 nije jednoznačan.**
Mjesto: `u13_…md:468–486` (`ex-petlja-gradske-mreze`); PDF str. 255.
Opis: „početnu raspodjelu protoka koja zadovoljava bilance” ima beskonačno mnogo rješenja (jedan stupanj slobode po petlji). Student s drugom početnom raspodjelom dobije drukčije ΔQ u prvoj i drugoj iteraciji i ne može usporediti s (13.38)–(13.40). Konačno rješenje je jedinstveno (moj račun: 18,89 / 6,89 / −9,11 / −21,11 L/s, rezidual 0,001 m nakon 3. iteracije).
Prijedlog: zadati početnu raspodjelu (22,0; 10,0; −6,0; −18,0 L/s) ili tražiti i konvergirani rezultat.

**P2-4. Jednadžba (13.4) za turbulentni tok vrijedi samo uz cjelovitu disipaciju.**
Mjesto: `u13_…md:46–62`, (13.3)–(13.4); PDF str. 246–247.
Opis: Φ = 2μS_ijS_ij s osrednjenim poljem u turbulentnom toku daje samo disipaciju osrednjenog toka; glavnina gubitka u cijevi je turbulentna disipacija ρε. Zadnja rečenica bloka spominje RANS, ali ne kaže izravno da jednakost tada traži ukupnu disipaciju niti da se viskozni rad na presjecima zanemaruje. Blok je označen „Dublje”, pa je rizik manji.
Prijedlog: jedna rečenica: „Za turbulentni tok Φ treba zamijeniti ukupnom disipacijom (viskoznom i turbulentnom), a viskozni rad na ulaznom i izlaznom presjeku zanemaruje se.”

**P2-5. Oznake čvorova i „piezometarska” naspram „energijska” visina.**
Mjesto: (13.18) „čvorova A i B”, h_AB (PDF str. 250) uz sl. 13.1 koja koristi C i D; P3, „Traži se” 3 „razliku piezometarskih visina između A i C” (`:486`, str. 255).
Opis: (13.18) i sl. 13.1 koriste različite oznake istih čvorova (K6). U P3 se računaju gubitci energijske visine; to je razlika piezometarskih visina samo ako se zanemare brzinske visine u čvorovima.
Prijedlog: u (13.18) rabiti iste čvorove kao sl. 13.1 ili opće „I i II”; u P3 „razliku energijskih visina” ili dodati zanemarenje brzinskih visina.

**P2-6. Kratice bez definicije pri prvoj uporabi (K5).**
Mjesto: „RANS” (`:62`, `:113`; str. 246, 248); „NPSH” (str. 245; kratica se nigdje ne razvija, hrvatski naziv stoji samo u opisu (13.27)).
Prijedlog: „Reynoldsovo osrednjene jednadžbe (engl. *RANS*)” i „neto pozitivna usisna visina (engl. *NPSH*)” pri prvom spomenu. RANS je možda definiran u ranijem poglavlju; ako jest, dovoljno je upućivanje.

### P3

**P3-1. Razina zadataka.**
Z2 (T1): student bira model za λ prema režimu za dva fluida i predviđa ponašanje pri 2Q; to je izbor modela, bliže T2/T3. Z4 (T2): iterativni Colebrook, presjecište krivulja i lanac snaga spajaju tri modela, bliže T3. Z1 je inverz P1 (ista struktura, druga nepoznanica): T1 je pošteno, ali raznolikost je mala. Ne tražim promjenu, samo autoricinu procjenu.

**P3-2. Naputci i skice otkrivaju postupak (K13, K15).**
Mjesto: ključ Z1 („Pretvori Δp u visinu hg, sastavi ζ, izrazi v…”), Z3, Z4; skica Z5 („λ(Re, ks/D) računaj”, str. 258).
Opis: naputak Z1 gotovo je cijelo rješenje.
Prijedlog: skratiti na usmjeravajuće pitanje; oznaku „računaj” maknuti sa skice.

**P3-3. Granični Re u Z2.**
Z2 B: Re = 4775, tek iznad praga 4000 za Blasius; tekst sam kaže da je 2300–4000 nepouzdano. Prijedlog: kratka napomena u ključu da je rezultat B osjetljiv na prag.

**P3-4. Empirijski pragovi bez izvora (K14).**
„Swamee–Jain odstupa oko 1 %” (str. 250), pragovi 2300/4000 i Blasius 4000–10⁵ navedeni su kao orijentacija, ali bez izvora uz tvrdnju. Za (13.16) nije naveden raspon ks/D (10⁻⁶–10⁻²); u Z5 (0,005) je zadovoljen.

**P3-5. Što nedostaje za nastavak studija.**
(a) Nema tablice tipičnih ξ (ulaz, koljeno, ventil, naglo proširenje) ni ks (čelik, lijevano željezo, PVC) ni upućivanja na izvor; (b) nema hidrauličkog promjera za nekružne presjeke (brodski kanali, ventilacija); (c) serijski i paralelni rad dviju crpki nije spomenut, a čest je u balastnim i rashladnim sustavima; (d) izvod ξ za naglo proširenje (Borda–Carnot) nije u poglavlju; možda je u ranijem, to nisam provjeravao. Predlažem najmanje (a) i (b), kratko.

**P3-6. Vjerodostojnost podataka u P6 (K16).**
Brzina u usisnoj cijevi 2,8 m/s uz usis iznad razine (zs = +2,6 m) viša je od uobičajene za usis. Prijedlog: Q = 0,010 m³/s (v = 1,99 m/s) ili D = 100 mm, uz prepravak brojeva.

**P3-7. Provjere koje ponavljaju isti račun.**
P1 („Δp/(ρg) vraća ukupni gubitak”) i P2 („podudaranje dvaju zapisa”) algebarski su isti račun; bolja bi bila provjera reda veličine ili neovisna metoda.

**P3-8. Interni nazivi i pitanja u uvodima blokova (K1, K4).**
Poveznice numeričkog pokusa sadrže `u10_moody_dijagram` (`:205–207`), a slika `u10_fig_…` (`:65`). Boldirani uvodi CFD blokova (str. 248, 250, 251, 253) postavljaju pitanja; K4 pitanja rezervira za Zastani i promisli. Ne mogu procijeniti je li bilježnica `u10_` namjerno u pog. 13.

## Što je posebno dobro

- Redoslijed Q, v, Re, λ, hg i upozorenje na referentnu brzinu uz svaki ξ.
- Izvod λ = 8τ/(ρv²) i provjera da je laminarni Δp razmjeran Q, a ne Q² (otklanja čestu zabludu).
- Granice modela su jasne: NPSHa ne jamči odsutnost kavitacije; afinitetni zakoni ne vrijede uz statičku visinu (P4 to pokazuje brojem 0,865 prema 0,899).
- Ključ Z6 imenuje što nedostaje za odluku (margina, NPSHr pri sniženoj brzini, zaprljani filtar, zrak pri njihanju); CFD blokovi opisuju postupak i ne iznose neprovedene rezultate.
- Z1–Z6 slijede raspodjelu 2×T1, 2×T2, T3, T4; podatci su dostatni.

Ograničenja: nisam provjeravao sadržaj bilježnica; skice 13.1–13.4 pregledao sam samo na rasteru (npr. završetak EGL-a u spremniku B nije se dao razlučiti); brojeve sam provjerio samo za ono što je tiskano u PDF-u i ključu.
