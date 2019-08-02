tour_price = float(input())
puzzles_num = float(input())
talking_dolls_num = float(input())
teddy_bears_num = float(input())
minions_num = float(input())
trucks_num = float(input())

summ = puzzles_num * 2.6 + talking_dolls_num * 3 + teddy_bears_num * 4.1 + minions_num * 8.2 + trucks_num * 2
all_toys_num = puzzles_num + talking_dolls_num + teddy_bears_num + minions_num + trucks_num

if all_toys_num >= 50:
    summ -= summ * 0.25

summ -= summ * 0.1

if summ >= tour_price:
    result = summ - tour_price
    print(f'Yes! {result:.2f} lv left.')
else:
    result = tour_price - summ
    print(f'Not enough money! {result:.2f} lv needed.')
