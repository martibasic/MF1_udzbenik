# Revizija U07 — 22. rujna 2026.

## Matrica prije provedbe

Opseg: šest vježbi i osam povezanih skica. Kanonski verifier je `verify_u08`,
namespace `U08`; datoteke skica `u08_*` pripadaju javnom U07. Tekst teorije
i riješenih primjera ostaje usporedni izvor. Prethodne lokalne izmjene U05/U06
i korisničkih omotača čuvaju se snimkom hash vrijednosti.

| P/Z | Princip, postupak i uloga | Odluka i didaktička korist | Razina / ID |
| --- | --- | --- | --- |
| P1 | Integracija paraboličnog profila, srednja naspram vršne brzine | Zadržati; podloga za protok kroz plohu | T2; postojeći |
| P2 | Difuzor, kontinuitet, omjer površina i maseni protok | Zadržati; Z1 čuva jednostavnu računsku tehniku | T2; postojeći |
| P3 | Stalna volumenska akumulacija i vrijeme porasta razine | Zadržati; stari Z5 ponavlja ovaj račun | T2; postojeći |
| P4 | Miješanje i akumulacija; masena pa volumenska bilanca | Zadržati; Z6 dodaje intervalnu odluku | T3; postojeći |
| P5/P6 | Razvod protoka, zadani omjer/identične grane i blokada | Zadržati; Z4 zahtijeva vezu brzina i površina | T2; postojeći |
| Z1 | Protok kroz proširenje, izravna računska vježba | ZADRŽATI, očuvati temeljnu tehniku | T1; postojeći |
| Z2 | Sapnica, isti niz računa kao Z1 i P2 | ZAMIJENITI: predznačeni protok kroz kosu zamišljenu plohu, kut prema normali | T1; `task-protok-kroz-kosu-kontrolnu-plohu` |
| Z3 | Dva ulaza i jedan izlaz vode | ZADRŽATI; osnovna višegranska bilanca, precizirati stacionarnost i gustoću; ukloniti neupotrijebljene ulazne promjere | T2; postojeći |
| Z4 | Razdjelnik s omjerom brzina, sustav dvije jednadžbe | ZADRŽATI; zadani omjer nije posljedica samih promjera | T2; postojeći |
| Z5 | Cilindrični spremnik, izravno vrijeme punjenja | ZAMIJENITI: komora s gibajućim klipom i izlazom kroz klip, relativni tok, akumulacija i hod | T3; `task-klip-s-protocnim-otvorom` |
| Z6 | Homogeno miješanje, intervali i slobodni bok | PREPRAVITI samo pretpostavke i potpunost odgovora: aditivni volumeni, zajamčene granice, prelijevanje prekida model | T4; postojeći |

Novi Z2 i Z5 su autorske nastavne konstrukcije, `rewrite_status=preradeno`,
`rewrite_level=P3`, `sketch_requirement=obavezna`. Mijenjaju scenarij,
geometriju, ulaze i izlaze; nisu samo novi brojevi. Stari ID-jevi ostaju span
aliasi, novi naslovi zadržavaju mjesta Z2/Z5. Za Z1/Z3/Z4 rekonstrukcija nije
potrebna; Z6 je ciljano preciziranje istog problema. Svih šest skica obvezno
je zbog orijentacije plohe, kontrolnog volumena ili više protoka.

Staro → novo:

- `task-u08-voda-ulazi-u-sapnicu-promjera-srednjom-brzinom` → Z2 gore.
- `task-u08-cilindricni-spremnik-promjera-puni-se-dotokom-dok` → Z5 gore.

## Skice i plan provjera

U početnim skicama krajnje pune linije cijevi izgledaju kao čepovi; T-komad
ima sastavljene neujednačene otvore i preklopljene gradijente. Budući porast
razine P3/P4 izgleda kao zaseban fluid; ulazne cijevi završavaju u zraku bez
mlaza koji povezuje dotok sa sadržajem. U zbirnoj sceni promjeri su kotirani
kao uzdužne udaljenosti, a rast tlaka u difuzoru navodi se bez energijskog
modela. Z1 ima dužu strelicu brzine u širem presjeku. Uvodni blok mora jasno
razlikovati apstraktnu granicu KV od krutoga kućišta.

Zadržati veličine i raspored panela, paletu, tipografiju i šrafure. Svaki
stvarni prolaz ostaviti otvorenim, isti fluid crtati jednim kontinuiranim
poljem. Pokretni klip ima dva kruta prstenasta dijela i stvaran otvor između
njih. Kosa kontrolna ploha nije stijenka; normalu i kut provjeriti vektorski.
Kinematičku skicu provjeriti prema stvarnoj tangenti krivulje.

Plan provjera: neovisne bilance i granični slučajevi, SVG geometrija i vizualni
pregled, D03 i generatorski D06/manifest, povezani notebook, potpuni HTML/PDF,
tipkovnica, povratne poveznice i očuvanje omotača.

## Provedeno i provjereno

Z2 sada provjerava normalnu komponentu i predznak protoka: 6,00 L/s i
5,988 kg/s za zadanu normalu, suprotne predznake za obrnutu orijentaciju.
Z5 zatvara RTT na klipu: izlazni relativni protok 0,4712 L/s, brzina klipa
0,06732 m/s, apsolutna izlazna brzina 1,5673 m/s, hod 1,7824 s i porast mase
0,9406 kg. Za zaustavljeni klip isti dotok zahtijeva izlaznu brzinu 3,1831 m/s.
Neovisno su uspoređeni integrirani protoci s volumenom ostvarenoga hoda,
te granice bez izlaza i bez gibanja klipa.

Z1 ostaje računski nepromijenjen. Z3 zadržava iste protoke i izlazni promjer;
izbačeni su ulazni promjeri koji nisu sudjelovali u traženom računu. Z4 ima
izričito zadani radni omjer brzina. Z6 ima aditivne volumene, zajamčene
intervale i granicu modela pri prelijevanju. Nominalno je rho_mix = 1021,3 kg/m³
i akumulacija oko 2558 kg. Ekstrapolirani maksimalni porast 0,5774 m pokazuje
da šest minuta rada prelazi zadani slobodni bok; rub se doseže za 349,0 s.
Maksimum je potvrđen svim osam kutnim kombinacijama; porast je linearan,
rastući u oba dotoka i padajući u izlaznoj brzini, pa nema skrivenoga maksimuma
unutar intervala. Nakon ruba porast nije fizička razina iznad stijenke,
nego znak da treba uključiti dodatni preljevni izlaz.

Pregledano je osam SVG-ova, sedam je dorađeno. Difuzor P2 već ima otvorene
presjeke, dobar omjer promjera i dosljedne smjerove te je zadržan. Kinematika
dobiva precizne tangente i položaje čestice na stvarnoj krivulji. Ostali
popravci obuhvaćaju otvorene priključke, T-komad kao jednu domenu ulja,
pravilne kote razina i promjera te uklanjanje lažnih slojeva buduće vode.
Uvodna primjena sada prikazuje ventiliranu komoru s otvorenim vodovima.
Veličine i raspored panela sačuvani su, kao i postojeća tipografija,
šrafure i osnovna paleta. `check_u07_sketch_geometry.py` provjerava stvarni
kut i normalu, tangente, otvor klipa i njegov omjer d/D, otvorenost priključaka
te omjere kota; vizualni pregled proveden je zasebno.

Izvršene provjere:

- `verify_u08`: 58 rezultata, od toga 48 brojčanih i 10 bilančnih/graničnih
  invarijanti; sve prolazi. `verify_all`: 1144 rezultata (1000 brojčanih,
  144 invarijante) i 22 zasebne fizikalne provjere; nema rupa u 90 ugovora.
- Audit strukture: 87 primjera i 90 vježbi u knjizi, šest propisanih razina
  U07; normalizacija, generatori D06/manifesta, Typst audit i diff provjera prolaze.
- Povezani `u08_kontinuitet_suzenje.ipynb` pregledan i izvršen u čistom
  kernelu; ostaje parametarski pokus suženja i nestacionarnog spremnika.
- Puni HTML render, prikaz U07 na 320/768/1440 px bez vodoravnog prelijevanja,
  12 sklopivih blokova s upravljanjem tipkovnicom, oba stara aliasa i šest
  povratnih poveznica D06. Svih osam SVG-ova ima tekst unutar okvira.
- Puni PDF render i audit: 309 A4 stranica. Vizualno pregledane skice,
  zadatci na 141–142 i ključ na 297–298. D06 sadrži sve rezultate, kriterije
  i zatvorenu inline matematiku; Z6 se u ključu nastavlja na sljedećoj stranici.
- Aktualni PDF kopiran u `_site/downloads/`; audit stranice: 24 HTML stranice,
  212 slika, 1918 poveznica i 434 sklopiva bloka.

Tekst teorije i P1–P6 uspoređen je s početnom kopijom i ostao isti. Sadržaj
prethodnih revizija U05/U06 očuvan je. QMD omotači nisu uređivani; u radnom
stablu se tijekom rada pojavila i razlika završetaka redaka omotača U05/U06,
bez sadržajnog git diffa. Ne pripada autorskoj reviziji U07.

Provjere geometrije i CI nisu dokaz didaktičke kvalitete; ona ostaje autorska
procjena. Crteži su shematski, a duljine svih strelica nisu jedinstvena skala
brzina. Z5 je kinematička masena bilanca, bez proračuna pogonskih sila.
Lokalno je korišten Quarto 1.9.32 (CI: 1.9.37); postojeća Typst upozorenja
`times.circle` u U10 ostaju. Puni JupyterLite build i udaljeni Actions nisu
pokretani. Nema commita ni pusha.

### Dopuna provjera prije zajedničke objave U05–U07

Na korisnikov zahtjev za commit i push ponovno su provjereni brojčani
rezultati i izvršeno svih 17 notebookova u čistim kernelima: sve prolazi.
Puni JupyterLite build sada je izvršen, a audit potvrđuje 17 notebookova,
četiri proširenja i Python (Pyodide). Audit renderirane stranice prolazi
za 24 HTML stranice, 212 slika, 1918 poveznica i 434 sklopiva bloka.
QR kodovi i generirani ključ aktualni su, a CFD provjera prolazi za sva
tri paketa. Nedostajući alati instalirani su u privremeno lokalno Python
okruženje, bez promjene projektnih ovisnosti.

## Revizija 12. 10. 2026.

Provedba nalaza stručne recenzije (recenzent mehanike fluida), odobrena od
autorice. Opseg: teorija (RTT, bilanca mase, granica modela, CFD odlomci),
P1, P2, Z1, Z3, Z5, Z6, četiri skice, verifier `verify_u08`, checker
`check_u07_sketch_geometry.py`. Bilježnica `u08_kontinuitet_suzenje.ipynb`
koristi vlastite podatke (12 L/s, 120/60 mm, spremnik s $k\sqrt h$) i nije
mijenjana.

| P/Z | Princip, postupak i uloga | Odluka i didaktička korist | Razina / ID |
| --- | --- | --- | --- |
| Teorija | RTT iskazan bez izvoda, iza bilance mase | PREPRAVITI: izvod RTT-a (sustav u $t$ i $t+\Delta t$, rubni volumeni, limes, provjera predznaka) prije bilance mase; bilanca mase kao $\eta=1$; blok Granica modela; naziv „Reynoldsov transportni teorem”; energijska jednadžba iz RTT-a sada u pog. 8 | `eq-rtt-dva-trenutka`; stari ID RTT-a zadržan |
| P1 | Difuzor, kontinuitet | ZADRŽATI uz realne podatke: $v_2=1{,}6$ m/s → $v_1=3{,}6$ m/s, 40,7 L/s, 40,6 kg/s | T2; postojeći |
| P2 | Izjednačni spremnik, isti postupak kao P3 | ZAMIJENITI: zahvatni usis morske vode na brodu u plovidbi, kontrolni volumen vezan uz brod, relativna naspram apsolutne brzine | T2; `ex-zahvatni-usis-morske-vode-u-plovidbi` |
| P3 | Miješajući spremnik | ZADRŽATI; skraćena provjera | T3; postojeći |
| P4 | T-komad | ZADRŽATI; „ogranak 2” | T2; postojeći |
| P5 | Rashladni krug EV | ZADRŽATI; CFD odlomak razdjelnika premješten iza njega (sidro `#cfd-razdjelnik-podjela-protoka` sačuvano) | T2; postojeći |
| Z1 | Proširenje cijevi, klon P1 | ZAMIJENITI: grijač ventilacijskog zraka strojarnice, promjena gustoće, masena naspram volumenske bilance | T2; `task-grijac-ventilacijskog-zraka-strojarnice` |
| Z2 | Kosa kontrolna ploha | ZADRŽATI (predznak normale, provjera RTT-a) | T1; postojeći |
| Z3 | Komora za miješanje | ZADRŽATI; razina T2 → T1 (primjena zadanog zakona) | T1; postojeći |
| Z4 | Razdjelna glava | ZADRŽATI | T2; postojeći |
| Z5 | Klip s protočnim otvorom | ZADRŽATI; indeksi ul/iz | T3; postojeći |
| Z6 | Miješajući spremnik, ≈P3 | ZAMIJENITI: balastni tank dvodna, morska i slatka voda, prebačajna crpka, odzračna cijev, zajamčeni intervali i odluka o nadzoru | T4; `task-balastni-tank-dvodna-mijesanje-i-odzracnik` |

Raspored ostaje 2×T1 (Z2, Z3), 2×T2 (Z1, Z4), T3 (Z5), T4 (Z6); šest
riješenih primjera.

Staro → novo (stari ID-jevi ostaju span aliasi):

- `ex-u08-izjednacni-spremnik-tijekom-ispiranja-filtra-t2` → P2 gore (primjer;
  bez aliasa jer se na njega ništa nije upućivalo).
- `task-u08-voda-struji-kroz-cijev-koja-se-siri` → Z1 gore.
- `task-u08-mijesajuci-spremnik-tlocrtne-povrsine-prima-vodu-gustoce` → Z6 gore.
- `fig-u08-izjednacni-spremnik-s-akumulacijom` → `fig-zahvatni-usis-morske-vode`
  (ista datoteka `u08_val3_izjednacni_spremnik.svg`, novi prizor).

Kontrolni rezultati: P2 $\dot m=51{,}3$ kg/s, $w=1{,}25$ m/s, $w_r=2{,}27$ m/s,
$v_{aps}=8{,}01$ m/s (pogrešni račun apsolutnom brzinom 328 kg/s). Z1
$\dot m=4{,}32$ kg/s, $v_2=17{,}6$ m/s, $Q_1=3{,}60$, $Q_2=4{,}24$ m³/s. Z6
$\rho_{mix}=1021{,}6$ kg/m³, $dh/dt=1{,}312$ mm/s, $h(15\ \text{min})=1{,}48$ m,
$\Delta m=43{,}4$ t; konzervativno 1,460 mm/s, 1,61 m > 1,60 m, odzračnik za
890 s. Nominalno prolazi, zajamčeno ne.

Skice: `u08_val3_izjednacni_spremnik.svg` (novi prizor zahvatnog usisa, isti
viewBox), `u08_val1_difuzor_kontinuitet.svg` (oznaka $v_2$),
`u08_vjezbe_skice.svg` (paneli Z1 i Z6 unutar postojećih okvira). Checker
provjerava otvoren prednji otvor usisa, antiparalelne brzine broda i relativne
brzine, KV koji obuhvaća otvor, omjer visina kanala 0,30:0,24 s grijačem u
fluidu te omjer razina 0,30:1,60 i otvorenu odzračnu cijev balastnog tanka.
Vizualni pregled i PDF izvedenice pripadaju koordinatoru.

Notacija: $m_{KV}$, indeksi ul/iz, $\vec v$, KV/KP u cijelom poglavlju.
Nije rađeno: commit, generatori s `--write`, D01–D06 (koordinator).

## Revizija 19. 10. 2026. — didaktičko pojačanje (odobreno u razgovoru)

Zahtjev autorice: zadatci su prelagani i prečesto ponavljaju riješene primjere; kroz poglavlja uvesti po koji zahtjevniji zadatak ili zakomplicirati primjer, ne dodavati tekst. Zahvat unutar šest mjesta Z1–Z6 i raspodjele T1, T1, T2, T2, T3, T4; broj primjera ostaje. Stari ID-jevi zamijenjenih zadataka ostaju kao prazni `<span>` aliasi.

| Mjesto | Staro | Novo | Razina | Didaktička korist |
| --- | --- | --- | --- | --- |
| Z4 | Raspodjela protoka po granama (ponavljanje kontinuiteta) | Protok iz izmjerenog profila brzine (`task-protok-iz-izmjerenog-profila-brzine`): trapezna integracija $\int v\,2\pi r\,dr$ iz tablice sedam točaka, $Q=0{,}561$ m³/s, $v/v_{max}=0{,}79$, $\dot m=0{,}673$ kg/s; $v_{max}$ precjenjuje 26 %, zakon 1/7 daje 0,817 | T2 | Integralna definicija protoka na stvarnim (sintetičkim) podatcima umjesto formule $Q=vA$; numerička integracija i usporedba s empirijskim profilom. Puni ključ u D06. |

Skica Z4: izmjereni profil (`u08vs_fix_z4_v0..v5`), sivi dimenzijski markeri dodani zbog podudaranja boje vrha i crte; panel proširen. `verify_u08.py`: `zadatak_4`, `U08.INV.z4_profile_sum`. D03 §7 dopunjen.

Prošlo nakon zahvata: pripadni `verify_*`, `verify_all`, `audit_publication`, `qa_audit`, `audit_sketch_design` (s `check_u*_sketch_geometry`), `audit_print_layouts`; D06 i manifest regenerirani generatorima, `print-layouts.json` hash obnovljen. Vizualna provjera skice obavljena headless renderom u PNG. Didaktička procjena je autorska; studentski pilot nije proveden.
