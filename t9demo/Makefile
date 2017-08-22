clean:
	rm -f *.pdf *.fst *.txt

t9.fst: digit2abc.fst case_restore.fst lex_opt.fst
	fstcompose digit2abc.fst case_restore.fst | fstcompose - lex_opt.fst > t9.fst

t9.pdf: t9.fst
	fstdraw --isymbols=data/ascii.syms --osymbols=data/us_presidents.syms -portrait $< | dot -Tpdf > $@

t9_opt.fst: t9.fst
	fstrmepsilon $< | fstdeterminize | fstminimize | fstarcsort --sort_type=ilabel > $@

t9_opt.pdf: t9_opt.fst
	fstdraw --isymbols=data/ascii.syms --osymbols=data/us_presidents.syms -portrait $< | dot -Tpdf > $@

lex.fst.txt:
	./bin/makelex.py < data/us_presidents.txt > $@

lex.fst: lex.fst.txt
	fstcompile --isymbols=data/ascii.syms --osymbols=data/us_presidents.syms < lex.fst.txt > $@

lex.pdf: lex.fst
	fstdraw --isymbols=data/ascii.syms --osymbols=data/us_presidents.syms -portrait $< | dot -Tpdf > $@

lex_opt.fst: lex.fst
	fstrmepsilon $< | fstdeterminize | fstminimize | fstarcsort --sort_type=ilabel > $@

lex_opt.pdf: lex_opt.fst
	fstdraw --isymbols=data/ascii.syms --osymbols=data/us_presidents.syms -portrait $< | dot -Tpdf > $@

obama_digits.fst:
	echo "227225062262" | ./bin/makeinput.py | fstcompile --isymbols=data/ascii.syms --osymbols=data/ascii.syms > $@

obama.fst: obama_digits.fst t9_opt.fst
	fstcompose $? | fstproject --project_output | fstrmepsilon > $@

obama.pdf: obama.fst
	fstdraw --isymbols=data/us_presidents.syms --osymbols=data/us_presidents.syms -portrait $< | dot -Tpdf > $@

downcase.fst:
	fstcompile --isymbols=data/ascii.syms --osymbols=data/ascii.syms < data/downcase.fst.txt > $@

downcase.pdf: downcase.fst
	fstdraw --isymbols=data/ascii.syms --osymbols=data/ascii.syms -portrait $< | dot -Tpdf > $@

case_restore.fst: downcase.fst
	fstinvert $< $@

case_restore.pdf: case_restore.fst
	fstdraw --isymbols=data/ascii.syms --osymbols=data/ascii.syms -portrait $< | dot -Tpdf > $@

digit2abc.fst:
	./bin/maket9.py | fstcompile --isymbols=data/ascii.syms --osymbols=data/ascii.syms > $@

digit2abc.pdf: digit2abc.fst
	fstdraw --isymbols=data/ascii.syms --osymbols=data/ascii.syms -portrait $< | dot -Tpdf > $@

abc2digit.fst: digit2abc.fst
	fstinvert $< $@

abc2digit.pdf: abc2digit.fst
	fstdraw --isymbols=data/ascii.syms --osymbols=data/ascii.syms -portrait $< | dot -Tpdf > $@
