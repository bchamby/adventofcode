code1 = 'RLRLLLULULULUUDUULULRDDLURURDDLDUUDDLRDDUUUDDRUDLRRDDUDUUDULUDRDULRUDRULRDRUDLDDULRRDLDRLUDDLLDRDDDUDDLUDUDULDRLLDRLULRLURDLULRUUUDRULLUUDLRDLDDUDRRRLDLRUUURRLDDRRRURLLULDUULLDRLRDLLDURDLDDULLDDLDLUURRRURLRURLLRRDURLDUDDLULUUULULLLDRRRRRLULRDUDURURLULRURRRLLUURDURULRRUULDRDLULDLLUDLUDRLUDLRRLDLLDLDUDDLULLDRULRLRULDURRDLDLLUDRLLDRRDLDUDUURUURDUUDDDLDLDDRDLUDLDUUUUDLDRLRURDLURURDLLLUURURDRDLUDLLRUDULLLDLULLULLDLDDRDRRRUDDDUDDDDRULLLLRLDDLLRDRLLLRRLDRRUDRUUURLLLRULRRDURDLDRLDDUUDUUURRLRRUDLDLDDRUDLULLUUDUUUDLUDDRUULLLURUDDDDLRUDDLLLRUR'
code2 = 'LDLRLDDDLUDRDRRUDUURLRULLUDDRLURLUULDLLRLLUDLRLRUDLULRLRRLRURLDDDURUDUUURDRLDDLUUUDRUDUDDDLLURLLULRUULLUDRULUDDULDUDUDULLDRUUUULRDUUDLUDURDLLRLLRLUUDUUDRLLLRULUURUDLDRLLDUDLDDRULDULDURRLDDDUDUDDRUDUDRDURLLLLLULDRDDLLUDULLLUDRURLDLDLDULLDDRURRLUDDRLURLULRLDDDUUUURLRDLRURDDURLDLRRLLRLRLUURRLLDDLDRLRDUDDLLDDDURUUDURLRRDUULRRDDRRUULDRLRUDRRLDDRLDRULLDLDURRULDURRRDLRRLRLLLRLDRLLULRRLLLLLDLDDULDLLDLLDUUDDRLURUUUUULRDDLRDLRDRDRDLUDDLDDRULLUDDRLDLLUDRLUURRLUDURURLLRURRURRLRLLRLURURDDDDRRLURDUULLUU'
code3 = 'LLRRDURRDLDULRDUDLRDRDRURULDURUDRRURDDDRLDLDRDRDRDRULDUURLULDDUURUULUDULLDUDLLLLDLLLDRLUUULLULDDRRUDDULLLULRDRULDDULDUDRDDLUUURULDLLUDUUUUURUDLLDRDULLRULLDURDRLLDLDRDDURUULUDURRRUULLDUUDDURDURLDLRRLLDURDDLRRRUDLRRRDLDRLUDLUDRDRLDDLLLRLLRURDLRDUUUURRLULDDLDLLLUDRDRLRRDURDDLURDLDDDULLLRRLDDDRULDDDLRRDULUUUDRRULDDLLLURDRRLLLUULDRRRUURRDDLULDRLULDDDLDULDRRRULRULLURLURULLLLRUDRRRDRDRDLDULURLRRRRLRUDDRRRUURUURLLRURURUURRURRDLDLLUDRRRDUDDRDURLLRLRRULD'
code4 = 'DULRRDRLRLUDLLURURLLRLRDLLDLLDRDUURLRUUUDLLDUUDDUULDUULLRUDRURLUDRDLRUDDDLULUDLLDRULULLLDRRULDLLUURLRRRLDRDLDRURRRRDLRUUDULLRLLLDLRUDLDUUDRLDLRDRLRDLDDDUDLRUDLDDLLLDRLLRRUUDRDDUUURURRRUUDLRRDDRUDLDDULULDLRRLRDDUDRUURRUULURLURUDRRURRRULDDDDURDLUUULUULULRDLRRRRRURURRLRUULDUUURRDRRDLDUUUULLULLLLUDLUUDUURRDLDLRRRLUUURULDULDLDRLLURDRUULLLLLULLLDRURURRUDRRRRUDUDUDRUDUDRDRULUUDRURDDUUDLDLDUURUDURLRLRRDRDRDLLDUDDULLRDLDDRLLDLRDURDDULLLDLLLULDLUUUDLDRDLURUURDDLRDLLLLLRLURDLLLULLRRLU'
code5 = 'DUULULUUDUDLLRLRURULLDLRRLURDLLDUDUDDRURRLUDULULDRRDRLUULUDDLUURURDLDDDRDRUDURLDDLUDUURULRRUUDRLURRLRLDURRRULRLDDDRUDDDDDUDDULLLRRLLDULDRULUDLRRDLLUDRDLDULRLLLUULLRULRLLLLUDDRRDRLULDLDLURDDRUDDLDLDLDRULDLLDDUUDULUULULLURDURRLLUDRULLRDUDRDRURDRDRDURUUDULDDRURUDLLUUDUUDURDLRDRURUDRUURLUUURLRLUDRUDRUURLLUDRLURDDURRUDRDRLRRLDDDRDDLUUUDDLULDUURUDUDLLDRURDURRDULRLURRDLDDRLUDRLDLRLDDUURRULDDLDUDDLRDULLDDDLDUUUUDLRUDUDLDRDLRDDLDLRLLUDDRRLUDLDUUULLDDRLRRDLRRRRUDDLRLLULRLRDURDUDDRRULLDDLDLRRDLLULDURURDDURLRLULULURRUDUDRDLURULDUDLUULDUUURLLRUDLLRDLRUDRLULDUDRRDUUDUUULUUUDDRUD'

pos = 'ww'

for i in code1:
    if i == 'R':
        if pos == 'nw':
            pos = 'n'
        elif pos == 'n':
            pos = 'ne'
        elif pos == 'ne':
            pos = 'ne'
        elif pos == 'w':
            pos = 'm'
        elif pos == 'm':
            pos = 'e'
        elif pos == 'e':
            pos = 'ee'
        elif pos == 'sw':
            pos = 's'
        elif pos == 's':
            pos = 'se'
        elif pos == 'se':
            pos = 'se'

        elif pos == 'nn':
            pos = 'nn'
        elif pos == 'ee':
            pos = 'ee'
        elif pos == 'ww':
            pos = 'w'
        elif pos == 'ss':
            pos = 'ss'

    elif i == 'L':
        if pos == 'nw':
            pos = 'nw'
        elif pos == 'n':
            pos = 'nw'
        elif pos == 'ne':
            pos = 'n'
        elif pos == 'w':
            pos = 'ww'
        elif pos == 'm':
            pos = 'w'
        elif pos == 'e':
            pos = 'm'
        elif pos == 'sw':
            pos = 'sw'
        elif pos == 's':
            pos = 'sw'
        elif pos == 'se':
            pos = 's'

        elif pos == 'nn':
            pos = 'nn'
        elif pos == 'ee':
            pos = 'e'
        elif pos == 'ww':
            pos = 'ww'
        elif pos == 'ss':
            pos = 'ss'

    elif i == 'U':
        if pos == 'nw':
            pos = 'nw'
        elif pos == 'n':
            pos = 'nn'
        elif pos == 'ne':
            pos = 'ne'
        elif pos == 'w':
            pos = 'nw'
        elif pos == 'm':
            pos = 'n'
        elif pos == 'e':
            pos = 'ne'
        elif pos == 'sw':
            pos = 'w'
        elif pos == 's':
            pos = 'm'
        elif pos == 'se':
            pos = 'e'

        elif pos == 'nn':
            pos = 'nn'
        elif pos == 'ee':
            pos = 'ee'
        elif pos == 'ww':
            pos = 'ww'
        elif pos == 'ss':
            pos = 's'

    elif i == 'D':
        if pos == 'nw':
            pos = 'w'
        elif pos == 'n':
            pos = 'm'
        elif pos == 'ne':
            pos = 'e'
        elif pos == 'w':
            pos = 'sw'
        elif pos == 'm':
            pos = 's'
        elif pos == 'e':
            pos = 'se'
        elif pos == 'sw':
            pos = 'sw'
        elif pos == 's':
            pos = 'ss'
        elif pos == 'se':
            pos = 'se'

        elif pos == 'nn':
            pos = 'n'
        elif pos == 'ee':
            pos = 'ee'
        elif pos == 'ww':
            pos = 'ww'
        elif pos == 'ss':
            pos = 'ss'

pos1 = pos

for i in code2:
    if i == 'R':
        if pos == 'nw':
            pos = 'n'
        elif pos == 'n':
            pos = 'ne'
        elif pos == 'ne':
            pos = 'ne'
        elif pos == 'w':
            pos = 'm'
        elif pos == 'm':
            pos = 'e'
        elif pos == 'e':
            pos = 'ee'
        elif pos == 'sw':
            pos = 's'
        elif pos == 's':
            pos = 'se'
        elif pos == 'se':
            pos = 'se'

        elif pos == 'nn':
            pos = 'nn'
        elif pos == 'ee':
            pos = 'ee'
        elif pos == 'ww':
            pos = 'w'
        elif pos == 'ss':
            pos = 'ss'

    elif i == 'L':
        if pos == 'nw':
            pos = 'nw'
        elif pos == 'n':
            pos = 'nw'
        elif pos == 'ne':
            pos = 'n'
        elif pos == 'w':
            pos = 'ww'
        elif pos == 'm':
            pos = 'w'
        elif pos == 'e':
            pos = 'm'
        elif pos == 'sw':
            pos = 'sw'
        elif pos == 's':
            pos = 'sw'
        elif pos == 'se':
            pos = 's'

        elif pos == 'nn':
            pos = 'nn'
        elif pos == 'ee':
            pos = 'e'
        elif pos == 'ww':
            pos = 'ww'
        elif pos == 'ss':
            pos = 'ss'

    elif i == 'U':
        if pos == 'nw':
            pos = 'nw'
        elif pos == 'n':
            pos = 'nn'
        elif pos == 'ne':
            pos = 'ne'
        elif pos == 'w':
            pos = 'nw'
        elif pos == 'm':
            pos = 'n'
        elif pos == 'e':
            pos = 'ne'
        elif pos == 'sw':
            pos = 'w'
        elif pos == 's':
            pos = 'm'
        elif pos == 'se':
            pos = 'e'

        elif pos == 'nn':
            pos = 'nn'
        elif pos == 'ee':
            pos = 'ee'
        elif pos == 'ww':
            pos = 'ww'
        elif pos == 'ss':
            pos = 's'

    elif i == 'D':
        if pos == 'nw':
            pos = 'w'
        elif pos == 'n':
            pos = 'm'
        elif pos == 'ne':
            pos = 'e'
        elif pos == 'w':
            pos = 'sw'
        elif pos == 'm':
            pos = 's'
        elif pos == 'e':
            pos = 'se'
        elif pos == 'sw':
            pos = 'sw'
        elif pos == 's':
            pos = 's'
        elif pos == 'se':
            pos = 'se'

        elif pos == 'nn':
            pos = 'n'
        elif pos == 'ee':
            pos = 'ee'
        elif pos == 'ww':
            pos = 'ww'
        elif pos == 'ss':
            pos = 'ss'

pos2 = pos

for i in code3:
    if i == 'R':
        if pos == 'nw':
            pos = 'n'
        elif pos == 'n':
            pos = 'ne'
        elif pos == 'ne':
            pos = 'ne'
        elif pos == 'w':
            pos = 'm'
        elif pos == 'm':
            pos = 'e'
        elif pos == 'e':
            pos = 'ee'
        elif pos == 'sw':
            pos = 's'
        elif pos == 's':
            pos = 'se'
        elif pos == 'se':
            pos = 'se'

        elif pos == 'nn':
            pos = 'nn'
        elif pos == 'ee':
            pos = 'ee'
        elif pos == 'ww':
            pos = 'w'
        elif pos == 'ss':
            pos = 'ss'

    elif i == 'L':
        if pos == 'nw':
            pos = 'nw'
        elif pos == 'n':
            pos = 'nw'
        elif pos == 'ne':
            pos = 'n'
        elif pos == 'w':
            pos = 'ww'
        elif pos == 'm':
            pos = 'w'
        elif pos == 'e':
            pos = 'm'
        elif pos == 'sw':
            pos = 'sw'
        elif pos == 's':
            pos = 'sw'
        elif pos == 'se':
            pos = 's'

        elif pos == 'nn':
            pos = 'nn'
        elif pos == 'ee':
            pos = 'e'
        elif pos == 'ww':
            pos = 'ww'
        elif pos == 'ss':
            pos = 'ss'

    elif i == 'U':
        if pos == 'nw':
            pos = 'nw'
        elif pos == 'n':
            pos = 'nn'
        elif pos == 'ne':
            pos = 'ne'
        elif pos == 'w':
            pos = 'nw'
        elif pos == 'm':
            pos = 'n'
        elif pos == 'e':
            pos = 'ne'
        elif pos == 'sw':
            pos = 'w'
        elif pos == 's':
            pos = 'm'
        elif pos == 'se':
            pos = 'e'

        elif pos == 'nn':
            pos = 'nn'
        elif pos == 'ee':
            pos = 'ee'
        elif pos == 'ww':
            pos = 'ww'
        elif pos == 'ss':
            pos = 's'

    elif i == 'D':
        if pos == 'nw':
            pos = 'w'
        elif pos == 'n':
            pos = 'm'
        elif pos == 'ne':
            pos = 'e'
        elif pos == 'w':
            pos = 'sw'
        elif pos == 'm':
            pos = 's'
        elif pos == 'e':
            pos = 'se'
        elif pos == 'sw':
            pos = 'sw'
        elif pos == 's':
            pos = 's'
        elif pos == 'se':
            pos = 'se'

        elif pos == 'nn':
            pos = 'n'
        elif pos == 'ee':
            pos = 'ee'
        elif pos == 'ww':
            pos = 'ww'
        elif pos == 'ss':
            pos = 'ss'
pos3 = pos

for i in code4:
    if i == 'R':
        if pos == 'nw':
            pos = 'n'
        elif pos == 'n':
            pos = 'ne'
        elif pos == 'ne':
            pos = 'ne'
        elif pos == 'w':
            pos = 'm'
        elif pos == 'm':
            pos = 'e'
        elif pos == 'e':
            pos = 'ee'
        elif pos == 'sw':
            pos = 's'
        elif pos == 's':
            pos = 'se'
        elif pos == 'se':
            pos = 'se'

        elif pos == 'nn':
            pos = 'nn'
        elif pos == 'ee':
            pos = 'ee'
        elif pos == 'ww':
            pos = 'w'
        elif pos == 'ss':
            pos = 'ss'

    elif i == 'L':
        if pos == 'nw':
            pos = 'nw'
        elif pos == 'n':
            pos = 'nw'
        elif pos == 'ne':
            pos = 'n'
        elif pos == 'w':
            pos = 'ww'
        elif pos == 'm':
            pos = 'w'
        elif pos == 'e':
            pos = 'm'
        elif pos == 'sw':
            pos = 'sw'
        elif pos == 's':
            pos = 'sw'
        elif pos == 'se':
            pos = 's'

        elif pos == 'nn':
            pos = 'nn'
        elif pos == 'ee':
            pos = 'e'
        elif pos == 'ww':
            pos = 'ww'
        elif pos == 'ss':
            pos = 'ss'

    elif i == 'U':
        if pos == 'nw':
            pos = 'nw'
        elif pos == 'n':
            pos = 'nn'
        elif pos == 'ne':
            pos = 'ne'
        elif pos == 'w':
            pos = 'nw'
        elif pos == 'm':
            pos = 'n'
        elif pos == 'e':
            pos = 'ne'
        elif pos == 'sw':
            pos = 'w'
        elif pos == 's':
            pos = 'm'
        elif pos == 'se':
            pos = 'e'

        elif pos == 'nn':
            pos = 'nn'
        elif pos == 'ee':
            pos = 'ee'
        elif pos == 'ww':
            pos = 'ww'
        elif pos == 'ss':
            pos = 's'

    elif i == 'D':
        if pos == 'nw':
            pos = 'w'
        elif pos == 'n':
            pos = 'm'
        elif pos == 'ne':
            pos = 'e'
        elif pos == 'w':
            pos = 'sw'
        elif pos == 'm':
            pos = 's'
        elif pos == 'e':
            pos = 'se'
        elif pos == 'sw':
            pos = 'sw'
        elif pos == 's':
            pos = 's'
        elif pos == 'se':
            pos = 'se'

        elif pos == 'nn':
            pos = 'n'
        elif pos == 'ee':
            pos = 'ee'
        elif pos == 'ww':
            pos = 'ww'
        elif pos == 'ss':
            pos = 'ss'

pos4 = pos

for i in code5:
    if i == 'R':
        if pos == 'nw':
            pos = 'n'
        elif pos == 'n':
            pos = 'ne'
        elif pos == 'ne':
            pos = 'ne'
        elif pos == 'w':
            pos = 'm'
        elif pos == 'm':
            pos = 'e'
        elif pos == 'e':
            pos = 'ee'
        elif pos == 'sw':
            pos = 's'
        elif pos == 's':
            pos = 'se'
        elif pos == 'se':
            pos = 'se'

        elif pos == 'nn':
            pos = 'nn'
        elif pos == 'ee':
            pos = 'ee'
        elif pos == 'ww':
            pos = 'w'
        elif pos == 'ss':
            pos = 'ss'

    elif i == 'L':
        if pos == 'nw':
            pos = 'nw'
        elif pos == 'n':
            pos = 'nw'
        elif pos == 'ne':
            pos = 'n'
        elif pos == 'w':
            pos = 'ww'
        elif pos == 'm':
            pos = 'w'
        elif pos == 'e':
            pos = 'm'
        elif pos == 'sw':
            pos = 'sw'
        elif pos == 's':
            pos = 'sw'
        elif pos == 'se':
            pos = 's'

        elif pos == 'nn':
            pos = 'nn'
        elif pos == 'ee':
            pos = 'e'
        elif pos == 'ww':
            pos = 'ww'
        elif pos == 'ss':
            pos = 'ss'

    elif i == 'U':
        if pos == 'nw':
            pos = 'nw'
        elif pos == 'n':
            pos = 'nn'
        elif pos == 'ne':
            pos = 'ne'
        elif pos == 'w':
            pos = 'nw'
        elif pos == 'm':
            pos = 'n'
        elif pos == 'e':
            pos = 'ne'
        elif pos == 'sw':
            pos = 'w'
        elif pos == 's':
            pos = 'm'
        elif pos == 'se':
            pos = 'e'

        elif pos == 'nn':
            pos = 'nn'
        elif pos == 'ee':
            pos = 'ee'
        elif pos == 'ww':
            pos = 'ww'
        elif pos == 'ss':
            pos = 's'

    elif i == 'D':
        if pos == 'nw':
            pos = 'w'
        elif pos == 'n':
            pos = 'm'
        elif pos == 'ne':
            pos = 'e'
        elif pos == 'w':
            pos = 'sw'
        elif pos == 'm':
            pos = 's'
        elif pos == 'e':
            pos = 'se'
        elif pos == 'sw':
            pos = 'sw'
        elif pos == 's':
            pos = 's'
        elif pos == 'se':
            pos = 'se'

        elif pos == 'nn':
            pos = 'n'
        elif pos == 'ee':
            pos = 'ee'
        elif pos == 'ww':
            pos = 'ww'
        elif pos == 'ss':
            pos = 'ss'
pos5 = pos

print pos1
print pos2
print pos3
print pos4
print pos5
