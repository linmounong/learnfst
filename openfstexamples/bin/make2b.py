#!/usr/bin/env python

import string

EPS = '<epsilon>'

def foo():
  for x in string.ascii_lowercase:
      print 0, 1, x, x.upper()
  for x in string.ascii_lowercase:
      print 1, 1, x, x
  print 1, 2, '_', EPS
  for x in string.ascii_lowercase:
      print 2, 1, x, x.upper()
  print 1

if __name__ == '__main__':
  foo()
