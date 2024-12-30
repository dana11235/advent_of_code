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


def count_valid_solutions(springs, springs_to_add, start_index, solution):
    if springs_to_add == 0:
        if is_valid(springs, solution):
            return 1
        else:
            return 0
    else:
        solution_sum = 0
        for i in range(start_index, len(springs)):
            if springs[i] == '?':
                new_springs = springs.copy()
                new_springs[i] = '#'
                solution_sum += count_valid_solutions(
                    new_springs, springs_to_add - 1, i + 1, solution)
        return solution_sum


with open('day12_input.txt', 'r') as file:
    for line in file:
        springs, solution = line.strip().split(' ')
        springs = list(springs)
        solution = [int(piece) for piece in solution.split(',')]
        curr_springs = 0
        for index, place in enumerate(springs):
            if place == '#':
                curr_springs += 1

        solution_springs = 0
        for piece in solution:
            solution_springs += piece
        springs_to_add = solution_springs - curr_springs
        num_solutions = count_valid_solutions(
            springs, springs_to_add, 0, solution)
        combinations += num_solutions
print(combinations)
