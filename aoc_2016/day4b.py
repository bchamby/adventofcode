from collections import Counter

file = open('day4input.txt')

input = []
answer = ''
strs = 'abcdefghijklmnopqrstuvwxyz'

count = 0

for i in file:
    input.append((i).replace('[', '-').replace(']', '').rstrip('\n'))

for j in input:
    checksum = j.split('-')[-1]
    secid = int(j.split('-')[-2])
    segments = len(j.split('-'))
    end = segments - 2
    roomname = []
    for l in j.split('-')[0:end]:
        roomname += l
    # print roomname
    #
    for i in roomname:
        # print i
        # print i
        # answer = ''
        if i in strs:
            # answer.append(strs[(strs.index(i) + secid) % 26])
            # answer += (strs[(strs.index(i) + secid) % 26])
            answer += (strs[(strs.index(i) + secid) % 26])
        else:
            # answer.append(' ')
            answer += ' '
        #
        # print answer
        #
        # # if answer == 'northpoleobjectstorage':
        # if answer == 'tttttuuusrq':
        #     print secid
        # else:
        #     answer = ''
    # print answer

    if answer == 'northpoleobjectstorage':
        print secid
        break
    else:
        answer = ''

# print answer
