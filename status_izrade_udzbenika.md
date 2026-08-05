# Status izrade udžbenika MF1

**Presjek:** 1. kolovoza 2026.

**Cilj izdanja:** tehničko stanje **spremno je za `1.0-rc1`**; `v1.0` dolazi tek
nakon dviju neovisnih stručnih recenzija i studentskog pilota.

Ovaj dokument opisuje stanje v2 revizije u aktualnoj radnoj grani. Kanonski
izvori, HTML, nativni PDF i JupyterLite sekvencijski su izgrađeni i prošli
tehnički QA. Time se ne tvrdi da je izdanju dodijeljena oznaka `v1.0`, da su
ljudski kriteriji provedeni ili da je kandidat javno deployan.

## Legenda

- **Implementirano** — sadržaj ili provjera postoji i prolazi u radnoj grani.
- **Tehnički RC spremno** — završni artefakt iz aktualnih izvora izgrađen je i
  prošao pripadajući automatizirani i renderirani QA.
- **Ljudski kriterij** — zahtijeva vanjske recenzente ili stvarne studente i ne
  može se zatvoriti automatizacijom u repozitoriju.

## Sažetak po radnim tokovima

| Radni tok | Status | Dokaz i granica tvrdnje |
|---|---|---|
| Arhitektura U01–U15 | **Implementirano** | Kanonski slijed ima 15 poglavlja i šest dodataka. Stari javni URL-ovi imaju prijelazna preusmjerenja, a `source/` ostaje jedini kanonski izvor. |
| Sadržaj i opterećenje | **Implementirano** | Inventar sadrži 87 riješenih primjera, 90 samostalnih zadataka i 145 sati rada uz udžbenik. Svako glavno poglavlje ima šest zadataka u raspodjeli `2×T1 + 2×T2 + T3 + T4`. |
| Konciznost glavnog teksta | **Implementirano** | Usporedivi regex inventar leksičkih tokena smanjen je sa 124.957 u prethodnih 14 poglavlja na 108.711 u RC-u s 15 poglavlja (`−13,00 %`), pa je kriterij rasta od najviše 5 % ispunjen. |
| Znanstvena korektura | **Implementirano u rukopisu** | Ispravljeni su poznati P0/P1 nalazi o predznacima, referentnom tlaku, nestacionarnosti, radu strojeva, kavitaciji, stabilitetu i granicama modela. Automatizirane fizikalne regresije prolaze 22/22; neovisna stručna potvrda ostaje zaseban ljudski kriterij. |
| Tekst i izvodi | **Implementirano** | Uvedeni su standardni blokovi, jasnije pretpostavke, granični slučajevi i granice modela; napredni detalji odvojeni su u blokove `Dublje` ili dodatke. |
| Zadaci i ključ | **Implementirano** | Svih 90 zadataka ima stabilni ID, razinu, zapis u zasebnom D06 ključu i `golden` ugovor u manifestu sheme v2. Manifest sadrži 393 parsirana skalarna ulaza i 312 ugovora rezultata; naputci i kontrolni rezultati odvojeni su od iskaza zadatka. |
| Numerički QA | **Implementirano** | `verify_all.py` obuhvaća 19 modula i prolazi 1.001 provjeru: 924 usporedbe s unaprijed zadanim ciljem te 77 invarijantnih, dimenzijskih ili graničnih provjera. Evidentirano je 0 self-comparison usporedbi, 0 rupa i 0 neprovjerenih zadataka. |
| Notebookovi | **Implementirano** | Svih 17 notebookova slijedi obrazac `predvidi → izračunaj → provjeri`, ima najmanje dvije izvršive tvrdnje i analizu pogreške, konvergencije, osjetljivosti ili nesigurnosti. Lokalno izvršavanje u čistim kernelima prolazi 17/17. |
| CFD V&V paketi | **2 spremna + 1 referentni** | Poiseuille i Venturi/difuzor imaju tri mreže, reziduale/monitore, masenu bilancu i GCI; oba su jasno označena kao sintetički nastavna. NACA 0012 ima javna mjerenja i tri najfinije FUN3D mreže, ali izvorna arhiva nema reziduale, monitore, maseni debalans ni potpuni mjerni budžet nesigurnosti. |
| Stabilna javna sučelja | **Implementirano** | Inventar sadrži 1.185 stabilnih ID-jeva i 789 prikazanih jednadžbi. Unutarnje veze, 11 prijelaznih preusmjerenja i zabrana kopiranja kanonskog `source/` u javni izlaz provjeravaju se automatizirano. |
| Skice i izvorna pristupačnost | **Tehnički RC spremno** | 143/143 SVG datoteke prošle su izvorni audit; završni HTML sadrži 210 renderiranih slika, a PDF i A4 prikaz uključeni su u izlazni vizualni QA. |
| Hrvatska lokalizacija | **Tehnički RC spremno** | Hrvatski UI, tipkovnički fokus, smanjeno gibanje, mobilno prelamanje i kontrast provjereni su u 72 prikaza na 320, 768 i 1.440 px te u zasebnom A4 prikazu. |
| HTML izdanje | **Tehnički RC spremno** | Sekvencijski izgrađen artefakt prolazi audit: 24 stranice, 210 slika, 2.081 veza, 472 sklopiva bloka i 11 preusmjerenja. |
| Nativni PDF | **Tehnički RC spremno** | Quarto/Typst PDF ima 299 A4 stranica i 7.045.244 B; audit ekstrahira 536.983 znaka. Autorski blokovi i primjeri nativno su stilizirani, prvi red odlomka nema uvlaku, a razmak između odlomaka iznosi `0.72em`. |
| JupyterLite | **Tehnički RC spremno** | Završni paket s Pyodide kernelom i svih 17 notebookova izgrađen je; strukturni audit i preglednički smoke-test kernela prolaze. Colab ostaje pričuvni put. |
| Citati i normativne tvrdnje | **Implementirano u rukopisu** | Lokalni citati povezuju promjenjive i normativne tvrdnje s primarnim izvorima, a konstrukcijska i sigurnosna značenja ograničena su na stvarno provedeni model. Vanjski recenzenti provjeravaju konačnu stručnu dostatnost. |
| Errata i dnevnik izmjena | **Implementirano** | Postoje javni issue obrazac, evidencija po stabilnom ID-ju i `CHANGELOG.md`; tablica errate ostaje prazna dok nema potvrđene pogreške objavljenoga izdanja. |

## Aktualna QA snimka

Provjere su pokrenute iz korijena repozitorija 1. kolovoza 2026. nad kanonskim
izvorima i sekvencijski izgrađenim RC artefaktima.

| Provjera | Rezultat | Tumačenje |
|---|---|---|
| `python tools/generate_verification_manifest.py` | **PASS**, shema v2, 90/90 `golden` zadataka | Manifest se reproducibilno izvodi iz kanonskih zadataka; sadrži 393 parsirana skalarna ulaza i 312 ugovora rezultata. |
| `python tools/verify_all.py` | **PASS**, 19 modula, 1.001/1.001 | 924 usporedbe s hard-coded ciljem + 77 invarijantnih, dimenzijskih ili graničnih provjera; 0 self-comparison zapisa i 0 rupa. |
| `python tools/verify_physics.py` | **PASS**, 22/22 | Kritični golden testovi pokrivaju predznake, bilance, granične slučajeve i energetski ledger; nisu zamjena za čitanje cijeloga rukopisa. |
| `python tools/execute_notebooks.py` | **PASS**, 17/17 | Svaki notebook izvršen je od početka u zasebnom čistom kernelu bez spremljenih izlaza. |
| `python tools/validate_cfd_vv.py` | **PASS**, 2 spremna + 1 referentni | Validator čuva eksplicitne arhivske praznine NACA skupa i ne proizvodi sintetičke dokaze za njih. |
| `python tools/audit_publication.py` | **PASS** | Potvrđuje 15 poglavlja, 87 primjera, 90 zadataka, šest dodataka, 145 sati, 1.185 stabilnih ID-jeva, 789 jednadžbi i 17 JupyterLite ulaza. |
| `python tools/audit_rendered_site.py _site` | **PASS** | HTML ima 24 stranice, 210 slika, 2.081 vezu, 472 sklopiva bloka i 11 preusmjerenja; kanonski Markdown nije javni resurs. |
| `python tools/audit_pdf.py` | **PASS** | Nativni PDF ima 299 A4 stranica, 7.045.244 B i 536.983 tekstualno ekstrahirana znaka; metapodatci, kazalo, poglavlja i reprezentativni rasteri prolaze. |
| `python tools/audit_jupyterlite.py _site/jlite` | **PASS**, 17 notebookova | Završni JupyterLite paket i Pyodide runtime strukturno su potpuni; preglednički kernel doseže stanje `Idle`. |
| `npm run audit:viewports -- _site` | **PASS**, 72 prikaza + A4 | Provjerene su širine 320, 768 i 1.440 px, WCAG pravila, tipkovnica, overflow i zasebni A4 prikaz. |

### Struktura numeričkih provjera

| Kategorija | Broj | Status |
|---|---:|---|
| Usporedbe s unaprijed zadanim ciljem | 924 | prolazi |
| Invarijantne, dimenzijske i granične provjere | 77 | prolazi |
| Ukupno | 1.001 | prolazi |
| Self-comparison usporedbe | 0 | nije dopušteno manifestom v2 |
| Rupe ili zadatci bez provjere | 0 | nije dopušteno manifestom v2 |

Usporedba s ciljem provjerava izračun prema unaprijed deklariranoj vrijednosti i
toleranciji. Invarijantna provjera ne ponavlja isti broj, nego provjerava
dimenziju, bilancu, predznak, monotonost, granični slučaj ili red veličine.
Manifest v2 čuva autoritativni tekst zadatka, strukturirane ulaze s jedinicama,
pretpostavke, objavljene rezultate, tolerancije, neovisne provjere i
pripadajuće verifier ID-jeve; svih 90 javnih zadataka ima `golden` ugovor.

## Implementirani opseg v2

1. Puna jezgra MF1 s 15 poglavlja, 87 primjera, 90 zadataka i šest dodataka.
2. Tri uzdužna lajtmotiva i radni ritual
   `izmjeri → idealiziraj → izračunaj → numerički provjeri → procijeni valjanost`.
3. Kurikularna matrica s ukupno 145 sati rada uz udžbenik.
4. Autorski ugovor za semantičke blokove, stabilne ID-jeve, manifest v2,
   notebookove i SVG.
5. Hrvatska Quarto lokalizacija te zajednički izvor za HTML i nativni Typst PDF.
6. Sedamnaest izvršivih notebookova i JupyterLite/Colab poveznice.
7. Tri CFD podatkovna paketa s provenijencom i strojnom validacijom strukture:
   dva spremna nastavna slučaja i jedan ograničeni referentni paket.
8. Reproducibilni numerički QA bez tautoloških usporedbi i deklariranih rupa.
9. Javni tok za prijavu i praćenje errate.
10. Sekvencijski izgrađeni i auditirani HTML, nativni PDF i JupyterLite te
    završni viewport/WCAG pregled.

## Tehnički kriteriji za 1.0-rc1

Svi tehnički kriteriji su **zatvoreni**: aktualni commit ima sekvencijski
izgrađene HTML/PDF/JupyterLite artefakte, audit javnih sučelja i pregledničkog
kernela te završni viewport/WCAG i A4 pregled. Stanje je zato tehnički spremno
za `1.0-rc1`. Ovaj zapis ne stvara Git oznaku, ne pokreće javni deploy i ne
pretvara kandidata u `v1.0`.

## Neizvršeni ljudski kriteriji za v1.0

Sljedeća tri kriterija **nisu provedena** i ne mogu se označiti dovršenima samo
promjenom repozitorija:

- neovisnu stručnu provjeru potpisuje najmanje jedan nastavnik mehanike fluida;
- odvojenu primjensku provjeru potpisuje recenzent iz strojarstva ili
  brodogradnje;
- pilot s 8–12 stvarnih studenata provjerava izbor modela i pretpostavki prije
  algebre, uz cilj najmanje 80 % točnih izbora.

Nalazi se evidentiraju po stabilnim ID-jevima, ispravljaju i ponovno
provjeravaju prije oznake `v1.0`.

Postupci i obrasci nalaze se u
[protokolu stručne recenzije](docs/protokol_strucne_recenzije.md) i
[protokolu studentskog pilota](docs/protokol_studentskog_pilota.md).

## Javni trag ispravaka

Pogreške se prijavljuju kroz
[GitHub obrazac](https://github.com/martibasic/MF1_udzbenik/issues/new?template=errata.yml).
Potvrđeni zapisi ulaze u [javnu erratu](docs/errata.md), a promjene jednadžbi,
brojčanih odgovora i područja valjanosti bilježe se u
[dnevniku promjena](CHANGELOG.md).
