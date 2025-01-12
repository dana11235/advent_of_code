WIRE_COORDS = []
DIRECTIONS = {
    'U': [-1, 0],
    'D': [1, 0],
    'L': [0, -1],
    'R': [0, 1]
}
with open('day3_input.txt', 'r') as file:
    for line in file:
        line = line.strip()
        moves = line.split(',')
        coordinates = [0, 0]
        move_coords = []
        for move in moves:
            direction = move[0]
            number = int(move[1:])
            new_coordinates = [coordinates[0] + number * DIRECTIONS[direction]
                               [0], coordinates[1] + number * DIRECTIONS[direction][1]]
            move_coords.append(
                {'dir': direction, 'from': coordinates, 'to': new_coordinates})
            coordinates = new_coordinates
        WIRE_COORDS.append(move_coords)

closest_dist = None

for i in range(len(WIRE_COORDS[0])):
    for j in range(len(WIRE_COORDS[1])):
        first_segment = WIRE_COORDS[0][i]
        second_segment = WIRE_COORDS[1][j]
        if first_segment['dir'] in ['U', 'D'] and second_segment['dir'] in ['L', 'R'] and first_segment['from'] != [0, 0]:
            first_x = first_segment['from'][1]
            second_x = [second_segment['from'][1], second_segment['to'][1]]
            second_x.sort()
            first_y = [first_segment['from'][0], first_segment['to'][0]]
            first_y.sort()
            second_y = second_segment['from'][0]
            if (first_x >= second_x[0] and first_x <= second_x[1]) and (second_y >= first_y[0] and second_y <= first_y[1]):
                intersection = [second_y, first_x]
                dist = abs(intersection[0]) + abs(intersection[1])
                if not closest_dist or closest_dist > dist:
                    closest_dist = dist
        elif second_segment['dir'] in ['U', 'D'] and first_segment['dir'] in ['L', 'R'] and first_segment['from'] != [0, 0]:
            first_x = [first_segment['from'][1], first_segment['to'][1]]
            first_x.sort()
            second_x = second_segment['from'][1]
            second_y = [second_segment['from'][0], second_segment['to'][0]]
            second_y.sort()
            first_y = first_segment['from'][0]
            if (second_x >= first_x[0] and second_x <= first_x[1]) and (first_y >= second_y[0] and first_y <= second_y[1]):
                intersection = [first_y, second_x]
                dist = abs(intersection[0]) + abs(intersection[1])
                if not closest_dist or closest_dist > dist:
                    closest_dist = dist
print('closest dist', closest_dist)
