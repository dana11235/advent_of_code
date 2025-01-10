PROTO_OPS = []
with open('day2_input.txt', 'r') as file:
    for line in file:
        line = line.strip()
        PROTO_OPS += [int(num) for num in line.split(',')]


def run_intcode(noun, verb):
    OPS = PROTO_OPS.copy()
    OPS[1] = noun
    OPS[2] = verb
    index = 0
    while index <= len(OPS):
        if OPS[index] == 99:
            break
        elif OPS[index] == 1:
            OPS[OPS[index + 3]] = OPS[OPS[index + 1]] + OPS[OPS[index + 2]]
            index += 4
        elif OPS[index] == 2:
            OPS[OPS[index + 3]] = OPS[OPS[index + 1]] * OPS[OPS[index + 2]]
            index += 4

    return OPS[0]


for noun in range(100):
    for verb in range(100):
        output = run_intcode(noun, verb)
        if output == 19690720:
            print(noun * 100 + verb)
