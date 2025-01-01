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
            pieces = line[1:-1].split(',')
            components = {}
            for piece in pieces:
                var, value = piece.split('=')
                components[var] = int(value)
            workflow = WORKFLOWS['in']
            cont = True
            while cont:
                dest = None
                for rule in workflow:
                    if rule['action'] == 'goto':
                        dest = rule['dest']
                    elif rule['action'] == 'test':
                        if rule['cmp'] == '>' and components[rule['var']] > rule['val']:
                            dest = rule['dest']
                        if rule['cmp'] == '<' and components[rule['var']] < rule['val']:
                            dest = rule['dest']
                    if dest:
                        if dest == 'A':
                            SUM += accept_part(components)
                            cont = False
                            break
                        elif dest == 'R':
                            cont = False
                            break
                        else:
                            workflow = WORKFLOWS[rule['dest']]
                            break

print(SUM)
