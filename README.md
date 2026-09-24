# Mehanika fluida 1

Otvoreni radni repozitorij sveučilišnog udžbenika za temeljni kolegij mehanike
fluida. Primarna su publika studenti strojarstva i brodogradnje, uz primjere iz
građevinarstva, energetike, okolišnog, biomedicinskog i procesnog inženjerstva
kada osvjetljavaju isti fizikalni model.

Aktualna grana sadrži arhitekturu **MF1 v2** s poglavljima U01–U15. Sadržajna i
automatizirana znanstvena revizija provedene su, a sekvencijski proizvodni
build i tehnički QA potvrđuju da je stanje **tehnički spremno za `1.0-rc1`**.
To nije oznaka `v1.0` ni potvrda javnoga deploya: zasebna stručna recenzija
nastavnika mehanike fluida, primjenska recenzija iz strojarstva ili
brodogradnje te studentski pilot ostaju obvezni izlazni kriteriji. Mjerodavan
presjek nalazi se u
[statusu izrade](status_izrade_udzbenika.md).

## Sadržaj v2

Aktualni dijelovi, poglavlja i dodaci definirani su u
[modelu knjige](content/book.json). Njihov se popis automatski prikazuje u
navigaciji, početnom katalogu i [kartiranju izvora](docs/kanonska-struktura-sadrzaja.md).

Kanonski rukopis trenutačno obuhvaća **15 poglavlja, 87 riješenih primjera, 90
samostalnih zadataka, šest dodataka, 17 notebookova, 1.216 stabilnih ID-jeva,
795 prikazanih jednadžbi i 145 sati** planiranoga rada uz udžbenik. Tih 145
sati nije cijelo ECTS opterećenje kolegija. Ishodi, preduvjeti i raspodjela rada
definirani su u
[kurikularnoj matrici](docs/kurikularna_matrica.md).

## Struktura repozitorija

- `content/book.json` je jedini model hijerarhije, naslova i javnih putanja.
- `source/` je jedini kanonski izvor teksta poglavlja i dodataka.
- `chapters/` sadrži generirane Quarto omotače i preusmjerenja starih javnih URL-ova;
  generirani HTML u toj mapi ne uređuje se ručno.
- `components/`, `design-system/`, `styles/` i `web/` odvajaju semantiku,
  globalne tokene i prikaz. Model, predlošci i postupak proširenja opisani su u
  [arhitekturi digitalnog udžbenika](docs/arhitektura.md).
- `assets/print/` sadrži statičke SVG skice, a `assets/qr/` QR kodove.
- `notebooks/` sadrži 17 nastavnih notebooka.
- `data/cfd/` sadrži tri mala V&V podatkovna paketa: dva su spremna nastavna
  slučaja, a jedan je pošteno ograničen referentni paket.
- `tools/` sadrži verifikatore, manifest zadataka sheme v2 i read-only QA
  provjere.
- `docs/` sadrži autorska pravila, kurikularnu matricu i javnu erratu; radna
  arhiva u `docs/radno/` nije dio studentskog izdanja.

Stabilne semantičke ID-jeve, ugovor zadatka, notebooka i slike opisuje
[autorski ugovor](docs/autorski_ugovor.md). Vizualna pravila nalaze se u
[protokolu prerade](protokol_prerade_zadataka_i_skica.md) i
[sažetku SVG pravila](pravila_svg.md).

Vanjski kriteriji za izdanje `v1.0` imaju zasebne, ponovljive protokole:
[stručnu recenziju](docs/protokol_strucne_recenzije.md) i
[studentski pilot](docs/protokol_studentskog_pilota.md). Ti dokumenti ne tvrde
da su recenzija ili pilot provedeni; određuju uzorak, evidenciju i prag prolaza.

## Izgradnja

Potrebni su Quarto 1.9.37, Python 3.12, Node.js 22 i Chrome/Chromium/Edge.
Lokalna izgradnja, pre-push hook i GitHub Action koriste isti puni runner.

```powershell
py -3.12 -m venv .venv-ci
.venv-ci/Scripts/python.exe -m pip install -r requirements.txt
python scripts/install_hooks.py
./scripts/izgradi.ps1
```

Hook prije svakog pusha provjerava čist HEAD i izvršava cijeli objavni CI.
Neuspjeh zaustavlja push. Priprema drugih sustava i granice lokalne provjere
opisane su u [uputama za lokalni CI](docs/lokalni-ci.md).
Izvore po potrebi najprije obnovi s `python scripts/build_book.py --write`;
objavna provjera ne popravlja zastarjele izvedenice.
Skripta namjerno izvodi Quarto rendere redom u izoliranoj radnoj mapi.
Izlazi su:

- `_site/` — HTML izdanje;
- `_book/mehanika-fluida-1.pdf` — nativni A4 PDF iz Typsta;
- `_site/jlite/` — JupyterLite s notebookovima koji se izvode u pregledniku.

U nativnom PDF-u autorski su blokovi stilizirani izravno u Typstu. Odlomci
nemaju uvlaku prvoga retka; razmak i tipografiju određuju globalni tokeni.

Pojedinačne naredbe za razvoj:

```powershell
python tools/verify_all.py
python tools/execute_notebooks.py --validate-only
python tools/validate_cfd_vv.py
python scripts/build_book.py --write
python tools/audit_architecture.py
python scripts/build_book.py --render all
python -m jupyterlite_core.app build --config=jupyter_lite_config.py --contents notebooks --output-dir _site/jlite
```

`verify_all.py` već uključuje audit neovisnosti verifikatora (`qa_audit.py`) i
fizikalne regresije (`verify_physics.py`). Te se provjere u punoj izgradnji
izvršavaju jednom; zasebne skripte ostaju dostupne za ciljanu dijagnostiku.
Opcija `--to typst` ograničava PDF korak na taj format jer profil inače
nasljeđuje i HTML format mrežnog izdanja.

GitHub Pages workflow izvršava numerički QA i notebookove, gradi HTML, nativni
PDF i JupyterLite te provjerava javne artefakte. Isti build radi i na pull
requestovima, ali je deploy ograničen na non-PR događaje. Potvrđeni lokalni RC
rezultati i preostali ljudski kriteriji vode se u
[statusu](status_izrade_udzbenika.md); sam tehnički prolaz nije odobrenje javne
objave.

## Kako se čita QA izvještaj

Aktualni `verify_all.py` obuhvaća svih 15 poglavlja kroz 19 modula i izvještava
**1.340 stvarnih provjera: 1.119 usporedbi s unaprijed zadanim ciljem i 221
invarijantnih, dimenzijskih ili graničnih provjera**. Manifest sheme v2 ima
90/90 zadataka u skupini `golden`, 393 parsirana skalarna ulaza i 312 ugovora
rezultata. Ne dopušta tautološku usporedbu rezultata sa samim sobom ni zadatak
bez deklarirane provjere; aktualni presjek ima **0 self-comparison zapisa i 0
rupa**. Odvojeni paket kritičnih fizikalnih regresija prolazi **22/22** provjere.

Proizvodni QA izvršava notebookove i provjerava slike, poveznice,
preusmjerenja, PDF te prikaz na širinama 320, 768 i 1.440 px. Rezultate čitaj
iz izlaza posljednje izgradnje; arhivski presjek nalazi se u
[statusu izrade](status_izrade_udzbenika.md).

Automatizirane provjere ne ocjenjuju jasnoću objašnjenja niti mogu otkriti
svaku pogrešku u pretpostavkama ili prijelomu. Uz njih treba pregledati
izmijenjene stranice i provesti stručnu recenziju te studentski pilot.

## Autorski rad i doprinosi

1. Tekst se mijenja u `source/`, ne u generiranom HTML-u ili PDF-u.
2. Novi primjer, zadatak, jednadžba i slika dobivaju semantički ID koji ne ovisi
   o broju poglavlja.
3. Brojčana izmjena istodobno obuhvaća tekst, odgovor, skicu, notebook i
   verifikator.
4. Svaki model navodi pretpostavke, predznake, referentni tlak, područje
   valjanosti i barem jednu neovisnu provjeru.
5. Prije predaje pokreću se relevantni verifikatori i oba izlazna formata.

## Prijava pogreške

Pogrešku u jednadžbi, rezultatu, zadatku, slici, poveznici ili pristupačnosti
prijavite kroz [obrazac za erratu](https://github.com/martibasic/MF1_udzbenik/issues/new?template=errata.yml).
U prijavi navedite stabilni ID sadržaja i inačicu izdanja. Potvrđene ispravke
objavljuju se u [javnoj evidenciji errate](docs/errata.md) i
[dnevniku promjena](CHANGELOG.md).

Autorica: Martina Bašić. U mrežnom izdanju navedena je licenca
[CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.hr).
