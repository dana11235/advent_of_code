import heapq
import random
import math

MAZE = []
START_POSITION = [0, 0]
END_POSITION = [70, 70]
DIRECTIONS = [[0, 1], [1, 0], [0, -1], [-1, 0]]
VISITED_COUNTS = {}

CORRUPTIONS = []
BYTES = 1024
with open('day18_input.txt', 'r') as file:
    for index, line in enumerate(file):
        if index >= BYTES:
            break
        x_pos, y_pos = line.strip().split(',')
        CORRUPTIONS.append([int(y_pos), int(x_pos)])

for i in range(END_POSITION[0] + 1):
    row = []
    for j in range(END_POSITION[1] + 1):
        if [i, j] in CORRUPTIONS:
            row.append('#')
        else:
            row.append('.')
    MAZE.append(row)

print('starting maze')
for row in MAZE:
    print(''.join(row))
print('-------------')

NUM_ROWS = len(MAZE)
NUM_COLS = len(MAZE[0])
MOVES = [[0, 1, {
    'direction': 0,
    'visited': [START_POSITION]
}]]
print('start', START_POSITION)


def in_bounds(point):
    return point[0] >= 0 and point[1] >= 0 and point[0] < NUM_ROWS and point[1] < NUM_COLS


def distance_to_end(point):
    y_dist = END_POSITION[0] - point[0]
    x_dist = END_POSITION[1] - point[1]
    return math.sqrt(math.pow(y_dist, 2) + math.pow(x_dist, 2))


count = 0
while True:
    count += 1
    lowest_move = heapq.heappop(MOVES)[2]
    last_visited = lowest_move['visited'][-1]
    if last_visited[0] == END_POSITION[0] and last_visited[1] == END_POSITION[1]:
        for move in lowest_move['visited']:
            MAZE[move[0]][move[1]] = 'X'
        for line in MAZE:
            print(''.join(line))
        print('count', count)
        print('num moves', len(lowest_move['visited']) - 1)
        break
    elif str(last_visited) in VISITED_COUNTS:
        continue

    VISITED_COUNTS[str(last_visited)] = len(lowest_move['visited'])
    straight = DIRECTIONS[lowest_move['direction']]
    straight_pos = [last_visited[0] + straight[0],
                    last_visited[1] + straight[1]]
    if in_bounds(straight_pos) and straight_pos not in lowest_move['visited'] and MAZE[straight_pos[0]][straight_pos[1]] != '#':
        straight_move = {
            'direction': lowest_move['direction'],
            'visited': lowest_move['visited'].copy()
        }
        straight_move['visited'].append(straight_pos)
        heapq.heappush(MOVES, [len(straight_move['visited']) + distance_to_end(
            straight_pos), random.random(), straight_move])

    left = DIRECTIONS[(lowest_move['direction'] - 1) % 4]
    left_pos = [last_visited[0] + left[0],
                last_visited[1] + left[1]]
    if in_bounds(left_pos) and left_pos not in lowest_move['visited'] and MAZE[left_pos[0]][left_pos[1]] != '#':
        left_move = {
            'direction': (lowest_move['direction'] - 1) % 4,
            'visited': lowest_move['visited'].copy()
        }
        left_move['visited'].append(left_pos)
        heapq.heappush(MOVES, [len(left_move['visited']) + distance_to_end(
            left_pos), random.random(), left_move])

    right = DIRECTIONS[(lowest_move['direction'] + 1) % 4]
    right_pos = [last_visited[0] + right[0],
                 last_visited[1] + right[1]]
    if in_bounds(right_pos) and right_pos not in lowest_move['visited'] and MAZE[right_pos[0]][right_pos[1]] != '#':
        right_move = {
            'direction': (lowest_move['direction'] + 1) % 4,
            'visited': lowest_move['visited'].copy()
        }
        right_move['visited'].append(right_pos)
        heapq.heappush(MOVES, [len(right_move['visited']) + distance_to_end(
            right_pos), random.random(), right_move])
