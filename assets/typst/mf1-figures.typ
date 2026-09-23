// Shared physical tokens. SVGs are inserted at intrinsic size, never stretched.
#let mf1-figure-tokens = json("/assets/figure-tokens.json")
#let mf1-print-rows(rows) = {
  for (i, row) in rows.enumerate() {
    // Keep the final diagram, any trailing legend rows, and its caption together.
    align(center, block(breakable: false, sticky: row.at(2),
      above: 4pt, below: 4pt)[
      #image(row.at(0), width: row.at(1) * 1pt)
    ])
  }
}
