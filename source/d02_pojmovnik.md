## Radne definicije temeljnih pojmova mehanike fluida

Ovaj dodatak nije zamjena za glavna poglavlja. Njegova je svrha vratiti kratko radno značenje pojma kad student zna u kojoj je temi, ali mu se zamagli točna definicija ili razlika između dvaju srodnih izraza.

## Kako koristiti ovaj dodatak

Najprirodniji redoslijed je:

1. prepoznati kojoj temi pojam pripada
2. ovdje provjeriti kratku radnu definiciju
3. ako pojam i dalje nije jasan, vratiti se u odgovarajuće glavno poglavlje

Pojmovnik je zato namjerno kratak. On vraća fizikalni smisao termina, ali ne može zamijeniti cijeli model iz poglavlja.

## Temeljni pojmovi `pog. 1–2`

| Pojam | Kratka radna definicija | Tipično poglavlje | U numerici |
| --- | --- | --- | --- |
| Kontinuumski model | Idealizacija prema kojoj su svojstva fluida definirana u svakoj točki prostora. | <span class="mf1-ch-ref"><span class="mf1-ch-code">pog. 1</span><span class="mf1-ch-title">Osnove fluida i Pascalov zakon</span></span> | Diskretizirana polja na svakoj ćeliji mreže — temelj FVM i FEM solvera. |
| Gustoća | Masa po jedinici volumena, $\rho = m/V$. | <span class="mf1-ch-ref"><span class="mf1-ch-code">pog. 1</span><span class="mf1-ch-title">Osnove fluida i Pascalov zakon</span></span> | Skalarno polje $\rho$ ili konstanta u solveru; u VOF nastaje miješanjem dviju faznih gustoća. |
| Specifična težina | Težina po jedinici volumena, $\gamma = \rho g$. | <span class="mf1-ch-ref"><span class="mf1-ch-code">pog. 1</span><span class="mf1-ch-title">Osnove fluida i Pascalov zakon</span></span> | Ulazi neizravno preko $\rho g$ u gravitacijskom članu Navier-Stokesove jednadžbe. |
| Relativna gustoća | Omjer gustoće promatranog fluida i gustoće vode. | <span class="mf1-ch-ref"><span class="mf1-ch-code">pog. 1</span><span class="mf1-ch-title">Osnove fluida i Pascalov zakon</span></span> | Koristi se pri zadavanju početnih uvjeta i identifikaciji faza u multifaznim simulacijama. |
| Tlak | Normalna sila po jedinici površine; u fluidu se tretira kao skalarno polje. | <span class="mf1-ch-ref"><span class="mf1-ch-code">pog. 1</span><span class="mf1-ch-title">Osnove fluida i Pascalov zakon</span></span> | Skalarno polje koje se rješava Poissonovom jednadžbom u SIMPLE ili PISO algoritmu. |
| Izotropnost tlaka | Svojstvo mirujućeg fluida da tlak u jednoj točki djeluje jednako u svim smjerovima. | <span class="mf1-ch-ref"><span class="mf1-ch-code">pog. 1</span><span class="mf1-ch-title">Osnove fluida i Pascalov zakon</span></span> | Temeljna pretpostavka kod razdvajanja normalnih i smičnih naprezanja u tenzorskom zapisu. |
| Pascalov zakon | Promjena tlaka zadana u zatvorenom mirujućem fluidu prenosi se kroz cijeli fluid. | <span class="mf1-ch-ref"><span class="mf1-ch-code">pog. 1</span><span class="mf1-ch-title">Osnove fluida i Pascalov zakon</span></span> | Implicitno zadovoljeno u svakom koraku iterativnog rješavanja tlačne jednadžbe. |
| Dinamička viskoznost | Mjera unutarnjeg trenja fluida, označena s $\mu$. | <span class="mf1-ch-ref"><span class="mf1-ch-code">pog. 2</span><span class="mf1-ch-title">Viskoznost, površinska napetost i kapilarnost</span></span> | Koeficijent ispred viskoznog (Laplaceova) člana u Navier-Stokesovoj jednadžbi. |
| Kinematička viskoznost | Omjer dinamičke viskoznosti i gustoće, $\nu = \mu / \rho$. | <span class="mf1-ch-ref"><span class="mf1-ch-code">pog. 2</span><span class="mf1-ch-title">Viskoznost, površinska napetost i kapilarnost</span></span> | Ulazi u definiciju lokalnog Reynoldsovog broja i u izvore $k$-$\varepsilon$ modela. |
| Površinska napetost | Površinski učinak koji se ponaša kao zatezanje slobodne površine, označen s $\sigma$. | <span class="mf1-ch-ref"><span class="mf1-ch-code">pog. 2</span><span class="mf1-ch-title">Viskoznost, površinska napetost i kapilarnost</span></span> | Modelira se preko CSF modela (Continuum Surface Force) u VOF solverima. |
| Kontaktni kut | Kut kojim se slobodna površina siječe sa stijenkom; određuje kvasi li tekućina stijenku. | <span class="mf1-ch-ref"><span class="mf1-ch-code">pog. 2</span><span class="mf1-ch-title">Viskoznost, površinska napetost i kapilarnost</span></span> | Rubni uvjet `contactAngle` na zidnim plohama u multifaznim simulacijama. |
| Kapilarnost | Uspon ili pad tekućine u uskoj cjevčici zbog površinske napetosti i kontaktnog kuta. | <span class="mf1-ch-ref"><span class="mf1-ch-code">pog. 2</span><span class="mf1-ch-title">Viskoznost, površinska napetost i kapilarnost</span></span> | Posljedica zajedničkog djelovanja CSF modela i kontaktnog kuta na slobodnoj površini. |
| Tlakovni skok | Porast ili pad tlaka preko zakrivljene slobodne površine, opisan Young-Laplaceovom relacijom. | <span class="mf1-ch-ref"><span class="mf1-ch-code">pog. 2</span><span class="mf1-ch-title">Viskoznost, površinska napetost i kapilarnost</span></span> | Diskretni skok polja tlaka preko sučelja faza u VOF simulacijama. |

## Hidrostatika i sile `pog. 3–7`

| Pojam | Kratka radna definicija | Tipično poglavlje | U numerici |
| --- | --- | --- | --- |
| Apsolutni tlak | Tlak mjeren u odnosu na idealni vakuum. | <span class="mf1-ch-ref"><span class="mf1-ch-code">pog. 3</span><span class="mf1-ch-title">Hidrostatička raspodjela tlaka i manometrija</span></span> | Rijetko se rješava izravno; rekonstruira se iz polja $p_{man}$ uvećanog za $p_{atm}$. |
| Manometarski tlak | Tlak mjeren u odnosu na lokalni atmosferski tlak. | <span class="mf1-ch-ref"><span class="mf1-ch-code">pog. 3</span><span class="mf1-ch-title">Hidrostatička raspodjela tlaka i manometrija</span></span> | Standardno polje $p$ ili $p_{rgh}$ u nestlačivim solverima. |
| Vakuumski tlak | Mjera koliko je tlak u sustavu ispod atmosferskog tlaka. | <span class="mf1-ch-ref"><span class="mf1-ch-code">pog. 3</span><span class="mf1-ch-title">Hidrostatička raspodjela tlaka i manometrija</span></span> | Rubni uvjet niže od $p_{atm}$, npr. na usisu pumpe ili kondenzatora. |
| Relativno mirovanje fluida | Stanje u kojem se fluid prema spremniku ponaša kao da miruje, iako se cijeli sustav može gibati. | <span class="mf1-ch-ref"><span class="mf1-ch-code">pog. 4</span><span class="mf1-ch-title">Relativno mirovanje fluida</span></span> | Modelirano MRF zonom (Moving Reference Frame) ili rotirajućim okvirom referencije. |
| Efektivno ubrzanje | Rezultantno ubrzanje gravitacije i gibanja spremnika koje određuje nagib slobodne površine i lokalnu raspodjelu tlaka. | <span class="mf1-ch-ref"><span class="mf1-ch-code">pog. 4</span><span class="mf1-ch-title">Relativno mirovanje fluida</span></span> | Volumni izvor sile koji uračunava centrifugalno i Coriolisovo ubrzanje. |
| Centar tlaka | Točka u kojoj djeluje rezultanta raspodijeljenog hidrostatskog tlaka na plohu. | <span class="mf1-ch-ref"><span class="mf1-ch-code">pog. 5</span><span class="mf1-ch-title">Hidrostatske sile na ravne plohe</span></span> | Post-procesni izračun integralima $p \vec{r}$ i $p$ preko zidnoga patcha. |
| Horizontalna komponenta sile | Komponenta sile na zakrivljenoj plohi koja se često dobiva iz vertikalne projekcije. | <span class="mf1-ch-ref"><span class="mf1-ch-code">pog. 6</span><span class="mf1-ch-title">Zakrivljene plohe i rastav sila</span></span> | Alati `forces` (OpenFOAM) ili `Surface integrate` (ParaView) na zadanom patchu. |
| Vertikalna komponenta sile | Komponenta sile na zakrivljenoj plohi povezana s težinom fluida iznad plohe. | <span class="mf1-ch-ref"><span class="mf1-ch-code">pog. 6</span><span class="mf1-ch-title">Zakrivljene plohe i rastav sila</span></span> | Isti alat — projekcija ukupne sile na zidu na vertikalnu os. |
| Uzgon | Rezultantna sila prema gore koja nastaje zbog hidrostatskog tlaka na uronjeno tijelo. | <span class="mf1-ch-ref"><span class="mf1-ch-code">pog. 7</span><span class="mf1-ch-title">Uzgon, plivanje i stabilnost</span></span> | U VOF se izračunava iz polja $\alpha$ pomnoženog razlikom gustoća dviju faza. |
| Centar uzgona | Težište istisnutog volumena fluida; pravac djelovanja uzgona prolazi kroz njega. | <span class="mf1-ch-ref"><span class="mf1-ch-code">pog. 7</span><span class="mf1-ch-title">Uzgon, plivanje i stabilnost</span></span> | Težište područja $\alpha > 0{,}5$ (vodena faza) ispod slobodne površine. |

## Strujanje, energija i mjerenje `pog. 8–10`

| Pojam | Kratka radna definicija | Tipično poglavlje | U numerici |
| --- | --- | --- | --- |
| Kontrolni volumen | Zamišljeni dio prostora kroz koji fluid može ulaziti, izlaziti i akumulirati se. | <span class="mf1-ch-ref"><span class="mf1-ch-code">pog. 8</span><span class="mf1-ch-title">Kontrolni volumen i kontinuitet</span></span> | Svaka ćelija mreže je elementarni kontrolni volumen u FVM diskretizaciji. |
| Akumulacija | Promjena mase ili volumena unutar kontrolnog volumena tijekom vremena. | <span class="mf1-ch-ref"><span class="mf1-ch-code">pog. 8</span><span class="mf1-ch-title">Kontrolni volumen i kontinuitet</span></span> | Vremenski član $\partial/\partial t$ u diskretizaciji tranzijentnih jednadžbi. |
| Volumenski protok | Volumen fluida koji prođe kroz presjek u jedinici vremena, $Q = dV/dt$. | <span class="mf1-ch-ref"><span class="mf1-ch-code">pog. 8</span><span class="mf1-ch-title">Kontrolni volumen i kontinuitet</span></span> | Post-procesni integral $\vec{u} \cdot \vec{n}$ preko zadanog presjeka mreže. |
| Maseni protok | Masa fluida koja prođe kroz presjek u jedinici vremena, $\dot{m} = dm/dt$. | <span class="mf1-ch-ref"><span class="mf1-ch-code">pog. 8</span><span class="mf1-ch-title">Kontrolni volumen i kontinuitet</span></span> | Isti integral pomnožen lokalnom gustoćom; alat `flowRatePatch` u OpenFOAM-u. |
| Strujnica | Krivulja koja je u svakoj točki tangencijalna na vektor brzine. | <span class="mf1-ch-ref"><span class="mf1-ch-code">pog. 9</span><span class="mf1-ch-title">Bernoullijeva jednadžba idealnog fluida</span></span> | Vizualizacija: `streamline` filter u ParaView-u ili `streamlines` u Fluentu. |
| Geodetska visina | Položajna komponenta energije fluida, označena s $z$. | <span class="mf1-ch-ref"><span class="mf1-ch-code">pog. 9</span><span class="mf1-ch-title">Bernoullijeva jednadžba idealnog fluida</span></span> | U nestlačivim solverima ugrađena je u definiciju $p_{rgh} = p - \rho g h$. |
| Stagnacijska točka | Mjesto gdje lokalna brzina fluida pada na nulu. | `pog. 9–10` | Detektira se kao lokalni minimum $|\vec{u}|$ uz tijelo u struji. |
| Stagnacijski tlak | Tlak koji bi fluid imao kada bi se idealno zaustavio bez gubitaka. | `pog. 9–10` | Skalarno polje $p + \tfrac{1}{2}\rho v^2$ izračunato u post-procesu. |
| EGL | Energijska linija koja prati ukupnu mehaničku energiju po jedinici težine. | `pog. 9–10` | Vizualizacijska linija ukupne energije po odabranoj strujnici. |
| HGL | Hidraulička linija koja prati tlačnu i geodetsku visinu, bez brzinskog člana. | `pog. 9–10` | Polje $p/(\rho g) + z$ prikazano kao iso-površina ili linija. |
| Pitot-statička cijev | Instrument koji iz razlike stagnacijskog i statičkog tlaka određuje brzinu strujanja. | <span class="mf1-ch-ref"><span class="mf1-ch-code">pog. 10</span><span class="mf1-ch-title">Realni Bernoulli i gubici</span></span> | Validacijska sonda: točkasti probe za $p$ i komponente $\vec{u}$ na zadanoj koordinati. |
| Linijski gubici | Gubici energije zbog trenja uz stijenku cijevi duž ravne dionice. | <span class="mf1-ch-ref"><span class="mf1-ch-code">pog. 10</span><span class="mf1-ch-title">Realni Bernoulli i gubici</span></span> | U RANS modelima dobiju se preko zidnih funkcija i odgovarajuće $y^+$ rezolucije. |
| Lokalni gubici | Gubici energije uzrokovani ventilima, koljenima, suženjima i drugim lokalnim poremećajima. | <span class="mf1-ch-ref"><span class="mf1-ch-code">pog. 10</span><span class="mf1-ch-title">Realni Bernoulli i gubici</span></span> | Razrešavaju se finijom mrežom oko geometrijskih singulariteta. |

## Sile strujanja i cjevovodi `pog. 11–13`

| Pojam | Kratka radna definicija | Tipično poglavlje | U numerici |
| --- | --- | --- | --- |
| Količina gibanja | Vektorska veličina koja povezuje protok mase i brzinu te određuje sile u kontrolnom volumenu. | <span class="mf1-ch-ref"><span class="mf1-ch-code">pog. 11</span><span class="mf1-ch-title">Količina gibanja i sile strujanja</span></span> | Konvektivni član $\nabla \cdot (\rho \vec{u} \otimes \vec{u})$ — srž Navier-Stokesove jednadžbe u svakom FVM koraku. |
| Reakcijska sila strujanja | Sila koju promjena brzine ili smjera struje proizvodi na cijev, mlaznicu, plohu ili spoj. | <span class="mf1-ch-ref"><span class="mf1-ch-code">pog. 11</span><span class="mf1-ch-title">Količina gibanja i sile strujanja</span></span> | Funkcijski objekt `forces` ili `forceCoeffs` integrira tlak i smična naprezanja po patchu. |
| Relativna brzina | Brzina fluida promatrana u odnosu na gibajući element, važna za lopatice i potisak. | <span class="mf1-ch-ref"><span class="mf1-ch-code">pog. 12</span><span class="mf1-ch-title">Pokretne lopatice i potisak</span></span> | U MRF zonama transformacija polja brzine u rotirajući okvir referencije. |
| Reynoldsov broj | Bezdimenzijski broj koji uspoređuje učinak inercije i viskoznosti, $Re = vD/\nu$. | <span class="mf1-ch-ref"><span class="mf1-ch-code">pog. 13</span><span class="mf1-ch-title">Cjevovodi</span></span> | Određuje izbor solvera: laminarni, RANS ($k$-$\varepsilon$, $k$-$\omega$ SST), LES ili DNS. |
| Moodyjev dijagram | Grafički alat za određivanje Darcyjeva koeficijenta trenja iz $Re$ i relativne hrapavosti. | <span class="mf1-ch-ref"><span class="mf1-ch-code">pog. 13</span><span class="mf1-ch-title">Cjevovodi</span></span> | Zamjenjuje se zidnim funkcijama (low-Re ili high-Re), izbor ovisi o $y^+$ rezoluciji mreže. |
| Darcyjev koeficijent trenja | Bezdimenzijski koeficijent $\lambda$ koji povezuje režim strujanja i linijske gubitke u cijevi. | <span class="mf1-ch-ref"><span class="mf1-ch-code">pog. 13</span><span class="mf1-ch-title">Cjevovodi</span></span> | Indirektno preko smičnog naprezanja na zidu i izabranih zidnih funkcija. |
| Koeficijent istjecanja | Bezdimenzijski faktor $C_d$ koji povezuje idealno i stvarno istjecanje kroz otvor ili pukotinu. | <span class="mf1-ch-ref"><span class="mf1-ch-code">pog. 13</span><span class="mf1-ch-title">Cjevovodi</span></span> | Razrešava se mrežom uskih otvora ili nadomješta diskretnim modelom otvora. |
| Serijski spoj cjevovoda | Spoj u kojem isti protok prolazi kroz sve dionice, a gubici se zbrajaju. | <span class="mf1-ch-ref"><span class="mf1-ch-code">pog. 13</span><span class="mf1-ch-title">Cjevovodi</span></span> | Modelira se kontinuiranom mrežom kroz sve dionice s istim ulaznim i izlaznim patchom. |
| Paralelni spoj cjevovoda | Spoj u kojem se protok dijeli među granama, a gubitak energije između istih čvorova mora biti jednak. | <span class="mf1-ch-ref"><span class="mf1-ch-code">pog. 13</span><span class="mf1-ch-title">Cjevovodi</span></span> | Više patchova s rubnim uvjetima $p$ ili $Q$ na zajedničkim čvorovima granjenja. |
| Radna točka sustava | Točka presjeka zahtjeva sustava i mogućnosti crpke ili postrojenja. | <span class="mf1-ch-ref"><span class="mf1-ch-code">pog. 13</span><span class="mf1-ch-title">Cjevovodi</span></span> | Određuje se iterativnom CFD simulacijom (sweep) ili komplementarnim 1D mrežnim modelom. |

## Bezdimenzijska analiza i sličnost `pog. 14`

| Pojam | Kratka radna definicija | Tipično poglavlje | U numerici |
| --- | --- | --- | --- |
| Bezdimenzijski broj | Omjer dviju sila (ili veličina iste dimenzije) koji mjeri koja sila dominira. | <span class="mf1-ch-ref"><span class="mf1-ch-code">pog. 14</span><span class="mf1-ch-title">Bezdimenzijski brojevi, dimenzijska analiza i sličnost</span></span> | Bezdimenzionirane jednadžbe; jedan parametar zamjenjuje više dimenzijskih veličina. |
| Sila inercije | Težnja fluida da nastavi gibanje, $F_i \sim \rho v^2 L^2$; referenca za većinu brojeva. | <span class="mf1-ch-ref"><span class="mf1-ch-code">pog. 14</span><span class="mf1-ch-title">Bezdimenzijski brojevi, dimenzijska analiza i sličnost</span></span> | Konvektivni član Navier-Stokesove jednadžbe. |
| Froudeov broj | Omjer inercije i gravitacije, $Fr = v/\sqrt{gL}$; vlada kod slobodne površine. | <span class="mf1-ch-ref"><span class="mf1-ch-code">pog. 14</span><span class="mf1-ch-title">Bezdimenzijski brojevi, dimenzijska analiza i sličnost</span></span> | Skaliranje slobodne površine u VOF simulaciji broda ili kanala. |
| Eulerov broj / koeficijent tlaka | Omjer tlačne i inercijske sile, $Eu = \Delta p/(\rho v^2)$, $C_p$. | <span class="mf1-ch-ref"><span class="mf1-ch-code">pog. 14</span><span class="mf1-ch-title">Bezdimenzijski brojevi, dimenzijska analiza i sličnost</span></span> | Izlazni koeficijent (`forceCoeffs`) ili polje $C_p$. |
| Kavitacijski broj | Rezerva tlaka iznad isparavanja, $\sigma_{kav} = (p - p_v)/(\tfrac12\rho v^2)$. | <span class="mf1-ch-ref"><span class="mf1-ch-code">pog. 14</span><span class="mf1-ch-title">Bezdimenzijski brojevi, dimenzijska analiza i sličnost</span></span> | Prag kavitacijskog modela (npr. Schnerr-Sauer). |
| Weberov broj | Omjer inercije i površinske napetosti, $We = \rho v^2 L/\sigma$. | <span class="mf1-ch-ref"><span class="mf1-ch-code">pog. 14</span><span class="mf1-ch-title">Bezdimenzijski brojevi, dimenzijska analiza i sličnost</span></span> | Parametar VOF/CSF modela raspršivanja. |
| Bondov (Eötvösov) broj | Omjer gravitacije i površinske napetosti, $Bo = \rho g L^2/\sigma$. | <span class="mf1-ch-ref"><span class="mf1-ch-code">pog. 14</span><span class="mf1-ch-title">Bezdimenzijski brojevi, dimenzijska analiza i sličnost</span></span> | Važnost napetosti vs gravitacije u multifaznom modelu. |
| Strouhalov broj | Bezdimenzijska frekvencija vrtložnog otpuštanja, $St = fL/v$. | <span class="mf1-ch-ref"><span class="mf1-ch-code">pog. 14</span><span class="mf1-ch-title">Bezdimenzijski brojevi, dimenzijska analiza i sličnost</span></span> | Validacija nestacionarne simulacije (vortex shedding). |
| Machov broj | Omjer inercije i stlačivosti, $Ma = v/a$; granica nestlačivosti $Ma < 0{,}3$. | <span class="mf1-ch-ref"><span class="mf1-ch-code">pog. 14</span><span class="mf1-ch-title">Bezdimenzijski brojevi, dimenzijska analiza i sličnost</span></span> | Izbor nestlačivog ili stlačivog solvera. |
| Buckinghamov Π teorem | Metoda koja iz $n$ veličina i $k$ dimenzija daje $n - k$ bezdimenzijskih grupa. | <span class="mf1-ch-ref"><span class="mf1-ch-code">pog. 14</span><span class="mf1-ch-title">Bezdimenzijski brojevi, dimenzijska analiza i sličnost</span></span> | Opravdava bezdimenzioniranje jednadžbi prije simulacije. |
| Dinamička sličnost | Jednakost mjerodavnih bezdimenzijskih brojeva modela i prototipa. | <span class="mf1-ch-ref"><span class="mf1-ch-code">pog. 14</span><span class="mf1-ch-title">Bezdimenzijski brojevi, dimenzijska analiza i sličnost</span></span> | Uvjet da rezultat simulacije modela vrijedi za prototip. |

::: {.mf1-warning}
<p class="mf1-box-label">Najčešća pogreška</p>

Najčešća pogreška pri radu s pojmovnikom nije pogrešna definicija nego pokušaj da se kratka definicija koristi kao zamjena za cijelo poglavlje. Ako pojam i dalje nije jasan u konkretnom zadatku, treba se vratiti na model i primjer iz pripadnog poglavlja, a ne tražiti još kraću verziju iste definicije.
:::

::: {.mf1-mini-summary}
<p class="mf1-box-label">Sažetak za ponijeti</p>

<span class="mf1-ch-ref"><span class="mf1-ch-code">dod. B</span><span class="mf1-ch-title">Pojmovnik</span></span> je brza orijentacijska karta pojmova, ne skraćeni udžbenik. Služi onda kad je tema poznata, ali je potrebno odmah vratiti točan fizikalni smisao termina prije nastavka računa. Stupac *U numerici* uz svaki pojam najavljuje gdje se isti pojam pojavljuje u računalnoj dinamici fluida — detaljnije u <span class="mf1-ch-ref"><span class="mf1-ch-code">dod. D</span><span class="mf1-ch-title">Numerička mehanika fluida</span></span>.
:::






