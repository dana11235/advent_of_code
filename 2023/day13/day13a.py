patterns = []
curr_pattern = []
with open('day13_input.txt', 'r') as file:
    for line in file:
        line = line.strip()
        if len(line) == 0:
            patterns.append(curr_pattern)
            curr_pattern = []
        else:
            curr_pattern.append(list(line))
    if len(curr_pattern) > 0:
        patterns.append(curr_pattern)


def matches_hor(pattern, row1_index, row2_index):
    matches = True
    row1 = pattern[row1_index]
    row2 = pattern[row2_index]
    for pos, obj in enumerate(row1):
        matches = matches and (obj == row2[pos])
    return matches


def matches_ver(pattern, col1_index, col2_index):
    matches = True
    for row in pattern:
        matches = matches and (row[col1_index] == row[col2_index])
    return matches


sum = 0
for pattern in patterns:
    index = 0
    reflection_found = False
    while index < len(pattern) - 1:
        lower_index = index
        upper_index = index + 1
        if matches_hor(pattern, lower_index, upper_index):
            reflects = True
            lower_index -= 1
            upper_index += 1
            while lower_index >= 0 and upper_index < len(pattern):
                reflects = reflects and matches_hor(
                    pattern, lower_index, upper_index)
                lower_index -= 1
                upper_index += 1
            if reflects:
                reflection_found = True
                sum += 100 * (index + 1)
                break
        index += 1
    index = 0
    if not reflection_found:
        while index < len(pattern[0]) - 1:
            left_index = index
            right_index = index + 1
            if matches_ver(pattern, left_index, right_index):
                reflects = True
                left_index -= 1
                right_index += 1
                while left_index >= 0 and right_index < len(pattern[0]):
                    reflects = reflects and matches_ver(
                        pattern, left_index, right_index)
                    left_index -= 1
                    right_index += 1
                if reflects:
                    sum += (index + 1)
                    break
            index += 1

print(sum)
