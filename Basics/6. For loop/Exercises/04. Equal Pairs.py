n = int(input())
pairs_sum = 0
last_sum = 0
diff = 0

for i in range(0, n):
    first_num = int(input())
    second_num = int(input())
    pairs_sum = first_num + second_num

    if i != 0:
        diff = abs(last_sum - pairs_sum)
    last_sum = pairs_sum

if diff == 0:
    print(f'Yes, value={last_sum}')
else:
    print(f'No, maxdiff={diff}')
