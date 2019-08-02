def print_dashed_row(n):
    print('-' * 2 * n)


def print_middle_rows(n):
    for k in range(0, n-2):
        print('-', end='')
        for i in range(0, n-1):
            print('\\/', end='')
        print('-', end='')
        print()


n = int(input())
print_dashed_row(n)
print_middle_rows(n)
print_dashed_row(n)
