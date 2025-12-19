import numpy

machines = []

class Machine:
	def __init__(self, lights, buttons, joltage):
		self.lights = lights
		self.buttons = buttons
		self.joltage = joltage

	def get_state(self, pushes):
		output = numpy.zeros(len(self.lights))
		for i, num_pushes in enumerate(pushes):
			curr = num_pushes * self.buttons[i]
			output +=  curr
		return output % 2

	def is_desired_state(self, output):
		return numpy.array_equal(output, self.lights)
	



MIN_SUM = {'x': 100000}
with open('input.txt', 'r') as file:
	for line in file:
		line = line.strip()
		pieces = line.split(' ')
		lights = []
		buttons = []
		joltage = []
		for piece in pieces:
			if piece[0] == '[':
				for light in piece[1:-1]:
					if light == '.':
						lights.append(0)
					else:
						lights.append(1)
			elif piece[0] == '(':
				curr_button = numpy.zeros(len(lights))
				for effect in piece[1:-1].split(','):
					curr_button[int(effect)] = 1
				buttons.append(curr_button)
			elif piece[0] == '{':
				joltage.append([int(effect) for effect in piece[1:-1].split(',')])
		
		machines.append(Machine(lights, buttons, joltage))

def calc_recurse(machine, index, values):
	if index == len(machine.buttons):
		state = machine.get_state(values)
		if machine.is_desired_state(state) and sum(values) < MIN_SUM['x']:
			MIN_SUM['x'] = sum(values)
			MIN_SUM['value'] = values
	else:
		for i in range(2):
			new_values = values[:]
			new_values.append(i)
			calc_recurse(machine, index + 1, new_values)


TOTAL = 0
for machine in machines:
	MIN_SUM['x'] = 1000000
	MIN_SUM['value'] = None
	calc_recurse(machine, 0, [])
	TOTAL += MIN_SUM['x']

print('total', TOTAL)


#[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
#[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
#[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}