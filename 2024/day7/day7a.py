def mul_add(operands, total, current):
    if len(operands) == 1:
        current.append(operands[0])
        calc = current[0]
        pos = 1 
        while pos < len(current):
            if current[pos] == '+':
                calc += current[pos + 1]
            elif current[pos] == '*':
                calc *= current[pos + 1]
            pos += 2

        return calc == total
    else:
        new_operands = operands.copy()
        curr_oper = new_operands.pop(0)
        mul = current.copy()
        mul.append(curr_oper)
        mul.append('*')

        add = current.copy()
        add.append(curr_oper)
        add.append('+')

        return mul_add(new_operands, total, mul) or mul_add(new_operands, total, add)

total_correct = 0
with open('day7_input.txt', 'r') as file:
    for line in file:
        parts = line.split(':')
        total = int(parts[0])
        operands = [int(number) for number in parts[1].split()]
        if mul_add(operands, total, []):
            total_correct += total

print(total_correct)