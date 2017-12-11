from common import run, read_lines

def p1():
    registries = {}
    instructions = []
    for instruction in read_lines(8):
        instructions.append(instruction)
        regs = instruction.split(' ')
        registries[regs[0].strip()] = 0
        registries[regs[4].strip()] = 0
    max_value_total = None
    for instruction in instructions:
        data = instruction.split(' ')
        regA = data[0].strip()
        regB = data[4].strip()
        operation = data[1].strip()
        value = int(data[2].strip())
        condition = data[5].strip()
        target = int(data[6].strip())

        if condition == '>' and registries[regB] > target:
            registries[regA] += value if operation == 'inc' else -value
        elif condition == '<' and registries[regB] < target:
            registries[regA] += value if operation == 'inc' else -value
        elif condition == '>=' and registries[regB] >= target:
            registries[regA] += value if operation == 'inc' else -value
        elif condition == '<=' and registries[regB] <= target:
            registries[regA] += value if operation == 'inc' else -value
        elif condition == '==' and registries[regB] == target:
            registries[regA] += value if operation == 'inc' else -value
        elif condition == '!=' and registries[regB] != target:
            registries[regA] += value if operation == 'inc' else -value

    print max([y for x,y in registries.items()])

def p2():
    registries = {}
    instructions = []
    for instruction in read_lines(8):
        instructions.append(instruction)
        regs = instruction.split(' ')
        registries[regs[0].strip()] = 0
        registries[regs[4].strip()] = 0
    max_value_total = None
    for instruction in instructions:
        data = instruction.split(' ')
        regA = data[0].strip()
        regB = data[4].strip()
        operation = data[1].strip()
        value = int(data[2].strip())
        condition = data[5].strip()
        target = int(data[6].strip())

        if condition == '>' and registries[regB] > target:
            registries[regA] += value if operation == 'inc' else -value
        elif condition == '<' and registries[regB] < target:
            registries[regA] += value if operation == 'inc' else -value
        elif condition == '>=' and registries[regB] >= target:
            registries[regA] += value if operation == 'inc' else -value
        elif condition == '<=' and registries[regB] <= target:
            registries[regA] += value if operation == 'inc' else -value
        elif condition == '==' and registries[regB] == target:
            registries[regA] += value if operation == 'inc' else -value
        elif condition == '!=' and registries[regB] != target:
            registries[regA] += value if operation == 'inc' else -value

        new_max = max([y for x,y in registries.items()])
        if max_value_total is None or new_max > max_value_total:
            max_value_total = new_max

    print max_value_total

if __name__ == '__main__':
    run(p1, p2)