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
