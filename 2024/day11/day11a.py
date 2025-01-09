stones = []
with open('day11_input.txt', 'r') as file:
    for line in file:
        stones = [int(num) for num in line.strip().split()]
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


print(len(stones))
