cache = {}
cards = {}
with open('day4_input.txt', 'r') as file:
    for index, line in enumerate(file):
        winner_str, card_str = line.split(':')[1].split('|')
        winners = winner_str.strip().split(' ')
        card = card_str.strip().split(' ')
        cards[index] = {
            'numbers': card,
            'winners': winners
        }


def count(index):
    matches = 0
    card = cards[index]
    for num in card['numbers']:
        if len(num) > 0 and num in card['winners']:
            matches += 1
    num_cards = 1
    if matches > 0:
        for child_index in range(index + 1, index + 1 + matches):
            if child_index in cache:
                num_cards += cache[child_index]
            else:
                num_cards += count(child_index)
    cache[index] = num_cards
    return num_cards


total = 0
for index in cards.keys():
    if index in cache:
        total += cache[index]
    else:
        total += count(index)

print(total)
