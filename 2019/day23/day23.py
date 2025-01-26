import os
import sys
here = os.path.dirname(__file__)
sys.path.append(os.path.join(here, '..'))
from intcode import IntCodeComputer  # NOQA
INPUT_OPS = []
with open('day23_input.txt', 'r') as file:
    for line in file:
        line = line.strip()
        INPUT_OPS += [int(code) for code in line.split(',')]

computers = []
instructions = {}
for i in range(50):
    computer = IntCodeComputer(INPUT_OPS.copy())
    _, _ = computer.run_step([i])
    computers.append(computer)

nat_val = None
first_nat = False
last_y = None
ctu = True
while ctu:
    idle = True
    for index, computer in enumerate(computers):
        inputs = [-1]
        if index in instructions and len(instructions[index]) > 0:
            inputs = instructions[index]
            instructions[index] = []
        _, output = computer.run_step(inputs)
        if len(output) > 0:
            idle = False
            while len(output) > 0:
                destination = output.pop(0)
                x = output.pop(0)
                y = output.pop(0)
                if destination == 255:
                    if not first_nat:
                        print('part a', y)
                        first_nat = True
                    nat_val = [x, y]
                else:
                    if destination not in instructions:
                        instructions[destination] = []
                    instructions[destination].append(x)
                    instructions[destination].append(y)
    if idle:
        if last_y and last_y == y:
            print('part b', y)
            ctu = False
        else:
            last_y = y
        instructions[0] = nat_val
