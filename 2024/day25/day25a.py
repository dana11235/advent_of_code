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

    # start with -1 in all rows, since 0-height has 1 pin set
    values = [-1, -1, -1, -1, -1]
    for row in item:
        # We can just add the total number since there isn't anything weird with heights
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
# Run through all of the lock/key combos
for lock in locks:
    for key in keys:
        valid = True
        for index, pin in enumerate(key):
            # If the sum of heights is > 5, there is overlap on that tumbler
            if pin + lock[index] > 5:
                valid = False
        # If there hasn't been any overlap, the combo matches
        if valid:
            matches += 1

print(matches)
