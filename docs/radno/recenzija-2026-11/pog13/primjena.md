# Primjenska recenzija — poglavlje 13. Gubitci, cjevovodi, crpke i mreže

Recenzent: primjenski recenzent (brodogradnja, pomorska tehnika, strojarstvo),
neovisno čitanje 8. 11. 2026. Materijal: PDF poglavlja (str. 245–262, u
izvještaju „PDF str.” = stranica knjige) i izvor
`source/u13_gubici_cjevovodi_crpke_i_mreze.md` (u nastavku `u13:redak`).
Pregledani su uvod, četiri odlomka „Računalna dinamika fluida”, P1–P6, Z1–Z6,
skice 13.1–13.4 i sažetak; izvodi nisu provjeravani.

## Sažetak

Poglavlje je tehnički pažljivo: radne točke, lanac snaga i NPSH ograđeni su
od konstrukcijske ocjene, a Z6 je primjerna integrirana brodska zadaća.
Glavni su nedostatci slaba zastupljenost brodogradnje (jedan od dvanaest
zadataka), nekoliko podataka izvan realnog raspona (učinkovitosti malog
agregata u P5, brzina na usisu u P6, uronjenost usisa u Z6) i skica Z6 bez
ventila na oplati.

Brojčano: P0 — 0, P1 — 0, P2 — 10, P3 — 12.

## Nalazi

### P0

Nema nalaza.

### P1

Nema nalaza. Napomena: ako kurikularna matrica izrijekom traži primjer obiju
struka u svakom poglavlju, nalaz P2-1 postaje P1 (kršenje ugovora). Matricu u
ovom pilotu nisam čitao.

### P2

**P2-1. Ravnoteža struka: brodogradnja se pojavljuje samo u Z6** (K16)
Mjesto: `u13:7` (PDF str. 245), P1–P6 (`u13:375–672`, str. 253–257), Z1–Z5
(`u13:718–858`, str. 259–261).
Opis: Uvod obećava „brodske balastne i rashladne sustave te sustave grijanja i
protupožarne zaštite”. Od dvanaest zadataka brodski je samo Z6
(`#task-balastna-crpka-regulacija-npsh`). Strojarstvo je dobro zastupljeno
(rashladni krugovi P2, P5, Z3; crpke P4, Z4; dimenzioniranje Z5). P3 je
komunalna vodovodna mreža, dakle građevinarstvo. Student brodogradnje u
riješenim primjerima ne nalazi ni jedan brodski sustav.
Prijedlog: Bez dodavanja zadataka promijeniti kontekst jednog riješenog
primjera, uz prilagodbu brojeva, ako autorica proširi opseg revizije na P:
- P3 kao **brodski protupožarni prsten** (cjevovod gašenja morem izveden kao
  petlja s hidrantima). Petlja je ondje stvarna konstrukcijska praksa, a
  Hardy–Crossova logika ostaje ista. Ako se navodi zahtijevani tlak na
  hidrantu, preuzeti ga iz SOLAS II-2, pravilo 10, s izvorom u dodatku E.
  Prema mom sjećanju, za teretne brodove to je reda 0,25–0,27 MPa, ali to
  treba provjeriti u izvorniku.
- ili P6 kao **kaljužna crpka** ili crpka opće službe s usisom iz kaljuže.
  Ondje je usisna visina iznad razine (pozitivan $z_s$) realna, za razliku od
  morskih usisa.
Druga mogućnost: u P5 navesti brodski niskotemperaturni krug centralnog
hlađenja. Tada protok treba povećati na red veličine 30–150 L/s, jer su
morske i slatkovodne rashladne crpke trgovačkih brodova obično reda
100–500 m³/h (iskustvena procjena).

**P2-2. Z6: uronjenost usisa i „balastno stanje” odgovaraju samo malom brodu**
Mjesto: `u13:868`, `u13:874`, skica Z6 (PDF str. 259), `#task-balastna-crpka-regulacija-npsh`.
Opis: Referentni usisni presjek nalazi se 1,8 m, a „u balastnom stanju” samo
0,4 m ispod vodne linije. Balastna crpka trgovačkog broda smještena je
u strojarnici ili crpnoj stanici blizu pokrova dvodna, 1,5–2,5 m iznad
kobilice. Pri gazu u balastu od 4–8 m njezin je usis uronjen najmanje oko
3–5 m (iskustvena procjena za brodove za rasute terete, tankere i kontejnerske
brodove). Vrijednosti 1,8/0,4 m realne su samo za plovilo gaza oko 2–3 m,
npr. tegljač, manji obalni brod ili trajekt. Protok 22 L/s (≈ 80 m³/h) također
odgovara malom brodu. Balastne crpke većih trgovačkih brodova obično su reda
nekoliko stotina do nekoliko tisuća m³/h. Usto, balastiranje se provodi
uglavnom tijekom iskrcaja tereta, kad brod postaje lakši. Najmanja uronjenost
pri radu crpke pojavljuje se zato potkraj iskrcaja ili na početku
balastiranja, a ne u „balastnom stanju” u smislu plovidbe u balastu, kad su
tankovi već puni. Uz to je neobično da se temeljna točka s 1,8 m uronjenosti
odnosi na punjenje balasta, jer krcat brod rijetko balastira.
Prijedlog: U tekstu imenovati vrstu plovila, npr. „manji obalni brod gaza oko
3 m”. Stanje $z_s=-0{,}4$ m preimenovati u „najmanji gaz tijekom
balastiranja, potkraj iskrcaja”. Druga mogućnost je zadržati velik brod i
povećati obje uronjenosti, ali tada NPSH dio gubi napetost.

**P2-3. Z6: stalna statička visina pri punjenju tanka nije ograđena** (K9, K16 — razgraničenje)
Mjesto: `u13:866`, `u13:872–873`.
Opis: $H_s(Q)=4+0{,}015Q^2$ i $H_{s,V}$ imaju stalnih 4 m, a energija se računa
za 1500 h. Pri punjenju tanka statička visina raste s razinom u tanku, a
istodobno raste i gaz broda. Tankovi dvodna ispod vodne linije mogu se
djelomično puniti i gravitacijski. Tekst ne kaže da je riječ o
reprezentativnoj (srednjoj) točki kvazistacionarnog procesa.
Prijedlog: U tekstu zadatka dodati rečenicu: „Statička visina 4 m jest srednja
vrijednost tijekom punjenja; promjenu razine u tanku i gaza zanemari.”
Rezultat se ne mijenja.

**P2-4. Skica Z6: prodor kroz oplatu bez ventila na oplati i bez usisnog sanduka**
Mjesto: `u13:712`, skica `u13_mreze_vjezbe_skice.svg`, panel Z6 (PDF str. 259).
Opis: Usisna cijev izlazi izravno kroz otvor u vanjskoj oplati i bez ikakve
armature vodi do crpke. Pravila klasifikacijskih društava i SOLAS traže da
svaki usis mora ispod vodne linije ima zaporni ventil pričvršćen izravno na
oplatu ili na usisni sanduk. Takav se usis u pravilu izvodi kroz usisni
(morski) sanduk s rešetkom, a ispred crpke slijedi filtar. Tekst već računa
gubitak „koša, filtra i armature” (`u13:868`), ali ga skica ne prikazuje.
Student brodogradnje mogao bi zaključiti da je goli prodor kroz oplatu
prihvatljiv, što je sigurnosno pogrešna slika.
Prijedlog: Bez redizajna, u postojećem stilu, dodati simbol ventila neposredno
uz oplatu i simbol filtra ispred točke S. Po želji oplatu oko ulaza nacrtati
kao udubljeni sanduk. Navesti da skica ne prikazuje propisanu izvedbu.

**P2-5. Nazivlje: „usisni koš u oplati”**
Mjesto: `u13:866`, oznaka „usisni koš” na skici Z6 (PDF str. 259), `u13:712` (fig-alt).
Opis: U brodskom strojarstvu „usisni koš” obično označuje perforiranu košaru
na kraju usisne cijevi u tanku ili kaljuži (engl. *rose box*, *strum box*).
Otvor u vanjskoj oplati s rešetkom jest usisni (morski) sanduk, u praksi
često zvan „kingston” (engl. *sea chest*). Uputa recenzentu navodi „usisni
koš” kao primjer ispravnog naziva, pa je moguće da autorica ovdje svjesno
rabi taj naziv. U kontekstu otvora u oplati ipak se razlikuje od uobičajenog
značenja.
Prijedlog: Provjeriti u hrvatskom brodograđevnom nazivlju (npr. hrvatsko
izdanje pravila HRB-a). U oplati pisati „usisni sanduk (kingston) s
rešetkom”, a „usisni koš” zadržati za usis u tanku ili kaljuži.

**P2-6. P5: učinkovitosti crpke i motora prevelike za agregat od oko 1 kW**
Mjesto: `u13:589`, `#ex-energijski-ledger-hladenja` (PDF str. 256–257).
Opis: Uz $Q=6$ L/s i $H=12$ m vratilna je snaga oko 0,9 kW. Zadani su
$\eta_p=0{,}78$ i $\eta_m=0{,}92$, pa je ukupno 0,70. Vrijednost 0,92 imaju
motori reda 10–20 kW. Prema mom sjećanju tablica IEC 60034-30-1, četveropolni
motor od 1,1 kW u razredu IE3 ima oko 84 %, a u razredu IE4 oko 87 %. Crpka
od približno 22 m³/h i 12 m pri $n_q\approx35$ realno postiže oko 0,60–0,70
(iskustvene krivulje najveće učinkovitosti u ovisnosti o protoku i
specifičnoj brzini vrtnje; vrijednosti nisu provjerene u izvoru tijekom ove
recenzije). Realna ukupna učinkovitost agregata s pretvaračem jest oko
0,50–0,58, a ne 0,70. Lanac snaga i kontrolni omjer ostaju ispravni, ali
student dobiva pogrešan dojam o razini učinkovitosti malih agregata.
Prijedlog: Uzeti $\eta_p\approx0{,}65$ i $\eta_m\approx0{,}85$. Druga je
mogućnost zadržati učinkovitosti i povećati snagu, npr. $Q\approx25$ L/s i
$H\approx20$ m (vratilna snaga oko 6–7 kW), za koju su 0,78 i 0,90–0,92
realni. Izmjena traži ažuriranje ključa i verifikatora.

**P2-7. P6: brzina u usisnom vodu 2,8 m/s bez komentara**
Mjesto: `u13:635`, `u13:646`, `#ex-npsha-usisne-crpke` (PDF str. 257).
Opis: Uz $D=80$ mm i 14 L/s brzina na usisu iznosi 2,79 m/s, uz usisnu
visinu 2,6 m. Uobičajena projektna praksa za usisne vodove jest oko
1–2 m/s, a pri usisu iznad razine bliže donjoj granici. Uobičajena preporuka
iz priručnika za crpke; točan raspon autorica treba preuzeti iz izvora
dodatka E. Primjer bez komentara prikazuje lošu izvedbu kao normalnu, iako je
upravo ona uzrok gubitka $h_{g,s}=1{,}45$ m.
Prijedlog: U „Provjeri i tumačenju” dodati jednu rečenicu, npr. „Brzina
2,8 m/s na usisu je velika; veći usisni promjer povećao bi $NPSH_a$.” Druga
mogućnost: zadržati brojeve kao namjerno lošu izvedbu i to izrijekom reći.

**P2-8. NPSH_r: kriterij i margina bez izvora i bez standardne definicije** (K9, K14)
Mjesto: `u13:357`, `u13:885` (kontrolni rezultat Z6), PDF str. 253 i 261.
Opis: Tekst kaže da proizvođač određuje $NPSH_r$ „prema kriteriju koji sam
navodi”. U praksi se objavljuje $NPSH_3$ prema ISO 9906 ili ANSI/HI 14.6, tj.
pri padu visine dobave od 3 %. To znači da pri $NPSH_a=NPSH_r$ kavitacija već
postoji. Taj je podatak primjenski najvažniji argument za marginu. Margina
je spomenuta, ali bez izvora i bez reda veličine. Prema mom sjećanju,
ANSI/HI 9.6.1 navodi omjere $NPSH_a/NPSH_3$ od oko 1,1 do 2,5, ovisno o
primjeni; treba provjeriti.
Prijedlog: Dodati rečenicu o kriteriju 3 % s izvorom iz dodatka E i
navesti red veličine margine kao orijentaciju s ogradom.

**P2-9. Empirijske korelacije i tvrdnja o praksi bez izvora** (K14)
Mjesto: `u13:185–192` (Swamee–Jain, Blasius, „odstupa za oko 1 %”);
`u13:525` („Brzine 0,74–1,19 m/s uobičajene su za distribucijske vodove”).
Opis: Colebrook i Moody citirani su (`u13:99`, `u13:164`), a Swamee–Jainova
i Blasiusova korelacija nisu, kao ni tvrdnja o točnosti od 1 %. Tvrdnja o
uobičajenim brzinama u distribucijskim vodovima tvrdnja je o praksi. Raspon
je realan, jer projektne brzine distribucijskih mreža obično iznose oko
0,5–1,5 m/s, ali nema izvora ni oznake nastavne procjene.
Prijedlog: Dodati izvore iz dodatka E, npr. Swamee i Jain 1976. te White
ili Çengel za Blasiusa. Za brzine dodati izvor ili oznaku nastavne procjene.

**P2-10. Nazivlje: „učinkovitost” umjesto „stupanj djelovanja” i kolebanje naziva**
Mjesto: `u13:311`, `u13:317`, `u13:589`, `u13:809`, `u13:866`; `u13:779` i `u13:775`; `u13:635`, `u13:630`.
Opis:
- Za $\eta$ crpke, motora i pretvarača hrvatska strojarska literatura
  ustaljeno piše „stupanj djelovanja” ili „stupanj korisnosti”.
  „Učinkovitost” je općenitija riječ (energetska učinkovitost). Ako je knjiga
  drugdje dosljedno odabrala „učinkovitost”, nalaz se svodi na P3, uz
  napomenu u pojmovniku.
- „ogranak” i „grana” kolebaju unutar Z3: naslov i tekst „Dva rashladna
  ogranka”, skica „Uravnoteženje dvaju ogranaka”, a traži se „u koju granu”.
- P6 „servisna crpka” anglizam je od *general service pump*. Hrvatski je
  „crpka opće službe”, ili jednostavno „crpka”, jer kontekst nije brodski.
Prijedlog: Odabrati jedan naziv po pojmu i uskladiti ga, zajedno s
naslovima skica (vidi P3-9).

### P3

**P3-1. P3: „lijevano željezo” i Hardy–Cross bez veze s današnjom praksom** (suvremenost)
Mjesto: `u13:473`, `u13:244–250`, `#ex-petlja-gradske-mreze` (PDF str. 254–256).
Opis: Nove vodovodne mreže grade se od duktilnog lijeva s cementnom oblogom
ili od PE-a i PVC-a. Sivi lijev pripada starim mrežama. $\lambda=0{,}022$
odgovara upravo staroj, inkrustiranoj cijevi, pa je broj dosljedan. Današnji
programi za mreže (npr. EPANET) rješavaju sve petlje istodobno globalnom
gradijentnom metodom (Todini–Pilati), a Hardy–Cross ostaje nastavni postupak.
Prijedlog: Napisati „stara mreža od lijevanog željeza” i u `u13:242` ili
`u13:250` dodati rečenicu da se u praksi sve petlje rješavaju istodobno
Newtonovim postupkom. Vidi i P2-1 (brodski protupožarni prsten).

**P3-2. Suvremenost: neiskorištene veze s dekarbonizacijom pomorstva i obradom balastnih voda**
Mjesto: P5 (`u13:584`), Z6 (`u13:862–874`), CFD `u13:111–116`.
Opis: Poglavlje dobro uvodi frekvencijsku regulaciju i energijsku bilancu.
Izostaju dvije današnje brodske teme:
- pretvarači na morskim rashladnim crpkama kao tipična mjera za EEXI i CII;
- sustavi obrade balastnih voda prema Konvenciji o upravljanju balastnim
  vodama (IMO). Njihov filtar i UV ili elektrolitička jedinica dodaju znatan
  pad tlaka i nameću raspon protoka, što izravno pomiče radnu točku iz Z6.
Hladna ploča u CFD odlomku dobra je veza s elektrifikacijom, ali P2
(„rashladni modul”) tu vezu ne imenuje.
Prijedlog: U Z6 dodati jednu rečenicu konteksta ili jedan od nedostajućih
podataka u kontrolnom rezultatu, npr. pad tlaka sustava obrade balastnih
voda. P2 nazvati npr. „vod hladne ploče baterijskog modula”. Za P5 vidi P2-1.

**P3-3. Z5: kriterij „najmanji promjer” bez provjere brzine i troška**
Mjesto: `u13:838–843`, `#task-robustan-izbor-promjera` (PDF str. 260–261).
Opis: Brzine iznose 3,6 m/s za 80 mm, 2,3 m/s za 100 mm i 1,5 m/s za
125 mm. Odabrani promjer od 100 mm troši 10,8 m na 150 m. U praksi se
promjer bira i prema dopuštenoj brzini (buka, erozija, vodeni udar) te
prema trošku životnog vijeka, a ne samo kao najmanji koji zadovoljava gubitak.
`u13:109` upravo naglašava da je promjer najjača poluga.
Prijedlog: U točki 2 dodati: „Komentiraj bi li zbog brzine ili troška
energije izabrao veći promjer.” Razina i opseg ostaju isti.

**P3-4. Z3: energija prigušena na ventilu za uravnoteženje**
Mjesto: `u13:779–784`, `#task-uravnotezenje-paralelnih-grana`.
Opis: Ventil troši 3,6 m od 4,8 m, odnosno oko 0,35 kW hidrauličke snage
trajno. To je realna i poučna posljedica uravnoteženja prigušivanjem, a ostaje
neizrečena. Hrvatski je stručni naziv „ventil za hidrauličko uravnoteženje”
(balansirni ventil).
Prijedlog: Jednu riječ dodati u naslov ili tekst. Po želji u naputku
uputiti na vezu s lancem snaga iz `#sec-ledger-snage`.

**P3-5. Z2: kontekst „dva fluida u istom vodu” i režim vode na granici prijelaza**
Mjesto: `u13:751`, `u13:761`, `u13:767`.
Opis: Naizmjenični protok dvaju fluida bez konteksta djeluje nategnuto.
Realan kontekst postoji: krug se ispire vodom, a zatim puni glikolnom
smjesom. $Re_B\approx4800$ blizu je praga 4000, pa je u cijevi od 8 mm
režim vode u praksi mogao biti prijelazni. Rezultat $\Delta p_B$ zato je
orijentacijski (K9).
Prijedlog: Dodati kontekst ispiranja i punjenja te u kontrolnom rezultatu
ogradu „uz pretpostavku razvijenog turbulentnog toka”.

**P3-6. Z1: nejasan izvor ograničenja pada tlaka**
Mjesto: `u13:724`.
Opis: „Mjerni pretvornici dopuštaju najveći pad tlaka” može se čitati kao
granica oštećenja osjetnika. U praksi se mjerno područje diferencijalnog
pretvornika bira prema protoku, a ne obrnuto.
Prijedlog: Napisati „mjerno područje diferencijalnog pretvornika tlaka
iznosi do 25,0 kPa” ili ograničenje vezati uz raspoloživu visinu crpke.

**P3-7. P5: nije rečeno kako se protok zadržava nakon čišćenja**
Mjesto: `u13:589`, `u13:627`.
Opis: Uz stalnu brzinu vrtnje čišćenje izmjenjivača povećalo bi protok, a ne
zadržalo ga. Ograda „uz isti protok” postoji, ali mehanizam (pretvarač
smanjuje brzinu vrtnje) nije izrečen.
Prijedlog: Dodati „pretvarač zadržava protok smanjenjem brzine vrtnje”.
Tako se primjer povezuje s P4.

**P3-8. Z6: „njihanje” i „napunjen usis”**
Mjesto: `u13:868`, `u13:885`, naslov skice Z6.
Opis: Za gibanja broda uobičajeni su nazivi ljuljanje, posrtanje i poniranje.
„Njihanje” je neodređeno. Za *flooded suction* u literaturi o crpkama češće
se susreću „usis s dotokom”, „crpka u dotoku” ili „potopljen usis”. Taj
izraz treba provjeriti.
Prijedlog: „pri ljuljanju, posrtanju i trimu”; za „napunjen usis” odabrati
naziv i rabiti ga dosljedno.

**P3-9. Naslovi panela skice 13.4 razlikuju se od naslova zadataka**
Mjesto: `u13:712`, PDF str. 258–259.
Opis: Panel Z2 nosi naslov „Isti vod, dva fluida”, a zadatak „… i dva
režima”. Panel Z3 nosi naslov „Uravnoteženje dvaju ogranaka”, a zadatak
„Uravnoteženje paralelnih grana”. Panel Z4 nosi naslov „Radna točka uz
promjenjivo trenje”, a zadatak „Radna točka hrapavog voda”. Panel Z6 nosi
naslov „Balastna crpka: napunjen usis”, a zadatak „Regulacija balastne crpke
i usisna rezerva”.
Prijedlog: Uskladiti naslove panela sa naslovima zadataka ili ih
skratiti na zajednički oblik.

**P3-10. Uvod obećava grijanje i protupožarnu zaštitu bez primjera**
Mjesto: `u13:7` (PDF str. 245).
Opis: Ni jedan primjer ni zadatak ne odnosi se na grijanje ni na
protupožarnu zaštitu.
Prijedlog: Rečenicu svesti na sustave koji se pojavljuju ili ih uvesti
promjenom konteksta prema P2-1.

**P3-11. CFD odlomak o kavitaciji: „U istom rashladnom krugu” bez jasnog referenta**
Mjesto: `u13:368` (PDF str. 253).
Opis: Nije jasno koji je krug „isti”: P5, prethodni CFD odlomak s
razdjelnikom ili Z6. Odlomak inače korektno razgraničuje jednofazni i
višefazni račun i ne iznosi neprovedene rezultate (K9 zadovoljen).
Prijedlog: Napisati „u rashladnom krugu s razdjelnikom iz prethodnog
odlomka”.

**P3-12. Sitnice u tekstu i skici 13.2**
Mjesto: `u13:109`; skica 13.2 (`u13:65`, PDF str. 247).
Opis:
- Izraz „nekoliko milimetara promjera” zanemaruje da se cijevi biraju po
  nazivnim promjerima (DN). Korak DN80 → DN100 iznosi 20 mm, a ne nekoliko
  milimetara.
- Na skici 13.2 simbol ventila stoji iznad cijevi i ne dodiruje je, iako je
  označen kao simbol.
Prijedlog: Napisati „jedan korak nazivnog promjera”. Simbol ventila
spustiti na os cijevi, bez promjene stila.

## Posebno dobre primjene

- **Z6, balastna crpka** (`#task-balastna-crpka-regulacija-npsh`). Zadatak
  povezuje regulaciju prigušivanjem i brzinom vrtnje, godišnju energiju,
  NPSH s apsolutnim tlakom i dva stanja broda. Kontrolni rezultat traži
  popis nedostajućih podataka: marginu, $NPSH_r$ pri sniženoj brzini,
  zaprljanje filtra i uvlačenje zraka. To je upravo inženjerska prosudba
  koju praksa traži. Tlak pare morske vode pri 30 °C (4,2 kPa) i $NPSH_r$
  od oko 4,5 m realni su.
- **P4, afinitetni zakoni i statička visina** (`#ex-radna-tocka-vfd`). Primjer
  pogađa najčešću pogrešku u praksi regulacije crpki: omjer brzina 0,899
  prema omjeru protoka 0,865.
- **Granica modela i odlomak o NPSH-u** (`u13:357–363`) te samoprovjera 4.
  Jasno je da $NPSH_a$ nije potvrda sigurnosti; razgraničenje je primjerno.
- **Z5, starenje cijevi**. Rezerva od samo 1 m nakon porasta $k_s$ realna je
  i važna projektna pouka.
- **Z4 s rezidualima**. Zahtjev za energijskim i Colebrookovim rezidualom
  odražava današnju praksu provjere numeričkog rješenja. Podatci (brzina
  2,4 m/s, $k_s=0{,}1$ mm, $\eta_p=0{,}76$ pri oko 4,7 kW) realni su.
- **Prvi CFD odlomak** (`u13:111–116`). Izvođenje $\xi$ za novi razdjelnik iz
  razlike tokova mehaničke energije, uz navedenu referentnu brzinu, jest
  ispravan i suvremen postupak, primjenjiv na hladne ploče.
- **Lanac snaga** (`u13:303–335`). Odvajanje hidrauličke, vratilne i
  električne snage te upozorenje da se disipacija na ventilu ne oduzima od
  električne snage korisna je inženjerska navika.

## Ograničenja ove recenzije

Pročitano je samo poglavlje 13. Ravnoteža struka procijenjena je unutar
poglavlja, ne za cijelu knjigu. Kurikularna matrica, dodatak E i ostala
poglavlja nisu čitani. Rasponi označeni kao „prema sjećanju” ili
„iskustvena procjena” (IEC 60034-30-1, ANSI/HI 9.6.1, SOLAS II-2/10, tipični
gazovi i kapaciteti balastnih crpki, učinkovitosti malih crpki) nisu
provjereni u izvorniku tijekom ove recenzije. Prije unosa u tekst treba ih
potvrditi.
