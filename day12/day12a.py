tiles = []
used = []
with open('day12_input.txt', 'r') as file:
    for line in file:
        line_pieces = list(line.strip())
        tiles.append(line_pieces)
used_row = []
for i in range(len(tiles[0])):
    used_row.append(0)
for i in range(len(tiles)):
    used.append(used_row.copy())


def explore_cell(row_index, col_index, cell):
    area = 0
    perimeter = 0
    if used[row_index][col_index] == 0:
        used[row_index][col_index] = 1
        area = 1
        if row_index > 0 and tiles[row_index - 1][col_index] == cell:
            if used[row_index - 1][col_index] == 0:
                print('N')
            add_area, add_perimeter = explore_cell(
                row_index - 1, col_index, cell)
            area += add_area
            perimeter += add_perimeter
        else:
            perimeter += 1
        if row_index < (len(tiles) - 1) and tiles[row_index + 1][col_index] == cell:
            if used[row_index + 1][col_index] == 0:
                print('S')
            add_area, add_perimeter = explore_cell(
                row_index + 1, col_index, cell)
            area += add_area
            perimeter += add_perimeter
        else:
            perimeter += 1
        if col_index > 0 and tiles[row_index][col_index - 1] == cell:
            if used[row_index][col_index - 1] == 0:
                print('W')
            add_area, add_perimeter = explore_cell(
                row_index, col_index - 1, cell)
            area += add_area
            perimeter += add_perimeter
        else:
            perimeter += 1
        if col_index < (len(tiles[0]) - 1) and tiles[row_index][col_index + 1] == cell:
            if used[row_index][col_index + 1] == 0:
                print('E')
            add_area, add_perimeter = explore_cell(
                row_index, col_index + 1, cell)
            area += add_area
            perimeter += add_perimeter
        else:
            perimeter += 1
    return [area, perimeter]


sum = 0
for row_index, row in enumerate(tiles):
    for col_index, cell in enumerate(row):
        area, perimeter = explore_cell(
            row_index, col_index, tiles[row_index][col_index])
        if area > 0:
            print(cell, area, perimeter)
        sum += area * perimeter
print(sum)
