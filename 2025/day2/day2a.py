with open("input.txt", "r") as file:
    total = 0
    for line in file:
        line = line.strip()
        for number in line.split(","):
            if len(number) == 0:
                continue
            min, max = number.split("-")
            num_min = int(min)
            num_max = int(max)
            print(num_min, num_max)
            for i in range(num_min, num_max + 1):
                str_i = str(i)
                digits = len(str_i)
                if digits % 2 == 0:
                    half = digits // 2
                    if str_i[0:half] == str_i[half:]:
                        curr_num = i
                        print("T", curr_num)
                        total += curr_num
print("total", total)
