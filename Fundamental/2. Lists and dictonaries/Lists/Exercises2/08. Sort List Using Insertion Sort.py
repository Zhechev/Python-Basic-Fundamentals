input_nums = list(map(int, input().split(' ')))

for i in range(1, len(input_nums)):
    for j in range(i, 0, -1):
        if input_nums[i] > input_nums[j]:
            curr_elem = input_nums[j]
            input_nums[j] = input_nums[i]
            input_nums[i] = curr_elem

print(input_nums)
