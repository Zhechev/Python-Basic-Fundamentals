n = int(input())

for a in range(1, 10):
    for b in range(1, 10):
        for c in range(1, 10):
            for d in range(1, 10):
                if (n % a == 0) and (n % b == 0) and (n % c == 0) and (n % d == 0):
                    print(f'{a}{b}{c}{d} ', end='')





# n = int(input()) !!!!1time problem in JUDGE!!!
#
# for i in range(1111, 10000):
#     is_special = True
#     for k in range(0, str(i).__len__()):
#         digit = int(str(i)[k])
#         if digit == 0:
#             is_special = False
#             break
#         if n % digit != 0:
#             is_special = False
#             break
#
#     if is_special:
#         print(f'{i} ', end='')
