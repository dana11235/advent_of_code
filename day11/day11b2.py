initial_stones = []
with open('day11_input.txt', 'r') as file:
    for line in file:
        initial_stones = [int(num) for num in line.strip().split()]


def freqs(stones):
    freqs = {}
    for stone in stones:
        if stone not in freqs:
            freqs[stone] = 1
        else:
            freqs[stone] += 1
    return freqs


def run_iter(start_stones):
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
    return stones


runs = [freqs(initial_stones)]
for i in range(74):
    start_stones = list(runs[i].keys())
    next_stones = run_iter(start_stones)
    runs.append(freqs(next_stones))

for stone in runs[73].keys():
    runs[73][stone] *= len(run_iter([stone]))

index = 72
while index >= 0:
    for stone in runs[index].keys():
        runs[index][stone] *= runs[index + 1][stone]
    index -= 1

total_count = sum(runs[0].values())

print(total_count)
