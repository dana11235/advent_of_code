import itertools
import os
import sys
here = os.path.dirname(__file__)
sys.path.append(os.path.join(here, '..'))
from intcode import run_program
OPS = []
PHASE_SETTINGS = [5, 6, 7, 8, 9]
with open('day7_input.txt', 'r') as file:
    for line in file:
        line = line.strip()
        OPS += [int(code) for code in line.split(',')]


max_power = 0
for combo in itertools.permutations(PHASE_SETTINGS, 5):
    states = []
    power = 0
    # Run the first iteration from scratch
    for i, input in enumerate(combo):
        states.append(run_program(OPS.copy(), [input, power], 0))
        power = states[i][1][0]
    # Now, continue to run until they have all halted (they will all halt at the same time)
    while not states[0][0]:
        for i, input in enumerate(combo):
            states[i] = run_program(states[i][3], [power], states[i][2])
            power = states[i][1][0]

    if power > max_power:
        max_power = power
print(max_power)