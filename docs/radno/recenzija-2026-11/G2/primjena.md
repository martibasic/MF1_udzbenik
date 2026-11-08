# Primjenska recenzija G2 (pog. 5–8): brodogradnja i strojarstvo

Recenzent: neovisni primjenski recenzent (uputa `references/primjena.md`), 8. 11. 2026.
Materijal: PDF G2 (knjiga str. 89–168) i izvori `source/u05_*.md` … `source/u08_*.md`.
Pravila: K9, K14, K16 i ljestvica P0–P3 iz `docs/konvencije_pisanja.md`; potvrđeno
nazivlje iz `docs/urednicki_stil.md` nije tretirano kao nalaz.

Napomena o izvorima: web nije pretraživan. Svaki raspon označen s „(po sjećanju)”
potječe iz inženjerske prakse i udžbeničkog znanja recenzenta, a ne iz provjerenog
izvora; prije unosa u tekst treba ga potkrijepiti djelom iz dodatka E ili označiti
kao nastavnu procjenu (K14).

## Sažetak

Primjene u pog. 5–8 uglavnom su vjerodostojne. Razgraničenje nastavnog modela od
klasifikacijske ili propisane ocjene u pog. 6 i 7 provedeno je uzorno, a suvremene
teme (plutajući vjetroagregat, baterijski rashladni krug, balast uz zajamčene
granice mjerača) dobro su odabrane. Glavne slabosti su:

- nedosljedno i djelomično nerealno prikazan brodski usis morske vode (pog. 7 i 8);
- nekoliko radnih točaka izvan uobičajene prakse (grijač zraka strojarnice, smještaj
  i brzina u usisu crpke, Venturi za ulje);
- prevlast hidrotehničkih primjera u pog. 5, gdje strojarstvo gotovo izostaje.

## Nalazi

### P0 i P1

Nema nalaza P0 ni P1. Nisam našao primjenu koja bi zbog pogrešnog opisa uređaja
dovela do opasnog ili fizikalno pogrešnog zaključka. Svi brojčani rezultati koje
sam provjerio odgovaraju zadanim podatcima.

### P2

**P2-1. Brodski usis morske vode: dva različita uređaja pod istim lajtmotivom (K16)**
Mjesto: pog. 7, `ex-zahvatni-usis-morske-vode-u-plovidbi`, str. 140–141, slika 7.3
(`u07_…md` r. 382–445); pog. 8, `ex-usisni-vod-rashladne-crpke-morske-vode`,
str. 160–162, slika 8.5 (`u08_…md` r. 426–507, osobito r. 502).

U pog. 7 opisan je „zahvatni usis ispod vodne linije”, „otvor okrenut prema pramcu”.
Na slici 7.3 to je cijev L-oblika koja izlazi ispod oplate dna, a otvor joj je
okrenut prema pramcu. Riječ je o izbočenom zahvatniku (engl. *scoop*). U pog. 8 isti
rashladni sustav ima usisni koš u boku, s rešetkom u ravnini oplate. Rečenica u
r. 502 izričito povezuje ta dva primjera („tlak na otvoru koša, @ex-zahvatni-usis…”),
pa student zaključuje da je riječ o istom uređaju.

U praksi se morska voda za hlađenje uzima kroz usisne koševe uvučene u trup. Rešetka
je u ravnini oplate i ništa ne strši ispod dna, jer bi izbočina povećala otpor i lako
bi se oštetila. Brodovi obično imaju niski usisni koš u dnu za plovidbu i visoki u
boku za plitku i zamuljenu vodu (po sjećanju; uobičajeno rješenje u strojarnicama
trgovačkih brodova). Zahvatnik okrenut prema pramcu (engl. *scoop cooling*) postoji,
ali je poseban i danas rijedak sustav.

Prijedlog: u pog. 7 zadržati fiziku relativne brzine kroz pomičnu plohu, ali uređaj
prikazati kao usisni koš u ravnini oplate. Član $\vec v-\vec v_{KP}$ jednako vrijedi
za otvor u ravnini dna. Ako se namjerno zadržava zahvatnik okrenut prema pramcu,
treba ga imenovati „zahvatnik (engl. *scoop*)” i jednom rečenicom reći da je to
poseban sustav, a da je uobičajen usisni koš. Pri ponovnoj pojavi u pog. 8 treba
navesti što se iz pog. 7 zadržava: isti protok od 180 m³/h i isti rashladni krug.
Treba navesti i što se mijenja: pog. 7 opisuje glavni rashladni sustav u plovidbi, a
pog. 8 pomoćne strojeve na sidrenju, s usisom u boku. Pri tome treba razlučiti visoki
i niski usisni koš.

**P2-2. Smještaj crpke morske vode iznad vodne linije i brzina u usisnom vodu**
Mjesto: pog. 8, `ex-usisni-vod-rashladne-crpke-morske-vode`, str. 160–161
(`u08_…md` r. 431, 455).

Crpke rashladne morske vode u strojarnici obično stoje nisko, na podnicama ili
pokrovu dvodna, ispod vodne linije praznog broda. Tako je usis potopljen i crpka se
sama zalijeva (po sjećanju). Kad je crpka 2,0 m iznad vodne linije, a u balastu
3,5 m, centrifugalna crpka se ne može pokrenuti bez sustava za zalijevanje ili
samousisne izvedbe. Tekst to ne spominje.

Brzina $v=2{,}83$ m/s u usisnom vodu DN 150 viša je od uobičajene. Za usisne vodove
morske vode obično se ciljaju brzine oko 1–2 m/s (po sjećanju, uz ograničenja
erozije za CuNi cijevi), pa bi pri 180 m³/h bio uobičajen DN 200, s oko 1,6 m/s.

Fizika primjera je ispravna. Primjer je i didaktički vrijedan, osobito korak 4 o
stanju u balastu.

Prijedlog, prva mogućnost: jednom rečenicom navesti da je crpka iznad vodne linije
samousisna ili spojena na sustav za zalijevanje. Treba dodati i da je smještaj
odabran kako bi se pokazala granica usisa, a nije tipičan raspored strojarnice.
Druga mogućnost: crpku spustiti ispod vodne linije ($z_P<0$) i pitati koliko gaz u
balastu i ljuljanje smanjuju rezervu. Promjer povećati na 200 mm ili navesti da je
brzina namjerno visoka.

**P2-3. Gustoća zagrijanog zraka u grijaču ventilacije strojarnice**
Mjesto: pog. 7, `task-grijac-ventilacijskog-zraka-strojarnice` (Z1), str. 146
(`u07_…md` r. 713–737).

$\rho_2=1{,}02$ kg/m³ pri atmosferskom tlaku odgovara temperaturi od oko 346 K, tj.
73 °C. Dovodni zrak strojarnice služi za izgaranje i hlađenje prostora. Grije se
samo u hladnom podneblju, i to do nekoliko stupnjeva iznad nule, ili do najviše
oko 20–30 °C (po sjećanju). Zrak od 73 °C u strojarnici nije vjerodostojan.

Prijedlog: zadržati fiziku promjene gustoće, a promijeniti kontekst. Dobar brodski
primjer s velikim omjerom gustoća jest ispušni plin kroz utilizacijski kotao
(ekonomizator) dizelskog motora. Plin se ondje hladi s otprilike 300–350 °C na
oko 170–200 °C, pa se gustoća mijenja s oko 0,57 na 0,78 kg/m³ (po sjećanju).
Taj kontekst ujedno uvodi iskorištavanje otpadne topline. Druga mogućnost je
zadržati grijač, ali s izlazom od oko 25 °C ($\rho_2\approx1{,}18$ kg/m³). Tada je
učinak malen, ali pokazuje da razlika gustoća postoji.

**P2-4. Kućište crpke u moru: nategnut kontekst i prešutna hermetičnost**
Mjesto: pog. 6, `ex-u07-uzgon-na-potonulo-pumpno-kuciste-pri-ispitivanju`, str. 110
(`u06_…md` r. 59–96).

Otvoreno kućište crpke pod vodom se napuni. Tada je istisnuti volumen samo volumen
materijala: za 85 kg lijevanog željeza to je oko 0,012 m³, a ne 0,045 m³. Zadani
$V_{ist}$ ima smisla samo ako je kućište zatvoreno slijepim prirubnicama ili je riječ
o hermetičnom sklopu. Tekst to ne kaže; tek „Provjera” spominje „šuplje hermetičko
tijelo”. Nije jasno ni o kakvom je „ispitivanju” riječ. „Potonulo” ne odgovara opisu
„bez dodira s dnom”.

Prijedlog: uređaj opisati kao uronjivu (potopnu) crpku s hermetičnim kućištem
motora koju dizalica spušta u usisni zdenac, kaljužni bunar ili tank. Tada je
istisnina cijelog sklopa prirodna, a „sila držanja” postaje sila u užetu dizalice.
Naslov uskladiti: „uronjeno” umjesto „potonulo”.

**P2-5. Plutajući vjetroagregat tipa spar: unutarnja nedosljednost i nepotkrijepljena usporedba**
Mjesto: pog. 6, `ex-u07-plutajuci-vjetroagregat-tipa-cilindricne-plovne-osnove-t3`,
str. 124–125 (`u06_…md` r. 785–845).

Primjer je suvremen i fizikalno poučan: stabilitet dolazi iz $KB-KG$, a ne iz $BM$.
Ima četiri slabosti:

- Tekst zadaje „čvrsti balast u dnu”, a promjenu mase od −5 % tumači „ispuštanjem
  balasta”. Čvrsti balast se ne ispušta. Za fino podešavanje gaza stvarne izvedbe
  koriste i vodeni balast (po sjećanju).
- Promjena od +5 % mase, oko 450 t, zbog „naslaga i leda” previsoka je. Morske naslage
  na plutajućoj osnovi tog reda veličine daju nekoliko desetaka do niskih stotina tona
  mase u zraku. Pod vodom većina te mase istisne vodu, pa je neto učinak na gaz manji
  (po sjećanju, nastavna procjena). Led je vezan uz rijetke lokacije.
- Usporedba $KG=45$ m „bez balasta” vodi se uz istu masu od 9000 t, pa nije sustav
  bez balasta, nego sustav s balastom podignutim više. Pri $KG=45$ m težište je i
  dalje 32,6 m ispod vodne linije, pa izraz „težište leži visoko” zbunjuje.
- „Gaz od oko 78 m … odgovara redu veličine izvedenih plovnih osnova tipa spar” jest
  tvrdnja o praksi bez izvora (K14). Po sjećanju, Hywind Scotland ima gaz oko 78 m,
  istisninu reda 11–12 kt i promjer oko 14–15 m pod vodom, uz suženje na vodnoj
  liniji. Red veličine je ispravan, ali treba ga potkrijepiti.

Prijedlog:

- balast opisati kao čvrsti i vodeni, a −5 % pripisati pražnjenju vodenog balasta;
- +5 % pripisati dodanoj opremi ili vodenom balastu, ne naslagama;
- usporedbu pisati kao „isti balast smješten 13 m više”;
- dodati izvor iz dodatka E ili napisati „nastavna procjena”;
- spomenuti da stvarne osnove imaju suženje na vodnoj liniji, zbog kojega je $BM$
  još manji;
- „spar” uvesti kao „(engl. *spar*)” (K5); vidi i P3-9.

**P2-6. Pog. 5: hidrotehnika prevladava, strojarstvo gotovo izostaje (ravnoteža struka)**
Mjesto: pog. 5 u cjelini, str. 89–107.

Od 12 primjera i zadataka izričit brodski kontekst ima samo Z1 (vodonepropusna vrata).
Strojarski kontekst nema nijedan, osim općeg „spremnika s nadtlakom” i „mjernog
panela”. Ostalo su ustave, kanali, bazeni i radijalni zatvarač, kao i oba odlomka o
računalnoj dinamici fluida („gradski kanal”, „zatvarač kanala”). Uvod pritom najavljuje
„brodske pregrade i vodonepropusna vrata”, a student strojarstva ne nalazi svoj primjer.

Prijedlog: fiziku ne mijenjati, nego postojećim primjerima dati kontekst iz obje
struke.

- `ex-u05-cetvrtcilindar-prema-dolje` (str. 101): zatvoreni spremnik s nadtlakom
  plina od 20 kPa odgovara teretnom tanku tankera pod inertnim plinom. Tlačno-vakuumski
  ventili obično su podešeni oko 0,14–0,21 bar (po sjećanju). Druga mogućnost je
  spremnik goriva ili amonijaka s tlakom pare, što je primjer dekarbonizacije.
- `ex-u05-pregrada-ulje-voda` (str. 95): taložni tank goriva ili separator kaljužne
  vode na brodu, s uljem iznad vode.
- `task-u05-nesigurnost-modela-i-mjerenja` (Z6): ispitni stol ili ispitni bazen u
  brodograđevnom laboratoriju.
- Barem jedan od dvaju odlomaka o računalnoj dinamici fluida mogao bi govoriti o
  pramčanim vratima ili rampi ro-ro broda, ili o poklopcu grotla. Tada se vidi da isti
  integral tlaka vrijedi i na brodu.

**P2-7. Venturijeva cijev za ulje: neodređeno „ulje” i model bez viskoznih učinaka**
Mjesto: pog. 8, `ex-u09-venturijeva-cijev-za-mjerenje-protoka-ulja-t2`, str. 162
(`u08_…md` r. 509–553); uvod r. 5 („u strojarstvu se njome mjere protok ulja”).

Ulje gustoće 870 kg/m³ bez zadane viskoznosti student će shvatiti kao mazivo ili
hidrauličko ulje. Za ulje razreda ISO VG 46–68 pri radnoj temperaturi (ν oko
30–70 mm²/s, po sjećanju) $Re$ na ulazu iznosi oko $1{,}6\cdot10^3$–$3{,}7\cdot10^3$,
dakle laminarno ili prijelazno strujanje. Koeficijent istjecanja Venturijeve cijevi
tada osjetno pada ispod 1, pa idealni model daje precijenjen protok. Viskozna ulja
u praksi se mjere volumetrijskim ili Coriolisovim mjeračima. Živin manometar u
industrijskoj se praksi napušta zbog ograničenja uporabe žive (po sjećanju: EU
propisi o živi i Minamatska konvencija).

Prijedlog: fluid zadati kao brodsko dizelsko gorivo (MGO/MDO, ν oko 2–6 mm²/s, po
sjećanju), za koje je $Re\approx2$–$5\cdot10^4$. Dodati jednu rečenicu da bi za
viskozno ulje trebalo provjeriti $Re$ i koeficijent istjecanja. Živin manometar može
ostati kao laboratorijski uređaj. Uz njega treba napomenuti da se u pogonu koristi
diferencijalni pretvornik tlaka.

**P2-8. Tvrdnje o praksi bez izvora ili ograde (K14)**
Mjesto:

- pog. 7, `ex-u08-voda-struji-kroz-difuzor-t2`, str. 139 (`u07_…md` r. 377):
  „brzine od 1,6 do 3,6 m/s uobičajene su za vodu u cijevima”;
- pog. 6, blok „Učinak slobodne površine”, str. 116 (`u06_…md` r. 338): „zato se
  tankovi drže punima ili praznima, a slobodne površine ograničavaju uzdužnim
  pregradama”;
- P2-5 (gaz spara).

Tvrdnje su u biti točne, ali K14 traži izvor ili oznaku nastavne procjene.

Prijedlog: dodati izvor iz dodatka E ili napisati „kao orijentacija”. Gornja granica
od 3,6 m/s za vodu u cijevima već je na rubu uobičajenih vrijednosti; za usise je
previsoka (vidi P2-2).

### P3

**P3-1. Vodonepropusna vrata: zatvarači i propisni kontekst**
Mjesto: pog. 5, `task-vodonepropusna-vrata-naplavljenog-odjeljka` (Z1), str. 104.

Dimenzije 0,80 × 1,60 m i morska voda vjerodostojni su. Stvarna zakretna vodonepropusna
vrata imaju veći broj zatvarača po obodu (engl. *dogs*), a ne dva. U putničkim
brodovima vrata ispod pregradne palube uglavnom su klizna, s pogonom (po sjećanju,
SOLAS II-1). Model s dva zasuna prihvatljiv je kao nastavno pojednostavljenje, a
granica modela već isključuje normativnu prihvatljivost.

Prijedlog: jednom rečenicom navesti da stvarna vrata imaju više zatvarača po obodu
i da su ispod pregradne palube često klizna. Za nazivlje provjeriti uz stručnjaka je
li „zasun” ili „pritezni zatvarač (engl. *dog*)” ustaljeniji u hrvatskoj brodogradnji.
Ovo je napomena, ne tvrdnja o pogrešci.

**P3-2. Preračunate imperijalne mjere**
Mjesto: pog. 5, `ex-u05-potopljena-cetvrtina-kruga`, str. 99 (`u05_…md` r. 452).

Vrijednosti $R=1{,}22$ m, $b=1{,}83$ m i $h_1=2{,}44$ m su 4, 6 i 8 ft. Inženjer
odmah prepoznaje preuzeti američki udžbenički podatak.

Prijedlog: zaokružiti na metričke vrijednosti, npr. 1,20; 1,80; 2,40 m, ili dati
brodski kontekst. Kontrolne rezultate treba ponovno izračunati.

**P3-3. Bočni tank i pravokutni trup**
Mjesto: pog. 6, `ex-u07-izolirani-puni-bocni-tank-kao-dodana-masa`, str. 122–124.

- Zahtjev 1 govori o vodi „koja je ušla u tank”, a tekst kaže da je trup neoštećen i
  tank izoliran. Jasnije je reći da je to balastni tank napunjen morem.
- Za trup se kaže „lijeva stijenka”; brodograđevni naziv je „lijevi bok”.
- $KG=3{,}0$ m pri visini broda 8 m i $GM\approx4{,}2$ m pri širini 15 m tipični su
  za teglenicu (baržu), ne za teretni brod. Za teretne brodove $GM/B$ je obično oko
  0,03–0,10 (po sjećanju).

Prijedlog: trup nazvati teglenicom ili pontonskim brodom, a tank balastnim tankom.

**P3-4. Pokus nagibanja s utegom od 10 % istisnine**
Mjesto: pog. 6, `task-metacentarska-visina-iz-pokusa-nagibanja` (Z3), str. 126.

U stvarnom pokusu nagibanja ukupna masa utega iznosi oko 1–2 % istisnine. Utezi se
pomiču u više koraka, a nagib se mjeri njihalima ili inklinometrima, uz kutove
reda 1–3° (po sjećanju). Zadatak je kao nastavni model ispravan.

Prijedlog: dodati rečenicu o tome kako se pokus stvarno izvodi ili smanjiti $m_k$.

**P3-5. More i rijeka te areometar**
Mjesto: pog. 6, Z1 i Z4, str. 126–127.

Z1 je vjerodostojan: 24,6 t/cm i 12 000 t realne su vrijednosti. Praksa za istu pojavu
koristi naziv dodatak za slatku vodu (engl. *fresh water allowance*, FWA), uz oznake
teretnih linija (po sjećanju).

Prijedlog: spomenuti FWA u Z1. Areometar u Z4 može postati areometar za lučku vodu
(engl. *dock water hydrometer*), kojim časnik mjeri gustoću vode u luci prije
određivanja gaza. Tako se Z1 i Z4 povezuju u brodski kontekst bez promjene fizike.

**P3-6. Platforma na granici ulja i vode bez stvarnog konteksta**
Mjesto: pog. 6, `ex-u07-plutajuca-servisna-platforma-na-granici-ulja-i` (T4,
str. 119) i `task-u07-pravokutna-servisna-platforma…` (Z6, str. 127).

Nije rečeno gdje servisna platforma pluta u sloju ulja debljine 8–10 cm. Moguće je
mjesto bazen separatora zauljenih voda, ali tekst ga ne imenuje. Dvaput se ponavlja
isti prizor.

Prijedlog: navesti kontekst, npr. mjernu platformu u bazenu separatora zauljenih voda
brodogradilišta ili rafinerije. Druga mogućnost je uslojeni estuarij sa slatkom vodom
iznad mora, primjerice ušće Krke ili Neretve. Tada bi debljinu sloja trebalo povećati,
pa bi se promijenili i brojevi.

**P3-7. Balastni tank dvodna: ispiranje slatkom vodom i odzračna cijev**
Mjesto: pog. 7, `task-balastni-tank-dvodna-mijesanje-i-odzracnik` (Z6), str. 147.

Zadatak je jedan od najboljih u skupini (vidi dolje).

- Istodobno balastiranje morem, „ispiranje slatkom vodom” i pretakanje neobičan su
  pogonski slijed.
- Tlocrtna površina od 36 m² mala je za tank dvodna broda s balastnom crpkom od
  250 m³/h.
- Kad razina dosegne odzračnu cijev, voda se u cijevi brzo diže do glave na palubi.
  Prije prelijevanja tank je pod tlakom stupca u cijevi, što je stvarni konstrukcijski
  rizik.

Prijedlog: miješanje gustoća povezati sa stvarnom operacijom. Primjer je izmjena
balastne vode protočnom metodom (Konvencija o upravljanju balastnim vodama, standard
D-1; po sjećanju), u kojoj se miješaju obalna voda niže slanosti i oceanska voda, a
višak izlazi kroz odušnike. Može se dodati i rečenica o tlaku u tanku dok se voda
diže u odzračnoj cijevi.

**P3-8. Brzina u konfuzoru ventilacijskog kanala**
Mjesto: pog. 8, `ex-u09-pad-statickog-tlaka-u-konfuzoru-ventilacijskog-kanala`, str. 156.

Brzina $v_2=30{,}6$ m/s viša je od uobičajenih brzina u ventilacijskim kanalima. Za
niskobrzinske sustave one su do oko 10 m/s, a za visokobrzinske do oko 20–25 m/s
(po sjećanju; buka i pad tlaka).

Prijedlog: povećati $A_2$ ili uređaj nazvati ulaznom mlaznicom ventilatora odnosno
mjernom mlaznicom.

**P3-9. Nazivlje**

- Pog. 6, r. 927 (str. 126): „uvjet stabilnosti homogenog pravokutnog bloka”. Ostatak
  poglavlja dosljedno piše „stabilitet”.
- Pog. 6, r. 790: „plovna osnova (spar)”. U struci se češće govori o plutajućem temelju
  (engl. *floating foundation*) tipa spar; ovo je napomena. Engleski izraz treba
  označiti s „engl.” (K5).
- Pog. 6, r. 281: „pridružena masa”. U hrvatskoj brodskoj hidrodinamici čest je naziv
  „dodana masa” (engl. *added mass*). Izbor „pridružena” razumljiv je jer se izbjegava
  zabuna s metodom dodane težine. Ovo je napomena, ne nalaz.
- Pog. 7, Z6: „odzračna cijev”. Na brodu je uobičajen i naziv „odušnik”; dovoljno je
  oba naziva povezati pri prvom spomenu.

**P3-10. Pitotov brzinomjer broda i Pitotova sonda na letjelici**
Mjesto: pog. 8, Z4 (str. 165) i `ex-u09-pitot-staticka-sonda-na-bespilotnoj-letjelici-za`
(str. 164).

Pitotov brzinomjer broda povijesno je postojao, a danas prevladavaju elektromagnetski
i Dopplerov brzinomjer (po sjećanju). Zadatak je vjerodostojan, ali treba ga
uokviriti kao načelo ili stariji uređaj. Primjer s bespilotnom letjelicom ispravan je,
ali izlazi iz obje ciljne struke.

Prijedlog: Z4 dodati rečenicu o suvremenim brzinomjerima. Kao alternativu za letjelicu
moguće je mjerenje brzine zraka u ventilacijskom ili ispušnom kanalu broda, ili
anemometar na palubi za heliodrom.

**P3-11. Slika 8.5: preklapanje oznaka**
Mjesto: pog. 8, slika 8.5, str. 161.

Strelica „u rashladni sustav” prelazi preko oznake „crpka”. Oznaka „$z_u = 3{,}0$ m”
dodiruje oplatu boka. Na skici nema usisnog ventila ni filtra koje gubitak
$h_g$ uključuje; prema AGENTS.md dovoljno ih je naznačiti.

**P3-12. Suvremenost: neiskorištena mjesta za dekarbonizaciju**

U pog. 5–8 nema spremnika alternativnih goriva (LNG, amonijak, metanol), uređaja za
obradu balastnih voda ni pročistača ispušnih plinova (engl. *scrubber*), premda svi
prirodno pripadaju hidrostatici i bilanci mase. Ideje koje ne mijenjaju fiziku:

- tlak pare u spremniku goriva ili amonijaka kao plinski nadtlak (pog. 5, vidi P2-6);
- slobodna površina u djelomično punom spremniku metanola ili LNG-a (pog. 6);
- bilanca mase vode za ispiranje u pročistaču ispušnih plinova ili protok kroz uređaj
  za obradu balastnih voda (pog. 7);
- gubitak $h_g$ kroz filtar uređaja za obradu balastnih voda, koji smanjuje
  raspoloživi tlak na usisu crpke (pog. 8).

Ovo je banka ideja, ne obveza proširenja.

## Ravnoteža struka

| Poglavlje | Brodogradnja i pomorstvo | Strojarstvo | Ocjena |
| --- | --- | --- | --- |
| 5 | Z1 vodonepropusna vrata; uvod | nema izričitog primjera | **neravnoteža**; prevladava hidrotehnika (P2-6) |
| 6 | ponton, platforma, tank, spar, brod more/rijeka, pokus nagibanja | kućište crpke (nategnuto, P2-4), kompresor, akumulator, areometar | brodogradnja prevladava, što je primjereno temi; strojarstvo je prisutno, ali slabo |
| 7 | zahvatni usis, balastni tank dvodna, ventilacija strojarnice | T-komad hidraulike, rashladni krug baterije, Pitotovo mjerenje profila, hladna ploča (CFD) | **uravnoteženo**, najbolje u skupini |
| 8 | usisni vod crpke morske vode, Pitotov brzinomjer broda | konfuzor ventilacije, Venturi za ulje, Pitotova sonda na letjelici | uravnoteženo; dio zadataka je općenit (spremnik, sifon, mlaz) |

Za skupinu u cjelini obje struke imaju svoje primjere, uz izuzetak pog. 5. Strojarski
primjeri u pog. 7 uglavnom su automobilski i zgradarski (električno vozilo,
ventilacijski kanal). Rashladni krug baterije lako se može prenijeti na baterijski
sustav električnog trajekta. Tako bi isti primjer služio objema strukama i temi
elektrifikacije pomorstva.

## Posebno dobre primjene

- **Pog. 6, kriteriji IMO 2008 IS Code** (str. 115): vrijednosti 0,055/0,09/0,03 m·rad,
  $GZ\ge0{,}20$ m, vrh na najmanje 25° i $GM_0\ge0{,}15$ m odgovaraju mom znanju kodeksa.
  Izvor je naveden, a ograda „sami kriteriji površina ne dokazuju usklađenost” uzorno
  zadovoljava K9 i K16.
- **Pog. 6, plutajući vjetroagregat tipa spar**: suvremena primjena s jasnim fizikalnim
  uvidom, koju treba samo dotjerati prema P2-5.
- **Pog. 6, blok o učinku slobodne površine i Z5 (plan A/B)**: realna inženjerska odluka
  s dva uvjeta i izričitim „nisu propisana provjera plovila”.
- **Pog. 6, Z1 more i rijeka**: realne vrijednosti 24,6 t/cm i razlika gaza 0,13 m.
- **Pog. 5, Z1 vodonepropusna vrata** i **Z3 samootvarajuća zaklopka**: vjerodostojne
  dimenzije i jasna odluka.
- **Pog. 7, Z6 balastni tank dvodna** (T4): zajamčene granice pogreške mjerača i odluka
  o radu bez nadzora pravi su inženjerski problem s ispravnim razgraničenjem („ne
  zamjenjuje plan upravljanja balastom”).
- **Pog. 7, rashladni krug baterije, hladna ploča i Z4 Pitotovo mjerenje profila u
  kanalu**: suvremeno i mjerno realno, s naglaskom na prsten uz stijenku.
- **Pog. 8, usisni vod crpke morske vode, korak 4 (brod u balastu)**: izvrsno povezuje
  gaz broda s usisnim uvjetima crpke i uvodi raspoloživu NPSH. Uz ispravke iz P2-1 i
  P2-2 to je središnja brodostrojarska primjena skupine.

## Opseg i ograničenja

Pročitani su uvodi, svi riješeni primjeri, zadatci za vježbu i odlomci o računalnoj
dinamici fluida u pog. 5–8, iz izvora i iz PDF-a. Slike su pregledane na str. 110,
140 i 161. Brojčani rezultati provjereni su samo ondje gdje su bili potrebni za ocjenu
vjerodostojnosti (npr. temperatura zraka iz $\rho_2$, $Re$ za Venturi). Izvodi nisu
provjeravani. Sve vrijednosti označene „po sjećanju” treba potvrditi izvorom prije
unosa u tekst.
