list_numbers = list(map(float, input().split(' ')))

i = 0

while i < len(list_numbers) - 1:
    if list_numbers[i] == list_numbers[i+1]:
        list_numbers[i] = list_numbers[i] + list_numbers[i+1]
        list_numbers.pop(i+1)

        if i > 0:
            i -= 1
    else:
        i += 1

print(' '.join(list(map(str, list_numbers))))
