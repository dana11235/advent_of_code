empty = ['.', '.', '.', '.', '.']
full = ['#', '#', '#', '#', '#']
keys = []
locks = []
current_item = []


def process_item(item):
    # check to see whether this is a lock or key, and convert to numbers
    type = 'lock'
    if item[0] == empty and item[-1] == full:
        type = 'key'

    values = [-1, -1, -1, -1, -1]
    for row in item:
        for index, value in enumerate(row):
            if value == '#':
                values[index] += 1
    if type == 'lock':
        locks.append(values)
    elif type == 'key':
        keys.append(values)


with open('day25_input.txt', 'r') as file:
    for line in file:
        if len(line.strip()) == 0:
            process_item(current_item)
            current_item = []
        else:
            current_item.append(list(line.strip()))
process_item(current_item)

matches = 0
for lock in locks:
    for key in keys:
        valid = True
        for index, pin in enumerate(key):
            if pin + lock[index] > 5:
                valid = False
        if valid:
            matches += 1

print(matches)
