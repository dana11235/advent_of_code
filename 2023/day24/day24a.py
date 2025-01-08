import numpy
STONES = []


def get_json(x, y, z):
    return {'x': x, 'y': y, 'z': z}


with open('day24_input.txt', 'r') as file:
    for line in file:
        line = line.strip()
        pos, vel = [part.strip() for part in line.split('@')]
        x_pos, y_pos, z_pos = [int(component.strip())
                               for component in pos.split(',')]
        x_vel, y_vel, z_vel = [int(component.strip())
                               for component in vel.split(',')]
        STONES.append({'pos': get_json(x_pos, y_pos, z_pos),
                      'vel': get_json(x_vel, y_vel, z_vel)})

MIN = 200000000000000
MAX = 400000000000000
# MIN = 7
# MAX = 27
crossing_stones = 0
prev_crossing_stones = 0
oor_stones = 0
combos = 0
for i, stone in enumerate(STONES):
    if i < len(STONES) - 1:
        for i2 in range(i + 1, len(STONES)):
            combos += 1
            stone2 = STONES[i2]
            a = stone['vel']['x']
            b = -1 * stone2['vel']['x']
            c = stone2['pos']['x'] - stone['pos']['x']
            d = stone['vel']['y']
            e = -1 * stone2['vel']['y']
            f = stone2['pos']['y'] - stone['pos']['y']
            denominator = (e - (d * b)/a)
            time1 = -1
            time2 = -1
            if denominator != 0:
                time2 = (f - (d * c)/a)/denominator
                time1 = c/a - b/a * time2
            if time1 >= 0 and time2 >= 0:
                x_coord = stone['pos']['x'] + \
                    time1 * stone['vel']['x']
                y_coord = stone['pos']['y'] + \
                    time1 * stone['vel']['y']
                if x_coord >= MIN and x_coord <= MAX and y_coord >= MIN and y_coord <= MAX:
                    crossing_stones += 1
                else:
                    oor_stones += 1
            else:
                prev_crossing_stones += 1


print('crossing stones', crossing_stones)
