# Status izrade MF1_udzbenika (svibanj 2026)

## Svrha dokumenta

Ovo je aktualni statusni presjek kanonskog udzbenika u `MF1_udzbenik`. Dokument vise ne vodi otvoreni migracijski backlog, nego opisuje sto je stvarno zatvoreno, sto je sada u odrzavanju i koji su najblizi vrijedni potezi.

## Trenutno stanje u jednoj recenici

`MF1_udzbenik` je stabilna integrirana Quarto knjiga s poglavljima `U00`, `U01-U13` i dodacima `D01-D03`; prijenos zadataka je urednicki zatvoren, a glavni posao presao je u odrzavanje, finu kalibraciju i selektivno autorsko jacanje.

## Sto je stvarno zatvoreno

1. Kanonska struktura knjige postoji i upotrebljiva je za web i print tok.
2. Glavna poglavlja `U01-U13` postoje kao stvarna, cjelovita poglavlja, a ne kao pilot-kosturi.
3. Teorija, matematicki izvodi, rijeseni primjeri i zadaci nalaze se u istom toku citanja.
4. Uvodi su prosireni stvarnim inzenjerskim kontekstom; pocetni application-okviri standardizirani su pod oznakom `Inzenjerski kontekst`.
5. Provedeni su jezikoslovni, stilisticki i interpunkcijski prolazi kroz glavni niz `U01-U13`.
6. Suvisna didakticka mini-potpoglavlja u prozi srezana su i pretvorena u kompaktniji tok prema primjerima.
7. Zadatkovni sloj i skice uskladeni su s kucnim print-first standardom.
8. Puni `quarto render` prolazi, a editor i problems checkovi su cisti.
9. Kanonski SVG dizajnerski standard definiran je u `protokol_prerade_zadataka_i_skica.md`; svi novi i prerađeni figure-blokovi koriste statičke SVG datoteke u `assets/print/` umjesto matplotlib/Python koda.
10. U01–U04 su potpuno konvertirani: svi matplotlib figure-blokovi u `source/` zamijenjeni su SVG referencama; uvodni figure-blokovi prate temu i filozofiju poglavlja, a ne recikliraju vizualni motiv iz riješenih primjera.

## Status po cjelinama

| Cjelina | Status | Napomena |
| --- | --- | --- |
| Arhitektura knjige | `zatvoreno` | `MF1_udzbenik` je jedini kanonski projekt |
| `U00` i `U01-U13` | `zatvoreno` | glavni niz postoji i urednicki je konsolidiran |
| `D01-D03` | `odrzavanje` | ostaju aktivni i trebaju pratiti notaciju i terminologiju knjige |
| Prijenos zadataka | `zatvoreno` | donorski backlog vise nije otvoreni razvojni problem |
| Jezik i urednistvo | `zatvoreno` | veliki sweepovi su odradeni; ostaje samo selektivno odrzavanje |
| Vizualni standard skica | `odrzavanje` | baza je zakljucana, ali pojedine skice se mogu i dalje dizati |
| SVG konverzija figura | `u tijeku` | U01–U04 potpuno konvertirani; U05–U13 selektivno po potrebi |
| Validacija builda | `cisto` | puni render prolazi i nema editor gresaka |
| Legacy vjezbe | `zamrznuto` | ne diraju se do sljedece akademske godine |

## Sto vise nije otvoreno pitanje

1. Ne otvara se nova masovna migracija iz starih izvora.
2. Ne tretira se zaseban teorijski prirucnik kao obvezan paralelni javni proizvod.
3. Ne lovi se vise mehanicka simetrija poglavlja samo radi forme.
4. Ne dira se `vjezba_01.qmd` do `vjezba_13.qmd` u ovom ciklusu.
5. Ne koristi se matplotlib/Python kod za generiranje figura u finalnoj knjizi; sve figure su staticke SVG datoteke.
6. Ne reciklira se isti vizualni motiv (npr. dizalica s vozilom, most) unutar istog poglavlja za razlicite figure — svaka figura nosi vlastitu vizualnu scenu.

## Aktivni prioriteti odrzavanja

1. Drzati `D01-D03` uskladenima s glavnim poglavljima kad se promijeni notacija, termin ili tipicna greska.
2. Fino kalibrirati tezinske oznake i raspored zadataka ondje gdje jos ima prostora za bolju gradaciju.
3. Selektivno podizati standard skica i print/PDF citljivosti.
4. Povremeno raditi puni render i lokalne chapter-render provjere nakon vecih urednickih promjena.
5. Otvarati nove zadatke ili visi integracijski sloj samo kad postoji stvarna didakticka rupa.
6. Nastaviti SVG konverziju figure-blokova po poglavljima (U05 i dalje); prioritet imaju uvodni pogledi i ilustracije riješenih primjera koji još koriste matplotlib/Python blokove.
7. Za svako poglavlje osigurati da uvodni figure-blok (`#fig-uvod-uXX`) prikazuje tri temeljne ideje poglavlja s različitim vizualnim scenama — ne smije ponavljati motiv iz riješenih primjera unutar istog poglavlja.
8. Poštovati kanonsku paletu boja, standard kota i standard markera definiran u `protokol_prerade_zadataka_i_skica.md` pri svakom novom SVG-u.

## Operativni zakljucak

Projekt je izasao iz faze dokazivanja da integrirani udzbenik postoji. Sada vrijedi jednostavnije pravilo: `MF1_udzbenik` je stabilna baza, a svaki sljedeci zahvat mora imati jasan razlog - bolju gradaciju, bolju skicu, bolji jezik, bolji appendix ili jaci inzenjerski smisao - umjesto da se otvara novi migracijski val.