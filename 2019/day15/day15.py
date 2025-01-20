import heapq
import os
import sys
import random
import copy
here = os.path.dirname(__file__)
sys.path.append(os.path.join(here, '..'))
from intcode import run_program
INPUT_OPS = []
with open('day15_input.txt', 'r') as file:
    for line in file:
        line = line.strip()
        INPUT_OPS += [int(code) for code in line.split(',')]

MOVEMENTS = {
    1: [-1, 0],
    2: [1, 0],
    3: [0, -1],
    4: [0, 1]
}

def find_oxygen_system():
    VISITED = {}
    MOVES = []
    heapq.heapify(MOVES)

    pos = [0,0]
    heapq.heappush(MOVES, (0, random.random(), INPUT_OPS.copy(), 0, 0, pos))
    VISITED[str(pos)] = True

    while len(MOVES) > 0:
        next_move = heapq.heappop(MOVES)
        distance = next_move[0]
        ops = next_move[2]
        index = next_move[3]
        rel_base = next_move[4]
        pos = next_move[5]

        for i in range(4):
            direction = i + 1
            new_pos = [pos[0] + MOVEMENTS[direction][0], pos[1] + MOVEMENTS[direction][1]]
            pos_key = str(new_pos)
            if pos_key not in VISITED:
                VISITED[pos_key] = True
                _, output, next_index, opcodes, next_rel_base = run_program(copy.deepcopy(ops), [direction], index, rel_base)
                output = output[0]
                if output == 2:
                    return [distance + 1, index, ops, rel_base]
                elif output == 1:
                    heapq.heappush(MOVES, (distance + 1, random.random(), opcodes, next_index, next_rel_base, new_pos))

def print_map(map):
    keys = list(map.keys())
    keys.sort()
    for key in keys:
        values = map[key]
        kvs = list(values.keys())
        kvs.sort()
        row = ''
        index = -8
        while index <= 32:
            if index in kvs:
                row += map[key][index]
            else:
                row += ' '
            index += 1
        print(row)

def diffuse(input_ops, index, rel_base):
    MAP = {0: {0: '*'}}
    VISITED = {}
    MOVES = []
    heapq.heapify(MOVES)

    pos = [0,0]
    heapq.heappush(MOVES, (0, random.random(), input_ops.copy(), index, rel_base, pos))
    VISITED[str(pos)] = True

    max_dist = 0
    while len(MOVES) > 0:
        next_move = heapq.heappop(MOVES)
        distance = next_move[0]
        if distance > max_dist:
            max_dist = distance
        ops = next_move[2]
        index = next_move[3]
        rel_base = next_move[4]
        pos = next_move[5]

        for i in range(4):
            direction = i + 1
            new_pos = [pos[0] + MOVEMENTS[direction][0], pos[1] + MOVEMENTS[direction][1]]
            pos_key = str(new_pos)
            if pos_key not in VISITED:
                VISITED[pos_key] = True
                _, output, next_index, opcodes, next_rel_base = run_program(copy.deepcopy(ops), [direction], index, rel_base)
                output = output[0]
                if new_pos[0] not in MAP:
                    MAP[new_pos[0]] = {}
                if output == 1:
                    MAP[new_pos[0]][new_pos[1]] = '.'
                    heapq.heappush(MOVES, (distance + 1, random.random(), opcodes, next_index, next_rel_base, new_pos))
                elif output == 0:
                    MAP[new_pos[0]][new_pos[1]] = '#'

    #print_map(MAP)
    return max_dist + 1

distance, index, ops, rel_base = find_oxygen_system()
print('part a:', distance)
time = diffuse(ops, index, rel_base)
print('part b:', time)