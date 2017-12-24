from common import run, read_lines_raw

def pp(nodes, s, x, y, d):
    print sum([1 if val == '#' else 0 for key,val in nodes.items()]), x, y, d
    for _y in xrange(s):
        line = ' '
        for _x in xrange(s):
            px = _x - (s/2)
            py = (s/2) - _y
            nk = '%d:%d' % (px, py)
            if px == x and py == y:
                line = line[:-1]
                line += '['
            if nk in nodes:
                line += nodes[nk]
            else:
                line += '.'
            if px == x and py == y:
                line += ']'
            else:
                line += ' '
        print line

def p1():
    nodes = {}
    _y = 0
    posx = 0
    posy = 0
    d = 'up'
    for line in read_lines_raw(22):
        l = len(line)
        center = l / 2
        y = center - _y
        for i in xrange(l):
            x = i - center
            nodes['%d:%d' % (x, y)] = line[i]
        _y += 1
    # pp(nodes, 13, posx, posy, d)
    infections = 0
    for b in xrange(10000):
        node_key = '%d:%d' % (posx, posy)
        node = nodes[node_key]
        if node == '.':
            infections += 1
        nodes[node_key] = '.' if node == '#' else '#'
        if d == 'up':
            if node == '.':
                d = 'left'
                posx -= 1
            elif node == '#':
                d = 'right'
                posx += 1
        elif d == 'down':
            if node == '.':
                d = 'right'
                posx += 1
            elif node == '#':
                d = 'left'
                posx -= 1
        elif d == 'left':
            if node == '#':
                d = 'up'
                posy += 1
            elif node == '#':
                d = 'down'
                posy -= 1
        elif d == 'right':
            if node == '#':
                d = 'down'
                posy -= 1
            elif node == '#':
                d = 'up'
                posy += 1
        # pp(nodes, 13, posx, posy, d)

        node_key = '%d:%d' % (posx, posy)
        if node_key not in nodes:
            nodes[node_key] = '.'

    print sum([1 if val == '#' else 0 for key,val in nodes.items()]), infections


def p2():
    nodes = {}
    _y = 0
    posx = 0
    posy = 0
    d = 'up'
    for line in read_lines_raw(22):
        l = len(line)
        center = l / 2
        y = center - _y
        for i in xrange(l):
            x = i - center
            nodes['%d:%d' % (x, y)] = line[i]
        _y += 1
    # pp(nodes, 13, posx, posy, d)
    infections = 0
    for b in xrange(10000000):
        node_key = '%d:%d' % (posx, posy)
        node = nodes[node_key]
        if node == 'W':
            infections += 1
        if node == '.':
            nodes[node_key] = 'W'
        elif node == 'W':
            nodes[node_key] = '#'
        if node == '#':
            nodes[node_key] = 'F'
        if node == 'F':
            nodes[node_key] = '.'

        if d == 'up':
            if node == '.':
                d = 'left'
                posx -= 1
            elif node == '#':
                d = 'right'
                posx += 1
            elif node == 'W':
                posy += 1
            elif node == 'F':
                d = 'down'
                posy -= 1
        elif d == 'down':
            if node == '.':
                d = 'right'
                posx += 1
            elif node == '#':
                d = 'left'
                posx -= 1
            elif node == 'W':
                posy -= 1
            elif node == 'F':
                d = 'up'
                posy += 1
        elif d == 'left':
            if node == '#':
                d = 'up'
                posy += 1
            elif node == '.':
                d = 'down'
                posy -= 1
            elif node == 'W':
                posx -= 1
            elif node == 'F':
                d = 'right'
                posx += 1
        elif d == 'right':
            if node == '#':
                d = 'down'
                posy -= 1
            elif node == '.':
                d = 'up'
                posy += 1
            elif node == 'W':
                posx += 1
            elif node == 'F':
                d = 'left'
                posx -= 1
        # pp(nodes, 13, posx, posy, d)

        node_key = '%d:%d' % (posx, posy)
        if node_key not in nodes:
            nodes[node_key] = '.'

    print sum([1 if val == '#' else 0 for key,val in nodes.items()]), infections


if __name__ == '__main__':
    run(p1, p2)