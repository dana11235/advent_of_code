LAYERS = []
WIDTH = 25
HEIGHT = 6
with open('day8_input.txt', 'r') as file:
    for line in file:
        digits = [int(digit) for digit in list(line.strip())]
        num_digits = len(digits)
        print('num', num_digits)
        index = 0
        min_0s = None
        answer = None
        while index < len(digits):
            IMAGE = []
            num_0s = 0
            num_1s = 0
            num_2s = 0
            for _ in range(HEIGHT):
                row = digits[index:index + WIDTH]
                IMAGE.append(row)
                num_0s += row.count(0)
                num_1s += row.count(1)
                num_2s += row.count(2)
                index += WIDTH
            if not min_0s or num_0s < min_0s:
                min_0s = num_0s
                answer = num_1s * num_2s
            LAYERS.append(IMAGE)
print('layers', len(LAYERS))
print('ans', answer)

image = []
row = []
for _ in range(WIDTH):
    row.append(2)
for _ in range(HEIGHT):
    image.append(row.copy())

for layer in LAYERS:
    for row_index, row in enumerate(layer):
        for col_index, cell in enumerate(row):
            if image[row_index][col_index] == 2 and cell != 2:
                image[row_index][col_index] = cell

for row in image:
    row_str = ''.join([str(num) for num in row])
    print(row_str.replace('0', ' ').replace('1','#'))