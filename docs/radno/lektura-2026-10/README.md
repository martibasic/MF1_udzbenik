# Lektura priručnika — 16. listopada 2026.

Jezična i stilska lektura svih poglavlja (1–15), uvoda, predgovora i dodataka A–E.
Svaka datoteka ima svoj izvještaj s primjerima „prije → poslije” i popisom sadržajnih
nalaza koji nisu ispravljani. Ključ rezultata (D06) obnovljen je generatorom.

## Pravila provedbe

- Mijenjan je samo jezik: padeži, sročnost, red riječi i enklitike, zarezi, kalkovi,
  nespretni izrazi, preduge rečenice, nazivlje prema `docs/urednicki_stil.md`.
- Formule, brojevi, oznake, ID-jevi, polja zadataka i struktura nisu mijenjani; to je
  provjereno usporedbom svake datoteke sa snimkom prije lekture (matematika, brojevi
  izvan formula, ID-jevi, atributi, ograde, polja, razine).
- Upućivanja u kosom padežu („u primjer 7.6”, „prema jednadžba 9.20”) zapisana su kao
  imenica u ispravnom padežu i broj bez prefiksa (`u primjeru [-@ex-…]`). Filtar
  `filters/mf1-components.lua` sada poštuje oblik `[-@id]` i za primjere i zadatke.

## Izmjene izvan čiste lekture

- `\leqs` → `\leq s` u pog. 9, Z6 (formula se nije ispisivala; ostatak zamjene u(x) → s(x)).
- Ostaci engleskih indeksa prema odluci od 15. listopada: `|_w` → `|_{st}` (pog. 12),
  `(\partial v_t/\partial n)_w` → `_{st}` (D04), `h<sub>w</sub>` → `h<sub>g</sub>` (D03).
- Ujednačen zapis $\vec g_{eff}$ (umjesto `\vec g_{\mathrm{eff}}`) u u00, u03 i u04.
- Pog. 10, „Postupak rješenja”: pokvaren zapis „($v = $ konst.)” i stopljen popis
  prepisani u ispravnu prozu i popis; isto za telegrafski redak „Korak: …” u pog. 11.
- Tri rečenice u pog. 9 i 10 preslagane su tako da upućivanje na jednadžbu ne završava
  redak u PDF-u (audit ga inače čita kao broj jednadžbe).

## Sadržajni nalazi za odluku autorice

Najvažniji su izdvojeni u nastavku; potpuni popis je u izvještajima po datotekama.

| Pog. | Nalaz |
| --- | --- |
| 5 | Z2, kontrolni rezultat: „$F_x$ i $F_z$ ne poništavaju momente ni oko jedne točke” fizikalno je netočno (poništavaju se oko točaka na pravcu rezultante). |
| 12 | Primjer trupa modela: $(1{,}08\cdot10^7)^{1/5}=25{,}5$, a ne 25,2; zato $\delta\approx0{,}087$ m (ne 0,088 m). |
| 6 | Bočni tank (T4): $T_1$ 3,477 m prema 3,478 m; $\Delta T$ 0,225 m prema 0,226 m. |
| 10 | Y-račva: iz napisanih 664 i 625 N slijedi 911,9 N ≈ 0,912 kN (piše 0,913); veže se na rezervu 87 N i D06. |
| 13 | Z2, naputak: „razlikuju se samo $Re$” — razlikuju se i gustoće. Z6: $NPSH_r(q,n_2)$ vjerojatno treba $Q$. |
| 7 | „Porast od 6,6 % jednak je omjeru 16/15” — porast je 16/15 − 1. |
| 11 | Nakon omjera snaga $\lambda_L^{7/2}$ „a ne faktorom $\lambda_L^3$” (to je faktor sile). Z3: negativni „pretlak” je podtlak. |
| 2 | Opis Weberova i Bondova broja imao je obrnut smjer omjera; preoblikovan u „inercija (gravitacija) prema površinskoj napetosti” — potvrditi. |
| 14 | Eulerov izraz i $F_x u$ jednaki su samo za kolo ($\dot m$ prema $\dot m_{rel}$); „nekonvergirana mreža” → nekonvergirano rješenje. |
| A | Jedinice $k$, $\varepsilon$, $\omega$, $\ell$ u D01 označene su s „-” (trebaju m²/s², m²/s³, s⁻¹, m). |
| više | Preostale nedosljednosti notacije: $K$ (volumni modul i kobilica), $M$ (metacentar i moment), $v_s$ (brzina broda i usisni presjek), $h_v$/$h_u$ u drugom značenju (pog. 4, 13), $H_t$ kao visina tanka (pog. 3), $p_0$ kao manometarski tlak (pog. 9). |
| više | Naziv poglavlja 5 „Hidrostatske sile…” prema nazivlju „hidrostatički”; „podkritični/nadkritični” prema pravopisnom „potkritični/natkritični”. |

Brojčani nalazi nisu ispravljani jer mijenjaju objavljene rezultate, verifikatore i D06.
