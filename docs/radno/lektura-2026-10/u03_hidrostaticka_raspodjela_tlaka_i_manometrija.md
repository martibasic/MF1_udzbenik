# Lektura: source/u03_hidrostaticka_raspodjela_tlaka_i_manometrija.md (pog. 3)

Prošao sam cijelu datoteku, od uvoda i teorije preko izvoda, CFD blokova, primjera, samoprovjere i Z1–Z6 do sažetka.
Polazni tekst bio je već prilično uredan. Napravio sam oko 50 izmjena, uglavnom sitnih, bez promjene matematike, brojeva, ID-jeva i polja.

## 1. Izmjene po vrstama

- **Upućivanja s krivim padežom (4):** `iz @ex-…` → `iz primjera [-@ex-…]` (CFD balastni tank); `kao u @ex-…` → `kao u primjeru [-@ex-…]` (balastni tank, provjera 2); `Ručni @ex-…` → `Ručni proračun u primjeru [-@ex-…]` (CFD usis), usklađeno s obrascem iz pog. 5 i 9.
- **Sročnost i padeži:** „plohu (okomita na os x)” → „(okomitu …)”; „pa je manometarski nula” → „pa je manometarski tlak jednak nuli”; „Provjeri je li dobiven raspored” → „dobiveni raspored”.
- **Kalkovi i nespretni izrazi:** „Neto sila po osi x je” → „Rezultantna sila tlaka u smjeru osi x iznosi”; „predstavlja gubitak” → „odgovarao bi gubitku”; „izvijestio o tlaku” → „pokazao tlak”; „Isti se princip koristi za” → „Isto načelo služi za”; „pri značajnom strujanju” → „pri izraženom strujanju”; „Kod otvorenog/zatvorenog spremnika” → „U otvorenom/zatvorenom spremniku”; „miruje prema stijenkama” → „miruje u odnosu na stijenke”; „gubitni doprinosi” → „doprinosi brzine i gubitaka” (3×).
- **Nazivlje i dosljednost:** „penjanje” → „uspon” (prema uvodu i sažetku, 3×); „volumne sile” → „volumenske sile”; „gubicima” → „gubitcima”; „dodira ulja i žive” → „granice ulja i žive”; „na podnožju” → „u podnožju” (2×); „precjenjenje” → „precjenjivanje” (oblik nije standardan).
- **Red riječi i enklitike:** „Najčešća pogreška jest uzeti” → „Najčešća je pogreška uzeti”; „njegova vanjska stijenka jest oplata” → „njegova je vanjska stijenka oplata”; „Tlak u mreži zato određuje kota …” → „Zato tlak u mreži određuje kota …, sve dok voda miruje”.
- **Zarezi:** neodređena odnosna rečenica („plinove, u kojima…”, „stanje C, u kojem…”), umetak („Za izotermalnu atmosferu, uz pretpostavku …, može…”), suvišan zarez ispred „jer” uklonjen.
- **Pravopis i tipografija:** `$0$--$140$` → `$0$–$140$` (4×, crtica u rasponu); uklonjen razmak ispred `&nbsp;` u naslovu primjera o usisu crpke.
- **Jasnoća i logika:** „Fluid … ne može nositi … ali i dalje nosi raspodjelu normalnog naprezanja” → „ne može preuzeti … ali i dalje preuzima normalno naprezanje, odnosno tlak”; „Ni piezometar ni manometar nisu novi zakon” → „ne uvode novi zakon, nego su …”; odgovor 3 u samoprovjeri sada izravno odgovara na pitanje „Kada…” („Kad se gustoća mijenja ili kad je na putu više fluida: …”); Z5, točka 5 („Ocijeni samo zadane mjerne zahtjeve.”) → „Pri ocjeni razmotri samo zadane mjerne zahtjeve.”, jer je riječ o ograničenju, a ne o zasebnom zadatku.

Reprezentativni primjeri (prije → poslije):

1. „Takva mjerenja koriste se u spremnicima, piezometrima te za razliku tlakova preko filtra ili izmjenjivača topline.” → „Takva se mjerenja primjenjuju u spremnicima i piezometrima te za određivanje razlike tlakova na filtru ili izmjenjivaču topline.”
2. „Isti hod kroz slojeve u brodskoj praksi određuje razinu tereta …” → „U brodskoj se praksi istim hodom kroz slojeve određuje razina tereta …”
3. „Sustav mjerenja razine mora, međutim, sadržavati pretlak inertnog plina i sondiranu debljinu vode: dvofluidni model …” → „… mora, međutim, uzeti u obzir pretlak inertnog plina i sondiranu debljinu vode, odnosno primijeniti dvofluidni model …”
4. „Za crpku u radu treba bilancu energije s brzinom i gubicima te usporedbu …” → „Za crpku u radu potrebni su bilanca energije s brzinom i gubitcima te usporedba …”
5. „… prije procjene tlaka pare obnavlja apsolutni tlak. … Taj će se usisni problem nastaviti uz crpku u pog. 13.” → „… i prije usporedbe s tlakom pare obnavlja apsolutni tlak. … Problem usisa nastavlja se, uz crpku, u pog. 13.”
6. „Ako je gustoća homogena i može se smatrati konstantnom” → „Ako je fluid homogen i njegova se gustoća može smatrati konstantnom”
7. „Za uvlačenje zraka treba pratiti i granicu vode i zraka.” → „Da bi se opisalo uvlačenje zraka, treba pratiti i granicu vode i zraka.”

Naslove bez `{#id}`, naslove zadataka (D06) i opise slika nisam mijenjao jer u njima nije bilo pogrešaka.

## 2. Sadržajni nalazi koje NISAM ispravio

Sve brojčane rezultate u primjerima i kontrolnim rezultatima Z1–Z6 ponovno sam izračunao i svi se slažu. Nalazi su ovi:

1. **R442 — opis veličine ne odgovara broju:** „Stupac plina od nekoliko paskala zanemariv je …”, a u jednadžbi `eq-sondiranje-stupac-inertnog-plina` (R434) izlazi $27{,}2\ \text{Pa}$. Točnije bi bilo „nekoliko desetaka paskala”.
2. **R498 i dalje (balastni tank), sukob s tablicom notacije:** visina tanka označena je $H_t$, a tablica u `docs/urednicki_stil.md` tu oznaku čuva za visinu turbine. Gaz je $T_g$, a tablica propisuje $T$. Balast ima $\rho_b$, iako je to ista morska voda kao $\rho_{mv}$. Iste oznake javljaju se u CFD bloku (R192, $\rho_{mv} g(T_g-H_t)$).
3. **R517–R552 — engleski indeksi:** $p_{M,ext,\dots}$ i $p_{M,int,\dots}$ (ext/int). Tablica traži hrvatske indekse (vidi gubitak, stijenka, preljev). Moguća zamjena je npr. vanj/unut.
4. **R119 i R831 — oznaka efektivnog polja nije ujednačena:** $\vec{g}_{eff}$ prema $\vec g_{\mathrm{eff}}$.
5. **R598 — oznaka $h_T$** (visina vode u vodotornju) koristi indeks $T$, koji se drugdje veže uz gaz ili temperaturu. Riječ je o sitnici i nije izravna kolizija.
6. **Višeznačni $H$ unutar poglavlja:** karakteristična visina atmosfere (R148), usisna visina crpke (R451) i ukupna visina tekućine u Z4 (R733). Svaki je put uveden lokalno, pa nema pogreške, samo je to dobro znati.
7. **R355 prema R350 — razmak ispred %** unutar matematike: `0{,}24\ \%` prema `100\%`. Tipografska nedosljednost u formuli, koju nisam dirao.
8. **Anglizam „ullage”** (primjer sondiranja i balastni tank, R365–R549): ostavljen je kao brodski stručni naziv vezan uz oznaku $U$. Ako postoji usvojen hrvatski naziv („ulaž” ili „prazni prostor tanka”), treba ga dosljedno uvesti pri prvom spomenu. To je autorska odluka.
9. **ID primjera „…usisu-pumpe…”** (R445) i dalje sadrži „pumpe”, a tekst koristi „crpku”. ID je stabilan i nisam ga dirao. Na čitatelja ne utječe.

## 3. Provjere

- `lektura_check.py source/u03_…md`: **ok**. Matematika, ID-jevi, atributi, ograde, polja, razine, brojevi i ciljevi upućivanja isti su kao u polaznom stanju. Četiri `@id` → `[-@id]` imaju iste ciljeve.
- `tools/check_u03_sketch_geometry.py`: **PASS** (4/4).
- `tools/audit_publication.py`: **Publication audit PASS** (U03: 6 primjera, 6 zadataka [T1,T1,T2,T2,T3,T4]).
- Render, generatore ni git naredbe nisam pokretao. Didaktička kvaliteta jezika moja je autorska procjena i alati je ne dokazuju.
