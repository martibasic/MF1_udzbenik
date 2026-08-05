# Postavljanje JupyterLite-a kao primarnog pregledničkog okruženja

JupyterLite omogućuje pokretanje Jupyter notebooka izravno u pregledniku,
bez ikakve prijave i bez lokalne instalacije. Pokreće se kao statički
sklop uz Quarto mrežno izdanje udžbenika. Colab je samo pričuvni put.

## Postupak postavljanja (jednokratno)

### 1. Instalacija JupyterLite alata

```
pip install jupyterlite-core==0.8.1
pip install jupyterlite-pyodide-kernel==0.8.1
```

`pyodide-kernel` je Python jezgra koja se izvršava u pregledniku
(WebAssembly). Podržava `numpy`, `matplotlib` i `ipywidgets` koji
su potrebni za naše notebooke.

### 2. Izgradnja JupyterLite sklopa

U korijenu repozitorija:

```
jupyter lite build --config=jupyter_lite_config.py --contents notebooks --output-dir _site/jlite
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
jupyter lite build --config=jupyter_lite_config.py --contents notebooks --output-dir _site/jlite
```

### 4. Veze prema JupyterLite-u u poglavljima

U okviru `.mf1-interaktivno` može se dodati druga veza koja vodi na
JupyterLite umjesto Colab-a, korisno za studente koji ne žele
prijavu na Google:

```html
<a class="mf1-interaktivno-veza" href="https://martibasic.github.io/MF1_udzbenik/jlite/lab/index.html?path=u09_venturi.ipynb">
  Otvori u pregledniku (bez prijave)
</a>
```

## Ograničenja JupyterLite-a

- **Sporiji start** — prvi put treba 5–15 sekundi za učitavanje Python
  okruženja u preglednik.
- **Manji izbor knjižnica** — sve knjižnice moraju biti dostupne kao
  WebAssembly inačica. Ovaj projekt namjerno ostaje na `numpy`, `matplotlib`
  i `ipywidgets`; specijalizirane knjižnice nisu dio ugovora notebooka.
- **Veće datoteke** — `_site/jlite/` može biti 50–100 MB. Ne stavlja
  se u git nego se generira pri izgradnji.

## Status integracije

JupyterLite je dio proizvodnoga CI toka. Workflow prvo izvršava svih 17
notebooka u čistim kernelima, zatim gradi statički sklop u `_site/jlite` i
provjerava `lab/index.html` te inventar svih 17 bilježnica. Colab ostaje
pričuvni put ako preglednik ili mrežna politika ne dopuštaju WebAssembly.
