numbers = []
prices = {}
deltas = {}
with open('day22_input.txt', 'r') as file:
    for line in file:
        numbers.append(int(line.strip()))


def mix(value, number):
    return value ^ number


def prune(number):
    return number % 16777216


def secretize(number):
    value = prune(mix(number * 64, number))
    value = prune(mix(value // 32, value))
    return prune(mix(value * 2048, value))


sum = 0
for seller, number in enumerate(numbers):
    prices[seller] = []
    deltas[seller] = []
    curr = number
    # Create a list of prices and deltas for each seller
    for i in range(2000):
        curr = secretize(curr)
        prices[seller].append(curr % 10)
        if i > 0:
            deltas[seller].append(prices[seller][-1] - prices[seller][-2])

combo_tracking = {}
combo_prices = {}
# For each seller, go through the combo of deltas, adding the seller to a tracking list and the
# price to a sum for that combo
for seller in deltas.keys():
    for index, delta in enumerate(deltas[seller]):
        if index < len(deltas[seller]) - 3:

            key = f"{deltas[seller][index]},{deltas[seller][index + 1]
                                             },{deltas[seller][index + 2]},{deltas[seller][index + 3]}"
            if key not in combo_tracking:
                combo_tracking[key] = {}
                combo_prices[key] = 0
            if seller not in combo_tracking[key]:
                combo_tracking[key][seller] = index
                combo_prices[key] += prices[seller][index + 4]

# The max prices is the highest total value you can get
print('max_price', max(list(combo_prices.values())))
