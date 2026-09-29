# Strujanje iza stepenice: stvarno mjerenje i objavljeni CFD

Paket prati primjer ponovnog priljubljivanja toka u 12. poglavlju
sveučilišnog priručnika. Mjerenja Drivera i Seegmillera (1985.) i objavljeni
CFL3D/SSTm rezultati preuzeti su iz [Turbulence Modeling Resourcea](https://tmbwg.github.io/turbmodels/backstep_val.html).
Ovdje je provedena obrada tih podataka, bez pokretanja nove CFD simulacije.

## Uvjeti i podrijetlo

- stepenica visine H, vodoravan suprotni zid; Re prema H približno 36 000;
- CFD pri Ma = 0,128, uz razvijanje odgovarajućeg ulaznog graničnog sloja;
- x/H se mjeri od stepenice, a Uref u sredini kanala približno na x/H = −4;
- Cf = τw / (ρ Uref² / 2), s predznakom srednjega zidnog smicanja;
- izvorna mjerenja: [Driver i Seegmiller](https://doi.org/10.2514/3.8890);
- izvor CFD-a, naziv varijante modela i ograničenja:
  [CFL3D/SSTm](https://tmbwg.github.io/turbmodels/backstep_val_sst.html).

`sources/cf.exp.dat` čuva svih 20 mjernih redaka i izvorni stupac `error`.
`sources/backstep_cfl3d_cf_sst.dat` čuva cijelu objavljenu CFD tablicu.
`sources/profiles.exp.dat` čuva mjerene profile, primjerice negativnu srednju
brzinu u području iza stepenice. Nisu digitizirani grafovi. Datoteke imaju
normalizirane završetke redaka; URL-ovi i SHA-256 zapisi su u `provenance.json`.

`comparison.csv` izdvaja četiri neizmijenjena retka koji omeđuju odabranu
nultočku. Za tablicu u priručniku CFD brojevi su zaokruženi. Stupac `error`
prenesen je kao objavljen podatak bez pretpostavljanja njegove raspodjele
ili faktora pokrivanja. Nije uključen u izmišljeni budžet nesigurnosti.

## Ponovljiv račun

Linearna interpolacija daje x/H = 6,27866 za mjerne retke i 6,54347 za
CFD retke. Izvor zasebno navodi eksperimentalno ponovno priljubljivanje
6,26 ± 0,10; interpolacija rijetke tablice nije zamjena za tu objavljenu
procjenu. Odstupanje CFD-a prema 6,26 jest +0,28347 H, odnosno +4,5283 %.
Sažetak CFD stranice navodi približno 6,50; račun u priručniku dosljedno
koristi nultočku priložene tablice, a ne taj približni sažetak.

Izračun je uključen u postojeću bilježnicu o realnom toku i konvergenciji.
`python tools/validate_cfd_vv.py` provjerava cijelost arhiva, prijenos redaka,
uvjete i granice zaključka. `python tools/verify_u12_real_flow.py` neovisno
provjerava objavljene računske rezultate.

## Što zaključak obuhvaća

Mjerni raspon iznosi [6,16; 6,36]. U njemu je interpolacija mjernih redaka,
a izvan njega rezultat CFD-a. Stranica izvora ne specificira faktor
pokrivanja tog raspona; zato ga ne zovemo standardnom nesigurnošću ni
95-postotnim intervalom. Izvor za SSTm navodi kvazistacionarni odziv i
izostanak potpune studije mrežne konvergencije. Usporedba utvrđuje
odstupanje jednog izlaza, ali ne daje cjelovitu validacijsku presudu niti
jedinstveno određuje uzrok odstupanja. Novi slučaj ne popunjava povijesti
reziduala ili nesigurnosti koje nedostaju drugom pokusu, NACA 0012.
