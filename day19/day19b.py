in_pieces = True
pieces = []
patterns = []
pattern_cache = {}
num_possible = 0


def can_build(pattern):
    if len(pattern) == 0:
        return 1
    elif pattern in pattern_cache:
        return pattern_cache[pattern]
    else:
        variants = 0
        for piece in pieces:
            if piece in pattern and pattern.index(piece) == 0:
                remainder = pattern[len(piece):]
                pattern_cache[remainder] = can_build(remainder)
                variants += pattern_cache[remainder]
        pattern_cache[pattern] = 0
        return variants


with open('day19_input.txt', 'r') as file:
    for line in file:
        if len(line.strip()) == 0:
            in_pieces = False
        elif in_pieces:
            for piece in line.strip().split(','):
                pieces.append(piece.strip())
        else:
            patterns.append(line.strip())

total_variants = 0
for pattern in patterns:
    variants = can_build(pattern)
    if variants > 0:
        print('built', pattern, variants)
        total_variants += variants

print('possible', total_variants)
