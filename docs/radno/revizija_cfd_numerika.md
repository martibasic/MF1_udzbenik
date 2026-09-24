# Revizija CFD i numeričkih poveznica kroz MF1

Datum: 23. rujna 2026. Početno stanje: `fd21d961f889a3e9391b667e7ce1dcbe87233dd3`.
Opseg je izričito cijela knjiga: kanonski izvori, pojmovnik, dodatak D i
povezane bilježnice/podatkovni paketi. Revizija uređuje postojeće poveznice;
ne mijenja raspored poglavlja ni zadatke Z1–Z6.

## Početni audit i uredničke odluke

[Inventar pojava](revizija_cfd_pojave.csv) sadrži izvor, redak, pronađene pojmove
i odjeljak prije i nakon revizije te pojave u Markdown ćelijama bilježnica.
Pretraženi su CFD, računalni opisi, numerički most/poveznica/trag/pokus,
diskretizacija, mreža, reziduali, verifikacija, validacija, nazivi softvera,
MRF, VOF, RANS, LES, DNS, y+, GCI, izvještaji sila i numerička nesigurnost.
Mreže cjevovoda i reziduali 1D računa namjerno su uključeni; pojava riječi
ne znači da je odlomak CFD. Izvedeni D06 evidentiran je odvojeno od izvora.

| Nalaz prije revizije | Odluka i didaktička korist |
|---|---|
| U01–U04: 4–5 računalnih okvira po poglavlju; ponovljene definicije, mreža i provjera | Spojeno u jednu kratku fizičku poveznicu po poglavlju; uklonjeni rani MRF, VOF i algoritmi. |
| U05: integracija sile ponavljana za ravnu plohu, u provjeri i u mostovima | Dvije komplementarne poveznice: sila/moment te normala/predznak za zakrivljenu plohu. |
| U06: pet računalnih napomena o istisnini, površini i ravnoteži | Jedan tekst „Kako računalo prati plutanje”; razdvojeni numerička geometrija, hidrostatika i dinamika. |
| U07: tri odvojena opisa ćelije | Jedna bilanca ćelije i objašnjenje poništavanja unutarnjih tokova; tablica skica → domena → mreža → izlaz. |
| U08: ponovljeni Bernoulli/V&V odlomci | Jedan most i kratka uputnica iz Venturija; odvojeni idealni model, viskozni gubitak i numerička pogreška. |
| U09–U10: opće kontrolne liste i ponovljene sile | Lokalni cilj: gustoća/energija u sapnici; ručna bilanca nasuprot integraciji polja na koljenu. |
| U11: više sličnih opisa sličnosti, prerani nazivi turbulencijskih pristupa | Tablica Re/Fr/Ma/We usmjerava izbor fizike i izlaza prije računanja. |
| U12: 12.9 i dva okvira ponavljaju konvergenciju | Objedinjeno u 12.9: lokalne jednadžbe → algebarski sustav → iteracije → izlaz. Sačuvano fizičko značenje Reynoldsovih naprezanja; razdvojeni CFD i RANS/LES/DNS. |
| U13–U15: općenite poruke o boljoj mreži | Ciljane odluke: lokalni koeficijent vraća se u mrežu; moment/pulsacije rotora; plitka voda ili višefazni opis. |
| D.4 i D.5 djelomično dvostruki rječnici, mnogo naziva alata | D.4 središnja mapa s pet stupaca; D.5 konkretna obrada polja; softver sveden na dvije uloge. |
| Venturi u D.8 nije izričito vezan uz podatke riješenog primjera | Polazište je uljni Venturi iz U08; popisani nedostajući ulazi za viskozni model. Vodeni sintetički paket iz D.9 jasno je zaseban slučaj. |
| Usporedba 3D Eulerova polja s 1D srednjim brzinama mogla se čitati kao strogi test numeričke pogreške | Razdvojena točna relacija duž strujnice od 1D presječne aproksimacije; profilna razlika ne mora iščeznuti profinjenjem. |
| Ponovljena teorija V&V i paušalne postotne granice | Sustavno objašnjenje u D.8; D.9 zadržava podrijetlo, pretpostavljene nesigurnosti i nedostajuće arhivske dokaze. |

Numerički pokusi u bilježnicama zadržani su: njihovi reziduali, bilance,
osjetljivosti i konvergencija imaju konkretnu računsku svrhu. Pregled nije
našao potrebu za promjenom njihovih podataka ili postupaka. Brojčani iskazi,
smjernice i odgovori svih 90 samostalnih zadataka uspoređeni su s početnim
stanjem bez promjene. CFD napomene unutar dvaju riješenih primjera skraćene
su na uputnice; proračuni primjera ostaju isti.

## Konačna mapa kroz knjigu

| Poglavlje | MF1 koncept | CFD poveznica / ciljani izlaz | Dublji izvor |
|---|---|---|---|
| 0 | rad s modelom i bilježnicom | kratki put od fizike do odluke; numerički pokus nije nužno CFD | U12, D.8 |
| 1 | kontinuum, tlak, Pascal | polje tlaka; kada ručni račun dostaje | U07, D.6 |
| 2 | viskoznost i međupovršine | gradijent → naprezanje → sila; potrebna svojstva fluida | U11–U12, D.4 |
| 3 | hidrostatska ravnoteža | mirna voda i tlakovi po dubini kao referenca | U05, D.4 |
| 4 | relativno mirovanje | ravnotežna površina kao provjera prolaznog modela | U14, D.8 |
| 5 | sila i moment tlaka | površinski zbroj, hvatište, normala i predznak | U10, D.5 |
| 6 | uzgon, gaz i mali nagib | sila iz polja i povratni utjecaj gibanja tijela | U15, D.6 |
| 7 | kontrolni volumen i kontinuitet | ćelijska i globalna bilanca mase | U08, U12.9, D.5 |
| 8 | Euler, Bernoulli, energija | idealni Venturi kao referenca, statički tlak nasuprot gubitku | U13, D.8 |
| 9 | Mach, gustoća i energija | kompresibilni model i maseni protok | U11, D.4 |
| 10 | količina i moment količine gibanja | sila/moment iz lokalnog polja i neovisne ukupne bilance | U12.9, D.5 |
| 11 | Re, Fr, Ma, We i sličnost | izbor fizike, modela i normiranog izlaza | U12, D.4 |
| 12 | lokalne bilance, zatvaranje, granični sloj | diskretizacija, iteracije, primjerena mreža i izlaz | D.5, D.8–D.9 |
| 13 | energija i mreža cjevovoda | 1D sustav → lokalni CFD → koeficijent gubitka → sustav | U08, D.6 |
| 14 | relativna brzina, moment i snaga | MRF ili klizajuća mreža prema srednjem ili vremenskom odzivu | D.2, D.8 |
| 15 | Fr, dubina i hidraulički skok | plitka voda ili VOF; bilanca i dubina kao izlazi | U06, D.6 |
| D | objedinjavanje i daljnje učenje | koncept → jednadžba → polje → izlaz → provjera → odluka | pripremljeni paketi i primarni izvori |

## Opseg, identiteti i izvori

Za usporedbu se koristi isti skup `source/*.md` i isti način brojanja
(`len(text.split())`); to je pokazatelj opsega Markdown izvora, uključujući
formule i oznake, a ne lingvistički broj riječi.

| Mjera | Prije | Poslije |
|---|---:|---:|
| Cijeli skup kanonskih izvora | 111.804 | 105.790 |
| Dodatak D | 2.931 | 2.429 |
| Urednički okviri `.mf1-numerika` bez poveznica za pokretanje bilježnica | 54 | 15 |
| Opseg tih okvira | 6.977 | 1.644 |
| Stranice lokalnog nativnog PDF-a | 339 | 327 |

Ukupni izvor skraćen je za **6.014 riječi po navedenom mjerilu (5,38 %)**.
Broj okvira nije ukupna mjera CFD sadržaja: objedinjeni odjeljci U06, U10
i U12.9 te dodatak D čitaju se i izvan tih okvira. Opseg U12 ostao je gotovo
isti (3.222 → 3.224), uz sadržajnije objašnjenje diskretizacije i iteracija.

Postojeći eksplicitni ID-jevi zadržani su. D.4–D.6 i D.8–D.9 dobili su
semantičke ID-jeve za međupoglavne reference, uz zadržane stare URL-ankere.
Ankeri dviju spojenih sklopivih provjera u U05 i U08 preneseni su u pripadne
mostove; sačuvano je i staro sidro postupka rješenja u U06. Redoslijed
D.1–D.10 i odjeljak U12.9 ostaju očuvani. Omotači i
indeks generiraju se postojećim alatom; manifest se obnavlja zbog promjena
provenijencijskih redaka. SVG-ovi, tiskovne kompozicije i dizajn nisu mijenjani.

Urednička provjera oslanja se na postojeću literaturu i primarne izvore:
[NASA V&V](https://www.grc.nasa.gov/www/wind/valid/tutorial/tutorial.html),
[mrežna konvergencija](https://www.grc.nasa.gov/www/wind/valid/tutorial/spatconv.html),
[OpenFOAM: iteracije i reziduali](https://doc.cfd.direct/openfoam/user-guide-v13/fvsolution)
i [integracija sila](https://cpp.openfoam.org/v13/classFoam_1_1functionObjects_1_1forces.html).
Normativne zahtjeve projekta nije bilo potrebno mijenjati niti oslabljivati.

## Izvršene provjere

- `build_book.py --write`, generator manifesta, `audit_architecture.py`,
  `test_book_model.py`, `test_render_workspace.py`,
  `test_component_visibility.py`, `audit_publication.py` i `audit_typst.py`:
  PASS; 87 primjera, 90 zadataka, 94 figure i 796 prikazanih jednadžbi.
- `verify_all.py`: PASS; 90/90 ugovora zadataka, 1.119 usporedbi s neovisnim
  ciljem, 221 invarijanta i 22 zasebne fizikalne provjere; bez rupa i tautologija.
- `validate_cfd_vv.py`: PASS za dva sintetička paketa i referentni profil,
  uz izričito očuvane praznine izvorne profilne dijagnostike.
- `execute_notebooks.py --timeout 120`: izvršeno 17/17 bilježnica bez pogreške;
  `test_legacy_notebook_generator.py`, provjera QR-ova i ključa rezultata: PASS.
- `normalize_public_text.py`: PASS. Usporedba s početnim stanjem potvrđuje
  iste tekstove svih Z1–Z6, postojeće prikazane jednadžbe glavnih poglavlja
  i eksplicitne ID-jeve. Novi su samo pripadni numerički zapisi i sidra.
- `build_book.py --render all`: uspješan završni web, zbirni ispis i PDF.
  `audit_rendered_site.py`: 24 stranice i 2.468 poveznica; `audit_rendered_model.py`:
  2.134 numerirana objekta u webu/ispisu; `audit_jupyterlite.py`: 17 bilježnica.
- `audit_pdf.py` i `audit_pdf_layout.py` s projektnim PyMuPDF 1.28.0: PASS;
  327 A4 stranica, 17 QR kodova i pripadne poveznice, razmaci jednadžbi,
  18 izvora literature i najmanje 9 pt na tiskovnim figurama. PDF za preuzimanje
  usklađen je s nativnim PDF-om.
- `audit_print_layouts.mjs` i `audit_print_site.mjs`: PASS; sačuvane geometrije,
  3.338 nepraznih oznaka, 149 tiskovnih redaka i njihove fizičke veličine.
- `audit_viewports.mjs _site`: završni PASS; 72 prikaza na 320/768/1440 px,
  pristupačnost i upravljanje tipkovnicom, A4 ispis te pokrenuti JupyterLite
  s Python jezgrom u stanju `Idle`.
- Vizualno pregledane ključne stranice PDF-a: uvodni put, ćelijska bilanca,
  tablica Re/Fr/Ma/We, U12.9 te tablice i Venturijev postupak u dodatku D.

Izgradnja ispisuje dva postojeća Typst upozorenja za zastarjeli naziv simbola
`times.circle` u neizmijenjenim jednadžbama U10; izlazi i auditi uspješno se
dovršavaju. Tijekom revizije ispravljen je položaj kompatibilnih sidara koji
je u prvom pokušaju PDF-a zasjenio nove oznake odjeljaka. Duga poveznica na
Venturijev postupak u uvodu skraćena je zbog prelijevanja pri širini od
320 px; odredište je očuvano. Provjere nisu mijenjane.

Autorska procjena: raspored sada gradi preduvjete, ponavljanja zamjenjuje
uputnicama i čuva razliku fizike, numerike i inženjerske odluke. Automatizirani
auditi mogu potvrditi strukturu, račune i poveznice; razumljivost studentima
treba zasebno provjeriti studentskim čitanjem i stručnom recenzijom.
