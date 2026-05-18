## Brza mapa formula, oznaka i tipičnih jedinica

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

$$
\rho = \frac{m}{V}
$$

$$
\gamma = \rho g
$$

$$
s = \frac{\rho}{\rho_{voda}}
$$

$$
p = \frac{F_n}{A}
$$

$$
\Delta p = \frac{F_1}{A_1} = \frac{F_2}{A_2}
$$

$$
A_p s_p = \sum_i A_i s_i
$$

$$
{}\tau = \mu \frac{dv}{dy}
$$

$$
\nu = \frac{\mu}{\rho}
$$

$$
h = \frac{4\sigma \cos\theta}{\rho g d}
$$

$$
\Delta p = \frac{4\sigma}{d}
$$

## U03-U07: Hidrostatika, plohe i uzgon

$$
\frac{dp}{dz} = -\rho g
$$

$$
p = p_0 + \rho g h
$$

$$
p_{aps} = p_{atm} + p_{man}
$$

$$
{}\tan\theta = \frac{a}{g}
$$

$$
g_{eff} = \sqrt{g^2 + a^2}
$$

$$
F = \rho g z_T A
$$

$$
F_H = \rho g z_T A_{proj}
$$

$$
F_V = \rho g V
$$

$$
F_R = \sqrt{F_H^2 + F_V^2}
$$

Za kombinaciju više doprinosa rezultanti vrijedi momentna superpozicija:

$$
y_R = \frac{\sum_i F_i y_i}{\sum_i F_i}
$$

$$
F_U = \rho g V_{istisnuto}
$$

$$
G = F_U
$$

## U08-U10: Kontinuitet, Bernoulli i gubici

$$
Q = A v
$$

$$
Q_{in} - Q_{out} = \frac{dV}{dt}
$$

$$
\dot{m} = \rho Q
$$

$$
\frac{p}{\rho g} + \frac{v^2}{2g} + z = \text{const.}
$$

$$
\frac{p_1}{\rho g} + \frac{v_1^2}{2g} + z_1 = \frac{p_2}{\rho g} + \frac{v_2^2}{2g} + z_2 + h_w
$$

Za slobodni mlaz iz velikog spremnika u idealnom modelu vrijedi:

$$
v_0 = \sqrt{2g(H-h)}
$$

$$
x = 2\sqrt{h(H-h)}
$$

$$
h_w = h_l + \sum h_{loc}
$$

$$
h_l = \lambda \frac{L}{D} \frac{v^2}{2g}
$$

$$
h_{loc} = \xi \frac{v^2}{2g}
$$

$$
p_0 - p = \frac{1}{2} \rho v^2
$$

$$
v = \sqrt{\frac{2(p_0 - p)}{\rho}}
$$

## U11-U13: Količina gibanja, lopatice, potisak i cjevovodi

$$
\sum \vec{F} = \dot{m}(\vec{v}_{izl} - \vec{v}_{ul})
$$

$$
v_{rel} = v - u
$$

$$
\dot{m}_{rel} = \rho A v_{rel}
$$

$$
F \approx \dot{m} v
$$

$$
F \approx 2\dot{m} v
$$

$$
P = Fw
$$

$$
Re = \frac{\rho v D}{\mu} = \frac{vD}{\nu}
$$

$$
\lambda = \frac{64}{Re}
$$

U turbulentnom području $\lambda$ više nije funkcija samo Reynoldsovog broja, nego i relativne hrapavosti $\varepsilon / D$.

$$
h_w = \lambda \frac{L}{D} \frac{v^2}{2g} + \sum \xi \frac{v^2}{2g}
$$

Za procjenu istjecanja kroz pukotinu ili servisni ispust pri poznatoj tlačnoj visini $H$ vrijedi:

$$
Q_p = C_d A_p \sqrt{2gH}
$$

$$
A_p = \frac{Q_p}{C_d \sqrt{2gH}}
$$

Za serijski spoj cjevovoda vrijedi: isti protok kroz sve dionice, a ukupni gubitak jednak je zbroju pojedinačnih gubitaka.

$$
h_{w,tot} = \sum_i h_{w,i}
$$

Za paralelni spoj vrijedi: ukupni protok se dijeli po granama, a gubitak energije između istih čvorova mora biti jednak u svakoj grani.

$$
Q_{tot} = \sum_i Q_i
$$

$$
h_{w,1} = h_{w,2} = \cdots
$$

## tipične zamjene jedinica koje treba zaustaviti odmah

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

<span class="mf1-ch-ref"><span class="mf1-ch-code">D01</span><span class="mf1-ch-title">Sažetak formula i oznaka</span></span> je karta, a ne zamjena za put. Služi za brzu provjeru oznaka, jedinica i najčešćih relacija, ali glavni smisao svake formule i dalje dolazi iz odgovarajućeg poglavlja udžbenika.
:::








