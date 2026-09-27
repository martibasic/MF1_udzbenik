# Tipografski sustav PDF izdanja

Revizija od 24. rujna 2026. obuhvaća isključivo prezentaciju knjige.
Kanonski tekst, formule, podatci, primjeri, zadatci, reference, CFD poveznice,
bilježnice, QR izvori te mrežne i tiskovne skice ostaju nepromijenjeni.

## Skala i ritam

Zadržani su Libertinus Serif za tekst i naslove, New Computer Modern Math
za formule te postojeći fontovi skica. A4 i margine od 26 mm vodoravno i
22 mm okomito ostaju isti, pa se tiskovne figure ne skaliraju ponovno.

| Element | Veličina |
| --- | ---: |
| Naslov knjige | 34 pt |
| Naslov dijela | 26 pt |
| Poglavlje | 22 pt |
| Podpoglavlje | 15 pt |
| Odjeljak / naslov riješenog primjera | 12,5 pt |
| Najniži strukturni podnaslov / naslov napomene | 11,5 pt |
| Oznaka koraka rješenja | 11,25 pt |
| Osnovni tekst i formule | 11 pt |
| Sadržaj: poglavlje / podpoglavlje | 11,5 / 10,5 pt |
| Opis slike / folio | 9,5 pt |
| Zaglavlje / oznaka razine zadatka | 9 pt |
| Najmanja oznaka skice | 9 pt |

Obični retci imaju izmjeren razmak osnovica približno 15,5 pt, nasuprot
13,4 pt u polaznom PDF-u. Typst `leading` iznosi 0,75 em, a razmak odlomaka
0,6 em. Razmaci prije/poslije podnaslova iznose 19/8, 14/6 i 11/5 pt prema
razini; nakon naslova poglavlja 18 pt. Formule imaju prostor od 10 pt, a
slika i njezin opis razmak od 7 pt. Sve vrijednosti dolaze iz
`design-system/tokens.json`; `mf1-tokens.typ` generira `build_book.py`.

## Pravila prijeloma

Broj naslova i njegov tekst tvore isti redak u mreži s visećim nastavkom
dugoga naslova. Blok je neprelomljiv i vezan uz sljedeći sadržaj. Ispravljen
je i doslovni prefiks „0.” u uvodu koji je Typst ranije tumačio kao popis.
Uklonjeni su suvišni omotači polja primjera koji su poništavali razmake.
LF završetci include datoteka sprječavaju da Windows/Quarto umetne dodatne
prazne retke između broja i teksta naslova.

Poglavlja počinju na novoj stranici bez forsiranja neparnog broja stranice.
Dijelovi zadržavaju naslov i svoj lokalni sadržaj, na bijeloj podlozi.
Postojeći razdjelnik „Dodaci” ostaje zasebna stranica. Glavni sadržaj ima
dosljedna uvlačenja, točkaste vođice, desno poravnane brojeve i aktivne veze.
Zaglavlje prikazuje poglavlje; broj stranice pojavljuje se jednom, u podnožju.

Primjeri ostaju otvoreni blokovi; napomene dobivaju tanku sivu liniju.
Dugi primjeri i izvodi smiju prijeći na sljedeću stranicu. Naslov napomene,
kratki uvod u izdvojenu formulu te naslov rezultata s povratnom poveznicom
ostaju uz pripadajući sadržaj. Kratke tablice ostaju zajedno, dok duge
tablice ponavljaju zaglavlje i ne dijele pojedinačnu ćeliju između stranica.
Postojeća pravila tiskovnih kompozicija zadržavaju zadnji panel uz opis.

## Opseg, očuvanost i provjere

Polazni PDF imao je 327 stranica. Pregledani završni prijelom ima
303 stranice uz veći prored. Ušteda proizlazi iz povezanih brojeva i naslova,
uklanjanja prisilnih praznih stranica i suvišnih razmaka omotača, a ne iz
smanjenja osnovnog fonta, skica ili sadržaja. Pregledani su svi listovi
polaznog i novog PDF-a u kontaktnim pregledima, uz povećane prikaze rubnih
slučajeva, sadržaja, primjera, formula i ključa rezultata.

Stari auditni raspon 310–380 bio je vezan uz raniji prijelom tiskovnih figura
od 340 stranica. On je prijavio novi prijelom kao odstupanje. Nakon pregleda
i provjere očuvanosti novi je ograničeni raspon 270–335 (oko ±10 %); smanjena
je i gornja granica. Istodobno je audit stvarnog PDF-a proširen kontrolom
svih brojeva jednadžbi i svih P/Z oznaka po poglavljima prema kanonskom
indeksu, pa se potpunost ne zaključuje iz broja stranica.

Automatska kontrola obuhvaća 15 poglavlja, 87 primjera, 90 zadataka,
94 numerirane figure, 796 numeriranih jednadžbi, 90 unosa ključa,
17 vidljivih QR kodova s poveznicama i 18 bibliografskih zapisa. Usporedba
sa spremljenim polaznim stanjem provjerava hash 383 sadržajne datoteke,
skice, bilježnice i QR izvora te jednak multiskup 44 vanjske PDF poveznice.
Provjera koordinata obuhvaća osnovicu broja i naslova, osamljene naslove,
granice stupca i razmak broja jednadžbe od matematičkog izraza.

Reprodukcija završne provjere: `python scripts/check_publication.py`.
Koristi iste verzije alata kao objavni workflow, iznova stvara PDF i web,
kopira PDF u web preuzimanja te provjerava bilježnice, JupyterLite, model,
mrežni prikaz i ispis. Izlaz `_site/` služi kao lokalni pregled.

Završni puni lokalni objavni CI prošao je za 736 s: svih 17 bilježnica,
72 prikaza stranica na tri širine, A4 ispis i JupyterLite Python kernel
(`Idle`). Završni PDF i datoteka u web preuzimanjima imaju isti SHA-256:
`def7dcd573a06aea9e5d6ed0c7451882d09db8d4d2d4080907e7f136a55cbcb7`.
Posljednje dorade promijenile su 23 stranice; sve su ponovno pregledane,
a ostalih 280 ima isti raster tijela stranice kao prethodno pregledani
prijelom. Lokalni izvještaji i polazni PDF nalaze se u ignoriranoj mapi
`tools/tmp/typography-review/`.

Renderer i dalje prijavljuje tri upozorenja o zastarjelom nazivu Typstova
simbola `times.circle` u Quartovu matematičkom izlazu. Kompilacija prolazi;
izvorne formule zbog tog upozorenja nisu mijenjane.

Vizualna procjena čitljivosti nije dokaz didaktičke ili znanstvene kvalitete.
Na krajevima poglavlja i uz nedjeljive tiskovne panele ostaju kraće stranice;
ne rastežu se odlomci ili skice radi jednakog popunjavanja svakog lista.
U ovoj reviziji nije provedena nova sadržajna recenzija.

## Urednička dopuna zadataka — 26. rujna 2026.

Nakon dopune CFD primjena polazno izdanje imalo je 315 stranica. Ova revizija
obuhvaća način zadavanja i praćenja računa: svih 87 primjera ima polja
„Zadano”, „Traži se”, „Rješenje” i „Provjera i tumačenje”, a svih 90 zadataka
odvojene uvjete i zahtjeve. Zahtjevi se iskazuju izravnim glagolima; više
zahtjeva tvori numerirani popis. Odvojena fizikalna stanja izričito se
imenuju, a dulji se podatci raspoređuju u kratke odlomke. Brojevi, modeli,
tolerancije, kontrolni rezultati i razine zadataka nisu promijenjeni.

Primjeri i zadatci koriste jednake razmake: 1,2 em između odlomaka i
1,0 em između stavki popisa, uz postojeći prored od 0,75 em. Oznake polja
imaju 12 pt prije i 7 pt poslije. Izričiti razmak ispod oznake sprječava
da promjena odlomnog razmaka udalji naslov od teksta kojem pripada.
Posljednji zahtjev ostaje u istom numeriranom popisu i drži oznaku razine
uz sebe; ostale stavke ostaju prelomive. Skice, fontovi i margine zadržani su.

Zajednički HTML/Typst adapter prepoznaje i naslijeđene oznake s točkom ili
dvotočkom. Izvori sada imaju jedinstven zapis bez završne interpunkcije.
Generator ključa uklanja nazive polja prije sažimanja iskaza, čuvajući
formule i postojeće naputke/rezultate. `audit_publication.py` trajno provjerava
obvezna polja; regresijski testovi pokrivaju oba izlazna formata, brojanje
popisa, odvajanje naputaka i sažimanje bez prekinutih formula.

Usporedba s lokalnom početnom snimkom provjerava svih 90 skupova skalarnih
ulaza, kontrolnih rezultata, tolerancija i neovisnih numeričkih ugovora,
svih 796 izdvojenih jednadžbi, stabilne ID-jeve i nepromijenjene CFD odlomke.
Snimka i izvještaji čuvaju se u ignoriranoj mapi `tools/tmp/editorial-review/`.
Automatska provjera potpunosti dopunjuje urednički i vizualni pregled;
ne predstavlja novu znanstvenu recenziju ili studentski pilot.

PDF nakon te prve dopune imao je 333 stranice. Urednički pregled obuhvatio je uzorak od
40 stranica: kontaktne preglede iz svih poglavlja i povećane prikaze
kratkih primjera, složenih zadataka te njihovih nastavaka. Puni objavni CI
prošao je za 850 s, uključujući 72 mrežna prikaza, A4 ispis, izvršavanje
bilježnica i automatski audit svih stranica PDF-a. Regresijski raspon
270–335 nije mijenjan. PDF knjige i PDF dostupan u mrežnom preuzimanju
imaju isti SHA-256:
`95bb681e951acfa3fea7a2e5225692373324dafca5c99635ff41f535ba76357b`.

### Naknadno sažimanje iskaza i razdvajanje skice od računa

Na dodatni zahtjev autora svih 87 primjera i 90 zadataka sada počinje
poljem „Tekst zadatka”: u njemu su zajedno fizikalni postav, ulazne
vrijednosti i potrebni uvjeti. Zasebno ostaje „Traži se”, a u primjerima
slijede „Rješenje” i „Provjera i tumačenje”. Matematički model koji treba
izvesti pripada rješenju. Tablice se zadržavaju za usporedna mjerenja.
Time su uvodni dijelovi primjera skraćeni približno za trećinu, bez
promjene jednadžbi, problemskih podataka, traženih odluka ili razina.

Svih 57 skica u riješenim primjerima urednički je pregledano. Ponovljeni
računi zamijenjeni su kratkim simboličkim relacijama, a oznake izračunatih
veličina simbolima nepoznanica. Zadržani su smisleni kvantitativni grafovi,
profili i trokuti brzina. Opisi slika više ne prepričavaju brojčano rješenje.
Skice koriste sustav opisan u [ispis-skica.md](ispis-skica.md): u pravilu
62 % širine za prizor i 34 % za relacije, uz font od najmanje 9 pt.

Ugovor, registar komponenti, oba adaptera, generator ključa i audit
usklađeni su s poljem „Tekst zadatka”. Lokalna snimka i usporedbe ove
dopune nalaze se u ignoriranoj mapi `tools/tmp/concise-tasks-review/`.
Automatska usporedba čuva svih 796 izdvojenih jednadžbi i stabilne ID-jeve;
numerički verifieri zasebno provjeravaju rezultate. Prolaz audita ne
zamjenjuje uredničku procjenu čitljivosti.

Kontrolni render dopune imao je 314 stranica. Kontaktni pregled obuhvatio
je 73 stranice s primjerima i vježbama iz svih 15 poglavlja, uz povećani
pregled složenih iskaza i tiskovnih skica. Naknadno je dodatno razmaknuta
usporedba Reynoldsovih režima, a preostali brojčani kriteriji premješteni
iz zahtjeva u iskaze zadataka. Konačno izdanje ponovno prolazi puni
objavni postupak; njegov zapis je `tools/tmp/concise-tasks-review/publication.log`.
