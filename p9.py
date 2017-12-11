from collections import Counter
from common import run, read_lines

words = ['a', 'b', 'c', 'a']

def find_groups(stream):
    total = 0
    groups = 0
    open_stack = []
    skip_next = False
    removed = 0
    for c in stream:
        last = None
        if len(open_stack) > 0:
            last = open_stack[-1]
        if skip_next:
            skip_next = False
            continue
        if c == '!':
            skip_next = True
            continue
        elif last != '<' and c == '<':
            open_stack.append(c)
            continue
        if last == '<' and c != '>':
            removed += 1
            continue
        elif last == '<' and c == '>':
            open_stack.pop()
            continue
        else:
            if c == '{':
                open_stack.append(c)
                continue
            if c == '}' and last == '{':
                k = Counter(open_stack).keys()
                i = k.index('{')
                v = Counter(open_stack).values()
                total += v[i]
                open_stack.pop()
                groups += 1
                continue
    return total, removed

def p1():
    groups = 0

    for line in read_lines(9, 1):
        total, removed = find_groups(line)
        groups += total
    print groups

def p2():
    groups = 0

    for line in read_lines(9, 1):
        total, removed = find_groups(line)
        groups += removed
    print groups


if __name__ == '__main__':
    run(p1, p2)