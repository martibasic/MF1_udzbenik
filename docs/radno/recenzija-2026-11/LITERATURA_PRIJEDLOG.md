# Prijedlog dopune literature (dodatak E)

Radna provjera 8. 11. 2026. Ništa u `references.bib` ni u `source/d05_literatura.md`
nije mijenjano. Zapisi su pisani u stilu postojećeg `references.bib`. Svaki podatak
naveden je uz izvor iz kojega je preuzet. Podatci koje nisam potvrdila u izvoru
označeni su **NEPOTVRĐENO**. Provjerila sam kontrolne znamenke ISBN-a. Kad je ISBN-13
izračunan iz ISBN-10, to je posebno navedeno.

Oznake statusa:

- **POTVRĐENO**: autori, naslov, izdanje, izdavač, godina i ISBN ili DOI potvrđeni su u
  barem jednom izdavačkom ili knjižničnom zapisu.
- **DJELOMIČNO**: dio polja (obično mjesto izdanja ili nakladnički otisak) potvrđen je
  samo u knjižarskom zapisu ili uopće nije potvrđen.
- **NEPOTVRĐENO**: polje ili tvrdnja nema pouzdan izvor.

---

## 1. Versteeg i Malalasekera: CFD, metoda konačnih volumena

```bibtex
@book{versteeg2007,
  author    = {Versteeg, Henk K. and Malalasekera, Weeratunge},
  title     = {An Introduction to Computational Fluid Dynamics: The Finite Volume Method},
  edition   = {2},
  publisher = {Pearson Education},
  address   = {Harlow},
  year      = {2007},
  isbn      = {978-0-13-127498-3}
}
```

- **Izvori:**
  - Knjižnični zapis UTB Zlín: <https://vufind.katalog.k.utb.cz/Record/34436>. Navodi
    „2nd ed.”, Harlow, England; New York: Pearson Education, 2007, xii + 503 str.,
    ISBN 9780131274983 / 0131274988, autore H. K. Versteeg (r. 1955) i W. Malalasekera
    (r. 1960).
  - Pearson: <https://pearson.com/en-au/subject-catalog/p/introduction-to-computational-fluid-dynamics-an-the-finite-volume-method/P200000005670/9780131274983>.
    Navodi 2nd edition, datum izdanja 6. 2. 2007. i godinu autorskog prava 2008.
- **Status:** POTVRĐENO za izdanje, izdavača, mjesto, godinu i ISBN.
  - Puna imena „Henk” i „Weeratunge” nisam našla u dohvaćenim zapisima. Zapisi navode
    „H. K.” i „W.” pa su puna imena **NEPOTVRĐENA**. Sigurniji oblik je
    `Versteeg, H. K. and Malalasekera, W.`.
  - Treće izdanje nisam našla ni u jednom izvoru. Drugo izdanje (2007.) zasad je
    najnovije, ali ni to nije potvrđeno izravnim izdavačkim navodom „latest edition”.
  - Knjiga nema DOI.

## 2. Ferziger, Perić i Street: Computational Methods for Fluid Dynamics

```bibtex
@book{ferziger2020,
  author    = {Ferziger, Joel H. and Peri{\'c}, Milovan and Street, Robert L.},
  title     = {Computational Methods for Fluid Dynamics},
  edition   = {4},
  publisher = {Springer},
  address   = {Cham},
  year      = {2020},
  isbn      = {978-3-319-99691-2},
  doi       = {10.1007/978-3-319-99693-6}
}
```

- **Izvori:**
  - Crossref: <https://api.crossref.org/works/10.1007/978-3-319-99693-6>. Navodi
    „Springer International Publishing”, Cham, published-print 2020, ISBN 9783319996912
    (tisak) i 9783319996936 (e-knjiga) te autore Joel H. Ferziger, Milovan Perić i
    Robert L. Street. Crossref nema polje izdanja.
  - Bookshare: <https://www.bookshare.org/browse/book/2906733>. Navodi „4th ed. 2020”,
    Springer International Publishing i godinu autorskog prava 2020.
- **Status:** POTVRĐENO.
  - Napomena: e-knjiga je prema knjižarskim navodima izašla u kolovozu 2019. Kao godina
    izdanja uzeta je 2020., kako je navode Crossref i podatak o autorskom pravu.

## 3. JCGM 100:2008 (GUM)

```bibtex
@standard{jcgm100-2008,
  author       = {{Joint Committee for Guides in Metrology (JCGM)}},
  title        = {JCGM 100:2008 Evaluation of measurement data --- Guide to the expression of uncertainty in measurement},
  organization = {JCGM},
  publisher    = {Bureau International des Poids et Mesures (BIPM)},
  year         = {2008},
  doi          = {10.59161/JCGM100-2008E},
  note         = {GUM 1995 s manjim ispravcima}
}
```

- **Izvori:**
  - BIPM, DOI stranica: <https://www.bipm.org/en/doi/10.59161/jcgm100-2008e>. Navodi
    naslov, oznaku JCGM 100:2008(E), DOI i opis „GUM 1995 with minor corrections”.
  - Crossref: <https://api.crossref.org/works/10.59161/JCGM100-2008E>. Kao izdavača
    navodi Bureau International des Poids et Mesures, godina 2008.
  - BIPM, popis publikacija JCGM: <https://www.bipm.org/en/committees/jc/jcgm/publications>.
- **Status:** POTVRĐENO.
  - Važno: na istom BIPM popisu sada je i **JCGM 100:2008/Amd.1:2026**, „AMENDMENT 1:
    Nonlinearity in measurement models”, kao i „GUMsuite:2026”. Stranica prikazuje DOI
    10.59161/PPDI3267, a poveznica vodi na 10.59161/JCGM100-Amd-2026. Ta su dva DOI-ja
    neusklađena, pa je DOI amandmana **NEPOTVRĐEN**.
  - Stranica ne navodi da je JCGM 100:2008 zamijenjen. Preporuka: citirati JCGM 100:2008
    i u bilješci ili tekstu spomenuti amandman iz 2026. ako se rabi linearizacija
    modela mjerenja.
  - Mjesto izdanja (Sèvres) nije navedeno u dohvaćenim zapisima pa je izostavljeno
    (**NEPOTVRĐENO**).

## 4. Zdravko Virag: Mehanika fluida, odabrana poglavlja

Djelo iz postojećeg zapisa `virag` jest *Mehanika fluida: odabrana poglavlja,
primjeri i zadaci*. Postojeći naslov „Mehanika fluida --- odabrana poglavlja” skraćeni
je oblik toga naslova.

```bibtex
@book{virag2019,
  author    = {Virag, Zdravko},
  title     = {Mehanika fluida: odabrana poglavlja, primjeri i zadaci},
  edition   = {7},
  publisher = {Fakultet strojarstva i brodogradnje, Sveu{\v c}ili{\v s}te u Zagrebu},
  address   = {Zagreb},
  year      = {2019},
  isbn      = {953-6313-39-1}
}
```

- **Izvori:**
  - FSB, Skriptarnica: <https://www.fsb.unizg.hr/index.php?fsbonline=&skriptarnica=>.
    Navodi „Mehanika fluida - Odabrana poglavlja - primjeri i zadaci”; Virag, Zdravko;
    „7. izd.”; 2019; Fakultet strojarstva i brodogradnje; ISBN 953-6313-39-1.
  - Hrvatska tehnička enciklopedija (LZMK): <https://tehnika.lzmk.hr/virag-zdravko/>.
    Navodi djelo „Mehanika fluida. Odabrana poglavlja, primjeri i zadaci” (2002.).
  - Silabus kolegija Mehanika fluida I, Veleučilište u Vukovaru:
    <https://www.vuka.hr/_download/repository/Mehanika%20fluida.pdf>. Citira „Virag, Z.:
    Mehanika fluida-odabrana poglavlja, primjeri i zadaci, Sveučilište u Zagrebu, Zagreb,
    2002.”
- **Status:** DJELOMIČNO.
  - Naslov, autor, nakladnik i 7. izdanje iz 2019. potvrđeni su samo na nakladnikovoj
    prodajnoj stranici. Zapis u katalogu NSK ili WorldCatu nisam uspjela dohvatiti:
    NSK URL vratio je 404, a WorldCat nije dao rezultate.
  - Kontrolna znamenka ISBN-10 953-6313-39-1 ispravna je. Odgovarajući ISBN-13
    978-953-6313-39-6 sama sam izračunala; u izvoru ga nisam našla.
  - **NEPOTVRĐENO:** vrijedi li isti ISBN za sva izdanja te koja izdanja postoje između
    prvog (2002.) i sedmog (2019.).
  - Preporuka: prije unosa provjeriti impresum primjerka koji autorica stvarno koristi.
    Ako je to drugo izdanje, zamijeniti `edition` i `year`. Ključ se može zadržati kao
    `virag` da se ne mijenjaju postojeći citati u izvorima.

## 5. Dixon i Hall: Fluid Mechanics and Thermodynamics of Turbomachinery

Najnovije, 8. izdanje (2025.) potpisuju Dan Zhao, S. Larry Dixon i Cesare Hall. Zhao je
naveden kao prvi autor.

```bibtex
@book{zhao2025,
  author    = {Zhao, Dan and Dixon, S. Larry and Hall, Cesare},
  title     = {Fluid Mechanics and Thermodynamics of Turbomachinery},
  edition   = {8},
  publisher = {Butterworth-Heinemann},
  year      = {2025},
  isbn      = {978-0-443-29831-8}
}
```

Prethodno izdanje, ako se želi citirati „Dixon i Hall” u užem smislu:

```bibtex
@book{dixon2014,
  author    = {Dixon, S. Larry and Hall, Cesare A.},
  title     = {Fluid Mechanics and Thermodynamics of Turbomachinery},
  edition   = {7},
  publisher = {Butterworth-Heinemann},
  address   = {Oxford},
  year      = {2014},
  isbn      = {978-0-12-415954-9}
}
```

- **Izvori:**
  - Elsevier, 8. izdanje: <https://shop.elsevier.com/books/catalog/isbn/9780443298318>.
    Navodi „8th Edition - May 5, 2025”, autore redom Dan Zhao (University of Canterbury),
    S. Larry Dixon (University of Liverpool) i Cesare Hall (University of Cambridge) te
    oznaku „Latest edition”.
  - Open Library: <https://openlibrary.org/isbn/9780443298318.json>. Navodi ISBN-13
    9780443298318, 2025.
  - Knjižarski navodi u pretraživanju: nakladnički otisak Butterworth-Heinemann i ISBN
    e-knjige 9780443298325.
  - 7. izdanje: knjižnični zapis prema pretraživanju (UAM, record SCIDIR_ocn861797371)
    navodi „seventh edition”, Oxford; Amsterdam: Butterworth-Heinemann, 2014, ISBN
    9780124159549. Izravni dohvat tog zapisa nije uspio.
- **Status:**
  - 8. izdanje: DJELOMIČNO. Naslov, autori, izdanje, godina i ISBN su POTVRĐENI.
    Nakladnički otisak Butterworth-Heinemann potvrđen je samo knjižarski, a mjesto izdanja
    je **NEPOTVRĐENO** pa je izostavljeno. DOI knjige nije pronađen (**NEPOTVRĐENO**).
  - 7. izdanje: DJELOMIČNO, jer je potvrđeno samo preko sažetka pretraživanja.

## 6. Carlton: Marine Propellers and Propulsion

```bibtex
@book{carlton2019,
  author    = {Carlton, John S.},
  title     = {Marine Propellers and Propulsion},
  edition   = {4},
  publisher = {Butterworth-Heinemann},
  address   = {Oxford},
  year      = {2019},
  isbn      = {978-0-08-100366-4}
}
```

- **Izvori:**
  - British Library: <https://eld.bl.uk/catalog/019086966>. Navodi Carlton, J. S.
    (John S.), „Fourth edition”, Butterworth-Heinemann, Amsterdam, 2018, ISBN
    9780081003749 (e-knjiga) i povezani ISBN 9780081003664.
  - Elsevier: <https://shop.elsevier.com/books/catalog/isbn/9780081003664>. Navodi
    „4th Edition”, 30. 11. 2018. i oznaku „latest edition”.
  - Crossref, poglavlja knjige (npr. DOI 10.1016/b978-0-08-100366-4.00003-1, „Propeller
    Geometry”): <https://api.crossref.org/works?filter=isbn:9780081003664&rows=3>.
    Izdavač Elsevier, godina 2019, ISBN 9780081003664 (tisak).
- **Status:** DJELOMIČNO.
  - Autor, naslov, 4. izdanje i ISBN su POTVRĐENI.
  - Godina se razlikuje po izvorima: 2018. (BL, Elsevier) i 2019. (Crossref, knjižnica
    ECU prema sažetku pretraživanja „[2019]”).
  - Mjesto se također razlikuje: Amsterdam (BL) te Oxford i Cambridge, MA (ECU, samo
    sažetak). Kako bi se zapis uskladio s Crossrefom, predlažem 2019. i Oxford. Ako
    se slijedi BL, treba upisati 2018. i Amsterdam.
  - Knjiga kao cjelina nema DOI u Crossrefu (pretraga s `type:book` dala je 0 rezultata).
    DOI-je imaju samo poglavlja.
  - Peto izdanje nisam našla.

**Pitanje: podupire li Carlton uobičajeni raspon stupnja djelovanja propelera u slobodnoj
vodi od približno 0,55 do 0,70?**

- **Iz Carltona: NEPOTVRĐENO.** Tekst knjige nisam mogla dohvatiti iz pouzdanog izvora.
  - Elsevierova stranica pokazuje samo sadržaj: poglavlje 6 „Propeller performance
    characteristics”, u 3. izdanju odjeljak 6.1 „General Open Water Characteristics”.
  - Brojčani raspon na njoj nije naveden.
  - Članak koji citira Carltona (2007.) navodi η₀ ≈ 0,55–0,59 za jedan propeler serije
    MAU. To je podatak za jednu seriju, a ne opća tvrdnja knjige.
- **Raspon podupire drugi pouzdan izvor:** MAN Energy Solutions, *Basic principles of
  ship propulsion*, publikacija 5510-0004-04, listopad 2018., str. 22–23 (stranica 12
  u PDF-u):
  <https://www.man-es.com/docs/default-source/document-sync-archive/basic-principles-of-ship-propulsion-eng.pdf?sfvrsn=48fc05b5_7>.
  - Doslovno: „Depending on the propeller loading and design, an efficiency of ηO =
    0.55 - 0.70 is typically attained.”
  - Dokument u popisu literature navodi Carlton, 3. izd., Elsevier 2012. [2.2], ali tu
    rečenicu ne pripisuje izravno Carltonu. Referenca [2.2] u blizini rečenice odnosi se
    na relativni rotacijski stupanj djelovanja i procjenu sustrujanja.
  - Prijedlog zapisa:

```bibtex
@techreport{man-propulsion2018,
  author      = {{MAN Energy Solutions}},
  title       = {Basic Principles of Ship Propulsion},
  institution = {MAN Energy Solutions},
  address     = {Copenhagen},
  number      = {5510-0004-04},
  year        = {2018},
  url         = {https://www.man-es.com/docs/default-source/document-sync-archive/basic-principles-of-ship-propulsion-eng.pdf},
  note        = {Pristupljeno 8. studenoga 2026.}
}
```

  - Mjesto „Copenhagen” preuzeto je s posljednje stranice dokumenta: „MAN Energy
    Solutions 2450 Copenhagen SV, Denmark”.
  - **Preporuka:** tvrdnju o rasponu 0,55–0,70 citirati prema MAN-u, a ne prema
    Carltonu, dok se raspon ne provjeri u tiskanom primjerku Carltona.

## 7. McGeorge i Taylor: brodski strojni sustavi

```bibtex
@book{mcgeorge1995,
  author    = {McGeorge, H. D.},
  title     = {Marine Auxiliary Machinery},
  edition   = {7},
  publisher = {Butterworth-Heinemann},
  address   = {Oxford},
  year      = {1995},
  isbn      = {978-0-7506-4398-6}
}

@book{taylor1996,
  author    = {Taylor, D. A.},
  title     = {Introduction to Marine Engineering},
  edition   = {2},
  publisher = {Butterworth-Heinemann},
  address   = {Oxford},
  year      = {1996},
  isbn      = {978-0-7506-2530-2},
  note      = {Prerađeno drugo izdanje}
}
```

- **Izvori za McGeorge:**
  - Knjižnični zapis UTB Zlín: <https://vufind.katalog.k.utb.cz/Record/kn-ocn162129755>.
    Navodi „7th edition”, Oxford: Butterworth/Heinemann, ©1995, ix + 514 str. te ISBN
    9780750618434 (izvorno tvrdo uvezano izdanje) i 9780750643986.
  - Elsevier: <https://shop.elsevier.com/books/catalog/isbn/9780750643986>. Navodi „7th”
    izdanje, datum 20. 10. 1998. i objavu 19. 1. 1999. te oznaku „Latest edition”.
- **Status za McGeorge:** POTVRĐENO.
  - Sedmo izdanje je najnovije. Izdanje je iz 1995., a ISBN 978-0-7506-4398-6 pripada
    mekoukoričenom otisku iz 1998.
  - Ako se citira taj otisak, u `note` treba dodati „meki uvez 1998.”.
- **Izvori za Taylor:**
  - Knjižnični zapis UTB Zlín: <https://vufind.katalog.k.utb.cz/Record/kn-ocn758471254>.
    Navodi „2nd edition, revised”, Oxford; Boston: Butterworth Heinemann, 1996, ix +
    372 str., ISBN 0750625309 / 9780750625302.
  - Elsevier: <https://shop.elsevier.com/books/catalog/isbn/9780750625302>. Navodi „2nd”,
    9. 10. 1996. i oznaku „Latest edition”.
- **Status za Taylor:** POTVRĐENO. Nijedna knjiga nema DOI.

## 8. ISGOTT: International Safety Guide for Oil Tankers and Terminals

```bibtex
@book{isgott2020,
  author    = {{International Chamber of Shipping} and {Oil Companies International Marine Forum} and {International Association of Ports and Harbors}},
  title     = {International Safety Guide for Oil Tankers and Terminals (ISGOTT)},
  edition   = {6},
  publisher = {Witherby Publishing Group},
  year      = {2020},
  isbn      = {978-1-85609-918-9}
}
```

- **Izvori:**
  - OCIMF: <https://www.ocimf.org/isgott-6>. Navodi „International Safety Guide for Oil
    Tankers and Terminals (ISGOTT 6)”, 6. izdanje, autore IAPH/ICS/OCIMF i godinu 2020.
    Navodi i da ISGOTT 6 zamjenjuje ISGOTT 5 iz 2006.
  - Open Library: <https://openlibrary.org/works/OL24845425W/ISGOTT_6th_Edition>. Navodi
    izdavača Witherby, 1. 7. 2020., ISBN 1856099180 / 9781856099189.
- **Status:** DJELOMIČNO.
  - Naslov, izdanje, autorske organizacije, godina i ISBN su POTVRĐENI.
  - Puni naziv izdavača („Witherby Publishing Group”) i mjesto izdanja su
    **NEPOTVRĐENI**. Mjesto je zato izostavljeno; sigurniji je oblik
    `publisher = {Witherby}`.
  - Sedmo izdanje nisam našla.

**Pitanje: podupire li ISGOTT zahtjev da se u inertiranom teretnom tanku ulaž,
temperatura i granica ulje–voda mjere zatvorenim mjerenjem kroz parnu bravu, a ne
otvorenim sondiranjem?**

Odgovor je **djelomično da, uz terminološku ispravku**. Izvor je OCIMF, *SIRE 2.0
Question Library Part 2*, verzija 1.0 (siječanj 2022.), pitanje 8.3.12, str. 100–101.
Dokument doslovno prenosi tekst ISGOTT-a 6:
<https://safety4sea.com/wp-content/uploads/2022/01/OCIMF-SIRE-2.0-Question-Library-Part-2-2022_01.pdf>.

Potvrđeno doslovnim navodima ISGOTT-a 6 u tom dokumentu:

1. **§12.8.1** razlikuje tri načina mjerenja: zatvoreno (*closed*), otvoreno (*open*) i
   ograničeno (*restricted*).
   - Zatvoreni uređaj je dio sustava koji „maintain[s] the complete integrity of cargo
     containment” i ne ispušta paru „in any amount”. Primjeri su plovak, radar i
     elektronička sonda.
   - Otvoreni način koristi „a gauge hatch or ullage port”.
   - Ograničeni uređaj ispušta male količine pare kroz mali otvor s ventilom „(sometimes
     known as a vapour lock)”.
2. Isti odjeljak: „As a closed gauging system offers complete integrity … its use is
   preferred at all times. Open gauging and restricted gauging should only be allowed
   where: open venting is allowed by the relevant regulations … [and] means are provided
   for relieving tank pressure before the gauge is operated.” Dodaje: „Cargo compartments
   may be pressurised, so only authorised personnel should open vapour lock valves,
   ullage ports or covers”.
3. **§12.8.5** („Closed gauging for custody transfer”): „Temperatures can be taken using
   electronic thermometers inserted through the tank's vapour locks.”
4. **§6.8.5:** „A positive pressure of inert gas should be maintained in the ullage space
   of an inerted cargo tank at all times in order to prevent air from entering.”
5. SIRE uz to traži da prijenosna oprema za ulaž, temperaturu i granicu ulje–voda
   (*ullage/temperature/interface*, UTI) ima certifikat za predviđeni način rada:
   „Portable UTI equipment may be rated for open, restricted or closed service”.

Zaključak i ograničenja:

- **Terminologija:** prema definiciji iz ISGOTT-a 6 (§12.8.1), prijenosni UTI uređaj
  spušten kroz parnu bravu spada u **ograničeno** (*restricted*) mjerenje. Zatvoreno je
  samo mjerenje koje ne ispušta paru, npr. fiksni radarski ili plovni sustav. ISGOTT ipak
  i sam govori o temperaturi kroz parnu bravu u odjeljku naslovljenom „Closed gauging for
  custody transfer” (§12.8.5).
- Prijedlog formulacije za tekst: „u inertiranom tanku pod nadtlakom ulaž, temperatura i
  granica ulje–voda mjere se fiksnim zatvorenim sustavom ili prijenosnim uređajem kroz
  parnu bravu, a ne kroz otvoreni otvor za sondiranje”.
- Izravnu rečenicu ISGOTT-a 6 da se u inertiranim tankovima ulaž, temperatura i granica
  ulje–voda **moraju** mjeriti zatvoreno nisam našla u pouzdanom izvoru. Takva tvrdnja
  ostaje **NEPOTVRĐENA**.
  - Odjeljak „Measuring and sampling inerted tanks” postoji u sadržaju ISGOTT-a 6 prema
    knjižarskim navodima, ali njegov tekst nisam dohvatila.
  - Potvrđeni su samo načelo prednosti zatvorenog mjerenja (§12.8.1), mjerenje
    temperature kroz parnu bravu (§12.8.5) i trajni nadtlak inertnog plina (§6.8.5).
- Starije izdanje (ISGOTT 5) i IMO MSC/Circ.353 prema sažecima pretraživanja govore o
  „portable equipment passed through a vapour lock” za ulaž, temperaturu i granicu
  ulje–voda te o „closed-type ullaging devices to avoid the opening of ullage ports”.
  Te izvore nisam mogla dohvatiti: ISGOTT 5 dostupan je samo kao skenirana neslužbena
  kopija, a stranica NeRF za MSC/Circ.353 vratila je 403. Zato ih ne predlažem kao
  citat (**NEPOTVRĐENO**).

---

## Sažetak

| Br. | Ključ | Status |
|---|---|---|
| 1 | `versteeg2007` | POTVRĐENO (puna imena autora nepotvrđena) |
| 2 | `ferziger2020` | POTVRĐENO |
| 3 | `jcgm100-2008` | POTVRĐENO (napomena o amandmanu iz 2026.) |
| 4 | `virag` / `virag2019` | DJELOMIČNO (potvrđeno samo na nakladnikovoj stranici) |
| 5 | `zhao2025` (8. izd.), `dixon2014` (7. izd.) | DJELOMIČNO |
| 6 | `carlton2019` | DJELOMIČNO; raspon 0,55–0,70 iz Carltona NEPOTVRĐEN, potvrđen u MAN ES 2018 |
| 7 | `mcgeorge1995`, `taylor1996` | POTVRĐENO |
| 8 | `isgott2020` | DJELOMIČNO; tvrdnja djelomično poduprta, uz terminološku ispravku (*restricted*) |

Ova datoteka sadrži samo provjeru izvora. O uvrštenju i tekstu dodatka E odlučuje
autorica.
