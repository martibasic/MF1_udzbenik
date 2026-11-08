# Provjera nalaza G2 (pog. 5–8)

Provjera prema koraku 5 skilla `recenzija-prirucnika`, 8. 11. 2026. Ulaz: `struka.md` (S),
`primjena.md` (A), `urednik.md` (U), `student_pog08.md` (St). Svaki nalaz P0–P2 otvoren je u
`source/` na navedenom retku (stanje grane `konvencije-recenzije`, izvori pog. 5–8 nepromijenjeni
od `9d343b3`). Računi su u `…/scratchpad/knjiga/prov_G2/racun.py`. Skice su pregledane na
renderu `pog05.pdf` str. 18–19 i `pog08.pdf` str. 12 i 18. Preskočeni su poznati nalazi na razini
knjige: F.(N+1), ponovljene stranice ključa, „primjer N.M”, skriveni „Provjeri sebe”, nazivi
bilježnica. Upućivanje „odjeljak D.7” (St) artefakt je izdvojenog PDF-a.

Oznake: težina je konačna; „izmjereno” = vlastiti račun ili render, „provjereno” = tekst
potvrđen u izvoru, „dojam” = procjena bez izvora.

## Tablica nalaza

| ID | Mjesto | Nalaz | Izvor | Težina | Status | Vrsta | Prijedlog ispravka |
| --- | --- | --- | --- | --- | --- | --- | --- |
| G2-01 | `u06:338` (Dublje, str. 116); verifikator `verify_u07.py:570–574` | „Napola pun” tank „pri istoj istisnini” daje $GM$ 4,23 → 4,16 m. Takvo stanje ne postoji: napola pun tank ima upola manje vode i niže težište. Stvarno napola puno stanje daje $GM_{ef}=4{,}26$ m, više od punoga (4,23 m). Usporedba ima pogrešan smjer, a verifikator ponavlja istu pretpostavku ($V_{ist}$ punoga tanka). Izmjereno. | S P1-1 | **P1** | POTVRĐENO | BROJ/MODEL | Izračunati stvarno napola puno stanje ($GM$ 4,33 kruto → 4,26 m) i reći da niži teret podiže $GM$, a slobodna površina dio toga poništava; ukloniti „pri istoj istisnini” i uskladiti `U07.CH2.free_surface_*`. |
| G2-02 | `u05:901` (Sažetak); `u05:134` | „Ista sila na nagnutoj plohi znači samo jednaku površinu i jednaku dubinu težišta” može se čitati kao nužan uvjet, a to je netočno: mjerodavan je umnožak $Ah_C$. Namjeravano čitanje (dovoljan uvjet, sila ne ovisi o nagibu) točno je. Isto vrijedi za r. 134. Izmjereno (protuprimjer ispod). | U | P2 (U: P1 za r. 901) | POTVRĐENO, težina snižena | TEKST | „Sila $F=\rho gAh_C$ ne ovisi o nagibu: plohe jednake površine i dubine težišta nose jednaku silu, ali centar tlaka ovisi o nagibu.” Isto u r. 134. |
| G2-03 | `u05:231` (P2, kosi poklopac), `u05:589` (P6, zglobni poklopac) | Gustoća vode nije zadana; rezultati koriste 998 kg/m³, a opća napomena stoji tek u r. 688 i vrijedi samo za zadatke. S 1000 kg/m³: 13,98 kN umjesto 13,95 kN i 8,309 kN umjesto 8,292 kN. Izmjereno. | S P2-1 | P2 | POTVRĐENO | TEKST | Dodati „gustoće $\rho=998\ \mathrm{kg/m^3}$” u oba teksta zadatka. |
| G2-04 | `u05:698`, naputak `u05:708` (Z1) | Raspodjela opterećenja između gornjeg i donjeg zasuna statički je neodređena, jer su šarke duž cijelog ruba. Brojevi 7,94/6,22 kN vrijede uz pretpostavku da se opterećenje prenosi vodoravnim trakama. Ta pretpostavka stoji samo u naputku, koji se u PDF-u ne prikazuje (`when-format="html"`). Izmjereno: $F=28{,}32$ kN, $h_{CP}=2{,}297$ m. | S P2-2 | P2 | POTVRĐENO | TEKST (razina: AUTORSKA ODLUKA) | U tekst dodati „Vrata nose opterećenje kao niz vodoravnih traka oslonjenih na šarke i zasune”; autorica odlučuje ostaje li T1. |
| G2-05 | pog. 5 u cjelini; `u05:7` | Izričit brodski kontekst ima samo Z1. Strojarskoga gotovo nema: primjeri su ustave, kanali i bazen, uz spremnik s plinom. Uvod i matrica („poplavna vrata i brodski otvor”) najavljuju više. Provjereno. | A P2-6 | P2 | POTVRĐENO | AUTORSKA ODLUKA | Bez promjene fizike dati brodski ili strojarski kontekst barem jednom primjeru, npr. P5 kao teretni tank pod inertnim plinom (izvan dogovorenog opsega revizije Z1–Z6 za primjere). |
| G2-06 | `u05:3`, `u05:5` prema `u05:22`, `u05:343` | Uvod iznosi $F$, $h_{CP}$, tri izraza za $I_G$ i komponente zakrivljene plohe prije izvoda; rečenice o ravnoj i zakrivljenoj plohi ponavljaju se u r. 22. Provjereno. | U | P2 | POTVRĐENO | TEKST | Uvod skratiti na po jednu rečenicu s upućivanjem na jednadžbe; $I_G$ kruga premjestiti uz izvod centra tlaka. |
| G2-07 | `u05:170`, `u05:581` | K12: „iz prethodnog poglavlja” i „kako je najavljeno u odjeljku o referentnom tlaku”. Provjereno (r. 170 i alat). | U | P2 | POTVRĐENO | TEKST | Zamijeniti s []{.mf1-chapter-ref target="u04"} i upućivanjem na jednadžbu referentnog tlaka. |
| G2-08 | `u05:441`, `u05:865`, `u07:750`, `u07:837`, `u07:844`, `u08:75` | K2: u istom bloku miješa se 1. l. mn. s 2. l. jd., a u tekstu zadatka stoji 1. l. mn. („označujemo”, „orijentiramo”, „zanemarujemo”, „zaustavimo”, „Provjeri … odvoji” u bloku s „pretpostavljamo”). Provjereno. | U | P2 | POTVRĐENO | TEKST | Ujednačiti glas prema prijedlozima urednika. |
| G2-09 | `u06:60–96` (P1, kućište crpke) | $V_{ist}=0{,}045$ m³ uz 85 kg vrijedi samo za zatvoreno kućište; otvoreno bi se napunilo (lijevano željezo ≈ 0,012 m³). Hermetičnost se spominje tek u provjeri. Naslov kaže „potonulo”, a tekst „bez dodira s dnom”. Izmjereno i provjereno. | A P2-4, U (`u06:60`) | P2 | POTVRĐENO | TEKST | U tekst dodati „zatvoreno slijepim prirubnicama (hermetično)”, a u naslovu „potonulo” zamijeniti s „uronjeno” (ID ostaje). |
| G2-10 | `u06:19`/`u06:51`; `u07:142`/`u07:245`; `u08:20`/`u08:148` | Ista jednadžba numerirana je dvaput: $F_U=\rho gV_{ist}$, bilanca mase i Bernoullijev oblik u metrima. Provjereno. | U | P2 | POTVRĐENO | TEKST | Jedno pojavljivanje ostaviti bez broja i uputiti na drugo; prije uklanjanja ID-ja provjeriti poveznice generatorom. |
| G2-11 | `u06:3`/`u06:143`; `u06:5`, `u06:115`, `u06:262` | K10: poništavanje atmosferskog tlaka navedeno je dvaput, a uvjeti $GM>0$, $=0$, $<0$ triput. Provjereno. | U | P2 | POTVRĐENO | TEKST | Zadržati r. 143 i 262; r. 3 i 115 skratiti uz upućivanje na jednadžbu. |
| G2-12 | `u06:28`; `u06:266`; `u06:279`, `u07:53`, `u07:313`, `u07:666`, `u08:230` | K4: naslov-pretinac „## Matematički izvod”; labela Granice modela u obliku pitanja; pet vodećih redaka CFD blokova u obliku pitanja, dok ostali CFD blokovi imaju izjavne. Provjereno. | U | P2 | POTVRĐENO | TEKST | Izjavni oblici prema tablici urednika; ID-jevi ostaju. |
| G2-13 | `u06:113`, `u06:234`, `u06:324`, `u07:9`, `u08:220`, `u08:225` | K3: rečenice od 41 do 61 riječi, s nizovima spojenima dvotočkom ili točkom-zarezom; u r. 324 kriteriji IS Codea u jednoj rečenici. Izmjereno (`prirucnik_stats --nalazi`). | U | P2 | POTVRĐENO | TEKST | Podijeliti prema prijedlozima urednika; r. 324 kao popis sa šest natuknica i nepromijenjenim brojevima. |
| G2-14 | `u06:265–275` (Granica modela, `eq-poluga-okomiti-bokovi`) | K11: Granica modela uvodi novu jednadžbu, koju dva primjera rabe kao neovisnu kontrolu. Brojevi su točni: 0,88 % pri 6,84°, 0,47 % pri 5°, za Z3 0,38 %, za Z6 0,46 %. Granica 5° za Z3 i Z6 opravdana je, ali argument je izveden na drugoj platformi. Izmjereno. | S P2-5; U P3-3 | P2 | POTVRĐENO | TEKST | Izvod premjestiti u izvod „Krivulja stabiliteta”, a u Granici ostaviti mjeru $\tfrac12(BM/GM)\tan^2\varphi$ u 1–3 rečenice. |
| G2-15 | `u06:486` (P4), `u06:640` (P5) | Oznaka T4 na riješenim primjerima nije opravdana: model je zadan („Primijeni …”), a nema podataka s nesigurnošću ni odluke među alternativama. Prema protokolu (odj. 3) to je T3. Provjereno. | S P2-6 | P2 | POTVRĐENO | AUTORSKA ODLUKA | Označiti T3 ili uvesti stvarnu T4 odluku (npr. izbor metode dodane težine ili izgubljenog uzgona). |
| G2-16 | pog. 6 Z6 (`u06:1036`), pog. 7 Z6 (`u07:864`), pog. 8 Z6 (`u08:810–825`) | Tri uzastopna T4 jesu postupak riješenog primjera i omotač rubnih kombinacija. Tekst pog. 8 Z6 daje gotove bilance s $\zeta$, a naputak ih ponavlja, pa model student ne postavlja sam. Brojevi su točni: pog. 7 $h=1{,}614$ m, 890 s; pog. 8 $Q\in[14{,}69;17{,}38]$ L/s, $p_C\in[59{,}12;70{,}78]$ kPa. Izmjereno. | S P2-7; U (`u08:812/825`); St (Z6) | P2 | POTVRĐENO | AUTORSKA ODLUKA | Zadržati jedan omotač intervala u skupini, a u ostalim T4 tražiti drugu vrstu odluke; iz teksta pog. 8 Z6 ukloniti gotove formule ili ih izričito proglasiti zadanim modelom. |
| G2-17 | `u06:786–845` (P6, spar) | Nedosljednosti: (a) „čvrsti balast u dnu”, a −5 % mase pripisuje se „ispuštanju balasta”; (b) „bez balasta … $KG=45$ m” računa se uz istu masu 9000 t i isti gaz, pa to nije sustav bez balasta, a težište je i dalje 32,6 m ispod vodne linije; (c) „(spar)” bez „engl.” (K5); (d) „gaz oko 78 m odgovara izvedenim osnovama” bez izvora (K14). Izmjereno: $T=77{,}64$ m, $BM=0{,}116$ m. | A P2-5; S P3-6; U (`u06:790`) | P2 | POTVRĐENO | TEKST | Balast opisati kao čvrsti i vodeni; usporedbu pisati kao „isti balast smješten 13 m više”; uvesti „(engl. *spar*)”; dodati izvor iz dodatka E ili oznaku „nastavna procjena”. |
| G2-18 | `u06:927`, `u06:933`, `u06:940` (Z2) | K6/K7: relativna gustoća označena je sa $s$ umjesto $s_r$ (urednički stil), a piše „uvjet stabilnosti” uz dosljedno „stabilitet” u ostatku poglavlja. Provjereno. | U; S P3-9; A P3-9 | P2 | POTVRĐENO | TEKST | $s_r=\rho_d/\rho$ u tekstu, naputku i ključu; „uvjet stabiliteta”. |
| G2-19 | `u06:176`, `u06:782` | K12: „obrađena je u okviru o granici modela” i „(vidi blok „Učinak slobodne površine u tanku”)”. Provjereno. | U | P2 | POTVRĐENO | TEKST | Uputiti na `[-@eq-poluga-okomiti-bokovi]` i `[-@eq-ucinak-slobodne-povrsine]`. |
| G2-20 | `u07:66` | „Nestacionarno strujanje javlja se pri pokretanju … crpke, zatvaranju ventila te pri punjenju i pražnjenju spremnika, kada … $dm_{KV}/dt$ nije jednak nuli.” U krutoj cijevi s nestlačivom tekućinom strujanje je nestacionarno, a $dm_{KV}/dt=0$. Provjereno. | S P2-3 | P2 | POTVRĐENO | TEKST | Razdvojiti nestacionarnost od akumulacije u dvije rečenice prema prijedlogu S. |
| G2-21 | `u07:329`, `u07:554`, `u07:601` (P2, P4, P5) | Tri riješena primjera T2 traže istu odluku: $Q=vA$ uz zadanu podjelu. Materijalna derivacija nema brojčani primjer, iako ga poglavlje proglašava ključem za suženje. Provjereno. | S P2-8 | P2 | POTVRĐENO | AUTORSKA ODLUKA | Jedan od primjera T-komada ili rashladnog kruga zamijeniti kratkim primjerom $a_x=v\,dv/dx$ u suženju (izvan dogovorenog opsega Z1–Z6). |
| G2-22 | `u07:211`, `u07:444` | Član relativnog toka „presudan za pokretne lopatice u pog. 14” preskače pog. 10. Ondje `u10:151` izrijekom kaže „Taj se model, uveden u pog. 7, ovdje primjenjuje”, a Peltonova lopatica dolazi u `u10:220`. Provjereno. | S P2-9 | P2 | POTVRĐENO | TEKST | „za pokretnu lopaticu i mlaz u pog. 10 te radno kolo u pog. 14”. |
| G2-23 | `u07:382–445` (P3, sl. 7.3); `u08:431`, `u08:502` (P4, sl. 8.5) | Isti rashladni sustav prikazan je dvama uređajima. U pog. 7 je „zahvatni usis … okrenut prema pramcu” na dnu trupa, u pog. 8 usisni koš u boku. Rečenica u r. 502 ih izjednačuje. Nedosljednost je provjerena. Tvrdnja da je usisni koš u ravnini oplate uobičajeno rješenje, a zahvatnik rijedak, nije potkrijepljena izvorom. | A P2-1 | P2 | POTVRĐENO (nedosljednost); praksa NEPOTVRDIVA | AUTORSKA ODLUKA (+SKICA) | U pog. 7 uređaj imenovati „zahvatnik (engl. *scoop*)” ili ga prikazati kao usisni koš; u pog. 8 navesti što se iz pog. 7 zadržava, a što mijenja. |
| G2-24 | `u07:713–737` (Z1) | $\rho_2=1{,}02$ kg/m³ pri atmosferskom tlaku odgovara 73 °C (uz $\rho_1=1{,}20$ → 21 °C). Za dovodni zrak strojarnice to nije vjerodostojna radna točka (K16). Izmjereno; ocjena prakse je dojam. | A P2-3 | P2 | POTVRĐENO | BROJ/MODEL | Zadržati fiziku promjene gustoće, a promijeniti kontekst (npr. ispušni plin kroz utilizacijski kotao) ili $\rho_2$; uskladiti ključ i verifikator. |
| G2-25 | `u07:5`, `u07:162`, `u07:906` | K10: ista rečenica o uvjetima za $A_1v_1=A_2v_2$ stoji tri puta. Provjereno. | U | P2 | POTVRĐENO | TEKST | Uvod završiti s „… poseban slučaj te bilance”; zadržati r. 162 i 906. |
| G2-26 | `u07:162`, `u07:323`, `u07:547` | K12: ručno upisan „P3” (sada točan, ali ne prati redoslijed), „sljedeće poglavlje” i „Sljedeća skica”. Provjereno (r. 323 i alat). | U | P2 | POTVRĐENO | TEKST | `@ex-zahvatni-usis-morske-vode-u-plovidbi`, chapter-ref `u08`, `[-@fig-u08-staticka-zamjena-…]`. |
| G2-27 | `u07:313`, `u06:324` | K5: „FVM” i „IMO” javljaju se jednom u poglavlju. Provjereno. | U | P2 | POTVRĐENO | TEKST | Pisati puni naziv bez kratice. |
| G2-28 | `u08:1`, `u08:54`, `u08:852` | „U suženju … tlak na stijenci pada” stoji bez „vodoravnom”. „HGL pada gdje se fluid ubrzava” lako se nauči kao pravilo za tlak; ispravak daje tek Z3 i ključ. Tekst ipak razlikuje tlak i HGL u r. 3 i 70. Provjereno. | St | P2 | POTVRĐENO | TEKST | U r. 1 dodati „vodoravnog”, a uz r. 54 jednu rečenicu: „U silaznom suženju tlak može i rasti (Z3); pada HGL, ne nužno tlak.” |
| G2-29 | `u08:179–198` (izvod energijske jednadžbe) | Prijelaz od $\dot W_s$ do $H_p$ na lijevoj i $H_t$ na desnoj strani nije pokazan; nedostaje $\dot W_s=\dot W_{turbina}-\dot W_{crpka}$. Izvod je točan. Izmjereno (rekonstrukcija predznaka). | St | P2 | POTVRĐENO | TEKST | Ispred definicija visina dodati redak $\dot W_s=\dot W_{turbina}-\dot W_{crpka}$ (oba pozitivna iznosa). |
| G2-30 | `u08:159–161` | Odjeljak „Kada se trenje može zanemariti” ima dvije rečenice bez kriterija, a zatim izvodi energijsku jednadžbu s gubitcima i strojevima. Naslov ne odgovara sadržaju. Provjereno. | St; S P3-8 | P2 | POTVRĐENO | TEKST | Naslov prema sadržaju („Energijska jednadžba s gubitcima i strojevima”) i jedna rečenica s kriterijem (npr. $h_g$ prema promjeni brzinske visine). |
| G2-31 | `u08:29–41`, `u08:72–78` | Interaktivni prikaz Venturija („uljni primjer iz knjige” = P5) i CFD s Pitotovom sondom, $p_t$ i difuzorom dolaze prije nego što su ti pojmovi uvedeni. Bilježnica `u09_venturi` uljni primjer sadrži (870 kg/m³; 0,18 m), pa cilj postoji. Provjereno. | St | P2 | POTVRĐENO | AUTORSKA ODLUKA | Blok premjestiti iza P5 ili dodati rečenicu da se vraćamo nakon P5. |
| G2-32 | `u08:225`, `u08:852` | „Zaključak o kavitaciji samo je nužan, ne i dovoljan uvjet” ne kaže čemu je uvjet nužan i može se pročitati obrnuto. Provjereno. | S P2-4 | P2 | POTVRĐENO | TEKST | „Ako je srednji apsolutni tlak iznad tlaka pare, kavitacija nije isključena: lokalni minimum može biti niži.” |
| G2-33 | `u08:3`, `u08:44–54`, `u08:58`; `u08:7`/`u08:225` | K10: HGL i EGL definirani su triput; uvod gotovo doslovno ponavlja Granicu modela. Provjereno. | U | P2 | POTVRĐENO | TEKST | Zadržati r. 44–54 i 225; r. 3 i 7 skratiti prema prijedlogu urednika. |
| G2-34 | `u08:431`, `u08:455` (P4) | Centrifugalna crpka 2,0 m (u balastu 3,5 m) iznad vodne linije ne može se pokrenuti bez zalijevanja ili samousisne izvedbe, a tekst to ne spominje. Brojevi su točni: $v=2{,}83$ m/s, 65,0 kPa, $NPSH_a=6{,}65$ m, $z_{P,max}=8{,}24$ m, u balastu 49,9 kPa. Izmjereno. | A P2-2 | P2 | POTVRĐENO (zalijevanje) | TEKST | Jednom rečenicom navesti samousisnu izvedbu ili sustav za zalijevanje, uz napomenu da smještaj pokazuje granicu usisa. |
| G2-35 | `u08:509–553` (P5), `u08:5` | Ulje bez zadane viskoznosti: uz $v_1=1{,}856$ m/s za $\nu=30$–70 mm²/s $Re_1\approx1600$–3700, laminarno ili prijelazno strujanje, pa idealni model i $C_d=1$ ne vrijede. Za dizelsko gorivo ($\nu=2$–6 mm²/s) $Re\approx1{,}9$–$5{,}6\cdot10^4$. Izmjereno. | A P2-7 | P2 | POTVRĐENO | TEKST | Fluid zadati kao dizelsko gorivo ili jednom rečenicom reći da za viskozno ulje treba provjeriti $Re$ i koeficijent istjecanja. |
| G2-36 | `u08:569` (P6) | Tvrdnja da $R$ i $T$ u $\rho=p/(RT)$ nisu definirani djelomično je netočna: $R$ je definiran u `u03:109`. Račun: $\rho=1{,}115$ kg/m³. | U | P3 | ODBAČENO kao P2 (cilj postoji) | TEKST | Po želji dodati „(pog. 3)” i „$T$ apsolutna temperatura”. |
| G2-37 | `u08:613` (P6) | „Granice $2300/4000$”: kosa crta (K8) i pragovi koji se u pog. 1–8 ne uvode; uvode se tek u `u11:59`. Provjereno. | U; St P3 | P2 | POTVRĐENO | TEKST | „Granice $Re\approx2300$ i $4000$ za razvijeno strujanje u kružnoj cijevi (pog. 11)”. |
| G2-38 | `u07:377`, `u08:190`, `u06:338`, `u06:844` | K14: tvrdnje o praksi bez izvora ili ograde: „1,6 do 3,6 m/s uobičajene su”, $\alpha=1{,}03$–$1{,}1$ (već uz „obično”), „tankovi se drže punima ili praznima”, gaz spara. Provjereno; točnost raspona nije provjerena izvorom. | A P2-8; S P3-5 | P2 | POTVRĐENO | TEKST | Dodati izvor iz dodatka E ili „kao orijentacija”; gornju granicu 3,6 m/s ne predstavljati kao uobičajenu za usis. |
| G2-39 | sl. 5.8 Z2, Z4, Z6 (str. 106–107); sl. 8.5 (str. 161); sl. 8.7 Z1, Z6 (str. 167) | Oznake se u PDF-u preklapaju. Sl. 5.8: „$L=1{,}20$ m” preko stijenke, „$b=1{,}50$ m” preko kote $H$, „$b$: okomito na presjek” preko dna, „$F_{max}$” i „$F_m$” preko kote $H$. Sl. 8.5: „P crpka”, „u rashladni sustav” i „platforma strojarnice” preko kote $z_P$, „1,5 m (balast)” preko kote. Sl. 8.7: „$z_C=$” i „$p_{atm}$” preko stijenke i cijevi, „$D=70$ mm” preko dna. Fizikalna povezanost je u redu. Izmjereno na renderu. | S P2-10; A P3-11; St P3 | P2 | POTVRĐENO | SKICA | Razmaknuti oznake u kanonskim SVG-ovima, obnoviti tiskovne izvedenice i pregledati konačni PDF. |
| G2-40 | `u07:53` | „Vraćamo se rashladnom krugu”: urednik tvrdi da se krug pojavljuje tek u r. 600. Netočno: hladna ploča i rashladni krug uvedeni su u `u01:27` i `u02:174`. | U | P3 | ODBAČENO kao P2 (cilj postoji) | TEKST | Po K16 dodati „iz pog. 1 i 2”. |
| G2-41 | `u05:15` | Naslov „## Hidrostatičke sile na plohe” ponavlja naslov poglavlja. Izjavan je, pa ga K4 ne zabranjuje. | U | P3 | ODBAČENO kao P2 | TEKST | Prijedlog ukusa („Od lokalnog tlaka do sile na plohu”), ID ostaje. |
| G2-42 | A P2-1, P2-2, P2-5, P2-7 (podtvrdnje) | Primjenski recenzent sam ih je označio „po sjećanju”: brzina usisa 1–2 m/s i DN 200; +5 % mase (≈450 t) od naslaga previsoko; viskozna ulja mjere se Coriolisovim mjeračima; usisni koš u ravnini oplate kao uobičajeno rješenje. | A | — | NEPOTVRDIVO | — | Prije unosa u tekst potkrijepiti djelom iz dodatka E ili izostaviti; ne mijenjati brojeve samo na temelju tih tvrdnji. |

## Računi uz P1 i ključne nalaze

**G2-01 (slobodna površina, P1).** Trup $80\times15$ m, $m_b=4000$ t, $KG_b=3{,}0$ m, tank
$15\times6\times3$ m, more 1025 kg/m³, $I_T=Lb^3/12=22\,500\ \text{m}^4$, $i_t=15\cdot6^3/12=270\ \text{m}^4$.

| Stanje | $m_v$ (t) | $KG$ (m) | $T$ (m) | $V_{ist}$ (m³) | $BM$ (m) | $GM_{kruto}$ (m) | $\delta GM$ (m) | $GM_{ef}$ (m) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| pun tank (primjer) | 276,8 | 2,903 | 3,477 | 4172,4 | 5,393 | 4,228 | 0 | **4,23** |
| napola pun, stvarno | 138,4 | 2,925 | 3,365 | 4037,4 | 5,573 | 4,330 | −0,067 | **4,26** |
| tekst knjige | — | 2,903 | — | 4172 | — | 4,228 | −0,065 | 4,16 |

Tekst kombinira masu i $KG$ punog tanka sa slobodnom površinom napola punoga. Stvarno
napola puno stanje daje veći $GM$ od punoga. Opća poruka da slobodna površina smanjuje $GM$
i dalje vrijedi. Verifikator `verify_u07.py:570–574` računa $\delta GM$ s $V_{ist}$ punoga
tanka, pa potvrđuje isti neodrživi scenarij.

**G2-02 (sažetak pog. 5).** $F=\rho gAh_C$. Za $A=1\ \text{m}^2$, $h_C=2$ m i $A=2\ \text{m}^2$,
$h_C=1$ m ($\rho=998$) obje plohe nose $19{,}58$ kN. Jednaka sila dakle ne zahtijeva jednake
$A$ i $h_C$, nego jednak umnožak. Čitanje „ista sila ⇒ ista $A$ i ista $h_C$” netočno je, a
čitanje „iste $A$ i $h_C$ ⇒ ista sila za svaki nagib” točno. Riječ je o dvosmislenosti koja u
praksi rijetko vodi na pogrešan račun, a sljedeća natuknica već kaže da centar tlaka ovisi o
nagibu. Zato P2, ne P1.

**Ostali računi (sažeto).** G2-03: 13,953/13,981 kN; 8,292/8,309 kN. G2-04: donji zasun
$14{,}158\cdot0{,}897/1{,}60=7{,}937$ kN, gornji $6{,}221$ kN. G2-14: korekcija
$\tfrac12 BM\tan^2\varphi$ iznosi 0,00214 m (0,88 %) pri 6,84°; pri 5° za P3, Z3 i Z6
0,47 %, 0,38 % i 0,46 %. G2-24: $T=p/(R\rho)$ daje 294,2 K i 346,1 K. G2-35: $v_1=1{,}856$ m/s,
$Q=5{,}248$ L/s. G2-34: $p/(\rho g)=6{,}466$ m; DN 200 dao bi 1,59 m/s. G2-17: $A=113{,}1$ m²,
$V=8780{,}5$ m³, $KM=38{,}93$ m. G2-16 (pog. 8 Z6): devet rubnih kombinacija; najniži tlak
59,12 kPa pri $\zeta_\Sigma=\zeta_C=1{,}5$ jednak je idealnom, jer tada od vrha do izlaza nema
gubitka (St P3). Ta je kombinacija rubna, ali dopuštena, jer je uvijek $\zeta_\Sigma\ge\zeta_C$.

## Što je dobro

- Svi brojčani rezultati provjereni ovdje slažu se s tekstom i ključem unutar zaokruživanja. To
  potvrđuje i struka (24 primjera i 24 kontrolna rezultata). Jedina brojčana pogreška je
  ilustracija u G2-01, koja nije riješeni primjer.
- Dosljedna normala $\vec n_f$ i pravilo da smjer $F_V$ određuje strana koju fluid kvasi.
  Primjer s plinskim nadtlakom u pog. 5 pokazuje zašto $h_{CP}=h_C+I_G/(Ah_C)$ ne vrijedi;
  provjera momenta oko središta luka pravi je neovisni test.
- Pog. 6 razdvaja $y_B$ od poluge stabiliteta. Kriteriji 2008 IS Codea navedeni su točno i
  ograđeno, a Z5 (plan A/B) i Z1 (more i rijeka) realne su inženjerske odluke.
- Pog. 7: RTT s pomičnom plohom i primjer broda u plovidbi uz relativnu brzinu; Z6 (balastni
  tank) sa zajamčenim granicama mjerača i jasnim „ne zamjenjuje plan upravljanja balastom”.
- Pog. 8: izvod energijske jednadžbe iz RTT-a s $h_g\ge0$ i $\alpha$. P4 povezuje gaz broda s
  $NPSH_a$ i objašnjava zašto se referentni presjek ne stavlja na otvor koša. Z3 (tlak raste u
  silaznom suženju) ruši tipičnu zabludu, a student ga ističe kao najkorisniji.
- CFD odlomci ne iznose neprovedene rezultate i razlikuju fizikalni model od numeričke pogreške.

Ovo je autorska procjena provjere. CI i verifikatori nisu pokretani za ovu provjeru, pa
didaktička kvaliteta nije dokazana.

## P3 sažetak

Ukupno 41 P3 nalaz u četiri izvještaja (S 10, A 12, U 11 skupina, St 8). Šest ih je u cijelosti
pripojeno gornjim P2 stavkama (S P3-5, P3-6, P3-8; A P3-11; St Re 2300/4000 i sl. 8.5), a S P3-9
i A P3-9 djelomično. Dva su poznata na razini knjige (St: ključ F.9 i Z6 prethodnog poglavlja;
„odjeljak D.7” izvan izdvojenog PDF-a). Ostaju 33, uz 3 snižena iz P2 (G2-36, G2-40, G2-41).

| Skupina | Broj | Primjeri |
| --- | --- | --- |
| Preciznost izvoda i tumačenja | 7 | os nagiba kroz težište vodne linije (`u06:194`), strujna cijev i stacionarnost (`u07:49`), $V^*$ četvrtine valjka (`u05:409`), uvjet monotonosti za omotač, maksimum dometa iz tri točke (P2 pog. 8), neoznačeni 3,6 u (8.35), kut $\zeta_C=\zeta_\Sigma$ u Z6 |
| Vjerodostojnost primjena | 9 | imperijalne mjere u P4 pog. 5, teglenica umjesto teretnog broda, uteg 10 % istisnine, FWA, kontekst platforme u ulju, slijed operacija balastnog tanka, 30,6 m/s u konfuzoru, Pitotov brzinomjer broda i letjelica, banka ideja za dekarbonizaciju |
| Nazivlje i oznake | 4 | Torricelli bez uvođenja, zasun ili pritezni zatvarač, pridružena ili dodana masa, odzračna cijev ili odušnik; L/min, m³/h, $\rho$ umjesto $\rho_{mv}$, $p_t$ uz $p_0$, $R$, $z$, $v_{pog}$ (U P3-7) |
| K10 i K11 sitno | 3 | dodatna ponavljanja (≈12 mjesta), Granica pog. 5 s četiri natuknice (S P3-10, U P3-3) |
| K8 znamenke | 1 | ≈15 mjesta s previše znamenki; ispravak traži usklađivanje ključa i verifikatora |
| K2, K3, K5, K12 blago | 4 | „Promatra se”, „Pitanje.”/„Fizikalno pitanje.”, KV/KP ponovno definirani, 7 prijelaznih „sljedeći”, sitne K3 rečenice (U P3-9) |
| Interpunkcija i raspored | 2 | natuknice bez interpunkcije, naslovi koraka s točkom u pog. 6, raspored teksta Z3 pog. 7 i Z6 pog. 8 |
| Prikaz | 2 | $\lvert\varphi\rvert$ s razmacima u PDF-u, kota $\Delta z$ u skici Z3 pog. 8 |
| Bilježnica | 1 | `u08_kontinuitet_suzenje`: „metoda konačnih volumena” i „FV bilanca” za Eulerovu integraciju jedne ODJ (naziv postoji u bilježnici, provjereno) |
| Snižene stavke iz tablice | 3 | G2-36, G2-40, G2-41 |
