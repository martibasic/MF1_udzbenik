# Status izrade MF1_udzbenika (srpanj 2026)

## Svrha dokumenta

Ovo je aktualni statusni presjek kanonskog udzbenika u `MF1_udzbenik`. Dokument vise ne vodi otvoreni migracijski backlog, nego opisuje sto je stvarno zatvoreno, sto je sada u odrzavanju i koji su najblizi vrijedni potezi.

> **Faza 2 — generalna recenzija i plan nadogradnje (pokrenuto 2026-07-02).** Provedena je sveobuhvatna recenzija udzbenika (sadrzaj, didaktika, notacija, produkcija, figure). Plan izmjena u pet faza (A–E) vodi se izvan repozitorija; Faza A (brzi popravci konzistentnosti) je u tijeku.
>
> **Zatvoreno u Fazi 2 / A**:
> - Poglavlje `U14` (bezdimenzijski brojevi, dimenzijska analiza i slicnost) i dodatak `D04` (numericka mehanika fluida) sada su dio knjige; glavni niz je `U00`, `U01–U14`, dodaci `D01–D04`.
> - **Matplotlib→SVG konverzija je dovrsena**: 0 preostalih python/matplotlib figure-blokova u `source/`, svih 139 SVG-ova referencirano (0 slijepih referenci, 0 orphana). Raniji backlog od 26–27 blokova vise ne postoji.
> - Notacija ujednacena: `h_f`→`h_l` (U13), `p_man`→`p_M` (U03/D01/D02), turbostrojarska trojka `c/w/u` uskladena u D01/D03 (uklonjen nekoristeni `v_rel`).
> - Uvodni vodic `U00` uskladen sa stvarnim tipovima primjera (Rijeseni/Kratki primjer, Cjeloviti zadatak, Zadaci za vjezbu) i brojem primjera (5–8 po poglavlju); uklonjeni nepostojeci tipovi `GP`/`PO`.
> - `za_ispis.qmd` sada ukljucuje i `D04`; opce reference "pog. 1–13" prosirene na "pog. 1–14".
>
> **Faza B (u tijeku)**: B1 — 78 brojcanih odgovora na vjezbe U01–U13 dodano (zatvoreno); B2 — utvrdjeno da sve vjezbe vec imaju T1 zadatke (nije potrebno); B3 — dodan T4 sintezni zadatak u U14 (Froudeova slicnost + provjera rezima). Otvoreno: B4 — notebook+QR za U14 (jedino poglavlje bez interaktivnog prikaza; treba `u14_vjezbe_skice.svg` prosiriti 7. mini-skicom).
>
> **Faza D (zatvoreno)**: uklonjeno 245 commitanih `*.quarto_ipynb_*` build-artefakata (+ `.gitignore` popravak — stablo ostaje cisto nakon rendera); 26 radnih dokumenata premjesteno u `docs/radno/`; dodatak `D05 Literatura` + `references.bib`; impressum (autorica, verzija, licenca CC BY-NC-SA 4.0); `toc` za web poglavlja; CI korak `verify_all.py` (blokirajuci, 498/498); `tools/README.md`. Popravljen check `U01.most.p_p_MPa` (sada 498/498 umjesto 497/1).
>
> **Otvoreno (Faza C, E, B4)**: kinematika strujanja kao novi uvod u U08; captioni skica uz vjezbe; nova SVG skica za kinematiku; interaktivni notebook+QR za U14.

> **Faza 1 — QA i unaprjeđenje primjera, zadataka i skica — tekstualni i strukturni dio završen 2026-05-18**. Tracking u [`qa_log_faza1.md`](docs/radno/qa_log_faza1.md). Otvoreno: matplotlib→SVG konverzija (27 blokova kroz U07–U13) i finalni quarto render check.
>
> **Rezultati Faze 1**:
> - 13/13 poglavlja prošlo tekstualni QA prema protokolu (Zadano/Traženo/Skica/Pretpostavke/Rješenje s fizikalnim tumačenjima/Provjera).
> - 427/428 SymPy provjera prošlo (1 zaokruženje, dokumentirano u qa_log).
> - 93 SVG-a normalizirano i naslovi uklonjeni (caption u Markdownu pokriva tu ulogu).
> - 1 stvarna matematička greška u izvoru otkrivena i popravljena (U10 rashladni cjevovod: λ·L/D = 1,20 umjesto 1,00).
> - 1 orphan SVG spojen s primjerom (U07 Kalibracijski modul).
> - U01 SVG sistemski popravci: oznake $A_e \to A_L$, $F_e \to F_L$, plave ulazne sile $\to$ crvene (per protokol).
>
> **Faza 1.5 — Didaktičko obogaćivanje (završeno tekstualno 2026-05-18)**. 11 novih primjera/cjelovitih zadataka uvedeno kroz U01–U13 da bi popunilo didaktičke prilike koje su identificirane kroz analizu pokrivenosti teorija↔primjeri. Detalji u [`qa_log_faza1.md`](docs/radno/qa_log_faza1.md) i SVG specifikacije za Codex u [`todo_svg_za_codex.md`](docs/radno/todo_svg_za_codex.md).
>
> **Rezultati Faze 1.5**:
> - 11 novih primjera dodano kroz U01–U13 (5× T2 P, 4× T3/T4 CH, 2× T2 P proširenja postojećih scena).
> - Glavni didaktički koncepti uvedeni: temperatura↔viskoznost (U02), neto tlak stijenke broda (U03), tri sloja fluida (U05), plinski jastuk + zakrivljena ploha (U06), stabilnost broda + SOLAS (U07), difuzor (U09), starenje cijevi (U10), vodeni udar (U11), optimalna brzina lopatice $u_{opt} = c_1/2$ (U12), radna točka crpka⇄cjevovod (U13), hidraulična kočnica vozila (U01).
> - 70 novih SymPy checkova; ukupno sada 497/498 PASS (1 pre-existing rounding u U01.most.p_p_MPa).
> - 11 novih SVG datoteka **za izradu** (Codex – specifikacije u `docs/radno/todo_svg_za_codex.md`).
> - Ukupno SVG otvoreno za izradu: 27 (Faza 1 matplotlib konverzija) + 11 (Faza 1.5 novi primjeri) = **38 SVG datoteka**.

## Trenutno stanje u jednoj recenici

`MF1_udzbenik` je stabilna integrirana Quarto knjiga s poglavljima `U00`, `U01-U14` i dodacima `D01-D04`; prijenos zadataka je urednicki zatvoren, a glavni posao presao je u odrzavanje, finu kalibraciju i selektivno autorsko jacanje.

## Sto je stvarno zatvoreno

1. Kanonska struktura knjige postoji i upotrebljiva je za web i print tok.
2. Glavna poglavlja `U01-U14` postoje kao stvarna, cjelovita poglavlja, a ne kao pilot-kosturi.
3. Teorija, matematicki izvodi, rijeseni primjeri i zadaci nalaze se u istom toku citanja.
4. Uvodi su prosireni stvarnim inzenjerskim kontekstom; pocetni application-okviri standardizirani su pod oznakom `Inzenjerski kontekst`.
5. Provedeni su jezikoslovni, stilisticki i interpunkcijski prolazi kroz glavni niz `U01-U14`.
6. Suvisna didakticka mini-potpoglavlja u prozi srezana su i pretvorena u kompaktniji tok prema primjerima.
7. Zadatkovni sloj i skice uskladeni su s kucnim print-first standardom.
8. Puni `quarto render` prolazi, a editor i problems checkovi su cisti.
9. Kanonski SVG dizajnerski standard definiran je u `protokol_prerade_zadataka_i_skica.md`; svi novi i prerađeni figure-blokovi koriste statičke SVG datoteke u `assets/print/` umjesto matplotlib/Python koda.
10. SVG konverzija je dovršena (provjereno 2026-07-02): u `source/` nema nijednog matplotlib/python figure-bloka, a svih 139 SVG datoteka u `assets/print/` je referencirano iz teksta (0 slijepih referenci, 0 orphana). Raniji backlog od 26 preostalih blokova više ne postoji.
11. Strukturna SVG normalizacija (prefiks ID-eva, font, aria, root atributi) provedena je jednokratnom skriptom `tools/svg_normalize.py` nad svih 93 SVG-a u `assets/print/`.

## Status po cjelinama

| Cjelina | Status | Napomena |
| --- | --- | --- |
| Arhitektura knjige | `zatvoreno` | `MF1_udzbenik` je jedini kanonski projekt |
| `U00` i `U01-U14` | `zatvoreno` | glavni niz postoji i urednicki je konsolidiran |
| `D01-D04` | `odrzavanje` | ostaju aktivni i trebaju pratiti notaciju i terminologiju knjige |
| Prijenos zadataka | `zatvoreno` | donorski backlog vise nije otvoreni razvojni problem |
| Jezik i urednistvo | `zatvoreno` | veliki sweepovi su odradeni; ostaje samo selektivno odrzavanje |
| Vizualni standard skica | `odrzavanje` | baza je zakljucana, ali pojedine skice se mogu i dalje dizati |
| SVG konverzija figura | `zatvoreno` | 0 preostalih matplotlib blokova; svih 139 SVG-ova referencirano (0 slijepih referenci, 0 orphana) |
| Strukturna normalizacija SVG-a | `zatvoreno` | `tools/svg_normalize.py` proveden globalno; prefiksirani ID-evi, kanonski font, aria, root atributi |
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

1. Drzati `D01-D04` uskladenima s glavnim poglavljima kad se promijeni notacija, termin ili tipicna greska.
2. Fino kalibrirati tezinske oznake i raspored zadataka ondje gdje jos ima prostora za bolju gradaciju.
3. Selektivno podizati standard skica i print/PDF citljivosti.
4. Povremeno raditi puni render i lokalne chapter-render provjere nakon vecih urednickih promjena.
5. Otvarati nove zadatke ili visi integracijski sloj samo kad postoji stvarna didakticka rupa.
6. Završiti SVG konverziju preostalih matplotlib blokova po poglavljima (U01 - 1; U07 - 5; U08 - 3; U09 - 3; U10 - 4; U11 - 3; U12 - 4; U13 - 3). Napomena: `assets/print/u07_val3_dva_fluida_modul.svg` već postoji kao pripremljena zamjena za matplotlib blok `fig-u07-kalibracijski-modul`.
7. Za svako poglavlje osigurati da uvodni figure-blok (`#fig-uvod-uXX`) prikazuje tri temeljne ideje poglavlja s različitim vizualnim scenama — ne smije ponavljati motiv iz riješenih primjera unutar istog poglavlja.
8. Poštovati kanonsku paletu boja, standard kota i standard markera definiran u `protokol_prerade_zadataka_i_skica.md` pri svakom novom SVG-u.

## Operativni zakljucak

Projekt je izasao iz faze dokazivanja da integrirani udzbenik postoji. Sada vrijedi jednostavnije pravilo: `MF1_udzbenik` je stabilna baza, a svaki sljedeci zahvat mora imati jasan razlog - bolju gradaciju, bolju skicu, bolji jezik, bolji appendix ili jaci inzenjerski smisao - umjesto da se otvara novi migracijski val.