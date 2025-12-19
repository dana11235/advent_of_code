import numpy

machines = []

class Machine:
	def __init__(self, lights, buttons, joltage):
		self.lights = lights
		self.buttons = buttons
		self.joltage = joltage

	def get_lights(self, pushes):
		output = numpy.zeros(len(self.lights))
		for i, num_pushes in enumerate(pushes):
			curr = num_pushes * self.buttons[i]
			output +=  curr
		return output % 2

	def get_joltage(self, pushes):
		output = numpy.zeros(len(self.joltage))
		for i, num_pushes in enumerate(pushes):
			curr = num_pushes * self.buttons[i]
			output +=  curr
		return output

	def is_desired_lights(self, output):
		return numpy.array_equal(output, self.lights)

	def is_desired_joltage(self, output):
		return numpy.array_equal(output, self.joltage)
	



MIN_SUM = {'x': 100000}
with open('input.txt', 'r') as file:
	for line in file:
		line = line.strip()
		print(line)
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
				curr_button = list(numpy.zeros(len(lights)))
				for effect in piece[1:-1].split(','):
					curr_button[int(effect)] = 1
				buttons.append(curr_button)
			elif piece[0] == '{':
				joltage = [int(effect) for effect in piece[1:-1].split(',')]
		
		machines.append(Machine(lights, buttons, joltage))

def calc_recurse(machine, index, values, max_joltage):
	if index == len(machine.buttons):
		joltage = machine.get_joltage(values)
		if machine.is_desired_joltage(joltage) and sum(values) < MIN_SUM['x']:
			MIN_SUM['x'] = sum(values)
			MIN_SUM['value'] = values
	else:
		for i in range(max_joltage + 1):
			new_values = values[:]
			new_values.append(i)
			if sum(values) > max_joltage:
				break
			calc_recurse(machine, index + 1, new_values, max_joltage)
		
def get_possibilities(index, light_index, possible_buttons, joltage_val, states):
	if index == len(possible_buttons):
		return [state for state in states if state[light_index] == joltage_val]
	else:
		possibilities = []
		curr_button = possible_buttons[index]
		for state in states:
			for i in range(joltage_val + 1):
				curr_state = numpy.array(state[:])
				curr_state += numpy.array(curr_button) * i
				if curr_state[light_index] <= joltage_val:
					possibilities += get_possibilities(index + 1, light_index, possible_buttons, joltage_val, [curr_state])
				else:
					break
		return possibilities


TOTAL = 0
POSSIBILITIES = {}
for machine in machines:
	print(machine)
	joltage_copy = machine.joltage.copy()
	excluded_buttons = []
	joltage_copy.sort()
	possibilities = [numpy.zeros(len(machine.joltage))]
	for joltage_val in joltage_copy:
		light_index = machine.joltage.index(joltage_val)
		possible_buttons = [button for button in machine.buttons if button[light_index] == 1 and button not in excluded_buttons]
		#print('buttons', possible_buttons)
		#possible_buttons = [button for button in possible_buttons if button not in excluded_buttons]
		possibilities = get_possibilities(0, light_index, possible_buttons, joltage_val, possibilities)
		#print(possibilities)
		for button in possible_buttons:
			excluded_buttons.append(button)
	#break

#print('total', TOTAL)


#[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
#[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
#[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}