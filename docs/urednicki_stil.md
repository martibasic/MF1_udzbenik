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
| gubitci; koeficijenti | $h_g$, $h_l$, $h_{loc}$; $\xi$, $\zeta=\lambda L/D+\sum\xi$, $\lambda$ | $K$ volumni modul (iznimka: kobilica u pog. 6); $\lambda_L$ mjerilo duljina |
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
| gustoće vode, morske vode, ulja, žive, zraka | $\rho_v$, $\rho_{mv}$, $\rho_u$, $\rho_{Hg}$, $\rho_{zr}$ | hrvatski indeksi: $v$ voda, $u$ ulje (i $\nu_v$, $\nu_u$, $h_v$, $h_u$ za slojeve); $p_v$ ostaje tlak pare; indeks $m$ samo model (pog. 11, 14) |
| relativna gustoća | $s_r=\rho/\rho_v$ | |
| kut poprečnog nagiba; ostali kutovi | $\varphi$; $\theta$ | |
| širina broda ili pontona | $b$ | $B$ samo centar uzgona |
| polumjer zavoja | $R_z$ | $R$ polumjer spremnika ili luka |
| tlak na slobodnoj površini; tlak plina | $p_{pov}$; $p_{pl}$ | |
| udio otvorene površine rešetke | $\psi$ | |
| ekvivalentna hrapavost; disipacija turbulentne kinetičke energije | $k_s$, relativno $k_s/D$; $\varepsilon$ | $\varepsilon$ samo disipacija (model $k$–$\varepsilon$); tolerancije s indeksom ($\varepsilon_h$) |
| visina dobave crpke; visina turbine | $H_p$; $H_t$ | ne $h_p$, $h_t$ |
| gubitak visine; smično naprezanje na stijenci; koeficijent preljeva | $h_g$ (s indeksima $h_{g,s}$, $h_{g,1}$…); $\tau_{st}$; $C_{pr}$ | hrvatski indeksi (gubitak, stijenka, preljev); ne $h_w$, $\tau_w$, $C_w$ |
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

## Odluke završne recenzije (16. listopada 2026.)

Odluke vrijede za cijelu knjigu; autorica ih može naknadno promijeniti.

- **Sažetak poglavlja** ima jedan oblik u svih 15 poglavlja: na kraju, iza
  zadataka, odjeljak `## Sažetak` (postojeći ID se zadržava) s okvirom
  `.mf1-zavrsni-okvir` bez vlastite labele. Okvir sadrži 5–7 natuknica,
  jednu rečenicu **Najčešća pogreška** i numerirani popis **Nakon ovoga
  poglavlja mora biti moguće**. Sadržaj se uzima iz teksta poglavlja,
  dodatka C i kurikularne matrice.
- **Početak poglavlja** nema okvir „Inženjerski kontekst”; redak
  „Procijenjeno vrijeme rada” stoji ispred prvog `##` odjeljka.
- **Odjeljak zadataka** u izvoru je `## Zadatci za vježbu` s ID-jem
  jedinstvenim u knjizi (`{#sec-uNN-zadatci}` ili postojeći `sec-…`). Samoprovjera se zove „Provjeri sebe”, s
  odgovorom ispod svakog pitanja.
- **Blok uz bilježnicu**: laboratorij s widgetima je „Interaktivni prikaz —
  …”, ostalo „Numerički pokus — …”; tipke „Pokreni u pregledniku” i
  „Pričuvno: otvori u Colabu”. Nazivi blokova slijede obrazac „Vrsta —
  Podnaslov”.
- **Pravopis i nazivlje**: potkritični / natkritični (ne pod-, nad-);
  vodoravno / okomito (prema smislu uspravno), ne horizontalno / vertikalno;
  brzina vrtnje u $\mathrm{min^{-1}}$, ne okr/min; ulaž (engl. *ullage*)
  pri prvom spomenu, dalje ulaž, ulažni otvor; usisni koš (engl. *sea
  chest*); kućište crpke, crpna stanica, radno kolo, propeler, umirni bazen;
  klizna mreža (engl. *sliding mesh*); u tekstu „Bernoullijeva jednadžba”
  (naslov pog. 8 ostaje); „konst.” u matematici uvijek `\text{konst.}`;
  kratica „MF1” ne stoji u tekućem tekstu (piše se „u ovom priručniku” ili
  „Mehanika fluida 1”).
- **Notacija**: oznake točaka i presjeka pišu se kao matematičke oznake
  ($A$, $B$), kratice HGL i EGL kao običan tekst, ne kodnim fontom. Popisi
  brojeva u matematici odvajaju se točkom-zarezom, npr. $(26;\,0)$. Masa
  pomaknutog utega u pokusu nagibanja je $m_k$; uzvodna dubina ispred ustave
  $y_0$; manometarski zaustavni tlak $p_{0,M}$.
- **Poznate iznimke oznaka** (navedene i u dodatku A): $K$ je volumni modul,
  a u pog. 6 točka kobilice; $M$ je moment, a u pog. 6 metacentar; $k$ je
  turbulentna kinetička energija (pog. 12), rang dimenzijske matrice i faktor
  oblika $(1+k)$ (pog. 11) te koeficijent gubitka relativne brzine (pog. 14);
  $R$ je polumjer, plinska konstanta (pog. 9) i hidraulički otpor dionice
  (pog. 13); $v_s$ je brzina broda, a u pog. 13 brzina u usisnom presjeku
  crpke. Svaka se iznimka uvodi uz definiciju pri prvom spomenu.
- **Dodatci** počinju uvodnim odlomkom izravno ispod naslova iz
  `content/book.json`, bez prvog `##` koji ponavlja naslov. Dodatak A sadrži
  samo opće relacije; postupci pojedinih zadataka ostaju u poglavljima i
  smjernicama dodatka F.
