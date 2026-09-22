# Revizija završnih poglavlja i ponovni pregled temelja

Korisnikov cilj: redom urediti U12, U13, U14 i U15, zatim ponovno pregledati
i urediti U01 i U02 prema pravilima primijenjenima do U11. Polazište je
commit `0a4a0ac`; njegova GitHub objava potvrđena je kao uspješna.
Zahtjev obuhvaća uređivanje i provjeru. Naknadnim zahtjevom za commit i push
odobreno je spremanje trenutačnih radnih evidencija; time se revizija U12
ni preostali koraci ne označavaju dovršenima.

## Redoslijed i dokaz dovršenosti

| Korak | Kanonski izvor | Stvarni verifier | Status | Evidencija |
| --- | --- | --- | --- | --- |
| 1 | `source/u12_diferencijalni_opis_realnog_toka.md` | `verify_u12_real_flow.py` / U12.REAL | u tijeku | `revizija_u12.md` |
| 2 | `source/u13_gubici_cjevovodi_crpke_i_mreze.md` | `verify_u13_integrated.py` / U13.CANON | slijedi | `revizija_u13.md` |
| 3 | `source/u14_turbostrojevi_i_propulzija.md` | `verify_u12.py` / U12 | slijedi | `revizija_u14.md` |
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
