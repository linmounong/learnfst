#!/usr/bin/env python

import sys

SYMS = [
  '<space>',
  '!',
  '"',
  '#',
  '$',
  '%',
  '&',
  '\'',
  '(',
  ')',
  '*',
  '+',
  ',',
  '-',
  '.',
  '/',
  '0',
  '1',
  '2',
  '3',
  '4',
  '5',
  '6',
  '7',
  '8',
  '9',
  ':',
  ';',
  '<',
  '=',
  '>',
  '?',
  '@',
  'A',
  'B',
  'C',
  'D',
  'E',
  'F',
  'G',
  'H',
  'I',
  'J',
  'K',
  'L',
  'M',
  'N',
  'O',
  'P',
  'Q',
  'R',
  'S',
  'T',
  'U',
  'V',
  'W',
  'X',
  'Y',
  'Z',
  '[',
  # '\\',
  ']',
  '^',
  '_',
  '`',
  'a',
  'b',
  'c',
  'd',
  'e',
  'f',
  'g',
  'h',
  'i',
  'j',
  'k',
  'l',
  'm',
  'n',
  'o',
  'p',
  'q',
  'r',
  's',
  't',
  'u',
  'v',
  'w',
  'x',
  'y',
  'z',
  '{',
  '|',
  '}',
  '~',
]
INS = '<ins>'
DEL = '<del>'
SUB = '<sub>'
EPS = '<epsilon>'
N = 3


def foo():
  print 0, 0, EPS, INS, 0.5
  for sym in SYMS:
    print 0, 0, sym, sym
    print 0, 0, sym, SUB, 0.5
    print 0, 0, sym, DEL, 0.5
  print 0


def bar():
  print 0, 0, DEL, EPS, 0.5
  for sym in SYMS:
    print 0, 0, sym, sym
    print 0, 0, SUB, sym, 0.5
    print 0, 0, INS, sym, 0.5
  print 0


def baz():
  print 0
  print 1, 0, SUB, SUB
  for sym in SYMS:
    print 1, 0, sym, sym
  print 0, 1, EPS, EPS

  s = 2
  print 0, s, INS, INS
  for _ in range(N - 1):
    print s, s + 1, INS, INS
    s += 1
  print s, 1, EPS, EPS
  print s
  print s, s + 1, DEL, DEL

  s += 1
  print 0, s, DEL, DEL
  for _ in range(N - 1):
    print s, s + 1, DEL, DEL
    s += 1
  print s, 1, EPS, EPS
  print s
  print s, 2, INS, INS


if __name__ == '__main__':
  if len(sys.argv) >= 2 and sys.argv[1] == '2':
    bar()
  elif len(sys.argv) >= 2 and sys.argv[1] == '3':
    baz()
  else:
    foo()
