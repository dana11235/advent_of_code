orders = {}
tests = []
sum = 0

def correct(input):
    passed = True
    for index, number in enumerate(test):
        if number in orders:
            successors = orders[number]
            for successor in successors:
                if successor in test and test.index(successor) < index:
                    passed = False

    return passed

def fix(input):
    passed = True
    index = len(test) - 1
    while index >= 0:
        number = test[index]
        if number in orders:
            successors = orders[number]
            for successor in successors:
                if successor in test and test.index(successor) < index:
                    passed = False
                    test.remove(successor)
                    test.insert(index, successor)
                    index -= 1
        index -= 1

    return passed


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
    passed = originally_passed = fix(test)
    while not passed: # I'm sure there is a better way to do this than repeatedly fixing
        passed = fix(test)

    if not originally_passed:
        sum += test[len(test) // 2]

print(sum)