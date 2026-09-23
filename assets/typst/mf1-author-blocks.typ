// MF1 authoring blocks for the native Quarto/Typst PDF.
// Examples use an open layout with a title and whitespace. Other authoring
// blocks keep their semantic rules. Long blocks remain breakable on A4.

#let mf1-author-block(
  title: [],
  accent: mf1-muted,
  mode: "rail",
  body,
) = {
  let rule = mf1-rule-print
  let background = if mode == "alert" {
    mf1-bg-alert
  } else if mode == "rail" {
    mf1-bg-rail
  } else {
    none
  }

  let frame = if mode == "example" {
    none
  } else if mode == "panel" {
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

  let padding = if mode == "example" {
    (top: 7pt, right: 0pt, bottom: 7pt, left: 0pt)
  } else if mode == "panel" {
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
        size: if mode == "example" { mf1-example-title-pt * 1pt } else { mf1-block-title-pt * 1pt },
        weight: "bold",
        tracking: if mode == "example" { 0em } else { 0.015em },
        fill: if mode == "example" { mf1-ink } else { accent },
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
  fill: mf1-bg-level,
  stroke: 0.35pt + mf1-rule-print,
)[
  #set text(size: mf1-level-pt * 1pt, weight: "bold", fill: mf1-ink-level)
  #body
]

// Razina samostalnog zadatka stoji na kraju, odvojena od lijeve numeracije.
#let mf1-task-level(body) = align(right)[
  #text(size: mf1-task-level-pt * 1pt, weight: "regular", fill: mf1-muted-print, body)
]

// Strukturni podnaslov unutar primjera.  Veći razmak iznad odvaja novu fazu
// rješenja, manji razmak ispod drži naslov uz sadržaj koji uvodi.
#let mf1-minor-heading(title) = block(
  above: 1.05em,
  below: 0.46em,
  sticky: true,
)[
  #set text(size: mf1-label-pt * 1pt, weight: "bold", fill: mf1-heading-print)
  #title
]
