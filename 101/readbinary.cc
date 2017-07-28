#include <fst/fstlib.h>
#include <stdio.h>
#include <memory>

using fst::StdFst;
using fst::StdArc;
using fst::StateIterator;
using fst::ArcIterator;

void foo(const string &filename) {
  std::unique_ptr<StdFst> fst(StdFst::Read(filename));
  printf("=== fst %s\n", filename.c_str());
  for (StateIterator<StdFst> siter(*fst); !siter.Done(); siter.Next()) {
    StdFst::StateId s = siter.Value();
    printf("state %d\n", s);
    for (ArcIterator<StdFst> aiter(*fst, s); !aiter.Done(); aiter.Next()) {
      const StdArc &arc = aiter.Value();
      printf("  ->%d %d:%d/%f\n", arc.nextstate, arc.ilabel, arc.olabel,
             arc.weight.Value());
    }
  }
}

int main() {
  foo("A.fst");
  foo("B.fst");
}
