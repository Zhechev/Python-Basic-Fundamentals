n = int(input())
fish = input()
win_money = 0
lost_money = 0
fishes_counter = 0
all_fishes_counter = 0

while fish != 'Stop':
    fish_kg = float(input())
    fish_price = 0
    fishes_counter += 1
    all_fishes_counter += 1
    fish_length = str(fish).__len__()
    for i in range(0, fish_length):
        fish_price += ord(fish[i])

    fish_price /= fish_kg

    if fishes_counter == 3:
        fishes_counter = 0
        win_money += fish_price
    else:
        lost_money += fish_price

    if all_fishes_counter == n:
        print(f'Lyubo fulfilled the quota!')
        break

    fish = input()

if win_money >= lost_money:
    profit = win_money - lost_money
    print(f'Lyubo\'s profit from {all_fishes_counter} fishes is {profit:.2f} leva.')
else:
    loss = lost_money - win_money
    print(f'Lyubo lost {loss:.2f} leva today.')
