// Code-mode blocks keep layout independent of source line endings.
#import "@preview/orange-book:0.7.1": part-change

#let mf1-heading-line(it) = {
  set par(justify: false, leading: mf1-heading-leading-em * 1em)
  set text(weight: "bold", hyphenate: false)
  if it.numbering == none {
    it.body
  } else {
    // One unbreakable row, with matching baselines and hanging title lines.
    grid(columns: (auto, 1fr), column-gutter: 0.45em, align: top,
      counter(heading).display(it.numbering), it.body)
  }
}

#let mf1-reading(body) = {
  set text(fill: mf1-ink, font: mf1-font-family,
    size: mf1-font-size-pt * 1pt, costs: (widow: 100%, orphan: 100%))
  set par(first-line-indent: 0pt, justify: true,
    spacing: mf1-paragraph-spacing-em * 1em, leading: mf1-leading-em * 1em)
  set heading(hanging-indent: 0pt)

  show heading: it => context {
    if it.level == 1 {
      pagebreak(weak: true)
      // Quarto uses custom figure kinds: reset every kind, not just image.
      for kind in query(figure).map(item => item.kind).dedup() {
        counter(figure.where(kind: kind)).update(0)
      }
      counter(math.equation).update(0)
      part-change.update(false)
      block(width: 100%, above: 0pt, below: mf1-chapter-after-pt * 1pt,
        breakable: false, sticky: true, {
          set text(size: mf1-h1-pt * 1pt)
          mf1-heading-line(it)
        })
    } else {
      let sizes = (mf1-h2-pt, mf1-h3-pt, mf1-h4-pt)
      let before = (mf1-h2-before-pt, mf1-h3-before-pt, mf1-h4-before-pt)
      let after = (mf1-h2-after-pt, mf1-h3-after-pt, mf1-h4-after-pt)
      let index = calc.min(it.level - 2, 2)
      block(width: 100%, above: before.at(index) * 1pt,
        below: after.at(index) * 1pt, breakable: false, sticky: true, {
          set text(size: sizes.at(index) * 1pt)
          mf1-heading-line(it)
        })
    }
  }

  show math.equation.where(block: true): set block(
    above: mf1-equation-gap-pt * 1pt, below: mf1-equation-gap-pt * 1pt)
  set math.equation(number-align: right + horizon)
  set figure(gap: mf1-figure-gap-pt * 1pt)
  show figure.caption: set text(
    size: mf1-figure-tokens.at("figure-caption-size") * 1pt, fill: mf1-muted)
  show figure.caption: set par(justify: false, leading: 0.4em)
  show figure: set block(breakable: true, above: 12pt, below: 12pt)
  show table.cell: set par(justify: false, leading: 0.5em)
  set table.cell(breakable: false)
  show table.cell.where(y: 0): set text(weight: "semibold")
  set list(spacing: 0.35em)
  set enum(spacing: 0.35em)
  body
}
