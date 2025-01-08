tokens = None
with open('day15_input.txt', 'r') as file:
    for line in file:
        tokens = line.strip().split(',')


def get_hash(input):
    curr_val = 0
    for char in list(input):
        ascii_val = ord(char)
        curr_val += ascii_val
        curr_val *= 17
        curr_val = curr_val % 256
    return curr_val


BOXES = {}
for token in tokens:
    op = None
    label = None
    lens = None
    if '-' in token:
        op = 'minus'
        label = token[:token.index('-')]
    elif '=' in token:
        op = 'set'
        label, lens = token.split('=')
    box = get_hash(label)
    if box not in BOXES:
        BOXES[box] = []

    if op == 'minus':
        for index, item in enumerate(BOXES[box]):
            if item['label'] == label:
                BOXES[box].pop(index)
    elif op == 'set':
        set = False
        for item in BOXES[box]:
            if item['label'] == label:
                item['lens'] = int(lens)
                set = True
        if not set:
            BOXES[box].append({'label': label, 'lens': int(lens)})

focusing_power = 0
for key in BOXES.keys():
    box = BOXES[key]
    for index, item in enumerate(box):
        focusing_power += (key + 1) * (index + 1) * item['lens']
print(focusing_power)
