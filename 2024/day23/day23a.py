connections = {}
sets = []
candidate_sets = []
with open('day23_input.txt', 'r') as file:
    for line in file:
        a, b = line.strip().split('-')
        if a not in connections:
            connections[a] = []
        if b not in connections:
            connections[b] = []
        connections[a].append(b)
        connections[b].append(a)


def starts_with_t(name):
    return 't' in name and name.index('t') == 0


for first in connections.keys():
    candidates = connections[first]
    for candidate in candidates:
        potential_thirds = connections[candidate]
        for third in potential_thirds:
            if third != first and third in candidates:
                set = [first, candidate, third]
                set.sort()
                if set not in sets:
                    sets.append(set)
                if set not in candidate_sets and (starts_with_t(first) or starts_with_t(candidate) or starts_with_t(third)):
                    candidate_sets.append(set)
print(len(sets))
print(len(candidate_sets))
