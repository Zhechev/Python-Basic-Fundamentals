def multiply_evens_odds(num):
    even_nums_sum = 0
    odd_nums_sum = 0
    for c in str(num):
        if int(c) % 2 == 0:
            even_nums_sum += int(c)
        else:
            odd_nums_sum += int(c)

    print(even_nums_sum * odd_nums_sum)


num = abs(int(input()))
multiply_evens_odds(num)
