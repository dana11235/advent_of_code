columns = []
universe = []
galaxies = []
with open('day11_input.txt', 'r') as file:
    for row_index, line in enumerate(file):
        row = list(line.strip())
        universe.append(row)
        if '#' not in row:
            universe.append(row.copy())
        for col_index, obj in enumerate(row):
            is_galaxy = False
            if obj == '#':
                is_galaxy = True
            if len(columns) > col_index:
                columns[col_index] = columns[col_index] or is_galaxy
            else:
                columns.append(is_galaxy)

col_index = 0
natural_index = 0
while col_index < len(universe[0]):
    if not columns[natural_index]:
        for row_index in range(len(universe)):
            universe[row_index].insert(col_index, '.')
        col_index += 1
    natural_index += 1
    col_index += 1

for row_index, row in enumerate(universe):
    for col_index, obj in enumerate(row):
        if obj == '#':
            galaxies.append([row_index, col_index])

shortest_distance = 0

for index1, galaxy1 in enumerate(galaxies):
    for index2 in range(index1 + 1, len(galaxies)):
        galaxy2 = galaxies[index2]
        shortest_distance += abs(galaxy1[0] - galaxy2[0]) + \
            abs(galaxy1[1] - galaxy2[1])

print(shortest_distance)
