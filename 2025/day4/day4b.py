MAP = []
with open("input.txt", "r") as file:
    for line in file:
        MAP.append(list(line.strip()))

y_len = len(MAP) - 1
x_len = len(MAP[0]) - 1
total_removed = 0


def remove_rolls():
    removed_rolls = 0
    for y_index, line in enumerate(MAP):
        for x_index, _ in enumerate(line):
            if MAP[y_index][x_index] == ".":
                continue
            adjacent = 0
            if x_index > 0 and MAP[y_index][x_index - 1] == "@":
                adjacent += 1
            if y_index > 0 and MAP[y_index - 1][x_index] == "@":
                adjacent += 1
            if x_index > 0 and y_index > 0 and MAP[y_index - 1][x_index - 1] == "@":
                adjacent += 1
            if x_index < x_len and MAP[y_index][x_index + 1] == "@":
                adjacent += 1
            if y_index < y_len and MAP[y_index + 1][x_index] == "@":
                adjacent += 1
            if (
                x_index < x_len
                and y_index < y_len
                and MAP[y_index + 1][x_index + 1] == "@"
            ):
                adjacent += 1
            if x_index > 0 and y_index < y_len and MAP[y_index + 1][x_index - 1] == "@":
                adjacent += 1
            if x_index < x_len and y_index > 0 and MAP[y_index - 1][x_index + 1] == "@":
                adjacent += 1
            if adjacent < 4:
                MAP[y_index][x_index] = "."
                removed_rolls += 1
    return removed_rolls


num_removed = remove_rolls()
total_removed += num_removed
print(num_removed)
while num_removed > 0:
    num_removed = remove_rolls()
    print(num_removed)
    total_removed += num_removed


print("removed", total_removed)
