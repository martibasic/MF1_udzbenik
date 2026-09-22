# Revizija U12 — diferencijalni opis realnog toka

## Dijagnoza prije provedbe

Pet primjera pokriva konvektivno ubrzanje, Couette–Poiseuilleov tok,
laminarni mikrokanal, granicu Blasiusova modela i intenzitet turbulencije.
Šest samostalnih zadataka već ima raznolike aktivnosti: diferenciranje,
procjenu vremenskog mjerila, obrnuti mjerni problem, promjenu predznaka
smicanja, izbor modela te mrežnu konvergenciju. Nije opravdana potpuna
zamjena dobrih zadataka. Potrebno je jasno označiti sintetičke podatke,
standardne nesigurnosti i fizičke pretpostavke te dodati stvarnu odluku
o mreži u Z6. Povezani notebook trenutačno koristi nominalni laminarni
slučaj čiji bi Re za vodu bio previsok; ulazi se usklađuju s laminarnim
referentnim slučajem iz podatkovnog paketa.

Postoji samo uvodna slika, bez skica vježbi. Na uvodu strelica smicanja
ima marker druge boje, donji rub graničnog sloja odvojen je od stijenke,
a druga plava ispuna može izgledati kao drugi fluid. Vremenski signal
nema osi ni jasno označene sintetičke provenijencije. Novom zajedničkom
slikom treba prikazati svih šest stvarnih problema, s otvorenim kapilarama,
točnim mjernim razmakom, rubnim uvjetima i fizičkim značenjem kota.

## Matrica prije provedbe

| Mjesto | Postojeći ID i uloga | Odluka i didaktička korist | Razina | Završni ID | Povezane provjere | Status |
| --- | --- | --- | --- | --- | --- | --- |
| P1 | `ex-konvektivno-ubrzanje`; u du/dx | ZADRŽATI: osnovna tehnika, razlikovanje stacionarnosti i ubrzanja | T1 | isti | verifier, prikaz | provedeno |
| P2 | `ex-uljni-film`; superpozicija pogona | ZADRŽATI: dva pogona istog smjera, osnova za Z4 | T2 | isti | rubni uvjeti, verifier | provedeno |
| P3 | `ex-laminarni-mikrokanal`; izravni pad tlaka | ZADRŽATI: osnovni laminarni slučaj; Z3 daje obrnuti račun i nesigurnost | T2 | isti | verifier | provedeno |
| P4 | `ex-granicni-sloj`; Blasius kao uvjetna referenca | ZADRŽATI: ne proglašavati prijelaz univerzalnim pragom | T2 | isti | verifier | provedeno |
| P5 | `ex-intenzitet-turbulencije`; u_rms/U | ZADRŽATI: tumačenje signala, ne etiketa režima | T3 | isti | verifier | provedeno |
| Z1 | `task-materijalna-derivacija`; lokalni i konvektivni član | PREPRAVITI sitno: eksplicitne jedinice koeficijenata i kinematički smisao, naputak | T1 | isti | SVG, verifier, D06 | provedeno |
| Z2 | `task-viskozna-difuzija`; H²/ν | PREPRAVITI sitno: vremensko mjerilo nije točan trenutak uspostave profila | T1 | isti | SVG, verifier, D06 | provedeno |
| Z3 | `task-poiseuille-inverzni`; μ i RSS | ZADRŽATI račun; sintetički podatci, ± kao standardne nesigurnosti, L između tlačnih priključaka | T2 | isti | SVG, notebook, verifier | provedeno |
| Z4 | `task-couette-povrat`; kritični gradijent i τ₀ | ZADRŽATI problem; razjasniti komponentu naprezanja i lokalni povratni tok bez prolaza kroz ploče | T2 | isti | SVG, rubni uvjeti, verifier | provedeno |
| Z5 | `task-granicni-sloj-model`; procjena prikladnosti | ZADRŽATI: vrijedan izbor modela; dopuniti sintetičku provenijenciju i skicu | T3 | isti | SVG, verifier | provedeno |
| Z6 | `task-cfd-tri-mreze`; red/GCI/validacijski dokazi | PREPRAVITI: izabrati mrežu uz GCI i maseni prag, uskladiti preciznost s tiskanim podatcima | T4 | isti | CSV, SVG, notebook, verifier, D06 | provedeno |

`rewrite_status`: complete; `rewrite_level`: selective;
`sketch_requirement`: ispraviti uvod i dodati skice šest vježbi.
Ne uvode se novi task ID-jevi niti mijenjaju omotači. Novi podatci i
odluke autorski su nastavni primjeri; CFD paket ostaje izričito sintetički.

## Rezultati

Provedena je selektivna dorada svih šest mjesta bez promjene task ID-jeva.
Z1 izričito zadaje dimenzije koeficijenata kinematičkog polja, Z2 razlikuje
vremensko mjerilo od točnog vremena uspostave, a Z3 jasno zadaje neovisne
standardne nesigurnosti i mjerni razmak u potpuno razvijenom toku. Z4
definira silu fluida na donju ploču i provjerava oba profila: povrat je u
otvorenom intervalu 0 < y < H/11, uz nultu brzinu na nepomičnoj ploči.
Z5 dodatno povezuje gradijent vanjske brzine s nepovoljnim gradijentom tlaka
od +374 Pa/m. U Z6 student bira mrežu pomoću dvaju neovisnih kriterija.
Račun s ispisanim zaokruženim protocima daje p = 2,00012246,
Q_ext = 7,85398889e-6 m³/s, GCI_m = 1,23748682 % i GCI_f = 0,31165956 %;
objavljena preciznost i tolerancije usklađene su s tim ulazima.

Pet riješenih primjera zadržano je. U teoriji i odgovoru samoprovjere
ciljano je ograničena tvrdnja o odvajanju: promjena znaka smicanja u
potpuno razvijenom Couette–Poiseuilleovu toku sama ne dokazuje odvajanje
strujnica od ploče. D03 navodi odgovarajuće tipične pogreške.

Uvodna slika zadržava trodijelni raspored. Zamišljeni element nema krute
stijenke, gradijent sloja je unutar jedne neprekinute ispune do ploče,
a sintetički signal ima osi i stvarnu vremensku sredinu. Nova datoteka
`u12_realni_tok_vjezbe_skice.svg` prikazuje svih šest vježbi. Naslijeđeni
`u12_vjezbe_skice.svg` pripada današnjem U14 i njegov sadržaj nije mijenjan
ovom revizijom. Tlačni priključci u Z3 imaju stvarne otvore, L spaja njihove
osi, H i D mjere unutarnji razmak, a mrežne crte Z6 nisu stijenke.

Notebook koristi referentni slučaj iz Poiseuilleova paketa: R = 0,010 m,
Δp = 2,004 Pa, μ = 1,002 mPa s, L = 1 m, ρ = 998,2 kg/m³, Re = 498,10.
Zasebno računa Z3, crta stvarne profile Z4 i bira mrežu Z6. Sadrži čiste
izlaze, fiksno sjeme, provjere prianjanja/nesigurnosti/konvergencije i
završna pitanja interpretacije. Sintetički ulazi označeni su kao takvi.

Postupak GCI-ja uspoređen je s primarnom dokumentacijom
[NASA NPARC — Examining Spatial Convergence](https://www.grc.nasa.gov/www/wind/valid/tutorial/spatconv.html).
Zadatci i skice autorska su prerada; nije preuzet tuđi tekst zadatka.

Izvršene provjere:

- `verify_u12_real_flow.py`: 53 rezultata, bez pogreške; dodatno stvarni
  predznaci profila, povratna zona, gradijent tlaka, srednji GCI, oba uvjeta
  izbora i podudarnost ispisanih podataka s arhivskim zaokruživanjem.
- `verify_all.py`: 90/90 ugovora, 1057 golden usporedbi, 191 invarijanta i
  22 dodatne neovisne fizikalne provjere; bez tautologija i rupa.
- `check_u12_sketch_geometry.py`: oba SVG-a; stijenke/otvori/kote/smjerovi,
  korijenski rast sloja, integrirana sredina signala i pročišćenje domene.
- Izvršenje promijenjenog notebooka od početka: PASS, 4,77 s.
- Normalizacija, generator D06 i manifesta, publication i Typst audit:
  PASS; 87 primjera i 90 zadataka, svih šest mjesta U12 očekivanih razina.
- Stvarni HTML na 320, 768 i 1440 px: šest zadataka, svi postojeći ID-jevi,
  12 otvaranja/zatvaranja pomoći tipkovnicom, bez vodoravnog preljeva;
  automatizirani WCAG A/AA PASS. D06 ima šest ključeva i ispravne povratne
  veze; matematički izrazi i kontrolni odgovori nisu odrezani generatorom.
- Nativni PDF: 315 stranica A4, audit PASS. Pregledane rasterizirane
  stranice 213 (uvod), 218–220 (skice i sve vježbe), 309–310 (ključ).
  Konačni pregled uklanja i dodir oznake presjeka s isprekidanom crtom Z5.

Ovo je autorski i računalni pregled, ne tvrdnja o neovisnoj stručnoj
recenziji. Zajednička završna objava, JupyterLite i puni viewport prolaz
slijede nakon svih šest koraka šireg cilja; ova revizija nije novi push.
