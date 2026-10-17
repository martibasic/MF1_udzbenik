// Open examples, restrained note rails, and breakable long derivations.
#let mf1-author-block(title: [], accent: mf1-muted, mode: "rail", body) = {
  let rule = mf1-rule-print
  let frame = if mode == "example" { none }
    else if mode == "panel" { (top: 0.45pt + rule, bottom: 0.45pt + rule) }
    else { (left: 0.8pt + rule) }
  let padding = if mode == "example" { (y: 3pt) }
    else if mode == "panel" { (x: 2pt, y: mf1-panel-inset-y-pt * 1pt) }
    else { (left: 10pt, right: 6pt, y: 6pt) }
  block(width: 100%, breakable: true,
    above: mf1-block-gap-pt * 1pt, below: mf1-block-gap-pt * 1pt,
    inset: padding, stroke: frame, {
      set par(first-line-indent: 0pt, spacing: if mode == "example" {
        mf1-exercise-paragraph-spacing-em * 1em
      } else { mf1-paragraph-spacing-em * 1em })
      set list(spacing: mf1-exercise-list-spacing-em * 1em) if mode == "example"
      set enum(spacing: mf1-exercise-list-spacing-em * 1em) if mode == "example"
      // Panels introduced by their own section heading (chapter summary)
      // carry no title row.
      if title != none {
        block(inset: (bottom: 6pt), below: if mode == "example" { 0pt } else { auto },
          breakable: false, sticky: true, {
          set par(justify: false, leading: mf1-heading-leading-em * 1em)
          set text(size: if mode == "example" { mf1-example-title-pt * 1pt }
            else { mf1-block-title-pt * 1pt }, weight: "bold", fill: mf1-ink,
            hyphenate: false)
          title
        })
      }
      body
    })
}

// Reserve room for a heading and the first lines after it. If the page has
// less space, the empty probe moves to the next page and takes the heading
// with it; otherwise the negative spacing returns to the original position.
#let mf1-needspace(height) = {
  block(width: 100%, height: height, above: 0pt, below: 0pt, breakable: false)
  v(-height, weak: false)
}

// Scope the same paragraph/list rhythm to unsolved exercises. Their titles
// and numbered requests retain normal pagination inside this open block.
// Extra space above separates consecutive Zn tasks.
#let mf1-exercise-body(body) = block(width: 100%, breakable: true,
  above: mf1-exercise-gap-pt * 1pt, {
  set par(first-line-indent: 0pt, spacing: mf1-exercise-paragraph-spacing-em * 1em)
  set list(spacing: mf1-exercise-list-spacing-em * 1em)
  set enum(spacing: mf1-exercise-list-spacing-em * 1em)
  body
})

#let mf1-level(body) = box(inset: (x: 4pt, y: 1pt), {
  set text(size: mf1-level-pt * 1pt, weight: "regular", fill: mf1-muted)
  body
})

#let mf1-task-level(body) = align(right, {
  set text(size: mf1-task-level-pt * 1pt, fill: mf1-muted)
  body
})

// "Traži se", "Rješenje" and similar labels must not end a page with only one
// line below them: sticky alone keeps just the first (often one-line) item.
#let mf1-minor-heading(title) = {
  mf1-needspace(mf1-keep-with-next-em * 1em)
  block(
  above: mf1-minor-before-pt * 1pt, below: mf1-minor-after-pt * 1pt,
  breakable: false, sticky: true, {
    set par(justify: false, leading: mf1-heading-leading-em * 1em)
    set text(size: mf1-label-pt * 1pt, weight: "bold",
      fill: mf1-heading-print, hyphenate: false)
    title
  })
}

// Printed return links: page of the target as a separate muted run.
#let mf1-page-ref(name) = context {
  let found = query(label(name))
  if found.len() > 0 {
    h(0.45em)
    text(size: mf1-task-level-pt * 1pt, fill: mf1-muted,
      "(str. " + numbering("1", ..counter(page).at(found.first().location())) + ")")
  }
}

// Visible web address for print readers; breaks after slashes if needed.
#let mf1-url(body) = {
  set text(size: mf1-task-level-pt * 1pt, hyphenate: false)
  show "/": it => it + sym.zws
  body
}

// Filled from the canonical "Impresum" section and shown on the title verso.
#let mf1-imprint = state("mf1-imprint", none)

// Retain Quarto's nested callout structure for its numbered-callout adapter,
// but give these existing notes the same quiet treatment as authoring blocks.
#let callout(body: [], title: "Callout", background_color: none,
  icon: none, icon_color: black, body_background_color: none) = {
  block(width: 100%, breakable: true,
    above: mf1-block-gap-pt * 1pt, below: mf1-block-gap-pt * 1pt,
    stroke: (left: 0.8pt + mf1-rule-print),
    block(width: 100%, inset: 1pt, below: 0pt, sticky: true,
      block(width: 100%, inset: (left: 10pt, top: 6pt, bottom: 5pt), sticky: true,
        text(size: mf1-block-title-pt * 1pt, weight: "bold", title))) +
    if body != [] {
      block(width: 100%, inset: 1pt,
        block(width: 100%, inset: (left: 10pt, right: 6pt, bottom: 6pt), body))
    })
}
