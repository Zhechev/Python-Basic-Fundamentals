money = float(input())
counter = 0

while money > 0:
    if money >= 2:
        money -= 2.0
    elif money >= 1:
        money -= 1.0
    elif money >= 0.50:
        money -= 0.50
    elif money >= 0.20:
        money -= 0.20
    elif money >= 0.10:
        money -= 0.10
    elif money >= 0.05:
        money -= 0.05
    elif money >= 0.02:
        money -= 0.02
    elif money >= 0.01:
        money -= 0.01

    money = round(money, 2)
    counter += 1

print(counter)
