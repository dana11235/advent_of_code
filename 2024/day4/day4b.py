total_xmas = 0
with open('day4_input.txt', 'r') as file:
    all_lines = []
    for line in file:
        all_lines.append(list(line))

    for row, line in enumerate(all_lines):
        if row > 0 and row < len(all_lines) - 1:
            for col, char in enumerate(line):
                if char == 'A':
                    if col > 0 and col < len(line) - 1:
                        forward = False
                        backwards = False
                        if all_lines[row - 1][col - 1] == 'M' and all_lines[row + 1][col + 1] == 'S':
                            forward = True
                        if all_lines[row - 1][col - 1] == 'S' and all_lines[row + 1][col + 1] == 'M':
                            forward = True
                        if all_lines[row - 1][col + 1] == 'M' and all_lines[row + 1][col - 1] == 'S':
                            backwards = True
                        if all_lines[row - 1][col + 1] == 'S' and all_lines[row + 1][col - 1] == 'M':
                            backwards = True
                        if forward and backwards:
                            total_xmas += 1
print(total_xmas)


