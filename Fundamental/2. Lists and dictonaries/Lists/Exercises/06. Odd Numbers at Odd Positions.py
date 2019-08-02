list_numbers = list(map(int, input().split(' ')))

for i in range(0, len(list_numbers)):
    if i % 2 != 0:
        if list_numbers[i] % 2 != 0:
            print(f'Index {i} -> {list_numbers[i]}')
