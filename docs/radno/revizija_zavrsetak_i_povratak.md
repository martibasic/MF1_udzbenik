# Revizija završnih poglavlja i ponovni pregled temelja

Korisnikov cilj: redom urediti U12, U13, U14 i U15, zatim ponovno pregledati
i urediti U01 i U02 prema pravilima primijenjenima do U11. Polazište je
commit `0a4a0ac`; njegova GitHub objava potvrđena je kao uspješna.
Zahtjev obuhvaća uređivanje i provjeru. Naknadnim zahtjevima za commit i push
odobreno je spremanje trenutačnih izmjena i evidencija. Objavljivanje U12/U13
ne označava dovršenima preostale korake.

## Redoslijed i dokaz dovršenosti

| Korak | Kanonski izvor | Stvarni verifier | Status | Evidencija |
| --- | --- | --- | --- | --- |
| 1 | `source/u12_diferencijalni_opis_realnog_toka.md` | `verify_u12_real_flow.py` / U12.REAL | dovršeno; zajednički završni build slijedi | `revizija_u12.md` |
| 2 | `source/u13_gubici_cjevovodi_crpke_i_mreze.md` | `verify_u13_integrated.py` / U13.CANON | dovršeno; zajednički završni build slijedi | `revizija_u13.md` |
| 3 | `source/u14_turbostrojevi_i_propulzija.md` | `verify_u12.py` / U12 | dovršeno; zajednički završni build slijedi | `revizija_u14.md` |
| 4 | `source/u15_otvoreni_tokovi.md` | `verify_u15_open_channels.py` / U15 | slijedi | `revizija_u15.md` |
| 5 | `source/u01_osnove_fluida_i_pascalov_zakon.md` | `verify_u01.py` / U01 | slijedi nakon U15 | dopuna `revizija_u01.md` |
| 6 | `source/u02_viskoznost_povrsinska_napetost_i_kapilarnost.md` | `verify_u02.py` / U02 | slijedi nakon U01 | dopuna `revizija_u02.md` |

Za svaki korak potrebni su pregled svih postojećih P/Z i skica, matrica
odluka prije sadržajnih izmjena, selektivna dorada zadataka, fizikalni i
matematički pregled SVG-ova, usklađeni odgovori/notebook/verifier/D03/D06,
očuvani ID-jevi te provjera stvarnog HTML-a i PDF-a. Zadržavaju se 6 vježbi
T1/T1/T2/T2/T3/T4 i postojeći broj riješenih primjera; kvalitetan zadatak
ne zamjenjuje se samo radi promjene. Poglavlja 1 i 2 dobit će novu provjeru,
ne samo oslanjanje na stare zapisnike.

## Završna provjera cilja

Cilj se smatra dovršenim tek kada svih šest redaka ima zabilježene provedene
izmjene ili obrazložene odluke o zadržavanju i rezultate odgovarajućih
provjera. Konačni zajednički HTML/PDF, D06 i JupyterLite moraju sadržavati
sve završne izmjene; provjere strukture, numerike, notebookova, geometrije,
poveznica i prikaza obuhvaćaju završno stanje cijele knjige. Djelomično
dovršeno poglavlje ne znači dovršenost ovog cilja.

## Provjera objave U12/U13 — 22. rujna 2026.

Prije novoga commita i pusha provedena je provjera cijeloga trenutačnog
izdanja prema koracima `publish.yml`:

- numerika i manifest: 1257 rezultata, od toga 1062 golden i 195 invarijanti,
  uz 22 dodatne fizikalne provjere i 90/90 ugovora zadataka; PASS;
- struktura, Typst, normalizacija, generirani QR i D06 te CFD podatci: PASS;
- svih 17 notebookova izvršeno od početka u čistim kernelima: PASS;
- cijeli HTML (24 stranice) i nativni PDF (315 A4 stranica) obnovljeni;
  PDF audit: PASS; aktualni PDF kopiran je u direktorij za preuzimanje;
- JupyterLite obnovljen s aktualnim notebookovima, audit 17 notebookova
  i četiri ekstenzije: PASS;
- audit renderirane stranice: 220 slika, 1930 poveznica i 446 sklopivih
  blokova; PASS;
- preglednik: 72 prikaza na 320/768/1440 px, A4 ispis, WCAG i pokretanje
  Pythona u JupyterLiteu do stanja Idle: PASS.

Ovo je provjera objave trenutačnih izmjena U12/U13. Završna provjera cijeloga
cilja ponovit će se nakon preostalih revizija U14, U15, U01 i U02.

## Provjera objave U14 — 22. rujna 2026.

Naknadni zahtjev za commit i push obuhvaća izmjene U14. Dovršeni su
zadaci i sedam skica, povezani notebook, D03, D06 i numerički manifest.
Provjere stvarne SVG geometrije, 1296 numeričkih rezultata, strukture,
izmijenjenog notebooka, HTML-a U14 u tri širine, povratnih poveznica D06,
nativnog PDF-a i obnovljenog JupyterLitea prolaze. Detalji i granice provjere
navedeni su u `revizija_u14.md`. Prethodna objava U12/U13, GitHub Actions
run `35775620655`, završila je uspješno.

Sljedeći korak ostaje U15, zatim ponovni pregled U01 i U02. Ovaj commit
ne označava dovršenim cijeli korisnikov cilj.
