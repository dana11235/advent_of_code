import os
import sys
import copy
here = os.path.dirname(__file__)
sys.path.append(os.path.join(here, '..'))
from intcode import IntCodeComputer  # NOQA
INPUT_OPS = []
with open('day25_input.txt', 'r') as file:
    for line in file:
        line = line.strip()
        INPUT_OPS += [int(code) for code in line.split(',')]

computer = IntCodeComputer(INPUT_OPS.copy())
finished = False
inp = None
while not finished:
    finished, output = computer.run_ascii_step(inp)
    for line in output:
        print(line)
    inp = input()

# I just built a repl and played the text adventure game manually
