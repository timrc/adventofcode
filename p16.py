from common import run, read_lines_array

def swap(text, f, t):
    l = list(text)
    tmp = l[f]
    l[f] = l[t]
    l[t] = tmp
    return ''.join(l)

def p1():
    for x in read_lines_array(16, ','):
        operations = x
    data = 'abcdefghijklmnop'
    for op in operations:
        if op[0] == 's':
            s = int(op[1:])
            data = data[-s:] + data[:-s]
        elif op[0] == 'x':
            f,t = op[1:].split('/')
            f,t = int(f), int(t)
            data = swap(data, f, t)

        elif op[0] == 'p':
            fn,tn = op[1:].split('/')
            f = data.index(fn)
            t = data.index(tn)
            data = swap(data, f, t)
    print data

def p2():
    seen = []
    for x in read_lines_array(16, ','):
        operations = x
    data = 'abcdefghijklmnop'
    for i in xrange(1000000000):
        if data in seen: 
            print(seen[1000000000 % i])
            break
        seen.append(data)

        for op in operations:
            if op[0] == 's':
                s = int(op[1:])
                data = data[-s:] + data[:-s]
            elif op[0] == 'x':
                f,t = op[1:].split('/')
                f,t = int(f), int(t)
                data = swap(data, f, t)

            elif op[0] == 'p':
                fn,tn = op[1:].split('/')
                f = data.index(fn)
                t = data.index(tn)
                data = swap(data, f, t)

if __name__ == '__main__':
    run(p1, p2)