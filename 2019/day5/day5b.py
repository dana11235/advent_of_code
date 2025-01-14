def get_params(index, num_params, modes, ops, values_to_get=[]):
    a_param = None
    b_param = None
    c_param = None

    a_index = None
    b_index = None
    c_index = None

    if num_params == 3:
        a_index = index + 1
        b_index = index + 2 
        c_index = index + 3
    elif num_params == 2:
        a_index = index + 1
        b_index = index + 2 
    else:
        a_index = index + 1
    if c_index:
        if modes['c'] == 0:
            c_index = ops[c_index]
    if b_index:
        if modes['b'] == 0:
            b_index = ops[b_index]
        if 'b' in values_to_get:
            b_param = ops[b_index]
    if a_index:
        if modes['a'] == 0:
            a_index =ops[a_index]
        if 'a' in values_to_get:
            a_param = ops[a_index]
    return {'index': {'a': a_index,'b': b_index,'c': c_index}, 'value': {'a': a_param,'b': b_param,'c': c_param}}


def add(index, modes, ops):
    params = get_params(index, 3, modes, ops, ['a', 'b'])
    ops[params['index']['c']] = params['value']['a'] + params['value']['b']
    return index + 4

def mul(index, modes, ops):
    params = get_params(index, 3, modes, ops, ['a', 'b'])
    ops[params['index']['c']] = params['value']['a'] * params['value']['b']
    return index + 4

INPUT = {}
def stor(index, modes, ops):
    params = get_params(index, 1, modes, ops)
    ops[params['index']['a']] = INPUT['val']
    return index + 2

OUTPUT = []
def output(index, modes, ops):
    params = get_params(index, 1, modes, ops, ['a'])
    OUTPUT.append(params['value']['a'])
    return index + 2

def jump_if_true(index, modes, ops):
    params = get_params(index, 2, modes, ops, ['a', 'b'])
    if params['value']['a'] != 0:
        return params['value']['b']
    else:
        return index + 3

def jump_if_false(index, modes, ops):
    params = get_params(index, 2, modes, ops, ['a', 'b'])
    if params['value']['a'] == 0:
        return params['value']['b']
    else:
        return index + 3
    
def less_than(index, modes, ops):
    params = get_params(index, 3, modes, ops, ['a', 'b'])
    value = 0
    if params['value']['a'] < params['value']['b']:
        value = 1
    ops[params['index']['c']] = value

    return index + 4

def equals(index, modes, ops):
    params = get_params(index, 3, modes, ops, ['a', 'b'])
    value = 0
    if params['value']['a'] == params['value']['b']:
        value = 1
    ops[params['index']['c']] = value

    return index + 4


OPCODES = {
    1: add,
    2: mul,
    3: stor,
    4: output,
    5: jump_if_true,
    6: jump_if_false,
    7: less_than,
    8: equals
}

def parse_params(value):
    value = str(value)
    while len(value) < 5:
        value = '0' + value
    return [int(value[0]), int(value[1]), int(value[2]), int(value[3:])]

OPS = []
with open('day5_input.txt', 'r') as file:
    for line in file:
        line = line.strip()
        OPS += [int(num) for num in line.split(',')]

def run_program(input):
    INPUT['val'] = input
    index = 0
    while index <= len(OPS):
        c_mode, b_mode, a_mode, opcode = parse_params(OPS[index])
        modes = {'a': a_mode, 'b': b_mode, 'c': c_mode}
        if opcode == 99:
            break
        else:
            operation = OPCODES[opcode]
            index = operation(index, modes, OPS)

    print(OUTPUT)
    print(OUTPUT[-1])

run_program(5)