combinations = 0


def is_valid(springs, solution):
    blocks = []
    curr_block = 0
    for place in springs:
        if place == '#':
            curr_block += 1
        elif place in ['.', '?']:
            if curr_block > 0:
                blocks.append(curr_block)
                curr_block = 0
    if curr_block > 0:
        blocks.append(curr_block)
    return blocks == solution


CACHE = {}


def count_valid_solutions(springs, index, group_index, num_in_group, solution):
    key = f"{index},{group_index},{num_in_group}"
    sol_sum = 0
    if key in CACHE:
        return CACHE[key]
    if index == len(springs) or group_index == len(solution):
        if is_valid(springs, solution):
            sol_sum = 1
        else:
            sol_sum = 0
    elif num_in_group > solution[group_index]:
        sol_sum = 0
    elif group_index > len(solution):
        sol_sum = 0
    else:
        if springs[index] == '?':
            dot = springs.copy()
            # Handle the case with the dot
            dot[index] = '.'
            # We add a new group if there is more than one in the existing group
            if num_in_group > 0:
                if num_in_group == solution[group_index]:
                    sol_sum += count_valid_solutions(dot,
                                                     index + 1, group_index + 1, 0, solution)
            else:
                sol_sum += count_valid_solutions(dot, index + 1,
                                                 group_index, num_in_group, solution)
            hash = springs.copy()
            # Handle the case with the hash
            hash[index] = '#'
            sol_sum += count_valid_solutions(hash, index + 1,
                                             group_index, num_in_group + 1, solution)
        elif springs[index] == '.':
            if num_in_group > 0:
                if num_in_group == solution[group_index]:
                    sol_sum += count_valid_solutions(springs, index + 1,
                                                     group_index + 1, 0, solution)
            else:
                sol_sum += count_valid_solutions(springs, index + 1,
                                                 group_index, num_in_group, solution)
        elif springs[index] == '#':
            sol_sum += count_valid_solutions(springs, index + 1,
                                             group_index, num_in_group + 1, solution)
    CACHE[key] = sol_sum
    return sol_sum


with open('day12_input.txt', 'r') as file:
    for line in file:
        # We need to clear the cache each timt to prevent old solutions from impacting the curr solution
        CACHE = {}
        springs, solution = line.strip().split(' ')
        partial_springs = list(springs)
        partial_solution = [int(piece) for piece in solution.split(',')]

        springs = []
        solution = []
        # Create the full springs and solution from the partial provided
        for i in range(5):
            springs += partial_springs
            if i < 4:
                springs += '?'
            solution += partial_solution

        num_solutions = count_valid_solutions(
            springs, 0, 0, 0, solution)
        combinations += num_solutions
print(combinations)
