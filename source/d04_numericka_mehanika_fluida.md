## Mehanika fluida i numerika — pregled

Ovaj dodatak povezuje ćelijsku bilancu iz []{.mf1-chapter-ref target="u07"}, analitičke reference iz []{.mf1-chapter-ref target="u08"} i lokalne jednadžbe iz []{.mf1-chapter-ref target="u12"}. CFD približno rješava odabrani model strujanja kada geometrija, rubni uvjeti ili promjene u vremenu otežavaju analitički račun.

::: {.callout-tip icon="false"}
## Opseg dodatka {#što-se-ovdje-neće-dogoditi}

**MF1** daje fizikalne zakone, pretpostavke i bilance. **Numerički mostovi** pokazuju njihov prijenos u račun. **Dublje** ovdje znači dodatno čitanje, izvan obveznog gradiva MF1; izvođenje shema i samostalno postavljanje rješavača pripadaju nastavku studija.

Za čitanje slijedi: @sec-cfd-mapa → @sec-cfd-polja-izlazi → @sec-cfd-venturi → @sec-cfd-vv-paketi. Prije vlastitog računa vrati se na @sec-cfd-kada-ne-treba.
:::

## Pojmovnik numeričkih metoda

Ovdje su kratice potrebne za dublje čitanje. Opće definicije CFD-a, reziduala i konvergencije nalaze se u [pojmovniku](d02_pojmovnik.qmd); pojedine se metode ne biraju samo po nazivu.

| Naziv | Značenje i uloga | Poveznica |
|---|---|---|
| FVM — *Finite Volume Method* | metoda konačnih volumena; povezane bilance ćelija | @eq-celijska-bilanca-mase |
| FEM — *Finite Element Method* | metoda konačnih elemenata; drugi način diskretizacije istih modelskih jednadžbi | @sec-realni-tok-cfd |
| RANS / LES / DNS | osrednjavanje / razrješavanje velikih / svih relevantnih turbulentnih skala | @sec-turbulencija |
| $k$–$\varepsilon$, $k$–$\omega$ SST | primjeri modela zatvaranja turbulentnih korelacija | @sec-turbulencija |
| SIMPLE / PISO / PIMPLE | primjeri algoritama usklađivanja tlaka, brzine i tokova; izbor ovisi o formulaciji i vremenskom opisu | @sec-realni-tok-cfd |
| MRF / klizajuća mreža | stacionarna aproksimacija referentnih okvira / praćenje relativnog gibanja dijelova mreže | []{.mf1-chapter-ref target="u14"} |
| VOF — *Volume of Fluid* | opis međupovršine volumnim udjelom faze; prikaz $\alpha=0{,}5$ samo je način vizualizacije granice | []{.mf1-chapter-ref target="u15"} |
| Zidne funkcije / $y^+$ | model područja uz stijenku / bezdimenzijska udaljenost; zahtjevi ovise o odabranoj obradi stijenke | @sec-turbulencija |
| GCI — *Grid Convergence Index* | procjena diskretizacijske nesigurnosti odabrane veličine iz sustavnog profinjenja | @sec-cfd-vv-paketi |

## Primjeri alata

**OpenFOAM** je primjer alata za rješavanje modela strujanja, a **ParaView** za pregled i obradu polja. Primjerice, OpenFOAMov [`forces`](https://cpp.openfoam.org/v13/classFoam_1_1functionObjects_1_1forces.html) integrira tlačne i viskozne doprinose sili i momentu; `forceCoeffs` ih normira zadanim referentnim veličinama. Isti fizikalni izlaz drugi alati mogu nazvati *force report*. Provjeri jedinice, referencu tlaka, obuhvaćene plohe i konvenciju predznaka u dokumentaciji svoje inačice.

Slika polja pomaže pronaći područje niskog tlaka ili odvajanja; odluku nosi izračunana veličina s procjenom nesigurnosti. Postavke alata slijede odabrani model i cilj računa.

## Rječnik MF1 → CFD: prijevod pojmova {#sec-cfd-mapa}

Tablica je središnja mapa: ista jednadžba dobiva prostorni numerički zapis, a polje se zatim svodi na traženi izlaz. Oznake $\mathbf u$ i $\vec v$ u knjizi predstavljaju brzinu fluida; u turbostrojevima razlikujemo apsolutnu $\vec c$, relativnu $\vec w$ i obodnu $\vec u$.[]{#rječnik-mf1-cfd-prijevod-pojmova}

| MF1 koncept | Jednadžba ili veza | Fizikalno značenje | CFD uloga | Tipičan izlaz |
|---|---|---|---|---|
| Tlak | $p=F_n/A$ za jednolik tlak | normalno opterećenje | skalarno polje $p$ | tlak, $\Delta p$ |
| Brzina i gustoća | $\mathbf u(\mathbf x,t)$, $\rho=dm/dV$ | gibanje i masa po volumenu | vektorsko polje brzine; gustoća zadana ili promjenjiva | profil, maseni protok |
| Hidrostatika | $dp/dz=-\rho g$ | ravnoteža s težinom | referentni test tlačnog polja | tlak po dubini |
| Viskoznost | $\tau=\mu\,du/dy$ u jednostavnom smicanju | prijenos količine gibanja | konstitutivna veza i viskozni član | smicanje na stijenci |
| Površinska napetost | $\Delta p=\sigma(1/R_1+1/R_2)$ | ravnoteža na zakrivljenom sučelju | međupovršinska sila i kontaktni kut | oblik meniska |
| Kontrolni volumen i kontinuitet | @eq-lokalna-kontinuitet | očuvanje mase | bilanca po ćelijama i plohama | $Q$, akumulacija |
| Količina gibanja | @eq-navier-stokes-nestlacivi | ubrzanje određuju sile | lokalna bilanca uz pretpostavke modela | tlak, brzina, sila |
| Energija | akumulacija = neto prijenos + izvori | prijenos i pretvorba energije | energijska jednadžba kada je potrebna | temperatura, entalpija |
| Bernoulli | $p/\rho+v^2/2+gz=\mathrm{const.}$ | idealna mehanička energija | referenca pod istim pretpostavkama | odnos tlaka i brzine |
| Hidrostatska sila i uzgon | $\mathbf F_p=-\int_Ap\mathbf n_b\,dA$ | rezultanta tlaka | integracija po površini tijela | sila, moment, gaz |
| Sličnost | $Re,Fr,Ma,We$ | omjeri važnih učinaka | izbor fizike i skaliranje | $C_D$, $C_p$, $\lambda$ |
| Turbulencija | $-\rho\overline{u_i'u_j'}$ u RANS-u | prijenos srednje količine gibanja fluktuacijama | dodatne korelacije treba zatvoriti | srednji profil, otpor |
| Gubitci | $h_L=\xi v_{ref}^2/(2g)$ | pad mehaničke energije | izlaz polja za 1D model | $h_L$, $\xi$, snaga |
| Rotor | $P=M\omega$ | prijenos rada | moment iz polja u odabranom okviru | snaga, učinkovitost |

Normala $\mathbf n_b$ usmjerena je iz tijela u fluid; $\mathbf F_p$ djeluje na tijelo. Za uzgon se integrira hidrostatski tlak, a za ukupnu silu u viskoznom toku dodaje se viskozna trakcija. Polumjeri su u Young–Laplaceovoj relaciji predznačeni prema odabranoj normali. Detaljan izbor fizike prema $Re$, $Fr$, $Ma$ i $We$ dan je u []{.mf1-chapter-ref target="u11"}.

## Kako se MF1 jednadžbe slažu u CFD slici {#sec-cfd-polja-izlazi}

Ćelijska bilanca @eq-celijska-bilanca-mase pokazuje prijelaz **jednadžba → algebarski sustav**. Nakon povezivanja s količinom gibanja i potrebnim dodatnim modelima dobivamo vrijednosti $p_i$, $\mathbf u_i$ i, prema slučaju, $\rho_i$ ili $T_i$. Vrijednost u ćeliji predstavlja lokalnu aproksimaciju polja; vrijednosti na plohama izračunavaju se dosljedno odabranoj shemi.[]{#kako-se-mf1-jednadžbe-slažu-u-cfd-slici}

Drugi je prijelaz **polje → inženjerska veličina → odluka**:

| Polje ili izvedena veličina | Obrada | Izlaz i odluka |
|---|---|---|
| $p(\mathbf x,t)$ | očitanje na zadanim mjestima ili jasno definirani prosjeci presjeka | $\Delta p$: mjerenje protoka ili tlačno opterećenje |
| $\mathbf u(\mathbf x,t)$ | $Q=\int_A\mathbf u\cdot\mathbf n\,dA$; uz $\rho$ daje maseni protok | raspodjela protoka po granama |
| Tlak i viskozno naprezanje | površinski zbroj sila i njihovih momenata | opterećenje nosača ili moment rotora |
| Gradijent brzine uz zid | $\tau_w=\mu(\partial u_t/\partial n)_w$ za jednostavan lokalni viskozni opis | trenje; prikladnost geometrije i obrade stijenke |
| Tlak, brzina i kota | bilančna razlika mehaničke energije na usklađenim presjecima | $h_L$, potrebna crpna snaga |

Za Venturi pad **statičkog** tlaka do grla velikim dijelom znači ubrzavanje. Trajni gubitak određuje pad **ukupne mehaničke energije**, uz profile i kote iz energijske bilance. Samo pod odgovarajućim uvjetima jednakih brzina i visina statički pad tlaka izravno mjeri gubitak. Sličnu razliku treba čuvati između lokalne vrijednosti i prosjeka, te između trenutnog i vremenski osrednjenog opterećenja.

## Kada CFD ne treba: granice primjenjivosti {#sec-cfd-kada-ne-treba}

CFD je metoda za pitanja kojima jednostavniji model više ne daje dovoljan odgovor. Biraj najjednostavniji model koji podupire odluku uz potrebnu nesigurnost.[]{#kada-cfd-ne-treba-granice-primjenjivosti}

| Pitanje | Dovoljan početni model | Razlog za proširenje |
|---|---|---|
| Sila idealne hidraulične preše | Pascalov zakon | lokalni tok kroz ventil |
| Tlak i sila u mirnom spremniku | hidrostatika i površinska integracija | zapljuskivanje, prolazno opterećenje |
| Gaz i mali nagib plovila | istisnina i početni stabilitet | dinamika u valovima |
| Protok jednostavnog Venturija | kontinuitet i Bernoulli | gubitci: najprije 1D korekcija; zatim lokalni tok |
| Radna točka instalacije | 1D cjevovod ili mreža sustava | nepouzdan otpor složenog lokalnog elementa |
| Odvajanje u difuzoru ili ventilu | prostorni model strujanja | ciljano polje i gubitak opravdavaju CFD |

Hijerarhija **analitika → 1D model → mrežni model sustava → prostorni CFD → nestacionarni ili višefazni CFD** opisuje rast potrebnih detalja, a ne ljestvicu kvalitete. Mogući su i 2D ili osnosimetrični CFD modeli. Više detalja traži više podataka, računskog vremena i provjera te otvara dodatne izvore nesigurnosti. Vodeni udar, primjerice, često se prvo računa nestacionarnim 1D modelom elastičnog voda. U []{.mf1-chapter-ref target="u13"} lokalni CFD vraća koeficijent gubitka jednostavnijem modelu cijele instalacije.

## Kako procijeniti računski trošak

Trošak ovisi o broju ćelija i jednadžbi, vremenskih koraka, iteracija, radnih varijanti i pohranjenih izlaza te hardveru. Zato naziv metode ne određuje univerzalan broj sati.

Najprije kratkim probnim računom procijeni trošak, zatim predvidi proračune za prostorno i vremensko profinjenje te osjetljivost na ulaze i model. Gruba mreža može služiti planiranju, ali prihvatljivu mrežu određuje konvergencija traženog izlaza. Laminarni slučaj s poznatim rješenjem dobar je prvi pokus prije složene simulacije.

## Tipičan CFD tijek na primjeru iz MF1: Venturijeva cijev {#sec-cfd-venturi}

Polazište je @ex-u09-venturijeva-cijev-za-mjerenje-protoka-ulja-t2: $D_1=60\ \mathrm{mm}$, $D_2=30\ \mathrm{mm}$, $\rho=870\ \mathrm{kg/m^3}$ i idealna procjena $Q\approx5{,}248\ \mathrm{L/s}$. Sada pitamo koliki su tlak u grlu i trajan gubitak kroz uređaj. Za viskozni model treba dodatno pribaviti viskoznost pri radnoj temperaturi, hrapavost, ulazni profil i cijelu geometriju; dva promjera ne određuju difuzor.[]{#tipičan-cfd-tijek-na-primjeru-iz-mf1-venturijeva-cijev}

Radni slijed jest **geometrija → mreža → fizikalni model i uvjeti → diskretne jednadžbe → iteracije → polja → provjera → validacija → odluka**. Izbor modela i mreže međusobno se usklađuju.

### Korak 1 — Geometrija {.unnumbered .unlisted .mf1-step}

Skicu cijevi pretvori u domenu fluida s ulazom, grlom, difuzorom, izlazom i stijenkama. Označi presjeke 1 (ulaz), 2 (grlo) i 3 (izlaz). Osnosimetričan model može smanjiti trošak ako su geometrija, uvjeti i traženi odziv osnosimetrični; simetrija geometrije sama ne jamči simetričan nestacionarni tok.

### Korak 2 — Mreža {.unnumbered .unlisted .mf1-step}

Podijeli domenu na ćelije povezane plohama. Razluči suženje, gradijente uz stijenku i moguće odvajanje u difuzoru. Razmak prve ćelije i $y^+$ moraju odgovarati odabranom modelu stijenke. Pripremi sustavno profinjenje iste geometrije i prati ciljane tlakove i gubitak; ukupan broj ćelija nije dovoljan kriterij.

### Korak 3 — Rubni uvjeti {.unnumbered .unlisted .mf1-step}

Odaberi idealni Eulerov referentni model ili viskozni model prema cilju i procjeni $Re$. Zadaj kompatibilan par uvjeta, primjerice profil/protok na ulazu i statički tlak na izlazu. Za Eulerov test stijenka je nepropusna uz dopušteno klizanje; za viskozni tok vrijedi prianjanje.

Početni uvjet jest polazno polje; u nestacionarnom računu predstavlja fizičko stanje u početnom trenutku. Kod stacionarnih iteracija početna procjena služi traženju rješenja. Apsolutni tlak i temperatura potrebni su za procjenu kavitacijskog rizika. Nije dopušteno neovisno propisati i protok i razliku tlakova ako ih model mora međusobno povezati.

### Korak 4 — Rješavač i iteracijska konvergencija []{#korak-4-rješavač-i-iteracijska-konvergencija} {#korak-4-solver-i-iteracijska-konvergencija .unnumbered .unlisted .mf1-step}

Diskretne jednadžbe iz @sec-realni-tok-cfd povezuju tlakove i brzine susjednih ćelija. Rješavač iterativno usklađuje polja i tokove. Prati reziduale zajedno s $\Delta p_{12}$, gubitkom između 1 i 3 te masenim protocima. Mali rezidual uz još promjenjiv gubitak nije dovoljan za zaustavljanje. Kod nestacionarnog modela razlikuj konvergenciju unutar koraka od fizičke promjene kroz vrijeme.

### Korak 5 — Verifikacija numeričkog rješenja {.unnumbered .unlisted .mf1-step}

**Verifikacija: rješava li numerički postupak pravilno zadane jednadžbe?** Analitički testovi ispituju kod i njegovu primjenu; za konkretan proračun procjenjuju se iteracijska i diskretizacijska pogreška [@nasa-cfd-vv].

| Dokaz | Što se provjerava na Venturiju |
|---|---|
| Iteracijska konvergencija | reziduali i ustaljivanje ciljane veličine |
| Očuvanje | ulazni i izlazni maseni protok, uz akumulaciju ako postoji |
| Mrežna konvergencija | promjena $\Delta p_{12}$ i gubitka pri prostornom profinjenju |
| Vremenska konvergencija | promjena nestacionarnog odziva smanjivanjem vremenskog koraka |
| Analitička referenca | Bernoulli uz iste pretpostavke i mjesto usporedbe |

Za horizontalni idealni slučaj vrijedi

$$
\Delta p_{12,B}=\frac{\rho}{2}\left(v_2^2-v_1^2\right).
$$ {#eq-cfd-vv-korak-5-verifikacija-numerickog-rjesenja-01}

Relacija je točna duž iste strujnice pri Bernoullijevim pretpostavkama. Uporabom srednjih presječnih brzina dobiva se 1D referenca: razliku zbog nejednolikih profila ne treba pripisati diskretizaciji. Prostorni Eulerov račun zato usporedi lokalno ili uskladi presječne energijske tokove.

Za procjenu opaženog reda i GCI-ja koristi barem tri sustavno profinjene mreže, uz dovoljno malu iteracijsku pogrešku. Monotoni trend sam ne dokazuje asimptotsko područje. Prihvatljivost numeričke nesigurnosti određuje tražena odluka, bez univerzalnog postotnog praga.

### Korak 6 — Validacija fizikalnog modela {.unnumbered .unlisted .mf1-step}

**Validacija: opisuje li model stvarni sustav dovoljno dobro za namjeravanu svrhu?** Viskozni Venturi uspoređuje se s mjerenim protocima i tlakovima pri odgovarajućoj geometriji i radnim uvjetima, uz mjerne, ulazne i numeričke nesigurnosti [@nasa-cfd-vv; @asme-vv20-2009].

Osjetljivost na hrapavost, ulazni profil ili turbulencijski model zasebna je analiza; nije ni mrežna konvergencija ni zamjena za mjerenje. Razlika viskoznog rješenja prema idealnom Bernoulliju uključuje stvarne gubitke i razliku pretpostavki. Na kraju izvijesti protok, definiciju $\Delta p$, gubitak i nesigurnost u odnosu na odluku, primjerice potrebnu crpnu visinu. Slaganje u jednoj radnoj točki ne potvrđuje cijelo radno područje.

## Tri pripremljena V&V paketa {#sec-cfd-vv-paketi}

Paketi u `data/cfd/` omogućuju obradu rezultata bez instalacije rješavača. Provjere se nadovezuju na poznato: analitičko rješenje daje referencu, kontinuitet bilancu, profinjenje numeričku procjenu, a eksperiment podatke za validaciju.[]{#tri-pripremljena-vv-paketa}

| Paket | Dostupni podatci | Dopušten zaključak |
|---|---|---|
| [`poiseuille_laminar`](../data/cfd/poiseuille_laminar/README.md) | analitičko rješenje, tri sintetičke mreže, reziduali, protok, bilanca i GCI | vježba postupka; nije test određenog rješavača |
| [`venturi_diffuser`](../data/cfd/venturi_diffuser/README.md) | sintetički 1D model s propisanim gubitkom, tri mreže i računski trag | obrada gubitka i konvergencije; nije stvarni CFD ni mjerenje |
| [`hydrofoil_experiment`](../data/cfd/hydrofoil_experiment/README.md) | Ladsonova mjerenja [@ladson1988], FUN3D rezultati NASA TMR-a [@nasa-tmr-naca0012], nastavna dopuna nesigurnosti | mrežni trend i uvjetna usporedba otpora; nepotpuni dokazi za izvornu validaciju |

Venturijev paket koristi vodu, promjere 100/50 mm i protok 10 L/s. To je zaseban nastavni skup iste vrste problema, a ne simulacija uljnog Venturija iz @sec-cfd-venturi. Propisani koeficijent gubitka $K=0{,}2$ ne prenosi se na taj primjer.

Validator `python tools/validate_cfd_vv.py` provjerava reference, bilance, podrijetlo, opaženi red i GCI. **GCI nije automatski standardna nesigurnost**, a tri monotone vrijednosti nisu same dokaz asimptotskog područja. Za profil nedostaju izvorni reziduali, povijesti sila i masena bilanca; nastavna dopuna ne nadomješta te dokaze.

**Veza sa Z6 u 12. poglavlju.** Najfiniji FUN3D rezultat $C_D=0{,}01222408822$ zaokružen je na $0{,}01222$. Ladsonove točke $(\alpha;C_D)=(8{,}08^\circ;0{,}00995)$ i $(10{,}10^\circ;0{,}01175)$ pri $Re_c=6\cdot10^6$, $Ma=0{,}15$ i prisilnom prijelazu (120 grit) daju linearnom interpolacijom na $10{,}00^\circ$ vrijednost $0{,}01166089$, zaokruženo $0{,}01166$.

Zadani $u_m=0{,}00020$, $u_n=0{,}00010$ i $u_v=0{,}00010$ **nastavne su pretpostavke**, ne objavljene nesigurnosti pokusa ili rješavača. Red veličine $u_v$ motivira lokalni nagib približno $0{,}000891$ po stupnju: nesigurnost kuta reda $0{,}1^\circ$ dala bi doprinos oko $0{,}00009$. Doprinos $u_n$ obuhvaća ukupnu numeričku nesigurnost scenarija; ne dodaje mu se ponovno GCI, osobito ne iz drugog slučaja.

Uz zadane neovisne, centrirane normalne doprinose s poznatim standardnim nesigurnostima zbrajaju se varijance, a $k=2$ daje približno 95 % pokrivanja. Kriterij $|E|\le U_E$ ispituje slaganje na toj točki. Povećanje $u_m$ na $0{,}00030$ širi interval, ali ne poboljšava CFD model. Pretpostavke i podrijetlo sačuvani su u `teaching_comparison.json`.

::: {.mf1-granica-modela}
<p class="mf1-box-label">Aeroprofil nije automatski hidroprofil</p>

NACA 0012 pokus u zraku ne validira kavitaciju, slobodnu površinu ni uvjete stvarnog hidroprofila. Prijenos koeficijenata zahtijeva odgovarajuću sličnost; vodena primjena može tražiti zaseban pokus.
:::

## Što čitati dalje

Za nastavak odaberi pripremljeni laminarni paket, objasni njegovu bilancu i pogrešku, pa pročitaj [NASA-in vodič za V&V](https://www.grc.nasa.gov/www/wind/valid/tutorial/tutorial.html). Za dublju diskretizaciju poslužit će Versteeg i Malalasekera, *An Introduction to Computational Fluid Dynamics: The Finite Volume Method*, ili Ferziger, Perić i Street, *Computational Methods for Fluid Dynamics*. Programske postavke provjeri u [službenom vodiču OpenFOAM-a](https://doc.cfd.direct/openfoam/user-guide); nisu preduvjet za MF1.

::: {.callout-note icon="false"}
## Sažetak

MF1 uči prepoznati fiziku, veličine, pretpostavke, bilance i granice modela te provjeriti rezultat. CFD proširuje istu logiku na složeniji prostor i vrijeme. Završni rezultat nije slika polja, nego obrazložena inženjerska odluka potkrijepljena provjerom i podacima za namjeravanu uporabu.
:::
