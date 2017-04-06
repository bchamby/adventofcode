file = open('day3input.txt')

count = 0

for i in file:
    if int(i.split( )[0]) + int(i.split( )[1]) > int(i.split( )[2]):
        if int(i.split( )[1]) + int(i.split( )[2]) > int(i.split( )[0]):
            if int(i.split( )[0]) + int(i.split( )[2]) > int(i.split( )[1]):
                count += 1
print count
