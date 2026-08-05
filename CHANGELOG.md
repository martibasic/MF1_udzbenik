# Dnevnik promjena

Ovaj dokument prati sadržajne i tehničke promjene javnih izdanja. Potvrđene
pogreške pojedinih izdanja dodatno se vode u [errati](docs/errata.md).

## Unreleased — tehnički spremno za `1.0-rc1`

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
