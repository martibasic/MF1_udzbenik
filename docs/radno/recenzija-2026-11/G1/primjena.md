# Primjenska recenzija — skupina G1 (poglavlja 1–4)

Recenzent: neovisni primjenski recenzent (brodogradnja, pomorska tehnika, strojarstvo).
Materijal: PDF G1 (knjiga str. 12–88) i izvori `source/u01_*.md` … `source/u04_*.md`
(retci navedeni prema stanju grane `konvencije-recenzije`, 8. 11. 2026.).
Pravila: K9, K14, K16 i ljestvica P0–P3 iz `docs/konvencije_pisanja.md`.
Web nije pretraživan; svi rasponi označeni s „(po sjećanju)” potječu iz
recenzentova iskustva i moraju se provjeriti u izvoru prije unosa u knjigu.

## Sažetak

Primjene u poglavljima 1–4 većinom su vjerodostojne i dobro razgraničene od
konstrukcijske ili propisne ocjene. Poglavlja 3 i 4 imaju vrlo dobre brodske
primjere (sondiranje i ulaž, balastni tank, separator goriva), a poglavlje 1 je
u riješenim primjerima gotovo bez brodogradnje. Najslabije su točke ležaj
statvene cijevi s nerealnim podatcima o viskoznosti i duljini ležaja te brod u
zavoju bez nagiba. Uz to, nekoliko tvrdnji o praksi nema izvor u dodatku E.

Nalaza P0 i P1 nema. Svi su nalazi P2 ili P3.

## Nalazi P2

### P2-1. Ležaj statvene cijevi: viskoznosti, geometrija i vrsta ležaja nisu usklađeni s praksom

- **Mjesto:** str. 41–43; `source/u02_…kapilarnost.md`, r. 487–578.
- **ID:** `ex-u02-hladni-start-i-radna-temperatura-koliko-kosta`.
- **Opis (K16, K9):**
  1. Viskoznosti $\mu_1=0{,}40$ Pa s pri 0 °C i $\mu_2=0{,}040$ Pa s pri 90 °C ne mogu pripadati istom mineralnom ulju. Za ulje ISO VG 100, tipično za statvenu cijev, gruba procjena Waltherovom relacijom iz $\nu_{40}=100$ i $\nu_{100}\approx11$ mm²/s (po sjećanju) daje $\mu\approx1{,}5$–$1{,}7$ Pa s pri 0 °C i $\approx0{,}012$ Pa s pri 90 °C. Omjer je tada oko 100 do 130, a ne 10. Tekst zato podcjenjuje upravo ono što poglavlje tvrdi u uvodu: da se viskoznost snažno mijenja s temperaturom.
  2. Za ležaj $L/D=70/50=1{,}4$ prekratak je. Pravila klasifikacijskih društava za uljem podmazani ležaj od bijele kovine traže duljinu oko $2D$, a uz uvjete najmanje oko $1{,}5D$. Za vodom podmazani ležaj traže oko $4D$ (po sjećanju; provjeriti u pravilima).
  3. Mala plovila s osovinom promjera 50 mm i brzinom vrtnje oko 2400 min⁻¹ gotovo uvijek imaju vodom podmazani gumeni ležaj (engl. *cutless bearing*), a ne zatvorenu uljnu statvenu cijev. Uljna statvena cijev tipična je za trgovačke brodove sa sporohodnim vratilom (po sjećanju).
  4. Puna brzina vrtnje odmah nakon hladnog isplovljenja nije uobičajen pogonski postupak.
- **Prijedlog:** zadržati didaktički omjer 10, ali uz realne temperature. Primjerice, uzeti oko 10 °C (more zimi) s $\mu_1\approx0{,}65$ Pa s i oko 45 °C (radna temperatura ulja) s $\mu_2\approx0{,}068$ Pa s, što je procjena za VG 100 (po sjećanju). Usporedbu 0 °C prema 90 °C premjestiti u rečenicu u **Provjeri i tumačenju**: „za stvarno ulje omjer je reda 100”. Geometriju uskladiti s jednim od dvaju slučajeva:
  - trgovački brod, primjerice $D\approx400$–500 mm, $L\approx2D$, $n\approx80$–120 min⁻¹, radijalna zračnost oko 0,4–0,5 mm (po sjećanju);
  - opći uljem podmazani klizni ležaj bez naziva „statvena cijev”.
  Rečenicu o radnoj temperaturi ulja (r. 577) potkrijepiti izvorom ili je označiti kao nastavnu procjenu (K14).

### P2-2. Brod u ustaljenom zavoju „bez nagiba”: zaključak o prelijevanju ovisi o pretpostavci koja u praksi ne vrijedi

- **Mjesto:** str. 79–80; `source/u04_…`, r. 354–414 (osobito r. 359, 389, 400, 413).
- **ID:** `ex-tank-broda-u-kruznom-zavoju`.
- **Opis (K9, K16):** pretpostavka „brod plovi bez nagiba” jest navedena. Ipak, tvrdnje da je razlika sondi od 0,19 m „mjera ubrzanja u zavoju” i da je granica „daleko iznad brzine broda” vrijede samo uz tu pretpostavku.
  - U ustaljenom zavoju istisninski se brod nagne prema van; početni nagib prema unutra brzo prolazi. Gruba procjena $\tan\varphi\approx(a/g)(KG-T/2)/GM$, uz $KG-T/2\approx3$–5 m i $GM\approx1$–2 m, daje $\varphi\approx2$–6°. Izraz je istoga oblika kao momenat nagiba pri okretu u IMO IS Code 2008 (po sjećanju).
  - U okviru tanka taj se nagib **zbraja** s 1,24°. Relativni nagib tada iznosi oko 3–7,5°, a $\Delta h$ preko 9 m oko 0,5–1,2 m. Gornja vrijednost već dodiruje vrh tanka ($\Delta h_{max}=1{,}20$ m).
  - Formulacija u **Provjeri i tumačenju** 2, „dodaje ili oduzima… ovisno o tome naginje li se brod prema van ili prema unutra”, ne kaže da je u ustaljenom zavoju mjerodavan nagib prema van.
- **Prijedlog:** u **Provjeri i tumačenju** 2 navesti da se brod u ustaljenom zavoju nagne prema van i da taj nagib povećava razliku razina. Dodati jednu rečenicu s redom veličine i uputom na pog. 6 i IS Code iz dodatka E. Rečenicu o sondama (r. 389) ograničiti: „uz pretpostavku broda bez nagiba”. Sondiranje se u praksi provodi u mirovanju, pa očitanja u zavoju daje daljinski mjerač razine. Naziv „poprečni balastni tank” mogao bi se zamijeniti nazivom „tank dvodna” (P3).

### P2-3. Brodogradnja izostaje iz riješenih primjera poglavlja 1

- **Mjesto:** str. 18–23; `source/u01_…`, r. 253–582.
- **ID-jevi:** svi riješeni primjeri pog. 1 (`ex-u01-…`).
- **Opis (K16):** šest riješenih primjera obuhvaća ulje, opterećeni klip, servisnu dizalicu, platformu, kočnicu vozila i steznu napravu za baterije. Sve su to strojarski ili opći primjeri. Brodski je kontekst u uvodu (r. 9) i u zadatku Z2 (kormilarski stroj). Student brodogradnje u riješenim primjerima ne vidi nijednu svoju primjenu Pascalova zakona.
- **Prijedlog:** jedan opći primjer zamijeniti brodskim ili mu promijeniti kontekst. Najprirodnija je servisna dizalica ili opterećeni klip. Prijedlozi sa sličnim računom:
  - hidraulička matica propelera (engl. *Pilgrim nut*), kojom se propeler navlači na konus vratila; tlakovi su reda desetaka MPa (po sjećanju);
  - hidraulički napinjač vijaka spojke osovinskog voda;
  - cilindar poklopca grotla ili rampe broda ro-ro.

  Bez novih P/Z mjesta: kontekst servisne dizalice (r. 303–363) promijeniti tako da račun ostane isti.

### P2-4. Sondiranje teretnog tanka: preciznost slaganja, gustoća tereta i postupak u inertiranom tanku

- **Mjesto:** str. 58–60; `source/u03_…`, r. 334–417 (r. 339, 377, 398–401).
- **ID:** `ex-sondiranje-teretnog-tanka-s-tlacnim-mjeracem-razine`.
- **Opis (K9, K16):**
  1. Tvrdnja „dva neovisna mjerenja razine slažu se unutar 1 mm, što je bolje od razlučivosti vrpce” (r. 377) proizlazi iz složenih nastavnih podataka. Tlačni pretvornik s mjernim područjem oko 250 kPa i točnošću 0,1–0,25 % pune skale (po sjećanju) ima nesigurnost reda ±3–7 cm stupca ulja. Slaganje unutar 1 mm stoga nije realno obilježje mjerenja.
  2. Model tlak → razina osjetljiv je na gustoću tereta pri temperaturi tanka. Za plinsko ulje promjena je oko 0,7 kg/m³ po kelvinu (po sjećanju), pa 10 K pogreške daje oko 13 cm na 16 m. Upravo je to glavni praktični izvor pogreške tlačnog mjerenja razine, a tekst ga ne navodi.
  3. „Ručno sondiranje s pastom” u tanku pod inertnim plinom: pri inertiranim tankovima propisano je zatvoreno mjerenje kroz parnu bravu (engl. *vapour lock*), sondom za ulaž, temperaturu i granicu ulje–voda (engl. *UTI*) (ISGOTT, po sjećanju). Pasta na mjernoj šipki pripada otvorenom mjerenju.
  4. Tlocrt $A_t=600$ m² velik je za tank tankera za naftne proizvode visine oko 18,6 m. Tank srednjega tankera (engl. *MR*) ima tlocrt reda 200–300 m² (po sjećanju), pa je pogreška od 250 m³ napuhana.
- **Prijedlog:** r. 377 zamijeniti rečenicom „slažu se unutar mjerne nesigurnosti pretvornika (reda centimetra)”. U točki 4 ili u **Provjeri i tumačenju** dodati jednu rečenicu o gustoći pri temperaturi tereta. „Pasta za otkrivanje vode” zamijeniti sondom UTI s detektorom granice ulje–voda kroz parnu bravu. Količina tereta za predaju ne određuje se iz tlaka, nego iz tablica ulaža s ispravcima za trim, nagib i temperaturu; to treba navesti kao razgraničenje. $A_t$ smanjiti na oko 250 m² ili brod navesti kao veći tanker.

### P2-5. Bočni balastni tank „visok 5 m s dnom na oplati dna” nije tipičan za tanker s dvostrukim trupom

- **Mjesto:** str. 61–63 i slika 3.6; `source/u03_…`, r. 463–531. CFD odlomak na str. 54 (r. 164) upućuje na isti primjer.
- **ID:** `ex-u03-balastni-tank-broda-tlak-iznutra-i-izvana`.
- **Opis (K16):** u tankeru s dvostrukim trupom bočni balastni tank obično se proteže do glavne palube. Često je spojen s dvodnom u tank oblika slova L ili U, a visina dvodna iznosi oko 2–3 m (po sjećanju). Tank visok 5 m s gornjom stijenkom ispod vodne linije više nalikuje donjem bočnom tanku.
  - Za taj je slučaj račun točan, ali izostaje najpoučnije stanje stvarnog tanka: kad je pun tank viši od gaza, iznad vodne linije neto tlak djeluje **prema van**.
  - Usto, ulaž se u stanju C (r. 521) mjeri od vrha tanka. U P3 (r. 339) ulaž je definiran od referentne točke na palubi, pa nastaje nedosljednost.
- **Prijedlog:** nazvati tank „donji bočni tank” ili „tank dvodna i uzvoja” i navesti da je to nastavno pojednostavnjenje. Druga je mogućnost dodati jednu rečenicu: za tank koji se proteže iznad gaza neto tlak na oplatu iznad vodne linije mijenja smjer. Ulaž u stanju C mjeriti od istoga referentnog mjesta kao u P3 ili ga preimenovati u „visina praznog prostora iznad balasta”.

### P2-6. Gustoća morske vode 1035 kg/m³ nedosljedna je s ostatkom skupine

- **Mjesto:** str. 57; `source/u03_…`, r. 262.
- **ID:** `ex-u03-diferencijalni-manometar-izme-u-slatke-i-morske`.
- **Opis (K16, dosljednost):** svugdje drugdje u skupini (u02 Z4, u03 P3 i P5, u04 P3) koristi se $\rho_{mv}=1025$ kg/m³. Vrijednost 1035 kg/m³ fizikalno je moguća, ali je na gornjem rubu raspona površinske morske vode od oko 1020 do 1030 kg/m³ (po sjećanju). Primjer uz to nema tehnički kontekst: nije rečeno zašto bi se vod slatke i vod morske vode spajali manometrom.
- **Prijedlog:** uzeti 1025 kg/m³. Kontekst bi bio središnji hladnjak brodskog rashladnog sustava, pločasti izmjenjivač između kruga slatke vode i kruga mora. Tlak u krugu slatke vode drži se višim od tlaka mora kako propuštanje ne bi onečistilo slatki krug (po sjećanju, uobičajena brodska praksa). Pozitivan $p_1-p_2$ tada ima izravno inženjersko značenje.

### P2-7. Usis crpke ulja: granica tlaka pare nije praktična granica za ulje

- **Mjesto:** str. 60–61; `source/u03_…`, r. 419–461.
- **ID:** `ex-u03-tlak-na-usisu-pumpe-za-cirkulaciju-ulja`.
- **Opis (K9, K16):** račun je ispravan, a ograda o $NPSH$ postoji. Ipak, za ulje je $p_v\approx200$ Pa nastavna vrijednost, jer je stvarni tlak pare ulja za podmazivanje mnogo niži.
  - Praktičnu granicu daje izdvajanje otopljenoga zraka, koji u ulju čini oko 8–10 % volumena pri atmosferskom tlaku.
  - Druga je granica najmanji apsolutni ulazni tlak koji propisuje proizvođač, za mnoge zupčaste i klipne crpke oko 0,8 bar (po sjećanju).
  - Dobivenih 80,8 kPa pri visini od 2,4 m već je na toj granici. „Statička gornja granica 11,8 m” zato može zavarati.
  - Na brodu se crpke za cirkulaciju ulja obično smještaju ispod razine ulja u spremniku ili su uronjene, s potopljenim usisom.
- **Prijedlog:** u **Provjeri i tumačenju** dodati rečenicu: „Za ulje praktična granica nastupa mnogo ranije, zbog izdvajanja otopljenoga zraka i proizvođačeva najmanjeg ulaznog tlaka; zato se takve crpke postavljaju s potopljenim usisom.” Izvor ili oznaku nastavne procjene dodati prema K14.

### P2-8. Tvrdnje o praksi bez izvora (K14) i nedostatak izvora iz brodskog strojarstva u dodatku E

- **Mjesta:**
  - str. 43; u02, r. 577: „u službi ulje statvene cijevi obično radi hladnije…”;
  - mrežni ključ; u03, r. 712: „u praksi se ne ide ispod 5–10°”;
  - str. 84; u04, r. 595: izbor gravitacijskog diska prema gustoći goriva;
  - str. 60; u03, r. 416: postupak pri ljuljanju i emulgiranoj vodi;
  - str. 25; u01, r. 658: Rapsonov raspored.
- **Opis:** to su tvrdnje o praksi bez izvora i bez izričite oznake nastavne procjene. Prema mom iskustvu sadržajno su točne. Dodatak E (`d05_literatura.md`) nema nijedan izvor za brodske pomoćne strojeve, kormilarske uređaje, osovinski vod ni mjerenje tereta.
- **Prijedlog:** dodati jedan ili dva udžbenika brodskog strojarstva u dodatak E. Po sjećanju to su H. D. McGeorge, *Marine Auxiliary Machinery*, i D. A. Taylor, *Introduction to Marine Engineering*; izdanje, izdavača i godinu treba provjeriti. Tvrdnje o mjerenju tereta potkrijepiti ISGOTT-om, aktualno izdanje. Inače tvrdnje izrijekom označiti kao nastavnu procjenu.

### P2-9. Nazivlje: „upravljački klip” u ručnoj dizalici

- **Mjesto:** str. 19; `source/u01_…`, r. 308.
- **ID:** `ex-u01-servisna-hidraulicna-dizalica-t2`.
- **Opis:** u ručnoj hidrauličkoj dizalici mali klip je crpni (tlačni) klip, a ne upravljački. „Upravljački klip” u hidraulici označuje razvodnik ili servoklip. U istom poglavlju (r. 370, 528, 750–756) dosljedno se piše „crpni klip”.
- **Prijedlog:** „crpni klip površine $A_1$”.

## Nalazi P3

1. **Kočnica vozila: promjeri i naziv.** Str. 21–23; u01, r. 444–521; `ex-u01-hidraulicna-kocnica-vozila-s-razdiobom-na-vise`.
   - Klip prednje kočne čeljusti od 35 mm malen je za osobni automobil. Za plivajuću čeljust s jednim klipom tipično je 48–57 mm, a straga 34–38 mm (po sjećanju).
   - Tekst spominje kliješta i disk, pa je „kočni cilindar” naziv za bubanj-kočnicu. Primjereniji je naziv „klip kočne čeljusti (kliješta)”.
   - Valja navesti da model nema servopojačivač. Uz servopojačivač stvarni tlakovi pri jakom kočenju veći su, reda 8–12 MPa (po sjećanju).
2. **Stezna naprava s ručnim crpnim klipom na robotskoj liniji.** Str. 23; u01, r. 523–582. Na automatiziranoj liniji tlak ne stvara ručni klip, nego hidraulički agregat ili pneumohidraulički pojačivač tlaka (engl. *booster*). Pojačivač je i sam Pascalov uređaj, pa bi primjer bio još bolji.
3. **Kormilarski stroj (Z2).** Str. 25; u01, r. 654–679. U izvedbi s četiri cilindra elementi su obično plunžeri (engl. *rams*) povezani križnom glavom s rudom, a ne klipovi u užem smislu. Tekst naizmjence koristi „kormilarski stroj” i „kormilarski uređaj” (r. 658). Prema SOLAS-ovu nazivlju uređaj obuhvaća stroj i pogon, pa razlikovanje treba ostaviti namjerno ili ga ujednačiti. Brojke su realne: 6 MPa, 88 kN m i hod koji odgovara otklonu od oko 27°.
4. **Procjep između limova (Z4).** Str. 45; u02, r. 759–784. Ulazna barijera od 189 Pa odgovara stupcu vode od oko 19 mm. Rubu spoja koji je uronjen ili ga zapljuskuju valovi dovoljno je nekoliko centimetara vode da je prijeđe. Vrijedi dodati rečenicu da premaz ne sprječava ulazak vode u uronjen procjep. Preklopni spojevi u suvremenom zavarenom trupu rijetki su; točniji je primjer procjep ispod podloške ili dodirne plohe.
5. **Pločasti viskozimetar (Z1, Z5).** Str. 44–45; u02, r. 677 i 792. Ploča od 0,22 m² nije viskozimetar, nego laboratorijski model. Rotacijski viskozimetri imaju površine reda cm². Dovoljno ga je nazvati „nastavni pokus s kliznom pločom”.
6. **Dron na 1528 m (u03 Z1).** Str. 64; r. 629–655. U otvorenoj kategoriji EU-a dron smije letjeti do oko 120 m iznad tla (po sjećanju). Za 1,5 km prikladniji su radiosonda, laki zrakoplov ili planinarski visinomjer, a fizika ostaje ista.
7. **Lučka dizalica (u04 Z2).** Str. 85; r. 683.
   - Ubrzanja $a_x=1{,}5$ i $a_z=1{,}2$ m/s² visoka su. Za kontejnersku obalnu dizalicu tipično je oko 0,4–0,8 m/s² za kolica i 0,4–1,0 m/s² za vitlo (po sjećanju).
   - „Spremnik se ne njiše” stroga je idealizacija, jer se teret obješen o užad pri ubrzanju kolica njiše. Treba je nazvati takvom ili spomenuti sustav protiv njihanja.
8. **Autocisterna (u04 P5).** Str. 82–83; r. 497–538. Otvoreni spremnik duljine 1,2 m nije odjeljak autocisterne. Realni odjeljci zatvoreni su i dugi oko 1,5–3 m (po sjećanju). Bolji je naslov „spremnik na vozilu” ili realniji odjeljak s ograničenim punjenjem. Razgraničenje od operativnih ograničenja (r. 536) je dobro.
9. **Servisni modul s kosom stijenkom (u04 P2).** Str. 77–78; r. 290–352. Stijenka postavljena okomito na slobodnu površinu za jedno određeno ubrzanje nema prepoznatljiv tehnički uređaj, pa je primjer nategnut. Prijedlog: kosa stijenka ili inspekcijsko okno zatvorenoga spremnika goriva na vozilu ili brodu, s istim računom.
10. **Tanker za plinsko ulje i inertni plin.** Pretlak inertnog plina od 3 kPa realan je i dobro je što se ne zanemaruje. U tekstu bi vrijedilo navesti da tlak ograničavaju sigurnosni tlačno-vakuumski ventili (engl. *P/V valve*), čiji je otvorni tlak reda 14–20 kPa (po sjećanju).
11. **Suvremenost na pomorskoj strani.** Strojarstvo u skupini G1 ima suvremene primjene: hlađenje baterija, steznu napravu za baterijske module, IoT senzor i laboratorij na čipu. Pomorska strana ostaje kod teškoga goriva, plinskog ulja i klasičnog balasta. Kurikularna matrica za pog. 1–4 ne traži lajtmotiv „pomorska i offshore dekarbonizacija”, pa ovo nije kršenje. Ipak, jedna rečenica ili kontekst bili bi dobrodošli, primjerice:
    - u03 P3: tlačno mjerenje razine metanola u tanku goriva ($\rho\approx790$ kg/m³) s dušikom iznad tekućine;
    - u04 uvod ili CFD: zapljuskivanje u membranskim tankovima LNG-a i ograničenja punjenja;
    - u01 CFD: rashladni krug baterijskog sustava električnog trajekta, čime bi lajtmotiv hlađenja obuhvatio obje struke.
12. **Etanol na staklu (u02 P2).** Str. 39–40. Etanol na čistom staklu praktički potpuno kvasi ($\theta\approx0^\circ$). Kut od 18° moguć je samo za onečišćenu ili obrađenu površinu, pa to treba reći jednom riječju.
13. **Napomene o potvrđenom autorskom nazivlju.** Ovo nisu nalazi.
    - „Oplakana površina osovine” (u02, r. 534): u tribologiji se češće govori o površini rukavca ili nosivoj površini ležaja. „Oplakan” je u brodogradnji ustaljen za trup, pa ga primjena na rukavac u uljnom filmu malo rasteže. Autorica odlučuje.
    - „Propeler” je potvrđen. U brodograđevnoj praksi i propisima i dalje se uz njega koristi „brodski vijak”. Jedan spomen u zagradi pri prvom pojavljivanju u knjizi pomogao bi studentima brodogradnje.
    - „Crpka”, „stabilitet”, „ulaž” i „zapljuskivanje”: slažem se.

## Ravnoteža struka

| Pog. | Brodogradnja i pomorstvo | Strojarstvo | Ostalo | Ocjena |
| --- | --- | --- | --- | --- |
| 1 | uvod (r. 9); Z2 kormilarski stroj | P kočnica, stezna naprava za baterije, dizalica, platforma; CFD hlađenje baterije; Z5, Z6 | P1, Z1, Z3, Z4 opći | **brodogradnja slaba** (0/6 riješenih primjera), vidi P2-3 |
| 2 | P statvena cijev; Z4 limovi u moru; uvod | P disk aksijalnog ležaja, uljni sloj; CFD hladna ploča i mlaznica; Z1, Z3, Z5 | P laboratorij na čipu, mikrodozator; Z2, Z6 | uravnoteženo; tri od dvanaest primjera i zadataka izvan obiju struka (biomedicina, doziranje) |
| 3 | P slatka i morska voda, P sondiranje tankera, P balastni tank; CFD balastni tank | P usis crpke ulja; Z3 ventilacijski kanal; CFD spremnik, usis | P vodotoranj (vodni grad); Z1 dron | dobro, brodogradnja najjača u skupini |
| 4 | P balastni tank u zavoju; P separator goriva (brodsko strojarstvo); Z2 lučka dizalica | P autocisterna, rotirajući spremnik, servisni modul; Z5, Z6 | — | uravnoteženo |
| **G1** | prisutna u svim poglavljima, slaba u pog. 1; offshore i pomorska dekarbonizacija izostaju | dobro zastupljeno, suvremeno | — | ukupno prihvatljivo; ispraviti pog. 1 |

## Posebno dobre primjene

- **u03 P3, sondiranje teretnog tanka** (`ex-sondiranje-teretnog-tanka-s-tlacnim-mjeracem-razine`, str. 58–60). Pravo brodsko pitanje: ulaž prema sondiranju, inertni plin, vodeni talog i dva neovisna mjerenja. Zaključak „o zanemarivanju odlučuje red veličine člana, ne vrsta fluida” izvrstan je.
- **u04 P6, centrifugalni separator goriva** (`ex-centrifugalni-separator-goriva`, str. 83–84). Brzina bubnja, gustoće pri temperaturi separacije i uloga gravitacijskog diska realni su (bubanj oko 7000–10 000 min⁻¹ po sjećanju). Proboj vodene brtve pri $\rho=950$ kg/m³ stvaran je pogonski kriterij, a procjena Coriolisova člana pokazuje granicu modela.
- **u03 P5, balastni tank** (str. 61–63). Neto tlak kao razlika vanjskog i unutarnjeg tlaka vrlo je dobro izveden, a razgraničenje prema propisanim kombinacijama opterećenja ispravno je. Primjedba o geometriji nalazi se u P2-5.
- **u01 Z2, kormilarski stroj** (`task-kormilarski-stroj-dva-cilindra`, str. 25). Realne brojke, ispravan raspored s dijagonalnim parom cilindara i izričito razgraničenje od propisnog proračuna.
- **u01 P6, stezna naprava** (str. 23). Usporedba hidrostatičkog člana (kPa) s radnim tlakom (MPa) i rečenica o sustavu od 100 kPa uzorno pokazuju kada je pretpostavka o jednakim visinama opravdana.
- **u03 CFD, „Što znači nizak tlak na usisu?”** i odlomak o $p_{rgh}$ (str. 54–55). Vrlo praktično: zamjena referenci tlaka česta je pogreška u stvarnim usporedbama CFD-a i mjerenja.
- **u03 P6, vodotoranj s IoT senzorom** (str. 63–64). Alarmni prag izvodi se iz nesigurnosti i posljedica, a ne iz univerzalne vrijednosti. To je dobro razgraničenje.
- **u04 P3, zavoj** (str. 79–80). Provjera paraboloida prema lokalnoj linearnoj aproksimaciji je dobra; primjedba o nagibu nalazi se u P2-2.

## Razgraničenje: ukupna ocjena

Razgraničenje od konstrukcijske, sigurnosne i propisne ocjene vrlo je dosljedno:

- platforma: „nije dopuštena nosivost”;
- kormilarski stroj: „ne zamjenjuju propisni proračun”;
- statvena cijev: „nije radna karta”;
- balastni tank: „propisane kombinacije opterećenja”;
- autocisterna: „ne operativna ograničenja”;
- stol: „nije odobrenje za puštanje u rad”;
- vodotoranj: alarmni prag.

Nedostaje samo razgraničenje uz količinu tereta u P3 pog. 3 (P2-4) i uz zaključak o prelijevanju u P3 pog. 4 (P2-2).

## Ograničenja ove recenzije

- Web nije pretraživan. Rasponi označeni s „(po sjećanju)” potječu iz recenzentova iskustva. Treba ih provjeriti u navedenim izvorima (pravila klasifikacijskih društava, ISGOTT, IMO IS Code 2008, tehnička dokumentacija proizvođača) prije unosa u tekst.
- Izvode i brojčane rezultate nisam provjeravao, osim ondje gdje je to bilo potrebno za ocjenu vjerodostojnosti. Skice sam pregledao samo za Z2 u pog. 1, balastni tank i zavoj.
- Didaktička kvaliteta i razine T1–T4 nisu predmet ove recenzije.
