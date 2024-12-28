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


while paths[0][-1] != paths[1][-1]:
    paths[0].append(get_next_move(paths[0]))
    paths[1].append(get_next_move(paths[1]))

print(len(paths[0]) - 1)
