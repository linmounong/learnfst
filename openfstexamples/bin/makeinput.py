#! /usr/bin/python

import sys

lines = sys.stdin.readlines()

s = 0
sp = '<space>'
for line in lines:
  for c in line.strip():
    if c == ' ':
      c = sp
    print s, s + 1, c, c
    s += 1
print s
