MAP = [['#']]
directions = {
    'R': [0, 1],
    'L': [0, -1],
    'U': [-1, 0],
    'D': [1, 0]
}


def add_blank_row():
    new_row = ['.']
    MAP.append(new_row)


def prepend_blank_row():
    new_row = ['.']
    MAP.insert(0, new_row)


def prepend_blank_column():
    for row in MAP:
        row.insert(0, '.')


with open('day18_input.txt', 'r') as file:
    curr_pos = [0, 0]
    for line in file:
        line = line.strip()
        direction, number, rgb = line.split(' ')
        movement = directions[direction]
        for _ in range(int(number)):
            curr_pos = [curr_pos[0] + movement[0], curr_pos[1] + movement[1]]
            while curr_pos[0] > len(MAP) - 1:
                add_blank_row()
            while curr_pos[0] < 0:
                prepend_blank_row()
                curr_pos[0] += 1
            while curr_pos[1] < 0:
                prepend_blank_column()
                curr_pos[1] += 1
            while curr_pos[1] > len(MAP[curr_pos[0]]) - 1:
                MAP[curr_pos[0]].append('.')

            MAP[curr_pos[0]][curr_pos[1]] = '#'

count = 0
for row, line in enumerate(MAP):
    num_crossings = 0
    crossing_ditch = False
    num_above = 0
    num_below = 0
    for col, char in enumerate(line):
        if char == '#':
            count += 1
            if not crossing_ditch:
                num_above = 0
                num_below = 0
                if row > 0 and len(MAP[row - 1]) > col and MAP[row - 1][col] == '#':
                    num_above += 1
                if row + 1 < len(MAP) and len(MAP[row + 1]) > col and MAP[row + 1][col] == '#':
                    num_below += 1
                crossing_ditch = True
            else:
                if row > 0 and len(MAP[row - 1]) > col and MAP[row - 1][col] == '#':
                    num_above += 1
                if row + 1 < len(MAP) and len(MAP[row + 1]) > col and MAP[row + 1][col] == '#':
                    num_below += 1
        elif char == '.':
            if crossing_ditch:
                crossing_ditch = False
                if num_above == 1 and num_below == 1:
                    num_crossings += 1
            if num_crossings % 2 == 1:
                MAP[row][col] = 'X'
                count += 1

print(count)
for line in MAP:
    print(''.join(line))
