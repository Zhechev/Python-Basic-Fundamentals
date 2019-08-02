budget_of_group = int(input())
season = input()
num_fishers = int(input())

if season == 'Spring':
    price = 3000
elif season == 'Summer' or season == 'Autumn':
    price = 4200
else:
    price = 2600

if num_fishers <= 6:
    price -= price * 0.10
elif 7 < num_fishers <= 11:
    price -= price * 0.15
elif num_fishers > 12:
    price -= price * 0.25

if num_fishers % 2 == 0 and not season == 'Autumn':
    price -= price * 0.05

if price <= budget_of_group:
    result = budget_of_group - price
    print(f'Yes! You have {result:.2f} leva left.')
else:
    result = price - budget_of_group
    print(f'Not enough money! You need {result:.2f} leva.')
