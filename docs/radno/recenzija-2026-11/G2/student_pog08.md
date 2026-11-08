# Simulirano čitanje

Poglavlje 8 (Energijska jednadžba i Bernoulli), PDF str. 150–168, ključ F.9.
Uloga: student druge godine strojarstva/brodogradnje; poglavlja 1–7 obrađena
na predavanjima. Ovo je simulirano čitanje, ne studentski pilot.
Zadatci riješeni bez naputka: Z3 i Z6. Model i rezultat zapisani su prije
otvaranja ključa.

## Procjena vremena

Oko 7 sati: teorija i izvodi oko 2 h, P1–P6 oko 2 h, Z1–Z6 oko 3 h (Z5 i Z6
po oko 45 min). Navedenih 10 sati (str. 151) realno je za studenta koji
rješava sve zadatke i otvara bilježnice.

## Tri mjesta na kojima bi student najvjerojatnije pogriješio ili odustao

1. **„Tlak pada u suženju” kao pravilo (str. 150, 152, 168 → Z3).** Prva
   rečenica poglavlja kaže da u suženju tlak na stijenci pada. Okvir na str. 152
   i sažetak kažu da „HGL pada ondje gdje se fluid ubrzava”. Ako student ne riješi
   Z3, naučit će da u suženju uvijek pada tlak, a ne HGL. Tek ključ za Z3
   izričito kaže „tlak i HGL nisu ista veličina”. Z3 dobro ispravlja tu zabludu,
   ali u teoriji nema ni rečenice koja na nju upozorava.
2. **Predznaci u izvodu energijske jednadžbe (str. 154–155).** $\dot W$ je rad
   koji sustav obavlja na okolini, a $H_p$ i $H_t$ u (8.18) definirani su kao
   pozitivni iznosi $\dot W_{crpka}$ i $\dot W_{turbina}$. Nisam mogao sam
   povezati kako $\dot W_s$ iz (8.16) postaje $H_p$ na lijevoj, a $H_t$ na desnoj
   strani (8.19). Isto vrijedi za predznak $\dot Q$ u $h_g$. Taj sam dio čitao
   dvaput i na kraju jednadžbu (8.19) samo prepisao. Na kolokviju bih mogao
   staviti $H_p$ na pogrešnu stranu.
3. **Manometarski i apsolutni tlak te HGL u sifonu (P3, str. 160).** U retku
   ispred (8.35) piše „$0 = p_{M,C}/(\rho g) + 3{,}6 + 2{,}2$”. Nisam odmah vidio
   da je 3,6 zapravo $v^2/(2g)=\Delta z$ iz (8.31). Odmah potom dolaze tri
   različita broja za istu točku: −5,8 m (tlačna visina), −3,6 m (HGL) i 4,4 m
   (apsolutna tlačna visina). Objašnjenje postoji, ali tu bih najlakše zamijenio
   HGL i tlačnu visinu.

## Riješeni primjeri (model prije čitanja rješenja)

| Primjer | Moj model i prvi korak | Poklapa se | Napomena |
|---|---|---|---|
| P1 (str. 156) | $Q=\dot m/\rho$, kontinuitet, Bernoulli uz $z_1=z_2$ | da | — |
| P2 (str. 157) | Torricelli, zatim vodoravni hitac | da | Za dio 2 očekivao sam derivaciju $h(H-h)$. Rješenje kaže „vidimo” iz tri točke (8.29), a tri točke ne dokazuju maksimum. Argument s umnoškom dolazi tek u provjeri. |
| P3 (str. 159) | A–B za brzinu, A–C za tlak u vrhu | da | Zastoj kod 3,6 u (8.35), vidi gore. |
| P4 (str. 160–162) | A na površini mora, P na ulazu, (8.19) s $h_g$ | da | Pomislio sam staviti presjek A na otvor koša ($z_u=-3$ m) s hidrostatičkim tlakom. Rješenje (str. 161 i provjera na str. 162) jasno objašnjava zašto to ne valja. Slika 8.5 je pretrpana: „P crpka”, „u rashladni sustav” i „platforma strojarnice” preklapaju se, kao i „vodna linija u balastu” s „$p_A=p_{atm}$”. |
| P5 (str. 162–163) | Manometar (pog. 2), kontinuitet, Bernoulli | da | — |
| P6 (str. 164) | Bernoulli do zaustavne točke | da | Za dio 3 (Re sonde) ne bih znao što zaključiti. Granice 2300/4000 spominju se kao poznate, a u pog. 1–8 ih nisam susreo. |

## Zadatci za vježbu

### Z3. Tlak u silaznom suženju (T1, str. 165)

**Model prije računa.** Strujna cijev od presjeka 1 do 2, jednoliki profili.
Zakoni: kontinuitet i Bernoulli (8.2). Os $z$ je prema gore. Referenca tlaka nije
bitna jer se traži razlika. Pretpostavke: stacionarno, nestlačivo, bez gubitaka.
Granica modela: realno suženje ima malen gubitak, pa je stvarni porast tlaka
nešto manji. Predviđanje: spuštanje od 2 m veće je od porasta brzinske visine
(procjena oko 1,2 m), pa očekujem $p_2-p_1>0$.

**Moj rezultat.** $v_1=1{,}768$ m/s, $v_2=5{,}197$ m/s,
$p_2-p_1=\rho g\Delta z+\tfrac{\rho}{2}(v_1^2-v_2^2)=19{,}62-11{,}94=+7{,}68$ kPa.
Tvrdnja nije općenito točna. Za vodoravno suženje istih promjera tlak bi pao
za 11,94 kPa.

**Kontrolni rezultat.** $v_1\approx1{,}768$ m/s, $v_2\approx5{,}197$ m/s,
$p_2-p_1\approx+7{,}680$ kPa; tvrdnja nije općenito točna.
**Podudaranje: da.**

**Gdje sam zapeo.** Nigdje računski. Na skici Z3 (str. 167) strelica
„Δz = 2,00 m” izgleda kao da ide od gornje stijenke cijevi 1 do gornje stijenke
cijevi 2, a ne između osi. Tekst kaže da je to razmak osi, pa sam se držao teksta.
Smjernica u ključu razumljiva je bez poglavlja i ne otkriva rezultat. Rečenica
„tlak i HGL nisu ista veličina” najkorisnija mi je u cijelom ključu.

### Z6. Sifon i putanja izlaznog mlaza (T4, str. 166)

**Model prije računa.** Strujnica od mirne površine A do izlaza B i do vrha C.
Mirna površina smije se spojiti s bilo kojim presjekom (str. 155). Zakoni: u
dijelu 1 Bernoulli, u dijelu 2 energijska jednadžba (8.19) s
$h_g=\zeta v^2/(2g)$, a za domet vodoravni hitac s 1,2 m. Referenca tlaka je
apsolutna jer je zahtjev zadan apsolutnim tlakom. Pozitivni smjer $z$ je prema
gore, a $z=0$ na slobodnoj površini. Pretpostavke: kvazistacionarno, nestlačivo,
jednolik profil ($\alpha=1$), mlaz bez otpora zraka. Granica modela: tlak u C
srednji je tlak u presjeku, a lokalni minimum u koljenu je niži. Predviđanje:
idealno $v\sim7$ m/s i $Q\sim27$ L/s. Gubitci s $1+\zeta_\Sigma\approx3$ smanjuju
$v$ za faktor $\sqrt3$, pa očekujem $Q\approx16$ L/s, blizu zahtjeva od 15 L/s.

**Moj rezultat.**
- Idealno: $v=7{,}14$ m/s, $Q=27{,}5$ L/s, $p_{aps,C}=59{,}1$ kPa, $x=3{,}53$ m.
- S gubitcima, nominalno ($\zeta_\Sigma=2{,}0$, $\zeta_C=1{,}2$): $Q=15{,}9$ L/s,
  $p_{aps,C}=65{,}9$ kPa.
- Granice: $Q\in[14{,}7;\,17{,}4]$ L/s (krajevi $\zeta_\Sigma=2{,}5$ i $1{,}5$).
  $p_{aps,C}\in[59{,}1;\,70{,}8]$ kPa: najniži tlak daje $\zeta_C=1{,}5$ uz
  $\zeta_\Sigma=1{,}5$, a najviši $\zeta_C=0{,}9$ uz $\zeta_\Sigma=2{,}5$.
- Zaključak: tlak je zajamčen ($59{,}1>30$ kPa), protok nije
  ($14{,}7<15{,}0$ L/s). Oba zahtjeva ne mogu se zajamčiti.

**Kontrolni rezultat.** Idealno: 7,14 m/s; 27,5 L/s; 59,1 kPa; 3,53 m.
Nominalno 15,9 L/s i 65,9 kPa. Intervali [14,7; 17,4] L/s i [59,1; 70,8] kPa.
Tlak prolazi, protok nije zajamčen. **Podudaranje: da.**

**Gdje sam zapeo.**
- Najviše vremena otišlo je na odluku o najgorem tlaku u C. Dva koeficijenta
  djeluju suprotno: veći $\zeta_\Sigma$ smanjuje $v$ i podiže tlak, a veći
  $\zeta_C$ ga spušta. Morao sam proći sve rubne kombinacije. Tu je zadatak
  doista T4.
- Najniži tlak s gubitcima ispao je točno jednak idealnom (59,1 kPa). Zastao sam
  jer ta kombinacija ($\zeta_C=\zeta_\Sigma=1{,}5$) znači da od vrha do izlaza
  nema nikakvog gubitka. Tekst kaže da su „dopuštene sve kombinacije”, a ključ to
  ne komentira. Nisam siguran je li ta krajnja kombinacija fizikalno smislena.
- Tekst zadatka već daje obje gotove bilance s $\zeta$. Model s gubitcima zato
  nisam morao sam postaviti iz (8.19), nego sam samo uvrštavao. Smjernica u
  ključu ponavlja iste formule; razumljiva je i ne upućuje na ništa izvan
  poglavlja.

## Zastani i promisli (str. 152)

Moj odgovor prije čitanja: ne, dio pada statičkog tlaka pretvara se u
kinetičku energiju i vraća u difuzoru. Poklapa se s odgovorom. Pitanje provjerava
razumijevanje, jer treba razlikovati statički tlak od ukupne energije, a ne samo
ponoviti formulu.

Interaktivni „Predvidi” (str. 151): odgovorio sam da se protok udvostručuje
($Q\propto\sqrt{\Delta p}$). To znam od ranije. Iz teksta do te stranice to se
ne može izvesti jer Venturijeva cijev dolazi tek u P5.

## Nejasnoće po težini

**P1**
- Nema.

**P2**
- Str. 150, 152, 168: „tlak pada u suženju” i „HGL pada gdje se fluid ubrzava”
  mogu se naučiti kao pravilo za tlak. Upozorenje dolazi tek u ključu za Z3
  (mjesto 1 gore).
- Str. 154–155: put predznaka od $\dot W$ i $\dot W_s$ do $H_p$ i $H_t$ u (8.19)
  nije pokazan. Isto vrijedi za $\dot Q$ u $h_g$ (mjesto 2 gore).
- Str. 154, naslov 8.2 „Kada se trenje može zanemariti”: odjeljak ima dvije
  rečenice i ne daje kriterij. Na str. 155 piše da pretpostavke moraju biti
  „dovoljno dobro opravdane”, ali ne piše kako to procijeniti. U zadatcima se
  oslanjam samo na riječi „glatko” i „zanemari gubitke”.
- Str. 151–152: interaktivni prikaz Venturija (s „uljnim primjerom iz knjige”) i
  okvir CFD dolaze prije nego što su uvedeni Venturijev mjerač, Pitotova sonda,
  ukupni tlak $p_t$ i difuzor. Pomislio sam da sam nešto preskočio.

**P3**
- Str. 160, (8.35): broj 3,6 pojavljuje se bez oznake da je to $v^2/(2g)$.
- Str. 158, P2: maksimum dometa zaključen je iz tri točke umjesto iz derivacije.
- Str. 156 i 163: „odjeljak D.7” nije u ovom poglavlju, pa ga nisam mogao
  otvoriti.
- Str. 164, P6: granice Re 2300/4000 spominju se kao poznate, a u poglavljima
  1–8 nisu uvedene.
- Str. 161, slika 8.5: oznake se preklapaju.
- Str. 167, skica Z3: strelica Δz ne vidi se jasno kao razmak osi.
- Z6: najgora kombinacija $\zeta_C=\zeta_\Sigma$ znači da od vrha do izlaza nema
  gubitka; ni zadatak ni ključ to ne komentiraju.
- Ključ: poglavlje 8 u dodatku je „F.9”, a ne F.8. Stranica ključa počinje sa
  „Z6” iz prethodnog poglavlja (balastni tank), pa sam na trenutak mislio da je
  to Z6 iz ovog poglavlja.

## Što mi je najviše pomoglo

- Slika 8.1 (energijski stupci uz suženje i uzlazni dovod): prvi put sam vidio
  da je suma uvijek ista, a mijenja se samo raspodjela.
- Napomena na str. 155 da sve strujnice iz mirnog spremnika nose istu ukupnu
  visinu. Uz objašnjenje u P4 zašto se presjek ne stavlja na otvor koša, to mi je
  razjasnilo izbor referentnih točaka.
- „Provjera i tumačenje” u P3 i P4: povratna bilanca u metrima odmah pokaže
  grešku.
- Z3 kao kratak zadatak koji ruši naučeno pravilo, a Z6 kao jedini zadatak u
  kojem sam stvarno morao odlučivati o najgorem slučaju.
