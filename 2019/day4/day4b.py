low = None
high = None
with open('day4_input.txt', 'r') as file:
    for line in file:
        line = line.strip()
        low, high = [int(num) for num in line.split('-')]

num_passwords = 0
for i in range(low + 1, high + 1):
    num_doubles = 0
    string_num = list(str(i))
    is_increasing = True
    run_len = 1
    for index, digit in enumerate(string_num):
        prev_digit = int(string_num[index - 1])
        if index > 0:
            if int(digit) == prev_digit:
                run_len += 1
            else:
                if run_len == 2:
                    num_doubles += 1
                run_len = 1
            if int(digit) < prev_digit:
                is_increasing = False
    if run_len == 2:
        num_doubles += 1
    if num_doubles >= 1 and is_increasing == True:
        num_passwords += 1

print(num_passwords)
