# Projektne upute za MF1_udzbenik

Ove upute vrijede za rad u cijelom repozitoriju, uključujući analizu i prijedloge
u razgovoru. Izričite korisnikove upute imaju prednost; već dano odobrenje za
provedbu vrijedi i dalje. Pravila nisu razlog za ponovno traženje odobrenja
za već dogovoreni posao.

## Prije analize ili zamjene zadataka i primjera

Pročitaj aktualne dokumente, ne oslanjaj se samo na prethodni razgovor:

- [Autorski ugovor](docs/autorski_ugovor.md)
- [Kurikularna matrica](docs/kurikularna_matrica.md)
- [Kanonski izvori i omotači](docs/kanonska-struktura-sadrzaja.md)
- [Protokol prerade zadataka i skica](protokol_prerade_zadataka_i_skica.md),
  osobito odjeljak „Sustavna didaktička revizija bez promjene strukture”.

Prije provedbe pročitaj i [upute za alate](tools/README.md), odgovarajući
verifikator i aktualni [.github/workflows/publish.yml](.github/workflows/publish.yml).
Za skice primijeni SVG standard iz protokola. Evidencije starih migracija u
`docs/radno/` služe za provenijenciju, a ne kao novi popis obveznog uvoza.

## Trajna pravila rada

- Prije svakog pusha obvezno izvrši puni lokalni objavni CI iz
  `scripts/check_publication.py` nad upravo onim commitom koji se šalje.
  Aktiviraj verzionirani `.githooks/pre-push` s `python scripts/install_hooks.py`.
  Ne zaobilazi hook, ne koristi `--no-verify` i ne smatraj djelomične provjere
  ili stari prolaz zamjenom za aktualni puni prolaz. Ako provjera padne,
  popravi uzrok i ponovi je prije pusha. Lokalni CI i GitHub Action moraju
  koristiti isti runner i verzije alata prema `docs/lokalni-ci.md`.

- Uz svako osvježavanje PDF-a obnovi i generirani web, pokreni ili osvježi
  njegov pregled na localhostu te korisniku daj provjerenu lokalnu adresu.
  Poslužuj izlaz `_site/` i ostavi lokalni pregled dostupan nakon završetka rada.

- Arhitekturu cijele knjige određuju `content/book.json`, kanonski `source/`,
  `components/registry.json` i globalni `design-system/tokens.json`.
  Prije strukturne izmjene pročitaj [arhitekturu](docs/arhitektura.md).
  Omotače, Quarto konfiguracije, katalog, indeks objekata i ključ rezultata
  generiraj s `python scripts/build_book.py --write`; ne uređuj izvedenice.
  P/Z brojeve ne upisuj u naslove izvora: prikaz ih izvodi iz redoslijeda.
  Za provjeru koristi `tools/audit_architecture.py`, `tools/test_book_model.py`
  i nakon rendera `tools/audit_rendered_model.py`.
  Puni render pokreći kroz `scripts/build_book.py --render web|pdf|all`:
  automatski koristi izoliranu radnu mapu i čuva previewovu predmemoriju.
  Vidljivost uređuj samo u registru komponenti (`web`, `pdf`, `print`);
  ne dodaj zasebne popise skrivenih klasa u adaptere. Regresije su u
  `tools/test_render_workspace.py` i `tools/test_component_visibility.py`.

- U dogovorenom ciklusu revizije mijenjaj samo samostalne zadatke za vježbu
  Z1–Z6 koji trebaju zamjenu; kvalitetne zadrži. Riješene primjere P1–P6 i teoriju
  koristi za usporedbu ponavljanja, a mijenjaj ih tek ako korisnik proširi opseg.
- Radi jedno dogovoreno poglavlje po jedno. Analiza obuhvaća i riješene primjere
  i samostalne zadatke iz stvarnog `source/` izvora, ne samo `.qmd` omotač.
- Prvo utvrdi ponavljanja zakona, matematičkog postupka i studentskih odluka;
  tek potom predloži zamjene. Drugi uređaj ili drugi brojevi nisu dokaz raznolikosti.
- Čuvaj jednostavne računske zadatke. Novi zadatci trebaju mijenjati vrstu
  razmišljanja, a ne svi postati teški ili opširni. Slijedi ishode i preduvjete.
- Zadrži šest mjesta Z1–Z6 po poglavlju: 2×T1, 2×T2, T3, T4; 5–7 riješenih
  primjera po poglavlju i 80–90 u knjizi. To vrijedi i za preporučeni završni
  raspored u analizi. Ne uklanjaj jedini T4 niti dodaj Z7 radi zaobilaženja ugovora.
- Razinu odredi prema stvarnim odlukama studenta. Ne povisuj oznaku samo radi
  kvote. Skup od 8–12 ideja jest banka alternativa, ne automatsko proširenje knjige.
- Zahtjev za pregled ili prijedlog ne znači izmjenu udžbenika. Kad je provedba
  zatražena ili već odobrena, dovrši povezane izmjene i provjere bez novog
  potvrđivanja svakog koraka. Ne širi posao na druga poglavlja bez razloga iz zadatka.
- Tekst, odgovor, skica, povezani notebook i verifikator moraju opisivati isti
  problem i podatke. Regeneracija manifesta sama ne dokazuje tu podudarnost.
- Pri prilagodbi skica zadrži postojeći vizualni stil udžbenika (raspored panela,
  paletu, šrafure, gradijente i tipografiju). Zamjena zadatka sama po sebi ne znači
  odobrenje za vizualni redizajn; prilagodi prizor i oznake novom sadržaju.
- Za PDF i ispis primijeni [sustav tiskovnih figura](docs/ispis-skica.md).
  Izvedenice generiraj iz kanonskih SVG-ova; ne mijenjaj mrežne skice radi
  tiskovnog rasporeda. Čuvaj formate MINI/STANDARD/WIDE/COMPOSITE, najmanje
  9 pt za oznake te odvojeno skaliranje geometrije i tipografije. Nakon izmjene
  izvora, tokena ili kompozicije obnovi izvedenice i pregledaj konačni PDF.
- U skicama provjeri fizikalnu povezanost: krute stijenke ne smiju zatvarati
  predviđeni prolaz, otvor cijevi mora biti stvarno otvoren i prikladno uronjen,
  a fluid ne smije prolaziti kroz krutu plohu. Razlikuj brzine, sile i kote;
  navedi na koje tijelo sila djeluje. Profili brzine moraju odgovarati prianjanju
  uz stijenke, a crte profila ne smiju prolaziti kroz kruto tijelo kao kroz fluid.
- Ne pretpostavljaj da broj poglavlja odgovara imenu `verify_uNN.py`: provjeri
  `CANONICAL_CHAPTERS` u `tools/generate_verification_manifest.py`.
- Čuvaj stabilne ID-jeve postojećeg sadržaja; za novu fizikalnu cjelinu primijeni
  pravila novih semantičkih ID-jeva i provjeri stare poveznice. D06 i generirana
  polja manifesta obnavljaj generatorima, ne ručnim prepisivanjem.
- Ne oslabljuj audit da bi izmjena prošla. Ako dokument i kod nisu usklađeni,
  navedi razliku i učinak na objavu. Ako korisnik traži strukturnu promjenu,
  uskladi dokumentaciju, generatore i provjere kao zaseban jasno opisan zahvat.
- Ne proglašavaj didaktičku kvalitetu dokazanom samo zato što CI prolazi.
  U izvještaju razlikuj autorsku procjenu, izvršene provjere i preostala ograničenja.

Detaljan postupak, obrazac matrice zamjena i format didaktičke analize nalaze
se u protokolu. Za druge vrste posla primijeni samo relevantne dijelove ovih uputa.
