# Lektura: index.md, u00, d01, d02, d05 (zajednički izvještaj)

Datoteke: `source/index.md`, `source/u00_kako_koristiti_udzbenik.md`,
`source/d01_sazetak_formula_i_oznaka.md`, `source/d02_pojmovnik.md`,
`source/d05_literatura.md` (u d05 samo uvodni tekst; bibliografski zapisi nisu dirani).
Sve izmjene napravljene su alatom Edit. Matematika, ID-jevi, atributi, poveznice i
citati nisu mijenjani.

## 1. Izmjene

| Datoteka | Približan broj zahvata | Vrste |
| --- | --- | --- |
| index.md | 8 rečenica | kalkovi („Primarna su publika”), nominalni nizovi, nazivlje (hidrostatički, modelska ispitivanja), dosljednost „kad” |
| u00 | 14 rečenica | dvosmislen imperativ („slijedi glavni tekst”), kalk „kroz” (petnaest poglavlja, cijeli priručnik), „automatski”, nespretni glagoli („uspostavljaju”), red riječi, elipse bez glagola |
| d01 | 33 ćelije ili rečenice | telegrafski izrazi kojima nedostaje imenica ili glagol, prijedlozi (u smjeru normale, na lopatici), „vezano uz”, „težinjen” → „ponderiran” (kao u pog. 6 i 8), „kada” → „kad” |
| d02 | 45 definicija i 1 okvir | pasiv („nije nadjačan”), dvosmisleni „koji”, „po jedinici volumena/površine”, „u kojoj” (točka), „debalans” → „neravnoteža”, „zadnji” → „posljednji”, „znak” → „predznak”; **redoslijed abecede** (vidi niže) |
| d05 | 7 rečenica | „Granični sloj … mogu se produbiti” → gradivo; „vezati uz postupak” → „provoditi prema”; „SOLAS zahtjeve” → „zahtjeve konvencije SOLAS”; upućivanje `@ex-…` u kosom padežu |

Reprezentativni primjeri (prije → poslije):

1. index: „Primarna su publika studenti strojarstva i brodogradnje, a primjeri … koriste se kada isti zakon pokazuju” → „Namijenjen je ponajprije studentima strojarstva i brodogradnje, a primjeri … uključeni su kad isti zakon pokazuju”.
2. index: „Dodatni numerički pokusi omogućuju istraživanje utjecaja podataka i pretpostavki na rezultat.” → „U dodatnim numeričkim pokusima može se istražiti kako podatci i pretpostavke utječu na rezultat.”
3. u00: „Pri prvom čitanju slijedi glavni tekst, riješene primjere i zadatke.” → „Pri prvom čitanju drži se glavnog teksta, riješenih primjera i zadataka.”
4. u00: „Riješeni primjeri uspostavljaju početnu jednadžbu i slijed proračuna.” → „Riješeni primjeri pokazuju kako se postavlja početna jednadžba i kojim slijedom teče proračun.”
5. d01: „istjecanje (*discharge*), preljev; otpor (*drag*), uzgon, tlak” → „koeficijenti istjecanja (*discharge*) i preljeva; otpora (*drag*), uzgona i tlaka”.
6. d01: „predznak $a_z$ iz ubrzanja, ne brzine” → „predznak $a_z$ određuje ubrzanje, ne brzina”.
7. d02: „Uređen režim u kojem viskozni prijenos nije nadjačan turbulentnim miješanjem” → „Uređen režim u kojem turbulentno miješanje ne nadjačava viskozni prijenos”.
8. d05: „omogućuju izravnu usporedbu u @ex-stepenica-mjerenje-cfd” → „omogućuju izravnu usporedbu u primjeru [-@ex-stepenica-mjerenje-cfd]”.

**Redoslijed u pojmovniku (d02).** Tri para bila su izvan abecednog reda pa su retci
premješteni bez promjene sadržaja: „Eulerov broj” sada je ispred „Eulerova jednadžba
turbostroja”, „Froudeov broj” ispred „Froudeova hipoteza”, a „Weberov broj” i
„Young–Laplaceova relacija” stoje između „Volumni modul elastičnosti” i „Zagušenje
sapnice” (W i Y prema latiničnom redu, ispred Z). Ako je autorica namjerno stavila
strana slova na kraj, ta dva retka treba vratiti.

## 2. Sadržajni nalazi koje nisam ispravila

1. **$K$ u dva značenja (d01).** U retku 14 piše „$K$ | volumni modul elastičnosti (samo to značenje)”, a u retku 27 „$B$, $G$, $M$, $K$ | točke … metacentra i kobilice” (te $KB$, $KG$). Isto proturječje postoji u `docs/urednicki_stil.md` („$K$ samo volumni modul”). Ogradu „samo to značenje” treba ublažiti ili dodati iznimku za točku kobilice.
2. **Pogrešne jedinice za veličine RANS-a (d01, redak 40).** „$k$, $\varepsilon$, $\omega$; $I_t$; $\ell$; $m$ | … | -”: bezdimenzijski su samo $I_t$ i $m$. Za $k$ je jedinica m$^2$/s$^2$, za $\varepsilon$ m$^2$/s$^3$, za $\omega$ s$^{-1}$, a za $\ell$ m.
3. **$v_s$ kao usisna brzina (d01, redak 184; d02, redak 45).** U izrazu $NPSH_a=p_{aps,s}/(\rho g)+v_s^2/(2g)-p_v/(\rho g)$ oznaka $v_s$ znači brzinu u usisnom presjeku, a standard oznaka i d01 (redak 31) rezerviraju je za brzinu broda. Potrebna je napomena o iznimci ili druga oznaka.
4. **$\vec g_{\mathrm{eff}}$ prema $\vec g_{eff}$.** U tablici strelica u u00 (redak 59) indeks je uspravan ($\vec g_{\mathrm{eff}}$), a u d01, d02, d03 i u04 kosi ($\vec g_{eff}$).
5. **Akumulacija (d02, redak 10):** „ne nestaje samo zato što su trenutačni ulaz i izlaz jednaki”. Za masu bez izvora jednaki trenutačni maseni ulaz i izlaz daju upravo $dm_{KV}/dt=0$. Tvrdnja vrijedi samo za neku drugu veličinu ili za volumenske protoke uz promjenjivu gustoću. Autorica bi trebala izričito navesti na što misli.
6. **Kavitacijski prag Venturija (d01, redak 144):** $\sigma_{kr}=1-(A_2/A_1)^2$ slijedi samo uz $p_{ref}=p_1$ (ulaz) i $v_{ref}=v_2$ (grlo). Budući da isti redak traži „navedi referentno mjesto”, valjalo bi napisati koje se mjesto ovdje koristi.
7. **$M$ u dva značenja (d01):** u retku 27 $M$ je metacentar, a u retku 38 moment. Kontekst ih razlikuje, ali za razliku od $R$ ili $T$ ta iznimka nije navedena.
8. **$p_b$ (d01, redak 117)** se koristi („zagušenje nastupa kad je $p_b/p_0$ …”), ali u tablici oznaka nije definiran (protutlak).
9. **Ponavljanje u PDF-u (index.md):** uvod vidljiv samo u Typstu (redak 6) i odjeljak „O priručniku” (redak 28) gotovo istim riječima navode publiku i primjere iz drugih područja. Sadržaj nisam uklanjala.
10. **Nazivlje:** „ullage” (d01, redci 20 i 72; d02) ostaje engleski naziv bez hrvatskog para. Izraz „napunjen usis” (d01, redak 184) zadržan je zbog dosljednosti s pog. 13.

## 3. Provjere

- `lektura_check.py` za svih pet datoteka: **ok** (bez redaka STROGO, bez promjena brojeva; refs se podudaraju jer `REF_RE` jednako broji `@id` i `[-@id]`).
- `tools/audit_publication.py`: **PASS** (15 poglavlja, 90 primjera, 90 zadataka, 145 sati).
- `tools/audit_architecture.py`: FAIL zbog „Generated book files are stale: source/d06_kljuc_kontrolnih_rezultata.md”. D06 se generira iz zadataka u poglavljima, a ne iz mojih datoteka, pa uzrok nije ova lektura. Vjerojatno su to izmjene naslova zadataka drugih lektora. Treba ga obnoviti s `python scripts/build_book.py --write` kad svi lektori završe. Taj korak nisam pokretala, prema uputama.
- Upućivanja: `#sec-cfd-venturi` (d04) i `#ex-stepenica-mjerenje-cfd` (u12, primjer) postoje.
