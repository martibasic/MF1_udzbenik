# Simulirano čitanje

**Poglavlje 3. Hidrostatička raspodjela tlaka i manometrija** (knjiga str. 50–69)

Ovo je simulirano čitanje: agent igra studenta druge godine i ne zamjenjuje pilot sa
stvarnim studentima. Predznanje: poglavlja 1–2 su obrađena na predavanjima.
Čitan je samo PDF poglavlja. Ključ (dodatak F.4) otvoren je tek nakon što su model i
rezultat Z3 i Z6 bili zapisani u ovoj datoteci.

## Procjena vremena

Teorija s izvodima oko 2 h, riješeni primjeri P1–P6 oko 3 h (P3 sam oko 1 h), Z3 i Z6
oko 1,5 h, ostali zadatci još 2–3 h. Ukupno 8–10 h, što odgovara navedenih 9 sati.

## Tri mjesta na kojima bi student najvjerojatnije odustao ili pogriješio

1. **P3, str. 58–60 (sondiranje teretnog tanka).** U jednom primjeru ima pet razina i
   dvije reference: ulaž se mjeri prema dolje od referentne točke na palubi, sondiranje
   prema gore od dna. K tome dolaze pretlak plina, talog i dvije pogrešne varijante.
   Student lako izgubi trag koja se visina odnosi na koju referencu. U P5 (str. 63)
   „ulaz” se potom mjeri od vrha tanka, a ne od palube. Morao sam se vratiti na sliku 3.4
   da provjerim da $U + h_u + h_v = H_{ref}$.
2. **Z3, str. 65 (nagnuti manometar).** Teorija nigdje ne obrađuje nagnuti manometar ni
   spuštanje razine u posudi. Tipične pogreške su da student uzme $L$ umjesto $L\sin\alpha$
   ili zaboravi spuštanje razine. Za to treba sam doći do ideje o jednakosti istisnutih
   volumena. U 3. dijelu „okomiti U-manometar s istim uljem” može značiti razliku razina
   dvaju krakova ili pomak jednog kraka, a to mijenja omjer osjetljivosti za faktor 2
   (3,6 ili 7,3). Što se misli, otkriva tek ključ.
3. **Z6, str. 66 (tolerancije i izbor pretvornika).** Najnepovoljniju kombinaciju
   tolerancija pronašao sam bez teškoća. Zbunilo me što već nominalni tlak traži punu
   skalu $1{,}05 \cdot 135{,}28 = 142{,}0$ kPa > 140 kPa. Analiza tolerancija zato ne
   mijenja odluku, a ključ kaže da „nominalna vrijednost sama nije dovoljna za izbor
   senzora”. Mislio sam da sam negdje pogriješio jer nisam vidio čemu služi drugi dio
   zadatka. Slabiji student bi ondje mogao stati.

## Čitanje teorije: mjesta zastoja

- **str. 50, uvod.** Na prvoj stranici su gotovo svi rezultati poglavlja: $dp/dz$,
  $p_M$, $h_p$, U-manometar i diferencijalni manometar. Odlomak sam pročitao dvaput.
  Formula $p_1 - p_2 = (\rho_{Hg} - \rho)g\Delta h$ poslije se nigdje ne izvodi hodom po
  stupcima. Na nju upućuje tek „Numerički pokus” (str. 55).
- **str. 51–52, izvodi.** Izvodi su mi bili jasni. Slijed (3.1)–(3.4) i vektorski oblik
  (3.8)–(3.10) slijede bez skokova.
- **str. 53, izotermalna atmosfera.** Izvod je jasan. Provjerio sam 35 kPa na 8,8 km i
  slaže se. Okvir CFD „Spremnik prije uključivanja crpke” (vrtlog, uvlačenje zraka) nisam
  povezao s gradivom pa sam ga preskočio.
- **str. 54, rečenica „Najčešća je pogreška uzeti atmosferu kao nulu i kad za to nema
  fizikalnog opravdanja”.** Pročitao sam je dvaput. Nije rečeno kada opravdanja nema.
  Odgovor (zatvoreni spremnik, usporedba s tlakom pare) našao sam tek u sažetku (str. 69).
- **str. 54, okvir CFD „Balastni tank prije početka balastiranja”.** Rabi $\rho_{mv}$,
  $T$, $H_{tk}$, ploču $P$ i $p_{rgh}$, a ništa od toga u tom trenutku nije uvedeno.
  $T$ i $H_{tk}$ definira tek P5 na str. 61. Okvir nisam razumio dok nisam pročitao P5.
- **str. 55, „kavitacijski se kriterij”.** Kavitacija još nije objašnjena. Iz
  termodinamike znam za tlak zasićenja pa sam mogao nastaviti.

## Riješeni primjeri (model i prvi korak prije čitanja rješenja)

| Primjer | Moj model / prvi korak | Poklapa se | Napomena |
|---|---|---|---|
| P1 (str. 56) | $p_{pl} = p_{atm} + p_{M,pl}$, zatim silazak $\rho g h$ do $A$ | da | – |
| P2 (str. 57–58) | hod $p_1 + \rho_v g h_1 - \rho_{Hg} g h_2 - \rho_{zr} g h_3 + \rho_{mv} g h_4 = p_2$ | da | Izraz „neto uspon kroz zrak” razumio sam tek sa slike 3.3. Oznake $p_1$, $h_1$, $h_2$ i „0,40 m” prelaze preko crta cijevi. |
| P3 (str. 58–60) | $p_{M,dno} = p_{M,pl} + \rho_u g h_u + \rho_{mv} g h_v$ | da | Vidi mjesto zastoja 1. Brojke sam provjerio (15,940 m, 250 m³, 213 m³). |
| P4 (str. 60–61) | $p_M = -\rho_u g H$, zatim apsolutni tlak usporediti s $p_v$ | da | $NPSH_a$ i $NPSH_r$ (str. 61) nisu objašnjeni. Shvatio sam da je to za kasnije pa nisam zapeo. |
| P5 (str. 61–63) | vani $\rho g (T - z)$, unutra $\rho g (H_{tk} - z)$, neto = razlika | da | Na slici 3.6 dva puta piše $p_{atm}$, jedno ispod drugoga iznad odzračnika, pa nije jasno koji se odnosi na sondnu cijev. |
| P6 (str. 63–64) | $p_{M,B} = p_{M,A} - \rho_v g \Delta z$ | da | – |

Ni u jednom primjeru rješenje nije izabralo nešto što iz teksta zadatka nisam mogao znati.

## Zadatci za vježbu

### Z3. Nagnuti manometar na ventilacijskom kanalu (str. 65, slika str. 67)

**Prije računa:**
- *Sustav:* mirujuće ulje u posudi i cjevčici; zrak u kanalu iznad posude, atmosfera na
  otvorenom kraju.
- *Zakon:* hidrostatika između površine u posudi i meniska.
- *Referenca:* manometarski tlak (atmosfera = 0); $z$ prema gore.
- *Pretpostavke:* $\rho_{zr} \approx 0$; $d$ i $D$ stalni; kapilarni pomak isti kao pri
  nultoj oznaci; menisk se pomiče prema gore uz cjevčicu.
- *Granica modela:* kut mora biti točno poznat, a priključak na kanalu ne smije osjećati
  dinamički tlak strujanja.
- *Predviđanje:* red veličine $\rho g L \sin\alpha \approx 400$ Pa; točan tlak za oko
  $(d/D)^2/\sin\alpha \approx 6\,\%$ veći.

**Moj rezultat:**
1. $p_M \approx \rho_u g L \sin\alpha = 385{,}2$ Pa.
2. Spuštanje razine u posudi $\delta = L(d/D)^2 = 2{,}89$ mm. Točan pretlak je
   $p_M = \rho_u g L(\sin\alpha + (d/D)^2) = 408{,}4$ Pa. Pojednostavljenje daje
   $-5{,}7\,\%$.
3. Osjetljivost $1/[\rho_u g(\sin\alpha + (d/D)^2)] = 0{,}453$ mm/Pa, a za U-manometar
   (razlika razina) $1/(\rho_u g) = 0{,}124$ mm/Pa. Nagnuti je 3,64 puta osjetljiviji.
   Kut se ne smanjuje proizvoljno iz više razloga:
   - član $(d/D)^2$ postaje usporediv sa $\sin\alpha$;
   - menisk se razvlači i teže se čita;
   - cjevčica postaje preduga;
   - relativna pogreška zbog netočnog kuta raste približno kao $\cot\alpha \cdot \delta\alpha$.

**Kontrolni rezultat (ključ, str. 337):** 385 Pa; 408 Pa; pojednostavljenje podcjenjuje
tlak za 5,7 %; 0,45 mm/Pa, 3,6 puta više od U-manometra (0,124 mm/Pa).

**Podudaranje:** da.

**Gdje sam zapeo:**
- U 2. dijelu sam se kratko pitao je li $L$ pomak meniska u odnosu na nultu oznaku ili u
  odnosu na novu razinu u posudi. Napomena uz skice (str. 68), „nulta oznaka vrijedi za
  jednake tlakove”, riješila je dvojbu.
- U 3. dijelu tekst ne kaže što se kod U-manometra čita. Uzeo sam razliku razina, a ključ
  to potvrđuje.
- Za obrazloženje kuta ključ ne daje kriterij, pa ne znam je li moj odgovor potpun.

**Ključ bez poglavlja:** smjernica je razumljiva. Uvodi oznake $a$, $A$ i $\delta$ kojih
nema u tekstu zadatka, ali ih definira u istoj rečenici. $A$ je u poglavlju inače oznaka
točke.

### Z6. Tlak plina iz manometarskog mjerenja (str. 66, slika str. 68)

**Prije računa:**
- *Sustav:* voda u spremniku i spojnom vodu, živa u U-manometru, plin iznad vode.
- *Zakon:* hidrostatski hod kroz stupce; na istoj razini istog mirujućeg fluida tlak je
  isti.
- *Referenca:* apsolutni tlak; $z$ prema gore.
- *Pretpostavke:* zrak iznad žive u otvorenom kraku se zanemaruje. Granica voda–živa je
  na visini priključka, pa između $A$ i žive nema neto stupca vode. Petlja spojnog voda
  na slici diže se i spušta kroz istu vodu, pa se poništava.
- *Granica modela:* tolerancije su granični intervali; svaka kombinacija je moguća.
- *Predviđanje:* $p_A \approx p_{atm} + 28$ kPa; $p_{pl}$ manji od $p_A$ za oko 6 kPa;
  dublja točka oko 135 kPa, blizu granice od 140 kPa.

**Moj rezultat:**
1. $p_A = 100{,}9 + 13600 \cdot 9{,}81 \cdot 0{,}210 / 1000 = 128{,}92$ kPa.
   $p_{pl} = p_A - \rho_v g h_1 = 122{,}55$ kPa (aps.).
   $p_{dublja} = p_{pl} + \rho_v g h_2 = 135{,}28$ kPa (aps.).
2. Iz $p_{dublja} = p_{atm} + \rho_{Hg} g \Delta h + \rho_v g(h_2 - h_1)$ najnepovoljnija
   kombinacija je: $p_{atm}$ +0,4 kPa, $\Delta h$ +2 mm, $h_2$ +5 mm, $h_1$ −5 mm.
   Daje $p_{max} = 136{,}05$ kPa, pa puna skala mora biti barem $1{,}05 \cdot 136{,}05
   = 142{,}85$ kPa > 140 kPa. Bira se 0–160 kPa.

**Kontrolni rezultat (ključ, str. 338):** $p_{pl} \approx 122{,}6$ kPa;
$p \approx 135{,}3$ kPa; $p_{max} \approx 136{,}05$ kPa; 142,85 kPa; 0–160 kPa.

**Podudaranje:** da.

**Gdje sam zapeo:**
- Kod pitanja čemu služi analiza tolerancija: odluka je ista i s nominalnom vrijednošću
  (vidi mjesto zastoja 3).
- Tek u „Traži se 2” saznao sam da se pretvornik ugrađuje u dubljoj točki. Ta točka na
  slici nema oznaku, samo točkicu.

**Ključ bez poglavlja:** smjernica je razumljiva i redoslijed koraka odgovara mom.

## Zastani i promisli / Numerički pokus

- **Zastani i promisli (str. 56).** Prije čitanja odgovorio sam: ne moraju se
  razlikovati, ako je $p_{atm} + p_M > 0$. Odgovor se poklapa. Pitanje provjerava
  razumijevanje referenci, a ne pamćenje. Odgovor stoji odmah ispod pitanja pa ga je lako
  pročitati prije razmišljanja.
- **Numerički pokus „Predvidi” (str. 55).** Prije bilježnice odgovorio sam ovako:
  udvostručena $\Delta h$ udvostručuje $p_1 - p_2$. Kad su gustoće gotovo jednake, mala
  razlika tlaka daje veliku $\Delta h$, pa je instrument vrlo osjetljiv. Pitanje traži
  razumijevanje formule. Bilježnicu nisam otvarao.

## Nejasnoće po težini

**P1** – nema. Nisam našao mjesto na kojem ne bih mogao nastaviti ili bih naučio nešto
pogrešno.

**P2**
1. str. 54, okvir CFD o balastnom tanku: $T$, $H_{tk}$, ploča $P$, $\rho_{mv}$ i
   $p_{rgh}$ rabe se prije P5 (str. 61), gdje se uvode.
2. Z3, str. 65, 3. dio: „usporedi s okomitim U-manometrom” ne kaže čita li se razlika
   razina ili pomak jednog kraka (omjer 3,6 ili 7,3). Za obrazloženje kuta ključ nema
   kriterij.
3. Z6, str. 66, 2. dio: nominalni tlak već isključuje područje 0–140 kPa, pa tolerancije
   ne utječu na izbor. Rečenica u ključu („nominalna vrijednost sama nije dovoljna”) mene
   je kao studenta zbunila.
4. P3 i P5 (str. 58–63): ulaz se u P3 mjeri od referentne točke na palubi, a u P5 od vrha
   tanka. Dvije reference za isti pojam usporile su me.

**P3**
1. str. 50: diferencijalni manometar $p_1 - p_2 = (\rho_{Hg} - \rho) g \Delta h$ nigdje se
   ne izvodi hodom po stupcima.
2. str. 54: rečenica o „atmosferi kao nuli bez opravdanja” bez primjera kad to vrijedi.
3. str. 57, slika 3.3: oznake $p_1$, $h_1 = 0{,}60$ m, $h_2 = 0{,}10$ m i „0,40 m”
   preklapaju se s crtama cijevi.
4. str. 61, P4: $NPSH_a$ i $NPSH_r$ bez objašnjenja.
5. str. 62, slika 3.6: dvostruka oznaka $p_{atm}$ iznad odzračnika; oznaka
   $p_{M,unu,P}{}^A$ s eksponentom $A$ odvojenim od simbola.
6. str. 68, slika Z6: dublja točka nema ime. U tekstu se ne kaže unaprijed gdje je
   pretvornik.
7. Ključ Z3: oznaka $A$ za površinu posude, a u poglavlju je $A$ točka.

## Što mi je najviše pomoglo

- Pravilo na str. 54: „jedna referentna točka, jedan smjer, pri silasku dodaj
  $\rho g\Delta h$, pri usponu oduzmi”. Po njemu sam riješio Z3, Z6 i sve primjere.
- Odlomci „Veza s proračunom” prije svakog rješenja. Kažu koja je referenca, pa sam svaki
  put mogao sam postaviti prvi korak.
- „Provjera i tumačenje” s fizikalnim provjerama, npr. $p_{M,A} - p_{M,pl} = \rho g h$
  u P1 i dva neovisna mjerenja ulaža u P3.
- Napomene uz skice (str. 68), koje su razriješile dvojbu o nultoj oznaci u Z3.

## Ograničenje ovog čitanja

Ovo je procjena jednog simuliranog čitatelja koji zna predznanje s prve godine. Lakoću
ili težinu zadataka ne dokazuje za stvarne studente. Računske brojke primjera P1–P6 i
zadataka Z3 i Z6 provjerene su kalkulatorom. Ostali zadatci (Z1, Z2, Z4, Z5) nisu
rješavani.
