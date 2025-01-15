orbits = {}
with open('day6_input.txt', 'r') as file:
    for line in file:
        line = line.strip()
        orbit, orbiter = line.split(')')
        orbits[orbiter] = orbit

def get_orbit_path(object):
    path = []
    node = orbits[object]
    path.append(node)
    while node in orbits:
        node = orbits[node]
        path.append(node)
    return path

you_orbit = get_orbit_path('YOU')
san_orbit = get_orbit_path('SAN')

for index, node in enumerate(you_orbit):
    if node in san_orbit:
        print('num transfers', index + san_orbit.index(node))
        break