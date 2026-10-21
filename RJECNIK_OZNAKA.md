# Rječnik oznaka sveučilišnog priručnika

Sastavljen 13. listopada 2026. za fizikalni pregled skica, osvježen 14. listopada 2026. nakon notacijskog usklađivanja poglavlja 1–15 i dodataka A–D. Mjerodavan je standard notacije iz [uredničkog stila](docs/urednicki_stil.md) (prenesen u nastavku), a zatim stvarni tekst poglavlja. Rječnici po poglavljima popisuju oznake kako ih tekst stvarno koristi, uključujući dvoznačnosti koje skice ne rješavaju samostalno (vidi „Treba odluku” u [izvještaju o skicama](IZVJESTAJ_SKICE.md)).

## Mjerodavni standard (preneseno iz `docs/urednicki_stil.md`)

Jedna veličina ima jednu oznaku kroz cijelu knjigu; dodatak A navodi iznimke.
Kad se u pojedinom poglavlju nužno koristi druga oznaka, uvodi se pri prvom
spomenu s izričitom napomenom.

| Veličina | Oznaka | Napomena |
| --- | --- | --- |
| brzina fluida | $v$, $\vec v$, komponente $v_x$, $v_i$ | ne $u$, $\mathbf u$, $V$ |
| brzina krute granice | $u$ (lopatica, klip, ploča); $v_s$, $v_m$, $v_p$ (brod, model, prototip); $v_A$ (napredovanje propelera); $v_j$ (mlaz) | turbostrojevi: $c$ apsolutna, $w$ relativna, $u$ obodna |
| vanjska brzina graničnog sloja, brzina trenja | $U_e$, $U_\infty$, $u_\tau$ | uz definiciju |
| brzina zvuka; brzina površinskog vala | $a$; $c$ (samo pog. 15) | |
| volumen; istisnina; masa istisnine; gaz; nadvođe | $V$; $V_{ist}$; $\Delta$; $T$; $f$ | |
| tlak atmosferski, manometarski, apsolutni, pare, zaustavni | $p_{atm}$, $p_M$, $p_{aps}$, $p_v$, $p_0$ | $p_0$ samo zaustavni; Bernoulli s $p/(\rho g)$ |
| gubitci; koeficijenti | $h_g$, $h_l$, $h_{loc}$; $\xi$, $\zeta=\lambda L/D+\sum\xi$, $\lambda$ | $K$ samo volumni modul; $\lambda_L$ mjerilo duljina |
| izentropski eksponent; specifična težina | $\kappa$; $\gamma$ | |
| bezdimenzijski brojevi | $Ma$, $Re$, $Fr$, $We$, $St$, $Bo$, $Eu=\Delta p/(\rho v^2)$ | |
| korekcijski faktori; kutovi | $\alpha$, $\beta$; $\theta$, $\varphi$ | kutovi lopatica $\beta_1$, $\beta_2$ samo u pog. 14 |
| hidraulički promjer, dubina, radijus | $D_h=4A/P$, $y_h=A/T$, $R_h=A/P$ | $T$ širina slobodne površine (pog. 15) |
| centar tlaka | $h_{CP}$, $y_{CP}$ | |
| protok po širini; volumenski; maseni | $q$ (samo pog. 15); $Q$; $\dot m$ | |
| tetiva profila; toplinski kapacitet | $l$; $c_p$ | |
| potisak; temperatura | $F_T$; $T$ | |
| kavitacijski broj | $\sigma_{kav}=(p_{ref}-p_v)/(\tfrac12\rho v_{ref}^2)$ | referentno mjesto navesti |
| kavitacijska rezerva | $NPSH_a$, $NPSH_r$ | |
| kontrolni volumen i ploha | KV, KP; indeksi ul, iz | |
| stabilitet | $B$, $G$, $M$, $KB$, $BM$, $KG$, $GM$ | bez nadvlake |
| težina | $F_G$ ili $mg$ | $G$ samo težište (stabilitet), ne težina |
| gustoće vode, morske vode, ulja, žive, zraka | $\rho_v$, $\rho_{mv}$, $\rho_u$, $\rho_{Hg}$, $\rho_{zr}$ | hrvatski indeksi: $v$ voda, $u$ ulje (i $\nu_v$, $\nu_u$, $h_v$, $h_u$ za slojeve); $p_v$ ostaje tlak pare; indeks $m$ samo model (pog. 11, 14) |
| relativna gustoća | $s_r=\rho/\rho_v$ | |
| kut poprečnog nagiba; ostali kutovi | $\varphi$; $\theta$ | |
| širina broda ili pontona | $b$ | $B$ samo središte istisnine |
| polumjer zavoja | $R_z$ | $R$ polumjer spremnika ili luka |
| tlak na slobodnoj površini; tlak plina | $p_{pov}$; $p_{pl}$ | |
| udio otvorene površine rešetke | $\psi$ | |
| ekvivalentna hrapavost; disipacija turbulentne kinetičke energije | $k_s$, relativno $k_s/D$; $\varepsilon$ | $\varepsilon$ samo disipacija (model $k$–$\varepsilon$); tolerancije s indeksom ($\varepsilon_h$) |
| visina dobave crpke; visina turbine | $H_p$; $H_t$ | ne $h_p$, $h_t$ |
| gubitak visine; smično naprezanje na stijenci; koeficijent preljeva | $h_g$ (s indeksima $h_{g,s}$, $h_{g,1}$…); $\tau_{st}$; $C_{pr}$ | hrvatski indeksi (gubitak, stijenka, preljev); ne $h_w$, $\tau_w$, $C_w$ |
| standardna nesigurnost | $s(x)$; $s_E$, $s_\Delta$ | ne $u(x)$ ($u$ je brzina krute granice) |
| koeficijent sustrujanja; faktor učinka rotora | $\chi$; $FM$ | samo pog. 14 |
| kut lopatice | $\beta_1$, $\beta_2$ od smjera $-u$ | kut skretanja mlaza $\theta$ |
| volumenski protok | $Q$ u m$^3$/s ili L/s | jedinica „L/s” (veliko L) |

Vektori na skicama (standard od 14. listopada 2026.): jedna boja `#356b83`,
a vrsta veličine određena je stilom i atributom `data-mf1-vector`. Sila i moment:
deblja puna crta (2,4–3,4) i pun vrh. Brzina, smjer protoka i kutna brzina: tanja
crta (1,3–2,0) i otvoren vrh. Ubrzanje i efektivno polje: isprekidana crta
(1,6–2,4) i pun vrh. Raspodijeljeni tlak i jedinična normala: tanka crta (0,8–1,6)
i pun vrh. Strelice koje nisu vektori (kote, osi, vodilice, strujnice, putanje,
dijagrami) nose `data-mf1-role` i ne koriste vektorsku boju. Oznaka vektora uz
strelicu piše se podebljano, oznake skalara obično. Pravilo provjerava
`tools/audit_sketch_design.py`; legenda za čitatelja nalazi se u uvodnom
poglavlju „Kako koristiti priručnik”.

Nazivlje: crpka; hidraulički; hidrostatički; meniskus; Reynoldsov transportni
teorem; zaustavne veličine; kalorički savršen plin; zagušenje (choking) prema
prigušenju (throttling); energijska crta (EGL) i piezometarska crta (HGL);
Darcyjev koeficijent trenja; volumenski protok; metacentarska visina;
stabilitet, nadvođe, poluga stabiliteta $GZ$, poprečni nagib, kut nestajanja
stabiliteta, metoda dodane težine; zapljuskivanje; prividna sila; impulsna
funkcija. Poglavlje ne upućuje samo na sebe brojem; piše „u ovom poglavlju”.

## Poglavlje 1

Izvor: stvarni tekst poglavlja (13. 10. 2026.), dopunski d01/d02.

| simbol | naziv veličine | jedinica | gdje se pojavljuje |
|---|---|---|---|
| p, p(x,y,z) | tlak (skalarno polje) | Pa | tumačenje uvodne skice, Tlak, izvod tetraedra |
| F_n | normalna tlačna sila na plohu | N | p = F_n/A (teorija); NB: u P4 (kočnica) F_n je sila vozača na papučicu |
| A | površina plohe | m² | p = F_n/A; Z4 (efektivna površina klipa) |
| ρ | gustoća | kg/m³ | Osnovne veličine, P1, Z1 |
| m | masa | kg | ρ = m/V |
| V | volumen | m³ (L, cm³) | ρ = m/V; tumačenje uvoda („litra ulja i vode”) |
| γ | specifična težina | N/m³ | γ = ρg, P1, Z1 |
| s_r | relativna gustoća | – | s_r = ρ/ρ_w, P1, Z1 |
| ρ_w | referentna gustoća vode | kg/m³ | uvod, teorija, P1, Z1, d01; skice uvod i P1 |
| g | ubrzanje sile teže | m/s² | P1, Z1 |
| F_G | težina (P1: samo ulje) / ukupna težina tereta na klipu (P2) / najveća težina tereta (P4) / opterećenje stola (Z6); G samo težište | N | P1, P2, P4 (ch), Z6; skice P1, P2, P4, Z6 |
| Δp | porast (nametnuta promjena) tlaka | Pa | Pascalov zakon, izvod; Z4 (razlika tlakova preko klipa) |
| F_1, F_2 | ulazna sila na mali klip; sila ulja na veliki (radni) klip | N | uvod, izvod, P3, Z3 |
| A_1, A_2 | površine malog i velikog klipa | m² | uvod, izvod, P2 (A_2), P3, Z3 |
| s_1, s_2 | pomaci (hodovi) malog i velikog klipa | m | uvod, izvod, P3, Z3 |
| ΔV_1, ΔV_2 | istisnuti volumeni | m³ | izvod |
| K | volumni modul elastičnosti | Pa | granica modela, P3, Z4 |
| V_0 | početni ukupni volumen zatvorene tekućine | m³ | granica modela, P3, Z4 |
| ΔV_c | smanjenje volumena zbog stlačivanja | m³ | granica modela, P3, Z4 |
| ΔV_p | volumen istisnut crpnim klipom | m³ | granica modela, P3, Z4 |
| A_L, s_L | površina i pomak radnog (podiznog) klipa | m², m | granica modela, P4 (ch), Z5, Z6 |
| s_{2,c} | pomak radnog klipa uz stlačivanje | m | P3 |
| d_k, A_k | promjer i površina opterećenog klipa | m, m² | P2 |
| p_M | manometarski tlak | Pa | P2, P3, P4, P5, P6, Z2, Z5, Z6, uvod vježbi |
| A_p, F_p | površina crpnog klipa; sila na crpni klip | m², N | P4 (ch), P6, Z6 (A_p u naputku) |
| s_h | puni tlačni hod crpke | m | P4 (ch) |
| s_p | ukupni zbroj hodova crpnog klipa | m | P4 (ch), Z5, Z6 |
| F_L | sila jednog radnog cilindra (P4); stalna sila na radnom klipu (Z5) | N | P4 (ch), Z5 |
| n | broj punih hodova (P4); broj stega (P6) | – | P4, P6 |
| s_{L,9}, s_posl | podizaj nakon 9 hodova; posljednji djelomični hod | m | P4 |
| ΔV | volumen potreban za podizaj (P4); dodatni dovedeni volumen (Z4) | m³ | P4, Z4 |
| i; a, 5a | omjer poluge papučice; krakovi poluge od zgloba | –; m | P5 |
| F_M, d_M, A_M | sila na glavni klip, promjer i površina glavnog cilindra | N, m, m² | P5 |
| d_f, A_f, F_f | promjer, površina, sila prednjeg kočnog cilindra | m, m², N | P5 |
| d_r, A_r, F_r | promjer, površina, sila stražnjeg kočnog cilindra | m, m², N | P5 |
| F_uk | skalarni zbroj iznosa sila klipova | N | P5, P6 |
| k | omjer F_uk/F_n | – | P5 |
| s_M, s_f, s_r | hodovi glavnog, prednjeg i stražnjeg klipa | m | P5 provjera (s_r ovdje hod, ne relativna gustoća) |
| d_p, A_p, d_s, A_s, F_s, F_dop | crpni klip i stege stezne naprave | m, m², N | P6 (bez skice) |
| m_0, m_1, m_2; V_1, V_2 | masa prazne/napunjene posude; volumeni ulja | g; cm³ | Z1 |
| r, d, A, F, M, s, V | krak ruda, promjer klipa, površina, sila, moment, hod, volumen (četiri cilindra: M = 2Fr, V = 2As) | m, m, m², N, N m, m, m³ | Z2 |
| d_1, d_2 | promjeri klipova preše | m | Z3 |
| W_1, W_2 | ulazni i izlazni rad | J | Z3 |
| s, s_0 | pomak klipa; nestlačivi pomak | m | Z4 |
| F_{p,max}, s_{p,max}, d_a, d_b, d_c, W_p, W_L | ograničenja i varijante crpke | N, m, J | Z5 |
| d | promjer crpnog klipa | m | Z6 (i Z2 za klip kormilarskog stroja) |
| Δz | podizaj stola | m | Z6 |
| η_F, η_V | faktor prijenosa sile, volumetrijska učinkovitost | – | Z6 |
| F_{G,kor}, F_{G,kor,min}, s_{p,st} | korisno opterećenje i njegova donja granica; stvarni hod crpke | N, m | Z6 |

#### Uočene nedosljednosti oznaka (zabilježeno, ne rješava se)

1. `F_n`: normalna tlačna sila (p = F_n/A) i sila vozača na papučicu u P5.
2. `s_r`: relativna gustoća (Osnovne veličine) i hod stražnjeg kočnog klipa u P5 (`A_M s_M = 2A_f s_f + 2A_r s_r`).
3. `d`: promjer klipa kormilarskog stroja (Z2) i promjer crpnog klipa (Z6) — različiti zadatci, bez sukoba unutar zadatka.
4. `ΔV`: volumen za podizaj (P4) i dodatni dovedeni volumen (Z4).
5. `F_L`: sila jednog radnog cilindra (P4, posljedica) i zadana stalna sila (Z5).
6. ID `#task-kormilarski-stroj-dva-cilindra` namjerno je zadržan (stabilni ID), iako stroj u Z2 sada ima četiri cilindra.


## Poglavlje 2

Izvor: stvarni tekst poglavlja (13. 10. 2026.), dopunski d01/d02.

| simbol | naziv veličine | jedinica | gdje se pojavljuje |
|---|---|---|---|
| v, v(y) | brzina fluida (profil) | m/s | uvod, izvod Couette (v(0)=0, v(δ)=u), P2, P4, Z1, Z3 |
| u | brzina pomične krute granice (ploča, obod osovine) | m/s | uvod, izvod, P2, P4 (obodna brzina), Z1, Z3, Z5 |
| u_* | brzina ploče za predviđanje | m/s | Z5 |
| y | koordinata okomita na stijenku (P4: od čahure prema osovini) | m | izvod, P4 |
| τ | smično naprezanje (komponenta s odabranim predznakom); \|τ\| iznos | Pa | uvod, izvod, P2, Z1, Z5 |
| τ_1, τ_2 | smično naprezanje pri 0 °C i 90 °C (P4); \|τ_1\|, \|τ_2\| u gornjem/donjem procjepu (Z3) | Pa | P4, Z3 |
| μ | dinamička viskoznost | Pa s | sve |
| μ_1, μ_2 | viskoznost pri T_1, T_2 | Pa s | P4 |
| ν | kinematička viskoznost | m²/s | uvod, P1, P2 |
| ρ | gustoća | kg/m³ | P1, P2, P3, P5, P6 (ch), Z4, Z6 |
| δ | debljina sloja / procjepa | m | izvod, P2, P4, Z1, Z5 |
| δ_1, δ_2 | debljine gornjeg i donjeg procjepa | m | Z3 |
| A | aktivna površina ploče; oplakana površina osovine (P4) | m² | izvod, P2, P4, Z1, Z3, Z5 |
| F | vučna (vanjska) sila na pokretnu ploču | N | uvod, izvod, P2, Z1, Z3 |
| F_v | sila ulja (uzorka) na ploču (viskozni otpor) | N | tumačenje uvodne skice; Z5 („Napomene uz skice”) |
| F_1, F_2 | sila trenja pri 0 °C i 90 °C (P4); sile na gornjoj/donjoj strani ploče (Z3) | N | P4, Z3 |
| F_* | predviđena sila pri u_* | N | Z5 |
| M_1, M_2 | zakretni moment trenja pri 0 °C i 90 °C | N m | P4 |
| P_1, P_2 | snaga viskoznog trenja | W | P4 |
| D | promjer osovine (P4); promjer kapljice (P5 ch, Z6) | m | P4, P5, Z6 |
| L | duljina ležaja | m | P4 |
| n | brzina vrtnje | min⁻¹ | P4 |
| ω | kutna brzina | rad/s | P4 |
| T_1, T_2 | temperature ulja | °C | P4 |
| σ | površinska napetost (σ_lv u Youngovoj jednadžbi) | N/m | izvod, P3, P5, P6, Z2, Z4, Z6 |
| σ_sv, σ_sl, σ_lv | napetosti krutina–para, krutina–tekućina, tekućina–para | N/m | Youngova jednadžba |
| θ | kontaktni kut (mjeri se kroz tekućinu) | ° | izvod, P3, P5, P6, Z6 |
| θ_1, θ_2 | kontaktni kut na očišćenom čeliku / premazu | ° | Z4 |
| h | visina kapilarnog uspona | m | izvod, P3, P6 |
| h_1, h_2 | uspon na čistom čeliku / spuštanje uz premaz | m | Z4 |
| h_cap | prirodni kapilarni uspon | m | P5 (ch), Z6 |
| h_hidrofobno | uspon uz hidrofobni premaz | m | P6 |
| d | promjer kapilare / igle; promjer kapljice i mjehura (Z2) | m | izvod, P3, P5, P6, Z2, Z6 |
| b | širina procjepa između limova | m | Z4, sažetak |
| F_{σ,z} | vertikalna komponenta površinske sile | N | izvod kapilarnog uspona |
| F_G | težina podignutog stupca (uvjet F_{σ,z} = F_G) | N | izvod kapilarnog uspona |
| V | volumen stupca | m³ | izvod |
| r | polumjer kapljice | m | izvod Young–Laplace |
| p_u | tlak unutar kapljice/mjehura | Pa | izvod, P5 (ch), Z2 |
| p_ok | tlak okolnog plina | Pa | izvod Young–Laplace |
| Δp | tlačni skok (p_u − p_ok; u P6 p_zrak − p_tekućina) | Pa | izvod, P5, P6, Z2 |
| Δp_k, Δp_m | skok za kapljicu i mjehur | Pa | Z2 |
| R_1, R_2 | glavni polumjeri zakrivljenosti | m | izvod |
| A_proj, F_tlak, F_σ, L | projicirana površina, tlačna sila, sila napetosti, duljina ekvatora | m², N, N, m | izvod Young–Laplace |
| H | visina izlaza iznad slobodne površine spremnika | m | P5 (ch), Z6 |
| p_M | pretlak iznad spremnika | Pa | P5 (ch), Z6 |
| p_{M,1}, p_{M,2} | pretlak za stanje 1 (meniskus do izlaza) i stanje 2 (formirana kapljica) | Pa | P5 (ch), Z6 |
| p_atm | atmosferski tlak | Pa | P5 (ch), Z2 napomena, Z6 („atmosferski tlak”) |
| p_izlaz | tlak vode na izlazu | Pa | P5 (ch) |
| p_zrak, p_tekućina | tlak zraka i tekućine uz meniskus | Pa | P6 |
| D_min, D_max | granice promjera kapljice | m | Z6 |
| p_v | tlak pare | Pa | fizikalno značenje (kavitacija) |
| τ_ij, v_i, x_j | tenzor viskoznih naprezanja, komponente brzine, koordinate | Pa, m/s, m | dublje |

#### Uočene nedosljednosti oznaka (zabilježeno, ne rješava se)

1. `D`: promjer osovine (P4) i promjer kapljice (P5 ch, Z6) — različiti zadatci.
2. `L`: duljina ležaja (P4), duljina ekvatora (izvod Young–Laplace), duljina procjepa (Z4 naputak).
3. `F_1, F_2`: sile trenja pri dvjema temperaturama (P4) i sile na dvjema stranama ploče (Z3).
4. `τ_1, τ_2`: dvije temperature (P4) i dva procjepa (Z3).
5. `Δp`: u Young–Laplaceu `p_u − p_ok`; u P6 `p_zrak − p_tekućina` (izričito definirano) — dva predznaka, ali uvijek definirana.
6. `M_otpor` (stara oznaka „Motpor” u skici P4) ne postoji u tekstu; tekst rabi `M_1`, `M_2`.
7. Skica Z6 imala je `p₀` za tlak okolnog zraka; prema urednickom stilu i d01 `p_0` je samo zaustavni tlak (ispravljeno u skici; tekst Z6 rabi „atmosferski tlak”).
8. Skice su na pet mjesta imale „donja stijenka: u = 0” / „čahura: u = 0”, iako je `u` brzina pomične granice; tekst rabi `v(0)=0` (ispravljeno u skicama).


## Poglavlje 3

| simbol | naziv veličine | jedinica | gdje se pojavljuje |
|---|---|---|---|
| p | tlak | Pa | cijelo poglavlje |
| z | visina, os prema gore | m | izvod (r. 25–86) |
| ρ | gustoća homogenog fluida u općim relacijama | kg/m³ | izvod; p = p_pov + ρgh, h_p = p_M/(ρg), diferencijalni manometar s istim fluidom |
| g | ubrzanje sile teže | m/s² | svugdje (9,81) |
| h | dubina ispod slobodne površine / visina vode iznad točke | m | izvod r. 83–88; uvod; P1 (1,40 m); Z1 (2,40 m); Z2 (traženo) |
| p_pov | tlak na slobodnoj površini | Pa | r. 3, 38, 88, 833 |
| p_M | manometarski tlak | Pa | r. 3, 169–173; P4; Z1 |
| p_aps | apsolutni tlak | Pa | r. 3, 206; P4 |
| p_atm | lokalni atmosferski tlak | Pa | r. 3; P1, P3, P4, P6, Z1, Z5, Z6 |
| p_vak | vakuumski tlak, p_atm − p_aps | Pa | r. 210, 215; Z5 (p_vak,max) |
| h_p | piezometarska visina p_M/(ρg) | m | r. 3, 172 |
| z_P | visina ploče P iznad dna tanka | m | P5 (2,0 m) |
| p_pl | (apsolutni) tlak plina u zatvorenom spremniku | Pa | r. 5, 88; P1; Z2 (Δp = p_A − p_pl); kontrolni rezultati Z5 i Z6 (aps.) |
| p_M,pl | plinski pretlak | Pa | P1 (18 kPa), P3 (3,0 kPa) |
| ρ_Hg | gustoća žive | kg/m³ | r. 5; P2; Z3, Z5, Z6 |
| Δh | razlika razina manometarske tekućine | m | r. 5; Z3 (0,185), Z5, Z6 (0,210); u P6 Δh = pad piezometarske visine |
| p_1, p_2 | tlakovi u vodovima diferencijalnog manometra | Pa | r. 5; P2 |
| ρ_mv | gustoća morske vode | kg/m³ | P2 (1035), P3 (1025, vodeni talog), P5 (1025, more izvana), CFD okvir balastnog tanka |
| ρ_zr | gustoća zraka | kg/m³ | P2 (1,2) |
| h_1…h_4 | visinski segmenti hoda kroz manometar | m | P2 (0,60; 0,10; 0,70; 0,40); Z6: h_1, h_2 dubine (0,65; 1,30) |
| δ | relativna pogreška | % | P2 |
| p_M,dno | manometarski tlak na dnu tanka | Pa | P3 (141,0 kPa) |
| ρ_o | gustoća ulja | kg/m³ | P3 (860, teret), P4 (870), Z3 (860), Z4 (850), Z5 (860) |
| ρ_w | gustoća (slatke) vode | kg/m³ | P1 (998), P2 (1000), P6 (998), Z1 (998), Z2 (998), Z4 (1000), Z5 (998), Z6 (998) |
| h_u, h_v | visina stupca ulja, debljina vodenog sloja | m | P3 (h_v = 0,35); Z4 (h_u, h_v) |
| H_ref | visina referentne točke ullagea iznad dna | m | P3 (18,60) |
| U_m, U | očitanje ullage vrpce; ullage iz tlaka i geometrije | m | P3 (U_m = 2,31) |
| A_t | tlocrtna površina tanka | m² | P3 (600) |
| ρ_pl | gustoća inertnog plina | kg/m³ | P3 (1,2) |
| h′, h″, ΔV | pogrešne visine ulja, pogreška volumena | m, m³ | P3 |
| p_aps,dno | apsolutni tlak na dnu | Pa | P3 |
| H | visina usisa crpke iznad površine | m | P4 (2,40) |
| H | ukupna visina tekućine | m | Z4 (1,50) |
| p_v | tlak pare | Pa | P4 (≈ 200) |
| H_max | statička granična visina stupca | m | P4 |
| Q | volumenski protok | m³/s | P4 (Q = 0) |
| H_t, T_g | visina tanka, gaz | m | P5 (5,0; 8,5) |
| ρ_mv, ρ_b | gustoća mora izvana, balasta iznutra | kg/m³ | P5 (1025, 1025; ρ_b zasebno jer balast može biti i slatka voda) |
| h_s | razina balasta iz sondiranja | m | P5 (3,0) |
| p_M,ext,dno, p_M,ext,P | manometarski tlak mora na dno / ploču P | Pa | P5 |
| p^A_M,int,dno, p^A_M,int,P | manometarski tlak balasta u stanju A | Pa | P5 |
| Δp^A_dno, Δp^A_P, Δp^B, Δp^C_dno | neto tlak na oplatu | Pa | P5 |
| p_M,A, p_M,B, p_aps,B | tlakovi u čvorovima mreže | Pa | P6; u Z4 p_M,A = tlak na dnu |
| Δz | razlika visina z_B − z_A | m | P6 (38) |
| h_T | visina vode u tornju iznad B | m | P6 |
| p_M,granica | tlak na granici ulja i vode | Pa | Z4 |
| Δh_max, ε_h, ε_p,max | najveća razlika razina, pogreška očitanja, pogreška tlaka | m, m, Pa | Z5 |
| p_max | konzervativni najveći tlak | Pa | Z6 |
| A, B, G, P | točke: A (P1 priključak, Z2 uz dno, Z4 dno, P6 čvor), B (P6), G plinski prostor (Z2), P ploča oplate (P5) | — | — |

#### Nedosljednosti u tekstu (zabilježeno, nije rješavano)

1. **Imena točaka** — Z1 („promatrana točka”), Z3 („priključna točka”) i Z6 („dublja točka”) nemaju slovne oznake u tekstu zadatka; napomena uz skice (r. 827) za Z6 ipak koristi „točka A”. Udaljenost 0,12 m u Z3 nema simbol.
2. **H** — usisna visina (P4) i ukupna visina tekućine (Z4); kontekstno jasno. U okviru izotermalne atmosfere $H$ je i karakteristična visina atmosfere (lokalno u izvodu, namjerno zadržano).


## Poglavlje 4

| simbol | naziv veličine | jedinica | gdje se pojavljuje |
|---|---|---|---|
| \vec a, a | stalno translacijsko ubrzanje spremnika | m/s² | izvod r. 25–87; P1 (1,35), P2 (3,4), P5 (3,8, kočenje), Z1 (1,20), Z5 (2,00) |
| a_x, a_z | komponente ubrzanja | m/s² | r. 57–75; Z3 (a_z = ±2,3) |
| a | centripetalno ubrzanje v_s²/R_z | m/s² | P3; uvod r. 3 |
| a_cf | centrifugalno ubrzanje ω²r | m/s² | r. 106 |
| a_max | ubrzanje na granici prelijevanja | m/s² | P3, Z2 |
| \vec g, g | gravitacija | m/s² | svugdje |
| \vec g_eff, g_eff | efektivno polje g − a | m/s² | r. 3, 42–47; P2 (10,38) |
| L | duljina spremnika u smjeru ubrzanja | m | r. 27; P1 (1,60), P5 (1,20), Z1 (1,80), Z2 (1,40), Z5 (1,50) |
| b | širina spremnika | m | P1 (0,80) |
| Δh | razlika razina slobodne površine | m | r. 3, 27, 147; P1, P3, P4, P5 |
| θ | kut nagiba slobodne površine | ° | r. 3; P1, P2, P3 |
| θ_AB | kut stijenke AB prema vodoravnici | ° | P2 |
| h_0 | početna (mirna, srednja) visina | m | r. 158; P1 (0,42), P3 (1,60), P4 (0,60), P5 (0,45), Z1–Z6 |
| h_str, h_pred | visina uz stražnju / prednju stijenku | m | P1, P5, Z1, Z5 |
| H | visina boka / spremnika | m | r. 198; P3 (2,20), P4 (0,78), P5 (0,80), Z1, Z2, Z5, Z6 |
| H | vertikalna projekcija stijenke AB | m | P2 (0,55) — druga veličina iste oznake |
| p_M,pl | plinski pretlak | Pa | P2 (16 kPa) |
| p_M(y), p_M,B | manometarski tlak uzduž AB, u točki B | Pa | P2 |
| s, y | duljina stijenke AB, udaljenost od A uzduž AB | m | P2 |
| ω | kutna brzina | rad/s | r. 92–204; P4 (5,20), Z4, Z6 |
| r | udaljenost od osi | m | r. 106–147 |
| R | polumjer spremnika | m | r. 147, 158; P4 (0,40), Z6 (0,32) |
| R_z | polumjer zavoja broda | m | P3 (180), uvod r. 3 |
| z(r) | visina površine kao koordinata u izvodu (z = h_C na osi) | m | izvod paraboloida |
| h(r), h_C, h_R | visina površine; na osi; uz stijenku | m | uvod r. 5, izvod, P4, Z6 |
| ω_crit^ogol, ω_crit^prel | kritične kutne brzine | rad/s | r. 195–201 |
| ω_max, n_max | granica prelijevanja | rad/s, okr/min | P4, Z6 |
| k, ω_zad | omjer ω_zad/ω_max, zadana brzina | –, rad/s | Z6 |
| p_M,C, p_M,D | tlak na dnu u osi / uz stijenku | Pa | P4 |
| v_s | brzina broda | m/s, čv | P3 (12 čv) |
| b_t | širina tanka | m | P3 (9,0) |
| h_v, h_u | razina uz vanjsku / unutarnju stijenku | m | P3 |
| v_max | brzina broda na granici prelijevanja | m/s | P3 |
| ρ; ρ_mv; ρ_w; ρ_o | gustoća (općenito; P2 960, P5 gorivo 750); morske vode (P3, 1025); vode (P4, uvod u vježbe, Z4, Z6 naputak); ulja (Z3, 870) | kg/m³ | izvodi, P2–P5, Z3, Z4, Z6 |
| n, r_2, r_u, r_v, r_i | brzina vrtnje; polumjeri bubnja, izlaza, razdjelnice | okr/min, m | P6 |
| ρ_o, ρ_w | gustoća goriva, vode | kg/m³ | P6 |
| Q, H_b, V, t_z, \vec v_rel | protok, visina bubnja, volumen, vrijeme zadržavanja, relativna brzina | — | P6; r. 92–106 |
| h, A, B | visina stupca; vrh, dno cilindra | m | Z3 |
| Δp, Δp_0 | razlika tlakova (ubrzano / mirovanje) | Pa | Z3 |
| r_A, r_B, p_M,A, p_M,B | polumjeri i tlakovi senzora | mm, kPa | Z4 |
| t, ε_h, s_h | vrijeme, dopušteno odstupanje, raspon | s, mm, mm | Z5 |

#### Nedosljednosti u tekstu (zabilježeno, nije rješavano)

1. **H** — visina spremnika i, u P2, vertikalna projekcija stijenke AB (r. 297).
2. **Granica prelijevanja** — ω_crit^prel (izvod) i ω_max (P4, Z6) za istu veličinu.
3. **h_v, h_u** (P3) — indeks v ovdje znači „vanjska”, a ne paru; za visine nema dvoznačnosti, namjerno zadržano (moguće h_un, h_van).
4. **h_C** — u ovom poglavlju visina površine na osi, u pog. 5 dubina težišta plohe; međupoglavna iznimka navedena u d01.
5. **Δp_0** (Z3) — mirovna razlika tlakova, nije zaustavni tlak $p_0$; zadržano.


## Poglavlje 5

| simbol | naziv veličine | jedinica | gdje se pojavljuje |
|---|---|---|---|
| $d\mathbf F$, $\mathbf F$ | elementarna / ukupna sila tlaka (vektor) | N | izvod (eq …-01), zakrivljena ploha; na skicama „dF” |
| $\mathbf n_f$; $n_{f,x}$, $n_{f,z}$ | jedinična normala iz fluida prema stijenci; komponente | – | izvodi, CFD okvir |
| $p$ | (manometarski) tlak $\rho gh$ | Pa | cijelo poglavlje |
| $p_{pl}$ | jednoliki tlak plina iznad slobodne površine | Pa | „Referentni tlak”, centar tlaka |
| $p_{\mathrm{net}}$ | neto tlak | Pa | eq …referentni-tlak-02 |
| $\rho$; $\rho_u$, $\rho_v$ | gustoća vode; ulja, vode (P3) | kg/m³ | svugdje; P3 |
| $g$ | ubrzanje sile teže | m/s² | svugdje |
| $h$ | vertikalna dubina od slobodne površine | m | izvodi |
| $h_a$, $h_b$ | dubine rubova pojasa | m | izvod rezultante |
| $h_C$ | dubina težišta plohe | m | izvodi, P1, P2, uvod |
| $h_{CP}$ | dubina centra tlaka | m | izvodi, P1, P3, Z1, Z4, uvod |
| $h_R$ | dubina hvatišta za $p_{pl}+\rho gh$ | m | izvod centra tlaka |
| $h_0$ | dubina početka osi $y$ (izvod nagnute plohe); dubina vrha trokuta (Z4) | m | izvod nagnute plohe; Z4 |
| $h_1$ | dubina gornjeg ruba (P1, Z1, Z6); dubina gornje točke luka (P4); dubina osi O (Z5) | m | P1, P4, Z1, Z5, Z6 |
| $h_A$ | dubina zgloba A | m | P2 |
| $h_u$, $h_v$ | visine sloja ulja / vode | m | P3 |
| $h_L$, $h_D$ | dubine vode lijevo / desno | m | Z3 |
| $h_{Cx}$ | dubina težišta vertikalne projekcije | m | zakrivljena ploha, P4, P5 |
| $h_H$ | dubina pravca djelovanja $F_H$ | m | P4, P5, P6 |
| $A$ | površina plohe (također točka A u P2, P4, P6, Z2, Z3, Z5) | m² | izvodi; točke |
| $A_x$ | vertikalna projekcija zakrivljene plohe | m² | P4, P5 |
| $b$ | širina (okomito na presjek); osnovica trokuta (Z4) | m | svi primjeri i zadatci |
| $H$ | visina plohe (P1, Z1, Z3, Z4, Z6); dubina točke B (Z2) | m | P1, Z1–Z4, Z6 |
| $L$ | duljina kosog poklopca (P2); vodoravna duljina pokrova (Z2) | m | P2, Z2 |
| $R$ | polumjer luka | m | P4–P6, Z5 |
| $\theta$ | kut plohe prema vodoravnici | ° | nagnuta ploha, P2 |
| $y$, $y_C$, $y_{CP}$ | koordinata duž plohe; težište; centar tlaka duž plohe | m | nagnuta ploha, P2 |
| $y_R$ | visina pravca neto sile iznad dna | m | Z3 (odgovor) |
| $I_G$, $I_O$ | drugi moment površine oko težišne osi / oko slobodne površine | m⁴ | izvodi, P1, P4 |
| $F$ | rezultanta na ravnu plohu | N | ravna ploha, P1, P2, P3, Z4, Z6 |
| $F_1$, $F_{2,r}$, $F_{2,t}$; $F_2$ | dijelovi sile na pregradu (ulje; pravokutni i trokutni dio vode); $F_2$ = vodeno polje | N | P3 (F_2 samo u „Veza s proračunom”) |
| $F_H$ ($\lvert F_H\rvert$) | vodoravna komponenta na zakrivljenu plohu | N | teorija, P4–P6 |
| $F_V$ ($\lvert F_V\rvert$) | vertikalna komponenta | N | teorija, P4–P6 |
| $F_x$, $F_z$ (Z2); $F_x$, $F_y$ (Z5); $F_x$ (Z1, Z3) | predznačene komponente sile vode | N | zadatci |
| $F_R$; $\theta_R$ | rezultanta komponenata; njezin kut prema vodoravnici (atan2; teorija, P5) | N; ° | teorija, P4–P6 |
| $V^*$; $V_1$, $V_2$ | pomoćni volumen; njegovi dijelovi | m³ | teorija, P4 (V_1 u „Veza”), P5, P6 |
| $x_V$ | vodoravni krak pravca $F_V$ (od vertikale kroz O u P4; od stijenke u P5; od A u P6) | m | P4–P6 |
| $C$, $CP$, $O$ | težište plohe, centar tlaka, središte zakrivljenosti | – | uvod, izvodi, P4–P6, Z5 |
| $M_A$, $M_O$ | moment oko A / O | N m | P2, P3, Z2, Z3, Z5 |
| $T$; $T_{\max}$ | sila spojnice; dopuštena | N | P2, P3, P6, Z3, Z5 |
| $R_A$; $R_{Ox}$, $R_{Oy}$ | reakcija zgloba; reakcija osi | N | P3; Z5 |
| $F_G$, $x_G$ | težina sklopa (točka G je težište), krak težine | N; m | Z5 |
| $F_{\max}$, $b_{\max}$ | dopuštena sila; najveća širina | N; m | Z4 |
| $F_m$, $s(\cdot)$, $z$ | izmjerena sila, standardna nesigurnost, normirano odstupanje | N; jedinica veličine; – | Z6 |

#### Nedosljednosti u tekstu (zabilježeno, ne rješavam)

1. $h_0$: u izvodu nagnute plohe dubina početka osi $y$; u Z4 dubina vrha trokuta (dva značenja, oba lokalno definirana).
2. $h_1$: četiri lokalna značenja (gornji rub P1/Z1/Z6, gornja točka luka P4, dubina osi O u Z5).
3. $H$: visina plohe (P1, Z1, Z3, Z4, Z6), ali u Z2 dubina točke B; $L$: duljina kose plohe (P2) i vodoravna duljina (Z2).
4. $A$: površina plohe i oznaka točke (P2, P4, P6, Z2, Z3, Z5) — ista oznaka za dvije stvari.
5. Komponente na zakrivljenoj plohi: teorija i P4–P6 rabe $F_H$, $F_V$ (iznosi + smjer s crteža), zadatci Z2/Z5 traže predznačene $F_x$, $F_z$/$F_y$. Skica Z2 rabi $F_H$, $F_V$ (vidi „Treba odluku”).
6. $x_V$ se mjeri od tri različite referentne crte (P4 vertikala kroz O, P5 stijenka, P6 zglob A) — tekst to svaki put navodi.
7. Z2 (redak 720): „gornju (konkavnu) stranu” — za $z=-H(x/L)^2$ gornja je strana konveksna.
8. P3: $F_2$ se pojavljuje samo u „Veza s proračunom” (skica), u rješenju samo $F_{2,r}$, $F_{2,t}$.
9. Uvod (redak 3): rezultanta na ravnu plohu je $F$; $F_R$ se rabi samo za zakrivljenu plohu — skice su usklađene s tim.
10. $F_m$ (izmjerena sila, Z6): pravilo „indeks $m$ samo model” u standardu stoji uz gustoće; namjerno zadržano (prijedlog ako se pravilo poopći: $F_{izm}$).
11. Generički $\rho$ u zadatcima s jednim fluidom (npr. Z1 morska voda 1025, P1 998) namjerno je zadržan; $\rho_u$, $\rho_v$ rabe se gdje su dva fluida (P3).


## Poglavlje 6

| simbol | naziv veličine | jedinica | gdje se pojavljuje |
|---|---|---|---|
| $F_U$ | sila uzgona | N | uvod, izvod, P1, Z1, skice |
| $\rho$; $\rho_{mv}$; $\rho_u$, $\rho_v$; $\rho_t$ | gustoća fluida u kojem tijelo pluta; morske vode (P5, spar); ulja/vode (P4, Z4, Z6, dva fluida); tekućine u tanku | kg/m³ | svugdje |
| $g$ | ubrzanje sile teže | m/s² | svugdje |
| $V$; $V_{ist}$ | volumen tijela (Z1); istisnuti volumen | m³ | izvod, P1–P6, Z1 |
| $V_u$, $V_v$ | istisnina u ulju / vodi | m³ | P4, Z6 |
| $V_{max}$, $m_{max}$, $\Delta m$ | najveća istisnina / masa, rezerva mase | m³; kg | P2 |
| $p_{pov}$; $p_1$, $p_2$ | tlak na slobodnoj površini (izvod Arhimeda); tlak na gornjoj/donjoj plohi | Pa | izvod (eq …matematicki-izvod-01/02) |
| $h_1$, $h_2$ | dubina gornje/donje plohe (izvod); uroni vrata areometra (Z4) | m; mm | izvod; Z4 |
| $A$; $A_{vl}$ | vodoravna površina prizme (izvod); površina vodne linije; površina presjeka spara (P6) | m² | izvod, BM izvod, P6 |
| $F_1$, $F_2$ | tlačne sile na gornju/donju plohu | N | izvod |
| $m$; $m_p$, $m_o$, $m_k$, $m_t$, $m_s$, $m_a$, $m_b$, $m_v$, $m_0$, $m_{uk}$ | masa tijela/sustava; pontona, opreme (P2), kompresora (P3) i ormara (P4), tereta (Z2), utega (Z3), akumulatora (Z6), broda (P5), vode u tanku (P5), početna masa (Z5), ukupna masa (P6) | kg, t | P1–P6, Z1–Z6 |
| $F_G$ | težina $mg$; točka $G$ je samo težište | N | uvod, P1, Z1 (naputak, kontrolni rezultat), „Napomene uz skice”; skice uvod, P1, P5, Z1, Z2 |
| $F_{neto}$; $F_d$ | neto sila (P1); dodatna sila držanja (Z1, samo „Napomene uz skice”) | N | P1; Z1 |
| $\Delta$ | masa istisnine $\rho V_{ist}$ | kg | izvodi, P4, Z3, Z6 |
| $L$, $b$, $H$ | duljina, širina, visina boka (trupa, pontona, spara: $H$ duljina spara u P6) | m | P2–P6, Z2–Z6 |
| $D$ | promjer spara | m | P6 |
| $d$ | promjer vrata areometra | mm | Z4 |
| $T$; $T_m$; $T_L$, $T_D$; $T_0$, $T_1$; $\Delta T$, $\Delta T_m$ | gaz; srednji gaz; gazovi lijevog/desnog ruba; gaz prije/poslije; promjena gaza | m | P2–P6, Z2, Z3, Z5, Z6 |
| $T_{v,L}$, $T_{v,D}$, $T_{v,m}$ | vodene dubine rubova / srednja (dva fluida) | m | P4 |
| $\delta$ | debljina sloja ulja | m | P4, Z6, izvod dva fluida |
| $f$, $f_L$ | nadvođe; preostalo nadvođe lijevog ruba | m | P2 (tekst), P5, P6 |
| $\varphi$ | kut poprečnog nagiba | rad, ° | izvodi, P3, P4, P5, Z3 |
| $\varphi_v$, $\varphi_{lim}$ | kut nestajanja stabiliteta; granični kut uronjenja ruba palube | ° | izvod GZ; P5 |
| B, G, M, K | centar uzgona, težište, metacentar, kobilica (dno) | – | uvod, izvodi, P3–P6, skice |
| $B'$, $B_\varphi$ | pomaknuti centar uzgona | – | izvodi |
| $KB$, $BM$, $KG$, $GM$, $KM$, $BG$, $BB'$ | udaljenosti stabiliteta | m | izvodi, P3–P6, Z3, Z5, Z6 |
| $KB_{eq}$, $BM_{eq}$, $GM_{eq}$ | ekvivalentne veličine za dva fluida | m | P4, Z6 |
| $KG_p$, $KG_k$, $KG_b$, $KG'$, $KG_0$ | visine težišta platforme, kompresora/ormara, broda, nova, početna | m | P3, P4, P5, Z5 |
| $GZ$ | poluga stabiliteta | m | izvodi |
| $y_B$; $y_{B,v}$; $\bar x$, $\bar x_{1,2}$; $A_1$, $A_2$ | bočni pomak centra uzgona; vodenog dijela; težišta trapeza i dijelova | m; m² | izvodi, P3, P4 |
| $z_{B,u}$, $z_{B,v}$ | visine centara uzgonskih doprinosa | m | P4 |
| $I_T$; $i_t$ | drugi moment vodne linije; slobodne površine tanka | m⁴ | izvodi, P4–P6 |
| $\delta GM$ | učinak slobodne površine | m | okvir „Učinak slobodne površine” |
| $e$; $e_G$; $e_t$ | udaljenost tereta od osi (pomak utega u Z3); bočni pomak težišta sustava; ekscentar tanka | m | P3, P4, Z3, Z6; P5 |
| $M_{pov}$, $M_{povratni}$, $W$, $A$ (integral) | povratni moment; rad; površina ispod GZ | N m; J; m rad | izvodi |
| $L_t$, $b_t$, $H_t$ | dimenzije tanka | m | P5 |

#### Nedosljednosti u tekstu (zabilježeno, ne rješavam)

1. **$A$**: vodoravna površina prizme (izvod), površina presjeka spara (P6) i površina ispod krivulje GZ (izvod) — tri značenja.
2. **$H$**: visina boka (P2–P5, Z2–Z6) i duljina spara (P6).
3. **$h_1$, $h_2$**: dubine ploha (izvod, m) i uroni vrata areometra (Z4, mm).
4. **Ukupna težina** nema jedinstvenu oznaku (P2: $mg$; P3/P4: $(m_p+m_k)g$, $\Delta g$); skice su prije koristile nepostojeću `G_uk` — zamijenjeno izrazima iz teksta.
5. **$e$**: u P3/P4/Z6 udaljenost tereta od osi; u Z3 pomak utega; $e_G$ i $e_t$ u P5 — lokalno definirano, dosljedno.
6. **$F_d$** postoji samo u „Napomenama uz skice” (Z1); P1 govori o „sili držanja” bez oznake, a fig-alt P1 je navodi kao nacrtanu.
7. **„Brod”** P5: tekst kaže „u sredini trupa, uz lijevu stijenku” i „Skica ne prikazuje L, L_t, H i H_t; e_t je ekscentar tanka” — $e_t$ nije na skici.
8. **$T_m$ (srednji gaz)** namjerno je zadržan: pravilo „indeks $m$ samo model” u standardu stoji uz gustoće, a oznaka je uobičajena u brodogradnji (prijedlog ako se pravilo poopći: $T_{sr}$).
9. **Generički $\rho$** u zadatcima s jednim fluidom (P1 more 1025; P2, P3, Z1–Z3, Z5 voda 998) namjerno je zadržan kao gustoća fluida u kojem tijelo pluta.


## Poglavlje 7

Izvor: stvarni tekst poglavlja (retci u zagradama). Oznake skica: prefiks datoteka `u08_*`.

| simbol | naziv veličine | jedinica | gdje se pojavljuje |
|---|---|---|---|
| $\vec v$, $v$ | brzina fluida (polje, srednja 1D brzina) | m/s | teorija (31, 79–88), svi primjeri |
| $\bar v_n$, $v_n$ | srednja normalna brzina; normalna komponenta | m/s | 85; Z2 (785) |
| $v_{max}$ | najveća brzina profila | m/s | P „srednja brzina iz profila” (95–113) |
| $R$, $r$ | polumjer cijevi; radijalna koordinata | m | 95–107 |
| $Q$ | volumenski protok | m³/s, L/s | 79, 162; svi primjeri |
| $\dot m$ | maseni protok | kg/s | 148–165; P1, P2, Z1 |
| $\dot m_{ul}$, $\dot m_{iz}$ | ulazni / izlazni maseni protok | kg/s | 3, 148, 157, 258–270 |
| $m_{KV}$, $dm_{KV}/dt$ | masa u KV; akumulacija | kg; kg/s | 3, 72, 148 |
| KV, KP | kontrolni volumen, kontrolna ploha | — | 3, 202–247 |
| $\vec n$ | vanjska jedinična normala KP | — | 3, 212, 222; Z2 (768) |
| $\vec v_{KP}$ | brzina kontrolne plohe | m/s | 212–243; P2 (427) |
| $\vec u$, $u$ | brzina krute granice (lopatica, klip) | m/s | 220; Z5 (856, 870) |
| $A$, $A_1$, $A_2$ | površina presjeka | m² | 79–88, 175–177; Z1, Z2 |
| $\rho$, $\rho_1$, $\rho_2$, $\rho_k$ | gustoća | kg/m³ | 162; Z1 (740) |
| $B$, $\eta$ | ekstenzivna veličina sustava; specifična veličina $dB/dm$ | — | RTT (202–228) |
| $V_{iz}$, $V_{ul}$ | izlazni / ulazni rubni volumen | m³ | 204 |
| $e$ | ukupna specifična energija | J/kg | 228 |
| $D_1$, $D_2$ | promjeri difuzora | mm | P1 (356) |
| $v_s$ | brzina broda | čv, m/s | P2 (410, 453) |
| $A_u$ | površina otvora zahvatnog usisa | m² | P2 (410) |
| $\psi$ | udio slobodne (otvorene) površine rešetke | — | P2 (410) |
| $w$, $w_r$ | relativna brzina prema brodu u otvoru / u rešetki | m/s | P2 (432–449) |
| $\vec i$ | jedinični vektor osi $x$ (prema pramcu) | — | P2 (427) |
| $L$, $b$ | duljina, širina spremnika | m | P3 ch (475) |
| $\rho_v$, $Q_A$ | gustoća vode; protok vode A | kg/m³, m³/s | P3 ch (475) |
| $s_r$, $\rho_B=s_r\rho_v$, $Q_B$ | relativna gustoća, gustoća i protok otopine B | —, kg/m³, m³/s | P3 ch (475, 496) |
| $D_3$, $v_3$, $A_3$, $Q_3$ | izlazni vod: promjer, brzina, površina, protok | mm, m/s, m², m³/s | P3 ch (475–509); Z3 (795) |
| $\rho_{mj}$ | gustoća homogenizirane mješavine | kg/m³ | P3 ch (482, 526), tumačenje skice kontrolnog volumena; Z6 |
| $h$, $h_0$, $h_1$, $\Delta h$, $dh/dt$ | razina, početna/ciljna, porast, brzina porasta | m, m/s | P3 ch (477–545) |
| $A_T$ | tlocrtna površina spremnika | m² | P3 ch (532); Z6 (882) |
| $\Delta V$, $\Delta m$, $t$ | akumulirani volumen, masa; vrijeme | m³, kg, s | P3 ch (550–562); Z5 |
| $\dot m_{ul}$, $Q_{ul}$ | ukupni ulazni maseni / volumenski protok | kg/s, m³/s | P3 ch (514–520); Z5 (849) |
| $D_1$, $D_2$, $D_3$, $v_1$, $v_2$, $v_3$, $Q_1$–$Q_3$ | T-komad: promjeri, brzine, protoci | mm, m/s, L/s | P4 (582–613) |
| $D_1$, $d$, $n$, $n'$, $A_d$, $A_n$, $v_d$ | rashladni kolektor | mm, —, m², m/s | P5 (628–677) |
| $\theta$ | kut između brzine i normale | ° | Z2 (768) |
| $Q_1$, $Q_2$, $Q_3$, $D_3$ | komora za miješanje | L/s, mm | Z3 (795) |
| $Q$, $D_1$, $D_2$, $D_3$, $v_2$, $v_3$ | razdjelna glava | m³/s, mm, m/s | Z4 (821) |
| $D$, $d$, $A_p$, $A_o$ | cilindar, otvor klipa, njihove površine | mm, m² | Z5 (849, 863) |
| $w$, $Q_{iz,rel}$, $v_{iz}$ | izlazna brzina relativna prema klipu; protok; apsolutna | m/s, L/s | Z5 (851, 863, 870) |
| $\ell_0$, $\ell(t)$, $s$ | početna duljina komore; duljina; hod klipa | m | Z5 (851, 863) |
| $h_{max}$ | visina početka odzračne cijevi | m | Z6 (882) |
| $\rho_{mv}$, $Q_{mv}$; $\rho_v$, $Q_v$; $Q_{iz}$; $\rho_{mj}$ | morska, slatka voda; odvod; mješavina | kg/m³, m³/h | Z6 (882, 901) |
| $n$ (FVM), $f$, $i$ | vremenska razina, ploha, ćelija | — | CFD (335–340) |

#### Uočene nedosljednosti oznaka (ne rješavam, samo bilježim)

1. **$s$ i $s_r$**: hod klipa $s$ (Z5) i relativna gustoća $s_r$ (P3) različite su oznake, kao u pog. 1; namjerno zadržano.
2. **$n$ za tri značenja**: jedinična normala $\vec n$, broj kanala $n=16$ (r. 628) i vremenska razina u FVM-u (r. 340) — iz konteksta jasno, ali isto slovo.
3. **$i$** je jedinični vektor $\vec i$ (P2) i indeks ćelije (CFD) — kontekstualno jasno.
4. Tumačenje skice kontrolnog volumena zadržava opće $\rho_A$, $\rho_B$ (opći dvoulazni slučaj), a uvodna skica „ρ₁, A₁, v₁” uz ṁ_ul; namjerno zadržano. Morska voda u P2 ($\rho=1025$) bez indeksa je jer je jedini fluid u zadatku.


## Poglavlje 8

Izvor: stvarni tekst poglavlja (retci u zagradama). Oznake skica: prefiks datoteka `u09_*`.

| simbol | naziv veličine | jedinica | gdje se pojavljuje |
|---|---|---|---|
| $p$, $p_1$, $p_2$ | (statički) tlak | Pa, kPa | 3, 21–29, P1, Z3 |
| $p/(\rho g)$ | tlačna visina | m | 3, 19, 63–69 |
| $v$, $v_1$, $v_2$ | brzina (srednja po presjeku) | m/s | svuda |
| $v^2/(2g)$ | brzinska visina | m | 3, 19, 60 |
| $z$, $z_1$, $z_2$ | geodetska visina | m | 3, 19–29; Z3 (772) |
| $\Delta z$ | razlika visina | m | 3 (uzlazni vod), P3 (403), Z6 (860) |
| HGL $=z+p/(\rho g)$ | piezometarska crta | m | 3, 49, 60, P3 (453), Z2 (748) |
| EGL $=$ HGL $+v^2/(2g)$ | energijska crta | m | 3, 55, 60, 263 |
| $\rho$, $g$, $\gamma=\rho g$ | gustoća, ubrzanje sile teže, specifična težina | kg/m³, m/s², N/m³ | 63–66 |
| $s$, $ds$, $A$, $dA$, $\theta$, $dm$ | koordinata, element, presjek, kut nagiba strujnice, masa elementa | m, m², rad, kg | izvodi (85–115, 168) |
| $dW_{tlak}$, $dW_{grav}$, $dE_k$ | rad tlaka, rad težine, promjena kin. energije | J | 172–193 |
| $\dot Q$, $\dot W$, $\dot W_s$, $\dot W_p$ | toplinski tok, snaga (rad vratila, tlačni rad) | W | 222–233 |
| $e$, $e_u$ | ukupna i unutarnja specifična energija | J/kg | 222 |
| $\alpha$ | korekcijski faktor kinetičke energije | — | 239–244, 255; Z6 (862) |
| $H_p$, $H_t$, $h_g$ | visina dobave crpke, visina turbine; gubitak visine | m | 247–263; P4 ch (485), Z6 (862) |
| $\dot m$ | maseni protok | kg/s | P1 (296) |
| $Q$ | volumenski protok | m³/s, L/s | P1, P3, P4, P5, Z1–Z6 |
| $A_1$, $A_2$ | ulazna / izlazna površina konfuzora | m² | P1 (296) |
| $\Delta p$ | razlika (pad) statičkog tlaka | Pa, kPa | P1 (300), P5 (583), P6 (623), Z2 (744) |
| $H$, $h$ | visina slobodne površine; visina otvora iznad tla | m | P2 (348) |
| $v_0$, $t$, $x$, $x_{max}$ | izlazna brzina mlaza; vrijeme leta; domet | m/s, s, m | P2 (361–390) |
| A, B, C | točke: površina bazena, slobodni izlaz, vrh sifona | — | P3 (403–453), Z6 |
| $D$ | promjer sifona / usisnog voda | mm | P3 (403), P4 (485), Z6 (860) |
| $z_A$, $z_B$, $z_C$ | visine točaka | m | P3 (420–444), Z6 (860) |
| $p_A$, $p_B$, $v_A$, $v_B$ | tlak i brzina u A, B | Pa, m/s | P3 (420–423) |
| $p_{atm}$ | atmosferski tlak | kPa; m | P3 (444), P4 (485), Z6 (860) |
| $p_{M,C}$, $p_{aps,C}$ | manometarski / apsolutni tlak u vrhu C | kPa; m | P3 (447–470), Z6 |
| $p_v$, $p_v/(\rho g)$ | tlak pare; visina tlaka pare | kPa; m | P3 (403, 473), P4 (485) |
| $z_P$, $z_u$ | visina ulaza crpke iznad / otvora košare ispod vodne linije | m | P4 ch (485) |
| $p_{aps,P}$, $p_{M,P}$ | apsolutni / manometarski tlak na ulazu crpke | kPa | P4 ch (517–529) |
| $NPSH_a$, $NPSH_r$, $z_{P,max}$ | raspoloživa / potrebna usisna visina; granična visina crpke | m | P4 ch (539–543) |
| $D_1$, $D_2$ | ulazni promjer, promjer grla Venturija | mm | P5 (569) |
| $\rho_u$, $\rho_{Hg}$, $\Delta h_m$ | gustoća ulja, žive; razlika razina žive | kg/m³, m | P5 (569) |
| $p_0$, $p_\infty$ | zaustavni, statički tlak (Pitot) | Pa | P6 (623–638) |
| $R$, $T$, $\nu$, $D_s$, $Re_s$ | plinska konstanta, temperatura, kin. viskoznost, promjer sonde, Re sonde | — | P6 (623–664) |
| $v'$ | brzina preračunata uz gušći zrak | m/s | P6 (656) |
| $H$, $d$ | visina vode iznad osi sapnice; promjer sapnice | m, mm | Z1 (716) |
| $D_1$, $d$, $\Delta p=p_1-p_2$ | Venturi: ulaz, grlo, razlika tlakova | mm, kPa | Z2 (744) |
| $D_1$, $D_2$, $z_1-z_2$, $p_2-p_1$ | silazno suženje | mm, m, kPa | Z3 (772–776) |
| $p_{M,A}$, $p_{M,S}$, $p_{M,0}$, $\Delta z_S$, S, A | Pitot broda: statički tlak u A, očitanje senzora S, zaustavni tlak, visina senzora | kPa, m | Z4 (801–820) |
| $D_1$, $d$, $p_{aps,1}$, $p_{aps,2}$, $p_1-p_2$ | izbor grla (grlo je presjek 2) | mm, kPa | Z5 (832) |
| $\zeta$, $\zeta_\Sigma$, $\zeta_C$ | koeficijenti gubitaka | — | Z6 (862) |

#### Uočene nedosljednosti oznaka (ne rješavam, samo bilježim)

1. **$\dot Q$ (toplinski tok) i $Q$ (volumenski protok)** u istom poglavlju (r. 222 i dalje) — razlikuje ih samo točka.
2. **$H$** u P2 (visina površine iznad tla) i u Z1 (visina vode iznad osi sapnice) — različite reference visine istog slova; svaka je u svom zadatku jasno definirana.
3. **$\rho$ bez indeksa** za morsku vodu u P4 (1025) i vodu u ostalim zadatcima: jedini fluid u zadatku, namjerno zadržano.


## Poglavlje 9

Izvor: stvarni tekst poglavlja (retci prema stanju 13. 10. 2026.).

| simbol | naziv veličine | jedinica | gdje se pojavljuje |
|---|---|---|---|
| $a$ | brzina zvuka (malog tlačnog poremećaja) | m/s | r. 3, 22–63, P1, Z1, Z3; skice uvod (−a, +a), Z1 |
| $a^*$ | kritična brzina zvuka (stanje $Ma=1$) | m/s | izvodi r. 237–258, 329–349 |
| $v$ | brzina toka (srednja po presjeku) | m/s | r. 32 ($a-\mathrm{d}v$), 101, 123, 145, Z3; skice uvod „v = 0”, Z1 „v = 0”, Z2 „v ≈ 0”, Z3, Z4, Z5 |
| $v_1$, $v_2$ | brzina ispred/iza normalnog vala | m/s | r. 309–346 |
| $p$ | statički tlak (apsolutni u jednadžbi stanja) | Pa, kPa, bar | r. 32, 53, 135 |
| $\rho$ | gustoća | kg/m³ | r. 22–56, 195 |
| $T$ | statička (apsolutna) temperatura | K | r. 53–63, P1, P3, Z1 (300 K), Z3; skica Z1 „T = 300 K” |
| $R$ | specifična plinska konstanta | J/(kg K) | r. 53, P1, P4, P6, Z1–Z5 |
| $\kappa=c_p/c_v$ | izentropski eksponent | – | r. 53 (izričito: $\gamma$ rezerviran za $\rho g$) |
| $c_p$, $c_v$ | specifični toplinski kapaciteti | J/(kg K) | r. 53, 151, 361 |
| $K$ | izentropski volumni modul kapljevine | Pa | r. 65 |
| $s$ | specifična entropija; indeks $s$ = konstantna entropija | J/(kg K) | r. 22, 25, 358–366 |
| $\Delta s$ | promjena specifične entropije kroz val | J/(kg K) | r. 361–366 |
| $h$, $h_0$ | specifična entalpija; zaustavna entalpija | J/kg | r. 145, 317, 320 (u ostatku knjige $h$ = visina; ovdje lokalno) |
| $L$ | duljina voda; razmak mjernih točaka | m | P1 (85 m), Z3 (1,20 m); skica Z3 „L = 1,20 m” |
| $t_a$; $t$ | akustičko vrijeme; trajanje upućivanja | s | P1; Z2 naputak |
| $t_{AB}$, $t_{BA}$ | vrijeme putovanja signala A→B, B→A | ms | Z3; skica Z3 |
| A, B | nepomične akustičke mjerne točke | – | Z3; skica Z3 |
| O | točka nastanka poremećaja | – | Z1; skice uvod i Z1 |
| $x$ | uzdužna os (predznak brzina) | – | Z1 („os $x$ sa skice”); skica Z1 |
| $Ma=v/a$ | Machov broj | – | r. 101; skice uvod (Ma < 1, Ma > 1), Z6 |
| $Ma^*=v/a^*$ | „karakteristični” Machov broj | – | r. 349, P5 |
| $D$ | promjer usisnog voda | m, mm | P2 |
| $Q$ | volumenski protok | m³/s | P2 |
| $A$ | površina presjeka | m², mm² | r. 120, 208–250 |
| $A^*$ | površina kritičnog presjeka (grla) | mm², m² | r. 3, 235–258, P4, P6, Z2; skice uvod „A*”, Z2 „ventil: A* = 120 mm²” |
| $A_e$ | izlazni presjek sapnice | mm² | r. 3, P6 (160 mm²); skica uvod „A_e” |
| $A_x$ | presjek u kojem stoji val | – (omjer $A_x/A^*$) | P6 r. 441 |
| $A_n$, $A_g$ | nazivna i izmjerena (geometrijska) površina izlaza | mm² | Z5; skica Z5 |
| $T_0$, $p_0$, $\rho_0$ | zaustavne veličine (indeks 0 u cijelom poglavlju) | K, Pa, kg/m³ | r. 151–168, P3, P4, P6, Z2, Z4, Z5; skice uvod „p₀, T₀”, Z2, Z5 |
| $p_{0,M}$ | manometarski zaustavni tlak komore | bar | Z4; skica Z4 |
| $p_{01}$, $p_{02}$; $T_{01}$, $T_{02}$ | zaustavni tlak/temperatura ispred i iza vala | kPa(abs); K | r. 3, 366, Z6; skica Z6 |
| $T^*$, $p^*$, $\rho^*$ | kritično stanje ($Ma=1$) | K, Pa, kg/m³ | r. 222–230, P4, Z4 |
| $\dot m$, $\dot m_{max}$, $\dot m_{ideal}$ | maseni protok; zagušeni (najveći); idealni kroz $A_g$ | kg/s | r. 252–265, P4, P6, Z2, Z5; skice Z2 „ṁ”, Z5 |
| $m$ | masa zraka za jedno upućivanje | kg | Z2; skica Z2 |
| $p_b$ | protutlak (nizvodni tlak izvan izlaza) | kPa(abs), bar(abs) | r. 3, P6 r. 406–408, Z2, Z4, Z5; skice uvod, Z2, Z5 |
| $p_{b,M}^{(I)}$, $p_{b,M}^{(II)}$ | manometarski protutlak postavke I i II | bar | Z4; skica Z4 „p_{b,M} (bar): I: 4,00; II: 3,00” |
| $p_e$, $Ma_e$ | izlazni tlak i Machov broj | kPa, – | P6, Z4; skica Z4 |
| $p_{e,\mathrm I}$, $p_{e,\mathrm{II}}$, $p_{e,\mathrm{III}}$ | karakteristični izlazni tlakovi KD sapnice | kPa | P6 |
| $p_{atm}$ | atmosferski tlak | kPa, bar(abs) | P4, Z4; skica Z4 |
| $p_1$, $p_2$, $T_1$, $T_2$, $\rho_1$, $\rho_2$, $Ma_1$, $Ma_2$ | stanja ispred (1) i iza (2) normalnog vala | kPa(abs), K, kg/m³, – | r. 3, 309–366, P5, P6, Z6; skice uvod (Ma₁ > 1, Ma₂ < 1), Z6 |
| $C_d$ | koeficijent istjecanja | – | Z5 |
| $\Lambda=p_{02}/p_{01}$; $\Lambda_{mj}$; $p_2/p_1$ | teorijski omjer zaustavnih tlakova; mjereni omjer; omjer statičkih tlakova (bez posebne oznake) | – | Z6 |
| $s(\cdot)$ | standardna nesigurnost | jedinica veličine | Z6 (uvedena pri prvom spomenu) |
| $\pm$ | standardna nesigurnost mjerenja | – | Z6; skica Z6 |

#### Uočene nedosljednosti (zabilježeno, ne rješavam)

1. $h$ — entalpija u ovom poglavlju (r. 145, 317), u ostatku knjige visina; tekst to ne napominje izričito.
2. Jedinice tlaka: Z6 tekst „kPa(abs)”, skica Z6 „kPa” (Napomene uz skice: „U Z6 svi označeni tlakovi su apsolutni” — pokriveno).


## Poglavlje 10

Izvor: stvarni tekst poglavlja (retci prema stanju 13. 10. 2026.). SVG-ovi ovog poglavlja nose prefiks `u11_`/`u10_` (prefiks nije broj poglavlja).

| simbol | naziv veličine | jedinica | gdje se pojavljuje |
|---|---|---|---|
| $\vec v$, $v_x$, $v_y$ | brzina fluida (srednja po presjeku), komponente | m/s | r. 24–27, cijelo poglavlje |
| $\vec v_1$, $\vec v_2$; $v_1$, $v_2$, $v_3$ | brzina na presjeku 1, 2, 3 | m/s | r. 5, 64, P2–P5, Z3; skice uvod, P2–P6, Z3, Z6 |
| ul, iz | indeksi ulaznog/izlaznog presjeka | – | r. 3, 24–27, 224 |
| $KV(t)$, $KP(t)$, $\vec v_{KP}$ | kontrolni volumen, kontrolna ploha, brzina plohe | –, m/s | r. 42–59; skice: „granica KV”, „KV prati lopaticu/ploču” |
| $\vec n$, $\vec n_i$ | vanjska jedinična normala | – | r. 3, 142–143 |
| $\mathrm dS$, $\mathrm dA$ | element plohe | m² | r. 46, 70, 139 (dva zapisa za isti pojam) |
| $\dot m$, $\dot m_1$, $\dot m_2$, $\dot m_3$ | maseni protok | kg/s | r. 5, 24, P2–P5, P7, Z1 |
| $\dot m_{rel}$ | maseni dotok kroz pomičnu granicu | kg/s | r. 181, P1, Z5 |
| $\sum\vec F$ | rezultanta vanjskih sila na fluid | N | r. 24, 47, 64 |
| $\vec F_p$, $\vec F_{p,i}=-p_{M,i}A_i\vec n_i$ | tlačna sila na presjecima | N | r. 3, 90–96; skica uvod „p_M1 A_1”, „p_M2 A_2”; P2 „p_M1 A_1” |
| $\vec F_G$ | težina fluida u KV | N | r. 3, 5, 90–96, 149; skica uvod „F_G” |
| $\vec R_{st\to f}$, $R_{st\to f,x}$, $R_{st\to f,y}$ | sila stijenke (konstrukcije) na fluid | N | r. 3, 5 (tumačenje skice), 90–99, P1–P6; skica uvod „R_st→f,x”, „R_st→f,y” |
| $\vec F$, $F_x$, $F_y$, $F$ | sila fluida na element ($\vec F=-\vec R_{st\to f}$) | N | r. 5, 96–99, P1–P6, Z3, Z4, Z6; skice P1 „F_x (fluid → lopatica)”, P3/P4/P6 „Fluid → …”, Z4 „F_x” |
| $\vec R$, $R_x$, $R_y$, $R$ | reakcija nosača/oslonca na element ($\vec R=-\vec F$) | N | r. 99, 477, 611, P5, Z3, Z4, Z6; skica P5 „R_x”, „R_y = 625 N” |
| $F_v$ | vlačna sila u vijcima prirubnice A-A | N | P2 |
| $F_P$ | sila mlaza na mjernu ploču | N | P2 (215 N); skica P2 „F_P”, „215 N” |
| $\beta$; $\alpha$ | koeficijent količine gibanja; Coriolisov koeficijent | – | r. 68–84, 157, P3 |
| $v_{lok}$, $v_{max}$, $r$, $R$ | lokalna brzina, najveća brzina, radijalna koordinata, polumjer cijevi | m/s, m | r. 73–82 — **$R$ ovdje polumjer** |
| $Q$, $Q_1$, $Q_2$, $Q_3$ | volumenski protok | m³/s; L/s (P2, P5, P7, Z4) | cijelo poglavlje; skice P6 „Q = 0,18 m³/s”, P7 „Q = 2,80 L/s”, Z1, Z3, Z4 „Q = 16,0 L/s”, Z6 |
| $\rho$; $\rho_v$; $\rho_{mv}$ | gustoća (opće formule, P1–P7); vode (preambula vježbi, $\rho=\rho_v=998$); morske vode (Z1, Z2) | kg/m³ | cijelo poglavlje |
| $p_{M1}$, $p_{M2}$, $p_M$, $p_{M,i}$ | manometarski tlak na presjeku; P6 jedan tlak $p_M$ | Pa, kPa | P2–P6, Z3, Z6; skice |
| $A$, $A_1$, $A_2$, $A_3$, $A_j$, $A_d$ | površina presjeka, mlaza, diska | m² | cijelo poglavlje |
| $D$, $D_1$, $D_2$, $D_3$, $d$ | promjer | mm, m | P1–P7, Z2, Z3, Z5, Z6; skice |
| $I=pA+\dot mv$ | impulsna funkcija | N | r. 101, P6 |
| $\vec e_{ul}$, $\vec e_{iz}$ | jedinični vektori ulaznog/izlaznog toka | – | P6 r. 774 |
| $\theta$ | kut koljena (P6, Z-interaktivno); kut skretanja relativnog toka lopatice (P1) | ° | P1 (165°), P6 (60°); skice P1 „θ = 165°”, P6 „θ = 60°” |
| $\theta_R$; $\theta_F$ | kut rezultante reakcije (P5); smjer sile fluida na koljeno (P6) | ° | P5, P6 |
| $\xi$ | koeficijent lokalnog gubitka | – | P3 |
| $\vec u$, $u$ | brzina krute granice (lopatica, ploča); obodna brzina mlaznice | m/s | r. 181, P1, P7, Z5; skice P1 „u = 12 m/s”, P7 „u = ωr”, Z5 „u = 8 m/s” |
| $\vec w=\vec v-\vec u$, $w$ | relativna brzina | m/s | r. 181, P1, P7; skice P1 „w = v − u (relativno)”, P7 „w” |
| $v_s$ | brzina broda | m/s | r. 183, Z1; skica Z1 |
| $v_j$ | brzina mlaza (relativno prema brodu / daleko iza diska) | m/s | r. 183–213, Z1, Z2; skice Z1, Z2 |
| $v_A$, $v_d$ | brzina napredovanja; brzina kroz disk | m/s | r. 196–213, Z2; skica Z2 |
| $F_T$, $P_T$ | potisak; snaga potiska | N, W | r. 183–213, Z1, Z2; skice Z1, Z2 „F_T (voda → …)” |
| $\eta_i$ | idealna (propulzijska) korisnost | – | r. 210, Z2 |
| $\Delta p$ | skok tlaka na disku | Pa | r. 198, Z2 |
| $\vec M_O$, $M_z$, $M_{O,z}$, $M_{R,z}$ | moment oko pola O / osi z; moment uklještenja | N m | r. 224–231, Z4 |
| $\vec r$, $r_1$, $r_2$ | položaj; radijusi presjeka | m | r. 221–231 |
| $v_{t1}$, $v_{t2}$, $v_t$ | tangencijalna komponenta apsolutne brzine | m/s | r. 231, P7 |
| $M_{st\to f}$, $M$, $M_0$ | moment stijenke na fluid; moment vode na glavu; moment zadržane glave | N m | P7; skica P7 „M”, „voda → glava” |
| $r$ (P7) | duljina kraka od osi vrtnje do mlaznice | m | P7 (0,25 m); skica P7 „r = 0,25 m” |
| $\omega$, $n$, $\omega_{max}$ | kutna brzina; brzina vrtnje | s⁻¹, min⁻¹ | P7; skica P7 |
| $P$, $P_{max}$ | snaga | W | P1, P7, Z5 |
| $x_C$, $y_C$ | koordinate točke C prema O; krak sile $F_x$ je $y_C$ | m | Z4; skica Z4 |
| O, C | uklještenje; središte udara | – | Z4; skica Z4 |
| $s$ | udio protoka kroz izlaz 2 | – | Z6; skica Z6 („s = 0,60”) — u pog. 9 $s$ = entropija |
| $R_{naz}$, $F_{max}$ | nazivna nosivost; najveća rezultanta | N, kN | Z6 |
| `A-A` | presjek prirubničkih vijaka | – | P2; skica P2 „prirubnica A–A” (crtica en-dash, tekst `A-A`) |
| 1, 2, 3 | numerirani presjeci | – | P2–P6, Z3, Z6; skice |

#### Uočene nedosljednosti (zabilježeno, ne rješavam)

1. **$R$** ima dva značenja: reakcija nosača (r. 99, P5, Z3) i polumjer cijevi (r. 82); krak u P7 sada je $r$.
2. **$\mathrm dS$ i $\mathrm dA$** za element plohe (r. 46/139 prema r. 70).
3. P6: tekst daje jedan tlak $p_M$ („ulazni i izlazni tlak jednaki”); skica je imala $p_{M1}$, $p_{M2}$ — usklađeno na $p_M$.
4. **$s$** u Z6 (udio protoka kroz izlaz 2) sudara se s entropijom $s$ (pog. 9) i sa $s_r$; namjerno zadržano (moguća nova oznaka, npr. $\Psi$).
5. Riješeni primjeri P1–P7 s jednim fluidom zadržavaju opći $\rho$ („Gustoća vode je $\rho=998$”); namjerno zadržano.


## Poglavlje 11

Izvor: stvarni tekst poglavlja (13. 10. 2026.), dopunski d01 r. 29–38, 132–142.

| simbol | naziv veličine | jedinica | gdje se pojavljuje |
|---|---|---|---|
| M, L, T, Θ | primarne dimenzije mase, duljine, vremena, temperature | – | uvod, Buckingham, izvodi |
| $F_i, F_\mu, F_g, F_p, F_\sigma$ | mjerila inercijske, viskozne, gravitacijske, tlačne sile i sile površinske napetosti | N | odjeljak mjerila sila |
| $L$ | karakteristična duljina; u izvodu pada tlaka duljina cijevne dionice | m | mjerila, $Re$, $Fr$, $We$, $St$; izvod $\Delta p$ |
| $v$ | karakteristična (srednja) brzina; u P4 relativna brzina zraka prema kapi; u P5/Z5 brzina vjetra/struje | m/s | svuda |
| $\rho$, $\mu$, $\nu$ | gustoća, dinamička i kinematička viskoznost | kg/m³, Pa s, m²/s | svuda |
| $\Delta p$, $p$, $p_\infty$ | razlika tlaka, statički tlak, referentni tlak neporemećene struje | Pa | $Eu$, $C_p$, izvod |
| $Re$, $Fr$, $Eu$, $We$, $Bo$, $St$, $Ma$ | bezdimenzijski brojevi | – | definicije, tablica, primjeri |
| $C_p$ | koeficijent tlaka | – | definicija |
| $\sigma_{kav}$, $p_{ref}$, $v_{ref}$, $\sigma_{kr}$ | kavitacijski broj, referentni tlak i brzina, kritična vrijednost | –, Pa, m/s, – | definicija, P3, Z3 |
| $p_v$ | tlak zasićene pare | Pa | P3, Z3 |
| $\sigma$ | površinska napetost | N/m | $We$, $Bo$, P4 |
| $\Delta\rho$, $L_c$ | razlika gustoća faza, kapilarna duljina | kg/m³, m | $Bo$, P4 |
| $f$ | frekvencija pojave (otpuštanja vrtloga) | Hz | $St$, P5, Z5 |
| $a$ | brzina zvuka | m/s | $Ma$, P5, Z2, Z4 ($a_m$) |
| $K$ | modul stlačivosti | Pa | Cauchyjev broj |
| $\lambda$; $\lambda_L=L_p/L_m$ | Darcyjev koeficijent trenja; mjerilo duljina | – | izvod; sličnost, P2, Z6 |
| $k_s$ ($\varepsilon$) | ekvivalentna hrapavost stijenke; jednadžbe izvoda pada tlaka još pišu $\varepsilon/D$ (vidi napomenu) | m | izvod, tablica |
| $C_D=F_D/(\tfrac12\rho v^2A)$, $F_D$, $A$ | koeficijent otpora, sila otpora, čeona/referentna površina | –, N, m² | Buckingham, P-kugla, Z4 |
| $n$, $k$, $\Pi_i$ | broj veličina, rang dimenzijske matrice, bezdimenzijske grupe | – | Buckingham, Z5 |
| $\Phi$, $\Phi_1$ | nepoznata funkcija bezdimenzijskih grupa (npr. $C_D=\Phi(Re)$) | – | izvodi, P-kugla, P5, Z5 |
| $D$ | promjer cijevi/kugle/cilindra | m, mm | izvodi, P1, P-kugla, P5, Z2, Z5 |
| $v_m$, $v_p$, $Q_p$, $Q_m$, $F_p$, $F_m$, $P_p$, $P_m$ | veličine modela i prototipa | m/s, m³/s, N, W | Froudeovo skaliranje, Z4, Z6 |
| $L_s$, $v_s$, $L_m$, $v_m$, $Re_s$, $Re_m$ | brod (prototip; indeks $s$ uveden pri prvoj uporabi) i model | m, m/s, – | P2, okvir „Fizikalno značenje” |
| $R_T$, $C_T$, $C_F$, $C_R$, $A_{opl}$, $C_{F,m}$, $C_{F,s}$ | ukupni otpor broda, koeficijenti ukupnog, trenja i preostalog otpora, oplakana površina | N, –, m² | Froudeova hipoteza, P2 |
| $v_A$, $v_B$, $\nu_v$, $\nu_u$ | brzina vode i ulja; kinematička viskoznost vode i ulja | m/s, m²/s | P1 |
| $Re_A$, $Re_B$, $Re_{kr}$, $v_{kr}$ | Reynoldsovi brojevi P1, orijentacijski prag, brzina vode pri $Re=2300$ | –, m/s | P1 |
| $D_1$, $D_2$, $A_1$, $A_2$, $v_1$, $v_2$, $p_1$, $p_2$, $Q$ | presjeci Venturija (1 ulaz, 2 grlo) | mm, m², m/s, Pa, L/s | P3 |
| $v_{2,\max}$, $Q_{\max}$ | idealizirani granični protok uz $p_2=p_v$ | m/s, L/s | P3 |
| $d$, $\rho_{zr}$, $\rho_v$, $We_{kr}$, $v_{kr}$ | promjer kapi, gustoća zraka i vode, prag raspada, kritična brzina | mm, kg/m³, –, m/s | P4 |
| $Q_1$, $Q_2$, $Ma_1$, $Ma_2$, $Q_{lim}$ | protoci i Machovi brojevi zračnog voda, granični protok za $Ma=0{,}3$ | m³/s, – | P5 |
| $D_d$, $f_n$, $v_{rez}$ | promjer dimnjaka, vlastita frekvencija, rezonantna brzina | m, Hz, m/s | P5 |
| $a$, $b$, $A$, $P$, $D_h=4A/P$ | stranice pravokutnog presjeka, površina, oplakani opseg, hidraulički promjer | m, m², m | Z1 |
| $p_M$, $p_{atm}$, $p_{aps}$, $p_{aps,min}$, $\sigma_{kav,1}$, $\sigma_{kav,2}$, $p_{M,min}$ | manometarski, atmosferski, apsolutni tlak; kavitacijski broj za $v_1$, $v_2$ | kPa, – | Z3 |
| $l_p$, $l_m$, $b_p$, $b_m$, $\rho_p$, $\rho_m$, $\nu_p$, $\nu_m$, $a_m$, $F_{D,m}$, $F_{D,p}$, $A_m$, $A_p$ | tetiva, raspon, svojstva fluida, brzina zvuka u modelu, sila otpora, referentna površina $bl$ | m, kg/m³, m²/s, m/s, N, m² | Z4 |
| $h_p$, $h_m$, $L_{pr}$, $L_{pr,m}$, $F_m$, $Q_{lim}$, $F_{min}$ | dubina i širina pravokutnog referentnog presjeka (prototip, model), izmjerena sila na modelu, laboratorijska ograničenja | m, N, L/s | Z6 ($L_{pr,m}$ u „Napomenama uz skice”) |

#### Zabilježene nedosljednosti u tekstu (ne rješavaju se ovdje)

1. **Oznaka $a$:** stranica kanala (Z1) i brzina zvuka (P5, Z2, $a_m$ u Z4).
2. **Oznaka $b$:** visina pravokutnog kanala (Z1) i raspon hidroprofila (Z4); u istoj figuri Z1–Z6.
3. **$L$:** karakteristična duljina, a u izvodu pada tlaka duljina dionice uz $D$ kao karakterističnu duljinu.
4. **$v_{kr}$ i $Q_{lim}$** imaju po dva lokalna značenja (P1 prijelaz / P4 raspad; P5 prag $Ma$ / Z6 laboratorijsko ograničenje).
5. **Hrapavost u izvodu pada tlaka:** jednadžbe (r. 125, 188, 194, 215) još pišu $\varepsilon/D$, a tekst istog izvoda (r. 180, 218) i ostatak knjige $k_s$, $k_s/D$; po standardu je $\varepsilon$ samo disipacija. Otvoreno (nije provedeno u ovom krugu).


## Poglavlje 12

Izvor: stvarni tekst poglavlja (13. 10. 2026.), dopunski d01/d02.

| simbol | naziv veličine | jedinica | gdje se pojavljuje |
|---|---|---|---|
| $\vec v$, $v_x,v_y,v_z$, $v_i$ | brzina fluida (polje), komponente | m/s | materijalna derivacija, NS, Couette, Z1 |
| $v(y)$, $v(r)$ | lokalna brzina u profilu | m/s | Couette–Poiseuille, Hagen–Poiseuille, Z4 |
| $v$ (srednja) , $v_{max}$ | srednja presječna i najveća brzina | m/s | izvod $\lambda=64/Re$ |
| $\overline{v}$, $\overline{v_i}$, $v'$, $v_i'$, $v'_{rms}$ | srednja brzina, fluktuacija, RMS fluktuacije | m/s | turbulencija, T3 primjer anemometra, uvodna skica |
| $t$ | vrijeme | s | Z1, uvodna skica (signal) |
| $x$, $y$, $z$; $r$ | koordinate; radijalna koordinata | m | posvuda |
| $a_x$; $a_{lok}$, $a_{kon}$, $a$ | materijalno ubrzanje; lokalno, konvektivno, ukupno | m/s² | P1, Z1 |
| $a$, $b$ (Z1) | parametri polja $v=at+bx^2$ | m/s²; m⁻¹s⁻¹ | Z1 |
| $\vec b$ | sila po jedinici mase | m/s² | Cauchyjeva jednadžba |
| $\rho$ | gustoća | kg/m³ | posvuda |
| $p$ | tlak | Pa | NS, uvodna skica (p, p + dp) |
| $dp/dx$; $(dp/dx)_{krit}$ | gradijent tlaka; kritični gradijent | Pa/m | Couette, Hagen–Poiseuille, Z4 |
| $\boldsymbol\sigma$, $\mathbf I$ | tenzor naprezanja, jedinični tenzor | Pa | Cauchy |
| $\boldsymbol\tau$, $\tau_{ij}$, $\tau_{xy}$ | viskozno naprezanje | Pa | izvod NS, uvodna skica |
| $\mathbf D$, $D_{ij}$ | tenzor brzine deformacije | 1/s | izvod NS |
| $\mu$; $\nu$ | dinamička, kinematička viskoznost | Pa s; m²/s | posvuda, Z2–Z5 |
| $H$ | razmak ploča (Couette, P2 ulje, Z2, Z4) | m | Couette, Z2, Z4 |
| $H_{st}$ | visina stepenice | m | P7 (stepenica) |
| $u$ | brzina gornje (krute) ploče | m/s | Couette, P2, Z2, Z4 |
| $R$, $D$, $L$ | polumjer, promjer, duljina cijevi (L: razmak priključaka u Z3) | m | Hagen–Poiseuille, P3, Z3 |
| $Q$ | volumenski protok | m³/s | Hagen–Poiseuille, P3, Z3, Z6 |
| $\Delta p$ ($=p_1-p_2$ u Z3) | pad tlaka | Pa | Hagen–Poiseuille, P3, Z3 |
| $p_1$, $p_2$ | tlakovi na priključcima | Pa | Z3 |
| $\lambda$ | Darcyjev koeficijent trenja | – | izvod |
| $Re$, $Re_x$, $Re_L$, $Re_s$, $Re_{st}$, $Re_l$ | Reynoldsovi brojevi ($Re_{st}$ prema visini stepenice, $Re_l$ prema tetivi profila) | – | posvuda |
| $\tau_{st}$; $\tau_0$ | smično naprezanje na stijenci; sila fluida na donju ploču po površini (x-komp.) | Pa | granični sloj; Z4 |
| $\delta_{99}$, $\delta_B$, $\delta$ | debljina graničnog sloja (99 %), Blasiusova referentna, turbulentna | m | granični sloj, P4, Z5, uvodna skica |
| $U_\infty$; $U_e$; $dU_e/dx$; $p_e$ | neporemećena brzina; vanjska brzina; gradijent; vanjski tlak | m/s; 1/s; Pa | granični sloj, P4, Z5 |
| $C_{f,x}$, $C_F$, $C_{F,m}$, $C_{F,s}$, $C_f$ | lokalni/ukupni koeficijent trenja | – | Blasius, P4, P7 |
| $L_m$, $v_m$, $x_1$ | duljina i brzina modela, položaj stimulatora | m; m/s | P4 |
| $I_t$ | intenzitet turbulencije | – | turbulencija, P6 |
| $k$, $\varepsilon$, $\omega$, $C_\mu$, $\ell$, $\mu_t$ | RANS veličine | m²/s², m²/s³, 1/s, –, m | P6 |
| $y^+$, $u_\tau$ | bezdim. udaljenost, brzina trenja | –; m/s | turbulencija |
| $X=x/H_{st}$, $X_r$, $U_{ref}$ | bezdim. položaj, priljubljivanje, ref. brzina | –; m/s | P7 (stepenica) |
| $k_s$ | ekvivalentna hrapavost | m (μm) | Z5 |
| $m$ | Falkner–Skanov eksponent | – | Z5 |
| $t_\nu$ | vrijeme viskozne difuzije | s | Z2 |
| $s(\cdot)$ | standardna nesigurnost ($s(\mu)$, $s(D)$, $s(L)$, $s(Q)$, $s(\Delta p)$) | jedinica veličine | Z3 |
| $h/h_f$, $\lambda_h$, $n_h$, $Q_g$, $Q_{sr}$, $Q_f$, $F_s$, $Q_{ext}$, $GCI_{sr}$, $GCI_f$ | omjer koraka mreže; omjer koraka susjednih mreža; opaženi red konvergencije; protoci na gruboj, srednjoj i finoj mreži; faktor sigurnosti … | – | Z6 a) |
| $C_D$, $E$, $s_E$, $s_{mj}$, $s_{num}$, $s_{uv}$; $\theta$ | otpor, odstupanje, standardna nesigurnost razlike (kriterij $\lvert E\rvert\le2s_E$), mjerna, numerička i nesigurnost usklađivanja uvjeta; napadni kut | –; ° | Z6 b) |

#### Neusklađenosti oznaka (zabilježeno, ne rješava se)

1. **$a$, $b$ u Z1:** $a$ je parametar polja (m/s²), a $a_{lok},a_{kon},a$ ubrzanja; $\vec b$ je u tekstu i sila po jedinici mase.
2. **Indeks ploha:** $\tau_{xy}$ u tekstu (simetrični tenzor), na $y$-plohi strogo je komponenta $\tau_{yx}$; jednako zbog simetrije.


## Poglavlje 13

| simbol | naziv veličine | jedinica | gdje se pojavljuje |
|---|---|---|---|
| $Q$; $Q_1$, $Q_2$; $Q_i$ | volumenski protok (u brojevnim karakteristikama u L/s); protoci grana | m³/s (L/s) | uvod, mreže, P3, P4, Z2–Z6 |
| $Q_A$, $Q_B$, $Q_C$, $Q_D$; $Q_{AB}$, $Q_{BC}$, $Q_{CD}$, $Q_{DA}$ | dotok/potrošnje u čvorovima; protoci cijevi petlje (pozitivno A→B→C→D→A) | L/s | P3 (petlja) |
| $v$, $v_s$, $v_{ref}$; $\bar v$ | srednja brzina, brzina na usisu, referentna brzina lokalnog gubitka | m/s | posvuda, NPSH |
| $D$, $L$, $A$ | unutarnji promjer, duljina, površina presjeka | m, m² | posvuda |
| $Re$, $\nu$, $\mu$, $\rho$ | Reynoldsov broj, viskoznosti, gustoća | –; m²/s; Pa s; kg/m³ | posvuda |
| $\lambda$, $\lambda_0$, $\lambda_k$ | Darcyjev koeficijent trenja (iteracije) | – | posvuda |
| $k_s$, $k_s/D$ | ekvivalentna hrapavost, relativna hrapavost | m (mm) | Colebrook, Z4, Z5 |
| $h_g$, $h_l$, $h_{loc}$, $h_{g,s}$ | ukupni, linijski, lokalni gubitak; usisni gubitak | m | posvuda, NPSH, Z6 |
| $h_{AB}$, $h_{AC}$, $h_{CD}$, $h_{DB}$, $h_{BC}$, $h_{DC}$, $h_{AD}$ | gubitci između čvorova | m | uvodna skica (Tumačenje), P3, Z3 |
| $\xi$, $\sum\xi$, $\zeta$ | lokalni koeficijent, zbroj, ukupni koeficijent dionice | – | posvuda |
| $R$, $R_i$, $R_{eq}$, $R_v$; $R_{AB}$… | hidraulički otpor ($h=RQ^2$) | s²/m⁵ | mreže, P3, Z3 |
| $h_v$ | gubitak na novom ventilu | m | Z3 |
| $H$; $H_1$, $H_2$ | energijska visina; u uvodnoj skici ukupna raspoloživa visina između slobodnih površina | m | bilanca, uvodna skica |
| $H_p$, $H_t$; $H_p(Q)$, $H_s(Q)$, $H_{s,V}$, $H_{stat}$, $H_{p,2}$ | visina dobave crpke / turbine u bilanci; karakteristike crpke, sustava, prigušenog sustava, statička visina, crpka pri $n_2$ | m | jedn. realne bilance, radna točka, P4, Z4, Z6 |
| $Q_{op}$, $H_{op}$; $H_V$ | radna točka | m³/s; m | P4, Z4, Z6 |
| $\Delta z$ | razlika razina slobodnih površina | m | Z4, $H_s$ |
| $s=n_2/n_1$, $n$ | omjer brzina vrtnje, brzina vrtnje | –; min⁻¹ | P4, Z6 |
| $P_h$, $P_{vr}$, $P_{el}$; $\eta_p$, $\eta_m$, $\eta_f$, $\eta$ | snage; učinkovitosti crpke, motora, pretvarača, ukupna | W; – | P5, Z4, Z6 |
| $E_{el}$, $E_V$, $E_s$, $\Delta E$, $t$ | godišnja energija, vrijeme rada | MWh/god; h/god | P5, Z6 |
| $NPSH_a$, $NPSH_r$ | raspoloživa/potrebna kavitacijska rezerva | m | NPSH, P6, Z6 |
| $p_{aps,s}$, $p_{atm}$, $p_v$; $z_s$ | apsolutni tlak na usisu, atmosferski, tlak pare; visina usisnog presjeka iznad slobodne površine ($z_s<0$ kod napunjenog usisa, Z6 $z_s=-1{,}8$ m) | Pa; m | NPSH, P6, Z6 |
| $p_1$, $p_2$, $\Delta p$, $\Delta p_{dop}$ | tlakovi presjeka, pad tlaka, dopušteni pad | Pa | bilanca, P1, Z1, Z2 |
| $\alpha$ | koeficijent kinetičke energije | – | bilanca |
| $\tau_{st}$, $\Phi$, $S_{ij}$ | smično naprezanje na stijenci, disipacija, tenzor brzine deformacije | Pa; W/m³; 1/s | izvod, „Fizikalni temelj” |

#### Neusklađenosti oznaka (zabilježeno, ne rješava se)

1. **$H$ višeznačan:** energijska visina $H_1$, $H_2$; ukupna raspoloživa visina u uvodnoj skici; „visina $H=12{,}0$ m” crpke u P5; $H_V$ u Z6.
2. **Ukupna učinkovitost:** $\eta_p$ (crpka, hidraulička/vratilna) u P5/Z4, a $\eta$ (električna–hidraulička) u Z6.
3. **Gubitci petlje** imenovani prema stvarnom smjeru ($h_{DC}$, $h_{AD}$), a protoci prema obilaznom smjeru ($Q_{CD}$, $Q_{DA}$) — tekst to objašnjava, ali miješa dva načina imenovanja.
4. **$s=n_2/n_1$** (P4, Z6) uz indeks $s$ za usis i sustav ($v_s$, $z_s$, $H_s$): namjerno zadržano; krivulja crpke pri $n_2$ označena je $H_{p,2}$ kako se ne bi sudarala s $H_s$.
5. **Z2:** fluid B (voda) ima $\rho_B$, $\nu_B$ (oznake slučaja A/B), a ne $\rho_v$, $\nu_v$; namjerno zadržano.


## Poglavlje 14

Napomena: SVG-ovi ovog poglavlja imaju naslijeđeni prefiks datoteke `u12_`, a ID-prefiks `u14…`.

| simbol | naziv veličine | jedinica | gdje se pojavljuje |
|---|---|---|---|
| $\vec c$, $c_1$, $c_2$; $c_{1t}$, $c_{2t}$; $c_{2x}$, $c_{2y}$; $c_{m1}$, $c_{m2}$ | apsolutna brzina; tangencijalne, x/y i meridijanske komponente | m/s | izvodi, P2–P4, Z3, Z4, uvodna skica |
| $u$, $u_1$, $u_2$ ($=\omega r_i$) | obodna brzina / brzina lopatice | m/s | posvuda |
| $\vec w$, $w_1$, $w_2$, $w_n$ | relativna brzina, normalna komponenta | m/s | posvuda |
| $k$ | omjer $w_2/w_1$ (gubitak relativne brzine) | – | izvod, P2, P3, Z3 |
| $\beta_1$, $\beta_2$ | kutovi lopatica, u cijelom poglavlju mjereni od smjera $-u$ ($\beta_2=0^\circ$ puni povrat) | ° | izvod, P2 (30°), P3 (20°), P4, Z3 (30,00°) |
| $\theta$ | kut skretanja mlaza od $+x$; za pokretnu lopaticu $\theta=180^\circ-\beta_2$ | ° | izvod, P1 (120°), Z2 (110°), Z3 (150,00°) |
| $\dot m$, $\dot m_{rel}$ | maseni protok kola / kroz pokretni KV | kg/s | posvuda |
| $\rho$, $A$, $d$, $D$, $D'$, $b$, $h$ | gustoća, površina, promjer sapnice/diska, širina/visina mlaza | kg/m³, m², m | posvuda |
| $r$, $r_1$, $r_2$; $b_1$, $b_2$ | polumjeri; širine kanala kola | m | P3, P4, Z4 |
| $n$, $\omega$ | brzina vrtnje, kutna brzina | min⁻¹, rad/s | P3, P4, Z4 |
| $M$, $M_{r\to f}$, $M_{f\to r}$, $M_{kolo}$ | moment | N m | P3, P4, Z4, Euler |
| $P$, $P_{r\to f}$, $P_{f\to r}$, $P_{kolo}$, $P_G$ | snage | W | posvuda |
| $e_{r\to f}$, $H_{th}$ | specifični rad, Eulerova visina | J/kg, m | P4, Z4 |
| $\eta_m$, $\eta_G$, $\eta_h$, $\eta_i$, $\eta_0$, $\eta_{prop}$, $\eta$ | učinkovitosti (η u Z5 = el.–hidr.) | – | P3, propulzija, Z5 |
| $F_x$, $F_y$; $\vec F_{f\to v}$, $\vec F_{v\to f}$, $\vec F_{f\to l}$, $\vec F_{l\to f}$, $F_{f\to lop,x}$ | komponente sile fluida na vodilicu/lopaticu i obratno | N | P1–P3, Z1–Z3 |
| $\vec R$, $R$; $\theta_R$ (P1) | reakcija nosača; kut reakcije iznad $-x$ | N; ° | P1, Z2 |
| $F_T$ | potisak | N | propulzija, P5 (dron), Z5, Z6 |
| $v_A$, $v_d$, $v_j$, $v_s$ | brzina napredovanja, kroz disk, dalekog traga/mlaza, broda | m/s | disk, P5, Z5, uvodna skica |
| $v_1$, $v_2$, $v$ | brzine mlaza na nepomičnoj vodilici/ploči | m/s | P1, Z1, Z2 |
| $C_{Th}$, $\Delta p_d$, $P_i$, $A_\infty$, $A_j$ | opterećenje potiskom, tlačni skok, idealna snaga, presjeci strujne cijevi | –, Pa, W, m² | disk, P4 (propeler) |
| $\chi$ | koeficijent sustrujanja ($w$ je relativna brzina) | – | propulzija, P4 (propeler) |
| $P_i$, $P_{st}$, $P_{uk}$, $t$; $FM$; $v_d$ | idealna (inducirana), stvarna, ukupna snaga drona; vrijeme; faktor učinka $FM=P_i/P_{st}$ (nije učinkovitost propulzije); brzina kroz disk | W, h; –; m/s | P5 (dron) |
| $Q$, $P_h$, $P_{el}$, $P_{el,max}$, $v_{j,A}$, $v_{j,B}$ | protok, snage, brzine mlaza kandidata | m³/s, W, m/s | Z5 |
| $\dot E_g$ | stopa gubitka mehaničke energije | W | Z3 |
| $m$, $g$, $a$, $F_{T,min}$, $m_{krit}$ | masa platforme, ubrzanje, granice | kg, m/s², N | Z6 |

#### Neusklađenosti oznaka (zabilježeno, ne rješava se)

1. **Sila na lopaticu:** $F_{f\to lop,x}$ (izvod), $\vec F_{f\to l}$ (P2, P3), na skicama $F_x$, $F_y$ uz napomenu „fluid → lopatica”.
2. **„Lopatica” / „vodilica”:** P2 tekst „zakrivljena lopatica”, a naslov skice bio je „Pokretna vodilica” (ispravljeno na skici).
3. U jednofluidnim primjerima zadržan je običan $\rho$; izraz „volumne sile” (body forces, r. 101, 474) nije protok i ostaje — namjerno zadržano.


## Poglavlje 15

| simbol | naziv veličine | jedinica | gdje se pojavljuje |
|---|---|---|---|
| $A$, $T$, $P$ | površina presjeka toka, širina slobodne površine, oplakani opseg | m², m, m | geometrija, Z3, Z6 |
| $R_h=A/P$, $y_h=A/T$, $D_h$ | hidraulički polumjer, hidraulička dubina, hidraulički promjer (usporedba) | m | geometrija, Z3 |
| $c=\sqrt{gy_h}$ | brzina dugog gravitacijskog vala (samo u ovom poglavlju) | m/s | Froude, Z1 |
| $Q$, $q=Q/b$ | volumenski protok, protok po širini | m³/s, m²/s | posvuda |
| $v$, $v_0$, $v_c$, $v_1$, $v_2$ | srednja brzina; početna (mirni dotok, uvodna skica); kritična; ispred i iza skoka | m/s | posvuda, P2, uvodna skica |
| $b$, $b_{baz}$ | širina pravokutnog kanala / dna trapeza; širina bazena | m | posvuda; Z6 |
| $y$, $y_0$, $y_1$, $y_2$, $y_c$, $y_n$, $y_{nv}$, $y_t$, $y_{kon}$, $y_{2,dop}$ | dubina; početna mirna (uvodna skica); silovit presjek ispred i mirni iza skoka; kritična; normalna; nizvodni vodostaj (P5); dubina na tjemenu praga (Z4); konstrukcijska dubina kanala (Z6); dopuštena spregnuta | m | posvuda |
| $Fr$, $Fr_1$, $Fr_t$, $Fr_y$ | Froudeov broj (kanal; ispred skoka; na tjemenu; brod u plitkoj vodi) | – | posvuda |
| $v_s$, $L$, $y$ | brzina broda, duljina broda, dubina vode | m/s, m, m | okvir „Fizikalno značenje” ($Fr_y=v_s/\sqrt{gy}$) |
| $E$, $E_{min}$, $E_1$, $E_2$, $E_t$, $\Delta E$ | specifična energija, minimum, u presjecima, na tjemenu, gubitak skoka | m | posvuda |
| $\alpha$, $\beta$ | korekcijski faktori kinetičke energije i količine gibanja | – | energija, skok |
| $z$ | geodetska visina dna ($z+E=$ konst.) | m | Tumačenje skice, Z4 |
| $m_{pok}$ | koeficijent pokosa trapeznog kanala (vodoravno : okomito) | – | Z3, Z6 |
| $\Delta z$, $\Delta z_{max}$ | povišenje dna (prag), najveće bez uspora | m | Z4 |
| $S_0$, $S_f$ | nagib dna, nagib energijske linije | – | postupno promjenjiv tok, Manning, Z6 |
| $h_g$ | ukupni gubitak visine između presjeka (linijski i lokalni) | m | jedn. postupno promjenjivog toka |
| $C_d$, $C_c$, $a$ | koeficijent istjecanja, kontrakcije, otvor ustave | –, –, m | kontrolne građevine |
| $C_{pr}$, $H$ | koeficijent preljeva; energijska visina iznad krune (jedino značenje $H$ u poglavlju) | –, m | preljev |
| $I$, $I_1$, $I_2$ | impulsna funkcija $pA+\dot mv$ | N | skok, uvodna skica, Z5 |
| $n$, $n_A$, $n_B$, $n_C$ | Manningov koeficijent | s/m^(1/3) | Manning, Z6 |
| $f$, $f_{min}$ | slobodni rub | m | Z6 |
| $Q_d$, $Q_{cap}$ | projektni protok, kapacitet | m³/s | Z6 |
| $\Delta_I=(I_2-I_1)/(\rho gb)$, $s_\Delta$, $u_q$ | rezidual impulsne bilance; standardna nesigurnost reziduala (kriterij $\lvert\Delta_I\rvert\le2s_\Delta$); standardna nesigurnost protoka po širini (samo kontrolni rezultat) | m², m², m²/s | Z5 |
| $\varepsilon_E$ | tolerancija energijskog reziduala | m | Z4 |

#### Neusklađenosti oznaka (zabilježeno, ne rješava se)

1. **$f$** slobodni rub (standard d01: $f$ nadvođe — srodan pojam, ali različit kontekst).
2. **$u_q$** u kontrolnom rezultatu Z5 (standardna nesigurnost protoka po širini) još slijedi stari zapis; standard propisuje $s(q)$. Otvoreno.
3. **$m_{pok}$:** osnovno slovo $m$ je masa, ali u poglavlju nema mase; indeks slijedi presedan $R_z$ uz $R$ — namjerno zadržano.
