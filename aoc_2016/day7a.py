import re
# import csv

file = open('/Users/chamby/Projects/adventofcode/aoc_2016/day7inputa.txt')

# file = 'lcototgbpkkoxhsg[erticxnxcjwypnunco]notoouvtmgqcfdupe[hubcmesmprktstzyae]unuquevgbpxqnrib[egalxegqwowylkdjkdg]spqmkzfjnzwcwgutl'

index = 0

valid = []
encl = []

# print delimiters

for line in file:

    # delimiters = "[", "]"
    # rexPattern = '|'.join(map(re.escape, delimiters))
    # rexPattern
    # re.split(rexPattern, line)

    # line.split('[')
    # print line
    # count = line.count('[')
    # print count
    start = '['
    end = ']'
    # print ((line.split(start))[1].split(end)[0])

    # string = line + 'hello'

    # print string

    # start = '['
    # end = ']'

    mysub = line[line.find(start)+len(start):line.find(end)]
    print mysub

    # result = re.match('%s(.*)%s' % (start,end), line).group(1)
    # print result

    # for i in csv.reader([line], delimiter='['):
        # print i
        # for j in csv.reader([i], delimiter=']'):
            # print j

    # result = re.search('%s(.*)%s' % (start, end), line)
    # print result.group(1)
    # print result

    # count1 = 0
    # count2 = 0
    #
    # result = ''
    # result2 = ''
    # result3 = ''
    # result4 = ''

    # result = re.findall(re.escape(start)+"(.*)"+re.escape(end),line)[0]
    #
    # print result
    #
    # for i in result:
    #     if i == '[':
    #         count1 += 1
    # print result
    # if count1 > 1:
    #     result2 = re.findall(re.escape(start)+"(.*)"+re.escape(end),result)[0]
        # result3 = re.findall(re.escape(start)+"(.*)"+re.escape(end),result)[1]

    # print result2
    # print result3

    # for j in result2:
    #     if j == '[':
    #         count2 += 1
    # print count2
    #
    # if count2 > 1:
    #     result3 = re.findall(re.escape(start)+"(.*)"+re.escape(end),result2)[0]
    #
    # print result3



    # print result2



    # print result
    # for i in result:
    #     print i.count('[')
    # print result.count('[')
    # if result.count('[') > 1:
        # result2 = re.findall(re.escape(start)+"(.*)"+re.escape(end),line)[0]
        # print result2
