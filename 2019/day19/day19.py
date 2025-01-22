import os
import sys
here = os.path.dirname(__file__)
sys.path.append(os.path.join(here, '..'))
from intcode import IntCodeComputer
INPUT_OPS = []
with open('day19_input.txt', 'r') as file:
    for line in file:
        line = line.strip()
        INPUT_OPS += [int(code) for code in line.split(',')]

num_1s = 0
for y in range(50):
    row = ''
    for x in range(50):
        computer = IntCodeComputer(INPUT_OPS.copy())
        _, output = computer.run_step([x, y])
        output = output[0]
        num_1s += output
print('part a', num_1s)

# Calculates a single row
def get_row(y, start_x = 0):
    x = start_x
    hit_beam = None
    left_beam = None
    while left_beam is None:
        computer = IntCodeComputer(INPUT_OPS.copy())
        _, output = computer.run_step([x, y])
        output = output[0]
        if hit_beam is None and output == 1:
            hit_beam = x
        if hit_beam is not None and output == 0:
            left_beam = x - 1
        x += 1
    width = left_beam - hit_beam + 1
    return [hit_beam, left_beam, width]

def fits(num):
    hit_beam, _, width = get_row(num)
    _, left_beam, width2 = get_row(num - 99)
    if width < 100 or width2 < 100:
        return False
    else:
        # The beam 99 rows up must end after hit_beam + 99
        left_after = hit_beam + 99
        return left_beam >= left_after

row = 1509 # I started with somethign sufficiently high to speed things up
# This is a bit lame, but it works quickly enough
while True: 
    if fits(row):
        break
    else:
        row += 100
while True:
    if fits(row):
        row -= 10
    else:
        break
while True:
    if fits(row):
        break
    else:
        row += 1

x, _, _ = get_row(row)
print('part b', x * 10000 + (row - 99))