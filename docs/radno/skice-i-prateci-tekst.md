# Skice i prateći tekst — urednička revizija

## Opseg i odluka

Prema korisnikovu zahtjevu pregledane su sve 94 dotadašnje figure u svih
15 glavnih poglavlja. Relacije, principi, pretpostavke, upute i dulje napomene
preneseni su iz SVG-a u obične Markdown odlomke neposredno ispod slike.
Oznaka odlomka prati ulogu: „Tumačenje skice”, „Veza s proračunom”,
„Napomene uz skice” ili, za grafove, „Uz dijagram”. Sadržaj je zajednički
webu, PDF-u i ispisu iz preglednika.

Skice zadržavaju geometriju, kote, simbole, kratke nazive i oznake fluida.
Grafovi zadržavaju osi, krivulje i radne točke, trokuti brzina svoje vektore,
a dimenzijska matrica i dijagram odluke oznake potrebne za čitanje odnosa.
Izričite granice fizikalnih modela i napomene o sintetičkim podatcima prenesene
su u tekst; nisu uklonjene iz nastavnog sadržaja.

Prikaz `u14_fig_omjer_sila.svg` sadržavao je isključivo tekstne definicije.
Njegov je sadržaj zato u cijelosti pretvoren u odlomke „Karakteristična
mjerila sila”, uz sačuvano javno sidro `fig-u14-omjer-sila`. Uputa koja je
upućivala na numeriranu sliku sada upućuje na taj pregled. Knjiga ima
93 numerirane figure; njihovi postojeći ID-jevi ostaju isti, a nove brojeve
generira sadržajni model. Neiskorišteni kanonski SVG ostaje arhivski izvor.

## Raspored i provjere

Uklonjen je 61 prazan tekstni panel te zaostali simboli i razdjelnici
premještenih legendi. Kanonska platna obrezana su, a prizori složeni samo
translacijom. Nisu mijenjane lokalne koordinate fizičkih objekata ni omjeri
njihovih duljina. Tiskovne izvedenice obnavlja zajednički generator uz
odvojeno oblikovanje oznaka od najmanje 9 pt.

Dvije geometrijske provjere imale su fiksne dimenzije starog platna koje je
uključivalo tekstnu legendu. Sada `check_scene_canvas` provjerava šest
sačuvanih prizora, translaciju bez skaliranja, granice i odvojenost panela.
Postojeće provjere istisnine, otvora, promjera, normala, sila i ostale
fizike ostaju aktivne. Preglednik dodatno mjeri stvarne granice svih
geometrijskih elemenata i oznaka. Audit skica odbija povratak formula u
`formula-guide` ili naslova za zasebne panele relacija i principa.

PDF provjera numeracije sada čita stvarne objekte `Figure` iz kanonskog
indeksa, pa sačuvano sidro pretvorene tekstne slike ne stvara lažnu sliku.
Stari prag od 3000 tekstnih raspona, koji je brojao i premještena objašnjenja,
zamijenjen je usporedbom svake oznake tiskovnog SVG-a s tekstom prije
pripadajućeg opisa u PDF-u. Ponovljene oznake zahtijevaju ponovljena
pojavljivanja; ostaje provjera najmanje veličine slova. Novi regresijski
testovi dio su istog lokalnog i GitHub objavnog runnera. Tom su provjerom
otkrivene tri nestale oznake `n̂`; sada su označene s `n`, uz definiciju
vanjske jedinične normale u pratećem tekstu.

Urednički pregled obuhvaća svih 93 tiskovnih figura i njihov položaj u
konačnom PDF-u. Dokazi ovog radnog ciklusa nalaze se u git-ignoriranoj mapi
`tools/tmp/sketch-prose-review/`: početna snimka, plan prijenosa za svaku
figuru, preneseni odlomci, preslikavanje tekstnih indeksa, prijevodi panela,
pregledi slika i zapisi provjera. To nije novi kanonski izvor; sadržaj ostaje
u `source/` i `assets/print/`.

Puni objavni CI pokreće `scripts/check_publication.py`. Numeričke i
strukturne provjere dopunjuju vizualni pregled; njihov prolaz sam ne
dokazuje didaktičku kvalitetu.
