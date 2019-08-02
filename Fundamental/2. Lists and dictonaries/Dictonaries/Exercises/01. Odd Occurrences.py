list_parts = list(input().split(' '))
list_occurrances = {}
list_result = []

for value in list_parts:
    value = value.lower()
    if value in list_occurrances:
        list_occurrances[value] += 1
    else:
        list_occurrances[value] = 1

for key, value in list_occurrances.items():
    if value % 2 != 0:
        list_result.append(key)

print(', '.join(list_result))
