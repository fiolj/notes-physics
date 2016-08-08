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

SOURCES=absorption_rotovib.tex angmom.tex approx.tex arbpot.tex atomestr.tex cluster_reaction.tex colis_molec.tex ctmc.tex coupl_eq.tex fglif.tex kinem.tex laser.tex main.tex manyel.tex math.tex molec_simple.tex nummeth.tex numpot.tex photons.tex resolutions.tex spfunc.tex sumcalc.tex tcdw.tex timedep.tex txs.tex

# approx.tex arbpot.tex atomestr.tex colis_molec.tex coupl_eq.tex ctmc.tex fglif.tex kinem.tex laser.tex main.tex manyel.tex math.tex nummeth.tex numpot.tex otros.tex photons.tex resolutions.tex revtdep.tex simult.tex spfunc.tex sumcalc.tex tcdwn.tex tcdw.tex timedep.tex txs.tex 

#	parttd.tex partti.tex 	

BIBEXTRACT="/home/fiol/trabajo/programas/biblio-py/scripts/bibextract.py" 

HTMLDIR= html
EPUBDIR= epubdir

EXCLUDING= --exclude='*.aux' --exclude='*.log' --exclude='*.toc' --exclude='*.out' \
     --exclude='*~' --exclude='*.bak' --exclude='*-2x1.pdf' \
     --exclude='*.blg' --exclude='*.bbl' --exclude='auto'\
     --exclude='*.idx' --exclude='cvs' --exclude='CVS' \
     --exclude='*.aux'  --exclude='*.log' --exclude='.svn' \
     --exclude='_region_.*' --exclude='main.prv/***' --exclude='tmp*'

html: html/main.html

# tex4htsty_opt="main_4ht,xhtml,2,mathml,charset=utf-8,frames"
tex4htsty_opt="main_4ht"
tex4ht_opt=" -cunihtf -utf8"
latex_opt="-cvalidate"
COPYFILES=figures $(SOURCES) main_4ht.cfg

html/main.html: $(SOURCES) main.tex Makefile
	cp -r $(COPYFILES)  main.bbl $(HTMLDIR)/
	cd $(HTMLDIR); mk4ht xhlatex main.tex $(tex4htsty_opt) $(tex4ht_opt) $(latex_opt)

htmlchapter: html/chapter.html

html/chapter.html: $(SOURCES) chapter.tex Makefile
	cp -r $(COPYFILES) chapter.tex chapter.bbl $(HTMLDIR)/
	cd $(HTMLDIR); mk4ht xhlatex chapter.tex $(tex4htsty_opt) $(tex4ht_opt) $(latex_opt); rm $(COPYFILES) chapter.tex chapter.bbl -fr


epub: $(EPUBDIR)/main.epub

$(EPUBDIR)/main.epub: $(SOURCES) $(EPUBDIR)/main.html
	cd $(EPUBDIR); ebook-convert main.html main.epub; cd -

$(EPUBDIR)/main.html: 
	cp -r figures $(SOURCES) main.bib  $(EPUBDIR)/
	cd $(EPUBDIR); pdflatex main.tex; biber main; pdflatex main.tex; pdflatex main.tex; mk4ht xhlatex main.tex "xhtml,charset=utf-8" " -cunihtf -utf8" " -cdvipng"#; rm figures $(SOURCES) main.bib -fr;	cd -

web: main.pdf html epub

biblio: main.bib

main.bib:$(SOURCES)
	$(BIBEXTRACT) --remove-common --remove-fields=file  -d $(BIBDB) main.aux;



clean:
	rm -f *.aux *.log *.toc *.idx *~ *.bbl *.blg *.bak

clean-html:
	rm -fr html/*

clean-all: clean clean-html
	rm -f *.dvi *.pdf

# put-all: put
# 	rsync --update --verbose -rtoz --cvs-exclude  $(HOME)/texmf/bibtex/bib $(PENDRIVE)/texmf/bibtex/
