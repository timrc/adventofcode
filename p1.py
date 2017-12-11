from common import run, read_lines

def p1():
    for line in read_lines(1, 1):
        data = line + line[0]
        sum = 0
        for i in xrange(len(data)):
            if i > 0:
                if data[i-1] == data[i]:
                    sum += int(data[i])
        print sum

def p2():
    for line in read_lines(1, 2):
        l = len(line)
        s = l/2
        sum = 0
        for i in xrange(l - s):
            if line[i] == line[i+s]:
                sum += (2*int(line[i]))
        print sum

if __name__ == '__main__':
    run(p1, p2)