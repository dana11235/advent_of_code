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

OPERATIONS_1 = [
    "NOT C J",
    "AND A J",
    "AND D J",
    "NOT A T",
    "OR T J",
    "WALK"
]

OPERATIONS_2 = [
    "NOT B J",
    "AND A J",
    "AND C J",
    "AND D J",
    "NOT E T",
    "AND T J",
    #
    "NOT C T",
    "AND A T",
    "AND D T",
    "AND H T",
    #
    "OR T J",
    #
    "NOT A T",
    "OR T J",
    "RUN"
]

computer = IntCodeComputer(INPUT_OPS.copy())
_, output = computer.run_ascii_step()
_, output = computer.run_ascii_steps(OPERATIONS_1)
print('part a:', output[-1])
#computer = IntCodeComputer(INPUT_OPS.copy())
#_, output = computer.run_ascii_step()
#_, output = computer.run_ascii_steps(OPERATIONS_2)
#disp(output)

prototype = ['.','.','.','.','.','.','.','.','.']
def represent(combo):
    rep = prototype.copy()
    for let in combo:
        rep[ord(let) - ord('a')] = '#'
    return rep

def can_walk(combo):
    jump = False
    walk = False

    if len(combo) < 4:
        jump = True
    elif combo[3] != '.':
        # Jumping won't land in a pit
        jump = can_walk(combo[4:])

    if len(combo) == 0:
        walk = True
    elif combo[0] != '.':
        # walking won't land in a pit
        walk = can_walk(combo[1:])
    
    if jump and not walk:
        return False
    else:
        # If there is no path forward, this returns true, but that's ok
        return True

list = ['a','b','c','d','e','f','g','h','i']
combos = []
for i in range(8):
    to_keep = i + 1
    for combo in itertools.combinations(list, to_keep):
        if not can_walk(represent(combo)):
            combos.append(combo)
for combo in combos:
    print(represent(combo))
print(len(combos))
    


