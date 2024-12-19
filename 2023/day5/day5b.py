seeds = []
ranges = {}
range_mapping = {}
in_map = None
with open('day5_input.txt', 'r') as file:
    for line in file:
        if 'seeds' in line:
            seed_nums = [int(seed)
                         for seed in line.split(':')[1].strip().split(' ')]
            pos = 0
            while pos < len(seed_nums):
                seed_start = seed_nums[pos]
                seed_end = seed_start + seed_nums[pos + 1] - 1
                seeds.append([[seed_start, seed_end]])
                pos += 2

        elif 'map' in line:
            in_map = line.split(' ')[0]
            ranges[in_map] = []
            range_mapping[in_map] = {}
        elif len(line.strip()) == 0:
            in_map = None
        else:
            numbers = [int(num) for num in line.strip().split(' ')]
            dest_start = numbers[0]
            source_start = numbers[1]
            range_len = numbers[2]
            source_end = source_start + range_len - 1
            ranges[in_map].append([source_start, source_end])
            range_mapping[in_map][source_start] = dest_start


def get_mapping(values, map):
    output_values = []
    for value in values:
        seed_start = value[0]
        seed_end = value[1]
        min_range = None
        max_range = None
        for source_range in ranges[map]:
            source_start = source_range[0]
            source_end = source_range[1]
            if not min_range or min_range > source_start:
                min_range = source_start
            if not max_range or max_range < source_end:
                max_range = source_end
            dest_start = range_mapping[map][source_start]
            dest_end = dest_start + (source_end - source_start)
            offset = (dest_start - source_start)
            new_value = None
            if (seed_start < source_start and seed_end < source_start) or (seed_start > source_end and seed_end > source_end):
                continue
            elif source_start <= seed_start and source_end >= seed_end:
                new_value = [seed_start + offset, seed_end + offset]
            elif source_start <= seed_start and source_end < seed_end:
                new_value = [seed_start + offset, dest_end]
            elif source_start > seed_start and source_end >= seed_end:
                new_value = [dest_start, seed_end + offset]
            elif source_start > seed_start and source_end < seed_end:
                new_value = [dest_start, dest_end]
            output_values.append(new_value)
        if seed_start < min_range and seed_end >= min_range:
            output_values.append([seed_start, min_range - 1])
        if max_range < seed_end and max_range >= seed_start:
            output_values.append([max_range + 1, seed_end])

    if len(output_values) == 0:
        output_values = values
    return output_values


lowest_location = None
for seed in seeds:

    soil = get_mapping(seed, 'seed-to-soil')
    fertilizer = get_mapping(soil, 'soil-to-fertilizer')
    water = get_mapping(fertilizer, 'fertilizer-to-water')
    light = get_mapping(water, 'water-to-light')
    temp = get_mapping(light, 'light-to-temperature')
    humidity = get_mapping(temp, 'temperature-to-humidity')
    locations = get_mapping(humidity, 'humidity-to-location')

    for location in locations:
        start = location[0]
        if not lowest_location or start < lowest_location:
            lowest_location = start

print(lowest_location)
