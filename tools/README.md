# `tools/` — pomoćne skripte

Arhitektura i izvođenje svih prikaza opisani su u
[vodiču](../docs/arhitektura.md). Prije provjera nakon uređivanja pokreni
`python scripts/build_book.py --write`.

| Provjera arhitekture | Namjena |
| --- | --- |
| `test_book_model.py` | Premještanje poglavlja i objekata, očuvanje ID-jeva i formula, odbijanje neispravnih referencija, fizička širina figure iz PDF margine. |
| `test_render_workspace.py` | Izolacija Quarto predmemorije, očuvanje izlaza nakon neuspjelog rendera ili izmjene izvora, zaključavanje između procesa. |
| `test_render_process.py` | Stvarni procesi: trajni log, izlaz bez završnog novog retka, propagacija pogreške i prekid cijelog stabla pri zastoju. |
| `test_component_visibility.py` | Stvarni HTML/Typst adapteri: promjena samo registra uključuje/skriva stare i nove komponente te povezane naslove za web/PDF/print. |
| `audit_architecture.py` | Jedna hijerarhija, aktualne izvedenice, semantičke komponente, razine i slojevi stilova. |
| `audit_rendered_model.py _site` | Stvarni brojevi sekcija, jednadžbi, captiona i P/Z objekata u webu i zbirnom ispisu. |

Skripte za numeričku verifikaciju sadržaja i za obradu SVG skica u `assets/print/`.
Sve se pokreću iz korijena projekta, npr. `python tools/verify_all.py`.
Numerička verifikacija i SVG alati koriste standardnu biblioteku Pythona i
lokalne datoteke; ne trebaju `numpy`/`sympy`. Audit konačnog PDF-a koristi
pinani `PyMuPDF` iz korijenskog `requirements.txt`.

## Puni objavni CI i zaštita pusha

`python scripts/check_publication.py` jedini je popis koraka za GitHub Action,
lokalnu izgradnju i `.githooks/pre-push`. Hook se uključuje jednom po klonu:
`python scripts/install_hooks.py`. Prije svakog pusha zahtijeva čist HEAD i
novi puni prolaz; provjerava i stanje nakon testiranja.
`python tools/test_pre_push.py` provjerava stvarnu blokadu Gitova pusha prema
privremenom lokalnom repozitoriju. Priprema alata i ograničenja opisani su u
[lokalnom CI-ju](../docs/lokalni-ci.md).

## Numerička verifikacija (trajno — koristi CI)

| Skripta | Namjena |
|---|---|
| `verify_all.py` | Runner za 19 numeričkih modula: regresijski niz U01–U14 i pet zasebnih kanonskih verifiera. Pokreće brojčane provjere, strukturni audit, manifest pokrivenosti i neovisne fizikalne golden provjere. Izlazni kod 1 vraća za brojčani FAIL, nestali modul/ID, tautologiju, rupu ili neusklađen manifest. |
| `verify_u01.py` … `verify_u07.py` | Neovisno ponovno računaju sve objavljene rezultate svih 42 zadatka za vježbu i dodaju bilančne, predznakovne ili granične invarijante. U tim modulima više nema self-comparison provjera. |
| `verify_u08.py` … `verify_u13.py` | Regresijski računski moduli s neovisnim golden ciljevima za svih 36 zadataka; uklonjeni primjeri i zadatci više se ne pozivaju kao pokrivenost. |
| `verify_u14.py` | Verifier aktualnog U11: šest zadataka s neovisnim golden rezultatima, prijenos otpora hidroprofila, dva Froudeova modela s intervalima sila te stvarni račun ranga i eksponenata Buckinghamovih grupa u Z5. Stari Z7 nije dio pokrivenosti. |
| `verify_u05_integrated.py`, `verify_u13_integrated.py` | Kanonski verifieri integriranih poglavlja U05 i U13. Neovisno ponovno računaju objavljene brojeve svih šest primjera i šest zadataka, uključujući predznake sila, nesigurnost, radnu točku, energetski ledger i NPSH. |
| `verify_u09_compressible.py`, `verify_u12_real_flow.py`, `verify_u15_open_channels.py` | Kanonski verifieri novih poglavlja. Svih 18 pripadajućih zadataka ima potpune brojčane ulaze, objavljene rezultate i golden ciljeve; dodatne invarijante provjeravaju bilance, predznake, konvergenciju, nesigurnost i granice modela. |
| `verification_manifest.json` | Jedini manifest sheme v2. Uz inventar 19 izvršnih modula sadrži 90 javnih task ID-jeva: razinu, autoritativni tekst i provenijencu, konzervativno parsirane ulaze i SI pretvorbe, eksplicitne/default pretpostavke, objavljeni rezultat ili kriterij, toleranciju, neovisni ugovor te verifier/result-ID veze. Release manifest ne dopušta `gap`. |
| `generate_verification_manifest.py` | Deterministički generira kanonski dio manifesta iz 15 javnih izvora i AST-a verifiera. Bez `--write` strogo provjerava zastarjelost; s `--write` osvježava generirana polja. Otvoreni zadatci ostaju invarijantni i ne dobivaju izmišljene brojeve. |
| `qa_audit.py` | AST provjera koja pronalazi `_check(..., x, x)`, potvrđuje točno šest aktualnih task anchora po modulu, strogo validira svih 90 zapisa sheme v2, ponovno ih generira u memoriji te povezuje deklarirane result-ID-jeve sa stvarnim izvršenjem. |
| `audit_publication.py` | Provjerava novu kanonsku strukturu U01–U15: 5–7 riješenih primjera i šest zadataka ciljane raspodjele po poglavlju, stabilne i jedinstvene ID-jeve, slike i SVG pristupačnost, citate te javne JupyterLite poveznice. |
| `audit_typst.py` | Provjerava da PDF profil uključuje nativnu Typst komponentu i Lua mapiranje svih standardnih autorskih blokova, da su dugi blokovi označeni kao prelomivi te da komponentu ne skriva `.gitignore`. |
| `audit_pdf.py` | Provjerava stvarni nativni PDF: A4, regresijski raspon 270–335 stranica, metapodatke, kazalo, U01–U15 i slijed oznaka slika. Obrazloženje prijeloma: `docs/pdf-tipografija.md`. |
| `audit_pdf_layout.py` | Na stvarnom PDF-u uspoređuje svih 17 rasterskih QR uzoraka s izvornim modulima i provjerava obje poveznice, razmak i potpunu numeraciju jednadžbi, P/Z naslove po poglavljima i ključ, 18 zapisa literature u E.7, opise slika/QR blokova, najmanje 9 pt za oznake skica, zajedničku osnovicu broja i naslova, osamljene naslove i granice tekstnog stupca. Dopunjuje, ne zamjenjuje vizualni pregled svih stranica. |
| `build_print_figures.mjs` | Iz kanonskih SVG-ova generira tiskovne izvedenice MINI/STANDARD/WIDE/COMPOSITE, zasebno slaže geometriju i oznake od 9–9,5 pt. Zajednički tokeni su u `assets/figure-tokens.json`; upute i iznimke opisane su u `docs/ispis-skica.md`. |
| `audit_print_layouts.mjs` | Provjerava pokrivenost svih 94 izvora i 3363 tekstna elementa te poziva `audit_print_figures.mjs`: hashovi ulaza i izvedenica, svih 3338 nepraznih oznaka i indeksa, koordinate zadržane geometrije, font najmanje 9 pt, preklapanja i clipping. Potreban je Chrome/Chromium/Edge i `npm ci`. |
| `audit_print_site.mjs` | Provjerava da se mrežne skice nisu zamijenile na zaslonu, a ispis prikazuje sve učitane tiskovne retke u zadanim fizičkim veličinama, bez skaliranja fonta i izlaska iz stranice. |
| `audit_viewports.mjs` | Pregledava 24 HTML stranice na 320, 768 i 1440 px; provjerava prelijevanje sadržaja, WCAG, vidljivost i rad tipkovničkog fokusa, lokalno pomicanje tablica, povećanje skica i odredišta brzih poveznica poglavlja. Provjerava i A4 ispis te učitavanje notebooka i spremnost Python kernela (Idle) u JupyterLiteu. Pokreni nakon rendera i izgradnje JupyterLitea: `npm run audit:viewports -- _site`. |
| `verify_physics.py` | Neovisni golden testovi temeljnih bilanci i kritičnih pretvorbi: Pascal, hidrostatika, kontinuitet, gubici, paralelne grane, smjer sile na simetričnom koljenu, Wh→s, dvofluidni uzgon i Froudeovo skaliranje. |
| `execute_notebooks.py` | Validira i izvršava svih 17 obveznih notebooka u čistim kernelima bez prepisivanja izvora. `--validate-only` radi samo strukturnu i sintaksnu provjeru. |
| `test_interactive_labs.py` | Neovisno provjerava tri ogledna laboratorija: granice rotacije, Venturijev referentni protok i nesigurnost, konvergenciju rješavača konačnih volumena, bilancu sila, kontrolne ulaze, usporedbu i resetiranje. Čuva granicu ovisnosti i jednakost zajedničke ćelije samostalnih bilježnica. |
| `audit_interactive_labs.mjs _site` | U stvarnom JupyterLiteu izvršava tri bilježnice, mijenja kontrole tipkovnicom i provjerava fizikalni odgovor, usporedbu, resetiranje, dijagnostiku, izvorni kod te raspored na 320/768/1280 px. Za razliku od provjere spremnosti kernela, ispituje stvarne callbackove. |
| `audit_sketch_design.py` | Objava provjerava svih 94 referenciranih SVG-ova: paletu, jednolične ispune, font, vrhove strelica, zatvorene kontrolne granice i crte čitljive bez boje; zatim izvršava sve neovisne geometrijske verifikatore. Vizualna i didaktička procjena ostaju zasebne. |
| `check_u01_sketch_geometry.py` | Čita sedam SVG-ova U01: provjerava povezane tekuće komore i otvorene priključke, klipove i klipnjače, smjerove sila, stvarne omjere promjera, kote iste početne/konačne plohe, krakove poluge 5:1 i dva punjenja posude. Dopunjuje vizualni pregled. |
| `check_u02_sketch_geometry.py` | Čita sedam SVG-ova U02: provjerava otvorene uronjene ulaze, povezane fluidne domene, kružne meniskuse i kutove od 18°, tangente površinskih sila, prianjanje, smjerove otpora, promjere, kote uspona i omjere procjepa. Dopunjuje vizualni pregled. |
| `check_u05_sketch_geometry.py` | Dodatna ručna provjera nakon izmjena skica U05: čita stvarne SVG putanje, provjerava četvrtkružne lukove, lokalne normale i krakove komponenti sile. Pokreće se zasebno; vizualni pregled ostaje potreban. |
| `check_u06_sketch_geometry.py` | Zasebno provjerava krute pravokutne trupove, vodoravne površine, centre uzgona neovisnom integracijom stvarnih SVG poligona, puni tank i razmak kućišta od dna. Dopunjuje vizualni pregled U06. |
| `check_u07_sketch_geometry.py` | Zasebno provjerava normalu kose plohe, tangente strujnice, stvarni otvor klipa, otvorene priključke i omjere kota/promjera u SVG skicama U07. Dopunjuje vizualni pregled. |
| `check_u08_sketch_geometry.py` | Zasebno provjerava stvarne SVG kote visina i promjera, otvorene sifone i mjerne priključke, balističke parabole, sučelja manometra te skalu EGL/HGL-a. Dopunjuje vizualni pregled U08. |
| `check_u09_sketch_geometry.py` | Zasebno provjerava otvorene presjeke i oblik sapnica, kotu akustičke mjerne duljine, smjerove signala, normalni val te stvarne otvore statičkih i Pitotovih priključaka. Dopunjuje vizualni pregled U09. |
| `check_u10_sketch_geometry.py` | Zasebno provjerava osam SVG-ova U10: otvorene prirubnice i račve, stijenke na rubu fluida, promjere kroz zavoje, normalne presjeke, krak momenta te smjerove tlaka, reakcije i apsolutne izlazne brzine pomične ploče. Dopunjuje vizualni pregled. |
| `check_u11_sketch_geometry.py` | Čita devet izmijenjenih SVG-ova U11: provjerava otvorene vodove i tlačni priključak, parabolični profil ulja, sličnost trupova i hidroprofila, kote kapi/cilindara, kontinuitet modelskih presjeka te stvarne krivulje tlaka i koeficijenta otpora s granicama prikazanih modela. Dopunjuje vizualni pregled. |
| `check_u12_sketch_geometry.py` | Provjerava dvije slike U12: x-komponente naprezanja, rast debljine sloja, srednju vrijednost nacrtanog signala, kinematičke vektore, nepropusne ploče, otvorene kapilarne priključke, kote i pročišćenje iste mrežne domene. Dopunjuje vizualni pregled. |
| `check_u13_sketch_geometry.py` | Provjerava tri slike U13: povezane grane i otvorene priključke, suhe i omočene stijenke spremnika, uronjen usis, unutarnje promjere i kote, parabolični profil, kružno koljeno stalne širine, EGL/HGL te stvarne krivulje crpke i sustava uz Colebrookovu jednadžbu. Dopunjuje vizualni pregled. |
| `check_u14_sketch_geometry.py` | Čita sedam SVG-ova U14 s naslijeđenim prefiksom u12: otvorene sapnice i vodilice, ploče i krak rotora izvan fluida, poprečne kote i kutove, stvarne trokute brzina, radijus i smjer vrtnje, reakcije te kontinuitet kružnih vodomlaznih vodova i četiriju mlazova. Dopunjuje vizualni pregled. |
| `check_u15_sketch_geometry.py` | Provjerava dva SVG-a U15: stvarne trapezne površine i opsege, kote i pokose, brzine valova prema obali, krivulju energije, kritičnost i podkritičnu granu na pragu, neprekinuto dno, hidrostatičke sile i bilance rubnih presjeka skoka te granicu dubine bazena. Dopunjuje vizualni pregled. |
| `validate_cfd_vv.py` | Read-only validator za `data/cfd/`: dva sintetička nastavna slučaja provjerava prema analitičkim modelima, bilancama i GCI-ju. Za javni NACA referentni skup uspoređuje sve kopirane brojeve s arhiviranim NASA tablicama, razlikuje točke od ćelija te čuva razliku između djelomičnih objavljenih dokaza i nedostajuće pune validacije. |

### Kako čitati rezultat

Ne koristi se više zbirna tvrdnja poput „498/498 PASS”, jer je skrivala razliku
između stvarne usporedbe i poziva koji rezultat uspoređuje sa samim sobom.
Aktualni audit zabilježio je:

- 1.001 sirov rezultat svih 19 modula;
- 924 usporedbe s neovisnom deklariranom ciljanom vrijednošću;
- 77 zasebno označenih dimenzijskih, bilančnih, predznakovnih, graničnih ili kvalitativnih invarijanti;
- 22 dodatna neovisna fizikalna golden testa;
- 0 self-comparison rezultata i 0 AST tautologija;
- 0 rupa na razini zadataka, 0 nepokrivenih modernih brojčanih primjera i 0 kanonskih poglavlja bez verifiera.

Manifest sheme v2 sadrži 90/90 zadataka u skupini `golden`, 393 parsirana
skalarna ulaza i 312 ugovora rezultata. Svi su ranije otvoreni T3/T4 zadatci u
novim poglavljima sada potpuno zadani; invarijante ostaju kao dodatna provjera
fizike, a ne kao zamjena za nedostajući brojčani ugovor.

Ti su brojevi početna snimka, ne obećanje trajnog fiksnog zbroja. Kanonski je
strojno čitljiv manifest, a aktualni izvještaj daje:

```
python tools/verify_all.py
```

Svaka rupa ili zastarjeli generirani zapis ruši CI. Nakon promjene teksta,
kontrolnog rezultata, task anchora ili verifiera pokreće se:

```
python tools/generate_verification_manifest.py --write
python tools/verify_all.py
```

Parser je namjerno ograničen. Autoritativan je puni Markdown teksta zadatka;
strukturiraju se samo nedvosmisleni skalarni brojevi iz inline matematike, a SI
pretvorba radi samo preko bijele liste. Simboličke krivulje, nizovi, intervali,
brojevi u prozi i nepotpuni T3/T4 podatci ostaju u tekstu i u polju
`unparsed_numeric_math`. Pretpostavke se ne zaključuju iz stručnog znanja nego
se prenose samo iz teksta zadatka, naputka ili uvoda liste uz provenijencu.

Hard-coded cilj verifiera i objavljeni kontrolni rezultat čuvaju se usporedno,
ali semantičko pridruživanje svakoga broja iz slobodno pisanoga Markdowna
pojedinom rezultatu nije automatsko. Zato promjena brojčanoga odgovora i dalje
zahtijeva autorski pregled teksta i fiksnoga cilja; generator osigurava da se
promjena vidi i da nijedan task/result-ID ne nestane tiho.

Za višedijelni kontrolni rezultat čije bi skraćivanje izostavilo odluku ili
ograničenje može se uz `data-answer-key="true"` dodati `data-key-full="true"`.
Generator `scripts/generate_exercise_key.py` tada prenosi cijeli odgovor
u D06. Ostali odgovori zadržavaju postojeće sažimanje; potpunost generiranog
ključa treba pregledati nakon svake sadržajne izmjene.

## SVG obrada i QA (trajno)

| Skripta | Namjena |
|---|---|
| `svg_normalize.py` | Strukturni normalizator: prefiksira `id`-eve po datoteci, postavlja kanonski font, `aria`/`role` atribute i root atribute. Jednokratno proveden nad svih 143 SVG-ova u `assets/print/`; ponovno primjenjiv na nove skice. |
| `strip_svg_titles.py` | Uklanja vidljive top-level naslove iz SVG-ova (naslov pokriva Markdown caption). |
| `fix_svg_xml.py`, `fix_svg_ns.py` | Popravci XML konformanse i namespacea SVG datoteka. |
| `detect_box_geometry_overlap.py`, `scan_label_format.py` | Dijagnostika: preklapanje teksta i geometrije, format oznaka (bez izmjena — samo izvještaj). |
| `preview_server.py` | Lagani lokalni server koji poslužuje projekt i generira indeks svih SVG-ova po poglavlju za brzi vizualni pregled. |

## Jednokratni migracijski/popravni skriptovi (arhiva)

Korišteni u prošlim fazama; zadržani radi ponovljivosti, ne pokreću se rutinski:
`replace_matplotlib_blocks.py` (matplotlib→SVG konverzija), `fix_u01_skice.py`
(sistemski popravci U01 skica), te per-detalj popravci
`bring_dims_to_front.py`, `bring_text_to_front.py`, `fix_dim_arrow_refx.py`,
`fix_kv_fill.py`, `fix_label_single_line.py`, `fix_text_overflow.py`,
`remove_white_panels.py`, `undo_label_y_move.py`.

Logovi jednokratnih prolaza: `svg_normalize.log`, `strip_svg_titles.log`.
Privremeni radni izlazi idu u `tools/tmp/` (git-ignorirano).

Aktualne bilježnice uređuju se izravno u `notebooks/`; ne obnavljaju se iz
starih predložaka. `scripts/generiraj_notebooke.py` služi samo arhivskoj
usporedbi i zahtijeva `--archive-output` s novom mapom izvan repozitorija ili
unutar `tools/tmp/`. Odbija zapisivanje u izvore i postojeća odredišta.
Zaštitu provjerava `python tools/test_legacy_notebook_generator.py`.

Aktualni QR generator je `scripts/generate_qr_assets.py`: bez argumenata
provjerava izlaze, a s `--write` ih obnavlja. `scripts/generiraj_qr.py`
prosljeđuje poziv istom generatoru radi kompatibilnosti. Postupak uređivanja
opisan je u [uputama za bilježnice](../notebooks/README.md).
