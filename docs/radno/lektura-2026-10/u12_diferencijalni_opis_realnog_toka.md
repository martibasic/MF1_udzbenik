# Lektura: source/u12_diferencijalni_opis_realnog_toka.md (pog. 12)

Prošao sam cijelu datoteku, svih 725 redaka: uvod, teoriju, izvode, blokove (Granica modela,
Fizikalno značenje, CFD, Numerički pokus), šest riješenih primjera, zadatke Z1–Z6 s naputcima
i kontrolnim rezultatima, opise slika, samoprovjeru i završni okvir. Polazni tekst bio je već
prilično uredan, pa su izmjene ciljane. Promijenjeno je 81 redak; ukupno ima oko 85 pojedinačnih zahvata.

## 1. Vrste izmjena

- **Upućivanja s krivim padežom (11):** `@eq`/`@ex` iza prijedloga ili u kosom padežu
  pretvoreni su u imenicu u ispravnom padežu + `[-@id]` (npr. „daje jednadžbu [-@…]”,
  „prema jednadžbi [-@…]”, „iz primjera [-@…]”, „u primjeru [-@…]”). Upućivanja u nominativu
  (subjekt, zagrada) ostavljena su kakva jesu.
- **Red riječi i enklitike (≈6):** „okomito mjerilo je uvećano” → „okomito je mjerilo uvećano”,
  „Lokalni član je nula” → „Lokalni je član jednak nuli”, „trenutna brzina rastavlja se” →
  „trenutna se brzina rastavlja”, „Obje ploče su” → „Obje su ploče”.
- **Sročnost i padeži (≈5):** „Ako nas zanima srednja podjela … i pad tlaka” → „zanimaju”,
  „zahtijeva se GCI … i debalans” → „zahtijevaju se”, „Ona nisu” (bez antecedenta u množini) →
  „Reynoldsova naprezanja nisu”, „U dvije i tri dimenzije” → „U dvodimenzijskom i trodimenzijskom računu”.
- **Kalkovi i nespretni izrazi (≈20):** „predstavlja” → „označuje”, „vezuju … uz” →
  „povezuju … s”, „budžet nesigurnosti” → „proračun nesigurnosti”, „Invertiraj” → „Riješi
  izraz … po viskoznosti”, „nezadovoljenje diskretnih jednadžbi” → „koliko diskretne jednadžbe
  nisu zadovoljene”, „s analitikom” → „s analitičkim rješenjem”, „poništava se” → „krati se”,
  „održanje” → „održavanje”, „zidno smicanje” → „smicanje na stijenci”.
- **Nazivlje (2):** „hidrostatski” → „hidrostatički”, „smično naprezanje stijenke” →
  „smično naprezanje na stijenci”.
- **Razbijene ili povezane rečenice (≈6):** uvodna rečenica od 40 riječi podijeljena je na dvije, a rečenica o CFD
  odstupanju (pokus sa stepenicom) također; nesigurnosti u Z6b izdvojene su u zasebnu rečenicu;
  „Njihovo nametanje uklonilo bi pitanje podjele” spojeno je s prethodnom rečenicom.
- **Zarezi (≈5):** uklonjen je zarez ispred „jer” kad zavisna rečenica slijedi glavnu, dodan je zarez ispred
  „dok” i ispred „a” u nizovima („a zatim”, „a gruba”).
- **Ponavljanja:** „pretpostavi …; pretpostavi …” (Z3), „uz … uz” (SST), „rješavač rješava”.

### Reprezentativni primjeri (prije → poslije)

1. „Uvrštavanje … u Cauchyjevu jednadžbu daje @eq-navier-stokes-nestlacivi.” →
   „… daje jednadžbu [-@eq-navier-stokes-nestlacivi].”
2. „Kako iz opće bilance @eq-…-sec-01, koja vrijedi za svaki kontinuum, …” →
   „Kako iz opće bilance, jednadžbe [-@eq-…-sec-01], koja vrijedi za svaki kontinuum, …”
3. „Ručni @ex-laminarni-mikrokanal pretpostavlja potpuno razvijen tok: usporedba …” →
   „Ručni račun u primjeru [-@ex-laminarni-mikrokanal] pretpostavlja potpuno razvijen tok, pa usporedba …”
4. „Oba vezuju Reynoldsova naprezanja uz gradijent srednje brzine … Oznaka SSTm u
   @ex-stepenica-mjerenje-cfd inačica je … kako ga vodi NASA-in …” → „Oba modela povezuju
   Reynoldsova naprezanja s gradijentom srednje brzine … Kratica SSTm u primjeru [-@…] označuje
   inačicu … u obliku koji navodi NASA-in …”
5. „Osrednjavanje Navier–Stokesove jednadžbe linearne članove ostavlja u istom obliku sa
   srednjim poljem” → „Osrednjavanjem Navier–Stokesove jednadžbe linearni članovi zadržavaju
   isti oblik, sada sa srednjim poljem”
6. „Model ne procjenjuje nosivost ležaja bez određivanja prostorne raspodjele tlaka.” →
   „Bez određivanja prostorne raspodjele tlaka ovaj model ne daje procjenu nosivosti ležaja.”
7. „Sam promjer doprinosi relativnoj standardnoj nesigurnosti od 4 %, pa ima najveći doprinos …”
   → „Doprinos samog promjera relativnoj standardnoj nesigurnosti iznosi 4 %, pa je on najveći doprinos …”
8. „Finija RANS mreža sama ne prelazi u takav opis.” → „Samo profinjenje RANS mreže ne pretvara
   račun u takav opis.”

## 2. Sadržajni nalazi (NISAM ispravljao)

1. **Brojčana pogreška u primjeru „Granični sloj na trupu modela broda”, r. 328:**
   `\delta\approx\frac{0{,}37\cdot6{,}0}{(1{,}08\cdot10^{7})^{1/5}}=\frac{2{,}22}{25{,}2}\approx0{,}088\ \text{m}`.
   Točno je $(1{,}08\cdot10^7)^{1/5}=25{,}5$, pa je $\delta\approx0{,}087$ m. Zaključak
   $\delta/L_m\approx0{,}015$ (r. 343) i dalje vrijedi (0,0145). Treba uskladiti i verifikator
   i ključ rezultata ako sadrže 25,2 / 0,088.
2. **Notacija indeksa stijenke, r. 270:** `\right|_w` u $\tau_{st}=\mu\,\partial v_x/\partial y|_w$;
   standard traži hrvatske indekse (st), ne $w$. Slično `\mu\,dv/dr|_R` u samoprovjeri je u redu.
3. **Nedosljednost $D$ i $D_h$ u primjeru „Od podatka anemometra…”:** u Traži se (r. 408) stoji
   $\ell\approx0{,}07D$, a u provjeri (r. 429) $\ell\approx0{,}07D_h$. Za kružni vod to je isto,
   ali oznaku treba ujednačiti.
4. **Z1, r. 524:** koeficijent $a=2\ \text{m/s}^2$ u $v=at+bx^2$. Po tablici notacije $a$ je
   brzina zvuka. U ovom kontekstu zabune nema, ali odstupa od pravila jedne oznake.
5. **Z6a, r. 669:** omjer koraka mreža $\lambda_h$; $\lambda$ je u knjizi Darcyjev koeficijent,
   a $\lambda_L$ mjerilo duljina. Oznaka $\lambda_h$ nije u tablici nazivlja, pa je vrijedi
   unijeti u iznimke (dodatak A) ili je zamijeniti oznakom $r$.
6. **Blaga logička napetost, r. 288 → primjer trupa modela:** u bloku Fizikalno značenje stoji
   „Turbulentni sloj … se odvaja kasnije; zato se na modelu broda sloj namjerno prevodi u
   turbulentni”. U samom primjeru (r. 342) stimulator se opravdava ispravnim $C_{F,m}$ za
   Froudeovu korekciju, a ne odgodom odvajanja. Preporučujem preformulirati „zato” (autorska odluka).
7. **Primjer mikrokanala, r. 262:** $Re\approx12{,}7$ zahtijeva gustoću (≈1000 kg/m³), koja u
   tekstu zadatka nije navedena (u Z3 jest, 998 kg/m³). Manji nedostatak podataka.
8. **Tablica pokusa sa stepenicom, r. 439/444:** tekst kaže da su CFD vrijednosti zaokružene, a
   tablica daje 6,541667 i −0,0012520 sa šest ili sedam znamenaka. To je moguća nedosljednost s
   opisom.

Ostali ručno provjereni rezultati slažu se: P1 (10,5 m/s²), uljni film (1,125 m/s),
mikrokanal (652 Pa; $Re$ 12,7), trup ($Re_{x_1}$, $\delta_B$ 2,04 mm, $C_{F,m}$, $C_{F,s}$,
omjer 125), anemometar ($k$, $\omega$, $\varepsilon$), stepenica (6,279; 6,543; 4,5 %), Z3, Z4,
Z5 i Z6 (n=2,000, GCI 1,237/0,312 %, $2s_E$, omjeri 1,14 i 0,844).

## 3. Provjere

- `lektura_check.py source/u12_diferencijalni_opis_realnog_toka.md`: **ok** (nema redaka STROGO,
  numbers ni refs).
- `tools/check_u12_sketch_geometry.py` (uz PYTHONIOENCODING=utf-8): **U12 SVG PASS**.
- `tools/audit_publication.py`: **Publication audit PASS** (U12: 6 primjera, 6 zadataka
  [T1,T1,T2,T2,T3,T4]).
