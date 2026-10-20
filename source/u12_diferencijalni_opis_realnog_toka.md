Realni fluid prianja uz svaku krutu plohu i opire se smicanju. Uz trup broda, lopaticu crpke ili stijenku cijevi brzina se zato mijenja u tankom sloju velikoga gradijenta. Ondje nastaju smično naprezanje i disipacija, a pri porastu tlaka u smjeru toka tok se može odvojiti od plohe. O tim pojavama ovise otpor trenja, zagrijavanje uljnog filma u ležaju i pad tlaka u kanalu. Idealni model iz []{.mf1-chapter-ref target="u08"} ne obuhvaća te pojave, pa ih u ovom poglavlju opisujemo lokalnim bilancama.

Čestica fluida ubrzava zbog promjene polja u vremenu i zbog prelaska u područje druge brzine, što sažima materijalna derivacija $D\vec v/Dt=\partial\vec v/\partial t+(\vec v\cdot\nabla)\vec v$. Za nestlačiv fluid lokalna bilanca mase daje $\nabla\cdot\vec v=0$, a drugi Newtonov zakon za element, uz newtonsku vezu naprezanja i brzine deformacije, daje Navier–Stokesovu jednadžbu $\rho\,D\vec v/Dt=-\nabla p+\mu\nabla^2\vec v+\rho\vec b$. Njezin je najjednostavniji poseban slučaj zakon viskoznosti iz []{.mf1-chapter-ref target="u02"}. Jednadžbe određuju polje tek uz početne i rubne uvjete, prije svega uz uvjet prianjanja $\vec v=\vec 0$ na nepomičnoj stijenci.

Poglavlje redom obrađuje materijalnu derivaciju, lokalne bilance i rubne uvjete, a zatim kanonska rješenja: tok između paralelnih ploča i Hagen–Poiseuilleov tok u cijevi, iz kojega slijedi $\lambda=64/Re$. Uz granični sloj uvode se smično naprezanje na stijenci $\tau_{st}$, Blasiusove procjene i odvajanje. Turbulentni tok opisujemo rastavom brzine na srednju vrijednost i fluktuaciju te Reynoldsovim naprezanjima, a završni odjeljak povezuje te jednadžbe s CFD-om. Reynoldsov broj povezuje poglavlje sa sličnošću iz []{.mf1-chapter-ref target="u11"}, a laminarni rezultat i $\tau_{st}$ polazište su modela gubitaka u []{.mf1-chapter-ref target="u13"}.

Isti model opisuje uljni film kliznog ležaja, granični sloj na trupu modela u vučnom bazenu, rashladne kanale i ulazne uvjete ventilacijskog voda u CFD proračunu. Analitička rješenja vrijede samo uz pretpostavke iz kojih su izvedena: newtonski fluid, konstantne $\rho$ i $\mu$ te stacionaran, potpuno razvijen laminarni tok; Blasiusove procjene traže glatku ravnu plohu bez gradijenta tlaka. Turbulencijski model zatvara nepoznate korelacije, a diskretizacija u CFD-u ne uvodi novu fiziku, pa numerička konvergencija ne zamjenjuje validaciju.

Slika [-@fig-realni-tok-pregled] povezuje tri razine opisa. Lijevo je zamišljeni element fluida dimenzija $dx$ i $dy$; njegovi rubovi nisu krute stijenke, a prikazane su samo $x$-komponente naprezanja: tlak $p$ i $p+dp$ na bočnim plohama te smično naprezanje $\tau_{xy}$ i $\tau_{xy}+d\tau_{xy}$ na donjoj i gornjoj plohi. U sredini je laminarni granični sloj uz ravnu plohu bez gradijenta tlaka ($dp/dx=0$): uz vanjsku brzinu $U_\infty$ njegova debljina $\delta_{99}$ raste s udaljenošću $x$ od prednjeg ruba kao $\delta_{99}\propto\sqrt{x}$, a okomito je mjerilo uvećano. Desno je signal brzine $v(t)=\overline{v}+v'(t)$ koji fluktuira oko srednje vrijednosti $\overline{v}=8{,}0\ \text{m/s}$; to je sintetička shema, a ne mjerenje.

![Diferencijalni opis povezuje lokalnu bilancu količine gibanja, rast graničnog sloja i turbulentne fluktuacije.](../assets/print/u12_fig_uvod_realni_tok.svg){#fig-realni-tok-pregled fig-align="center" fig-alt="Tri panela: element fluida s tlakovima i smičnim naprezanjima na plohama, granični sloj čija debljina raste duž ravne ploče i signal brzine koji fluktuira oko srednje vrijednosti."}

**Procijenjeno vrijeme rada uz priručnik:** 10 sati.

## Diferencijalni opis realnog toka {#sec-realni-tok-motivacija}

Integralne bilance odgovaraju na pitanje kolika je ukupna sila, protok ili snaga sustava. Ne govore izravno gdje nastaje najveće naprezanje, kada se tok odvaja od stijenke ni kako se brzina mijenja unutar graničnog sloja. Za ta pitanja bilancu treba primijeniti na proizvoljno malen element fluida [@schlichting2017; @pope2000].

## Materijalna derivacija {#sec-materijalna-derivacija}

Brzina je polje $\vec v(\vec x,t)$ s komponentama $v_x,v_y,v_z$; u indeksnom zapisu pišemo $v_i$ s $i=1,2,3$ za tri koordinatne osi, a ponovljeni indeks u umnošku znači zbrajanje po svim trima vrijednostima. Brzina čestice koja se giba kroz to polje mijenja se zbog promjene polja u vremenu i zbog prelaska u područje druge brzine. Lančano pravilo daje

$$
\frac{D\vec v}{Dt}=
\underbrace{\frac{\partial\vec v}{\partial t}}_{\text{lokalno ubrzanje}}+
\underbrace{(\vec v\cdot\nabla)\vec v}_{\text{konvektivno ubrzanje}}.
$$ {#eq-materijalna-derivacija}

Stacionarno strujanje ima $\partial\vec v/\partial t=0$, ali čestica može ubrzavati zbog promjene brzine duž svoje putanje, primjerice u suženju ili zavoju. Nejednolik profil sam po sebi ne znači ubrzanje: u potpuno razvijenom ravnom toku $\vec v=(v_x(y),0,0)$ vrijedi $(\vec v\cdot\nabla)\vec v=v_x\,\partial\vec v/\partial x=0$, iako je $dv_x/dy$ različit od nule. U stacionarnom polju putanje čestica poklapaju se sa strujnicama.

::: {#ex-konvektivno-ubrzanje .mf1-we}
<p class="mf1-box-label">Ubrzanje u stacionarnom toku kroz suženje <span class="mf1-level">T1</span></p>

**Tekst zadatka**

U jednodimenzijskom stacionarnom modelu brzina raste linearno, $v(x)=2+3x\ \text{m/s}$ za $x$ u metrima. Promatra se položaj $x=0{,}50\ \text{m}$.

**Traži se**

Odredi materijalno ubrzanje čestice u zadanom položaju.

**Rješenje**

U tom položaju vrijedi $v=3{,}5\ \text{m/s}$ i

$$
a_x=v\frac{dv}{dx}=3{,}5\cdot3=10{,}5\ \text{m/s}^2.
$$ {#eq-realni-tok-rijeseni-primjer-ubrzanje-kroz-mirno-suzenje-t1-01}

**Provjera i tumačenje**

Lokalni je član jednak nuli, ali konvektivni nije. Jedinice $(\text{m/s})(1/\text{s})$ daju $\text{m/s}^2$.
:::

## Lokalna bilanca mase i količine gibanja {#sec-navier-stokes}

Za kontinuum bez izvora mase lokalna bilanca mase jest

$$
\frac{\partial\rho}{\partial t}+\nabla\cdot(\rho\vec v)=0.
$$ {#eq-lokalna-kontinuitet}

Za nestlačiv fluid konstantne gustoće ona se svodi na $\nabla\cdot\vec v=0$.

Drugi Newtonov zakon za materijalni element (Cauchyjeva jednadžba gibanja) glasi

$$
\rho\frac{D\vec v}{Dt}=\nabla\cdot\boldsymbol\sigma+\rho\vec b,
$$ {#eq-realni-tok-lokalna-bilanca-mase-i-kolicine-gibanja-sec-01}

gdje je $\boldsymbol\sigma=-p\mathbf I+\boldsymbol\tau$ ukupni tenzor naprezanja, a $\vec b$ sila po jedinici mase. Za newtonski fluid konstantnih $\rho$ i $\mu$ s $\nabla\cdot\vec v=0$ vrijedi $\nabla\cdot\boldsymbol\tau=\mu\nabla^2\vec v$ (izvod slijedi), pa se dobiva

$$
\boxed{
\rho\left(\frac{\partial\vec v}{\partial t}+(\vec v\cdot\nabla)\vec v\right)
=-\nabla p+\mu\nabla^2\vec v+\rho\vec b
}.
$$ {#eq-navier-stokes-nestlacivi}

Članovi redom opisuju lokalnu i konvektivnu promjenu količine gibanja, tlačnu silu, viskoznu difuziju količine gibanja i volumensku silu. Konvektivni član nije sam po sebi „izvor turbulencije”; nelinearnost omogućuje međudjelovanje skala, dok nastanak i održavanje turbulencije ovise o nestabilnostima, smičnom radu, geometriji i disipaciji.

::: {.mf1-izvod}
<p class="mf1-box-label">Matematički izvod — Od Cauchyjeve jednadžbe do Navier–Stokesove</p>

**Pitanje.** Kako iz opće bilance, jednadžbe [-@eq-realni-tok-lokalna-bilanca-mase-i-kolicine-gibanja-sec-01], koja vrijedi za svaki kontinuum, nastaje jednadžba s članom $\mu\nabla^2\vec v$?

**Bilanca i konstitutivna relacija.** Fizika fluida ulazi u bilancu tek preko veze naprezanja i deformacije. Za newtonski fluid viskozno naprezanje linearno ovisi o tenzoru brzine deformacije $\mathbf D$:

$$
\tau_{ij}=2\mu D_{ij}=\mu\left(\frac{\partial v_i}{\partial x_j}+\frac{\partial v_j}{\partial x_i}\right),
\qquad
D_{ij}=\frac12\left(\frac{\partial v_i}{\partial x_j}+\frac{\partial v_j}{\partial x_i}\right),
$$ {#eq-newtonska-konstitutivna-relacija}

uz $\nabla\cdot\vec v=0$. Za jednostavno smicanje $\vec v=(v_x(y),0,0)$ ostaje samo $\tau_{xy}=\mu\,dv_x/dy$, što je zakon viskoznosti iz []{.mf1-chapter-ref target="u02"}.

**Koraci.** Divergencija viskoznog naprezanja po komponentama glasi

$$
\frac{\partial\tau_{ij}}{\partial x_j}
=\mu\frac{\partial^2 v_i}{\partial x_j\partial x_j}
+\mu\frac{\partial}{\partial x_i}\underbrace{\frac{\partial v_j}{\partial x_j}}_{\nabla\cdot\vec v\,=\,0}
=\mu\nabla^2 v_i,
$$ {#eq-divergencija-viskoznog-naprezanja}

pri čemu je zamjena redoslijeda derivacija dopuštena za glatko polje, a $\mu$ je konstantan. Tlačni dio daje $\nabla\cdot(-p\mathbf I)=-\nabla p$. Uvrštavanje $\nabla\cdot\boldsymbol\sigma=-\nabla p+\mu\nabla^2\vec v$ u Cauchyjevu jednadžbu daje jednadžbu [-@eq-navier-stokes-nestlacivi].

**Rezultat i provjera.** Viskozni član ima dimenziju $\mu v/L^2=\mathsf{M}\,\mathsf{L}^{-2}\,\mathsf{T}^{-2}$, jednaku dimenziji $\nabla p$ i $\rho\,D\vec v/Dt$. Svaka pretpostavka ima vidljivu posljedicu: bez $\nabla\cdot\vec v=0$ ostaje dodatni član $\mu\nabla(\nabla\cdot\vec v)$ i doprinos volumenske viskoznosti, bez konstantnog $\mu$ ostaje član s $\nabla\mu$, a za nenewtonski fluid mijenja se jednadžba [-@eq-newtonska-konstitutivna-relacija].
:::

::: {.mf1-granica-modela}
<p class="mf1-box-label">Granica modela — Pretpostavke prikazanog oblika</p>

Jednadžba [-@eq-navier-stokes-nestlacivi] pretpostavlja newtonski fluid, konstantnu viskoznost i gustoću te odsutnost dodatnih konstitutivnih učinaka. Nenewtonski fluid ne zahtijeva novi zakon količine gibanja, nego drukčiju vezu $\boldsymbol\tau(\mathbf D)$ između naprezanja i tenzora brzine deformacije $\mathbf D$ umjesto jednadžbe [-@eq-newtonska-konstitutivna-relacija] (oznaku $\mathbf D$ ne treba miješati s promjerom $D$).
:::


::: {#cfd-hladna-ploca-toplina .mf1-cfd title="Računalna dinamika fluida"}

**Od protoka u hladnoj ploči do temperature baterije.** Nastavljamo model razdjelnika: Navier–Stokesove jednadžbe povezuju tlak, prijenos količine gibanja i viskozna naprezanja u kanalima. U nestlačivom računu tlak se usklađuje s brzinom tako da bude zadovoljen kontinuitet. Takav model daje raspodjelu protoka i potreban pogon, pa možemo prepoznati slabije opskrbljene kanale.

Za pitanje o najvišoj temperaturi baterije dodajemo energijsku jednadžbu fluida i provođenje topline kroz krutu ploču. Trebaju nam ulazna temperatura, toplinska svojstva i zadano zagrijavanje baterije; na dodiru krutine i fluida usklađujemo prijenos topline. Spregnuti toplinski proračun tada omogućuje usporedbu temperature i potrebnog pada tlaka [@greenshieldsweller2022].
:::

## Rubni uvjeti i fizikalno zatvaranje problema {#sec-rubni-uvjeti}

Jednadžbe bez rubnih i početnih uvjeta ne određuju jedinstveno polje. Na nepomičnoj nepropusnoj stijenci za viskozni tok vrijedi

$$
\vec v=\vec 0,
$$ {#eq-realni-tok-rubni-uvjeti-i-fizikalno-zatvaranje-problema-sec-01}

odnosno nema prolaza kroz stijenku i nema klizanja uz nju. Na slobodnoj površini treba zadati kinematički uvjet gibanja granice i ravnotežu normalnih i tangencijalnih naprezanja. Na ulazu se zadaje konzistentan profil ili protok, a na izlazu tlak ili uvjet dovoljno udaljen od poremećaja. Pogrešan rubni uvjet može dati uredne reziduale, ali pogrešno fizikalno rješenje.

::: {.mf1-cfd title="Računalna dinamika fluida"}

**Ulaz i izlaz hladne ploče moraju opisivati ostatak kruga.** Za poznati protok zadajemo ulazni profil i odgovarajući izlazni tlak; na mirnim stijenkama vrijedi prianjanje. U odlomku *Računalna dinamika fluida* o podjeli protoka razdjelnika u []{.mf1-chapter-ref target="u07"} pojedinačni protoci proizlaze iz računa; kad bismo ih nametnuli, uklonili bismo upravo pitanje podjele.

Za proračun cijeloga rashladnog kruga protok određuje i crpka. U zatvorenoj nestlačivoj domeni treba odabrati referencu tlaka, a ostale uvjete uskladiti s formulacijom rješavača. Primjerice, u mirovanju uz gravitaciju gradijent fizičkog tlaka $p$ okomito na stijenku uravnotežuje težinu, $\partial p/\partial n=\rho g_n$; uvjet „nulti gradijent tlaka na stijenci” vrijedi samo za tlak iz kojega je hidrostatički dio izdvojen (u OpenFOAM-u $p_{rgh}=p-\rho\,\vec g\cdot\vec x$), pa rubni uvjet treba zadati za onu varijablu koju rješavač stvarno računa [@greenshieldsweller2022].
:::

## Kanonsko rješenje: tok između paralelnih ploča {#sec-couette-poiseuille}

Promatra se stacionarni, potpuno razvijeni, laminarni tok newtonskog fluida između ploča na $y=0$ i $y=H$. Brzina fluida je $\vec v=(v(y),0,0)$, gornja ploča giba se brzinom $u$ (oznaka $u$ ovdje je brzina krute granice, a $v$ brzina fluida), gravitacija u smjeru toka zanemariva, a gradijent tlaka konstantan. Navier–Stokesova jednadžba svodi se na

$$
0=-\frac{dp}{dx}+\mu\frac{d^2v}{dy^2}.
$$ {#eq-realni-tok-kanonsko-rjesenje-tok-izme-u-paralelnih-ploca-01}

Dvostrukom integracijom uz rubne uvjete $v(0)=0$, $v(H)=u$ dobiva se Couette–Poiseuilleov profil

$$
v(y)=\frac{u}{H}y+\frac{1}{2\mu}\frac{dp}{dx}(y^2-Hy).
$$ {#eq-couette-poiseuille}

Prvi član opisuje doprinos gibanja gornje ploče, a drugi doprinos gradijenta tlaka. Suprotstave li se ta dva pogona, u dijelu procjepa može nastati povratni tok.

::: {#ex-uljni-film .mf1-we}
<p class="mf1-box-label">Uljni film s dva pogonska mehanizma <span class="mf1-level">T2</span></p>

**Tekst zadatka**

Ulje viskoznosti $\mu=0{,}10\ \text{Pa s}$ stacionarno struji između ploča razmaknutih za $H=1{,}0\ \text{mm}$. Donja ploča miruje, a gornja se giba brzinom $u=2{,}0\ \text{m/s}$ u smjeru $x$. Gradijent tlaka iznosi $dp/dx=-100\ \text{kPa/m}$.

**Traži se**

Odredi brzinu u sredini procjepa i razdvoji doprinose gibanja ploče i gradijenta tlaka.

**Rješenje**

$$
v(H/2)=\frac{u}{2}+\frac{1}{2\mu}\frac{dp}{dx}\left(-\frac{H^2}{4}\right)
=1{,}0+0{,}125=1{,}125\ \text{m/s}.
$$ {#eq-realni-tok-rijeseni-primjer-uljni-film-s-dva-pogonska-01}

**Provjera i tumačenje**

Negativan $dp/dx$ znači pad tlaka u pozitivnom $x$-smjeru i zato povećava brzinu. Bez određivanja prostorne raspodjele tlaka ovaj model ne daje procjenu nosivosti ležaja.
:::

## Hagen–Poiseuilleov tok i linearni gubitak {#sec-hagen-poiseuille}

Za kružnu cijev polumjera $R$, uz $\vec v=(v(r),0,0)$ duž osi $x$, Navier–Stokesova jednadžba u cilindričnim koordinatama svodi se na

$$
\frac{\mu}{r}\frac{d}{dr}\left(r\frac{dv}{dr}\right)=\frac{dp}{dx}=\text{konst.}
$$ {#eq-poiseuille-ode}

Dvostruka integracija daje $v(r)=\frac{1}{4\mu}\frac{dp}{dx}r^2+C_1\ln r+C_2$. Konačna brzina u osi ($r=0$) zahtijeva $C_1=0$, a prianjanje $v(R)=0$ određuje $C_2$, pa je

$$
v(r)=-\frac{1}{4\mu}\frac{dp}{dx}(R^2-r^2),
$$ {#eq-realni-tok-hagen-poiseuilleov-tok-i-linearni-gubitak-sec-01}

$$
Q=-\frac{\pi R^4}{8\mu}\frac{dp}{dx},
\qquad
\Delta p=\frac{128\mu L}{\pi D^4}Q.
$$ {#eq-hagen-poiseuille}

To je važan granični test cijelog modela gubitaka: pri laminarnom potpuno razvijenom toku pad tlaka raste **linearno** s $Q$. U Darcyjevu zapisu isti rezultat daje $\lambda=64/Re$; zato tvrdnja da su svi gubitci nužno proporcionalni $v^2$ nije točna.

::: {.mf1-izvod}
<p class="mf1-box-label">Matematički izvod — Od profila brzine do $\lambda=64/Re$</p>

Protok slijedi integracijom paraboličnog profila iz jednadžbe [-@eq-realni-tok-hagen-poiseuilleov-tok-i-linearni-gubitak-sec-01] po presjeku:

$$
Q=\int_0^R v(r)\,2\pi r\,dr
=-\frac{\pi R^4}{8\mu}\frac{dp}{dx}.
$$ {#eq-realni-tok-hagen-poiseuilleov-tok-i-linearni-gubitak-sec-02}

Uz srednju presječnu brzinu $v=Q/(\pi R^2)$ i $D=2R$ slijedi $\Delta p=-L\,dp/dx=32\mu Lv/D^2$ te $v_{max}=2v$. Izjednačavanjem s Darcyjevim zapisom

$$
\Delta p=\lambda\frac{L}{D}\frac{\rho v^2}{2}
$$ {#eq-realni-tok-izvod-od-profila-brzine-do-lambda-64-re-01}

dobiva se

$$
\lambda=\frac{64\mu}{\rho vD}=\frac{64}{Re}.
$$ {#eq-realni-tok-izvod-od-profila-brzine-do-lambda-64-re-02}

Faktor $64$ zato nije empirijska konstanta, nego posljedica stacionarnog, potpuno razvijenog laminarnog toka newtonskoga fluida u kružnoj cijevi. Izvan tih pretpostavki ovaj se rezultat ne prenosi bez provjere.
:::

::: {.mf1-cfd title="Računalna dinamika fluida"}

**Jednostavan kanal prije složene hladne ploče.** Prije računa zavoja i razdjelnika provjerimo isti laminarni model na ravnom kanalu s poznatim rješenjem. Ručni račun u primjeru [-@ex-laminarni-mikrokanal] pretpostavlja potpuno razvijen tok, pa usporedba njegova pada tlaka mora isključiti dodatni pad u ulaznom području. Za idealizirani prorez koristimo rješenje između ploča.

**Zastani i promisli.** Rezidual je malen, ali se pad tlaka mijenja pri profinjenju mreže. Koja je pogreška još nerazjašnjena?

Mali rezidual uz promjenu pada tlaka na finijoj mreži još ne potvrđuje točnost. Usporedi profil, protok i smično naprezanje s analitičkim rješenjem; točna brzina u osi ne jamči točno trenje. Pokus na stvarnoj hladnoj ploči zasebno provjerava fizikalni model.
:::

::: {#ex-laminarni-mikrokanal .mf1-we}
<p class="mf1-box-label">Pad tlaka u dijagnostičkom mikrokanalu <span class="mf1-level">T2</span></p>

**Tekst zadatka**

Voda gustoće $\rho=998\ \text{kg/m}^3$ i dinamičke viskoznosti $\mu=1{,}0\ \text{mPa s}$ teče kroz kružnu kapilaru promjera $D=0{,}50\ \text{mm}$ i duljine $L=0{,}20\ \text{m}$, protokom $Q=0{,}30\ \text{mL/min}=5{,}0\cdot10^{-9}\ \text{m}^3/\text{s}$. Pretpostavi potpuno razvijen laminarni tok.

**Traži se**

Odredi pad tlaka za potpuno razvijen laminarni tok i provjeri je li laminarna pretpostavka prihvatljiva.

**Rješenje**

$$
\Delta p=\frac{128(10^{-3})(0{,}20)}{\pi(5\cdot10^{-4})^4}(5\cdot10^{-9})=652\ \text{Pa}.
$$ {#eq-realni-tok-rijeseni-primjer-pad-tlaka-u-dijagnostickom-mikr-01}

**Provjera i tumačenje**

Srednja brzina je $0{,}0255\ \text{m/s}$ i $Re\approx12{,}7$, pa je pretpostavka laminarnog toka u skladu s rezultatom. Udvostručenje protoka udvostručuje $\Delta p$, a ne učetverostručuje ga.
:::

## Granični sloj, smično naprezanje i odvajanje {#sec-granicni-sloj}

Kada gotovo jednoliko strujanje naiđe na stijenku, uvjet prianjanja stvara tanko područje velikoga gradijenta brzine. Izvan njega viskozni učinak može biti malen, a unutar njega upravo on određuje smično naprezanje

$$
\tau_{st}=\mu\left.\frac{\partial v_x}{\partial y}\right|_{st}.
$$ {#eq-realni-tok-granicni-sloj-smicno-naprezanje-i-odvajanje-sec-01}

Za laminarni granični sloj uz ravnu ploču bez gradijenta tlaka Blasiusovo rješenje daje procjene

$$
\delta_{99}\approx\frac{5x}{\sqrt{Re_x}},
\qquad
C_{f,x}\approx\frac{0{,}664}{\sqrt{Re_x}},
\qquad Re_x=\frac{U_\infty x}{\nu},
$$ {#eq-blasius-procjene}

gdje je $U_\infty$ brzina neporemećenog vanjskog toka, a $x$ udaljenost od prednjeg ruba. To nisu univerzalne formule: vrijede za glatku ravnu plohu, približno nulti gradijent tlaka i laminarni sloj.

Nepovoljan gradijent tlaka, $dp/dx>0$ u smjeru toka, usporava fluid uz stijenku. U stacionarnom dvodimenzijskom graničnom sloju nulto smično naprezanje može označiti početak odvajanja, uz pojavu lokalnog povratnog toka. Sama promjena znaka u drugoj geometriji, primjerice u potpuno razvijenom toku između ploča u Z4, ne dokazuje odvajanje strujnica od plohe. Odvajanje mijenja tlak i otpor mnogo više nego sama lokalna viskozna sila; zato geometrijski blaga promjena difuzora može odlučiti radi li uređaj učinkovito.

::: {.mf1-fizikalno-znacenje}
<p class="mf1-box-label">Fizikalno značenje — Rast graničnog sloja i odvajanje</p>

Granični sloj je područje u kojem se utjecaj prianjanja širi viskoznom difuzijom (vremensko mjerilo $\delta^2/\nu$), dok ga struja istodobno nosi niz plohu (vremensko mjerilo $x/U_\infty$). Izjednačavanje tih dvaju vremena daje $\delta\sim\sqrt{\nu x/U_\infty}=x/\sqrt{Re_x}$, što je struktura Blasiusova rezultata. Nepovoljan gradijent tlaka jednako djeluje na cijeli presjek sloja, ali fluid uz stijenku ima najmanju kinetičku energiju, pa prvi zastaje: odvajanje je ishod nadmetanja tlaka koji koči i količine gibanja koju sloj nosi. Turbulentni sloj miješanjem dovodi količinu gibanja prema stijenci, pa se odvaja kasnije. Na modelu broda sloj se namjerno prevodi u turbulentni zato da bi $C_{F,m}$ odgovarao turbulentnoj korelacijskoj liniji (primjer [-@ex-granicni-sloj-trupa-modela]).
:::

::: {.mf1-cfd title="Računalna dinamika fluida"}

**Zašto se tok odvaja u kratkom difuzoru?** Vraćamo se dvjema izvedbama iza Venturijeva grla iz []{.mf1-chapter-ref target="u08"}. Pri porastu tlaka u smjeru toka sporiji fluid uz stijenku može zastati i poteći unatrag. CFD pokazuje mjesto odvajanja i područje povratnog toka, a integracija mehaničke energije pokazuje kako se to odražava na gubitak.

Blasiusovo rješenje služi za provjeru laminarnog sloja bez gradijenta tlaka, ali ne predviđa odvajanje u difuzoru. Ondje mrežu profinjujemo uz stijenku i u području povratnog toka te pratimo mjesto odvajanja i gubitak. Usporedbu cijeloga uređaja donosi @sec-cfd-venturi.
:::

<span id="ex-granicni-sloj"></span>

::: {#ex-granicni-sloj-trupa-modela .mf1-we}
<p class="mf1-box-label">Granični sloj na trupu modela broda <span class="mf1-level">T2</span></p>

**Tekst zadatka**

Model broda iz primjera [-@ex-u14-froudeova-slicnost-model-broda-u-vucnom-bazenu] ima duljinu $L_m=6{,}0\ \text{m}$ i vuče se brzinom $v_m=1{,}8\ \text{m/s}$ u slatkoj vodi bazena kinematičke viskoznosti $\nu=1{,}0\cdot10^{-6}\ \text{m}^2/\text{s}$. Za procjenu se trup zamjenjuje glatkom ravnom pločom iste duljine uz jednolik vanjski tok brzine $U_\infty=v_m$. Reynoldsov broj broda iznosi $Re_s=1{,}35\cdot10^{9}$.

**Traži se**

1. Odredi $Re_x$ i laminarnu Blasiusovu debljinu na udaljenosti $x_1=0{,}05L_m$ od pramca, gdje se obično ugrađuje stimulator turbulencije; objasni zašto se on ugrađuje.
2. Odredi $Re_L$ i procijeni debljinu turbulentnog sloja na krmi prema $\delta\approx0{,}37x/Re_x^{1/5}$ (aproksimacija potencijskog profila $1/7$).
3. Odredi $C_F$ prema liniji ITTC 1957 (@eq-ittc-1957) za model i brod i protumači razliku.

**Rješenje**

### 1. Pramčano područje {.unnumbered .unlisted .mf1-step}

$$
\begin{aligned}
x_1&=0{,}30\ \text{m},\qquad Re_{x_1}=\frac{1{,}8\cdot0{,}30}{1{,}0\cdot10^{-6}}=5{,}4\cdot10^{5}, \\
\delta_{B}&\approx\frac{5\cdot0{,}30}{\sqrt{5{,}4\cdot10^{5}}}=2{,}04\ \text{mm}.
\end{aligned}
$$ {#eq-granicni-sloj-trupa-modela-01}

### 2. Krma {.unnumbered .unlisted .mf1-step}

$$
Re_L=\frac{1{,}8\cdot6{,}0}{1{,}0\cdot10^{-6}}=1{,}08\cdot10^{7},\qquad
\delta\approx\frac{0{,}37\cdot6{,}0}{(1{,}08\cdot10^{7})^{1/5}}=\frac{2{,}22}{25{,}5}\approx0{,}087\ \text{m}.
$$ {#eq-granicni-sloj-trupa-modela-02}

### 3. Koeficijent trenja {.unnumbered .unlisted .mf1-step}

$$
\begin{aligned}
C_{F,m}&=\frac{0{,}075}{(\log_{10}1{,}08\cdot10^{7}-2)^2}\approx2{,}96\cdot10^{-3}, \\
C_{F,s}&=\frac{0{,}075}{(\log_{10}1{,}35\cdot10^{9}-2)^2}\approx1{,}48\cdot10^{-3}.
\end{aligned}
$$ {#eq-granicni-sloj-trupa-modela-03}

**Provjera i tumačenje**

1. $Re_{x_1}=5{,}4\cdot10^{5}$ leži u području u kojem laminarni sloj na glatkoj ploči još može opstati (prirodni prijelaz približno između $3\cdot10^{5}$ i $3\cdot10^{6}$), dok je na brodu $Re_x$ na istom mjestu 125 puta veći. Zato se prijelaz na modelu izaziva žicom, trakom s pijeskom ili klinovima; bez toga bi $C_{F,m}$ bio manji od pretpostavljenog, a korekcija prema jednadžbi [-@eq-froudeova-hipoteza] bila bi pogrešna.
2. $\delta/L_m\approx0{,}015\ll1$ potvrđuje aproksimaciju tankog sloja; $C_{F,m}/C_{F,s}\approx2{,}0$ pokazuje zašto se viskozni otpor ne skalira s $\lambda_L^3$. Model ravne ploče zanemaruje zakrivljenost trupa, gradijent tlaka i hrapavost.
:::

## Turbulentni tok: srednja vrijednost nije cijelo polje {#sec-turbulencija}

U turbulentnom toku trenutna se brzina rastavlja na vremenski srednju vrijednost i fluktuaciju,

$$
v_i(\vec x,t)=\overline{v_i}(\vec x)+v_i'(\vec x,t),
\qquad \overline{v_i'}=0.
$$ {#eq-realni-tok-turbulentni-tok-srednja-vrijednost-nije-cijelo-p-01}

Intenzitet turbulencije za jednu (uzdužnu) komponentu može se izraziti kao

$$
I_t=\frac{v'_{rms}}{\overline{v}},
\qquad
v'_{rms}=\sqrt{\overline{v'^2}}.
$$ {#eq-realni-tok-turbulentni-tok-srednja-vrijednost-nije-cijelo-p-02}

Osrednjavanjem Navier–Stokesove jednadžbe linearni članovi zadržavaju isti oblik, sada sa srednjim poljem, ali nelinearni konvektivni član daje dodatni doprinos:

$$
\overline{\frac{\partial(v_iv_j)}{\partial x_j}}
=\frac{\partial(\overline{v_i}\,\overline{v_j})}{\partial x_j}
+\frac{\partial\overline{v_i'v_j'}}{\partial x_j},
$$ {#eq-reynoldsovo-osrednjavanje}

jer je $\overline{\overline{v_i}\,v_j'}=0$, dok $\overline{v_i'v_j'}$ općenito nije nula. Taj se član prebacuje na stranu naprezanja kao Reynoldsovo naprezanje $-\rho\overline{v_i'v_j'}$ (RANS, engl. *Reynolds-averaged Navier–Stokes*). Reynoldsova naprezanja nisu nova molekularna naprezanja, nego tok srednje količine gibanja koji nose fluktuacije. Turbulencijski model zatvara te nepoznate korelacije; on nije numerička zamjena za Darcyjev koeficijent trenja. Najčešći su dvojednadžbeni modeli: $k$–$\varepsilon$ rješava prijenosne jednadžbe za turbulentnu kinetičku energiju $k=\tfrac12\overline{v_i'v_i'}$ i njezinu disipaciju $\varepsilon$, a $k$–$\omega$ SST (engl. *shear stress transport*) za $k$ i specifičnu disipaciju $\omega$, uz prijelaz s $k$–$\omega$ blizu stijenke na $k$–$\varepsilon$ daleko od nje. Oba modela povezuju Reynoldsova naprezanja s gradijentom srednje brzine preko turbulentne viskoznosti $\mu_t$ (Boussinesqova pretpostavka). Kratica SSTm u primjeru [-@ex-stepenica-mjerenje-cfd] označuje inačicu $k$–$\omega$ SST modela u obliku koji navodi NASA-in Turbulence Modeling Resource (TMR).

CFD je način numeričkog rješavanja i laminarnog i turbulentnog modela. RANS rješava osrednjene jednadžbe uz model korelacija; LES (engl. *large eddy simulation*) razrješava velike vrtloge i modelira učinak manjih; DNS (engl. *direct numerical simulation*) razrješava sve dinamički relevantne turbulentne skale bez turbulencijskog modela. Izbor ovisi o tome treba li nam srednji ili vremenski promjenjiv odziv i o raspoloživoj razlučivosti, a ne samo o $Re$ iz prethodnog poglavlja [@pope2000].

::: {.mf1-cfd title="Računalna dinamika fluida"}

**Srednji rad razdjelnika ili njegove pulsacije?** Pri većim brzinama tok u razdjelniku može biti turbulentan. Ako nas zanimaju srednja podjela protoka i pad tlaka, RANS računa osrednjeno polje, a dodatnim modelom opisuje prijenos količine gibanja zbog fluktuacija. Na ulazu zato trebamo i podatke o turbulenciji primjerene odabranom modelu; sam intenzitet jedne komponente nije dovoljan za sve veličine.

Ako je cilj promjenjivo opterećenje ili detaljno miješanje, treba odabrati vremenski i turbulencijski opis koji može prikazati tražene pojave. Nestacionarni RANS može pratiti neke promjene srednjeg toka, dok LES razrješava dio vrtložnoga gibanja uz veće zahtjeve za mrežu i vrijeme računanja. Samo profinjenje RANS mreže ne pretvara račun u takav opis. Izbor određuje izlaz koji trebamo, uz usporedbu s mjerenjem.
:::

Uz stijenku je korisna bezdimenzijska udaljenost

$$
y^+=\frac{u_\tau y}{\nu},\qquad u_\tau=\sqrt{\frac{|\tau_{st}|}{\rho}}.
$$ {#eq-realni-tok-turbulentni-tok-srednja-vrijednost-nije-cijelo-p-03}

Ovdje je $y$ udaljenost od stijenke, a $u_\tau$ nenegativna brzina trenja, definirana iznosom smičnog naprezanja. Predznak $\tau_{st}$ zasebno opisuje smjer smicanja. Položaj prve ćelije i model strujanja uz stijenku moraju biti usklađeni: izravno razrješavanje viskoznog podsloja i zidna funkcija ne traže isti $y^+$.

::: {.mf1-cfd title="Računalna dinamika fluida"}

**Mreža uz stijenku iste hladne ploče.** U turbulentnoj inačici računa odabrani model stijenke određuje gdje trebaju biti prve računske točke. Ako izravno razrješavamo viskozni podsloj, obično ciljamo $y^+\approx1$ ili manje; zidne funkcije modeliraju dio profila i imaju vlastito područje primjene. Procjena brzine trenja daje početnu visinu ćelije, a nakon računa provjeravamo stvarni $y^+$.

Provjera obuhvaća sve kanale i zavoje jer naprezanje nije jednako posvuda. Uz $y^+$ pratimo promjenu pada tlaka i protoka po granama pri profinjenju; u toplinskom modelu i najvišu temperaturu. Prihvatljiv $y^+$ tako provjerava jednu pretpostavku obrade stijenke, a konvergencija ciljanih veličina pokazuje je li mreža dovoljna za usporedbu izvedbi.
:::

::: {#ex-intenzitet-turbulencije .mf1-we}
<p class="mf1-box-label">Od podatka anemometra do ulaznog uvjeta RANS-a <span class="mf1-level">T3</span></p>

**Tekst zadatka**

Senzor u ventilacijskom vodu promjera $D=0{,}30\ \text{m}$ mjeri srednju brzinu $\overline{v}=8{,}0\ \text{m/s}$ i standardnu devijaciju uzdužne fluktuacije $v'_{rms}=0{,}48\ \text{m/s}$. Za RANS proračun nizvodnog difuzora s modelom $k$–$\omega$ SST na ulazu treba zadati $k$ i $\omega$; model koristi $C_\mu=0{,}09$.

**Traži se**

1. Odredi uzdužni intenzitet turbulencije.
2. Uz pretpostavku izotropne turbulencije procijeni $k$.
3. Utvrdi što još nedostaje za određivanje $\omega$; pokaži procjenu uz uobičajenu duljinsku skalu $\ell\approx0{,}07D$ i obrazloži zašto je ona pretpostavka, a ne mjerenje.

**Rješenje**

$$
I_t=\frac{0{,}48}{8{,}0}=0{,}060=6{,}0\ \%,
\qquad
k=\tfrac32\,(I_t\,\overline{v})^2=\tfrac32\cdot0{,}48^2\approx0{,}346\ \text{m}^2/\text{s}^2.
$$ {#eq-realni-tok-rijeseni-primjer-podatak-anemometra-a-ne-etiketa-01}

Faktor $\tfrac32$ pretpostavlja da su sve tri komponente fluktuacije jednake uzdužnoj. Specifična disipacija traži duljinsku skalu koju senzor ne daje; uz $\ell=0{,}07\cdot0{,}30=0{,}021\ \text{m}$:

$$
\omega=\frac{\sqrt{k}}{C_\mu^{1/4}\,\ell}=\frac{0{,}588}{0{,}548\cdot0{,}021}\approx51\ \text{s}^{-1},
\qquad
\varepsilon=C_\mu k\omega\approx1{,}59\ \text{m}^2/\text{s}^3.
$$ {#eq-anemometar-ulazni-uvjet-rans}

**Provjera i tumačenje**

1. Kontrola: $\varepsilon=C_\mu^{3/4}k^{3/2}/\ell=0{,}164\cdot0{,}203/0{,}021\approx1{,}59\ \text{m}^2/\text{s}^3$, jednako kao $C_\mu k\omega$. Uz stijenku $v_x'\ne v_y'$, pa je izotropni $k$ gruba procjena.
2. Odluka: $k$ se određuje iz mjerenja uz pretpostavku izotropije, a $\omega$ iz dogovorne skale $\ell\approx0{,}07D$ uz ispitivanje osjetljivosti jer prepolovljeni $\ell$ udvostručuje $\omega$; „izmjereni” $\omega$ zahtijevao bi spektar ili integralnu skalu signala.
:::

::: {#ex-stepenica-mjerenje-cfd .mf1-we}
<p class="mf1-box-label">Ponovno priljubljivanje toka: mjerenje i CFD <span class="mf1-level">T3</span></p>

**Tekst zadatka**

U pokusu Drivera i Seegmillera dno kanala spušta se za visinu stepenice $H_s$, uz vodoravan gornji zid. Turbulentni zrak ($Re_{H_s}\approx36\,000$, prema visini stepenice) odvaja se na rubu i ponovno priljubljuje nizvodno. Koristi bezdimenzijsku udaljenost $X=x/H_s$ od ruba i $C_f=\tau_{st}/(\rho U_{ref}^2/2)$, gdje je $U_{ref}$ uzvodna brzina u sredini kanala pri $X\approx-4$. Predznak $C_f$ prati srednje smicanje na stijenci.

Tablica daje mjerenja i objavljeni kvazistacionarni CFD rezultat CFL3D-a s modelom turbulencije SSTm. Vrijednosti CFD-a preuzete su iz [izvornih datoteka](../data/cfd/backstep_experiment/README.md) i zaokružene samo na pet do sedam značajnih znamenaka. Eksperimentalni položaj ponovnog priljubljivanja iznosi $X_r=6{,}26\pm0{,}10$ [@driver-seegmiller1985; @tmr-backstep].

| Izvor | $X_a$ | $10^3C_{f,a}$ | $X_b$ | $10^3C_{f,b}$ |
|---|---:|---:|---:|---:|
| Mjerenje | 5,882 | −0,220 | 7,090 | 0,450 |
| CFL3D / SSTm | 6,541667 | −0,0012520 | 6,562500 | 0,013198 |

**Traži se**

1. Linearnom interpolacijom odredi nultočku $C_f$ za oba niza.
2. Usporedi CFD nultočku s objavljenim eksperimentalnim položajem i protumači što usporedba dokazuje.

**Rješenje**

Za promjenu iz negativnog u pozitivno smicanje između zadanih točaka vrijedi

$$
X_r=X_a-\frac{C_{f,a}}{C_{f,b}-C_{f,a}}(X_b-X_a).
$$ {#eq-stepenica-interpolacija-priljubljivanja}

Faktor $10^3$ krati se u omjeru. Mjerni podatci daju $X_{r,m}\approx6{,}279$ (linearna interpolacija preko razmaka $1{,}2H_s$ samo je gruba provjera jer $C_f$ oko priljubljivanja nije linearan), a podatci CFD-a $X_{r,CFD}\approx6{,}543$. U odnosu na objavljenu mjernu vrijednost $6{,}26$ CFD predviđa položaj približno $0{,}283H_s$ nizvodnije, odnosno oko $4{,}5\,\%$ veću duljinu.

**Provjera i tumačenje**

Obje nultočke leže između pripadnih zadanih položaja. Mjerna interpolacija nalazi se u objavljenom rasponu $6{,}16$–$6{,}36$, a CFD rezultat izvan njega. Time je utvrđeno odstupanje ove veličine, ali mogući uzroci (mreža, ulazni sloj, model turbulencije) nisu razdvojeni jer izvor ne daje potpunu studiju mrežne konvergencije. Oznaku $\pm0{,}10$ ne pretvaramo u standardnu nesigurnost ni 95-postotni interval. Za difuzor rashladnog ili brodskog ventilacijskog voda takva usporedba provjerava duljinu povratnog toka, ali ne i cijeli profil brzine ni gubitak tlaka.
:::

## Veza s CFD-om: diskretizacija nije nova fizika {#sec-realni-tok-cfd}

Navier–Stokesove jednadžbe, jednadžba kontinuiteta, materijalni model i rubni uvjeti određuju polje. Jednostavne simetrije omogućuju Poiseuilleovo rješenje; složen difuzor obično traži numerički račun.

**Od jednadžbe do iteracije.** Metoda konačnih volumena (FVM) integrira bilance po ćelijama prema jednadžbi [-@eq-celijska-bilanca-mase]. Aproksimacije tokova, gradijenata i vremenskih promjena pretvaraju jednadžbe u spregnut, uglavnom nelinearan algebarski sustav. Računalo rješava linearizirane sustave i ažurira polja; u nestlačivom modelu tlak i brzina usklađuju se s očuvanjem mase. Iteracija ne odgovara vremenu putovanja tlačnog vala; fizički vremenski korak pripada nestacionarnom računu.

**Primjer na Poiseuilleovu toku.** Podijelimo polumjer cijevi na $N$ prstenastih ćelija širine $\Delta r$ sa središtima $r_i$ i plohama $r_{i\pm1/2}$. Integracija jednadžbe [-@eq-poiseuille-ode] po ćeliji (nakon množenja s $r\,dr$) daje

$$
\begin{aligned}
\mu\left[\left(r\frac{dv}{dr}\right)_{i+1/2}-\left(r\frac{dv}{dr}\right)_{i-1/2}\right]
&=\frac{dp}{dx}\,r_i\,\Delta r, \\
\left(r\frac{dv}{dr}\right)_{i+1/2}&\approx r_{i+1/2}\,\frac{v_{i+1}-v_i}{\Delta r}.
\end{aligned}
$$ {#eq-poiseuille-fvm-celija}

Lijeva je strana razlika viskoznih tokova količine gibanja kroz dvije plohe ćelije, a desna izvor zbog tlaka; to je ista logika bilance kao u jednadžbi [-@eq-celijska-bilanca-mase] za masu. Svaka ćelija daje jednu linearnu jednadžbu s nepoznanicama $v_{i-1}$, $v_i$ i $v_{i+1}$; uz $v=0$ na stijenci i nulti tok kroz os nastaje tridijagonalni sustav od $N$ jednadžbi koji se rješava izravno. Bilježnica iz interaktivnog prikaza na kraju poglavlja rješava upravo taj sustav i uspoređuje rezultat s jednadžbom [-@eq-realni-tok-hagen-poiseuilleov-tok-i-linearni-gubitak-sec-01], a Z6a obrađuje protoke triju takvih mreža. U dvodimenzijskom i trodimenzijskom računu isti zapis vrijedi po ćeliji, ali konvektivni član čini sustav nelinearnim, pa se rješava iterativno.

**Tlak i druge diskretizacije.** Algoritmi sprezanja tlaka i brzine (npr. SIMPLE i PISO) i metoda konačnih elemenata (FEM) samo drukčije zapisuju i rješavaju iste jednadžbe, pa ne mijenjaju fiziku modela; njihove nazive i ulogu objašnjava pojmovnik numeričkih metoda u dodatku D.

**Što provjeriti.** Rezidual mjeri koliko diskretne jednadžbe nisu zadovoljene, a profinjenje ispituje promjenu traženog izlaza; Z6 pokazuje zašto uz konvergenciju protoka zasebno provjeravamo masenu bilancu. Razliku numeričke provjere i validacije mjerenjem razrađuje @sec-cfd-venturi [@nasa-cfd-vv]; @sec-cfd-polja-izlazi povezuje polja s inženjerskim veličinama, a @sec-cfd-vv-paketi donosi pripremljene podatke.

::: {.mf1-samoprovjera}
<p class="mf1-box-label">Provjeri sebe</p>

1. Kako stacionarni tok može imati nenulto ubrzanje?

::: {.callout-note collapse="true"}
### Odgovor
Zbog konvektivnog ubrzanja: čestica prelazi u područje druge brzine, primjerice u suženju, iako se polje u vremenu ne mijenja.
:::

2. Koja pretpostavka omogućuje zapis $\mu\nabla^2\vec v$?

::: {.callout-note collapse="true"}
### Odgovor
Potrebni su newtonski fluid, konstantna viskoznost i nestlačivost.
:::

3. Zašto Hagen–Poiseuilleov rezultat mora biti test svakog općeg modela gubitaka?

::: {.callout-note collapse="true"}
### Odgovor
On daje točan laminarni granični slučaj $\Delta p\propto Q$.
:::

4. Što fizikalno znači promjena znaka $\tau_{st}$?

::: {.callout-note collapse="true"}
### Odgovor
Promjena znaka označuje promjenu smjera smicanja i lokalni povratni tok; zaključak o odvajanju zahtijeva odgovarajuću geometriju i uvjete graničnog sloja.
:::

5. Gruba mreža pogađa brzinu u osi cijevi. Zašto to još ne jamči točno smično naprezanje na stijenci?

::: {.callout-note collapse="true"}
### Odgovor
Smično naprezanje $\tau_{st}=\mu\,dv/dr|_R$ ovisi o nagibu profila u prvoj ćeliji uz stijenku, a ne o vrijednosti u osi; gruba mreža može pogoditi maksimum i protok uz pogrešan nagib. Zato se uz protok provjeravaju i $\tau_{st}$ ili $\lambda$, koji su osjetljiviji na razlučivost uz stijenku, a mrežna konvergencija provjerava se pri istom modelu.
:::
:::


## Zadatci za vježbu {#sec-realni-tok-zadaci}

![Skice uz Z1–Z6: lokalni tok, viskozni pogoni i profinjenje mreže.](../assets/print/u12_realni_tok_vjezbe_skice.svg){#fig-realni-tok-vjezbe fig-align="center" fig-alt="Šest panela: polje brzine duž osi x, vodoravna cijev s izmjerenim padom tlaka i prvom ćelijom uz stijenku, vodoravna kapilara s dvama tlačnim priključcima, uljni film između mirne i pomične ploče, ploha s vanjskim tokom i tri mreže iste domene."}

**Napomene uz skice.** Z1 prikazuje kinematičko polje, a ne cijev; duljine strelica nisu u mjerilu traženih brzina. U Z2 prva ćelija uz stijenku nije u mjerilu, a $\tau_{st}$ je naprezanje stijenke na fluid. U Z3 promjer kapilare nacrtan je uvećano. U Z4 $dp/dx>0$ znači da tlak raste udesno, pa tlačni pogon djeluje suprotno gibanju gornje ploče. U Z6 mrežne crte nisu krute stijenke; profinjenje ne mijenja domenu.

::::: {.mf1-vjezbe-list}

### Lokalno i konvektivno ubrzanje {#task-materijalna-derivacija .unnumbered .unlisted}

**Tekst zadatka**

Jednodimenzijsko kinematičko polje glasi $v(x,t)=a_0t+bx^2$, gdje su $a_0=2\ \text{m/s}^2$ i $b=1\ \text{m}^{-1}\text{s}^{-1}$. Promatra se položaj $x=1\ \text{m}$ u trenutku $t=2\ \text{s}$. Polje služi za vježbu materijalne derivacije i ne opisuje potpuno nestlačivo strujanje u cijevi.

**Traži se**

Odredi brzinu, lokalno, konvektivno i ukupno ubrzanje čestice u zadanom položaju i trenutku.

:::: {.content-visible .mf1-hint-online when-format="html"}
::: {.callout-note collapse="true" data-hint-key="true"}
### Naputak

Najprije izračunaj brzinu u zadanoj točki. U lokalnom članu deriviraj po vremenu uz stalan položaj; u konvektivnom pomnoži brzinu s prostornom derivacijom polja.
:::
::::
:::: {.content-visible .mf1-answer-online when-format="html"}
::: {.callout-tip collapse="true" data-answer-key="true"}
### Kontrolni rezultat

$v=5\ \text{m/s}$; $a_{lok}=2\ \text{m/s}^2$, $a_{kon}=10\ \text{m/s}^2$ i $a=12\ \text{m/s}^2$.
:::
::::

[Razina: T1]{.mf1-task-level}

<span id="task-viskozna-difuzija"></span>

### Smično naprezanje iz pada tlaka i visina prve ćelije {#task-smicno-naprezanje-prva-celija .unnumbered .unlisted}

**Tekst zadatka**

U vodoravnoj cijevi unutarnjeg promjera $D=50{,}0\ \text{mm}$ voda gustoće $\rho=998\ \text{kg/m}^3$ i kinematičke viskoznosti $\nu=1{,}00\cdot10^{-6}\ \text{m}^2/\text{s}$ struji srednjom brzinom $v=2{,}00\ \text{m/s}$. Na potpuno razvijenoj dionici duljine $L=4{,}00\ \text{m}$ između dvaju tlačnih priključaka na istoj visini izmjeren je pad tlaka $\Delta p=p_1-p_2=3{,}20\ \text{kPa}$. Za CFD proračun iste dionice treba procijeniti visinu središta prve ćelije uz stijenku. Vezu smičnog naprezanja s koeficijentom trenja cjevovoda obrađuje []{.mf1-chapter-ref target="u13"}.

**Traži se**

1. Iz bilance sila na valjak fluida između priključaka odredi smično naprezanje na stijenci $\tau_{st}$ i brzinu trenja $u_\tau$.
2. Odredi visinu središta prve ćelije $y_1$ za $y^+=1$ (razrješavanje viskoznog podsloja) i za $y^+=30$ (zidna funkcija).
3. Koliki bi pad tlaka na istoj dionici predvidio Hagen–Poiseuilleov izraz za laminarni tok? Što iz usporedbe s mjerenjem zaključuješ o režimu i vrijedi li bilanca iz točke 1 neovisno o njemu?

:::: {.content-visible .mf1-hint-online when-format="html"}
::: {.callout-note collapse="true" data-hint-key="true"}
### Naputak

Na razvijenoj dionici fluid se ne ubrzava, pa tlačna sila $\Delta p\,\pi D^2/4$ drži ravnotežu sa silom trenja $\tau_{st}\,\pi DL$ po plaštu. Iz definicije $y^+=u_\tau y/\nu$ slijedi $y_1=y^+\nu/u_\tau$. Bilanca sila ne pretpostavlja oblik profila; Hagen–Poiseuilleov izraz $\Delta p=32\mu Lv/D^2$ pretpostavlja laminarni parabolični profil.
:::
::::
:::: {.content-visible .mf1-answer-online when-format="html"}
::: {.callout-tip collapse="true" data-answer-key="true"}
### Kontrolni rezultat

$\tau_{st}=\Delta p\,D/(4L)=10{,}0\ \text{Pa}$, $u_\tau=\sqrt{\tau_{st}/\rho}=0{,}100\ \text{m/s}$. $y_1\approx0{,}0100\ \text{mm}$ za $y^+=1$ i $y_1\approx0{,}300\ \text{mm}$ za $y^+=30$. Laminarni izraz daje $\Delta p\approx102\ \text{Pa}$, oko 31 puta manje od izmjerenoga: uz $Re=vD/\nu=1{,}00\cdot10^5$ tok je turbulentan i parabolični profil ne vrijedi, dok bilanca sila iz točke 1 vrijedi za svaki razvijeni tok. Pripadni koeficijent trenja iznosi $\lambda=8\tau_{st}/(\rho v^2)=0{,}0200$.
:::
::::

[Razina: T1]{.mf1-task-level}

### Viskoznost iz mjerenja u kapilari {#task-poiseuille-inverzni .unnumbered .unlisted}

**Tekst zadatka**

Dinamička viskoznost određuje se iz protoka i razlike tlakova između dvaju priključaka na vodoravnoj kapilari. Sintetički nastavni podatci su $Q=0{,}300\pm0{,}003\ \text{mL/min}$, $\Delta p=p_1-p_2=652\pm5\ \text{Pa}$, $L=0{,}200\pm0{,}001\ \text{m}$ i $D=0{,}500\pm0{,}005\ \text{mm}$. Znakovi $\pm$ označuju neovisne standardne nesigurnosti; standardnu nesigurnost veličine $x$ označujemo sa $s(x)$ jer je $u$ u ovom poglavlju brzina ploče. Newtonski fluid ima gustoću $\rho=998\ \text{kg/m}^3$; njezinu nesigurnost zanemari. Duljina $L$ mjeri se između tlačnih priključaka na istoj visini.

U tom dijelu kružne kapilare pretpostavi potpuno razvijen laminarni tok uz prianjanje uz stijenku, a ulazne učinke smatraj ograničenima na dio ispred mjernog razmaka.

**Traži se**

1. Obrnutim Poiseuilleovim računom procijeni viskoznost i Reynoldsov broj te utvrdi koji mjerni podatak najviše pridonosi nesigurnosti.
2. Procijeni $s(\mu)$ linearnom propagacijom nesigurnosti uz korijen zbroja kvadrata doprinosa (RSS) i posebno pokaži doprinos promjera.

:::: {.content-visible .mf1-hint-online when-format="html"}
::: {.callout-note collapse="true" data-hint-key="true"}
### Naputak

Riješi izraz $Q=\pi D^4\Delta p/(128\mu L)$ po viskoznosti. Za neovisne standardne nesigurnosti vrijedi $[s(\mu)/\mu]^2=[4s(D)/D]^2+[s(\Delta p)/\Delta p]^2+[s(L)/L]^2+[s(Q)/Q]^2$.
:::
::::
:::: {.content-visible .mf1-answer-online when-format="html"}
::: {.callout-tip collapse="true" data-answer-key="true"}
### Kontrolni rezultat

$\mu\approx1{,}000\ \text{mPa s}$, $s(\mu)\approx0{,}042\ \text{mPa s}$ i $Re\approx12{,}7$. Doprinos samog promjera relativnoj standardnoj nesigurnosti iznosi $4\,\%$, pa je on najveći doprinos ukupnoj mjernoj nesigurnosti.
:::
::::

[Razina: T2]{.mf1-task-level}

### Povratni tok između ploča {#task-couette-povrat .unnumbered .unlisted}

**Tekst zadatka**

U uskom procjepu gibanje gornje ploče i nepovoljan gradijent tlaka tjeraju ulje u suprotnim smjerovima. Newtonski fluid ima $\mu=0{,}100\ \text{Pa s}$; donja ploča na $y=0$ miruje, a gornja na $y=H$ klizi u pozitivnom smjeru osi $x$ brzinom $u=2{,}00\ \text{m/s}$. Razmak ploča iznosi $H=1{,}00\ \text{mm}$. Za potpuno razvijeni laminarni tok i konstantan gradijent tlaka $dp/dx>0$ vrijedi $v(y)=uy/H+(dp/dx)(y^2-Hy)/(2\mu)$.

Ovdje je $\tau_0$ komponenta sile fluida na donju ploču po jedinici površine u smjeru osi $x$. Obje su ploče nepropusne i uz njih nema klizanja.

Usporedi $dp/dx=0{,}90\,(dp/dx)_{krit}$ i $dp/dx=1{,}10\,(dp/dx)_{krit}$.

**Traži se**

1. Odredi kritični gradijent $(dp/dx)_{krit}$ pri kojem $\tau_0=\mu v'(0)$ mijenja znak, a zatim $\tau_0$ za oba zadana gradijenta.
2. Skiciraj profile brzine za oba zadana pogona. Razlikuj povratni tok uz ploču od prolaza kroz nju.

:::: {.content-visible .mf1-hint-online when-format="html"}
::: {.callout-note collapse="true" data-hint-key="true"}
### Naputak

Deriviraj profil i postavi $\tau_0=0$. Provjeri $v(0)=0$ i $v(H)=u$. Negativna brzina može nastati neposredno uz donju ploču, ali na samoj ploči brzina ostaje jednaka nuli.
:::
::::
:::: {.content-visible .mf1-answer-online when-format="html"}
::: {.callout-tip collapse="true" data-answer-key="true"}
### Kontrolni rezultat

$(dp/dx)_{krit}=4{,}00\cdot10^5\ \text{Pa/m}$. Pri $0{,}90\,(dp/dx)_{krit}$ vrijedi $\tau_0=+20{,}0\ \text{Pa}$ i $v(y)>0$ za $0<y\le H$; pri $1{,}10\,(dp/dx)_{krit}$ vrijedi $\tau_0=-20{,}0\ \text{Pa}$ i povratni tok u $0<y<H/11$. U oba profila $v(0)=0$ i $v(H)=u$; fluid ne prolazi kroz ploče.
:::
::::

[Razina: T2]{.mf1-task-level}

### Izbor modela graničnog sloja {#task-granicni-sloj-model .unnumbered .unlisted}

**Tekst zadatka**

Sintetički nastavni podatci za vodu su $\nu=1{,}00\cdot10^{-6}\ \text{m}^2/\text{s}$, $\rho=998\ \text{kg/m}^3$, $x=0{,}400\ \text{m}$, $U_e=1{,}50\ \text{m/s}$ i $dU_e/dx=-0{,}250\ \text{s}^{-1}$. Ekvivalentna hrapavost iznosi $k_s=5{,}0\ \mu\text{m}$. Vanjski tok smatraj stacionarnim, nestlačivim i približno neviskoznim, uz stalnu visinu.

**Traži se**

1. Izračunaj $Re_x$, Blasiusovu referentnu debljinu $\delta_B=5x/\sqrt{Re_x}$, $k_s/\delta_B$, lokalni eksponent vanjske brzine $m=(x/U_e)\,dU_e/dx$ (Falkner–Skanov parametar; $m=0$ je Blasiusov slučaj) te $dp_e/dx$.
2. Odluči je li Blasiusov model opravdan. Razdvoji uvjetnu referentnu procjenu od potvrđenog modela te obrazloži koje bi dodatne provjere trebale prethoditi njegovoj uporabi. Mali $k_s/\delta_B$ nemoj poistovjetiti s dokazanom hidrauličkom glatkoćom niti prijelaz određivati iz jednoga univerzalnog praga $Re_x$.

:::: {.content-visible .mf1-hint-online when-format="html"}
::: {.callout-note collapse="true" data-hint-key="true"}
### Naputak

Blasiusovo rješenje zahtijeva glatku plohu, laminaran tok i nulti gradijent tlaka. U zadanom vanjskom toku vrijedi $dp_e/dx=-\rho U_e\,dU_e/dx$. Odvoji dokazano prekršen uvjet od pretpostavke koju podatci još ne potvrđuju.
:::
::::
:::: {.content-visible .mf1-answer-online when-format="html"}
::: {.callout-tip collapse="true" data-answer-key="true"}
### Kontrolni rezultat

$Re_x=6{,}00\cdot10^5$, $\delta_B\approx2{,}58\ \text{mm}$, $k_s/\delta_B\approx1{,}94\cdot10^{-3}$, $m=-0{,}0667$ i $dp_e/dx\approx+374\ \text{Pa/m}$. Uvjet nultoga gradijenta tlaka nije zadovoljen; laminarnost i hidraulička glatkoća nisu dokazane. Blasiusov model nije opravdan za predviđanje debljine sloja: $\delta_B$ je samo referenca. Potrebno je provjeriti profil brzine i prijelaz.
:::
::::

[Razina: T3]{.mf1-task-level}

### Konvergencija i izbor mreže {#task-cfd-tri-mreze .unnumbered .unlisted}

**Tekst zadatka**

**a) Izbor mreže.** Sintetički Poiseuilleov skup podataka iz `data/cfd/poiseuille_laminar` prikazan je sa zaokruženim vrijednostima. Tri sustavno profinjene mreže imaju $h/h_f=(4;\ 2;\ 1)$, protoke $(Q_g;\ Q_{sr};\ Q_f)=(8{,}16814;\ 7{,}93252;\ 7{,}87362)\cdot10^{-6}\ \text{m}^3/\text{s}$ i masene debalanse $(0{,}040;\ 0{,}010;\ 0{,}0025)\,\%$, redom od grube do fine. Računaj s ovdje ispisanim brojevima, uz omjer koraka susjednih mreža $\lambda_h=2$ i faktor sigurnosti $F_s=1{,}25$; zahtijevaju se $GCI\le0{,}50\,\%$ i maseni debalans najviše $0{,}0050\,\%$.

**b) Usporedba otpora.** Za profil NACA 0012 pri $Re_l=6\cdot10^6$ (prema tetivi $l$), $Ma=0{,}15$ i napadnom kutu $\theta=10{,}00^\circ$ uzmi $C_{D,CFD}=0{,}01222$ (najfinija FUN3D mreža) i $C_{D,ref}=0{,}01166$ (linearna interpolacija javno dostupnih mjerenja na isti kut; podrijetlo i ograde navedeni su u dodatku D). Zadane standardne nesigurnosti nastavnog scenarija jesu mjerna $s_{mj}=0{,}00020$, numerička $s_{num}=0{,}00010$ (ukupna; GCI iz dijela a) ne pribraja se) i doprinos usklađivanja uvjeta i interpolacije $s_{uv}=0{,}00010$. Doprinosi su neovisni, normalno raspodijeljeni i nakon korekcija centrirani na nulu. To su pretpostavke za vježbu, a ne objavljene nesigurnosti NASA-ina pokusa. Usporedba je sukladna zadanom kriteriju ako $|E|\le 2s_E$, gdje je $s_E$ standardna nesigurnost razlike (dvostruka standardna nesigurnost daje približno 95 % pokrivanja). Dodatno razmotri $s_{mj}=0{,}00030$ uz nepromijenjene ostale vrijednosti.

**Traži se**

1. **Dio a).** Odredi opaženi red konvergencije $n_h$, Richardsonovu ekstrapolaciju $Q_{ext}$ te $GCI_{sr}$ i $GCI_f$ srednje i fine mreže. Odaberi najgrublju mrežu koja zadovoljava zadane numeričke kriterije.
2. **Dio b).** Izračunaj $E=C_{D,CFD}-C_{D,ref}$, relativno odstupanje prema referenci i proširenu nesigurnost razlike $2s_E=2\sqrt{s_{mj}^2+s_{num}^2+s_{uv}^2}$.
3. Ponovi odluku za veću zadanu vrijednost $s_{mj}$ uz nepromijenjene ostale vrijednosti. Objasni znači li eventualno zadovoljen kriterij točniji model i zašto rezultat dijela a) ne dokazuje valjanost modela profila.

:::: {.content-visible .mf1-hint-online when-format="html"}
::: {.callout-note collapse="true" data-hint-key="true"}
### Naputak

Za monotoni niz koristi $n_h=\ln[(Q_g-Q_{sr})/(Q_{sr}-Q_f)]/\ln\lambda_h$ i $Q_{ext}=Q_f+(Q_f-Q_{sr})/(\lambda_h^{n_h}-1)$. Zatim izračunaj $GCI_f=F_s|(Q_f-Q_{sr})/Q_f|/(\lambda_h^{n_h}-1)$; za $GCI_{sr}$ zamijeni par $(Q_f,Q_{sr})$ parom $(Q_{sr},Q_g)$. Razlomke pretvori u postotke i provjeri oba uvjeta.

U dijelu b) sve su nesigurnosti apsolutne i bezdimenzijske, kao i $C_D$. Relativno odstupanje iznosi $100E/C_{D,ref}$ u postotcima. Provjeri sadrži li interval $[E-2s_E;\ E+2s_E]$ nulu. Veća nesigurnost širi interval, ali ne mijenja središnju razliku.
:::
::::
:::: {.content-visible .mf1-answer-online when-format="html"}
::: {.callout-tip collapse="true" data-answer-key="true" data-key-full="true"}
### Kontrolni rezultat

**a)** $n_h\approx2{,}000$, $Q_{ext}\approx7{,}8540\cdot10^{-6}\ \text{m}^3/\text{s}$, $GCI_{sr}\approx1{,}237\,\%$ i $GCI_f\approx0{,}312\,\%$. Odabire se fina mreža: debalans je $0{,}0025\,\%$; srednja krši oba uvjeta, a gruba maseni uvjet.

**b)** $E=+0{,}00056$, odnosno približno $+4{,}80\,\%$; CFD daje veći otpor. Za $s_{mj}=0{,}00020$ dobiva se $2s_E\approx0{,}000490$ i $|E|/(2s_E)\approx1{,}14>1$: kriterij nije zadovoljen. Za $s_{mj}=0{,}00030$ vrijedi $2s_E\approx0{,}000663$ i $|E|/(2s_E)\approx0{,}844<1$: kriterij je zadovoljen. Razlika ostaje ista; širi interval znači slabiju sposobnost razlikovanja modela od reference, a ne poboljšanje modela. To je uvjetna procjena za zadane nastavne pretpostavke: stvarna validacija traži dokumentirane reziduale, povijesti sila, masenu bilancu i stvarni proračun nesigurnosti (dodatak D). Konvergencija Poiseuilleova protoka ne potvrđuje turbulentni otpor profila.
:::
::::

[Razina: T4]{.mf1-task-level}

:::::

::: {.mf1-interaktivno}
<p class="mf1-box-label">Interaktivni prikaz — Profil, mreža i pogreška</p>

**Predvidi.** Kako će profinjenje promijeniti profil, protok i pogrešku? Može li finija mreža opravdati pogrešan izbor laminarnog modela?

**Provjeri i protumači.** U laboratoriju usporedi rješenje po prstenastim ćelijama s analitičkim rješenjem i bilancom sila. Odvoji taj račun od integracije poznatog profila i sintetičkih podataka iz Z6; mali rezidual i mala pogreška nisu isto.

<div class="mf1-interaktivno-akcija">
<a class="mf1-interaktivno-veza" href="https://martibasic.github.io/MF1_udzbenik/jlite/lab/index.html?path=u12_poiseuille_konvergencija.ipynb">Pokreni u pregledniku</a>
<a class="mf1-interaktivno-veza" href="https://colab.research.google.com/github/martibasic/MF1_udzbenik/blob/main/notebooks/u12_poiseuille_konvergencija.ipynb" target="_blank" rel="noopener">Pričuvno: otvori u Colabu</a>
<img class="mf1-interaktivno-qr" src="../assets/qr/u12_poiseuille_konvergencija_jlite.svg" alt="QR kod za Poiseuilleov pokus konvergencije u pregledniku"/>
</div>
:::

## Sažetak

::: {.mf1-zavrsni-okvir}
- Materijalna derivacija povezuje Eulerov opis polja s ubrzanjem čestice.
- Navier–Stokesova jednadžba jest lokalna bilanca količine gibanja uz konstitutivni zakon newtonskog fluida.
- Analitička rješenja nastaju iz jasno navedenih simetrija i rubnih uvjeta.
- Laminarni tok u cijevi daje $\Delta p\propto Q$ i zato je obvezan granični test modela gubitaka.
- Granični sloj prenosi utjecaj uvjeta prianjanja; nepovoljan gradijent tlaka može izazvati odvajanje.
- Turbulencijski model zatvara korelacije fluktuacija; numerička konvergencija i fizikalna validacija nisu isto.

**Najčešća pogreška.** Mali rezidual ili mrežnu konvergenciju proglasiti potvrdom fizikalnog modela, koji se zasebno provjerava usporedbom s mjerenjem ili referentnim rješenjem.

**Nakon ovoga poglavlja mora biti moguće**

1. iz zadanog polja brzine odrediti lokalno, konvektivno i ukupno ubrzanje čestice;
2. iz Navier–Stokesove jednadžbe uz rubne uvjete izvesti profil između ploča i Hagen–Poiseuilleov profil te iz njega $\Delta p\propto Q$ i $\lambda=64/Re$;
3. procijeniti debljinu graničnog sloja i provjeriti uvjete primjene Blasiusova rješenja;
4. odvojiti mrežnu konvergenciju (GCI, maseni debalans) od validacije mjerenjem.
:::
