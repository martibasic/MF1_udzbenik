# Dorada sveučilišnog priručnika — 27. rujna 2026.

## Provedeni opseg

Prema odobrenom opsegu provedene su prve četiri točke uredničkog pregleda:
vidljiva konceptualna pitanja, povezani pojmovnik, aktualni središnji status
i eksperimentalna CFD usporedba. Stručna recenzija i studentski pilot ostaju
budući koraci; priručnik još nije poslan na recenziju.

- U svakom od 15 poglavlja izdvojeno je jedno postojeće pitanje „Zastani i
  promisli”, prije pripadajućeg tumačenja. Usporedba s polaznom snimkom potvrđuje
  da pitanja potječu iz postojećeg materijala; skriveni skupovi samoprovjere
  zadržavaju ugovorenu vidljivost.
- U pojmovniku je 121 upućivanje zamijenjeno poveznicom. Definicije su sačuvane;
  zadnji stupac „Odredište” i uvod tumače brojeve poglavlja i slova dodataka.
  Dodatno je ispravljeno 105 PDF veza koje su pokušavale otvoriti izvornu
  `.qmd` datoteku, među njima osam novih upućivanja iz pojmovnika u dodatak D.
  PDF sada koristi postojeća unutarnja sidra iz kanonskog indeksa; zasebna
  regresija pokriva sva 22 dokumenta, fragmente i očuvanje vanjskih veza.
- `status_izrade_udzbenika.md`, `README.md`, `tools/README.md` i `CHANGELOG.md`
  usklađeni su s aktualnim inventarom. Datirani stariji izvještaji ostaju
  povijesni trag, a ne paralelni aktualni status.
- Dodan je P6 u U12, `ex-stepenica-mjerenje-cfd`, kao kratak račun na stvarnim
  mjernim i objavljenim CFD podatcima. Knjiga ima 88 primjera i 90 zadataka.
- Naslov je usklađen s traženim podnaslovom koji uključuje strojarstvo, a
  vidljivi naziv djela glasi sveučilišni priručnik. Ažuriran je i `CITATION.cff`.
  Stari tehnički nazivi datoteka, URL-ovi i sidra čuvaju postojeće poveznice.
  Auditi stvarnog PDF-a i HTML-a trajno provjeravaju naziv publikacije.

## Stvarni pokus i granice zaključka

Driverov i Seegmillerov pokus iza stepenice pri `Re_H ≈ 36000` povezan je s
objavljenim CFL3D/SSTm podatcima iz Turbulence Modeling Resourcea. Arhivirani
su cijeli mjerni i CFD nizovi te mjereni profili; četiri odabrana retka
preuzeta su izravno iz tablica, bez digitiziranja grafova. URL-ovi, normalizirani
hashovi i uvjeti nalaze se u
[podatkovnom paketu](../../data/cfd/backstep_experiment/README.md).

Interpolacija daje `x/H ≈ 6,279` za mjerne retke i `6,543` za CFD. Objavljena
mjerna procjena jest `6,26 ± 0,10`. CFD odstupa približno `+0,283 H`, odnosno
`+4,5 %`. Navedeni raspon nije proglašen standardnom nesigurnošću ni intervalom
s poznatom razinom pouzdanosti. Nema potpune studije mrežne konvergencije toga
CFD prikaza; jedan položaj priljubljivanja ne potvrđuje cijeli tok.

Ponovljen pregled NACA arhive nije pronašao nove datoteke u relevantnim
mapama. `source_review.json` čuva pregledani Git objekt, izvore i granice.
Arhivske praznine vode se kao dokumentirano ograničenje, bez čekanja podataka
od korisnika. Novi pokus ne nadomješta stare povijesti reziduala ili mjerni
budžet NACA profila. Nastavne pretpostavke postojećeg Z6 ostaju označene.

## Provjere i očuvani sadržaj

- Polazna snimka: commit `8e05312`; lokalni dokaz usporedbe je
  `tools/tmp/prirucnik-dorada-20260927/preservation.json`.
- Očuvano je 796 ranijih izdvojenih jednadžbi, svih 90 punih ugovora zadataka,
  1066 postojećih ID-jeva indeksiranih objekata i sve definicije pojmovnika.
  Dodani su jedan primjer i jedna jednadžba; ukupno je 797 jednadžbi.
- Prvih 20 ćelija bilježnice U12 ostalo je nepromijenjeno; tri nove ćelije
  obrađuju pokus. AST provjera uspoređuje ugrađene retke s podatkovnim paketom.
- Numerički QA: 1345 provjera (1123 ciljne i 222 invarijantne), dodatne
  fizikalne regresije 22/22, 90/90 ugovora zadataka, bez deklariranih rupa.
- Sedam novih regresija čuva arhivske podatke, uvjete, nesigurnost i
  podudarnost bilježnice. Postojeće provjere nisu oslabljene.
- Završni puni objavni CI prošao je za 838 s: arhitektura, slike,
  bilježnice, izgradnja svih izdanja, PDF, JupyterLite, tri interaktivna
  laboratorija, 72 prikaza i A4 pristupačnost.
- PDF ima 318 stranica. Kontaktni pregled obuhvatio je 35 odabranih
  stranica, uz povećani pregled naslovnice, novog primjera i tablica.
  Pregled weba ima deset snimaka radne površine, mobilnog prikaza i pomaknutih
  tablica. Svih 15 pitanja je vidljivo; upućivanja u pojmovniku razriješena su
  i u webu i u PDF-u. Lokalni izvještaji su u podmapama `pdf/` i `web/` iste
  ignorirane radne mape.

PDF i mrežno preuzimanje imaju SHA-256
`7a11b4bd9effebcd2dd9fd667837d54443ed9019b1066e3cb15b59217c2b50a4`. Lokalni pregled na <http://127.0.0.1:8766/> ostavljen je dostupan.

Ovo je autorska i tehnička dorada. Ne predstavlja neovisnu stručnu recenziju,
studentski pilot ili potpunu validaciju CFD modela.
