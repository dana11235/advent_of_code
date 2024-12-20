time = None
distance = None
with open('day6_input.txt', 'r') as file:
    for index, line in enumerate(file):
        if index == 0:
            time = int(''.join([time
                                for time in line.strip().split(':')[1].strip().split(' ') if len(time) > 0]))
        else:
            distance = int(''.join([distance
                                    for distance in line.strip().split(':')[1].strip().split(' ') if len(distance) > 0]))


def get_value(candidate_time):
    return (time - candidate_time) * candidate_time


left_pointer = 0
right_pointer = time // 2
while (right_pointer - left_pointer) > 1:
    mid_pointer = (left_pointer + right_pointer) // 2
    value = get_value(mid_pointer)
    if value > distance:
        right_pointer = mid_pointer
    else:
        left_pointer = mid_pointer
lower_bound = right_pointer


left_pointer = time // 2
right_pointer = time
while right_pointer - left_pointer > 1:
    mid_pointer = (left_pointer + right_pointer) // 2
    value = get_value(mid_pointer)
    if value < distance:
        right_pointer = mid_pointer
    else:
        left_pointer = mid_pointer
upper_bound = left_pointer

print(upper_bound - lower_bound + 1)
