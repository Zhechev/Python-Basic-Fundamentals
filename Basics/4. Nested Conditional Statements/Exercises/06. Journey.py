budget = float(input())
season = input()

if budget <= 100:
    print('Somewhere in Bulgaria')
    if season == 'summer':
        result = budget * 0.30
        print(f'Camp - {result:.2f}')
    else:
        result = budget * 0.70
        print(f'Hotel - {result:.2f}')

elif 100 < budget <= 1000:
    print('Somewhere in Balkans')
    if season == 'summer':
        result = budget * 0.40
        print(f'Camp - {result:.2f}')
    else:
        result = budget * 0.80
        print(f'Hotel - {result:.2f}')
else:
    print('Somewhere in Europe')
    result = budget * 0.90
    print(f'Hotel - {result:.2f}')



