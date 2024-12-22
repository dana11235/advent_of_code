numbers = []
with open('day22_input.txt', 'r') as file:
    for line in file:
        numbers.append(int(line.strip()))


def mix(value, number):
    return value ^ number


def prune(number):
    return number % 16777216


def secretize(number):
    value = prune(mix(number * 64, number))
    value = prune(mix(value // 32, value))
    return prune(mix(value * 2048, value))


sum = 0
for number in numbers:
    curr = number
    for _ in range(2000):
        curr = secretize(curr)
    sum += curr
    print(number, curr)

print('sum', sum)
