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

| Cjelina | Poglavlja |
|---|---|
| Temelji | U01 kontinuum, svojstva i tlak; U02 reologija, viskoznost i međupovršine |
| Statika fluida | U03 hidrostatika i manometrija; U04 relativno mirovanje; U05 sile na plohe; U06 uzgon i početni stabilitet |
| Integralna dinamika | U07 kinematika, RTT i kontinuitet; U08 energijska jednadžba; U09 kompresibilni idealni tok; U10 količina i moment količine gibanja |
| Sličnost i realni tok | U11 dimenzijska analiza; U12 diferencijalni opis realnog toka |
| Inženjerski sustavi | U13 cjevovodi, crpke i mreže; U14 turbostrojevi i propulzija; U15 otvoreni tokovi |
| Dodaci | D01 formule i oznake; D02 pojmovnik; D03 tipične pogreške; D04 numerička mehanika fluida; D05 literatura; D06 ključ kontrolnih rezultata |

Kanonski rukopis trenutačno obuhvaća **15 poglavlja, 87 riješenih primjera, 90
samostalnih zadataka, šest dodataka, 17 notebookova, 1.185 stabilnih ID-jeva,
789 prikazanih jednadžbi i 145 sati** planiranoga rada uz udžbenik. Tih 145
sati nije cijelo ECTS opterećenje kolegija. Ishodi, preduvjeti i raspodjela rada
definirani su u
[kurikularnoj matrici](docs/kurikularna_matrica.md).

## Struktura repozitorija

- `source/` je jedini kanonski izvor teksta poglavlja i dodataka.
- `chapters/` sadrži tanke Quarto omotače i preusmjerenja starih javnih URL-ova;
  generirani HTML u toj mapi ne uređuje se ručno.
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

Potrebni su Quarto s podrškom za Typst, Python 3.12 i Python paketi navedeni u
`requirements.txt`.

```powershell
python -m pip install -r requirements.txt
./scripts/izgradi.ps1
```

Skripta namjerno izvodi Quarto rendere redom jer dijele radnu predmemoriju.
Izlazi su:

- `_site/` — HTML izdanje;
- `_book/mehanika-fluida-1.pdf` — nativni A4 PDF iz Typsta;
- `_site/jlite/` — JupyterLite s notebookovima koji se izvode u pregledniku.

U nativnom PDF-u autorski su blokovi stilizirani izravno u Typstu. Odlomci
nemaju uvlaku prvoga retka, nego razmak od `0.72em` između odlomaka.

Pojedinačne naredbe za razvoj:

```powershell
python tools/verify_all.py
python tools/verify_physics.py
python tools/execute_notebooks.py --validate-only
python tools/validate_cfd_vv.py
quarto render
quarto render --profile pdf
python -m jupyterlite_core.app build --config=jupyter_lite_config.py --contents notebooks --output-dir _site/jlite
```

GitHub Pages workflow izvršava numerički QA i notebookove, gradi HTML, nativni
PDF i JupyterLite te provjerava javne artefakte. Isti build radi i na pull
requestovima, ali je deploy ograničen na non-PR događaje. Potvrđeni lokalni RC
rezultati i preostali ljudski kriteriji vode se u
[statusu](status_izrade_udzbenika.md); sam tehnički prolaz nije odobrenje javne
objave.

## Kako se čita QA izvještaj

Aktualni `verify_all.py` obuhvaća svih 15 poglavlja kroz 19 modula i izvještava
**1.001 stvarnu provjeru: 924 usporedbe s unaprijed zadanim ciljem i 77
invarijantnih, dimenzijskih ili graničnih provjera**. Manifest sheme v2 ima
90/90 zadataka u skupini `golden`, 393 parsirana skalarna ulaza i 312 ugovora
rezultata. Ne dopušta tautološku usporedbu rezultata sa samim sobom ni zadatak
bez deklarirane provjere; aktualni presjek ima **0 self-comparison zapisa i 0
rupa**. Odvojeni paket kritičnih fizikalnih regresija prolazi **22/22** provjere.

Sekvencijski proizvodni QA dodatno prolazi za 17/17 notebookova te za HTML:
24 stranice, 210 slika, 2.081 veza, 472 sklopiva bloka i 11 preusmjerenja. Uz to
prolazi audit nativnoga PDF-a od 299 A4 stranica, 7.045.244 B i 536.983
ekstrahirana znaka.
Viewport/WCAG audit prolazi 72 prikaza na širinama 320, 768 i 1.440 px te
zasebni A4 prikaz. Ti brojevi dokazuju strojno
provjerena svojstva trenutačnoga RC stanja, ali nisu zamjena za stručnu
recenziju cijeloga rukopisa ni studentski pilot.

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
