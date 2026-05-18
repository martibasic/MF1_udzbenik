# Val 1 - javne prerade zadataka

> Status u svibnju 2026.: ovaj dokument je povijesni zapis prvog vala javnih prerada. Opisani zadaci vec su preseljeni u stvarna `source` poglavlja i vise se ne tretiraju kao otvoreni staging-paket.

## Svrha dokumenta

Ovo je prvi stvarni izlaz nakon `protokol_prerade_zadataka_i_skica.md`. Dokument ne cuva samo ideju prerade, nego tri konkretne javne verzije zadataka koje se vise ne oslanjaju na izvorni tekst kao predlozak.

## Status ovog vala

- broj javnih prerada: `3`
- poglavlja: `U04`, `U07`, `U12`
- namjena: zakljucati prvi kucni prag `P2/P3` prerade i prvi standard briefa za skicu
- povezana puna rjesenja: `val1_puna_rjesenja_zadataka.md`
- izvedene radne skice: `assets/print/u04_val1_procesna_kada.svg`, `assets/print/u07_val1_platforma_kompresor.svg`, `assets/print/u12_val1_vodilica_mlaza.svg`
- migrirano u source: `source/u04_relativno_mirovanje_fluida.md`, `source/u07_uzgon_plivanje_i_stabilnost.md`, `source/u12_pokretne_lopatice_i_potisak.md`

---

## VAL1-01 | U04 | Procesna kada na ubrzanoj platformi

### Interni metapodaci

- target_chapter: `U04`
- source_concept: `relativno mirovanje u otvorenom spremniku s granicnim uvjetom prelijevanja`
- editorial_role: `tipicni T3 prijelazni zadatak`
- rewrite_status: `preradeno`
- rewrite_level: `P3`
- sketch_requirement: `obavezna`
- sketch_asset: `assets/print/u04_val1_procesna_kada.svg`
- pilot_anchor: `PILOT-01`

### Sto je promijenjeno

1. Opci otvoreni spremnik pretvoren je u procesnu kadu na automatskoj platformi.
2. Umjesto trazene vanjske sile uvodi se granicno dopusteno ubrzanje i sila na straznju stijenku.
3. Pocetno punjenje vise nije potpuno, pa zadatak prirodno trazi i geometrijsku provjeru slobodne povrsine.
4. Javna scena je napisana od nule i ne slijedi izvorni redoslijed pitanja.

### Javni naslov

Procesna kada na automatskoj platformi

### Javni tekst zadatka

Pravokutna otvorena kada unutarnjih dimenzija $L = 1{,}80\ \text{m}$, $H = 0{,}72\ \text{m}$ i $B = 0{,}95\ \text{m}$ prevozi rashladnu tekucinu gustoce $\rho = 970\ \text{kg/m}^3$. U mirovanju je tekucina u kadi do visine $h_0 = 0{,}54\ \text{m}$. Kada se platforma pocne gibati stalnim ubrzanjem udesno, tekucina se postavi u relativno mirovanje.

1. Odredite najvece dopusteno ubrzanje $a_{max}$ pri kojem tekucina jos ne prelijeva preko ruba kade.
2. Za to granicno stanje odredite visinu tekucine uz straznju i prednju stijenku.
3. Odredite rezultantnu silu fluida na straznju vertikalnu stijenku po punoj sirini kade.

Zanemarite valjanje, povrsinsku napetost i prolazne oscilacije. Pretpostavite da je gibanje dovoljno sporo da se moze primijeniti model relativnog mirovanja.

### Brief za skicu

- nacrtati pravokutni spremnik u bocnom pogledu
- oznaciti smjer ubrzanja `a` udesno
- prikazati nagnutu slobodnu povrsinu koja raste prema straznjoj stijenci
- oznaciti `L`, `H`, `h_straznja`, `h_prednja`
- na straznjoj stijenci ucrtati rezultantu `F_R`
- u malom pomocnom detalju prikazati efektivno polje sila `g_e`

---

## VAL1-02 | U07 | Plutajuca servisna platforma s pomaknutim kompresorom

### Interni metapodaci

- target_chapter: `U07`
- source_concept: `plivanje prizmatskog tijela uz bocno pomaknut teret i momentnu ravnotezu`
- editorial_role: `reprezentativni T3 zadatak za ravnotezu i geometriju urona`
- rewrite_status: `preradeno`
- rewrite_level: `P3`
- sketch_requirement: `obavezna`
- sketch_asset: `assets/print/u07_val1_platforma_kompresor.svg`
- pilot_anchor: `PILOT-05`

### Sto je promijenjeno

1. Ponton s nepoznatom masom tereta pretvoren je u servisnu platformu s poznatim uredajem i nepoznatim polozajem uredaja.
2. Glavno pitanje vise nije masa tereta za zadani nagib, nego lateralni polozaj kompresora iz izmjerenih urona.
3. U zadatak je dodana stvarna mjeriva posljedica nagiba: uroni lijevog i desnog ruba.
4. Geometrija i pitanja su poslozeni tako da student mora odvojiti ravnotezu sila i ravnotezu momenata.

### Javni naslov

Plutajuca servisna platforma s pomaknutim kompresorom

### Javni tekst zadatka

Pravokutna plutajuca servisna platforma duljine $L = 3{,}10\ \text{m}$ i sirine $B = 1{,}00\ \text{m}$ ima masu $m_p = 676\ \text{kg}$ i pluta u vodi gustoce $\rho = 998\ \text{kg/m}^3$. Na platformu je postavljen prijenosni kompresor mase $m_k = 190\ \text{kg}$, ali nije poznato na kojoj se udaljenosti $e$ od uzduzne osi simetrije nalazi njegovo teziste.

Nakon postavljanja kompresora izmjereno je da je uron lijevog ruba platforme $h_L = 0{,}34\ \text{m}$, a uron desnog ruba $h_D = 0{,}22\ \text{m}$. Pretpostavite da je platforma kruta, da joj je dno ravno, a bocne stijenke okomite.

1. Odredite ukupni istisnuti volumen vode u ravnoteznom polozaju.
2. Odredite udaljenost $e$ tezista kompresora od uzduzne osi simetrije platforme.
3. Odredite za koliko je srednja uronjenost platforme veca nego prije postavljanja kompresora.

Zanemarite valove, debljinu stijenki i dodatne pomake tereta tijekom mjerenja.

### Brief za skicu

- nacrtati poprecni presjek platforme u vodi
- oznaciti lijevi i desni rub te urone `h_L` i `h_D`
- ucrtati uzduznu os simetrije
- prikazati tezinu platforme u osi simetrije i tezinu kompresora pomaknutu za `e`
- ucrtati silu uzgona kroz teziste istisnine
- po mogucnosti dodati mali tlocrtni inset s oznakom smjera pomaka kompresora

---

## VAL1-03 | U12 | Vodilica mlaza na ispitnom stolu

### Interni metapodaci

- target_chapter: `U12`
- source_concept: `sila mlaza na nepomicnu zakrivljenu vodilicu`
- editorial_role: `bazni P2 zadatak za prijelaz sa sile mlaza na reakciju nosaca`
- rewrite_status: `preradeno`
- rewrite_level: `P2`
- sketch_requirement: `obavezna`
- sketch_asset: `assets/print/u12_val1_vodilica_mlaza.svg`
- pilot_anchor: `PILOT-08`

### Sto je promijenjeno

1. Opca nepomicna lopatica pretvorena je u vodilicu mlaza na ispitnom stolu.
2. Uveden je pravokutni mlaz i gubitak brzine kroz vodilicu, pa scena vise nije cisti preslik idealnog primjera.
3. Traze se komponente sile i reakcija nosaca, a ne samo jedna ukupna sila.
4. Javni tekst je napisan kao samostalni laboratorijsko-inzenjerski zadatak.

### Javni naslov

Vodilica mlaza na ispitnom stolu

### Javni tekst zadatka

Na ispitnom stolu voda izlazi iz pravokutne sapnice sirine $b = 36\ \text{mm}$ i visine $h = 14\ \text{mm}$ brzinom $v_1 = 24\ \text{m/s}$. Mlaz ulazi u nepomicnu vodilicu koja ga u horizontalnoj ravnini skrece za kut $\beta = 120^\circ$ u odnosu na smjer ulaza. Zbog gubitaka u vodilici izlazna brzina mlaza iznosi $v_2 = 19\ \text{m/s}$. Gustoce vode je $\rho = 998\ \text{kg/m}^3$.

1. Odredite maseni protok vode kroz sapnicu.
2. Odredite horizontalne komponente sile koju fluid vrsi na vodilicu.
3. Odredite iznos i smjer reakcije koju mora preuzeti nosac vodilice.

Pretpostavite da je tlak na ulazu i izlazu jednak atmosferskom, a tezinu vode unutar vodilice zanemarite.

### Brief za skicu

- nacrtati tlocrt mlaza i vodilice
- oznaciti ulazni smjer `v_1` i izlazni smjer `v_2`
- jasno oznaciti kut skretanja `beta`
- oko vodilice ucrtati kontrolni volumen
- prikazati osi `x` i `y` za rastav sila
- uz nosac ucrtati reakcijske komponente `R_x` i `R_y`

---

## Operativna napomena za sljedeci korak

Val 1 sada ima cetiri zatvorena sloja:

1. javne prerade zadataka
2. puna rjesenja u istom kucnom stilu
3. radne staticke SVG skice za print
4. preseljena pilot-poglavlja u stvarni `source` sloj

Sljedeci stvarni korak vise nije migracija Val 1 trojca, nego jedno od ova dva sirenja:

1. prosiriti `U04`, `U07` i `U12` dodatnim zadacima iz pilot-batcha
2. otvoriti `Val 2` prerade za `U05` i `U11/U12`