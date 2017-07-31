all: draw

clean:
	rm *.pdf *.fst *.txt

# fst txt

lex.fst.txt:
	python bin/makelex.py < data/wotw.syms > lex.fst.txt

Marsman.fst.txt:
	echo "Mars man!" | python bin/makeinput.py > Marsman.fst.txt

# fst

lex.fst: lex.fst.txt punct.fst
	fstcompile --isymbols=data/ascii.syms --osymbols=data/wotw.syms < lex.fst.txt | fstconcat - punct.fst | fstclosure > lex.fst

lex_opt.fst: lex.fst
	fstrmepsilon lex.fst | fstdeterminize | fstminimize > lex_opt.fst

punct.fst:
	fstcompile --isymbols=data/ascii.syms --osymbols=data/wotw.syms < data/full_punct.txt > punct.fst

Marsman.fst: Marsman.fst.txt
	fstcompile --isymbols=data/ascii.syms --osymbols=data/ascii.syms < Marsman.fst.txt > Marsman.fst

tokens.fst: Marsman.fst lex_opt.fst
	fstcompose Marsman.fst lex_opt.fst | fstproject --project_output | fstrmepsilon > tokens.fst

# pdf

draw: punct.pdf Marsman.pdf tokens.pdf
	nautilus .

punct.pdf: punct.fst
	fstdraw --isymbols=data/ascii.syms --osymbols=data/wotw.syms -portrait punct.fst | dot -Tpdf > punct.pdf

tokens.pdf: tokens.fst
	fstdraw --isymbols=data/wotw.syms --osymbols=data/wotw.syms -portrait tokens.fst | dot -Tpdf > tokens.pdf

Marsman.pdf: Marsman.fst
	fstdraw --isymbols=data/ascii.syms --osymbols=data/ascii.syms -portrait Marsman.fst | dot -Tpdf > Marsman.pdf

