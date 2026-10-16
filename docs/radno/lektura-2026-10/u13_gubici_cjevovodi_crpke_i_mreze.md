# Lektura: source/u13_gubici_cjevovodi_crpke_i_mreze.md (pog. 13)

Prođena cijela datoteka (921 redak): uvod, teorija, izvod, CFD i numerički blokovi,
šest riješenih primjera, samoprovjera, Z1–Z6 s naputcima i kontrolnim rezultatima,
opisi slika i sažetak. Izmijenjeno je 75 redaka. Matematika, brojevi, ID-jevi i polja
nisu dirani.

## 1. Vrste izmjena (približno)

- Upućivanja s krivim padežom ili bez imenice (`u [-@eq]`, `iz [-@eq]`, `prema [-@eq]`,
  `pa [-@eq] daje`): 11
- „predstavlja / je” → „jest / iznosi / nisu”, „jesu” → „iznose”: 12
- Kalkovi i nespretni izrazi („fiksni”, „konstantni” → „stalni”; „nema nužno”;
  „izvijesti”; „riješi radnu točku”; „crpna visina”; „energetski”; „ventilska disipacija”): 14
- Padeži, sročnost i oblici („po oba puta” → „po obama putovima”, „u oba presjeka”,
  „više petlja” → „više petlji”, „razmjeran s” → „razmjeran omjeru”, „određenoj s” →
  „određenoj omjerom”, „ih se ne smije” → „ne smiju se”): 9
- Red riječi i enklitike („odsječka se ne mijenja” → „odsječka ne mijenja se”,
  „Za opću mrežu zato se” → „Zato se za opću mrežu”): 5
- Razbijena spojena rečenica (zarezni niz u uvodu) i dopune nedovršenih konstrukcija
  („i ponavlja” → „i ponavlja se iteracija”, „može zapisati” → „može zapisati kao”): 6
- Zarez ispred „jer” uklonjen, nazivlje usklađeno („prianjanje uz stijenke”,
  „visina dobave”, „bilance u čvorovima”, „odljev” umjesto „odtok”): 8
- Ostalo (jasniji naslov polja „Najčešća pogreška” imenskim oblikom, napomene uz skice): 10

### Reprezentativni primjeri

1. „Uvrštavanjem u [-@eq-darcy-weisbach] dobiva se” → „Uvrštavanjem u jednadžbu [-@eq-darcy-weisbach] dobiva se”
2. „Kota $H$ … za prikazanu mrežu predstavlja ukupnu raspoloživu visinu, koju energijska crta (EGL) troši u tri dijela” → „… jest ukupna raspoloživa visina, koja se duž energijske crte (EGL) troši u tri dijela”
3. „Zato ne mogu imati različitu razliku ukupne energijske visine.” → „Zato razlika ukupne energijske visine između njihovih krajeva mora biti ista.”
4. „Colebrookovu relaciju ne dodajemo kao novu silu na otpor koji je već dobiven …” → „Otporu koji je već dobiven iz naprezanja u CFD domeni ne dodajemo Colebrookovu relaciju kao novu silu.”
5. „Ventilska disipacija dio je hidrauličke snage, dok su gubitci motora i crpke razlike između različitih razina pretvorbe.” → „Disipacija na ventilu dio je hidrauličke snage, a gubitci motora i crpke razlike su između pojedinih razina pretvorbe.”
6. „Ukupna učinkovitost električna–hidraulička pretpostavlja se jednakom $\eta=0{,}70$ u obje uspoređene točke” → „Ukupna učinkovitost pretvorbe električne u hidrauličku snagu pretpostavlja se jednakom $\eta=0{,}70$ u objema uspoređenim točkama”
7. „a tlak pare mora na $30\ \mathrm{^\circ C}$ $p_v=4{,}2\ \mathrm{kPa}$” → „a tlak pare morske vode pri $30\ \mathrm{^\circ C}$ iznosi $p_v=4{,}2\ \mathrm{kPa}$”
8. „**Najčešća pogreška.** Zbrajati lokalne koeficijente … ili afinitetne zakone primijeniti …” → „Zbrajanje lokalnih koeficijenata … ili primjena afinitetnih zakona …”

Dvije male jezične preciznosti koje lagano mijenjaju naglasak (molim autoričinu potvrdu):
- Z3, naputak: „Prigušenje može povećati otpor, pa ne smiješ dobiti negativan $R_v$” →
  „Prigušenje otpor može samo povećati, pa $R_v$ ne smije ispasti negativan.” (usklađeno s uvjetom $R_v\ge0$)
- Primjer petlje: „promjeri cijevi uvećani su prema duljinama” → „promjeri cijevi nacrtani su
  uvećano u odnosu na duljine” (protumačeno kao napomena o mjerilu skice).

## 2. Sadržajni nalazi koje nisam ispravio

1. **R. 900 (Z6, kontrolni rezultat):** „$NPSH_r(q,n_2)$ za sniženu brzinu”. Malo slovo $q$
   prema notacijskoj tablici označuje protok po širini (samo pog. 15). Vjerojatno treba
   $NPSH_r(Q,n_2)$. Ispravak je u formuli, pa ga nisam napravio.
2. **R. 794 (Z3):** „novi ventil dodaje $h_v=R_vQ_i^2$”. Oznaka $h_v$ u notacijskoj tablici
   rezervirana je za sloj vode ($h_v$, $h_u$). Prijedlog: $h_{g,V}$ ili $h_{V}$. U istom zadatku
   traži se „zajednički gubitak $h_{AB}$”, a čvorovi A i B nisu imenovani u tekstu
   („između istih čvorova”). Treba provjeriti označuje li ih skica.
3. **R. 776 (Z2, naputak):** „Brzina je ista za oba fluida; razlikuju se samo $Re$.” Fluidi
   imaju i različite gustoće (1080 i 998 kg/m³), a o gustoći ovisi $\Delta p$. Riječ „samo” je
   netočna, ali je nisam brisao jer je to sadržajna tvrdnja.
4. **R. 602–616 (primjer godišnje energije):** visina se označuje s $H$, a snaga s
   $P_h=\rho gQH$. U odjeljku i u notacijskoj tablici visina dobave crpke je $H_p$
   ($P_h=\rho gQH_p$). Ovo je manja nedosljednost notacije.
5. **R. 27:** „disipacija se zapisuje pozitivnim članom $h_g\ge0$”. Ispravno bi bilo
   „nenegativnim”, jer je jednakost dopuštena. Tekst sam ostavio jer se tiče ograde.
6. **R. 278:** „nastavci zasebno obrađuju Z3 i Z6” u bloku o paralelnim granama. Z6 je
   zadatak o regulaciji balastne crpke i NPSH-u, a ne o paralelnim granama. Treba provjeriti
   sadrži li bilježnica `u13_paralelne_grane.ipynb` doista nastavak za Z6.
7. Napomena bez pogreške: slika u r. 73 i bilježnica u r. 215–217 nose prefiks `u10_`
   (`u10_fig_uvod_pregled.svg`, `u10_moody_dijagram.ipynb`). Koristi ih samo ovo poglavlje,
   pa je riječ o starom imenovanju, a ne o krivoj slici.

Brojeve u svim riješenim primjerima i kontrolnim rezultatima Z1–Z6 provjerio sam ručno
(primjeri: gubitci dionice, laminarni vod, Hardy–Cross, radna točka, godišnja energija,
NPSH; zadatci: Z1, Z2, Z3, Z4 u snagama, Z5 za 100 mm i Z6). Svi su konzistentni.

## 3. Provjere

- `lektura_check.py source/u13_gubici_cjevovodi_crpke_i_mreze.md`: **ok**, izlazni kod 0
  (nema STROGO redaka ni razlika u brojevima ili upućivanjima).
- `tools/check_u13_sketch_geometry.py`: **U13 SVG PASS** (uz `PYTHONIOENCODING=utf-8`;
  bez te varijable skripta pada na ispisu znaka „č” u konzoli cp1252, što nema veze s lekturom).
- `tools/audit_publication.py`: **Publication audit PASS** (U13: primjeri=6, zadatci=6
  [T1,T1,T2,T2,T3,T4]).
