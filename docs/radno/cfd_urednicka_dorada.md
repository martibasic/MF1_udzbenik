# Urednička dorada CFD poveznica i čitanja primjera

Opseg: korisnikova provedba svih pet predloženih dorada, 26. rujna 2026.
Izvori su svih 15 nastavnih poglavlja i dodatak D. Rad nadograđuje prethodno
uređenje zadataka i izdvajanje objašnjenja iz skica u obični tekst.

## Provedene odluke

1. U 49 napomena uz skice uklonjeno je ponavljanje računa koji slijedi u
   rješenju. Zadržani su modeli, tijela na koja djeluju sile, smjerovi,
   grafička mjerila i važna geometrijska objašnjenja. Pregledne skice i
   napomene uz vježbe nisu mehanički skraćivane.
2. U svakom poglavlju dorađeno je jedno dijagnostičko pitanje i odgovor.
   Skupni odgovori u osam poglavlja razdvojeni su brojevima. Pregled stvarnih
   izlaza potvrdio je da `SelfCheck` ima `visibility: []`, što ostaje
   očuvano. Zato je smisao svih 15 provjera ugrađen i u postojeći vidljivi
   tekst: u CFD odlomke U01–U13 i U15 te numerički pokus U14.
3. CFD tekst upućuje na pretpostavke stvarnih riješenih primjera. U07
   razlikuje zadanu jednoliku podjelu protoka od podjele koju računa CFD;
   U12 uspoređuje razvijeni tok u kapilari s računalnim testom istih uvjeta;
   U14 povezuje idealni disk drona s modelom propelera uz trup.
4. Svih 17 uputa uz bilježnice koristi slijed „Predvidi” i „Provjeri i
   protumači”. Pitanja proizlaze iz postojećih pokusa. Poveznice, QR kodovi
   i izvršni sadržaj bilježnica nisu mijenjani.
5. U12 sažima diskretizaciju i provjeru uz svoje jednadžbe, a zajednički
   tijek i V&V povezuje s dodatkom D. Njegov postojeći pregled četiriju
   primjena dobio je 14 izravnih poveznica na CFD odlomke.

## Dijagnostičke provjere po poglavljima

| Poglavlje | Što rezultat sam još ne potvrđuje |
|---|---|
| U01 | povećanje sile nije povećanje rada |
| U02 | točna ravnotežna visina nije provjera vremena punjenja |
| U03 | različite reference tlaka mogu opisivati isto stanje |
| U04 | viši prvi val nije proturječje ravnotežnom nagibu |
| U05 | jednaka sila ne znači jednak moment oko zgloba |
| U06 | isti gaz ne potvrđuje isti stabilitet |
| U07 | točan ukupni protok ne potvrđuje raspodjelu po granama |
| U08 | pad statičkog tlaka nije sam po sebi trajan gubitak |
| U09 | rast statičkog i pad ukupnog tlaka kroz udar nisu proturječni |
| U10 | suprotne sile na različitim tijelima nisu pogreška predznaka |
| U11 | jednak Froudeov broj ne potvrđuje prijenos viskoznog otpora |
| U12 | mali rezidual ne potvrđuje malu diskretizacijsku pogrešku |
| U13 | jednaki padovi energije ne zahtijevaju jednake protoke |
| U14 | različit zahvaćeni protok može dati različite optimume snage |
| U15 | disipacija energije sukladna je bilanci količine gibanja |

## Provjera i granice zaključka

Početna snimka i pregled svake izmjene nalaze se u lokalnom radnom izlazu
`tools/tmp/cfd-editorial-review/`. Usporedba potvrđuje isti matematički
sadržaj svih 796 numeriranih jednadžbi, iste zadane podatke, stabilne stare
ID-jeve te 87 primjera i 90 zadataka s istim razinama. Novi ID-jevi služe
odredištima poveznica; ne mijenjaju strukturu knjige. Izvedenice su obnovljene
generatorima. SVG-ovi, izvršni kod bilježnica i registar vidljivosti nisu
mijenjani u ovom prolazu.

Puni lokalni objavni CI prošao je u 737 s, uključujući izvršavanje svih
17 bilježnica i provjere prikaza i pristupačnosti u 72 prikaza na širinama
320, 768 i 1440 px te u A4 ispisu. Nakon posljednjih sitnih dorada početaka
rečenica i prilagodbe tablice u D04 uslijedili su ponovni puni render weba
i PDF-a te ciljane provjere arhitekture, izvora i konačnih izlaza. I taj
završni prolaz uspješno je dovršen; puni CI nije ponavljan nakon tih dorada.

Konačni PDF ima 315 stranica, jednako kao početni. Provjere obuhvaćaju
raspored PDF-a, svih 24 mrežnih stranica, 15 vidljivih dijagnostičkih
tumačenja, 17 uputa uz bilježnice i svih 14 poveznica iz dodatka D na
odgovarajuće CFD odlomke u oba izlaza. Tablica u D04 na uskom zaslonu
podržava vodoravno pomicanje i tipkovnicu. Vizualno su pregledane odabrane
stranice svih 15 poglavlja, a nakon završnih sitnih dorada svih 15
promijenjenih stranica; preostalih 300 stranica rasterom je jednako
prethodnom renderu.

Isporučeni PDF u `_book/`, kopija u `_site/downloads/` i datoteka preuzeta
preko lokalnog pregleda podudaraju se: 6 572 323 bajta, SHA-256
`2841833e97ee4e320bfb15a6b1bdef1abc0960876303caf2dd2d9b8d96049c22`.
Lokalni pregled ostavljen je dostupan na <http://127.0.0.1:8766/>.
Zapisnici, usporedbe i slike nalaze se u navedenoj lokalnoj radnoj mapi.

Urednička procjena odnosi se na manju količinu ponavljanja, jasnije granice
modela i konkretnije studentske odluke. Automatske provjere potvrđuju
tehničku cjelovitost, a učinak na studentsko razumijevanje zahtijeva pilot.
