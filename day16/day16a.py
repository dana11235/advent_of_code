import heapq
import copy
import random

MAZE = []
START_POSITION = []
DIRECTIONS = [[0, 1], [1, 0], [0, -1], [-1, 0]]
VISITED_COUNTS = {}
with open('day16_input.txt', 'r') as file:
    for row_index, line in enumerate(file):
        row = list(line.strip())
        MAZE.append(row)
        if 'S' in row:
            START_POSITION = [row_index, row.index('S')]

NUM_ROWS = len(MAZE)
NUM_COLS = len(MAZE[0])
MOVES = [[0, 1, {
    'score': 0,
    'direction': 0,
    'visited': [START_POSITION]
}]]
print('start', START_POSITION)


def in_bounds(point):
    return point[0] >= 0 and point[1] >= 0 and point[0] < NUM_ROWS and point[1] < NUM_COLS


count = 0
while True:
    count += 1
    lowest_move = heapq.heappop(MOVES)[2]
    last_visited = lowest_move['visited'][-1]
    if MAZE[last_visited[0]][last_visited[1]] == 'E':
        for move in lowest_move['visited']:
            MAZE[move[0]][move[1]] = 'X'
        for line in MAZE:
            print(''.join(line))
        print('count', count)
        print('score', lowest_move['score'])
        print('num moves', len(lowest_move['visited']))
        break
    elif str(last_visited) in VISITED_COUNTS and VISITED_COUNTS[str(last_visited)] < len(lowest_move['visited']):
        continue

    VISITED_COUNTS[str(last_visited)] = len(lowest_move['visited'])
    straight = DIRECTIONS[lowest_move['direction']]
    straight_pos = [last_visited[0] + straight[0],
                    last_visited[1] + straight[1]]
    if in_bounds(straight_pos) and straight_pos not in lowest_move['visited'] and MAZE[straight_pos[0]][straight_pos[1]] != '#':
        straight_move = {
            'score': lowest_move['score'] + 1,
            'direction': lowest_move['direction'],
            'visited': lowest_move['visited'].copy()
        }
        straight_move['visited'].append(straight_pos)
        heapq.heappush(MOVES, [
                       straight_move['score'], random.random(), straight_move])

    left = DIRECTIONS[(lowest_move['direction'] - 1) % 4]
    left_pos = [last_visited[0] + left[0],
                last_visited[1] + left[1]]
    if in_bounds(left_pos) and left_pos not in lowest_move['visited'] and MAZE[left_pos[0]][left_pos[1]] != '#':
        left_move = {
            'score': lowest_move['score'] + 1001,
            'direction': (lowest_move['direction'] - 1) % 4,
            'visited': lowest_move['visited'].copy()
        }
        left_move['visited'].append(left_pos)
        heapq.heappush(
            MOVES, [left_move['score'], random.random(), left_move])

    right = DIRECTIONS[(lowest_move['direction'] + 1) % 4]
    right_pos = [last_visited[0] + right[0],
                 last_visited[1] + right[1]]
    if in_bounds(right_pos) and right_pos not in lowest_move['visited'] and MAZE[right_pos[0]][right_pos[1]] != '#':
        right_move = {
            'score': lowest_move['score'] + 1001,
            'direction': (lowest_move['direction'] + 1) % 4,
            'visited': lowest_move['visited'].copy()
        }
        right_move['visited'].append(right_pos)
        heapq.heappush(MOVES, [
                       right_move['score'], random.random(), right_move])
