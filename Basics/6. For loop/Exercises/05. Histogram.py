n = int(input())

nums_below_200 = 0
nums_between_200_and_399 = 0
nums_between_400_and_599 = 0
nums_between_600_and_799 = 0
nums_above_800 = 0


for i in range(0, n):
    num = int(input())

    if num < 200:
        nums_below_200 += 1
    elif 200 <= num < 400:
        nums_between_200_and_399 += 1
    elif 400 <= num < 600:
        nums_between_400_and_599 += 1
    elif 600 <= num < 800:
        nums_between_600_and_799 += 1
    elif num >= 800:
        nums_above_800 += 1

p1 = (nums_below_200 / n) * 100
p2 = (nums_between_200_and_399 / n) * 100
p3 = (nums_between_400_and_599 / n) * 100
p4 = (nums_between_600_and_799 / n) * 100
p5 = (nums_above_800 / n) * 100

print(f'{p1:.2f}%\n{p2:.2f}%\n{p3:.2f}%\n{p4:.2f}%\n{p5:.2f}%')
