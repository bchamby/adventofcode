#!/usr/bin/python

# Create initial count at zero
total = 0

# Open file
file = open('day2input.txt')
# For each line in the file
for line in file.readlines():
  # Create width, height, and length variables splitting the line at x and referencing
  # elements 1, 2, and 3 (the index is zero-based)
  w = line.split("x")[0]
  h = line.split("x")[1]
  l = line.split("x")[2]
  # By default, these are strings, so we'll use the int method to make them integers
  w = int(w)
  h = int(h)
  l = int(l)
  # Create a list with the width, height, and length variables
  list = [w, h, l]
  # Sort the list, from smallest to largest (I guess this is the default with "sorted")
  list2 = sorted(list, key=int)
  # Grab the smallest and second smallest
  # The instructions were helpful enough to explain that this is how we measure the 
  # amount of ribbon we need.
  fir = list2[0]
  sec = list2[1]
  # Calculate the total amount of ribbon needed. Again, the instructions helped us
  # know the formula.
  total = total + (fir + fir + sec + sec) + (w * h * l)

# Print the answer
print "The elves should order %s feet of ribbon" % (total)
