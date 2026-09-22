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
