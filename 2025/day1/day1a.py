num_0s = 0
position = 50
with open('input1.txt', 'r') as file:
	for line in file:
		direction = line[0]
		spaces = int(line[1:])
		if direction == 'L':
			position -= spaces
		else:
			position += spaces
		position = position % 100
		if position == 0:
			num_0s += 1
	print(num_0s)

