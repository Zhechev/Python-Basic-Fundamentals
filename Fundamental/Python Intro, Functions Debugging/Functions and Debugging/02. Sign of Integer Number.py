def check_sign_number(n):
    if n < 0:
        print(f'The number {n} is negative.')
    elif n == 0:
        print(f'The number 0 is zero.')
    else:
        print(f'The number {n} is positive.')


n = int(input())
check_sign_number(n)