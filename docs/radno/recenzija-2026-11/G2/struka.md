# Stručna recenzija — skupina G2 (pog. 5–8)

Recenzent: neovisni stručni recenzent mehanike fluida (agentsko čitanje prema
`.claude/skills/recenzija-prirucnika/references/struka.md`).
Materijal: `G2.pdf` (knjiga str. 89–168), `G2_kljuc.pdf`, izvori
`source/u05_…`–`source/u08_…`, bilježnice `u05_sila_na_ravnu_plohu`,
`u06_zakrivljena_ploha`, `u07_gaz_plivajuceg_tijela`, `u08_kontinuitet_suzenje`,
`u09_venturi`. Ponovni izračuni: `rad/g2_struka/racun.py` u mapi materijala.
Stranice su stranice knjige (PDF stranica + 88).

## Sažetak

Poglavlja 5–8 fizikalno su ispravna: svih 24 riješenih primjera i 24 kontrolna
rezultata ponovno sam izračunao i nijedno odstupanje ne prelazi zaokruživanje, a
predznaci, normale, reference tlaka i bilance momenata dosljedno su provedeni.
Bitni nedostatci nisu u računu, nego u jednoj netočnoj brojčanoj ilustraciji
učinka slobodne površine, u nekoliko nenavedenih pretpostavki i u
ponavljanju istog obrasca „primjer + omotač intervala” u zadatcima T4.

Brojčano stanje nalaza: P0 = 0, P1 = 1, P2 = 10, P3 = 10.

## P0 — pogrešan ili opasan zaključak

Nema nalaza. Nisam našao pogrešan predznak, pogrešan broj ni zaključak koji bi
vodio na nesigurnu odluku.

## P1 — bitna znanstvena ili pedagoška pogreška

### P1-1. Učinak slobodne površine: brojčani primjer opisuje nemoguće stanje i daje pogrešnu usporedbu

- Mjesto: `source/u06_uzgon_plivanje_i_stabilnost.md:338`, blok „Dublje — Učinak
  slobodne površine u tanku”, str. 116; ID jednadžbe `eq-ucinak-slobodne-povrsine`,
  upućuje na `ex-u07-izolirani-puni-bocni-tank-kao-dodana-masa`.
- Opis: tekst kaže da bi tank iz primjera „napola pun morem, pri istoj
  istisnini” imao $\delta GM=-270/4172\approx-0{,}065$ m, pa bi „$GM$ pao s
  $4{,}23$ na oko $4{,}16$ m”. Napola pun tank ne može imati istu istisninu ni isti
  $KG$ kao pun tank: ima upola manju masu vode, s težištem na $0{,}75$ m umjesto
  $1{,}5$ m. Usporedba zato sugerira da je napola pun tank lošiji od punoga za
  $0{,}07$ m, a za taj trup vrijedi obrnuto. Učinak je tema sigurnosti broda, pa
  je pogrešna brojčana usporedba bitna, iako je opća poruka (slobodna površina
  smanjuje $GM$) točna.
- Moj račun (napola pun tank, voda $1{,}5$ m u tanku):
  $m_v=1025\cdot135=138{,}4$ t; $m=4138{,}4$ t; $KG=(4000\cdot3{,}0+138{,}4\cdot0{,}75)/4138{,}4=2{,}925$ m;
  $T=3{,}3645$ m, $KB=1{,}682$ m; $V_{ist}=4037{,}4\ \text{m}^3$, $BM=22\,500/4037{,}4=5{,}573$ m;
  $GM_{kruto}=4{,}330$ m; $\delta GM=-270/4037{,}4=-0{,}067$ m; $GM_{ef}\approx4{,}26$ m
  (pun tank: $4{,}23$ m).
- Prijedlog: ili izračunati stvarno napola puno stanje ($4{,}33\to4{,}26$ m) i
  reći da je ovdje povoljniji niži teret, a slobodna površina ga djelomično
  poništava; ili ilustraciju preformulirati bez pozivanja na taj primjer, npr.
  „tank iste mase tereta, ali sa slobodnom površinom širine $b_t$, smanjio bi
  $GM$ za $\rho_t i_t/\Delta$”. Rečenicu „pri istoj istisnini” ukloniti.

## P2 — jasnoća i manji nedostatci

### P2-1. U dva riješena primjera nije zadana gustoća vode

- Mjesto: `u05…:231` (`ex-u05-kosi-poklopac`, str. 94) i `u05…:589`
  (`ex-u05-zglobni-cetvrtcilindricni-poklopac`, str. 102).
- Opis: tekst glasi samo „Voda miruje”; rezultati su izračunani s
  $\rho=998\ \mathrm{kg/m^3}$. Opća napomena o $\rho=998$ stoji tek u uvodu
  zadataka za vježbu (`u05…:688`) i ne vrijedi za primjere. S
  $\rho=1000$ dobiva se $F=13{,}98$ kN umjesto $13{,}95$ kN, odnosno $F_H=8{,}309$ kN
  umjesto $8{,}292$ kN. Razlika je malena, ali primjer nije rješiv iz vlastitog
  teksta (K15).
- Prijedlog: dodati „gustoće $\rho=998\ \mathrm{kg/m^3}$” u oba teksta zadatka.

### P2-2. Z1 pog. 5: pretpostavka o prijenosu opterećenja na zasune nije u tekstu zadatka

- Mjesto: `u05…:698` i naputak `u05…:708`, `task-u05-ravna-pravokutna-zaklopka`
  (`task-vodonepropusna-vrata-naplavljenog-odjeljka`), str. 104.
- Opis: podjela $F/2$ na šarke i zasune slijedi iz momenta oko osi šarki i
  točna je. Podjela između gornjeg i donjeg zasuna ($7{,}94$ i $6{,}22$ kN)
  vrijedi samo ako vrata nose opterećenje vodoravno (svaka vodoravna traka
  predaje polovinu svoje sile svakom rubu), pa rub uz zasune prima opterećenje
  raspodijeljeno kao $p(h)/2$ s hvatištem u $h_{CP}$. Bez toga je raspodjela
  između zasuna statički neodređena (šarke duž cijelog ruba). Pretpostavka
  stoji samo u naputku, koji je skriven u PDF-u. Zbog te odluke oznaka T1
  podcjenjuje zadatak.
- Moj račun potvrđuje brojeve uz tu pretpostavku: $F=28{,}31$ kN,
  $h_{CP}=2{,}297$ m, donji zasun $14{,}16\cdot0{,}897/1{,}60=7{,}94$ kN.
- Prijedlog: u tekst dodati „Vrata nose opterećenje kao niz vodoravnih traka
  oslonjenih na šarke i zasune.” Razinu razmotriti kao T2.

### P2-3. Nestacionarnost se poistovjećuje s akumulacijom mase

- Mjesto: `u07…:66`, str. 133.
- Opis: „Nestacionarno strujanje javlja se pri pokretanju i zaustavljanju
  crpke, zatvaranju ventila te pri punjenju i pražnjenju spremnika, kada član
  akumulacije $dm_{KV}/dt$ nije jednak nuli.” Pri pokretanju crpke ili
  zatvaranju ventila u krutoj cijevi s nestlačivom tekućinom strujanje je
  nestacionarno, a $dm_{KV}/dt=0$. Skriveni odgovor u „Provjeri sebe” to točno
  razlikuje, ali vidljivi tekst sugerira suprotno.
- Prijedlog: razdvojiti na dvije rečenice: „Nestacionarno je strujanje pri
  pokretanju crpke ili zatvaranju ventila. Pri punjenju i pražnjenju spremnika
  usto je $dm_{KV}/dt\neq0$; u krutoj cijevi s nestlačivom tekućinom
  akumulacije nema ni kad je strujanje nestacionarno.”

### P2-4. Dvosmislena tvrdnja o kavitaciji kao „nužnom, ne i dovoljnom uvjetu”

- Mjesto: `u08…:225` (Granica modela, str. 156) i `u08…:852` (Sažetak, str. 168).
- Opis: nije rečeno čemu je uvjet nužan. Logički vrijedi: srednji apsolutni
  tlak iznad tlaka pare nužan je, ali ne i dovoljan uvjet **izostanka**
  kavitacije; srednji tlak na tlaku pare ili ispod njega dovoljan je dokaz da
  kavitacija nastupa. Formulacija „zaključak o kavitaciji samo je nužan uvjet”
  može se čitati obrnuto.
- Prijedlog: „Ako je srednji apsolutni tlak iznad tlaka pare, kavitacija nije
  isključena: lokalni minimum može biti niži.”

### P2-5. Granica modela u pog. 6 sadrži novu teoriju koju primjeri rabe kao alat

- Mjesto: `u06…:265–275`, `eq-poluga-okomiti-bokovi`, str. 114; rabi se u
  `u06…:481` i `u06…:636`.
- Opis: blok „Granica modela” uvodi točan izraz $GZ=(GM+\tfrac12BM\tan^2\varphi)\sin\varphi$
  za okomite bokove, koji dva primjera rabe kao „neovisnu kontrolu”. K11 traži
  da granica ne sadrži nastavak teorije. Tvrdnja „pri $\varphi=5^\circ$ pada ispod
  0,5 %” vrijedi za omjer $BM/GM$ te platforme (moj račun: $0{,}46$ %), što
  tekst navodi, ali se zatim proglašava „razlogom zadane granice” za Z3 i Z6.
  Za Z3 ($BM/GM\approx1{,}00$) korekcija je $0{,}38$ %, za Z6 ($BM/GM=1{,}19$) $0{,}46$ %,
  pa je zaključak ovdje točan, ali slučajno.
- Prijedlog: izvod premjestiti u matematički izvod „Krivulja stabiliteta”, a u
  granici ostaviti jednu do tri rečenice s pravilom
  $\tfrac12(BM/GM)\tan^2\varphi$ kao mjerom.

### P2-6. Razina T4 na dvama riješenim primjerima u pog. 6 nije opravdana

- Mjesto: `u06…:486` (`ex-u07-plutajuca-servisna-platforma-na-granici-ulja-i`,
  str. 119) i `u06…:640` (`ex-u07-izolirani-puni-bocni-tank-kao-dodana-masa`,
  str. 122).
- Opis: u oba je model zadan („Primijeni ekvivalentni dvofluidni model”,
  „Primijeni metodu dodane težine”), nema podataka s nesigurnošću ni odluke
  među alternativama. Student spaja dva modela, što je T3 prema protokolu.
- Prijedlog: označiti T3 ili u primjer uvesti stvarnu T4 odluku (npr. izbor
  između metode dodane težine i izgubljenog uzgona s obrazloženjem).

### P2-7. Zadatci T4 u pog. 6, 7 i 8 ponavljaju riješeni primjer s drugim brojevima i omotačem intervala

- Mjesto: pog. 6 Z6 (`task-u07-pravokutna-servisna-platforma-duljine-i-sirine-pluta`,
  str. 127) prema `ex-u07-plutajuca-servisna-platforma-na-granici-ulja-i`;
  pog. 7 Z6 (`task-balastni-tank-dvodna-mijesanje-i-odzracnik`, str. 147)
  prema `ex-u08-mijesajuci-izjednacni-spremnik-s-porastom-razine-t3`;
  pog. 8 Z6 (`task-u09-idealni-sifon-promjera-prazni-otvoreni-spremnik-tako`,
  str. 166) prema `ex-u09-privremeni-sifon-za-praznjenje-servisnog-bazena-t2` i
  `ex-u09-domet-slobodnog-mlaza-iz-velikog-spremnika-t2`.
- Opis: prvi zahtjev svakog Z6 isti je postupak kao primjer (isti model, isti
  traženi izlazi), a jedina nova odluka jest omotač rubnih kombinacija
  ($2^5$, $2^3$, $2^2$ kutova). U pog. 6 isti lanac „rubni gazovi → $\tan\varphi$ →
  $KB$, $BM$, $KG$ → $GM$ → $e$” pojavljuje se u P3, P4 i Z6. U pog. 8 Z6 tekst
  zadatka izrijekom daje obje bilance s gubitcima, pa naputak i tekst zajedno
  rješavaju modelsku odluku (K15). Tri uzastopna poglavlja tako vježbaju istu
  T4 vještinu.
- Prijedlog: zadržati jedan omotač intervala u skupini; u ostalim T4
  mjestima tražiti drugu vrstu odluke (npr. izbor između dvaju modela iz
  izmjerenih podataka, procjena koja nesigurnost dominira i što izmjeriti).
  U pog. 8 Z6 izbaciti zadane formule iz teksta zadatka.

### P2-8. U pog. 7 tri riješena primjera traže istu odluku ($Q=vA$ uz zadanu podjelu)

- Mjesto: `ex-u08-voda-struji-kroz-difuzor-t2` (str. 139),
  `ex-u08-kontinuitet-kroz-razvodni-t-komad-hidraulicnog-sustava` (str. 143),
  `ex-u08-rashladni-krug-baterijskog-paketa-elektricnog-vozila-t2` (str. 144);
  usporedi i Z3 (`task-u08-u-komoru-za-mijesanje-ulaze-dvije-vodene`).
- Opis: sva tri primjera jesu $A_1v_1=A_2v_2$ ili $Q=\sum Q_i$ uz poznate udjele,
  označena T2. Materijalna derivacija nema nijedan brojčani primjer, iako
  poglavlje tvrdi da je konvektivno ubrzanje ključ za suženje i pripremu za
  pog. 8, 10 i 12.
- Prijedlog: jedan od primjera T-komada ili rashladnog kruga zamijeniti
  kratkim primjerom konvektivnog ubrzanja u linearnom suženju
  ($a_x=v\,dv/dx$), uz broj i usporedbu s $g$.

### P2-9. Upućivanje na pokretne lopatice preskače pog. 10

- Mjesto: `u07…:211` (str. 136) i `u07…:444` (str. 141).
- Opis: tekst kaže da je član relativnog toka „presudan za pokretne lopatice u
  pog. 14”. Pokretni kontrolni volumen uz Peltonovu lopaticu riješen je u
  pog. 10 (`source/u10_…:151` izrijekom kaže „Taj se model, uveden u pog. 7,
  ovdje primjenjuje na lopaticu”).
- Prijedlog: „za pokretnu lopaticu i mlazni pogon u pog. 10 te radno kolo u
  pog. 14”.

### P2-10. Preklapanje oznaka u skicama u tisku

- Mjesto: Slika 5.8, paneli Z2 („$L=1{,}20$ m” preko desne stijenke,
  „$b=1{,}50$ m” preko kote $H$, „$b$: okomito na presjek” preko dna) i Z4
  („$F_{max}$” preko kote $H$), str. 106; Slika 8.5 (`fig-usisni-vod-rashladne-crpke`:
  „P” i „crpka”, „u rashladni sustav” i „platforma strojarnice” preko kote $z_P$,
  „1,5 m” preko kote), str. 161; Slika 8.7, panel Z6 („$z_C=$” preko stijenke,
  „$p_{atm}=101{,}3$ kPa” preko cijevi sifona, „$D=70$ mm” preko dna), str. 167.
- Opis: fizikalna povezanost je ispravna (provjerio sam otvor koša, suhu
  unutrašnjost trupa, uronjen ulaz sifona, mjerilo visina u Z6), ali dio
  oznaka nije čitljiv u tisku.
- Prijedlog: obnoviti tiskovne izvedenice prema sustavu tiskovnih figura i
  pregledati konačni PDF.

## P3 — prijedlozi

1. **Os nagiba pri izvodu $BM$.** `u06…:194`, str. 112: „oko uzdužne osi koja
   prolazi kroz njegovu vodnu liniju”. Jednaki klinovi (stalna istisnina)
   zahtijevaju os kroz težište vodne linije; za simetričnu vodnu liniju to je
   uzdužna simetrala. Predlažem „kroz težište vodne linije”.
2. **Strujna cijev.** `u07…:49`, str. 132: „U stacionarnom strujanju fluid ne
   prolazi kroz njezin plašt”. Fluid u danom trenutku ne prolazi kroz plašt ni
   u nestacionarnom strujanju, jer je brzina tangentna na strujnice. Stacionarnost
   je važna zato što cijev tada ne mijenja oblik. Predlažem preformulaciju.
3. **Četvrtina valjka u provjeri izvoda.** `u05…:409`, str. 98: $|F_V|=\rho gb\pi R^2/4$
   vrijedi samo kad je pomoćni volumen četvrtina kruga (središte na slobodnoj
   površini). Za drugu orijentaciju luka $V^*=R^2b(1-\pi/4)$. Dodati „sa
   središtem na slobodnoj površini”.
4. **Bilježnica kontinuiteta.** `notebooks/u08_kontinuitet_suzenje.ipynb`, odjeljak
   „Izračunaj — nestacionarni račun spremnika metodom konačnih volumena” i poruka
   „FV bilanca”: riječ je o eksplicitnoj Eulerovoj integraciji jedne obične
   diferencijalne jednadžbe za cijeli spremnik, ne o metodi konačnih volumena.
   Poglavlje (str. 137) uvodi FVM kao diskretizaciju polja; naziv u bilježnici
   miješa numeričku integraciju i CFD (kriterij 6).
5. **Iskustvene vrijednosti bez izvora ili ograde (K9, K14).** $\alpha=1{,}03$–$1{,}1$
   za turbulentni tok (`u08…:190`, str. 155); „brzine od 1,6 do 3,6 m/s
   uobičajene su za vodu u cijevima” (`u07…:377`, str. 139); „gaz od oko 78 m …
   odgovara redu veličine izvedenih plovnih osnova tipa spar” (`u06…:844`, str. 125).
   Dodati izvor iz dodatka E ili oznaku „orijentacijski”.
6. **Spar bez balasta.** `u06…:833–840`, str. 125: „bez balasta” je ilustriran s
   $KG=45$ m uz nepromijenjenu masu i gaz. Bez balasta masa i gaz nisu isti.
   Predlažem „uz isti gaz, ali težište na 45 m”.
7. **Omotač rubnih kombinacija.** Naputci pog. 6 Z6, pog. 7 Z6 i pog. 8 Z6:
   provjera samo vrhova intervala konzervativna je ako je izlaz monoton u
   svakom ulazu. Za ove modele to vrijedi, ali uvjet treba izreći jednom
   rečenicom.
8. **Struktura pog. 8.** Odjeljak „Kada se trenje može zanemariti” (`u08…:159`)
   sadrži izvod energijske jednadžbe s gubitcima i strojevima, a uvod
   (`u08…:7`) kaže „Model ne sadrži trenje, rad strojeva…”, iako poglavlje
   uvodi $H_p$, $H_t$ i $h_g$. Predlažem uvod „Bernoullijev model ne sadrži …;
   opća energijska jednadžba dodaje …” i naslov odjeljka s energijskom jednadžbom.
9. **Nazivlje.** `u06…:927`, str. 126: „uvjet stabilnosti”, a poglavlje inače
   dosljedno rabi „stabilitet”. „Torricellijeva formula” u naputku pog. 8 Z1
   nije uvedena u vidljivom tekstu (samo u skrivenom „Provjeri sebe”); primjer
   mlaza (str. 152) izvodi isti izraz bez imena.
10. **Granica modela u pog. 5.** `u05…:412–419`, str. 98: četiri natuknice; K11
    traži jednu do tri rečenice. Četvrtu (čvrstoća, zamor, brtvljenje) moguće je
    spojiti sa sažetkom ili uvodom, gdje se već ponavlja.

## Ponovni izračun (sažeto)

Svi brojevi u nastavku slažu se s tekstom, ključem (dodatak F) i bilježnicama
unutar zaokruživanja; navodim samo kontrolne vrijednosti.

| Mjesto | Moj račun | Tekst |
| --- | --- | --- |
| Pog. 5 P1–P6 | $205{,}6$ kN, $3{,}714$ m; $13{,}95$ kN, $0{,}679$ m, $7{,}89$ kN; $48{,}15$ kN, $1{,}894$ m, $32{,}58/15{,}57$ kN; $66{,}67/74{,}28/99{,}81$ kN, $x_V=0{,}584$ m; $26{,}36/29{,}07/39{,}24$ kN, $-47{,}8^\circ$; $F_s=13{,}03$ kN | isto |
| Pog. 5 Z1–Z6 | $28{,}316$ kN, $2{,}297$ m, $7{,}94/6{,}22$ kN; $-5{,}948/-5{,}287$ kN, $M_A=-8{,}327$ kN m; $h_C=1{,}443$, $y_{otv}=2{,}309$ m, $R=3{,}74$ kN; $b_{max}=1{,}1673$ m; $F_s=0{,}9035$ kN, $R_O=(-10{,}19;-11{,}31)$ kN; $z=1{,}74$ | isto |
| Pog. 6 primjeri | $V=0{,}6012$, $T=0{,}2088$ m; $GM=0{,}2449$ m, $e=0{,}134$ m (točno $0{,}1352$); $GM_{eq}=0{,}4289$ m, $e=0{,}1644$ m; $GM=4{,}228$ m, $\varphi=3{,}94^\circ$, $\varphi_{lim}=31{,}1^\circ$; spar $T=77{,}64$, $BM=0{,}116$ m | isto |
| Pog. 6 Z1–Z6 | $\Delta T=0{,}132$ m, $316$ t; $GM=0{,}038$, $b_{min}=0{,}584$ m; $GM=0{,}5724$, $KG=0{,}1412$ m; $\rho_x=992{,}4$; plan B $GM=0{,}1857$ m; $e=0{,}3209$, $e_{max}=0{,}3546$ m (32 kombinacije) | isto |
| Pog. 7 | $Q=2{,}945$ L/s; $v_1=3{,}6$ m/s; $w=1{,}25$, $w_r=2{,}27$, $v=8{,}01$ m/s; $t=255{,}5$ s; $D_3=24{,}8$ mm; $v_d'=0{,}982$ m/s; Z4 $Q=0{,}5611\ \text{m}^3/\text{s}$, $0{,}794$, $+26{,}0$ %, $0{,}817/0{,}794=1{,}029$; Z5 $u=0{,}06733$ m/s; Z6 $h=1{,}614$ m, $890$ s | isto |
| Pog. 8 | $\Delta p=523{,}6$ Pa; sifon $8{,}40$ m/s, $-5{,}8$ m; usisni vod $6{,}466$ m, $65{,}0$ kPa, $NPSH_a=6{,}65$ m, $z_{P,max}=8{,}24$ m; Venturi $Q=5{,}248$ L/s; Pitot $26{,}1$ m/s; Z2 $1853$ s; Z3 $+7{,}680$ kPa; Z4 $6{,}288$ m/s; Z5 $43{,}18\le d\le52{,}33$ mm; Z6 $Q\in[14{,}7;17{,}4]$ L/s, $p_C\in[59{,}1;70{,}8]$ kPa | isto |

Dimenzijska homogenost provjerena je u svim izvodima (izvod $y_B$, $BM$, $BM_{eq}$,
RTT, Eulerova jednadžba, energijska jednadžba s $\alpha$): bez nalaza.

## Što je u ovim poglavljima posebno dobro

- Dosljedna normala $\vec n_f$ „iz fluida prema stijenci” i pravilo da smjer
  $F_V$ određuje strana koju fluid kvasi, a ne nacrtani $V^*$. Primjer s plinskim
  nadtlakom (pog. 5, P5) pokazuje zašto $h_{CP}=h_C+I_G/(Ah_C)$ ne vrijedi kad se
  jednoliki tlak ne poništava. Provjera momenta oko središta luka u P4 i P5
  pravi je neovisni test.
- Pog. 6 izričito razdvaja geometrijski pomak $y_B$ od poluge stabiliteta i ne
  dopušta $\Delta y_B=m_ke$ bez $KG$. Dvofluidni $BM_{eq}=\rho_vI_T/\Delta$ izveden
  je čisto i potvrđen identitetom $BM_{eq}\tan\varphi=y_B$. Navođenje kriterija IS
  Code 2008 je točno i ograđeno.
- Pog. 7: izvod RTT-a s pomičnom plohom i primjer zahvatnog usisa broda u
  plovidbi dobro pokazuju zašto u tok mase ulazi relativna brzina. Brojka
  „šest puta prevelik protok pogrešnog smjera” pamtljiva je i točna.
- Pog. 8: energijska jednadžba izvedena je iz RTT-a s definicijom $h_g\ge0$ i
  $\alpha$. Primjer usisnog voda rashladne crpke s $NPSH_a$ i promjenom gaza u
  balastu primjena je iz obje struke s vjerodostojnim brojevima. Pitotov
  primjer ispravno upozorava da granice $Re$ za cijev ne vrijede za sondu.
- Zadatci pog. 5 Z3 (samootvarajuća zaklopka) i pog. 8 Z3 (tlak raste u
  silaznom suženju) traže stvarnu odluku i ruše tipične pogrešne intuicije.
- CFD odlomci ne iznose neprovedene rezultate i razlikuju fizikalni model,
  numeričku pogrešku i provjeru.

## Ograničenja ove recenzije

- Ovo je autorska procjena agentskog čitatelja, a ne potvrda didaktičke
  kvalitete; ne zamjenjuje imenovane recenzente ni studentski pilot.
- Skice sam pregledao na odabranim stranicama (104–107, 127–128, 140, 149, 161,
  166–167), ne sve slike u punoj rezoluciji.
- U dostavljenom `G2_kljuc.pdf` stranice 340, 342 i 343 pojavljuju se dvaput.
  To je vjerojatno posljedica izrezivanja materijala za recenziju, a ne
  knjige; nisam provjerio puni dodatak F.
- Bilježnice sam pročitao kao izvor, bez pokretanja.
