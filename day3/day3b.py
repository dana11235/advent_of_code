import re
total = 0
enabled = True
with open('day3_input.txt', 'r') as file:
    for line in file:
        print(line)
        matches = re.findall(r'(?:mul\([0-9]+\,[0-9]+\))|(?:do\(\))|(?:don\'t\(\))', line)
        print(matches)
        for match in matches:
            if match == 'do()':
                enabled = True
            elif match  == 'don\'t()':
                enabled = False
            else:
                if enabled:
                    match_parts = re.findall(r'[0-9]+', match)
                    total += int(match_parts[0]) * int(match_parts[1])

print('total', total)