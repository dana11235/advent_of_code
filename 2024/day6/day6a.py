cells = []
num_visited = 0
direction = -1 
col = -1
row = -1
with open('day6_input.txt', 'r') as file:
    for index, line in enumerate(file):
        cells.append(list(line.strip()))
        if '>' in line:
            row = index
            col = line.index('>')
            direction = 0
        elif '<' in line:
            row = index
            col = line.index('<')
            direction = 2 
        elif '^' in line:
            row = index
            col = line.index('^')
            direction = 3
        elif 'v' in line:
            row = index
            col = line.index('v')
            direction = 1

num_rows = len(cells)
num_cols = len(cells[0])
print(direction, col, row)

def in_bounds(row, col):
    return col >= 0 and col < num_cols and row >= 0 and row < num_rows

def get_next_cell(row, col, direction):
    if direction == 0:
        return [row, col + 1]
    elif direction == 1:
        return [row + 1, col]
    elif direction == 2:
        return [row, col - 1]
    elif direction == 3:
        return [row - 1, col]


while in_bounds(row, col):
    can_move = False
    cand_pos = get_next_cell(row, col, direction)
    
    while in_bounds(cand_pos[0], cand_pos[1]) and cells[cand_pos[0]][cand_pos[1]] == '#':
        direction = (direction + 1) % 4
        cand_pos = get_next_cell(row, col, direction)

    if cells[row][col] in ['.', '<', '>', '^']:
        cells[row][col] = 'X'
        num_visited += 1

    row = cand_pos[0]
    col = cand_pos[1]

for row in cells:
    print(row)
print(num_visited)





