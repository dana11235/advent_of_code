import itertools
import copy
import math
INITIAL_MOONS = []
with open('day12_input.txt', 'r') as file:
    for line in file:
        line = line.strip()
        line = line[1:-1]
        x, y, z = [char.strip() for char in line.split(',')]
        x = int(x.split('=')[1])
        y = int(y.split('=')[1])
        z = int(z.split('=')[1])
        INITIAL_MOONS.append({'pos': [x, y, z], 'vel': [0, 0, 0]})

def run_step(MOONS):
    for pair in itertools.combinations(MOONS, 2):
        if pair[0]['pos'][0] < pair[1]['pos'][0]:
            pair[0]['vel'][0] += 1
            pair[1]['vel'][0] -= 1
        elif pair[0]['pos'][0] > pair[1]['pos'][0]:
            pair[0]['vel'][0] -= 1
            pair[1]['vel'][0] += 1

        if pair[0]['pos'][1] < pair[1]['pos'][1]:
            pair[0]['vel'][1] += 1
            pair[1]['vel'][1] -= 1
        elif pair[0]['pos'][1] > pair[1]['pos'][1]:
            pair[0]['vel'][1] -= 1
            pair[1]['vel'][1] += 1

        if pair[0]['pos'][2] < pair[1]['pos'][2]:
            pair[0]['vel'][2] += 1
            pair[1]['vel'][2] -= 1
        elif pair[0]['pos'][2] > pair[1]['pos'][2]:
            pair[0]['vel'][2] -= 1
            pair[1]['vel'][2] += 1
    
    for moon in MOONS:
        moon['pos'][0] += moon['vel'][0]
        moon['pos'][1] += moon['vel'][1]
        moon['pos'][2] += moon['vel'][2]
        
MOONS = copy.deepcopy(INITIAL_MOONS)
for _ in range(1000):
    run_step(MOONS)

energy = 0
for moon in MOONS:
    pot = abs(moon['pos'][0]) + abs(moon['pos'][1]) + abs(moon['pos'][2])
    kin = abs(moon['vel'][0]) + abs(moon['vel'][1]) + abs(moon['vel'][2])
    energy += pot * kin

print('part a:', energy)

MOONS = copy.deepcopy(INITIAL_MOONS)
Xs = {}
Ys = {}
Zs = {}
x_repeated = None
y_repeated = None
z_repeated = None
for i in range(1000000):
    curr_x = []
    curr_y = []
    curr_z = []
    for moon in MOONS:
        curr_x.append(
            [ moon['vel'][0], moon['pos'][0] ]
        )
        curr_y.append(
            [ moon['vel'][1], moon['pos'][1] ]
        )
        curr_z.append(
            [ moon['vel'][2], moon['pos'][2] ]
        )
    
    # Since the 3 axes are independent, we can find the period separately
    if x_repeated is None:
        if str(curr_x) in Xs:
            x_repeated = i
        else:
            Xs[str(curr_x)] = i

    if y_repeated is None:
        if str(curr_y) in Ys:
            y_repeated = i
        else:
            Ys[str(curr_y)] = i

    if z_repeated is None:
        if str(curr_z) in Zs:
            z_repeated = i
        else:
            Zs[str(curr_z)] = i

    run_step(MOONS)

# Now find the LCM between the 3 periods
print('part b:', math.lcm(x_repeated, y_repeated, z_repeated))