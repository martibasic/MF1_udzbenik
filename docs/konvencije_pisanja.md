# Konvencije pisanja i recenzije priručnika

Ovaj dokument skuplja pravila teksta sveučilišnog priručnika „Mehanika fluida:
modeli, problemi i rješenja” na jedno mjesto, tako da se svako pravilo može
provjeriti i navesti u recenziji oznakom (K1–K16). Vrijedi za svaki tekst koji
čitatelj vidi: poglavlja, dodatke, potpise i opise slika, naputke, kontrolne
rezultate i bilježnice.

Ne zamjenjuje mjerodavne dokumente. Kad se razlikuju, prednost imaju:

1. izričita odluka autorice;
2. [autorski ugovor](autorski_ugovor.md) (oblik, blokovi, ID-jevi, zadatci, slike);
3. [kurikularna matrica](kurikularna_matrica.md) (ishodi, razine, preduvjeti);
4. [urednički stil](urednicki_stil.md) (notacija, nazivlje, odluke od 16. 10. 2026.);
5. [protokol prerade](../protokol_prerade_zadataka_i_skica.md) (zadatci i skice);
6. ovaj dokument.

Postupak recenzije opisuje skill
[`.claude/skills/recenzija-prirucnika/`](../.claude/skills/recenzija-prirucnika/SKILL.md).
Svaki agent koji piše, prerađuje ili recenzira tekst stavlja ova pravila u
upute podagentima.

## Pravila teksta

**K1. Priručnik, ne dnevnik izrade.** Vidljivi tekst opisuje fiziku, model i
postupak kakvi jesu, a ne kako su nastali. U njemu nema verzija, prerada,
„dodano”, „u ovoj inačici”, „radno izdanje”, verifikatora, manifesta, CI-ja,
interne oznake `U05` ili `D06`, valova prerade ni HTML komentara s uputama.
Za drugo poglavlje piše se „pog. N” preko oznake poglavlja, za dodatak „dodatak
A–F”. Status izdanja i promjene pripadaju impresumu, `CHANGELOG.md` i
[errati](errata.md).

**K2. Glas i obraćanje.** Izlaganje i rješenje pišu se u prvom licu množine
(„zapisujemo”, „primijenimo”), a upute studentu u drugom licu jednine
(„Odredi”, „Provjeri”, „Obrazloži”). Ne koristi se „Vi” ni bezlični „student
treba”. Glasovi se ne miješaju unutar istog bloka.

**K3. Rečenice.** Rečenica nosi jednu tvrdnju ili jedan korak. Prosjek u
poglavljima drži se oko 12–18 riječi; rečenica dulja od 40 riječi iznimka je
koju treba opravdati. Niz pogrešaka ili uvjeta odvojen točkom-zarezom postaje
popis s natuknicama. Dvije samostalne tvrdnje ne spajaju se golim zarezom.
Rečenica koja samo ponavlja upravo danu definiciju briše se.

**K4. Izjavni naslovi.** Naslov odjeljka imenuje temu, model ili problem
(„Kada se trenje može zanemariti”, „Vrijeme pražnjenja spremnika”), a ne
postavlja pitanje. Pitanja pripadaju blokovima **Zastani i promisli**,
**Provjeri sebe** i polju **Traži se**. Naslov zadatka imenuje problem; odluka
koju zadatak traži stoji u zahtjevu.

**K5. Pojam, oznaka i kratica prije uporabe.** Svaki pojam, simbol i kratica
definiraju se pri prvoj uporabi u poglavlju ili se upućuje na mjesto definicije
(ranije poglavlje, dodatak A ili B). Kratica koja se u poglavlju javlja manje od
tri puta piše se punim nazivom. Engleski izraz stoji jednom, pri prvom spomenu:
„uvjet prianjanja (engl. *no-slip*)”. Nazivi algoritama, ključeva programa i
internih komponenti ne zamjenjuju opis onoga što rade.

**K6. Jedna veličina, jedna oznaka.** Oznake slijede tablicu u
[uredničkom stilu](urednicki_stil.md) (odjeljak „Notacija i nazivlje”).
Iznimka ($K$, $M$, $k$, $R$, $v_s$) uvodi se uz definiciju i navodi u dodatku A.
Ista točka, presjek i veličina nose istu oznaku u tekstu, skici, naputku,
kontrolnom rezultatu, bilježnici i verifikatoru.

**K7. Autorsko nazivlje i pravopis.** Vrijede oblici iz uredničkog stila i
potvrđeni autorski termini: zadatci, podatci, gubitci; izračunan- (ne
izračunat-); crpka, kućište crpke, radno kolo, propeler, usisni koš, umirni
bazen; hidrostatički; potkritični i natkritični; vodoravno i okomito (uspravno);
oplakan- (oplakani opseg, oplakana ploha), nikad „omočen-”; brzina vrtnje u
$\mathrm{min^{-1}}$; protok u L/s; hrvatski navodnici „…”. Kratica „MF1” ne
stoji u tekstu; piše se „u ovom priručniku”.

**K8. Brojevi, jedinice i zaokruživanje.** Decimalni zarez u formuli piše se
`9{,}81`, a popis brojeva odvaja točkom-zarezom: $(26;\,0)$, $i=1;\,2;\,3$.
Broj i jedinica dijele se razmakom; jedinice su SI s dogovorenim iznimkama
(L/s, bar uz Pa ako je u praksi uobičajen). Unutar jednog primjera koristi se
jedna razina zaokruživanja: međurezultati s tri do četiri značajne znamenke,
konačni rezultat s dvije do tri. Isti rezultat ima istu vrijednost u rješenju,
skici, kontrolnom rezultatu, ključu (dodatak F) i verifikatoru.

**K9. Snaga tvrdnje odgovara dokazu.** „Vrijedi” dolazi uz uvjet pod kojim
vrijedi. „Uvijek”, „nikad” i „samo” rabe se za ono što je točno u granicama
modela, a ne za iskustveno pravilo. Iskustveni prag (npr. $Ma\approx0{,}3$,
$Re\approx2300$) navodi se kao orijentacija s izvorom ili ogradom. Poredba
imenuje s čim se uspoređuje. CFD odlomak ne iznosi rezultate simulacije ili
mjerenja koji nisu provedeni; sintetički nastavni podatci označeni su kao takvi.

**K10. Jednom izvedeno, dalje upućeno.** Zakon se izvodi jednom; kasnije se
upućuje na njegovu jednadžbu brojem. Uvod, okvir, napomena uz skicu, rješenje i
sažetak ne ponavljaju isti niz formula ni istu rečenicu. Napomena uz skicu kaže
samo ono što skica ne može pokazati, najčešće u jednom do tri retka.

**K11. Granica modela.** Blok **Granica modela** ima jednu do tri izjavne
rečenice: što model zanemaruje, gdje prestaje vrijediti i koji je zaključak
izvan modela zabranjen. Ne sadrži planove, isprike ni nastavak teorije.
Granica na koju se rješenje oslanja stoji u vidljivom tekstu, ne samo u
skrivenom bloku.

**K12. Upućivanja.** Na jednadžbu, sliku i tablicu upućuje se brojem
(`[-@eq-…]`, `[-@fig-…]`), ne riječima „ispod” ili „iznad”, jer se prijelom
razlikuje u webu i PDF-u. Poglavlje o sebi piše „u ovom poglavlju”. Upućivanje
na zadatak izvan poglavlja navodi i broj poglavlja.

**K13. Slike i opisi.** Potpis je opisna rečenica sa završnom točkom i kaže što
slika pokazuje. Alternativni opis (`fig-alt`) kaže što je nacrtano i ne ponavlja
potpis. Na slici nema imena datoteka, verzija, datuma ni oznaka izrade. Skica
samostalnog zadatka ne otkriva postupak; skica primjera ne ponavlja brojčani
račun. Fizikalna povezanost i stil skica slijede [AGENTS.md](../AGENTS.md) i
[protokol](../protokol_prerade_zadataka_i_skica.md#svg-standard-za-skice-i-ilustracije).

**K14. Izvori.** Tvrdnja o normi, praksi, empirijskom koeficijentu ili
povijesti ima izvor iz dodatka E ili je izrijekom označena kao nastavna
procjena. Djelu se pripisuje samo ono što u njemu piše. Izdanja u literaturi
su aktualna, a zapis potpun (autor, naslov, izdanje, izdavač, godina).

**K15. Zadatak je rješiv i razina je poštena.** **Tekst zadatka** sadrži sve
podatke i pretpostavke potrebne za rješenje; **Traži se** je jednoznačan i za
alternativna stanja navodi na koje se stanje odnosi. Razina T1–T4 odgovara
stvarnoj odluci studenta prema [protokolu](../protokol_prerade_zadataka_i_skica.md#3-strukturne-granice-i-razine),
a ne duljini računa. Naputak usmjerava, a ne rješava.

**K16. Primjena iz obje struke.** Primjeri iz brodogradnje i strojarstva imaju
vjerodostojne dimenzije, opterećenja i radne točke. Nastavni model jasno se
razlikuje od konstrukcijske, sigurnosne ili normativne ocjene. Ponovna pojava
lajtmotiva navodi što se iz ranijeg modela zadržava i koja fizika ulazi
([kurikularna matrica](kurikularna_matrica.md#tri-uzdužna-lajtmotiva)).

## Izvor pravila

| Pravilo | Izvor |
| --- | --- |
| K1 | AGENTS.md (ne objavljivati internu izradu), završna recenzija 16. 10. 2026. (V9, P3) |
| K2 | dosadašnja praksa knjige, urednički stil („obraćamo se u jednini”) |
| K3, K4, K9 | uvedeno ovim dokumentom prema konvencijama znanstvenih radova autorske skupine; mjere izmjerene 8. 11. 2026. |
| K5, K6, K7, K8 | urednički stil, odluke od 12., 14. i 16. 10. 2026., potvrđeno nazivlje (oplakan, 21. 10. 2026.) |
| K10 | završna recenzija 16. 10. 2026. (R1–R8), autorski ugovor (napomene uz skice) |
| K11, K13, K15 | autorski ugovor, kurikularna matrica, protokol prerade |
| K12 | autorski ugovor, završna recenzija (V2) |
| K14 | protokol stručne recenzije (empirijski pragovi), završna recenzija (V8) |
| K16 | protokol stručne recenzije (primjenski recenzent), kurikularna matrica |

## Provjera prije predaje

Iz korijena repozitorija:

```powershell
python tools/prirucnik_stats.py                 # profil po poglavljima: duljina rečenica, formule, P/Z, nalazi po pravilu
python tools/prirucnik_stats.py --nalazi        # svaki nalaz K1, K3, K4, K5, K7, K8, K12, K13 s retkom i prijedlogom
python tools/prirucnik_stats.py --nacrt source/uNN_….md   # obrnuti nacrt jednog poglavlja
python tools/prirucnik_stats.py --usporedi HEAD source/uNN_….md   # nakon svake prerade: brojevi, ID-jevi, nijekanja, ograde
```

Alat nalazi oblike, ne značenje; za K5 prepoznaje samo poznate engleske izraze. Pravila K2, K5, K6, K9, K10, K11, K14, K15 i
K16 traže čitanje. `--usporedi` pokazuje promijenjene rečenice s brojem,
nijekanjem, ogradom ili poredbom, ali ne dokazuje da je značenje sačuvano.
Strukturu, brojeve i prikaz i dalje provjeravaju `tools/audit_publication.py`,
`tools/verify_all.py`, `tools/qa_audit.py`, `tools/audit_pdf_layout.py` i puni
objavni CI iz `scripts/check_publication.py`.

### Stanje 8. studenoga 2026.

Mjere su orijentacija za usporedbu nakon izmjena, a ne cilj. Prvo mjerenje
(commit `49e2304`) našlo je tri naslova zadataka u obliku pitanja, šest popisa
brojeva sa zarezom u formulama, sedam engleskih izraza bez „engl.” i u dodatku C
nizove pogrešaka od 57 do 101 riječi u jednoj rečenici. Ti su nalazi ispravljeni
isti dan; tablica prikazuje stanje nakon ispravka.

| Mjera | Poglavlja 1–15 | Dodatci |
| --- | --- | --- |
| Prosječna duljina rečenice | 13,3–15,3 riječi | 12,2–17,6 (dodatak C prije: 25,7) |
| Rečenice iznad 30 riječi | 1,1–4,3 % | najviše 1,0 % |
| Rečenice iznad 40 riječi | 17 (pog. 3, 4, 6, 7, 8, 11, 12, 14, 15) | 1 u dodatku D |
| Istaknute formule | 784, sve numerirane | završna recenzija: referencirano oko 49 (V1) |
| Nalazi alata K1, K4, K5, K7, K8, K12, K13 | 0 | 0 |

## Oznake težine nalaza

Recenzije i trijaža koriste ljestvicu iz
[protokola stručne recenzije](protokol_strucne_recenzije.md), proširenu
neobveznom razinom:

| Oznaka | Značenje | Predaja Povjerenstvu |
| --- | --- | --- |
| P0 | pogrešan ili opasan zaključak (fizika, predznak, broj, sigurnost) | ne bez ispravka |
| P1 | znanstveno ili pedagoški bitna pogreška: netočna tvrdnja, nerješiv zadatak, nedefinirana veličina, kršenje ugovora | ne bez ispravka |
| P2 | jasnoća, stil, dosljednost, manji tehnički nedostatak | ispraviti ako je jeftino |
| P3 | prijedlog ili stvar ukusa | autorica odlučuje |

Završna recenzija od 16. 10. 2026. koristila je P1–P3 s pomaknutim značenjem;
njezin P1 odgovara ovdje P0 ili P1.

## Postupak

- **Prije restrukturiranja matrica ishoda.** Prije spajanja, premještanja ili
  brisanja odjeljaka poglavlja zapiši za taj red kurikularne matrice gdje je
  svaki od šest obveznih elemenata (izvod, riješeni primjer s neovisnom
  provjerom, konceptualno pitanje, samostalni zadatak, granica modela, numerički
  pokus) i u kojem je stanju. Autorica odobrava prijedlog premještanja.
- **Nakon svake prerade provjera značenja.** Pročitaj cijeli
  `git diff --word-diff`, pokreni `prirucnik_stats.py --usporedi` prema stanju
  prije prerade i u poruci commita navedi svaki broj koji je nestao iz teksta i
  kamo je otišao. Nakon izmjene brojeva vrijede koraci iz
  [protokola](../protokol_prerade_zadataka_i_skica.md#7-redoslijed-provjera).
- **Prije predaje recenzentima neovisno čitanje.** Svježi agenti bez konteksta
  pisanja čitaju PDF prema uputama iz skilla, a autorica razvrstava nalaze.
  Nijedan se nalaz ne provodi automatski. Agentsko čitanje ne zamjenjuje
  imenovane recenzente ni [studentski pilot](protokol_studentskog_pilota.md).
