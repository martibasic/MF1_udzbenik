Ovaj dodatak povezuje ćelijsku bilancu iz []{.mf1-chapter-ref target="u07"}, analitičke reference iz []{.mf1-chapter-ref target="u08"} i lokalne jednadžbe iz []{.mf1-chapter-ref target="u12"}. CFD približno rješava odabrani model strujanja kada geometrija, rubni uvjeti ili promjene u vremenu otežavaju analitički račun.

**Povezani primjeri kroz knjigu.** Odlomci *Računalna dinamika fluida* prate kako se model mijenja kada se promijeni pitanje. Za usporedno čitanje služe sljedeći nizovi:

| Primjena | Povezani odlomci | Što želimo odlučiti |
|---|---|---|
| Rashladni krug baterije | [početni model](u01_osnove_fluida_i_pascalov_zakon.qmd#cfd-rashladni-krug-model) → [podjela protoka](u07_kinematika_kontrolni_volumen_i_kontinuitet.qmd#cfd-razdjelnik-podjela-protoka) → [mjerenje i gubitak](u08_energijska_jednadzba_i_bernoulli.qmd#cfd-venturi-mjerenje-gubitak) → [toplina](u12_diferencijalni_opis_realnog_toka.qmd#cfd-hladna-ploca-toplina) → [radna točka](u13_gubici_cjevovodi_crpke_i_mreze.qmd#cfd-krug-radna-tocka) → [rotor](u14_turbostrojevi_i_propulzija.qmd#cfd-rotor-karakteristika) | raspored kanala, protoci i pogon |
| Cisterna i ponton | [kočenje i valovi](u04_relativno_mirovanje_fluida.qmd#cfd-cisterna-kocenje) → [gaz i stabilitet](u06_uzgon_plivanje_i_stabilnost.qmd#cfd-ponton-gaz-stabilitet) → [prijenos mjerila](u11_dimenzijska_analiza_i_slicnost.qmd#cfd-ponton-slicnost) | učinak pregrada ili položaja tereta |
| Gradski kanal s ustavom | [sila i moment](u05_hidrostatske_sile_na_plohe.qmd#cfd-ustava-opterecenje) → [vodostaji](u15_otvoreni_tokovi.qmd#cfd-kanal-vodostaji) → [mlaz i skok](u15_otvoreni_tokovi.qmd#cfd-ustava-hidraulicki-skok) | opterećenje pogona i umirni bazen |
| Zračna sapnica | [zagušenje](u09_kompresibilni_idealni_tok.qmd#cfd-sapnica-prigusenje) → [udarni val](u09_kompresibilni_idealni_tok.qmd#cfd-sapnica-udarni-val) | potrošnja zraka i radno područje |

: {.mf1-reference-table tbl-colwidths="[27,46,27]"}

Pri svakom prijelazu provjeri što ostaje pretpostavka, koji podatak treba dodati i koju novu veličinu daje račun.

::: {.callout-tip icon="false"}
## Opseg dodatka {#što-se-ovdje-neće-dogoditi}

**Glavni tekst priručnika** daje fizikalne zakone, pretpostavke i bilance. **Odlomci Računalna dinamika fluida** povezuju ih s konkretnim primjenama i postupnim proširenjem modela. **Dublje** ovdje znači dodatno čitanje, izvan obveznog gradiva kolegija Mehanika fluida 1; izvođenje numeričkih shema i samostalno postavljanje rješavača pripadaju nastavku studija.

Preporučeni redoslijed čitanja: @sec-cfd-mapa → @sec-cfd-polja-izlazi → @sec-cfd-venturi → @sec-cfd-vv-paketi. Prije vlastitog računa vrati se na @sec-cfd-kada-ne-treba.
:::

## Dodatne kratice numeričkih metoda

CFD, FEM, RANS s modelima $k$–$\varepsilon$ i $k$–$\omega$ SST, SIMPLE i PISO, MRF i klizna mreža, rezidual i mrežna konvergencija definirani su u [pojmovniku](d02_pojmovnik.qmd). Ovdje su samo kratice kojih ondje nema. Imaj na umu da se metoda ne bira samo prema nazivu.

| Naziv | Značenje i uloga | Poveznica |
|---|---|---|
| FVM — *Finite Volume Method* | metoda konačnih volumena; povezane bilance ćelija | @eq-celijska-bilanca-mase |
| LES / DNS | razrješavanje velikih / svih relevantnih turbulentnih skala, za razliku od osrednjavanja u RANS-u | @sec-turbulencija |
| VOF — *Volume of Fluid* | opis međupovršine volumenskim udjelom faze; prikaz izoplohe udjela $0{,}5$ samo je način vizualizacije granice | []{.mf1-chapter-ref target="u15"} |
| Zidne funkcije / $y^+$ | model područja uz stijenku / bezdimenzijska udaljenost; zahtjevi ovise o odabranoj obradi stijenke | @sec-turbulencija |
| GCI — *Grid Convergence Index* | procjena diskretizacijske nesigurnosti odabrane veličine iz sustavnog profinjenja | @sec-cfd-vv-paketi |

## Primjeri alata

**OpenFOAM** je primjer alata za rješavanje modela strujanja, a **ParaView** za pregled i obradu polja. Primjerice, OpenFOAM-ova funkcija [`forces`](https://cpp.openfoam.org/v13/classFoam_1_1functionObjects_1_1forces.html) integrira tlačne i viskozne doprinose sili i momentu, a `forceCoeffs` ih normira zadanim referentnim veličinama. Drugi alati isti fizikalni izlaz mogu nazivati, primjerice, *force report*. Jedinice, referentni tlak, obuhvaćene plohe i konvenciju predznaka provjeri u dokumentaciji inačice koju koristiš.

Slika polja pomaže pronaći područje niskog tlaka ili odvajanja, ali se odluka temelji na izračunanoj veličini s procjenom nesigurnosti. Postavke alata proizlaze iz odabranog modela i cilja računa.

## Rječnik priručnik → CFD: prijevod pojmova {#sec-cfd-mapa}

Tablica služi kao središnja mapa: ista jednadžba dobiva prostorni numerički zapis, a polje se zatim svodi na traženi izlaz. Brzina fluida u knjizi označena je s $v$ (vektor $\vec v$, komponente $v_i$); $u$ označuje brzinu krute granice (lopatica, klip), a u turbostrojevima razlikujemo apsolutnu $\vec c$, relativnu $\vec w$ i obodnu $\vec u$. Vanjska brzina graničnog sloja $U_e$ i brzina trenja $u_\tau=\sqrt{\tau_{st}/\rho}$ uvode se uz definiciju.[]{#rječnik-mf1-cfd-prijevod-pojmova}

| Pojam iz priručnika | Jednadžba ili veza | Fizikalno značenje | CFD uloga | Tipičan izlaz |
|---|---|---|---|---|
| Tlak | $p=F_n/A$ za jednolik tlak | normalno opterećenje | skalarno polje $p$ | tlak, $\Delta p$ |
| Brzina i gustoća | $\vec v(\vec x,t)$, $\rho=dm/dV$ | gibanje i masa po jedinici volumena | vektorsko polje brzine; gustoća zadana ili promjenjiva | profil, maseni protok |
| Hidrostatika | $dp/dz=-\rho g$ | ravnoteža s težinom | referentni test tlačnog polja (mirni balastni tank); rješavači često pohranjuju $p_{rgh}$, tlak bez hidrostatičkog doprinosa, koji u mirnoj vodi mora biti konstantan | tlak po dubini, neto tlak na oplatu |
| Viskoznost | $\tau=\mu\,dv/dy$ u jednostavnom smicanju | prijenos količine gibanja | konstitutivna veza i viskozni član | smicanje na stijenci |
| Površinska napetost | $\Delta p=\sigma(1/R_1+1/R_2)$ | ravnoteža na zakrivljenom sučelju | međupovršinska sila i kontaktni kut | oblik meniskusa |
| Kontrolni volumen i kontinuitet | @eq-lokalna-kontinuitet | očuvanje mase | bilanca po ćelijama i plohama | $Q$, akumulacija |
| Količina gibanja | @eq-navier-stokes-nestlacivi | ubrzanje određuju sile | lokalna bilanca uz pretpostavke modela | tlak, brzina, sila |
| Energija | akumulacija = neto prijenos + izvori | prijenos i pretvorba energije | energijska jednadžba kad je potrebna | temperatura, entalpija |
| Bernoullijeva jednadžba | $p/(\rho g)+v^2/(2g)+z=\text{konst.}$ | idealna mehanička energija | referenca pod istim pretpostavkama | odnos tlaka i brzine |
| Hidrostatička sila i uzgon | $\vec F_p=-\int_Ap\,\vec n_b\,dA$ | rezultanta tlaka | integracija po površini tijela | sila, moment, gaz |
| Sličnost | $Re,Fr,Ma,We$ | omjeri mjerodavnih učinaka | izbor fizike i skaliranje | $C_D$, $C_p$, $\lambda$ |
| Turbulencija | $-\rho\overline{v_i'v_j'}$ u RANS-u | prijenos srednje količine gibanja fluktuacijama | dodatne korelacije treba zatvoriti | srednji profil, otpor |
| Gubitci | $h_{loc}=\xi v_{ref}^2/(2g)$ | pad mehaničke energije | izlaz polja za 1D model | $h_g$, $\xi$, snaga |
| Rotor | $P=M\omega$ | prijenos rada | moment iz polja u odabranom okviru | snaga, učinkovitost |

Normala $\vec n_b$ usmjerena je iz tijela u fluid; $\vec F_p$ djeluje na tijelo. Za uzgon se integrira hidrostatički tlak, a za ukupnu silu u viskoznom toku dodaje se viskozna trakcija. Polumjeri u Young–Laplaceovoj relaciji imaju predznak određen odabranom normalom. Detaljan izbor fizike prema $Re$, $Fr$, $Ma$ i $We$ razrađen je u []{.mf1-chapter-ref target="u11"}.

## Kako se jednadžbe priručnika slažu u CFD slici {#sec-cfd-polja-izlazi}

Ćelijska bilanca (jednadžba [-@eq-celijska-bilanca-mase]) pokazuje prijelaz **jednadžba → algebarski sustav**. Nakon povezivanja s količinom gibanja i potrebnim dodatnim modelima dobivamo vrijednosti $p_i$, $\vec v_i$ i, prema slučaju, $\rho_i$ ili $T_i$. Vrijednost u ćeliji lokalna je aproksimacija polja, a vrijednosti na plohama računaju se u skladu s odabranom shemom.[]{#kako-se-mf1-jednadžbe-slažu-u-cfd-slici}

Drugi je prijelaz **polje → inženjerska veličina → odluka**:

| Polje ili izvedena veličina | Obrada | Izlaz i odluka |
|---|---|---|
| $p(\vec x,t)$ | očitanje na zadanim mjestima ili jasno definirani prosjeci po presjeku | $\Delta p$: mjerenje protoka ili tlačno opterećenje |
| $\vec v(\vec x,t)$ | $Q=\int_A\vec v\cdot\vec n\,dA$; uz $\rho$ daje maseni protok | raspodjela protoka po granama |
| Tlak i viskozno naprezanje | površinski zbroj sila i njihovih momenata | opterećenje nosača ili moment rotora |
| Gradijent brzine uz stijenku | $\tau_{st}=\mu(\partial v_t/\partial n)_{st}$ za jednostavan lokalni viskozni opis | trenje; prikladnost geometrije i obrade stijenke |
| Tlak, brzina i kota | bilančna razlika mehaničke energije na usklađenim presjecima | $h_g$, potrebna crpna snaga |

U Venturijevoj cijevi pad **statičkog** tlaka do grla većim je dijelom posljedica ubrzavanja fluida. Trajni gubitak određuje pad **ukupne mehaničke energije**, uz profile i kote iz energijske bilance. Statički pad tlaka izravno mjeri gubitak samo kad su brzine i visine uspoređenih presjeka jednake. Jednako tako treba razlikovati lokalnu vrijednost od prosjeka te trenutačno od vremenski osrednjenog opterećenja.

## Kada CFD ne treba: granice primjenjivosti {#sec-cfd-kada-ne-treba}

CFD je metoda za pitanja na koja jednostavniji model više ne daje dovoljan odgovor. Biraj najjednostavniji model koji, uz potrebnu nesigurnost, podupire odluku.[]{#kada-cfd-ne-treba-granice-primjenjivosti}

| Pitanje | Dovoljan početni model | Razlog za proširenje |
|---|---|---|
| Sila idealne hidrauličke preše | Pascalov zakon | lokalni tok kroz ventil |
| Tlak i sila u mirnom spremniku | hidrostatika i površinska integracija | zapljuskivanje, prolazno opterećenje |
| Gaz i mali nagib plovila | istisnina i početni stabilitet | dinamika u valovima |
| Protok jednostavnog Venturija | kontinuitet i Bernoulli | gubitci: najprije 1D korekcija; zatim lokalni tok |
| Radna točka instalacije | 1D cjevovod ili mreža sustava | nepouzdan otpor složenog lokalnog elementa |
| Odvajanje u difuzoru ili ventilu | prostorni model strujanja | ciljano polje i gubitak opravdavaju CFD |

Hijerarhija **analitika → 1D model → mrežni model sustava → prostorni CFD → nestacionarni ili višefazni CFD** opisuje rast potrebne razine detalja, a ne ljestvicu kvalitete. Mogući su i 2D ili osnosimetrični CFD modeli. Više detalja zahtijeva više podataka, računskog vremena i provjera te otvara dodatne izvore nesigurnosti. Vodeni udar, primjerice, često se najprije računa nestacionarnim 1D modelom elastičnog voda. U []{.mf1-chapter-ref target="u13"} lokalni CFD daje koeficijent gubitka koji se zatim vraća u jednostavniji model cijele instalacije.

## Kako procijeniti računski trošak

Trošak ovisi o broju ćelija, jednadžbi, vremenskih koraka, iteracija, radnih varijanti i pohranjenih izlaza te o računalnoj opremi. Zato naziv metode ne određuje univerzalan broj sati računa.

Najprije kratkim probnim računom procijeni trošak, a zatim u plan uključi proračune za prostorno i vremensko profinjenje te za ispitivanje osjetljivosti na ulaze i model. Gruba mreža može služiti planiranju, ali prihvatljivu mrežu određuje konvergencija traženog izlaza. Laminarni slučaj s poznatim rješenjem dobar je prvi pokus prije složene simulacije.

## Tipičan CFD tijek na primjeru iz priručnika: Venturijeva cijev {#sec-cfd-venturi}

Polazište je @ex-u09-venturijeva-cijev-za-mjerenje-protoka-ulja-t2: $D_1=60\ \mathrm{mm}$, $D_2=30\ \mathrm{mm}$, $\rho=870\ \mathrm{kg/m^3}$ i idealna procjena $Q\approx5{,}248\ \mathrm{L/s}$. Sada pitamo koliki su tlak u grlu i trajni gubitak u uređaju. Za viskozni model treba dodatno pribaviti viskoznost pri radnoj temperaturi, hrapavost, ulazni profil i cijelu geometriju; sama dva promjera ne određuju oblik difuzora.[]{#tipičan-cfd-tijek-na-primjeru-iz-mf1-venturijeva-cijev}

Radni slijed jest **geometrija → mreža → fizikalni model i uvjeti → diskretne jednadžbe → iteracije → polja → provjera → validacija → odluka**. Izbor modela i izbor mreže međusobno se usklađuju.

### Korak 1 — Geometrija {.unnumbered .unlisted .mf1-step}

Skicu cijevi pretvori u domenu fluida s ulazom, grlom, difuzorom, izlazom i stijenkama. Označi presjeke 1 (ulaz), 2 (grlo) i 3 (izlaz). Osnosimetričan model može smanjiti trošak ako su geometrija, uvjeti i traženi odziv osnosimetrični; simetrija geometrije sama po sebi ne jamči simetričan nestacionarni tok.

### Korak 2 — Mreža {.unnumbered .unlisted .mf1-step}

Podijeli domenu na ćelije povezane plohama. Mrežom razluči suženje, gradijente uz stijenku i moguće odvajanje u difuzoru. Udaljenost prve ćelije od stijenke i $y^+$ moraju odgovarati odabranom modelu stijenke. Pripremi sustavno profinjenje iste geometrije i prati ciljane tlakove i gubitak; ukupan broj ćelija nije dovoljan kriterij.

### Korak 3 — Rubni uvjeti {.unnumbered .unlisted .mf1-step}

Odaberi idealni Eulerov referentni model ili viskozni model prema cilju računa i procijenjenom $Re$. Zadaj usklađen par uvjeta, primjerice profil ili protok na ulazu i statički tlak na izlazu. Za Eulerov test stijenka je nepropusna uz dopušteno klizanje; za viskozni tok vrijedi prianjanje.

Početni uvjet jest polazno polje: u nestacionarnom računu opisuje fizičko stanje u početnom trenutku, a u stacionarnim iteracijama početna procjena služi traženju rješenja. Apsolutni tlak i temperatura potrebni su za procjenu kavitacijskog rizika. Protok i razliku tlakova ne smiješ propisati neovisno ako ih model mora međusobno povezati.

### Korak 4 — Rješavač i iteracijska konvergencija []{#korak-4-rješavač-i-iteracijska-konvergencija} {#korak-4-solver-i-iteracijska-konvergencija .unnumbered .unlisted .mf1-step}

Diskretne jednadžbe iz odjeljka [-@sec-realni-tok-cfd] povezuju tlakove i brzine susjednih ćelija. Rješavač iterativno usklađuje polja i tokove. Prati reziduale zajedno s $\Delta p_{12}$, gubitkom između presjeka 1 i 3 te masenim protocima. Mali rezidual nije dovoljan razlog za zaustavljanje ako se gubitak još mijenja. U nestacionarnom modelu razlikuj konvergenciju unutar vremenskog koraka od fizičke promjene u vremenu.

### Korak 5 — Verifikacija numeričkog rješenja {.unnumbered .unlisted .mf1-step}

**Verifikacija: rješava li numerički postupak zadane jednadžbe pravilno?** Analitički testovi ispituju programski kod i njegovu primjenu; za konkretan proračun procjenjuju se iteracijska i diskretizacijska pogreška [@nasa-cfd-vv].

| Dokaz | Što se provjerava na Venturiju |
|---|---|
| Iteracijska konvergencija | reziduali i ustaljivanje ciljane veličine |
| Očuvanje | ulazni i izlazni maseni protok, uz akumulaciju ako postoji |
| Mrežna konvergencija | promjena $\Delta p_{12}$ i gubitka pri prostornom profinjenju |
| Vremenska konvergencija | promjena nestacionarnog odziva pri smanjivanju vremenskog koraka |
| Analitička referenca | Bernoullijeva jednadžba uz iste pretpostavke i isto mjesto usporedbe |

Za vodoravni idealni slučaj vrijedi

$$
\Delta p_{12,B}=\frac{\rho}{2}\left(v_2^2-v_1^2\right).
$$ {#eq-cfd-vv-korak-5-verifikacija-numerickog-rjesenja-01}

Relacija je točna duž iste strujnice pri Bernoullijevim pretpostavkama. Sa srednjim presječnim brzinama dobiva se 1D referenca, pa razliku zbog nejednolikih profila ne treba pripisati diskretizaciji. Rezultat prostornog Eulerova računa zato usporedi lokalno ili uskladi presječne energijske tokove.

Za procjenu opaženog reda točnosti i GCI-ja koristi barem tri sustavno profinjene mreže, uz dovoljno malu iteracijsku pogrešku. Monotoni trend sam po sebi ne dokazuje asimptotsko područje. Prihvatljivost numeričke nesigurnosti određuje tražena odluka; univerzalni postotni prag ne postoji.

### Korak 6 — Validacija fizikalnog modela {.unnumbered .unlisted .mf1-step}

**Validacija: opisuje li model stvarni sustav dovoljno dobro za namjeravanu svrhu?** Rezultat viskoznog modela Venturijeve cijevi uspoređuje se s izmjerenim protocima i tlakovima pri odgovarajućoj geometriji i radnim uvjetima, uz mjerne, ulazne i numeričke nesigurnosti [@nasa-cfd-vv; @asme-vv20-2009].

Osjetljivost na hrapavost, ulazni profil ili model turbulencije ispituje se zasebnom analizom, koja nije ni provjera mrežne konvergencije ni zamjena za mjerenje. Razlika između viskoznog rješenja i idealnoga Bernoullijeva rješenja obuhvaća stvarne gubitke i razliku u pretpostavkama. Na kraju navedi protok, definiciju $\Delta p$, gubitak i nesigurnost u odnosu na odluku, primjerice na potrebnu crpnu visinu. Slaganje u jednoj radnoj točki ne potvrđuje cijelo radno područje.

## Pripremljeni V&V paketi {#sec-cfd-vv-paketi}

Paketi u mapi `data/cfd/` [repozitorija priručnika](https://github.com/martibasic/MF1_udzbenik/tree/main/data/cfd) omogućuju obradu rezultata bez instaliranja rješavača; svaki paket ima vlastiti opis podataka i podrijetla. Provjere se nadovezuju na poznato: analitičko rješenje daje referencu, kontinuitet bilancu, profinjenje numeričku procjenu, a eksperiment podatke za validaciju.[]{#tri-pripremljena-vv-paketa}

| Paket | Dostupni podatci | Dopušten zaključak |
|---|---|---|
| paket `poiseuille_laminar` | analitičko rješenje, tri sintetičke mreže, reziduali, protok, bilanca i GCI | vježba postupka; nije test određenog rješavača |
| paket `venturi_diffuser` | sintetički 1D model s propisanim gubitkom, tri mreže i računski trag | obrada gubitka i konvergencije; nije stvarni CFD ni mjerenje |
| paket `backstep_experiment` | izmjerena smična naprezanja i objavljeni CFL3D/SSTm rezultat | stvarna usporedba ponovnog priljubljivanja u primjeru [-@ex-stepenica-mjerenje-cfd] |
| paket `hydrofoil_experiment` | Ladsonova mjerenja [@ladson1988], FUN3D rezultati NASA TMR-a [@nasa-tmr-naca0012], nastavna dopuna nesigurnosti | mrežni trend i uvjetna usporedba otpora; nepotpuni dokazi za izvornu validaciju |

Venturijev paket odnosi se na vodu, promjere 100/50 mm i protok 10 L/s. To je zaseban nastavni skup iste vrste problema, a ne simulacija uljne Venturijeve cijevi iz odjeljka [-@sec-cfd-venturi]. Propisani koeficijent gubitka $\xi=0{,}2$ (u datotekama paketa označen `K`) ne prenosi se na taj primjer.

Validator `python tools/validate_cfd_vv.py` provjerava reference, bilance, podrijetlo, opaženi red i GCI. **GCI nije automatski standardna nesigurnost**, a tri monotone vrijednosti same po sebi nisu dokaz asimptotskog područja. Aeroprofil ostaje primjer usporedbe s nepotpunim arhivom: izvorni reziduali, zapisi sila kroz iteracije i masena bilanca nisu dostupni u pregledanim izvorima. Zaseban pokus sa strujanjem iza stepenice daje stvarna mjerenja za izravan račun odstupanja, ali ni ondje usporedba jednog izlaza ne zamjenjuje cjelovitu validaciju.

**Veza sa Z6 u []{.mf1-chapter-ref target="u12"}.** Rezultat FUN3D na najfinijoj mreži iznosi $C_D\approx0{,}01222$. Ladsonove točke (napadni kut; $C_D$) $=(8{,}08^\circ;\,0{,}00995)$ i $(10{,}10^\circ;\,0{,}01175)$ pri $Re_l=6\cdot10^6$, $Ma=0{,}15$ i prisilnom prijelazu (120 grit) linearnom interpolacijom na $10{,}00^\circ$ daju $C_D\approx0{,}01166$.

Zadani $s_{mj}=0{,}00020$, $s_{num}=0{,}00010$ i $s_{uv}=0{,}00010$ **nastavne su pretpostavke**, a ne objavljene nesigurnosti pokusa ili rješavača. Red veličine $s_{uv}$ obrazlaže se lokalnim nagibom od približno $0{,}000891$ po stupnju: nesigurnost kuta reda $0{,}1^\circ$ dala bi doprinos od oko $0{,}00009$. Doprinos $s_{num}$ obuhvaća ukupnu numeričku nesigurnost scenarija; GCI mu se ne dodaje ponovno, a osobito ne GCI iz drugog slučaja.

Za zadane neovisne normalne doprinose centrirane na nulu, s poznatim standardnim nesigurnostima, zbrajaju se varijance, $s_E=\sqrt{s_{mj}^2+s_{num}^2+s_{uv}^2}$, a dvostruka standardna nesigurnost razlike $2s_E$ daje približno 95 % pokrivanja. Kriterij $|E|\le 2s_E$ ispituje slaganje u toj točki. Povećanje $s_{mj}$ na $0{,}00030$ širi interval, ali ne poboljšava CFD model. Pretpostavke i podrijetlo podataka sačuvani su u `teaching_comparison.json`.

::: {.mf1-granica-modela}
<p class="mf1-box-label">Aeroprofil nije automatski hidroprofil</p>

Pokus s profilom NACA 0012 u zraku ne validira kavitaciju, slobodnu površinu ni uvjete stvarnog hidroprofila. Prijenos koeficijenata zahtijeva odgovarajuću sličnost, a primjena u vodi može zahtijevati zaseban pokus.
:::

## Što čitati dalje

Za nastavak odaberi pripremljeni laminarni paket, objasni njegovu bilancu i pogrešku, pa pročitaj [NASA-in vodič za V&V](https://www.grc.nasa.gov/www/wind/valid/tutorial/tutorial.html). Za dublje upoznavanje s diskretizacijom poslužit će Versteeg i Malalasekera, *An Introduction to Computational Fluid Dynamics: The Finite Volume Method*, ili Ferziger, Perić i Street, *Computational Methods for Fluid Dynamics*. Programske postavke, koje nisu preduvjet za ovaj priručnik, provjeri u [službenom vodiču OpenFOAM-a](https://doc.cfd.direct/openfoam/user-guide).

::: {.callout-note icon="false"}
## Završna poruka dodatka

Priručnik uči kako prepoznati fiziku, veličine, pretpostavke, bilance i granice modela te kako provjeriti rezultat. CFD proširuje istu logiku na složeniji prostor i vrijeme. Završni rezultat nije slika polja, nego obrazložena inženjerska odluka potkrijepljena provjerom i podatcima za namjeravanu uporabu.
:::
