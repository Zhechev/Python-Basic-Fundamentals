list_parts = list(input().split('|'))
list_result = []
list_parts.reverse()
num = -3

for i in range(0, len(list_parts)):
    list_nums = list(list_parts[i].split(' '))
    for k in range(0, len(list_nums)):
        if list_nums[k] != '':
            list_result.append(list_nums[k])

print(' '.join(list_result))
