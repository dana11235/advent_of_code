input = []
base_pattern = [0, 1, 0, -1]

def parse_line(line):
    return [int(num) for num in list(line.strip())]

with open('day16_input.txt', 'r') as file:
    for line in file:
        input += parse_line(line)

input_size = len(input)

def get_pattern(iter, pos):
    pattern_pos = ((pos + 1) // iter) % 4
    return base_pattern[pattern_pos]

def run_iter(input):
    output = []
    for iter in range(len(input)):
        sum = 0
        sum_str = ''
        for pos, value in enumerate(input):
            pattern = get_pattern(iter + 1, pos)
            sum_str += f"{value}*{pattern} +"
            sum += (value * pattern)
        output.append(abs(sum) % 10) 
    return output

def print_output(input):
    return ''.join( [str(num) for num in input[0:8]])

def print_full_output(input):
    return ''.join( [str(num) for num in input])

def calc_sample(input):
    for _ in range(100):
        input = run_iter(input)
    return input

def repeat_input(input, num):
    repeated_input = []
    for _ in range(num):
        repeated_input += input
    return repeated_input

def zero_indices(numbers):
    return [i for i, x in enumerate(numbers) if x == 0]


def calc_full(input):
    full_output = repeat_input(input, 10000)

    return_position = int(print_full_output(input)[0:7])
    # We can start at the indicated position because all previous coefficients will be 0
    full_output = full_output[return_position:]
    zeros = None
    for i in range(100):
        pos = len(full_output) - 1
        sum = 0
        next = []
        while pos >= 0:
            sum = (sum + full_output[pos]) % 10
            next.append(sum)
            pos -= 1
        next.reverse()
        full_output = next
    return full_output

part_a = calc_sample(input)
print('part a:', print_output(part_a))
part_b = calc_full(input)
print('part b:', print_output(part_b))