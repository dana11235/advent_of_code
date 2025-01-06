MAP = []
STARTING_POS = None
with open('day21_input.txt', 'r') as file:
    for row_index, row in enumerate(file):
        row = list(row.strip())
        if 'S' in row:
            STARTING_POS = [row_index, row.index('S')]
        MAP.append(row)


def in_bounds(pos):
    return pos[0] >= 0 and pos[1] >= 0 and pos[0] < len(MAP) and pos[1] < len(MAP[0])


POSS_DIRS = [
    [0, 1], [0, -1], [1, 0], [-1, 0]
]


def visit_plots(state):
    # This was highly optimized when building part b
    curr_steps = state['num_steps']
    if 'last_steps' in state:
        last_steps = state['last_steps']

        delta = curr_steps - last_steps
        frontiers = state['frontiers']
        to_visit = []
        frontier_keys = list(frontiers.keys())
        # This allows us to run this iteratively, using the previous output as intermediate state
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
            # If the number of steps has the right mod, it will be stopped at eventually, so se can stop processing it now
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


state = {'visited': {}, 'unique': 0, 'stopped': {}, 'pos': STARTING_POS,
         'ignore_rocks': False, 'ignore_bounds': False, 'num_steps': 64, 'mod': 64 % 2}

visit_plots(state)
print('num_combinations', state['unique'])
