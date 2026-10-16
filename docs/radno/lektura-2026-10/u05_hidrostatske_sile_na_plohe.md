# Lektura — source/u05_hidrostatske_sile_na_plohe.md (pog. 5)

Pročitano je i lektorirano svih 899 redaka: uvod, teorija, izvodi, blokovi CFD-a i granice modela, 6 riješenih primjera, Z1–Z6 s naputcima i kontrolnim rezultatima, opisi slika, samoprovjera i sažetak. U `git diff` je promijenjeno 67 redaka (oko 60 zasebnih zahvata). Matematika, brojevi, ID-jevi, atributi, polja i razine ostali su netaknuti.

## 1. Izmjene po vrstama

- **Upućivanja s krivim padežom (5):** `prelazi u @eq-…` (2×), `daje @ex-…`, `Ručni @ex-…`. Sva su prebačena u oblik imenica + `[-@id]`.
- **Red riječi i enklitike (~12):** „atmosferski tlak se poništava” → „atmosferski se tlak poništava”, „s druge strane je zrak” → „s druge je strane zrak”, „Gornji rub je” → „Gornji je rub”, „su zatvorene” → „zatvorene su”, „Z1 i Z4 su pogledi” → „Z1 i Z4 pogledi su” i slično.
- **Kalkovi i nespretni izrazi (~20):** „centroidna os” → „težišna os” (3×), „predstavlja” → „opisuje/znači”, „vraća” → „daje/potvrđuje”, „puta” → „umnožak … i …”, „momentirati” → „moment računati iz”, „Faktorizacija razlike kvadrata” → „Rastavljanjem razlike kvadrata”, „tipično” → „u pravilu”, „krajnji učinci” → „rubni učinci”, „validiran” → „potvrđen”, „vlačiti” → „vući”, „Slika ispod” → „Slika u nastavku”, „jest/jesu” → „su/iznosi”.
- **Pasiv i preoblikovane rečenice (~8):** „ne smije biti automatski primijenjena” → „ne smije se automatski primijeniti”, „Za hidrostatičku analizu određuju se: koliki su…” → „Hidrostatička analiza zato odgovara na dva pitanja:”, a nabrajanje u Traži se (Z1) složeno je u čist niz.
- **Zarezi i padeži (~8):** zarez ispred „nego” (2×), iza uvodne zavisne rečenice („Kada θ→0, …”), bez zareza ispred „jer” iza glavne rečenice, „s obje strane” → „s obiju strana” (2×).
- **Nazivlje:** „aksijalni moment površine” / „drugi moment površine” ujednačeno je na „drugi moment površine”, kako piše u D01 i u06. „Horizontale” → „vodoravnice” (2×), radi dosljednosti s ostatkom poglavlja.
- **Dvoznačnost:** „poklopac na stijenci spremnika s gornjim zglobom” → „poklopac s gornjim zglobom i donjim vijkom na stijenci spremnika”.

Reprezentativni primjeri:

1. „pa je CP ispod C i donji vijak prenosi…” → „pa je CP ispod C, a donji vijak prenosi…”
2. „Zbog toga formula za centar tlaka … ne smije biti automatski primijenjena na zatvoren spremnik” → „Zato se formula za centar tlaka … ne smije automatski primijeniti na zatvoren spremnik”
3. „izraz za $h_R$ prelazi u @eq-u05-centar-tlaka-vertikalna” → „prelazi u jednadžbu [-@eq-u05-centar-tlaka-vertikalna]”
4. „za slojevit fluid isti postupak daje @ex-u05-pregrada-ulje-voda. Odluka je potreban moment…” → „za slojeviti fluid isti je postupak proveden u primjeru [-@ex-u05-pregrada-ulje-voda]. Odluka se odnosi na potreban moment…”
5. „srednja vrijednost 34,27 kPa puta 6,0 m² vraća 205,6 kN” → „umnožak srednje vrijednosti 34,27 kPa i površine 6,0 m² ponovno daje 205,6 kN”
6. „Kod plohe s pregibom, prevjesom ili promjenom predznaka $n_{f,x}$ površinu treba podijeliti i komponente zbrojiti predznačeno” → „Ako ploha ima pregib ili prevjes ili ako $n_{f,x}$ mijenja predznak, površinu treba podijeliti, a komponente predznačeno zbrojiti”
7. „Vodoravna spojnica u $B$ može samo vlačiti ulijevo, do $T_{\max}$” → „može samo vući ulijevo, i to najviše silom $T_{\max}$”
8. „ali samo uz usporedbu ploha jednake površine…” → „ali to znači jednaku silu samo za plohe jednake površine…”

## 2. Sadržajni nalazi koje nisam ispravio

1. **R. 745 (Z2, kontrolni rezultat):** „Provjera: $F_x$ i $F_z$ ne poništavaju momente ni oko jedne točke, za razliku od kružnog luka.” Tvrdnja je fizikalno netočna. Momenti dviju komponenata poništavaju se oko svake točke na pravcu djelovanja rezultante. Vjerojatno se misli da lokalne tlačne sile parabole nemaju zajedničku točku, pa za njih ne postoji unaprijed poznata točka poput središta O. Zato moment treba računati iz obiju komponenata (tako ispravno kaže naputak u r. 736). Preporuka je preformulirati rečenicu.
2. **R. 83 (izvod, provjera):** „Za vodoravnu plohu ($h_a=h_b=h_C$) oba zapisa daju $F=\rho gh_CA$”. Integralni zapis s r. 77 odnosi se na vertikalni pojas. Za njega $h_a=h_b$ znači pojas visine nula, pa $A=0$. Provjera vrijedi samo za oblik $F=\rho gA(h_a+h_b)/2$ ako se $A$ shvati kao zadana površina. Granični slučaj je formalno nekonzistentan.
3. **Nazivlje „hidrostatske/hidrostatički”:** naslov `## Hidrostatske sile na plohe` (r. 13, bez ID-ja), oznaka sažetka (r. 892), alt QR koda (r. 170) i naslov poglavlja u `book.json` koriste „hidrostatske”. Nazivlje u `docs/urednicki_stil.md` traži „hidrostatički”, a ostatak teksta ga i koristi. Nisam mijenjao jer bi to odvojilo oznaku od naslova poglavlja i sidara. Preporuka je promijeniti sve zajedno, kao strukturni zahvat.
4. **Oznake:** u r. 106–115 dubina hvatišta opće raspodjele označena je s $h_R$, a drugdje je $h_{CP}$. U r. 276/343 i u Z3/Z5 sila spojnice je $T$, iako je u tablici notacije $T$ gaz, temperatura ili širina slobodne površine. To nije pogreška, ali odstupa od načela „jedna veličina, jedna oznaka”.
5. **Bilježnica (r. 441–443):** numerički pokus za zakrivljenu plohu u pog. 5 poziva `u06_zakrivljena_ploha.ipynb`. Slike primjera također nose prefiks `u06_` (`u06_val1_…`, `u06_ch1_…`). To je vjerojatno ostatak stare numeracije. Treba provjeriti da bilježnica opisuje upravo ove podatke.
6. **Manja napomena, r. 120:** „plitak poklopac uz slobodnu površinu nosi najveći dio sile u donjoj trećini”. Za trokutni dijagram donja trećina nosi 5/9 ≈ 56 % sile. „Najveći dio” je točno, ali slabo; samo informativno.

Ručno sam preračunao sve primjere i kontrolne rezultate Z1–Z6 (sile, krakove, momente, $T$, $R_A$, $R_O$, $z$). Svi brojevi se slažu s tekstom, uz uobičajeno zaokruživanje: $R_A=15{,}5737\to15{,}574$ kN.

## 3. Provjere

- `lektura_check.py source/u05_hidrostatske_sile_na_plohe.md` → **ok** (nema redaka STROGO; brojevi i refs bez prijave).
- `tools/check_u05_sketch_geometry.py` → **PASS** (sve 4 provjere).
- `tools/audit_publication.py` → **Publication audit PASS**.
- Kontrolni znakovi u datoteci: 0 (formule nisu oštećene).
