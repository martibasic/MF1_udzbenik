# Sustav figura za PDF i tisak

Izvorni SVG-ovi u `assets/print/` ostaju autoritativni za fiziku i mrežno
izdanje. Tiskovne izvedenice u `assets/pdf-figures/` generiraju se iz iste
geometrije i teksta. Ne uređuju se ručno. U ovom izdanju svih 94 referenciranih
skica jesu SVG-ovi; nema referenciranih PNG skica za obrezivanje. Zasebnih
17 QR kodova zadržava svoj provjereni format i funkciju.

## Formati i fizičke veličine

Autoritativni su tokeni u `assets/figure-tokens.json`. Širina tekstnog stupca
na A4 uz margine 26 mm iznosi 447,874 pt.

| Format | Širina | Primjena |
|---|---:|---|
| MINI | 34 % | Jednostavne sheme i kratke pomoćne cjeline. |
| STANDARD | 62 % | Uobičajene tehničke skice, centrirane. |
| WIDE | 100 % | Složeni povezani sustavi i široke matematičke strukture. |
| COMPOSITE | do 100 % | Povezane podslike, usporedni redci i jedan izvorni opis slike. |

Podslika u kompozitnom retku može imati polovinu dostupne širine. Nije
samostalna STANDARD figura: oznaka `subfigure` u manifestu razlikuje te ćelije
od triju samostalnih formata. MINI ne podrazumijeva sitniji tekst. Tipografija
ostaje ista i kad se geometrija povećava ili smanjuje.

| Token | Vrijednost |
|---|---:|
| `figure-label-size` | 9,5 pt |
| `figure-small-label-size` | 9 pt, uključujući jedinice i indekse u skicama |
| `figure-caption-size` | 9,5 pt |
| `figure-stroke` | osnovna crta 0,7 pt; hijerarhija prema izvornom značenju |
| `figure-arrow-size` | najveća dimenzija vrha 4 pt |
| `figure-gap` | 14 pt između podslika |
| `figure-padding` | 4 pt oko sadržaja |

Tanke crte imaju najmanje 0,5 pt. Debeli potezi koji grade cijev, masku ili
stijenku zadržavaju svoje geometrijske omjere. Gradijenti fluida, šrafure,
smjerovi vektora, hvatišta i kote ostaju povezani s izvornom geometrijom.
Uklanjaju se dekorativne kartice, pozadine zaglavlja, naglasne trake i okviri
napomena. Granica kontrolnog volumena, kućište uređaja i mreža dimenzijske
matrice nose značenje i nisu dekorativne kartice.

## Kompozicija bez promjene sadržaja

`assets/print-layouts.json` čuva provjerene logičke izreze u izvornim SVG
koordinatama te hash izvora. `before` i `after` označavaju zajedničke napomene.
Naslijeđena polja za zakretanje i povećavanje panela više ne određuju ispis.

`tools/build_print_figures.mjs` odvojeno slaže geometriju i tipografiju.
Najprije pokušava horizontalni raspored; ako oznake ne stanu, povećava
format. Mjeri stvarne glifove, prelama napomene i lokalno razmiče oznake,
uz očuvanje matematičkih indeksa i zakrenutih kota. Oznake iznad različitih
posuda i vrijednosti na osima zadržavaju prostornu pripadnost.

Provjerene posebne kompozicije nalaze se u `assets/figure-compositions.json`:
usporedba ulja i vode u U01, dimenzijska matrica, tablica dometa mlaza,
dijagram odluke, zajedničke legende te odmak oznaka i napomena od stijenki.
Svaka iznimka mora objasniti razlog; ne smije smanjivati font ispod minimuma.
Za novi složeni slučaj prvo promijeniti raspored, prijelom ili položaj oznake.

Svaki tiskovni SVG ima vlastiti obrezani `viewBox` i dimenzije u pt. Typst
umeće retke u toj fizičkoj veličini; ne rasteže ih na širinu stranice. Redci
kompozitne figure mogu se razdvojiti između stranica. Posljednja podslika,
sve napomene iza nje i izvorni opis s brojem slike ostaju na istoj stranici.
Polje `caption_anchor_panel` određuje posljednju stvarnu skicu kada iza nje
slijedi panel legende. Zajednički naslov također ostaje uz prvi redak figure.

HTML filter dodaje samo podatke za ispis. Skripta priprema skrivene tiskovne
retke, a `@media print` zamjenjuje prikaz. Na zaslonu ostaju izvorna slika,
uvećanje, opis i poveznice. CSS tokene generira isti generator iz JSON-a.

## Obnova i provjere

```text
node tools/build_print_figures.mjs
node tools/audit_print_layouts.mjs
quarto render
quarto render --profile pdf --to typst
python tools/audit_pdf.py
python tools/audit_pdf_layout.py
node tools/audit_print_site.mjs _site
```

HTML i PDF renderaju se redom, jer Quarto dijeli predmemoriju. Nakon HTML
rendera obnoviti JupyterLite i kopirati aktualni PDF u `_site/downloads/`
prema objavnom workflowu. Potreban je instaliran Chrome/Chromium/Edge i
`npm ci`; `CHROME_PATH` može odabrati preglednik.

Izmjena izvora, tokena, recepta ili generatora poništava hash u manifestu.
Audit odbija zastarjele izvedenice. Provjerava sve neprazne oznake i njihove
indekse, nepromijenjene koordinate zadržane geometrije, granice platna,
preklapanja teksta i fizički minimum 9 pt. PDF audit dodatno mjeri stvarni
font u konačnom PDF-u, uz QR kodove, opise, jednadžbe i bibliografiju. HTML
audit provjerava odvajanje zaslona i ispisa te stvarnu, neskaliranu veličinu
svakoga učitanog tiskovnog retka.

Automatske provjere dopunjuju vizualni pregled cijelog PDF-a i odnosa oznaka
prema stijenkama, fluidu, osima i vektorima. Ne dokazuju same fizikalnu
točnost. Sadržaj, ID-jevi, 90 zadataka, 87 primjera i 94 figure ostaju predmet
zasebnoga publikacijskog audita.

Redizajn smanjuje polaznih 420 stranica na 340 uz povećanje
minimalne veličine oznaka sa 7 na 9 pt. Regresijski raspon PDF audita je
310–380 stranica: približno ±10 % novog prijeloma. To je kontrola potpunosti
i neželjenog rasta dokumenta, a ne dopuštenje za sitniji tekst ili uklanjanje
sadržaja. Promjena izvan raspona zahtijeva obrazloženje i ponovni pregled.
