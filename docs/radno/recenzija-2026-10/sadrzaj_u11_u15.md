# Sadržajna i didaktička recenzija poglavlja 11–15

Područje: `sadrzaj_u11_u15` — `source/u11_dimenzijska_analiza_i_slicnost.md`,
`u12_diferencijalni_opis_realnog_toka.md`, `u13_gubici_cjevovodi_crpke_i_mreze.md`,
`u14_turbostrojevi_i_propulzija.md`, `u15_otvoreni_tokovi.md`.
Recenzent: strog, dobronamjeran, mehanika fluida. Ništa u repozitoriju nije mijenjano.

Što sam doista provjerio: svih pet datoteka pročitao sam od prvog do zadnjeg retka
(4165 redaka); izvode sam pratio korak po korak; **sve** brojčane rezultate riješenih
primjera P1–P6 i kontrolnih rezultata Z1–Z6 u svih pet poglavlja ponovno sam izračunao
skriptom (`scratchpad/recenzija/sadrzaj_u11_u15/check.py`, Python iz `.venv-ci`), što je
više od tražene polovice; provjerio sam postojanje svih međupoglavnih ID-jeva na koje
tekst upućuje (svi postoje), sadržaj bilježnica `u13_paralelne_grane.ipynb` i
`u12_pelton_lopatica.ipynb` (nastavci za Z3/Z6 odnosno Z3–Z5 doista postoje) te README
paketa `data/cfd/backstep_experiment`. Nalaze lekture (`docs/radno/lektura-2026-10/`)
ne ponavljam; one koje sam neovisno potvrdio označujem „potvrđeno (lektura)”.

## 1. Sažetak

Poglavlja 11–15 fizikalno su i matematički točna: od oko 110 provjerenih brojeva
odstupaju samo dva već poznata (u12 δ na krmi 0,087 m, ne 0,088; u14 dron 5,87 N iz
zaokruženih faktora) i nijedan izvod nema pogrešku u koraku ili predznaku. Razina
izlaganja odgovara drugoj godini: svaki zakon dolazi s bilancom, pretpostavkom i granicom
valjanosti, a blokovi „Granica modela” spadaju među najbolje dijelove knjige. CFD odlomci
su uvjerljivi, nepretenciozni i stručno točni (MRF/klizna mreža, VOF, $p_{rgh}$, $y^+$,
GCI), bez izmišljenih rezultata. Glavni problemi nisu u točnosti nego u **ponavljanju i
strukturi**: nakon dodavanja uvodnih tekstova okviri „Inženjerski kontekst” u svih pet
poglavlja ponavljaju uvod gotovo doslovno; nekoliko je zadataka računski istovjetno
riješenom primjeru (u15 Z2 ≡ P2, u14 Z2 ≈ P1, u14 Z1 ≈ Z2); završni okviri, nazivi
blokova samoprovjere, naslovi odjeljaka sa zadatcima i tekst gumba bilježnica razlikuju
se od poglavlja do poglavlja. Oznaka $k$ ima tri značenja u tri uzastopna poglavlja
(faktor oblika $1+k$, turbulentna kinetička energija, gubitak relativne brzine), a u u15
$y_1$ u istom odlomku znači dvije različite dubine. Uz ispravak P1 nalaza (njih 6) i
ujednačavanje P2 strukture, područje je spremno za završetak; ništa ne treba dodavati.

## 2. Tablica nalaza

Oznaka retka odnosi se na `source/uNN_*.md`. „Potvrđeno (lektura)” = nalaz iz
`docs/radno/lektura-2026-10/`, koji sam neovisno provjerio i potvrđujem.

### P1 — ispraviti prije završetka

| # | Gdje | Što | Zašto je problem | Prijedlog |
|---|---|---|---|---|
| 1 | u15 r. 176–189 | U istom odlomku $y_1$ je najprije *uzvodna* dubina ispred ustave ($Q=C_d\,b\,a\sqrt{2gy_1}$), a dva retka dalje „dubina suženog mlaza ispod ustave, $y_1\approx C_ca$”. $C_c$ nije definiran riječima. | Student koji uvrsti $y_1$ iz formule za istjecanje u spregnute dubine dobit će besmislen rezultat; isti simbol za dvije dubine u pet redaka. Potvrđeno (lektura), podižem na P1. | Uzvodnu dubinu nazvati $y_0$ (kao na uvodnoj slici, r. 9, gdje je $y_0$ već „početna dubina mirnog toka”), zadržati $y_1$ za suženi mlaz; dodati „($C_c$ koeficijent kontrakcije)”. |
| 2 | u12 r. 328 | $(1{,}08\cdot10^7)^{1/5}=25{,}5$, ne 25,2; $\delta\approx0{,}087$ m. | Pogrešan međurezultat u prikazanom računu; čitatelj koji ponovi račun dobije drugu vrijednost. Potvrđeno (lektura) ponovnim računom: 25,508; 0,0870 m. | `=\frac{2{,}22}{25{,}5}\approx0{,}087\ \text{m}`; provjeriti verifikator i D06. |
| 3 | u14 r. 133 | „To je isti izraz kao umnožak $F_xu$ … iz jednadžbe -04”. Jednadžba -04 ima $\dot m_{rel}$, Eulerov zapis -05 puni $\dot m$. | Upravo je razlika $\dot m_{rel}$ prema $\dot m$ središnja poruka poglavlja (dva optimuma); „isti izraz” je potkopava. Potvrđeno (lektura). | „Isti oblik kao $F_xu$ iz jednadžbe -04, ali s punim protokom $\dot m$ umjesto $\dot m_{rel}$: Eulerov zapis vrijedi za kolo, ne za jednu lopaticu.” |
| 4 | u14 r. 142 | „razlika otkriva nekonvergiranu mrežu ili propuštanje kroz spoj okvira” | Mreža ne konvergira, nego rješenje; k tome $P=M\omega$ i Eulerov tok razlikuju se i fizikalno (trenje diska, procjepi), ne samo numerički. Potvrđeno (lektura). | „razlika otkriva nekonvergirano rješenje, propuštanje kroz spoj okvira ili gubitke koje Eulerov zapis ne sadrži (trenje diska, procjepi)”. |
| 5 | u13 r. 776 (Z2, naputak) | „Brzina je ista za oba fluida; razlikuju se samo $Re$.” | Razlikuju se i gustoće (1080 prema 998), a $\Delta p=\lambda\frac{L}{D}\frac{\rho v^2}{2}$ ovisi o $\rho$; naputak navodi na pogrešan račun. Potvrđeno (lektura). | „Brzina je ista za oba fluida; razlikuju se $Re$ (dakle režim i $\lambda$) i gustoća.” |
| 6 | u11 r. 306 | „dok se viskozni dio skalira preko $C_F$, a ne faktorom $\lambda_L^3$” iza jednadžbe za **snagu** ($\lambda_L^{7/2}$). | Miješa faktor sile i faktor snage u istoj rečenici; student ne zna na koju se veličinu „a ne” odnosi. Potvrđeno (lektura). | „…dok se viskozni dio otpora računa preko $C_F$ pri brodskom $Re$ i ne skalira ni faktorom $\lambda_L^3$ (sila) ni $\lambda_L^{7/2}$ (snaga).” |

### P2 — vrijedi napraviti

| # | Gdje | Što | Zašto je problem | Prijedlog |
|---|---|---|---|---|
| 7 | u11 r. 15–21; u12 r. 15–21; u13 r. 15–21; u14 r. 15–19; u15 r. 15–21 | Okvir „Inženjerski kontekst” (i rečenica ispod prvog H2) ponavlja uvodni tekst poglavlja gotovo doslovno: u11 „Brod se prije gradnje ispituje kao model u vučnom bazenu…svi mjerodavni brojevi” (r. 1, 5 i 20); u13 „balastni vod, rashladni krug, protupožarna mreža, grijanje” (r. 7 i 20); u12 „uljni film, rashladni kanal, otpor trupa, CFD” (r. 7 i 20); u14 r. 3–5 i 18; u15 r. 5 i 20. | Uvodni tekst dodan je naknadno (commit 40a088e); okviri su sada čisto ponavljanje na istoj stranici, što je prvi dojam svakog poglavlja. | Skratiti okvir na jednu rečenicu koja donosi *novo* (npr. u11: „Kad se svi brojevi ne mogu uskladiti, bira se prioritetna sličnost, a učinak ostalih brojčano se procjenjuje.”) ili ga ukloniti, uz zadržavanje retka „Procijenjeno vrijeme rada”. Vidi i odjeljak 4. |
| 8 | u15 P2 (r. 146–172) i Z2 (r. 449–475) | P2 „Kritični presjek na širokom preljevu” i Z2 „Kritična dubina i minimalna energija” traže isto: iz $q$ izračunati $y_c=(q^2/g)^{1/3}$ i $E_{min}=\tfrac32y_c$. Isti korak ponavlja i Z4 (točka 1). | Dva zadatka zapravo su isti; Z2 ne donosi nikakvu novu studentsku odluku. | Ne dodavati novi zadatak; najmanji zahvat: u Z2 zadržati podatke, ali zamijeniti pitanje 2 pitanjem koje P2 ne postavlja (npr. „kolika je $E$ pri dubini $2y_c$ i koja je grana?”) ili u P2 ostaviti samo $y_c$, a $E_{min}$ i $Fr=1$ prepustiti Z2. |
| 9 | u14 P1 (r. 231–295), Z1 (r. 708–731), Z2 (r. 733–758) | P1 (nepomična vodilica, 120°, 24→19 m/s), Z2 (nepomična vodilica, 110°, bez gubitka) i Z1 (nepomična ploča, 90°) ista su vrsta problema: $\vec F=\dot m(\vec v_1-\vec v_2)$ na nepomičnoj plohi, što poglavlje samo kaže da je izvedeno u pog. 10 (r. 25). U poglavlju o *turbostrojevima* tri od dvanaest mjesta troše se na nepomične plohe. | Z1 i Z2 razlikuju se samo kutom; Z2 je P1 s drugim brojevima. Ne provjerava se ništa od onoga što je novo u poglavlju (relativna brzina, trokut, Euler). | U ovom ciklusu ne mijenjati broj zadataka; zabilježiti za sljedeći ciklus kao kandidate za zamjenu (Z2 prije Z1). Minimalno: u P1 skratiti tumačenje (r. 294 je već u pog. 10). |
| 10 | u11 r. 311 ($1+k$), u12 r. 371 ($k=\tfrac12\overline{v_i'v_i'}$), u14 r. 39 i dalje ($w_2=kw_1$) | Oznaka $k$ u tri uzastopna poglavlja ima tri značenja: faktor oblika ITTC, turbulentnu kinetičku energiju i koeficijent gubitka relativne brzine; nijedno nije u tablici notacije `docs/urednicki_stil.md` (tamo je samo $k_s$). | Krši pravilo „jedna veličina – jedna oznaka”; $k$ iz u12 i u14 javljaju se i u zadatcima (u12 P5, Z5 preko $k_s$; u14 Z3 traži $k$). | Najmanji zahvat: u u14 uvesti $k$ s izričitom napomenom pri prvom spomenu (r. 39) kako to čini pog. 15 za $c$ i $q$; u11 r. 311 pisati „$(1+k)$, faktor oblika” već piše — dovoljno; dodati sva tri u dodatak A kao iznimke. |
| 11 | u12 P6 (r. 437–444) | U istom primjeru indeks „st” znači stijenku ($\tau_{st}$) i stepenicu ($H_{st}$, $Re_{st}$). | Tablica notacije rezervira „st” za stijenku; u istoj rečenici r. 437 stoje $H_{st}$ i $\tau_{st}$. | $H_{st}\to H_s$ ili $h_{step}$; usput $U_{ref}$ nije u tablici (prihvatljivo, definiran je u tekstu). |
| 12 | u15 r. 332–334 | „Zastani i promisli” pita jesu li pad energije i zatvorena bilanca količine gibanja nespojivi; odgovor **počinje** definicijom metode VOF, a stvarni odgovor dolazi tek u 4. rečenici. | Ugovor traži: pitanje, pa pripadno tumačenje. Ovdje tumačenje počinje nečim nepovezanim, pa student misli da je VOF odgovor. | Premjestiti rečenicu „Metoda VOF prati…” iza rečenice „Pad mehaničke energije uz zatvorenu bilancu … očekivana je posljedica disipacije u skoku.” |
| 13 | u13 r. 688, 723; u11/u12/u14/u15 | Nazivi se razlikuju: u13 „Konceptualna provjera” i „Zadaci za samostalan rad”, ostala četiri „Provjeri sebe” i „Zadaci za vježbu”; u13 gumbi „Pokreni u JupyterLiteu / Pričuvno: Google Colab”, ostala „Pokreni u pregledniku / Pričuvno: otvori u Colabu”; oznake bilježničkih blokova: „Interaktivni prikaz” (u11, u14), „Numerički pokus” (u12, u13, u15), a u13 „Numerički pokus” nosi klasu `mf1-interaktivno`. | Dojam neujednačenosti u pet uzastopnih poglavlja; student uči tri različita naziva za istu stvar. | Ujednačiti na „Provjeri sebe”, „Zadaci za vježbu”, „Pokreni u pregledniku / Pričuvno: otvori u Colabu”; za bilježnice jedno pravilo: interaktivni laboratorij s widgetima = „Interaktivni prikaz”, ostalo = „Numerički pokus”. |
| 14 | u11 r. 972–994; u12 r. 716–725; u13 r. 909–921; u14 r. 884–900; u15 r. 617–625 | Završni okviri nemaju istu strukturu: u11 ima natuknice + „Najčešća pogreška” + „Nakon ovoga poglavlja mora biti moguće” + „Kamo dalje”; u14 prve tri; u13 numerirani popis + „Najčešća pogreška” pod naslovom „Sažeta mapa modela” i zasebnim H2 „Sažetak”; u12 i u15 samo natuknice. | Sažetak je mjesto na koje se student najčešće vraća; različit sadržaj po poglavljima otežava učenje za ispit. | Odabrati jedan obrazac (predlažem u14: natuknice + najčešća pogreška + ishodi) i primijeniti ga na pet poglavlja; u12 i u15 ishodi se mogu prepisati iz postojećeg teksta (u15 r. 380–386 „Postupak analize” već je gotov materijal). |
| 15 | u14 r. 23–226 | Cijela teorija (lopatica, dva optimuma, Euler, dva CFD bloka, interaktivni prikaz, aktuatorski disk, granica modela) stoji pod jednim H2 „Od lopatice do turbostroja”; propulzija nema vlastiti naslov iako je intro najavljuje kao treću cjelinu (r. 7). | Navigacija i sadržaj knjige ne pokazuju gdje počinje propulzija; ostala poglavlja imaju 5–7 H2. | Dodati H2 „Eulerova jednadžba i trokuti brzina” ispred r. 98 i H2 „Propulzija: aktuatorski disk” ispred r. 174 — bez novog teksta. |
| 16 | u12 r. 288 | „Turbulentni sloj … odvaja se kasnije; **zato** se na modelu broda sloj namjerno prevodi u turbulentni” | U primjeru trupa (r. 342) stimulator se opravdava ispravnim $C_{F,m}$ za Froudeovu korekciju; „zato” povezuje krivi uzrok. Potvrđeno (lektura). | „…odvaja se kasnije. Na modelu broda sloj se prevodi u turbulentni i zato da bi $C_{F,m}$ odgovarao turbulentnoj korelacijskoj liniji (@ex-granicni-sloj-trupa-modela).” |
| 17 | u15 r. 206 | „presjek s kritičnom dubinom može određivati režim toka” | Kontrolni presjek određuje vezu dubina–protok i uzvodnu razinu, ne „režim”. Potvrđeno (lektura). | „…zašto presjek s kritičnom dubinom djeluje kao kontrolni presjek: ondje je veza dubine i protoka jednoznačna, a…”. |
| 18 | u15 r. 294 (naslov P4) | „Disipacijski bazen” prema „umirni bazen” u r. 5, 330 i D04. | Dva naziva za isti objekt unutar poglavlja. Potvrđeno (lektura). | „Umirni bazen iza ustave” uz regeneraciju D06 (naslov je u ključu). |
| 19 | u15 Z5 (r. 538–566) i P4 (r. 293–326) | Isti ulaz ($y_1=0{,}250$ m, $q/y_1=6{,}0$ m/s) i ista spregnuta dubina 1,2353 m. | Pitanje (T4, nesigurnost) jest različito, ali student prepoznaje gotove brojeve. Potvrđeno (lektura). | Ako se išta mijenja, promijeniti samo $Q$ ili $b$ u Z5 (npr. $b=1{,}50$ m) i regenerirati D06/verifikator; inače prihvatljivo. |
| 20 | u13 r. 602–616 (P5) | Visina dobave piše se $H$ i $P_h=\rho gQH$; odjeljak i tablica notacije koriste $H_p$. | Nedosljednost u istom poglavlju. Potvrđeno (lektura). | $H\to H_p$ (tri mjesta). |
| 21 | u13 r. 794 (Z3), r. 900 (Z6) | $h_v=R_vQ_i^2$ ($h_v$ je u tablici sloj vode); „zajednički gubitak $h_{AB}$” bez imenovanih čvorova A, B u tekstu; $NPSH_r(q,n_2)$ s malim $q$. | Potvrđeno (lektura). | $h_v\to h_{g,V}$; „između zajedničkih čvorova A i B”; $NPSH_r(Q,n_2)$. |
| 22 | u14 r. 536 | „stvarnu visinu reda $0{,}82\cdot27{,}8\approx22{,}8$ m” — faktor 0,82 bez imena i izvora. | Potvrđeno (lektura). Student ne zna je li to faktor klizanja, hidraulička učinkovitost ili oboje. | „uz pretpostavljeni umnožak faktora klizanja i hidrauličke učinkovitosti $\approx0{,}82$”. |
| 23 | u11 r. 318–378 | Slika `u14_fig_odluka` (dijagram pitanja, alt-tekst nabraja svih sedam) i odmah ispod sedmerostruka mreža odluke s istim pitanjima. | Isti sadržaj dvaput na istoj stranici; mreža je potpuna, slika je njezin sažetak. | Zadržati jedno: ili sliku s kraćim „Tumačenjem dijagrama”, ili mrežu bez slike (slika je u tiskanom izdanju vjerojatno korisnija). |
| 24 | u11 r. 46–49 i r. 3 | Okvir „Fizikalno značenje” ponavlja drugi odlomak uvoda ($Re$, $Fr^2$, $We$ omjeri sila; $St$ vremenske skale; $Ma$; $C_p$, $C_D$ odzivi). | Treće ponavljanje istog popisa unutar prve stranice (uvod, tablica r. 151, okvir). | Skratiti okvir na posljednju rečenicu („Jednaka vrijednost jedne grupe nije dovoljna…”). |
| 25 | u15 r. 53–55 i još 4×; D01 r. 203; D06 r. 739 | „podkritični/nadkritični” prema pravopisnom „potkritični/natkritični”. | Potvrđeno (lektura); odluka za cijelu knjigu. | Odlučiti; ako ostaje strukovni oblik, navesti u uredničkom stilu kao svjesnu iznimku. |

### P3 — opcionalno

| # | Gdje | Što | Prijedlog |
|---|---|---|---|
| 26 | u12 P1 (r. 37–59) i Z1 (r. 520–545) | Oba računaju $v\,dv/dx$ u 1D polju; Z1 dodaje samo $\partial v/\partial t$. P2 (uljni film) i Z4 dijele sve podatke ($\mu=0{,}10$, $H=1$ mm, $u=2$ m/s); P3 (mikrokanal, 652 Pa) i Z3 isti podatci (namjerno obrnuti). | Prihvatljivo kao „primjer → zadatak”, ali tri od šest zadataka koriste podatke primjera; zabilježiti za budući ciklus. |
| 27 | u13 Z4 (T2, r. 818–847) | Zadatak izričito traži računski alat i iterativno rješavanje Colebrooka i radne točke; po matrici to je bliže T3 (kombiniranje modela) nego T2 (geometrijska/jedinična odluka). | Ne mijenjati oznaku radi kvote; samo napomena autorici. Z6 (T4) ponavlja postupak P4 (afinitetni $s$ pri istom $Q$) i P6 (NPSH), što je za T4 sintezu u redu. |
| 28 | u15 r. 325 | Za duljinu umirnog bazena citiraju se [@nasa-cfd-vv; @asme-vv20-2009] (standardi V&V), što se čita kao izvor za duljinu bazena. | Premjestiti citate uz „validiranog CFD-a” ili ih izostaviti; za bazen je prirodan [@chow1959]. |
| 29 | u14 r. 5 i r. 211; r. 5 i r. 174 | Rečenica „potisak dobiven velikom brzinom mlaza plaća se skupom kinetičkom energijom traga” doslovno dvaput; „U propulziji pogonski sustav predaje energiju fluidu” doslovno dvaput. | Jednu od svake izbrisati (uvod je noviji; zadržati u izvodu). |
| 30 | u14 r. 185–189 | Jednadžba -08 završava točkom, a iduća riječ je „odnosno” malim slovom. | Točku u formuli zamijeniti zarezom. |
| 31 | u11 r. 224/226 i r. 258/260 | Jednadžbe -02 završavaju zarezom, a iza njih počinje nova rečenica velikim slovom. Potvrđeno (lektura). | Zarez → točka. |
| 32 | u13 r. 99 | „Kod naglog proširenja” (kalk koji je lektura drugdje uklanjala); r. 538 „stalan $\lambda$ pri $Re\approx0{,}9$–$1{,}8\cdot10^5$ stvarni bi projekt provjerio…” — rečenica bez veznika. | „Pri naglom proširenju”; „stalan $\lambda$ … jest pojednostavnjenje: stvarni bi projekt provjerio…”. |
| 33 | u13 r. 308, 370, 719 | „radno kolo (impeler)” pa dalje „impeler” (4×), a u14 samo „radno kolo”. | Jedan naziv: „radno kolo”. |
| 34 | u13 r. 73 | Slika `u10_fig_uvod_pregled.svg` (ime iz stare numeracije) koristi se samo ovdje; r. 77 ponavlja definicije $h_l$, $h_{loc}$ koje odmah slijede u r. 87–97. | Ime nije problem (stabilni ID); r. 77 skratiti na rečenicu o skici. |
| 35 | u12 r. 439/444 | „zaokružene” vrijednosti CFD-a sa 7 znamenaka (6,541667); README kaže da su zaokružene prema izvornoj tablici. Potvrđeno (lektura). | „prenesene iz izvornih datoteka s izvornim brojem znamenaka”. |
| 36 | u11 r. 179; r. 396; r. 488; r. 977; Z3 naslov | Potvrđeno (lektura): slika prikazuje samo dimenzijsku matricu; „kanal” prema „cijev”; „po jedinici dinamičkog tlaka (i oplakane površine)”; „$Re$ mjeri relativnu važnost viskoznosti” nepotpuno; „pretlak” za negativno očitanje. | Kako predlaže lektura; za Z3 „Manometarski tlak senzora i kavitacijski kriterij” (ulazi u D06). |
| 37 | u12 r. 524 ($a=2$ m/s²), r. 669 ($\lambda_h$), r. 408/429 ($D$ prema $D_h$), r. 262 (gustoća u $Re$ nije zadana) | Potvrđeno (lektura). $\lambda_h$ već jest u D01 (r. 44). | Kako predlaže lektura; za $a$ u Z1 koristiti $a_0$ ili $\kappa_t$. |
| 38 | u13 r. 27 | „pozitivnim članom $h_g\ge0$” → „nenegativnim”. Potvrđeno (lektura). | Jedna riječ. |
| 39 | u14 r. 644 ($P_{st}$), r. 655 (5,87 prema 5,89 N), Z4 naslov „radijusa”, r. 236/246 „visoka”/„dubina” | Potvrđeno (lektura). | $P_{st}\to P_{vr}$ (isto kao u pog. 13); u r. 655 pisati „$\approx5{,}89$ N (iz nezaokruženih vrijednosti)”. |
| 40 | u15 r. 227 | Alternativne dubine označene $y_1$, $y_2$, iste oznake kao spregnute dubine skoka; numerički pokus traži da student objasni zašto *nisu* spregnute. Potvrđeno (lektura). | $y_a$, $y_b$. |
| 41 | u15 r. 370 | Drugi traženi protok (2,70 m³/s) i smanjenje izračunani su u „Provjeri i tumačenju”, a ne u „Rješenju”. Potvrđeno (lektura). | Premjestiti dvije rečenice. |
| 42 | u15 audit | Redoslijed razina Z1–Z6 je T1,T1,T2,T3,T4,T2 (ostala poglavlja završavaju s T4). | Zamijeniti mjesta Z5 i Z6 ako se D06 ionako regenerira. |
| 43 | u13 r. 239–243 i tablica notacije | $R$ kao hidraulički otpor ($\mathrm{s^2/m^5}$) nije u tablici (tamo je $R$ polumjer spremnika); u u12 je $R$ polumjer cijevi. | Unijeti $R$ (hidraulički otpor, pog. 13) u dodatak A kao iznimku. |

## 3. Što je dobro i treba ostati

- **Brojevi i izvodi.** Svi kontrolni rezultati Z1–Z6 i svi riješeni primjeri u pet
  poglavlja reproducirani su na zadnju navedenu znamenku (iznimke #2 i #39). Posebno
  pohvalno: u13 P3 Hardy–Cross (obje iteracije, rezidual 1,1 mm), u12 Z6 (GCI, $n_h=2{,}000$,
  $2s_E$), u15 Z5 (propagacija nesigurnosti sa zajedničkim $q$, $s_\Delta=0{,}0201$),
  u14 P3 (bilanca 20,86 + 1,09 + 0,66 = 22,6 kW).
- **Dva optimuma Peltonove lopatice** (u14 r. 59–85, 217, 466–470): razlika $c_1/3$ i
  $c_1/2$ objašnjena je kontrolnim volumenom, provjerena brojevima i ponovljena u
  „Zastani i promisli”; to je najbolje didaktičko mjesto u pet poglavlja.
- **Blokovi „Granica modela”**: Froudeova hipoteza i ITTC 1957 kao dogovorna linija
  (u11 r. 311), što $NPSH_a$ ne jamči (u13 r. 375), aktuatorski disk kao gornja granica
  (u14 r. 217), skok i plitkovodni opis (u15 r. 290). Svaki navodi zanemareni član,
  raspon i zabranjeni zaključak.
- **CFD odlomci**: konkretni, s pitanjem → modelom → podatcima → izlazom → provjerom;
  stručno točni (u12 $p_{rgh}$ i rubni uvjet tlaka, $y^+$ prema modelu stijenke; u14
  MRF prema kliznoj mreži i provjera $P=M\omega$ prema Eulerovu toku; u15 VOF i što
  mreža ne razlučuje; u13 kako iz CFD-a izvesti $\xi$ s referentnom brzinom). Ne
  predstavljaju izmišljene rezultate kao simulaciju; u12 P6 koristi stvarne TMR podatke s
  provenijencijom.
- **Tvrdnje o praksi** provjerene i točne: ITTC 1957/1978 i faktor oblika, stimulatori na
  5 % $L$, $\chi\approx0{,}14$ za obalni brod, $\eta_0=0{,}55$–$0{,}70$, squat i blokada u
  vučnom bazenu, Swamee–Jain ±1 %, afinitetni zakoni i statička visina (u13 P4 je odličan
  protuprimjer slijepoj primjeni), balastna crpka i usis u balastnom stanju (u13 Z6).
- **Veze među poglavljima**: svi upućeni ID-jevi postoje (u07, u08, u10, D04); u12 P4
  nastavlja u11 P2 s istim brojevima, u14 P4 upućuje na radnu točku u13, u15 povezuje
  $Fr$ broda i kanala — lajtmotivi su stvarno provedeni.
- **Zadatci T4** (u11 Z6 intervali sile, u12 Z6 GCI + validacija, u13 Z6 regulacija +
  NPSH, u14 Z6 granice ulaza, u15 Z5 sukladnost mjerenja) traže obrazloženu odluku, a
  ne samo veći račun; „što nedostaje za odluku” formulacije su primjer dobre prakse.

## 4. Što se može ukloniti ili skratiti bez gubitka

1. **„Inženjerski kontekst” u svih pet poglavlja** (#7): ~5 × 4 retka koji ponavljaju
   uvod; zadržati samo rečenicu koja donosi novo ili ukloniti okvir.
2. **u11 okvir „Fizikalno značenje” r. 46–49** (#24) — treći popis istih brojeva.
3. **u11 dijagram odluke ili mreža odluke** (#23) — jedno od dvoje.
4. **u14 P1 „Provjera i tumačenje” r. 294** i ponovljene rečenice r. 5/174/211 (#29);
   P2 (pokretna lopatica, r. 298–367) sadržajno je prvi dio P3 (ista procedura, $k=0{,}9$,
   drugi kut) — može se skratiti na kraći primjer ili zadržati kao priprema; poglavlje bi i
   s pet primjera ostalo u ugovornom rasponu.
5. **u13 r. 77** (ponavlja definicije iz r. 87–97) i **r. 233–234** (dvije natuknice
   ponavljaju r. 5 iz uvoda).
6. **u15 odjeljak „Postupak analize otvorenog toka” r. 380–386** ne treba brisati, nego
   premjestiti u završni okvir kao ishode (#14): time se u15 ujednačuje s ostalima bez
   novog teksta.
7. **u12 r. 470–486 „Veza s CFD-om”**: odlomak „Tlak i druge diskretizacije” (SIMPLE,
   PISO, FEM) nije potreban za ishod poglavlja; ugovor kaže da nazivi algoritama pripadaju
   dodatnom gradivu (D04 to već obrađuje). Kandidat za premještanje u `.mf1-dublje` ili
   skraćivanje na jednu rečenicu s poveznicom na D04.

## Ograničenja ove recenzije

Pregledan je kanonski `source/`, ne renderirani PDF/web (prijelomi i prikaz skica nisu
dio ovog područja). Verifikatore i D06 nisam pokretao ni uspoređivao redak po redak;
za #2, #18, #36 i #42 autorica treba regenerirati D06. Procjene razine (T2/T3) i
„isti zadatak” autorska su prosudba, a ne nalaz CI-ja.
