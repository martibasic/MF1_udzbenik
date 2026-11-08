# Stručna recenzija — skupina G3 (pog. 9–12)

Recenzent: neovisni agent (uputa `struka.md`), 8. 11. 2026.
Materijal: `G3.pdf` (knjiga str. 169–244), `G3_kljuc.pdf` (dodatak F, str. 344–350),
izvori `source/u09_…`, `u10_…`, `u11_…`, `u12_…`, bilježnice samo za provjeru upućivanja.
Mjesto se navodi kao `datoteka:redak` (izvor) i/ili „str.” (stranica knjige u PDF-u).

## Sažetak

Fizika u poglavljima 9–12 je ispravna. Ponovno sam izračunao sve rezultate riješenih
primjera i sve kontrolne rezultate (24 zadatka). Nisam našao odstupanje veće od zaokruživanja.
Glavni su nedostatci pedagoški: nekoliko zadataka i primjera ponavlja već riješeni problem
(ponekad s istim brojevima), dva mjesta T3 nemaju stvarnu odluku T3, a u ključu nedostaje
dio jednog kontrolnog rezultata. Uz to postoji nekoliko pogrešaka u slikama i upućivanjima.

Broj nalaza: P0 = 0, P1 = 1, P2 = 17, P3 = 14.

## Nalazi

### P0

Nema nalaza.

### P1

**P1-1. Z5 u pog. 10 ponavlja riješeni primjer P1 (Peltonova lopatica) i nosi oznaku T3.**
Mjesto: `u10:1025–1056` (`task-mlaz-na-pomicnu-plocu`, str. 202) i `u10:219–295`
(`ex-peltonova-lopatica-u-gibanju`, str. 189–191).
Opis: Postupak je korak po korak isti kao u P1: kontrolni volumen prati tijelo,
$\dot m_{rel}=\rho A(v-u)$, $F_x$, $P=F_xu$, energijska provjera s apsolutnom izlaznom brzinom
i optimum $u$. Razlikuju se samo kut ($90^\circ$ umjesto $165^\circ$) i optimum jedne ploče
($u=v/3$) umjesto kola ($u=v/2$). Pitanje 5 („zašto ne sav protok sapnice”) odgovoreno je
već u P1, `u10:250`. Provjera P1 izrijekom spominje i okomitu ploču (`u10:294`).
U poglavlju je to jedino mjesto T3, a od studenta ne traži izbor ni spajanje modela. Tako se
krši pravilo K15 i pravilo autorskog ugovora da zadatak ne smije biti riješeni primjer s drugim
brojevima.
Prijedlog: zamijeniti Z5 zadatkom koji zahtijeva stvarnu odluku T3. Primjeri: mlaz na
nagnutu ploču, gdje treba podijeliti protok na dvije grane iz bilance u smjeru ploče;
lopatica s trenjem, gdje se bira između energijskog i impulsnog pristupa; kolica koja mlaz
ubrzava, gdje treba odlučiti o nestacionarnom kontrolnom volumenu.
Alternativa je zadržati zadatak, prebaciti ga u T2 i pronaći drugo mjesto za T3.

### P2

**P2-1. Ključ za pog. 10, Z3: nedostaje odgovor na treći zahtjev.**
Mjesto: `G3_kljuc.pdf` str. 346 (F.11 Z3); izvor `u10:985`.
Opis: Izvorni kontrolni rezultat završava rečenicom: „Račun u vodoravnoj ravnini dao bi
$F_z\approx-4{,}97$ kN … stvarna okomita komponenta oko 3 % veća.” U ključu tiskane
knjige ta rečenica nedostaje. Odsječeno je točno iza „5,8 % okomite komponente.”
Student koji radi iz PDF-a nema provjeru za zahtjev 3 („koliko bi se $F_z$ promijenio …”).
Kršenje K8: isti rezultat mora postojati u rješenju i u ključu.
Prijedlog: provjeriti generator ključa. Rez je možda nastao na sekvenci `\,\%`.
Zatim obnoviti dodatak F i usporediti ga sa svim kontrolnim rezultatima.
Moj račun: $p_{M2}=150\,000-998\cdot9{,}81\,(0{,}40+0{,}1255)=144{,}86$ kPa.
$F_z=-(257{,}3+4550{,}9+293{,}7)=-5101{,}9$ N.
Vodoravni (pogrešni) račun daje $-(257{,}3+4712{,}4)=-4969{,}7$ N.
Omjer je 1,027, što se slaže s izvorom.

**P2-2. Pog. 12, Z3 obrće P3 s istim podatcima, pa je glavni rezultat već tiskan.**
Mjesto: `u12:589–617` (`task-poiseuille-inverzni`, str. 241) prema `u12:237–257`
(`ex-laminarni-mikrokanal`, str. 235).
Opis: Z3 ima iste $D=0{,}50$ mm, $L=0{,}20$ m, $Q=0{,}30$ mL/min i $\Delta p=652$ Pa kao P3.
P3 polazi od $\mu=1{,}0$ mPa s i u provjeri navodi $Re\approx12{,}7$. Z3 traži upravo
$\mu$ i $Re$, pa student oba broja čita iz primjera. Novi je samo proračun nesigurnosti.
Prijedlog: promijeniti fluid ili podatke, primjerice ulje ili glikol s
$\mu\approx 5$–$20$ mPa s i drugim $\Delta p$. Zadržati strukturu nesigurnosti i
dominantni doprinos promjera ($4s(D)/D$).

**P2-3. Pog. 9: Z2 i Z4 vježbaju istu odluku kao P4.**
Mjesto: `u09:271–299` (`ex-priguseni-ventil`, T2), `u09:540–567`
(`task-zrak-za-upucivanje-motora`, T1) i `u09:599–625` (`task-priguseni-protok`, T2).
Opis: Sva tri zadatka traže isti postupak: usporediti apsolutni $p_b/p_0$ s 0,528, primijeniti
@eq-priguseni-protok i paziti na apsolutni tlak. Zamku manometarskog tlaka P4 već obrađuje
u provjeri (`u09:298`). Z2 je P4 s drugim brojevima i jednim dijeljenjem $t=m/\dot m$, a
nosi nižu razinu (T1) od istovrsnog primjera (T2). Zbog toga oznake razine nisu dosljedne.
Prijedlog: zadržati jedan od Z2 i Z4. Drugi zamijeniti zadatkom koji mijenja vrstu
razmišljanja, na primjer pražnjenjem boce uz pad $p_0(t)$ (kvazistacionarno, uz vrijeme do
prestanka zagušenja) ili silom mlaza na izlazu zagušene sapnice s tlačnim članom
$(p_e-p_b)A_e$. Drugi primjer usput povezuje pog. 9 s pog. 10 (vidi P3-13).

**P2-4. Pog. 11, P6 (Mach) ponavlja pog. 9, P2.**
Mjesto: `u11:661–711` (`ex-u14-machov-i-strouhalov-broj-stlacivost-i-vrtlozno`, str. 222–223)
i `u09:108–133` (`ex-odabir-modela-kompresibilnosti`, str. 171).
Opis: Oba primjera imaju zračni vod promjera 80 mm i protok oko $0{,}4\ \text{m}^3/\text{s}$.
Oba računaju $v=Q/A$, $Ma$ i usporedbu s 0,3 te povećani protok. U pog. 9 dobiva se
$Ma=0{,}244/0{,}317$, a u pog. 11 $Ma=0{,}234/0{,}468$. Kršenje K10.
Prijedlog: u pog. 11 Mach-dio zamijeniti pitanjem sličnosti, na primjer koliku brzinu traži
model u zraku pri $Re_m=Re_p$ i nastaje li pritom problem s $Ma$ (vidi P3-10). Druga je
mogućnost samo uputiti na pog. 9.

**P2-5. Pog. 12, P4 (zahtjev 3) doslovno ponavlja izračun $C_F$ iz pog. 11, P2.**
Mjesto: `u12:306` i `u12:326–333` (`ex-granicni-sloj-trupa-modela`, str. 237) te `u11:466–478`.
Opis: Isti $Re_m=1{,}08\cdot10^7$ i $Re_s=1{,}35\cdot10^9$ daju iste $C_{F,m}=2{,}96\cdot10^{-3}$
i $C_{F,s}=1{,}48\cdot10^{-3}$. Zaključak o $\lambda_L^3$ također je isti. Kršenje K10.
Prijedlog: zahtjev 3 zamijeniti uputom na pog. 11 („$C_F$ iz primjera 11.2”). Umjesto
njega usporediti laminarni $C_F=1{,}328/\sqrt{Re_L}$ s turbulentnim na istom modelu. Tako se
izravno vidi zašto je stimulator potreban.

**P2-6. Pog. 11 nema stvarnu odluku T3: P5 i Z5 ponavljaju gotov postupak.**
Mjesto: `u11:590–641` (`ex-u14-buckinghamova-analiza-otpora-kugle-i-krivulja-cd`, T3),
`u11:224–253` (izvod „Otpor kugle daje $C_D(Re)$”), `u11:173–183` (tablica 11.1 i njezino
tumačenje) te `u11:889–917` (`task-u14-frekvencija-otpustanja-vrtloga…`, T3).
Opis: Buckinghamova analiza kugle provedena je u poglavlju tri puta: u tumačenju tablice,
u izvodu i u P5. P5 dodaje samo $Re$ i $F_D=C_D\tfrac12\rho v^2A$. Z5 ponavlja isti postupak
za $f$ i pritom zadaje ponavljajuće varijable. Izbor ili spajanje modela ne postoje, pa je
oznaka T3 previsoka (K15). P5 krši i K10.
Prijedlog: P5 skratiti na upućivanje na izvod, a zadržati provjeru $\Pi_1=C_D\pi/8$ i granicu
krize otpora. Z5 učiniti pravim T3: izostaviti popis varijabli, uvesti hrapavost ili blizinu
stijenke i tražiti da student sam odluči koje grupe zadržava. Druga je mogućnost označiti
Z5 kao T2.

**P2-7. Pog. 11, P6: $St\approx0{,}2$ za dimnjak proturječi vlastitoj ogradi teksta.**
Mjesto: `u11:668` i `u11:698–710`, `u11:107`, tablica `u11:154`.
Opis: Tekst kaže da je $St$ reda 0,2 „za kružni cilindar u određenom subkritičnom
području”. Za dimnjak je $Re=vD/\nu=12\cdot2/1{,}5\cdot10^{-5}=1{,}6\cdot10^6$ pri 12 m/s i
$8\cdot10^5$ pri rezonantnih 6 m/s. Oba su izvan subkritičnog područja. Rezultat je
inženjerski prihvatljiv (norme za vjetar rabe $St\approx0{,}18$ za kružni presjek bez obzira na
$Re$), ali čitatelj vidi proturječje. Kršenje K9.
Prijedlog: u tekstu P6 izračunati $Re$ i navesti da je $St=0{,}2$ zadana projektna
vrijednost (uz izvor ili oznaku nastavne procjene), a ne posljedica subkritičnog režima.

**P2-8. Pog. 10, P7: pogrešan naziv „snaga mlazova”.**
Mjesto: `u10:857` (`ex-rotirajuca-mlaznica-pranje-tanka`, str. 201).
Opis: $\dot m(w^2-u^2)/2\approx440$ W nije snaga mlazova. To je hidraulička snaga dovoda
izražena u rotirajućem sustavu, s centrifugalnim članom. Apsolutna kinetička snaga mlazova
iznosi $\dot m(w-u)^2/2=369$ W. Zbroj $369+71{,}3=440{,}4$ W daje upravo
$\dot m(w^2-u^2)/2$, jer vrijedi $(w-u)^2/2+u(w-u)=(w^2-u^2)/2$. Rečenica „ostatak odnosi
mlaz” je točna, ali samo ako se 440 W tumači kao predana snaga.
Prijedlog: „Kočena snaga (71 W) mali je dio snage koju voda predaje glavi,
$\dot m(w^2-u^2)/2\approx440$ W; ostatak, $\dot m(w-u)^2/2\approx369$ W, odnosi mlaz prema
stijenci tanka.”

**P2-9. Pog. 12, uvod: netočna tvrdnja da je zakon viskoznosti poseban slučaj NS jednadžbe.**
Mjesto: `u12:3` (str. 228).
Opis: „Njezin [Navier–Stokesove jednadžbe] je najjednostavniji poseban slučaj zakon
viskoznosti iz pog. 2.” Newtonov zakon viskoznosti je poseban slučaj konstitutivne
relacije @eq-newtonska-konstitutivna-relacija, a ne jednadžbe gibanja. Izvod na `u12:95` to
kaže ispravno. Najjednostavniji poseban slučaj NS jednadžbe bio bi Couetteov tok.
Prijedlog: „Newtonski zakon viskoznosti iz pog. 2 poseban je slučaj konstitutivne veze
koja u nju ulazi.”

**P2-10. Pog. 11: tablica bezdimenzijskih brojeva nema broj, a upućuje se na nju opisno.**
Mjesto: `u11:143–155` (str. 212).
Opis: „Tablica sažima sve brojeve …” upućuje na tablicu bez potpisa i bez ID-a. U PDF-u
jedina numerirana tablica je 11.1 (dimenzijska matrica). Kršenje K12.
Prijedlog: dodati potpis i `{#tbl-bezdimenzijski-brojevi}` te upućivati s
„Tablica [-@tbl-…]”.

**P2-11. Pog. 11: dodatak A u PDF-u je ispisan kao „pog. A”.**
Mjesto: `u11:143`; PDF str. 212: „u skraćenom obliku nalazi se i u pog. A Sažetak formula i
oznaka”.
Opis: Ručno upisani `<span class="mf1-ch-ref"><span class="mf1-ch-code">dod. A</span>…` u
PDF-u postaje „pog. A”. Kršenje K1: dodatak se piše „dodatak A–F”.
Prijedlog: upotrijebiti isti mehanizam upućivanja kao drugdje („dodatak A”, pog. 12 piše
„u dodatku D”) ili ispraviti adapter za `mf1-ch-ref` kod dodataka. Provjeriti i ostala
poglavlja.

**P2-12. Pog. 10, uvodna slika: oznaka presjeka 1 stoji na krivom mjestu.**
Mjesto: `u10:9–11` (`fig-uvod-u11`, slika 10.1, str. 184).
Opis: Broj „1” stoji iznad vrha zavoja, oko dvije petine duljine vodoravnog kraka od ulaza.
Ulazni presjek (isprekidana crta i strelica $p_{M1}A_1$) nalazi se na lijevom rubu. Čitatelj
može pomisliti da je presjek 1 na početku zavoja. Kršenje K6 i K13. Presjek 2 je ispravno
označen. Uz to strelica $F_G$ izlazi iz točke na unutarnjoj stijenci i završava ispod cijevi.
Prijedlog: pomaknuti „1” uz ulazni presjek. Hvatište $F_G$ staviti u fluid, a ne na stijenku.

**P2-13. Pog. 11, slika 11.4: os tlaka je pogrešno označena i nečitljiva.**
Mjesto: `u11:494` (`fig-u14-val3-venturi`, str. 218).
Opis: Oznake osi „50” i „0” preklapaju se na istoj visini („50 0”), a isprekidana linija $p_v$
leži na toj razini. Mjerilo zato nije jednoznačno: ne vidi se je li $p_v$ na 0 ili na 50 kPa.
Natpisi „$p_2$ prema modelu” i „izvan jednofaznog modela” prekrivaju krivulju. Kota
„$D_2=20$ mm” prelazi stijenku difuzora. Brojčana poruka (model daje $p_2=-78{,}8$ kPa)
time se gubi. Kršenje K13.
Prijedlog: osi dati jednake razmake (100; 50; 0; −50; −100), staviti $p_v=2{,}34$ kPa
neposredno iznad 0, a natpise premjestiti izvan krivulje.

**P2-14. Pog. 11: ista oznaka $a$ za širinu kanala i brzinu zvuka; $b$ ima tri značenja.**
Mjesto: `u11:764` (Z1: $a=0{,}400$ m, $b=0{,}200$ m), `u11:860` (Z4: $a_m=340$ m/s,
$b$ raspon), `u11:796` (Z2: $b=2{,}00$ m širina), `u11:116–122` ($Ma=v/a$).
Opis: Unutar istog poglavlja i iste slike 11.8 oznaka $a$ znači duljinu i brzinu zvuka.
Kršenje K6.
Prijedlog: u Z1 pisati $B\times H$ ili $a_k$, $b_k$, ili $s_1$, $s_2$.

**P2-15. Blokovi „Granica modela” u pog. 10 i 11 premašuju K11.**
Mjesto: `u10:122–133` (četiri natuknice i rečenica, str. 186–187); `u11:300–304`.
Opis: Pog. 10 nabraja četiri pretpostavke s objašnjenjima, što je nastavak teorije. Pog. 11
u istom bloku uvodi metodu ITTC 1978, faktor oblika $1+k$ i razlikovanje oznake $k$ u jednoj
rečenici od oko 60 riječi (K3).
Prijedlog: u pog. 10 natuknice premjestiti u tekst ispred bloka, a u bloku ostaviti dvije
rečenice („Model zanemaruje … ; ne smije se zaključivati …”). U pog. 11 napomenu o
$1+k$ premjestiti u tekst.

**P2-16. Pog. 10, CFD odlomak iznosi rezultat neprovedene usporedbe.**
Mjesto: `u10:95` (str. 186).
Opis: „Usporedba oštrog i blažeg koljena pri istom dotoku pokazuje da manji gubitak ne
jamči jednako povoljno opterećenje nosača.” Takva usporedba nije provedena ni navedena
izvorom. Kršenje K9.
Prijedlog: „… može pokazati …” ili „treba provjeriti pokazuje li …”.

**P2-17. Pog. 12: kratica GCI nigdje nije objašnjena.**
Mjesto: `u12:683–706` (Z6), `u12:747` (ishod 4).
Opis: GCI se rabi kao zahtjev („$GCI\le0{,}50\,\%$”) i kao ishod učenja, ali puni naziv
(Grid Convergence Index, indeks mrežne konvergencije) i izvor (Roache; ASME V&V 20) nisu
navedeni. Kršenje K5. Formula postoji samo u naputku, koji je u PDF-u skriven.
Prijedlog: u odjeljku „Što provjeriti” (`u12:481`) jednom rečenicom definirati GCI i
uputiti na dodatak D.

### P3

**P3-1. Nečitljivi natpisi na slikama (K13).**
- Sl. 10.2, str. 189: natpis $F_x$ je djelomično prekriven obrisom lopatice.
- Sl. 10.7, str. 198: „y” stoji iznad crteža, odvojen od osi.
- Sl. 10.9, Z6, str. 204: „$p_{M3}=0$” preklapa koordinatne osi, a „$D_3=80$ mm” preklapa
  izlaz grane.
- Sl. 10.9, Z5: „u” je dijelom pod šrafurom ploče.
- Sl. 10.9, Z1 (str. 203): „$v_j$” je pod krmenom stijenkom.
- Sl. 11.5: „d” je unutar kapi.
- Sl. 11.7: „v = 12 m/s” zalazi u dimnjak.
- Sl. 12.2, Z4: „y = 0; donja ploča miruje” prekriva šrafuru.

**P3-2. Pog. 11, We≈12 pripisan Whiteu.**
Mjesto: `u11:91` i `u11:549`.
Opis: Prag $We\approx12$ za aerodinamički raspad kapi obično se navodi prema eksperimentalnoj
literaturi o raspadu kapi (npr. Pilch i Erdman). Nisam siguran da White (2011) navodi tu
vrijednost. Ovaj priručnik nisam mogao provjeriti, pa nalaz označavam kao nesiguran (K14).
Prijedlog: provjeriti stranicu u Whiteu. Ako je nema, navesti izvor u dodatku E ili tvrdnju
označiti kao nastavnu procjenu.

**P3-3. Pog. 11, P4: tumačenje $Bo$ za kap u struji.**
Mjesto: `u11:587`.
Opis: „$Bo\approx1$ znači da gravitacija još utječe na statički oblik kapi.” Kap koja slobodno
leti u struji nema statički oblik određen težinom. Deformaciju određuje aerodinamički tlak,
a $Bo$ s $g$ ima smisao za kap koja visi ili leži, odnosno za kap u terminalnom padu.
Prijedlog: „$Bo\approx1$ znači da kap te veličine ni u mirovanju ne bi bila kuglasta; u struji
je deformacija određena prije svega s $We$.”

**P3-4. Pog. 10, nespretne formulacije.**
Mjesto: `u10:71` i `u10:207`.
Opis: Na `u10:71` piše: „vrijedi $\alpha\ge\beta^{3/2}$, pa su oba veća od jedan”. Iz
nejednakosti ne slijedi $\beta>1$; to slijedi iz Jensenove nejednakosti ($\beta=\langle u^2\rangle\ge1$).
Na `u10:207` piše: „Dva mlaza čije se sile poništavaju mogu stvarati moment ako im krakovi
nisu jednaki ili su usmjereni suprotno.” Sile koje se poništavaju već su suprotne; moment
nastaje ako im pravci djelovanja nisu kolinearni.
Prijedlog: preformulirati obje tvrdnje.

**P3-5. Razine nekih zadataka ne odgovaraju odluci.**
- Pog. 11, Z2 (`u11:792–820`, T1): zahtjev 3 je odluka o sustavu jedinica, što je definicija
  T2.
- Pog. 12, Z2 (`u12:560–587`, T1): ravnoteža sila, $y^+$ i usporedba s Hagen–Poiseuilleom
  traže usporedbu modela.
- Pog. 12, P6 (`ex-stepenica-mjerenje-cfd`, T3): to je usporedba s mjernim podatcima, dakle
  po definiciji T4.

Ništa od toga ne zahtijeva zamjenu. Navodim to jer bi oznaka trebala odgovarati odluci, a
ne duljini računa (K15).

**P3-6. Naputci rješavaju zadatak (K15).**
Mjesto: `u09:586` (Z3: daje $L/t_{AB}=a+v$, $L/t_{BA}=a-v$ i postupak), `u10:916` (Z1: daje
konačni omjer učinkovitosti), `u12:697` (Z6: sve formule).
Prijedlog: naputak svesti na usmjerenje („U kojem sustavu signal ima brzinu $a$?”).

**P3-7. Pog. 12, Z6 spaja dva nepovezana problema i navodi putanju repozitorija.**
Mjesto: `u12:683` („iz `data/cfd/poiseuille_laminar`”, vidljivo i u PDF-u, str. 242) i
`u12:685`.
Opis: Dio a) (GCI za Poiseuilleov protok) i dio b) (validacija $C_D$ za NACA 0012) dva su
zadatka u jednom mjestu T4. Putanja u repozitoriju nema značenja za čitatelja tiska (K1, K5).
Prijedlog: putanju zamijeniti uputom na dodatak D. Razmotriti da se b) prebaci u
dodatak D kao primjer.

**P3-8. Nedefinirane kratice.**
- ITTC nije raspisan ni u pog. 11 ni u pog. 12.
- NPSH se pojavljuje na `u11:541` prije pog. 13.
- „VL” na sl. 10.9, Z1 nije objašnjen.
- „KV” stoji na `u10:9` prije definicije na `u10:38`.

Prijedlog: raspisati pri prvoj uporabi ili uputiti na dodatak B (K5).

**P3-9. Naslovi prvih odjeljaka ponavljaju naslov poglavlja.**
Mjesto: `u11:15` („11.1 Dimenzijska analiza i sličnost”), `u12:15` („12.1 Diferencijalni opis
realnog toka”).
Opis: K4 traži da naslov imenuje temu odjeljka. Pog. 11 uz to ima blok „Fizikalno značenje”
od jedne rečenice (`u11:42`), koja ponavlja uvod (`u11:5`); kršenje K10.
Prijedlog: preimenovati odjeljke (npr. „Svrha bezdimenzijskog opisa”, „Od integralne do
lokalne bilance”), a jednorečenični blok obrisati.

**P3-10. Pog. 11, uvodna slika: $Re_m=Re_p$ za model automobila.**
Mjesto: `u11:9–11`.
Opis: Za model automobila u mjerilu 1 : 4 u zraku, $Re_m=Re_p$ traži četiri puta veću
brzinu. Pri 30 m/s to je oko 120 m/s, odnosno $Ma\approx0{,}35$. Slika prikazuje sličnost
kao lako ostvarivu. To je dobra prilika za pouku o nespojivosti dviju grupa.
Prijedlog: u potpisu ili tekstu dodati rečenicu o granici $Ma$ ili o rasponu u kojem $C_D$ ne
ovisi o $Re$.

**P3-11. Pog. 11, Z3: brzina na usisu crpke.**
Mjesto: `u11:828`.
Opis: Brzine od 4 i 8 m/s na usisu crpke znatno su veće od uobičajenih (oko 1–3 m/s).
Riječ je o nastavnom modelu, ali K16 traži vjerodostojnu radnu točku.
Prijedlog: navesti da je presjek suženje ispred radnog kola ili smanjiti brzine i prilagoditi
$p_M$.

**P3-12. Pog. 12: tvrdnje o prijelazu i o difuzoru bez izvora.**
Mjesto: `u12:337` i `u12:659–673`.
Opis: Na `u12:337` stoji „Prirodni prijelaz približno između $3\cdot10^5$ i $3\cdot10^6$”
bez izvora (K9, K14). Na `u12:659–673` (Z5) kontrolni rezultat bi bio jači uz usporedbu
$m=-0{,}0667$ s Falkner–Skanovom granicom odvajanja $m\approx-0{,}090$
($\beta_{FS}=-0{,}1988$). Zadani gradijent iznosi oko 74 % praga odvajanja, pa slučaj nije
blizu Blasiusovog.
Prijedlog: dodati izvor (Schlichting) i jednu rečenicu u kontrolni rezultat.

**P3-13. Nedostajuće poveznice s nastavkom studija.**
1. Pog. 9 najavljuje da se sila mlaza računa u pog. 10 (`u09:7`). Pog. 10 obrađuje samo
   nestlačive mlazove. Nema nijednog primjera potiska s tlačnim članom $(p_e-p_b)A_e$
   (preekspandirana sapnica iz P6 u pog. 9 bila bi prirodan nastavak).
2. Pog. 12, P2 (uljni film) računa samo brzinu u sredini procjepa. Inženjerski važan izlaz za
   klizni ležaj (lajtmotiv `u12:7`) jest smično naprezanje na pomičnoj ploči i snaga trenja
   po površini. Prijedlog: dodati jedan redak $\tau(H)$ i $P/A=\tau(H)\,u$.

**P3-14. Sitnice u zapisu.**
- `u11:611`: „pa nastaju $\Pi=5-3=2$ grupe” upotrebljava $\Pi$ kao broj.
- `u09:137`: „ranije obrađenoga kruga s kapljevinom” nema broj poglavlja (K12).
- `u12:368`: „$Re$ iz prethodnog poglavlja” bez broja (K12).
- `u12:434`: CFD vrijednosti sa šest do sedam znamenaka. Ondje su opravdane jer točke
  CFD-a leže na razmaku $0{,}02H_s$. Rečenicu „zaokružene samo na pet do sedam značajnih
  znamenaka” bolje je zamijeniti kratkim obrazloženjem.

## Brojčana provjera (moj račun)

Sve vrijednosti izračunane su skriptom u `M/rad/g3s/racun.py`, uz $\kappa=1{,}4$ i
$R=287$ J/(kg K) gdje je zadano.

| Mjesto | Izvor | Moj račun |
| --- | --- | --- |
| pog. 9 P1 | 343 m/s; 0,248 s | 343,1; 0,2477 |
| pog. 9 P2 | $Ma=0{,}244$; 0,317 | 0,2435; 0,3166 |
| pog. 9 P3 | $T_0=293{,}3$ K; $p_0=83{,}8$ kPa; 24,6/28,8 kPa | 293,3; 83,84; 24,65/28,84 (−14,5 %) |
| pog. 9 P4 | 0,0700 kg/s; 317 kPa | 0,07001; 316,9 |
| pog. 9 izvod | $\Delta s=+94$ J/(kg K) | 93,9 |
| pog. 9 P5 | $Ma_2=0{,}577$; 4,50 | 0,5774; 4,500 |
| pog. 9 P6 | 0,397/1,935; 448,5/70,7 kPa; 297 kPa; 0,117 kg/s | 0,3970/1,9353; 448,5/70,66; 296,96; 0,1167 |
| pog. 9 P6 (val pri 350 kPa) | $A_x/A^*=1{,}39$; $Ma_1=1{,}75$; $0{,}833p_0$ | 1,391; 1,755; 0,8326 |
| pog. 9 Z2 | 0,850 kg/s; 2,94 s | 0,8501; 2,941 |
| pog. 9 Z3 | 50; 350; 304,9 K; 0,143 | isto |
| pog. 9 Z4 | 4,226 bar; $Ma_e=0{,}848$ | 4,226; 0,847 |
| pog. 9 Z5 | 42,50 mm²; 0,0672; 0,885 | 42,50; 0,06721; 0,8853 |
| pog. 9 Z6 | $2{,}000\pm0{,}007$; $0{,}7209\pm0{,}0032$; $0{,}7204\pm0{,}0079$; 0,050 | 2,000 ± 0,0068; 0,72087 ± 0,00319; 0,72045 ± 0,00788; 0,0502 |
| pog. 10 P1 | 35,3 kg/s; 1248 N; 14,98 kW; 2080 N; 26,0 kW | 35,27; 1248,2; 14,98; 2080; 26,0 |
| pog. 10 P2 | 37,0 L/s; 16,4 kPa; 445 N | 37,02; 16,42; 445,3 |
| pog. 10 P3 | −1402/665 N; 1552 N; $\xi=0{,}34$ | −1402,6/665,0; 1552,3; 0,337 |
| pog. 10 P4 | 4,48/10,01 m/s; −891/503 N; 1023 N | 4,481/10,012; −891,3/502,6; 1023,2 |
| pog. 10 P5 | 11,99 m/s; 48,6 kPa; 913 N; 43,2° | 11,994; 48,66; 913,6; 43,2 |
| pog. 10 P6 | $I=9827$ N; 4,91/8,51 kN | 9826; 4,913/8,509 |
| pog. 10 P7 | 11,4 N m; 71 W; 12,5 N m; 680 min⁻¹ | 11,36; 71,3; 12,45; 681 |
| pog. 10 Z1–Z5 | vidi ključ | sve se slaže (npr. Z3: $F_x=4{,}970$, $F_z=-5{,}102$ kN) |
| pog. 10 Z6 | 2835,8/−44,0 N; max 2918,3 N pri (190 kPa; 39,2 L/s; 0,57) | 2835,8/−44,0; 2918,3 na istom rubu |
| pog. 11 P1–P6 | 7200/45; 0,383 m/s; $2{,}96/1{,}48\cdot10^{-3}$; −78,8 kPa; 4,45 L/s; 0,543; 31,3; 1,22; 15,5 m/s; 76,3 mN; 0,177; 0,234/0,468; 0,513 m³/s; 1,2 Hz; 6 m/s | sve se slaže |
| pog. 11 Z1–Z6 | vidi ključ | sve se slaže (Z2: 1,002 m/s; 2,21/3,29 ft/s; Z6: presjek [219,2; 221,4] kN) |
| pog. 12 P1–P6 | 10,5 m/s²; 1,125 m/s; 652 Pa; 2,04 mm; 0,087 m; 51 s⁻¹; 1,59 m²/s³; $X_r$ 6,279/6,543 | 10,5; 1,125; 651,9; 2,041; 0,0870; 51,1; 1,590; 6,2787/6,5435 |
| pog. 12 Z1–Z6 | vidi ključ | sve se slaže (Z6: $GCI_{sr}=1{,}238$ % prema 1,237 % je zaokruživanje) |

Dimenzijsku homogenost provjerio sam za @eq-priguseni-protok, @eq-aktuatorski-disk-potisak,
@eq-moment-kolicine-gibanja, Manningovu jednadžbu i @eq-poiseuille-fvm-celija. Sve su
homogene. Svi redovi veličine su vjerodostojni.

## Napomena o materijalu

Datoteka `G3_kljuc.pdf` sadrži stranice 346, 347 i 348 po dva puta. Vjerojatno je to
artefakt izdvajanja, a ne greška knjige. Nisam to mogao provjeriti na cijelom PDF-u, pa
nalaz ne ubrajam.

## Što je posebno dobro

- Dosljedno razlikovanje $\vec R_{st\to f}$, $\vec F=-\vec R_{st\to f}$ i reakcije nosača
  $\vec R$ u pog. 10. Na svakoj slici piše na koje tijelo sila djeluje. Predznaci u svim
  primjerima su točni.
- Pog. 9 dosljedno inzistira na apsolutnom tlaku i pokazuje brojčanu posljedicu pogreške
  (P4). P6 s režimima konvergentno-divergentne sapnice potpun je i točan, uključujući
  položaj vala pri 350 kPa.
- Izvodi su kratki i provjerivi. Primjeri su Prandtlova relacija s argumentom entropije,
  aktuatorski disk, $\beta$ i $\alpha$ te put od Cauchyjeve do Navier–Stokesove jednadžbe uz
  navedenu posljedicu svake pretpostavke.
- T4 zadatci (pog. 9 Z6, pog. 10 Z6, pog. 11 Z6, pog. 12 Z6) uče pravu inženjersku
  odluku iz podataka i nesigurnosti. Pritom jasno razlikuju zajamčene granice od
  standardnih nesigurnosti.
- Pog. 12 razdvaja numeričku konvergenciju od validacije na stvarnim podatcima
  (Driver–Seegmiller, CFL3D). CFD odlomci uglavnom opisuju pitanje, ulaze i provjeru,
  a ne izmišljene rezultate.
- Primjene iz brodogradnje (vodomlaz, aktuatorski disk, model u bazenu, stimulator
  turbulencije, zrak za upućivanje) vjerodostojne su po dimenzijama i radnim točkama.

Ova procjena je autorska procjena recenzenta. Brojčane provjere su izvršene. Didaktičku
korisnost zamjena treba potvrditi studentski pilot.
