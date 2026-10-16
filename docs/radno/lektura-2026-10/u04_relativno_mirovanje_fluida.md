# Lektura: source/u04_relativno_mirovanje_fluida.md (pog. 4)

Pročitana je cijela datoteka (855 redaka): uvod, teorija, izvodi, blokovi Fizikalno značenje, CFD i Granica modela, interaktivni blok, šest riješenih primjera, samoprovjera, Z1–Z6 s naputcima i kontrolnim rezultatima, napomene uz skice i sažetak. Promijenjen je 71 redak (diff prema `lektura_base`).

## 1. Izmjene

Približno 75 pojedinačnih zahvata:

- red riječi i položaj enklitika (≈10): „Slobodna je površina … okomita” → „Slobodna površina … okomita je”, „Kutna brzina se krati” → „Kutna se brzina krati”, „stalni su”;
- kalkovi i nespretni izrazi (≈20): „jest nula” → „jednaka je nuli”, „ima iznos” → „iznosi”, „sama razlika sondi … mjeri ubrzanje zavoja”, „osjeća gravitaciju”, „poviješću kočenja”, „k tome”, „značajnom”, „mirovnim stanjem”, „uzduž” → „duž”, „zavrtavanje” → „pokretanje vrtnje”;
- glagolske i sročne pogreške (≈8): „Sustav ubrzava” → „Sustav se ubrzava”, „spremnik ne prelijeva” → „spremnik se ne prelijeva”, „Mjere manometarske tlakove” bez subjekta → „Senzori mjere …”;
- nelogične tvrdnje (≈4): „nagib određuje smjer ubrzanja” → „nagib ovisi o smjeru ubrzanja”, „Gradijent određuje ubrzanje” → „Gradijent ovisi o ubrzanju”, „osjetljivost … je stvarna odluka” → „stvaran kriterij”;
- zarezi (≈5): ispred „pa” u odgovorima samoprovjere, nepotreban zarez iza priložne oznake;
- preoblikovane rečenice (≈12): uvod (brod u zavoju), Translatorno ubrzanje, separator („Hod od izlaza … daju”), Z6;
- upućivanje s krivim padežom (1): `površina je paraboloid @eq-…-08` → `paraboloid opisan jednadžbom [-@eq-…-08]`;
- dosljednost naziva: „prijelazno zapljuskivanje” → „prolazno” (kao u ostatku poglavlja), „fizičko stanje” → „fizikalno stanje”;
- oblikovanje: suvišni razmak prije `&nbsp;` u naslovu primjera o autocisterni i dvostruki prazni redak iza njega;
- naslov izvoda (box-label): „Coriolisova sila u relativnom mirovanju — zašto nestaje” → „Zašto Coriolisova sila nestaje u relativnom mirovanju”. Nije riječ o naslovu zadatka, pa izmjena ne utječe na D06.

Reprezentativni primjeri (prije → poslije):

1. „Ako se spremnik giba … i ako se nakon prolaznih oscilacija fluid smiri u odnosu na stijenke, onda se problem može promatrati …” → „Ako se spremnik giba …, a fluid se nakon prolaznih oscilacija smiri u odnosu na stijenke, problem se može promatrati …”
2. „centripetalno ubrzanje $a=v_s^2/R_z$ vrijedi lokalno kada je …, a površina se podiže na vanjskoj strani zavoja.” → „uz centripetalno ubrzanje $a=v_s^2/R_z$, što lokalno vrijedi kada je … Površina se tada podiže na vanjskoj strani zavoja.”
3. „Hod od izlaza goriva kroz gorivo i hod od izlaza vode kroz vodu, oba od istog tlaka na izlazima, daju” → „Integriramo tlak od izlaza goriva kroz gorivo i od izlaza vode kroz vodu; budući da na oba izlaza vlada isti tlak, slijedi”
4. „Razina je viša na stražnjoj strani jer nagib određuje smjer ubrzanja, a ne brzine.” → „… jer nagib ovisi o smjeru ubrzanja, a ne o smjeru brzine.”
5. „Veći radijus nosi veće centrifugalno ubrzanje pa zato treba veći gradijent tlaka.” → „Na većem polumjeru centrifugalno je ubrzanje veće, pa je za ravnotežu potreban i veći gradijent tlaka.”
6. „Viši prvi val od ravnotežne razine sam ne znači pogrešan CFD račun” → „Prvi val viši od ravnotežne razine sam po sebi ne znači da je CFD račun pogrešan”
7. „Cilindar se još giba prema gore, ali usporava uz ubrzanje iznosa … prema dolje.” → „Cilindar se i dalje giba prema gore, ali usporava: ubrzanje iznosa … usmjereno je prema dolje.”
8. „U stanju relativnog mirovanja … pa Coriolisov član automatski iščezava” → „… pa Coriolisov član iščezava:”

## 2. Sadržajni nalazi (NISU ispravljeni)

Svi brojčani rezultati u primjerima i kontrolnim rezultatima ručno su preračunati i slažu se: P1–P6 i Z1–Z6, uključujući $k_{max}\approx0{,}790$ i rezervu 2,68 mm u Z6.

1. **Dva zapisa efektivnog polja.** U uvodu (r. 3 i 9) piše se `$\vec g_{\mathrm{eff}}$`, a u ostatku poglavlja `$\vec g_{eff}$` / `$\vec{g}_{eff}$` (npr. r. 31, 48, 53, 850). Treba izabrati jedan zapis.
2. **Sukob s tablicom notacije: $h_v$, $h_u$.** U primjeru o balastnom tanku (r. 388–420 i fig-alt r. 376) $h_v$ i $h_u$ znače razinu uz vanjsku i uz unutarnju stijenku. Prema `docs/urednicki_stil.md` ti su indeksi rezervirani za slojeve vode i ulja. Prijedlog: $h_{van}$/$h_{unu}$ ili $h_1$/$h_2$. Pritom treba uskladiti i SVG.
3. **Sukob s tablicom notacije: $s_h$.** U Z5 (r. 786) $s_h = 4\ \text{mm}$ označava raspon očitanja (najveće minus najmanje). Prema standardu je $s(x)$ standardna nesigurnost, a Z6 izričito razlikuje zadanu granicu od standardne nesigurnosti. Oznaka može zavarati. Prijedlog: $R_h$ ili $\Delta_h$, uz usklađenje verifikatora i bilježnice ako ga koriste.
4. **Nagib broda u zavoju (r. 421).** Tekst kaže da se kutu površine u okviru tanka „pribraja kut nagiba broda”. Predznak ovisi o smjeru nagiba: u ustaljenom zavoju brod se obično nagne prema van, a u početnoj fazi može se nagnuti prema unutra. Dodaje li se ili oduzima, ovisi o slučaju, pa bi ogradu bilo dobro izreći. Smisao nisam mijenjao, samo jezik („dodaje” → „pribraja”).
5. **Prevelika preciznost međurezultata.** U primjeru o autocisterni (r. 533–540, unutar formula) navedeno je `0{,}682416` i `0{,}217584` m, šest decimala uz ulaze s dvije ili tri značajne znamenke. To je stilski nalaz, ne pogreška.
6. **Naslijeđena imena.** Skica tanka broda koristi datoteku `u04_fig_rotirajuci_cilindar.svg`, a u tekstu tog primjera (r. 367) stoji skriveno sidro `ex-u04-rotirajuci-cilindricni-spremnik-bez-prelijevanja-t2`. Primjer o separatoru ima sidro `ex-u04-laboratorijska-centrifuga-…`. Stari ID-jevi namjerno su sačuvani radi poveznica, ali ime SVG datoteke ne odgovara prizoru. Ostavljeno je.
7. **CFD blok (r. 58).** „nagib slobodne površine $-a/g$” vrijedi samo za os $x$ u smjeru ubrzanja. Tekst bloka to ne kaže, iako izvod ispod uvodi tu orijentaciju. Pogreške nema, ali predznak bez osi može zbuniti.

## 3. Provjere

- `lektura_check.py source/u04_relativno_mirovanje_fluida.md` → **ok**: nema redaka STROGO, `numbers` ni `refs`. Matematika, ID-jevi, atributi, ograde, polja i razine ostali su identični.
- `tools/check_u04_sketch_geometry.py` → 3× PASS (brod u zavoju, kosa stijenka, skice vježbi).
- `tools/audit_publication.py` → **Publication audit PASS** (U04: 6 primjera, 6 zadataka [T1,T1,T2,T2,T3,T4]).
- Nisu pokretani generatori ni render (prema uputama). Didaktička kvaliteta nije time dokazana: provjere potvrđuju samo strukturne invarijante.
