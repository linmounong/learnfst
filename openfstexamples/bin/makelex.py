#!/usr/bin/env python

import sys

lines = sys.stdin.readlines()

s = 0
eps = '<epsilon>'
for line in lines:
  cols = line.split()
  if cols[1] == '0':
    continue  # epsilon
  word = cols[0]
  letters = list(word)
  for i in range(0, len(letters)):
    if i == 0:
      print 0, s + 1, letters[i], word
    else:
      s = s + 1
      print s, s + 1, letters[i], eps
  s = s + 1
  print s
