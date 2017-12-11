from common import run, read_lines_array, read_lines_int_array

def p1():
    total = 0
    for data in read_lines_array(2):
        mi = None
        ma = None
        for i in data:
            m = int(i)
            if mi is None:
                mi = m
            elif m < mi:
                mi = m

            if ma is None:
                ma = m
            elif m > ma:
                ma = m
        total += (ma - mi)
    print total

def p2():
    # data = [
    #     [5, 9, 2, 8,],
    #     [9, 4, 7, 3,],
    #     [3, 8, 6, 5,],
    # ]
    s = 0
    for data in read_lines_int_array(2):
        bbb = False
        for ai in xrange(len(data)):
            for bi in xrange(ai+1, len(data)):
                a = data[ai]
                b = data[bi]
                x = a/b
                y = b/a
                if x*b == a:
                    s += x
                    bbb = True
                elif y*a == b:
                    s += y
                    bbb = True
                if bbb:
                    break
            if bbb:
                break
    print s

if __name__ == '__main__':
    run(p1, p2)