from common import run, read_lines_raw

def connect(i, xused, ports, xrotations, max_strengths, xlenghts):
    mmm = 0 if len(xlenghts) == 0 else max(xlenghts)
    for x in xrange(len(ports)):
        port = ports[x]
        used = xused[::]
        rotations = xrotations[::]
        lenghts = xlenghts[::]
        if len(used) == 0:
            if port[0] == 0:
                used.append(x)
                rotations.append(False)
                connect(x, used, ports, rotations, max_strengths, lenghts)
        else:
            xport = ports[used[-1]]
            rotated = rotations[-1]
            # print port, xport
            if x == i:
                continue
            if x in used:
                continue
            if not rotated and xport[1] == port[0]:
                used.append(x)
                rotations.append(False)
                if len(used) > 35:
                    print sum(ports[_][0] + ports[_][1] for _ in used)
                connect(x, used, ports, rotations, max_strengths, lenghts)
            elif not rotated and xport[1] == port[1]:
                used.append(x)
                rotations.append(True)
                if len(used) > 35:
                    print sum(ports[_][0] + ports[_][1] for _ in used)
                connect(x, used, ports, rotations, max_strengths, lenghts)
            elif rotated and xport[0] == port[0]:
                used.append(x)
                rotations.append(False)
                if len(used) > 35:
                    print sum(ports[_][0] + ports[_][1] for _ in used)
                connect(x, used, ports, rotations, max_strengths, lenghts)
            elif rotated and xport[0] == port[1]:
                used.append(x)
                rotations.append(True)
                if len(used) > 35:
                    print sum(ports[_][0] + ports[_][1] for _ in used)
                connect(x, used, ports, rotations, max_strengths, lenghts)
    strength = sum(ports[_][0] + ports[_][1] for _ in used)
    # print strength, [ports[_] for _ in used], rotations

    max_strengths.append(strength)
    # if  max(lenghts)
    # if len(lenghts) > 0:
    #     max_length = max(lenghts)
    #     if len(used) > max_length:
    #         print strength, len(used)

def p1():
    ports = [[int(_.split('/')[0]), int(_.split('/')[1])] for _ in read_lines_raw(24)]
    max_strengths = []
    lenghts = []
    connect(0, [], ports, [], max_strengths, lenghts)
    print max(max_strengths)

def p2():
    pass

if __name__ == '__main__':
    run(p1, p2)