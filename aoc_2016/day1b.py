input = ['L1', 'L5', 'R1', 'R3', 'L4', 'L5', 'R5', 'R1', 'L2', 'L2', 'L3', 'R4', 'L2', 'R3', 'R1', 'L2', 'R5', 'R3', 'L4', 'R4', 'L3', 'R3', 'R3', 'L2', 'R1', 'L3', 'R2', 'L1', 'R4', 'L2', 'R4', 'L4', 'R5', 'L3', 'R1', 'R1', 'L1', 'L3', 'L2', 'R1', 'R3', 'R2', 'L1', 'R4', 'L4', 'R2', 'L189', 'L4', 'R5', 'R3', 'L1', 'R47', 'R4', 'R1', 'R3', 'L3', 'L3', 'L2', 'R70', 'L1', 'R4', 'R185', 'R5', 'L4', 'L5', 'R4', 'L1', 'L4', 'R5', 'L3', 'R2', 'R3', 'L5', 'L3', 'R5', 'L1', 'R5', 'L4', 'R1', 'R2', 'L2', 'L5', 'L2', 'R4', 'L3', 'R5', 'R1', 'L5', 'L4', 'L3', 'R4', 'L3', 'L4', 'L1', 'L5', 'L5', 'R5', 'L5', 'L2', 'L1', 'L2', 'L4', 'L1', 'L2', 'R3', 'R1', 'R1', 'L2', 'L5', 'R2', 'L3', 'L5', 'L4', 'L2', 'L1', 'L2', 'R3', 'L1', 'L4', 'R3', 'R3', 'L2', 'R5', 'L1', 'L3', 'L3', 'L3', 'L5', 'R5', 'R1', 'R2', 'L3', 'L2', 'R4', 'R1', 'R1', 'R3', 'R4', 'R3', 'L3', 'R3', 'L5', 'R2', 'L2', 'R4', 'R5', 'L4', 'L3', 'L1', 'L5', 'L1', 'R1', 'R2', 'L1', 'R3', 'R4', 'R5', 'R2', 'R3', 'L2', 'L1', 'L5']

coordinates = []
x = 0
y = 0
d = 'n'

coordinates.append((x,y))

# def left(num):
#     x -= num
# def right(num):
#     x += num
# def up(num):
#     y += num
# def down(num):
#     y -= num

for i in input:
    if i[0] == 'L':
        if d == 'n':
            # left(i[1])
            # x -= int(i[1:])
            moves = int(i[1:])
            while moves > 0:
                x -= 1
                moves -= 1
                coordinates.append((x,y))
            # j = abs(x) + abs(y)
            # coordinates.append(j)
            d = 'w'
        elif d == 'e':
            # up(i[1])
            # y += int(i[1:])
            moves = int(i[1:])
            while moves > 0:
                y += 1
                moves -= 1
                coordinates.append((x,y))
            # j = abs(x) + abs(y)
            # coordinates.append(j)
            d = 'n'
        elif d == 's':
            # left(i[1])
            # x += int(i[1:])
            moves = int(i[1:])
            while moves > 0:
                x += 1
                moves -= 1
                coordinates.append((x,y))
            # j = abs(x) + abs(y)
            # coordinates.append(j)
            d = 'e'
        elif d == 'w':
            # down(i[1])
            # y -= int(i[1:])
            moves = int(i[1:])
            while moves > 0:
                y -= 1
                moves -= 1
                coordinates.append((x,y))
            # j = abs(x) + abs(y)
            # coordinates.append(j)
            d = 's'
    elif i[0] == 'R':
        if d == 'n':
            # right(i[1])
            # x += int(i[1:])
            moves = int(i[1:])
            while moves > 0:
                x += 1
                moves -= 1
                coordinates.append((x,y))
            # j = abs(x) + abs(y)
            # coordinates.append(j)
            d = 'e'
        elif d == 'e':
            # down(i[1])
            # y -= int(i[1:])
            moves = int(i[1:])
            while moves > 0:
                y -= 1
                moves -= 1
                coordinates.append((x,y))
            # j = abs(x) + abs(y)
            # coordinates.append(j)
            d = 's'
        elif d == 's':
            # left(i[1])
            # x -= int(i[1:])
            moves = int(i[1:])
            while moves > 0:
                x -= 1
                moves -= 1
                coordinates.append((x,y))
            # j = abs(x) + abs(y)
            # coordinates.append(j)
            d = 'w'
        elif d == 'w':
            # up(i[1])
            # y += int(i[1:])
            moves = int(i[1:])
            while moves > 0:
                y += 1
                moves -= 1
                coordinates.append((x,y))
            # j = abs(x) + abs(y)
            # coordinates.append(j)
            d = 'n'

# print coordinates

i = 0

for k in coordinates:
    l = coordinates.pop(i)
    if l in coordinates:
        print l
        print l[0] + l[1]
        break
    # j = coordinates.pop(i)
    # print j
    # break

# answer = x + y

# print answer

# c = len(coordinates) - 1
#
# i = 0
#
# while i < c:
#     for j in coordinates:
#         k = coordinates.pop(i)
#         if k in coordinates:
#             print k
#             break

    # j = coordinates.pop(i)
    # if j in coordinates:
    #     print j
    # else:
    #     i += 1
