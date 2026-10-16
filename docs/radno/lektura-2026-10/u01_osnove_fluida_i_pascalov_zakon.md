# Lektura: source/u01_osnove_fluida_i_pascalov_zakon.md (pog. 1)

Cijela datoteka (835 redaka) pregledana je odlomak po odlomak: uvod, teorija, CFD blokovi,
granica modela, izvod, Cauchyjev tetraedar, šest riješenih primjera, samoprovjera s odgovorima,
Z1–Z6 s naputcima i kontrolnim rezultatima, napomene uz skice i sažetak.
Diff prema polaznom stanju: 75 promijenjenih redaka, oko 70 zahvata. Svi su uređeni alatom Edit.

## 1. Vrste izmjena

- **Red riječi i enklitike (oko 10)**: „istisnuti volumeni su jednaki”, „taj dodatni tlak ne prenosi se”,
  „izlazna sila 35 je puta veća”, „Oba cilindra pod tlakom pritom se produljuju”, „Oba zadana
  kriterija jesu zadovoljena”, „Gustoća sama”, „Sile same”.
- **Upućivanja (1)**: „Ručni @ex-u01-servisna-hidraulicna-dizalica-t2 pretpostavlja” (ispisivalo bi
  „Ručni primjer 1.x”) → „Ručna dizalica iz primjera [-@ex-…] pretpostavlja”. Upućivanja na pog. 3
  složena su prirodno („iz pog. 3 …”).
- **Kalkovi i nespretni izrazi (oko 20)**: „predstavlja” → „je”, „jest” umjesto „iznosi”, „navodi da” → „kaže da”,
  „račun treba vratiti” → „račun mora dati”, „dostaje” → „dovoljan je”, „Sila po jednom … cilindru” →
  „Sila jednoga … cilindra”, „omjer … prema …” → „omjer … i …”, „dostavljenog” → „dobavljenog”,
  „slobodan za pomak” → „može se slobodno pomicati”, „Za izoterman CFD” → „U izotermnom CFD modelu”.
- **Bezlični pasiv u aktiv („mi”) (oko 8)**: „pretpostavljaju se …” → „pretpostavljamo …”, „Time se izvodi” →
  „Time dobivamo”, „primjenjuje se kontinuumski model” → „primjenjujemo …”.
- **Sročnost i padeži (3)**: „potreban najmanje $n=9$ punih hodova” → „potrebno je najmanje …”;
  „ima … silu $F_p$” (crpka) → „na njezin klip djeluje sila $F_p$”; „Odluči prolazi li taj kriterij”
  → „je li taj kriterij zadovoljen”.
- **Razbijene ili preoblikovane predugačke rečenice (5)**: tetraedar (rečenica od 45 riječi i izraz
  bez glagola „Ravnoteža sila po osi $x$ (uz zanemarivanje težine …):”), kočnica (lanac s točkom
  sa zarezom), procjena stlačivosti u primjeru dizalice, uvod CFD-a o preši.
- **Nazivlje (2)**: „hidrostatska razlika” → „hidrostatička” prema `docs/urednicki_stil.md`.
- **Zarezi i interpunkcija (oko 4)**: zarez ispred „pa”, točka sa zarezom pretvorena u zarez ispred „a”.
- **Ostalo**: „Slika ispod” → „Sljedeća slika” (PDF može pomaknuti sliku), „pa je sila” iza
  formule koja završava točkom → nova rečenica „Sila na velikom klipu stoga je”.

### Primjeri „prije → poslije”

1. „Ručni @ex-u01-servisna-hidraulicna-dizalica-t2 pretpostavlja sporo podizanje …” →
   „Ručna dizalica iz primjera [-@ex-u01-servisna-hidraulicna-dizalica-t2] pretpostavlja sporo podizanje …”
2. „pa je za podizaj **barem** 25 mm potreban najmanje $n=9$ punih tlačnih hodova” →
   „pa je za podizaj od **barem** 25 mm potrebno najmanje $n=9$ punih tlačnih hodova”
3. „Ravnoteža sila po osi $x$ (uz zanemarivanje težine, koja je razmjerna volumenu … kada $\ell \to 0$):” →
   „Težinu zanemarujemo: razmjerna je volumenu, $\propto \ell^3$, pa kada $\ell \to 0$ iščezava brže od
   tlačnih sila, koje su razmjerne površinama, $\propto \ell^2$. Ravnoteža sila u smjeru osi $x$ tada glasi”
4. „Za odziv cijele instalacije često najprije dostaje jednostavniji dinamički model; CFD se koristi za dio
   čiji prostorni tok bitno utječe na odgovor.” → „Za odziv cijele instalacije u početku je često dovoljan
   jednostavniji dinamički model, a CFD primjenjujemo na dio u kojem prostorna slika strujanja bitno utječe na odziv.”
5. „Ćelija predstavlja dio kontinuuma, a ne molekulu. Isti krug dalje proširujemo …” →
   „Ćelija je dio kontinuuma, a ne molekula. Taj krug u nastavku proširujemo …”
6. „Ručna crpka ima klip površine $A_p$, silu $F_p$ i puni tlačni hod $s_h$.” →
   „Ručna crpka ima klip površine $A_p$ i puni tlačni hod $s_h$, a na njezin klip djeluje sila $F_p$.”
7. „Odabire se 9 mm; 8 mm ne zadovoljava hod, a 10 mm silu.” →
   „Odabire se promjer 9 mm: uz 8 mm nije zadovoljen uvjet hoda, a uz 10 mm uvjet sile.”
8. „Time se razlikuju ulazni podatci modela od njegova rezultata. Promjena boje prikazanoga polja ne može
   nadomjestiti pogrešno zadana svojstva.” → „Zato valja razlikovati ulazne podatke modela od njegova
   rezultata. Drukčije obojeno polje u prikazu ne ispravlja pogrešno zadana svojstva.”

## 2. Sadržajni nalazi koje nisam ispravio

Svi brojčani rezultati u primjerima i kontrolnim rezultatima Z1–Z6 ručno su preračunani i slažu se
(npr. 179 kPa / 8,06 kN; 0,0463 %; $n=9$, 27,0 mm, 60 mm; 4,77 MPa, 4,59 / 3,38 kN, $k\approx53$;
2,73 MPa, 1,68 kN; Z4 9,80 mm i 2,0 %; Z5 parovi $(F_p,s_p)$; Z6 22,1 kN i 1,55 m).

1. **Sukob oznake $F_n$** (r. 5, 40–46 i r. 479): $F_n$ je u teoriji normalna (tlačna) sila u $p=F_n/A$,
   a u primjeru kočnice sila vozača na papučicu („silom $F_n = 300\ \text{N}$”). Predlažem drugu oznaku
   za silu na papučici (npr. $F_{pap}$ ili $F_v$). U formulama nisam ništa mijenjala.
2. **Engleski indeksi u primjeru kočnice** (r. 479–545): $d_f$, $d_r$, $A_f$, $F_r$ (engl. front/rear),
   a indeks $M$ (glavni cilindar: $d_M$, $A_M$, $F_M$) vizualno se sudara s $p_M$ (manometarski tlak)
   u istom primjeru. Standard nazivlja traži hrvatske indekse. Mogući su npr. $pr$/$st$ i $gc$.
3. **Uvod Z1–Z6 i Z2** (r. 632 i 669): uvod kaže „Sile djeluju izravno na klipove, bez dodatnog
   prijenosa polugom”, a Z2 sile s klipova prenosi preko ruda (krak $r=0{,}60$ m) u moment. Tvrdnja
   o silama na klipovima ostaje točna, ali je moguća zabuna; možda valja dodati ogradu „osim ruda u Z2”.
4. **$p$ prema $\Delta p$** (r. 7 i 122–126): uvod piše $p=F_1/A_1=F_2/A_2$, a odjeljak o Pascalovu
   zakonu i izvod $\Delta p = F_1/A_1 = F_2/A_2$ (porast tlaka uz vanjske strane na atmosferi).
   Nije pogreška (u uvodu je riječ o manometarskom tlaku), ali bi bilo dosljednije koristiti $\Delta p$ ili $p_M$.
5. **Suvišan razmak ispred `&nbsp;` u naslovima primjera** (r. 474 i 554): „… kočnih cilindara &nbsp;<span …”
   i „… električnog vozila &nbsp;<span …”. Nisam dirala jer naslovi ulaze u ključ D06, a generatore ne smijem pokretati.
6. **Sitnica u formuli** (r. 596): $F_{uk} = 6 \cdot 1{,}680 \approx 10{,}08$, gdje je umnožak točan
   pa bi trebalo stajati „=”. Nisam mijenjala jer je unutar matematike.
7. **Oznaka $F_G$ za podiznu sposobnost** (primjer platforme r. 406–436; Z6 r. 804–817): $F_G$ (težina)
   označuje i „ukupnu idealiziranu podiznu silu”. Tekst to izjednačuje s najvećom težinom tereta, pa je
   prihvatljivo, ali je granično prema standardu „$F_G$ = težina”.
8. Naslov „## Zadaci za vježbu” nema `{#id}` pa je ostao s „Zadaci”, iako knjiga inače piše „zadatci”.

## 3. Provjere

- `lektura_check.py source/u01_osnove_fluida_i_pascalov_zakon.md`: **ok**, izlazni kod 0. Nema
  redaka STROGO, `provjeri numbers` ni `provjeri refs`.
- `tools/check_u01_sketch_geometry.py`: **U01 SVG PASS** (7 slika).
- `tools/audit_publication.py`: **Publication audit PASS** (U01: 6 primjera, Z1–Z6 [T1,T1,T2,T2,T3,T4]).
- Generatori, render i git naredbe nisu pokretani. SVG-ovi i generirane datoteke nisu dirani.
