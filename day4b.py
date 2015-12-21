#!/usr/bin/python

# For instructions, just review day4a.py
# Interestingly, the puzzle is the exact same, exact they say to look
# for the first md5 hash that starts with six zeroeos.
# Maybe the idea is to reinforce how powerful computers and programming languages are?

import hashlib

num = 0

var = 1
while var == 1:
  secret_key = 'iwrupvqb'
  prefix = str('000000')
  new_key = secret_key + str(num)
  hash = hashlib.md5(new_key)
  string = hash.hexdigest()
  if string.startswith(prefix):
    print "The answer is %s" % (num)
    break
  num += 1
