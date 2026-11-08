# Stručna recenzija: pog. 13 „Gubitci, cjevovodi, crpke i mreže”

Recenzent: neovisni agent (stručna uputa `struka.md`), 8. 11. 2026.
Materijal: PDF poglavlja (str. 245–262), PDF ključa (dodatak F, str. 350–351),
izvor `source/u13_gubici_cjevovodi_crpke_i_mreze.md` (dalje: `u13:redak`).
Nisam čitao `tools/`, `docs/radno/` (osim ove datoteke), završnu recenziju,
CHANGELOG ni git povijest. Sve brojeve riješenih primjera i kontrolnih rezultata
ponovno sam izračunao u Pythonu (skripte u radnoj mapi izvan repozitorija);
ponovni račun je u odjeljku „Brojčana provjera”.

## Sažetak

Fizika poglavlja je točna, a svi brojevi u P1–P6, Z1–Z6 i ključu podudaraju se s
mojim ponovnim računom unutar zaokruživanja. Najveća slabost je didaktička:
nijedan riješeni primjer ne pokazuje središnji korak poglavlja, izračun
turbulentnog $\lambda$ iz $Re$ i $k_s/D$, koji samostalni zadatci Z4 i Z5 traže.
Uz to, oznake razina Z2 i Z4 niže su od stvarne odluke, a nekoliko skica i
uputnica treba doraditi.

## Nalazi po težini

### P0

Nema nalaza. Nisam našao pogrešan predznak, pogrešan broj ni opasan zaključak.

### P1

**P1-1. Nijedan riješeni primjer ne računa turbulentni $\lambda(Re,k_s/D)$, a Z4 i Z5 to traže.**
Mjesto: `u13:375–672` (P1–P6, str. 253–257); Z4 `u13:801–832`
(`task-radna-tocka-hrapavog-voda`), Z5 `u13:834–858`
(`task-robustan-izbor-promjera`); slijed `eq-cjevovodi-3-od-reynoldsova-broja-do-koeficijenta-trenja-01`
(13.9); ishod 1 u `u13:909`.
Opis: P1 zadaje $\lambda=0{,}028$, P3 zadaje $\lambda=0{,}022$, P6 zadaje
$\lambda=0{,}030$, a P2 je laminaran ($64/Re$). Colebrookova jednadžba (13.14),
iteracija (13.15) i Swamee–Jainova formula (13.16) izvedeni su samo u
okviru izvoda. U poglavljima 1–15 nema drugog mjesta gdje se računa
Colebrook ili Swamee–Jain (pretraživanje `source/`: pojavljuju se samo u pog. 13 i
dodatcima). Student prvi put računa $\lambda$ za turbulentni tok u samostalnom
Z4, i to iterativno i spregnuto s krivuljom crpke, a zatim u Z5. Time slijed
$Q\to v\to Re\to\lambda\to h_g$, koji poglavlje proglašava „ispravnim slijedom” i
navodi kao prvi ishod, nema riješeni primjer s neovisnom provjerom.
Prijedlog: jedan od primjera s zadanim $\lambda$ preoblikovati tako da $\lambda$
proizlazi iz $Re$ i $k_s/D$. Najmanji zahvat je P1: zadati $k_s$ i $\nu$ umjesto
$\lambda$. Swamee–Jainom izračunati $\lambda$, zatim provjeriti Colebrookovim rezidualom
ili očitanjem iz Moodyjeva dijagrama. Druga mogućnost je P6, gdje bi usisni
$\lambda$ iz hrapavosti dao i povezanu odluku o NPSH-u. Broj primjera ostaje isti.

### P2

**P2-1. Razine Z2 i Z4 niže su od stvarne odluke; nedosljedno s P2.**
Mjesto: Z2 `u13:747–771` (`task-dva-fluida-isti-vod`, T1, str. 259);
Z4 `u13:803–832` (T2, str. 260); P2 `u13:418–466` (`ex-laminarni-rashladni-vod`, T2).
Opis: P2 obuhvaća samo laminarni vod i označen je T2. Z2 sadrži cijeli P2
(fluid A) i još odluku o režimu, izbor između $64/Re$ i Blasiusa te skaliranje
pri $2Q$. Prema definiciji iz upute (T1 jedan zakon, T3 izbor modela) Z2 je
barem T2, a izbor korelacije prema režimu jest izbor modela. Z4 spreže
Colebrookovu jednadžbu, Darcy–Weisbacha i krivulju crpke u iterativnom
rješenju, a to je spajanje modela (T3). Z5 (T3) pak računa eksplicitnom
korelacijom bez sprege s crpkom. Po zahtjevnosti odluke Z5 nije iznad Z4.
Prijedlog: ne podizati oznake radi kvote nego prilagoditi zadatke. Primjerice,
u Z2 dati oba fluida u laminarnom režimu ili zadati režim, pa zadatak ostaje T1.
Ili zamijeniti mjesta T2/T3 (Z4 T3, Z5 T2, ako se u Z5 izbor svede na geometrijsku
odluku). Autorica odlučuje o rasporedu 2×T1, 2×T2, T3, T4.

**P2-2. „Najčešća pogreška” i izravni problem mreže nisu uvježbani.**
Mjesto: `u13:905` (Najčešća pogreška), `u13:89`, `u13:97`, `u13:910` (ishod 2),
slika `fig-cjevovodna-mreza-pregled` (str. 245).
Opis: poglavlje kao najčešću pogrešku navodi zbrajanje $\xi$ s različitim
referentnim brzinama. Ni u jednom P ni Z nema dionica različitih promjera ni
elementa s dvjema brzinama, pa se pogreška nigdje ne može pogriješiti ni ispraviti.
Ni izravni problem paralelnih grana nije uvježban (zadan $Q$ i $R_i$, traže se
$Q_i$; to radi samo bilježnica). Z3 je obrnut, projektni problem s ciljem
$Q_1=Q_2$. Serijsko-paralelna mreža sa slike 13.1 ostaje neizračunata.
Prijedlog: u postojećem primjeru ili zadatku (npr. Z1 ili P1) uvesti drugi
promjer ili nagli prijelaz, tako da student mora razdvojiti dvije brzinske
visine. Alternativno, u Z3 dodati prvi korak: raspodjelu protoka prije
ugradnje ventila. Iz nje se vidi i omjer $Q_1/Q_2=\sqrt{R_2/R_1}=2$.

**P2-3. P5: visina dobave pada uz isti protok bez navedenog mehanizma.**
Mjesto: `u13:589` (`ex-energijski-ledger-hladenja`, str. 256); usporedi `u13:278`.
Opis: „Nakon čišćenja izmjenjivača visina dobave pada na $H_p=10\ \mathrm{m}$,
uz isti protok”. Uz nepromijenjenu brzinu vrtnje smanjenje otpora pomiče radnu
točku prema većem $Q$. Upravo to poglavlje samo kaže u `u13:278`: „pri
nepromijenjenoj brzini crpke mijenja se i radni protok”. Primjer pretpostavlja da
frekvencijski pretvarač snizuje brzinu vrtnje kako bi $Q$ ostao 6,0 L/s, ali to ne
piše. Račun je točan uz izrečenu pretpostavku, no student dobiva proturječnu sliku.
Prijedlog: jedna rečenica u tekstu zadatka: „Pretvarač snizuje brzinu vrtnje
tako da protok ostane 6,0 L/s; učinkovitosti pretpostavljamo nepromijenjenima.”

**P2-4. Slika 13.2: ventil izvan cijevi, oznaka presjeka 2 na krivom mjestu, radna oznaka.**
Mjesto: `u13:65` (`fig-energijska-crta-gubitci`), str. 247, lijevi panel.
Opis: simbol ventila nacrtan je iznad cijevi, bez spoja s njom. Stepenica EGL/HGL
je pod njim, ali ventil nije u vodu. Oznaka „2” stoji ispod sredine cijevi, a ne
na izlaznom presjeku na kojem EGL završava i gdje vrijedi $p_{M,2}=0$. Oznaka
„ventil (simbol)” je napomena izrade (K13) i stoji odvojeno od ventila.
Prijedlog: ventil smjestiti u os cijevi s otvorenim prolazom, „2” postaviti na
izlazni presjek i ukloniti „(simbol)”. Stil slike ne mijenjati.

**P2-5. „Redukcijski ventil” kao primjer elementa s različitim brzinama.**
Mjesto: `u13:89`, str. 248.
Opis: „Pri naglom proširenju, redukcijskom ventilu ili grananju brzine s dviju
strana elementa nisu jednake”. Redukcijski ventil u hrvatskom tehničkom nazivlju
obično znači ventil za sniženje tlaka. Njegovi su priključci najčešće jednakog
promjera, pa brzine s dviju strana nisu nužno različite. Vjerojatno se misli na
redukciju (suženje) promjera. Nisam potpuno siguran u namjeru autorice.
Prijedlog: „Pri naglom proširenju, suženju (redukciji) ili grananju …”.

**P2-6. Empirijske relacije bez izvora i bez punog područja valjanosti (K14, K9).**
Mjesto: Swamee–Jain `u13:185–190`, Blasius `u13:192`, Hardy–Cross `u13:244–250`;
str. 249–251. Dodatak E/literatura (`source/d05_literatura.md:13`) navodi samo
Moodyja i Colebrooka.
Opis: tvrdnja „od Colebrookove odstupa za oko 1 %” i pragovi Blasiusa nemaju
izvor. Za Swamee–Jainovu formulu navedeno je samo područje $Re$, a izostavljeno je
područje relativne hrapavosti (u izvornom radu približno
$10^{-6}<k_s/D<10^{-2}$; granice navodim po sjećanju i treba ih provjeriti u
izvoru). Moj račun potvrđuje red veličine tvrdnje o točnosti: u Z5 Swamee–Jain
odstupa od Colebrooka 0,6–0,8 %, u Z4 0,7 %.
Prijedlog: dodati izvore (Swamee i Jain 1976., Blasius 1913., Cross 1936., ili
udžbenik iz dodatka E koji ih navodi) i područje $k_s/D$.

**P2-7. Ključ u PDF-u: uputnica na jednadžbu prikazana kao „odgovarajući izraz”.**
Mjesto: dodatak F, str. 350 (Z5) i 351 (Z6); izvor naputka `u13:848` i `u13:879`.
Opis: u tiskanom ključu piše „pa $\lambda$ iz jednadžbe odgovarajući izraz” i
„usisna bilanca prema jednadžbi odgovarajući izraz”. Uputnice
`[-@eq-swamee-jain]` i `[-@eq-npsha-spremnik]` nisu razriješene u broj
(13.16 i 13.28). U tisku student ne zna na koju se jednadžbu upućuje (K12).
Prijedlog: razriješiti uputnice u generiranom ključu kao brojeve jednadžbi.
Usput: ključ ovog poglavlja ima naslov „F.14”, a sljedeći „F.15 Turbostrojevi”.
Ne znam je li pomak broja za jedan namjeran (npr. ako je F.1 uvod); treba provjeriti.

**P2-8. Provjera u P1 nije neovisna i daje drugi broj.**
Mjesto: `u13:415` (`ex-gubitci-jedne-dionice`), str. 254.
Opis: „$\Delta p/(\rho g)=37\,400/(1000\cdot9{,}81)=3{,}81\ \mathrm{m}$ vraća ukupni
gubitak” samo obrće posljednji korak, pa ne provjerava ništa. Zbog zaokruživanja
$\Delta p$ na 37,4 kPa daje 3,81 m umjesto 3,82 m u (13.31). Nezaokruženo
$\Delta p=37\,440\ \mathrm{Pa}$ daje 3,817 m. Pažljiv student vidi da „vraća” nije istina.
Prijedlog: neovisna provjera, npr. udio lokalnih gubitaka
$\sum\xi/(\lambda L/D+\sum\xi)=4{,}6/13{,}0=0{,}354$ prema $1{,}35/3{,}82$, ili
ocjena reda veličine gradijenta $h_l/L=6{,}9\ \mathrm{m}/100\ \mathrm{m}$.

**P2-9. Naputak Z2 rješava drugi dio zadatka (K15).**
Mjesto: `u13:761`.
Opis: „Udvostručenje $Q$ u laminarnom toku udvostručuje $\Delta p$, a u Blasiusovu
području množi ga s $2^{1{,}75}$” izravno je odgovor na „Traži se 2”.
Prijedlog: „Izrazi $\Delta p$ kao potenciju od $Q$ za svaki zapis $\lambda$.”

**P2-10. Nejasna upućivanja (K12).**
Mjesto i opis:
- `u13:115` (str. 248): „kao u ranijem Venturijevu primjeru”. Nema broja
  poglavlja ni primjera. Venturi se obrađuje u pog. 8, 11 i dodatku D.
- `u13:265` (str. 251): „nastavci zasebno obrađuju Z3 i Z6”. Ne kaže se što su
  „nastavci” (dijelovi bilježnice?). Z6 nema paralelnih grana, pa veza nije jasna.
- `u13:276` (str. 251): „ne zadržavamo automatski dotok iz pog. 7”. Čitatelj ne
  zna koji dotok ni koji primjer pog. 7.
- `u13:370`: „koji obrađuje sljedeće poglavlje” → „pog. 14”.
Prijedlog: navesti poglavlje i primjer ili rečenicu skratiti tako da ne upućuje.

**P2-11. Jedno slovo za tri veličine: $s$ (K6).**
Mjesto: Z6 `u13:866–874`, P4 `u13:566`, NPSH `u13:339–355`.
Opis: $s=n_2/n_1$ je omjer brzina vrtnje. Indeks $s$ znači sustav ($H_s$,
$H_{s,V}$), ali i usis ($z_s$, $v_s$, $h_{g,s}$, presjek S). U Z6 se sve tri
pojavljuju u istom zadatku: „$s=n_2/n_1$, potrebnu visinu $H_s$” uz $z_s$ i
$h_{g,s}$.
Prijedlog: za usis uzeti indeks $u$ ili $us$, ili za omjer brzina $\kappa=n_2/n_1$,
i zapisati izbor u dodatku A.

### P3

**P3-1. P3: „lijevano željezo” i $\lambda=0{,}022$.** `u13:473`, `u13:525`.
Uz uobičajenu ekvivalentnu hrapavost lijevanog željeza $k_s\approx0{,}26\ \mathrm{mm}$
(Moodyjeva tablica; vrijednost navodim po sjećanju) Colebrook pri stvarnim $Re$
daje $\lambda_{AB}=0{,}0238$, $\lambda_{BC}=0{,}0268$, $\lambda_{CD}=0{,}0254$ i
$\lambda_{DA}=0{,}0236$. To je 7–22 % više od 0,022. Tekst to ograđuje („jest
pojednostavnjenje”), ali materijal i broj ne odgovaraju jedno drugom.
Prijedlog: napisati „obložene cijevi” ili ne navoditi materijal. Druga mogućnost
je zadati $k_s$, pa se povezuje i s P1-1.
Usput: `u13:486` traži „razliku piezometarskih visina”, a petlja se zatvara po
gubitcima energije. Treba reći da se razlike brzinskih visina zanemaruju
(najviše $1{,}19^2/19{,}62=0{,}07\ \mathrm{m}$ prema 4,72 m).

**P3-2. Ponavljanje riješenih primjera u zadatcima.**
Z1 (`u13:720`) je obrnuti P1: isti zapis, traži se $v$ umjesto $h_g$. Fluid A u Z2
jest P2 s drugim brojevima. Z6, 1. i 2. dio, ponavlja postupak P4 (presjecište
pa $s$ iz $25s^2-\dots$) i P5. Novi sadržaj Z6 su NPSH i odluka. Za T1 i T4 to je
prihvatljivo, ali ostavlja malo novih odluka (vidi P2-2).

**P3-3. Kriterij $NPSH_r$.** `u13:357`. Dobro je što tekst ne propisuje marginu.
Studentu bi pomoglo jednom navesti uobičajeni ispitni kriterij: $NPSH_r$ se
određuje kao NPSH pri kojem visina dobave padne za 3 % (NPSH3, norme za
prihvatna ispitivanja crpki, npr. ISO 9906). Tako bi bilo jasno zašto pri
$NPSH_a=NPSH_r$ kavitacija već postoji. Izvor treba provjeriti i navesti u dodatku E.

**P3-4. Što nedostaje za nastavak studija.** Crpke u paralelnom i serijskom
spoju (zbrajanje karakteristika) ne obrađuju se ni u pog. 13 ni u pog. 14 (pretraživanje
izvora). To je izravno potrebno za brodske balastne, protupožarne i rashladne
sustave s pričuvnom crpkom. Hidraulički promjer uveden je u pog. 11
(`u11:764`), ali pog. 13 ne kaže da se Darcy–Weisbach i $\lambda(Re,k_s/D_h)$ za
nekružne kanale (ventilacija strojarnice) računaju s $D_h$. Kratka napomena ili
zadatak iz banke alternativa riješio bi oba.

**P3-5. Prva granica modela ne navodi zabranjeni zaključak (K11).** `u13:69–73`.
Blok nabraja što traži proširen model, ali ne kaže što se ne smije zaključiti.
Primjer zaključka koji fali: „vršni tlak pri brzom zatvaranju ventila ne smije se
procjenjivati iz (13.1)”.

**P3-6. CFD provjera s „inače” isključuje druge uzroke (K9).** `u13:162`.
„…mora vratiti $64/Re$, inače tok u domeni nije razvijen ili mreža nije dovoljno
fina”. Uzrok mogu biti i rubni uvjeti, svojstva fluida ili definicija srednje
brzine. Prijedlog: „…inače treba provjeriti razvijenost toka, mrežu i rubne uvjete”.

**P3-7. P5 i Z6: ista učinkovitost sa pretvaračem i bez njega.** `u13:866`.
Pretpostavka je izrečena. Ipak, regulacija prigušivanjem nema gubitke pretvarača,
a regulacija brzinom ih ima (u P5 $\eta_f=0{,}97$), pa jednaki $\eta$ blago ide u
prilog regulaciji brzinom. Moglo bi se navesti u ključu kao dio „koji podatci
nedostaju”.

**P3-8. P6: podatci uz usis.** `u13:635`. Temperatura uz $p_v=2{,}34\ \mathrm{kPa}$
(≈ 20 °C) nije navedena, a granica modela (`u13:362`) traži da tlak pare odgovara
temperaturi. Brzina u usisu 2,79 m/s velika je za usisni vod. Smatram da se u
praksi teži nižim brzinama na usisu, ali za to ne navodim izvor. Prijedlog:
dopisati temperaturu i, po želji, komentar u „Provjeri i tumačenju”.

**P3-9. Skice zadataka: naslovi panela ≠ naslovi zadataka.**
`u13:712`, str. 258. Z2 „Isti vod, dva fluida” prema „… i dva režima”, Z3
„Uravnoteženje dvaju ogranaka” prema „… paralelnih grana”, Z4 „Radna točka uz
promjenjivo trenje” prema „Radna točka hrapavog voda”. Oznake u panelu Z2 složene
su serifnim slogom, a u ostalim panelima bezserifnim. Prijedlog: uskladiti naslove i font.

**P3-10. Tipografija i oznake.** U (13.19) i P3 $|Q_i|$ se u PDF-u slaže s
razmacima („$Q_i\ |\ Q_i\ |$”, str. 251, 255); bolje je `\lvert Q_i\rvert`.
$\xi$ i $\zeta$ (`u13:97`) rukom se lako zamijene. Rezultati Z4 u ključu imaju 5–6
značajnih znamenki ($\lambda\approx0{,}020812$). To je opravdano provjerom reziduala,
ali to odstupa od K8 i treba ga jednom reći.

**P3-11. Interna oznaka u tiskanoj poveznici (K1).** `u13:205`, str. 250.
Tiskani URL glasi `…?path=u10_moody_dijagram.ipynb`. Oznaka „u10” ne odgovara
ni ovom poglavlju ni pog. 10 (Količina gibanja). Prijedlog: preimenovati
bilježnicu (npr. `u13_moody_dijagram`) ili prihvatiti kao tehnički naziv.
Nisam provjerio sadrži li bilježnica radnu točku iz Z4 na koju upućuje
`u13:200`.

## Brojčana provjera (moj račun, $g=9{,}81\ \mathrm{m/s^2}$)

| Mjesto | U knjizi | Moj račun | Ocjena |
|---|---|---|---|
| P1 | $v^2/2g=0{,}294$; $h_l=2{,}47$; $h_{loc}=1{,}35$; $h_g=3{,}82$ m; $\Delta p=37{,}4$ kPa | 0,2936; 2,466; 1,350; 3,817; 37,44 | točno (provjera 3,81, vidi P2-8) |
| P2 | $v=0{,}637$; $Re=509$; $\lambda=0{,}1257$; $h_l=1{,}298$ m; $\Delta p=13{,}37$ kPa (oba zapisa) | 0,6366; 509,3; 0,12566; 1,2979; 13,369 / 13,369 | točno |
| P3 | $R=7181/45\,445/11\,913/8378$; it. 1: 4,877 m, 1669, $\Delta Q=-2{,}92$; it. 2: 0,276, 1481, $-0{,}19$; $Q=18{,}89/6{,}89/-9{,}11/-21{,}11$; $h=2{,}56/2{,}16/0{,}99/3{,}73$; rezidual 1,1 mm; A–C 4,72 m; $v=0{,}74$–$1{,}19$; $Re=0{,}9$–$1{,}8\cdot10^5$ | 7181,4/45 444,8/11 913,1/8378,3; 4,8768, 1669,5, −2,921; 0,2759, 1480,5, −0,186; 18,892/6,892/−9,108/−21,108; 2,563/2,159/0,988/3,733; 1,12 mm; 4,722 i 4,721; 0,742–1,194; 0,88–1,79·10⁵ | točno |
| P4 | $Q_{op}=19{,}94$; $H_{op}=18{,}04$; $H_s(Q_2)=15{,}01$; $s=0{,}899$; 0,865 | 19,937; 18,044; 15,006; 0,8990; 0,8647 | točno |
| P5 | $P_h=0{,}706$; $P_{vr}=0{,}906$; $P_{el}=1{,}015$ kW; 7,10 / 5,92 / 1,18 MWh/god; 0,696 | 0,7063; 0,9055; 1,0147; 7,103 / 5,919 / 1,184; 0,6961 | točno |
| P6 | $v_s=2{,}785$; $h_{g,s}=1{,}453$; $p/\rho g=5{,}847$ m; $p=57{,}36$ kPa; $NPSH_a=6{,}00$ | 2,7852; 1,4530; 5,8472; 57,361; 6,004 | točno |
| Z1 | $h_g=2{,}554$; $\zeta=16{,}5$; $v=1{,}743$; $Q=13{,}69$ L/s; 75,8 % | 2,5535; 16,5; 1,7425; 13,686; 75,76 % | točno |
| Z2 | $v=0{,}597$; A: 796, 0,0804, 7,73 kPa; B: 4775, 0,0381, 3,38 kPa; $2Q$: 15,5 i 11,4 kPa | 0,5968; 795,8, 0,08042, 7,735; 4774,6, 0,03806, 3,383; 15,47 i 11,38 | točno |
| Z3 | $R_v=36\,000$; $Q_i=10{,}00$ L/s; $h_{AB}=4{,}80$; $h_{g,V}=3{,}60$ m | isto | točno |
| Z4 | $Q=19{,}030$ L/s; $H=19{,}136$ m; $Re=2{,}423\cdot10^5$; $\lambda=0{,}020812$; 3,572/4,700/5,109 kW | 19,0296; 19,1362; 2,4229·10⁵; 0,020812; 3,5724/4,7005/5,1092 (bisekcija + Colebrook, oba reziduala < 10⁻¹⁰) | točno |
| Z5 | $\lambda=0{,}0238/0{,}0228/0{,}0221$; $h_g=33{,}1/10{,}8/3{,}56$ m; 100 mm; staro: 0,0309, 14,0 m | SJ: 0,02383/0,02284/0,02205; 33,13/10,78/3,56; staro 0,03094, 14,03 (Colebrook: 0,03079, 13,97) | točno |
| Z6 | $Q=22{,}36$; $(17{,}00;11{,}50)$; $s=0{,}866$; $(8{,}19;5{,}54;2{,}65)$ MWh; $(10{,}06;4{,}50;5{,}56)$; balast 8,66 m | 22,361; 17,000 i 11,500; 0,8660; 8,191, 5,541, 2,650; 10,057, 4,500, 5,557; 8,657 | točno |

Dimenzije: $R=8\lambda L/(\pi^2gD^5)$ u $\mathrm{s^2/m^5}$, (13.17) i
$1/\sqrt{R_{eq}}=\sum1/\sqrt{R_i}$ izveo sam ponovno i točni su. Izvod
$\tau_{st}=D\Delta p/(4L)$, $\lambda=8\tau_{st}/(\rho v^2)$, $\tau_{st}=8\mu v/D$,
$64/Re$ i (13.13) je korak po korak ispravan. Isto vrijedi za Hardy–Crossovu
linearizaciju (13.19), skaliranje $H_{p,2}(Q)=s^2H_p(Q/s)$ i oba zapisa
$NPSH_a$ (13.27, 13.28). Skica Z4 (str. 258) odgovara zadanoj krivulji:
$H_p(5)=29{,}25$, $H_p(20)=18$ i $H_p(30)=3$ m. Kota $z_s=-1{,}8$ m u skici Z6
odgovara tekstu.

## Što je posebno dobro

- Referentni tlak (apsolutni/manometarski) i referentna brzina za $\xi$
  dosljedno se ističu (`u13:29`, `u13:89–97`). NPSH se računa na dva neovisna
  načina koji se slažu (P6).
- Izvod $\lambda=8\tau_{st}/(\rho v^2)$ iz ravnoteže sila odsječka kratak je i
  fizikalno jasan. Povezuje Darcyjev koeficijent s naprezanjem stijenke i
  objašnjava zašto je laminarni $\Delta p$ linearan u $Q$.
- P4 i sažetak ispravno i izričito pokazuju da se afinitetni zakoni ne prenose
  na sustav sa statičkom visinom. Brojčana usporedba 0,899 prema 0,865 dobar je
  dokaz.
- Lanac snaga $P_{el}\to P_{vr}\to P_h$ i upozorenje o oduzimanju disipacije na
  ventilu (`u13:335`) rješavaju čestu studentsku zabunu.
- Z4 traži oba reziduala, a Z6 traži da student kaže koji podatci nedostaju
  (margina, $NPSH_r$ pri sniženoj brzini, zaprljan filtar, uvlačenje zraka pri
  njihanju). To je primjerena T4 odluka iz brodske prakse.
- CFD odlomci jasno odvajaju 1D mrežni model od lokalnog CFD-a i ne iznose
  rezultate simulacija koje nisu provedene.

## Ograničenja ove recenzije

Bilježnice (`u10_moody_dijagram`, `u13_paralelne_grane`), web izdanje ni izvor
dodatka F nisam otvarao. Vrijednosti $k_s$ za lijevano željezo, područje
valjanosti Swamee–Jaina i kriterij NPSH3 navodim prema općem stručnom znanju,
bez provjere u izvoru; prije unosa u tekst treba ih potvrditi u literaturi.
Ocjena razina T1–T4 je moja stručna procjena prema definicijama iz upute.
