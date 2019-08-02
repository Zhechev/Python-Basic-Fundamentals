n = input()
steps = 0

while n != 'Going home':
    steps += int(n)
    if steps >= 10000:
        print('Goal reached! Good job!')
        exit()
    n = input()
add_steps = int(input())
steps += add_steps

if steps >= 10000:
    print('Goal reached! Good job!')
else:
    result = 10000 - steps
    print(f'{result} more steps to reach goal.')
