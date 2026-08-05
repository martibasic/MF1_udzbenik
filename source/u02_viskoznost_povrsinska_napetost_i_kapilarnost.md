![Pregled poglavlja pog. 2: Viskoznost, površinska napetost i kapilarnost](../assets/print/u02_fig_uvod_pregled.svg){#fig-uvod-u02 fig-align="center" fig-alt="Pregled poglavlja pog. 2: Viskoznost, površinska napetost i kapilarnost"}

## Kad fluid više nije samo nositelj tlaka

<span class="mf1-ch-ref"><span class="mf1-ch-code">pog. 1</span><span class="mf1-ch-title">Osnove fluida i Pascalov zakon</span></span> zatvorio je tlak i Pascalov zakon za mirujući fluid. <span class="mf1-ch-ref"><span class="mf1-ch-code">pog. 2</span><span class="mf1-ch-title">Reologija, viskoznost i međupovršinske pojave</span></span> otvara ono što se u tehnici vrlo brzo osjeti rukom i alatom: fluid nije samo nositelj tlaka, nego i medij koji pruža otpor gibanju te stvara pojave na slobodnoj površini.

Zato ovo poglavlje namjerno drži dva mehanizma jedan uz drugi: viskoznost u volumenu fluida i površinsku napetost na granici faza.

::: {.mf1-application}
<p class="mf1-box-label">Inženjerski kontekst</p>

Viskoznost u strojarstvu odlučuje hoće li ležaj i klizna vodilica ostati odvojeni tankim uljnim filmom ili će prijeći u trošenje, a u autoindustriji upravo ona zatvara radni prozor motornog i hidrauličnog ulja pri hladnom startu i toplom radu. Površinska napetost i kapilarnost pojavljuju se u raspršivačima, premazima, zavarivačkim kupkama i podizanju vlage kroz porozne građevinske materijale, pa ovo poglavlje spaja tribologiju, obradu površina i fiziku slobodne površine.
:::

::: {.mf1-priprema}
<p class="mf1-box-label">Prije čitanja poglavlja</p>

**Predznanje koje se pretpostavlja:**

- pojam smičnog naprezanja i naprezanja u tvari (Fizika I, osnove čvrstoće);
- diferencijalni račun jedne varijable, gradijent funkcije (Matematika I);
- razlikovanje sila i tlaka uvedeno u poglavlju <span class="mf1-ch-ref"><span class="mf1-ch-code">pog. 1</span><span class="mf1-ch-title">Osnove fluida i Pascalov zakon</span></span>.

**Ishodi učenja:**

- razlikovati dinamičku i kinematičku viskoznost te ih pravilno koristiti;
- primijeniti Newtonov zakon viskoznosti na strujanje između dviju ploha;
- izračunati kapilarni uspon u kapilari zadanih svojstava;
- procijeniti kada površinska napetost dominira nad ostalim učincima na slobodnoj površini.

**Procijenjeno vrijeme rada uz udžbenik:** 9 sati.
:::

## Fizikalni uvod i matematički izvod

Kad se slojevi fluida gibaju relativno jedan prema drugom, pojavljuje se smično naprezanje i otpor gibanju. U Newtonskom fluidu vrijedi

$$
{}\tau = \mu \frac{dv}{dy}
$$ {#eq-reologija-fizikalni-uvod-i-matematicki-izvod-01}

::: {.mf1-fizikalno-znacenje}
<p class="mf1-box-label">Fizikalno značenje</p>
Smično naprezanje $\tau$ je sila trenja po jedinici površine između susjednih slojeva fluida koji se kližu jedan uz drugoga. Gradijent brzine $dv/dy$ opisuje koliko se brzo ta brzina mijenja po okomici na tok – što su slojevi bliži po brzini, to je za zadanu viskoznost manje smično naprezanje. Dinamička viskoznost vode pri sobnoj temperaturi reda je $10^{-3}\ \text{Pa s}$, dok ulja mogu biti višestruko viskoznija; svojstvo se uvijek veže uz temperaturu i konkretan fluid [@white2011]. Newtonski model kaže da je $\tau$ linearno s $dv/dy$; za nenewtonske fluide ta veza zahtijeva drukčiji konstitutivni model.
:::

gdje je $\mu$ dinamička viskoznost, a $dv/dy$ gradijent brzine. Taj zapis kaže da matematika gradijenta brzine nije formalnost: što se susjedni slojevi brže razilaze po brzini, to je potrebno veće smično naprezanje da se njihovo relativno gibanje održi.

Na slobodnoj površini druga je fizika presudna: stvaranje površine traži energiju, pa se površina ponaša kao da je pod zateznom silom. To vodi prema površinskoj napetosti, kontaktnom kutu i kapilarnom usponu.

::: {.mf1-izvod}
<p class="mf1-box-label">Konstitutivna motivacija — Newtonov zakon viskoznosti i ravnoteža kapilarnog uspona</p>

Promatra se tanak sloj fluida između dviju ravnih paralelnih ploča površine $A$ i razmaka $\delta$. Donja ploča miruje, a gornja se giba brzinom $U$. Pretpostavljaju se stacionarno laminarno strujanje Newtonskoga fluida, prianjanje fluida na obje ploče, zanemarivi rubni učinci i gradijent tlaka u smjeru gibanja jednak nuli. Tada je Couetteov profil brzine linearan. Pokusno utvrđena proporcionalnost smičnoga naprezanja i gradijenta brzine jest **konstitutivni model**, a ne posljedica ravnoteže sila sama po sebi. Za ovaj se slučaj piše razmjer

$$
F \propto A\frac{U}{\delta}.
$$ {#eq-reologija-konstitutivna-motivacija-newtonov-zakon-viskozno-01}

Uvođenjem konstante razmjernosti $\mu$ dobiva se

$$
F = \mu A\frac{U}{\delta}.
$$ {#eq-reologija-konstitutivna-motivacija-newtonov-zakon-viskozno-02}

Dijeljenjem s površinom slijedi smično naprezanje

$$
τ = \frac{F}{A} = \mu\frac{U}{\delta}.
$$ {#eq-reologija-konstitutivna-motivacija-newtonov-zakon-viskozno-03}

Kad se prijelaz s jedne brzine na drugu više ne promatra kao konačna razlika nego kao lokalni gradijent profila brzine, omjer $U/\delta$ prelazi u diferencijalni zapis $dv/dy$, pa nastaje Newtonov zakon viskoznosti

$$
τ = \mu\frac{dv}{dy}.
$$ {#eq-reologija-konstitutivna-motivacija-newtonov-zakon-viskozno-04}

U tom zapisu $\tau$ označuje komponentu smičnoga naprezanja s unaprijed odabranim pozitivnim smjerovima. Promijene li se orijentacija normale ili smjer brzine, mijenja se i predznak te komponente; $|\tau|$ je njezin iznos. Veličina $\mu$ mjeri unutarnji otpor fluida relativnom klizanju slojeva, a $dv/dy$ pokazuje koliko se brzo brzina mijenja po okomici na strujanje.

Za kapilarni uspon promatra se kružna kapilara promjera $d$. Površinska napetost $\sigma$ djeluje duž cijeloga oboda, pa je ukupna sila na kontaktnoj liniji jednaka $\sigma\pi d$. Njezina vertikalna komponenta iznosi

$$
F_{\sigma,z} = \sigma\pi d\cos\theta,
$$ {#eq-reologija-konstitutivna-motivacija-newtonov-zakon-viskozno-05}

dok je težina podignutoga stupca tekućine

$$
G = \rho gV = \rho g\frac{\pi d^2}{4}h.
$$ {#eq-reologija-konstitutivna-motivacija-newtonov-zakon-viskozno-06}

U ravnoteži mora vrijediti $F_{\sigma,z}=G$, pa slijedi

$$
\sigma \pi d \cos\theta = \rho g \frac{\pi d^2}{4} h
$$ {#eq-reologija-konstitutivna-motivacija-newtonov-zakon-viskozno-07}

::: {.callout-note}
## Razrada koraka
Korak: jednadžba ravnoteže → $h = 4\sigma\cos\theta / (\rho g d)$

Dijeljenje obje strane s $\pi d$ (koji se pojavljuje na obje strane):
$$
\sigma \cos\theta = \rho g \frac{d}{4} h.
$$ {#eq-reologija-razrada-koraka-01}
Zatim se $h$ izolira dijeljenjem s $\rho g d/4$:
$$
h = \frac{4\sigma \cos\theta}{\rho g d}.
$$ {#eq-reologija-razrada-koraka-02}
Faktor $\pi$ otpada jer je zajednički objema stranama jednadžbe ravnoteže. Jedna potencija promjera skrati se između obodne površinske sile i težine stupca, pa u konačnom izrazu ostaje $d$ u nazivniku.
:::

i zato

$$
h = \frac{4\sigma \cos\theta}{\rho g d}.
$$ {#eq-reologija-razrada-koraka-03}

Iz iste relacije čita se i puni fizikalni smisao pojave: veća površinska napetost povećava uspon, veći promjer kapilare ga smanjuje, a znak člana $\cos\theta$ odlučuje radi li se o usponu ili padu. Kad je $\theta < 90^\circ$, tekućina kvasi stijenku i stupac raste; kad je $\theta > 90^\circ$, kapilarna pojava djeluje u suprotnom smjeru. Omjeri površinske napetosti prema inerciji i prema gravitaciji formaliziraju se Weberovim i Bondovim brojem u <span class="mf1-ch-ref"><span class="mf1-ch-code">pog. 11</span><span class="mf1-ch-title">Dimenzijska analiza i sličnost</span></span>.
:::

## Dinamička i kinematička viskoznost

Za inženjerski rad treba odmah razdvojiti dvije veličine:

$$
\mu\ [\text{Pa s}]
$$ {#eq-reologija-dinamicka-i-kinematicka-viskoznost-01}

$$
\nu = \frac{\mu}{\rho}\ [\text{m}^2/\text{s}]
$$ {#eq-reologija-dinamicka-i-kinematicka-viskoznost-02}

::: {.mf1-fizikalno-znacenje}
<p class="mf1-box-label">Fizikalno značenje</p>
Kinematička viskoznost $\nu$ kombinira viskozni prijenos količine gibanja ($\mu$) s masenom inercijom ($\rho$), pa se može tumačiti kao **difuzivnost količine gibanja**. Upravo $\nu$ nastupa u Reynoldsovu broju $Re=UL/\nu$. Dva nestlačiva Newtonska fluida s jednakim $\nu$ imaju isti Reynoldsov broj pri istoj referentnoj brzini i duljini; isti bezdimenzijski uzorak strujanja očekuje se tek za geometrijski slične domene, jednake bezdimenzijske rubne uvjete i jednake ostale relevantne bezdimenzijske skupine.
:::

Dinamička viskoznost govori koliki otpor fluid daje smičanju, a kinematička viskoznost taj isti otpor povezuje s gustoćom fluida. Ako se te dvije veličine pomiješaju, kasnije se pogrešno čitaju Reynoldsov broj i otpor strujanja.

::: {#ex-u02-pretvorba-dinamicke-u-kinematicku-viskoznost-t1 .mf1-we}
<p class="mf1-box-label">Kratki primjer — Pretvorba dinamičke u kinematičku viskoznost&nbsp;<span class="mf1-level">T1</span></p>

**Kontekst:** Za procjenu Reynoldsovog broja u hidrauličkom sustavu potrebno je dinamičku viskoznost ulja izraziti kao kinematičku viskoznost, što se izvodi izravno pomoću gustoće tog ulja.

**Zadano**

- Dinamička viskoznost hidrauličnog ulja: $\mu = 0{,}18\ \text{Pa s}$
- Gustoća ulja: $\rho = 900\ \text{kg/m}^3$

**Traženo**

Odredi kinematičku viskoznost $\nu$.

![Kratki primjer: ν = μ/ρ – kinematička viskoznost ulja (μ=0,18 Pa·s, ρ=900 kg/m³)](../assets/print/u02_fig_kinematicka_viskoznost.svg){#fig-u02-kinematicka-viskoznost fig-align="center" fig-alt="Kratki primjer: ν = μ/ρ – kinematička viskoznost ulja (μ=0,18 Pa·s, ρ=900 kg/m³)"}

**Pretpostavke i model**

Promatra se samo veza između dinamičke i kinematičke viskoznosti, pa vrijedi izravna relacija

$$
\nu = \frac{\mu}{\rho}.
$$ {#eq-reologija-kratki-primjer-pretvorba-dinamicke-u-kinematicku-01}

**Rješenje**

Uvrštavanjem zadanih podataka dobiva se

$$
\nu = \frac{\mu}{\rho} = \frac{0{,}18}{900} = 2{,}00 \cdot 10^{-4}\ \text{m}^2/\text{s}.
$$ {#eq-reologija-kratki-primjer-pretvorba-dinamicke-u-kinematicku-02}

**Provjera i komentar**

1. Kinematička viskoznost mora imati jedinicu površine po vremenu.
2. Pri istoj dinamičkoj viskoznosti veća gustoća daje manji $\nu$.
3. Ovaj korak ne govori još ništa o smičnom naprezanju; on samo pravilno prevodi jednu viskoznost u drugu.
:::

## Newtonov zakon viskoznosti

Za Newtonski fluid smično naprezanje raste linearno s gradijentom brzine:

$$
{}\tau = \mu \frac{dv}{dy}
$$ {#eq-reologija-newtonov-zakon-viskoznosti-01}

To nije univerzalni zakon za sve fluide, nego model za one fluide kod kojih je odnos linearan. U jednostavnom sloju fluida između dvije paralelne ploče, ako je profil brzine linearan, vrijedi i praktični zapis

$$
{}\tau = \mu \frac{v}{\delta}
$$ {#eq-reologija-newtonov-zakon-viskoznosti-02}

gdje je $\delta$ razmak među pločama.

::: {.callout-note collapse="true" icon="false"}
## Numerički trag

Newtonov zakon viskoznosti $\tau=\mu\,dv/dy$ ulazi u numerički model kao **konstitutivni zakon** koji povezuje naprezanje s gradijentom brzine i time zatvara viskozni član jednadžbe količine gibanja. Za nenewtonske fluide, poput svježega betona, isplake ili krvi u odgovarajućem rasponu smicanja, treba odabrati drugi konstitutivni model i njegove parametre odrediti iz podataka.
:::

::: {.mf1-dublje}
<p class="mf1-box-label">Dublje — Tenzor viskoznih naprezanja u trodimenzijskom strujanju</p>

Newtonov zakon viskoznosti $\tau = \mu\,dv/dy$ predstavljen je za **jednodimenzijsko strujanje** u kojem brzina ima samo jednu komponentu, a gradijent samo u jednom smjeru. U realnim trodimenzijskim strujanjima brzina ima tri komponente $u_1, u_2, u_3$ koje mogu varirati u sva tri smjera $x_1, x_2, x_3$, pa viskozno dodatno naprezanje postaje tenzor drugog reda.

Za **nestlačivi Newtonov fluid** poopćeni Newtonov zakon glasi

$$
\tau_{ij} = \mu\!\left(\frac{\partial u_i}{\partial x_j} + \frac{\partial u_j}{\partial x_i}\right),
$$ {#eq-reologija-dublje-tenzor-viskoznih-naprezanja-u-trodimenzij-01}

gdje su indeksi $i, j = 1, 2, 3$ koordinate prostora. Komponenta $\tau_{ij}$ djeluje u smjeru osi $i$ na plohu okomitu na os $j$: izvandijagonalne komponente ($i\ne j$) jesu smične, a dijagonalne ($i=j$) jesu viskozna normalna dodatna naprezanja.

Tenzor je **simetričan** ($\tau_{ij} = \tau_{ji}$), što fizikalno znači da svaka tri smična para djeluju jednako uzajamno — posljedica je to ravnoteže momenata na infinitezimalnom elementu fluida.

Iz tenzorske forme izlazi važan rezultat: trag tenzora (zbroj dijagonalnih elemenata) za nestlačivi fluid iščezava

$$
\tau_{11} + \tau_{22} + \tau_{33} = 2\mu\!\left(\frac{\partial u_1}{\partial x_1} + \frac{\partial u_2}{\partial x_2} + \frac{\partial u_3}{\partial x_3}\right) = 2\mu\,\nabla\cdot\vec{u} = 0,
$$ {#eq-reologija-dublje-tenzor-viskoznih-naprezanja-u-trodimenzij-02}

što znači da viskoznost ne dodaje vlastiti **izotropni dio** naprezanja — taj je dio u potpunosti pokriven tlakom $p$.

Skalarni jednodimenzijski oblik $\tau = \mu\,dv/dy$ koristi se kao radna verzija u svim $1$D problemima ovog poglavlja. Tenzorski zakon i njegov ulazak u Navier–Stokesovu jednadžbu sustavno se obrađuju u <span class="mf1-ch-ref"><span class="mf1-ch-code">pog. 12</span><span class="mf1-ch-title">Diferencijalni opis realnog toka</span></span>.
:::

## Površinska napetost i kontaktni kut

Na slobodnoj površini molekule nisu okružene susjedima kao u unutrašnjosti fluida. Zato površina nosi dodatnu energiju i ponaša se kao da je pod zatezanjem. Taj učinak opisuje se površinskom napetošću $\sigma$.

Površinska napetost ima dvostruku interpretaciju koja je istovremeno korisna. Mjeri se u jedinicama $\text{N/m}$ kao sila po jediničnoj duljini kontaktne linije, ali jednako vrijedi $\text{N/m} = \text{N}\cdot\text{m}/\text{m}^2 = \text{J/m}^2$, što znači da se $\sigma$ može čitati i kao energija po jediničnoj površini. Stvaranje nove površine fluida zahtijeva uložen rad jednak $\sigma \cdot \Delta A$, pa minimum energije pri zadanom volumenu objašnjava zašto kapljice u stanju bestežinskosti i sapunasti mjehuri zauzimaju sferni oblik — sfera, naime, ima najmanju površinu pri zadanom volumenu.

Kad je fluid u dodiru sa stijenkama, presudan postaje i kontaktni kut $\theta$. Znak i iznos $\cos \theta$ odlučuju penje li se tekućina u tankoj kapilari ili se razina spušta.

::: {.mf1-izvod}
<p class="mf1-box-label">Matematički izvod — Youngova jednadžba i podrijetlo kontaktnog kuta</p>

Vrijednost kontaktnog kuta $\theta$ nije proizvoljna, nego proizlazi iz ravnoteže triju površinskih napetosti na trokontaktnoj liniji na kojoj se susreću kruta stijenka, tekućina i para. Na tu liniju djeluju tri sile po jedinici duljine:

- napetost između krutine i pare: $\sigma_{sv}$, koja vuče po krutoj površini prema van od tekućine;
- napetost između krutine i tekućine: $\sigma_{sl}$, koja vuče po krutoj površini prema tekućini;
- napetost između tekućine i pare: $\sigma_{lv}$, koja vuče po slobodnoj površini tekućine pod kutom $\theta$ prema krutoj plohi.

Tangencijalna ravnoteža duž krute površine glasi

$$
\sigma_{sv} = \sigma_{sl} + \sigma_{lv}\cos\theta,
$$ {#eq-reologija-matematicki-izvod-youngova-jednadzba-i-podrijetl-01}

odakle slijedi **Youngova jednadžba**

$$
\cos\theta = \frac{\sigma_{sv} - \sigma_{sl}}{\sigma_{lv}}.
$$ {#eq-reologija-matematicki-izvod-youngova-jednadzba-i-podrijetl-02}

Veličina $\sigma$ koja se koristi u kapilarnom usponu i u svim formulama koje slijede zapravo je $\sigma_{lv}$ — napetost između tekućine i pare. Ako krutina kvasi tekućinu (npr. voda na čistom staklu), vrijedi $\sigma_{sv} > \sigma_{sl}$, pa je $\cos\theta > 0$ i $\theta < 90^\circ$. Ako krutina ne kvasi tekućinu (npr. živa na staklu, voda na voštanoj površini), vrijedi $\sigma_{sv} < \sigma_{sl}$, pa je $\cos\theta < 0$ i $\theta > 90^\circ$.

Kvašenje i nekvašenje time prestaju biti svojstvo same tekućine — postaju **svojstvo para tekućina–krutina**. Ista voda u staklenoj kapilari kvasi ($\theta \approx 0$), u teflonskoj ne kvasi ($\theta > 90^\circ$), a kapilarni uspon ili pad mijenja predznak.
:::

Za kapilarni uspon vrijedi radni zapis

$$
h = \frac{4\sigma \cos\theta}{\rho g d}
$$ {#eq-reologija-matematicki-izvod-youngova-jednadzba-i-podrijetl-03}

::: {.mf1-fizikalno-znacenje}
<p class="mf1-box-label">Fizikalno značenje</p>
Formula za $h$ sadržava sva četiri aktera kapilarnosti: površinska napetost $\sigma$ "vuče" tekućinu gore, $\cos\theta$ smanjuje tu silu za parcijalno kvašenje (za $\theta > 90^\circ$ ona okrene smjer i tekućina pada), a gustoća $\rho$ i gravitacija $g$ pružaju otpor težine stupca. Promjer $d$ stoji u nazivniku: prepoloviti promjer znači udvostručiti uspon. Zato je kapilarnost odlučujuća u tankim porama betona i opeke, ali zanemariva u cijevima centimetarskog ili većeg promjera.
:::

::: {.mf1-interaktivno}
<p class="mf1-box-label">Interaktivni prikaz — Kapilarni uspon</p>

Interaktivni prikaz omogućuje mijenjanje površinske napetosti $\sigma$, kontaktnog kuta $\theta$ i promjera kapilare $d$ uz neposredno praćenje ravnotežne visine $h$. Krivulja $h(d)$ pokazuje karakterističnu ovisnost u logaritamskim koordinatama.

<div class="mf1-interaktivno-akcija">
<a class="mf1-interaktivno-veza" href="https://martibasic.github.io/MF1_udzbenik/jlite/lab/index.html?path=u02_kapilarni_uspon.ipynb">Pokreni u pregledniku</a>
<a class="mf1-interaktivno-veza" href="https://colab.research.google.com/github/martibasic/MF1_udzbenik/blob/main/notebooks/u02_kapilarni_uspon.ipynb" target="_blank" rel="noopener">Pričuvno: otvori u Colabu</a>
<img class="mf1-interaktivno-qr" src="../assets/qr/u02_kapilarni_uspon.svg" alt="QR kod za interaktivni prikaz kapilarnog uspona"/>
</div>

<div class="mf1-interaktivno-pitanja">
**Pitanja za samostalno istraživanje:** (a) Što se događa s usponom pri $\theta = 90°$ i pri $\theta > 90°$? (b) Koji eksponent ovisnosti $h \propto d^{?}$ slijedi iz formule? (c) Zašto je kapilarnost značajna u porama betona, ali zanemariva u cijevima centimetarskog promjera?
</div>
:::

pa su male promjene promjera cijevi ili kontaktnog kuta odmah vidljive na visini stupca. Kad je $\theta > 90^\circ$, izraz daje negativan $h$, što znači da se ne javlja kapilarni uspon nego kapilarni pad.

Za zakrivljenu slobodnu površinu nastaje karakterističan skok tlaka koji je posljedica iste ravnoteže sila kao i kod kapilarnog uspona, samo primijenjene na zatvoreni mjehurić. Za kapljicu s jednom granicom faza tlak skoka je $\Delta p = 4\sigma/d$, dok je za sapunasti mjehur s dvjema slobodnim površinama $\Delta p = 8\sigma/d$.

::: {.mf1-izvod}
<p class="mf1-box-label">Matematički izvod — Young-Laplaceov zakon za kapljicu i mjehurić</p>

Promatra se sferna kapljica polumjera $r$ koja je u dodiru s okolnim plinom. Tlak unutar kapljice ($p_u$) veći je od tlaka u plinu ($p_v$) jer ga zatvara površinska napetost. Ravnoteža sila se najlakše postavlja po horizontalnoj presječnoj ravnini koja prolazi kroz ekvator kapljice; gornja polusfera mora ostati u ravnoteži pod djelovanjem dviju suprotno usmjerenih sila:

- sile tlačne razlike, koja tjera polusferu od ekvatora prema van — djeluje na projiciranu kružnu površinu $A_{proj} = \pi r^2$ i iznosi

$$
F_{tlak} = (p_u - p_v)\,\pi r^2,
$$ {#eq-reologija-matematicki-izvod-young-laplaceov-zakon-za-kaplj-01}

- sile površinske napetosti, koja gornju polusferu vuče prema dolje duž ekvatorske kružnice duljine $L = 2\pi r$:

$$
F_\sigma = \sigma \cdot 2\pi r.
$$ {#eq-reologija-matematicki-izvod-young-laplaceov-zakon-za-kaplj-02}

U ravnoteži vrijedi $F_{tlak} = F_\sigma$, odnosno

$$
(p_u - p_v)\,\pi r^2 = \sigma \cdot 2\pi r,
$$ {#eq-reologija-matematicki-izvod-young-laplaceov-zakon-za-kaplj-03}

odakle se kraćenjem zajedničkog faktora $\pi r$ dobiva tlačni skok

$$
\Delta p = p_u - p_v = \frac{2\sigma}{r} = \frac{4\sigma}{d}.
$$ {#eq-reologija-matematicki-izvod-young-laplaceov-zakon-za-kaplj-04}

Za **sapunasti mjehur** s dvije slobodne površine (unutarnja i vanjska opna) sila površinske napetosti je dvostruka jer obje opne dijele isti ekvatorski obod:

$$
F_\sigma = 2\cdot\sigma\cdot 2\pi r = 4\pi r\sigma,
$$ {#eq-reologija-matematicki-izvod-young-laplaceov-zakon-za-kaplj-05}

pa je tlačni skok

$$
\Delta p = \frac{4\sigma}{r} = \frac{8\sigma}{d}.
$$ {#eq-reologija-matematicki-izvod-young-laplaceov-zakon-za-kaplj-06}

Za općenitu zakrivljenu plohu s glavnim polumjerima zakrivljenosti $R_1$ i $R_2$, opći **Young-Laplaceov zakon** glasi

$$
\Delta p = \sigma\!\left(\frac{1}{R_1} + \frac{1}{R_2}\right),
$$ {#eq-reologija-matematicki-izvod-young-laplaceov-zakon-za-kaplj-07}

Pri tome je ovdje $\Delta p=p_{unutra}-p_{vani}$, a zakrivljenosti su pozitivne za konveksnu kapljicu promatranu iz unutarnje faze. Uz drugu orijentaciju normale predznaci zakrivljenosti i tlačnoga skoka moraju se promijeniti zajedno. Za sferu ($R_1 = R_2 = r$) tako se dobiva $\Delta p = 2\sigma/r$, a za cilindar ($R_2 \to \infty$) $\Delta p = \sigma/R$.
:::

::: {.mf1-fizikalno-znacenje}
<p class="mf1-box-label">Fizikalno značenje</p>
Zakrivljena površina zahtijeva tlačni skok koji uravnotežuje površinsku napetost. Što je manji promjer, to je veća zakrivljenost i veći potreban skok tlaka. Faktor 4 za kapljicu nastaje jer sfera ima jednu granicu faza i polumjer $r=d/2$; faktor 8 za sapunasti mjehur dolazi od dviju površina opne. Pri kavitaciji mjehuri pare mogu nastati i rasti kada lokalni **apsolutni** tlak dovoljno padne u odnosu na tlak pare. Stvarni prag ovisi i o prisutnim jezgrama, otopljenim plinovima te Laplaceovu nadtlaku $2\sigma/r$; površinska napetost zato otežava rast vrlo malih jezgara, a ne daje jednostavan kriterij „tlaka koji zatvara mikrokapljicu”.
:::

## Riješeni primjeri

::: {#ex-u02-smicno-naprezanje-u-tankom-uljnom-sloju-t2 .mf1-we}
<p class="mf1-box-label">Riješeni primjer — Smično naprezanje u tankom uljnom sloju&nbsp;<span class="mf1-level">T2</span></p>

**Kontekst:** Tanak sloj ulja između dviju paralelnih ploča je tipičan model za hidrauličku brtvu ili klizni element. Treba odrediti gradijent brzine, smično naprezanje, silu vučenja i kinematičku viskoznost.

**Zadano**

- Debljina uljnog sloja: $\delta = 3\ \text{mm}$
- Brzina gornje ploče: $v = 0{,}90\ \text{m/s}$
- Aktivna površina ploče: $A = 0{,}18\ \text{m}^2$
- Dinamička viskoznost ulja: $\mu = 0{,}42\ \text{Pa s}$
- Gustoća ulja: $\rho = 870\ \text{kg/m}^3$

**Traženo**

1. Odredi gradijent brzine $dv/dy$.
2. Odredi smično naprezanje $\tau$.
3. Odredi silu potrebnu za jednoliko gibanje gornje ploče.
4. Odredi kinematičku viskoznost $\nu$.

![viskoznost i kapilarnost](../assets/print/u02_val2_viskoznost_kapilarnost.svg){#fig-u02-viskoznost-i-kapilarnost fig-alt="viskoznost i kapilarnost"}

**Pretpostavke i model**

Promatra se linearni profil brzine između dviju paralelnih ploča. Zato je gradijent brzine konstantan, a smično naprezanje dobiva se iz Newtonova zakona viskoznosti.

**Rješenje**

Najprije razmak pretvorimo u metre:

$$
\delta = 0{,}003\ \text{m}.
$$ {#eq-reologija-rijeseni-primjer-smicno-naprezanje-u-tankom-uljn-01}

pa je gradijent brzine

$$
\frac{dv}{dy} = \frac{v}{\delta} = \frac{0{,}90}{0{,}003} = 300\ \text{s}^{-1}.
$$ {#eq-reologija-rijeseni-primjer-smicno-naprezanje-u-tankom-uljn-02}

smično naprezanje iznosi

$$
{}\tau = \mu \frac{dv}{dy} = 0{,}42 \cdot 300 = 126\ \text{Pa}.
$$ {#eq-reologija-rijeseni-primjer-smicno-naprezanje-u-tankom-uljn-03}

Sila na ploči zato je

$$
F = \tau A = 126 \cdot 0{,}18 = 22{,}68\ \text{N} \approx 22{,}7\ \text{N}.
$$ {#eq-reologija-rijeseni-primjer-smicno-naprezanje-u-tankom-uljn-04}

kinematička viskoznost glasi

$$
\nu = \frac{\mu}{\rho} = \frac{0{,}42}{870} = 4{,}83 \cdot 10^{-4}\ \text{m}^2/\text{s}.
$$ {#eq-reologija-rijeseni-primjer-smicno-naprezanje-u-tankom-uljn-05}

**Provjera i komentar**

1. Manji razmak među pločama mora povećati gradijent brzine.
2. Veća viskoznost mora povećati smično naprezanje i potrebnu silu.
3. Red veličine sile od nekoliko desetaka njutna razuman je za ovakav sloj i površinu.
:::

::: {#ex-u02-kapilarni-uspon-etanola-u-staklenoj-cjevcici-t1 .mf1-we}
<p class="mf1-box-label">Riješeni primjer — Kapilarni uspon etanola u staklenoj cjevčici&nbsp;<span class="mf1-level">T1</span></p>

**Kontekst:** Staklena kapilara uronjena u etanol pokazuje kapilarni uspon manji nego u potpunom kvašenju jer kontaktni kut nije nula. Treba odrediti visinu kapilarnog uspona.

**Zadano**

- Unutarnji promjer kapilare: $d = 1{,}0\ \text{mm}$
- Površinska napetost etanola: $\sigma = 0{,}022\ \text{N/m}$
- Gustoća etanola: $\rho = 790\ \text{kg/m}^3$
- Gravitacijsko ubrzanje: $g = 9{,}81\ \text{m/s}^2$
- Kontaktni kut etanol-staklo: $\theta = 18^\circ$

**Traženo**

Odredi visinu kapilarnog uspona $h$.

![Kapilarni uspon etanola u staklenoj kapilari (d=1,0 mm, θ=18°, h≈10,8 mm)](../assets/print/u02_fig_kapilarni_uspon_etanol.svg){#fig-u02-kapilarni-uspon-etanol fig-align="center" fig-alt="Kapilarni uspon etanola u staklenoj kapilari (d=1,0 mm, θ=18°, h≈10,8 mm)"}

**Pretpostavke i model**

Kontaktni kut ovdje nije nula, pa se kapilarni uspon ne smije računati kao potpuno kvašenje. U visinu uspona ulazi faktor $\cos\theta$, koji smanjuje vertikalnu komponentu površinske sile.

**Rješenje**

Promjer u metrima iznosi $d = 1{,}0 \cdot 10^{-3}\ \text{m}$, a za zadani kontaktni kut vrijedi $\cos 18^\circ \approx 0{,}951$, pa je kapilarni uspon

$$
h = \frac{4\sigma\cos\theta}{\rho g d} = \frac{4 \cdot 0{,}022 \cdot 0{,}951}{790 \cdot 9{,}81 \cdot 1{,}0 \cdot 10^{-3}} = 0{,}0108\ \text{m} \approx 1{,}08\ \text{cm}.
$$ {#eq-reologija-rijeseni-primjer-kapilarni-uspon-etanola-u-stakl-01}

**Provjera i komentar**

1. Kako je $\theta < 90^\circ$, razina mora rasti, a ne padati.
2. Tanja kapilara mora dati veći uspon.
3. Neto uspon mora biti manji nego u slučaju potpunog kvašenja jer je ovdje $\cos\theta < 1$.
:::

::: {#ex-u02-kapilarni-mikrodozator-s-izlaznom-kapljicom-t3 .mf1-ch}
<p class="mf1-box-label">Cjeloviti zadatak — Kapilarni mikrodozator s izlaznom kapljicom&nbsp;<span class="mf1-level">T3</span></p>

**Kontekst:** U laboratorijskom mikrodozatoru voda iz spremnika diže se tankom staklenom kapilarom do izlaza na kojem nastaje gotovo sferna kapljica. Treba odrediti kapilarni uspon, Laplaceov skok tlaka na kapljici i najmanji potreban pretlak u spremniku da uređaj pouzdano dozira.

**Zadano**

- Unutarnji promjer vertikalne staklene kapilare: $d = 0{,}80\ \text{mm}$
- Gustoća vode: $\rho = 998\ \text{kg/m}^3$
- Površinska napetost vode: $\sigma = 0{,}072\ \text{N/m}$
- Kontaktni kut voda-staklo (potpuno kvašenje): $\theta = 0^\circ$
- Visina izlaza kapilare iznad slobodne površine u spremniku: $H = 60\ \text{mm}$
- Promjer gotovo sferne izlazne kapljice: $D = 2{,}4\ \text{mm}$

Iznad vode u spremniku može se po potrebi zadati mali manometarski pretlak $p_M$.

**Traženo**

1. kapilarni uspon $h_{cap}$ kada je spremnik otvoren prema atmosferi.
2. tlakovni skok $\Delta p$ na izlaznoj kapljici i apsolutni tlak unutar kapljice.
3. najmanji manometarski pretlak $p_{M,min}$ koji treba zadati spremniku da voda dosegne izlaz i održi kapljicu promjera $D$.
4. je li kapilarnost sama dovoljna da voda dosegne izlaz bez dodatnog pretlaka.

Pretpostavi da je kapljica kvazistacionarna, da je gubitak u kapilari zanemariv i da se kapilarni uspon može čitati iz standardne relacije za potpunu vlažnost.

![kapilarni mikrodozator s izlaznom kapljicom](../assets/print/u02_ch1_kapilarni_mikrodozator_kapljica.svg){#fig-u02-kapilarni-mikrodozator-s-izlaznom-kapljicom fig-alt="kapilarni mikrodozator s izlaznom kapljicom"}

**Pretpostavke i model**

Kapilarnost i Laplaceov skok ovdje djeluju u istom uređaju, ali ih treba čitati odvojeno. Kapilarnost sama daje koliko se voda može podići u tankoj cjevčici bez dodatnog pogona. Ako izlaz leži više od tog uspona, ostatak visine mora se savladati dodatnim pretlakom u spremniku. Na samom izlazu zatim treba još zatvoriti skok tlaka preko zakrivljene površine kapljice.

**Rješenje**

### 1. Kapilarni uspon

Za vodu u staklenoj kapilari pri $\theta = 0^\circ$ ($\cos 0^\circ = 1$) vrijedi

$$
h_{cap} = \frac{4\sigma \cos\theta}{\rho g d} = \frac{4 \cdot 0{,}072}{998 \cdot 9{,}81 \cdot 0{,}80 \cdot 10^{-3}} = 0{,}0368\ \text{m} \approx 36{,}8\ \text{mm}.
$$ {#eq-reologija-1-kapilarni-uspon-01}

#### 2. Tlakovni skok na kapljici

Za gotovo sfernu kapljicu, uz $D = 2{,}4\ \text{mm} = 2{,}4 \cdot 10^{-3}\ \text{m}$, relacija Young-Laplace daje

$$
\Delta p = \frac{4\sigma}{D} = \frac{4 \cdot 0{,}072}{2{,}4 \cdot 10^{-3}} = 120\ \text{Pa}.
$$ {#eq-reologija-2-tlakovni-skok-na-kapljici-01}

Ako je vanjski tlak atmosferski,

$$
p_{in} = p_0 + \Delta p = 101325 + 120 = 101445\ \text{Pa} \approx 101{,}45\ \text{kPa}.
$$ {#eq-reologija-2-tlakovni-skok-na-kapljici-02}

#### 3. Najmanji potreban pretlak u spremniku

Izlaz kapilare nalazi se na visini $H = 60\ \text{mm}$, a kapilarnost sama može podići vodu samo do $h_{cap}$. Preostala hidrostatička razlika $H - h_{cap} = 60 - 36{,}8 = 23{,}2\ \text{mm}$ odgovara dodatnom tlaku

$$
p_H = \rho g (H - h_{cap}) = 998 \cdot 9{,}81 \cdot (0{,}060 - 0{,}0368) = 227\ \text{Pa}.
$$ {#eq-reologija-3-najmanji-potreban-pretlak-u-spremniku-01}

Na izlazu treba još savladati i tlačni skok na kapljici, pa je najmanji potreban manometarski pretlak

$$
p_{M,min} = p_H + \Delta p = 227 + 120 = 347\ \text{Pa} \approx 0{,}347\ \text{kPa}.
$$ {#eq-reologija-3-najmanji-potreban-pretlak-u-spremniku-02}

#### 4. Je li kapilarnost sama dovoljna?

Kapilarnost sama bila bi dovoljna kada bi vrijedilo $h_{cap} \geq H$. Ovdje je, međutim, $36{,}8\ \text{mm} < 60\ \text{mm}$, pa sama kapilarnost nije dovoljna da voda dosegne izlaz. Potreban je mali dodatni pretlak u spremniku.

**Provjera i komentar**

Kapilarnost sama podiže vodu za oko $36{,}8\ \text{mm}$, dok izlaz mikrodozatora leži na $60\ \text{mm}$ iznad spremnika. Zato je za dosezanje izlaza potreban dodatni tlak od oko $227\ \text{Pa}$, a za zadržavanje kapljice promjera $2{,}4\ \text{mm}$ treba još oko $120\ \text{Pa}$ Laplaceova skoka. Ukupno je potreban minimalni manometarski pretlak od oko $347\ \text{Pa}$, a apsolutni tlak unutar kapljice iznosi oko $101{,}45\ \text{kPa}$.

1. Manja kapilarna cjevčica mora davati veći kapilarni uspon, pa bi smanjenje promjera olakšalo doseg izlaza.
2. Manja kapljica mora tražiti veći tlačni skok, pa bi smanjenje promjera kapljice povećalo potrebni pretlak.
3. Kako je $h_{cap} < H$, dodatni pogonski tlak mora biti pozitivan; negativan rezultat ovdje bi odmah značilo da je negdje izgubljen znak ili pretvorba jedinica.
::: 

::: {#ex-u02-hladni-start-i-radna-temperatura-koliko-kosta .mf1-we}
<p class="mf1-box-label">Riješeni primjer — Hladni start i radna temperatura: koliko košta hladno ulje &nbsp;<span class="mf1-level">T2</span></p>

**Primjer za strojare**

**Kontekst:** U ovoj kontroliranoj usporedbi isti idealizirani klizni ležaj promatra se pri dvjema zadanim temperaturama i dvjema zadanim dinamičkim viskoznostima. Cilj je izdvojiti samo linearnu ovisnost Couetteova smičnog otpora o $\mu$; primjer ne predstavlja radnu kartu određenoga motora niti uputu za njegovo rukovanje.

**Zadano**

Isti klizni ležaj radi pri dvjema temperaturama:

- Promjer vratila: $D = 50\ \text{mm}$
- Duljina ležaja: $L = 70\ \text{mm}$
- Uljni procjep: $\delta = 0{,}30\ \text{mm}$
- Brzina vrtnje: $n = 2400\ \text{min}^{-1}$
- Dinamička viskoznost pri $T_1 = 0^\circ\text{C}$: $\mu_1 = 0{,}40\ \text{Pa s}$
- Dinamička viskoznost pri $T_2 = 90^\circ\text{C}$: $\mu_2 = 0{,}040\ \text{Pa s}$

**Traženo**

1. Obodna brzina vratila i gradijent brzine u procjepu.
2. Smično naprezanje pri obje temperature.
3. Zakretni moment trenja pri obje temperature.
4. Snaga koju motor mora trošiti samo na svladavanje viskoznog trenja pri obje temperature i omjer hladne i tople snage.

![Klizni ležaj pri hladnom startu ($\mu_1 = 0{,}40$ Pa·s) i radnoj temperaturi ($\mu_2 = 0{,}040$ Pa·s) – ista geometrija, faktor 10 razlike u viskoznosti, faktor 10 razlike u snazi trenja.](../assets/print/u02_fig_lezaj_temperatura.svg){#fig-u02-lezaj-temperatura fig-align="center" fig-alt="Klizni ležaj pri hladnom startu ($\mu_1 = 0{,}40$ Pa·s) i radnoj temperaturi ($\mu_2 = 0{,}040$ Pa·s) – ista geometrija, faktor 10 razlike u viskoznosti, faktor 10 razlike u snazi trenja."}

**Pretpostavke i model**

Primjenjuje se idealni Couetteov model tankoga uljnog procjepa: vratilo i čahura su koncentrični, profil je linearan, $dv/dy=v/\delta$, a $\mu$ je u svakom stanju zadana i jednolika. Geometrija i broj okretaja ne mijenjaju se. Zanemaruju se hidrodinamički klin, ekscentricitet, opterećenje, rubni tok, lokalno zagrijavanje smicanjem i spregnuta toplinska bilanca. Zato se sve razlike u rezultatu namjerno pripisuju samo zadanoj promjeni viskoznosti.

**Rješenje**

Obodna brzina vratila ne ovisi o temperaturi:

$$
v = \frac{\pi D n}{60} = \frac{\pi \cdot 0{,}050 \cdot 2400}{60} \approx 6{,}28\ \text{m/s}
$$ {#eq-reologija-rijeseni-primjer-hladni-start-i-radna-temperatur-01}

Gradijent brzine u procjepu:

$$
\frac{dv}{dy} \approx \frac{v}{\delta} = \frac{6{,}28}{0{,}30 \cdot 10^{-3}} \approx 2{,}09 \cdot 10^4\ \text{s}^{-1}
$$ {#eq-reologija-rijeseni-primjer-hladni-start-i-radna-temperatur-02}

Smično naprezanje pri hladnom startu:

$$
\tau_1 = \mu_1 \frac{v}{\delta} = 0{,}40 \cdot 2{,}09 \cdot 10^4 \approx 8{,}38 \cdot 10^3\ \text{Pa}
$$ {#eq-reologija-rijeseni-primjer-hladni-start-i-radna-temperatur-03}

Smično naprezanje pri radnoj temperaturi:

$$
\tau_2 = \mu_2 \frac{v}{\delta} = 0{,}040 \cdot 2{,}09 \cdot 10^4 \approx 838\ \text{Pa}
$$ {#eq-reologija-rijeseni-primjer-hladni-start-i-radna-temperatur-04}

Kontaktna površina ležaja:

$$
A = \pi D L = \pi \cdot 0{,}050 \cdot 0{,}070 = 1{,}10 \cdot 10^{-2}\ \text{m}^2
$$ {#eq-reologija-rijeseni-primjer-hladni-start-i-radna-temperatur-05}

Sila viskoznog trenja i zakretni moment pri hladnom startu:

$$
F_1 = \tau_1 A \approx 92{,}2\ \text{N}, \qquad M_1 = F_1 \cdot \frac{D}{2} \approx 2{,}30\ \text{N m}
$$ {#eq-reologija-rijeseni-primjer-hladni-start-i-radna-temperatur-06}

Sila viskoznog trenja i zakretni moment pri radnoj temperaturi:

$$
F_2 = \tau_2 A \approx 9{,}22\ \text{N}, \qquad M_2 = F_2 \cdot \frac{D}{2} \approx 0{,}231\ \text{N m}
$$ {#eq-reologija-rijeseni-primjer-hladni-start-i-radna-temperatur-07}

Kutna brzina rotacije:

$$
\omega = \frac{2\pi n}{60} \approx 251{,}3\ \text{rad/s}
$$ {#eq-reologija-rijeseni-primjer-hladni-start-i-radna-temperatur-08}

Snaga koju motor mora trošiti samo zbog viskoznog trenja:

$$
P_1 = M_1 \omega \approx 2{,}30 \cdot 251{,}3 \approx 578\ \text{W}
$$ {#eq-reologija-rijeseni-primjer-hladni-start-i-radna-temperatur-09}

$$
P_2 = M_2 \omega \approx 0{,}231 \cdot 251{,}3 \approx 58{,}0\ \text{W}
$$ {#eq-reologija-rijeseni-primjer-hladni-start-i-radna-temperatur-10}

Omjer snage hladnog starta prema snazi pri radnoj temperaturi:

$$
\frac{P_1}{P_2} = \frac{\mu_1}{\mu_2} = 10
$$ {#eq-reologija-rijeseni-primjer-hladni-start-i-radna-temperatur-11}

**Provjera i komentar**

1. U ovom namjerno ograničenom modelu smično naprezanje, sila trenja, moment i snaga linearno se mijenjaju s viskoznošću. Zato faktor 10 u zadanoj $\mu$ daje faktor 10 u tim izlaznim veličinama.
2. Dobivenih $578\ \text{W}$ nije prognoza stvarnoga gubitka određenoga motora: rezultat snažno ovisi o idealiziranom procjepu i izostavljenim hidrodinamičkim i toplinskim učincima.
3. Omjer $P_1/P_2=\mu_1/\mu_2$ vrijedi jer su u usporedbi geometrija i brzina umjetno zadržane jednakima. U konstrukciji se istodobno biraju geometrija ležaja, dovod maziva, režim rada i odgovarajuće reološko-temperaturno svojstvo ulja; nijedan od tih čimbenika sam nije potpuna mjera.
:::

::: {#ex-u02-mikrofluidicki-kanal-u-lab-on-chip-ure .mf1-we}
<p class="mf1-box-label">Riješeni primjer — Mikrofluidički kanal u lab-on-chip uređaju za dijagnostiku &nbsp;<span class="mf1-level">T2</span></p>

**Kontekst:** U nekim dijagnostičkim uređajima vrste *lab-on-chip* uzorak se dovodi kapilarnim djelovanjem bez vanjske pumpe. Ovdje se promatra kružni mikrokanal od površinski obrađenoga ili obloženoga PDMS-a sa zadanim kontaktnim kutom $25^\circ$. Kontaktni se kut tretira kao ulazni podatak konkretne obrađene površine, a ne kao univerzalno svojstvo naziva materijala.

**Zadano**

- Promjer kapilarnog kanala: $d = 60\ \mu\text{m}$
- Površinska napetost uzorka (vodena otopina sa surfaktantom): $\sigma = 0{,}055\ \text{N/m}$
- Kontaktni kut tekućine na PDMS materijalu: $\theta = 25^\circ$
- Gustoća uzorka (krv razrijeđena s reagensom): $\rho = 1010\ \text{kg/m}^3$

**Traženo**

1. Maksimalna ravnotežna visina kapilarnog uspona;
2. Razlika tlakova na meniskusu prema Young-Laplaceovu zakonu;
3. Učinak hidrofobnog premaza kanala (promjena kontaktnog kuta na $\theta = 110^\circ$).

**Pretpostavke i model**

Mikrofluidički kanal je vertikalno orijentiran, kružnoga presjeka i jednoliko obrađene površine; kontaktni kut uzima se konstantnim duž stijenke. Promatra se ravnotežno stanje (Lucas-Washburnova kinetika punjenja zanemaruje se), a tekućina se aproksimira jednofaznim Newtonskim fluidom. Histereza kontaktnoga kuta, onečišćenje i promjena površinske obrade s vremenom nisu obuhvaćeni.

**Rješenje**

Ravnotežna visina kapilarnog uspona slijedi iz uvjeta ravnoteže sile površinske napetosti i težine stupca:

$$
h = \frac{4\sigma\cos\theta}{\rho g d} = \frac{4 \cdot 0{,}055 \cdot \cos 25^\circ}{1010 \cdot 9{,}81 \cdot 60 \cdot 10^{-6}}.
$$ {#eq-reologija-rijeseni-primjer-mikrofluidicki-kanal-u-lab-on-01}

Uvrštavanjem $\cos 25^\circ \approx 0{,}906$:

$$
h = \frac{4 \cdot 0{,}055 \cdot 0{,}906}{1010 \cdot 9{,}81 \cdot 6 \cdot 10^{-5}} = \frac{0{,}1993}{0{,}5945} \approx 0{,}335\ \text{m}.
$$ {#eq-reologija-rijeseni-primjer-mikrofluidicki-kanal-u-lab-on-02}

Dakle visina kapilarnog uspona iznosi približno

$$
h \approx 33{,}5\ \text{cm}.
$$ {#eq-reologija-rijeseni-primjer-mikrofluidicki-kanal-u-lab-on-03}

Razlika tlakova na meniskusu prema Young-Laplaceovu zakonu za kružni presjek:

$$
\Delta p = \frac{4\sigma\cos\theta}{d} = \frac{4 \cdot 0{,}055 \cdot 0{,}906}{60 \cdot 10^{-6}} \approx 3{,}32 \cdot 10^3\ \text{Pa} \approx 3{,}32\ \text{kPa}.
$$ {#eq-reologija-rijeseni-primjer-mikrofluidicki-kanal-u-lab-on-04}

Pri hidrofobnom premazu kanala ($\theta = 110^\circ$) vrijedi $\cos 110^\circ \approx -0{,}342$, pa rezultat postaje negativan:

$$
h_{hidrofobno} = \frac{4 \cdot 0{,}055 \cdot (-0{,}342)}{1010 \cdot 9{,}81 \cdot 6 \cdot 10^{-5}} \approx -0{,}127\ \text{m}.
$$ {#eq-reologija-rijeseni-primjer-mikrofluidicki-kanal-u-lab-on-05}

Negativna vrijednost znači kapilarnu depresiju u vertikalnoj cijevi. Ako tekućina tek treba ući u suh hidrofobni kanal, isti predznak odgovara kapilarnoj ulaznoj barijeri koju vanjski nadtlak mora svladati; sam rezultat ne dokazuje da tekućina ni u kojim uvjetima neće ući.

**Provjera i komentar**

Ravnotežna visina od oko $33{,}5\ \text{cm}$ pokazuje da je za zadanu idealnu kapilaru gravitacijska granica mnogo veća od centimetarske duljine uređaja. Time još nije dokazana pouzdanost ili brzina punjenja: za to treba uključiti viskozni otpor, zarobljeni plin, geometrijske prijelaze i dinamički kontaktni kut. Tlačni skok od $3{,}3\ \text{kPa}$ karakterizira meniskus; dimenzioniranje spojnica i pasivnih ventila zahtijeva puni raspon tlakova i stvarne uvjete kvašenja.
:::

::: {.mf1-samoprovjera}
<p class="mf1-box-label">Provjeri sebe</p>

Sljedeća pitanja služe za samostalnu provjeru razumijevanja prije prelaska na zadatke za vježbu. Preporučuje se prvo samostalno odgovoriti, a tek zatim otvoriti sklopivi blok s kratkim odgovorom.

1. Po čemu se razlikuju dinamička i kinematička viskoznost te zašto se uvodi i jedna i druga?

::: {.callout-note collapse="true"}
### Odgovor
Dinamička viskoznost $\mu$ (Pa·s) ulazi izravno u Newtonov zakon viskoznosti i veže smično naprezanje s gradijentom brzine. Kinematička viskoznost $\nu = \mu/\rho$ (m²/s) ima dimenziju difuzivnosti i prirodno se pojavljuje u bezdimenzijskim brojevima poput Reynoldsovog. Uvode se obje jer različiti zadaci zahtijevaju različitu prikladnu formu.
:::

2. Pri kojem se znaku člana $\cos\theta$ kapilarna pojava izvodi prema gore, a pri kojem prema dolje?

::: {.callout-note collapse="true"}
### Odgovor
Za $\theta < 90^\circ$ vrijedi $\cos\theta > 0$ pa kapilarni uspon je pozitivan i tekućina se penje (tekućina kvasi stijenku). Za $\theta > 90^\circ$ vrijedi $\cos\theta < 0$ pa kapilarna pojava daje pad razine (tekućina ne kvasi stijenku).
:::

3. Zašto je kapilarni uspon značajan u porama opeke, a praktički zanemariv u cijevi promjera dva centimetra?

::: {.callout-note collapse="true"}
### Odgovor
Kapilarni uspon je obrnuto proporcionalan promjeru, pa za pore reda $10\ \mu\text{m}$ daje desetke centimetara, dok za cijev od $20\ \text{mm}$ daje samo desetke mikrometara, što je u realnim uvjetima zanemarivo.
:::

4. Zašto Newtonov zakon viskoznosti ne vrijedi za svaki fluid?

::: {.callout-note collapse="true"}
### Odgovor
Newtonov zakon vrijedi samo za fluide kod kojih je veza između smičnog naprezanja i gradijenta brzine linearna. Mnoge stvarne tekućine (svježi beton, krv, polimerne otopine) nisu linearne; njihovo modeliranje zahtijeva proširene konstitutivne zakone poput Bingham, power-law ili Carreau modela.
:::
:::

## Zadaci za vježbu

::::: {.mf1-vjezbe-list}
1. [**T1**]{#task-u02-izme-u-dviju-paralelnih-ploca-nalazi-se} Između dviju paralelnih ploča nalazi se glicerin debljine $\delta = 2{,}4\ \text{mm}$. Gornja ploča površine $A = 0{,}22\ \text{m}^2$ giba se stalnom brzinom $v = 0{,}65\ \text{m/s}$, donja ploča miruje, a dinamička viskoznost glicerina iznosi $\mu = 0{,}84\ \text{Pa s}$. Odredi gradijent brzine, smično naprezanje i silu potrebnu za gibanje ploče.

   :::: {.content-visible .mf1-hint-online when-format="html"}
   ::: {.callout-note collapse="true" data-hint-key="true"}
   ### Naputak
   $dv/dy = v/\delta$, zatim $\tau = \mu dv/dy$ i na kraju $F = \tau A$.
   :::
   ::::
   :::: {.content-visible .mf1-answer-online when-format="html"}
   ::: {.callout-tip collapse="true" data-answer-key="true"}
   ### Kontrolni rezultat

   $dv/dy \approx 271\ \text{s}^{-1}$; $\tau \approx 228\ \text{Pa}$; $F \approx 50\ \text{N}$.
   :::
   ::::
   **Skica:** da - dvije ploče, razmak $\delta$, gornja brzina $v$ i aktivna površina $A$.

2. [**T1**]{#task-u02-klizna-ploca-povrsine-giba-se-brzinom-kroz} Klizna ploča površine $A = 0{,}14\ \text{m}^2$ giba se brzinom $v = 0{,}80\ \text{m/s}$ kroz uljni procjep debljine $\delta = 1{,}8\ \text{mm}$. Ako je mjerena vučna sila $F = 21\ \text{N}$, odredi dinamičku viskoznost ulja.

   :::: {.content-visible .mf1-hint-online when-format="html"}
   ::: {.callout-note collapse="true" data-hint-key="true"}
   ### Naputak
   iz $F = \tau A$ dobij $\tau$, a zatim iz $\tau = \mu v/\delta$ vrati $\mu$.
   :::
   ::::
   :::: {.content-visible .mf1-answer-online when-format="html"}
   ::: {.callout-tip collapse="true" data-answer-key="true"}
   ### Kontrolni rezultat

   $\tau = 150\ \text{Pa}$; $\mu \approx 0{,}34\ \text{Pa s}$.
   :::
   ::::
   **Skica:** da - ploča u procjepu s označenim $F$, $v$, $A$ i $\delta$.

3. [**T2**]{#task-u02-vratilo-promjera-i-duljine-vrti-se-tako} Vratilo promjera $D = 70\ \text{mm}$ i duljine $L = 0{,}24\ \text{m}$ vrti se tako da je obodna brzina $v = 1{,}6\ \text{m/s}$ u uljnom procjepu debljine $\delta = 0{,}60\ \text{mm}$. Dinamička viskoznost ulja je $\mu = 0{,}36\ \text{Pa s}$. Odredi smično naprezanje i silu smicanja na vratilu.

   :::: {.content-visible .mf1-hint-online when-format="html"}
   ::: {.callout-note collapse="true" data-hint-key="true"}
   ### Naputak
   koristi aproksimaciju ravnih slojeva: $\tau = \mu v/\delta$ i $F = \tau A$ uz $A = \pi DL$.
   :::
   ::::
   :::: {.content-visible .mf1-answer-online when-format="html"}
   ::: {.callout-tip collapse="true" data-answer-key="true"}
   ### Kontrolni rezultat

   $\tau = 960\ \text{Pa}$; $F \approx 51\ \text{N}$.
   :::
   ::::
   **Skica:** da - vratilo u ležajnom procjepu, oznake $D$, $L$, $\delta$ i smjer gibanja.

4. [**T2**]{#task-u02-kapilara-promjera-uronjena-je-u-etanol-za} Kapilara promjera $d = 0{,}60\ \text{mm}$ uronjena je u etanol za koji vrijedi $\sigma = 0{,}022\ \text{N/m}$, $\theta = 18^\circ$ i $\rho = 790\ \text{kg/m}^3$. Odredi kapilarni uspon i usporedi ga s usponom u drugoj kapilari promjera $1{,}20\ \text{mm}$.

   :::: {.content-visible .mf1-hint-online when-format="html"}
   ::: {.callout-note collapse="true" data-hint-key="true"}
   ### Naputak
   $h = 4\sigma \cos\theta /(\rho g d)$; drugi slučaj računa se istom formulom samo s novim promjerom.
   :::
   ::::
   :::: {.content-visible .mf1-answer-online when-format="html"}
   ::: {.callout-tip collapse="true" data-answer-key="true"}
   ### Kontrolni rezultat

   $h \approx 18{,}0\ \text{mm}$; kod $d = 1{,}2\ \text{mm}$ upola manje, $h \approx 9{,}0\ \text{mm}$.
   :::
   ::::
   **Skica:** da - dvije tanke kapilare, meniskus, kontaktni kut $\theta$ i različiti promjeri.

5. [**T3**]{#task-u02-staklena-kapilara-promjera-uronjena-je-u-vodu} Staklena kapilara promjera $d = 0{,}90\ \text{mm}$ uronjena je u vodu za koju vrijedi $\sigma = 0{,}072\ \text{N/m}$, $\theta = 10^\circ$ i $\rho = 998\ \text{kg/m}^3$. Odredi kapilarni uspon. Zatim odredi tlak skoka u kapljici vode promjera $d_k = 1{,}2\ \text{mm}$ nastaloj na izlazu raspršivača istog sustava.

   :::: {.content-visible .mf1-hint-online when-format="html"}
   ::: {.callout-note collapse="true" data-hint-key="true"}
   ### Naputak
   najprije kapilarni uspon iz $h = 4\sigma \cos\theta /(\rho g d)$, a zatim tlak skoka kapljice iz $\Delta p = 4\sigma/d_k$.
   :::
   ::::
   :::: {.content-visible .mf1-answer-online when-format="html"}
   ::: {.callout-tip collapse="true" data-answer-key="true"}
   ### Kontrolni rezultat

   $h \approx 32{,}2\ \text{mm}$; $\Delta p \approx 240\ \text{Pa}$.
   :::
   ::::
   **Skica:** da - kapilara s meniskusom i zasebno kapljica raspršivača s označenim promjerom $d_k$.

6. [**T4**]{#task-u02-kapilarna-igla-unutarnjeg-promjera-spojena-je-na} Kapilarna igla unutarnjeg promjera $d = 0{,}50\ \text{mm}$ spojena je na spremnik vode za koju vrijedi $\sigma = 0{,}072\ \text{N/m}$, $\rho = 998\ \text{kg/m}^3$ i $\theta = 0^\circ$. Izlaz igle nalazi se na visini $H = 42\ \text{mm}$ iznad slobodne površine, a na izlazu se treba održati kapljica promjera $D = 1{,}8\ \text{mm}$. Odredi kapilarni uspon i najmanji dodatni manometarski pretlak u spremniku prema idealizaciji kapilarnog uspona. Za izbor regulatora usporedi taj rezultat s konzervativnim alternativnim stanjem u kojem je meniskus već izašao iz igle pa nema kapilarne depresije tlaka u cijevi, a na izlazu ostaje sferna kapljica. Pokriva li najveći pretlak regulatora od $0{,}50\ \text{kPa}$ statički zahtjev obaju modela? Obrazloži koji je model mjerodavan pri pokretanju, a koji nakon nastanka kapljice.

   :::: {.content-visible .mf1-hint-online when-format="html"}
   ::: {.callout-note collapse="true" data-hint-key="true"}
   ### Naputak
   prvo izračunaj $h_{cap} = 4\sigma /(\rho g d)$, zatim tlakovni skok kapljice $\Delta p = 4\sigma/D$, a preostali pretlak u idealizaciji kapilarnog uspona zatvori iz $p_M = \rho g(H-h_{cap}) + \Delta p$, uz donju granicu $p_M\ge0$. U alternativnom stanju više nema konkavnoga meniskusa koji daje $h_{cap}$, pa regulator mora svladati i visinsku razliku i pozitivni Laplaceov skok: $p_{M,konz}=\rho gH+4\sigma/D$.
   :::
   ::::
   :::: {.content-visible .mf1-answer-online when-format="html"}
   ::: {.callout-tip collapse="true" data-answer-key="true"}
   ### Kontrolni rezultat

   $h_{cap} \approx 58{,}8\ \text{mm}$; u idealizaciji kapilarnog uspona dobiva se zanemariv dodatni pretlak, $p_M \approx 0$. Kada je na izlazu već formirana sferna kapljica, konzervativni model daje $p_{M,konz}\approx0{,}571\ \text{kPa}$. Regulator od $0{,}50\ \text{kPa}$ stoga nije dovoljan za oba stanja: prvi model opisuje uspon s meniskusom u igli, ali izbor regulatora mora pokriti drugi model ili se mora provjeriti prijelaz između njih.
   :::
   ::::
   **Skica:** da - spremnik, kapilarna igla, visina $H$ i izlazna kapljica promjera $D$.
:::::

![Skice uz zadatke za vježbu — viskozni procjepi, kapilare i kapljice (poglavlje 2).](../assets/print/u02_vjezbe_skice.svg){#fig-u02-vjezbe fig-align="center" fig-alt="Skice uz zadatke za vježbu — viskozni procjepi, kapilare i kapljice (poglavlje 2)."}

::: {.mf1-zavrsni-okvir}
<p class="mf1-box-label">Za ponijeti iz poglavlja</p>

**Sažeta provjera prije računa**

- Treba prepoznati govori li zadatak o unutarnjem trenju ili o slobodnoj površini.
- Treba provjeriti koristi li se $\mu$ ili $\nu$ i razlikuju li se njihove uloge.
- Razmak sloja ili promjer kapilare treba pretvoriti u metre.
- Treba provjeriti ulazi li kontaktni kut kroz $\cos\theta$ i je li predznak ispravno određen.
- Treba očekivati fizikalno smislen trend: veća viskoznost daje veću silu, a manji promjer veći uspon.

**Najčešća pogreška**

Najčešća greška u <span class="mf1-ch-ref"><span class="mf1-ch-code">pog. 2</span><span class="mf1-ch-title">Reologija, viskoznost i međupovršinske pojave</span></span> je miješanje dvaju potpuno različitih mehanizama. Newtonov zakon ne rješava kapilarni uspon, a površinska napetost ne opisuje smičanje između slojeva ulja. Prvi korak mora biti odluka koji je stvarni fizikalni uzrok u zadatku.

**Nakon ovoga poglavlja mora biti moguće**

1. razlikovati dinamičku i kinematičku viskoznost.
2. iz gradijenta brzine odrediti smično naprezanje u Newtonskom fluidu.
3. procijeniti kada površinska napetost i kontaktni kut određuju ponašanje slobodne površine i kapilare.

**U tehnici to znači**

U ležaju viskoznost čuva razmak između dviju ploha, u raspršivaču površinska napetost oblikuje kapljicu, a u građevinskom zidu kapilarnost određuje koliko će se vlaga penjati kroz porozni materijal. Isto poglavlje tako spaja mazanje, obradu površina i ponašanje tekućine na malim mjerilima.

**Granica modela**

Newtonov zakon viskoznosti ne vrijedi za svaki fluid, nego za one u kojima je veza između smičnog naprezanja i gradijenta brzine linearna. Jednako tako, kapilarni uspon i kontaktni kut vrlo su osjetljivi na onečišćenje, hrapavost i kemiju stijenke, pa idealna laboratorijska slika ne prelazi uvijek bez korekcija u stvarni sustav.

<span class="mf1-ch-ref"><span class="mf1-ch-code">pog. 2</span><span class="mf1-ch-title">Reologija, viskoznost i međupovršinske pojave</span></span> razdvaja dvije nove fizike: unutarnje trenje u volumenu fluida i zatezanje slobodne površine. Kad je ovdje jasno koji se mehanizam čita, kasnije se sigurnije razlikuju viskoznost, hidrostatika i kapilarnost.
:::

::: {.mf1-numerika}
<p class="mf1-box-label">Numerički most</p>

**Gdje ovo živi u numerici.** Površinska napetost i kontaktni kut ulaze u modele višefaznog strujanja kada su važni kapljice, mjehurići, menisci ili tanki filmovi. Njihovo izostavljanje opravdano je samo nakon procjene mjerodavnih skala i bezdimenzijskih brojeva.

**Što numerički alat radi s tim.** U jednom čestom pristupu, metodi VOF (*Volume of Fluid*), polje volumnoga udjela $\alpha\in[0,1]$ prati raspodjelu faza, a model površinske sile prenosi učinak zakrivljenosti u jednadžbu količine gibanja. To je model diskretizirane međupovršine, ne nova fizikalna bilanca.

**Tipičan scenarij.** Mikrofluidika i procesna industrija često razmatraju fluide kojima viskoznost ovisi o stopi smicanja, pa konstitutivni model treba odabrati i provjeriti prema odgovarajućim podatcima. Pri simulaciji kapljice na stijenci kontaktni je kut zaseban rubni podatak i ne proizlazi iz nenewtonskoga modela viskoznosti.

> *Nije gradivo MF1. Ovo poglavlje otvara vrata u svijet multifaznih simulacija.*
:::
