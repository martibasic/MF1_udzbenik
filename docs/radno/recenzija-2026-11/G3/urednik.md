# Urednički i lektorski pregled: poglavlja 9–12

Neovisno čitanje 8. 11. 2026. Pregledani su izvori `source/u09_…`–`source/u12_…`
i PDF izvadak G3 (knjiga str. 169–244). PDF je čitan tekstualnim izvlačenjem
(PyMuPDF, pdftotext), a ne vizualno. Uz čitanje su pokrenuti
`prirucnik_stats.py` (profil), `--nalazi` i `--nacrt`. Fizika nije ocjenjivana.
Ovo je urednička procjena, a ne dokaz kvalitete. Prijedlozi čuvaju brojeve,
uvjete i ograde. Gdje to nije moguće, problem je samo opisan.

Nalazi alata: pet nalaza (u11:303, u11:796, u12:139, u12:366, u12:368). Svih
pet je potvrđeno i nalazi se u tablicama.

## Pog. 9 — Kompresibilni idealni tok

| Mjesto | Pravilo | Sadašnji tekst | Prijedlog | Težina |
| --- | --- | --- | --- | --- |
| u09:3, 5, 7, 17 → 106, 132, 170, 460 | K10 | Uvod ponavlja tvrdnje iz kasnijih dijelova poglavlja. Rečenica „granica $Ma<0{,}3$ korisna je inženjerska heuristika” (r. 3) gotovo je jednaka r. 106. Skokovi kroz val „$p_2>p_1$ … $p_{02}<p_{01}$ … $T_{02}=T_{01}$” (r. 5) ponavljaju se u r. 170, 452 i 717. Rečenica „Model pretpostavlja kalorički savršen plin sa stalnim $\kappa$, jednolike veličine …” (r. 7) gotovo je jednaka GM-u u r. 460. Izraz „pri velikoj brzini ili velikoj promjeni tlaka” stoji u r. 1 i u r. 17. Podatak „4,4 %” stoji u r. 106 i u r. 132. | Uvod neka pojave samo imenuje, bez nejednakosti, i neka uputi na jednadžbe. Rečenicu o pretpostavkama u r. 7 treba izbrisati jer GM u r. 460 sadrži sve te pretpostavke. U r. 132 treba izbrisati „Pri $Ma=0{,}3$ izentropska promjena gustoće iznosi oko 4,4 %;”, jer broj ostaje u r. 106. U r. 17 izraz zamijeniti s „Kod brzog toka plina …”. | P2 |
| u09:106, 362 | K7 | „kaloričkoga savršenog plina” | „kalorički savršenog plina”: *kalorički* je ovdje prilog, kao u r. 144. | P2 |
| u09:137, 139 | K12 | „Za razliku od ranije obrađenoga kruga s kapljevinom …”; „… u Venturijevoj cijevi s vodom nije bila potrebna” | „Za razliku od rashladnog kruga s kapljevinom iz []{.mf1-chapter-ref target="u07"} …”; „… u Venturijevoj cijevi s vodom iz []{.mf1-chapter-ref target="u08"} …” | P2 |
| u09:445 | K3 (jasnoća) | „iteracija, koja nadilazi ispitnu razinu, smješta val …” | Izraz „ispitna razina” je nejasan: ne vidi se misli li se na ispit ili na razinu primjera. Prijedlog: „iteracija, zahtjevnija od razine ovog primjera, smješta val …”. Autorica potvrđuje značenje. | P2 |

## Pog. 10 — Količina i moment količine gibanja

| Mjesto | Pravilo | Sadašnji tekst | Prijedlog | Težina |
| --- | --- | --- | --- | --- |
| u10:1, 3, 5, 27, 36 → 77–86 | K10 | U r. 3 je cijela jednadžba $\vec F_p+\vec F_G+\vec R_{st\to f}=…$ s definicijama svih članova, a r. 77–86 je ponovno uvode. Isti se smisao ponavlja u r. 1 („… daju brzine i tlakove, ali ne i tu silu”) i u r. 36 („… ali ne i reakciju konstrukcije”). Treći Newtonov zakon pojavljuje se u r. 1, 5 i 27. | U uvodu jednadžbu napisati riječima i uputiti na jednadžbu [-@eq-momentum-matematicki-izvod-koeficijent-kolicine-gibanja-i-03]. Rečenicu u r. 36 skratiti na „Tek vektorski zapis daje istodobno smjer, predznak i iznos reakcije.” U okviru u r. 27 izbrisati rečenicu o trećem zakonu. | P2 |
| u10:74 | K3, K12 | „No taj oblik nije dovoljan …” stoji iza okvira izvoda, pa nije jasno na koji se oblik odnosi. | „No oblik iz jednadžbe [-@eq-momentum-numericki-trag-01] nije dovoljan …” | P2 |
| u10:452 | K12, K2 | „usporedi s CFD odlomkom u odjeljku [Provjera sile na cijevno koljeno](#…)” (PDF str. 25 izvatka: naslov napisan riječima) | Odjeljku u r. 91 dodati ID (npr. `{#sec-u10-provjera-koljena}`). Tekst: „Usporedbu donosi odlomak *Računalna dinamika fluida* u odjeljku [-@sec-u10-provjera-koljena].” Rješenje je tako u prvom licu množine ili u bezličnom obliku. | P2 |
| u10:708 | K7 | „pa proračunati režim zadovoljava” | „pa proračunani režim zadovoljava” (trpni pridjev, kao *izračunan-*) | P2 |
| u10:1064 | K5 | „To nisu standardne nesigurnosti za RSS.” Kratica nije uvedena u pog. 10. | „To nisu standardne nesigurnosti, pa se ne zbrajaju korijenom zbroja kvadrata.” | P2 |
| u10:1062, 1070; u11:945 | K7, K6 | „Nominalni protok”, „nominalne protoke”, a u istom zadatku stoji $R_{naz}$. U pog. 11: „nominalna sila”. | „Nazivni protok”, „nazivne protoke”, „nazivna sila” (usklađeno s $R_{naz}$ i s „nazivnom površinom” u pog. 9). | P2 |

## Pog. 11 — Dimenzijska analiza i sličnost

| Mjesto | Pravilo | Sadašnji tekst | Prijedlog | Težina |
| --- | --- | --- | --- | --- |
| u11:15 | K4 | „## Dimenzijska analiza i sličnost” jednak je naslovu poglavlja. Odjeljak ima jedan odlomak koji ponavlja uvod. | Naslov ukloniti, a odlomak iz r. 17 spojiti s početkom odjeljka „Dimenzije, jedinice …”. Druga mogućnost je naslov „Svrha bezdimenzijskih grupa”. Stabilni ID ostaje, ako postoji. | P2 |
| u11:3, 5, 42, 131, 267 | K10 | Uvod u r. 3 daje definicije osam brojeva i $n-k$, a sve se ponovno uvode u r. 47–122, u tablici r. 145–155 i u r. 159–165. Rečenica „Jednaka vrijednost (samo) jedne grupe nije dovoljna” stoji u r. 5 i u okviru r. 42. Popis „relativna hrapavost, $Ma$, slobodna turbulencija i blizina stijenke” stoji u r. 5 i u r. 131. Nespojivost $Fr$ i $Re$ ponavlja se u r. 5, 267 i 477. | Uvod neka brojeve samo imenuje, bez formula. Okvir u r. 42 izbrisati ili ga zamijeniti tvrdnjom koje nema u uvodu: on i ne pripada odjeljku o dimenzijama. Popis ostaviti u r. 131, a nespojivost u okviru u r. 267. | P2 |
| u11:34 ↔ 276, 295 | K6 | $F_p\sim\Delta p\,L^2$ označuje mjerilo tlačne sile (r. 34, 47), a $F_p/F_m$ silu prototipa (r. 276, 295). | U r. 34 i 47 pisati $F_{\Delta p}$. | P2 |
| u11:107 | K7 | „u određenom subkritičnom području Reynoldsova broja” | „u određenom potkritičnom području Reynoldsova broja” | P2 |
| u11:122 | K7, K6 | „a $K$ modul stlačivosti” | „a $K$ volumni modul” (urednički stil; pog. 9, r. 67) | P2 |
| u11:143 | K12 | „Tablica sažima sve brojeve iz ovog poglavlja” stoji uz tablicu bez potpisa i broja (r. 145). | Tablici dodati potpis i ID (`: Bezdimenzijski brojevi i njihovo tumačenje. {#tbl-u11-brojevi}`). Tekst: „Tablica [-@tbl-u11-brojevi] sažima …”. | P2 |
| u11:143 (PDF str. 43 izvatka, knjiga ≈ 211) | K1, K12 | Izvor ima `dod. A`, a PDF ispisuje „u pog. A Sažetak formula i oznaka”. | Popraviti prikaz upućivanja na dodatak, tako da piše „u dodatku A”. Provjeriti i ostala `mf1-ch-ref` upućivanja na dodatke u knjizi. | P2 |
| u11:286, 303, 434, 971 | K5 | Kratica „ITTC 1957/1978” nije razriješena (pet pojava). | Pri prvom spomenu (r. 286): „linijom Međunarodne konferencije pokusnih bazena (engl. *International Towing Tank Conference*, ITTC) iz 1957.” Dalje ITTC. | P2 |
| u11:303 | K3 (alat, 58 riječi) | „Rastavljanje … radna je hipoteza, a ne zakon: trodimenzijski učinci oblika trupa (metoda ITTC 1978 zato uvodi faktor oblika $1+k$; ovdje $k$ označuje …), hrapavost oplate, … ne ulaze u model ravne ploče.” | GM: „Rastavljanje $C_T=C_F(Re)+C_R(Fr)$ radna je hipoteza, a ne zakon: model ravne ploče ne obuhvaća trodimenzijske učinke oblika trupa, hrapavost oplate, stimulatore turbulencije na modelu ni utjecaj slobodne površine na trenje.” Zagradu premjestiti u tekst iza jednadžbe [-@eq-ittc-1957]: „Učinke oblika trupa metoda ITTC 1978 obuhvaća faktorom oblika $1+k$; ovdje $k$ označuje samo dodatak otpora zbog oblika trupa, a ne hrapavost $k_s$ ni turbulentnu kinetičku energiju iz pog. 12.” GM tako ostaje u tri rečenice (K11). | P2 |
| u11:541 | K5 | „… karakteristika početka kavitacije i NPSH.” Kratica se javlja samo ovdje i nije definirana. | „… karakteristika početka kavitacije i kavitacijska rezerva ($NPSH$, []{.mf1-chapter-ref target="u13"}).” | P2 |
| u11:796 | K3 (alat, 44 riječi) | „Za uniformni tok … rabi se empirijska Manningova jednadžba $v=…$, gdje je $R_h=A/P$ …, $S$ …, a $n$ Manningov koeficijent, zadan brojčanom vrijednošću koja vrijedi u sustavu SI.” | „Za uniformni tok u dugom otvorenom kanalu u pog. 15 rabi se empirijska Manningova jednadžba $v=…$. U njoj je $R_h=A/P$ hidraulički radijus (omjer površine presjeka toka i oplakanog opsega), $S$ bezdimenzijski nagib dna, a $n$ Manningov koeficijent, zadan brojčanom vrijednošću koja vrijedi u sustavu SI.” | P2 |
| u11:175–183, 224–253, 590–641 | K10 | Π-analiza otpora kugle izvedena je triput: u tablici s „Tumačenjem matrice”, u izvodu i u koraku 1 primjera T3. | Izvod zadržati. „Tumačenje matrice” skratiti na rang i $n-k$ te uputiti na izvod. U primjeru (r. 611) uputiti na jednadžbu [-@eq-slicnost-matematicki-izvod-otpor-kugle-daje-cd-re-01]. Primjer mijenjati samo ako autorica proširi opseg. | P2 |

## Pog. 12 — Diferencijalni opis realnog toka

| Mjesto | Pravilo | Sadašnji tekst | Prijedlog | Težina |
| --- | --- | --- | --- | --- |
| u12:15 | K4 | „## Diferencijalni opis realnog toka” jednak je naslovu poglavlja. Odjeljak ima jedan odlomak. | „## Od integralne do lokalne bilance” (ID `sec-realni-tok-motivacija` ostaje). | P2 |
| u12:3, 7 → 24, 74, 114, 130, 225, 276 | K10 | Uvod (r. 3) daje materijalnu derivaciju, Navier–Stokesovu jednadžbu i $\vec v=\vec 0$ u obliku istaknutih jednadžbi [-@eq-materijalna-derivacija] i [-@eq-navier-stokes-nestlacivi]. Pretpostavke analitičkih rješenja (r. 7) ponavljaju se u GM-u r. 114 te u r. 225 i r. 276. | U uvodu jednadžbe navesti riječima i uputiti na njih. U r. 7 ostaviti samo „Analitička rješenja vrijede samo uz pretpostavke iz kojih su izvedene.” jer se pojedinosti navode uz svako rješenje. | P2 |
| u12:139 | K3 (alat, 47 riječi) | „Primjerice, u mirovanju … $\partial p/\partial n=\rho g_n$; uvjet „nulti gradijent …” vrijedi samo za tlak iz kojega je hidrostatički dio izdvojen (u OpenFOAM-u …), pa rubni uvjet treba zadati …” | „Primjerice, u mirovanju uz gravitaciju gradijent fizičkog tlaka $p$ okomito na stijenku uravnotežuje težinu, $\partial p/\partial n=\rho g_n$. Uvjet „nulti gradijent tlaka na stijenci” vrijedi samo za tlak iz kojega je hidrostatički dio izdvojen (u programu OpenFOAM $p_{rgh}=p-\rho\,\vec g\cdot\vec x$). Rubni uvjet zato treba zadati za onu varijablu koju rješavač stvarno računa [@greenshieldsweller2022].” | P2 |
| u12:366 | K3 (alat, 45 riječi), K5 | „… kao Reynoldsovo naprezanje $-\rho\overline{v_i'v_j'}$ (RANS, engl. …)”: kratica stoji uz naprezanje, a ne uz jednadžbe. Slijedi duga rečenica „Najčešći su dvojednadžbeni modeli: $k$–$\varepsilon$ … a $k$–$\omega$ SST … uz prijelaz …”. | „… kao Reynoldsovo naprezanje $-\rho\overline{v_i'v_j'}$. Tako osrednjene jednadžbe nazivaju se RANS (engl. *Reynolds-averaged Navier–Stokes*).” Zatim: „Najčešći su dvojednadžbeni modeli. Model $k$–$\varepsilon$ rješava prijenosne jednadžbe za turbulentnu kinetičku energiju $k=\tfrac12\overline{v_i'v_i'}$ i njezinu disipaciju $\varepsilon$. Model $k$–$\omega$ SST (engl. *shear stress transport*) rješava jednadžbe za $k$ i specifičnu disipaciju $\omega$; blizu stijenke koristi oblik $k$–$\omega$, a daleko od nje prelazi na $k$–$\varepsilon$.” | P2 |
| u12:368 | K12 (alat) | „a ne samo o $Re$ iz prethodnog poglavlja” | „a ne samo o $Re$ iz []{.mf1-chapter-ref target="u11"}” | P2 |
| u12:270 ↔ 315, 659, 673 | K6 | Teorija rabi $\delta_{99}\approx5x/\sqrt{Re_x}$, a primjer (r. 315) i Z5 (r. 659, 673) za istu procjenu rabe $\delta_B$. | Svugdje $\delta_{99}$. Druga mogućnost: pri prvom spomenu napisati „$\delta_B$ (Blasiusova procjena $\delta_{99}$)”. | P2 |
| u12:631 | K6 | „pri kojem $\tau_0=\mu v'(0)$ mijenja predznak”: crtica u r. 346 označuje fluktuaciju. | „pri kojem $\tau_0=\mu\,(dv/dy)_{y=0}$ mijenja predznak” | P2 |
| u12:683, 685, 689, 697, 706, 747 | K5 | Kratica GCI javlja se šest puta, a u poglavlju nije razriješena. Definicija je u dodatku D, a formula samo u naputku, koji u PDF-u nije prikazan. | Pri prvom spomenu (r. 683): „indeks mrežne konvergencije (engl. *grid convergence index*, GCI; dodatak D)”. | P2 |
| u12:683 | K1 | „Sintetički Poiseuilleov skup podataka iz `data/cfd/poiseuille_laminar`”: staza repozitorija kodnim fontom vidljiva je i u PDF-u. | „Sintetički Poiseuilleov skup podataka (dodatak D)” | P2 |

Nalaza P0 i P1 nema.

## Nalazi P3 (skupno)

- **Upitni podebljani uvodi u CFD okvirima** djeluju kao naslovi (u duhu K4). Mjesta: u09:203, 303; u11:111, 136; u12:288, 372. Ukupno 6.
- **Opisna upućivanja (K12).** Mjesta: u11:47 „uvedeni u nastavku”, u11:310 „Pitanja u nastavku”, u12:71 „(izvod slijedi)”, u12:120 „Nastavljamo model razdjelnika” (bez pog. 7), u12:477 „na kraju poglavlja”. Ukupno 5.
- **Miješanje glasa (K2).** Drugo lice jednine u okviru pisanom u prvom licu množine: u10:101, u12:234. „Usporedi” u rješenju: u10:452. Imperativ u izlaganju: u11:292. „Označujemo” u tekstu zadatka koji je pisan u drugom licu: u09:663, u12:593. Sažetci miješaju imperativ i izjavne natuknice: u10:1100, u11:968–969. Ukupno 8.
- **Kratice s manje od tri pojave (K5).** RSS (u09:667, u12:600), CFL (u09:454), FVM, FEM i DNS (u12:465, 479, 368). TMR (u12:366) je engleski naziv bez „engl.” i javlja se jedanput. Programi CFL3D, FUN3D i OpenFOAM nisu opisani (u12:434, 685, 139). Ukupno 9.
- **Brojevi (K8).** Popisi bez `\,` iza točke-zareza: u11:953 (5 popisa). Grupiranje tisućica nije ujednačeno: „1\,029”, „8\,798”, „9\,827” (u10:759–762) stoje uz „1402”, „1248”, a „600000”, „40000”, „48600” (u09:285, 440; u10:517, 556, 688) uz „52\,000”, „280\,000”. Ukupno oko 12.
- **Interpunkcija.** Istaknute formule bez završnog znaka: u10:477–498, 611–619, 659, 665 (oko 10). Em-crtica „—” u prozi umjesto crtice „–”: u10:881, 888; u11:21, 38, 168, 259–261, 541 (oko 9).
- **Nazivlje.** „Aksijalne” (u10:302) prema „osni” u istom poglavlju. „Trenutna brzina” (u12:343) prema „trenutačno” (u09:1, 52). Isti blok uz skicu nosi tri naziva: „Uz skicu”, „Uz dijagram” i „Veza s proračunom” (u11:395, 496, 605). Oblici na -oga/-ega stoje uz oblike na -og u istom tekstu, oko 20 puta (npr. u09:137, 463; u11:17, 75, 221; u12:225, 374, 535).
- **Naslovi-pretinci.** „## Riješeni primjeri” postoji samo u pog. 10 i 11 (u10:217, u11:379). Odjeljak „Provjera sile na cijevno koljeno” (u10:91) sadrži i opću granicu modela i lokalni oblik zakona.
- **K13.** Alternativni opis slike gotovo je jednak potpisu: u11:11, 436.
- **Redoslijed.** Napomene uz skice u u10:1095 idu redom Z1, Z3, Z2, Z5, Z6.
- **Neodređena poveznica.** U u12:434 „izvornih datoteka” vodi na README repozitorija, pa u PDF-u nije jasno na što se odnosi.
- **Izvan ovog opsega (K11).** GM u u10:125–132 ima popis od četiri natuknice i dodatnu rečenicu.

## Tri najčešća obrasca

1. **Uvod poglavlja ponavlja tijelo (K10).** U sva četiri poglavlja drugi do četvrti
   uvodni odlomak donose formule, pragove i pretpostavke modela. Iste ih zatim izvode
   odjeljci, okviri „Fizikalno značenje” i blokovi „Granica modela”.
2. **Kratice i oznake bez uvođenja ili s dva značenja (K5, K6).** Kratice: ITTC, GCI,
   RSS, NPSH, RANS. Oznake s dva značenja: $F_p$, $v'$, $\delta_B$ i $\delta_{99}$, $K$
   (modul stlačivosti i volumni modul).
3. **Upućivanja bez broja i naslovi bez vlastite teme (K12, K4).** Upućivanja: „ranije
   obrađenoga”, „prethodnog poglavlja”, „u odjeljku ⟨naslov⟩”, nenumerirana tablica i
   „pog. A” za dodatak. Naslovi: dva odjeljka nose naslov poglavlja, a „Riješeni primjeri”
   je pretinac.

## Ograničenja

PDF nije pregledan vizualno, pa prijelom, formule i skice nisu ocijenjeni. Brojevi u
nalazima o K8 provjereni su samo u izvoru. Bilježnice i ključ (dodatak F) nisu čitani.
Nalazi K10 traže autoričinu odluku o tome koje mjesto ostaje. Prijedlozi koji diraju
riješene primjere (u11:590–641) izvan su dogovorenog opsega izmjena.
