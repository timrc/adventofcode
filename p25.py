from common import run



def check_tape(tape, cursor):
    if not cursor in tape:
        tape[cursor] = 0

def run_state_A(tape, cursor):
    check_tape(tape, cursor)
    if tape[cursor] == 0:
        tape[cursor] = 1
        cursor += 1
        return 'B', cursor
    else:
        tape[cursor] = 0
        cursor += 1
        return 'C', cursor

def run_state_B(tape, cursor):
    check_tape(tape, cursor)
    if tape[cursor] == 0:
        tape[cursor] = 0
        cursor -= 1
        return 'A', cursor
    else:
        tape[cursor] = 0
        cursor += 1
        return 'D', cursor

def run_state_C(tape, cursor):
    check_tape(tape, cursor)
    if tape[cursor] == 0:
        tape[cursor] = 1
        cursor += 1
        return 'D', cursor
    else:
        tape[cursor] = 1
        cursor += 1
        return 'A', cursor

def run_state_D(tape, cursor):
    check_tape(tape, cursor)
    if tape[cursor] == 0:
        tape[cursor] = 1
        cursor -= 1
        return 'E', cursor
    else:
        tape[cursor] = 0
        cursor -= 1
        return 'D', cursor

def run_state_E(tape, cursor):
    check_tape(tape, cursor)
    if tape[cursor] == 0:
        tape[cursor] = 1
        cursor += 1
        return 'F', cursor
    else:
        tape[cursor] = 1
        cursor -= 1
        return 'B', cursor

def run_state_F(tape, cursor):
    check_tape(tape, cursor)
    if tape[cursor] == 0:
        tape[cursor] = 1
        cursor += 1
        return 'A', cursor
    else:
        tape[cursor] = 1
        cursor += 1
        return 'E', cursor


def p1():
    state = 'A'
    tape = {}
    cursor = 0
    for x in xrange(12368930):
        if x % 100000 == 0:
            print x
        if state == 'A':
            state, cursor = run_state_A(tape, cursor)
        elif state == 'B':
            state, cursor = run_state_B(tape, cursor)
        elif state == 'C':
            state, cursor = run_state_C(tape, cursor)
        elif state == 'D':
            state, cursor = run_state_D(tape, cursor)
        elif state == 'E':
            state, cursor = run_state_E(tape, cursor)
        elif state == 'F':
            state, cursor = run_state_F(tape, cursor)
        # print cursor, state
    total = sum(tape.values())
    print total

def p2():
    pass

if __name__ == '__main__':
    run(p1, p2)