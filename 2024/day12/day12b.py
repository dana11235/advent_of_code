import copy
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

proto_surrounds = []
for i in range(3):
    proto_surround = []
    for j in range(3):
        proto_surround.append(0)
    proto_surrounds.append(proto_surround)


def explore_cell(row_index, col_index, cell):
    area = 0
    vertices = 0
    if used[row_index][col_index] == 0:
        used[row_index][col_index] = 1
        area = 1
        if row_index > 0 and tiles[row_index - 1][col_index] == cell:
            add_area, add_vertices = explore_cell(
                row_index - 1, col_index, cell)
            area += add_area
            vertices += add_vertices
        if row_index < (len(tiles) - 1) and tiles[row_index + 1][col_index] == cell:
            add_area, add_vertices = explore_cell(
                row_index + 1, col_index, cell)
            area += add_area
            vertices += add_vertices
        if col_index > 0 and tiles[row_index][col_index - 1] == cell:
            add_area, add_vertices = explore_cell(
                row_index, col_index - 1, cell)
            area += add_area
            vertices += add_vertices
        if col_index < (len(tiles[0]) - 1) and tiles[row_index][col_index + 1] == cell:
            add_area, add_vertices = explore_cell(
                row_index, col_index + 1, cell)
            area += add_area
            vertices += add_vertices

        surrounds = copy.deepcopy(proto_surrounds)
        if row_index == 0 or tiles[row_index - 1][col_index] != cell:
            surrounds[0][1] = 1
        if col_index == 0 or tiles[row_index][col_index - 1] != cell:
            surrounds[1][0] = 1
        if row_index == len(tiles) - 1 or tiles[row_index + 1][col_index] != cell:
            surrounds[2][1] = 1
        if col_index == len(tiles[0]) - 1 or tiles[row_index][col_index + 1] != cell:
            surrounds[1][2] = 1

        if row_index == 0:
            surrounds[0][0] = 1
            surrounds[0][2] = 1
        if col_index == 0:
            surrounds[0][0] = 1
            surrounds[2][0] = 1
        if row_index == len(tiles) - 1:
            surrounds[2][0] = 1
            surrounds[2][2] = 1
        if col_index == len(tiles[0]) - 1:
            surrounds[0][2] = 1
            surrounds[2][2] = 1

        if row_index != 0 and col_index != 0 and tiles[row_index - 1][col_index - 1] != cell:
            surrounds[0][0] = 1
        if row_index != 0 and col_index != len(tiles[0]) - 1 and tiles[row_index - 1][col_index + 1] != cell:
            surrounds[0][2] = 1
        if row_index != len(tiles) - 1 and col_index != 0 and tiles[row_index + 1][col_index - 1] != cell:
            surrounds[2][0] = 1
        if row_index != len(tiles) - 1 and col_index != len(tiles[0]) - 1 and tiles[row_index + 1][col_index + 1] != cell:
            surrounds[2][2] = 1

        curr_vertices = 0
        if (surrounds[1][0] == 1 and surrounds[0][1] == 1) or (surrounds[0][0] == 1 and surrounds[1][0] == 0 and surrounds[0][1] == 0):
            curr_vertices += 1
        if (surrounds[1][0] == 1 and surrounds[2][1] == 1) or (surrounds[2][0] == 1 and surrounds[1][0] == 0 and surrounds[2][1] == 0):
            curr_vertices += 1
        if (surrounds[1][2] == 1 and surrounds[0][1] == 1) or (surrounds[0][2] == 1 and surrounds[1][2] == 0 and surrounds[0][1] == 0):
            curr_vertices += 1
        if (surrounds[1][2] == 1 and surrounds[2][1] == 1) or (surrounds[2][2] == 1 and surrounds[1][2] == 0 and surrounds[2][1] == 0):
            curr_vertices += 1
        vertices += curr_vertices

    return [area, vertices]


sum = 0
for row_index, row in enumerate(tiles):
    for col_index, cell in enumerate(row):
        area, vertices = explore_cell(
            row_index, col_index, tiles[row_index][col_index])
        sum += area * vertices
print(sum)
