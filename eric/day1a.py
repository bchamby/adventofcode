input = 'L5, R1, R3, L4, R3, R1, L3, L2, R3, L5, L1, L2, R5, L1, R5, R1, L4, R1, R3, L4, L1, R2, R5, R3, R1, R1, L1, R1, L1, L2, L1, R2, L5, L188, L4, R1, R4, L3, R47, R1, L1, R77, R5, L2, R1, L2, R4, L5, L1, R3, R187, L4, L3, L3, R2, L3, L5, L4, L4, R1, R5, L4, L3, L3, L3, L2, L5, R1, L2, R5, L3, L4, R4, L5, R3, R4, L2, L1, L4, R1, L3, R1, R3, L2, R1, R4, R5, L3, R5, R3, L3, R4, L2, L5, L1, L1, R3, R1, L4, R3, R3, L2, R5, R4, R1, R3, L4, R3, R3, L2, L4, L5, R1, L4, L5, R4, L2, L1, L3, L3, L5, R3, L4, L3, R5, R4, R2, L4, R2, R3, L3, R4, L1, L3, R2, R1, R5, L4, L5, L5, R4, L5, L2, L4, R4, R4, R1, L3, L2, L4, R3'

# input = 'L5, R1, R3, L4, R3, R1, L3'
pos = 'N'
x = 0
y = 0

list = input.split(',')

for i in list:
    dir = i.strip()[0]
    moves = int(i.strip()[1:])

    if pos == 'N':
        if dir == 'L':
            pos = 'W'
            x = x - moves
        elif dir == 'R':
            pos = 'E'
            x = x + moves
    elif pos == 'E':
        if dir == 'L':
            pos = 'N'
            y = y + moves
        elif dir == 'R':
            pos = 'S'
            y = y - moves
    elif pos == 'S':
        if dir == 'L':
            pos = 'E'
            x = x + moves
        elif dir == 'R':
            pos = 'W'
            x = x - moves
    elif pos == 'W':
        if dir == 'L':
            pos = 'S'
            y = y - moves
        elif dir == 'R':
            pos = 'N'
            y = y + moves

answer = abs(x) + abs(y)

print "The answer is %s" % (answer)
