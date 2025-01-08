import sympy
from sympy.abc import a, b, c, d, e, f, g, h, i
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

stone1 = STONES[0]
stone2 = STONES[1]
stone3 = STONES[2]

# With 3 stones, we have 9 equations with 9 unknowns
t1a = (stone1['pos']['x'] - a) / (d - stone1['vel']['x']) - g
t1b = (stone1['pos']['y'] - b) / (e - stone1['vel']['y']) - g
t1c = (stone1['pos']['z'] - c) / (f - stone1['vel']['z']) - g
t2a = (stone2['pos']['x'] - a) / (d - stone2['vel']['x']) - h
t2b = (stone2['pos']['y'] - b) / (e - stone2['vel']['y']) - h
t2c = (stone2['pos']['z'] - c) / (f - stone2['vel']['z']) - h
t3a = (stone3['pos']['x'] - a) / (d - stone3['vel']['x']) - i
t3b = (stone3['pos']['y'] - b) / (e - stone3['vel']['y']) - i
t3c = (stone3['pos']['z'] - c) / (f - stone3['vel']['z']) - i
# Use SYMPY to solve
results = sympy.solve([t1a, t1b, t1c, t2a, t2b,
                       t2c, t3a, t3b, t3c])[0]
# a, b, and c are the positions
print(results[a] + results[b] + results[c])
