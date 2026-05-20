## Sažetak formula, oznaka i tipičnih jedinica

Ovaj dodatak nije zamjena za glavna poglavlja. Njegova je svrha dati brzi pregled najčešćih oznaka i radnih relacija koje se u udžbeniku stalno ponavljaju. Formulu ovdje treba čitati kao podsjetnik na zapis i jedinice, a ne kao dozvolu da se preskoče model i uvjeti primjene iz glavnog poglavlja.

## Kako koristiti ovaj sažetak

Najsigurniji redoslijed je:

1. prepoznati kojoj temi formula pripada
2. provjeriti radi li se o tlaku, sili, gubitku, protoku ili bezdimenzijskoj veličini
3. tek onda koristiti zapis iz sažetka

Ako nije jasno zašto formula vrijedi, prioritet uvijek ima odgovarajuće poglavlje `U01-U13`, a ne ovaj dodatak.

## Najčešće oznake

| Oznaka | Značenje | Tipična jedinica |
| --- | --- | --- |
| $\rho$ | gustoća | kg/m$^3$ |
| $\gamma$ | specifična težina, $\rho g$ | N/m$^3$ |
| $\mu$ | dinamička viskoznost | Pa s |
| $\nu$ | kinematička viskoznost, $\mu/\rho$ | m$^2$/s |
| $\sigma$ | površinska napetost | N/m |
| $p$ | tlak | Pa |
| $\Delta p$ | razlika tlakova ili tlakovni skok | Pa |
| $p_0$ | stagnacijski tlak ili poznati referentni tlak | Pa |
| $p_{M0}$ | jednoliki manometarski pretlak plina iznad tekućine | Pa |
| $z$ | geodetska visina | m |
| $h$ | visina stupca ili gubitak izražen u metrima fluida | m |
| $H$ | zadana razlika razina ili raspoloživa energijska visina | m |
| $g_{eff}$ | efektivno ubrzanje u relativnom mirovanju | m/s$^2$ |
| $A$ | površina presjeka ili plohe | m$^2$ |
| $A_p$ | površina otvora ili pukotine | m$^2$ |
| $V$ | volumen | m$^3$ |
| $v$ | srednja ili lokalna brzina | m/s |
| $u$ | brzina gibajućeg elementa ili lopatice | m/s |
| $v_{rel}$ | relativna brzina fluida prema gibajućem elementu | m/s |
| $Q$ | volumenski protok | m$^3$/s |
| $Q_p$ | protok kroz pukotinu ili servisni ispust | m$^3$/s |
| $\dot{m}$ | maseni protok | kg/s |
| $D$ | promjer cijevi | m |
| $L$ | duljina cijevi | m |
| $y_R$ | položaj hvatista rezultante ili centra tlaka | m |
| $Re$ | Reynoldsov broj | - |
| $\varepsilon$ | apsolutna hrapavost cijevi | m |
| $\lambda$ | Darcyjev koeficijent trenja | - |
| $\xi$ | lokalni koeficijent gubitka | - |
| $C_d$ | koeficijent istjecanja otvora | - |

## U01-U02: Osnovne veličine, tlak, viskoznost i kapilarnost

| Formula | Konkretan brojčani primjer |
| --- | --- |
| $\rho = m/V$ | Voda na $20\,^\circ\text{C}$: $m = 1\,\text{kg}$ u $V = 10^{-3}\,\text{m}^3$ → $\rho = 1000\,\text{kg/m}^3$. |
| $\gamma = \rho g$ | Voda: $\gamma = 1000 \cdot 9{,}81 \approx 9810\,\text{N/m}^3$. |
| $s = \rho / \rho_{voda}$ | Živa: $s = 13\,600/1000 = 13{,}6$. |
| $p = F_n / A$ | $F = 100\,\text{N}$ na $A = 10\,\text{cm}^2$ → $p = 10^5\,\text{Pa} = 100\,\text{kPa}$. |
| $\Delta p = F_1/A_1 = F_2/A_2$ (Pascalova preša) | $F_1 = 50\,\text{N}$ na $A_1 = 5\,\text{cm}^2$ daje istu $\Delta p$ kao $F_2 = 500\,\text{N}$ na $A_2 = 50\,\text{cm}^2$. |
| $A_p s_p = \sum_i A_i s_i$ (Pascalova bilanca pomaka) | Malim klipom $A_1 = 1\,\text{cm}^2$ pomaknutim za $s_1 = 10\,\text{cm}$ veliki klip $A_2 = 10\,\text{cm}^2$ pomakne se za $s_2 = 1\,\text{cm}$. |
| $\tau = \mu\,dv/dy$ | Maslinovo ulje $\mu \approx 0{,}08\,\text{Pa s}$, $dv/dy = 100\,\text{s}^{-1}$ → $\tau = 8\,\text{Pa}$. |
| $\nu = \mu / \rho$ | Voda na $20\,^\circ\text{C}$: $\nu \approx 10^{-6}\,\text{m}^2/\text{s}$; zrak: $\nu \approx 1{,}5 \cdot 10^{-5}\,\text{m}^2/\text{s}$. |
| $h = 4\sigma\cos\theta / (\rho g d)$ | Voda u staklenoj kapilari $d = 1\,\text{mm}$, $\theta \approx 0$: $h \approx 30\,\text{mm}$. |
| $\Delta p = 4\sigma / d$ (Young-Laplace) | Kapljica vode $d = 1\,\text{mm}$, $\sigma = 0{,}072\,\text{N/m}$: $\Delta p \approx 288\,\text{Pa}$. |

## U03-U07: Hidrostatika, plohe i uzgon

| Formula | Konkretan brojčani primjer |
| --- | --- |
| $dp/dz = -\rho g$ | Voda: tlak raste oko $9810\,\text{Pa}$ po metru dubine (≈ $1\,\text{bar}$ na svakih $10\,\text{m}$). |
| $p = p_0 + \rho g h$ | Pri $p_0 = 101\,325\,\text{Pa}$ na dubini $h = 5\,\text{m}$ vode: $p \approx 150\,\text{kPa}$. |
| $p_{aps} = p_{atm} + p_{man}$ | Manometar pokazuje $50\,\text{kPa}$ → apsolutni tlak $\approx 151\,\text{kPa}$. |
| $\tan\theta = a/g$ (slobodna površina pri linijskom ubrzanju) | Spremnik koji ubrzava $a = 2\,\text{m/s}^2$: slobodna površina nagnuta za $\theta \approx 11{,}5^\circ$. |
| $g_{eff} = \sqrt{g^2 + a^2}$ | Pri $a = 5\,\text{m/s}^2$: $g_{eff} \approx 11{,}0\,\text{m/s}^2$. |
| $F = \rho g z_T A$ (sila na ravnu plohu) | Pravokutna zaklopka $2 \times 3\,\text{m}$, težište na dubini $z_T = 3{,}5\,\text{m}$: $F \approx 205\,\text{kN}$. |
| $F_H = \rho g z_T A_{proj}$ | Vertikalna projekcija zakrivljene plohe iste površine i težišta daje istu $F_H$ kao kod ravne plohe. |
| $F_V = \rho g V$ | Imaginarni "vodeni stupac" volumena $V = 1\,\text{m}^3$ iznad zakrivljene plohe: $F_V \approx 9810\,\text{N}$. |
| $F_R = \sqrt{F_H^2 + F_V^2}$ | $F_H = 20\,\text{kN}$ i $F_V = 15\,\text{kN}$: $F_R = 25\,\text{kN}$. |
| $y_R = \sum_i F_i y_i / \sum_i F_i$ (momentna superpozicija) | Dva doprinosa $F_1 = 10\,\text{kN}$ na $y_1 = 2\,\text{m}$ i $F_2 = 30\,\text{kN}$ na $y_2 = 5\,\text{m}$: $y_R = 170/40 = 4{,}25\,\text{m}$. |
| $F_U = \rho g V_{istisnuto}$ (Arhimedov zakon) | Tijelo istisne $V = 0{,}1\,\text{m}^3$ vode: $F_U \approx 981\,\text{N}$. |
| $G = F_U$ (uvjet plivanja) | Brod mase $10\,000\,\text{kg}$ uravnotežen je istisnutim volumenom od $\approx 10{,}02\,\text{m}^3$ vode. |

## U08-U10: Kontinuitet, Bernoulli i gubici

| Formula | Konkretan brojčani primjer |
| --- | --- |
| $Q = A v$ | Cijev $D = 50\,\text{mm}$ ($A \approx 19{,}6\,\text{cm}^2$), $v = 2\,\text{m/s}$ → $Q \approx 3{,}93\,\text{L/s}$. |
| $Q_{in} - Q_{out} = dV/dt$ | Ako je $Q_{in} = 2\,\text{L/s}$ i $Q_{out} = 1{,}5\,\text{L/s}$: spremnik akumulira $0{,}5\,\text{L/s}$. |
| $\dot{m} = \rho Q$ | Voda, $Q = 0{,}01\,\text{m}^3/\text{s}$: $\dot{m} = 10\,\text{kg/s}$. |
| $p/(\rho g) + v^2/(2g) + z = \text{const.}$ (Bernoulli, idealan fluid) | Slobodna površina spremnika na $z_1 = 10\,\text{m}$, $v_1 \approx 0$ ima istu ukupnu energiju kao izlazni mlaz na $z_2 = 0$, $v_2 \approx 14\,\text{m/s}$. |
| $p_1/(\rho g) + v_1^2/(2g) + z_1 = p_2/(\rho g) + v_2^2/(2g) + z_2 + h_w$ (Bernoulli, realan fluid) | Razlika visina $z_1 - z_2 = 6\,\text{m}$ pri $h_w = 2\,\text{m}$: $4\,\text{m}$ ostaje na raspolaganju za pretvorbu u kinetičku i tlačnu energiju. |
| $v_0 = \sqrt{2gH}$ (Torricelli) | Spremnik visine $H = 5\,\text{m}$: $v_0 \approx 9{,}9\,\text{m/s}$. |
| $x = 2\sqrt{h(H-h)}$ (vodoravni domet mlaza) | $H = 1\,\text{m}$, otvor na visini $h = 0{,}5\,\text{m}$ od dna: $x_{\max} = 1\,\text{m}$. |
| $h_l = \lambda(L/D)(v^2/2g)$ (Darcy-Weisbach) | Cijev $L = 100\,\text{m}$, $D = 0{,}1\,\text{m}$, $\lambda = 0{,}025$, $v = 2\,\text{m/s}$: $h_l \approx 5{,}1\,\text{m}$. |
| $h_{loc} = \xi v^2/(2g)$ | Koljeno $\xi = 0{,}9$, $v = 3\,\text{m/s}$: $h_{loc} \approx 0{,}41\,\text{m}$. |
| $h_w = h_l + \sum h_{loc}$ | Cijev $h_l = 5\,\text{m}$ + tri koljena po $0{,}4\,\text{m}$: $h_w = 6{,}2\,\text{m}$. |
| $p_0 - p = \tfrac{1}{2}\rho v^2$ (Pitot, dinamički tlak) | Voda, $v = 10\,\text{m/s}$: $\Delta p = 50\,\text{kPa}$. |
| $v = \sqrt{2(p_0 - p)/\rho}$ | Voda, $\Delta p = 5\,\text{kPa}$: $v \approx 3{,}16\,\text{m/s}$. |

## U11-U13: Količina gibanja, lopatice, potisak i cjevovodi

| Formula | Konkretan brojčani primjer |
| --- | --- |
| $\sum \vec{F} = \dot{m}(\vec{v}_{izl} - \vec{v}_{ul})$ | Mlaz $\dot{m} = 5\,\text{kg/s}$ skreće za $90^\circ$ pri $v = 20\,\text{m/s}$: $|F_x| = |F_y| = 100\,\text{N}$. |
| $v_{rel} = v - u$ | Mlaz $v = 30\,\text{m/s}$, obodna brzina lopatice $u = 12\,\text{m/s}$: $v_{rel} = 18\,\text{m/s}$. |
| $\dot{m}_{rel} = \rho A v_{rel}$ | Mlaz $A = 1\,\text{cm}^2$ vode, $v_{rel} = 18\,\text{m/s}$: $\dot{m}_{rel} = 1{,}8\,\text{kg/s}$. |
| $F \approx \dot{m} v$ (mlaz na nepokretnu plohu) | $\dot{m} = 2\,\text{kg/s}$, $v = 25\,\text{m/s}$: $F = 50\,\text{N}$. |
| $F \approx 2\dot{m} v$ (mlaz potpuno skreće za $180^\circ$) | Isti primjer: $F = 100\,\text{N}$. |
| $P = F u$ (snaga predana lopatici) | Lopatica $F = 1\,\text{kN}$, obodna brzina $u = 10\,\text{m/s}$: $P = 10\,\text{kW}$. |
| $Re = vD/\nu$ | Voda u cijevi $D = 50\,\text{mm}$, $v = 1\,\text{m/s}$, $\nu = 10^{-6}\,\text{m}^2/\text{s}$: $Re = 5 \cdot 10^4$ (turbulentno). |
| $\lambda = 64/Re$ (laminarno strujanje) | $Re = 1500$: $\lambda \approx 0{,}043$. |
| $h_w = \lambda(L/D)(v^2/2g) + \sum \xi v^2/(2g)$ | Cijev s linijskim gubitkom $5\,\text{m}$ i tri lokalna otpora po $0{,}4\,\text{m}$: $h_w = 6{,}2\,\text{m}$. |
| $Q_p = C_d A_p \sqrt{2gH}$ (istjecanje kroz otvor) | Otvor $A_p = 1\,\text{cm}^2$, $C_d = 0{,}62$, $H = 5\,\text{m}$: $Q_p \approx 0{,}61\,\text{L/s}$. |
| $A_p = Q_p / (C_d \sqrt{2gH})$ | Za $Q_p = 1\,\text{L/s}$, $H = 4\,\text{m}$: $A_p \approx 1{,}82\,\text{cm}^2$. |
| $h_{w,tot} = \sum_i h_{w,i}$ (serijski spoj) | Tri dionice s gubicima $2{,}0$, $1{,}5$ i $0{,}8\,\text{m}$: ukupno $h_{w,tot} = 4{,}3\,\text{m}$. |
| $Q_{tot} = \sum_i Q_i$, $h_{w,1} = h_{w,2}$ (paralelni spoj) | Dvije grane: kraća prima $Q_1 = 6\,\text{L/s}$, dulja $Q_2 = 4\,\text{L/s}$ za isti pad od $3\,\text{m}$. |

U turbulentnom području $\lambda$ više nije funkcija samo Reynoldsovog broja, nego i relativne hrapavosti $\varepsilon / D$ — koeficijent se očitava s Moodyjeva dijagrama.

## Tipične zamjene jedinica koje treba zaustaviti odmah

- $\rho$ nije isto što i $\gamma$
- tlak u Pa nije isto što i sila u N
- $Q$ i $\dot{m}$ nisu ista veličina
- $\mu$ i $\nu$ nisu iste jedinice ni isto fizikalno značenje
- gubitak $h_w$ u metrima nije isto što i pad tlaka u Pa, iako su povezani

::: {.mf1-checklist}
### Kako koristiti sažetak bez mehaničkog uvrstavanja

- Najprije prepoznaj temu: tlak, sila, protok, energija ili gubitak.
- Provjeri jesu li jedinice konzistentne prije uvrstavanja brojeva.
- Tek tada koristi relaciju iz sažetka.
- Ako nije jasno zašto formula vrijedi, vrati se u glavno poglavlje.
:::

::: {.mf1-warning}
<p class="mf1-box-label">Najčešća pogreška</p>

Najčešća pogreška pri radu sa sažetkom nije pogrešna formula nego pogrešan kontekst. Ispravan zapis primijenjen na krivi model daje fizikalno pogrešan rezultat jednako sigurno kao i kriva algebra.
:::

::: {.mf1-mini-summary}
<p class="mf1-box-label">Sažetak za ponijeti</p>

<span class="mf1-ch-ref"><span class="mf1-ch-code">D01</span><span class="mf1-ch-title">Sažetak formula i oznaka</span></span> je karta, a ne zamjena za put. Služi za brzu provjeru oznaka, jedinica i najčešćih relacija, ali glavni smisao svake formule i dalje dolazi iz odgovarajućeg poglavlja udžbenika. Stupac konkretnih brojčanih primjera uz svaku formulu pomaže odmah ustanoviti red veličine i jedinice rezultata prije punog izračuna.
:::








