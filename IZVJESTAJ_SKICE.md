# Izvještaj o fizikalnom pregledu skica

Datum: 13. listopada 2026. · Grana: `popravak-skica`

## Opseg i postupak

- **95 referenciranih SVG skica** iz `assets/print/` u 15 poglavlja. Svaki panel višepanelnih skica (uvodni pregledi, vježbe Z1–Z6) pregledan je kao zasebna skica.
- **17 bilježnica** (`notebooks/`), uključujući tri interaktivna laboratorija.
- U `web/`, `filters/`, `includes/`, `components/` i `source/` nema drugih crteža (canvas, inline SVG, Mermaid, TikZ).

Za svako poglavlje najprije je iz stvarnog teksta sastavljen rječnik oznaka. Objedinjen je u [RJECNIK_OZNAKA.md](RJECNIK_OZNAKA.md), a mjerodavni standard ostaje [urednički stil](docs/urednicki_stil.md).

Svaka skica zatim je prošla isti slijed:

1. čitanje teksta zadatka ili primjera, rješenja i jednadžbi;
2. render u PNG i pregled;
3. pisana analiza prije izmjene: problemi, tablica vektora i tablica oznaka;
4. minimalan ispravak kanonskog SVG-a u postojećem stilu;
5. ponovni render i pregled;
6. geometrijski checker poglavlja (`tools/check_uNN_sketch_geometry.py`) i `tools/audit_sketch_design.py`.

Tablica vektora sadrži, za svaki vektor:

- oznaku i veličinu;
- očekivani i nacrtani smjer;
- očekivanu i nacrtanu relativnu duljinu;
- status.

Tablica oznaka uspoređuje svaku oznaku sa skice s tekstom, znak po znak. Pune analize za svaku skicu nalaze se u `docs/radno/skice-2026-10/uNN.md` i `notebooks.md`.

Tekst zadataka, brojevi, rješenja i ID-jevi nisu mijenjani (`source/*.md` nije diran). Proturječja i dvoznačnosti nisu rješavani pogađanjem, nego su izdvojeni na kraju ovog izvještaja.

## Rezultat

| Skupina | Pregledano | Ispravljeno | Bez promjene |
|---|---:|---:|---:|
| SVG skice | 95 | 94 | 1 (`u02_fig_kapilarni_uspon_etanol`) |
| Bilježnice | 17 | 13 (samo kod crteža: osi, legende, oznake, strelice) | 4 |

Najčešće vrste ispravaka:

1. **Duljine vektora protiv brojeva iz teksta.** Primjeri:
   - kontinuitet: brzina u užem presjeku bila je kraća (pog. 7, 8, 10, 13, 15);
   - G < F_L uz G = 2F_L (pog. 1);
   - jednake sile kočnih cilindara (pog. 1);
   - težina i uzgon nisu bili jednaki kod plivanja, a u Z1 je G bila dulja od F_U iako je F_U > G (pog. 6);
   - nerazmjeran dijagram sile na koljeno (pog. 10);
   - trokuti brzina s u > c₁ (pog. 14).

   Gdje pravi omjer nije čitljiv (npr. 1 : 35), zadržan je točan poredak, a to je zabilježeno.
2. **Fizikalne greške geometrije.** Primjeri:
   - more nacrtano s unutarnje strane broda (pog. 3, pog. 8);
   - sile F_H, F_V i F_R prolazile su kroz poklopac ili u pod (pog. 5);
   - sapnica nacrtana s A_e/A* ≈ 12,5, a primjer traži 1,6 (pog. 9);
   - nagib linijskog gubitka EGL/HGL bio je različit u istoj cijevi (pog. 13);
   - cijevi petlje istog promjera unatoč D = 150/100/125/150 mm (pog. 13);
   - kontrolni volumen obuhvaćao je vanjsko more (pog. 7);
   - Peltonov krak r nije završavao na osi mlaza (pog. 14);
   - nespojeni vodovi manometra (pog. 3).
3. **Oznake usklađene s tekstom i standardom.** Primjeri:
   - p → p_M, p₀ → p_atm ili p_pov, p_abs → p_aps;
   - G_uk → mg, C_d → C_D, α (kut) → θ;
   - „u = 0” na nepomičnoj stijenci → „v = 0”;
   - R_γ (Unicode gama) → R_y;
   - uklonjene oznake kojih nema u tekstu;
   - dodani zadani podatci koji su nedostajali.
4. **Tehnički zapis.** Unicode indeksi zamijenjeni su pravim `tspan` indeksima. Uklonjeni su znakovi ↑↓, koje preglednik crta kao emoji. Opisi (`<desc>`) koji su opisivali staru shemu boja ili nepostojeće panele su ispravljeni.
5. **Skice zadataka koje su otkrivale traženi rezultat.** Uklonjeno je ono što je to izravno činilo: „−a/+a” (pog. 9 Z1), smjer sile T (pog. 5 Z3), „e ulijevo” (pog. 6 Z6). Ostali slučajevi traže tvoju odluku.

Checkeri su usklađeni s ispravljenom geometrijom i postroženi; nijedna provjera nije oslabljena.

- **Pog. 1 i 2:** dodane provjere omjera sila i brzine ploče.
- **Pog. 7:** novi KV u P2.
- **Pog. 9:** provjera „simetričan uzdužni profil” zamijenjena je strožom provjerom (D_e/D*)² = 1,6 ± 1 %.
- **Pog. 11:** v_m < v_s i v₂ > 2v₁.
- **Pog. 13:** promjeri cijevi i kote padova EGL-a.
- **Pog. 14:** krak r na osi mlaza.

## Provjere

- Geometrijski checkeri svih 15 poglavlja i `tools/audit_sketch_design.py`: PASS (95 figura).
- Tiskovne izvedenice obnovljene iz kanonskih SVG-ova; `tools/audit_print_layouts.mjs`: PASS (95 figura, 2060 oznaka, bez preklapanja i rezanja, slova od najmanje 9 pt).
- Bilježnice: `tools/test_interactive_labs.py` 12/12; izvršavanje 17/17 bez greške.
- Puni lokalni objavni CI `scripts/check_publication.py`: **PASS (756 s)** nad radnim stablom s ovim ispravcima.
  - PDF ima 324 A4 stranice (prije 323).
  - `_book` i `_site/downloads` imaju isti SHA-256 (`9b510d0844df1c43…`).
  - Lokalni pregled: <http://127.0.0.1:8000/>.
- Svaka izmijenjena skica pregledana je kao PNG prije i poslije izmjene. Konačni PDF pregledan je samo na uzorku stranica, ne u cijelosti.
- Prolaz CI-ja i checkera potvrđuje geometriju i usklađenost oznaka koje provjere pokrivaju. Ne dokazuje didaktičku kvalitetu skica.
- Commiti: nijedan nije napravljen. Necommitane recenzentske izmjene i ispravci skica nalaze se zajedno u radnom stablu, pa zaseban commit po poglavlju čeka tvoju odluku o baznom commitu. Stanje svih SVG-ova prije pregleda sačuvano je izvan repozitorija.

## Tablica po skicama

Status: **ispravljeno** / **provjereno, bez promjene** / **odluka** (treba tvoju odluku; skica je ostavljena kako je opisano).

### Poglavlje 1 — osnove fluida i pascalov zakon

Detaljna analiza: [docs/radno/skice-2026-10/u01.md](docs/radno/skice-2026-10/u01.md)

| skica | problem | ispravak | status |
|---|---|---|---|
| u01_fig_uvod_pregled | p preko stijenke kanala | p u oba cilindra | ispravljeno |
| u01_fig_gustoca_sr | kota h nije u tekstu; V podebljan | h uklonjen; V normalan; checker zamijenjen jednakom provjerom | ispravljeno |
| u01_val1_klip_manometar | p umjesto p_M; d_k preko klipnjače; A_k lebdi; boje u desc; F₂/G | p_M ×2; premještene oznake; desc; F₂ 90 px | ispravljeno |
| u01_val2_hidraulicna_dizalica | p umjesto p_M; ↑/↓ emoji; „hidraulična” | p_M ×2; bez ↑/↓; naslov | ispravljeno |
| u01_ch1_dvostruka_platforma_manometar | G < F_L (G = 2F_L); s_L/s_h 3,33 umjesto 7,2; p; s_h razdvojen; „pumpa” | G 62/F_L 31/F_p 22; kota s_L 13,89 px; p_M; s_h = 180 mm; crpka | ispravljeno |
| u01_fig_kocnica_vozila | F_f = F_r; poredak sila; oznake preko cijevi; p | 24/30/36/49 px; oznake uz cijevi; p_M | ispravljeno |
| u01_vjezbe_skice Z1–Z4 | — | — | provjereno, bez promjene |
| u01_vjezbe_skice Z5 | F_p = F_L po duljini | 20 / 36 px | ispravljeno |
| u01_vjezbe_skice Z6 | nedostaje d | oznaka d | ispravljeno |

### Poglavlje 2 — viskoznost povrsinska napetost i kapilarnost

Detaljna analiza: [docs/radno/skice-2026-10/u02.md](docs/radno/skice-2026-10/u02.md)

| skica | problem | ispravak | status |
|---|---|---|---|
| u02_fig_uvod_pregled | „u = 0” na nepomičnoj stijenci; u ≠ v(δ); F ≠ F_v; σ i fluid bez oznake | v = 0; u = 194,9 px; F = F_v; oznake σ, ulje; desc | ispravljeno |
| u02_fig_kinematicka_viskoznost | isto + nema μ, ρ; zastarjeli desc | isto + μ, ρ, ulje; desc | ispravljeno |
| u02_val2_viskoznost_kapilarnost | „v = 0,90 m/s” umjesto u; „u = 0”; duljine | u = 0,90 m/s; v = 0; duljine; desc | ispravljeno |
| u02_fig_kapilarni_uspon_etanol | — | — | provjereno, bez promjene |
| u02_ch1_kapilarni_mikrodozator_kapljica | „hcap”; tekst preko stijenki; nema σ, θ | h_cap; premještene oznake; σ, θ = 0°; desc | ispravljeno |
| u02_fig_lezaj_temperatura | „čahura: u = 0”; u ≠ v; τ₁ = τ₂ po duljini; „Motpor” | v = 0; u 150 px; τ₁ 100 / τ₂ 24; M₁, M₂; desc | ispravljeno |
| u02_vjezbe_skice Z1 | u ≠ v(δ); F ≠ F_v; fluid | duljine; glicerin | ispravljeno |
| u02_vjezbe_skice Z2 | p_atm nije označen | p_atm | ispravljeno |
| u02_vjezbe_skice Z3 | F < F₁ (F = F₁ + F₂); u | F 96 px; u 90 px | ispravljeno |
| u02_vjezbe_skice Z4 | — | — | provjereno, bez promjene |
| u02_vjezbe_skice Z5 | „u = 0”; F ≠ F_v; u | v = 0; F = F_v = 38; u 96,9 | ispravljeno |
| u02_vjezbe_skice Z6 | p₀ (zaustavni tlak) za okolni zrak | p_atm; H = 42 mm | ispravljeno |

### Poglavlje 3 — hidrostaticka raspodjela tlaka i manometrija

Detaljna analiza: [docs/radno/skice-2026-10/u03.md](docs/radno/skice-2026-10/u03.md)

| skica | problem | ispravak | status |
|---|---|---|---|
| u03_fig_uvod_pregled | p_0 umjesto p_pov; „hidrostatska”; tlačne strelice prelaze hipotenuzu; p_g; plin u dvije boje; otvoreni krajevi vodova; nedostaje ρ | p_pov, „hidrostatička”, strelice = p_M(h), p_pl, jedna boja plina, filtar, ρ | ispravljeno |
| u03_fig_zatvoreni_spremnik_tlak | p_G,m; „zrak”; 1,4 m; hod ne doseže A | p_M,pl, „plin”, 1,40 m, hod do razine A | ispravljeno |
| u03_val1_diferencijalni_manometar | zrak u boji ulja; nema ρ_v, ρ_mv, ρ_zr | boja plina, oznake gustoća | ispravljeno |
| u03_ch1_zatvoreni_spremnik_ulje_ziva | U = 2,31 m umjesto U_m; nema p_M,dno | U = ?, U_m = 2,31 m, p_M,dno = 141,0 kPa | ispravljeno |
| u03_fig_pumpa_usis | „pumpa”, p_abs, plutajuće oznake i vodilica kroz crpku, natpis preko cijevi, siva tlačna boja | crpka, p_aps, oznake uz U, premješten natpis, `#356b83` | ispravljeno |
| u03_fig_balastni_tank | more unutar broda; tlačne strelice nisu proporcionalne; bez oznake stanja A | unutrašnjost broda, 0,7 px/kPa, p^A | ispravljeno |
| u03_vjezbe_skice | Unicode indeksi; plin u boji ulja; zrak u boji stijenke; oznake A, a, C bez uporišta; p_M „na dnu” | tspan, boje, uklonjene oznake, p_M,A | ispravljeno |
| u03_balans_tlaka_i_geff | α umjesto θ; g u boji konture; a ≠ |−a|; vrhovi izvan trokuta; kanal bez stijenke | θ, boja, duljine, vrhovi, stijenka | ispravljeno |

### Poglavlje 4 — relativno mirovanje fluida

Detaljna analiza: [docs/radno/skice-2026-10/u04.md](docs/radno/skice-2026-10/u04.md)

| skica | problem | ispravak | status |
|---|---|---|---|
| u04_fig_uvod_pregled | tlocrtna putanja čini a uzdužnim; obrnut trup; a > g_eff; kota Δh/2 s dva ista vrha; „separator” uz gravitacijski paraboloid; g ≠ komponenta g_eff; plutajući h_C/h_R | putanja uklonjena, trup, duljine, kota, naslov, g = 35 px, kote h_C/h_R | ispravljeno |
| u04_val2_laboratorijska_kolica | g u boji konture; a = 3 × g; Unicode h₀ | boja, a < g, tspan | ispravljeno |
| u04_val3_kosa_stijenka | plin u boji tekućine; g u boji konture; a = 4 × g; H bez veze s A | boje, a < g, pomoćna crta | ispravljeno |
| u04_fig_rotirajuci_cilindar | a ≠ prividna sila po duljini; formula u skici; nedostaje tijelo sile | 80 = 80 px, natpisi | ispravljeno |
| u04_ch1_rotirajuci_spremnik_paraboloid | natpisi preko krivulja i kota | premješteni natpisi | ispravljeno |
| u04_fig_autocisterna_kocenje | strelica vožnje u boji konture; simbol v | boja, „smjer vožnje” | ispravljeno |
| u04_vjezbe_skice | Unicode h₀; v u boji konture; α u legendi Z6; L = 1,8 / 1,4 m; zastarjeli opis boja | tspan, boja, „ω = 0,80 ω_max”, 1,80 / 1,40 m, opis | ispravljeno |

### Poglavlje 5 — hidrostatske sile na plohe

Detaljna analiza: [docs/radno/skice-2026-10/u05.md](docs/radno/skice-2026-10/u05.md)

| skica | problem | ispravak | status |
|---|---|---|---|
| u05_fig_uvod_pregled | lažna slobodna površina na suhoj strani; F_R umjesto F; h_t; tekst preko crta; zastarjeli desc | uklonjena crta; F; h_1; razmaknuti natpisi; desc | ispravljeno |
| u05_val1_pravokutna_zaklopka | tlačne strelice nisu ∝ dubini; trapez 2,44 umjesto 2,5; p₀ (zaustavni) umjesto p_atm; p₁/p₂ i z nisu u tekstu | strelice i trapez ∝ dubini; p_atm; ρgh_1, ρg(h_1+H); h_CP−h_1 | ispravljeno |
| u05_val3_kosi_poklopac | T:F 0,70 umjesto 0,566; vrh T u simbolu B; h A razmak; nema b | T skraćena, vrh odmaknut; indeks; b = 0,90 m | ispravljeno |
| u05_ch1_pregrada_ulje_voda | H, D, p₁, pD nisu u tekstu; RA bez indeksa, na slobodnoj površini; T:R_A 1,5 umjesto 2,09 | oznake iz teksta; R_A premještena i skraćena; tspan | ispravljeno |
| u06_val1_cetvrtina_kruga | F_H i F_V prolaze kroz plohu; F_V:F_H 0,77 umjesto 1,11; unicode-strelice; h₁ preko stijenke | vrhovi na plohi; omjer; natpisi | ispravljeno |
| u06_val3_cetvrtcilindricni_poklopac | F_H, F_V, F_R kroz poklopac i pod; F_R ne kroz O; omjeri; A/B nisu u tekstu | sve iz vode do plohe; F_R kroz O; omjer 1:1,57:1,86; oznake | ispravljeno |
| u06_ch1_poklopac_spojnica | F_H kroz plohu; F_V:F_H 0,75; T≠F_V; D nije u tekstu; unicode-strelice | vrh na plohi; omjeri (T=F_V); D uklonjen | ispravljeno |
| u05_vjezbe_skice | Z3 otkriva smjer T (traženi rezultat); Z5 bez kote h_1; unicode-indeksi; L/h_D uz crte; desc „smeđe kote” | Z3 spojnica bez smjera; kota h_1; tspan; oznake; desc | ispravljeno |

### Poglavlje 6 — uzgon plivanje i stabilnost

Detaljna analiza: [docs/radno/skice-2026-10/u06.md](docs/radno/skice-2026-10/u06.md)

| skica | problem | ispravak | status |
|---|---|---|---|
| u07_fig_uvod_pregled | plutajuće legende s unicode-strelicama; F_U ≠ G pri plivanju; unicode-indeksi | natpisi uz strelice; jednake duljine; tspan; desc | ispravljeno |
| u07_fig_pumpno_kuciste | F_U i G nacrtane jednako (stvarno G = 1,84 F_U); „shema sila” preko strelice; V umjesto V_ist; nema osi z | omjer 1:1,84; natpis uklonjen; V_ist; os z | ispravljeno + treba odluku (sila držanja) |
| u07_val2_ponton_gaz | G_uk nije u tekstu; mg ≠ F_U; H daleko od kote; nema L, ρ | mg = F_U; H uz kotu; L, ρ | ispravljeno |
| u07_val1_platforma_kompresor | G_uk; težina ≠ F_U; kote e i B bez pomoćnih crta; „more” | (m_p+m_k)g; pomoćne crte; ρ, L | ispravljeno |
| u07_ch1_platforma_ulje_voda_ormar | G_uk; težina ≠ F_U; „180 kg”; T_D na razdjelnici; „ulje” na koti; kote bez pomoćnih crta; nema ρ_o, ρ_w | sve navedeno ispravljeno | ispravljeno |
| u07_ch2_poplavljen_tank | B_t preko palube; kote bez pomoćnih crta; e_t nije nacrtan | natpis premješten; pomoćne crte | ispravljeno + treba odluku (e_t) |
| u07_vjezbe_skice | Z1 obrnut poredak G/F_U (ΣF≠0); Z4 areometri nisu isti; Z6 δ/T_D preklopljene, „e ulijevo”; nedostajući podatci; unicode | omjeri; isti areometri; razmaknute kote; podatci; tspan | ispravljeno |

### Poglavlje 7 — kinematika kontrolni volumen i kontinuitet

Detaljna analiza: [docs/radno/skice-2026-10/u07.md](docs/radno/skice-2026-10/u07.md)

| skica | problem | ispravak | status |
|---|---|---|---|
| u08_fig_uvod_pregled | $m_{CV}$; komora bijela, priključci plavi; bold skalari; natpis preko KP; normale u pomoćnoj boji | $m_{KV}$, jedinstvena ispuna, `tspan`, preslagan natpis, normale `#356b83` | ispravljeno |
| u08_fig_kinematika | vektori u boji konture, strujnice u boji vektora; oznaka v daleko od vektora | zamijenjene uloge boja, oznaka uz vektor | ispravljeno |
| u08_fig_t_komad_hidraulika | $v_2$ kraći od $v_1$; nema 60/40 %; KV preko stijenke | strelice u mjerilu, udjeli, oznake pomaknute | ispravljeno |
| u08_kontrolni_volumen_scene | omjer strelica 2 umjesto $(D_1/D_2)^2$ | $D$ 2 : 1, strelice 1 : 4, d$h$/d$t$ | ispravljeno |
| u08_val1_difuzor_kontinuitet | natpis $v_2$ preko presjeka/KV; jednake pomoćne strelice | preslagan natpis, skraćene strelice | ispravljeno |
| u08_val3_izjednacni_spremnik | pravokutni KV s vanjskim morem; omjer $v_s:w$ 2,3 | KV duž kanala; 7,4 : 1; oplata cijelom širinom; checker pojačan | ispravljeno |
| u08_ch1_mijesajuci_spremnik | $Q_A=Q_B$ strelice; nedostaju $L,b,\rho_A,s_B$ | strelice 18 : 6 : 14, podatci | ispravljeno |
| u08_vjezbe_skice | Z1/Z4 KV mimo presjeka; Z4 promjeri i $v_2=2v_3$; Z3/Z6 protoci; Z5 $u$, $Q_{in}$; Z2 boje | sve ispravljeno u postojećem rasporedu | ispravljeno |

### Poglavlje 8 — energijska jednadzba i bernoulli

Detaljna analiza: [docs/radno/skice-2026-10/u08.md](docs/radno/skice-2026-10/u08.md)

| skica | problem | ispravak | status |
|---|---|---|---|
| u09_fig_uvod_pregled | oznake v na stijenci; nema presjeka 1, 2; desc | pomaknute oznake, 1/2, desc | ispravljeno |
| u09_egl_hgl_schema | $v_2$ u stijenci; $v_2^2/(2g)$ daleko od kote | preslagane oznake | ispravljeno |
| u09_val2_slobodni_mlaz | h1/h2/h3 dvosmisleni, bez indeksa; $v_0$ neoznačen | oznake uz kote, $v_0$ | ispravljeno |
| u09_val3_idealni_sifon | indeksi; nejednake brzine; desc o HGL-u | `tspan`, 55/55/55, v, desc | ispravljeno |
| u09_ch1_bypass_sifon_suzenje_mlaz | dno trupa ispod mora | dno unutar broda, more ispod | ispravljeno |
| u09_fig_venturijeva_cijev | strelice 1 : 3,35 umjesto 1 : 4; indeksi | 20 : 80, indeksi | ispravljeno |
| u09_vjezbe_skice | Z1 prestrma parabola; Z2/Z6 omjeri brzina; Z4 skriven natpis, lažna stijenka, „st”; Z5 „abs”; Z6 $z_C$ | ispravljeno; Z5 omjer → odluka | ispravljeno / treba odluku (Z5) |

### Poglavlje 9 — kompresibilni idealni tok

Detaljna analiza: [docs/radno/skice-2026-10/u09.md](docs/radno/skice-2026-10/u09.md)

| skica | problem | ispravak | status |
|---|---|---|---|
| uvod, panel sapnica | A_e/A* nacrtano ≈ 12,5 (osnosim.) umjesto 1,6 iz P6 | grlo 64 px, izlaz 81 px, ulaz 120 px | ispravljeno |
| uvod, panel sapnica | „A_e, p_b” na izlaznom presjeku (p_b ≠ p_e) | A_e uz izlaz, p_b izvan sapnice | ispravljeno |
| uvod, panel sapnica | grlo bez Ma = 1 | „A*, Ma = 1” | ispravljeno |
| uvod, desc | „ukupni tlak” | „zaustavni tlak” | ispravljeno |
| vježbe Z1 | „−a/+a” otkriva traženi rezultat | oznake „a” | ispravljeno / treba odluku (alternativa) |
| vježbe Z2 | vod iste širine kao A* (nemoguće širenje do p_b) | vod 40 px, zatvorena stepenica | ispravljeno |
| vježbe Z3, Z4 | – | – | provjereno, bez promjene |
| vježbe Z5 | unicode indeksi | tspan | ispravljeno (oznake) |
| vježbe Z6 | Pitotov otvor 18 px iza presjeka 2; „otvor ←” odvojen; „ukupni tlak” | otvor u presjeku 2, vodilica, desc | ispravljeno |
| check_u09 | „simetričan profil” kodirao nefizikalnu geometriju; Z2 vod = A* | zamijenjeno provjerom A_e/A* = 1,6 ± 1 % i „vod širi od A* bez procjepa” | usklađeno (strože) |

### Poglavlje 10 — kolicina i moment kolicine gibanja

Detaljna analiza: [docs/radno/skice-2026-10/u10.md](docs/radno/skice-2026-10/u10.md)

| skica | problem | ispravak | status |
|---|---|---|---|
| svih 9 | unicode indeksi; „Rᵧ/Fᵧ” = gama | tspan; R_y, F_y | ispravljeno |
| uvod | v₁ > v₂ uz A₁ > A₂; G izvan težišta | v₁ 34 px; G iz težišta (226; 222) | ispravljeno |
| P1 Pelton | w kraći od u (18 > 12) | v : u : w = 100 : 40 : 60 | ispravljeno |
| P2 mlaznica | tlačna strelica bez oznake; „215 N” bez F_P | p_M1A_1, F_P; p_M1 uz presjek 1 | ispravljeno |
| P3 koljeno | v₁ > v₂; F_x : F_y = 3,66 umjesto 2,11; desc „crveni” | v₁ 34; 80 : 37,9; oznaka p_M1A_1 | ispravljeno |
| P4 T-račva | v₁ ≈ v₂ ≠ v₃ | 34 : 77 : 77 | ispravljeno |
| P5 Y-račva | obrnut poredak brzina; v₃ na stijenci; luk kroz krutinu | 40 : 70 : 70; luk r = 25; oznake | ispravljeno |
| P6 hidro koljeno | v₁ ≠ v₂; p_M1/p_M2; L/s; „60°” | jednake; p_M; m³/s; θ = 60° | ispravljeno |
| P7 rot. mlaznica | u ≈ w (omjer 11,3) | u 22 px | ispravljeno |
| Z1 | v_s = v_j po duljini | 36 : 64 | ispravljeno |
| Z2 | v_d najkraća; cijev pretjerano suzena | 6 : 7 : 8; D 86,4/80/74,8 | ispravljeno |
| Z3 | v₁ ≠ v₂; L/s | jednake; 0,026 m³/s | ispravljeno |
| Z4 | „18 m/s” | „18,0 m/s” | ispravljeno |
| Z5 | u predug, v₂ prekratak | 75 : 30 : 54 | ispravljeno |
| Z6 | v₁ najdulji; luk 60° kroz krutinu; L/s | 46 : 67 : 56,5; luk u fluidu; 0,040 m³/s | ispravljeno |
| check_u10 | – (sve izmjene unutar postojećih provjera) | bez izmjene | PASS |

### Poglavlje 11 — dimenzijska analiza i slicnost

Detaljna analiza: [docs/radno/skice-2026-10/u11.md](docs/radno/skice-2026-10/u11.md)

| skica | problem | ispravak | status |
|---|---|---|---|
| u14_fig_uvod_pregled | desc „tri panela”; zrak/krutina zamijenjene boje; neujednačeni parovi; „napetost”; strelica do tijela; model bez veze s prototipom | desc, boje materijala, ujednačeni parovi, „površinska napetost”, strelice odmaknute, „model: Re_m = Re_p” | ispravljeno (+odluka 2) |
| u14_fig_pi_buckingham | desc: F umjesto F_D, C_d umjesto C_D | desc | ispravljeno (matrica točna) |
| u14_fig_odluka | marker zakrenut (vrh ulijevo); logičke strelice u boji vektora; σkav bez indeksa; poravnanje; tekst koraka 2 | marker, stil strelica, σ_kav, poravnanje, „Režim ili trenje uz stijenku” | ispravljeno |
| u14_val1_reynolds_kanal | ν bez indeksa v/u; znamenke ≠ tekst | ν_v, ν_u; 1,2; 1,0·10⁻⁶; 4,0·10⁻⁵ | ispravljeno |
| u14_val2_brod_bazen | Unicode indeksi; v_m = v_s po duljini | tspan; 100 / 40 px | ispravljeno |
| u14_val3_venturi_kavitacija | „p_aβs”; „m_odelu”; v₂ ≈ v₁; oznake odvojene; p_v crta kao krivulja; nema 0; 6,00 | p_aps, tekst, v₁ 40 / v₂ 100 px, oznake uz elemente, p_v sivo, 0 i minus, 6,0 | ispravljeno |
| u14_val4_kap_raspad | v_rel ≠ tekst; nema ρ_zr, ρ_v; g nije u vektorskom stilu | v, gustoće, g `#356b83` | ispravljeno |
| u14_ch1_kugla_struja | C_d umjesto C_D; „model”; nema ρ, ν | C_D, „korelacija”, podatci zraka | ispravljeno |
| u14_val5_mach_strouhal | „plinski vod · lokalni Q”; „Ma = 0,3” kao natpis; oznake odvojene; nema St, f_n | „Zračni vod”, os „Ma”, oznake uz kote/strelice, St i f_n | ispravljeno |
| u14_vjezbe_skice | Z2 0,50; Z3 100 kPa, nema ρ; Z4 profili u boji fluida, nedostaju podatci, oznake brzina odvojene; Z5 oznaka v; Z6 F bez oznake, b_m nije u tekstu, nedostaju podatci | brojevi, ρ, boja krutine, podatci, oznake uz strelice, F_m, b_m uklonjen | ispravljeno (+odluka 1) |

### Poglavlje 12 — diferencijalni opis realnog toka

Detaljna analiza: [docs/radno/skice-2026-10/u12.md](docs/radno/skice-2026-10/u12.md)

| skica | problem | ispravak | status |
|---|---|---|---|
| u12_fig_uvod_realni_tok | indeksi τxy, U∞, δ99 kao običan tekst/Unicode | tspan indeksi | ispravljeno |
| u12_realni_tok_vjezbe_skice Z1 | oznake „A”, „xA” nisu u tekstu; strelice bez oznake | „x = 1 m”, „v(x, t)”, bez „A” | ispravljeno |
| … Z2 | — | — | provjereno, bez promjene |
| … Z3 | p₁, p₂ Unicode | tspan | ispravljeno |
| … Z4 | — | — | provjereno, bez promjene |
| … Z5 | Ue, dUe/dx, ks bez indeksa | tspan | ispravljeno |
| … Z6 | hf bez indeksa | tspan | ispravljeno |

### Poglavlje 13 — gubici cjevovodi crpke i mreze

Detaljna analiza: [docs/radno/skice-2026-10/u13.md](docs/radno/skice-2026-10/u13.md)

| skica | problem | ispravak | status |
|---|---|---|---|
| u13_fig_uvod_pregled | strelice Q/Q1/Q2 protivne kontinuitetu; desc; indeksi; h_CD bez kote | duljine; desc; tspan; kote h_AC, h_CD, h_DB (Dopuna) | ispravljeno |
| u10_fig_uvod_pregled | različit nagib linijskog gubitka uzvodno/nizvodno od ventila u istoj cijevi; nejednake brzine u koljenu; p₂,man; hw, hl | jednak nagib EGL/HGL, kota i oznaka v²/2g; strelice koljena 44/44; p_M,2; indeksi | ispravljeno |
| u13_ch1_serijsko_paralelna_mreza | strelice potrošnji nerazmjerne; bez oznaka Q_B…Q_D; jednake širine cijevi | 37/50/37 px; oznake; provrti 150:100:125:150 (Dopuna) | ispravljeno |
| u13_mreze_vjezbe Z1 | D u mm, p1−p2 umjesto Δp_dop | prema tekstu | ispravljeno |
| … Z2 | — | — | provjereno, bez promjene |
| … Z3 | strelice grana dulje od Q; jedinice; indeksi | 60/30 px; 0,020 m³/s; tspan | ispravljeno |
| … Z4 | H_s(Q)/H_p; Σξ = 6.; skica otkriva radnu točku | oznake | ispravljeno / treba odluku |
| … Z5 | nedostaje h_w ≤ 15 m; jedinice | dodano | ispravljeno |
| … Z6 | — | — | provjereno, bez promjene |

### Poglavlje 14 — turbostrojevi i propulzija

Detaljna analiza: [docs/radno/skice-2026-10/u14.md](docs/radno/skice-2026-10/u14.md)

| skica | problem | ispravak | status |
|---|---|---|---|
| u12_fig_uvod_pregled | u > c1 u prizoru; v_s broda ≠ v_s u kanalu; F_x bez primatelja; desc (3 panela, V0) | zajedničko mjerilo 3,75; v_s 32 px; „na lopaticu”; desc | ispravljeno |
| u12_val1_vodilica_mlaza | v2 nerazmjeran; nema h; sile bez primatelja | v2 49,9 px; h; „fluid → vodilica” | ispravljeno |
| u12_ch1_pokretna_zakrivljena_lopatica | u > c1, w2 > w1 u prizoru; naslov „vodilica” | mjerilo 3,2; „lopatica”; primatelj sile | ispravljeno |
| u12_ch2_pelton_rotor_moment | prizor nije u mjerilu; ω daleko od strelice; stil vrtnje | mjerilo 3; ω uz luk; siva strelica vrtnje | ispravljeno (krak r na osi mlaza — Dopuna) |
| u12_val3_pokretna_lopatica | nema r1 = 0,060 m; nejasan smjer +t | dodano | ispravljeno |
| u12_fig_relativni_dotok | p∞, p_d± nisu u tekstu | „tlak okoline”, „tlačni skok Δp_d” | ispravljeno |
| u12_vjezbe Z1 | oznaka na crti KV | pomaknuta | ispravljeno |
| … Z2 | |v2| ≠ |v1| unatoč tekstu; v1/v2 | 57 px; „v” | ispravljeno |
| … Z3 | u > c1 | mjerilo | ispravljeno / odluka |
| … Z4 | indeksi; skica otkriva trokute | indeksi | ispravljeno / odluka |
| … Z5 | nedostaju F_T, v_s; oznake | dodano | ispravljeno |
| … Z6 | — | — | provjereno, bez promjene |

### Poglavlje 15 — otvoreni tokovi

Detaljna analiza: [docs/radno/skice-2026-10/u15.md](docs/radno/skice-2026-10/u15.md)

| skica | problem | ispravak | status |
|---|---|---|---|
| u15_fig_uvod_otvoreni_tok | brzine u četiri različita mjerila; v2 na granici KV; indeksi; „vs” | zajedničko mjerilo 20 px/(m/s); pomak v2; tspan | ispravljeno (+ odluka „v_s”) |
| u15_vjezbe Z1 | nema Q; skica otkriva smjer v − c | dodan Q | ispravljeno / odluka |
| … Z2 | „²y (m)” zabuna; minimum očitljiv | pomak oznake osi | ispravljeno / odluka |
| … Z3 | — | — | provjereno, bez promjene |
| … Z4 | indeksi | tspan | ispravljeno |
| … Z5 | v1 preko F_p,1; indeksi; „izvan slike” | pomak; tspan; „okomito na sliku” | ispravljeno |
| … Z6 | indeksi; y2 < y_2,dop vidljivo | tspan | ispravljeno / odluka |

### Bilježnice i interaktivni laboratoriji (`notebooks/`)

Detaljna analiza: [docs/radno/skice-2026-10/notebooks.md](docs/radno/skice-2026-10/notebooks.md)

| crtež | problem | ispravak | status |
|---|---|---|---|
| u01 c04 | dvije osi bez legende | legenda i obojene oznake sa simbolima | ispravljeno |
| u01 c08 | — | — | provjereno |
| u02 c04 | — | — | provjereno |
| u02 c11 (Z5) | osi bez $\tau$, $dv/dy$ | simboli iz teksta | ispravljeno |
| u02 c13 (Z6) | „drugi regulator” dvosmislen; nema $p_{M,2}$, $D$ | rasponi regulatora i simboli | ispravljeno |
| u03 c04 | $\rho_m$ prema $\rho_2$ (ρ_m = more u U03) | $\rho_2$ | ispravljeno |
| u04 c09 | — | — | provjereno |
| u04 laboratorij | presjek nije u jednakom mjerilu (≈ 3×) | — | treba odluku |
| u05 c04 | (notacija markdowna α/b/L/h_t) | — | provjereno; notacija → odluka |
| u06 c04 | — | — | provjereno |
| u07 c04 | (notacija d/F_B) | — | provjereno; notacija → odluka |
| u08 c04 | boja ravnoteže kao Δt = 5 s | sivoplava crta | ispravljeno |
| u09k c05 | „M=1”; glavna krivulja bez oznake | $Ma=1$, „izentropski model” | ispravljeno |
| u09 Venturi laboratorij | jednake strelice (kontinuitet), preklapanje „1/2” i naslova, Cd | dulja strelica u grlu, pad, $C_d$ | ispravljeno |
| u09 Venturi c12 | imena varijabli na stupcima | simboli | ispravljeno |
| u10 c05, c09 | „1e+05”; „Hp − Hs” | $Re=1\cdot10^5$, $H_p-H_s$, radna točka | ispravljeno |
| u11 c05 | poligon: tlak skriven; oznake riječima | širine i glave strelica, $\vec F_p$, $\vec R_{st\to f}$ | ispravljeno |
| u11 c07 (Z5) | oznake obični tekst | $P=F_xu$, $u=v/3$ | ispravljeno |
| u12p c05, c07, c09, c11 | decimalna točka, t/r osi, oznake bez vektora, T/Vj | oznake prema tekstu U14 | ispravljeno |
| u12 Poiseuille laboratorij | „Qref” obični tekst; $u$ za brzinu fluida | $Q_{ref}$; $u$/$v$ → odluka | ispravljeno + odluka |
| u12 c10, c14, c16, c18 | bez jedinice; $u$ (ploča) za fluid; nedostaje legenda | (m³/s), $v$, $G_{krit}$, $\tau_0$, legenda | ispravljeno |
| u13 c05 | „Q_A” doslovno | $Q_A$ | ispravljeno |
| u13 c09 | — | — | provjereno |
| u14 c05 | raspon „označen”, a nije | granice modela, $Re$ | ispravljeno |
| u14 c12 | „λL” | $\lambda_L$ | ispravljeno |
| u15 c05, c07, c09, c11 | neobjašnjene crte i točke; M umjesto I; bez n | legende i oznake prema tekstu | ispravljeno |
| web/filters/includes/components | nema crteža | — | — |

## Provedba odluka autorice (14. listopada 2026.)

Autorica je 14. listopada odobrila sve prijedloge iz odjeljaka A–E1 ispod. Popis u nastavku ostaje kao zapis o odlukama. Pune evidencije po poglavljima, s tablicama staro → novo, nalaze se u `docs/radno/skice-2026-10/provedba/uNN.md`.

**A. Proturječja u tekstu.** Sve stavke su ispravljene.

- **Pog. 1, Z2:** kormilarski stroj sada je četverocilindrični Rapsonov stroj; tlak drži dijagonalni par cilindara, a povratni par vraća ulje.
  - Moment ostaje M = 2Fr = 88,4 kN·m.
  - Dobava je ispravljena na V = 2As = 7,36 L (prije 3,68 L).
  - Uz iskaz su usklađeni verifikator, skica i D01/D02.
  - Stabilni ID `#task-kormilarski-stroj-dva-cilindra` je zadržan.
- **Pog. 5, Z2:** „konkavnu” → „konveksnu”.
- **Pog. 6, P1:** zahtjev je tražio „silu držanja prema dolje”, a rješenje daje oko 381 N prema gore. Zahtjev sada traži iznos i smjer.
- **Ostalo:** usklađeni su p_pl, p_aps, alt-tekstovi, „L/s”, „volumenski” i p_aps,C.

**B. Skice zadataka više ne otkrivaju rezultat.** Načelo je primijenjeno na sve skice zadataka Z1–Z6, ne samo na popis B.

- Traženi smjerovi, krivulje, radne točke, kutovi, razine, gazovi i dometi više nisu nacrtani u mjerilu rezultata. Nepoznanica je shematska i označena s „?”.
- Zadani podatci ostaju u mjerilu.
- Napomene uz skice više ne tvrde zajedničko mjerilo tamo gdje ga nema.
- Checkeri sada provjeravaju da rezultat nije prikazan. Primjeri: element ne postoji, omjer odstupa od rezultata za više od 15 %, kut nije traženi.

**E1. Stil vektora.** Vektori sada imaju propisan stil i atribut `data-mf1-vector`; strelice koje nisu vektori imaju `data-mf1-role`. Svih 953 strelica u 95 skica je razvrstano.

- Sila i moment: deblja crta i pun vrh.
- Brzina, smjer protoka, pomak i kutna brzina: tanja crta i otvoren vrh.
- Ubrzanje i efektivno polje: isprekidana crta.
- Tlak i normala: tanka crta i mali vrh.
- Oznake vektora pisane su podebljano.

Pravilo je zapisano u [urednički stil](docs/urednicki_stil.md) i u protokol skica. Legenda za čitatelja je odjeljak „Strelice na skicama” u uvodnom poglavlju. Provjerava ga `tools/audit_sketch_design.py` (`check_arrow_semantics` u `tools/sketch_style.py`).

Sive strelice brzine lopatice, brzine broda i vrtnje u pog. 14 te pomaci u pog. 1 sada su u vektorskom stilu.

**C i D. Notacija.** Standard je dopunjen. Primijenjen je u tekstu, jednadžbama, skicama, bilježnicama i dodatcima D01–D05; D06 je generiran.

| Veličina | Oznaka |
|---|---|
| težina | $F_G$ ($G$ samo težište) |
| širina broda ili pontona | $b$ ($B$ samo središte istisnine) |
| kut poprečnog nagiba | $\varphi$ |
| gustoće vode, morske vode, ulja | $\rho_w$, $\rho_{mv}$, $\rho_o$ (indeks $v$ samo para, $m$ samo model) |
| polumjer zavoja | $R_z$ |
| udio otvorene površine | $\psi$ |
| ekvivalentna hrapavost | $k_s$ ($\varepsilon$ samo disipacija) |
| visina dobave crpke; visina turbine | $H_p$, $H_t$ |
| standardna nesigurnost | $s(x)$ |
| kutovi lopatice | $\beta_1$, $\beta_2$ od smjera $-u$ (zadani kutovi preračunati, rezultati isti) |
| koeficijent sustrujanja | $\chi$ |

Lokalne dvoznačnosti po poglavljima razriješene su novim oznakama koje nisu zauzete u knjizi. Popisane su u [rječniku oznaka](RJECNIK_OZNAKA.md).

Nazivlje je ujednačeno: „Darcyjev koeficijent trenja”, „hidrostatički”, „piezometarski”, „zaustavna entalpija”.

**Namjerno ostavljeno.** Razlozi su u evidencijama provedbe.

- Opći $\rho$ u zadatcima s jednim fluidom.
- Indeks $m$ u $T_m$ (srednji gaz) i $F_m$ (izmjerena sila).
- Duljina ležaja $L$ u pog. 2, P4, koja se vidi samo u tekstu, jer bi uzdužni pogled bio novi panel.
- Omjeri koji nisu čitljivi (zadržan je poredak).
- Vrlo kratke strelice u pog. 14 i 15, kod kojih se vidi uglavnom vrh.
- Ključevi `u` i `u_ref` u bilježnici pog. 12, koje čita test laboratorija.
- Putanje slobodnog mlaza u pog. 8, koje su crte, a ne strelice.
- Nekorištena datoteka `u14_fig_omjer_sila.svg` uz sačuvano sidro.

## Stavke koje trebaju tvoju odluku (stanje 13. 10. — provedeno 14. 10., vidi gore)

Najprije sažetak po vrsti, zatim potpun popis po poglavljima s citatima i prijedlozima.

### A. Proturječja i moguće tipfeler-greške u tekstu (tekst nije mijenjan)

1. **Pog. 1, Z2 (r. 676), kormilarski stroj.** Oba cilindra guraju (M = 2Fr), a crpka „dobavlja ulje u jedan cilindar, a iz drugoga ulje istodobno istječe”. Ako oba guraju, oba se produljuju, pa je V = 2As. Inače vrijedi Rapsonov raspored s M = Fr.
2. **Pog. 5, Z2 (r. 720).** Piše „gornju (konkavnu) stranu”, a za z = −H(x/L)² gornja je strana konveksna.
3. **Pog. 3, Z5 (r. 786).** Kontrolni rezultat koristi p_gas,aps, a poglavlje i skica p_pl.
4. **Pog. 11, Z3.** Piše p_abs umjesto p_aps.
5. **Pog. 11, alt-tekst Buckinghamove slike (r. 172).** Piše F umjesto F_D i navodi Π-grupe kojih na slici nema.
6. **Pog. 7.** Gustoća mješavine je ρ₃ u P3, a ρ_mix u Z6. Oblik „volumni” treba biti „volumenski protok” (P4).
7. **Pog. 8, Z6 (r. 864).** p_C treba biti p_aps,C.
8. **Pog. 10, P2.** Piše „l/s”, a ostatak poglavlja „L/s”.
9. **Pog. 6, P1.** Alt-tekst spominje „silu držanja”, koje nema na skici ni u tekstu.
10. **Pog. 6, P5.** „e_t je ekscentar tanka”, ali e_t nije na skici.
11. **Pog. 14.** Alt-tekst slike diska navodi „vw” umjesto v_j.

### B. Skice zadataka koje i dalje otkrivaju dio rezultata

Zasad ih checkeri namjerno zahtijevaju. Za svaku stavku odluči: zadržati ili neutralizirati (uz usklađenje checkera).

| Mjesto | Što skica otkriva |
|---|---|
| pog. 1 Z5 | promjer crpnog klipa d_p = 9 mm |
| pog. 2 Z3 | smjer obaju otpora |
| pog. 2 Z4 | depresiju i omjer h₁/h₂ |
| pog. 5 Z2 | hvatišta i predznake F_H i F_V |
| pog. 5 Z1 | oznaku ⊗ |
| pog. 5 Z6 | silu F |
| pog. 6 Z2, Z3, Z5, Z6 | gazove i položaj akumulatora točno u mjerilu rezultata |
| pog. 8 Z5 | grlo d = D₁/2, što je upravo rješenje od 50 mm; strelice 1 : 2,4 ne odgovaraju nacrtanoj geometriji |
| pog. 9 Z1 | smjerove (može se razmotriti potpuno uklanjanje strelica smjera) |
| pog. 13 Z4 | krivulju sustava i radnu točku (Q ≈ 19 L/s, H ≈ 19 m) |
| pog. 14 Z3 | izlaz lopatice točno pod traženim β₂ = 150° |
| pog. 14 Z4 | potpune trokute brzina, koje zadatak traži da se nacrtaju |
| pog. 15 Z1 | predznak v − c |
| pog. 15 Z2 | označeni minimum krivulje |
| pog. 15 Z6 | nacrtani y₂ vidljivo manji od y_2,dop |

Pog. 5 Z3: strelica T je uklonjena. Ako je želiš natrag, vraćanje je jednostavno.

### C. Dvoznačna notacija u tekstu

Ovo ne rješavam sama. Detalji su u rječniku po poglavljima.

- **Odstupanja od standarda notacije:**
  - α kao kut (pog. 7 Z2; bilježnica pog. 5);
  - φ kao udio slobodne površine rešetke (pog. 7 P2);
  - kut nagiba je θ u primjerima, a φ u pog. 6 Z3 i D01/D02;
  - p₀ kao tlak na površini u izvodu Arhimedova zakona (pog. 6);
  - p_abs (pog. 11 Z3).
- **Ista oznaka za dvije veličine:**
  - G i B: težina i težište, širina i središte istisnine (pog. 6);
  - R: polumjer spremnika i polumjer zavoja (pog. 4); krak i polumjer (pog. 10);
  - h_p (pog. 3 i 13);
  - y_t (pog. 15);
  - indeks v znači vodu u ν_v i ρ_v, a paru u p_v (pog. 11);
  - s (pog. 7);
  - K (pog. 9 Z5, prema volumnom modulu);
  - u i r (pog. 9 Z6);
  - e: krak i jedinični vektor (pog. 10);
  - C: grlo i vrh sifona (pog. 8);
  - β s četiri referentna smjera (pog. 14);
  - H, p, r, u, k (pog. 12).
- **Dvije oznake za istu veličinu:**
  - z_C, h_C i h_osa (pog. 4);
  - gustoće ulja i vode: ρ_o, ρ_u, ρ_v, ρ_w, ρ_mv… (pog. 3);
  - R_x i R_y kao sila stijenke na fluid (r. 5) i R kao reakcija nosača (r. 99) (pog. 10);
  - v_s za brzinu silovitog toka, što se sudara s brzinom broda v_s (pog. 15, uvodna skica).

### D. Oznake koje skica treba, a tekst ih ne definira, ili obrnuto

| Mjesto | Stanje |
|---|---|
| pog. 1 P5 | krakovi a i 5a nisu u tekstu (tekst daje i = 5) |
| pog. 3 Z1, Z3, Z6 | točke A i C te simbol „a” uklonjeni sa skice jer ih tekst ne imenuje |
| pog. 5 uvod | h₁ nije definiran u uvodnom tekstu |
| pog. 7 kinematika | P(t_i) |
| pog. 8 P2 | h₁–h₃ i x₁–x₃ |
| pog. 11 Z6 | širina b_m uklonjena (b već znači visinu kanala i raspon profila) |
| pog. 11 uvod | „Model i prototip”, a nacrtan je samo model |

### E. Stil i standard skica

1. **Razlikovanje vektora brzine i sile stilom** (tvoja točka 6). Projektni standard iz rujna 2026. propisuje jednu boju `#356b83` za sve vektore; vrsta se razlikuje oznakom. Stvarno stanje nije jedinstveno: pomaci u pog. 1 te u, brzina broda i strelice vrtnje u pog. 14 sivi su `#657781`.
   - Prijedlog: u istoj boji sila kao puna deblja strelica, brzina kao tanja strelica s otvorenim vrhom.
   - To bi bila promjena svih skica, tokena i `audit_sketch_design`.
2. **Oznaka vektora na skicama.** Nema konvencije: podebljano ili strelica iznad.
3. **Unicode eksponenti** (10⁻⁶, m², s⁻¹). Zadržani su, a protokol traži `tspan`.
4. **Omjeri koji nisu u mjerilu zbog čitljivosti** (zadržan je poredak):
   - pog. 1: 6,6; 35; 30; ~47;
   - pog. 4: a prema g (pravi omjer nose umetci);
   - pog. 7: Z5 u : w = 1 : 22;
   - pog. 10: P2 i P7.
5. **Pog. 4, uvodna slika.** Panel je preimenovan iz „Centrifugalni separator” u „Rotirajući spremnik”, jer gravitacijski paraboloid proturječi modelu separatora iz P6. Za separator treba zasebna skica.
6. **Pog. 9.** Potvrdi osnosimetričnu interpretaciju A_e/A* = 1,6 (omjer promjera 1,26).
7. **Pog. 10, P6.** Potvrdi jednu oznaku p_M na oba presjeka.
8. **Pog. 1, P5.** Kočna tekućina u boji „drugog fluida” nema oznaku vrste. Strelica F_M leži na potisnoj šipki.
9. **Pog. 2.** Strelice σ presijecaju tanku stijenku kapilare (posljedica točne tangente). Duljina L ležaja u P4 ne vidi se bez aksijalnog pogleda.
10. **Pog. 11.** `u14_fig_omjer_sila.svg` postoji, ali se ne koristi; u tekstu je sidro bez slike.
11. **Bilježnice:**
    - decimalni zarez na osima (zadano je ponašanje matplotliba);
    - jednako mjerilo osi u laboratoriju pog. 4;
    - u prema v za brzinu fluida u `u12_poiseuille`;
    - notacija u modelu `u05` (α, b, L, h_t);
    - notacija u markdownu više bilježnica;
    - umetak s uvećanim vrhom poligona sila u `u11`.

### Potpun popis po poglavljima

### Poglavlje 1

1. **Z2 — kinematička proturječnost teksta** (`source/u01_...md`, redak 676): „cilindri guraju u suprotnim smjerovima, pa oba daju moment istoga smisla.
   Crpka u radnim komorama obaju cilindara održava manometarski tlak p_M = 6,0 MPa. Pri prebacivanju kormila crpka dobavlja ulje u jedan cilindar,
   a iz drugoga ulje istodobno istječe natrag”. Ako oba klipa guraju (M = 2Fr), zakret u smislu tog momenta produljuje **oba** cilindra
   (lijevi kraj ide od lijevog klipa, desni od desnog), pa crpka mora dobaviti 2As, a ne As; cilindar iz kojeg ulje istječe uvlači se, tj. giba
   se protiv vlastite tlačne sile i ne može davati moment istog smisla pri p_M. Skica prikazuje statički opis (oba guraju, isti tlak) i nije mijenjana.
   Prijedlog: ili M = 2Fr i V = 2As (oba cilindra pod tlakom, oba se produljuju), ili klasični dvoklipni (Rapsonov) raspored u kojem jedan klip tlači,
   a drugi vraća ulje, uz M = Fr.
2. **P5 kočnica — oznake a i 5a** nisu u tekstu (tekst: „Poluga omjera i = 5”). Prijedlog: u tekst dodati „krakovi a i 5a od zgloba” ili zamijeniti kote jednom oznakom i = 5.
3. **P5 kočnica — ispuna kočne tekućine `#eadfc5`** (paleta: „drugi fluid”, uz obveznu oznaku vrste) bez oznake. Prijedlog: dodati oznaku „kočna tekućina”
   ili prebaciti na osnovnu ispunu `#dcebf1`. Također u pog. 1 ulje je u uvodu i P1 `#eadfc5`, a u P2, P3, P4 i Z-skicama `#dcebf1`.
4. **P5 — F_M leži na potisnoj šipki**: vidljiv je uglavnom vrh. Pomak strelice uz šipku maknuo bi je s pravca djelovanja; ostavljeno.
5. **Z5 — crpni klip nacrtan promjerom 9 mm**, što je točno odabrano rješenje („Odabire se 9 mm”). Mjerljivo samo ravnalom; prijedlog: ili prihvatiti
   (srednja varijanta), ili nacrtati neutralnu shemu bez zajedničkog mjerila promjera i to navesti u napomeni (napomena sada tvrdi zajedničko mjerilo unutar Z5).
6. **Stil vektora**: pomaci u Z3–Z6 i P3/P4 crtani su `#3a4a56` + `axisMarker`, sile `#356b83`; protokol propisuje jednu boju za sve vektore.
   Razlika nije mijenjana (odluka autorice).
7. **Omjeri sila koji se ne mogu nacrtati** (zadržan poredak): uvod F₂/F₁ = 6,6 (crtano 3,0), P3 F₂/F₁ = 35, P4 F_L/F_p = 30, P5 F_M/F_n = 5 i F_f/F_n ≈ 15, Z5 F_L/F_p ≈ 47.
   Tekst uz skice to već navodi („strelice sila imaju zasebna mjerila”).

### Poglavlje 2

1. **Z3 i Z4 — skica otkriva dio traženog rezultata.** Z3 (redak 748): „2. Odredi smjer svakog otpora i objasni pogrešku predloženog postupka.” —
   skica crta oba otpora ulijevo (i F₁ = 2F₂). Z4 (redak 778): „3. Odredi h₂ za premazani procjep i protumači predznak” — skica crta spuštanje
   s konveksnim meniskusom u omjeru h₁/h₂ = 3,35, a napomena uz skice to izričito navodi. Checker oba prikaza zahtijeva. Prijedlog: ili prihvatiti
   (skica kao podrška zaključivanju), ili u Z3 ukloniti strelice F₁/F₂ i ostaviti samo u i F, a u Z4 prikazati premazani procjep bez razine (samo θ₂ = 105°).
2. **Z5 — oznaka F_v** nije u tekstu Z5 („vučna sila uzorka”); u knjizi je F_v uveden samo u tumačenju uvodne skice. Prijedlog: u tekstu Z5 ili napomeni uz skice
   navesti „F_v — sila uzorka na ploču”.
3. **P4 ležaj — duljina L = 70 mm** (ulazi u A = πDL) nije na skici; bez uzdužnog pogleda nije prikaziva kotom. Prijedlog: prihvatiti (podatak u tekstu)
   ili dodati uzdužni pogled kao zaseban panel (strukturna izmjena, novi PANEL u `print-layouts.json`).
4. **σ-strelice u uvodu i P3** počinju na kontaktnoj liniji i, zbog fizikalno točnog smjera (tangenta, 18° prema stijenci), prelaze tanku stijenku kapilare;
   checker propisuje početak na kontaktnoj liniji. Prijedlog: prihvatiti kao uobičajeni udžbenički prikaz ili crtati strelicu s vrhom u kontaktnoj točki
   (rep u tekućini) — to traži usklađenje checkera.
5. **P4 — omjer τ₁ : τ₂ = 10 : 1** nije nacrtiv uz čitljiv vrh strelice; crtano 100 : 24 (poredak). Opis slike to sada navodi.
6. **Stil vektora**: brzine (profili, u) crtane su `#3a4a56` + `axisMarker`, sile i σ `#356b83`; protokol propisuje jednu boju za sve vektore. Nije mijenjano.
7. **Boja ulja/glicerina/uzorka `#eadfc5`** („drugi fluid”) u jednofluidnim skicama: oznaka vrste dodana u uvodu, P1 i Z1; u P2 (naslov „Smicanje ulja”), P4 i Z3 (napomena „uljni procjep”)
   vrsta je imenovana u naslovu/opisu, ne uz ispunu.

### Poglavlje 3

1. **Imena točaka u Z1, Z3, Z6.** Tekst ne imenuje „promatranu točku” (Z1, r. 650), „priključnu točku … 0,12 m iznad dodira” (Z3, r. 707) ni „dublju točku … h_2” (Z6, r. 798); skica je imala A, A i C te simbol „a” za 0,12 m. Oznake su uklonjene. Prijedlog: ako ih želite, uvedite ih u tekst („točka A”, „točka C”) — tada ih vratiti na skicu (za 0,12 m ne koristiti „a”, nego npr. $h_{u}$ ili $z_A$).
2. **Z5, r. 786:** „$p_{gas,aps} = 92{,}6\ \text{kPa}$” — u ostatku poglavlja i na skici tlak plina je $p_{pl}$. Prijedlog: $p_{pl}$ (aps.).
3. **h_p dvoznačan:** r. 172 „$h_p = p_M/(\rho g)$” (piezometarska visina) i P5 r. 489 „$h_p = 2{,}0\ \text{m}$” (visina ploče P). Skica P5 slijedi tekst P5. Prijedlog: u P5 npr. $z_P$ ili $h_P$.
4. **Gustoće ulja i vode** nisu jednoznačne (ρ_o/ρ_u/ρ za ulje; ρ_v/ρ_w/ρ_mv/ρ_m/ρ_b za vodu) — skice slijede pojedine zadatke; odluka o ujednačenju je tekstualna.

Napomena o tuđim skicama: nisu uočeni problemi izvan pog. 3 i 4.

### Poglavlje 4

1. **R dvoznačan:** polumjer spremnika (r. 147, P4, Z6) i polumjer zavoja (P3, r. 361 „$R = 180\ \text{m}$”). Skice slijede pojedini tekst. Prijedlog: u P3 npr. $R_z$.
2. **Visina na osi:** uvod r. 5 „$z(r)=z_C+\omega^2r^2/(2g)$”, izvod i P4 $h_C$, Z6 naputak (r. 831) $h_{osa}$, $h_{rub}$. Uvodna skica sada označuje h_C i h_R (prema izvodu), Z6 skica h_osa (prema naputku). Prijedlog: ujednačiti na $h_C$, $h_R$.
3. **Uvod r. 3 „$a=v^2/R$”** prema P3 „$a=v_s^2/R$” (standard: $v_s$ za brod).
4. **H u P2** (r. 297) jest vertikalna projekcija stijenke, ne visina modula; prijedlog: $h_{AB}$ ili napomena.
5. **Naslov desnog panela uvodne skice** promijenjen je iz „Centrifugalni separator” u „Rotirajući spremnik” jer prikazani gravitacijski paraboloid proturječi modelu separatora iz P6. Ako autorica želi zadržati separator kao primjenu, treba posebna skica s cilindričnom razdjelnicom bez gravitacije.
6. **Strelice ubrzanja izvan umetka** (P1, P2, uvod lijevo) skraćene su na duljinu manju od g; pravi omjer a/g prikazuju umetci. Ako se želi da sve strelice budu u jednom mjerilu, glavne bi strelice bile 6–17 px — nečitljivo; zato je zadržan poredak.

### Poglavlje 5

1. **Z2, redak 720:** „Voda … kvasi gornju (konkavnu) stranu pokrova”. Za zadanu parabolu $z=-H(x/L)^2$ (naputak, i skica) gornja je strana **konveksna**. Prijedlog: „kvasi gornju (konveksnu) stranu pokrova” ili samo „gornju stranu”. Skica nije mijenjana.
2. **Z2 skica otkriva rezultate:** strelice F_H i F_V nacrtane su točno na traženoj dubini 0,600 m i udaljenosti 0,900 m te s traženim predznacima (prema stijenci, prema dolje); to propisuje i checker (`check_u05_sketch_geometry.py`, Z2) i opis slike. Pravilo „skica zadatka ne otkriva rezultat” u sukobu je s tim. Prijedlog: (a) zadržati (smjer iz strane koju voda kvasi je dio „postavljanja modela”, kako kaže uvod zadataka) ili (b) zamijeniti F_H/F_V samo lokalnom normalom dF i uskladiti checker. Isto vrijedi blaže za ⊗ u Z1 i strelicu F u Z6 (položaj = h_CP; u Z6 se h_CP ne traži).
3. **Z2 oznake:** zadatak traži predznačene $F_x$, $F_z$, a skica (kao teorija) rabi $F_H$, $F_V$. Preimenovanje strelice koja pokazuje −x u „F_x” bilo bi dvoznačno (F_x<0), pa je ostavljeno F_H/F_V. Odluka: zadržati ili dodati napomenu „|F_x|, |F_z|”.
4. **Z3:** sila spojnice T bila je nacrtana ulijevo (traženi smjer). Zamijenjena je šipkom „spojnica, sila T” bez smjera. Ako autorica želi zadržati vektor, vratiti strelicu (lako reverzibilno).
5. **u05_fig_uvod_pregled:** kota dubine gornjeg ruba preimenovana iz `h_t` u `h_1` (konvencija poglavlja); u uvodnom tekstu ta oznaka nije definirana — prihvatljivo ili ukloniti oznaku.

### Poglavlje 6

1. **P1 (u07_fig_pumpno_kuciste), fig-alt i opis slike:** „Uzgon, težina i sila držanja potpuno uronjenoga pumpnog kućišta.” — sila držanja nije nacrtana, a tekst primjera nema oznaku za nju („Veza s proračunom”: „ne treba unaprijed pretpostaviti da držač vuče prema gore”). Prijedlog: (a) ukloniti „i sila držanja” iz fig-alt/opisa ili (b) dodati strelicu s oznakom (npr. $F_d$ kao u Z1) prema gore, ≈0,46 duljine G.
2. **P5 (u07_ch2_poplavljen_tank), „Veza s proračunom”:** „Skica ne prikazuje L, L_t, H i H_t; e_t je ekscentar tanka.” — rečenica sugerira da je $e_t$ na skici, ali nije; kota od centroida tanka do osi križala bi F_U i B. Prijedlog: „$e_t=B/2-B_t/2$ je ekscentar tanka (nije kotiran)” ili dopustiti kotu ispod trupa.
3. **Skice zadataka prikazuju rezultate geometrijski:** Z2 (gaz 0,201 m), Z3 (gazovi 0,2496/0,3229 m), Z5 (gazovi 0,2227/0,3563 m), Z6 (položaj akumulatora 0,321 m) nacrtani su točno na izračunatim vrijednostima (checker integrira istisninu za nacrtani gaz). Brojevi nisu napisani, ali se mogu izmjeriti. Odluka: zadržati (fizikalno dosljedan crtež) ili prikazati „ilustrativni” gaz uz napomenu.
4. **Oznaka kuta nagiba u tekstu:** P3, P4, P5 i izvodi rabe $\theta$, a Z3 i d01/d02 $\varphi$. Skice slijede tekst pojedinog zadatka; ujednačiti u tekstu.
5. **Oznaka G:** tekst rabi $G$ i za težinu ($G=mg$, P1; „Napomene uz skice”) i za točku težišta G. Skice slijede tekst; u uvodnoj skici sila je sada „težina G”, točka „G”. Razmotriti $mg$ ili $F_G$ za silu.
6. **$p_0$ u izvodu Arhimeda** (eq …matematicki-izvod-01/02: „$F_1=(p_0+\rho gh_1)A$”): prema standardu notacije $p_0$ je samo zaustavni tlak; ovdje znači tlak na slobodnoj površini (prijedlog $p_{atm}$). Skica ne nosi tu oznaku.

### Poglavlje 7

1. **Z2, r. 768**: „Kut između brzine i odabrane jedinične normale $\vec n$ iznosi $\alpha=60^\circ$”. Standard (urednički stil, Notacija) rezervira $\alpha$ za korekcijske faktore, kutove za $\theta$, $\varphi$. Skica sada prati tekst ($\alpha$). Prijedlog: u tekstu i skici $\theta=60^\circ$.
2. **P2, r. 410**: „slobodnih $\varphi = 0{,}55$” — $\varphi$ je po standardu kut. Prijedlog: npr. $\psi$ ili $\varepsilon$ (udio slobodne površine).
3. **$s$ dvaput**: $s_B$ relativna gustoća (r. 475) i hod klipa $s$ (Z5, r. 851). Prijedlog: hod klipa $\ell_s$ ili $\Delta\ell$.
4. **Gustoća mješavine**: $\rho_3$ (P3, r. 482) prema $\rho_{mix}$ (Z6, r. 901). Prijedlog: ujednačiti.
5. **Kinematika, oznake „P(t₀)…P(t₃)”**: tekst nema oznaku za položaj čestice. Zadržano jer ilustrira „kroz vrijeme”; prijedlog: ili dodati u tekst „položaji čestice $P(t_i)$”, ili na skici „čestica u $t_0$…”.
6. **Duljine koje nije moguće nacrtati proporcionalno**: Z5 $u:w=1:22$ i Z6 $Q_s:Q_{iz}=1:3$ (uz $Q_m$) nacrtani su samo po poretku. Ako autorica želi pravi omjer, treba odlučiti o kraćim markerima ili napomeni „strelice nisu u mjerilu” u Napomenama uz skice (r. 911).
7. **Uvodna skica, „ρ₁, A₁, v₁” uz $\dot m_{ul}$**: miješaju se indeks „ul” i „1”. Tekst koristi oba (r. 3 i r. 222). Prijedlog: ili $\rho_{ul}, A_{ul}, v_{ul}$, ili ostaviti.
8. **Oznaka vektora na skicama**: projekt nema SVG konvenciju za vektorske oznake (strelica iznad ili bold). Ovdje je $\vec n$ i $\vec v$ (kinematika) prikazan podebljanim kurzivom, ostale brzine kao skalarni iznosi. Odluka o jedinstvenoj konvenciji na razini knjige.
9. **P4 (r. 586)** „volumni protok” prema standardnom „volumenski protok” (tekst, ne skica).
10. **Razlikovanje brzine i protoka stilom**: u poglavlju ih razlikuje samo oznaka (jedna boja vektora) — prema briefu ne uvodim novu shemu.

### Poglavlje 8

1. **P2 (r. 348–390)**: tekst piše „$h = 1{,}0$ m, $h = 2{,}0$ m, $h = 3{,}0$ m” i jedan domet $x$; skica razlikuje slučajeve indeksima $h_1,h_2,h_3$ i $x_1,x_2,x_3$ kojih u tekstu nema. Zadržano (pravi indeksi, oznake uz kote). Prijedlog: u tekstu „za $h_1 = 1{,}0$ m …” ili na skici samo vrijednosti.
2. **Z5 (r. 832)**: promjer grla nije zadan (ulošci 40/50/60 mm), a skica crta grlo $d = D_1/2$, tj. upravo **ispravni uložak od 50 mm** — moguć nenamjeran nagovještaj rješenja; strelice $v_1:v_C$ = 1 : 2,4 ne odgovaraju nacrtanoj geometriji (bila bi 1 : 4). Prijedlog: nacrtati neutralno grlo (npr. $d/D_1\approx0{,}55$) s napomenom „$d$ shematski”, ili zadržati i strelice uskladiti na 1 : 4.
3. **Z6, r. 864**: „apsolutni tlak $p_C\ge30\ \text{kPa}$” prema $p_{aps,C}$ u r. 862 i rezultatu — ujednačiti u $p_{aps,C}$.
4. **P6 (r. 656)**: $v_o$ za brzinu uz gušći zrak — lako se brka s $v_0$ (P2). Prijedlog: $v'$ ili $v_{1,25}$.
5. **Indeks grla**: Z2 grlo = 2, Z5 grlo = C, a C je i vrh sifona (P3, Z6). Prijedlog: grlo uvijek 2 (ili $g$).
6. **Z6 (skica)**: vrh strelice u uzlaznom kraku širi je od unutarnjeg promjera uvećane cijevi (8 px) pa prelazi preko stijenki — postojeće stanje, čitljivost; smanjenje markera bilo bi odstupanje od zajedničkog markera datoteke.
7. **Z4 (skica)**: smjer pramca nije izričito označen (tekst: „otvorom prema pramcu”); prikazano posredno smjerom nastrujavanja. Ako treba, dodati oznaku „← pramac” (potrebno mjesto u panelu postoji).

### Poglavlje 9

1. **Z1 (r. 507):** „Označi oba uzdužna smjera njegova širenja i predznake brzina prema osi $x$ sa skice.” — skica je imala „−a/+a”, tj. traženi odgovor. Promijenjeno u „a”; strelice ostale jer Napomene (r. 492) već kažu „U Z1 poremećaj putuje u oba smjera”. Prijedlog alternative: ukloniti i strelice (tada se iz checkera mora ukloniti provjera `z1left/z1right`), pa student ucrtava oba smjera.
2. **P6 / uvodna shema (r. 400 „shema na @fig-kompresibilni-pregled”):** shema sada crta A_e/A* = 1,6 kao osnosimetričnu sapnicu (omjer promjera 1,26). Ako autorica želi ravninsku (2D) interpretaciju, omjer visina bio bi 1,6 — potvrditi.
3. **Z5 naputak (r. 632):** „$\dot m=C_dA_gK(p_0,T_0)$” — $K$ je prema standardu notacije rezerviran za volumni modul (r. 65). Prijedlog: npr. $\Phi(p_0,T_0)$. (Tekst, ne skica.)
4. **Z6 (r. 664–671):** $u(\cdot)$ za nesigurnost i $r$ za omjer kolidiraju s $u$ (brzina granice) i $r$ (polumjer) iz standarda. (Tekst.)
5. Uočeno izvan opsega (d01 r. 113): „ukupna entalpija” prema „zaustavna entalpija” u poglavlju (r. 702).

### Poglavlje 10

1. **Oznaka R_x, R_y u uvodnoj slici.** Tumačenje skice (r. 5): „Strelice $R_x$ i $R_y$ pokazuju pretpostavljene pozitivne smjerove sile stijenke na fluid”, a r. 99: „$\vec R_{st\to f}$ silu stijenke na fluid, a $\vec R$ reakciju nosača ili oslonca na element”. Skica slijedi r. 5. Prijedlog: u r. 5 i na skici pisati $R_{st\to f,x}$, $R_{st\to f,y}$ (ili zadržati $R$ i promijeniti r. 5 u reakciju nosača uz suprotne strelice).
2. **$R$ kao duljina kraka (P7, r. 824) i polumjer (r. 82)** uz $R$ = reakcija (r. 99). Prijedlog: krak $r$ ili $L$.
3. **$e$** kao krak (Z4) i $\vec e_{ul}$, $\vec e_{iz}$ jedinični vektori (P6, r. 774).
4. **Jedinica „l/s”** (P2, r. 360) prema „L/s” drugdje.
5. **P6 (r. 750):** tekst daje samo $p_M$; na skici sada $p_M$ na oba presjeka (prije $p_{M1}$, $p_{M2}$). Potvrditi.

### Poglavlje 11

1. **Z6, širina preljeva `b_m`.** Tekst ne definira širinu preljeva; skica je imala „b<sub>m</sub>”, a $b$ u istoj figuri znači visinu kanala (Z1: „visine $b=0{,}200\ \text{m}$”) i raspon (Z4: „raspona $b_p=0{,}600\ \text{m}$”). Oznaka je uklonjena, kote širina ostavljene bez oznake (pokazuju isto mjerilo 1,5 : 1). Prijedlog: ostaviti tako, ili u tekst Z6 uvesti širinu drugom oznakom (npr. $B$) pa je vratiti na skicu.
2. **Uvodna slika, naslov panela „Model i prototip”.** Nacrtan je samo model u aerotunelu; dodana je oznaka „model: Re<sub>m</sub> = Re<sub>p</sub>” prema tumačenju „Aerotunel prenosi $C_D$ pri jednakom $Re$ samo ako su i ostali relevantni uvjeti isti.” Prijedlog: zadržati, ili naslov promijeniti u „Model u aerotunelu” (i uskladiti caption „usporedba modela i prototipa”).
3. **`fig-alt` slike @fig-u14-pi-buckingham (izvor, r. 172):** „popis varijabli {F, ρ, v, D, μ}, dimenzijska matrica M-L-T i tvorba dviju Π-grupa Π₁ = F/(ρv²D²) i Π₂ = Re”. Tekst koristi $F_D$, a slika prikazuje samo matricu. Prijedlog: „Dimenzijska matrica varijabli {F_D, ρ, v, D, μ} u M-L-T ranga 3; iz nje slijede dvije Π-grupe Π₁ = F_D/(ρv²D²) i Π₂ = Re.”
4. **Z3 apsolutni tlak:** naputak i kontrolni rezultat pišu „$p_{abs}=p_{atm}+p_M$”, „$p_{abs,min}=98{,}34$ kPa”; standard notacije propisuje $p_{aps}$ (skica P3 sada koristi $p_{aps}$). Prijedlog: $p_{aps}$ u tekstu Z3.
5. **Indeks „v”:** „$\nu_v = 1{,}0\cdot10^{-6}$” (voda, P1), „$\rho_v = 1000$ kg/m³” (voda, P4) i „$p_v = 2340$ Pa” (para, P3, Z3). Prijedlog: za vodu drugi indeks ili napomena pri prvom spomenu. Skice slijede tekst.
6. **Ostale dvoznačnosti iz rječnika** ($a$ stranica/brzina zvuka; $f$ frekvencija/funkcija; $\sigma_1,\sigma_2$ u Z3; indeks prototipa $s$ i $p$; $v_{kr}$, $Q_{lim}$ s po dva značenja) — vidi `rjecnik_u11.md`.

### Poglavlje 12

1. (Neobvezno) Z4: dodati oznaku „G = dp/dx > 0” uz strelicu „tlačni pogon”? Tekst je jasan i bez nje (napomena uz skice: „U Z4 G=dp/dx>0 znači da tlak raste udesno”), pa nije dodana.
2. Oznake u tekstu (vidi rječnik): H je i razmak ploča i visina stepenice (P7); p tlak i opaženi red (Z6); r radijus i omjer profinjenja (Z6); u brzina ploče i standardne nesigurnosti; k turbulentna energija i faktor pokrivanja; intenzitet I_t (tekst) prema I (d01); C_f,x (tekst) prema c_f (d01). Skice nisu pogođene.
3. Eksponenti (10⁻⁶, m², s⁻¹) ostali su Unicode-znakovi, kao u većini skica knjige; protokol traži tspan i za eksponente — odluka o globalnoj konverziji.

### Poglavlje 13

1. **Z4 otkriva rezultat.** Skica crta točnu krivulju sustava (Colebrook) i označeno presjecište; s grafa se očita Q_op ≈ 19 L/s, H_op ≈ 19 m, što je upravo traženi rezultat („Numerički riješi radnu točku…”). Prijedlog: zadržati krivulju crpke i statičku visinu Δz = 8 m, a krivulju sustava i točku ukloniti (ili barem ukloniti kružić presjecišta). Zahtijeva usklađenje `check_u13_sketch_geometry.py` (provjere `z4system`, `z4operatingPoint`) i alt-teksta u izvoru.
2. ~~P3 (petlja) — širine cijevi.~~ **Ispravljeno** (nalog koordinatora), vidi „Dopuna” dolje.
3. ~~Uvodna skica — h_CD bez kote.~~ **Ispravljeno** (nalog koordinatora), vidi „Dopuna” dolje.
4. **Oznake u tekstu (vidi rječnik):** h_p (bilanca) prema H_p (karakteristika); q za protok u L/s (P4, Z6) protivno standardu (q samo pog. 15); u kao brzina fluida u definiciji α (redak 38) i S_ij; „piezometrijska” (redci 44, 46) prema „piezometarska”; z_s s promjenom predznaka (P6 iznad, Z6 ispod).

### Poglavlje 14

1. **Boja brzine krute granice.** U pog. 14 u, brzina broda prema tlu i strelice vrtnje sustavno su sive `#657781` (pomoćna boja kota), a projektni standard propisuje `#356b83` za sve vektore. Prijedlog: ili prihvatiti kao iznimku poglavlja (u trokutima pomaže razlikovanju u od c i w) i zapisati je u protokol, ili sve prebojiti u `#356b83` (5 datoteka). Nije mijenjano.
2. **Z4 otkriva rezultate.** Skica crta potpune trokute (u1, u2, w1, w2), iako zadatak traži „Izračunaj u1, u2, oba relativna vektora… Nacrtaj oba trokuta brzina”. Prijedlog: na skici ostaviti samo c1, c2 i lokalne osi (+ r1, r2, ω), a trokute prepustiti studentu; zahtijeva usklađenje `check_u14_sketch_geometry.py` (`triangle(ex,'u14ex_z4one'…)`).
3. **Z3 izlazni kut.** Lopatica je nacrtana s izlazom točno pod traženim β2 = 150° (checker to zahtijeva). Kut nije označen, ali se može izmjeriti. Prijedlog: izlaz nacrtati pod neutralnim kutom (npr. 140°) uz napomenu „smjer w2 shematski” ili prihvatiti.
4. ~~P3 (Pelton) — krak r.~~ **Ispravljeno** (nalog koordinatora), vidi „Dopuna” dolje.
5. **Oznake u tekstu (vidi rječnik):** β s četiri referentna smjera (θ je po standardu kut skretanja); w_s prema w; α kao kut reakcije u P1; v umjesto v_d i η kao faktor učinka u P5; alt-tekst slike diska navodi „vw” umjesto v_j.

### Poglavlje 15

1. **Oznaka brzine u silovitom području (uvodna skica).** Tekst joj ne daje oznaku; na skici je „vs” (sada v_s), što se sudara s v_s (brzina broda, okvir „Fizikalno značenje” istog poglavlja i standard). Tumačenje skice istodobno koristi indeks 1 za početnu mirnu dubinu (y1 = 1,30 m) i za „silovit presjek 1” skoka. Prijedlog: u tekstu i na skici uvesti npr. y_a, v_a (ili y_s′) za silovit presjek ispred skoka, ili prenumerirati presjeke 1–2–3; tada uskladiti oznaku na skici.
2. **Skice zadataka koje grafički daju rezultat:** Z1 (smjer v − c, tj. da poremećaj putuje uzvodno, i omjeri brzina), Z2 (označen minimum na točnoj krivulji s podjelama osi → y_c ≈ 0,97 m, E_min ≈ 1,46 m), Z6 (nacrtan izračunati y2 = 1,06 m ispod crte y_2,dop = 1,40 m). Checker sve to namjerno kodira („stvarna potpisana brzina”, „minimum daje Fr = 1”, „spregnute dubine”). Prijedlog: ukloniti točku/projekciju minimuma u Z2 i nacrtati v − c bez predznaka (npr. dvosmjerna strelica „v ± c”), a y2 u Z6 shematski — uz usklađenje `check_u15_sketch_geometry.py`; ili izričito prihvatiti kao pomoć studentu.
3. **Oznake u tekstu (vidi rječnik):** y_t dvoznačan (P5 nizvodni vodostaj, Z4 dubina na tjemenu); z (visina dna i pokos); H (energijska visina iznad krune i konstrukcijska dubina); h_L umjesto h_w/h_l; R rezidual uz R_h; h kao dubina u okviru o brodu.

### Bilježnice

1. **u04 laboratorij, mjerilo presjeka.** Gornji panel „Presjek otvorenog spremnika” nema
   jednako mjerilo osi; okomito je sabijen oko 3×, pa paraboloid izgleda plići. Prijedlog:
   `ax.set_aspect('equal', adjustable='datalim')`. To mijenja izgled laboratorija; nakon izmjene
   treba pokrenuti `audit_interactive_labs.mjs`.
2. **u12_poiseuille, brzina fluida $u$.** Markdown laboratorija (
   $\frac{d}{dr}(r\,du/dr)$ …), kod i osi koriste $u$ za brzinu fluida. Knjiga (u12, r. 623)
   koristi $v(r)$, $v(y)$, a $u$ za brzinu ploče. Z4 markdown piše „$U=2{,}00$ m/s”, a tekst $u$.
   Graf Z4 je usklađen s knjigom ($v$), ostatak nije. Prijedlog: preimenovati u cijeloj bilježnici
   ($u\to v$, $U\to u$).
3. **u05_sila_na_ravnu_plohu, notacija modela.** Markdown: „Kut $\alpha$ ovdje je izričito mjeren
   **od vertikale**; gornji rub nalazi se na dubini $h_t$”. Tekst (r. 124, 236): $\theta$ prema
   vodoravnici, $h_0$/$h_A$, b širina i L duljina niz plohu. Bilježnica ima obrnute uloge b i L,
   a α je prema standardu korekcijski faktor. Prijedlog: prijeći na θ od vodoravnice, $h_0$, b i L
   kao u tekstu (mijenja `analiticka_ploha` i markdown).
4. **u07, u08, u09_kompresibilna, u12_pelton (Z5), u13: notacija markdowna i koda.**
   u07 $d$ → $T$, $F_B$ → $F_U$, „slobodni bok” → nadvođe $f$; u08 $Q_{in}$/$Q_{out}$ →
   $Q_{ul}$/$Q_{iz}$; u09k $M$, `gamma` → $Ma$, $\kappa$; u12p Z5 „T, U, TU” → $F_T$, $v_s$,
   $F_Tv_s$; u13 ključ `K` (lokalni koeficijent) → $\xi$. Grafovi su usklađeni gdje te oznake
   prikazuju; tekst bilježnica nisam mijenjao jer je izvan opsega crteža.
5. **Izvor U04, dvije oznake za istu veličinu (ne pogađam).** r. 5: „paraboloid
   $z(r)=z_C+\omega^2r^2/(2g)$”, a r. 147 i 445: „$h_C$ visina površine na osi”. Zato u u04
   grafu nije dodan simbol razine na osi.
6. **Izvor U15, ista oznaka za dvije veličine.** $y_t$ je nizvodni vodostaj u r. 294 i 313
   („nizvodni vodostaj kanala iznosi $y_t=1{,}00$ m”) i dubina na tjemenu praga u r. 509
   („odaberi dubinu $y_t$ te njezin $Fr_t$”). Graf Z4 koristi $y_t$ za tjeme prema Z4.
7. **Decimalni zarez na osima.** Matplotlib na svim grafovima prikazuje decimalnu točku na
   oznakama osi (npr. 0.25). Oznake u legendama i naslovima koje sam mijenjao imaju zarez.
   Globalna promjena (npr. `axes.formatter.use_locale` uz hr_HR ili vlastiti formatter u svih
   17 bilježnica) zasebna je odluka.
8. **u11 poligon sila.** Trokut je fizikalno gotovo degeneriran (121 N prema oko 2000 N). Sada je
   čitljiv. Ako treba naglasiti zatvaranje, moguć je umetak s uvećanim vrhom ili tekstualni
   iznos $|\dot m\Delta\vec v|$.
