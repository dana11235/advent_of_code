import os
import sys
here = os.path.dirname(__file__)
sys.path.append(os.path.join(here, '..'))
from intcode import run_program
INPUT_OPS = []
with open('day11_input.txt', 'r') as file:
    for line in file:
        line = line.strip()
        INPUT_OPS += [int(code) for code in line.split(',')]

MOVEMENTS = [
    [-1, 0],
    [0, 1],
    [1, 0],
    [0, -1]
]

def run_robot(initial_color):
    COORDINATES = [0, 0]
    DIRECTION = 0
    PANELS = {}
    OPS = INPUT_OPS.copy()

    finished = False
    rel_base = 0
    index = 0
    input = [initial_color]
    num_painted = 0

    while not finished:
        finished, output, index, OPS, rel_base = run_program(OPS, input, index, rel_base)
        if not finished:
            new_color = output[0]
            if COORDINATES[0] not in PANELS:
                PANELS[COORDINATES[0]] = {}
            if COORDINATES[1] not in PANELS[COORDINATES[0]]:
                num_painted += 1
            PANELS[COORDINATES[0]][COORDINATES[1]] = new_color
            direction = output[1]
            if direction == 0:
                DIRECTION = (DIRECTION - 1) % 4
            else:
                DIRECTION = (DIRECTION + 1) % 4
            COORDINATES = [COORDINATES[0] + MOVEMENTS[DIRECTION][0] , COORDINATES[1] + MOVEMENTS[DIRECTION][1]]
            if COORDINATES[0] not in PANELS or COORDINATES[1] not in PANELS[COORDINATES[0]]:
                input = [0]
            else:
                input = [PANELS[COORDINATES[0]][COORDINATES[1]]]
    return num_painted, PANELS

num_painted, _ = run_robot(0)
print('part a:', num_painted)

_, panels = run_robot(1)
print('part b')
for item in panels.items():
    values = item[1]
    x = list(values.keys())
    max_x = max(x)
    index = 0
    row = []
    while index <= max_x:
        if index in x:
            row.append(values[index])
        else:
            row.append(0)
        index += 1
    print(''.join([str(item) for item in row]).replace('0',' ').replace('1', '#'))
