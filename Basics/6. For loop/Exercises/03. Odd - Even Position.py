import sys

n = int(input())
odd_sum = 0
odd_min = 1000
odd_max = -1000
even_sum = 0
even_min = 1000
even_max = -1000

max = -sys.maxsize - 1

for i in range(1, n+1):
    num = float(input())
    if i % 2 == 0:
        even_sum += num
        if num > even_max:
            even_max = num
        if num < even_min:
            even_min = num
    else:
        odd_sum += num
        if num > odd_max:
            odd_max = num
        if num < odd_min:
            odd_min = num


if even_min != 1000 and even_max != -1000:
    print(f'OddSum={odd_sum:.2f},\nOddMin={odd_min:.2f},\nOddMax={odd_max:.2f},\nEvenSum={even_sum:.2f},\nEvenMin={even_min:.2f},\nEvenMax={even_max:.2f}')
elif even_min == 1000 and even_max == -1000 and odd_min == 1000 and odd_max == -1000:
    print(f'OddSum={odd_sum:.2f},\nOddMin=No,\nOddMax=No,\nEvenSum={even_sum:.2f},\nEvenMin=No,\nEvenMax=No')
else:
    print(f'OddSum={odd_sum:.2f},\nOddMin={odd_min:.2f},\nOddMax={odd_max:.2f},\nEvenSum={even_sum:.2f},\nEvenMin=No,\nEvenMax=No')
