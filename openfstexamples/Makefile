SHELL = /bin/bash -o pipefail

all: draw a1 a2 a4

clean:
	rm -f *.pdf *.fst *.txt

# delete output on errors
.DELETE_ON_ERRORS:

# fst txt

lex.fst.txt:
	./bin/makelex.py < data/wotw.syms > $@

# basic fst

lex.fst: lex.fst.txt punct.fst
	fstcompile --isymbols=data/ascii.syms --osymbols=data/wotw.syms < lex.fst.txt | fstunion - prebuilt/numbers.fst | fstconcat - punct.fst | fstclosure > $@

lex_opt.fst: lex.fst
	fstrmepsilon $< | fstdeterminize | fstminimize | fstarcsort --sort_type=ilabel > $@

punct.fst:
	fstcompile --isymbols=data/ascii.syms --osymbols=data/wotw.syms < data/full_punct.txt > $@

downcase.fst:
	fstcompile --isymbols=data/ascii.syms --osymbols=data/ascii.syms < data/full_downcase.txt > $@

small_numbers.fst:
	./bin/makenumbers.py 100 | fstcompile --isymbols=data/ascii.syms --osymbols=data/wotw.syms | fstrmepsilon | fstdeterminize | fstminimize > $@

# prebuilt fst, not build by default

prebuild: prebuilt/numbers.fst

prebuilt:
	mkdir -p $@

prebuilt/numbers.fst: prebuilt
	./bin/makenumbers.py | fstcompile --isymbols=data/ascii.syms --osymbols=data/wotw.syms | fstrmepsilon | fstdeterminize | fstminimize > $@

# Mars man (for testing)

Marsman.fst.txt:
	echo "Mars man!" | ./bin/makeinput.py > $@

Marsman.fst: Marsman.fst.txt
	fstcompile --isymbols=data/ascii.syms --osymbols=data/ascii.syms < $< > $@

Marsman_tokens.fst: Marsman.fst lex_opt.fst
	fstcompose $? | fstproject --project_output | fstrmepsilon > $@

# exercise 1

q1.fst:
	echo "Mars is 4225 miles across." | ./bin/makeinput.py | fstcompile --isymbols=data/ascii.syms --osymbols=data/ascii.syms > $@

a1: a1.fst

a1.fst: q1.fst lex_opt.fst
	fstcompose q1.fst lex_opt.fst | fstproject --project_output | fstrmepsilon > $@

# exercise 2

q2b.fst:
	echo "num_final_states" | ./bin/makeinput.py | fstcompile --isymbols=data/ascii.syms --osymbols=data/ascii.syms > $@

camelcase.fst:
	./bin/make2b.py | fstcompile --isymbols=data/ascii.syms --osymbols=data/ascii.syms > $@

a2: a2b.fst

a2b.fst: q2b.fst camelcase.fst
	fstcompose $? | fstproject --project_output | fstrmepsilon > $@

# exercise 4

q4.fst:
	./bin/makerandstring.sh 1000000 | ./bin/makeinput.py | fstcompile --isymbols=data/ascii.syms --osymbols=data/ascii.syms > $@

a4: a4_xxxx_Aa_isorted.fst a4_Aa_xxxx_isorted.fst a4_xxxx_Aa_osorted.fst a4_Aa_xxxx_osorted.fst

downcase_isorted.fst: downcase.fst
	fstarcsort --sort_type=ilabel $< $@

downcase_osorted.fst: downcase.fst
	fstarcsort --sort_type=olabel $< $@

a4_xxxx_Aa_isorted.fst: q4.fst downcase_isorted.fst
	time fstcompose $? $@

a4_xxxx_Aa_osorted.fst: q4.fst downcase_osorted.fst
	time fstcompose $? $@

a4_Aa_xxxx_isorted.fst: downcase_isorted.fst q4.fst
	time fstcompose $? $@

a4_Aa_xxxx_osorted.fst: downcase_osorted.fst q4.fst
	time fstcompose $? $@

# pdf

draw: punct.pdf small_numbers.pdf a1.pdf a2b.pdf Marsman.pdf Marsman_tokens.pdf
	nautilus .

punct.pdf: punct.fst
	fstdraw --isymbols=data/ascii.syms --osymbols=data/wotw.syms -portrait $< | dot -Tpdf > $@

small_numbers.pdf: small_numbers.fst
	fstdraw --isymbols=data/ascii.syms --osymbols=data/wotw.syms -portrait $< | dot -Tpdf > $@

a1.pdf: a1.fst
	fstdraw --isymbols=data/wotw.syms --osymbols=data/wotw.syms -portrait $< | dot -Tpdf > $@

a2b.pdf: a2b.fst
	fstdraw --isymbols=data/ascii.syms --osymbols=data/ascii.syms -portrait $< | dot -Tpdf > $@

Marsman.pdf: Marsman.fst
	fstdraw --isymbols=data/ascii.syms --osymbols=data/ascii.syms -portrait $< | dot -Tpdf > $@

Marsman_tokens.pdf: Marsman_tokens.fst
	fstdraw --isymbols=data/wotw.syms --osymbols=data/wotw.syms -portrait $< | dot -Tpdf > $@
