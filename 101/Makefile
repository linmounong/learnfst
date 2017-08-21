test: build build/readbinary build/A.fst build/B.fst
	cd build && ./readbinary

build/composebinary: build composebinary.cc
	g++ -std=c++11 composebinary.cc -ldl -lfst -o build/composebinary

build/readbinary: build readbinary.cc
	g++ -std=c++11 readbinary.cc -ldl -lfst -o build/readbinary

build/A.fst build/B.fst: build build/genbinary
	cd build && ./genbinary

build/AB.fst: build/A.fst build/B.fst build/composebinary
	cd build && ./composebinary

build/genbinary: genbinary.cc build
	g++ -std=c++11 genbinary.cc -ldl -lfst -o build/genbinary

build:
	mkdir -p build

clean:
	rm -rf build

draw: build/A.png build/B.png build/AB.png
	nautilus build

build/A.png: isyms.A.txt osyms.A.txt build build/A.fst
	fstdraw --isymbols=isyms.A.txt --osymbols=osyms.A.txt --portrait build/A.fst build/A.dot
	dot -Tpng build/A.dot > build/A.png

build/B.png: isyms.B.txt osyms.B.txt build build/B.fst
	fstdraw --isymbols=isyms.B.txt --osymbols=osyms.B.txt --portrait build/B.fst build/B.dot
	dot -Tpng build/B.dot > build/B.png

build/AB.png: isyms.A.txt osyms.B.txt build build/AB.fst
	fstdraw --isymbols=isyms.A.txt --osymbols=osyms.B.txt --portrait build/AB.fst build/AB.dot
	dot -Tpng build/AB.dot > build/AB.png
