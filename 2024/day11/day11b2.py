initial_stones = []
with open('day11_input.txt', 'r') as file:
    for line in file:
        initial_stones = [int(num) for num in line.strip().split()]

cache = {}


def run_iter(start_stones, iter):
    if iter == 0:
        return len(start_stones)

    stones = start_stones.copy()
    index = 0
    while index < len(stones):
        num = stones[index]
        str_num = str(num)
        if num == 0:
            stones[index] = 1
        elif len(str_num) % 2 == 0:
            half = int(len(str_num) / 2)
            stone1 = str_num[0:half]
            stone2 = str_num[half:]
            stones[index] = int(stone2)
            stones.insert(index, int(stone1))
            index += 1
        else:
            stones[index] *= 2024
        index += 1

    num_stones = 0
    next_iter = iter - 1
    for stone in stones:
        if stone in cache and next_iter in cache[stone]:
            num_stones += cache[stone][next_iter]
        else:
            iter_stones = run_iter([stone], next_iter)
            if stone not in cache:
                cache[stone] = {}
            cache[stone][next_iter] = iter_stones
            num_stones += iter_stones
    return num_stones


total_count = run_iter(initial_stones, 75)

print(total_count)
