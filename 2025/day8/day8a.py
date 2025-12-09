import math
boxes = []

class Box:
	def __init__(self, id, coords):
		x, y, z = coords
		self.x = x
		self.y = y 
		self.z = z
		self.id = id
	def __str__(self):
		return f"{self.id}: {self.x},{self.y},{self.z}"

with open('input.txt', 'r') as file:
	for id, line in enumerate(file):
		line = line.strip()
		boxes.append(Box(id, [int(num) for num in line.split(',')]))
		
for box in boxes:
	print(box)
		
REPS = 1000
connections = {}
GROUPS = {'n': []}

def dist(box1, box2):
	return math.sqrt(
		math.pow(box1.x - box2.x, 2) + 
		math.pow(box1.y - box2.y, 2) + 
		math.pow(box1.z - box2.z, 2)
	)
	
def connected(box1, box2):
	return (box1 in connections and box2 in connections[box1]) or (box2 in connections and box1 in connections[box2])

def same_circuit(box1, box2):
	for group in GROUPS['n']:
		if box1 in group and box2 in GROUPS['n']:
			return True
	return False
	
def connect(box1, box2):
	if  box1 not in connections:
		connections[box1] = []
	connections[box1].append(box2)
	if box2 not in connections:
		connections[box2] = []
	connections[box2].append(box1)

	groups_to_merge = []
	new_groups = []
	for group in GROUPS['n']:
		if box1 in group or box2 in group:
			groups_to_merge.append(group)
		else:
			new_groups.append(group)

	unified_group = {box1: True, box2: True}
	for group in groups_to_merge:
		for key in group.keys():
			unified_group[key] = True
	new_groups.append(unified_group)
	GROUPS['n'] = new_groups

distances = {}
for i, box1 in enumerate(boxes[:-1]):
	for j, box2 in enumerate(boxes[i + 1:]):
		distance = dist(box1, box2)
		distances[distance] = [box1, box2]

sorted_lengths = list(distances.keys())
sorted_lengths.sort()
print('len', len(sorted_lengths))

count = 0
position = 0
while count < REPS: 
	box1, box2 = distances[sorted_lengths[position]]
	if not connected(box1, box2) and not same_circuit(box1, box2):
		connect(box1, box2)
		count += 1
	position += 1

group_sizes = [len(group) for group in GROUPS['n']]
group_sizes.sort()

print('mul', group_sizes[-1] * group_sizes[-2] * group_sizes[-3])



