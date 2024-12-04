num_safe = 0
with open('day2_input.txt', 'r') as file:
    for line in file:
        parts = line.split()
        dir = int(parts[1]) - int(parts[0])

        for index, value in enumerate(parts):
            if index == 0:
                continue
            diff = int(parts[index]) - int(parts[index - 1])
            if diff == 0:
                break
            elif diff > 0 and dir < 0:
                break
            elif diff < 0 and dir > 0:
                break
            elif abs(diff) > 3:
                break
            if index == len(parts) - 1:
                # print('safe', line)
                num_safe += 1
print('ns', num_safe)