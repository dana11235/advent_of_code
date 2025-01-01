import copy
WORKFLOWS = {}
mode = 'workflows'
SUM = 0


def accept_part(part):
    local_sum = 0
    for value in part.values():
        local_sum += value
    return local_sum


with open('day19_input.txt', 'r') as file:
    for line in file:
        line = line.strip()
        if len(line) == 0:
            mode = "parts"
        elif mode == 'workflows':
            workflow = []
            name, rules = line.split('{')
            rules = rules[:-1].split(',')
            for rule in rules:
                if ':' in rule:
                    pieces = rule.split(':')
                    cmp = '>'
                    if '<' in pieces[0]:
                        cmp = '<'
                    workflow.append(
                        {'action': 'test', 'var': pieces[0][0], 'cmp': cmp, 'val': int(pieces[0][2:]), 'dest': pieces[1]})
                else:
                    workflow.append({'action': 'goto', 'dest': rule})
            WORKFLOWS[name] = workflow
        elif mode == 'parts':
            break


ACCEPTED_FLOWS = []


def process_flows(current_rules, workflow, index):
    rule = workflow[index]
    dest = None
    if rule['action'] == 'goto':
        dest = rule['dest']
    else:
        dest = rule['dest']
        pass_sign = rule['cmp']
        fail_sign = '>'
        fail_val = rule['val'] - 1
        # convert the pass into an equivalent fail
        if pass_sign == '>':
            fail_sign = '<'
            fail_val = rule['val'] + 1
        pass_rule = [rule["var"], pass_sign, rule["val"]]
        fail_rule = [rule["var"], fail_sign, fail_val]
        fail_rules = copy.deepcopy(current_rules)
        current_rules.append(pass_rule)
        fail_rules.append(fail_rule)
        # we need to process the fail rule separately
        process_flows(fail_rules, workflow, index + 1)
    if dest:
        if dest == 'A':
            ACCEPTED_FLOWS.append(current_rules)
        elif dest != 'R':
            process_flows(current_rules, WORKFLOWS[dest], 0)


process_flows([], WORKFLOWS['in'], 0)
possibilities = 0
for flow in ACCEPTED_FLOWS:
    min_maxes = {}
    for item in flow:
        key, cmp, val = item
        if key not in min_maxes:
            min_maxes[key] = [0, 4001]
        if cmp == '>' and min_maxes[key][0] < val:
            min_maxes[key][0] = val
        if cmp == '<' and min_maxes[key][1] > val:
            min_maxes[key][1] = val
    value = 1
    for letter in ['x', 'm', 'a', 's']:
        if letter in min_maxes:
            item = min_maxes[letter]
            range = item[1] - item[0] - 1
            value *= range
        else:
            value *= 4000
    possibilities += value
print('poss', possibilities)
