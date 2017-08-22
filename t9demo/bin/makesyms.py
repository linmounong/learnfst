#!/usr/bin/env python

import sys

lines = sys.stdin.readlines()

s = 0
eps = '<epsilon>'
sp = '<space>'
print '%s\t%s' % (eps, s)
for line in lines:
  s += 1
  name = line.strip().replace(' ', '<space>')
  print name, s
