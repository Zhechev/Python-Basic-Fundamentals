input_nums = list(map(int, input().split(' ')))

result = {}

for num in input_nums:
    if num in result:
        result[num] += 1
    else:
        result[num] = 1

for key, val in sorted(result.items()):
    print(f"{key} -> {val}")
