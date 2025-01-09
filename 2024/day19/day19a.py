in_pieces = True
pieces = []
patterns = []
pattern_cache = {}
num_possible = 0


def can_build(pattern):
    if len(pattern) == 0:
        return True
    elif pattern in pattern_cache:
        return pattern_cache[pattern]
    else:
        for piece in pieces:
            if piece in pattern and pattern.index(piece) == 0:
                result = can_build(pattern[len(piece):])
                pattern_cache[pattern] = result
                if result:
                    return True
        pattern_cache[pattern] = False
        return False


with open('day19_input.txt', 'r') as file:
    for line in file:
        if len(line.strip()) == 0:
            in_pieces = False
        elif in_pieces:
            for piece in line.strip().split(','):
                pieces.append(piece.strip())
        else:
            patterns.append(line.strip())

for pattern in patterns:
    if can_build(pattern):
        print('built', pattern)
        num_possible += 1

print('possible', num_possible)
