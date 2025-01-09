import math
total_fuel = 0
with open('day1_input.txt', 'r') as file:
    for line in file:
        mass = int(line.strip())
        while mass > 0:
            mass = math.trunc(mass / 3) - 2
            if mass > 0:
                total_fuel += mass

print(total_fuel)
