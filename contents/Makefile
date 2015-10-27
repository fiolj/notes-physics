top_srcdir=$(PWD)/..
MNFILE := $(notdir $(PWD))

.SUFFIXES:
.SUFFIXES: .tex .dvi .pdf

.tex.dvi:
	latex -src-specials -interaction=nonstopmode $<

.tex.pdf:
	pdflatex -interaction=nonstopmode $<

main-2x1.pdf: main.pdf
	pdfjam --suffix nup --nup '2x1' --landscape --noautoscale 'true' --delta '0cm 0cm' --offset '-0.3cm .cm' --trim '1.5cm 1cm 1.5cm 1.2cm' --scale '.77' --outfile main-2up.pdf -- main.pdf 

.PHONY: web dist unpack bring send clean clean-all mostlyclean

SOURCES= approx.tex arbpot.tex atomestr.tex colis_molec.tex coupl_eq.tex ctmc.tex fglif.tex kinem.tex laser.tex main.tex manyel.tex math.tex nummeth.tex numpot.tex otros.tex photons.tex resolutions.tex revtdep.tex simult.tex spfunc.tex sumcalc.tex tcdwn.tex tcdw.tex timedep.tex txs.tex 
#	parttd.tex partti.tex 	


HTMLDIR= html
EPUBDIR= epubdir

EXCLUDING= --exclude='*.aux' --exclude='*.log' --exclude='*.toc' --exclude='*.out' \
     --exclude='*~' --exclude='*.bak' --exclude='*-2x1.pdf' \
     --exclude='*.blg' --exclude='*.bbl' --exclude='auto'\
     --exclude='*.idx' --exclude='cvs' --exclude='CVS' \
     --exclude='*.aux'  --exclude='*.log' --exclude='.svn' \
     --exclude='_region_.*' --exclude='main.prv/***' --exclude='tmp*'

html: html/main.html

html/main.html: $(SOURCES) Makefile
	cp -r figures $(SOURCES) main.bib  $(HTMLDIR)/
	cd $(HTMLDIR); pdflatex main.tex; biber main.tex; pdflatex main.tex; mk4ht xhlatex main.tex "xhtml,2,charset=utf-8,frames" " -cunihtf -utf8" " -cdvipng"; rm figures $(SOURCES) main.bib -fr; cd ..

epub: $(EPUBDIR)/main.epub

$(EPUBDIR)/main.epub: $(SOURCES) $(EPUBDIR)/main.html
	cd $(EPUBDIR); ebook-convert main.html main.epub; cd -

$(EPUBDIR)/main.html: 
	cp -r figures $(SOURCES) main.bib  $(EPUBDIR)/
	cd $(EPUBDIR); pdflatex main.tex; bibtex main.aux; pdflatex main.tex; pdflatex main.tex; mk4ht xhlatex main.tex "xhtml,charset=utf-8" " -cunihtf -utf8" " -cdvipng"; 	rm figures $(SOURCES) main.bib -fr;	cd -

web: main.pdf html epub



clean:
	rm -f *.aux *.log *.toc *.idx *~ *.bbl *.blg *.bak

clean-all: clean
	rm -f *.dvi *.pdf

# put-all: put
# 	rsync --update --verbose -rtoz --cvs-exclude  $(HOME)/texmf/bibtex/bib $(PENDRIVE)/texmf/bibtex/
