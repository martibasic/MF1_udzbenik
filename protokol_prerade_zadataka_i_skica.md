# Protokol prerade zadataka i skica za MF1_udzbenik

## Svrha dokumenta

Ovaj dokument ostaje aktivni operativni protokol za svaku novu ozbiljnu preradu zadatka ili skice u `MF1_udzbenik`. Ne sluzi vise za masovni migracijski val, nego za selektivne buduce dopune i za kvalitetno preoblikovanje pojedinih jacih zadataka.

## Kada se ovaj protokol koristi

1. Kad se u poglavlje uvodi novi zadatak iz internog ili vanjskog donor-izvora.
2. Kad se postojeci zadatak znacajno preraduje radi boljeg inzenjerskog konteksta, bolje gradacije ili jacih trazenih velicina.
3. Kad se mijenja ili iznova crta skica koja vise ne zadovoljava kucni standard.
4. Kad se otvara novi jaci `WE` ili `CH` koji treba biti reprezentativan za poglavlje.

## Kada se ovaj protokol ne koristi

1. Za cisto jezikoslovno ili interpunkcijsko uredjivanje.
2. Za sitnu notacijsku izmjenu bez promjene scenarija zadatka.
3. Za mehanicko prepisivanje postojeceg javnog zadatka u drugi layout.
4. Za ponovno otvaranje masovnog prijenosa iz starih izvora.

## Temeljna urednicka odluka

1. Izvorni zadatak sluzi kao banka ideja, a ne kao tekstualni predlozak.
2. Javna verzija mora biti nasa u formulaciji, scenariju, zadanom, trazenom i skici.
3. `legacy_ref` i trag izvora ostaju u internim evidencijama, ali ne smiju upravljati stilom javne verzije.
4. Ako je izvor autorski osjetljiv, ne radi se kozmeticka parafraza nego stvarna rekonstrukcija od nule.

## Sto se ne smatra dovoljnom preradom

1. Isti zadatak s drugim brojkama.
2. Isti redoslijed recenica sa sinonimima.
3. Ista geometrija i isto trazeno uz drukcije oznake varijabli.
4. Precrtana ili samo "ociscena" izvorna skica.
5. Spajanje dvaju slicnih zadataka bez nove didakticke svrhe.

## Minimalni prag prihvatljive prerade

Da bi se zadatak smatrao prihvatljivo preradenim, mora promijeniti najmanje `3 od 5` sljedecih elemenata:

1. geometriju ili topologiju sustava
2. fizikalni scenarij ili inzenjerski kontekst
3. skup zadanih velicina
4. skup trazenih velicina
5. numericki rezim ili omjere karakteristicnih velicina

Dodatno pravilo: barem jedna promjena mora biti strukturna, odnosno mora zahvatiti `1`, `2` ili `4`. Sama promjena brojki, jedinica ili notacije nije dovoljna.

## Razine prerade

- `P0 - zabranjeno`: gotovo isti tekst, ista skica i iste brojke
- `P1 - preslabo`: novi brojevi i malo drukciji stil, ali ista scena i isti put rjesavanja
- `P2 - prihvatljivo`: nova scena ili geometrija, drukcije zadano i/ili trazeno, rjesenje izvedeno od nule
- `P3 - pozeljno`: novi zadatak s jasnom vlastitom didaktickom svrhom, vlastitom skicom i vlastitom tezinskom gradacijom

Za glavni tok knjige cilj je `P2` kao minimum, a `P3` kad god se radi o visem integracijskom sloju ili reprezentativnom primjeru poglavlja.

## Operativni postupak po zadatku

### 1. Izvuci jezgru, ne tekst

Za izvorni zadatak prvo treba zapisati samo sljedece:

- koji zakon ili model provjerava
- koja je minimalna geometrijska scena
- koja je stvarna didakticka tezina
- sto je stvarno zanimljivo: sila, protok, tlak, moment, stabilnost ili granicni uvjet

### 2. Odredi ulogu nove verzije

Nova verzija mora imati jednu jasnu urednicku ulogu:

- uvodni bazni zadatak
- tipicna varijanta
- prijelaz prema tezoj sceni
- integracijski ili izazovni zadatak

Ako ta uloga nije jasna, ne treba jos pisati finalni tekst zadatka.

### 3. Izgradi novu scenu

Nova scena se gradi jednom od sljedecih strategija:

1. promijeni geometriju, a zadrzi zakon
2. zadrzi fizikalnu jezgru, ali promijeni inzenjerski kontekst
3. obrni smjer zadatka tako da se trazi nova velicina
4. razbij jedan izvorni zadatak na dvije smislenije razine ili spoji dvije ideje u jedan jaci integracijski problem

### 4. Prepakiraj zadano i trazeno

Dobar znak prerade je kad student u novoj verziji mora napraviti drukciji prvi korak nego u izvornom zadatku.

### 5. Rijesi zadatak od nule

Finalna verzija mora imati:

1. vlastitu skicu ili vlastiti kontrolni volumen
2. novi popis pretpostavki
3. vlastiti redoslijed jednadzbi
4. vlastitu numericku provjeru

### 6. Napravi urednicki check

Prije prihvacanja provjeri sljedece:

1. moze li se zadatak procitati bez izvornog teksta
2. bi li student prepoznao novu scenu, a ne samo druge brojke
3. ima li zadatak jasnu ulogu u gradaciji poglavlja
4. postoji li vlastita skica ili je svjesno odluceno da skica nije potrebna

Ako je odgovor "ne" na neko od prva tri pitanja, prerada se vraca na prethodni korak.

## Operativni metapodaci koje treba voditi interno

- `rewrite_status`: `nije_potrebno`, `za_preradu`, `u_preradi`, `preradeno`, `pravno_provjereno`
- `rewrite_level`: `P0`, `P1`, `P2`, `P3`
- `sketch_requirement`: `obavezna`, `preporucena`, `nije_potrebna`

Ta polja ne sluze studentima, nego internom pracenju kvalitete.

## Pravilo za skice

### Opce pravilo

Skica se ne radi kao ukras, nego da ukloni geometrijsku ili fizikalnu dvosmislenost.

### Sto je zabranjeno

1. precrtavanje izvorne slike liniju po liniju
2. zadrzavanje istog rasporeda oznaka i mjernih linija kad je scena i dalje prepoznatljivo ista
3. dekorativne skice koje ne sluze rjesavanju

### Trenutni kucni standard skica

1. skica mora biti print-first i citljiva u grayscale rezimu
2. geometrija mora biti cista i tanja nego u starijim skicama
3. label-boxovi i kote moraju biti izmaknuti iz geometrije kad god to poboljsava citljivost
4. vektori, kote i granice sustava moraju imati jasnu hijerarhiju kontrasta
5. tekst se ne smije naslanjati preko same geometrije ako postoji cist vanjski raspored

## Brza odluka o tome treba li skica

Skica je `obavezna` ako je odgovor "da" barem na jedno od ovih pitanja:

1. postoji li vise od jedne karakteristicne razine, tocke ili osi
2. postoji li kut, zakrivljena ploha ili promjena smjera strujanja
3. treba li student odabrati kontrolni volumen ili rastaviti silu na komponente
4. ovisi li rjesenje o polozaju tezista, istisnine, hvatiste sile ili slobodne povrsine

Ako je odgovor svugdje "ne", skica je obicno samo `preporucena` ili `nije_potrebna`.

## Trenutna prakticna uporaba protokola

U danasnjoj fazi knjige ovaj protokol koristi se samo za selektivne buduce dopune `MF1_udzbenik`, za jacanje reprezentativnih zadataka i za eventualnu zamjenu slabijih skica. Ne koristi se kao izgovor za ponovno otvaranje cijelog prijenosnog backlog-a.

---

## SVG standard za skice i ilustracije

Ovaj odjeljak je kanonski i autoritativan. Svi novi i rerađeni SVG-ovi u `MF1_udzbenik` moraju ga poštovati u potpunosti.

### Kanonski format i pohrana

Sve skice i ilustracije pohranuju se kao statičke SVG datoteke u:

```
MF1_udzbenik/assets/print/uXX_*.svg
```

Matplotlib/Python kod za generiranje figura **zabranjeno** je koristiti u finalnim Quarto izvorima. Referenca iz `source/uXX_naziv.md`:

```markdown
![Opis slike.](../assets/print/uXX_naziv_skice.svg){#fig-oznaka fig-align="center"}
```

Za slike kojima treba ograničiti širinu (npr. kvadratne, uske):

```markdown
![Opis.](../assets/print/uXX_fig.svg){#fig-oznaka fig-align="center" out-width="45%"}
```

### Konvencija imenovanja datoteke

Format: `uXX_tip_kratki_opis.svg`

| Prefiks tipa | Svrha |
|---|---|
| `val1`, `val2`… | riješeni primjer (wave-of-the-art) |
| `ch1`, `ch2`… | challenge (izazovni zadatak) |
| `fig_uvod_pregled` | uvodni figure-blok poglavlja |
| `fig_naziv_scene` | ilustracija specifičnog riješenog primjera |

Primjeri: `u01_val1_klip_manometar.svg`, `u01_fig_uvod_pregled.svg`, `u02_fig_kapilarni_uspon_etanol.svg`

### Obvezni tehnički atributi svakog SVG-a

```xml
<svg xmlns="http://www.w3.org/2000/svg"
     viewBox="0 0 SIRINA VISINA"
     role="img"
     aria-labelledby="PREFIXvT PREFIXvD"
     preserveAspectRatio="xMidYMid meet"
     style="display:block;width:100%;max-width:XXXpx;height:auto;">
  <title id="PREFIXvT">Kratki opis za screenreader</title>
  <desc  id="PREFIXvD">Duži opis sadržaja slike za pristupačnost</desc>
  <defs>
    <!-- markeri, gradienti, srafure ovdje -->
  </defs>
  ...
</svg>
```

**Pravilo za ID prefikse:** svaka SVG datoteka dobiva kratki jedinstven prefiks (npr. `u1kp` za `u01_val1_klip_manometar`, `u2ke` za `u02_fig_kapilarni_uspon_etanol`). Svi `id` atributi unutar te datoteke počinju tim prefiksom. Bez prefiksa zabranjeno — kolizija ID-ova na HTML stranici uzrokuje broken markere i gradiente.

Tipične vrijednosti `max-width`:
- Uski prikaz (jedan element, kvadratni): `420–540 px`
- Standardna ilustracija (jedan prizor): `640–720 px`
- Uvodni pregled / dvo-panelna slika: `800–900 px`
- Tro-panelni uvodni blok: `960–980 px`

---

### Kanonska paleta boja

Ova paleta je jedina dopuštena za nove SVG-ove. Derogacije od palete moraju biti obrazložene u komentaru unutar SVG-a.

#### Fluidi

| Fluid | Gornji stop | Donji stop | Primjena |
|---|---|---|---|
| Voda / opći fluid | `#aed6f1` | `#5b9ec9` | hidrostatika, tlak, cijevi |
| Ulje / hidraulično ulje | `#fde68a` → `#c8a000` | zlatno-žuta | klizni ležajevi, kapilarnost ulje |
| Gorivo (dizel, benzin) | `#fde68a` | `#d4a017` | cisterne, gorivni tank |
| Živa | `#b0b8c0` | `#808890` | manometri s živom |

Gradient se uvijek definira vertikalno (`x1="0" y1="0" x2="0" y2="1"`).

#### Stijenke, kućišta i čvrsti elementi

| Svrha | Boja |
|---|---|
| Gornja boja stijenke / klipa | `#909fa8` |
| Donja boja stijenke / klipa | `#5d6d7e` |
| Tamni rub/okvir geometrije | `#3a4a56` |
| Srafura (linija u patternu) | `#7a8a96` |

#### Vektori i oznake

| Svrha | Boja | Napomena |
|---|---|---|
| Sila ulaz / opterećenje / kočenje | `#c0392b` | crvena |
| Sila izlaz / rezultat / korisna | `#1e8449` | zelena |
| Tlak / dubina / površinski napon | `#1565c0` | plava |
| Kota / dimenzija | `#b7600c` | smeđa |
| Efektivno polje sila (g_eff, rotacija) | `#8e44ad` | ljubičasta |
| Kutna brzina ω / rotacija | `#1e8449` | zelena |
| Δh/2 razmaci (paraboloid) | `#e67e22` | narančasta |

#### Header bar uvodnih figure-blokova

```xml
<linearGradient id="PREFIXhdr" x1="0" y1="0" x2="1" y2="0">
  <stop offset="0%" stop-color="#1a2e42"/>
  <stop offset="100%" stop-color="#1a3a52"/>
</linearGradient>
<rect x="0" y="0" width="SIRINA" height="48" fill="url(#PREFIXhdr)"/>
<text x="SIRINA/2" y="22" ... fill="white" text-anchor="middle">Naslov poglavlja</text>
<text x="SIRINA/2" y="40" ... fill="#8aaccc" text-anchor="middle">ključne riječi · poglavlja</text>
```

---

### Standard srafure (hatch pattern)

Srafura stijenki i kućišta uvijek je 45° dijagonala, veličina 7×7 px:

```xml
<pattern id="PREFIXh" width="7" height="7" patternUnits="userSpaceOnUse" patternTransform="rotate(45)">
  <line x1="0" y1="0" x2="0" y2="7" stroke="#7a8a96" stroke-width="1.8"/>
</pattern>
```

Srafurirani elementi (stijenka, dno, kućište):

```xml
<rect x="..." y="..." width="..." height="..." fill="url(#PREFIXh)" stroke="#3a4a56" stroke-width="1.8"/>
```

---

### Standard kota (dimenzijskih linija)

Kote se crtaju s dvo-smjernim markerima, tik-crtama i tekstom izmaknuti od geometrije.

#### Marker definicije (u `<defs>`)

```xml
<!-- Desni/gornji kraj kote -->
<marker id="PREFIXDim" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto">
  <path d="M0,0 L0,8 L8,4 z" fill="#b7600c"/>
</marker>
<!-- Lijevi/donji kraj kote (auto-start-reverse) -->
<marker id="PREFIXDimL" markerWidth="8" markerHeight="8" refX="1" refY="4" orient="auto-start-reverse">
  <path d="M0,0 L0,8 L8,4 z" fill="#b7600c"/>
</marker>
```

#### Crtanje kote (vertikalna, primjer)

```xml
<!-- Tik-crte na oba kraja -->
<line x1="x-5" y1="y1" x2="x+1" y2="y1" stroke="#b7600c" stroke-width="1.3"/>
<line x1="x-5" y1="y2" x2="x+1" y2="y2" stroke="#b7600c" stroke-width="1.3"/>
<!-- Dimenzijska linija s markerima -->
<line x1="x-3" y1="y1+2" x2="x-3" y2="y2-2"
      stroke="#b7600c" stroke-width="1.5"
      marker-start="url(#PREFIXDimL)" marker-end="url(#PREFIXDim)"/>
<!-- Oznaka -->
<text x="x-12" y="(y1+y2)/2" font-family="..." font-size="12" font-style="italic"
      fill="#b7600c" text-anchor="end">L</text>
```

Pravila:
- Tekst kote uvijek izvan geometrije (barem 8 px odmak od tik-crte).
- Kote za osi X ide ispod geometrije, za os Y s lijeve ili desne strane.
- Numerička vrijednost (npr. `1,2 m`) navodi se ispod/pored oznake ako je relevantna.
- Decimalni separator: **zarez** (hrvatska konvencija), npr. `1,2 m`, `22,5 cm`.

---

### Standard strelica sila i vektora

#### Marker definicije

```xml
<!-- Crvena sila (ulaz, opterećenje, ubrzanje) -->
<marker id="PREFIXaR" markerWidth="10" markerHeight="8" refX="9" refY="4" orient="auto">
  <path d="M0,0 L0,8 L10,4 z" fill="#c0392b"/>
</marker>
<!-- Zelena sila (rezultat, korisna) -->
<marker id="PREFIXaG" markerWidth="10" markerHeight="8" refX="9" refY="4" orient="auto">
  <path d="M0,0 L0,8 L10,4 z" fill="#1e8449"/>
</marker>
<!-- Plava sila (tlak, dubina) -->
<marker id="PREFIXaB" markerWidth="10" markerHeight="8" refX="9" refY="4" orient="auto">
  <path d="M0,0 L0,8 L10,4 z" fill="#1565c0"/>
</marker>
<!-- Ljubičasta (g_eff, efektivno polje) -->
<marker id="PREFIXaP" markerWidth="10" markerHeight="8" refX="9" refY="4" orient="auto">
  <path d="M0,0 L0,8 L10,4 z" fill="#8e44ad"/>
</marker>
```

Strelica sile: `stroke-width="2.5–3.0"`, linija iste boje kao marker.  
Strelica kote: `stroke-width="1.4–1.6"`, boja `#b7600c`.

---

### Tipografija

Jedina dopuštena font-family deklaracija:

```xml
font-family="'Segoe UI',Arial,sans-serif"
```

Veličine teksta:

| Svrha | font-size | Stil |
|---|---|---|
| Naslov panela / poglavlja | `18` | `font-weight="700"` |
| Podpodnaslov / caption panela | `13–14` | `font-weight="700"` |
| Oznaka varijable (italic) | `11–14` | `font-style="italic"` |
| Jednadžba (inline) | `14–22` | `font-style="italic"` |
| Opisni tekst / legenda | `10–11` | normalni |
| Kota broj | `10–12` | normalni ili italic |

Pravila:
- Tekst se ne smije naslanjati na geometriju: minimalan odmak 6 px.
- `text-anchor="middle"` za središnje naslove panela; `text-anchor="end"` za oznake s desne na lijevu stranu.
- Za jednadžbe u SVG-u koristiti Unicode znakove: `Δ`, `α`, `τ`, `μ`, `ν`, `ρ`, `σ`, `ω`, `²`, `³`, `·`, `≈`, `≤`, `≥`.

---

### Konstruktivni detalji po tipu prizora

#### Menisk (kapilarnost)

Konkavni menisk crta se Bezier krivuljom:

```xml
<path d="M x1,y1 Q xc,yc_gore x2,y2" fill="none" stroke="#1565c0" stroke-width="2.2"/>
```

gdje je `yc_gore` kontrolna točka **iznad** y1 i y2 (dižući sredinu prema gore za konkavni menisk).  
Konveksni menisk: kontrolna točka **ispod** (spuštajuća sredina).

Kut θ crta se lukom `<path d="M ... A r,r 0 0 0 ..." stroke="#8e44ad"/>` s tekstom `θ` u istoj boji.

#### Slobodna površina (nagnuta, ubrzanje)

Za linearno nagnutu slobodnu površinu:

```xml
<!-- Fluid (trapez) -->
<polygon points="x_l,y_l x_r,y_r x_r,y_dno x_l,y_dno" fill="url(#PREFIXfl)" opacity="0.88"/>
<!-- Slobodna površina -->
<line x1="x_l" y1="y_l" x2="x_r" y2="y_r" stroke="#1565c0" stroke-width="2.4"/>
<!-- Mirna razina (isprekidana) -->
<line x1="x_l" y1="y_h0" x2="x_r" y2="y_h0" stroke="#7a8a96" stroke-width="1.4" stroke-dasharray="9,6"/>
```

Mirna razina uvijek isprekidana; slobodna površina puna linija, deblja.

#### Paraboloid (rotirajući cilindar)

Aproximacija kubičnim Bezierom koji daje vizualno točan paraboloid:

```xml
<path d="M x_l,y_rub C x_l,y_osa HALF,y_osa HALF,y_osa C HALF,y_osa x_r,y_osa x_r,y_rub"
      fill="none" stroke="#1565c0" stroke-width="2.8"/>
```

gdje je `HALF` horizontalna sredina cilindra, `y_osa` najniža točka (os), `y_rub` najviša točka (rub).

#### Osi simetrije

Vertikalna os simetrije cilindra ili simetričnih elemenata:

```xml
<line x1="x_ctr" y1="y_top" x2="x_ctr" y2="y_bot"
      stroke="#88a" stroke-width="1.2" stroke-dasharray="5,4"/>
```

---

### Kutija s rezultatima (result box)

Za prikaz numeričkih rezultata unutar SVG-a:

```xml
<rect x="..." y="..." width="..." height="..." rx="7"
      fill="white" stroke="#BOJA" stroke-width="1.4"/>
<text ... font-size="13" font-style="italic" fill="#1a2530" text-anchor="middle">formula</text>
<text ... font-size="13" font-weight="700" fill="#c0392b" text-anchor="middle">rezultat</text>
```

Pravila:
- Konačni numerički rezultat uvijek `fill="#c0392b"` (crvena) ili `fill="#1e8449"` (zelena) i `font-weight="700"`.
- Rubna boja kutije odgovara tematskoj boji odjeljka (plava za tlak, smeđa za kotu, zelena za rezultat…).

---

### Filozofija uvodnog figure-bloka poglavlja (fig-uvod-uXX)

Uvodni figure-blok **mora** prikazivati tri konceptualno odvojena panela:

| Panel | Sadržaj |
|---|---|
| Lijevo (široki) | Fizikalni model – geometrija sustava, vektori sila, kote, oznake veličina |
| Srednji ili gornji desni | Ključne jednadžbe poglavlja u kutijama (po jedna jednadžba po kutiji) |
| Donji desni | Primjena u strojarstvu / industriji – scena koja se **ne smije ponavljati** u riješenim primjerima |

Svaki panel ima naslov (tamni tekst, `font-weight="700"`) i laganu pozadinsku boju koja razlikuje panele.  
Cijeli SVG ima tamni header bar s naslovom poglavlja i ključnim riječima.

Zabranjeno u uvodnom figure-bloku:
- Koristiti isti vizualni motiv koji se pojavljuje u bilo kojoj drugoj figuri istog poglavlja.
- Prikazivati samo jedan prizor bez pregleda temeljnih ideja.
- Izostaviti header bar s oznakom poglavlja.

---

### Pravilo o vizualnoj raznolikosti unutar poglavlja

1. Svaka figura u poglavlju prikazuje zasebnu fizikalnu scenu i zasebni geometrijski prizor.
2. Zabranjeno je reciklirati isti motiv (npr. isto vozilo, ista posuda, ista geometrija ležaja) u različitim figurama istog poglavlja.
3. Uvodni figure-blok najosjetljiviji je: smije prikazivati isključivo scene kojih **nema** u riješenim primjerima tog poglavlja.

---

### Što nije dopušteno u SVG skicama

1. Generiranje SVG-a matplotlib/Python kodom u Quarto izvoru.
2. Kopiranje vizualnog rasporeda iz starih matplotlib skica bez strukturne promjene geometrije.
3. Pojava istog vizualnog motiva u više od jedne figure unutar istog poglavlja.
4. Izostanak `<title>` i `<desc>` elemenata (obavezno za pristupačnost).
5. Globalni (ne-prefiksani) `id` atributi koji mogu kolidirati s drugim SVG-ima na istoj HTML stranici.
6. Decimalna točka umjesto zareza u numeričkim vrijednostima (koristiti `1,2 m`, ne `1.2 m`).
7. Font izvan `'Segoe UI', Arial, sans-serif`.
8. Preklapanje teksta s geometrijom ili vektorima.
9. Kote bez tik-crta na krajnjim točkama.
10. Strelice sila bez `<marker>` elemenata (ne koristiti samo `stroke-width` za simulaciju strelice).

---

### Operativni postupak za pisanje novih SVG-a

Za **novu** datoteku koristiti `create_file`. Za **prepisivanje** postojeće datoteke koristiti PowerShell here-string:

```powershell
$svg = @'
<svg ...>
  ...
</svg>
'@
$svg | Set-Content "assets\print\uXX_naziv.svg" -Encoding UTF8 -NoNewline
Write-Host "OK $((Get-Item 'assets\print\uXX_naziv.svg').Length) bytes"
```

Provjera po završetku:
1. Veličina datoteke razumna (tipično 5–25 KB za ručno pisani SVG).
2. `quarto render chapters/uXX_naziv.qmd` prolazi bez grešaka.
3. Vizualni pregled u browseru: nema preklapanja teksta, kote su čitljive, boje odgovaraju paleti.

---

### Status SVG konverzije po poglavljima (svibanj 2026)

| Poglavlje | Uvodni blok | Fig. primjera | Status |
|---|---|---|---|
| U01 | ✅ | ✅ 8 SVG-a | Potpuno konvertirano |
| U02 | ✅ | ✅ 4 SVG-a | Potpuno konvertirano |
| U03 | ✅ | ✅ 4 SVG-a | Potpuno konvertirano |
| U04 | ✅ | ✅ 3 SVG-a | Potpuno konvertirano |
| U05–U13 | ❓ | ❓ | Provjera potrebna – selektivna konverzija |