# QA log — Faza 1 (svibanj 2026)

Tracking dokument za Fazu 1 plana iz `~/.claude/plans/pro-itaj-to-u-folderu-federated-moore.md`.
Cilj faze: sekvencijalni QA prolaz kroz U01–U13 (riješeni primjeri + zadaci za vježbu + SVG skice), uz numeričku verifikaciju kroz `tools/verify_uXX.py`.

## Polazni inventar (utvrđeno u exploration fazi)

- 91 riješenih primjera, 79 zadataka, 14 cjelovitih (T3/T4), 26 aplikativnih (13 strojarstvo + 13 građevina) preko 13 poglavlja.
- 93 SVG datoteke u [assets/print/](assets/print/).
- Didaktičke rupe (procjena): nisko = U01–U03, U08, U09, U12; srednje = U05, U06, U10, U11, U13.

## Foundation log

### A1–A2: Strukturna normalizacija SVG-a — `zatvoreno`

- Skripta [tools/svg_normalize.py](tools/svg_normalize.py) prefiksira ID-eve po datoteci, popravi `font-family` na kanonski `'Segoe UI',Arial,sans-serif`, dodaje `preserveAspectRatio` i responsive `style`, ažurira `url(#...)`, `href="#..."` i `aria-labelledby` reference.
- Pokrenuto jednokratno nad 93 SVG datoteke; idempotentno (drugi run = 0 izmjena).
- Log: [tools/svg_normalize.log](tools/svg_normalize.log).

### A3: Orphan SVG analiza — `riješeno (ne briše se)`

- [assets/print/u07_val3_dva_fluida_modul.svg](assets/print/u07_val3_dva_fluida_modul.svg) inicijalno označen kao orphan jer nije referenciran u nijednom `source/*.md`.
- Stvarno stanje: SVG je pripremljena zamjena za matplotlib blok `fig-u07-kalibracijski-modul` u [source/u07_uzgon_plivanje_i_stabilnost.md](source/u07_uzgon_plivanje_i_stabilnost.md):518–593.
- Akcija: ostaviti datoteku; spojiti je s primjerom u Phase B-U07.

### A4: Statusni dokument ažuriran — `zatvoreno`

- [status_izrade_udzbenika.md](status_izrade_udzbenika.md) reflektira točno stanje SVG konverzije i bilježi pokretanje Faze 1.

### A6: Numerička verifikacija harness — vidi sekciju ispod

## Inventar preostalih matplotlib blokova (otkriveno u Foundation fazi)

Tri prethodna statusna teksta govorila su "U01–U04 su potpuno konvertirani; ostalo selektivno". Točan stvarni inventar (grep ` ```{python} ` u `source/`):

| Poglavlje | Matplotlib blokova |
|-----------|--------------------|
| U01 | 1 |
| U02 | 0 |
| U03 | 0 |
| U04 | 0 |
| U05 | 0 |
| U06 | 0 |
| **U07** | **5** |
| U08 | 3 |
| U09 | 3 |
| U10 | 4 |
| U11 | 3 |
| U12 | 4 |
| U13 | 3 |
| **Ukupno** | **26** |

Svi ti blokovi moraju biti zamijenjeni statičkim SVG-om kroz pripadajući Phase B-UXX prolaz. Za neke postoje pripremljeni SVG-ovi (npr. `u07_val3_dva_fluida_modul.svg`), za većinu treba autorska skica.

## Per-chapter prolaz

Za svako poglavlje popunjava se sekcija po sljedećoj predlošci:

```
### B-UXX: <naslov> — `<status>`

**Datum start**: ...
**Datum zatvaranja**: ...

**1. Tekst Primjeri**
- Primjer X.Y — ime
  - nalazi: ...
  - fixevi: ...

**2. Tekst Zadaci**
- Zadatak X.Y — ime
  - nalazi: ...
  - fixevi: ...

**3. SVG skice**
- uXX_*.svg — fizikalna/matematička provjera, palette, oznake
  - nalazi: ...
  - fixevi: ...

**4. Matplotlib → SVG konverzija**
- broj blokova, status

**5. Didaktičke rupe i novi sadržaj**
- prijedlozi, odluke, dodavanja

**6. Numerička verifikacija (`tools/verify_uXX.py`)**
- stanje SymPy/numpy provjere

**7. Lokalni render check**
- `quarto render chapters/uXX_*.qmd` — rezultat
```

### B-U01: Osnove fluida i Pascalov zakon — `u tijeku` (čeka odluke autora o sistemskim popravcima)

**Datum start**: 2026-05-18

#### Inventar

- 1 kratki primjer (T1): Gustoća, specifična težina i relativna gustoća ulja → [u01_fig_gustoca_sr.svg](assets/print/u01_fig_gustoca_sr.svg)
- 3 riješena primjera u sekciji "Riješeni primjeri":
  - Primjer 1 (T2): Opterećeni klip → [u01_val1_klip_manometar.svg](assets/print/u01_val1_klip_manometar.svg)
  - Primjer 2 (T2): Servisna hidraulična dizalica → [u01_val2_hidraulicna_dizalica.svg](assets/print/u01_val2_hidraulicna_dizalica.svg)
  - Primjer 3 (T2): Dvostruki hidraulični podizač → [u01_val3_dvostruki_podizac.svg](assets/print/u01_val3_dvostruki_podizac.svg)
- 1 cjeloviti zadatak (T3): Dvostruka hidraulična platforma s ručnom pumpom → [u01_ch1_dvostruka_platforma_manometar.svg](assets/print/u01_ch1_dvostruka_platforma_manometar.svg)
- 2 aplikativna primjera:
  - Strojarstvo (T2): Hidraulična preša za savijanje cijevi → [u01_fig_presa_savijanje.svg](assets/print/u01_fig_presa_savijanje.svg)
  - Građevinarstvo (T2): Hidraulično podizanje mosta → [u01_fig_most_podizanje.svg](assets/print/u01_fig_most_podizanje.svg)
- 6 zadataka za vježbu (T1–T3) → [u01_vjezbe_skice.svg](assets/print/u01_vjezbe_skice.svg)
- 1 uvodna figura → [u01_fig_uvod_pregled.svg](assets/print/u01_fig_uvod_pregled.svg)

#### Tekst Primjeri (5 primjeri + 1 cjeloviti zadatak)

Pregled svih primjera kroz protokolnu checklistu (Zadano → Traženo → Skica → Pretpostavke i model → Rješenje s fizikalnim tumačenjima → Provjera i komentar):

- **Kratki primjer (Gustoća) — T1, [u01_*.md:58–114](source/u01_osnove_fluida_i_pascalov_zakon.md#L58-L114)**: ✅ struktura potpuna, fizikalna tumačenja prisutna, matematika korektna.
- **Primjer 1 (Opterećeni klip) — T2, [u01_*.md:206–289](source/u01_osnove_fluida_i_pascalov_zakon.md#L206-L289)**: ✅ struktura potpuna, fizikalna tumačenja, matematika korektna ($p = G/A_k = 179\,\text{kPa}$, $F_2 = pA_2 = 8{,}06\,\text{kN}$).
- **Primjer 2 (Servisna dizalica) — T2, [u01_*.md:291–373](source/u01_osnove_fluida_i_pascalov_zakon.md#L291-L373)**: ✅ struktura potpuna, fizikalna tumačenja, matematika korektna ($p = 250\,\text{kPa}$, $F_2 = 5{,}25\,\text{kN}$, $s_2 \approx 5{,}1\,\text{mm}$).
- **Primjer 3 (Dvostruki podizač) — T2, [u01_*.md:375–487](source/u01_osnove_fluida_i_pascalov_zakon.md#L375-L487)**: ✅ struktura potpuna, fizikalna tumačenja, matematika korektna ($p = 0{,}80\,\text{MPa}$, $F_p = 480\,\text{N}$, $s_p = 1{,}0\,\text{m}$).
- **Cjeloviti zadatak (Dvostruka platforma s ručnom pumpom) — T3, [u01_*.md:489–662](source/u01_osnove_fluida_i_pascalov_zakon.md#L489-L662)**: ✅ struktura potpuna, fizikalna tumačenja, matematika korektna ($p = 0{,}92\,\text{MPa}$, $F_L = 13{,}8\,\text{kN}$, $G = 27{,}6\,\text{kN}$, $s_p = 1{,}5\,\text{m}$, $n = 9$).
- **Primjer (Hidraulična preša) — T2, [u01_*.md:664–725](source/u01_osnove_fluida_i_pascalov_zakon.md#L664-L725)**: ✅ struktura potpuna, matematika korektna ($p \approx 0{,}40\,\text{MPa}$, $F_2 = 16F_1 = 5{,}12\,\text{kN}$, $s_2 = s_1/16 = 5{,}0\,\text{mm}$).
- **Primjer (Hidraulično podizanje mosta) — T2, [u01_*.md:727–786](source/u01_osnove_fluida_i_pascalov_zakon.md#L727-L786)**: ✅ struktura potpuna, matematika korektna ($F_{pod} = 120\,\text{kN}$, $p_{min} \approx 12{,}6\,\text{MPa}$, $p_p \approx 1{,}3\,\text{MPa}$, ručna pumpa nije dostatna).

Konkluzija: **tekstualni sloj 5 Primjera + 1 Cjelovitog zadatka prolazi sve protokolne provjere**. Matematika numericki verificirana ručno; bit će potvrđeno kroz [tools/verify_u01.py](tools/verify_u01.py).

#### Tekst Zadaci (6 zadataka u sekciji "Zadaci za vježbu")

- T1 zadatak 1 (servisna preša): ✅ Zadano/Traženo/Natuknica/Skica oznake — struktura potpuna.
- T1 zadatak 2 (dva klipa, ista grana): ✅
- T2 zadatak 3 (hidraulična stega): ✅ — uvodi traženje promjera klipa iz zadanog tlaka, dobra didaktička varijacija.
- T2 zadatak 4 (hidraulični stol, dva cilindra): ✅
- T3 zadatak 5 (ručna pumpa, dva radna cilindra): ✅ — dobar prirez ka cjelovitom zadatku.
- T3 zadatak 6 (tri jednaka cilindra): ✅ — prošireno na tri cilindra, dobro varira broj radnih jedinica.

Konkluzija: **svih 6 zadataka prolazi protokolne provjere**.

#### SVG skice — vizualna inspekcija (preko Inkscape rendera u `tools/tmp/u01_*.png`)

**A. Sistemski problemi (vidljivi u više SVG-eva, čekaju autorovu odluku za pravilo prije masovne korekcije):**

1. **Naslov skice preklapa se s oznakama veličina u gornjem dijelu canvas-a** — primijećeno u: val1 (G label preklopljen), val2 (F_1 label preklopljen), val3 (G label preklopljen), ch1 (F_e label preklopljen), most (F_p label preklopljen), preša (F_2 label upada u naslov truncating "d_1 = 32 mm" dio).
   - Uzrok: top-bar oznake i naslovni tekst koriste isti vertikalni prostor (y ≈ 30–80 px).
   - Predlog pravila: rezervirati gornjih ~70 px isključivo za naslov; sve oznake veličina pomaknuti ispod naslova.
2. **Nekonzistentna paleta za ulazne sile** — Val 1 koristi crvenu (#c0392b) za G (ulaz), Val 2 koristi plavu za F_1 (ulaz), Most koristi plavu za F_p (ulaz). Protokol [protokol_prerade_zadataka_i_skica.md](protokol_prerade_zadataka_i_skica.md) zahtijeva: ulazna sila = crvena (#c0392b), izlazna = zelena (#1e8449), tlak = plava (#1565c0). Plave strelice za F_1 i F_p nisu "ulazne sile", nego se vizualno čitaju kao tlak — semantička greška.
   - Predlog pravila: sve ulazne sile (F_p, F_1, G, F_p,pumpe) u crvenoj; izlazne (F_2, F_pod, F_R, F_L na radnom cilindru kao reakcija prema gore) u zelenoj; tlak strelice u fluidu u plavoj.
3. **Oznake u skici NE odgovaraju oznakama u tekstu zadatka** — najkritičniji nalaz: Val 3 i CH 1 koriste $A_e, F_e$ za radne cilindre, dok tekst koristi $A_L, F_L$. Most koristi $F_{p01}, p_{t3a}$ što uopće nije u tekstu (tekst: $F_{pod}, p_{min}$).
   - Ovo je upravo problem koji autorka eksplicitno spominje: "skice fizikalno i matematički nekorektne". Doslovno — oznake su semantički netočne jer ih tekst ne uvodi.
   - Predlog pravila: skica je vezana za točno onaj tekst zadatka koji je ispred nje; oznake u skici moraju biti **doslovni isti string** kao u Zadano/Rješenje. Nije dopušteno uvoditi nove oznake u skici koje tekst ne koristi.

**B. Specifični nalazi po SVG-u:**

- **[u01_fig_uvod_pregled.svg](assets/print/u01_fig_uvod_pregled.svg)** — render: tri panela (kontinuumski model, osnovne veličine ρ/γ/sr, Pascalov zakon). Pregled poglavlja ✓. Treba veću render rezoluciju za detaljnu kritiku. Inicijalno: layout OK, paleta voda plava + ulje žuto-zlatno + stijenke sive ✓.

- **[u01_fig_gustoca_sr.svg](assets/print/u01_fig_gustoca_sr.svg)** — render: dvopanelni prikaz ulja s gustoćom 860 i usporedba 1L ulja vs 1L vode. **Status: dobar**. Boje konzistentne s palettom, kote smeđe, srafurane stijenke, $\Delta G \approx 14\%$ jasno označeno. Nema sistemskih problema.

- **[u01_val1_klip_manometar.svg](assets/print/u01_val1_klip_manometar.svg)** — fizikalno korektno, brojevi se podudaraju s tekstom ($A_k \approx 201\,\text{cm}^2$, $p \approx 179\,\text{kPa}$, $F_2 \approx 8{,}06\,\text{kN}$, $A_2 = 450\,\text{cm}^2$ ✓). Smjer sila G crvena dolje ✓, F_2 zelena gore ✓, tlak strelice plave ✓. **Problem**: G label preklopljen s naslovom.

- **[u01_val2_hidraulicna_dizalica.svg](assets/print/u01_val2_hidraulicna_dizalica.svg)** — brojevi se podudaraju ($A_1=6\,\text{cm}^2$, $A_2=210\,\text{cm}^2$, $p=250\,\text{kPa}$, $F_2=5{,}25\,\text{kN}$, $s_2 \approx 5{,}1\,\text{mm}$ ✓). **Problemi**: (i) F_1 plava umjesto crvena (palette), (ii) F_1 label preklopljen s naslovom, (iii) "150·0,18 = 5250·0,0051 ✓" je $27 = 26{,}775$ — to NIJE `=` već `≈` (zaokruženje); treba zamijeniti `=` s `≈` ili napisati $F_1 s_1 \approx F_2 s_2$.

- **[u01_val3_dvostruki_podizac.svg](assets/print/u01_val3_dvostruki_podizac.svg)** — **kritični nalaz**: oznake $A_e, F_e$ u skici, ali tekst koristi $A_L, F_L$. Inače brojevi se podudaraju ($G=24\,\text{kN}$, $A_L=150\,\text{cm}^2$, $A_p=6\,\text{cm}^2$, $p=0{,}80\,\text{MPa}$, $F_p=480\,\text{N}$, $\sum s_p = 1{,}0\,\text{m}$ ✓). Smjerovi sila: G crvena dolje ✓, $F_e$ zelena gore ✓, $F_p$ plava dolje ❌ (treba crvena), $s_p$ smeđa ✓.

- **[u01_ch1_dvostruka_platforma_manometar.svg](assets/print/u01_ch1_dvostruka_platforma_manometar.svg)** — isti problem oznaka kao Val 3 ($A_e, F_e$ vs $A_L, F_L$ u tekstu). Brojevi se podudaraju ($G=27{,}6\,\text{kN}$, $p=0{,}92\,\text{MPa}$, $F_p=460\,\text{N}$, $\sum s_p = 1{,}5\,\text{m}$, $n=9$ ✓). $F_p$ plava treba biti crvena.

- **[u01_fig_presa_savijanje.svg](assets/print/u01_fig_presa_savijanje.svg)** — **paleta korektno**: $F_1=320\,\text{N}$ **crvena** ✓ (ulaz), $F_2=5{,}12\,\text{kN}$ **zelena** ✓ (izlaz), $p=0{,}40\,\text{MPa}$ plava ✓, tlak strelice u fluidu plave ✓. Brojevi se podudaraju s tekstom. **Problem**: naslov truncated/preklopljen s $F_2$ oznakom ("$d_1 = 32\,\text{mm}$ dio nestaje iza naslova"). Inače: ovo je jedini Val/Fig/CH SVG koji **prati paletu protokola**.

- **[u01_fig_most_podizanje.svg](assets/print/u01_fig_most_podizanje.svg)** — više problema: (i) $F_p$ plava dolje (treba crvena, ulaz). (ii) Oznake $F_{p01}$, $p_{t3a}$ nisu u tekstu — tekst koristi $F_{pod}$, $p_{min}$. (iii) Naslov preklopljen s $F_p$ oznakom. (iv) Layout pregusto, vrlo malen tekst pri zumiranju. Inače brojevi se podudaraju ($G=480\,\text{kN}$, $d=110\,\text{mm}$, $d_p=22\,\text{mm}$, $F_p=500\,\text{N}$, $p_{min}=12{,}6\,\text{MPa}$, $p_p=1{,}3\,\text{MPa}$ ✓).

- **[u01_vjezbe_skice.svg](assets/print/u01_vjezbe_skice.svg)** — 6 mini skica u 2×3 grid za T1–T6 zadatke. Stiliziraly grayscale ✓. Treba veću render rezoluciju za detaljnu kritiku oznaka. Inicijalno: layout OK, ali tekst sitan; rebriefirati pri implementaciji popravaka.

#### Matplotlib → SVG konverzija — `zatvoreno`

- 1 matplotlib blok identificiran, već je bio dead code (`#| eval: false`, label `fig-u01-most-podizanje-UNUSED`).
- Akcija: obrisan blok (linije 749–908 u izvoru), -161 redaka, -6266 znakova; izvor je sada matplotlib-free.

#### Didaktičke rupe i prijedlozi novog sadržaja

- Pokrivenost: gustoća i specifična težina (kratki primjer), tlak iz F/A (Val 1), Pascalov zakon s dva klipa (Val 2), višeklipni hidraulični sustav (Val 3 + CH 1), pojačanje sile (Preša), neostvariv ručni pogon (Most).
- Eventualni prostor za dodavanje (NIJE prioritet — autor ocijeniti):
  - Mali fizikalni-konceptualni primjer "Pascalov zakon u svakodnevnom životu" (npr. zubarska brizgalica, hidraulična kočnica) bez računa, kao motivacija prije Val 1.
  - Primjer s pretvorbom mjernih jedinica (cm² ↔ m², bar ↔ Pa) — sada studenti dobivaju to "uzgredno" u svakom primjeru, ali eksplicitan kratki Primjer/Zadatak s naglaskom na pretvorbu nije prisutan.
- Predlog: **bez novih primjera ili zadataka u U01** — pokrivenost je ekstenzivna i didaktička gradacija T1→T3 dobro vodi.

#### Numerička verifikacija — `zatvoreno` ([tools/verify_u01.py](tools/verify_u01.py))

- 29 checkova; 28 prolaze direktno, 1 pokazuje 1,15% odstupanje od navedene vrijednosti:
  - `U01.most.p_p_MPa`: izračun daje $p_p = 1{,}315$ MPa, ali tekst zaokružuje na $p_p \approx 1{,}3$ MPa (vidi [u01_*.md:776–779](source/u01_osnove_fluida_i_pascalov_zakon.md)).
  - To NIJE matematička greška — samo zaokruženje teksta na jednu decimalu. Preciznije je $1{,}32$ MPa.
  - **Predlog**: u tekstu zamijeniti `≈ 1{,}3 MPa` s `≈ 1{,}32 MPa` radi konzistentnog zaokruživanja (ostali tlakovi u istom primjeru imaju dvije značajne znamenke).
- Skripta integrirana u [tools/verify_all.py](tools/verify_all.py) runner.

#### Implementacija SVG popravaka — `zatvoreno`

Autorske odluke (potvrđene 2026-05-18):
1. Skica se prilagođava tekstu (tekst je kanon za oznake).
2. Ulazne sile crvene, izlazne zelene — masovno.
3. Naslovi se uklanjaju iz SVG-a (caption u Markdownu pokriva tu ulogu).

Provedeni popravci po SVG-u:

- **[u01_fig_uvod_pregled.svg](assets/print/u01_fig_uvod_pregled.svg)**: uklonjen "U01 – Osnove fluida i Pascalov zakon" naslov i podnaslov.
- **[u01_fig_gustoca_sr.svg](assets/print/u01_fig_gustoca_sr.svg)**: nema SVG-level naslova (samo panel oznake "Ulje u posudi", "Usporedba: isti volumen V = 1 L" — to su sub-figure labele, ne SVG title). Nepromijenjeno.
- **[u01_val1_klip_manometar.svg](assets/print/u01_val1_klip_manometar.svg)**: uklonjen naslov. Sad: G crvena (ulaz) ✓, F_2 zelena (izlaz) ✓, p plava (tlak) ✓.
- **[u01_val2_hidraulicna_dizalica.svg](assets/print/u01_val2_hidraulicna_dizalica.svg)**: uklonjen naslov; F_1 plava→crvena (stroke, marker, fill, legenda); legenda razdvojena na 4 stavke (ulaz F_1 / tlak p / izlaz F_2 / hodovi); `150·0,18 = 5250·0,0051` → `150·0,18 ≈ 5250·0,0051`.
- **[u01_val3_dvostruki_podizac.svg](assets/print/u01_val3_dvostruki_podizac.svg)**: uklonjen naslov; replace_all `A_e → A_L` (kroz tspan), `F_e → F_L`, `s_e → s_L`; F_p plava→crvena; legenda update.
- **[u01_ch1_dvostruka_platforma_manometar.svg](assets/print/u01_ch1_dvostruka_platforma_manometar.svg)**: uklonjen naslov; replace_all `A_e → A_L`, `F_e → F_L`, `s_e → s_L`; `s_k → s_h` (greška u oznaci puni hod pumpe); F_p plava→crvena; legenda update.
- **[u01_fig_presa_savijanje.svg](assets/print/u01_fig_presa_savijanje.svg)**: uklonjen naslov. Paleta već bila ispravna.
- **[u01_fig_most_podizanje.svg](assets/print/u01_fig_most_podizanje.svg)**: uklonjen naslov i podnaslov; replace_all `F_p01 → F_pod`, `A_p01 → A_pod`, `p_t3n → p_min` (svi sa tspan subscript); F_p plava→crvena.
- **[u01_vjezbe_skice.svg](assets/print/u01_vjezbe_skice.svg)**: nema SVG-level naslova (samo panel oznake "T1 — ...", "T2 — ..." što su sub-figure labele). Nepromijenjeno.

Re-render kroz Inkscape i vizualna provjera potvrdili sve promjene. PNG izlazi u [tools/tmp/u01_*.png](tools/tmp/).

**Reziduali (manji, ne sistemski)**:
- Val3 i CH1: oznaka $G$ u sredini (na platformi) malo se preklapa s $F_L$ labelom između cilindara. Layout pomak ali bez funkcijske greške; ostavlja se za eventualan polishing.

#### Stanje U01 — `zatvoreno za Fazu 1`

Datum zatvaranja: 2026-05-18.

Što je gotovo:
- Tekstualni sloj 5 Primjera + 1 Cjelovitog zadatka prošao protokolnu provjeru.
- Svih 6 zadataka za vježbu prošlo protokolnu provjeru.
- 1 dead matplotlib blok obrisan (-161 redaka).
- 9 SVG-eva: naslovi uklonjeni, ulazne sile crvene per protokol, oznake u skicama doslovno usklađene s tekstom.
- 29 SymPy provjera ([tools/verify_u01.py](tools/verify_u01.py)) sve ispravne (28 direktnih + 1 rounding-artifact u $p_p$).

Otvoreni mali fixevi za autorov pregled:
- U tekstu zamijeniti `p_p ≈ 1,3 MPa` s `p_p ≈ 1,32 MPa` ili podići toleranciju verify checka.
- Val3/CH1: G label u sredini canvas-a (pomak za 8–10 px udesno) da ne taknete F_L label.

#### Lokalni render check — `odgođeno`

- `quarto` CLI nije pronađen u sustavnom PATH-u niti na standardnim lokacijama (`Program Files\Quarto\bin\quarto.exe`, `LocalAppData\Programs\Quarto`).
- Akcija: render check provesti pri završnom pregledu (Faza C) kad autorka potvrdi gdje je Quarto instaliran, ili pred kraj kad se proveze puni `quarto render` iz njenog uobičajenog terminala.
- Strukturalne SVG promjene (samo prefiksiranje ID-eva, font, aria) ne mijenjaju vizualni output, pa render nije vraćen unazad. Brisanje mrtvog matplotlib bloka (već `eval: false`) također neutralan utjecaj na render.

### B-U02: Viskoznost, površinska napetost i kapilarnost — `zatvoreno`

**Datum start/zatvaranja**: 2026-05-18.

#### Inventar
- 1 kratki primjer (T1, [u02_*.md:123–162](source/u02_viskoznost_povrsinska_napetost_i_kapilarnost.md#L123-L162)): Pretvorba dinamičke u kinematičku viskoznost → [u02_fig_kinematicka_viskoznost.svg](assets/print/u02_fig_kinematicka_viskoznost.svg).
- 5 riješenih primjera:
  - P1 (T2, smično naprezanje u uljnom sloju) → [u02_val2_viskoznost_kapilarnost.svg](assets/print/u02_val2_viskoznost_kapilarnost.svg)
  - P2 (T1, kapilarni uspon etanola) → [u02_fig_kapilarni_uspon_etanol.svg](assets/print/u02_fig_kapilarni_uspon_etanol.svg)
  - P3 (T1, tlakovni skok u kapljici) → [u02_val3_tlacni_skok_kapljica.svg](assets/print/u02_val3_tlacni_skok_kapljica.svg)
  - P4 strojarstvo (T2, klizni ležaj) → [u02_fig_klizni_lezaj.svg](assets/print/u02_fig_klizni_lezaj.svg)
  - P5 građevinarstvo (T1, vlaga kroz opečni zid) → [u02_fig_kapilarna_vlaga_zid.svg](assets/print/u02_fig_kapilarna_vlaga_zid.svg)
- 1 cjeloviti zadatak (T3, kapilarni mikrodozator) → [u02_ch1_kapilarni_mikrodozator_kapljica.svg](assets/print/u02_ch1_kapilarni_mikrodozator_kapljica.svg)
- 6 zadataka za vježbu → [u02_vjezbe_skice.svg](assets/print/u02_vjezbe_skice.svg)
- 1 uvodna figura → [u02_fig_uvod_pregled.svg](assets/print/u02_fig_uvod_pregled.svg)

#### Tekst Primjeri + Zadaci — `prolaze`
Svi primjeri (kratki, P1–P5, cjeloviti zadatak) i 6 zadataka prolaze protokolne provjere: Zadano, Traženo, Skica, Pretpostavke i model, Rješenje s fizikalnim tumačenjima, Provjera i komentar. Matematika ručno verificirana, potvrđena kroz SymPy (vidi dolje).

#### SVG popravci — `gotovo`
Primijenjeno pravilo iz B-U01: naslovi uklonjeni iz svih 9 SVG-eva (caption u Markdownu pokriva). Paleta i oznake bile su uglavnom ispravne — niti jedan SVG nije imao $A_e/F_e$ ili plave ulazne sile (pattern iz U01 ne ponavlja se).

Konkretni popravci (svi: ukloniti SVG-level naslov + opcijski podnaslov):
- [u02_fig_uvod_pregled.svg](assets/print/u02_fig_uvod_pregled.svg): uklonjen "U02 – Viskoznost..." naslov i header bar.
- [u02_fig_kinematicka_viskoznost.svg](assets/print/u02_fig_kinematicka_viskoznost.svg): uklonjen "Kinematička viskoznost..." naslov.
- [u02_val2_viskoznost_kapilarnost.svg](assets/print/u02_val2_viskoznost_kapilarnost.svg): uklonjen "U02 – Smicanje između ploča..." naslov; panel sub-titlovi ostaju.
- [u02_fig_kapilarni_uspon_etanol.svg](assets/print/u02_fig_kapilarni_uspon_etanol.svg): uklonjen naslov.
- [u02_val3_tlacni_skok_kapljica.svg](assets/print/u02_val3_tlacni_skok_kapljica.svg): uklonjen naslov.
- [u02_ch1_kapilarni_mikrodozator_kapljica.svg](assets/print/u02_ch1_kapilarni_mikrodozator_kapljica.svg): uklonjen naslov.
- [u02_fig_klizni_lezaj.svg](assets/print/u02_fig_klizni_lezaj.svg): uklonjen naslov.
- [u02_fig_kapilarna_vlaga_zid.svg](assets/print/u02_fig_kapilarna_vlaga_zid.svg): uklonjen naslov.
- [u02_vjezbe_skice.svg](assets/print/u02_vjezbe_skice.svg): uklonjen "U02 – Skice zadataka T1–T6" naslov; T1–T6 panel labele ostaju.

Re-render kroz Inkscape potvrđuje da svi SVG-evi izgledaju kako treba — panel sub-titlovi, kote, oznake doslovno match tekst.

#### Numerička verifikacija — `OK 25/25` ([tools/verify_u02.py](tools/verify_u02.py))
Sve provjere prolaze bez izuzetka. Pokriva: kratki primjer (ν=2,0·10⁻⁴), P1 (dv/dy=300, τ=126, F=22,7, ν=4,83·10⁻⁴), P2 (h=10,8 mm), P3 (Δp=240, p_in=101 565, Δp_2=480), CH1 (h_cap=36,8 mm, Δp=120, p_M,min=347 Pa), P4 ležaj (v=4,56, τ=2280, F=34,4, M=1,03), P5 vlaga (h=18,8 cm, h_2=37,6 cm), Z1–Z6 (fizikalna razumnost).

### B-U03: Hidrostatička raspodjela tlaka i manometrija — `zatvoreno`

**Datum start/zatvaranja**: 2026-05-18.

#### Inventar
- 4 Riješena primjera u sekciji "Riješeni primjeri" (P1–P4): zatvoreni spremnik, klip + komore, diferencijalni manometar, vakuumski spremnik.
- 1 cjeloviti zadatak (T3): zatvoreni vodeni + uljni referentni spremnik + živin manometar.
- 2 aplikativna primjera: pumpa na usisu (T2 strojarstvo), distribucijska mreža iz vodotornja (T1 građevinarstvo).
- 6 zadataka za vježbu (T1–T3).
- 10 SVG datoteka: [u03_fig_uvod_pregled](assets/print/u03_fig_uvod_pregled.svg), [u03_fig_zatvoreni_spremnik_tlak](assets/print/u03_fig_zatvoreni_spremnik_tlak.svg), [u03_val2_klip_komore](assets/print/u03_val2_klip_komore.svg), [u03_val1_diferencijalni_manometar](assets/print/u03_val1_diferencijalni_manometar.svg), [u03_val3_vakuumski_spremnik](assets/print/u03_val3_vakuumski_spremnik.svg), [u03_ch1_zatvoreni_spremnik_ulje_ziva](assets/print/u03_ch1_zatvoreni_spremnik_ulje_ziva.svg), [u03_balans_tlaka_i_geff](assets/print/u03_balans_tlaka_i_geff.svg) (teorijska ilustracija), [u03_fig_pumpa_usis](assets/print/u03_fig_pumpa_usis.svg), [u03_fig_vodotoranj_distribucija](assets/print/u03_fig_vodotoranj_distribucija.svg), [u03_vjezbe_skice](assets/print/u03_vjezbe_skice.svg).

#### Tekst Primjeri + Zadaci — `prolaze`
Svi primjeri (P1–P4 + cjeloviti + P5–P6 aplikativni) i 6 zadataka prolaze protokolne provjere. Matematika korektna, fizikalna tumačenja prisutna.

#### SVG popravci — `gotovo`
Primijenjeno pravilo: ukloniti SVG-level naslove. **7 od 10 SVG-eva imalo je top-level naslov koji se uklonio** (uvod, zatvoreni_spremnik_tlak, ch1, balans_tlaka_i_geff, pumpa_usis, vodotoranj_distribucija, vjezbe_skice). **3 SVG-eva nisu imala top-level naslov** (val1, val2, val3 koriste info-box headers na desnoj strani što su panel labele, ne SVG titlovi) — nepromijenjeno.

Paleta i oznake: bez sistemskih problema; ulazne sile crvene (G na klip u val2, p_atm i p_0 strelice), tlak plave, oznake match tekst.

#### Numerička verifikacija — `OK 31/31` ([tools/verify_u03.py](tools/verify_u03.py))
Pokriva: P1 (p_G=118,8 kPa, p_A=132,5 kPa, p_A,m=31,7 kPa), P2 (A_k=707 cm², p_c=353,6 Pa, p_A=2806 Pa, p_B=-2099 Pa), P3 (Δp=3394/3402 Pa s/bez zraka), P4 (p_g=77,3 kPa, p_g,m=-24,0 kPa, p_A=89,1 kPa, p_A,m=-12,2 kPa), CH1 (p_1=129,1, p_2=105,9, p_G=121,2, p_C=133,0 kPa), P5 pumpa (p_man=-20,5 kPa, p_aps=80,8 kPa, H_max=11,8 m), P6 vodotoranj (ΔH=16 m, p_man=156,7 kPa, p_aps=257,2 kPa), Z1–Z6 (fizikalna razumnost).

### B-U04: Relativno mirovanje fluida — `zatvoreno`

**Datum start/zatvaranja**: 2026-05-18.

#### Inventar
- 4 Riješena primjera (P1–P4): laboratorijska kolica, procesna kada, zatvoreni modul s kosom stijenkom, rotirajući cilindar.
- 1 cjeloviti zadatak (T3): rotirajući cilindar s granicom prelijevanja.
- 2 aplikativna primjera: autocisterna pri kočenju (T2 strojarstvo), vatrogasna cisterna pri zaustavljanju (T2 građevinarstvo).
- 6 zadataka za vježbu (T1–T3).
- 9 SVG datoteka: [u04_fig_uvod_pregled](assets/print/u04_fig_uvod_pregled.svg), [u04_val2_laboratorijska_kolica](assets/print/u04_val2_laboratorijska_kolica.svg), [u04_val1_procesna_kada](assets/print/u04_val1_procesna_kada.svg), [u04_val3_kosa_stijenka](assets/print/u04_val3_kosa_stijenka.svg), [u04_fig_rotirajuci_cilindar](assets/print/u04_fig_rotirajuci_cilindar.svg), [u04_ch1_rotirajuci_spremnik_paraboloid](assets/print/u04_ch1_rotirajuci_spremnik_paraboloid.svg), [u04_fig_autocisterna_kocenje](assets/print/u04_fig_autocisterna_kocenje.svg), [u04_fig_vatrogasna_cisterna](assets/print/u04_fig_vatrogasna_cisterna.svg), [u04_vjezbe_skice](assets/print/u04_vjezbe_skice.svg).

#### Tekst Primjeri + Zadaci — `prolaze`
Svi primjeri i zadaci prolaze protokolne provjere. Posebno snažan didaktički luk: P1 (najjednostavnije ubrzanje) → P2 (granično prelijevanje + sila) → P3 (kosa stijenka + plinski pretlak) → P4 (rotacija) → CH1 (rotacija s granicom prelijevanja).

#### SVG popravci — `gotovo`
9 SVG-eva: naslovi uklonjeni (svih devet imalo SVG-level naslov u top-baru ili header gradient bar; po pravilima Faze 1 caption u Markdownu pokriva tu ulogu).

Napomena za buduće autorske odluke (ostavljeno za polishing kasnije, ne mijenja se sada):
- val1, val2, val3 koriste boje malo izvan kanonske palete: blue za vektor ubrzanja $a$ koristi `#1976d2` (kanon: `#1565c0`), narančasta za kote `#c96c35` (kanon: `#b7600c`), crvena za rezultantnu silu `#c23b22` (kanon: `#c0392b`), zelena `#2e7d32` (kanon: `#1e8449`). Razlike su minimalne i ne mijenjaju semantičko čitanje; mogu se kasnije usuglasiti masovnim search-replace.
- F_R u val1 je crvena prema protokolu bi trebala biti zelena (izlazna/rezultantna), ali u kontekstu "sila fluida koja udara stijenku" semantika crvene kao ulazne sile također ima smisla. Ostavljam autoru na odluku.

#### Numerička verifikacija — `OK 38/38` ([tools/verify_u04.py](tools/verify_u04.py))
Pokriva sve: P1 (Δh=0,220 m, h_str=0,530, h_pred=0,310, θ=7,9°), P2 (h_pred=0,36, a_max=1,962 m/s², F_R=2343 N), P3 (θ=19,1°, α=70,9°, s=0,582 m, g_eff=10,38, F_0=9312, F_h=1688, F_R=11000, y_R=0,306), P4 (Δh=0,225, h_rub=0,393, h_osa=0,168), CH1 (Δh=0,2205, h_C=0,490, h_R=0,710, p_M_C=4804, p_M_D=6968, ω_max=6,64, n_max=63,4), P5 autocisterna (Δh=0,465, h_pred=0,683, h_str=0,217), P6 vatrogasna (Δh=1,101, h_pred=1,751, h_str=0,650, θ=24,7°), Z1–Z6 (fizikalna razumnost).

### B-U05: Hidrostatske sile na ravne plohe — `zatvoreno`

**Datum start/zatvaranja**: 2026-05-18.

#### Inventar
- 3 Riješena primjera (P1–P3): vertikalna pravokutna zaklopka, vertikalna stijenka s tri ukrute, kosi inspekcijski poklopac.
- 1 cjeloviti zadatak (T3): zglobna pregrada s uljem iznad vode.
- 2 aplikativna primjera: inspekcijski poklopac kotla (T2 strojarstvo), brodska vrata brane (T2 građevinarstvo).
- 6 zadataka za vježbu (T1–T3).
- 8 SVG datoteka: [u05_fig_uvod_pregled](assets/print/u05_fig_uvod_pregled.svg), [u05_val1_pravokutna_zaklopka](assets/print/u05_val1_pravokutna_zaklopka.svg), [u05_val2_ukrute_stijenke](assets/print/u05_val2_ukrute_stijenke.svg), [u05_val3_kosi_poklopac](assets/print/u05_val3_kosi_poklopac.svg), [u05_ch1_pregrada_ulje_voda](assets/print/u05_ch1_pregrada_ulje_voda.svg), [u05_fig_inspekcijski_poklopac](assets/print/u05_fig_inspekcijski_poklopac.svg), [u05_fig_brodska_vrata_brane](assets/print/u05_fig_brodska_vrata_brane.svg), [u05_vjezbe_skice](assets/print/u05_vjezbe_skice.svg).

#### Tekst Primjeri + Zadaci — `prolaze`
Sve primjere (P1–P3 + cjeloviti + P5–P6 aplikativni) i 6 zadataka prolaze protokolne provjere. Posebno snažan didaktički luk: P1 (jedna ploha → jedna rezultanta) → P2 (jedna stijena podijeljena u 4 pojasa jednakih sila) → P3 (kosi poklopac sa zglobom) → CH1 (uslojeno: ulje + voda + zglob + spojnica). Iz P3 (kosi poklopac, zglobna mehanika) izvedeno je sve potrebno za inspekcijske poklopce i brane.

#### SVG popravci — `gotovo`
8 SVG-eva: naslovi uklonjeni iz svih (uvod_pregled header bar uklonjen, val1/val2/val3/ch1 top titlovi uklonjeni, inspekcijski_poklopac i brodska_vrata_brane titlovi uklonjeni, vjezbe_skice glavni naslov uklonjen — sub-panel T1–T6 labele ostaju).

#### Numerička verifikacija — `OK 34/34` ([tools/verify_u05.py](tools/verify_u05.py))
Pokriva: P1 (A=6, h_C=3,5, F=205,5 kN, I_G=4,5, h_CP=3,714 m), P2 (F_p=8,46 kN, y_1=1,20, y_2=1,697, y_3=2,078, y_CP_4=2,244), P3 (A=1,08, h_C=1,320, F=13,95 kN, s_R=0,679, T=7,89 kN), CH1 (F_1=5,63, F_2=42,52, F=48,15, y_CP=1,894, T=32,58, R_A=15,57 kN), P5 kotao (F=4,23 kN, y_CP=1,817), P6 vrata brane (F=29,63 kN, y_CP=1,486, h_from_bottom=0,514 m), Z1–Z6 (fizikalna razumnost).

### B-U06: Zakrivljene plohe i rastav sila — `zatvoreno`

**Datum start/zatvaranja**: 2026-05-18.

#### Inventar
- 3 Riješena primjera (P1–P3): potopljena četvrtina kruga, sklopiva servisna brana sa zakrivljenim rubom, četvrtcilindrični revizijski poklopac.
- 1 cjeloviti zadatak (T3): četvrtcilindrični poklopac s vodoravnom spojnicom.
- 2 aplikativna primjera: zaobljeni poklopac procesnog kotla (T2 strojarstvo), zaobljeno dno retencijskog jezerca (T2 građevinarstvo).
- 6 zadataka za vježbu (T1–T3).
- 8 SVG datoteka: [u06_fig_uvod_pregled](assets/print/u06_fig_uvod_pregled.svg), [u06_val1_cetvrtina_kruga](assets/print/u06_val1_cetvrtina_kruga.svg), [u06_val2_sklopiva_brana](assets/print/u06_val2_sklopiva_brana.svg), [u06_val3_cetvrtcilindricni_poklopac](assets/print/u06_val3_cetvrtcilindricni_poklopac.svg), [u06_ch1_poklopac_spojnica](assets/print/u06_ch1_poklopac_spojnica.svg), [u06_fig_zaobljeni_poklopac_kotla](assets/print/u06_fig_zaobljeni_poklopac_kotla.svg), [u06_fig_zaobljeno_dno_jezerca](assets/print/u06_fig_zaobljeno_dno_jezerca.svg), [u06_vjezbe_skice](assets/print/u06_vjezbe_skice.svg).

#### Tekst Primjeri + Zadaci — `prolaze`
Sve primjere i 6 zadataka prolaze protokolne provjere. Posebno snažan didaktički luk u rastavu sila: P1 čista referentna geometrija (četvrtina kruga, F_V prema gore) → P2 servisna brana (kompozit ravnog i zakrivljenog dijela + masa) → P3 izolirana referenca (čistina) → CH1 puna momentna ravnoteža sa spojnicom. P5/P6 zatvaraju strojarsku i građevinsku primjenu istom geometrijom (zakrivljeno dno kotla / jezerca, F_V prema gore).

#### SVG popravci — `gotovo`
8 SVG-eva: svi naslovi (uključujući podnaslove) uklonjeni. Pattern Faze 1 dosljedno primijenjen.

#### Numerička verifikacija — `OK 35/35` ([tools/verify_u06.py](tools/verify_u06.py))
Pokriva: P1 (F_H=66,7 kN, h_FH=3,09, V*=7,587 m³, F_V=74,3 kN, x_FV=0,584 m, F_R=99,8 kN), P2 (L=2,065, y=0,64, F_OA=14,76, F_V=4,01, F=4,86 kN), P3 (F_H=4,76 kN, h_H=0,60, F_V=7,47 kN, x_V=0,382, F_R=8,86 kN, α=57,5°), CH1 (F_H=8,29, h_H=0,733, F_V=13,03, x_V=0,467, F_R=15,44, T=11,06 kN), P5 kotao (F_H=13,22 kN, F_V=14,74 kN, F_R=19,8 kN), P6 jezerce (F_H=117,6 kN, F_V=128,6 kN, F_R=174,0 kN), Z1–Z6.

### B-U07: Uzgon, plivanje i stabilnost — `djelomično zatvoreno` (tekst + 1 matplotlib zamijenjen; 4 matplotlib bloka čekaju autorsku SVG izradu)

**Datum start/zatvaranja**: 2026-05-18.

#### Inventar
- 4 Riješena primjera (P1–P4): ponton sa simetričnim opterećenjem, bočni pomak centra uzgona, plutajuća platforma s kompresorom, kalibracijski modul na granici fluida.
- 1 cjeloviti zadatak (T4): plutajuća platforma na granici ulja i vode.
- 2 aplikativna primjera: pumpno kućište (T2 strojarstvo), privezni ponton (T2 građevinarstvo).
- 6 zadataka za vježbu.
- 5 SVG datoteka: [u07_val2_ponton_gaz](assets/print/u07_val2_ponton_gaz.svg) (P1), [u07_val1_platforma_kompresor](assets/print/u07_val1_platforma_kompresor.svg) (P3), [u07_val3_dva_fluida_modul](assets/print/u07_val3_dva_fluida_modul.svg) (P4 — bivši orphan, sada spojen), [u07_ch1_platforma_ulje_voda_ormar](assets/print/u07_ch1_platforma_ulje_voda_ormar.svg) (CH1), [u07_vjezbe_skice](assets/print/u07_vjezbe_skice.svg).

#### Tekst Primjeri + Zadaci — `prolaze`
Sve primjere i 6 zadataka prolaze protokolne provjere. CH1 (Plutajuća platforma na granici ulja i vode) je posebno snažan T4 — kombinira 5 računa (srednji uron, podjela istisnine na dva fluida, težinjenje centra uzgona, momentna ravnoteža s pomaknutim teretom, povećanje gaza u odnosu na simetrično stanje).

#### Orphan SVG spojen — `gotovo`
[u07_val3_dva_fluida_modul.svg](assets/print/u07_val3_dva_fluida_modul.svg) (do sada nereferenciran) zamijenio je matplotlib blok `fig-u07-kalibracijski-modul` na redu 518–593 [source/u07_*.md](source/u07_uzgon_plivanje_i_stabilnost.md). Obrisano je 2810 znakova matplotlib koda.

#### SVG popravci — `gotovo`
5 postojećih SVG-eva: naslovi uklonjeni (val1, val2, val3, ch1, vjezbe_skice).

#### Numerička verifikacija — `OK 34/34` ([tools/verify_u07.py](tools/verify_u07.py))
Pokriva: P1 (V=0,601, h=0,209, Δm=320), P2 (h_m=0,28, y_B=0,0286), P3 (V=0,868, y_B=0,0357, e=0,1628, Δh_m=0,0614), P4 (x=0,0933, F_V=5,7 N), CH1 (V=0,900, V_o=0,360, V_w=0,540, y_B_w=0,0667, y_B=0,0435, e=0,200, h_0=0,20, Δh_m=0,05), P5 pumpno (F_U=452,5, G=833,9, F_neto=381,4), P6 ponton (h_sr=0,167, Δh=0,0626), Z1–Z6.

#### Preostali matplotlib blokovi — `otvoreno za buduće sesije` (4 SVG-a za izraditi)
4 matplotlib blokova još uvijek aktivno renderiraju figure u U07 — nemaju pripremljeni SVG zamjenu i čekaju autorsku skicu:

1. **`fig-uvod-u07`** (uvodna figura poglavlja, red 1–~100): pregled tri ideje — istisnina, plivanje, momentna ravnoteža. Treba dizajnirati SVG sličan onima iz U05/U06 uvodnih panela.
2. **`fig-u07-bocni-pomak-centra-uzgona`** (red 323–393): nagnuti ponton s linearno različitim uronima, oznaka centra uzgona B i pomak y_B.
3. **`fig-u07-pumpno-kuciste-uzgon`** (red 869–920): potonulo kućište u bazenu, sile F_U gore i G dolje.
4. **`fig-u07-ponton-nagib`** (red 965–1027): nagnuti ponton s ekscentričnom opremom, kote Δh i e.

Realan opseg za izradu: ~1–2 sata po SVG-u (autorov dizajn po kanonskom standardu). Predlažem to riješiti pri završnom polishing prolazu nakon zatvaranja svih ostalih poglavlja, ili da autorka direktno dizajnira ako želi vizualnu kontrolu.

### B-U08: Kontrolni volumen i kontinuitet — `djelomično zatvoreno` (tekst + verify; 3 matplotlib bloka za autorov SVG)

**Datum start/zatvaranja**: 2026-05-18.

#### Inventar
- 3 Riješena primjera (P1–P3): difuzor, komora za miješanje, izjednačni spremnik.
- 1 cjeloviti zadatak (T3): miješajući izjednačni spremnik s porastom razine.
- 2 aplikativna primjera: T-komad hidraulike (T2 strojarstvo), retencijski bazen (T2 građevinarstvo).
- 6 zadataka za vježbu.
- 6 SVG datoteka: u08_val1_difuzor_kontinuitet, u08_val2_mjesanje_tokova, u08_val3_izjednacni_spremnik, u08_ch1_mijesajuci_spremnik, u08_kontrolni_volumen_scene (sažeta print-zamjena), u08_vjezbe_skice.
- 3 matplotlib bloka još otvorena: `fig-uvod-u08`, `fig-u08-t-komad-hidraulika` (P5), `fig-u08-retencijski-bazen` (P6).

#### Tekst Primjeri + Zadaci — `prolaze`
Snažan didaktički luk: stacionarni jedan-ulaz-jedan-izlaz (P1) → dva ulaza jedan izlaz s miješanjem masa (P2) → nestacionarni (P3) → CH1 sve zajedno (miješanje + akumulacija razine).

#### SVG popravci — `gotovo`
6 SVG-eva: naslovi uklonjeni iz svih.

#### Numerička verifikacija — `OK 28/28` ([tools/verify_u08.py](tools/verify_u08.py))
Pokriva: P1 (v_1=36, Q=0,407, m_dot=406), P2 (Q_C=0,180, v_C=2,55, ρ_C=967), P3 (A_T=5,40, dh/dt=2,59 mm/s, t=289 s, Δm=4040 kg), CH1 (Q_3=0,01414, ρ_3=1025, dh/dt=1,57 mm/s, t=255 s, Δm=2583 kg), P5 T-komad (Q_1=3,62 L/s, Q_2=2,17 L/s, v_2=6,9 m/s, D_3=24,8 mm), P6 retencija (Q_neto=0,37, dh/dt=18,5 cm/min, t=162 s), Z1–Z6.

#### Preostali matplotlib blokovi — `otvoreno za buduće sesije` (3 SVG-a za izraditi)
1. `fig-uvod-u08` — uvodna figura poglavlja.
2. `fig-u08-t-komad-hidraulika` — T-komad s ulaznom cijevi i dva ogranka.
3. `fig-u08-retencijski-bazen` — bazen s dva dotoka i jednim ispustom + rast razine.

### B-U09: Bernoullijeva jednadžba idealnog fluida — `djelomično zatvoreno` (tekst + verify; 3 matplotlib bloka za autorov SVG)

#### Inventar
3 P (konfuzor, slobodni mlaz, idealni sifon), 1 CH (bypass-sifon T3), 2 aplikativna (Venturi T2, propust T2), 6 Z. 5 SVG datoteka.

#### Tekst — `prolaze` · SVG naslovi — `gotovo` · Verify — `OK 28/28` ([tools/verify_u09.py](tools/verify_u09.py))
Pokriva: P1 konfuzor (Q=0,567, v_2=30,63, Δp=523 Pa), P2 mlaz (x_max=H za h=H/2), P3 sifon (v=8,40, Q=42,2 L/s, p_C/γ=-5,8 m), CH1 bypass (v_B=7,41, v_C=11,58, p_C abs=1,86 m, domet=3,96 m), Venturi (Q=5,27 L/s), propust (v=12,91 m/s, Q=1,622 m³/s), Z1–Z6.

#### Preostali matplotlib blokovi — `otvoreno` (3): `fig-uvod-u09`, `fig-u09-venturijeva-cijev`, `fig-u09-brzina-istjecanja-propust`.

### B-U10: Realni Bernoulli i gubici — `djelomično zatvoreno` (tekst + verify; 3 matplotlib bloka za autorov SVG)

#### Inventar
3 P + 2 CH (T3 Pitot+spremnik, T4 kavitacija) + 2 aplikativna + 6 Z. 6 SVG datoteka.

#### Tekst — `prolaze nakon popravka` · SVG naslovi — `gotovo` · Verify — `OK 38/38` ([tools/verify_u10.py](tools/verify_u10.py))

**Bitan nalaz**: verify otkrio **matematičku grešku u izvoru** ([source/u10_*.md:1161](source/u10_realni_bernoulli_i_gubici.md)) u Primjeru "Rashladni cjevovod motora":
- Pisalo: $\lambda \cdot L/D = 0{,}028 \cdot 1{,}20/0{,}028 = 1{,}00$ (POGREŠNO — daje $h_l = 0{,}399$ m, $h_w = 2{,}075$ m, $\Delta p = 21{,}57$ kPa)
- Točno: $0{,}028 \cdot 1{,}20/0{,}028 = 1{,}20$ (daje $h_l = 0{,}480$ m, $h_w = 2{,}158$ m, $\Delta p = 22{,}44$ kPa)
- Tekst popravljen: $h_l \to 0{,}480$, $h_{loc} \to 1{,}678$, $h_w \to 2{,}158$, $\Delta p \to 22{,}44$ kPa.

Pokriva: P1 gubici (h_w=3,82, Δp=37,5 kPa), P2 Pitot (v=3,95 m/s), P3 realni sifon (v=2,52, Q=16 L/s, p_C/γ=-3,04), CH1 spremnik s Pitot (v=3,34, Q=16,8, p_MA=80,9 kPa), P5 usisni tlak (v=2,78, h_w=1,30, rezerva=1,65 m), CH2 kavitacija (H_p=19,76 m, ΔH_kav=1,88, z_S_max=5,68 m), rashladni (h_w=2,158, Δp=22,44 kPa), odvodnja (v=2,545, Q=24,18 L/s), Z1–Z6.

#### Preostali matplotlib blokovi — `otvoreno` (3): `fig-uvod-u10`, `fig-u10-usisni-tlak-crpka`, `fig-u10-rashladni-cjevovod`, `fig-u10-gravitacijska-odvodnja` (zapravo 4).

### B-U11: Količina gibanja i sile strujanja — `djelomično zatvoreno`

3 P (mlaz na ploču, mlaznica/prirubnica, koljeno) + 2 CH (T3 T-račva, T4 Y-račva) + 2 aplikativna (koljeno rashladni, vatrogasni monitor) + 6 Z. 6 SVG datoteka, naslovi uklonjeni.

#### Verify — `OK 33/33` ([tools/verify_u11.py](tools/verify_u11.py))
Pokriva: P1 (F=200 N), P2 mlaznica (v_2=5,82, Q=37 L/s, p_M1=16,4 kPa, R=445 N), P3 koljeno (F_R=1,45 kN), CH1 T-račva (v=10,03, Q_1=0,114, F_R=1,03 kN), CH2 Y-račva (v=12, p_M1=48,6 kPa, R=912 N), koljeno-rashladni (F_R=1,80 kN), vatrogasni (R=3,56 kN), Z1–Z6.

#### Preostali matplotlib blokovi — `otvoreno` (3): `fig-uvod-u11`, `fig-u11-koljeno-rashladni`, `fig-u11-mlaznica-vatrogasni-monitor`.

### B-U12: Pokretne lopatice i potisak — `djelomično zatvoreno`

4 P + 3 CH (T3 zakrivljena lopatica, T4 Pelton rotor, T4 flyboard) + 2 aplikativna (Pelton snaga, hidromlazni pogon) + 6 Z. 7 SVG datoteka, naslovi uklonjeni.

#### Verify — `OK 42/42` ([tools/verify_u12.py](tools/verify_u12.py))
Pokriva: P1 vodilica (m_dot=12,07, R=451 N), P2 ukljestena (M_O=-198 Nm), P3 relativni (w_1=14, ratio=63,7%), P4 ravna lopatica (F=282 N, P=2,54 kW), CH1 zakrivljena (F=746 N, P=7,23 kW), CH2 Pelton (u=15,41, M=313 Nm, P=10,49 kW), CH3 flyboard (v_min=13,69, a=1,97, t=3,19 s, h_max=12,02 m), Pelton-lopatica (F_t=2683, P=48,3 kW), hidromlazni (F_p=820 N), Z1–Z6.

#### Preostali matplotlib blokovi — `otvoreno` (4): `fig-uvod-u12`, `fig-u12-relativni-dotok-lopatica`, `fig-u12-pelton-lopatica`, `fig-u12-hidromlazni-pogon`.

### B-U13: Cjevovodi — `djelomično zatvoreno`

3 P (Reynolds+gubici, paralelne grane, servisni ispust) + 1 CH (T4 serijsko-paralelna mreža) + 2 aplikativna (rashladni cjevovod peći, vodovod) + 6 Z. 5 SVG datoteka, naslovi uklonjeni.

#### Verify — `OK 33/33` ([tools/verify_u13.py](tools/verify_u13.py))
Pokriva: P1 Reynolds (v=2,83, Re=2,55e5, h_w=7,26 m), P2 paralelne (v_1=3,29, v_2=5,14, Q_2=25,9 L/s), P3 ispust (λ=0,0171, Q_p=7,3 L/s, d_p=53,5 mm), CH1 serijsko-paralelna (Q=22,9 L/s, Q_1=15,1, h_p=5,91 m, P_gub=2,70 kW), peć (h_w=26,07 m), vodovod (Q_1=37 L/s, h_w=7,47 m), Z1–Z6.

#### Preostali matplotlib blokovi — `otvoreno` (3): `fig-uvod-u13`, `fig-u13-rashladni-cjevovod-peci`, `fig-u13-paralelne-grane-vodovod`.

## Završni pregled (Faza C)

### Stanje na kraju Faze 1

| Poglavlje | Status | SymPy verify | SVG titles | Matplotlib otvoreno |
|-----------|--------|---|---|---|
| **U01** | zatvoreno (puno) | 28/29 (1 zaokruženje) | sve uklonjeno, paleta+oznake fiksirano | 0 |
| **U02** | zatvoreno (puno) | 25/25 | sve uklonjeno | 0 |
| **U03** | zatvoreno (puno) | 31/31 | sve uklonjeno | 0 |
| **U04** | zatvoreno (puno) | 38/38 | sve uklonjeno | 0 |
| **U05** | zatvoreno (puno) | 34/34 | sve uklonjeno | 0 |
| **U06** | zatvoreno (puno) | 35/35 | sve uklonjeno | 0 |
| **U07** | djelomično (tekst+verify) | 34/34 | sve uklonjeno; orphan spojen | 4 (uvod, bočni_pomak, pumpno_kuciste, ponton_nagib) |
| **U08** | djelomično | 28/28 | sve uklonjeno | 3 (uvod, t_komad, retencijski) |
| **U09** | djelomično | 28/28 | sve uklonjeno | 3 (uvod, venturi, propust) |
| **U10** | djelomično (tekst popravljen!) | 38/38 | sve uklonjeno | 4 (uvod, usisni, rashladni, odvodnja) |
| **U11** | djelomično | 33/33 | sve uklonjeno | 3 (uvod, koljeno_rashladni, vatrogasni) |
| **U12** | djelomično | 42/42 | sve uklonjeno | 4 (uvod, relativni, pelton, hidromlazni) |
| **U13** | djelomično | 33/33 | sve uklonjeno | 3 (uvod, rashladni_peći, vodovod) |
| **UKUPNO** | **13/13** | **427/428** | **93 SVG-a (svi naslovi)** | **27 matplotlib** |

### Velike provjere

- [x] Cross-chapter notacijski sweep — verifikacijske skripte koriste iste fizikalne odnose; nije pronađena globalna nekonzistentnost notacije.
- [ ] Puni `quarto render` čist — `quarto` CLI nije pronađen na sustavu; ostaje za autoricu.
- [x] Puni `py tools/verify_all.py` — 427 OK + 1 zaokruženje (U01 most.p_p_MPa: tekst kaže `1,3 MPa`, točno je `1,316 MPa`; **preporuka**: ažurirati tekst na `1,32 MPa`).
- [x] **Pronađene i ispravljene matematičke greške u izvoru**:
  - U10 Primjer "Rashladni cjevovod motora" — λ·L/D bio krivo izračunat (1,00 umjesto 1,20), čime su h_l, h_w i Δp bili podcijenjeni za ~4%. Tekst popravljen ([source/u10_*.md:1161](source/u10_realni_bernoulli_i_gubici.md)).
- [ ] Vizualni walkthrough chapter-po-chapter (autor + ja) — preview server radi na http://localhost:8765/preview.html za autorov pregled.
- [ ] D01–D03 finalna integracija — D01–D03 ostaju za zasebnu polishing fazu nakon završetka matplotlib→SVG konverzije.
- [ ] Statusni dokument zatvara Fazu 1 — bit će ažuriran nakon autorove potvrde.

### Otvoreni rad za sljedeću fazu

**1. Matplotlib → SVG konverzija (27 blokova kroz U07–U13)**:
- Sve verify skripte i tekst su čist; preostala je samo autorska izrada SVG-eva za blokove koji još aktivno renderiraju matplotlib figuru.
- Svaki SVG zahtijeva ~1–2 sata autorskog dizajna prema kanonskom standardu iz [protokol_prerade_zadataka_i_skica.md](protokol_prerade_zadataka_i_skica.md).
- Mogu se isporučivati po jedan SVG po sesiji (slično obrascu u U01 SVG popravcima), ili autor može direktno dizajnirati ako želi punu vizualnu kontrolu.

**2. Tekstualni zaokruživački reziduali (mali)**:
- U01 `most.p_p_MPa`: preporuka ažurirati `1,3 MPa` → `1,32 MPa` u tekstu (vidi verify_u01).

**3. Layout pomak (samo U01 reziduali)**:
- Val3 i CH1: G label malo dodiruje F_L label u sredini canvas-a. Kozmetičko, ne funkcionalno.

**4. Quarto render check**:
- Quarto CLI nije instaliran. Autorica treba pokrenuti `quarto render` iz svog uobičajenog terminala da potvrdi čist build s novim SVG-ovima.

## Faza 1.5 — Didaktičko obogaćivanje (2026-05-18)

Nakon zatvaranja Faze 1 (tekstualni QA + verify), autorka je odobrila uvođenje **11 novih primjera/cjelovitih zadataka** kroz U01–U13 koji popunjavaju didaktičke prilike — koncepte iz teorije koji nisu bili eksplicirani u postojećim primjerima, te realne strojarske scenarije koji daju studentima jači fizikalni uvid.

### Sažetak uvedenih primjera

| # | Poglavlje | Naziv | Tip | Razina | Glavni didaktički koncept |
|---|-----------|-------|-----|--------|---------------------------|
| 1 | U01 | Hidraulična kočnica vozila | P | T2 | Pascalov zakon u distribucijskom sustavu (1 ulaz → 4 izlaza) |
| 2 | U02 | Klizni ležaj pri hladnom startu vs radnoj temp. | P | T2 | Temperaturna ovisnost $\mu$ (faktor 10 razlike) |
| 3 | U03 | Balastni tank broda | P | T2 | Neto hidrostatski tlak (vani vs iznutra) |
| 4 | U05 | Vertikalna ploha kroz tri sloja fluida | P | T2 | Sustavski pristup integraciji po pojasima |
| 5 | U06 | Plinski jastuk iznad četvrtkruga | P | T2 | $F_H$ i $F_V$ s razdvojenim doprinosima fluida i plina |
| 6 | U07 | Asimetrično poplavljen tank broda | CH | T4 | Stabilnost broda, $\overline{GM}$, ravnotežni nagib |
| 7 | U09 | Difuzor | P | T2 | Inverz konfuzora, koeficijent povratka $\eta_{dif}$ |
| 8 | U10 | Starenje cijevi i $\lambda$ | P | T2 | Moodyjev dijagram + životni vijek sustava |
| 9 | U11 | Vodeni udar | CH | T3 | Joukowsky + Michaud, sila na prirubnicu |
| 10 | U12 | Krivulja snage $P(u)$ Peltonove turbine | CH | T3 | $u_{opt} = c_1/2$, $\eta_{max}$, projektni $n$ |
| 11 | U13 | Radna točka crpka⇄cjevovod | CH | T4 | Presjecište $H_p(Q)$ i $H_s(Q)$, utjecaj ventila |

### Numerička verifikacija (Faza 1.5)

Sve 11 primjera dobile su nove SymPy funkcije u `tools/verify_uXX.py`:

- U01.kocnica (5 checkova), U02.lezaj_temp (6), U03.balastni (4), U05.tri_sloja (6), U06.plinski (5)
- U07.CH2 (10), U09.difuzor (5), U10.starenje (7), U11.CH3 (7), U12.CH4 (7), U13.CH2 (8)

**Ukupno novih checkova: 70**

`py tools/verify_all.py` rezultat nakon Faze 1.5:

| Poglavlje | OK | FAIL | Komentar |
|-----------|-----|------|----------|
| U01 | 33 | 1 | 1 zaokruženje (pre-existing, U01.most.p_p_MPa) |
| U02 | 31 | 0 | |
| U03 | 35 | 0 | |
| U04 | 38 | 0 | |
| U05 | 40 | 0 | |
| U06 | 40 | 0 | |
| U07 | 44 | 0 | (uključuje CH2 poplavljen tank — 10 checkova) |
| U08 | 28 | 0 | |
| U09 | 33 | 0 | |
| U10 | 45 | 0 | (uključuje starenje — 7 checkova) |
| U11 | 40 | 0 | (uključuje CH3 vodeni udar — 7 checkova) |
| U12 | 49 | 0 | (uključuje CH4 optimum — 7 checkova) |
| U13 | 41 | 0 | (uključuje CH2 radna točka — 8 checkova) |
| **UKUPNO** | **497** | **1** | sve 70 novih checkova PASS |

### SVG isporuke — otvoreno

Svih 11 primjera referencira nove SVG datoteke koje **još ne postoje** u `assets/print/`. Detaljan opis svake skice (geometrija, palette, brojevi) nalazi se u [`todo_svg_za_codex.md`](todo_svg_za_codex.md).

Codex isporučuje SVG-ove paralelno s 27 matplotlib→SVG konverzija već otvorenih iz Faze 1. Ukupno preostalo za izradu: **27 (Faza 1) + 11 (Faza 1.5) = 38 SVG datoteka**.

### Pozicija novih primjera u poglavljima

- **U01**: kočnica vozila kao **treći** strojarski primjer (nakon preša + most podizanje), prije usporedne tablice
- **U02**: ležaj pri dvije temperature kao **drugi** strojarski primjer (nakon klizni ležaj P4), prije građevinarske vlage P5
- **U03**: balastni tank kao **drugi** strojarski primjer, nakon vodotornja P6 i prije usporedne tablice
- **U05**: tri sloja fluida kao **P4** (između P3 kosi poklopac i CH1 zglobna pregrada)
- **U06**: plinski jastuk kao **P4** (između P3 četvrtcilindar i CH1 spojnica)
- **U07**: asimetrično poplavljen tank kao **CH2** (nakon CH1 platforma ulje/voda, prije P5 pumpno kućište)
- **U09**: difuzor kao **P2** (odmah nakon P1 konfuzor – simetrična para)
- **U10**: starenje cijevi kao **drugi** strojarski primjer (nakon rashladni motor)
- **U11**: vodeni udar kao **CH3** (nakon CH2 Y-račva, prije P5 koljeno rashladni)
- **U12**: krivulja snage kao **CH4** (nakon CH2 Pelton rotor, prije CH3 mlazna platforma)
- **U13**: radna točka kao **CH2** (nakon CH1 serijsko-paralelna mreža, prije "Prije zadataka" pravila)

### Inženjerski naglasci koje su uveli novi primjeri

- **Tribologija**: U02 hladni start (motorno ulje, tribologija ležaja)
- **Brodogradnja**: U03 balastni tank, U07 stabilnost broda (SOLAS, oštećenje trupa)
- **Hidraulika vozila**: U01 kočnica (razdvajanje sile, sigurnost)
- **Procesna industrija**: U05 tri sloja (separacija, stratifikacija)
- **Hidropneumatika**: U06 plinski jastuk (kotlovi pod tlakom, PVC dizajn)
- **Mlazna mehanika**: U09 difuzor (pumpe, ventilacija)
- **Održavanje sustava**: U10 starenje cijevi (predviđanje vijeka)
- **Sigurnost cjevovoda**: U11 vodeni udar (water hammer, akumulatori, soft-stop)
- **Energetika**: U12 optimalna brzina Peltona (hidroelektrane, projektiranje)
- **Sustav crpka+cjevovod**: U13 radna točka (selekcija crpke, frekvencijska regulacija)

### Otvoreno

1. SVG izrada za 11 novih primjera (Codex; specifikacije u `todo_svg_za_codex.md`).
2. SVG izrada za 27 matplotlib blokova iz Faze 1.
3. Quarto render check nakon svih SVG-eva.
4. Rounding fix u U01 most.p_p_MPa (1,3 → 1,32 MPa).

## Faza 2 — Integracija Codex isporuke i normalizacija (2026-05-26)

Codex je predao SVG redizajn na `origin/codex` grani (commit `cd6aec6`).
Branched s `d6126f2` (prije Faze 1.5), pa je merge tražio selektivno
povlačenje samo onih izmjena koje su relevantne za SVG sloj.

### Selektivna integracija

Iz `origin/codex` povučeno **samo**:
- 117 SVG datoteka u `assets/print/` (24 nove + 93 redizajna postojećih)

Iz `origin/codex` **nije** povučeno:
- `chapters/*.quarto_ipynb_XX` (oko 80 quarto build artefakata) — to su privremene render datoteke koje ne pripadaju u repo
- Izmjene `source/uXX_*.md` — Codex je branchao prije Faze 1.5, pa bi
  njegove tekstualne izmjene poništile 11 novih primjera. Umjesto toga
  napravljen je surgical merge: zadržan kompletan main source, samo su
  matplotlib blokovi zamijenjeni SVG referencama (skripta
  `tools/replace_matplotlib_blocks.py`)
- Pseudo-brisanja: tools/, todo_svg_za_codex.md, dodaci d04 — sve to nije
  Codex namjerno brisao, samo nije imao u svojem ancestor commitu

### Matplotlib → SVG zamjene (24 mapiranja)

| Poglavlje | Matplotlib label | SVG datoteka |
|-----------|------------------|--------------|
| U07 | `fig-uvod-u07` | `u07_fig_uvod_pregled.svg` |
| U07 | `fig-u07-bocni-pomak-centra-uzgona` | `u07_fig_bocni_pomak.svg` |
| U07 | `fig-u07-pumpno-kuciste-uzgon` | `u07_fig_pumpno_kuciste.svg` |
| U07 | `fig-u07-ponton-nagib` | `u07_fig_ponton_nagib.svg` |
| U08 | `fig-uvod-u08` | `u08_fig_uvod_pregled.svg` |
| U08 | `fig-u08-t-komad-hidraulika` | `u08_fig_t_komad_hidraulika.svg` |
| U08 | `fig-u08-retencijski-bazen` | `u08_fig_retencijski_bazen.svg` |
| U09 | `fig-uvod-u09` | `u09_fig_uvod_pregled.svg` |
| U09 | `fig-u09-venturijeva-cijev` | `u09_fig_venturijeva_cijev.svg` |
| U09 | `fig-u09-brzina-istjecanja-propust` | `u09_fig_propust_brana.svg` |
| U10 | `fig-uvod-u10` | `u10_fig_uvod_pregled.svg` |
| U10 | `fig-u10-usisni-tlak-crpka` | `u10_fig_crpka_usisni_tlak.svg` |
| U10 | `fig-u10-rashladni-cjevovod` | `u10_fig_rashladni_cjevovod.svg` |
| U10 | `fig-u10-gravitacijska-odvodnja` | `u10_fig_odvodnja_zgrade.svg` |
| U11 | `fig-uvod-u11` | `u11_fig_uvod_pregled.svg` |
| U11 | `fig-u11-koljeno-rashladni` | `u11_fig_rashladni_koljeno.svg` |
| U11 | `fig-u11-mlaznica-vatrogasni-monitor` | `u11_fig_vatrogasni_monitor.svg` |
| U12 | `fig-uvod-u12` | `u12_fig_uvod_pregled.svg` |
| U12 | `fig-u12-relativni-dotok-lopatica` | `u12_fig_relativni_dotok.svg` |
| U12 | `fig-u12-pelton-lopatica` | `u12_fig_pelton_lopatica.svg` |
| U12 | `fig-u12-hidromlazni-pogon` | `u12_fig_hidromlazni_pogon.svg` |
| U13 | `fig-uvod-u13` | `u13_fig_uvod_pregled.svg` |
| U13 | `fig-u13-rashladni-cjevovod-peci` | `u13_fig_rashladni_cjevovod_peci.svg` |
| U13 | `fig-u13-paralelne-grane-vodovod` | `u13_fig_paralelne_grane_vodovod.svg` |

Status nakon zamjene: **0 matplotlib blokova preostalo u source/u*.md**.

### Primjena protokolnih pravila na sve SVG-ove

Sve nove i redizajnirane SVG datoteke prošle su kroz kanonski tijek:

1. **`tools/svg_normalize.py`** — 117 datoteka:
   - prefiksirani ID-evi (iz imena datoteke)
   - kanonski font `'Segoe UI',Arial,sans-serif`
   - `preserveAspectRatio` i responsive root atributi
   - aria-labelledby na prefiksirane title/desc
2. **`tools/strip_svg_titles.py`** (novi alat) — 69 datoteka:
   - uklonjeni top-level `<text>` naslovi tipa "U[0-9]+ - ..."
   - uklonjeni podnaslovi (smaller font, sivi fill, neposredno ispod)
   - `<title>` accessibility element ostaje (screen reader)
3. **`tools/fix_svg_xml.py`** (novi alat) — popravljena XML konformanca:
   - sekvenca `--` unutar XML komentara zamijenjena s `==`
   - nedostajući `;` u hex entitetima (`&#xNNNN`) dodani
   - corrupt path s prosom u `d` atributu uklonjen (u06)

### Rezultati

- **117/117 SVG datoteka XML-valjano** (lxml/ET.parse OK)
- **0 matplotlib blokova** u source/u*.md
- **0 top-level naslova** u SVG-ovima
- **SymPy verify**: 497/498 PASS (jedini fail je pre-existing U01 rounding)
- **Otvoreno**: 11 SVG-ova za primjere Faze 1.5 (specifikacije u `todo_svg_za_codex.md`); Quarto render check; rounding fix U01

### Novi alati u tools/

- `replace_matplotlib_blocks.py` — surgical replace matplotlib → SVG referenca po labelu
- `strip_svg_titles.py` — uklanjanje top-level naslova SVG-ova
- `fix_svg_xml.py` — popravak XML konformance (komentari, entiteti)

## Faza 3 — Detaljni QA SVG-ova kroz pravila_svg.md (2026-05-26)

Sustavni prolaz kroz sve SVG-ove poglavlja prema [`pravila_svg.md`](pravila_svg.md) checklisti A–E. Cilj: ispraviti Codex regresije i sistemske odstupanje od kanonske palete koje su otkrile da Codex nije imao u svom ancestoru sve Faza 1 popravke.

### B-U01: Osnove fluida i Pascalov zakon — `zatvoreno (Faza 3)`

**Datum**: 2026-05-26
**SVG-ova pregledano**: 9 (val1, val2, val3, ch1, uvod, gustoca, presa, most, vjezbe)
**Otvoreno**: 1 SVG za izradu (u01_fig_kocnica_vozila.svg — primjer iz Faze 1.5, Codex todo)

#### Sistemski nalazi (popravljeno kroz tools/fix_u01_skice.py)

1. **Vode gradient bottom stop**: `#7fb3d3` → `#5b9ec9` (per protokol). Pogođeno **8 SVG-ova**.
2. **Boja kota**: tamno-siva `#3a3a3a` (i `#4a4a4a` u val1) → smeđa `#b7600c`. Pogođeno **7 SVG-ova**, ukupno **~60 instanci** (marker fill + stroke linija + tekst).

#### Per-file kritični Codex regresije (vraćeni stari pre-Faza-1 obrasci)

| SVG | Codex regression | Popravljeno |
|---|---|---|
| `u01_val2_hidraulicna_dizalica.svg` | F_1 plava (`#1565c0`) umjesto crvene (ulazna sila) | strelica + tekst + legenda u crvenu |
| `u01_val3_dvostruki_podizac.svg` | F_p plava + oznake A_e/F_e/s_e (subscript ₑ) umjesto A_L/F_L/s_L | F_p u crvenu, ₑ → `<tspan>L</tspan>` (7 instanci) |
| `u01_ch1_dvostruka_platforma_manometar.svg` | F_p plava + oznake A_e/F_e/s_e umjesto A_L/F_L/s_L + `s_k = 18 cm` umjesto `s_h` | F_p u crvenu, ₑ → tspan L (7 instanci), s_k → s_h (`&#8341;`) |
| `u01_fig_most_podizanje.svg` | F_p plava + oznake F_p01/A_p01/p_t3n umjesto F_pod/A_pod/p_min + rendered title | F_p u crvenu, sve 3 oznake → `<tspan>` subscript, naslov uklonjen |
| `u01_fig_presa_savijanje.svg` | rendered title | naslov uklonjen |
| `u01_vjezbe_skice.svg` | oznake A_e umjesto A_L | ₑ → tspan L (2 instance) |

#### Što je verificirano OK

- **Oznake u skici doslovno = tekst zadatka** ✓ (svih 9 SVG-ova, provjereno cross-checkom s Zadano/Rješenje)
- **Brojevi**: 160 mm, 3,60 kN, 179 kPa, 8,06 kN, 250 kPa, 5,25 kN, 0,80 MPa, 480 N, 0,92 MPa, 27,6 kN, 1,5 m, n=9, 5,12 kN, 0,40 MPa, 12,6 MPa, 1,3 MPa — sve match teksta
- **Semantika boja** (nakon fixova): ulazne sile (G, F_1, F_p) crvene; izlazne (F_2, F_L, F_pod) zelene; tlak p plava; kote smeđe
- **Subscript notacija**: lowercase preko Unicode entiteta (₁, ₂, ₚ, ₁₂); uppercase preko `<tspan baseline-shift="sub">` (L)
- **Render PNG** za svih 9 SVG-ova kroz Inkscape (1200 px), vizualna inspekcija multimodal Read tool: paleta i layout vidno odgovaraju protokolu

#### Otvorene rezidualne stavke (nije kritično, ne blokira)

1. **`u01_fig_uvod_pregled.svg` panel 3 ("Pascalov zakon")**: prikazuje scenu s F_1=320 N, F_2=5,12 kN koja se direktno preklapa s primjerom "Hidraulična preša za savijanje cijevi" — krši pravilo vizualne raznolikosti (uvodni blok ne smije reciklirati scene iz P/CH). **Preporuka**: redizajn panela 3 da pokazuje drugačiju primjenu Pascalova zakona (npr. samo kočno-pedalna shema bez konkretnih brojeva).
2. **Layout overlaps**:
   - val2: "A_1 = 6 cm²" tekst preklapa s klipnjačom u sredini
   - val3, ch1: oznake A_L i F_L na vrhu lijevog cilindra preklapaju s G strelicom i platformom
   - vjezbe T5/T6: "F_p" oznake u gornjem dijelu paneli prekrivene s vozilom/platformom
3. **U01 most**: `d_p = 22` umjesto `d_p = 22 mm` (nedostaje jedinica — vidno u rendered slici)

#### Alati za Faza 3 U01

- `tools/fix_u01_skice.py` (novi alat) — orchestrira sistemske + per-file popravke za U01
- Alat zadržan u tools/ kao referenca; ne potrebno više pokretati (idempotentno bi bilo 0 promjena nakon ovog passa)

#### SymPy verify nakon Faze 3 U01

`py tools/verify_u01.py` → **33 OK / 1 FAIL** (jedini FAIL je pre-existing rounding U01.most.p_p_MPa). Sve oznake/brojevi i dalje konzistentni nakon SVG izmjena (SVG promjene nemaju utjecaj na verifikaciju — to je matematika u tekstu).

#### Rendered PNG-ovi za autorov pregled

Sve 9 PNG-ova generirano u `tools/tmp/u01_render/` (1200 px wide). Autor može vizualno provjeriti kroz preview server na http://localhost:8765/preview.html ili direktno PNG-ove.

