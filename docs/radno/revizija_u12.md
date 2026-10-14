# Revizija U12 — diferencijalni opis realnog toka

## Revizija 12. 10. 2026. (provedba nalaza stručne recenzije)

Autorica je odobrila provedbu svih nalaza. Provedeno u
`source/u12_diferencijalni_opis_realnog_toka.md`, `tools/verify_u12_real_flow.py`
te oznakama brzine u `assets/print/u12_fig_uvod_realni_tok.svg` i
`assets/print/u12_realni_tok_vjezbe_skice.svg`. Podatci P6 i Z6 iz `data/cfd`
i bilježnica `u12_poiseuille_konvergencija.ipynb` (Z3, Z4, Z6) nisu mijenjani.

Izvodi: novi blok „Matematički izvod — Od Cauchyjeve jednadžbe do
Navier–Stokesove” (`eq-newtonska-konstitutivna-relacija`,
`eq-divergencija-viskoznog-naprezanja`, veza s $\tau=\mu\,dv/dy$ iz u02);
Poiseuilleova ODE s rubnim uvjetima (`eq-poiseuille-ode`); Reynoldsovo
osrednjavanje (`eq-reynoldsovo-osrednjavanje`) s imenima $k$–$\varepsilon$ i
$k$–$\omega$ SST te objašnjenjem oznake SSTm; 1-D primjer konačnih volumena za
Poiseuilleov tok (`eq-poiseuille-fvm-celija`), SIMPLE/PISO i FEM imenovani u
`sec-realni-tok-cfd`. Novi blok „Fizikalno značenje” uz granični sloj i
odvajanje; granica modela preimenovana u obrazac „Granica modela — …” s
definicijom tenzora $\mathbf D$. Notacija: brzina fluida $\vec v$, $v$, $v_i$,
indeksna notacija uvedena jednom rečenicom; brzina ploče $u$; srednja
presječna brzina $v$; $\overline{v}$ i $v'$ u turbulenciji; $U_\infty$, $U_e$
uz definiciju; pokazatelj $K$ u Z5 preimenovan u $m$ (Falkner–Skanov
parametar) jer je $K$ rezerviran za volumni modul. Pitanje 5 u „Provjeri
sebe” zamijenjeno (brzina u osi vs. $\tau_w$). P6: napomena o interpolaciji
preko $1{,}2H$. Z6: tekst skraćen, podatci i kriteriji nepromijenjeni. Sirova
`.qmd` poveznica zamijenjena makroom; pojašnjen uvjet „nulti gradijent” ($p$ vs.
$p_{rgh}$).

| Mjesto | Postojeći ID i uloga | Odluka | Razina | Završni ID | Kontrolni rezultat | Provjere |
| --- | --- | --- | --- | --- | --- | --- |
| P4 | `ex-granicni-sloj`; Blasius na ravnoj ploči, isti podatci kao Z5 | ZAMIJENITI: granični sloj na trupu modela broda iz pog. 11 P2 (stimulatori turbulencije, turbulentna $\delta$ na krmi, $C_F$ po ITTC 1957) | T2 | `ex-granicni-sloj-trupa-modela` (stari ID kao `<span>`) | $Re_{x_1}=5{,}4\cdot10^5$, $\delta_B=2{,}04$ mm, $Re_L=1{,}08\cdot10^7$, $\delta\approx88$ mm, $C_{F,m}=2{,}96\cdot10^{-3}$, $C_{F,s}=1{,}48\cdot10^{-3}$ | `U12.REAL.P4.*` (6 golden, 2 invarijante) |
| P5 | `ex-intenzitet-turbulencije`; jedno dijeljenje s oznakom T3 | PREPRAVITI u stvarnu odluku: $I\to k$ uz izotropiju, $\omega$ iz dogovorne skale $\ell=0{,}07D$ s osjetljivošću | T3 | isti | $I=6{,}0$ %, $k=0{,}346$ m²/s², $\omega\approx51$ s⁻¹, $\varepsilon\approx1{,}59$ m²/s³ | `U12.REAL.P5.*` (5 golden, 2 invarijante) |
| Z5 | `task-granicni-sloj-model` | NOTACIJA: $K\to m$; brojevi isti | T3 | isti | $m=-0{,}0667$ | nepromijenjene |
| Z6 | `task-cfd-tri-mreze` | SKRATITI tekst; podatci i kriteriji isti | T4 | isti | nepromijenjen | nepromijenjene |

Provjere: `verify_u12_real_flow.py` 76 rezultata bez pada (prije 66);
`check_u12_sketch_geometry.py` PASS; `audit_sketch_design.py` bez poruka za
U12 skice. Nije stvorena nova skica za P4 (stari P4 nije imao skicu; nova bi
datoteka bila opcionalna). Ovo je autorska provedba recenzentskih nalaza;
D01/D02/D04/D06 i manifest usklađuje koordinator.

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
