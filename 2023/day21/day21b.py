import math
import copy
MAP = []
STARTING_POS = None
NUM_ROCKS = 0
with open('day21_input.txt', 'r') as file:
    for row_index, row in enumerate(file):
        row = list(row.strip())
        NUM_ROCKS += row.count('#')
        if 'S' in row:
            STARTING_POS = [row_index, row.index('S')]
        MAP.append(row)

MAP_HEIGHT = len(MAP)
MAP_WIDTH = len(MAP[0])
MAP_SIZE = MAP_HEIGHT * MAP_WIDTH
print('start', STARTING_POS)
print('height', MAP_HEIGHT)
print('width', MAP_WIDTH)
left_offset = STARTING_POS[1]
right_offset = MAP_WIDTH - STARTING_POS[1] - 1
top_offset = STARTING_POS[0]
bottom_offset = MAP_HEIGHT - STARTING_POS[0] - 1
print('map area', MAP_SIZE)
print('num_rocks', NUM_ROCKS)
total_plots = MAP_SIZE - NUM_ROCKS
print('total plots', total_plots)
ratio = (MAP_SIZE - NUM_ROCKS) / MAP_SIZE


def get_key(pos, num_left):
    return f"{pos},{num_left}"


def in_bounds(pos):
    return pos[0] >= 0 and pos[1] >= 0 and pos[0] < len(MAP) and pos[1] < len(MAP[0])


POSS_DIRS = [
    [0, 1], [0, -1], [1, 0], [-1, 0]
]


def visit_plots(state):
    curr_steps = state['num_steps']
    if 'last_steps' in state:
        last_steps = state['last_steps']

        delta = curr_steps - last_steps
        frontiers = state['frontiers']
        to_visit = []
        frontier_keys = list(frontiers.keys())
        for key in frontier_keys:
            row, col = key.split(',')
            to_visit.append(
                {'pos': [int(row), int(col)], 'num_left': delta, 'num_taken': 0, 'start': True})
    else:
        to_visit = [{'pos': state['pos'],
                     'num_left': state['num_steps'], 'num_taken': 0}]
    state['last_steps'] = curr_steps
    state['frontiers'] = {}
    while len(to_visit) > 0:
        next = to_visit.pop(0)
        pos = next['pos']
        num_left = next['num_left']
        num_taken = next['num_taken']
        key = f"{pos[0]},{pos[1]}"
        if key not in state['visited'] or 'start' in next:
            if (num_taken % 2) == state['mod'] and 'start' not in next:
                state['stopped'][key] = True
                state['unique'] += 1
            state['visited'][key] = True

            if num_left == 0:
                state['frontiers'][key] = True
            if num_left > 0:
                for dir in POSS_DIRS:
                    new_loc = [pos[0] + dir[0], pos[1] + dir[1]]
                    if (state['ignore_bounds'] or in_bounds(new_loc)) and (state['ignore_rocks'] or (MAP[new_loc[0] % len(MAP)][new_loc[1] % len(MAP[0])] != '#')) and str(new_loc) not in state['visited']:
                        to_visit.append(
                            {'pos': new_loc, 'num_left': num_left - 1, 'num_taken': num_taken + 1})


def is_rock(loc):
    return MAP[loc[0] % len(MAP)][loc[1] % len(MAP[0])] == '#'


def test_frontier(num_steps):
    rocks = {True: 0, False: 0}
    loc = [STARTING_POS[0] + num_steps, STARTING_POS[1]]
    print(loc)
    print(loc[0] % len(MAP), loc[1] % len(MAP[0]))
    while loc[0] > STARTING_POS[0]:
        rock = is_rock(loc)
        rocks[rock] += 1
        loc = [loc[0] - 1, loc[1] + 1]
    loc = [STARTING_POS[0] - num_steps, STARTING_POS[1]]
    while loc[0] < STARTING_POS[0]:
        rock = is_rock(loc)
        rocks[rock] += 1
        loc = [loc[0] + 1, loc[1] - 1]
    loc = [STARTING_POS[0], STARTING_POS[1] + num_steps]
    while loc[1] > STARTING_POS[0]:
        rock = is_rock(loc)
        rocks[rock] += 1
        loc = [loc[0] + 1, loc[1] - 1]
    loc = [STARTING_POS[0], STARTING_POS[1] - num_steps]
    while loc[1] < STARTING_POS[0]:
        rock = is_rock(loc)
        rocks[rock] += 1
        loc = [loc[0] - 1, loc[1] + 1]
    return rocks


def print_map(state):
    map = copy.deepcopy(MAP)
    for key in list(state['stopped'].keys()):
        row, col = key.split(',')
        map[int(row)][int(col)] = 'O'
    for row in map:
        print(''.join(row))


def get_dists(state):
    dists = {}
    frontiers_keys = list(state['frontiers'].keys())
    for frontier in frontiers_keys:
        row, col = [int(num) for num in frontier.split(',')]
        dist = abs(row - STARTING_POS[0]) + abs(col - STARTING_POS[1])
        if dist not in dists:
            dists[dist] = 1
        else:
            dists[dist] += 1
    dist_keys = list(dists.keys())
    num_keys = len(frontiers_keys)
    dist_keys.sort()
    num_steps = state['num_steps']
    print('tot:', len(frontiers_keys))
    print('----')
    for dist in dist_keys:
        print(dist, ':', dists[dist])
    print('----')


def limit_map(map, dist=None):
    squares = 0
    for row in range(MAP_HEIGHT):
        for col in range(MAP_WIDTH):
            offset = abs(row - STARTING_POS[0]) + abs(col - STARTING_POS[1])
            if (not dist or offset <= dist) and f"{row},{col}" in map:
                squares += 1
    return squares


def get_TL(map, dist):
    squares = 0
    for row in range(MAP_HEIGHT):
        for col in range(MAP_WIDTH):
            offset = abs(row - STARTING_POS[0]) + abs(col - STARTING_POS[1])
            if offset > dist and f"{row},{col}" in map and row < STARTING_POS[0] and col < STARTING_POS[0]:
                squares += 1
    return squares


def get_BL(map, dist):
    squares = 0
    for row in range(MAP_HEIGHT):
        for col in range(MAP_WIDTH):
            offset = abs(row - STARTING_POS[0]) + abs(col - STARTING_POS[1])
            if offset > dist and f"{row},{col}" in map and row > STARTING_POS[0] and col < STARTING_POS[0]:
                squares += 1
    return squares


def get_TR(map, dist):
    squares = 0
    for row in range(MAP_HEIGHT):
        for col in range(MAP_WIDTH):
            offset = abs(row - STARTING_POS[0]) + abs(col - STARTING_POS[1])
            if offset > dist and f"{row},{col}" in map and row < STARTING_POS[0] and col > STARTING_POS[0]:
                squares += 1
    return squares


def get_BR(map, dist):
    squares = 0
    for row in range(MAP_HEIGHT):
        for col in range(MAP_WIDTH):
            offset = abs(row - STARTING_POS[0]) + abs(col - STARTING_POS[1])
            if offset > dist and f"{row},{col}" in map and row > STARTING_POS[0] and col > STARTING_POS[0]:
                squares += 1
    return squares


def get_est(reps, odd, even, checker_1, checker_2):
    n_squared = reps ** 2
    n_plus_one_squared = (reps + 1) ** 2
    coeff_3 = ((reps * 2 + 1) ** 2 - n_squared - n_plus_one_squared) / 2
    if reps % 2 == 0:
        return even * n_squared + odd * n_plus_one_squared + coeff_3 * (checker_1 + checker_2)
    else:
        return odd * n_squared + even * n_plus_one_squared + coeff_3 * (checker_1 + checker_2)


last = 1
odd_state = {'visited': {}, 'unique': 0, 'stopped': {}, 'pos': STARTING_POS,
             'ignore_rocks': False, 'ignore_bounds': False, 'num_steps': 131, 'mod': 131 % 2}
visit_plots(odd_state)
even_state = {'visited': {}, 'unique': 0, 'stopped': {}, 'pos': STARTING_POS,
              'ignore_rocks': False, 'ignore_bounds': False, 'num_steps': 130, 'mod': 130 % 2}
visit_plots(even_state)
state = {'visited': {}, 'unique': 0, 'stopped': {}, 'pos': STARTING_POS,
         'ignore_rocks': False, 'ignore_bounds': True}
state['num_steps'] = 65
state['mod'] = 65 % 2
visit_plots(state)
unique_65 = state['unique']
even = limit_map(even_state['stopped'])
odd = limit_map(odd_state['stopped'])
print('all visited', even + odd)
even_65 = limit_map(even_state['stopped'], 65)
odd_65 = limit_map(odd_state['stopped'], 65)
checker_1 = get_TL(odd_state['stopped'], 65) + get_BR(odd_state['stopped'], 65) + \
    get_TR(even_state['stopped'], 65) + get_BL(even_state['stopped'], 65)
checker_2 = get_TL(even_state['stopped'], 65) + get_BR(even_state['stopped'], 65) + \
    get_TR(odd_state['stopped'], 65) + get_BL(odd_state['stopped'], 65)
odd_corners = get_TL(odd_state['stopped'], 65) + get_BR(odd_state['stopped'], 65) + \
    get_TR(odd_state['stopped'], 65) + get_BL(odd_state['stopped'], 65)
even_corners = get_TL(even_state['stopped'], 65) + get_BR(even_state['stopped'], 65) + \
    get_TR(even_state['stopped'], 65) + get_BL(even_state['stopped'], 65)
for i in [26501365]:
    # num_steps = 65 + (i + 1) * 131
    num_steps = i
    mod = num_steps % 2
    num_reps = round((num_steps - 65) / 131)
    print('reps', num_reps)
    state['num_steps'] = num_steps
    state['mod'] = mod
    # This is commented out because we are going to use the estimate
    # visit_plots(state)
    est = get_est(num_reps, odd_65, even_65, checker_1, checker_2)
    # print(num_steps, state['unique'], est, est - state['unique'])
    print(num_steps, est)
    last = state['unique']
