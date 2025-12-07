grid = []
with open("input.txt", "r") as file:
    for line in file:
        grid.append(list(line))

cells = []
current_cell = []
value = ""
for column in range(len(grid[0]) - 1):
    has_value = False
    value = ""
    for cell in range(len(grid)):
        curr_value = grid[cell][column]
        if curr_value != " ":
            if curr_value == "+" or curr_value == "*":
                current_cell.append(curr_value)
            else:
                value += curr_value
                has_value = True
    if has_value:
        current_cell.append(value)
    else:
        cells.append(current_cell)
        current_cell = []
cells.append(current_cell)

grand_total = 0
for cell in cells:
    operation = ""
    line_total = 0

    for index, num in enumerate(cell):
        if index == 0:
            operation = num
            if operation == "*":
                line_total = 1
        else:
            if operation == "+":
                line_total += int(num)
            else:
                line_total *= int(num)
    grand_total += line_total

print(grand_total)
