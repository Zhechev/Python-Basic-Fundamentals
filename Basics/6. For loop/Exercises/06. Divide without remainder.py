n = int(input())

divide_without_reminder_by_2 = 0
divide_without_reminder_by_3 = 0
divide_without_reminder_by_4 = 0


for i in range(0, n):
    num = int(input())

    if num % 2 == 0:
        divide_without_reminder_by_2 += 1
    if num % 3 == 0:
        divide_without_reminder_by_3 += 1
    if num % 4 == 0:
        divide_without_reminder_by_4 += 1


p1 = (divide_without_reminder_by_2 / n) * 100
p2 = (divide_without_reminder_by_3 / n) * 100
p3 = (divide_without_reminder_by_4 / n) * 100

print(f'{p1:.2f}%\n{p2:.2f}%\n{p3:.2f}%')
