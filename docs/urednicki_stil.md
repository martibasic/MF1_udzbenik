# Urednički stil sveučilišnog priručnika

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

## CFD objašnjenja i numerički pokusi

- CFD odlomak povezuje pitanje iz poglavlja s konkretnim modelom, ulazima,
  izlazima i odlukom. Uz riješeni primjer navedi koja njegova pretpostavka
  u proširenom modelu postaje rezultat ili zahtijeva dodatne podatke.
- Napomena uz skicu objašnjava izbor modela, oznake, smjerove i mjerilo.
  Računski postupak pripada rješenju, a provjera tumači rezultat i granice
  primjene. Ne ponavljaj isti niz formula na sva tri mjesta.
- Dijagnostička provjera razlikuje ono što rezultat potvrđuje od onoga što
  još ne potvrđuje: primjerice, točan ukupni protok ne potvrđuje točnu podjelu.
  Ključna provjera mora biti u vidljivom tekstu. Postojeći skriveni blokovi
  samoprovjere ne zamjenjuju tu provjeru; vidljivost određuje registar.
- Uputa uz bilježnicu ima dvije kratke cjeline: **Predvidi** te
  **Provjeri i protumači**. Koristi stvarne pokuse iz bilježnice; analitički
  model, numeričku integraciju i sintetičke podatke jasno razlikuj od CFD-a.
- Dodatak D sadrži zajednički postupak i provjere. Iz poglavlja uputi na
  odgovarajući odjeljak, a iz pregleda primjena na konkretne CFD odlomke.

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

## Notacija i nazivlje (standard od 12. listopada 2026.)

Jedna veličina ima jednu oznaku kroz cijelu knjigu; dodatak A navodi iznimke.
Kad se u pojedinom poglavlju nužno koristi druga oznaka, uvodi se pri prvom
spomenu s izričitom napomenom.

| Veličina | Oznaka | Napomena |
| --- | --- | --- |
| brzina fluida | $v$, $\vec v$, komponente $v_x$, $v_i$ | ne $u$, $\mathbf u$, $V$ |
| brzina krute granice | $u$ (lopatica, klip, ploča); $v_s$, $v_m$, $v_p$ (brod, model, prototip); $v_A$ (napredovanje propelera); $v_j$ (mlaz) | turbostrojevi: $c$ apsolutna, $w$ relativna, $u$ obodna |
| vanjska brzina graničnog sloja, brzina trenja | $U_e$, $U_\infty$, $u_\tau$ | uz definiciju |
| brzina zvuka; brzina površinskog vala | $a$; $c$ (samo pog. 15) | |
| volumen; istisnina; masa istisnine; gaz; nadvođe | $V$; $V_{ist}$; $\Delta$; $T$; $f$ | |
| tlak atmosferski, manometarski, apsolutni, pare, zaustavni | $p_{atm}$, $p_M$, $p_{aps}$, $p_v$, $p_0$ | $p_0$ samo zaustavni; Bernoulli s $p/(\rho g)$ |
| gubitci; koeficijenti | $h_w$, $h_l$, $h_{loc}$; $\xi$, $\zeta=\lambda L/D+\sum\xi$, $\lambda$ | $K$ samo volumni modul; $\lambda_L$ mjerilo duljina |
| izentropski eksponent; specifična težina | $\kappa$; $\gamma$ | |
| bezdimenzijski brojevi | $Ma$, $Re$, $Fr$, $We$, $St$, $Bo$, $Eu=\Delta p/(\rho v^2)$ | |
| korekcijski faktori; kutovi | $\alpha$, $\beta$; $\theta$, $\varphi$ | kutovi lopatica $\beta_1$, $\beta_2$ samo u pog. 14 |
| hidraulički promjer, dubina, radijus | $D_h=4A/P$, $y_h=A/T$, $R_h=A/P$ | $T$ širina slobodne površine (pog. 15) |
| centar tlaka | $h_{CP}$, $y_{CP}$ | |
| protok po širini; volumenski; maseni | $q$ (samo pog. 15); $Q$; $\dot m$ | |
| tetiva profila; toplinski kapacitet | $l$; $c_p$ | |
| potisak; temperatura | $F_T$; $T$ | |
| kavitacijski broj | $\sigma_{kav}=(p_{ref}-p_v)/(\tfrac12\rho v_{ref}^2)$ | referentno mjesto navesti |
| kavitacijska rezerva | $NPSH_a$, $NPSH_r$ | |
| kontrolni volumen i ploha | KV, KP; indeksi ul, iz | |
| stabilitet | $B$, $G$, $M$, $KB$, $BM$, $KG$, $GM$ | bez nadvlake |
| težina | $F_G$ ili $mg$ | $G$ samo težište (stabilitet), ne težina |
| gustoće vode, morske vode, ulja, žive, zraka | $\rho_w$, $\rho_{mv}$, $\rho_o$, $\rho_{Hg}$, $\rho_{zr}$ | indeks $v$ samo para ($p_v$); indeks $m$ samo model (pog. 11, 14) |
| relativna gustoća | $s_r=\rho/\rho_w$ | |
| kut poprečnog nagiba; ostali kutovi | $\varphi$; $\theta$ | |
| širina broda ili pontona | $b$ | $B$ samo središte istisnine |
| polumjer zavoja | $R_z$ | $R$ polumjer spremnika ili luka |
| tlak na slobodnoj površini; tlak plina | $p_{pov}$; $p_{pl}$ | |
| udio otvorene površine rešetke | $\psi$ | |
| ekvivalentna hrapavost; disipacija turbulentne kinetičke energije | $k_s$, relativno $k_s/D$; $\varepsilon$ | $\varepsilon$ samo disipacija (model $k$–$\varepsilon$); tolerancije s indeksom ($\varepsilon_h$) |
| visina dobave crpke; visina turbine | $H_p$; $H_t$ | ne $h_p$, $h_t$ |
| standardna nesigurnost | $s(x)$; $s_E$, $s_\Delta$ | ne $u(x)$ ($u$ je brzina krute granice) |
| koeficijent sustrujanja; faktor učinka rotora | $\chi$; $FM$ | samo pog. 14 |
| kut lopatice | $\beta_1$, $\beta_2$ od smjera $-u$ | kut skretanja mlaza $\theta$ |
| volumenski protok | $Q$ u m$^3$/s ili L/s | jedinica „L/s” (veliko L) |

Vektori na skicama (standard od 14. listopada 2026.): jedna boja `#356b83`,
a vrsta veličine određena je stilom i atributom `data-mf1-vector`. Sila i moment:
deblja puna crta (2,4–3,4) i pun vrh. Brzina, smjer protoka i kutna brzina: tanja
crta (1,3–2,0) i otvoren vrh. Ubrzanje i efektivno polje: isprekidana crta
(1,6–2,4) i pun vrh. Raspodijeljeni tlak i jedinična normala: tanka crta (0,8–1,6)
i pun vrh. Strelice koje nisu vektori (kote, osi, vodilice, strujnice, putanje,
dijagrami) nose `data-mf1-role` i ne koriste vektorsku boju. Oznaka vektora uz
strelicu piše se podebljano, oznake skalara obično. Pravilo provjerava
`tools/audit_sketch_design.py`; legenda za čitatelja nalazi se u uvodnom
poglavlju „Kako koristiti priručnik”.

Nazivlje: crpka; hidraulički; hidrostatički; meniskus; Reynoldsov transportni
teorem; zaustavne veličine; kalorički savršen plin; zagušenje (choking) prema
prigušenju (throttling); energijska crta (EGL) i piezometarska crta (HGL);
Darcyjev koeficijent trenja; volumenski protok; metacentarska visina;
stabilitet, nadvođe, poluga stabiliteta $GZ$, poprečni nagib, kut nestajanja
stabiliteta, metoda dodane težine; zapljuskivanje; prividna sila; impulsna
funkcija. Poglavlje ne upućuje samo na sebe brojem; piše „u ovom poglavlju”.
