from common import run, read_lines_raw

def matrix_2_rule(matrix):
    return '/'.join([''.join(row) for row in matrix])

def rule_2_matrix(matrix_string):
    return [[c for c in row] for row in matrix_string.split('/')]

def rotate_clockwise(matrix, degree=90):
    return matrix if not degree else rotate_clockwise(zip(*matrix[::-1]), degree-90)

def get_permutations(rule):
    rule_matrix = rule_2_matrix(rule)
    flip_matrix = [row[::-1] for row in rule_matrix]
    # original
    yield matrix_2_rule(rule_matrix)
    # rotate 90
    yield matrix_2_rule(rotate_clockwise(rule_matrix, 90))
    # rotate -90
    yield matrix_2_rule(rotate_clockwise(rule_matrix, 270))
    # rotate 180
    yield matrix_2_rule(rotate_clockwise(rule_matrix, 180))
    # flip
    yield matrix_2_rule(flip_matrix)
    # rotate 90
    yield matrix_2_rule(rotate_clockwise(flip_matrix, 90))
    # rotate -90
    yield matrix_2_rule(rotate_clockwise(flip_matrix, 270))
    # rotate 180
    yield matrix_2_rule(rotate_clockwise(flip_matrix, 180))

def get_2_rules(all_rules):
    rules = {}
    for rule in all_rules:
        if len(rule[0]) == 5:
            for permutation in get_permutations(rule[0]):
                rules[permutation] = rule[1]
    return rules

def get_3_rules(all_rules):
    rules = {}
    for rule in all_rules:
        if len(rule[0]) == 11:
            for permutation in get_permutations(rule[0]):
                rules[permutation] = rule[1]
    return rules

def get_matrix(puzzle, group_size, x, y):
    matrix = []
    for a in xrange(group_size):
        matrix.append(puzzle[x + a][y:y + group_size])
    return matrix

def solve(iterations):
    puzzle = [
        '.#.',
        '..#',
        '###'
    ]
    rules = [line.split(' => ') for line in read_lines_raw(21)]
    rules_2 = get_2_rules(rules)
    rules_3 = get_3_rules(rules)

    for a in xrange(iterations):
        l = len(puzzle)
        group_size = 2 if l % 2 == 0 else 3
        t_group_size = 3 if group_size == 2 else 4
        groups = l / group_size
        new_matrix = [
            '' for _ in xrange(groups * (3 if group_size == 2 else 4))
        ]
        x_rules = rules_2 if group_size == 2 else rules_3
        for x in xrange(groups):
            for y in xrange(groups):
                matrix = get_matrix(puzzle, group_size, x * group_size, y * group_size)
                matrix_string = matrix_2_rule(matrix)
                for rule, val in x_rules.items():
                    if rule == matrix_string:
                        d = val.split('/')
                        for v in xrange(len(d)):
                            new_matrix[x * t_group_size + v] += d[v]
                        break

        puzzle = [''.join(row) for row in new_matrix]
    print sum([1 if c == '#' else 0 for c in matrix_2_rule(puzzle)])

def p1():
    solve(5)

def p2():
    solve(18)

if __name__ == '__main__':
    run(p1, p2)