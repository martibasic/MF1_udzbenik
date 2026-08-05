![Pregled poglavlja: fizikalni sustav (Pascalov zakon s dva klipa), ključna jednadžba p = F₁/A₁ = F₂/A₂ i primjena u praksi (hidraulična dizalica)](../assets/print/u01_fig_uvod_pregled.svg){#fig-uvod-u01 fig-align="center" fig-alt="Pregled poglavlja: fizikalni sustav (Pascalov zakon s dva klipa), ključna jednadžba p = F₁/A₁ = F₂/A₂ i primjena u praksi (hidraulična dizalica)"}

## Fluid kao kontinuum: model umjesto popisa formula

Prvo poglavlje ne počinje samo definicijom tlaka ili gustoće. Najprije se razjašnjava što je fluid, zašto ga opisujemo kontinuumom i zašto su tlak i Pascalov zakon prirodne posljedice tog modela.

Bez tog uvoda kasnija hidrostatika i Bernoullijeva jednadžba lako postaju samo algebra bez fizikalnoga smisla.

::: {.mf1-application}
<p class="mf1-box-label">Inženjerski kontekst</p>

Hidraulične dizalice, preše za oblikovanje lima i brodski kormilarski hidraulični pogoni počivaju na istoj ideji: tlak prenesen zatvorenim fluidom pretvara mali ulazni napor u veliku radnu silu. Zato se u ovom poglavlju gustoća, tlak i Pascalov zakon ne čitaju odvojeno, nego kao povezane veličine kojima se čita cilindar, crpka, vod i radni alat.
:::

::: {.mf1-priprema}
<p class="mf1-box-label">Prije čitanja poglavlja</p>

**Predznanje koje se pretpostavlja:**

- pojam sile i mase iz Fizike I; jedinice SI sustava;
- osnove geometrije (površina kruga $A = \pi d^2/4$, prevođenje cm² u m²);
- razlikovanje težine od mase u gravitacijskom polju.

**Ishodi učenja:**

- razlikovati silu, tlak, gustoću i specifičnu težinu kao zasebne fizikalne veličine;
- prepoznati tlak kao skalarno polje u mirujućem fluidu i razumjeti zašto djeluje jednako u svim smjerovima;
- primijeniti Pascalov zakon na zatvoreni hidraulični sustav s dva ili više klipova;
- objasniti zašto pojačanje sile uvijek prati proporcionalno smanjenje pomaka.

**Procijenjeno vrijeme rada uz udžbenik:** 8 sati.
:::

::: {.callout-tip collapse="true" icon="false"}
## Mehanika fluida i numerika — najava

Svaka jednadžba u ovom udžbeniku ima svoju ulogu u **računalnoj dinamici fluida (CFD)**. Time se ovdje neće baviti detaljnije — to je tema kolegija Računalna dinamika fluida. No kroz udžbenik javljaju se dvije vrste oznaka:

- **Numerički trag** *(sklopiv, uz pojedine jednadžbe)* — kratki podsjetnik gdje ta jednadžba živi u numerici.
- **Numerički most** *(na kraju svakog poglavlja, plavi okvir)* — kratak osvrt kamo navedeno poglavlje vodi dalje.

Nije gradivo MF1. Otvara se s znatiželjom.
:::

## Fizikalni uvod i matematički izvod

Fluid je tvar koja se pod djelovanjem tangencijalnog naprezanja neprestano deformira. Zato ga u inženjerskom radu ne pratimo po molekulama, nego uvodimo kontinuumski model: pretpostavljamo da su veličine poput gustoće, tlaka i brzine definirane u svakoj točki prostora.

Tek tada matematika dobiva jasan fizički smisao: polja poput $p(x,y,z)$ i $\rho(x,y,z)$ nisu apstrakcija radi apstrakcije, nego način da složen stvarni fluid postane računski čitljiv i mjerljiv.

U tom jeziku tlak postaje osnovna radna veličina:

$$
p = \frac{F_n}{A}
$$ {#eq-svojstva-tlak-fizikalni-uvod-i-matematicki-izvod-01}

::: {.mf1-fizikalno-znacenje}
<p class="mf1-box-label">Fizikalno značenje</p>
Tlak nije sila – on mjeri koliko je sile sabijeno na jedinicu površine. Ista sila raspršena na veliku površinu daje nizak tlak; stisnuta na malu površinu daje visok tlak. U mirujućem fluidu nema tangencijalnih naprezanja, pa tlak u jednoj točki djeluje jednako u svim smjerovima – vodoravno, okomito i dijagonalno – i zato ga opisujemo jednim skalarem, a ne vektorom.
:::

Za mirujući zatvoreni fluid promjena tlaka prenosi se jednako u svim smjerovima. To je radna srž Pascalova zakona i razlog zašto hidraulični sustavi mogu pretvoriti malu silu na malom klipu u veliku silu na velikom klipu.

## Osnovne veličine koje se najčešće miješaju

Na samom početku treba razdvojiti tri veličine koje studenti najčešće miješaju:

$$
\rho = \frac{m}{V}
$$ {#eq-svojstva-tlak-osnovne-velicine-koje-se-najcesce-mijesaju-01}

$$
\gamma = \rho g
$$ {#eq-svojstva-tlak-osnovne-velicine-koje-se-najcesce-mijesaju-02}

$$
s_r = \frac{\rho}{\rho_{voda}}
$$ {#eq-svojstva-tlak-osnovne-velicine-koje-se-najcesce-mijesaju-03}

::: {.mf1-fizikalno-znacenje}
<p class="mf1-box-label">Fizikalno značenje</p>
Gustoća $\rho$ mjeri masenu zbijenost fluida – koliko kilograma mase stane u jedan kubni metar. Specifična težina $\gamma = \rho g$ pretvara tu masu u gravitacijsku silu: to je ono što fluid u Zemljinom polju fizički "teži" po kubnom metru. Relativna gustoća $s_r$ je bezdimenzijski omjer prema vodi: vrijednost 0,86 odmah kaže da ulje pluta na vodi jer je lakše, a vrijednost 13,6 za živu kaže da gotovo 14 litara vode teži koliko litra žive.
:::

Gustoća govori koliko mase ima u jedinici volumena, specifična težina kolika je težina tog volumena, a relativna gustoća daje odnos prema vodi kao referenci. Ako se ove tri veličine ne odvoje u <span class="mf1-ch-ref"><span class="mf1-ch-code">pog. 1</span><span class="mf1-ch-title">Osnove fluida i Pascalov zakon</span></span>, kasnije pogreške u hidrostatici i uzgonu izgledaju kao računski problem, iako su zapravo problem modela. Tlak je normalna sila po jedinici površine. U mirujućem fluidu tlak u jednoj točki djeluje jednako u svim smjerovima, pa ga opisujemo kao skalarno polje, a ne kao vektor. Taj je korak temeljni: kasnije ćemo iz tlaka dobivati sile na plohe i stijenke, ali sam tlak nije sila nego intenzitet normalnog naprezanja.

::: {#ex-u01-gustoca-specificna-tezina-i-relativna-gustoca-ulja .mf1-we}
<p class="mf1-box-label">Kratki primjer — Gustoća, specifična težina i relativna gustoća ulja&nbsp;<span class="mf1-level">T1</span></p>

**Kontekst:** Hidraulično ulje koristi se kao radni medij u hidrauličnim sustavima. Za odabir komponenti i provjeru uzgona potrebno je razlikovati gustoću, specifičnu težinu i relativnu gustoću tog ulja.

**Zadano**

- Gustoća hidrauličnog ulja: $\rho = 860\ \text{kg/m}^3$

**Traženo**

1. specifičnu težinu $\gamma$.
2. relativnu gustoću $s_r$.

![Gustoća, specifična težina i relativna gustoća ulja (ρ = 860 kg/m³) u usporedbi s vodom (ρ = 1000 kg/m³)](../assets/print/u01_fig_gustoca_sr.svg){#fig-u01-gustoca-sr fig-align="center" fig-alt="Gustoća, specifična težina i relativna gustoća ulja (ρ = 860 kg/m³) u usporedbi s vodom (ρ = 1000 kg/m³)"}

**Pretpostavke i model**

Uzmi

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

**Provjera i komentar**

1. Relativna gustoća mora biti bez dimenzije.
2. Specifična težina mora imati jedinicu sile po volumenu, a ne mase po volumenu.
3. Čim se pomiješaju $\rho$, $\gamma$ i $s_r$, kasniji zadaci s tlakom i uzgonom kreću iz pogrešne fizikalne veličine.
:::

Kad su osnovne veličine razdvojene, Pascalov zakon više se ne čita kao napamet naučena formula, nego kao prirodna posljedica tlaka u zatvorenom mirujućem fluidu.

## Pascalov zakon kao prvi inženjerski alat

Pascalov zakon ne govori da fluid "stvara" silu, nego da se u povezanom fluidu u mirovanju nametnuta promjena tlaka prenosi bez promjene na sve njegove dijelove. U primjeni na dva klipa pretpostavljaju se kvazistatičko stanje, približno jednake visine klipova te zanemarivi gubici i stlačivost. Ako klipovi nisu na istoj visini, u apsolutni tlak treba uključiti i hidrostatsku razliku. Uz te uvjete vrijedi

$$
\Delta p = \frac{F_1}{A_1} = \frac{F_2}{A_2}
$$ {#eq-svojstva-tlak-pascalov-zakon-kao-prvi-inzenjerski-alat-01}

odnosno

$$
F_2 = F_1 \frac{A_2}{A_1}
$$ {#eq-svojstva-tlak-pascalov-zakon-kao-prvi-inzenjerski-alat-02}

::: {.mf1-fizikalno-znacenje}
<p class="mf1-box-label">Fizikalno značenje</p>
Pascalov zakon ne stvara energiju – on mijenja omjer sile i pomaka. Isti tlak koji mali klip unosi u zatvoreni fluid, fluid prenosi jednako prema svim stjenkama. Gdje je površina veća, isti tlak skuplja veću ukupnu silu. Omjer $A_2/A_1 = 35$ znači 35 puta veća izlazna sila, ali uz 35 puta manji izlazni pomak: mehanički rad ulaza ostaje jednak mehaničkom radu izlaza.
:::

::: {.callout-note collapse="true" icon="false"}
## Numerički trag

U stvarnom fluidu poremećaj tlaka ne putuje trenutačno, nego konačnom brzinom tlačnoga vala, približno akustičnom brzinom sustava fluid–cijev. U modelu nestlačivoga strujanja ta se vrlo brza dinamika ne razlučuje: tlak djeluje kao globalno polje kojim se u svakom vremenskom koraku nameće uvjet očuvanja mase. Zato pressure-based CFD rješavači, primjerice algoritmi SIMPLE i PISO, dobivaju tlak iz eliptičke jednadžbe za korekciju tlaka. Globalna matematička sprega svojstvo je nestlačivoga modela, a ne tvrdnja o beskonačno brzoj fizikalnoj propagaciji.
:::

::: {.mf1-interaktivno}
<p class="mf1-box-label">Interaktivni prikaz — Hidraulična preša</p>

Interaktivni prikaz omogućuje mijenjanje promjera ulaznog i izlaznog klipa te sile na ulazu uz neposredno praćenje izlazne sile i pripadnog omjera pomaka klipova. Vizualizacija jasno razdvaja pojačanje sile od smanjenja pomaka koje slijedi iz očuvanja istisnutog volumena.

<div class="mf1-interaktivno-akcija">
<a class="mf1-interaktivno-veza" href="https://martibasic.github.io/MF1_udzbenik/jlite/lab/index.html?path=u01_hidraulicna_presa.ipynb">Pokreni u pregledniku</a>
<a class="mf1-interaktivno-veza" href="https://colab.research.google.com/github/martibasic/MF1_udzbenik/blob/main/notebooks/u01_hidraulicna_presa.ipynb" target="_blank" rel="noopener">Pričuvno: otvori u Colabu</a>
<img class="mf1-interaktivno-qr" src="../assets/qr/u01_hidraulicna_presa.svg" alt="QR kod za interaktivni prikaz hidraulične preše"/>
</div>

<div class="mf1-interaktivno-pitanja">
**Pitanja za samostalno istraživanje:** (a) Što se događa s pojačanjem sile kada se $D_1$ približi $D_2$? (b) Postoji li teorijska granica omjera $D_2/D_1$ koju propisuje sam Pascalov zakon? (c) Vrijedi li bilanca rada $F_1 s_1 = F_2 s_2$ za sve odabire parametara?
</div>
:::

Pojačanje sile ne znači pojačanje rada niotkuda. Ako zanemarimo gubitke i stlačivost, istisnuti volumen ostaje isti, pa je

$$
A_1 s_1 = A_2 s_2
$$ {#eq-svojstva-tlak-interaktivni-prikaz-hidraulicna-presa-01}

::: {.mf1-fizikalno-znacenje}
<p class="mf1-box-label">Fizikalno značenje</p>
Ova jednadžba je izravna posljedica nestlačivosti fluida: volumen koji uđe u sustav mora negdje izaći. Manji klip mora prijeći duži put da istisnuti volumen bude jednak volumenu koji veliki klip pomakne za kratki hod. Zato sustav s omjerom površina 35 zahtijeva da mali klip hoda 35 puta dulje od radnog klipa. Volumna bilanca vrijedi neovisno o tlaku – dovoljno je da je fluid nestlačiv.
:::

Veća izlazna sila zato dolazi uz manji izlazni pomak.

U ovom se poglavlju zato zadržavamo na osnovnom hidrauličnom prijenosu u kojem se tlak prenosi kroz zatvoreni mirujući fluid bez dodatnog hodanja po visinama. Kad radne točke nisu na istoj razini, isti se sustav mora čitati zajedno s hidrostatikom, što pripada <span class="mf1-ch-ref"><span class="mf1-ch-code">pog. 3</span><span class="mf1-ch-title">Hidrostatička raspodjela tlaka i manometrija</span></span>.

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

Fizikalno značenje članova pritom je neposredno: $F_1$ je ulazna sila, $A_1$ površina preko koje se ta sila pretvara u tlak, $F_2$ izlazna radna sila, a $A_2$ površina na kojoj isti tlak daje veći ukupni iznos sile. Povećanje sile ne znači i stvaranje rada niotkuda. Ako se fluid uzme nestlačivim, istisnuti volumen mora biti jednak na oba klipa, pa vrijedi

$$
\Delta V_1 = \Delta V_2
\qquad \Longrightarrow \qquad
A_1 s_1 = A_2 s_2.
$$ {#eq-svojstva-tlak-matematicki-izvod-pascalov-zakon-i-ocuvanje-rada-04}

Uvrštavanjem odnosa sila i hodova slijedi i radna bilanca

$$
F_1 s_1 = F_2 s_2,
$$ {#eq-svojstva-tlak-matematicki-izvod-pascalov-zakon-i-ocuvanje-rada-05}

::: {.callout-note}
## Razrada koraka
Korak: $F_2 = F_1 \dfrac{A_2}{A_1}$ i $A_1 s_1 = A_2 s_2$ $\;\Rightarrow\;$ $F_1 s_1 = F_2 s_2$

Iz volumne bilance slijedi $s_2 = s_1 \dfrac{A_1}{A_2}$. Uvrstimo to u rad izlaza:
$$
F_2 s_2 = F_1 \frac{A_2}{A_1} \cdot s_1 \frac{A_1}{A_2} = F_1 s_1.
$$ {#eq-svojstva-tlak-razrada-koraka-01}
Razlomci $A_2/A_1$ i $A_1/A_2$ se pokrate bez obzira na veličinu površina, pa jednakost radova vrijedi općenito za svaki omjer klipova.
:::

što zatvara cjelovito fizikalno značenje Pascalova zakona: hidraulični sustav mijenja omjer sile i pomaka zato što isti porast tlaka djeluje na različitim površinama, ali ukupna mehanička energija ne nastaje iz ničega.
:::

::: {.mf1-dublje}
<p class="mf1-box-label">Dublje — Izotropnost tlaka (Cauchyjev tetraedar)</p>

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

## Riješeni primjeri

::: {#ex-u01-optereceni-klip-i-tlak-u-zatvorenom-cilindru .mf1-we}
<p class="mf1-box-label">Riješeni primjer — Opterećeni klip i tlak u zatvorenom cilindru&nbsp;<span class="mf1-level">T2</span></p>

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

Površinu radnog klipa treba zapisati u SI jedinicama:

$$
A_2 = 450 \cdot 10^{-4} = 0{,}0450\ \text{m}^2.
$$ {#eq-svojstva-tlak-rijeseni-primjer-optereceni-klip-i-tlak-u-03}

Sila na radnom klipu zato je

$$
F_2 = pA_2 = 1{,}79 \cdot 10^5 \cdot 0{,}0450 = 8{,}06 \cdot 10^3\ \text{N} \approx 8{,}06\ \text{kN}.
$$ {#eq-svojstva-tlak-rijeseni-primjer-optereceni-klip-i-tlak-u-04}

**Provjera i komentar**

1. Veća ukupna sila na istom klipu mora dati veći tlak u ulju.
2. Na većem radnom klipu ista tlačna razina mora dati veću silu.
3. Ako je izlazna sila veća od ulazne, to je ovdje posljedica većeg presjeka, a ne stvaranja rada niotkuda.
:::

::: {#ex-u01-servisna-hidraulicna-dizalica-t2 .mf1-we}
<p class="mf1-box-label">Riješeni primjer — Servisna hidraulična dizalica&nbsp;<span class="mf1-level">T2</span></p>

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

Zanemari gubitke i stlačivost ulja.

![servisna hidraulična dizalica](../assets/print/u01_val2_hidraulicna_dizalica.svg){#fig-u01-servisna-hidraulicna-dizalica fig-alt="servisna hidraulična dizalica"}

**Pretpostavke i model**

Promatra se mirujući fluid u zatvorenom hidrauličnom sustavu. Najprije se iz sile i površine dobije tlak, zatim se isti tlak prenese na drugi klip, a na kraju se pomak zatvara jednakošću istisnutog volumena.

**Rješenje**

Površinu malog klipa treba pretvoriti u kvadratne metre:

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

**Provjera i komentar**

1. Izlazna sila mora biti mnogo veća od ulazne jer je $A_2/A_1 = 35$.
2. Izlazni pomak mora biti mnogo manji od ulaznog iz istog razloga.
3. Ako su i sila i pomak ispali veliki, negdje je izgubljeno očuvanje volumena odnosno rada.
:::

::: {#ex-u01-dvostruka-hidraulicna-platforma-s-rucnom-pumpom-t3 .mf1-ch}
<p class="mf1-box-label">Cjeloviti zadatak — Dvostruka hidraulična platforma s ručnom pumpom&nbsp;<span class="mf1-level">T3</span></p>

**Kontekst:** U autoservisnoj radionici servisna platforma za pregled vozila oslanja se na dva paralelna radna cilindra, dok operater ručnom pumpom razvija tlak u hidrauličnom ulju. Treba odrediti idealizirani tlak i podiznu silu te ukupan hod i broj poteza pumpe za podizanje na zadanu visinu.

**Zadano**

- Površina jednog radnog cilindra: $A_L = 150\ \text{cm}^2$ (dva jednaka cilindra)
- Površina pumpnog klipa: $A_p = 5\ \text{cm}^2$
- Sila operatera na pumpni klip: $F_p = 460\ \text{N}$
- Visina podizanja platforme: $s_L = 25\ \text{mm}$
- Puni hod pumpnog klipa: $s_h = 180\ \text{mm}$

Zanemari gubitke i stlačivost ulja. Pretpostavi da su oba radna cilindra jednako opterećena.

**Traženo**

1. tlak $p$ u ulju.
2. silu jednoga radnog cilindra i ukupnu idealiziranu podiznu silu $G$.
3. ukupni zbroj hodova pumpnog klipa potreban da se platforma podigne za $s_L$.
4. najmanji broj punih pumpnih hodova potreban za taj podizaj.

![dvostruka hidraulična platforma s ručnom pumpom](../assets/print/u01_ch1_dvostruka_platforma_manometar.svg){#fig-u01-dvostruka-hidraulicna-platforma-s-rucnom-pumpom fig-alt="dvostruka hidraulična platforma s ručnom pumpom"}

**Pretpostavke i model**

U zatvorenom mirujućem ulju tlak koji stvara mali pumpni klip prenosi se jednako na oba radna cilindra. Zato se najprije iz sile i površine pumpnog klipa određuje tlak, zatim iz toga sila na radnim cilindrima, a na kraju iz volumne bilance ukupni hod i broj pumpnih poteza.

**Rješenje**

### 1. Tlak u ulju

Površina pumpnog klipa u SI jedinicama iznosi $A_p = 5 \cdot 10^{-4}\ \text{m}^2$. Tlak koji pumpni klip stvara u ulju jednak je

$$
p = \frac{F_p}{A_p} = \frac{460}{5 \cdot 10^{-4}} = 9{,}20 \cdot 10^5\ \text{Pa} = 0{,}92\ \text{MPa}.
$$ {#eq-svojstva-tlak-1-tlak-u-ulju-01}

#### 2. Sila jednog cilindra i ukupno opterećenje

Površina jednog radnog cilindra u SI jedinicama iznosi $A_L = 150 \cdot 10^{-4} = 0{,}015\ \text{m}^2$. Sila koju preuzima jedan cilindar zato je

$$
F_L = pA_L = 9{,}20 \cdot 10^5 \cdot 0{,}015 = 13800\ \text{N} = 13{,}8\ \text{kN}.
$$ {#eq-svojstva-tlak-2-sila-jednog-cilindra-i-ukupno-opterecenje-01}

Kako postoje dva jednaka cilindra, ukupna idealizirana podizna sila iznosi

$$
G = 2F_L = 2 \cdot 13800 = 27600\ \text{N} = 27{,}6\ \text{kN}.
$$ {#eq-svojstva-tlak-2-sila-jednog-cilindra-i-ukupno-opterecenje-02}

#### 3. Zbroj hodova pumpnog klipa

Za podizanje platforme oba radna cilindra zajedno, uz $s_L = 25\ \text{mm} = 0{,}025\ \text{m}$, trebaju volumen

$$
\Delta V = 2A_L s_L = 2 \cdot 0{,}015 \cdot 0{,}025 = 7{,}5 \cdot 10^{-4}\ \text{m}^3.
$$ {#eq-svojstva-tlak-3-zbroj-hodova-pumpnog-klipa-01}

Taj volumen mora dati pumpni klip, pa iz $A_p s_p = \Delta V$ slijedi

$$
s_p = \frac{\Delta V}{A_p} = \frac{7{,}5 \cdot 10^{-4}}{5 \cdot 10^{-4}} = 1{,}5\ \text{m},
$$ {#eq-svojstva-tlak-3-zbroj-hodova-pumpnog-klipa-02}

što se u praksi ostvaruje nizom kratkih pumpnih poteza.

#### 4. Broj punih pumpnih hodova

Uz $s_h = 180\ \text{mm} = 0{,}180\ \text{m}$ najmanji potreban broj punih hodova je

$$
n = \frac{s_p}{s_h} = \frac{1{,}5}{0{,}180} = 8{,}33,
$$ {#eq-svojstva-tlak-4-broj-punih-pumpnih-hodova-01}

pa u praksi treba uzeti $n = 9$ punih pumpnih hodova.

**Provjera i komentar**

Pumpni klip površine $5\ \text{cm}^2$ pod silom $460\ \text{N}$ u idealnom modelu stvara tlak od $0{,}92\ \text{MPa}$. Na toj tlačnoj razini svaki radni cilindar daje oko $13{,}8\ \text{kN}$, odnosno zajedno oko $27{,}6\ \text{kN}$. To nije dopuštena nosivost platforme: nedostaju vlastita težina, trenje, razdioba opterećenja, čvrstoća, stabilnost, sigurnosni uređaji i mjerodavni propisi. Za podizanje za $25\ \text{mm}$ potreban je ukupni zbroj hodova pumpnog klipa od $1{,}5\ \text{m}$, odnosno najmanje devet punih pumpnih poteza.

1. Ukupna idealizirana podizna sila mora biti mnogo veća od sile pumpnog klipa jer je ukupna radna površina mnogo veća od pumpne.
2. Ukupni hod pumpe mora ostati velik jer mali klip volumenski puni dva velika cilindra.
3. Broj punih hodova mora se na kraju zaokružiti na prvi veći cijeli broj.
::: 

::: {#ex-u01-hidraulicna-kocnica-vozila-s-razdiobom-na-vise .mf1-we}
<p class="mf1-box-label">Riješeni primjer — Hidraulična kočnica vozila s razdiobom na više kočnih cilindara &nbsp;<span class="mf1-level">T2</span></p>

**Primjer za strojare**

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

**Provjera i komentar**

1. Broj $k \approx 53$ omjer je zbroja sila četiriju paralelnih aktuatora i jedne ulazne sile; nije pojačanje jedne izlazne sile niti izravno određuje kočni moment vozila. Za kočni moment trebaju još model kliješta, koeficijent trenja obloge, efektivni polumjer diska te veza s gumom i podlogom.
2. Izračunani $F_f$ i $F_r$ sile su pojedinih klipova. Sila stezanja para pločica ovisi o izvedbi kliješta: kod idealiziranih plutajućih kliješta s jednim klipom može biti približno $2F$, dok se kod kliješta s nasuprotnim klipovima zbrajaju doprinosi aktivnih klipova. Zato se bez zadane izvedbe ne smije $pA$ automatski nazvati silom stezanja.
3. Stvarni dopušteni radni tlak i izbor kočne tekućine određuju proizvođač sustava i mjerodavne specifikacije; ovaj idealni hidraulički račun nije specifikacija tekućine ni kočnog sklopa.
4. Ako bi vozač pumpao papučicom dok kočne pločice ne dodirnu disk, ukupni hod papučice morao bi po volumnoj bilanci pokriti hod svih četiriju kočnih cilindara: $A_M s_M = 2 A_f s_f + 2 A_r s_r$. „Mekana" papučica može upućivati na stlačivi plin, propuštanje ili povećanu elastičnost sustava, ali se uzrok ne može dijagnosticirati samo Pascalovim modelom.
:::

::: {#ex-u01-hidraulicka-stezna-naprava-na-robotskoj-liniji-za .mf1-we}
<p class="mf1-box-label">Riješeni primjer — Hidraulička stezna naprava na robotskoj liniji za montažu baterijskih modula električnog vozila &nbsp;<span class="mf1-level">T2</span></p>

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

Sila po jednoj stezi $F_s \approx 1{,}68\ \text{kN}$ ostaje ispod u zadatku zadane granice $F_{dop} = 3{,}5\ \text{kN}$. To je provjera idealiziranoga opterećenja jedne stege, a ne potpuna potvrda sigurnosti ćelije ili proizvodne linije.

**Provjera i komentar**

Omjer sile jednoga idealnog cilindra i sile pumpnoga klipa iznosi $F_s/F_p = 1680/420 = 4$, što odgovara omjeru površina $(d_s/d_p)^2 = (28/14)^2 = 4$. Omjer $F_{uk}/F_p = 24$ samo je zbroj sila šest paralelnih aktuatora prema jednoj ulaznoj sili; za njihov zajednički hod pumpa mora isporučiti zbroj svih istisnutih volumena. Omjer zadane granice i nominalne sile, $F_{dop}/F_s \approx 2{,}1$, ovdje je nastavna rezerva prema jednom kriteriju. Stvarna procjena traži najmanje tolerancije tlaka i površina, raspodjelu kontakta, prijelazne vršne sile, otkazne slučajeve te zasebnu analizu sigurnosti stroja i baterijskog modula.
:::

::: {.mf1-samoprovjera}
<p class="mf1-box-label">Provjeri sebe</p>

Sljedeća pitanja služe za samostalnu provjeru razumijevanja prije prelaska na zadatke za vježbu. Preporučuje se prvo samostalno odgovoriti, a tek zatim otvoriti sklopivi blok s kratkim odgovorom.

1. Što se događa s pojačanjem sile $F_2/F_1$ ako se promjer obaju klipova udvostruči?

::: {.callout-note collapse="true"}
### Odgovor
Pojačanje sile se ne mijenja jer ovisi isključivo o omjeru površina $A_2/A_1$, a taj omjer ostaje jednak kada se oba promjera proporcionalno povećaju.
:::

2. Zašto pojačana izlazna sila u hidrauličnoj preši ne narušava zakon očuvanja energije?

::: {.callout-note collapse="true"}
### Odgovor
Veća izlazna sila proporcionalno je nadoknađena manjim izlaznim pomakom; iz volumne bilance vrijedi $F_1 s_1 = F_2 s_2$, pa mehanički rad ulaza ostaje jednak mehaničkom radu izlaza.
:::

3. Kako tlak djeluje u pojedinoj točki mirujućega fluida — vektorski ili skalarno, i zašto?

::: {.callout-note collapse="true"}
### Odgovor
Tlak u mirujućem fluidu djeluje jednako u svim smjerovima jer nema tangencijalnih naprezanja koja bi razlikovala smjer; opisuje ga jedan skalarni broj u svakoj točki, a ne vektor.
:::

4. Kolika je razlika između $\rho$, $\gamma$ i $s_r$, i u kojim jedinicama se izražavaju?

::: {.callout-note collapse="true"}
### Odgovor
Gustoća $\rho$ je masa po jedinici volumena (kg/m³), specifična težina $\gamma = \rho g$ je težinska sila po jedinici volumena (N/m³), a relativna gustoća $s_r = \rho/\rho_{voda}$ je bezdimenzijski omjer prema referentnoj gustoći vode.
:::
:::

## Zadaci za vježbu

::::: {.mf1-vjezbe-list}
1. [**T1**]{#task-u01-u-servisnoj-hidraulicnoj-presi-mali-klip-promjera} U servisnoj hidrauličnoj preši mali klip promjera $d_1 = 28\ \text{mm}$ potiskuje ulje prema radnom klipu promjera $d_2 = 140\ \text{mm}$. Ako operater na mali klip djeluje silom $F_1 = 180\ \text{N}$, odredi tlak u ulju, silu na radnom klipu i pomak radnog klipa ako mali klip prijeđe put $s_1 = 120\ \text{mm}$.

   :::: {.content-visible .mf1-hint-online when-format="html"}
   ::: {.callout-note collapse="true" data-hint-key="true"}
   ### Naputak
   $p = F_1/A_1$; zatim $F_2 = pA_2$ i iz volumne bilance $A_1 s_1 = A_2 s_2$.
   :::
   ::::
   :::: {.content-visible .mf1-answer-online when-format="html"}
   ::: {.callout-tip collapse="true" data-answer-key="true"}
   ### Kontrolni rezultat

   $p \approx 292\ \text{kPa}$; $F_2 = 4{,}5\ \text{kN}$; $s_2 = 4{,}8\ \text{mm}$.
   :::
   ::::
   **Skica:** da - dva klipa spojena istim fluidom, kote $d_1$, $d_2$, $s_1$, $s_2$ i sile $F_1$, $F_2$.

2. [**T1**]{#task-u01-na-kruzni-klip-promjera-djeluje-sila-odredi} Na kružni klip promjera $d = 24\ \text{mm}$ djeluje sila $F = 95\ \text{N}$. Odredi tlak u ulju i silu koju isti tlak daje na drugi klip promjera $D = 72\ \text{mm}$.

   :::: {.content-visible .mf1-hint-online when-format="html"}
   ::: {.callout-note collapse="true" data-hint-key="true"}
   ### Naputak
   najprije $A = \pi d^2/4$, zatim $p = F/A$ i na većem klipu $F_2 = pA_2$.
   :::
   ::::
   :::: {.content-visible .mf1-answer-online when-format="html"}
   ::: {.callout-tip collapse="true" data-answer-key="true"}
   ### Kontrolni rezultat

   $p \approx 210\ \text{kPa}$; $F_2 = 855\ \text{N}$.
   :::
   ::::
   **Skica:** da - dva kružna klipa različitih promjera u istoj hidrauličnoj grani.

3. [**T2**]{#task-u01-u-zatvorenoj-hidraulicnoj-stezi-tlak-ulja-iznosi} U zatvorenoj hidrauličnoj stezi tlak ulja iznosi $p = 2{,}4\ \text{MPa}$, a radni klip ima promjer $d = 52\ \text{mm}$. Odredi silu stezanja i procijeni koliki bi promjer morao imati novi klip ako se pri istom tlaku traži sila stezanja od najmanje $8{,}0\ \text{kN}$.

   :::: {.content-visible .mf1-hint-online when-format="html"}
   ::: {.callout-note collapse="true" data-hint-key="true"}
   ### Naputak
   koristi $F = pA$; iz tražene sile vrati površinu $A = F/p$, pa zatim promjer iz $A = \pi d^2/4$.
   :::
   ::::
   :::: {.content-visible .mf1-answer-online when-format="html"}
   ::: {.callout-tip collapse="true" data-answer-key="true"}
   ### Kontrolni rezultat

   $F \approx 5{,}1\ \text{kN}$; $d_{min} \approx 65\ \text{mm}$.
   :::
   ::::
   **Skica:** da - hidraulična stega s jednim radnim klipom i označenom silom stezanja.

4. [**T2**]{#task-u01-hidraulicni-stol-nosi-teret-mase-preko-dvaju} Hidraulični stol nosi teret mase $m = 1350\ \text{kg}$ preko dvaju jednakih radnih cilindara promjera $D = 95\ \text{mm}$. Ulje se dovodi ručnom pumpom čiji klip ima promjer $d = 18\ \text{mm}$ i hod $s = 160\ \text{mm}$. Odredi minimalnu silu na pumpnom klipu potrebnu za podizanje tereta i broj punih pumpnih hodova potreban da se stol podigne za $\Delta z = 45\ \text{mm}$.

   :::: {.content-visible .mf1-hint-online when-format="html"}
   ::: {.callout-note collapse="true" data-hint-key="true"}
   ### Naputak
   teret raspodijeli na dva cilindra; iz $p = G/(2A_D)$ dobij $F_p = pA_d$, a broj hodova iz $nA_d s = 2A_D \Delta z$.
   :::
   ::::
   :::: {.content-visible .mf1-answer-online when-format="html"}
   ::: {.callout-tip collapse="true" data-answer-key="true"}
   ### Kontrolni rezultat

   $p \approx 0{,}93\ \text{MPa}$; $F_p \approx 238\ \text{N}$; $n = 16$ hodova.
   :::
   ::::
   **Skica:** da - pumpni klip, dva radna cilindra i vertikalni pomak stola $\Delta z$.

5. [**T3**]{#task-u01-rucna-pumpa-s-klipom-promjera-razvija-silu} Ručna pumpa s klipom promjera $d = 25\ \text{mm}$ razvija silu $F_p = 420\ \text{N}$. Dva radna cilindra promjera $D = 140\ \text{mm}$ nalaze se na istoj razini i podižu platformu. Odredi tlak u ulju, ukupno nosivo opterećenje platforme i ukupni hod pumpnog klipa potreban da se platforma podigne za $\Delta z = 30\ \text{mm}$.

   :::: {.content-visible .mf1-hint-online when-format="html"}
   ::: {.callout-note collapse="true" data-hint-key="true"}
   ### Naputak
   najprije izračunaj tlak iz $p = F_p/A_d$; zatim ukupno opterećenje iz $G = 2pA_D$, a ukupan hod pumpe iz volumne bilance $A_d s_p = 2A_D \Delta z$.
   :::
   ::::
   :::: {.content-visible .mf1-answer-online when-format="html"}
   ::: {.callout-tip collapse="true" data-answer-key="true"}
   ### Kontrolni rezultat

   $p \approx 856\ \text{kPa}$; $G \approx 26{,}3\ \text{kN}$; $s_p \approx 1{,}88\ \text{m}$.
   :::
   ::::
   **Skica:** da - pumpni klip, dva radna cilindra na istoj razini i nosiva platforma.

6. [**T4**]{#task-u01-hidraulicni-radni-stol-podupiru-tri-jednaka-cilindra} Hidraulični radni stol podupiru tri jednaka cilindra, svaki površine $A_L = 95\ \text{cm}^2$. Ulje dovodi pumpni klip promjera $d = 22\ \text{mm}$ na koji djeluje sila $F_p = 360\ \text{N}$. Odredi tlak u ulju, ukupno idealno opterećenje koje stol može nositi i ukupan idealni hod pumpnog klipa potreban da se stol podigne za $\Delta z = 18\ \text{mm}$. Za odluku o puštanju u rad uzmi da su izmjereni faktor prijenosa sile $\eta_F=0{,}86\pm0{,}04$ i volumetrijska učinkovitost $\eta_V=0{,}90\pm0{,}03$. Stol mora nositi najmanje $22{,}0\ \text{kN}$, a raspoloživi hod pumpe iznosi $1{,}60\ \text{m}$. Izračunaj nominalno i konzervativno korisno opterećenje i potreban hod te obrazloži zadovoljava li sustav oba zahtjeva u cijelom zadanom rasponu učinkovitosti.

   :::: {.content-visible .mf1-hint-online when-format="html"}
   ::: {.callout-note collapse="true" data-hint-key="true"}
   ### Naputak
   prvo izračunaj $A_p$ i tlak iz $p = F_p/A_p$; zatim idealno opterećenje iz $G = 3pA_L$, a idealni hod pumpe iz volumne bilance $A_p s_p = 3A_L \Delta z$. Za stvarni sustav vrijedi $G_{kor}=\eta_FG$ i $s_{p,st}=s_p/\eta_V$. Konzervativnu odluku donesi s $\eta_{F,min}$ i $\eta_{V,min}$, a ne samo sa srednjim vrijednostima.
   :::
   ::::
   :::: {.content-visible .mf1-answer-online when-format="html"}
   ::: {.callout-tip collapse="true" data-answer-key="true"}
   ### Kontrolni rezultat

   $p \approx 947\ \text{kPa}$; $G \approx 27{,}0\ \text{kN}$; $s_p \approx 1{,}35\ \text{m}$. Nominalno je $G_{kor}\approx23{,}2\ \text{kN}$ i $s_{p,st}\approx1{,}50\ \text{m}$, a konzervativno $G_{kor,min}\approx22{,}1\ \text{kN}$ i $s_{p,st,max}\approx1{,}55\ \text{m}$. Oba zadana brojčana kriterija jesu zadovoljena, ali s malim rezervama, približno $0{,}1\ \text{kN}$ i $0{,}05\ \text{m}$; to nije potpuna provjera stroja ni odobrenje za puštanje u rad.
   :::
   ::::
   **Skica:** da - pumpni klip, tri jednaka radna cilindra i vertikalni pomak radnog stola.
:::::

![Skice uz zadatke za vježbu — hidraulične preše, klipovi i radni cilindri (poglavlje 1).](../assets/print/u01_vjezbe_skice.svg){#fig-u01-vjezbe fig-align="center" fig-alt="Skice uz zadatke za vježbu — hidraulične preše, klipovi i radni cilindri (poglavlje 1)."}

::: {.mf1-zavrsni-okvir}
<p class="mf1-box-label">Za ponijeti iz poglavlja</p>

**Sažeta provjera prije računa**

- Treba razdvojiti gustoću, specifičnu težinu i relativnu gustoću.
- Treba razlikovati silu, tlak i težinsku silu.
- Kod klipova treba razlikovati prenosi li se isti tlak ili ista sila.
- Površine treba pretvoriti u kvadratne metre prije računa.
- Na kraju treba provjeriti jesu li sila i pomak fizikalno konzistentni.

**Najčešća pogreška**

Najčešća pogreška u <span class="mf1-ch-ref"><span class="mf1-ch-code">pog. 1</span><span class="mf1-ch-title">Osnove fluida i Pascalov zakon</span></span> nije algebra nego pogrešna identifikacija fizikalne veličine. Ako se uzme $\rho$ umjesto $\gamma$, tlak umjesto sile ili isti tlak zamijeni istom silom na oba klipa, cijeli račun može izgledati uredno, a biti fizikalno pogrešan.

**Nakon ovoga poglavlja mora biti moguće**

1. razlikovati fluid od krutoga tijela na razini modela.
2. razlikovati gustoću, specifičnu težinu, relativnu gustoću i tlak.
3. primijeniti Pascalov zakon na jednostavan hidraulični sustav i protumačiti posljedice za silu i pomak.

**U tehnici to znači**

Hidraulična dizalica, preša ili kormilarski pogon rade pouzdano samo ako je jasno što je tlak, a što sila te na kojoj se površini taj tlak pretvara u radni učinak. Upravo zato ovo poglavlje nije uvodna formalnost, nego temelj za čitanje cijelog hidrauličnog sklopa.

**Granica modela**

Pascalov zakon u ovom obliku vrijedi kao idealizacija zatvorenog mirujućeg fluida. U stvarnim sustavima odziv mijenjaju stlačivost fluida, elastičnost vodova, unutarnje propuštanje i gubici u ventilima, pa se stvarna sila i pomak ne prenose savršeno.

<span class="mf1-ch-ref"><span class="mf1-ch-code">pog. 1</span><span class="mf1-ch-title">Osnove fluida i Pascalov zakon</span></span> uspostavlja temeljni jezik cijeloga kolegija. Kad su ovdje jasni tlak, gustoća i Pascalov zakon, kasnija poglavlja o hidrostatici, energiji i strujanju čitaju se sigurnije i bez miješanja osnovnih veličina.
:::

::: {.mf1-numerika}
<p class="mf1-box-label">Numerički most</p>

**Gdje ovo živi u numerici.** Tlak kao skalarno polje $p(x,y,z)$ — temeljni objekt koji svaki CFD solver mora prije svega *postaviti*. Pojam tlaka u kontinuumu i Pascalov zakon su upravo razlog zašto se u nestlačivom CFD-u tlak ne marsira u vremenu, nego se rješava globalno po cijeloj domeni.

**Što numerički alat radi s tim.** Na početku simulacije postavlja se *inicijalni uvjet tlaka* — najčešće jednoliko polje ili hidrostatska raspodjela iz idućeg poglavlja. Promjene na rubu (klip, ulaz crpke, ventil) propagiraju se kroz mrežu kontrolnih volumena unutar jedne iteracije sprege tlaka i brzine.

**Tipičan scenarij.** U industrijskom hidrauličkom sustavu CFD se rijetko primjenjuje na samu Pascalovu prijenosnu silu — ona je analitički rješiva. Vrijednost numerike pojavljuje se onda kad fluid prolazi uskim kanalima, kroz ventile ili kada se promatra dinamika tlačnog vala (vodeni udar pri naglom zatvaranju ventila): tada lokalna polja brzine, tlaka i mogućih kavitacijskih zona postaju netrivijalna, a analitička procjena prestaje biti dovoljna.

> *Nije gradivo MF1. U kasnijim kolegijima posvećenima računalnoj dinamici fluida opisani sadržaj postat će poznat teren.*
:::
