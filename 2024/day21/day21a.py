CODES = []
LEVEL1 = []
LEVEL2 = []
LEVEL3 = {}
ALPHA = {
    '7': [0, 0],
    '8': [0, 1],
    '9': [0, 2],
    '4': [1, 0],
    '5': [1, 1],
    '6': [1, 2],
    '1': [2, 0],
    '2': [2, 1],
    '3': [2, 2],
    '0': [3, 1],
    'A': [3, 2],
}
DIRECTIONS = {
    '^': [0, 1],
    'A': [0, 2],
    '<': [1, 0],
    'v': [1, 1],
    '>': [1, 2],

}
with open('day21_input.txt', 'r') as file:
    for line in file:
        CODES.append(list(line.strip()))


def move(number, direction, instructions):
    for i in range(number):
        instructions.append(direction)


def move_vertical(number, instructions):
    if number > 0:
        move(number, 'v', instructions)
    elif number < 0:
        move(-number, '^', instructions)
    # We don't move if the number == 0


def move_horizontal(number, instructions):
    if number > 0:
        move(number, '>', instructions)
    elif number < 0:
        move(-number, '<', instructions)
    # We don't move if the number == 0


def calc_diff(pos1, pos2):
    return [pos1[0] - pos2[0], pos1[1] - pos2[1]]


def translate(start_pos, codex, input):
    output = []
    position = start_pos
    for code in input:
        instructions = []
        for symbol in code:
            direction = ALPHA[symbol]
            diff = calc_diff(direction, position)
            # This keeps the robot from aiming at a gap
            if codex == ALPHA:
                if position[0] == 3 and direction[1] == 0:
                    move_combos(diff, instructions, 'v')
                elif position[1] == 0 and direction[0] == 3:
                    move_combos(diff, instructions, 'h')
                else:
                    move_combos(diff, instructions)
            elif codex == DIRECTIONS:
                if position[0] == 1 and position[1] == 0 and direction[0] == 0:
                    move_combos(diff, instructions, 'h')
                elif direction[0] == 1 and direction[1] == 0 and position[0] == 0:
                    move_combos(diff, instructions, 'v')
                else:
                    move_combos(diff, instructions)

            instructions.append('A')
            position = direction
        output.append(instructions)
    return output


MOVE_CACHE = {}


def generate_all_combos(horizontal_move, horizontal_count, vertical_move, vertical_count):
    key = f"{horizontal_move},{horizontal_count},{
        vertical_move},{vertical_count}"
    if key in MOVE_CACHE:
        return MOVE_CACHE[key]
    combos = []
    if vertical_count == 0 and horizontal_count != 0:
        combo = []
        for _ in range(horizontal_count):
            combo += [horizontal_move]
        combos.append(combo)
    elif horizontal_count == 0 and vertical_count != 0:
        combo = []
        for _ in range(vertical_count):
            combo += [vertical_move]
        combos.append(combo)
    else:
        for combo in generate_all_combos(horizontal_move, horizontal_count, vertical_move, vertical_count - 1):
            combos.append([vertical_move] + combo)
        for combo in generate_all_combos(horizontal_move, horizontal_count - 1, vertical_move, vertical_count):
            combos.append([horizontal_move] + combo)
    MOVE_CACHE[key] = combos
    return combos


def move_combos(diff, combos, first=None):
    all_combos = []
    prefix = []
    horizontal_move = '>'
    if diff[1] < 0:
        horizontal_move = '<'
    vertical_move = 'v'
    if diff[0] < 0:
        vertical_move = '^'
    horizontal_count = abs(diff[1])
    vertical_count = abs(diff[0])
    if first == 'h':
        prefix.append(horizontal_move)
        horizontal_count -= 1
    elif first == 'v':
        prefix.append(vertical_move)
        vertical_count -= 1
    for combo in generate_all_combos(horizontal_move, horizontal_count, vertical_move, vertical_count):
        all_combos.append(prefix + combo + ['A'])
    return all_combos


def get_alpha_combos(word):
    combos = []
    position = [3, 2]
    for letter in word:
        destination = ALPHA[letter]
        diff = calc_diff(destination, position)
        if position[0] == 3 and destination[1] == 0:
            letter_combos = move_combos(diff, combos, 'v')
        elif position[1] == 0 and destination[0] == 3:
            letter_combos = move_combos(diff, combos, 'h')
        else:
            letter_combos = move_combos(diff, combos)
        combos.append(letter_combos)
        position = destination
    return enumerate_all(combos)


def enumerate_all(combos):
    output_combos = []
    if len(combos) == 0:
        return output_combos
    for combo in combos[0]:
        children = combos[1:]
        if len(children) == 0:
            output_combos.append(combo)
        else:
            child_combos = enumerate_all(children)
            for child_combo in child_combos:
                output_combos.append(combo + child_combo)
    return output_combos


def get_direction_combos(combos):
    output_combos = []
    for combo in combos:
        letter_combo_combos = []
        position = [0, 2]
        for letter in combo:
            letter_combos = []
            direction = DIRECTIONS[letter]
            diff = calc_diff(direction, position)
            if position[0] == 1 and position[1] == 0 and direction[0] == 0:
                letter_combos = move_combos(diff, letter_combos, 'h')
            elif direction[0] == 1 and direction[1] == 0 and position[0] == 0:
                letter_combos = move_combos(diff, letter_combos, 'v')
            else:
                letter_combos = move_combos(diff, letter_combos)
            letter_combo_combos.append(letter_combos)
            position = direction
        all_com = enumerate_all(letter_combo_combos)
        output_combos.append(all_com)
    return output_combos


def get_all_combos(letter):
    alpha_combos = get_alpha_combos(letter)
    print(letter, alpha_combos)
    direction_combos = get_direction_combos(alpha_combos)
    direction_combos = get_direction_combos(direction_combos[0])
    return direction_combos[0]


def generate_move(diff, first=None):
    output = []
    horizontal_move = '>'
    if diff[1] < 0:
        horizontal_move = '<'
    vertical_move = 'v'
    if diff[0] < 0:
        vertical_move = '^'
    horizontal_count = abs(diff[1])
    vertical_count = abs(diff[0])
    if first == 'h':
        output.append(horizontal_move)
        horizontal_count -= 1
    elif first == 'v':
        output.append(vertical_move)
        vertical_count -= 1
    for _ in range(horizontal_count):
        output.append(horizontal_move)
    for _ in range(vertical_count):
        output.append(vertical_move)
    output.append('A')
    return output


def convert_to_directions(combo):
    output_combo = []
    position = [0, 2]
    for letter in combo:
        destination = DIRECTIONS[letter]
        diff = calc_diff(destination, position)
        if position[0] == 1 and position[1] == 0 and destination[0] == 0:
            output_combo += generate_move(diff, 'h')
        elif destination[0] == 1 and destination[1] == 0 and position[0] == 0:
            output_combo += generate_move(diff, 'v')
        else:
            output_combo += generate_move(diff)
        position = destination
    return output_combo


LEVEL1_COMBOS = {}
for code in CODES:
    LEVEL1_COMBOS[''.join(code)] = get_alpha_combos(code)

LEVEL3_COMBOS = {}
for key in LEVEL1_COMBOS.keys():
    LEVEL3_COMBOS[key] = []
    for combo in LEVEL1_COMBOS[key]:
        LEVEL3_COMBOS[key].append(convert_to_directions(
            convert_to_directions(combo)))
    shortest_combo = None
    for combo in LEVEL3_COMBOS[key]:
        if not shortest_combo or len(combo) < len(shortest_combo):
            shortest_combo = combo
    LEVEL3[key] = shortest_combo

complexity = 0
for key in LEVEL3:
    complexity += (int(key[:-1]) * len(LEVEL3[key]))
print(complexity)
