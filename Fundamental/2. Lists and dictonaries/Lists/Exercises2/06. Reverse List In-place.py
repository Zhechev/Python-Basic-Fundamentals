input_nums = list(input().split(' '))

for i in range(0, int(len(input_nums) / 2)):
    curr_num = input_nums[i]
    input_nums[i] = input_nums[-(i+1)]
    input_nums[-(i+1)] = curr_num

print(' '.join(input_nums))
