import json
GATES = {}
LOGIC = []
mode = 'gates'
# I modified the input file as I made fixes. I could alternatively use a dict to store substitutions
with open('day24_input_fixed.txt', 'r') as file:
    for line in file:
        if len(line.strip()) == 0:
            mode = 'logic'
        elif mode == 'gates':
            gate, value = line.strip().split(':')
            GATES[gate] = int(value.strip())
        elif mode == 'logic':
            LOGIC.append(line.strip().split(' '))

MAPPED = {}

# Here were the swaps I had to make
# (z06,hwk)
# (tnt,qmd)
# (hpc,z31)
# (z37,cgr)


def get_pieces(input_1, input_2):
    first = input_1.split('_')
    first[1] = int(first[1])
    second = input_2.split('_')
    second[1] = int(second[1])
    if first[1] < second[1] or first[0] < second[0]:
        return [first, second]
    else:
        return [second, first]

# I went through and figured out the operations needed to add two bits (including the carry from previous bits)
# Here were the operations (other than a simple AND or XOR of corresponding X and Y bits)

# FIRST_OP - SECOND_OP(previous) AND XOR(current)


def is_first_op(operation, pieces):
    return operation == 'AND' and pieces[0][0] == 'SECONDOP' and pieces[1][0] == 'XOR' and pieces[0][1] + \
        1 == pieces[1][1]


# SECOND_OP - FIRST_OP(current) OR AND(current)
def is_second_op(operation, pieces):
    return operation == 'OR' and pieces[0][0] == 'AND' and pieces[1][0] == 'FIRSTOP' and pieces[0][1] == pieces[1][1]


# Z - SECOND_OP(current) XOR XOR(next)
def is_z(operation, pieces):
    return operation == 'XOR' and pieces[0][0] == 'SECONDOP' and pieces[1][0] == 'XOR' and pieces[0][1] + 1 == pieces[1][1]


# We had to special case the first z and first first_op since they were degenerate and had fewer inputs
def is_z1(operation, pieces):
    return operation == 'XOR' and pieces[0][0] == 'AND' and pieces[1][0] == 'XOR' and pieces[0][1] == 0


def is_first_op_1(operation, pieces):
    return operation == 'AND' and pieces[0][0] == 'AND' and pieces[1][0] == 'XOR' and pieces[0][1] == 0


last = None
# Go through the operations, mapping each set of gate to the operations
while len(LOGIC) > 0:
    current = len(LOGIC)
    # This will break if it can't map any more operations
    if last and last == current:
        print(current)
        break
    last = current
    for line in LOGIC:
        label_1 = line[0]
        operation = line[1]
        label_2 = line[2]
        output = line[4]
        if label_1[1:] == label_2[1:]:
            MAPPED[output] = f"{operation}_{label_1[1:]}"
            LOGIC.remove(line)
        elif line[0] in MAPPED and line[2] in MAPPED:
            input_1 = MAPPED[label_1]
            input_2 = MAPPED[label_2]
            pieces = get_pieces(input_1, input_2)
            if is_z1(operation, pieces):
                MAPPED[output] = 'Z_1'
            elif is_first_op_1(operation, pieces):
                MAPPED[output] = 'FIRSTOP_1'
            elif is_first_op(operation, pieces):
                MAPPED[output] = f"FIRSTOP_{pieces[1][1]}"
            elif is_second_op(operation, pieces):
                MAPPED[output] = f"SECONDOP_{pieces[1][1]}"
            elif is_z(operation, pieces):
                MAPPED[output] = f"Z_{pieces[1][1]}"
            else:
                print('can\'t map', input_1, operation, input_2, output)
                print(pieces[0], operation, pieces[1], output)
            LOGIC.remove(line)
mapping_vals = list(MAPPED.values())
mapping_keys = list(MAPPED.keys())
sorted_mapping_vals = mapping_vals.copy()
sorted_mapping_vals.sort()
# When this breaks, the mapping will give us a hint as to what to fix
for line in sorted_mapping_vals:
    print(line, mapping_keys[mapping_vals.index(line)])

# If we get to the end without it breaking, we had done the right substitutions
