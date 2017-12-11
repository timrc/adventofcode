from math import ceil
from common import run, read_lines_int_array

def p1():
    for data in read_lines_int_array(6):
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
    for data in read_lines_int_array(6):
        permutations = []
        steps = 0
        l = len(data)
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

if __name__ == '__main__':
    run(p1, p2)