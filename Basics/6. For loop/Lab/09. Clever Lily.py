lily_age = int(input())
washing_machine_price = float(input())
toy_price = int(input())
money = 0
toys_count = 0
money_from_birthdays = 0

for i in range(1, lily_age + 1):
    if i % 2 == 0:
        money_from_birthdays += 10
        money += money_from_birthdays
        money -= 1
    else:
        toys_count += 1

money_from_toys = toys_count * toy_price
money += money_from_toys

if money >= washing_machine_price:
    print(f'Yes! {money - washing_machine_price:.2f}')
else:
    print(f'No! {washing_machine_price - money:.2f}')
