CARDS = {'val': list(range(10007))}

def cut(n):
    if n > 0:
        CARDS['val'] = CARDS['val'][n:] + CARDS['val'][0:n]
    elif n < 0:
        CARDS['val'] = CARDS['val'][n:] + CARDS['val'][:n]

def stack():
    CARDS['val'].reverse()

def deal(n):
    new_cards = {}
    index = 0
    new_cards[0] = CARDS['val'][0]
    for value in CARDS['val'][1:]:
        index = (index + n) % len(CARDS['val']) 
        new_cards[index] = value
    for i, v in enumerate(CARDS['val']):
        CARDS['val'][i] = new_cards[i]

with open('day22_input.txt', 'r') as file:
    for line in file:
        line = line.strip()
        if 'cut' in line:
            cut(int(line.split(' ')[-1]))
        if 'deal with increment' in line:
            deal(int(line.split(' ')[-1]))
        elif 'deal into new stack' in line:
            stack()

print('part a:', CARDS['val'].index(2019))