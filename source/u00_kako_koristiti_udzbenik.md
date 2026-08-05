## Dobrodošli u Mehaniku fluida 1

Udžbenik prati studenta kroz petnaest poglavlja. Kurikularna matrica predviđa približno **145 sati rada uz udžbenik** — čitanja, izvođenja, riješenih primjera, samostalnih zadataka i numeričkih pokusa. To nije isto što i cjelokupno ECTS opterećenje kolegija, koje uključuje nastavu, laboratorij, pripremu provjera i ispit. Teorija, riješeni primjeri i samostalni zadatci čitaju se kao **jedan radni tok**, a ne kao tri odvojene cjeline.

::: {.mf1-application}
<p class="mf1-box-label">Predznanje koje se pretpostavlja</p>

- diferencijalni i integralni račun (Matematika I i II);
- vektorska analiza i osnove diferencijalnih jednadžbi;
- mehanika, rad i energija (Fizika I).

Ako pojedina matematička tehnika u nekom izvodu nije do kraja poznata, dovoljno je pratiti fizikalni smisao koraka; potpuna ovladanost tehnikom postiže se kasnije, paralelno s vježbanjem.
:::

## Što očekivati od svakog poglavlja

Svako poglavlje slijedi isti unutarnji raspored:

1. **Inženjerski kontekst** — kratak okvir koji povezuje temu sa stvarnim sustavima u praksi.
2. **Fizikalni uvod i matematički izvod** — postupno uvođenje središnjih jednadžbi uz prateća tumačenja u okvirima *Fizikalno značenje*.
3. **Riješeni primjeri** — pet do sedam odabranih primjera, označenih razinom odluke T1 do T4.
4. **Zadaci za vježbu** — šest zadataka za samostalan rad: dva T1, dva T2, jedan T3 i jedan T4; pomoć se smanjuje kako raste razina.
5. **Završni okvir** *Za ponijeti iz poglavlja* — sažeta provjera, najčešća pogreška, granica modela i prijenos prema sljedećem poglavlju.
6. **Numerički pokus** — obrazac *predvidi → izračunaj → provjeri* koji uvodi integraciju, iteraciju, nesigurnost ili konvergenciju samo kada ona donosi novu fizikalnu spoznaju.

Svako poglavlje ima pripadni **Jupyter notebook** koji se može pokrenuti bez prijave u JupyterLiteu ili, kao pričuvni put, u Google Colabu. Notebook mora sadržavati izvršivu provjeru rezultata i pitanja interpretacije; klizač zatvorene formule sam po sebi nije numerički laboratorij.

## Tipovi primjera i zadataka

Primjeri i zadaci razlikuju se prema razini vođenja koju nude:

::: {.mf1-checklist}
<p class="mf1-box-label">Kako birati tip zadatka</p>

- **Riješeni primjer** — usvaja se prvi put novi model ili radni ritual; cijeli je postupak raspisan korak po korak. Kraći uvodni slučajevi nose oznaku *Kratki primjer*.
- **Cjeloviti zadatak** — integracija više ideja iz poglavlja ili priprema za teži ispitni zadatak; postupak je i dalje vođen, ali traži samostalne odluke o modelu, geometriji i predznaku.
- **Zadaci za vježbu** — niz numeriranih zadataka za samostalan rad na kraju poglavlja; svaki nosi razinu težine, natuknicu i zahtjev za skicu.
:::

## Razine težine

Svaki zadatak nosi oznaku razine težine:

- **T1** — primjena jednoga već odabranog zakona, bez modelske odluke.
- **T2** — jedan dominantni model uz geometrijsku, jediničnu ili manju modelsku odluku.
- **T3** — izbor ili kombiniranje modela uz obrazloženje pretpostavki i granica.
- **T4** — nepotpuni ili šumni podaci, nesigurnost, kompromis, optimiranje ili obranjena inženjerska odluka.

Studentu se preporučuje da prvih nekoliko zadataka u svakom poglavlju rješava redoslijedom po rastućoj težini, a tek nakon stabilnog T1 i T2 prelazi na T3 i eventualne T4 zadatke.

## Mrežno i tiskano izdanje

Isti izvor sadržaja generira **mrežno izdanje**, **nativni Quarto/Typst PDF** i JupyterLite. Pregled za ispis iz preglednika ostaje pomoćna inačica, a ne primarni PDF proizvod. QR kodovi i javne poveznice provjeravaju se kao dio izgradnje.

::: {.mf1-warning}
<p class="mf1-box-label">Pravilo čitanja</p>

Kanonski tekst svakog poglavlja razumljiv je i bez interaktivnih elemenata. Interaktivni prikazi nadopunjuju, a ne zamjenjuju, izvod i primjere u tekstu.
:::

## Dodaci

Šest dodataka strukturno nadopunjuje glavna poglavlja:

- <span class="mf1-ch-ref"><span class="mf1-ch-code">dod. A</span><span class="mf1-ch-title">Sažetak formula i oznaka</span></span> — komprimirani pregled formula, oznaka i uvjeta primjene; služi za brzo podsjećanje prije računa.
- <span class="mf1-ch-ref"><span class="mf1-ch-code">dod. B</span><span class="mf1-ch-title">Pojmovnik</span></span> — radne definicije temeljnih pojmova; služi za razdvajanje pojmova koji se često miješaju.
- <span class="mf1-ch-ref"><span class="mf1-ch-code">dod. C</span><span class="mf1-ch-title">Tipične pogreške po poglavljima</span></span> — sustavni katalog načina na koje zadatak zalazi krivim putem; služi kao preventivni filtar prije računa i prije predaje zadatka.
- <span class="mf1-ch-ref"><span class="mf1-ch-code">dod. D</span><span class="mf1-ch-title">Numerička mehanika fluida (pregled)</span></span> — pregledni dokument koji sažima sve oznake *Numerički most* kroz udžbenik i postavlja ih u jednu cjelinu kao najavu kolegija Računalna dinamika fluida.
- <span class="mf1-ch-ref"><span class="mf1-ch-code">dod. E</span><span class="mf1-ch-title">Literatura i izvori</span></span> — primarni izvori, norme i preporučeni udžbenici povezani s konkretnim tvrdnjama u tekstu.
- <span class="mf1-ch-ref"><span class="mf1-ch-code">dod. F</span><span class="mf1-ch-title">Ključ kontrolnih rezultata</span></span> — u tisku odvaja rezultate od teksta zadatka, a otvorene zadatke veže uz kriterije vrednovanja i stabilne ID-jeve.

## Preporučeni redoslijed rada

1. Započni fizičkim pitanjem i nacrtaj **sustav ili kontrolni volumen**.
2. Odredi osi, pozitivne smjerove, referencu tlaka i granicu sustava.
3. Napiši pretpostavke prije jednadžbe i provjeri vrijedi li model.
4. Izvedi ili odaberi bilancu, tek zatim uvrsti podatke.
5. Provedi najmanje jednu neovisnu provjeru: jedinice, predznak, bilancu, granični slučaj ili red veličine.
6. Na kraju zapiši što bi u stvarnom sustavu moglo srušiti zaključak te, kada je predviđeno, usporedi s numeričkim pokusom.

::: {.mf1-mini-summary}
<p class="mf1-box-label">Sažetak za ponijeti</p>

Udžbenik je zamišljen kao jedan radni tok: **izmjeri → idealiziraj → izračunaj → numerički provjeri → procijeni valjanost**. Interaktivni prikazi nadopunjuju, ali ne zamjenjuju, fizičku sliku, izvod i provjeru modela.
:::
