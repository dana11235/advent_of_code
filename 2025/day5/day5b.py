ranges = {}
range_starts = []
in_ranges = True
with open("input.txt", "r") as file:
    for index, line in enumerate(file):
        line = line.strip()
        if not line:
            break
        else:
            first, last = [int(num) for num in line.split("-")]
            if first not in ranges:
                ranges[first] = last
                range_starts.append(first)
            elif last > ranges[first]:
                ranges[first] = last

range_starts.sort()
skip_indices = []


def find_end(index):
    curr_start = range_starts[index]
    curr_end = ranges[curr_start]

    step = 1
    while True:
        next_index = index + step
        if next_index > len(range_starts) - 1:
            return curr_end + 1
        next_start = range_starts[next_index]
        next_end = ranges[next_start]
        if next_start > curr_end:
            return curr_end + 1
        elif next_start <= curr_end and next_end > curr_end:
            return next_start
        else:
            skip_indices.append(next_index)
            step += 1


num_fresh = 0
for index, start in enumerate(range_starts):
    if index in skip_indices:
        continue
    end = find_end(index)
    num_fresh += end - start

print("fresh", num_fresh)
