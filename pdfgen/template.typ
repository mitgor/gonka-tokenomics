// Pandoc -> Typst template for gonka-tokenomics documents. Used by pdfgen/build_pdfs.py.
#let navy = rgb("#0b1a4a")
#let orange = rgb("#e8600a")
#let grey = rgb("#5b6170")
#let rule = rgb("#d9dce3")
#let tint = rgb("#f4f5f8")
#let compact = $if(compact)$true$else$false$endif$

#set document(title: [$title$])
#set page(
  paper: "a4",
  margin: if compact { (top: 11mm, bottom: 11mm, x: 13mm) } else { (top: 22mm, bottom: 20mm, x: 18mm) },
  header: context {
    if counter(page).get().first() > 1 {
      set text(size: 8pt, fill: grey)
      grid(columns: (1fr, auto), [$header-title$], [$doc-date$])
      v(-5pt)
      line(length: 100%, stroke: 0.5pt + rule)
    }
  },
  footer: context {
    set text(size: 8pt, fill: grey)
    grid(columns: (1fr, auto), [$footer-left$],
      [Page #counter(page).display() of #counter(page).final().first()])
  },
)
#set text(font: ("Helvetica Neue", "Inter", "Helvetica", "Arial"),
  size: if compact { 8.2pt } else { 9.5pt }, fill: rgb("#1a1a1a"))
#set par(justify: false, leading: if compact { 0.5em } else { 0.6em }, spacing: if compact { 0.4em } else { 0.8em })
#set list(indent: 0.9em, spacing: if compact { 0.3em } else { 0.5em })
#set enum(indent: 0.9em, spacing: if compact { 0.3em } else { 0.5em })
#set terms(hanging-indent: 1.5em)
#show link: set text(fill: navy)
#show link: underline

// Headings
#show heading: set text(fill: navy)
#show heading.where(level: 1): it => {
  v(if compact { 4pt } else { 14pt })
  text(size: if compact { 10.5pt } else { 15pt }, weight: 700)[#it.body]
  v(if compact { 1pt } else { 2pt }); line(length: 100%, stroke: 1.2pt + orange); v(if compact { 2pt } else { 3pt })
}
#show heading.where(level: 2): it => {
  v(if compact { 3pt } else { 10pt })
  text(size: if compact { 9pt } else { 12pt }, weight: 700, fill: orange)[#it.body]
  v(if compact { 1pt } else { 2pt })
}
#show heading.where(level: 3): it => {
  v(7pt); text(size: 10.5pt, weight: 700)[#it.body]; v(2pt)
}
#show heading.where(level: 4): it => {
  v(5pt); text(size: 9.5pt, weight: 700, fill: grey)[#it.body]; v(1pt)
}
#show heading.where(level: 5): it => { v(4pt); text(size: 9.5pt, weight: 700, style: "italic")[#it.body]; v(1pt) }
#show heading.where(level: 6): it => { v(4pt); text(size: 9pt, weight: 700, style: "italic", fill: grey)[#it.body]; v(1pt) }

// Tables: navy header row, zebra rows, breakable across pages
#set table(
  inset: if compact { (x: 4pt, y: 2.2pt) } else { (x: 5pt, y: 3.5pt) },
  stroke: (x, y) => (bottom: 0.5pt + rule),
  fill: (x, y) => if y == 0 { navy } else if calc.odd(y) { tint } else { white },
)
#show table.cell: set align(left + top)
#show table.cell.where(y: 0): set text(weight: 700, fill: white)
#show table: set text(size: if compact { 7.4pt } else { 8.2pt })
#show figure.where(kind: table): set block(breakable: true, width: 100%)
#show figure.where(kind: table): set figure.caption(position: top)
#show figure.where(kind: image): set figure.caption(position: bottom)
#show figure: set align(left)

// Code
#show raw: set text(font: ("Menlo", "DejaVu Sans Mono"))
#show raw.where(block: true): it => block(width: 100%, fill: tint, inset: 8pt, radius: 3pt,
  stroke: 0.5pt + rule, text(size: 7.8pt, it))
#show raw.where(block: false): it => box(fill: tint, inset: (x: 3pt, y: 0pt), outset: (y: 2pt),
  radius: 2pt, text(size: 8.3pt, it))

// Block quotes
#show quote.where(block: true): it => block(width: 100%, inset: (left: 10pt, right: 8pt, y: 6pt),
  stroke: (left: 2.5pt + orange), fill: rgb("#fbf7f3"), it.body)

// Horizontal rules (pandoc emits #horizontalRule / #divider)
#let horizontalRule = { v(3pt); line(length: 100%, stroke: 0.6pt + rule); v(3pt) }
#let divider(..args) = horizontalRule

$if(smart)$
$else$
#set smartquote(enabled: false)
$endif$
$for(header-includes)$
$header-includes$
$endfor$

// Title block
#block(below: if compact { 4pt } else { 14pt })[
  #text(size: 8pt, fill: orange, weight: 700, tracking: 0.09em)[GONKA TOKENOMICS & GTM RESEARCH]
  #v(1pt)
  #text(size: if compact { 13pt } else { 22pt }, weight: 700, fill: navy)[$title$]
  $if(subtitle)$
  #v(1pt)
  #text(size: if compact { 10pt } else { 13pt }, fill: grey)[$subtitle$]
  $endif$
  #v(if compact { 3pt } else { 6pt })
  #line(length: 100%, stroke: 1.5pt + orange)
]

$body$
