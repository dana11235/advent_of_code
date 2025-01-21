import heapq
import random
import copy
MAP = []
START_POS = None

DIRECTIONS = [
    [0, 1],
    [0, -1],
    [1, 0],
    [-1, 0]
]
NEW_STARTS = [
    [1,1],
    [-1,1],
    [1,-1],
    [-1,-1],
]
START_POSES = []

KEYS = []
KEY_POSITIONS = {}
DOORS = []

# This file is a back-ported version with the multi-robot logic (it isn't significantly different in speed from the single-robot version)
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

# Now generate the split map
SPLIT_MAP = copy.deepcopy(MAP)
SPLIT_MAP[START_POS[0]][START_POS[1]] = '#'
for dir in DIRECTIONS:
    pos = [START_POS[0] + dir[0], START_POS[1] + dir[1]]
    SPLIT_MAP[pos[0]][pos[1]] = '#'
for new_start in NEW_STARTS:
    start_pos = [START_POS[0] + new_start[0], START_POS[1] + new_start[1]]
    SPLIT_MAP[start_pos[0]][start_pos[1]] = '@'
    START_POSES.append(start_pos)


def print_map(map):
    for row in map:
        print(''.join(row))
print('starts', START_POSES)
# print_map(SPLIT_MAP)
MAP = SPLIT_MAP

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
            obsolete = is_subset(keys, obj_keys) and num_steps > obj_steps
            # The above line works for the full input.
            # This line below makes this return strictly the right answer, but it's slow. Need to work on the memoization.
            # obsolete = is_subset(keys, obj_keys) and obj_keys[:len(keys)] == keys and num_steps > obj_steps
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

def get_valid_moves(pos, keys):
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
heapq.heappush(MOVES, (0, 0, 0, random.random(), [], copy.deepcopy(START_POSES)))

def closest_key_dist(moves, keys):
    dist = None
    for move in moves:
        for key in KEY_POSITIONS.keys():
            if key not in keys:
                key_pos = KEY_POSITIONS[key]
                curr_dist = abs(move[0] - key_pos[0]) + abs(move[1] - key_pos[1])
                if not dist or curr_dist < dist:
                    dist = curr_dist
    return dist

def total_key_dist(moves, keys):
    dist = 0
    for move in moves:
        for key in KEY_POSITIONS.keys():
            if key not in keys:
                key_pos = KEY_POSITIONS[key]
                curr_dist = abs(move[0] - key_pos[0]) + abs(move[1] - key_pos[1])
                dist += curr_dist
    return dist

def enqueue(num_steps, keys, moves):
    heapq.heappush(MOVES, (num_steps + 1, 26 - len(keys), closest_key_dist(moves, keys), random.random(), keys.copy(), moves))

while len(MOVES) > 0:
    num_steps, _, _, _, keys, poses = heapq.heappop(MOVES)
    if num_steps > counts['steps']:
        print('steps', num_steps)
        counts['steps'] = num_steps

    # If we have all the keys, we are done
    if len(keys) == len(KEYS):
        print('num moves',num_steps)
        break

    for i, pos in enumerate(poses):
        if not is_obsolete(pos, num_steps, keys):
            cache_key = str(pos)
            if cache_key not in VISITED:
                VISITED[cache_key] = []
            VISITED[cache_key].append({'num_steps': num_steps, 'keys': keys})
            valid_moves = get_valid_moves(pos, keys)
            for valid_move in valid_moves:
                new_keys = keys.copy()
                detect_key(valid_move, new_keys)
                if not is_obsolete(valid_move, num_steps + 1, new_keys):
                    new_poses = copy.deepcopy(poses)
                    new_poses[i] = valid_move
                    enqueue(num_steps, new_keys, new_poses)