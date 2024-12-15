GLOBALS = {
    "mode": "maze",
    "directions": [],
    "map": [],
    "commands": {
        '<': [0, -1],
        '>': [0, 1],
        '^': [-1, 0],
        'v': [1, 0]
    },
    "position": [-1, -1]
}


def print_map():
    for p_row in GLOBALS['map']:
        print(''.join(p_row))


with open('day15_input.txt', 'r') as file:
    for index, line in enumerate(file):
        if line.strip() == '':
            GLOBALS['mode'] = "directions"
        elif GLOBALS['mode'] == "directions":
            for direction in list(line.strip()):
                GLOBALS['directions'].append(direction)
        else:
            row_input = list(line.strip())
            row = []
            for col_index, char in enumerate(row_input):
                if char == '.':
                    row.append('.')
                    row.append('.')
                elif char == 'O':
                    row.append('[')
                    row.append(']')
                elif char == '#':
                    row.append('#')
                    row.append('#')
                elif char == '@':
                    GLOBALS['position'] = [index, 2 * col_index]
                    row.append('@')
                    row.append('.')
            GLOBALS['map'].append(row)


def move(position, direction):
    command = GLOBALS['commands'][direction]
    piece = GLOBALS['map'][position[0]][position[1]]
    if piece in ['[', ']'] and direction in ['v', '^']:
        pos = [position[0], position[1]]
        if piece == ']':
            piece = '['
            pos = [position[0], position[1] - 1]
        next_piece1 = [pos[0] + command[0], pos[1] + command[1]]
        next_piece2 = [pos[0] + command[0], pos[1] + command[1] + 1]
        move(next_piece1, direction)
        move(next_piece2, direction)
        GLOBALS['map'][next_piece1[0]][next_piece1[1]] = piece
        GLOBALS['map'][next_piece2[0]][next_piece2[1]
                                       ] = GLOBALS['map'][pos[0]][pos[1] + 1]
        GLOBALS['map'][pos[0]][pos[1]] = '.'
        GLOBALS['map'][pos[0]][pos[1] + 1] = '.'
    elif piece in ['@', '[', ']']:
        next_position = [position[0] + command[0], position[1] + command[1]]
        move(next_position, direction)
        GLOBALS['map'][next_position[0]][next_position[1]] = piece
        GLOBALS['map'][position[0]][position[1]] = '.'


def can_move(position, direction):
    command = GLOBALS['commands'][direction]
    piece = GLOBALS['map'][position[0]][position[1]]
    if piece == '[' and direction in ['v', '^']:
        next_piece1 = [position[0] + command[0], position[1] + command[1]]
        next_piece2 = [position[0] + command[0], position[1] + command[1] + 1]
        return can_move(next_piece1, direction) and can_move(next_piece2, direction)
    elif piece == ']' and direction in ['v', '^']:
        next_piece1 = [position[0] + command[0], position[1] + command[1]]
        next_piece2 = [position[0] + command[0], position[1] + command[1] - 1]
        return can_move(next_piece1, direction) and can_move(next_piece2, direction)
    elif piece in ['@', '[', ']']:
        next_piece = [position[0] + command[0], position[1] + command[1]]
        return can_move(next_piece, direction)
    elif piece == '#':
        return False
    elif piece == '.':
        return True


# print_map()
for direction in GLOBALS['directions']:
    curr_pos = GLOBALS['position']
    if can_move(GLOBALS['position'], direction):
        # print('moving', direction)
        move(GLOBALS['position'], direction)
        command = GLOBALS['commands'][direction]
        GLOBALS['position'] = [curr_pos[0] +
                               command[0], curr_pos[1] + command[1]]
    # print_map()

sum = 0
for row_index, line in enumerate(GLOBALS['map']):
    for col_index, char in enumerate(line):
        if char == '[':
            sum += (100 * row_index + col_index)
print(sum)
