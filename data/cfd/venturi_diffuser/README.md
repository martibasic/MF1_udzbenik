# Venturi i difuzor

Ovaj je slučaj namjerno označen kao **sintetički pedagoški skup**, a ne kao
eksperimentalna validacija ili stvarni izlaz CFD solvera.

Kontinuitet daje brzine u ulazu i grlu. Idealni pad statičkog tlaka do grla
slijedi iz Bernoullijeve jednadžbe, dok je ukupni gubitak propisan s
`K_loss=0,2` u odnosu na dinamički tlak u grlu. Tri mreže zatim dobivaju
kontrolirane pogreške drugoga reda.

Skup omogućuje provjeru četiri odvojena pitanja:

1. zatvara li se masena bilanca;
2. jesu li reziduali pali i je li fizikalni monitor stabilan;
3. konvergiraju li pad tlaka i ukupni gubitak monotono;
4. je li diskretizacijska nesigurnost odvojena od nepoznate modelne
   nesigurnosti koeficijenta gubitka.

Vrijednosti se ne smiju citirati kao karakteristike stvarnog Venturija ili
difuzora. Za validaciju bi bili potrebni mjerena geometrija, uvjeti na ulazu,
kalibrirani tlakovi/protok i pripadni mjerni budžet nesigurnosti.
