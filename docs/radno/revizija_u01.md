# Revizija zadataka za vježbu U01 — 21. rujna 2026.

## Opseg

Korisnik je odobrio zamjenu ponavljajućih zadataka za vježbu uz zadržavanje
kvalitetnih zadataka. P1–P6, teorija, notebook i javni URL poglavlja ostaju
nepromijenjeni. Šest samostalnih zadataka zadržava razine T1, T1, T2, T2, T3, T4.
Izvor usporedbe prije revizije: commit `8622219`.

## Matrica zamjena

| Novo mjesto | Postojeća uloga / odluka | Nova aktivnost | Razina | Stabilni ID | Status |
| --- | --- | --- | --- | --- | --- |
| Z1 | Stari Z2 ponavlja prešu; ZAMIJENITI | Neto masa, dvije procjene gustoće, tumačenje razlike | T1 | `task-gustoca-ulja-iz-vaganja` | ugrađeno |
| Z2 | Stari Z1; ZADRŽATI i premjestiti | Izravni Pascalov prijenos i pomak | T1 | `task-u01-u-servisnoj-hidraulicnoj-presi-mali-klip-promjera` | ugrađeno |
| Z3 | Stari Z3: izravno preuređivanje F=pA; ZAMIJENITI | Prepoznavanje pogreške omjera i provjera rada | T2 | `task-pogreske-omjera-sile-i-pomaka` | ugrađeno |
| Z4 | Stari Z4 ponavlja višecilindarski primjer P4; ZAMIJENITI | Određivanje geometrije iz mjerenja i granica nestlačivog modela | T2 | `task-promjer-cilindra-iz-volumena` | ugrađeno |
| Z5 | Stari Z5 ponavlja P4 i Z4; ZAMIJENITI | Izbor između tri pumpe uz dva suprotstavljena ograničenja | T3 | `task-izbor-pumpe-sila-i-hod` | ugrađeno |
| Z6 | Kvalitetan intervalni problem; ZADRŽATI uz pojašnjenje | Isti račun, definirani faktori učinkovitosti, granični intervali i vođeni stol | T4 | `task-u01-hidraulicni-radni-stol-podupiru-tri-jednaka-cilindra` | ugrađeno |

Z3 je zamjena odobrene ranije ideje N3; cilj obratnog računa iz starog Z3
preuzima Z4, a izbor komponente Z5. Neodabrana nova stega s tolerancijom
promjera nije ugrađena: kvalitetni postojeći Z6 ostaje u knjizi.

## Provenijencija i skice

Novi problemi autorske su nastavne konstrukcije iz dogovorene didaktičke
revizije, bez vanjskog donor-teksta. Z1 i Z4 izričito su označeni kao sintetički
mjerni podatci. Povijesne evidencije izvora nisu prepisane.

- Z1, Z3, Z4 i Z5: `rewrite_status=preradeno`, `rewrite_level=P3`.
  Mijenjaju se najmanje scenarij/geometrija, zadano i traženo; primarni cilj
  je drukčiji prvi korak studenta, ne novi broj u istoj formuli.
- Z2: `rewrite_status=nije_potrebno`; nema nove autorske prerade ni nove razine P.
- Z6: `rewrite_status=nije_potrebno` za rekonstrukciju; precizirane su
  pretpostavke bez promjene scenarija, podataka i računa. Prag 3/5 nije primjenjiv.
- `sketch_requirement`: Z1 nije potrebna (vaganja su potpuno zadana);
  Z2–Z6 preporučena. Z2/Z3/Z5 dijele shemu istoga prijenosa, Z4 zasebnu mjernu
  shemu, Z6 shemu triju jednakih cilindara. Nema dekorativne slike za vaganje.
- `assets/print/u01_vjezbe_skice.svg` zamijenjena je vlastitom shemom triju
  scena bez numeričkih rezultata. Na skici su samo veličine korištene u tekstu.

## Stabilne poveznice

Stari Z1 zadržava isti ID i sada je Z2; stari Z6 zadržava i ID i položaj.
Za četiri zamijenjena problema zadržana su HTML odredišta starih veza neposredno
prije novih zadataka, kao prazni `span` elementi. Oni nisu dodatni Pandoc
`{#task-…}` zapisi i ne stvaraju sedmi zadatak. Stara veza vodi na zamjenski
problem, ne na arhivsku verziju. Arhivska verzija ostaje dostupna u Gitu.

| Uklonjeni ID | Novo odredište |
| --- | --- |
| `task-u01-na-kruzni-klip-promjera-djeluje-sila-odredi` | novi Z1 |
| `task-u01-u-zatvorenoj-hidraulicnoj-stezi-tlak-ulja-iznosi` | novi Z3 |
| `task-u01-hidraulicni-stol-nosi-teret-mase-preko-dvaju` | novi Z4 |
| `task-u01-rucna-pumpa-s-klipom-promjera-razvija-silu` | novi Z5 |

D06 koristi aktualne kanonske ID-jeve i redne brojeve. HTML kompatibilna
odredišta služe starim poveznicama na poglavlje; nisu obećanje očuvanja starih
brojeva stranica ili svih nekadašnjih odredišta ključa.

## Kontrolni račun i kriteriji odgovora

- Z1: mase ulja 42,9 i 86,1 g; gustoće 858 i 861 kg/m³; sredina 859,5 kg/m³,
  specifična težina 8431,695 N/m³, relativna gustoća 0,8595. Provjera dodavanjem
  iste mase posudi i punjenjima ne mijenja gustoću. Razlika dvaju mjerenja bez
  mjernog budžeta ne dokazuje nehomogenost.
- Z2: tlak 292,325 kPa; sila 4500 N; pomak 4,8 mm. Neovisno se provjerava
  jednakost istisnutih volumena. Isti podatci i rješenje kao u starom Z1.
- Z3: omjer površina 9; sila 900 N, pomak 10 mm. Ulazni i izlazni rad 9 J;
  netočno rješenje daje 81 J. Obvezno objasniti obje pogreške, ne samo dati brojeve.
- Z4: sva tri omjera volumena i pomaka daju 500 mm², promjer 25,2313 mm,
  a blokirani klip idealnu silu 200 N. Provjera mijenja treći volumen kako bi
  otkrila nekonzistentan niz. Nestlačiv model poduprt je samo u ispitanim uvjetima;
  smanjeni pomak pri većem tlaku ne razlikuje sam stlačivost, elastičnost i gubitak volumena.
- Z5: tlak 2 MPa, potreban volumen 30 cm³. Iz ograničenja slijedi dopuštena
  površina pumpe od 60 do 75 mm². Površine za 8/9/10 mm su 50,2655/63,6173/78,5398 mm²;
  samo 9 mm prolazi. Sile 100,531/127,235/157,080 N; hodovi
  0,596831/0,471570/0,381972 m. Rad je 60 J za sve varijante. Provjera uključuje
  odbacivanje obje druge varijante i gubitak izvedivosti kad se granica sile snizi.
- Z6: zadržani kontrolni brojevi i računska funkcija. Konzervativna sila mora
  biti barem 22 kN, a konzervativni hod najviše 1,60 m. Provjerava se i da
  krajnje vrijednosti učinkovitosti daju ispravan smjer konzervativnosti.

## Povezane datoteke

- `source/u01_osnove_fluida_i_pascalov_zakon.md`: samo odjeljak zadataka i pripadna slika.
- `tools/verify_u01.py`: funkcije i result-ID-jevi prema novim mjestima Z1–Z6;
  svih šest riješenih primjera ostaje provjereno istim računima.
- `tools/verification_manifest.json`: generirani kanonski zapisi i inventar rezultata.
- `source/d06_kljuc_kontrolnih_rezultata.md`: generirano iz aktualnog izvora.
- `source/d03_tipicne_pogreske_po_poglavljima.md`: dopunjena samo stavka U01.
- D01/D02 već sadrže potrebne veličine; postojeći notebook o preši i QR odredišta
  ne ovise o izmijenjenim zadatcima i ostaju nepromijenjeni.

## Validacija

Numerika i strukturni audit prolaze: U01 ima 69 provjera, svih 19 modula 1023
rezultata bez FAIL-a; knjiga zadržava 87 primjera i 90 zadataka. Manifest i
ključ regenerirani su nakon usklađivanja izvora i verifikatora.

- `python tools/verify_all.py`: 942 usporedbe s fiksnim ciljevima, 81 invarijanta,
  još 22 neovisne fizikalne provjere; 90/90 ugovora i bez rupa.
- `audit_publication.py`, `audit_typst.py`, provjera generiranog ključa,
  normalizacije javnog teksta i `git diff --check`: prolaze.
- Puni `quarto render` i `quarto render --profile pdf --to typst`: uspješni.
  `audit_pdf.py`: prolazi; 297 A4 stranica. Typst javlja postojeća upozorenja
  o zastarjelom `times.circle` u neizmijenjenom poglavlju o količini gibanja.
- Lokalni pregled u Edgeu na 320, 768 i 1440 px: šest zadataka i ispravne razine,
  bez duplikata ID-jeva i vodoravnog prelijevanja stranice; svih 12 naputaka i
  odgovora otvara se tipkom Enter i zatvara razmaknicom. Stara četiri HTML
  odredišta postoje, a svih šest poveznica iz D06 vraća se na aktualni zadatak.
- Vizualno pregledani SVG i PDF stranice zadataka; oznake skice unutar su kadra.
  Usporedba s Gitom potvrđuje da je cijeli izvor U01 prije i poslije odjeljka
  zadataka nepromijenjen, uključujući P1–P6.

Ovo je lokalna provjera sadržaja i rendera, ne potvrda cijeloga objavnog CI-ja:
JupyterLite i puni audit objavljenog weba nisu ponovno pokrenuti. Notebooki
nisu mijenjani. Nije napravljen commit ni push ove revizije. Lokalni Quarto je
1.9.32, a CI koristi 1.9.37.

## Povratak vizualnog stila — 22. rujna 2026.

Na zahtjev korisnice vraćen je izgled skice iz verzije `8622219`: šest manjih
panela u dva reda, plave naslovne trake, svijetle podloge, šrafirane stijenke,
gradijenti tekućine i metalnih klipova. Zadržana je tadašnja plava konvencija
prikaza tekućine, što je obrazloženo i komentarom u SVG-u. Prizori i podatci
odgovaraju aktualnim zadatcima: Z1 prikazuje taru i dva punjenja, Z2/Z3 preše,
Z4 mjerni cilindar, Z5 jednu pumpu i jedan radni cilindar, a Z6 tri cilindra.
Time ova dopuna zamjenjuje raniju odluku o zajedničkoj skici s tri scene.
Tekstovi zadataka, odgovori i numerički računi nisu mijenjani; usklađeni su
samo opis slike i alternativni tekst. Pravilo očuvanja stila zapisano je u AGENTS.md.

Provjere ove dopune: pregled stare i prilagođene skice u Edgeu, bez izlaska
teksta iz kadra; HTML render U01 i puni Typst render prolaze. Vizualno pregledana
slika na stranici 30 PDF-a; `audit_pdf.py` prolazi (297 A4 stranica). Prolaze i
`audit_publication.py`, normalizacija javnog teksta, provjera aktualnosti manifesta
i ključa te `git diff --check`. Računski testovi nisu ponavljani jer se numerički
sadržaj nije promijenio.

## Fizikalna dorada skica Z1–Z6 — 22. rujna 2026.

Na zahtjev korisnice primijenjena su pravila fizikalne dorade korištena u U02.
Sačuvani su raspored šest panela, plave naslovne trake i tekućina, šrafure,
gradijenti i tipografija. Ova dorada mijenja samo SVG i ovu evidenciju.

- Z1: posuda dodiruje plohu vage, tekućina doseže dno, a otvoreni vrh i debljina
  stijenki jasno su prikazani u sva tri stanja vaganja.
- Z2 i Z3: komore i donji spoj čine jednu neprekinutu fluidnu domenu. Brtve su
  na klipovima uz stijenke; uklonjeni su nepovezani dijelovi uz klipnjače.
  Ulazna sila djeluje prema dolje, sila ulja na veliki klip prema gore.
  Posebne tamne strelice označuju smjerove pomaka.
- Z4: dovod ima otvoreno ušće i stijenke spojene s tekućom komorom. Cilindar
  se nastavlja iza klipa, a zračna strana ostaje otvorena. Početna ploha
  označena je isprekidano samo unutar provrta; kota prati pomak iste plohe.
  Zadržana je razlika između mjerenja pomaka i zasebnoga pokusa blokiranja.
- Z5: vanjsko opterećenje radnog klipa djeluje prema dolje, nasuprot njegovu
  podizanju. Označeni su tlačni hod pumpe, radni pomak i površina radnog klipa;
  napomena izričito navodi da ventili nisu prikazani.
- Z6: zajednički vod stvarno spaja sve komore. Stol je povezan s trima jednakim
  klipovima i bočnom vodilicom; odvojeno su označeni opterećenje prema dolje,
  zajednički pomak prema gore i tlačni hod pumpnog klipa.

Opis pristupačnosti i vidljiva legenda razlikuju sile, smjerove pomaka i
geometrijske veličine te navode da skice i duljine strelica nisu u mjerilu.
Tekstovi zadataka, podatci, odgovori, teorija i riješeni primjeri nisu mijenjani.

Provjere: vizualni pregled SVG-a u Edgeu i slike na stranici 30 konačnog PDF-a;
tekst ne izlazi iz kadra. HTML render U01 i puni Typst render prolaze.
`audit_pdf.py` prolazi za 299 A4 stranica; `audit_publication.py` potvrđuje
87 primjera i 90 zadataka. Prolaze provjere normalizacije javnog teksta,
aktualnosti manifesta i ključa te `git diff --check`. Računski testovi nisu
ponavljani jer nema numeričkih promjena. Typst i dalje javlja postojeća
upozorenja za `times.circle` u U10. Objava, commit i push nisu dio ove dorade.

## Ponovni pregled nakon U15 — 22. rujna 2026.

Korisnikov prošireni cilj traži novu provjeru U01 i U02 nakon završnih
poglavlja. Ponovno su pročitani cijeli izvor U01, svih šest P/Z, stvarni
verifier i notebook te vizualno pregledano svih sedam referenciranih SVG-ova.
Polazište je `a7573d1`; izvorne radne kopije spremljene su radi usporedbe.
Ovaj pregled dopunjuje prethodne evidencije i ne pretpostavlja da stare
provjere dokazuju točnost sadašnjeg prikaza.

### Matrica odluka prije provedbe

| Mjesto | Postojeći ID / uloga | Odluka i korist | Razina | ID nakon dorade | Veze i provjere | Status |
| --- | --- | --- | --- | --- | --- | --- |
| P1 | `ex-u01-gustoca-specificna-tezina-i-relativna-gustoca-ulja`; svojstva iz gustoće | ZADRŽATI; precizirati zaokruživanje i hvatište težine ulja na skici | T1 | isti | SVG, verifier | provedeno |
| P2 | `ex-u01-optereceni-klip-i-tlak-u-zatvorenom-cilindru`; sila–tlak–sila | ZADRŽATI; otvoreni spojni vodovi i jasne sile na klipove | T2 | isti | SVG, verifier | provedeno |
| P3 | `ex-u01-servisna-hidraulicna-dizalica-t2`; sila, volumen i rad | ZADRŽATI; popraviti kote hoda, odnos promjera i dodati kratku procjenu utjecaja stlačivosti | T2 | isti | SVG, verifier | provedeno |
| P4 | `ex-u01-dvostruka-hidraulicna-platforma-s-rucnom-pumpom-t3`; broj poteza | PREPRAVITI razliku između najmanje zadanog podizaja i točno 25 mm; kotirati jedan potez, ne zbroj kao geometrijsku duljinu | T3 | isti | SVG, verifier | provedeno |
| P5 | `ex-u01-hidraulicna-kocnica-vozila-s-razdiobom-na-vise`; poluga i četiri cilindra | ZADRŽATI; stvarni krakovi 5:1, kote provrta, otvoreni priključci, dvije jednake sile po osovini | T2 | isti | SVG, verifier | provedeno |
| P6 | `ex-u01-hidraulicka-stezna-naprava-na-robotskoj-liniji-za`; paralelne stege | ZADRŽATI; razjasniti prijenos sile na ćeliju i skalarni zbroj iznosa sila | T2 | isti | verifier | provedeno |
| Z1 | `task-gustoca-ulja-iz-vaganja`; tara i mjerna razlika | ZADRŽATI; razlikuje se od P1 po određivanju neto mase i tumačenju mjerenja | T1 | isti | SVG, verifier, D06 | provedeno |
| Z2 | `task-u01-u-servisnoj-hidraulicnoj-presi-mali-klip-promjera`; osnovni Pascal | ZADRŽATI temeljnu tehniku; nacrtati točan omjer promjera i kote | T1 | isti | SVG, notebook, verifier | provedeno |
| Z3 | `task-pogreske-omjera-sile-i-pomaka`; dijagnostika pogreške | ZADRŽATI; ispraviti geometrijski omjer, ne mijenjati dobru aktivnost | T2 | isti | SVG, verifier | provedeno |
| Z4 | `task-promjer-cilindra-iz-volumena`; obratni mjerni račun | PREPRAVITI dopunom brojčane procjene stlačivosti i pogreške pomaka, uz jasnu bilancu zatvorene količine fluida | T2 | isti | SVG, notebook, verifier, D03/D06 | provedeno |
| Z5 | `task-izbor-pumpe-sila-i-hod`; izbor iz dvaju ograničenja | ZADRŽATI; provjeriti granične nejednakosti i prikaz radnog promjera | T3 | isti | SVG, notebook, verifier | provedeno |
| Z6 | `task-u01-hidraulicni-radni-stol-podupiru-tri-jednaka-cilindra`; intervalna odluka | ZADRŽATI; jasno odvojiti ukupno opterećenje od dodatnog tereta i ukupan tlačni hod od jednog poteza | T4 | isti | SVG, notebook, verifier | provedeno |

`rewrite_status=complete`; `rewrite_level=selective`;
`sketch_requirement=provjera i ciljana dorada svih sedam postojećih slika`.
Nema nove rekonstrukcije samo radi novosti: šest vježbi već razdvaja izravni
račun, pogrešku, obratni račun, izbor i intervalnu odluku. Novi podatci za
stlačivost autorski su nastavni dodatak, a ne mjerenja ili specifikacija uređaja.

### Početni nalazi ponovnog pregleda

- P2–P4 skrivaju pune stijenke priključaka dodatnim obojenim pravokutnicima.
  Zasebni gradijenti komora i spojeva stvaraju pruge u istom fluidu.
- P3 kotira hod između različitih dijelova klipa; P4 prikazuje zbroj svih
  poteza kao jednu geometrijsku duljinu. U tekstu devet punih poteza daje
  27 mm, a za točno 25 mm treba osam punih i posljednji djelomični potez.
- P5 kota glavnog promjera stoji preko uskog voda. Krak papučice označen
  kao 5a ne mjeri se od zgloba, pa nacrtana poluga ne daje omjer 5:1.
  Priključci četiriju radnih cilindara prolaze preko njihovih stijenki.
- Z2/Z3 koriste iste nacrtane širine iako su omjeri promjera 5 i 3;
  Z5 također treba geometriju povezanu s promjerima. Z6 je valjana shema,
  ali spojeni fluid treba jednak prostorni gradijent i jasne oznake površina.
- Stlačivost je samo kvalitativno pitanje; nema računa kojim student
  uspoređuje promjenu volumena s dopuštenom pogreškom pomaka.
- Notebook ima korisnu jezgru, ali završava tvrdnjom umjesto pitanjima,
  a njegove brojke nisu povezane s aktualnim vježbama. Verifier još dopušta
  1–2 % kod mnogih objavljenih rezultata; tolerancije treba vezati uz ispis.

### Provedene dorade i provjere prije commita

Zadržano je šest riješenih primjera i šest vježbi, njihove razine i postojeći
ID-jevi. Z4 dopunjen je brojčanom provjerom stlačivosti: gubitak volumena
0,100 cm³ smanjuje pomak s 10,0 na 9,80 mm, pa pogreška od 2 % ne prolazi
zadani kriterij od 1 %. P3 s drugim početnim volumenom daje odstupanje
0,0463 %. U tekstu su izričito razdvojeni ti pokusi, zatvorena količina
tekućine i pretpostavke modela. Usklađeni su D01–D03, generirani D06,
notebook i manifest. Novi podatci služe nastavnoj procjeni.

U P4 razdvojeno je devet punih poteza (27 mm) od osam punih i posljednjeg
poteza od 60 mm (točno 25 mm). U P5 stvarni krakovi poluge daju 5:1,
a četiri radna cilindra imaju prikazane odgovarajuće provrte i sile.
Svih sedam SVG-ova zadržava format i raspored panela; popravljeni su
povezani fluidni prostori, priključci, klipovi, omjeri promjera i kote.
Provjera prije commita otkrila je pet indeksa od 8,25 jedinica na skici
vježbi; povećani su na dopuštenih 9 jedinica, bez slabljenja audita.

Provedene provjere:

- `verify_all.py`: PASS, 1321 rezultat (1106 usporedbi s ciljnim
  vrijednostima i 215 invarijanti), 22 dodatne fizikalne provjere i 90/90
  ugovora zadataka; U01 ima 83 provjere.
- `check_u01_sketch_geometry.py`: PASS za svih sedam stvarnih SVG-ova;
  provjerava fluidne prolaze, stijenke, klipove, sile, promjere i kote.
- Strukturni i Typst audit, normalizacija, aktualnost D06 i manifesta:
  PASS; struktura knjige ostaje 87 primjera i 90 vježbi.
- Notebook izvršen od početka u čistom kernelu: PASS, 5,27 s.
- Obnovljeni HTML U01: PASS na 320, 768 i 1440 px, svih šest vježbi,
  stare poveznice, 12 blokova dostupnih tipkovnicom, bez prelijevanja;
  automatizirana WCAG A/AA provjera i povratne poveznice D06: PASS.
- Obnovljen puni nativni PDF: 319 A4 stranica, `audit_pdf.py` PASS.
  Vizualno pregledane sve slike U01 na stranicama 15, 17, 20, 21, 23,
  25 i 30 te nastavak odgovora Z4 u ključu na stranici 300.

Računske i geometrijske provjere dopunjuju autorski i vizualni pregled;
ne dokazuju same didaktičku kvalitetu. Postojeća Typst upozorenja za
`times.circle` u U10 ostaju. Ponovni pregled U02 i završna zajednička
provjera cijele knjige ostaju dio šireg cilja. GitHub će nakon pusha
izvršiti puni postupak objave iz `publish.yml`.

### Dopuna zajedničkog završnog prolaza

Razjašnjeno je da 8,33 predstavlja omjer potrebnog zbroja hodova i jednog
punog hoda, prije odluke o devet cijelih poteza. U P6 uklonjeno je rano
zaokruživanje površina pri računu tlaka i sile: sila se provjerava izravno
omjerom kvadrata promjera. Konačni rezultati, podatci i ID-jevi ostaju isti.
Obnovljeni su HTML U01, cjeloviti HTML za ispis i zajednički nativni PDF.
