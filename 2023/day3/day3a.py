schematic = []
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
with open('day3_input.txt', 'r') as file:
    for line in file:
        schematic.append(list(line.strip()))

sum = 0
for row_index, line in enumerate(schematic):
    position = 0
    while position < len(line):
        while position < len(line) and line[position] not in numbers:
            position += 1
        curr_number = ''
        first_pos = position
        while position < len(line) and line[position] in numbers:
            curr_number += line[position]
            position += 1
        if len(curr_number) == 0:
            continue
        last_pos = position - 1
        is_part = False
        if first_pos > 0 and line[first_pos - 1] != '.':
            is_part = True
        elif last_pos < len(line) - 1 and line[last_pos + 1] != '.':
            is_part = True
        else:
            i = max(first_pos - 1, 0)
            while i < len(line) and i <= last_pos + 1:
                if row_index > 0 and schematic[row_index - 1][i] != '.' and schematic[row_index - 1][i] not in numbers:
                    is_part = True
                if row_index < len(schematic) - 1 and schematic[row_index + 1][i] != '.' and schematic[row_index + 1][i] not in numbers:
                    is_part = True
                i += 1
        print(curr_number, is_part)
        if is_part:
            sum += int(curr_number)
print(sum)
