<!-- Generirano skriptom scripts/generate_exercise_key.py; ne uređivati ručno. -->

## Ključ smjernica i kontrolnih rezultata

Zadatci su označeni Z1–Z6 unutar svakog poglavlja, jednako kao u glavnom tekstu. Ovaj dodatak sadrži sažete smjernice postupka i kontrolne rezultate za tiskano izdanje. Ne zamjenjuje cjelovito rješenje: provjera uključuje model, pretpostavke, jedinice i barem jednu neovisnu fizikalnu provjeru. Otvoreni zadatci razina T3 i T4 mogu imati više prihvatljivih odgovora.

## Osnove fluida i Pascalov zakon

### Z1. Gustoća ulja iz vaganja {#key-task-gustoca-ulja-iz-vaganja .unnumbered .unlisted}

[Vrati se na zadatak](u01_osnove_fluida_i_pascalov_zakon.qmd#task-gustoca-ulja-iz-vaganja)

**Sažetak.** Prazna posuda ima masu $m_0 = 42{,}6\ \text{g}$. S volumenom ulja $V_1 = 50{,}0\ \text{cm}^3$ njezina ukupna masa iznosi $m_1 = 85{,}5\ \text{g}$, a s volumenom $V_2 = 100{,}0\ \text{cm}^3$ ukupna masa iznosi $m_2 = 128{,}7\ \text{g}$.…

**Smjernica postupka.** Najprije odvoji masu ulja od mase posude. Gustoće računaj u SI jedinicama; za preostale dvije veličine upotrijebi srednju gustoću. Bez podataka o točnosti instrumenata ne možeš razliku pripisati samo svojstvu ulja.

**Kontrolni rezultat ili kriterij.** $\rho_1=858\ \text{kg/m}^3$, $\rho_2=861\ \text{kg/m}^3$, $\bar\rho=859{,}5\ \text{kg/m}^3$; $\bar\gamma\approx8{,}432\ \text{kN/m}^3$, $s_r=0{,}8595$. Masa ulja jest razlika ukupne mase i mase posude. Sama razlika gustoća ne dokazuje nehomogenost: nedostaju podatci o mjernoj točnosti.

### Z2. Servisna hidraulična preša {#key-task-u01-u-servisnoj-hidraulicnoj-presi-mali-klip-promjera .unnumbered .unlisted}

[Vrati se na zadatak](u01_osnove_fluida_i_pascalov_zakon.qmd#task-u01-u-servisnoj-hidraulicnoj-presi-mali-klip-promjera)

**Sažetak.** U servisnoj hidrauličnoj preši mali klip promjera $d_1 = 28\ \text{mm}$ potiskuje ulje prema radnom klipu promjera $d_2 = 140\ \text{mm}$. Ako operater na mali klip djeluje silom $F_1 = 180\ \text{N}$, odredi tlak u ulju, silu na radnom…

**Smjernica postupka.** Primjenjuju se $p = F_1/A_1$, $F_2 = pA_2$ te volumna bilanca $A_1 s_1 = A_2 s_2$.

**Kontrolni rezultat ili kriterij.** $p \approx 292\ \text{kPa}$; $F_2 = 4{,}5\ \text{kN}$; $s_2 = 4{,}8\ \text{mm}$.

### Z3. Provjera pogrešnog proračuna preše {#key-task-pogreske-omjera-sile-i-pomaka .unnumbered .unlisted}

[Vrati se na zadatak](u01_osnove_fluida_i_pascalov_zakon.qmd#task-pogreske-omjera-sile-i-pomaka)

**Sažetak.** Na maloj nastavnoj preši promjeri klipova iznose $d_1 = 20\ \text{mm}$ i $d_2 = 60\ \text{mm}$. Stalna ulazna sila jest $F_1 = 100\ \text{N}$, a ulazni pomak $s_1 = 90\ \text{mm}$. Student predlaže: „Promjer radnog klipa triput je veći…

**Smjernica postupka.** Usporedi površine, ne promjere. Provjeri istisnute volumene. Za stalnu silu rad je umnožak sile i puta u njezinu smjeru; u računu rada pretvori milimetre u metre.

**Kontrolni rezultat ili kriterij.** $A_2/A_1=9$, $F_2=900\ \text{N}$, $s_2=10\ \text{mm}$; $W_1=W_2=9\ \text{J}$. Pogrešni izlazni rad bio bi $81\ \text{J}$. Površina raste s kvadratom promjera, a povećanje sile prati smanjenje pomaka. Predloženi izlazni rad devet je puta veći od raspoloživog ulaznog rada.

### Z4. Promjer cilindra iz mjerenja pomaka {#key-task-promjer-cilindra-iz-volumena .unnumbered .unlisted}

[Vrati se na zadatak](u01_osnove_fluida_i_pascalov_zakon.qmd#task-promjer-cilindra-iz-volumena)

**Sažetak.** Laboratorijski cilindar prije mjerenja potpuno je napunjen tekućinom i odzračen. Dovedeni dodatni volumeni, mjereni od istoga početnog položaja, i pomaci klipa pri malom opterećenju prikazani su u tablici. U zasebnom pokusu s blokiranim…

**Smjernica postupka.** Usporedi omjere dodatnog volumena i pomaka. Iz dobivene površine izračunaj promjer, zatim silu u drugom pokusu. Podudaranje pri malom opterećenju podupire model samo u ispitanim uvjetima; odstupanje pri većem tlaku zahtijeva dodatne podatke.

**Kontrolni rezultat ili kriterij.** Sva tri para daju $A=500\ \text{mm}^2$ i $d\approx25{,}23\ \text{mm}$; idealno $F=200\ \text{N}$. Tablica je usklađena s modelom u ispitanim uvjetima. Manji pomak pri većem tlaku opravdava provjeru stlačivosti, elastičnosti i propuštanja; ne dokazuje jedan određeni uzrok.

### Z5. Izbor pumpe uz ograničenje sile i hoda {#key-task-izbor-pumpe-sila-i-hod .unnumbered .unlisted}

[Vrati se na zadatak](u01_osnove_fluida_i_pascalov_zakon.qmd#task-izbor-pumpe-sila-i-hod)

**Sažetak.** Radni klip površine $A_L = 30\ \text{cm}^2$ mora svladati stalnu silu $F_L = 6{,}0\ \text{kN}$ i prijeći put $s_L = 10\ \text{mm}$. Najveća dopuštena sila neposredno na pumpnom klipu iznosi $F_{p,max} = 150\ \text{N}$, a zbroj njegovih…

**Smjernica postupka.** Kreni od opterećenja radnog klipa. Jedan zahtjev postavlja gornju, a drugi donju granicu površine pumpe. Računaj s nezaokruženim površinama i provjeri obje granice prije odabira.

**Kontrolni rezultat ili kriterij.** $p=2{,}00\ \text{MPa}$. Za promjere 8, 9 i 10 mm parovi $(F_p,s_p)$ jesu približno $(100{,}5\ \text{N},0{,}5968\ \text{m})$, $(127{,}2\ \text{N},0{,}4716\ \text{m})$ i $(157{,}1\ \text{N},0{,}3820\ \text{m})$. Odabire se 9 mm; 8 mm ne zadovoljava hod, a 10 mm silu. Za odabranu pumpu $W_p=W_L=60\ \text{J}$.

### Z6. Nosivost stola uz nesigurnu učinkovitost {#key-task-u01-hidraulicni-radni-stol-podupiru-tri-jednaka-cilindra .unnumbered .unlisted}

[Vrati se na zadatak](u01_osnove_fluida_i_pascalov_zakon.qmd#task-u01-hidraulicni-radni-stol-podupiru-tri-jednaka-cilindra)

**Sažetak.** Hidraulični radni stol podupiru tri jednaka cilindra, svaki površine $A_L = 95\ \text{cm}^2$. Ulje dovodi pumpni klip promjera $d = 22\ \text{mm}$ na koji djeluje sila $F_p = 360\ \text{N}$. Odredi tlak u ulju, ukupno idealno opterećenje…

**Smjernica postupka.** Površina $A_p$ i tlak određuju se iz $p = F_p/A_p$, idealno opterećenje iz $G = 3pA_L$, a idealni hod pumpe iz volumne bilance $A_p s_p = 3A_L \Delta z$. Za stvarni sustav vrijedi $G_{kor}=\eta_FG$ i $s_{p,st}=s_p/\eta_V$. Konzervativna se odluka temelji na vrijednostima $\eta_{F,min}$ i $\eta_{V,min}$, a ne na srednjim vrijednostima.

**Kontrolni rezultat ili kriterij.** $p \approx 947\ \text{kPa}$; $G \approx 27{,}0\ \text{kN}$; $s_p \approx 1{,}35\ \text{m}$. Nominalno je $G_{kor}\approx23{,}2\ \text{kN}$ i $s_{p,st}\approx1{,}50\ \text{m}$, a konzervativno $G_{kor,min}\approx22{,}1\ \text{kN}$ i $s_{p,st,max}\approx1{,}55\ \text{m}$. Oba zadana brojčana kriterija jesu zadovoljena, ali s malim rezervama, približno $0{,}1\ \text{kN}$ i $0{,}05\ \text{m}$; to nije potpuna provjera stroja ni odobrenje za puštanje u rad.

## Viskoznost, površinska napetost i kapilarnost

### Z1. Viskozna sila između ploča {#key-task-u02-izme-u-dviju-paralelnih-ploca-nalazi-se .unnumbered .unlisted}

[Vrati se na zadatak](u02_viskoznost_povrsinska_napetost_i_kapilarnost.qmd#task-u02-izme-u-dviju-paralelnih-ploca-nalazi-se)

**Sažetak.** Između dviju paralelnih ploča nalazi se glicerin debljine $\delta = 2{,}4\ \text{mm}$. Gornja ploča površine $A = 0{,}22\ \text{m}^2$ giba se stalnom brzinom $v = 0{,}65\ \text{m/s}$, donja ploča miruje, a dinamička viskoznost glicerina…

**Smjernica postupka.** $dv/dy = v/\delta$, zatim $\tau = \mu dv/dy$ i na kraju $F = \tau A$.

**Kontrolni rezultat ili kriterij.** $dv/dy \approx 271\ \text{s}^{-1}$; $\tau \approx 228\ \text{Pa}$; $F \approx 50\ \text{N}$.

### Z2. Kapljica i sapunasti mjehur {#key-task-kapljica-i-sapunasti-mjehur .unnumbered .unlisted}

[Vrati se na zadatak](u02_viskoznost_povrsinska_napetost_i_kapilarnost.qmd#task-kapljica-i-sapunasti-mjehur)

**Sažetak.** Sferna kapljica i tankostijeni sapunasti mjehur imaju isti promjer $d = 1{,}20\ \text{mm}$. Za obje idealizirane tvorevine uzmi površinsku napetost $\sigma = 0{,}030\ \text{N/m}$. Kapljica ima jednu međupovršinu tekućina–zrak, a sapunasti…

**Smjernica postupka.** Za kapljicu vrijedi $\Delta p=4\sigma/d$, a za tanki sapunasti mjehur $\Delta p=8\sigma/d$. Broj međupovršina razlikuje ta dva slučaja; promjer nije polumjer.

**Kontrolni rezultat ili kriterij.** $\Delta p_k=100\ \text{Pa}$; $\Delta p_m=200\ \text{Pa}$; $\Delta p_m/\Delta p_k=2$. U oba slučaja unutarnji je tlak viši, a mjehur ima dva doprinosa površinske napetosti.

### Z3. Ploča između dva uljna procjepa {#key-task-ploca-izmedu-dva-procjepa .unnumbered .unlisted}

[Vrati se na zadatak](u02_viskoznost_povrsinska_napetost_i_kapilarnost.qmd#task-ploca-izmedu-dva-procjepa)

**Sažetak.** Tanka ploča klizi udesno brzinom $v = 0{,}30\ \text{m/s}$ između dviju nepomičnih paralelnih stijenki. Površina svake strane ploče u dodiru s uljem iznosi $A = 0{,}020\ \text{m}^2$. U oba procjepa nalazi se isto ulje. Gornji procjep ima…

**Smjernica postupka.** Svaki procjep ima vlastitu promjenu brzine od nule do $v$. Izračunaj oba iznosa gradijenta zasebno. Sile ulja na pokretnoj ploči obje se suprotstavljaju njezinu gibanju pa se njihovi iznosi zbrajaju.

**Kontrolni rezultat ili kriterij.** $|\tau_1|=36\ \text{Pa}$, $|\tau_2|=18\ \text{Pa}$; $F_1=0{,}72\ \text{N}$, $F_2=0{,}36\ \text{N}$, $F=1{,}08\ \text{N}$. Oba otpora djeluju ulijevo, vučna sila udesno. Pogrešan postupak daje $0{,}24\ \text{N}$: ploča dijeli dva zasebna sloja. Za vrlo velik donji procjep njegov doprinos teži nuli unutar tog modela.

### Z4. Kapilarni uspon etanola {#key-task-u02-kapilara-promjera-uronjena-je-u-etanol-za .unnumbered .unlisted}

[Vrati se na zadatak](u02_viskoznost_povrsinska_napetost_i_kapilarnost.qmd#task-u02-kapilara-promjera-uronjena-je-u-etanol-za)

**Sažetak.** Kapilara promjera $d = 0{,}60\ \text{mm}$ uronjena je u etanol za koji vrijedi $\sigma = 0{,}022\ \text{N/m}$, $\theta = 18^\circ$ i $\rho = 790\ \text{kg/m}^3$. Odredi kapilarni uspon i usporedi ga s usponom u drugoj kapilari promjera…

**Smjernica postupka.** $h = 4\sigma \cos\theta /(\rho g d)$; drugi slučaj računa se istom formulom samo s novim promjerom.

**Kontrolni rezultat ili kriterij.** $h \approx 18{,}0\ \text{mm}$; kod $d = 1{,}2\ \text{mm}$ upola manje, $h \approx 9{,}0\ \text{mm}$.

### Z5. Može li se pretpostaviti stalna viskoznost? {#key-task-newtonski-model-iz-mjerenja .unnumbered .unlisted}

[Vrati se na zadatak](u02_viskoznost_povrsinska_napetost_i_kapilarnost.qmd#task-newtonski-model-iz-mjerenja)

**Sažetak.** U nastavnom pokusu ispituju se uzorci A i B između nepomične i pokretne ploče. Samo jedna strana pokretne ploče površine $S = 0{,}010\ \text{m}^2$ dodiruje uzorak; razmak ploča je $\delta = 1{,}0\ \text{mm}$. Pri stalnoj temperaturi…

**Smjernica postupka.** Iz sile i površine izračunaj naprezanje, a iz brzine i razmaka gradijent. Njihov omjer jest prividna viskoznost. Newtonski model traži isti omjer u svim redcima pri istoj temperaturi; samo jedna točka to ne provjerava.

**Kontrolni rezultat ili kriterij.** Gradijenti su $100$, $200$, $400\ \text{s}^{-1}$. A: $\tau=20,40,80\ \text{Pa}$, $\mu=0{,}20\ \text{Pa s}$ i $F_*=0{,}60\ \text{N}$. B: $\tau=30,45,60\ \text{Pa}$, prividne viskoznosti $0{,}30$, $0{,}225$, $0{,}15\ \text{Pa s}$. Prva točka B predviđa $1{,}20\ \text{N}$ umjesto $0{,}60\ \text{N}$. A je usklađen s Newtonskim modelom u ispitanom rasponu; B nije. Podatci ne određuju jedinstven novi zakon ni ekstrapolaciju.

### Z6. Kapilarna igla pod tlakom {#key-task-u02-kapilarna-igla-unutarnjeg-promjera-spojena-je-na .unnumbered .unlisted}

[Vrati se na zadatak](u02_viskoznost_povrsinska_napetost_i_kapilarnost.qmd#task-u02-kapilarna-igla-unutarnjeg-promjera-spojena-je-na)

**Sažetak.** Kapilarna igla unutarnjeg promjera $d = 0{,}50\ \text{mm}$ spojena je na spremnik vode za koju vrijedi $\sigma = 0{,}072\ \text{N/m}$, $\rho = 998\ \text{kg/m}^3$ i $\theta = 0^\circ$. Izlaz je na visini $H = 42\ \text{mm}$ iznad široke…

**Smjernica postupka.** Prvo stanje: $h_{cap}=4\sigma\cos\theta/(\rho gd)$ i $p_{M,1}=\max(0,\rho gH-4\sigma\cos\theta/d)$. Drugo stanje: $p_{M,2}=\rho gH+4\sigma/D$. Te relacije opisuju različite oblike jedne međupovršine. Za izbor regulatora provjeri oba kraja intervala promjera.

**Kontrolni rezultat ili kriterij.** $h_{cap}\approx58{,}8\ \text{mm}$; $p_{M,1}=0\ \text{Pa}$. Nominalno $p_{M,2}\approx0{,}571\ \text{kPa}$; interval je $0{,}555$–$0{,}591\ \text{kPa}$, s maksimumom pri $D_{min}$. Raspon do $0{,}50\ \text{kPa}$ nije dovoljan; do $0{,}60\ \text{kPa}$ pokriva zadana stanja uz najmanju rezervu $8{,}8\ \text{Pa}$. Formirana kapljica nema dodatni konkavni meniskus čiji bi tlak smanjio zahtjev. Prijelaz i protočni gubitci nisu provjereni.

## Hidrostatička raspodjela tlaka i manometrija

### Z1. Tlak u otvorenom spremniku {#key-task-u03-otvoreni-spremnik-s-vodom-ima-slobodnu-povrsinu .unnumbered .unlisted}

[Vrati se na zadatak](u03_hidrostaticka_raspodjela_tlaka_i_manometrija.qmd#task-u03-otvoreni-spremnik-s-vodom-ima-slobodnu-povrsinu)

**Sažetak.** Otvoreni spremnik s vodom ima slobodnu površinu na atmosferskom tlaku. Odredi apsolutni i manometarski tlak u točki koja se nalazi na dubini $h = 2{,}40\ \text{m}$ ako je $p_{atm} = 100{,}8\ \text{kPa}$ i $\rho = 998\ \text{kg/m}^3$.

**Smjernica postupka.** manometarski tlak je $p_M = \rho gh$, a apsolutni $p_{aps} = p_{atm} + p_M$.

**Kontrolni rezultat ili kriterij.** $p_M \approx 23{,}5\ \text{kPa}$; $p_{aps} \approx 124{,}3\ \text{kPa}$.

### Z2. Razina vode iz razlike tlakova {#key-task-razina-vode-iz-razlike-tlakova .unnumbered .unlisted}

[Vrati se na zadatak](u03_hidrostaticka_raspodjela_tlaka_i_manometrija.qmd#task-razina-vode-iz-razlike-tlakova)

**Sažetak.** U zatvorenom spremniku s vodom gustoće $\rho = 998\ \text{kg/m}^3$ tlak se mjeri u točki `A` uz dno i u plinskom prostoru `G`. Razlika tlakova iznosi $\Delta p = p_A-p_G = 17{,}62\ \text{kPa}$. Oba se tlaka odnose izravno na označene…

**Smjernica postupka.** Zapiši tlak u `A` polazeći od tlaka plina. Oduzmi $p_G$ pa iz preostale hidrostatičke razlike odredi visinu.

**Kontrolni rezultat ili kriterij.** $h \approx 1{,}80\ \text{m}$. Pri zadanoj promjeni tlaka plina oba tlaka porastu za $5{,}0\ \text{kPa}$, pa $\Delta p$ ostaje $17{,}62\ \text{kPa}$.

### Z3. U-manometar s uljem i živom {#key-task-u03-cjevovod-s-uljem-gustoce-spojen-je-na .unnumbered .unlisted}

[Vrati se na zadatak](u03_hidrostaticka_raspodjela_tlaka_i_manometrija.qmd#task-u03-cjevovod-s-uljem-gustoce-spojen-je-na)

**Sažetak.** Cjevovod s uljem gustoće $\rho_u = 860\ \text{kg/m}^3$ spojen je na otvoreni U-manometar sa živom gustoće $\rho_{Hg} = 13600\ \text{kg/m}^3$. Razlika razina žive iznosi $\Delta h = 0{,}185\ \text{m}$; razina u otvorenom kraku viša je od…

**Smjernica postupka.** kreni od slobodne površine otvorenog kraka; niz stupce piši promjene tlaka kao $\rho g\Delta h$ uz točan znak.

**Kontrolni rezultat ili kriterij.** $p_M \approx 23{,}7\ \text{kPa}$.

### Z4. Debljina sloja ulja iz tlaka {#key-task-debljina-sloja-ulja-iz-tlaka .unnumbered .unlisted}

[Vrati se na zadatak](u03_hidrostaticka_raspodjela_tlaka_i_manometrija.qmd#task-debljina-sloja-ulja-iz-tlaka)

**Sažetak.** U otvorenom spremniku miruju dva nemješljiva sloja: ulje gustoće $\rho_u = 850\ \text{kg/m}^3$ iznad vode gustoće $\rho_w = 1000\ \text{kg/m}^3$. Ukupna visina tekućine iznad dna iznosi $H = 1{,}50\ \text{m}$, a manometarski tlak na dnu…

**Smjernica postupka.** Debljine slojeva moraju dati ukupnu visinu. Tlak na dnu dobiva se zbrajanjem dvaju hidrostatičkih doprinosa. Kao provjeru usporedi zadani tlak s tlakovima koje bi dala ista ukupna visina čistog ulja i čiste vode.

**Kontrolni rezultat ili kriterij.** $h_u \approx 0{,}601\ \text{m}$; $h_w \approx 0{,}899\ \text{m}$; $p_{M,granica} \approx 5{,}015\ \text{kPa}$. Obje su debljine pozitivne, a $12{,}508 < 13{,}830 < 14{,}715\ \text{kPa}$. Tlak je na ravnoj granici kontinuiran; nagib $dp/dh$ raste s $8{,}339$ na $9{,}810\ \text{kPa/m}$ pri ulasku iz ulja u vodu.

### Z5. Izbor manometra za podtlak {#key-task-izbor-manometra-za-podtlak .unnumbered .unlisted}

[Vrati se na zadatak](u03_hidrostaticka_raspodjela_tlaka_i_manometrija.qmd#task-izbor-manometra-za-podtlak)

**Sažetak.** U-manometrom otvorenim prema atmosferi treba mjeriti podtlak plina od nule do $p_{vak,max} = 6{,}00\ \text{kPa}$. Lokalni atmosferski tlak iznosi $p_{atm} = 98{,}6\ \text{kPa}$. Razmatraju se tri odvojene izvedbe ispunjene uljem gustoće…

**Smjernica postupka.** Kreni od atmosferskog tlaka i penjanja kroz manometarsku tekućinu prema strani podtlaka. Ista gustoća određuje i potrebnu visinu za zadani tlak i promjenu tlaka pri pogrešci visine. Provjeri oba ograničenja za svaki fluid.

**Kontrolni rezultat ili kriterij.** Za ulje, vodu i živu redom: $\Delta h \approx 0{,}711$; $0{,}613$; $0{,}04497\ \text{m}$, a granice tlačne pogreške su $8{,}44$; $9{,}79$; $133{,}42\ \text{Pa}$. Bira se **voda**: ulje traži preveliku razliku razina, a živa daje preveliku tlačnu pogrešku. Razina je viša u kraku spojenom s plinom; $p_{gas,aps} = 92{,}6\ \text{kPa}$. Veća gustoća skraćuje stupac, ali pri istoj pogrešci očitanja povećava tlačnu pogrešku.

### Z6. Tlak plina iz manometarskog mjerenja {#key-task-u03-zatvoreni-spremnik-s-vodom-ima-plinski-prostor .unnumbered .unlisted}

[Vrati se na zadatak](u03_hidrostaticka_raspodjela_tlaka_i_manometrija.qmd#task-u03-zatvoreni-spremnik-s-vodom-ima-plinski-prostor)

**Sažetak.** Zatvoreni spremnik s vodom ima plinski prostor nepoznatog apsolutnog tlaka. Bočni priključak na dubini $h_1 = 0{,}65\ \text{m}$ spojen je na otvoreni U-manometar sa živom gustoće $\rho_{Hg} = 13600\ \text{kg/m}^3$, pri čemu je razlika…

**Smjernica postupka.** iz otvorenog manometra najprije vrati tlak u priključku, zatim se penjanjem kroz vodu vrati na plinski prostor, a silaskom na dubinu $h_2$ dobije tlak u traženoj točki. Za konzervativnu gornju granicu istodobno uzmi najveće $p_{atm}$, $\Delta h$ i $h_2$, a najmanje $h_1$. Nakon toga primijeni zahtijevanu rezervu na mjerno područje; nominalna vrijednost sama nije dovoljna za izbor senzora.

**Kontrolni rezultat ili kriterij.** $p_{gas} \approx 122{,}6\ \text{kPa}$ (aps.); na dubini $1{,}30\ \text{m}$: $p \approx 135{,}3\ \text{kPa}$. Konzervativna gornja granica iznosi $p_{max}\approx136{,}05\ \text{kPa}$, pa uz rezervu od $5\ \%$ treba puna skala od najmanje $142{,}85\ \text{kPa}$. Pretvornik $0$--$140\ \text{kPa}$ nije dostatan; bira se područje $0$--$160\ \text{kPa}$.

## Relativno mirovanje fluida

### Z1. Slobodna površina pri ubrzanju {#key-task-u04-otvoreni-pravokutni-spremnik-duljine-i-pocetne-dubine .unnumbered .unlisted}

[Vrati se na zadatak](u04_relativno_mirovanje_fluida.qmd#task-u04-otvoreni-pravokutni-spremnik-duljine-i-pocetne-dubine)

**Sažetak.** Otvoreni pravokutni spremnik duljine $L = 1{,}80\ \text{m}$ i početne dubine vode $h_0 = 0{,}34\ \text{m}$ giba se vodoravno stalnim ubrzanjem $a = 1{,}20\ \text{m/s}^2$. Odredi razliku razina između krajeva spremnika, lokalne dubine uz…

**Smjernica postupka.** $\Delta h = aL/g$; zatim $h_{str} = h_0 + \Delta h/2$ i $h_{pred} = h_0 - \Delta h/2$; usporedi $h_{str}$ s $H$.

**Kontrolni rezultat ili kriterij.** $\Delta h \approx 0{,}22\ \text{m}$; $h_{str} \approx 0{,}45\ \text{m}$, $h_{pred} \approx 0{,}23\ \text{m}$; nema prelijevanja jer je $h_{str} < H$.

### Z2. Ubrzanje na granici prelijevanja {#key-task-u04-otvoreni-spremnik-duljine-napunjen-je-do-visine .unnumbered .unlisted}

[Vrati se na zadatak](u04_relativno_mirovanje_fluida.qmd#task-u04-otvoreni-spremnik-duljine-napunjen-je-do-visine)

**Sažetak.** Otvoreni pravokutni spremnik duljine $L = 1{,}40\ \text{m}$ napunjen je do visine $h_0 = 0{,}30\ \text{m}$, a visina boka je $H = 0{,}42\ \text{m}$. Odredi najveće vodoravno ubrzanje prije početka prelijevanja.

**Smjernica postupka.** u graničnom stanju vrijedi $h_{str} = H$ i $\Delta h = 2(H-h_0)$; nakon toga $a = g\Delta h/L$.

**Kontrolni rezultat ili kriterij.** $a_{max} \approx 1{,}68\ \text{m/s}^2$.

### Z3. Tlak pri vertikalnom ubrzanju {#key-task-u04-zatvoreni-vertikalni-cilindar-potpuno-ispunjen-uljem-gustoce .unnumbered .unlisted}

[Vrati se na zadatak](u04_relativno_mirovanje_fluida.qmd#task-u04-zatvoreni-vertikalni-cilindar-potpuno-ispunjen-uljem-gustoce)

**Sažetak.** Zatvoreni vertikalni cilindar potpuno ispunjen uljem gustoće $\rho = 870\ \text{kg/m}^3$ ima visinu stupca fluida $h = 0{,}75\ \text{m}$. Sustav ubrzava prema gore s $a_z = 2{,}3\ \text{m/s}^2$. Odredi razliku tlaka između dna i vrha…

**Smjernica postupka.** koristi efektivnu težinu fluida: $\Delta p = \rho (g+a_z)h$; za usporedbu u mirovanju uzmi $\Delta p_0 = \rho gh$. Os $z$ usmjeri prema gore; pri kočenju je $a_z<0$ iako je brzina još pozitivna.

**Kontrolni rezultat ili kriterij.** $\Delta p \approx 7{,}90\ \text{kPa}$; u mirovanju $\Delta p_0 \approx 6{,}40\ \text{kPa}$ — oko 23 % više. Pri gibanju prema gore uz kočenje $a_z=-2{,}3\ \text{m/s}^2$ dobiva se $\Delta p \approx 4{,}90\ \text{kPa}$. Gradijent određuje ubrzanje, a ne smjer brzine.

### Z4. Brzina vrtnje iz razlike tlakova {#key-task-vrtnja-iz-radijalne-razlike-tlakova .unnumbered .unlisted}

[Vrati se na zadatak](u04_relativno_mirovanje_fluida.qmd#task-vrtnja-iz-radijalne-razlike-tlakova)

**Sažetak.** Zatvorena cilindrična posuda potpuno je ispunjena vodom gustoće $\rho = 1000\ \text{kg/m}^3$ i vrti se stalnom brzinom oko okomite osi. Voda je dosegnula vrtnju krutoga tijela. Dva senzora u točkama `A` i `B` nalaze se na istoj visini, na…

**Smjernica postupka.** Na istoj visini poništava se gravitacijski doprinos. Integriraj radijalni gradijent tlaka između $r_A$ i $r_B$, vodeći računa o kvadratu polumjera i pretvorbi milimetara u metre.

**Kontrolni rezultat ili kriterij.** $p_B-p_A = 1{,}60\ \text{kPa}$; $|\omega| \approx 7{,}91\ \text{rad/s}$; $n \approx 75{,}5\ \text{okr/min}$. Zajednički pomak reference ne mijenja razliku tlakova ni rezultat. Smjer vrtnje nije odrediv jer tlak ovisi o $\omega^2$.

### Z5. Je li se fluid smirio nakon ubrzanja? {#key-task-provjera-smirivanja-ubrzanog-fluida .unnumbered .unlisted}

[Vrati se na zadatak](u04_relativno_mirovanje_fluida.qmd#task-provjera-smirivanja-ubrzanog-fluida)

**Sažetak.** Otvoreni pravokutni spremnik na vozilu ima duljinu $L = 1{,}50\ \text{m}$, početnu dubinu vode $h_0 = 0{,}300\ \text{m}$ i visinu boka $H = 0{,}550\ \text{m}$. Vozilo nakon pokretanja ubrzava stalno udesno s $a = 2{,}00\ \text{m/s}^2$. Za…

**Smjernica postupka.** Najprije upotrijebi nagib slobodne površine i očuvanje volumena. Zatim odvojeno provjeri blizinu predviđenim razinama i promjenjivost kroz vrijeme; jedna podudarna točka ili prosjek nisu dovoljni.

**Kontrolni rezultat ili kriterij.** Referentne dubine: $h_{str}\approx0{,}45291$ m, $h_{pred}\approx0{,}14709$ m. Niz I: najveće odstupanje 72,91 mm, raspon 140 mm; ne prolazi. Niz II: odstupanje 1,095 mm, raspon 2,0 mm; prolazi oba kriterija. Referentni profil je ispod boka. Očitanja ipak ne dokazuju mirovanje cijelog fluida ni izostanak prolaznog prelijevanja; treba pratiti slobodnu površinu i relativno gibanje kroz vrijeme.

### Z6. Rotirajući spremnik i prelijevanje {#key-task-u04-otvoreni-cilindricni-spremnik-polumjera-i-visine-ispunjen .unnumbered .unlisted}

[Vrati se na zadatak](u04_relativno_mirovanje_fluida.qmd#task-u04-otvoreni-cilindricni-spremnik-polumjera-i-visine-ispunjen)

**Sažetak.** Otvoreni cilindrični spremnik polumjera $R = 0{,}32\ \text{m}$ i visine $H = 0{,}62\ \text{m}$ ispunjen je vodom do početne srednje visine $h_0 = 0{,}46\ \text{m}$. Odredi najveću kutnu brzinu pri kojoj još nema prelijevanja. Zatim za…

**Smjernica postupka.** u graničnom stanju vrijedi $h_{rub} = H = h_0 + \omega_{max}^2 R^2/(4g)$; za radni režim najprije nađi $\Delta h = \omega^2 R^2/(2g)$, zatim $h_{osa}$ i $h_{rub}$, a tlakove iz $p_M = \rho gh$. U provjeri tolerancije koristi $\omega=1{,}05\alpha\omega_{max}$ i iz uvjeta $h_{osa}\ge0{,}350\ \text{m}$ riješi gornju granicu za $\alpha$.

**Kontrolni rezultat ili kriterij.** $\omega_{max}\approx7{,}83$ rad/s. Za $\alpha=0{,}80$: dubine (os, rub) ≈ (0,3576; 0,5624) m, tlakovi ≈ (3,51; 5,52) kPa. Uz +5 % brzine: omjer 0,84, dubine ≈ (0,3471; 0,5729) m; nema prelijevanja, ali dubina u osi nije dovoljna. $\alpha_{max}\approx0{,}790$. Preporuka $\alpha=0{,}78$: pri najvećem odstupanju dubine ≈ (0,35268; 0,56732) m, rezerva 2,68 mm. Vrijedi za ustaljeni model sa zatvorenim usisom.

## Hidrostatske sile na ravne i zakrivljene plohe

### Z1. Sila na pravokutni poklopac {#key-task-u05-ravna-pravokutna-zaklopka .unnumbered .unlisted}

[Vrati se na zadatak](u05_hidrostatske_sile_na_plohe.qmd#task-u05-ravna-pravokutna-zaklopka)

**Sažetak.** Vertikalni pravokutni poklopac širine $b=1{,}40\ \mathrm{m}$ i visine $H=1{,}80\ \mathrm{m}$ nalazi se u vodi tako da mu je gornji rub na dubini $h_1=1{,}10\ \mathrm{m}$. Odredite rezultantnu silu, dubinu centra tlaka i njegovu udaljenost…

**Smjernica postupka.** Najprije izračunajte $A$ i $h_C$. Za centar tlaka treba $I_G=bH^3/12$.

**Kontrolni rezultat ili kriterij.** $F=49{,}34\ \mathrm{kN}$; $h_{CP}=2{,}135\ \mathrm{m}$; udaljenost od gornjeg ruba $1{,}035\ \mathrm{m}$.

### Z2. Sila na zakrivljeni poklopac {#key-task-u05-zakrivljeni-poklopac-cetvrtine-kruga .unnumbered .unlisted}

[Vrati se na zadatak](u05_hidrostatske_sile_na_plohe.qmd#task-u05-zakrivljeni-poklopac-cetvrtine-kruga)

**Sažetak.** Zakrivljeni poklopac presjeka četvrtine kruga ima $R=0{,}65\ \mathrm{m}$ i širinu $b=1{,}20\ \mathrm{m}$. Gornja mu je točka na dubini $h_1=1{,}10\ \mathrm{m}$. Voda kvasi konveksnu vanjsku i donju stranu. Odredite $F_H$, predznačeni…

**Smjernica postupka.** Za $F_H$ rabite vertikalnu projekciju $Rb$ na dubini $h_1+R/2$. Pomoćni volumen čine pravokutni dio $h_1Rb$ i četvrtina valjka.

**Kontrolni rezultat ili kriterij.** $F_H=10{,}88\ \mathrm{kN}$; $F_V=+12{,}30\ \mathrm{kN}$ prema gore; $F_R=16{,}42\ \mathrm{kN}$.

### Z3. Pregrada između dviju razina vode {#key-task-pregrada-izmedu-dviju-razina-vode .unnumbered .unlisted}

[Vrati se na zadatak](u05_hidrostatske_sile_na_plohe.qmd#task-pregrada-izmedu-dviju-razina-vode)

**Sažetak.** Vertikalna nepropusna pregrada širine $b=1{,}20\ \mathrm{m}$ i visine $H=3{,}00\ \mathrm{m}$ dijeli dva otvorena spremnika. Dubina vode iznad zajedničkog dna lijevo je $h_L=2{,}40\ \mathrm{m}$, a desno $h_D=1{,}20\ \mathrm{m}$. Pregrada…

**Smjernica postupka.** Odvojeno nacrtajte dva trokutasta dijagrama manometarskog tlaka. Svaki daje silu na visini $h/3$ iznad dna. Sile i njihove momente oduzmite uz odgovarajuće predznake; krak spojnice jest $H$.

**Kontrolni rezultat ili kriterij.** $F_x=+25{,}377\ \mathrm{kN}$; $y_R=0{,}9333\ \mathrm{m}$ iznad dna; $M_A=-23{,}685\ \mathrm{kN\,m}$; $T=7{,}895\ \mathrm{kN}$ ulijevo u $B$. Provjera: pri jednakim razinama neto sila i moment su nula; zamjena lijeve i desne razine obrće njihove predznake.

### Z4. Širina trokutastog poklopca {#key-task-sirina-trokutastog-poklopca .unnumbered .unlisted}

[Vrati se na zadatak](u05_hidrostatske_sile_na_plohe.qmd#task-sirina-trokutastog-poklopca)

**Sažetak.** Vertikalni poklopac ima oblik jednakokračnog trokuta s vrhom gore, visinom $H=1{,}50\ \mathrm{m}$ i vodoravnom osnovicom širine $b$. Vrh je na dubini $h_0=0{,}40\ \mathrm{m}$ ispod slobodne površine vode; s druge strane je zrak na…

**Smjernica postupka.** Za trokut s vrhom gore vrijedi $A=bH/2$, $h_C=h_0+2H/3$ i $I_G=bH^3/36$ oko vodoravne težišne osi. Uporabite $F\le F_{\max}$; zatim provjerite ovisi li $h_{CP}$ o širini.

**Kontrolni rezultat ili kriterij.** $b_{\max}=1{,}1673\ \mathrm{m}$; $h_{CP}=1{,}4893\ \mathrm{m}$. Za $b=1{,}20\ \mathrm{m}$ sila je $F=12{,}336\ \mathrm{kN}>F_{\max}$, pa ponuđena širina ne zadovoljava. Pri zadanim $H$ i $h_0$, $h_{CP}$ ne ovisi o $b$.

### Z5. Radijalni poklopac s težinom {#key-task-radijalni-poklopac-s-tezinom .unnumbered .unlisted}

[Vrati se na zadatak](u05_hidrostatske_sile_na_plohe.qmd#task-radijalni-poklopac-s-tezinom)

**Sažetak.** Kruti sklop četvrtcilindričnog poklopca i njegovih krakova okreće se oko osi kroz središte kružnice $O$, a ne oko kraja luka. Voda kvasi konveksnu lijevu i donju stranu, a s druge strane je zrak na atmosferskom tlaku. U presjeku s…

**Smjernica postupka.** Nacrtajte jednu lokalnu tlačnu normalu i provjerite njezin pravac prema $O$. Za ravnotežu izdvojite cijeli kruti sklop; tek nakon momentne jednadžbe zatvorite ravnotežu sila. Zasebno provjerite predznak i kapacitet spojnice.

**Kontrolni rezultat ili kriterij.** $F_x=+11{,}089\ \mathrm{kN}$; $F_y=+13{,}713\ \mathrm{kN}$; $M_{O,\mathrm{voda}}=0$. $T=0{,}904\ \mathrm{kN}$ ulijevo, manje od $T_{\max}$; $R_{Ox}=-10{,}185\ \mathrm{kN}$, $R_{Oy}=-11{,}313\ \mathrm{kN}$. Sve tlačne normale prolaze kroz $O$; $T=W|x_G|/R$ ne ovisi o $h_1$ u zadanom modelu.

### Z6. Nesigurnost sile na mjerni panel {#key-task-u05-nesigurnost-modela-i-mjerenja .unnumbered .unlisted}

[Vrati se na zadatak](u05_hidrostatske_sile_na_plohe.qmd#task-u05-nesigurnost-modela-i-mjerenja)

**Sažetak.** Pravokutni mjerni panel ima točno poznate dimenzije $b=1{,}20\ \mathrm{m}$ i $H=0{,}80\ \mathrm{m}$. Gornji rub je na izmjerenoj dubini $h_1=0{,}90\ \mathrm{m}$ sa standardnom nesigurnošću $u(h_1)=0{,}020\ \mathrm{m}$, a gustoća je…

**Smjernica postupka.** Za $F=\rho gbH(h_1+H/2)$ relativna nesigurnost zbog dvaju nesigurnih ulaza jest $u(F)/F=\sqrt{[u(\rho)/\rho]^2+[u(h_1)/(h_1+H/2)]^2}$.

**Kontrolni rezultat ili kriterij.** $F=12{,}218\ \mathrm{kN}$; $u(F)=0{,}192\ \mathrm{kN}$; kombinirana nesigurnost razlike $0{,}356\ \mathrm{kN}$; $z=1{,}74$. Budući da je $z<2$, ovaj skup podataka ne pokazuje neslaganje na zadanoj razini, ali time model nije općenito validiran.

## Uzgon, plivanje i početni stabilitet

### Z1. Uzgon potpuno uronjenog tijela {#key-task-u07-hermeticki-zatvoreno-tijelo-volumena-i-mase-potpuno .unnumbered .unlisted}

[Vrati se na zadatak](u06_uzgon_plivanje_i_stabilnost.qmd#task-u07-hermeticki-zatvoreno-tijelo-volumena-i-mase-potpuno)

**Sažetak.** Hermetički zatvoreno tijelo volumena $V = 0{,}085\ \text{m}^3$ i mase $m = 62\ \text{kg}$ potpuno je uronjeno u vodu gustoće $\rho = 998\ \text{kg/m}^3$. Odredi silu uzgona i silu koju treba primijeniti da tijelo ostane potpuno uronjeno i…

**Smjernica postupka.** uzgon je $F_U = \rho gV$; potom usporedi $F_U$ i težinu $G = mg$ da dobiješ potrebnu dodatnu silu.

**Kontrolni rezultat ili kriterij.** $F_U \approx 832\ \text{N}$; kako je $F_U > G = 608\ \text{N}$, treba dodatna sila prema dolje $\approx 224\ \text{N}$.

### Z2. Gaz opterećenog pontona {#key-task-u07-pravokutni-radni-ponton-duljine-sirine-i-visine .unnumbered .unlisted}

[Vrati se na zadatak](u06_uzgon_plivanje_i_stabilnost.qmd#task-u07-pravokutni-radni-ponton-duljine-sirine-i-visine)

**Sažetak.** Pravokutni radni ponton duljine $L = 2{,}60\ \text{m}$, širine $B = 1{,}40\ \text{m}$ i visine boka $H = 0{,}38\ \text{m}$ ima vlastitu masu $m_p = 510\ \text{kg}$. Na njega se simetrično postavlja teret mase $m_t = 220\ \text{kg}$.…

**Smjernica postupka.** iz vertikalne ravnoteže vrijedi $\rho gV_{ist} = (m_p + m_t)g$; srednji gaz slijedi iz $V_{ist} = LBh$.

**Kontrolni rezultat ili kriterij.** $V_{ist} \approx 0{,}73\ \text{m}^3$; srednji gaz $h \approx 0{,}20\ \text{m}$; dodatna masa do ruba $\approx 650\ \text{kg}$.

### Z3. Metacentarska visina iz pokusa nagibanja {#key-task-metacentarska-visina-iz-pokusa-nagibanja .unnumbered .unlisted}

[Vrati se na zadatak](u06_uzgon_plivanje_i_stabilnost.qmd#task-metacentarska-visina-iz-pokusa-nagibanja)

**Sažetak.** Pri nastavnom pokusu na zatvorenom pravokutnom pontonu pomicanjem utega određuje se početna metacentarska visina. Ponton u mirnoj vodi najprije stoji uspravno, a teret je na osi simetrije. Duljina je $L=3{,}00\ \text{m}$, širina…

**Smjernica postupka.** Iz momentne ravnoteže $m_s e=mGM\tan\varphi$ najprije odredi izmjereni $GM$. Zatim primijeni $KG=KB+BM-GM$, uz $KB=h_m/2$ i $BM=B^2/(12h_m)$. U linearnom modelu rubni gazovi su $h_m\pm(B/2)\tan\varphi$.

**Kontrolni rezultat ili kriterij.** $h_m=0{,}2863\ \text{m}$; $GM=0{,}5724\ \text{m}$; $KG=0{,}1412\ \text{m}$. Gazovi su $h_L=0{,}2496\ \text{m}$ i $h_D=0{,}3230\ \text{m}$: oba su između $0$ i $H$. Kut $3^\circ<5^\circ$ zadovoljava zadani kriterij; pozitivan $GM$ dokazuje samo početni stabilitet.

### Z4. Gustoća ulja iz očitanja areometra {#key-task-u07-areometar-mase-s-cilindricnim-vratom-promjera-pluta .unnumbered .unlisted}

[Vrati se na zadatak](u06_uzgon_plivanje_i_stabilnost.qmd#task-u07-areometar-mase-s-cilindricnim-vratom-promjera-pluta)

**Sažetak.** Areometar mase $m = 0{,}085\ \text{kg}$ s cilindričnim vratom promjera $d = 8\ \text{mm}$ pluta u referentnoj vodi gustoće $\rho_w=1000\ \text{kg/m}^3$ tako da je uronjena duljina cilindričnog vrata $h_1 = 82\ \text{mm}$, a u nepoznatom…

**Smjernica postupka.** u oba fluida vrijedi $\rho gV_{ist} = mg$; razlika je samo u uronjenom volumenu vrata i tijela areometra.

**Kontrolni rezultat ili kriterij.** $\rho_{ulje} \approx 992{,}4\ \text{kg/m}^3$; uron je veći jer je ulje rjeđe pa je za istu težinu potreban veći istisnuti volumen.

### Z5. Spuštanje opreme ili dodavanje balasta {#key-task-spustanje-opreme-ili-dodavanje-balasta .unnumbered .unlisted}

[Vrati se na zadatak](u06_uzgon_plivanje_i_stabilnost.qmd#task-spustanje-opreme-ili-dodavanje-balasta)

**Sažetak.** Na zatvorenom pravokutnom pontonu razmatraju se dvije odvojene preinake radi povećanja početnog stabiliteta. Sva oprema i balast postavljaju se simetrično, pa se računa uspravno stanje u mirnoj vodi. Ponton ima $L=3{,}00\ \text{m}$…

**Smjernica postupka.** Za svaki plan ponovno zatvori ukupnu masu i njezin vertikalni moment. Spuštanje opreme čuva masu; dodani balast mijenja i istisninu, $KB$ i $BM$. Dva uvjeta provjeri zasebno.

**Kontrolni rezultat ili kriterij.** Početno: $(h,f,KG,GM)=(0{,}2227;0{,}3773;0{,}8000;0{,}1534)\ \text{m}$. Plan A: $(0{,}2227;0{,}3773;0{,}6800;0{,}2734)\ \text{m}$, prihvatljiv. Plan B: $(0{,}3563;0{,}2437;0{,}5188;0{,}1857)\ \text{m}$, ne zadovoljava oba uvjeta. Balast snižava $KG$, ali smanjuje i $BM$ te slobodni bok $f=H-h$.

### Z6. Platforma na granici ulja i vode {#key-task-u07-pravokutna-servisna-platforma-duljine-i-sirine-pluta .unnumbered .unlisted}

[Vrati se na zadatak](u06_uzgon_plivanje_i_stabilnost.qmd#task-u07-pravokutna-servisna-platforma-duljine-i-sirine-pluta)

**Sažetak.** Pravokutna servisna platforma duljine $L = 2{,}80\ \text{m}$ i širine $B = 1{,}20\ \text{m}$ pluta na granici ulja gustoće $\rho_o = 820\ \text{kg/m}^3$ debljine $\delta = 0{,}08\ \text{m}$ i vode gustoće $\rho_w = 998\ \text{kg/m}^3$.…

**Smjernica postupka.** najprije uzmi $h_m=(h_L+h_D)/2$ i $m_\Delta=\rho_oV_o+\rho_wV_w$. Za položaje uzgonskih doprinosa vrijedi $z_{B,o}=h_m-\delta/2$ i $z_{B,w}=(h_m-\delta)/2$, pa izračunaj $KB_{eq}$ njihovim uzgonskim težinjenjem. U ovom modelu $BM_{eq}=\rho_w I_T/m_\Delta$, gdje je $I_T=LB^3/12$, a $GM_{eq}=KB_{eq}+BM_{eq}-KG$. Tek zatim primijeni $m_a e=m_\Delta GM_{eq}\tan\theta$ i $\tan\theta=(h_L-h_D)/B$. Za konzervativni omotač izračunaj svih $2^5=32$ rubnih kombinacija pet nesigurnih skalarnih ulaza.

**Kontrolni rezultat ili kriterij.** $h_m=0{,}220\ \text{m}$; $(V_o,V_w)=(0{,}269;0{,}470)\ \text{m}^3$; $m_\Delta=689{,}9\ \text{kg}$; $y_B=0{,}0389\ \text{m}$. $(KB_{eq},BM_{eq},GM_{eq})=(0{,}105;0{,}583;0{,}488)\ \text{m}$. $e=0{,}321\ \text{m}$ ulijevo; $e_{max}=0{,}3546\ \text{m}>0{,}34\ \text{m}$: raspored se ne prihvaća. Sve rubne kombinacije imaju $\delta<h_L,h_D<H$ i $|\theta|<5^\circ$.

## Kinematika, kontrolni volumen i kontinuitet

### Z1. Protok kroz proširenje cijevi {#key-task-u08-voda-struji-kroz-cijev-koja-se-siri .unnumbered .unlisted}

[Vrati se na zadatak](u07_kinematika_kontrolni_volumen_i_kontinuitet.qmd#task-u08-voda-struji-kroz-cijev-koja-se-siri)

**Sažetak.** Voda struji kroz cijev koja se širi s promjera $D_1 = 0{,}10\ \text{m}$ na $D_2 = 0{,}16\ \text{m}$. Ako je ulazna srednja brzina $v_1 = 4{,}8\ \text{m/s}$, a gustoća vode $\rho = 998\ \text{kg/m}^3$, odredi izlaznu brzinu, volumenski…

**Smjernica postupka.** najprije $Q = A_1 v_1$, zatim $v_2 = Q/A_2$ i na kraju $\dot m = \rho Q$.

**Kontrolni rezultat ili kriterij.** $Q \approx 37{,}7\ \text{L/s}$; $v_2 \approx 1{,}88\ \text{m/s}$; $\dot m \approx 37{,}6\ \text{kg/s}$.

### Z2. Protok kroz kosu kontrolnu plohu {#key-task-protok-kroz-kosu-kontrolnu-plohu .unnumbered .unlisted}

[Vrati se na zadatak](u07_kinematika_kontrolni_volumen_i_kontinuitet.qmd#task-protok-kroz-kosu-kontrolnu-plohu)

**Sažetak.** U širokom toku vode odabrana je nepomična zamišljena ravna ploha površine $A=0{,}0040\ \text{m}^2$. Brzina vode jednolika je na toj plohi i iznosi $v=3{,}0\ \text{m/s}$. Kut između brzine i odabrane jedinične normale $\vec n$ iznosi…

**Smjernica postupka.** Protok određuje normalna komponenta brzine: $Q=Av\cos\alpha$. Kut je zadan prema normali, a ne prema samoj plohi.

**Kontrolni rezultat ili kriterij.** $v_n=1{,}50\ \text{m/s}$; $Q=+6{,}00\ \text{L/s}$; $\dot m=+5{,}988\ \text{kg/s}$. Za suprotnu normalu protoci su $-6{,}00\ \text{L/s}$ i $-5{,}988\ \text{kg/s}$; fizički tok ostaje isti.

### Z3. Bilanca komore za miješanje {#key-task-u08-u-komoru-za-mijesanje-ulaze-dvije-vodene .unnumbered .unlisted}

[Vrati se na zadatak](u07_kinematika_kontrolni_volumen_i_kontinuitet.qmd#task-u08-u-komoru-za-mijesanje-ulaze-dvije-vodene)

**Sažetak.** U stacionarnu komoru ulaze dvije vodene struje protoka $Q_1=12\ \text{L/s}$ i $Q_2=8\ \text{L/s}$. Jedini izlaz ima promjer $D_3=120\ \text{mm}$. Odredi izlaznu srednju brzinu i napiši masenu bilancu; nema akumulacije ni drugih priključaka.

**Smjernica postupka.** za stacionarnu mješalicu vrijedi $\dot m_1 + \dot m_2 = \dot m_3$; za vodu je dovoljno računati preko volumenskih protoka.

**Kontrolni rezultat ili kriterij.** $Q_3 = 20\ \text{L/s}$; $v_3 \approx 1{,}77\ \text{m/s}$.

### Z4. Raspodjela protoka u dvije grane {#key-task-u08-u-razdjelnu-glavu-ulazi-voda-protokom-kroz .unnumbered .unlisted}

[Vrati se na zadatak](u07_kinematika_kontrolni_volumen_i_kontinuitet.qmd#task-u08-u-razdjelnu-glavu-ulazi-voda-protokom-kroz)

**Sažetak.** U razdjelnu glavu ulazi voda protokom $Q = 0{,}030\ \text{m}^3/\text{s}$ kroz cijev promjera $D_1 = 140\ \text{mm}$. Voda izlazi kroz dvije grane promjera $D_2 = 90\ \text{mm}$ i $D_3 = 70\ \text{mm}$, pri čemu je zadano da je brzina u…

**Smjernica postupka.** postavi $Q = Q_2 + Q_3$ i vezu brzina $v_2 = 2v_3$; preko $Q = Av$ zatvori sustav za dvije nepoznanice.

**Kontrolni rezultat ili kriterij.** $v_3 \approx 1{,}81\ \text{m/s}$, $v_2 \approx 3{,}62\ \text{m/s}$; $Q_2 \approx 23{,}0\ \text{L/s}$, $Q_3 \approx 7{,}0\ \text{L/s}$.

### Z5. Klip s protočnim otvorom {#key-task-klip-s-protocnim-otvorom .unnumbered .unlisted}

[Vrati se na zadatak](u07_kinematika_kontrolni_volumen_i_kontinuitet.qmd#task-klip-s-protocnim-otvorom)

**Sažetak.** Vodom ispunjena vodoravna dozirna komora ima nepomični cilindar i klip koji se pomiče udesno. Voda ulazi kroz nepomični lijevi priključak, a izlazi kroz središnji otvor u klipu. Klip brtvi uz cilindar; nema drugih tokova ni zračnog džepa.…

**Smjernica postupka.** Promjenjivi volumen komore je $V=A_p\ell(t)$, gdje je $A_p=\pi D^2/4$. Kroz izlaznu plohu vezanu uz klip prolazi $Q_{out,rel}=A_o w$, uz $A_o=\pi d^2/4$. Zatvori akumulaciju mase u komori; zatim poveži apsolutnu i relativnu brzinu. Za zaustavljeni klip akumulacija mora nestati.

**Kontrolni rezultat ili kriterij.** $Q_{out,rel}=0{,}4712\ \text{L/s}$; $u=0{,}06732\ \text{m/s}$ udesno; $v_{out}=1{,}5673\ \text{m/s}$. Vrijeme hoda $t=1{,}7824\ \text{s}$; porast mase $\Delta m=0{,}9406\ \text{kg}$. Za $u=0$ nužno je $w=3{,}1831\ \text{m/s}$; isti dotok i prvotna vrijednost $w$ ne mogu se zadržati bez promjene modela.

### Z6. Bilanca spremnika s dvama fluidima {#key-task-u08-mijesajuci-spremnik-tlocrtne-povrsine-prima-vodu-gustoce .unnumbered .unlisted}

[Vrati se na zadatak](u07_kinematika_kontrolni_volumen_i_kontinuitet.qmd#task-u08-mijesajuci-spremnik-tlocrtne-povrsine-prima-vodu-gustoce)

**Sažetak.** U spremniku za pripremu slane otopine dva dotoka ulaze u homogenu mješavinu. Izlazni je protok manji od ukupnog dotoka pa razina raste. Treba provjeriti koliko se tekućine zadrži u spremniku i dopušta li raspoloživi slobodni bok šest…

**Smjernica postupka.** najprije izračunaj $Q_3 = A_3 v_3$, zatim gustoću mješavine iz masene bilance ulaza, a član akumulacije zatvori preko $Q_A + Q_B - Q_3 = A_T\,dh/dt$. Za najveći porast razine uzmi oba ulazna protoka na gornjoj, a izlaznu brzinu na donjoj granici. Najdulje trajanje slijedi iz $t_{max}=h_{slob}/(dh/dt)_{max}$.

**Kontrolni rezultat ili kriterij.** $Q_3=8{,}042\ \text{L/s}$; $\rho_{mix}=1021{,}3\ \text{kg/m}^3$; $dh/dt=1{,}450\ \text{mm/s}$; $\Delta m\approx2558\ \text{kg}$ za 6 min nominalno. Najveći rast prije ruba je $1{,}604\ \text{mm/s}$, a vrijeme do ruba $349{,}0\ \text{s}$. Šest minuta ne zadovoljava kriterij. Ekstrapoliranih $0{,}5774\ \text{m}>0{,}560\ \text{m}$ pokazuje manjak boka $17{,}4\ \text{mm}$; nakon ruba voda se prelijeva.

## Energijska jednadžba i Bernoulli

### Z1. Istjecanje iz otvorenog spremnika {#key-task-u09-veliki-otvoreni-spremnik-sadrzi-vodu-do-visine .unnumbered .unlisted}

[Vrati se na zadatak](u08_energijska_jednadzba_i_bernoulli.qmd#task-u09-veliki-otvoreni-spremnik-sadrzi-vodu-do-visine)

**Sažetak.** Veliki otvoreni spremnik sadrži vodu do visine $H = 3{,}20\ \text{m}$ iznad osi male bočne sapnice promjera $d = 26\ \text{mm}$. Za vodu uzmi $\rho=998\ \text{kg/m}^3$. Promatraj kvazistacionarni trenutak dok se razina velikog spremnika…

**Smjernica postupka.** između slobodne površine i izlaza vrijedi Torricelli: $v = \sqrt{2gH}$; nakon toga $Q = Av$ i $\dot m = \rho Q$.

**Kontrolni rezultat ili kriterij.** $v \approx 7{,}92\ \text{m/s}$; $Q \approx 4{,}21\ \text{L/s}$; $\dot m \approx 4{,}20\ \text{kg/s}$.

### Z2. Tlak u suženju ventilacijskog kanala {#key-task-u09-horizontalnim-ventilacijskim-kanalom-smanjuje-se-presjek-s .unnumbered .unlisted}

[Vrati se na zadatak](u08_energijska_jednadzba_i_bernoulli.qmd#task-u09-horizontalnim-ventilacijskim-kanalom-smanjuje-se-presjek-s)

**Sažetak.** Horizontalnim ventilacijskim kanalom smanjuje se presjek s $A_1 = 0{,}060\ \text{m}^2$ na $A_2 = 0{,}020\ \text{m}^2$. Volumenski protok zraka iznosi $Q = 0{,}42\ \text{m}^3/\text{s}$, a gustoća zraka je $\rho = 1{,}20\ \text{kg/m}^3$.…

**Smjernica postupka.** iz kontinuiteta dobij $v_1$ i $v_2$, a za horizontalni kanal bez gubitaka vrijedi $p_1 + \rho v_1^2/2 = p_2 + \rho v_2^2/2$.

**Kontrolni rezultat ili kriterij.** $v_1 = 7{,}0\ \text{m/s}$, $v_2 = 21{,}0\ \text{m/s}$; $\Delta p \approx 235\ \text{Pa}$.

### Z3. Tlak u silaznom suženju {#key-task-tlak-u-silaznom-suzenju .unnumbered .unlisted}

[Vrati se na zadatak](u08_energijska_jednadzba_i_bernoulli.qmd#task-tlak-u-silaznom-suzenju)

**Sažetak.** Voda gustoće $\rho=1000\ \text{kg/m}^3$ stacionarno teče kroz glatko silazno suženje. U vodoravnom ulaznom presjeku 1 promjer je $D_1=120\ \text{mm}$, a u vodoravnom izlaznom presjeku 2 $D_2=70\ \text{mm}$. Os presjeka 1 nalazi se…

**Smjernica postupka.** Najprije iz protoka odredi obje brzine. U Bernoulliju zadrži razliku geodetskih visina. Usporedi doprinos spuštanja s doprinosom ubrzanja; tlak i HGL nisu ista veličina.

**Kontrolni rezultat ili kriterij.** $v_1\approx1{,}768\ \text{m/s}$; $v_2\approx5{,}197\ \text{m/s}$; $p_2-p_1\approx+7{,}680\ \text{kPa}$. Tlak raste jer doprinos spuštanja $19{,}620\ \text{kPa}$ nadmašuje doprinos ubrzanja $11{,}940\ \text{kPa}$. Tvrdnja nije općenito točna: u ovom idealnom toku pada HGL, dok statički tlak raste.

### Z4. Pitot s izdignutim senzorom {#key-task-pitot-s-izdignutim-senzorom .unnumbered .unlisted}

[Vrati se na zadatak](u08_energijska_jednadzba_i_bernoulli.qmd#task-pitot-s-izdignutim-senzorom)

**Sažetak.** Pitotova sonda okrenuta je otvorom prema jednolikoj struji vode gustoće $\rho=1000\ \text{kg/m}^3$. U neporemećenoj struji A, na visini otvora sonde, statički manometarski tlak iznosi $p_{M,A}=16{,}0\ \text{kPa}$. Sonda je potpuno…

**Smjernica postupka.** Očitanje u S prvo hidrostatički prenesi na visinu otvora sonde. Tek tada oduzmi statički tlak u A i primijeni Bernoullija između neporemećene struje i stagnacijske točke.

**Kontrolni rezultat ili kriterij.** Stagnacijski manometarski tlak je $p_{M,st}=35{,}772\ \text{kPa}$, a razlika prema statičkom tlaku $19{,}772\ \text{kPa}$. Lokalna brzina je $v\approx6{,}288\ \text{m/s}$. Zanemarivanje visine senzora dalo bi $v_{pog}=4{,}000\ \text{m/s}$, odnosno podcijenjenu brzinu.

### Z5. Odabir grla prema tlaku i mjernom signalu {#key-task-odabir-grla-prema-tlaku .unnumbered .unlisted}

[Vrati se na zadatak](u08_energijska_jednadzba_i_bernoulli.qmd#task-odabir-grla-prema-tlaku)

**Sažetak.** Kroz vodoravni mjerni sklop prolazi zadani stalni protok vode $Q=20{,}0\ \text{L/s}$ pri gustoći $\rho=1000\ \text{kg/m}^3$. Ulazni promjer je $D_1=100\ \text{mm}$, a apsolutni ulazni tlak $p_{1,abs}=150\ \text{kPa}$. Glatki zamjenjivi…

**Smjernica postupka.** Iz kontinuiteta izrazom za brzinu u grlu prijeđi s promjera na pad tlaka. Minimalni apsolutni tlak ograničava najveći dopušteni pad, a minimalni mjerni signal najmanji pad. Tek nakon određivanja obaju rubova intervala usporedi ponuđene promjere.

**Kontrolni rezultat ili kriterij.** Dopušteno je $43{,}183\ \text{mm}\le d\le52{,}328\ \text{mm}$, pa odgovara uložak od $50\ \text{mm}$. Za promjere $40$, $50$ i $60\ \text{mm}$ apsolutni tlakovi u grlu redom su $26{,}591$, $101{,}366$ i $128{,}225\ \text{kPa}$, a padovi tlaka $123{,}409$, $48{,}634$ i $21{,}775\ \text{kPa}$. Uložak od 40 mm krši tlačni prag, a onaj od 60 mm nema dovoljan mjerni signal. Granice su zaokružene; odluka se provjerava izvornim nejednakostima.

### Z6. Sifon i putanja izlaznog mlaza {#key-task-u09-idealni-sifon-promjera-prazni-otvoreni-spremnik-tako .unnumbered .unlisted}

[Vrati se na zadatak](u08_energijska_jednadzba_i_bernoulli.qmd#task-u09-idealni-sifon-promjera-prazni-otvoreni-spremnik-tako)

**Sažetak.** Sifon je prethodno napunjen vodom, a ulaz je uronjen. U kvazistacionarnom trenutku uzmi gustoću vode $\rho=1000\ \text{kg/m}^3$. Idealni sifon promjera $D = 70\ \text{mm}$ prazni otvoreni spremnik tako da je izlaz vodoravan i nalazi se…

**Smjernica postupka.** Bernoullijem između slobodne površine i izlaza vrati idealni $v$, između slobodne površine i vrha sifona vrati tlak, a domet mlaza zatvori kao vodoravno izbačeno tijelo s visine $1{,}2\ \text{m}$. Za izvedeni sustav koristi $v=\sqrt{2g\Delta z/(1+K_\Sigma)}$ i $p_C=p_{atm}-\rho g[z_C+(1+K_C)v^2/(2g)]$. Najmanji protok daje najveći $K_\Sigma$; najmanji tlak u vrhu provjeri konzervativnim kutovima zadanih intervala, ne samo nominalnim koeficijentima.

**Kontrolni rezultat ili kriterij.** Idealno: $v\approx7{,}14$ m/s, $Q\approx27{,}5$ L/s, $p_{C,abs}\approx59{,}1$ kPa, $x\approx3{,}53$ m. Uz gubitke nominalno je $Q\approx15{,}9$ L/s i $p_{C,abs}\approx65{,}9$ kPa; intervali su $Q\in[14{,}7;17{,}4]$ L/s i $p_{C,abs}\in[59{,}1;70{,}8]$ kPa. Tlačni zahtjev prolazi, ali protok od 15,0 L/s nije zajamčen. Smanjiti gubitke, povećati promjer ili suziti interval mjerenjem.

## Kompresibilni idealni tok

### Z1. Brzina zvuka u heliju {#key-task-brzina-zvuka-helium .unnumbered .unlisted}

[Vrati se na zadatak](u09_kompresibilni_idealni_tok.qmd#task-brzina-zvuka-helium)

**Sažetak.** Izračunaj brzinu zvuka u heliju pri $300\ \text{K}$ za $\gamma=1{,}667$ i $R=2077\ \text{J/(kg K)}$. Nacrtaj smjer širenja poremećaja.

**Kontrolni rezultat ili kriterij.** $a\approx1019\ \text{m/s}$.

### Z2. Machov broj u ventilacijskom vodu {#key-task-mach-ventilacija .unnumbered .unlisted}

[Vrati se na zadatak](u09_kompresibilni_idealni_tok.qmd#task-mach-ventilacija)

**Sažetak.** Zrak pri $20\ ^\circ\text{C}$ struji vodom $D=0{,}20\ \text{m}$ protokom $2{,}0\ \text{m}^3/\text{s}$. Odredi $Ma$ i obrazloži izbor modela.

**Kontrolni rezultat ili kriterij.** $Ma\approx0{,}186$.

### Z3. Stagnacijska temperatura zraka {#key-task-stagnacijska-temperatura .unnumbered .unlisted}

[Vrati se na zadatak](u09_kompresibilni_idealni_tok.qmd#task-stagnacijska-temperatura)

**Sažetak.** Za zrak pri $T=240\ \text{K}$ i $Ma=1{,}5$ izračunaj $T_0$. Zatim procijeni rezultat preko $v^2/(2c_p)$.

**Kontrolni rezultat ili kriterij.** $T_0=348\ \text{K}$.

### Z4. Kritični tlak pri prigušenju protoka {#key-task-priguseni-protok .unnumbered .unlisted}

[Vrati se na zadatak](u09_kompresibilni_idealni_tok.qmd#task-priguseni-protok)

**Sažetak.** Odredi kritični nizvodni tlak za zrak iz spremnika pri $p_0=8\ \text{bar(abs)}$. Ne računaj kapacitet ventila.

**Kontrolni rezultat ili kriterij.** $p^*\approx4{,}23\ \text{bar(abs)}$.

### Z5. Model protoka kroz konvergentnu sapnicu {#key-task-sapnica-model .unnumbered .unlisted}

[Vrati se na zadatak](u09_kompresibilni_idealni_tok.qmd#task-sapnica-model)

**Sažetak.** U konvergentnoj sapnici za zrak izmjereni su $p_0=600\pm3\ \text{kPa(abs)}$, $T_0=300\pm1\ \text{K}$ i prigušeni maseni protok $\dot m=0{,}0595\pm0{,}0006\ \text{kg/s}$. Geometrijski otvor ima površinu $A_g=50{,}0\ \text{mm}^2$, a…

**Smjernica postupka.** napiši prigušeni protok kao $\dot m=C_dA_{eff}K(p_0,T_0)$ i najprije iz mjerenja odredi samo produkt $C_dA_{eff}$. Za propagaciju upotrijebi relativne osjetljivosti $+1$ na $\dot m$, $-1$ na $A_{eff}$, $-1$ na $p_0$ i $+1/2$ na $T_0$.

**Kontrolni rezultat ili kriterij.** $C_dA_{eff}\approx42{,}50\ \text{mm}^2$; uz neovisno kalibrirano $A_{eff}$ slijedi $C_d\approx0{,}885$ i $u(C_d)\approx0{,}014$. Bez neovisne geometrijske ili protokovne kalibracije mjerenje određuje samo produkt, pa su $A_{eff}$ i $C_d$ neidentifikabilni zasebno.

### Z6. Provjera podataka o udarnom valu {#key-task-udarni-val-podaci .unnumbered .unlisted}

[Vrati se na zadatak](u09_kompresibilni_idealni_tok.qmd#task-udarni-val-podaci)

**Sažetak.** U zračnom kanalu mjereni su apsolutni statički tlakovi neposredno prije i poslije približno normalnoga vala: $p_1=80{,}0\pm0{,}4\ \text{kPa}$ i $p_2=360{,}0\pm1{,}8\ \text{kPa}$. Pitot-mjerenja daju ukupne tlakove $p_{01}=626\pm4\…

**Smjernica postupka.** iz $p_2/p_1=1+2\gamma(M_1^2-1)/(\gamma+1)$ najprije izoliraj $M_1$. Nesigurnost omjera statičkih tlakova propagiraj iz oba senzora; izmjereni omjer ukupnih tlakova usporedi s normalno-udarnom relacijom pri dobivenom $M_1$.

**Kontrolni rezultat ili kriterij.** $p_2/p_1=4{,}500$, $M_1=2{,}000\pm0{,}007$; teorijski $p_{02}/p_{01}=0{,}7209\pm0{,}0032$, a izmjereni omjer je $0{,}7204\pm0{,}0079$. Kombinirana standardna nesigurnost razlike iznosi $0{,}0085$, pa je normirana razlika samo oko $0{,}050$ i podaci su konzistentni s modelom normalnoga vala. Bez $p_{01}$ i $p_{02}$ statička mjerenja određuju $M_1$, ali ne mjere izravno pad ukupnog tlaka.

## Količina i moment količine gibanja

### Z1. Sila mlaza na nepomičnu ploču {#key-task-u11-vodeni-mlaz-promjera-izlazi-iz-sapnice-brzinom .unnumbered .unlisted}

[Vrati se na zadatak](u10_kolicina_i_moment_kolicine_gibanja.qmd#task-u11-vodeni-mlaz-promjera-izlazi-iz-sapnice-brzinom)

**Sažetak.** Vodeni mlaz promjera $d = 38\ \text{mm}$ izlazi iz sapnice brzinom $v = 22\ \text{m/s}$ i udara okomito na nepomičnu ravnu ploču. Odredi maseni protok i silu koju mlaz prenosi na ploču.

**Smjernica postupka.** $\dot m = \rho Av$; za ravnu ploču izlazna komponenta u osi mlaza je nula pa je $F = \dot m v$.

**Kontrolni rezultat ili kriterij.** $\dot m \approx 24{,}9\ \text{kg/s}$; $F \approx 548\ \text{N}$.

### Z2. Brzina mlaza iz izmjerene sile {#key-task-u11-mlaz-vode-udara-okomito-na-nepomicnu-plocu .unnumbered .unlisted}

[Vrati se na zadatak](u10_kolicina_i_moment_kolicine_gibanja.qmd#task-u11-mlaz-vode-udara-okomito-na-nepomicnu-plocu)

**Sažetak.** Mlaz vode udara okomito na nepomičnu ploču i sila na ploču iznosi $F = 310\ \text{N}$. Promjer mlaza je $d = 42\ \text{mm}$. Odredi brzinu mlaza i volumenski protok.

**Smjernica postupka.** iz relacije $F = \rho A v^2$ vrati $v$, a zatim $Q = Av$.

**Kontrolni rezultat ili kriterij.** $v \approx 15{,}0\ \text{m/s}$; $Q \approx 20{,}7\ \text{L/s}$.

### Z3. Sile na cijevno koljeno {#key-task-u11-horizontalno-koljeno-zakrece-tok-vode-za-bez .unnumbered .unlisted}

[Vrati se na zadatak](u10_kolicina_i_moment_kolicine_gibanja.qmd#task-u11-horizontalno-koljeno-zakrece-tok-vode-za-bez)

**Sažetak.** Horizontalno koljeno zakreće tok vode za $90^\circ$ bez promjene promjera. Cijev ima promjer $D = 100\ \text{mm}$, protok je $Q = 0{,}026\ \text{m}^3/\text{s}$, ulazni manometarski tlak $p_1 = 180\ \text{kPa}$, a izlazni $p_2 = 150\…

**Smjernica postupka.** iz $Q$ prvo dobij brzinu; zatim u x i y smjeru zbroji tlakove na presjecima i promjenu količine gibanja.

**Kontrolni rezultat ili kriterij.** $v \approx 3{,}31\ \text{m/s}$; komponente sile fluida na koljeno $F_x \approx 1{,}50\ \text{kN}$, $F_y \approx -1{,}26\ \text{kN}$; rezultanta $\approx 1{,}96\ \text{kN}$.

### Z4. Sile na T-račvu {#key-task-u11-t-racva-prima-vodu-kroz-ulaz-promjera .unnumbered .unlisted}

[Vrati se na zadatak](u10_kolicina_i_moment_kolicine_gibanja.qmd#task-u11-t-racva-prima-vodu-kroz-ulaz-promjera)

**Sažetak.** T-račva prima vodu kroz ulaz promjera $D_1 = 120\ \text{mm}$ s protokom $Q_1 = 0{,}030\ \text{m}^3/\text{s}$. U vodoravni izlaz promjera $D_2 = 80\ \text{mm}$ odlazi $Q_2 = 0{,}018\ \text{m}^3/\text{s}$, a ostatak izlazi okomito prema…

**Smjernica postupka.** kontinuitetom zatvori $Q_3$, zatim u svakoj osi napiši jednadžbu količine gibanja za cijelu račvu.

**Kontrolni rezultat ili kriterij.** $Q_3 = 12\ \text{L/s}$; reakcija nosača $\approx 2{,}39\ \text{kN}$ (pretežno u osi ulaza), okomita komponenta $\approx 37\ \text{N}$.

### Z5. Sila na konvergentnu mlaznicu {#key-task-u11-konvergentna-mlaznica-ima-ulazni-promjer-izlazni-promjer .unnumbered .unlisted}

[Vrati se na zadatak](u10_kolicina_i_moment_kolicine_gibanja.qmd#task-u11-konvergentna-mlaznica-ima-ulazni-promjer-izlazni-promjer)

**Sažetak.** Konvergentna mlaznica ima ulazni promjer $D_1 = 110\ \text{mm}$, izlazni promjer $D_2 = 45\ \text{mm}$ i protok vode $Q = 0{,}018\ \text{m}^3/\text{s}$. Ulazni manometarski tlak iznosi $p_1 = 240\ \text{kPa}$, a mlaz izlazi u atmosferu.…

**Smjernica postupka.** iz kontinuiteta dobij brzine u oba presjeka; zatim za unutarnji kontrolni volumen spoji tlak na ulazu i promjenu količine gibanja.

**Kontrolni rezultat ili kriterij.** $v_1 \approx 1{,}89\ \text{m/s}$, $v_2 \approx 11{,}3\ \text{m/s}$; sila u vijcima prirubnice $\approx 2{,}11\ \text{kN}$.

### Z6. Sile na Y-račvu {#key-task-u11-vodoravna-y-racva-prima-vodu-kroz-ulaz .unnumbered .unlisted}

[Vrati se na zadatak](u10_kolicina_i_moment_kolicine_gibanja.qmd#task-u11-vodoravna-y-racva-prima-vodu-kroz-ulaz)

**Sažetak.** Vodoravna Y-račva prima vodu kroz ulaz promjera $D_1 = 140\ \text{mm}$ pri protoku $Q_1 = 0{,}040\ \text{m}^3/\text{s}$ i ulaznom manometarskom tlaku $p_1 = 185\ \text{kPa}$. Šezdeset posto protoka odlazi ravno kroz izlaz promjera $D_2 =…

**Smjernica postupka.** najprije iz zadanog udjela vrati $Q_2$ i $Q_3$, zatim preko presjeka dobij brzine u svim granama, a na kraju po osima $x$ i $y$ napiši jednadžbu količine gibanja uz ulaznu tlaknu silu. Za omotač nesigurnosti izračunaj rezultantu u rubnim kombinacijama $p_1$, $Q_1$ i udjela protoka; zbog kvadratne ovisnosti članova količine gibanja nije dovoljno samo uvećati nominalnu rezultantu za jedan postotak.

**Kontrolni rezultat ili kriterij.** $Q_2 = 24\ \text{L/s}$, $Q_3 = 16\ \text{L/s}$; $F_x \approx 2{,}84\ \text{kN}$, $F_y \approx -44\ \text{N}$; rezultanta $\approx 2{,}84\ \text{kN}$. Rubne kombinacije daju najveću očekivanu rezultantu približno $2{,}92\ \text{kN}$. Zadani faktor daje kriterij od oko $3{,}36\ \text{kN}$, pa deklariranih $3{,}0\ \text{kN}$ ne zadovoljava taj pojedinačni kriterij, dok bi $3{,}5\ \text{kN}$ zadovoljilo samo tu usporedbu. Potpuni odabir traži zasebnu provjeru nosača, spojeva i svih kombinacija…

## Dimenzijska analiza i sličnost

### Z1. Reynoldsov broj u arterioli i vodovodu {#key-task-u14-krv-tece-arteriolom-promjera-brzinom-a-voda .unnumbered .unlisted}

[Vrati se na zadatak](u11_dimenzijska_analiza_i_slicnost.qmd#task-u14-krv-tece-arteriolom-promjera-brzinom-a-voda)

**Sažetak.** Krv teče arteriolom promjera $D = 0{,}3\ \text{mm}$ brzinom $v = 5\ \text{mm/s}$ ($\nu = 3{,}3 \cdot 10^{-6}\ \text{m}^2/\text{s}$), a voda gradskim vodom promjera $D = 0{,}3\ \text{m}$ brzinom $v = 1{,}5\ \text{m/s}$ ($\nu = 1{,}0 \cdot…

**Smjernica postupka.** $Re = vD/\nu$; za kružnu cijev usporedi s orijentacijskim područjima režima, bez prijenosa praga $2300$ na geometriju arteriole.

**Kontrolni rezultat ili kriterij.** $Re_{krv} \approx 0{,}45$ — viskoznost dominira; $Re_{voda} \approx 4{,}5 \cdot 10^5$ — inercija dominira.

### Z2. Machov broj i izbor modela {#key-task-u14-zrak-struji-vodom-promjera-lokalnim-volumenskim-protokom .unnumbered .unlisted}

[Vrati se na zadatak](u11_dimenzijska_analiza_i_slicnost.qmd#task-u14-zrak-struji-vodom-promjera-lokalnim-volumenskim-protokom)

**Sažetak.** Zrak struji vodom promjera $D = 100\ \text{mm}$ lokalnim volumenskim protokom $Q = 0{,}5\ \text{m}^3/\text{s}$; brzina zvuka $a = 340\ \text{m/s}$. Odredi brzinu i Machov broj te prosudi je li, bez velikih toplinskih i tlačnih promjena…

**Smjernica postupka.** $v=Q/A$, $Ma=v/a$; vrijednost $0{,}3$ uzmi kao orijentacijski prag.

**Kontrolni rezultat ili kriterij.** $v\approx63{,}7\ \text{m/s}$, $Ma\approx0{,}19$; prema zadanom kriteriju nestlačiva je aproksimacija razumna uz navedene dodatne pretpostavke.

### Z3. Kavitacijski broj na usisu crpke {#key-task-u14-na-referentnom-presjeku-usisa-crpke-apsolutni-tlak .unnumbered .unlisted}

[Vrati se na zadatak](u11_dimenzijska_analiza_i_slicnost.qmd#task-u14-na-referentnom-presjeku-usisa-crpke-apsolutni-tlak)

**Sažetak.** Na referentnom presjeku usisa crpke apsolutni tlak iznosi $p_{ref}=80\ \text{kPa}$, brzina $v_{ref}=4\ \text{m/s}$, gustoća vode $\rho=1000\ \text{kg/m}^3$, a tlak zasićene pare $p_v=2340\ \text{Pa}$. Ispitivanje iste crpke, pri istoj…

**Smjernica postupka.** koristi iste referentne veličine kao u definiciji kritične vrijednosti.

**Kontrolni rezultat ili kriterij.** $\sigma_{kav}\approx9{,}7>\sigma_{kr}=3{,}0$; prema zadanoj karakteristici crpka ima rezervu u toj radnoj točki.

### Z4. Weberov broj i raspad kapi {#key-task-u14-kap-goriva-promjera-izlozena-je-relativnoj-struji .unnumbered .unlisted}

[Vrati se na zadatak](u11_dimenzijska_analiza_i_slicnost.qmd#task-u14-kap-goriva-promjera-izlozena-je-relativnoj-struji)

**Sažetak.** Kap goriva promjera $d=0{,}15\ \text{mm}$ izložena je relativnoj struji zraka brzine $v=80\ \text{m/s}$ ($\rho_{zr}=1{,}2\ \text{kg/m}^3$, $\sigma=0{,}025\ \text{N/m}$). Za ovaj pojednostavljeni slučaj zanemari viskozne učinke i kao…

**Smjernica postupka.** izračunaj $We=\rho_{zr}v^2d/\sigma$ i usporedi ga sa zadanim pragom, ali odvoji „početak raspada” od „kvalitete atomizacije”.

**Kontrolni rezultat ili kriterij.** $We\approx46>12$; pojednostavljeni kriterij predviđa raspad, ali bez viskoznosti, omjera gustoća i modela sekundarnog raspada ne određuje raspodjelu veličina kapljica.

### Z5. Dimenzijska analiza otpuštanja vrtloga {#key-task-u14-frekvencija-otpustanja-vrtloga-iza-geometrijski-slicnog-tijela .unnumbered .unlisted}

[Vrati se na zadatak](u11_dimenzijska_analiza_i_slicnost.qmd#task-u14-frekvencija-otpustanja-vrtloga-iza-geometrijski-slicnog-tijela)

**Sažetak.** Frekvencija otpuštanja vrtloga $f$ iza geometrijski sličnog tijela ovisi o brzini neporemećene struje $v$, karakterističnoj duljini $D$, gustoći $\rho$ i dinamičkoj viskoznosti $\mu$. Buckinghamovim postupkom, uz ponavljajuće varijable…

**Smjernica postupka.** u popis uključi i zavisnu varijablu $f$; tek potom primijeni $n-k$. Nemoj unaprijed uvrstiti gotove definicije $St$ i $Re$.

**Kontrolni rezultat ili kriterij.** $n=5$, $k=3$, pa nastaju dvije grupe; izborom ponavljajućih varijabli dobivaju se $\Pi_1=fD/v=St$ i $\Pi_2=\rho vD/\mu=Re$, odnosno $St=\Phi(Re)$. Za zadani slučaj $Re=4{,}00\cdot10^4$ i $f=St\,v/D=45{,}6\ \text{Hz}$. Dimenzijska analiza određuje oblik ovisnosti, ali broj $St=0{,}190$ dolazi iz mjerenja ili odgovarajućega modela, ne iz samog Buckinghamova postupka.

### Z6. Sličnost modela preljeva brane {#key-task-u14-preljev-brane-ispituje-se-vodenim-modelom-u .unnumbered .unlisted}

[Vrati se na zadatak](u11_dimenzijska_analiza_i_slicnost.qmd#task-u14-preljev-brane-ispituje-se-vodenim-modelom-u)

**Sažetak.** Preljev brane ispituje se vodenim modelom u mjerilu $\lambda_L=30$, pri istom gravitacijskom ubrzanju i gustoći kao prototip. Prototip pri projektnom protoku ima brzinu preljeva $v_p=6{,}0\ \text{m/s}$ i protok $Q_p=480\…

**Smjernica postupka.** čuvaj $Fr$ te koristi $v_m=v_p/\sqrt{\lambda_L}$, $Q_m=Q_p/\lambda_L^{5/2}$ i, zbog jednake gustoće, $F_m=F_p/\lambda_L^3$. Zatim izračunaj $Re_m=v_mh_m/\nu$.

**Kontrolni rezultat ili kriterij.** $v_m\approx1{,}10\ \text{m/s}$; $Q_m\approx97{,}4\ \text{L/s}$; $F_m\approx8{,}15\ \text{N}$; $Re_m\approx2{,}7\cdot10^5$. Model je vjerojatno turbulentan, ali veličina viskozne mjerilne pogreške mora se provjeriti korekcijom otpora, nizom modelskih mjerila ili podatcima — ne slijedi samo iz oznake „turbulentno”.

## Diferencijalni opis realnog toka

### Z1. Lokalno i konvektivno ubrzanje {#key-task-materijalna-derivacija .unnumbered .unlisted}

[Vrati se na zadatak](u12_diferencijalni_opis_realnog_toka.qmd#task-materijalna-derivacija)

**Sažetak.** Za $u(x,t)=2t+x^2$ odredi lokalno, konvektivno i ukupno ubrzanje u $x=1\ \text{m}$, $t=2\ \text{s}$ uz konzistentne SI jedinice koeficijenata.

**Kontrolni rezultat ili kriterij.** $u=5\ \text{m/s}$, $a_{lok}=2$, $a_{kon}=10$, $a=12\ \text{m/s}^2$.

### Z2. Vrijeme viskozne difuzije {#key-task-viskozna-difuzija .unnumbered .unlisted}

[Vrati se na zadatak](u12_diferencijalni_opis_realnog_toka.qmd#task-viskozna-difuzija)

**Sažetak.** Procijeni vrijeme viskozne difuzije $t_\nu\sim H^2/\nu$ kroz sloj vode $H=10\ \text{mm}$ pri $20\ ^\circ\text{C}$, za $\nu=1{,}00\cdot10^{-6}\ \text{m}^2/\text{s}$. Obrazloži red veličine.

**Kontrolni rezultat ili kriterij.** $t_\nu\sim100\ \text{s}$.

### Z3. Viskoznost iz mjerenja u kapilari {#key-task-poiseuille-inverzni .unnumbered .unlisted}

[Vrati se na zadatak](u12_diferencijalni_opis_realnog_toka.qmd#task-poiseuille-inverzni)

**Sažetak.** U kapilari su izmjereni $Q=0{,}300\pm0{,}003\ \text{mL/min}$, $\Delta p=652\pm5\ \text{Pa}$, $L=0{,}200\pm0{,}001\ \text{m}$ i $D=0{,}500\pm0{,}005\ \text{mm}$. Fluid je Newtonski, gustoće $\rho=998\ \text{kg/m}^3$. Odredi dinamičku…

**Smjernica postupka.** invertiraj $Q=\pi D^4\Delta p/(128\mu L)$. Za neovisne ulaze vrijedi $[u(\mu)/\mu]^2=[4u(D)/D]^2+[u(\Delta p)/\Delta p]^2+[u(L)/L]^2+[u(Q)/Q]^2$.

**Kontrolni rezultat ili kriterij.** $\mu\approx1{,}000\ \text{mPa s}$, $u(\mu)\approx0{,}042\ \text{mPa s}$ i $Re\approx12{,}7$. Sam promjer doprinosi relativnoj nesigurnosti od $4\,\%$, pa dominira zadanim mjernim budžetom.

### Z4. Povratni tok između ploča {#key-task-couette-povrat .unnumbered .unlisted}

[Vrati se na zadatak](u12_diferencijalni_opis_realnog_toka.qmd#task-couette-povrat)

**Sažetak.** Newtonski fluid viskoznosti $\mu=0{,}100\ \text{Pa s}$ nalazi se između nepomične donje i gornje ploče koja se giba brzinom $U=2{,}00\ \text{m/s}$; razmak je $H=1{,}00\ \text{mm}$. Za potpuno razvijeni profil…

**Smjernica postupka.** deriviraj profil i postavi $\tau_0=\mu(du/dy)_{y=0}=0$; predznak gradijenta mora odgovarati nepovoljnom porastu tlaka u smjeru gibanja gornje ploče.

**Kontrolni rezultat ili kriterij.** $(dp/dx)_{krit}=4{,}00\cdot10^5\ \text{Pa/m}$; pri $0{,}90$ te vrijednosti $\tau_0=+20{,}0\ \text{Pa}$, a pri $1{,}10$ vrijedi $\tau_0=-20{,}0\ \text{Pa}$. Promjena predznaka zidnog naprezanja označuje početak lokalnog povratnog toka na donjoj stijenci.

### Z5. Izbor modela graničnog sloja {#key-task-granicni-sloj-model .unnumbered .unlisted}

[Vrati se na zadatak](u12_diferencijalni_opis_realnog_toka.qmd#task-granicni-sloj-model)

**Sažetak.** Voda pri $20\ ^\circ\text{C}$ ($\nu=1{,}00\cdot10^{-6}\ \text{m}^2/\text{s}$, $\rho=998\ \text{kg/m}^3$) struji uz nominalno ravnu plohu. U presjeku $x=0{,}400\ \text{m}$ izmjereno je $U_e=1{,}50\ \text{m/s}$ i $dU_e/dx=-0{,}250\…

**Smjernica postupka.** Blasius zahtijeva glatku plohu, laminaran tok i praktično nulti gradijent tlaka odnosno stalnu $U_e$. Negativan $dU_e/dx$ odgovara nepovoljnom gradijentu tlaka; procijeni i njegovu važnost prije odluke.

**Kontrolni rezultat ili kriterij.** $Re_x=6{,}00\cdot10^5$, $\delta_{99}\approx2{,}58\ \text{mm}$, $k_s/\delta_{99}\approx1{,}94\cdot10^{-3}$ i $(x/U_e)dU_e/dx=-0{,}0667$. Hrapavost je mala prema procijenjenoj debljini, ali mjerljiva promjena $U_e$ krši pretpostavku nultoga gradijenta tlaka, a stanje laminarnosti pri tom $Re_x$ nije dokazano; Blasius zato nije opravdan bez dodatne provjere profila i prijelaza.

### Z6. Konvergencija rješenja na trima mrežama {#key-task-cfd-tri-mreze .unnumbered .unlisted}

[Vrati se na zadatak](u12_diferencijalni_opis_realnog_toka.qmd#task-cfd-tri-mreze)

**Sažetak.** Za Poiseuilleov paket iz `data/cfd/poiseuille_laminar` tri mreže imaju omjer koraka $h/h_f=4,2,1$, protoke $Q=(8{,}16814;\ 7{,}93252;\ 7{,}87362)\cdot10^{-6}\ \text{m}^3/\text{s}$ i masene debalanse $(0{,}040;\ 0{,}010;\ 0{,}0025)\,\%$.…

**Smjernica postupka.** za $r=2$ koristi $p=\ln[(Q_c-Q_m)/(Q_m-Q_f)]/\ln r$, zatim $Q_{ext}=Q_f+(Q_f-Q_m)/(r^p-1)$ i $GCI_f=F_s|(Q_f-Q_m)/Q_f|/(r^p-1)$.

**Kontrolni rezultat ili kriterij.** $p\approx2{,}000$, $Q_{ext}\approx7{,}85398\cdot10^{-6}\ \text{m}^3/\text{s}$, $GCI_f\approx0{,}312\,\%$ i fini maseni debalans iznosi $0{,}0025\,\%$. Arhiva profila ne sadrži reziduale, povijesti monitoriranih sila, masenu bilancu ni potpuni mjerni budžet nesigurnosti; zato je korisna za usporedbu integralnih koeficijenata i mrežnog trenda, ali ne zatvara validacijsku presudu.

## Gubitci, cjevovodi, crpke i mreže

### Z1. Gubitci ravne dionice {#key-task-gubitci-ravne-dionice .unnumbered .unlisted}

[Vrati se na zadatak](u13_gubici_cjevovodi_crpke_i_mreze.qmd#task-gubitci-ravne-dionice)

**Sažetak.** Voda gustoće $998\ \mathrm{kg/m^3}$ protječe cijevi $D=0{,}10\ \mathrm{m}$, $L=50\ \mathrm{m}$ protokom $Q=0{,}012\ \mathrm{m^3/s}$. Zadano je $\lambda=0{,}025$ i $\sum\xi=4{,}0$. Odredi brzinu, linijski i lokalni gubitak, ukupni gubitak…

**Smjernica postupka.** Najprije izračunaj $A$ i $v=Q/A$. Tek zatim zajedničku brzinsku visinu pomnoži s $\lambda L/D$ odnosno $\sum\xi$.

**Kontrolni rezultat ili kriterij.** $v=1{,}528\ \mathrm{m/s}$, $h_l=1{,}487\ \mathrm{m}$, $h_{loc}=0{,}476\ \mathrm{m}$, $h_w=1{,}963\ \mathrm{m}$ i $\Delta p=19{,}2\ \mathrm{kPa}$. Provjeri da je $\Delta p/(\rho g)=h_w$.

### Z2. Laminarni tok viskozne smjese {#key-task-laminarna-cijev-smjese .unnumbered .unlisted}

[Vrati se na zadatak](u13_gubici_cjevovodi_crpke_i_mreze.qmd#task-laminarna-cijev-smjese)

**Sažetak.** Smjesa gustoće $1100\ \mathrm{kg/m^3}$ i $\nu=3{,}0\cdot10^{-6}\ \mathrm{m^2/s}$ protječe kružnom cijevi $D=6{,}0\ \mathrm{mm}$, $L=5{,}0\ \mathrm{m}$ protokom $Q=6{,}0\cdot10^{-6}\ \mathrm{m^3/s}$. Zanemari lokalne gubitke. Odredi $Re$…

**Smjernica postupka.** Izračunaj režim prije izbora korelacije. Ako je tok laminaran, upotrijebi $\lambda=64/Re$; rezultat zatim provjeri Poiseuilleovim zakonom.

**Kontrolni rezultat ili kriterij.** $v=0{,}212\ \mathrm{m/s}$, $Re=424$, $\lambda=0{,}1508$ i $\Delta p=3{,}11\ \mathrm{kPa}$. Udvostručenje $Q$ uz ostale iste podatke udvostručuje $\Delta p$ dok tok ostaje laminaran.

### Z3. Raspodjela kroz dvije paralelne grane {#key-task-raspodjela-paralelnih-grana .unnumbered .unlisted}

[Vrati se na zadatak](u13_gubici_cjevovodi_crpke_i_mreze.qmd#task-raspodjela-paralelnih-grana)

**Sažetak.** Između istih čvorova spojene su grane s približno konstantnim otporima $R_1=12\,000\ \mathrm{s^2/m^5}$ i $R_2=48\,000\ \mathrm{s^2/m^5}$. Ukupni protok iznosi $Q=0{,}020\ \mathrm{m^3/s}$. Odredi $Q_1$, $Q_2$ i zajednički pad energije.

**Smjernica postupka.** Postavi $R_1Q_1^2=R_2Q_2^2$ i $Q_1+Q_2=Q$. Prije računa predvidi koja grana nosi veći protok.

**Kontrolni rezultat ili kriterij.** $Q_1=13{,}33\ \mathrm{L/s}$, $Q_2=6{,}67\ \mathrm{L/s}$ i $h_{AB}=2{,}13\ \mathrm{m}$. Obje grane moraju vratiti isti $h_{AB}$.

### Z4. Radna točka i snaga crpke {#key-task-radna-tocka-tri-snage .unnumbered .unlisted}

[Vrati se na zadatak](u13_gubici_cjevovodi_crpke_i_mreze.qmd#task-radna-tocka-tri-snage)

**Sažetak.** Za $Q$ u $\mathrm{m^3/s}$ zadane su krivulje $H_p=30-30\,000Q^2$ i $H_s=8+20\,000Q^2$. Za vodu uzmi $\rho=1000\ \mathrm{kg/m^3}$. U radnoj točki vrijede $\eta_p=0{,}76$ i $\eta_m=0{,}92$; gubitke pretvarača zanemari. Odredi $Q_{op}$…

**Smjernica postupka.** Najprije izjednači krivulje. Zatim slijedi pretvorbeni lanac $P_h=\rho gQH$, $P_{vr}=P_h/\eta_p$, $P_{el}=P_{vr}/\eta_m$.

**Kontrolni rezultat ili kriterij.** $Q_{op}=20{,}98\ \mathrm{L/s}$, $H_{op}=16{,}8\ \mathrm{m}$, $P_h=3{,}46\ \mathrm{kW}$, $P_{vr}=4{,}55\ \mathrm{kW}$ i $P_{el}=4{,}94\ \mathrm{kW}$. Provjeri da snage rastu prema električnom ulazu.

### Z5. Izbor promjera uz nesiguran otpor {#key-task-robustan-izbor-promjera .unnumbered .unlisted}

[Vrati se na zadatak](u13_gubici_cjevovodi_crpke_i_mreze.qmd#task-robustan-izbor-promjera)

**Sažetak.** Vod duljine $L=150\ \mathrm{m}$ mora prenositi $Q=0{,}018\ \mathrm{m^3/s}$. Zbroj lokalnih koeficijenata iznosi $6{,}0$, a zbog starenja je $\lambda$ između 0,020 i 0,028. Dostupni su promjeri 80, 100 i 125 mm. Odaberi najmanji promjer…

**Smjernica postupka.** Za svaki kandidat izračunaj brzinu, a zatim raspon $h_w$ za obje granice $\lambda$. Odluku donesi prema najvećem, ne srednjem gubitku.

**Kontrolni rezultat ili kriterij.** Rasponi $h_w$ su približno 28,4–38,2 m za 80 mm, 9,64–12,85 m za 100 mm i 3,29–4,34 m za 125 mm. Najmanji robustan izbor jest 100 mm. Provjera odluke jest gornja granica $12{,}85<15\ \mathrm{m}$.

### Z6. Regulacija crpke, energija i usisna rezerva {#key-task-regulacija-energija-npsh .unnumbered .unlisted}

[Vrati se na zadatak](u13_gubici_cjevovodi_crpke_i_mreze.qmd#task-regulacija-energija-npsh)

**Sažetak.** Crpka pri nazivnoj brzini ima $H_p(q)=24-0{,}012q^2$, gdje je $q$ u $\mathrm{L/s}$. Izvorni sustav ima $H_s(q)=5+0{,}025q^2$. Prigušivanje ventila mijenja ga u $H_{s,V}(q)=5+0{,}040q^2$. Ukupna učinkovitost pretvorbe električna $\to$…

**Smjernica postupka.** Prigušenu radnu točku dobiješ iz $H_p=H_{s,V}$. Za otvoren sustav pri istom $q$ vrijedi $H_{p,s}(q)=24s^2-0{,}012q^2=H_s(q)$. Energiju računaj iz $P_{el}=\rho gQH/0{,}72$. Za usis upotrijebi [odgovarajući izraz](u13_gubici_cjevovodi_crpke_i_mreze.qmd#eq-npsha-spremnik).

**Kontrolni rezultat ili kriterij.** Prigušeno: $q=19{,}12\ \mathrm{L/s}$, $H=19{,}62\ \mathrm{m}$ i $P_{el}=5{,}11\ \mathrm{kW}$. Regulacija brzinom: otvoren sustav traži $H=14{,}13\ \mathrm{m}$, $s=0{,}878$, $P_{el}=3{,}68\ \mathrm{kW}$ i idealizirana godišnja ušteda je $7{,}14\ \mathrm{MWh}$. Za usis su $NPSH_a=6{,}65\ \mathrm{m}$, $NPSH_r=3{,}10\ \mathrm{m}$ i numerička razlika $3{,}55\ \mathrm{m}$. Prihvatljivost ipak zahtijeva proizvođačev kriterij margine, dopušteno radno područje i stvarne temperaturne/atmosferske uvjete.

## Turbostrojevi i propulzija

### Z1. Sila mlaza na nepomičnu ploču {#key-task-u12-vodeni-mlaz-brzine-izlazi-iz-kruzne-sapnice .unnumbered .unlisted}

[Vrati se na zadatak](u14_turbostrojevi_i_propulzija.qmd#task-u12-vodeni-mlaz-brzine-izlazi-iz-kruzne-sapnice)

**Sažetak.** Vodeni mlaz brzine $v = 24\ \text{m/s}$ izlazi iz kružne sapnice promjera $d = 22\ \text{mm}$ i udara okomito na nepomičnu ravnu ploču. Odredi silu na ploču.

**Smjernica postupka.** $\dot m = \rho Av$, a za potpuno kočenje komponente brzine na ploči vrijedi $F = \dot m v$.

**Kontrolni rezultat ili kriterij.** $\dot m \approx 9{,}1\ \text{kg/s}$; $F \approx 219\ \text{N}$.

### Z2. Zakretanje mlaza u vodilici {#key-task-u12-vodeni-mlaz-brzine-izlazi-iz-pravokutne-sapnice .unnumbered .unlisted}

[Vrati se na zadatak](u14_turbostrojevi_i_propulzija.qmd#task-u12-vodeni-mlaz-brzine-izlazi-iz-pravokutne-sapnice)

**Sažetak.** Vodeni mlaz brzine $v = 26\ \text{m/s}$ izlazi iz pravokutne sapnice širine $b = 30\ \text{mm}$ i visine $h = 16\ \text{mm}$ te udara u nepomičnu vodilicu koja tok zakreće za $110^\circ$ bez promjene iznosa brzine. Odredi komponente sile…

**Smjernica postupka.** iz presjeka dobij $\dot m$, a zatim razliku ulazne i izlazne komponente brzine u x i y smjeru.

**Kontrolni rezultat ili kriterij.** $\dot m \approx 12{,}5\ \text{kg/s}$; $F_x \approx 435\ \text{N}$, $F_y \approx -304\ \text{N}$; reakcija nosača $\approx 531\ \text{N}$.

### Z3. Sila na pokretnu lopaticu {#key-task-u12-na-pokretnu-lopaticu-dolazi-mlaz-vode-apsolutnom .unnumbered .unlisted}

[Vrati se na zadatak](u14_turbostrojevi_i_propulzija.qmd#task-u12-na-pokretnu-lopaticu-dolazi-mlaz-vode-apsolutnom)

**Sažetak.** Na pokretnu lopaticu dolazi mlaz vode apsolutnom brzinom $v_1 = 32\ \text{m/s}$, dok se lopatica giba brzinom $u = 12\ \text{m/s}$ u smjeru mlaza. Pretpostavi da je relativna izlazna brzina po iznosu jednaka ulaznoj i zakrenuta za…

**Smjernica postupka.** prijeđi na relativne brzine, zatim vrati apsolutnu izlaznu brzinu i iz tangencijalne promjene količine gibanja dobij silu; snaga je $P = Fu$.

**Kontrolni rezultat ili kriterij.** $w_1 = 20\ \text{m/s}$; $F_t \approx 672\ \text{N}$; $P \approx 8{,}06\ \text{kW}$.

### Z4. Moment i snaga Peltonove lopatice {#key-task-u12-peltonova-lopatica-na-rotoru-radijusa-prima-mlaz .unnumbered .unlisted}

[Vrati se na zadatak](u14_turbostrojevi_i_propulzija.qmd#task-u12-peltonova-lopatica-na-rotoru-radijusa-prima-mlaz)

**Sažetak.** Peltonova lopatica na rotoru radijusa $R = 0{,}42\ \text{m}$ prima mlaz vode masenog protoka $\dot m = 24\ \text{kg/s}$. Tangencijalna komponenta apsolutne brzine na ulazu iznosi $v_{u1} = 28\ \text{m/s}$, a na izlazu $v_{u2} = 6\…

**Smjernica postupka.** tangencijalna sila slijedi iz $F_t = \dot m (v_{u1} - v_{u2})$, a moment je $M = F_t R$.

**Kontrolni rezultat ili kriterij.** $F_t = 528\ \text{N}$; $M \approx 222\ \text{N·m}$.

### Z5. Potisak modula s trima sapnicama {#key-task-u12-potisni-modul-ima-tri-jednake-sapnice-promjera .unnumbered .unlisted}

[Vrati se na zadatak](u14_turbostrojevi_i_propulzija.qmd#task-u12-potisni-modul-ima-tri-jednake-sapnice-promjera)

**Sažetak.** Potisni modul ima tri jednake sapnice promjera $d = 30\ \text{mm}$. Iz svake sapnice voda izlazi brzinom $v = 42\ \text{m/s}$ u suprotnom smjeru od gibanja platforme. Odredi ukupni potisak modula i hidrauličku snagu mlaza ako je gustoća…

**Smjernica postupka.** za jednu sapnicu vrijedi $F = \dot m v$ i $P = \dot m v^2/2$; ukupni rezultat je trostruki zbroj.

**Kontrolni rezultat ili kriterij.** ukupni potisak $\approx 3{,}73\ \text{kN}$; hidraulička snaga $\approx 78{,}4\ \text{kW}$.

### Z6. Podizanje mlazne platforme {#key-task-u12-mlazna-platforma-ukupne-mase-ima-cetiri-jednake .unnumbered .unlisted}

[Vrati se na zadatak](u14_turbostrojevi_i_propulzija.qmd#task-u12-mlazna-platforma-ukupne-mase-ima-cetiri-jednake)

**Sažetak.** Mlazna platforma ukupne mase $m = 110\ \text{kg}$ ima četiri jednake sapnice promjera $d = 28\ \text{mm}$. Voda gustoće $\rho=998\ \text{kg/m}^3$ iz svake sapnice izlazi okomito prema dolje brzinom $v = 36\ \text{m/s}$. Odredi ukupni…

**Smjernica postupka.** najprije zbroji izlazne površine svih sapnica; zatim koristi $F_p = \rho A v^2$, uvjet lebdenja $F_p = mg$ i za zadanu masu Newtonov zakon $a = (F_p - mg)/m$. Za masu prema zadanom kriteriju izračunaj najmanji potisak s $d_{min}$ i $v_{min}$ te postavi $F_{p,min}=1{,}10\,m_{krit}g$.

**Kontrolni rezultat ili kriterij.** $F_p \approx 3{,}19\ \text{kN}$; najveća masa lebdenja $\approx 325\ \text{kg}$; pri $m = 110\ \text{kg}$ ubrzanje $a \approx 19{,}2\ \text{m/s}^2$. Za $d_{min}=27{,}7\ \text{mm}$ i $v_{min}=34{,}5\ \text{m/s}$ najmanji je potisak približno $2{,}86\ \text{kN}$, pa zadani kriterij daje $m_{krit}\approx265\ \text{kg}$. To je rezultat idealiziranoga statičkog modela, ne certificirana nosivost; nedostaju dinamika, stabilnost, konstrukcija, upravljanje i mjerodavni propisi.

## Otvoreni tokovi

### Z1. Froudeov broj i širenje poremećaja {#key-task-otvoreni-fr .unnumbered .unlisted}

[Vrati se na zadatak](u15_otvoreni_tokovi.qmd#task-otvoreni-fr)

**Sažetak.** Pravokutni kanal $b=1{,}5\ \text{m}$ vodi $Q=1{,}2\ \text{m}^3/\text{s}$ pri $y=0{,}60\ \text{m}$. Odredi $v$, $Fr$ i smjer mogućeg širenja poremećaja.

**Kontrolni rezultat ili kriterij.** $v=1{,}33\ \text{m/s}$, $Fr=0{,}55$.

### Z2. Kritična dubina i minimalna energija {#key-task-kriticna-dubina .unnumbered .unlisted}

[Vrati se na zadatak](u15_otvoreni_tokovi.qmd#task-kriticna-dubina)

**Sažetak.** Za $q=3{,}0\ \text{m}^2/\text{s}$ odredi $y_c$ i $E_{min}$.

**Kontrolni rezultat ili kriterij.** $y_c\approx0{,}972\ \text{m}$, $E_{min}\approx1{,}46\ \text{m}$.

### Z3. Geometrija i tok trapeznog kanala {#key-task-trapezni-presjek .unnumbered .unlisted}

[Vrati se na zadatak](u15_otvoreni_tokovi.qmd#task-trapezni-presjek)

**Sažetak.** Simetrični trapezni kanal ima širinu dna $b=2{,}40\ \text{m}$, pokos $z=1{,}50$ vodoravno na jedan okomito, dubinu $y=0{,}900\ \text{m}$ i protok $Q=3{,}60\ \text{m}^3/\text{s}$. Izračunaj $A$, $T$, $P$, $D_h$, $R_h$, srednju brzinu i…

**Smjernica postupka.** Za pokos $z{:}1$ vrijedi $A=y(b+zy)$, $T=b+2zy$ i $P=b+2y\sqrt{1+z^2}$. U izrazu za $Fr$ upotrijebi $D_h=A/T$, a ne $R_h$.

**Kontrolni rezultat ili kriterij.** $A=3{,}375\ \text{m}^2$, $T=5{,}100\ \text{m}$, $P=5{,}645\ \text{m}$, $D_h=0{,}6618\ \text{m}$, $R_h=0{,}5979\ \text{m}$, $v=1{,}0667\ \text{m/s}$ i $Fr=0{,}4186$ (mirni tok).

### Z4. Alternativne dubine toka {#key-task-alternativne-dubine .unnumbered .unlisted}

[Vrati se na zadatak](u15_otvoreni_tokovi.qmd#task-alternativne-dubine)

**Sažetak.** U pravokutnom kanalu protok po jedinici širine iznosi $q=2{,}20\ \text{m}^2/\text{s}$, a specifična energija $E=1{,}600\ \text{m}$. Bez uporabe gotove formule za korijene najprije provjeri $E>E_{min}$, zatim numerički odredi obje…

**Smjernica postupka.** Kritična dubina razdvaja intervale traženja korijena funkcije $f(y)=y+q^2/(2gy^2)-E$. Jedan korijen traži u $0<y<y_c$, a drugi u $y>y_c$; zapiši i kriterij zaustavljanja numeričkog postupka.

**Kontrolni rezultat ili kriterij.** $y_c=0{,}7902\ \text{m}$ i $E_{min}=1{,}1853\ \text{m}$. Plića je grana $y_s=0{,}4665\ \text{m}$, $Fr_s=2{,}204$; dublja je $y_d=1{,}4887\ \text{m}$, $Fr_d=0{,}3867$.

### Z5. Provjera mjerenja hidrauličkog skoka {#key-task-skok-mjerenje .unnumbered .unlisted}

[Vrati se na zadatak](u15_otvoreni_tokovi.qmd#task-skok-mjerenje)

**Sažetak.** Na vodoravnom pravokutnom pokusnom kanalu izmjereni su $Q=1{,}800\pm0{,}018\ \text{m}^3/\text{s}$, $b=1{,}200\pm0{,}003\ \text{m}$, $y_1=0{,}250\pm0{,}003\ \text{m}$ i $y_2=1{,}220\pm0{,}008\ \text{m}$; navedene su neovisne standardne…

**Smjernica postupka.** Najprije propagiraj $q=Q/b$. Za $M(y,q)=y^2/2+q^2/(gy)$ izračunaj parcijalne derivacije reziduala prema $y_1$, $y_2$ i $q$, a zatim primijeni korijen iz zbroja kvadrata. Hidrostatičke sile na krajnjim presjecima djeluju u suprotnim smjerovima; težina nema uzdužnu komponentu.

**Kontrolni rezultat ili kriterij.** $q=1{,}5000\ \text{m}^2/\text{s}$ i $u_q=0{,}01546\ \text{m}^2/\text{s}$. Dobiva se $R=-0{,}01648\ \text{m}^2$, $u_R=0{,}02010\ \text{m}^2$ i $|R|/u_R=0{,}820<2$, pa se u granicama zadanoga modela bilanca zatvara. Iz srednjih ulaza teorijska je spregnuta dubina $1{,}2353\ \text{m}$.

### Z6. Propusnost oborinskog kanala {#key-task-klimatski-kanal .unnumbered .unlisted}

[Vrati se na zadatak](u15_otvoreni_tokovi.qmd#task-klimatski-kanal)

**Sažetak.** Trapezni oborinski kanal ima $b=3{,}00\ \text{m}$, pokos $z=2{,}00$, nagib $S_f=0{,}00150$ i konstrukcijsku dubinu $H=1{,}50\ \text{m}$; traže se projektni protok $Q_d=8{,}00\ \text{m}^3/\text{s}$ i slobodni rub najmanje $f_{min}=0{,}300\…

**Smjernica postupka.** Za svaki $n$ najprije računaj kapacitet na dopuštenoj dubini $1{,}20\ \text{m}$, a normalnu dubinu pri $Q_d$ pronađi kao korijen Manningove jednadžbe. Odvojeno provjeri srednju procjenu i konzervativni $n_c$. U bazenu je $q=Q/B$; ista vrijednost $Q_d$ daje isti skok neovisno o stanju uzvodnog održavanja, ali kapaciteti daju različitu izvanprojektnu ovojnicu.

**Kontrolni rezultat ili kriterij.** Za A/B/C kapaciteti pri $y=1{,}20\ \text{m}$ iznose $11{,}759/8{,}141/6{,}047\ \text{m}^3/\text{s}$, a normalne dubine pri $Q_d$ $0{,}985/1{,}189/1{,}380\ \text{m}$, odnosno slobodni rubovi $0{,}515/0{,}311/0{,}120\ \text{m}$. S $n_c$ kapaciteti padaju na $10{,}583/7{,}055/4{,}922\ \text{m}^3/\text{s}$, pa samo A robusno zadovoljava oba zahtjeva. Pri $Q_d$ je $y_2=1{,}059\ \text{m}$; pri kapacitetima A/B/C dobiva se $y_2=1{,}628/1{,}080/0{,}765\ \text{m}$, pa bazen ne pokriva cijelu…

::: {.mf1-mini-summary}
<p class="mf1-box-label">Opseg ključa</p>

Ključ obuhvaća 90 zadataka iz javnog toka U01–U15. Pogrešku u rezultatu prijavite prema stabilnom ID-ju zadatka kroz errata obrazac.
:::
