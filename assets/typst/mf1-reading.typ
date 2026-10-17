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
      let appendix = state("appendix-state", none).get() != none
      if appendix and it.numbering == none and it.body == [Dodaci] {
        // Appendix divider: title plus local contents, like the part pages.
        block(above: 24pt, below: 24pt, {
          set par(justify: false)
          text(size: mf1-part-pt * 1pt, weight: "bold", it.body)
        })
        {
          show outline.entry: entry => {
            // Headings imply bold; the local contents are a list, not titles.
            set text(size: mf1-toc-chapter-pt * 1pt, weight: "regular", fill: mf1-ink)
            set par(justify: false, leading: 0.35em)
            show link: set text(fill: mf1-ink)
            block(above: 9pt, below: 2pt, breakable: false,
              link(entry.element.location(),
                entry.indented(entry.prefix(), entry.inner(), gap: 0.6em)))
          }
          outline(title: none, depth: 1, indent: auto,
            target: heading.where(level: 1).after(here(), inclusive: false))
        }
        pagebreak(weak: true)
      } else {
      block(width: 100%, above: 0pt, below: mf1-chapter-after-pt * 1pt,
        breakable: false, sticky: true, {
          set text(size: mf1-h1-pt * 1pt)
          if appendix and it.numbering != none {
            // "Dodatak A — Naslov" in the PDF, as in the web edition.
            set par(justify: false, leading: mf1-heading-leading-em * 1em)
            set text(weight: "bold", hyphenate: false)
            [Dodatak #counter(heading).display("A") — #it.body]
          } else {
            mf1-heading-line(it)
          }
        })
      }
    } else {
      let sizes = (mf1-h2-pt, mf1-h3-pt, mf1-h4-pt)
      let before = (mf1-h2-before-pt, mf1-h3-before-pt, mf1-h4-before-pt)
      let after = (mf1-h2-after-pt, mf1-h3-after-pt, mf1-h4-after-pt)
      let index = calc.min(it.level - 2, 2)
      // Keep every section title with at least two following lines.
      mf1-needspace((mf1-keep-with-next-em + 1) * 1em)
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
  // Items must not sit closer than ordinary lines (vectors/indices touched).
  set list(spacing: mf1-list-spacing-em * 1em)
  set enum(spacing: mf1-list-spacing-em * 1em)
  // Croatian quotation marks „…” also in CSL-generated bibliography entries.
  show bibliography: it => {
    show "“": "”"
    it
  }
  body
}
