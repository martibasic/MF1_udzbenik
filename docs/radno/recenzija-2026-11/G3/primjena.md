# Primjenska recenzija, skupina G3 (poglavlja 9–12)

Recenzent: neovisni primjenski recenzent (brodogradnja i strojarstvo), 8. 11. 2026.
Materijal: PDF G3 (knjiga str. 169–244) i izvori `source/u09_*.md` … `source/u12_*.md`.
Uputa: `.claude/skills/recenzija-prirucnika/references/primjena.md`. Pravila: K9, K14 i K16 te ljestvica P0–P3 iz `docs/konvencije_pisanja.md`.
Oznake P1…P7 i Z1…Z6 slijede prikaz u PDF-u. Uz njih je naveden stabilni ID. Retci se odnose na izvor `source/uNN_*.md`.

Nisam pretraživao web niti otvarao vanjske izvore. Raspone koji nisu zadani u tekstu ili u literaturi knjige naveo sam po sjećanju iz inženjerske prakse i tako sam ih označio (**po sjećanju**). Te vrijednosti treba provjeriti u izvoru iz dodatka E prije nego što se unesu u tekst.

## Sažetak

Primjene u poglavljima 9–12 većinom su vjerodostojne i pošteno razgraničene od konstrukcijske ili sigurnosne ocjene. Lanac vučni bazen, ITTC 1957 i granični sloj trupa modela (pog. 11 i 12) te vodomlazni pogon i aktuatorski disk (pog. 10) posebno su dobri. Nema nalaza P0 ni P1. Glavni nedostatci su prikaz stroja za pranje tanka, koji ne odgovara brodskoj praksi, i debljina uljnog filma uz spomen ležaja. Uz to, strojarske primjene u poglavljima 9 i 12 izrazito prevladavaju, a cijeloj skupini nedostaju offshore primjene i primjene vezane uz dekarbonizaciju.

## Nalazi P0

Nema.

## Nalazi P1

Nema.

## Nalazi P2

### P2-1. Stroj za pranje teretnog tanka ne odgovara brodskoj izvedbi

- **Mjesto:** str. 199–200, pog. 10, P7, `ex-rotirajuca-mlaznica-pranje-tanka` (u10, r. 792–858). Povezani CFD odlomak „Zakretni moment raspršivača” (r. 210–215).
- **Opis:** Tekst opisuje „stroj za pranje teretnog tanka” s dvjema tangencijalnim reakcijskim mlaznicama, brzinom vrtnje $n=60\ \text{min}^{-1}$ koju koči reduktor i mlazom $w=17{,}8\ \text{m/s}$. Iz te brzine slijedi dobavni tlak od samo oko 1,6 bar. Fiksni i prijenosni strojevi za pranje tankova tankera rade drukčije (**po sjećanju**). Dobavni tlak im je reda 8–12 bar, a mlaz izlazi brzinom reda 35–45 m/s. Mlaznice su usmjerene prema stijenci, a ne tangencijalno u ravnini vrtnje. Glavu pokreće unutarnja turbinica preko reduktora, a mlaznice se okreću vrlo sporo, reda nekoliko $\text{min}^{-1}$, jer učinak pranja ovisi o vremenu udara mlaza. Reakcijski pogon s brzinom reda desetaka do stotina $\text{min}^{-1}$ tipičan je za vrtne raspršivače i niskotlačne procesne kugle za ispiranje, a ne za pranje teretnih tankova. Fizika primjera je točna, ali student brodogradnje dobiva pogrešnu predodžbu o uređaju (K16).
- **Prijedlog:** Lakše je promijeniti naziv nego podatke. Naziv bi mogao biti „Reakcijska glava za ispiranje spremnika” ili „Rotacijski raspršivač”. Tada bi samo provjera i tumačenje mogli dodati jednu rečenicu: brodski strojevi za pranje tankova rade pri većem tlaku i vrte se sporo jer ih pogoni turbinica preko reduktora. Ako brodski kontekst treba ostati, zadrži $d$ i $r$, a povećaj $w$ na oko 35–40 m/s, primjerice s $Q\approx5{,}5$–$6{,}3\ \text{L/s}$. Tumačenje tada treba reći da je realna vrtnja spora, pa je moment blizu momenta zadržane glave. Dio s $u\ne0$ zadržao bi se kao granična analiza.

### P2-2. Uvod poglavlja 10 najavljuje primjene iz strojarnice koje primjeri ne daju

- **Mjesto:** str. 183, uvod pog. 10 (u10, r. 7): „Primjene su koljena i račve u brodskim strojarnicama …”. Povezani su P3 `ex-u11-servisno-koljeno-na-sidrenom-nosacu-t2`, P4 `ex-u11-t-racva-na-sidrenoj-konzoli-t3`, P5 `ex-u11-y-racva-s-mjerenom-reakcijom-konzole-t4`, Z3 `task-koljeno-u-okomitoj-ravnini-tezina` i Z6 `task-u11-vodoravna-y-racva-prima-vodu-kroz-ulaz`.
- **Opis:** Nijedan primjer ni zadatak s koljenom ili račvom nije smješten u strojarnicu. Svi računaju sa slatkom vodom ($\rho=998$) i bez brodskog konteksta. Jedini „rashladni vod” javlja se u CFD odlomku. Uvod tako obećava više nego što poglavlje daje (K16).
- **Prijedlog:** Jedan postojeći primjer neka dobije brodski smještaj bez promjene računa. P3 može postati koljeno voda rashladne morske vode iza usisnog koša, uz $\rho_{mv}=1025\ \text{kg/m}^3$ ako se računa nanovo. Z3 može postati koljeno tlačnog voda balastne ili protupožarne crpke. Druga je mogućnost da uvod umjesto toga kaže „cijevni elementi brodskih i kopnenih sustava”.

### P2-3. Uljni film od 1 mm uz spomen nosivosti ležaja

- **Mjesto:** str. 232, pog. 12, P2, `ex-uljni-film` (u12, r. 158–179). Uvod pog. 12 (r. 7) navodi „uljni film kliznog ležaja”.
- **Opis:** $H=1{,}0\ \text{mm}$ i $dp/dx=-100\ \text{kPa/m}$ nisu vjerodostojni za nosivi uljni film kliznog ležaja. Debljina nosivog filma reda je 10–100 µm, a gradijent tlaka u nosivom dijelu reda je $10^7$–$10^9\ \text{Pa/m}$ (**po sjećanju**). Procjep od 1 mm reda je veličine dijametralne zračnosti velikog ležaja, na primjer ležaja statvene cijevi, a ne debljine filma pod opterećenjem. Rečenica o „nosivosti ležaja” čitatelja upućuje upravo na ležaj (K16).
- **Prijedlog:** Uzmi $H=50\ \mu\text{m}$ i $dp/dx=-40\ \text{MPa/m}$, uz iste $\mu=0{,}10\ \text{Pa s}$ i $u=2{,}0\ \text{m/s}$. Tada ostaje isti rezultat $v(H/2)=1{,}0+0{,}125=1{,}125\ \text{m/s}$, pa skica i ključ ne trebaju nove brojke. Promijenili bi se samo ulazni podatci i verifikator. Druga je mogućnost zadržati podatke i izbaciti riječ „ležaj”, pa primjer nazvati „Ulje u procjepu …”. Isto vrijedi i za Z4 `task-couette-povrat` (r. 619–649). Uz $H=50\ \mu\text{m}$ kritični gradijent iznosi $1{,}6\cdot10^8\ \text{Pa/m}$, što je realno za ležaj.

### P2-4. Brzine na „usisu crpke” prevelike za usisni vod

- **Mjesto:** str. 224, pog. 11, Z3, `task-u14-na-referentnom-presjeku-usisa-crpke-apsolutni-tlak` (u11, r. 822–852).
- **Opis:** Na „referentnom presjeku usisa crpke” zadane su brzine 4 i 8 m/s. U usisnom vodu i na usisnoj prirubnici brzine se obično drže oko 1–3 m/s upravo zbog kavitacijske rezerve (**po sjećanju**), pa je 8 m/s nevjerodostojno za taj presjek. Kriterij $\sigma_{kr}=3{,}0$ ispravno je označen kao nastavni model, pa nalaz ne dira razgraničenje, nego samo radnu točku (K16).
- **Prijedlog:** Referentni presjek neka bude ulaz u radno kolo (oko rotora), gdje su brzine od nekoliko m/s realne. Tada podatci i ključ ostaju isti. Dovoljna je i rečenica da se brzina odnosi na suženi ulaz u radno kolo, a ne na usisni vod.

### P2-5. Ravnoteža struka i suvremenost u skupini

- **Mjesto:** pog. 9–12 u cjelini.
- **Opis:** Po poglavljima, prema mojem razvrstavanju 51 primjera i zadatka, slika je sljedeća:
  - **Pog. 9:** brodogradnji izričito pripada samo Z2 (zrak za upućivanje). P2 s turbopuhalom „pomoćnog dizelskog motora” nema brodski smještaj. Ostalo su strojarstvo, laboratorij i aeronautika (P3, Pitotova sonda pri 55 kPa i 260 K, što odgovara letu na visini).
  - **Pog. 10:** uravnoteženo. Brodogradnji pripadaju P7, Z1 i Z2, strojarstvu i energetici P1, P6 i cijevni elementi.
  - **Pog. 11:** brodogradnji pripadaju P2, CFD odlomak s pontonom, Z1 i Z4. Strojarstvu pripadaju P1, P3–P6 i Z3. Primjera iz građevinarstva ima više nego u drugim poglavljima: Z2 (Manningova jednadžba), Z6 (preljev brane, jedini T4) i P6 (dimnjak).
  - **Pog. 12:** brodogradnji pripada samo P4 (granični sloj trupa modela). Nijedan od zadataka Z1–Z6 nije pomorski.

  Offshore konstrukcije i offshore vjetar ne pojavljuju se nigdje u skupini. Dekarbonizaciju pomorstva (LNG, vodik, amonijak, ispiranje ispušnih plinova) ne spominje nijedan primjer. Suvremenu praksu predstavlja samo hladna ploča baterije u CFD odlomcima pog. 9 i 12, a ona pripada elektrifikaciji (K16, uputa, točke 3 i 4).
- **Prijedlog:** Novi zadatci nisu potrebni. Dovoljne su zamjene konteksta uz iste ili slične brojke (banka ideja, ne obveza):
  - pog. 9, P2: „turbopuhalo brodskog generatorskog motora”, a provjera neka se odnosi na ulaz u kolo kompresora, gdje lokalni $Ma$ doista prelazi 0,3 (vidi P3-2);
  - pog. 9, Z1: helij kao plin za ispitivanje nepropusnosti hladne ploče ili spremnika (vidi P3-3);
  - pog. 11, P6: umjesto dimnjaka monopilot ili toranj vjetroagregata tijekom offshore montaže, ili brodski jarbol odnosno dimnjak;
  - pog. 11, Z6 (T4): isti postupak s dvama mjerilima modela broda i korekcijom ITTC 1957 umjesto preljeva; Manningova jednadžba može ostati jedini građevinski primjer;
  - pog. 12, Z2: cijev rashladne morske vode;
  - pog. 12, Z4: ležaj statvene cijevi uz realan $H$ (vidi P2-3);
  - pog. 12, Z5: pramčani dio trupa modela ili kormilo.

  Pregledom je potrebno samo provjeriti da razine T1–T4 ostaju iste.

## Nalazi P3

### P3-1. Zrak za upućivanje: nazivlje i propisni kontekst

- **Mjesto:** str. 179, pog. 9, Z2, `task-zrak-za-upucivanje-motora` (u09, r. 540–567).
- **Opis:** Podatci su vjerodostojni za manji pomoćni ili srednjohodni motor: 30 bar(abs), oko 2,5 kg po upućivanju i trajanje reda 3 s. U hrvatskoj brodostrojarskoj literaturi uvriježeni su nazivi „uputni zrak” i „boca (spremnik) uputnog zraka” (**po sjećanju**). Tekst piše „zrak za upućivanje” i „boca stlačenog zraka”. To je razumljivo, ali nije strukovno ustaljeno. Broj uzastopnih upućivanja koji spremnici moraju osigurati propisuju pravila klasifikacijskih društava (**po sjećanju**: 12 za prekretni, 6 za neprekretni motor). Zadatak ne tvrdi ništa o tome, pa razgraničenje nije narušeno.
- **Prijedlog:** Pri prvom spomenu napiši „uputni zrak (zrak za upućivanje)”. Navedi da je motor „pomoćni (generatorski)”. U naputku ili tumačenju dodaj ogradu: „broj upućivanja koji spremnik mora osigurati propisuju pravila klasifikacijskog društva”. Ako autorica želi zadržati postojeći naziv, ovo je samo napomena.

### P3-2. Usis turbopuhala i zračni vod ponavljaju istu umjetnu geometriju

- **Mjesto:** str. 171, pog. 9, P2, `ex-odabir-modela-kompresibilnosti` (u09, r. 108–133). Str. 222, pog. 11, P6, `ex-u14-machov-i-strouhalov-broj-stlacivost-i-vrtlozno` (u11, r. 661–711).
- **Opis:** Oba primjera uzimaju vod $D=80\ \text{mm}$ s protokom oko 0,4 m³/s. Tekst pog. 9 pošteno kaže da je vod „namjerno uzak”. Primjena je ipak nategnuta jer lokalni $Ma>0{,}3$ u turbopuhalu doista nastaje na ulazu u kolo kompresora (inducer), a ne u usisnom vodu. Ponavljanje iste brojke u pog. 11 ne donosi novu primjenu.
- **Prijedlog:** U pog. 9 premjesti odluku na ulaz u kolo kompresora (prstenasti presjek), gdje je visoka brzina realna, pa ograda o uskom vodu više ne treba. U pog. 11 može ostati generički vod ili ventilator. Druga je mogućnost odvojak ispuha pneumatskog alata s drukčijim promjerom.

### P3-3. Veza CFD odlomka pog. 9 s lajtmotivom hladne ploče je slaba

- **Mjesto:** str. 172, pog. 9, CFD „Zračna sapnica za čišćenje hladne ploče” (u09, r. 135–140).
- **Opis:** Čišćenje hladne ploče mlazom zraka nategnuta je poveznica s lajtmotivom tekućinskog hlađenja. Rečenica „za razliku od ranije obrađenoga kruga s kapljevinom” ne kaže iz kojeg poglavlja dolazi krug ni što se iz njega zadržava (K16, lajtmotiv).
- **Prijedlog:** Stvarna praksa s istom fizikom jest ispitivanje nepropusnosti hladne ploče ili baterijskog modula stlačenim zrakom ili helijem. Istjecanje kroz mikropropuštanje tada je zagušeno, pa vrijedi upravo jednadžba za zagušeni protok. Navedi poglavlje kruga i koja fizika ulazi (stlačivost, energija).

### P3-4. Sigurnosni otvor: norma bi pomogla studentu

- **Mjesto:** str. 174, pog. 9, P4, `ex-priguseni-ventil` (u09, r. 271–299).
- **Opis:** Razgraničenje je dobro, jer tekst izrijekom kaže „ne zamjenjuje sigurnosnu certifikaciju”. Student ipak ne saznaje gdje se nalazi normirani postupak.
- **Prijedlog:** Ako je u dodatku E, uputi na normu za dimenzioniranje sigurnosnih ventila. Po sjećanju to su niz ISO 4126 i API 520, oba bez provjere izdanja. Ako normu nije moguće navesti uz potpun zapis, ostavi postojeći tekst (K14).

### P3-5. Tvrdnje o uobičajenoj praksi bez izvora ili ograde

Ovo su sitni nalazi po K14 i K9. U svakom je slučaju dovoljno dodati „orijentacijski”, „nastavna procjena” ili navesti izvor:

- **pog. 9, P2 (u09, r. 132):** „u ventilacijskim vodovima (10–20 m/s)”. Po sjećanju niskobrzinski sustavi rade s 3–10 m/s, a visokobrzinski do oko 20–25 m/s;
- **pog. 10, P3 (u10, r. 452):** „$\xi\approx0{,}34$ … uobičajeno za koljeno sa suženjem”;
- **pog. 12, P4 (u12, r. 304):** „$x_1=0{,}05L_m$ … gdje se obično ugrađuje stimulator turbulencije”. Po sjećanju je to u skladu s preporučenim postupcima ITTC-a, pa bi izvor bio [@ittc];
- **pog. 12, P5 (u12, r. 403):** „uobičajenu duljinsku skalu $\ell\approx0{,}07D$”. Tumačenje to već zove „dogovornom skalom”, što je dovoljno ako se riječ „uobičajena” poveže s izvorom.

### P3-6. CFD odlomak pog. 10 iznosi neprovedenu usporedbu kao rezultat

- **Mjesto:** str. 186, pog. 10, CFD „Koljeno rashladnog voda i njegov nosač” (u10, r. 95).
- **Opis:** Rečenica „Usporedba oštrog i blažeg koljena pri istom dotoku pokazuje da manji gubitak ne jamči …” zvuči kao rezultat provedene simulacije (K9).
- **Prijedlog:** Napiši „Usporedba … može pokazati …” ili „Bilanca količine gibanja pokazuje …”. Zaključak slijedi i iz same bilance, jer manji gubitak znači viši izlazni tlak i time veću tlačnu silu na izlaznom presjeku.

### P3-7. Sidrenje tlačnog voda: mjerodavni tlak

- **Mjesto:** str. 198, pog. 10, P6, `ex-u11-sila-na-koljeno-tlacnog-voda-male-hidroelektrane` (u10, r. 715–790).
- **Opis:** Tumačenje ispravno kaže da tlačni dio prevladava. U praksi se sidreni blok tlačnog voda ne dimenzionira za pogonski tlak, nego za najveći tlak koji uključuje vodeni udar ili ispitni tlak (**po sjećanju**). Granica modela pog. 10 spominje vodeni udar, ali ne uz ovaj primjer.
- **Prijedlog:** Dodaj jednu rečenicu: „za sidreni blok mjerodavan je najveći tlak uključujući vodeni udar, što ovaj stacionarni račun ne daje.”

### P3-8. Nazivlje: sapnica i mlaznica, „servisno koljeno”

- **Mjesto:** pog. 10. Kalibracijska „mlaznica” u P2 (r. 297–372) jest konvergentni element koji daje slobodni vodeni mlaz. Isti element u Z5 (r. 1029) i u Peltonovu primjeru (r. 233) zove se „sapnica”. Pog. 9 dosljedno piše „sapnica”. Naslov P3 glasi „Servisno koljeno na sidrenom nosaču” (r. 374).
- **Opis:** Ista vrsta elementa u istom poglavlju nosi dva naziva. „Servisno koljeno” nije ustaljen strukovni naziv i ništa ne govori o uređaju.
- **Prijedlog:** Za konvergentni element koji tvori mlaz piši dosljedno „sapnica”, a „mlaznica” zadrži za rotirajuću glavu i raspršivač ili obrnuto, uz jednu odluku za cijelu knjigu. „Servisno koljeno” zamijeni opisnim nazivom, na primjer „Koljeno sa suženjem na sidrenom nosaču”. Odluka o nazivlju pripada autorici.

### P3-9. Modelska ispitivanja: voda modela i broda

- **Mjesto:** str. 217, pog. 11, P2, `ex-u14-froudeova-slicnost-model-broda-u-vucnom-bazenu` (u11, r. 427). Str. 235, pog. 12, P4, `ex-granicni-sloj-trupa-modela`.
- **Opis:** Za model i brod uzet je isti $\nu=1{,}0\cdot10^{-6}\ \text{m}^2/\text{s}$. U praksi se model računa sa slatkom vodom bazena pri izmjerenoj temperaturi. Brod se računa s morskom vodom pri 15 °C, a $\nu\approx1{,}19\cdot10^{-6}\ \text{m}^2/\text{s}$ i $\rho_{mv}\approx1025\ \text{kg/m}^3$ (**po sjećanju**, ITTC). Pojednostavljenje ne mijenja poruku primjera.
- **Prijedlog:** Dodaj jednu rečenicu ograde u tekstu zadatka ili tumačenju: „radi jednostavnosti uzet je isti $\nu$; u praksi se brod računa s morskom vodom pri 15 °C.” Brojke se ne moraju mijenjati.

### P3-10. Uvodna slika pog. 11: automobil pri $Re_m=Re_p$

- **Mjesto:** str. 207, `fig-uvod-u14` (u11, r. 9–11).
- **Opis:** Umanjeni model automobila pri jednakom $Re$ u zraku tražio bi višestruko veću brzinu i ulazak u stlačivo područje. Automobilska praksa zato koristi tunele u mjerilu 1 : 1 ili modele velikog mjerila, oslanja se na slabu ovisnost $C_D$ o $Re$ i koristi pomični pod (**po sjećanju**). Slika tako implicitno prikazuje uvjet koji se u praksi rijetko ostvaruje.
- **Prijedlog:** U potpis ili rečenicu uz sliku dodaj ogradu da je $Re_m=Re_p$ idealizirani cilj. Druga je mogućnost da uvodna slika bude model broda u vučnom bazenu, koji je ionako prva rečenica poglavlja.

### P3-11. Dimnjak: Strouhalov broj u nadkritičnom području

- **Mjesto:** str. 222, pog. 11, P6 (u11, r. 668–710).
- **Opis:** Pri $v=12\ \text{m/s}$ i $D=2\ \text{m}$ dobiva se $Re\approx1{,}6\cdot10^6$, a pri $6\ \text{m/s}$ oko $8\cdot10^5$, dakle kritično do nadkritično područje kružnog cilindra. Ondje otpuštanje vrtloga nije pravilno, a norme za vjetrom pobuđene vibracije uzimaju posebnu vrijednost $St$ (**po sjećanju**: EN 1991-1-4 navodi $St\approx0{,}18$ za kružni presjek). Tekst ima ogradu „$St\approx0{,}2$” i uputu na aeroelastičnu provjeru, pa je razgraničenje dobro.
- **Prijedlog:** Dodaj kratku napomenu da je pri ovom $Re$ vrijednost $St$ podatak norme ili mjerenja, a ne vrijednost iz subkritičnog područja. Pri zamjeni konteksta vidi P2-5.

### P3-12. Hidroprofil u Z4 bez primjene

- **Mjesto:** str. 224, pog. 11, Z4, `task-reynoldsova-slicnost-hidroprofila` (u11, r. 856–887).
- **Opis:** Podatci su vjerodostojni: $Re=3\cdot10^5$, $C_D\approx0{,}017$ pri nultom napadnom kutu, a model u zraku pri $Ma=0{,}13$. Zadatak ipak ne kaže o kojem je uređaju riječ.
- **Prijedlog:** Jedna riječ konteksta, na primjer „peraja stabilizatora ljuljanja”, „kormilo manjeg plovila” ili „lopatica plimne turbine”, odmah bi pripadala brodogradnji ili offshore energetici. Brojke ne treba mijenjati.

## Posebno dobre primjene

- **Pog. 11, P2 → pog. 12, P4** (`ex-u14-froudeova-slicnost-model-broda-u-vucnom-bazenu` → `ex-granicni-sloj-trupa-modela`): lanac je realan i dobro postavljen. Brod je dug 150 m, plovi brzinom 9 m/s i ima $Fr=0{,}235$, a model u mjerilu 1 : 25 dug je 6 m. Lanac obuhvaća ITTC 1957, objašnjava zašto se otpor ne smije pomnožiti s $\lambda_L^3$ i zašto se ugrađuje stimulator turbulencije. Granica modela poštenim jezikom spominje ITTC 1978 i faktor oblika.
- **Pog. 10, Z1 i Z2** (`task-vodomlazni-potisak-broda`, `task-propeler-aktuatorski-disk`): vodomlazni pogon pri 35 čvorova ima realan omjer $v_j/v_s\approx1{,}8$ i idealnu učinkovitost 0,72. Propeler $D=4$ m ima koeficijent opterećenja potiskom oko 0,8, što je realno za trgovački brod.
- **Pog. 10, P5 i Z6** (Y-račva): „zadani statički kriterij” i faktor 1,15 jasno su označeni kao nastavni. Tekst izrijekom kaže da čvrstoća, zamor i prolazna opterećenja nisu provjereni. To je uzor razgraničenja.
- **Pog. 9, Z2** (uputni zrak): uvjerljiva brodostrojarska primjena zagušenja s apsolutnim tlakovima. Trajanje je ispravno protumačeno kao donja granica.
- **Pog. 9, Z3** (akustičko mjerenje): načelo ultrazvučnog protokomjera s mjerenjem vremena prolaza (transit-time), koje je stvarno i suvremeno.
- **Pog. 9, P4** (sigurnosni otvor): idealna gornja granica jasno je odvojena od certifikacije i koeficijenta istjecanja.
- **Pog. 11, P6** (dimnjak): ispravna logika rezonancije, uz izričito upućivanje na aeroelastičnu provjeru i spiralne trake.
- **Pog. 12, P6** (Driver–Seegmiller, `ex-stepenica-mjerenje-cfd`): stvarni objavljeni mjerni i CFD podatci s izvorom. Tumačenje pošteno kaže da uzroci odstupanja nisu razdvojeni.
- **Pog. 12, Z2** (`task-smicno-naprezanje-prva-celija`): realna cijev s $\lambda=0{,}020$ pri $Re=10^5$ i izravna veza s izborom $y^+$ u CFD-u.
- **Pog. 12, CFD odlomci o hladnoj ploči baterije:** jedina izrazito suvremena primjena u skupini (elektrifikacija i hlađenje). Lajtmotiv je ovdje ispravno nastavljen: tekst kaže što se zadržava i koja fizika ulazi.

## Razlika između procjene i provjere

- **Autorska procjena recenzenta:** sve ocjene vjerodostojnosti i raspone označene s **po sjećanju**. Nisu provjereni u izvoru jer recenzent nije smio pretraživati web.
- **Provjera tijekom čitanja:** ručno sam preračunao radne točke na koje se oslanjaju nalazi:
  - protok zraka za upućivanje 0,850 kg/s;
  - koeficijent opterećenja propelera;
  - dobavni tlak glave za pranje;
  - zamjenske podatke uljnog filma, koji daju isti rezultat $1{,}125\ \text{m/s}$, i kritični gradijent $1{,}6\cdot10^8\ \text{Pa/m}$;
  - $Re$ dimnjaka.

  Verifikatore i bilježnice nisam pokretao.
- **Ograničenje:** razvrstavanje primjera po strukama u P2-5 moja je procjena. Granica između strojarstva i neutralnog laboratorijskog primjera nije oštra.
