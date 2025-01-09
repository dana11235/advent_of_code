GATES = {}
LOGIC = []
Z_GATES = {}
X_GATES = {}
Y_GATES = {}
mode = 'gates'
with open('day24_input.txt', 'r') as file:
    for line in file:
        if len(line.strip()) == 0:
            mode = 'logic'
        elif mode == 'gates':
            gate, value = line.strip().split(':')
            GATES[gate] = int(value.strip())
            if gate.startswith('x'):
                X_GATES[int(gate[1:])] = GATES[gate]
            elif gate.startswith('y'):
                Y_GATES[int(gate[1:])] = GATES[gate]
        elif mode == 'logic':
            LOGIC.append(line.strip().split(' '))

while len(LOGIC) > 0:
    for line in LOGIC:
        if line[0] in GATES and line[2] in GATES:
            input_1 = GATES[line[0]]
            operation = line[1]
            input_2 = GATES[line[2]]
            output = line[4]
            computation = None
            if operation == 'AND':
                GATES[output] = input_1 and input_2
            elif operation == 'OR':
                GATES[output] = input_1 or input_2
            elif operation == 'XOR':
                val = (input_1 and not input_2) or (
                    input_2 and not input_1)
                if val:
                    GATES[output] = 1
                else:
                    GATES[output] = 0
            if 'z' in output:
                Z_GATES[int(output[1:])] = GATES[output]
            LOGIC.remove(line)


def parse_int(gates):
    output = ''
    keys = list(gates.keys())
    keys.sort()
    for key in keys:
        output = str(gates[key]) + output
    return int(output, 2)


xinput = parse_int(X_GATES)
yinput = parse_int(Y_GATES)
output = parse_int(Z_GATES)

print('OUTPUT', output)
# I went back and printed out the complete math problem. This won't be correct unless you use the
# correct gates in the "fixed" file.
print('MATH PROBLEM', xinput, '+', yinput, '=', output)
