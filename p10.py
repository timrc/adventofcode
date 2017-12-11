def p1():
    numbers = []
    data = range(256)
    with open('p10.txt') as file:
        for line in file:
            numbers = [int(x) for x in line.split(',')]
    
    skip = 0
    pos = 0
    l = len(data)
    last = l - 1
    for length in numbers:
        overflow = 0
        end = pos + length
        if end > last:
            overflow = end - l
        selection = data[pos:end]
        if overflow:
            selection += data[:overflow]
        p = 0
        old_data = data[::]
        old_selection = selection[::]
        selection = selection[::-1]
        for x in range(pos, min(l, end)):
            data[x] = selection[p]
            p += 1
        if overflow:
            for x in range(overflow):
                data[x] = selection[p]
                p += 1
        pos += (length + skip)
        while pos > last:
            pos = pos - l
        skip += 1
    print data[0] * data[1]

def do_hash(line):
    lengths = []
    sparse_hash = range(256)
    for x in line:
        lengths.append(ord(x))
    lengths += [17,31,73,47,23]
    
    skip = 0
    pos = 0
    l = len(sparse_hash)
    last = l - 1
    for i in range(64):
        for length in lengths:
            overflow = 0
            end = pos + length
            if end > last:
                overflow = end - l
            selection = sparse_hash[pos:end]
            if overflow:
                selection += sparse_hash[:overflow]
            p = 0
            selection = selection[::-1]
            for x in range(pos, min(l, end)):
                sparse_hash[x] = selection[p]
                p += 1
            if overflow:
                for x in range(overflow):
                    sparse_hash[x] = selection[p]
                    p += 1
            pos += (length + skip)
            while pos > last:
                pos = pos - l
            skip += 1
    dense_hash = []
    for x in range(16):
        tmp = reduce(lambda i, j: int(i) ^ int(j), sparse_hash[(x*16):((x+1)*16)])
        dense_hash.append(tmp)
    hash_hexadecimal = ''.join('0x{:02x}'.format(x)[2:] for x in dense_hash)
    print hash_hexadecimal

def p2():
    with open('p10.txt') as file:
        for line in file:
            do_hash(line.strip())

p2()