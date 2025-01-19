import heapq
import random
import math
import copy
MAPPING = {}

with open('day14_input.txt', 'r') as file:
    for line in file:
        line = line.strip()
        input, output = [token.strip() for token in line.split('=>')]
        output = output.split(' ')
        output[0] = int(output[0])
        input = [token.strip() for token in input.split(',')]
        parsed_input = []
        for token in input:
            token = token.split(' ')
            parsed_input.append([int(token[0]), token[1]])
        MAPPING[output[1]] = {
            'quantity': output[0],
            'inputs': parsed_input
        }

START = 'FUEL'
END = 'ORE'
DEPS = {}

# What we do here is recursively calculate the max level on which each product
# is produced. This allows us to figure out the number required
def calc_deps(item, level):
    lookup = MAPPING[item]
    components = lookup['inputs']
    for component in components:
        if component[1] not in DEPS or DEPS[component[1]] < level:
            DEPS[component[1]] = level
        if component[1] != END:
            calc_deps(component[1], level + 1)

calc_deps(START, 0)
to_produce = []
heapq.heapify(to_produce)
# Now we generate a priority queue to produce the products in order
for item in DEPS.items():
    heapq.heappush(to_produce, (item[1], random.random(), item[0]))

def calc_needed(num_fuel):
    curr_to_prod = copy.deepcopy(to_produce)
    NEEDED = {}
    # We seed the needed with the final components (multiplied by the number we produce)
    for component in MAPPING[START]['inputs']:
        NEEDED[component[1]] = num_fuel * component[0]

    while len(curr_to_prod) > 0:
        next = heapq.heappop(curr_to_prod)[2]
        # If we are producing ORE, we can just return the amount required
        if next == 'ORE':
            return NEEDED['ORE']
        else:
            lookup = MAPPING[next]
            output_quantity = lookup['quantity']
            quantity_needed = NEEDED[next]
            # figure out the whole number of each output required
            multiple = math.ceil(quantity_needed / output_quantity)
            for component in lookup['inputs']:
                quantity_produced = component[0]
                # We need to produce this amount of each input
                amount = multiple * quantity_produced
                name = component[1]
                # Add this to the quantity required of that input
                if name not in NEEDED:
                    NEEDED[name] = 0
                NEEDED[name] += amount

ore_needed_for_1 = calc_needed(1)
print('part a:', ore_needed_for_1)
max_ore = 1000000000000
# It's going to be more than this because of less waste, but we can start as a baseline
num_fuel = math.ceil(max_ore / ore_needed_for_1)
ore_needed = calc_needed(num_fuel)
while ore_needed < max_ore:
    num_fuel += 100
    ore_needed = calc_needed(num_fuel)
while ore_needed > max_ore:
    num_fuel -= 1
    ore_needed = calc_needed(num_fuel)

print('part b:', num_fuel)