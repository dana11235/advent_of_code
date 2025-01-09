import numpy
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
            moves = line.split(":")[1].strip()
            x, y = moves.split(',')
            prize = {'x': int(
                x.split("=")[1]) + 10000000000000, 'y': int(y.split("=")[1]) + 10000000000000}
            A = numpy.array([
                [button_a['x'], button_b['x']],
                [button_a['y'], button_b['y']]
            ])
            B = numpy.array([[prize['x']], [prize['y']]])
            AT = numpy.linalg.inv(A)
            solution = numpy.matmul(AT, B)
            if round(solution.item(0)) == round(solution.item(0), 2) and round(solution.item(1)) == round(solution.item(1), 2):
                cost += (round(solution.item(0)) * 3 + round(solution.item(1)))

print(cost)
