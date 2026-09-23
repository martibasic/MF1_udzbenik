# Arhitektura digitalnog udžbenika

Knjiga ima jedan sadržajni model i tri izlaza: web, nativni PDF i ispis
iz preglednika. Početni nalazi i odluke zapisani su u
[auditu prije implementacije](arhitekturni-audit.md).

## Izvori i odgovornosti

| Sloj | Autoritativne datoteke | Što se uređuje |
| --- | --- | --- |
| Hijerarhija | `content/book.json` | Metapodatci knjige, dijelovi, poglavlja, dodaci, naslovi, stabilne putanje |
| Sadržaj | `source/*.md` | Tekst, sekcije, formule, zadatci, captioni i alt tekst |
| Podatci | `data/`, `notebooks/` | Nastavni podatci i izvršivi pokusi |
| Komponente | `components/registry.json`, `components/chapter.qmd.tmpl` | Semantičke uloge i zajednički predložak poglavlja |
| Dizajn | `design-system/tokens.json`, `assets/figure-tokens.json` | Boje, fontovi, razmaci, širine, točke loma, PDF margine, veličine oznaka |
| Web | `styles/`, `web/`, HTML adapter | Slojevi CSS-a, navigacija iz modela, pristupačno ponašanje |
| PDF/print | `assets/typst/`, `styles/print.css.in`, Typst adapter | Prijelom, tiskovne figure, QR zamjene i držanje povezanih elemenata |
| Skice | `assets/print/`, kompozicijski manifesti | Kanonski prizori i odvojene tiskovne kompozicije |

`chapters/*.qmd`, `_quarto*.yml`, `assets/book-model.json`,
`assets/content-index.json`, početni katalog i dodatak s odgovorima su
**izvedenice**. Uključene su u Git radi pregleda i IDE pretpregleda; CI
odbija zastarjele izvedenice. Popis izvora također je
[generiran iz modela](kanonska-struktura-sadrzaja.md).

Putanje i postojeći ID-jevi sačuvani su. Ime `u04` označava stabilnu
identifikaciju datoteke, a broj prikazanog poglavlja položaj u modelu.
Dodaci imaju zaseban niz A–F. Prethodno/sljedeće poglavlje, sidebar i TOC
generira Quarto book iz istoga modela. Ispis iz preglednika koristi isti
indeks brojeva i isti tekst; nije drugi ručno održavani rukopis.

## Izgradnja i provjere

Potrebni su Quarto 1.9.37, Python paketi iz `requirements.txt`, Node paketi
iz `package-lock.json` te Chrome/Chromium/Edge za kompoziciju i vizualni QA.

```powershell
python scripts/build_book.py --write
python tools/test_book_model.py
python tools/test_render_workspace.py
python tools/test_component_visibility.py
python tools/audit_architecture.py
python scripts/build_book.py --render all
python tools/audit_pdf.py
python tools/audit_pdf_layout.py
python tools/audit_rendered_model.py _site
```

`--render web` stvara web knjigu i zasebno stranicu za ispis;
`--render pdf` stvara nativni PDF. Renderi se izvode redom. Puni proizvodni
postupak `scripts/izgradi.ps1` i GitHub workflow uključuju numeričke provjere,
notebookove, JupyterLite, kopiranje PDF-a za preuzimanje i pregled izlaza.
Pokreni `npm ci --ignore-scripts` prije prve kompozicije ili viewport audita.

Za brzi pretpregled pojedinog poglavlja prvo obnovi model pa koristi Quarto
preview. `build_book.py --render ...` automatski kopira spremljene projektne
datoteke u novu mapu `tools/tmp/render-*` i tamo koristi vlastitu `.quarto`
predmemoriju. Obuhvaćene su i nove, još necommitane datoteke koje Git ne
ignorira; ovisnosti i stari izlazi ne kopiraju se. Preview može ostati otvoren.
Git je potreban za popis ulaza. Puni renderi istog projekta zaštićeni su
zaključavanjem; drugi se odbija dok prvi radi, a zaključavanje se oslobađa
i nakon prekida procesa.

Završeni izlazi prenose se u `_site`/`_book` tek kada svi zatraženi renderi
uspiju i spremljeni ulazi ostanu isti. Ako tijekom izgradnje uređuješ izvore,
pokreni izgradnju ponovno. Neuspjeli render ne prepisuje prethodne izlaze.
Zasebno izgrađeni JupyterLite i PDF za preuzimanje ostaju sačuvani. Zamjena
pojedinih datoteka je atomska, ali prijenos cijele izlazne mape nije jedna
transakcija; otvoreni preview može naknadno obnoviti svoju stranicu.
Privremena radna mapa uklanja se nakon završetka. Pripremna regeneracija
omotača i indeksa ostaje u glavnom projektu radi IDE-a i provjere izvedenica.

Izravni `quarto render` zaobilazi ovu zaštitu. Ispis se renderira eksplicitnom naredbom koju koristi build;
sam `quarto render --profile print` može prepisati web poglavlja zbog
Quartova spajanja konfiguracijskih popisa.

## Novi sadržaj bez vlastitog HTML-a

Novo poglavlje dobiva zapis u `documents` i mjesto u jednom `parts[].chapters`.
Tekst se piše u jednoj Markdown datoteci. Ne kopiraju se omotači ili sidebar.
Pravila kolegija i verifikatorska pokrivenost i dalje vrijede; arhitekturna
proširivost ne zaobilazi autorski ugovor.

Sekcije počinju s `##`, podsekcije s `###`. Brojeve ne treba upisivati.
Za poveznice koje moraju preživjeti promjenu naslova navodi se semantički ID:

```markdown
## Bilanca sustava {#sec-bilanca-sustava}

$$ Q = A v $$ {#eq-protok-presjek}

Vidi @eq-protok-presjek.

![Opis prizora](../assets/print/stabilno-ime.svg){#fig-stabilni-prizor fig-alt="Pristupačan opis skice"}
```

Tip i fizička kompozicija figure određeni su tiskovnim manifestima; podržani
su mini, standard, wide i composite te semantički comparison/interactive.
Nove skice uključuju se u iste manifeste i generator, bez CSS-a po poglavlju.
Pravila i postupak: [tiskovne figure](ispis-skica.md). Nativne tablice s
captionom `: Opis tablice {#tbl-stabilni-id}` dobivaju broj; postojeće tablice
bez captiona ostaju bez izmišljenih naslova.

```markdown
::: {#ex-bilanca-primjer .mf1-we title="Bilanca odabranog sustava" level="T2"}
**Zadano.** Postojeći podatci.

**Traži se.** Postojeći zahtjev.

**Rješenje.** Postojeći postupak.
:::

::: {.mf1-vjezbe-list}
### Odabir sustava {#task-odabir-sustava .unnumbered .unlisted}

Iskaz zadatka.

[Razina: T1]{.mf1-task-level}
:::
```

Prikaz dodaje P1… i Z1… prema redoslijedu. T1–T4 je podatak objekta u indeksu
i u HTML-u (`data-level`). Polja koja ne postoje ne dodaju se. Stari zapisi
`mf1-box-label` ostaju podržani adapterom; novi primjer ne zahtijeva HTML.
Komponenta može sadržavati samo stvarna polja, bez obveze dopisivanja teksta.
Za ostale uloge koristi se klasa iz `components/registry.json`, primjerice
`.mf1-temelj`, `.mf1-izvod`, `.mf1-numerika`, `.mf1-zavrsni-okvir`.

Unutarnji koraci rješenja imaju `.mf1-step .unnumbered .unlisted`; adapter ih
pretvara u manje naslove koji ne mijenjaju hijerarhiju ni TOC. Primjeri su
HTML `article`, kontekst i upozorenja `section role="note"`, figure i tablice zadržavaju
nativnu semantiku, a lokalna polja rješenja pripadaju istom primjeru.
Quarto element `aside` rezervira za marginalije i automatski sužava glavni
stupac. Napomene koje pripadaju toku čitanja zato koriste semantičku ulogu
`note` unutar obične sekcije; to pravilo vrijedi za cijeli registar.

Vidljivost određuje isključivo polje `visibility` u registru komponente.
Izostavljeno polje znači sve prikaze; `[]` skriva komponentu svugdje;
`["web", "print"]` prikazuje je u HTML-u i ispisu iz preglednika, a izostavlja
iz nativnog PDF-a. Dopuštene vrijednosti su `web`, `pdf` i `print`.
Sva tri adaptera koriste `filters/mf1-component-model.lua`; PDF nema zaseban
popis skrivenih klasa. Povezani naslov prati isto pravilo, uz očuvanje sidra
kada je skriven. HTML razlikuje zaslon i ispis zajedničkim medijskim pravilima.
Postojeća priprema i samoprovjera zadržavaju `[]`; promjena mehanizma nije
odobrenje za promjenu vidljivog sadržaja.

## Referencije i metapodatci

```markdown
Vidi @ex-bilanca-primjer i @task-odabir-sustava.
[]{.mf1-chapter-ref target="u04"}
[gustoća]{.mf1-term term="Gustoća"}
[]{.mf1-book-meta key="author"}
```

Brojevi referencija dolaze iz indeksa, ne iz ručnog teksta. Odjeljci, slike,
tablice i jednadžbe koriste Quarto `@sec-*`, `@fig-*`, `@tbl-*`, `@eq-*`.
ID i URL nisu broj; pri premještanju ih treba sačuvati. Izgovoreno upućivanje
na primjer iz drugog poglavlja zato sadrži broj oblika „primjer 4.2”, dok
lokalni naslov zadržava P2. Pojmovnik dobiva stabilne sidrene oznake iz pojma.

## Globalne promjene izgleda

- Boje, web font, širina i H2: `design-system/tokens.json` → `web`.
- PDF font, H2 i margine: isti dokument → `pdf`.
- Točke loma: isti dokument → `breakpoints`.
- Skice, font oznaka i debljine crta: uvezeni `assets/figure-tokens.json`.

`text-width-pt` je izvedena širina A4 lista umanjena za PDF margine.
Build je obnavlja i regenerira figure kada se promijene ulazi. Oznake zadržavaju
zasebnu veličinu u točkama. Promjena fonta izvan već učitanih obitelji zahtijeva
i dostupnost fonta / odgovarajući `web_font_import`.

CSS se učitava redom tokens → base → typography → layout → components →
utilities → print → responsive. Bootstrapove zadane vrijednosti generiraju
se u `design-system/quarto-theme.scss`; nema selektora vezanih uz poglavlje.
`!important` ograničen je na deklariranu vidljivost i reduced-motion.
Typst ima vlastiti prijelom: naslov ostaje uz sadržaj, caption uz sliku,
kratki zadatci i redci figura drže se zajedno gdje stanu. Cijeli dugi izvod
ili primjer ne zaključava se u jedan neprelomljiv blok.

## Što provjere dokazuju

`audit_architecture.py` provjerava model, izvedenice, objekte, reference,
razine i CSS slojeve. `test_book_model.py` premješta poglavlja i objekte te
provjerava promjenu brojeva uz očuvanje identiteta i formula.
`audit_rendered_model.py` uspoređuje stvarne brojeve odjeljaka, captiona,
jednadžbi i P/Z naslova u webu i zbirnom ispisu s indeksom.
Ostali postojeći auditi provjeravaju numeriku, poveznice, PDF, skice,
tipkovnicu, kontrast i prelijevanje na 320/768/1440 px.

Automatska provjera ne zamjenjuje vizualni pregled PDF-a i složenih skica.
Posebno nakon promjene globalnog fonta ili margina treba obnoviti i pregledati
sva tri izlaza. Znanstvena recenzija i studentski pilot ostaju odvojeni poslovi.

Rezultati početnog refaktora zabilježeni su u
[završnoj provjeri](arhitekturna-provjera.md).
