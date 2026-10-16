# Lektura: source/u10_kolicina_i_moment_kolicine_gibanja.md (pog. 10)

Prošla sam cijelu datoteku (1146 redaka): uvod, teoriju, izvode, CFD-blokove, granicu modela, sedam riješenih primjera, samoprovjeru, Z1–Z6 s naputcima i kontrolnim rezultatima, opise slika, napomene uz skice i završni okvir. Promijenjeno je 85 redaka (85 umetanja, 85 brisanja), a matematika, brojevi i struktura nisu dirani.

## 1. Izmjene po vrsti (približno)

- **Upućivanja s krivim padežom** (12): `u @ex-…` u „u primjeru [-@ex-…]”, `iz @eq-…` u „iz jednadžbe [-@eq-…]”, `prema @eq-…` u „prema jednadžbi […]”, `Primijeni @eq-…` u „Primijeni jednadžbu […]”, `na @fig-u11-vjezbe` u „na slici […]”, a apozicija „zapis @eq-…” u „jednadžba […]”. Nominativi („Ručni @ex-… polazi”, „daje @sec-navier-stokes”) ostali su kakvi jesu.
- **Kolokvijalni ili skraćeni nazivi** (8): „Bernoulli” postaje „Bernoullijeva jednadžba”, „Newton III” postaje „treći Newtonov zakon”, „Bernoullijeva relacija” postaje „Bernoullijeva jednadžba”.
- **Kalkovi i nespretni izrazi** (≈20): „predstavlja” u „opisuje”; „glasi” za brojčanu silu u „iznosi”; „na atmosferi” u „otvorena prema atmosferi” odnosno „vlada atmosferski tlak”; „relativno prema brodu” u „u odnosu na brod”; „inercijski referentni okvir” u „inercijski referentni sustav”; „kod povratnoga toka” u „pri povratnom toku”; „u ulazu” u „na ulazu”; „vraća se iz mjerene reakcije” u „određuje se iz izmjerene reakcije”.
- **Red riječi i enklitike** (≈12): „Uvrštavanjem dobiva se” u „Uvrštavanjem se dobiva”; „Poprečna reakcija je već” u „Poprečna reakcija već je”; „su manometarski” u „manometarski su”; „Sile … se poništavaju” u „Sile … poništavaju se”.
- **Sročnost, vid i oblik** (≈6): „ostaje samo moment … i …” u „ostaju samo”; „Protok u granama zato je” u „Protoci u granama zato iznose”; „poistovjeti se” (završni okvir, opće pravilo) u „poistovjećuje se”.
- **Preformulirane rečenice** (≈10): naputak Z6, pitanja u interaktivnom bloku, Z4 (nejasno „okomito na os x” postalo je „ploču okomitu na os x”), Z5 („Jedna dovoljno velika…”), samoprovjera 3 i 4.
- **Interpunkcija i sitnice**: zarez iza inverzne zavisne rečenice („Koji doprinos prevladava, ovisi o…”); popis „Nakon ovoga poglavlja…” sada ima „;” umjesto „.” na kraju stavki, kao u u06, u08 i u14; uklonjen je suvišan razmak prije `&nbsp;` u naslovu primjera; „energetskoj” u završnom okviru zamijenjeno je s „energijskoj”.
- **Opisi slika**: „zakreće tok 60 stupnjeva” u „zakreće tok za 60 stupnjeva”; „račve s pravom granom od 60 stupnjeva” u „račve s ravnom granom i granom pod 60 stupnjeva”.

### Reprezentativni primjeri (prije → poslije)

1. „u @ex-u11-servisno-koljeno-na-sidrenom-nosacu-t2 brojčano je pokazano” → „u primjeru [-@ex-u11-servisno-koljeno-na-sidrenom-nosacu-t2] brojčano je pokazano”
2. „zapis @eq-momentum-fizikalno-znacenje-01 ostaje valjan u sustavu toga tijela jer je on inercijski … u toku količine gibanja ulazi brzina” → „jednadžba [-@eq-…] ostaje valjana u sustavu toga tijela jer je taj sustav inercijski … u tok količine gibanja ulazi brzina”
3. „Vektorskim množenjem položajem $\vec r$ prelazi u zakon momenta” → „Vektorskim množenjem s vektorom položaja $\vec r$ zakon prelazi u zakon momenta”
4. „Isti potisak jednak je skoku tlaka na disku, $F_T=\Delta p\,A_d$. Bernoulli vrijedi odvojeno…” → „Taj je potisak jednak i sili koju stvara skok tlaka na disku, $F_T=\Delta p\,A_d$. Bernoullijeva jednadžba vrijedi odvojeno…” (u izvorniku je sila izjednačena s tlakom, što dimenzijski nije točno)
5. „Strujna cijev koja obuhvaća disk zatvara kontrolni volumen.” → „Kontrolni volumen omeđuje strujna cijev koja obuhvaća disk.”
6. „Oba izlaza su na atmosferi i visini ulaza.” → „Oba izlaza otvorena su prema atmosferi i nalaze se na visini ulaza.”
7. „Vrijedi li primjena zakona količine gibanja i ako su gubitci u koljenu nezanemarivi? / Vrijedi i tada … ulazi preko različitih tlakova … mora uračunati preko proširene Bernoullijeve jednadžbe” → „Smije li se zakon količine gibanja primijeniti i kad gubitci u koljenu nisu zanemarivi? / Smije, jer … ulazi kroz različite tlakove … treba uračunati proširenom Bernoullijevom jednadžbom”
8. „Provjeri smjer promjene rezultante s … prije uporabe samo rubnih kombinacija. Traži maksimum sile, zatim…” → „Prije nego što upotrijebiš samo rubne kombinacije, provjeri kako se rezultanta mijenja s … Najprije pronađi najveću silu, a zatim…”

## 2. Sadržajni nalazi (nisam ih ispravila)

1. **R. 735, Y-račva, zaokruživanje nije dosljedno**: `R = \sqrt{664^2 + 625^2} = 912{,}1\ \text{N} \approx 0{,}913\ \text{kN}`. Iz napisanih brojeva izlazi $\sqrt{664^2+625^2}=911{,}9$ N, odnosno ≈ 0,912 kN. Vrijednost 0,913 kN dobiva se tek s nezaokruženim $R_x\approx665{,}6$ N. O tome ovise i rezerva od „87 N” (r. 744 i 748) i ključ D06, pa treba odabrati jednu razinu zaokruživanja.
2. **R. 724–726, ista bilanca**: zbroj desne strane s napisanim zaokruženim vrijednostima (94,0·11,99 + 60,2·11,99·0,5 − 154,2·6,81) daje 437,9, a ne „439”. 439 izlazi iz nezaokruženih vrijednosti, a $R_x=-664$ N iz 439 − 1103. Pogreška je mala, ali je vidljiva studentu koji račun ponavlja.
3. **R. 1124, napomene uz skice (Z2)**: izvorno je pisalo „promjeri strujne cijevi daleko ispred i iza diska u omjeru su zadanih brzina”. Kontinuitet daje $A_A/A_j=v_j/v_A$, dakle omjer promjera iznosi $\sqrt{v_j/v_A}$, i tako je nacrtano (checker r. 263 provjerava `sqrt(8/6)`). Tekst sam jezično ublažila u „određeni su omjerom zadanih brzina”, što je točno. Autorica može izričito napisati da su površine obrnuto razmjerne brzinama.
4. **R. 1122, opis slike `fig-u11-vjezbe`**: opis kaže „Šest skica…”, ali opisuje samo Z1, Z2, Z4, Z5 i Z6. Skica za Z3 (koljeno 90°) nije opisana.
5. **R. 304, naslov koraka „3. Energetska provjera”**: naziv odstupa od nazivlja „energijski” (r. 60, završni okvir). Naslov nema `{#id}`, pa ga prema pravilima nisam mijenjala.
6. **Naslijeđeni nazivi `u11_*` u pog. 10** (`fig-uvod-u11`, `u11_fig_uvod_pregled.svg`, `u11_sila_na_koljeno.ipynb`, ID-jevi `ex-u11-…`, `task-u11-…`): to su stabilni ID-jevi iz stare numeracije, a ne pogreška. Navodim ih samo radi preglednosti.
7. **R. 878, sitno zaokruživanje**: $M_0=\dot m r w=2{,}794\cdot0{,}25\cdot17{,}83=12{,}45$ N m, a u tekstu stoji „12,4 N m”. Granični je to slučaj zaokruživanja i ne mijenja zaključak.

Ostale brojčane rezultate provjerila sam ručno i podudaraju se: Pelton (1248 N, 14,98 kW, 2080 N, 26,0 kW), mlaznica (5,82 m/s, 16,4 kPa, 445 N), servisno koljeno (−1402/665 N, 1552 N, ξ≈0,34, β-varijante), T-račva (891/503 N, 1023 N), hidroenergetsko koljeno (I≈9827 N), rotirajuća mlaznica (11,4 N m, 71 W, 680 min⁻¹, 440 W) te Z1–Z6. Također je točna nejednakost $\alpha\ge\beta^{3/2}$ (r. 90).

## 3. Provjere

- `lektura_check.py source/u10_kolicina_i_moment_kolicine_gibanja.md`: **ok** (nema retka STROGO; brojevi i upućivanja u redu).
- `tools/check_u10_sketch_geometry.py`: **PASS U10** (devet SVG-ova).
- `tools/audit_publication.py`: **Publication audit PASS** (U10: primjeri = 7, zadatci = 6 [T1,T1,T2,T2,T3,T4]).

Ograničenje: provjere potvrđuju samo invarijante i strukturu. Jezična i stilska procjena autorska je.
