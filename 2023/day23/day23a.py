import heapq
import random
import copy
MAZE = []
START_POS = [0, 1]
DIRECTIONS = [[0, 1], [1, 0], [0, -1], [-1, 0]]
MOVES = []
VISITED_CACHE = {}

LARGE_NUMBER = 10000000
heapq.heapify(MOVES)


def add_to_queue(curr):
    num_visited = len(curr['visited'].keys())
    heapq.heappush(
        MOVES, (LARGE_NUMBER - num_visited, random.random(), curr))


def get_next():
    return heapq.heappop(MOVES)[2]


with open('day23_input.txt', 'r') as file:
    for line in file:
        MAZE.append(list(line.strip()))


def prepare(pos, visited):
    key = str(pos)
    visited[key] = True
    num_visited = len(list(visited.keys()))
    VISITED_CACHE[key] = num_visited
    return {'pos': pos, 'visited': visited}


add_to_queue(prepare(START_POS, {}))

END_POS = [len(MAZE) - 1, len(MAZE[0]) - 2]

longest_solution = 0
while len(MOVES) > 0:
    curr = get_next()
    pos = curr['pos']
    key = str(pos)
    visited = curr['visited']
    num_moves = len(list(curr['visited'].keys()))
    if pos == END_POS:
        print('num moves', num_moves)
        if num_moves > longest_solution:
            longest_solution = num_moves
    else:
        dirs = DIRECTIONS
        curr_move = MAZE[pos[0]][pos[1]]
        if curr_move == '>':
            dirs = [[0, 1]]
        elif curr_move == '<':
            dirs = [[0, -1]]
        elif curr_move == '^':
            dirs = [[-1, 0]]
        elif curr_move == 'v':
            dirs = [[1, 0]]
        for dir in dirs:
            next = [pos[0] + dir[0], pos[1] + dir[1]]
            next_key = str(next)
            if MAZE[next[0]][next[1]] != '#' and next_key not in visited:
                # only visit this square if this is the longest path to the square (might get us into trouble)
                if next_key not in VISITED_CACHE or num_moves + 1 > VISITED_CACHE[next_key]:
                    add_to_queue(prepare(next, copy.deepcopy(visited)))

print('longest solution', longest_solution - 1)
