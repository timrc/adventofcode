from common import run, read_lines_array

def get_last(registries, registry, x=0):
    return registries[x].get(registry, 0)

def get_value(registries, value, x=0):
    try:
        return int(value)
    except:
        return get_last(registries, value, x)

def set_value(registries, registry, value, x=0):
    registries[x][registry] = value

def do_operation(idx, instructions, registries, instruction, last_played_frequency):
    stop = False
    if len(instruction) == 3:
        operator, registry, value = instruction
    else:
        operator, registry = instruction
    print idx, last_played_frequency, instruction, registries
    if operator == 'set':
        rvalue = get_value(registries, value)
        set_value(registries, registry, rvalue)
    elif operator == 'add':
        last_frequency = get_last(registries, registry)
        rvalue = get_value(registries, value)
        set_value(registries, registry, last_frequency + rvalue)
    elif operator == 'mul':
        last_frequency = get_last(registries, registry)
        rvalue = get_value(registries, value)
        set_value(registries, registry, last_frequency * rvalue)
    elif operator == 'mod':
        last_frequency = get_last(registries, registry)
        rvalue = get_value(registries, value)
        if rvalue > 0:
            set_value(registries, registry, last_frequency % rvalue)
        else:
            set_value(registries, registry, 0)
    elif operator == 'snd':
        last_frequency = get_last(registries, registry)
        if last_frequency > 0:
            last_played_frequency = last_frequency
    elif operator == 'rcv':
        last_frequency = get_last(registries, registry)
        if last_frequency > 0:
            stop = True
    elif operator == 'jgz':
        last_frequency = get_last(registries, registry)
        rvalue = get_value(registries, value)
        if last_frequency > 0:
            last_played_frequency, stop, idx = do_operation(idx + rvalue, instructions, registries, instructions[idx + rvalue], last_played_frequency)

    return last_played_frequency, stop, idx

def p1():
    instructions = [line for line in read_lines_array(18)]
    registries = [
        {},
    ]
    last_played_frequency = 0
    idx = 0
    stop = False
    l = len(instructions)
    while not stop or idx < l:
        instruction = instructions[idx]
        last_played_frequency, stop, idx = do_operation(idx, instructions, registries, instruction, last_played_frequency)
        if stop:
            break
        idx += 1
    print last_played_frequency

def do_operation_2(x, y, idx, instructions, registries, instruction, queues, send):
    stop = False
    if len(instruction) == 3:
        operator, registry, value = instruction
    else:
        operator, registry = instruction
    if operator == 'set':
        rvalue = get_value(registries, value, x)
        set_value(registries, registry, rvalue, x)
    elif operator == 'add':
        last_frequency = get_last(registries, registry, x)
        rvalue = get_value(registries, value, x)
        set_value(registries, registry, last_frequency + rvalue, x)
    elif operator == 'mul':
        last_frequency = get_last(registries, registry, x)
        rvalue = get_value(registries, value, x)
        set_value(registries, registry, last_frequency * rvalue, x)
    elif operator == 'mod':
        last_frequency = get_last(registries, registry, x)
        rvalue = get_value(registries, value, x)
        if rvalue > 0:
            set_value(registries, registry, last_frequency % rvalue, x)
        else:
            set_value(registries, registry, 0, x)
    elif operator == 'snd':
        last_frequency = get_value(registries, registry, x)
        queues[x].append(last_frequency)
        send[x] += 1
    elif operator == 'rcv':
        if len(queues[y]) > 0:
            last_frequency = queues[y].pop(0)
            set_value(registries, registry, last_frequency, x)
        else:
            stop = True
            return stop, idx
    elif operator == 'jgz':
        last_frequency = get_last(registries, registry, x)
        rvalue = get_value(registries, value, x)
        if last_frequency > 0:
            return stop, idx + rvalue

    return stop, idx + 1

def p2():
    instructions = [line for line in read_lines_array(18)]
    registries = [
        {'p':0},
        {'p':1}
    ]
    queues = [
        [],
        []
    ]
    idx = [0, 0]
    stop = [False, False]
    send = [
        0,
        0
    ]
    l = len(instructions)
    register_index = 0
    while True:
        i = idx[register_index]
        instruction = instructions[i]
        new_stop, new_idx = do_operation_2(register_index, 1 - register_index, i, instructions, registries, instruction, queues, send)
        stop[register_index] = new_stop
        idx[register_index] = new_idx
        if new_stop:
            if len(queues[0]) == 0 and len(queues[1]) == 0:
                break
            print register_index, instruction
            print registries[0]
            print registries[1]
            print
            print '---------------------', send, len(queues[0]), len(queues[1])
            register_index = 1 - register_index
    print send, len(queues[0]), len(queues[1])

if __name__ == '__main__':
    run(p1, p2)