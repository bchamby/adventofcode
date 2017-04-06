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

commona = Counter(a).most_common()
commonb = Counter(b).most_common()
commonc = Counter(c).most_common()
commond = Counter(d).most_common()
commone = Counter(e).most_common()
commonf = Counter(f).most_common()
commong = Counter(g).most_common()
commonh = Counter(h).most_common()

print commona[-1][0] + commonb[-1][0] + commonc[-1][0] + commond[-1][0] + commone[-1][0] + commonf[-1][0] + commong[-1][0] + commonh[-1][0]
# print commona[0][0]
# print sorted(commona)[0]
