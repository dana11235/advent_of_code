OPS = []
with open('day2_input.txt', 'r') as file:
    for line in file:
        line = line.strip()
        OPS += [int(num) for num in line.split(',')]

OPS[1] = 12
OPS[2] = 2
index = 0
while index <= len(OPS):
    if OPS[index] == 99:
        break
    elif OPS[index] == 1:
        OPS[OPS[index + 3]] = OPS[OPS[index + 1]] + OPS[OPS[index + 2]]
        index += 4
    elif OPS[index] == 2:
        OPS[OPS[index + 3]] = OPS[OPS[index + 1]] * OPS[OPS[index + 2]]
        index += 4

print(OPS[0])
