DIRECTIONS = []
NODES = {}
mode = 'directions'
with open('day8_input.txt', 'r') as file:
    for line in file:
        if len(line.strip()) == 0:
            mode = 'nodes'
        elif mode == 'directions':
            DIRECTIONS += list(line.strip())
        elif mode == 'nodes':
            source, destinations = line.strip().split('=')
            left_node, right_node = destinations.split(',')
            NODES[source.strip()] = [left_node[2:].strip(),
                                     right_node[0:-1].strip()]

DIRECTION_POINTER = -1
CURR_NODE = 'AAA'

COUNT = 0
while CURR_NODE != 'ZZZ':
    COUNT += 1
    DIRECTION_POINTER = (DIRECTION_POINTER + 1) % len(DIRECTIONS)
    curr_direction = DIRECTIONS[DIRECTION_POINTER]
    if curr_direction == 'L':
        CURR_NODE = NODES[CURR_NODE][0]
    elif curr_direction == 'R':
        CURR_NODE = NODES[CURR_NODE][1]

print(COUNT)
