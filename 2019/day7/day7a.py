import itertools
import os
import sys
here = os.path.dirname(__file__)
sys.path.append(os.path.join(here, '..'))
from intcode import run_program
OPS = []
PHASE_SETTINGS = [0, 1, 2, 3, 4]
with open('day7_input.txt', 'r') as file:
    for line in file:
        line = line.strip()
        OPS += [int(code) for code in line.split(',')]


max_power = 0
for combo in itertools.permutations(PHASE_SETTINGS, 5):
    power = 0
    for input in combo:
        _, power, _, _ = run_program(OPS.copy(), [input, power], 0)
        power = power[0]
    if power > max_power:
        max_power = power
print(max_power)