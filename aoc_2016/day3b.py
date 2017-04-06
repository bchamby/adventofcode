file = open('day3inputa.txt')

count = 0

col1 = []
col2 = []
col3 = []

input = []

for line in file:

    data = line.split()

    # col1.append(int(data[0]))
    # col2.append(int(data[1]))
    # col3.append(int(data[2]))

    input.append(int(data[0]))
    input.append(int(data[1]))
    input.append(int(data[2]))

# print int(input[1])

# for j in input:
#     if j[0]

# while True:
#     if int(j[i]) + int(j[i + 3]) > int(j[i + 6]):
#         if int(j[i + 3]) + int(j[i + 6]) > int(j[i]):
#             if int(j[i]) + int(j[i + 6]) > int(j[i + 3]):
#                 count += 1
#                 print count

# print input[6]
#

# print input[i]
# print input[i + 3]
# print input[i + 6]
# i += 1
# print input[i]
# print input[i + 3]
# print input[i + 6]
# i += 1
# print input[i]
# print input[i + 3]
# print input[i + 6]

# i = len(input)

i = 0

# print len(input)

# print i
# print input[i + int(-50)]

# print input[-4]

while True:
    if input[i] + input[i + 3] > input[i + 6]:
        if input[i + 3] + input[i + 6] > input[i]:
            if input[i] + input[i + 6] > input[i + 3]:
                count += 1
                print i
                print count
                i += 1
            i += 1
        i += 1
    i += 1
#
# while i > 0:
#     if int(input[i-1]) + int(input[i-4]) > int(input[i-7]):
#         if int(input[i-4]) + int(input[i-7]) > int(input[i-1]):
#             if int(input[i-1]) + int(input[i-7]) > int(input[i-4]):
#                 count += 1
#                 # print i
#                 print count
#                 i -= 1
#             # pass
#             i -= 1
#         # pass
#         i -= 1
#     # pass
#     i -= 1

# print input

# print count

#     i += 3
#
# print count

#
# for i in col1:
#     if i[0] + i[1] > i[2]:
#         if i[1] + i[2] > i[0]:
#             if i[0] + i[2]:
#                 count += 1
#
# for i in col2:
#     if i[0] + i[1] > i[2]:
#         if i[1] + i[2] > i[0]:
#             if i[0] + i[2]:
#                 count += 1
#
# for i in col3:
#     if i[0] + i[1] > i[2]:
#         if i[1] + i[2] > i[0]:
#             if i[0] + i[2]:
#                 count += 1
#
# print count
