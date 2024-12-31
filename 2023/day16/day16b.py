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


def print_map(input):
    for line in input:
        print(''.join(line))


def run_puzzle(position, direction):
    ENERGIZED_TILES = {str(position): True}
    BEAMS = [{'direction': direction, 'position': position}]
    PREV_BEAMS = {str(BEAMS[0]): True}
    # Repeat while there are still beams to move
    while len(BEAMS) > 0:
        # Go through the beams 1 at a time, and figure out any effects (reflection, splitting)
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
        # Figure out the next position for each beam
        index = 0
        while index < len(BEAMS):
            beam = BEAMS[index]
            position = beam['position']
            motion = directions[beam['direction']]
            new_position = [position[0] + motion[0], position[1] + motion[1]]
            # If the beam moves off the map, we can remove it
            if new_position[0] < 0 or new_position[0] >= len(map) or new_position[1] < 0 or new_position[1] >= len(map[0]):
                BEAMS.pop(index)
            else:
                beam['position'] = new_position
                if str(new_position) not in ENERGIZED_TILES:
                    ENERGIZED_TILES[str(new_position)] = True
                index += 1
        # Figure out whether a beam has been in the same position/direction before (in which case it isn't needed)
        index = 0
        while index < len(BEAMS):
            beam = BEAMS[index]
            if str(beam) in PREV_BEAMS:
                BEAMS.pop(index)
            else:
                PREV_BEAMS[str(beam)] = True
                index += 1
    # When we are finished, return the number of energized tiles
    return len(list(ENERGIZED_TILES.keys()))


max_energized = None
# Run though each edge, determining the energy of the state
for i in range(len(map[0])):
    curr_energized = run_puzzle([0, i], 3)
    if not max_energized or curr_energized > max_energized:
        max_energized = curr_energized
    curr_energized = run_puzzle([len(map) - 1, i], 4)
    if not max_energized or curr_energized > max_energized:
        max_energized = curr_energized
for i in range(len(map)):
    curr_energized = run_puzzle([i, 0], 1)
    if not max_energized or curr_energized > max_energized:
        max_energized = curr_energized
    curr_energized = run_puzzle([i, len(map[0]) - 1], 2)
    if not max_energized or curr_energized > max_energized:
        max_energized = curr_energized

# Show the highest energized state
print(max_energized)
