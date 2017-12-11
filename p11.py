from common import run, read_lines, read_lines_int_array

def solve(line):
    data = {}

    def add(step, n=1):
        if step not in data:
            data[step] = n
        else:
            data[step] += n

    def cancel(step1, step2):
        if data.get(step2, 0) > 0:
            tmp1 = data[step1]
            tmp2 = data[step2]
            data[step2] = max(0, tmp2 - tmp1)
            data[step1] = max(0, tmp1 - tmp2) 

    def replace(step1, step2, to):
        v = data[step1]
        if data.get(step2, 0) > 0:
            m = min(v, data[step2])
            data[step2] = max(0, data[step2] - m)
            data[k] = max(0, v - m)
            add(to, m)

    for step in line.split(','):
        add(step)

#   \ n  /
# nw +--+ ne
#   /    \
# -+      +-
#   \    /
# sw +--+ se
#   / s  \

    while True:
        s = sum(data.values())
        for k,v in data.items():
            if v == 0:
                continue
            if k == 'n':
                cancel(k, 's')
                replace(k, 'se', 'ne')
                replace(k, 'sw', 'nw')
            elif k == 'ne':
                cancel(k, 'sw')
                replace(k, 's', 'se')
                replace(k, 'nw', 'n')
            elif k == 'se':
                cancel(k, 'nw')
                replace(k, 'sw', 's')
                replace(k, 'n', 'ne')
            elif k == 's':
                cancel(k, 'n')
                replace(k, 'ne', 'se')
                replace(k, 'nw', 'sw')
            elif k == 'sw':
                cancel(k, 'ne')
                replace(k, 'n', 'nw')
                replace(k, 'se', 's')
            elif k == 'nw':
                cancel(k, 'se')
                replace(k, 's', 'sw')
                replace(k, 'ne', 'n')
        if s == sum(data.values()):
            break
    print sum(data.values())

def solve2(line):
    x = 0
    y = 0
    distance = 0
    distances = []
    for k in line.split(','):
        if k == 'n':
            x -= 1
            y += 1
        elif k == 'ne':
            y += 1
        elif k == 'nw':
            x -= 1
        elif k == 's':
            x += 1
            y -= 1
        elif k == 'se':
            x += 1
        elif k == 'sw':
            y -= 1

        new_distance = 0
        if (x >= 0 and y >= 0) or (x < 0 and y < 0):
            new_distance = abs(x + y)
        else:
            new_distance = max(abs(x), abs(y))

        distances.append(new_distance)
        if new_distance > distance:
            distance = new_distance
    print distance

def p1():
    # 810
    for line in read_lines(11):
        solve(line)

def p2():
    # Distance:
    #       http://althenia.net/svn/stackoverflow/hexgrid.png?usemime=1&rev=3
    #       https://stackoverflow.com/questions/5084801/manhattan-distance-between-tiles-in-a-hexagonal-grid
    # 1567
    for line in read_lines(11):
        solve2(line)

if __name__ == '__main__':
    run(p1, p2)