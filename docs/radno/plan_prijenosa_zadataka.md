# Status prijenosa zadataka u MF1_udzbenik

## Svrha dokumenta

Naziv datoteke zadrzan je zbog kontinuiteta, ali dokument vise ne otvara novi plan masovnog prijenosa. Sada sluzi kao zakljuceni presjek prijenosa zadataka i kao operativno pravilo za buduce selektivne dopune korpusa.

## Zakljuceni status prijenosa

1. Skriptni sloj, sloj `530_540_150` i treci sloj dodatnih izvora urednicki su zatvoreni kao migracijski posao.
2. Javna poglavlja `U01-U13` vise se ne ravnaju prema redoslijedu donor-izvora, nego prema vlastitoj didaktickoj cjelini.
3. Donorski dug vise se ne vodi kao otvoreni urednicki dug koji treba "dovuci" u knjigu.
4. Novi zadaci od ovog trenutka predstavljaju novi autorski razvoj, a ne zakasnjeli prijenos starog materijala.

## Cemu sada sluze evidencije i matrice

1. `evidencija_zadataka_skripta.md`, `evidencija_zadataka_530_540_150.md` i `evidencija_zadataka_treci_sloj.md` ostaju trag provenijencije i urednickih odluka.
2. `radna_matrica_sparivanja_*.md` ostaju detaljni usporedni alati, a ne aktivna javna mapa knjige.
3. `legacy_ref` i slicna polja ostaju interni podaci i ne smiju upravljati stilom javnog teksta.

## Nepromjenjiva pravila za buduce dopune

1. Ne otvarati novi masovni uvoz zadataka iz starih izvora.
2. Ne dirati `vjezba_01.qmd` do `vjezba_13.qmd` u ovom ciklusu.
3. Novi zadatak ulazi u knjigu samo ako donosi stvarnu novu fizikalnu scenu, jacu gradaciju tezine, bolji inzenjerski kontekst ili znatno bolju skicu.
4. Trag izvora i eventualni `legacy_ref` mora se zadrzati u internim evidencijama.
5. Javna verzija zadatka mora proci stvarnu urednicku preradu prema aktivnom protokolu.
6. Ako novi zadatak otvara novu tipicnu gresku ili novu notacijsku tocku, treba uskladiti i `D01-D03`.

## Prioritet izvora za eventualne buduce dopune

1. Prvo se provjerava postoji li rupa koju se moze zatvoriti unutar vec postojeceg korpusa `MF1_udzbenik`.
2. Tek nakon toga provjerava se postoji li opravdan donor u skriptnoj, drugoslojnoj ili treceslojnoj evidenciji.
3. Ako donor postoji, preuzima se samo fizikalna jezgra i urednicka ideja, ne tekstualni raspored izvora.

## Operativni postupak za novu dopunu

1. Identificirati stvarnu didakticku rupu u konkretnom poglavlju `U01-U13`.
2. Provjeriti interne evidencije i radne matrice radi provenijencije i mogucih varijanti.
3. Odabrati jedan izvor ili skup bliskih izvora kao banku ideja.
4. Primijeniti pravila iz `protokol_prerade_zadataka_i_skica.md`.
5. Novi zadatak i skicu ugraditi izravno u `source/` poglavlje.
6. Provjeriti render dotaknutog chaptera, a po potrebi i cijele knjige.
7. Dopuniti statusnu ili appendix dokumentaciju samo ako je promjena strukturna ili terminoloski vazna.

## Operativni zakljucak po poglavljima

Za sva poglavlja `U01-U13` vrijedi isto pravilo: prijenos je zatvoren, a buduci dodaci moraju biti selektivni, obrazlozeni i autorski dovoljno jaki da podignu knjigu. Nema vise obveze da se svaka donorska jedinica pretvori u javni zadatak.