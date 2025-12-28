import numpy
from scipy.optimize import linprog

TOTAL = 0
with open("input.txt", "r") as file:
    for line in file:
        line = line.strip()
        print(line)
        pieces = line.split(" ")
        lights = []
        buttons = []
        joltage = []
        for piece in pieces:
            if piece[0] == "[":
                for light in piece[1:-1]:
                    if light == ".":
                        lights.append(0)
                    else:
                        lights.append(1)
            elif piece[0] == "(":
                curr_button = numpy.zeros(len(lights))
                for effect in piece[1:-1].split(","):
                    curr_button[int(effect)] = 1
                buttons.append(curr_button)
            elif piece[0] == "{":
                joltage = [int(effect) for effect in piece[1:-1].split(",")]

        c = [int(x) for x in numpy.ones(len(buttons))]
        A_eq = []
        b_eq = joltage
        for index, val in enumerate(joltage):
            curr_vals = []
            for button in buttons:
                if button[index] == 1:
                    curr_vals.append(1)
                else:
                    curr_vals.append(0)
            A_eq.append(curr_vals)

        x_bounds = (0, None)
        bounds = [x_bounds for n in range(len(buttons))]

        # 1 = Integer constraint, 0 = Continuous
        integrality = [1 for n in range(len(buttons))]

        res = linprog(
            c,
            A_eq=A_eq,
            b_eq=b_eq,
            bounds=bounds,
            integrality=integrality,
            method="highs",
        )

        print("Optimal value:", res.fun)
        TOTAL += int(res.fun)

print("total", TOTAL)
