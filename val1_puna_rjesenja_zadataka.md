# Val 1 - puna rjesenja zadataka

> Status u svibnju 2026.: ovaj dokument ostaje arhivska pratnja prvog vala javnih prerada. Puna rjesenja vise nisu prijelazni materijal, nego povijesna podloga za zadatke koji su vec preseljeni u aktivna `source` poglavlja.

## Svrha dokumenta

Ovo je prvi puni worked-solution izlaz za javne prerade iz `val1_javne_prerade_zadataka.md`. Rjesenja su izvedena od nule i pisana tako da se kasnije mogu rastaviti i preseliti u pripadna poglavlja `U04`, `U07` i `U12`.

## Status dokumenta

- broj punih rjesenja: `3`
- obuhvat: `VAL1-01`, `VAL1-02`, `VAL1-03`
- svrha: zakljucati numericki, metodski i urednicki prag prve tri prerade

---

## VAL1-01 | U04 | Procesna kada na automatskoj platformi

### Model i pretpostavke

Koristi se model relativnog mirovanja otvorenog spremnika pri stalnom translatornom ubrzanju. U takvom stanju slobodna povrsina je ravna, a njezin nagib je odreden odnosom

$$\tan \theta = \frac{a}{g}$$

pa razlika razina fluida na krajevima spremnika iznosi

$$\Delta h = \frac{aL}{g}$$

Sve dok nema prelijevanja, srednja visina fluida ostaje jednaka pocetnoj srednjoj visini $h_0$.

### Rjesenje

#### 1. Najvece dopusteno ubrzanje

U granicnom stanju tekucina upravo dodiruje gornji rub straznje stijenke, pa je

$$h_{straznja} = H = 0{,}72\ \text{m}$$

Kako je srednja visina prije ubrzanja jednaka $h_0 = 0{,}54\ \text{m}$, vrijedi

$$\frac{h_{straznja} + h_{prednja}}{2} = h_0$$

odakle slijedi

$$h_{prednja} = 2h_0 - h_{straznja} = 2 \cdot 0{,}54 - 0{,}72 = 0{,}36\ \text{m}$$

Razlika razina tada iznosi

$$\Delta h = h_{straznja} - h_{prednja} = 0{,}72 - 0{,}36 = 0{,}36\ \text{m}$$

Iz relacije za nagib slobodne povrsine slijedi

$$a_{max} = g \frac{\Delta h}{L} = 9{,}81 \cdot \frac{0{,}36}{1{,}80} = 1{,}962\ \text{m/s}^2$$

Zaokruzeno,

$$a_{max} \approx 1{,}96\ \text{m/s}^2$$

#### 2. Visine uz stijene u granicnom stanju

Dobiveno je

$$h_{straznja} = 0{,}72\ \text{m}, \qquad h_{prednja} = 0{,}36\ \text{m}$$

#### 3. Rezultantna sila na straznju stijenku

Na straznjoj stijenci tlak raste linearno s dubinom ispod lokalne slobodne povrsine. Buduci da slobodna povrsina u granicnom stanju prolazi kroz gornji rub straznje stijenke, dobiva se trokutasta raspodjela tlaka po visini $h_{straznja}$.

Rezultantna sila na vertikalnu stijenku sirine $B$ iznosi

$$F_R = \frac{1}{2} \rho g B h_{straznja}^2$$

Uvrstavanjem podataka:

$$F_R = \frac{1}{2} \cdot 970 \cdot 9{,}81 \cdot 0{,}95 \cdot 0{,}72^2 = 2343\ \text{N}$$

odnosno

$$F_R \approx 2{,}34\ \text{kN}$$

Ako se zeli i polozaj hvatiste, ono je za trokutastu raspodjelu na udaljenosti $h_{straznja}/3 = 0{,}24\ \text{m}$ od dna stijenke.

### Brza provjera rezultata

1. Ubrzanje je oko $0{,}20g$, sto je sasvim razumno za platformu koja jos treba zadrzati tekućinu bez prelijevanja.
2. Prednja visina ostaje pozitivna, pa se dno ne "ogoljuje" s prednje strane.
3. Sila reda velicine nekoliko kilonjutna razumna je za stijenku sirine gotovo jednog metra i dubine reda $0{,}7\ \text{m}$.

### Najcesca greska

Najcesca greska je uzeti da je u granicnom stanju $\Delta h = H - h_0$. To nije tocno. Granicno stanje se mora citati preko dvaju uvjeta istodobno: jedan rub dodiruje vrh spremnika, a srednja visina ostaje jednaka pocetnoj vrijednosti dok nema prelijevanja.

---

## VAL1-02 | U07 | Plutajuca servisna platforma s pomaknutim kompresorom

### Model i pretpostavke

Platforma se promatra kao kruto prizmatsko tijelo pravokutnog tlocrta i ravnog dna. U ravnotezi vrijedi:

1. suma vertikalnih sila je jednaka nuli
2. suma momenata oko uzduzne osi simetrije je jednaka nuli

Kako je dno ravno, gaz po sirini platforme mijenja se linearno, pa je srednja uronjenost jednaka aritmetickoj sredini lijevog i desnog urona.

### Rjesenje

#### 1. Ukupni istisnuti volumen vode

Srednja uronjenost platforme iznosi

$$h_m = \frac{h_L + h_D}{2} = \frac{0{,}34 + 0{,}22}{2} = 0{,}28\ \text{m}$$

Kako je tlocrt pravokutan, istisnuti volumen glasi

$$V = L B h_m = 3{,}10 \cdot 1{,}00 \cdot 0{,}28 = 0{,}868\ \text{m}^3$$

Dakle,

$$V = 0{,}868\ \text{m}^3$$

To odgovara istisnutoj masi vode od priblizno

$$m_{ist} = \rho V = 998 \cdot 0{,}868 \approx 866\ \text{kg}$$

sto je u skladu s ukupnom masom platforme i kompresora uz zaokruzenje zadanih urona na dvije decimale.

#### 2. Udaljenost tezista kompresora od osi simetrije

Najprije treba odrediti bocni pomak tezista istisnine. Za pravokutnu platformu s linearnom promjenom urona po sirini vrijedi

$$y_B = \frac{B\,(h_L - h_D)}{12 h_m}$$

Uvrstavanjem:

$$y_B = \frac{1{,}00 \cdot (0{,}34 - 0{,}22)}{12 \cdot 0{,}28} = 0{,}0357\ \text{m}$$

Dakle, pravac djelovanja sile uzgona pomaknut je za oko $3{,}57\ \text{cm}$ prema dublje uronjenoj strani.

U ravnotezi momenata oko osi simetrije vrijedi

$$F_U y_B = m_k g e$$

Buduci da je sila uzgona jednaka ukupnoj tezini platforme i kompresora,

$$F_U = (m_p + m_k) g$$

slijedi

$$ (m_p + m_k) g y_B = m_k g e $$

odakle se gravitacija skracuje i dobiva

$$e = \frac{m_p + m_k}{m_k} y_B$$

Numericki:

$$e = \frac{676 + 190}{190} \cdot 0{,}0357 = 0{,}1628\ \text{m}$$

odnosno

$$e \approx 0{,}163\ \text{m}$$

Teziste kompresora nalazi se oko $16{,}3\ \text{cm}$ od uzduzne osi simetrije prema dublje uronjenom rubu.

#### 3. Povecanje srednje uronjenosti nakon postavljanja kompresora

Povecanje srednjeg gaza uzrokuje samo dodatna masa kompresora. Zato vrijedi

$$\Delta h_m = \frac{m_k}{\rho L B} = \frac{190}{998 \cdot 3{,}10 \cdot 1{,}00} = 0{,}0614\ \text{m}$$

odnosno

$$\Delta h_m \approx 6{,}14\ \text{cm}$$

Ako se zeli i provjera, pocetni srednji gaz platforme bez kompresora bio bi

$$h_{m,0} = \frac{676}{998 \cdot 3{,}10 \cdot 1{,}00} \approx 0{,}219\ \text{m}$$

a konacni srednji gaz je $0{,}280\ \text{m}$, pa je razlika upravo oko $0{,}061\ \text{m}$.

### Brza provjera rezultata

1. Veci uron na jednoj strani mora znaciti da je teziste kompresora pomaknuto na tu stranu, a dobiveni rezultat to i daje.
2. Bocni pomak kompresora manji je od polovice sirine platforme, pa je geometrijski moguc.
3. Povecanje srednje uronjenosti reda nekoliko centimetara za teret od $190\ \text{kg}$ na platformi reda nekoliko kvadratnih metara potpuno je razumno.

### Najcesca greska

Najcesca greska je pomijesati dvije razlicite stvari: srednju uronjenost i nagib. Srednja uronjenost dolazi iz ukupne tezine, dok razlika urona lijevog i desnog ruba dolazi iz momentne ravnoteze.

---

## VAL1-03 | U12 | Vodilica mlaza na ispitnom stolu

### Model i pretpostavke

Promatra se stacionarni kontrolni volumen oko vodilice u horizontalnoj ravnini. Pretpostavlja se:

1. tlak na ulazu i izlazu jednak je atmosferskom, pa u jednadzbi kolicine gibanja radimo s manometarskim tlakom nula
2. tezina vode unutar vodilice zanemariva je u odnosu na horizontalne sile
3. smjer izlaza definiran je tako da mlaz nakon skretanja ide prema pozitivnom smjeru osi $y$

Koordinatni sustav uzima se tako da je ulazni mlaz usmjeren u pozitivnom smjeru osi $x$.

### Rjesenje

#### 1. Maseni protok kroz sapnicu

Povrsina pravokutnog izlaza sapnice iznosi

$$A = b h = 0{,}036 \cdot 0{,}014 = 5{,}04 \cdot 10^{-4}\ \text{m}^2$$

Maseni protok je

$$\dot{m} = \rho A v_1 = 998 \cdot 5{,}04 \cdot 10^{-4} \cdot 24 = 12{,}07\ \text{kg/s}$$

Dakle,

$$\dot{m} \approx 12{,}1\ \text{kg/s}$$

#### 2. Horizontalne komponente sile koju fluid vrsi na vodilicu

Ulazna brzina je

$$\vec{v}_1 = (24,\ 0)\ \text{m/s}$$

Izlazna brzina ima iznos $v_2 = 19\ \text{m/s}$ i kut $\beta = 120^\circ$ u odnosu na ulazni smjer, pa su njezine komponente

$$\vec{v}_2 = (19 \cos 120^\circ,\ 19 \sin 120^\circ) = (-9{,}5,\ 16{,}45)\ \text{m/s}$$

Jednadzba kolicine gibanja za silu vodilice na fluid glasi

$$\vec{F}_{v\to f} = \dot{m}(\vec{v}_2 - \vec{v}_1)$$

pa dobivamo

$$\vec{F}_{v\to f} = 12{,}07 \cdot [(-9{,}5 - 24),\ (16{,}45 - 0)]$$

odnosno

$$\vec{F}_{v\to f} = (-404{,}4,\ 198{,}6)\ \text{N}$$

To je sila koju vodilica vrsi na fluid. Zadatak trazi silu koju fluid vrsi na vodilicu, pa treba promijeniti predznak:

$$\vec{F}_{f\to v} = -\vec{F}_{v\to f} = (404{,}4,\ -198{,}6)\ \text{N}$$

Dakle, komponente sile fluida na vodilicu su

$$F_x \approx 404\ \text{N}, \qquad F_y \approx -199\ \text{N}$$

To znaci da fluid gura vodilicu pretezno udesno i prema dolje u nacrtanom koordinatnom sustavu.

#### 3. Reakcija nosaca vodilice

Da bi vodilica mirovala, nosac mora preuzeti reakciju jednaku po iznosu i suprotnu sili fluida na vodilicu:

$$\vec{R} = -\vec{F}_{f\to v} = (-404{,}4,\ 198{,}6)\ \text{N}$$

Iznos reakcije je

$$R = \sqrt{R_x^2 + R_y^2} = \sqrt{404{,}4^2 + 198{,}6^2} = 450{,}6\ \text{N}$$

odnosno

$$R \approx 451\ \text{N}$$

Kut reakcije u odnosu na negativni smjer osi $x$ iznosi

$$\alpha = \arctan \left( \frac{198{,}6}{404{,}4} \right) = 26{,}2^\circ$$

Dakle, nosac mora preuzeti reakciju od oko $451\ \text{N}$ usmjerenu $26{,}2^\circ$ iznad negativnog smjera osi $x$.

Ako se u skici odabere zrcalna orijentacija izlaznog mlaza, iznos reakcije ostaje isti, a mijenja se samo predznak komponente po osi $y$.

### Brza provjera rezultata

1. Maseni protok reda desetak kilograma u sekundi razuman je za ovakav presjek i brzinu mlaza.
2. Komponenta po osi $x$ mora biti dominantna jer mlaz mijenja i smjer i iznos brzine, pa je ulazna komponenta $+24\ \text{m/s}$ znatno veca od izlazne projekcije na istu os.
3. Reakcija reda nekoliko stotina njutna razumna je za mlaz brzine reda dvadesetak metara u sekundi.

### Najcesca greska

Najcesca greska nije u racunu masenog protoka, nego u znaku sile. Prvo se u jednadzbi kolicine gibanja dobiva sila vodilice na fluid. Tek nakon toga smije se preci na silu fluida na vodilicu i na reakciju nosaca.

---

## Operativna napomena

Ova tri puna rjesenja vise nisu samo staging-materijal: preseljena su u radne `source` verzije poglavlja `U04`, `U07` i `U12`, zajedno s pripadajucim statickim skicama. Sljedeci korak je prosiriti ta poglavlja novim zadatkovnim blokovima istog kucnog stila.