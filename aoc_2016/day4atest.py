from collections import Counter
from operator import itemgetter, attrgetter, methodcaller

file = open('day4inputb.txt')

input = []

valid = []

count = 0

# for i in file:
#     input.append(i)
#
# print input

for i in file:
    input.append((i).replace('[', '-').replace(']', '').rstrip('\n'))

# print input
#
for j in input:
    # print j
    checksum = j.split('-')[-1]
    # print checksum
    secid = int(j.split('-')[-2])
    # print secid
    segments = len(j.split('-'))
    # print segments
    end = segments - 2
    # print end
    roomname = ''
    for l in j.split('-')[0:end]:
        roomname += l
    # roomname += j.split('-')[0:end]
    # print roomname

    answer = ''
    tie1 = []
    tie2 = []
    tie3 = []
    tie4 = []
    tie5 = []

    most_common = Counter(roomname).most_common(5)


    brad = sorted(most_common, key=itemgetter(0,1))
    # brad2 = brad.reverse()

    # print brad

    answer += brad[0][0]
    answer += brad[1][0]
    answer += brad[2][0]
    answer += brad[3][0]
    answer += brad[4][0]

    if answer == checksum:
        count = count += secid

print count

    # print answer

    # answer += brad[4]
    # answer += brad[3]
    # answer += brad[2]
    # answer += brad[1]
    # answer += brad[0]
    #
    # print answer


    # print most_common
    # if most_common[0][1] > most_common[1][1]:
    #     answer += most_common[0][0]
    # else:
    #     if most_common[1][1] > most_common[2][1]:
    #         tie1 += most_common[0][0]
    #         tie1 += most_common[1][0]
    #         answer += sorted(tie1)[0]
    #         answer += sorted(tie1)[1]

    # if most_common[0][1] == most_common[1][1] and most_common[1][1] == most_common[2][1] and most

    # if most_common[0][1] > most_common[1][1]:
    #     answer += most_common[0][0]
    # elif most_common[0][1] == most_common[1][1]:
    #     if most_common[1][1] > most_common[2][1]:
    #         tie1 += most_common[0][0]
    #         tie1 += most_common[1][0]
    #         answer += sorted(tie1)[0]
    #         answer += sorted(tie1)[1]
    #     elif most_common[1][1] == most_common[2][1]:
    #         if most_common[2][1] > most_common[3][1]:
    #             tie1 += most_common[0][0]
    #             tie1 += most_common[1][0]
    #             tie1 += most_common[2][0]
    #             answer += sorted(tie1)[0]
    #             answer += sorted(tie1)[1]
    #             answer += sorted(tie1)[2]
    #         elif most_common[2][1] == most_common[3][1]:
    #             if most_common[3][1] > most_common[4][1]:
    #                 tie1 += most_common[0][0]
    #                 tie1 += most_common[1][0]
    #                 tie1 += most_common[2][0]
    #                 tie1 += most_common[3][0]
    #                 answer += sorted(tie1)[0]
    #                 answer += sorted(tie1)[1]
    #                 answer += sorted(tie1)[2]
    #                 answer += sorted(tie1)[3]
    #                 answer += most_common[4][0]
    #             elif most_common[3][1] == most_common[4][1]:
    #                 tie1 += most_common[0][0]
    #                 tie1 += most_common[1][0]
    #                 tie1 += most_common[2][0]
    #                 tie1 += most_common[3][0]
    #                 tie1 += most_common[4][0]
    #                 answer += sorted(tie1)[0]
    #                 answer += sorted(tie1)[1]
    #                 answer += sorted(tie1)[2]
    #                 answer += sorted(tie1)[3]
    #                 answer += sorted(tie1)[4]
    #                 if answer == checksum:
    #                     valid.append(secid)
    #                 continue
    #
    # if most_common[0+1][1] > most_common[1+1][1]:
    #     answer += most_common[0+1][0]
    # elif most_common[0+1][1] == most_common[1+1][1]:
    #     if most_common[1+1][1] > most_common[2+1][1]:
    #         tie2 += most_common[0+1][0]
    #         tie2 += most_common[1+1][0]
    #         answer += sorted(tie2)[0]
    #         answer += sorted(tie2)[1]
    #     elif most_common[1+1][1] == most_common[2+1][1]:
    #         if most_common[2+1][1] > most_common[3+1][1]:
    #             tie2 += most_common[0+1][0]
    #             tie2 += most_common[1+1][0]
    #             tie2 += most_common[2+1][0]
    #             answer += sorted(tie2)[0]
    #             answer += sorted(tie2)[1]
    #             answer += sorted(tie2)[2]
    #         elif most_common[2+1][1] == most_common[3+1][1]:
    #             tie2 += most_common[0][0]
    #             tie2 += most_common[1][0]
    #             tie2 += most_common[2][0]
    #             tie2 += most_common[3][0]
    #             answer += sorted(tie2)[0]
    #             answer += sorted(tie2)[1]
    #             answer += sorted(tie2)[2]
    #             answer += sorted(tie2)[3]
    #             if answer == checksum:
    #                 valid.append(secid)
    #             continue
    #
    # if most_common[0+2][1] > most_common[1+2][1]:
    #     answer += most_common[0+2][0]
    # elif most_common[0+2][1] == most_common[1+2][1]:
    #     if most_common[1+2][1] > most_common[2+2][1]:
    #         tie3 += most_common[0+2][0]
    #         tie3 += most_common[1+2][0]
    #         answer += sorted(tie3)[0]
    #         answer += sorted(tie3)[1]
    #     elif most_common[1+2][1] == most_common[2+2][1]:
    #         # if most_common[2+2][1] > most_common[3+2][1]:
    #         tie3 += most_common[0+2][0]
    #         tie3 += most_common[1+2][0]
    #         tie3 += most_common[2+2][0]
    #         answer += sorted(tie3)[0]
    #         answer += sorted(tie3)[1]
    #         answer += sorted(tie3)[2]
    #         if answer == checksum:
    #             valid.append(secid)
    #             continue
    #
    # if most_common[0+3][1] > most_common[1+3][1]:
    #     answer += most_common[0+3][0]
    #     # answer += most_common[0+4][0]
    # elif most_common[0+3][1] == most_common[1+3][1]:
    #     tie4 += most_common[0+3][0]
    #     tie4 += most_common[1+3][0]
    #     answer += sorted(tie4)[0]
    #     answer += sorted(tie4)[1]
    #     if answer == checksum:
    #         valid.append(secid)
    #         continue

# print sum(valid)
# print valid

    # if most_common[1][1] > most_common[2][1]:
    #     answer += most_common[1][0]
    # elif most_common[1][1] == most_common[2][1]:
    #     if most_common[2][1] > most_common[3][1]:
    #         tie2 += most_common[1][0]
    #         tie2 += most_common[2][0]
    #         answer += sorted(tie2)[0]
    #         answer += sorted(tie2)[1]
    #     elif most_common[2][1] == most_common[3][1]:
    #         if most_common[3][1] > most_common[4][1]:
    #             tie2 += most_common[1][0]
    #             tie2 += most_common[2][0]
    #             tie2 += most_common[3][0]
    #             answer += sorted(tie2)[0]
    #             answer += sorted(tie2)[1]
    #             answer += sorted(tie2)[3]
    #         elif most_common[3][1] == most_common[4][1]:
    #             tie2 += most_common[1][0]
    #             tie2 += most_common[2][0]
    #             tie2 += most_common[3][0]
    #             tie2 += most_common[4][0]
    #             answer += sorted(tie2)[0]
    #             answer += sorted(tie2)[1]
    #             answer += sorted(tie2)[2]
    #             answer += sorted(tie2)[3]
    #
    # if most_common[2][1] > most_common[3][1]:
    #     answer += most_common[2][0]
    # elif most_common[2][1] == most_common[3][1]:
    #     if most_common[3][1] > most_common[4][1]:
    #         tie3 += most_common[2][0]
    #         tie3 += most_common[3][0]
    #         answer += sorted(tie3)[0]
    #         answer += sorted(tie3)[1]
    #     elif most_common[3][1] == most_common[4][1]:
    #         tie3 += most_common[3][0]
    #         tie3 += most_common[4][0]
    #         answer += sorted(tie3)[0]
    #         answer += sorted(tie3)[1]
    #
    # if most_common[3][1] > most_common[4][1]:
    #     answer += most_common[3][0]
    # elif most_common[3][1] == most_common[4][1]:
    #     tie4 += most_common[3][0]
    #     tie4 += most_common[4][0]
    #     answer += sorted(tie4)[0]
    #     answer += sorted(tie4)[1]

# print answer

    # if answer == checksum:
    #     count = count + secid
        # valid.append(secid)
        # print 'VALID!!!'

# print count

    # if most_common[0][0] > most_common[0][1]:
    #     answer += most_common[0][0]
    # elif most_common[0][0] == most_common[0][1]:
    #     tie1 += most_common[0][0]
    #     tie1 += most_common[0][1]
    # answer += tie1.sort()[0]
    #
    # if most_common[1][0] > most_common[1][1]:
    #     answer += most_common[1][0]
    # elif most_common[1][0] == most_common[1][1]:
    #     tie2 += most_common[1][0]
    #     tie2 += most_common[1][1]
    # answer += tie2.sort()[0]
    #
    # if most_common[2][0] > most_common[2][1]:
    #     answer += most_common[0][2]
    # elif most_common[0][2] == most_common[0][3]:
    #     tie2 += most_common[0][2]
    #     tie2 += most_common[0][3]
    # answer += tie2.sort()[0]

    #
    #
    # for letter in most_common:
    #     if letter[0] > letter[1]:
    #         # answer += letter[0]
    #         print letter[0]
    #     elif letter[0] == letter[1]:
    #         tie += letter[0]
    #         tie += letter[1]



#
#     list = []
#
#     for k in roomname:
#         if k.isalpha():
#             list.append(k)
#     print list
    #
    # most_common = Counter(list).most_common(5)
    # print most_common
    # for l in most_common:
    #     # string = str(l[0]) + str(l[1]) + str(l[2]) + str(l[3]) + str(l[4])
    #     string = l
    #     print string
    #     # print l[0] + l[1] + l[2] + l[3] + l[4]
