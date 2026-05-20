## Tipične pogreške i preventivni filtar prije računa

Ovaj dodatak nije pasivni prilog, nego radni sloj za provjeru modela prije računa, tijekom računa i prije predaje zadatka. Većina pogrešaka u zadacima mehanike fluida ne nastaje u zadnjem retku algebre, nego mnogo ranije: pri izboru modela, referentne točke, kontrolnog volumena, predznaka ili tipa protoka.

## Globalna provjera prije računa

::: {.mf1-checklist}
<p class="mf1-box-label">Brza provjera</p>

- Potrebno je odrediti model problema: hidrostatika, relativno mirovanje, kontinuitet, Bernoulli, količina gibanja ili cjevovod.
- Potrebno je provjeriti vrijede li pretpostavke modela ili je granica njihove primjene već prijeđena.
- Potrebno je nacrtati skicu, strujnicu ili kontrolni volumen prije prve jednadžbe.
- Potrebno je potvrditi da su jedinice konzistentne i u istom sustavu.
- Potrebno je provjeriti ima li rezultat fizikalnog smisla i razumnog reda veličine.
:::

<p class="mf1-signal-note">Vizualni tragovi za brzo listanje dodatka: <span class="mf1-signal-chip">ρ / γ / p</span> osnovne veličine, <span class="mf1-signal-chip">μ / ν / σ</span> svojstva fluida, <span class="mf1-signal-chip">F / M</span> sile i momenti, <span class="mf1-signal-chip">Q / ṁ / h_w</span> protoci i gubici.</p>

## Tablica tipičnih pogrešaka po poglavljima

| Poglavlje | Signal | Tipičan lom modela | Što provjeriti prije računa |
| --- | --- | --- |
| <span class="mf1-ch-ref"><span class="mf1-ch-code">U01</span><span class="mf1-ch-title">Osnove fluida i Pascalov zakon</span></span> | <span class="mf1-signal-chip">ρ / γ / p</span> <span class="mf1-signal-chip">F / A</span> | Miješanje gustoće, specifične težine i tlaka; zamjena istoga tlaka istom silom na oba klipa; tretiranje hidraulične preše kao stvaranja rada niotkuda. | Potrebno je jasno odvojiti $\rho$, $\gamma$ i $p$, razlikovati isti tlak od iste sile i provjeriti gdje se dobitak sile plaća većim hodom. |
| <span class="mf1-ch-ref"><span class="mf1-ch-code">U02</span><span class="mf1-ch-title">Viskoznost, površinska napetost i kapilarnost</span></span> | <span class="mf1-signal-chip">μ / ν / σ</span> <span class="mf1-signal-chip">\cos\theta</span> | Miješanje dinamičke i kinematičke viskoznosti; zaboravljena pretvorba $\text{mm}^2/\text{s}$ u $\text{m}^2/\text{s}$; korištenje pogrešnoga mehanizma za kapilarnost ili smičanje. | Potrebno je utvrditi govori li zadatak o unutarnjem trenju, površinskoj napetosti ili kontaktnom kutu te treba li koristiti $\mu$, $\nu$ ili njihov odnos s gustoćom. |
| <span class="mf1-ch-ref"><span class="mf1-ch-code">U03</span><span class="mf1-ch-title">Hidrostatička raspodjela tlaka i manometrija</span></span> | <span class="mf1-signal-chip">p_{aps}</span> <span class="mf1-signal-chip">p_M</span> <span class="mf1-signal-chip">p_v</span> | Miješanje apsolutnog, manometarskog i vakuumskog tlaka; nekonzistentni predznači u manometarskoj putanji; zaborav da zatvoreni plinski jastuk mijenja tlak na slobodnoj površini tekućine. | Potrebno je odrediti koji je poznati referentni tlak, raste li tlak pri kretanju prema dolje i pripada li slobodna površina atmosferi ili zatvorenom plinu. |
| <span class="mf1-ch-ref"><span class="mf1-ch-code">U04</span><span class="mf1-ch-title">Relativno mirovanje fluida</span></span> | <span class="mf1-signal-chip">a / g</span> <span class="mf1-signal-chip">g_{eff}</span> | Primjena obične hidrostatike bez efektivnog ubrzanja; pogrešan smjer nagiba slobodne površine; korištenje geometrije mirne razine i onda kad je spremnik već na granici prelijevanja ili ogoljavanja. | Potrebno je prvo odrediti efektivno polje sila, tek zatim geometriju slobodne površine i provjeriti vrijedi li očuvanje volumena bez gubitka tekućine. |
| <span class="mf1-ch-ref"><span class="mf1-ch-code">U05</span><span class="mf1-ch-title">Hidrostatske sile na ravne plohe</span></span> | <span class="mf1-signal-chip">F</span> <span class="mf1-signal-chip">y_{CP}</span> | Računanje rezultante samo iz dubine, bez provjere mjesta djelovanja sile; miješanje jednolikoga pretlaka i linearnoga hidrostatičkog dijela u zatvorenom spremniku. | Potrebno je razlikovati veličinu sile od položaja centra tlaka i odrediti koje se opterećenje zbraja kao konstantan tlak, a koje kao gradijent s dubinom. |
| <span class="mf1-ch-ref"><span class="mf1-ch-code">U06</span><span class="mf1-ch-title">Zakrivljene plohe i rastav sila</span></span> | <span class="mf1-signal-chip">F_H</span> <span class="mf1-signal-chip">F_V</span> <span class="mf1-signal-chip">V^*</span> | Tretiranje zakrivljene plohe kao ravne; pogrešan volumen za vertikalnu komponentu sile; automatska pretpostavka da je $F_V$ uvijek prema gore. | Potrebno je odvojiti projekciju za $F_H$ od volumena koji određuje $F_V$ te provjeriti nalazi li se imaginarni volumen stvarno ispod slobodne površine ili ga geometrija i plinski jastuk okreću. |
| <span class="mf1-ch-ref"><span class="mf1-ch-code">U07</span><span class="mf1-ch-title">Uzgon, plivanje i stabilnost</span></span> | <span class="mf1-signal-chip">F_U</span> <span class="mf1-signal-chip">V_{ist}</span> <span class="mf1-signal-chip">M</span> | Zamjena volumena tijela istisnutim volumenom; miješanje ravnoteže i stabilnosti; ignoriranje uloge zarobljenoga zraka ili drugoga fluida kod plivanja na granici dvaju medija. | Potrebno je računati uzgon iz stvarno istisnutoga volumena, razdvojiti ravnotežu sila od momentne stabilnosti i utvrditi koji dio uzgona dolazi iz kojeg fluida ili plinskog džepa. |
| <span class="mf1-ch-ref"><span class="mf1-ch-code">U08</span><span class="mf1-ch-title">Kontrolni volumen i kontinuitet</span></span> | <span class="mf1-signal-chip">Q / ṁ</span> <span class="mf1-signal-chip">dm_{CV}/dt</span> | Mehaničko pisanje $A_1 v_1 = A_2 v_2$ bez crtanja kontrolnog volumena; zaboravljena akumulacija; korištenje volumenskoga umjesto masenoga protoka kad je plin stlačiv ili kad izlazna ploha nije običan kružni presjek. | Potrebno je odrediti koji presjeci ulaze u bilancu mase, radi li se s $Q$ ili s $\dot{m}$ i je li pravilno prepoznata stvarna izlazna površina sustava. |
| <span class="mf1-ch-ref"><span class="mf1-ch-code">U09</span><span class="mf1-ch-title">Bernoullijeva jednadžba idealnog fluida</span></span> | <span class="mf1-signal-chip">p/(\rho g)</span> <span class="mf1-signal-chip">v^2/(2g)</span> <span class="mf1-signal-chip">z</span> | Pisanje Bernoullija bez provjere uvjeta primjene; pogrešan izbor točaka ili miješanje idealnoga i realnoga modela; zamjena statičkoga, stagnacijskoga i manometarskoga tlaka u grlu Venturija ili sličnog uređaja. | Potrebno je odabrati dvije fizikalno smisleno postavljene točke, zatvoriti idealne pretpostavke i jasno razdvojiti koji tlak stvarno ulazi u Bernoullijevu bilancu. |
| <span class="mf1-ch-ref"><span class="mf1-ch-code">U10</span><span class="mf1-ch-title">Realni Bernoulli i gubici</span></span> | <span class="mf1-signal-chip">h_l</span> <span class="mf1-signal-chip">\xi</span> <span class="mf1-signal-chip">h_w</span> | Dodavanje gubitaka kao naknadnoga popravka idealnog Bernoullija; miješanje $\lambda$, $\xi$, Pa i m fluida. | Potrebno je unaprijed popisati sve linijske i lokalne gubitke i prebaciti ih u isti energijski oblik. |
| <span class="mf1-ch-ref"><span class="mf1-ch-code">U11</span><span class="mf1-ch-title">Količina gibanja i sile strujanja</span></span> | <span class="mf1-signal-chip">\sum \vec F</span> <span class="mf1-signal-chip">\dot m\vec V</span> | Korištenje samo iznosa brzine umjesto vektora; zamjena sile na fluid silom fluida na konstrukciju. | Potrebno je zapisati jednadžbu po komponentama i jasno odrediti za koji se sustav računa sila. |
| <span class="mf1-ch-ref"><span class="mf1-ch-code">U12</span><span class="mf1-ch-title">Pokretne lopatice i potisak</span></span> | <span class="mf1-signal-chip">c / w / u</span> <span class="mf1-signal-chip">F_t</span> | Korištenje apsolutne brzine ondje gdje treba relativna; poistovjećivanje maksimuma sile s maksimumom snage. | Potrebno je razlikovati $v$, $w$ i $v_{rel}$ te odrediti traži li se sila, moment ili snaga. |
| <span class="mf1-ch-ref"><span class="mf1-ch-code">U13</span><span class="mf1-ch-title">Cjevovodi</span></span> | <span class="mf1-signal-chip">Re</span> <span class="mf1-signal-chip">\lambda</span> <span class="mf1-signal-chip">h_w</span> | Računanje gubitaka prije određivanja režima strujanja; miješanje pravila serijskog i paralelnog spoja; zanemarivanje da se protok može odvojiti prema ispuštu ili grani. | Potrebno je najprije odrediti $v$, zatim $Re$, pa tek onda $\lambda$, $h_w$ i logiku mreže, te zatvoriti kontinuitet u svakom čvoru ili na mjestu ispušta. |

## Kako koristiti ovu tablicu bez lutanja

Najkorisnija je u tri trenutka:

1. prije početka zadatka, da potvrdiš da si u pravom modelu
2. usred računa, kad broj ili predznak počnu izgledati šumnjivo
3. na kraju, kao kratka samoprovjera prije zaključivanja rješenja

Ako se rezultat raspadne već na ovoj tablici, bolje je vratiti se na početnu skicu nego produžavati algebarski lanac.

## Brza završna provjera prije predaje rješenja

::: {.mf1-decision-grid}
::: {.mf1-decision-step}
<span class="mf1-step-index">1</span>

<p class="mf1-box-label">Provjeri model</p>

Hidrostatika nije Bernoulli, a cjevovod nije samo jedan Darcy-Weisbachov zapis bez geometrije i režima strujanja.
:::

::: {.mf1-decision-step}
<span class="mf1-step-index">2</span>

<p class="mf1-box-label">Provjeri što je zadano</p>

Velik broj pogrešaka nastaje jer se miješaju tlak i sila, maseni i volumenski protok ili apsolutni i manometarski tlak.
:::

::: {.mf1-decision-step}
<span class="mf1-step-index">3</span>

<p class="mf1-box-label">Provjeri smjer i geometriju</p>

Predznači, projekcije, vektorske komponente, istisnuti volumen i odabir točaka često odlučuju više od same numerike.
:::

::: {.mf1-decision-step}
<span class="mf1-step-index">4</span>

<p class="mf1-box-label">Tek onda vjeruj rezultatu</p>

Ako broj nema fizikalni smisao, uredna algebra ne spašava pogrešan model.
:::
:::

::: {.mf1-warning}
<p class="mf1-box-label">Najčešća pogreška</p>

Najčešća završna pogreška jest preskočiti samoprovjeru zato što račun "izgleda uredno". U MF1 uredan broj bez fizikalnog smisla obično znači da je model, geometrija ili referentni tlak bio krivo postavljen mnogo prije zadnjeg retka.
:::

::: {.mf1-mini-summary}
<p class="mf1-box-label">Operativna namjena dodatka</p>

<span class="mf1-ch-ref"><span class="mf1-ch-code">D03</span><span class="mf1-ch-title">Tipične pogreške po poglavljima</span></span> je završni filtar prije povjerenja rezultatu. Služi za brzo prepoznavanje tipičnih kvarova modela, predznaka, geometrije i jedinica prije nego što pogreška postane "uredno" rješenje.
:::







