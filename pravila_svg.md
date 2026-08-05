# Pravila za provjeru i izmjenu SVG skica — operativni cheat-sheet

> Konsolidirani sažetak pravila iz [`protokol_prerade_zadataka_i_skica.md`](protokol_prerade_zadataka_i_skica.md), [`kucni_stil_skica_val1.md`](docs/radno/kucni_stil_skica_val1.md) i operativnih odluka u [`qa_log_faza1.md`](docs/radno/qa_log_faza1.md). Ovaj dokument je radna referenca; izvori ostaju autoritativni.

> **Ažurirano 2026-05-26 (Faza 3 redizajn)** s naucima iz iterativnog redizajna val1: geometrijska koherentnost fluida, format sila, struktura formula panela. Vidi sekcije 12–14 na dnu.

---

## 1. Što SVG skica MORA imati

### Tehnička osnova
- [ ] Root: `<svg xmlns="..." viewBox="0 0 W H" role="img" aria-labelledby="PFX-title PFX-desc" preserveAspectRatio="xMidYMid meet" style="display:block;width:100%;max-width:XXXpx;height:auto;">`
- [ ] **Prefiksirani ID-evi**: svaki `id="..."` počinje kratkim prefiksom iz imena datoteke (npr. `u01v1km` za `u01_val1_klip_manometar.svg`). Bez prefiksa → kolizija na HTML stranici.
- [ ] `<title>` i `<desc>` elementi za pristupačnost (screen reader).
- [ ] Font: **isključivo** `'Segoe UI',Arial,sans-serif`.
- [ ] Decimalni separator: **zarez** (`1,2 m`, ne `1.2 m`).

### Tipične `max-width` vrijednosti
| Tip prikaza | max-width |
|---|---|
| Uski (kvadrat) | 420–540 px |
| Standardna ilustracija | 640–720 px |
| Dvopanelni | 800–900 px |
| Tropanelni uvodni blok | 960–980 px |

---

## 2. Što SVG skica NE smije imati

1. **Vidljiv naslov u rendered-u** (tip `<text>U10 – ...</text>`). Caption u Markdownu pokriva ulogu naslova. `<title>` za screen reader **smije** ostati.
2. **Dekorativne detalje** koji ne ulaze u model (sjenčanje, ornamenti).
3. **Iste vizualne motive** koji se već pojavljuju u drugoj figuri istog poglavlja (pravilo vizualne raznolikosti).
4. **Oznake koje tekst zadatka ne koristi** — ako tekst piše $F_L$, skica ne smije imati $F_e$.
5. **Globalne (ne-prefiksirane)** `id` atribute.
6. **Decimalnu točku** u brojevima.
7. **Font izvan** `'Segoe UI', Arial, sans-serif`.
8. **Preklapanje teksta** s geometrijom ili vektorima (min. odmak 6 px).
9. **Kote bez tik-crta** na krajevima.
10. **Strelice sila bez `<marker>` elementa** (ne simulirati strelicu stroke-widthom).
11. **Matplotlib/Python kod u Quarto izvoru** — sve figure su statičke SVG datoteke.

---

## 3. Kanonska paleta (jedina dopuštena)

### Vektori i oznake — semantika boja

| Svrha | Boja hex | Boja ime |
|---|---|---|
| **Sila ulaz** (opterećenje, kočenje, ubrzanje) | `#c0392b` | crvena |
| **Sila izlaz** (rezultat, korisna) | `#1e8449` | zelena |
| **Tlak / dubina / površinski napon** | `#1565c0` | plava |
| **Kota / dimenzija** | `#b7600c` | smeđa |
| **Efektivno polje sila** ($g_\text{eff}$, rotacija) | `#8e44ad` | ljubičasta |
| **Kutna brzina ω / rotacija** | `#1e8449` | zelena |
| **Δh/2 razmaci** (paraboloid) | `#e67e22` | narančasta |

**Semantika boja je obavezujuća** — boja označava *fizikalnu funkciju* sile, ne dekoraciju. Ulazna sila s plavom strelicom je **semantička greška** (čita se kao tlak).

### Fluidi (gradient, vertikalan: `x1="0" y1="0" x2="0" y2="1"`)

| Fluid | Gornji → Donji stop |
|---|---|
| Voda / opći fluid | `#aed6f1` → `#5b9ec9` |
| Ulje / hidraulično ulje | `#fde68a` → `#c8a000` |
| Gorivo (dizel, benzin) | `#fde68a` → `#d4a017` |
| Živa | `#b0b8c0` → `#808890` |

### Stijenke i čvrsti elementi

| Svrha | Boja |
|---|---|
| Gornja stijenka / klip | `#909fa8` |
| Donja stijenka / klip | `#5d6d7e` |
| Tamni rub geometrije | `#3a4a56` |
| Srafura | `#7a8a96` |

### Result box

- Konačni numerički rezultat: `fill="#c0392b"` (crveno) ili `#1e8449` (zeleno), `font-weight="700"`
- Rubna boja kutije odgovara tematskoj boji odjeljka

---

## 4. Linijska hijerarhija

| Tip linije | Što označava |
|---|---|
| puna debela | kruta stijenka, granica tijela, lopatica, spremnik |
| puna srednja | slobodna površina, presjek, stvarna granica fluida |
| tanka puna | mjere, kote, pomoćne geometrijske veze |
| isprekidana | referentna razina, os simetrije, produženje smjera |
| strelica srednje debljine | sila, brzina, ubrzanje, reakcija |

Razlika linija mora biti čitljiva i u **grayscale print** modu — print-first pravilo.

### Specifične širine

- Strelica sile: `stroke-width="2.5–3.0"`
- Strelica kote: `stroke-width="1.4–1.6"`, boja `#b7600c`
- Slobodna površina: deblja puna linija u plavoj `#1565c0`
- Mirna razina (referenca): isprekidana `stroke-dasharray="9,6"`, siva `#7a8a96`
- Srafura: 45° dijagonala, **7×7 px** pattern

---

## 5. Standard kota (dimenzijskih linija)

```xml
<!-- Marker desni (smeđi) -->
<marker id="PFXDim" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto">
  <path d="M0,0 L0,8 L8,4 z" fill="#b7600c"/>
</marker>
<!-- Marker lijevi (auto-start-reverse) -->
<marker id="PFXDimL" markerWidth="8" markerHeight="8" refX="1" refY="4" orient="auto-start-reverse">
  <path d="M0,0 L0,8 L8,4 z" fill="#b7600c"/>
</marker>
```

- Tik-crte na oba kraja (`stroke-width="1.3"`).
- Tekst kote **uvijek izvan geometrije** (min. 8 px odmak).
- Kote za os X: ispod geometrije. Za os Y: lijevo ili desno.
- Numerička vrijednost (`1,2 m`) navodi se pored oznake.

---

## 6. Tipografija

| Svrha | font-size | Stil |
|---|---|---|
| Naslov panela | 18 | bold |
| Caption panela | 13–14 | bold |
| Oznaka varijable | 11–14 | italic |
| Jednadžba inline | 14–22 | italic |
| Opisni tekst / legenda | 10–11 | normalan |
| Kota broj | 10–12 | normalan ili italic |

Unicode za jednadžbe: `Δ α τ μ ν ρ σ ω ² ³ · ≈ ≤ ≥`.

### Subscript u SVG-u

- **Mala slova** (e, p, k...): Unicode subscript entiteti — `&#8337;` ₑ, `&#8346;` ₚ
- **Velika slova** (L, R...): `<tspan baseline-shift="sub" font-size="0.7em">L</tspan>`

---

## 7. Filozofija uvodnog figure-bloka `fig-uvod-uXX`

Tri konceptualno odvojena panela:

| Panel | Sadržaj |
|---|---|
| **Lijevo** (široki) | Fizikalni model — geometrija, sile, kote, oznake |
| **Srednji / gornji desni** | Ključne jednadžbe poglavlja (jedna po kutiji) |
| **Donji desni** | Primjena u strojarstvu — scena koja se **ne smije ponavljati** u P/CH |

Tamni header bar s naslovom poglavlja na vrhu.

**Pravilo vizualne raznolikosti** (kritično za uvodni blok):
> Uvodni blok smije prikazivati **isključivo scene kojih nema** u riješenim primjerima istog poglavlja.

---

## 8. Operativna QA checklista za reviziju postojećeg SVG-a

Kad otvoriš SVG za pregled, idi redom:

### A. Konzistentnost s tekstom zadatka (najkritičnije)
- [ ] Sve **oznake u skici doslovno se podudaraju** s tekstom Zadano/Rješenje (znak po znak).
- [ ] **Brojevi u skici** (npr. dimenzije, sile) podudaraju se s brojevima iz Zadano.
- [ ] Nema novih oznaka u skici koje tekst ne uvodi.

### B. Semantika boja
- [ ] Ulazne sile crvene (`#c0392b`).
- [ ] Izlazne / rezultantne sile zelene (`#1e8449`).
- [ ] Strelice tlaka u fluidu plave (`#1565c0`).
- [ ] Kote smeđe (`#b7600c`).
- [ ] Ulje žuto-zlatno, voda plavi gradient.

### C. Tehnička higijena
- [ ] Bez vidljivog `<text>` naslova tipa "U10 – ..." u rendered-u.
- [ ] ID-evi prefiksirani iz imena datoteke.
- [ ] Font `'Segoe UI',Arial,sans-serif`.
- [ ] Decimalni zarez.
- [ ] Strelice koriste `<marker>` (nije bare line).
- [ ] Tekst se ne preklapa s geometrijom.

### D. Print-čitljivost
- [ ] Skica je čitljiva u grayscale.
- [ ] Linijska hijerarhija razlikuje stijenku / fluid / kote.
- [ ] Geometrija je čista, ne pretrpana.

### E. Vizualna raznolikost
- [ ] Skica ne reciklira motiv iz druge figure istog poglavlja.
- [ ] Uvodni blok ne ponavlja scene iz P/CH.

---

## 9. Alati za automatsku provjeru

| Alat | Što radi |
|---|---|
| [`tools/svg_normalize.py`](tools/svg_normalize.py) | Prefiksira ID-eve, popravlja font, dodaje root atribute. Idempotentno. |
| [`tools/strip_svg_titles.py`](tools/strip_svg_titles.py) | Uklanja top-level `<text>` naslove tipa "U[0-9]+ – ..." i pripadne podnaslove. |
| [`tools/fix_svg_xml.py`](tools/fix_svg_xml.py) | Popravlja XML konformancu: `--` u komentarima → `==`, nedostajući `;` u hex entitetima. |
| [`tools/preview_server.py`](tools/preview_server.py) | Lokalni HTTP server (port 8765) za vizualnu inspekciju svih SVG-eva po poglavlju. |

Tipičan workflow nakon nove SVG isporuke:

```powershell
py tools/svg_normalize.py        # strukturna normalizacija
py tools/strip_svg_titles.py     # uklanjanje rendered naslova
py tools/fix_svg_xml.py          # popravak XML konformance
py tools/preview_server.py       # vizualna inspekcija na http://localhost:8765/preview.html
```

---

## 10. Najčešće semantičke greške (iz Faze 1)

1. **Plave strelice za ulazne sile** — semantička greška (plava = tlak, ne sila).
2. **Oznake u skici ne odgovaraju tekstu** (skica koristi $A_e$, tekst $A_L$). Pravilo: **tekst je kanon**, skica se prilagođava tekstu.
3. **Naslov SVG-a u rendered-u** preklapa se s oznakama u gornjem dijelu canvas-a. Rješenje: ukloniti naslov (caption u Markdownu pokriva).
4. **Recikliranje motiva** unutar poglavlja (npr. ista dizalica u dvije figure). Rješenje: svaka figura nosi vlastitu vizualnu scenu.
5. **Mješanje fizikalnih veličina i pomoćnih geometrijskih crtica** bez jasne hijerarhije linija.
6. **Matplotlib generirana figura u Quarto izvoru** — zabranjeno; svi blokovi `{python}` koji renderiraju figure moraju biti zamijenjeni statičkim SVG-om.

---

## 11. Brza referenca: što treba prvo provjeriti

Ako imaš samo 30 sekundi po SVG-u:

1. **Oznake u skici = oznake u tekstu?** (najkritičnije — semantička točnost)
2. **Crvena za ulaz, zelena za izlaz, plava za tlak?** (palette)
3. **Nema rendered naslova "U[0-9]+ – ..."?** (top-level title removal)
4. **Brojevi u skici = brojevi iz Zadano?** (numerička točnost)
5. **Fluid teče?** Trasiraj putanju od ulaza do izlaza — nema "skoka preko stjenke" (vidi sekciju 12)

Ako sve točke OK, SVG je vjerojatno spreman. Detaljnija provjera (tipografija, srafura, kote) ide tek kad osnovna semantika prolazi.

---

## 12. Geometrijska koherentnost hidrauličkog sustava

> Najvažnije pravilo Faze 3: skica nije ukras, mora vjerno reproducirati **stvarnu fluidnu putanju**.

### Spojni vod između dvaju cilindara
1. **Cijev/vod mora biti na samom dnu fluida**, neposredno iznad zajedničkog dna (ne u sredini fluida). Razlog: tako se gravitacijski stvarno povezuju spremnici u realnom hidrauličkom sustavu.
2. **Fluid mora vidno biti kontinuiran** kroz cijeli sustav. Tehnički: više `<rect>` elemenata istog fill-a (gradijent vode) postavljenih bez razmaka da formiraju jedan vizualni "blob" preko cilindara i voda.
3. **Tank mora ostati VIZUALNO ZATVOREN** — stjenke su PUNE visine (od top cap-a do zajedničkog dna), bez gapa. Spoj fluida kroz port rješava se **fluid overlay-em**, NE rupom u stjenci:
   - **Krivo** (tank izgleda otvoren): stjenka podijeljena na TOP + BOTTOM s prazninom na visini voda.
   - **Ispravno**: stjenka je jedan rect pune visine (zatvoren tank). Nakon što su sve stjenke nacrtane, doda se **port fluid overlay** — mali `<rect>` u boji fluida PREKO stjenke na visini spoja (y voda). Redoslijed: (1) fluid u cilindrima i vodu, (2) sve stjenke pune visine, (3) port fluid overlay preko stjenki, (4) klipovi/sile/kote.
4. **Zajedničko dno** preko svih cilindara + voda — jedan kontinuirani hatched rect, ne više odvojenih.
5. **Klipnjača prolazi kroz brtvu** u top cap-u: tamni rect (`fill="#3a4a56"`) s 2 horizontalne svjetle linije (vizualna oznaka brtve), umjesto rupe ili overlap-a klipnjače preko hatched top cap-a.
6. **Klip mora dotaknuti fluid** — donji rub klipa = gornji rub fluida (bez gapa). Svi klipovi istog sustava neka imaju istu debljinu radi konzistentnosti.

### Što nije dopušteno geometrijski
- Cijev koja prolazi **kroz** stjenku cilindra ili dno bez vidljive rupe
- Cijev koja "lebdi" odvojeno od cilindara (gap između tube fluida i cyl fluida)
- Preklapanje voda s dnom cilindra (oba na istoj y)
- Klipnjača preko hatched cap-a bez vidljive brtve
- Tanke cijevi (<10 px) koje ne čitaju kao "veza"

### Provjera prije nego što se kaže "gotovo"
Trasiraj fluid pixel-by-pixel od ulaza (klip lijevog cilindra) do izlaza (klip desnog cilindra). Svaki segment mora **dotaknuti** sljedeći. Ako vidiš sivi piksel (stjenka, hatched) između dva plava područja koja navodno predstavljaju isti fluid, geometrija je pogrešna.

---

## 13. Strelice sila — proporcionalne i čitljive

### Format labele
**Jedna linija**, ne dvije: simbol bold + vrijednost regular weight u istom `<text>`:
```xml
<text x="..." y="..." font-size="14" font-style="italic" fill="#c0392b">
  <tspan font-weight="700">G</tspan> = 3,60 kN
</text>
```

Pogrešno (Codex pattern):
```xml
<text>G</text>
<text>= 3,60 kN</text>  <!-- u drugom redu, ispod -->
```

### Veličina trokuta strelice
Manji trokuti (Codex je koristio prevelike):
- Sile: `markerWidth="7" markerHeight="5"`, path `M0,0 L0,5 L7,2.5 z`
- Tlačne strelice u fluidu: `markerWidth="6" markerHeight="4"`, path `M0,0 L0,4 L6,2 z`
- Kote: `markerWidth="6" markerHeight="5"`, path `M0,0 L0,5 L6,2.5 z`

### Duljina strelice proporcionalna iznosu sile
Veća sila → vidno duža strelica. Skala se bira po SVG-u tako da:
- Najmanja sila bude min. ~15 px (vidljiva)
- Najveća stane u dostupan prostor iznad/ispod cilindra

Tipična skala kad su sile bliske (npr. val1: G = 3,60 kN i F₂ = 8,06 kN, omjer 2,24):
- 1 kN ≈ 7 px → G = 25 px, F₂ = 56 px

Kad je omjer velik (npr. val2: F₁ = 150 N i F₂ = 5,25 kN, omjer 35:1):
- Ne ide čisto linearno (F₁ bi bila 1 px) — koristi **stupnjevanu** skalu ili dvije zone:
  - F₁: min visible (15–20 px)
  - F₂: ~3–4× dulja od F₁ (ne 35× — samo dovoljno da se vidi da je puno veća)
- Komentarno objasniti u Provjera sekciji da je strelica simbolično skraćena.

### Pravac strelice
- Sila prema dolje (npr. G teret): line `y1 < y2`, `marker-end` na donjem kraju
- Sila prema gore (npr. F₂ podizač): line `y1 > y2`, `marker-end` na gornjem kraju
- Tipka: `marker-end` je uvijek tip strelice (kraj linije)

### Pomoćne (extension) linije za kote — OBVEZNO
Kota mora biti vidno **vezana za geometriju** koju mjeri. Sama tik-crta visoko iznad geometrije ne čita se. Standard:
1. **Pomoćne linije** (tanke, `stroke-width="0.7"`, smeđe `#b7600c`) idu OD geometrije (npr. ruba cilindra) DO razine dimenzijske linije.
2. **Tik-crte** (kratke, `stroke-width="1.2"`) na krajevima dimenzijske linije, perpendikularne na nju.
3. **Dimenzijska linija** s markerima (`marker-start` + `marker-end`) između tik-crta.

Primjer za vodoravnu kotu širine cilindra (interior x=50–190, stjenke od y=240):
```xml
<!-- Pomocne linije od stjenke do kote -->
<line x1="50" y1="240" x2="50" y2="320" stroke="#b7600c" stroke-width="0.7"/>
<line x1="190" y1="240" x2="190" y2="320" stroke="#b7600c" stroke-width="0.7"/>
<!-- Tik-crte -->
<line x1="50" y1="330" x2="50" y2="318" stroke="#b7600c" stroke-width="1.2"/>
<line x1="190" y1="330" x2="190" y2="318" stroke="#b7600c" stroke-width="1.2"/>
<!-- Dimenzijska linija -->
<line x1="53" y1="325" x2="187" y2="325" stroke="#b7600c" stroke-width="1.3" marker-start="url(#PFXDimR)" marker-end="url(#PFXDim)"/>
```

Za vertikalnu kotu (npr. hod s_L) pomoćne linije idu HORIZONTALNO od geometrije do dimenzijske osi.

### Kotači na vozilu
Ako prikaz ima vozilo na platformi (dizalica, podizač): kotači pripadaju **vozilu**, ne platformi. Dno kotača stoji NA platformi, vrh kotača veže se za karoseriju vozila. NE crtati kotače ISPOD platforme.

---

## 14. Format informacijskog panela (formula box)

### Struktura panela
1. **Header bar** ispunjen tematskom bojom (plava `#1565c0` za formule, zelena `#1e8449` za rezultate), tekst u bijelom centrirano
2. **Jednako visoki blokovi** za svaku jednadžbu, svi centrirano (`text-anchor="middle"`)
3. **Tanke svjetle separator linije** između blokova
4. **Sažetak italic** na dnu panela
5. **Zaseban "REZULTATI" badge** ispod glavnog panela (kompaktni prikaz ključnih brojeva)

### Struktura jednog bloka
```
Label sive (font-size=11, fill="#5a6a78")      ← što se računa
Formula bold crna (font-size=14, fill="#1a2530") ← kako se računa
Rezultat bold u boji (font-size=13)              ← rezultat
```

Boje rezultata:
- Plava `#1565c0` za tlak/površinu (procesni rezultati)
- Zelena `#1e8449` za izlaznu silu (krajnji rezultat)
- Crvena `#c0392b` za ulazni tlak/silu kad je ključan (npr. u rezultatima badge)

### Što izbjegavati
- **Lijevo poravnanje** mješano s indented rezultatima → izgleda netjedno
- **Različite veličine fonta** za iste tipove elemenata kroz panel
- **Nedostatak header bara** → panel izgleda kao nedovršen
- **Dvije linije gdje stane jedna** → npr. "Isti tlak · veća površina" + "→ veća sila" mogu biti zajedno na jednoj liniji ako stanu

### Primjer urednog bloka (centriran)
```xml
<!-- Blok n: y_top..y_bottom (visina ~70 px) -->
<text x="CENTER" y="Y_LABEL" font-size="11" text-anchor="middle" fill="#5a6a78">Label</text>
<text x="CENTER" y="Y_FORMULA" font-size="14" font-weight="700" text-anchor="middle" fill="#1a2530">Formula</text>
<text x="CENTER" y="Y_RESULT" font-size="13" font-weight="700" text-anchor="middle" fill="#1565c0">≈ vrijednost</text>
<line x1="..." y1="Y_SEP" x2="..." y2="Y_SEP" stroke="#c8d6e4" stroke-width="1"/>
```

### Result badge format
```xml
<rect x="..." y="..." width="..." height="44" rx="8" fill="#e8f5e9" stroke="#1e8449" stroke-width="1.4"/>
<text x="CENTER" y="Y_TITLE" font-size="11" font-weight="700" text-anchor="middle" fill="#5a6a78">REZULTATI</text>
<text x="X_LEFT" y="Y_VAL" font-size="13" font-weight="700" text-anchor="middle" fill="#c0392b">prvi rezultat</text>
<text x="X_RIGHT" y="Y_VAL" font-size="13" font-weight="700" text-anchor="middle" fill="#1e8449">drugi rezultat</text>
```
