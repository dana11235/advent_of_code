coordinates = []

class Coord:
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def rectangle_area_with(self, coord2):
		return abs(self.x - coord2.x + 1) * abs(self.y - coord2.y + 1)


with open('input.txt', 'r') as file:
	for line in file:
		line = line.strip()
		x, y = [int(num) for num in line.split(',')]
		coordinates.append(Coord(x, y))

max_area = 0
for i, coord1 in enumerate(coordinates[:-1]):
	for coord2 in coordinates[i + 1:]:
		area = coord1.rectangle_area_with(coord2)
		if area > max_area:
			max_area = area

print(max_area)

