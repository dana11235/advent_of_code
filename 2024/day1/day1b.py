list_one = []
list_two = []
list2_loc = 0
sim_score = 0
counts = {}
with open('day1_input.txt', 'r') as file:
    for line in file:
        parts = line.split()
        list_one.append(int(parts[0]))
        list_two.append(int(parts[1]))
list_one.sort()
list_two.sort()
for val in list_one:
    while list2_loc < len(list_two) and list_two[list2_loc] < val:
        list2_loc += 1
    while list2_loc < len(list_two) and list_two[list2_loc] == val:
        if val not in counts:
            counts[val] = 1
        else:
            counts[val] += 1
        list2_loc += 1
    if list2_loc >= len(list_two):
        break

for key in counts:
    sim_score += (key * counts[key])

print('sim score', sim_score)