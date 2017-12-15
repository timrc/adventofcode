from common import run

def int_to_bin(number):
    scale = 32
    return bin(number)[2:].zfill(scale)

def numberGenerator(valA, factorA, valB, factorB, iterations=5):
    prev_valA = valA
    prev_valB = valB
    for x in xrange(iterations):
        next_valA = prev_valA * factorA
        next_valA = next_valA % 2147483647

        next_valB = prev_valB * factorB
        next_valB = next_valB % 2147483647

        yield [next_valA, next_valB]
        prev_valA = next_valA
        prev_valB = next_valB

def pickyNumberGenerator(valA, factorA, valB, factorB, iterations=5):
    prev_valA = valA
    prev_valB = valB
    for x in xrange(iterations):
        if x % 100000 == 0:
            print x
        while True:
            next_valA = prev_valA * factorA
            next_valA = next_valA % 2147483647
            if next_valA % 4 == 0:
                break
            prev_valA = next_valA


        while True:
            next_valB = prev_valB * factorB
            next_valB = next_valB % 2147483647
            if next_valB % 8 == 0:
                break
            prev_valB = next_valB

        yield [next_valA, next_valB]
        prev_valA = next_valA
        prev_valB = next_valB

def p1():
    matches = 0
    for numberA, numberB in numberGenerator(883, 16807, 879, 48271, iterations=40000000):
        bitsA = int_to_bin(numberA)
        bitsB = int_to_bin(numberB)
        if bitsA[-16:] == bitsB[-16:]:
            matches += 1
    print matches

def p2():
    matches = 0
    for numberA, numberB in pickyNumberGenerator(883, 16807, 879, 48271, iterations=5000000):
        bitsA = int_to_bin(numberA)
        bitsB = int_to_bin(numberB)
        if bitsA[-16:] == bitsB[-16:]:
            matches += 1
    print matches

if __name__ == '__main__':
    run(p1, p2)