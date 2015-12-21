total = 0

file = open('day2input.txt', 'rU')
for line in file.readlines():
  w = line.split("x")[0]
  h = line.split("x")[1]
  l = line.split("x")[2]
  w = int(w)
  h = int(h)
  l = int(l)
  a = w * h
  b = h * l
  c = w * l
  # print "The width is %s, the height is %s, and the length is %s" % (w, h, l)
  dim = (2 * a) + (2 * b) + (2 * c)
  list = [a, b, c]
  extra = min(list)
  # print "The smallest of the dimensions is %s" % (extra)
  total = total + dim + extra

print "The elves need to order %s feet of wrapping paper" % (total)
