from common import run, read_data_int

def p1():
    data = read_data_int(5)
    index=0
    steps=0
    end_index=len(data)
    while index < end_index:
        instruction=data[index]
        data[index] += 1
        index += instruction
        steps += 1
    print steps


def p2():
    data = read_data_int(5)
    index=0
    steps=0
    end_index=len(data)
    while index < end_index:
        instruction=data[index]
        data[index] += (-1 if data[index] >= 3 else 1)
        index += instruction
        steps += 1
    print steps

if __name__ == '__main__':
    run(p1, p2)