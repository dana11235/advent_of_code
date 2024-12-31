import heapq
import random
import copy
directions = [
    [0, 1],
    [1, 0],
    [0, -1],
    [-1, 0]
]

MAP = []

with open('day17_input.txt', 'r') as file:
    for line in file:
        line = line.strip()
        MAP.append(list(line))

START_POSITION = [0, 0]
END_POSITION = [len(MAP) - 1, len(MAP[0]) - 1]

MOVES = []
heapq.heapify(MOVES)


def add_move(move):
    # I need to add a small random number to enable the sorting to be stable
    heapq.heappush(
        MOVES, (move['cost'] + (0.01 * random.random()), move))


def get_next_move():
    return heapq.heappop(MOVES)[1]


def has_reached_goal(position):
    return position[0] == END_POSITION[0] and position[1] == END_POSITION[1]


def in_bounds(position):
    return position[0] >= 0 and position[1] >= 0 and position[0] < len(MAP) and position[1] < len(MAP[0])


def get_key(position, direction, num_moves):
    return f"{position[0]},{position[1]},{direction},{num_moves}"


def parse_key(key):
    return [int(v) for v in key.split(',')]


GLOBAL_VISITED = {}


def maybe_add_move_in_dir(direction, last_move, reset):
    curr_pos = last_move['position']
    curr_cost = last_move['cost']
    dir_move = directions[direction]
    dir_position = [curr_pos[0] + dir_move[0], curr_pos[1] + dir_move[1]]
    num_moves = last_move['num_moves'] + 1
    if reset:
        num_moves = 1

    if in_bounds(dir_position):
        dir_key = get_key(dir_position, direction, num_moves)
        new_cost = curr_cost + int(MAP[dir_position[0]][dir_position[1]])
        min_cost = 100000000
        if dir_key in GLOBAL_VISITED:
            min_cost = GLOBAL_VISITED[dir_key]
        if new_cost < min_cost:
            GLOBAL_VISITED[dir_key] = new_cost
            visited = copy.deepcopy(next_move['visited'])
            visited[dir_key] = True
            add_move({'position': dir_position, 'direction': direction,
                      'cost': new_cost,
                      'num_moves': num_moves, 'visited': visited})


def mark_map(move):
    for key in list(move['visited'].keys()):
        visit = parse_key(key)
        char = '>'
        if visit[2] == 1:
            char = 'v'
        elif visit[2] == 2:
            char = '<'
        elif visit[2] == 3:
            char = '^'
        MAP[visit[0]][visit[1]] = char
    for line in MAP:
        print(''.join(line))


def print_next_5():
    for item in MOVES[0:5]:
        item = item[1]
        print(item['position'], item['cost'])


add_move({'position': START_POSITION, 'direction': 0, 'num_moves': 0,
         'cost': 0, 'visited': {get_key(START_POSITION, 0, 0): True}})
count = 0
while True:
    count += 1
    next_move = get_next_move()
    if has_reached_goal(next_move['position']):
        print('count', count)
        print('cost', next_move['cost'])
        mark_map(next_move)
        break
    else:
        if next_move['num_moves'] < 3:
            maybe_add_move_in_dir(next_move['direction'], next_move, False)
        left_dir = (next_move['direction'] - 1) % 4
        maybe_add_move_in_dir(left_dir, next_move, True)
        right_dir = (next_move['direction'] + 1) % 4
        maybe_add_move_in_dir(right_dir, next_move, True)
