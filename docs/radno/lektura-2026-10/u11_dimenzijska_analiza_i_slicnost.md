# Lektura: source/u11_dimenzijska_analiza_i_slicnost.md (pog. 11)

Prošla sam cijelu datoteku (994 retka): uvod, teoriju, izvode, CFD blokove, granicu
modela, dijagram odluke, šest riješenih primjera, interaktivni blok, „Provjeri sebe”,
Z1–Z6 s naputcima i kontrolnim rezultatima, napomene uz skice i završni okvir.
Sve sam uređivala alatom Edit. Brojeve u primjerima i kontrolnim rezultatima
provjerila sam računski i svi se slažu.

## 1. Izmjene (oko 95 zahvata)

- Upućivanja s krivim padežom (5): `prema @eq-ittc-1957` → `prema jednadžbi [-@eq-ittc-1957]`;
  `prema @eq-froudeova-hipoteza` → `prema jednadžbi [-@…]`; `na @fig-u14-vjezbe` →
  `na slici [-@…]`; `Ručni @ex-…` → `Riješeni primjer [-@ex-…]`. Upućivanja u zagradi
  i u nominativu (subjekt) ostala su nepromijenjena.
- Red riječi i enklitike (oko 12): „Kavitacijski broj je posebni” → „poseban je”;
  „U vučnom bazenu zato se” → „Zato se u vučnom bazenu”; „U Z6 $F_m$ je” → „U Z6 je $F_m$”.
- Kalkovi i nespretni izrazi (oko 25): „predstavlja”, „koristi”, „kod broda”, „istovremeno”,
  „iz Bernoullija”, „incipijencija”, „po Froudeovoj sličnosti”, „empirijski/numerički”,
  „tlak/temperatura”.
- Sročnost i potpunost (oko 15): „jednaki $Re$ … omogućuju” → „jednak $Re$ … omogućuje”;
  „jednak oblik ulaznog profila i relativnu hrapavost” → „… i jednaku relativnu hrapavost”;
  „Koeficijent trenja, otpora i tlaka” → „Koeficijenti …”.
- Zarezi i interpunkcija (oko 10): uklonjen zarez ispred „i” u upitnim rečenicama, dodano
  „a ne”, u popisu „Nakon ovoga poglavlja” sada je „;” umjesto „.”.
- Dosljednost nazivlja (oko 8): „otporna kriza” → „kriza otpora” (izjednačeno sa slikom
  i bilježnicom); „skok” → „hidraulički skok”; „viskoznosti $\nu$” → „kinematičke
  viskoznosti”; „brzinu toka i širenja zvuka” → „brzinu toka i brzinu zvuka”.
- Preoblikovane ili razbijene rečenice (oko 10): definicija $C_p$/$Eu$, odlomak o
  dimenzijskoj homogenosti, „Najčešća pogreška”, „Kamo dalje”.

Reprezentativni primjeri „prije → poslije”:

1. „Za razvijeno strujanje u kružnoj cijevi $Re\lesssim2300$ obično je laminarno” →
   „Razvijeno strujanje u kružnoj cijevi pri $Re\lesssim2300$ obično je laminarno”
2. „Oznaka $F_i$ predstavlja inercijsko mjerilo, a ne dodatnu vanjsku silu.” →
   „Pritom je $F_i$ inercijsko mjerilo, a ne dodatna vanjska sila.”
3. „Ručni @ex-u14-froudeova-… računski pokazuje” → „Riješeni primjer [-@ex-u14-froudeova-…] računski pokazuje”
4. „istim fluidom i ovim mjerilom obje sličnosti nisu moguće” →
   „s istim fluidom i u ovom mjerilu ne mogu se ostvariti obje sličnosti”
5. „ta provjera traži gubitke, temperaturu, karakteristiku incipijencije i NPSH” →
   „za tu su provjeru potrebni gubitci, temperatura, karakteristika početka kavitacije i NPSH”
6. „Parovi mjerila shematski su i nemaju numeričko mjerilo” →
   „Parovi su prikazani shematski, bez brojčanog mjerila”
7. „Pokušaj … ili pogrešna karakteristična duljina (npr. stranica umjesto $D_h$); te miješanje …” →
   „Pokušaj …, pogrešna karakteristična duljina (npr. stranica umjesto $D_h$) te miješanje …”
8. „a $C_R$ preostali, pretežno valni otpor” → „a $C_R$ koeficijent preostalog, pretežno valnog otpora”

Nisu mijenjani: matematika, ID-jevi, naslovi bez `{#id}`, naslovi zadataka s `{#id}`
(zbog ključa D06), oznake polja, razine, putanje i SVG-ovi.

## 2. Sadržajni nalazi koje nisam ispravila

1. **Redak 179** — „Slika [-@fig-u14-pi-buckingham] prikazuje taj postupak shematski na primjeru otpora kugle.”
   Slika prikazuje samo dimenzijsku matricu (prvi i drugi korak), a fig-alt izričito kaže
   „Π-grupe nisu na slici”. Predlažem: „prikazuje dimenzijsku matricu tog postupka”.
2. **Interpunkcija u formulama** — `eq-slicnost-razrada-koraka-02` (oko r. 223) i
   `eq-slicnost-matematicki-izvod-otpor-kugle-daje-cd-re-02` (oko r. 257) završavaju zarezom
   (`…\right),` odnosno `= \Phi(Re),`), a iza njih počinje nova rečenica velikim slovom
   („Dimenzijska analiza tako…”, „Unutar navedenih…”). Zarez bi trebao biti točka.
3. **Oko r. 306** — „…omjer snaga … $\lambda_L^{7/2}$, dok se viskozni dio skalira preko $C_F$,
   a ne faktorom $\lambda_L^3$.” Ovdje se miješa faktor sile ($\lambda_L^3$) s
   prethodno izvedenim faktorom snage ($\lambda_L^{7/2}$). Za snagu bi bilo dosljedno
   „a ne faktorom $\lambda_L^{7/2}$”, ili rečenicu treba vezati uz otpor.
4. **Z3 (r. 829–855), nazivlje** — naslov „Pretlak senzora…” i „najmanji pretlak” odnose se
   na negativne vrijednosti $p_M=-20{,}0$ kPa i $p_{M,min}=-1{,}660$ kPa. Negativan
   pretlak zapravo je podtlak. Predlažem „manometarski tlak” ili „očitanje senzora”. Naslov
   nisam mijenjala jer ulazi u D06.
5. **P1 (r. 396 / slika)** — tekst kaže „razvijeni ravni kružni kanal”, a naslov slike i
   fig-alt kažu „ista cijev”. Predlažem dosljedno „cijev”.
6. **R. 977 (završni okvir)** — „$Re$ mjeri relativnu važnost viskoznosti” nepotpuno je
   prema definiciji u poglavlju (omjer inercije i viskoznosti).
7. **P2, r. 488** — „Trenje modela po jedinici dinamičkog tlaka dvostruko je veće” — $C_F$
   je normiran i oplakanom površinom; preciznije bi bilo „po jedinici dinamičkog tlaka
   i oplakane površine”.
8. **P3, r. 523** — iz prikazanih zaokruženih brzina (2,12 i 19,10 m/s) izlazi
   $p_2\approx-78{,}9$ kPa, a tekst navodi −78,8 kPa (dobiveno iz nezaokruženih vrijednosti).
   Razlika je zanemariva; spominjem je samo radi provjere čitatelja.
9. **Notacija** — $\sigma_{kr}$ (kritični kavitacijski broj) nije u tablici notacije
   uredničkog stila. Poglavlje ga dosljedno uvodi uz $\sigma_{kav}$, pa to nije pogreška,
   nego kandidat za dodatak A. ID-jevi i nazivi SVG-ova nose staru oznaku `u14`
   (`fig-u14-…`, `ex-u14-…`). To je očekivano jer su ID-jevi stabilni, ali pri pregledu
   može zbuniti.

## 3. Provjere

- `lektura_check.py source/u11_dimenzijska_analiza_i_slicnost.md` → **ok** (nema redaka STROGO
  ni „provjeri numbers”/„refs”).
- `tools/check_u11_sketch_geometry.py` → **PASS U11** (devet SVG-ova).
- `tools/audit_publication.py` → **Publication audit PASS** (U11: 6 primjera, 6 zadataka
  [T1,T1,T2,T2,T3,T4]).
- Nisam pokretala generatore ni render (prema uputi). D06 i omotači nisu dirani.
