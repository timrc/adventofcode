from math import ceil

def p1():
    # data = [0,2,7,0]
    data = [4,10,4,1,8,4,9,14,5,1,14,15,0,15,3,5]
    permutations = []
    steps = 0
    l = len(data)
    while True:
        steps += 1
        value = max(data)
        index = data.index(value)
        data[index] = 0
        while value > 0:
            index += 1
            if index == l:
                index = 0
            data[index] += 1
            value -= 1
        t = tuple(data)
        if t in permutations:

            break
        permutations.append(t)
    print steps


def p2():
    # data = [0,2,7,0]
    data = [4,10,4,1,8,4,9,14,5,1,14,15,0,15,3,5]
    permutations = []
    steps = 0
    l = len(data)
    print data
    idx = 0
    while True:
        steps += 1
        value = max(data)
        index = data.index(value)
        data[index] = 0
        while value > 0:
            index += 1
            if index == l:
                index = 0
            data[index] += 1
            value -= 1
        t = tuple(data)
        if t in permutations:
            idx = permutations.index(t) + 1
            break
        permutations.append(t)
    print steps - idx

p2()