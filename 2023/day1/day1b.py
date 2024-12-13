import re

nums = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}


def numz(input):
    if input in nums:
        return nums[input]
    else:
        return input


sum = 0
with open('day1_input.txt', 'r') as file:
    for line in file:
        results = re.findall(
            "(?=([0-9]|one|two|three|four|five|six|seven|eight|nine))", line)
        curr_num = int(numz(results[0]) + numz(results[-1]))
        print(line, results, curr_num)
        sum += curr_num
print(sum)
