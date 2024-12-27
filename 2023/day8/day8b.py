DIRECTIONS = []
NODES = {}
CURR_NODES = []
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
            source = source.strip()
            if source[2] == 'A':
                CURR_NODES.append(source)
            NODES[source] = [left_node[2:].strip(),
                             right_node[0:-1].strip()]

print(CURR_NODES)
print('num_curr_nodes', len(CURR_NODES))

multiple = 1
for curr_node in CURR_NODES:
    orig_curr_node = curr_node
    direction_pointer = -1
    count = 0
    while curr_node[2] != 'Z':
        count += 1
        direction_pointer = (direction_pointer + 1) % len(DIRECTIONS)
        curr_direction = DIRECTIONS[direction_pointer]
        if curr_direction == 'L':
            curr_node = NODES[curr_node][0]
        elif curr_direction == 'R':
            curr_node = NODES[curr_node][1]
    print(count, orig_curr_node, curr_node)
    # I factored all of the lengths, and they have a common factor of 271
    multiple *= (count / 271)

# Then we multiply by 271 again to get the smallest common multiple
multiple *= 271
print(multiple)
