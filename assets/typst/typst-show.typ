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
$if(description)$
  description: "$description$",
$endif$
$if(keywords)$
  keywords: ($for(keywords)$"$keywords$",$endfor$),
$endif$
$if(mf1-institution)$
  institution: ($for(mf1-institution)$[$mf1-institution$],$endfor$),
$endif$
$if(mf1-place-year)$
  place-year: [$mf1-place-year$],
$endif$
$if(toc-depth)$
  outline-depth: $toc-depth$,
$endif$
)
