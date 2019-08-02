num_floors = int(input())
num_rooms = int(input())

for n in range(num_floors, 0, -1):
    row = ''
    for k in range(0, num_rooms):
        if n == num_floors:
            row += f'L{n}{k} '
        else:
            if n % 2 == 0:
                row += f'O{n}{k} '
            else:
                row += f'A{n}{k} '

    print(row)
