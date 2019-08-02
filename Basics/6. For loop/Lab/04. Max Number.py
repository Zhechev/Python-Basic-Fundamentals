import sys
input_nums = int(input())
min_num = max = sys.maxsize

for i in range(0, input_nums):
    num = int(input())
    if num < min_num:
        min_num = num

print(min_num)
