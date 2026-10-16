# Lektura — source/u02_viskoznost_povrsinska_napetost_i_kapilarnost.md (pog. 2)

Pregledana je cijela datoteka (880 redaka): uvod, teorija, izvodi, blokovi CFD/Fizikalno
značenje/Granica modela/Dublje, šest riješenih primjera, samoprovjera, Z1–Z6 s naputcima
i kontrolnim rezultatima, napomene uz skice i sažetak. Izmijenjen je 81 redak
(oko 70 pojedinačnih zahvata). Matematika, brojevi, ID-jevi, atributi, polja i razine
nisu dirani.

## 1. Vrste izmjena

- **Padeži i sročnost** (~8): „pri obje temperature” → „pri objema temperaturama” (3×);
  „zanemariv volumen meniskusa i promjena…” → „zanemariv volumen…, zanemariva promjena…”;
  usporedba „200 je puta veća od vode” → „od kinematičke viskoznosti vode”.
- **Upućivanja** (1): `prema @eq-reologija-razrada-koraka-02` → `prema jednadžbi [-@eq-…]`.
  „Ručni @ex-…” ostavljen (nominativ „Ručni primjer 2.x” je ispravan).
- **Mala početna slova nakon formula koje završavaju točkom** (4): „pa je gradijent brzine”,
  „smično naprezanje iznosi”, „kinematička viskoznost glasi” u P2 → rečenice s velikim slovom;
  „Pri tome je ovdje” iza formule sa zarezom → „pri čemu je”.
- **Kalkovi i nespretni izrazi** (~20): „predstavljen je” → „uveden je”; „formaliziraju se” →
  „iskazuju”; „Izoliranjem h” → „Izražavanjem h”; „hladni start” → „hladno pokretanje”;
  „signal je za uzbunu” → „znak je za uzbunu”; „dvije neovisne staze” → „dva neovisna puta
  računa”; „linearne su u μ” → „linearno ovise o μ”; „varirati” → „mijenjati se”;
  „nastupa u Re” → „pojavljuje se u Re”; „traži stalan omjer” → „zahtijeva”.
- **Red riječi i enklitike** (~6): „Dijeljenjem s πd faktor π i jedna potencija promjera krate se”
  → „Dijeljenjem s πd krate se faktor π i jedna potencija promjera”; „numerički pad tlaka
  najprije se uspoređuje” → „numerički se pad tlaka najprije uspoređuje”.
- **Zarezi** (~6): ispred „nego”, „pa”, „a ne”; umetnute odnosne rečenice.
- **Razbijene/prestrukturirane rečenice** (~6): odvojena oznaka u/v od tvrdnje o modelu (pog.
  „Viskoznost”); tautološka rečenica o kavitaciji; skok tlaka na zakrivljenoj površini.
- **Humanizacija** (~6): „Promatra se” → „Promatramo”; „Prate se” → „Pratimo”.
- **Nazivlje i dosljednost** (~5): „trokontaktna linija” → „trofazna kontaktna linija”;
  „igla” → „kapilara” u P3 (zadatak govori o kapilari; „igla” je ostala samo u Z6, gdje je
  tako uvedena); „red” → „redak” tablice u Z5; „kapilarni pad” → „spuštanje razine” (sažetak).
- Napomene uz skice: rečenica o Z5 premještena iza Z4 (redoslijed Z1–Z5).

### Reprezentativni primjeri

1. „Kad se susjedni slojevi gibaju jedan prema drugom” → „…jedan u odnosu na drugi”.
2. „Za usporedbu najprije izračunamo isti zadani protok” → „…najprije simuliramo isti zadani protok”.
3. „Pri kavitaciji, nastanku i rastu mjehura pare u tekućini, mjehuri mogu nastati i rasti kada…”
   → „Kavitacija je nastanak i rast mjehura pare u tekućini: mjehuri mogu nastati i rasti kada…”.
4. „Spojene cjevčicom, tekućina teče iz manje u veću kapljicu, pa se manja prazni, a ne
   izjednačuju se.” → „Ako se kapljice spoje cjevčicom, tekućina teče iz manje u veću, pa se
   manja prazni umjesto da se kapljice izjednače.”
5. „Zbroj 227+120=347 Pa zato bi dvaput iskoristio različite oblike iste međupovršine.” →
   „Zato zbroj 227+120=347 Pa nema smisla: u njemu bi se dvaput uračunali različiti oblici
   iste međupovršine.”
6. „Između dviju paralelnih ploča nalazi se glicerin debljine δ” → „…sloj glicerina debljine δ”.
7. „U mirnom kanalu pogonjenom tlakom profil je drukčiji.” → „U kanalu s nepomičnim
   stijenkama, u kojem strujanje pokreće razlika tlakova, profil je drukčiji.”
8. „Kvašenje i nekvašenje time prestaju biti svojstvo same tekućine — postaju svojstvo para…”
   → „Kvašenje i nekvašenje stoga nisu svojstvo same tekućine, nego svojstvo para…”.

## 2. Sadržajni nalazi (NISU ispravljeni)

1. **Redak ~321 (Young–Laplace, cilindar)**: „za cilindar ($R_2 \to \infty$) $\Delta p = \sigma/R$”
   — oznaka $R$ nije uvedena (glavni polumjeri su $R_1$, $R_2$, a polumjer sfere $r$; prema
   tablici notacije $R$ je polumjer spremnika/luka). Vjerojatno treba $\sigma/R_1$.
2. **Redak ~326 (Fizikalno značenje, kavitacija)**: „ne daje jednostavan kriterij „tlaka koji
   zatvara mikrokapljicu”” — u kontekstu kavitacije riječ je o jezgri/mjehuriću pare, ne o
   kapljici; smisao navoda nejasan (moguće „mikromjehurić”).
3. **Redak 7 i ~243 (Weber/Bond)**: ista rečenica ponovljena u uvodu i na kraju izvoda kapilarnog
   uspona. Izvorni smjer „omjeri površinske napetosti prema inerciji i gravitaciji” obrnut je
   prema uobičajenoj definiciji ($We=\rho v^2L/\sigma$, $Bo=\rho gL^2/\sigma$); u lekturi je
   preformulirano u „odnos inercije, odnosno gravitacije, prema površinskoj napetosti” — molim
   autoričinu potvrdu i odluku treba li ponavljanje ostati.
4. **P3 „Kapilarni mikrodozator s izlaznom kapljicom” (T3, r. ~428) i Z6 „Kapilarna igla pod
   tlakom” (T4, r. ~831)**: isti fizikalni problem i isti postupak ($h_{cap}$,
   $p_{M,1}=\max(0,\rho gH-4\sigma/d)$, $p_{M,2}=\rho gH+4\sigma/D$, provjera $\rho gD$);
   Z6 dodaje samo raspon $D$ i izbor regulatora. Prema AGENTS.md to je ponavljanje istih
   studentskih odluka — kandidat za didaktičku reviziju Z6.
5. **P „Utjecaj temperature na viskozni otpor ležaja” (r. ~511–595)**: tekst zadatka $T_2=90\,^\circ$C
   naziva „gornjom nastavnom granicom zagrijanog ulja”, rješenje ga zove „radna temperatura”,
   a provjera kaže da ulje u službi obično radi hladnije od te granice. Nazivlje stanja 2
   treba ujednačiti (ID primjera i jednadžbi i dalje nose „hladni-start”).
6. **Granica modela (r. ~340)**: „hidrostatički član $\rho gD$ kroz visinu kapljice” — u teoriji
   je promjer kapljice $d$ ($\Delta p=4\sigma/d$), a $D$ se koristi samo u P3/Z6. Manja
   nedosljednost oznaka.
7. **Napomene uz skice (r. ~872)** ne spominju Z6 (iglu s kapljicom), iako ju skica i fig-alt
   prikazuju.
8. Informativno: ID-jevi jednadžbi kapilarnog uspona nose ime
   `eq-reologija-konstitutivna-motivacija-newtonov-zakon-viskozno-05…07` (zaostatak starog
   imenovanja). Stabilni ID-jevi — ne mijenjati, samo napomena.

Svi brojevi u P1–P6 i kontrolni rezultati Z1–Z6 provjereni su ručnim preračunom i
konzistentni su (npr. P2 22,68 N i 20,4 W; etanol 10,8 mm; lab-on-chip 33,5 cm, 3,32 kPa,
−12,7 cm; Z4 62,9 mm, −18,8 mm, 189 Pa; Z6 0,571/0,555–0,591 kPa, rezerva 8,8 Pa, 19,6 Pa).

## 3. Provjere

- `lektura_check.py source/u02_…md`: **ok** (nema redaka STROGO ni „provjeri”).
- `tools/check_u02_sketch_geometry.py`: **PASS** (7 slika).
- `tools/audit_publication.py`: **Publication audit PASS** (U02: 6 primjera, Z1–Z6 [T1,T1,T2,T2,T3,T4]).
- Napomena: datoteka je već prije lekture imala necommitanu izmjenu u radnoj kopiji (11 obrisanih
  redaka u odnosu na HEAD); polazište lekture bila je ta radna kopija (= `lektura_base`).
