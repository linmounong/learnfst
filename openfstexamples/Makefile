all: draw

clean:
	rm *.pdf *.fst *.txt

# fst txt

lex.fst.txt:
	./bin/makelex.py < data/wotw.syms > lex.fst.txt

Marsman.fst.txt:
	echo "Mars man!" | ./bin/makeinput.py > Marsman.fst.txt


# fst

lex.fst: lex.fst.txt punct.fst
	fstcompile --isymbols=data/ascii.syms --osymbols=data/wotw.syms < lex.fst.txt | fstunion - prebuilt/numbers.fst | fstconcat - punct.fst | fstclosure > lex.fst

lex_opt.fst: lex.fst
	fstrmepsilon lex.fst | fstdeterminize | fstminimize > lex_opt.fst

punct.fst:
	fstcompile --isymbols=data/ascii.syms --osymbols=data/wotw.syms < data/full_punct.txt > punct.fst

Marsman.fst: Marsman.fst.txt
	fstcompile --isymbols=data/ascii.syms --osymbols=data/ascii.syms < Marsman.fst.txt > Marsman.fst

small_numbers.fst:
	./bin/makenumbers.py 100 | fstcompile --isymbols=data/ascii.syms --osymbols=data/wotw.syms | fstrmepsilon | fstdeterminize | fstminimize > small_numbers.fst

tokens.fst: Marsman.fst lex_opt.fst
	fstcompose Marsman.fst lex_opt.fst | fstproject --project_output | fstrmepsilon > tokens.fst

q1.fst:
	echo "Mars is 4225 miles across." | ./bin/makeinput.py | fstcompile --isymbols=data/ascii.syms --osymbols=data/ascii.syms > q1.fst

sol1.fst: q1.fst lex_opt.fst
	fstcompose q1.fst lex_opt.fst | fstproject --project_output | fstrmepsilon > sol1.fst

q2b.fst:
	echo "num_final_states" | ./bin/makeinput.py | fstcompile --isymbols=data/ascii.syms --osymbols=data/ascii.syms > q2b.fst

camelcase.fst:
	./bin/make2b.py | fstcompile --isymbols=data/ascii.syms --osymbols=data/ascii.syms > camelcase.fst

sol2b.fst: camelcase.fst q2b.fst
	fstcompose q2b.fst camelcase.fst | fstproject --project_output | fstrmepsilon > sol2b.fst






# prebuilt fst

prebuild: prebuilt/numbers.fst

prebuilt:
	mkdir -p prebuilt

prebuilt/numbers.fst: prebuilt
	./bin/makenumbers.py | fstcompile --isymbols=data/ascii.syms --osymbols=data/wotw.syms | fstrmepsilon | fstdeterminize | fstminimize > prebuilt/numbers.fst

# pdf

draw: punct.pdf Marsman.pdf tokens.pdf small_numbers.pdf sol1.pdf sol2.pdf
	nautilus .

punct.pdf: punct.fst
	fstdraw --isymbols=data/ascii.syms --osymbols=data/wotw.syms -portrait punct.fst | dot -Tpdf > punct.pdf

Marsman.pdf: Marsman.fst
	fstdraw --isymbols=data/ascii.syms --osymbols=data/ascii.syms -portrait Marsman.fst | dot -Tpdf > Marsman.pdf

small_numbers.pdf: small_numbers.fst
	fstdraw --isymbols=data/ascii.syms --osymbols=data/wotw.syms -portrait small_numbers.fst | dot -Tpdf > small_numbers.pdf

tokens.pdf: tokens.fst
	fstdraw --isymbols=data/wotw.syms --osymbols=data/wotw.syms -portrait tokens.fst | dot -Tpdf > tokens.pdf

sol1.pdf: sol1.fst
	fstdraw --isymbols=data/wotw.syms --osymbols=data/wotw.syms -portrait sol1.fst | dot -Tpdf > sol1.pdf

sol2b.pdf: sol2b.fst
	fstdraw --isymbols=data/ascii.syms --osymbols=data/ascii.syms -portrait sol2b.fst | dot -Tpdf > sol2b.pdf
