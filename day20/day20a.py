MAZE = []
START_POSITION = None
END_POSITION = None
DIRECTIONS = [[0, 1], [1, 0], [0, -1], [-1, 0]]
CHEATS = [[0, 2], [2, 0], [0, -2], [-2, 0]]

# Construct the maze
with open('day20_input.txt', 'r') as file:
    for index, line in enumerate(file):
        row = list(line.strip())
        MAZE.append(row)
        if 'S' in line:
            START_POSITION = [index, row.index('S')]
        if 'E' in line:
            END_POSITION = [index, row.index('E')]


print('starting maze')
for row in MAZE:
    print(''.join(row))
print('-------------')

curr_pos = START_POSITION
DISTANCE = {
    str(curr_pos): 0
}
TO_GO = {}
steps = 0
VISITED = [START_POSITION]
# Navigate through the maze
while curr_pos != END_POSITION:
    # Try each of the directions
    for direction in DIRECTIONS:
        candidate = [curr_pos[0] + direction[0], curr_pos[1] + direction[1]]
        # Only go this way if it's a valid move, and not visited (there will only be one possibility in this maze)
        if candidate not in VISITED and MAZE[candidate[0]][candidate[1]] in ['.', 'E']:
            steps += 1
            curr_pos = candidate
            VISITED.append(candidate)
            # Keep track of the number of steps we have taken to get to thie point
            DISTANCE[str(curr_pos)] = steps

print('num_steps', steps)

# Generate a hash of the number of steps to go from each point
for index, pos in enumerate(VISITED):
    TO_GO[str(pos)] = steps - index

SAVES = {}
greater_than_100 = 0
for pos in VISITED:
    for cheat in CHEATS:
        candidate = [pos[0] + cheat[0], pos[1] + cheat[1]]
        # Make sure the cheat lands on a valid square
        if str(candidate) in DISTANCE:
            # The total path length is [dist_travelled + cheat_len(2) + cheat_end_steps_to_go]
            candidate_steps = DISTANCE[str(pos)] + 2 + TO_GO[str(candidate)]
            # If the cheat saves us time, track it
            if candidate_steps < steps:
                num_saved = steps - candidate_steps
                if num_saved not in SAVES:
                    SAVES[num_saved] = 1
                else:
                    SAVES[num_saved] += 1
                if num_saved >= 100:
                    greater_than_100 += 1

save_keys = list(SAVES.keys())
save_keys.sort()
for key in save_keys:
    print(key, SAVES[key])

print('at least 100:', greater_than_100)
