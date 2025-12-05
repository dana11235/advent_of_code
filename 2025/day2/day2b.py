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
                digits = len(str(i))
                for num_groups in range(2, digits + 1):
                    str_i = str(i)
                    if (digits % num_groups) == 0:
                        size = digits // num_groups
                        groups = []
                        while len(str_i) > 0:
                            groups.append(str_i[0:size])
                            str_i = str_i[size:]
                        is_bad = True
                        for group_i in range(len(groups)):
                            if groups[group_i] != groups[0]:
                                is_bad = False
                                break
                        if is_bad and len(groups) > 0:
                            total += i
                            break

print("total", total)
