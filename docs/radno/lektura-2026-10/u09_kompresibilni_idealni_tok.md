# Lektura: source/u09_kompresibilni_idealni_tok.md (pog. 9)

Pregledana je cijela datoteka (redci 1–711): uvod, teorija, tri izvoda, šest riješenih primjera,
CFD blokovi, granice modela, postupak, samoprovjera, napomene uz skice, Z1–Z6 s naputcima i
kontrolnim rezultatima, numerički pokus i završni okvir.

## 1. Izmjene (oko 83 zahvata)

| Vrsta | Broj (približno) |
| --- | --- |
| Upućivanja s krivim padežom (`@id` → imenica u padežu + `[-@id]`) | 19 |
| Kalkovi i nespretni izrazi („predstavlja”, „jest” → „iznosi”, „značajan” → „znatan”, „pripadajući” → „pripadni”, „proporcionalno” → „razmjerno”) | 14 |
| Bezlični pasiv „promatra se / raspiše se / podijeli li se” → aktiv u 1. l. mn. | 6 |
| Red riječi i enklitike („U Z2 ventil je” → „U Z2 je ventil”; „iza njega tok je” → „iza njega je tok”) | 6 |
| Sročnost i padež („zanima nas potrošnja i stanje” → „zanimaju nas”; „a $T_0$ ostaje isti” → „ista”) | 4 |
| Nepotpune rečenice ispred formule dopunjene glagolom („pa diferenciranjem” → „pa diferenciranjem slijedi”) | 3 |
| Preslagivanje dugih ili nejasnih rečenica (zagušenje, Z2, Z3, Z4, završni okvir) | 10 |
| Nazivlje („prije/poslije vala” → „ispred/iza vala”; „udar” → „udarni val”; „tekućinski krug” → „krug s kapljevinom”; „vodeni Venturi” → „Venturijeva cijev s vodom”) | 8 |
| Ostalo (zarez ispred „pa”, vid glagola, „zadamo” → „zadajemo”) | ~13 |

Reprezentativni primjeri:

- „Tlačni poremećaj širi se **relativno prema plinu**” → „… širi se **u odnosu na plin**”
- „pri zagušenju **grlo** $A^*$ doseže $Ma=1$” → „pri zagušenju **tok u grlu** $A^*$ doseže $Ma=1$”
- „Uvrštavanjem $Ma=1$ **u @eq-t0-t i @eq-stagnacijski-omjeri**” → „… **u jednadžbe [-@eq-t0-t] i [-@eq-stagnacijski-omjeri]**”
- „Ručni @ex-normalni-udar daje …, a @ex-kd-sapnica-rezim …” → „Ručni proračun **u primjeru [-@ex-normalni-udar]** daje …, a **primjer [-@ex-kd-sapnica-rezim]** …”
- „maseni protok dostiže granicu … i daljnje snižavanje nizvodnog tlaka više ga ne povećava uz iste …: tok je zagušen” → „maseni protok dostiže granicu …: uz iste $p_0$, $T_0$ i površinu grla daljnje ga snižavanje nizvodnog tlaka više ne povećava, pa je tok zagušen”
- „Pri upućivanju zrak teče kroz ventil čiji je najmanji slobodni presjek … u vod prema motoru u kojem vlada tlak …” → „Pri upućivanju zrak kroz ventil najmanjeg slobodnog presjeka … teče u vod prema motoru, u kojem vlada tlak …”
- „Stvarni ventil traži koeficijent istjecanja …; vrijednost nije sigurnosna certifikacija.” → „Za stvarni ventil potrebni su koeficijent istjecanja …; izračunana vrijednost ne zamjenjuje sigurnosnu certifikaciju.”
- „Za podzvučni tok ubrzavanje zahtijeva suženje; za nadzvučni tok ubrzavanje zahtijeva širenje.” → „U podzvučnom toku ubrzavanje zahtijeva suženje, a u nadzvučnom proširenje.”

Naslovi `###` bez izričitog `{#id}` (koraci rješenja u primjeru 9.6) nisu mijenjani.

## 2. Sadržajni nalazi koje NISAM ispravio

1. **Pogreška u LaTeX-u, r. 664 (Z6, stavka 2):** `$|\Lambda-\Lambda_{mj}|\leqs(\Lambda-\Lambda_{mj})$`.
   `\leqs` nije naredba (nedostaje razmak: treba `\leq s(\Lambda-\Lambda_{mj})`). MathJax/Typst će
   ispisati grešku ili krivi znak. Pogreška je ušla u commitu 36f29af (zamjena $u(x)$ → $s(x)$).
2. **Notacija tlaka, r. 302 (primjer 9.4, provjera):** „s manometarskim tlakom $p_0=499\ \text{kPa}$” —
   prema standardu $p_0$ je samo zaustavni (apsolutni) tlak, a manometarski se piše $p_M$ (u Z4 se
   ispravno koristi $p_{0,M}$). Prijedlog: $p_{0,M}=499\ \text{kPa}$.
3. **Neznatna nedosljednost naziva, r. 150:** „Za stacionarni, adijabatski tok **idealnog plina**”, dok
   ostatak poglavlja i granica modela govore o **kalorički savršenom plinu**. Fizikalno nije pogrešno
   (relacija $h+v^2/2=h_0$ vrijedi općenito), ali može zbuniti.

Numerički sam ponovio sve rezultate primjera i kontrolnih rezultata (a, Ma, $T_0$, $p_0$, $\dot m_{max}$,
$p^*$, $Ma_2$, $p_2/p_1$, $\Delta s$, $A/A^*$ grane, $p_{e,I/II/III}$, položaj vala $A_x/A^*=1{,}39$,
$Ma_1=1{,}75$, $p_{02}/p_{01}=0{,}833$, Z1–Z6): svi se slažu unutar zaokruživanja.

## 3. Provjere

- `lektura_check.py source/u09_kompresibilni_idealni_tok.md`: **ok** (bez redaka STROGO; matematika,
  ID-jevi, atributi, ograde, polja i razine identični polaznom stanju).
- `tools/check_u09_sketch_geometry.py`: **PASS U09: 1251 provjera stvarne geometrije skica.**
- `tools/audit_publication.py`: **Publication audit PASS** (U09: primjeri=6, zadatci=6 [T1,T1,T2,T2,T3,T4]).
