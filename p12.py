from common import run, read_lines

def traverse_to_zero(programs, program, traversed=[]):
    if program == '0':
        return True

    # Failsafe to break from loop
    if program in traversed:
        return False

    traversed.append(program)

    childs = programs[program]
    for child in childs:
        ok = traverse_to_zero(programs, child, traversed)
        if ok:
            return True


def traverse(programs, program, traversed=[]):
    # Failsafe to break from loop
    if program in traversed:
        return

    traversed.append(program)

    for child in programs[program]:
        traverse(programs, child, traversed)

def p1():
    programs = {}
    for line in read_lines(12, 2):
        program, childs = line.split('<->')
        childs = childs.split(',')
        programs[program.strip()] = [c.strip() for c in childs]
    found = []
    for program, childs in programs.items():
        traversed = []
        ok = traverse_to_zero(programs, program, traversed)
        if ok:
            found.append(program)
    print len(found)


def p2():
    programs = {}
    for line in read_lines(12, 2):
        program, childs = line.split('<->')
        childs = childs.split(',')
        programs[program.strip()] = [c.strip() for c in childs]
    groups = 0
    # Iterate all programs
    for program, childs in programs.items():
        traversed = []
        # Check programs not already traversed
        if program in programs:
            # Find all subprocesses for the programs
            traverse(programs, program, traversed)
            if len(traversed) > 0:
                groups += 1
                for t in traversed:
                    if t in programs:
                        # Remove all traversed programs from the initial queue
                        del programs[t]

    print groups

if __name__ == '__main__':
    run(p1, p2)