#!/usr/bin/env python

import itertools
import num2words
import re
import sys

EPS = '<epsilon>'


# [start, end]
def foo(start, end):
  s = 1
  for i in range(start, end + 1):
    words = re.split('\W+', num2words.num2words(i))  # removes delimiters
    isym = str(i)
    prev = 0
    for isym, osym in itertools.izip_longest(str(i), words, fillvalue=EPS):
      print prev, s, isym, osym
      prev = s
      s += 1
    print s - 1  # finish state


if __name__ == '__main__':
  start = 0
  end = 999999
  if len(sys.argv) > 1:
    end = int(sys.argv[1])
  if len(sys.argv) > 2:
    start = end
    end = int(sys.argv[2])
  foo(start, end)
