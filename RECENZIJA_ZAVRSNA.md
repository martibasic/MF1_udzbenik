# Završna recenzija priručnika „Mehanika fluida: modeli, problemi i rješenja”

Datum: 16. listopada 2026. Stanje: grana `popravak-skica`, commit `2fff6c5` (nakon pregleda skica
i cjelovite lekture). Izgrađeni PDF: 335 stranica; web: 24 stranice.

Cilj recenzije, prema zahtjevu autorice: **ne dodavati novi sadržaj, nego postojeći dovesti do
završnog stanja** — točnijeg, dosljednijeg, čitljivijeg i suvremenijeg, uz uklanjanje onoga što je
suvišno. Recenzija je provedena u osam područja, neovisno i bez izmjena u repozitoriju; potpuni
izvještaji su u `docs/radno/recenzija-2026-10/`. Ovaj dokument objedinjuje nalaze, uklanja
ponavljanja među područjima i daje redoslijed provedbe.

Oznake: **P1** ispraviti prije završetka · **P2** vrijedi napraviti · **P3** opcionalno.
Sve što je navedeno kao „provjereno” izmjereno je skriptom ili viđeno na renderu; procjene su
označene kao dojam.

---

## 1. Opća ocjena

Priručnik je **sadržajno spreman za završetak**. Tri sadržajna recenzenta ponovno su izračunala
**sve** brojčane rezultate svih 90 riješenih primjera i 90 kontrolnih rezultata (ne samo polovinu) i
prošla sve izvode korak po korak: nije nađena nijedna nova brojčana ni fizikalna pogreška. Odstupaju
samo četiri već poznata mjesta zaokruživanja i jedna krivo napisana rečenica (pog. 5, Z2). Svi
CFD blokovi ocijenjeni su kao uvjerljivi, točni i nepretenciozni; blokovi „Granica modela” i zadatci
T4 ocijenjeni su kao najjači dio knjige. Tvrdnje o brodograđevnoj i strojarskoj praksi su točne, uz
jednu iznimku (visina gondole spar-turbine).

Jezik je nakon lekture čist: automatska pretraga cijelog PDF-a ne nalazi ostatke Markdowna, ravne
navodnike, kalkove, stare oblike (zadaci, podaci, pumpa) ni kriva upućivanja. Ton uvoda i sažetaka je
akademski i pitak.

Ono što priručnik još dijeli od završne inačice nisu greške u sadržaju, nego tri skupine stvari:

1. **Jedan tipografski kvar u PDF-u koji se vidi na gotovo svakoj stranici**: decimalni zarez u
   formulama slaže se s razmakom („9, 81 m/s²”, „1, 20 m”; oko 3000 mjesta na 210 stranica).
   Web je ispravan. Rješava se jednim pravilom u Typst filtru. Tri su ga recenzenta neovisno
   stavila na prvo mjesto.
2. **Ponavljanje**, nastalo dobrim dijelom dodavanjem uvodnih tekstova 15. listopada: okvir
   „Inženjerski kontekst” sada u svih 15 poglavlja ponavlja uvod, uvodni dio knjige tri puta kaže
   komu je namijenjena, pog. 8 izvodi Bernoullijevu jednadžbu tri puta, pog. 10 radni zapis četiri
   puta, a desetak parova primjer–zadatak isti je problem s drugim brojevima. Procjena: oko 400–500
   redaka izvora (otprilike 10 stranica PDF-a) može otići bez gubitka ijednog ishoda.
3. **Nedosljednost istog elementa među poglavljima**: sažetak u tri oblika, samoprovjera s dva
   naziva, odjeljak zadataka s dva naziva, blok uz bilježnice s tri naziva i dva para tipki, dva
   tipografska „dijalekta” skica (pog. 3–7 prema 8–14), obrnute boje naputka i rezultata u pog. 13.

Ništa od toga ne traži novi sadržaj. Nakon provedbe P1 i većine P2 stavki knjiga će biti kraća,
ujednačenija i spremna za postupak odobravanja.

---

## 2. P1 — ispraviti prije završetka

### 2.1 Sadržaj (točnost)

| # | Gdje | Što | Prijedlog |
|---|---|---|---|
| S1 | pog. 5, Z2 kontrolni rezultat (`u05` r. 745) | „$F_x$ i $F_z$ ne poništavaju momente ni oko jedne točke” — fizikalno netočno (poništavaju se oko svake točke na pravcu rezultante). | „Za razliku od kružnog luka, normale parabole nemaju zajedničku točku, pa ne postoji unaprijed poznata točka s nultim momentom; $M_A$ zato treba računati iz obiju komponenata i njihovih krakova.” |
| S2 | pog. 12, primjer trupa modela (`u12` r. 328) | $(1{,}08\cdot10^7)^{1/5}=25{,}2$ — točno je 25,5; $\delta\approx0{,}087$ m, ne 0,088. | Ispraviti broj; provjeriti verifikator i obnoviti D06. |
| S3 | pog. 6, P6 spar (`u06` r. 842) | „Gondola i rotor nalaze se oko 100 m iznad kobilice” — $H=100$ m je vrh plovne osnove; gondola je ~80–100 m iznad mora. | „Gondola i rotor nalaze se visoko iznad vrha plovne osnove (reda 100 m iznad mora)…”; račun se ne mijenja. |
| S4 | pog. 8, CFD blok (`u08` r. 81) | „Mjerač iz pog. 3” — Venturijeva cijev u pog. 3 ne postoji (prvi put je u pog. 7 i u interaktivu pog. 8). | Uputiti na interaktivni prikaz na početku poglavlja / CFD tablicu u pog. 7. |
| S5 | pog. 15, ustava (`u15` r. 176–189) | Isti simbol $y_1$ za uzvodnu dubinu i za suženi mlaz u pet redaka; $C_c$ nedefiniran. | Uzvodna dubina $y_0$ (kao na uvodnoj slici), $y_1$ ostaje suženi mlaz; dodati „($C_c$ koeficijent kontrakcije)”. |
| S6 | pog. 14 (`u14` r. 133, 142) | „Isti izraz” briše razliku $\dot m_{rel}$ prema $\dot m$ (poanta poglavlja); „nekonvergirana mreža” (konvergira rješenje; razlika je i fizikalna: trenje diska, procjepi). | Formulacije iz izvještaja `sadrzaj_u11_u15.md`, nalazi 3 i 4. |
| S7 | pog. 13, Z2 naputak (`u13` r. 776) | „razlikuju se samo $Re$” — razlikuju se i gustoće (1080 prema 998), a $\Delta p\propto\rho$. | „…razlikuju se $Re$ (dakle režim i $\lambda$) i gustoća.” |
| S8 | pog. 11 (`u11` r. 306) | Iza omjera **snaga** $\lambda_L^{7/2}$ stoji „a ne faktorom $\lambda_L^3$” (to je faktor sile). | „…ne skalira ni faktorom $\lambda_L^3$ (sila) ni $\lambda_L^{7/2}$ (snaga).” |
| S9 | zaokruživanja: pog. 6 P5 (3,477 / 0,225 m, verifikator `verify_u07.py` r. 528–529), pog. 10 P5 (439 / 912 N / rezerva 88 N), pog. 10 P7 (12,45 N m), pog. 14 P6 (5,87 N iz zaokruženih faktora) | Tekst miješa zaokružene i nezaokružene međurezultate; student koji ponavlja račun dobije drugu zadnju znamenku. | Odabrati jednu razinu po primjeru; uskladiti verifikator i D06. |
| S10 | pog. 5, izvod (`u05` r. 83); pog. 2 (`u02` r. 321) | Granični slučaj $h_a=h_b$ daje pojas površine nula; $\Delta p=\sigma/R$ s neuvedenim $R$. | Granični slučaj $h_a=0$; $\sigma/R_1$. |
| S11 | D01 r. 40 | Jedinice za $k$, $\varepsilon$, $\omega$, $\ell$ označene „-”. | m²/s², m²/s³, s⁻¹, m. |
| S12 | D06 (8 mjesta, PDF str. 327–335); uzrok `scripts/generate_exercise_key.py:76` | U ključu stoji rezervni tekst „iz jednadžbe [odgovarajući izraz]”. | Generator neka ispisuje `[-@eq-id]`; obnoviti D06. |

### 2.2 PDF (tipografija i prijelom)

| # | Gdje | Što | Prijedlog |
|---|---|---|---|
| T1 | cijeli PDF (≈3000 mjesta, 210 str.) | Decimalni zarez u matematici s razmakom: „9, 81”, „0, 0700 kg/s”, „κ = 1, 4”. Izvor (`9{,}81`) i web su ispravni; gubi se u Pandoc → Typst. Srodno: „m³/ s”, „m³/ h” (razmak iza kose crte u jedinicama). | U Typst filtru (`filters/mf1-typst-author-blocks.lua`, koji već uklanja `\!`) pretvoriti `{,}` u literalni zarez bez razmaka i ukloniti razmak oko `/` unutar `\mathrm{}`. Provjeriti na str. 20, 48, 103, 155, 168, 327. |
| T2 | 83 stranice, 203 mjesta | Istaknute jednadžbe završavaju „… = 179 kPa .” (razmak pa točka), negdje bez razmaka. | Dosljedno: točka unutar formule uz jedinicu ili je izostaviti u istaknutim jednadžbama. |
| T3 | str. 52–84, 146–158, 184–191, 321 | Oznake točaka A, B, P, HGL/EGL i brojevi grana slažu se u kodnom fontu (backtick u izvoru pog. 3, 4, 8, 10). | U izvoru kao matematičke oznake $A$, $B$; HGL/EGL kao običan tekst. Kodni font samo za datoteke i naredbe. |
| T4 | str. 9, 27, 85, 124, 235, 286, 316 | Sedam gotovo praznih stranica (3–6 redaka); str. 286 „Dodaci” samo naslov. | Stisnuti razmake oko završnih okvira, dopustiti sažetak na stranici sa skicama; razdjelnici dodati mini-sadržaj ili je ukloniti. |
| T5 | 20-ak stranica (20, 23, 55, 61, 105, 173, 215, 283, 305…) | Naslovi „Traži se”, „Rješenje”, naslov poglavlja u dodatku C na dnu stranice bez teksta ispod (siročad). | Typst `sticky: true`/`breakable: false` za naslov + prvi element. |
| T6 | str. 1–6 | Naslovnica samo tekst bez godine, ustanove i grafike; sadržaj na poleđini naslovnice; impresum tek na str. 6 s „radno izdanje”, „ISBN u pripremi”, „rujan 2026.” i poveznicama bez URL-a. | Naslovnica s godinom, ustanovom i jednim vizualnim elementom (npr. skica 1.1 u jednoj boji); poleđina = impresum; sadržaj od str. 3; URL-ovi ispisani ili uklonjeni; status i datum konačni. |
| T7 | str. 36, 55, 101, 177, 282 | Kolizije i prelomi oznaka u skicama (npr. „Rst→f,x/y” preklopljeni na 10.1; „m³/s.” sam u retku na 15.2; „A = 0,18 / m²” na 2.3). | Pomaknuti oznake u pet SVG-ova; jedinicu vezati nelomljivim razmakom. |
| T8 | sve tiskovne izvedenice (`assets/pdf-figures/`), npr. str. 26, 139, 282 | Indeksi u skicama 9 pt uz osnovno slovo 9,5 pt, pa se $F_L$, $A_L$, $s_L$, $d_p$, $m_{pok}$ čitaju kao dvoslovne oznake „FL”, „AL”, „dp”. | Svjesno odstupiti od pravila „najmanje 9 pt i za indekse”: indeks ~70 % osnovnog slova (6,5–7 pt). Zahvat u tokenu, `tools/build_print_figures.mjs`, auditu i `docs/ispis-skica.md`; obnoviti izvedenice. |

### 2.3 Web

| # | Gdje | Što | Prijedlog |
|---|---|---|---|
| W1 | sva poglavlja na 390 px (izmjereno: pog. 6 — 70 jednadžbi, pog. 10 — 73, pog. 14 — 54…) | Numerirane jednadžbe šire od zaslona odrezane su s desne strane bez ikakvog znaka da se mogu pomicati; broj jednadžbe nestaje. | MathJax `displayOverflow: 'linebreak'` ili na ≤ 768 px sakriti broj i smanjiti font formula; dodati gradijent kao znak pomicanja; najduže `A ⟹ B` jednadžbe podijeliti u dva retka. |
| W2 | pog. 13 (`u13` r. 746, 752, …, šest parova) | „Smjernica” i „Kontrolni rezultat” imaju **zamijenjene boje** (tip/zelena ↔ note/plava) u odnosu na svih 14 ostalih poglavlja. | Zamijeniti `.callout-tip` ↔ `.callout-note` na šest mjesta. |
| W3 | `content/book.json:372` | Početna stranica ispisuje doslovno „Numerika i CFD V&amp;V”. | Upisati `V&V` (ili ispraviti escapiranje u generatoru). |
| W4 | `_language.yml:55`; naslovi dodataka | „dodatak A — Sažetak formula…” malim slovom kao H1 (i u PDF-u). | Naslov dodatka „Dodatak A — …” (u generatoru omotača ili CSS `::first-letter`). |
| W5 | `styles/components.css` `.mf1-ch-ref {display:inline-flex}` (95 mjesta) | Upućivanje „pog. 3 Naslov” je atomaran okvir: pada u zaseban redak, interpunkcija ostaje odvojena od riječi. | `display:inline; padding:0`. |
| W6 | kompozitne skice Z1–Z6 i uvodni pregledi na webu | Na stupcu od 750 px efektivne oznake 7–9 px, na mobitelu ~3 px. Po-panelni tiskovni redci već postoje u DOM-u (`mf1-print-layout`), ali su skriveni na zaslonu. | Na ≤ ~720 px prikazati postojeće tiskovne retke naslagane okomito; na širokom zaslonu zadržati ploču. Nije novi sadržaj. |

### 2.4 Struktura i dosljednost (vidljivo u sadržaju knjige)

| # | Gdje | Što | Prijedlog |
|---|---|---|---|
| D1 | svih 15 poglavlja | **Sažetak u tri oblika**: numerirani prozni odjeljak (pog. 1–4), okvir s natuknicama (6–12, 14, 15; s tri podvarijante), oboje s dvostrukim naslovom „Sažetak / Sažetak” (5, 13). U sadržaju PDF-a sažetak ima 6 od 15 poglavlja. | **Jedan oblik za sve:** završni okvir **Sažetak** s 5–7 natuknica + **Najčešća pogreška** (1 rečenica) + **Nakon ovoga poglavlja mora biti moguće** (3–4 stavke); prozne sažetke pog. 1–5 i 13 prepisati u natuknice (sadržaj već postoji). Odluka o numeriranom odjeljku (ulazi u TOC) ili samo okviru — autoričina; preporuka: odjeljak `## Sažetak` koji sadrži okvir bez vlastite labele. |
| D2 | početak knjige (`index.md` r. 5–9, 26–36; `u00` r. 50–56) | „O priručniku” i publika rečeni tri puta (PDF str. 6 i 7, dvaput u sadržaju); ista rečenica o primjerima iz drugih struka dvaput na istoj stranici; „Numerički pokusi” u index i u00; „CFD put” na četiri mjesta. | `index.md`: hero, katalog, impresum; `u00`: jedino „O priručniku”, „Predznanje”, „Numerički pokusi i izdanja”. Typst-only odlomak ukloniti. |
| D3 | `book.json`, `u05` r. 13, 170, 892, `d02`, `d04`, D06; 18 zaglavlja PDF-a | Naslov pog. 5 „Hidrostatske sile…” prema nazivlju „hidrostatički” (81 pojava u knjizi). | „Hidrostatičke sile na ravne i zakrivljene plohe”; ID i slug ne mijenjati. |
| D4 | `u15` (10×), D01, D06 | „podkritični / nadkritični” prema pravopisnom „potkritični / natkritični”. | Odlučiti za cijelu knjigu; ako ostaje strukovni oblik, zapisati kao svjesnu iznimku u urednički stil. |

---

## 3. P2 — vrijedi napraviti

### 3.1 Ukloniti ponavljanja (najveći dobitak uz najmanji rizik)

| # | Gdje | Što | Prijedlog |
|---|---|---|---|
| R1 | okvir „Inženjerski kontekst” u svih 15 poglavlja + prvi H2 koji sadrži samo taj okvir i „Procijenjeno vrijeme” (pog. 2–15; prvi odjeljak nosi isti naslov kao poglavlje: „6. Uzgon…” → „6.1 Uzgon…”) | Nakon dodavanja uvoda 15. 10. okvir gotovo doslovno ponavlja uvod (npr. `u08` r. 5 ↔ 15 ↔ 20 triput nabraja Venturi–Pitot–mlaz–sifon). Udvostručen naslov u sadržaju i numeracija odjeljaka pomaknuta za jedan bez razloga. | Ukloniti okvir (ili ga svesti na jednu rečenicu koja donosi novo), „Procijenjeno vrijeme” staviti izravno pod naslov poglavlja, ukloniti razinu „X.1” — kao što pog. 1 već ima. Isto za prvi H2 u dodatcima A–F (npr. „B. Pojmovnik / B.1 Pojmovnik”). Oko 15 × 6 redaka + 20 naslova. |
| R2 | pog. 8 r. 171–223 | Treći potpuni izvod Bernoullijeve jednadžbe (isti diferencijal kao prva dva). | Zadržati samo završni odlomak (interpretacija rad/energija) kao kratko „Fizikalno značenje”. ~50 redaka. |
| R3 | pog. 10 r. 139–157, 56–63 + 112–119 | Callout „Postupak rješenja” ponavlja $\sum\vec F=\dot m\Delta\vec v$ četvrti put (i jedini je generički callout u knjizi uz pog. 11); dva CFD bloka o istom koljenu. | Obrisati callout (rečenicu o predznaku normale prebaciti u r. 65); spojiti CFD blokove. ~25 redaka. |
| R4 | pog. 7 r. 161–163, 181–188, 348–350 | $A_1v_1=A_2v_2$ četiri puta; tablica s jednim retkom. | Zadržati uvod, granicu modela i izvod; obrisati ostalo. ~20 redaka. |
| R5 | pog. 3 r. 25–94, 171–173; pog. 4 r. 95–159 | $p=p_{pov}+\rho gh$ numeriran četiri puta (Temelj, dva okvira „Fizikalno značenje”, H2 „Matematički izvod”, r. 173); u pog. 4 Coriolisov okvir prije nego je rotacija uvedena, okvir-u-okviru koji ponavlja r. 153. | Spojiti u jedan odjeljak s izvodom u okviru; Coriolis iza paraboloida ili u „Granica modela”; ukloniti drugi ugniježđeni okvir. |
| R6 | pog. 1 r. 151–157, 381–391; pog. 11 r. 46–49, 318–378; pog. 14 r. 5/174/211 i r. 294; pog. 13 r. 77, 233–234; pog. 2 r. 243; pog. 5 r. 36; pog. 6 r. 304 | Pojedinačna ponavljanja: $A_1s_1=A_2s_2$ šest puta u pog. 1; drugi mini-primjer unutar „Provjere” P3; treći popis bezdimenzijskih brojeva u pog. 11 i dijagram odluke + mreža odluke s istim pitanjima; doslovno ponovljene rečenice u pog. 14; definicije $h_l$, $h_{loc}$ dvaput u pog. 13; druga rečenica o We/Bo; visjeća rečenica o $f(\varphi)$. | Kako je navedeno u izvještajima po poglavljima (sve su rečenice-kandidati citirane s retcima). |
| R7 | dodatak C r. 292–348; dodatak D r. 26–40 i 175–179; dodatak A (7 redaka) | Četiri završna bloka C ponavljaju uvod; pojmovnik kratica u D udvostručuje B; A sadrži sedam redaka koji su rješenja konkretnih zadataka (pog. 1 Z2, 2 Z6, 3 Z4, 4 Z5/Z6, 5 Z2, 6 Z6) i time odaju postupak; 10-znamenkasti brojevi u D. | C: zadržati najviše „Kriteriji provjere”; D: kratice samo one kojih nema u B; A: ukloniti sedam redaka; brojeve zaokružiti na 4 značajne. |
| R8 | „Napomene uz skice” (8 odlomaka 97–124 riječi; medijan knjige 26) | Trećina ponavlja SVG `<desc>`, trećina podatke zadatka, a opće konvencije („nisu u mjerilu”, „kote”) ponavljaju legendu iz pog. 0. | Skratiti na ≤ 60 riječi: samo ono što skica ne može reći. Primjer prije → poslije za pog. 3 (62 → 27 riječi) u `skice_i_interaktivno.md`, nalaz 12. ~1 stranica PDF-a. |
| R9 | slike: 11.1-lijevo (prazne trake), 11.3 (tekstni dijagram koji tekst ispod ponavlja), 11.2-lijevo (tablica kao slika), 7.2 (dvije krivulje na praznom platnu), `u11_fig_uvod_pregled` i lijevi panel `u12_fig_uvod_pregled` (ponavljaju P-skice); 27 skica s naslovom koji ponavlja potpis; proza u 6 SVG-ova | Slike koje ne nose informaciju ili ponavljaju motiv unutar 10 stranica; dvostruki naslovi. | Ukloniti/pretvoriti u tablicu kako je navedeno; naslove u jednoprizornim skicama izostaviti u tiskovnoj izvedenici; prozu prenijeti u tekst. |
| R10 | web: QR kod na zaslonu, `.mf1-eyebrow` + meta „AUTORICA” na svakom poglavlju (CSS pravilo ne djeluje), prva stavka bočne trake, 90 redaka „Vrati se na zadatak” u F | Vizualni šum koji nema funkciju na zaslonu. | QR samo za `pdf`/`print` u registru komponenti; sakriti meta blok; „Vrati se” kao ikona uz naslov. |

### 3.2 Parovi primjer ↔ zadatak koji su isti problem s drugim brojevima (autorska odluka)

Recenzenti su ih zabilježili, a ne traže nove zadatke. Minimalni zahvati bez novog sadržaja:

| Pog. | Par | Najmanji zahvat |
|---|---|---|
| 1 | P5 ≈ P6 (lanac $p=F/A\to F=pA$; pet od šest primjera) | P6 skratiti na zahtjeve 1, 2, 4 ili ukloniti (ostaje 5 primjera). |
| 2 | P3 ≡ Z6 (mikrodozator / kapilarna igla: isti postupak); P1 trivijalan ($\nu=\mu/\rho$) | P3 skratiti na korake 1–2 (Z6 ostaje T4 s istim brojevima); P1 svesti na rečenicu u Temelju. |
| 4 | P1 ≡ P5 (translatorni nagib riješen četiri puta: P1, P5, Z1, Z2) | Ukloniti P1 (CFD blok upućuje na P5). |
| 5 | P5 ≈ P6 (četvrtina valjka, dva smjera vode) | P5 svesti na odlomak „što se mijenja ako voda kvasi drugu stranu” uz P6. |
| 6 | Z1 ≈ P1, Z2 ≈ P2; Z4 „ulje” gustoće 992,4 kg/m³ (nerealno) | U naputku uputiti na pripadni primjer; Z4 preimenovati fluid („vodena otopina”, $\rho_x$) bez promjene brojeva. |
| 8 | Z2 ≈ P5 | Naputak upućuje na P5. |
| 10 | Z3 ≈ P3; Z5.4 traži optimum $u=v/3$ koji je napisan u provjeri P1 (r. 330) | Iz P1 obrisati rečenicu o optimumu jedne lopatice (Z5 postaje neovisan). |
| 14 | Z2 ≈ P1, Z1 ≈ Z2 (nepomične plohe iz pog. 10 na 3 od 12 mjesta poglavlja o turbostrojevima); P2 je prvi dio P3 | Zabilježiti za sljedeći ciklus; P2 skratiti. |
| 15 | Z2 ≡ P2 ($y_c$, $E_{min}$ iz $q$; Z4 ponavlja); Z5 i P4 isti ulazni podatci | U Z2 zamijeniti pitanje 2 pitanjem koje P2 ne postavlja (npr. $E$ pri $2y_c$ i grana); u Z5 promijeniti $b$. |

### 3.3 Ujednačiti isti element kroz knjigu

| # | Element | Sada | Prijedlog |
|---|---|---|---|
| U1 | odjeljak zadataka | „Zadaci za vježbu” (13) / „za samostalan rad” (pog. 5, 13); u izvoru „Zadaci”, filtar mijenja u „Zadatci”; u tijelu 18 : 14 | U izvoru svuda `## Zadatci za vježbu`; zamjenu iz Lua filtra ukloniti (ID-jevi ostaju). |
| U2 | samoprovjera | „Provjeri sebe” (14) / „Konceptualna provjera” (13); jedan blok „Odgovori” (8 pog.) / „Odgovor” po pitanju (7 pog.) | „Provjeri sebe”, odgovor po pitanju (praktičniji na mobitelu). |
| U3 | blok uz bilježnice | „Interaktivni prikaz” / „Numerički pokus” / „Numerička perspektiva”; prefiks ▶ / →; tipke „Pokreni u pregledniku / Pričuvno: otvori u Colabu” prema pog. 13 „Pokreni u JupyterLiteu / Pričuvno: Google Colab” | Jedno pravilo: laboratorij s widgetima = „Interaktivni prikaz”, ostalo = „Numerički pokus”; jedan razred, jedan prefiks, iste tipke; rezervni put kao tekstna poveznica. |
| U4 | nazivi obojenih blokova | „Granica modela — Kada…” / „— kad…” / bez podnaslova; `.mf1-dublje` s prefiksom „Dublje —” (pog. 10) ili bez (1, 6) ili „Fizikalni temelj —” (13); jedini `.mf1-temelj` u pog. 10 | Obrazac „Vrsta — Podnaslov” (veliko slovo); `Dublje` uvijek s prefiksom; `Temelj` izbaciti iz ugovora ili ne spominjati. |
| U5 | razina zadatka | kod P čip uz naslov, kod Z „Razina: T1” sitno desno ispod | Isti čip uz naslov Z; u PDF-u razmak ≈ 1 em ispred svakog Zn. |
| U6 | redoslijed razina | pog. 7: T2,T1,T1,T2,T3,T4; pog. 15: …,T4,T2; pog. 5: Z2 (parabola, moment) T1, a Z4 (trokut) T2 | Zamijeniti položaje (pog. 5 Z2↔Z4, pog. 7 Z1↔Z2, pog. 15 Z5↔Z6) — strukturni zahvat: SVG oznake + D06. |
| U7 | opisi slika | 4 obrasca za skice zadataka; „Slika 4.1: Pregled poglavlja: Relativno…” (dvostruka dvotočka, prazan potpis, 8×); 39/95 bez točke; 71/95 `fig-alt` jednak potpisu | Uvodna slika = opisna rečenica (npr. „Nagnuta slobodna površina u zavoju i paraboloid u rotirajućem spremniku”); zadatci = „Skice uz Z1–Z6: …”; alt ≠ potpis, jedna rečenica o tome što je nacrtano. |
| U8 | skice kao serija | pog. 3–7 (datoteke u03–u08): kurzivne, sitnije oznake, bez naslova; pog. 8–14: uspravne, krupnije (naslovi 17–19 px), deblji obrisi; cijevi čas šrafirane, čas debeli obris (i unutar pog. 8); „tlocrt” na tri načina; Unicode indeksi uz tspan u istoj skici (14 datoteka) | Jedno pravilo (simboli kurziv kao u tekstu, riječi uspravno; raspon osnovne veličine 11–12; cijevi = obris, spremnici = šrafura); provjera u `audit_sketch_design.py`. Mehanička izmjena atributa, bez promjene geometrije. |
| U9 | B/W ispis fluida | voda / ulje / krutina u sivoj skali 231 / 224 / 220 — nerazlučivi bez tekstualne oznake | Samo u tiskovnoj izvedenici: drugi fluid 25–30 % tamniji ili rijetka tekstura; audit „svaki drugi fluid označen”. |
| U10 | bilježnice | dva kućna stila zaglavlja (u01–u08 prema u09–u15); „Poglavlje U05” u datoteci `u06_…` (broj datoteke ≠ broj poglavlja); decimalna točka u izlazima | Jedno zaglavlje „# Naslov / **Poglavlje 5 — …**” s brojem iz knjige; zajednička ćelija s formatterom za zarez. |
| U11 | nazivlje | „usisna košara” (pog. 8) / „usisni koš” (13); „pumpno kućište”, „pumpnim stanicama” (6, 10); „impeler” (13) / „radno kolo” (14); „brodski vijak” / „propeler”; „Disipacijski” / „umirni bazen” (15); „okr/min” (4, F) / „min⁻¹”; „ullage” bez hrvatske inačice; horizontalno/vodoravno 51 : 100 | Jedan naziv za svako (usisni koš, kućište crpke, radno kolo, propeler, umirni bazen, min⁻¹, „ulaž (engl. ullage)”, vodoravno/okomito). |
| U12 | notacija (odstupanja od tablice) | $K$ (modul i kobilica), $M$ (metacentar i moment), $v_s$ (brod i usisni presjek), $k$ s tri značenja (pog. 11, 12, 14), „st” za stijenku i stepenicu (pog. 12 P6), $R$ hidraulički otpor (13), $H$ umjesto $H_p$ (13 P5), $h_v$ u drugom značenju (4, 13), $H_t$, $T_g$, $\rho_b$, ext/int (3), $F_n$, $f/r$, $d_M$ (1), $h_R$, $T$ spojnica, `\mathbf` umjesto `\vec` (5), $p_0$ kao manometarski (9 P4), tri oznake za uteg $m_s/m_k/m_a$ (6, A, F), $\vec g_{eff}$ sada ujednačen | Minimalne zamjene po izvještajima; poznate iznimke ($K$, $M$, $k$, $R$) zapisati u dodatak A. |
| U13 | zapis popisa u matematici | $(26,0)$ m/s, $\tau=20,40,80$ Pa — čita se kao decimalni broj | Točka-zarez ili razmak: $(26;\,0)$, kao što već radi pog. 3. |
| U14 | pojmovnik B | abeceda (No-slip, Rezidual), „No-slip uvjet” (knjiga rabi „prianjanje”), pojmovi kojih u poglavljima nema (Boussinesq, Coriolisov koeficijent, podekspandirani), nedostaju Bernoullijeva jednadžba (69 pojava), Darcy–Weisbach, Pelton, sifon, meniskus | 5–6 jednorečeničnih redaka za pojmove koji su u knjizi središnji; preimenovati/ukloniti rubne. |

### 3.4 PDF i web — ostalo

| # | Što | Prijedlog |
|---|---|---|
| V1 | 798 numeriranih jednadžbi, referirano ~49; numerirani su i zadani podatci („$g=9{,}81$” kao jednadžba) | Numerirati samo teoriju i referirane; u rješenjima nenumerirane istaknute jednadžbe. |
| V2 | 20 stranica s 18–66 % praznine na dnu (slike ne plutaju); „Slika ispod…” a slika na sljedećoj stranici (str. 48, 67, 200); skice koje zauzimaju pola stranice s malo informacija (str. 64, 137) | Plutanje slika ili manji format (STANDARD umjesto WIDE); „Slika 3.1” s brojem umjesto „ispod”. |
| V3 | odlomci bez razmaka i uvlake (str. 28, 104 — „zid teksta”); tijesan prored u natuknicama okvira (vektori dodiruju redak iznad) | Razmak odlomaka 0,5–0,6 em; prored popisa u okvirima kao osnovni. |
| V4 | „Vrati se na zadatak” 91× i poveznice uz QR bez broja stranice/URL-a — u tisku mrtve | „→ str. N” (Typst `locate`); uz QR jedna kratka adresa. |
| V5 | tablice nenumerirane, dimenzijska matrica numerirana kao „Slika 11.2”; stupac „Fizikalno tumačenje” širok 100 pt (str. 205) | Numeracija „Tablica n.m”; širine stupaca. |
| V6 | dodatak C: redci „vizualnih oznaka” („ρ / γ / p F / A”) u PDF-u kao gole tekstne linije | Sakriti u PDF/print preko registra ili ukloniti (i rečenicu r. 18). |
| V7 | „pog.” i broj lome se preko retka (str. 67, 104, 155, 200, 221); inline formula u Z6 pog. 5 lomi se unutar $|F-F_m|$ | Neprekidni razmak u generatoru omotača; formulu u zaseban redak. |
| V8 | bibliografija zatvara navodnike „…“ (njemački), tekst „…”; izdanja White 2011, Munson 2009, Çengel 2014 zastarjela; [6], [12], [17], [20], [23] bez godine/izdavača | CSL lokalizacija; osvježiti izdanja i dopuniti zapise. |
| V9 | kratica „MF1” 16× u tekstu bez razrješenja („U MF1 gotovo uvijek…”, „Rječnik MF1 → CFD”) | „u ovom priručniku”; u naslovu dodatka D „Rječnik priručnik → CFD”. |
| V10 | web: globalni `a{border-bottom}` curi u navbar/bočnu traku (podcrtani naslov, chevroni); TOC na 820 px u stupcu od 130 px; tablice s `min-width 42rem/32rem` na mobitelu (dodatak A drugi stupac nevidljiv); Google Fonts preko `@import` (offline, GDPR); pregledne skice 6 px oznake, portretne skice razvučene na 835 px s naslovom većim od H1 | Ograničiti pravilo na sadržaj; sakriti TOC ispod ~1000 px; ukloniti `min-width` za 2–3-stupčane tablice; fontovi iz `assets/fonts/`; `figure img {max-height:70vh}`. |
| V11 | web: 4 engleske poruke u pretrazi („Copy link to search”…); naslovi primjera P1–P6 nisu `<h3>` (Z1–Z6 jesu) pa ih navigacija po naslovima preskače; bez JS-a sklopivi blokovi „Toggle callout” i nefokusabilni | `_language.yml` ključevi; `<h3 class="mf1-component-title">`; `<details><summary>` ili oznaka u filtru. |
| V12 | metapodatci: web bez `description`/OG; PDF bez `subject`/`keywords`; tagirani PDF: 127 od 144 slika bez alt-teksta (web ih ima) | `_quarto.yml` `description`, `open-graph`; Typst `set document(…)`; `image(…, alt:)` u `mf1-figures.typ`. |
| V13 | pog. 14: cijela teorija pod jednim H2, propulzija bez naslova; pog. 9, 12, 15 bez odjeljka „Riješeni primjeri” (TOC ne vodi do primjera) | Dva H2 u pog. 14 („Eulerova jednadžba i trokuti brzina”, „Propulzija: aktuatorski disk”) bez novog teksta; u alatnoj traci poveznica na prvi primjer. |
| V14 | pog. 15 „Zastani i promisli”: odgovor počinje definicijom VOF-a umjesto odgovorom | Premjestiti rečenicu. |

---

## 4. P3 — opcionalno

Potpuni popis je u izvještajima; ovdje samo najzanimljivije:

- 54 nereferencirana SVG-a u `assets/print/` (stare verzije) — premjestiti u arhivu.
- Sadržaj PDF-a do dvije razine; razdjelnice dijelova ujednačiti; recto/verso ako ide u dvostrani tisak.
- „0. Kako koristiti priručnik” bez broja (jedini naslov s točkom).
- Tamni način weba (tokeni su već centralizirani).
- `lang="en"` na engleskim izrazima; `<caption>` i `scope` u tablicama; `aria-label` bočne navigacije.
- Katalog na početnoj stranici ima druge naslove od bočne trake („Reologija i međupovršine” → „Viskoznost…”).
- Jedan `\boxed`, HTML komentari „[NOVA PEDAGOŠKA DOPUNA]”, prazna sidra s dijakritikom — ostatci uređivanja u izvoru.
- Procjene razina (pog. 3 P2 T3→T2; pog. 13 Z4 T2→T3) — napomene, ne zahtjevi.

---

## 5. Što je dobro i treba ostati (potvrđeno)

- **Točnost**: svih 180 brojčanih rezultata reproducirano na zadnju znamenku (uz S2, S9); nijedan izvod bez pogreške u koraku ili predznaku; svi međupoglavni ID-jevi postoje; sva 23 bibliografska ključa citirana i obrnuto; dodatak C odgovara stvarnim zadatcima u svih 15 poglavlja; formule u A točne.
- **Didaktika**: blokovi „Granica modela” (pog. 2, 6, 10, 11, 13–15 posebno), zadatci T4 koji traže obrazloženu odluku, dva optimuma Peltonove lopatice (pog. 14) kao najbolje didaktičko mjesto, primjeri iz prakse (sondiranje tanka, separator s gravitacijskim diskom, Rapsonov stroj, zahvatni usis, Hardy–Cross, spar-turbina).
- **CFD**: svih 52 odlomka konkretni, bez izmišljenih rezultata, s pitanjem → modelom → podatcima → provjerom; dodatak D pošten („Kada CFD ne treba”).
- **Jezik**: čist nakon lekture; dosljedni oblici i nazivlje; glas „mi” u rješenju i „ti” u zahtjevima.
- **Vizualno**: web zreo i suzdržan (paleta, tanke lijeve crte, mirna bočna traka, bez horizontalnog pomaka na 390 px); PDF bez ijednog retka ili jednadžbe izvan stupca, hijerarhija naslova čitljiva, oznake skica ≥ 9 pt; vektorski standard proveden i u tisku; kompozitne skice Z1–Z6 čitljive u sivoj skali; QR kodovi ispravni (17/17); interaktivni laboratorij radi iz prve u JupyterLiteu.
- **Pristupačnost weba**: `lang="hr"`, alt na svim slikama, asistivni MathML za sve formule, vidljiv fokus, axe-core bez ozbiljnih povreda.

---

## 6. Preporučeni redoslijed provedbe

Sve je bez novog sadržaja; procjena je gruba, a neki koraci traže obnovu D06, izvedenica i puni CI.

| Korak | Stavke | Učinak | Rizik |
|---|---|---|---|
| 1 | T1 (decimalni zarez), T2, V7 | Najvidljiviji kvar PDF-a nestaje; jedan filtar | nizak |
| 2 | S1–S12 (sadržajne ispravke i zaokruživanja), W2, W3, W4, W5 | Sve poznate netočnosti i vidljive greške | nizak; S2/S9 traže verifikator + D06 |
| 3 | R1 (Inženjerski kontekst + X.1), D2 (početak knjige), R2–R7 | Knjiga kraća za ~10 stranica, bez ponavljanja | nizak; samo brisanje |
| 4 | D1 (jedan oblik sažetka), U1–U5, U11, U13 | Dosljednost vidljiva u sadržaju i na svakoj stranici | srednji; dotiče 15 poglavlja |
| 5 | T8 (indeksi u skicama), U8, U9, T7, R8, R9, U7 | Skice kao jedna serija, čitljive u B/W i na mobitelu | srednji; obnova izvedenica + audit |
| 6 | W1, W6, V10–V12 | Web na mobitelu i pristupačnost PDF-a | nizak |
| 7 | T4–T6, V1–V5, V8–V9 | Prijelom, naslovnica, impresum, jednadžbe, bibliografija | srednji (Typst predložak) |
| 8 | 3.2 (parovi primjer–zadatak), U6, U12, U14 | Didaktika i notacija — autorska odluka | srednji; D06, SVG, verifikatori |

---

## 7. Odluke koje su autoričine

1. **Oblik sažetka** za svih 15 poglavlja (preporuka u D1).
2. **Okvir „Inženjerski kontekst”**: ukloniti ili svesti na jednu rečenicu (R1).
3. **Parovi primjer–zadatak** (3.2): koje skratiti sada, a koje ostaviti za sljedeći ciklus.
4. **Pravopis**: potkritični/natkritični; naslov pog. 5 „Hidrostatičke”.
5. **Indeksi u tiskovnim skicama** ispod 9 pt (T8) — svjesno odstupanje od vlastitog pravila.
6. **Naslovnica i impresum**: ustanova, godina, status izdanja, URL-ovi.
7. **Bibliografija**: osvježiti izdanja (White, Munson, Çengel).

---

Potpuni izvještaji (s retcima, brojevima stranica, snimkama i skriptama kojima su mjerenja
ponovljiva): `docs/radno/recenzija-2026-10/` — `web.md`, `pdf.md`, `sadrzaj_u01_u05.md`,
`sadrzaj_u06_u10.md`, `sadrzaj_u11_u15.md`, `struktura_i_dodaci.md`, `skice_i_interaktivno.md`,
`jezik_i_pristupacnost.md`.
