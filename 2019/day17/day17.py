import heapq
import os
import sys
import random
import copy
here = os.path.dirname(__file__)
sys.path.append(os.path.join(here, '..'))
from intcode import IntCodeComputer
INPUT_OPS = []
with open('day17_input.txt', 'r') as file:
    for line in file:
        line = line.strip()
        INPUT_OPS += [int(code) for code in line.split(',')]


computer = IntCodeComputer(INPUT_OPS.copy())
_, output = computer.run_step([])

def print_output(output):
    output_str = ''
    for char in output:
        output_str += chr(char)

    print(output_str)

def build_map(output):
    map = []
    line = []
    for char in output:
        if char != 10:
            line.append(chr(char))
        elif len(line) > 0:
            map.append(line)
            line = []
    if len(line) > 0:
        map.append(line)
    return map

def print_map(map):
    for line in map:
        print(''.join(line))

map = build_map(output)

moves = [
    [0, -1], [-1, 0], [0, 1], [1, 0]
]

START_POS = None
alignment_sum = 0
for y, line in enumerate(map):
    if '^' in line:
        START_POS = [y, line.index('^')]
    if y > 0 and y < len(map) - 1:
        for x, char in enumerate(line):
            if x > 0 and x < len(line) - 1 and char == '#':
                is_intersection = True
                for dir in moves:
                    pos = [y + dir[0], x + dir[1]]
                    if map[pos[0]][pos[1]] == '.':
                        is_intersection = False
                if is_intersection:
                    alignment_sum += x * y
print('part a:', alignment_sum)
#print_map(map)

def convert_function_to_ascii(function):
    ascii = []
    for char in list(function):
        ascii.append(ord(char))
    ascii.append(10)
    return ascii

# This converts the inputs into the input array. Technically we could do these one at a time, but we can just feed them in at once
def convert_input(main, func_a, func_b, func_c, video):
    input = []
    input += convert_function_to_ascii(main)
    input += convert_function_to_ascii(func_a)
    input += convert_function_to_ascii(func_b)
    input += convert_function_to_ascii(func_c)
    input += convert_function_to_ascii(video)
    return input

def in_bounds(pos):
    return pos[0] >= 0 and pos[1] >= 0 and pos[0] < len(map) and pos[1] < len(map[0])

def get_move(pos, direction):
    return [pos[0] + moves[direction][0], pos[1] + moves[direction][1]]

def is_scaffold(pos):
    return map[pos[0]][pos[1]] == '#'

# Calculates the instructions to go from the beginning to the end
def get_instruction(start_pos):
    INSTRUCTIONS = ['L']
    pos = start_pos.copy()
    direction = 0
    run = 0
    while True:
        next_move = get_move(pos, direction)
        # Go forward if we can
        if in_bounds(next_move) and is_scaffold(next_move):
            run += 1
            pos = next_move
        else:
            INSTRUCTIONS.append(str(run))
            run = 0
            # Otherwise, we try turning both left and right
            left_move = get_move(pos, (direction - 1) % 4)
            right_move = get_move(pos, (direction + 1) % 4)
            if is_scaffold(left_move):
                INSTRUCTIONS.append('L')
                direction = (direction - 1) % 4
            elif is_scaffold(right_move):
                INSTRUCTIONS.append('R')
                direction = (direction + 1) % 4
            else:
                # If we can't turn left or right, we must be at the end
                break
    return ','.join(INSTRUCTIONS)

instructions = get_instruction(START_POS)
# I figured the functions out by looking at the instructions. There might be a way to do it automatically
FUNCTION_A = 'L,10,L,10,R,6'
FUNCTION_B = 'R,12,L,12,L,12'
FUNCTION_C = 'L,6,L,10,R,12,R,12'
# Generate the main routine by replacing the functions with their letters
MAIN_ROUTINE = instructions.replace(FUNCTION_A, 'A').replace(FUNCTION_B, 'B').replace(FUNCTION_C, 'C')
VIDEO_FEED = 'n'

input = convert_input(MAIN_ROUTINE, FUNCTION_A, FUNCTION_B, FUNCTION_C, VIDEO_FEED)

ops = INPUT_OPS.copy()
ops[0] = 2

move_computer = IntCodeComputer(ops)
finished, output = move_computer.run_step(input)
#print_output(output[:-1])

# The last piece of output is the answer (the other pieces are strings/video the computer returns)
print('part b:', output[-1])