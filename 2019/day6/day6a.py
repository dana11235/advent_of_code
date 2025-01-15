orbits = {}
with open('day6_input.txt', 'r') as file:
    for line in file:
        line = line.strip()
        orbit, orbiter = line.split(')')
        orbits[orbiter] = orbit

num_orbits = 0
for key in list(orbits.keys()):
    curr_orbits = 1 
    value = orbits[key]
    while value in orbits:
        curr_orbits += 1
        value = orbits[value]
    num_orbits += curr_orbits
print(num_orbits)