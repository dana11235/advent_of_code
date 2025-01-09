import math
total_fuel = 0
with open('day1_input.txt', 'r') as file:
    for line in file:
        mass = int(line.strip())
        total_fuel += math.trunc(mass / 3) - 2

print(total_fuel)
