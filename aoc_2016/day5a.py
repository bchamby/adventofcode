import hashlib

input = 'reyedfim'

a = 0
b = 0
woot = ''

while a < 8:
    test = input + str(b)
    m = hashlib.md5()
    m.update(test)
    answer = str(m.hexdigest())

    if answer[0] == '0' and answer[1] == '0' and answer[2] == '0' and answer[3] == '0' and answer[4] == '0':
        woot += answer[5]
        a += 1

    b += 1

print woot
