# Simulirano čitanje

Poglavlje 14 (Turbostrojevi i propulzija), knjiga str. 263–282, i ključ F.15
(str. 351–352). Ovo nije studentski pilot sa stvarnim studentima. Simulirani
student druge godine ima predznanje iz poglavlja 1–13 (količina i moment
količine gibanja, dimenzijska analiza, gubitci, crpke, radna točka). Zadatci
za samostalno rješavanje: Z3 i Z6.

Dogovoreno: ne prijavljujem ponovo „odgovarajući izraz” u ključu, upućivanja
„primjer N.M” umjesto Pk ni skriveni „Provjeri sebe”.

## Procjena vremena

Teoriju s izvodima čitao bih oko 2,5 h, šest riješenih primjera oko 3,5 h, a
Z3 i Z6 oko 1 h. Za cijelo poglavlje sa svim zadatcima trebalo bi mi 8–10 h,
što se slaže s navedenih 9 sati (str. 264).

## Tri mjesta na kojima bi student najvjerojatnije pogriješio ili odustao

1. **Predznak sile u obrnutom računu (str. 270 P1, str. 272 P2, str. 280 Z3).**
   Izraz ṁ(c₂ − c₁) daje silu lopatice na fluid. U Z3 je zadana sila fluida na
   lopaticu, pa c₂ = c₁ − F/ṁ_rel. Ako se zaboravi predznak, dobije se
   c₂x ≈ 66,7 m/s i c₂y ≈ −8,5 m/s, pa k > 1, što ne može biti. Uvjet
   pasivnosti 0 ≤ k ≤ 1 tu dobro hvata pogrešku, ali samo onoga tko ga provjeri.
   Sažetak na str. 282 tu pogrešku s pravom ističe.
2. **Izbor ṁ_rel ili ṁ (str. 265, str. 274 P3).** Dva optimuma, c₁/3 i c₁/2,
   razumio sam tek kad sam u P3 vidio isti trokut brzina s dva različita
   protoka. Iz same rečenice „razlikuju se kontrolni volumeni i zahvaćeni
   protoci” (str. 265) to ne bih znao primijeniti. Student će na kolokviju lako
   za Peltonovo kolo uzeti ρA(c₁ − u).
3. **Kut β mjeren od −u i predznak tangencijalne komponente (str. 265, 266, 275).**
   U P4 je w⃗₂ = (−c_m2/tan β₂; c_m2), a u Z3 β₂ treba dobiti iz atan2(w₂y, −w₂x).
   Tko je navikao kut mjeriti od +u, dobit će 150° umjesto 30° ili pogrešan
   predznak c₂t. U izvodu Eulerove jednadžbe (str. 266) nije izrijekom rečeno da
   je c_t pozitivan u smjeru vrtnje. To se kaže tek u P4 i Z4.

## Čitanje teorije: mjesta zastoja

| Mjesto | Što mi nije bilo jasno | Težina |
|---|---|---|
| str. 264, 14.1, uvod | U ṁ_rel = ρAw_n oznaka w_n nije objašnjena. Pretpostavljam da je to normalna komponenta relativne brzine. | P3 |
| str. 266, izvod Eulerove jednadžbe, (14.7)–(14.8) | „Pozitivan moment znači moment rotora na fluid”: moment je vektor (14.7), pa nisam znao uz koju os je pozitivan. Nije rečeno da je c_t pozitivan u smjeru vrtnje. Rečenicu sam čitao dvaput. | P2 |
| str. 267, Numerički pokus | „Nastavci obrađuju Z3–Z5”: Z3–Z5 u poglavlju nisu Peltonovi zadatci (Z3 je obrnuti račun lopatice, Z4 rotor na dva polumjera, Z5 vodomlazni pogon). Ne znam misli li se na zadatke iz bilježnice. Bilježnica se zove `u12_…`, a poglavlje je 14. | P2 |
| str. 267, Zastani i promisli | Odgovor je u istom okviru, odmah ispod. Već je izrečen i na str. 265 („Nijedan od dvaju rezultata nije pogrešan”). Pitanje provjerava pamćenje, ne razumijevanje. | P3 |
| str. 267 i 268 | Na str. 267 potisak je vezan uz jednadžbu (10.9), a disk uz (10.10). Na str. 268 piše „uz potisak iz jednadžbe (10.11)”. Nisam siguran koja je jednadžba potiska. U istom okviru je F_T = ρAv_d(v_j − v_A), pa bi uputa na nju bila jasnija. | P3 |
| str. 268, Provjera | „Za vodomlazni pogon isti izraz daje η_i = 2v_s/(v_s + v_j)”: zastao sam jer vodomlazni pogon nije disk. Shvatio sam tek kad sam sam uvrstio v_A = v_s. | P3 |
| str. 276, P4, Provjera i tumačenje | Pojam „faktor klizanja” u ovom poglavlju nije uveden i nema uputu na poglavlje u kojem bi bio. Ne znam odakle broj 0,82. | P2 |
| str. 277, P5, Provjera i tumačenje | Idealna snaga je ½ṁ(v_j² − v_A²), a gubitak u tragu ½ṁ(v_j − v_A)². Trebalo mi je vremena da vidim da je prvi izraz u okviru propelera, a drugi u okviru mirne vode. To nije rečeno. | P2 |
| str. 272, P2, Provjera i tumačenje | Energijska bilanca množi ṁ_rel s apsolutnim brzinama (c₁² − c₂²)/2. Brojevi se slažu (7,23 + 0,62 = 7,85 kW), ali ne znam zašto je to dopušteno za pokretni KV. Isti oblik koristi ključ za Z3. | P3 |
| str. 270, slika 14.2 | Luk kuta θ = 120° nacrtan je odvojeno, gore lijevo, a ne uz vodilicu. Morao sam iz teksta pročitati od čega se kut mjeri. | P3 |
| str. 272, P3 | „Tražena snaga generatora P_G = 9,5 kW” stoji odmah iznad „Traži se”, pa sam prvo pomislio da je P_G rezultat. Tek u rješenju vidim da je to potrošnja s kojom se uspoređuje. | P3 |
| str. 278, P6 | Podatci o bateriji (5 000 mAh, 14,8 V) pojavljuju se samo u provjeri, a ne u tekstu zadatka. | P3 |

## Riješeni primjeri: moj model prije rješenja

| Primjer | Moj model i prvi korak | Podudaranje | Napomena |
|---|---|---|---|
| P1 (str. 269) | KV oko vodilice, ṁ = ρbhv₁, F_v→f = ṁ(v⃗₂ − v⃗₁), zatim promjena predznaka | da | — |
| P2 (str. 271) | KV prati lopaticu, ṁ_rel = ρA(c₁ − u), w₂ = kw₁ pod β₂ od −x, c⃗₂ = u⃗ + w⃗₂ | da | Prvi korak naveo je „stvarno ulazi u pokretni KV” u 1. stavci |
| P3 (str. 272) | Prvo jedna lopatica s ṁ_rel, zatim kolo s ρAc₁ i istim trokutom | da | Tek ovdje sam stvarno razumio razliku dvaju optimuma |
| P4 (str. 274) | Euler s c₁t = 0, c_m = Q/(2πrb), w⃗₂ u smjeru lopatice | da | Formulu c_m = Q/(2πrb) poglavlje nije uvelo, ali je iz kontinuiteta razumljiva |
| P5 (str. 276) | C_Th → v_d iz (14.14), Δp = F_T/A, η_i | da | Vidi zastoj na str. 277 (dva izraza za kinetičku energiju) |
| P6 (str. 277) | F_T = mg/4, v_d iz (14.12), P_i = F_T v_d, P = P_i/FM | da | — |

Ni u jednom primjeru rješenje nije izabralo nešto što iz teksta nisam mogao znati.

## Zadatci za vježbu

### Z3. Izlaz lopatice iz izmjerene sile (str. 280, T2)

**Prije računa.**

- Kontrolni volumen prati lopaticu. Okvir je inercijski jer je u = konst.
- Zakon: bilanca količine gibanja, F⃗_f→l = ṁ_rel(c⃗₁ − c⃗₂). Za gubitak
  energijska bilanca u relativnom okviru.
- Referenca tlaka: atmosferski tlak na svim presjecima, pa nema tlačnih sila.
- Pozitivni smjerovi: +x u smjeru gibanja lopatice, +y prema gore.
- Pretpostavke: jednolike brzine na presjecima, bez težine, stacionarno u okviru
  lopatice.
- Granica modela: sile su „sintetički” podatci bez nesigurnosti. Sa stvarno
  izmjerenim silama k i β₂ bili bi osjetljivi na pogrešku F_y.
- Predviđanje: F_y < 0 znači da je fluid skrenut prema +y (c₂y > 0). F_x/ṁ_rel
  ≈ 35 m/s > c₁ − u = 20 m/s, pa mlaz mora biti vraćen unatrag, a c₂x malen i
  vjerojatno negativan.

**Moj rezultat.**

- c⃗₂ = (32 − 625/18; 153/18) = (−2,722; 8,500) m/s
- w⃗₂ = (−14,722; 8,500) m/s, |w⃗₂| = 17,00 m/s, w₁ = 20 m/s
- k = 0,850 i β₂ = 30,0°
- P = F_x u = 7,500 kW
- Ė_g = ṁ_rel(w₁² − w₂²)/2 = 0,999 kW
- ṁ_rel(c₁² − |c⃗₂|²)/2 = 8,499 kW = P + Ė_g, dakle uvjeti pasivnosti su
  zadovoljeni.

**Kontrolni rezultat (F.15, str. 351):** c⃗₂ ≈ (−2,722; 8,500), w⃗₂ ≈ (−14,722;
8,500), k ≈ 0,850, β₂ ≈ 30,00°, P = 7,500 kW, Ė_g ≈ 0,999 kW. **Podudaranje: da.**

**Gdje sam zapeo.** Nisam pravo zapeo. Na trenutak nisam znao u kojem okviru
treba računati „stopu gubitka mehaničke energije”. Izabrao sam relativni okvir
(po uzoru na P3, str. 274). Ključ računa iz apsolutnih brzina minus P.
Rezultat je isti, a dobro je što ključ to pokazuje kao provjeru.

**Ključ.** Smjernica je razumljiva bez poglavlja. Oblik β₂ = atan2(w₂y, −w₂x)
jasno pokazuje konvenciju kuta. Kut skretanja θ = 150° naveden je iako ga
zadatak ne traži. Ne smeta, ali mogao bih pomisliti da sam ga trebao
izračunati.

### Z6. Podizanje mlazne platforme (str. 281, T4)

**Prije računa.**

- Sustav: platforma s fluidom u njoj. Kontrolni volumen je oko nje, u trenutku
  mirovanja (kvazistacionarno).
- Zakon: Newtonov zakon za KV, m a = ΣF + (ulazni − izlazni) tok količine
  gibanja. Okomiti ulazni tok je nula, dovodi ne daju okomitu silu.
- Referenca tlaka: atmosferski tlak na izlazima.
- Pozitivni smjer: +y prema gore.
- Pretpostavke: jednolika brzina u sapnicama, bez akumulacije u razdjelniku.
- Granica modela: vrijedi samo u trenutku mirovanja. Kad se platforma ubrza,
  mijenjaju se relativni uvjeti i sila dovodnih cijevi.
- Predviđanje: potisak reda 3 kN (4 · ~22 kg/s · 36 m/s), ubrzanje reda g,
  pozitivno.

**Moj rezultat.**

- Protok jedne sapnice ṁ₁ = 22,12 kg/s, pa je F_T = 4ρAv² = 3,186 kN.
- Najveća masa lebdenja F_T/g = 324,7 kg.
- a = F_T/m − g = 19,15 m/s² prema gore.
- Najgori slučaj: d = 27,7 mm, v = 34,5 m/s. F_T raste i s d i s v, pa su
  rubovi intervala dovoljni. Dobivam F_T,min = 2,863 kN i
  m_max = F_T,min/(1,1g) = 265,3 kg.

**Kontrolni rezultat (F.15, str. 352):** F_T ≈ 3,186 kN, 324,7 kg, a ≈ 19,15 m/s²,
F_T,min ≈ 2,863 kN, m_krit ≈ 265,3 kg. **Podudaranje: da.**

**Gdje sam zapeo.**

- Izraz „akumulaciju relativne količine gibanja u razdjelniku” (str. 282)
  pročitao sam dvaput. Nisam znao je li „relativne” bitno ili je to samo
  zato što je v zadan „u odnosu na platformu”.
- U 2. stavci piše „stvarni promjer **svake** sapnice”. Pitao sam se smiju li
  sapnice odstupati različito. Tada potisci nisu jednaki i javlja se moment
  koji naginje platformu. Zadatak to ne spominje. Ključ stabilnost navodi
  samo kao nedostajuću provjeru.
- Za 3. stavku („certificirana nosivost”) nisam znao koliko opširan odgovor
  se očekuje. Ključ navodi popis (sile dovoda, dinamika, stabilnost,
  konstrukcijska i upravljačka provjera), pa sam svoj odgovor mogao usporediti.
- Zadatak mi se, iskreno, činio lakšim od Z5 (T3). Račun je jedna formula.
  Teže su samo odluka o najgorem slučaju i tumačenje.

**Ključ.** U smjernici je A „zbroj četiriju površina”. To je napisano, ali
F_T = ρAv² bez indeksa lako je pročitati kao jednu sapnicu. Oznaka m_krit
ne pojavljuje se u tekstu zadatka (ondje piše „najveću masu”), ali je
razumljiva. Smjernica ne otkriva rješenje više nego što treba.

## Popis nejasnoća po težini

**P1:** nema. Nigdje nisam bio blokiran niti bih naučio nešto pogrešno.

**P2:**

- str. 266, izvod Eulerove jednadžbe: nije rečeno da je c_t pozitivan u smjeru
  vrtnje. Nije jasno uz koju os je moment „pozitivan”.
- str. 267, Numerički pokus: „Nastavci obrađuju Z3–Z5” ne odgovara zadatcima
  Z3–Z5 u poglavlju.
- str. 276, P4: „faktor klizanja” nije uveden.
- str. 277, P5: dva izraza za kinetičku energiju (½ṁ(v_j² − v_A²) i
  ½ṁ(v_j − v_A)²) nisu povezana s okvirom promatranja.

**P3:**

- str. 264: w_n nije objašnjen.
- str. 267: „Zastani i promisli” ima odgovor odmah ispod i već na str. 265.
- str. 268: nejasno je koja je jednadžba potiska, (10.9) ili (10.11).
- str. 268: η_i za vodomlazni pogon zahtijeva prešutno v_A = v_s.
- str. 270: luk kuta θ na slici 14.2 odvojen je od vodilice.
- str. 272, P2: energijska bilanca s ṁ_rel i apsolutnim brzinama nije
  objašnjena.
- str. 272, P3: „Tražena snaga generatora” uz „Traži se” zbunjuje.
- str. 278, P6: podatci o bateriji samo u provjeri.
- str. 282, Z6: „akumulacija relativne količine gibanja” i moguće nejednako
  odstupanje sapnica.
- Ključ Z3: θ = 150° naveden je iako se ne traži.

## Što mi je najviše pomoglo

- P3 (str. 272–274): ista lopatica računata najprije s ṁ_rel, a zatim s punim
  protokom, uz omjer P_kolo/P_lop = c₁/(c₁ − u). Tek mi je to objasnilo dva
  optimuma.
- Svaki primjer ima „Provjeru i tumačenje” s energijskom bilancom
  (str. 272, 274, 276). Isti obrazac primijenio sam u Z3 i odmah znao je li
  rezultat dobar.
- Uvjeti pasivnosti u Z3 (0 ≤ k ≤ 1, Ė_g ≥ 0) daju mi samokontrolu predznaka
  bez gledanja u ključ.
- „Konvencija kuta” (str. 265) na jednom mjestu kaže od čega se mjeri β.

## Ograničenja ovog čitanja

Ovo je simulirano čitanje jednog modela. Nije mjerenje na stvarnim studentima.
Procjene vremena i težine su autorska procjena simuliranog studenta.
Podudaranje Z3 i Z6 s ključem pokazuje samo da su tekst i ključ međusobno
dosljedni. Ne dokazuje didaktičku kvalitetu zadataka.
