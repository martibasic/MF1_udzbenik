# Protokol studentskog pilota

Pilot provjerava bira li student ispravan model i njegove pretpostavke prije
algebarskog računa. Ovaj dokument je pripremljen protokol; rezultat pilota ne
smije se proglasiti ostvarenim prije rada sa stvarnim studentima.

## Uzorak i materijali

- Uključiti 8–12 studenata koji su upravo završili ili pohađaju prvi kolegij
  mehanike fluida.
- Upotrijebiti release-candidate označen verzijom i Git commitom.
- Odabrati najmanje 12 zadataka: po jedan iz svake veće sadržajne cjeline te
  najmanje četiri zadatka razine T3/T4.
- Ne prikazivati naputak ni kontrolni rezultat prije predaje modelskog dijela.

Ako se rezultati namjeravaju rabiti kao istraživački podaci, voditelj prije
pilota provjerava obveze informiranog pristanka, privatnosti i etičkog
odobrenja svoje ustanove. U javni repozitorij ne upisuju se osobni podaci.

## Tijek jednog zadatka

Student prije računanja zapisuje:

1. sustav ili kontrolni volumen i traženu veličinu;
2. zakon bilance ili konstitutivnu vezu koju će primijeniti;
3. referencu tlaka, osi i pozitivne smjerove ako su relevantni;
4. pretpostavke i najmanje jednu granicu modela;
5. kvalitativno predviđanje predznaka, trenda ili reda veličine.

Tek nakon zaključavanja tih odgovora student izvodi račun i neovisnu provjeru
rezultata. Moderator bilježi vrijeme, mjesta zastajanja i otkrivene naputke.

## Bodovanje i kriterij prolaza

Za svaki pokušaj binarno se ocjenjuju `izbor modela` i `ključne pretpostavke`
prema unaprijed pripremljenom ključu. Glavna metrika jest

\[
S=\frac{N_{\text{ispravan model i pretpostavke}}}
        {N_{\text{svih valjanih pokušaja}}}.
\]

Pilot prolazi kada je \(S\ge 0{,}80\). Uz ukupni rezultat izvještavaju se
rezultati po zadatku i poglavlju; ukupni prag ne skriva pojedini zadatak na
kojem manje od polovice studenata prepoznaje model.

## Dnevnik nejasnoća

Svaka nejasnoća dobiva:

- stabilni ID sadržaja;
- anonimizirani opis pogrešnog tumačenja;
- fazu u kojoj se javila: postavljanje, model, algebra, jedinice ili provjera;
- broj pogođenih studenata;
- odluku i poveznicu na ispravak.

Nakon izmjena ponovno se provjeravaju pogođeni zadatci. Sažetak pilota navodi
uzorak, korišteni commit, metriku \(S\), otvorene nalaze i odluku o `v1.0`.
