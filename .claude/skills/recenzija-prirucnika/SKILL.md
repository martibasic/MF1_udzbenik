---
name: recenzija-prirucnika
description: Recenzija, pregled i jezična ili sadržajna prerada sveučilišnog priručnika „Mehanika fluida – modeli, problemi i rješenja” (MF1_udzbenik). Koristi za svaki zahtjev da se pregleda, recenzira, ocijeni ili lektorira poglavlje, dodatak ili cijela knjiga, za pripremu predaje Povjerenstvu FESB-a, probnu recenziju, upute ili obrazac za recenzente te odgovor na recenziju. Projektni AGENTS.md i docs/konvencije_pisanja.md čitaju se prvi i imaju prednost.
---

# Recenzija priručnika

Ovaj skill je postupak. Pravila teksta su u
[`docs/konvencije_pisanja.md`](../../../docs/konvencije_pisanja.md) (K1–K16), a
sadržajna i strukturna pravila u dokumentima na koje upućuje
[`AGENTS.md`](../../../AGENTS.md). Recenzija koja slijedi oboje daje autorici
popis provjerenih nalaza po važnosti, s mjestom u izvoru, i ne mijenja knjigu.

## 0. Najprije pravila i granice

Pročitaj `AGENTS.md`, `docs/konvencije_pisanja.md`, `docs/autorski_ugovor.md`,
`docs/kurikularna_matrica.md`, `docs/urednicki_stil.md`,
`docs/protokol_strucne_recenzije.md` i, za zadatke i skice,
`protokol_prerade_zadataka_i_skica.md`. U svaku uputu podagentu koji piše ili
čita tekst stavi pravila K1–K16 i oznake težine P0–P3.

Autorica odlučuje o identitetu knjige, opsegu, uklanjanju ili premještanju
sadržaja, nazivlju, recenzentima i odgovorima Povjerenstvu. Predloži, zapiši
odluku kad je donesena, ali je ne donosi sama.

- **Pregled ne mijenja knjigu.** Zahtjev za recenziju ili pregled daje izvještaj
  s nalazima po prioritetu. Izmjene slijede tek kad ih autorica zatraži ili odobri.
- **Uklanjanje ponovljenih riječi je uređivanje; uklanjanje primjera, zadatka,
  izvoda ili granice modela je autorska odluka.**
- Agentsko čitanje ne zamjenjuje imenovane recenzente, studentski pilot ni
  autoričinu procjenu. U izvještaju razlikuj izmjereno, provjereno računom ili
  renderom i dojam.

## Odaberi opseg

| Zahtjev | Koraci |
| --- | --- |
| Lektura ili ispravak odlomka | 6 na tom odlomku |
| Pregled jednog poglavlja | 1, 2 (taj red matrice), 3, 4 (struka, student, urednik), 5, 6 |
| Recenzija cijele knjige prije predaje | 1–6 redom; čitanja 4 razdijeli po skupinama poglavlja |
| Probna recenzija ili obrazac za recenzente | 1, 2, zatim 7 |
| Odgovor na recenziju Povjerenstva | [references/odgovor_recenzentu.md](references/odgovor_recenzentu.md) |
| Zamjena zadataka Z1–Z6 | protokol prerade, ne ovaj skill; nakon provedbe korak 6 |

Mjesni ispravak ne pokreće recenziju cijele knjige. Opseg čitanja u koraku 4
(broj agenata) dogovori s autoricom prije pokretanja: cijela knjiga uz opsege
iz koraka 4 i provjeru iz koraka 5 traži oko 15–20 agenata.

## 1. Stanje i mjerenje

Zabilježi commit, datum i artefakte koje recenziraš. Recenzija se odnosi na
jedan commit; PDF i web moraju biti izgrađeni iz njega. Ako treba novi render,
slijedi pravila iz `AGENTS.md` (puni render kroz `scripts/build_book.py`, web na
localhostu).

```powershell
git rev-parse --short HEAD
python tools/prirucnik_stats.py                  # profil i nalazi po pravilu
python tools/prirucnik_stats.py --nalazi         # nalazi s retkom
python tools/audit_publication.py                # struktura P/Z, polja, ID-jevi, slike
python tools/verify_all.py                       # brojčani rezultati zadataka
```

Usporedi profil s tablicom „Stanje” u konvencijama. Mjere su poticaj za
čitanje, ne presuda: dugačka rečenica u izvodu može biti opravdana, a nula
nalaza ne znači da tekst nema problema s registrom.

## 2. Matrica ishoda

Ishodi su „doprinosi” priručnika. Za svaki red
[kurikularne matrice](../../../docs/kurikularna_matrica.md) zapiši gdje se
nalazi svaki od šest obveznih elemenata i u kojem je stanju:

| Pog. | Ishod | Element | Gdje (stabilni ID) | Stanje |
| --- | --- | --- | --- | --- |
| 8 | izbor referentnih presjeka i tlaka | riješeni primjer s neovisnom provjerom | `ex-…` | ostvareno |

Stanja:

- **ostvareno**: element postoji, vidljiv je studentu i doista provjerava ishod
  (zadatak traži odluku iz ishoda, a ne samo uvrštavanje);
- **djelomično**: postoji, ali je skriven, provjerava samo dio ishoda, ponavlja
  primjer s drugim brojevima ili mu nedostaje neovisna provjera; navedi što;
- **nedostaje**: elementa nema ili je u suprotnosti s ishodom.

Uz matricu provjeri graf preduvjeta (pojam ne smije biti potreban prije
poglavlja u kojem je uveden) i lajtmotive. Matrica je dokaz za recenzentsko
pitanje „odgovara li djelo izvedbenom planu kolegija”.

## 3. Obrnuti nacrt poglavlja

```powershell
python tools/prirucnik_stats.py --nacrt source/uNN_….md
```

Za svaki odlomak napiši poantu (ne temu) i jednu ulogu:

| Uloga | Odlomak |
| --- | --- |
| `temelj` | uvodi model ili pojam potreban za ishod |
| `izvod` | izvodi zakon iz bilance |
| `tumačenje` | objašnjava značenje bez nove algebre |
| `primjena` | povezuje model s uređajem, strukom ili CFD-om |
| `granica` | kaže gdje model prestaje vrijediti |
| `postupak` | korak rješenja primjera |
| `ponavljanje` | kaže što je već rečeno drugdje (navedi gdje) |
| `dnevnik` | govori o izradi knjige, ne o fizici (K1) |
| `bez poante` | ne služi nijednom ishodu |

Spoji nacrt s matricom: svaki odlomak `temelj`, `izvod` i `primjena` treba
služiti nekom ishodu. Odlomci `ponavljanje`, `dnevnik` i `bez poante` postaju
prijedlozi (spojiti, skratiti, ukloniti) s procjenom ušteđenih redaka. Nacrt
ne mijenja nijednu datoteku.

## 4. Neovisna čitanja

Svako čitanje radi svjež agent bez konteksta ovog razgovora. Daj mu PDF (ili
izgrađeni HTML), putanje izvora za navođenje redaka, odgovarajuću uputu i
pravila K1–K16. Ne daj mu autoričine bilješke, raniju recenziju, matricu iz
koraka 2 ni svoju procjenu: čitatelj koji dobije hipotezu vraća je potvrđenu.

| Čitanje | Uputa | Opseg po agentu |
| --- | --- | --- |
| Stručni recenzent mehanike fluida | [references/struka.md](references/struka.md) | 3–4 poglavlja |
| Primjenski recenzent (brodogradnja, strojarstvo) | [references/primjena.md](references/primjena.md) | 5 poglavlja, samo primjene i zadatci |
| Student koji uči iz knjige | [references/student.md](references/student.md) | 1–2 poglavlja |
| Urednik i lektor | [references/urednik.md](references/urednik.md) | 3–5 poglavlja ili dodatci |

Studentu daj PDF samo zadanih poglavlja i zaseban PDF njihova ključa (izdvoji
stranice), ne izvor. Prijelom PDF-a i weba provjeravaju postojeći audit alati i
pregled renderiranih stranica (`docs/urednicki_stil.md`, odjeljak „Provjera”).
Drugo stručno čitanje drugim modelom vrijedi za teže skupine poglavlja; u
pilotu je dodalo dva nova nalaza i jedan netočan.

Pouke pilota na pog. 13 (`docs/radno/recenzija-2026-11/pog13/RECENZIJA.md`,
odjeljak 10): sve brojeve potvrdila su sva stručna čitanja; student je dao
najviše nalaza koji vrijede za cijelu knjigu; urednik bez ograničenja daje
desetke nalaza P3; dva čitatelja neovisno su pogriješila jer nisu otvorila
bilježnicu na koju tekst upućuje.

## 5. Provjera nalaza i trijaža

Agentski nalaz zvuči jednako sigurno kad je točan i kad nije. Prije nego uđe u
izvještaj:

- otvori izvor na navedenom retku i potvrdi da tekst ondje doista stoji;
- brojčani nalaz ponovno izračunaj (ili pokreni pripadni verifikator iz
  `CANONICAL_CHAPTERS` u `tools/generate_verification_manifest.py`);
- nalaz o prijelomu potvrdi na renderu;
- odbaci nalaz koji traži nešto što ugovor, matrica ili autoričina odluka
  izričito drukčije određuju, a sukob zapiši kao pitanje autorici.

Dva čitatelja koja tvrde isto nisu dokaz: mogu dijeliti isti propust. Za više od
dva-tri poglavlja provjeru razdijeli: po skupini poglavlja jedan svjež agent
provjerava nalaze P0–P2 svih čitanja te skupine prema ovim pravilima i vraća
potvrđeno, odbačeno ili nepotvrdivo s razlogom. Glavni agent provjerava sve P0
i P1 sam.

Zatim objedini nalaze svih čitanja, ukloni preklapanja i razvrstaj ih po P0–P3.
Izvještaj ide u `docs/radno/recenzija-GGGG-MM/` (pojedinačna čitanja) i
`docs/radno/recenzija-GGGG-MM/RECENZIJA.md` (objedinjeni), po uzoru na
`RECENZIJA_ZAVRSNA.md`:

1. opća ocjena u jednom odlomku i tri najvažnija nalaza;
2. P0 i P1 kao tablice (mjesto, što, prijedlog);
3. P2 grupirano po vrsti (ponavljanje, dosljednost, jezik, prikaz);
4. P3 kratko;
5. što je dobro i treba ostati;
6. redoslijed provedbe s rizikom i povezanim datotekama (D06, verifikator, SVG);
7. odluke koje su autoričine.

Svaki nalaz ima stabilni ID ili `datoteka:redak`, pravilo (K…, ugovor, matrica)
i oznaku „izmjereno”, „provjereno” ili „dojam”.

## 6. Provjera značenja nakon prerade (obvezno)

Nakon svake lekture ili prerade, ručne ili agentske:

```powershell
git diff --word-diff -- source/
python tools/prirucnik_stats.py --usporedi <commit prije prerade> source/…
```

- Pročitaj cijeli diff. `--usporedi` izdvaja promijenjene rečenice u kojima se
  promijenio broj, nijekanje („bez”, „nije”), ograda („približno”, „može”),
  snaga („uvijek”, „samo”) ili poredba. Lektorski prolazi u ovom repozitoriju
  znali su usput promijeniti tvrdnju; prolaz alata to ne isključuje.
- Svaki broj koji je nestao iz teksta nalazi se drugdje ili je autorica odobrila
  uklanjanje. Navedi ga u poruci commita.
- Ne dodaj broj, izvor, mehanizam ni rezultat simulacije koji ne slijede iz
  izvora knjige ili provjerenog djela.
- Ako se promijenio broj, iskaz zadatka ili oznaka, slijedi
  [redoslijed provjera](../../../protokol_prerade_zadataka_i_skica.md#7-redoslijed-provjera)
  i obnovi D06 i manifest generatorima.
- Pogledaj promijenjene stranice u renderiranom PDF-u i webu.

## 7. Formalna recenzija i predaja

Postupak FESB-a i ono što pravilnik propisuje, odnosno ne propisuje, nalaze se
u [references/fesb_postupak.md](references/fesb_postupak.md). Predložak pisane
recenzije za imenovane recenzente je
[references/obrazac_recenzije.md](references/obrazac_recenzije.md).

Agent može napisati **probnu recenziju** po tom predlošku da autorica vidi što
će recenzent vjerojatno pitati. Probna recenzija označena je kao takva i nikad
se ne predaje kao recenzija imenovanog recenzenta. Za izdanje `v1.0` vrijedi i
[protokol stručne recenzije](../../../docs/protokol_strucne_recenzije.md).

## Nikad

- Ne izmišljaj rezultate, izvore, članke pravilnika ni uvjete Povjerenstva.
  Što nije provjereno u dokumentu, piše se kao nepoznato.
- Ne proglašavaj didaktičku kvalitetu dokazanom jer CI ili alat prolazi.
- Ne oslabljuj audit ni pravilo da bi pregled izgledao čišće.
- Ne provodi nalaze bez autoričine odluke i ne mijenjaj knjigu tijekom pregleda.
- Ne piši recenziju u ime imenovanog recenzenta.
