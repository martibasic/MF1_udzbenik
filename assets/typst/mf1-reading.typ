// Reading styles apply inside the book body, after orange-book's defaults.
// Keep the same counters and part transition as the bundled heading rule.
#import "@preview/orange-book:0.7.1": part-change

#let mf1-reading(body) = {
  let ink = mf1-ink
  let muted = mf1-muted
  let accent = mf1-accent-d
  set text(fill: ink, font: mf1-font-family)
  set par(first-line-indent: 0pt, spacing: mf1-paragraph-spacing-em * 1em, leading: mf1-leading-em * 1em)

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
        #set text(size: mf1-h1-pt * 1pt, weight: "bold", hyphenate: false)
        #if it.numbering != none [#text(fill: accent)[#counter(heading).display(it.numbering)]#h(0.25em)]
        #it.body
        #v(0.5em)
        #line(length: 100%, stroke: 0.65pt + mf1-rule-heading)
      ]
    } else {
      let size = if it.level == 2 { mf1-h2-pt * 1pt } else if it.level == 3 { mf1-h3-pt * 1pt } else { mf1-h4-pt * 1pt }
      block(above: 1.25em, below: 0.55em, sticky: true)[
        #set par(justify: false)
        #set text(size: size, weight: "bold", hyphenate: false)
        #if it.numbering != none [#text(fill: accent)[#counter(heading).display(it.numbering)]#h(0.5em)]
        #it.body
      ]
    }
  }

  show figure.caption: set text(size: mf1-figure-tokens.at("figure-caption-size") * 1pt, fill: muted)
  show figure.caption: set par(justify: false)
  show figure: set block(breakable: true)
  show table.cell: set par(justify: false)
  set table.cell(breakable: false)
  show table.cell.where(y: 0): set text(weight: "semibold")
  body
}
