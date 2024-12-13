schematic = []
test_numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
with open('day3_input.txt', 'r') as file:
    for line in file:
        schematic.append(list(line.strip()))

sum = 0
for row_index, line in enumerate(schematic):
    for col_index, char in enumerate(line):
        if schematic[row_index][col_index] == '*':
            numbers = []
            i = max(row_index - 1, 0)
            while i <= row_index + 1 and i < len(schematic):
                j = max(col_index - 1, 0)
                while j <= col_index + 1 and j < len(line):
                    if schematic[i][j] in test_numbers:
                        left = j
                        right = j
                        while left - 1 >= 0 and schematic[i][left - 1] in test_numbers:
                            left -= 1
                        while right + 1 < len(line) and schematic[i][right + 1] in test_numbers:
                            right += 1
                        curr_number = ''.join(schematic[i][left: right + 1])
                        if curr_number not in numbers:
                            numbers.append(curr_number)
                    j += 1
                i += 1
            if len(numbers) == 2:
                sum += int(numbers[0]) * int(numbers[1])
print(sum)
