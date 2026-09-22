# Revizija zadataka za vježbu U04 — 22. rujna 2026.

## Opseg i odluke prije provedbe

Polazište je commit `51b21b9` uz postojeću lokalnu reviziju U03. Njezine
izmjene i korisnički omotači U02/U11 čuvaju se. Uređuju se zadatci za vježbu
U04 i njihove ovisnosti; P1–P6, teorija i notebook ostaju izvan zahvata.
Ostaje šest mjesta T1, T1, T2, T2, T3, T4.

| Primjer | Princip i postupak | Studentska aktivnost i sličnost |
| --- | --- | --- |
| P1, laboratorijska kolica, T2 | Nagib a/g i očuvanje volumena | Izravni račun razina; Z1 daje osnovnu samostalnu vježbu |
| P2, zatvoreni modul, T2 | Efektivna gravitacija, geometrija stijenke i sila | Sila i hvatište; stari Z4 ponovno povezuje silu i visinu |
| P3, rotirajući cilindar, T2 | Paraboloid i volumen | Izravni račun; stari Z5 ponavlja isti postupak bez stvarne odluke T3 |
| P4, rotacijski spremnik, T3 | Paraboloid, tlakovi i granica prelijevanja | Povezivanje uvjeta; Z6 dodaje korisnu toleranciju i ograničenje pokrivenosti |
| P5, kočenje autocisterne, T2 | Smjer ubrzanja i dvije geometrijske granice | Razlikovanje prednje i stražnje strane; blisko Z1/Z2 |
| P6, centrifuga, T2 | Radijalni gradijent, r² i pretvorba okr/min | Izravni tlak iz vrtnje; novi Z4 uvodi obrnuti problem i neodređenost smjera |

| Mjesto | Odluka | Didaktička korist | Razina | ID i status |
| --- | --- | --- | --- | --- |
| Z1 | ZADRŽATI | Osnovni nagib, volumen i provjera ruba | T1 | Stari ID; odabrano |
| Z2 | ZADRŽATI uz preciziranje pravokutne geometrije | Obrnuti račun ubrzanja na granici; komplement Z1 | T1 | Stari ID; odabrano |
| Z3 | PREPRAVITI dodatnom usporedbom kočenja | Razlikovati brzinu prema gore od ubrzanja prema dolje | T2 | Stari ID; odabrano |
| Z4 | ZAMIJENITI | Vrtnja iz dvaju tlakova na istoj visini; zajednička referenca i kvadrat polumjera | T2 | `task-vrtnja-iz-radijalne-razlike-tlakova`; odabrano |
| Z5 | ZAMIJENITI | Ocjena relativnog mirovanja iz niza podataka, ne jedne podudarnosti | T3 | `task-provjera-smirivanja-ubrzanog-fluida`; odabrano |
| Z6 | ZADRŽATI uz preciziranje pretpostavki i provjeru preporuke | Geometrijsko ograničenje, tolerancija brzine i rezerva | T4 | Stari ID; odabrano |

Z4/Z5: `rewrite_status=preradeno`, `rewrite_level=P3`; mijenjaju se prizor,
ulazi, izlazi i studentska odluka (najmanje 3/5). Ideje su autorske nastavne
konstrukcije proizašle iz ove analize; očitanja nisu stvarni pokus.
Z1/Z2: `rewrite_status=nije_potrebno`; Z3/Z6 su ciljane dopune postojećeg
problema, za koje prag rekonstrukcije 3/5 nije uvjet.

Obvezni ishod U04, granica kvazistacionarne aproksimacije, dobiva samostalan
zadatak Z5. Dva nastavna kriterija razlikuju blizinu referentnom rješenju od
promjenjivosti razine. Prihvaćen uzorak nije dokaz mirovanja cijelog fluida,
niti dokaz da tijekom naglog pokretanja nije bilo valova ili prelijevanja.

## Poveznice, skice i plan provjera

Stari ID-jevi ostaju uz nova mjesta kao prazni HTML span elementi:

| Stari ID | Novi ID |
| --- | --- |
| `task-u04-ubrzani-otvoreni-spremnik-sirine-stijenke-i-duljine` | `task-vrtnja-iz-radijalne-razlike-tlakova` |
| `task-u04-cilindricna-posuda-radijusa-s-pocetnom-dubinom-vode` | `task-provjera-smirivanja-ubrzanog-fluida` |

`sketch_requirement`: preporučena za Z1/Z2, potrebna za Z3–Z6. Sačuvati
raspored dva stupca i tri reda, dimenzije panela, svijetlu podlogu, šrafuru,
gradijente vode/ulja i tipografiju. U Z3 odvojiti strelice brzine i ubrzanja;
Z4 ne prikazati jedan smjer vrtnje kao izmjeren; Z5 razlikovati referentni
profil od sintetičkih očitanja; Z6 parabolu vezati uz stvarne razine i rub.

Neovisne provjere: Z1/Z2 očuvanje volumena, granica ruba i pokrivenost dna;
Z3 predznak efektivne gravitacije te mirno stanje/slobodni pad; Z4 povratni
račun razlike tlakova, zajednički pomak reference i zamjena točaka; Z5 obje
nejednakosti i promjena odluke za stabilan ali pogrešan niz te za oscilirajući
niz blizu ravnoteže; Z6 granica alpha, provjera postavke 0,78 i intervala brzine.

Notebook `u04_paraboloidna_povrsina.ipynb` zasebno provjerava integraciju
radijalnog gradijenta, volumen i konvergenciju; nije vezan za stari Z5.
Nema potrebe mijenjati ga. D03 uskladiti s novim pogreškama; D06 i manifest
obnoviti generatorima. Kanonski verifier jest `tools/verify_u04.py`.


## Provedeno

- Zamijenjeni su Z4/Z5, dopunjeni Z3/Z6 i precizirana geometrija Z2.
  Teorija, P1–P6 i završni sažetak ostali su identični početnom izvoru.
- SVG ostaje u postojećem rasporedu 2×3, s istim osnovnim dimenzijama,
  paletom, šrafurom i gradijentima. Dubine i rotacijske parabole prate podatke;
  Z3 razlikuje brzinu od ubrzanja, Z4 nema zadani smjer vrtnje, Z5 odvojeno
  prikazuje referentni profil i očitanja, a usis Z6 je zatvoren.
- D03 je usklađen. D06 i manifest obnovljeni su generatorima. Novi odgovori
  Z5/Z6 sažeti su ispod ograničenja generatora od 500 znakova, pa D06 čuva
  sve tražene kontrolne vrijednosti i ograničenja modela. U Z4/Z5 uklonjeni
  su prijelomi sažetaka unutar Markdown naglaska odnosno matematičkog zapisa.
- Tablica Z5 ima lokalni Typst blok bez dijeljenja preko stranice. Podatci
  i njihova HTML tablica ostaju isti; zajednički predložak nije mijenjan.
- Očuvanje prethodnih lokalnih promjena U03 i omotača U02/U11 provjereno
  je usporedbom SHA-256 sa stanjem na početku ovog zahvata.

## Računske i strukturne provjere

- `python tools/verify_all.py`: PASS svih 19 modula, 1094 zapisa
  (984 usporedbe s referentnim vrijednostima i 110 provjera dimenzija,
  granica ili invarijanti) te 22 zasebne neovisne fizikalne provjere.
  U04 ima 75 uspješnih provjera; pokrivenost manifesta je 90/90.
- `audit_publication.py`, `audit_typst.py`, normalizacija javnog teksta
  i generator D06 prolaze. Ostaju 90 zadataka i 87 riješenih primjera.
- Provjera preglednikom na 320, 768 i 1440 px obuhvaća šest zadataka,
  propisane razine, jedinstvene ID-jeve, oba stara sidra, svih 12 sklopivih
  blokova tipkama Enter/Space, izostanak vodoravnog prelijevanja stranice
  i šest povratnih poveznica iz D06.

Autorska procjena: novi Z4 uvodi obrnuti problem i ograničenje informacije
iz tlakova, a novi Z5 zasebno ispituje opravdanost modela. To je obrazloženje
raznolikosti i razina zadataka; prolazak računalnih provjera sam po sebi
nije dokaz didaktičke kvalitete.


## Završni prikaz i ograničenja provjere

- `quarto render` i `quarto render --profile pdf --to typst`: PASS.
  Završni PDF ima 305 stranica. Vizualno su pregledani tablica Z5 na str. 83,
  skice na str. 84 te kontrolni odgovori Z5/Z6 na str. 290. Tablica je cijela,
  skice bez odrezanih oznaka, a ključ sadrži i preporuku i rezervu za Z6.
- `audit_pdf.py`: PASS; nakon kopiranja PDF-a u lokalni `_site/downloads`
  prema objavnom workflowu prolazi i `audit_rendered_site.py`: 24 stranice,
  210 slika, 1916 poveznica i 434 sklopiva bloka. To je lokalni pregled,
  ne objava na GitHub Pages.
- Završna provjera U04 u pregledniku ponovljena je nakon dorada prijeloma
  i odgovora; sve tri širine te D06 prolaze. `git diff --check`: PASS.
- Lokalni Quarto je 1.9.32, a CI koristi 1.9.37. Cijeli udaljeni CI nije
  pokrenut. Notebookovi nisu mijenjani niti ponovno izvršavani, a JupyterLite
  nije ponovno građen. Postojeća Typst upozorenja za `times.circle` odnose
  se na U10 i nisu posljedica ovog zahvata.

## Naknadni popravak svih skica U04

Korisnik je nakon popravka U03 zatražio isti pregled i provedbu za cijelo
poglavlje 4. Opseg ove dopune obuhvaća svih sedam uključenih SVG-ova,
pripadajuće fizikalne pretpostavke, računske ispravke i verifikator.
Raniji odjeljci ostaju evidencija zamjene vježbi. Sadašnji popravak ne
mijenja tekst ni odgovore Z1–Z6, raspodjelu razina, ID-jeve ili QMD omotače.

| Skica | Nalaz i popravak |
| --- | --- |
| Uvodni pregled | U separatoru su vektori pomaknuti na stvarnu parabolu i postavljeni okomito na njezinu lokalnu tangentu. Formula tlaka sada koristi g za okomitu dubinu uz a_z=0; ranije je uz neodređenu dubinu stajao g_eff. Za brod je navedena lokalna aproksimacija L mnogo manje od polumjera zavoja. |
| P1, laboratorijska kolica | Ispravljen predznak inercijskog ubrzanja u izdvojenom vektorskom prikazu; g_eff je stvarni zbroj g i −a. Nagib, dubine i duljina koriste isto mjerilo. Oznaka strelice govori o ubrzanju, ne brzini. Kote su odmaknute od stijenki. |
| P2, kosa stijenka | Raniji plinski prostor prividno je obilazio vrh pregrade AB, pa nije bilo jasno zašto pretlak daje neto silu. AB je sada nepropusna vanjska stijenka s nastavkom do poklopca; izvana je izričito atmosferski tlak. Slobodna površina završava u A, tlakovi i rezultanta okomiti su na AB, a hvatište je na izračunanoj udaljenosti. Popravljen i vektorski zbroj u izdvojenom prikazu. |
| P3, rotirajući cilindar | Prijašnja kubična krivulja s gotovo ravnim dnom zamijenjena je točnom kvadratnom parabolom. Očuvani su mjerilo radijusa i dubina te cilindrični volumen. Razmaknute su preklopljene oznake Δh i Δh/2. |
| P4, granica prelijevanja | Postojeća parabola i granični profil bili su fizikalno primjereni. Precizirane su radne razine i odmaknute oznake kota. Tlakovi C/D označeni su kao skalari uz mjerne točke na dnu. |
| P5, kočenje autocisterne | Uklonjen je nepropusni krov koji je proturječio modelu prelijevanja preko boka; izričito je riječ o idealiziranom otvorenom pravokutnom spremniku. Presjek ima isto vodoravno i okomito mjerilo. Obje kote Δh/2 sada polaze od mirne razine, uz očuvan volumen i pravi nagib. |
| Z1–Z6 | Z4 dobiva centriranu os rotacije uz očuvan omjer rB/rA=3 i mjerne točke u fluidu. Z6 dobiva stvarnu kotu dubine na osi. Navedeno je da su širine malih presjeka shematske, dok visine u pojedinom panelu imaju isto mjerilo. Ostali ispravni prikazi i sintetički podatci očuvani su. |

Zadržani su postojeći rasporedi panela, paleta, šrafure, gradijenti i fontovi.
Nije dodan novi primjer niti zamijenjen zadatak. Rotacijski notebook ostaje
zaseban pokus s omega=7 rad/s, R=0,55 m i h0=0,70 m; njegov profil i volumen
usklađeni su s teorijom te ne zahtijevaju promjenu zbog ovih popravaka.

### Matematičko i tekstualno usklađivanje

- U izvedenom uvjetu ogoljavanja dodan je izostavljeni kvadrat:
  `(omega_crit)^2 R^2 = 4 g h0`. Konačna formula za omega bila je ispravna.
- P2 razlikuje ukupnu silu za b=1 m od sile po širini F_R/b. Račun s
  nezaokruženim veličinama daje F0=9313,55 N, Fh=1688,62 N,
  FR=11002,17 N i yR=0,30594 m. Usklađeni su skica i verifikator.
- P3: h_rub=0,392385 m, h_osa=0,167615 m. Zaokruženje ruba na tri
  decimale iznosi 0,392 m; prethodnih 0,393 nastalo je preranim
  zaokruživanjem razlike razina.
- P5: h_pred=0,682416 m, h_str=0,217584 m, odnosno 0,682/0,218 m.
  Prelijevanje nastupa prije formalne granice ogoljavanja bez gubitka
  volumena; tekst sada izričito kaže da nakon prelijevanja treba novi račun.
- U P1 razlikuju se smjer ubrzanja i smjer brzine. Svi stabilni ID-jevi
  jednadžbi ostali su isti, kao i postojeći verifier ID-jevi.

### Provjere popravka

- U04 prolazi svih 75 provjera. Ukupni `verify_all.py` prolazi s 1096
  zapisa: 986 usporedbi s ciljevima, 110 invarijanti i dodatne 22 neovisne
  fizikalne provjere; pokrivenost zadataka 90/90. Uz ispravljene brojeve
  tolerancije su pooštrene, bez slabljenja audita.
- Neovisna provjera samih SVG koordinata potvrđuje vektorske zbrojeve,
  okomitost površine i efektivne gravitacije, okomitost sile na AB,
  položaj rezultante, nagibe te volumne bilance. Volumen obaju rotacijskih
  primjera dobiven je integracijom nacrtane kvadratne krivulje s radijalnom
  težinom 2*pi*r; nije provjeren samo izgled krivulje.
- Svih sedam SVG-ova pregledano je u Edgeu; tekst ostaje unutar granica.
  Provjereni su nepropusna oplata P2, otvoreni rub P5 i zatvoreni usis Z6.
- SHA-256 usporedba potvrđuje očuvanje prethodnih izmjena drugih poglavlja,
  uključujući U03. Tekst vježbi i ostatak U04 nakon njih identični su
  početku ovog popravka. Manifest i D06 ostaju aktualni prema generatorima.
- Puni HTML i Typst render prolaze. PDF audit prolazi za 305 A4 stranica;
  vizualno pregledane sve slike 4.1–4.7 na stranicama 69, 73, 74, 76, 77,
  80 i 84 te popravljene jednadžbe na stranicama 72 i 75.
- HTML provjera na 320/768/1440 px potvrđuje šest zadataka i propisane
  razine, oba stara sidra, jedinstvene ID-jeve, 12 sklopivih blokova koji
  rade tipkovnicom, poveznice D06 i izostanak vodoravnog prelijevanja.
- Nakon kopiranja PDF-a u lokalni `_site/downloads`, audit konačne stranice
  prolazi: 24 stranice, 210 slika, 1916 veza i 434 sklopiva bloka.
  Prolaze i audit publikacije, Typst blokova, normalizacija javnog teksta
  te `git diff --check`.

Ovo je lokalna validacija. Udaljeni objavni CI, ponovno izvršavanje
notebooka i gradnja JupyterLite nisu dio ovog popravka. Quarto 1.9.32
uspješno je izradio knjigu; CI koristi 1.9.37. Ranija upozorenja za
`times.circle` u U10 ostaju. Commit i push nisu napravljeni.
