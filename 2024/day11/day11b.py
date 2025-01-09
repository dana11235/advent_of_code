initial_stones = []
with open('day11_input.txt', 'r') as file:
    for line in file:
        initial_stones = [int(num) for num in line.strip().split()]


def run25(input_stones):
    stones = input_stones.copy()
    for i in range(25):
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
    return stones


f25_stones = run25(initial_stones)
print('f25', len(f25_stones))

freqs = {}
for stone in f25_stones:
    if stone not in freqs:
        freqs[stone] = 1
    else:
        freqs[stone] += 1


next25 = {}
cached = {}
for key in freqs.keys():
    expansion = run25([key])
    next25[key] = expansion
    cached[key] = len(expansion)
print(cached)

total_count = 0
for key in next25.keys():
    values = next25[key]
    key_count = 0
    for value in values:
        if value not in cached:
            expansion = run25([value])
            cached[value] = len(expansion)
        key_count += cached[value]
    total_count += freqs[key] * key_count

print(total_count)
