// Configure the bundled Quarto 1.9.37 book template. Keep its chapter,
// appendix, reference and outline machinery; use the MF1 print palette.
#import "@preview/orange-book:0.7.1": book, part, chapter, appendices

#show: book.with(
$if(title)$
  title: [#text(size: 36pt, weight: "semibold", fill: mf1-ink)[$title$]],
$endif$
$if(subtitle)$
  subtitle: [#text(size: 14pt, fill: mf1-muted)[$subtitle$]],
$endif$
$if(by-author)$
  author: "$for(by-author)$$it.name.literal$$sep$, $endfor$",
$endif$
$if(date)$
  date: "$date$",
$endif$
  lang: "hr",
  supplement-chapter: "Poglavlje",
  supplement-part: "Dio",
  main-color: mf1-accent-d,
  cover-background: none,
  cover: block(width: 100%, height: 100%)[
    #place(top + left, dx: 24mm, dy: 35mm)[
      #line(length: 24mm, stroke: 2pt + mf1-accent)
      #v(5mm)
      #text(size: 10pt, fill: mf1-muted)[SVEUČILIŠNI UDŽBENIK]
    ]
  ],
  paper-size: "a4",
  margin: (x: $margin.x$, top: $margin.y$, bottom: $margin.y$),
  font-size: $fontsize$,
  first-line-indent: false,
  padded-heading-number: false,
$if(toc-depth)$
  outline-depth: $toc-depth$,
$endif$
)
