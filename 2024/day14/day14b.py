import sys
import time

width = 101
height = 103


def run_loop():
    hashes = []
    for iter in range(0, 10403):
        hash = 0
        grid = []
        for i in range(height):
            row = []
            for j in range(width):
                row.append(' ')
            grid.append(row)

        with open('day14_input.txt', 'r') as file:
            for line in file:
                parts = line.strip().split(' ')
                xpos, ypos = parts[0].split('=')[1].split(',')
                xvel, yvel = parts[1].split('=')[1].split(',')
                new_xpos = (int(xpos) + iter * int(xvel)) % width
                new_ypos = (int(ypos) + iter * int(yvel)) % height
                grid[new_ypos][new_xpos] = '*'
                hash += new_ypos * width + new_xpos
        if hash in hashes:
            print(hashes.index(hash), iter)
            break
        hashes.append(hash)


def run_one(iter):
    grid = []
    for i in range(height):
        row = []
        for j in range(width):
            row.append(' ')
        grid.append(row)

    with open('day14_input.txt', 'r') as file:
        for line in file:
            parts = line.strip().split(' ')
            xpos, ypos = parts[0].split('=')[1].split(',')
            xvel, yvel = parts[1].split('=')[1].split(',')
            new_xpos = (int(xpos) + iter * int(xvel)) % width
            new_ypos = (int(ypos) + iter * int(yvel)) % height
            grid[new_ypos][new_xpos] = '*'
        for line in grid:
            print(''.join(line))


# These slopes bisect the rectangle at the bottom corners and top middle
slope_a = -103 / 50
slope_b = 103 / 50


def find_tree():
    for iter in range(0, 10403):
        grid = []
        for i in range(height):
            row = []
            for j in range(width):
                row.append(' ')
            grid.append(row)

        with open('day14_input.txt', 'r') as file:
            inp = 0
            outp = 0
            for line in file:
                parts = line.strip().split(' ')
                xpos, ypos = parts[0].split('=')[1].split(',')
                xvel, yvel = parts[1].split('=')[1].split(',')
                new_xpos = (int(xpos) + iter * int(xvel)) % width
                new_ypos = (int(ypos) + iter * int(yvel)) % height
                grid[new_ypos][new_xpos] = '*'
                if new_xpos == 50:
                    inp += 1
                    continue
                # I compared the slope of the point to the other slopes
                slope = (-1 * new_ypos)/(50 - new_xpos)
                if new_xpos == 50 or slope < slope_a or slope > slope_b:
                    inp += 1
                else:
                    outp += 1
            # I made the assumption that most of the points would lie
            # in the middle of the screen when we draw the tree.
            if (inp / (inp + outp)) > 0.77:
                for line in grid:
                    print(''.join(line))
                print(iter)


find_tree()
