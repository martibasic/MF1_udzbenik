# Lektura: source/u08_energijska_jednadzba_i_bernoulli.md (pog. 8)

Pregledana je cijela datoteka (923 retka): uvod, teorija, tri izvoda, okviri, šest riješenih primjera, samoprovjera, Z1–Z6 s naputcima i kontrolnim rezultatima, napomene uz skice i završni okvir. Promijenjeno je oko 80 redaka, a sve izmjene su uređene alatom Edit.

## 1. Izmjene po vrstama

- **Upućivanja s krivim padežom ili udvojenom imenicom (8):** `od @eq-…`, `slučaj @eq-…`, `treba @eq-…`, `U @sec-…` i „Energijska jednadžba @eq-…” (ispisivalo bi se „Energijska jednadžba jednadžba …”) pretvoreni su u imenicu u ispravnom padežu + `[-@id]`.
- **Kolokvijalno „Bernoulli/Bernoullija” kao imenica jednadžbe (oko 20):** zamijenjeno s „Bernoullijeva jednadžba” u odgovarajućem padežu. Isto vrijedi za „Venturija, Pitota” i „Torricelli”. Pojedinačni „Bernoulli” ostavljen je samo ondje gdje autorski tekst namjerno koristi kraći naziv.
- **Kalkovi i glagoli:** „vrši rad” → „obavlja rad”, „predstavlja” → „opisuje”, „značajna pogreška” → „znatna pogreška”, „u impeleru” → „u radnom kolu”, „ulazi u usisne uvjete” → „utječe na usisne uvjete”, „biva guran” → aktivna konstrukcija, „pomnoženu masenim protokom” → „pomnoženu s masenim protokom”.
- **Bezlični pasiv u izvodima → „mi”:** „Promatra se” → „Promatramo”, „Pretpostavlja se” → „Pretpostavljamo”, „Računaju se redom” → „Redom računamo”.
- **Sročnost, red riječi i enklitike:** „a u strojarstvu mjeri protok ulja i brzina zraka” → „a u strojarstvu se njome mjere…”, „manometarski tlak je negativan” → „manometarski je tlak negativan”, „HGL pada gdje fluid ubrzava” → „…ondje gdje se fluid ubrzava”.
- **Zarezi:** uklonjen je zarez ispred „jer” iza glavne rečenice (3 mjesta), a dodan je veznik „a” u nizovima suprotnosti.
- **Telegrafski stil u rješenjima pretvoren u rečenice:** „Iz kontinuiteta: …” → „Iz jednadžbe kontinuiteta slijedi …, pa je”, „…iz Bernoullija:” → „Bernoullijeva jednadžba daje”, a fragment „Smanjiti gubitke…” → „Treba smanjiti gubitke…”.
- **Ponavljanja i nejasnoće:** dvostruko „ostaje” u samoprovjeri 3, „prema tomu lokalnom” → „prema tom lokalnom”, „Živin diferencijalni manometar gustoće ρ_Hg” → „Diferencijalni manometar sa živom gustoće ρ_Hg”.
- **Završni okvir:** stavke popisa „Nakon ovoga poglavlja…” završavaju točkom-zarezom, kao u pog. 6 i 14.
- **Naslovi:** u oznakama primjera uklonjen je suvišan razmak ispred `&nbsp;` (2). Labela izvoda „…izvod Bernoullija…” → „…izvod Bernoullijeve jednadžbe…”. Naslov Z2 s `{#id}` glasio je „Venturijeva cijev u vodu rashladne vode”, što se lako krivo pročita kao „voda”; sada glasi „Venturijeva cijev u cjevovodu rashladne vode”.

### Reprezentativni primjeri (prije → poslije)

1. `Polazimo od @eq-…-04 za stacionarno…` → `Polazimo od jednadžbe [-@eq-…-04] za stacionarno…`
2. `Energijska jednadžba @eq-energijska-jednadzba-kv između A i P` → `Energijska jednadžba [-@eq-energijska-jednadzba-kv] između A i P`
3. `Na element djeluju dvije vrste sila koje vrše rad` → `… koje obavljaju rad`
4. `kraći uređaj biramo samo ako je dodatni gubitak manji od uštede prostora vrijedne za crpnu snagu` → `kraći uređaj biramo samo ako ušteda prostora vrijedi više od crpne snage potrebne za dodatni gubitak`
5. `Tijekom … element prelazi udaljenost $ds = v\,dt$, podignuvši se za visinski element …` → `… element prijeđe udaljenost $ds = v\,dt$ i pritom se podigne za visinski element …`
6. `Pitotova cijev … izvučena je kroz dno trupa otvorom prema pramcu, u slatku vodu … koja u sustavu vezanom uz brod jednoliko nastrujava brzinom broda.` → dvije rečenice: `… izvučena je kroz dno trupa u slatku vodu …, s otvorom okrenutim prema pramcu. U sustavu vezanom uz brod voda jednoliko nastrujava brzinom broda.`
7. `Postavljanjem Bernoullija … poništavaju se jednaki tlačni članovi, a ostaje razlika geodetskih visina i ostaje $v^2/(2g)=H$` → `Postavimo li Bernoullijevu jednadžbu …, jednaki se tlačni članovi poništavaju, pa razlika geodetskih visina daje $v^2/(2g)=H$`
8. `Iz kontinuiteta izrazom za brzinu u grlu prijeđi s promjera na pad tlaka.` → `Pomoću jednadžbe kontinuiteta izrazi brzinu u grlu i tako prijeđi s promjera na pad tlaka.`

## 2. Sadržajni nalazi koje NISAM ispravio

Ponovno sam izračunao sve riješene primjere (konfuzor, mlaz, sifon, usisni vod, Venturi s uljem, Pitot) i sve kontrolne rezultate Z1–Z6, uključujući granice intervala u Z5 i Z6. Svi se slažu sa zadanim podatcima. Brojčanih pogrešaka nisam našao.

1. **Pojam „usisna košara (engl. *sea chest*)”** (r. 493: „Voda ulazi kroz usisnu košaru (engl. *sea chest*) u boku broda”). U brodskom nazivlju *sea chest* je usisni zdenac, odnosno usisni sanduk (kingston), a „usisna košara” češće znači sito ili rešetku. Autorica neka provjeri naziv. Isti se pojam ponavlja u r. 510, 564 i 568.
2. **Mjerna jedinica pada HGL-a u primjeru s uljem** (r. 615: „`HGL` je ondje za $\Delta p/(\rho g)=2{,}634\ \text{m}$ niže”). Vrijednost je u metrima **stupca ulja** (ρ_u = 870), što tekst ne kaže. Drugdje se piše „m vodenog stupca”, pa bi čitatelj mogao pomisliti da je riječ o vodi. Predlažem dodati „stupca ulja”.
3. **Miješanje `HGL`/`EGL` u kodnom fontu (backtick) i običnog HGL/EGL** (npr. r. 54, 60, 68, 77, 615 prema r. 3, 68, 461). Tipografija je nedosljedna, a backtickove nisam dirao.
4. **Naslijeđeni nazivi „u09” u poglavlju 8** (r. 11 `#fig-uvod-u09`, `u09_*.svg`, `u09_venturi.ipynb`, ID-jevi `ex-u09-…`, `task-u09-…`). Stabilni su ID-jevi, pa ih ne treba mijenjati. Bilježim ih samo kao izvor moguće zabune.
5. **Re u Pitotovu primjeru** (r. 675: „Vrijednost $Re_s$ reda $10^4$”, uz izračunanih 8 700). To je prihvatljivo, ali preciznije bi bilo „reda $10^4$ (≈ 9·10³)”.
6. **Promjena naslova Z2** (vidi gore) mijenja tekst koji generator prenosi u `source/d06_kljuc_kontrolnih_rezultata.md` i `assets/content-index.json`. Te izvedenice treba obnoviti s `python scripts/build_book.py --write`. Prema uputama nisam pokretao generator. Audit trenutačno prolazi i bez toga.

## 3. Provjere

- `lektura_check.py source/u08_energijska_jednadzba_i_bernoulli.md` → **ok**: nema redaka STROGO, `numbers` ni `refs`.
- `tools/check_u08_sketch_geometry.py` → **PASS** (146 provjera).
- `tools/audit_publication.py` → **Publication audit PASS**.
