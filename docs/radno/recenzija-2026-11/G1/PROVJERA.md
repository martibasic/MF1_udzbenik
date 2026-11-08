# Provjera nalaza — skupina G1 (pog. 1–4)

Provjeru je 8. 11. 2026. proveo neovisni agent prema koraku 5 skilla
`recenzija-prirucnika`. Ulaz su četiri izvještaja iz ove mape: struka (S),
primjena (A), urednik (U) i studentsko čitanje pog. 3 (St). Svako je mjesto
otvoreno u `source/` (grana `konvencije-recenzije`), a brojčani i fizikalni
nalazi preračunani su u
`C:/Users/mandr/AppData/Local/Temp/claude/60109e3fc54e5b4d/04a739be-433a-464c-925a-63c7f06751f8/scratchpad/knjiga/prov_G1/`
(`provjera_g1.py`, `temp_mu.py`, `z6_opcije.py`, `recenice.py`). Prikaz u PDF-u
provjeren je tekstnim izvlačenjem iz `pog01.pdf` i `kljuc03.pdf`.

Nalazi koji su već obrađeni na razini knjige su preskočeni: ključ s „odgovarajućim
izrazom”, „primjer N.M”, skriveni „Provjeri sebe”, F.(N+1) i nazivi bilježnica.

**Ukupno 45 stavki P0–P2** nakon spajanja (raw: S 10, A 9, U 31, St 4).

| Težina | POTVRĐENO | ODBAČENO | NEPOTVRDIVO |
| --- | ---: | ---: | ---: |
| P0 | 0 | 0 | 0 |
| P1 | 1 | 0 | 0 |
| P2 | 37 | 0 | 2 |
| P3 (sniženo iz P2) | 4 | 0 | 1 |

Djelomično odbačeni dijelovi navedeni su u stupcu „Status” uz pojedinu stavku.

## Tablica nalaza

Oznake izvora: S-P1-1 znači stručni izvještaj, nalaz P1-1. Kod uredničkih
nalaza (U) navedeno je pravilo iz pripadnog retka tablice.

| ID | Mjesto | Nalaz | Izvor | Težina | Status | Vrsta ispravka | Prijedlog ispravka |
| --- | --- | --- | --- | --- | --- | --- | --- |
| G1-01 | `u04:683` (Z2 `task-spremnik-na-dizalici-dva-ubrzanja`); `u04:853`; skica `fig-u04-vjezbe`; ključ | Spremnik slobodno visi o kuki dizalice. Pri stalnom ubrzanju u ustaljenom stanju uže i spremnik zakreću se u smjer $\vec g_{eff}$, pa je površina usporedna s dnom. Razlika razina uz stijenke tada je 0, a ne 0,272 m. Tlak na dnu je 8,89 kPa umjesto 10,31 kPa (račun niže). | S-P1-1; A-P3-7 (njihanje) | **P1** | POTVRĐENO | AUTORSKA ODLUKA + SKICA (brojevi mogu ostati) | Spremnik kruto pričvrstiti na nosač koji krute vodilice drže vodoravnim, a skicu i napomenu uz skice uskladiti s tim; inače preokrenuti pitanje, tako da student pokaže otklon za $\theta$. |
| G1-02 | `u01:183`, `u01:7` | Izvod kaže da je prijenos neumanjen jer se zanemaruje $\rho g\Delta z$. *Promjena* tlaka u nestlačivom mirujućem fluidu ista je točno, za bilo koji $\Delta z$ (račun: 250 000 Pa na oba klipa). Zanemarenje treba samo za apsolutnu ravnotežu sila. „Praktički isti” u r. 7 sugerira da je zakon približan. | S-P2-1 | P2 | POTVRĐENO | TEKST | Napisati da se $\rho g\Delta z$ pri opterećenju ne mijenja, pa je $\Delta p$ isti točno; član zanemariti samo u ravnoteži sila na klipovima na različitim visinama; iz r. 7 ukloniti „praktički”. |
| G1-03 | `u02:68` | „Za nenewtonski fluid … gradijent brzine ne mora biti [stalan]” u Couetteovu sloju. Za $\tau=f(\dot\gamma)$ s monotonim $f$ stalan $\tau$ daje stalan $\dot\gamma$. Tvrdnja proturječi i Z5 (`u02:794`: „profil je linearan”). | S-P2-2 | P2 | POTVRĐENO | TEKST | „…gradijent je stalan ako naprezanje ovisi samo o lokalnom gradijentu; newtonski je model tvrdnja da je njihov omjer isti pri svim brzinama.” |
| G1-04 | `u03:339` prema `u03:521` | Ulaž se u P3 mjeri od referentne točke na palubi, a u P5 od vrha tanka (K6). Sondna cijev u P5 izlazi na palubu, kojoj visina nije zadana. | S-P2-3; A-P2-5 (dio); St-P2-4 | P2 | POTVRĐENO | TEKST | U P5 pisati „visina praznog prostora iznad balasta, $H_{tk}-h_s$” umjesto „ulaž”. |
| G1-05 | `u04:223` | „Kapilarna duljina iz pog. 2”: u pog. 2 je nema. $L_c$ je definirana tek u `u11:99` i `d01:140` (K5, K12). | S-P2-4; U (P1) | P2 | POTVRĐENO (težina snižena s P1) | TEKST | Uputiti na pog. 11 i dodatak A, ili u pog. 2 uz kapilarni uspon dodati rečenicu $L_c=\sqrt{\sigma/(\Delta\rho g)}\approx2{,}7$ mm za vodu. P1 snižen jer je pojam u knjizi definiran i ne ulazi u račun; pogrešno je samo upućivanje. |
| G1-06 | `u01:663` (Z2 `task-kormilarski-stroj-dva-cilindra`, Traži se 2) | Moment nije vezan uz položaj kormila. Uz hod 0,30 m i $r=0{,}60$ m otklon je 26,6°. Kod Rapsonova klizača $M=2Fr/\cos^2\delta$ = 110,4 kN m, a ne 88,4 kN m (+25 %). | S-P2-5 | P2 | POTVRĐENO | TEKST | „Odredi ukupni moment u srednjem položaju kormila.” Ključ i verifikator ostaju. |
| G1-07 | `u02:827` prema `u02:435`; `u04:817` prema `u04:417`; `u04:651` prema `u04:498`; `u01:779` prema `u01:366` | Samostalni zadatci ponavljaju zakon i postupak riješenih primjera: dva stanja kapilare i kapljice; $\omega_{max}$, $h_C$, $h_R$; $\Delta h$ i prelijevanje; platforma s više cilindara. T4-zadatci dodaju odluku, a Z1 pog. 4 ne dodaje ništa. | S-P2-6 | P2 | POTVRĐENO | AUTORSKA ODLUKA | U ciklusu revizije Z1–Z6, jedno poglavlje po jedno, najprije zamijeniti u04 Z1 obrnutim pitanjem (npr. ubrzanje iz izmjerenog $\Delta h$); P1–P6 ne dirati bez proširenja opsega. |
| G1-08 | `u01:140–160`, `u02:346`, `u03:200`, `u04:223` | Blokovi „Granica modela” imaju 4–8 rečenica (K11: 1–3). U pog. 1 blok uvodi modul $K$ i numeriranu jednadžbu `eq-modul-stlacivosti-volumna-promjena`, dakle novu teoriju. Jednadžba nema brojčanih upućivanja. U `u02:346` niz od četiri pretpostavke odvojen je točkom-zarezom (K3). | S-P2-7; U (u02:346, K3); U-P3-10 | P2 | POTVRĐENO | TEKST | Teoriju modula $K$ premjestiti u kratak odjeljak ili blok „Dublje” ispred primjera, a granice skratiti na tri izjavne rečenice; u pog. 2 pretpostavke dati kao popis. |
| G1-09 | `u01:141`, `u03:206`, `u04:179` | Naslovi bloka postavljeni kao pitanje: „Kada stlačivost utječe…?”, „Što znači nizak tlak na usisu?”, „Zašto Coriolisova sila nestaje…” (K4). | U (K4, tri retka) | P2 | POTVRĐENO | TEKST | „Utjecaj stlačivosti na pomak klipa”, „Nizak tlak na usisu i referenca tlaka”, „Coriolisova sila u relativnom mirovanju”. |
| G1-10 | `u03:243`, `u03:249`, `u03:442`, `u03:448`; ključ `u04:811` (Z5), `u04:843` (Z6) | Međurezultati sa 6–9 značajnih znamenaka (132506,532 Pa; −20483,28 Pa). Kontrolni rezultati: 0,45291 m; 72,91 mm; 1,095 mm uz kriterij 5 mm; 0,35268 m; 2,68 mm (K8). | S-P2-8; U (K8); U-P3-9 | P2 | POTVRĐENO | TEKST (u03) / BROJ/MODEL (ključ u04; D06 obnoviti generatorom, provjeriti tolerancije manifesta) | Međurezultate pisati na 4 značajne znamenke; Z5: 0,453 m, 73 mm, 1,1 mm; Z6: (0,353; 0,567) m, rezerva oko 3 mm. |
| G1-11 | `u04:3`, `u04:9`; sl. 4.1 (`u04_fig_uvod_pregled.svg`, oznaka „L”) | Za brod u zavoju uvod i slika rabe „duljinu $L$” i uvjet „duljina ≪ $R_z$”. Mjerodavna je poprečna mjera, a primjer (`u04:359`) ispravno rabi $b_t$ (K6). | S-P2-9 | P2 | POTVRĐENO | TEKST + SKICA | U uvodu i na lijevom panelu sl. 4.1 pisati širinu tanka $b_t$ (mjera prema središtu zavoja). |
| G1-12 | `u02:492` (`ex-u02-hladni-start-i-radna-temperatura-koliko-kosta`) | $\mu=0{,}40$ Pa s pri 0 °C i 0,040 Pa s pri 90 °C ne odgovaraju jednom mineralnom ulju. Walther za VG 100 daje 1,62 i 0,0121 Pa s (omjer 134); za VG 32 omjer je 53. Primjer time umanjuje temperaturnu ovisnost koju poglavlje naglašava (`u02:3`). | A-P2-1 (1) | P2 | POTVRĐENO (vlastiti račun, ASTM D341) | BROJ/MODEL (samo temperature; rezultati ostaju) | Zadržati $\mu_1$, $\mu_2$ i sve rezultate, a temperature promijeniti u oko 10 °C i 50 °C (VG 68 daje 9,7 °C i 48 °C); u Provjeri dodati da je omjer između 0 °C i 90 °C reda 100. |
| G1-13 | `u02:492`, `u02:577` | Za ležaj statvene cijevi $L/D=1{,}4$ je prekratak (pravila klasifikacijskih društava). Malo plovilo s vratilom od 50 mm ima vodom podmazan gumeni ležaj. Puna brzina vrtnje nije uobičajena odmah nakon hladnog isplovljenja. | A-P2-1 (2–4) | P2 | NEPOTVRDIVO (pravila i praksa „po sjećanju”, bez izvora u dodatku E) | AUTORSKA ODLUKA | Provjeriti u pravilima klasifikacijskog društva; ako se potvrdi, primjer nazvati „uljem podmazani klizni ležaj” bez „statvene cijevi” ili prilagoditi geometriju. |
| G1-14 | `u04:389`, `u04:400`, `u04:413` (`ex-tank-broda-u-kruznom-zavoju`) | „Razlika očitanja mjera je ubrzanja” i „u ustaljenom zavoju tank se ne prelijeva” vrijede samo uz pretpostavku „bez nagiba”. Brod se u ustaljenom zavoju nagne prema van i taj nagib zbraja se s 1,24°. Uz $KG-T/2=3$–5 m i $GM=1$–2 m: $\varphi=1{,}9$–6,2°, $\Delta h=0{,}49$–1,17 m prema $\Delta h_{max}=1{,}20$ m (K9). | A-P2-2 | P2 | POTVRĐENO | TEKST | U r. 389 i 400 dodati „uz pretpostavku broda bez nagiba”; u Provjeri 2 navesti da je u ustaljenom zavoju mjerodavan nagib prema van, koji povećava razliku razina (uputa na pog. 6). |
| G1-15 | `u01:253–582` | Nijedan od šest riješenih primjera pog. 1 nije iz brodogradnje; brodski su samo uvod i Z2 (K16). Matrica za pog. 1 to ne traži (lajtmotiv: rashladni i hidraulični sustav). | A-P2-3 | P2 | POTVRĐENO | AUTORSKA ODLUKA | Ako autorica proširi opseg na P1–P6: promijeniti kontekst servisne dizalice (`u01:304`) u brodski uređaj s istim računom. AGENTS.md P1–P6 inače ne mijenja. |
| G1-16 | `u03:377` | „Dva neovisna mjerenja slažu se unutar 1 mm, bolje od razlučivosti vrpce.” Slaganje je posljedica složenih podataka ($U=18{,}60-0{,}35-15{,}940=2{,}310$ m). Pretvornik s 0,1–0,25 % od 250 kPa ima nesigurnost 3–7 cm stupca ulja (K9). | A-P2-4 (1) | P2 | POTVRĐENO | TEKST | „…slažu se unutar mjerne nesigurnosti tlačnog pretvornika, reda nekoliko centimetara.” |
| G1-17 | `u03:416` (Provjera 2) | Glavni praktični izvor pogreške tlačnog mjerenja razine nije naveden: gustoća tereta pri temperaturi tanka. Uz $\approx8\cdot10^{-4}$ 1/K, 10 K pogreške daje 7 kg/m³, odnosno 13 cm na 15,9 m. | A-P2-4 (2) | P2 | POTVRĐENO (red veličine; koeficijent je uobičajena vrijednost za plinsko ulje) | TEKST | Dodati rečenicu da se $\rho_u$ uzima pri temperaturi tereta, jer 10 K pogreške daje oko 0,1 m razine. |
| G1-18 | `u03:339` | Ručno sondiranje „s pastom” u tanku pod inertnim plinom: propisano je zatvoreno mjerenje kroz parnu bravu (ISGOTT). | A-P2-4 (3) | P2 | NEPOTVRDIVO (ISGOTT „po sjećanju”, nije u dodatku E) | TEKST | Ako se potvrdi u ISGOTT-u: „sonda za ulaž, temperaturu i granicu ulje–voda kroz parnu bravu”. Uz to dodati razgraničenje da se količina za predaju određuje iz tablica ulaža s ispravcima. |
| G1-19 | `u03:468` (`ex-u03-balastni-tank-broda-tlak-iznutra-i-izvana`) | Bočni tank tankera s dvostrukim trupom obično seže do palube; tank visok 5 m ispod vodne linije nije tipičan (nepotvrdivo). Fizikalni dio je točan: za tank viši od gaza neto tlak iznad vodne linije djeluje prema van, $\rho g(H_{tk}-z)>0$ uz vanjski 0. | A-P2-5 | P2 | POTVRĐENO (fizika) / NEPOTVRDIVO (tipičnost) | TEKST | Tank nazvati „donji bočni tank (nastavno pojednostavnjenje)” i dodati jednu rečenicu o promjeni smjera neto tlaka iznad vodne linije. |
| G1-20 | `u02:577`; `u03:712` (ključ Z3); `u03:416`; `d05_literatura.md` | Tvrdnje o praksi bez izvora i bez oznake nastavne procjene: „ulje statvene cijevi obično radi hladnije”, „u praksi se ne ide ispod 5–10°” (K9, K14). Dodatak E nema izvor za brodsko strojarstvo ni za mjerenje tereta. Odbačeno: `u04:595` (zaključak izveden računom u primjeru) i `u01:658` (naziv rasporeda, ne tvrdnja o praksi). | A-P2-8; S-P3-3 | P2 | POTVRĐENO (`u04:595`, `u01:658` ODBAČENO) | TEKST | Uz tvrdnje dodati „nastavna procjena” ili izvor. Tek nakon provjere izdanja dodati u dodatak E McGeorge, *Marine Auxiliary Machinery*, i Taylor, *Introduction to Marine Engineering*. |
| G1-21 | `u01:308` | „Upravljački klip” za mali klip ručne dizalice; drugdje u poglavlju stoji „crpni klip” (r. 153, 389, 528, 783). | A-P2-9 | P2 | POTVRĐENO | TEKST | „crpni klip površine $A_1$”. |
| G1-22 | `u01:5`/`44`/`249`/`823`; `u02:3`/`23`/`44`/`873`; `u03:3`/`65`, `u03:5`/`160`/`830`, `u03:190`/`195`; `u04:1`/`19` | Doslovna ponavljanja (K10): „tlak je skalarna veličina” 4×, „konstitutivni model, a ne opći zakon” 4×, u03:65 ponavlja r. 3, $p_{vak}$ stoji u zagradi i odmah u jednadžbi, u04:19 ponavlja r. 1. **Odbačeno:** (a) „uvod bez formula”, jer ugovor (odluka 15. 10. 2026.) traži da uvod objasni pojave i zakone; (b) ponavljanje u sažetku, jer prema odluci od 16. 10. 2026. sažetak uzima sadržaj iz teksta poglavlja. | U (K10, četiri retka); St-P3-1 | P2 | POTVRĐENO (dijelovi a i b ODBAČENO) | TEKST (brisanje doslovnih rečenica); formule u uvodu: AUTORSKA ODLUKA | Izbrisati drugu rečenicu `u01:5`, rečenicu „To nije univerzalni zakon…” u `u02:23`, `u03:65`, zagradu u `u03:190` i `u04:19`; uvodne formule ostaviti autorici. |
| G1-23 | `u04:23` i `u04:71`; `u04:114` i `u04:120`; `u01:114–121` i `u01:192–195` | Ista relacija numerirana dvaput: $\Delta h=aL/g$, paraboloid, Pascalov omjer (K10). `eq-…-fizikalno-znacenje-08` citira se u `u04:436`; `eq-…-izvod-01` i `razrada-koraka-03` nemaju upućivanja. | U (K10); S-P3-5 | P2 | POTVRĐENO | TEKST | Kasniju ili raniju pojavu ostaviti bez broja i uputiti na preostalu jednadžbu; zadržati ID-jeve koji se citiraju. |
| G1-24 | `u02:340`; `u03:821`; `u04:232` (i `u04:7`, `u04:307`) | Opisna upućivanja „kasnije”, „u sljedećem poglavlju”, „sljedeće poglavlje” (K12; alat). Najava pog. 5 („integraciju tlaka u silu”) stoji triput u pog. 4 (K10). | U (K12, K10) | P2 | POTVRĐENO | TEKST | Upotrijebiti `[]{.mf1-chapter-ref target="u11"}` / `"u04"`; rečenicu u `u04:232` izbrisati jer je pokrivaju r. 7 i 307. |
| G1-25 | `u01:169` | U CFD bloku pisanom u 1. l. mn. odgovor glasi „usporedi i hodove” (K2: glasovi se ne miješaju u bloku). | U (K2) | P2 | POTVRĐENO | TEKST | „…usporedimo i hodove.” |
| G1-26 | `u01:268`, `u01:316`, `u01:381`, `u04:305` | Potpis slike samo ponavlja naslov primjera i ne kaže što slika pokazuje (K13). | U (K13, dva retka) | P2 | POTVRĐENO | TEKST | Opisna rečenica, npr. „Hidraulička dizalica: mali i veliki klip povezani uljem, s hodovima obaju klipova.” |
| G1-27 | `u02:176` | „…daje takav test”: test nije spomenut u prethodnom odlomku (`u02:174`). | U (K3) | P2 | POTVRĐENO | TEKST | „…daje referentni test za takav CFD model:”. |
| G1-28 | `u02:333`, `u02:625`, `u02:780` | „Nadtlak” uz „pretlak” za isti pojam. U knjizi je „pretlak” 39×, „nadtlak” 12× (pog. 2, pog. 5, d03, d06). | U (K7) | P2 | POTVRĐENO | TEKST | U pog. 2 posvuda „pretlak”; pog. 5 i dodatke uskladiti u svom ciklusu. |
| G1-29 | `u03:160` (45 riječi), `u04:181` (41), `u04:413` (≈44) | Rečenice duže od 40 riječi s nizom koraka ili članova (K3; alat, moj brojač). | U (K3, alat) | P2 | POTVRĐENO | TEKST | Uvodna rečenica i numerirani popis koraka ili članova; `u04:413` podijeliti na tri rečenice (spojiti s G1-14). |
| G1-30 | `u02:445`, `464`, `484`, `851`, `857`; D06; `u02_ch1_kapilarni_mikrodozator_kapljica.svg` | $h_{cap}$ ima engleski indeks; urednički stil traži hrvatske indekse (K6). | U (K6) | P2 | POTVRĐENO | TEKST + SKICA (oznaka; D06 obnoviti generatorom) | $h_{kap}$ u tekstu, skici i ključu; ime varijable u verifikatoru nije vidljivo i može ostati. |
| G1-31 | `u03:149`, `u03:190`, `u03:834` | „Najčešća je pogreška…” (r. 149) i „jedna od najtipičnijih” (r. 190) bez osnove, a sažetak kao najčešću navodi drugu (K9). Druga rečenica r. 149 nije povezana s prvom. Kad atmosfera nije nula, kaže se tek u sažetku. | U (K9, K10); St-P3-2 | P2 | POTVRĐENO | TEKST | „Česta je pogreška…” uz primjer (zatvoreni spremnik, usporedba s $p_v$); rečenicu o piezometarskoj visini odvojiti; zadnju rečenicu r. 190 izbrisati. |
| G1-32 | `u03:68`, `u03:156`, `u03:189`; `u04:40`, `u04:95` | Blok „Fizikalno značenje” nema podnaslov (urednički stil: „Vrsta — Podnaslov”); u pog. 2 ga ima. | U | P2 | POTVRĐENO | TEKST | Npr. „Fizikalno značenje — Piezometarska visina”, „— Efektivno polje sila”. |
| G1-33 | `u03:166` | CFD blok rabi $T$, $H_{tk}$ i ploču $P$ prije primjera P5 (`u03:468`) u kojem se uvode (K5). **Odbačeno** za $p_{rgh}$: definiran je u istoj rečenici. | U (K5); St-P2-1 | P2 | POTVRĐENO (dio o $p_{rgh}$ ODBAČENO) | TEKST | „…ručnom računu $\rho_{mv}g(T-H_{tk})$ iz primjera [-@ex-u03-balastni-tank-…], s gazom $T$ i visinom tanka $H_{tk}$.” |
| G1-34 | `u03:329` | „…tlak veći u vodu slatke vode”: „u vodu” se čita kao akuzativ od „voda”. | U | P2 | POTVRĐENO | TEKST | „…tlak veći u vodu kojim teče slatka voda”. Urednikov prijedlog („u vodu sa slatkom vodom”) dvosmislenost ne uklanja. |
| G1-35 | `u03:459` | $NPSH_a$ i $NPSH_r$ bez definicije i upućivanja (K5). | U (K5); St-P3-4 | P2 | POTVRĐENO | TEKST | „…raspoložive kavitacijske rezerve $NPSH_a$ s potrebnom $NPSH_r$ koju daje proizvođač (pog. 13)”. |
| G1-36 | `u03:534`, `u03:538` | Kratica „IoT” javlja se dvaput i nije objašnjena; ispod praga od tri pojave (K5). | U (K5); S-P3-6 | P2 | POTVRĐENO | TEKST | „umreženi tlačni senzor” u naslovu i u r. 538. |
| G1-37 | `u03:712` (ključ Z3) | „…osjetljiv na horizontiranje” (K7: vodoravno, ne horizontalno). | U (K7) | P2 | POTVRĐENO | TEKST | „…osjetljiv na vodoravno postavljanje instrumenta” (s G1-20 u istoj rečenici). |
| G1-38 | prikaz `chapter-ref` (`filters/mf1-components.lua`, `chapter_link`); npr. `u01:5`, `u01:111`, `u01:183` | PDF ispisuje „…u pog. 3 Hidrostatička raspodjela tlaka i manometrija.”: naslov u nominativu bez razgraničenja usred rečenice (potvrđeno u `pog01.pdf`, retci 17, 180, 260). | U (zajedničko) | P2 | POTVRĐENO (razina knjige) | TEKST (adapter, ne izvor) | U tekućoj rečenici ispisivati „pog. 3” ili „pog. 3 („Naslov”)”; provjeriti je li zahvat već u tijeku (filtar je u radnoj kopiji izmijenjen). |
| G1-39 | `u03:700` (Z3, Traži se 3) | „Usporedi s okomitim U-manometrom” ne kaže čita li se razlika razina ili pomak jednog kraka; omjer je 3,64 ili 7,29 (račun). Naputak u dodatku F to razrješava. **Odbačeno:** da ključ nema kriterij za kut, jer `u03:712` navodi razloge. | St-P2-2 | P2 | POTVRĐENO (dio o ključu ODBAČENO) | TEKST | U Traži se 3 dodati „(očitanje je razlika razina dvaju krakova)”. |
| G1-40 | `u03:793` (Z6, Traži se 2) | Već nominalni tlak isključuje područje 0–140 kPa ($1{,}05\cdot135{,}28=142{,}05$ kPa), pa analiza tolerancija ne mijenja odluku T4 (K15). Rečenica naputka „nominalna vrijednost sama nije dovoljna” zbunjuje. | St-P2-3 | P2 | POTVRĐENO | BROJ/MODEL (+ ključ, verifikator `verify_u03.py`, D06) | Npr. rezervu smanjiti na 3 %: nominalno 139,34 kPa (0–140 bi prošlo), konzervativno 140,13 kPa (ne prolazi). Razmak je malen, pa podatke bira autorica. |
| G1-41 | `u03:143–211` | Manometrija (dio naslova poglavlja) nema vlastiti odjeljak; sve je pod „Otvoreni i zatvoreni spremnici”. | U (K4) | P3 | POTVRĐENO (težina snižena: naslov nije pogrešan) | AUTORSKA ODLUKA (strukturna promjena, novi ID) | Po odluci autorice ispred r. 160 umetnuti „## Manometri i reference tlaka” s novim semantičkim ID-jem. |
| G1-42 | `u03:817–821` | Most prema pog. 4 sa sl. 3.8 stoji iza zadataka, a ispred sažetka. Sadržajno ponavlja `u03:95` i uvod pog. 4. | U | P3 | POTVRĐENO (K12 dio u G1-24) | AUTORSKA ODLUKA | Sliku premjestiti uz `u03:95` ili izostaviti. |
| G1-43 | `u03:262`; `tools/verify_u03.py:41` | $\rho_{mv}=1035$ kg/m³, a drugdje u pog. 3, 4 i 6 stoji 1025. Vrijednost je fizikalno moguća; primjeru nedostaje tehnički kontekst. | A-P2-6 | P3 | POTVRĐENO (težina snižena: nije pogreška, promjena nije jeftina) | BROJ/MODEL | Pri sljedećoj reviziji uzeti 1025 i kontekst središnjeg hladnjaka (slatki krug drži viši tlak od mora). |
| G1-44 | `u03:459` | Za ulje je praktična granica usisa izdvajanje otopljenoga zraka, a ne $p_v$. Tekst već ograđuje „11,8 m samo je gornja granica pri nultom protoku” i ne propisuje sigurnu visinu. | A-P2-7 | P3 | POTVRĐENO (fizika); 0,8 bar NEPOTVRDIVO | TEKST | Jedna rečenica o izdvajanju otopljenoga zraka i potopljenom usisu, označena kao nastavna procjena. |
| G1-45 | `u02:492` | Puna brzina vrtnje odmah nakon hladnog isplovljenja nije uobičajen pogonski postupak. | A-P2-1 (4) | P3 | NEPOTVRDIVO (praksa) | TEKST | Ako se mijenjaju temperature (G1-12), „hladno isplovljenje” zamijeniti „hladnim startom”. |

## Račun za P1 (G1-01)

Podatci iz `u04:683`: $L=2{,}00$ m, $h_0=0{,}80$ m, $a_x=1{,}5$ m/s², $a_z=\pm1{,}2$ m/s².

- **Ravnoteža obješenog tijela.** Na sustav (užad, spremnik i voda) djeluju
  samo sila u užetu i težina. Iz $\vec F_{uze}=m(\vec a-\vec g)=-m\vec g_{eff}$
  slijedi da uže leži u pravcu $\vec g_{eff}$. Otklon od okomice je
  $\tan\theta=a_x/(g+a_z)=0{,}1362$, odnosno $7{,}76^\circ$; pri usporavanju je
  $0{,}1742$, odnosno $9{,}88^\circ$.
- **Moment oko kuke.** U okviru spremnika težište mora ležati na pravcu kroz kuku
  usporedno s $\vec g_{eff}$. Ako spremnik ostane vodoravan, voda pomakne težište
  unatrag za samo $\approx L^2\tan\theta/(12h_0)=0{,}057$ m. Pravac iz kuke pod
  $7{,}8^\circ$ prolazi kroz razinu težišta mnogo dalje od osi, pa vodoravan
  položaj nije ravnoteža. Ravnoteža nastaje kad je os spremnika usporedna s
  $\vec g_{eff}$. Tada je površina okomita na $\vec g_{eff}$, dakle usporedna s
  dnom, a razlika razina uz stijenke iznosi 0.
- **Tlak na dnu.** $g_{eff}=\sqrt{a_x^2+(g+a_z)^2}=11{,}112$ m/s², pa je
  $p_M=\rho g_{eff}h_0=8{,}89$ kPa. U ključu stoji 10,31 kPa. Pri usporavanju je
  $g_{eff}=8{,}740$ m/s² i $p_M=6{,}99$ kPa (u ključu 8,39 kPa).
- **Model teksta.** Moj račun reproducira brojeve ključa (0,2725 m; 0,9362 m;
  10,31 kPa; 0,3484 m; 8,39 kPa). Ključ je dakle točan za kruto vođen spremnik,
  a ne za spremnik koji visi.

Izmjena dira `source/u04_…:683` (tekst), `u04:853` (napomena uz skice), panel
Z2 u `assets/…/u04_vjezbe_skice.svg` (stropi i kuka), `tools/verify_u04.py:147`
(samo opis, ako brojevi ostaju) i D06 preko generatora.

## Što je dobro (iz izvještaja)

- **Brojčana pouzdanost.** Struka je preračunala svih 48 primjera i zadataka.
  Izvan zaokruživanja nema pogreške, a ključ se slaže s izvorom. Moj račun
  potvrđuje provjerene brojeve u G1-01, G1-06 i G1-40. Neovisne provjere u
  primjerima su stvarne: bilanca rada, disipacija jednaka snazi,
  $\rho gh=4\sigma/d$, dva puta do $p_{M,B}$ i srednja razina sondi.
- **Brodske primjene.** Sondiranje teretnog tanka s talogom i inertnim plinom
  i balastni tank iznutra i izvana su dobri primjeri. Separator goriva ima
  realne gustoće i kvantitativnu granicu modela (vrijeme zadržavanja,
  Coriolisov član). Kormilarski stroj ima realne brojke.
- **Razgraničenje od propisne ocjene.** Dosljedno je kroz cijelu skupinu, npr.
  „nije dopuštena nosivost”, „ne zamjenjuju propisni proračun”, „nije radna
  karta”.
- **T4-zadatci.** Zajamčeni intervali, konzervativni krajevi i rezerva prema
  zanemarenom učinku uče stvarnu inženjersku odluku.
- **Reference tlaka.** Apsolutni, manometarski i vakuumski tlak, $p_{rgh}$ u CFD-u
  i usporedba apsolutnog tlaka s $p_v$ vode se dosljedno. Pravilo hoda kroz
  stupce (`u03:160`) i odlomci „Veza s proračunom” studentu su najviše pomogli
  (St).
- **Kapilarnost.** Konkavni i konveksni meniskus te stanja punjenja i formirane
  kapljice dosljedno se razlikuju.
- **P6 pog. 1.** Primjer kvantitativno opravdava pretpostavku jednakih visina
  (kPa prema MPa; isti $\Delta z$ pri 100 kPa).

## Sažetak P3 nalaza (izvještaji: S 9, A 13, U 10, St 7; ukupno 39)

| Skupina | Broj | Mjesta (primjeri) | Ocjena provjere |
| --- | ---: | --- | --- |
| Nazivlje, sitni izrazi, interpunkcija | 9 | konstantan/stalan, izotermalan, „manometarski pretlak” (`u03:157`), „Tih 5 % zadana je” (`u04:823`), crtice | uglavnom točno, jeftino; autorica bira |
| Oznake lokalno definirane, a sudaraju se s tablicom stila | 3 | $k$, $\alpha$, $G$, $p_u$/$\rho_u$, $H$; oznaka $A$ u ključu Z3 | točno; ispraviti samo $A$ u ključu Z3 i $p_u$ |
| Vjerodostojnost podataka „po sjećanju” | 9 | kočnica 35 mm, stezna naprava s ručnim klipom, dron na 1528 m, ubrzanja dizalice, autocisterna 1,2 m, $A_t=600$ m², P/V ventil, etanol $\theta=18^\circ$, ploča 0,22 m² | nepotvrdivo bez izvora; dron iznad 120 m ima smisla zamijeniti |
| Skice i prikaz | 4 | šrafura zraka i preklapanje oznaka na sl. 3.3 i 1.5, dvostruki $p_{atm}$ na sl. 3.6, neimenovana dublja točka Z6 | potvrditi na renderu; SKICA |
| Razine T1–T4 | 1 | u03 Z1 (T1→T2?), u04 Z5 (T3→T4?), u04 P4 | ne mijenjati radi kvote (AGENTS.md); autorica |
| Rezultat zadatka u teoriji | 1 | `u02:250` „faktor 2 umjesto 4 (Z4)” | točno; brisanje jeftino |
| Ponavljanje i nacrt uvoda | 3 | „Poglavlje redom obrađuje…” 4×, diferencijalni manometar bez izvoda hodom, dvostruke jednadžbe (spojeno u G1-23) | dio spojen u G1-22 i G1-23 |
| Kratice i iskustvene tvrdnje | 3 | PDMS 2× (`u02:585`, već raspisan u zagradi), Re bez uputnice na pog. 11, sonde 1,70 − 1,50 = 0,19 (`u04:389`; točno 0,194) | točno; jeftino |
| Suvremenost i dodatni konteksti | 3 | metanol, LNG, električni trajekt, pojačivač tlaka, brodski vijak u zagradi | prijedlozi; matrica ih ne traži |
| **Odbačeno** | 3 | S-P3-8 (Interaktivni prikaz: prema uredničkom stilu laboratorij s widgetima nosi taj naziv); A-P3-13 „oplakana površina” (potvrđeno nazivlje); St-P2-2 dio o kriteriju kuta | sukob s uredničkim stilom ili nazivljem |

## Izvan opsega knjige

Struka je u `G1_kljuc.pdf` vidjela stranice 335, 337 i 338 dvaput. To je
artefakt izvatka skupine i nije provjereno na punom PDF-u.

## Ograničenja provjere

- Ova provjera je autorska procjena jednog agenta. Prolaz računa i nalaza ne
  dokazuje didaktičku kvalitetu.
- Skice nisu vizualno pregledane; oznake su provjerene samo kroz tekst SVG-a
  i `fig-alt`.
- Tvrdnje o pravilima i praksi (ISGOTT, klasifikacijska društva, IS Code,
  proizvođači) nisu provjerene u izvoru. Zato su označene kao NEPOTVRDIVO.
- Verifikatori nisu pokrenuti. Nijedna datoteka osim ovog izvještaja nije
  mijenjana.
