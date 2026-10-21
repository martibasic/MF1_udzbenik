## O priručniku {#o-udžbeniku}

Sveučilišni priručnik namijenjen je studentima druge godine strojarstva i brodogradnje. Povezuje fizikalno objašnjenje, matematički izvod i rješavanje zadataka: u petnaest poglavlja upoznat ćeš svojstva fluida, hidrostatiku te strujanje u cijevima, turbostrojevima i otvorenim kanalima.

Primjene u brodogradnji obuhvaćaju hidrostatička opterećenja, uzgon i početni stabilitet, sličnost pri modelskim ispitivanjima te propulziju. Primjeri iz građevinarstva, energetike, zaštite okoliša, biomedicine i procesne tehnike uključeni su kad prenose isti model i pomažu prepoznati njegovu opću strukturu.

Rješavanje tehničkog zadatka počinje skicom sustava i popisom pretpostavki; zatim slijede odgovarajuća bilanca, proračun i provjera rezultata. Pri prvom čitanju drži se glavnog teksta, riješenih primjera i zadataka. Blokovi *Dublje* i odlomci *Računalna dinamika fluida* dodatno su štivo: osnovno gradivo priručnika možeš pratiti i bez učenja CFD postupaka.

## Predznanje

Potrebne su osnove mehanike, rada i energije te računanje s jedinicama i vektorima. Diferencijalni i integralni račun primjenjuju se u izvodima, a vektorska analiza osobito je važna za diferencijalni opis toka. Ako preskačeš poglavlja, provjeri poznaješ li veličine i bilance na koje se novo gradivo poziva.

Procijenjeno vrijeme navedeno uz poglavlja pomaže ti planirati samostalan rad. Ukupno je predviđeno približno **145 sati rada uz priručnik**, uključujući zadatke i numeričke pokuse; to nije cjelokupno ECTS opterećenje kolegija.

## Struktura rada s poglavljem

1. Uvod određuje fizikalno pitanje i opseg modela poglavlja.
2. Izvodi povezuju skicu, pretpostavke i značenje pojedinih članova jednadžbe.
3. Riješeni primjeri, smješteni uz teoriju ili u zasebnom odjeljku, pokazuju kako se postavlja početna jednadžba i kojim slijedom teče proračun.
4. Zadatci za vježbu razvrstani su po razini samostalnog izbora modela. Smjernice i kontrolni rezultati nalaze se u dodatku F; mrežno izdanje ih prikazuje i uz sam zadatak.
5. Sažetak na kraju poglavlja, iza zadataka, okuplja osnovne modele i granice njihove primjene, najčešću pogrešku i ono što nakon poglavlja mora biti moguće.

Uz pitanje **Zastani i promisli** najprije oblikuj vlastiti odgovor, a zatim ga usporedi s objašnjenjem koje slijedi. Takvo pitanje provjerava razumiješ li izbor modela i značenje rezultata prije nego što kreneš u novi račun.

Okviri *Fizikalno značenje* tumače rezultat, dok okvir *Granica modela* objašnjava kada odabrane pretpostavke prestaju vrijediti.

::: {.mf1-cfd title="Računalna dinamika fluida"}

**Kako čitati CFD primjere.** Polazište je konkretno pitanje: dobivaju li svi rashladni kanali dovoljno tekućine, koliki val nastaje pri kočenju cisterne ili kako ustava mijenja razinu vode? Odlomak povezuje to pitanje s modelom, podatcima koje zadajemo i veličinama koje dobivamo iz računa. Uz rezultat pratimo provjeru i odluku koju on omogućuje.

Neki se sustavi u knjizi pojavljuju više puta. Rashladnom krugu postupno dodajemo viskoznost, podjelu protoka, gubitke i crpku; plutanje pontona proširujemo na njihanje, a opterećenje ustave na tok nizvodno. Takvi primjeri pokazuju zašto novo pitanje traži dodatnu fiziku. Pregled poveznica i cjelovit postupak daje [dodatak o numeričkoj mehanici fluida](d04_numericka_mehanika_fluida.qmd).
:::

## Oznake i razine zadataka

Riješeni primjeri označeni su **P1, P2, … zasebno u svakom poglavlju**. Oznaka stoji lijevo od naslova. Koraci rješenja numerirani su redom 1., 2., 3., bez dodatne numeracije odjeljka.

Zadatci za vježbu označeni su **Z1–Z6 zasebno u svakom poglavlju**, uz kratak naslov problema. Ključ rezultata u dodatku F koristi iste oznake i naslove. Upućivanje na zadatak uključuje i oznaku poglavlja, primjerice „poglavlje 3, Z2”.

Razine T1–T4, navedene sitnim slovima na kraju zadatka, pokazuju koliko samostalnog izbora zadatak traži, a ne samo koliko je račun dug.

| Razina | Što zadatak traži |
| --- | --- |
| **T1** | Primjenu već odabranog zakona. |
| **T2** | Izbor geometrije, pretvorbu jedinica ili manju odluku o modelu. |
| **T3** | Izbor ili povezivanje modela uz obrazloženje pretpostavki. |
| **T4** | Procjenu nesigurnosti, rad s nepotpunim podatcima ili obrazloženu inženjersku odluku. |

U svakom je poglavlju šest zadataka, od T1 do T4. Zadatci nižih razina oslanjaju se na izravnu primjenu modela, dok T3 i T4 zahtijevaju obrazloženje odabranoga postupka, pretpostavki i zaključka.

## Strelice na skicama

Svi vektori na skicama imaju istu boju, a vrstu veličine pokazuju debljina crte, vrh strelice i crtkanje. Isti stil vrijedi u cijelom priručniku.

| Prikaz | Veličina |
| --- | --- |
| deblja puna crta, pun trokutasti vrh | sila, težina $F_G$, uzgon $F_U$, reakcija, tlačna sila $pA$; zakrivljena: moment |
| tanja puna crta, otvoren vrh | brzina, smjer protoka, pomak (hod); zakrivljena: kutna brzina $\omega$ |
| isprekidana crta, pun vrh | ubrzanje i efektivno polje ($\vec a$, $\vec g$, $\vec g_{eff}$) |
| tanka crta, mali pun vrh | raspodijeljeni tlak na stijenci; jedinična normala $\vec n$ |
| siva tanka crta s vrhovima na oba kraja | kota (duljina, visina, promjer) |

Oznake vektora uz strelice pisane su podebljano, a oznake skalara (kote, tlakovi, gustoće) obično. Uz svaku silu naznačeno je tijelo na koje djeluje. Duljine strelica iste vrste unutar jedne skice razmjerne su iznosima; kad stvarni omjer ne bi bio čitljiv, zadržan je poredak iznosa, a tekst uz skicu to navodi.

## Numerički pokusi i izdanja

Numerički pokusi istražuju osjetljivost, bilance i pogrešku jednostavnih modela i nisu sami po sebi CFD simulacije. Bilježnice (*Jupyter notebooks*) otvaraju se preko poveznica ili QR kodova u JupyterLiteu, bez prijave; pričuvna je mogućnost Google Colab. Prvo pokretanje traži mrežnu vezu i može potrajati minutu ili dvije. Blok *Interaktivni prikaz* otvara laboratorij s klizačima, a blok *Numerički pokus* bilježnicu u kojoj se model provjerava računom.

**Za čitanje i rješavanje zadataka dovoljan je tekst priručnika.** Mrežno izdanje i PDF sadrže isto gradivo, a bilježnice ga nadopunjuju. Izdanje u PDF-u namijenjeno je ispisu i radu bez mrežne veze.

## Dodaci za brzo snalaženje

- **A — Sažetak formula i oznaka:** podsjetnik na relacije, jedinice i uvjete primjene.
- **B — Pojmovnik:** kratke definicije i upućivanja na pripadno poglavlje.
- **C — Tipične pogreške po poglavljima:** pomoć pri traženju pogreške u vlastitom postupku.
- **D — Numerička mehanika fluida:** dodatno čitanje o numeričkim metodama i provjeri simulacija.
- **E — Literatura:** popis izvora i preporuke za daljnje čitanje.
- **F — Ključ kontrolnih rezultata:** smjernice, rezultati i kriteriji za otvorene zadatke.
