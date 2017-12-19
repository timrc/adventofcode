from common import run, read_lines_raw

def p1():
    graph = {}
    y = 0
    starting_x = 0
    starting_y = 0
    l = 0
    for line in read_lines_raw(19):
        l = len(line) - 1
        x = 0
        for c in line:
            if c == ',':
                break
            graph['%d:%d' % (y, x)] = c or ' '
            if (c == '|' and y == 0):
                starting_x = x
                starting_y = y
            x += 1
        y += 1
    # for _y in xrange(y):
    #     for x in xrange(l):
    #         print graph['%d:%d' % (_y, x)],
    #     print

 #     |          
 #     |  +--+    
 #     A  |  C    
 # F---|----E|--+ 
 #     |  |  |  D 
 #     +B-+  +--+ 
    x = starting_x
    y = starting_y - 1
    letters = ''
    prev_c = None
    down = True
    up = False
    right = False
    left = False

    prev_x = x
    prev_y = y
    steps = 0
    while True:
        if down:
            y += 1
        if up:
            y -= 1
        if right:
            x += 1
        if left:
            x -= 1
        c = graph['%d:%d' % (y, x)]
        # print c, x, y, down, up, right, left

        if c == '|' and down:
            down = down
            up = False
            right = False
            left = False
        elif c == '|' and up:
            down = False
            up = up
            right = False
            left = False
        elif c == '|' and right:
            down = False
            up = False
            right = right
            left = False
        elif c == '|' and left:
            down = False
            up = False
            right = False
            left = left
        elif c == '-' and down:
            down = down
            up = False
            right = False
            left = False
        elif c == '-' and up:
            down = False
            up = up
            right = False
            left = False
        elif c == '-' and right:
            down = False
            up = False
            right = right
            left = False
        elif c == '-' and left:
            down = False
            up = False
            right = False
            left = left
        elif c == '+':
            if left or right:
                try:
                    up_c = graph['%d:%d' % (y-1, x)]
                except:
                    up_c = ' '
                try:
                    down_c = graph['%d:%d' % (y+1, x)]
                except:
                    down_c = ' '
                down = down_c != ' '
                up = up_c != ' '
                right = False
                left = False
            elif down or up:
                try:
                    left_c = graph['%d:%d' % (y, x-1)]
                except:
                    left_c = ' '
                try:
                    right_c = graph['%d:%d' % (y, x+1)]
                except:
                    right_c = ' '
                down = False
                up = False
                left = left_c != ' '
                right = right_c != ' '
        elif c != ' ':
            letters += c
        else:
            break
        steps += 1
    print steps
    print letters


def p2():
    pass

if __name__ == '__main__':
    run(p1, p2)