def not_zeros(sequence):
    for number in sequence:
        if number != 0:
            return True
    return False


sum = 0
with open('day9_input.txt', 'r') as file:
    for line in file:
        sequences = [[int(num) for num in line.strip().split(' ')]]
        while not_zeros(sequences[-1]):
            diffs = []
            for i in range(1, len(sequences[-1])):
                diffs.append(sequences[-1][i] - sequences[-1][i - 1])
            sequences.append(diffs)

        index = len(sequences) - 2
        while index >= 0:
            curr_sequence = sequences[index]
            next_sequence = sequences[index + 1]
            curr_sequence.insert(0, curr_sequence[0] - next_sequence[0])
            index -= 1
        sum += sequences[0][0]

print(sum)
