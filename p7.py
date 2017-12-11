from common import run, read_lines

def p1():
    data = {}
    for line in read_lines(7):
        struct = line.split('->')
        x = struct[0].split('(')[0].strip()
        has_children = len(struct) > 1
        if has_children:
            for s in struct[1].split(','):
                data[s.strip()] = x

    bottom = None
    node, parent = data.items()[0]
    while True:
        bottom = parent
        if not parent in data:
            break
        node = parent
        parent = data[parent]
    print bottom

def p2():
    children = {}
    parents = {}
    weight = {}
    for line in read_lines(7):
        struct = line.split('->')
        x = struct[0].split('(')[0].strip()
        weight[x] = int(struct[0].split('(')[1].split(')')[0].strip())
        children[x] = []
        if len(struct) > 1:
            for s in struct[1].split(','):
                parents[s.strip()] = x
                children[x].append(s.strip())

    root = None
    node, parent = parents.items()[0]
    while True:
        root = parent
        if not parent in parents:
            break
        node = parent
        parent = parents[parent]

    def set_weight(x):
        ch = children[x]
        if not len(children):
            return weight[x]

        ws = {}
        for c in ch:
            ws[c] = set_weight(c)

        vals = ws.values()
        if len(vals) > 0:
            mi = min(vals)
            ma = max(vals)
            if mi != ma:
                diff = ma - mi
                for a,b in ws.items():
                    if b == ma:
                        print a, weight[a], diff, weight[a] - diff
        return weight[x] + sum(vals)

    set_weight(root)

if __name__ == '__main__':
    run(p1, p2)