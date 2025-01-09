map = []
with open('day10_input.txt', 'r') as file:
    for row in file:
        map.append([int(char) for char in list(row.strip())])

num_rows = len(map)
num_cols = len(map[0])


def get_score(row_index, col_index, num, ends):

    if num == 9:
        return 1

    score = 0
    next_num = num + 1
    if row_index > 0:
        n = map[row_index - 1][col_index]
        if n == next_num:
            score += get_score(row_index - 1, col_index, next_num, ends)
    if row_index < num_rows - 1:
        s = map[row_index + 1][col_index]
        if s == next_num:
            score += get_score(row_index + 1, col_index, next_num, ends)
    if col_index > 0:
        w = map[row_index][col_index - 1]
        if w == next_num:
            score += get_score(row_index, col_index - 1, next_num, ends)
    if col_index < num_cols - 1:
        e = map[row_index][col_index + 1]
        if e == next_num:
            score += get_score(row_index, col_index + 1, next_num, ends)

    return score


total_score = 0
for row_index, row in enumerate(map):
    for col_index, char in enumerate(row):
        if char == 0:
            score = 0
            ends = []
            score = get_score(row_index, col_index, 0, ends)
            total_score += score
print('ts', total_score)
