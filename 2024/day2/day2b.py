def is_safe(parts):
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
            return True
    return False


num_safe = 0
with open('day2_input.txt', 'r') as file:
    for line in file:
        parts = line.split()
        if is_safe(parts):
            num_safe += 1
        else:
            for index, value in enumerate(parts):
                if is_safe(parts[0:index] + parts[index + 1:]):
                    num_safe += 1
                    break
print('ns', num_safe)