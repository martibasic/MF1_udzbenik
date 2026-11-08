# Simulirano čitanje — poglavlje 13 (Gubitci, cjevovodi, crpke i mreže)

Ovo je simulirano čitanje (agent u ulozi studenta), a ne studentski pilot sa
stvarnim studentima. Čitan je samo PDF poglavlja (18 stranica, izvorne
str. 245–262); ključ rezultata otvoren je tek nakon što su modeli i rezultati
za Z3 i Z6 bili zapisani. Mjesta su navedena kao stranica PDF-a poglavlja
(1–18) i oznaka.

Predznanje: poglavlja 1–12 obrađena na predavanjima (svojstva fluida,
hidrostatika, kontinuitet, Bernoullijeva i energijska jednadžba, količina
gibanja, dimenzijska analiza, laminarni tok i granični sloj).

Ograničenje simulacije: u PDF-u su rješenja riješenih primjera odmah ispod
teksta zadatka, pa je „prvi korak prije rješenja” zapisan nakon čitanja teksta
zadatka, ali uz rješenje u vidnom polju. Procjena poklapanja zato je
vjerojatno blaža nego kod stvarnog studenta.

## Procjena vremena

Oko 11–12 sati, što se slaže s navedenih 12 sati: teorija 3–4 h (Colebrook,
Hardy–Cross i NPSH čitao bih dvaput), riješeni primjeri oko 2 h, zadatci
Z1–Z6 oko 5–6 h (Z4 traži alat i iteraciju, Z6 je dug).

## Tri mjesta gdje bi student najvjerojatnije odustao ili pogriješio

1. **Afinitetno skaliranje cijele krivulje crpke (str. 8, odjeljak 13.5; str. 12, P4; str. 17, Z6).**
   Teorija navodi samo Q ∝ n, H ∝ n², P ∝ n³ i upozorava da se to ne prenosi
   na sustav sa statičkom visinom. Kako se iz toga dobije nova krivulja
   H_p,2(Q) = s²·H_p(Q/s) prvi put vidim tek u rješenju P4, jednadžba (13.45),
   bez objašnjenja zašto se u zagradi pojavljuje Q/s. Za Z6 to je ključni korak.
   Bez P4 bih, kao i većina, skalirao samu radnu točku (s = Q₂/Q₁), dakle
   upravo ono na što poglavlje upozorava.
2. **Upućivanja koja ne vode na pravo mjesto (str. 7).** „primjer 13.3” i
   „primjer 13.4” znače P3 i P4, ali primjeri su označeni P1–P6, a (13.3) je
   jednadžba disipacije, pa sam prvo tražio jednadžbu. U „Numeričkom pokusu”
   piše da „nastavci zasebno obrađuju Z3 i Z6”, a Z6 nema paralelnih grana
   (riječ je o balastnoj crpki), pa sam u Z6 tražio paralelni spoj.
3. **Otvoreni dio Z6.3 i „NPSH_a s apsolutnim tlakom” (str. 17, Z6).**
   „S apsolutnim tlakom” pročitao sam kao zahtjev da izračunam p_aps,s.
   Promjer usisa nije zadan, pa brzinsku visinu nisam mogao odrediti i
   neko sam vrijeme tražio podatak kojeg nema. Tek sam onda shvatio da treba
   (13.28) s apsolutnom referencom. U pitanju „koji podatci nedostaju” ključ
   očekuje i uvlačenje zraka pri njihanju i trimu broda. To u poglavlju nigdje
   nije spomenuto: ni u „Granici modela” na str. 9 ni u tekstu o NPSH-u. Iz
   teksta to nisam mogao zaključiti.

## Riješeni primjeri (korak 2)

| Primjer | Moj model i prvi korak | Poklapanje | Napomena |
|---|---|---|---|
| P1 (str. 9–10) | Darcy–Weisbach + Σξ uz istu brzinu, zatim Δp = ρg·h_g jer je cijev vodoravna | da | Jednostavno; provjera unatrag korisna. |
| P2 (str. 10) | v = Q/A, Re, zatim odluka laminarno → 64/Re | da | Usporedba s (13.13) dobro provjerava faktor 64. |
| P3 (str. 10–12) | Otpori R_i iz (13.17), početna raspodjela koja zadovoljava čvorove, zatim ΔQ iz (13.19) | da, osim početnih brojeva | Ja bih izabrao drugu početnu raspodjelu. Rješenje kaže da je bilo koja dobra, pa to nije problem. Oznake h_DC i h_AD u završnoj provjeri pišu se suprotno od obilaznog smjera (CD, DA) pa sam predznake slagao dvaput. |
| P4 (str. 12) | Presjecište H_p = H_s; za brzinu bih krenuo sa s = 17,24/19,94 | ne (drugi dio) | Rješenje pokazuje zašto to ne valja. Transformaciju H_p,2(Q) = s²H_p(Q/s) iz teksta nisam mogao znati (v. mjesto 1). Ponovio sam račun: s = 0,899. |
| P5 (str. 12–13) | Lanac P_h → P_vr → P_el, E = P_el·t | da | Zastao sam na tekstu: kako crpka pri istom protoku daje manju visinu (12 → 10 m)? Pretpostavljam da pretvarač snizi brzinu, ali to nije rečeno, a isto tako ni zašto učinkovitosti ostaju iste. |
| P6 (str. 13) | Bernoulli od slobodne površine do S, zatim (13.27) i provjera s (13.28) | da | Dvostruki zapis je pomogao da razumijem rečenicu sa str. 9 o „pokraćenoj” brzinskoj visini. |

## Riješeni zadatci (korak 3)

### Z3. Uravnoteženje paralelnih grana (T2, str. 16)

- **Model prije računa.** Sustav: dvije grane između čvorova A i B. Zakoni:
  kontinuitet u čvoru (Q = Q₁ + Q₂) i jednak pad energije između zajedničkih
  čvorova. Kvadratni model h = RQ² s ventilom kao dodatnim R_v u seriji u
  jednoj grani. Pozitivni smjer od A prema B. Tlakove ne trebam jer radim s
  padom energijske visine. Pretpostavke: R_i stalni (potpuno turbulentno),
  stacionarno. Granica modela: ako se λ mijenja s protokom, R_i nisu stalni.
  Predviđanje: ventil ide u granu 1 jer manji otpor bez ventila nosi veći
  protok (str. 7, „Fizikalno značenje”). h_AB će narasti u odnosu na stanje
  bez ventila i bit će reda nekoliko metara.
- **Moj rezultat.** Bez ventila: Q₁ = 13,33 L/s, Q₂ = 6,67 L/s, h_AB = 2,13 m.
  S ventilom: Q₁ = Q₂ = 10,00 L/s, h_AB = R₂Q₂² = 4,80 m, R₁ + R_v = 48 000,
  dakle R_v = 36 000 s²/m⁵, a sam ventil daje h_g,V = 3,60 m (1,20 m otpada
  na postojeću granu 1). Kontinuitet 10 + 10 = 20 L/s; oba puta daju 4,80 m.
- **Kontrolni rezultat.** Grana 1, R_v = 36 000 s²/m⁵, Q₁ = Q₂ = 10,00 L/s,
  h_AB = 4,80 m, h_g,V = 3,60 m.
- **Podudaranje:** da.
- **Gdje sam zapeo.** Nigdje bitno. Ovo mi je bio „lagani T2”: odluka o grani
  slijedi izravno iz „Fizikalnog značenja” na str. 7. Usporedba sa stanjem
  bez ventila nije tražena, ali sam je napravio da vidim zašto regulacija
  mora „osigurati potrebnu visinu” (2,13 → 4,80 m). Smjernica u ključu
  (R_v ≥ 0) pomaže i ne otkriva rješenje.

### Z6. Regulacija balastne crpke i usisna rezerva (T4, str. 17)

- **Model prije računa.** Sustav: crpka s usisom kroz koš u oplati i potisom u
  tank. Zakoni: radna točka H_p(Q) = H_s,V(Q); snaga P_el = ρgQH/η; afinitetno
  skaliranje cijele krivulje crpke (prema P4); usisna bilanca (13.28) od vodne
  linije do S. Referenca tlaka: apsolutna (p_atm i p_v). Pozitivni smjerovi:
  z_s prema gore, pa je napunjen usis z_s < 0. Pretpostavke: Q u L/s u
  krivuljama, a u m³/s u snazi; η = 0,70 u objema točkama; h_g,s jednak u
  oba načina regulacije jer je Q isti. Granica modela: NPSH_r vrijedi samo pri
  nazivnoj brzini; jednodimenzijski stacionarni model ne vidi uvlačenje zraka.
  Predviđanje: regulacija brzinom troši manje energije (statička visina 4 m
  ne skalira se, pa je s veći od omjera protoka); NPSH_a > 10 m jer je usis
  napunjen.
- **Moj rezultat.**
  1. 22 − 0,010Q² = 4 + 0,026Q² → Q² = 500, Q = 22,36 L/s, H_V = 17,00 m;
     P_el = 5,46 kW, E_V = 8,19 MWh/god.
  2. H_s = 4 + 0,015·500 = 11,50 m; 22s² − 0,010·500 = 11,5 → s² = 0,75,
     s = 0,866; P_el = 3,69 kW, E_s = 5,54 MWh/god, ΔE = 2,65 MWh/god (oko 32 %).
  3. p_atm/(ρg) = 10,07 m, p_v/(ρg) = 0,42 m; NPSH_a = 10,07 + 1,8 − 1,4 −
     0,42 = 10,06 m; NPSH_r = 2,5 + 0,004·500 = 4,50 m; razlika 5,56 m.
     Uz z_s = −0,4 m: NPSH_a = 8,66 m (uz isti h_g,s i p_v). Nedostaju po mom
     sudu: margina/kriterij proizvođača, NPSH_r pri sniženoj brzini,
     najviša temperatura mora (p_v), stanje filtra/koša (h_g,s raste).
- **Kontrolni rezultat.** Q ≈ 22,36 L/s; (H_V, H_s) ≈ (17,00; 11,50) m;
  s ≈ 0,866; (E_V, E_s, ΔE) ≈ (8,19; 5,54; 2,65) MWh/god; (NPSH_a, NPSH_r,
  razlika) ≈ (10,06; 4,50; 5,56) m; u balastnom stanju 8,66 m. Nedostaju:
  margina proizvođača, NPSH_r(Q, n₂), porast h_g,s zbog zaprljanog filtra i
  provjera uvlačenja zraka pri njihanju i trimu.
- **Podudaranje:** da, za sve brojeve. U otvorenom dijelu nisam naveo uvlačenje
  zraka pri njihanju i trimu, a dodao sam temperaturu mora, koju ključ ne
  navodi.
- **Gdje sam zapeo.** (a) Formula H_p,2(Q) = s²H_p(Q/s): imao sam je samo zato
  što sam prije čitao P4. (b) „NPSH_a s apsolutnim tlakom”: tražio sam promjer
  usisa za p_aps,s (v. mjesto 3). (c) Hoće li „h_g,s pri protoku prigušenog
  sustava” vrijediti i za regulaciju brzinom: zaključio sam da hoće jer je Q
  isti, ali to bi moglo biti rečeno. Naputka uz zadatak u poglavlju nema.
  Smjernica u ključu je korisna, ali u njoj piše „prema jednadžbi odgovarajući
  izraz” umjesto broja jednadžbe.

## Pitanja „Predvidi”, „Zastani i promisli” i „Provjeri sebe” (korak 4)

Poglavlje nema okvira „Provjeri sebe”.

- **Str. 6, Predvidi (hrapavost i Z4).** Moj odgovor: veći k_s/D daje veći λ,
  krivulja sustava postaje strmija, pa Q pada, a H raste. Provjerava
  razumijevanje, ali upućuje na Z4 prije nego što ga student vidi.
- **Str. 7, Predvidi (koja grana preuzima najveći protok).** Moj odgovor:
  grana najmanjeg R. Bez zadanih grana pitanje je općenito i odgovor je
  gotovo napamet.
- **Str. 7, Zastani i promisli (jednak pad, različiti protoci, kontinuitet).**
  Moj odgovor: nije narušen jer kontinuitet traži samo zbroj protoka u čvoru.
  Provjerava razumijevanje, ali odgovor stoji odmah ispod pa ga je lako
  pročitati prije razmišljanja.

## Nejasnoće po težini

### P1

Nema mjesta na kojem nisam mogao nastaviti.

### P2

- **Str. 8, 13.5; str. 12, P4.** Transformacija krivulje crpke
  H_p,2(Q) = s²H_p(Q/s) nije izvedena u teoriji. Jedna rečenica bi bila
  dovoljna: točka (Q, H) prelazi u (sQ, s²H). Potrebna je za Z6.
- **Str. 7.** „primjer 13.3” i „primjer 13.4” odnose se na P3 i P4, a
  (13.3) je i broj jednadžbe. Uz to „nastavci zasebno obrađuju Z3 i Z6”, a Z6
  nije o paralelnim granama.
- **Str. 17, Z6.3.** „Odredi NPSH_a s apsolutnim tlakom” može se pročitati kao
  zahtjev za p_aps,s, a promjer usisa nije zadan. Otvoreni dio očekuje
  uvlačenje zraka pri njihanju i trimu, a toga nema u poglavlju.
- **Str. 4 i str. 16 (Z4).** Nema tablice tipičnih ξ ni objašnjenja da je
  izlaz u veliki spremnik gubitak s ξ = 1. Z4 piše „Σξ = 6,0, uključujući
  ulaz i izlaz”, a ja ne bih znao bi li izlaz trebalo brojiti posebno ili je
  to kinetička energija.
- **Str. 6.** Moodyjev dijagram se spominje („može se očitati”), ali nije
  prikazan, nego je samo na QR kodu. Iz tiskane knjige ne mogu vidjeti
  područja režima.
- **Str. 12, P5.** Pad visine dobave s 12 na 10 m pri istom protoku i istim
  učinkovitostima nije objašnjen. Ista crpka pri istoj brzini dala bi veći
  protok. Pretpostavljam sniženje brzine, ali to bi trebalo reći.

### P3

- **Str. 2.** NPSH se spominje u bilanci (13.1) prije nego što je definiran
  (str. 8).
- **Str. 3, slika 13.2.** U panelu „Linijski gubitak” nisam shvatio što su dva
  tamna odsječka uz stijenku desno. Ventil je nacrtan iznad cijevi, a ne u
  njoj; uz oznaku „(simbol)” to je razumljivo.
- **Str. 4, okvir CFD.** „kao u ranijem Venturijevu primjeru” ne kaže koji je
  to primjer ni u kojem poglavlju.
- **Str. 6 i str. 7.** Oznake A, B su u slici 13.1 spremnici, a u (13.18) i Z3
  čvorovi. To me na trenutak zbunilo.
- **Str. 8, 13.5.1.** Rečenicu o disipaciji na ventilu i električnoj snazi
  čitao sam dvaput.
- **Str. 9.** Rečenicu o tome da se brzinska visina „pokrati” u drugom zapisu
  razumio sam tek nakon P6.
- **Ključ, Z5 i Z6.** „iz jednadžbe odgovarajući izraz” i „prema jednadžbi
  odgovarajući izraz”: broj jednadžbe nedostaje.

## Što mi je najviše pomoglo

- Slijed Q → v → Re → λ → h_g (13.9) i sažetak na str. 17: jasan recept.
- „Fizikalno značenje — Što se izjednačuje?” (str. 7): iz njega sam izravno
  riješio Z3.
- P4 s eksplicitnim upozorenjem da omjer brzina nije omjer protoka. Bez
  njega bih pogriješio u Z6.
- P6 s dvostrukom provjerom NPSH_a (13.27 i 13.28) i jasna konvencija
  predznaka z_s (str. 9 i napomena uz sliku 13.4).

## Što ova simulacija ne dokazuje

Rezultati Z3 i Z6 poklapaju se s ključem, ali to pokazuje samo da su tekst
zadatka i ključ dosljedni za čitatelja koji je prethodno pažljivo pročitao P4
i P6. Ne pokazuje koliko bi stvarni studenti zapeli. Procjene P2/P3 i
vremena su procjene simuliranog čitatelja.
