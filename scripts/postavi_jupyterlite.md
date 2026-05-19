# Postavljanje JupyterLite-a kao rezervne inačice

JupyterLite omogućuje pokretanje Jupyter notebooka izravno u pregledniku,
bez ikakve prijave i bez lokalne instalacije. Pokreće se kao statički
sklop koji se može poslužiti uz Quarto mrežno izdanje udžbenika.

## Postupak postavljanja (jednokratno)

### 1. Instalacija JupyterLite alata

```
pip install jupyterlite-core
pip install jupyterlite-pyodide-kernel
```

`pyodide-kernel` je Python jezgra koja se izvršava u pregledniku
(WebAssembly). Podržava `numpy`, `matplotlib` i `ipywidgets` koji
su potrebni za naše notebooke.

### 2. Izgradnja JupyterLite sklopa

U korijenu repozitorija:

```
jupyter lite build --contents notebooks --output-dir _site/jlite
```

Ova naredba uzima sve notebooke iz `notebooks/` i pakira ih u statički
sklop u `_site/jlite/`. Quarto već koristi `_site/` kao izlaznu mapu,
pa je JupyterLite automatski dostupan na adresi
`<korijen-stranice>/jlite/`.

### 3. Izgradnja u istom toku kao Quarto

Najjednostavnije je dodati `quarto render` i `jupyter lite build` kao
dva koraka u skripti `scripts/izgradi.ps1`:

```powershell
# scripts/izgradi.ps1
quarto render
jupyter lite build --contents notebooks --output-dir _site/jlite
```

### 4. Veze prema JupyterLite-u u poglavljima

U okviru `.mf1-interaktivno` može se dodati druga veza koja vodi na
JupyterLite umjesto Colab-a, korisno za studente koji ne žele
prijavu na Google:

```html
<a class="mf1-interaktivno-veza" href="/jlite/lab/index.html?path=u09_venturi.ipynb">
  Otvori u pregledniku (bez prijave)
</a>
```

## Ograničenja JupyterLite-a

- **Sporiji start** — prvi put treba 5–15 sekundi za učitavanje Python
  okruženja u preglednik.
- **Manji izbor knjižnica** — sve knjižnice moraju biti dostupne kao
  WebAssembly inačica. `numpy`, `matplotlib`, `ipywidgets`, `pandas`
  su dostupni. Specijalizirane knjižnice mogu nedostajati.
- **Veće datoteke** — `_site/jlite/` može biti 50–100 MB. Ne stavlja
  se u git nego se generira pri izgradnji.

## Status integracije

JupyterLite je trenutno **dokumentiran ali nije izgrađen**. Pilot inačica
udžbenika koristi samo Colab vezu. Kada se odluči o aktivaciji
JupyterLite-a, slijede se koraci iz ovog dokumenta.
