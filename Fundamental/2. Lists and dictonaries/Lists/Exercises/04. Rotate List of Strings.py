list_strings = list(input().split(' '))
first_elem = list_strings[0]
last_elem = list_strings[-1]
list_result = []

for i in range(0, len(list_strings) - 1):
    list_result.append(list_strings[i])

list_result.insert(0, last_elem)

print(' '.join(list_result))
