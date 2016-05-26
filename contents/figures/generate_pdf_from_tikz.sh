pdflatex -jobname $1 "\documentclass{standalone}\usepackage{tkz-graph,amsmath,bm}\begin{document}\newcommand{\vect}[1]{\bm{#1}}\input{$1.tikz}\end{document}"
 # && convert -density 150 $1.pdf -quality 90 $1.png
latex -jobname $1 "\documentclass{standalone}\usepackage{tkz-graph,amsmath,bm}\begin{document}\newcommand{\vect}[1]{\bm{#1}}\input{$1.tikz}\end{document}" && dvips $1.dvi
