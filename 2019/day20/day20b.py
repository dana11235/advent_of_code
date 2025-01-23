import heapq
import random
MAZE = []
PORTALS = {}
REVERSE_PORTALS = {}
PORTAL_POS = {}
VISITED = {}

with open('day20_input.txt', 'r') as file:
    for line in file:
        line = line[:-1]
        MAZE.append(list(line))

def is_letter(char):
    return char >= 'A' and char <= 'Z'

def in_bounds(y, x):
    return y >= 0 and x >= 0 and y < len(MAZE) and x < len(MAZE[y])

for y, row in enumerate(MAZE):
    for x, char in enumerate(row):
        if is_letter(char):
            letters = char
            position = None
            hor = [y, x + 1]
            vert = [y + 1, x]
            if in_bounds(hor[0], hor[1]) and is_letter(MAZE[hor[0]][hor[1]]):
                letters += MAZE[hor[0]][hor[1]]
                for cand in [[y, x + 2],[y, x - 1]]:
                    if in_bounds(cand[0], cand[1]) and MAZE[cand[0]][cand[1]] == '.':
                        position = cand
            elif in_bounds(vert[0], vert[1]) and is_letter(MAZE[vert[0]][vert[1]]):
                letters += MAZE[vert[0]][vert[1]]
                for cand in [[y + 2, x],[y - 1, x]]:
                    if in_bounds(cand[0], cand[1]) and MAZE[cand[0]][cand[1]] == '.':
                        position = cand
                if not position:
                    print('nopos', letters, y, x, MAZE[y][x])
            if len(letters) == 2:
                if letters not in PORTALS:
                    PORTALS[letters] = []
                PORTALS[letters].append(position)
                if letters not in ['AA','ZZ']:
                    REVERSE_PORTALS[str(position)] = letters

START = PORTALS['AA'][0]
END = PORTALS['ZZ'][0]

MOVES = []
heapq.heapify(MOVES)

heapq.heappush(MOVES, (0, 0, 0, START.copy()))

DIRECTIONS = [
    [0, 1],[1, 0],[0, -1],[-1, 0]
]

def is_outer(pos):
    return pos[0] == 2 or pos[0] == len(MAZE) - 3 or pos[1] == 2 or pos[1] == len(MAZE[pos[0]]) - 3 

while len(MOVES) > 0:
    num_moves, _, level, next = heapq.heappop(MOVES)
    if next == END and level == 0:
        print('part b', num_moves)
        break

    key = str(next)
    if key in REVERSE_PORTALS and (not is_outer(next) or level > 0):
        letters = REVERSE_PORTALS[key]
        options = PORTALS[letters]
        if is_outer(next):
            level -= 1
        else:
            level += 1
        poss_next = options[0]
        if next == poss_next:
            poss_next = options[1]
        next = poss_next
        key = str(next)
        num_moves += 1
    cache_key = key + str(level)
    if cache_key not in VISITED:
        VISITED[cache_key] = True
        for dir in DIRECTIONS:
                new_move = [next[0] + dir[0], next[1] + dir[1]]
                if in_bounds(new_move[0], new_move[1]) and MAZE[new_move[0]][new_move[1]] == '.':
                    heapq.heappush(MOVES, (num_moves + 1, random.random(), level, new_move))