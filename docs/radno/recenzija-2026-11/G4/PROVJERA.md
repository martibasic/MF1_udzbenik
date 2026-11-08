# Provjera nalaza G4: pog. 14, pog. 15, pog. 0 i dodatci A–E

Provjereno 8. 11. 2026. prema koraku 5 skilla `recenzija-prirucnika`. Ulaz su
izvještaji `struka.md`, `primjena.md`, `urednik.md` i `student_pog14.md` u ovoj
mapi. Svaki nalaz P0–P2 provjeren je u izvoru (`source/`, stanje radnog stabla
na grani `konvencije-recenzije`) i, gdje je potrebno, u PDF-u, bilježnici,
ključu (D06) ili drugom poglavlju. Nijedna datoteka osim ove nije mijenjana.

Izvršene provjere:

- pokrenuti su kanonski verifikatori (prema `CANONICAL_CHAPTERS`):
  `verify_u12.py` za pog. 14 (122 provjere, 0 pogrešaka) i
  `verify_u15_open_channels.py` za pog. 15 (80 provjera, 0 pogrešaka);
- vlastiti računi su u `…/scratchpad/knjiga/prov_G4/racun1.py` (pog. 15 Z2 i Z6),
  `racun2.py` (pog. 14) i `kolo.py` (kut lopatica na skici iz SVG koordinata);
- `prirucnik_stats.py --nalazi` potvrđuje za ove izvore samo u14:17, u14:136 (K3)
  i u14:290 (K12); ostali nalazi urednika provjereni su čitanjem;
- render: str. 275 (sl. 14.5) i str. 292 (sl. 15.2) pregledani su u PDF-u,
  a tekst svih isječaka izvučen je s `pdftotext`.

Preskočeni su poznati nalazi na razini knjige (ključ „odgovarajući izraz”,
„primjer N.M”, skriveni „Provjeri sebe”, F.(N+1), naziv bilježnice `u12_…`,
ponovljene stranice u izdvojenom PDF-u ključa).

Kratice: `u14` = `source/u14_turbostrojevi_i_propulzija.md`, `u15` =
`source/u15_otvoreni_tokovi.md`, `u00` = `source/u00_kako_koristiti_udzbenik.md`,
`d0N` = odgovarajući dodatak. Izvori čitatelja: S = struka, A = primjena,
U = urednik, St = student.

## Tablica nalaza P0–P2

P0: nijedan čitatelj ga nije prijavio, a provjera ga nije našla.

| ID | Mjesto | Nalaz | Izvor | Težina | Status | Vrsta | Prijedlog ispravka |
|---|---|---|---|---|---|---|---|
| G4-01 | u14:702–874; u10:1025–1056, u10:279–294 | Pog. 14 Z2 isti je problem kao pog. 10 Z5 (jedna ploča, $u=v/3$) spojen s korakom 4 primjera P1 pog. 10 (kolo, $u=v/2$), samo s drugim brojevima. Ishod 3 iz sažetka (u14:893: aktuatorski disk, $C_{Th}$, sustrujanje) nema samostalnog zadatka u pog. 14. Djelomično: Z1 je legitiman jednostavan T1; ishod 2 pokriva Z4 (trokuti i predznak rada), pa je dio tvrdnje o ishodu 2 odbačen. Obvezna provjera iz matrice (znak rada, trokut brzina, raspoloživa snaga) pokrivena je sa Z4 i Z5. | S P1-1 | P1 | POTVRĐENO (djelomično) | AUTORSKA ODLUKA | Prema protokolu prerade zamijeniti Z2 zadatkom na aktuatorskom disku ($C_{Th}$, $FM$ ili $\chi$), a Z6 ocijeniti zajedno s G4-20; Z1 zadržati. |
| G4-02 | u15:481 (`task-istjecanje-ispod-ustave`, kontrolni rezultat) | „$C_d$ pada na 0,547 jer brzina dolaska uzvodno raste” obrnuto je: član brzine dolaska povećava $C_d$; pad dolazi od relativnog smanjenja $y_0-y_1$. Vidljivo u webu; u PDF-u ključ taj dio odsijeca (G4-15). | S P1-2 | P1 | POTVRĐENO (račun niže) | TEKST | Zamijeniti obrazloženje: „veći otvor daje dublji suženi mlaz, pa se razlika $y_0-y_1$ relativno smanjuje; veća brzina dolaska taj pad samo djelomično nadoknađuje.” |
| G4-03 | u15:586–595 (`task-klimatski-kanal`), u15:421, sl. 15.2 Z6, bilježnica `u15_otvoreni_tokovi.ipynb` ćelija 11 | $y_{2,dop}=1{,}40$ m nigdje nije definiran; napomena uz skicu sama kaže da je „samo podatak”. Bilježnica ga koristi kao gornju granicu (`y2_design<y2_allowed<y2_cap[0]`), a P4 istog poglavlja odluku veže uz nizvodni vodostaj $y_{nv}$. „Traži se 2” zato ne vodi do fizikalne odluke (K15). Dio „bazen nije povezan s kanalom” je djelomičan: odvojenost je izrijekom zadana (naslov panela, „zaseban kontrolni volumen”), pa je zadatak rješiv. | S P1-3, A P2-5 | P1 | POTVRĐENO (definicija); spoj kanala i bazena djelomično | TEKST, SKICA (oznaka); BROJ/MODEL ako se doda $y_{nv}$ | Imenovati veličinu (raspoloživa nizvodna dubina $y_{nv}$ ili najveća dubina zidova bazena) i u „Traži se 2” tražiti odluku ostaje li skok u bazenu; jednom rečenicom navesti da $y_1$ daje brzotok ili pad dna. |
| G4-04 | u15:173–183 | $C_d\approx0{,}55$–$0{,}60$ i „$C_{pr}$ … blizu jedinice” bez izvora i bez raspona $a/y_0$; Z2 pri $a/y_0=0{,}4$ daje 0,547, izvan navedenog raspona. | S P2-7, A P2-4 | P2 | POTVRĐENO | TEKST | Navesti raspon $a/y_0$ i izvor koji te vrijednosti stvarno daje, ili ih označiti kao nastavnu procjenu. |
| G4-05 | u14 (0 citata); u14:584 | Pog. 14 nema nijedan izvor; $\eta_0\approx0{,}55$–$0{,}70$ i optimum Peltonova kola bez izvora; dodatak E nema djelo o turbostrojevima ni propelerima. | S P2-6, A P2-4 | P2 | POTVRĐENO | TEKST | Dodati u dodatak E po jedan standardni izvor za turbostrojeve i brodske propelere i citirati ih uz $\eta_0$ i $H_{th}$; inače raspon označiti kao orijentaciju. |
| G4-06 | u14:478, 496, 532 | „Meridijanske komponente” i „faktor klizanja” nisu definirani u knjizi (nema ih ni u dodatcima A i B); umnožak 0,82 nema izvor. Primjenski dio („0,82 je optimistično”) računom izgleda točan (Wiesner uz pretpostavljenih 6–7 lopatica daje $c_{2t}/c_{2t,\infty}\approx0{,}74$–$0{,}76$, umnožak s $\eta_h=0{,}85$–$0{,}90$ oko 0,63–0,69), ali broj lopatica nije zadan, pa je taj dio nepotvrdiv. | S P2-5, U, St P2, A P2-4 | P2 | POTVRĐENO (definicije); NEPOTVRDIVO (vrijednost 0,82) | TEKST | Jednom rečenicom definirati meridijansku komponentu (ovdje radijalna) i faktor klizanja; 0,82 označiti kao nastavnu pretpostavku. |
| G4-07 | u14:367–467 (P3 Pelton) | $P_G=9{,}5$ kW zadan je u tekstu, a nijedna stavka „Traži se” ne traži usporedbu; $10{,}49\cdot0{,}96\cdot0{,}94=9{,}47$ kW, dakle podatak odgovara upravo pogrešnom modelu jedne lopatice. Stavka 4 traži „snagu koju mlaz predaje rotoru”, a rješenje kaže da to nije snaga kola. Odluka koja bi opravdala T4 stoji samo u rješenju. | S P2-3, St P3 | P2 | POTVRĐENO | TEKST; razina AUTORSKA ODLUKA | Stavku 4 vezati uz jednu lopaticu u modelu lopatice koja se udaljava i u stavci 5 izrijekom tražiti usporedbu s $P_G$; inače razinu spustiti na T3. |
| G4-08 | u14:462, 466 | U istom primjeru triput stoji da snaga jedne lopatice nije snaga kola; optimum dvaput s različitim zaokruživanjem ($\approx0{,}50$ i $0{,}497$). | U | P2 | POTVRĐENO | TEKST | Izostaviti posljednju rečenicu r. 462; vrijednost 0,497 ostaje u r. 466. |
| G4-09 | u14:482, sl. 14.5 (`assets/print/u12_val3_pokretna_lopatica.svg`) | Lopatice su gotovo ravne i na izlaznom krugu zatvaraju oko $64^\circ$ sa smjerom $-u$ (izmjereno iz koordinata SVG-a), a podatak je $\beta_2=25^\circ$; `fig-alt` govori o „unatrag zakrivljenim” lopaticama. Izlazni trokut na istoj slici ispravan je. | S P2-4 | P2 | POTVRĐENO (izmjereno) | SKICA | Nacrtati zakrivljene lopatice s $\beta_2=25^\circ$ na $r_2$ i $\beta_1\approx20{,}5^\circ$ na $r_1$ u postojećem stilu, uz obnovu tiskovnih izvedenica. |
| G4-10 | u14:5, u14:207 | „Propeler i vodomlazni pogon modeliraju se aktuatorskim diskom”: vodomlazni pogon knjiga računa bilancom kanala s crpkom (`eq-potisak-mlaznog-pogona`); s diskom dijeli samo izraz za $\eta_i$ uz $v_A=v_s$, što r. 207 prešutno pretpostavlja. | S P2-1, St P3 | P2 | POTVRĐENO | TEKST | „Propeler se modelira aktuatorskim diskom; vodomlazni pogon ima isti izraz za idealnu učinkovitost uz $v_A=v_s$.” |
| G4-11 | u14:191–197; u10:177–182 | $\eta_i=2v_A/(v_A+v_j)$ već je dio `eq-aktuatorski-disk-potisak` u pog. 10, a pog. 14 ga ponovno izvodi pod novom oznakom (K10). Student pritom nije znao koja je jednadžba potiska. | S P2-2, St P3 | P2 | POTVRĐENO | TEKST | Uputiti na jednadžbu pog. 10 i izvesti samo zapis preko $C_{Th}$ i lebdenje; oznaku `eq-idealna-ucinkovitost-propelera` zadržati jer je koristi Z5 (u14:829). |
| G4-12 | u14:584 (P5, Provjera i tumačenje) | „…pa se bira najveći propeler koji gaz i trup dopuštaju” iznosi zaključak modela diska kao pravilo projektiranja (K9). | A P2-3, S P3-2 | P2 | POTVRĐENO | TEKST | „U modelu diska veći promjer štedi snagu; stvarni izbor ograničavaju i brzina vrtnje pogona, zračnost prema trupu i uron vrha lopatica.” |
| G4-13 | u14:99–111 | Izvod Eulerove jednadžbe kaže „pozitivan moment znači moment rotora na fluid”, ali ne kaže oko koje osi ni da je $c_t$ pozitivan u smjeru vrtnje; to se kaže tek u P4 i Z4. | St P2 | P2 | POTVRĐENO | TEKST | Dodati: „$c_t$ i moment pozitivni su u smjeru vrtnje rotora.” |
| G4-14 | u14:584 | „$P_i-F_Tv_A=212$ kW jest tok kinetičke energije traga $\tfrac12\dot m(v_j-v_A)^2$”: račun je točan (1172 i 212 kW), ali nije rečeno da je $\tfrac12\dot m(v_j^2-v_A^2)$ u okviru propelera, a $\tfrac12\dot m(v_j-v_A)^2$ u okviru mirne vode. | St P2 | P2 | POTVRĐENO | TEKST | Uz drugi izraz dodati „u okviru mirne vode”. |
| G4-15 | u14:749, u15:481; `scripts/generate_exercise_key.py:111–122` | Ključ u dodatku F skraćuje odgovor na 500 znakova ako nema `data-key-full`; pog. 14 Z2 (601 znak) gubi optimume, pog. 15 Z2 (558 znakova) cijeli dio 3. To su jedina dva takva odgovora u G4. | S P2-8 | P2 | POTVRĐENO | TEKST (oznaka i obnova D06 generatorom) | Označiti oba odgovora s `data-key-full="true"` (nakon G4-02) i provjeriti pravilo za višedijelne zadatke u cijeloj knjizi. |
| G4-16 | u15:522, sl. 15.2 Z4, ključ | U Z4 je $y_1=1{,}200$ m mirna uzvodna dubina, iako uvod (u15:9) indekse 1 i 2 veže uz skok, a u15:170 uzvodnu dubinu označuje s $y_0$ (K6). | S P2-9 | P2 | POTVRĐENO | TEKST, SKICA (oznaka) | U Z4, naputku, ključu, skici i verifikatoru pisati $y_0$ i $E_0$. |
| G4-17 | d04:5–12 | Tablica „Povezani primjeri kroz knjigu” u PDF-u ostaje goli tekst bez broja poglavlja (potvrđeno u tekstu PDF-a). | S P2-10 | P2 | POTVRĐENO | TEKST | Uz svaku poveznicu dodati „pog. N”. |
| G4-18 | d04:183 | Versteeg i Malalasekera te Ferziger, Perić i Street bez izdanja, izdavača i godine; nisu u dodatku E (K14). | S P2-11, U | P2 | POTVRĐENO | TEKST | Unijeti oba djela u `references.bib` s aktualnim izdanjem i citirati ključem. |
| G4-19 | pog. 15, P1–P5 i Z1–Z6 | Sve primjene pripadaju gradskom kanalu i ustavi; brodogradnja je samo u okviru o plitkoj vodi (u15:56), bez računa; strojarstva nema. Matrica pog. 15 određuje lajtmotiv „klimatski otporan vodni grad”, pa to nije kršenje ugovora. | A P2-1 | P2 | POTVRĐENO (činjenica) | AUTORSKA ODLUKA | Pri sljedećoj reviziji pog. 15 razmotriti jedan Z iste razine iz brodogradnje ili strojarstva, bez dodavanja mjesta. |
| G4-20 | u14:847–874 (Z6) | Potisak je $2{,}95\,mg$ ($a=19{,}15$ m/s²), a hidraulička snaga mlazova $57{,}3$ kW (račun). Uz 265 kg prema 110 kg odluka o 10 % rezerve postaje trivijalna; student je Z6 ocijenio lakšim od Z5 (T3). Tvrdnja da „nijedna upravljana naprava” ne radi s takvom rezervom je iz prakse bez izvora. | A P2-2, St P3 | P2 | POTVRĐENO (račun); NEPOTVRDIVO (tvrdnja o praksi) | AUTORSKA ODLUKA; BROJ/MODEL ako se mijenja $v$ | Odlučiti zajedno s G4-01; uz zadržavanje imenovati uređaj i pri $v\approx22$–$24$ m/s ($F_T/mg=1{,}10$–$1{,}31$) obnoviti ključ, verifikator i bilježnicu. |
| G4-21 | pog. 14 | Lajtmotiv pomorske dekarbonizacije nije imenovan; prijedlog Betzove granice i vjetroagregata. Matrica za pog. 14 navodi lajtmotiv „pumpa, turbina i propeler”; uzdužni lajtmotiv ondje se ne pojavljuje, pa nema „ponovne pojave” koju bi K16 tražio. $C_P\approx0{,}45$–$0{,}5$ je po sjećanju. | A P2-6 | P3 | ODBAČENO kao P2 (matrica) | AUTORSKA ODLUKA | Ostaje prijedlog za banku alternativa. |
| G4-22 | d04:5–12; u14:132, 216; u15:228, 369 | U tablici dodatka D nema niza trup–propeler; četiri CFD odlomka nemaju stabilni ID (potvrđeno). Nedostatak sadržaja, ne pogreška. | A P2-7 | P3 | POTVRĐENO (činjenica) | AUTORSKA ODLUKA | Ako se doda redak, CFD odlomcima dati nove semantičke ID-jeve. |
| G4-23 | u14:3, 5, 7, 17 | Uvod unaprijed donosi $\dot m_{rel}$, oba optimuma, Eulerovu jednadžbu, $\eta_i$ i ogradu iz Granice modela; r. 17 ponavlja oznake iz r. 3 (K10). Ugovor dopušta da uvod imenuje zakone, ali ne niz formula koji se zatim izvodi. | U | P2 | POTVRĐENO | TEKST | Zakone u uvodu navesti riječima, formule ostaviti izvodima; izostaviti posljednju rečenicu r. 17. |
| G4-24 | u14:3, 49, 79, 87, 130 | Tvrdnja da rad daje samo tangencijalna komponenta, pa su kutovi lopatica projektni parametri, stoji pet puta (K10). | U | P2 | POTVRĐENO | TEKST | Zadržati r. 49 i r. 130, a okvir r. 85–88 i rečenicu u uvodu izostaviti. |
| G4-25 | u14:31, 76 | Okvir „Konvencija kuta” ponavlja definiciju iz r. 31. | U | P3 | POTVRĐENO, snižen | TEKST | Student ga navodi kao korisno sažeto pravilo; skratiti samo ako autorica želi. |
| G4-26 | u14:290, 587 | „u sljedećem primjeru” i „Posljednji primjer” umjesto broja (K12; r. 290 bilježi i alat). | U | P2 | POTVRĐENO | TEKST | Uputiti s `[-@ex-…]`. |
| G4-27 | u14:17 | Rečenica od 47 riječi (K3, potvrđeno alatom). | U | P2 | POTVRĐENO | TEKST | Podijeliti na tri rečenice prema prijedlogu urednika. |
| G4-28 | u14:127 | Duga rečenica s umetkom „umnožak … sile … i obodne brzine”; alat je ne bilježi iznad 40 riječi. | U | P3 | POTVRĐENO, snižen | TEKST | Podijeliti na dvije rečenice. |
| G4-29 | u14:136, u14:594, u15:56 | MRF (*Multiple Reference Frame*), *figure of merit* i *squat* bez „engl.” (K5). | U, S P3-3 | P2 | POTVRĐENO | TEKST | „model s više referentnih okvira (engl. *Multiple Reference Frame*, MRF)”, „(engl. *figure of merit*)”, „(engl. *squat*)”. |
| G4-30 | u14:3, 95, 111; d02:28; u10:7, 202 | Isti zakon ima tri naziva: „Eulerova jednadžba turbostrojarstva”, „Eulerova turbinska jednadžba” (i pog. 10) i „Eulerova jednadžba turbostroja” (pojmovnik). | U | P2 | POTVRĐENO | AUTORSKA ODLUKA (nazivlje) | Autorica bira jedan naziv; zatim uskladiti pog. 10, pog. 14 i dodatak B bez promjene ID-jeva jednadžbi. |
| G4-31 | u14:240, 308, 382 | Potpisi „Vodilica mlaza na ispitnom stolu.”, „Pokretna zakrivljena lopatica.”, „Peltonov rotor s jednim mlazom.” ponavljaju naslov primjera i ne kažu što slika pokazuje (K13). | U, S P3-4 | P2 | POTVRĐENO | TEKST | Opisne rečenice prema prijedlogu urednika; `fig-alt` tada opisuje raspored crteža. |
| G4-32 | u14:448 | Samo peti korak rješenja ima naslov s brojem („5. Cijelo kolo …”); u PDF-u „5.” stoji bez prethodnika. | U | P2 | POTVRĐENO (PDF) | TEKST | Pretvoriti u podebljani uvod bez broja ili numerirati sve korake. |
| G4-33 | u14:148 | Student: „Nastavci obrađuju Z3–Z5” ne odgovara zadatcima. Bilježnica `u12_pelton_lopatica.ipynb` ima odjeljke 4–6 upravo za Z3, Z4 i Z5 pog. 14, pa je tvrdnja netočna; ostaje samo nejasan subjekt („nastavci”). | St P2, U | P3 | ODBAČENO kao P2 (cilj postoji) | TEKST | „Nastavci bilježnice obrađuju Z3–Z5.” |
| G4-34 | u14:698 | „trokute $\vec c=\vec u+\vec w$ crta student” (K2: bez bezličnog „student”). | U | P2 | POTVRĐENO | TEKST | „… nacrtaj sam.” |
| G4-35 | u14:218, u15:230 | Podebljani uvod CFD odlomka u obliku pitanja (K4). Isti je obrazac u 17 CFD odlomaka cijele knjige, a K4 izrijekom pokriva naslove odjeljaka i zadataka, ne uvod okvira. | U, S P3-12 | P3 | ODBAČENO kao nalaz G4 (obrazac knjige) | AUTORSKA ODLUKA | Pitanje autorici: vrijedi li K4 i za uvode CFD okvira; ako da, ispraviti svih 17 odjednom. |
| G4-36 | u15:3, 7 | Uvod donosi $Fr$, $E$, $y_c$, $E_{min}$, $I_1=I_2$ i zaključak o bilanci skoka, koji se izvode i ponavljaju u r. 237; r. 7 ponavlja ograde iz r. 183, 284 i Sažetka (K10). | U | P2 | POTVRĐENO | TEKST | Režime i zakone u uvodu navesti riječima; ograde ostaviti u Granici modela i Sažetku. |
| G4-37 | u15:15 | Odjeljak „## Otvoreni tokovi” ponavlja naslov poglavlja i r. 1. | U | P2 | POTVRĐENO | TEKST | Izjavni naslov teme ili pripajanje uvodu, uz zadržani `sec-otvoreni-tok-motivacija`. |
| G4-38 | u15:244 | „Valjak” (8 pojava) nije definiran pri prvoj uporabi (K5). | U | P2 | POTVRĐENO | TEKST | „… izvan valjka, vrtložnog područja povratnog toka na površini skoka, …” |
| G4-39 | u15:328, u15:564 | VOF i GUM javljaju se po jednom, bez punog naziva (K5). | U | P2 | POTVRĐENO | TEKST | Pun naziv uz „engl.”; GUM unijeti u dodatak E. |
| G4-40 | u15:165 | „(vidi odjeljak o kontrolnim građevinama)” (K12). | U, S P3-7 | P2 | POTVRĐENO | TEKST | „(odjeljak [-@sec-kontrolne-gradevine])”. |
| G4-41 | u15:90 | „obje informacije” nema izričit prethodnik. Prethodni odlomak (r. 88) imenuje ulazni protok i izlaznu razinu, pa je smisao razumljiv. | U | P3 | POTVRĐENO, snižen | TEKST | „oba rubna podatka”. |
| G4-42 | u15:232 | „S hidrostatičkim modelom ne uspoređujemo …” bez objekta. | U | P3 | POTVRĐENO, snižen | TEKST | „Rezultate prostornog modela ne uspoređujemo s hidrostatičkim …”. |
| G4-43 | u00:7 | Prvi spomen kratice CFD u knjizi bez veze s punim nazivom (K5). | U | P2 | POTVRĐENO | TEKST | „… odlomci *Računalna dinamika fluida* (engl. *Computational Fluid Dynamics*, CFD) …” |
| G4-44 | u00:71 | „## Dodaci za brzo snalaženje” uz „dodatci” u uredničkom stilu (K7). | U | P2 | POTVRĐENO | TEKST | „Dodatci”. |
| G4-45 | u00:38 | Primjer upućivanja „poglavlje 3, Z2”, a knjiga piše „pog. 3” (K1, K12). | U | P2 | POTVRĐENO | TEKST | „pog. 3, Z2”. |
| G4-46 | d01:50, 63, 86, 101, 119, 131, 147, 163, 181, 192 | Deset naslova počinje malim slovom („A.2 pog. 1–2: …”). | U | P2 | POTVRĐENO | TEKST | „Osnovne veličine … (pog. 1–2)” ili „Pog. 1–2: …”. |
| G4-47 | d04:26; d02:80, 105, 112 | d04:26 tvrdi da pojmovnik definira MRF, RANS, SST, SIMPLE i PISO, a pojmovnik ih opisuje bez punog naziva. | U | P2 | POTVRĐENO | TEKST | Pune nazive (engl.) dodati u pojmovnik. |
| G4-48 | d04:154, 183; d04:31 | „V&V” u naslovu D.8 nigdje nije razriješen; LES/DNS ima opis, ali ne puni naziv. | U | P2 (V&V); LES/DNS P3 | POTVRĐENO | TEKST | „Pripremljeni paketi za verifikaciju i validaciju (V&V)”. |
| G4-49 | d04:167, 173 | „Validator `python tools/validate_cfd_vv.py` …” i „`teaching_comparison.json`” su interna izrada u vidljivom tekstu (K1). | U, S P3-10 | P2 | POTVRĐENO | TEKST | „Uz pakete je priložena skripta koja provjerava …”; „… zapisani su u opisu paketa.” |
| G4-50 | `references.bib` (`virag`), d05:5 | Zapis Virag nema godinu ni izdanje (K14). | U | P2 | POTVRĐENO | TEKST | Dopuniti godinom i izdanjem nakon provjere u izvoru. |
| G4-51 | d03:325 | „Izostavljen ulazni tok … $\dot mv_A$ … (Z5)”, a Z5 pog. 14 računa s $v_s$ (K6). | U | P2 | POTVRĐENO | TEKST | $\dot mv_s$. |
| G4-52 | d03:280 | Dvije pogreške spojene zarezom u jednoj natuknici (K3). | U | P2 | POTVRĐENO | TEKST | Razdvojiti u dvije natuknice. |

## Računi za P1

**G4-01.** pog. 14 Z2: $A=4{,}909\cdot10^{-4}$ m², $\dot m_{ml}=14{,}70$ kg/s; (a)
$F=196$ N, $P=1{,}96$ kW, $\eta=0{,}296=8/27$ pri $u=v/3$; (b) optimum $u=v/2$,
$F=220$ N, $P=3{,}31$ kW, $\eta=0{,}5$. Pog. 10 Z5 (`task-mlaz-na-pomicnu-plocu`,
T3) maksimizira istu funkciju $u(v-u)^2$ s optimumom $u=v/3$, a pog. 10 P1 korak 4
(`ex-peltonova-lopatica-u-gibanju`) daje $u=v/2$ za kolo. Isti par optimuma izveden
je i u u14:51–72. Pretraga u14:694–874 nema $C_{Th}$, $FM$ ni $\chi$ ni u jednom
zadatku.

**G4-02.** $y_0=2{,}00$ m, $C_c=0{,}61$. Iz energijske jednadžbe
$q=y_1\sqrt{2g(y_0-y_1)/[1-(y_1/y_0)^2]}$, pa je $C_d=C_c/\sqrt{1+y_1/y_0}$.
Bez člana brzine dolaska $C_d=C_c\sqrt{1-y_1/y_0}$.

| $a$ (m) | $y_1$ (m) | $q$ (m²/s) | $C_d$ | $C_d$ bez brzine dolaska | faktor $1/\sqrt{1-(y_1/y_0)^2}$ |
|---|---|---|---|---|---|
| 0,400 | 0,244 | 1,443 | 0,5759 | 0,5716 | 1,0075 |
| 0,800 | 0,488 | 2,741 | 0,5469 | 0,5304 | 1,0312 |

Brzina dolaska podiže $C_d$ za 0,004 odnosno 0,017. Pad s 0,576 na 0,547 nastaje
jer $(y_0-y_1)/y_0$ pada s 0,878 na 0,756.

**G4-03.** Kanal pri $Q_d=8$ m³/s: $y_n=0{,}985/1{,}189/1{,}380$ m,
$Fr=0{,}62/0{,}44/0{,}33$, $E=1{,}12/1{,}27/1{,}43$ m (A/B/C). Bazen: $q=1{,}60$ m²/s,
$v_1=4{,}57$ m/s, $Fr_1=2{,}47$, $E_1=1{,}415$ m, $y_2=1{,}059$ m. Za stanje A od
mirnog toka u kanalu do zadanog silovitog ulaza bazena treba bez gubitaka pad dna
od najmanje oko 0,29 m. $y_2=1{,}40$ m dosegnulo bi se tek pri $Q\approx10{,}25$ m³/s,
a pri kapacitetu A ($11{,}76$ m³/s) je $y_2=1{,}63$ m. Na tome se temelji asercija u
bilježnici. Rezultati se slažu s ključem i s `verify_u15_open_channels.py`.

## Što je dobro

- Svi brojevi riješenih primjera i kontrolnih rezultata pog. 14 i 15 koje su
  čitatelji ponovno izračunali slažu se s vlastitim računom. Oba kanonska
  verifikatora prolaze (122 i 80 provjera).
- Predznaci su u pog. 14 dosljedni ($M_{r\to f}$ i $M_{f\to r}$, sila vodilice i
  sila fluida, $\beta$ od $-u$, $\theta=180^\circ-\beta_2$). P3 Pelton istim trokutom
  brzina s dva protoka objašnjava oba optimuma; student ga navodi kao mjesto na
  kojem je razlika postala jasna.
- Gotovo svaki primjer zatvara energijsku bilancu. Provjereno je za P2
  ($7{,}85=7{,}23+0{,}62$ kW), P3 ($22{,}6$ kW) i P5 (trag $212$ kW).
- Pog. 14 Z3 (obrnuti račun s uvjetom pasivnosti) i pog. 15 Z5 (rezidual
  impulsne funkcije s koreliranim $q$) mijenjaju vrstu razmišljanja. Odluka o
  položaju skoka prema $y_{nv}$ u pog. 15 P4 fizikalno je točna.
- Dodatak D pošteno označuje sintetičke pakete i nastavne nesigurnosti. GCI ne
  izjednačuje sa standardnom nesigurnošću; interpolacija $C_D=0{,}01166$ je točna.

Ovo je autorska procjena čitatelja i provjera računom. Didaktička kvaliteta
time nije dokazana.

## Sažetak P3

Izvorni P3: struka 12, primjena 11, urednik 15 skupina, student 10, ukupno 48
stavki. Uz to je 8 nalaza P2 sniženo na P3 i navedeno je u tablici.

1. K5, engleski izrazi i kratice: *Jupyter notebooks*, *discharge*/*drag*, FVM i drugi u d04, „120 grit”, NPSH, FEM, RSS, CFL3D/SSTm, FUN3D, NASA TMR (U 2–3, S 3); hrvatski opis za *squat* (A 9).
2. K8, previše znamenaka: u14:779, 841, u15:449, 510, 572; u15:542 je opravdan zahtjevom reziduala (U 1, S 9).
3. Skice: preklapanja oznaka na sl. 14.3, 14.5, 14.7, 15.1 i 15.2 (na str. 292 potvrđeno $Q_d$ uz $y_1$); nedefinirana točka B i šrafura Z6 na sl. 14.4/14.7; luk $\theta$ odvojen od vodilice na sl. 14.2 (S 4, St).
4. Primjenska vjerodostojnost (A 1–7, 10–11): brzina vrtnje 1450 i 320 min⁻¹, $u/c_1$ izvedenih kola, $Fr_1=3{,}83$ (izračunano) u području oscilirajućeg skoka, $FM$ drona, $\chi$ jednovijčanog broda, omjer $v_j/v_s$. Rasponi „po sjećanju” su NEPOTVRDIVI bez izvora. $\rho_{zr}$ u P6: ISA na 1500 m daje 84,55 kPa i 1,058 kg/m³; zadano 1,045 kg/m³ odstupa −1,3 % (S 8, provjereno).
5. Nazivlje: „knjiga” umjesto „priručnik” (6×), lebdenje i vis, radijus i polumjer, jedinični protok (U 4, 6). Prijedlog „brodski vijak” i „poriv” (A 8) autorska je odluka; „propeler” je potvrđeni naziv (K7).
6. K10 i K11 manji: ponavljanja u14:21/74, u15:278/326, u14:5/191; Granica modela skoka ima 4 rečenice; dugi opisi slika u14:9 i u15:9 (U 7–8, S 6).
7. K2, K4 i oznake blokova: bezlični „treba” (u14:7, 165, 532; u15:17); naslovi-pretinci u d02 i d04; oznake „Kako čitati pragove” i „Aeroprofil nije …” bez obrasca „Vrsta — Podnaslov” (U 9–11, S 10).
8. Razine i studentske nejasnoće: pog. 15 P2 i P5 prema odluci su T1; P2 nosi naslov „na širokom preljevu” bez preljeva; $w_n$ nije objašnjen; „Zastani i promisli” ima odgovor već na str. 265; podatci o bateriji drona samo u provjeri; $\theta=150^\circ$ u ključu Z3 (S 5, St).
9. Upućivanja i struktura: „dodatak o numeričkoj …”, „pojmovniku”, „u poglavlju 9” u d05; „pog. 10 Količina …” četiri puta na dvije stranice; „Veza sa Z6 u pog. 12” u d04 rješava tuđi zadatak; numerički pokus pog. 15 stoji iza zadataka (U 5, 12–14, S 10).
10. Sadržaj za nastavak i literatura: $J$, $K_T$, $K_Q$ za propeler, razvrstavanje profila razine, redak „otpor broda” u d04 (S 11, A 10); novija izdanja White, Munson i Çengel (U 15). Sve su to autorske odluke.

## Pitanja autorici

- G4-01 i G4-20: zamjena Z2 i Z6 pog. 14 u sljedećem ciklusu revizije.
- G4-03: što je $y_{2,dop}$ (nizvodni vodostaj ili visina zidova)? O odgovoru ovise tekst, skica i bilježnica.
- G4-30: koji naziv Eulerove jednadžbe vrijedi u cijeloj knjizi.
- G4-35: vrijedi li K4 i za podebljane uvode CFD okvira (17 mjesta).
- G4-19: treba li pog. 15 jedan zadatak iz brodogradnje ili strojarstva unatoč lajtmotivu iz matrice.
