num_0s = 0
position = 50
with open('input1.txt', 'r') as file:
	for line in file:
		new_0s = 0
		direction = line[0]
		spaces = int(line[1:])
		if direction == 'L':
			start = position
			position -= spaces
			if position <= 0:
				new_0s = (abs(position) // 100) + 1
				if start == 0:
					new_0s -= 1
		else:
			position += spaces
			new_0s += (position // 100)
		num_0s += new_0s
		position = position % 100
	print('num0', num_0s)

