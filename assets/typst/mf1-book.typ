// Presentation only: the bundled appendix state is shared with Quarto.
#import "@preview/orange-book:0.7.1": part-change, part-state, part-counter, part-location

#let mf1-outline-row(it) = {
  show link: set text(fill: mf1-ink)
  set text(size: if it.level == 1 { mf1-toc-chapter-pt * 1pt }
    else { mf1-toc-pt * 1pt },
    weight: if it.level == 1 { "bold" } else { "regular" }, fill: mf1-ink)
  set par(justify: false, leading: 0.35em)
  block(above: if it.level == 1 { 9pt } else { 2pt }, below: 2pt,
    inset: (y: if it.level == 1 { 2pt } else { 2.2pt }),
    breakable: false, sticky: it.level == 1,
    link(it.element.location(), it.indented(it.prefix(), it.inner(), gap: 0.6em)))
}

// Keep the existing part title and local contents, without coloured full pages.
#let part(title) = {
  pagebreak(weak: true)
  metadata("mf1-part-page")
  part-change.update(true)
  part-state.update(title)
  part-counter.step()
  context part-location.update(here())
  block(above: 24pt, below: 24pt, {
    set par(justify: false)
    text(size: mf1-part-pt * 1pt, weight: "bold", {
      context counter("part-counter").display("I.")
      h(0.5em)
      title
    })
  })
  context {
    show outline.entry: it => {
      if (part-state.at(it.element.location()) == title
        and state("appendix-state", none).at(it.element.location()) == none) {
        mf1-outline-row(it)
      }
    }
    outline(title: none, depth: 2, indent: auto)
  }
  pagebreak(weak: true)
}

// One restrained cover motif taken from an existing book sketch (streamline
// with velocity vectors, Slika "Strujnica i trajektorija"), recoloured to a
// single ink at build time. Labels and title text of the sketch are removed;
// the canonical SVG stays untouched.
#let mf1-cover-motif(colour: mf1-accent, width: 100mm) = {
  let svg = read("/assets/print/u08_fig_kinematika.svg")
  svg = svg.replace(regex("(?s)<text\b.*?</text>"), "")
  svg = svg.replace(regex("(?s)<title\b.*?</title>"), "")
  svg = svg.replace(regex("(?s)<desc\b.*?</desc>"), "")
  svg = svg.replace(regex("fill=\"(#fff|#ffffff|#FFFFFF|white)\""), "fill=\"none\"")
  svg = svg.replace(regex("#[0-9a-fA-F]{6}\b"), colour.to-hex())
  // Left panel only: the streamline and its tangent velocity vectors.
  svg = svg.replace(regex("viewBox=\"[^\"]*\""), "viewBox=\"20 128 345 128\"", count: 1)
  image(bytes(svg), format: "svg", width: width,
    alt: "Ukrasni motiv: strujnice s vektorima brzine.")
}

#let mf1-book(title: [], subtitle: [], author: "", description: none,
  keywords: (), institution: (), place-year: none, outline-depth: 2, body) = {
  set document(title: title, author: author, description: description,
    keywords: keywords)
  set text(font: mf1-font-family, size: mf1-font-size-pt * 1pt,
    lang: "hr", fill: mf1-ink)
  set par(justify: false, first-line-indent: 0pt)
  set page(paper: mf1-paper,
    margin: (x: mf1-margin-x-mm * 1mm, y: mf1-margin-y-mm * 1mm),
    numbering: "1", header: context {
      let current = here().page()
      let starts = query(heading.where(level: 1))
      let dividers = query(metadata).filter(it => it.value == "mf1-part-page")
      if (not starts.any(it => it.location().page() == current)
        and not dividers.any(it => it.location().page() == current)) {
        let before = starts.filter(it => it.location().page() < current)
        if before != () {
          let chapter = before.last()
          set text(size: mf1-header-pt * 1pt, fill: mf1-muted)
          set par(justify: false, leading: 0.25em)
          block(width: 100%, inset: (bottom: 5pt),
            stroke: (bottom: 0.4pt + mf1-rule-print), {
              let appendix = state("appendix-state", none).at(chapter.location()) != none
              if appendix and chapter.numbering != none {
                [Dodatak #numbering("A", counter(heading).at(chapter.location()).first()) — ]
              } else if chapter.numbering != none {
                numbering(chapter.numbering, ..counter(heading).at(chapter.location()))
                h(0.4em)
              }
              chapter.body
            })
        }
      }
    }, footer: context align(center,
      text(size: mf1-folio-pt * 1pt, fill: mf1-muted, counter(page).display("1"))))
  set heading(numbering: (..nums) => {
    numbering(if nums.pos().len() == 1 { "1." } else { "1.1" }, ..nums)
  }, supplement: "Poglavlje")
  set math.equation(numbering: equation-numbering)
  set figure(numbering: callout-numbering)
  show figure.where(caption: none): set figure(outlined: false)
  show link: set text(fill: mf1-accent-d)

  // Title page (recto): series label, title, subtitle, author, one motif,
  // institution and year.
  page(header: none, footer: none, {
    set par(justify: false)
    v(12mm)
    text(size: 10pt, fill: mf1-muted, tracking: 0.12em, upper[Sveučilišni priručnik])
    v(36mm)
    block(below: 22pt, {
      set par(leading: 0.4em)
      set text(size: mf1-title-pt * 1pt, weight: "bold", hyphenate: false)
      title
    })
    block(below: 30pt, {
      set par(leading: 0.55em)
      text(size: 14pt, fill: mf1-muted, hyphenate: false, subtitle)
    })
    text(size: 16pt, author)
    v(1fr)
    align(center, mf1-cover-motif())
    v(1fr)
    {
      set text(size: 11pt, fill: mf1-ink)
      set par(leading: 0.5em)
      for line in institution { line; linebreak() }
      if place-year != none { v(4pt); text(fill: mf1-muted, place-year) }
    }
  })

  // Title verso: imprint from the canonical "Impresum" section.
  page(header: none, footer: none, {
    set par(justify: false, spacing: 0.9em, leading: 0.55em)
    set text(size: 9.5pt, fill: mf1-soft-ink)
    set list(spacing: 0.7em)
    v(1fr)
    context {
      let imprint = mf1-imprint.final()
      if imprint != none {
        block(below: 10pt, text(size: 10.5pt, weight: "bold", fill: mf1-ink)[Impresum])
        imprint
      }
    }
  })

  {
    show heading: it => block(below: 20pt, sticky: true,
      text(size: mf1-h1-pt * 1pt, weight: "bold", it.body))
    show outline.entry: it => context {
      if it.level == 1 and part-change.at(it.element.location()) {
        block(above: 17pt, below: 5pt, breakable: false, sticky: true, {
          set text(size: 12pt, weight: "bold", fill: mf1-muted)
          numbering("I.", part-counter.at(it.element.location()).first())
          h(0.5em)
          part-state.at(it.element.location())
        })
      }
      mf1-outline-row(it)
    }
    outline(title: [Sadržaj], depth: outline-depth, indent: auto)
  }
  pagebreak(weak: true)
  body
}
