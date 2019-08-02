import sys

n = int(input())
sum = 0
flag = False
flag_num = None

max = -sys.maxsize - 1

for i in range(0, n):
    num = int(input())
    sum += num
    if num > max:
        max = num

if max == (sum - max):
    print(f'Yes\nSum = {max}')
else:
    print(f'No\nDiff = {abs(max - (sum - max))}')
