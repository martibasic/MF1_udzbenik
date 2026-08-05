# CFD V&V podatkovni slučajevi

Ova mapa sadrži male, strojno čitljive nastavne slučajeve za učenje razlike
između **verifikacije rješenja** i **validacije fizikalnog modela**. Podaci nisu
izvoz komercijalnog ili otvorenog CFD solvera osim kada to pojedinačna
provenijenca izričito navodi; profilni slučaj sadrži objavljene FUN3D rezultate.

| Slučaj | Status | Uloga | Istina/referenca |
|---|---|---|---|
| `poiseuille_laminar` | spreman | verifikacija rješenja | analitičko Hagen–Poiseuilleovo rješenje |
| `venturi_diffuser` | spreman | pedagoška verifikacija postupka | sintetički niz prema 1D Bernoulliju i propisanom gubitku |
| `hydrofoil_experiment` | referentni skup | profilna validacija uz eksplicitne arhivske praznine | Ladsonov eksperiment + NASA TMR FUN3D mreže |

## Važno ograničenje

Poiseuilleovi i Venturi/difuzor rezultati namjerno su **sintetički**. Izgrađeni
su tako da imaju tri samoslične mreže, kontrolirani red konvergencije, mali
maseni debalans i konvergentne iteracijske monitore. Oni služe za provjeru
računskog V&V postupka i za nastavu; ne smiju se predstavljati kao dokaz
točnosti određenog CFD programa, turbulencijskog modela ili stvarnog uređaja.

Za profilni slučaj preuzete su strojno čitljive Ladsonove mjerne točke i FUN3D
rezultati koje distribuira NASA TMR; nijedna točka nije digitizirana s grafa.
Arhiva nema reziduale, monitore ni maseni debalans, pa paket to jasno vodi kao
nedostajuću dijagnostiku, a ne kao dovršenu validacijsku presudu.

## Struktura spremnog slučaja

- `case.json` — geometrija, fluid, rubni uvjeti, referentne vrijednosti i pragovi;
- `grids.csv` — tri mreže i integralne veličine;
- `solver_history.csv` — reziduali i jedan fizikalni monitor kroz iteracije;
- `uncertainty.json` — tro-mrežni opaženi red i GCI;
- `provenance.json` — podrijetlo, način konstrukcije i ograničenja;
- `README.md` — ljudski čitljiv opis.

Profilni referentni paket umjesto sintetičke `solver_history.csv` sadrži
`experimental_forces.csv`. Nedostupna povijest izvornog solvera navedena je u
`case.json` i ne popunjava se izmišljenim rezidualima.

Sva polja u CSV-u imaju jedinicu u nazivu. `mass_imbalance_percent` definiran je
kao `100*abs(m_in-m_out)/max(abs(m_in),abs(m_out))`. Reziduali su
bezdimenzijski L2 reziduali kako ih definira ovaj nastavni skup, a ne univerzalno
usporediva metrika među solverima.

## Validacija strukture

Validator samo čita datoteke:

```powershell
python tools/validate_cfd_vv.py
```

Provjerava inventar, tri mreže, monotono profinjenje, maseni debalans,
smanjenje reziduala, stabilizaciju monitora, GCI zapis, analitičke/reference
vrijednosti te obveznu provenancu. Referentni profilni slučaj dodatno provjerava
izvornu mrežnu tablicu, rastav otpora te opaženi red i GCI za monotono
konvergentne $C_L$ i $C_D$ na tri najfinije mreže.

## Metoda numeričke nesigurnosti

Tro-mrežni zapisi slijede oblik GCI postupka iz rada I. B. Celika i suradnika,
„Procedure for Estimation and Reporting of Uncertainty Due to Discretization in
CFD Applications”, *Journal of Fluids Engineering* 130(7), 2008,
<https://doi.org/10.1115/1.2960953>. Ovaj mali skup koristi jednolik omjer
profinjenja `r=2` i faktor sigurnosti `Fs=1.25`; ne pokriva oscilatornu ili
statističku konvergenciju.
