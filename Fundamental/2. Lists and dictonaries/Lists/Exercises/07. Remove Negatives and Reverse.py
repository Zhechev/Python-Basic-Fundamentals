list_numbers = list(map(int, input().split(' ')))
list_result = []

for i in range(0, len(list_numbers)):
    if list_numbers[i] > 0:
        list_result.append(list_numbers[i])

if not list_result:
    print('empty')
else:
    list_result = list(map(str, list_result))
    list_result.reverse()
    print(' '.join(list_result))
