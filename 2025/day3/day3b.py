with open("input.txt", "r") as file:
    n = 12
    total = 0
    for line in file:
        line = [int(i) for i in list(line.strip())]
        digits = 0
        curr_index = 0
        for num in range(-n + 1, 1, 1):
            curr_digit = -1
            curr_num = num
            if num == 0:
                curr_num = None
            sel_index = -1
            for index, i in enumerate(line[curr_index:curr_num]):
                if i > curr_digit:
                    curr_digit = i
                    sel_index = index
            curr_index += sel_index + 1
            digits = digits * 10 + curr_digit
        total += digits

print("total", total)
