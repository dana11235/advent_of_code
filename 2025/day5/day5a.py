nums = []
ranges = {}
in_ranges = True
with open("input.txt", "r") as file:
    for line in file:
        line = line.strip()
        if not line:
            in_ranges = False
        elif in_ranges:
            first, last = [int(num) for num in line.split("-")]
            if first not in ranges or ranges[first] < last:
                ranges[first] = last
        else:
            nums.append(int(line))


num_fresh = 0
for num in nums:
    for start, end in ranges.items():
        if num >= start and num <= end:
            num_fresh += 1
            break

print("fresh", num_fresh)
