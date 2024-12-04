import re
total_matches = 0
rotated = []
diag1 = []
diag2 = []

def find_in_line(line):
    total = 0
    matches = len(re.findall(r'XMAS', line))
    print('forward', matches)
    total += matches
    matches = len(re.findall(r'SAMX', line))
    print('backward', matches)
    total += matches
    print('total', total)
    return total


with open('day4_input.txt', 'r') as file:
    for line_index, line in enumerate(file):
        total_matches += find_in_line(line)
        for index, letter in enumerate(line):
            # Handle the rotated 90 degrees
            if len(rotated) < len(line):
                rotated.append(letter)
            else:
                rotated[index] += letter
            # Handle diagonal forwards
            if line_index == 0:
                diag1.append(letter)
            elif index == 0:
                diag1.insert(0, letter)
            else:
                diag1[index] += letter
            # Handle diagonal backwards
            if line_index == 0:
                diag2.append(letter)
            elif index == len(line) - 1:
                diag2.append(letter)
            else:
                diag2[index + line_index] += letter
            
print(total_matches)

for line in rotated:
    total_matches += find_in_line(line)

for line in diag1:
    total_matches += find_in_line(line)

for line in diag2:
    total_matches += find_in_line(line)

print('total', total_matches)