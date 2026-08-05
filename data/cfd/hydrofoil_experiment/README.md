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

## Što se ne smije tvrditi

Arhiva integralnih rezultata ne sadrži reziduale, povijest monitora sila ni
maseni debalans, a distribuirana eksperimentalna tablica nema potpuni budžet
mjerne nesigurnosti. Zato ovaj paket **nije dovršena validacijska presuda**.
Student koji pokrene novu simulaciju mora dodati te tri dijagnostike, a tek
zatim spojiti numeričku i mjernu nesigurnost.

NACA 0012 ovdje služi kao profilni primjer prenosiv na hidrodinamiku preko
bezdimenzijskih koeficijenata. Slobodna površina, kavitacija, hrapavost i drugi
učinci specifični za hidroprofil zahtijevaju zaseban model i podatke.
