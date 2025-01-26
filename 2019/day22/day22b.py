import copy
import time
import re
from sympy import simplify, symbols
NUM_CARDS = 119315717514047


# These functions are used to display the equations in a composed format so that we can simplify

def compose_cut_pos(input, cut):
    if SKIP_MOD:
        if cut > 0:
            return f"(x - {cut} + {input})"
        else:
            return f"(x + {-cut} + {input})"
    else:
        if cut > 0:
            return f"(x - {cut} + {input}) % x"
        else:
            return f"(x + {-cut} + {input}) % x"


def compose_stack_pos(input):
    return f"x - {input} - 1"


def compose_deal_pos(input, deal):
    # return f"({deal} * ({input})) % {NUM_CARDS}"
    if SKIP_MOD:
        return f"({deal} * ({input}))"
    else:
        return f"({deal} * ({input})) % x"


OPERATIONS = []
with open('day22_input.txt', 'r') as file:
    for line in file:
        line = line.strip()
        if 'cut' in line:
            cut_num = int(line.split(' ')[-1])
            OPERATIONS.append(['cut', cut_num])
        if 'deal with increment' in line:
            deal_num = int(line.split(' ')[-1])
            OPERATIONS.append(['deal', deal_num])
        elif 'deal into new stack' in line:
            OPERATIONS.append(['stack'])


def compose_pos():
    rep = "y"
    for operation in OPERATIONS:
        if operation[0] == 'cut':
            rep = compose_cut_pos(rep, operation[1])
        elif operation[0] == 'deal':
            rep = compose_deal_pos(rep, operation[1])
        elif operation[0] == 'stack':
            rep = compose_stack_pos(rep)
    return rep


def calc_euclidean(x, y):
    # This is the extended euclidean algorithm. The last row returned contains the answer
    results = []
    results.append([None, x, 1, 0])
    results.append([None, y, 0, 1])
    remainder = y
    quotient = 0
    row = 1
    while remainder > 0:
        remainder = x % y
        quotient = x // y
        s = results[row - 1][2] - quotient * results[row][2]
        t = results[row - 1][3] - quotient * results[row][3]
        if remainder != 0:
            results.append([quotient, remainder, s, t])
        x = y
        y = remainder
        row += 1
    return results


def pow_mod(x, n, m):
    # This calculates the modular exponentiation of x^n mod m
    if n == 0:
        return 1
    t = pow_mod(x, n // 2, m)
    if n % 2 == 0:
        return (t * t) % m
    else:
        return (t * t * x) % m


SKIP_MOD = True
NUM_CARDS = 119315717514047
iterations = 101741582076661

# Compose the equations to get everything in a single step
composed_equation = compose_pos()

# Now use the sympy library to simplify the equation
x = symbols('x')
y = symbols('y')
simplified_eq = simplify(composed_equation)
matches = re.search(
    '^(.*)[*]x ([+|-]) (.*)[*]y ([+|-]) (.*)$', str(simplified_eq))
sign_1 = matches.group(2)
a = int(matches.group(3))
if sign_1 == '-':
    a *= -1
sign_2 = matches.group(4)
b = int(matches.group(5))
if sign_1 == '-':
    b *= -1
a = a % NUM_CARDS
b = b % NUM_CARDS
# We can now solve for a given position using a * y + b % NUM_CARDS

# Since we need to go backwards from position 2020, let's invert the equation
# x = a * y + b % NUM_CARDS
# y = (x - b) * a_inv % NUM_CARDS
# a_inv is the modular inverse of a
inverse_results = calc_euclidean(NUM_CARDS, a)
a_inverse = inverse_results[-1][3] % NUM_CARDS
# We multiple a_inverse * b to get the value of b in the simplified inverse equation
inv_b = -(a_inverse * b) % NUM_CARDS

forward = a * 2020 + b
reverse = (forward * a_inverse + inv_b) % NUM_CARDS

# Now we can calculate the value of a gemoetric series to get repeated application of ax + b
# F^k(x) = a^k * x + b * (1 - a^k) * (1 - a^(-1))^(-1) % NUM_CARDS

# The denominator is the inverse of (1 - a_inverse)
denom = (1 - a_inverse) % NUM_CARDS
results = calc_euclidean(NUM_CARDS, denom)
coeff = results[-1][3]

# We can use exponentiation by squaring to figure out a^k % NUM_CARDS
a_to_k = pow_mod(a_inverse, iterations, NUM_CARDS)

# Now we can calculate the answer
answer = (a_to_k * 2020 - inv_b * (1 - a_to_k) * coeff) % NUM_CARDS
print('part b', answer)
