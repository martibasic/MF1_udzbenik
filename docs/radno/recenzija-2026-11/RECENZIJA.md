# Recenzija priručnika — cijela knjiga (studeni 2026.)

Datum: 8. 11. 2026. Stanje: grana `konvencije-recenzije`; čitanja nad PDF-om izgrađenim iz
commita `9d343b3` (prije ispravaka pog. 13). Postupak: skill `recenzija-prirucnika`,
dorađen nakon pilota na pog. 13 ([pog13/RECENZIJA.md](pog13/RECENZIJA.md)).

Oznake: **P0** pogrešan ili opasan zaključak · **P1** bitna pogreška, ne predavati bez ispravka ·
**P2** vrijedi ispraviti · **P3** prijedlog. Svaki nalaz P0–P2 provjerio je zaseban agent u
izvoru, PDF-u ili računom (`G1`–`G4/PROVJERA.md`); svaki P1 dodatno je pročitao glavni agent.

## 1. Opseg i postupak

| Skupina | Poglavlja | Čitanja | Provjera |
| --- | --- | --- | --- |
| G1 | 1–4 | struka, primjena, urednik, student (pog. 3) | [G1/PROVJERA.md](G1/PROVJERA.md) |
| G2 | 5–8 | struka, primjena, urednik, student (pog. 8) | [G2/PROVJERA.md](G2/PROVJERA.md) |
| G3 | 9–12 | struka, struka drugim modelom, primjena, urednik, student (pog. 10) | [G3/PROVJERA.md](G3/PROVJERA.md) |
| G4 | 14, 15, 0, dodatci A–E | struka, primjena, urednik, student (pog. 14) | [G4/PROVJERA.md](G4/PROVJERA.md) |
| pilot | 13 | pet čitanja | [pog13/RECENZIJA.md](pog13/RECENZIJA.md) (provedeno) |

## 2. Opća ocjena

**Brojčano i fizikalno priručnik je pouzdan.** Stručni čitatelji ponovno su izračunali
rezultate svih riješenih primjera i kontrolnih rezultata svih 15 poglavlja (oko 180 brojčanih
rezultata) i nisu našli odstupanje veće od zaokruživanja. Nema nalaza P0. Četiri simulirana
studenta riješila su po dva zadatka (Z3 i Z6) bez naputka i svi su se rezultati podudarali s
ključem. Recenzenti ističu dosljedne predznake i oznake sila, neovisne provjere u primjerima,
T4 zadatke s intervalima i obrazloženom odlukom te razgraničenje nastavnog modela od propisne
ocjene.

Ono što priručnik dijeli od predaje recenzentima jest:

1. **osam bitnih nalaza (P1)**: tri netočne tvrdnje u tekstu, dva fizikalno nedosljedna stanja
   u zadatku i ilustraciji, nedefinirani podatak u T4 zadatku te dva poglavlja čiji zadatci
   ponavljaju riješene primjere ili drugo poglavlje;
2. **oko 160 potvrđenih nalaza P2**, od kojih su četiri petine tekstni ispravci bez promjene
   brojeva;
3. nekoliko **autorskih odluka** koje se ponavljaju kroz knjigu (ravnoteža struka,
   ponavljanje primjera u zadatcima, razine T).

## 3. Brojke

| Skupina | Stavke P0–P2 | P1 | P2 potvrđeno | Nepotvrdivo | Odbačeno ili sniženo na P3 |
| --- | ---: | ---: | ---: | ---: | ---: |
| G1 (1–4) | 45 | 1 | 37 | 2 | 5 |
| G2 (5–8) | 42 | 1 | 37 | 1 | 3 |
| G3 (9–12) | 54 | 3 | 42 | 3 + 1 | 6 |
| G4 (14–15, dodatci) | 52 | 3 | 41 | dijelovi 2 stavki | 11 |
| pog. 13 (pilot) | ≈ 30 | 2 | ≈ 20 | — | 4 |

Vrsta ispravka potvrđenih P2: TEKST ≈ 110, AUTORSKA ODLUKA ≈ 13, SKICA ≈ 6, BROJ/MODEL ≈ 5
(ostalo kombinirano). Detalji, mjesta i prijedlozi su u tablicama `PROVJERA.md`.

## 4. P1

| # | Mjesto | Nalaz | Vrsta | Prijedlog |
| --- | --- | --- | --- | --- |
| G1-01 | pog. 4 Z2, `task-spremnik-na-dizalici-dva-ubrzanja` | Spremnik „visi na lučkoj dizalici” i „ne njiše se”. Slobodno obješen teret pri stalnom ubrzanju kolica u ustaljenom stanju nagne se u smjer $\vec g_{eff}$ (≈ 7,8°), pa je površina usporedna s dnom i razlika razina 0, a ne 0,272 m. Brojevi ključa vrijede samo za kruto vođen spremnik. | TEKST (+ skica) | „…je kruto vođen pa se ne naginje ni njiše”; brojevi ostaju. |
| G2-01 | pog. 6, „Dublje — Učinak slobodne površine” (`u06:338`) | Napola pun tank „pri istoj istisnini” ne postoji: manje vode mijenja istisninu i težište. Stvarno stanje daje $GM\approx4{,}26$ m, više od punog tanka (4,23 m), a ne 4,16 m. Verifikator ponavlja istu pretpostavku. | BROJ/MODEL | Izričito reći da je masa nadoknađena drugdje (ista istisnina i težište) ili prikazati stvarno stanje; uskladiti `verify_u07.py`. |
| G3-01 | pog. 10 Z5 | Jedini T3 u poglavlju korak po korak ponavlja P1 (Peltonova lopatica); pitanje 5 odgovoreno je u tekstu (`u10:250`). | AUTORSKA ODLUKA | Zamjena zadatka u ciklusu revizije Z1–Z6. |
| G3-02 | pog. 10 P7 (`u10:857`) | $\dot m(w^2-u^2)/2\approx440$ W nazvan je „snagom mlazova”; mlazovi nose 369 W, a 440 W je snaga koju dovod predaje vodi (369 + 71 W). | TEKST | Preimenovati veličinu i navesti 369 W kao snagu mlazova. |
| G3-03 | pog. 12, uvod (`u12:3`) | „Najjednostavniji poseban slučaj [Navier–Stokesove jednadžbe] zakon je viskoznosti” — zakon viskoznosti poseban je slučaj konstitutivne veze, kako ispravno kaže `u12:95`. | TEKST | „…a zakon viskoznosti iz pog. 2 poseban je slučaj njezine konstitutivne veze.” |
| G4-01 | pog. 14 Z1, Z2, Z6 | Zadatci vježbaju pog. 10: Z2 je pog. 10 Z5 spojen s korakom 4 primjera P1 pog. 10; aktuatorski disk ($C_{Th}$, $FM$, $\chi$) nema samostalnog zadatka. | AUTORSKA ODLUKA | Zamjena Z1 ili Z2 zadatkom o aktuatorskom disku. |
| G4-02 | pog. 15 Z2, kontrolni rezultat (`u15:481`) | „$C_d$ pada jer brzina dolaska raste” — obrnuto: član brzine dolaska povećava $C_d$ (0,576 i 0,547 prema 0,572 i 0,530 bez njega); pad dolazi od relativnog smanjenja $y_0-y_1$. | TEKST | Ispraviti obrazloženje; brojevi ostaju. |
| G4-03 | pog. 15 Z6 (`task-klimatski-kanal`) | „Dopuštena spregnuta dubina” $y_{2,dop}=1{,}40$ m nigdje nije definirana; bilježnica je rabi kao gornju granicu, a P4 odluku veže uz nizvodni vodostaj. | TEKST (+ skica; BROJ ako se doda $y_{nv}$) | Definirati veličinu ili je zamijeniti nizvodnim vodostajem kao u P4. |

Pilot pog. 13 imao je još dva P1 (turbulentni λ bez riješenog primjera; nedefinirane oznake
uz NPSH); oba su provedena.

## 5. P2 po obrascima

Svaki obrazac javlja se u svim ili većini skupina; mjesta su u `PROVJERA.md`.

| Obrazac | Pravilo | Primjeri | Vrsta |
| --- | --- | --- | --- |
| Uvod unaprijed izvodi formule odjeljka; ista rečenica ili formula u uvodu, okviru i sažetku; ista jednadžba numerirana dvaput | K10 | u04:23 i :71; u03:190 i :195; pog. 6 (6.1 i 6.5), pog. 7, 8; pog. 14 (tangencijalna komponenta pet puta) | TEKST; uvod s formulama je autorska odluka od 15. 10., pa se uklanjaju samo doslovna ponavljanja |
| Kratice i oznake bez definicije ili s dva značenja | K5, K6 | NPSH (pog. 3, 8), RSS, GCI, ITTC, MRF, VOF, IoT; $F_p$, $v'$, $\delta_B$/$\delta_{99}$; $T$, $H_{tk}$ prije definicije | TEKST |
| Opisna upućivanja bez broja; dodatak u PDF-u kao „pog. A”; naslov poglavlja usred rečenice | K12 | „sljedeće poglavlje”, „prethodnog poglavlja”, „kasnije”; kapilarna duljina „iz pog. 2” (definirana u pog. 11) | TEKST; prikaz upućivanja je ispravak adaptera |
| Zadatak ponavlja riješeni primjer s drugim brojevima; razina T ne odgovara odluci | K15, matrica | pog. 1, 2, 4 (Z6 ≈ P4), pog. 6–8 (T4 omotač), pog. 7 (tri puta $Q=vA$), pog. 9, 11, 12 (Z3 obrnuti primjer) | AUTORSKA ODLUKA |
| Tvrdnje o praksi i empirijski pragovi bez izvora | K14 | We ≈ 12 pripisan Whiteu (nepotvrđeno), η propelera, brzine na usisu, pog. 14 bez ijednog izvora | TEKST + izvori; vrijednosti „po sjećanju” čitatelja nisu potvrđene |
| Primjena: vjerodostojnost i ravnoteža struka | K16 | ležaj statvene cijevi (omjer viskoznosti 10 umjesto ~130), brod u zavoju bez nagiba, grijač zraka (73 °C), uljni film 1 mm, pog. 1, 5 i 15 bez brodogradnje ili strojarstva | BROJ/MODEL ili AUTORSKA ODLUKA |
| Skice: preklapanje oznaka i oznake na krivom mjestu | K13 | sl. 5.8, 8.5, 8.7 (tisak), 10.1 (oznaka 1), 11.4 (os tlaka), radijalno kolo pog. 14 (kut lopatica) | SKICA |
| Ključ odsijeca odgovor dulji od 500 znakova | — | pog. 10 Z3 (zahtjev 3); `compact()` u generatoru | TEKST (`data-key-full="true"`) |
| Interni alat u vidljivom tekstu | K1 | `validate_cfd_vv.py` u dodatku D; putanja `data/cfd/…` u pog. 12 Z6 | TEKST |

## 6. Što je dobro i treba ostati

- **Brojke**: nijedan od ≈ 180 rezultata nije pogrešan izvan zaokruživanja; neovisne provjere u
  primjerima su stvarne (bilance, dva puta do istog tlaka, energija zatvara lanac).
- **Predznaci i tijela**: $\vec R_{st\to f}$, $\vec F$, $\vec R$ u pog. 10; $M_{r\to f}$ i
  $M_{f\to r}$ u pog. 14; normala $\vec n_f$ i strana koju fluid kvasi u pog. 5.
- **T4 zadatci** s intervalima, zajamčenim granicama i obrazloženom odlukom u svim skupinama.
- **Brodske primjene**: sondiranje tanka s talogom i inertnim plinom, balastni tank, separator
  goriva, kormilarski stroj, IS Code s izvorom i ogradom, lanac vučni bazen → ITTC 1957 →
  granični sloj trupa, Peltonova lopatica s oba optimuma.
- **CFD odlomci** ne iznose neprovedene rezultate; dodatak D pošteno označuje sintetičke pakete.

## 7. Redoslijed provedbe

| Korak | Stavke | Rizik |
| --- | --- | --- |
| 1 | P1 tekstni: G1-01, G3-02, G3-03, G4-02, G4-03 (definicija) | nizak; puni lanac provjera |
| 2 | P2 TEKST po skupinama (≈ 110 stavki) — jedno poglavlje po jedno, uz `prirucnik_stats --usporedi` | nizak |
| 3 | Ključ: `data-key-full` za pog. 10 Z3; prikaz „dodatak A” umjesto „pog. A”; upućivanje bez naslova usred rečenice | srednji; filtar i generator, render |
| 4 | Skice (sl. 5.8, 8.5, 8.7, 10.1, 11.4, kolo pog. 14) | srednji; izvedenice i tiskovni audit |
| 5 | G2-01 i ostali BROJ/MODEL (grijač zraka, ležaj statvene cijevi) | srednji; verifikator, D06 |
| 6 | Autorske odluke: G3-01, G4-01 i ponovljeni zadatci kao ciklus revizije Z1–Z6 po poglavlju | srednji; protokol prerade |

## 8. Odluke koje su autoričine

1. Ciklus revizije zadataka Z1–Z6 za pog. 10, 14 i poglavlja u kojima Z ponavlja P (obrazac 4).
2. Ravnoteža struka u pog. 1, 5 i 15 te lajtmotivi (offshore, dekarbonizacija).
3. Vidljivost bloka „Provjeri sebe” (sada skriven svugdje).
4. Nazivlje: „učinkovitost” ili „stupanj djelovanja”; „usisni koš” u značenju *sea chest*.
5. Primjene koje primjenski čitatelji smatraju nerealnima, a čije raspone nisu potvrdili izvorom.

## 9. Ocjena prolaza

- Provjera je odbacila ili snizila oko 25 stavki, među njima dvije tvrdnje o „nepostojećem”
  upućivanju koje postoji u bilježnici i prijedloge protivne autorskom ugovoru (uvod bez
  formula, pitanja kao uvod CFD odlomka).
- Primjenski čitatelji bez pristupa izvorima navode prakse „po sjećanju”; takve stavke ostaju
  nepotvrdive dok ih autorica ne potvrdi u literaturi.
- Uredničko čitanje i nakon ograničenja daje 30–40 nalaza P2 po skupini; za iduću reviziju
  vrijedi ga voditi poglavlje po poglavlje, zajedno s provedbom.

## 10. Provedba

**8. 11. 2026. — tekstni P1** (brojevi i rezultati nepromijenjeni; verifikatori, auditi i render prolaze):

| # | Provedeno |
| --- | --- |
| G1-01 | Pog. 4 Z2: spremnik je „kruto ovješen o kolica lučke dizalice” i „ne naginje se ni njiše”; napomena uz skice navodi da bi slobodno obješen teret zadržao površinu usporednu s dnom; opis skice i alt usklađeni. |
| G3-02 | Pog. 10 P7: 440 W je snaga koju dovod predaje vodi; mlazovi odnose $\dot m(w-u)^2/2\approx369$ W. |
| G3-03 | Pog. 12 uvod: zakon viskoznosti je slučaj konstitutivne veze koja ulazi u Navier–Stokesovu jednadžbu. |
| G4-02 | Pog. 15 Z2 ključ: $C_d$ pada jer se razlika $y_0-y_1$ relativno smanjuje; brzina dolaska taj pad djelomično nadoknađuje. U PDF-u ključ taj dio odgovora i dalje skraćuje (G4-15). |
| G4-03 | Pog. 15 Z6: $y_{2,dop}$ je dubina koju nizvodni vodostaj može održati; „Traži se 2” traži odluku ostaje li skok u bazenu; navedeno da $y_1$ daje brzotok ili pad dna; ključ i oznaka na skici („nizvodno”) usklađeni. |

Preostali P1 (G2-01, G3-01, G4-01) traže promjenu brojeva ili zadataka i čekaju autoričinu odluku.

**8. 11. 2026. — preostali P1 (najjednostavniji zahvat)**

| # | Provedeno |
| --- | --- |
| G2-01 | Pog. 6: ilustracija izrijekom pretpostavlja nadoknadu mase na istoj visini; dodana rečenica da bi bez nje $GM$ mogao porasti. Brojevi ostaju. |
| G3-01 | Pog. 10 Z5: ploča na kolicima kočenim silom $F_o$; student određuje ustaljenu brzinu (10,22 m/s; 6,17 m/s za 240 N) i objašnjava zašto sporija ploča prima veću snagu. Verifikator, bilježnica i skica usklađeni (`docs/radno/revizija_u10.md`). |
| G4-01 | Pog. 14 Z1: isti potisak s dva promjera propelera ($C_{Th}$, $\eta_i$, $P_i$) umjesto mlaza na nepomičnu ploču; novi ID, panel iz skice aktuatorskog diska pog. 10 (`docs/radno/revizija_u14.md`). |

**8. 11. 2026. — tekstni P2** (provedba po skupinama: `G1`–`G4/PROVEDBA.md`)

| Skupina | Provedeno | Preskočeno (BROJ/MODEL, SKICA, AUTORSKA ODLUKA, NEPOTVRDIVO, ODBAČENO) | Neprimjenjivo |
| --- | ---: | ---: | ---: |
| G1 (1–4) | 32 | 13 | 0 |
| G2 (5–8) | 29 | 13 | 0 |
| G3 (9–12) | 36 | 15 | 3 |
| G4 (14–15, dodatci) | 36 | 13 | 3 |

Glavni agent pregledao je izmjene: nijedan konačni ili kontrolni rezultat nije promijenjen;
uklonjeno je šest doslovno ponovljenih numeriranih jednadžbi bez upućivanja (780 umjesto 786);
zaokruženi su međurezultati u pog. 3 (K8); ključevi pog. 10 Z3, 14 Z2 i 15 Z2 ispisuju se u
cijelosti (`data-key-full`); novi ID-jevi `sec-provjera-sile-na-koljeno` i
`tbl-bezdimenzijski-brojevi`; u pog. 12 iznos $\tau_{st}=\mu|dv/dr|_R$ usklađen s konvencijom.

Za autoričino čitanje (formulacije provedbe bez vanjskog izvora): kriterij za zanemarivanje
trenja (pog. 8), samousisna izvedba ili zalijevanje u pog. 8 P4, ograde „nastavna procjena” i
„kao orijentacija” (pog. 6–8, pog. 3 ulaž), ograda „otvor malen prema uzvodnoj dubini” (pog. 15),
definicija meridijanske komponente (pog. 14). Preskočeno ostaje: izvori za dodatak E
(`references.bib`), skice, promjene brojeva i autorske odluke iz `PROVJERA.md`.

**8. 11. 2026. — brojevi, izvori i skice** (verifikatori, auditi, oba rendera i pregled PDF-a prolaze; PDF 353 str.)

| # | Provedeno |
| --- | --- |
| G1-10 | Pog. 4 ključ Z5 i Z6: jedna razina zaokruživanja (K8); `verify_u04.py` usklađen. |
| G1-11 | Pog. 4 uvod: mjerodavna je širina spremnika prema središtu zavoja $b_t$; sl. 4.1 usklađena. |
| G1-12 | Pog. 2 ležaj: temperature 10 °C i 50 °C odgovaraju zadanom omjeru viskoznosti 10; dodana rečenica o rasponu 0–90 °C; rezultati nepromijenjeni. |
| G1-30 | Pog. 2: $h_{kap}$ umjesto $h_{cap}$. |
| G3-06 | Pog. 12 Z3: vlastiti podatci (glikolna otopina) umjesto podataka primjera P3: $\mu\approx4{,}00$ mPa s, $s(\mu)\approx0{,}11$ mPa s, $Re\approx8{,}4$; verifikator i bilježnica usklađeni (`docs/radno/revizija_u12.md`). |
| G4-16 | Pog. 15 Z4: $y_0$ i $E_0$ za mirnu uzvodnu dubinu; skica, naputak i ključ usklađeni. |
| Literatura | Dodano sedam provjerenih izvora (Versteeg i Malalasekera, Ferziger i dr., GUM, MAN Energy Solutions, McGeorge, Taylor, ISGOTT) s citatima u pog. 3, 14, 15 i dodatcima D i E (`LITERATURA_PRIJEDLOG.md`). |
| Skice | Dvanaest zahvata u `SKICE_PROVEDBA.md` (preklapanja oznaka na sl. 5.8, 8.5, 8.7, 10.1, 10.9, 11.4, 14.5, 14.7, 15.2, skici ležaja i mikrodozatora; oznaka „2” na sl. 13.2). Sl. 8.5 i 11.4 sada su široke (WIDE). |

Nisu dodani: Virag, Dixon i Carlton (nepotpuni bibliografski podatci). Čekaju autoricu
autorske odluke iz `PROVJERA.md` (G1-40, G1-43, G2-23, G2-24, G4-20), vidljivost „Provjeri
sebe”, nazivlje „učinkovitost”/„stupanj djelovanja”, ravnoteža struka i licenca.
