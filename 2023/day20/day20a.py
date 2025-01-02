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


def process_next():
    next = TO_PROCESS.pop(0)
    name = next['name']
    last = next['last']
    input_state = next['state']
    PULSES[input_state] += 1

    # If this is the output module, don't do anything
    module = None
    if name in CONNECTIONS:
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
            for dest in module['dests']:
                TO_PROCESS.append(
                    {'name': dest, 'state': output_state, 'last': name}
                )


for _ in range(1000):
    TO_PROCESS = [{'name': 'broadcaster', 'state': 0, 'last': None}]
    while len(TO_PROCESS) > 0:
        process_next()

print('pulses', PULSES[0] * PULSES[1])
