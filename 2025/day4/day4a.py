MAP = []
OUTPUT_MAP = []
num_accessible = 0
with open("input.txt", "r") as file:
    for line in file:
        MAP.append(list(line.strip()))
        OUTPUT_MAP.append([])
y_len = len(MAP) - 1
x_len = len(MAP[0]) - 1

for y_index, line in enumerate(MAP):
    for x_index, _ in enumerate(line):
        if MAP[y_index][x_index] == ".":
            OUTPUT_MAP[y_index].append(".")
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
        if x_index < x_len and y_index < y_len and MAP[y_index + 1][x_index + 1] == "@":
            adjacent += 1
        if x_index > 0 and y_index < y_len and MAP[y_index + 1][x_index - 1] == "@":
            adjacent += 1
        if x_index < x_len and y_index > 0 and MAP[y_index - 1][x_index + 1] == "@":
            adjacent += 1
        if adjacent < 4:
            OUTPUT_MAP[y_index].append(str(adjacent))
            num_accessible += 1
        else:
            OUTPUT_MAP[y_index].append(str(adjacent))


for line in OUTPUT_MAP:
    print("".join(line))

print("accessible", num_accessible)
