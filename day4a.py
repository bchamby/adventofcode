#!/usr/bin/python

# import the hashlib library
import hashlib

# Create an initial number
num = 0

# Apparently, we can initialize a variable called var and assign it 1,
# and then start a while loop that will effectively create an infinite loop
var = 1
while var == 1:
  # From the instructions, our secret_key is iwrupvqb
  secret_key = 'iwrupvqb'
  # Create a prefix variable and assign a string value of five zeroes
  prefix = str('00000')
  # Create a new_key variable and assign it the secret key plus our number,
  # which is starting at zero.
  new_key = secret_key + str(num)
  # Calculate the hash (found instructions online)
  hash = hashlib.md5(new_key)
  # Create a variable called string and assign the "hex digest" (I dunno, also found this online)
  # I tested interactively with the Python interpreter and it seemed to give me an md5 hash
  # similar to what I would get running Powershell's Get-FileHash or 'openssl md5 <file>' on OS X / Linux
  string = hash.hexdigest()

  # if the MD5 hash starts with our prefix (five zeroes)
  if string.startswith(prefix):
    # Print the answer
    print "The answer is %s" % (num)
    # And break the while loop, so it doesn't run forever
    break
  # else, add one to the number and start the loop over again
  num += 1
