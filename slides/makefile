# Name of manuscript
manuscript = slides

# Source files
sources = $(wildcard *.tex) *.bib

# PdfLaTeX compilation options
latexopt = -halt-on-error -file-line-error -shell-escape

#=================================================================
# Generate PDF of manuscript using PdfLaTeX
#=================================================================

all: $(manuscript).pdf

$(manuscript).pdf: $(sources)
	pdflatex $(latexopt) $(manuscript).tex
	bibtex -terse $(manuscript).aux
	bibtex Mypub
	pdflatex $(latexopt) $(manuscript).tex
	pdflatex $(latexopt) $(manuscript).tex

#=================================================================
# Generate Images
#=================================================================

#=================================================================
# Other
#=================================================================

clean:
	@rm -f *.aux *.bbl *.blg *.log *.out *.spl *.lof *.lot *.toc *.backup *.snm *.nav

.PHONY: all clean
