import re
total = 0
with open('day3_input.txt', 'r') as file:
    for line in file:
        print(line)
        matches = re.findall(r'mul\(([0-9]+)\,([0-9]+)\)', line)
        print(matches)
        for match in matches:
            total += int(match[0]) * int(match[1])

print('total', total)