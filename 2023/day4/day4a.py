total = 0
with open('day4_input.txt', 'r') as file:
    for line in file:
        points = 0
        winner_str, card_str = line.split(':')[1].split('|')
        print(winner_str, card_str)
        winners = winner_str.strip().split(' ')
        card = card_str.strip().split(' ')
        print(winners)
        print(card)
        for num in card:
            if len(num) > 0 and num in winners:
                if points == 0:
                    points = 1
                else:
                    points *= 2
        total += points
print(total)
