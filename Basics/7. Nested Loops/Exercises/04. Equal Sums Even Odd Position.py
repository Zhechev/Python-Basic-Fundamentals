first_num = int(input())
second_num = int(input())

for i in range(first_num, second_num+1):
    sum_event_position = 0
    sum_odd_position = 0
    for k in range(0, str(i).__len__()):
        num = int(str(i)[k])
        if k % 2 == 0:
            sum_event_position += num
        else:
            sum_odd_position += num

    if sum_event_position == sum_odd_position:
        print(i, end=' ')

# import math
#
# n1 = int(input())
# n2 = int(input())
# x1 = 0
# x2 = 0
# x3 = 0
# x4 = 0
# x5 = 0
# x6 = 0
#
# for i in range(n1, n2 + 1):
#     x1 = math.floor(i / 100000) % 10
#     x2 = math.floor(i / 10000) % 10
#     x3 = math.floor(i / 1000) % 10
#     x4 = math.floor(i / 100) % 10
#     x5 = math.floor(i / 10) % 10
#     x6 = i % 10
#     evenSum = x1 + x3 + x5
#     oddSum = x2 + x4 + x6
#     if evenSum == oddSum:
#         print(f"{i} ", end="")
