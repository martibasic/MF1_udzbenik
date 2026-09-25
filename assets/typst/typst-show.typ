// MF1 owns presentation; Quarto's chapter/appendix counters and references stay native.
#import "@preview/orange-book:0.7.1": chapter, appendices

#show: mf1-book.with(
$if(title)$
  title: [$title$],
$endif$
$if(subtitle)$
  subtitle: [$subtitle$],
$endif$
$if(by-author)$
  author: "$for(by-author)$$it.name.literal$$sep$, $endfor$",
$endif$
$if(toc-depth)$
  outline-depth: $toc-depth$,
$endif$
)
