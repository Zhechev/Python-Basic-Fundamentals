input_nums = list(map(int, input().split(' ')))

for j in range(len(input_nums)):

    for i in range(0, len(input_nums) - j - 1):
        if input_nums[i] > input_nums[i+1]:
            curr_num = input_nums[i]
            input_nums[i] = input_nums[i+1]
            input_nums[i+1] = curr_num

print(' '.join(map(str, input_nums)))
