list_numbers = list(map(int, input().split(' ')))
count_odd_nums = 0

for i in range(0, len(list_numbers)):
    if abs(list_numbers[i]) % 2 != 0:
        count_odd_nums += 1

print(count_odd_nums)
