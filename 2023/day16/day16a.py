import copy
directions = {
    1: [0, 1],
    2: [0, -1],
    3: [1, 0],
    4: [-1, 0]
}
map = []
with open('day16_input.txt', 'r') as file:
    for line in file:
        map.append(list(line.strip()))
BEAMS = [{'direction': 1, 'position': [0, 0]}]
ENERGIZED_TILES = [[0, 0]]
PREV_BEAMS = [copy.deepcopy(BEAMS[0])]


def print_map(input):
    for line in input:
        print(''.join(line))


while len(BEAMS) > 0:
    index = 0
    while index < len(BEAMS):
        beam = BEAMS[index]
        position = beam['position']
        tile = map[position[0]][position[1]]
        if tile == '/':
            if beam['direction'] == 4:
                beam['direction'] = 1
            elif beam['direction'] == 3:
                beam['direction'] = 2
            elif beam['direction'] == 2:
                beam['direction'] = 3
            elif beam['direction'] == 1:
                beam['direction'] = 4
        elif tile == '\\':
            if beam['direction'] == 4:
                beam['direction'] = 2
            elif beam['direction'] == 3:
                beam['direction'] = 1
            elif beam['direction'] == 2:
                beam['direction'] = 4
            elif beam['direction'] == 1:
                beam['direction'] = 3
        elif tile == '|' and beam['direction'] in [1, 2]:
            beam['direction'] = 3
            second_beam = copy.deepcopy(beam)
            second_beam['direction'] = 4
            BEAMS.insert(index + 1, second_beam)
            index += 1
        elif tile == '-' and beam['direction'] in [3, 4]:
            beam['direction'] = 1
            second_beam = copy.deepcopy(beam)
            second_beam['direction'] = 2
            BEAMS.insert(index + 1, second_beam)
            index += 1
        index += 1
    index = 0
    while index < len(BEAMS):
        beam = BEAMS[index]
        position = beam['position']
        motion = directions[beam['direction']]
        new_position = [position[0] + motion[0], position[1] + motion[1]]
        if new_position[0] < 0 or new_position[0] >= len(map) or new_position[1] < 0 or new_position[1] >= len(map[0]):
            BEAMS.pop(index)
        else:
            beam['position'] = new_position
            if new_position not in ENERGIZED_TILES:
                ENERGIZED_TILES.append(new_position)
            index += 1
    index = 0
    while index < len(BEAMS):
        beam = BEAMS[index]
        if beam in PREV_BEAMS:
            BEAMS.pop(index)
        else:
            PREV_BEAMS.append(copy.deepcopy(beam))
            index += 1


for tile in ENERGIZED_TILES:
    map[tile[0]][tile[1]] = '#'

print(len(ENERGIZED_TILES))
