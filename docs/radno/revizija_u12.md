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
| P1 | `ex-konvektivno-ubrzanje`; u du/dx | ZADRŽATI: osnovna tehnika, razlikovanje stacionarnosti i ubrzanja | T1 | isti | verifier, prikaz | planirano |
| P2 | `ex-uljni-film`; superpozicija pogona | ZADRŽATI: dva pogona istog smjera, osnova za Z4 | T2 | isti | rubni uvjeti, verifier | planirano |
| P3 | `ex-laminarni-mikrokanal`; izravni pad tlaka | ZADRŽATI: osnovni laminarni slučaj; Z3 daje obrnuti račun i nesigurnost | T2 | isti | verifier | planirano |
| P4 | `ex-granicni-sloj`; Blasius kao uvjetna referenca | ZADRŽATI: ne proglašavati prijelaz univerzalnim pragom | T2 | isti | verifier | planirano |
| P5 | `ex-intenzitet-turbulencije`; u_rms/U | ZADRŽATI: tumačenje signala, ne etiketa režima | T3 | isti | verifier | planirano |
| Z1 | `task-materijalna-derivacija`; lokalni i konvektivni član | PREPRAVITI sitno: eksplicitne jedinice koeficijenata i kinematički smisao, naputak | T1 | isti | SVG, verifier, D06 | planirano |
| Z2 | `task-viskozna-difuzija`; H²/ν | PREPRAVITI sitno: vremensko mjerilo nije točan trenutak uspostave profila | T1 | isti | SVG, verifier, D06 | planirano |
| Z3 | `task-poiseuille-inverzni`; μ i RSS | ZADRŽATI račun; sintetički podatci, ± kao standardne nesigurnosti, L između tlačnih priključaka | T2 | isti | SVG, notebook, verifier | planirano |
| Z4 | `task-couette-povrat`; kritični gradijent i τ₀ | ZADRŽATI problem; razjasniti komponentu naprezanja i lokalni povratni tok bez prolaza kroz ploče | T2 | isti | SVG, rubni uvjeti, verifier | planirano |
| Z5 | `task-granicni-sloj-model`; procjena prikladnosti | ZADRŽATI: vrijedan izbor modela; dopuniti sintetičku provenijenciju i skicu | T3 | isti | SVG, verifier | planirano |
| Z6 | `task-cfd-tri-mreze`; red/GCI/validacijski dokazi | PREPRAVITI: izabrati mrežu uz GCI i maseni prag, uskladiti preciznost s tiskanim podatcima | T4 | isti | CSV, SVG, notebook, verifier, D06 | planirano |

`rewrite_status`: in_progress; `rewrite_level`: selective;
`sketch_requirement`: ispraviti uvod i dodati skice šest vježbi.
Ne uvode se novi task ID-jevi niti mijenjaju omotači. Novi podatci i
odluke autorski su nastavni primjeri; CFD paket ostaje izričito sintetički.

## Rezultati

Dopuniti nakon provedbe i provjera.
