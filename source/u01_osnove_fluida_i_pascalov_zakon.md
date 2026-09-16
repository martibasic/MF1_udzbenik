![Pregled poglavlja: fizikalni sustav (Pascalov zakon s dva klipa), ključna jednadžba p = F₁/A₁ = F₂/A₂ i primjena u praksi (hidraulična dizalica)](../assets/print/u01_fig_uvod_pregled.svg){#fig-uvod-u01 fig-align="center" fig-alt="Pregled poglavlja: fizikalni sustav (Pascalov zakon s dva klipa), ključna jednadžba p = F₁/A₁ = F₂/A₂ i primjena u praksi (hidraulična dizalica)"}

## Fluid kao kontinuum

Mehanika fluida polazi od pojma fluida, kontinuumskog modela te veličina kojima se fluid opisuje. Gustoća, tlak i Pascalov zakon čine osnovu za analizu hidrostatskih i strujnih pojava te za proračun hidrauličnih sustava.

::: {.mf1-application}
<p class="mf1-box-label">Inženjerski kontekst</p>

Hidraulične dizalice, preše za oblikovanje lima i brodski kormilarski pogoni temelje se na prijenosu tlaka zatvorenim fluidom. U takvim sustavima tlak povezuje ulaznu silu, geometriju cilindara i radnu silu aktuatora.
:::

**Procijenjeno vrijeme rada uz udžbenik:** 8 sati.

### Kontinuumski model

Fluid je tvar koja se pri djelovanju bilo kojega, pa i vrlo malog, tangencijalnog naprezanja neprekidno deformira. U inženjerskoj se analizi njegova molekularna građa obično ne promatra izravno. Umjesto toga primjenjuje se kontinuumski model, prema kojem su veličine kao što su gustoća, tlak i brzina definirane u svakoj točki prostora i vremenu.

Polja $p(x,y,z)$ i $\rho(x,y,z)$ matematički opisuju prostornu raspodjelu tlaka i gustoće te omogućuju određivanje sila i gibanja fluida na razini prikladnoj za tehnički proračun.

### Tlak

Za jednoliko raspodijeljen tlak na ravnoj plohi tlačna sila $F_n$ i površina $A$ povezane su izrazom:

$$
p = \frac{F_n}{A}
$$ {#eq-svojstva-tlak-fizikalni-uvod-i-matematicki-izvod-01}

Ako tlak po plohi nije jednolik, omjer $F_n/A$ daje srednji tlak. Lokalno se tlak definira kao $p=dF_n/dA$, a rezultantna sila dobiva integriranjem po plohi.

Tlak nije sila, nego normalna sila po jedinici površine. Ista normalna sila raspodijeljena na veću površinu daje manji tlak. U fluidu u mirovanju nema tangencijalnih naprezanja, a tlak u pojedinoj točki djeluje jednako u svim smjerovima. Tlak je stoga skalarna veličina.

U zatvorenom fluidu u mirovanju nametnuta se promjena tlaka prenosi jednako u svim smjerovima. To je temelj Pascalova zakona i rada hidrauličnih sustava, u kojima mala sila na klipu manje površine može proizvesti veću silu na klipu veće površine.

## Osnovne veličine

Gustoća, specifična težina i relativna gustoća različite su fizikalne veličine:

$$
\rho = \frac{m}{V}
$$ {#eq-svojstva-tlak-osnovne-velicine-koje-se-najcesce-mijesaju-01}

$$
\gamma = \rho g
$$ {#eq-svojstva-tlak-osnovne-velicine-koje-se-najcesce-mijesaju-02}

$$
s_r = \frac{\rho}{\rho_{voda}}
$$ {#eq-svojstva-tlak-osnovne-velicine-koje-se-najcesce-mijesaju-03}

Gustoća $\rho$ jest masa po jedinici volumena. Specifična težina $\gamma = \rho g$ jest težinska sila po jedinici volumena u zadanome gravitacijskom polju. Relativna gustoća $s_r$ bezdimenzijski je omjer gustoće fluida i referentne gustoće vode. Primjerice, vrijednost $s_r=0{,}86$ za ulje pokazuje da je njegova gustoća manja od gustoće vode, dok je za živu $s_r\approx13{,}6$.

Izraz $\rho=m/V$ daje gustoću homogenog fluida, odnosno srednju gustoću promatranog volumena. Kada se gustoća mijenja s položajem, lokalno pišemo $\rho=dm/dV$. Referentna gustoća vode u omjeru $s_r$ određuje se pri zadanoj temperaturi; u zadatcima se često usvaja približna vrijednost $1000\ \text{kg/m}^3$.

::: {#ex-u01-gustoca-specificna-tezina-i-relativna-gustoca-ulja .mf1-we}
<p class="mf1-box-label">P1. Gustoća, specifična težina i relativna gustoća ulja&nbsp;<span class="mf1-level">T1</span></p>

**Kontekst:** Hidraulično ulje koristi se kao radni medij u hidrauličnim sustavima. Za odabir komponenti i provjeru uzgona potrebno je razlikovati gustoću, specifičnu težinu i relativnu gustoću tog ulja.

**Zadano**

- Gustoća hidrauličnog ulja: $\rho = 860\ \text{kg/m}^3$

**Traženo**

1. specifičnu težinu $\gamma$.
2. relativnu gustoću $s_r$.

![Gustoća, specifična težina i relativna gustoća ulja (ρ = 860 kg/m³) u usporedbi s vodom (ρ = 1000 kg/m³)](../assets/print/u01_fig_gustoca_sr.svg){#fig-u01-gustoca-sr fig-align="center" fig-alt="Gustoća, specifična težina i relativna gustoća ulja (ρ = 860 kg/m³) u usporedbi s vodom (ρ = 1000 kg/m³)"}

**Pretpostavke i model**

Usvaja se

$$
g = 9{,}81\ \text{m/s}^2
$$ {#eq-svojstva-tlak-kratki-primjer-gustoca-specificna-tezina-i-relat-01}

i referentnu gustoću vode

$$
\rho_{voda} = 1000\ \text{kg/m}^3.
$$ {#eq-svojstva-tlak-kratki-primjer-gustoca-specificna-tezina-i-relat-02}

**Rješenje**

Specifična težina ulja iznosi

$$
\gamma = \rho g = 860 \cdot 9{,}81 = 8437\ \text{N/m}^3\approx 8{,}44\ \text{kN/m}^3.
$$ {#eq-svojstva-tlak-kratki-primjer-gustoca-specificna-tezina-i-relat-03}

Relativna gustoća dobiva se omjerom prema vodi:

$$
s_r = \frac{\rho}{\rho_{voda}} = \frac{860}{1000} = 0{,}86.
$$ {#eq-svojstva-tlak-kratki-primjer-gustoca-specificna-tezina-i-relat-04}

**Tumačenje rezultata**

Relativna gustoća je bezdimenzijska veličina, a specifična težina ima jedinicu sile po volumenu. Razlikovanje $\rho$, $\gamma$ i $s_r$ nužno je pri proračunu hidrostatskoga tlaka i uzgona.
:::

::: {.mf1-numerika .kompakt}
<p class="mf1-box-label">Kako računalo pomaže pri proračunu strujanja</p>

Računalo može procijeniti brzinu i tlak i ondje gdje je ručni račun previše složen, primjerice unutar cijevnog koljena ili između lopatica crpke. Pritom koristi iste zakone očuvanja mase, količine gibanja i energije koje učimo u ovom udžbeniku. Takav pristup naziva se **računalna dinamika fluida (CFD)**.

Kratke napomene uz jednadžbe objašnjavaju tu vezu na primjerima. Završni osvrti povezuju poglavlja sa složenijim proračunima. To je dodatno čitanje za znatiželjne; za osnovno gradivo nije potrebno poznavati računalne postupke.
:::

## Pascalov zakon

Pascalov zakon navodi da se promjena tlaka nametnuta zatvorenom fluidu u mirovanju prenosi neumanjena na sve dijelove fluida i na stijenke spremnika. Pri primjeni na sustav s dva klipa pretpostavljaju se kvazistatičko stanje, približno jednake visine klipova te zanemarivi gubici i stlačivost. Ako klipovi nisu na istoj visini, u analizu se uključuje hidrostatska razlika tlaka. U navedenim uvjetima vrijedi

$$
\Delta p = \frac{F_1}{A_1} = \frac{F_2}{A_2}
$$ {#eq-svojstva-tlak-pascalov-zakon-kao-prvi-inzenjerski-alat-01}

odnosno

$$
F_2 = F_1 \frac{A_2}{A_1}
$$ {#eq-svojstva-tlak-pascalov-zakon-kao-prvi-inzenjerski-alat-02}

Pascalov zakon ne podrazumijeva stvaranje energije, nego promjenu omjera sile i pomaka. Isti porast tlaka koji mali klip unosi u fluid na većoj površini daje veću ukupnu silu. Omjer $A_2/A_1=35$ daje 35 puta veću izlaznu silu, ali i 35 puta manji izlazni pomak; u idealiziranom sustavu rad ulaza jednak je radu izlaza.

::: {.mf1-interaktivno}
<p class="mf1-box-label">Interaktivni prikaz — Hidraulična preša</p>

Interaktivni prikaz omogućuje promjenu promjera ulaznog i izlaznog klipa te ulazne sile, uz prikaz izlazne sile i omjera pomaka klipova. Prikaz povezuje pojačanje sile sa smanjenjem pomaka koje proizlazi iz očuvanja istisnutoga volumena.

<div class="mf1-interaktivno-akcija">
<a class="mf1-interaktivno-veza" href="https://martibasic.github.io/MF1_udzbenik/jlite/lab/index.html?path=u01_hidraulicna_presa.ipynb">Pokreni u pregledniku</a>
<a class="mf1-interaktivno-veza" href="https://colab.research.google.com/github/martibasic/MF1_udzbenik/blob/main/notebooks/u01_hidraulicna_presa.ipynb" target="_blank" rel="noopener">Pričuvno: otvori u Colabu</a>
<img class="mf1-interaktivno-qr" src="../assets/qr/u01_hidraulicna_presa.svg" alt="QR kod za interaktivni prikaz hidraulične preše"/>
</div>

:::

Povećanje sile ne znači povećanje rada. Uz zanemarive gubitke i stlačivost istisnuti volumen ostaje jednak, pa vrijedi

$$
A_1 s_1 = A_2 s_2
$$ {#eq-svojstva-tlak-interaktivni-prikaz-hidraulicna-presa-01}

Jednakost je posljedica nestlačivosti fluida: volumen koji jedan klip istisne jednak je volumenu kojim se pomiče drugi klip. Manji klip zato mora prijeći dulji put. Sustav s omjerom površina 35 zahtijeva da mali klip prijeđe 35 puta dulji put od radnog klipa. Volumna bilanca ne ovisi o razini tlaka, nego o pretpostavci nestlačivosti fluida.

Veća izlazna sila zato dolazi uz manji izlazni pomak.

U osnovnom hidrauličnom prijenosu tlak se promatra u zatvorenom fluidu u mirovanju, pri čemu se zanemaruje razlika visina. Sustavi čije se radne točke nalaze na različitim visinama analiziraju se zajedno s hidrostatskom raspodjelom tlaka, obrađenom u <span class="mf1-ch-ref"><span class="mf1-ch-code">pog. 3</span><span class="mf1-ch-title">Hidrostatička raspodjela tlaka i manometrija</span></span>.

::: {.mf1-izvod}
<p class="mf1-box-label">Matematički izvod — Pascalov zakon i očuvanje rada</p>

Neka na mali klip površine $A_1$ djeluje dodatna sila $F_1$. Dodatni tlak koji ta sila stvara u zatvorenom mirujućem fluidu definira se relacijom

$$
\Delta p = \frac{F_1}{A_1}.
$$ {#eq-svojstva-tlak-matematicki-izvod-pascalov-zakon-i-ocuvanje-rada-01}

U mirujućem fluidu taj dodatni tlak ne prenosi se kao smična sila, nego kao porast normalnog naprezanja koji se kroz istu povezanu tekućinu očituje jednako u svim smjerovima. Zato na velikom klipu površine $A_2$ vrijedi isti porast tlaka,

$$
\Delta p = \frac{F_2}{A_2}.
$$ {#eq-svojstva-tlak-matematicki-izvod-pascalov-zakon-i-ocuvanje-rada-02}

Izjednačavanjem dvaju izraza dobiva se temeljni omjer hidrauličnoga sustava

$$
\frac{F_1}{A_1} = \frac{F_2}{A_2}
\qquad \Longrightarrow \qquad
F_2 = F_1 \frac{A_2}{A_1}.
$$ {#eq-svojstva-tlak-matematicki-izvod-pascalov-zakon-i-ocuvanje-rada-03}

U izrazu je $F_1$ ulazna sila, $A_1$ površina ulaznog klipa, $F_2$ izlazna radna sila, a $A_2$ površina izlaznog klipa. Povećanje sile ne znači stvaranje rada. Za nestlačiv fluid istisnuti je volumen jednak na oba klipa, pa vrijedi

$$
\Delta V_1 = \Delta V_2
\qquad \Longrightarrow \qquad
A_1 s_1 = A_2 s_2.
$$ {#eq-svojstva-tlak-matematicki-izvod-pascalov-zakon-i-ocuvanje-rada-04}

Uvrštavanjem odnosa sila i hodova slijedi i radna bilanca

$$
F_1 s_1 = F_2 s_2,
$$ {#eq-svojstva-tlak-matematicki-izvod-pascalov-zakon-i-ocuvanje-rada-05}

Iz volumne bilance slijedi $s_2 = s_1 \dfrac{A_1}{A_2}$. Uvrštavanjem u izraz za izlazni rad dobiva se
$$
F_2 s_2 = F_1 \frac{A_2}{A_1} \cdot s_1 \frac{A_1}{A_2} = F_1 s_1.
$$ {#eq-svojstva-tlak-razrada-koraka-01}

Omjeri površina međusobno se poništavaju, pa jednakost radova vrijedi za svaki omjer površina klipova u idealiziranom sustavu.

Hidraulični sustav stoga mijenja omjer sile i pomaka djelovanjem istoga porasta tlaka na različitim površinama, bez stvaranja mehaničke energije.
:::

::: {.mf1-dublje}
<p class="mf1-box-label">Izotropnost tlaka: Cauchyjev tetraedar</p>

Tvrdnja da u mirujućem fluidu tlak u jednoj točki djeluje jednako u svim smjerovima može se izvesti formalno iz ravnoteže sila na infinitezimalnom **trodimenzijskom tetraedru** s tri okomite plohe duž koordinatnih osi i jednom kosom plohom proizvoljne orijentacije s jediničnim vektorom normale $\vec{n} = (n_x, n_y, n_z)$.

Neka su pripadne površine $A_x$, $A_y$, $A_z$ (okomite na osi) i $A_n$ (kosa). Ako je tetraedar odabran tako da su komponente normale nenegativne, iz geometrije projekcija slijedi:

$$
A_x = n_x A_n, \qquad A_y = n_y A_n, \qquad A_z = n_z A_n.
$$ {#eq-svojstva-tlak-dublje-izotropnost-tlaka-cauchyjev-tetraedar-01}

Za proizvoljnu orijentaciju geometrijske površine projekcija se piše s $|n_i|$, dok se predznak čuva u vektoru normale i jednadžbi sila. Ovdje odabrani prvi oktant samo pojednostavnjuje zapis i ne ograničava zaključak.

Na svaku plohu djeluje normalna tlačna sila — neka su odgovarajući tlakovi $p_x$, $p_y$, $p_z$ na koordinatnim plohama i $p_n$ na kosoj plohi. Ravnoteža sila po osi $x$ (zanemarujući težinu jer ona ima dimenziju volumena $\propto \ell^3$ koja iščezava brže od površina $\propto \ell^2$ kada $\ell \to 0$):

$$
p_x A_x - p_n A_n n_x = 0,
$$ {#eq-svojstva-tlak-dublje-izotropnost-tlaka-cauchyjev-tetraedar-02}

odakle slijedi $p_x = p_n$. Analogno za osi $y$ i $z$ daje $p_y = p_n$ i $p_z = p_n$. Time se izvodi

$$
p_x = p_y = p_z = p_n,
$$ {#eq-svojstva-tlak-dublje-izotropnost-tlaka-cauchyjev-tetraedar-03}

što znači da je tlak u jednoj točki mirujućeg fluida **neovisan o orijentaciji plohe** na kojoj se mjeri. Tlak je dakle skalarna veličina, što opravdava njegov zapis kao polje $p(x, y, z)$ koje će se koristiti u svim daljnjim poglavljima. I u fluidu koji se giba tlak ostaje skalarni, izotropni dio tenzora naprezanja; ukupno naprezanje tada uz tlak sadrži i viskozni, devijatorski dio, pa ukupna kontaktna sila općenito nije samo normalna na plohu.
:::

::: {.mf1-numerika .kompakt}
<p class="mf1-box-label">Kako računalo povezuje tlak i protok</p>

Kada pritisnemo klip hidraulične preše, promjena tlaka širi se kroz ulje velikom, ali konačnom brzinom. U sporom radu preše to je širenje mnogo brže od pomicanja klipa, pa ga u proračunu obično ne pratimo zasebno. Ulje tada promatramo kao nestlačivo: volumen koji jedan klip potisne mora se pojaviti drugdje u sustavu.

Računalo usklađuje tlakove i brzine tako da se ta bilanca zadovolji u cijelom sustavu. Time se pojednostavljuje račun. Ne tvrdi se da se tlak u stvarnom ulju prenosi trenutačno.
:::

## Riješeni primjeri

::: {#ex-u01-optereceni-klip-i-tlak-u-zatvorenom-cilindru .mf1-we}
<p class="mf1-box-label">P2. Opterećeni klip i tlak u zatvorenom cilindru&nbsp;<span class="mf1-level">T2</span></p>

**Kontekst:** U hidrauličnom cilindru kružni klip zatvara ulje, a vlastita težina i dodatni teret stvaraju tlak koji se Pascalovim zakonom prenosi na drugi radni klip veće površine.

**Zadano**

- Promjer kružnog klipa: $d_k = 160\ \text{mm}$
- Ukupna sila opterećenja na klipu: $G = 3{,}60\ \text{kN}$
- Površina drugog radnog klipa: $A_2 = 450\ \text{cm}^2$

**Traženo**

1. površinu klipa $A_k$.
2. manometarski tlak u ulju neposredno ispod klipa.
3. silu na radnom klipu površine $A_2$.

![opterećeni klip i tlak u zatvorenom cilindru](../assets/print/u01_val1_klip_manometar.svg){#fig-u01-optereceni-klip-i-tlak-u-zatvorenom-cilindru fig-alt="opterećeni klip i tlak u zatvorenom cilindru"}

**Pretpostavke i model**

Na istoj razini mirujućeg ulja tlak se čita izravno iz odnosa sile i površine. Tek nakon što se odredi tlak pod opterećenim klipom, isti se tlak smije prenijeti na drugi klip i pretvoriti u novu silu.

**Rješenje**

Površina klipa iznosi

$$
A_k = \frac{\pi d_k^2}{4} = \frac{\pi \cdot 0{,}16^2}{4} = 2{,}01 \cdot 10^{-2}\ \text{m}^2 \approx 0{,}0201\ \text{m}^2.
$$ {#eq-svojstva-tlak-rijeseni-primjer-optereceni-klip-i-tlak-u-01}

Manometarski tlak neposredno ispod klipa dobiva se iz definicije tlaka:

$$
p = \frac{G}{A_k} = \frac{3600}{0{,}0201} = 1{,}79 \cdot 10^5\ \text{Pa} \approx 179\ \text{kPa}.
$$ {#eq-svojstva-tlak-rijeseni-primjer-optereceni-klip-i-tlak-u-02}

Površina radnog klipa u SI jedinicama iznosi

$$
A_2 = 450 \cdot 10^{-4} = 0{,}0450\ \text{m}^2.
$$ {#eq-svojstva-tlak-rijeseni-primjer-optereceni-klip-i-tlak-u-03}

Sila na radnom klipu zato je

$$
F_2 = pA_2 = 1{,}79 \cdot 10^5 \cdot 0{,}0450 = 8{,}06 \cdot 10^3\ \text{N} \approx 8{,}06\ \text{kN}.
$$ {#eq-svojstva-tlak-rijeseni-primjer-optereceni-klip-i-tlak-u-04}

**Tumačenje rezultata**

Veća ukupna sila na istom klipu daje veći tlak u ulju. Pri istome tlaku veća površina radnog klipa daje veću silu. Povećanje izlazne sile posljedica je većega presjeka klipa, a ne povećanja mehaničkog rada.
:::

::: {#ex-u01-servisna-hidraulicna-dizalica-t2 .mf1-we}
<p class="mf1-box-label">P3. Servisna hidraulična dizalica&nbsp;<span class="mf1-level">T2</span></p>

**Kontekst:** U radioničkoj hidrauličnoj dizalici mali upravljački klip prenosi tlak na veliki radni klip koji podiže teret. Treba odrediti tlak, izlaznu silu i izlazni pomak.

**Zadano**

- Površina malog upravljačkog klipa: $A_1 = 6\ \text{cm}^2$
- Površina velikog radnog klipa: $A_2 = 210\ \text{cm}^2$
- Sila na malom klipu: $F_1 = 150\ \text{N}$
- Pomak malog klipa: $s_1 = 18\ \text{cm}$

**Traženo**

1. tlak koji se prenosi kroz ulje.
2. silu na velikom klipu.
3. pomak velikog klipa.

Gubici i stlačivost ulja zanemaruju se.

![servisna hidraulična dizalica](../assets/print/u01_val2_hidraulicna_dizalica.svg){#fig-u01-servisna-hidraulicna-dizalica fig-alt="servisna hidraulična dizalica"}

**Pretpostavke i model**

Promatra se fluid u mirovanju u zatvorenom hidrauličnom sustavu. Tlak se određuje iz sile i površine maloga klipa, na drugome se klipu pretvara u silu, a pomak se određuje iz jednakosti istisnutoga volumena.

**Rješenje**

Površina malog klipa u kvadratnim metrima iznosi

$$
A_1 = 6 \cdot 10^{-4}\ \text{m}^2.
$$ {#eq-svojstva-tlak-rijeseni-primjer-servisna-hidraulicna-dizalica-t-01}

Zato je tlak u ulju

$$
p = \frac{F_1}{A_1} = \frac{150}{6 \cdot 10^{-4}} = 2{,}50 \cdot 10^5\ \text{Pa} = 250\ \text{kPa}.
$$ {#eq-svojstva-tlak-rijeseni-primjer-servisna-hidraulicna-dizalica-t-02}

Površina velikog klipa iznosi

$$
A_2 = 210 \cdot 10^{-4} = 2{,}10 \cdot 10^{-2}\ \text{m}^2.
$$ {#eq-svojstva-tlak-rijeseni-primjer-servisna-hidraulicna-dizalica-t-03}

pa je sila na velikom klipu

$$
F_2 = pA_2 = 2{,}50 \cdot 10^5 \cdot 2{,}10 \cdot 10^{-2} = 5250\ \text{N} = 5{,}25\ \text{kN}.
$$ {#eq-svojstva-tlak-rijeseni-primjer-servisna-hidraulicna-dizalica-t-04}

Za pomake koristimo jednakost istisnutog volumena:

$$
A_1 s_1 = A_2 s_2
$$ {#eq-svojstva-tlak-rijeseni-primjer-servisna-hidraulicna-dizalica-t-05}

odakle slijedi

$$
s_2 = \frac{A_1}{A_2} s_1 = \frac{6}{210} \cdot 18\ \text{cm} = 0{,}514\ \text{cm} \approx 5{,}1\ \text{mm}.
$$ {#eq-svojstva-tlak-rijeseni-primjer-servisna-hidraulicna-dizalica-t-06}

**Tumačenje rezultata**

Kako je $A_2/A_1=35$, izlazna sila 35 je puta veća, a izlazni pomak 35 puta manji od pripadnih ulaznih veličina. Istodobno veliko povećanje sile i pomaka bilo bi protivno volumnoj bilanci i očuvanju rada.
:::

::: {#ex-u01-dvostruka-hidraulicna-platforma-s-rucnom-pumpom-t3 .mf1-ch}
<p class="mf1-box-label">P4. Dvostruka hidraulična platforma s ručnom pumpom&nbsp;<span class="mf1-level">T3</span></p>

**Kontekst:** U autoservisnoj radionici servisna platforma za pregled vozila oslanja se na dva paralelna radna cilindra, dok operater ručnom pumpom razvija tlak u hidrauličnom ulju. Treba odrediti idealizirani tlak i podiznu silu te ukupan hod i broj poteza pumpe za podizanje na zadanu visinu.

**Zadano**

- Površina jednog radnog cilindra: $A_L = 150\ \text{cm}^2$ (dva jednaka cilindra)
- Površina pumpnog klipa: $A_p = 5\ \text{cm}^2$
- Sila operatera na pumpni klip: $F_p = 460\ \text{N}$
- Visina podizanja platforme: $s_L = 25\ \text{mm}$
- Puni hod pumpnog klipa: $s_h = 180\ \text{mm}$

Gubici i stlačivost ulja zanemaruju se, a oba se radna cilindra smatraju jednako opterećenima.

**Traženo**

1. tlak $p$ u ulju.
2. silu jednoga radnog cilindra i ukupnu idealiziranu podiznu silu $G$.
3. ukupni zbroj hodova pumpnog klipa potreban da se platforma podigne za $s_L$.
4. najmanji broj punih pumpnih hodova potreban za taj podizaj.

![dvostruka hidraulična platforma s ručnom pumpom](../assets/print/u01_ch1_dvostruka_platforma_manometar.svg){#fig-u01-dvostruka-hidraulicna-platforma-s-rucnom-pumpom fig-alt="dvostruka hidraulična platforma s ručnom pumpom"}

**Pretpostavke i model**

U zatvorenom ulju u mirovanju tlak koji stvara mali pumpni klip prenosi se jednako na oba radna cilindra. Iz sile i površine pumpnog klipa određuje se tlak, iz njega sila na radnim cilindrima te iz volumne bilance ukupni hod i broj pumpnih poteza.

**Rješenje**

### 1. Tlak u ulju {.unnumbered .unlisted .mf1-step}

Površina pumpnog klipa u SI jedinicama iznosi $A_p = 5 \cdot 10^{-4}\ \text{m}^2$. Tlak koji pumpni klip stvara u ulju jednak je

$$
p = \frac{F_p}{A_p} = \frac{460}{5 \cdot 10^{-4}} = 9{,}20 \cdot 10^5\ \text{Pa} = 0{,}92\ \text{MPa}.
$$ {#eq-svojstva-tlak-1-tlak-u-ulju-01}

### 2. Sila jednog cilindra i ukupno opterećenje {.unnumbered .unlisted .mf1-step}

Površina jednog radnog cilindra u SI jedinicama iznosi $A_L = 150 \cdot 10^{-4} = 0{,}015\ \text{m}^2$. Sila koju preuzima jedan cilindar zato je

$$
F_L = pA_L = 9{,}20 \cdot 10^5 \cdot 0{,}015 = 13800\ \text{N} = 13{,}8\ \text{kN}.
$$ {#eq-svojstva-tlak-2-sila-jednog-cilindra-i-ukupno-opterecenje-01}

Kako postoje dva jednaka cilindra, ukupna idealizirana podizna sila iznosi

$$
G = 2F_L = 2 \cdot 13800 = 27600\ \text{N} = 27{,}6\ \text{kN}.
$$ {#eq-svojstva-tlak-2-sila-jednog-cilindra-i-ukupno-opterecenje-02}

### 3. Zbroj hodova pumpnog klipa {.unnumbered .unlisted .mf1-step}

Za podizanje platforme oba radna cilindra zajedno, uz $s_L = 25\ \text{mm} = 0{,}025\ \text{m}$, trebaju volumen

$$
\Delta V = 2A_L s_L = 2 \cdot 0{,}015 \cdot 0{,}025 = 7{,}5 \cdot 10^{-4}\ \text{m}^3.
$$ {#eq-svojstva-tlak-3-zbroj-hodova-pumpnog-klipa-01}

Taj volumen mora dati pumpni klip, pa iz $A_p s_p = \Delta V$ slijedi

$$
s_p = \frac{\Delta V}{A_p} = \frac{7{,}5 \cdot 10^{-4}}{5 \cdot 10^{-4}} = 1{,}5\ \text{m},
$$ {#eq-svojstva-tlak-3-zbroj-hodova-pumpnog-klipa-02}

što se u praksi ostvaruje nizom kratkih pumpnih poteza.

### 4. Broj punih pumpnih hodova {.unnumbered .unlisted .mf1-step}

Uz $s_h = 180\ \text{mm} = 0{,}180\ \text{m}$ najmanji potreban broj punih hodova je

$$
n = \frac{s_p}{s_h} = \frac{1{,}5}{0{,}180} = 8{,}33,
$$ {#eq-svojstva-tlak-4-broj-punih-pumpnih-hodova-01}

pa je potreban najmanje $n = 9$ punih pumpnih hodova.

**Tumačenje rezultata**

Pumpni klip površine $5\ \text{cm}^2$ pod silom $460\ \text{N}$ u idealnom modelu stvara tlak od $0{,}92\ \text{MPa}$. Na toj tlačnoj razini svaki radni cilindar daje oko $13{,}8\ \text{kN}$, odnosno zajedno oko $27{,}6\ \text{kN}$. To nije dopuštena nosivost platforme: nedostaju vlastita težina, trenje, razdioba opterećenja, čvrstoća, stabilnost, sigurnosni uređaji i mjerodavni propisi. Za podizanje za $25\ \text{mm}$ potreban je ukupni zbroj hodova pumpnog klipa od $1{,}5\ \text{m}$, odnosno najmanje devet punih pumpnih poteza.

Ukupna idealizirana podizna sila veća je od sile na pumpnom klipu zbog veće ukupne radne površine. Ukupni hod pumpe ostaje velik jer mali klip volumenski puni dva velika cilindra. Broj potrebnih punih hodova zaokružuje se na prvi veći cijeli broj.
::: 

::: {#ex-u01-hidraulicna-kocnica-vozila-s-razdiobom-na-vise .mf1-we}
<p class="mf1-box-label">P5. Hidraulična kočnica vozila s razdiobom na više kočnih cilindara &nbsp;<span class="mf1-level">T2</span></p>


**Kontekst:** U hidrauličnom kočnom sustavu osobnog vozila operater pritiska kočnu papučicu, a poluga papučice mehanički povećava silu prije nego se ona prenese na klip glavnog kočnog cilindra. Tlak koji se u glavnom cilindru razvije isti se prenosi do **četiri** kočna cilindra (po jedan u svakom kotaču), ali kočna kliješta na prednjoj osovini imaju veći promjer od onih na stražnjoj. Time se s **jednim** ulazom (papučicom) dobivaju **četiri različite** kočne sile prilagođene podjeli kočne težine između prednje i stražnje osovine.

**Zadano**

- Sila vozača na papučicu: $F_n = 300\ \text{N}$
- Prijenosni omjer papučice: $i = 5$ (poluga $5 : 1$)
- Promjer klipa glavnog cilindra: $d_M = 20\ \text{mm}$
- Promjer kočnog cilindra prednjeg kotača: $d_f = 35\ \text{mm}$ (po jednom kotaču)
- Promjer kočnog cilindra stražnjeg kotača: $d_r = 30\ \text{mm}$ (po jednom kotaču)

**Traženo**

1. Sila kojom poluga papučice tlači klip glavnog cilindra.
2. Manometarski tlak u kočnoj tekućini.
3. Sila koju razvija klip svakoga **prednjeg** kočnog cilindra.
4. Sila koju razvija klip svakoga **stražnjeg** kočnog cilindra.
5. Zbroj sila svih klipova i omjer toga zbroja prema sili vozača na papučicu.

![Hidraulična kočnica vozila: papučica s polugom $i = 5$, glavni cilindar $d_M = 20$ mm i četiri kočna cilindra (prednji $d_f = 35$ mm, stražnji $d_r = 30$ mm). Isti tlak u kočnoj tekućini daje različite sile na kočna kliješta.](../assets/print/u01_fig_kocnica_vozila.svg){#fig-u01-kocnica-vozila fig-align="center" fig-alt="Hidraulična kočnica vozila: papučica s polugom $i = 5$, glavni cilindar $d_M = 20$ mm i četiri kočna cilindra (prednji $d_f = 35$ mm, stražnji $d_r = 30$ mm). Isti tlak u kočnoj tekućini daje različite sile na kočna kliješta."}

**Pretpostavke i model**

Kočna tekućina modelira se kao nestlačiva, vodovi kao kruti i bez gubitaka, a svi kočni cilindri leže na približno istoj razini (hidrostatske razlike između cilindara zanemarive). Trenje u glavnom cilindru i prijelazna dinamika zanemaruju se – promatra se kvazistatičko stanje. Time se sustav svodi na Pascalov zakon: jedna ulazna sila razvija tlak koji je u tom stanju jednak u svim radnim cilindrima.

**Rješenje**

Poluga papučice mehanički pojačava silu vozača:

$$
F_M = i \cdot F_n = 5 \cdot 300 = 1500\ \text{N}
$$ {#eq-svojstva-tlak-rijeseni-primjer-hidraulicna-kocnica-vozila-s-ra-01}

Površina klipa glavnog cilindra:

$$
A_M = \frac{\pi d_M^2}{4} = \frac{\pi \cdot 0{,}020^2}{4} = 3{,}142 \cdot 10^{-4}\ \text{m}^2
$$ {#eq-svojstva-tlak-rijeseni-primjer-hidraulicna-kocnica-vozila-s-ra-02}

Manometarski tlak u kočnoj tekućini:

$$
p = \frac{F_M}{A_M} = \frac{1500}{3{,}142 \cdot 10^{-4}} = 4{,}77 \cdot 10^6\ \text{Pa} \approx 4{,}77\ \text{MPa}
$$ {#eq-svojstva-tlak-rijeseni-primjer-hidraulicna-kocnica-vozila-s-ra-03}

Površine prednjeg i stražnjeg kočnog cilindra:

$$
A_f = \frac{\pi d_f^2}{4} = \frac{\pi \cdot 0{,}035^2}{4} = 9{,}621 \cdot 10^{-4}\ \text{m}^2
$$ {#eq-svojstva-tlak-rijeseni-primjer-hidraulicna-kocnica-vozila-s-ra-04}

$$
A_r = \frac{\pi d_r^2}{4} = \frac{\pi \cdot 0{,}030^2}{4} = 7{,}069 \cdot 10^{-4}\ \text{m}^2
$$ {#eq-svojstva-tlak-rijeseni-primjer-hidraulicna-kocnica-vozila-s-ra-05}

Isti tlak na različitim površinama daje različite sile. Sila po jednom prednjem kočnom cilindru:

$$
F_f = p \cdot A_f = 4{,}77 \cdot 10^6 \cdot 9{,}621 \cdot 10^{-4} \approx 4{,}59\ \text{kN}
$$ {#eq-svojstva-tlak-rijeseni-primjer-hidraulicna-kocnica-vozila-s-ra-06}

Sila po jednom stražnjem kočnom cilindru:

$$
F_r = p \cdot A_r = 4{,}77 \cdot 10^6 \cdot 7{,}069 \cdot 10^{-4} \approx 3{,}38\ \text{kN}
$$ {#eq-svojstva-tlak-rijeseni-primjer-hidraulicna-kocnica-vozila-s-ra-07}

Zbroj sila svih klipova (dva prednja + dva stražnja):

$$
F_{uk} = 2 F_f + 2 F_r = 2 \cdot 4{,}59 + 2 \cdot 3{,}38 = 15{,}94\ \text{kN}
$$ {#eq-svojstva-tlak-rijeseni-primjer-hidraulicna-kocnica-vozila-s-ra-08}

Omjer zbroja sila klipova prema sili na papučici:

$$
k = \frac{F_{uk}}{F_n} = \frac{15{,}94 \cdot 10^3}{300} \approx 53
$$ {#eq-svojstva-tlak-rijeseni-primjer-hidraulicna-kocnica-vozila-s-ra-09}

**Tumačenje rezultata**

1. Broj $k \approx 53$ omjer je zbroja sila četiriju paralelnih aktuatora i jedne ulazne sile; nije pojačanje jedne izlazne sile niti izravno određuje kočni moment vozila. Za kočni moment trebaju još model kliješta, koeficijent trenja obloge, efektivni polumjer diska te veza s gumom i podlogom.
2. Izračunani $F_f$ i $F_r$ sile su pojedinih klipova. Sila stezanja para pločica ovisi o izvedbi kliješta: kod idealiziranih plutajućih kliješta s jednim klipom može biti približno $2F$, dok se kod kliješta s nasuprotnim klipovima zbrajaju doprinosi aktivnih klipova. Zato se bez zadane izvedbe ne smije $pA$ automatski nazvati silom stezanja.
3. Stvarni dopušteni radni tlak i izbor kočne tekućine određuju proizvođač sustava i mjerodavne specifikacije; ovaj idealni hidraulički račun nije specifikacija tekućine ni kočnog sklopa.
4. Ako bi vozač pumpao papučicom dok kočne pločice ne dodirnu disk, ukupni hod papučice morao bi po volumnoj bilanci pokriti hod svih četiriju kočnih cilindara: $A_M s_M = 2 A_f s_f + 2 A_r s_r$. „Mekana" papučica može upućivati na stlačivi plin, propuštanje ili povećanu elastičnost sustava, ali se uzrok ne može dijagnosticirati samo Pascalovim modelom.
:::

::: {#ex-u01-hidraulicka-stezna-naprava-na-robotskoj-liniji-za .mf1-we}
<p class="mf1-box-label">P6. Hidraulička stezna naprava na robotskoj liniji za montažu baterijskih modula električnog vozila &nbsp;<span class="mf1-level">T2</span></p>

**Kontekst:** U robotskoj proizvodnoj liniji za sklapanje litij-ionskih baterijskih modula električnog vozila, prije zavarivanja kontakata ćelija aktivira se sustav hidrauličkih stega koji točno pozicionira modul. Centralna pumpa u kvazistatičkom stanju održava zajednički tlak u više paralelnih steznih cilindara. Svi stezni cilindri su istog promjera jer moduli zahtijevaju jednoliko opterećenje po obodu radi sprječavanja deformacije ćelija.

**Zadano**

- Promjer pumpnog klipa: $d_p = 14\ \text{mm}$
- Sila pogonskog motora na pumpni klip: $F_p = 420\ \text{N}$
- Promjer svakog steznog cilindra: $d_s = 28\ \text{mm}$
- Broj paralelnih stega: $n = 6$
- Najveća dopuštena sila na jednoj baterijskoj ćeliji (radi sprječavanja oštećenja): $F_{dop} = 3{,}5\ \text{kN}$

**Traženo**

1. manometarski tlak u sustavu;
2. sila stezanja jednog cilindra;
3. ukupna sila stezanja na modulu;
4. ostaje li sila po jednoj stezi unutar dopuštene vrijednosti $F_{dop}$.

**Pretpostavke i model**

Hidrauličko ulje smatra se nestlačivim, gubici u vodovima zanemarivi, svi cilindri leže približno na istoj razini. Sustav radi u kvazistatičkom stanju nakon što su sve stege dosegle radni položaj. Tlak se tada uzima jednakim u svim paralelnim steznim cilindrima.

**Rješenje**

Površina pumpnog klipa iznosi

$$
A_p = \frac{\pi d_p^2}{4} = \frac{\pi \cdot 0{,}014^2}{4} = 1{,}539 \cdot 10^{-4}\ \text{m}^2.
$$ {#eq-svojstva-tlak-rijeseni-primjer-hidraulicka-stezna-naprava-na-r-01}

Tlak u sustavu zato je

$$
p = \frac{F_p}{A_p} = \frac{420}{1{,}539 \cdot 10^{-4}} \approx 2{,}729 \cdot 10^6\ \text{Pa} \approx 2{,}73\ \text{MPa}.
$$ {#eq-svojstva-tlak-rijeseni-primjer-hidraulicka-stezna-naprava-na-r-02}

Površina pojedinog steznog cilindra iznosi

$$
A_s = \frac{\pi d_s^2}{4} = \frac{\pi \cdot 0{,}028^2}{4} = 6{,}158 \cdot 10^{-4}\ \text{m}^2.
$$ {#eq-svojstva-tlak-rijeseni-primjer-hidraulicka-stezna-naprava-na-r-03}

Sila stezanja jednog cilindra zato je

$$
F_s = p \cdot A_s = 2{,}729 \cdot 10^6 \cdot 6{,}158 \cdot 10^{-4} \approx 1{,}680\ \text{kN}.
$$ {#eq-svojstva-tlak-rijeseni-primjer-hidraulicka-stezna-naprava-na-r-04}

Kako sustav ima $n = 6$ paralelnih stega, ukupna sila stezanja na modulu iznosi

$$
F_{uk} = n \cdot F_s = 6 \cdot 1{,}680 \approx 10{,}08\ \text{kN}.
$$ {#eq-svojstva-tlak-rijeseni-primjer-hidraulicka-stezna-naprava-na-r-05}

Sila jedne stege $F_s \approx 1{,}68\ \text{kN}$ manja je od zadane granice $F_{dop} = 3{,}5\ \text{kN}$. Time se provjerava idealizirano opterećenje jedne stege, a ne potpuna sigurnost ćelije ili proizvodne linije.

**Pitanje za stručnu provjeru.** Usporedba $F_s$ s dopuštenom silom na jednoj ćeliji vrijedi samo ako konstrukcija stege prenosi silu jednog cilindra na jednu ćeliju bez dodatne raspodjele opterećenja. U stvarnoj napravi odnos sile stege i sile na pojedinoj ćeliji zahtijeva model kontakta i geometrije modula.

**Tumačenje rezultata**

Omjer sile jednoga idealnog cilindra i sile pumpnoga klipa iznosi $F_s/F_p = 1680/420 = 4$, što odgovara omjeru površina $(d_s/d_p)^2 = (28/14)^2 = 4$. Omjer $F_{uk}/F_p = 24$ jest zbroj sila šest paralelnih aktuatora prema jednoj ulaznoj sili; za njihov zajednički hod pumpa mora isporučiti zbroj svih istisnutih volumena. Omjer zadane granice i nominalne sile, $F_{dop}/F_s \approx 2{,}1$, predstavlja razinu rezerve prema jednome kriteriju. Stvarna procjena zahtijeva tolerancije tlaka i površina, raspodjelu kontakta, prijelazne vršne sile, otkazne slučajeve te zasebnu analizu sigurnosti stroja i baterijskog modula.
:::

::: {.mf1-numerika .kompakt}
<p class="mf1-box-label">Numerički most</p>

**Gdje ovo živi u numerici.** Tlak kao skalarno polje $p(x,y,z)$ — temeljni objekt koji svaki CFD solver mora prije svega *postaviti*. Pojam tlaka u kontinuumu i Pascalov zakon su upravo razlog zašto se u nestlačivom CFD-u tlak ne marsira u vremenu, nego se rješava globalno po cijeloj domeni.

**Što numerički alat radi s tim.** Na početku simulacije postavlja se *inicijalni uvjet tlaka* — najčešće jednoliko polje ili hidrostatska raspodjela iz idućeg poglavlja. Promjene na rubu (klip, ulaz crpke, ventil) propagiraju se kroz mrežu kontrolnih volumena unutar jedne iteracije sprege tlaka i brzine.

**Tipičan scenarij.** U industrijskom hidrauličkom sustavu CFD se rijetko primjenjuje na samu Pascalovu prijenosnu silu — ona je analitički rješiva. Vrijednost numerike pojavljuje se onda kad fluid prolazi uskim kanalima, kroz ventile ili kada se promatra dinamika tlačnog vala (vodeni udar pri naglom zatvaranju ventila): tada lokalna polja brzine, tlaka i mogućih kavitacijskih zona postaju netrivijalna, a analitička procjena prestaje biti dovoljna.

> *Nije gradivo MF1. U kasnijim kolegijima posvećenima računalnoj dinamici fluida opisani sadržaj postat će poznat teren.*
:::

::: {.mf1-samoprovjera}
<p class="mf1-box-label">Provjeri sebe</p>

1. Zašto tlak u fluidu u mirovanju u točki ne ovisi o orijentaciji zamišljene plohe kroz tu točku?
2. Zašto veća sila na radnom klipu hidraulične preše ne znači stvaranje rada iz ničega?
3. Kada je razumno uzeti da je ulje u ovim zadatcima praktično nestlačivo?
4. Zašto se u Pascalovu zakonu uspoređuju tlakovi, a ne samo sile?

::: {.callout-note collapse="true"}
### Odgovori

U fluidu u mirovanju tlak je izotropan jer bi inače nastao tangencijalni rezultant koji bi pokrenuo tok. Povećanje sile prati manji pomak pa se idealni rad ne stvara nego prenosi. Aproksimacija nestlačivosti vrijedi kada su promjene gustoće u odnosu na traženu točnost zanemarive. Sile same nisu dovoljne jer ovise i o površini na kojoj djeluju.
:::
:::

::: {.mf1-zavrsni-okvir}
<p class="mf1-box-label">Za ponijeti iz poglavlja</p>

- Kontinuumski model omogućuje da gustoću i tlak promatramo kao polja pogodna za inženjerski račun.
- Tlak je normalna sila po jedinici površine i u fluidu u mirovanju djeluje izotropno.
- Pascalov zakon prenosi promjenu tlaka kroz zatvoren fluid u mirovanju.
- Veći izlazni učinak hidrauličkog sustava prati odgovarajući kompromis u pomaku ili hodu.
- Idealizirani model ne uključuje stlačivost, propuštanje, trenje ni dinamičke valove.
:::

## Zadaci za vježbu

::::: {.mf1-vjezbe-list}

### Z1. Servisna hidraulična preša {#task-u01-u-servisnoj-hidraulicnoj-presi-mali-klip-promjera .unnumbered .unlisted}

U servisnoj hidrauličnoj preši mali klip promjera $d_1 = 28\ \text{mm}$ potiskuje ulje prema radnom klipu promjera $d_2 = 140\ \text{mm}$. Ako operater na mali klip djeluje silom $F_1 = 180\ \text{N}$, odredi tlak u ulju, silu na radnom klipu i pomak radnog klipa ako mali klip prijeđe put $s_1 = 120\ \text{mm}$.

:::: {.content-visible .mf1-hint-online when-format="html"}
::: {.callout-note collapse="true" data-hint-key="true"}
### Naputak
Primjenjuju se $p = F_1/A_1$, $F_2 = pA_2$ te volumna bilanca $A_1 s_1 = A_2 s_2$.
:::
::::
:::: {.content-visible .mf1-answer-online when-format="html"}
::: {.callout-tip collapse="true" data-answer-key="true"}
### Kontrolni rezultat

$p \approx 292\ \text{kPa}$; $F_2 = 4{,}5\ \text{kN}$; $s_2 = 4{,}8\ \text{mm}$.
:::
::::

[Razina: T1]{.mf1-task-level}

### Z2. Dva klipa pod istim tlakom {#task-u01-na-kruzni-klip-promjera-djeluje-sila-odredi .unnumbered .unlisted}

Na kružni klip promjera $d = 24\ \text{mm}$ djeluje sila $F = 95\ \text{N}$. Odredi tlak u ulju i silu koju isti tlak daje na drugi klip promjera $D = 72\ \text{mm}$.

:::: {.content-visible .mf1-hint-online when-format="html"}
::: {.callout-note collapse="true" data-hint-key="true"}
### Naputak
Površina se određuje iz $A = \pi d^2/4$, tlak iz $p = F/A$, a sila na većem klipu iz $F_2 = pA_2$.
:::
::::
:::: {.content-visible .mf1-answer-online when-format="html"}
::: {.callout-tip collapse="true" data-answer-key="true"}
### Kontrolni rezultat

$p \approx 210\ \text{kPa}$; $F_2 = 855\ \text{N}$.
:::
::::

[Razina: T1]{.mf1-task-level}

### Z3. Dimenzioniranje hidraulične stege {#task-u01-u-zatvorenoj-hidraulicnoj-stezi-tlak-ulja-iznosi .unnumbered .unlisted}

U zatvorenoj hidrauličnoj stezi tlak ulja iznosi $p = 2{,}4\ \text{MPa}$, a radni klip ima promjer $d = 52\ \text{mm}$. Odredi silu stezanja i procijeni koliki bi promjer morao imati novi klip ako se pri istom tlaku traži sila stezanja od najmanje $8{,}0\ \text{kN}$.

:::: {.content-visible .mf1-hint-online when-format="html"}
::: {.callout-note collapse="true" data-hint-key="true"}
### Naputak
Primjenjuje se $F = pA$. Iz zahtijevane sile slijedi površina $A = F/p$, a promjer se određuje iz $A = \pi d^2/4$.
:::
::::
:::: {.content-visible .mf1-answer-online when-format="html"}
::: {.callout-tip collapse="true" data-answer-key="true"}
### Kontrolni rezultat

$F \approx 5{,}1\ \text{kN}$; $d_{min} \approx 65\ \text{mm}$.
:::
::::

[Razina: T2]{.mf1-task-level}

### Z4. Podizanje hidrauličnog stola {#task-u01-hidraulicni-stol-nosi-teret-mase-preko-dvaju .unnumbered .unlisted}

Hidraulični stol nosi teret mase $m = 1350\ \text{kg}$ preko dvaju jednakih radnih cilindara promjera $D = 95\ \text{mm}$. Ulje se dovodi ručnom pumpom čiji klip ima promjer $d = 18\ \text{mm}$ i hod $s = 160\ \text{mm}$. Odredi minimalnu silu na pumpnom klipu potrebnu za podizanje tereta i broj punih pumpnih hodova potreban da se stol podigne za $\Delta z = 45\ \text{mm}$.

:::: {.content-visible .mf1-hint-online when-format="html"}
::: {.callout-note collapse="true" data-hint-key="true"}
### Naputak
Teret se raspodjeljuje na dva cilindra. Iz $p = G/(2A_D)$ slijedi $F_p = pA_d$, a broj hodova određuje se iz $nA_d s = 2A_D \Delta z$.
:::
::::
:::: {.content-visible .mf1-answer-online when-format="html"}
::: {.callout-tip collapse="true" data-answer-key="true"}
### Kontrolni rezultat

$p \approx 0{,}93\ \text{MPa}$; $F_p \approx 238\ \text{N}$; $n = 16$ hodova.
:::
::::

[Razina: T2]{.mf1-task-level}

### Z5. Ručna pumpa i podizna platforma {#task-u01-rucna-pumpa-s-klipom-promjera-razvija-silu .unnumbered .unlisted}

Ručna pumpa s klipom promjera $d = 25\ \text{mm}$ razvija silu $F_p = 420\ \text{N}$. Dva radna cilindra promjera $D = 140\ \text{mm}$ nalaze se na istoj razini i podižu platformu. Odredi tlak u ulju, ukupno nosivo opterećenje platforme i ukupni hod pumpnog klipa potreban da se platforma podigne za $\Delta z = 30\ \text{mm}$.

:::: {.content-visible .mf1-hint-online when-format="html"}
::: {.callout-note collapse="true" data-hint-key="true"}
### Naputak
Tlak se određuje iz $p = F_p/A_d$, ukupno opterećenje iz $G = 2pA_D$, a ukupan hod pumpe iz volumne bilance $A_d s_p = 2A_D \Delta z$.
:::
::::
:::: {.content-visible .mf1-answer-online when-format="html"}
::: {.callout-tip collapse="true" data-answer-key="true"}
### Kontrolni rezultat

$p \approx 856\ \text{kPa}$; $G \approx 26{,}3\ \text{kN}$; $s_p \approx 1{,}88\ \text{m}$.
:::
::::

[Razina: T3]{.mf1-task-level}

### Z6. Nosivost stola uz nesigurnu učinkovitost {#task-u01-hidraulicni-radni-stol-podupiru-tri-jednaka-cilindra .unnumbered .unlisted}

Hidraulični radni stol podupiru tri jednaka cilindra, svaki površine $A_L = 95\ \text{cm}^2$. Ulje dovodi pumpni klip promjera $d = 22\ \text{mm}$ na koji djeluje sila $F_p = 360\ \text{N}$. Odredi tlak u ulju, ukupno idealno opterećenje koje stol može nositi i ukupan idealni hod pumpnog klipa potreban da se stol podigne za $\Delta z = 18\ \text{mm}$. Za odluku o puštanju u rad uzmi da su izmjereni faktor prijenosa sile $\eta_F=0{,}86\pm0{,}04$ i volumetrijska učinkovitost $\eta_V=0{,}90\pm0{,}03$. Stol mora nositi najmanje $22{,}0\ \text{kN}$, a raspoloživi hod pumpe iznosi $1{,}60\ \text{m}$. Izračunaj nominalno i konzervativno korisno opterećenje i potreban hod te obrazloži zadovoljava li sustav oba zahtjeva u cijelom zadanom rasponu učinkovitosti.

:::: {.content-visible .mf1-hint-online when-format="html"}
::: {.callout-note collapse="true" data-hint-key="true"}
### Naputak
Površina $A_p$ i tlak određuju se iz $p = F_p/A_p$, idealno opterećenje iz $G = 3pA_L$, a idealni hod pumpe iz volumne bilance $A_p s_p = 3A_L \Delta z$. Za stvarni sustav vrijedi $G_{kor}=\eta_FG$ i $s_{p,st}=s_p/\eta_V$. Konzervativna se odluka temelji na vrijednostima $\eta_{F,min}$ i $\eta_{V,min}$, a ne na srednjim vrijednostima.
:::
::::
:::: {.content-visible .mf1-answer-online when-format="html"}
::: {.callout-tip collapse="true" data-answer-key="true"}
### Kontrolni rezultat

$p \approx 947\ \text{kPa}$; $G \approx 27{,}0\ \text{kN}$; $s_p \approx 1{,}35\ \text{m}$. Nominalno je $G_{kor}\approx23{,}2\ \text{kN}$ i $s_{p,st}\approx1{,}50\ \text{m}$, a konzervativno $G_{kor,min}\approx22{,}1\ \text{kN}$ i $s_{p,st,max}\approx1{,}55\ \text{m}$. Oba zadana brojčana kriterija jesu zadovoljena, ali s malim rezervama, približno $0{,}1\ \text{kN}$ i $0{,}05\ \text{m}$; to nije potpuna provjera stroja ni odobrenje za puštanje u rad.
:::
::::

[Razina: T4]{.mf1-task-level}

:::::

![Skice uz zadatke za vježbu — hidraulične preše, klipovi i radni cilindri (poglavlje 1).](../assets/print/u01_vjezbe_skice.svg){#fig-u01-vjezbe fig-align="center" fig-alt="Skice uz zadatke za vježbu — hidraulične preše, klipovi i radni cilindri (poglavlje 1)."}

## Sažetak

Fluid se u inženjerskoj analizi najčešće opisuje kontinuumskim modelom, pri čemu su gustoća $\rho$, tlak $p$ i druge fizikalne veličine definirane kao polja u prostoru. Gustoća je masa po jedinici volumena, specifična težina težinska sila po jedinici volumena, a relativna gustoća bezdimenzijski omjer gustoće fluida i referentne gustoće vode.

Tlak je normalna sila po jedinici površine i u fluidu u mirovanju djeluje jednako u svim smjerovima. Pascalov zakon opisuje prijenos nametnute promjene tlaka kroz zatvoreni fluid u mirovanju. U idealiziranom hidrauličnom sustavu isti porast tlaka na klipovima različitih površina mijenja omjer sila prema $F_2/F_1=A_2/A_1$. Za nestlačiv fluid istodobno vrijedi $A_1s_1=A_2s_2$, pa povećanje izlazne sile prati razmjerno smanjenje izlaznoga pomaka, uz očuvanje mehaničkog rada.

Prikazani model zanemaruje stlačivost fluida, elastičnost vodova, unutarnje propuštanje, trenje i gubitke u ventilima. Ti utjecaji u stvarnim hidrauličnim sustavima određuju odstupanje od idealnoga prijenosa sile i pomaka.
