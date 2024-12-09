antennas = {}
antinodes = []
map = []
with open('day8_input.txt', 'r') as file:
    for row, line in enumerate(file):
        chars = list(line.strip())
        map.append(chars)
        for col, char in enumerate(chars):
            if char != '.':
                if char not in antennas:
                    antennas[char] = [[row, col]]
                else:
                    antennas[char].append([row, col])
for key in antennas.keys():
    values = antennas[key]
    for i in range(len(values)):
        for j in range(i + 1, len(values)):
            first = values[i]
            second = values[j]
            if first not in antinodes:
                antinodes.append(first.copy())
            if second not in antinodes:
                antinodes.append(second.copy())
            diff = [second[0] - first[0], second[1] - first[1]]
            first_cand = first.copy()
            while first_cand[0] >= 0 and first_cand[0] < len(map[0]) and first_cand[1] >= 0 and first_cand[1] < len(map):
                first_cand = [first_cand[0] - diff[0], first_cand[1] - diff[1]]
                if first_cand[0] >= 0 and first_cand[0] < len(map[0]) and first_cand[1] >= 0 and first_cand[1] < len(map) and first_cand not in antinodes:
                    antinodes.append(first_cand.copy())
            second_cand = second.copy()
            while second_cand[0] >= 0 and second_cand[0] < len(map[0]) and second_cand[1] >= 0 and second_cand[1] < len(map):
                second_cand = [second_cand[0] + diff[0], second_cand[1] + diff[1]]
                if second_cand[0] >= 0 and second_cand[0] < len(map[0]) and second_cand[1] >= 0 and second_cand[1] < len(map) and second_cand not in antinodes:
                    antinodes.append(second_cand.copy())
print(len(antinodes))