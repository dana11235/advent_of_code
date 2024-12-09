uncompressed = []
free_spaces = 0
status = True
id = 0
with open('day9_input.txt', 'r') as file:
    for line in list(file):
        for num_str in list(line):
           num = int(num_str) 
           for i in range(num):
               if status:
                   uncompressed.append(id)
               else:
                   uncompressed.append('X')
                   free_spaces += 1
           if status:
               id += 1

           status = not status

flipped = True
while flipped:
    right_pointer = len(uncompressed) - 1
    left_pointer = 0
    num_flipped = 0
    while left_pointer < right_pointer:
        while uncompressed[left_pointer] != 'X':
            left_pointer += 1
        while  uncompressed[right_pointer] == 'X':
            right_pointer -= 1
        if left_pointer < right_pointer:
            uncompressed[left_pointer] = uncompressed[right_pointer]
            uncompressed[right_pointer] = 'X'
            num_flipped += 1
    if num_flipped == 0:
        flipped = False
    

checksum = 0
for index, id in enumerate(uncompressed):
    if id != 'X':
        checksum += index * id

print(checksum)
