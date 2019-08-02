list_numbers = list(map(int, input().split(' ')))

list_numbers.sort()
list_result = list(map(str, list_numbers))

print(' <= '.join(list_result))

