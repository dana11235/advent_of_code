import os
import sys
here = os.path.dirname(__file__)
sys.path.append(os.path.join(here, '..'))
from intcode import run_program
INPUT_OPS = []
with open('day13_input.txt', 'r') as file:
    for line in file:
        line = line.strip()
        INPUT_OPS += [int(code) for code in line.split(',')]

def run_frame(OPS, input, index, rel_base):
    finished = False
    rel_base = 0
    index = 0
    finished, output, index, OPS, rel_base = run_program(OPS, input, index, rel_base)
    return finished, output, index, OPS, rel_base

CHARS = {
    0: ' ',
    1: '|',
    2: '#',
    3: '_',
    4: 'o'
}

def parse_screen(input, render):
    SCREEN = {}
    index = 0
    paddle = None
    ball = None
    score = None
    num_blocks = 0
    while index < len(input):
        x_pos = input[index]
        y_pos = input[index + 1]
        id = input[index + 2]
        # Handle getting the score
        if x_pos == -1 and y_pos == 0:
            score = id
        else:
            if id == 2:
                num_blocks += 1
            elif id == 3:
                paddle = x_pos
            elif id == 4:
                ball = x_pos
            if render:
                if y_pos not in SCREEN:
                    SCREEN[y_pos] = {}
                SCREEN[y_pos][x_pos] = id
        index += 3

    if render:
        for y, row in enumerate(SCREEN.values()):
            output = []
            for x, pixel in enumerate(row.values()):
                output.append(CHARS[pixel])
            print(''.join(output))
        print('score:', score)
        print('ball:', ball)
        print('paddle:', paddle)
    
    return num_blocks, score, paddle, ball

def run_game():
    game_ops = INPUT_OPS.copy()

    game_ops[0] = 2
    finished = False
    index = 0
    rel_base = 0
    joy_pos = [0]
    while not finished:
        finished, output, index, game_ops, rel_base = run_frame(game_ops, joy_pos, index, rel_base)
        _, score, paddle, ball = parse_screen(output, False)
        if ball < paddle:
            joy_pos = [-1]
        elif ball > paddle:
            joy_pos = [1]
        else:
            joy_pos = [0]

        if finished:
            return score


_, output, _, _, _ = run_frame(INPUT_OPS.copy(), [], 0, 0)
num_blocks, _, _, _ = parse_screen(output, False)
print('part a:', num_blocks)
score = run_game()
print('part b:', score)