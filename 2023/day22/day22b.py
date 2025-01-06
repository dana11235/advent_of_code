import heapq
import random
PQ_BRICKS = []
BRICKS_BY_ID = {}
ORDERED_BRICKS = []
GRID = []
SUPPORT_GRID = []
max_x = 0
max_y = 0

heapq.heapify(PQ_BRICKS)


def add_to_heap(brick):
    heapq.heappush(PQ_BRICKS, (brick['start']['z'], random.random(), brick))


def get_next_brick():
    return heapq.heappop(PQ_BRICKS)[2]


with open('day22_input.txt', 'r') as file:
    for index, line in enumerate(file):
        line = line.strip()
        start, end = line.split('~')
        start = [int(num) for num in start.split(',')]
        start = {'x': start[0], 'y': start[1], 'z': start[2]}
        end = [int(num) for num in end.split(',')]
        end = {'x': end[0], 'y': end[1], 'z': end[2]}
        brick = {'start': start, 'end': end, 'index': index,
                 'supports': [], 'supported_by': []}
        add_to_heap(brick)
        BRICKS_BY_ID[index] = brick
        if end['x'] > max_x:
            max_x = end['x']
        if end['y'] > max_y:
            max_y = end['y']

proto_row = []
support_proto_row = []
for i in range(max_x + 1):
    proto_row.append(0)
    support_proto_row.append(-1)
for i in range(max_y + 1):
    GRID.append(proto_row.copy())
    SUPPORT_GRID.append(support_proto_row.copy())


def disp_grid(grid):
    for row in grid:
        print(','.join([str(num) for num in row]))
    print('')


while len(PQ_BRICKS) > 0:
    brick = get_next_brick()
    new_z = 0
    supported_by = []
    if brick['end']['z'] > brick['start']['z']:
        # brick is vertical
        z_diff = brick['end']['z'] - brick['start']['z']
        # We find the current z for the x and y, and add 1
        curr_z = GRID[brick['start']['y']][brick['start']['x']]
        curr_z += 1
        if curr_z > 1:
            supported_by.append(
                SUPPORT_GRID[brick['start']['y']][brick['start']['x']])

        GRID[brick['start']['y']][brick['start']['x']] = curr_z + z_diff
        SUPPORT_GRID[brick['start']['y']][brick['start']['x']] = brick['index']
        brick['start']['z'] = curr_z
        new_z = curr_z + z_diff
        brick['end']['z'] = new_z
    elif brick['end']['y'] > brick['start']['y']:
        # brick moves in the y direction
        curr_x = brick['start']['x']
        # We need to figure out the minimum z for bricks under the brick
        for y_pos in range(brick['start']['y'], brick['end']['y'] + 1):
            z_height = GRID[y_pos][curr_x]
            if z_height >= new_z:
                if z_height > new_z:
                    new_z = GRID[y_pos][curr_x]
                    supported_by = []
                supported_by.append(SUPPORT_GRID[y_pos][curr_x])
        # add 1 to this
        new_z += 1
        # Now assign this to the grid
        for y_pos in range(brick['start']['y'], brick['end']['y'] + 1):
            GRID[y_pos][curr_x] = new_z
            SUPPORT_GRID[y_pos][curr_x] = brick['index']
        brick['start']['z'] = new_z
        brick['end']['z'] = new_z
    else:
        # brick moves in the x direction
        curr_y = brick['start']['y']
        # We need to figure out the minimum z for bricks under the brick
        for x_pos in range(brick['start']['x'], brick['end']['x'] + 1):
            z_height = GRID[curr_y][x_pos]
            if z_height >= new_z:
                if z_height > new_z:
                    new_z = GRID[curr_y][x_pos]
                    supported_by = []

                supported_by.append(SUPPORT_GRID[curr_y][x_pos])
        # add 1 to this
        new_z += 1
        # Now assign this to the grid
        for x_pos in range(brick['start']['x'], brick['end']['x'] + 1):
            GRID[curr_y][x_pos] = new_z
            SUPPORT_GRID[curr_y][x_pos] = brick['index']
        brick['start']['z'] = new_z
        brick['end']['z'] = new_z
    supported_by = list(set(supported_by))
    if supported_by != [-1]:
        brick['supported_by'] = supported_by
    for supporter_id in supported_by:
        if supporter_id != -1:
            BRICKS_BY_ID[supporter_id]['supports'].append(brick['index'])


bricks_would_fall = 0
for brick in list(BRICKS_BY_ID.values()):
    # We only need to consider bricks that support other bricks
    if len(brick['supports']) > 0:
        disintegrated = [brick['index']]
        bricks_to_test = brick['supports'].copy()
        # We use a queue to do BFS
        while len(bricks_to_test) > 0:
            next_id = bricks_to_test.pop(0)
            next_brick = BRICKS_BY_ID[next_id]
            num_supports = 0
            # Check to see whether this brick is still supported by any bricks
            for id in next_brick['supported_by']:
                if id not in disintegrated:
                    num_supports += 1
            # If it isn't supported and it hasn't yet fallen, then it falls
            if num_supports == 0 and next_id not in disintegrated:
                bricks_would_fall += 1
                disintegrated.append(next_id)
                bricks_to_test += next_brick['supports']

print('num would fall', bricks_would_fall)
