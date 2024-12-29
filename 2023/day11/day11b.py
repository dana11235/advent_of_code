columns = []
rows = []
universe = []
galaxies = []
with open('day11_input.txt', 'r') as file:
    for row_index, line in enumerate(file):
        row = list(line.strip())
        universe.append(row)
        rows.append('#' in row)
        for col_index, obj in enumerate(row):
            is_galaxy = False
            if obj == '#':
                galaxies.append([row_index, col_index])
                is_galaxy = True
            if len(columns) > col_index:
                columns[col_index] = columns[col_index] or is_galaxy
            else:
                columns.append(is_galaxy)

shortest_distance = 0

DILATION_FACTOR = 1000000
for index1, galaxy1 in enumerate(galaxies):
    for index2 in range(index1 + 1, len(galaxies)):
        galaxy2 = galaxies[index2]
        curr_distance = 0
        ys = [galaxy1[0], galaxy2[0]]
        ys.sort()
        y_dist = 0
        if ys[1] > ys[0]:
            for index in range(ys[0] + 1, ys[1]):
                if not rows[index]:
                    y_dist += DILATION_FACTOR
                else:
                    y_dist += 1
            y_dist += 1
        xs = [galaxy1[1], galaxy2[1]]
        xs.sort()
        x_dist = 0
        if xs[1] > xs[0]:
            for index in range(xs[0] + 1, xs[1]):
                if not columns[index]:
                    x_dist += DILATION_FACTOR
                else:
                    x_dist += 1
            x_dist += 1
        shortest_distance += y_dist + x_dist

print(shortest_distance)
