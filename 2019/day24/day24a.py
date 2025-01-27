import math
import copy
MAP = []

with open('day24_input.txt', 'r') as file:
    for line in file:
        line = line.strip()
        MAP.append(list(line))


def print_map():
    print('---------')
    for row in MAP:
        print(''.join(row))
    print('---------')


row_len = len(MAP[0])


def calc_biodiversity():
    biodiversity = 0
    for y, row in enumerate(MAP):
        for x, char in enumerate(row):
            if char == '#':
                biodiversity += math.pow(2, (row_len * y) + x)
    return biodiversity


DIRECTIONS = [
    [1, 0], [0, 1], [-1, 0], [0, -1]
]


def in_bounds(y, x):
    return x >= 0 and y >= 0 and x < len(MAP[0]) and y < len(MAP)


def get_adjacent(y, x):
    num_adjacent = 0
    for dir in DIRECTIONS:
        adj_y = y + dir[0]
        adj_x = x + dir[1]
        if in_bounds(adj_y, adj_x) and MAP[adj_y][adj_x] == '#':
            num_adjacent += 1
    return num_adjacent


biodiversity_record = [calc_biodiversity()]

# print_map()
# print(biodiversity_record[0])
while True:
    new_map = copy.deepcopy(MAP)
    for y, row in enumerate(MAP):
        for x, char in enumerate(row):
            if char == '#' and get_adjacent(y, x) != 1:
                new_map[y][x] = '.'
            elif char == '.' and get_adjacent(y, x) in [1, 2]:
                new_map[y][x] = '#'
    MAP = new_map
    new_biodiversity = calc_biodiversity()
    # print_map()
    # print(new_biodiversity)
    if new_biodiversity in biodiversity_record:
        print('part a:', math.trunc(new_biodiversity))
        break
    else:
        biodiversity_record.append(new_biodiversity)
