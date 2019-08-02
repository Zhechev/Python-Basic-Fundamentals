dict = {}

while True:
    command = input()
    if command == 'end':
        break

    parts = command.split(' = ')
    if parts[1].isdigit():
        dict[parts[0]] = int(parts[1])
    elif parts[1] in dict.keys():
        dict[parts[0]] = dict[parts[1]]

for key, value in dict.items():
    print(f'{key} === {value}')
