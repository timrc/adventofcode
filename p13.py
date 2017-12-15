from common import run, read_lines
import copy

# 0: 3
# 1: 2
# 4: 4
# 6: 4
def p1():
    data = {}
    state = {}
    direction = {}
    for line in read_lines(13):
        idx, depth = line.split(': ')
        data[int(idx)] = int(depth)
        state[int(idx)] = 0
        direction[int(idx)] = 1
    keys = data.keys()
    m = max(keys)
    for x in range(m + 1):
        if x not in data:
            data[x] = 0
            state[x] = 0
    idx = -1
    severity = []

    # print data  
    for x in range(m + 1):
        idx += 1
        # print idx, state
        if data[x] > 0 and state[x] == 0:
            severity.append(x)
        for d,r in state.items():
            if data[d] > 0:
                state[d] += (1 * direction[d])
                if state[d] >= data[d]:
                    direction[d] = -1
                    state[d] -=2
                if state[d] < 0:
                    direction[d] = 1
                    state[d] += 2
    print sum([d*x for d,x in data.items() if d in severity])

import time


def p2():

    # START = time.time()

    # data = open("data/p13.txt", "r")
    # rows = data.read().strip().split("\n")

    # valDict = dict()

    # for row in rows:
    #     rowS = row.split(" ")
    #     valDict[int(rowS[0][:-1])] = int(rowS[-1])

    # caught = False
    # for delay in xrange(10, 10**7):
    #     caught = False
    #     print 'DELAY', delay
    #     for i in valDict.keys():
    #         print i, (i+delay), (2* valDict[i] - 2), (i+delay) % (2* valDict[i] - 2) == 0
    #         if (i+delay) % (2* valDict[i] - 2) == 0:
    #             caught = True
    #             break
    #     if not caught:
    #         print delay
    #         break


    # print "Time Taken:", time.time() - START

    # 3946838

    data = {}
    state = {}
    direction = {}
    for line in read_lines(13):
        idx, depth = line.split(': ')
        data[int(idx)] = int(depth)
        state[int(idx)] = 0
        direction[int(idx)] = 1
    keys = data.keys()
    m = max(keys)
    for x in range(m + 1):
        if x not in data:
            data[x] = 0
            state[x] = 0

    initial_data = copy.deepcopy(data)
    initial_state = copy.deepcopy(state)
    initial_direction = copy.deepcopy(direction)

    for i in range(10):
        for d in initial_state.keys():
            if initial_data[d] > 0:
                initial_state[d] += (1 * initial_direction[d])
                if initial_state[d] >= initial_data[d]:
                    initial_direction[d] = -1
                    initial_state[d] -=2
                if initial_state[d] < 0:
                    initial_direction[d] = 1
                    initial_state[d] += 2

    for p in xrange(11, 10**7):
        for d in initial_state.keys():
            if initial_data[d] > 0:
                initial_state[d] += (1 * initial_direction[d])
                if initial_state[d] >= initial_data[d]:
                    initial_direction[d] = -1
                    initial_state[d] -=2
                if initial_state[d] < 0:
                    initial_direction[d] = 1
                    initial_state[d] += 2

        data = copy.deepcopy(initial_data)
        state = copy.deepcopy(initial_state)
        direction = copy.deepcopy(initial_direction)
        idx = -1
        severity = []

        if p % 100 == 0:
            print p

        caught = False
        for x in xrange(m + 1):
            idx += 1
            if data[x] > 0 and state[x] == 0:
                caught = True
                break
            for d in state.keys():
                if data[d] > 0:
                    state[d] += (1 * direction[d])
                    if state[d] >= data[d]:
                        direction[d] = -1
                        state[d] -=2
                    if state[d] < 0:
                        direction[d] = 1
                        state[d] += 2
        if not caught:
            break
    print p

if __name__ == '__main__':
    run(p1, p2)