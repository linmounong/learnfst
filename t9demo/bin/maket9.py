#!/usr/bin/env python

SP = '<space>'
MAPPING = {
  0: [SP],
  1: '.',
  2: 'abc',
  3: 'def',
  4: 'ghi',
  5: 'jkl',
  6: 'mno',
  7: 'pqrs',
  8: 'tuv',
  9: 'wxyz',
}


def foo():
  for digit, syms in MAPPING.iteritems():
    for sym in syms:
      print 0, 0, digit, sym
  print 0


if __name__ == '__main__':
  foo()
