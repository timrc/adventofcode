from common import run, read_lines_array

def get_last(registries, registry):
    return registries.get(registry, 0)

def get_value(registries, value):
    try:
        return int(value)
    except:
        return get_last(registries, value)

def set_value(registries, registry, value):
    registries[registry] = value

def do_operation(idx, instructions, registries, send):
    stop = False
    instruction = instructions[idx]
    operator, registry, value = instruction
    if operator == 'set':
        rvalue = get_value(registries, value)
        set_value(registries, registry, rvalue)
    elif operator == 'sub':
        last_frequency = get_last(registries, registry)
        rvalue = get_value(registries, value)
        set_value(registries, registry, last_frequency - rvalue)
    elif operator == 'mul':
        last_frequency = get_last(registries, registry)
        rvalue = get_value(registries, value)
        send[0] += 1
        set_value(registries, registry, last_frequency * rvalue)
    elif operator == 'jnz':
        last_frequency = get_value(registries, registry)
        if last_frequency != 0:
            rvalue = get_value(registries, value)
            return stop, idx + rvalue

    return stop, idx + 1

def p1():
    instructions = [line for line in read_lines_array(23)]
    registries = {
        'a':1,
        'b':0,
        'c':0,
        'd':0,
        'e':0,
        'f':0,
        'g':0,
        'h':0,
    }
    queues = [
        [],
        []
    ]
    idx = 0
    stop = [False, False]
    send = [
        0,
    ]
    l = len(instructions)
    register_index = 0
    a = 0
    while True:
        if a % 10000 == 0:
            print a, registries

        stop, idx = do_operation(idx, instructions, registries, send)
        if stop:
            break
        a += 1

def p2():
    pass

if __name__ == '__main__':
    run(p1, p2)