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

with open('day15_input.txt', 'r') as file:
    for index, line in enumerate(file):
        if line.strip() == '':
            GLOBALS['mode'] = "directions"
        elif GLOBALS['mode'] == "directions":
            for direction in list(line.strip()):
                GLOBALS['directions'].append(direction)
        else:
            row = list(line.strip())
            GLOBALS['map'].append(row)
            if '@' in row:
                GLOBALS['position'] = [index, row.index('@')]

for direction in GLOBALS['directions']:
    cursor = GLOBALS['position'].copy()
    command = GLOBALS['commands'][direction]
    while GLOBALS['map'][cursor[0]][cursor[1]] not in ['.', '#']:
        cursor[0] += command[0]
        cursor[1] += command[1]
    if GLOBALS['map'][cursor[0]][cursor[1]] == '.':
        while cursor != GLOBALS['position']:
            GLOBALS['map'][cursor[0]][cursor[1]] = GLOBALS['map'][cursor[0] -
                                                                  command[0]][cursor[1] - command[1]]
            cursor[0] -= command[0]
            cursor[1] -= command[1]
        GLOBALS['map'][cursor[0]][cursor[1]] = '.'
        GLOBALS['position'][0] += command[0]
        GLOBALS['position'][1] += command[1]

sum = 0
for row_index, line in enumerate(GLOBALS['map']):
    for col_index, char in enumerate(line):
        if char == 'O':
            sum += (100 * row_index + col_index)
print(sum)
