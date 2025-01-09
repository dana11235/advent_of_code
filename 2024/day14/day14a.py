num_1 = 0
num_2 = 0
num_3 = 0
num_4 = 0
width = 101
height = 103
mid_w = 50
mid_h = 51
with open('day14_input.txt', 'r') as file:
    for line in file:
        parts = line.strip().split(' ')
        xpos, ypos = parts[0].split('=')[1].split(',')
        xvel, yvel = parts[1].split('=')[1].split(',')
        print(xpos, ypos, xvel, yvel)
        new_xpos = (int(xpos) + 100 * int(xvel)) % width
        new_ypos = (int(ypos) + 100 * int(yvel)) % height
        if new_xpos < mid_w and new_ypos < mid_h:
            num_1 += 1
        elif new_xpos > mid_w and new_ypos < mid_h:
            num_2 += 1
        elif new_xpos < mid_w and new_ypos > mid_h:
            num_3 += 1
        elif new_xpos > mid_w and new_ypos > mid_h:
            num_4 += 1
print(num_1, num_2, num_3, num_4, num_1 * num_2 * num_3 * num_4)
