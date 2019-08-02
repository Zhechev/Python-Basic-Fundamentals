row = input()
name = ''
name_sum = 0
max_name_sum = 0

while row != 'STOP':
    name_sum = 0

    for i in range(0, row.__len__()):
        name_sum += ord(row[i])

    if name_sum >= max_name_sum:
        max_name_sum = name_sum
        name = row

    row = input()

print(f'Winner is {name} - {max_name_sum}!')