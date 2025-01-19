import heapq
import random
import math
ASTEROIDS = []
with open('day10_input.txt', 'r') as file:
    for i, line in enumerate(file):
        cells = list(line.strip())
        for j, cell in enumerate(cells):
            if cell == '#':
                ASTEROIDS.append([i, j])

def reduce(distance):
    gcd = math.gcd(distance[0], distance[1])
    return [math.trunc(distance[0] / gcd), math.trunc(distance[1] / gcd)]
    
def get_angle(next_dist):
    vec_1 = [-1, 0]
    dot = next_dist[0] * vec_1[0] + next_dist[1] * vec_1[1]
    mag_1 = math.sqrt(vec_1[0] ** 2 + vec_1[1] ** 2)
    mag_2 = math.sqrt(next_dist[0] ** 2 + next_dist[1] ** 2)
    angle = math.acos(dot/(mag_1 * mag_2)) * (180 / math.pi)
    if next_dist[1] < 0:
        angle = 360 - angle
    return angle

max_coords = None
max_asteroids = 0
max_angles = None
for asteroid in ASTEROIDS:
    within_sight = []
    distances = []
    angles = {}
    angles2 = {}
    heapq.heapify(distances)
    for other_asteroid in ASTEROIDS:
        y_dist = other_asteroid[0] - asteroid[0]
        x_dist = other_asteroid[1] - asteroid[1]
        distance = abs(x_dist) + abs(y_dist)
        if distance > 0:
            heapq.heappush(distances, (distance, random.random(), [y_dist, x_dist], other_asteroid))
    
    while len(distances) > 0:
        _, _, next_dist, next_coords = heapq.heappop(distances)
        next_dist = reduce(next_dist)
        angle = round(get_angle(next_dist), 2)
        if next_dist not in within_sight:
            angles[angle] = [next_coords]
            within_sight.append(next_dist)
        else:
            angles[angle].append(next_coords)
    vis_asteroids = len(within_sight)
    if vis_asteroids > max_asteroids:
        max_asteroids = vis_asteroids
        max_coords = asteroid
        max_angles = angles

print('coords', max_coords)
print('part a:', max_asteroids)

def dist(origin, coord):
    return [coord[0] - origin[0], coord[1] - origin[1]]

ordering = []
finished = False
num_to_return = 200
while not finished:
    keys = list(max_angles.keys())
    keys.sort()
    for key in keys:
        if len(max_angles[key]) > 0:
            ordering.append(max_angles[key].pop(0))
            if len(max_angles[key]) == 0:
                del max_angles[key]
            if len(ordering) == num_to_return:
                num_200 = ordering[num_to_return - 1]
                print('part b:', num_200[1] * 100 + num_200[0])
                finished = True
                break