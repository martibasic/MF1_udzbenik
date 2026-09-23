# Urednički stil udžbenika

Ovaj dokument opisuje zajednički prikaz i urednički glas nakon dotjerivanja
knjige. Autorski ugovor, kurikularna matrica i pravila fizikalnih skica ostaju
mjerodavni za sadržaj.

## Tekst

- Uvod imenuje fizikalno pitanje i model. Primjene trebaju pomoći razumijevanju;
  dugi popisi industrija i izjave o važnosti predmeta nisu zamjena za objašnjenje.
- Čitatelju se u uputama obraćamo u jednini: „Odredi”, „Provjeri”, „Obrazloži”.
- U dužem zadatku odvoji prizor i podatke, pretpostavke te traženu odluku u
  odlomke. Zadrži sve uvjete, jedinice i granice modela.
- Skraćivanje ne smije ukloniti fizikalno važnu ogradu niti promijeniti model.
  Formule, ulazi i rezultati provjeravaju se odvojeno od jezične dorade.
- Naslov i njegova oznaka trebaju jasno razlikovati odjeljak, primjer, korak
  rješenja i samostalni zadatak. Ne mijenjaj stabilni ID radi kraćeg naslova.

## Mrežno izdanje

Glavni tekst koristi Source Serif 4, a naslovi i navigacija Inter. Taman tekst,
bijela podloga, mirna bočna traka i bakreni naglasak čine zajedničku paletu.
Zadržane su postojeće boje semantičkih blokova i skica. Sadržaj poglavlja stoji
uz tekst, a početak poglavlja ima kratke poveznice na vježbe, formule i rezultate.

Slike se mogu otvoriti u punoj veličini. Široka tablica pomiče se unutar vlastita
imenovanog područja, dostupnog tipkovnicom; cijela stranica ne smije se širiti.
Sadržaj i osnovne poveznice ostaju čitljivi i bez dodatnog JavaScripta.

## PDF

Nativni PDF koristi otvorene naslove bez obojenih okvira, zajedničku paletu,
hrvatska zaglavlja i jasno odvojene naslove primjera. Autorski blokovi ostaju
prelomivi, a naslovi se drže uz tekst koji uvode. A4 i brojčane oznake poglavlja,
slika, tablica i jednadžbi ostaju očuvani.

Prilagođeni `assets/typst/typst-show.typ` konfigurira ugrađeni predložak
Quarta 1.9.37, a `mf1-reading.typ` oblikuje sadržaj knjige. Pri nadogradnji
provjeri i Quartoove posebne brojače slika: promjena izgleda naslova ne smije
uzrokovati nastavak numeracije slika iz prethodnoga poglavlja.

Typst filtar uklanja samo TeX-ovu oznaku negativnog tankog razmaka `\!`
iz prikaznog stabla formule. Pandoc u Quartu 1.9.37 prevodi je u prevelik
pomak `#h(-1em)`, što preklapa simbole. Izvorna formula ostaje nepromijenjena,
a PDF koristi uobičajene matematičke razmake.

## Provjera

Nakon zajedničke promjene tipografije pregledaj HTML i PDF: početnu stranicu,
dug naslov, tekst s formulama, tablicu, riješeni primjer, zadatak i dodatak.
Automatizirani pregled obuhvaća sve stranice na tri širine, kontrast i
tipkovnicu. Vizualna provjera mora obuhvatiti i stvarne PDF prijelome,
čitljivost skica te potpunost matematičkih izraza.

Tehnička podloga: [Quarto — prilagođeni Typst formati](https://quarto.org/docs/output-formats/typst-custom.html).
