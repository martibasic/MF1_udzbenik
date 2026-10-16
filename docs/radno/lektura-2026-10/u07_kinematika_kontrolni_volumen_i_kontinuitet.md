# Lektura: source/u07_kinematika_kontrolni_volumen_i_kontinuitet.md (pog. 7)

## 1. Izmjene

Pregledana cijela datoteka (939 redaka): uvod, teorija, izvodi (RTT, bilanca mase,
diferencijalni oblik), CFD blokovi, 6 riješenih primjera, samoprovjera, Z1–Z6
(tekst, naputci, kontrolni rezultati), opisi slika, napomene uz skice i završni okvir.
Promijenjena su 83 retka (oko 90 pojedinačnih zahvata).

Vrste izmjena:
- upućivanja s krivim padežom (5): `Prema @eq-…` → `Prema jednadžbi [-@eq-…]`;
  `u @ex-…` → `u primjeru [-@ex-…]` (2×); `a postupak rješavanja @sec-…` →
  `a postupak rješavanja opisan je u odjeljku [-@sec-…]`;
- položaj enklitika (oko 10): „masa se akumulira” → „se masa akumulira”, „U Z1 gustoća
  zraka se mijenja” → „U Z1 se gustoća zraka mijenja”, „dobiva se” iza „pa”…;
- glagolski oblici: „čestica ubrzava” → „čestica se ubrzava” (3×), „dobili smo” → „dobivamo”;
- kalkovi i anglizmi: „kroz vrijeme” → „s vremenom”, „fiksna točka” → „nepomična točka”,
  „predstavlja” → „je/znači” (4×), „komplementarna” → „koji se nadopunjuju”, „reducira” →
  „svodi”, „ekvivalentne” → „jednakovrijedne”, „relevantne” → „bitne”, „gibajući” →
  „pomični” (2×), „zatvori akumulaciju” → „postavi bilancu / izrazi”, „Most između…” →
  „Vezu između… uspostavlja”, „Venturi” → „Venturijeva cijev”;
- nazivlje prema `docs/urednicki_stil.md`: „hidraulični” → „hidraulički” (2×, uključujući
  naslov primjera; ID nepromijenjen), „Fizičko pitanje” → „Fizikalno pitanje”, „fizički tok”
  → „fizikalni tok”, „bilanca gibanja” → „bilanca količine gibanja”, „mjerilo (protoka)” →
  „mjerač protoka” (3×), „smjesa” → „mješavina” (dosljednost), „trenutačna strujnica” →
  „trenutna strujnica” (dosljednost unutar odjeljka), „prebačajna crpka” → „crpka za pretakanje”;
- red riječi / pogrešno pridruženi atributi: „Zrak ulazi u grijač … strojarnice gustoće ρ1”
  → „Zrak gustoće ρ1 ulazi u grijač …”; „Odredi gustoću … u izlaznom vodu ρmj” → „Odredi
  gustoću ρmj …”;
- fragmenti i interpunkcija: „Cijev s jednim ulaznim presjekom 1…, nepomičan KV, η = 1.” →
  „Promotrimo cijev … uz nepomičan KV i η = 1.”; „w ≪ vs: usis…” → „Budući da je w ≪ vs, usis…”;
  suvišan zarez ispred „jer” i „i”; točke u nabrajanju završnog okvira → točka-zarez
  (kao u pog. 6 i 8); suvišan razmak ispred `&nbsp;` u dvama naslovima primjera;
- naslov okvira izvoda: „Diferencijalni oblik kontinuiteta — iz integralnog preko teorema o
  divergenciji” → „Diferencijalni oblik kontinuiteta iz teorema o divergenciji”;
- opis slike: „Miješajući izjednačni spremnik” → „Izjednačni spremnik s miješanjem”.

Reprezentativni primjeri (prije → poslije):
1. „Prema @eq-kinematika-kv-…-01 bez akumulacije vrijedi” → „Prema jednadžbi [-@eq-kinematika-kv-…-01] bez akumulacije vrijedi”
2. „U stacionarnom strujanju polje brzine se ne mijenja kroz vrijeme, … — strujnica i trajektorija se podudaraju.” → „… polje brzine ne mijenja se s vremenom, … — strujnica i trajektorija podudaraju se.”
3. „Sustav ili kontrolna masa znači da se prati ista količina tvari … Formalni most između ta dva pogleda daje …” → „U sustavu, odnosno kontrolnoj masi, pratimo uvijek istu količinu tvari … Formalnu vezu između tih dvaju pogleda daje …”
4. „Maseni protok ṁ mjeri koliko mase prolazi u sekundi i uvijek je primarni zapis kontinuiteta” → „… mjeri koliko mase prođe u sekundi i na njemu se uvijek temelji osnovni zapis kontinuiteta”
5. „To provjerava račun prije dodavanja stlačivosti ili gibanja opterećenoga klipa.” → „Time se račun provjerava prije nego što se dodaju stlačivost ili gibanje opterećenoga klipa.”
6. „Nominalno prolazi, zajamčeno ne: skratiti operaciju, … ili suziti nesigurnost mjerila.” → „Nominalni plan prolazi, ali ne uz zajamčene granice: treba skratiti operaciju, … ili smanjiti nesigurnost mjerača.”
7. „Zbrajanjem lokalnih bilanci unutarnji se tokovi ponište: ostaju granice domene i ukupna akumulacija. Za stacionarni Venturi … moraju se slagati.” → „… unutarnji se tokovi poništavaju, pa ostaju samo tokovi kroz granice domene i ukupna akumulacija. Pri stacionarnom strujanju kroz Venturijevu cijev … moraju biti jednaki.”

## 2. Sadržajni nalazi koje NISAM ispravio

Sve brojke u primjerima i kontrolnim rezultatima Z1–Z6 ručno sam preračunao i odgovaraju
(P1, P2 usis, P3 spremnik, T-komad, rashladni krug, Z1–Z6, uključujući konzervativnu granicu u Z6).

1. **Nedosljedan zapis derivacije** (matematika, ne dirano): r. 580 `\mathrm{d}h/\mathrm{d}t`,
   r. 709 i 719 `\mathrm{d}m/\mathrm{d}t` (samoprovjera, bez indeksa KV), a drugdje u poglavlju
   `dh/dt` i `dm_{KV}/dt`. Preporuka: ujednačiti na `dm_{KV}/dt`, `dh/dt`.
2. **r. 680/683**: u tekstu `$A_n'$`, u formuli `$A_{n}'$` — sitna razlika zapisa iste veličine.
3. **r. 690** (izvorno): „Porast od 6,6 % jednak je omjeru $16/15$” — strogo, porast je
   $16/15-1$. Jezično ublaženo u „odgovara omjeru”; autorica može napisati „$16/15-1$”.
4. **r. 425**: slika zahvatnog usisa broda učitava se iz `u08_val3_izjednacni_spremnik.svg`;
   sadržaj SVG-a ispravan je (usis, KV uz brod), ali ime datoteke ostatak je stare skice
   izjednačnog spremnika — moguća zabuna pri održavanju.
5. **r. 465**: „Voda u ravnini otvora giba se prema pramcu gotovo brzinom broda: brod je gura
   ispred sebe.” Slikovito i dvojbeno: apsolutna brzina 8,01 m/s posljedica je toga da usis
   „hvata” vodu, a ne guranja vode ispred trupa. Preporuka: „usis je zahvaća i ubrzava do gotovo brzine broda”.
6. **r. 473**: „$w \ll v_s$” uz $w/v_s \approx 0{,}13$ — „≪” je izdašno; moguće „$w < v_s$”
   ili „$w$ je mnogo manji od $v_s$”.
7. **Ponavljanja** (nisam brisao jer bi nestao sadržaj): rečenica o Eulerovu opisu u inženjerskim
   proračunima gotovo je doslovno u r. 1 i r. 30; „Srednja brzina ne govori ništa o obliku profila,
   vrtloženju ni tlaku…” u r. 7 i r. 178; definicija $A_1v_1=A_2v_2$ kao posebnog slučaja u r. 5,
   r. 178, r. 181 i r. 279.
8. **Redoslijed razina Z1–Z6** je [T2, T1, T1, T2, T3, T4] (audit ga prihvaća); drugdje u knjizi
   je T1, T1, T2, T2, T3, T4 — samo napomena, nije jezični zahvat.

## 3. Provjere

- `lektura_check.py source/u07_…md`: **ok** (bez redaka STROGO, bez `provjeri numbers`;
  upućivanja istih ciljeva).
- `tools/check_u07_sketch_geometry.py`: svi PASS (izlaz 0; bez `PYTHONIOENCODING=utf-8`
  pada samo ispis znaka θ u konzoli cp1252, a ne provjera).
- `tools/audit_publication.py`: **Publication audit PASS**.
