tokens = None
with open('day15_input.txt', 'r') as file:
    for line in file:
        tokens = line.strip().split(',')

sum = 0
for token in tokens:
    curr_val = 0
    for char in list(token):
        ascii_val = ord(char)
        curr_val += ascii_val
        curr_val *= 17
        curr_val = curr_val % 256
    sum += curr_val

print(sum)
