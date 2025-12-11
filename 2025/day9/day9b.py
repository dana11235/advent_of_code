import matplotlib.pyplot as plt
reds = {}
greens = {}

class Coord:
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def __lt__(self, other):
		return self.x < other.x

	def rectangle_area_with(self, coord2):
		
		return (abs(self.x - coord2.x) + 1) * (abs(self.y - coord2.y) + 1)

	def __str__(self):
		return f'(x: {self.x},y: {self.y})'
	
	def __eq__(self, other):
		return self.x == other.x and self.y == other.y
	
	def __hash__(self):
		return hash((self.x, self.y))

def fill_between(coord1, coord2):
	if coord1.x > coord2.x:
		for i in range(coord2.x + 1, coord1.x):
			coord = Coord(i, coord1.y)
			if coord not in greens and coord not in reds:
				greens[coord] = True
	elif coord1.x < coord2.x:
		for i in range(coord1.x + 1, coord2.x):
			coord = Coord(i, coord1.y)
			if coord not in greens and coord not in reds:
				greens[coord] = True
	elif coord1.y > coord2.y:
		for i in range(coord2.y + 1, coord1.y):
			coord = Coord(coord1.x, i)
			if coord not in greens and coord not in reds:
				greens[coord] = True
	elif coord1.y < coord2.y:
		for i in range(coord1.y + 1, coord2.y):
			coord = Coord(coord1.x, i)
			if coord not in greens and coord not in reds:
				greens[coord] = True

last = None
first = None
max_y = 0
with open('input.txt', 'r') as file:
	for line in file:
		line = line.strip()
		x, y = [int(num) for num in line.split(',')]
		if y > max_y:
			max_y = y
		coord = Coord(x, y)
		if not first:
			first = coord
		reds[coord] = True
		if last:
			fill_between(last, coord)
		last = coord
	fill_between(last, first)
print('num points', len(reds.keys()))

def draw_picture():
	x_coords = []
	y_coords = []
	first = None
	for coord in reds:
		if not first:
			first = coord
		x_coords.append(coord.x)
		y_coords.append(coord.y)
	x_coords.append(first.x)
	y_coords.append(first.y)
	plt.plot(x_coords, y_coords)
	

# I figured these out by drawing a picture of the plot
top_point = Coord(94865,48656)
bottom_point = Coord(94865,50110)

def is_in(test, point1, point2):
	return test != point1 and test != point2 and test.x > min(point1.x, point2.x) and test.x < max(point1.x, point2.x) and test.y > min(point1.y, point2.y) and test.y < max(point1.y, point2.y)

def get_max_rect():
	max_point_1 = None
	max_point_2 = None
	max_rect_area = 0
	for coord in reds:
		if coord.y < top_point.y and (coord.rectangle_area_with(top_point) > max_rect_area):
			point_in_rect = False
			for test in reds:
				if is_in(test, coord, top_point):
					point_in_rect = True
					break
			if not point_in_rect:
				max_rect_area = coord.rectangle_area_with(top_point)
				max_point_1 = coord
				max_point_2 = top_point
		elif coord.y > bottom_point.y and (coord.rectangle_area_with(bottom_point) > max_rect_area):
			point_in_rect = False
			for test in reds:
				if is_in(test, coord, bottom_point):
					point_in_rect = True
					break
			if not point_in_rect:
				max_rect_area = coord.rectangle_area_with(bottom_point)
				max_point_1 = coord
				max_point_2 = bottom_point
	return [max_rect_area, max_point_1, max_point_2]

def draw_rect(point1, point2):
	point_x = [point1.x, point2.x, point2.x, point1.x, point1.x]
	point_y = [point1.y, point1.y, point2.y, point2.y, point1.y]
	plt.plot(point_x, point_y)


max_rect_area, max_point_1, max_point_2 = get_max_rect()
print("max area", max_rect_area)
#draw_picture()
#draw_rect(max_point_1, max_point_2)
#plt.show()


#print('-----------')
#for k in greens.keys():
#	print(k)

#print('r', len(reds.keys()))
#print('gr', len(greens.keys()))

#..............
#.......#XXX#..
#.......X...X..
#..#XXXX#...X..
#..X........X..
#..#XXXXXX#.X..
#.........X.X..
#.........#X#..
#..............