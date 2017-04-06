from collections import Counter

file = open('day6input.txt')

message = ''

a = ''
b = ''
c = ''
d = ''
e = ''
f = ''
g = ''
h = ''


for line in file:
    a += line[0]
    b += line[1]
    c += line[2]
    d += line[3]
    e += line[4]
    f += line[5]
    g += line[6]
    h += line[7]

commona = Counter(a).most_common(1)
commonb = Counter(b).most_common(1)
commonc = Counter(c).most_common(1)
commond = Counter(d).most_common(1)
commone = Counter(e).most_common(1)
commonf = Counter(f).most_common(1)
commong = Counter(g).most_common(1)
commonh = Counter(h).most_common(1)

print commona[0][0] + commonb[0][0] + commonc[0][0] + commond[0][0] + commone[0][0] + commonf[0][0] + commong[0][0] + commonh[0][0]
# print commona[0][0]
# print sorted(commona)[0]
