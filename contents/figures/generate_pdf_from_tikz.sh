pdflatex -jobname $1 "\documentclass{standalone}\usepackage{tkz-graph,amsmath}\begin{document}\input{$1.tikz}\end{document}" && convert -density 150 $1.pdf -quality 90 $1_p.png
