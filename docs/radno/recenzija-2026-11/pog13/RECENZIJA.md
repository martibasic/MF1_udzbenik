# Recenzija pog. 13 — Gubitci, cjevovodi, crpke i mreže (pilot skilla)

Datum: 8. 11. 2026. Stanje: grana `konvencije-recenzije`, commit `5ec5ff1`, PDF str. 245–262,
ključ str. 350–351. Ništa u knjizi nije mijenjano.

Čitanja (svako neovisno, bez konteksta pisanja i bez ranijih recenzija):
[struka.md](struka.md) (Opus), [struka_drugi_model.md](struka_drugi_model.md) (Sonnet),
[primjena.md](primjena.md), [student.md](student.md) (simulirano), [urednik.md](urednik.md);
glavni agent: [matrica_i_nacrt.md](matrica_i_nacrt.md).

Oznake: **P0** pogrešan ili opasan zaključak · **P1** bitna pogreška, ne predavati bez ispravka ·
**P2** vrijedi ispraviti · **P3** prijedlog. „Provjereno” znači da je glavni agent nalaz potvrdio
u izvoru, PDF-u ili računom; „dojam” je procjena čitatelja koju glavni agent nije mogao provjeriti.

## 1. Opća ocjena

Poglavlje je **fizikalno i brojčano ispravno**. Tri čitatelja i glavni agent neovisno su ponovno
izračunali sve rezultate P1–P6 i Z1–Z6: sve se slaže, uz jednu provjeru u P1 koja zbog
zaokruživanja daje 3,81 m umjesto 3,82 m. Simulirani student riješio je Z3 i Z6 točno. Nema
nalaza P0. Recenzenti posebno hvale izvod $\lambda=8\tau_{st}/(\rho v^2)$, P4 (afinitetni zakoni
uz statičku visinu), lanac snaga i Z6 kao primjernu T4 odluku iz brodske prakse.

Tri najvažnija nalaza:

1. **Središnji postupak poglavlja nema riješenog primjera.** Nijedan P ne računa turbulentni
   $\lambda$ iz $Re$ i $k_s/D$ niti radnu točku s $\lambda$ koji se mijenja s protokom; student to
   prvi put radi sam u Z4 i Z5. Colebrook i Swamee–Jain ne pojavljuju se ni u jednom drugom
   poglavlju.
2. **Nedefinirane i dvoznačne oznake** uz NPSH i mreže: $v_s$, $p_{aps,s}$, $h_{g,s}$, $R$,
   $H_{stat}$; indeks $s$ za sustav, usis i omjer brzina vrtnje; $H$, $\Delta z$ i $H_{stat}$ za
   istu razliku razina.
3. **Ponavljanje i opisna upućivanja:** uvod unaprijed izvodi formule odjeljaka; upozorenje da
   $NPSH_a$ nije dovoljan stoji na šest mjesta; „ranijem Venturijevu primjeru”, „sljedeće
   poglavlje”, „dotok iz pog. 7” bez broja.

Pilot je otkrio i četiri problema koji vrijede za **cijelu knjigu** (odjeljak 6).

## 2. P1

| # | Mjesto | Nalaz | Prijedlog | Izvor, status |
| --- | --- | --- | --- | --- |
| A1 | P1–P6 (`u13:375–672`); Z4, Z5 | Nijedan riješeni primjer ne pokazuje slijed $Re\to\lambda(Re,k_s/D)$ za turbulentni tok ni iterativnu radnu točku; P1, P3 i P6 zadaju $\lambda$, P2 je laminaran, P4 ima zadanu kvadratnu karakteristiku. Obvezna provjera ishoda iz kurikularne matrice („iterativna radna točka”) tako se prvi put pojavljuje u samostalnom Z4. | Najmanji zahvat: u P1 zadati $k_s$ i $\nu$ umjesto $\lambda$; $\lambda$ iz Swamee–Jaina, provjera Colebrookovim rezidualom. Broj primjera ostaje isti. Mijenja primjer, pa je **autoričina odluka** (izvan dogovorenog opsega Z1–Z6). | struka P1-1, glavni agent G6; provjereno |
| A2 | `u13:339–355`, (13.27)–(13.28) | $p_{aps,s}$, $v_s$ i $h_{g,s}$ nisu definirani; definirani su samo $p_v$ i $z_s$. Urednički stil izričito traži da se iznimka $v_s$ (inače brzina broda) uvede uz definiciju. | Iza (13.27): „gdje su $p_{aps,s}$ apsolutni tlak i $v_s$ srednja brzina u usisnom presjeku S (u ovom poglavlju $v_s$ nije brzina broda)…”; uz (13.28): „$h_{g,s}$ gubitak u usisnom vodu do presjeka S”. | urednik; provjereno |

## 3. P2

### Sadržaj i didaktika

| # | Mjesto | Nalaz | Prijedlog | Izvor, status |
| --- | --- | --- | --- | --- |
| B1 | P5 `u13:589` | Nakon čišćenja „visina dobave pada … uz isti protok”, a ne kaže se da pretvarač snizuje brzinu vrtnje. CFD odlomak r. 278 tvrdi suprotno za stalnu brzinu. | Jedna rečenica: „Pretvarač snizuje brzinu vrtnje tako da protok ostane 6,0 L/s; učinkovitosti pretpostavljamo nepromijenjenima.” | 4 čitatelja; provjereno |
| B2 | odjeljak 13.5 `u13:301`; P4 r. 569 | Skaliranje cijele krivulje $H_{p,2}(Q)=s^2H_p(Q/s)$ prvi se put pojavljuje u rješenju P4, bez objašnjenja; za Z6 je presudno. | Jedna rečenica u 13.5: točka $(Q,H)$ prelazi u $(sQ,\,s^2H)$. | student; provjereno |
| B3 | Z6 kontrolni rezultat `u13:885` | Ključ očekuje „uvlačenje zraka pri njihanju i trimu”, što poglavlje nigdje ne spominje (K15). | Spomenuti u Granici modela NPSH-a ili izostaviti iz kriterija. | student; provjereno |
| B4 | P3 „Traži se 1” `u13:484` | Početna raspodjela koja zadovoljava čvorove nije jednoznačna, pa student ne može usporediti iteracije s (13.38)–(13.40). | Zadati početnu raspodjelu ili tražiti konvergirani rezultat. | drugi model; provjereno |
| B5 | P1 `u13:409–415` | Ispisano $1000\cdot9{,}81\cdot3{,}82=37{,}4$ kPa (točno 37,47); provjera $37\,400/9810=3{,}81$ ne „vraća” 3,82 m i nije neovisna. | Neovisna provjera, npr. udio lokalnih gubitaka $4{,}6/13{,}0=0{,}354$ prema $1{,}35/3{,}82$. | struka, glavni agent; provjereno računom |
| B6 | Z2, Z4 | Razina Z2 (T1) i Z4 (T2) niža je od stvarne odluke (izbor korelacije prema režimu; sprega Colebrooka i krivulje crpke). | Prilagoditi zadatke, ne oznake; **autoričina odluka** o rasporedu 2×T1, 2×T2, T3, T4. | oba stručna; dojam |
| B7 | `u13:905`, Z1–Z6 | „Najčešća pogreška” (zbrajanje $\xi$ s različitim referentnim brzinama) i izravni problem paralelnih grana nigdje se ne uvježbavaju. | U Z1 uvesti drugi promjer ili nagli prijelaz; ili u Z3 dodati raspodjelu prije ventila. | struka; provjereno |
| B8 | „Dublje” `u13:48–62` | $\Phi=2\mu S_{ij}S_{ij}$ s osrednjenim poljem ne obuhvaća turbulentnu disipaciju. | „Za turbulentni tok $\Phi$ obuhvaća i turbulentnu disipaciju.” | drugi model; provjereno |
| B9 | `u13:89` | „redukcijskom ventilu” — u hrvatskom nazivlju ventil za sniženje tlaka, ne suženje. | „suženju (redukciji)”. | struka; provjereno |
| B10 | Z6 `u13:874` | „Odredi $NPSH_a$ s apsolutnim tlakom” čita se kao zahtjev za $p_{aps,s}$ bez zadanog promjera usisa. | „… prema (13.28), s apsolutnim referentnim tlakom”. | student; provjereno |

### Primjena

| # | Mjesto | Nalaz | Status |
| --- | --- | --- | --- |
| C1 | cijelo poglavlje | Od 6 P i 6 Z brodski je samo Z6, a uvod obećava i brodske rashladne, grijanje i protupožarne sustave. Kurikularna matrica za ovaj red traži „hlađenje i urbana mreža”; ravnoteža struka je **autoričina odluka** (npr. P3 kao brodski protupožarni prsten). | provjereno |
| C2 | P5 | $\eta_p=0{,}78$ i $\eta_m=0{,}92$ previsoki su za agregat od ~1 kW; recenzent procjenjuje ukupno 0,50–0,58. | dojam (izvori po sjećanju) |
| C3 | P6 | Brzina na usisu 2,8 m/s velika je i nije komentirana; upravo daje $h_{g,s}=1{,}45$ m. | provjereno računom; raspon „1–2 m/s” dojam |
| C4 | Z6 tekst i skica | Uronjenost 1,8 i 0,4 m odgovara samo malom brodu; stalna statička visina 4 m pri punjenju tanka nije ograđena; na skici usis prolazi kroz oplatu bez ventila na oplati. | skica provjerena; rasponi dojam |
| C5 | `u13:357`, Z6 | $NPSH_r$ bez standardne definicije (pad visine dobave 3 %, NPSH3) i bez reda veličine margine. | dojam; norme treba provjeriti u izvoru |

### Oznake, izvori, upućivanja, jezik

| # | Mjesto | Nalaz | Status |
| --- | --- | --- | --- |
| D1 | `u13:223`, `:292`, `:9` | $R$ i $H_{stat}$ bez definicije; ista razlika razina kao $H$, $\Delta z$, $H_{stat}$ (K5, K6). | provjereno |
| D2 | Z6, P4, NPSH | Indeks $s$: sustav ($H_s$), usis ($z_s$, $h_{g,s}$), omjer $s=n_2/n_1$ i $E_s$ u istom zadatku (K6); $R_v$ prema $h_{g,V}$. | provjereno |
| D3 | sl. 13.2 (`u10_fig_uvod_pregled.svg`) | Ventil iznad cijevi, oznaka „2” nije na izlaznom presjeku, radna oznaka „ventil (simbol)” (K13). | provjereno na PDF-u i SVG-u |
| D4 | `u13:185–192`, `:244` | Swamee–Jain, Blasius, Hardy–Cross i tvrdnja „odstupa oko 1 %” bez izvora; nedostaje raspon $k_s/D$ (K14). | provjereno; točni izvori tek trebaju provjeru |
| D5 | `u13:115`, `:276`, `:370`, `:265` | Opisna upućivanja bez broja: Venturijev primjer (pog. 8), „dotok iz pog. 7”, „sljedeće poglavlje”, „nastavci” (K12). | provjereno |
| D6 | uvod `u13:3`, `:5`, `:13`; NPSH `:357–370`, `:671` | Uvod unaprijed iznosi formule i pravila odjeljaka; r. 3 i Sažetak r. 899 doslovno isti; upozorenje o $NPSH_a$ šest puta (K10). Uvod ~200 riječi manje. | provjereno |
| D7 | Sažetak `u13:898`, `:903` | „prijelazno područje … nije pouzdano” (nepouzdana je korelacija); „ni $NPSH_a>0$ ni … model ne opisuju … vodeni udar” spaja nespojivo. | provjereno |
| D8 | `u13:515`, `:854`, `:868` | Brojevi odvojeni zarezom ili kosom crtom ($0{,}0238/0{,}0228$) čitaju se dvoznačno (K8); r. 868 spaja samostalne tvrdnje zarezom (K3). | provjereno |
| D9 | `u13:67` | Zadnja rečenica tumačenja skice potvrđuje ispravnost crteža („koljeno … bez pregrade”), što je trag izrade (K1). | provjereno |
| D10 | više mjesta | Naziv Darcy–Weisbachove jednadžbe koleba (zapis, korelacija, formula, model); „mreža” za cjevovod i za mrežu ćelija; „brzina” umjesto „brzina vrtnje”. | provjereno |

## 4. P3

Oko 50 prijedloga u pojedinačnim izvještajima, ukratko: kratice RANS i NPSH pri prvom spomenu;
naslovi panela skice 13.4 ≠ naslovi zadataka i uputa „računaj” na panelu Z5; „lijevano
željezo” uz $\lambda=0{,}022$; naputak Z2 odgovara na drugi dio zadatka; $Re_B=4775$ blizu praga;
tablica tipičnih $\xi$ i $k_s$; hidraulički promjer; crpke u seriji i paraleli (ne obrađuje ni
pog. 14, provjereno pretraživanjem); oblik „jest”; prvo lice u izvodu; naslov okvira kao pitanje
(„Što se izjednačuje?”). Mjesta su u [urednik.md](urednik.md), [struka.md](struka.md) i
[primjena.md](primjena.md).

## 5. Odbačeno ili izmijenjeno pri provjeri

| Tvrdnja čitatelja | Provjera | Odluka |
| --- | --- | --- |
| „nastavci obrađuju Z3 i Z6” je pogrešno upućivanje; treba „Z3 i Z5” (drugi model, student, struka) | Bilježnica `u13_paralelne_grane` ima odjeljke „4. Z3” i „5. Z6: balastna crpka”. Upućivanje je točno; nejasna je samo riječ „nastavci”. | spušteno na P3, preformulirati (D5) |
| „usisni koš u oplati” je kriv naziv (primjena P2-5) | Autoričin potvrđeni naziv u uredničkom stilu: „usisni koš (engl. *sea chest*)”. | nije nalaz; recenzentova primjedba (u praksi koš = *rose box*, sanduk = *sea chest*) prosljeđuje se autorici na znanje |
| „učinkovitost” umjesto „stupanj djelovanja” (primjena P2-10) | Naziv se rabi kroz cijelu knjigu. | pitanje nazivlja za cijelu knjigu, autoričina odluka |
| „Poglavlje nema okvira Provjeri sebe” (student) | Točno, ali posljedica je svjesne odluke od 27. 9. 2026. (`SelfCheck`, `visibility: []`). | premješteno u odjeljak 6 |

## 6. Nalazi koji vrijede za cijelu knjigu

| # | Nalaz | Uzrok | Težina |
| --- | --- | --- | --- |
| K-1 | U ključu (dodatak F) na 10 mjesta (pog. 9: 2, pog. 10: 3, pog. 13: 2, pog. 15: 3) stoji „prema jednadžbi odgovarajući izraz” umjesto broja jednadžbe. CHANGELOG 17. 10. bilježi ovo kao ispravljeno (S12). | `scripts/generate_exercise_key.py:76` upisuje tekst poveznice „odgovarajući izraz”. | P1 |
| K-2 | Upućivanja na primjere ispisuju se kao „primjer 13.3”, a primjeri su označeni P1–P6; (13.3) je ujedno broj jednadžbe. | `filters/mf1-components.lua:146` koristi globalni broj objekta. | P2 |
| K-3 | „Provjeri sebe” (oko 4 pitanja s odgovorima po poglavlju) skriven je u webu i PDF-u; vidljivo je samo izdvojeno „Zastani i promisli”. Urednički stil i CHANGELOG opisuju „Provjeri sebe” kao vidljiv dio poglavlja. | `components/registry.json`: `SelfCheck.visibility = []` (odluka 27. 9.). | autoričina odluka |
| K-4 | Ključ za pog. N nosi broj F.(N+1) jer je F.1 uvod („F.14 Gubitci…”). | struktura dodatka F | P3 |
| K-5 | Bilježnica Moodyjeva dijagrama u pog. 13 zove se `u10_moody_dijagram`, vidljivo u tiskanom URL-u i QR-u. | naslijeđeni naziv | P3 |

## 7. Što je dobro i treba ostati

- Izvod $\lambda=8\tau_{st}/(\rho v^2)$ iz ravnoteže sila i objašnjenje zašto je laminarni $\Delta p$ linearan u $Q$.
- P4: omjer brzina vrtnje 0,899 prema omjeru protoka 0,865 kao dokaz da se afinitetni zakoni ne prenose na sustav sa statičkom visinom.
- Lanac snaga $P_{el}\to P_{vr}\to P_h$ i upozorenje o disipaciji na ventilu.
- P6 s dva neovisna zapisa $NPSH_a$ koji se slažu; jasna konvencija predznaka $z_s$.
- Z4 traži i energijski i Colebrookov rezidual; Z5 sa starenjem cijevi (rezerva 1 m); Z6 traži popis podataka koji nedostaju.
- CFD odlomci odvajaju 1D mrežni model od lokalnog CFD-a i ne iznose neprovedene rezultate.

## 8. Redoslijed provedbe (nakon autoričine odluke)

| Korak | Stavke | Rizik |
| --- | --- | --- |
| 1 | A2, D1, D2 (bez promjene oznaka u ključu), D5, D7, D8, D9, D10, B9, B10 — jezični i oznakovni ispravci teksta | nizak; `--usporedi` i puni lanac provjera |
| 2 | B1, B2, B3, B4, B5, B8 — rečenice u primjerima i teoriji, bez novih brojeva | nizak |
| 3 | D3 i C4 (skica): ventil u cijev, oznaka 2, „(simbol)”; ventil na oplati u Z6 | srednji; SVG, tiskovne izvedenice, audit skica |
| 4 | D4, C5 — izvori u dodatku E, nakon provjere u izvornicima | srednji; bez izmišljenih navoda |
| 5 | D6 — skraćivanje uvoda i ponovljenih upozorenja | nizak, ali briše tekst: autorica odobrava |
| 6 | A1, B6, B7, C1, C2 — promjena primjera ili zadataka | srednji; verifikator, D06, skice; autoričina odluka |
| 7 | K-1, K-2 — generator ključa i filtar upućivanja (cijela knjiga) | srednji; obnova D06, render, auditi |

## 9. Odluke koje su autoričine

1. Preraditi li P1 (ili P6) tako da računa turbulentni $\lambda$ (A1) — proširenje opsega izvan Z1–Z6.
2. Razine Z2 i Z4 (B6) i ravnoteža struka u poglavlju (C1).
3. Brojevi u P5 i P6 (C2, C3): zadržati kao nastavne ili uskladiti s praksom.
4. Vidljivost „Provjeri sebe” u cijeloj knjizi (K-3).
5. Nazivlje: „učinkovitost” ili „stupanj djelovanja”; napomena primjenskog recenzenta o „usisnom košu”.
6. Indeks za usis ($s$) i ventil ($R_v$) — zahvaća ključ i verifikator.

## 10. Ocjena pilota (za doradu skilla)

| Čitanje | Nalaza | Jedinstveno korisno | Netočno |
| --- | --- | --- | --- |
| struka (Opus) | 23 | A1, B6, B7, B9, D3 | 0 |
| struka, drugi model (Sonnet) | 14 | B4, B8 | 1 („Z3 i Z5”) |
| primjena | 22 | C1–C5 | 0 (1 nazivlje protivno autorskom standardu) |
| student | ~12 | B2, B3, B10, K-1, K-2, K-3 | 0 (1 dvoznačno shvaćeno upućivanje) |
| urednik | 65 | A2, D1, D2, D7, D8, D10 | 0, ali previše P3 za trijažu |

Zaključci:

- **Brojeve su svi potvrdili**; drugo stručno čitanje vrijedi za teže skupine poglavlja, ne za sve.
- **Student je najisplativiji**: otkrio je tri problema na razini knjige koje stručnjaci nisu vidjeli.
- **Urednik daje previše P3** (43). Za cijelu knjigu to je oko 1000 stavki; uputa treba ograničiti P3 na sažetak.
- **Čitatelji nisu otvarali bilježnice**, pa su dva neovisno pogriješila oko „Z3 i Z6”. Neovisnost dvaju čitatelja nije dokaz.
- **Alat je propustio** popise s kosom crtom u formulama, opisna upućivanja („sljedeće poglavlje”, „ranijem … primjeru”) i kratice prije definicije; dvije od tih provjera mogu se dodati.
- Provjera nalaza u ovom opsegu (≈130 stavki) traje koliko i samo čitanje; za 15 poglavlja treba je razdijeliti.

## 11. Provedba (8. 11. 2026., grana `konvencije-recenzije`)

Provedeno na autoričin zahtjev („provedi nađene ispravke”):

| Nalaz | Što je učinjeno |
| --- | --- |
| A1 | P1 sada zadaje $\nu$ i $k_s=0{,}26$ mm (lijevano željezo, Moody); računa $Re=2{,}88\cdot10^5$, $\lambda=0{,}02467$ (Swamee–Jain), provjera Colebrookom (0,02452, 0,6 %) i udjelom lokalnih gubitaka; razina T1 → T2; verifikator proširen. |
| A2, D1 | Definirani $p_{aps,s}$, $v_s$, $h_{g,s}$, hidraulički otpor $R$ i $H_{stat}=\Delta z$; kota na slici 13.1 je $\Delta z$. |
| B1–B5, B8–B10 | Mehanizam istog protoka u P5; skaliranje krivulje $H_{p,2}(Q)=s^2H_p(Q/s)$ u 13.5; uvlačenje zraka u granici modela NPSH; P3 sa zadanom početnom raspodjelom i energijskim visinama; neovisna provjera P1; turbulentna disipacija u bloku „Dublje”; „suženju presjeka”; Z6.3 s upućivanjem na (13.28). |
| B7 (dio) | Z3 sada počinje izravnim problemom (raspodjela bez ventila: 13,33 i 6,67 L/s, 2,13 m); ključ i verifikator usklađeni. |
| C3, C4, C5 | P6: temperatura uz $p_v$ i komentar brzine na usisu; Z6: manji obalni brod, srednja statička visina, „najmanji gaz tijekom balastiranja”, zaporni ventil iza oplate na skici; $NPSH_3$ uz izvor ISO 9906. |
| D2 | $R_V$ i $E_n$; $s$ ostaje omjer brzina vrtnje uz izričitu definiciju. |
| D3 | „ventil (simbol)” → „ventil” uz simbol. Ventil ostaje izdvojeni simbol, kako je namjerno crtano (opis skice: „ne krutom preprekom u fluidu”). **Otvoreno:** u tiskovnoj izvedenici generator i dalje smješta oznaku „2” pod sredinu cijevi; na webu je na izlazu. |
| D4 | Izvori Swamee i Jain (1976), Cross (1936), ISO 9906:2012 u literaturi; Blasius uz Schlichtinga; raspon $k_s/D$ za Swamee–Jaina. `audit_pdf_layout.py` broj zapisa čita iz `references.bib`. |
| D5–D10 | Upućivanja brojem poglavlja; uklonjeni ponovljeni odlomci uvoda i rečenica o $NPSH_a$ u CFD odlomku; sažetak r. 898 i 903; popisi s točkom-zarezom; uklonjena rečenica o ispravnosti skice; ujednačen naziv Darcy–Weisbachove jednadžbe, „mreža ćelija”, „brzina vrtnje”. |
| K-1 | Generator ključa upisuje broj jednadžbe, npr. „(13.16)”; nepoznat ID je pogreška. |
| K-2 | Upućivanje na primjer ili zadatak ispisuje „primjer P3”, a za drugo poglavlje „primjer P5 iz pog. 8”. |
| P3 | Z5 skica bez upute „računaj”; naputak Z2 više ne odgovara na drugi dio; naslov okvira „Jednak pad energije paralelnih grana”; puni naziv NPSH. |

Nije provedeno (autoričina odluka ili nepotvrđen podatak): B6 (razine Z2, Z4), C1 (ravnoteža struka), C2 (stupnjevi djelovanja u P5 — rasponi samo po sjećanju), K-3 (vidljivost „Provjeri sebe”), nazivlje „učinkovitost” / „stupanj djelovanja” i „usisni koš”, dio B7 (zbrajanje $\xi$ s različitim brzinama), P3 „lijevano željezo” u P3.
