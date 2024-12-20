times = []
distances = []
with open('day6_input.txt', 'r') as file:
    for index, line in enumerate(file):
        if index == 0:
            times = [int(time)
                     for time in line.strip().split(':')[1].strip().split(' ') if len(time) > 0]
        else:
            distances = [int(distance)
                         for distance in line.strip().split(':')[1].strip().split(' ') if len(distance) > 0]

total_possibilities = 1
for index, time in enumerate(times):
    num_beats = 0
    for candidate_time in range(1, time):
        if (time - candidate_time) * candidate_time > distances[index]:
            num_beats += 1
    if num_beats > 0:
        total_possibilities *= num_beats

print(total_possibilities)
