# Dnevnik promjena

Ovaj dokument prati sadržajne i tehničke promjene javnih izdanja. Potvrđene
pogreške pojedinih izdanja dodatno se vode u [errati](docs/errata.md).

## Provedba odluka o skicama i notaciji — 14. listopada 2026.

- Ispravljena su proturječja u tekstu. Najvažnije: kormilarski stroj u pog. 1, Z2 sada je četverocilindrični Rapsonov stroj, uz V = 2As = 7,36 L.
- Skice zadataka više ne otkrivaju tražene rezultate; checkeri provjeravaju da rezultat nije prikazan.
- Uveden je stil vektora s atributom `data-mf1-vector`, legendom u uvodnom poglavlju i provjerom u `audit_sketch_design`.
- Notacija je ujednačena u tekstu, skicama, bilježnicama i dodatcima. Primjeri:
  - $F_G$ za težinu, $b$ za širinu broda, $\varphi$ za kut nagiba;
  - $\rho_w$, $\rho_{mv}$ i $\rho_o$ za gustoće vode, morske vode i ulja;
  - $k_s$ za hrapavost, $H_p$ i $H_t$ za visine crpke i turbine, $s(x)$ za nesigurnost;
  - $\beta$ od smjera $-u$, $\chi$ za sustrujanje.
- Rezultati verifikatora su nepromijenjeni, osim namjerne dobave u pog. 1, Z2. Evidencija je u `docs/radno/skice-2026-10/provedba/`.
- Puni lokalni objavni CI: PASS (913 s); PDF ima 326 stranica.

## Fizikalni pregled skica — 13. listopada 2026.

- Pregledano je 95 SVG skica i 17 bilježnica, skica po skica, uz tablice vektora i oznaka. Ispravljene su 94 skice i 13 bilježnica (samo kod crteža). Analize su u `docs/radno/skice-2026-10/`, sažetak i stavke za odluku autorice u `IZVJESTAJ_SKICE.md`, a rječnik oznaka u `RJECNIK_OZNAKA.md`.
- Glavni ispravci su:
  - duljine vektora prema kontinuitetu, ravnoteži i količini gibanja;
  - fizikalno pogrešna geometrija (more unutar broda, sile kroz poklopac, omjer sapnice, nagib EGL-a, promjeri cijevi petlje, kontrolni volumen);
  - oznake usklađene s tekstom i standardom notacije;
  - pravi indeksi.
- Tekst, brojevi i rješenja nisu mijenjani. Checkeri su postroženi, nijedan nije oslabljen. PDF ima 324 stranice.

## Unreleased — radno izdanje

Aktualno stanje i potvrđeni prolazi vode se u
[statusu izrade](status_izrade_udzbenika.md). Donji datirani zapisi opisuju
stanje pojedine revizije; stare brojke i navodi o objavi nisu aktualni status.

### Recenzentska revizija cijele knjige — 12.–13. listopada 2026.

Provedeno je deset prioritetnih nalaza autorskog recenzentskog pregleda
(stručni recenzent mehanike fluida i primjenski recenzent brodogradnje).
Evidencija po poglavljima je u `docs/radno/revizija_u01.md`–`revizija_u15.md`.

- **Ispravci:** kut uronjenja ruba palube u pog. 6 (tan umjesto sin,
  31,1° umjesto 37,1°) u tekstu i verifikatoru; plutajuća osnova vjetroagregata
  sa stvarnim podatcima stabilnog spara; zaokruživanja i nerealni podatci u
  pog. 3, 4, 7, 8, 10.
- **Izvodi koji su nedostajali:** Reynoldsov transportni teorem (pog. 7),
  energijska jednadžba s crpkom, turbinom, gubitcima i α (pog. 8), brzina
  zvuka, omjer površina A/A*, normalni val i porast entropije (pog. 9),
  moment količine gibanja i aktuatorski disk (pog. 10), konstitutivna
  relacija do Navier–Stokesove jednadžbe, Poiseuilleova jednadžba,
  Reynoldsovo osrednjavanje i jednodimenzijski primjer konačnih volumena
  (pog. 12), Darcyjev koeficijent iz ravnoteže sila i Hardy–Crossova
  metoda (pog. 13), idealna učinkovitost propelera i Eulerova visina crpke
  (pog. 14), hidraulički skok i opći kritični uvjet (pog. 15), dvofluidni
  metacentarski radijus i granica malog kuta (pog. 6), paraboloid rotacije
  premješten u teoriju (pog. 4).
- **Brodogradnja u svim poglavljima:** kormilarski stroj, ležaj statvene
  cijevi, procjep limova, bočni balastni tank, sondiranje teretnog tanka,
  tank u zavoju, separator goriva, vodonepropusna vrata, zahvatni usis,
  usisni vod rashladne crpke, zrak za upućivanje motora, Peltonova lopatica,
  vodomlazni potisak, aktuatorski disk propelera, Froudeova hipoteza i
  ITTC 1957, granični sloj modela broda, balastna crpka, propeler u
  napredovanju i plitkovodni Froudeov broj broda.
- **Struktura:** 90 riješenih primjera (pog. 9 i 10 dobili su po jedan),
  zamijenjeni ponovljeni zadatci uz zadržan raspored 2×T1, 2×T2, T3, T4,
  blok granice modela u svakom poglavlju, novo pitanje samoprovjere umjesto
  ponovljenog pitanja „Zastani i promisli”, usklađene razine T.
- **Notacija i nazivlje:** jedinstveni standard u `docs/urednicki_stil.md`
  primijenjen u svim poglavljima i dodatcima (v, ξ, ζ, κ, p_M, p_aps, p_0,
  y_h, nadvođe, poluga stabiliteta, zagušenje i prigušenje, crpka).
- **Dodatci:** sažetak formula poredan po poglavljima i dopunjen svim
  novim relacijama; pojmovnik proširen s 99 na 126 natuknica; dodatak s
  tipičnim pogreškama dopunjen klasičnim pogreškama i općim formulacijama.
- **Skice i alati:** novi i preuređeni SVG prizori, dva nova geometrijska
  checkera (pog. 3 i 4), stroži postojeći checkeri; regresijski raspon PDF-a
  pomaknut uz obrazloženje u `docs/pdf-tipografija.md`.
- **Sažimanje (354 → 323 stranice):** ključ rezultata bez ponovljenog sažetka
  iskaza, sažetak formula bez brojčanih primjera (oko pola kraći), pojmovnik
  sveden na jednorečenične definicije, provjere uz primjere, napomene uz skice
  i završni okviri svedeni na stvarne provjere, uklonjena ponavljanja pog. 10
  u pog. 14 i lokalni izvod u bloku „Dublje” pog. 10. Izvodi, primjeri, zadatci
  i CFD odlomci nisu uklanjani.

### Pitanja, eksperimentalna usporedba i naziv — 27. rujna 2026.

- U svih 15 poglavlja jedno od postojećih konceptualnih pitanja izdvojeno
  je u vidljivi tekst uz pripadajuće CFD ili numeričko tumačenje.
- Pojmovnik ima izravne poveznice na poglavlja i dodatke, s čitljivim
  oznakama umjesto internih kodova.
- U PDF-u kanonske poveznice i generirane reference poglavlja vode na
  unutarnja odredišta, uključujući dodatke; više ne pokušavaju otvoriti
  izvorne `.qmd` datoteke. Regresija čuva odvojeni web prikaz i vanjske veze.
- Novi P6 u U12 uspoređuje mjerenje i CFD položaja ponovnog priljubljivanja
  iza stepenice. Izvorne tablice Driverova i Seegmillerova pokusa te
  objavljeni CFL3D rezultati arhivirani su s provenijencom. Postojeća
  bilježnica i verifier provjeravaju isti račun; dodani su testovi arhiva
  i podudarnosti bilježnice. Knjiga sada ima 88 primjera i 797 jednadžbi.
- Ponovljen pregled javne NACA arhive dokumentira preostale granice
  dostupnih dokaza; ne nadomješta ih izmišljenim podatcima i ne ostavlja
  korisniku obvezu traženja nedostajućih zapisa.
- Podnaslov glasi „Priručnik za samostalan rad s numeričkim pokusima i
  primjenama u brodogradnji i strojarstvu”. Naziv publikacije usklađen je
  na sveučilišni priručnik. Stabilna sidra i putanje ostaju sačuvani.
  Auditi stvarnog HTML-a i PDF-a trajno provjeravaju naziv, a PDF audit i
  potpuni aktualni podnaslov na naslovnici.
- Središnji status obnovljen je prema aktualnim izvorima. Stručna recenzija
  i studentski pilot ostaju budući koraci; priručnik još nije poslan na recenziju.

### CFD primjene i ujednačeni zadaci — 26.–27. rujna 2026.

- CFD objašnjenja u svih 15 poglavlja povezana su s konkretnim fizikalnim
  sustavima, očekivanim rezultatima i provjerama valjanosti modela.
- Postojećih 87 primjera i 90 zadataka dobilo je jedinstvena polja „Tekst
  zadatka” i „Traži se”; primjeri imaju i „Rješenje” te „Provjera i tumačenje”.
  Fizikalni postav i podatci objedinjeni su, zahtjevi iskazani izravnim
  glagolima, a razmaci usklađeni u PDF-u i webu.
- U 57 skica uz riješene primjere uklonjeno je ponavljanje cijelog računa;
  zadržani su simbolički odnosi i smisleni grafovi. Tiskovne izvedenice
  obnovljene su uz najmanje 9 pt za oznake.
- Prethodno izdanje od 315 stranica prošlo je puni lokalni objavni CI i
  GitHub Action za commit `8e05312`. Taj prolaz prethodi gornjoj dopuni i
  ne služi kao njezina potvrda.

### Numeričke poveznice — 16. rujna 2026.

- Numerički mostovi ponovno su prikazani u HTML-u i nativnom PDF-u. Kratki
  numerički trag vraćen je u svih 15 javnih poglavlja kao izravna poveznica
  između ručnoga fizikalnog modela, diskretizacije i odgovarajuće CFD provjere.
- Numerički tragovi sada se u tijeku teksta prikazuju kao sadržajni blokovi s
  vlastitom ljubičastom naslovnom bojom i lijevom vodilicom, jednako čitljivo
  kao fizikalno značenje i inženjerski kontekst.
- Poglavlja U02–U15 imaju dva proširena numerička traga: prvi je uz ključni
  fizikalni model, a drugi sintetizira provjere, mjerodavne izlaze i granicu
  ručnog modela u teorijskom tijeku prije riješenih primjera odnosno zadataka.
- U01 je pilot-novo uređenje bez oznake „Numerički trag”: sadržaj je ugrađen u
  dva odjeljka „Kako računalo pomaže pri proračunu strujanja” i „Kako računalo
  povezuje tlak i protok”. Zaključni numerički most dolazi prije zadataka;
  sažetak ostaje posljednji sadržaj poglavlja.
- Prošireni numerički mostovi, provjere i pokusi u poglavljima U02–U15 ostaju
  nakon zadataka i neposredno prije sažetka.
- U primjerima su uklonjene oznake „Primjer za …”, a iz zadataka 60 internih
  redaka „Skica: da …”; objedinjene skice za vježbu ostaju prikazane pri dnu
  odgovarajućih poglavlja.
- Revizija refaktora vratila je pune CFD mostove u U01–U04, pitanja prije
  numeričkih pokusa u U05, izvod $\lambda=64/Re$ u U12 te fizikalni temelj
  viskozne disipacije u U13. Dimenzijski izvod Darcyjeva oblika, energijske
  crte i korekcija kinetičke energije ostali su u kanonskom sadržaju pa nisu
  ponovno umetani.

### Urednička dorada — 9. rujna 2026.

- Riješeni primjeri dobili su oznake P1, P2, … unutar svakog poglavlja.
  Numeracija se automatski usklađuje i provjerava. Koraci rješenja imaju
  jedinstvenu razinu naslova i samo svoj redni broj; uklonjene su dvostruke
  oznake poput „2.6.1 1.” i pogrešno ugniježđeni koraci. Isto pravilo vrijedi
  za korake računalnog proračuna u dodatku D.
- Svih 87 riješenih primjera i cjelovitih vođenih zadataka ima izravni
  naslov problema, bez ponovljenog generičkog prefiksa. U HTML-u i PDF-u
  uklonjene su vertikalne crte i lijeve uvlake tih blokova, uključujući
  mobilni prikaz i preglednički ispis.
- Svih 90 samostalnih zadataka ima oznaku Z1–Z6 unutar poglavlja i kratak
  naslov problema. Razina T1–T4 sitna je oznaka na kraju, desno; uklonjeno je
  miješanje popisne i odjeljačne numeracije. Ključ rezultata preuzima isti
  broj i naslov te provjerava redoslijed. Usklađene su i oznake na skicama.
- Svih 15 kratkih napomena s naslovom „Numerički trag” dobilo je opisne
  naslove i pristupačnije objašnjenje preko fizikalnog sustava. Divergencija
  je objašnjena kao lokalno širenje ili sabijanje fluida; uklonjeni su
  preuranjeni nazivi algoritama i neobjašnjeni stručni izrazi. Uvod u CFD
  usklađen je s tim pristupom.
- Skraćene studentske upute i početna stranica: jasnije je odakle početi,
  kako koristiti razine T1–T4 te što se može ostaviti za dodatno čitanje.
  Uklonjena su ponavljanja u sažetku formula i tehnički detalji iz studentskog uvoda.
- U01 razlikuje lokalni i srednji tlak te gustoću. U09 ispravlja zapis
  `dρ/ρ = −Ma² dv/v`, navodi izentropske pretpostavke, definira `γ = cp/cv`
  i dosljedno koristi oznaku `Ma` za Machov broj. Izvod površina–brzina
  uspoređen je s [NASA-inim izvodom](https://www.grc.nasa.gov/www/k-12/airplane/tunnozt.html).
- U12 uklanja pogrešnu implikaciju da nejednolik profil nužno znači
  konvektivno ubrzanje i definira brzinu trenja magnitudom zidnog naprezanja.
- U11 više ne traži prethodno čitanje kasnijeg U13; opis dimenzija
  razlikuje mehaničke od toplinskih veličina.
- U15 zadržava tlačne sile u objašnjenju bilance hidrauličkog skoka,
  uklanja nedosljednost zbog preranog zaokruživanja u primjeru bazena
  (`ex-hidraulicki-skok-bazen`) i navodi SI jedinicu Manningova koeficijenta.
- Sažetak formula i pojmovnik usklađeni su s glavnim tekstom: dopunjeni su
  uvjeti energijske i količinske bilance, značenja višeznačnih oznaka,
  Bondov i Froudeov broj te razlika između disipacije mehaničke i očuvanja
  ukupne energije.
- Lokalna i CI izgradnja više zasebno ne ponavljaju dvije provjere koje
  već izvodi `verify_all.py`; opseg provjera ostaje isti.
  PDF korak izričito bira `--to typst` i ne ponavlja naslijeđeni HTML render.
- PDF više dvostruko ne numerira uokvirene jednadžbe: uklonjena je
  naslijeđena numeracija unutarnje formule koju Pandoc stvara za `\boxed`.
  Time se uklanjaju preklapanja brojeva i pogrešni pomaci numeracije.
  Oznaka i naslov poglavlja u PDF referencama odvajaju se razmakom.

Sekvencijski proizvodni build i tehnički QA prolaze. Kandidat još nije javno
deployan niti je proglašen izdanjem `v1.0`; za to ostaju obvezne dvije neovisne
stručne recenzije i studentski pilot.

### Dodano

- Arhitektura pune jezgre MF1 s poglavljima U01–U15 i prijelaznim
  preusmjerenjima starih javnih URL-ova.
- Nova poglavlja o kompresibilnom idealnom toku, diferencijalnom opisu realnog
  toka i otvorenim tokovima.
- Kurikularna matrica s 145 sati rada, autorski ugovor za stabilne ID-jeve te
  javni tok errate.
- Šesti dodatak D06 sa zasebnim ključem naputaka i kontrolnih rezultata za svih
  90 samostalnih zadataka.
- Nativni Quarto/Typst PDF profil, hrvatska lokalizacija sučelja i ponovljivi
  audit stvarnoga PDF artefakta.
- CI tok za izvršavanje 17 notebookova, izgradnju HTML-a, PDF-a i JupyterLitea
  te viewport/WCAG provjeru na pull requestovima; deploy ostaje odvojen.
- Tri CFD V&V paketa s provenijencom i strojnom provjerom strukture: dva
  spremna nastavna slučaja i jedan ograničeni referentni paket.
- Ponovljivi protokoli neovisne stručne recenzije i studentskog pilota; sami
  ljudski postupci time nisu proglašeni provedenima.

### Promijenjeno

- Redoslijed sadržaja sada slijedi graf preduvjeta: statika → integralna
  dinamika → sličnost i diferencijalni realni tok → inženjerski sustavi.
- Kanonski rukopis sveden je na 15 poglavlja, 87 riješenih primjera, 90
  samostalnih zadataka i šest dodataka.
- Usporedivi regex inventar glavnih poglavlja smanjen je sa 124.957 na 108.711
  leksičkih tokena (`−13,00 %`) iako je dodano petnaesto poglavlje.
- Znanstvena revizija ispravila je poznate pogreške u predznacima, referencama
  tlaka, nestacionarnim članovima, radu strojeva, kavitaciji, stabilitetu i
  granicama modela te uklonila preširoke sigurnosne i normativne zaključke.
- Uvedeni su autorski blokovi `Temelj`, `Izvod`, `Fizikalno značenje`, `Granica
  modela`, `Numerički pokus` i `Dublje`; u PDF-u su nativno stilizirani i
  prelomivi. Uklonjena je uvlaka prvoga retka odlomka i uveden razmak od
  `0.72em` između odlomaka.
- Riješeni primjeri i cjeloviti zadatci u PDF-u dobili su zaseban nativni
  naslov, značku razine T1–T4 i odvojeni redak konteksta. Mali strukturni
  podnaslovi imaju veći razmak iznad i manji razmak prema sadržaju koji uvode.
- Svih 17 notebookova preoblikovano je prema obrascu
  `predvidi → izračunaj → provjeri`, s izvršivim tvrdnjama i analizom pogreške,
  konvergencije, osjetljivosti ili nesigurnosti.
- Skice su usklađene u predznacima i oznakama, a SVG inventar dobio je
  semantičke naslove, opise i pristupačne atribute.
- Mobilno prelamanje, fokus tipkovnice, kontrast i ponašanje pri smanjenom
  gibanju unaprijeđeni su i provjereni na 320, 768 i 1.440 px.

### QA

- Stara zbirna tvrdnja „500/500 PASS” uklonjena je iz javne dokumentacije.
- Manifest zadataka nadograđen je na shemu v2: svih 90 zadataka ima `golden`
  ugovor, uz 393 parsirana skalarna ulaza i 312 ugovora rezultata te
  autoritativni tekst, jedinice, pretpostavke, tolerancije i verifier ID-jeve.
- Numerički runner sada obuhvaća 19 modula i prolazi 1.001 stvarnu provjeru:
  924 usporedbe s unaprijed zadanim ciljem te 77 invarijantnih, dimenzijskih ili
  graničnih provjera, bez self-comparison usporedbi i bez rupa u pokrivenosti.
- Paket kritičnih fizikalnih regresija proširen je na 22/22 provjere.
- Svih 17 notebookova izvršava se od početka u zasebnim čistim kernelima, bez
  spremanja generiranih izlaza u izvorne datoteke.
- Završni JupyterLite paket sadrži svih 17 notebookova, prolazi strukturni audit
  i u pregledniku pokreće Pyodide kernel do stanja `Idle`.
- Publikacijski audit potvrđuje 15 poglavlja, 87 riješenih primjera, 90
  zadataka, šest dodataka, 145 sati, 1.185 stabilnih ID-jeva i 789 prikazanih
  jednadžbi.
- Završni HTML audit prolazi za 24 stranice, 210 slika, 2.081 vezu, 472
  sklopiva bloka i 11 preusmjerenja.
- Nativni PDF audit prolazi za 299 A4 stranica, 7.045.244 B i 536.983
  ekstrahirana znaka; metapodatci, kazalo, poglavlja i reprezentativni rasteri
  također prolaze.
- Viewport/WCAG audit prolazi 72 prikaza na širinama 320, 768 i 1.440 px te
  zasebni A4 prikaz.

### Preostali ljudski izlazni kriteriji i deklarirana ograničenja

- Profilni CFD referentni paket nema arhivske reziduale, monitore, maseni
  debalans ni potpuni budžet mjerne nesigurnosti; ta se praznina ne popunjava
  sintetičkim mjerenjima.
- Zasebna recenzija nastavnika mehanike fluida, odvojena primjenska recenzija
  stručnjaka iz strojarstva ili brodogradnje te pilot s 8–12 stvarnih studenata
  **nisu provedeni**. Ostaju obvezni ljudski kriteriji prije `v1.0`.
