from collections import Counter

file = open('day4input.txt')

input = []

count = 0

for i in file:
    input.append((i).replace('[', '-').replace(']', '').rstrip('\n'))

for j in input:
    checksum = j.split('-')[-1]
    secid = int(j.split('-')[-2])
    segments = len(j.split('-'))
    end = segments - 2
    roomname = ''
    for l in j.split('-')[0:end]:
        roomname += l

    answer = ''

    most_common = Counter(roomname).most_common(10)

    brad = sorted(most_common, key=lambda k: (-k[1], k[0]))


    answer += brad[0][0]
    answer += brad[1][0]
    answer += brad[2][0]
    answer += brad[3][0]
    answer += brad[4][0]

    if answer == checksum:
        count = count + secid
print count
