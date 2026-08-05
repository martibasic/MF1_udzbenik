<!-- Generirano skriptom scripts/generate_exercise_key.py; ne uređivati ručno. -->

## Ključ naputaka i kontrolnih rezultata

Ovaj dodatak odvaja naputke i kontrolne rezultate od teksta zadatka u tiskanom izdanju. Ne zamjenjuje postupak: prije provjere treba zapisati model, pretpostavke, jedinice i barem jednu neovisnu fizikalnu provjeru. Otvoreni T3/T4 zadatci namjerno nemaju jedinstven broj.

## Osnove fluida i Pascalov zakon

### Zadatak 1 · T1 {#key-task-u01-u-servisnoj-hidraulicnoj-presi-mali-klip-promjera}

[Vrati se na zadatak](u01_osnove_fluida_i_pascalov_zakon.qmd#task-u01-u-servisnoj-hidraulicnoj-presi-mali-klip-promjera)

**Sažetak.** U servisnoj hidrauličnoj preši mali klip promjera $d_1 = 28\ \text{mm}$ potiskuje ulje prema radnom klipu promjera $d_2 = 140\ \text{mm}$. Ako operater na mali klip djeluje silom $F_1 = 180\ \text{N}$, odredi tlak u ulju, silu na radnom…

**Naputak.** $p = F_1/A_1$; zatim $F_2 = pA_2$ i iz volumne bilance $A_1 s_1 = A_2 s_2$.

**Kontrolni rezultat ili kriterij.** $p \approx 292\ \text{kPa}$; $F_2 = 4{,}5\ \text{kN}$; $s_2 = 4{,}8\ \text{mm}$.

### Zadatak 2 · T1 {#key-task-u01-na-kruzni-klip-promjera-djeluje-sila-odredi}

[Vrati se na zadatak](u01_osnove_fluida_i_pascalov_zakon.qmd#task-u01-na-kruzni-klip-promjera-djeluje-sila-odredi)

**Sažetak.** Na kružni klip promjera $d = 24\ \text{mm}$ djeluje sila $F = 95\ \text{N}$. Odredi tlak u ulju i silu koju isti tlak daje na drugi klip promjera $D = 72\ \text{mm}$.

**Naputak.** najprije $A = \pi d^2/4$, zatim $p = F/A$ i na većem klipu $F_2 = pA_2$.

**Kontrolni rezultat ili kriterij.** $p \approx 210\ \text{kPa}$; $F_2 = 855\ \text{N}$.

### Zadatak 3 · T2 {#key-task-u01-u-zatvorenoj-hidraulicnoj-stezi-tlak-ulja-iznosi}

[Vrati se na zadatak](u01_osnove_fluida_i_pascalov_zakon.qmd#task-u01-u-zatvorenoj-hidraulicnoj-stezi-tlak-ulja-iznosi)

**Sažetak.** U zatvorenoj hidrauličnoj stezi tlak ulja iznosi $p = 2{,}4\ \text{MPa}$, a radni klip ima promjer $d = 52\ \text{mm}$. Odredi silu stezanja i procijeni koliki bi promjer morao imati novi klip ako se pri istom tlaku traži sila stezanja od…

**Naputak.** koristi $F = pA$; iz tražene sile vrati površinu $A = F/p$, pa zatim promjer iz $A = \pi d^2/4$.

**Kontrolni rezultat ili kriterij.** $F \approx 5{,}1\ \text{kN}$; $d_{min} \approx 65\ \text{mm}$.

### Zadatak 4 · T2 {#key-task-u01-hidraulicni-stol-nosi-teret-mase-preko-dvaju}

[Vrati se na zadatak](u01_osnove_fluida_i_pascalov_zakon.qmd#task-u01-hidraulicni-stol-nosi-teret-mase-preko-dvaju)

**Sažetak.** Hidraulični stol nosi teret mase $m = 1350\ \text{kg}$ preko dvaju jednakih radnih cilindara promjera $D = 95\ \text{mm}$. Ulje se dovodi ručnom pumpom čiji klip ima promjer $d = 18\ \text{mm}$ i hod $s = 160\ \text{mm}$. Odredi minimalnu…

**Naputak.** teret raspodijeli na dva cilindra; iz $p = G/(2A_D)$ dobij $F_p = pA_d$, a broj hodova iz $nA_d s = 2A_D \Delta z$.

**Kontrolni rezultat ili kriterij.** $p \approx 0{,}93\ \text{MPa}$; $F_p \approx 238\ \text{N}$; $n = 16$ hodova.

### Zadatak 5 · T3 {#key-task-u01-rucna-pumpa-s-klipom-promjera-razvija-silu}

[Vrati se na zadatak](u01_osnove_fluida_i_pascalov_zakon.qmd#task-u01-rucna-pumpa-s-klipom-promjera-razvija-silu)

**Sažetak.** Ručna pumpa s klipom promjera $d = 25\ \text{mm}$ razvija silu $F_p = 420\ \text{N}$. Dva radna cilindra promjera $D = 140\ \text{mm}$ nalaze se na istoj razini i podižu platformu. Odredi tlak u ulju, ukupno nosivo opterećenje platforme i…

**Naputak.** najprije izračunaj tlak iz $p = F_p/A_d$; zatim ukupno opterećenje iz $G = 2pA_D$, a ukupan hod pumpe iz volumne bilance $A_d s_p = 2A_D \Delta z$.

**Kontrolni rezultat ili kriterij.** $p \approx 856\ \text{kPa}$; $G \approx 26{,}3\ \text{kN}$; $s_p \approx 1{,}88\ \text{m}$.

### Zadatak 6 · T4 {#key-task-u01-hidraulicni-radni-stol-podupiru-tri-jednaka-cilindra}

[Vrati se na zadatak](u01_osnove_fluida_i_pascalov_zakon.qmd#task-u01-hidraulicni-radni-stol-podupiru-tri-jednaka-cilindra)

**Sažetak.** Hidraulični radni stol podupiru tri jednaka cilindra, svaki površine $A_L = 95\ \text{cm}^2$. Ulje dovodi pumpni klip promjera $d = 22\ \text{mm}$ na koji djeluje sila $F_p = 360\ \text{N}$. Odredi tlak u ulju, ukupno idealno opterećenje…

**Naputak.** prvo izračunaj $A_p$ i tlak iz $p = F_p/A_p$; zatim idealno opterećenje iz $G = 3pA_L$, a idealni hod pumpe iz volumne bilance $A_p s_p = 3A_L \Delta z$. Za stvarni sustav vrijedi $G_{kor}=\eta_FG$ i $s_{p,st}=s_p/\eta_V$. Konzervativnu odluku donesi s $\eta_{F,min}$ i $\eta_{V,min}$, a ne samo sa srednjim vrijednostima.

**Kontrolni rezultat ili kriterij.** $p \approx 947\ \text{kPa}$; $G \approx 27{,}0\ \text{kN}$; $s_p \approx 1{,}35\ \text{m}$. Nominalno je $G_{kor}\approx23{,}2\ \text{kN}$ i $s_{p,st}\approx1{,}50\ \text{m}$, a konzervativno $G_{kor,min}\approx22{,}1\ \text{kN}$ i $s_{p,st,max}\approx1{,}55\ \text{m}$. Oba zadana brojčana kriterija jesu zadovoljena, ali s malim rezervama, približno $0{,}1\ \text{kN}$ i $0{,}05\ \text{m}$; to nije potpuna provjera stroja ni odobrenje za puštanje u rad.

## Viskoznost, površinska napetost i kapilarnost

### Zadatak 1 · T1 {#key-task-u02-izme-u-dviju-paralelnih-ploca-nalazi-se}

[Vrati se na zadatak](u02_viskoznost_povrsinska_napetost_i_kapilarnost.qmd#task-u02-izme-u-dviju-paralelnih-ploca-nalazi-se)

**Sažetak.** Između dviju paralelnih ploča nalazi se glicerin debljine $\delta = 2{,}4\ \text{mm}$. Gornja ploča površine $A = 0{,}22\ \text{m}^2$ giba se stalnom brzinom $v = 0{,}65\ \text{m/s}$, donja ploča miruje, a dinamička viskoznost glicerina…

**Naputak.** $dv/dy = v/\delta$, zatim $\tau = \mu dv/dy$ i na kraju $F = \tau A$.

**Kontrolni rezultat ili kriterij.** $dv/dy \approx 271\ \text{s}^{-1}$; $\tau \approx 228\ \text{Pa}$; $F \approx 50\ \text{N}$.

### Zadatak 2 · T1 {#key-task-u02-klizna-ploca-povrsine-giba-se-brzinom-kroz}

[Vrati se na zadatak](u02_viskoznost_povrsinska_napetost_i_kapilarnost.qmd#task-u02-klizna-ploca-povrsine-giba-se-brzinom-kroz)

**Sažetak.** Klizna ploča površine $A = 0{,}14\ \text{m}^2$ giba se brzinom $v = 0{,}80\ \text{m/s}$ kroz uljni procjep debljine $\delta = 1{,}8\ \text{mm}$. Ako je mjerena vučna sila $F = 21\ \text{N}$, odredi dinamičku viskoznost ulja.

**Naputak.** iz $F = \tau A$ dobij $\tau$, a zatim iz $\tau = \mu v/\delta$ vrati $\mu$.

**Kontrolni rezultat ili kriterij.** $\tau = 150\ \text{Pa}$; $\mu \approx 0{,}34\ \text{Pa s}$.

### Zadatak 3 · T2 {#key-task-u02-vratilo-promjera-i-duljine-vrti-se-tako}

[Vrati se na zadatak](u02_viskoznost_povrsinska_napetost_i_kapilarnost.qmd#task-u02-vratilo-promjera-i-duljine-vrti-se-tako)

**Sažetak.** Vratilo promjera $D = 70\ \text{mm}$ i duljine $L = 0{,}24\ \text{m}$ vrti se tako da je obodna brzina $v = 1{,}6\ \text{m/s}$ u uljnom procjepu debljine $\delta = 0{,}60\ \text{mm}$. Dinamička viskoznost ulja je $\mu = 0{,}36\ \text{Pa…

**Naputak.** koristi aproksimaciju ravnih slojeva: $\tau = \mu v/\delta$ i $F = \tau A$ uz $A = \pi DL$.

**Kontrolni rezultat ili kriterij.** $\tau = 960\ \text{Pa}$; $F \approx 51\ \text{N}$.

### Zadatak 4 · T2 {#key-task-u02-kapilara-promjera-uronjena-je-u-etanol-za}

[Vrati se na zadatak](u02_viskoznost_povrsinska_napetost_i_kapilarnost.qmd#task-u02-kapilara-promjera-uronjena-je-u-etanol-za)

**Sažetak.** Kapilara promjera $d = 0{,}60\ \text{mm}$ uronjena je u etanol za koji vrijedi $\sigma = 0{,}022\ \text{N/m}$, $\theta = 18^\circ$ i $\rho = 790\ \text{kg/m}^3$. Odredi kapilarni uspon i usporedi ga s usponom u drugoj kapilari promjera…

**Naputak.** $h = 4\sigma \cos\theta /(\rho g d)$; drugi slučaj računa se istom formulom samo s novim promjerom.

**Kontrolni rezultat ili kriterij.** $h \approx 18{,}0\ \text{mm}$; kod $d = 1{,}2\ \text{mm}$ upola manje, $h \approx 9{,}0\ \text{mm}$.

### Zadatak 5 · T3 {#key-task-u02-staklena-kapilara-promjera-uronjena-je-u-vodu}

[Vrati se na zadatak](u02_viskoznost_povrsinska_napetost_i_kapilarnost.qmd#task-u02-staklena-kapilara-promjera-uronjena-je-u-vodu)

**Sažetak.** Staklena kapilara promjera $d = 0{,}90\ \text{mm}$ uronjena je u vodu za koju vrijedi $\sigma = 0{,}072\ \text{N/m}$, $\theta = 10^\circ$ i $\rho = 998\ \text{kg/m}^3$. Odredi kapilarni uspon. Zatim odredi tlak skoka u kapljici vode…

**Naputak.** najprije kapilarni uspon iz $h = 4\sigma \cos\theta /(\rho g d)$, a zatim tlak skoka kapljice iz $\Delta p = 4\sigma/d_k$.

**Kontrolni rezultat ili kriterij.** $h \approx 32{,}2\ \text{mm}$; $\Delta p \approx 240\ \text{Pa}$.

### Zadatak 6 · T4 {#key-task-u02-kapilarna-igla-unutarnjeg-promjera-spojena-je-na}

[Vrati se na zadatak](u02_viskoznost_povrsinska_napetost_i_kapilarnost.qmd#task-u02-kapilarna-igla-unutarnjeg-promjera-spojena-je-na)

**Sažetak.** Kapilarna igla unutarnjeg promjera $d = 0{,}50\ \text{mm}$ spojena je na spremnik vode za koju vrijedi $\sigma = 0{,}072\ \text{N/m}$, $\rho = 998\ \text{kg/m}^3$ i $\theta = 0^\circ$. Izlaz igle nalazi se na visini $H = 42\ \text{mm}$…

**Naputak.** prvo izračunaj $h_{cap} = 4\sigma /(\rho g d)$, zatim tlakovni skok kapljice $\Delta p = 4\sigma/D$, a preostali pretlak u idealizaciji kapilarnog uspona zatvori iz $p_M = \rho g(H-h_{cap}) + \Delta p$, uz donju granicu $p_M\ge0$. U alternativnom stanju više nema konkavnoga meniskusa koji daje $h_{cap}$, pa regulator mora svladati i visinsku razliku i pozitivni Laplaceov skok: $p_{M,konz}=\rho gH+4\sigma/D$.

**Kontrolni rezultat ili kriterij.** $h_{cap} \approx 58{,}8\ \text{mm}$; u idealizaciji kapilarnog uspona dobiva se zanemariv dodatni pretlak, $p_M \approx 0$. Kada je na izlazu već formirana sferna kapljica, konzervativni model daje $p_{M,konz}\approx0{,}571\ \text{kPa}$. Regulator od $0{,}50\ \text{kPa}$ stoga nije dovoljan za oba stanja: prvi model opisuje uspon s meniskusom u igli, ali izbor regulatora mora pokriti drugi model ili se mora provjeriti prijelaz između njih.

## Hidrostatička raspodjela tlaka i manometrija

### Zadatak 1 · T1 {#key-task-u03-otvoreni-spremnik-s-vodom-ima-slobodnu-povrsinu}

[Vrati se na zadatak](u03_hidrostaticka_raspodjela_tlaka_i_manometrija.qmd#task-u03-otvoreni-spremnik-s-vodom-ima-slobodnu-povrsinu)

**Sažetak.** Otvoreni spremnik s vodom ima slobodnu površinu na atmosferskom tlaku. Odredi apsolutni i manometarski tlak u točki koja se nalazi na dubini $h = 2{,}40\ \text{m}$ ako je $p_{atm} = 100{,}8\ \text{kPa}$ i $\rho = 998\ \text{kg/m}^3$.

**Naputak.** manometarski tlak je $p_M = \rho gh$, a apsolutni $p_{aps} = p_{atm} + p_M$.

**Kontrolni rezultat ili kriterij.** $p_M \approx 23{,}5\ \text{kPa}$; $p_{aps} \approx 124{,}3\ \text{kPa}$.

### Zadatak 2 · T1 {#key-task-u03-u-zatvorenom-spremniku-iznad-vode-vlada-manometarski}

[Vrati se na zadatak](u03_hidrostaticka_raspodjela_tlaka_i_manometrija.qmd#task-u03-u-zatvorenom-spremniku-iznad-vode-vlada-manometarski)

**Sažetak.** U zatvorenom spremniku iznad vode vlada manometarski tlak $p_m = 26\ \text{kPa}$. Odredi apsolutni i manometarski tlak u priključku koji se nalazi $1{,}80\ \text{m}$ ispod slobodne površine ako je lokalni atmosferski tlak $p_{atm} =…

**Naputak.** najprije tlak na slobodnoj površini, zatim kroz isti fluid dodaj $\rho gh$; tek na kraju razdvoji apsolutni i manometarski tlak.

**Kontrolni rezultat ili kriterij.** $p_M \approx 43{,}6\ \text{kPa}$; $p_{aps} \approx 142{,}8\ \text{kPa}$.

### Zadatak 3 · T2 {#key-task-u03-cjevovod-s-uljem-gustoce-spojen-je-na}

[Vrati se na zadatak](u03_hidrostaticka_raspodjela_tlaka_i_manometrija.qmd#task-u03-cjevovod-s-uljem-gustoce-spojen-je-na)

**Sažetak.** Cjevovod s uljem gustoće $\rho_u = 860\ \text{kg/m}^3$ spojen je na otvoreni U-manometar sa živom gustoće $\rho_{Hg} = 13600\ \text{kg/m}^3$. Razlika razina žive iznosi $\Delta h = 0{,}185\ \text{m}$, a priključna točka u kraku s uljem…

**Naputak.** kreni od slobodne površine otvorenog kraka; niz stupce piši promjene tlaka kao $\rho g\Delta h$ uz točan znak.

**Kontrolni rezultat ili kriterij.** $p_M \approx 23{,}7\ \text{kPa}$.

### Zadatak 4 · T2 {#key-task-u03-diferencijalni-manometar-ispunjen-zivom-spaja-dvije-tocke}

[Vrati se na zadatak](u03_hidrostaticka_raspodjela_tlaka_i_manometrija.qmd#task-u03-diferencijalni-manometar-ispunjen-zivom-spaja-dvije-tocke)

**Sažetak.** Diferencijalni manometar ispunjen živom spaja dvije točke u vodi, pri čemu je razlika razina žive $\Delta h = 0{,}145\ \text{m}$. Točka `A` nalazi se $0{,}30\ \text{m}$ ispod točke `B`. Odredi razliku tlakova $p_A - p_B$.

**Naputak.** napravi jednu zatvorenu putanju od `A` do `B`; kroz vodu i živu piši odvojene doprinose $\rho g\Delta h$ i tek na kraju zbroji.

**Kontrolni rezultat ili kriterij.** $p_A - p_B \approx 20{,}9\ \text{kPa}$.

### Zadatak 5 · T3 {#key-task-u03-vakuumski-spremnik-spojen-je-na-otvoreni-zivin}

[Vrati se na zadatak](u03_hidrostaticka_raspodjela_tlaka_i_manometrija.qmd#task-u03-vakuumski-spremnik-spojen-je-na-otvoreni-zivin)

**Sažetak.** Vakuumski spremnik spojen je na otvoreni živin manometar koji pokazuje razliku razina $\Delta h = 0{,}230\ \text{m}$. Ako je lokalni atmosferski tlak $p_{atm} = 98{,}6\ \text{kPa}$, odredi apsolutni tlak plina u spremniku. Zatim odredi…

**Naputak.** iz manometra najprije vrati tlak plina, a zatim u istom spremniku kroz vodu dodaj $\rho gh$ do tražene točke.

**Kontrolni rezultat ili kriterij.** $p_{gas} \approx 67{,}9\ \text{kPa}$ (aps.); na dubini $0{,}90\ \text{m}$: $p \approx 76{,}7\ \text{kPa}$.

### Zadatak 6 · T4 {#key-task-u03-zatvoreni-spremnik-s-vodom-ima-plinski-prostor}

[Vrati se na zadatak](u03_hidrostaticka_raspodjela_tlaka_i_manometrija.qmd#task-u03-zatvoreni-spremnik-s-vodom-ima-plinski-prostor)

**Sažetak.** Zatvoreni spremnik s vodom ima plinski prostor nepoznatog apsolutnog tlaka. Bočni priključak na dubini $h_1 = 0{,}65\ \text{m}$ spojen je na otvoreni U-manometar sa živom gustoće $\rho_{Hg} = 13600\ \text{kg/m}^3$, pri čemu je razlika…

**Naputak.** iz otvorenog manometra najprije vrati tlak u priključku, zatim se penjanjem kroz vodu vrati na plinski prostor, a silaskom na dubinu $h_2$ dobije tlak u traženoj točki. Za konzervativnu gornju granicu istodobno uzmi najveće $p_{atm}$, $\Delta h$ i $h_2$, a najmanje $h_1$. Nakon toga primijeni zahtijevanu rezervu na mjerno područje; nominalna vrijednost sama nije dovoljna za izbor senzora.

**Kontrolni rezultat ili kriterij.** $p_{gas} \approx 122{,}6\ \text{kPa}$ (aps.); na dubini $1{,}30\ \text{m}$: $p \approx 135{,}3\ \text{kPa}$. Konzervativna gornja granica iznosi $p_{max}\approx136{,}05\ \text{kPa}$, pa uz rezervu od $5\ \%$ treba puna skala od najmanje $142{,}9\ \text{kPa}$. Pretvornik $0$--$140\ \text{kPa}$ nije dostatan; bira se područje $0$--$160\ \text{kPa}$.

## Relativno mirovanje fluida

### Zadatak 1 · T1 {#key-task-u04-otvoreni-pravokutni-spremnik-duljine-i-pocetne-dubine}

[Vrati se na zadatak](u04_relativno_mirovanje_fluida.qmd#task-u04-otvoreni-pravokutni-spremnik-duljine-i-pocetne-dubine)

**Sažetak.** Otvoreni pravokutni spremnik duljine $L = 1{,}80\ \text{m}$ i početne dubine vode $h_0 = 0{,}34\ \text{m}$ giba se vodoravno stalnim ubrzanjem $a = 1{,}20\ \text{m/s}^2$. Odredi razliku razina između krajeva spremnika, lokalne dubine uz…

**Naputak.** $\Delta h = aL/g$; zatim $h_{str} = h_0 + \Delta h/2$ i $h_{pred} = h_0 - \Delta h/2$; usporedi $h_{str}$ s $H$.

**Kontrolni rezultat ili kriterij.** $\Delta h \approx 0{,}22\ \text{m}$; $h_{str} \approx 0{,}45\ \text{m}$, $h_{pred} \approx 0{,}23\ \text{m}$; nema prelijevanja jer je $h_{str} < H$.

### Zadatak 2 · T1 {#key-task-u04-otvoreni-spremnik-duljine-napunjen-je-do-visine}

[Vrati se na zadatak](u04_relativno_mirovanje_fluida.qmd#task-u04-otvoreni-spremnik-duljine-napunjen-je-do-visine)

**Sažetak.** Otvoreni spremnik duljine $L = 1{,}40\ \text{m}$ napunjen je do visine $h_0 = 0{,}30\ \text{m}$, a visina boka je $H = 0{,}42\ \text{m}$. Odredi najveće vodoravno ubrzanje prije početka prelijevanja.

**Naputak.** u graničnom stanju vrijedi $h_{str} = H$ i $\Delta h = 2(H-h_0)$; nakon toga $a = g\Delta h/L$.

**Kontrolni rezultat ili kriterij.** $a_{max} \approx 1{,}68\ \text{m/s}^2$.

### Zadatak 3 · T2 {#key-task-u04-zatvoreni-vertikalni-cilindar-potpuno-ispunjen-uljem-gustoce}

[Vrati se na zadatak](u04_relativno_mirovanje_fluida.qmd#task-u04-zatvoreni-vertikalni-cilindar-potpuno-ispunjen-uljem-gustoce)

**Sažetak.** Zatvoreni vertikalni cilindar potpuno ispunjen uljem gustoće $\rho = 870\ \text{kg/m}^3$ ima visinu stupca fluida $h = 0{,}75\ \text{m}$. Sustav se giba prema gore ubrzanjem $a_z = 2{,}3\ \text{m/s}^2$. Odredi razliku tlaka između dna i…

**Naputak.** koristi efektivnu težinu fluida: $\Delta p = \rho (g+a_z)h$; za usporedbu u mirovanju uzmi $\Delta p_0 = \rho gh$.

**Kontrolni rezultat ili kriterij.** $\Delta p \approx 7{,}90\ \text{kPa}$; u mirovanju $\Delta p_0 \approx 6{,}40\ \text{kPa}$ — oko 23 % više.

### Zadatak 4 · T2 {#key-task-u04-ubrzani-otvoreni-spremnik-sirine-stijenke-i-duljine}

[Vrati se na zadatak](u04_relativno_mirovanje_fluida.qmd#task-u04-ubrzani-otvoreni-spremnik-sirine-stijenke-i-duljine)

**Sažetak.** Ubrzani otvoreni spremnik širine stijenke $b = 0{,}75\ \text{m}$ i duljine $L = 1{,}60\ \text{m}$ s početnom dubinom $h_0 = 0{,}36\ \text{m}$ nosi na stražnjoj stijenci hidrostatsku silu $F = 820\ \text{N}$. Odredi ubrzanje spremnika ako…

**Naputak.** iz sile vrati lokalnu dubinu preko $F = \rho g b h_{str}^2/2$; zatim $h_{str} = h_0 + \Delta h/2$ i $a = g\Delta h/L$.

**Kontrolni rezultat ili kriterij.** $h_{str} \approx 0{,}47\ \text{m}$; $a \approx 1{,}38\ \text{m/s}^2$.

### Zadatak 5 · T3 {#key-task-u04-cilindricna-posuda-radijusa-s-pocetnom-dubinom-vode}

[Vrati se na zadatak](u04_relativno_mirovanje_fluida.qmd#task-u04-cilindricna-posuda-radijusa-s-pocetnom-dubinom-vode)

**Sažetak.** Cilindrična posuda radijusa $R = 0{,}28\ \text{m}$ s početnom dubinom vode $h_0 = 0{,}22\ \text{m}$ vrti se stalnom kutnom brzinom $\omega = 5{,}5\ \text{rad/s}$. Odredi porast razine uz stijenku, spuštanje razine u osi i procijeni ostaje…

**Naputak.** razlika razina je $\Delta h = \omega^2 R^2/(2g)$; uz očuvanje volumena vrijedi $h_{rub} = h_0 + \Delta h/2$ i $h_{osa} = h_0 - \Delta h/2$.

**Kontrolni rezultat ili kriterij.** $\Delta h \approx 0{,}12\ \text{m}$; $h_{rub} \approx 0{,}28\ \text{m}$, $h_{osa} \approx 0{,}16\ \text{m}$ — dno u osi ostaje pokriveno.

### Zadatak 6 · T4 {#key-task-u04-otvoreni-cilindricni-spremnik-polumjera-i-visine-ispunjen}

[Vrati se na zadatak](u04_relativno_mirovanje_fluida.qmd#task-u04-otvoreni-cilindricni-spremnik-polumjera-i-visine-ispunjen)

**Sažetak.** Otvoreni cilindrični spremnik polumjera $R = 0{,}32\ \text{m}$ i visine $H = 0{,}62\ \text{m}$ ispunjen je vodom do početne srednje visine $h_0 = 0{,}46\ \text{m}$. Odredi najveću kutnu brzinu pri kojoj još nema prelijevanja. Zatim za…

**Naputak.** u graničnom stanju vrijedi $h_{rub} = H = h_0 + \omega_{max}^2 R^2/(4g)$; za radni režim najprije nađi $\Delta h = \omega^2 R^2/(2g)$, zatim $h_{osa}$ i $h_{rub}$, a tlakove iz $p_M = \rho gh$. U provjeri tolerancije koristi $\omega=1{,}05\alpha\omega_{max}$ i iz uvjeta $h_{osa}\ge0{,}350\ \text{m}$ riješi gornju granicu za $\alpha$.

**Kontrolni rezultat ili kriterij.** $\omega_{max} \approx 7{,}83\ \text{rad/s}$; pri $\omega = 0{,}80\,\omega_{max}$: $h_{osa} \approx 0{,}36\ \text{m}$, $h_{rub} \approx 0{,}56\ \text{m}$; $p_{M,osa} \approx 3{,}51\ \text{kPa}$, $p_{M,rub} \approx 5{,}52\ \text{kPa}$. U nepovoljnoj toleranciji stvarni je omjer $0{,}84$, pa je $h_{osa}\approx0{,}347\ \text{m}$, a $h_{rub}\approx0{,}573\ \text{m}$: nema prelijevanja, ali usis nije dovoljno prekriven. Iz uvjeta dubine slijedi $\alpha_{max}\approx0{,}790$; razumna je postavka…

## Hidrostatske sile na ravne i zakrivljene plohe

### Zadatak 1 · T1 {#key-task-u05-ravna-pravokutna-zaklopka}

[Vrati se na zadatak](u05_hidrostatske_sile_na_plohe.qmd#task-u05-ravna-pravokutna-zaklopka)

**Sažetak.** Vertikalni pravokutni poklopac širine $b=1{,}40\ \mathrm{m}$ i visine $H=1{,}80\ \mathrm{m}$ nalazi se u vodi tako da mu je gornji rub na dubini $h_1=1{,}10\ \mathrm{m}$. Odredite rezultantnu silu, dubinu centra tlaka i njegovu udaljenost…

**Naputak.** Najprije izračunajte $A$ i $h_C$. Za centar tlaka treba $I_G=bH^3/12$.

**Kontrolni rezultat ili kriterij.** $F=49{,}34\ \mathrm{kN}$; $h_{CP}=2{,}135\ \mathrm{m}$; udaljenost od gornjeg ruba $1{,}035\ \mathrm{m}$.

### Zadatak 2 · T1 {#key-task-u05-zakrivljeni-poklopac-cetvrtine-kruga}

[Vrati se na zadatak](u05_hidrostatske_sile_na_plohe.qmd#task-u05-zakrivljeni-poklopac-cetvrtine-kruga)

**Sažetak.** Zakrivljeni poklopac presjeka četvrtine kruga ima $R=0{,}65\ \mathrm{m}$ i širinu $b=1{,}20\ \mathrm{m}$. Gornja mu je točka na dubini $h_1=1{,}10\ \mathrm{m}$. Voda kvasi konveksnu vanjsku i donju stranu. Odredite $F_H$, predznačeni…

**Naputak.** Za $F_H$ rabite vertikalnu projekciju $Rb$ na dubini $h_1+R/2$. Pomoćni volumen čine pravokutni dio $h_1Rb$ i četvrtina valjka.

**Kontrolni rezultat ili kriterij.** $F_H=10{,}88\ \mathrm{kN}$; $F_V=+12{,}30\ \mathrm{kN}$ prema gore; $F_R=16{,}42\ \mathrm{kN}$.

### Zadatak 3 · T2 {#key-task-u05-kosi-poklopac-sa-zglobom}

[Vrati se na zadatak](u05_hidrostatske_sile_na_plohe.qmd#task-u05-kosi-poklopac-sa-zglobom)

**Sažetak.** Kosi pravokutni poklopac širine $b=0{,}80\ \mathrm{m}$ i duljine $L=1{,}00\ \mathrm{m}$ zatvara kut $\theta=40^\circ$ prema vodoravnici. Gornji rub na dubini je $h_1=0{,}90\ \mathrm{m}$ i spojen je zglobom. Na donjem rubu djeluje sila…

**Naputak.** Postavite $h(s)=h_1+s\sin\theta$ i uporabite omjer prvog momenta sile i ukupne sile. Zatim zatvorite moment oko zgloba.

**Kontrolni rezultat ili kriterij.** $F=9{,}566\ \mathrm{kN}$; $s_{CP}=0{,}5439\ \mathrm{m}$; $T=5{,}203\ \mathrm{kN}$.

### Zadatak 4 · T2 {#key-task-u05-dvoslojna-vertikalna-stijena}

[Vrati se na zadatak](u05_hidrostatske_sile_na_plohe.qmd#task-u05-dvoslojna-vertikalna-stijena)

**Sažetak.** Vertikalna stijena širine $b=1{,}80\ \mathrm{m}$ zadržava gornji sloj ulja gustoće $820\ \mathrm{kg/m^3}$ i visine $0{,}90\ \mathrm{m}$ te donji sloj vode gustoće $998\ \mathrm{kg/m^3}$ i visine $1{,}50\ \mathrm{m}$. Slobodna površina…

**Naputak.** Dijagram tlaka rastavite na uljni trokut, pravokutni doprinos uljnog stupca u vodi i vodeni trokut. Svaki dio ima svoje hvatište.

**Kontrolni rezultat ili kriterij.** $F=45{,}24\ \mathrm{kN}$; $h_{CP}=1{,}623\ \mathrm{m}$.

### Zadatak 5 · T3 {#key-task-u05-zglobni-zakrivljeni-poklopac-model}

[Vrati se na zadatak](u05_hidrostatske_sile_na_plohe.qmd#task-u05-zglobni-zakrivljeni-poklopac-model)

**Sažetak.** Četvrtcilindrični poklopac ima $R=0{,}75\ \mathrm{m}$, $b=1{,}10\ \mathrm{m}$ i gornju točku na dubini $h_1=0{,}45\ \mathrm{m}$. Voda kvasi konkavnu stranu odozgo, pa lokalne normale imaju vertikalnu komponentu prema dolje. Poklopac je…

**Naputak.** $F_H$ dolazi iz vertikalne projekcije. Za $F_V$ pomoćni volumen ima pravokutni dio i četvrtinu valjka. U momentu oko zgloba rabite zasebne krakove obiju komponenti.

**Kontrolni rezultat ili kriterij.** $F_H=6{,}664\ \mathrm{kN}$; $h_H=0{,}8818\ \mathrm{m}$ ispod slobodne površine, odnosno krak $0{,}4318\ \mathrm{m}$ prema zglobu; $F_V=8{,}392\ \mathrm{kN}$ prema dolje s krakom $0{,}4071\ \mathrm{m}$; $F_R=10{,}72\ \mathrm{kN}$; $T=8{,}392\ \mathrm{kN}$.

### Zadatak 6 · T4 {#key-task-u05-nesigurnost-modela-i-mjerenja}

[Vrati se na zadatak](u05_hidrostatske_sile_na_plohe.qmd#task-u05-nesigurnost-modela-i-mjerenja)

**Sažetak.** Pravokutni mjerni panel ima točno poznate dimenzije $b=1{,}20\ \mathrm{m}$ i $H=0{,}80\ \mathrm{m}$. Gornji rub je na izmjerenoj dubini $h_1=0{,}90\ \mathrm{m}$ sa standardnom nesigurnošću $u(h_1)=0{,}020\ \mathrm{m}$, a gustoća je…

**Naputak.** Za $F=\rho gbH(h_1+H/2)$ relativna nesigurnost zbog dvaju nesigurnih ulaza jest $u(F)/F=\sqrt{[u(\rho)/\rho]^2+[u(h_1)/(h_1+H/2)]^2}$.

**Kontrolni rezultat ili kriterij.** $F=12{,}218\ \mathrm{kN}$; $u(F)=0{,}192\ \mathrm{kN}$; kombinirana nesigurnost razlike $0{,}356\ \mathrm{kN}$; $z=1{,}74$. Budući da je $z<2$, ovaj skup podataka ne pokazuje neslaganje na zadanoj razini, ali time model nije općenito validiran.

## Uzgon, plivanje i početni stabilitet

### Zadatak 1 · T1 {#key-task-u07-hermeticki-zatvoreno-tijelo-volumena-i-mase-potpuno}

[Vrati se na zadatak](u06_uzgon_plivanje_i_stabilnost.qmd#task-u07-hermeticki-zatvoreno-tijelo-volumena-i-mase-potpuno)

**Sažetak.** Hermetički zatvoreno tijelo volumena $V = 0{,}085\ \text{m}^3$ i mase $m = 62\ \text{kg}$ potpuno je uronjeno u vodu gustoće $\rho = 998\ \text{kg/m}^3$. Odredi silu uzgona i silu koju treba primijeniti da tijelo ostane potpuno uronjeno i…

**Naputak.** uzgon je $F_U = \rho gV$; potom usporedi $F_U$ i težinu $G = mg$ da dobiješ potrebnu dodatnu silu.

**Kontrolni rezultat ili kriterij.** $F_U \approx 832\ \text{N}$; kako je $F_U > G = 608\ \text{N}$, treba dodatna sila prema dolje $\approx 224\ \text{N}$.

### Zadatak 2 · T1 {#key-task-u07-pravokutni-radni-ponton-duljine-sirine-i-visine}

[Vrati se na zadatak](u06_uzgon_plivanje_i_stabilnost.qmd#task-u07-pravokutni-radni-ponton-duljine-sirine-i-visine)

**Sažetak.** Pravokutni radni ponton duljine $L = 2{,}60\ \text{m}$, širine $B = 1{,}40\ \text{m}$ i visine boka $H = 0{,}38\ \text{m}$ ima vlastitu masu $m_p = 510\ \text{kg}$. Na njega se simetrično postavlja teret mase $m_t = 220\ \text{kg}$.…

**Naputak.** iz vertikalne ravnoteže vrijedi $\rho gV_{ist} = (m_p + m_t)g$; srednji gaz slijedi iz $V_{ist} = LBh$.

**Kontrolni rezultat ili kriterij.** $V_{ist} \approx 0{,}73\ \text{m}^3$; srednji gaz $h \approx 0{,}20\ \text{m}$; dodatna masa do ruba $\approx 650\ \text{kg}$.

### Zadatak 3 · T2 {#key-task-u07-plutajuca-servisna-platforma-duljine-i-sirine-ima}

[Vrati se na zadatak](u06_uzgon_plivanje_i_stabilnost.qmd#task-u07-plutajuca-servisna-platforma-duljine-i-sirine-ima)

**Sažetak.** Plutajuća servisna platforma duljine $L = 2{,}20\ \text{m}$ i širine $B = 1{,}00\ \text{m}$ ima ukupnu masu s opremom $m = 560\ \text{kg}$ i ukupno težište na visini $KG=0{,}18\ \text{m}$ iznad dna. Kompresor mase $85\ \text{kg}$ pomakne…

**Naputak.** srednji gaz dolazi iz ukupne težine. Zatim upotrijebi $KB=h_m/2$, $BM=B^2/(12h_m)$, $GM=KB+BM-KG$ i $m_k e=mGM\tan\theta$, uz $|h_L-h_D|=B\tan\theta$; nemoj izjednačiti geometrijski $y_B$ s krakom $GZ$.

**Kontrolni rezultat ili kriterij.** $h_m\approx0{,}255\ \text{m}$; $KB\approx0{,}128\ \text{m}$; $BM\approx0{,}327\ \text{m}$; $GM\approx0{,}274\ \text{m}$; $|h_L-h_D|\approx0{,}133\ \text{m}$, pri čemu je desni rub dublje uronjen.

### Zadatak 4 · T2 {#key-task-u07-areometar-mase-s-cilindricnim-vratom-promjera-pluta}

[Vrati se na zadatak](u06_uzgon_plivanje_i_stabilnost.qmd#task-u07-areometar-mase-s-cilindricnim-vratom-promjera-pluta)

**Sažetak.** Areometar mase $m = 0{,}085\ \text{kg}$ s cilindričnim vratom promjera $d = 8\ \text{mm}$ pluta tako da mu je u vodi uronjena duljina $h_1 = 82\ \text{mm}$, a u nepoznatom ulju $h_2 = 95\ \text{mm}$. Odredi gustoću ulja i protumači zašto…

**Naputak.** u oba fluida vrijedi $\rho gV_{ist} = mg$; razlika je samo u uronjenom volumenu vrata i tijela areometra.

**Kontrolni rezultat ili kriterij.** $\rho_{ulje} \approx 990\ \text{kg/m}^3$; uron je veći jer je ulje rjeđe pa je za istu težinu potreban veći istisnuti volumen.

### Zadatak 5 · T3 {#key-task-u07-plutajuci-modul-istiskuje-volumen-vode-i-ima}

[Vrati se na zadatak](u06_uzgon_plivanje_i_stabilnost.qmd#task-u07-plutajuci-modul-istiskuje-volumen-vode-i-ima)

**Sažetak.** Plutajući modul istiskuje volumen vode $V_{ist} = 0{,}62\ \text{m}^3$ i ima metacentarsku visinu $GM = 0{,}18\ \text{m}$. Ako se pri malom nagibu zakrene za $\varphi = 7^\circ$, odredi povratni moment stabilnosti i procijeni je li…

**Naputak.** deplasman je $\Delta = \rho gV_{ist}$, a za male nagibe povratni moment je $M_r = \Delta GM\sin\varphi$; znak $GM$ odlučuje o stabilnosti.

**Kontrolni rezultat ili kriterij.** $\Delta \approx 6{,}07\ \text{kN}$; $M_r \approx 133\ \text{N·m}$; $GM > 0$ pa je ravnoteža stabilna.

### Zadatak 6 · T4 {#key-task-u07-pravokutna-servisna-platforma-duljine-i-sirine-pluta}

[Vrati se na zadatak](u06_uzgon_plivanje_i_stabilnost.qmd#task-u07-pravokutna-servisna-platforma-duljine-i-sirine-pluta)

**Sažetak.** Pravokutna servisna platforma duljine $L = 2{,}80\ \text{m}$ i širine $B = 1{,}20\ \text{m}$ pluta na granici ulja gustoće $\rho_o = 820\ \text{kg/m}^3$ debljine $\delta = 0{,}08\ \text{m}$ i vode gustoće $\rho_w = 998\ \text{kg/m}^3$.…

**Naputak.** najprije uzmi $h_m=(h_L+h_D)/2$ i $m_\Delta=\rho_oV_o+\rho_wV_w$. Za položaje uzgonskih doprinosa vrijedi $z_{B,o}=h_m-\delta/2$ i $z_{B,w}=(h_m-\delta)/2$, pa izračunaj $KB_{eq}$ njihovim uzgonskim težinjenjem. U ovom modelu $BM_{eq}=\rho_w I_T/m_\Delta$, gdje je $I_T=LB^3/12$, a $GM_{eq}=KB_{eq}+BM_{eq}-KG$. Tek zatim primijeni $m_a e=mGM_{eq}\tan\theta$ i $\tan\theta=(h_L-h_D)/B$. Za konzervativni omotač izračunaj svih $2^5=32$ rubnih kombinacija pet nesigurnih skalarnih ulaza.

**Kontrolni rezultat ili kriterij.** $h_m=0{,}220\ \text{m}$; $V_o\approx0{,}269\ \text{m}^3$; $V_w\approx0{,}470\ \text{m}^3$; $m_\Delta\approx689{,}9\ \text{kg}$. Geometrijski su $y_{B,w}\approx0{,}0571\ \text{m}$ i $y_B\approx0{,}0389\ \text{m}$, ali $y_B$ nije $GZ$. Dobiva se $KB_{eq}\approx0{,}105\ \text{m}$, $BM_{eq}\approx0{,}583\ \text{m}$, $GM_{eq}\approx0{,}488\ \text{m}$ i $e\approx0{,}321\ \text{m}$. Najveća rubna vrijednost nastaje za $h_L=0{,}263\ \text{m}$, $h_D=0{,}177\ \text{m}$, $\rho_w=1001\ \text{kg/m}^3$…

## Kinematika, kontrolni volumen i kontinuitet

### Zadatak 1 · T1 {#key-task-u08-voda-struji-kroz-cijev-koja-se-siri}

[Vrati se na zadatak](u07_kinematika_kontrolni_volumen_i_kontinuitet.qmd#task-u08-voda-struji-kroz-cijev-koja-se-siri)

**Sažetak.** Voda struji kroz cijev koja se širi s promjera $D_1 = 0{,}10\ \text{m}$ na $D_2 = 0{,}16\ \text{m}$. Ako je ulazna srednja brzina $v_1 = 4{,}8\ \text{m/s}$, a gustoća vode $\rho = 998\ \text{kg/m}^3$, odredi izlaznu brzinu, volumenski…

**Naputak.** najprije $Q = A_1 v_1$, zatim $v_2 = Q/A_2$ i na kraju $\dot m = \rho Q$.

**Kontrolni rezultat ili kriterij.** $Q \approx 37{,}7\ \text{L/s}$; $v_2 \approx 1{,}88\ \text{m/s}$; $\dot m \approx 37{,}6\ \text{kg/s}$.

### Zadatak 2 · T1 {#key-task-u08-voda-ulazi-u-sapnicu-promjera-srednjom-brzinom}

[Vrati se na zadatak](u07_kinematika_kontrolni_volumen_i_kontinuitet.qmd#task-u08-voda-ulazi-u-sapnicu-promjera-srednjom-brzinom)

**Sažetak.** Voda ulazi u sapnicu promjera $D_1 = 120\ \text{mm}$ srednjom brzinom $v_1 = 3{,}1\ \text{m/s}$ i izlazi kroz otvor promjera $D_2 = 50\ \text{mm}$. Odredi izlaznu brzinu i maseni protok.

**Naputak.** za nestlačivu vodu vrijedi isti $Q$ kroz oba presjeka; iz $Q = A_1 v_1$ vrati $v_2$ i $\dot m$.

**Kontrolni rezultat ili kriterij.** $Q \approx 35{,}1\ \text{L/s}$; $v_2 \approx 17{,}9\ \text{m/s}$; $\dot m \approx 35{,}0\ \text{kg/s}$.

### Zadatak 3 · T2 {#key-task-u08-u-komoru-za-mijesanje-ulaze-dvije-vodene}

[Vrati se na zadatak](u07_kinematika_kontrolni_volumen_i_kontinuitet.qmd#task-u08-u-komoru-za-mijesanje-ulaze-dvije-vodene)

**Sažetak.** U komoru za miješanje ulaze dvije vodene struje: prva s protokom $Q_1 = 0{,}012\ \text{m}^3/\text{s}$ kroz cijev promjera $D_1 = 90\ \text{mm}$, a druga s protokom $Q_2 = 0{,}008\ \text{m}^3/\text{s}$ kroz cijev promjera $D_2 = 70\…

**Naputak.** za stacionarnu mješalicu vrijedi $\dot m_1 + \dot m_2 = \dot m_3$; za vodu je dovoljno računati preko volumenskih protoka.

**Kontrolni rezultat ili kriterij.** $Q_3 = 20\ \text{L/s}$; $v_3 \approx 1{,}77\ \text{m/s}$.

### Zadatak 4 · T2 {#key-task-u08-u-razdjelnu-glavu-ulazi-voda-protokom-kroz}

[Vrati se na zadatak](u07_kinematika_kontrolni_volumen_i_kontinuitet.qmd#task-u08-u-razdjelnu-glavu-ulazi-voda-protokom-kroz)

**Sažetak.** U razdjelnu glavu ulazi voda protokom $Q = 0{,}030\ \text{m}^3/\text{s}$ kroz cijev promjera $D_1 = 140\ \text{mm}$. Voda izlazi kroz dvije grane promjera $D_2 = 90\ \text{mm}$ i $D_3 = 70\ \text{mm}$, pri čemu je brzina u drugoj grani…

**Naputak.** postavi $Q = Q_2 + Q_3$ i vezu brzina $v_2 = 2v_3$; preko $Q = Av$ zatvori sustav za dvije nepoznanice.

**Kontrolni rezultat ili kriterij.** $v_3 \approx 1{,}81\ \text{m/s}$, $v_2 \approx 3{,}62\ \text{m/s}$; $Q_2 \approx 23{,}0\ \text{L/s}$, $Q_3 \approx 7{,}0\ \text{L/s}$.

### Zadatak 5 · T3 {#key-task-u08-cilindricni-spremnik-promjera-puni-se-dotokom-dok}

[Vrati se na zadatak](u07_kinematika_kontrolni_volumen_i_kontinuitet.qmd#task-u08-cilindricni-spremnik-promjera-puni-se-dotokom-dok)

**Sažetak.** Cilindrični spremnik promjera $D = 1{,}60\ \text{m}$ puni se dotokom $Q_{in} = 0{,}014\ \text{m}^3/\text{s}$, dok kroz odvod stalno izlazi $Q_{out} = 0{,}009\ \text{m}^3/\text{s}$. Odredi brzinu porasta razine u spremniku i vrijeme…

**Naputak.** akumulacija je $Q_{in} - Q_{out}$; zatim vrijedi $A\,dh/dt = Q_{in} - Q_{out}$ i iz toga slijedi vrijeme za zadani porast razine.

**Kontrolni rezultat ili kriterij.** $dh/dt \approx 2{,}49\ \text{mm/s}$; $t \approx 322\ \text{s} \approx 5{,}4\ \text{min}$.

### Zadatak 6 · T4 {#key-task-u08-mijesajuci-spremnik-tlocrtne-povrsine-prima-vodu-gustoce}

[Vrati se na zadatak](u07_kinematika_kontrolni_volumen_i_kontinuitet.qmd#task-u08-mijesajuci-spremnik-tlocrtne-povrsine-prima-vodu-gustoce)

**Sažetak.** Miješajući spremnik tlocrtne površine $A_T = 4{,}8\ \text{m}^2$ prima vodu gustoće $\rho_A=1000\ \text{kg/m}^3$ protokom $Q_A = 0{,}011\ \text{m}^3/\text{s}$ i slanu otopinu gustoće $\rho_B = 1080\ \text{kg/m}^3$ protokom $Q_B = 0{,}004\…

**Naputak.** najprije izračunaj $Q_3 = A_3 v_3$, zatim gustoću mješavine iz masene bilance ulaza, a član akumulacije zatvori preko $Q_A + Q_B - Q_3 = A_T\,dh/dt$. Za najveći porast razine uzmi oba ulazna protoka na gornjoj, a izlaznu brzinu na donjoj granici. Najdulje trajanje slijedi iz $t_{max}=h_{slob}/(dh/dt)_{max}$.

**Kontrolni rezultat ili kriterij.** $Q_3 \approx 8{,}0\ \text{L/s}$; $\rho_{mix} \approx 1020\ \text{kg/m}^3$; $dh/dt \approx 1{,}45\ \text{mm/s}$; akumulirana masa za 6 min $\approx 2{,}55 \cdot 10^3\ \text{kg}$. U nepovoljnoj kombinaciji granica $(dh/dt)_{max}\approx1{,}60\ \text{mm/s}$, pa bi razina za $6\ \text{min}$ porasla približno $0{,}577\ \text{m}$ i premašila slobodni bok za oko $17\ \text{mm}$. Zadani geometrijski kriterij nije zadovoljen; idealizirano vrijeme do ruba iznosi približno $349\ \text{s}$, odnosno $5{,}8\…

## Energijska jednadžba i Bernoulli

### Zadatak 1 · T1 {#key-task-u09-veliki-otvoreni-spremnik-sadrzi-vodu-do-visine}

[Vrati se na zadatak](u08_energijska_jednadzba_i_bernoulli.qmd#task-u09-veliki-otvoreni-spremnik-sadrzi-vodu-do-visine)

**Sažetak.** Veliki otvoreni spremnik sadrži vodu do visine $H = 3{,}20\ \text{m}$ iznad osi male bočne sapnice promjera $d = 26\ \text{mm}$. Zanemari gubitke i odredi izlaznu brzinu mlaza, volumenski protok i maseni protok vode.

**Naputak.** između slobodne površine i izlaza vrijedi Torricelli: $v = \sqrt{2gH}$; nakon toga $Q = Av$ i $\dot m = \rho Q$.

**Kontrolni rezultat ili kriterij.** $v \approx 7{,}92\ \text{m/s}$; $Q \approx 4{,}21\ \text{L/s}$; $\dot m \approx 4{,}20\ \text{kg/s}$.

### Zadatak 2 · T1 {#key-task-u09-horizontalnim-ventilacijskim-kanalom-smanjuje-se-presjek-s}

[Vrati se na zadatak](u08_energijska_jednadzba_i_bernoulli.qmd#task-u09-horizontalnim-ventilacijskim-kanalom-smanjuje-se-presjek-s)

**Sažetak.** Horizontalnim ventilacijskim kanalom smanjuje se presjek s $A_1 = 0{,}060\ \text{m}^2$ na $A_2 = 0{,}020\ \text{m}^2$. Volumenski protok zraka iznosi $Q = 0{,}42\ \text{m}^3/\text{s}$, a gustoća zraka je $\rho = 1{,}20\ \text{kg/m}^3$.…

**Naputak.** iz kontinuiteta dobij $v_1$ i $v_2$, a za horizontalni kanal bez gubitaka vrijedi $p_1 + \rho v_1^2/2 = p_2 + \rho v_2^2/2$.

**Kontrolni rezultat ili kriterij.** $v_1 = 7{,}0\ \text{m/s}$, $v_2 = 21{,}0\ \text{m/s}$; $\Delta p \approx 235\ \text{Pa}$.

### Zadatak 3 · T2 {#key-task-u09-idealna-venturijeva-cijev-za-vodu-ima-ulazni}

[Vrati se na zadatak](u08_energijska_jednadzba_i_bernoulli.qmd#task-u09-idealna-venturijeva-cijev-za-vodu-ima-ulazni)

**Sažetak.** Idealna Venturijeva cijev za vodu ima ulazni promjer $D_1 = 120\ \text{mm}$ i promjer grla $D_2 = 70\ \text{mm}$. Razlika statičkih tlakova između ulaza i grla iznosi $\Delta p = 24\ \text{kPa}$. Odredi brzinu u grlu i volumenski protok…

**Naputak.** spoji kontinuitet $A_1 v_1 = A_2 v_2$ s Bernoullijem između ulaza i grla, pa riješi dvije nepoznate brzine.

**Kontrolni rezultat ili kriterij.** $v_2 \approx 7{,}38\ \text{m/s}$; $Q \approx 28{,}4\ \text{L/s}$.

### Zadatak 4 · T2 {#key-task-u09-pitotova-cijev-uronjena-je-u-vodeni-tok}

[Vrati se na zadatak](u08_energijska_jednadzba_i_bernoulli.qmd#task-u09-pitotova-cijev-uronjena-je-u-vodeni-tok)

**Sažetak.** Pitotova cijev uronjena je u vodeni tok. Razlika između stagnacijskog i statičkog tlaka iznosi $\Delta p = 8{,}5\ \text{kPa}$. Odredi lokalnu brzinu strujanja.

**Naputak.** u Pitotu vrijedi $\Delta p = \rho v^2/2$, pa brzina slijedi iz $v = \sqrt{2\Delta p/\rho}$.

**Kontrolni rezultat ili kriterij.** $v \approx 4{,}13\ \text{m/s}$.

### Zadatak 5 · T3 {#key-task-u09-idealni-sifon-prazni-otvoreni-spremnik-razlika-razina}

[Vrati se na zadatak](u08_energijska_jednadzba_i_bernoulli.qmd#task-u09-idealni-sifon-prazni-otvoreni-spremnik-razlika-razina)

**Sažetak.** Idealni sifon prazni otvoreni spremnik. Razlika razina između slobodne površine u spremniku i izlaza sifona iznosi $\Delta z = 2{,}8\ \text{m}$, a vrh sifona nalazi se $1{,}1\ \text{m}$ iznad slobodne površine. Odredi brzinu strujanja…

**Naputak.** brzinu dobij iz Bernoullija između slobodne površine i izlaza, a tlak u vrhu iz Bernoullija između slobodne površine i vrha sifona. Uz manometarski tlak vrijedi $HGL_C=z_C+p_{M,C}/(\rho g)$, dok se kavitacija provjerava apsolutnim tlakom.

**Kontrolni rezultat ili kriterij.** $v \approx 7{,}41\ \text{m/s}$; $p_C \approx 62{,}8\ \text{kPa}$ (aps.); $HGL_C=-2{,}8\ \text{m}$ u odnosu na slobodnu površinu; $p_C-p_v\approx60{,}5\ \text{kPa}$, pa idealni račun pokazuje pozitivnu rezervu.

### Zadatak 6 · T4 {#key-task-u09-idealni-sifon-promjera-prazni-otvoreni-spremnik-tako}

[Vrati se na zadatak](u08_energijska_jednadzba_i_bernoulli.qmd#task-u09-idealni-sifon-promjera-prazni-otvoreni-spremnik-tako)

**Sažetak.** Idealni sifon promjera $D = 70\ \text{mm}$ prazni otvoreni spremnik tako da je izlaz vodoravan i nalazi se $\Delta z = 2{,}6\ \text{m}$ ispod slobodne površine. Vrh sifona je $z_C = 1{,}7\ \text{m}$ iznad slobodne površine, a izlaz se…

**Naputak.** Bernoullijem između slobodne površine i izlaza vrati idealni $v$, između slobodne površine i vrha sifona vrati tlak, a domet mlaza zatvori kao vodoravno izbačeno tijelo s visine $1{,}2\ \text{m}$. Za izvedeni sustav koristi $v=\sqrt{2g\Delta z/(1+K_\Sigma)}$ i $p_C=p_{atm}-\rho g[z_C+(1+K_C)v^2/(2g)]$. Najmanji protok daje najveći $K_\Sigma$; najmanji tlak u vrhu provjeri konzervativnim kutovima zadanih intervala, ne samo nominalnim koeficijentima.

**Kontrolni rezultat ili kriterij.** Idealni model daje $v \approx 7{,}14\ \text{m/s}$; $Q \approx 27{,}5\ \text{L/s}$; $p_C \approx 59{,}2\ \text{kPa}$ (aps.); domet $x \approx 3{,}53\ \text{m}$. Za $K_\Sigma=2{,}0$ stvarni je protok približno $15{,}9\ \text{L/s}$, a za interval $K_\Sigma=1{,}5$--$2{,}5$ iznosi približno $17{,}4$--$14{,}7\ \text{L/s}$. Konzervativni tlak u vrhu ostaje oko $59{,}2\ \text{kPa}$ apsolutno, pa je tlačni zahtjev zadovoljen, ali se zahtjev protoka ne može zajamčiti. Potrebno je smanjiti gubitke…

## Kompresibilni idealni tok

### Zadatak 1 · T1 {#key-task-brzina-zvuka-helium}

[Vrati se na zadatak](u09_kompresibilni_idealni_tok.qmd#task-brzina-zvuka-helium)

**Sažetak.** Izračunaj brzinu zvuka u heliju pri $300\ \text{K}$ za $\gamma=1{,}667$ i $R=2077\ \text{J/(kg K)}$. Nacrtaj smjer širenja poremećaja.

**Kontrolni rezultat ili kriterij.** $a\approx1019\ \text{m/s}$.

### Zadatak 2 · T1 {#key-task-mach-ventilacija}

[Vrati se na zadatak](u09_kompresibilni_idealni_tok.qmd#task-mach-ventilacija)

**Sažetak.** Zrak pri $20\ ^\circ\text{C}$ struji vodom $D=0{,}20\ \text{m}$ protokom $2{,}0\ \text{m}^3/\text{s}$. Odredi $Ma$ i obrazloži izbor modela.

**Kontrolni rezultat ili kriterij.** $Ma\approx0{,}186$.

### Zadatak 3 · T2 {#key-task-stagnacijska-temperatura}

[Vrati se na zadatak](u09_kompresibilni_idealni_tok.qmd#task-stagnacijska-temperatura)

**Sažetak.** Za zrak pri $T=240\ \text{K}$ i $Ma=1{,}5$ izračunaj $T_0$. Zatim procijeni rezultat preko $v^2/(2c_p)$.

**Kontrolni rezultat ili kriterij.** $T_0=348\ \text{K}$.

### Zadatak 4 · T2 {#key-task-priguseni-protok}

[Vrati se na zadatak](u09_kompresibilni_idealni_tok.qmd#task-priguseni-protok)

**Sažetak.** Odredi kritični nizvodni tlak za zrak iz spremnika pri $p_0=8\ \text{bar(abs)}$. Ne računaj kapacitet ventila.

**Kontrolni rezultat ili kriterij.** $p^*\approx4{,}23\ \text{bar(abs)}$.

### Zadatak 5 · T3 {#key-task-sapnica-model}

[Vrati se na zadatak](u09_kompresibilni_idealni_tok.qmd#task-sapnica-model)

**Sažetak.** U konvergentnoj sapnici za zrak izmjereni su $p_0=600\pm3\ \text{kPa(abs)}$, $T_0=300\pm1\ \text{K}$ i prigušeni maseni protok $\dot m=0{,}0595\pm0{,}0006\ \text{kg/s}$. Geometrijski otvor ima površinu $A_g=50{,}0\ \text{mm}^2$, a…

**Naputak.** napiši prigušeni protok kao $\dot m=C_dA_{eff}K(p_0,T_0)$ i najprije iz mjerenja odredi samo produkt $C_dA_{eff}$. Za propagaciju upotrijebi relativne osjetljivosti $+1$ na $\dot m$, $-1$ na $A_{eff}$, $-1$ na $p_0$ i $+1/2$ na $T_0$.

**Kontrolni rezultat ili kriterij.** $C_dA_{eff}\approx42{,}50\ \text{mm}^2$; uz neovisno kalibrirano $A_{eff}$ slijedi $C_d\approx0{,}885$ i $u(C_d)\approx0{,}014$. Bez neovisne geometrijske ili protokovne kalibracije mjerenje određuje samo produkt, pa su $A_{eff}$ i $C_d$ neidentifikabilni zasebno.

### Zadatak 6 · T4 {#key-task-udarni-val-podaci}

[Vrati se na zadatak](u09_kompresibilni_idealni_tok.qmd#task-udarni-val-podaci)

**Sažetak.** U zračnom kanalu mjereni su apsolutni statički tlakovi neposredno prije i poslije približno normalnoga vala: $p_1=80{,}0\pm0{,}4\ \text{kPa}$ i $p_2=360{,}0\pm1{,}8\ \text{kPa}$. Pitot-mjerenja daju ukupne tlakove $p_{01}=626\pm4\…

**Naputak.** iz $p_2/p_1=1+2\gamma(M_1^2-1)/(\gamma+1)$ najprije izoliraj $M_1$. Nesigurnost omjera statičkih tlakova propagiraj iz oba senzora; izmjereni omjer ukupnih tlakova usporedi s normalno-udarnom relacijom pri dobivenom $M_1$.

**Kontrolni rezultat ili kriterij.** $p_2/p_1=4{,}500$, $M_1=2{,}000\pm0{,}007$; teorijski $p_{02}/p_{01}=0{,}7209\pm0{,}0032$, a izmjereni omjer je $0{,}7204\pm0{,}0079$. Kombinirana standardna nesigurnost razlike iznosi $0{,}0085$, pa je normirana razlika samo oko $0{,}050$ i podaci su konzistentni s modelom normalnoga vala. Bez $p_{01}$ i $p_{02}$ statička mjerenja određuju $M_1$, ali ne mjere izravno pad ukupnog tlaka.

## Količina i moment količine gibanja

### Zadatak 1 · T1 {#key-task-u11-vodeni-mlaz-promjera-izlazi-iz-sapnice-brzinom}

[Vrati se na zadatak](u10_kolicina_i_moment_kolicine_gibanja.qmd#task-u11-vodeni-mlaz-promjera-izlazi-iz-sapnice-brzinom)

**Sažetak.** Vodeni mlaz promjera $d = 38\ \text{mm}$ izlazi iz sapnice brzinom $v = 22\ \text{m/s}$ i udara okomito na nepomičnu ravnu ploču. Odredi maseni protok i silu koju mlaz prenosi na ploču.

**Naputak.** $\dot m = \rho Av$; za ravnu ploču izlazna komponenta u osi mlaza je nula pa je $F = \dot m v$.

**Kontrolni rezultat ili kriterij.** $\dot m \approx 24{,}9\ \text{kg/s}$; $F \approx 548\ \text{N}$.

### Zadatak 2 · T1 {#key-task-u11-mlaz-vode-udara-okomito-na-nepomicnu-plocu}

[Vrati se na zadatak](u10_kolicina_i_moment_kolicine_gibanja.qmd#task-u11-mlaz-vode-udara-okomito-na-nepomicnu-plocu)

**Sažetak.** Mlaz vode udara okomito na nepomičnu ploču i sila na ploču iznosi $F = 310\ \text{N}$. Promjer mlaza je $d = 42\ \text{mm}$. Odredi brzinu mlaza i volumenski protok.

**Naputak.** iz relacije $F = \rho A v^2$ vrati $v$, a zatim $Q = Av$.

**Kontrolni rezultat ili kriterij.** $v \approx 15{,}0\ \text{m/s}$; $Q \approx 20{,}7\ \text{L/s}$.

### Zadatak 3 · T2 {#key-task-u11-horizontalno-koljeno-zakrece-tok-vode-za-bez}

[Vrati se na zadatak](u10_kolicina_i_moment_kolicine_gibanja.qmd#task-u11-horizontalno-koljeno-zakrece-tok-vode-za-bez)

**Sažetak.** Horizontalno koljeno zakreće tok vode za $90^\circ$ bez promjene promjera. Cijev ima promjer $D = 100\ \text{mm}$, protok je $Q = 0{,}026\ \text{m}^3/\text{s}$, ulazni manometarski tlak $p_1 = 180\ \text{kPa}$, a izlazni $p_2 = 150\…

**Naputak.** iz $Q$ prvo dobij brzinu; zatim u x i y smjeru zbroji tlakove na presjecima i promjenu količine gibanja.

**Kontrolni rezultat ili kriterij.** $v \approx 3{,}31\ \text{m/s}$; komponente sile fluida na koljeno $F_x \approx 1{,}50\ \text{kN}$, $F_y \approx -1{,}26\ \text{kN}$; rezultanta $\approx 1{,}96\ \text{kN}$.

### Zadatak 4 · T2 {#key-task-u11-t-racva-prima-vodu-kroz-ulaz-promjera}

[Vrati se na zadatak](u10_kolicina_i_moment_kolicine_gibanja.qmd#task-u11-t-racva-prima-vodu-kroz-ulaz-promjera)

**Sažetak.** T-račva prima vodu kroz ulaz promjera $D_1 = 120\ \text{mm}$ s protokom $Q_1 = 0{,}030\ \text{m}^3/\text{s}$. U vodoravni izlaz promjera $D_2 = 80\ \text{mm}$ odlazi $Q_2 = 0{,}018\ \text{m}^3/\text{s}$, a ostatak izlazi okomito prema…

**Naputak.** kontinuitetom zatvori $Q_3$, zatim u svakoj osi napiši jednadžbu količine gibanja za cijelu račvu.

**Kontrolni rezultat ili kriterij.** $Q_3 = 12\ \text{L/s}$; reakcija nosača $\approx 2{,}39\ \text{kN}$ (pretežno u osi ulaza), okomita komponenta $\approx 37\ \text{N}$.

### Zadatak 5 · T3 {#key-task-u11-konvergentna-mlaznica-ima-ulazni-promjer-izlazni-promjer}

[Vrati se na zadatak](u10_kolicina_i_moment_kolicine_gibanja.qmd#task-u11-konvergentna-mlaznica-ima-ulazni-promjer-izlazni-promjer)

**Sažetak.** Konvergentna mlaznica ima ulazni promjer $D_1 = 110\ \text{mm}$, izlazni promjer $D_2 = 45\ \text{mm}$ i protok vode $Q = 0{,}018\ \text{m}^3/\text{s}$. Ulazni manometarski tlak iznosi $p_1 = 240\ \text{kPa}$, a mlaz izlazi u atmosferu.…

**Naputak.** iz kontinuiteta dobij brzine u oba presjeka; zatim za unutarnji kontrolni volumen spoji tlak na ulazu i promjenu količine gibanja.

**Kontrolni rezultat ili kriterij.** $v_1 \approx 1{,}89\ \text{m/s}$, $v_2 \approx 11{,}3\ \text{m/s}$; sila u vijcima prirubnice $\approx 2{,}11\ \text{kN}$.

### Zadatak 6 · T4 {#key-task-u11-vodoravna-y-racva-prima-vodu-kroz-ulaz}

[Vrati se na zadatak](u10_kolicina_i_moment_kolicine_gibanja.qmd#task-u11-vodoravna-y-racva-prima-vodu-kroz-ulaz)

**Sažetak.** Vodoravna Y-račva prima vodu kroz ulaz promjera $D_1 = 140\ \text{mm}$ pri protoku $Q_1 = 0{,}040\ \text{m}^3/\text{s}$ i ulaznom manometarskom tlaku $p_1 = 185\ \text{kPa}$. Šezdeset posto protoka odlazi ravno kroz izlaz promjera $D_2 =…

**Naputak.** najprije iz zadanog udjela vrati $Q_2$ i $Q_3$, zatim preko presjeka dobij brzine u svim granama, a na kraju po osima $x$ i $y$ napiši jednadžbu količine gibanja uz ulaznu tlaknu silu. Za omotač nesigurnosti izračunaj rezultantu u rubnim kombinacijama $p_1$, $Q_1$ i udjela protoka; zbog kvadratne ovisnosti članova količine gibanja nije dovoljno samo uvećati nominalnu rezultantu za jedan postotak.

**Kontrolni rezultat ili kriterij.** $Q_2 = 24\ \text{L/s}$, $Q_3 = 16\ \text{L/s}$; $F_x \approx 2{,}84\ \text{kN}$, $F_y \approx -44\ \text{N}$; rezultanta $\approx 2{,}84\ \text{kN}$. Rubne kombinacije daju najveću očekivanu rezultantu približno $2{,}92\ \text{kN}$. Zadani faktor daje kriterij od oko $3{,}36\ \text{kN}$, pa deklariranih $3{,}0\ \text{kN}$ ne zadovoljava taj pojedinačni kriterij, dok bi $3{,}5\ \text{kN}$ zadovoljilo samo tu usporedbu. Potpuni odabir traži zasebnu provjeru nosača, spojeva i svih kombinacija…

## Dimenzijska analiza i sličnost

### Zadatak 1 · T1 {#key-task-u14-krv-tece-arteriolom-promjera-brzinom-a-voda}

[Vrati se na zadatak](u11_dimenzijska_analiza_i_slicnost.qmd#task-u14-krv-tece-arteriolom-promjera-brzinom-a-voda)

**Sažetak.** Krv teče arteriolom promjera $D = 0{,}3\ \text{mm}$ brzinom $v = 5\ \text{mm/s}$ ($\nu = 3{,}3 \cdot 10^{-6}\ \text{m}^2/\text{s}$), a voda gradskim vodom promjera $D = 0{,}3\ \text{m}$ brzinom $v = 1{,}5\ \text{m/s}$ ($\nu = 1{,}0 \cdot…

**Naputak.** $Re = vD/\nu$; za kružnu cijev usporedi s orijentacijskim područjima režima, bez prijenosa praga $2300$ na geometriju arteriole.

**Kontrolni rezultat ili kriterij.** $Re_{krv} \approx 0{,}45$ — viskoznost dominira; $Re_{voda} \approx 4{,}5 \cdot 10^5$ — inercija dominira.

### Zadatak 2 · T1 {#key-task-u14-zrak-struji-vodom-promjera-lokalnim-volumenskim-protokom}

[Vrati se na zadatak](u11_dimenzijska_analiza_i_slicnost.qmd#task-u14-zrak-struji-vodom-promjera-lokalnim-volumenskim-protokom)

**Sažetak.** Zrak struji vodom promjera $D = 100\ \text{mm}$ lokalnim volumenskim protokom $Q = 0{,}5\ \text{m}^3/\text{s}$; brzina zvuka $a = 340\ \text{m/s}$. Odredi brzinu i Machov broj te prosudi je li, bez velikih toplinskih i tlačnih promjena…

**Naputak.** $v=Q/A$, $Ma=v/a$; vrijednost $0{,}3$ uzmi kao orijentacijski prag.

**Kontrolni rezultat ili kriterij.** $v\approx63{,}7\ \text{m/s}$, $Ma\approx0{,}19$; prema zadanom kriteriju nestlačiva je aproksimacija razumna uz navedene dodatne pretpostavke.

### Zadatak 3 · T2 {#key-task-u14-na-referentnom-presjeku-usisa-crpke-apsolutni-tlak}

[Vrati se na zadatak](u11_dimenzijska_analiza_i_slicnost.qmd#task-u14-na-referentnom-presjeku-usisa-crpke-apsolutni-tlak)

**Sažetak.** Na referentnom presjeku usisa crpke apsolutni tlak iznosi $p_{ref}=80\ \text{kPa}$, brzina $v_{ref}=4\ \text{m/s}$, gustoća vode $\rho=1000\ \text{kg/m}^3$, a tlak zasićene pare $p_v=2340\ \text{Pa}$. Ispitivanje iste crpke, pri istoj…

**Naputak.** koristi iste referentne veličine kao u definiciji kritične vrijednosti.

**Kontrolni rezultat ili kriterij.** $\sigma_{kav}\approx9{,}7>\sigma_{kr}=3{,}0$; prema zadanoj karakteristici crpka ima rezervu u toj radnoj točki.

### Zadatak 4 · T2 {#key-task-u14-kap-goriva-promjera-izlozena-je-relativnoj-struji}

[Vrati se na zadatak](u11_dimenzijska_analiza_i_slicnost.qmd#task-u14-kap-goriva-promjera-izlozena-je-relativnoj-struji)

**Sažetak.** Kap goriva promjera $d=0{,}15\ \text{mm}$ izložena je relativnoj struji zraka brzine $v=80\ \text{m/s}$ ($\rho_{zr}=1{,}2\ \text{kg/m}^3$, $\sigma=0{,}025\ \text{N/m}$). Za ovaj pojednostavljeni slučaj zanemari viskozne učinke i kao…

**Naputak.** izračunaj $We=\rho_{zr}v^2d/\sigma$ i usporedi ga sa zadanim pragom, ali odvoji „početak raspada” od „kvalitete atomizacije”.

**Kontrolni rezultat ili kriterij.** $We\approx46>12$; pojednostavljeni kriterij predviđa raspad, ali bez viskoznosti, omjera gustoća i modela sekundarnog raspada ne određuje raspodjelu veličina kapljica.

### Zadatak 5 · T3 {#key-task-u14-frekvencija-otpustanja-vrtloga-iza-geometrijski-slicnog-tijela}

[Vrati se na zadatak](u11_dimenzijska_analiza_i_slicnost.qmd#task-u14-frekvencija-otpustanja-vrtloga-iza-geometrijski-slicnog-tijela)

**Sažetak.** Frekvencija otpuštanja vrtloga $f$ iza geometrijski sličnog tijela ovisi o brzini neporemećene struje $v$, karakterističnoj duljini $D$, gustoći $\rho$ i dinamičkoj viskoznosti $\mu$. Buckinghamovim postupkom, uz ponavljajuće varijable…

**Naputak.** u popis uključi i zavisnu varijablu $f$; tek potom primijeni $n-k$. Nemoj unaprijed uvrstiti gotove definicije $St$ i $Re$.

**Kontrolni rezultat ili kriterij.** $n=5$, $k=3$, pa nastaju dvije grupe; izborom ponavljajućih varijabli dobivaju se $\Pi_1=fD/v=St$ i $\Pi_2=\rho vD/\mu=Re$, odnosno $St=\Phi(Re)$. Za zadani slučaj $Re=4{,}00\cdot10^4$ i $f=St\,v/D=45{,}6\ \text{Hz}$. Dimenzijska analiza određuje oblik ovisnosti, ali broj $St=0{,}190$ dolazi iz mjerenja ili odgovarajućega modela, ne iz samog Buckinghamova postupka.

### Zadatak 6 · T4 {#key-task-u14-preljev-brane-ispituje-se-vodenim-modelom-u}

[Vrati se na zadatak](u11_dimenzijska_analiza_i_slicnost.qmd#task-u14-preljev-brane-ispituje-se-vodenim-modelom-u)

**Sažetak.** Preljev brane ispituje se vodenim modelom u mjerilu $\lambda_L=30$, pri istom gravitacijskom ubrzanju i gustoći kao prototip. Prototip pri projektnom protoku ima brzinu preljeva $v_p=6{,}0\ \text{m/s}$ i protok $Q_p=480\…

**Naputak.** čuvaj $Fr$ te koristi $v_m=v_p/\sqrt{\lambda_L}$, $Q_m=Q_p/\lambda_L^{5/2}$ i, zbog jednake gustoće, $F_m=F_p/\lambda_L^3$. Zatim izračunaj $Re_m=v_mh_m/\nu$.

**Kontrolni rezultat ili kriterij.** $v_m\approx1{,}10\ \text{m/s}$; $Q_m\approx97{,}4\ \text{L/s}$; $F_m\approx8{,}15\ \text{N}$; $Re_m\approx2{,}7\cdot10^5$. Model je vjerojatno turbulentan, ali veličina viskozne mjerilne pogreške mora se provjeriti korekcijom otpora, nizom modelskih mjerila ili podatcima — ne slijedi samo iz oznake „turbulentno”.

## Diferencijalni opis realnog toka

### Zadatak 1 · T1 {#key-task-materijalna-derivacija}

[Vrati se na zadatak](u12_diferencijalni_opis_realnog_toka.qmd#task-materijalna-derivacija)

**Sažetak.** Za $u(x,t)=2t+x^2$ odredi lokalno, konvektivno i ukupno ubrzanje u $x=1\ \text{m}$, $t=2\ \text{s}$ uz konzistentne SI jedinice koeficijenata.

**Kontrolni rezultat ili kriterij.** $u=5\ \text{m/s}$, $a_{lok}=2$, $a_{kon}=10$, $a=12\ \text{m/s}^2$.

### Zadatak 2 · T1 {#key-task-viskozna-difuzija}

[Vrati se na zadatak](u12_diferencijalni_opis_realnog_toka.qmd#task-viskozna-difuzija)

**Sažetak.** Procijeni vrijeme viskozne difuzije $t_\nu\sim H^2/\nu$ kroz sloj vode $H=10\ \text{mm}$ pri $20\ ^\circ\text{C}$, za $\nu=1{,}00\cdot10^{-6}\ \text{m}^2/\text{s}$. Obrazloži red veličine.

**Kontrolni rezultat ili kriterij.** $t_\nu\sim100\ \text{s}$.

### Zadatak 3 · T2 {#key-task-poiseuille-inverzni}

[Vrati se na zadatak](u12_diferencijalni_opis_realnog_toka.qmd#task-poiseuille-inverzni)

**Sažetak.** U kapilari su izmjereni $Q=0{,}300\pm0{,}003\ \text{mL/min}$, $\Delta p=652\pm5\ \text{Pa}$, $L=0{,}200\pm0{,}001\ \text{m}$ i $D=0{,}500\pm0{,}005\ \text{mm}$. Fluid je Newtonski, gustoće $\rho=998\ \text{kg/m}^3$. Odredi dinamičku…

**Naputak.** invertiraj $Q=\pi D^4\Delta p/(128\mu L)$. Za neovisne ulaze vrijedi $[u(\mu)/\mu]^2=[4u(D)/D]^2+[u(\Delta p)/\Delta p]^2+[u(L)/L]^2+[u(Q)/Q]^2$.

**Kontrolni rezultat ili kriterij.** $\mu\approx1{,}000\ \text{mPa s}$, $u(\mu)\approx0{,}042\ \text{mPa s}$ i $Re\approx12{,}7$. Sam promjer doprinosi relativnoj nesigurnosti od $4\,\%$, pa dominira zadanim mjernim budžetom.

### Zadatak 4 · T2 {#key-task-couette-povrat}

[Vrati se na zadatak](u12_diferencijalni_opis_realnog_toka.qmd#task-couette-povrat)

**Sažetak.** Newtonski fluid viskoznosti $\mu=0{,}100\ \text{Pa s}$ nalazi se između nepomične donje i gornje ploče koja se giba brzinom $U=2{,}00\ \text{m/s}$; razmak je $H=1{,}00\ \text{mm}$. Za potpuno razvijeni profil…

**Naputak.** deriviraj profil i postavi $\tau_0=\mu(du/dy)_{y=0}=0$; predznak gradijenta mora odgovarati nepovoljnom porastu tlaka u smjeru gibanja gornje ploče.

**Kontrolni rezultat ili kriterij.** $(dp/dx)_{krit}=4{,}00\cdot10^5\ \text{Pa/m}$; pri $0{,}90$ te vrijednosti $\tau_0=+20{,}0\ \text{Pa}$, a pri $1{,}10$ vrijedi $\tau_0=-20{,}0\ \text{Pa}$. Promjena predznaka zidnog naprezanja označuje početak lokalnog povratnog toka na donjoj stijenci.

### Zadatak 5 · T3 {#key-task-granicni-sloj-model}

[Vrati se na zadatak](u12_diferencijalni_opis_realnog_toka.qmd#task-granicni-sloj-model)

**Sažetak.** Voda pri $20\ ^\circ\text{C}$ ($\nu=1{,}00\cdot10^{-6}\ \text{m}^2/\text{s}$, $\rho=998\ \text{kg/m}^3$) struji uz nominalno ravnu plohu. U presjeku $x=0{,}400\ \text{m}$ izmjereno je $U_e=1{,}50\ \text{m/s}$ i $dU_e/dx=-0{,}250\…

**Naputak.** Blasius zahtijeva glatku plohu, laminaran tok i praktično nulti gradijent tlaka odnosno stalnu $U_e$. Negativan $dU_e/dx$ odgovara nepovoljnom gradijentu tlaka; procijeni i njegovu važnost prije odluke.

**Kontrolni rezultat ili kriterij.** $Re_x=6{,}00\cdot10^5$, $\delta_{99}\approx2{,}58\ \text{mm}$, $k_s/\delta_{99}\approx1{,}94\cdot10^{-3}$ i $(x/U_e)dU_e/dx=-0{,}0667$. Hrapavost je mala prema procijenjenoj debljini, ali mjerljiva promjena $U_e$ krši pretpostavku nultoga gradijenta tlaka, a stanje laminarnosti pri tom $Re_x$ nije dokazano; Blasius zato nije opravdan bez dodatne provjere profila i prijelaza.

### Zadatak 6 · T4 {#key-task-cfd-tri-mreze}

[Vrati se na zadatak](u12_diferencijalni_opis_realnog_toka.qmd#task-cfd-tri-mreze)

**Sažetak.** Za Poiseuilleov paket iz `data/cfd/poiseuille_laminar` tri mreže imaju omjer koraka $h/h_f=4,2,1$, protoke $Q=(8{,}16814;\ 7{,}93252;\ 7{,}87362)\cdot10^{-6}\ \text{m}^3/\text{s}$ i masene debalanse $(0{,}040;\ 0{,}010;\ 0{,}0025)\,\%$.…

**Naputak.** za $r=2$ koristi $p=\ln[(Q_c-Q_m)/(Q_m-Q_f)]/\ln r$, zatim $Q_{ext}=Q_f+(Q_f-Q_m)/(r^p-1)$ i $GCI_f=F_s|(Q_f-Q_m)/Q_f|/(r^p-1)$.

**Kontrolni rezultat ili kriterij.** $p\approx2{,}000$, $Q_{ext}\approx7{,}85398\cdot10^{-6}\ \text{m}^3/\text{s}$, $GCI_f\approx0{,}312\,\%$ i fini maseni debalans iznosi $0{,}0025\,\%$. Arhiva profila ne sadrži reziduale, povijesti monitoriranih sila, masenu bilancu ni potpuni mjerni budžet nesigurnosti; zato je korisna za usporedbu integralnih koeficijenata i mrežnog trenda, ali ne zatvara validacijsku presudu.

## Gubitci, cjevovodi, crpke i mreže

### Zadatak 1 · T1 {#key-task-gubitci-ravne-dionice}

[Vrati se na zadatak](u13_gubici_cjevovodi_crpke_i_mreze.qmd#task-gubitci-ravne-dionice)

**Sažetak.** Gubitci ravne dionice — Voda gustoće $998\ \mathrm{kg/m^3}$ protječe cijevi $D=0{,}10\ \mathrm{m}$, $L=50\ \mathrm{m}$ protokom $Q=0{,}012\ \mathrm{m^3/s}$. Zadano je $\lambda=0{,}025$ i $\sum\xi=4{,}0$. Odredi brzinu, linijski i lokalni…

**Naputak.** Najprije izračunaj $A$ i $v=Q/A$. Tek zatim zajedničku brzinsku visinu pomnoži s $\lambda L/D$ odnosno $\sum\xi$.

**Kontrolni rezultat ili kriterij.** $v=1{,}528\ \mathrm{m/s}$, $h_l=1{,}487\ \mathrm{m}$, $h_{loc}=0{,}476\ \mathrm{m}$, $h_w=1{,}963\ \mathrm{m}$ i $\Delta p=19{,}2\ \mathrm{kPa}$. Provjeri da je $\Delta p/(\rho g)=h_w$.

### Zadatak 2 · T1 {#key-task-laminarna-cijev-smjese}

[Vrati se na zadatak](u13_gubici_cjevovodi_crpke_i_mreze.qmd#task-laminarna-cijev-smjese)

**Sažetak.** Laminarna cijev viskozne smjese — Smjesa gustoće $1100\ \mathrm{kg/m^3}$ i $\nu=3{,}0\cdot10^{-6}\ \mathrm{m^2/s}$ protječe kružnom cijevi $D=6{,}0\ \mathrm{mm}$, $L=5{,}0\ \mathrm{m}$ protokom $Q=6{,}0\cdot10^{-6}\ \mathrm{m^3/s}$.…

**Naputak.** Izračunaj režim prije izbora korelacije. Ako je tok laminaran, upotrijebi $\lambda=64/Re$; rezultat zatim provjeri Poiseuilleovim zakonom.

**Kontrolni rezultat ili kriterij.** $v=0{,}212\ \mathrm{m/s}$, $Re=424$, $\lambda=0{,}1508$ i $\Delta p=3{,}11\ \mathrm{kPa}$. Udvostručenje $Q$ uz ostale iste podatke udvostručuje $\Delta p$ dok tok ostaje laminaran.

### Zadatak 3 · T2 {#key-task-raspodjela-paralelnih-grana}

[Vrati se na zadatak](u13_gubici_cjevovodi_crpke_i_mreze.qmd#task-raspodjela-paralelnih-grana)

**Sažetak.** Raspodjela kroz dvije paralelne grane — Između istih čvorova spojene su grane s približno konstantnim otporima $R_1=12\,000\ \mathrm{s^2/m^5}$ i $R_2=48\,000\ \mathrm{s^2/m^5}$. Ukupni protok iznosi $Q=0{,}020\ \mathrm{m^3/s}$. Odredi…

**Naputak.** Postavi $R_1Q_1^2=R_2Q_2^2$ i $Q_1+Q_2=Q$. Prije računa predvidi koja grana nosi veći protok.

**Kontrolni rezultat ili kriterij.** $Q_1=13{,}33\ \mathrm{L/s}$, $Q_2=6{,}67\ \mathrm{L/s}$ i $h_{AB}=2{,}13\ \mathrm{m}$. Obje grane moraju vratiti isti $h_{AB}$.

### Zadatak 4 · T2 {#key-task-radna-tocka-tri-snage}

[Vrati se na zadatak](u13_gubici_cjevovodi_crpke_i_mreze.qmd#task-radna-tocka-tri-snage)

**Sažetak.** Radna točka i tri razine snage — Za $Q$ u $\mathrm{m^3/s}$ zadane su krivulje $H_p=30-30\,000Q^2$ i $H_s=8+20\,000Q^2$. Za vodu uzmi $\rho=1000\ \mathrm{kg/m^3}$. U radnoj točki vrijede $\eta_p=0{,}76$ i $\eta_m=0{,}92$; gubitke…

**Naputak.** Najprije izjednači krivulje. Zatim slijedi pretvorbeni lanac $P_h=\rho gQH$, $P_{vr}=P_h/\eta_p$, $P_{el}=P_{vr}/\eta_m$.

**Kontrolni rezultat ili kriterij.** $Q_{op}=20{,}98\ \mathrm{L/s}$, $H_{op}=16{,}8\ \mathrm{m}$, $P_h=3{,}46\ \mathrm{kW}$, $P_{vr}=4{,}55\ \mathrm{kW}$ i $P_{el}=4{,}94\ \mathrm{kW}$. Provjeri da snage rastu prema električnom ulazu.

### Zadatak 5 · T3 {#key-task-robustan-izbor-promjera}

[Vrati se na zadatak](u13_gubici_cjevovodi_crpke_i_mreze.qmd#task-robustan-izbor-promjera)

**Sažetak.** Robustan izbor promjera — Vod duljine $L=150\ \mathrm{m}$ mora prenositi $Q=0{,}018\ \mathrm{m^3/s}$. Zbroj lokalnih koeficijenata iznosi $6{,}0$, a zbog starenja je $\lambda$ između 0,020 i 0,028. Dostupni su promjeri 80, 100 i 125 mm.…

**Naputak.** Za svaki kandidat izračunaj brzinu, a zatim raspon $h_w$ za obje granice $\lambda$. Odluku donesi prema najvećem, ne srednjem gubitku.

**Kontrolni rezultat ili kriterij.** Rasponi $h_w$ su približno 28,4–38,2 m za 80 mm, 9,64–12,85 m za 100 mm i 3,29–4,34 m za 125 mm. Najmanji robustan izbor jest 100 mm. Provjera odluke jest gornja granica $12{,}85<15\ \mathrm{m}$.

### Zadatak 6 · T4 {#key-task-regulacija-energija-npsh}

[Vrati se na zadatak](u13_gubici_cjevovodi_crpke_i_mreze.qmd#task-regulacija-energija-npsh)

**Sažetak.** Regulacija crpke, godišnja energija i usisna rezerva — Crpka pri nazivnoj brzini ima $H_p(q)=24-0{,}012q^2$, gdje je $q$ u $\mathrm{L/s}$. Izvorni sustav ima $H_s(q)=5+0{,}025q^2$. Prigušivanje ventila mijenja ga u…

**Naputak.** Prigušenu radnu točku dobiješ iz $H_p=H_{s,V}$. Za otvoren sustav pri istom $q$ vrijedi $H_{p,s}(q)=24s^2-0{,}012q^2=H_s(q)$. Energiju računaj iz $P_{el}=\rho gQH/0{,}72$. Za usis upotrijebi [odgovarajući izraz](u13_gubici_cjevovodi_crpke_i_mreze.qmd#eq-npsha-spremnik).

**Kontrolni rezultat ili kriterij.** Prigušeno: $q=19{,}12\ \mathrm{L/s}$, $H=19{,}62\ \mathrm{m}$ i $P_{el}=5{,}11\ \mathrm{kW}$. Regulacija brzinom: otvoren sustav traži $H=14{,}13\ \mathrm{m}$, $s=0{,}878$, $P_{el}=3{,}68\ \mathrm{kW}$ i idealizirana godišnja ušteda je $7{,}14\ \mathrm{MWh}$. Za usis su $NPSH_a=6{,}65\ \mathrm{m}$, $NPSH_r=3{,}10\ \mathrm{m}$ i numerička razlika $3{,}55\ \mathrm{m}$. Prihvatljivost ipak zahtijeva proizvođačev kriterij margine, dopušteno radno područje i stvarne temperaturne/atmosferske uvjete.

## Turbostrojevi i propulzija

### Zadatak 1 · T1 {#key-task-u12-vodeni-mlaz-brzine-izlazi-iz-kruzne-sapnice}

[Vrati se na zadatak](u14_turbostrojevi_i_propulzija.qmd#task-u12-vodeni-mlaz-brzine-izlazi-iz-kruzne-sapnice)

**Sažetak.** Vodeni mlaz brzine $v = 24\ \text{m/s}$ izlazi iz kružne sapnice promjera $d = 22\ \text{mm}$ i udara okomito na nepomičnu ravnu ploču. Odredi silu na ploču.

**Naputak.** $\dot m = \rho Av$, a za potpuno kočenje komponente brzine na ploči vrijedi $F = \dot m v$.

**Kontrolni rezultat ili kriterij.** $\dot m \approx 9{,}1\ \text{kg/s}$; $F \approx 219\ \text{N}$.

### Zadatak 2 · T1 {#key-task-u12-vodeni-mlaz-brzine-izlazi-iz-pravokutne-sapnice}

[Vrati se na zadatak](u14_turbostrojevi_i_propulzija.qmd#task-u12-vodeni-mlaz-brzine-izlazi-iz-pravokutne-sapnice)

**Sažetak.** Vodeni mlaz brzine $v = 26\ \text{m/s}$ izlazi iz pravokutne sapnice širine $b = 30\ \text{mm}$ i visine $h = 16\ \text{mm}$ te udara u nepomičnu vodilicu koja tok zakreće za $110^\circ$ bez promjene iznosa brzine. Odredi komponente sile…

**Naputak.** iz presjeka dobij $\dot m$, a zatim razliku ulazne i izlazne komponente brzine u x i y smjeru.

**Kontrolni rezultat ili kriterij.** $\dot m \approx 12{,}5\ \text{kg/s}$; $F_x \approx 435\ \text{N}$, $F_y \approx -304\ \text{N}$; reakcija nosača $\approx 531\ \text{N}$.

### Zadatak 3 · T2 {#key-task-u12-na-pokretnu-lopaticu-dolazi-mlaz-vode-apsolutnom}

[Vrati se na zadatak](u14_turbostrojevi_i_propulzija.qmd#task-u12-na-pokretnu-lopaticu-dolazi-mlaz-vode-apsolutnom)

**Sažetak.** Na pokretnu lopaticu dolazi mlaz vode apsolutnom brzinom $v_1 = 32\ \text{m/s}$, dok se lopatica giba brzinom $u = 12\ \text{m/s}$ u smjeru mlaza. Pretpostavi da je relativna izlazna brzina po iznosu jednaka ulaznoj i zakrenuta za…

**Naputak.** prijeđi na relativne brzine, zatim vrati apsolutnu izlaznu brzinu i iz tangencijalne promjene količine gibanja dobij silu; snaga je $P = Fu$.

**Kontrolni rezultat ili kriterij.** $w_1 = 20\ \text{m/s}$; $F_t \approx 672\ \text{N}$; $P \approx 8{,}06\ \text{kW}$.

### Zadatak 4 · T2 {#key-task-u12-peltonova-lopatica-na-rotoru-radijusa-prima-mlaz}

[Vrati se na zadatak](u14_turbostrojevi_i_propulzija.qmd#task-u12-peltonova-lopatica-na-rotoru-radijusa-prima-mlaz)

**Sažetak.** Peltonova lopatica na rotoru radijusa $R = 0{,}42\ \text{m}$ prima mlaz vode masenog protoka $\dot m = 24\ \text{kg/s}$. Tangencijalna komponenta apsolutne brzine na ulazu iznosi $v_{u1} = 28\ \text{m/s}$, a na izlazu $v_{u2} = 6\…

**Naputak.** tangencijalna sila slijedi iz $F_t = \dot m (v_{u1} - v_{u2})$, a moment je $M = F_t R$.

**Kontrolni rezultat ili kriterij.** $F_t = 528\ \text{N}$; $M \approx 222\ \text{N·m}$.

### Zadatak 5 · T3 {#key-task-u12-potisni-modul-ima-tri-jednake-sapnice-promjera}

[Vrati se na zadatak](u14_turbostrojevi_i_propulzija.qmd#task-u12-potisni-modul-ima-tri-jednake-sapnice-promjera)

**Sažetak.** Potisni modul ima tri jednake sapnice promjera $d = 30\ \text{mm}$. Iz svake sapnice voda izlazi brzinom $v = 42\ \text{m/s}$ u suprotnom smjeru od gibanja platforme. Odredi ukupni potisak modula i hidrauličku snagu mlaza ako je gustoća…

**Naputak.** za jednu sapnicu vrijedi $F = \dot m v$ i $P = \dot m v^2/2$; ukupni rezultat je trostruki zbroj.

**Kontrolni rezultat ili kriterij.** ukupni potisak $\approx 3{,}73\ \text{kN}$; hidraulička snaga $\approx 78{,}4\ \text{kW}$.

### Zadatak 6 · T4 {#key-task-u12-mlazna-platforma-ukupne-mase-ima-cetiri-jednake}

[Vrati se na zadatak](u14_turbostrojevi_i_propulzija.qmd#task-u12-mlazna-platforma-ukupne-mase-ima-cetiri-jednake)

**Sažetak.** Mlazna platforma ukupne mase $m = 110\ \text{kg}$ ima četiri jednake sapnice promjera $d = 28\ \text{mm}$. Voda gustoće $\rho=998\ \text{kg/m}^3$ iz svake sapnice izlazi okomito prema dolje brzinom $v = 36\ \text{m/s}$. Odredi ukupni…

**Naputak.** najprije zbroji izlazne površine svih sapnica; zatim koristi $F_p = \rho A v^2$, uvjet lebdenja $F_p = mg$ i za zadanu masu Newtonov zakon $a = (F_p - mg)/m$. Za masu prema zadanom kriteriju izračunaj najmanji potisak s $d_{min}$ i $v_{min}$ te postavi $F_{p,min}=1{,}10\,m_{krit}g$.

**Kontrolni rezultat ili kriterij.** $F_p \approx 3{,}19\ \text{kN}$; najveća masa lebdenja $\approx 325\ \text{kg}$; pri $m = 110\ \text{kg}$ ubrzanje $a \approx 19{,}2\ \text{m/s}^2$. Za $d_{min}=27{,}7\ \text{mm}$ i $v_{min}=34{,}5\ \text{m/s}$ najmanji je potisak približno $2{,}86\ \text{kN}$, pa zadani kriterij daje $m_{krit}\approx265\ \text{kg}$. To je rezultat idealiziranoga statičkog modela, ne certificirana nosivost; nedostaju dinamika, stabilnost, konstrukcija, upravljanje i mjerodavni propisi.

## Otvoreni tokovi

### Zadatak 1 · T1 {#key-task-otvoreni-fr}

[Vrati se na zadatak](u15_otvoreni_tokovi.qmd#task-otvoreni-fr)

**Sažetak.** Pravokutni kanal $b=1{,}5\ \text{m}$ vodi $Q=1{,}2\ \text{m}^3/\text{s}$ pri $y=0{,}60\ \text{m}$. Odredi $v$, $Fr$ i smjer mogućeg širenja poremećaja.

**Kontrolni rezultat ili kriterij.** $v=1{,}33\ \text{m/s}$, $Fr=0{,}55$.

### Zadatak 2 · T1 {#key-task-kriticna-dubina}

[Vrati se na zadatak](u15_otvoreni_tokovi.qmd#task-kriticna-dubina)

**Sažetak.** Za $q=3{,}0\ \text{m}^2/\text{s}$ odredi $y_c$ i $E_{min}$.

**Kontrolni rezultat ili kriterij.** $y_c\approx0{,}972\ \text{m}$, $E_{min}\approx1{,}46\ \text{m}$.

### Zadatak 3 · T2 {#key-task-trapezni-presjek}

[Vrati se na zadatak](u15_otvoreni_tokovi.qmd#task-trapezni-presjek)

**Sažetak.** Simetrični trapezni kanal ima širinu dna $b=2{,}40\ \text{m}$, pokos $z=1{,}50$ vodoravno na jedan okomito, dubinu $y=0{,}900\ \text{m}$ i protok $Q=3{,}60\ \text{m}^3/\text{s}$. Izračunaj $A$, $T$, $P$, $D_h$, $R_h$, srednju brzinu i…

**Naputak.** Za pokos $z{:}1$ vrijedi $A=y(b+zy)$, $T=b+2zy$ i $P=b+2y\sqrt{1+z^2}$. U izrazu za $Fr$ upotrijebi $D_h=A/T$, a ne $R_h$.

**Kontrolni rezultat ili kriterij.** $A=3{,}375\ \text{m}^2$, $T=5{,}100\ \text{m}$, $P=5{,}645\ \text{m}$, $D_h=0{,}6618\ \text{m}$, $R_h=0{,}5979\ \text{m}$, $v=1{,}0667\ \text{m/s}$ i $Fr=0{,}4186$ (mirni tok).

### Zadatak 4 · T2 {#key-task-alternativne-dubine}

[Vrati se na zadatak](u15_otvoreni_tokovi.qmd#task-alternativne-dubine)

**Sažetak.** U pravokutnom kanalu protok po jedinici širine iznosi $q=2{,}20\ \text{m}^2/\text{s}$, a specifična energija $E=1{,}600\ \text{m}$. Bez uporabe gotove formule za korijene najprije provjeri $E>E_{min}$, zatim numerički odredi obje…

**Naputak.** Kritična dubina razdvaja intervale traženja korijena funkcije $f(y)=y+q^2/(2gy^2)-E$. Jedan korijen traži u $0<y<y_c$, a drugi u $y>y_c$; zapiši i kriterij zaustavljanja numeričkog postupka.

**Kontrolni rezultat ili kriterij.** $y_c=0{,}7902\ \text{m}$ i $E_{min}=1{,}1853\ \text{m}$. Plića je grana $y_s=0{,}4665\ \text{m}$, $Fr_s=2{,}204$; dublja je $y_d=1{,}4887\ \text{m}$, $Fr_d=0{,}3867$.

### Zadatak 5 · T3 {#key-task-skok-mjerenje}

[Vrati se na zadatak](u15_otvoreni_tokovi.qmd#task-skok-mjerenje)

**Sažetak.** Na vodoravnom pravokutnom pokusnom kanalu izmjereni su $Q=1{,}800\pm0{,}018\ \text{m}^3/\text{s}$, $b=1{,}200\pm0{,}003\ \text{m}$, $y_1=0{,}250\pm0{,}003\ \text{m}$ i $y_2=1{,}220\pm0{,}008\ \text{m}$; navedene su neovisne standardne…

**Naputak.** Najprije propagiraj $q=Q/b$. Za $M(y,q)=y^2/2+q^2/(gy)$ izračunaj parcijalne derivacije reziduala prema $y_1$, $y_2$ i $q$, a zatim primijeni korijen iz zbroja kvadrata. Hidrostatičke sile na krajnjim presjecima djeluju u suprotnim smjerovima; težina nema uzdužnu komponentu.

**Kontrolni rezultat ili kriterij.** $q=1{,}5000\ \text{m}^2/\text{s}$ i $u_q=0{,}01546\ \text{m}^2/\text{s}$. Dobiva se $R=-0{,}01648\ \text{m}^2$, $u_R=0{,}02010\ \text{m}^2$ i $|R|/u_R=0{,}820<2$, pa se u granicama zadanoga modela bilanca zatvara. Iz srednjih ulaza teorijska je spregnuta dubina $1{,}2353\ \text{m}$.

### Zadatak 6 · T4 {#key-task-klimatski-kanal}

[Vrati se na zadatak](u15_otvoreni_tokovi.qmd#task-klimatski-kanal)

**Sažetak.** Trapezni oborinski kanal ima $b=3{,}00\ \text{m}$, pokos $z=2{,}00$, nagib $S_f=0{,}00150$ i konstrukcijsku dubinu $H=1{,}50\ \text{m}$; traže se projektni protok $Q_d=8{,}00\ \text{m}^3/\text{s}$ i slobodni rub najmanje $f_{min}=0{,}300\…

**Naputak.** Za svaki $n$ najprije računaj kapacitet na dopuštenoj dubini $1{,}20\ \text{m}$, a normalnu dubinu pri $Q_d$ pronađi kao korijen Manningove jednadžbe. Odvojeno provjeri srednju procjenu i konzervativni $n_c$. U bazenu je $q=Q/B$; ista vrijednost $Q_d$ daje isti skok neovisno o stanju uzvodnog održavanja, ali kapaciteti daju različitu izvanprojektnu ovojnicu.

**Kontrolni rezultat ili kriterij.** Za A/B/C kapaciteti pri $y=1{,}20\ \text{m}$ iznose $11{,}759/8{,}141/6{,}047\ \text{m}^3/\text{s}$, a normalne dubine pri $Q_d$ $0{,}985/1{,}189/1{,}380\ \text{m}$, odnosno slobodni rubovi $0{,}515/0{,}311/0{,}120\ \text{m}$. S $n_c$ kapaciteti padaju na $10{,}583/7{,}055/4{,}922\ \text{m}^3/\text{s}$, pa samo A robusno zadovoljava oba zahtjeva. Pri $Q_d$ je $y_2=1{,}059\ \text{m}$; pri kapacitetima A/B/C dobiva se $y_2=1{,}628/1{,}080/0{,}765\ \text{m}$, pa bazen ne pokriva cijelu…

::: {.mf1-mini-summary}
<p class="mf1-box-label">Opseg ključa</p>

Ključ obuhvaća 90 zadataka iz javnog toka U01–U15. Pogrešku u rezultatu prijavite prema stabilnom ID-ju zadatka kroz errata obrazac.
:::
