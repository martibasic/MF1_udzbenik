# Stručna recenzija — skupina G4: pog. 14, pog. 15 i dodatak D

Recenzent: neovisni agent (stručni recenzent mehanike fluida), 8. 11. 2026.
Materijal: `G4.pdf` (knjiga str. 263–295 i 323–330), `G4_kljuc.pdf`, izvori
`source/u14_turbostrojevi_i_propulzija.md`, `source/u15_otvoreni_tokovi.md`,
`source/d04_numericka_mehanika_fluida.md`, bilježnice
`notebooks/u12_pelton_lopatica.ipynb` i `notebooks/u15_otvoreni_tokovi.ipynb`.
Radi provjere upućivanja otvoreni su i `source/u10_…`, `source/u08_…`,
`source/d01_…`, `source/d05_literatura.md` i `docs/kurikularna_matrica.md`.
Svi brojevi ponovno su izračunani skriptom (izvan repozitorija).

## Sažetak

Fizika pog. 14 i 15 u izvodima i riješenim primjerima točna je: svi brojevi
riješenih primjera i kontrolnih rezultata slažu se s mojim računom unutar
zaokruživanja, a predznaci (r→f / f→r, sila fluida na tijelo, konvencija
kuta $\beta$ od $-u$) dosljedno su provedeni. Glavne slabosti nisu računske,
nego pedagoške i definicijske: polovica samostalnih zadataka pog. 14 vježba
gradivo pog. 10 dok aktuatorski disk nema samostalnog zadatka, jedno
obrazloženje u kontrolnom rezultatu pog. 15 (Z2) fizikalno je pogrešno, a
pog. 15 Z6 traži odluku na temelju veličine bez definiranog fizikalnog
značenja.

Ukupno: **P0 0, P1 3, P2 11, P3 12.**

## Provjereni brojevi

Ponovno izračunano i potvrđeno (odstupanja samo u zadnjoj znamenci):

- pog. 14: P1 vodilica ($\dot m=12{,}07$ kg/s, $\vec F_{f\to v}=(404{,}4;\,-198{,}6)$ N, $R=450{,}6$ N, $26{,}2^\circ$, $1{,}30$ kW);
  P2 pokretna lopatica ($\dot m_{rel}=25{,}40$ kg/s, $\vec c_2=(-2{,}47;\,7{,}20)$, $F=(723{,}0;\,-182{,}9)$ N, $745{,}8$ N, $7{,}23$ kW, bilanca $7{,}85=7{,}23+0{,}62$ kW);
  P3 Pelton ($u=15{,}41$, $\dot m_{rel}=23{,}65$, $F_x=680{,}3$ N, $M=313$ N m, $10{,}49$ kW; kolo $47{,}04$ kg/s, $1353$ N, $20{,}86$ kW, $\eta_h=0{,}923$, $18{,}8$ kW, bilanca $22{,}60$ kW);
  P4 radijalno kolo ($u_1=9{,}11$, $u_2=19{,}74$, $c_{m1}=3{,}41$, $c_{m2}=2{,}755$, $\beta_1=20{,}5^\circ$, $c_{2t}=13{,}83$, $e=273{,}0$ J/kg, $H_{th}=27{,}8$ m, $12{,}6$ kW, $82{,}9$ N m, rastav $93{,}6+153{,}3+26{,}1$);
  P5 propeler ($C_{Th}=1{,}078$; $v_d=7{,}32$; $v_j=8{,}65$; $19{,}9$ kPa; $P_i=1172$ kW; $\eta_i=0{,}819$; $D'$: $1{,}633$; $7{,}87$; $1259$ kW; $0{,}763$; trag $212$ kW; $\chi=0{,}143$);
  P6 dron ($5{,}886$ N; $v_d=6{,}76$ m/s; $39{,}8$ W; $56{,}9$ W; $227$ W; $19{,}5$ min);
  Z1–Z6 kontrolni rezultati (npr. Z3 $k=0{,}850$, $\beta_2=30{,}00^\circ$, $\dot E_g=0{,}999$ kW; Z6 $3{,}186$ kN, $324{,}7$ kg, $19{,}15$ m/s², $265{,}3$ kg).
- pog. 15: P1–P5 ($Fr=0{,}669$; $y_c=0{,}742$ m, $E_{min}=1{,}112$ m; $y_a=1{,}106$, $y_b=0{,}372$ m, $Fr=0{,}412/2{,}11$; $Fr_1=3{,}83$, $y_2=1{,}235$ m, $\Delta E=0{,}774$ m; Manning $4{,}50/2{,}70$ m³/s);
  Z1–Z6 kontrolni rezultati (Z2 $q=1{,}443$, $C_d=0{,}576$; $a=0{,}8$: $q=2{,}741$, $C_d=0{,}547$; Z4 korijeni $0{,}630231/1{,}009009$ m; Z5 $\Delta_I=-0{,}01648$ m², $s_\Delta=0{,}02010$ m²; Z6 $Q_{cap}=11{,}759/8{,}141/6{,}047$, $y_n=0{,}985/1{,}189/1{,}380$, $y_2=1{,}059$ m).
- Uvodna slika pog. 15 ($q=1{,}40$, $y_0=1{,}30$): kritični presjek traži prag $\approx0{,}48$ m, silovita dubina $0{,}308$ m, spregnuta $0{,}995$ m — skica je s tim u skladu.
- Dodatak D: interpolacija Ladsonovih točaka na $10{,}00^\circ$ daje $C_D=0{,}01166$, nagib $0{,}000891$/°; točno.

## P0 — pogrešan ili opasan zaključak

Nema nalaza.

## P1 — bitna znanstvena ili pedagoška pogreška

### P1-1. Samostalni zadatci pog. 14 većinom ponavljaju pog. 10; aktuatorski disk nema zadatka

- **Mjesto:** `source/u14_turbostrojevi_i_propulzija.md:702–874` (str. 280–281); `task-u12-vodeni-mlaz-brzine-izlazi-iz-kruzne-sapnice` (Z1), `task-pokretna-ploca-i-kolo-s-plocama` (Z2), `task-u12-mlazna-platforma-ukupne-mase-ima-cetiri-jednake` (Z6); usporedi `source/u10_kolicina_i_moment_kolicine_gibanja.md:219–294` (`ex-peltonova-lopatica-u-gibanju`) i `:1025–1056` (`task-mlaz-na-pomicnu-plocu`).
- **Opis:**
  - Z2 je isti problem kao zadatak „Mlaz na ploču koja se udaljava” iz pog. 10 (jedna okomita ploča, $\dot m_{rel}=\rho A(v-u)$, optimum $u=v/3$) spojen s korakom 4 primjera 10.1 (kolo, $u=v/2$), samo s drugim brojevima. U pog. 10 taj je problem označen T3, ovdje T1. Isti par optimuma k tome je izveden u izvodu pog. 14 (`eq-turbostrojevi-matematicki-izvod-optimum-obodne-brzine-za-jednu-03/-07`) i ponovljen u P3.
  - Z1 (sila mlaza na nepomičnu ploču) i Z6 (potisak mlazova $F_T=\rho Av^2$) gradivo su pog. 10; tekst pog. 14 (redak 17) i sam kaže da je bilanca na nepomičnoj vodilici izvedena u pog. 10. Isto vrijedi za riješeni P1 (vodilica).
  - Ishod 3 iz sažetka (redak 893: „iz aktuatorskog diska odrediti induciranu brzinu, idealnu snagu i učinkovitost te objasniti ulogu sustrujanja”) nema nijednog samostalnog zadatka: Z5 (vodomlaz) koristi samo $\eta=2v_s/(v_s+v_j)$, koji je već zadatak Z1 pog. 10. $C_{Th}$, lebdenje, faktor učinka i $v_A=(1-\chi)v_s$ pojavljuju se samo u riješenim primjerima. Ni ishod 2 (trokuti iz kutova lopatica i geometrije kola) nema zadatka: Z4 zadaje gotove apsolutne brzine.
- **Prijedlog:** zadržati Z1 kao jednostavan T1 ako autorica želi zagrijavanje, ali Z2 zamijeniti zadatkom na disku (npr. T1/T2: inducirana brzina i snaga rotora u visu s $FM$ ili usporedba $C_{Th}$ za dva promjera uz sustrujanje), a Z6 po mogućnosti zadatkom s trokutima iz geometrije kola (kutovi $\beta_1$, $\beta_2$, širine $b_1$, $b_2$, predvrtnja $c_{1t}\neq0$ ili turbinski režim s negativnim predznakom). Odluku o zamjeni donosi autorica prema protokolu.

### P1-2. Pogrešno obrazloženje pada $C_d$ u kontrolnom rezultatu pog. 15 Z2

- **Mjesto:** `source/u15_otvoreni_tokovi.md:481` (web; u PDF-u je skriveno, a dodatak F taj dio ne prikazuje, v. P2-8); `task-istjecanje-ispod-ustave`.
- **Opis:** Ključ kaže: „$C_d$ pada na $0{,}547$ jer brzina dolaska uzvodno raste, a raspoloživa razlika $y_0-y_1$ se smanjuje.” Prvi dio je obrnut. Iz naputka je $q=C_ca\sqrt{2g(y_0-y_1)}\,/\sqrt{1-(y_1/y_0)^2}$; faktor $1/\sqrt{1-(y_1/y_0)^2}$ jest učinak brzine dolaska i on **povećava** $q$ i $C_d$. Pad $C_d=C_c/\sqrt{1+C_ca/y_0}$ potječe od smanjenja razlike $y_0-y_1$ u odnosu na $y_0$.
- **Moj račun:** bez člana brzine dolaska $C_d=C_c\sqrt{1-y_1/y_0}$ = $0{,}572$ ($a=0{,}4$ m) i $0{,}530$ ($a=0{,}8$ m); s njim $0{,}576$ i $0{,}547$. Brzina dolaska dakle podiže $C_d$ za $0{,}004$ odnosno $0{,}017$, a ne spušta ga.
- **Prijedlog:** „$C_d$ pada na $0{,}547$ jer veći otvor daje dublji suženi mlaz, pa se razlika $y_0-y_1$ relativno smanjuje; veća brzina dolaska taj pad samo djelomično nadoknađuje.”

### P1-3. Pog. 15 Z6: „dopuštena spregnuta dubina” nema fizikalno značenje, a bazen nije povezan s kanalom

- **Mjesto:** `source/u15_otvoreni_tokovi.md:578–609` (str. 294), skica `fig-otvoreni-tok-vjezbe` panel Z6 (str. 292); `task-klimatski-kanal`.
- **Opis:**
  - $y_{2,dop}=1{,}40$ m nije definiran. U P4 istog poglavlja (redak 315) odluka ovisi o usporedbi spregnute dubine s **nizvodnim vodostajem** $y_{nv}$: $y_{nv}<y_2$ znači da skok odlazi iz bazena. Riječ „dopuštena” sugerira gornju granicu (npr. visinu zida), pa student zaključak „$y_2=1{,}059<1{,}40$ m, dakle u redu” ne može povezati ni sa sigurnim ni s nesigurnim stanjem. Bilježnica (ćelija 11, `y2_design<y2_allowed<y2_cap[0]`) i pitanje 7 tretiraju $y_{2,dop}$ kao raspoloživu nizvodnu dubinu, ali to nigdje ne piše. „Traži se 2” zato nije jednoznačan (K15).
  - Kanal pri $Q_d$ teče mirno ($Fr=0{,}62/0{,}44/0{,}33$ za A/B/C), a bazen ima silovit ulaz $y_1=0{,}350$ m pri $b_{baz}=5{,}00$ m, $E_1=1{,}415$ m. Tekst ne kaže kako mirni tok iz kanala ($E\approx1{,}12$ m za stanje A) postaje silovit; za to treba pad dna ili brzotok od najmanje oko $0{,}3$ m. Skica prikazuje bazen „iza kanala” bez ikakve građevine između njih.
- **Prijedlog:** preimenovati u „raspoloživa nizvodna dubina u bazenu $y_{nv}$” (kao u P4), u „Traži se 2” tražiti odluku ostaje li skok u bazenu i navesti kriterij $y_2\le y_{nv}$; u tekstu dodati spoj (npr. brzotok s padom dna $\Delta z$) ili izrijekom reći da je $y_1$ zadan izmjerom na kraju brzotoka.

## P2 — jasnoća i manji nedostatci

### P2-1. Vodomlazni pogon nije aktuatorski disk

- **Mjesto:** `source/u14_turbostrojevi_i_propulzija.md:5` (str. 263).
- **Opis:** „Propeler i vodomlazni pogon modeliraju se aktuatorskim diskom”. Vodomlazni pogon u knjizi se (ispravno) računa bilancom količine gibanja i energije za kanal s crpkom (`eq-potisak-mlaznog-pogona`, Z5); s diskom dijeli samo izraz za idealnu učinkovitost.
- **Prijedlog:** „Propeler se modelira aktuatorskim diskom; vodomlazni pogon ima isti izraz za idealnu učinkovitost, $\eta_i=2v_A/(v_A+v_j)$, …”

### P2-2. Froudeova učinkovitost izvedena dvaput (K10)

- **Mjesto:** `u14…:193–197` (`eq-idealna-ucinkovitost-propelera`, str. 268) prema `u10…:177–182` (`eq-aktuatorski-disk-potisak`).
- **Opis:** Jednadžba pog. 10 već sadrži $\eta_i=F_Tv_A/(F_Tv_d)=v_A/v_d=2v_A/(v_A+v_j)$. Pog. 14 izvodi isti izraz ponovno i daje mu novu oznaku; izraz se ponavlja još u uvodu (redak 5) i u provjeri (redak 207).
- **Prijedlog:** u pog. 14 uputiti na `eq-aktuatorski-disk-potisak` i izvesti samo ono novo: zapis preko $C_{Th}$ (`eq-idealna-ucinkovitost-ct`) i lebdenje.

### P2-3. Pelton P3: podatak $P_G$ bez zahtjeva, proturječni „Traži se 4” i razina T4

- **Mjesto:** `u14…:365–467` (str. 272–274); `ex-u12-peltonov-rotor-s-jednim-mlazom-i-momentom`.
- **Opis:**
  - $P_G=9{,}5$ kW zadan je, ali ga nijedna stavka „Traži se” ne koristi. Moj račun: $P_{lop}\eta_m\eta_G=10{,}49\cdot0{,}96\cdot0{,}94=9{,}46$ kW. Podatak dakle odgovara upravo pogrešnom modelu jedne lopatice, pa student koji zastane nakon stavke 4 dobiva „potvrdu” pogrešnog rezultata.
  - Stavka 4 traži „snagu koju mlaz predaje rotoru”, a rješenje (redak 446) odmah kaže da $10{,}49$ kW **nije** snaga kola. Isto vrijedi za „moment na obodu rotora” $M=313$ N m, kojem u rotirajućem kolu ne odgovara nijedno stvarno stanje.
  - Razina T4: nema podataka s nesigurnošću, a obrazložena odluka (rad generatora na oko polovici snage) stoji samo u rješenju. Prema stvarnoj odluci (izbor kontrolnog volumena) primjer je T3.
- **Prijedlog:** u stavci 4 pisati „snagu predanu toj jednoj lopatici u modelu lopatice koja se udaljava”; dodati stavku „Usporedi raspoloživu električnu snagu s $P_G$ i objasni koji bi model doveo do pogrešnog zaključka da je kolo jedva dovoljno”. Tada je oznaka T4 opravdana; inače T3.

### P2-4. Skica radijalnog kola ne odgovara $\beta_2=25^\circ$

- **Mjesto:** `u14…:482`, `fig-radijalno-kolo-crpke-trokuti` (str. 275).
- **Opis:** Lopatice su nacrtane kao ravne dužine koje izlazni krug sijeku pod oko $65^\circ$ prema tangenti (izmjereno na gornjoj lopatici: oko $25^\circ$ od radijalnog smjera). Izlazni trokut na istoj slici ispravno ima $\vec w_2$ pod $25^\circ$ od $-u$. Lopatica i relativna brzina, koja prema tekstu „ima smjer lopatice”, zato se na slici ne podudaraju. `fig-alt` govori o „unatrag zakrivljenim lopaticama”, a nacrtane su ravne. Smjer zakretanja unatrag je ispravan.
- **Prijedlog:** nacrtati zakrivljene lopatice koje na $r_2$ zatvaraju $25^\circ$, a na $r_1$ $20{,}5^\circ$ s tangentom (smjer $-u$), uz isti stil skice.

### P2-5. „Faktor klizanja” nije definiran (K5)

- **Mjesto:** `u14…:532` (str. 276).
- **Opis:** Pojam se javlja samo ovdje, a nema ga ni u dodatku A ni u pojmovniku. Uz to „pretpostavljeni umnožak … $\approx0{,}82$” nema izvor.
- **Prijedlog:** jednom rečenicom: „konačan broj lopatica ne skreće fluid točno po lopatici, pa je stvarni $c_{2t}$ manji od idealnog; omjer se naziva faktor klizanja (engl. *slip factor*)”. Vrijednost označiti kao nastavnu procjenu ili je potkrijepiti izvorom.

### P2-6. Pog. 14 nema nijedan izvor; empirijski raspon $\eta_0$ nije potkrijepljen (K14)

- **Mjesto:** `u14…:584` („$\eta_0\approx0{,}55$–$0{,}70$”, str. 277); cijelo poglavlje: 0 citata. U `d05_literatura.md` nema nijednog djela o turbostrojevima ni brodskim propelerima.
- **Opis:** Tvrdnje o rasponu učinkovitosti propelera u slobodnoj vožnji, o klasičnom optimumu Peltonove turbine i o faktoru učinka rotora iskustvene su ili udžbeničke. Za studente brodogradnje i strojarstva upravo ovo poglavlje treba uputu na daljnje čitanje.
- **Prijedlog:** dodati u dodatak E po jedan standardni izvor za turbostrojeve (crpke i turbine) i za brodske propelere te ih citirati uz $\eta_0$, uz $H_{th}$ i klizanje te uz Froudeov teorem. Ako izvor nije dodan, raspon označiti kao orijentaciju („red veličine za brodske propelere”).

### P2-7. Koeficijenti ustave i preljeva bez izvora i bez raspona valjanosti (K9, K14)

- **Mjesto:** `u15…:173–183` (`eq-istjecanje-ispod-ustave`, `eq-preljev-siroki`, str. 286).
- **Opis:** $C_d\approx0{,}55$–$0{,}60$ i „$C_{pr}$ … blizu jedinice” stoje bez citata. Raspon $C_d$ vrijedi samo za određeni raspon $a/y_0$. Z2 to i pokazuje: pri $a/y_0=0{,}4$ dobiva se $C_d=0{,}547$, izvan navedenog raspona, iako je model isti.
- **Prijedlog:** „uz $C_c\approx0{,}61$ i $a/y_0\approx0{,}1$–$0{,}3$ je $C_d\approx0{,}55$–$0{,}60$ [@chow1959]” (ili drugi izvor koji to stvarno navodi), a za $C_{pr}$ navesti izvor ili ogradu.

### P2-8. Ključ u dodatku F izostavlja dijelove rezultata

- **Mjesto:** `G4_kljuc.pdf`, str. 351 (F.15 Z2) i 352 (F.16 Z2); izvori `u14…:749`, `u15…:481`.
- **Opis:** Za pog. 14 Z2 ključ završava rezultatom (b) i izostavlja optimume ($u=v/3$, $\eta_{max}=29{,}6\,\%$; $u=v/2$, $F=220$ N, $P=3{,}31$ kW, $\eta_{max}=50\,\%$), koje traži „Traži se 2”. Za pog. 15 Z2 izostavljen je cijeli dio 3 ($a=0{,}800$ m: $q=2{,}741$ m²/s, omjer $1{,}90$, $C_d=0{,}547$). Čitatelj PDF-a za te dijelove nema kontrolni rezultat (K8: isti rezultat u rješenju i ključu). Čini se da se ključ skraćuje ako polje nema oznaku `data-key-full` (ima je samo pog. 15 Z5).
- **Prijedlog:** označiti ta dva odgovora za puni prijenos u ključ ili provjeriti pravilo skraćivanja za sve višedijelne zadatke.
- **Napomena:** u isječku `G4_kljuc.pdf` stranica 352 pojavljuje se dvaput. To je vjerojatno artefakt izrade isječka, a ne knjige; nisam mogao provjeriti cijeli dodatak F.

### P2-9. Oznaka $y_1$ u pog. 15 Z4 suprotna dogovoru iz uvoda (K6)

- **Mjesto:** `u15…:522` (`task-kontrolni-presjek-na-pragu`, str. 293) i skica Z4 (str. 292); usp. redak 9 (uvod) i 170.
- **Opis:** Uvod određuje $y_0$ kao uzvodnu mirnu dubinu, a indekse 1 i 2 kao presjeke ispred i iza skoka. U istom poglavlju $y_1$ je i suženi mlaz ispod ustave (redak 170, Z2). U Z4 je $y_1=1{,}200$ m mirna uzvodna dubina, a u Z6 $y_1=0{,}350$ m silovita ulazna dubina bazena. Student koji pamti da je „1 siloviti presjek” u Z4 lako krivo odabere granu.
- **Prijedlog:** u Z4 pisati $y_0$ (i $E_0$ u naputku i ključu).

### P2-10. Tablica „Povezani primjeri” u dodatku D u PDF-u nema brojeve (K12)

- **Mjesto:** `d04…:5–12` (str. 323).
- **Opis:** U tiskanoj inačici poveznice postaju goli tekst („početni model → podjela protoka → …”) bez broja poglavlja ili odjeljka, pa čitatelj ne može pronaći mjesto.
- **Prijedlog:** uz svaki odlomak dodati „pog. N” ili upućivanje na odjeljak brojem, kao u ostatku dodatka.

### P2-11. Literatura za CFD bez potpunog zapisa (K14)

- **Mjesto:** `d04…:183` (str. 330).
- **Opis:** Versteeg i Malalasekera te Ferziger, Perić i Street navedeni su samo autorom i naslovom, bez izdanja, izdavača i godine, a nema ih u `d05_literatura.md`.
- **Prijedlog:** dodati ih u dodatak E s aktualnim izdanjima i citirati ih ključem.

## P3 — prijedlozi

1. **Izraz „bez viskoznih gubitaka izvan tlačnog skoka”** (`u14…:177`, str. 268) sugerira da su u skoku gubitci. Bolje: „bez viskoznih gubitaka; energija se fluidu predaje samo tlačnim skokom na disku”.
2. **Preporuka u P5** (`u14…:584`): „bira se najveći propeler koji gaz i trup dopuštaju” jača je od dokaza (K9). Dodati da veći promjer traži manju brzinu vrtnje i veći moment. „Odbitak potiska” (`u14…:213`, d01) nigdje nije definiran; dovoljna je jedna rečenica ili izostavljanje.
3. **Engleski izrazi i kratice (K5):** MRF (`u14…:136`) bez „engl.”; *figure of merit* (`u14…:594`) i *squat* (`u15…:56`) bez „engl.”; u dodatku D (`d04…:162–163`) „CFL3D/SSTm” i „NASA TMR” nisu objašnjeni.
4. **Skice — preklapanja i nedefinirane oznake:**
   - preklapanja: „fluid → lopatica” (sl. 14.3), „radijalno ↑” (sl. 14.5), „v = 30 m/s” (Z2), „dva vodoravna dovoda” i „v = 36 m/s” (Z6) na sl. 14.7, oznake $Fr=1$/$v_c$/$y_2$ na sl. 15.1, „$y_{kon}$” na sl. 15.2;
   - nedefinirane oznake: točka „B” na sl. 14.4 i šrafirani pravokutnici na gornjem vodu Z6 nisu objašnjeni; strelica $F_y$ na sl. 14.4 gotovo je nevidljiva;
   - potpisi „Vodilica mlaza na ispitnom stolu.”, „Pokretna zakrivljena lopatica.” i „Peltonov rotor s jednim mlazom.” naslovi su, a ne opisne rečenice (K13).
5. **Razine riješenih primjera:** pog. 15 P2 (kritični presjek, jedan izraz) i P5 (Manning, jedan zakon s dva $n$) prema stvarnoj odluci su T1, a ne T2. Pog. 15 P2 nosi naslov „na širokom preljevu”, ali preljev ne koristi; može se dodati korak $H=E_{min}$ i izraz `eq-preljev-siroki`.
6. **Granica modela skoka** (`u15…:284`) ima četiri rečenice, a K11 dopušta jednu do tri; posljednja rečenica može prijeći u tekst odjeljka.
7. **Opisno upućivanje** „(vidi odjeljak o kontrolnim građevinama)” (`u15…:165`) treba zamijeniti s `@sec-kontrolne-gradevine` (K12).
8. **Gustoća zraka u P6** (`u14…:594`): ISA na 1500 m daje $p=84{,}56$ kPa i $\rho=1{,}058$ kg/m³ (pri $5^\circ$C $1{,}059$). Zadanih $1{,}045$ kg/m³ (−1,3 %) ne mijenja zaključak, ali valja navesti tlak ili uzeti $1{,}06$.
9. **Pog. 15 Z4, ključ:** šest do sedam značajnih znamenaka (K8). Opravdano je zahtjevom $\varepsilon_E=10^{-6}$ m, ali bi bilo čitljivije $y_t=1{,}0090$ m uz napomenu o rezidualu.
10. **Dodatak D:**
    - redak 167 spominje „Validator `python tools/validate_cfd_vv.py`”; to je uz K1 granični slučaj, pa predlažem formulaciju „skripta uz pakete provjerava …”;
    - odlomak „Veza sa Z6 u pog. 12” (retci 169–173) izvodi dio rješenja zadatka iz drugog poglavlja; dovoljno je uputiti na zadatak;
    - okvir granice modela (redak 176) nema prefiks „Granica modela —” kao ostali okviri.
11. **Gradivo za nastavak studija:**
    - pog. 14: bezdimenzijska karakteristika propelera ($J$, $K_T$, $K_Q$, $\eta_0=JK_T/(2\pi K_Q)$) bila bi prirodan most od diska do „računa po lopaticama” koji P5 spominje, a brodograditeljima je nužna;
    - pog. 15: uz `eq-postupno-promjenjivi-tok` nedostaje razvrstavanje nagiba (blagi ili strmi prema $y_n\gtrless y_c$) i tipova profila razine. Bez toga jednadžba ostaje bez primjene.
12. **CFD odlomci s naslovom u obliku pitanja** („Propeler iza trupa: kad trebamo pojedine lopatice?”, `u14…:218`; „Hoće li prag uzvodno podići vodu?”, `u15…:230`) — prema K4 predlažem izjavni oblik, ako se pravilo primjenjuje i na podnaslove okvira.

## Što je posebno dobro

- Pog. 14 izričito razdvaja dva optimuma obodne brzine ($c_1/3$ i $c_1/2$) prema zahvaćenom protoku. Taj se odnos vraća u granici modela, sažetku i bilježnici, pa je čest izvor zabune riješen na razini kontrolnog volumena.
- Predznaci su vrlo dosljedni: $M_{r\to f}$ prema $M_{f\to r}$, $P_{r\to f}$ prema $P_{f\to r}$, sila vodilice na fluid prema sili fluida na vodilicu, jedinstvena konvencija kuta $\beta$ od $-u$ uz $\theta=180^\circ-\beta_2$.
- Gotovo svaki riješeni primjer zatvara energijsku bilancu (gubitak u lopatici i izlazna kinetička energija, rastav Eulerova rada na tri člana, kinetička energija traga diska).
- Zadatak Z3 pog. 14 (obrnuti račun iz sile uz uvjet pasivnosti) i Z5 pog. 15 (rezidual impulsne funkcije s ispravno koreliranim $q$ i kriterijem $2s_\Delta$) dobri su T2 i T4 zadatci koji mijenjaju vrstu razmišljanja.
- Pog. 15 jasno razlikuje $y_h$, $R_h$ i $D_h$ te energijsku bilancu od bilance količine gibanja u skoku. Odluka o položaju skoka prema nizvodnom vodostaju (P4) fizikalno je točna.
- CFD odlomci ne iznose neprovedene rezultate. Dodatak D pošteno označuje sintetičke pakete i nastavne pretpostavke nesigurnosti te ne izjednačuje GCI sa standardnom nesigurnošću.
- Bilježnice provjeravaju točno one vrijednosti koje su u kontrolnim rezultatima (asertacije za Z3–Z6).

## Ograničenja recenzije

- Ladsonove točke i vrijednost FUN3D ($C_D=0{,}01222$) nisam mogao provjeriti u izvorniku; provjerio sam samo račun koji se na njih oslanja.
- Web inačicu nisam pregledao; skice sam pregledao u PDF-u pri 110–250 dpi.
- Ocjena razina T1–T4 i prijedlozi zamjena autorska su procjena recenzenta, a ne provjera alatom.
