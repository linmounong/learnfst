#include <fst/fstlib.h>

using fst::StdVectorFst;
using fst::StdArc;

void GenA() {
  StdVectorFst fst;

  fst.AddState();
  fst.SetStart(0);
  fst.AddArc(0, StdArc(1, 2, 1, 1));
  fst.AddArc(0, StdArc(1, 3, 2.5, 2));

  fst.AddState();
  fst.AddArc(1, StdArc(2, 1, 1, 1));
  fst.SetFinal(1, 0);

  fst.AddState();
  fst.SetFinal(2, 2.5);

  fst.Write("A.fst");
}

void GenB() {
  StdVectorFst fst;

  fst.AddState();
  fst.SetStart(0);
  fst.AddArc(0, StdArc(2, 1, 1, 1));
  fst.AddArc(0, StdArc(3, 2, 3, 2));

  fst.AddState();
  fst.AddArc(1, StdArc(1, 3, 2.5, 2));

  fst.AddState();
  fst.SetFinal(2, 2);
  fst.AddArc(2, StdArc(1, 4, 1.5, 2));

  fst.Write("B.fst");
}

int main() {
  GenA();
  GenB();
  return 0;
}
