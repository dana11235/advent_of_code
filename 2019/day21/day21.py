import heapq
import os
import sys
import random
import copy
import itertools
here = os.path.dirname(__file__)
sys.path.append(os.path.join(here, '..'))
from intcode import IntCodeComputer
INPUT_OPS = []
with open('day21_input.txt', 'r') as file:
    for line in file:
        line = line.strip()
        INPUT_OPS += [int(code) for code in line.split(',')]

def disp(output):
    for line in output:
        print(line)

# I constructed both of these by hand by looking at examples. I tried writing code to figure this out, but it didn't work
# quite right
OPERATIONS_1 = [
    "NOT C J",
    "AND A J",
    "AND D J",
    "NOT A T",
    "OR T J",
    "WALK"
]

OPERATIONS_2 = [
    "NOT E T",
    "NOT G J",
    "OR J T",
    "NOT B J",
    "AND A J",
    "AND C J",
    "AND D J",
    "AND T J",
    "NOT C T",
    "AND A T",
    "AND D T",
    "AND H T",
    "OR T J",
    "NOT A T",
    "OR T J",
    "RUN"
]

computer = IntCodeComputer(INPUT_OPS.copy())
_, output = computer.run_ascii_step()
_, output = computer.run_ascii_steps(OPERATIONS_1)
print('part a:', output[-1])
computer = IntCodeComputer(INPUT_OPS.copy())
_, output = computer.run_ascii_step()
_, output = computer.run_ascii_steps(OPERATIONS_2)
print('part b:', output[-1])