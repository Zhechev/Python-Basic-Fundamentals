n = input()
prime_numbers_sum = 0
non_prime_numbers_sum = 0

while n != 'stop':
    is_prime = True
    num = int(n)
    if num < 0:
        print('Number is negative.')
    elif 0 <= num < 2:
        non_prime_numbers_sum += num
    else:
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break

        if is_prime:
            prime_numbers_sum += num
        else:
            non_prime_numbers_sum += num

    n = input()

print(f'Sum of all prime numbers is: {prime_numbers_sum}')
print(f'Sum of all non prime numbers is: {non_prime_numbers_sum}')