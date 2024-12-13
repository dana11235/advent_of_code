sum = 0

with open('day2_input.txt', 'r') as file:
    for line in file:
        game, desc = line.split(':')
        game_number = int(game.split(' ')[1])
        trials = desc.split(';')
        mins = {}
        for trial in trials:
            cubes = trial.split(',')
            for cube in cubes:
                num_str, color = cube.strip().split(' ')
                num = int(num_str)
                if color not in mins or num > mins[color]:
                    mins[color] = num
        power = 1
        for value in mins.values():
            power *= value
        sum += power
print(sum)
