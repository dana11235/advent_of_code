orders = {}
tests = []
sum = 0

with open('day5_input.txt', 'r') as file:
    for line in file:
        if '|' in line:
            parts = line.split('|')
            if int(parts[0]) in orders:
                orders[int(parts[0])].append(int(parts[1]))
            else:
                orders[int(parts[0])] = [int(parts[1])]

        if ',' in line:
            tests.append([int(num) for num in line.split(',')])

for test in tests:
    passed = True
    for index, number in enumerate(test):
        if number in orders:
            successors = orders[number]
            for successor in successors:
                if successor in test and test.index(successor) < index:
                    passed = False

    if passed:
        sum += test[len(test) // 2]

print(sum)