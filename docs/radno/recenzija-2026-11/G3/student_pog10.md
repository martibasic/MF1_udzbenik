# Simulirano čitanje

Poglavlje 10, Količina i moment količine gibanja (knjiga str. 183–206).
Ovo je simulirano čitanje, a ne studentski pilot sa stvarnim studentima.
Čitatelj je simulirani student druge godine (strojarstvo ili brodogradnja).
Poglavlja 1–9 obrađena su na predavanjima. Pročitan je samo PDF poglavlja.
Ključ rezultata otvoren je tek nakon što su model i rezultat za Z3 i Z6
zapisani u ovu datoteku.

## Zadatci za vježbu (zapisano prije otvaranja ključa)

### Z3. Koljeno u okomitoj ravnini s težinom vode (str. 202)

**Model prije računa.**

- Kontrolni volumen: nepomičan, obuhvaća vodu u koljenu od presjeka 1
  (vodoravni ulaz, +x) do presjeka 2 (izlaz prema gore, +z).
- Zakoni: kontinuitet (stalan promjer, pa v1 = v2), energijska jednadžba
  s gubitkom h_g = ξv²/(2g) za p_M2 i zakon količine gibanja (10.6) po x i z.
- Referenca tlaka: manometarski tlak, jer je vani atmosferski tlak.
- Pozitivni smjerovi: +x udesno, +z prema gore. Najprije tražim R_st→f,
  a zatim F = −R_st→f. Reakcija nosača je R = −F, jer se težina koljena
  ne računa.
- Pretpostavke: stacionaran tok, jednoliki profili (β = 1), g = 9,81 m/s².
  Zadatak ne zadaje g, pa sam ga pretpostavio.
- Granica modela: gubitak je zadan jednim koeficijentom, a raspodjela tlaka
  po stijenci nije poznata. Jednoliki profil neposredno iza kratkog koljena
  nije realan.
- Predviđanje: F_x > 0, jer fluid gura koljeno prema van od ulaza. F_z < 0,
  jer ga gura prema dolje. Iznos je reda p_M·A·√2 ≈ 6,7 kN, plus nešto zbog
  toka količine gibanja. Težina od približno 0,3 kN mali je dio toga.

**Račun.**

- A = π·0,2²/4 = 3,142·10⁻² m², v = Q/A = 2,865 m/s, ṁ = 89,82 kg/s,
  ṁv = 257,3 N.
- p_M2 = p_M1 − ρgΔz − ξρv²/2 = 150 000 − 3916 − 1229 = 144 855 Pa
  ≈ **144,9 kPa**.
- Težina vode: W = ρgV = 293,7 N.
- Za os x vrijedi p_M1A + R_x = ṁ(0 − v). Odatle je R_x = −257,3 − 4712,4
  = −4970 N, pa je **F_x = +4,97 kN**.
- Za os z vrijedi −p_M2A − W + R_z = ṁ(v − 0). Odatle je
  R_z = 257,3 + 4550,8 + 293,7 = 5102 N, pa je **F_z = −5,10 kN**.
- Rezultanta je **F ≈ 7,12 kN**. Reakcija nosača R = −F ima komponente
  (−4,97 kN; +5,10 kN), dakle ulijevo i prema gore, a iznos joj je 7,12 kN.
- Udio težine u okomitoj komponenti je 293,7/5102 ≈ **5,8 %**.
- Pogrešan „vodoravni” račun (p_M2 = p_M1, bez težine) daje
  F_z' = −(ṁv + p_M1A) = −4970 N. Okomita komponenta tako je po iznosu
  manja za **≈ 132 N (2,6 %)**. Težina (+294 N) i pad tlaka
  ((p_M1 − p_M2)A ≈ 162 N) djelomično se poništavaju.

### Z6. Sile na Y-račvu (str. 203)

**Model prije računa.**

- Kontrolni volumen: nepomičan, obuhvaća vodu u račvi od presjeka 1
  do izlaza 2 i 3.
- Zakoni: kontinuitet uz zadani udio s (Q2 = sQ1, Q3 = (1 − s)Q1) i zakon
  količine gibanja u ravnini xy. Bernoullijevu jednadžbu ne rabim, jer
  zadatak izričito kaže da tok nije bez gubitaka i da brzine nisu jednake.
- Referenca tlaka: manometarski tlak. Na izlazima je p_M = 0.
- Pozitivni smjerovi su +x i +y. Izlaz 3 ima smjer (cos 60°; sin 60°).
- Pretpostavke: stacionaran tok i jednoliki profili. Težina je okomita
  na ravninu, pa se ne računa.
- Granica modela: zadani udio s nije posljedica nikakve jednadžbe toka.
  Kut i promjer grane u stvarnosti bi utjecali na raspodjelu protoka.
- Predviđanje: dominira ulazna tlačna sila p_M1A1 ≈ 2,85 kN prema +x.
  Članovi ṁv iznose oko 100 N, pa će F biti malo ispod ili iznad 2,85 kN.
  F_y je mala i negativna.

**Račun (nominalno).**

- A1 = 1,539·10⁻² m², A2 = 6,362·10⁻³ m², A3 = 5,027·10⁻³ m².
- Protoci su Q2 = 0,024 m³/s i Q3 = 0,016 m³/s. Brzine su v1 = 2,598 m/s,
  v2 = 3,773 m/s i v3 = 3,183 m/s.
- Za os x vrijedi p_M1A1 + R_x = ṁ2v2 + ṁ3v3 cos 60° − ṁ1v1. Odatle je
  R_x = 90,4 + 25,4 − 103,7 − 2847,9 = −2836 N, pa je **F_x = +2,84 kN**.
- Za os y vrijedi R_y = ṁ3v3 sin 60° = 44,0 N, pa je **F_y = −44 N**.
- Rezultanta je **F ≈ 2,84 kN (2836 N)**. Reakcija nosača
  R = (−2836; +44) N.

**Najveća rezultanta u zadanom području.**

- F_x = p_M1A1 + ρQ1²·f(s), uz
  f(s) = 1/A1 − s²/A2 − (1 − s)²/(2A3) < 0 u cijelom području.
- f raste kad s pada, pa se najveći F_x dobiva uz najveći p_M1, najmanji Q1
  i najmanji s. F_y mijenja rezultantu tek za desetinku njutna.
- Kutove sam provjerio računom, a gustom mrežom potvrdio da maksimum leži
  u kutu p_M1 = 190 kPa, Q1 = 0,0392 m³/s, s = 0,57.
- Tamo je F_x = 2918 N i F_y = −49 N, pa je **F_max ≈ 2,92 kN**.
- Kriterij: 1,15·F_max = 3,36 kN > 3,0 kN, pa treba izabrati **3,5 kN**.
  Već nominalno 1,15·2,84 = 3,26 kN premašuje 3,0 kN.

## Usporedba s ključem (nakon otvaranja `kljuc10.pdf`)

| Zadatak | Moj rezultat | Kontrolni rezultat | Podudaranje |
|---|---|---|---|
| Z3 | v = 2,865 m/s; p_M2 = 144,9 kPa; F_x = +4,97 kN; F_z = −5,10 kN; F = 7,12 kN; R ulijevo i gore; težina 5,8 %; promjena F_z u „vodoravnom” računu ≈ 132 N | v ≈ 2,865 m/s; p_M2 ≈ 144,9 kPa; F_x ≈ +4,97 kN; F_z ≈ −5,10 kN; F ≈ 7,12 kN; R ulijevo i gore; težina 294 N ≈ 5,8 % | **da** (za dio 3b ključ nema broja) |
| Z6 | Q2; Q3 = 24; 16 L/s; F = (2835,8; −44,0) N; 2836 N; F_max = 2918 N pri 190 kPa, 39,2 L/s, s = 0,57; 1,15F_max = 3,36 kN, pa 3,5 kN | isto: 2836,2 N; maksimum 2918,3 N u istom kutu; 3356,1 N, pa 3,5 kN | **da** |

**Gdje sam zapeo.**

- **Z3.** Najviše vremena otišlo je na predznake u bilanci po z. Na izlazu
  tlačna sila djeluje prema dolje, u KV, a težina također prema dolje.
  Zatim treba dvaput promijeniti predznak (R_st→f, pa F). Da nisam riješio
  P3 (str. 192–193), lako bih izostavio jedan od tih koraka.
  - U dijelu 3 iznenadilo me da je razlika samo ≈ 132 N. Težina i pad
    tlaka djeluju suprotno, pa se djelomično poništavaju. Ključ to ne
    potvrđuje: daje udio težine, ali ne i traženu promjenu F_z, pa za drugi
    dio pitanja 3 nemam kontrolni broj.
  - Vrijednost g nije zadana. Uzeo sam 9,81 m/s² i to se poklapa s ključem.
- **Z6.** Fizika je jednostavna, jer je sila gotovo samo p_M1A1. Zapeo sam
  na tome kako se traži „najveća rezultanta u cijelom zadanom području”.
  - Poglavlje nigdje ne pokazuje kako se pretražuju granice parametara
    (monotonost, kutovi), pa sam to izveo sam iz izraza F_x(p, Q, s).
  - Rečenicu „To nisu standardne nesigurnosti za RSS” nisam razumio, jer
    kraticu RSS nisam sreo u poglavlju. Zaključio sam samo da ne smijem
    kombinirati odstupanja korijenom zbroja kvadrata.
  - Smjernica u ključu („prije nego što upotrijebiš samo rubne kombinacije,
    provjeri kako se rezultanta mijenja”) pomogla bi bez otkrivanja
    rješenja. Razumljiva je i bez poglavlja.
- **Ključ.** Odjeljak ključa za ovo poglavlje nosi oznaku **F.11**, a
  poglavlje je 10 (sljedeći, F.12, jest pog. 11). Prvo sam tražio „F.10”.
  Smjernice za Z3 i Z6 razumljive su bez poglavlja. U smjernici Z3
  jednadžba je zapisana s visinama (p/(ρg), Δz, h_g), a ne s tlakovima,
  ali to je lako povezati.

## Čitanje teorije (str. 183–188)

Mjesta na kojima sam zastao:

- **Str. 183.** Odmah se rabi F_p,i = −p_M,i A_i n_i s manometarskim tlakom.
  Zašto se smije izostaviti atmosferski tlak, objašnjeno je tek na str. 186
  (granica modela, „manometarski tlak”). Pri prvom čitanju pitao sam se
  što je s atmosferskim tlakom na vanjskoj stijenci.
- **Str. 185, okvir o β.** Rečenice „α ≥ β^{3/2} … Pri povratnom toku ili
  drukčije definiranim presjecima te se nejednakosti ne smiju primijeniti”
  morao sam čitati dvaput. Nije mi jasno je li to za kolokvij potrebno
  ili samo usput.
- **Str. 187, mlazni pogon.** Uz „ukupna kinetička snaga predana vodi
  iznosi ṁ(v_j² − v_s²)/2” nije rečeno u kojem je sustavu ta snaga.
  - U sustavu obale voda miruje i izlazi brzinom v_j − v_s, pa sam prvo
    napisao ṁ(v_j − v_s)²/2 i dobio drugu učinkovitost.
  - Tek kad sam sam zbrojio F_Tv_s + ṁ(v_j − v_s)²/2, vidio sam da je to isto.
  - Z1 pita „koliki dio ostaje u mlazu”, pa bi ta jedna rečenica pomogla.
- **Str. 187, aktuatorski disk.** „Bernoullijeva jednadžba vrijedi odvojeno
  ispred i iza diska, pa je Δp = ρ(v_j² − v_A²)/2” preskače dva retka.
  Rekonstruirao sam ih (p0 + ρv_A²/2 = p_ispred + ρv_d²/2 i
  p_iza + ρv_d²/2 = p0 + ρv_j²/2), ali sam za to trebao par minuta.
- **Str. 188, rotor.** M_z = ṁ(r2v_t2 − r1v_t1) moment je stijenke na fluid.
  Odmah zatim stoji da „pomnožen kutnom brzinom daje snagu”, ali ne piše
  je li to snaga predana fluidu ili dobivena od njega. Predznak sam shvatio
  tek iz P7.

**Zastani i promisli (str. 186).** Prije čitanja odgovora rekao sam: „Ne,
CFD daje silu na drugo tijelo, pa je suprotan predznak očekivan.” Odgovor
se poklopio. Pitanje provjerava razumijevanje (koje tijelo), a ne pamćenje.
Odgovor je odmah ispod pitanja, pa ga je teško ne pročitati prije
razmišljanja.

**Pitanja uz numerički pokus (str. 186).** Pitanja (b) i (c) mogao sam
odgovoriti iz teorije:

- (b) faktor 1 − cos θ najveći je pri 180°;
- (c) ṁv prevladava kad je ρv² veći od p_M.

Za (a) bez bilježnice nisam siguran koje vrijednosti autorica očekuje.

## Riješeni primjeri (prvi pokušaj prije čitanja rješenja)

| Primjer | Moj model i prvi korak | Poklapanje | Napomena |
|---|---|---|---|
| P1 Peltonova lopatica (str. 189–190) | KV prati lopaticu, w = v − u, ṁ_rel = ρAw | da (1–3) | Za dio 4 ne bih sam znao da kolo prima ρAv, a ne ρAw. Rješenje to objašnjava, ali teorija na str. 187 to ne najavljuje. |
| P2 Kalibracijska mlaznica (str. 190–192) | v2 iz F_P = ρA2v2², pa Bernoulli, pa KV mlaznice | da | Dobro je što je odvojen KV mlaza od KV mlaznice. |
| P3 Servisno koljeno (str. 192–193) | x i y bilanca s p_M1A1 i p_M2A2 u KV | da | Provjera s β i gubitkom korisna je. |
| P4 T-račva (str. 193–195) | Bernoulli 1→2 i 1→3, v2 = v3, kontinuitet | da | Zastao sam smije li se Bernoulli pisati kroz račvanje. Rješenje to samo primijeni. |
| P5 Y-račva s mjerenom reakcijom (str. 195–198) | Iz R_y dobiti v3 | da, nakon razmišljanja | Trebalo mi je vremena da povežem R_y (konzola na račvu) s R_st→f,y. Rečenica na str. 196 to razjašnjava. |
| P6 Koljeno 60° (str. 198–199) | Komponente po x i y izravno | isti rezultat, drugi put | Rješenje rabi jedinične vektore i impulsnu funkciju. Elegantno je, a provjera 2I sin(θ/2) jako mi se svidjela. |
| P7 Rotirajuća mlaznica (str. 199–201) | Pol na osi, v_t = w − u | da | „Snaga mlazova ṁ(w² − u²)/2 ≈ 440 W” (str. 201) nije izvedena. Tek sam računom provjerio da je to 71 W + ṁ(w − u)²/2. |

## Tri mjesta na kojima bi student najvjerojatnije pogriješio ili odustao

1. **Predznaci tlaka na izlazu i težine u okomitoj bilanci (P3, Z3,
   str. 192, 202).**
   - Tri oznake (R_st→f, F, R) za iste komponente traže dvije promjene
     predznaka.
   - U Z3 se uz to izlazni tlak mora prvo dobiti energijskom jednadžbom
     s Δz i gubitkom.
   - Student će lako napisati +p_M2A2 ili zaboraviti težinu.
2. **Maseni protok kroz pomičnu granicu (P1 dio 4, Z5, str. 187 i 190).**
   Razlika ρAw (jedna lopatica) i ρAv (kolo) uvodi se tek u rješenju P1.
   Student koji ne pročita pažljivo P1 u Z5 uzet će ρAv.
3. **Traženje maksimuma po granicama parametara (Z6, str. 203).**
   Poglavlje ne pokazuje postupak. Uz nepoznat izraz „RSS” student će
   vjerojatno izračunati samo nominalno stanje ili sve kombinacije
   naslijepo.
   - Ovdje nominalno stanje slučajno već daje isti izbor nosivosti
     (3,26 kN > 3,0 kN), pa pogreška neće biti vidljiva.

## Nejasnoće po težini

**P1** (ne mogu nastaviti ili ću naučiti nešto pogrešno): nisam našao
nijednu.

**P2** (usporava ili zbunjuje):

- **Str. 187, mlazni pogon.** Nije rečeno u kojem je sustavu kinetička
  snaga ṁ(v_j² − v_s²)/2. U sustavu obale student dobiva ṁ(v_j − v_s)²/2
  i drugu učinkovitost. Ključ Z1 potvrđuje izraz iz knjige.
- **Z6 (str. 203).** Kratica „RSS” nije objašnjena. Formulacija
  „sintetički pogonski scenarij” i „zajamčene granice” zbunjuje.
  Postupak traženja maksimuma po granicama nije pokazan u poglavlju.
- **Z3, ključ.** Za drugi dio pitanja 3 (promjena F_z) nema kontrolnog
  rezultata.

**P3** (sitnica):

- **Str. 183.** Manometarski tlak u F_p,i rabi se prije nego što je na
  str. 186 objašnjeno zašto smije.
- **Str. 187.** Dva koraka do Δp = ρ(v_j² − v_A²)/2 nisu ispisana.
- **Str. 188.** Nije rečeno je li ωM_z snaga predana fluidu ili dobivena
  od fluida.
- **Str. 201, P7.** Izraz ṁ(w² − u²)/2 za snagu mlazova nije objašnjen.
- **Sl. 10.2 (str. 189).** Uz donju strelicu desno vidim samo indeks „x”
  i „(fluid → lopatica)”. Čini mi se da nedostaje slovo F.
- **Sl. 10.4 (str. 192) i panel Z3 na sl. 10.9 (str. 204).** Na izlazu 2
  su dvije suprotne strelice blizu jedna drugoj, a oznaka v2 stoji uz onu
  koja pokazuje prema dolje, iako tok ide prema gore.
  - Pri razlučivosti kojom sam čitao nisam siguran koja je strelica brzina,
    a koja tlačna sila.
  - Za Z3 napomena na str. 204 kaže da izlazni tlak nije nacrtan, pa ne
    znam što je druga strelica.
- **Sl. 10.7 (str. 198).** Nad skicom stoji osamljena oznaka „y”, odvojena
  od koordinatnog križa desno.
- **Z3.** Vrijednost g nije zadana (pretpostavio sam 9,81 m/s²).
- **Ključ.** Poglavlje 10 ima oznaku F.11.

## Procjena vremena

- teorija oko 2,5 h;
- sedam riješenih primjera s vlastitim pokušajem oko 3,5 h;
- šest zadataka za vježbu oko 4 h.

Ukupno je to oko 10 h, što se slaže s procjenom na str. 184.

## Što mi je najviše pomoglo

- Dosljedna oznaka R_st→f i rečenica „To je sila stijenke na fluid. Zato
  fluid na … djeluje silom …” nakon svake bilance (P3–P5).
- Izdvojeni dijagram „Fluid → koljeno” uz skice s predznacima F_x i F_y.
- Provjere na kraju primjera: energijska provjera u P1, 2I sin(θ/2) u P6
  i utjecaj β u P3.
- Popis četiriju pretpostavki u okviru „Granica modela” (str. 186–187).

## Ograničenja ovog čitanja

Ovo je simulirano čitanje jednog čitatelja. Ono ne dokazuje da je
poglavlje didaktički uspješno. Primjedbe o skicama odnose se na
razlučivost kojom je PDF pregledan i treba ih provjeriti u punoj
razlučivosti. Zadatci Z1, Z2, Z4 i Z5 nisu rješavani, pa je ključ
za njih samo pročitan.
