## Sažetak formula, oznaka i tipičnih jedinica

Sažetak služi za brzo pronalaženje oznaka, jedinica i radnih relacija. Prije uvrštavanja provjeri odgovaraju li navedene pretpostavke tvojem zadatku; izvod i detaljni uvjeti primjene nalaze se u pripadnom poglavlju.

## Najčešće oznake

| Oznaka | Značenje | Tipična jedinica |
| --- | --- | --- |
| $\rho$ | gustoća | kg/m$^3$ |
| $\gamma$ | specifična težina, $\rho g$ | N/m$^3$ |
| $\gamma$ (pog. 9) | omjer toplinskih kapaciteta, $c_p/c_v$ | - |
| $\mu$ | dinamička viskoznost | Pa s |
| $\nu$ | kinematička viskoznost, $\mu/\rho$ | m$^2$/s |
| $\sigma$ | površinska napetost | N/m |
| $p$ | tlak | Pa |
| $K$ (pog. 1) | volumni modul elastičnosti tekućine, uz zadane toplinske uvjete | Pa |
| $\Delta p$ | razlika tlakova ili tlakovni skok | Pa |
| $p_0$ | stagnacijski tlak ili poznati referentni tlak | Pa |
| $p_M$ | manometarski (pretlak) tlak, $p_M = p_{aps} - p_{atm}$ | Pa |
| $p_{M0}$ | jednoliki manometarski pretlak plina iznad tekućine | Pa |
| $z$ | geodetska visina | m |
| $h$ | visina stupca ili gubitak izražen u metrima fluida | m |
| $H$ | zadana razlika razina ili raspoloživa energijska visina | m |
| $g_{eff}$ | efektivno ubrzanje u relativnom mirovanju | m/s$^2$ |
| $A$ | površina presjeka ili plohe | m$^2$ |
| $A_p$ | površina otvora ili pukotine | m$^2$ |
| $V$ | volumen | m$^3$ |
| $v$ | srednja ili lokalna brzina fluida | m/s |
| $a$ | brzina zvuka; iz konteksta se razlikuje od translacijskog ubrzanja | m/s |
| $c$ | apsolutna brzina fluida u turbostrojevima | m/s |
| $u$ | brzina gibajućeg elementa ili lopatice | m/s |
| $w$ | relativna brzina fluida prema gibajućem elementu, $\mathbf w = \mathbf c-\mathbf u$ (pog. 14) | m/s |
| $Q$ | volumenski protok | m$^3$/s |
| $Q_p$ | protok kroz pukotinu ili servisni ispust | m$^3$/s |
| $\dot{m}$ | maseni protok | kg/s |
| $D$ | promjer cijevi | m |
| $D_h$ | hidraulički promjer $4A/P$ u cijevi; u pog. 15 hidraulička dubina $A/T$ | m |
| $n$ (pog. 15) | Manningov koeficijent u SI zapisu | s/m$^{1/3}$ |
| $L$ | duljina cijevi | m |
| $y_R$ | položaj hvatišta rezultante ili centra tlaka | m |
| $Re$ | Reynoldsov broj | - |
| $\varepsilon$ | apsolutna hrapavost cijevi | m |
| $\lambda$ | Darcyjev koeficijent trenja | - |
| $\xi$ | lokalni koeficijent gubitka | - |
| $C_d$ | koeficijent istjecanja otvora | - |
| $C_D$ | koeficijent otpora tijela, $F_D/(\tfrac12\rho v^2 A)$ | - |
| $Fr$ | Froudeov broj, $v/\sqrt{gL}$ | - |
| $Eu$ | Eulerov broj, $\Delta p/(\rho v^2)$ | - |
| $C_p$ | koeficijent tlaka, $(p-p_\infty)/(\tfrac12\rho v^2)$ | - |
| $\sigma_{kav}$ | kavitacijski broj (ne miješati s napetošću $\sigma$) | - |
| $We$ | Weberov broj, $\rho v^2 L/\sigma$ | - |
| $Bo$ | Bondov (Eötvösov) broj, $\Delta\rho g L^2/\sigma$ | - |
| $St$ | Strouhalov broj, $fL/v$ | - |
| $Ma$ | Machov broj, $v/a$ | - |

: {.mf1-reference-table tbl-colwidths="[17,60,23]"}

## pog. 1–2: Osnovne veličine, tlak, viskoznost i kapilarnost

| Formula | Konkretan brojčani primjer |
| --- | --- |
| $\rho = m/V$ (homogen fluid ili srednja gustoća) | Uz približnu gustoću vode $1000\,\text{kg/m}^3$, masa $1\,\text{kg}$ zauzima $10^{-3}\,\text{m}^3$. |
| $\gamma = \rho g$ | Voda: $\gamma = 1000 \cdot 9{,}81 \approx 9810\,\text{N/m}^3$. |
| $s_r = \rho / \rho_{voda}$ | Živa: $s_r = 13\,600/1000 = 13{,}6$. |
| $p = F_n / A$ (jednolik tlak na ravnoj plohi) | $F = 100\,\text{N}$ na $A = 10\,\text{cm}^2$ → $p = 10^5\,\text{Pa} = 100\,\text{kPa}$. |
| $\Delta p = F_1/A_1 = F_2/A_2$ (Pascalova preša) | $F_1 = 50\,\text{N}$ na $A_1 = 5\,\text{cm}^2$ daje istu $\Delta p$ kao $F_2 = 500\,\text{N}$ na $A_2 = 50\,\text{cm}^2$. |
| $A_p s_p = \sum_i A_i s_i$ (Pascalova bilanca pomaka) | Malim klipom $A_1 = 1\,\text{cm}^2$ pomaknutim za $s_1 = 10\,\text{cm}$ veliki klip $A_2 = 10\,\text{cm}^2$ pomakne se za $s_2 = 1\,\text{cm}$. |
| $\Delta V_c\approx V_0\Delta p/K$, $As\approx\Delta V_p-\Delta V_c$ | Z4 u pog. 1: zatvorena količina tekućine od 250 cm³, porast tlaka 0,40 MPa i $K=1{,}00$ GPa daju smanjenje volumena 0,100 cm³. To je 2 % istisnutih 5,00 cm³. Stalna temperatura, kruti vodovi, bez zraka i propuštanja. |
| $\tau = \mu\,dv/dy$ | Maslinovo ulje $\mu \approx 0{,}08\,\text{Pa s}$, $dv/dy = 100\,\text{s}^{-1}$ → $\tau = 8\,\text{Pa}$. |
| $\nu = \mu / \rho$ | Voda na $20\,^\circ\text{C}$: $\nu \approx 10^{-6}\,\text{m}^2/\text{s}$; zrak: $\nu \approx 1{,}5 \cdot 10^{-5}\,\text{m}^2/\text{s}$. |
| $h = 4\sigma\cos\theta / (\rho g d)$ | Voda u staklenoj kapilari $d = 1\,\text{mm}$, $\theta \approx 0$: $h \approx 30\,\text{mm}$. |
| $p_{M,1}=\max(0,\rho gH-4\sigma\cos\theta/d)$; $p_{M,2}=\rho gH+4\sigma/D$ | Dva odvojena stanja mikrodozatora: konkavni meniskus pri punjenju i zatim puna igla s kapljicom. P4 u pog. 2 daje 227 Pa i 707 Pa. Drugi izraz zanemaruje težinu kapljice i ne određuje tlak tijekom njezina rasta. |
| $\Delta p = 4\sigma / d$ (sferna kapljica ili mjehurić s jednim sučeljem) | Kapljica vode $d = 1\,\text{mm}$, $\sigma = 0{,}072\,\text{N/m}$: $\Delta p \approx 288\,\text{Pa}$. Tanka sapunica ima dva sučelja i daje $\Delta p\approx8\sigma/d$. |

## pog. 3–6: Hidrostatika, plohe i uzgon

U izrazima za sile $z_T$ označuje **dubinu ispod slobodne površine**, a ne geodetsku visinu $z$. Izrazi s $\rho g$ pretpostavljaju homogen fluid i jednoliko gravitacijsko polje. Za silu na plohu koristi razliku tlakova s njezinih dviju strana; zapisi bez dodatnog pretlaka pretpostavljaju da se atmosferski doprinosi poništavaju.

| Formula | Konkretan brojčani primjer |
| --- | --- |
| $dp/dz = -\rho g$ | Voda: tlak raste oko $9810\,\text{Pa}$ po metru dubine (≈ $1\,\text{bar}$ na svakih $10\,\text{m}$). |
| $p = p_0 + \rho g h$ | Pri $p_0 = 101\,325\,\text{Pa}$ na dubini $h = 5\,\text{m}$ vode: $p \approx 150\,\text{kPa}$. |
| $p_{aps} = p_{atm} + p_M$ | Manometar pokazuje $50\,\text{kPa}$ → apsolutni tlak $\approx 151\,\text{kPa}$. |
| $\tan\theta = a/g$ (slobodna površina pri linijskom ubrzanju) | Spremnik koji ubrzava $a = 2\,\text{m/s}^2$: slobodna površina nagnuta za $\theta \approx 11{,}5^\circ$. |
| $g_{eff} = \sqrt{g^2 + a^2}$ | Pri $a = 5\,\text{m/s}^2$: $g_{eff} \approx 11{,}0\,\text{m/s}^2$. |
| $F = \rho g z_T A$ (sila na ravnu plohu) | Pravokutna zaklopka $2 \times 3\,\text{m}$, težište na dubini $z_T = 3{,}5\,\text{m}$: $F \approx 205\,\text{kN}$. |
| $F_H = \rho g z_T A_{proj}$ | Vertikalna projekcija zakrivljene plohe iste površine i težišta daje istu $F_H$ kao kod ravne plohe. |
| $|F_V| = \rho g V$ | Magnituda vertikalne komponente odgovara težini odgovarajućeg imaginarnog volumena; smjer se određuje iz lokalnih normala i strane na kojoj je fluid. |
| $F_R = \sqrt{F_H^2 + F_V^2}$ | $F_H = 20\,\text{kN}$ i $F_V = 15\,\text{kN}$: $F_R = 25\,\text{kN}$. |
| $y_R = \sum_i F_i y_i / \sum_i F_i$ (momentna superpozicija) | Dva doprinosa $F_1 = 10\,\text{kN}$ na $y_1 = 2\,\text{m}$ i $F_2 = 30\,\text{kN}$ na $y_2 = 5\,\text{m}$: $y_R = 170/40 = 4{,}25\,\text{m}$. |
| $F_U = \rho g V_{istisnuto}$ (Arhimedov zakon) | Tijelo istisne $V = 0{,}1\,\text{m}^3$ vode: $F_U \approx 981\,\text{N}$. |
| $G = F_U$ (slobodno plivanje u ravnoteži) | Brod mase $10\,000\,\text{kg}$ u vodi gustoće $1000\,\text{kg/m}^3$ istiskuje $V=10{,}0\,\text{m}^3$. |

## pog. 7–8 i 13: Kontinuitet, Bernoulli i gubitci

Vrijedi $v=Q/A$ za srednju normalnu brzinu presjeka. Idealni Bernoullijev zapis primjenjuje se duž strujnice pri stacionarnom nestlačivom toku bez viskoznih gubitaka i rada strojeva. Za realni tok između presjeka koristi se energijska bilanca s korekcijom profila i radom strojeva.

| Formula | Konkretan brojčani primjer |
| --- | --- |
| $Q = A v$ | Cijev $D = 50\,\text{mm}$ ($A \approx 19{,}6\,\text{cm}^2$), $v = 2\,\text{m/s}$ → $Q \approx 3{,}93\,\text{L/s}$. |
| $Q_{in} - Q_{out} = dV/dt$ | Ako je $Q_{in} = 2\,\text{L/s}$ i $Q_{out} = 1{,}5\,\text{L/s}$: spremnik akumulira $0{,}5\,\text{L/s}$. |
| $\dot{m} = \rho Q$ | Voda, $Q = 0{,}01\,\text{m}^3/\text{s}$: $\dot{m} = 10\,\text{kg/s}$. |
| $p/(\rho g) + v^2/(2g) + z = \text{const.}$ (Bernoulli, idealan fluid) | Slobodna površina spremnika na $z_1 = 10\,\text{m}$, $v_1 \approx 0$ ima istu ukupnu energiju kao izlazni mlaz na $z_2 = 0$, $v_2 \approx 14\,\text{m/s}$. |
| $H_1+h_p=H_2+h_t+h_w$, $H_i=z_i+p_i/(\rho g)+\alpha_i v_i^2/(2g)$ | Stacionarni nestlačivi tok: crpka dodaje $h_p$, turbina oduzima $h_t$, a $h_w\ge0$ opisuje gubitke. Za razvijeni laminarni tok u kružnoj cijevi $\alpha=2$; $\alpha\approx1$ zasebna je aproksimacija. |
| $v_0 = \sqrt{2gH}$ (Torricelli) | Spremnik visine $H = 5\,\text{m}$: $v_0 \approx 9{,}9\,\text{m/s}$. |
| $x = 2\sqrt{h(H-h)}$ (vodoravni domet mlaza) | $H = 1\,\text{m}$, otvor na visini $h = 0{,}5\,\text{m}$ od dna: $x_{\max} = 1\,\text{m}$. |
| $h_l = \lambda(L/D)(v^2/2g)$ (Darcy-Weisbach) | Cijev $L = 100\,\text{m}$, $D = 0{,}1\,\text{m}$, $\lambda = 0{,}025$, $v = 2\,\text{m/s}$: $h_l \approx 5{,}1\,\text{m}$. |
| $h_{loc} = \xi v^2/(2g)$ | Koljeno $\xi = 0{,}9$, $v = 3\,\text{m/s}$: $h_{loc} \approx 0{,}41\,\text{m}$. |
| $h_w = h_l + \sum h_{loc}$ | Cijev $h_l = 5\,\text{m}$ + tri koljena po $0{,}4\,\text{m}$: $h_w = 6{,}2\,\text{m}$. |
| $p_0 - p = \tfrac{1}{2}\rho v^2$ (Pitot, dinamički tlak) | Voda, $v = 10\,\text{m/s}$: $\Delta p = 50\,\text{kPa}$. |
| $v = \sqrt{2(p_0 - p)/\rho}$ | Voda, $\Delta p = 5\,\text{kPa}$: $v \approx 3{,}16\,\text{m/s}$. |

## pog. 10 i 13–14: Količina gibanja, cjevovodi i turbostrojevi

| Formula | Konkretan brojčani primjer |
| --- | --- |
| $\sum \vec{F} = \dot{m}(\vec{v}_{izl} - \vec{v}_{ul})$ | Stacionaran tok, fiksni kontrolni volumen, jedan ulaz i izlaz te jednoliki profili. Zbroj obuhvaća sve vanjske sile **na fluid**. Slobodni mlaz $\dot m=5\,\text{kg/s}$ skrenut za $90^\circ$ pri $v=20\,\text{m/s}$ daje $|F_x|=|F_y|=100\,\text{N}$; sila fluida na skretač suprotnog je smjera. |
| $\mathbf w = \mathbf c-\mathbf u$ (relativna brzina, pog. 14) | Kolinerani mlaz $c = 30\,\text{m/s}$ i lopatica $u = 12\,\text{m/s}$ daju $w = 18\,\text{m/s}$; u općem slučaju račun je vektorski. |
| $\dot{m}_{rel} = \rho A w$ | Mlaz $A = 1\,\text{cm}^2$ vode, $w = 18\,\text{m/s}$: $\dot{m}_{rel} = 1{,}8\,\text{kg/s}$. |
| $F \approx \dot{m} v$ (mlaz na nepokretnu plohu) | $\dot{m} = 2\,\text{kg/s}$, $v = 25\,\text{m/s}$: $F = 50\,\text{N}$. |
| $F \approx 2\dot{m} v$ (mlaz potpuno skreće za $180^\circ$) | Isti primjer: $F = 100\,\text{N}$. |
| $P = F u$ (snaga predana lopatici) | Lopatica $F = 1\,\text{kN}$, obodna brzina $u = 10\,\text{m/s}$: $P = 10\,\text{kW}$. |
| $Re = vD/\nu$ | Voda u kružnoj tehničkoj cijevi $D = 50\,\text{mm}$, $v = 1\,\text{m/s}$, $\nu = 10^{-6}\,\text{m}^2/\text{s}$: $Re = 5 \cdot 10^4$; za uobičajene ulazne poremećaje i hrapavost očekuje se turbulentan razvijeni tok. |
| $\lambda = 64/Re$ (potpuno razvijen laminarni tok u kružnoj cijevi) | $Re = 1500$: Darcyjev koeficijent $\lambda \approx 0{,}043$. |
| $h_w = \lambda(L/D)(v^2/2g) + \sum \xi v^2/(2g)$ | Cijev s linijskim gubitkom $5\,\text{m}$ i tri lokalna otpora po $0{,}4\,\text{m}$: $h_w = 6{,}2\,\text{m}$. |
| $Q_p = C_d A_p \sqrt{2gH}$ (istjecanje kroz otvor) | Otvor $A_p = 1\,\text{cm}^2$, $C_d = 0{,}62$, $H = 5\,\text{m}$: $Q_p \approx 0{,}61\,\text{L/s}$. |
| $A_p = Q_p / (C_d \sqrt{2gH})$ | Za $Q_p = 1\,\text{L/s}$, $H = 4\,\text{m}$: $A_p \approx 1{,}82\,\text{cm}^2$. |
| $h_{w,tot} = \sum_i h_{w,i}$ (serijski spoj) | Tri dionice s gubicima $2{,}0$, $1{,}5$ i $0{,}8\,\text{m}$: ukupno $h_{w,tot} = 4{,}3\,\text{m}$. |
| $Q_{tot} = \sum_i Q_i$, $h_{w,1} = h_{w,2}$ (paralelni spoj) | Dvije grane: kraća prima $Q_1 = 6\,\text{L/s}$, dulja $Q_2 = 4\,\text{L/s}$ za isti pad od $3\,\text{m}$. |

U turbulentnom području $\lambda$ više nije funkcija samo Reynoldsovog broja, nego i relativne hrapavosti $\varepsilon / D$ — koeficijent se očitava s Moodyjeva dijagrama.

## pog. 11: Bezdimenzijski brojevi i sličnost

Bezdimenzijski broj može izražavati omjer sila, brzina, vremenskih skala ili drugih istodimenzijskih veličina. Pri sličnosti se čuvaju sve grupe važne za promatranu fiziku, rubne i početne uvjete.

| Formula | Konkretan brojčani primjer |
| --- | --- |
| $Re = \rho v L/\mu = vL/\nu$ (relativna važnost inercijskog i viskoznog člana za odabrane skale) | Voda u tehničkom toku kružne cijevi $D = 6\,\text{mm}$, $v = 1{,}2\,\text{m/s}$: $Re = 7200$; najčešće se očekuje turbulentan režim, uz provjeru ulaza, poremećaja i geometrije. |
| $Fr = v/\sqrt{gL}$ (omjer brzina; inercijska/gravitacijska skala razmjerna je $Fr^2$) | Brod $L = 150\,\text{m}$, $v = 9\,\text{m/s}$: $Fr \approx 0{,}235$. |
| $Eu = \Delta p/(\rho v^2)$ (tlak/inercija) | Cijev $\Delta p = 18\,\text{kPa}$, $v = 2\,\text{m/s}$: $Eu = 4{,}5$. |
| $\sigma_{kav} = (p - p_v)/(\tfrac12\rho v^2)$ (kavitacija) | Venturi $p_1 = 101{,}3\,\text{kPa}$, $v_2 = 19{,}1\,\text{m/s}$: $\sigma_{kav} \approx 0{,}543$. |
| $We = \rho v^2 L/\sigma$ (relativna važnost deformirajućeg toka i površinske napetosti) | Kap $d = 3\,\text{mm}$, $v = 25\,\text{m/s}$ u zraku: $We \approx 31$; zadani orijentacijski kriterij može predvidjeti početak određenoga režima raspada, ali prag ovisi o omjerima gustoće i viskoznosti, početnoj deformaciji i definiciji režima. |
| $Bo = \Delta\rho g L^2/\sigma$ (gravitacija/napetost) | Za vodu u zraku $\Delta\rho\approx\rho_{voda}$. Pri $L = 3\,\text{mm}$: $Bo \approx 1{,}2$; kapilarna duljina $L_c \approx 2{,}7\,\text{mm}$. |
| $St = fL/v$ (vrtložno otpuštanje) | Dimnjak $D = 2\,\text{m}$, $v = 12\,\text{m/s}$, $St \approx 0{,}2$: $f \approx 1{,}2\,\text{Hz}$. |
| $Ma = v/a$ (brzina toka prema brzini širenja malog poremećaja) | Zrak $v = 79{,}6\,\text{m/s}$, $a = 340\,\text{m/s}$: $Ma \approx 0{,}23$; model konstantne gustoće početno je razuman samo ako su i toplinske te ukupne tlačne promjene dovoljno male. |
| $C_D = F_D/(\tfrac12\rho v^2 A)$ (otpor tijela) | Kugla $Re = 4\cdot10^4$: $C_D \approx 0{,}45$ → $F_D \approx 76\,\text{mN}$. |

Froudeova i Reynoldsova sličnost u pravilu se ne mogu zadovoljiti istovremeno istim fluidom; bira se dominantni broj, a drugi se korigira (npr. otpor broda se razdvaja na valni i viskozni dio).

## pog. 9: Kompresibilni idealni tok

| Formula | Pretpostavke i kontrolni primjer |
| --- | --- |
| $a^2=(\partial p/\partial\rho)_s$, $a=\sqrt{\gamma RT}$ | Mali, izentropski poremećaj; zrak pri $293\,\text{K}$ ima $a\approx343\,\text{m/s}$. |
| $Ma=v/a$ | Prvi filtar stlačivosti; $Ma<0{,}3$ je heuristika samo uz ograničene promjene temperature i tlaka. |
| $T_0/T=1+(\gamma-1)Ma^2/2$ | Stacionarni adijabatski tok kalorijski idealnog plina bez rada vratila. |
| $p_0/p=[1+(\gamma-1)Ma^2/2]^{\gamma/(\gamma-1)}$ | Dodatno reverzibilan, odnosno izentropski prijelaz. |
| $dA/A=(Ma^2-1)dv/v$ | Kvazijednodimenzijski izentropski tok; za $Ma>1$ ubrzanje traži divergentnu sapnicu. |
| $p^*/p_0=[2/(\gamma+1)]^{\gamma/(\gamma-1)}$ | Kritični omjer prigušenja; za zrak približno $0{,}528$. |

## pog. 12: Diferencijalni opis realnog toka

| Formula | Pretpostavke i kontrolni primjer |
| --- | --- |
| $D\mathbf u/Dt=\partial\mathbf u/\partial t+(\mathbf u\cdot\nabla)\mathbf u$ | Lokalno + konvektivno ubrzanje; stacionarni tok može imati nenulto ubrzanje. |
| $\nabla\cdot\mathbf u=0$ | Nestlačiv fluid konstantne gustoće. |
| $\rho D\mathbf u/Dt=-\nabla p+\mu\nabla^2\mathbf u+\rho\mathbf b$ | Newtonski fluid, konstantni $\rho$ i $\mu$. |
| $\Delta p=128\mu LQ/(\pi D^4)$ | Stacionarni, potpuno razvijeni laminarni tok Newtonskog fluida u ravnoj kružnoj cijevi, konstantna $\mu$, bez klizanja i uz zanemarivu visinsku razliku; $\Delta p\propto Q$. |
| $\delta_{99}\approx5x/\sqrt{Re_x}$ | Laminarna glatka ravna ploča, približno nulti gradijent tlaka. |
| $I_u=u'_{rms}/U$ | Mjera lokalne fluktuacije, ne dokaz potpuno razvijenog toka ni izbor modela sam po sebi. |

## pog. 15: Otvoreni tokovi

| Formula | Pretpostavke i kontrolni primjer |
| --- | --- |
| $D_h=A/T$, $Fr=v/\sqrt{gD_h}$ | Plitkovodni gravitacijski val; $Fr<1$ mirni, $Fr>1$ siloviti tok. |
| $E=y+q^2/(2gy^2)$ | Pravokutni kanal, $q=Q/b$, blag nagib, približno hidrostatički tlak i $\alpha\approx1$. |
| $y_c=(q^2/g)^{1/3}$, $E_{min}=3y_c/2$ | Kritično stanje pri zadanom protoku po širini. |
| $y_2/y_1=[\sqrt{1+8Fr_1^2}-1]/2$ | Pravokutni skok, približno vodoravno dno, hidrostatički tlak u rubnim presjecima, $\beta\approx1$ i zanemarivo trenje na kratkoj dionici. |
| $\Delta E=(y_2-y_1)^3/(4y_1y_2)$ | Gubitak mehaničke energije između spregnutih dubina, uz $\alpha\approx1$; ukupna energija ostaje očuvana. |
| $Q=A R_h^{2/3}S_f^{1/2}/n$ | Uniformni tok: $S_f=S_0$. Manningov $n$ ima SI jedinicu s/m$^{1/3}$; vrijednost ovisi o stanju korita. |

## Tipične zamjene jedinica koje treba zaustaviti odmah

- $\rho$ nije isto što i $\gamma$
- tlak u Pa nije isto što i sila u N
- $Q$ i $\dot{m}$ nisu ista veličina
- $\mu$ i $\nu$ nisu iste jedinice ni isto fizikalno značenje
- gubitak $h_w$ u metrima nije isto što i pad tlaka u Pa, iako su povezani





