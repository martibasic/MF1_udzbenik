# Interaktivni prikazi (Jupyter notebooci)

Ova mapa sadrži interaktivne Jupyter notebooke koji nadopunjuju
poglavlja udžbenika. Svaki notebook je samostalna jedinica koja
omogućuje studentu mijenjanje ključnih parametara i neposredno
praćenje učinka na rezultat.

## Struktura notebooka

Svaki notebook prati istu akademsku strukturu:

1. **Naslov i poveznica s poglavljem** — kratak opis o čemu se radi.
2. **Cilj i pretpostavke modela** — što se istražuje i pod kojim uvjetima.
3. **Računski model** — jednadžbe u istom obliku kao u poglavlju.
4. **Interaktivni prikaz** — 2 do 3 klizača za ključne parametre.
5. **Pitanja za samostalno istraživanje** — 3 do 4 otvorena pitanja.
6. **Veza s teorijom poglavlja** — kratak zatvarač.

## Pokretanje

### Google Colab (preporučeno)

Najjednostavniji način korištenja. Klikom na vezu
*Otvori interaktivni prikaz* u poglavlju, notebook se otvara
izravno u pregledniku. Potreban je Google račun.

Veze imaju oblik:
```
https://colab.research.google.com/github/martibasic/MF1_udzbenik/blob/main/notebooks/<ime>.ipynb
```

### Lokalno pokretanje

Za rad bez interneta potrebne su sljedeće knjižnice:

```
pip install jupyter numpy matplotlib ipywidgets
jupyter notebook
```

Klizači zahtijevaju proširenje `ipywidgets` koje je u standardnoj
Jupyter distribuciji uključeno.

### JupyterLite (mrežno izdanje udžbenika)

U mrežnom izdanju udžbenika integriran je JupyterLite koji omogućuje
pokretanje notebooka izravno u pregledniku, bez prijave i bez
lokalne instalacije. Postavlja se kao zaseban podsklop pri izgradnji
Quarto projekta (vidi `scripts/postavi_jupyterlite.md`).

## Popis dostupnih notebooka

| Oznaka | Tema | Poglavlje |
|---|---|---|
| `u09_venturi.ipynb` | Venturijeva cijev — utjecaj geometrije na tlak i brzinu | U09 |

Daljnji notebooci dodaju se prema obrascu iz `u09_venturi.ipynb`.

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
