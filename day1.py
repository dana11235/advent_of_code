list_one = []
list_two = []
difference = 0
with open('day1_input.txt', 'r') as file:
    for line in file:
        parts = line.split()
        list_one.append(parts[0])
        list_two.append(parts[1])
list_one.sort()
list_two.sort()
print('l1', list_one)
print('l2', list_two)
for index, val in enumerate(list_one):
    difference += abs(int(val) - int(list_two[index]))
print('totdiff', difference)
