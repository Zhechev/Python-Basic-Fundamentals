product = input()
town = input()
quantity = float(input())

if town == 'Sofia':
    if product == 'coffee':
        print(quantity * 0.50)
    elif product == 'water':
        print(quantity * 0.80)
    elif product == 'beer':
        print(quantity * 1.20)
    elif product == 'sweets':
        print(quantity * 1.45)
    else:
        print(quantity * 1.60)
elif town == 'Plovdiv':
    if product == 'coffee':
        print(quantity * 0.40)
    elif product == 'water':
        print(quantity * 0.70)
    elif product == 'beer':
        print(quantity * 1.15)
    elif product == 'sweets':
        print(quantity * 1.30)
    else:
        print(quantity * 1.50)
else:
    if product == 'coffee':
        print(quantity * 0.45)
    elif product == 'water':
        print(quantity * 0.70)
    elif product == 'beer':
        print(quantity * 1.10)
    elif product == 'sweets':
        print(quantity * 1.35)
    else:
        print(quantity * 1.55)
