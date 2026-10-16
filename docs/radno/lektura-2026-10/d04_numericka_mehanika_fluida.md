# Lektura: source/d04_numericka_mehanika_fluida.md

## 1. Izmjene

Pregledana je cijela datoteka: uvod, tablica povezanih primjera, okvir „Opseg dodatka”, pojmovnik metoda, alati, rječnik MF1 → CFD, polja i izlazi, granice primjenjivosti, trošak, šest koraka Venturijeva tijeka, V&V paketi, veza sa Z6, okvir granice modela, literatura i sažetak. Napravljeno je oko 42 zahvata (113 zamijenjenih riječi ili skupina riječi):

- **Upućivanja s krivim padežom** (4): `iz @sec-realni-tok-cfd` → `iz odjeljka [-@sec-realni-tok-cfd]`; `u @ex-stepenica-mjerenje-cfd` → `u primjeru [-@ex-…]`; `iz @sec-cfd-venturi` → `iz odjeljka [-@sec-cfd-venturi]`; „Ćelijska bilanca @eq-… pokazuje” (dvije imenice u nominativu jedna uz drugu) → „Ćelijska bilanca (jednadžba [-@eq-…]) pokazuje”. Popis `@sec → @sec` i „vrati se na @sec-…” ostali su nepromijenjeni jer je za muški rod neživo akuzativ jednak nominativu („na odjeljak”).
- **Kalkovi i pogrešni glagoli** (~10): „izvijesti protok …” → „navedi protok …”; „motivira lokalni nagib” → „obrazlaže se lokalnim nagibom”; „odluku nosi izračunana veličina” → „odluka se temelji na izračunanoj veličini”; „predstavlja lokalnu aproksimaciju” → „lokalna je aproksimacija”; „povijesti sila” → „zapisi sila kroz iteracije”; „hardver” → „računalna oprema”; „klizajuća mreža” → „klizna mreža”; „kompatibilan par uvjeta” → „usklađen par uvjeta”.
- **Sročnost, padeži i prijedlozi** (~8): „pitanja kojima jednostavniji model … ne daje odgovor” → „pitanja na koja …”; „dosljedno odabranoj shemi” → „u skladu s odabranom shemom”; „razlika viskoznog rješenja prema idealnom Bernoulliju” → „razlika između viskoznog rješenja i idealnoga Bernoullijeva rješenja”; „trajan gubitak kroz uređaj” → „trajni gubitak u uređaju”; „slaganje na toj točki” → „u toj točki”.
- **Narušena usporednost u nabrajanju** (1): „o broju ćelija i jednadžbi, vremenskih koraka, … te hardveru” → „o broju ćelija, jednadžbi, vremenskih koraka, … te o računalnoj opremi”.
- **Nazivlje** (~6): „meniska” → „meniskusa” (standard); „zid” → „stijenka”; „turbulencijski model” → „model turbulencije”; „Bernoulli” → „Bernoullijeva jednadžba”; „opaženi red” → „opaženi red točnosti”; „podacima” → „podatcima” (oblik knjige).
- **Dvosmislenosti i red riječi** (~6): „rješava li numerički postupak pravilno zadane jednadžbe?” (moglo se čitati kao „pravilno zadane”) → „rješava li numerički postupak zadane jednadžbe pravilno?”; „Profil ostaje primjer …” (moglo se shvatiti kao profil brzine) → „Aeroprofil ostaje primjer …”; „Za dublju diskretizaciju” → „Za dublje upoznavanje s diskretizacijom”.
- **Spojene ili preoblikovane rečenice** (~5): dvije rečenice o početnom uvjetu spojene su u jednu s dvotočkom; „Mali rezidual uz još promjenjiv gubitak nije dovoljan za zaustavljanje” → „Mali rezidual nije dovoljan razlog za zaustavljanje ako se gubitak još mijenja”.

Reprezentativni primjeri:

1. „Za Venturi pad **statičkog** tlaka do grla velikim dijelom znači ubrzavanje.” → „U Venturijevoj cijevi pad **statičkog** tlaka do grla većim je dijelom posljedica ubrzavanja fluida.”
2. „Samo pod odgovarajućim uvjetima jednakih brzina i visina statički pad tlaka izravno mjeri gubitak.” → „Statički pad tlaka izravno mjeri gubitak samo kad su brzine i visine uspoređenih presjeka jednake.” (ograda „samo” zadržana)
3. „Osjetljivost na … zasebna je analiza; nije ni mrežna konvergencija ni zamjena za mjerenje.” → „Osjetljivost na … ispituje se zasebnom analizom, koja nije ni provjera mrežne konvergencije ni zamjena za mjerenje.”
4. „U [pog. 13] lokalni CFD vraća koeficijent gubitka jednostavnijem modelu cijele instalacije.” → „U [pog. 13] lokalni CFD daje koeficijent gubitka koji se zatim vraća u jednostavniji model cijele instalacije.”
5. „Najfiniji FUN3D rezultat $C_D=…$ zaokružen je …” → „Rezultat FUN3D na najfinijoj mreži, $C_D=…$, zaokružen je …”
6. „Programske postavke provjeri u [vodiču]; nisu preduvjet za MF1.” → „Programske postavke, koje nisu preduvjet za MF1, provjeri u [vodiču].”
7. „Uz zadane neovisne, centrirane normalne doprinose …” → „Za zadane neovisne normalne doprinose centrirane na nulu …” (izraz preuzet iz Z6 u pog. 12)

Naslovi bez `{#id}` i naslovi s ID-jem (koraci 1–6, „Opseg dodatka”, „Rječnik MF1 → CFD”) nisu mijenjani.

## 2. Sadržajni nalazi koje NISAM ispravio

1. **Notacija, r. 62 (tablica rječnika):** Bernoulli je zapisan kao `$p/\rho+v^2/2+gz=\mathrm{konst.}$`, a standard (urednicki_stil, r. 88) propisuje „Bernoulli s $p/(\rho g)$”, odnosno oblik s visinama. Treba odlučiti je li energijski oblik po jedinici mase ovdje namjerna iznimka.
2. **Notacija, r. 82:** `$\tau_{st}=\mu(\partial v_t/\partial n)_w$`. Indeks $w$ (wall) protivi se standardu „hrvatski indeksi … ne $\tau_w$”. Dosljednije bi bilo $(\cdot)_{st}$.
3. **Notacija, r. 110:** u dodatku piše $\rho=870$ kg/m³, a u izvornom primjeru (u08, r. 577) $\rho_u=870$ kg/m³. To je manja nedosljednost oznaka.
4. **ID primjera:** `@ex-u09-venturijeva-cijev-za-mjerenje-protoka-ulja-t2` definiran je u `u08_…` (r. 571). Prefiks `u09` u ID-ju je povijesni ostatak. Upućivanje radi, a ID se po pravilima ne mijenja; navodim to samo radi provenijencije.
5. **r. 175:** „Veza sa Z6 u 12. poglavlju” piše broj poglavlja ručno. Ostatak dodatka koristi `mf1-chapter-ref`, pa bi se broj pri promjeni redoslijeda poglavlja razišao s numeracijom. Nije jezično pitanje, pa nije mijenjano.
6. **r. 173:** izvorno „Profil ostaje primjer usporedbe” promijenjen je u „Aeroprofil …”. Iz konteksta (tablica, NACA 0012) jasno je da se misli na paket `hydrofoil_experiment`; autorica neka potvrdi.

Brojke su provjerene i ispravne: interpolacija (8,08°; 0,00995) i (10,10°; 0,01175) daje nagib 0,000891/° i vrijednost 0,01166089 pri 10,00°; doprinos 0,1° · 0,000891 ≈ 0,00009; $Q\approx5{,}248$ L/s odgovara rješenju u u08.

## 3. Provjere

- `lektura_check.py source/d04_numericka_mehanika_fluida.md` → **ok** (matematika, brojevi, ID-jevi, upućivanja, atributi, ograde, poveznice nepromijenjeni; `@id` → `[-@id]` ne mijenja ciljeve).
- `tools/audit_publication.py` → **Publication audit PASS**.
- Render nije pokrenut (prema uputama). Treba vizualno potvrditi da `[-@sec-…]` u dodatku ispisuje samo broj odjeljka.
