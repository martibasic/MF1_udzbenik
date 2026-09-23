# NACA 0012 profil — javni validacijski referentni skup

Paket povezuje javne eksperimentalne sile Charlesa Ladsona (NASA TM 4074) s
objavljenim FUN3D rezultatima na tri mreže iz NASA Turbulence Modeling
Resourcea. Uspoređuju se $C_L$ i $C_D$ pri približno 10° za $Re_c=6\cdot10^6$
i $Ma=0{,}15$. Nije provedeno digitiziranje grafova: CSV vrijednosti preuzete su
iz strojno čitljivih tablica koje NASA TMR izravno distribuira.

## Što se može provjeriti

- tri najfinije stvarne FUN3D mreže iste NASA TMR obitelji II;
- zatvaranje $C_D=C_{D,p}+C_{D,v}$;
- opaženi red i GCI za monotono konvergentne $C_L$ i $C_D$;
- razlika CFD-a prema najbližoj mjernoj točki od 10,10°.

`grids.csv` koristi `structured_points = points_i * points_j`, odnosno NASA-in
broj **strukturiranih točaka**, ne ćelija. Najfinija mreža ima 7169 × 2049
točaka. Uklanjanje dvostrukih točaka u tragu mijenja broj jedinstvenih čvorova
nestrukturirane mreže; taj se broj ovdje ne tvrdi. Stupci `cells` i
`h_sqrt_inverse_cells` preimenovani su radi ispravka značenja. Koeficijenti
i rezultati tro-mrežnog računa nisu promijenjeni.
[NASA opis mreža](https://tmbwg.github.io/turbmodels/naca0012numerics_grids.html).

Izvorne male tablice sačuvane su u `sources/`, s normaliziranim SHA-256
hashovima u `provenance.json`. Validator uspoređuje svih 18 mjernih redaka
i svih sedam vrijednosti na svakoj od tri odabrane CFD mreže s tim izvornicima.

## Dovršena nastavna usporedba za Z6 u 12. poglavlju

`teaching_comparison.json` daje sve podatke za samostalan račun usporedbe
otpora. Izvorne tablice ostaju sačuvane. Najfiniji CFD rezultat zaokružen je
na `CD = 0.01222`; mjerenja na 8,08° i 10,10° linearno su interpolirana na
isti kut 10,00°, pa je referenca zaokružena na `CD = 0.01166`.

Nedostajuće standardne nesigurnosti **pretpostavljene su za nastavu**:
`u_m = 0.00020`, `u_n = 0.00010`, `u_v = 0.00010`. To su apsolutni doprinosi
bezdimenzijskom koeficijentu; predstavljaju oko 1,7 % mjerne reference,
oko 0,8 % CFD vrijednosti te učinak usklađivanja uvjeta i interpolacije.
Lokalni mjerni nagib od približno 0,000891 po stupnju motivira red veličine
posljednjeg doprinosa uz pretpostavljenu preostalu nesigurnost kuta reda
0,1°. Nije riječ o izmjerenom budžetu. Numerički doprinos je ukupna
pretpostavka; GCI se ne pribraja ponovno niti se preuzima iz Poiseuillea.

Uz neovisne normalne doprinose centrirane na nulu nakon korekcija i poznate
standardne nesigurnosti, `U_E = 2 sqrt(u_m² + u_n² + u_v²)` odgovara približno
95 % pokrivanja. U osnovnom scenariju `E = +0.00056` (oko +4,80 %) premašuje
`U_E ≈ 0.000490`. Uz `u_m = 0.00030`, `U_E ≈ 0.000663` obuhvaća razliku:
zadani kriterij slaganja tada je zadovoljen, bez poboljšanja samog modela.
Zadatak i njegova analiza osjetljivosti time su rješivi iz zadanih podataka.
Arhivske dijagnostike nisu rekonstruirane ni zamijenjene izmišljenim zapisima.

Metoda kombiniranja standardnih nesigurnosti i pretpostavke faktora pokrivanja:
[NIST TN 1297, §5](https://www.nist.gov/pml/nist-technical-note-1297/nist-tn-1297-5-combined-standard-uncertainty)
i [§6](https://www.nist.gov/pml/nist-technical-note-1297/nist-tn-1297-6-expanded-uncertainty).
NIST daje metodu, a ne brojčane nesigurnosti ovog nastavnog primjera.

## Granice zaključka o izvornom arhivu

Arhiva integralnih rezultata ne sadrži reziduale, povijest monitora sila ni
maseni debalans, a distribuirana eksperimentalna tablica nema potpun popis doprinosa
mjernoj nesigurnosti. Zato ovaj paket **nije dovršena validacijska presuda**.
Student koji pokrene novu simulaciju mora dodati te tri vrste dijagnostičkih podataka, a tek
zatim spojiti numeričku i mjernu nesigurnost.

Tro-mrežni GCI u `uncertainty.json` jest **uvjetna procjena**, a monotoni niz
sam ne potvrđuje asimptotsko područje. Prateći rad izvještava o vrlo malim
FUN3D rezidualima (str. 3), ali zaključuje da asimptotski red nije konačno
utvrđen (str. 41). Objavljeni sažetak konvergencije razlikujemo od izvornih
iteracijskih zapisa. Graf reziduala na sl. 59 tog rada pripada ravnoj ploči,
pa se ne može koristiti kao povijest ovog profila.
[Diskin i sur., AIAA 2015-1746](https://fun3d.larc.nasa.gov/papers/aiaa-2015-1746.pdf).

## Dopuna iz primarnih izvora, 23. rujna 2026.

Ladsonov izvještaj na tiskanoj str. 2 (PDF str. 4) navodi točnost tlačnih
pretvornika i razlike ponovljenih mjerenja blizu nultog napadnog kuta.
Vrijednosti i njihovo područje primjene uneseni su u `uncertainty.json`.
To nisu standardne nesigurnosti pri 10,10°; koeficijent normalne sile
`CN` iz tog odlomka također se ne smije zamijeniti koeficijentom uzgona `CL`.
Bez raspodjela, korelacija, tunelskih korekcija i pripadnih podataka ne
izračunavamo izmišljeni kombinirani interval.
[Ladson, NASA TM 4074](https://ntrs.nasa.gov/citations/19880019495).

Dodatno je provjeren rad Freemana i Roya: na tiskanoj str. 90–91 (PDF
str. 7–8) koristi mjernu nesigurnost otpora od 2,5 % za **napadni kut 0°**,
uz pozivanje na Ladsona. Taj navod ne daje potpunu nesigurnost naše točke
pri 10,10° i nije prenesen u njezin proračun.
[Freeman i Roy, 2014.](https://www.cobaltcfd.com/pdfs/V%26VexternalTurbFlow.Freeman.AeroSci%26Tech.published.20140127.pdf).

`source_review.json` evidentira pregledane izvore, hashove izvještaja i
potpuni popis datoteka dviju relevantnih TMR mapa u provjerenom Git stablu.
U njima nisu pronađene tražene sirove povijesti ni masena bilanca.
Za dovršetak trebaju zapisi za svaku odabranu mrežu, definicija i
normalizacija reziduala, `CL/CD` kroz iteracije, potpisani rubni maseni
tokovi te potpuni mjerni budžet na usporednom kutu. Novi proračun daje
dokaze za taj novi proračun; ne potvrđuje automatski stare NASA rezultate
niti nadomješta nedostajuću eksperimentalnu nesigurnost.

NACA 0012 ovdje služi kao profilni primjer prenosiv na hidrodinamiku preko
bezdimenzijskih koeficijenata. Slobodna površina, kavitacija, hrapavost i drugi
učinci specifični za hidroprofil zahtijevaju zaseban model i podatke.
