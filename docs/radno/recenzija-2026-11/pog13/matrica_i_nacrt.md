# Pog. 13 — matrica ishoda i obrnuti nacrt

Pilot skilla `recenzija-prirucnika`, 8. 11. 2026., commit `5ec5ff1`, PDF str. 245–262.
Koraci 2 i 3 skilla; izradio glavni agent prije čitanja izvještaja ostalih čitatelja.

## Profil (korak 1)

`prirucnik_stats.py`: 4624 riječi, 293 rečenice, prosjek 14,1, nijedna iznad 40 riječi,
54 istaknute formule (sve numerirane), 6 P, 6 Z (T1, T1, T2, T2, T3, T4), 2 bloka
„Granica modela”, 4 CFD odlomka, 0 nalaza K1–K13. `audit_publication`, `verify_all`
prolaze. Brojevi P1, P2, P4–P6 i Z1–Z6 ponovno izračunani: svi kontrolni rezultati
reproducirani (Z4: $Q=19{,}030$ L/s, $H=19{,}136$ m, $\lambda=0{,}020812$; Z5: 33,13 / 10,78 /
3,56 m, nakon starenja 14,03 m).

## Matrica ishoda (korak 2)

Red matrice: *Gubitci, cjevovodi, crpke i mreže* — obvezna provjera „iterativna radna
točka i energetski ledger”, lajtmotiv „hlađenje i urbana mreža”, 12 h.

| Element | Gdje | Stanje |
| --- | --- | --- |
| 1. temeljno objašnjenje ili izvod | `eq-realna-energijska-bilanca`; izvod $\lambda=8\tau_{st}/(\rho v^2)\to64/Re$; Colebrookova iteracija; Hardy–Cross linearizacija; `eq-radna-tocka`; lanac snaga `eq-elektricna-snaga-crpke` | ostvareno |
| 2. riješeni primjer s neovisnom provjerom — radna točka | `ex-radna-tocka-vfd` | **djelomično**: karakteristika sustava zadana je kvadratno sa stalnim koeficijentom; nijedan riješeni primjer ne računa radnu točku s $\lambda(Re)$ koji se mijenja s protokom. Iterativna radna točka prvi se put pojavljuje u Z4 (T2), uz obvezni računski alat. Provjera u P4 tumači omjer, ne vraća rješenje u obje krivulje. |
| 2. riješeni primjer — energetski lanac | `ex-energijski-ledger-hladenja` (provjera $P_h/P_{el}=\eta_p\eta_m\eta_f$) | ostvareno |
| 2. riješeni primjer — iterativna mreža | `ex-petlja-gradske-mreze` (čvorovi i oba puta A→C) | ostvareno |
| 3. kratko konceptualno pitanje | **Zastani i promisli** uz paralelne grane (vidljivo); „Provjeri sebe” (4 pitanja s odgovorima) postoji u izvoru, ali je skriven u webu i PDF-u (`SelfCheck`, `visibility: []`) | ostvareno jednim vidljivim pitanjem (ispravak nakon studentskog čitanja) |
| 4. samostalni zadatak bez zadane formule | Z4 (radna točka s Colebrookom), Z6 (energija i NPSH, T4) | ostvareno |
| 5. granica modela | „Kada jednodimenzijska bilanca nije dovoljna”, „Što $NPSH_a$ ne jamči” | ostvareno |
| 6. numerički pokus | `u10_moody_dijagram` (rezidual, Z4), `u13_paralelne_grane` | ostvareno |

Preduvjeti: $Re$ (pog. 11), Hagen–Poiseuille (pog. 12), sličnost za afinitetne zakone
(pog. 11) uvedeni su ranije; rotor crpke najavljen za pog. 14. Lajtmotivi: hlađenje (P2,
P5, Z3, CFD razdjelnika s izričitom vezom na dotok iz pog. 7), gradska mreža (P3), pomorstvo
(Z6 balastna crpka, uvod). Uvjet „što se zadržava, a što je novo” ispunjen je u CFD odlomku
`cfd-krug-radna-tocka`.

## Obrnuti nacrt (korak 3)

Uloge: temelj, izvod, tumačenje, primjena, granica, postupak, ponavljanje, dnevnik, bez poante.

| Redak | Poanta | Uloga |
| --- | --- | --- |
| 1 | gubitak $h_g$ određuje protok, visinu crpke i potrošnju; Bernoulli se proširuje | temelj |
| 3 | slijed $v\to Re\to\lambda\to h_g$, oblik $h_g$, $Q^2/D^5$ | **ponavljanje** (r. 93–109, 120–127, sažetak) |
| 5 | serija i paralela, $R_{eq}$ | **ponavljanje** (r. 225–240) |
| 7 | sadržaj poglavlja, primjene na brodu, 1D granica | primjena; granica ponovljena u r. 72 |
| 9 | čitanje uvodne slike mreže | tumačenje |
| 13 | radna točka kao presjecište | **ponavljanje** (r. 295–299) |
| 19–37 | KV, predznaci, ista referenca tlaka, $\alpha$ | izvod, temelj |
| 42 | EGL i HGL | tumačenje |
| 48–62 | disipacija $\Phi\ge0$ daje $h_g\ge0$ | izvod (Dublje) |
| 67 | tumačenje skice; zadnja rečenica („profil zadovoljava prianjanje…, koljeno … bez pregrade”) potvrđuje ispravnost crteža | tumačenje; zadnja rečenica **dnevnik** (provjera izrade skice) |
| 72 | granica 1D bilance | granica |
| 77–99 | Darcy–Weisbach, $\xi$ i referentna brzina, $\zeta$, izvori | temelj |
| 103–109 | promjer kao poluga, 32 i 16 puta | tumačenje |
| 113–115 | CFD razdjelnika daje $\xi$; „kao u ranijem Venturijevu primjeru” | primjena; upućivanje bez poglavlja (K12) |
| 120–127 | slijed kao formula | postupak (treći put) |
| 130–194 | izvod $\lambda$, laminarno, Colebrook, Swamee–Jain, Blasius, granice | izvod |
| 198–202 | pokus s Moodyjevim dijagramom | primjena |
| 214–216 | CFD: otpor ravnih vodova | primjena |
| 221–242 | otpor $R$, serija, paralela, granica analogije | temelj |
| 244–250 | Hardy–Cross | izvod |
| 255 | jednak pad u paralelnim granama | tumačenje (peti put: r. 5, 9, 265, sažetak) |
| 261–265 | pokus i **Zastani i promisli** | tumačenje |
| 276–278 | CFD i radna točka kruga | primjena |
| 283–301 | karakteristika sustava, radna točka, afinitet | temelj |
| 305–335 | lanac snaga, ventil | temelj |
| 339–362 | NPSH i granica | temelj, granica |
| 368–370 | CFD kavitacije | primjena |
| 375–672 | P1–P6 | postupak |
| 674–708 | Provjeri sebe | tumačenje |
| 714 | napomene uz skice | tumačenje |

Odlomci `ponavljanje` u uvodu (r. 3, 5, 13) zajedno imaju oko 200 riječi; dnevnička rečenica
r. 67 oko 20 riječi.

## Vlastiti nalazi glavnog agenta

| # | Mjesto | Težina | Nalaz | Status |
| --- | --- | --- | --- | --- |
| G1 | `u13:3`, `:5`, `:13` | P2 | Uvod iznosi formule ($h_g$, $Q^2/D^5$, $R_{eq}$, radna točka) koje odjeljci zatim izvode; jednak pad u paralelnim granama izrečen pet puta (K10). | provjereno |
| G2 | `u13:115` | P2 | „kao u ranijem Venturijevu primjeru” — nije rečeno u kojem poglavlju (K12). | provjereno |
| G3 | `u13:67` | P3 | Rečenica o prianjanju i koljenu bez pregrade provjera je izrade skice, ne tumačenje (K1). | provjereno |
| G4 | `ex-gubitci-jedne-dionice`, `u13:409–415` | P2 | $1000\cdot9{,}81\cdot3{,}82=37{,}47$ kPa, ispisano 37,4 (iz nezaokruženog $h_g=3{,}817$); provjera $37\,400/9810=3{,}81$ ne „vraća” ispisanih 3,82 m (K8). | provjereno računom |
| G5 | `ex-energijski-ledger-hladenja`, `u13:589` | P2 | Nakon čišćenja „uz isti protok” — ne kaže da pretvarač smanjuje brzinu vrtnje; CFD odlomak r. 278 upozorava da se pri istoj brzini mijenja protok. | provjereno |
| G6 | matrica, element 2 | P2 | Iterativni postupak (P3, Hardy–Cross) i radna točka (P4, zadana kvadratna karakteristika) riješeni su odvojeno; radna točka s $\lambda(Re)$ koji se mijenja s protokom, kako je glasi obvezna provjera ishoda, pojavljuje se tek u samostalnom Z4. Promjena primjera je autoričina odluka. | provjereno |
| G7 | dodatak F | P3 | Ključ pog. 13 nosi oznaku F.14 (F.1 je uvod), pa se brojevi odjeljaka ključa ne podudaraju s brojevima poglavlja. Izvan opsega poglavlja. | provjereno na PDF-u |
