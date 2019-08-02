list_parts = list(map(float, input().split(' ')))
list_result = {}

for value in list_parts:
    if value in list_result:
        list_result[value] += 1
    else:
        list_result[value] = 1

for key in sorted(list_result.keys()):
    print(f'{key} -> {list_result[key]} times')
