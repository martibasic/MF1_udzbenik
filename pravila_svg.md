# Pravila za provjeru i izmjenu SVG skica — operativni cheat-sheet

> Konsolidirani sažetak pravila iz [`protokol_prerade_zadataka_i_skica.md`](protokol_prerade_zadataka_i_skica.md), [`kucni_stil_skica_val1.md`](kucni_stil_skica_val1.md) i operativnih odluka u [`qa_log_faza1.md`](qa_log_faza1.md). Ovaj dokument je radna referenca; izvori ostaju autoritativni.

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

Ako sve četiri točke OK, SVG je vjerojatno spreman. Detaljnija provjera (tipografija, srafura, kote) ide tek kad osnovna semantika prolazi.
