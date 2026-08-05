// MF1 authoring blocks for the native Quarto/Typst PDF.
// Kept deliberately quiet: a thin semantic rule, a restrained tint and a
// compact label.  The block remains breakable for long derivations on A4.

#let mf1-author-block(
  title: [],
  accent: rgb("#536577"),
  mode: "rail",
  body,
) = {
  let rule = rgb("#c8cdd2")
  let background = if mode == "alert" {
    rgb("#fff8f3")
  } else if mode == "rail" {
    rgb("#f8fafb")
  } else {
    none
  }

  let frame = if mode == "panel" {
    (
      top: 0.45pt + rule,
      right: none,
      bottom: 0.45pt + rule,
      left: none,
    )
  } else {
    (
      top: none,
      right: none,
      bottom: none,
      left: 1.55pt + accent,
    )
  }

  let padding = if mode == "panel" {
    (top: 8pt, right: 2pt, bottom: 8pt, left: 2pt)
  } else {
    (top: 7pt, right: 9pt, bottom: 7pt, left: 11pt)
  }

  block(
    width: 100%,
    breakable: true,
    above: 1.05em,
    below: 1.05em,
    inset: padding,
    fill: background,
    stroke: frame,
  )[
    #set par(first-line-indent: 0pt, spacing: 0.62em)
    #block(below: 0.48em, sticky: true)[
      #set text(
        size: 8.7pt,
        weight: "bold",
        tracking: 0.035em,
        fill: accent,
      )
      #title
    ]
    #body
  ]
}

// Diskretna oznaka razine ostaje uz naslov primjera, ali se čita kao zasebna
// značka umjesto kao posljednja riječ naslova.
#let mf1-level(body) = box(
  inset: (x: 4pt, y: 1.2pt),
  radius: 2pt,
  fill: rgb("#eef1f3"),
  stroke: 0.35pt + rgb("#c8cdd2"),
)[
  #set text(size: 7.2pt, weight: "bold", fill: rgb("#4f5963"))
  #body
]

// Strukturni podnaslov unutar primjera.  Veći razmak iznad odvaja novu fazu
// rješenja, manji razmak ispod drži naslov uz sadržaj koji uvodi.
#let mf1-minor-heading(title) = block(
  above: 1.05em,
  below: 0.46em,
  sticky: true,
)[
  #set text(size: 9.5pt, weight: "bold", fill: rgb("#303841"))
  #title
]
