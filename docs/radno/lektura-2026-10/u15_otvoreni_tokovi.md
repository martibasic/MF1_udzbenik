# Lektura: source/u15_otvoreni_tokovi.md (pog. 15)

## 1. Izmjene

Prošao sam cijelu datoteku: uvod, teoriju, oba izvoda, blokove (Fizikalno značenje,
Granica modela, tri CFD bloka, Numerički pokus, Za ponijeti), pet riješenih primjera,
šest zadataka s naputcima i kontrolnim rezultatima, napomene uz skice, fig-alt i
samoprovjeru. Promijenjeno je oko 60 odlomaka ili stavaka (97 redaka u diffu).

Vrste izmjena:
- **Upućivanja u kosom padežu (5):** `iz [-@eq-…]` / `u [-@eq-…]` / `Ručni @ex-…` dopunjeni
  imenicom („iz jednadžbe [-@eq-manning]”, „Ručni račun u primjeru [-@ex-…]”, „jednadžba
  [-@eq-specificna-energija]” kao umetak). Nominativni `@ex-…` u odjeljku o ustavi ostao je
  nepromijenjen jer je ondje ispravan.
- **Nazivlje:** „energijska linija” → „energijska crta” (3×, prema urednickom_stilu.md i D01);
  „omočen opseg” → „omočeni opseg” (3×, ujednačeno s ostatkom poglavlja); „prema obali” →
  „u odnosu na obalu” (4×, Z1, naputak, kontrolni rezultat, napomene; „prema” je ovdje bio
  dvosmislen: „u smjeru obale”); „varijanta” → „inačica”; „fenomen” → „pojava”.
- **Kalkovi i nespretni izrazi:** „predstavlja duboku vodu”, „što njezin mlaz radi”,
  „obrada stijenke”, „Nerazlučeni mjehurići”, „Traže se projektni protok” (u tekstu zadatka),
  „Kod postupno promjenjivog toka”, „proizvesti promjenu”, „dolaze uzvodno” (dvosmisleno).
- **Razbijene preduge rečenice (≈8):** Granica modela, odjeljak o ustavi/preljevu, odluka o
  položaju skoka, Fizikalno značenje (Froude kanala i broda), Z6, odgovor 3 u samoprovjeri.
- **Red riječi, enklitike, sročnost, zarezi:** „Između presjeka energijska bilanca može se
  zapisati”, „ali unutar skoka tok je…”, „$y_{2,dop}$ je naveden”, mala slova nakon formule
  koja završava točkom („dijeli se…” → „Jednadžbu dijelimo…”).
- **Postupak analize:** bezlični pasiv („Određuju se…”) pretvoren u upute u 2. licu jednine
  („Skiciraj”, „Odredi”, „Primijeni”), u skladu s uputom o obraćanju studentu.
- **Pravopis:** „s obje strane” → „s obiju strana”; „kojoj je gornja granica” → „čija je gornja
  granica”; zarez uz umetnute dodatke.

Reprezentativni primjeri (prije → poslije):
1. „U ovom SI zapisu Manningov koeficijent $n$ ima jedinicu …; nije bezdimenzijski. … Jednadžba
   nije zamjena za lokalnu bilancu pri brzom suženju…” → „… ima jedinicu … i nije bezdimenzijski.
   … Jednadžba ne zamjenjuje lokalnu bilancu pri naglom suženju, na preljevu ili u hidrauličkom skoku.”
2. „Preuređena, $$…$$ dijeli se trivijalnim rješenjem $y_1=y_2$, dakle faktorom $(y_1-y_2)$, i
   ostaje …” → „Nakon preuređenja dobivamo $$…$$ Jednadžbu dijelimo faktorom $(y_1-y_2)$, koji
   pripada trivijalnom rješenju $y_1=y_2$, pa ostaje …”
3. „$\rho g b y_1^2/2$ (uzvodno, u smjeru toka)” → „(na uzvodnom presjeku, u smjeru toka)”.
4. „Pri nadkritičnom režimu obje informacije dolaze uzvodno pa se mijenja i zadavanje granica.”
   → „U nadkritičnom režimu obje informacije dolaze s uzvodne strane, pa se mijenja i način
   zadavanja rubnih uvjeta.” (izvorni zapis mogao se čitati kao „putuju uzvodno”, što je fizikalno
   suprotno; nova formulacija odgovara karakteristikama.)
5. „Ručni @ex-hidraulicki-skok-bazen daje … Te veličine, očuvanje vode te prostorno i vremensko
   profinjenje provjeravamo i u CFD-u.” → „Ručni račun u primjeru [-@ex-hidraulicki-skok-bazen]
   daje … U CFD-u provjeravamo te veličine, očuvanje vode i utjecaj prostornog i vremenskog profinjenja.”
6. „$v_c=q/y_c=2{,}70$ … i …=1,00; stvarni preljev dodaje empirijski koeficijent $C_{pr}$
   (odjeljak o kontrolnim građevinama).” → „Kritična brzina je $v_c=…$, a … Za stvarni preljev
   dodaje se empirijski koeficijent $C_{pr}$ (vidi odjeljak o kontrolnim građevinama).”
7. „kapacitet pada 40 %, točno u omjeru $0{,}015/0{,}025$, jer je $Q\propto1/n$” → „Kapacitet
   pada za 40 %: budući da je $Q\propto1/n$, omjer protoka točno je jednak omjeru $0{,}015/0{,}025$.”
8. „Model hidrauličkog skoka … a bilanca količine gibanja se zatvara.” → „… a bilanca količine
   gibanja pritom se zatvara. Jesu li ti rezultati nespojivi?”

Naslovi, ID-jevi, polja, razine, formule i brojevi nisu dirani (naslov primjera
„Disipacijski bazen iza ustave” namjerno je ostavljen, vidi nalaz 3).

## 2. Sadržajni nalazi (nisu ispravljeni)

Sve sam brojeve u primjerima i kontrolnim rezultatima ručno preračunao (P1–P5, Z1–Z6). Svi se slažu.

1. **Dvoznačan $y_1$ u odjeljku „Kontrolne građevine” (oko r. 176–189).** U jednadžbi
   [-@eq-istjecanje-ispod-ustave] $y_1$ je *uzvodna* dubina („s otvorom $a$ i uzvodnom dubinom
   $y_1$”, $Q=C_d\,b\,a\sqrt{2gy_1}$), a dva retka niže $y_1\approx C_ca$ je dubina *suženog mlaza
   ispod ustave* (silovita dubina ispred skoka, kao u primjeru o bazenu). Ista oznaka u istom
   odlomku za dvije različite dubine. Uz to $C_c$ (koeficijent kontrakcije) nigdje nije
   definiran riječima.
2. **$y_1$, $y_2$ za alternativne dubine (primjer „Dvije dubine za istu energiju”, r. 227).**
   Poglavlje inače rabi $y_1$, $y_2$ za spregnute dubine skoka, a numerički pokus izričito traži
   da student objasni zašto alternativne dubine *nisu* spregnute. Ista oznaka potiče baš tu
   zabunu. Prijedlog: drugačija oznaka (npr. $y_m$, $y_s$ ili $y_a$, $y_b$).
3. **Nazivlje bazena:** naslov P-primjera „Disipacijski bazen iza ustave” (ex-hidraulicki-skok-bazen)
   prema „umirni bazen” u uvodu (r. 5), CFD bloku (r. 330) i D04. Naslov nisam mijenjao jer ulazi u
   ključ D06. Prijedlog je ujednačiti naziv na „umirni bazen” i regenerirati D06.
4. **R. 206:** „presjek s kritičnom dubinom može određivati režim toka”. Kontrolni presjek
   određuje vezu između dubine i protoka (i time uzvodnu razinu), a ne sam „režim”. Formulacija je
   neprecizna. Nisam je mijenjao jer bi to bila promjena tvrdnje.
5. **R. 256:** u $I=pA+\dot mv$ nije rečeno da je $p$ tlak u težištu presjeka. Dobro bi bilo
   dodati kratku napomenu.
6. **Primjer „Osjetljivost propusnosti…” (r. 370):** drugi traženi protok (obrasli kanal,
   $2{,}70\ \mathrm{m^3/s}$) i relativno smanjenje izračunani su tek u „Provjeri i tumačenju”, a ne u
   „Rješenju”, iako ih zadatak izričito traži.
7. **Ponovljeni podatci:** Z5 (task-skok-mjerenje) ima $y_1=0{,}250$ m i $q/y_1=6{,}0$ m/s, kao i
   P-primjer o umirnom bazenu, pa je teorijska spregnuta dubina u oba slučaja $1{,}2353$ m. Pitanje
   (T4: nesigurnost) jest drugačije, ali isti ulazni podatci slabe dojam raznolikosti.
8. **R. 377:** „logika … koju smo koristili za rashladni krug” nema upućivanja na poglavlje
   (rashladni krug provlači se kroz više poglavlja). Čitatelj ne zna na koji se dio misli.
9. **Pravopis „podkritični/nadkritični” (6×):** prema pravilu o jednačenju po zvučnosti na
   granici prefiksa Hrvatski pravopis bilježi oblike *potkritičan* i *natkritičan*. U struci je
   češći oblik bez jednačenja. Odluku treba donijeti autorica za cijelu knjigu, pa nisam mijenjao.
10. **Redoslijed razina:** audit ispisuje U15 [T1,T1,T2,T3,T4,T2]. Broj je u skladu s ugovorom
    (2×T1, 2×T2, T3, T4), ali T2 stoji na kraju, za razliku od ostalih poglavlja. To je samo napomena.

## 3. Provjere

- `lektura_check.py source/u15_otvoreni_tokovi.md`: **ok** (bez STROGO redaka i bez promjena
  brojeva; refs isti jer je `@id` → `[-@id]` zadržao ciljeve).
- `tools/check_u15_sketch_geometry.py`: **U15 SVG PASS** (2 slike).
- `tools/audit_publication.py`: **Publication audit PASS** (U15: primjeri=5, zadatci=6).
- Napomena: checker bez `PYTHONIOENCODING=utf-8` pada na Windows konzoli (cp1252) pri ispisu „č”.
  To je ograničenje okoline, a ne nalaz.
