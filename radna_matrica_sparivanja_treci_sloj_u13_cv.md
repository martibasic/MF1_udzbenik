# Radna matrica sparivanja treci sloj za U13 (CV)

## Svrha dokumenta

Ovo je cetvrti radni dokument za sparivanje treceg sloja u bloku `U13`, s rubnim prijelazima prema `U10` i `U12`. Fokus je samo na bloku `CV` iz izvora `SAVAR_sesija2_RM_Bernoulli_Istjecanje_Cjevovod.md`.

## Pravilo citanja ove matrice

1. Skripta ostaje kanonski prvi zapis.
2. Drugi sloj ostaje vec zatvoren prvi sloj dopune.
3. `jedinstven` znaci da treci sloj donosi novu mrezu, novi projektni uvjet ili novu primjenu koju nizi slojevi nemaju u tom obliku.
4. `varijanta` znaci da zadatak ostaje u istoj obitelji cjevovoda, gubitaka ili radne tocke, ali s drugim trazenim parametrom ili drukcijom geometrijom.
5. `bliski_duplikat` se koristi kad novi zapis ocito konkurira istom urednickom mjestu i ne otvara dovoljno novu vrijednost.
6. `rezervni` se koristi kad je zadatak vrijedan, ali po trenutnoj urednickoj granici izlazi iz uskog jezgrenog toka `U13`.

## U13 - Cjevovodi, pumpni sustavi i rubni prijelazi

### Postojeca jezgra

- skripta: `v13_z121-v13_z124`, uz rubne pomocne parove `v10_z89-v10_z95` i `v12_z111`
- drugi sloj: `av08_01-av08_03`, uz rubne pomocne zapise `av06_01-av06_02` i `av09_01`

### Treci sloj CV - preliminarna presuda

- `CV-1` | skriptna_obitelj: `v13_z123-v13_z124` | druga_slojna_veza: `av08_03` | presuda: `jedinstven` | razlog: serijski i paralelni spoj dviju istih pumpi uvodi stvarni sustav s dvjema karakteristikama, sto nizi slojevi nemaju kao zaseban projektni motiv.
- `CV-2` | skriptna_obitelj: `v13_z123` | druga_slojna_veza: `av06_01-av06_02, av08_02-av08_03` | presuda: `jedinstven` | razlog: minimalni tlak u sustavu koji kombinira pumpu, sifon i gubitke daje jasan prijelaz izmedu cjevovoda i kavitacijskog razmisljanja.
- `CV-3` | skriptna_obitelj: `v12_z111` | druga_slojna_veza: `av08_03, av09_01` | presuda: `jedinstven` | razlog: reverzibilni agregat u pumpnom i turbinskom radu uvodi puni energetski ciklus postrojenja, a ne samo jednokratni cjevovodni proracun.
- `CV-4` | skriptna_obitelj: `nema bliskog para` | druga_slojna_veza: `nema bliskog para` | presuda: `jedinstven` | razlog: rekonstrukcija klimatizacijskog voda preko jednakog pada tlaka po duljini otvara zasebnu obitelj ekvivalentnog promjera za neokrugle presjeke.
- `CV-5` | skriptna_obitelj: `v13_z121-v13_z123` | druga_slojna_veza: `av08_01, av08_03` | presuda: `varijanta` | razlog: povecanje potrebne snage zbog vece hrapavosti i vece potraznje ostaje jezgrena obitelj gubitaka i rada pumpe.
- `CV-6` | skriptna_obitelj: `v13_z121-v13_z123` | druga_slojna_veza: `av08_01, av08_03` | presuda: `bliski_duplikat` | razlog: izvor sam ga postavlja kao isti problem kao `CV-5`, pa nova vrijednost ostaje uglavnom parametarska.
- `CV-7` | skriptna_obitelj: `v13_z121` | druga_slojna_veza: `av08_01` | presuda: `varijanta` | razlog: identifikacija pjezcane hrapavosti iz izmjerenog protoka i pada tlaka ostaje ista obitelj linijskih gubitaka, samo s obrnutim nepoznanicama.
- `CV-8` | skriptna_obitelj: `v13_z123-v13_z124` | druga_slojna_veza: `nema bliskog para` | presuda: `jedinstven` | razlog: razgranati sustav s tri spremnika i trazenom stacionarnom razinom srednjeg spremnika znacajno siri bazni blok dvaju spremnika.
- `CV-9` | skriptna_obitelj: `v13_z122` | druga_slojna_veza: `nema bliskog para` | presuda: `varijanta` | razlog: optimiranje odnosa `D/d` za minimalni lokalni gubitak ostaje u istoj obitelji difuzora i lokalnih gubitaka.
- `CV-10` | skriptna_obitelj: `nema bliskog para` | druga_slojna_veza: `nema bliskog para` | presuda: `jedinstven` | razlog: odnos protoka za tri i cetiri cijevi unutar zastitne cijevi donosi novu geometrijsku i laminarnu projektnu scenu.
- `CV-11` | skriptna_obitelj: `v13_z123-v13_z124` | druga_slojna_veza: `nema bliskog para` | presuda: `jedinstven` | razlog: stabilan nivo u trecem spremniku preko triju cjevovoda daje bogatiji balans mreze nego sto ga nose nizi slojevi.
- `CV-12` | skriptna_obitelj: `v13_z123-v13_z124` | druga_slojna_veza: `av08_03` | presuda: `jedinstven` | razlog: kombinacija akumulacijskog rezervoara, dviju trasa i jeftinije tarife uvodi ekonomsku optimizaciju koja nije prisutna u nizim slojevima.
- `CV-13` | skriptna_obitelj: `v13_z122-v13_z123` | druga_slojna_veza: `nema bliskog para` | presuda: `jedinstven` | razlog: maksimalni domet mlaza iz cjevovoda spaja cjevovodne gubitke s projektilskom kinematikom i nije samo obicni proracun protoka.
- `CV-14` | skriptna_obitelj: `nema bliskog para` | druga_slojna_veza: `nema bliskog para` | presuda: `jedinstven` | razlog: hipodermalna igla i sila na stap uvode vrlo cistu, primijenjenu viskoznu mikrocjevovodnu scenu koju baza nema.
- `CV-15` | skriptna_obitelj: `v13_z122-v13_z123` | druga_slojna_veza: `av08_03` | presuda: `varijanta` | razlog: radna tocka pumpe za vodoskok ostaje ista obitelj sustavne i pumpne karakteristike, samo s drugim izlaznim ciljem.
- `CV-16` | skriptna_obitelj: `v13_z122-v13_z123` | druga_slojna_veza: `av08_03` | presuda: `varijanta` | razlog: radna tocka pumpe za domet preljeva zadrzava isti metodski kostur kao `CV-15`, ali s drukcijim kriterijem mlaza.
- `CV-17` | skriptna_obitelj: `v12_z111, v13_z123` | druga_slojna_veza: `av09_01` | presuda: `jedinstven` | razlog: protok kroz sustav s turbinom i zadanim padom tlaka daje jasan hibridni most izmedu energetskog i cjevovodnog bloka.
- `CV-18` | skriptna_obitelj: `v13_z123` | druga_slojna_veza: `av08_03` | presuda: `varijanta` | razlog: zamjena pumpe visom dobavnom visinom i usporedba protoka ostaje izravna radna tocka sustava s novom pumpom.
- `CV-19` | skriptna_obitelj: `v12_z111, v13_z122` | druga_slojna_veza: `av09_01` | presuda: `varijanta` | razlog: difuzor ispod turbine ostaje ista rubna obitelj turbine, difuzora i gubitaka kao rezervni hibrid drugog sloja.
- `CV-20` | skriptna_obitelj: `v13_z123-v13_z124` | druga_slojna_veza: `nema bliskog para` | presuda: `bliski_duplikat` | razlog: gotovo je isti urednicki problem kao `CV-8`, samo s blagom parametrskom izmjenom razgranatog sustava.
- `CV-21` | skriptna_obitelj: `nema bliskog para` | druga_slojna_veza: `nema bliskog para` | presuda: `jedinstven` | razlog: zamjena kvadratne cijevi okruglom pri istom protoku i istoj razlici razina otvara zaseban ekvivalentni presjecni problem.
- `CV-22` | skriptna_obitelj: `nema bliskog para` | druga_slojna_veza: `nema bliskog para` | presuda: `jedinstven` | razlog: laminarno smanjenje protoka pregradom je cist analiticki problem unutarnjeg strujanja kojeg nema u nizim slojevima.
- `CV-23` | skriptna_obitelj: `v13_z124` | druga_slojna_veza: `av08_01, av08_03` | presuda: `varijanta` | razlog: dodavanje novog paralelnog cjevovoda za vecu dobavu direktno siri bazni skriptni motiv paralelnih cjevovoda.
- `CV-24` | skriptna_obitelj: `nema bliskog para` | druga_slojna_veza: `nema bliskog para` | presuda: `rezervni` | razlog: trapezni otvoreni kanal jest vrijedan, ali zasad izlazi iz usko postavljene jezgre `U13` kao poglavlja o cijevnim sustavima.
- `CV-25` | skriptna_obitelj: `nema bliskog para` | druga_slojna_veza: `nema bliskog para` | presuda: `jedinstven` | razlog: kompenzacijska posuda, klip i viskozno ulje uvode zaseban hidraulicki pogonski sklop s cjevovodnim gubicima.
- `CV-26` | skriptna_obitelj: `v12_z111, v13_z123` | druga_slojna_veza: `av09_01` | presuda: `jedinstven` | razlog: razlika razina izmedu akumulacijskog jezera i kompenzacione komore uz zadani neto pad turbine donosi novi penstockski scenarij.
- `CV-27` | skriptna_obitelj: `v10_z89-v10_z95` | druga_slojna_veza: `nema bliskog para` | presuda: `jedinstven` | razlog: vrijeme pijenja slamkom spaja kvazistacionarno praznjenje s viskoznim gubicima u vrlo pamtljivoj primjeni.
- `CV-28` | skriptna_obitelj: `nema bliskog para` | druga_slojna_veza: `nema bliskog para` | presuda: `jedinstven` | razlog: punjenje i praznjenje hidraulickog akumulatora te njegov stupanj djelovanja otvaraju zaseban sklop koji ne postoji u nizim slojevima.
- `CV-29` | skriptna_obitelj: `v13_z122-v13_z124` | druga_slojna_veza: `nema bliskog para` | presuda: `varijanta` | razlog: trazeni `K_v` za zadani protok u grani ostaje unutar obitelji lokalnih gubitaka i razgranatih cjevovoda.
- `CV-30` | skriptna_obitelj: `v13_z123` | druga_slojna_veza: `av08_03` | presuda: `varijanta` | razlog: eksplicitna karakteristika pumpe i radna tocka predstavljaju izravnu varijantu vec zatvorenog pumpnog bloka.
- `CV-31` | skriptna_obitelj: `v13_z123` | druga_slojna_veza: `nema bliskog para` | presuda: `varijanta` | razlog: trazeni izlazni promjer iz rezervoara s konstantnom razinom ostaje u istoj projektnoj obitelji zadavanja protoka i gubitaka izmedu spremnika.
- `CV-32` | skriptna_obitelj: `nema bliskog para` | druga_slojna_veza: `nema bliskog para` | presuda: `jedinstven` | razlog: hidraulicki stol povezuje mehanicko opterecenje, uljni vod i pumpne karakteristike u aplikaciju kakvu nizi slojevi nemaju.
- `CV-33` | skriptna_obitelj: `nema bliskog para` | druga_slojna_veza: `nema bliskog para` | presuda: `bliski_duplikat` | razlog: prakticki ponavlja `CV-4` s istom geometrijom i istim rezultatom, pa zauzima isto urednicko mjesto.
- `CV-34` | skriptna_obitelj: `v13_z124` | druga_slojna_veza: `nema bliskog para` | presuda: `varijanta` | razlog: paralelni cjevovodi sa zadanim omjerom protoka ostaju izravna varijanta baznog skriptnog motiva.
- `CV-35` | skriptna_obitelj: `nema bliskog para` | druga_slojna_veza: `nema bliskog para` | presuda: `rezervni` | razlog: pravokutni otvoreni kanal korisno siri prijenos fluida, ali urednicki je blizi zasebnom otvorenom toku nego jezgri `U13`.
- `CV-36` | skriptna_obitelj: `nema bliskog para` | druga_slojna_veza: `nema bliskog para` | presuda: `jedinstven` | razlog: dimnjak za vruci plin uvodi uzgon, stlaciviji medij i trenje u zaseban projektni problem dimenzioniranja voda.

### Radni zakljucak za U13 (CV)

Blok `CV` je najgusci i urednicki najkorisniji cjevovodni dodatak iz `SAVAR sesija 2`. Jezgreni kandidati za zadrzavanje su `CV-1`, `CV-2`, `CV-4`, `CV-8`, `CV-10`, `CV-11`, `CV-12`, `CV-17`, `CV-21`, `CV-25`, `CV-26`, `CV-28`, `CV-32` i `CV-36`, dok je dobar dio preostalih zapisa kvalitetna `varijanta` vec zatvorenih obitelji. Najvaznije unutarnje kompresije bloka su `CV-5/CV-6`, `CV-8/CV-20` i `CV-4/CV-33`, a `CV-24` i `CV-35` zasad imaju najbolji status kao `rezervni` rubni otvoreni tok.

## Prva operativna odluka nakon ove matrice

1. U glavnoj evidenciji treceg sloja mogu se dopisati `duplication_status` oznake za `CV-1` do `CV-36`.
2. Nakon toga se moze zatvoriti cijeli `SAVAR sesija 2` i nastaviti na `Virag 7.x` kao sljedeci cisti `U13` blok.