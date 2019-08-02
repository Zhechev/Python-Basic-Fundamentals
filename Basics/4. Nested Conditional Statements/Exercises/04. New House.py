flowers = input()
quantity = int(input())
budget = int(input())
price = None

if flowers == 'Roses':
    price = quantity * 5
    if quantity > 80:
        price -= price * 0.10
elif flowers == 'Dahlias':
    price = quantity * 3.80
    if quantity > 90:
        price -= price * 0.15

elif flowers == 'Tulips':
    price = quantity * 2.80
    if quantity > 80:
        price -= price * 0.15

elif flowers == 'Narcissus':
    price = quantity * 3.00
    if quantity < 120:
        price += price * 0.15

elif flowers == 'Gladiolus':
    price = quantity * 2.50
    if quantity < 80:
        price += price * 0.20

if price > budget:
    result = price - budget
    print(f'Not enough money, you need {result:.2f} leva more.')
else:
    result = budget - price
    print(f'Hey, you have a great garden with {quantity} {flowers} and {result:.2f} leva left.')
