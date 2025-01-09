with open('day13_input.txt', 'r') as file:
    cost = 0
    button_a = None
    button_b = None
    prize = None
    for line_num, line in enumerate(file):
        if line_num % 4 == 0:
            moves = line.split(":")[1].strip()
            x, y = moves.split(',')
            button_a = {'x': int(x.split("+")[1]), 'y': int(y.split("+")[1])}
        elif line_num % 4 == 1:
            moves = line.split(":")[1].strip()
            x, y = moves.split(',')
            button_b = {'x': int(x.split("+")[1]), 'y': int(y.split("+")[1])}
        elif line_num % 4 == 2:
            print('hi')
            moves = line.split(":")[1].strip()
            x, y = moves.split(',')
            prize = {'x': int(x.split("=")[1]), 'y': int(y.split("=")[1])}
            solved = False
            for i in range(0, 101):
                for j in range(0, 101):
                    if i*button_a['x'] + j*button_b['x'] == prize['x'] and i*button_a['y'] + j*button_b['y'] == prize['y']:
                        solved = True
                        print('solved', i, j)
                        cost += (3 * i + j)
            print(prize, solved)
print(cost)
