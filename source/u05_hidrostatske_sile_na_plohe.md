![Od raspodjele hidrostatskog tlaka do rezultantne sile i njezina pravca djelovanja na ravnoj plohi](../assets/print/u05_fig_uvod_pregled.svg){#fig-u05-pregled-sila-na-plohe fig-align="center" style="width:100%;max-width:980px;" fig-alt="Od raspodjele hidrostatskog tlaka do rezultantne sile i njezina pravca djelovanja na ravnoj plohi"}

## Od lokalnog tlaka do sile na plohu

Tlak je lokalna veličina, a poklopac, vrata ili stijenka odgovaraju na njegovu raspodjelu po cijeloj površini. Zato hidrostatika ploha uvijek traži dva odgovora:

1. koliki je vektor rezultantne sile;
2. kojim pravcem taj vektor djeluje.

Na ravnoj plohi sve lokalne tlačne sile imaju isti smjer, pa se integracijom traže iznos i centar tlaka. Na zakrivljenoj plohi lokalne normale mijenjaju smjer, pa je pouzdanije najprije odrediti horizontalnu i vertikalnu komponentu. Oba slučaja proizlaze iz istoga temeljnog zapisa

$$
d\mathbf F=p\,\mathbf n_f\,dA,
$$ {#eq-sile-plohe-od-lokalnog-tlaka-do-sile-na-plohu-01}

gdje je $\mathbf n_f$ jedinična normala usmjerena **iz stvarnog fluida prema stijenci**. Ta definicija normale nije formalnost: ona određuje predznak svake komponente sile.

::: {.mf1-application}
<p class="mf1-box-label">Lajtmotiv — isti model u različitim sustavima</p>

Isti se račun pojavljuje na brodskim i procesnim poklopcima, ustavama retencijskih bazena, stijenkama rashladnih spremnika i zakrivljenim prijelazima vodnih građevina. Hidrostatika daje opterećenje fluida za zadanu geometriju i stanje. Ne provjerava sama po sebi čvrstoću, zamor, brtvljenje, stabilnost cijele konstrukcije ni normativnu prihvatljivost.
:::

::: {.mf1-priprema}
<p class="mf1-box-label">Ishodi i pretpostavke poglavlja</p>

Nakon poglavlja student može:

- od referentnog tlaka i geometrije postaviti neto raspodjelu tlaka;
- izvesti rezultantu i centar tlaka ravne plohe;
- jasno definirati kut nagnute plohe i postaviti momentnu ravnotežu;
- rastaviti silu na zakrivljenu plohu preko vertikalne projekcije i pomoćnog volumena;
- odrediti smjer $F_V$ iz stvarne okupane strane, a ne iz položaja nacrtanog pomoćnog volumena;
- provjeriti rezultat bilansom momenata, graničnim slučajem ili neovisnom integracijom.

U glavnom modelu fluid miruje, gustoća svakog homogenog sloja je stalna, gravitacijsko polje je jednoliko, a kapilarni učinci nisu važni za razmatranu mjeru.

**Procijenjeno vrijeme rada uz udžbenik:** 11 sati.
:::

## Referentni tlak i smjer sile

Prije integriranja treba nacrtati obje strane plohe. Neto tlak je razlika tlakova koji djeluju s njezinih dviju strana. Ako je spremnik otvoren i atmosfera djeluje i na slobodnu površinu i na vanjsku stranu poklopca, atmosferski se doprinos poništava. Tada je najjednostavnije rabiti manometarski tlak

$$
p=\rho gh.
$$ {#eq-sile-plohe-referentni-tlak-i-smjer-sile-01}

Ako se jednoliki tlak $p_0$ **ne poništava**, neto raspodjela glasi

$$
p_{\mathrm{net}}(h)=p_0+\rho gh.
$$ {#eq-sile-plohe-referentni-tlak-i-smjer-sile-02}

Jednoliki član mijenja i silu i položaj njezina hvatišta. Zbog toga formula za centar tlaka izvedena samo za $p=\rho gh$ ne smije biti automatski primijenjena na zatvoren spremnik s plinskim nadtlakom.

::: {.mf1-temelj}
<p class="mf1-box-label">Temelj — radni slijed prije računa</p>

1. Izdvoji plohu i označi stvarnu okupanu stranu.
2. Zapiši je li tlak apsolutni, manometarski ili neto tlak između dviju strana.
3. Odaberi osi i pozitivne smjerove; za nagnutu plohu definiraj kut prema navedenoj osi.
4. Integriraj silu i moment iste raspodjele tlaka.
5. Provjeri nalazi li se pravac djelovanja unutar fizički mogućeg područja i odgovara li smjer lokalnim tlačnim strelicama.
:::

## Ravna ploha: rezultanta i centar tlaka

Na ravnoj plohi normala je stalna. Zato se vektorska integracija svodi na određivanje iznosa

$$
F=\int_A p\,dA.
$$ {#eq-sile-plohe-ravna-ploha-rezultanta-i-centar-tlaka-01}

Za otvoren spremnik i neto manometarski tlak $p=\rho gh$ vrijedi

$$
F=\rho g\int_A h\,dA=\rho gAh_C,
$$ {#eq-u05-sila-ravna-ploha}

gdje je $A$ površina plohe, a $h_C$ vertikalna dubina njezina težišta. Rezultanta djeluje okomito na plohu, od fluida prema stijenci. Zapis $F=p_C A$ valjan je zato što je u homogenom fluidu tlak linearna funkcija dubine, pa je srednji tlak jednak tlaku u težištu plohe.

Za vertikalni pravokutni pojas širine $b$, od dubine $h_a$ do $h_b$, isti rezultat dobiva se izravno:

$$
F=\rho gb\int_{h_a}^{h_b}h\,dh
=\frac{\rho gb}{2}\left(h_b^2-h_a^2\right).
$$ {#eq-sile-plohe-ravna-ploha-rezultanta-i-centar-tlaka-02}

Faktorizacija razlike kvadrata vraća $F=\rho gA(h_a+h_b)/2$. Integralni i težišni zapis nisu dvije različite metode, nego dva oblika iste bilance.

### Centar tlaka

Pravac djelovanja rezultante dobiva se iz jednakosti momenata. Za vertikalnu koordinatu $h$ mjerenu od slobodne površine prema dolje,

$$
Fh_{CP}=\int_A h\,p\,dA=\rho g\int_A h^2\,dA.
$$ {#eq-sile-plohe-centar-tlaka-01}

Za neto polje $p=\rho gh$ slijedi

$$
h_{CP}=\frac{I_O}{Ah_C}
=h_C+\frac{I_G}{Ah_C},
$$ {#eq-u05-centar-tlaka-vertikalna}

gdje je $I_G$ drugi moment površine oko centroidne osi paralelne slobodnoj površini, a $I_O=I_G+Ah_C^2$. Za nehorizontalnu plohu pod pozitivnim manometarskim tlakom centar tlaka nalazi se dublje od težišta. To nije opće pravilo za svaku moguću raspodjelu: za vodoravnu plohu ili jednoliki neto tlak hvatište je u težištu, a za kombinaciju $p_0+\rho gh$ treba momentirati cijelu raspodjelu.

Ako je $p_0$ jednoliki neto doprinos, opći zapis za dubinu hvatišta jest

$$
h_R=\frac{\int_A h\,(p_0+\rho gh)\,dA}
{(p_0+\rho gh_C)A}.
$$ {#eq-sile-plohe-centar-tlaka-02}

Taj oblik je sigurniji od pamćenja posebnih korekcija jer prisiljava da sila i moment potječu iz istoga tlaka.

### Nagnuta ploha i jasno definiran kut

Neka je $s$ koordinata duž linije najvećeg pada po plohi, a $\theta$ kut te linije prema **vodoravnici**, $0\leq\theta\leq90^\circ$. Ako je početna točka osi $s$ na dubini $h_0$, tada je

$$
h(s)=h_0+s\sin\theta.
$$ {#eq-sile-plohe-nagnuta-ploha-i-jasno-definiran-kut-01}

Za potpuno uronjenu ravnu plohu i $p_0=0$ rezultanta ostaje

$$
F=\rho gAh_C,
$$ {#eq-sile-plohe-nagnuta-ploha-i-jasno-definiran-kut-02}

ali samo uz usporedbu ploha jednake površine i jednake vertikalne dubine težišta. Nagib nije nestao iz geometrije: određuje dubine rubova, smjer normale i krak sile prema zglobu.

Moment oko centroidne osi paralelne slobodnoj površini daje položaj centra tlaka duž plohe

$$
s_{CP}=s_C+\frac{I_G\sin\theta}{Ah_C},
$$ {#eq-sile-plohe-nagnuta-ploha-i-jasno-definiran-kut-03}

a njegova vertikalna dubina iznosi

$$
h_{CP}=h_C+\frac{I_G\sin^2\theta}{Ah_C}.
$$ {#eq-u05-centar-tlaka-nagnuta}

Za $\theta=90^\circ$ dobiva se vertikalna ploha. Kada $\theta\to0$ tlak po vodoravnoj plohi postaje jednolik i $h_{CP}\to h_C$. To je važan granični slučaj izvoda.

::: {.mf1-interaktivno}
<p class="mf1-box-label">Numerički pokus — ravna ploha</p>

Prije pokretanja predvidite kako će se promijeniti $F$ i razlika $h_{CP}-h_C$ kada se cijela ploha spusti dublje, a kako kada se pri istoj dubini težišta promijeni nagib.

<div class="mf1-interaktivno-akcija">
<a class="mf1-interaktivno-veza" href="https://martibasic.github.io/MF1_udzbenik/jlite/lab/index.html?path=u05_sila_na_ravnu_plohu.ipynb">Pokreni u pregledniku</a>
<a class="mf1-interaktivno-veza" href="https://colab.research.google.com/github/martibasic/MF1_udzbenik/blob/main/notebooks/u05_sila_na_ravnu_plohu.ipynb" target="_blank" rel="noopener">Pričuvno: otvori u Colabu</a>
<img class="mf1-interaktivno-qr" src="../assets/qr/u05_sila_na_ravnu_plohu.svg" alt="QR kod za numerički pokus hidrostatske sile na ravnu plohu"/>
</div>
:::

## Riješeni primjeri: ravne plohe

::: {#ex-u05-vertikalna-pravokutna-zaklopka .mf1-we}
<p class="mf1-box-label">Riješeni primjer — Vertikalna pravokutna zaklopka <span class="mf1-level">T2</span></p>

Pravokutna zaklopka širine $b=2{,}0\ \mathrm{m}$ i visine $H=3{,}0\ \mathrm{m}$ potpuno je uronjena u vodu gustoće $\rho=998\ \mathrm{kg/m^3}$. Gornji joj je rub na dubini $h_1=2{,}0\ \mathrm{m}$. Vanjska je strana na atmosferi. Odredite rezultantnu silu i centar tlaka.

![Vertikalna pravokutna zaklopka s dubinama rubova, težištem i centrom tlaka](../assets/print/u05_val1_pravokutna_zaklopka.svg){#fig-u05-vertikalna-pravokutna-zaklopka fig-align="center" fig-alt="Vertikalna pravokutna zaklopka s dubinama rubova, težištem i centrom tlaka"}

**Pretpostavke.** Računa se neto manometarski tlak; voda miruje i gustoća je stalna. Zaklopka je ravna, a deformacija se ne razmatra.

Površina i dubina težišta jesu

$$
A=bH=6{,}0\ \mathrm{m^2},\qquad
h_C=h_1+\frac H2=3{,}5\ \mathrm{m}.
$$ {#eq-sile-plohe-rijeseni-primjer-vertikalna-pravokutna-zaklopka-01}

Stoga je

$$
F=\rho gAh_C
=998\cdot9{,}81\cdot6{,}0\cdot3{,}5
=205{,}6\ \mathrm{kN}.
$$ {#eq-sile-plohe-rijeseni-primjer-vertikalna-pravokutna-zaklopka-02}

Za centroidnu vodoravnu os pravokutnika

$$
I_G=\frac{bH^3}{12}=4{,}50\ \mathrm{m^4},
$$ {#eq-sile-plohe-rijeseni-primjer-vertikalna-pravokutna-zaklopka-03}

pa je

$$
h_{CP}=3{,}5+\frac{4{,}50}{6{,}0\cdot3{,}5}
=3{,}714\ \mathrm{m}.
$$ {#eq-sile-plohe-rijeseni-primjer-vertikalna-pravokutna-zaklopka-04}

Centar tlaka je $1{,}714\ \mathrm{m}$ ispod gornjeg ruba.

**Neovisna provjera.** Tlak na gornjem i donjem rubu iznosi $19{,}58$ i $48{,}95\ \mathrm{kPa}$. Srednja vrijednost linearnog dijagrama jest $34{,}27\ \mathrm{kPa}$, a $34{,}27\cdot6{,}0=205{,}6\ \mathrm{kN}$. Hvatište mora biti između težišta na $3{,}5\ \mathrm{m}$ i donjeg ruba na $5{,}0\ \mathrm{m}$, što je zadovoljeno.
:::

::: {#ex-u05-kosi-poklopac .mf1-we}
<p class="mf1-box-label">Riješeni primjer — Kosi poklopac sa spojnicom <span class="mf1-level">T2</span></p>

Pravokutni poklopac širine $b=0{,}90\ \mathrm{m}$ i duljine $L=1{,}20\ \mathrm{m}$ zglobno je vezan na gornjem rubu $A$, koji je na dubini $h_A=0{,}80\ \mathrm{m}$. Ploha zatvara kut $\theta=60^\circ$ s vodoravnicom. Spojnica na donjem rubu djeluje okomito na plohu. Odredite hidrostatsku silu, njezin krak prema zglobu i silu spojnice.

![Kosi poklopac s kutom prema vodoravnici, zglobom, centrom tlaka i spojnicom](../assets/print/u05_val3_kosi_poklopac.svg){#fig-u05-kosi-poklopac fig-align="center" fig-alt="Kosi poklopac s kutom prema vodoravnici, zglobom, centrom tlaka i spojnicom"}

**Pretpostavke.** S obje strane poništava se atmosferski tlak; težina poklopca i trenje zgloba nisu dio zadanog modela. Rezultat je samo statičko opterećenje za tu idealizaciju.

Površina i dubina težišta su

$$
A=bL=1{,}08\ \mathrm{m^2},\qquad
h_C=h_A+\frac L2\sin\theta=1{,}3196\ \mathrm{m}.
$$ {#eq-sile-plohe-rijeseni-primjer-kosi-poklopac-sa-spojnicom-t2-01}

Zato je

$$
F=\rho gAh_C=13{,}95\ \mathrm{kN}.
$$ {#eq-sile-plohe-rijeseni-primjer-kosi-poklopac-sa-spojnicom-t2-02}

Koordinata $s$ mjeri se od zgloba niz plohu. Budući da je $h(s)=h_A+s\sin\theta$, jednakost momenata daje

$$
s_{CP}=
\frac{h_A L^2/2+(\sin\theta)L^3/3}
{h_A L+(\sin\theta)L^2/2}
=0{,}679\ \mathrm{m}.
$$ {#eq-sile-plohe-rijeseni-primjer-kosi-poklopac-sa-spojnicom-t2-03}

Moment tlaka oko zgloba iznosi $M_A=Fs_{CP}=9{,}47\ \mathrm{kN\,m}$. Spojnica ima krak $L$, pa

$$
T=\frac{M_A}{L}=7{,}89\ \mathrm{kN}.
$$ {#eq-sile-plohe-rijeseni-primjer-kosi-poklopac-sa-spojnicom-t2-04}

**Neovisna provjera.** Težište poklopca je $0{,}600\ \mathrm{m}$ od zgloba, a centar tlaka mora biti dalje niz plohu jer tlak raste: $0{,}600<s_{CP}<1{,}200\ \mathrm{m}$. Momentna bilanca izravno vraća $TL=Fs_{CP}$; usporedba samih magnituda $T$ i $F$ ne bi bila dovoljna.
:::

::: {#ex-u05-pregrada-ulje-voda .mf1-we}
<p class="mf1-box-label">Riješeni primjer — Zglobna pregrada s uljem iznad vode <span class="mf1-level">T3</span></p>

Vertikalna pregrada širine $b=1{,}40\ \mathrm{m}$ zglobno je vezana na slobodnoj površini. Gornji sloj ulja ima $\rho_o=820\ \mathrm{kg/m^3}$ i visinu $h_o=1{,}00\ \mathrm{m}$, a donji sloj vode $\rho_w=1000\ \mathrm{kg/m^3}$ i visinu $h_w=1{,}80\ \mathrm{m}$. Donji rub pridržava vodoravna spojnica. Odredite silu, centar tlaka i statičke reakcije.

![Zglobna vertikalna pregrada s izlomljenim dijagramom tlaka kroz ulje i vodu](../assets/print/u05_ch1_pregrada_ulje_voda.svg){#fig-u05-pregrada-ulje-voda fig-align="center" fig-alt="Zglobna vertikalna pregrada s izlomljenim dijagramom tlaka kroz ulje i vodu"}

**Pretpostavke.** Fluidi miruju, ne miješaju se i svaki ima stalnu gustoću. Atmosferski tlak se poništava. Zglob i spojnica modeliraju se idealno; ne donosi se zaključak o njihovoj konstrukcijskoj dostatnosti.

Na uljnom polju tlak čini trokut, pa je

$$
F_1=\frac12\rho_o gb h_o^2=5{,}631\ \mathrm{kN}.
$$ {#eq-sile-plohe-rijeseni-primjer-zglobna-pregrada-s-uljem-iznad-01}

Na vodenom polju ostaje pravokutni doprinos uljnog stupca i trokutni doprinos vode:

$$
F_{2,r}=\rho_o gbh_oh_w=20{,}271\ \mathrm{kN},
$$ {#eq-sile-plohe-rijeseni-primjer-zglobna-pregrada-s-uljem-iznad-02}

$$
F_{2,t}=\frac12\rho_wgbh_w^2=22{,}249\ \mathrm{kN}.
$$ {#eq-sile-plohe-rijeseni-primjer-zglobna-pregrada-s-uljem-iznad-03}

Ukupna sila iznosi

$$
F=F_1+F_{2,r}+F_{2,t}=48{,}151\ \mathrm{kN}.
$$ {#eq-sile-plohe-rijeseni-primjer-zglobna-pregrada-s-uljem-iznad-04}

Momenti oko gornjeg zgloba računaju se preko težišta svakog dijela dijagrama tlaka:

$$
M_A=
F_1\frac{2h_o}{3}
+F_{2,r}\left(h_o+\frac{h_w}{2}\right)
+F_{2,t}\left(h_o+\frac{2h_w}{3}\right)
=91{,}218\ \mathrm{kN\,m}.
$$ {#eq-sile-plohe-rijeseni-primjer-zglobna-pregrada-s-uljem-iznad-05}

Zato su

$$
h_{CP}=\frac{M_A}{F}=1{,}894\ \mathrm{m},
$$ {#eq-sile-plohe-rijeseni-primjer-zglobna-pregrada-s-uljem-iznad-06}

$$
T=\frac{M_A}{h_o+h_w}=32{,}578\ \mathrm{kN},\qquad
R_A=F-T=15{,}574\ \mathrm{kN}.
$$ {#eq-sile-plohe-rijeseni-primjer-zglobna-pregrada-s-uljem-iznad-07}

**Neovisna provjera.** Tlak je kontinuiran na razdjelnici: vodeno polje počinje s tlakom $\rho_o gh_o$, a ne s nulom. Zbroj sila zadovoljava $R_A+T=F$, a zbroj momenata $T(h_o+h_w)=M_A$. Izostavljanje pravokutnog doprinosa $F_{2,r}$ prekršilo bi i kontinuitet tlaka i obje bilance.
:::

## Zakrivljena ploha: projekcija i pomoćni volumen

Na zakrivljenoj plohi lokalne normale nisu paralelne. Izravni vektorski integral i dalje je temelj,

$$
\mathbf F=\int_A p\,\mathbf n_f\,dA,
$$ {#eq-sile-plohe-zakrivljena-ploha-projekcija-i-pomocni-volumen-01}

ali se za često korištene cilindrične i dvodimenzijske geometrije rezultat preglednije nalazi po komponentama.

### Horizontalna komponenta

Za odabrani vodoravni smjer $x$ vrijedi

$$
F_x=\int_A p\,n_{f,x}\,dA.
$$ {#eq-sile-plohe-horizontalna-komponenta-01}

Predznačeni element $n_{f,x}dA$ jednak je projekciji na ravninu okomitu na $x$. Ako se predznak normale ne mijenja i projekcija je jednoznačna, magnituda horizontalne komponente jednaka je sili na **vertikalnu projekciju** zakrivljene plohe:

$$
|F_H|=\rho gA_xh_{Cx}.
$$ {#eq-u05-zakrivljena-horizontalna}

Pravac djelovanja prolazi centrom tlaka te vertikalne projekcije. Kod plohe s pregibom, prevjesom ili promjenom predznaka $n_{f,x}$ površinu treba podijeliti i komponente zbrojiti predznačeno; jedna ukupna „sjena” tada nije dovoljna.

### Vertikalna komponenta i njezin smjer

Za vertikalnu komponentu vrijedi

$$
F_V=\int_A p\,n_{f,z}\,dA.
$$ {#eq-sile-plohe-vertikalna-komponenta-i-njezin-smjer-01}

U otvorenom spremniku, s manometarskim tlakom jednakim nuli na slobodnoj površini, magnituda se može dobiti ravnotežom pomoćnog volumena $V^*$ omeđenog zakrivljenom plohom, okomitim bočnim plohama i vodoravnom zatvarajućom plohom:

$$
|F_V|=\rho gV^*.
$$ {#eq-u05-zakrivljena-vertikalna}

Pravac djelovanja prolazi težištem toga volumena. Formula daje **magnitudu**, ne automatski smjer. Smjer se određuje ovim redoslijedom:

1. označi stvarnu stranu na kojoj fluid dodiruje plohu;
2. nacrtaj lokalnu strelicu $p\mathbf n_f$ od fluida prema stijenci;
3. pročitaj predznak njezine vertikalne komponente.

Fluid iznad konkavne plohe tipično opterećuje plohu prema dolje. Fluid koji kvasi konveksnu donju stranu može djelovati prema gore. Položaj nacrtanog pomoćnog volumena sam po sebi nije kriterij smjera, jer taj volumen ne mora biti stvarni fluid.

Ako je tlak na vodoravnoj zatvarajućoj plohi različit od nule ili se ne poništava tlak s druge strane, njegov doprinos treba dodati predznačeno. U složenoj geometriji najsigurnija je kontrola izravnim integralom $\int p n_{f,z}\,dA$.

Nakon određivanja predznačenih komponenti,

$$
F_R=\sqrt{F_H^2+F_V^2},\qquad
\alpha=\operatorname{atan2}(F_V,F_H).
$$ {#eq-sile-plohe-vertikalna-komponenta-i-njezin-smjer-02}

Funkcija $\operatorname{atan2}$ zadržava kvadrant; obični $\arctan(F_V/F_H)$ može sakriti pogrešan predznak. Na kružnom luku u ravninskom presjeku sve lokalne tlačne sile prolaze središtem zakrivljenosti, pa kroz njega prolazi i rezultanta. To geometrijsko svojstvo ne vrijedi za proizvoljnu zakrivljenu plohu.

::: {.mf1-interaktivno}
<p class="mf1-box-label">Numerički pokus — zakrivljena ploha</p>

Prije pokretanja odredite smjer $F_V$ samo iz okupane strane. Zatim mijenjajte dubinu i polumjer te usporedite numerički rast $F_H$ i $F_V$ s njihovim geometrijskim izrazima.

<div class="mf1-interaktivno-akcija">
<a class="mf1-interaktivno-veza" href="https://martibasic.github.io/MF1_udzbenik/jlite/lab/index.html?path=u06_zakrivljena_ploha.ipynb">Pokreni u pregledniku</a>
<a class="mf1-interaktivno-veza" href="https://colab.research.google.com/github/martibasic/MF1_udzbenik/blob/main/notebooks/u06_zakrivljena_ploha.ipynb" target="_blank" rel="noopener">Pričuvno: otvori u Colabu</a>
<img class="mf1-interaktivno-qr" src="../assets/qr/u06_zakrivljena_ploha.svg" alt="QR kod za numerički pokus sile na zakrivljenu plohu"/>
</div>
:::

## Riješeni primjeri: zakrivljene plohe

::: {#ex-u05-potopljena-cetvrtina-kruga .mf1-we}
<p class="mf1-box-label">Riješeni primjer — Potopljena četvrtina kruga, sila prema gore <span class="mf1-level">T2</span></p>

Četvrtcilindrična ploha ima polumjer $R=1{,}22\ \mathrm{m}$, širinu $b=1{,}83\ \mathrm{m}$ i gornju točku na dubini $h_1=2{,}44\ \mathrm{m}$. Voda gustoće $998\ \mathrm{kg/m^3}$ kvasi konveksnu vanjsku i donju stranu plohe. Odredite komponente, pravce djelovanja i rezultantu.

![Potopljena četvrtcilindrična ploha s vodom na konveksnoj donjoj strani i vertikalnom silom prema gore](../assets/print/u06_val1_cetvrtina_kruga.svg){#fig-u05-potopljena-cetvrtcilindricna-ploha fig-align="center" fig-alt="Potopljena četvrtcilindrična ploha s vodom na konveksnoj donjoj strani i vertikalnom silom prema gore"}

**Pretpostavke.** Atmosferski tlak se poništava. Zakrivljena ploha je cilindrična, bez krajnjih učinaka. Pozitivni vertikalni smjer odabran je prema gore.

Vertikalna projekcija ima

$$
A_x=Rb=2{,}233\ \mathrm{m^2},\qquad
h_{Cx}=h_1+\frac R2=3{,}05\ \mathrm{m}.
$$ {#eq-sile-plohe-rijeseni-primjer-potopljena-cetvrtina-kruga-sila-01}

Zato je

$$
F_H=\rho gA_xh_{Cx}=66{,}67\ \mathrm{kN}.
$$ {#eq-sile-plohe-rijeseni-primjer-potopljena-cetvrtina-kruga-sila-02}

Za projekciju je $I_G=bR^3/12=0{,}277\ \mathrm{m^4}$, pa horizontalna komponenta djeluje na dubini

$$
h_H=h_{Cx}+\frac{I_G}{A_xh_{Cx}}=3{,}091\ \mathrm{m}.
$$ {#eq-sile-plohe-rijeseni-primjer-potopljena-cetvrtina-kruga-sila-03}

Pomoćni volumen sastoji se od pravokutnog i četvrtcilindričnog dijela:

$$
V^*=h_1Rb+\frac{\pi R^2}{4}b
=5{,}448+2{,}139=7{,}587\ \mathrm{m^3}.
$$ {#eq-sile-plohe-rijeseni-primjer-potopljena-cetvrtina-kruga-sila-04}

Magnituda vertikalne komponente je

$$
|F_V|=\rho gV^*=74{,}28\ \mathrm{kN}.
$$ {#eq-sile-plohe-rijeseni-primjer-potopljena-cetvrtina-kruga-sila-05}

Stvarna voda kvasi donju konveksnu stranu, pa lokalne tlačne strelice imaju vertikalnu komponentu prema gore: $F_V=+74{,}28\ \mathrm{kN}$. Vodoravni položaj pravca djelovanja dobiva se iz težišta složenog volumena,

$$
x_V=\frac{(h_1Rb)(R/2)+[(\pi R^2/4)b][4R/(3\pi)]}{V^*}
=0{,}584\ \mathrm{m}.
$$ {#eq-sile-plohe-rijeseni-primjer-potopljena-cetvrtina-kruga-sila-06}

Rezultanta je

$$
F_R=\sqrt{66{,}67^2+74{,}28^2}=99{,}81\ \mathrm{kN},
$$ {#eq-sile-plohe-rijeseni-primjer-potopljena-cetvrtina-kruga-sila-07}

pod kutom $48{,}1^\circ$ iznad horizontale.

**Neovisna provjera.** Rezultanta mora biti između veće komponente i njihova zbroja: $74{,}28<99{,}81<140{,}95\ \mathrm{kN}$. Smjer se dodatno provjerava jednom lokalnom normalom na donjoj okupanoj strani; ona ima pozitivnu vertikalnu komponentu neovisno o tome gdje je nacrtan $V^*$.
:::

::: {#ex-u05-cetvrtcilindar-prema-dolje .mf1-we}
<p class="mf1-box-label">Riješeni primjer — Četvrtcilindrični poklopac uz slobodnu površinu <span class="mf1-level">T2</span></p>

Poklopac širine $b=1{,}20\ \mathrm{m}$ i polumjera $R=0{,}90\ \mathrm{m}$ počinje na slobodnoj površini. Voda kvasi stranu na kojoj lokalne normale od fluida prema stijenci imaju vertikalne komponente prema dolje. Odredite komponente i rezultantu.

![Četvrtcilindrični poklopac uz slobodnu površinu s vertikalnom komponentom prema dolje](../assets/print/u06_val3_cetvrtcilindricni_poklopac.svg){#fig-u05-cetvrtcilindricni-poklopac-slobodna-povrsina fig-align="center" fig-alt="Četvrtcilindrični poklopac uz slobodnu površinu s vertikalnom komponentom prema dolje"}

**Pretpostavke.** Računa se neto manometarski tlak; ploha je kružni cilindrični luk, a tlak na slobodnoj površini je nula.

Za vertikalnu projekciju

$$
A_x=Rb=1{,}08\ \mathrm{m^2},\qquad h_{Cx}=R/2=0{,}45\ \mathrm{m},
$$ {#eq-sile-plohe-rijeseni-primjer-cetvrtcilindricni-poklopac-uz-s-01}

pa su

$$
F_H=\rho gA_xh_{Cx}=4{,}758\ \mathrm{kN},\qquad
h_H=\frac{2R}{3}=0{,}600\ \mathrm{m}.
$$ {#eq-sile-plohe-rijeseni-primjer-cetvrtcilindricni-poklopac-uz-s-02}

Pomoćni volumen je četvrtina valjka,

$$
V^*=\frac{\pi R^2}{4}b=0{,}7634\ \mathrm{m^3},
$$ {#eq-sile-plohe-rijeseni-primjer-cetvrtcilindricni-poklopac-uz-s-03}

zbog čega je

$$
F_V=-\rho gV^*=-7{,}474\ \mathrm{kN}.
$$ {#eq-sile-plohe-rijeseni-primjer-cetvrtcilindricni-poklopac-uz-s-04}

Negativan predznak označuje smjer prema dolje. Pravac djelovanja udaljen je od okomite stijenke

$$
x_V=\frac{4R}{3\pi}=0{,}382\ \mathrm{m}.
$$ {#eq-sile-plohe-rijeseni-primjer-cetvrtcilindricni-poklopac-uz-s-05}

Stoga je

$$
F_R=8{,}860\ \mathrm{kN},\qquad
\alpha=-57{,}52^\circ.
$$ {#eq-sile-plohe-rijeseni-primjer-cetvrtcilindricni-poklopac-uz-s-06}

**Neovisna provjera.** Izravna integracija po kružnom luku koji počinje na slobodnoj površini daje $F_H=\rho gbR^2/2$ i $|F_V|=\rho gb\pi R^2/4$. Zato mora vrijediti $|F_V|/F_H=\pi/2=1{,}571$; numerički je $7{,}474/4{,}758=1{,}571$.
:::

::: {#ex-u05-zglobni-cetvrtcilindricni-poklopac .mf1-we}
<p class="mf1-box-label">Riješeni primjer — Zglobni poklopac s vertikalnom silom prema gore <span class="mf1-level">T3</span></p>

Četvrtcilindrični poklopac širine $b=1{,}40\ \mathrm{m}$ i polumjera $R=1{,}10\ \mathrm{m}$ zglobno je vezan u gornjoj točki $A$ na slobodnoj površini. Donji rub pridržava vodoravna spojnica. Voda kvasi konveksnu donju i lijevu stranu. Odredite komponente i statičku silu spojnice.

![Zglobni četvrtcilindrični poklopac s vodom na donjoj strani, silom prema gore i vodoravnom spojnicom](../assets/print/u06_ch1_poklopac_spojnica.svg){#fig-u05-zglobni-cetvrtcilindricni-poklopac fig-align="center" fig-alt="Zglobni četvrtcilindrični poklopac s vodom na donjoj strani, silom prema gore i vodoravnom spojnicom"}

**Pretpostavke.** Voda miruje, atmosferski tlak se poništava, poklopac je krut, a njegova težina i trenje zgloba nisu uključeni. Pozitivni vertikalni smjer je prema gore.

Horizontalna komponenta i njezin krak prema zglobu jesu

$$
F_H=\rho g(Rb)\frac R2=8{,}292\ \mathrm{kN},\qquad
h_H=\frac{2R}{3}=0{,}733\ \mathrm{m}.
$$ {#eq-sile-plohe-rijeseni-primjer-zglobni-poklopac-s-vertikalnom-01}

Pomoćni volumen je

$$
V^*=\frac{\pi R^2}{4}b=1{,}3305\ \mathrm{m^3},
$$ {#eq-sile-plohe-rijeseni-primjer-zglobni-poklopac-s-vertikalnom-02}

pa je magnituda vertikalne komponente

$$
|F_V|=\rho gV^*=13{,}026\ \mathrm{kN}.
$$ {#eq-sile-plohe-rijeseni-primjer-zglobni-poklopac-s-vertikalnom-03}

Voda kvasi donju konveksnu stranu, stoga je $F_V$ **prema gore**. Njezin je vodoravni krak prema zglobu

$$
x_V=R-\frac{4R}{3\pi}=0{,}633\ \mathrm{m}.
$$ {#eq-sile-plohe-rijeseni-primjer-zglobni-poklopac-s-vertikalnom-04}

Rezultanta iznosi $F_R=15{,}441\ \mathrm{kN}$ i usmjerena je $57{,}52^\circ$ iznad horizontale. Za prikazane smjerove obje komponente daju moment otvaranja oko $A$. Ravnoteža momenata zato zahtijeva

$$
TR=F_Hh_H+F_Vx_V,
$$ {#eq-sile-plohe-rijeseni-primjer-zglobni-poklopac-s-vertikalnom-05}

odnosno

$$
T=\frac{8{,}292\cdot0{,}733+13{,}026\cdot0{,}633}{1{,}10}
=13{,}026\ \mathrm{kN}.
$$ {#eq-sile-plohe-rijeseni-primjer-zglobni-poklopac-s-vertikalnom-06}

**Neovisna provjera.** Za ovu posebnu geometriju

$$
F_Hh_H=\rho gbR^3/3,
$$ {#eq-sile-plohe-rijeseni-primjer-zglobni-poklopac-s-vertikalnom-07}

$$
F_Vx_V=\rho gbR^3\left(\frac\pi4-\frac13\right).
$$ {#eq-sile-plohe-rijeseni-primjer-zglobni-poklopac-s-vertikalnom-08}

Zbroj je $\rho gb\pi R^3/4=F_VR$, pa identitet daje $T=F_V=13{,}026\ \mathrm{kN}$. Jednakost je geometrijska provjera ovog slučaja, a ne opće pravilo za zakrivljene poklopce.
:::

## Konceptualna provjera

::: {.mf1-questions}
1. Može li se iznos sile na nagnutu plohu odrediti samo iz njezina kuta? Obrazložite koje se geometrijske veličine moraju držati jednakima pri usporedbi.
2. Zašto je centar tlaka vertikalne plohe u manometarskom polju dublji od težišta, ali se kod vodoravne plohe s njime podudara?
3. Zašto položaj zamišljenog volumena ne određuje smjer $F_V$?
4. U kojem slučaju jedna vertikalna projekcija nije dovoljna za račun $F_H$ zakrivljene plohe?
5. Koja bi se dodatna fizika morala uključiti kada je fluid u gibanju ili kada je druga strana poklopca pod nepoznatim tlakom?
:::

## Zadaci za samostalan rad

U svim zadatcima uzmite $g=9{,}81\ \mathrm{m/s^2}$. Ako nije drukčije navedeno, voda ima $\rho=998\ \mathrm{kg/m^3}$, atmosfera djeluje s obje strane gdje je prisutna i računa se neto manometarski tlak. Skica s okupanom stranom, normalom i pozitivnim smjerovima dio je postavljanja modela.

::::: {.mf1-vjezbe-list}
1. [**T1**]{#task-u05-ravna-pravokutna-zaklopka} Vertikalni pravokutni poklopac širine $b=1{,}40\ \mathrm{m}$ i visine $H=1{,}80\ \mathrm{m}$ nalazi se u vodi tako da mu je gornji rub na dubini $h_1=1{,}10\ \mathrm{m}$. Odredite rezultantnu silu, dubinu centra tlaka i njegovu udaljenost od gornjeg ruba.

   :::: {.content-visible when-format="html"}
   :::: {.content-visible .mf1-hint-online when-format="html"}
   ::: {.callout-note collapse="true" data-hint-key="true"}
   ### Naputak
   Najprije izračunajte $A$ i $h_C$. Za centar tlaka treba $I_G=bH^3/12$.
   :::
   ::::
   ::::

   :::: {.content-visible .mf1-answer-online when-format="html"}
   ::: {.callout-tip collapse="true" data-answer-key="true"}
   ### Kontrolni rezultat

   $F=49{,}34\ \mathrm{kN}$; $h_{CP}=2{,}135\ \mathrm{m}$; udaljenost od gornjeg ruba $1{,}035\ \mathrm{m}$.
   :::
   ::::

2. [**T1**]{#task-u05-zakrivljeni-poklopac-cetvrtine-kruga} Zakrivljeni poklopac presjeka četvrtine kruga ima $R=0{,}65\ \mathrm{m}$ i širinu $b=1{,}20\ \mathrm{m}$. Gornja mu je točka na dubini $h_1=1{,}10\ \mathrm{m}$. Voda kvasi konveksnu vanjsku i donju stranu. Odredite $F_H$, predznačeni $F_V$ i $F_R$.

   :::: {.content-visible when-format="html"}
   :::: {.content-visible .mf1-hint-online when-format="html"}
   ::: {.callout-note collapse="true" data-hint-key="true"}
   ### Naputak
   Za $F_H$ rabite vertikalnu projekciju $Rb$ na dubini $h_1+R/2$. Pomoćni volumen čine pravokutni dio $h_1Rb$ i četvrtina valjka.
   :::
   ::::
   ::::

   :::: {.content-visible .mf1-answer-online when-format="html"}
   ::: {.callout-tip collapse="true" data-answer-key="true"}
   ### Kontrolni rezultat

   $F_H=10{,}88\ \mathrm{kN}$; $F_V=+12{,}30\ \mathrm{kN}$ prema gore; $F_R=16{,}42\ \mathrm{kN}$.
   :::
   ::::

3. [**T2**]{#task-u05-kosi-poklopac-sa-zglobom} Kosi pravokutni poklopac širine $b=0{,}80\ \mathrm{m}$ i duljine $L=1{,}00\ \mathrm{m}$ zatvara kut $\theta=40^\circ$ prema vodoravnici. Gornji rub na dubini je $h_1=0{,}90\ \mathrm{m}$ i spojen je zglobom. Na donjem rubu djeluje sila držanja okomita na plohu. Odredite rezultantu, položaj centra tlaka od zgloba i silu držanja.

   :::: {.content-visible when-format="html"}
   :::: {.content-visible .mf1-hint-online when-format="html"}
   ::: {.callout-note collapse="true" data-hint-key="true"}
   ### Naputak
   Postavite $h(s)=h_1+s\sin\theta$ i uporabite omjer prvog momenta sile i ukupne sile. Zatim zatvorite moment oko zgloba.
   :::
   ::::
   ::::

   :::: {.content-visible .mf1-answer-online when-format="html"}
   ::: {.callout-tip collapse="true" data-answer-key="true"}
   ### Kontrolni rezultat

   $F=9{,}566\ \mathrm{kN}$; $s_{CP}=0{,}5439\ \mathrm{m}$; $T=5{,}203\ \mathrm{kN}$.
   :::
   ::::

4. [**T2**]{#task-u05-dvoslojna-vertikalna-stijena} Vertikalna stijena širine $b=1{,}80\ \mathrm{m}$ zadržava gornji sloj ulja gustoće $820\ \mathrm{kg/m^3}$ i visine $0{,}90\ \mathrm{m}$ te donji sloj vode gustoće $998\ \mathrm{kg/m^3}$ i visine $1{,}50\ \mathrm{m}$. Slobodna površina ulja je na atmosferi. Odredite ukupnu silu i dubinu njezina hvatišta od slobodne površine.

   :::: {.content-visible when-format="html"}
   :::: {.content-visible .mf1-hint-online when-format="html"}
   ::: {.callout-note collapse="true" data-hint-key="true"}
   ### Naputak
   Dijagram tlaka rastavite na uljni trokut, pravokutni doprinos uljnog stupca u vodi i vodeni trokut. Svaki dio ima svoje hvatište.
   :::
   ::::
   ::::

   :::: {.content-visible .mf1-answer-online when-format="html"}
   ::: {.callout-tip collapse="true" data-answer-key="true"}
   ### Kontrolni rezultat

   $F=45{,}24\ \mathrm{kN}$; $h_{CP}=1{,}623\ \mathrm{m}$.
   :::
   ::::

5. [**T3**]{#task-u05-zglobni-zakrivljeni-poklopac-model} Četvrtcilindrični poklopac ima $R=0{,}75\ \mathrm{m}$, $b=1{,}10\ \mathrm{m}$ i gornju točku na dubini $h_1=0{,}45\ \mathrm{m}$. Voda kvasi konkavnu stranu odozgo, pa lokalne normale imaju vertikalnu komponentu prema dolje. Poklopac je zglobno vezan u gornjoj točki, a donji rub pridržava vodoravna spojnica. Sami odaberite potreban skup modela te odredite $F_H$, pravac $F_H$, $F_V$, $F_R$ i silu spojnice.

   :::: {.content-visible when-format="html"}
   :::: {.content-visible .mf1-hint-online when-format="html"}
   ::: {.callout-note collapse="true" data-hint-key="true"}
   ### Naputak
   $F_H$ dolazi iz vertikalne projekcije. Za $F_V$ pomoćni volumen ima pravokutni dio i četvrtinu valjka. U momentu oko zgloba rabite zasebne krakove obiju komponenti.
   :::
   ::::
   ::::

   :::: {.content-visible .mf1-answer-online when-format="html"}
   ::: {.callout-tip collapse="true" data-answer-key="true"}
   ### Kontrolni rezultat

   $F_H=6{,}664\ \mathrm{kN}$; $h_H=0{,}8818\ \mathrm{m}$ ispod slobodne površine, odnosno krak $0{,}4318\ \mathrm{m}$ prema zglobu; $F_V=8{,}392\ \mathrm{kN}$ prema dolje s krakom $0{,}4071\ \mathrm{m}$; $F_R=10{,}72\ \mathrm{kN}$; $T=8{,}392\ \mathrm{kN}$.
   :::
   ::::

6. [**T4**]{#task-u05-nesigurnost-modela-i-mjerenja} Pravokutni mjerni panel ima točno poznate dimenzije $b=1{,}20\ \mathrm{m}$ i $H=0{,}80\ \mathrm{m}$. Gornji rub je na izmjerenoj dubini $h_1=0{,}90\ \mathrm{m}$ sa standardnom nesigurnošću $u(h_1)=0{,}020\ \mathrm{m}$, a gustoća je $\rho=998\ \mathrm{kg/m^3}$ uz $u(\rho)=3\ \mathrm{kg/m^3}$. Neovisna mjerna ćelija daje $F_m=11{,}60\ \mathrm{kN}$ uz $u(F_m)=0{,}30\ \mathrm{kN}$. Pretpostavite nezavisne ulaze i primijenite linearnu propagaciju nesigurnosti. Izračunajte predviđanje $F$, njegovu standardnu nesigurnost i normirano odstupanje $z=|F-F_m|/\sqrt{u(F)^2+u(F_m)^2}$. Obrazložite podržavaju li podaci tvrdnju o neslaganju na razini $2u$.

   :::: {.content-visible when-format="html"}
   :::: {.content-visible .mf1-hint-online when-format="html"}
   ::: {.callout-note collapse="true" data-hint-key="true"}
   ### Naputak
   Za $F=\rho gbH(h_1+H/2)$ relativna nesigurnost zbog dvaju nesigurnih ulaza jest $u(F)/F=\sqrt{[u(\rho)/\rho]^2+[u(h_1)/(h_1+H/2)]^2}$.
   :::
   ::::
   ::::

   :::: {.content-visible .mf1-answer-online when-format="html"}
   ::: {.callout-tip collapse="true" data-answer-key="true"}
   ### Kontrolni rezultat

   $F=12{,}218\ \mathrm{kN}$; $u(F)=0{,}192\ \mathrm{kN}$; kombinirana nesigurnost razlike $0{,}356\ \mathrm{kN}$; $z=1{,}74$. Budući da je $z<2$, ovaj skup podataka ne pokazuje neslaganje na zadanoj razini, ali time model nije općenito validiran.
   :::
   ::::
:::::

## Za ponijeti

::: {.mf1-zavrsni-okvir}
<p class="mf1-box-label">Sažetak modela i njegovih granica</p>

- Za ravnu plohu prvo integrirajte neto tlak: pri $p=\rho gh$ vrijedi $F=\rho gAh_C$.
- Centar tlaka dolazi iz momenta **iste** raspodjele. Formula $h_C+I_G/(Ah_C)$ nije opća za nenulti jednoliki dodatak tlaka.
- Kut nagnute plohe ovdje je kut prema vodoravnici; geometrija dubina ulazi preko $\sin\theta$.
- Za zakrivljenu plohu $F_H$ se dobiva iz sile na vertikalnu projekciju, a $|F_V|$ iz težine odgovarajućega pomoćnog volumena kada su ispunjene pretpostavke otvorenog manometarskog slučaja.
- Smjer $F_V$ određuje stvarna okupana strana i normala $\mathbf n_f$. Vertikalna komponenta može biti prema gore ili prema dolje.
- Hidrostatički račun ne uključuje strujne udare, valove, inerciju poklopca, deformaciju, zamor, brtvljenje ni normativnu provjeru konstrukcije.
:::
