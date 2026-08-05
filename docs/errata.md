# Errata udžbenika Mehanika fluida 1

Ovo je javna evidencija potvrđenih pogrešaka u objavljenim release candidate i
stabilnim izdanjima. Otvoreni razvojni dug prije objave vodi se u
[statusu izrade](../status_izrade_udzbenika.md), a ne prikazuje se kao errata
izdanja koje još nije objavljeno.

## Kako prijaviti pogrešku

Upotrijebite [GitHub obrazac za erratu](https://github.com/martibasic/MF1_udzbenik/issues/new?template=errata.yml).
Za jednu pogrešku otvorite jednu prijavu i navedite:

- inačicu iz impresuma ili datum pristupa mrežnom izdanju;
- stabilni ID primjera, zadatka, jednadžbe, slike ili odjeljka;
- URL ili poglavlje i broj stranice;
- uočeni problem te, kada je moguće, neovisnu provjeru ili primarni izvor.

Ako sadržaj još nema vidljiv stabilni ID, u obrascu upišite `nije pronađen` i
navedite točan naslov poglavlja i odjeljka. Uredništvo dodjeljuje ID prije
zatvaranja potvrđene errate.

## Statusi

| Status | Značenje |
|---|---|
| `prijavljeno` | Zaprimljeno, još nije neovisno reproducirano. |
| `potvrđeno` | Pogreška je reproducirana i određen je zahvaćeni sadržaj. |
| `ispravak-pripremljen` | Ispravak i povezane provjere postoje u radnoj grani. |
| `objavljeno` | Ispravak je dio navedene javne inačice. |
| `odbijeno` | Prijava nije reproducirana ili je ponašanje namjerno; razlog ostaje javno zabilježen u issueu. |

Prioriteti su `P0` za potencijalno opasnu ili normativno pogrešnu tvrdnju, `P1`
za pogrešku koja mijenja fizikalni ili brojčani rezultat, `P2` za pedagošku ili
lokalnu tehničku nejasnoću i `P3` za jezik ili prikaz bez promjene značenja.

## Evidencija potvrđenih ispravaka

Tablica je namjerno prazna dok ne postoji potvrđena errata objavljenoga
izdanja. Ne unose se pretpostavljeni ni razvojni zapisi.

| Stabilni ID | Pogođena inačica | Prioritet | Status | Lokacija | Ispravak | Prvo ispravljeno izdanje |
|---|---|---|---|---|---|---|

## Tok zatvaranja

1. Uredništvo reproducira problem i provjerava zahvaća li isti model tekst,
   odgovor, SVG, notebook ili verifikator.
2. Potvrđenom zapisu dodjeljuju se stabilni ID, prioritet i pogođene inačice.
3. Ispravak uključuje odgovarajuću neovisnu provjeru, a ne samo izmjenu
   objavljenoga broja.
4. Nakon prolaza QA i oba formata status postaje `ispravak-pripremljen`.
5. Nakon javne objave u tablicu se unosi prvo ispravljeno izdanje i status
   `objavljeno`; promjena se istodobno bilježi u
   [dnevniku promjena](../CHANGELOG.md).

Promjene jednadžbi, brojčanih odgovora, predznaka, normativnih tvrdnji i granica
modela uvijek ulaze u javni trag. Čiste pravopisne izmjene mogu se grupirati u
dnevniku promjena, ali potvrđena pojedinačna prijava ostaje povezana sa svojim
GitHub issueom.
