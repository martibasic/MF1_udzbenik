# Obvezna provjera prije pusha

GitHub Action, `scripts/izgradi.ps1` i Gitov `.githooks/pre-push` pokreću isti
`scripts/check_publication.py`. Popis numeričkih, strukturnih, SVG, notebook,
PDF, JupyterLite i pregledničkih provjera postoji samo u tom runneru.
Izgradnja ne popravlja izvore automatski; zastarjele izvedenice ruše provjeru.

## Jednokratna priprema svakoga klona

Potrebni su Python 3.12, Node.js 22, Quarto 1.9.37 i Chrome/Chromium/Edge.
Runner provjerava verzije prema `publish.yml` i svaku pinanu Python ovisnost
prema `requirements.txt`. Nepodudaranje zaustavlja provjeru.

```powershell
py -3.12 -m venv .venv-ci
.venv-ci/Scripts/python.exe -m pip install -r requirements.txt
python scripts/install_hooks.py
```

Na Linuxu/macOS-u odgovarajuće su naredbe `python3.12 -m venv .venv-ci` i
`.venv-ci/bin/python -m pip install -r requirements.txt`.
Ako su Quarto i Node instalirani globalno, njihove propisane verzije trebaju
biti na PATH-u. Prijenosive lokalne instalacije mogu biti u
`tools/tmp/ci/quarto/bin/` i `.tools-ci/node/`; runner tim putanjama daje prednost.
Obje lokalne mape i `.venv-ci/` isključene su iz Gita.

Instalacija hooka postavlja samo `core.hooksPath=.githooks` za ovaj klon.
Postojeću drugu konfiguraciju hookova odbija prepisati. Novi klon zahtijeva
ponovno pokretanje instalacije jer Git ne prenosi lokalnu konfiguraciju.
Datoteka hooka mora biti izvršiva na Unixu; instalacijska skripta to postavlja.

## Rad i provjera

```powershell
python scripts/check_publication.py
```

Naredba automatski koristi lokalni `.venv-ci` ako postoji, instalira Node
ovisnosti s `npm ci --ignore-scripts` i izvršava cijelu objavnu izgradnju.
To je i ručna provjera nezacommitanoga rada. Log izlazi na terminal; za zapis:

```powershell
python scripts/check_publication.py *> tools/tmp/local-ci.log
```

Prilikom `git push` hook zahtijeva čist radni direktorij i indeks, bez
nepraćenih datoteka koje nisu ignorirane. Poslani commit mora biti trenutačni
HEAD. Za slanje drugog vrha grane najprije ga treba checkoutati i zasebno
provjeriti. Anotirani tag razrješava se na commit. Samo brisanje udaljene
reference ne šalje kod pa nema objavne izgradnje.

Svaki push koji šalje kod ponovno pokreće puni runner. Nema predmemorije
uspješnih provjera. Nakon izgradnje hook ponovno provjerava HEAD i čistoću
rada kako izmjena tijekom testiranja ne bi prošla neopaženo. Ne koristi se
`--no-verify`. Pogreška testiranja ili nedostupan alat zaustavlja push.

`tools/test_pre_push.py` pokreće stvarni Gitov hook prema privremenom lokalnom
bare repozitoriju. Provjerava uspjeh, neuspjeh, ponovljeni push, prljav rad,
pogrešan commit, promjenu tijekom provjere, tagove i brisanje. Test ne šalje
ništa na GitHub.

## Granice lokalnog dokaza

Isti runner i pinane verzije smanjuju razliku lokalnog rada i Actionsa.
Windows i Ubuntu i dalje imaju različite sistemske fontove i preglednike;
audit tiskovnih izreza zato provjerava i zamjenski Arial/sans-serif.
Lokalni prolaz ne provjerava GitHubove ovlasti, dostupnost udaljenih servisa,
upload artefakta ni Pages deploy. Poslije odobrenoga pusha treba provjeriti
i udaljeni Action; lokalni prolaz nije tvrdnja da je deploy već uspio.

Prethodni pad: [Action 35961612272](https://github.com/martibasic/MF1_udzbenik/actions/runs/35961612272),
korak `Audit canonical SVGs and generated print compositions`, oznaka
`0,55 m` u `u03_ch1_zatvoreni_spremnik_ulje_ziva.svg`. Zamjenski font
prelazio je izrez širine 690 SVG jedinica. Izrez je proširen na 694; provjera
obaju fontova lokalno reproducira stari pad. Geometrija i tekst skice ostaju isti.
