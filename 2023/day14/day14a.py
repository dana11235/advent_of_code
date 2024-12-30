map = []
lowest_rows = []
with open('day14_input.txt', 'r') as file:
    for row_index, line in enumerate(file):
        line = line.strip()
        map.append(list(line))
        for col_index, char in enumerate(line):
            if len(lowest_rows) < len(line):
                if char == '.':
                    lowest_rows.append(row_index)
                else:
                    lowest_rows.append(-1)
            else:
                if lowest_rows[col_index] == -1 and char == '.':
                    lowest_rows[col_index] = row_index
                elif char == 'O' and lowest_rows[col_index] > -1:
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


load = 0
for index, line in enumerate(map):
    for char in line:
        if char == 'O':
            load += (len(map) - index)
print(load)
