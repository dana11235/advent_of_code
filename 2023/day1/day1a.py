import re

sum = 0
with open('day1_input.txt', 'r') as file:
    for line in file:
        results = re.findall("[0-9]", line)
        sum += int(results[0] + results[-1])
print(sum)
