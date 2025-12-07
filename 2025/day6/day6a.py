problems = []
with open("input.txt", "r") as file:
    for line in file:
        nums = []
        curr_num = ""
        line = line.strip()
        for char in line:
            if char == " ":
                if curr_num:
                    nums.append(curr_num)
                    curr_num = ""
            else:
                curr_num += char
        if curr_num:
            nums.append(curr_num)
        problems.append(nums)

operations = problems[-1]
combinations = []
for i, row in enumerate(problems):
    if i == len(problems) - 1:
        break
    for index, num in enumerate(row):
        if len(combinations) < index + 1:
            combinations.append(int(num))
        else:
            if operations[index] == "+":
                combinations[index] += int(num)
            else:
                combinations[index] *= int(num)

total = sum(combinations)

print("total", total)
