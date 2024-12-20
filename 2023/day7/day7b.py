import functools

hands = []
bids = {}
scores = {}

card_ordering = {
    'A': 14,
    'K': 13,
    'Q': 12,
    'J': 1,
    'T': 10,
    '9': 9,
    '8': 8,
    '7': 7,
    '6': 6,
    '5': 5,
    '4': 4,
    '3': 3,
    '2': 2,
}


def comparator(hand1, hand2):
    if scores[hand1] > scores[hand2]:
        return 1
    elif scores[hand1] < scores[hand2]:
        return -1
    else:
        lh1 = list(hand1)
        lh2 = list(hand2)
        for index, card in enumerate(lh1):
            if card_ordering[card] > card_ordering[lh2[index]]:
                return 1
            elif card_ordering[card] < card_ordering[lh2[index]]:
                return -1


with open('day7_input.txt', 'r') as file:
    for line in file:
        hand, bid = line.split(' ')
        bids[hand] = int(bid)
        hands.append(hand)

for hand in hands:
    freqs = {}
    hand_list = list(hand)
    for card in hand_list:
        if card not in freqs:
            freqs[card] = 1
        else:
            freqs[card] += 1

    num_jokers = 0
    if 'J' in freqs:
        num_jokers = freqs['J']
        freqs['J'] = 0
    vals = freqs.values()
    max_count = max(vals) + num_jokers
    score = None
    if max_count == 5:
        score = 7
    elif max_count == 4:
        score = 6
    elif max_count == 3:
        if (num_jokers == 0 and 2 in vals) or (num_jokers == 1 and list(vals).count(2) == 2) or (num_jokers == 2 and 2 in vals):
            score = 5
        else:
            score = 4
    elif max_count == 2:
        if (num_jokers == 0 and list(vals).count(2) == 2) or (num_jokers == 1 and 2 in vals):
            score = 3
        else:
            score = 2
    else:
        score = 1
    scores[hand] = score

hands = sorted(hands, key=functools.cmp_to_key(comparator))

score = 0
for index, hand in enumerate(hands):
    score += (index + 1) * bids[hand]

print(score)
