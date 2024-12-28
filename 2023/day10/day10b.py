maze = []
start_pos = None
with open('day10_input.txt', 'r') as file:
    for index, line in enumerate(file):
        tiles = list(line.strip())
        maze.append(tiles)
        if 'S' in tiles:
            start_pos = [index, tiles.index('S')]

print('y', len(maze))
print('x', len(maze[0]))

paths = []
if maze[start_pos[0]][start_pos[1] - 1] in ['-', 'L', 'F']:
    paths.append([start_pos, [start_pos[0], start_pos[1] - 1]])
if maze[start_pos[0]][start_pos[1] + 1] in ['-', 'J', '7']:
    paths.append([start_pos, [start_pos[0], start_pos[1] + 1]])
if maze[start_pos[0] - 1][start_pos[1]] in ['|', '7', 'F']:
    paths.append([start_pos, [start_pos[0] - 1, start_pos[1]]])
if maze[start_pos[0] + 1][start_pos[1]] in ['|', 'L', 'J']:
    paths.append([start_pos, [start_pos[0] + 1, start_pos[1]]])


def get_next_move(path):
    current_tile = path[-1]
    prev_tile = path[-2]
    tile = maze[current_tile[0]][current_tile[1]]
    candidate_1 = None
    candidate_2 = None
    if tile == '-':
        candidate_1 = [current_tile[0], current_tile[1] - 1]
        candidate_2 = [current_tile[0], current_tile[1] + 1]
    elif tile == '|':
        candidate_1 = [current_tile[0] - 1, current_tile[1]]
        candidate_2 = [current_tile[0] + 1, current_tile[1]]
    elif tile == 'J':
        candidate_1 = [current_tile[0], current_tile[1] - 1]
        candidate_2 = [current_tile[0] - 1, current_tile[1]]
    elif tile == '7':
        candidate_1 = [current_tile[0], current_tile[1] - 1]
        candidate_2 = [current_tile[0] + 1, current_tile[1]]
    elif tile == 'F':
        candidate_1 = [current_tile[0], current_tile[1] + 1]
        candidate_2 = [current_tile[0] + 1, current_tile[1]]
    elif tile == 'L':
        candidate_1 = [current_tile[0] - 1, current_tile[1]]
        candidate_2 = [current_tile[0], current_tile[1] + 1]
    if candidate_1 == prev_tile:
        return candidate_2
    else:
        return candidate_1


while maze[paths[0][-1][0]][paths[0][-1][1]] != 'S':
    paths[0].append(get_next_move(paths[0]))


in_maze = 0
# The basic intuition is that we find spaces that are in an odd number of lines
for row_index, row in enumerate(maze):
    line_crossed = 0
    for col_index, cell in enumerate(row):
        if [row_index, col_index] in paths[0]:
            if maze[row_index][col_index] in ['|', 'J', 'L']:
                line_crossed += 1
        elif line_crossed % 2 == 1:
            # It turns out that we need to do it from both directions
            lines_remaining = 0
            for i in range(col_index, len(maze[0])):
                if [row_index, i] in paths[0] and maze[row_index][i] in ['|', 'J', 'L']:
                    lines_remaining += 1
            if lines_remaining % 2 == 1:
                in_maze += 1
                maze[row_index][col_index] = '*'
            else:
                maze[row_index][col_index] = ' '

        else:
            maze[row_index][col_index] = ' '

for point in paths[0]:
    maze[point[0]][point[1]] = 'X'

for row in maze:
    print(''.join(row))

print(in_maze)
