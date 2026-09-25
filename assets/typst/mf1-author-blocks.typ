// Open examples, restrained note rails, and breakable long derivations.
#let mf1-author-block(title: [], accent: mf1-muted, mode: "rail", body) = {
  let rule = mf1-rule-print
  let frame = if mode == "example" { none }
    else if mode == "panel" { (top: 0.45pt + rule, bottom: 0.45pt + rule) }
    else { (left: 0.8pt + rule) }
  let padding = if mode == "example" { (y: 3pt) }
    else if mode == "panel" { (x: 2pt, y: 8pt) }
    else { (left: 10pt, right: 6pt, y: 6pt) }
  block(width: 100%, breakable: true,
    above: mf1-block-gap-pt * 1pt, below: mf1-block-gap-pt * 1pt,
    inset: padding, stroke: frame, {
      set par(first-line-indent: 0pt, spacing: mf1-paragraph-spacing-em * 1em)
      block(inset: (bottom: 6pt), breakable: false, sticky: true, {
        set par(justify: false, leading: mf1-heading-leading-em * 1em)
        set text(size: if mode == "example" { mf1-example-title-pt * 1pt }
          else { mf1-block-title-pt * 1pt }, weight: "bold", fill: mf1-ink,
          hyphenate: false)
        title
      })
      body
    })
}

#let mf1-level(body) = box(inset: (x: 4pt, y: 1pt), {
  set text(size: mf1-level-pt * 1pt, weight: "regular", fill: mf1-muted)
  body
})

#let mf1-task-level(body) = align(right, {
  set text(size: mf1-task-level-pt * 1pt, fill: mf1-muted)
  body
})

#let mf1-minor-heading(title) = block(
  above: mf1-minor-before-pt * 1pt, inset: (bottom: mf1-minor-after-pt * 1pt),
  breakable: false, sticky: true, {
    set par(justify: false, leading: mf1-heading-leading-em * 1em)
    set text(size: mf1-label-pt * 1pt, weight: "bold",
      fill: mf1-heading-print, hyphenate: false)
    title
  })

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
