# Recenzija: struktura knjige, uvodni dio i dodatci

Područje: `source/index.md`, `source/u00_*.md`, `source/d01…d06*.md`, `content/book.json`, presjek svih
poglavlja (notacija, nazivlje, struktura, opisi slika). Pregledani su kanonski izvori, generirani web
(`_site/`) i PDF (`_book/mehanika-fluida-1.pdf`, 335 str.). Ništa nije mijenjano. Pomoćne snimke
stranica PDF-a: `scratchpad/recenzija/struktura_i_dodaci/pdf_p*.png`.

Oznake: **provjereno** = utvrđeno pretragom izvora ili izravnim čitanjem PDF-a/HTML-a; **dojam** =
autorska procjena. Nalazi koje je lektura (`docs/radno/lektura-2026-10/`) već zabilježila samo su
potvrđeni i označeni „(lektura)”.

## 1. Sažetak

Okvir knjige je čvrst: `book.json` dosljedno vodi 15 poglavlja, 90 primjera i 90 zadataka, oznake polja
(Tekst zadatka / Traži se / Rješenje / Provjera i tumačenje) i razina (`[Razina: T1]{.mf1-task-level}`,
30/30/15/15) potpuno su ujednačene, bibliografija je obostrano potpuna (23 ključa, svi citirani, svi
postoje), a dodatak C po poglavljima doista odgovara stvarnim zadatcima Z1–Z6. Notacijski standard
od 12. listopada proveden je: automatska pretraga nije našla `V` kao brzinu, `\rho_w`, `h_w`, `\tau_w`,
`g_{\mathrm{eff}}` ni `u` kao brzinu fluida (svih 60 pojava `u` jesu brzine krute granice). Dva nalaza ipak
smatram preprekama za završetak: (1) u PDF-u se svaki decimalni zarez u matematici slaže s razmakom
(„9, 20 · 10⁵ Pa”, „35, 772 kPa”; oko 3000 pojava na 214 stranica) i (2) ključ F na osam mjesta ima
generatorski rezervni tekst „odgovarajući izraz” umjesto broja jednadžbe. Treći sustavni problem je
dvojni oblik sažetka poglavlja (numerirani prozni odjeljak u 6 poglavlja, nenumerirani okvir s
natuknicama u 9, s tri podvarijante) te udvostručeni početak knjige („O priručniku” i u `index.md` i u
u00, u PDF-u na str. 6 i 7, dvaput u sadržaju). Dodatci su sadržajno dobri, ali A sadrži sedam
zadatkovno specifičnih redaka i nekoliko praznina, B ima dva poremećaja abecede i pojmove koji se u
poglavljima ne imenuju (a nedostaju Bernoullijeva jednadžba, Darcy–Weisbach, sifon…), a C ima četiri
završna bloka koja ponavljaju uvod. Nakon ispravka P1 nalaza i ujednačavanja sažetaka i opisa slika,
područje je spremno za završetak.

## 2. Nalazi po prioritetu

### P1 — ispraviti prije završetka

| # | Gdje | Što (provjereno) | Zašto je problem | Prijedlog |
|---|---|---|---|---|
| 1 | PDF, sve stranice s formulama (npr. str. 20, jedn. 1.32; str. 327, ključ Z4 pog. 8); `assets/typst/*.typ`, `filters/` | U matematici se `{,}` iz izvora (`9{,}20`) u Typstu slaže kao „9, 20 ⋅ 10⁵ Pa”, „0, 92 MPa”, „35, 772 kPa”, „6, 288 m/s ≈ 12, 2 čv”. Brojanje u tekstu PDF-a: 3042 „d, d” prema 443 tijesnih (prozni brojevi). Web (MathJax) prikazuje tijesno. Nije zabilježeno ni u lekturi ni u `IZVJESTAJ_SKICE.md`. | Svaki brojčani rezultat u PDF-u izgleda kao popis dvaju brojeva; recenzent i student to čitaju kao pogrešku sloga. Izvan užeg područja, ali zahvaća cijelu knjigu. | U Typst filtru (uz postojeće uklanjanje `\!`) pretvoriti `{,}` u matematici u literalni zarez bez razmaka (u Typst mat. zapisu `","` ili ekvivalent); provjeriti na str. 20 i 327 prije i poslije. |
| 2 | `source/d06…md` r. 423, 447, 465, 473, 647, 655, 747, 755 (×2); PDF str. 327–329, 333, 335; web `d06…html`; uzrok `scripts/generate_exercise_key.py:76` | Tekst poveznice glasi „iz jednadžbe [odgovarajući izraz](…#eq-…)” umjesto broja jednadžbe. | Rečenica u ključu je nedovršena („maseni protok izračunaj iz jednadžbe odgovarajući izraz”). | Generator neka ispisuje `[-@eq-id]` (kao što lektura već radi za primjere), pa Quarto daje „jednadžbe 9.12”; ako ID nije razriješiv, ispisati naziv jednadžbe („iz jednadžbe za zagušeni protok”). Obnoviti D06 generatorom. |
| 3 | `source/index.md` r. 5–9 (samo Typst), r. 26–32 („O priručniku”), r. 34–36; `source/u00…md` r. 50–56 („O priručniku”), r. 114–118; PDF str. 2 (sadržaj), 6, 7; web `index.html` i `u00…html` | Početak knjige tri puta kaže komu je namijenjen i da su primjeri iz drugih struka uključeni (index r. 6 i r. 28 gotovo istim riječima, u00 r. 52). Naslov „O priručniku” pojavljuje se u PDF-u na str. 6 i 7 i dvaput u sadržaju; „Numerički pokusi” (index) i „Numerički pokusi i izdanja” (u00) prekrivaju se. (lektura, dopunjeno) | Čitatelj već na prvoj stranici dobiva dojam ponavljanja; sadržaj PDF-a izgleda neuredno. | Jedno mjesto za svaku poruku: `index.md` zadrži hero, katalog i impresum (bez „O priručniku” i „Numerički pokusi”); u00 ostane jedino „O priručniku” + „Predznanje” + „Numerički pokusi i izdanja”. Typst-only odlomak r. 5–9 ukloniti ili pretvoriti u jednu rečenicu ispod naslova. |
| 4 | Završetci svih 15 poglavlja: `## Sažetak` u u01 r. 829, u02 r. 874, u03 r. 833, u04 r. 848, u05 r. 889, u13 r. 909; `.mf1-zavrsni-okvir` u u06–u12, u14, u15 | Dva oblika sažetka: numerirani odjeljak s 2–4 prozna odlomka (6 pog.) i nenumerirani okvir „Za ponijeti iz poglavlja” (9 pog., u PDF-u naslov „Sažetak” bez broja). Unutar okvira tri podvarijante: natuknice + „Najčešća pogreška” + „Nakon ovoga poglavlja mora biti moguće” (u06, u07, u08, u10, u11, u14), samo natuknice (u09, u12, u15), u11 dodatno „Kamo dalje nakon MF1”, u14 „Najčešća pogreška.” inline umjesto kao podnaslov. U sadržaju PDF-a 6 poglavlja ima stavku „x.y Sažetak”, 9 nema. | Brief izričito traži jedan oblik; nedosljednost je vidljiva u sadržaju i pri listanju. | Jedan oblik za svih 15: nenumerirani završni okvir **Sažetak** (ne „Za ponijeti iz poglavlja”) s 5–7 natuknica, jednom rečenicom **Najčešća pogreška** i 3–4 stavke **Nakon ovoga poglavlja mora biti moguće**. Prozne sažetke u 1–5 i 13 pretvoriti u natuknice (sadržaj već postoji); „Kamo dalje nakon MF1” iz u11 ukloniti ili premjestiti u u00. |
| 5 | `content/book.json` (naslov u05 „Hidrostatske sile na ravne i zakrivljene plohe”), `source/u05…md` r. 13, 170, 892; `source/d02…md` r. 17, 127; `source/d04…md` r. 11; `source/d06…md` r. 209–253 (naslov odjeljka F.6); PDF tekuće zaglavlje str. 86–103 | „hidrostatske” u naslovu poglavlja i dodataka; standard nazivlja i ostatak knjige (81 pojava) rabe „hidrostatički”. (lektura, dopunjeno s d02/d04/d06) | Naslov poglavlja u sadržaju, na 18 zaglavlja i u tri dodatka odstupa od vlastitog standarda. | `book.json` title → „Hidrostatičke sile na ravne i zakrivljene plohe”; ispraviti u05 r. 13, 170, 892, d02 r. 17, 127, d04 r. 11; D06 obnoviti generatorom. Stabilni ID i slug ne mijenjati. |
| 6 | `source/u15…md` r. 53, 55, 94, 96, 512 (×2), 524, 576; `source/d01…md` r. 203; `source/d06…md` r. 739; PDF str. 275, 276, 282, 283, 295 | „podkritični”, „nadkritični” (10 pojava) umjesto pravopisnih „potkritični”, „natkritični”. (lektura) | Pravopisna pogreška u stručnom nazivu u sveučilišnom priručniku. | Zamijeniti u u15 i d01; D06 obnoviti. |
| 7 | `source/d01…md` r. 40 | Jedinice za $k$, $\varepsilon$, $\omega$, $\ell$ navedene su „-”; bezdimenzijski su samo $I_t$ i $m$. (lektura) | Netočnost u tablici koja služi kao referenca. | „m²/s²; m²/s³; s⁻¹; -; m; -” po redu veličina u retku. |

### P2 — vrijedi napraviti

| # | Gdje | Što (provjereno) | Zašto | Prijedlog |
|---|---|---|---|---|
| 8 | Naslovi odjeljaka zadataka: „Zadaci za vježbu” (12 pog.), „Zadaci za samostalan rad” (u05 r. 679, u13 r. 723); `filters/mf1-editorial-normalization.lua` r. 15–22; tijelo teksta | Izvor piše „Zadaci”, a Lua filtar u naslovima mijenja u „Zadatci”; u tijelu teksta „zadaci : zadatci” = 18 : 14 (malim slovom 3 : 2). Dva različita naslova odjeljka za isto mjesto u strukturi. | Pravopisno kolebanje i naslovna nedosljednost skrivena filtrom; D06 i ključ nasljeđuju izvor. | U izvoru svih 15 poglavlja `## Zadatci za vježbu`, u tijelu „zadatci”; zamjenu iz filtra ukloniti (ID-jevi odjeljaka ostaju). |
| 9 | Opisi slika (95 slika, svi `source/u*.md`) | Četiri obrasca za skice zadataka: „Skice uz Z1–Z6: …” (9), „Skice zadataka Z1–Z6: …” (u05), „Skice uz zadatke za vježbu — …” (u06, u07), „Skice vježbi: …” (u08, u14, u15). Uvodne slike: 8× „Pregled poglavlja: …” (3 s točkom, 5 bez; iza dvotočke čas veliko čas malo slovo) prema 7 opisnih rečenica. 39/95 opisa bez završne točke; 63/95 `fig-alt` doslovno jednak opisu. | Stil opisa slika vidljiv je na svakoj stranici sa slikom; ugovor slike traži alt koji govori o fizikalnoj poruci. | Jedan obrazac: uvodna slika = opisna rečenica s točkom (bez prefiksa „Pregled poglavlja:”), skice zadataka = „Skice uz Z1–Z6: …” s točkom; svi opisi završavaju točkom. Alt ostaviti jednak opisu gdje opis već govori o fizici (nije P1). |
| 10 | `source/u01…md` (Napomene uz skice Z1–Z6, 124 riječi; PDF str. 26), u06 (119; str. 123), u05 (112), u04 (107), u02 (107), u07 (105), u10 (99), u11 (97) | Medijan „Napomena uz skice” je 26 riječi, ali osam odlomaka ima 97–124 riječi (9–10 redaka ispod slike). Velik dio su rečenice o mjerilu („sile i pomaci nigdje nisu u mjerilu”, „Z2 ima vlastito mjerilo”) koje opće pravilo iz u00 r. 112 već pokriva. | Predugi tekst ispod slike zadataka otežava prijelom i ponavlja legendu. | Skratiti na ≤ 60 riječi: zadržati samo ono što se ne vidi iz skice (orijentacija, koji je presjek A/B, što nije nacrtano jer se traži); rečenice o mjerilu izbaciti jer ih pokriva u00. |
| 11 | `source/d03…md` r. 18, 24, 42, 60, 78, 96, …, 276 (`<span class="mf1-signal-chip">`, `<p class="mf1-signal-note">`); PDF str. 303–308 | U PDF-u „čipovi” ispadaju kao gole tekstne linije ispod naslova („ρ / γ / p F / A”, „μ / ν / σ cos θ”) i rečenica „Vizualne oznake za brzo snalaženje u dodatku…”, bez oblikovanja i bez funkcije. | Izgleda kao zaostatak; u webu su ukras bez navigacijske uloge. | Sakriti u `pdf`/`print` preko registra komponenti ili ukloniti u cijelosti (i rečenicu r. 18). |
| 12 | `source/d03…md` r. 292–348 („Kako koristiti pregled”, „Kriteriji provjere rješenja”, okvir „Najčešća pogreška”, „Operativna namjena dodatka”) | Četiri završna bloka (≈ 55 redaka) ponavljaju uvodni odlomak r. 3 i „Brzu provjeru” r. 7–16: tri faze uporabe, četiri kriterija, ista poruka „uredna algebra ne spašava pogrešan model” dvaput (r. 334 i r. 341). | Dodatak koji služi brzoj provjeri završava stranicom bez nove informacije. | Zadržati najviše „Kriteriji provjere rješenja” (4 koraka); ukloniti „Kako koristiti pregled”, okvir „Najčešća pogreška” i „Operativna namjena dodatka”. |
| 13 | `source/d02…md` r. 83–84, 102–103 | Abecedni red: „No-slip uvjet” stoji iza „Normalni udarni val” (treba ispred), „Rezidual” ispred „Reynoldsov broj” (treba iza). Naziv „No-slip uvjet” u poglavljima se ne pojavljuje (0 pojava „no-slip”; knjiga rabi „prianjanje”/„uvjet prianjanja”). | Pojmovnik se pretražuje abecedno; natuknica pod engleskim imenom ne pomaže čitatelju koji traži „prianjanje”. | Preimenovati u „Uvjet prianjanja (no-slip)” i smjestiti pod U; „Reynoldsov broj” ispred „Rezidual”. |
| 14 | `source/d02…md` r. 14 (Boussinesqov koeficijent → 10, 15), r. 20 (Coriolisov koeficijent → 8, 10, 15), r. 77 (MRF i klizajuća mreža), r. 97 (Preekspandirani i podekspandirani mlaz), r. 86, 98 | Pojmovi koji u ciljnim poglavljima nisu imenovani: „Boussinesqov” se u u10/u15 ne pojavljuje (u u12 r. 371 „Boussinesqova” je hipoteza o turbulentnoj viskoznosti, drugi pojam); „Coriolisov koeficijent” u u08 i u15 nije imenovan; „podekspandiran” 0 pojava; d04 r. 37 piše „klizna mreža”, d02 i u14 „klizajuća”; „Odbitak potiska” i „Pridružena masa” po jedna pojava. | Poveznica iz pojmovnika vodi u poglavlje gdje se naziv ne nalazi; dva naziva za istu stvar. | Ili dodati naziv u zagradi na mjestu prve uporabe u poglavlju (jedna riječ), ili natuknicu izbaciti; ujednačiti „klizna mreža” (d04) ↔ „klizajuća” (d02, u14). |
| 15 | `source/d02…md` (126 natuknica) | Nedostaju pojmovi koji su u knjizi istaknuti i česti: Bernoullijeva jednadžba (69 pojava, nema natuknice), Darcy–Weisbachova jednadžba / Darcyjev koeficijent (27), Peltonovo kolo (47), sifon (39), meniskus (25), reologija / nenewtonski fluid (53 / 7), Couetteov tok (10), Blasiusovo rješenje (15), energijska jednadžba (12), trokut brzina (7), afinitetni zakoni (6), specifična težina / relativna gustoća. | Pojmovnik ima natuknice za rubne pojmove (statvena cijev, zahvatni usis), a nema za središnju jednadžbu knjige. | Dodati 5–6 jednorečeničnih redaka (Bernoullijeva jednadžba, Darcy–Weisbachova jednadžba, Peltonovo kolo, sifon, meniskus, afinitetni zakoni) uz postojeće poglavlje kao odredište; ostalo ne širiti. |
| 16 | `source/d01…md` r. 58 (kormilarski stroj $M=2Fr$, $V=2As$), r. 63 (igla $p_{M,1}$, $p_{M,2}$), r. 72 (tlačni mjerač i ullage), r. 74 (tank u zavoju), r. 78 (separator), r. 83 (parabolični segment $A=HL/3$), r. 90 ($BM_{eq}$) | Sedam redaka sažetka formula zapravo su rješenja pojedinih zadataka (pog. 1 Z2, pog. 2 Z6, pog. 3 Z4, pog. 4 Z5/Z6, pog. 5 Z2, pog. 6 Z6), a ne opće relacije. | Sažetak formula gubi karakter podsjetnika i odaje postupak samostalnih zadataka (suprotno pravilu da skice i pomagala ne otkrivaju postupak). | Ukloniti iz A; opis postupka već postoji u smjernicama D06. |
| 17 | `source/d01…md` (potpunost) | Nedostaju relacije koje poglavlja rabe: jednadžba stanja $p=\rho RT$ i izentropska veza $p/\rho^\kappa=\text{konst.}$ (u09 r. 61), izotermna atmosfera (u03), Youngova jednadžba kontaktnog kuta (u02, podebljano), momenti tromosti ploha $I_G$ za pravokutnik, krug i trokut (u05; d03 r. 102 ih spominje) — bez njih se nijedan zadatak o centru tlaka ne može riješiti iz A. | Sažetak je nepotpun upravo tamo gdje ga student najviše treba. | Dodati redak s $p=\rho RT$, $p/\rho^\kappa$ u pog. 9 i redak s $I_G$ ($bh^3/12$, $\pi d^4/64$, $bh^3/36$) u pog. 3–6; po želji izotermnu atmosferu i Youngovu jednadžbu. |
| 18 | `source/d01…md` r. 86 ($m_se$); `source/u06…md` r. 198, 264–269, 474, 1088 ($m_ke$); u06 r. 1055 i `d06` r. 305 ($m_ae$) | Tri oznake za masu pomaknutog utega u pokusu nagibanja: $m_s$, $m_k$, $m_a$. | Ista veličina, isti pokus, tri simbola (jedan od njih u sažetku formula). | Jedna oznaka u u06, A i D06 (predlažem $m_u$ „uteg” ili zadržati $m_k$ koji prevladava). |
| 19 | Brojčane liste u matematici: `source/u02…md` r. 825 i `d06` r. 99 ($\tau=20,40,80\ \text{Pa}$), `u11` r. 960 i `d06` r. 557 ($\lambda_L=20,30$), `u10` r. 1115 i `d06` r. 507 ($(Q_2,Q_3)=(24,16)$), `u14` r. 346, 426 ($\vec c_1=(26,0)\ \text{m/s}$, $(31,0)$) | U hrvatskom zapisu „26,0” je decimalni broj; vektor $(26,0)$ m/s i popis $20,40,80$ Pa dvosmisleni su. | Student čita „26,0 m/s” kao jedan broj. | Odvajati točkom-zarezom ili razmakom: $(26;\,0)$, $\tau=20;\ 40;\ 80\ \text{Pa}$ (kako već radi u03 r. 784). |
| 20 | „konst.”: `d01` r. 99 i `u07` r. 325, `u09` r. 61, 216 (`\text{konst.}`); `u08` r. 3, `u15` r. 9 (`\mathrm{konst}`); `d04` r. 62 (`\mathrm{konst.}`); `u03` r. 125, `u08` r. 210 (prozno „= konst.” izvan matematike) | Četiri zapisa iste oznake. | Sitna, ali uočljiva nedosljednost (brief je izričito navodi). | Svugdje `\text{konst.}` unutar matematike. |
| 21 | „horizontalno/vertikalno” prema „vodoravno/okomito”: 51 : 100 i 117 : 93 pojava; najgušće u u05 (9), u08 (9), u10 (11); `d04` r. 144; `d01` r. 80 „vertikalna” uz r. 12 „vodoravnici” | Oba para supostoje i unutar istog dodatka. | Standard nazivlja ne određuje izbor, pa knjiga koleba. | Odabrati domaći par (vodoravno/okomito) jer ga već rabe legenda strelica i opisi skica; zamjena je mehanička (`horizontaln` → `vodoravn`, `vertikaln` → `okomit`/`uspravn` prema smislu). |
| 22 | `source/d05…md`, `references.bib` | Izdanja: White 7. izd. 2011 (aktualno 9. izd. 2021), Munson i sur. 6. izd. 2009 (aktualno 9. izd. 2021, Gerhart–Gerhart–Hochstein), Çengel–Cimbala 3. izd. 2014 (4. izd. 2018); Virag bez godine; `nasa-wind-boundaries` bez godine (u PDF-u [6] završava „Boundary Conditions“. ”); IMO IS Code naveden kao 2008 bez napomene o konsolidiranom izdanju 2020. Obostrana podudarnost citata i popisa: potvrđena (23/23). | Za postupak odobravanja recenzent gleda aktualnost udžbeničkih izvora. | Osvježiti tri izdanja i dopuniti godine; za IS Code dodati „s izmjenama do 2020.” u `note`. |
| 23 | `source/u00…md` r. 74 | „Kratki primjeri uvode pojedinu relaciju, a cjeloviti zadatci povezuju više koraka.” Ugovor je ukinuo prefikse „Kratki primjer —” / „Cjeloviti zadatak —”, pa razlika čitatelju nije vidljiva (0 pojava u poglavljima). | Uputa opisuje nešto što u knjizi više ne postoji. | Rečenicu ukloniti; zadržati drugu rečenicu o okvirima *Fizikalno značenje* i *Granica modela*. |
| 24 | `source/u00…md` r. 56 („CFD put: … → … → …”, 6 članova) i r. 76–81 (CFD okvir); `source/index.md` r. 34–36; `source/d04…md` r. 3–24 | Isti „put” od zakona do CFD-a opisan je na četiri mjesta u prvih deset stranica. | Ponavljanje na početku knjige; strelični lanac teško se čita u jednom odlomku. | U u00 zadržati samo CFD okvir (r. 76–81) i izbaciti rečenicu „CFD put”; u indexu izbaciti „Numerički pokusi” (vidi #3). |
| 25 | `source/index.md` r. 38–47 (Impresum) | „Verzija: 1.0-rc1, rujan 2026.” (knjiga se dovršava u listopadu), „Status: radno izdanje”, poveznice na GitHub dokumente `protokol_strucne_recenzije.md` i `protokol_studentskog_pilota.md` (postoje, ali su radni dokumenti). | Završna inačica priručnika ne bi trebala nositi radne protokole u impresumu. | Pri završetku: verzija 1.0 s datumom, status prema postupku odobravanja, zadržati samo poveznicu na erratu. |
| 26 | `source/d01…md` r. 1, `d02` r. 1, `d03` r. 1, `d04` r. 1, `d05` r. 1, `d06` r. 3 (prvi `##` u svakom dodatku); PDF sadržaj str. 4–5; web `d04…html` („D.1 Mehanika fluida i numerika — pregled”) | Svaki dodatak počinje H2 koji ponavlja ili preformulira naslov iz `book.json` („B. Pojmovnik / B.1 Pojmovnik”, „F. Ključ kontrolnih rezultata / F.1 Ključ smjernica i kontrolnih rezultata”, „D. Numerička mehanika fluida / D.1 Mehanika fluida i numerika — pregled”). | Dvostruki naslovi u sadržaju i tri različita imena za isti dodatak (book.json, H2, u00 r. 122–127). | Ukloniti prvi H2 u d01–d06 tako da uvodni odlomak stoji izravno ispod naslova dodatka; naslove dodataka u u00 r. 122–127 uskladiti s `book.json`. |
| 27 | `source/d04…md` r. 26–40 („Pojmovnik numeričkih metoda”) prema `d02` r. 19, 23, 74, 77, 100, 102, 105, 106 | FEM, RANS/LES/DNS, $k$–$\varepsilon$ / SST, SIMPLE/PISO, MRF/klizna mreža i rezidual definirani su i u B i u D (s različitim nijansama). | Dva pojmovnika za isti skup kratica. | U D zadržati samo kratice kojih nema u B (FVM, VOF, zidne funkcije/$y^+$, GCI) i uputiti na B; ili obrnuto, ali jedno mjesto. |

### P3 — opcionalno

| # | Gdje | Što | Prijedlog |
|---|---|---|---|
| 28 | `source/d01…md` r. 147 | Omjeri Froudeove sličnosti pisani kao $v_m/v_p$, $Q_m/Q_p$, $F_m/F_p$, ali snaga kao $P_p/P_m$. | Isti smjer omjera u svim članovima. |
| 29 | `source/d01…md` r. 14 i 27 ($K$ modul i kobilica), r. 27 i 38 ($M$ metacentar i moment), r. 117 ($p_b$ nedefiniran), r. 144 ($\sigma_{kr}$ bez referentnog mjesta) (lektura) | Potvrđeno. | Ublažiti „samo to značenje” i dodati $p_b$ u tablicu oznaka. |
| 30 | `source/d02…md` r. 124, 126 (Validacija, Verifikacija) | Jedine dvorečenične definicije („Postupak: dodatak D, @sec-cfd-venturi.”). | Drugu rečenicu premjestiti u stupac Odredište. |
| 31 | `source/d04…md` r. 166–169 (poveznice `../data/cfd/*/README.md`), r. 175–179 | U PDF-u poveznice na README su mrtve, u webu vode na sirovi Markdown; $C_D=0{,}01222408822$ i „$0{,}01166089$” s 10 znamenki djeluju pretenciozno u priručniku. | Poveznice označiti kao „paket `poiseuille_laminar` u repozitoriju”; brojeve zaokružiti na 4 značajne, provenijenciju ostaviti u `teaching_comparison.json`. |
| 32 | CFD blokovi pog. 1–7, 9, 10, 13–15 | Samo pog. 8, 11 i 12 upućuju na odjeljke dodatka D (`@sec-cfd-…`), iako urednički stil traži uputu iz poglavlja; D obrnuto pokriva svih 15 sidara (provjereno: sve poveznice iz tablice r. 7–12 postoje). | Po jedna poveznica na D u prvom CFD odlomku svakog lajtmotiva (pog. 1, 4, 5, 9) dovoljna je. |
| 33 | `source/u04…md` r. 201 | $\omega_{crit}^{ogol}$ miješa engleski i hrvatski indeks. | $\omega_{kr}^{ogol}$ ili $\omega_{ogol}$. |
| 34 | ID-jevi uvodnih slika: `fig-uvod-u07` u pog. 6, `fig-uvod-u08` u 7, `fig-uvod-u09` u 8, `fig-uvod-u11` u 10, `fig-uvod-u14` u 11, `fig-uvod-u12` u 14 | Naslijeđeni brojevi iz starog rasporeda; ugovor ih dopušta, ali zbunjuju pri održavanju. | Ne mijenjati (poveznice); zabilježiti u `docs/arhitektura.md`. |
| 35 | `source/u00…md` r. 69 | „mrežno izdanje uz njih nudi sklopive smjernice…, a u izdanju u PDF-u oni se nalaze u dodatku F” — dodatak F postoji i u webu. | „…smjernice i kontrolni rezultati nalaze se u dodatku F; mrežno izdanje ih prikazuje i uz sam zadatak.” |
| 36 | `docs/autorski_ugovor.md` (7 blokova) prema stvarnoj uporabi | `Temelj` je upotrijebljen jednom u cijeloj knjizi (u10), `Numerički pokus` u 4 poglavlja, `Dublje` u 5; `Fizikalno značenje` nema u u01 i u09. | Ili izbaciti tip `Temelj` iz ugovora i registra, ili ga ne spominjati u u00; nije nužno dodavati blokove. |
| 37 | PDF str. 317 (dodatak E) | Brojevi citata u tekstu dodatka idu [1], [21], [15], [22], [23], [2]… (redoslijed prve pojave u knjizi, ne u dodatku). Dojam. | Prihvatljivo za IEEE stil; alternativa je autor–godina stil u CSL-u. |
| 38 | Struktura odjeljaka: `## Riješeni primjeri` postoji u 11 poglavlja (u05 podijeljen na „ravne”/„zakrivljene plohe”), a u 9, 12, 15 primjeri su uz teoriju; 9 i 15 imaju dodatni odjeljak „Postupak analize …” prije zadataka | Dva legitimna obrasca; ne predlažem restrukturiranje, samo svijest da sadržaj PDF-a za 9/12/15 izgleda drukčije. | Ostaviti; eventualno u u00 „Struktura rada s poglavljem” reći da primjeri stoje uz teoriju ili u zasebnom odjeljku. |

## 3. Što je dobro i treba ostati

- **Notacija je provedena.** Pretraga svih izvora: nema `V` kao brzine, `\rho_w`, `h_w`, `\tau_w`, `C_w`,
  `g_{\mathrm{eff}}`; svih 60 pojava `$u$` izvan pog. 14 jesu brzine ploče, klipa ili stijenke (u02, u07,
  u10, u12), u skladu sa standardom; preostali latinski indeksi (`_{max}`, `_{ref}`, `_{eff}`, `_{loc}`,
  `_{th}`) standard dopušta. Jedina iznimka je #33.
- **Oznake zadataka i polja potpuno su ujednačene:** 180× „Tekst zadatka”/„Traži se”, 90× „Rješenje”/
  „Provjera i tumačenje”, 90 oznaka razine u istom obliku (30 T1, 30 T2, 15 T3, 15 T4), 15 pitanja
  „Zastani i promisli”, točno 6 zadataka po poglavlju.
- **Dodatak C odgovara stvarnim zadatcima:** sve oznake (Z2–Z6) u 15 odjeljaka provjerene su prema
  naslovima i sadržaju zadataka u D06 — nema promašaja. Dvostupčani oblik „Česta pogreška / Što
  provjeriti” je koristan i treba ostati.
- **Dodatak A — točnost:** četrdesetak formula uspoređeno je s poglavljima i standardnim oblicima
  (kritični omjeri 0,833/0,528/0,634, normalni udarni val, Swamee–Jain, Hardy–Cross, Blasius,
  spregnute dubine, $GZ$ za okomite bokove, Froudeova sličnost, NPSH); nije nađena netočna relacija.
  Završni popis „Tipične zamjene… koje treba zaustaviti odmah” (r. 209–219) je kratak i koristan.
- **Dodatak D je nepretenciozan i pošten:** jasno razlikuje sintetičke pakete od stvarnog CFD-a i
  mjerenja (r. 164–173), tablica povezanih primjera (r. 7–12) s 15 sidara u poglavljima u potpunosti
  je ispravna, a odjeljak „Kada CFD ne treba” vrijedan je i rijetko viđen u priručnicima.
- **Literatura:** svih 23 ključa iz `references.bib` citirano je u tekstu i obrnuto; tematski uvod u E
  (umjesto golog popisa) čitatelju govori što otkud dolazi.
- **Ključ F:** nema prekinutih rečenica (svi odlomci završavaju interpunkcijom), svaka stavka ima
  povratnu poveznicu, smjernice ne prepisuju rješenje. Jedini problem je #2.
- **Legenda strelica u u00** (r. 100–112) kratka je, točna i odgovara standardu od 14. listopada; tablica
  razina T1–T4 jasna je i treba ostati.

## 4. Što se može ukloniti ili skratiti bez gubitka

1. `index.md` r. 5–9 (Typst-only uvod) i r. 26–36 („O priručniku”, „Numerički pokusi”) — sve već stoji
   u u00 (#3).
2. u00 r. 56 („CFD put”) i r. 74 (prva rečenica o kratkim primjerima i cjelovitim zadatcima) (#23, #24).
3. d03 r. 292–348: tri od četiri završna bloka (#12) i svi „čipovi” r. 18, 24, 42, … (#11).
4. d01: sedam zadatkovno specifičnih redaka (#16).
5. d04 r. 26–40: pojmovnik kratica, ako se zadrži u B (#27); 10-znamenkasti brojevi r. 175–179 (#31).
6. Prozni sažetci u pog. 1–5 i 13 — pretvoriti u natuknice, čime se u svakom poglavlju štedi pola
   stranice (#4); „Kamo dalje nakon MF1” u u11.
7. Osam najdužih „Napomena uz skice” (97–124 riječi) skratiti na ≤ 60 riječi (#10).
8. Prvi H2 u svakom dodatku (#26).

## 5. Provjere koje su izvršene i ograničenja

- Automatske pretrage izvora (`source/*.md`): oznake, nazivlje, naslovi odjeljaka, blokovi, oznake
  razina i polja, opisi slika, duljina napomena, abeceda pojmovnika, prisutnost pojmova u poglavljima,
  podudarnost `references.bib` ↔ citati, postojanje svih sidara iz dodataka A–E i u00 (nijedno ne nedostaje).
- PDF: sadržaj (TOC) i tekst stranica 2, 5–8, 20, 26, 123, 287, 296, 303, 317–318, 327; snimke u
  `scratchpad/recenzija/struktura_i_dodaci/`. Web: naslovi i poveznice u `index.html`, `u00…html`,
  `d04…html`, `d06…html`.
- Nisam provjeravala brojčane rezultate zadataka ni fizikalnu točnost poglavlja (izvan područja);
  formule u A provjerene su po obliku, ne ponovnim računom primjera. Nalaz #1 (decimalni zarez)
  zahtijeva provjeru u Typst lancu prije ispravka; ponudila sam mehanizam, ne gotov kod.
