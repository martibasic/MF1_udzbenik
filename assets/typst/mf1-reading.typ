// Reading styles apply inside the book body, after orange-book's defaults.
// Keep the same counters and part transition as the bundled heading rule.
#import "@preview/orange-book:0.7.1": part-change

#let mf1-reading(body) = {
  let ink = rgb("#11202e")
  let muted = rgb("#536577")
  let accent = rgb("#8e4519")
  set text(fill: ink)
  set par(first-line-indent: 0pt, spacing: 0.68em, leading: 0.56em)

  show heading: it => context {
    if it.level == 1 {
      pagebreak(to: "odd")
      // Quarto uses custom kinds such as "quarto-float-fig". Reset those
      // too; resetting only the native image/table counters is insufficient.
      for kind in query(figure).map(item => item.kind).dedup() {
        counter(figure.where(kind: kind)).update(0)
      }
      counter(math.equation).update(0)
      part-change.update(false)
      block(width: 100%, above: 0pt, below: 1.3em, sticky: true)[
        #set par(justify: false, leading: 0.45em)
        #set text(size: 23pt, weight: "bold", hyphenate: false)
        #if it.numbering != none [#text(fill: accent)[#counter(heading).display(it.numbering)]#h(0.25em)]
        #it.body
        #v(0.5em)
        #line(length: 100%, stroke: 0.65pt + rgb("#d8d4cb"))
      ]
    } else {
      let size = if it.level == 2 { 14pt } else if it.level == 3 { 11.5pt } else { 10.5pt }
      block(above: 1.25em, below: 0.55em, sticky: true)[
        #set par(justify: false)
        #set text(size: size, weight: "bold", hyphenate: false)
        #if it.numbering != none [#text(fill: accent)[#counter(heading).display(it.numbering)]#h(0.5em)]
        #it.body
      ]
    }
  }

  show figure.caption: set text(size: 9pt, fill: muted)
  show figure.caption: set par(justify: false)
  show table.cell: set par(justify: false)
  show table.cell.where(y: 0): set text(weight: "semibold")
  body
}
