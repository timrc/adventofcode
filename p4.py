from common import run, read_lines_array

def p1():
    valid = 0
    for d in read_lines_array(4):
        valid += 1 if (len(set(d)) == len(d)) else 0
    print valid


def p2():
    valid = 0
    for d in read_lines_array(4):
        valid += 1 if (len(set([''.join(sorted(x)) for x in d])) == len(d)) else 0
    print valid

if __name__ == '__main__':
    run(p1, p2)