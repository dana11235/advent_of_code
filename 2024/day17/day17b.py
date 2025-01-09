import math
import sys

ORIG_REG_A = -1
ORIG_REG_B = -1
ORIG_REG_C = -1
INSTRUCTIONS = []
INSTRUCTIONS_STR = ""


def stringify(input):
    return ",".join([str(num) for num in input])


with open('day17_input.txt', 'r') as file:
    for row_index, line in enumerate(file):
        if row_index == 0:
            ORIG_REG_A = int(line.split(':')[1])
        elif row_index == 1:
            ORIG_REG_B = int(line.split(':')[1])
        elif row_index == 2:
            ORIG_REG_C = int(line.split(':')[1])
        elif row_index == 4:
            INSTRUCTIONS = [int(num)
                            for num in line.split(':')[1].strip().split(',')]
            INSTRUCTIONS_STR = stringify(INSTRUCTIONS)


def get_operand_value(operand, opcode, registers):
    if opcode in [1, 3, 4]:
        return operand
    else:
        if operand in [0, 1, 2, 3]:
            return operand
        elif operand == 4:
            return registers['A']
        elif operand == 5:
            return registers['B']
        elif operand == 6:
            return registers['C']


def get_output(input):
    registers = {
        'A': input,
        'B': ORIG_REG_B,
        'C': ORIG_REG_C
    }
    INSTR_PTR = 0
    OUTPUT = []
    while INSTR_PTR < len(INSTRUCTIONS):
        opcode = INSTRUCTIONS[INSTR_PTR]
        operand = get_operand_value(
            INSTRUCTIONS[INSTR_PTR + 1], opcode, registers)
        if opcode == 0:
            registers['A'] = math.trunc(registers['A'] / math.pow(2, operand))
        elif opcode == 6:
            registers['B'] = math.trunc(registers['A'] / math.pow(2, operand))
        elif opcode == 7:
            registers['C'] = math.trunc(registers['A'] / math.pow(2, operand))
        elif opcode == 1:
            registers['B'] = registers['B'] ^ operand
        elif opcode == 2:
            registers['B'] = operand % 8
        elif opcode == 3:
            if registers['A'] != 0:
                INSTR_PTR = operand
                continue
        elif opcode == 4:
            registers['B'] = registers['B'] ^ registers['C']
        elif opcode == 5:
            OUTPUT.append(operand % 8)
        INSTR_PTR += 2

    return OUTPUT


num_instructions = len(INSTRUCTIONS)


def find_matches(input):
    output = get_output(input)
    matches = 0
    broken = False
    for index, num in enumerate(output):
        if num_instructions > index and INSTRUCTIONS[index] == num:
            if not broken:
                matches += 1
            output[index] = f"[{num}]"
        else:
            broken = True
            output[index] = str(num)

    return [output, matches]


def get_iter(x):
    xp = (x % 8) ^ 3
    divisor = math.pow(2, xp)
    y = 5 ^ (xp ^ math.trunc((x / math.pow(2, xp))))
    return [math.trunc(x / 8), y % 8, divisor]


# Generates suffixes, 3 numbers at a time, recursively
def generate_combos(suffix, index):
    used_suffixes = []
    if index < len(INSTRUCTIONS) - 1:
        for prefix in range(int('100000000000000000', 2), int('111111111111111111', 2) + 1):
            binary_prefix = bin(prefix)[2:]
            number = binary_prefix + suffix
            _, matches = find_matches(int(number, 2))
            new_suffix = binary_prefix[-9:] + suffix
            if matches == index + 3 and new_suffix not in used_suffixes:
                used_suffixes.append(new_suffix)
                result = generate_combos(new_suffix, index + 3)
                if len(result) > 0:
                    return result
        return ''
    else:
        return suffix


answer = generate_combos('', 0)
# Now that we have an answer to the first 15 digits, find the lowest first 18 numbers that satisfy us
if answer:
    suffix = answer[-30:]
    for prefix in range(int('111111111111111111', 2) + 1):
        number = bin(prefix)[2:] + suffix
        _, matches = find_matches(int(number, 2))
        if matches == len(INSTRUCTIONS):
            print('result', number, int(number, 2))
            break
else:
    print('not found')
