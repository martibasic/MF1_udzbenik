# Interaktivni prikazi (Jupyter bilježnice)

Ova mapa sadrži 17 interaktivnih Jupyter bilježnica koje nadopunjuju
kanonska poglavlja U01–U15. Svaka bilježnica je samostalni numerički pokus:
student najprije predviđa ishod, zatim izvodi račun i naposljetku provjerava
bilancu, granični slučaj, pogrešku, konvergenciju, osjetljivost ili nesigurnost.

## Struktura bilježnice

Svaka bilježnica prati istu akademsku strukturu:

1. **Predvidi** — kvalitativni smjer, predznak ili red veličine prije računa.
2. **Model i pretpostavke** — sustav, jednadžbe i područje valjanosti.
3. **Izračunaj** — ponovljiv račun u Pythonu s knjižnicama dostupnima u pregledniku.
4. **Provjeri** — najmanje dvije neovisne izvršive tvrdnje.
5. **Numerička kvaliteta** — analiza pogreške, konvergencije, osjetljivosti,
   reziduala ili nesigurnosti.
6. **Protumači** — pitanja o fizikalnom značenju i granici modela.

## Pokretanje

### JupyterLite (primarni mrežni put)

Svako kanonsko poglavlje vodi na odgovarajuću bilježnicu u JupyterLiteu, bez
prijave i bez lokalne instalacije. Paket koristi Python/Pyodide u pregledniku i
gradi se u `_site/jlite`. Konfiguracija, hashovi svih 17 bilježnica i pokretanje
kernela provjeravaju se automatizirano; konačni javni artefakt ipak se ne smatra
spremnim dok ne prođe završni proizvodni build aktualnoga commita.

### Google Colab (pričuvni put)

Ako preglednik ili mrežna politika ne podržava JupyterLite, poveznica
*Pričuvno: otvori u Colabu* otvara istu izvornu bilježnicu. Potreban je Google
račun. Veze imaju oblik:

```text
https://colab.research.google.com/github/martibasic/MF1_udzbenik/blob/main/notebooks/<ime>.ipynb
```

### Lokalno pokretanje

Za rad bez interneta potrebne su sljedeće knjižnice:

```powershell
python -m pip install -r requirements.txt
python -m notebook
```

Od vanjskih računskih knjižnica bilježnice koriste samo `numpy` i `matplotlib`,
pa isti račun radi u lokalnom kernelu, Colabu i Pyodide kernelu u pregledniku.

## Popis dostupnih bilježnica

| Oznaka | Tema | Poglavlje |
|---|---|---|
| `u01_hidraulicna_presa.ipynb` | Hidraulična preša — pojačanje sile i pomak klipa | U01 |
| `u02_kapilarni_uspon.ipynb` | Kapilarni uspon u tankoj cijevi | U02 |
| `u03_diferencijalni_manometar.ipynb` | Diferencijalni manometar s dva fluida | U03 |
| `u04_paraboloidna_povrsina.ipynb` | Paraboloidna slobodna površina u rotirajućem spremniku | U04 |
| `u05_sila_na_ravnu_plohu.ipynb` | Sila na uronjenu pravokutnu plohu i njezino hvatište | U05 |
| `u06_zakrivljena_ploha.ipynb` | Sila na zakrivljenu plohu — četvrtina kruga | U05 |
| `u07_gaz_plivajuceg_tijela.ipynb` | Gaz plivajućeg tijela | U06 |
| `u08_kontinuitet_suzenje.ipynb` | Kontinuitet u suženju cijevi | U07 |
| `u09_venturi.ipynb` | Venturijeva cijev — utjecaj geometrije na tlak i brzinu | U08 |
| `u09_kompresibilna_sapnica.ipynb` | Kompresibilna sapnica i prigušenje protoka | U09 |
| `u11_sila_na_koljeno.ipynb` | Sila na koljeno — promjena smjera strujanja | U10 |
| `u14_cd_re_kugla.ipynb` | Ovisnost koeficijenta otpora kugle o Reynoldsovu broju | U11 |
| `u12_poiseuille_konvergencija.ipynb` | Poiseuilleov profil i numerička konvergencija | U12 |
| `u10_moody_dijagram.ipynb` | Colebrookova jednadžba i koeficijent trenja | U13 |
| `u13_paralelne_grane.ipynb` | Paralelne grane cjevovoda — raspodjela protoka | U13 |
| `u12_pelton_lopatica.ipynb` | Trokuti brzina i snaga na Peltonovoj lopatici | U14 |
| `u15_otvoreni_tokovi.ipynb` | Režimi otvorenog toka i kritična dubina | U15 |

## Automatska provjera

Kanonski popis svih 17 obveznih bilježnica nalazi se u manifestu sheme v2,
`tools/verification_manifest.json`. Sljedeća naredba provjerava inventar, JSON,
Python sintaksu, faze `predvidi → izračunaj → provjeri`, najmanje dvije neovisne
tvrdnje, numeričku analizu i dopuštene pregledničke ovisnosti bez pokretanja
kernela:

```
python tools/execute_notebooks.py --validate-only
```

Potpuna provjera pokreće svaku bilježnicu u zasebnom čistom kernelu, u memoriji,
bez prepisivanja izvornog `.ipynb` zapisa:

```
python tools/execute_notebooks.py
```

Ista se potpuna provjera izvršava u Pages CI-ju prije Quarto rendera. Aktualni
lokalni presjek prolazi 17/17 bilježnica u zasebnim čistim kernelima. To
potvrđuje izvršivost i ugovor bilježnice, ali nije zamjena za stručnu validaciju
fizikalnoga modela.

## Dodavanje nove bilježnice

Aktualne bilježnice uređuju se izravno u datotekama `.ipynb` u ovoj mapi.
Nova bilježnica treba slijediti opisanu strukturu te biti uključena u inventar
`tools/verification_manifest.json` i pripadne provjere. U odgovarajućem izvoru
poglavlja u `source/` dodaje se okvir `.mf1-interaktivno` s poveznicama i QR kodom.

Skripte `scripts/generiraj_notebooke.py` i `scripts/generiraj_qr.py`
sadrže stare predloške. Ne pokreću se pri redovitom uređivanju: mogu prepisati
novije bilježnice ili QR kodove starijim sadržajem.

## QR kodovi

Aktualni generator je `scripts/generate_qr_assets.py`. Nakon promjene
popisa `ASSETS` u toj skripti QR kodovi obnavljaju se naredbom:

```powershell
python scripts/generate_qr_assets.py --write
```

SVG datoteke spremaju se u `assets/qr/`. Ista naredba bez `--write`
provjerava jesu li svi izlazi aktualni, bez prepisivanja datoteka.

## Konvencije

- Sav tekst u bilježnici piše se na hrvatskom književnom jeziku,
  akademskim stilom. Upute čitatelju pišu se u 2. licu jednine
  (npr. „Predvidi”, „Izračunaj”, „Provjeri”).
- Komentari u Python kodu također su na hrvatskom.
- Imena varijabli koriste standardne fizikalne oznake
  (`rho`, `v1`, `D2`, `Re`, `lambda_`) — riječ je o
  internacionalnim matematičkim simbolima, ne anglizmima.
- Imena knjižnica (`numpy`, `matplotlib`) zadržavaju izvornu pisanu
  inačicu jer su vlastite imenice alata.
- Naslovi grafova i oznake osi pišu se na hrvatskom.
