import math
import copy
MAP = []

with open('day24_input.txt', 'r') as file:
    for line in file:
        line = line.strip()
        MAP.append(list(line))
    MAP[2][2] = '?'


def print_map(map):
    for row in map:
        print(''.join(row))


blank_row = ['.', '.', '.', '.', '.']


def create_blank_map():
    new_map = []
    for _ in range(5):
        new_map.append(blank_row.copy())
    new_map[2][2] = '?'
    return new_map


MAPS = [MAP]


def print_maps():
    num_maps = len(MAPS)
    for index, map in enumerate(MAPS):
        print(f"-- MAP {index - num_maps // 2} --")
        print_map(map)
        print(f"-----------")


row_len = len(MAP[0])


DIRECTIONS = [
    [1, 0], [0, 1], [-1, 0], [0, -1]
]

MIDDLE_SQUARE = [2, 2]


def in_bounds(y, x):
    # We also check for the innermost square
    return x >= 0 and y >= 0 and x < len(MAP[0]) and y < len(MAP) and [y, x] != [2, 2]


def get_adjacent(index, y, x):
    num_adjacent = 0
    for dir in DIRECTIONS:
        adj_y = y + dir[0]
        adj_x = x + dir[1]
        if in_bounds(adj_y, adj_x) and MAPS[index][adj_y][adj_x] == '#':
            num_adjacent += 1
        elif not in_bounds(adj_y, adj_x):
            # Determine adjacencies on the next outer and next inner maps
            # The first 4 are outer maps, and the last is inner map
            if adj_y == -1 and index > 0:
                adjacent_map = MAPS[index - 1]
                if adjacent_map[1][2] == '#':
                    num_adjacent += 1
            elif adj_y == row_len and index > 0:
                adjacent_map = MAPS[index - 1]
                if adjacent_map[3][2] == '#':
                    num_adjacent += 1
            elif adj_x == -1 and index > 0:
                adjacent_map = MAPS[index - 1]
                if adjacent_map[2][1] == '#':
                    num_adjacent += 1
            elif adj_x == row_len and index > 0:
                adjacent_map = MAPS[index - 1]
                if adjacent_map[2][3] == '#':
                    num_adjacent += 1
            elif [adj_y, adj_x] == MIDDLE_SQUARE and index < len(MAPS) - 1:
                adjacent_map = MAPS[index + 1]
                if [y, x] == [1, 2]:
                    row = 0
                    for i in range(5):
                        if adjacent_map[row][i] == '#':
                            num_adjacent += 1
                elif [y, x] == [3, 2]:
                    row = 4
                    for i in range(5):
                        if adjacent_map[row][i] == '#':
                            num_adjacent += 1
                elif [y, x] == [2, 1]:
                    col = 0
                    for i in range(5):
                        if adjacent_map[i][col] == '#':
                            num_adjacent += 1
                elif [y, x] == [2, 3]:
                    col = 4
                    for i in range(5):
                        if adjacent_map[i][col] == '#':
                            num_adjacent += 1
    return num_adjacent


def calc_updated_map(index, map, new_map):
    num_added = 0
    for y, row in enumerate(map):
        for x, char in enumerate(row):
            # Ignore the middle row because it's special
            if [y, x] != [2, 2]:
                if char == '#' and get_adjacent(index, y, x) != 1:
                    new_map[y][x] = '.'
                elif char == '.' and get_adjacent(index, y, x) in [1, 2]:
                    new_map[y][x] = '#'
                    num_added += 1
    return num_added


def count_bugs(map):
    num_bugs = 0
    for row in range(5):
        for col in range(5):
            if map[row][col] == '#':
                num_bugs += 1
    return num_bugs


def run_step():
    global MAPS
    MAPS.insert(0, create_blank_map())
    MAPS.append(create_blank_map())
    new_maps = copy.deepcopy(MAPS)
    for index, map in enumerate(MAPS):
        calc_updated_map(index, map, new_maps[index])
    num_outer_bugs = count_bugs(new_maps[0])
    if num_outer_bugs == 0:
        new_maps.pop(0)
    num_inner_bugs = count_bugs(new_maps[-1])
    if num_inner_bugs == 0:
        new_maps.pop(-1)
    MAPS = new_maps


for _ in range(200):
    run_step()
# print_maps()
total_bugs = 0
for map in MAPS:
    total_bugs += count_bugs(map)
print('part b:', total_bugs)
