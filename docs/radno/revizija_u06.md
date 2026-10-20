# Revizija U06 — 22. rujna 2026.

## Odluke prije provedbe

Opseg: zadatci za vježbu i svih sedam uključenih skica U06. Tekstovi
riješenih primjera i teorija služe usporedbi. Prethodna lokalna revizija U05
i korisnički QMD omotači čuvaju se. Kanonski verifier je `verify_u07`,
namespace `U07`; nazivi slika `u07_*` također pripadaju javnom U06.

| Primjeri | Princip, postupak i odluka | Odnos prema vježbama |
| --- | --- | --- |
| P1, ponton; P6, cilindrična osnova | Vertikalna ravnoteža, gaz i geometrijska rezerva | Z2 čuva osnovnu računsku tehniku T1 |
| P2, kompresor | GM iz geometrije i težišta, položaj tereta iz nagiba | Stari Z3 uglavnom ponavlja isti niz s obrnutim zadanim pomakom |
| P3, dva fluida | Podjela istisnine, ekvivalentni GM i moment | Z6 dodaje vrijednu procjenu intervala i odluku o koridoru |
| P4, puni izolirani tank | Dodana masa, pomak težišta, gaz i nagib | Novi Z5 uspoređuje dvije mjere uz dva uvjeta, bez bočnog opterećenja |
| P5, pumpno kućište | Uzgon i potrebna sila pridržavanja/podizanja | Z1 je koristan suprotni smjer pridržavanja |

| Mjesto | Odluka i korist | Razina | ID/status |
| --- | --- | --- | --- |
| Z1 | Zadržati; zatvoriti sile na istom tijelu u skici | T1 | Postojeći; nije potrebna zamjena |
| Z2 | Zadržati; razlikovati geometrijsku rezervu od dopuštenog tereta | T1 | Postojeći; ciljano preciziranje |
| Z3 | Zamijeniti pokusom nagibanja: izmjereni kut daje GM, zatim KG | T2 | `task-metacentarska-visina-iz-pokusa-nagibanja`; P3 |
| Z4 | Zadržati areometar; navesti gustoću referentne vode i točnu referencu urona vrata | T2 | Postojeći; preciziranje i rezultat |
| Z5 | Zamijeniti usporedbom spuštanja opreme i dodavanja balasta | T3 | `task-spustanje-opreme-ili-dodavanje-balasta`; P3 |
| Z6 | Zadržati intervalnu odluku; ukloniti neovisno fiksiranu masu koja proturječi nesigurnim uronima | T4 | Postojeći fizikalni problem; korekcija modela |

Novi Z3/Z5 autorske su nastavne konstrukcije (`rewrite_status=preradeno`,
`rewrite_level=P3`). Mijenjaju se scenarij, ulazi i izlazi (Z5 i maseni režim);
prag 3/5 je zadovoljen. Z5 više nije samo uvrštavanje u jednu zadanu formulu.
Z1/Z2/Z4/Z6 ne zahtijevaju rekonstrukciju radi kvote. Ostaje šest mjesta
T1,T1,T2,T2,T3,T4; obvezni ishod GM i granica maloga kuta dobiva izričitu provjeru.

Stari Z3 `task-u07-plutajuca-servisna-platforma-duljine-i-sirine-ima` i Z5
`task-u07-plutajuci-modul-istiskuje-volumen-vode-i-ima` ostaju HTML span aliasi.

## Skice i plan provjera

Sačuvati postojeće dvo-panelne prikaze primjera i raspored vježbi 3×2 s
donjom legendom, paletu, gradijente, šrafure i tipografiju. Prikazati zatvorenu
ovojnicu plovaka, vodu izvan nje, vodoravne slobodne površine, uronjene volumene
i centre uzgona unutar njih. Vektori sila nisu strelice strujanja. U ravnoteži
ukupna težina i uzgon moraju imati isti vertikalni pravac; prikaz komponenata
ne smije dvostruko ubrojiti njihovu rezultantu.

Nalazi prije popravka: uvodni B je izvan uronjenog tijela; P1 dijeli isti fluid
na nepovezane nijanse i nema silu u centru uzgona; P2 izgleda kao tanka ploča,
a ne tijelo zadane istisnine; P3 stavlja centar uzgona ispod tijela; P4 kombinira
uspravan trup s nagnutom morskom površinom; P5 kućište dodiruje dno bez reakcije
oslonca. Z3 ima krivi smjer nagiba prema pomaknutom teretu, Z4 su uroni kotirani
od dna umjesto referencije vrata, Z5 ne prikazuje ispravan odnos B/G/M.

Plan: neovisne bilance, granični slučajevi i intervalni omotač; koordinate
stvarnih SVG-ova i vizualni pregled; D03 te generatorski D06/manifest;
povezani notebook; HTML i PDF, tipkovnica, poveznice i raspodjela razina.

## Rezultat i provjere nakon provedbe

Z3 sada iz izmjerenog nagiba određuje GM i KG; Z5 uspoređuje spuštanje opreme
i dodavanje čvrstoga balasta uz istodobne uvjete za GM i slobodni bok.
Z1 je zadržan, Z2 ima preciziranu geometrijsku granicu, Z4 referentnu gustoću
i datum mjerenja vrata areometra. Z6 za svaki skup nesigurnih ulaza zatvara
i istisninu i masu prije momentne bilance. Stari Z3/Z5 ID-jevi ostali su aliasi.
Tekst prije odjeljka vježbi uspoređen je s početnom kopijom: teorija i P1–P6
nisu mijenjani. Hash usporedba potvrđuje očuvanje prethodnih izmjena U05 i svih
korisničkih QMD omotača. Ažurirani su D03, generatorski D06 i manifest.

Za Z6 provjera kutova intervala daje nominalno e = 0,32091 m i maksimum
0,35463384 m pri hL = 0,263 m, hD = 0,177 m, gustoći vode 1001 kg/m³,
masi akumulatora 69 kg i KG = 0,195 m. Maksimum prelazi koridor 0,34 m.
Kutne kombinacije daju i ispravnu geometriju te kut manji od 5°.

Provjera da unutrašnjost intervala ne skriva veći maksimum: uz h = (hL+hD)/2,
d = hL−hD i N = mΔ GM vrijedi e = Nd/(B ma), gdje je

```text
N = LB [rho_o delta (h − delta/2 − KG)
        + rho_w ((h − delta)^2/2 − KG(h − delta) + B^2/12)].
```

Na cijelom zadanom intervalu N > 328 kg m i |dN/dh| < 47 kg, uz d ≤ 0,086 m.
Stoga su derivacije prema hL pozitivne, a prema hD negativne. Derivacija
prema gustoći vode pozitivna je jer izraz u njezinoj zagradi prelazi 0,100 m²;
derivacije prema KG i ma negativne su. Maksimum je zato upravo u navedenom
kutu, a ne samo najveći među nasumično uzorkovanim točkama.

Svih sedam SVG skica pregledano je u pregledniku; popravljene su ovojnice,
vodoravne površine, centri uzgona, smjerovi sila i kote. Zasebna skripta
`check_u06_sketch_geometry.py` neovisno integrira stvarne poligone po
vodoravnim trakama: provjerava deset trupova/centara uzgona, geometriju
zatvorenog punog tanka, šest panela vježbi i odmak kućišta od dna.
SVG tekstovi ostaju unutar svojih okvira. Crteži zadržavaju izvornu paletu,
raspored panela i dimenzije; veličine strelica sila nisu u mjerilu.

Izvršene provjere:

- `verify_u07`: 97/97 provjera; cijeli `verify_all`: 1128 rezultata
  (994 brojčane usporedbe i 134 invarijante), uz 22 zasebne fizikalne provjere.
- Audit publikacije: 87 riješenih primjera, 90 vježbi, u U06 šest vježbi
  T1,T1,T2,T2,T3,T4; svih 90 ugovora u manifestu pokriveno.
- Generatori D06/manifesta i normalizacija teksta aktualni; Typst audit i
  `git diff --check` prolaze.
- Povezani `u07_gaz_plivajuceg_tijela.ipynb` pregledan i izvršen u čistom
  kernelu; ostaje zaseban parametarski pokus vertikalne ravnoteže.
- Puni HTML render; pregled U06 na 320, 768 i 1440 px bez vodoravnog
  prelijevanja, 12 sklopivih naputaka/odgovora upravljivih tipkovnicom,
  oba stara aliasa te šest D06 povratnih poveznica rade.
- Puni PDF render: 309 A4 stranica; audit PDF-a prolazi. Vizualno pregledane
  stranice primjera, vježbi 120–122 i ključa 296; rezultati nisu odrezani.
- Audit izgrađene stranice: 24 HTML stranice, 212 slika, 1918 poveznica i
  434 sklopiva bloka; aktualni PDF kopiran je u `_site/downloads/`.

Didaktička raznolikost ostaje autorska procjena, odvojena od prolaza testova.
Rotirana geometrija skica prikazuje krut trup; račun GM i rubnih gazova ostaje
početni model s razlikama višeg reda u kutu, a ne provjera konačne stabilnosti.
Lokalni Quarto je 1.9.32 (CI koristi 1.9.37); postojeća upozorenja Typsta o
`times.circle` u U10 nisu povezana s ovom izmjenom. Puni JupyterLite build
i udaljeni GitHub Actions nisu pokretani. Izmjene nisu commitane ni pushane.

## Revizija 12. 10. 2026.

Provedba nalaza stručne recenzije (brodska hidrostatika), odobrene od autorice.
Zadatci Z1–Z6 nisu mijenjani sadržajno (samo oznake $T$, $\Delta$, nadvođe i po
jedna rečenica konteksta u Z3/Z5); razine ostaju T1, T1, T2, T2, T3, T4. Broj
primjera ostaje 6; P5 (pumpno kućište) premješten je odmah iza izvoda uzgona i
sada je P1, a ID `ex-u07-uzgon-na-potonulo-pumpno-kuciste-pri-ispitivanju` ostaje.

| Nalaz recenzije | Provedeno | Mjesto |
| --- | --- | --- |
| Kut uronjenja ruba palube računan sa $\sin$ (37,1°) | Ispravljen uvjet $F_b\cos\theta=(B/2)\sin\theta$, $\tan\theta_{lim}=2F_b/B$, 31,1°; verifikator `atan` + invarijanta | P4 (CH2), `verify_u07.py` |
| Spar fizikalno neuvjerljiv (gaz 17 m, 78 m iznad vode) | Novi podatci $D=12$ m, $H=100$ m, $m=9000$ t: $T=77{,}6$ m, $f=22{,}4$ m, $KB=38{,}8$ m, $BM=0{,}116$ m, $KM=38{,}9$ m; uvjet $KG<KM$, primjeri $GM$ s balastom i bez njega; T3 opravdan izborom modela (njihalo, ne vodna linija) | P6 `ex-u07-plutajuci-vjetroagregat-tipa-cilindricne-plovne-osnove-t3` |
| Dvofluidni $BM_{eq}$ bez izvoda | Dopisan izvod s dvama klinovima ($\rho_oI_T\theta+(\rho_w-\rho_o)I_T\theta$) i granicama $\rho_o\to\rho_w$, $\rho_o\to0$ | izvod BM, `#eq-metacentarski-radijus-dva-fluida` |
| Granica malog kuta samo deklarativna; P2 6,84° vs 5° u Z3/Z6 | Blok „Granica modela” s wall-sided polugom $GZ=(GM+\tfrac12BM\tan^2\theta)\sin\theta$; u P2 korekcija 0,9 %, u P3 0,4 %; obrazložena granica 5° | `#eq-poluga-okomiti-bokovi`, P2, P3 |
| „Neovisna provjera” $y_B=BM\tan\theta$ tautološka | Preimenovano u konzistentnost; neovisna kontrola wall-sided izrazom | P2, P3 |
| Dupli izvod, redoslijed GM prije BM, orphan odlomci | Uklonjen callout „Postupak rješenja”; momentna ravnoteža $m_ke=\Delta GM\tan\theta$ izvedena iz povratnog momenta unutar izvoda BM (ID jednadžbe zadržan); uklonjeni odlomci o nepostojećem međukoraku; r. 80 obrazloženje za proizvoljan oblik; r. 450 „plutajuće tijelo” | teorija |
| Slobodna površina bez formule | Blok „Dublje”: $\delta GM=-\rho_ti_t/(\rho V_{ist})$, tank iz P4 napola pun: $-0{,}065$ m | `#eq-ucinak-slobodne-povrsine` |
| Nazivlje i notacija | nadvođe, poluga stabiliteta, poprečni nagib, kut nestajanja stabiliteta, centar uzgona, stabilitet, metoda dodane težine (P4), pridružena masa (CFD); $V_{ist}$, $T$ ($T_m$, $T_L$, $T_D$, $T_0$), $\Delta$ masa istisnine, $BM$/$GM$ bez nadvlake; drugo pitanje samoprovjere zamijenjeno (jednak $GM$, različit $BM$) | cijelo poglavlje; oznake $T_L$/$T_D$/$T$ i u skicama |

Matrica zamjena: nema zamijenjenih zadataka (Z1–Z6 ID-jevi i kontrolni rezultati
nepromijenjeni; Z6 $\Delta=689{,}9$ kg i dalje odgovara `verify_physics`).
Promijenjeni primjer P6 (spar) zadržava ID; novi kontrolni rezultati navedeni su
u tablici.

Provjere: `verify_u07.py` 112/112 (nove provjere: `U07.CH2.theta_lim_deg` 31,1°,
geometrija ruba palube, slobodna površina, spar KB/BM/KM/GM, wall-sided korekcije
i invarijanta granice malog kuta). `check_u06_sketch_geometry.py` PASS (bez
geometrijskih izmjena; promijenjene su samo tekstne oznake gaza u
`u07_ch1_platforma_ulje_voda_ormar.svg`, `u07_val1_platforma_kompresor.svg`,
`u07_val2_ponton_gaz.svg` i `u07_vjezbe_skice.svg`). Skica za spar nije dodana
(zahtijevala bi novu SVG datoteku). Drugi numerički pokus ($GZ$ wall-sided) nije
izrađen jer traži novu bilježnicu i CI. `audit_publication` javlja da redoslijed
primjera P1–P6 treba obnoviti generatorom indeksa (koordinator). Didaktička
procjena ostaje autorska.

## Revizija 19. 10. 2026. — didaktičko pojačanje (odobreno u razgovoru)

Zahtjev autorice: zadatci su prelagani i prečesto ponavljaju riješene primjere; kroz poglavlja uvesti po koji zahtjevniji zadatak ili zakomplicirati primjer, ne dodavati tekst. Zahvat unutar šest mjesta Z1–Z6 i raspodjele T1, T1, T2, T2, T3, T4; broj primjera ostaje. Stari ID-jevi zamijenjenih zadataka ostaju kao prazni `<span>` aliasi.

| Mjesto | Staro | Novo | Razina | Didaktička korist |
| --- | --- | --- | --- | --- |
| Z1 | Klon P1 | Promjena gaza broda između mora i rijeke (`task-promjena-gaza-broda-more-rijeka`): $V=11\,707$ / $12\,024$ m³, $\Delta T=0{,}132$ m, iskrcaj 316 t, 24,6 / 24,0 t/cm | T1 | Brodograđevna primjena istisnine; jedinice t/cm i prijelaz slatka–slana voda. |
| Z2 | Klon P2 | Plutanje homogenog drvenog bloka (`task-plutanje-homogenog-bloka-stabilitet`): $T=0{,}326$ m, $GM=+0{,}038$ m, uvjet $b/h\ge\sqrt{6s(1-s)}$, $b_{min}=0{,}584$ m; gušći blok stabilniji | T2 | Izvod uvjeta stabilnosti po omjeru stranica i protuintuitivan zaključak o gustoći. Puni ključ u D06. |
| Z4 | Areometar | Nepromijenjen, razina T1 | T1 | Raspodjela. |

Skica: Z1 presjek broda s dvije vodne linije, Z2 blok s G (B nije nacrtan); `check_u06_sketch_geometry.py` usklađen; invarijante `U07.INV.*` preimenovane. D03 §6 dopunjen.

Prošlo nakon zahvata: pripadni `verify_*`, `verify_all`, `audit_publication`, `qa_audit`, `audit_sketch_design` (s `check_u*_sketch_geometry`), `audit_print_layouts`; D06 i manifest regenerirani generatorima, `print-layouts.json` hash obnovljen. Vizualna provjera skice obavljena headless renderom u PNG. Didaktička procjena je autorska; studentski pilot nije proveden.
