from common import run

def do_hash(val):
    lengths = []
    sparse_hash = range(256)
    for x in val:
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
    return hash_hexadecimal

def hex_to_bin(h):
    scale = 16
    num_of_bits = 4
    data = []
    for x in h:
        data.append(bin(int(x, scale))[2:].zfill(num_of_bits))
    return ''.join(data)

def p1():
    # val = 'flqrgnkx-%d' # Test
    val = 'amgozmfv-%d' # Actual
    data = [hex_to_bin(do_hash(val % d)) for d in range(128)]
    # for d in data:
    #    print d
    print (''.join(data)).count('1')

def connected(regions, data, i, j, region=1):
    if j < 0 or i < 0 or j >= len(data[0]) or i >= len(data):
        return
    if data[i][j] == '0':
        return

    data[i][j] = '0'
    regions[i][j] = region
    connected(regions, data, i+1, j, region)
    connected(regions, data, i-1, j, region)
    connected(regions, data, i, j+1, region)
    connected(regions, data, i, j-1, region)

def p2():
    # val = 'flqrgnkx-%d' # Test
    val = 'amgozmfv-%d' # Actual
    regions = []
    data = [[a for a in hex_to_bin(do_hash(val % d))] for d in range(128)]
    for a in xrange(128):
        regions.append([])
        for b in xrange(128):
            regions[a].append(0)
    region = 1
    for a in xrange(128):
        for b in xrange(128):
            connected(regions, data, a, b, region)
            region += 1

    # for y in range(16):
    #     print ['%4d' % x for x in regions[y][:16]]
    print len(set([x for x in reduce(lambda x, y: x+y, regions) if x > 0]))

if __name__ == '__main__':
    run(p1, p2)