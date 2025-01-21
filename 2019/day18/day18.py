import heapq
import random
MAP = []
START_POS = None

DIRECTIONS = [
    [0, 1],
    [0, -1],
    [1, 0],
    [-1, 0]
]
KEYS = []
KEY_POSITIONS = {}
DOORS = []

with open('day18_input.txt', 'r') as file:
    for y, line in enumerate(file):
        row = list(line.strip())
        for x, char in enumerate(row):
            if char == '@':
                START_POS = [y, x]
            if char not in ['#', '.', '@'] and char == char.lower() and char not in KEYS:
                KEYS.append(char)
                KEY_POSITIONS[char] = [y, x]
            if char not in ['#', '.', '@'] and char == char.upper() and char not in DOORS:
                DOORS.append(char)
        MAP.append(row)

def print_map(MAP):
    for row in MAP:
        print(''.join(row))

def is_subset(keys, obj_keys):
    obj_set = set(obj_keys)
    key_set = set(keys)
    # It's a subset if we don't have any keys that they don't have
    return len(key_set.difference(obj_set)) == 0

VISITED = {}
# {'keys': [], 'num_steps': n}
def is_obsolete(pos, num_steps, keys):
    cache_key = str(pos)
    if cache_key not in VISITED:
        return False
    else:
        objs = VISITED[cache_key]
        for obj in objs:
            obj_keys = obj['keys']
            obj_steps = obj['num_steps']
            obsolete = is_subset(keys, obj_keys) and num_steps >= obj_steps
            if obsolete:
                return True
        return False

def is_valid_move(new_pos, keys):
    char = MAP[new_pos[0]][new_pos[1]]
    # invalid if out of bounds or wall
    if new_pos[0] < 0 or new_pos[1] < 0 or new_pos[0] > len(MAP) - 1 or new_pos[1] > len(MAP[0]) - 1 or char == '#':
        return False
    # Valid if path, the starting point, or a key
    elif char in ['.', '@'] or char in KEYS:
        return True
    # Valid if it's a door we have the key for
    elif char in DOORS:
        return char.lower() in keys

counts = {'keys': 0, 'steps': 0}
# Figure out whether we picked up a key
def detect_key(pos, keys):
    char = MAP[pos[0]][pos[1]]
    if char in KEYS and char not in keys:
        keys.append(char)
        num_collected = len(keys)
        if num_collected > counts['keys']:
            print('got key', num_collected, keys)
            counts['keys'] = num_collected

def get_valid_moves(pos):
    moves = []
    for dir in DIRECTIONS:
        new_pos = [pos[0] + dir[0], pos[1] + dir[1]]
        if is_valid_move(new_pos, keys):
            moves.append(new_pos)
    return moves

print_map(MAP)
KEYS.sort()
DOORS.sort()
print('keys', KEYS)
print('doors', DOORS)
print(KEY_POSITIONS)

MOVES = []
heapq.heapify(MOVES)
heapq.heappush(MOVES, (0, 0, 0, random.random(), [], START_POS.copy()))

def closest_key_dist(move, keys):
    dist = None
    for key in KEY_POSITIONS.keys():
        if key not in keys:
            key_pos = KEY_POSITIONS[key]
            curr_dist = abs(move[0] - key_pos[0]) + abs(move[1] - key_pos[1])
            if not dist or curr_dist < dist:
                dist = curr_dist
    return dist

def total_key_dist(move, keys):
    dist = 0
    for key in KEY_POSITIONS.keys():
        if key not in keys:
            key_pos = KEY_POSITIONS[key]
            curr_dist = abs(move[0] - key_pos[0]) + abs(move[1] - key_pos[1])
            dist += curr_dist
    return dist

def enqueue(num_steps, keys, move):
    heapq.heappush(MOVES, (num_steps + 1, 26 - len(keys), total_key_dist(move, keys), random.random(), keys.copy(), move))

while len(MOVES) > 0:
    num_steps, _, _, _, keys, pos = heapq.heappop(MOVES)
    if num_steps > counts['steps']:
        print('steps', num_steps)
        counts['steps'] = num_steps
    detect_key(pos, keys)

    # If we have all the keys, we are done
    if len(keys) == len(KEYS):
        print('num moves',num_steps)
        break
    if not is_obsolete(pos, num_steps, keys):
        cache_key = str(pos)
        if cache_key not in VISITED:
            VISITED[cache_key] = []
        VISITED[cache_key].append({'num_steps': num_steps, 'keys': keys})
        valid_moves = get_valid_moves(pos)
        for valid_move in valid_moves:
            enqueue(num_steps, keys.copy(), valid_move)