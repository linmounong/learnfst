#include <fst/fstlib.h>
#include <memory>

using fst::StdFst;
using fst::StdArc;
using fst::ComposeFst;
using fst::StdVectorFst;

void Compose() {
  std::unique_ptr<StdFst> A(StdFst::Read("A.fst"));
  std::unique_ptr<StdFst> B(StdFst::Read("B.fst"));
  StdVectorFst AB(ComposeFst<StdArc>(*A, *B));
  AB.Write("AB.fst");
}

int main() {
  Compose();
  return 0;
}
