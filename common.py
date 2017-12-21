import sys

def run(*problems):
    problem = sys.argv[1] if len(sys.argv) > 1 else '1'
    func = problems[int(problem) - 1]
    if func:
        func()

def read_lines_raw(problem, sub_problem=None):
    file_name = 'p%d' % problem
    if sub_problem:
        file_name = '%s.%s' % (file_name, str(sub_problem))
    with open('data/%s.txt' % file_name) as file:
        for line in file:
            yield line.strip('\n')
            # yield line[:-1]

def read_lines(problem, sub_problem=None):
    for line in read_lines_raw(problem, sub_problem):
        yield line.strip()

def read_lines_array(problem, separator=' ', sub_problem=None):
    for line in read_lines(problem, sub_problem):
        yield line.split(separator)

def read_lines_int_array(problem, separator=' ', sub_problem=None):
    for arr in read_lines_array(problem, separator, sub_problem):
        yield [int(x) for x in arr]

def read_data_int(problem, sub_problem=None):
    return [int(x) for x in read_lines(problem, sub_problem)]