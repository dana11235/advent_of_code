reps = []
status = True
id = 0
with open('day9_input.txt', 'r') as file:
    for line in list(file):
        for num_str in list(line):
           num = int(num_str) 
           if status:
               reps.append(dict(type='file', id=id, size=num))
               id += 1
           else:
               if num > 0:
                reps.append(dict(type='free', size=num))

           status = not status

index = len(reps) - 1
while index >= 0:
    token = reps[index]
    if token['type'] == 'file':
        for space_index, space_token in enumerate(reps[0:index]):
            if space_token['type'] == 'file':
                continue
            if space_token['size'] >= token['size']:
                token_size = token['size']
                rem_free_size = space_token['size'] - token_size
                reps[space_index] = token
                if (rem_free_size) > 0:
                    reps[index] = dict(type='free', size=token_size)
                    reps.insert(space_index + 1, dict(type='free', size=rem_free_size))
                    index += 1
                else:
                    reps[index] = space_token
                break
    index -= 1

checksum = 0
position = 0
for token in reps:
    if token['type'] == 'file':
        for pos in range(position, position + token['size']):
            checksum += pos * token['id']
    position += token['size']

print(checksum)
