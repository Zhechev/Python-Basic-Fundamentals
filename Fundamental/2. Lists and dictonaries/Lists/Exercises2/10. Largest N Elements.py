input_nums = list(map(int, input().split(' ')))
n = int(input())

result = sorted(input_nums, reverse=True)[:n]

print(' '.join(map(str, result)))
