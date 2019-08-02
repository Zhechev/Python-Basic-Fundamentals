n = int(input())
result = {}

for i in range(1, n+1):
    input_row = input()
    input_parts = input_row.split(' -> ')
    color = input_parts[0]
    items = input_parts[1].split(',')

    if color not in result:
        result[color] = {}

    for item in items:
        if item not in result[color]:
            result[color].update({item: 0})
        result[color][item] += 1

print_row = input().split(' ')
color = print_row[0]
item = print_row[1]

for key, value in result.items():
    print(f'{key} clothes:')
    for cloth, count in value.items():
        if item == cloth:
            print(f'* {cloth} - {count} (found!)')
        else:
            print(f'* {cloth} - {count}')
