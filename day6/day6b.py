cells = []
orig_direction = -1 
orig_col = -1
orig_row = -1
num_loops = 0
with open('day6_input.txt', 'r') as file:
    for index, line in enumerate(file):
        cells.append(list(line.strip()))
        if '>' in line:
            orig_row = index
            orig_col = line.index('>')
            orig_direction = 0
        elif '<' in line:
            orig_row = index
            orig_col = line.index('<')
            orig_direction = 2 
        elif '^' in line:
            orig_row = index
            orig_col = line.index('^')
            orig_direction = 3
        elif 'v' in line:
            orig_row = index
            orig_col = line.index('v')
            orig_direction = 1

num_rows = len(cells)
num_cols = len(cells[0])
#print(orig_direction, orig_row, orig_col)

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


for row_index, cells_row in enumerate(cells):
    for col_index, cell in enumerate(cells_row):
        if cell != '.':
            continue

        in_loop = False
        turns = []
        direction = orig_direction
        col = orig_col
        row = orig_row
        steps = 0

        while in_bounds(row, col) and not in_loop:
            cand_pos = get_next_cell(row, col, direction)
            
            while in_bounds(cand_pos[0], cand_pos[1]) and (cells[cand_pos[0]][cand_pos[1]] == '#' or (cand_pos[0] == row_index and cand_pos[1] == col_index)):
                turn_record = [row, col, direction]
                if turn_record in turns:
                    in_loop = True
                    num_loops += 1
                    break
                else:
                    turns.append(turn_record)
                    direction = (direction + 1) % 4
                    cand_pos = get_next_cell(row, col, direction)

            row = cand_pos[0]
            col = cand_pos[1]
            steps += 1
        #print(row_index, col_index, in_bounds(row, col), in_loop, steps)

print('loops', num_loops)