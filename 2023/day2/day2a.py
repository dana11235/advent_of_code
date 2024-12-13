sum = 0
maxes = {
    'red': 12,
    'green': 13,
    'blue': 14
}

with open('day2_input.txt', 'r') as file:
    for line in file:
        game, desc = line.split(':')
        game_number = int(game.split(' ')[1])
        valid = True
        trials = desc.split(';')
        for trial in trials:
            cubes = trial.split(',')
            for cube in cubes:
                num_str, color = cube.strip().split(' ')
                num = int(num_str)
                if num > maxes[color]:
                    valid = False
        if valid:
            sum += game_number
print(sum)
