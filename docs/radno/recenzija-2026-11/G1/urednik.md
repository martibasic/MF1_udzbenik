# Urednički i lektorski pregled — poglavlja 1–4

Datum: 8. 11. 2026. Uloga: urednik i lektor (uputa `.claude/skills/recenzija-prirucnika/references/urednik.md`).

Gradivo: `source/u01_…`, `u02_…`, `u03_…`, `u04_…` (pročitani cijeli), PDF G1 (knjiga str. 12–88, tekstno izvučen i
djelomično vizualno provjeren), `docs/konvencije_pisanja.md`, odjeljci „Tekst”, „Notacija i nazivlje” i „Odluke završne
recenzije” iz `docs/urednicki_stil.md`, izlaz `prirucnik_stats.py --nalazi` i `--nacrt`.

Alat je našao 5 nalaza (K3: u03:160, u04:181, u04:413; K12: u03:821, u04:232). **Svih pet potvrđujem**; uvršteni su u
tablice. Fiziku nisam procjenjivao osim gdje jezik mijenja tvrdnju. Poznate stavke iz zadatka (ključ, „primjer N.M”,
skriveni „Provjeri sebe”, nazivi bilježnica) nisu ponovno prijavljene.

## Pog. 1 — Osnove fluida i Pascalov zakon

| Mjesto | Pravilo | Sadašnji tekst | Prijedlog | Težina |
| --- | --- | --- | --- | --- |
| u01:3–7, 44, 62, 111–121, 249, 822–823 | K10 | Uvod donosi ρ, γ, s_r, p=F_n/A, Δp=F₁/A₁=F₂/A₂, A₁s₁=A₂s₂ i F₁s₁=F₂s₂, koje zatim izvode odjeljci i izvod. „Tlak je skalarna veličina” stoji u r. 5, 44, 249 i 823. Definicije u sažetku (r. 822) gotovo doslovno prepisuju r. 62. | Uvod zadržati kao pitanje i model bez formula (formule ostaju u izvodu, eq. 1.x). Drugu rečenicu r. 5 izbaciti jer je r. 44 nosi. Natuknicu r. 822 sažeti, a ne prepisati r. 62. | P2 |
| u01:141 | K4 | „Granica modela — Kada stlačivost utječe na pomak klipa?” | „Granica modela — Utjecaj stlačivosti na pomak klipa” | P2 |
| u01:169 | K2 | Blok CFD-a pisan je u 1. l. mn. („Možemo zadati”, „primjenjujemo”), a odgovor glasi „…ne potvrđuje veći rad: usporedi i hodove.” | „…ne potvrđuje veći rad: usporedimo i hodove.” | P2 |
| u01:268, 316, 381 (sl. 1.3–1.5) | K13 | Potpis je samo naslov primjera: „Opterećeni klip i tlak u zatvorenom cilindru.”, „Servisna hidraulička dizalica.”, „Dvostruka hidraulička platforma s ručnom crpkom.” | Opisna rečenica koja ne ponavlja `fig-alt`, npr. sl. 1.4: „Hidraulička dizalica: mali i veliki klip povezani uljem, s hodovima obaju klipova.” Sl. 1.3 i 1.5 slično. | P2 |

## Pog. 2 — Viskoznost, površinska napetost i kapilarnost

| Mjesto | Pravilo | Sadašnji tekst | Prijedlog | Težina |
| --- | --- | --- | --- | --- |
| u02:3, 5, 20–23, 44–47, 149, 247, 873 | K10 | τ=μ dv/dy stoji u r. 3, 20, 47 i 149, a h=4σcosθ/(ρgd) u r. 5 i 247. Tvrdnja „konstitutivni model, a ne opći zakon” ponavlja se u r. 3, 23, 44 i 873. | Uvod bez formula. U r. 23 izbaciti „To nije univerzalni zakon za sve fluide, nego model…”: tvrdnja ostaje u izvodu (r. 44) i sažetku. | P2 |
| u02:176 | K3 | „Ručni račun u primjeru [-@ex-u02-smicno…] daje takav test:”. Riječ „takav” nema prethodnika jer se test prije ne spominje. | „Ručni račun u primjeru [-@ex-u02-smicno…] daje referentni test za takav CFD model:” | P2 |
| u02:333, 625, 780 prema 441, 464, 843–844 | K7 (dosljednost) | „nadtlak” i „pretlak” stoje za isti pojam. | Posvuda „pretlak” (r. 333: „Isti pretlak 2σ/r…”, r. 625: „…koju vanjski pretlak mora svladati”, r. 780: „…bez pretlaka od oko 189 Pa”). | P2 |
| u02:340 | K12 | „…a njihov omjer kasnije opisuje Weberov broj.” | „…a njihov omjer opisuje Weberov broj ([]{.mf1-chapter-ref target="u11"}).” | P2 |
| u02:346 | K3 | Granica modela najavljuje „četirima pretpostavkama”, a slijede četiri rečenice s točkom-zarezom, od kojih dvije imaju 38–40 riječi. | Uvodna rečenica i numerirani popis četiriju stavki (newtonski model; Couetteov profil; statički meniskus; hidrostatički član kapljice). Tekst stavki ostaje nepromijenjen, uključujući (Z5) i (Z6). | P2 |
| u02:445, 459, 464, 484, 851, 857 | K6 (hrvatski indeksi) | $h_{cap}$ ima engleski indeks. | $h_{kap}$, po uzoru na $\sigma_{kav}$ i $h_g$. Uskladiti i ključ, skicu, bilježnicu i verifikator ako koriste oznaku. | P2 |

## Pog. 3 — Hidrostatička raspodjela tlaka i manometrija

| Mjesto | Pravilo | Sadašnji tekst | Prijedlog | Težina |
| --- | --- | --- | --- | --- |
| u03:3–5, 65, 160, 184–195, 830 | K10 | Uvod donosi dp/dz, p=p_pov+ρgh, p_M, p_aps, h_p, pravilo hoda i dvije manometarske formule. R. 65 gotovo doslovno ponavlja r. 3 („atmosferski u otvorenom, … tlak plina $p_{pl}$ u zatvorenom spremniku”). $p_{vak}$ je zadan u zagradi r. 190, a odmah zatim jednadžbom r. 195. Pravilo „silazak +ρgΔh, uspon −” stoji u r. 5, 160 i 830. | Uvod bez formula. Zagradu „($p_{vak}=p_{atm}-p_{aps}$)” u r. 190 izbaciti jer ostaje jednadžba r. 195. Drugu polovicu r. 5 o hodu kroz stupce izbaciti jer ostaje r. 160. | P2 |
| u03:149, 190, 834 | K9, K10 | R. 149 kaže „Najčešća je pogreška uzeti atmosferu kao nulu…”, r. 190 „…jedna od najtipičnijih pogrešaka”, a sažetak (r. 834) kao najčešću navodi drugu pogrešku. Druga rečenica r. 149 (piezometarska visina) nije povezana s prvom. | R. 149: „Česta je pogreška uzeti atmosferu kao nulu i kad za to nema fizikalnog opravdanja.” Rečenicu premjestiti na kraj r. 147, a „Iz manometarskog tlaka…” ostaviti kao zaseban odlomak. Zadnju rečenicu r. 190 izbaciti. | P2 |
| u03:160 | K3 (alat) | Jedna rečenica od 45 riječi sadrži četiri koraka. | „U praksi je dovoljno držati se jednoga slijeda:” i zatim popis: 1. odabrati jednu referentnu točku ili jednu poznatu vrijednost tlaka; 2. kretati se kroz stupce fluida u jednom dosljednom smjeru; 3. pri silasku dodavati ρgΔh, a pri usponu oduzimati isti član; 4. na istoj vodoravnoj razini istog mirujućeg fluida izjednačiti tlakove. | P2 |
| u03:143–211 | K4 | Odjeljak „Otvoreni i zatvoreni spremnici” obuhvaća i piezometre, manometarski hod i reference tlaka. Manometrija, dio naslova poglavlja, nema vlastiti odjeljak. | Prijedlog autorici: ispred r. 160 umetnuti „## Manometri i reference tlaka” s novim ID-jem, bez diranja postojećih ID-jeva. | P2 |
| u03:68, 156, 189; u04:40, 95 | Urednički stil (obrazac „Vrsta — Podnaslov”) | Naziv bloka je samo „Fizikalno značenje”, dok blokovi u pog. 2 imaju i podnaslov. | Primjeri: „— Gradijent tlaka i težina fluida”, „— Piezometarska visina”, „— Apsolutni, manometarski i vakuumski tlak”; u pog. 4 „— Efektivno polje sila” i „— Radijalni i okomiti gradijent tlaka”. | P2 |
| u03:166 | K5 | „…jednak ručnom računu $\rho_{mv} g(T-H_{tk})$”. Oznake $T$ i $H_{tk}$ definiraju se tek u primjeru r. 468. | „…jednak ručnom računu $\rho_{mv} g(T-H_{tk})$ iz primjera [-@ex-u03-balastni-tank-broda-tlak-iznutra-i-izvana], s gazom $T$ i visinom tanka $H_{tk}$.” | P2 |
| u03:206 | K4 | Podnaslov CFD bloka glasi „**Što znači nizak tlak na usisu?**”, a ostali su izjavni. | „**Nizak tlak na usisu i referenca tlaka.**” | P2 |
| u03:243, 249, 442, 448 | K8 | Međurezultati imaju previše znamenaka: 132506,532 Pa; 31706,532 Pa; −20483,28 Pa; 80816,72 Pa. | $1{,}325\cdot10^5$ Pa; $3{,}171\cdot10^4$ Pa; $-2{,}048\cdot10^4$ Pa; $8{,}082\cdot10^4$ Pa. Konačni rezultati (132,5; 31,7; −20,5; 80,8 kPa) ostaju isti. | P2 |
| u03:329 | Jasnoća | „…tlak veći u vodu slatke vode.” („u vodu” se može pročitati i kao akuzativ.) | „…tlak veći u vodu sa slatkom vodom.” | P2 |
| u03:459 | K5 | „…usporedba $NPSH_a$ s proizvođačevim $NPSH_r$”: kratica nije definirana i nema upućivanja. | „…usporedba raspoložive kavitacijske rezerve $NPSH_a$ s potrebnom $NPSH_r$ koju daje proizvođač ([]{.mf1-chapter-ref target="u13"})…” | P2 |
| u03:534, 538 | K5 | „IoT senzor”: engleska kratica pojavljuje se dvaput i nije objašnjena. | Naslov: „…i umreženi senzor za otkrivanje propuštanja”. R. 538: „Umreženi tlačni senzor u nižem čvoru $A$…”. Ako se kratica zadrži, uvesti je kao „(engl. *Internet of Things*, IoT)”. | P2 |
| u03:712 | K7 (vodoravno, ne horizontalno) | „…nagib postaje osjetljiv na horizontiranje” | „…nagib postaje osjetljiv na vodoravno postavljanje instrumenta” | P2 |
| u03:817–821 | K12 (alat), raspored | „…s relativnim mirovanjem u sljedećem poglavlju.” Most prema pog. 4 sa slikom 3.8 stoji iza zadataka, a ispred sažetka. Sadržaj ponavlja r. 95 i uvod pog. 4. | „…s relativnim mirovanjem u []{.mf1-chapter-ref target="u04"}.” Autorici predložiti da sliku 3.8 premjesti uz r. 95 ili izostavi. | P2 |

## Pog. 4 — Relativno mirovanje fluida

| Mjesto | Pravilo | Sadašnji tekst | Prijedlog | Težina |
| --- | --- | --- | --- | --- |
| u04:223 | K5, K12 | „…zanemaruje se u spremnicima znatno širima od kapilarne duljine iz []{pog. 2}.” Pog. 2 nigdje ne definira kapilarnu duljinu: nema ni pojma ni oznake. | Ne predlažem preformulaciju jer bi promijenila tvrdnju. Upućivanje vodi na nepostojeću definiciju. Autorica bira: definirati kapilarnu duljinu u pog. 2 (granica modela ili uz Bondov broj) ili ovdje dati pojam s definicijom. | P1 |
| u04:1, 3–7, 17–25, 68–72, 859 | K10 | $\Delta h=aL/g$ dvaput je istaknuta kao zasebna numerirana jednadžba (r. 23 i r. 71), a ponavlja se i u uvodu i u sažetku. R. 19 gotovo doslovno ponavlja r. 1 („kao kruto tijelo, bez … smičnih naprezanja … statički problem”). Uvod donosi i ∇p, tanθ, $a=v_s^2/R_z$, paraboloid i $(h_C+h_R)/2=h_0$. | R. 21–25 bez istaknute jednadžbe: „…slobodna površina ostaje okomita na $\vec g_{eff}$; razliku razina na krajevima pravokutnog spremnika izvodimo u nastavku.” Uvjet „dok nema prelijevanja ni ogoljavanja dna” premjestiti uz r. 71. R. 19 izbaciti, a uvod ostaviti bez formula. Prije brisanja provjeriti upućivanja na `eq-…-fizikalni-uvod-i-matematicki-izvod-01`. | P2 |
| u04:7, 232, 307 | K10, K12 (alat) | Rečenica da integraciju tlaka u silu obrađuje pog. 5 stoji triput; r. 232 kaže „…obrađuje sljedeće poglavlje.” | Rečenicu u r. 232 izbaciti jer je pokrivaju r. 7 i r. 307. Ako ostaje, napisati „…obrađuje []{.mf1-chapter-ref target="u05"}.” | P2 |
| u04:179 | K4 | „Matematički izvod — Zašto Coriolisova sila nestaje u relativnom mirovanju” | „Matematički izvod — Coriolisova sila u relativnom mirovanju” | P2 |
| u04:181 | K3 (alat) | Rečenica od 41 riječi navodi tri člana. | „Kad spremnik rotira, puni izraz za prividne sile u neinercijskom (rotirajućem) okviru sadrži tri člana:” i zatim natuknice: centrifugalna sila …; Eulerova sila …, koja iščezava pri konstantnoj kutnoj brzini; **Coriolisova sila** …, koja djeluje samo kad fluid ima brzinu u rotirajućem okviru. | P2 |
| u04:413 | K3 (alat) | Rečenica od 44 riječi. | „U stvarnom zavoju brod se osim toga nagne. U okviru tanka kutu nagiba slobodne površine tada se dodaje kut poprečnog nagiba broda ili se od njega oduzima, ovisno o tome naginje li se brod prema van ili prema unutra. Pomak tekućine pritom mijenja stabilitet, što obrađuje []{pog. 6}.” | P2 |
| u04:305 (sl. 4.3) | K13 | Potpis je samo naslov primjera: „Zatvoreni servisni modul s kosom inspekcijskom stijenkom.” | „Ubrzani zatvoreni modul: kosa stijenka AB postavljena okomito na nagnutu slobodnu površinu.” | P2 |

## Zajedničko za sva poglavlja

| Mjesto | Pravilo | Sadašnji tekst | Prijedlog | Težina |
| --- | --- | --- | --- | --- |
| Sva `mf1-chapter-ref` upućivanja, npr. u01:5 (PDF str. 12), u01:562, u03:7 | K12, čitljivost | PDF ispisuje „Porast tlaka s dubinom obrađuje se u pog. 3 Hidrostatička raspodjela tlaka i manometrija.” Naslov u nominativu stoji bez razgraničenja usred rečenice, pa sintaksa puca (npr. „iz pog. 3 Hidrostatička … :”). | Za tekuću rečenicu ispisivati samo „pog. 3” ili „pog. 3 („Hidrostatička raspodjela tlaka i manometrija”)”. Promjena je u prikaznom adapteru, izvori ostaju isti. | P2 |

## Nalazi P3 (skupno)

1. **Dosljednost nazivlja (oko 20 pojava).** Usporedo stoje konstantan i stalan (u03:46, 95, 101; u04:52, 181), radijus i polumjer (u04:96, 111) te mjehurić i mjehur (u02:279, 282 prema 310). „Izotermalan” bi trebao biti „izotermni” (u03:99–133, 633–644). „Generalizacija” bi trebala biti „poopćenje” (u03:73), a „maksimalnu” „najveću” (u02:589). „Kapljevina” stoji uz „tekućina” (u03:190), a „pretvornik” uz „mjerač” (u03:385).
2. **Oznake koje se sudaraju s tablicom uredničkog stila (9 mjesta, sve lokalno definirane).** To su $k$ kao omjer (u01:514, u04:831), $\alpha$ kao kut (u03:694), $G$ kao točka u plinu (u03:663) i indeks $m$ za mjehur i za izmjereno (u02:722, u03:339). Tu su još $p_u$ za unutarnji tlak uz $\rho_u$ za ulje (u02:284), $z(r)$ i $h(r)$ za istu plohu (u04:114/120), $H$ za karakterističnu visinu i za visinu spremnika (u03:124) te indeks $v$ za paru u Youngovoj jednadžbi (u02:190).
3. **Oznake napomena uz skice.** U upotrebi su „Uz skicu.” (u01:88), „Veza s proračunom.” (ostali primjeri) i „Tumačenje skice.” (u03:821). Naslovi panela na skicama vježbi razlikuju se od naslova zadataka (sl. 1.7: „Provjera proračuna”, „Mjerni cilindar”; sl. 2.7: „Procjep između dvaju limova”, „Mjerenje vučne sile”).
4. **Mehanički nacrt u uvodu.** Rečenica „Poglavlje redom obrađuje/izvodi…” ponavlja se u u01:9, u02:7, u03:7 i u04:7.
5. **Interpunkcija.** Zarez ispred „jer” iza glavne rečenice (u02:868, u03:166). Koraci se naslovljuju s „–” u u03:494–519, a s „—” u u02:833–835. Duga crtica u tekućem tekstu stoji u u02:159, 167, 208 i 286.
6. **Duge rečenice ispod praga alata (35–40 riječi).** Mjesta su u01:581 i u02:85, 90; podjela je po izboru.
7. **Sitni izrazi.**
   - u02:100: „Disk polumjera R aksijalnog ležaja” → „Disk aksijalnog ležaja, polumjera R,”
   - u02:149: „viskozno dodatno” → „dodatno viskozno”
   - u02:169: „1D problemima” → „jednodimenzijskim problemima”
   - u02:577: „znak je za uzbunu” → „upozorava na kvar”
   - u03:157: „manometarski pretlak” je pleonazam
   - u04:823: „Tih 5 % zadana je” → „Tih 5 % jest zadana”
8. **Kratice i upućivanja (K5).** PDMS se pojavljuje samo dvaput (u02:585), pa ga treba pisati punim nazivom. Uz Re (u02:85) treba uputiti na pog. 11.
9. **K8 u kontrolnim rezultatima.** U u04:811 (0,45291 m; 72,91 mm) i u04:843 (0,35268 m) ima više znamenaka nego što K8 propisuje. To je opravdano ako se uspoređuju milimetri.
10. **Izvan uredničkog opsega, za didaktičkog recenzenta.** Granica modela u u01:143–159 ima 7 rečenica i formulu, a u u02:346 i u03:200 po 5 rečenica (K11 traži 1–3). Naputci u01:799, u02:851 i u04:664 daju cijeli postupak (K15).

## Tri najčešća obrasca

1. **Ponavljanje (K10).** Uvod svakog od četiriju poglavlja sažima cijelo poglavlje s formulama. Iste formule i tvrdnje zatim se ponavljaju u odjeljku, izvodu, okviru i sažetku (npr. „tlak je skalaran” 4×, Δh=aL/g kao dvije numerirane jednadžbe).
2. **Neujednačeni nazivi blokova i opisi slika.** „Fizikalno značenje” stoji bez podnaslova (5×). Napomena uz skicu ima tri različita naziva. Četiri potpisa samo ponavljaju naslov primjera. Naslovi okvira postavljeni su kao pitanja (u01:141, u04:179, u03:206).
3. **Pojam ili upućivanje bez definicije ili broja (K5, K12).** Primjeri su kapilarna duljina, NPSH, IoT, oznake $T$ i $H_{tk}$ uporabljene prije definicije, te „sljedeće poglavlje” i „kasnije”. Uz to dolazi i prikaz `chapter-ref` koji upleće naslov poglavlja u rečenicu.

## Ograničenja

- Ovo je autorska procjena urednika, a ne dokaz kvalitete.
- PDF je pregledan tekstnim izvlačenjem i jednim slikovnim isječkom. Skice nisu pojedinačno vizualno provjerene.
- Prijedlozi koji brišu istaknute jednadžbe (u04:23) traže provjeru upućivanja na njihove ID-jeve.
- Prijedlozi koji mijenjaju oznake ($h_{cap}$) traže usklađivanje ključa, bilježnice i verifikatora.
- Nijedna datoteka osim ovog izvještaja nije mijenjana.
