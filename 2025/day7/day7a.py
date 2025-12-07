board = []
with open("input.txt", "r") as file:
    for line in file:
        board.append(list(line.strip()))

active = None
for index, cell in enumerate(board[0]):
    if cell == "S":
        active = [index]

num_splits = 0
for row in board[1:]:
    new_active = []
    for index in active:
        if row[index] == ".":
            if index not in new_active:
                new_active.append(index)
        elif row[index] == "^":
            if index - 1 not in new_active:
                new_active.append(index - 1)
            if index + 1 not in new_active:
                new_active.append(index + 1)
            num_splits += 1
    active = new_active

print("splits", num_splits)
