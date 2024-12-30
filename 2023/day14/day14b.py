import copy
map = []
with open('day14_input.txt', 'r') as file:
    for row_index, line in enumerate(file):
        line = line.strip()
        map.append(list(line))


def tilt_north():
    lowest_rows = []
    row_index = 0
    while row_index < len(map):
        line = map[row_index]
        for col_index, char in enumerate(line):
            if len(lowest_rows) < len(line):
                if char == '.':
                    lowest_rows.append(row_index)
                else:
                    lowest_rows.append(-1)
            else:
                if lowest_rows[col_index] == -1 and char == '.':
                    lowest_rows[col_index] = row_index
                elif char == 'O' and lowest_rows[col_index] != -1:
                    original_row = lowest_rows[col_index]
                    map[original_row][col_index] = 'O'
                    map[row_index][col_index] = '.'
                    curr_row = original_row
                    lowest_rows[col_index] = -1
                    while curr_row <= row_index:
                        if map[curr_row][col_index] == '.':
                            lowest_rows[col_index] = curr_row
                            break
                        curr_row += 1
                elif char == '#':
                    lowest_rows[col_index] = -1
        row_index += 1


def tilt_south():
    lowest_rows = []
    row_index = len(map) - 1
    while row_index >= 0:
        line = map[row_index]
        for col_index, char in enumerate(line):
            if len(lowest_rows) < len(line):
                if char == '.':
                    lowest_rows.append(row_index)
                else:
                    lowest_rows.append(-1)
            else:
                if lowest_rows[col_index] == -1 and char == '.':
                    lowest_rows[col_index] = row_index
                elif char == 'O' and lowest_rows[col_index] != -1:
                    original_row = lowest_rows[col_index]
                    map[original_row][col_index] = 'O'
                    map[row_index][col_index] = '.'
                    curr_row = original_row
                    lowest_rows[col_index] = -1
                    while curr_row >= row_index:
                        if map[curr_row][col_index] == '.':
                            lowest_rows[col_index] = curr_row
                            break
                        curr_row -= 1
                elif char == '#':
                    lowest_rows[col_index] = -1
        row_index -= 1


def tilt_west():
    lowest_cols = []
    col_index = 0
    while col_index < len(map[0]):
        row_index = 0
        while row_index < len(map):
            char = map[row_index][col_index]
            if len(lowest_cols) < len(map):
                if char == '.':
                    lowest_cols.append(col_index)
                else:
                    lowest_cols.append(-1)
            else:
                if lowest_cols[row_index] == -1 and char == '.':
                    lowest_cols[row_index] = col_index
                elif char == 'O' and lowest_cols[row_index] != -1:
                    original_col = lowest_cols[row_index]
                    map[row_index][original_col] = 'O'
                    map[row_index][col_index] = '.'
                    curr_col = original_col
                    lowest_cols[row_index] = -1
                    while curr_col <= col_index:
                        if map[row_index][curr_col] == '.':
                            lowest_cols[row_index] = curr_col
                            break
                        curr_col += 1
                elif char == '#':
                    lowest_cols[row_index] = -1
            row_index += 1
        col_index += 1


def tilt_east():
    lowest_cols = []
    col_index = len(map[0]) - 1
    while col_index >= 0:
        row_index = 0
        while row_index < len(map):
            char = map[row_index][col_index]
            if len(lowest_cols) < len(map):
                if char == '.':
                    lowest_cols.append(col_index)
                else:
                    lowest_cols.append(-1)
            else:
                if lowest_cols[row_index] == -1 and char == '.':
                    lowest_cols[row_index] = col_index
                elif char == 'O' and lowest_cols[row_index] != -1:
                    original_col = lowest_cols[row_index]
                    map[row_index][original_col] = 'O'
                    map[row_index][col_index] = '.'
                    curr_col = original_col
                    lowest_cols[row_index] = -1
                    while curr_col >= col_index:
                        if map[row_index][curr_col] == '.':
                            lowest_cols[row_index] = curr_col
                            break
                        curr_col -= 1
                elif char == '#':
                    lowest_cols[row_index] = -1
            row_index += 1
        col_index -= 1


def calc_load(input):
    load = 0
    for index, line in enumerate(input):
        for char in line:
            if char == 'O':
                load += (len(input) - index)
    return load


def print_map(input):
    for line in input:
        print(''.join(line))


def run_cycle():
    tilt_north()
    tilt_west()
    tilt_south()
    tilt_east()


loads = []
cycles = []

cycle_calc = 1000000000
while True:
    run_cycle()
    load = calc_load(map)
    if map not in cycles:
        loads.append(load)
        cycles.append(copy.deepcopy(map))
    else:
        cycle_start = cycles.index(map) + 1
        cycle_len = len(cycles) + 1 - cycle_start
        cycle_num = ((cycle_calc - cycle_start) % cycle_len) + cycle_start
        print(loads[cycle_num - 1])

        break
