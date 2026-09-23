# Kanonska struktura sadržaja

<!-- Generirano iz content/book.json; ne uređivati ručno. -->

Hijerarhija, naslovi i putanje uređuju se u `content/book.json`, a tekst u
navedenom izvoru. Omotači nastaju iz zajedničkog predloška. Broj poglavlja
određuje položaj u modelu; stabilni ID i javna putanja ne mijenjaju se pri
premještanju. Pravila proširenja opisuje [arhitektura](arhitektura.md).

| Oznaka | Kanonski omotač | Izvor |
| --- | --- | --- |
| 0 | `chapters/u00_kako_koristiti_udzbenik.qmd` | `source/u00_kako_koristiti_udzbenik.md` |
| 1 | `chapters/u01_osnove_fluida_i_pascalov_zakon.qmd` | `source/u01_osnove_fluida_i_pascalov_zakon.md` |
| 2 | `chapters/u02_viskoznost_povrsinska_napetost_i_kapilarnost.qmd` | `source/u02_viskoznost_povrsinska_napetost_i_kapilarnost.md` |
| 3 | `chapters/u03_hidrostaticka_raspodjela_tlaka_i_manometrija.qmd` | `source/u03_hidrostaticka_raspodjela_tlaka_i_manometrija.md` |
| 4 | `chapters/u04_relativno_mirovanje_fluida.qmd` | `source/u04_relativno_mirovanje_fluida.md` |
| 5 | `chapters/u05_hidrostatske_sile_na_plohe.qmd` | `source/u05_hidrostatske_sile_na_plohe.md` |
| 6 | `chapters/u06_uzgon_plivanje_i_stabilnost.qmd` | `source/u06_uzgon_plivanje_i_stabilnost.md` |
| 7 | `chapters/u07_kinematika_kontrolni_volumen_i_kontinuitet.qmd` | `source/u07_kinematika_kontrolni_volumen_i_kontinuitet.md` |
| 8 | `chapters/u08_energijska_jednadzba_i_bernoulli.qmd` | `source/u08_energijska_jednadzba_i_bernoulli.md` |
| 9 | `chapters/u09_kompresibilni_idealni_tok.qmd` | `source/u09_kompresibilni_idealni_tok.md` |
| 10 | `chapters/u10_kolicina_i_moment_kolicine_gibanja.qmd` | `source/u10_kolicina_i_moment_kolicine_gibanja.md` |
| 11 | `chapters/u11_dimenzijska_analiza_i_slicnost.qmd` | `source/u11_dimenzijska_analiza_i_slicnost.md` |
| 12 | `chapters/u12_diferencijalni_opis_realnog_toka.qmd` | `source/u12_diferencijalni_opis_realnog_toka.md` |
| 13 | `chapters/u13_gubici_cjevovodi_crpke_i_mreze.qmd` | `source/u13_gubici_cjevovodi_crpke_i_mreze.md` |
| 14 | `chapters/u14_turbostrojevi_i_propulzija.qmd` | `source/u14_turbostrojevi_i_propulzija.md` |
| 15 | `chapters/u15_otvoreni_tokovi.qmd` | `source/u15_otvoreni_tokovi.md` |
| A | `chapters/d01_sazetak_formula_i_oznaka.qmd` | `source/d01_sazetak_formula_i_oznaka.md` |
| B | `chapters/d02_pojmovnik.qmd` | `source/d02_pojmovnik.md` |
| C | `chapters/d03_tipicne_pogreske_po_poglavljima.qmd` | `source/d03_tipicne_pogreske_po_poglavljima.md` |
| D | `chapters/d04_numericka_mehanika_fluida.qmd` | `source/d04_numericka_mehanika_fluida.md` |
| E | `chapters/d05_literatura.qmd` | `source/d05_literatura.md` |
| F | `chapters/d06_kljuc_kontrolnih_rezultata.qmd` | `source/d06_kljuc_kontrolnih_rezultata.md` |

Dodatak s kontrolnim rezultatima također se generira iz zadataka. Pokreni `python scripts/build_book.py --write` nakon izmjene izvora ili modela.
