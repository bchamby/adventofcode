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
  # Create new variables (a, b, and c) which store the dimensions
  # width * height, height * length, and width * length
  a = w * h
  b = h * l
  c = w * l
  # Create a new variable (dim) and multiply each dimension by 2 and add them together
  # The instructions were helpful enough to explain that this is how we calculate the dimensions
  dim = (2 * a) + (2 * b) + (2 * c)
  # Create a list from the exiting variables a, b, and c
  # We do this so we can find the smallest one of the three, so we know how much extra
  # wrapping paper is needed.
  list = [a, b, c]
  # Create a new variable (extra) and use the min method to find the smallest one
  extra = min(list)
  # Add the dimensions and extra to get the total amount of wrapping paper for each line
  total = total + dim + extra

# Print the answer
print "The elves need to order %s feet of wrapping paper" % (total)
