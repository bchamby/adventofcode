total = 0

file = open('day2input.txt', 'rU')
for line in file.readlines():
  w = line.split("x")[0]
  h = line.split("x")[1]
  l = line.split("x")[2]
  w = int(w)
  h = int(h)
  l = int(l)
  list = [w, h, l]
  list2 = sorted(list, key=int)
  fir = list2[0]
  sec = list2[1]
  total = total + (fir + fir + sec + sec) + (w * h * l)

print "The elves should order %s feet of ribbon" % (total)
