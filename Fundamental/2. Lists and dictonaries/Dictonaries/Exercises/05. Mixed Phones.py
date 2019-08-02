dict = {}

while True:
    command = input()
    if command == 'Over':
        break

    parts = command.split(' : ')
    if parts[1].isdigit():
        dict[parts[0]] = parts[1]
    else:
        dict[parts[1]] = parts[0]

for key in sorted(dict.keys()):
    print(f'{key} -> {dict[key]}')
