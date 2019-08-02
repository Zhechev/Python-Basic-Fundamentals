import math

list_numbers = list(map(int, input().split(' ')))
list_result = []

for i in range(0, len(list_numbers)):
    if list_numbers[i] > 0 and math.sqrt(list_numbers[i]) == int(math.sqrt(list_numbers[i])):
        list_result.append(list_numbers[i])

list_result.sort()
list_result.reverse()
list_result = list(map(str, list_result))
print(' '.join(list_result))
