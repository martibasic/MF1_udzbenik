# Vizualna i tipografska recenzija PDF-a

Predmet: `_book/mehanika-fluida-1.pdf` (335 str., A4, Typst 0.14.2, commit 2fff6c5, izgrađen 16. 10. 2026. 17:24).
Metoda: sve stranice renderirane u PNG (100 dpi, PyMuPDF) i automatski pregledane skriptom
(`scratchpad/recenzija/pdf/analyze.py`, rezultat u `analysis.json`); ručno pregledano 60-ak stranica
kao slike: naslovnica, sadržaj, dvije prve stranice poglavlja 1, 2, 3, 4, 6, 7, 9, 10, 13, stranice s
riješenim primjerima (13, 17, 18, 20, 36, 55, 61, 74, 78, 137, 189, 214, 226, 263, 269), sa zadatcima
(23, 24, 44, 64, 101, 173, 282), s velikim slikama (26, 45, 64, 101, 123, 137, 282), s tablicama (205,
287, 288, 296, 309, 315), s dugim izvodom (224, 226), dodatci A, B, C, D, E, F i posljednje stranice.
Ništa u repozitoriju nije mijenjano.

Oznake: „provjereno” = izmjereno skriptom ili viđeno na renderu; „dojam” = autorska procjena.

## 1. Sažetak

PDF je tipografski uredan u osnovi: Libertinus Serif 11 pt s New CM Math, jedan stupac, dosljedna
zaglavlja (naslov poglavlja gore lijevo, folija centrirana dolje), nema ni jednog retka ni jednadžbe
koja strši izvan stupca (provjereno na svih 335 stranica), a oznake u skicama drže minimum 9 pt
(Liberation Sans 9–9,5 pt). Dojam suvremenosti ipak kvare tri stvari koje se vide na gotovo svakoj
stranici: u matematičkom slogu decimalni zarez dobiva razmak („9, 81” umjesto „9,81”; 2976 pojava na
209 stranica), iza mjerne jedinice stoji razmak pa točka („179 kPa .”; 203 pojave na 83 stranice), a
oznake točaka A, B, P, HGL/EGL slažu se u monospace fontu kao programski kod. Prijelom je
nedosljedan: slike se ne „plutaju”, pa 20 stranica završava s 18–66 % praznine, sedam je stranica gotovo
praznih (9, 27, 85, 124, 235, 286, 316), a 20-ak naslova „Traži se”/„Rješenje” ostaje na dnu stranice s
jednim retkom ispod. Naslovnica je samo tekst bez godine, izdavača i ikakvog grafičkog elementa, a
odmah na poleđini počinje sadržaj. Sažetci poglavlja postoje u dva različita oblika (numerirani prozni
odjeljak u pog. 1–5 i 13, okvir s natuknicama u pog. 6–12, 14–15), a svaki poglavlje i dodatak ima
odjeljak „X.1” s istim naslovom kao i poglavlje. Za crno-bijeli ispis skice su u redu (jedna boja vektora,
razlika stilom crte), ali ispuna ulja i vode u sivoj se gotovo ne razlikuje (sivo 223 prema 231). Ništa od
navedenoga nije sadržajno; sve se rješava u predlošku/Typst konfiguraciji i u nekoliko SVG-ova, pa je
PDF blizu završetka, uz tri-četiri sustavna popravka.

## 2. Nalazi po prioritetu

### P1 — ispraviti prije završetka

| # | Gdje | Što (provjereno) | Zašto je problem | Prijedlog |
|---|------|------------------|------------------|-----------|
| 1 | cijeli PDF (209 str., npr. 13, 17, 20, 78, 247, 334) | U matematičkom slogu „$9,81$” ispisuje se kao „9, 81”, „$0,86$” kao „0, 86”; 2976 pojava. Isto u tekstu kad je broj u `$…$` (str. 48 „9, 81 kPa”, str. 173 „1, 667”). | Decimalni zarez je u hrvatskom standard; razmak iza njega čita se kao nabrajanje („166, 67; 90, 91” na str. 334 doslovno izgleda kao četiri broja). Najvidljiviji tipografski nedostatak knjige. | U Typst predlošku zamijeniti zarez u brojevima ne-razmaknutim znakom (npr. `show regex("\d,\d")` pravilo ili `math.class("normal", ",")`), ili u izvoru pisati `9{,}81`. Jedan globalni popravak. |
| 2 | 83 stranice (npr. 17 eq. 1.23/1.25, 18, 20, 23, 55, 61, 74, 78, 226, 269) | Jednadžbe završavaju „… = 179 kPa .” — razmak pa točka; 203 pojave. Negdje točka stoji odmah („= 652 Pa .” str. 226 ali „0, 86.” str. 13). | Nedosljedna interpunkcija u 800 prikazanih jednadžbi; izgleda kao greška u slogu. | Točku staviti unutar `$…$` uz jedinicu bez razmaka ili je dosljedno izostaviti u istaknutim jednadžbama (tada i na str. 13 „0,86.”). |
| 3 | str. 52–84, 146–147, 154–158, 184–191, 321 | Oznake točaka i presjeka (A, B, P, AB, C, D, A-A), kratice HGL/EGL i brojevi grana 1, 2, 3 (str. 187–191) slažu se kao kod: DejaVu Sans Mono 8,8 pt u sredini serifnog retka („Tlak u točki `A`”, „`HGL` jednaka je zbroju…”). | Mono font u tiskanom udžbeniku označava programski kod; ovdje zbunjuje i vizualno „iskače”; u D dodatku (str. 234, 310, 315) kod je ispravno mono, pa se značenje miješa. | U izvoru točke pisati kao matematičke oznake ($A$, $\mathrm{A}$) ili kurzivom; HGL/EGL kao običan tekst/kratice. Mono zadržati samo za nazive datoteka i naredbe. |
| 4 | str. 9, 27, 85, 124, 235, 316 | Gotovo prazne stranice: 9 (4 natuknice, 95 % prazno), 27 (3 retka sažetka), 85 (5 redaka), 124 (3 natuknice), 235 (okvir „Sažetak” s 6 natuknica), 316 (3 retka + okvir). Str. 286 „Dodaci” sadrži samo naslov. | Sedam gotovo praznih stranica u knjizi od 335 djeluje neuredno i nepotrebno povećava opseg; posebno 27, 85, 124 jer odmah iza njih novo poglavlje počinje na parnoj stranici. | Stisnuti razmake oko okvira sažetka (ili dopustiti da sažetak počne na istoj stranici sa skicama), odnosno kratiti završne rečenice; za „Dodaci” dodati mini-sadržaj kao na stranicama dijelova (10, 47) ili ukloniti razdjelnicu. |
| 5 | str. 20, 23, 43, 55, 56, 61, 91, 105, 120, 123, 151, 157, 173, 194, 195, 214, 215, 283, 305, 306 | Naslov („Traži se”, „Rješenje”, „1. Dimenzijska analiza”, „9 · Kompresibilni idealni tok”) stoji u posljednja 2–3 retka stranice, s najviše jednim retkom sadržaja ispod. Str. 305/306: naslov poglavlja u dodatku C i red „vizualnih oznaka”, a tekst na sljedećoj stranici. | Siročad naslova: čitatelj okreće stranicu da vidi što se traži; tipografsko pravilo „naslov + najmanje 2 retka”. | U Typstu za te naslove postaviti `block(breakable: false)` s prvim odlomkom ili `sticky: true`; za „Traži se” spojiti naslov i prvi element popisa u nelomljivi blok. |
| 6 | str. 1 (naslovnica), 2–5 (sadržaj), 6 (impresum) | Naslovnica: samo lijevo poravnan tekst (oznaka „PRIRUČNIK”, naslov u dva retka, podnaslov odmah ispod bez razmaka, autorica), 60 % stranice prazno; nema godine, mjesta, ustanove ni grafičkog elementa. Sadržaj počinje na str. 2 (poleđina naslovnice), impresum je tek na str. 6, i to kao natuknice unutar odjeljka s naslovom knjige; u njemu „Status: radno izdanje”, „Verzija: 1.0-rc1”, „ISBN / DOI: u pripremi” i tri poveznice kao narančasti tekst bez URL-a. | Za postupak odobravanja sveučilišnog priručnika naslovnica i impresum prvi su dojam recenzenta; ovako PDF izgleda kao radni ispis. Poveznice bez URL-a u tisku su mrtve. | Naslovnica: dodati godinu, ustanovu i jedan vizualni element (npr. skica 1.1 ili 7.1 u jednoj boji preko donje polovice); razmak naslov–podnaslov. Poleđina naslovnice = impresum (autorica, naslov, ustanova, godina, licencija, verzija, ISBN kad bude), sadržaj od str. 3. U impresumu ispisati URL-ove ili ih ukloniti; „radno izdanje” zamijeniti konačnim statusom prije predaje. |
| 7 | str. 101 (Slika 5.8), 177 (Slika 10.1), 282 (Slika 15.2), 36 (Slika 2.3), 55 (Slika 3.3) | Kolizije oznaka: str. 101 „H = 3,00 m (A–B)” preko desne stijenke, „Pmax = 12,00 kN” preko kote, „HF = ?” ispod crte „Fm = (11,60 ± 0,30) kN”; str. 177 oznake „Rst→f,y” i „Rst→f,x” preklapaju se; str. 282 Z6 „y1 = 0,350 m” preko „Qd”, opis „Qd = 8,00 / m³/s.” prelomljen tako da „m³/s.” stoji sam u retku; str. 36 podnaslov skice prelomljen „A = 0,18 / m²”; str. 55 „h3 = 0,70 m” preko kotne crte. | Preklopljene ili prelomljene oznake ne čitaju se u tisku, a jedinica odvojena od broja je tipografska pogreška. | Pomaknuti oznake / skratiti tekst u SVG-u (npr. „Qd = 8,00 m³/s” u vlastiti redak, „A = 0,18 m²” s nelomljivim razmakom); pri tome zadržati postojeći stil. |
| 8 | str. 123, 198, 235 i svi sažetci pog. 6–12, 14–15 nasuprot str. 26, 46, 66, 84, 103, 253 | Dva oblika sažetka: pog. 1–5 i 13 imaju numerirani odjeljak „X.6 Sažetak” u prozi (3 odlomka); pog. 6–12, 14, 15 imaju nenumerirani okvir „Sažetak” s natuknicama + „Najčešća pogreška” + „Nakon ovoga poglavlja mora biti moguće”. U sadržaju se zato „Sažetak” pojavljuje samo za 6 od 15 poglavlja. | Nedosljednost strukture vidi se već u sadržaju (str. 2–5) i djeluje kao nedovršena revizija. | Odabrati jedan oblik za svih 15 poglavlja (preporuka: numerirani odjeljak „Sažetak” koji sadrži kratku prozu + tri postojeća podnaslova) i ujednačiti u predlošku; nije novi sadržaj, samo preslagivanje. |

### P2 — vrijedi napraviti

| # | Gdje | Što | Zašto | Prijedlog |
|---|------|-----|-------|-----------|
| 9 | 20 stranica: 1, 9, 44, 46, 67, 74, 86, 124, 135, 176, 189, 193, 198, 200, 209, 235, 254, 263, 269, 314 | Donja praznina 180–660 pt (18–66 % stupca) jer slika ne stane pa cijela ide na sljedeću stranicu (npr. 74→75, 189→190, 263→264), a tekst se ne nastavlja ispod. | Rastrgan ritam, veći opseg; str. 263 završava na 55 %. | Dopustiti plutanje slika (`figure(placement: auto)`) ili smanjiti najveće skice (vidi #12); tekst „Veza s proračunom” može ići ispred slike. |
| 10 | str. 48, 67, 200 (uvodi pog. 3, 4, 11) | Tekst kaže „Slika ispod prikazuje…”, a slika je na sljedećoj stranici (49, 68, 201); donja trećina stranice prazna. Isti obrazac na str. 176 („Slika u nastavku”, slika na 177) i 86. | U tisku „ispod” nije točno; vizualno uvodna stranica izgleda prekinuto. | Skratiti uvodni odlomak za 3–5 redaka da slika stane, ili pisati „Slika 3.1” s brojem. |
| 11 | str. 12, 29, 49, 68, 87, 105, 127, 146, 177, 201, 222, 238, 255, 274 te A.1, B.1, C.1, D.1, E.1, F.1 | Prvi odjeljak svakog poglavlja i dodatka nosi isti naslov kao poglavlje („6. Uzgon, plivanje i početni stabilitet” → „6.1 Uzgon, plivanje i početni stabilitet”); sadrži samo okvir „Inženjerski kontekst” i „Procijenjeno vrijeme”. Iznimka pog. 1 („1.1 Fluid kao kontinuum”). | Udvostručen naslov u sadržaju (str. 2–5) i na stranici; numeracija odjeljaka pomaknuta za jedan bez razloga. | Ukloniti razinu „X.1” i staviti okvir i procjenu vremena izravno ispod naslova poglavlja (kao što pog. 1 već radi); u dodatcima isto. |
| 12 | str. 64 (Slika Z1–Z2), 137 (Slika 7.5), 78 (4.5), 101, 123 | Skice zauzimaju 40–55 % stranice, a nose malo informacija (str. 64: dva spremnika s po 2 oznake preko pola stranice; 137: spremnik visok 35 % stupca). Oznake ostaju 9 pt, pa veliki prizor ne povećava čitljivost. | Troši prostor, uzrokuje praznine iz #9 i vizualnu neujednačenost prema malim skicama (str. 36, 163). | Za te skice smanjiti format (STANDARD umjesto WIDE/COMPOSITE) u tiskovnim izvedenicama, uz nepromijenjenu veličinu oznaka. |
| 13 | str. 23, 44, 101, 173 nasuprot 13, 17, 36, 55 | Razina zadatka: u riješenim primjerima je u naslovu („P2. … T2”, sitno sivo), u zadatcima za vježbu stoji desno poravnano „Razina: T1” ispod popisa, pa sljedeći „Zn.” naslov počinje odmah bez razmaka (str. 173: četiri zadatka bez vizualnog odvajanja). | Dva mjesta za istu informaciju; zadatci se slijevaju jedan u drugi. | Oznaku razine staviti u naslov Zn jednako kao kod Pn i dodati razmak (≈ 1 em) ispred svakog Zn naslova. |
| 14 | svi riješeni primjeri; npr. str. 13 (1.5)–(1.6), 17 (1.22)–(1.25), 269 (14.49)–(14.56) | Numerirano je 798 jednadžbi, a u tekstu se poziva na ~49 (provjereno pretragom „jednadžba (n.m)”). Numerirani su i zadani podatci („g = 9,81 m/s² (1.5)”) i svaki međukorak. | Brojevi uz svaki redak vizualno opterećuju i obezvređuju brojeve koji doista trebaju; pog. 6 ima 85 jednadžbi. | Numerirati samo jednadžbe u teoriji i one na koje se poziva; u rješenjima koristiti nenumerirane istaknute jednadžbe. Tehnički: izvor označava samo referirane. |
| 15 | str. 319–335 („Vrati se na zadatak”, 91 puta); str. 7, 14, 90, 146 („Pokreni u pregledniku”, „Pričuvno: otvori u Colabu”, 15 puta); unakrsne poveznice „primjeru 3.3”, „Venturijevu primjeru” | Poveznice su narančasti tekst bez broja stranice ni URL-a; u tisku (i u crno-bijelom) to je sivi tekst bez funkcije. | Ključ F u tiskanom izdanju ne vodi nikamo; uz QR kod tekst „Pokreni u pregledniku” nema smisla. | U PDF-u ispisati „→ str. 23” uz „Vrati se na zadatak” (Typst `locate`), a u okvirima s QR-om zamijeniti dvije poveznice jednim retkom „Skeniraj QR ili otvori <kratki URL>”. |
| 16 | str. 11–12, 28, 48, 67, 104, 176 i općenito | Odlomci nemaju ni uvlaku ni razmak (razmak između odlomaka ≈ 2 pt): na str. 28 i 104 šest odlomaka izgleda kao jedan blok od 40 redaka. Duljina retka ≈ 90 znakova. | Čitljivost gustih uvodnih stranica; dojam „zida teksta”. | Dodati razmak među odlomcima 0,5–0,6 em ili uvlaku 1 em; razmotriti suženje stupca za 20–30 pt (sada 452 pt) ili veći prored. |
| 17 | str. 14, 90, 146 (okviri s QR kodom) | Unutar okvira 60–70 pt praznine između teksta i poveznica; QR (90×90 pt) desno gura tekst. | Okvir izgleda nedovršeno. | QR smjestiti uz tekst u retku (lijevo tekst, desno QR iste visine), bez praznog pojasa. |
| 18 | str. 205 (Slika 11.2), 287–288, 296, 303, 309, 315 i tablica na str. 205 | Nijedna tablica nema broj ni naslov („Tablica …” se ne pojavljuje), a dimenzijska matrica na str. 205 numerirana je kao „Slika 11.2” iako je tablica. Tablica bezdimenzijskih brojeva na str. 205 ima stupac „Fizikalno tumačenje” širok 100 pt pa redci imaju 4–6 prelomljenih redaka. | Nedosljednost objekata; na tablice se ne može pozvati. | Uvesti numeraciju „Tablica n.m” za tablice u glavnom tekstu, dimenzijsku matricu preimenovati; stupcima na str. 205 dati širine ~12/14/34/22/18 %. |
| 19 | str. 303–306 (dodatak C) | Ispod svakog naslova poglavlja stoji redak „vizualnih oznaka” poput „ρ / γ / p F / A”, „F_U V_ist GM / GZ”, „a/(v ± a) Ma/p0”, najavljen rečenicom na str. 303. | Čita se kao ostatak nekog starog ikonografskog sustava; u tisku nema značenja i izgleda kao greška. | Oblikovati kao jasnu etiketu („Ključne veličine: ρ, γ, p; F/A”) sivim sitnijim slogom ili ukloniti redak i rečenicu koja ga najavljuje. |
| 20 | skice s uljem i vodom: str. 11, 13, 45, 115, 123 (desno) i dr. | Ispuna vode #dcebf1 (siva ≈ 231) i ulja #eadfc5 (siva ≈ 223) u crno-bijelom ispisu su praktički iste; razlika postoji samo gdje je tekstualna oznaka. Vektori su u redu (jedna boja, razlika debljinom i vrhom). | Crno-bijeli ispis gubi razliku fluida (npr. str. 123 Z4 „voda”/„ulje” ima oznake, str. 115 ulje nad vodom oslanja se na boju). | Ulju dati svjetliju/tamniju ispunu (siva ≥ 40 razlike) ili rijetku šrafuru u tiskovnim izvedenicama; paleta web skica ostaje. |
| 21 | str. 214 (Slika 11.8), 104 (6.1), 126 (7.1), 163 (9.1), 247 (13.3) | Sitne nedosljednosti u skicama: str. 214 redak „zrak: ρ = 1,2 kg/m³; ν = …” u serifu 9 pt dok su ostale oznake Liberation Sans; „0,1” na osi preklapa „10²”; str. 126 „bilo koji proces / uređaj” udara u oznaku „KV”, „ρ1, A1, v1” preko isprekidane crte; str. 247 „obilazni smjer, Q > 0” preko unutarnjeg ruba, strelica „QD” preko slova „D”; str. 104 desni panel vrlo malen (oznake „M”, „G”, „B” zgurane). | Smanjuju dojam profesionalnosti upravo na uvodnim slikama poglavlja. | Male korekcije položaja oznaka u SVG-u; na str. 214 ujednačiti font. |
| 22 | str. 198, 123, 235 (okviri sažetka) | Natuknice u okviru imaju prored tako tijesan da vektorske strelice i indeksi dodiruju prethodni redak („R⃗_st→f”, str. 198); isto u popisu na str. 124. | Čitljivost matematike u popisima. | Prored popisa u okviru izjednačiti s osnovnim (1,25–1,3) ili `par(leading: 0.65em)`. |
| 23 | str. 7 i 6 | Dva odjeljka „O priručniku” (str. 6 i 7) s preklapajućim sadržajem; uvodni odjeljak nosi naslov cijele knjige („Mehanika fluida: modeli, problemi i rješenja” kao naslov na str. 6 i prva stavka sadržaja). | Zbunjujuće u sadržaju i na stranici. | Str. 6 preimenovati u „Predgovor” (ili spojiti s impresumom), zadržati jedan „O priručniku”. |
| 24 | str. 2–5, 10, 47, 286 | Sadržaj ide do treće razine samo za dodatke (A.3–A.13 su podnaslovi tablica), a stranice dijelova (10, 47) ponavljaju iste stavke; „Dodaci” (286) nema mini-sadržaj. | Nedosljedno; 4 stranice sadržaja + 5 razdjelnica. | U glavnom sadržaju prikazati dvije razine, dodatke do razine A.2; razdjelnice dijelova ujednačiti (sve s mini-sadržajem ili nijedna). |
| 25 | str. 317 | „E.7 Bibliografski zapisi” počinje s jednom stavkom [1] na dnu stranice, ostatak na 318. | Siroče popisa. | Prebaciti naslov E.7 na novu stranicu (`pagebreak(weak: true)` prije). |
| 26 | zaglavlje svih stranica | Živo zaglavlje jednako na lijevoj i desnoj stranici (naslov poglavlja), bez naslova odjeljka; poglavlja počinju na parnim i neparnim stranicama (28, 48, 86, 104, 126… parne). | Za dvostrano tiskano izdanje recto/verso nije razlikovano; ako je izdanje jednostrano, prihvatljivo. | Odlučiti: ako ide u tisak dvostrano, poglavlja na recto, zaglavlje verso = poglavlje, recto = odjeljak. Inače ostaviti i navesti u impresumu „namijenjeno jednostranom ispisu/zaslonu”. |

### P3 — opcionalno

| # | Gdje | Što | Prijedlog |
|---|------|-----|-----------|
| 27 | str. 36, 55, 78, 137, 247 i dr. | Naslov unutar skice („Smicanje ulja između ploča”) ponavlja potpis slike („Slika 2.3: Smicanje ulja između nepomične i pokretne ploče”). | Zadržati naslov u skici samo u kompozitnim Z1–Z6 skicama; kod pojedinačnih ga izostaviti u tiskovnoj izvedenici. |
| 28 | str. 13 | P1 poglavlja 1 nalazi se u teorijskom odjeljku 1.2, a „1.4 Riješeni primjeri” počinje s P2 (str. 17). | Ako je namjerno („kratki primjeri uvode relaciju”), dodati tu napomenu u „Kako koristiti”; inače premjestiti. Sadržajna odluka, ne tipografska. |
| 29 | okviri: 52× „Računalna dinamika fluida”, 40× „Matematički izvod”, 26× „Fizikalno značenje”, 17× „Granica modela”, 15× „Inženjerski kontekst”, 10× „Interaktivni prikaz”, 7× „Numerički pokus” + 13 jednokratnih naslova | Svi okviri imaju isti izgled (lijeva siva crta, naslov 12 pt); razlikuju se samo naslovom. Jednokratni naslovi („Temelj”, „Numerička perspektiva”, „Postupak rješenja”…) razbijaju sustav. | Dvije vizualne obitelji (npr. CFD/Interaktivno s tankom tamnijom crtom ili sitnom ikonom; ostalo kako jest) i svođenje jednokratnih naslova na postojeće vrste. Dojam, ne greška. |
| 30 | str. 7–8 | Pog. „0. Kako koristiti priručnik” nosi broj 0 u naslovu, sadržaju i zaglavlju. | Učiniti ga nenumeriranim („Kako koristiti priručnik”) ako Typst predložak to dopušta bez pomaka numeracije. |
| 31 | str. 1 | Oznaka „PRIRUČNIK” u verzalu bez spacioniranja. | Dodati spacioniranje 0,1 em ili zamijeniti s „Sveučilišni priručnik”. |

## 3. Što je dobro i treba ostati

- Nema prelijevanja: ni jedan tekstualni ni matematički blok ne prelazi desni rub stupca (526 pt) na 335 stranica; nema jednadžbe šire od stupca (provjereno skriptom).
- Oznake u svim tiskovnim skicama su 9–9,5 pt Liberation Sans, bold za vektore; minimum iz `docs/ispis-skica.md` je poštovan (jedine manje vrijednosti su indeksi u matematici, 7,7 i 5,5 pt, što je normalno).
- Vektorski standard (jedna boja #356b83, razlika debljinom i vrhom strelice) doista je proveden u PDF-u: u crtežima PDF-a nema plavih/crvenih/zelenih poteza (#1565c0, #c0392b, #1e8449 postoje samo u web SVG-ovima u `assets/print/`, ne u izvedenicama). To je ključno za crno-bijeli ispis.
- Hijerarhija naslova je čitljiva: poglavlje 22 pt, odjeljak 15 pt, pododjeljak 12,5 pt, naslovi primjera 12,5 pt bold, run-in naslovi 11,2 pt; zaglavlje 9 pt sivo s tankom crtom; folija centrirana.
- Struktura riješenog primjera (Tekst zadatka / Traži se / skica / Veza s proračunom / Rješenje / Provjera i tumačenje) vizualno je prepoznatljiva na svakoj stranici (str. 17, 18, 55, 78, 269).
- Kompozitne skice Z1–Z6 (str. 26, 45, 101, 123, 282) daju dobar pregled i u sivoj skali su čitljive (šrafure stijenki, tamni obrisi).
- Tablice u dodatcima A, B i D (str. 287–288, 296, 309) imaju jasne glave, dovoljno zraka i bez vertikalnih linija; pojmovnik s „Odredište” stupcem je praktičan.
- Sadržaj je potpun i točan (provjereno nasumično: 1.4→17, 5.7→100, 12.6→225, F.16→334).

## 4. Što se može ukloniti ili skratiti bez gubitka

- Numeracija ~750 jednadžbi na koje se nitko ne poziva (ostaviti ~50 referiranih + teorijske).
- Naslov razine „X.1” koji ponavlja naslov poglavlja (14 poglavlja + 6 dodataka) i s njim jedna razina u sadržaju.
- Drugi „O priručniku” (str. 6 ili 7) i razdjelnica „Dodaci” (str. 286) ako ne dobije mini-sadržaj.
- Retci „vizualnih oznaka” u dodatku C (str. 303–306) i rečenica koja ih najavljuje.
- Poveznice „Pokreni u pregledniku / Pričuvno: otvori u Colabu” uz QR kod (jedan redak s URL-om dovoljan).
- Naslovi unutar pojedinačnih skica koji ponavljaju potpis.
- Stavke impresuma „Status: radno izdanje” i „u pripremi” prije predaje.

## Ograničenja ove recenzije

Pregled slika obavljen je na 100 dpi, pa su kolizije oznaka navedene samo tamo gdje su jasne; moguće su
još sitnije na skicama koje nisam otvarao (ukupno 95 potpisanih slika, ručno pregledano ≈ 30).
Hrvatsko rastavljanje riječi i lektorska pitanja nisu ocjenjivani. Sve mjere (razmaci, praznine,
brojevi pojava) dolaze iz PyMuPDF analize i ponovljive su skriptom u `scratchpad/recenzija/pdf/analyze.py`.
