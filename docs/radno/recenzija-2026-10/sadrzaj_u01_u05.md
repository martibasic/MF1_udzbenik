# Sadržajna i didaktička recenzija poglavlja 1–5 (`source/u01…u05*.md`)

Recenzent: sadržajna recenzija (mehanika fluida), 16. listopada 2026.
Pročitano u cijelosti: pet kanonskih izvora, `docs/kurikularna_matrica.md`, `docs/autorski_ugovor.md`,
`docs/urednicki_stil.md` (tablica notacije), lekturni izvještaji `docs/radno/lektura-2026-10/u01…u05*.md`.
Ništa u repozitoriju nije mijenjano.

## 1. Sažetak

Poglavlja 1–5 fizikalno su i matematički točna: svi izvodi (Pascal, Cauchyjev tetraedar, Couette, Young,
kapilarni uspon, Young–Laplace, diferencijalna hidrostatika, Eulerov oblik, izotermalna atmosfera, efektivno
polje, paraboloid i očuvanje volumena, Coriolisov član, rezultanta i centar tlaka, projekcija i pomoćni
volumen) provjereni su korak po korak i ispravni su. Ponovnim računom provjerio sam sve brojčane rezultate
30 riješenih primjera i 30 kontrolnih rezultata Z1–Z6 (ne samo polovinu); nije nađena nijedna brojčana
pogreška, a jedino stvarno netočno mjesto je rečenica u kontrolnom rezultatu Z2 pog. 5 (već zabilježena u
lekturi). Razina izlaganja primjerena je drugoj godini: svaki ishod iz matrice ima izvod, primjer s
provjerom, konceptualno pitanje, samostalni zadatak i blok „Granica modela”. Glavna su slabost ponavljanja:
isti rezultat izriče se u uvodu, u „Temelju”, u izvodu, u blokovima „Fizikalno značenje” i u sažetku
(pog. 3 i 4 osobito), a u svakom poglavlju barem dva riješena primjera ili primjer i zadatak ponavljaju iste
studentske odluke (pog. 2: P3 ≡ Z6; pog. 4: P1 ≡ P5; pog. 1: P5 ≈ P6; pog. 5: P5 ≈ P6). CFD blokovi su
konkretni, točni i nepretenciozni; tvrdnje o brodogradilišnoj i strojarskoj praksi odgovaraju stvarnosti.
Preostali nalazi su nedosljednosti oznaka prema tablici u `docs/urednicki_stil.md`, strukturne sitnice
(prazne uvodne sekcije, naslov „Zadaci za samostalan rad” samo u pog. 5) i nekoliko jezičnih ostataka.
Procjena spremnosti: sadržaj je spreman za završetak nakon ispravka dvaju–triju P1 nalaza i odluke
autorice o kraćenju navedenih ponavljanja; nijedan nalaz ne traži nov sadržaj.

Legenda: „potvrđeno iz lekture” = nalaz već postoji u `docs/radno/lektura-2026-10/`, ovdje samo
potvrđen i po potrebi precizno formuliran; „novo” = nalaz koji lektura nije zabilježila; „dojam” = autorska
procjena, ne provjerljiva činjenica.

## 2. Nalazi po prioritetu

### P1 — ispraviti prije završetka

| # | Gdje | Što | Zašto je problem | Prijedlog |
|---|---|---|---|---|
| 1 | `u05` r. 745, Z2 kontrolni rezultat (potvrđeno iz lekture) | „Provjera: $F_x$ i $F_z$ ne poništavaju momente ni oko jedne točke, za razliku od kružnog luka.” | Fizikalno netočno: svaki ravninski sustav sila ima pravac rezultante, a oko svake točke na njemu moment je nula. Recenzent bi to odmah zamjerio. | Prije → poslije: „Provjera: za razliku od kružnog luka, normale parabole nemaju zajedničku točku, pa ne postoji unaprijed poznata točka s nultim momentom; $M_A$ zato treba računati iz obiju komponenata i njihovih krakova.” Brojevi ostaju. |
| 2 | `u05` r. 83, izvod „Rezultanta na ravnoj plohi”, Provjera (potvrđeno iz lekture) | „Za vodoravnu plohu ($h_a=h_b=h_C$) oba zapisa daju $F=\rho gh_CA$.” | Integralni zapis r. 77 vrijedi za vertikalni pojas; $h_a=h_b$ znači pojas visine nula, $A=0$. Granični slučaj je formalno nekonzistentan, a student to primijeti. | Zamijeniti provjeru graničnim slučajem koji oba zapisa stvarno dijele: „Za pojas koji počinje na slobodnoj površini ($h_a=0$) integral daje $F=\rho gbh_b^2/2=\rho gA\,(h_b/2)$, što je upravo $\rho gAh_C$ uz $h_C=h_b/2$.” |
| 3 | `u02` r. 321, Young–Laplace, zadnja rečenica (potvrđeno iz lekture) | „za cilindar ($R_2\to\infty$) $\Delta p=\sigma/R$” | Oznaka $R$ nije uvedena u tom izvodu (glavni polumjeri su $R_1$, $R_2$; prema tablici notacije $R$ je polumjer spremnika). Formula s neuvedenim simbolom. | $\Delta p=\sigma/R_1$. |
| 4 | `u02` P3 „Kapilarni mikrodozator s izlaznom kapljicom” (r. 428–503) i Z6 „Kapilarna igla pod tlakom” (r. 831–865) (potvrđeno iz lekture; ovdje izričito označeno kao isti zadatak) | Isti fizikalni problem, isti podatci po vrsti ($d$, $H$, $D$, $\sigma$, $\theta=0$), isti postupak: $h_{cap}$, $p_{M,1}=\max(0,\rho gH-4\sigma/d)$, $p_{M,2}=\rho gH+4\sigma/D$, usporedba s $\rho gD$. Z6 dodaje samo raspon $D$ i izbor regulatora. | Prema AGENTS.md drugi brojevi nisu dokaz raznolikosti; student u Z6 ne donosi nijednu odluku koju već nije pročitao u P3. T4 tako gubi smisao provjere ishoda. | Bez novog sadržaja: skratiti P3 na korake 1–2 (prirodni uspon, Laplaceov skok i apsolutni tlak u kapljici) i u „Provjera i tumačenje” ostaviti samo rečenicu o predznaku zakrivljenosti; korake 3–4 (dva stanja pretlaka) ukloniti, jer ih Z6 traži od studenta. P3 tada postaje T2, a Z6 ostaje T4 s nepromijenjenim brojevima i verifikatorom. Autorska odluka. |

### P2 — vrijedi napraviti

| # | Gdje | Što | Zašto je problem | Prijedlog |
|---|---|---|---|---|
| 5 | `u01` r. 9 i r. 17–21; `u02` r. 7 i r. 17–21; `u03` r. 7 i r. 17–21; `u04` r. 5 i r. 17–21; `u05` r. 7 i r. 28–32 (novo) | U svih pet poglavlja uvod već nabraja primjene (prema uredničkom stilu), a odmah ispod naslova prvog odjeljka slijedi okvir „Inženjerski kontekst” s istim popisom (dizalice, preše, kormilarski pogoni; ležajevi, raspršivači; piezometri, balastni tankovi; autocisterna, centrifuge; brodska vrata, ustave). Prvi H2 odjeljak (npr. „Fluid kao kontinuum”, „Viskoznost i međupovršinske pojave”, „Relativno mirovanje fluida”) sadrži samo tu jednu rečenicu, okvir i „Procijenjeno vrijeme”. | Dvostruko nabrajanje industrija koje urednički stil izrijekom ne želi; prazna sekcija u sadržaju. | Ukloniti okvir „Inženjerski kontekst” u svih pet poglavlja (ili rečenicu u uvodu), a „Procijenjeno vrijeme rada uz priručnik” premjestiti neposredno pod naslov poglavlja, prije uvodnog teksta. Prvi H2 tada se spaja sa sljedećim odjeljkom. |
| 6 | `u03` r. 25–49, r. 51–94, r. 171–173 (novo) | Rezultat $dp/dz=-\rho g$ i $p=p_{pov}+\rho gh$ zadani su u „Temelju” (r. 31, 40, 44) s dva uzastopna okvira „Fizikalno značenje”, zatim slijedi H2 odjeljak „Matematički izvod” koji isto izvodi od početka (r. 53–94, treći put r. 91), a r. 173 isti izraz numerira četvrti put. Naslov „Matematički izvod” kao H2 odjeljak nije informativan u sadržaju (ostala poglavlja izvode drže u okviru `.mf1-izvod`). | Slijed uvod → model → izvod prekinut; student triput čita isto; tri broja jednadžbe za istu formulu. | Spojiti r. 25–49 i r. 51–94 u jedan odjeljak „Diferencijalna jednadžba hidrostatike” (izvod u okviru, zatim radni zapis jednom), spojiti dva okvira „Fizikalno značenje” u jedan, a u r. 171–173 samo uputiti na već numeriranu jednadžbu. |
| 7 | `u04` r. 37 i r. 95–113, r. 115–159 (novo) | Isti obrazac: „## Matematički izvod” kao H2; okvir „Zašto Coriolisova sila nestaje” dolazi prije nego što je rotacija uopće uvedena (paraboloid tek r. 115). Unutar okvira izvoda paraboloida ugniježđena su dva okvira „Fizikalno značenje” (r. 124–127 i r. 155–158); drugi ponavlja r. 153 (dvije rečenice iste provjere). | Student čita o Coriolisovu članu prije nego zna što je kruta vrtnja; okvir u okviru vizualno je težak i ponavlja. | Premjestiti Coriolisov okvir iza izvoda paraboloida (ili ga svesti na dvije rečenice u „Granica modela”, koja ga već spominje). Ukloniti drugi ugniježđeni okvir (r. 155–158). Naslov r. 162 „… — eksplicitan izvod” skratiti. |
| 8 | `u01` r. 7, 134, 151–157, 184–188, 218–240, 833 (novo) | Tvrdnja „sila raste, pomak se smanjuje, rad se čuva, $A_1s_1=A_2s_2$” pojavljuje se šest puta (uvod, Temelj, zasebno numerirana jednadžba r. 154, CFD blok, izvod, sažetak). | Najjednostavnija ideja poglavlja razvodnjena ponavljanjem. | Ukloniti r. 151–157 (jednadžba i odlomak; izvod r. 218–224 ima isto) i u r. 134 ostaviti samo rečenicu o omjeru 35. |
| 9 | `u01` r. 381–391, P3 „Servisna dizalica”, odlomak „Procjena stlačivosti” (novo) | Unutar „Provjera i tumačenje” dodan je drugi mini-primjer s novim podatcima ($V_0$, $K$) i rezultatom 0,0463 %. Ista stlačivost obrađena je u „Granica modela” (r. 159–179), Z4 i samoprovjeri 3. | Ugovor traži da provjera sadrži provedenu provjeru, ne novi račun; stlačivost se vježba četiri puta, a Z4 zapravo ponavlja ovaj odlomak s drugim brojevima. | Skratiti r. 381–391 na jednu rečenicu: „Procjenu stlačivosti za ovaj sustav provodi Z4; ovdje je $\Delta V_c/\Delta V_p\ll1\ \%$.” (ili cijeli odlomak ukloniti). |
| 10 | `u01` P5 „Hidraulička kočnica” (r. 473–551) i P6 „Stezna naprava” (r. 553–604) (novo) | Ista struktura: sila na crpni klip → $p_M$ → $n$ paralelnih cilindara → $F=p_MA$ → skalarni zbroj. P6 dodaje samo usporedbu s $F_{dop}$. Također P2 „Opterećeni klip” i P3 „Dizalica” isti zakon ($p=F/A$, $F_2=pA_2$). U poglavlju pet od šest primjera je lanac $p=F/A\to F=pA$. | Kvaliteta i raznolikost primjera: student ne vidi novu odluku; brojčana provjera „$F_s/F_p=(d_s/d_p)^2$” ponavlja provjeru P5. | Skratiti P6 na zahtjeve 1, 2 i 4 (bez zbroja sila) ili ga ukloniti; poglavlje zadržava 5 primjera, što ugovor dopušta. Dojam: ako se jedan primjer uklanja, bolje je P6 nego P5, jer P5 nosi polugu i Z-samoprovjeru 2. |
| 11 | `u04` P1 „Otvoreni spremnik na laboratorijskim kolicima” (r. 252–296) i P5 „Autocisterna pri kočenju” (r. 505–546); Z1 (r. 648–672) (novo) | P1 i P5 isti su zadatak ($\Delta h=aL/g$, $h_0\pm\Delta h/2$, kut); P5 dodaje pragove prelijevanja/ogoljavanja, Z1 traži isto s provjerom prelijevanja. Translatorni nagib tako se rješava četiri puta (P1, P5, Z1, Z2). | Ponavljanje istih odluka. | Ukloniti P1 (poglavlje zadržava 5 primjera; CFD blok r. 243 upućuje na P5, pa ništa ne puca) ili ga svesti na tri retka u Temelju kao brojčanu ilustraciju bez statusa primjera. |
| 12 | `u05` P5 „Četvrtcilindrični poklopac uz slobodnu površinu” (r. 528–586) i P6 „Zglobni poklopac” (r. 588–656) (novo; dojam) | Ista geometrija (četvrtina valjka koja počinje na slobodnoj površini, $F_H=\rho gbR^2/2$, $|F_V|=\rho gb\pi R^2/4$); P5 ima vodu iznad (smjer dolje), P6 vodu ispod + spojnicu. Uz P4 i Z5 to su četiri četvrtine kruga. | Djelomično ponavljanje; lekcija o predznaku $F_V$ vrijedna je, ali ne treba cijeli primjer. | Zadržati P6; P5 skratiti na „Tekst, komponente s predznakom i provjeru $|F_V|/F_H=\pi/2$” bez $x_V$ i $\theta_R$, ili ga pretvoriti u odlomak „Što se mijenja ako voda kvasi drugu stranu” uz P6. Autorska odluka. |
| 13 | `u05` r. 679 i r. 683 (novo) | Naslov „## Zadaci za samostalan rad” (sva ostala poglavlja 1–4: „Zadaci za vježbu”); slika sa skicama Z1–Z6 i „Napomene uz skice” stoje prije zadataka, a u pog. 1–4 iza njih. | Nedosljednost vidljiva u sadržaju knjige i u ritmu poglavlja. | Ujednačiti naslov na „Zadaci za vježbu” (isti problem ima i pog. 13) i premjestiti sliku iza popisa zadataka kao u pog. 1–4. |
| 14 | `u05` Z2 „Parabolični pokrov suhog kanala” (r. 722–749), oznaka razine (novo) | Označen T1, a traži predznačene komponente, pravce djelovanja, rezultantu i moment oko $A$ za parabolu (čija normala nema zajedničku točku). Z4 „Širina trokutastog poklopca” (T2) traži samo $F=\rho gAh_C\le F_{max}$ i $h_{CP}$. | Razina ne odgovara stvarnim odlukama studenta; matrica 2×T1 ostaje zadovoljena samo ako se oznake zamijene. | Zamijeniti položaje i oznake: trokutasti poklopac kao Z2 (T1), parabolični pokrov kao Z4 (T2). To mijenja redoslijed, pa traži usklađenje SVG oznaka i generatora D06 (strukturni zahvat prema AGENTS.md). |
| 15 | `u03` r. 442 (potvrđeno iz lekture) | „Stupac plina od nekoliko paskala zanemariv je” uz izračunanih 27,2 Pa (r. 434). | Opis ne odgovara broju. | „Stupac plina od nekoliko desetaka paskala …”. |
| 16 | `u03` Z5 (r. 766–772), „Traži se” točka 5 (novo) | „5. Pri ocjeni razmotri samo zadane mjerne zahtjeve.” nije zahtjev nego uputa. | Ugovor: popis „Traži se” sadrži zahtjeve; student traži „što se traži pod 5”. | Premjestiti rečenicu u tekst zadatka iza r. 764; popis ostaje 1–4. |
| 17 | `u02` r. 324–327, okvir „Fizikalno značenje” uz Young–Laplace (potvrđeno iz lekture, dopunjeno) | Okvir od Laplaceova skoka skreće u kavitaciju, $NPSH$ i „tlak koji zatvara mikrokapljicu” (treba „mikromjehurić” ili jezgru). | Okvir „Fizikalno značenje” po ugovoru tumači, ne uvodi nove teme; kavitacija je obrađena u pog. 13. | Zadržati prve tri rečenice; kavitaciju svesti na jednu: „Isti nadtlak $2\sigma/r$ otežava rast vrlo malih mjehurića pare pri kavitaciji (pog. 13).” |
| 18 | `u05` cijelo poglavlje (r. 5, 23, 26, 357, 370, 392, 404) prema `u03` r. 116–119 i `u04` (16 pojava) (novo) | Vektori u pog. 5 pišu se `\mathbf` ($d\mathbf F$, $\mathbf n_f$), u pog. 3 i 4 `\vec` ($\vec g_{eff}$, $\vec a$, $\vec\omega$). Tablica notacije propisuje $\vec v$. | Dva stila vektora u istoj knjizi; u PDF-u podebljano i strelica izgledaju kao različite veličine. | U pog. 5 zamijeniti `\mathbf` s `\vec` (8 mjesta). |
| 19 | Oznake u sukobu s tablicom `docs/urednicki_stil.md` (potvrđeno iz lekture, sabrano): `u01` r. 479 $F_n$ za silu na papučicu (u Temelju $F_n$ je normalna sila); `u01` r. 479–545 indeksi $f$/$r$ (front/rear) i $d_M,A_M,F_M$ uz $p_M$; `u03` r. 498–557 $H_t$ (visina turbine u tablici), $T_g$ (tablica: gaz $T$), $\rho_b$ (ista morska voda $\rho_{mv}$), indeksi ext/int; `u04` r. 388–397 $h_v$, $h_u$ kao vanjska/unutarnja stijenka (tablica: voda/ulje); `u04` r. 786 $s_h$ za raspon očitanja (tablica: $s(x)$ je nesigurnost); `u05` r. 106–115 $h_R$ uz $h_{CP}$; `u05` r. 276, 343 i Z3/Z5 $T$ za silu spojnice (tablica: gaz/temperatura). | Načelo „jedna veličina, jedna oznaka” iz standarda od 12. 10. | Minimalne zamjene: $F_{pap}$; indeksi $pr$/$st$ i $gc$; $H_{tk}$, $T$, $\rho_{mv}$, indeksi $van$/$unu$; $h_{van}$/$h_{unu}$ (i SVG); $R_h$ ili $\Delta_h$; $h_{CP}$; $F_s$ ili $S$ za spojnicu. Uz svaku zamjenu provjeriti pripadni SVG, bilježnicu i verifikator. |
| 20 | `u03` P3 (r. 365–376, 397–403) i P5 r. 549, riječ „ullage” (potvrđeno iz lekture; autorska odluka) | Anglizam bez hrvatske inačice pri prvom spomenu; u hrvatskoj pomorskoj praksi uobičajen je „ulaž” (uz „sondaža”). | Terminološka dosljednost za recenzenta iz brodogradnje. | Pri prvom spomenu: „ulaž (engl. *ullage*), udaljenost od referentne točke do površine tereta”, dalje „ulaž”, „ulažni otvor”, „ulažna vrpca”. |

### P3 — opcionalno

| # | Gdje | Što | Prijedlog |
|---|---|---|---|
| 21 | `u02` P1 „Pretvorba dinamičke u kinematičku viskoznost” (r. 105–137) (novo) | Jedina radnja je $\nu=\mu/\rho$; P2 (r. 389–393) računa isto kao svoju 4. točku. | Ukloniti P1 ili ga svesti na rečenicu u Temelju; poglavlje zadržava 5 primjera. |
| 22 | `u03` P2 „Diferencijalni manometar između slatke i morske vode” (r. 283–356), oznaka T3 (novo; dojam) | Jedan hidrostatički lanac s četiri segmenta; nema izbora modela. Konfiguracija (zračni most od 0,70 m između žive i morske vode) tehnički je neuobičajena. | Oznaka T2; u tekstu dodati pola rečenice da je zračni most nastavna konstrukcija (obrnuti U-krak). |
| 23 | `u03` r. 230–237, CFD blok „Što znači nizak tlak na usisu?” (novo) | „Zastani i promisli” stoji prije naslovnog odlomka bloka, suprotno od ostalih blokova (pitanje slijedi iza tematskog uvoda). | Zamijeniti redoslijed odlomaka. |
| 24 | `u03` r. 827–831, slika „Ravnoteža tlaka i efektivno polje sila” između zadataka i sažetka (novo) | Most prema pog. 4 ponavlja njegov uvod ($\tan\theta=a/g$, $g_{eff}$). | Kandidat za uklanjanje; pog. 4 uvod i slika već to pokrivaju. |
| 25 | `u03` r. 148 `\boxed{…}` (novo) | Jedina uokvirena jednadžba u pog. 1–5. | Ukloniti okvir radi dosljednosti. |
| 26 | `u03` i `u04`: oznake točaka u kodnom fontu (`A`, `P`, `G`, `C`, `D`; npr. `u03` r. 246, 251, 498; `u04` r. 303, 435) prema matematičkom $A$, $B$, $O$ u `u05` (novo) | Dva stila za istu vrstu oznake. | Jedan stil u cijeloj knjizi (preporuka: matematički kurziv). |
| 27 | `u05` r. 159 i 432 HTML komentari „<!-- [NOVA PEDAGOŠKA DOPUNA] … -->”; r. 181 prazno sidro `[]{#verifikacija-cfd-a-ručnim-računom}` s dijakritikom u ID-u; r. 11 inline `style="width:100%;max-width:980px;"` na uvodnoj slici (novo) | Ostatci uređivanja u kanonskom izvoru. | Ukloniti. |
| 28 | `u05` r. 161 i 434 oznake „Numerički pokus — …” na blokovima `.mf1-interaktivno` (pog. 1–4: „Interaktivni prikaz — …”) (novo) | Ugovor razlikuje „Numerički pokus” i interaktivni prikaz; isti tip bloka ima dva imena. | Ujednačiti na „Interaktivni prikaz — ravna ploha / zakrivljena ploha”. |
| 29 | `u05` r. 441–443 bilježnica `u06_zakrivljena_ploha.ipynb` (potvrđeno iz lekture, provjereno) | Sadržaj bilježnice opisuje upravo geometriju pog. 5 (četvrtina valjka, voda na konveksnoj donjoj i lijevoj strani, oznaka „Poglavlje U05”), s općim podatcima $R=0{,}80$, $h_1=1{,}00$, $b=2{,}00$ m, ne s podatcima primjera. Podudarnost fizike je u redu; samo je ime datoteke naslijeđeno. | Informativno; ne dirati bez razloga (QR i poveznice). |
| 30 | Numerirane jednadžbe za podatke i pretvorbe: `u01` r. 77–83 ($g=9{,}81$, $\rho_v=1000$ kao dvije numerirane jednadžbe), `u02` r. 85–91 („$\mu\ [\text{Pa s}]$” kao jednadžba), `u02` r. 367–369 ($\delta=0{,}003$ m), `u03` r. 471–473 (zaokruživanje kao zasebna jednadžba) (novo; dojam) | Numeracija gubi značenje kad svaka pretvorba ima broj. | Zadane vrijednosti pisati u rečenici; ako generator traži ID za svaki prikaz, ostaviti. |
| 31 | `u02` P5 r. 511 (novo; dojam o praksi) | Osovina propelera $D=50$ mm pri $n=2400\ \mathrm{min^{-1}}$ u ležaju statvene cijevi: brzohodni dizelski motori manjih plovila s reduktorom obično daju osovini propelera znatno manje okretaje; procjep 0,30 mm na 50 mm (0,6 %) velik je za uljem podmazan ležaj. Brojevi su nastavni i ne mijenjaju fiziku. | Ako se brojevi ne mijenjaju (D06), dodati „nastavni podatci” već stoji u r. 513 („Ovo je usporedba …”); dovoljno. |
| 32 | `u02` r. 185–201 indeksi $\sigma_{sv}$, $\sigma_{sl}$, $\sigma_{lv}$ (engl. solid/liquid/vapour) (novo) | Tablica traži hrvatske indekse; ovdje su standardni iz literature. | Zadržati uz objašnjenje u zagradi pri prvom spomenu („indeksi: $s$ kruto, $l$ tekuće, $v$ para”), ili $\sigma_{kp}$, $\sigma_{kt}$, $\sigma_{tp}$. |
| 33 | `u02` r. 7 i r. 243 (potvrđeno iz lekture) | Ista rečenica o Weberovu i Bondovu broju dvaput; smjer omjera nakon lekture ispravan ($We=\rho v^2L/\sigma$, $Bo=\rho gL^2/\sigma$: inercija odnosno gravitacija prema površinskoj napetosti). | Ukloniti rečenicu u r. 243. |
| 34 | `u02` r. 169 „Ručni @ex-u02-… daje takav test” (novo; jezik) | Renderira se kao „Ručni primjer 2.x daje…”. | „Ručni račun u primjeru [-@ex-…] daje takav test”. |
| 35 | `u03` r. 125 „$T = T_0$ = konst.” (novo; jezik) | Mješavina matematike i teksta. | $T=T_0=\text{konst.}$ |
| 36 | `u03` r. 175 „(ista oznaka u cijelom priručniku)” (novo) | Urednička napomena u glavnom tekstu. | Ukloniti zagradu. |
| 37 | `u01` r. 7 „…, pa su istisnuti volumeni jednaki, $A_1s_1=A_2s_2$, pa veliki klip prijeđe…” (novo; jezik) | Dva „pa” u nizu. | „…pa su istisnuti volumeni jednaki, $A_1s_1=A_2s_2$: veliki klip prijeđe…”. |
| 38 | `u01` r. 596 „$6\cdot1{,}680\approx10{,}08$”; r. 628 „Zadaci” prema „zadatci”; r. 632 uvod Z1–Z6 prema Z2 s rudom (potvrđeno iz lekture) | — | „=”; „Zadatci za vježbu” (ako se naslov mijenja, u svim poglavljima); uvodu dodati „osim ruda u Z2”. |
| 39 | `u04` r. 58 „nagib slobodne površine $-a/g$” bez osi; r. 421 „pribraja kut nagiba broda” bez ograde o smjeru nagiba (potvrđeno iz lekture) | — | „nagib $dz/dx=-a/g$ za os $x$ u smjeru ubrzanja”; „tom se kutu dodaje ili oduzima kut nagiba broda, ovisno o tome naginje li se brod prema van ili prema unutra”. |
| 40 | `u05` r. 36 (novo) | Rečenica o pretpostavkama modela ponavlja r. 7. | Ukloniti r. 36. |
| 41 | `u01` CFD blok r. 113–118 „Voda ili smjesa vode i glikola?” (novo; dojam) | Najslabiji od 15 CFD blokova: ne vodi do odluke, samo upozorava na unos svojstava; tema pripada pog. 2. | Spojiti s prvim blokom (r. 31–36) u dvije rečenice o svojstvima kao ulaznim podatcima. |
| 42 | `u05` r. 889–899 sažetak kao okvir s natuknicama; pog. 1–4 prozni sažetci (novo) | Ugovor dopušta oboje; dojam o dosljednosti. | Ostaviti ili prepisati u tri prozna odlomka kao u pog. 1–4. |

## 3. Što je dobro i treba ostati

- **Točnost.** Svih 30 primjera i 30 kontrolnih rezultata preračunano i potvrđeno, među ostalim:
  pog. 1 kočnica 4,77 MPa / 4,59 / 3,38 kN, $k\approx53$; Z6 947 kPa, 22,13 kN, 1,551 m.
  Pog. 2 ležaj 579 / 57,9 W; mikrodozator 227 / 707 Pa; Z6 0,555–0,591 kPa, rezerva 8,8 Pa, $\rho gD_{max}=19{,}6$ Pa.
  Pog. 3 sondiranje 15,940 m, $U=2{,}310$ m, 250 i 213 m³, 27,2 Pa; Z5 0,711/0,613/0,0450 m i 8,44/9,79/133,4 Pa; Z6 122,55 / 135,28 / 136,05 kPa → 142,85 kPa.
  Pog. 4 separator 754 rad/s, 6950 $g$, 32,7 bar, $r_i=89$ mm (140 mm pri 950 kg/m³), $t_z\approx14$ s, Coriolis $1{,}5\cdot10^{-4}$; Z6 $\omega_{max}=7{,}830$ rad/s, $k_{max}=0{,}790$, rezerva 2,68 mm.
  Pog. 5 kosi poklopac $y_{CP}=0{,}679$ m; pregrada 48,151 kN, $h_{CP}=1{,}894$ m, $T=32{,}578$ kN; četvrtina kruga 66,67 / 74,28 / 99,81 kN i moment oko O 43,4 = 43,4 kN m; Z2 $-5{,}948$ / $-5{,}287$ kN, $M_A=-8{,}327$ kN m; Z5 $T=0{,}904$ kN; Z6 $z=1{,}74$.
- **Izvodi s provjerom graničnih slučajeva** (Pascal: $A_1=A_2$ i $A_2\to\infty$; Couette: $u\to0$; kapilara: $\theta=90^\circ$; nagnuta ploha: $\theta\to0$; četvrtina valjka: $|F_V|/F_H=\pi/2$) točno su ono što ugovor traži; Cauchyjev tetraedar i tenzor naprezanja ispravno su stavljeni u „Dublje”.
- **Pog. 2 „Granica modela — Newtonski sloj i statički meniskus”** uzorni je blok: četiri pretpostavke, svaka s upućivanjem na zadatak koji je krši. Granice pog. 3–5 jednako su konkretne.
- **CFD blokovi** (15 ukupno) su konkretni, točni i nepretenciozni: $p_{rgh}=p-\rho g h$ i provjera konstantnosti u mirnoj vodi (pog. 3) je točna; usporedba s Hagen–Poiseuilleom prije podjele protoka (pog. 2), test mirne tekućine prije uključenja crpke (pog. 3), razlika okvira cisterne (pog. 4) i integracija $p_i\mathbf n_{f,i}A_i$ (pog. 5) odgovaraju stvarnoj praksi. Niti jedan blok ne prikazuje izmišljene brojeve kao simulaciju. Pitanja „Zastani i promisli” (jedno po poglavlju) imaju stvaran raskorak koji student mora riješiti.
- **Primjeri iz prakse** su vjerodostojni: Rapsonov kormilarski stroj (Z2 pog. 1, s ispravnom napomenom o srednjem položaju), ležaj statvene cijevi, sondiranje teretnog tanka s inertnim plinom i vodenim talogom (pog. 3, P3 — najbolji primjer u cjelini), bočni balastni tank s neto tlakom na oplatu, vodotoranj s IoT senzorom, brodski centrifugalni separator s gravitacijskim diskom (pog. 4, P6; uvjet razdjelnice $r_i^2=(\rho_vr_v^2-\rho_ur_u^2)/(\rho_v-\rho_u)$ i zaključak o izboru diska točni), vodonepropusna vrata naplavljenog odjeljka.
- **T3/T4 zadatci** s dijagnozom modela (pog. 1 Z3 pogrešni proračun, Z4 stlačivost; pog. 2 Z5 newtonski model iz mjerenja; pog. 3 Z5 izbor manometra, Z6 izbor pretvornika; pog. 4 Z5 smirivanje, Z6 tolerancija pretvarača; pog. 5 Z6 nesigurnost) doista mijenjaju vrstu razmišljanja i ne traže formulu unaprijed.
- **Dosljedno razlikovanje** manometarskog i apsolutnog tlaka, iznosa i smjera komponenata ($\operatorname{atan2}$, normala $\mathbf n_f$ iz fluida prema stijenci), te „zajamčena granica ≠ standardna nesigurnost” u svim T4 zadatcima.
- **Sažetci pog. 1–4** su kratki, bez novih tvrdnji, i izrijekom navode što model zanemaruje.

## 4. Što se može ukloniti ili skratiti bez gubitka

1. Okviri „Inženjerski kontekst” u svih pet poglavlja (nalaz 5) — ukupno oko 25 redaka ponavljanja uvoda.
2. `u01` r. 151–157 (jednadžba volumena izvan izvoda) i r. 381–391 („Procjena stlačivosti” unutar provjere P3) — nalazi 8 i 9.
3. `u01` P6 „Stezna naprava” (ili barem zahtjev 3) — nalaz 10.
4. `u02` P1 „Pretvorba viskoznosti” — nalaz 21; `u02` r. 243 druga rečenica o We/Bo — nalaz 33; kavitacijski dio okvira r. 326 — nalaz 17.
5. `u02` P3 koraci 3–4 (ostaju u Z6) — nalaz 4.
6. `u03` dvostruki izvod i treće/četvrto numeriranje $p=p_{pov}+\rho gh$ (r. 25–49 + 51–94 + 173) — nalaz 6; most prema pog. 4 (r. 827–831) — nalaz 24; zagrada u r. 175.
7. `u04` P1 „Laboratorijska kolica” — nalaz 11; drugi ugniježđeni okvir r. 155–158 — nalaz 7.
8. `u05` P5 (ili njegove točke $x_V$, $\theta_R$) — nalaz 12; r. 36; HTML komentari i prazno sidro — nalaz 27.

Ukupno bi to skratilo pet poglavlja za oko 150–200 redaka izvora bez gubitka ijednog ishoda iz matrice;
broj riješenih primjera ostao bi 5–6 po poglavlju, a Z1–Z6 nepromijenjeni (osim zamjene položaja Z2/Z4
u pog. 5 ako autorica prihvati nalaz 14).

## 5. Što je provjereno, a što nije

- Provjereno: izvodi i svi brojčani rezultati (ručno i skriptom u scratchpadu), postojanje citiranih
  ključeva `white2011`, `anderson2021`, `openfoam-hydrostatic` u `references.bib`, sadržaj bilježnice
  `u06_zakrivljena_ploha.ipynb`, raspodjela razina Z1–Z6 (2×T1, 2×T2, T3, T4 u svakom poglavlju), po jedno
  „Zastani i promisli” po poglavlju.
- Nije provjereno: podudarnost SVG skica s tekstom (područje druge recenzije), verifikatori
  `tools/verify_uNN.py`, render PDF-a/weba. Ocjene razine zadataka (nalazi 14, 22) i ponavljanja
  (nalazi 4, 10–12, 21) autorska su procjena, ne rezultat alata.
