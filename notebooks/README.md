# Interaktivni prikazi (Jupyter notebookovi)

Ova mapa sadrži 17 interaktivnih Jupyter notebookova koji nadopunjuju
kanonska poglavlja U01–U15. Svaki notebook je samostalni numerički pokus:
student najprije predviđa ishod, zatim izvodi račun i naposljetku provjerava
bilancu, granični slučaj, pogrešku, konvergenciju, osjetljivost ili nesigurnost.

## Struktura notebooka

Svaki notebook prati istu akademsku strukturu:

1. **Predvidi** — kvalitativni smjer, predznak ili red veličine prije računa.
2. **Model i pretpostavke** — sustav, jednadžbe i područje valjanosti.
3. **Izračunaj** — reproducibilni Python račun s pregledničkim ovisnostima.
4. **Provjeri** — najmanje dvije neovisne izvršive tvrdnje.
5. **Numerička kvaliteta** — analiza pogreške, konvergencije, osjetljivosti,
   reziduala ili nesigurnosti.
6. **Protumači** — pitanja o fizikalnom značenju i granici modela.

## Pokretanje

### JupyterLite (primarni mrežni put)

Svako kanonsko poglavlje vodi na odgovarajući notebook u JupyterLiteu, bez
prijave i bez lokalne instalacije. Paket koristi Python/Pyodide u pregledniku i
gradi se u `_site/jlite`. Konfiguracija, hashovi svih 17 notebookova i pokretanje
kernela provjeravaju se automatizirano; konačni javni artefakt ipak se ne smatra
spremnim dok ne prođe završni proizvodni build aktualnoga commita.

### Google Colab (pričuvni put)

Ako preglednik ili mrežna politika ne podržava JupyterLite, poveznica
*Pričuvno: otvori u Colabu* otvara isti izvorni notebook. Potreban je Google
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

Notebookovi namjerno ovise samo o `numpy` i `matplotlib`, pa isti račun radi u
lokalnom kernelu, Colabu i pregledničkom Pyodide kernelu.

## Popis dostupnih notebooka

| Oznaka | Tema | Poglavlje |
|---|---|---|
| `u01_hidraulicna_presa.ipynb` | Hidraulična preša — pojačanje sile i pomak klipa | U01 |
| `u02_kapilarni_uspon.ipynb` | Kapilarni uspon u tankoj cijevi | U02 |
| `u03_diferencijalni_manometar.ipynb` | Diferencijalni manometar s dva fluida | U03 |
| `u04_paraboloidna_povrsina.ipynb` | Paraboloidna slobodna površina u rotirajućem spremniku | U04 |
| `u05_sila_na_ravnu_plohu.ipynb` | Sila i hvatište na pravokutnu plohu pod vodom | U05 |
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

Kanonski popis svih 17 obveznih notebookova nalazi se u manifestu sheme v2,
`tools/verification_manifest.json`. Sljedeća naredba provjerava inventar, JSON,
Python sintaksu, faze `predvidi → izračunaj → provjeri`, najmanje dvije neovisne
tvrdnje, numeričku analizu i dopuštene pregledničke ovisnosti bez pokretanja
kernela:

```
python tools/execute_notebooks.py --validate-only
```

Potpuna provjera pokreće svaki notebook u zasebnom čistom kernelu, u memoriji,
bez prepisivanja izvornog `.ipynb` zapisa:

```
python tools/execute_notebooks.py
```

Ista se potpuna provjera izvršava u Pages CI-ju prije Quarto rendera. Aktualni
lokalni presjek prolazi 17/17 notebookova u zasebnim čistim kernelima. To
potvrđuje izvršivost i ugovor notebooka, ali nije zamjena za stručnu validaciju
fizikalnoga modela.

## Dodavanje novog notebooka

Novi se notebooci dodaju u rječnik `NOTEBOOKS` u skripti
`scripts/generiraj_notebooke.py`. Nakon dodavanja pokreće se:

```
python scripts/generiraj_notebooke.py
```

Veze se dopunjuju u rječniku `VEZE` u `scripts/generiraj_qr.py`,
nakon čega se pokreće:

```
python scripts/generiraj_qr.py
```

Završno se u odgovarajućoj `.md` datoteci u mapi `source/` dodaje
okvir `.mf1-interaktivno` uz središnju jednadžbu poglavlja.

## QR kodovi

QR kodovi za tiskanu inačicu udžbenika generiraju se skriptom:

```
python scripts/generiraj_qr.py
```

SVG datoteke spremaju se u `assets/qr/`. Kada se doda novi notebook,
treba dopuniti rječnik `VEZE` u toj skripti i pokrenuti generiranje.

## Konvencije

- Sav tekst u notebooku piše se na hrvatskom književnom jeziku,
  u 3. licu jednine, akademskim stilom.
- Komentari u Python kodu također su na hrvatskom.
- Imena varijabli koriste standardne fizikalne oznake
  (`rho`, `v1`, `D2`, `Re`, `lambda_`) — riječ je o
  internacionalnim matematičkim simbolima, ne anglizmima.
- Imena knjižnica (`numpy`, `matplotlib`) zadržavaju izvornu pisanu
  inačicu jer su vlastite imenice alata.
- Naslovi grafova i oznake osi pišu se na hrvatskom.
