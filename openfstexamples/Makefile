SHELL=/bin/bash -o pipefail

all: draw a1 a2 a4

clean:
	rm -f *.pdf *.fst *.txt *.pairs

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

# exercise 5

marsman.fst: Marsman.fst downcase.fst
	fstproject Marsman.fst | fstcompose - downcase.fst | fstproject --project_output > $@

wotw.lm.fst:
	gzip -dc data/wotw.lm.gz | fstcompile --isymbols=data/wotw.syms --osymbols=data/wotw.syms > $@

prediction.fst: downcase.fst marsman.fst lex_opt.fst wotw.lm.fst
	fstcompose downcase.fst marsman.fst | fstinvert | fstcompose - lex_opt.fst | fstcompose - wotw.lm.fst | fstproject --project_output | fstshortestpath | fstrmepsilon | fsttopsort > $@

# NOTE disabled, hard to compile
# lex_lookahead.fst: lex_opt.fst
# 	fstconvert --fst_type=olabel_lookahead --save_relabel_opairs=relabel.pairs $< > $@
# 
# wotw_relabel.lm.fst: wotw.lm.fst lex_lookahead.fst
# 	fstrelabel --relabel_ipairs=relabel.pairs wotw.lm.fst | fstarcsort --sort_type=ilabel > $@
# 
# wotw.fst: lex_lookahead.fst wotw_relabel.lm.fst
# 	fstcompose $? > $@
# 
# case_restore.fst: downcase.fst wotw.fst
# 	fstinvert downcase.fst | fstcompose - wotw.fst > $@

a5a.fst: downcase.fst marsman.fst lex_opt.fst wotw.lm.fst
	fstcompose downcase.fst marsman.fst | fstinvert | fstcompose - lex_opt.fst | fstcompose - wotw.lm.fst | fstproject --project_output | fstrmepsilon | fstshortestpath --unique=true --nshortest=2 | fstrmepsilon | fsttopsort > $@

ac.fst: prediction.fst
	fstencode --encode_weights $< /dev/null | fstproject --project_output | fstrmepsilon > $@

a5b.fst: downcase.fst marsman.fst lex_opt.fst wotw.lm.fst ac.fst
	fstcompose downcase.fst marsman.fst | fstinvert | fstcompose - lex_opt.fst | fstcompose - wotw.lm.fst | fstproject --project_output | fstdifference - ac.fst | fstshortestpath | fstrmepsilon | fsttopsort > $@

# pdf

draw: punct.pdf small_numbers.pdf a1.pdf a2b.pdf Marsman.pdf Marsman_tokens.pdf marsman.pdf a5a.pdf a5b.pdf
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

marsman.pdf: marsman.fst
	fstdraw --isymbols=data/ascii.syms --osymbols=data/ascii.syms -portrait $< | dot -Tpdf > $@

a5a.pdf: a5a.fst
	fstdraw --isymbols=data/wotw.syms --osymbols=data/wotw.syms -portrait $< | dot -Tpdf > $@

a5b.pdf: a5b.fst
	fstdraw --isymbols=data/wotw.syms --osymbols=data/wotw.syms -portrait $< | dot -Tpdf > $@

