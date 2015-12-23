#!/usr/bin/python

import re

vowel = ('a','e','i','o','u')
nice_string = []
bad1 = 'ab'
bad2 = 'cd'
bad3 = 'pq'
bad4 = 'xy'

file = open('day5ainput.txt')
for line in file.readlines():
  numvowels = 0
  for i in line:
    if i in vowel:
      numvowels += 1
    if numvowels >= 3:
      result = re.findall(r"(.)\1", line)
      if len(result) > 0:
        if not line.find(bad1) > 0:
          if not line.find(bad2) > 0:
            if not line.find(bad3) > 0:
              if not line.find(bad4) > 0:
                nice_string.append(line)

count = len(set(nice_string))

print "The answer is %s" % (count)