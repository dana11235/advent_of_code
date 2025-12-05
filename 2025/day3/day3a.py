with open("input.txt", "r") as file:
    total = 0
    for line in file:
        line = [int(i) for i in list(line.strip())]
        first_digit = -1
        first_index = 0
        for index, i in enumerate(line[0:-1]):
            if i > first_digit:
                first_digit = i
                first_index = index
        second_digit = -1
        second_index = 0
        after_first = first_index + 1
        for index, i in enumerate(line[after_first:]):
            if i > second_digit:
                second_digit = i
                second_index = index
        max = int(f"{first_digit}{second_digit}")
        print(max)
        total += max

print("total", total)
