# Provedba tekstnih ispravaka G2 (pog. 5–8)

Provedba 8. 11. 2026. prema `PROVJERA.md`. Provedene su samo stavke sa statusom POTVRĐENO,
težinom P2 i vrstom TEKST, a kod mješovitih samo tekstni dio bez promjene broja, rezultata ili
oznake koju koriste ključ i verifikator. Izmijenjeni su samo `source/u05_…`, `u06_…`, `u07_…`
i `u08_…`. Generatori nisu pokretani s `--write`, a commit nije napravljen.

## Tablica

| ID | Mjesto | Status | Napomena |
| --- | --- | --- | --- |
| G2-01 | `u06` Dublje, slobodna površina | PRESKOČENO | BROJ/MODEL; blok već sadrži nadoknadu mase i upozorenje da stvarni $GM$ može porasti. |
| G2-02 | `u05` sažetak, izvod nagnute plohe | PROVEDENO | Oba mjesta kažu da sila ne ovisi o nagibu i da plohe jednake $A$ i $h_C$ nose jednaku silu; sažetak dodaje da centar tlaka ovisi o nagibu. |
| G2-03 | `u05` P2 i P6 | PROVEDENO | U oba teksta zadatka dodano je „gustoće $\rho=998\ \mathrm{kg/m^3}$”. |
| G2-04 | `u05` Z1 | PROVEDENO | Dodana je rečenica o vodoravnim trakama oslonjenima na šarke i zasune; razina T1 ostaje autorskoj odluci. |
| G2-05 | pog. 5, kontekst primjera | PRESKOČENO | AUTORSKA ODLUKA. |
| G2-06 | `u05` uvod i odjeljak „Hidrostatičke sile na plohe” | PROVEDENO (djelomično) | Uklonjene su ponovljene rečenice o ravnoj i zakrivljenoj plohi u odjeljku; uvod s formulama i izrazi $I_G$ ostaju prema odluci od 15. 10. 2026. |
| G2-07 | `u05` CFD ustava, P5 | PROVEDENO | „Prethodno poglavlje” zamijenjeno je chapter-ref `u04`, a „odjeljak o referentnom tlaku” upućivanjem na jednadžbu `eq-sile-plohe-referentni-tlak-i-smjer-sile-02`. |
| G2-08 | `u05` CFD, Z6; `u07` Z2, Z5; `u08` CFD Venturi | PROVEDENO | Glas je ujednačen: „usporedimo”, „označuje se”, „orijentiraš”, „zanemari”, „Ako se klip zaustavi”, „Provjeravamo … odvajamo”. |
| G2-09 | `u06` P1 | PROVEDENO | Kućište je u tekstu zadatka hermetično zatvoreno slijepim prirubnicama; u naslovu „potonulo” je zamijenjeno s „uronjeno”, ID ostaje. |
| G2-10 | `u06` r. 19; `u07` r. 245; `u08` r. 148 | PROVEDENO | Dvostruke numerirane jednadžbe zamijenjene su upućivanjem; uklonjeni ID-jevi (`…fizikalni-uvod-i-matematicki-izvod-01` u pog. 6, `…bilanca-mase-u-kontrolnom-volu-05`, `…razrada-koraka-07`) nemaju poveznica u `source/`. |
| G2-11 | `u06` uvod, r. 115 | PROVEDENO | Iz uvoda je uklonjena rečenica o poništavanju atmosferskog tlaka, a r. 115 upućuje na jednadžbu $GM$ umjesto trećeg nabrajanja uvjeta. |
| G2-12 | `u06` r. 28, 266, 279; `u07` r. 53, 313, 666; `u08` r. 230 | PROVEDENO | Naslov-pretinac i labela Granice modela su izjavni, a pet vodećih redaka CFD blokova izjavno je oblikovano; ID-jevi ostaju. |
| G2-13 | `u06` r. 113, 234, 324; `u07` r. 9; `u08` r. 220, 225 | PROVEDENO | Duge rečenice su podijeljene; dva klina i šest kriterija IS Codea sada su natuknice s nepromijenjenim brojevima. |
| G2-14 | `u06` Granica modela i izvod „Krivulja stabiliteta” | PROVEDENO | `eq-poluga-okomiti-bokovi` s brojevima za platformu premješten je u izvod, a u Granici su ostale tri rečenice s mjerom $\tfrac12(BM/GM)\tan^2\varphi$. |
| G2-15 | `u06` P4, P5 (T4) | PRESKOČENO | AUTORSKA ODLUKA. |
| G2-16 | Z6 pog. 6, 7, 8 | PRESKOČENO | AUTORSKA ODLUKA. |
| G2-17 | `u06` P6 (spar) | PROVEDENO | Uvedeni su čvrsti i vodeni balast (−5 % sada je „ispuštanje vodenog balasta”) i „(engl. *spar*)”; usporedba je „isti balast smješten više” uz $KG=45$ m, a gaz ima oznaku „nastavna procjena”. |
| G2-18 | `u06` Z2 | PROVEDENO | $s\to s_r$ u tekstu, naputku i kontrolnom rezultatu te „uvjet stabiliteta”; `d06` treba obnoviti generatorom. |
| G2-19 | `u06` r. 176, 782 | PROVEDENO | Opisna su upućivanja zamijenjena s `[-@eq-poluga-okomiti-bokovi]` i `[-@eq-ucinak-slobodne-povrsine]`. |
| G2-20 | `u07` r. 66 | PROVEDENO | Nestacionarnost je odvojena od akumulacije, uz rečenicu da u krutoj cijevi s nestlačivom tekućinom akumulacije nema. |
| G2-21 | `u07` P2, P4, P5 | PRESKOČENO | AUTORSKA ODLUKA. |
| G2-22 | `u07` r. 211, 444 | PROVEDENO | Upućivanje sada glasi „pokretnu lopaticu i mlaz u pog. 10 te radno kolo u pog. 14” (chapter-ref `u10`, `u14`). |
| G2-23 | `u07` P3 / `u08` P4 | PRESKOČENO | AUTORSKA ODLUKA i SKICA. |
| G2-24 | `u07` Z1 | PRESKOČENO | BROJ/MODEL. |
| G2-25 | `u07` uvod | PROVEDENO | Uvod završava s „… poseban slučaj te bilance, odnosno jednadžbe kontinuiteta”, a uvjeti ostaju u Granici modela i sažetku. |
| G2-26 | `u07` r. 162, 323, 547 | PROVEDENO | Ručni „P3” zamijenjen je s `[-@ex-zahvatni-usis-morske-vode-u-plovidbi]`, „sljedeće poglavlje” s chapter-ref `u08`, a „Sljedeća skica” sa `[-@fig-u08-staticka-zamjena-za-kontrolni-volumen-i-kontinuitet]`. |
| G2-27 | `u07` r. 313; `u06` r. 324 | PROVEDENO | Uklonjena je kratica FVM, a „IMO-ova” je zamijenjeno s „Međunarodne pomorske organizacije”. |
| G2-28 | `u08` r. 1, Fizikalno značenje uz HGL | PROVEDENO | Dodano je „vodoravne” i rečenica „U silaznom suženju tlak može i rasti (Z3): pada HGL, ne nužno tlak.” |
| G2-29 | `u08` izvod energijske jednadžbe | PROVEDENO | Ispred definicija visina umetnut je redak $\dot W_s=\dot W_{turbina}-\dot W_{crpka}$ (oba iznosa pozitivna), bez novog broja jednadžbe. |
| G2-30 | `u08` odjeljak „Kada se trenje može zanemariti” | PROVEDENO | Naslov je „Energijska jednadžba s gubitcima i strojevima”, a dodana je jedna rečenica s kriterijem ($h_g$ prema promjeni brzinske visine). |
| G2-31 | `u08` interaktivni prikaz Venturija | PRESKOČENO | AUTORSKA ODLUKA. |
| G2-32 | `u08` Granica modela, sažetak | PROVEDENO | Tekst sada kaže da srednji apsolutni tlak iznad tlaka pare ne isključuje kavitaciju jer lokalni minimum može biti niži. |
| G2-33 | `u08` r. 3, 7, 58 | PROVEDENO | U r. 3 HGL i EGL su samo imenovane, iz r. 7 je uklonjena rečenica doslovno ponovljena u Granici modela, a r. 58 počinje odnosom EGL i HGL. |
| G2-34 | `u08` P4 | PROVEDENO | U tekst zadatka dodana je samousisna izvedba ili sustav za zalijevanje, uz napomenu da smještaj pokazuje granicu usisa. |
| G2-35 | `u08` P5 | PROVEDENO | U provjeri je jedna rečenica o provjeri $Re$ i koeficijenta istjecanja za viskozno ulje; fluid i brojevi ostaju. |
| G2-36 | `u08` P6, $R$ i $T$ | PRESKOČENO | ODBAČENO kao P2. |
| G2-37 | `u08` P6 | PROVEDENO | Tekst sada glasi „Granice $Re\approx2300$ i $4000$ … u kružnoj cijevi (pog. 11)”. |
| G2-38 | `u07` P1; `u08` $\alpha$; `u06` slobodna površina, spar | PROVEDENO | Dodane su oznake „kao orijentacija” ili „nastavna procjena”; za 1,6–3,6 m/s dodano je „a ne preporuka za usis crpke”, a tvrdnja o tankovima postala je posljedica modela. |
| G2-39 | sl. 5.8, 8.5, 8.7 | PRESKOČENO | SKICA. |
| G2-40 | `u07` r. 53 | PRESKOČENO | ODBAČENO kao P2. |
| G2-41 | `u05` r. 15 | PRESKOČENO | ODBAČENO kao P2. |
| G2-42 | podtvrdnje primjenskog recenzenta | PRESKOČENO | NEPOTVRDIVO; ni u G2-38 nije unesen nijedan raspon iz tih tvrdnji. |

Zbroj: 29 PROVEDENO (G2-06 djelomično), 13 PRESKOČENO, 0 NEPRIMJENJIVO, 0 PREPUŠTENO G4.
Nijedna stavka u ovom opsegu ne traži izmjenu dodataka; jedina posljedica za dodatke jest
ključ `d06`, koji se obnavlja generatorom.

## `prirucnik_stats.py --usporedi HEAD` (sažeto)

| Izvor | Brojevi izgubljeni | Brojevi dodani | ID-jevi izgubljeni | Tumačenje |
| --- | --- | --- | --- | --- |
| u05 | — | 3, 3, 998, 998 | — | 998 iz G2-03; „3” iz $\mathrm{m^3}$. |
| u06 | 0, 0, 0 | 13, 2 | `eq-uzgon-stabilitet-fizikalni-uvod-i-matematicki-izvod-01` | 0, 0, 0: uvjeti $GM>0$, $=0$, $<0$ uklonjeni iz r. 115 (G2-11), a ostaju u uvodu i u izvodu r. 262. 13: razlika $45-32$ m u G2-17. 2: indeks u natuknicama. Kriteriji IS Codea i brojevi spara prijavljeni su kao uklonjeni, ali stoje nepromijenjeni u natuknicama i novim rečenicama. |
| u07 | — | — | `eq-kinematika-kv-matematicki-izvod-bilanca-mase-u-kontrolnom-volu-05` | Broj istaknutih formula pada s 57 na 56 (G2-10). |
| u08 | 2, 2300 | — | `eq-energijska-bilanca-razrada-koraka-07` | 2: formule HGL i EGL uklonjene iz uvoda; ostaju u jednadžbama r. 44–54 (G2-33). 2300 ostaje u tekstu kao $Re\approx2300$, a alat ga ne broji zbog `\approx`. Broj istaknutih formula pada s 54 na 53. |

Prijavljene promjene nijekanja i ograda su namjerne: „samo” u G2-02 i G2-32, rečenica iz
uvoda pog. 6 i pog. 8 koja se doslovno ponavlja (G2-11, G2-33), „može” u preimenovanim naslovima
(G2-12, G2-30) i „nije” u razdijeljenoj rečenici G2-20, koja stoji u novoj rečenici.

`--nalazi` za četiri izvora daje još dva nalaza u pog. 7. Oba su P3 izvan ovog opsega: K3 u r. 690
(skriveni „Provjeri sebe”) i K12 u r. 376 („Sljedeći primjer”).

## Napomene za integraciju

- `tools/audit_architecture.py` javlja „Generated book files are stale: source/d06_…”. Ključ
  treba obnoviti s `python scripts/build_book.py --write`. Na to utječu G2-18 i promijenjeni
  tekstovi zadataka (`u05` Z1, Z6; `u06` Z2; `u07` Z2, Z5). Obnoviti treba i manifest
  zadataka i `assets/content-index.json` (uklonjeni ID-jevi jednadžbi i premještena
  `eq-poluga-okomiti-bokovi`).
- Naslov `## Matematički izvod` u pog. 6 nije imao izričiti ID. Novi naslov mijenja automatsko
  sidro; u `source/`, `content/`, `components/`, `tools/` i `scripts/` nema poveznice na staro sidro.
- Završetci redaka su kao prije izmjena: u05 LF, a u06–u08 CRLF u radnoj kopiji.
- Ovo je autorska procjena provedbe. Pokrenuti su samo `prirucnik_stats.py --usporedi` i
  `--nalazi` te `audit_architecture.py` (pao zbog zastarjelog `d06`). Render, verifikatori
  i objavni CI nisu pokrenuti, pa didaktička kvaliteta ni prikaz nisu dokazani.
