name = input()
sum = 0
n = 1
counter_excluded = 0

while n <= 12:
    grade = float(input())
    if grade >= 4.00:
        sum += grade
        n += 1
    else:
        counter_excluded += 1
        if counter_excluded == 2:
            print(f'{name} has been excluded at {n} grade')
            exit()

avg = sum / 12
print(f'{name} graduated. Average grade: {avg:.2f}')
