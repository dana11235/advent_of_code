CONNECTIONS = {}
STATE = {}
PULSES = [0, 0]
TO_PROCESS = []
with open('day20_input.txt', 'r') as file:
    for line in file:
        line = line.strip()
        source, dests = line.split(' -> ')
        dests = [dest.strip() for dest in dests.split(',')]
        op = '-'
        if source != 'broadcaster':
            op = source[0]
            source = source[1:]
        CONNECTIONS[source] = {'op': op, 'dests': dests}

# Initialize the conjunction modules
for key in list(CONNECTIONS.keys()):
    module = CONNECTIONS[key]
    if module['op'] == '&':
        initial_state = {}
        for inbound_name in list(CONNECTIONS.keys()):
            inbound = CONNECTIONS[inbound_name]
            if key in inbound['dests']:
                initial_state[inbound_name] = 0
        STATE[key] = initial_state


ITER_NUM = 0
TOTAL_ITERS = 1


def process_next():
    mul_by_total_iters = None
    next = TO_PROCESS.pop(0)
    name = next['name']
    last = next['last']
    input_state = next['state']

    if name not in CONNECTIONS:
        PULSES[input_state] += 1
    else:
        module = CONNECTIONS[name]

        if module['op'] == '-':
            # It's a broadcaster, just pass straight through
            for dest in module['dests']:
                TO_PROCESS.append(
                    {'name': dest, 'state': input_state, 'last': name})
        elif module['op'] == '%':
            # It's a flip flop
            flip_flop_state = 0
            if name in STATE:
                flip_flop_state = STATE[name]
            if input_state == 0:
                flip_flop_state = (flip_flop_state + 1) % 2
                STATE[name] = flip_flop_state
                for dest in module['dests']:
                    TO_PROCESS.append(
                        {'name': dest, 'state': flip_flop_state, 'last': name})
        elif module['op'] == '&':
            # It's a conjunction module
            last_inputs = STATE[name]
            last_inputs[last] = input_state
            STATE[name] = last_inputs
            output_state = 1
            for input in list(last_inputs.values()):
                output_state &= input
            output_state = (output_state + 1) % 2
            # These are the 4 inputs that feed into RX.
            if output_state == 1 and name in ['zf', 'qx', 'cd', 'rk']:
                # If an input is high, we can multiply the product by it
                # There is a possibility that the LCM is less than the numbers multiplied, but that isn't the case here
                mul_by_total_iters = ITER_NUM
            for dest in module['dests']:
                TO_PROCESS.append(
                    {'name': dest, 'state': output_state, 'last': name}
                )
        return mul_by_total_iters


# I chose this number because this was enough time for each critical input to be high once
for i in range(5000):
    ITER_NUM = i + 1
    TO_PROCESS = [{'name': 'broadcaster', 'state': 0, 'last': None}]
    while len(TO_PROCESS) > 0:
        mul = process_next()
        if mul:
            TOTAL_ITERS *= mul

print('iterations', TOTAL_ITERS)
