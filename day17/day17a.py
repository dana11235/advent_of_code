import math

REG_A = -1
REG_B = -1
REG_C = -1
INSTRUCTIONS = []
INSTR_PTR = 0
OUTPUT = []

with open('day17_input.txt', 'r') as file:
    for row_index, line in enumerate(file):
        if row_index == 0:
            REG_A = int(line.split(':')[1])
        elif row_index == 1:
            REG_B = int(line.split(':')[1])
        elif row_index == 2:
            REG_C = int(line.split(':')[1])
        elif row_index == 4:
            INSTRUCTIONS = [int(num)
                            for num in line.split(':')[1].strip().split(',')]


def get_operand_value(operand, opcode):
    if opcode in [1, 3, 4]:
        return operand
    else:
        if operand in [0, 1, 2, 3]:
            return operand
        elif operand == 4:
            return REG_A
        elif operand == 5:
            return REG_B
        elif operand == 6:
            return REG_C


while INSTR_PTR < len(INSTRUCTIONS):
    opcode = INSTRUCTIONS[INSTR_PTR]
    operand = get_operand_value(INSTRUCTIONS[INSTR_PTR + 1], opcode)
    print(opcode, operand)
    if opcode == 0:
        REG_A = math.trunc(REG_A / math.pow(2, operand))
    elif opcode == 6:
        REG_B = math.trunc(REG_A / math.pow(2, operand))
    elif opcode == 7:
        REG_C = math.trunc(REG_A / math.pow(2, operand))
    elif opcode == 1:
        REG_B = REG_B ^ operand
    elif opcode == 2:
        REG_B = operand % 8
    elif opcode == 3:
        if REG_A != 0:
            INSTR_PTR = operand
            continue
    elif opcode == 4:
        REG_B = REG_B ^ REG_C
    elif opcode == 5:
        OUTPUT.append(operand % 8)
    INSTR_PTR += 2

print(",".join([str(num) for num in OUTPUT]))
