# Arhitekturni audit prije refaktora

Datum: 23. rujna 2026. Opseg: cijeli lokalni projekt i izlazi web/PDF/print.
Referentna javna adresa: https://martibasic.github.io/MF1_udzbenik/.
Lokalno izdanje uključuje još neobjavljene ispravke i sustav tiskovnih figura;
ono je polazište refaktora. Prije izmjena spremljena je lokalna snimka datoteka,
kontrolni hashovi i PDF u `tools/tmp/architecture-refactor/`.

## Zatečeno stanje

- `source/` već jest jedini izvor teksta 15 poglavlja, uvoda i šest dodataka.
  `.qmd` omotači određuju javne URL-ove. Njih treba očuvati.
- `_quarto.yml` opisuje website, a `_quarto-pdf.yml` zasebno opisuje knjigu.
  Redoslijed se dodatno ponavlja u početnoj stranici, pregledu za ispis,
  generatoru verifikacijskog manifesta, normalizatoru referencija i auditima.
  Time promjena redoslijeda traži više ručnih izmjena.
- PDF koristi izvorno Quarto/Typst numeriranje po poglavljima i dodatke A–F.
  Website nema zajednički kontekst knjige za sva numeriranja i reference.
- Jednadžbe i figure uglavnom već imaju stabilne ID-jeve i Quarto sintaksu.
  Primjeri imaju stabilne `ex-*` ID-jeve, ali naslovi P1… i razine T1–T4
  zapisani su u HTML oznakama. Zadatci imaju `task-*` ID-jeve, naslove Z1–Z6
  i odvojene razine; njihovu didaktičku logiku treba zadržati.
- Autorski blokovi koriste zajedničke `.mf1-*` klase, ali njihov registar,
  boje i pretvorba značenja postoje odvojeno u CSS-u, JavaScriptu i Lua filteru.
  Koraci rješenja izgledaju kao headingovi premda ne pripadaju hijerarhiji TOC-a.
- `custom.css` miješa osnovne stilove, navigaciju, komponente, responzivnost
  i ispis; sadrži brojne `!important` deklaracije i iznimku vezanu uz ID jedne
  tablice. To treba zamijeniti komponentnim pravilom za široke tablice.
- Priprema i samoprovjera skrivaju se prezentacijskim kodom; pravilo vidljivosti
  treba biti deklarirani metapodatak komponente, uz očuvan postojeći sadržaj.
- Figure već imaju odvojene tiskovne izvedenice i tokene te provjeru najmanje
  9 pt. Taj sustav treba integrirati, ne zamijeniti novim crtežima.
- Interaktivni blokovi imaju notebook, poveznice i QR fallback za PDF.
  Njihovo ponašanje treba ostati zajedničko, bez iznimki po poglavljima.
- Postoje numerički, publikacijski, PDF, SVG, link i viewport auditi.
  Nedostaje zajednička provjera modela, semantičkih komponenti i promjene
  redoslijeda bez ručnog popravljanja brojeva.

## Odluka o arhitekturi

1. Kanonski Markdown ostaje u `source/`. Model knjige određuje metapodatke,
   dijelove, redoslijed poglavlja, zasebne dodatke, URL-ove i tehničke veze.
2. Zajednički generator stvara Quarto konfiguraciju i omotače, navigaciju,
   početni katalog, pregled za ispis i indeks sadržajnih objekata.
3. Web i PDF koriste Quarto book strukturu; PDF profil sadrži samo pravila
   PDF prikaza. Brojevi proizlaze iz položaja, a ID-jevi ostaju stabilni.
4. Registar komponenti i Pandoc adapter daju isto značenje postojećoj sintaksi
   i novim komponentama. HTML i Typst imaju zasebne prikazivače tog modela.
5. Tokeni i slojevi stilova odvajaju osnovu, tipografiju, layout, komponente,
   pomoćna pravila, ispis i responzivnost. Nema pravila vezanih uz broj poglavlja.
6. Generirani indeks povezuje objekte, poglavlja i pojmovnik. Nije dodatni
   ručno održavani izvor formula, naslova ili captiona.
7. Automatske provjere obuhvaćaju integritet modela, sadržaj, stare poveznice,
   numeriranje, headingove, figure, matematiku, dostupnost i oba završna izlaza.

## Granice zahvata

Ne mijenjaju se fizikalna objašnjenja, formule, podatci, odgovori, skice,
raspodjela T1–T4 ni broj primjera i zadataka. Strukturne promjene izvora
dopuštene su samo za semantičke oznake i uklanjanje ručno dupliranih
metapodataka. Ne izmišlja se sadržaj za prazne dijelove predloška.
Postojeće prethodne izmjene ostaju sačuvane.
