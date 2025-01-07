import heapq
import random
import copy
import time
MAZE = []
START_POS = [0, 1]
DIRECTIONS = [[0, 1], [1, 0], [0, -1], [-1, 0]]
MOVES = []
VISITED_CACHE = {}

LARGE_NUMBER = 10000000
heapq.heapify(MOVES)

with open('day23_input.txt', 'r') as file:
    for line in file:
        MAZE.append(list(line.strip()))

END_POS = [len(MAZE) - 1, len(MAZE[0]) - 2]
end_str = str(END_POS)


def in_bounds(pos):
    return pos[0] >= 0 and pos[1] >= 0 and pos[0] < len(MAZE) and pos[1] < len(MAZE[0])


def not_rock(pos):
    return in_bounds(pos) and MAZE[pos[0]][pos[1]] != '#'


# This returns all of the squares that are valid moves
def get_possibilities(pos):
    possibilities = []
    for dir in DIRECTIONS:
        next = [pos[0] + dir[0], pos[1] + dir[1]]
        if in_bounds(next) and MAZE[next[0]][next[1]] != '#':
            possibilities.append(next)
    return possibilities


# In order to find a segment, we move one square at a time until there is more than one square left
def get_segment(pos, dir):
    visited = [pos]
    pos = [pos[0] + dir[0], pos[1] + dir[1]]
    visited.append(pos)
    num_moves = 0
    if not_rock(pos):
        num_moves += 1
        possibilities = get_possibilities(pos)
        while len(possibilities) == 2:
            new_pos = None
            for possibility in possibilities:
                if possibility not in visited:
                    new_pos = possibility
                    visited.append(possibility)
            num_moves += 1
            pos = new_pos
            possibilities = get_possibilities(pos)
    return {'num_moves': num_moves, 'next': pos}


SEGMENTS = {}


# This code finds all of the segments so that we can move one segment at a time instead of one square at a time
def explore(pos):
    segments = []
    for dir in DIRECTIONS:
        new_segment = get_segment(pos, dir)
        if new_segment['num_moves'] > 0:
            segments.append(new_segment)
    SEGMENTS[str(pos)] = segments
    for segment in segments:
        next_segment = segment['next']
        next_key = str(next_segment)
        if next_key not in SEGMENTS and next_key != end_str:
            explore(segment['next'])


explore(START_POS)


def visit(pos, visited):
    key = str(pos)
    visited[key] = True
    return visited


MAX_STEPS = {'num': -1}


def find_longest_path(segment, visited, traveled):
    # We add the length of this segment to the number of moves
    traveled += segment['num_moves']
    if segment['next'] == END_POS:
        if traveled > MAX_STEPS['num']:
            # This was some debug code I wrote to print progressive longer steps (since this takes a while to run)
            print('reached end in', traveled)
            MAX_STEPS['num'] = traveled
        return traveled
    else:
        next_key = str(segment['next'])
        visit(segment['next'], visited)
        max_steps = -1
        for next_segment in SEGMENTS[next_key]:
            if str(next_segment['next']) not in visited:
                num_steps = find_longest_path(
                    next_segment, copy.deepcopy(visited), traveled)
                if num_steps != -1 and (max_steps == -1 or num_steps > max_steps):
                    max_steps = num_steps
        return max_steps


start = time.time()
max_steps = find_longest_path(
    SEGMENTS[str(START_POS)][0], visit(START_POS, {}), 0)
print('max_steps', max_steps)
print('time', time.time() - start)
