// Shared physical tokens. SVGs are inserted at intrinsic size, never stretched.
#let mf1-figure-tokens = json("/assets/figure-tokens.json")
#let mf1-print-rows(rows, alt: none) = {
  let count = rows.len()
  for (i, row) in rows.enumerate() {
    // Tagged PDF: every row is an image of the same figure and carries its
    // description; continuation rows say which part they are.
    let description = if alt == none or alt == "" { none }
      else if count == 1 { alt }
      else { alt + " (dio " + str(i + 1) + " od " + str(count) + ")" }
    // Keep the final diagram, any trailing legend rows, and its caption together.
    align(center, block(breakable: false, sticky: row.at(2),
      above: 4pt, below: 4pt)[
      #image(row.at(0), width: row.at(1) * 1pt, alt: description)
    ])
  }
}
