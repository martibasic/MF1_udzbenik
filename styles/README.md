# Slojevi stilova

Redoslijed učitavanja: tokens → base → typography → layout → components →
utilities → print → responsive. Bootstrap dobiva iste osnovne vrijednosti
kroz generirani `design-system/quarto-theme.scss`. Komponentni stilovi nisu vezani uz broj
poglavlja ili ID pojedine tablice.

Autoritativne vrijednosti su u `design-system/tokens.json`, a figure imaju
zaseban uvezeni modul `assets/figure-tokens.json`. `tokens.css`,
`quarto-theme.scss`, `print.css` i `responsive.css` generira build;
predlošci za posljednje dvije datoteke završavaju s `.css.in`.

`!important` se koristi samo za isključivanje animacija i za obveznu
vidljivost u tisku, gdje nadjačava Bootstrapove pomoćne klase.
