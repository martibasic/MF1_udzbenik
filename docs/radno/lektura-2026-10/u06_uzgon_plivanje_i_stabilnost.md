# Lektura: source/u06_uzgon_plivanje_i_stabilnost.md (pog. 6)

## 1. Izmjene

Pregledana je cijela datoteka (1096 redaka): uvod, teorija, izvodi, okviri (Fizikalno značenje, CFD, Granica modela, Učinak slobodne površine), šest riješenih primjera, samoprovjera, Z1–Z6 s naputcima i kontrolnim rezultatima, napomene uz skice i završni okvir. Promijenjeno je 75 redaka, s ukupno oko 80 pojedinačnih zahvata.

Vrste izmjena:
- upućivanja s krivim padežom: 4 (`iz @ex` / `u @ex` / `Prema @eq` prebačeno u `[-@id]` s imenicom u pravom padežu);
- red riječi i položaj enklitika: oko 15 („vodna linija je kružna” → „vodna je linija kružna”, „U Z3 pomični uteg već je uključen” → „U Z3 je pomični uteg već uključen”);
- kalkovi i nespretni izrazi: oko 15 („predstavlja energiju”, „robustan zapis”, „tretiraj kao”, „centroid”, „ekscentar”, „težinjen/težinjenje”, „zatvori/zatvaraju ravnotežu”, „fiksnim”, „horizontalnom”);
- nazivlje prema uredničkom stilu: „hidrostatske” → „hidrostatičke”, „stabilnošću/stabilnosti” → „stabilitetom/stabiliteta”, „prizmatskih” → „prizmatičnih” (usklađeno s „prizmatičnog” u izvodu), „granica fluida” → „razdjelnica” (usklađeno s okvirom o dvama fluidima);
- sročnost, padeži i glagolski oblici: „propusnosti prostora” → „propusnost prostora” (akuzativ u nizu), „uranjaju se” → „uranjaju”, „nastaje nagibni moment” umjesto „stvara” bez subjekta;
- zarezi: dodani pri zatvaranju umetka i ispred „pa”, uklonjeni ispred „te” i „jer”;
- logički nejasne rečenice: „Budući da je uljni sloj i dalje potpuno presijecao platformu” → „Budući da je platforma i tada potpuno presijecala uljni sloj”; u Z2 rečenica „To je geometrijska granica…” upućivala je na pojam koji se uvodi tek u „Traži se” i preoblikovana je tako da imenuje dodatnu masu do ruba boka;
- terminološki precizniji opis: trapez „s okomicama/okomitim krakovima” → „s okomitim stranicama” (okomite stranice duljina $T_L$, $T_D$ zapravo su osnovice, a ne krakovi).

Primjeri (prije → poslije):
1. „Model se primjenjuje u @ex-u07-plutajuca-…” → „Model se primjenjuje u primjeru [-@ex-u07-plutajuca-…]”
2. „Za platformu iz @ex-…-t2 (…)” → „Za platformu iz primjera [-@ex-…-t2] (…)”
3. „Pripadni $KB_{eq}$ jest težište istisnute mase, težinjeno gustoćama slojeva, i $GM_{eq}=…$” → „Pripadni $KB_{eq}$ visina je težišta istisnute mase, pri čemu se volumeni slojeva ponderiraju njihovim gustoćama, a $GM_{eq}=…$”
4. „Pozitivan $GM$ sam ne određuje nijedno od toga.” → „Sam pozitivan $GM$ ne određuje ni jedno ni drugo.”
5. „Oštećeni stabilitet može zahtijevati metodu izgubljenoga uzgona, propusnosti prostora, … ništa od toga nije sadržano ovdje.” → „Stabilitet oštećenoga broda može zahtijevati metodu izgubljenoga uzgona, propusnost prostora, … ništa od toga ovdje nije obuhvaćeno.”
6. „vodu tretiraj kao ukrcanu masu s težištem u centroidu tanka” → „vodu smatraj ukrcanom masom s težištem u središtu volumena tanka”
7. „Rubni gazovi imaju zadane granice pogreške ±3 mm, vrijedi $\rho_v=…$” → „Za rubne gazove zadane su granice pogreške ±3 mm, a za ostale veličine vrijedi $\rho_v=…$”
8. „Kućište tone bez dodatne sile prema dolje. Za njegovo statičko pridržavanje ili ravnomjerno podizanje … potrebna je sila” → „Kućište tone i bez dodatne sile prema dolje. Da bi ga se statički pridržalo ili ravnomjerno podizalo dok je potpuno uronjeno, potrebna je sila”

Jedina promjena brojčanog zapisa izvan formule: „(~1025 kg/m³)” i „(~998 kg/m³)” → „(približno 1025 kg/m³)” i „(približno 998 kg/m³)”. Brojevi su ostali isti, pa provjera nije prijavila razliku.

## 2. Sadržajni nalazi (nisu ispravljani)

1. **Rezultat T₁ i ΔT u T4 primjeru tanka (r. 703–710, 790).** „$T_1 = \frac{4277 \cdot 10^3}{1025 \cdot 80 \cdot 15} \approx 3{,}478\ \text{m}$”: račun daje 3,477 m (4,277·10⁶/1,23·10⁶ = 3,4772). „$\Delta T = T_1 - T_0 \approx 0{,}226\ \text{m}$” (i u provjeri „$\Delta T=m_v/(\rho_{mv}Lb)\approx0{,}226$”): $m_v/(\rho Lb)$ = 276 750/1 230 000 = 0,2250 m, a i s $m_v$ = 277 t dobiva se 0,2252 m. Treba provjeriti i D06 ili verifikator.
2. **Notacija V umjesto $V_{ist}$ (r. 27 i Z1).** „$$F_U = \rho g V$$”, a odmah zatim izvod zaključuje s $F_U=\rho gV_{ist}$. U Z1 se koristi $V$ za volumen tijela, što je ondje opravdano (tijelo je potpuno uronjeno), ali jednadžba 6.1 odstupa od standarda $V_{ist}$.
3. **Oznaka $B'$ u uspravnom položaju (r. 726).** „Metacentarski radijus (razmak centra uzgona $B'$ od metacentra $M$)” u koraku 4 tankovskog primjera. Prema izvodu, $BM$ se mjeri od $B$ uspravnog položaja, pa bi trebalo pisati $B$.
4. **Točke B i G bez matematičkog zapisa (r. 428, 513, 668).** „**Veza s proračunom.** B označuje centar uzgona…”, „B označuje centar uzgona ponderiran…”, „…zajedničko težište G; B ostaje centar vanjske istisnine”. Te su oznake napisane običnim slovima umjesto `$B$`, `$G$`. Nisu promijenjene jer bi se time promijenio skup formula.
5. **Visina gondole spara (r. 842).** „Gondola i rotor nalaze se oko $100\ \text{m}$ iznad kobilice”. Uz $H=100$ m i gaz 77,6 m vrh plovne osnove već je 100 m iznad kobilice, a gondola na stupu tipično je još 80–100 m iznad mora. Tvrdnju treba provjeriti (vjerojatno „iznad mora” ili veća visina iznad kobilice).
6. **„IMO-ovi kriteriji” i „dvije površine” (r. 333).** Navedena su tri kriterija površine (0,055; 0,09; 0,03 m rad), a završna ograda govorila je o „dvije površine”. Jezično je ublaženo u „sami kriteriji površina”; autorica neka potvrdi namjeru.
7. **Gustoća „ulja” u Z4 (r. 997).** $\rho_u\approx992{,}4$ kg/m³ neuobičajeno je visoka za ulje (tipično 800–950 kg/m³). Računski je točna, ali didaktički čudna, jer se ulje i voda gotovo ne razlikuju.
8. **Zaokruživanje gaza pri ±5 % mase u spar primjeru (r. 827).** „$T_{-5\%} \approx 73{,}8\ \text{m}$”: 0,95·77,6 = 73,72 ≈ 73,7 m (s 77,63 dobiva se 73,75). To je granično zaokruživanje.
9. **Okvir CFD (r. 144).** „Ručni @ex-… provjerava gaz” ispisuje „Ručni primjer 6.x”, što je gramatički ispravno, pa je ostavljeno.

Provjereni i ispravni: P1 (452,5 / 833,9 / 381,4 N; 1889 kg/m³), P2 (0,601 m³; 0,209 m; 320 kg), P3 (KG 0,1927; GM 0,2450; e 0,134; točni e 0,1352; ΔT 6,14 cm), P4 dva fluida (KB_eq 0,1185; BM_eq 0,5217; GM_eq 0,4289; e 0,164; točni 0,165), P5 (osim nalaza 1: KG′ 2,90; BM 5,39; GM 4,23; φ 3,94°; φ_lim 31,1°), P6 (A, V, T, BM 0,116), Granica modela (0,0021 m; 0,9 %; < 0,5 % pri 5°), slobodna površina (−0,065 m), Z1–Z6 kontrolni rezultati (Z6: Δ 689,9 kg; KB 0,105; BM 0,583; GM 0,488; e 0,321 m).

## 3. Provjere

- `lektura_check.py source/u06_uzgon_plivanje_i_stabilnost.md`: **ok** (nema redaka STROGO; matematika, ID-jevi, atributi, ograde, polja i razine identični su polaznom stanju; nema razlika u brojevima ni upućivanjima). Jedan međukorak (uklonjeni `$\delta$` i dodani `$K$`) vraćen je.
- `tools/check_u06_sketch_geometry.py`: **PASS** (svih 11 provjera, izlaz 0).
- `tools/audit_publication.py`: **Publication audit PASS** (U06: 6 primjera, 6 zadataka [T1,T1,T2,T2,T3,T4]).
