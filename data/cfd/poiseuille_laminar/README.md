# Laminarni Poiseuilleov tok

Ovo je slučaj **verifikacije rješenja** s poznatim analitičkim odgovorom.
Voda struji kroz cijev promjera 20 mm i duljine 1 m pri nametnutom padu tlaka
2,004 Pa. Reynoldsov broj temeljen na srednjoj brzini iznosi približno 498, pa
je laminarni model konzistentan.

Tri sintetičke mreže imaju omjer karakteristične veličine `r=2`. Profilna
perturbacija konstruirana je tako da nestaje na stijenci i daje urednu
konvergenciju drugoga reda prema paraboličnom profilu. CSV zapisi nisu nastali
pokretanjem solvera; točno pravilo konstrukcije nalazi se u `provenance.json`.

Za studentsku provjeru treba odvojeno pokazati:

1. `Q`, `u_max=2*Umean`, `Delta p` i `tau_w` iz analitičkih relacija;
2. maseni debalans svake mreže;
3. smanjenje reziduala i stabilizaciju protoka;
4. opaženi red i GCI iz tri integralna rezultata;
5. razliku između iteracijske konvergencije i prostorne konvergencije.
