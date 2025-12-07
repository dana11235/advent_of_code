board = []
with open("input.txt", "r") as file:
    for line in file:
        board.append(list(line.strip()))

active = None
for index, cell in enumerate(board[0]):
    if cell == "S":
        active = {index: 1}

num_splits = 0
for row in board[1:]:
    new_active = {}
    for index in active.keys():
        curr_val = active[index]
        if row[index] == ".":
            if index not in new_active:
                new_active[index] = curr_val
            else:
                new_active[index] += curr_val

        elif row[index] == "^":
            if index - 1 not in new_active:
                new_active[index - 1] = curr_val
            else:
                new_active[index - 1] += curr_val

            if index + 1 not in new_active:
                new_active[index + 1] = curr_val
            else:
                new_active[index + 1] += curr_val
            num_splits += 1
    active = new_active

print("splits", num_splits)
print("poss", sum(active.values()))
