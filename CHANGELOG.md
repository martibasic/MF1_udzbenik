# Dnevnik promjena

Ovaj dokument prati sadržajne i tehničke promjene javnih izdanja. Potvrđene
pogreške pojedinih izdanja dodatno se vode u [errati](docs/errata.md).

## Unreleased — tehnički spremno za `1.0-rc1`

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
