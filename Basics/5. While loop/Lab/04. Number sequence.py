import sys
max = sys.maxsize
min = -sys.maxsize - 1

n = input()

while True:
    if n == 'END':
        break
    n = int(n)
    if n > min:
        min = n
    if n < max:
        max = n

    n = input()

print(f'Max number: {min}')
print(f'Min number: {max}')