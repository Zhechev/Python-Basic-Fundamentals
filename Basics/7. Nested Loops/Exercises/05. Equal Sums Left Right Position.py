first_num = int(input())
second_num = int(input())

for i in range(first_num, second_num + 1):
    x1 = int(i / 10000) % 10
    x2 = int(i / 1000) % 10
    x3 = int(i / 100) % 10
    x4 = int(i / 10) % 10
    x5 = i % 10

    left_side = x1 + x2
    right_side = x4 + x5

    if left_side != right_side:
        if left_side < right_side:
            left_side += x3
        else:
            right_side += x3

    if left_side == right_side:
        print(f'{i} ', end='')
