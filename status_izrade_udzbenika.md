# Status izrade sveučilišnog priručnika MF1

**Presjek: 27. rujna 2026.** Ovaj dokument opisuje aktualno lokalno radno
izdanje. Datirani zapisi u `docs/radno/`, dnevniku promjena i tipografskom
izvještaju čuvaju povijest; njihovi brojevi nisu aktualni inventar.

**Naslov:** *Mehanika fluida: modeli, problemi i rješenja — Priručnik za
samostalan rad s numeričkim pokusima i primjenama u brodogradnji i strojarstvu*

Prethodni commit `8e05312b4b70eb1c96b9b14d3585ea853c609149` prošao je puni
lokalni objavni CI i [GitHub Action](https://github.com/martibasic/MF1_udzbenik/actions/runs/36302967616)
(završen uspješno 27. rujna). Današnje dopune još nisu poslane na GitHub.
Prolaz prethodnog commita nije dokaz provjere tih dopuna.

## Aktualni sadržaj i završene dorade

| Područje | Stanje i granica tvrdnje |
|---|---|
| Inventar | 15 poglavlja, 88 riješenih primjera, 90 samostalnih zadataka, šest dodataka, 797 prikazanih jednadžbi, 93 referencirane SVG skice, 23 bibliografska zapisa i 17 bilježnica. Planirano opterećenje ostaje 145 sati rada uz priručnik. |
| Zadaci | Svako poglavlje ima šest zadataka u raspodjeli `2×T1 + 2×T2 + T3 + T4`. Iskazi i rezultati postojećih 90 zadataka nisu mijenjani u ovoj dopuni. |
| CFD objašnjenja | Postojeći povezani primjeri i fizikalna tumačenja dobili su po jedno odabrano postojeće pitanje „Zastani i promisli” u svakom poglavlju. Slijedi ga pripadajuće tumačenje u tijeku teksta. |
| Pojmovnik | Posljednji stupac sadrži poveznice na poglavlja i dodatke umjesto internih kodova U/D. Broj ili slovo odredišta tumači se u uvodu tablice. |
| Eksperimentalni primjer | Novi P6 u U12, `ex-stepenica-mjerenje-cfd`, povezuje mjerenje ponovnog priljubljivanja iza stepenice i objavljeni CFD. Izvorne tablice, provenijenca, račun, bilježnica i verifier usklađeni su. |
| CFD podatci | Dva sintetička nastavna paketa te dvije javne reference: NACA 0012 i tok iza stepenice. Sintetički paket nije stvarni pokus; referentni paket nije potpuna validacija. |
| NACA arhivske praznine | Ponovljen pregled TMR arhive nije pronašao tražene povijesti reziduala/sila ni masenu bilancu. Izostanak je dokumentirano ograničenje izvora, a ne zadatak korisniku da pribavi podatke. Nastavna usporedba Z6 izričito razlikuje objavljene brojeve i pretpostavljene nesigurnosti. |
| Naziv publikacije | Vidljivi tekst koristi naziv sveučilišni priručnik; naslov uključuje i strojarstvo. Stare putanje repozitorija i sidra sačuvani su radi postojećih poveznica. |

## Provjere aktualne dopune

Numerički QA prolazi **1.345 provjera u 19 modula**: 1.123 usporedbe s unaprijed
zadanim ciljem i 222 invarijantne, dimenzijske ili granične provjere. Dodatne
neovisne fizikalne regresije prolaze 22/22. Manifest pokriva 90/90 zadataka;
nema deklariranih rupa ni tautoloških usporedbi.

Novi arhivski verifier provjerava izvorne datoteke, odabrane retke i podatke
ugrađene u bilježnicu. Sedam regresijskih testova odbija promijenjeno mjerenje,
oštećen arhivski izvor, izmišljenu razinu pouzdanosti ili mrežnu konvergenciju,
pogrešan Reynoldsov broj i razilaženje podataka bilježnice.

**Puni lokalni objavni CI: PASS (838 s).** Zajednički runner izgradio je
web, PDF i JupyterLite iz završnih izvora; izvršio 17/17 bilježnica i provjerio
tri interaktivna laboratorija, 72 mrežna prikaza na 320/768/1440 px te A4 ispis.
Izvještaj: `tools/tmp/prirucnik-dorada-20260927/publication-final.log` (lokalni,
ignorirani dokaz). Današnje promjene nisu commitane ni poslane na GitHub.

PDF ima **318 A4 stranica** i **6.662.819 B**. Kontaktni vizualni
pregled obuhvatio je 35 odabranih stranica: naslovnicu, sva izdvojena
pitanja, novi primjer, pojmovnik te dodatke D i E; novi primjer i ključne
tablice dodatno su pregledani povećano. Pregled cijelog teksta PDF-a nije
pronašao stari naziv publikacije. Automatski PDF audit provjerava sve stranice,
ali taj prolaz nije tvrdnja o vizualnom čitanju svake od njih.

Mrežni pregled potvrdio je 15 vidljivih pitanja, 121 poveznicu zadnjeg stupca
pojmovnika, potpuni naslov i odsutnost starog naziva. Provjereno je i pomicanje
tablica tipkovnicom na mobilnoj širini. PDF pojmovnik ima 123 valjana unutarnja
odredišta, uključujući dvije zadržane poveznice u definicijama.

Lokalni pregled: <http://127.0.0.1:8766/>. Poslužuje `_site/`; preuzimanje PDF-a
ima isti SHA-256 kao `_book/mehanika-fluida-1.pdf`:
`7a11b4bd9effebcd2dd9fd667837d54443ed9019b1066e3cb15b59217c2b50a4`.
Postupak i granice pregleda sažeti su u
[zapisu dorade](docs/radno/prirucnik_dorada_2026-09-27.md).

## Granice eksperimentalne usporedbe

Objavljeni interval `x_r/H = 6,26 ± 0,10` nije sam po sebi standardna
nesigurnost ni interval s poznatom razinom pouzdanosti. Odabrani CFD skup
iza stepenice nema potpunu studiju mrežne konvergencije. Zato P6 uči odrediti
položaj ponovnog priljubljivanja, usporediti ga s mjerenjem i imenovati
nedostajuće provjere; ne proglašava model validiranim na osnovi jednog broja.

Za NACA primjer ostaje nepoznat potpuni mjerni budžet na usporednom napadnom
kutu. Novi proračun ne bi retroaktivno dokazao konvergenciju starih objavljenih
rezultata. Oba ograničenja opisana su uz podatke i u dodatku D.

## Stručna recenzija i studentski pilot

Priručnik **još nije poslan na neovisnu stručnu recenziju**. Stručna i
primjenska recenzija te studentski pilot nisu provedeni i nisu dio ove dorade.
Automatske provjere, autorski pregled i uspješan deploy ne zamjenjuju te
korake niti znače dodjelu oznake `v1.0` ili formalno odobrenje kategorije djela.

Planirani postupci ostaju u [protokolu stručne recenzije](docs/protokol_strucne_recenzije.md)
i [protokolu studentskog pilota](docs/protokol_studentskog_pilota.md).
Posebno stručno čitanje naprednog dvofluidnog modela stabiliteta u U06 ostaje
dio buduće recenzije. Ovim zapisom ne stvara se nova obveza prikupljanja podataka.

## Javni trag izmjena

Potvrđene pogreške vode se u [errati](docs/errata.md), sadržajne i tehničke
dorade u [dnevniku promjena](CHANGELOG.md), a provedene provjere u izlazu
zajedničkog runnera `scripts/check_publication.py`.
