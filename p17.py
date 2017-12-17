from common import run
from collections import deque

def p1():
    steps = 363
    data = deque([0])
    for x in xrange(1, 2018):
        data.rotate(-steps)
        data.append(x)
    l = list(data)
    index = l.index(2017) + 1
    if index >= len(l):
        index = 0

    print l[index]

    # Slow
    # steps = 363
    # data = [0]
    # position = 0
    # for x in xrange(1, 2018):
    #     tmp = steps
    #     position = (position + steps) % len(data)
    #     data.insert(position + 1, x)
    #     position += 1
    #     if position >= len(data):
    #         position = 0
    # index = data.index(2017)
    # print data[index + 1]

def p2():
    steps = 363
    data = deque([0])
    for x in xrange(1, 50000001):
        if x % 100000 == 0:
            print x
        data.rotate(-steps)
        data.append(x)
    l = list(data)
    index = l.index(0) + 1
    if index >= len(l):
        index = 0

    print l[index]

if __name__ == '__main__':
    run(p1, p2)