# Stručna recenzija, poglavlja 9–12 (drugi neovisni model)

Poglavlja: 9 Kompresibilni idealni tok, 10 Količina i moment količine gibanja,
11 Dimenzijska analiza i sličnost, 12 Diferencijalni opis realnog toka
(PDF skupine G3, knjiga str. 169–244; ključ G3_kljuc.pdf; izvori `source/u09`–`u12`).
Oznake mjesta: `datoteka:redak` u `source/`, zatim stranica knjige. Poznati nalazi
razine knjige (a)–(e) nisu ponovljeni.

## Sažetak

Fizika i brojevi u sva četiri poglavlja su ispravni: ponovno sam izračunao sve
riješene primjere, sve kontrolne rezultate Z1–Z6 i brojeve ključa, i nisam našao
odstupanje veće od zaokruživanja (nalaza P0 i P1 nema). Preostali nalazi odnose se
na tekst (netočna rečenica o kutu u P1 pog. 10, pogrešno uvođenje Navier–Stokesove
jednadžbe u pog. 12, St u pog. 11), na ponavljanje zadataka i primjera (K15, K10) te
na skice i prijelom.

Broj nalaza: P0 = 0, P1 = 0, P2 = 12, P3 = 16 (uz jednu pozitivnu napomenu, S29).

## Što je provjereno računom (bez odstupanja)

Pog. 9: brzine zvuka (343,1 m/s; helij 1019,2 m/s), Ma 0,244 i 0,317, Pitotova sonda
(T0 = 293,3 K, p0/p = 1,524, nestlačiva procjena −14,6 %), ṁmax = 0,07001 kg/s,
p* = 316,8 kPa, Prandtlova relacija i Δs = +93,9 J/(kg K), A/A* = 1,6 daje Ma = 0,3970 i
1,9353, pe = 448,5 / 70,7 / 297,0 kPa, ṁ = 0,1167 kg/s, val za pb = 350 kPa u presjeku
Ax/A* = 1,391 uz Ma1 = 1,7545 i p02/p01 = 0,8326 (tekst 1,39; 1,75; 0,833), Z2 0,850 kg/s i
2,94 s, Z4 (Mae = 0,8477; p* = 4,226 bar), Z5 (CdAg = 42,50 mm², Cd = 0,885), Z6
(Ma1 = 2,000 ± 0,0068; Λ = 0,72087; dΛ/dMa = −0,467; s(Λ − Λmj) = 0,0085; razlika 0,050).
Pog. 10: sve sile i brzine u P1–P7 (npr. koljeno 1402,6/665,0 N, β-varijante −1404/669 i
−1429/725 N, T-račva 891/503 N, Y-račva 665 N i 913 N, hidrokoljeno I = 9827 N),
Z1–Z6 (Z6: Fx = 2835,8 N, Fy = −44,0 N, maksimum 2918,3 N pri 190 kPa; 39,2 L/s; s = 0,57;
1,15·Fmax = 3356,1 N). Pog. 11: Re 7200 i 45, Fr 0,2346, Re omjer 125, CF 2,96·10⁻³ i
1,48·10⁻³, σkav = 0,5425, Qmax = 4,447 L/s, We = 31,25, Bo = 1,225, Lc = 2,711 mm, Π1 = Cd·π/8,
Z1–Z6 (Manning v = 1,0016 m/s, 2,21 ft/s; σ 9,708 / 2,427; preljev 224 ± 4,8 i 216 ± 5,4 kN).
Pog. 12: ωSST = 51,1 s⁻¹, ε = 1,59, Δp = 651,9 Pa, Re = 12,7, interpolacije 6,279 i 6,543,
Z1–Z6 (τ0 = ±20 Pa, H/11; Blasius 2,582 mm; GCI 1,237 % i 0,312 %; 2sE = 0,000490 i 0,000663).
Jedina razlika: pog. 10, P3, Rx = −1402,65 N (točno) prema −1402 N u tekstu
(zbroj zaokruženih članova); zanemarivo.

## Nalazi

### P2

**S01. Pelton, opis kuta (K15/K6).** `u10:224`, str. 189; `ex-peltonova-lopatica-u-gibanju`,
`fig-peltonova-lopatica-u-gibanju`. Tekst: „skreće relativni tok simetrično za θ = 165°, tako da
relativna izlazna brzina zatvara kut od 15° s dolaznim mlazom”. Račun i skica koriste
w·cos165°, tj. izlazna brzina zatvara 15° s *suprotnim* smjerom dolaznog mlaza (165° s dolaznim).
Doslovno čitanje daje drugi zadatak: Fx = ṁrel·w·(1 − cos15°) = 35,27·18·0,0341 = 21,6 N umjesto
1248 N. Prijedlog: „zatvara kut od 15° sa suprotnim smjerom dolaznog mlaza”.

**S02. Isti zadatak u dva poglavlja (K15).** `u11:661–711` (`ex-u14-machov-i-strouhalov-broj-stlacivost-i-vrtlozno`,
str. 222), prvi dio, ponavlja `u09:108–133` (`ex-odabir-modela-kompresibilnosti`, str. 171):
zračni vod D = 80 mm, dva protoka, ocjena Ma prema pragu 0,3 i granični protok.
Račun: u pog. 9 Q = 0,42 i 0,546 m³/s daje Ma = 0,244 i 0,317; u pog. 11 Q = 0,40 i 0,80 m³/s daje
0,234 i 0,468, Qlim = 0,513 m³/s (isti postupak, ista odluka). Prijedlog: u pog. 11 zamijeniti prvi dio
primjerom gdje se Ma bira kao grupa uz drugu grupu (npr. Ma uz Fr ili Re), ili ga ukloniti i ostaviti St.

**S03. Z5 (T3) ponavlja izvod i P5 (K10, K15).** `u11:889–915` (`task-u14-frekvencija-otpustanja-vrtloga-iza-geometrijski-slicnog-tijela`, str. 225),
`u11:590–641` (`ex-u14-buckinghamova-analiza-otpora-kugle-i-krivulja-cd`, str. 220) i izvod `u11:225–253`
(`eq-slicnost-matematicki-izvod-otpor-kugle-daje-cd-re-01`). Isti postupak triput: n = 5, k = 3,
ponavljajuće ρ, v, D, μ → Re (a = b = c = −1). P5 ne dodaje odluku, nego ponavlja korake izvoda i dodaje Fd = CD·½ρv²A
(0,0763 N). Razina T3 („izbor ili spajanje modela”) nije poštena: u Z5 student ne bira model, nego ponavlja
poznati postupak s drugom zavisnom varijablom. Prijedlog: P5 skratiti na brojčani dio uz upućivanje na izvod;
Z5 označiti T2 ili mu dati pravu odluku (npr. izbor nepotpunog skupa varijabli: zašto bez μ ili s g zadatak
ne prenosi).

**S04. Z3 pog. 12 je obrnuti P iz istog poglavlja (K15, razina).** `u12:589–617` (`task-poiseuille-inverzni`, str. 241)
i `u12:237–257` (`ex-laminarni-mikrokanal`, str. 233): ista kapilara (D = 0,50 mm, L = 0,20 m, Q = 0,30 mL/min),
Δp = 652 Pa je rješenje primjera, μ = 1,000 mPa s je ulaz primjera. Nova je samo RSS propagacija
(relativno 4 %, 0,77 %, 0,5 %, 1 % → s(μ)/μ = 4,22 %, s(μ) = 0,0422 mPa s), a to je „nesigurnost”,
dakle T4 prema definiciji razina, a ne T2. Prijedlog: razina T3/T4 ili zamjena drugim uređajem
(npr. rotacijski viskozimetar s Couetteovim tokom).

**S05. Navier–Stokes „poseban slučaj” zakona viskoznosti (fizikalna jasnoća).** `u12:3`, str. 228:
„Njezin je najjednostavniji poseban slučaj zakon viskoznosti iz pog. 2.” Newtonov zakon viskoznosti je
konstitutivna veza koja *ulazi* u jednadžbu (izvod `u12:87–95` to ispravno kaže), a ne njezin poseban
slučaj. Student može izvesti pogrešan zaključak o hijerarhiji zakona. Prijedlog: „Zakon viskoznosti iz
pog. 2 ulazi u nju kao veza naprezanja i brzine deformacije.”

**S06. Dvije konvencije za τ (K6/K15 „na koje tijelo”).** `u12:264` (`eq-realni-tok-granicni-sloj-smicno-naprezanje-i-odvajanje-sec-01`,
str. 233–234) definira τst = μ ∂v/∂y|st, što je za donju stijenku sila fluida na stijenku. Napomena uz skice
`u12:527` (str. 240) kaže da je τst „naprezanje stijenke na fluid” (strelica u Z2 usmjerena uz stijenku
suprotno toku), a Z4 `u12:625` definira τ0 kao silu fluida na donju ploču. U Z2 se rabi samo |τ|, pa
rezultat nije pogrešan, ali tri tijela i dva predznaka u istom poglavlju. Prijedlog: jedna definicija (npr.
„τst je naprezanje kojim fluid djeluje na stijenku”) i skica Z2 s tim smjerom.

**S07. St ≈ 0,2 izvan navedenog područja (K9/K16).** `u11:661–711`, str. 222 (dimnjak) uz `u11:107`
(„za kružni cilindar u određenom subkritičnom području ... St reda 0,2”). Za D = 2,0 m, v = 12 m/s,
ν = 1,5·10⁻⁵ m²/s (vrijednost nije zadana u zadatku): Re = 1,6·10⁶; pri „rezonantnih” 6,0 m/s Re = 8·10⁵.
To je nadkritično područje u kojem je vrtložni trag širokopojasan i St nije jednoznačno 0,2. Poglavlje samo
upozorava na subkritični St, a primjer to ne spominje. Prijedlog: navesti Re dimnjaka i označiti St = 0,2
kao nastavnu orijentaciju za konstrukciju, ili uzeti manji promjer (npr. stup 0,3 m u vodi, Re ≈ 10⁵).

**S08. Z6 pog. 12 (T4): nedefinirani pojmovi, put repozitorija, naputak rješava (K1, K5, K15).**
`u12:683–712`, str. 242 (`task-cfd-tri-mreze`). (a) „GCI”, „Richardsonova ekstrapolacija”, „red konvergencije”
nigdje u pog. 12 nisu definirani; prvo pojavljivanje je u samom zadatku, definicija je u dodatku D (`d04`), bez
upućivanja. (b) Vidljivi tekst sadrži put `data/cfd/poiseuille_laminar` (K1: interna datoteka); isto „izvornih
datoteka” (`u12:434`, str. 238) kao poveznica bez adrese u ispisu. (c) Naputak (`u12:697`) daje cijele formule za
nh, Qext i GCI, pa ostaje aritmetika (naputak „usmjerava, a ne rješava”). Brojeve sam provjerio: nh = 2,0001,
Qext = 7,85399·10⁻⁶, GCI = 1,237 % i 0,312 %. Prijedlog: definirati GCI i Fs jednom rečenicom u poglavlju ili uputiti na
dodatak D; ukloniti put; naputak svesti na „provjeri monotonost niza i red konvergencije”.

**S09. „Snaga mlazova” 440 W (jasnoća, fizika).** `u10:857`, str. 201 (`ex-rotirajuca-mlaznica-pranje-tanka`):
„snage mlazova ṁ(w² − u²)/2 ≈ 440 W”. Apsolutna kinetička snaga izlaznih mlazova je ṁ(w − u)²/2 =
2,794·16,25²/2 = 369 W; 440 W = 369 W + Mω (71 W) je snaga koju vodi predaje dovod (tlačna energija u
rotirajućem sustavu). „Ostatak odnosi mlaz” (369 W) je zato točno, ali izraz „snaga mlazova” označuje drugu
veličinu od one koju nosi mlaz. Prijedlog: „snaga koju dovod predaje vodi ṁ(w² − u²)/2 = 440 W; od toga je
71 W kočena snaga, a 369 W ostaje kao kinetička energija mlaza”.

**S10. Tvrdnja o nesigurnosti bez podataka (K9/K15).** `u10:712`, str. 198 (`ex-u11-y-racva-s-mjerenom-reakcijom-konzole-t4`):
„rezerva od 87 N (oko 9 %) usporediva je s nesigurnošću mjerenja sile”, a zadatak ne navodi nikakvu nesigurnost
Ry. Također T4 se u primjeru ostvaruje samo usporedbom s kriterijem R ≤ 1,0 kN; nesigurnost i podatci ne ulaze u
račun (v ∝ √Ry daje samo osjetljivost: +10 % Ry → +4,9 % v). Prijedlog: zadati s(Ry) i dodati RSS ili usporedbu
|R − 1,0 kN| s 2s, ili izbaciti rečenicu i razinu spustiti na T3.

**S11. Izvor praga We ≈ 12 (K14), nisam siguran.** `u11:91`, str. 209: prag je pripisan [@white2011], općem
udžbeniku. Ne mogu provjeriti sadrži li taj izvor upravo ovaj prag (u literaturi o raspadu kapi pojavljuje se u
specijaliziranim radovima). Ako ne sadrži, pripisivanje krši „djelu se pripisuje samo ono što u njemu piše”.
Prijedlog: provjeriti u izvoru; ako ga nema, izvor iz dodatka E ili „nastavna orijentacija”.

**S12. Skica uvoda pog. 10, oznaka presjeka 1 (K13/AGENTS).** `fig-uvod-u11`, `u10:11`, str. 184:
brojka „1” stoji iznad zavoja u sredini slike, a ulazni presjek (isprekidana crta) je na lijevom kraju; strelica
težine FG polazi od ruba stijenke i izlazi iz cijevi (težina bi trebala djelovati iz fluida unutar KV).
Tekst (`u10:9`) kaže „u sredini težina”. Prijedlog: oznaku 1 uz isprekidanu crtu ulaza; FG iz težišta fluida u
koljenu.

### P3

**S13. Ponavljanja manje težine (K15).** (a) `u09` Z2 (`task-zrak-za-upucivanje-motora`, str. 179) isti
postupak kao P2 `ex-priguseni-ventil` (str. 174): provjera pb/p0 prema 0,528, ṁ iz jednadžbe
`eq-priguseni-protok` (0,0700 → 0,850 kg/s), uz Z1 helij koji je prvi korak P1. Novo samo t = m/ṁ.
(b) `u10` Z5 (`task-mlaz-na-pomicnu-plocu`, str. 202) je P1 s θ = 90° (isti koraci: ṁrel = ρA(v − u),
Fx, P = Fx·u, energijska provjera); novo je samo u = v/3 za jednu ploču (račun: 15,05 kg/s; 180,6 N;
1,445 kW; 1,486 kW; potvrđeno), a oznaka T3 (P1 T2) nije opravdana novom odlukom. (c) `u12` Z1
(`task-materijalna-derivacija`, str. 240) je P1 `ex-konvektivno-ubrzanje` (str. 229) plus član ∂v/∂t.
Prijedlog: Z1 u pog. 12 neka koristi 2D polje (ux, uy) ili polje iz cijevi sa suženjem; Z5 u pog. 10 neka mijenja
tijelo (npr. mlaz koji se dijeli na kosoj ploči); Z2 u pog. 9 neka traži odluku (npr. koliki A* da se postigne
vrijeme od 2 s).

**S14. Nazivlje „koeficijent protoka” (K6/K7).** `u09:627` (`task-sapnica-model`, naslov, str. 179): Cd je
u pojmovniku (`d02`) i u pog. 8 „koeficijent istjecanja”, a „koeficijent protoka” je u praksi Cv/Kv. Prijedlog:
„koeficijent istjecanja zagušene sapnice”.

**S15. Naputci koji rješavaju (K15).** Naputak u `u09:676` (Z6, str. 180), `u12:606` (Z3) i `u12:697` (Z6) daje
cijeli algoritam; u `u12:660` (Z5, `task-granicni-sloj-model`) sam „Traži se” otkriva zaključak („Mali ks/δB nemoj
poistovjetiti s dokazanom hidrauličkom glatkoćom ...”). Prijedlog: skratiti na smjer postupka.

**S16. Rotor, tijelo na koje moment djeluje (AGENTS: „na koje tijelo”).** `u10:202`
(`eq-moment-kolicine-gibanja`, bullet „Rotor”, str. 188): Mz = ṁ(r2 vt2 − r1 vt1) je lijeva strana
jednadžbe, dakle moment rotora *na fluid*; tekst piše samo „osna komponenta momenta”, a „pomnožena
kutnom brzinom daje snagu” traži obrnuti predznak za turbinu. Prijedlog: dopisati „moment lopatica na fluid; fluid
na rotor djeluje suprotnim momentom”.

**S17. Skica Z3 u pog. 10 (`fig-u11-vjezbe`, `u10:1093`, str. 204).** U izlaznoj nozi dvije strelice: gornja
(označena v2) usmjerena prema gore i druga, neoznačena, tamna, prema dolje; napomena (`u10:1095`) kaže da izlazni
tlak nije nacrtan, pa je druga strelica ili tlak ili višak. Isprekidana strelica gravitacije prelazi u oznaku
„Δz = 0,40 m”. Prijedlog: ukloniti neoznačenu strelicu; g pomaknuti.

**S18. Prijelom i preklapanja.** Str. 183: ~ četvrtina stranice prazna jer je slika 10.1 na idućoj; str. 205:
na stranici samo dvije natuknice iz završnog okvira pog. 10 (siroče); `fig-realni-tok-vjezbe` (Slika 12.2) razdvojena je
preko str. 239–240, panele Z1–Z4 nosi str. 239 bez potpisa, a Z5–Z6 str. 240 s potpisom. Na slici 9.2 (str. 181)
tekst „iz napojne komore” i „pb =” u panelu Z5 dodiruje stijenku sapnice; u Z4 pog. 10 (str. 204) oznaka yC dodiruje
nosač; na slici 10.2 (str. 189) „Fx” je djelomično prekriven lopaticom.

**S19. Ključ (G3_kljuc.pdf): udvojene stranice, nisam siguran je li greška PDF-a ili izrezivanja.** Stranice
346, 347 i 348 pojavljuju se po dvaput (PDF stranice 3/4, 5/6, 7/8 s istim sadržajem i istim brojem). Ako je to u
konačnom PDF-u, ključ ima tri suvišne stranice; provjeriti u izvornom ključu.

**S20. Duge rečenice (K3).** `u11:303` (58 riječi, Granica modela, str. 214; u njoj 25-riječna zagrada o faktoru
oblika), `u11:796` (44), `u12:139` (47, str. 231), `u10:118` (46, upit uz numerički pokus). Prijedlog: `u11:303`
raspodijeliti u natuknice (što ne ulazi u model: oblik trupa, hrapavost, stimulatori, slobodna površina).

**S21. K4/K10/K12/K13 u pog. 11.** (a) Odjeljak „Dimenzijska analiza i sličnost” (`u11:15–17`, str. 207) ponavlja
naslov poglavlja i uvod. (b) `u11:143–155`, str. 211: „Tablica sažima sve brojeve ...” bez numeriranog upućivanja
(`[-@tbl-…]`). (c) `fig-uvod-u14` (`u11:11`): fig-alt „Model automobila u aerotunelu s jednolikim dotokom” ne dodaje
ništa potpisu (K13); uvodna slika pokazuje automobil, a tekst i poglavlje nose brod i Froudea.

**S22. Empirijski pragovi i koeficijenti bez izvora (K14), manji.** `u10:452` ξ ≈ 0,34 „uobičajeno za koljeno sa
suženjem”; `u12:337` prirodni prijelaz 3·10⁵–3·10⁶; `u11:640` kriza otpora „nekoliko 10⁵”; `u12:403` ℓ ≈ 0,07 D
„uobičajena skala” (u rješenju označeno kao dogovorna, ali bez izvora); `u09:132` ventilacijski vodovi 10–20 m/s.
Prijedlog: izvor iz dodatka E ili „nastavna orijentacija”.

**S23. K5: kratice i imena programa.** `CFL3D`, `FUN3D` (`u12:434`, `u12:685`) bez opisa; `NPSH` (`u11:541`,
jedna uporaba u poglavlju) puni naziv; `ITTC` (`u11:286`) bez razrade pri prvom spomenu; „KV” (`u10:9`) rabljen prije
definicije u `u10:38`.

**S24. Preljev, red veličine sile (K16).** `u11:919–958` (`task-u14-preljev-brane-ispituje-se-vodenim-modelom-u`,
str. 225): hidrostatska sila za h = 7,5 m i b = Q/(vh) = 10,67 m je ½ρgh²b = 2,94 MN, a „sila vode na preljev nakon
tariranja” je 224 kN (model: 28 N prema 368 N hidrostatskih pri 1:20). „Nakon tariranja ostalih opterećenja” to
pokriva, ali ne kaže koja se sila mjeri. Prijedlog: reći koja komponenta (npr. dinamički dio) ostaje.

**S25. T-račva i Y-račva bez Granice modela (K11/K16).** `u10:455–583` (T3) i `u10:585–713` (T4): Bernoulli
bez gubitaka kroz račvu s grananjem od 60° i 90° je jaka idealizacija (gubitci na račvi nisu zanemarivi prema ρv²/2);
primjeri to ne komentiraju u „Provjeri i tumačenje”. Prijedlog: jedna rečenica o tome da pM1 i raspodjela protoka
stvarne račve ovise o gubitcima i da primjer pokazuje opterećenje pri zadanom (idealnom) režimu.

**S26. Redoslijed i razine (K15).** Pog. 10: P6 hidrokoljeno (T2, najlakši) stoji iza P5 (T4), a P1 (Pelton, kretanje
KV) prije osnovnog koljena. Pog. 11: P4 (We, Bo; dva izravna uvrštavanja) bliži je T1 nego T2; Z2 (Manning)
sadrži jediničnu odluku (stope) pa je prije T2 nego T1. Prijedlog: P6 premjestiti iza P3; razine uskladiti.

**S27. K9, „uvijek”.** `u09:370`: „p02 ... uvijek je manji od p01”, a pri Ma1 = 1 jednakost; dodati „za Ma1 > 1”.
Isto `u09:137`, str. 172: „Za razliku od ranije obrađenoga kruga s kapljevinom” (K12, opisno upućivanje: navesti pog. 8 i Venturijevu cijev).

**S28. Razina (nedostaje ili je preteško).** (a) Pog. 11 govori da se grupe izdvajaju „iz jednadžbi”, ali ne pokazuje
bezdimenzijski oblik Navier–Stokesove jednadžbe (inspekcijska analiza koja daje Re, Fr, Eu iz jednadžbe), a student će
je trebati kod CFD-a i modelskih ispitivanja; moguće kao „Dublje” blok uz upućivanje na pog. 12. (b) Pog. 12 Z6
(GCI, Richardson, RSS za CD, FUN3D) i primjer s k–ω SST i CFL3D traže više nego prvi kolegij zahtijeva; smatram da
je dio a) (red konvergencije, GCI) dovoljan, a dio b) preteško bez uvoda u nesigurnost (dodatak D).
Pog. 9 ne obuhvaća kose udarne valove ni trenje i izmjenu topline (Fanno, Rayleigh); to je prikladno za prvi kolegij.
Granica modela (`u09:457–461`) to navodi za trenje i toplinu, ali ne spominje da se P `ex-kd-sapnica-rezim` za
pb = 100 kPa poziva na kose valove izvan sapnice, koje model ne opisuje; dodati pola rečenice.

**S29. Napomena o CFD odlomcima (nije nalaz).** CFD odlomci u pog. 9–12 ne iznose rezultate koji nisu provedeni
(provjereno): opisuju pitanje, model, ulaze, izlaze i provjeru; razlikuju analitički model, numeričku integraciju i CFD.
Iznimka je jedino pozivanje na „objavljeni CFD rezultat” u P u `u12:427–459`, koje je izvorno navedeno (TMR,
Driver i Seegmiller), s napomenom da se ±0,10 ne tumači kao nesigurnost. Zabilježeno zbog potpunosti.

## Što je posebno dobro

- Svi brojevi se mogu ponoviti i unutarnje su dosljedni (tekst, kontrolni rezultat i ključ); posebno uredni su
  zadatci s intervalima (Z6 pog. 9, 10, 11 i 12) u kojima se odluka donosi na donjoj/gornjoj granici, a ne na nominalu.
- Pog. 9: izvod Prandtlove relacije i entropije korak po korak, dosljedna uporaba apsolutnih tlakova (P2,
  Z2, Z4), P „režim sapnice” s provjerom položaja vala (Ax/A* = 1,39) koji čitatelj može neovisno ponoviti.
- Pog. 10: dosljedno razlikovanje sile stijenke na fluid, fluida na element i reakcije nosača; usporedba β-varijanti
  pokazuje da tlačni članovi dominiraju; Z3 s težinom vode i Z4 s krakom (yC, a ne √(xC² + yC²)) hvataju stvarne pogreške.
- Pog. 11: „Granica modela” za Froudeovu hipotezu i ITTC liniju, brojčani P2 koji pokazuje zašto se Fr i Re ne mogu
  istodobno očuvati i zašto se viskozni dio ne skalira s λ³; Z6 s „zajamčenim granicama” koje nisu standardne nesigurnosti.
- Pog. 12: ispravno odvajanje konvergencije od validacije; primjer s ulaznim uvjetom RANS-a (izotropija i ℓ kao
  pretpostavke, ne mjerenja); Z4 s povratnim tokom i točnom tvrdnjom da je v(0) = 0 i unutar 0 < y < H/11 brzina negativna.
