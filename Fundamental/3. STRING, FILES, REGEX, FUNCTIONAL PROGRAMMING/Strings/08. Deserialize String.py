result = []

for i in range(0, 300):
    result.append('')

while True:
    input_row = input()

    if input_row == 'end':
        break

    input_parts = input_row.split(':')
    char = input_parts[0]
    nums = input_parts[1].split('/')

    for num in nums:
        result[int(num)] = char

print(''.join(result))

