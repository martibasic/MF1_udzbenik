# Provjera nalaza skupine G3 (pog. 9–12)

Provjera 8. 11. 2026. prema koraku 5 skilla `recenzija-prirucnika`. Ulaz su
izvještaji `struka.md` (S-A), `struka_drugi_model.md` (S-B, oznake S01–S28),
`primjena.md` (PR), `urednik.md` (UR) i `student_pog10.md` (ST). Svaki nalaz
P0–P2 provjeren je u izvoru `source/`. Skice su provjerene na renderu
`pog10.pdf` i `pog11.pdf` (sl. 10.1, 10.2, 10.4, 10.9 i 11.4), a ključ u `kljuc10.pdf`.
Račun je u `scratchpad/knjiga/prov_G3/racun_g3.py` i `racun_g3b.py`.
Nalazi na razini knjige (F.(N+1), udvojene stranice ključa i ostali s popisa) preskočeni su.

Oznake težine slijede `docs/konvencije_pisanja.md`. Vrste ispravka su TEKST,
BROJ/MODEL, SKICA i AUTORSKA ODLUKA. Stupac „Težina” je konačna težina; kad se
razlikuje od težine čitatelja, razlog je naveden u nalazu.

## Račun uz nalaze P1 i provjerene brojčane tvrdnje

| Mjesto | Provjereno | Moj račun |
| --- | --- | --- |
| pog. 10 Z5 (`u10:1025–1056`) | $\dot m_{rel}=\rho\frac{\pi d^2}{4}(v-u)$, $F_x=\dot m_{rel}(v-u)$, $P=F_xu$, $v_2=\sqrt{u^2+(v-u)^2}$, maksimum $u(v-u)^2$ | 15,049 kg/s; 180,59 N; 1444,75 W; 14,422 m/s; energijom 1444,75 W; $u^*=v/3=6{,}667$ m/s, $P_{max}=1486{,}4$ W. Ključ se slaže. Koraci 1–3 istovjetni su P1 (`u10:233–273`). Pitanje 5 odgovoreno je u P1 `u10:250`, a okomitu ploču P1 spominje u `u10:294`. |
| pog. 10 P1, kut (`u10:224`) | sila uz $\theta=165^\circ$ prema doslovnom čitanju „15° s dolaznim mlazom” | $\dot m_{rel}=35{,}27$ kg/s; $F_x(165^\circ)=1248{,}2$ N; $F_x$ uz izlaz pod 15° prema smjeru $+x$: $35{,}27\cdot18\cdot(1-\cos15^\circ)=21{,}6$ N. Skica i račun koriste 165°; tekst je dvosmislen. |
| pog. 10 P7 (`u10:857`) | „snaga mlazova $\dot m(w^2-u^2)/2\approx440$ W” | $w=17{,}825$ m/s; $u=1{,}571$ m/s; $\dot m=2{,}794$ kg/s. $\dot m(w^2-u^2)/2=440{,}5$ W; apsolutna kinetička snaga mlazova $\dot m(w-u)^2/2=369{,}2$ W; $M\omega=71{,}35$ W. Vrijedi $369{,}2+71{,}35=440{,}5$ W. Relativna snaga $\dot m w^2/2=444{,}0$ W. Dakle 440 W je snaga koju dovod predaje vodi u glavi (dovodni tlak $\rho(w^2-u^2)/2=1{,}573$ bar), a ne snaga mlazova. |
| pog. 10 Z3 (`u10:962–989`) | ključ i dio 3 | $v=2{,}865$ m/s; $p_{M2}=144{,}855$ kPa; $F_x=4969{,}7$ N; $F_z=-5101{,}8$ N; $|F|=7122{,}2$ N; težina/$|F_z|=5{,}76$ %. „Vodoravni” račun daje $F_z=-4969{,}7$ N, razlika je 132,1 N (2,66 %). |
| pog. 10 P3 β (`u10:452`) | $\beta=1;\,1{,}02;\,4/3$ i $\xi$ | (−1402,7; 665,0), (−1404,2; 668,6), (−1429,1; 724,6) N; gubitak 2661 Pa, $\xi=0{,}337$. |
| pog. 10 P5 (`u10:712`) | osjetljivost rezultante na $R_y$ | $R_y\pm5\,\%$ daje $R=867$–$959$ N; uz $\pm10\,\%$ rezerva od 87 N nestaje. Tvrdnja o „nesigurnosti mjerenja” nema podatka u zadatku. |
| pog. 10 Z1 (`u10:159`) | snaga u dva sustava | U sustavu broda $\dot m(v_j^2-v_s^2)/2=645{,}75$ kW. U sustavu obale $F_Tv_s+\dot m(v_j-v_s)^2/2=645{,}75$ kW. Izraz je točan, ali bez navedenog sustava zbunjuje. |
| pog. 11 P6 (`u11:668`) | $Re$ dimnjaka uz $\nu=1{,}5\cdot10^{-5}$ m²/s | $1{,}6\cdot10^6$ pri 12 m/s i $8{,}0\cdot10^5$ pri 6 m/s, dakle izvan „subkritičnog područja” iz `u11:107`. |
| pog. 12 P2 (`u12:163`) | prijedlog PR za realan film | $H=1$ mm uz $-100$ kPa/m i $H=50$ µm uz $-40$ MPa/m daju isti $v(H/2)=1{,}125$ m/s. |
| pog. 12 Z3 (`u12:589–617`) | podudarnost s P3 | $\mu=1{,}0002$ mPa s, $Re=12{,}70$, $s(\mu)/\mu=4{,}22\,\%$. Ulazi su isti kao u P3, gdje su $\mu$ i $Re=12{,}7$ već tiskani. |
| pog. 12 Z5 (`u12:651–677`) | Falkner–Skan | $m=-0{,}0667$, $\beta_{FS}=-0{,}143$, $m/m_{odv}=0{,}74$ (uz $m_{odv}\approx-0{,}0904$). |
| pog. 11 Z6 (`u11:919`) | red veličine sile | $b=Q/(vh)=10{,}67$ m, $\tfrac12\rho gh^2b=2{,}94$ MN prema 224 kN „nakon tariranja” (P3, S24). |

## Tablica nalaza P0–P2

Nalaza P0 nema; nijedan čitatelj nije prijavio P0, a provjera ga nije našla.

| ID | Mjesto | Nalaz | Izvor čitatelja | Težina | Status | Vrsta | Prijedlog ispravka |
| --- | --- | --- | --- | --- | --- | --- | --- |
| G3-01 | `u10:1025–1056` (Z5), uz `u10:219–295` (P1) | Z5 „Mlaz na ploču koja se udaljava” ponavlja P1 (pomični KV, $\dot m_{rel}$, $F_x$, $P=F_xu$, energijska provjera). Pitanje 5 odgovoreno je u `u10:250`. Jedini T3 u poglavlju ne traži izbor ni povezivanje modela (K15, raspodjela T1–T4). Novo je samo $u=v/3$. | S-A P1-1; S-B S13b (P3); ST (mjesto 2) | P1 | POTVRĐENO | AUTORSKA ODLUKA | Zamijeniti Z5 zadatkom sa stvarnom odlukom T3 (npr. kosa ploča s podjelom protoka iz bilance uz ploču) ili ga spustiti na T2 i T3 dodijeliti drugom mjestu. |
| G3-02 | `u10:857` (P7, Provjera) | „Snaga mlazova $\dot m(w^2-u^2)/2\approx440$ W” netočno imenuje veličinu. Mlazovi nose 369 W, a 440 W je snaga koju dovod predaje vodi (račun gore). Podignuto s P2 jer je riječ o netočnoj fizikalnoj tvrdnji (definicija P1). | S-A P2-8; S-B S09; ST (P3) | P1 | POTVRĐENO | TEKST | „Kočena snaga (71 W) mali je dio snage $\dot m(w^2-u^2)/2\approx440$ W koju dovod predaje vodi; ostatak, $\dot m(w-u)^2/2\approx369$ W, odnosi mlaz prema stijenci tanka.” |
| G3-03 | `u12:3` | „Njezin [NS] je najjednostavniji poseban slučaj zakon viskoznosti iz pog. 2”: Newtonov zakon je poseban slučaj konstitutivne veze `eq-newtonska-konstitutivna-relacija`, a ne jednadžbe gibanja. Izvod `u12:95` to kaže točno. Podignuto s P2 jer je tvrdnja netočna. | S-A P2-9; S-B S05 | P1 | POTVRĐENO | TEKST | „Za jednostavno smicanje konstitutivna veza koja ulazi u nju svodi se na zakon viskoznosti iz pog. 2.” |
| G3-04 | `u10:224` (P1) | „Relativna izlazna brzina zatvara kut od 15° s dolaznim mlazom” dvosmisleno je. Vektorski kut je 165°; doslovno čitanje daje 21,6 N umjesto 1248 N. Skica i račun su ispravni. | S-B S01 | P2 | POTVRĐENO | TEKST | „… zatvara kut od 15° sa smjerom suprotnim dolaznom mlazu.” |
| G3-05 | `u10:983–985` → D06 Z3 | Tiskani ključ odsijeca rečenicu „Račun u vodoravnoj ravnini dao bi $F_z\approx-4{,}97$ kN … oko 3 % veća”, pa zahtjev 3 nema kontrolni broj. Uzrok nije `\,\%`: `compact()` u `scripts/generate_exercise_key.py` skraćuje odgovor dulji od 500 znakova (ovaj ima 552) na kraj rečenice. U pog. 9–12 to je jedini takav odgovor. | S-A P2-1; ST | P2 | POTVRĐENO | TEKST | Odgovoru dodati `data-key-full="true"` (kao u `u12` Z6) i obnoviti D06 generatorom. |
| G3-06 | `u12:589–617` (Z3) prema `u12:237–257` (P3) | Z3 ima iste $D$, $L$, $Q$ i $\Delta p=652$ Pa kao P3. Traženi $\mu=1{,}0$ mPa s i $Re=12{,}7$ već su tiskani u P3; novo je samo širenje nesigurnosti. | S-A P2-2; S-B S04 | P2 | POTVRĐENO | BROJ/MODEL | Promijeniti fluid i podatke (npr. glikol, $\mu\approx10$ mPa s, novi $\Delta p$) uz istu strukturu nesigurnosti; verifikator, D06 i skica Z3 slijede. |
| G3-07 | `u09:540–567` (Z2, T1), `u09:599–625` (Z4, T2), `u09:271–299` (P4, T2) | Z2 je P4 s drugim brojevima i $t=m/\dot m$; Z4 ponavlja istu odluku $p_b/p_0$ prema 0,528 (dodaje nezagušeni slučaj). Z2 nosi nižu razinu od istovrsnog P4. | S-A P2-3; S-B S13a (P3) | P2 | POTVRĐENO | AUTORSKA ODLUKA | Zadržati Z4; Z2 promijeniti tako da mijenja vrstu razmišljanja (npr. kvazistacionarno pražnjenje boce do prestanka zagušenja). |
| G3-08 | `u11:661–711` (P6) prema `u09:108–133` (P2) | Prvi dio P6 pog. 11 ponavlja P2 pog. 9: vod $D=80$ mm, $Q\approx0{,}4$ m³/s, $Ma$ prema 0,3, granični protok. Kršenje K10. | S-A P2-4; S-B S02; PR P3-2 | P2 | POTVRĐENO | AUTORSKA ODLUKA | U pog. 11 Mach-dio zamijeniti pitanjem sličnosti (npr. $Re_m=Re_p$ u zraku i posljedični $Ma$) ili ga svesti na upućivanje na pog. 9. |
| G3-09 | `u12:306`, `u12:326–333` (P4) prema `u11:466–478` (P2) | Zahtjev 3 P4 pog. 12 doslovno ponavlja $C_{F,m}=2{,}96\cdot10^{-3}$, $C_{F,s}=1{,}48\cdot10^{-3}$ i zaključak o $\lambda_L^3$ iz pog. 11. Kršenje K10. | S-A P2-5 | P2 | POTVRĐENO | AUTORSKA ODLUKA | Zahtjev 3 zamijeniti upućivanjem na P2 pog. 11 i usporedbom laminarnog $C_F=1{,}328/\sqrt{Re_L}$ s turbulentnim (izmjena primjera traži proširenje opsega). |
| G3-10 | `u11:889–917` (Z5, T3), `u11:590–641` (P5), `u11:175–183`, `u11:224–253` | Buckinghamova analiza kugle provedena je triput (tumačenje matrice, izvod, P5). Z5 ponavlja postupak za $f$ uz zadane ponavljajuće varijable; T3 nema izbor modela (K15). Težina P2, ne P1: Z5 vježba obvezni ishod „puni Buckinghamov postupak” za novu zavisnu veličinu. | S-A P2-6; S-B S03; UR (K10) | P2 | POTVRĐENO | AUTORSKA ODLUKA | Z5 dati pravu odluku T3 (npr. student sam bira popis varijabli uz hrapavost ili blizinu stijenke); P5 skratiti upućivanjem na izvod. Spuštanje Z5 na T2 traži novi T3 u poglavlju. |
| G3-11 | `u11:668`, `u11:698–710`, `u11:107` | $St\approx0{,}2$ za dimnjak pri $Re=1{,}6\cdot10^6$ (8·10⁵ pri 6 m/s) proturječi ogradi „u određenom subkritičnom području” (K9). Tvrdnja o EN 1991-1-4 ($St\approx0{,}18$) nije provjerena. | S-A P2-7; S-B S07; PR P3-11 | P2 | POTVRĐENO (podatak o normi NEPOTVRDIV) | TEKST | U P6 izračunati $Re$ i navesti da je $St=0{,}2$ zadana projektna vrijednost, uz izvor ili oznaku nastavne procjene. |
| G3-12 | `u11:143–155` | Tablica bezdimenzijskih brojeva nema potpis ni ID, a upućuje se na nju opisno („Tablica sažima …”). Kršenje K12. | S-A P2-10; S-B S21b; UR | P2 | POTVRĐENO | TEKST | Dodati potpis i `{#tbl-…}` te upućivati brojem. |
| G3-13 | `u11:143` | Ručni `<span class="mf1-ch-ref">…dod. A…` u PDF-u daje „u pog. A Sažetak formula i oznaka” (`pog11.pdf`). Kršenje K1. Jedino takvo mjesto u izvorima. | S-A P2-11; UR | P2 | POTVRĐENO | TEKST | Pisati „u dodatku A” bez ručnog spana. |
| G3-14 | `u10:11` (sl. 10.1) | Oznaka „1” stoji iznad zavoja, daleko od ulaznog presjeka. Strelica $F_G$ polazi sa stijenke i izlazi iz cijevi (provjereno na renderu). | S-A P2-12; S-B S12 | P2 | POTVRĐENO | SKICA | „1” premjestiti uz isprekidani ulazni presjek, a hvatište $F_G$ staviti u fluid. |
| G3-15 | `u11:494` (sl. 11.4) | Oznake osi „50” i „0” preklapaju se; $p_v$ je na toj razini; natpisi prekrivaju krivulju; kota $D_2$ prelazi stijenku (provjereno na renderu). | S-A P2-13 | P2 | POTVRĐENO | SKICA | Ravnomjerna podjela osi, $p_v$ neposredno iznad 0, natpisi izvan krivulje. |
| G3-16 | `u11:764` (Z1), `u11:796` (Z2), `u11:860` (Z4), `u11:116–122` | $a$ je u Z1 širina kanala, a u istom poglavlju brzina zvuka ($a_m$ u Z4). $b$ ima tri značenja (visina, širina, raspon). Kršenje K6. | S-A P2-14 | P2 | POTVRĐENO | TEKST | U Z1 i na skici Z1 pisati npr. $s_1\times s_2$ ili $B\times H$; brojevi ostaju. |
| G3-17 | `u10:122–133`, `u11:300–304` | Granica modela u pog. 10 ima četiri natuknice i rečenicu, a u pog. 11 rečenicu od 58 riječi sa zagradom o $1+k$ (K11, K3). | S-A P2-15; UR (u11:303); S-B S20 | P2 | POTVRĐENO | TEKST | Natuknice pog. 10 premjestiti u tekst ispred bloka (student ih ističe kao korisne) i blok svesti na 2–3 rečenice; zagradu o $1+k$ prenijeti u tekst iza `eq-ittc-1957`. |
| G3-18 | `u12:683–706`, `u12:747`; `u12:683` | Kratica GCI ne definira se u pog. 12 niti se upućuje na dodatak D, gdje je definirana (`d04:34`, `d04:146`). Vidljivi tekst sadrži put `data/cfd/poiseuille_laminar` (K1, K5). | S-A P2-17, P3-7; S-B S08 (a, b); UR | P2 | POTVRĐENO | TEKST | Pri prvom spomenu „indeks mrežne konvergencije (engl. *grid convergence index*, GCI; dodatak D)”; put zamijeniti s „(dodatak D)”. |
| G3-19 | `u12:264`, `u12:527`, `u12:625` | $\tau_{st}=\mu\,\partial v_x/\partial y|_{st}$ bez tijela; napomena Z2 kaže „stijenke na fluid”, a Z4 definira $\tau_0$ kao silu fluida na ploču. Rezultati nisu pogrešni jer Z2 rabi iznos. | S-B S06 | P2 | POTVRĐENO | TEKST | Uz `u12:264` jednom navesti tijelo i predznak („fluid na stijenku”) i uskladiti napomenu Z2. |
| G3-20 | `u10:712` (P5) | „Rezerva od 87 N (oko 9 %) usporediva je s nesigurnošću mjerenja sile”, a zadatak ne daje nesigurnost $R_y$ (K9). | S-B S10 | P2 | POTVRĐENO | TEKST | Napisati „mogla bi biti usporediva s nesigurnošću mjerenja, koja ovdje nije zadana” ili zadati $s(R_y)$. |
| G3-21 | `u11:91` | Prag $We\approx12$ pripisan je [@white2011]. Ne može se provjeriti da White navodi tu vrijednost (K14). | S-B S11; S-A P3-2 | P2 | NEPOTVRDIVO | TEKST | Autorica provjerava stranicu u Whiteu; ako je nema, navesti specijalizirani izvor u dodatku E ili označiti nastavnu orijentaciju. |
| G3-22 | `u10:797` (P7) | Brodski stroj za pranje tanka po PR radi pri 8–12 bar i sporo se vrti uz pogon turbinicom. Primjer daje oko 1,6 bar (potvrđeno: 1,573 bar) i reakcijski pogon (K16). Tvrdnja o praksi je „po sjećanju”. | PR P2-1 | P2 | NEPOTVRDIVO (račun tlaka POTVRĐEN) | AUTORSKA ODLUKA | Preimenovati u „Reakcijska glava za ispiranje spremnika” ili, uz izvor, povećati $w$ i dodati rečenicu o stvarnom stroju. |
| G3-23 | `u10:7` | Uvod najavljuje „koljena i račve u brodskim strojarnicama”, a nijedan primjer ni zadatak s koljenom ili račvom nema brodski smještaj (K16). | PR P2-2 | P2 | POTVRĐENO | TEKST | Uvod preformulirati („cijevni elementi brodskih i kopnenih sustava”) ili jednom primjeru dati brodski smještaj. |
| G3-24 | `u12:163–179` (P2), `u12:7` | $H=1$ mm i $-100$ kPa/m po PR nisu vjerodostojni za nosivi film kliznog ležaja (raspon 10–100 µm je „po sjećanju”). Zamjenski podatci daju isti rezultat (potvrđeno). | PR P2-3 | P2 | NEPOTVRDIVO | AUTORSKA ODLUKA | Ili iz P2 i uvoda ukloniti vezu s nosivim filmom ležaja („ulje u procjepu”), ili uz izvor uzeti $H=50$ µm i $-40$ MPa/m. |
| G3-25 | `u10:159` | „Ukupna kinetička snaga predana vodi $\dot m(v_j^2-v_s^2)/2$” ne navodi sustav. U sustavu obale student dobije $\dot m(v_j-v_s)^2/2$ (račun gore). | ST (P2) | P2 | POTVRĐENO | TEKST | Dodati „u sustavu broda (snaga pogona); u sustavu obale to je $F_Tv_s+\dot m(v_j-v_s)^2/2$”. |
| G3-26 | `u10:1064` (Z6) | Kratica „RSS” nije uvedena u pog. 10 (K5). | UR; ST (P2) | P2 | POTVRĐENO | TEKST | „To nisu standardne nesigurnosti, pa se ne zbrajaju korijenom zbroja kvadrata.” |
| G3-27 | `u09:3`, `u09:5`, `u09:7`, `u09:17` → `u09:106`, `u09:132`, `u09:460` | Uvod ponavlja rečenice iz tijela: „$Ma<0{,}3$ … heuristika”, pretpostavke modela (gotovo jednako Granici modela), „4,4 %” dvaput (K10). | UR | P2 | POTVRĐENO | TEKST | Uvod neka pojave samo imenuje; ukloniti rečenicu o pretpostavkama (`u09:7`) i drugi „4,4 %” (`u09:132`). |
| G3-28 | `u09:106`, `u09:362` | „kaloričkoga savršenog plina”: prema nazivlju „kalorički savršen plin” (K7). | UR | P2 | POTVRĐENO | TEKST | „kalorički savršenog plina”. |
| G3-29 | `u09:137`, `u09:139` | „Ranije obrađenoga kruga s kapljevinom” i „Venturijevoj cijevi s vodom” bez broja poglavlja (K12). | UR; S-A P3-14; S-B S27; PR P3-3 | P2 | POTVRĐENO | TEKST | Uputiti s `mf1-chapter-ref` na pog. 7 i pog. 8. |
| G3-30 | `u09:445` | „iteracija, koja nadilazi ispitnu razinu” nejasno je. | UR | P2 | POTVRĐENO | TEKST | „iteracija, zahtjevnija od razine ovog primjera, …” (autorica potvrđuje značenje). |
| G3-31 | `u10:1`, `u10:3`, `u10:5`, `u10:27`, `u10:36` → `u10:77–86` | Uvod daje cijelu jednadžbu s definicijama koju `u10:77–86` ponovno uvodi; treći Newtonov zakon spominje se triput (K10). | UR | P2 | POTVRĐENO | TEKST | U uvodu jednadžbu opisati riječima i uputiti na nju brojem; ukloniti ponovljenu rečenicu u okviru `u10:27`. |
| G3-32 | `u10:74` | „No taj oblik nije dovoljan” stoji iza okvira o $\beta$, pa referent nije jasan (K12). | UR | P2 | POTVRĐENO | TEKST | „No oblik iz jednadžbe [-@eq-momentum-numericki-trag-01] nije dovoljan …” |
| G3-33 | `u10:452` | Upućivanje naslovom odjeljka („u odjeljku Provjera sile na cijevno koljeno”), u PDF-u bez broja; imperativ „usporedi” u rješenju (K12, K2). | UR | P2 | POTVRĐENO | TEKST | Odjeljku `u10:91` dodati ID i uputiti brojem, u prvom licu množine. |
| G3-34 | `u10:708` | „proračunati režim”, prema K7 (izračunan-) „proračunani”. | UR | P2 | POTVRĐENO | TEKST | „proračunani režim”. |
| G3-35 | `u10:1093`, `u10:1095` (sl. 10.9, Z3) | Na izlazu 2 nacrtana je neoznačena tlačna strelica prema dolje, uz oznaku $v_2$ smještenu između dviju strelica. Napomena kaže „izlazni tlak nije nacrtan” (provjereno na renderu). Strelica $g$ zadire u kotu $\Delta z$. Podignuto s P3 jer napomena i skica proturječe. | S-B S17 (P3); ST (P3) | P2 | POTVRĐENO | SKICA | Strelicu označiti $p_{M2}A_2$ (i ispraviti napomenu) ili je ukloniti; $v_2$ odmaknuti uz svoju strelicu, $g$ odmaknuti od kote. |
| G3-36 | `u11:15`, `u12:15` | Naslov prvog odjeljka jednak je naslovu poglavlja (K4); u pog. 11 slijedi jednorečenično „Fizikalno značenje” (`u11:42`) koje ponavlja uvod. | UR; S-A P3-9; S-B S21a | P2 | POTVRĐENO | TEKST | Npr. „Svrha bezdimenzijskog opisa” i „Od integralne do lokalne bilance”; ID-jevi ostaju. |
| G3-37 | `u11:3`, `u11:5`, `u11:42`, `u11:131`, `u11:267` | Uvod definira osam brojeva i $n-k$, koji se zatim ponovno uvode; „jedna grupa nije dovoljna” i nespojivost $Fr$–$Re$ stoje na više mjesta (K10). | UR | P2 | POTVRĐENO | TEKST | Uvod neka brojeve samo imenuje; ponavljanja zadržati na jednom mjestu. |
| G3-38 | `u11:34`, `u11:47` prema `u11:275` | $F_p$ je mjerilo tlačne sile i sila prototipa (K6). | UR | P2 | POTVRĐENO | TEKST | Mjerilo tlačne sile pisati $F_{\Delta p}$. |
| G3-39 | `u11:107` | „subkritičnom području”; potvrđeno nazivlje je potkritični/natkritični (K7). | UR | P2 | POTVRĐENO | TEKST | „potkritičnom području Reynoldsova broja” (rješava se zajedno s G3-11). |
| G3-40 | `u11:122` | „$K$ modul stlačivosti”, prema uredničkom stilu „volumni modul”. | UR | P2 | POTVRĐENO | TEKST | „$K$ volumni modul”. |
| G3-41 | `u11:286` (prvi spomen), `u11:303`, `u11:434`, `u11:971`, `u12:306` | ITTC nije raspisan u poglavlju ni u pojmovniku, nego samo u literaturi (K5). | UR; S-A P3-8; S-B S23 | P2 | POTVRĐENO | TEKST | Pri prvom spomenu „Međunarodna konferencija pokusnih bazena (engl. *International Towing Tank Conference*, ITTC)”. |
| G3-42 | `u11:541` | „NPSH” jedanput u poglavlju i prije pog. 13 (K5). | UR; S-A P3-8; S-B S23 | P2 | POTVRĐENO | TEKST | „kavitacijska rezerva ($NPSH$, pog. 13)”. |
| G3-43 | `u11:796` | Rečenica od 44 riječi s nizom definicija (K3; potvrđeno alatom). | UR | P2 | POTVRĐENO | TEKST | Podijeliti na jednadžbu i rečenicu s definicijama simbola. |
| G3-44 | `u12:3`, `u12:7` → `u12:24`, `u12:114`, `u12:225`, `u12:276` | Uvod donosi materijalnu derivaciju i NS jednadžbu (u tekstu, ne istaknuto, kako tvrdi UR), a pretpostavke analitičkih rješenja ponavljaju se na tri mjesta (K10). | UR | P2 | POTVRĐENO (opis djelomično netočan) | TEKST | Uvod neka jednadžbe imenuje; u `u12:7` ostaviti samo opću rečenicu o pretpostavkama. |
| G3-45 | `u12:139` | Rečenica od 47 riječi (K3; potvrđeno alatom). | UR | P2 | POTVRĐENO | TEKST | Podijeliti na tri rečenice prema prijedlogu UR. |
| G3-46 | `u12:366` | Kratica RANS stoji uz Reynoldsovo naprezanje, a ne uz jednadžbe; rečenica o $k$–$\varepsilon$ i $k$–$\omega$ SST ima 45 riječi (K5, K3). | UR | P2 | POTVRĐENO | TEKST | RANS pridružiti osrednjenim jednadžbama; rečenicu o modelima podijeliti. |
| G3-47 | `u12:368` | „$Re$ iz prethodnog poglavlja” bez broja (K12; potvrđeno alatom). | UR | P2 | POTVRĐENO | TEKST | Uputiti na pog. 11 s `mf1-chapter-ref`. |
| G3-48 | `u12:631` | $\tau_0=\mu v'(0)$: crtica je u `u12:346` oznaka fluktuacije (K6). | UR | P2 | POTVRĐENO | TEKST | $\tau_0=\mu\,(dv/dy)_{y=0}$. |
| G3-49 | `u10:95` | „Usporedba oštrog i blažeg koljena … pokazuje” zvuči kao rezultat provedene simulacije. Zaključak ipak slijedi iz bilance (manji gubitak daje viši $p_{M2}$ i veću tlačnu silu na izlazu), a brojeva nema. Spušteno na P3. | S-A P2-16; PR P3-6 | P3 | POTVRĐENO | TEKST | „… može pokazati …” ili „Bilanca pokazuje …”. |
| G3-50 | `u10:1062`, `u10:1070`, `u11:945` | „nominalni” uz $R_{naz}$; nije pravilo uredničkog stila, nego dosljednost. Spušteno na P3. | UR | P3 | POTVRĐENO | TEKST | Po želji „nazivni”. |
| G3-51 | `u12:270` prema `u12:315`, `u12:659`, `u12:673` | $\delta_{99}$ u teoriji, $\delta_B$ u P4 i Z5. U Z5 razlika je namjerna jer je $\delta_B$ samo referenca, a ne stvarni $\delta_{99}$. Spušteno na P3. | UR | P3 | POTVRĐENO | TEKST | Pri prvom spomenu napisati „$\delta_B$ (Blasiusova procjena $\delta_{99}$)”. |
| G3-52 | `u11:826` (Z3) | Brzine 4 i 8 m/s na „referentnom presjeku usisa crpke” veće su od uobičajenih brzina u usisnom vodu (1–3 m/s, „po sjećanju”). Presjek može biti ulaz u radno kolo; kriterij je izrijekom nastavni. Spušteno na P3. | PR P2-4; S-A P3-11 | P3 | NEPOTVRDIVO | TEKST | Napisati da je presjek suženi ulaz u radno kolo; podatci ostaju. |
| G3-53 | pog. 9–12 | Ravnoteža struka: u pog. 12 Z1–Z6 nema pomorskog primjera, u pog. 9 samo Z2; offshore i dekarbonizacija izostaju. Opis je točan, ali ugovor i matrica (lajtmotivi pog. 9–12) to ne traže. Spušteno na P3. | PR P2-5 | P3 | POTVRĐENO | AUTORSKA ODLUKA | Banka zamjena konteksta iz PR P2-5, bez obveze. |
| G3-54 | `u12:617` (S04, dio) | Prijedlog da se Z3 pog. 12 podigne na T3/T4 jer sadrži nesigurnost. | S-B S04 | — | ODBAČENO | — | Ne provoditi. Širenje nesigurnosti po zadanoj formuli nije odluka T4 (protokol §3; AGENTS: ne povisuj oznaku radi kvote). Pog. 12 već ima T4 (Z6), pa bi raspodjela 2×T1, 2×T2, T3, T4 bila narušena. Ponavljanje se rješava pod G3-06. |

Napomene uz tablicu:

- Prijedlozi koji mijenjaju riješene primjere (G3-08, G3-09, G3-10 u dijelu P5,
  G3-22, G3-24) izvan su dogovorenog opsega revizije Z1–Z6 iz AGENTS.md i traže
  da autorica proširi opseg.
- Uz G3-01 i G3-10 vrijedi isto ograničenje: spuštanje razine traži novo mjesto
  T3 u istom poglavlju.
- Pretpostavka S-A da je rez ključa nastao na `\,\%` netočna je; uzrok je naveden
  pod G3-05.

## Brojčani pregled

| Status | P1 | P2 | P3 (spušteno) | Ukupno |
| --- | ---: | ---: | ---: | ---: |
| POTVRĐENO | 3 | 42 | 4 | 49 |
| NEPOTVRDIVO | 0 | 3 | 1 | 4 |
| ODBAČENO | — | — | — | 1 |

Nalazi G3-11 i G3-22 potvrđeni su u računskom dijelu, a nepotvrdivi u dijelu
o praksi. Prvi se broji kao potvrđen, a drugi kao nepotvrdiv. P0 nema.

## Što je dobro

- Brojevi se mogu ponoviti. Provjereni su P1, P3, P5 i P7 te Z1, Z3 i Z5 u pog. 10,
  P2 u pog. 9, P6 ($Re$) u pog. 11 te P2, P3, Z3 i Z5 u pog. 12, svi bez odstupanja
  većeg od zaokruživanja. To se slaže s oba stručna čitanja.
- Pog. 10 dosljedno razlikuje $\vec R_{st\to f}$, $\vec F$ i $\vec R$ i uz skice
  navodi tijelo na koje sila djeluje. Simulirani student to ističe kao najveću pomoć.
- Pog. 9 dosljedno inzistira na apsolutnom tlaku i pokazuje posljedicu pogreške.
  P6 sa sva tri režima sapnice i položajem vala pri 350 kPa točan je.
- Zadatci T4 (Z6 u svim četirima poglavljima) traže odluku na granicama intervala
  i razlikuju zajamčene granice od standardnih nesigurnosti.
- CFD odlomci ne iznose neprovedene brojčane rezultate. Pog. 12 razdvaja mrežnu
  konvergenciju od validacije na stvarnim podatcima (Driver–Seegmiller) s izvorom.
- Lanac pog. 11 P2 → pog. 12 P4 (vučni bazen, ITTC 1957, stimulator) primjenski je
  dobar. Treba samo ukloniti ponovljeni račun (G3-09).

## Sažetak P3 (prebrojeno, nije pojedinačno provjeravano)

Ukupno oko 75 nalaza P3 iz pet čitanja, uz pet nalaza spuštenih iz P2 (G3-49 do G3-53).

| Skupina | Približno | Glavna mjesta |
| --- | ---: | --- |
| Čitljivost skica i prijelom (K13) | 15 | sl. 10.2 ($F_x$ prekriven), 10.7, 10.9 (Z1, Z5, Z6), 11.5, 11.7, 12.2 (Z4; slika razdvojena na dvije stranice), 9.2 (Z5); alternativni opis jednak potpisu `u11:11`, `u11:436`. |
| Naputak rješava ili „Traži se” otkriva zaključak (K15) | 6 | `u09:586`, `u09:676`, `u10:916`, `u12:606`, `u12:660`, `u12:697`. |
| Razine i redoslijed primjera (K15) | 8 | pog. 11 Z2 i P4, pog. 12 Z2, P6 i Z1 (= P1 + $\partial v/\partial t$), pog. 10 P6 iza P5; težina pog. 12 Z6 b). |
| Kratice i pojmovi (K5) | 12 | KV prije definicije (`u10:9`), VL, CFL, FVM, FEM, DNS, TMR, CFL3D, FUN3D, OpenFOAM. |
| Izvori i iskustveni pragovi (K14, K9) | 10 | $\xi\approx0{,}34$ „uobičajeno”, prijelaz $3\cdot10^5$–$3\cdot10^6$, kriza otpora, $\ell\approx0{,}07D$, 10–20 m/s, „uvijek” za $p_{02}<p_{01}$ (`u09:370`). |
| Primjenska vjerodostojnost (K16) | 12 | uputni zrak, usis turbopuhala, sigurnosni ventil (norma), vodeni udar uz sidreni blok, $\nu$ morske vode, automobil pri $Re_m=Re_p$, hidroprofil bez uređaja, preljev 224 kN prema 2,94 MN, račve bez gubitaka. |
| Fizikalne formulacije i preskočeni koraci | 9 | $\alpha\ge\beta^{3/2}$ (`u10:71`), „krakovi … suprotno” (`u10:207`), moment rotora na fluid (`u10:202`), $Bo$ za kap u struji, koraci aktuatorskog diska, manometarski tlak prije obrazloženja, $\tau(H)$ uz P2 pog. 12. |
| Nazivlje (K7) | 25 | „koeficijent protoka” prema „koeficijent istjecanja” (`u09:627`), sapnica/mlaznica, „servisno koljeno”, „aksijalne”, „trenutna”, -oga/-og (oko 20). |
| Brojevi i interpunkcija (K8) | 31 | grupiranje tisućica (oko 12), formule bez završnog znaka (oko 10), em-crtica u prozi (oko 9). |
| Glas, upućivanja i struktura (K2, K12, K4) | 25 | miješanje glasa (8), opisna upućivanja (5), upitni podebljani uvodi CFD-a (6), pretinci „Riješeni primjeri”, redoslijed napomena Z1, Z3, Z2…, Z6 pog. 12 spaja dva problema, $\Pi$ kao broj. |

## Ograničenja

Didaktička procjena (G3-01, G3-06 do G3-10) autorska je procjena provjeritelja i
čitatelja, a ne dokaz; potvrditi je može studentski pilot. Tvrdnje o praksi
označene kao NEPOTVRDIVO traže izvor iz dodatka E. Verifikatori nisu pokretani
jer nijedan potvrđeni nalaz ne mijenja objavljeni rezultat. G3-06 i eventualna
zamjena G3-01 promijenit će verifikator, manifest i D06.
