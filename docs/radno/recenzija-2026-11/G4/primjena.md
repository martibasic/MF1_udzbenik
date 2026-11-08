# Primjenska recenzija G4 — pog. 14, pog. 15, dodatak D

Recenzent: neovisni primjenski recenzent (brodogradnja i strojarstvo), 8. 11. 2026.
Materijal: G4.pdf (knjiga str. 263–295 i 323–330) i izvori
`source/u14_turbostrojevi_i_propulzija.md`, `source/u15_otvoreni_tokovi.md`,
`source/d04_numericka_mehanika_fluida.md`. Mjerila: uputa za primjenskog
recenzenta, K9, K14, K16 i ljestvica P0–P3 iz `docs/konvencije_pisanja.md`.

Napomena o izvorima: web nije pretraživan. Svi rasponi koje navodim kao
„realne” potječu iz mojeg inženjerskog iskustva i iz standardne literature po
sjećanju (Carlton, *Marine Propellers and Propulsion*; Gülich, *Centrifugal
Pumps*; Chow, *Open-Channel Hydraulics*; Peterka, USBR Engineering Monograph 25).
Označeni su s **(po sjećanju)** i prije unosa u tekst treba ih provjeriti u
izvoru.

## Sažetak

Pog. 14 ima vjerodostojne i dobro ograđene primjene. Balastna crpka, propeler
obalnog broda i električni vodomlazni pogon brojčano su realni, a granice
modela jasno su odvojene od projektne ocjene. Pog. 15 je primjenski
jednostran: svi riješeni primjeri i zadatci pripadaju hidrotehnici gradskih
kanala, a brodogradnja se javlja samo u jednom okviru o plitkoj vodi, dok
strojarstvo izostaje. Dodatak D u pregledu CFD primjena nema niz trup–propeler,
koji je glavna industrijska CFD primjena u brodogradnji.

Nema nalaza P0 ni P1. Ima sedam nalaza P2 i jedanaest nalaza P3.

## Nalazi

### P2

**P2-1. Pog. 15 nema primjene iz brodogradnje ni iz strojarstva (K16).**
Mjesto: str. 283–295, cijelo poglavlje. Riješeni primjeri su
`ex-rezim-retencijski-kanal`, `ex-kriticni-preljev`, `ex-dvije-dubine`,
`ex-hidraulicki-skok-bazen` i `ex-manning-osjetljivost`. Zadatci su
`task-otvoreni-fr` … `task-klimatski-kanal`.
Opis: uvod (str. 283) najavljuje „vučne bazene te plovidbu u plitkoj vodi”,
no to se pojavljuje samo u okviru „Isti Froudeov broj u kanalu i uz brod”
(str. 284), bez računa. Svih 11 primjena (P1–P5, Z1–Z6) pripada gradskom
kanalu, oborinskoj odvodnji i ustavi. Student strojarstva nema nijedan uređaj
ili postrojenje, a student brodogradnje nema nijedan račun. Kurikularna matrica
poglavlju doduše namjenjuje lajtmotiv „klimatski otporan vodni grad”, pa to nije
kršenje ugovora. Ipak se kosi s K16 („primjeri iz brodogradnje i strojarstva”).
Prijedlog: ne dodavati mjesta. Jedan Z iste razine zamijeniti zadatkom iz
banke alternativa ili tako preoblikovati jedan P:
- *brodogradnja*: brod u ograničenom kanalu kao suženje presjeka. Povratno
  strujanje i spuštanje razine dobiju se iz kontinuiteta i specifične energije,
  a granična brzina odgovara minimumu $E$. Taj račun izravno nastavlja okvir
  sa str. 284 i prirodan je T3. Druge mogućnosti su punjenje suhog doka ili
  brodske prevodnice kroz kanal s ustavom te voda na palubi kao val nakon
  loma brane;
- *strojarstvo*: dovodni ili odvodni kanal rashladne vode termoelektrane ili
  postrojenja za desalinizaciju, mjerni preljev (Parshallov kanal) u
  postrojenju za obradu voda ili dovodni kanal male hidroelektrane. Posljednja
  primjena povezuje se s Peltonovim kolom iz pog. 14.

**P2-2. Z6 pog. 14: nejasan uređaj i nerealna rezerva potiska.**
Mjesto: str. 281–282, `task-u12-mlazna-platforma-ukupne-mase-ima-cetiri-jednake`.
Opis: „mlazna platforma” nije imenovana kao poznata naprava (vodeni
*jetpack*/*flyboard*, nosač mjerne opreme, ispitni model?). Brojke daju
$F_T\approx3{,}19$ kN za $m=110$ kg, dakle potisak $\approx2{,}95\,mg$ i
početno ubrzanje $\approx19$ m/s². Nijedna upravljana lebdeća naprava ne radi
u nazivnoj točki s trostrukom rezervom potiska. Mlazovi pritom nose hidrauličku
snagu oko $\tfrac12\rho Qv^2\approx57$ kW (moj račun iz zadanih podataka).
Kontekst stoga djeluje nategnuto, iako je razgraničenje od certificirane
nosivosti dobro napisano (Traži se 3).
Prijedlog: imenovati uređaj i radnu točku približiti lebdenju. Primjerice
$v\approx22$–$24$ m/s pri istim sapnicama daje $F_T/mg\approx1{,}1$–$1{,}3$,
pa provjera 10 % rezerve u intervalu ulaza postaje stvarna odluka. Posljedice
za ključ i verifikator treba provjeriti.

**P2-3. P5 pog. 14: „bira se najveći propeler koji gaz i trup dopuštaju” je
prejaka tvrdnja (K9).**
Mjesto: str. 276–277, `ex-propeler-u-napredovanju`, Provjera i tumačenje.
Opis: zaključak vrijedi unutar modela diska, ali je napisan kao pravilo
projektiranja. Kod stvarnog propelera optimalni promjer pri zadanoj snazi
određuje i brzina vrtnje motora ili reduktora. Veći promjer zahtijeva manju
brzinu vrtnje i veći moment, a time i veći reduktor. S površinom lopatica rastu
gubitci trenja. Zračnost vrha prema trupu ograničena je zbog vibracija i
tlačnih pulsacija, a u balastnom stanju traži se dovoljan uron vrha.
Prijedlog: „U modelu diska veći promjer uvijek štedi snagu; stvarni izbor
promjera ograničavaju i brzina vrtnje pogona, zračnost prema trupu i uron vrha
lopatica.” Odlično mjesto i za vezu s lajtmotivom dekarbonizacije (P2-6).

**P2-4. Iskustveni rasponi bez izvora ili oznake nastavne procjene (K14).**
Mjesta:
- str. 277, `ex-propeler-u-napredovanju`: „$\eta_0\approx0{,}55$–$0{,}70$”.
  Raspon je realan za trgovačke propelere u slobodnoj vožnji, oko 0,5–0,7
  (po sjećanju, Wageningen B-serija i Carlton), ali nema izvor;
- str. 275, `ex-radijalno-kolo-crpke-euler`: „pretpostavljeni umnožak faktora
  klizanja i hidrauličke učinkovitosti $\approx0{,}82$” označen je kao
  pretpostavka, što je dovoljno za K14. Vrijednost je ipak optimistična. Za kolo
  sa 6–7 lopatica i $\beta_2=25^\circ$ Wiesnerova procjena daje faktor
  klizanja (smanjenje $c_{2t}$) oko 0,75–0,8, a uz $\eta_h\approx0{,}85$–$0{,}9$
  umnožak za visinu iznosi oko 0,65–0,72 (po sjećanju, Gülich);
- str. 286 i 289, $C_d\approx0{,}55$–$0{,}60$ i „$C_{pr}$ … blizu jedinice”
  bez izravnog upućivanja. Chow se navodi drugdje u poglavlju.

Prijedlog: uz $\eta_0$ dodati izvor iz dodatka E ili napisati „orijentacijski,
nastavna procjena”. Uz 0,82 dodati „optimistično” ili sniziti vrijednost na
približno 0,7. Uz $C_d$ i $C_{pr}$ upisati [@chow1959].

**P2-5. Z6 pog. 15: značenje „dopuštene spregnute dubine” nije inženjerski
jasno.**
Mjesto: str. 294, `task-klimatski-kanal`, Traži se 2.
Opis: kod umirnog bazena mjerodavno je odnosi li se nizvodni vodostaj prema
spregnutoj dubini $y_2$. Ako je vodostaj manji, skok bježi iz bazena (to P4
dobro objašnjava). Uz to valja paziti i na visinu zidova. U Z6 je
$y_{2,dop}=1{,}40$ m samo „podatak”. Rezultat $y_2=1{,}059$ m $<1{,}40$ m
student ne može fizikalno protumačiti: je li to visina zida, potrebni
nizvodni vodostaj ili nešto treće? Pri $Fr_1\approx2{,}47$ skok je k tome na
granici slabog skoka, pa je bazen za tu svrhu jedva potreban.
Prijedlog: $y_{2,dop}$ definirati kao najveću dubinu koju dopuštaju zidovi
bazena uz slobodni rub i dodati podatak o nizvodnom vodostaju, tako da odluka
glasi „ostaje li skok u bazenu i stane li u njega”. Razina T2 se ne mijenja.

**P2-6. Lajtmotiv dekarbonizacije pomorstva u pog. 14 je implicitan (K16,
suvremenost).**
Mjesto: str. 263–282.
Opis: kurikularna matrica određuje lajtmotiv „pomorska i offshore
dekarbonizacija”. Pog. 14 ima izvrsnu podlogu za nj (P5 s usporedbom promjera,
Z5 s električnim vodomlaznim pogonom), ali ga nigdje ne imenuje. Nema ni
offshore vjetra, iako je aktuatorski disk njegov izravni model: Betzova granica
$16/27$ izlazi iz istog izvoda uz obrnut predznak rada. Samoprovjera 4
(str. 278) vjetroagregat spominje samo kinematički.
Prijedlog: jedna rečenica u P5 („ušteda $\approx87$ kW pri istom potisku je
smjer kojim se smanjuju potrošnja goriva i emisije; propeler većeg promjera i
manje brzine vrtnje uobičajena je mjera za poboljšanje energetske učinkovitosti
postojećih brodova”) te jedna rečenica u provjeri izvoda aktuatorskog diska o
vjetroagregatu ($v_j<v_A$, rad prelazi s fluida na rotor, Betz). U banku
alternativa dodati T2 zadatak: snaga offshore vjetroagregata zadanog promjera
prema Betzovoj granici i usporedba sa stvarnim $C_P\approx0{,}45$–$0{,}5$
(po sjećanju).

**P2-7. Dodatak D: tablica povezanih CFD primjena nema niz trup–propeler.**
Mjesto: str. 323, tablica „Povezani primjeri kroz knjigu”.
Opis: tablica ima rashladni krug (strojarstvo), cisternu i ponton (brod,
offshore), gradski kanal i zračnu sapnicu. CFD otpora broda, samopropulzije i
propelera iza trupa glavni je industrijski CFD posao u brodogradnji. Knjiga
ima sve sastojke: model broda u pog. 11, granični sloj trupa u pog. 12 i
odlomak „Propeler iza trupa” u pog. 14. Tablica ih ipak ne povezuje, a
odlomak „Propeler iza trupa” nema stabilan ID na koji bi se moglo uputiti.
Isto vrijedi za odlomke „Crpka rashladnog kruga iznutra” (pog. 14) te
„Hoće li prag uzvodno podići vodu?” i „Cijeli kanal i detalj oko ustave”
(pog. 15).
Prijedlog: dodati redak „Trup i propeler: model i sličnost → granični sloj
trupa → propeler iza trupa | snaga za zadanu brzinu”. CFD odlomcima bez ID-ja
dodijeliti stabilne ID-jeve prema pravilima novih semantičkih ID-jeva. Za
studente brodogradnje uz NASA i ASME V&V dodati preporučeni postupak ITTC-a
za nesigurnost u CFD verifikaciji i validaciji (po sjećanju, oznaka
7.5-03-01-01; provjeriti aktualno izdanje).

### P3

**P3-1. P4 pog. 14: brzina vrtnje brodske crpke.** `ex-radijalno-kolo-crpke-euler`,
str. 274. $n=1450\ \mathrm{min^{-1}}$ odgovara četveropolnom motoru na mreži
50 Hz. Većina trgovačkih brodova ima mrežu 440 V / 60 Hz, pa su tipične brzine
vrtnje oko 1750–1780 ili 1170 $\mathrm{min^{-1}}$ (po sjećanju). Primjer nije
pogrešan, jer brodovi s mrežom 50 Hz postoje, ali student brodogradnje to može
primijetiti. Moguće rješenje je kratka napomena „brodska mreža 50 Hz” ili
prerada na 60 Hz uz pratnju verifikatora. Protok $162\ \mathrm{m^3/h}$ pri
$H\approx23$ m odgovara balastnoj crpki manjeg broda. Kod većih brodova
uobičajene su stotine do više od tisuću $\mathrm{m^3/h}$ (po sjećanju). Dovoljno
je napisati „balastna crpka manjeg broda”.

**P3-2. P3 pog. 14: brzina vrtnje Peltonova kola i generator.**
`ex-u12-peltonov-rotor-s-jednim-mlazom-i-momentom`, str. 272–273.
$n=320\ \mathrm{min^{-1}}$ nije sinkrona brzina izravno spojenog generatora,
ni pri 50 Hz (333 ili 300) ni pri 60 Hz. Prijedlog: uzeti
$333\ \mathrm{min^{-1}}$ ili napisati da je generator spojen preko remenskog
prijenosa ili pretvarača. Rečenicu „pitanje regulacije sapnice” može
konkretizirati naziv „regulacijska igla sapnice”. Omjer $u/c_1\approx0{,}50$
teorijski je optimum. Izvedena kola rade nešto niže, pri
$u/c_1\approx0{,}45$–$0{,}48$ (po sjećanju). Jedna rečenica o tome povezala bi
model s praksom.

**P3-3. P4 pog. 15: Froudeov broj pripada području oscilirajućeg skoka.**
`ex-hidraulicki-skok-bazen`, str. 289. $Fr_1=3{,}83$ leži u području
$\approx2{,}5$–$4{,}5$ koje se u literaturi umirnih bazena opisuje kao
oscilirajući skok s valovima nizvodno i nepovoljno za bazen (po sjećanju, Chow
i Peterka/USBR). Jedna rečenica u provjeri pokazala bi da $Fr_1$ ne određuje
samo $y_2$ nego i vrstu bazena.

**P3-4. P6 pog. 14: kontekst drona.**
`ex-u12-propeler-dronskog-kvadkoptera-u-stanju-visa-t2`, str. 277–278.
Primjer je brojčano realan: oko 227 W i do 19,5 min za 2,4 kg i propeler od
11 inča. Struci bi bio bliži uz okvir „dron za daljinski pregled tankova ili
oplate broda”, jer klasifikacijska društva takve preglede danas prihvaćaju.
Tada valja dodati ogradu da utjecaj stijenki i dna tanka nije u modelu.
$FM=0{,}70$ je na gornjem rubu za male rotore pri niskom $Re$, gdje je
tipično oko 0,5–0,65 (po sjećanju).

**P3-5. P5 pog. 14: sustrujanje.** $\chi\approx0{,}14$ uz $v_s=7$ m/s
tipičnije je za dvovijčani brod. Jednovijčani obalni brod obično ima
$\chi\approx0{,}2$–$0{,}35$ (po sjećanju). Moguća je napomena „dvovijčani
brod” ili drukčija brzina broda.

**P3-6. Uvod pog. 14: prijenos otpora Froudeovom sličnošću.** Str. 263
(odlomak 4): „otpor trupa, koji se iz modelnih ispitivanja prenosi Froudeovom
sličnošću”. Točnije je „…Froudeovom sličnošću za valni otpor, uz zasebno
preračunavanje otpora trenja prema $Re$”, ako to pog. 11 već ne kaže na mjestu
na koje se upućuje.

**P3-7. Z5 pog. 14: realnost omjera brzina.**
`task-vodomlazni-pogon-uz-ogranicenu-snagu`. Kao suvremena električna primjena
zadatak je dobar. Varijanta B s $v_j/v_s=3{,}75$ namjerno je nepovoljna.
Projektni omjer vodomlaznih pogona brzih plovila obično je oko 1,5–2,5
(po sjećanju), pa je varijanta A realna. Rečenica „B predstavlja preopterećen
vodomlazni pogon” pojasnila bi namjeru. Model zanemaruje gubitke u usisu
vodomlaznog pogona, koji su u praksi znatni. Zadatak to navodi, a dobro bi bilo
dodati i da je sustrujanje u usisu u stvarnosti povoljno.

**P3-8. Nazivlje brodske hidrodinamike (napomena, ne nalaz).**
„Propeler” je potvrđeni autorski naziv. U dijelu hrvatske brodograđevne
literature i prakse ravnopravno se rabe „brodski vijak” i „poriv”
(umjesto „potisak”), a odbitak potiska zove se „koeficijent upijanja $t$”
(po sjećanju, nisam siguran u ujednačenost). Prijedlog: pri prvom spomenu u
pog. 14 navesti „propeler (brodski vijak)” i „potisak (poriv)”, a
„odbitak potiska” (str. 268) usporediti s nazivljem kolegija Otpor i propulzija
broda na FESB-u. „Koeficijent sustrujanja”, „brzina napredovanja” i
„učinkovitost u slobodnoj vožnji” odgovaraju struci.

**P3-9. Nazivlje pog. 15: „vučni bazen” i *squat*.**
Str. 283–284. Hrvatski brodograđevni naziv za *towing tank* češće je „bazen za
ispitivanje modela” ili „bazen za tegljenje modela” (po sjećanju). „Vučni
bazen” razumljiv je, ali zvuči kao doslovni prijevod. Za *squat* bi valjalo
navesti hrvatski opis, npr. „uron i trim broda u plitkoj vodi”, a engleski
naziv ostaviti u zagradi. Ostalo nazivlje je dosljedno: mirni i siloviti tok,
spregnute dubine, umirni bazen i slobodni rub.

**P3-10. Dodatak D, hijerarhija modela.** Str. 325, tablica „Kada CFD ne
treba”. Svi reci osim „gaza i malog nagiba plovila” pripadaju strojarstvu ili
općoj hidraulici. Nedostaje redak koji bi izravno pomogao studentu
brodogradnje, npr. „otpor broda: Froudeova ekstrapolacija iz modelnog pokusa
→ CFD kad se ispituje oblik krme ili uređaj za uštedu energije”.

**P3-11. P1 i P2 pog. 14 bez tehničkog konteksta.** Str. 269–271. Vodilica
„na ispitnom stolu” i opća pokretna lopatica nemaju uređaj. To je prihvatljivo
za uvodne T2 i T3, jer ih P3–P6 nadoknađuju. Ako se primjer ikada mijenja,
lopatica bi se mogla vezati uz akcijsku turbinu ili ispitni stol za mlazni
razdjelnik.

## Ravnoteža struka po poglavlju

| Poglavlje | Brodogradnja / pomorstvo | Strojarstvo / energetika | Ocjena |
|---|---|---|---|
| 14 | P4 balastna crpka, P5 propeler, Z5 vodomlazni pogon, CFD propeler iza trupa | P3 Pelton, CFD crpka rashladnog kruga, P4 (crpka općenito) | uravnoteženo; nema ventilatora, kompresora ni vjetroagregata |
| 15 | samo okvir o plitkoj vodi (bez računa) | izostaje | jednostrano hidrotehničko (P2-1) |
| D | ponton, balastni tank u tablici pojmova | rashladni krug, Venturi, sapnica | nedostaje niz trup–propeler (P2-7) |

## Posebno dobre primjene

- `ex-radijalno-kolo-crpke-euler` (str. 274–275). Geometrija je realna:
  $D_2=260$ mm, $b_2=20$ mm, $\beta_2=25^\circ$, $n_q\approx30$ (moj račun),
  kolo je radijalno. Rastav specifičnog rada i izričita veza s radnom točkom iz
  pog. 13 primjeren su inženjerski slijed.
- `ex-propeler-u-napredovanju` (str. 276–277). $C_{Th}\approx1{,}1$,
  $\Delta p\approx20$ kPa i potrebna snaga reda 1,2–1,5 MW realni su za obalni
  brod s propelerom promjera 3,2 m. Usporedba dvaju promjera i sustrujanje
  pokazuju studentu stvarnu projektnu odluku.
- `task-vodomlazni-pogon-uz-ogranicenu-snagu` (Z5). Električni pogon s
  ograničenom snagom realna je i suvremena odluka. Bilanca traga jasno pokazuje
  zašto veća brzina mlaza ne znači bolji pogon.
- Granica modela i CFD odlomak „Propeler iza trupa” (str. 268–269). Ispravno
  razlikuju disk kao raspodijeljenu silu od razlučenih lopatica i naglašavaju
  da potisak treba povezati s otporom trupa.
- Okvir „Isti Froudeov broj u kanalu i uz brod” (str. 284). Plitka voda, valni
  otpor, *squat* i blokada vučnog bazena opisani su točno i jezgrovito. Na toj
  osnovi treba izgraditi brodograđevni zadatak iz P2-1.
- `ex-hidraulicki-skok-bazen` (str. 289). Odluka o položaju skoka prema
  nizvodnom vodostaju, s ispravnim zaključkom o spuštenom dnu ili završnom
  pragu, odgovara pravom projektantskom pitanju.
- `task-klimatski-kanal` (Z6 pog. 15). Osjetljivost kapaciteta na stanje
  održavanja (raspon $n$ prema Chowovim tablicama, po sjećanju) i slobodni rub
  realna su inženjerska odluka s dobrom ogradom „nastavne procjene”.
- Dodatak D, granica modela „Aeroprofil nije automatski hidroprofil”
  (str. 329). To je točno ono upozorenje koje student brodogradnje treba.

## Razgraničenje recenzije

Ovo je autorska procjena primjenskog recenzenta. Izvode nisam provjeravao, osim
pojedinačnih brojeva koje sam za vjerodostojnost ponovno izračunao iz zadanih
podataka. Ključ rezultata, verifikatore i bilježnice nisam čitao. Svi rasponi
označeni s „po sjećanju” traže provjeru u izvoru prije unosa u priručnik.
