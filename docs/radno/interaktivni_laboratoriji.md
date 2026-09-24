# Interaktivni laboratoriji i objavna provjera — 24. rujna 2026.

## Opseg

Tri pilot-bilježnice: U04 rotirajući spremnik, U08 Venturijeva cijev i U12
Poiseuilleovo strujanje. Ostali notebookovi i P/Z sadržaj ostaju isti.
U kanonskim poglavljima usklađeni su opisi tih triju interaktivnih blokova.

Kontrole istodobno obnavljaju skicu, grafove, rezultate i dijagnostiku.
Dostupni su početni slučajevi, usporedba sa spremljenim slučajem A, vraćanje
početnoga stanja te kartice Istraži / Provjeri / Pogledaj kod. Izvor stvarnih
računskih funkcija dostupan je studentu. Neispravni ulazi uklanjaju stari
rezultat. Bilježnice zadržavaju sve prethodne numeričke pokuse i provjere.

## Fizikalne razlike

- U04: zasebno se računaju dodir dna i prelijevanje; profil s očuvanim
  početnim volumenom vrijedi samo do prvog događaja. Nakon granice nije
  nacrtana izmišljena raspodjela fluida. Provjera volumena je neovisna
  numerička integracija prikazanoga profila.
- U08: prikazana su dva presjeka, njihove brzine, protok i doprinosi
  nesigurnosti D2, razlike tlaka i koeficijenta protoka. U ovoj lokalnoj
  linearizaciji ostali ulazi smatraju se točnima; stari Monte Carlo pokus
  s više nesigurnih ulaza ostaje ispod. Nema izmišljenoga polja tlaka ili
  tvrdnje da koeficijent protoka određuje trajni ukupni gubitak.
- U12: prstenasti konačni volumeni diskretiziraju bilancu gibanja i daju
  tridiagonalni sustav za nepoznate brzine. Analitički profil nije ulaz
  numeričkog rješenja. Prikaz razlikuje algebarski rezidual, pogrešku
  protoka, konvergenciju mreže, globalnu bilancu sila i granicu laminarnog
  modela. Izvorna kvadratura i zasebni sintetički tro-mrežni podatci
  nisu predstavljeni kao rezultati novog solvera.

## Izvedba i ograničenja

Četiri označene ćelije odvajaju učitavanje widgeta, račun, zajedničko sučelje
te prikaz konkretnog laboratorija. Zajednički dio uključen je u svaku
bilježnicu radi samostalnog otvaranja; test provjerava njihovu jednakost.
U Pyodideu se ipywidgets 8.1.8 učitava početnom ćelijom. Prvo pokretanje
zahtijeva mrežni pristup. Na uskom zaslonu zatvara se standardni bočni
popis datoteka JupyterLaba; uputa je u bilježnici.

Automatske provjere potvrđuju izvršivost i navedene numeričke odnose.
Nisu dokaz didaktičke kvalitete niti puna validacija modela prema pokusu.
Google Colab nije zasebno ručno pokrenut u ovoj reviziji. Studentski pilot
ostaje sljedeći izvor povratnih informacija.

## Povezani popravci

Verzionirani pre-push hook i GitHub Action koriste isti puni objavni runner.
Detalji, uzrok prethodnoga pada i lokalne verzije alata nalaze se u
[protokolu lokalnog CI-ja](../lokalni-ci.md). Lokalni Quarto 1.9.37 smješten
je u putanju bez skrivenog direktorija: Windowsova inačica pri izradi
naslovnice pogrešno je obradila separator ispred `.tools-ci`.

Web formule više nisu sve zasebni scroll-okviri. Kratke formule slijede
osnovnu crtu teksta, a samo formule šire od svojega odlomka dobivaju
imenovano područje dostupno tipkovnicom. Mjerenje se ponavlja nakon
učitavanja MathJaxa/fontova i promjene raspoložive širine. Sadržaj formula
nije izmijenjen. Izvorni i zamjenski font provjeravaju se i pri auditu
izreza tiskovnih skica.

## Izvršene provjere

Puni `python scripts/check_publication.py` prošao je 24. rujna 2026. za
672 s. Lokalni log: `tools/tmp/local-ci.log`. Okruženje: Python 3.12.14,
Node.js 22.23.3, Quarto 1.9.37 i sve pinane Python ovisnosti; PyMuPDF 1.28.0.

- Numerički ugovor: 90/90 zadataka, 1340 rezultata provjera, bez deklariranih rupa.
- Svih 17 bilježnica izvršeno u čistim lokalnim kernelima.
- 12 testova modela i kontrola laboratorija te 6 testova stvarnoga pre-push hooka.
- Tri stvarne Pyodide bilježnice: promjena kontrola tipkovnicom, fizikalni
  odziv, usporedba A, reset, dijagnostika, kod te devet prikaza na 320/768/1280 px.
- 94 kanonska SVG-a, 256 izreza i 3363 tekstualna elementa; 94 tiskovne figure,
  149 redaka, 3338 nepromijenjenih oznaka i 3989 geometrijskih elemenata.
- PDF od 327 A4 stranica; provjereni sadržaj, metapodatci, razmaci,
  17 QR kodova, bibliografija i najmanje 9 pt za oznake figura.
- Renderirani web: 24 stranice, 222 slike i 2468 poveznica; model provjerava
  2134 numerirana objekta u webu i pregledničkom ispisu.
- Viewport/WCAG: 72 prikaza na 320/768/1440 px, A4 ispis i JupyterLite kernel.
  Provjeravaju se i nepotrebni klizači kratkih formula, tipkovničko pomicanje
  duge formule te uklanjanje toga područja nakon povećanja širine zaslona.

Ručno su pregledani snimci laboratorija, formula Δp = 4σ/d u stvarnom
odlomku U02 i konačna stranica 59 PDF-a s oznakom 0,55 m. U U02 na desktopu
svih 260 formula unutar teksta ima prikaz bez scroll-područja.

Obnovljeni su `_site/`, `_book/mehanika-fluida-1.pdf` i kopija PDF-a za
preuzimanje. Lokalni web ostavljen je na `http://localhost:8766/`; početna
stranica i PDF potvrđeni su odgovorom HTTP 200. Gitov hook aktiviran je u
ovom klonu. Ovaj presjek ne uključuje novi commit, push ni novi udaljeni Action.
