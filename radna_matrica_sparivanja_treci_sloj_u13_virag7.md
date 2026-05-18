# Radna matrica sparivanja treci sloj za U13 (Virag 7.x)

## Svrha dokumenta

Ovo je peti radni dokument za sparivanje treceg sloja u bloku `U13`. Fokus je samo na bloku `Virag 7.x` iz izvora `zdravko-virag-mehanika-fluida.md`.

## Pravilo citanja ove matrice

1. Skripta ostaje kanonski prvi zapis.
2. Drugi sloj ostaje vec zatvoren prvi sloj dopune.
3. Vec zatvoreni blokovi treceg sloja mogu se koristiti za lokalnu kompresiju kad ocito zauzimaju isto urednicko mjesto.
4. `jedinstven` znaci da novi zapis uvodi novu mrezu, novi rubni uvjet ili novu primjenu koju vec zatvoreni korpus nema u tom obliku.
5. `varijanta` znaci da zadatak ostaje u istoj obitelji cjevovoda, pumpi, grananja ili lokalnih gubitaka, ali s drukcijim trazenim parametrom ili drukcijom formulacijom.
6. `bliski_duplikat` se koristi samo kada novi zapis gotovo izravno ponavlja vec zatvoreno urednicko mjesto.

## U13 - Cjevovodi i grananja

### Postojeca jezgra

- skripta: `v13_z121-v13_z124`, uz rubne pomocne parove `v10_z89-v10_z95` i `v12_z111`
- drugi sloj: `av08_01-av08_03`, uz rubne pomocne zapise `av06_01-av06_02` i `av09_01`
- vec zatvoreni treci sloj za lokalnu kompresiju: `CV-1` do `CV-36`

### Treci sloj Virag 7.x - preliminarna presuda

- `VG-07-01` | skriptna_obitelj: `v13_z123` | druga_slojna_veza: `av06_01-av06_02, av08_02-av08_03` | presuda: `varijanta` | razlog: prepumpavanje preko brijega uz kontrolu tlaka u najvisoj tocki ostaje ista hibridna obitelj koju je blok `CV` vec dobro otvorio zadatkom `CV-2`.
- `VG-07-02` | skriptna_obitelj: `v13_z123-v13_z124` | druga_slojna_veza: `nema bliskog para` | presuda: `varijanta` | razlog: trazena razina u spremniku za zadani protok ostaje standardna projektna varijanta razgranatog cjevovoda.
- `VG-07-03` | skriptna_obitelj: `v13_z122-v13_z123` | druga_slojna_veza: `nema bliskog para` | presuda: `varijanta` | razlog: pretlak u spremniku za trazenu visinu mlaza ostaje ista obitelj cjevovoda, mlaznice i lokalnih gubitaka.
- `VG-07-04` | skriptna_obitelj: `v13_z123-v13_z124` | druga_slojna_veza: `nema bliskog para` | presuda: `jedinstven` | razlog: manometarski tlak u drugom spremniku kao aktivni rubni uvjet mreze otvara novi tip cjevovodnog zadavanja koji baza nema.
- `VG-07-05` | skriptna_obitelj: `v13_z123` | druga_slojna_veza: `av08_03` | presuda: `varijanta` | razlog: pumpna dobava za zadani protok i usporedba s protocima bez pumpe ostaje jezgrena pumpno-sustavna obitelj.
- `VG-07-06` | skriptna_obitelj: `v13_z121-v13_z123` | druga_slojna_veza: `av08_01` | presuda: `jedinstven` | razlog: zamjena samo polovice duljine cjevovoda cijevi drugog promjera daje jasan rekonstrukcijski scenarij kakav nizi slojevi nemaju.
- `VG-07-07` | skriptna_obitelj: `v13_z122-v13_z123` | druga_slojna_veza: `nema bliskog para` | presuda: `varijanta` | razlog: visina mlaza iz spremnika pod pretlakom ostaje ista obitelj kao `VG-07-03`, samo s izravno zadanom pogonskom razlikom tlakova.
- `VG-07-08` | skriptna_obitelj: `v13_z123` | druga_slojna_veza: `nema bliskog para` | presuda: `jedinstven` | razlog: procjena povrsine pukotine iz pada dobave uvodi dijagnosticki zadatak propuštanja koji vec zatvoreni korpus nema.
- `VG-07-09` | skriptna_obitelj: `v13_z124` | druga_slojna_veza: `nema bliskog para` | presuda: `varijanta` | razlog: protok u lijevoj grani iz poznatog protoka desne grane ostaje izravna obitelj paralelnih cjevovoda.
- `VG-07-10` | skriptna_obitelj: `v13_z122-v13_z123` | druga_slojna_veza: `nema bliskog para` | presuda: `varijanta` | razlog: smanjenje protoka nakon mehanicke deformacije i novog lokalnog gubitka ostaje lokalno-gubitaska varijanta.
- `VG-07-11` | skriptna_obitelj: `v13_z123-v13_z124` | druga_slojna_veza: `nema bliskog para` | presuda: `jedinstven` | razlog: protok kroz prikljucni cjevovod izveden iz promjene glavnog protoka nakon otvaranja grane daje dobar inverzni problem grananja.
- `VG-07-12` | skriptna_obitelj: `v13_z124` | druga_slojna_veza: `nema bliskog para` | presuda: `varijanta` | razlog: ustaljeni protok nakon potpunog zatvaranja ventila ostaje ista obitelj grananja i ventila kao u `VG-07-11`.
- `VG-07-13` | skriptna_obitelj: `v13_z122` | druga_slojna_veza: `nema bliskog para` | presuda: `varijanta` | razlog: dvije pa jedna mlaznica zadrzavaju istu mlaznicku i izlazno-gubitasku obitelj bez novog urednickog skoka.
- `VG-07-14` | skriptna_obitelj: `v13_z123-v13_z124` | druga_slojna_veza: `av08_03` | presuda: `varijanta` | razlog: protok kroz pumpu u razgranatom sustavu ostaje standardna pumpno-mrezna varijanta.
- `VG-07-15` | skriptna_obitelj: `v13_z122-v13_z123` | druga_slojna_veza: `nema bliskog para` | presuda: `varijanta` | razlog: otvaranje ventila na horizontalnoj cijevi ostaje jos jedna lokalno-gubitaska varijanta izljevnog sustava.
- `VG-07-16` | skriptna_obitelj: `v13_z124` | druga_slojna_veza: `nema bliskog para` | presuda: `varijanta` | razlog: zatvaranje jedne grane i novi ustaljeni protok ostaje izravna obitelj paralelnog grananja.
- `VG-07-17` | skriptna_obitelj: `v13_z123` | druga_slojna_veza: `nema bliskog para` | presuda: `varijanta` | razlog: promjer cjevovoda za stalnu razinu u spremniku ostaje ista obitelj stabilne razine koju je treci sloj vec otvorio zadatkom `CV-11`.
- `VG-07-18` | skriptna_obitelj: `v13_z122-v13_z123` | druga_slojna_veza: `nema bliskog para` | presuda: `varijanta` | razlog: promjer cijevi za zadanu izlaznu brzinu mlaza ostaje standardna projektna varijanta cjevovoda i mlaznice.
- `VG-07-19` | skriptna_obitelj: `v13_z121-v13_z123` | druga_slojna_veza: `av08_01` | presuda: `varijanta` | razlog: promjer za trostruko veci protok pod istim uvjetima ostaje tipicna varijanta gubitaka i dimenzioniranja.
- `VG-07-20` | skriptna_obitelj: `v13_z123` | druga_slojna_veza: `av08_03` | presuda: `varijanta` | razlog: promjer cjevovoda za zadani pretlak u tocki A s poznatom pumpom ostaje unutar vec zatvorene obitelji pumpnog dimenzioniranja.
- `VG-07-21` | skriptna_obitelj: `v13_z123` | druga_slojna_veza: `av08_03` | presuda: `jedinstven` | razlog: sustav hladenja s eksplicitnim padovima tlaka na komponentama je jak primijenjeni kruzni sustav kakav baza nema.
- `VG-07-22` | skriptna_obitelj: `v13_z123-v13_z124` | druga_slojna_veza: `nema bliskog para` | presuda: `varijanta` | razlog: jednaki protoci iz dva spremnika ostaju izravna ravnotezna varijanta razgranatog cjevovoda.
- `VG-07-23` | skriptna_obitelj: `v13_z124` | druga_slojna_veza: `nema bliskog para` | presuda: `varijanta` | razlog: promjer grane za zadani pretlak u tocki A ostaje jos jedna projektna varijanta grananja.
- `VG-07-24` | skriptna_obitelj: `v13_z124` | druga_slojna_veza: `nema bliskog para` | presuda: `varijanta` | razlog: jednake dobave u dvjema granama cine gotovo kanonsku varijantu baznog zadatka o paralelnim cjevovodima.
- `VG-07-25` | skriptna_obitelj: `v13_z124` | druga_slojna_veza: `nema bliskog para` | presuda: `varijanta` | razlog: promjer paralelnog cjevovoda za zadani protok ostaje izravno u istoj obitelji kao `v13_z124`.
- `VG-07-26` | skriptna_obitelj: `v13_z123` | druga_slojna_veza: `nema bliskog para` | presuda: `jedinstven` | razlog: usporedba dviju konfiguracija sa snagom mlaza i naknadnim redizajnom promjera daje siru usporednu vrijednost od tipicnog jednog proracuna.
- `VG-07-27` | skriptna_obitelj: `v13_z123` | druga_slojna_veza: `nema bliskog para` | presuda: `jedinstven` | razlog: protok i pretlak u presjeku A-A, uz mjerni koeficijent i spoj s manometrijom, daju zaseban mjerno-proracunski tip problema.
- `VG-07-28` | skriptna_obitelj: `v13_z123` | druga_slojna_veza: `nema bliskog para` | presuda: `jedinstven` | razlog: eksplicitna usporedba viskoznog i neviskoznog protoka u istom sustavu nije zastupljena u dosad zatvorenom korpusu.
- `VG-07-29` | skriptna_obitelj: `v10_z89-v10_z95` | druga_slojna_veza: `nema bliskog para` | presuda: `varijanta` | razlog: sila i snaga za pomicanje stapa s izlazom ulja ostaju u istoj primijenjenoj hidraulickoj obitelji koju je blok `CV` vec otvorio zadacima `CV-25`, `CV-28` i `CV-32`.

### Radni zakljucak za U13 (Virag 7.x)

Blok `Virag 7.x` je cist i vrijedan `U13` korpus, ali je znatno varijantniji od bloka `CV`. Najjaci kandidati za stvarno novo zadrzavanje su `VG-07-04`, `VG-07-06`, `VG-07-08`, `VG-07-11`, `VG-07-21`, `VG-07-26`, `VG-07-27` i `VG-07-28`, dok vecina ostalih zapisa sluzi kao kvalitetno pojacanje vec zatvorenih obitelji `protok-pretlak-promjer-grananje`.

## Prva operativna odluka nakon ove matrice

1. U glavnoj evidenciji treceg sloja mogu se dopisati `duplication_status` oznake za `VG-07-01` do `VG-07-29`.
2. Nakon toga se moze birati sljedeci otvoreni treci-slojni blok izmedu `DA`, `HS` i preostalih `Virag` podblokova.