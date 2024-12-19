seeds = []
ranges = {}
range_mapping = {}
in_map = None
with open('day5_input.txt', 'r') as file:
    for line in file:
        if 'seeds' in line:
            seeds = [int(seed)
                     for seed in line.split(':')[1].strip().split(' ')]
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


def get_mapping(value, map):
    for source_range in ranges[map]:
        source_start = source_range[0]
        if value >= source_start and value <= source_range[1]:
            dest_start = range_mapping[map][source_start]
            return value - source_start + dest_start
    return value


lowest_location = None
for seed in seeds:

    soil = get_mapping(seed, 'seed-to-soil')
    fertilizer = get_mapping(soil, 'soil-to-fertilizer')
    water = get_mapping(fertilizer, 'fertilizer-to-water')
    light = get_mapping(water, 'water-to-light')
    temp = get_mapping(light, 'light-to-temperature')
    humidity = get_mapping(temp, 'temperature-to-humidity')
    location = get_mapping(humidity, 'humidity-to-location')

    if not lowest_location or location < lowest_location:
        lowest_location = location

print(lowest_location)
