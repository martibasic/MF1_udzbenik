# Završna provjera arhitekturnog refaktora

Datum: 23. rujna 2026. Polazište je lokalno stanje prije ovog refaktora,
uključujući prethodne izmjene CFD zadatka i tiskovnih skica.
Početni nalazi: [arhitekturni audit](arhitekturni-audit.md).
Upute za održavanje: [arhitektura](arhitektura.md).

## Provedene promjene

- Jedan model opisuje pet dijelova, 15 poglavlja, uvod i šest dodataka.
  Iz njega nastaju konfiguracije, omotači, navigacija i katalog knjige.
- Kanonski Markdown ostaje zajednički izvor weba, PDF-a i zbirnog ispisa.
  Indeks objekata izvodi brojeve, reference, naslove, razine i matematički zapis.
- Zajednički registar komponenti i predložak zamjenjuju ručno oblikovanje
  novih primjera, zadataka i autorskih blokova. P/Z brojevi slijede redoslijed;
  T1–T4 ostaje semantički podatak.
- Tokeni upravljaju izgledom cijele knjige. CSS ima odvojene slojeve, a
  Typst vlastita pravila prijeloma. Tiskovne figure koriste postojeće izvore
  i zasebno zadane veličine geometrije i oznaka.
- CI i lokalna izgradnja koriste isti generator i provjere modela.

## Očuvanje sadržaja i identiteta

Usporedba 22 kanonska dokumenta s lokalnom snimkom prije refaktora potvrdila
je istovjetnost **6.355 matematičkih izraza** i očuvanje eksplicitnih stabilnih
ID-jeva. Dopuštene razlike ograničene su na semantičke oznake, uklanjanje
ručnih P/Z brojeva i zamjenu dupliciranih metapodataka generiranim prikazom.

Sačuvano je **87 riješenih primjera i 90 zadataka**, njihovi rezultati i razine.
Tiskovni audit potvrdio je 94 kanonske skice, 256 izvornih panela,
3.338 nepromijenjenih nepraznih oznaka i 3.989 geometrijskih elemenata.
Nisu mijenjani fizikalni sadržaj ili didaktička logika radi ovog refaktora.

## Automatske provjere

| Provjera | Rezultat |
| --- | --- |
| Generiranje modela | 37 izvedenica usklađeno s izvorima |
| Regresije modela | 6 testova: redoslijed, stabilni ID-jevi i formule, neispravne reference, predložak komponenti i margine |
| Publikacijska struktura | 15 poglavlja, 6 dodataka, 795 numeriranih jednadžbi, 94 figure, 17 notebookova |
| Numerika i pokrivenost | 1.119 usporedbi s kontrolnim vrijednostima, 221 provjera dimenzija/granica/invarijanti i 22 neovisne fizikalne provjere; bez deklariranih praznina |
| Stvarni web i zbirni ispis | 2.132 prikaza numeriranih objekata podudaraju se s modelom; usklađene sekcije i razine |
| Poveznice i HTML | 24 stranice, 222 slike, 2.375 poveznica i 450 sklopivih blokova; bez neispravnih lokalnih odredišta |
| Tiskovne figure | 149 redaka, bez detektiranih preklapanja i odsijecanja; oznake najmanje 9 pt |
| Figure u webu i ispisu | 188 očuvanih zaslonskih prikaza i 298 učitanih tiskovnih redaka u fizičkoj veličini |
| PDF | 339 A4 stranica; provjereni sadržaj, metapodatci, 17 QR kodova, literatura, vezanje captiona i oznake skica |
| JupyterLite paket | 17 notebookova, 4 proširenja i Pyodide |
| Prikaz i pristupačnost | PASS: 72 prikaza na 320/768/1440 px i A4 ispis; WCAG axe, tipkovnica, fokus, kontrast, smanjeno kretanje i prelijevanje |
| JupyterLite u pregledniku | PASS: otvoren notebook i pokrenut Python (Pyodide), status Idle |

Provjera redoslijeda namjerno premješta poglavlja i jednadžbe: prikazani broj
mijenja se, a identitet i matematički sadržaj ostaju isti. Provjera HTML-a
obuhvaća i tijelo zadatka unutar pripadajućeg elementa `article`, jedan H1 po
stranici i napomene koje ostaju u glavnom toku čitanja.

Audit je otkrio Quartovo smanjivanje prozirnosti naslova sklopivih blokova
(kontrast oko 4,0–4,1 umjesto najmanje 4,5) i prednost osnovnog selektora nad
pravilom za smanjeno kretanje. Ispravci su u zajedničkoj komponenti callouta
i globalnom `prefers-reduced-motion` pravilu, bez iznimki po poglavlju.

Za zbirni ispis axe provjerava okvir stranice i svako poglavlje u istom DOM
okruženju i stilovima, uz privremeno odvajanje ostalih poglavlja. Tako se
izbjegava prespor obilazak cijelog matematičkog DOM-a za svaki kontekst.
Provjere geometrije, ID-jeva, headingova i poveznica rade nad cjelovitim izlazom.

## Vizualni pregled

Pregledan je prijelom svih **339 stranica PDF-a** na 22 kontaktna lista,
uz uvećan pregled odabranih stranica. Pregledane su 53 snimke weba koje
obuhvaćaju početnu stranicu, uvod, sva poglavlja i dodatke te dostupne prve
primjere i figure. Dodatno je pregledan početni prikaz poglavlja na 320 px.

Pregled je obuhvatio raspored teksta, širinu sadržaja, napomene, naslove,
figure, captione i prijelome. Nisu opaženi odsijecanje sadržaja ili preklapanja.
Namjerne prazne stranice između cjelina PDF-a ostaju dio obostranog prijeloma.
Ovo je pregled arhitekture i prikaza, a ne nova znanstvena recenzija sadržaja.

Provjereni PDF ima SHA-256:

```text
8218f5da8e617b5ec6d8f6cf71c2b34dbce8f5abeb9aec3739e23441d1654de9
```

Lokalne snimke, kontaktni listovi i međurezultati nalaze se u zanemarenim
direktorijima `tools/tmp/architecture-refactor/` i `tools/tmp/visual/`.
Izlazi namijenjeni korisniku nalaze se u `_site/` i `_book/`.
Ova evidencija ne potvrđuje objavu na GitHub Pagesu; opisuje lokalnu izgradnju.

## Naknadne tehničke dorade: izgradnja i vidljivost

Puni render sada koristi `scripts/render_workspace.py`: zasebnu snimku
spremljenih ulaza, vlastitu Quarto predmemoriju i OS zaključavanje između
punih rendera. Novi izlazi prenose se nakon uspjeha svih zatraženih rendera
i provjere da ulazi nisu promijenjeni. Postojeći JupyterLite i PDF za
preuzimanje ne brišu se tijekom HTML rendera.

Vidljivost za `web`, `pdf` i `print` određuje samo registar komponenti.
Zajednički Lua modul primjenjuju sva tri adaptera. Priprema i samoprovjera
zadržavaju postojeću vidljivost; uklonjen je zaseban PDF popis njihovih klasa.

Provjera dorada:

- 4 testa izolacije: zaštita preview predmemorije i zasebnih resursa,
  neuspjeli render, izmjena izvora tijekom rendera te zaključavanje između procesa.
- 3 testa vidljivosti: šest politika nad dvije postojeće i jednom novom
  komponentom, odbijanje nepoznatog izlaza i stvarni Quarto render.
- Postojećih 6 testova modela i arhitekturni/Typst auditi prolaze.
- `python scripts/build_book.py --render all` uspješno je izgradio cijeli
  web, zbirni ispis i PDF u novoj radnoj mapi. Glavna `.quarto` predmemorija
  i svi kanonski izvori ostali su bajtno isti.
- Svih 339 stranica novog PDF-a ima jednak izdvojeni tekst i jednake
  rasterske piksele kao prethodno pregledano izdanje. PDF i layout auditi prolaze.
- Web/print numeriranje (2.132 prikaza objekata), lokalne poveznice
  (2.375) i JupyterLite paket (17 notebookova) ponovno prolaze provjere.

PDF nakon ponovne izgradnje ima SHA-256
`8a19a0a25b498c5a4310e9e47ca4a667bed1f32fafe1f65f8d820f219ef92a3b`.
Dokazi ove dorade nalaze se u `tools/tmp/technical-refinements/`.
Prethodni potpuni viewport/WCAG pregled ostaje dokaz arhitekturnog refaktora;
ovdje nije ponovno pokretan pregled svih 72 prikaza.
