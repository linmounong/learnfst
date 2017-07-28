all: draw

build/man.fst: build man.fst.txt
	fstcompile --isymbols=data/ascii.syms --osymbols=data/wotw.syms < man.fst.txt > build/man.fst

build/Martian.fst: build Martian.fst.txt
	fstcompile --isymbols=data/ascii.syms --osymbols=data/wotw.syms < Martian.fst.txt > build/Martian.fst

build/Mars.fst: build Mars.fst.txt
	fstcompile --isymbols=data/ascii.syms --osymbols=data/wotw.syms < Mars.fst.txt > build/Mars.fst

build/lexicon.fst: build/Mars.fst build/Martian.fst build/man.fst
	cd build && fstunion man.fst Mars.fst | fstunion - Martian.fst | fstclosure > lexicon.fst

build:
	mkdir -p build

clean:
	rm -rf build

draw: build/lexicon.pdf build/Mars.pdf build/Martian.pdf build/man.pdf
	nautilus build

build/Mars.pdf: build/Mars.fst
	fstdraw --isymbols=data/ascii.syms --osymbols=data/wotw.syms -portrait build/Mars.fst | dot -Tpdf > build/Mars.pdf

build/Martian.pdf: build/Martian.fst
	fstdraw --isymbols=data/ascii.syms --osymbols=data/wotw.syms -portrait build/Martian.fst | dot -Tpdf > build/Martian.pdf

build/man.pdf: build/man.fst
	fstdraw --isymbols=data/ascii.syms --osymbols=data/wotw.syms -portrait build/man.fst | dot -Tpdf > build/man.pdf

build/lexicon.pdf: build/lexicon.fst
	fstdraw --isymbols=data/ascii.syms --osymbols=data/wotw.syms -portrait build/lexicon.fst | dot -Tpdf > build/lexicon.pdf
