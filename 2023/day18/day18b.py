import heapq
import random
DIRS = {
    '0': [0, 1],
    '2': [0, -1],
    '3': [-1, 0],
    '1': [1, 0]
}

dir_lookup = ['R', 'D', 'L', 'U']

SEGMENTS = []
heapq.heapify(SEGMENTS)

vertical_sum = 0
start_pos = [0, 0]
with open('day18_input.txt', 'r') as file:
    for line in file:
        line = line.strip()
        dir, number, rgb = line.split(' ')
        # Uncomment the next 2 lines and comment the 2 lines after that to run part a
        # dir = str(dir_lookup.index(dir))
        # number = int(number)
        dir = rgb[7]
        number = int(rgb[2:-2], 16)
        end_pos = [start_pos[0] + DIRS[dir][0] * number,
                   start_pos[1] + DIRS[dir][1] * number]
        # We only consider the horizontal segments for considering the internal area
        # Put them on a priority queue, which enables us to calculate from top down
        if dir == '0':
            heapq.heappush(SEGMENTS, (start_pos[0], random.random(), [
                           start_pos[1], end_pos[1]]))
        elif dir == '2':
            heapq.heappush(SEGMENTS, (start_pos[0], random.random(), [
                           end_pos[1], start_pos[1]]))
        else:
            # We need to consider the sum of the vertical segments for the edge
            vertical_sum += number

        start_pos = end_pos

area = 0
ACTIVE_SEGMENTS = []
while len(SEGMENTS) > 0:
    end_y, _, end_range = heapq.heappop(SEGMENTS)
    segment_index = 0
    closed_segments = False
    while segment_index < len(ACTIVE_SEGMENTS):
        num_added = 0
        active_segment = ACTIVE_SEGMENTS[segment_index]
        start_y = active_segment['start_y']
        start_range = active_segment['range']

        y_diff = end_y - start_y + 1
        # We consider various cases where the start and candidate end ranges overlap
        # If they do overlap, we may still have one or two remaining sub-segments from the
        # start range to add back to the list of active segments
        if start_range[0] <= end_range[0] and start_range[1] >= end_range[1]:
            # Whole overlap
            closed_segments = True
            ACTIVE_SEGMENTS.pop(segment_index)
            x_diff = end_range[1] - end_range[0]
            if start_range[0] < end_range[0]:
                new_range_1 = [start_range[0], end_range[0]]
                ACTIVE_SEGMENTS.insert(
                    segment_index, {'start_y': start_y, 'range': new_range_1})
                num_added += 1
            if start_range[1] > end_range[1]:
                new_range_2 = [end_range[1], start_range[1]]
                ACTIVE_SEGMENTS.insert(
                    segment_index, {'start_y': start_y, 'range': new_range_2})
                num_added += 1
            polygon_size = y_diff * x_diff
            area += polygon_size
        elif start_range[0] > end_range[0] and start_range[1] < end_range[1]:
            # Whole overlap
            closed_segments = True
            ACTIVE_SEGMENTS.pop(segment_index)
            x_diff = start_range[1] - start_range[0]
            polygon_size = y_diff * x_diff
            area += polygon_size
        elif start_range[0] <= end_range[0] and start_range[1] > end_range[0] and start_range[1] < end_range[1]:
            # Left Overlaps with right
            closed_segments = True
            ACTIVE_SEGMENTS.pop(segment_index)
            x_diff = start_range[1] - end_range[0]
            if start_range[0] < end_range[0]:
                new_range = [start_range[0], end_range[0]]
                ACTIVE_SEGMENTS.insert(
                    segment_index, {'start_y': start_y, 'range': new_range})
                num_added += 1
            polygon_size = y_diff * x_diff
            area += polygon_size
        elif start_range[0] > end_range[0] and start_range[0] < end_range[1] and start_range[1] >= end_range[1]:
            # Left Overlaps with right
            closed_segments = True
            ACTIVE_SEGMENTS.pop(segment_index)
            x_diff = end_range[1] - start_range[0]
            if start_range[1] > end_range[0] and end_range[1] < start_range[1]:
                new_range = [end_range[1], start_range[1]]
                ACTIVE_SEGMENTS.insert(
                    segment_index, {'start_y': start_y, 'range': new_range})
                num_added += 1
            polygon_size = y_diff * x_diff
            area += polygon_size
        else:
            segment_index += 1
        if num_added == 1:
            segment_index += 1
        elif num_added == 2:
            segment_index += 2
    # If we didn't close any segments, then this is a starting segment
    if not closed_segments:
        ACTIVE_SEGMENTS.append({'start_y': end_y, 'range': end_range})

# Since there are two edges to each segment, divide by 2
# We then need to add 1 to account for the height of the first line
print(area + round(vertical_sum/2) + 1)
