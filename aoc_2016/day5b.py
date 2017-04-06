import hashlib

input = 'reyedfim'

a = 0
b = 0
valid = ['0','1','2','3','4','5','6','7']
woot = {}
finwoot = ''

while a < 8:
    test = input + str(b)
    m = hashlib.md5()
    m.update(test)
    answer = str(m.hexdigest())

    if answer[0] == '0' and answer[1] == '0' and answer[2] == '0' and answer[3] == '0' and answer[4] == '0' and answer[5] in valid:
        k = answer[5]
        v = answer[6]
        woot[k] = v
        valid.remove(k)
        a += 1

    b += 1

finwoot = woot['0'] + woot['1'] + woot['2'] + woot['3'] + woot['4'] + woot['5'] + woot['6'] + woot['7']

print woot
print finwoot
