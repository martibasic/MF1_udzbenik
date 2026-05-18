# Evidencija zadataka iz skripte

## Svrha dokumenta

Ovo je prvi bazni inventar svih zadataka iz postojece skripte. On namjerno dolazi prije unosa zadataka iz foldera `Vjezbe_530_540_150` i prije dodatnih izvora.

## Status baze

- source_layer: `skripta`
- obuhvat: `vjezba_01.qmd` do `vjezba_13.qmd`
- stvarni broj zadatkovnih jedinica: `106`
- broj heading-blokova tipa `### Zadatak ...`: `104`
- dodatne skrivene zadatkovne jedinice unutar spojenih blokova: `Z95`, `Z101`

## Pravila ove evidencije

1. `inventory_id` je jedinstveni identifikator evidencije i rjesava probleme dvostruke ili resetirane numeracije.
2. `legacy_ref` cuva izvornu oznaku iz skripte.
3. `preliminarni_cilj` je radna oznaka prema trenutnom planu knjige, ne konacna presuda za svaki zadatak.
4. `status` je polje zavrsne sinkronizacije: `validirano` oznacava obranjiv javni `1:1` prijenos, a preostalo `nije_uneseno` nakon closure-prolaza oznacava svjesnu urednicku odluku da donor nije prenesen kao zaseban javni `1:1` zadatak u trenutnom udzbeniku.

## Prvi potvrdeni javni prijenosi nakon buildout prolaza

Ovaj dokument je krenuo kao bazni inventar, ali vise nije tocno da su sve stavke u istom statusu. U prvom uskom sync-prolazu javno su potvrdene sljedece prerade iz skriptnog sloja:

1. `v01_z01` -> javna prerada u `U01` kao WE `Servisna hidraulicna dizalica`
2. `v01_z02` -> javna prerada u `U01` kao WE `Klip, uljni stupac i manometarsko ocitanje`
3. `v03_z23` -> javna prerada u `U03` kao WE `Diferencijalni manometar izmedu slatke i morske vode`
4. `v03_z25` -> javna prerada u `U03` kao WE `Ravnoteza klipa i tlak u dvjema komorama`
5. `v05_z41` -> javna prerada u `U05` kao WE `Vertikalna pravokutna zaklopka ispod slobodne povrsine`
6. `v06_z50` -> javna prerada u `U06` kao WE `Potopljena cetvrtina kruga`
7. `v08_z70` -> javna prerada u `U08` kao WE `Voda struji kroz difuzor`
8. `v08_z71` -> javna prerada u `U08` kao WE `Komora za mjesanje s dva ulaza i jednim izlazom`
9. `v09_z76` -> javna prerada u `U09` kao WE `Domet slobodnog mlaza iz velikog spremnika`
10. `v09_z79` -> javna prerada u `U09` kao WE `Pad statickog tlaka u konfuzoru ventilacijskog kanala`
11. `v10_z90` -> javna prerada u `U10` kao WE `Pitot-staticka cijev u struji vode`
12. `v11_z102` -> javna prerada u `U11` kao WE `Mlaz vode na mirnu ravnu plocu`
13. `v13_z124` -> javna prerada u `U13` kao WE `Raspodjela ukupnog protoka u dvjema paralelnim granama`
14. `v03_z32` -> javna prerada u `U04` kao WE `Otvoreni spremnik na laboratorijskim kolicima`

## Zavrsni closure-prolaz bez laznih `1:1` veza

Ovaj inventar sada daje i konacnu urednicku presudu za preostale rubne veze. Preostalo `status: nije_uneseno` nakon ovog closure-prolaza vise ne znaci dodatni backlog, nego svjesno zakljucenu odluku da donor nije prenesen kao zaseban javni `1:1` zadatak u trenutnom udzbeniku.

1. `U04`: kao sigurna veza potvrden je `v03_z32`, dok se `v03_z31`, `v03_z33` i `v04_z34-v04_z39` zakljucuju kao nepodudarni `1:1` donori; danasnji javni `U04` vec pokriva taj prostor kroz jedan skriptno potvrden primjer i dva urednicki samostalna rubna `WE`-a.
2. `U07`: ni nakon dodavanja dvafluidnog modula kandidati `v03_z30`, `v06_z54`, `v06_z55` i `v07_z01-v07_z02` ne prelaze prag za `validirano`; blok se zakljucuje kao tematska granica uzgona, stabilnosti i zakrivljenih ploha bez ciste skriptne `1:1` potvrde.
3. `U12`: skriptni zadaci o mlazu, sili i potisku ostaju metodicki srodni, ali ne i dovoljno bliski trenutnim javnim primjerima za automatski `1:1` sync; taj korpus se zatvara kao tematski pokriven bez zasebne task-level potvrde.
4. `U13`: kao sigurna skriptna veza i dalje vrijedi `v13_z124`, dok se `v13_z121-v13_z123` zakljucuju kao ne-`1:1` varijante; novi javni servisni ispust zatvara treci sloj, ali ne pretvara ventilacijski kanal, difuzor ni `spremnik-spremnik` zadatak u skriptni `migration_status`.
5. `U10`: dodatni pregled potvrduje da javni `WE` o linijskim i lokalnim gubicima ostaje urednicki kompozit, pa se `v10_z88`, `v10_z93` i tlakna grana oko `v09_z82` zatvaraju kao metodicki srodni, ali ne i `1:1` prijenosi.
6. `U06/U07`: granicni kandidati `v06_z54`, `v06_z55`, `v07_z01` i `v07_z02` zakljucuju se kao tematski prijelaz izmedu zakrivljenih ploha i uzgona; `U06` ostaje sigurno vezan uz `v06_z50`, a `U07` uz vlastite javne urednicke primjere.
7. `U03`: osim `v03_z23` i `v03_z25`, preostali zadaci iz bloka `v02_z19-v03_z29` zatvaraju se kao tematski bliski, ali ne-`1:1` donori jer uvode viseslojne spremnike, tezinu zraka, nagnute i visefluidne manometre ili spoj idealnog plina i manometrije koji nemaju zaseban javni pandan.
8. `U05`: nakon pregleda `v05_z42-v05_z48` preostali kandidati zatvaraju se kao varijantni korpus ravnih ploha; javni `U05` ostaje zakljucan na potvrdenoj pravokutnoj zaklopci i projektnom primjeru s ukrutama.
9. `U08`: blok `v08_z72-v08_z75` zakljucuje se kao skup rezervnih kontinuitetskih scenarija; danasnji javni `U08` `1:1` zatvara samo difuzor i komoru za mijesanje, a spremnici s akumulacijom, perforirani tunel i koaksijalno mjesanje ostaju izvan task-level synca.
10. `U01-U02`, `U09` i `U11`: ondje vec postoje potvrdene javne jezgre, a preostali donori bez `validirano` oznake zakljucuju se kao nepodudarne varijante, siri teorijski blokovi ili drukcije geometrijske scene, ne kao otvorene veze.

## Kljuicne anomalije koje treba cuvati tijekom migracije

1. `vjezba_04.qmd` i `vjezba_05.qmd` obje koriste `Z37-Z39`, pa `legacy_ref` sam po sebi nije jedinstven.
2. `vjezba_07.qmd` resetira numeraciju na `Z1` i `Z2`, iako su ti brojevi vec zauzeti u `vjezba_01.qmd`.
3. `vjezba_10.qmd` sadrzi spojeni blok `Z94-Z95`, ali su to dvije odvojene zadatkovne jedinice.
4. `vjezba_11.qmd` sadrzi spojeni blok `Z100-Z101`, ali su to dvije odvojene zadatkovne jedinice.
5. U skripti postoje brojcane praznine i prekidi numeracije; one se ne smiju "ispravljati" u ovoj fazi, nego samo evidentirati.

## Popis po izvornoj datoteci

### vjezba_01.qmd

- `v01_z01` | legacy_ref: `Z1` | naslov: `Rucna hidraulicka dizalica` | preliminarni_cilj: `U01` | status: `validirano` | napomena: `javna prerada potvrdena u U01 WE Servisna hidraulicna dizalica`
- `v01_z02` | legacy_ref: `Z2` | naslov: `Tezina klipa i manometarski tlak` | preliminarni_cilj: `U01` | status: `validirano` | napomena: `javna prerada potvrdena u U01 WE Klip, uljni stupac i manometarsko ocitanje`
- `v01_z03` | legacy_ref: `Z3` | naslov: `Toplinsko sirenje vode i staklene posude` | preliminarni_cilj: `U01` | status: `nije_uneseno`
- `v01_z04` | legacy_ref: `Z4` | naslov: `Modul stlacivosti tekucine` | preliminarni_cilj: `U01` | status: `nije_uneseno`
- `v01_z05` | legacy_ref: `Z5` | naslov: `Gustoca oceana na velikim dubinama` | preliminarni_cilj: `U01` | status: `nije_uneseno`
- `v01_z06` | legacy_ref: `Z6` | naslov: `Profil brzine u cijevi` | preliminarni_cilj: `U02` | status: `nije_uneseno`
- `v01_z07` | legacy_ref: `Z7` | naslov: `Blok na kosini` | preliminarni_cilj: `U02` | status: `nije_uneseno`
- `v01_z08` | legacy_ref: `Z8` | naslov: `Sila na rotirajuce vratilo` | preliminarni_cilj: `U02` | status: `nije_uneseno`
- `v01_z09` | legacy_ref: `Z9` | naslov: `Utjecaj temperature na silu pomicanja klipa` | preliminarni_cilj: `U02` | status: `nije_uneseno`

### vjezba_02.qmd

- `v02_z10` | legacy_ref: `Z10` | naslov: `Okretni moment na krnjem stosču` | preliminarni_cilj: `U02` | status: `nije_uneseno`
- `v02_z11` | legacy_ref: `Z11` | naslov: `Proracun snage rotacije` | preliminarni_cilj: `U02` | status: `nije_uneseno`
- `v02_z12` | legacy_ref: `Z12` | naslov: `Kapilarni porast (Voda vs Ziva)` | preliminarni_cilj: `U02` | status: `nije_uneseno`
- `v02_z13` | legacy_ref: `Z13` | naslov: `Young-Laplaceov zakon` | preliminarni_cilj: `U02` | status: `nije_uneseno`
- `v02_z14` | legacy_ref: `Z14` | naslov: `Sila na staklenu cijev` | preliminarni_cilj: `U02` | status: `nije_uneseno`
- `v02_z15` | legacy_ref: `Z15` | naslov: `Plutajuca kuglica` | preliminarni_cilj: `U07` | status: `nije_uneseno` | napomena: `preporuceno preseljenje iz U02 u U07`
- `v02_z16` | legacy_ref: `Z16` | naslov: `Vizualizacija kapilarne greske` | preliminarni_cilj: `U02` | status: `nije_uneseno`
- `v02_z17` | legacy_ref: `Z17` | naslov: `Kapilarni porast kerozina` | preliminarni_cilj: `U02` | status: `nije_uneseno`
- `v02_z18` | legacy_ref: `Z18` | naslov: `Transport vode u biljkama` | preliminarni_cilj: `U02` | status: `nije_uneseno`
- `v02_z19` | legacy_ref: `Z19` | naslov: `Tlak u viseslojnom spremniku` | preliminarni_cilj: `U03` | status: `nije_uneseno` | napomena: `preporuceno preseljenje iz U02 u U03`
- `v02_z19` | legacy_ref: `Z19` | naslov: `Tlak u viseslojnom spremniku` | preliminarni_cilj: `U03` | status: `nije_uneseno` | napomena: `preporuceno preseljenje iz U02 u U03; trenutni U03 nema javni WE s viseslojnim spremnikom i trazenom relativnom gustocom ulja`
- `v02_z20` | legacy_ref: `Z20` | naslov: `Intravenozna infuzija` | preliminarni_cilj: `U03` | status: `nije_uneseno` | napomena: `preporuceno preseljenje iz U02 u U03; medicinski hidrostatski primjer nema 1:1 javnu preradu u danasnjem U03`
- `v02_z21` | legacy_ref: `Z21` | naslov: `Utjecaj tezine zraka` | preliminarni_cilj: `U03` | status: `nije_uneseno` | napomena: `preporuceno preseljenje iz U02 u U03; trenutni U03 nema javni WE koji eksplicitno vodi korekciju zbog tezine zraka`
- `v02_z22` | legacy_ref: `Z22` | naslov: `Manometar na planini` | preliminarni_cilj: `U03` | status: `nije_uneseno` | napomena: `preporuceno preseljenje iz U02 u U03; planinski visefluidni manometar ostaje samo tematski blizak danasnjem U03`

### vjezba_03.qmd

- `v03_z23` | legacy_ref: `Z23` | naslov: `Diferencijalni manometar s morskom vodom` | preliminarni_cilj: `U03` | status: `validirano` | napomena: `javna prerada potvrdena u U03 WE Diferencijalni manometar izmedu slatke i morske vode`
- `v03_z24` | legacy_ref: `Z24` | naslov: `Manometar s vise fluida (Prirodni plin)` | preliminarni_cilj: `U03` | status: `nije_uneseno` | napomena: `visefluidni manometar s prirodnim plinom nije 1:1 s javnim WE o slatkoj i morskoj vodi`
- `v03_z25` | legacy_ref: `Z25` | naslov: `Ravnoteza klipa i tlak u komorama` | preliminarni_cilj: `U03` | status: `validirano` | napomena: `javna prerada potvrdena u U03 WE Ravnoteza klipa i tlak u dvjema komorama`
- `v03_z26` | legacy_ref: `Z26` | naslov: `Nagnuti zivin manometar` | preliminarni_cilj: `U03` | status: `nije_uneseno` | napomena: `nagnuti zivin manometar trazi drugu geometriju i osjetljivost mjerenja nego trenutni javni U03`
- `v03_z27` | legacy_ref: `Z27` | naslov: `Vise-fluidni spremnik i U-cijev` | preliminarni_cilj: `U03` | status: `nije_uneseno` | napomena: `visefluidni spremnik i ekvivalentna visina zive nisu javno preradeni kao zaseban U03 primjer`
- `v03_z28` | legacy_ref: `Z28` | naslov: `Solarna jezera (nelinearna gustoca)` | preliminarni_cilj: `U03` | status: `nije_uneseno` | napomena: `nelinearna gustoca i integral tlaka nemaju 1:1 javni pandan u trenutnom U03`
- `v03_z29` | legacy_ref: `Z29` | naslov: `Naftovod, spremnik zraka i manometar` | preliminarni_cilj: `U03` | status: `nije_uneseno` | napomena: `spoj idealnog plina i manometrije ostaje urednicki siri lanac od danasnjih javnih U03 WE`
- `v03_z30` | legacy_ref: `Z30` | naslov: `Areometar` | preliminarni_cilj: `U07` | status: `nije_uneseno`
- `v03_z31` | legacy_ref: `Z31` | naslov: `Ubrzanje spremnika - Orijentacija` | preliminarni_cilj: `U04` | status: `nije_uneseno` | napomena: `trenutni U04 nema cisti orijentacijski zadatak s trazenim maksimalnim punjenjem spremnika`
- `v03_z32` | legacy_ref: `Z32` | naslov: `Otvoreni ubrzani spremnik: tlak na dnu` | preliminarni_cilj: `U04` | status: `validirano` | napomena: `javna prerada potvrdena u U04 WE Otvoreni spremnik na laboratorijskim kolicima`
- `v03_z33` | legacy_ref: `Z33` | naslov: `Cisterna mlijeka: tlak u zatvorenom spremniku` | preliminarni_cilj: `U04` | status: `nije_uneseno` | napomena: `zatvoreni spremnik bez slobodne povrsine nije 1:1 s trenutnim javnim primjerima u U04`

### vjezba_04.qmd

- `v04_z34` | legacy_ref: `Z34` | naslov: `Kolica na kosini` | preliminarni_cilj: `U04` | status: `nije_uneseno`
- `v04_z35` | legacy_ref: `Z35` | naslov: `Rotirajuci cilindar (Kriticni broj okretaja)` | preliminarni_cilj: `U04` | status: `nije_uneseno`
- `v04_z36` | legacy_ref: `Z36` | naslov: `Cilindricni spremnik - Benzin (Kombinirano ubrzanje)` | preliminarni_cilj: `U04` | status: `nije_uneseno`
- `v04_z37` | legacy_ref: `Z37` | naslov: `Rotirajuca U-cijev s dva fluida` | preliminarni_cilj: `U04` | status: `nije_uneseno` | napomena: `legacy_ref se preklapa s vjezba_05`
- `v04_z38` | legacy_ref: `Z38` | naslov: `Rotirajuci spremnik (Mokro vs. Suho dno)` | preliminarni_cilj: `U04` | status: `nije_uneseno` | napomena: `legacy_ref se preklapa s vjezba_05`
- `v04_z39` | legacy_ref: `Z39` | naslov: `Nakoseni spremnik koji rotira i ubrzava` | preliminarni_cilj: `U04` | status: `nije_uneseno` | napomena: `legacy_ref se preklapa s vjezba_05`

### vjezba_05.qmd

- `v05_z37` | legacy_ref: `Z37` | naslov: `Vertikalni trokut s vrhom na povrsini` | preliminarni_cilj: `U05` | status: `nije_uneseno` | napomena: `legacy_ref se preklapa s vjezba_04`
- `v05_z38` | legacy_ref: `Z38` | naslov: `Trokut uronjen na dubini a` | preliminarni_cilj: `U05` | status: `nije_uneseno` | napomena: `legacy_ref se preklapa s vjezba_04`
- `v05_z39` | legacy_ref: `Z39` | naslov: `Krug uronjen s gornjim rubom na povrsini` | preliminarni_cilj: `U05` | status: `nije_uneseno` | napomena: `legacy_ref se preklapa s vjezba_04`
- `v05_z40` | legacy_ref: `Z40` | naslov: `Polukrug s tetivom na povrsini` | preliminarni_cilj: `U05` | status: `nije_uneseno`
- `v05_z41` | legacy_ref: `Z41` | naslov: `Pravokutna vertikalna zaklopka` | preliminarni_cilj: `U05` | status: `validirano` | napomena: `javna prerada potvrdena u U05 WE Vertikalna pravokutna zaklopka ispod slobodne povrsine`
- `v05_z42` | legacy_ref: `Z42` | naslov: `Nagnuta zaklopka` | preliminarni_cilj: `U05` | status: `nije_uneseno` | napomena: `trenutni U05 nema javni WE otvaranja nagnute zaklopke momentnom ravnotezom`
- `v05_z43` | legacy_ref: `Z43` | naslov: `Brana s nagnutom stjenkom` | preliminarni_cilj: `U05` | status: `nije_uneseno` | napomena: `brana s nagnutom stjenkom i trazenim hvatistem nije 1:1 s danasnjim javnim U05`
- `v05_z44` | legacy_ref: `Z44` | naslov: `Brana s atmosferskim pretlakom` | preliminarni_cilj: `U05` | status: `nije_uneseno` | napomena: `atmosferski pretlak kao dodatna nadomjesna visina nije zasebno javno zatvoren u U05`
- `v05_z45` | legacy_ref: `Z45` | naslov: `Vertikalna pravokutna zaklopka (Integral)` | preliminarni_cilj: `U05` | status: `nije_uneseno` | napomena: `ista je obitelj kao validirani v05_z41, ali integralna varijanta s drugim postavom zasad nije zaseban 1:1 javni prijenos`
- `v05_z46` | legacy_ref: `Z46` | naslov: `Vertikalna trokutna zaklopka (Integral)` | preliminarni_cilj: `U05` | status: `nije_uneseno` | napomena: `vertikalna trokutna integralna varijanta nema odgovarajuci javni WE u U05`
- `v05_z47` | legacy_ref: `Z47` | naslov: `Nakosena pravokutna zaklopka (30 stupnjeva)` | preliminarni_cilj: `U05` | status: `nije_uneseno` | napomena: `nakosena pravokutna zaklopka s dubinom vrha i kutom 30 stupnjeva nije zasebno javno preradena`
- `v05_z48` | legacy_ref: `Z48` | naslov: `Asimetricna trokutna zaklopka` | preliminarni_cilj: `U05` | status: `nije_uneseno` | napomena: `asimetricna trokutna zaklopka i bocni pomak hvatiste ostaju izvan trenutnog javnog U05`

### vjezba_06.qmd

- `v06_z49` | legacy_ref: `Z49` | naslov: `Cilindar kao automatska zaklopka (CENGEL 3.9)` | preliminarni_cilj: `U06` | status: `nije_uneseno` | napomena: `trenutni drugi U06 WE nije cista prerada cilindarske zaklopke nego siri urednicki zadatak s ravnim segmentom, zakrivljenim rubom i momentnom ravnotezom`
- `v06_z50` | legacy_ref: `Z50` | naslov: `Potopljena cetvrtina kruga (2500 SPFM - 5.1)` | preliminarni_cilj: `U06` | status: `validirano` | napomena: `javna prerada potvrdena u U06 WE Potopljena cetvrtina kruga`
- `v06_z51` | legacy_ref: `Z51` | naslov: `Potopljena cetvrtina kruga (voda s desne strane)` | preliminarni_cilj: `U06` | status: `nije_uneseno`
- `v06_z52` | legacy_ref: `Z52` | naslov: `Potopljena zaklopka (sestina isjecka kruga)` | preliminarni_cilj: `U06` | status: `nije_uneseno`
- `v06_z53` | legacy_ref: `Z53` | naslov: `Elasticni balon i promjena sile u uzetu` | preliminarni_cilj: `U06` | status: `nije_uneseno`
- `v06_z54` | legacy_ref: `Z54` | naslov: `Ledenjak (volumni udio i stabilnost)` | preliminarni_cilj: `REV-U06/U07` | status: `nije_uneseno` | napomena: `sadrzajno granica izmedu zakrivljenih ploha i uzgona/stabilnosti`
- `v06_z55` | legacy_ref: `Z55` | naslov: `Potopljeni naopaki cilindar (CENGEL 3.151)` | preliminarni_cilj: `REV-U06/U07` | status: `nije_uneseno` | napomena: `sadrzajno granica izmedu zakrivljenih ploha i uzgona`

### vjezba_07.qmd

- `v07_z01` | legacy_ref: `Z1` | naslov: `Cilindar na granici fluida` | preliminarni_cilj: `REV-U06/U07` | status: `nije_uneseno` | napomena: `reset numeracije; thematic mismatch s trenutnim naslovom U07`
- `v07_z02` | legacy_ref: `Z2` | naslov: `Polu-cilindricni zatvarac (60 stupnjeva luk)` | preliminarni_cilj: `REV-U06/U07` | status: `nije_uneseno` | napomena: `reset numeracije; thematic mismatch s trenutnim naslovom U07`

### vjezba_08.qmd

- `v08_z70` | legacy_ref: `Z70` | naslov: `Voda struji kroz difuzor` | preliminarni_cilj: `U08` | status: `validirano` | napomena: `javna prerada potvrdena u U08 WE Voda struji kroz difuzor`
- `v08_z71` | legacy_ref: `Z71` | naslov: `Voda ustrujava u spremnik za mijesanje` | preliminarni_cilj: `U08` | status: `validirano` | napomena: `javna prerada potvrdena u U08 WE Komora za mjesanje s dva ulaza i jednim izlazom`
- `v08_z72` | legacy_ref: `Z72` | naslov: `Voda ustrujava u cilindricni spremnik` | preliminarni_cilj: `U08` | status: `nije_uneseno` | napomena: `trenutni U08 nema javni WE sa spremnikom, promjenom razine i odzracivanjem zraka`
- `v08_z73` | legacy_ref: `Z73` | naslov: `U spremnik sa slike ustrujava 10` | preliminarni_cilj: `U08` | status: `nije_uneseno` | napomena: `ulaz vode, izlaz benzina i bilanca zraka nisu 1:1 s javnom komorom za mijesanje u U08`
- `v08_z74` | legacy_ref: `Z74` | naslov: `Ispitne stjenke zracnog tunela izradene su od perforiranog materijala` | preliminarni_cilj: `U08` | status: `nije_uneseno` | napomena: `perforirani zracni tunel i raspodijeljeni odsis ostaju poseban kontinuitetski scenarij bez javnog WE u U08`
- `v08_z75` | legacy_ref: `Z75` | naslov: `Pumpa ubrizgava vodu` | preliminarni_cilj: `U08` | status: `nije_uneseno` | napomena: `koaksijalno mijesanje dvaju tokova dijeli motiv mijesanja, ali nije isti javni primjer kao komora s dva ulaza i jednim izlazom`

### vjezba_09.qmd

- `v09_z76` | legacy_ref: `Z76` | naslov: `Domet slobodnog mlaza` | preliminarni_cilj: `U09` | status: `validirano` | napomena: `javna prerada potvrdena u U09 WE Domet slobodnog mlaza iz velikog spremnika`
- `v09_z77` | legacy_ref: `Z77` | naslov: `Srednja brzina laminarnog toka` | preliminarni_cilj: `U09` | status: `nije_uneseno`
- `v09_z78` | legacy_ref: `Z78` | naslov: `Difuzor bez gubitaka` | preliminarni_cilj: `U09` | status: `nije_uneseno`
- `v09_z79` | legacy_ref: `Z79` | naslov: `Pad tlaka u konfuzoru` | preliminarni_cilj: `U09` | status: `validirano` | napomena: `javna prerada potvrdena u U09 WE Pad statickog tlaka u konfuzoru ventilacijskog kanala`
- `v09_z80` | legacy_ref: `Z80` | naslov: `Usisna visina pumpe` | preliminarni_cilj: `U10` | status: `nije_uneseno` | napomena: `preporuceno preseljenje iz U09 u U10`
- `v09_z81` | legacy_ref: `Z81` | naslov: `Ukupna visina dobave pumpe` | preliminarni_cilj: `U10` | status: `nije_uneseno` | napomena: `preporuceno preseljenje iz U09 u U10`
- `v09_z82` | legacy_ref: `Z82` | naslov: `Pad tlaka u cijevi` | preliminarni_cilj: `U10` | status: `nije_uneseno` | napomena: `preporuceno preseljenje iz U09 u U10; nije 1:1 s javnim U10 jer koristi drugu geometriju, drugi fluid i tlaknu bilancu izmedu dvaju presjeka`
- `v09_z83` | legacy_ref: `Z83` | naslov: `Protok kroz sifon s gubicima` | preliminarni_cilj: `U10` | status: `nije_uneseno` | napomena: `preporuceno preseljenje iz U09 u U10`
- `v09_z84` | legacy_ref: `Z84` | naslov: `Apsolutni tlak u vrhu sifona` | preliminarni_cilj: `U10` | status: `nije_uneseno` | napomena: `preporuceno preseljenje iz U09 u U10`
- `v09_z85` | legacy_ref: `Z85` | naslov: `Dinamika sifona i kavitacija` | preliminarni_cilj: `U10` | status: `nije_uneseno` | napomena: `preporuceno preseljenje iz U09 u U10`

### vjezba_10.qmd

- `v10_z86` | legacy_ref: `Z86` | naslov: `Sifon s realnim fluidom` | preliminarni_cilj: `U10` | status: `nije_uneseno`
- `v10_z87` | legacy_ref: `Z87` | naslov: `Visina mlaza iz sapnice` | preliminarni_cilj: `U10` | status: `nije_uneseno`
- `v10_z88` | legacy_ref: `Z88` | naslov: `Linijski gubici u cijevi` | preliminarni_cilj: `U10` | status: `nije_uneseno` | napomena: `javni U10 WE koristi isti lanac, ali ga siri i na lokalne gubitke pa zasad nije cista 1:1 prerada`
- `v10_z89` | legacy_ref: `Z89` | naslov: `Istjecanje iz velikog spremnika` | preliminarni_cilj: `U10` | status: `nije_uneseno`
- `v10_z90` | legacy_ref: `Z90` | naslov: `Pitot-staticka cijev (Prandtl)` | preliminarni_cilj: `U10` | status: `validirano` | napomena: `javna prerada potvrdena u U10 WE Pitot-staticka cijev u struji vode`
- `v10_z91` | legacy_ref: `Z91` | naslov: `Stratificirani visefazni spremnik - istjecanje` | preliminarni_cilj: `U10` | status: `nije_uneseno`
- `v10_z92` | legacy_ref: `Z92` | naslov: `Protocna sapnica u cijevi` | preliminarni_cilj: `U10` | status: `nije_uneseno`
- `v10_z93` | legacy_ref: `Z93` | naslov: `Lokalni gubitak (Koljeno)` | preliminarni_cilj: `U10` | status: `nije_uneseno` | napomena: `javni U10 WE ukljucuje lokalne gubitke, ali ne kao zasebni 1:1 zadatak za jedno koljeno`
- `v10_z94` | legacy_ref: `Z94` | naslov: `Venturi cijev i podizanje tekucine` | preliminarni_cilj: `U10` | status: `nije_uneseno` | napomena: `izvuceno iz spojenog bloka Z94-Z95`
- `v10_z95` | legacy_ref: `Z95` | naslov: `Cjevovod s tri koljena i ventilom spaja dva spremnika` | preliminarni_cilj: `U10/U13 review` | status: `nije_uneseno` | napomena: `skriven unutar spojenog bloka Z94-Z95`

### vjezba_11.qmd

- `v11_z97` | legacy_ref: `Z97` | naslov: `Vrijeme praznjenja spremnika` | preliminarni_cilj: `U11` | status: `nije_uneseno`
- `v11_z98` | legacy_ref: `Z98` | naslov: `Kinematika dva mlaza` | preliminarni_cilj: `U11` | status: `nije_uneseno`
- `v11_z99` | legacy_ref: `Z99` | naslov: `Rotirajuci spremnik s cijevi` | preliminarni_cilj: `U11` | status: `nije_uneseno`
- `v11_z100` | legacy_ref: `Z100` | naslov: `Sila na koljeno cijevi (30 stupnjeva)` | preliminarni_cilj: `U11` | status: `nije_uneseno` | napomena: `izvuceno iz spojenog bloka Z100-Z101`
- `v11_z101` | legacy_ref: `Z101` | naslov: `Sila na koljeno cijevi (180 stupnjeva)` | preliminarni_cilj: `U11` | status: `nije_uneseno` | napomena: `skriven unutar spojenog bloka Z100-Z101`
- `v11_z102` | legacy_ref: `Z102` | naslov: `Mlaz na plocu` | preliminarni_cilj: `U11` | status: `validirano` | napomena: `javna prerada potvrdena u U11 WE Mlaz vode na mirnu ravnu plocu`
- `v11_z103` | legacy_ref: `Z103` | naslov: `Vjetroturbina` | preliminarni_cilj: `U11` | status: `nije_uneseno`

### vjezba_12.qmd

- `v12_z104` | legacy_ref: `Z104` | naslov: `Potisak satelita` | preliminarni_cilj: `U12` | status: `nije_uneseno`
- `v12_z105` | legacy_ref: `Z105` | naslov: `Sila na prirubnici slavine` | preliminarni_cilj: `U12` | status: `nije_uneseno`
- `v12_z106` | legacy_ref: `Z106` | naslov: `Konzolni cjevovod - Moment savijanja` | preliminarni_cilj: `U12` | status: `nije_uneseno`
- `v12_z107` | legacy_ref: `Z107` | naslov: `Snaga rotirajuce prskalice` | preliminarni_cilj: `U12` | status: `nije_uneseno`
- `v12_z108` | legacy_ref: `Z108` | naslov: `Komercijalne vjetroturbine` | preliminarni_cilj: `U12` | status: `nije_uneseno`
- `v12_z109` | legacy_ref: `Z109` | naslov: `Snaga helikoptera` | preliminarni_cilj: `U12` | status: `nije_uneseno`
- `v12_z110` | legacy_ref: `Z110` | naslov: `Brana s razlikom razina - Sila na ustavu` | preliminarni_cilj: `U12` | status: `nije_uneseno`
- `v12_z111` | legacy_ref: `Z111` | naslov: `Peltonova turbina` | preliminarni_cilj: `U12` | status: `nije_uneseno`
- `v12_z112` | legacy_ref: `Z112` | naslov: `Flyboard dinamika` | preliminarni_cilj: `U12` | status: `nije_uneseno`

### vjezba_13.qmd

- `v13_z121` | legacy_ref: `Z121` | naslov: `Turbulentno strujanje zraka` | preliminarni_cilj: `U13` | status: `nije_uneseno` | napomena: `javni U13 WE o Reynoldsovu broju i gubicima dijeli lanac, ali nije 1:1 zbog pravokutnog ventilacijskog kanala i pada tlaka zraka`
- `v13_z122` | legacy_ref: `Z122` | naslov: `Difuzor s lokalnim gubicima` | preliminarni_cilj: `U13` | status: `nije_uneseno` | napomena: `trenutni javni U13 nema zasebni difuzor s lokalnim gubicima i trazenim izlaznim tlakom`
- `v13_z123` | legacy_ref: `Z123` | naslov: `Protok izmedu dva spremnika` | preliminarni_cilj: `U13` | status: `nije_uneseno` | napomena: `javni U13 validira paralelne grane, ne jedan vod izmedu dvaju spremnika`
- `v13_z124` | legacy_ref: `Z124` | naslov: `Paralelni cjevovodi` | preliminarni_cilj: `U13` | status: `validirano` | napomena: `javna prerada potvrdena u U13 WE Raspodjela ukupnog protoka u dvjema paralelnim granama`

## Sto slijedi nakon ove baze

1. Nad ovom datotekom treba otvoriti drugi sloj iz `private/materials/Vjezbe_530_540_150`.
2. Tek nakon toga treba dodavati zadatke iz dodatnih izvora.
3. U sljedecoj fazi treba svakoj jedinici dodijeliti `WE`, `GP`, `PO`, `CH` i `T1-T4`.