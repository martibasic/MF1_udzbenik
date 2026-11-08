# Urednički i lektorski pregled — poglavlja 5–8

Uloga: urednik i lektor (uputa `.claude/skills/recenzija-prirucnika/references/urednik.md`).
Materijal: `source/u05_…`, `u06_…`, `u07_…`, `u08_…` (stanje radne kopije na grani
`konvencije-recenzije`, commit `9d343b3`), PDF `G2.pdf` (knjiga str. 89–168; str. PDF-a + 88 =
str. knjige), izlaz `tools/prirucnik_stats.py` (profil, `--nalazi`, `--nacrt`).
Pravila: `docs/konvencije_pisanja.md` (K1–K16), `docs/urednicki_stil.md` (Tekst; Notacija i
nazivlje; Odluke završne recenzije). Pregled je neovisan: nisu čitani `docs/radno/`,
`RECENZIJA_ZAVRSNA.md`, `CHANGELOG.md`, git povijest ni drugi izvještaji.
Izostavljeno kao poznato: „odgovarajući izraz” u ključu, upućivanja „primjer N.M”, skriveni
„Provjeri sebe”, nazivi bilježnica `uNN_`. Fiziku ne ocjenjujem, osim gdje formulacija mijenja tvrdnju.

## Nalazi alata (`--nalazi`) — potvrda

| Mjesto | Pravilo | Odluka |
| --- | --- | --- |
| u05:170 | K12 | potvrđeno, P2 (tablica pog. 5) |
| u06:113, 234, 324 | K3 | potvrđeno, P2; u r. 324 i K5 (IMO) |
| u07:9 | K3 | potvrđeno, P2 |
| u07:694 | K3 | oblik potvrđen, ali u skrivenom „Provjeri sebe”; P3 |
| u07:323 | K12 | potvrđeno, P2 |
| u07:380 | K12 | djelomično: prijelazna rečenica neposredno ispred primjera; P3 |
| u08:220, 225 | K3 | potvrđeno, P2 |

Alat nije prepoznao još nekoliko opisnih upućivanja („Sljedeća skica”, „vidi blok”, „u okviru
o granici modela”, „P3”), engleske kratice (FVM, *spar*) ni ponovljene formule; dodane su niže.

## Poglavlje 5 — Hidrostatičke sile na ravne i zakrivljene plohe

| Mjesto | Pravilo | Sadašnji tekst | Prijedlog | Težina |
| --- | --- | --- | --- | --- |
| u05:901 (i u05:134) | K9, jezik mijenja tvrdnju | r. 901: „ista sila na nagnutoj plohi znači samo jednaku površinu i jednaku dubinu težišta”; r. 134: „to znači jednaku silu samo za plohe jednake površine i jednake dubine težišta” | r. 901: „…vrijedi $F=\rho gAh_C$ za svaki nagib: plohe jednake površine i jednake dubine težišta nose jednaku silu bez obzira na nagib.” r. 134: „ali to znači samo da plohe jednake površine i jednake dubine težišta nose jednaku silu bez obzira na nagib.” Doslovno čitanje sada tvrdi da jednaka sila zahtijeva jednake $A$ i $h_C$, a dovoljan je jednak umnožak $Ah_C$; „samo” premješteno uz „znači” | P1 (r. 901, sažetak), P2 (r. 134) |
| u05:15 | K4 | „## Hidrostatičke sile na plohe” (ponavlja naslov poglavlja) | „## Od lokalnog tlaka do sile na plohu” (ID `#hidrostatske-sile-na-plohe` ostaje) | P2 |
| u05:170 | K12 | „na stijenku cisterne iz prethodnog poglavlja” | „na stijenku cisterne iz []{.mf1-chapter-ref target="u04"}” | P2 |
| u05:581 | K12, K10 | „…ne smije primijeniti; moment se računa iz cijele raspodjele, kako je najavljeno u odjeljku o referentnom tlaku.” | „…ne smije primijeniti; moment se računa iz cijele raspodjele, kako upozorava tekst uz jednadžbu [-@eq-sile-plohe-referentni-tlak-i-smjer-sile-02].” | P2 |
| u05:441 | K2 | CFD blok u 1. l. mn. („računamo”, „provjeravamo”) uz „usporedi njihove krakove prema istoj osi” | „usporedimo njihove krakove prema istoj osi” | P2 |
| u05:865 | K2 | u tekstu zadatka („Pretpostavi…”) „Standardnu nesigurnost veličine $x$ označujemo sa $s(x)$” | „Standardna nesigurnost veličine $x$ označuje se sa $s(x)$, kao u ostatku priručnika.” | P2 |
| u05:3, 5, 22, 343 | K10 | „Na ravnoj plohi sve lokalne tlačne sile imaju isti smjer” (r. 3 = r. 22); „Na zakrivljenoj plohi lokalne normale mijenjaju smjer” (r. 5 = r. 22, slično r. 343); uvod r. 3 iznosi $F$, $h_{CP}$ i tri izraza za $I_G$ prije izvoda | Zadržati r. 22 i 343. Uvod r. 3 i 5 skratiti na po jednu rečenicu s upućivanjem na [-@eq-u05-sila-ravna-ploha], [-@eq-u05-centar-tlaka-vertikalna] i [-@eq-u05-zakrivljena-horizontalna]. Izraze $I_G$ za trokut i krug ne brisati, nego premjestiti uz izvod centra tlaka (krug se ne javlja drugdje u poglavlju) | P2 |

## Poglavlje 6 — Uzgon, plivanje i početni stabilitet

| Mjesto | Pravilo | Sadašnji tekst | Prijedlog | Težina |
| --- | --- | --- | --- | --- |
| u06:28 | K4 | „## Matematički izvod” (odjeljak 6.2 obuhvaća izvod, primjer, CFD, $BM$, $GZ$ i slobodnu površinu) | Naslov-pretinac zamijeniti izjavnim, npr. „## Arhimedov zakon, plivanje i metacentar”; razmotriti podjelu na `###` („Arhimedov zakon”, „Metacentarski radijus”, „Krivulja stabiliteta $GZ$”) | P2 |
| u06:266 | K4 | Granica modela — „Koliko je „mali” kut za pravokutni ponton?” | „Granica modela — Granica malog kuta za pravokutni ponton” | P2 |
| u06:279 | K4 | „**Vraća li se ponton i koliko se dugo njiše?**” | „**Povratni moment i njihanje pontona.**” (kao u05:168, 437) | P2 |
| u06:19 i 51 | K10 | $F_U=\rho gV_{ist}$ numerirana dvaput, jedn. (6.1) i (6.5), četiri retka razmaka (str. 109) | r. 17–19 bez istaknute jednadžbe: „…jednaka je težini istisnutog fluida, $F_U=\rho gV_{ist}$; izvod slijedi u jednadžbi [-@eq-uzgon-stabilitet-matematicki-izvod-04].” Prije uklanjanja ID-ja provjeriti poveznice | P2 |
| u06:5, 115, 262 | K10 | uvjeti $GM>0$, $=0$, $<0$ navedeni tri puta | Zadržati r. 262 (izvod) i r. 5 (uvod). R. 115 skratiti: „Tada se uvodi metacentar $M$, a o početnom stabilitetu odlučuje predznak metacentarske visine $GM$ (jednadžba [-@eq-uzgon-stabilitet-matematicki-izvod-metacentarski-radijus-07]).” | P2 |
| u06:3 i 143 | K10 | „Jednoliki tlak na slobodnoj površini poništava se, pa uzgon ne ovisi o atmosferskom tlaku” (r. 3) ≈ r. 143 | Zadržati r. 143 uz izvod (sadrži i „ni o apsolutnom tlaku”); iz r. 3 izostaviti tu rečenicu | P2 |
| u06:113 | K3 (42 r.) | „Obrazloženje je kratko: zamislimo …; na njega djeluju …, a on je u ravnoteži …, pa rezultanta …” | „Zamislimo da istisnuti volumen ispunjava isti fluid u mirovanju. Na njega djeluju isti okolni tlakovi kao na tijelo, a on je u ravnoteži pod vlastitom težinom. Rezultanta tlakova zato mora biti jednaka toj težini i prolaziti težištem toga volumena.” | P2 |
| u06:234 | K3 (52 r.) | „Ako tijelo pluta u sloju … , pri nagibu nastaju dva para klinova: na slobodnoj površini … i na razdjelnici …” | „Neka tijelo pluta u sloju lakšeg fluida gustoće $\rho_u$ i debljine $\delta$ iznad težeg fluida gustoće $\rho_v$, a dno mu je u težem fluidu. Pri nagibu tada nastaju dva para klinova:” + natuknice „na slobodnoj površini klin lakšeg fluida, s momentom $\rho_uI_T\varphi$;” i „na razdjelnici klin u kojem teži fluid zamjenjuje lakši, s momentom $(\rho_v-\rho_u)I_T\varphi$.” | P2 |
| u06:324 | K3 (61 r.), K5 | niz kriterija odvojen točkom-zarezom; „IMO-ova pravilnika” (kratica jednom u poglavlju) | „Za brodove na koje se primjenjuju opći kriteriji pravilnika Međunarodne pomorske organizacije *2008 Intact Stability Code* [@imo-is-code-2008] provjerava se skup uvjeta, među ostalim:” + šest natuknica s nepromijenjenim brojevima (0,055 m rad do 30°; 0,09 m rad do 40° ili kuta naplavljivanja ako je manji; 0,03 m rad između 30° i te granice; $GZ\ge0{,}20$ m pri kutu od najmanje 30°; maksimum $GZ$ pri kutu ne manjem od 25°; $GM_0\ge0{,}15$ m). Zadnja rečenica ostaje | P2 |
| u06:790 | K5 | „Uspravna cilindrična plovna osnova (spar)” | „…plovna osnova (engl. *spar*)” | P2 |
| u06:927, 933, 940 | K6, K7 | „relativne gustoće $s=\rho_d/\rho$”, „uvjet stabilnosti” | „$s_r=\rho_d/\rho$” na sva tri mjesta; „uvjet stabiliteta” (naslov poglavlja i urednički stil rabe „stabilitet”) | P2 |
| u06:176 | K12 | „razlika višeg reda u kutu obrađena je u okviru o granici modela” | „…obrađena je jednadžbom [-@eq-poluga-okomiti-bokovi]” | P2 |
| u06:782 | K12, K2 | „(vidi blok „Učinak slobodne površine u tanku”)” | „(jednadžba [-@eq-ucinak-slobodne-povrsine])” | P2 |
| u06:60 | jasnoća naslova | „Uzgon na potonulo kućište crpke pri ispitivanju” uz „bez dodira s dnom” | „Uzgon na uronjeno kućište crpke pri ispitivanju” (ID ostaje) | P2 |

## Poglavlje 7 — Kinematika, kontrolni volumen i kontinuitet

| Mjesto | Pravilo | Sadašnji tekst | Prijedlog | Težina |
| --- | --- | --- | --- | --- |
| u07:5, 162, 906 | K10 | ista rečenica tri puta: „$A_1v_1=A_2v_2$ … vrijedi za stacionaran tok jednoga fluida stalne gustoće kroz jedan ulaz i jedan izlaz” | Zadržati r. 162 (Granica modela) i r. 906 (sažetak). R. 5 završiti s „…samo je poseban slučaj te bilance, odnosno jednadžbe kontinuiteta.” | P2 |
| u07:142 i 245 | K10 | ista jednadžba $\sum\dot m_{ul}-\sum\dot m_{iz}=dm_{KV}/dt$ numerirana dvaput | R. 242–246: „odnosno u poznatijem obliku, jednadžbi [-@eq-kinematika-kv-fizikalni-uvod-i-matematicki-izvod-01].” (ili obratno: r. 142 bez broja) | P2 |
| u07:53, 313, 666 | K4 | „**Zadržava li se tekućina u kutu razdjelnika?**”, „**Zašto mreža od tisuću ćelija poštuje istu bilancu kao spremnik?**”, „**Dobivaju li svi rashladni kanali jednak protok?**” | „**Zadržavanje tekućine u kutu razdjelnika.**”, „**Ćelija mreže i spremnik: ista bilanca mase.**”, „**Podjela protoka među rashladnim kanalima.**” (pitanje već stoji u *Pitanje:* odnosno u „Zastani i promisli”) | P2 |
| u07:53 | K12 | „Vraćamo se rashladnom krugu i promatramo ulaznu komoru hladne ploče.” | Nije jasno na koji se krug vraća: rashladni krug baterije pojavljuje se tek u primjeru na r. 600. Navesti izvor („pog. N”) ili ukloniti „Vraćamo se” | P2 |
| u07:162 | K12 | „(klip u Z5, brod u plovidbi u P3)” | „(klip u Z5, brod u plovidbi u primjeru [-@ex-zahvatni-usis-morske-vode-u-plovidbi])”; ručno upisan „P3” ne prati promjenu redoslijeda | P2 |
| u07:313 | K5 | „U metodi konačnih volumena (FVM) jedan mogući zapis…” (kratica jednom, engleska) | „U metodi konačnih volumena jedan mogući zapis…” | P2 |
| u07:323 | K12 | „Tlak i energiju istoga problema povezuje sljedeće poglavlje” | „…povezuje []{.mf1-chapter-ref target="u08"}” | P2 |
| u07:547 | K12 | „Sljedeća skica uspoređuje tri tipična slučaja” | „Slika [-@fig-u08-staticka-zamjena-za-kontrolni-volumen-i-kontinuitet] uspoređuje tri tipična slučaja” | P2 |
| u07:9 | K3 (46 r.) | „Lijevo je apstraktni uređaj …, a ne krutu ovojnicu: u kontrolni volumen KV ulazi …, iz njega izlaze …, a unutar njega …” | „Lijevo je apstraktni uređaj koji predstavlja bilo koji proces, a ne krutu ovojnicu. U kontrolni volumen KV ulazi struja gustoće $\rho_1$, presjeka $A_1$ i brzine $v_1$ s masenim protokom $\dot m_{ul}$. Iz njega izlaze dvije struje $\dot m_{iz,1}$ i $\dot m_{iz,2}$, a unutar njega se masa akumulira brzinom $dm_{KV}/dt$.” | P2 |
| u07:750, 837, 844 | K2 | u zadatcima („Odredi”): „ako istu plohu orijentiramo”, „debljinu klipa … zanemarujemo”, „Ako klip zaustavimo” | „ako istu plohu orijentiraš suprotnom normalom”; „debljinu klipa pri računanju volumena komore zanemari”; „Ako se klip zaustavi uz isti dotok” | P2 |

## Poglavlje 8 — Energijska jednadžba i Bernoulli

| Mjesto | Pravilo | Sadašnji tekst | Prijedlog | Težina |
| --- | --- | --- | --- | --- |
| u08:3, 44–54, 58 | K10 | definicije HGL i EGL tri puta; „Iz tih članova grade se dvije crte za prikaz energije toka” (r. 3) ≈ „Iz istih članova proizlaze dvije crte za prikaz energije toka” (r. 44); r. 58 počinje ponovnom definicijom | Zadržati r. 44–54. R. 3: „Iz tih članova grade se piezometarska crta (HGL) i energijska crta (EGL).” (bez formula). R. 58 početi s „Pri crtanju otvorenih vodnih sustava…”; rečenicu o položaju EGL iznad HGL zadržati | P2 |
| u08:20 i 148 | K10 | $p/(\rho g)+v^2/(2g)+z=\text{konst.}$ numerirana dvaput (jedn. 8.1 i kraj izvoda) | R. 145–149: „Dijeljenjem s $g$ nastaje klasični Bernoullijev oblik u metrima fluida, jednadžba [-@eq-energijska-bilanca-fizikalni-uvod-i-matematicki-izvod-01].” | P2 |
| u08:7 i 225 | K10 | uvod gotovo doslovno ponavlja Granicu modela („ne sadrži trenje, rad strojeva ni nestacionarne članove … srednji tlak … ne lokalni minimum … Machov broj … 0,3”) | Zadržati r. 225. R. 7: „Gubitci i rad crpke brojčano se obrađuju u pog. 13, a stlačivost plina u pog. 9.” (svi uvjeti i prag 0,3 ostaju na r. 225) | P2 |
| u08:75 | K2 | blok u 1. l. mn. („pretpostavljamo”, „Smijemo li”) uz „Provjeri ukupnu mehaničku energiju… Tako odvoji…” | „Provjeravamo ukupnu mehaničku energiju prije cijelog mjerača i poslije njega. Tako odvajamo koristan mjerni signal od trajnog opterećenja crpke.” | P2 |
| u08:230 | K4 | „**Što ručni račun može provjeriti u CFD-u, a što CFD dodaje?**” | „**Ručna provjera CFD-a i ono što CFD dodaje.**” | P2 |
| u08:220 | K3 (41 r.) | „…nose istu ukupnu visinu $p_{atm}/(\rho g)+z_A$; zato smijemo spojiti…” | točku umjesto točke-zareza: „…$+z_A$. Zato smijemo spojiti površinu s bilo kojim presjekom cijevi ili mlaza, iako ne znamo koja strujnica vodi do koje točke presjeka.” | P2 |
| u08:225 | K3 (42 r.) | „…nestacionarne članove: čim gubitci …, čim je u sustavu …, treba primijeniti jednadžbu […] ili modele iz pog. 13.” | „Bernoullijeva jednadžba ne sadrži trenje, rad strojeva ni nestacionarne članove. Jednadžbu [-@eq-energijska-jednadzba-kv] ili modele iz []{.mf1-chapter-ref target="u13"} treba primijeniti čim gubitci mjerljivo smanjuju tlak (dugi vodovi, ventili, nagla proširenja), čim je u sustavu crpka ili turbina ili čim se protok mijenja u vremenu.” | P2 |
| u08:569 | K5, K6 | „gustoća zraka iz jednadžbe stanja $\rho=p/(RT)$” ($R$ i $T$ nisu definirani; $R$ je prema stilu plinska konstanta tek u pog. 9) | „…iz jednadžbe stanja idealnog plina $\rho=p/(RT)$, gdje je $R$ plinska konstanta zraka, a $T$ apsolutna temperatura, iznosi…” | P2 |
| u08:613 | K8 (kosa crta) | „Granice $2300/4000$ vrijede…” | „Granice $Re\approx2300$ i $4000$ vrijede…” | P2 |
| u08:812 i 825 | K10, K15 | **Tekst zadatka** daje gotove bilance („Primijeni bilance $\Delta z=(1+\zeta_\Sigma)v^2/(2g)$ i $p_{aps,C}=…$”), a **Naputak** ih ponavlja doslovno | Problem, ne zamjena: formule stoje na dva mjesta i u tekstu T4 zadatka unaprijed daju postupak. Autorica odlučuje ostaju li u tekstu (model kao podatak) ili samo u naputku | P2 |

## P3 — skupno

1. K10, ostala ponavljanja: „jednoliki tlak plina mijenja i silu i hvatište” (u05:5, 44, 581, 661, 900); „ukupna sila ne jamči moment” (u05:170, 441); ubrzanje u stacionarnom suženju (u07:66, 131, 903); popis Venturi, Pitot, mlaz, sifon (u08:5, 44); „metacentarska teorija samo za mali nagib” (u06:7, 326); opisi slike u uvodu (r. 9 u sva četiri poglavlja) djelomično ponavljaju potpis. Oko 12 mjesta.
2. K8, više znamenki nego što pravilo dopušta (međurezultat 3–4, rezultat 2–3): u05:717, 818; u06:1030; u07:856; u08:279 (30,63063; 523,62 Pa), 529, 544 (22478,634), 548, 739, 770, 800. Oko 15 mjesta; promjena zahtijeva usklađivanje ključa i verifikatora.
3. K11: Granica modela duža od tri rečenice: u05:415–418 (četiri natuknice), u06:268–274 (pet rečenica i jednadžba).
4. K2 i ujednačenost izvoda: bezlični „Promatra se” (u06:148, 194) uz „zamislimo” i „promatramo” drugdje; „**Pitanje.**” (u05, u08:121) i „**Fizikalno pitanje.**” (u07:183, u08:166).
5. K5: KV i KP definirani ponovno (u07:5 te 183, 185).
6. K12, blaga prijelazna upućivanja: u06:140 „sljedeći račun”, u06:188 „u sljedećem okviru”, u07:380 „Sljedeći primjer”, u08:115 „tema sljedećeg izvoda”, u08:34 „uljni primjer iz knjige”, u08:207 „prvi korak prema njemu”, u08:419 „prema tom lokalnom kriteriju”. 7 mjesta.
7. K6, K7: protok u L/min i m³/h (u07:53, 605; u07:387, 868; u08:431) uz pravilo L/s; morska voda $\rho$ umjesto $\rho_{mv}$ (u07:387, u08:431); „ukupni tlak” $p_t$ (u08:71) uz $p_0$ iz tablice; $R$ za silu praga (u05:782); $z$ i za normirano odstupanje (u05:869); indeks $v_{pog}$ (u08:770).
8. Interpunkcija: natuknice bez interpunkcije (u06:23–24, u08:214–218) uz točku-zarez drugdje; naslovi koraka s točkom u pog. 6 (u06:663–751, 800–821), bez točke u pog. 7 i 8; istaknute jednadžbe bez završnog znaka (u06:19, u08:27, 527–535); `$60\%$`, `$40\%$` (u07:559) uz `6{,}7\,\%`; `12^\circ\text{C}` bez razmaka (u08:569); „(brod + voda u tanku)” (u06:651).
9. K3, sitno: u07:49 (druga rečenica ponavlja prvu); u07:157 („nestlačivom … i kad je gustoća praktički ista”); u08:127 i 133 (stalna gustoća dvaput); u08:212 (meta-rečenica „Uz izvod treba jasno navesti…”); u05:338 („bez doprinosa $F_{2,r}$ to ne bi vrijedilo”, nejasan subjekt); u07:138 („drugi pogled”); u07:694 (skriveno).
10. Raspored teksta zadatka: u07:707 uvod pripisuje opće pretpostavke samo Z3; u08:810 pretpostavke prije prizora (urednički stil: prizor, pretpostavke, odluka).
11. PDF: $|\varphi|\le5^\circ$ prikazano s razmacima unutar apsolutne vrijednosti (str. 114 i dalje).

## Tri najčešća obrasca

1. **Ponavljanje istog sadržaja (K10).** Uvod iznosi formule i uvjete koje odjeljak zatim izvodi, Granica modela i sažetak ponavljaju istu rečenicu, a ista je formula dvaput numerirana (jedn. 6.1 i 6.5, bilanca mase u pog. 7, Bernoullijeva jednadžba u pog. 8).
2. **Opisna upućivanja bez broja (K12).** „Prethodno” ili „sljedeće poglavlje”, „sljedeća skica”, „okvir o granici modela”, „vidi blok”, ručno upisan „P3”.
3. **Naslovi u obliku pitanja ili naslovi-pretinci (K4).** Vodeći retci CFD blokova (u06:279, u07:53, 313, 666, u08:230), labela Granice modela u06:266, naslovi „Matematički izvod” (u06:28) i ponovljeni naslov poglavlja (u05:15). Odmah iza njih su duge rečenice spojene dvotočkom ili točkom-zarezom (K3, 7 mjesta).

## Ograničenja

Ovo je autorska procjena jednog čitača. Provjereno je: izvori su pročitani cijeli, alat je pokrenut, a PDF je uspoređen tekstom (`pdftotext`) i pregledom str. 109 i 114. Nisu provjereni prikaz u webu, skice ni bilježnice. Prijedlozi koji uklanjaju numerirane jednadžbe traže provjeru poveznica i provjeru generatorima prije provedbe.
