num = int(input())

while num > 100 or num < 1:
    print(f'Invalid number!')
    num = int(input())

print(f'The number is: {num}')
