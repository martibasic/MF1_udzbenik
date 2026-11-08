# Stručna recenzija — skupina G1 (pog. 1–4)

Recenzent: neovisni agent (stručni recenzent mehanike fluida), 8. 11. 2026.
Materijal: `G1.pdf` (knjiga str. 12–88), `G1_kljuc.pdf` (dodatak F, str. 334–339),
izvori `source/u01_…`–`source/u04_…`, bilježnice `notebooks/u01_…`–`u04_…`.
Stranice su stranice knjige (otisnuti broj), retci se odnose na `source/`.
Ponovni izračun proveden je u Pythonu u mapi `rad/`. Pet poznatih nalaza
iz zadatka (a)–(e) nije ponovno prijavljeno.

## Sažetak

Poglavlja 1–4 fizikalno su vrlo solidna: od 24 riješena primjera i 24 zadatka
svi brojčani rezultati i kontrolni rezultati u ključu slažu se s mojim
računom unutar zaokruživanja, a izvodi (tetraedar, Couetteov sloj,
Young–Laplace, hidrostatika, paraboloid i očuvanje volumena) korektni su.
Jedini ozbiljan nalaz jest fizikalno nekonzistentan zadatak s obješenim
spremnikom (pog. 4, Z2). Ostali nalazi tiču se logike jednog izvoda, nedosljedne
definicije ulaža, ponavljanja riješenih primjera u zadatcima, predugih blokova
„Granica modela” i zaokruživanja.

Broj nalaza: P0 – 0; P1 – 1; P2 – 9; P3 – 9.

---

## P0 — pogrešan ili opasan zaključak

Nema.

## P1 — bitna znanstvena ili pedagoška pogreška

### P1-1. Obješeni spremnik „bez njihanja” ne može imati traženi nagib površine prema stijenkama

- **Mjesto:** `u04_relativno_mirovanje_fluida.md:679–705`,
  `task-spremnik-na-dizalici-dva-ubrzanja` (Z2, str. 85); skica Z2 na str. 87
  (`fig-u04-vjezbe`); napomena uz skice `u04:853`; ključ str. 338.
- **Opis:** Spremnik „visi na lučkoj dizalici”, kolica ubrzavaju vodoravno
  ($a_x=1{,}5\ \mathrm{m/s^2}$), a skica prikazuje spremnik obješen o jednu
  kuku preko dviju stropi, s vodoravnim dnom. Napomena kaže da spremnik „visi
  bez njihanja”. Obješeno tijelo u ustaljenom stanju pri stalnom ubrzanju ne
  ostaje okomito: cijeli sustav (užad, spremnik i voda) zakrene se tako da
  pravac uža prolazi težištem i leži u smjeru $\vec g_{eff}$. Kut otklona
  jednak je kutu slobodne površine, $\tan\theta=a_x/(g+a_z)=0{,}136$. Zato je
  u ustaljenom stanju slobodna površina usporedna s dnom spremnika, a razlika
  razina uz stijenke $\approx0$, a ne $0{,}272\ \mathrm{m}$. Tlak na dnu tada je
  $\rho_v g_{eff}h_0\approx1000\cdot11{,}11\cdot0{,}80\approx8{,}9\ \mathrm{kPa}$,
  a ne $10{,}3\ \mathrm{kPa}$. „Bez njihanja” znači samo da nema oscilacija oko
  tog otklonjenog položaja, ne da je spremnik vodoravan. Student koji to uoči
  ne može uskladiti svoj zaključak s ključem. Ovaj primjer nosi i
  inženjersku pouku za rukovanje teretom: tekući teret na dizalici ne pokazuje
  nagib prema spremniku, nego se cijeli teret otkloni.
- **Prijedlog:** Spremnik kruto učvrstiti na vođeni nosač (npr. „na platformi
  koju vitlo diže uz krute vodilice, a platforma se istodobno vodoravno
  pomiče”) ili ga postaviti na vozilo s dizalom. Ako se želi zadržati
  dizalica, preokrenuti pitanje: neka student pokaže da se obješeni spremnik
  otkloni za $\theta$ i da je površina u njegovu okviru vodoravna. Uskladiti
  skicu Z2, napomenu uz skice i ključ.

## P2 — jasnoća, dosljednost, manji tehnički nedostatak

### P2-1. Neumanjeni prijenos promjene tlaka ne ovisi o zanemarivanju $\rho g\Delta z$

- **Mjesto:** `u01:7` (str. 12), `u01:183` (izvod „Pascalov zakon i očuvanje
  rada”).
- **Opis:** Uvod kaže da je „porast tlaka u cijelom sustavu *praktički* isti”
  jer su tlakovi klipova mnogo veći od visinskih razlika. Izvod kaže da
  neumanjeni prijenos „pokazuje hidrostatička jednadžba: tlakovi se razlikuju
  samo za $\rho g\Delta z$, koji ovdje zanemarujemo”. Za nestlačiv mirujući
  fluid razlika $p_2-p_1=-\rho g(z_2-z_1)$ ne ovisi o opterećenju, pa je
  *promjena* tlaka $\Delta p$ ista u svakoj točki točno, bez obzira na
  $\Delta z$. Zanemarivanje $\rho g\Delta z$ potrebno je tek za ravnotežu
  apsolutnih sila na klipove (početno stanje), kao u P6 (stezna naprava).
  Sadašnji zapis sugerira da je Pascalov zakon približan.
- **Prijedlog:** U izvodu: „Razlika $\rho g\Delta z$ ne mijenja se pri
  opterećenju, pa se nametnuta promjena tlaka prenosi neumanjena u svaku
  točku. Član $\rho g\Delta z$ zanemarujemo tek u ravnoteži sila na klipovima
  na različitim visinama.” U uvodu ukloniti „praktički”.

### P2-2. Tvrdnja o nelinearnom profilu nenewtonskog fluida proturječi zadatku Z5

- **Mjesto:** `u02:68` (str. 31) prema `u02:794`
  (`task-newtonski-model-iz-mjerenja`, str. 45).
- **Opis:** Izvod kaže da je za nenewtonski fluid $\tau$ stalan po visini,
  „ali gradijent brzine ne mora biti”. Za uobičajene (vremenski neovisne,
  monotone) nenewtonske modele, $\tau=f(\dot\gamma)$, stalan $\tau$ daje
  stalan $\dot\gamma$, dakle linearan profil. Z5 to ispravno koristi
  („Smični je profil u svakom stacionarnom pokusu linearan; newtonsko
  ponašanje tek treba provjeriti”). Nelinearan profil u Couetteovu sloju javlja
  se tek uz klizanje uz stijenku, nemonotonu krivulju tečenja (smične pruge),
  granicu tečenja ili temperaturni gradijent.
- **Prijedlog:** „…za nenewtonski fluid $\tau$ je i dalje stalan po visini, pa
  je i gradijent stalan ako naprezanje ovisi samo o lokalnom gradijentu;
  newtonski je model tek tvrdnja da je njihov omjer isti pri svim brzinama.”

### P2-3. Ulaž je u istom poglavlju definiran od dviju različitih referenci

- **Mjesto:** `u03:339` (`ex-sondiranje-teretnog-tanka-s-tlacnim-mjeracem-razine`,
  str. 58): „udaljenost od referentne točke (rub ulažnog otvora na palubi) do
  površine tereta”; `u03:521` (`ex-u03-balastni-tank-broda-tlak-iznutra-i-izvana`,
  str. 63): „ulaž, udaljenost od vrha tanka do površine”.
- **Opis:** Ista veličina mijenja referencu (K6). U balastnom tanku razinu
  provjerava sondna cijev koja izlazi na palubu (skica 3.6), pa bi ulaž po
  definiciji iz prethodnog primjera trebao uključiti i visinu palube iznad
  pokrova tanka, a ta nije zadana.
- **Prijedlog:** U balastnom primjeru pisati „visina praznog prostora iznad
  balasta, $H_{tk}-h_s$” ili izrijekom reći da se ulaž ovdje mjeri od pokrova
  tanka.

### P2-4. „Kapilarna duljina iz pog. 2” ne postoji u pog. 2

- **Mjesto:** `u04:223` (Granica modela, str. 75).
- **Opis:** Upućuje se na kapilarnu duljinu „iz pog. 2”, ali je
  $L_c=\sqrt{\sigma/(\Delta\rho g)}$ definirana tek u pog. 11
  (`u11:99`, uz Bondov broj) i u dodatku A (`d01:140`). U pog. 2 izraz se ne
  javlja (K5, K12).
- **Prijedlog:** Uputiti na pog. 11 ili u pog. 2 uz kapilarni uspon dodati
  jednu rečenicu s $L_c$ (za vodu oko 2,7 mm).

### P2-5. Kormilarski stroj: moment bez zadanog položaja kormila

- **Mjesto:** `u01:654–679` (`task-kormilarski-stroj-dva-cilindra`, Z2,
  str. 25).
- **Opis:** Tekst kaže da su klipnjače okomite na rudo „u srednjem položaju”,
  ali „Traži se 2” ne veže moment za taj položaj. Uz hod $s=0{,}30\ \mathrm{m}$
  i $r=0{,}60\ \mathrm{m}$ kormilo se otkloni za oko $27^\circ$. Kod
  Rapsonova klizača moment pri otklonu $\delta$ iznosi $2Fr/\cos^2\delta$
  (oko 110 kN m pri $27^\circ$), a ne 88,4 kN m. Rezultat ključa vrijedi samo u
  srednjem položaju (K15: „Traži se” mora biti jednoznačan).
- **Prijedlog:** „Odredi ukupni moment u srednjem položaju kormila.”

### P2-6. Samostalni zadatci ponavljaju riješene primjere s drugim brojevima

- **Mjesto i opis:**
  - pog. 2: Z6 `task-u02-kapilarna-igla-…` (str. 46) isti je problem kao P4
    `ex-u02-kapilarni-mikrodozator-s-izlaznom-kapljicom-t3` (str. 40). Ponavljaju
    se uspon $h_{cap}$, dovoljnost uspona do izlaza i skok $4\sigma/D$; nova je
    samo odluka o regulatoru. P4 izrijekom kaže da se $p_M$ „ovdje ne traži”,
    a Z6 ga traži.
  - pog. 4: Z6 `task-u04-otvoreni-cilindricni-spremnik-…` (str. 86) ponavlja
    P4 `ex-u04-rotirajuci-cilindricni-spremnik-s-granicom-prelijevanja-t3`
    (str. 80): $\omega_{max}$, $h_C$, $h_R$ i tlakovi u osi i uz stijenku. Z1
    `task-u04-otvoreni-pravokutni-spremnik-…` ponavlja P5 (autocisterna,
    str. 82): $\Delta h$, dubine uz stijenke i prelijevanje.
  - pog. 1: Z6 (stol s tri cilindra) jest P4 (platforma s dva cilindra) uz
    dodane faktore učinkovitosti.
- **Opis učinka:** Prema uputi recenzije i AGENTS.md drugi brojevi nisu
  raznolikost. T4-zadatci ipak dodaju stvarnu odluku, pa ovo nije P1.
- **Prijedlog:** U pog. 4 Z1 zamijeniti obrnutim pitanjem (npr. ubrzanje iz
  izmjerenog $\Delta h$ ili nagnuti spremnik s okomitim ubrzanjem). U pog. 2
  Z6 ili P4 preusmjeriti, npr. tako da P4 obradi samo tlačne skokove, a Z6
  odluku. Odluku donosi autorica u ciklusu revizije Z1–Z6.

### P2-7. Blokovi „Granica modela” prelaze opseg iz K11

- **Mjesto:** `u01:140–160` (str. 15), `u02:343–347` (str. 37),
  `u03:197–201` (str. 55), `u04:220–224` (str. 75).
- **Opis:** K11 traži jednu do tri izjavne rečenice. U pog. 1 blok uvodi novu
  teoriju: definiciju modula $K$, numeriranu jednadžbu
  `eq-modul-stlacivosti-volumna-promjena` i bilancu $A_Ls_L\approx\Delta V_p-\Delta V_c$.
  Na tu jednadžbu oslanjaju se P3 i Z4, dakle ona nije granica nego gradivo.
  Naslov tog bloka uz to je pitanje (K4). Blokovi u pog. 2–4 imaju četiri do
  šest rečenica.
- **Prijedlog:** Teoriju modula $K$ premjestiti u kratki odjeljak ili blok
  „Dublje” prije primjera. Granice skratiti na tri rečenice, npr. za pog. 1:
  „Model zanemaruje stlačivost, podatljivost vodova i zrak. Za pomak klipa
  nije mjerodavan omjer $\Delta p/K$, nego $\Delta V_c/\Delta V_p$. Bez te
  usporedbe ne smije se zaključiti da je pomak točan.”

### P2-8. Zaokruživanje: međurezultati i kontrolni rezultati s prekomjernim brojem znamenaka

- **Mjesto:** `u03:243,249` (str. 57: $132506{,}532$ Pa, $31706{,}532$ Pa);
  `u03:442,448` (str. 61: $-20483{,}28$ Pa, $80816{,}72$ Pa); ključ pog. 4 Z5
  ($0{,}45291$ m, $72{,}91$ mm, $1{,}095$ mm) i Z6 ($0{,}35268$; $0{,}56732$ m,
  $2{,}68$ mm), `u04:811,843`.
- **Opis:** K8 traži tri do četiri značajne znamenke za međurezultate i dvije
  do tri za konačni rezultat. Kriterij u Z5 iznosi 5 mm, pa stotinke
  milimetra nemaju mjerni smisao.
- **Prijedlog:** $p_A\approx132{,}5$ kPa, $p_{M,A}\approx31{,}7$ kPa; Z5:
  $h_{str}\approx0{,}453$ m, odstupanje 73 mm odnosno 1,1 mm; Z6: (0,353;
  0,567) m, rezerva oko 3 mm.

### P2-9. Uvod pog. 4 za brod u zavoju koristi „duljinu $L$”, a primjer širinu $b_t$

- **Mjesto:** `u04:3`, `u04:9` i slika 4.1 (str. 71) prema
  `ex-tank-broda-u-kruznom-zavoju` (`u04:359`, str. 79).
- **Opis:** U zavoju je centripetalno ubrzanje poprečno na brod, pa je
  mjerodavna poprečna mjera tanka. Uvod i slika 4.1 govore o „spremniku duljine
  $L$” i o tome da „duljina spremnika mora biti mnogo manja od $R_z$”, a
  primjer ispravno koristi širinu $b_t$ (K6).
- **Prijedlog:** U uvodu i na slici 4.1 pisati „širina tanka $b_t$ (mjera u
  smjeru prema središtu zavoja)”.

## P3 — prijedlozi

1. **Razine.** `u03` Z1 (`task-visina-iz-barometarskog-ocitanja`, T1, str. 64)
   traži dva modela, njihovu usporedbu i razlučivost. To je odluka razine T2,
   a ne primjena jednog zakona. `u04` Z5 (`task-provjera-smirivanja-…`, T3)
   jest odluka iz sintetičkih podataka i kriterija, dakle po definiciji T4.
   `u04` P4 (T3, oznaka `.mf1-ch`) samo uvrštava izraze izvedene na str. 73–74,
   pa je bliži T2. Oznake ne treba mijenjati radi kvote, ali opis razine u
   protokolu treba odgovarati sadržaju.
2. **Rezultat zadatka u teoriji.** `u02:250` i sažetak `u02:877` daju
   $h=2\sigma\cos\theta/(\rho gb)$, a Z4 (str. 45) traži da ga student
   izvede. Iz izvoda predlažem ukloniti „faktor 2 umjesto 4 (Z4)”, a formulu
   ostaviti u sažetku.
3. **Iskustvene tvrdnje bez izvora (K9, K14).** U ključu `u03` Z3 piše „u praksi
   se ne ide ispod 5–10°”, a u `u02:577` (str. 43) „ulje statvene cijevi obično
   radi hladnije od gornje nastavne granice”. Predlažem dodati izvor iz
   dodatka E ili ogradu „nastavna procjena”.
4. **Zaokruživanje sondi.** U `u04:389` (str. 80) sonde pokazuju 1,70 i
   1,50 m, a „razlika očitanja” iznosi 0,19 m. Iz zaokruženih očitanja slijedi
   0,20 m. Predlažem pisati $1{,}697-1{,}503=0{,}194$ m.
5. **Dvostruko numerirane jednadžbe (K10).** `u01:114–121` i `u01:192–195`
   (isti Pascalov omjer); `u04:23` i `u04:71` (isti $\Delta h=aL/g$);
   `u04:114` i `u04:120` (isti paraboloid). Kasniju pojavu predlažem
   uputiti brojem.
6. **Kratica IoT** (`u03:534,538`, str. 63) u pog. 3 javlja se dvaput i nije
   definirana (K5). Predlažem „mrežni (IoT) tlačni senzor” pri prvom spomenu ili
   samo „daljinski tlačni senzor”.
7. **Slike.** Na sl. 3.3 (str. 57) zrak je ispunjen rešetkastom šrafurom kakva
   se drugdje rabi za krute stijenke; predlažem jednoliku svijetlu ispunu.
   Oznake se preklapaju s crtama: na sl. 3.3 „$p_1$”, „$h_1=0{,}60$ m”,
   „$h_2=0{,}10$ m” i „0,40 m”, a na sl. 1.5 (str. 20) „$s_L=25$ mm” sa
   stijenkom crpke i „$s_h=180$ mm” s pokaznom crtom.
8. **Nazivi blokova.** U pog. 4 blok glasi „Interaktivni prikaz —
   Paraboloidna…” (str. 75), a u pog. 1–3 „Numerički pokus — …”. Predlažem
   ujednačiti.
9. **Temperaturna ovisnost viskoznosti.** `u02` Z1 traži linearnu interpolaciju
   viskoznosti glicerina. Viskoznost ovisi o temperaturi približno
   eksponencijalno, pa bi interpolacija $\ln\mu$ bila prirodnija i studentu
   korisna za nastavak studija (podmazivanje, pog. 12–13). Rezultat se gotovo
   ne mijenja: interpolacija $\ln\mu$ daje oko 26,2 °C, a linearna oko 26,4 °C.

**Napomena o materijalu (nije nalaz knjige):** u dostavljenom `G1_kljuc.pdf`
stranice 335, 337 i 338 pojavljuju se dvaput (MD5 teksta stranica 2 = 3,
5 = 6, 7 = 8). Vjerojatno je riječ o artefaktu izdvajanja skupine. Ako se isto
vidi u punom PDF-u, riječ je o pogrešci prijeloma dodatka F.

---

## Provjera brojeva (moj račun)

Sve vrijednosti su moj račun u Pythonu, s podatcima iz teksta. Nijedno
odstupanje nije veće od zaokruživanja, osim nalaza P1-1 (fizikalni model) i
P3-4 (zaokruživanje sondi).

**Pog. 1.** Ulje: $\gamma=8436{,}6$ N/m³, $s_r=0{,}86$; litra ulja lakša je za
$0{,}14\cdot9{,}81=1{,}37$ N. P2: $A_k=0{,}020106$ m², $p_M=179{,}05$ kPa,
$F_2=8{,}057$ kN, omjer 2,238. P3: $p_M=250$ kPa, $F_2=5250$ N,
$s_2=5{,}14$ mm, $W=27$ J. Volumen stlačivanja
$300\cdot10^{-6}\cdot2{,}5\cdot10^5/1{,}5\cdot10^9=0{,}05$ cm³, što je 0,0463 %
od 108 cm³. P4: $p_M=0{,}92$ MPa, $F_G=27{,}6$ kN, $s_p=1{,}50$ m, $s_p/s_h=8{,}33$.
Devet hodova daje $1{,}62\cdot5\cdot10^{-4}/0{,}03=27{,}0$ mm; djelomični hod
iznosi 60 mm, $W=690$ J. P5: $p_M=4{,}775$ MPa, $F_{pr}=4{,}594$ kN,
$F_{st}=3{,}375$ kN, $F_{uk}=15{,}94$ kN, $k=53{,}1$. P6: $p_M=2{,}728$ MPa,
$F_s=1680$ N, $\rho g\Delta z=21{,}09$ kPa, $F_s'=1667$ N; udio 0,77 %, rezerva
2,10.

Zadatci pog. 1: Z1 858; 861; 859,5 kg/m³ i $\bar\gamma=8{,}432$ kN/m³. Z2
$A=0{,}012272$ m², $F=73{,}63$ kN, $M=88{,}36$ kN m, $V=7{,}36$ L. Z3 900 N, 10 mm,
9 J i 81 J. Z4 500 mm², $d=25{,}23$ mm, 200 N, $\Delta V_c=0{,}100$ cm³,
$s=9{,}80$ mm, odstupanje 2,0 %. Z5 2,00 MPa; (100,5 N; 0,5968 m), (127,2;
0,4716), (157,1; 0,3820). Z6 $p_M=947{,}0$ kPa, $F_G=26{,}99$ kN,
$s_p=1{,}350$ m; 23,21 kN i 1,500 m; 22,13 kN i 1,551 m.

**Pog. 2.** Disk: $\omega=62{,}83$ rad/s, $\tau(R)=2262$ Pa, $M=0{,}7675$ N m,
$P=48{,}2$ W, $M'=0{,}384$ N m; udio vanjske polovice polumjera je 15/16.
P2: $300\ \mathrm{s^{-1}}$, 126 Pa, 22,68 N, $\nu=4{,}83\cdot10^{-4}$ m²/s,
disipacija 20,4 W. P3: $h=10{,}80$ mm, uz $\theta=0$ 11,36 mm. P4:
$h_{cap}=36{,}77$ mm, $4\sigma/D=120$ Pa, $4\sigma/d=360$ Pa
$=\rho gh_{cap}$. P5: $u=6{,}283$ m/s, $\tau_1=8378$ Pa, $A=0{,}010996$ m²,
$F_1=92{,}1$ N, $M_1=2{,}303$ N m, $P_1=578{,}8$ W, $P_2=57{,}9$ W. P6:
$h=0{,}3354$ m, $\Delta p=3323$ Pa, $h_{110^\circ}=-0{,}1266$ m.

Zadatci pog. 2: Z1 $270{,}8\ \mathrm{s^{-1}}$, 227,3 Pa, $\mu=0{,}839$ Pa s,
26,4 °C. Z2 100 i 200 Pa. Z3 36 i 18 Pa; 0,72 + 0,36 = 1,08 N, pogrešno
0,24 N. Z4 $h_1=62{,}87$ mm, kružno 125,7 mm, $h_2=-18{,}79$ mm, nadtlak 189 Pa.
Z5 kao u ključu. Z6 $h_{cap}=58{,}83$ mm, $p_{M,1}=0$, $p_{M,2}=571{,}2$ Pa
(raspon 555,2–591,2 Pa), rezerva 8,8 Pa, $\rho gD_{max}=19{,}6$ Pa.

**Pog. 3.** $H=8426$ m; na 8,8 km model daje 35,7 kPa (tekst: „oko 35 kPa”).
P1 132,51 kPa i 31,71 kPa. P2 3394,3 Pa; sa zrakom 3402,5 Pa, 8,24 Pa, 0,24 %.
Geometrija skice 3.3 provjerena je u mjerilu. P3 $h_u=15{,}940$ m,
$U=2{,}310$ m, $h'=16{,}357$ m, $\Delta V=250$ m³, $h''=16{,}296$ m (213 m³),
stupac plina 27,2 Pa. P4 $-20{,}48$ kPa, 80,82 kPa, $H_{max}=11{,}85$ m.
P5 85,47; 65,36; 50,28; 30,17 kPa, neto 35,19 kPa, stanje C 55,30 kPa.
P6 372,0 kPa, $p_{M,B}=147{,}97$ kPa, $h_{vt}=15{,}11$ m, $\Delta h=5{,}11$ m.

Zadatci pog. 3: Z1 $z=1528$ m, $\rho_0=1{,}2256$ kg/m³, 1397 m (−8,6 %),
razlučivost 0,997 m na vrhu i 0,832 m na bazi. Z2 1,800 m. Z3 385,2 Pa,
$\delta=2{,}89$ mm, 408,4 Pa, −5,7 %, osjetljivost 0,453 mm/Pa prema 0,124 mm/Pa.
Z4 $h_u=0{,}6014$ m, granica 5,015 kPa. Z5 0,711; 0,613; 0,0450 m i 8,44; 9,79;
133,4 Pa, $p_{pl}=92{,}6$ kPa. Z6 $p_{pl}=122{,}55$ kPa, 135,28 kPa,
$p_{max}=136{,}05$ kPa, potrebna puna skala 142,85 kPa.

**Pog. 4.** P1 −4,50; 5,886; 1,386 kPa, $\theta=17{,}0^\circ$, 0,459 m,
$a_D=3{,}924$ m/s²; s odzračnikom u B 4,50; 10,39; 5,89 kPa. P2
$\theta_{AB}=70{,}88^\circ$, $s=0{,}5821$ m, $g_{eff}=10{,}383$ m/s², 21,80 kPa;
račun po komponentama daje isto. P3 $a=0{,}2115$ m/s², $\theta=1{,}235^\circ$,
$\Delta h=0{,}194$ m, $v_{max}=15{,}34$ m/s = 29,8 čv; pomak srednje razine
zbog zakrivljenosti 0,40 mm. P4 $\Delta h=0{,}2205$ m, $h_C=0{,}4897$ m,
$h_R=0{,}7103$ m, 4,804 i 6,968 kPa, $\omega_{max}=6{,}644$ rad/s,
63,4 $\mathrm{min^{-1}}$. P5 0,465 m, 0,682 i 0,218 m, prag prelijevanja
5,72 m/s², prag ogoljavanja 7,36 m/s². P6 $\omega=754{,}0$ rad/s, omjer
ubrzanja 6954, $\Delta p=3{,}271$ MPa, $r_i=88{,}96$ mm (uz 950 kg/m³:
140,3 mm), $t_z=14{,}0$ s, $v_{rel}=4{,}97$ mm/s, Coriolisovo ubrzanje
7,49 m/s², omjer $1{,}48\cdot10^{-4}$.

Zadatci pog. 4: Z1 0,220; 0,450; 0,230 m. Z2 (u modelu teksta) 0,2725 m,
0,9362 m, 10,31 kPa; bez $a_z$ 0,3058 m i 9,35 kPa; pri usporavanju 0,3484 m,
0,9742 m i 8,39 kPa. Za fizikalnu primjedbu vidi P1-1. Z3 7,90; 6,40; 4,90 kPa.
Z4 $\omega=7{,}906$ rad/s, 75,5 $\mathrm{min^{-1}}$. Z5 referentne dubine
0,4529 i 0,1471 m; niz I 72,9 mm i 140 mm; niz II 1,10 mm i 2 mm. Z6
$\omega_{max}=7{,}830$ rad/s, (0,3576; 0,5624) m, (3,51; 5,52) kPa;
uz +5 % (0,3471; 0,5729) m, $k_{max}=0{,}7897$, uz $k=0{,}78$ rezerva 2,7 mm.

Dimenzijska homogenost svih radnih izraza (Couette, disk, kapilarnost,
Young–Laplace, izotermalna atmosfera, paraboloid, separator) je u redu.
Redovi veličine su vjerodostojni.

## Ocjena po kriterijima upute

1. **Fizikalna točnost.** Osi, predznaci i reference tlaka vođeni su
   dosljedno. Izvrstan je zapis manometarskog hoda i razlikovanja
   apsolutnog, manometarskog i vakuumskog tlaka (usis crpke: s tlakom pare
   uspoređuje se apsolutni tlak). Iznimke su P1-1, P2-1 i P2-2.
2. **Brojevi.** Vidi gore. Ključ (dodatak F) slaže se s izvorom i s mojim
   računom, a poveznice „Vrati se na zadatak (str. …)” pokazuju na ispravne
   stranice.
3. **Modeli i granice.** Pretpostavke (kvazistatičnost, nestlačivost,
   prianjanje, statički meniskus, relativno mirovanje) navedene su uz svaki
   primjer. Granice uz primjere imenuju zabranjene zaključke (npr. 27,6 kN
   nije nosivost platforme; 11,8 m nije sigurna usisna visina). Blokovi
   Granica modela predugi su (P2-7).
4. **Dosljednost.** Problemi su ulaž (P2-3), $L$ i $b_t$ (P2-9) i kapilarna
   duljina (P2-4). Oznake $p_M$, $p_{pov}$, $h$ i $h_C/h_R$ inače su
   dosljedne kroz tekst, skice i ključ.
5. **Zadatci.** Svi su rješivi iz teksta, osim fizikalne nekonzistencije u
   pog. 4 Z2 i neodređenog položaja u pog. 1 Z2. Raspored razina je 2×T1,
   2×T2, T3 i T4 u svakom poglavlju. Ponavljanja su opisana u P2-6.
6. **CFD i numerika.** CFD odlomci opisuju pitanje, model, ulaze, izlaze i
   test s ručnim računom te ne iznose neprovedene rezultate. Dobri primjeri
   su statički test $p_{rgh}$ u balastnom tanku i razlikovanje ravnotežnog
   nagiba od prvog vala pri kočenju. Bilježnice imaju predviđanje, numerički
   postupak (bisekcija, integracija gradijenta), neovisne provjere i granice,
   a podatci su im usklađeni s P/Z oznakama u knjizi.
7. **Razina.** Razina odgovara prvom kolegiju. Tetraedar, tenzor naprezanja i
   Coriolisov član ispravno su izdvojeni u blokove „Dublje” i izvode. Za
   nastavak studija korisno bi bilo dodati kapilarnu duljinu u pog. 2 (P2-4)
   i barem napomenu o eksponencijalnoj ovisnosti viskoznosti o temperaturi
   (P3-9).

## Što je posebno dobro

- Brojčana pouzdanost je izvanredna: 48 primjera i zadataka bez ijedne
  računske pogreške, uz neovisne provjere u svakom primjeru (bilanca rada,
  disipacija = snaga, $\rho gh_{cap}=4\sigma/d$, dva puta do $p_{M,B}$,
  srednja razina sondi).
- Inženjerski su realni i dobro ograđeni primjeri iz brodogradnje
  (sondiranje teretnog tanka s vodenim talogom i inertnim plinom, balastni
  tank iznutra i izvana, separator goriva s gravitacijskim diskom pri
  stvarnoj razlici gustoća 930/960 kg/m³ i kormilarski stroj).
- Granica relativnog mirovanja u separatoru provjerena je kvantitativno
  (vrijeme zadržavanja i omjer Coriolisova i centrifugalnog ubrzanja),
  a ne samo tvrdnjom.
- T4-zadatci (zajamčeni intervali, konzervativni krajevi, rezerva prema
  zanemarenom učinku) uče stvarnu inženjersku odluku i jasno odvajaju
  nastavni model od dopuštenja za rad.
- Kod kapilarnosti dosljedno se razlikuju konkavni i konveksni meniskus te
  stanja punjenja i formirane kapljice.
