#!/usr/bin/env python

import sys

lines = sys.stdin.readlines()

s = 0
eps = '<epsilon>'
sp = '<space>'
for line in lines:
  name = line.strip()
  for i, letter in enumerate(name):
    if letter == ' ':
      letter = '<space>'
    if i == 0:
      print 0, s + 1, letter, name.replace(' ', '<space>')
    else:
      s = s + 1
      print s, s + 1, letter, eps
  s = s + 1
  print s
