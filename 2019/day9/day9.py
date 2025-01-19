import itertools
import os
import sys
here = os.path.dirname(__file__)
sys.path.append(os.path.join(here, '..'))
from intcode import run_program
OPS = []
with open('day9_input.txt', 'r') as file:
    for line in file:
        line = line.strip()
        OPS += [int(code) for code in line.split(',')]


_, output, _, _, _ = run_program(OPS.copy(), [1], 0)
print('part a', output[0])
_, output, _, _, _ = run_program(OPS.copy(), [2], 0)
print('part b', output[0])