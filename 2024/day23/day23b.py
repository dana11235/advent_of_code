connections = {}
groups = []
with open('day23_input.txt', 'r') as file:
    for line in file:
        a, b = line.strip().split('-')
        if a not in connections:
            connections[a] = []
        if b not in connections:
            connections[b] = []
        connections[a].append(b)
        connections[b].append(a)


for first in connections.keys():
    candidates = connections[first]
    for candidate in candidates:
        potential_thirds = connections[candidate]
        for third in potential_thirds:
            if third != first and third in candidates:
                group = set([first, candidate, third])
                if group not in groups:
                    groups.append(group)


while True:
    new_groups = []
    for group in groups:
        as_list = list(group)
        intersection = None
        # This code calculates the intersection between the three sets of connections
        for index, element in enumerate(as_list):
            if index == 0:
                intersection = set(connections[element])
            else:
                intersection &= set(connections[element])
        intersections = list(intersection)
        if len(intersections) > 0:
            # We only take the first connection.
            # This seemed simpler than checking for mutual connectedness.
            # I also assumed that we would prune the list quickly.
            new_member = intersections[0]
            candidate_group = group.copy()
            candidate_group.add(new_member)
            # We wouldn't want to add the group more than once
            if candidate_group not in new_groups:
                new_groups.append(candidate_group)

    # We only continue if we have found a group that is larger on this iteration
    if len(new_groups) > 0:
        groups = new_groups
    else:
        break

# Do some formatting
group_list = list(groups[0])
group_list.sort()
print(','.join(group_list))
