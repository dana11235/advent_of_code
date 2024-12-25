GATES = {}
LOGIC = []
Z_GATES = {}
mode = 'gates'
with open('day24_input.txt', 'r') as file:
    for line in file:
        if len(line.strip()) == 0:
            mode = 'logic'
        elif mode == 'gates':
            gate, value = line.strip().split(':')
            GATES[gate] = int(value.strip())
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
output = ''
keys = list(Z_GATES.keys())
keys.sort()
for key in keys:
    output = str(Z_GATES[key]) + output

print(int(output, 2))
