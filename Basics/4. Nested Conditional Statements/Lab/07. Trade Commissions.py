city_name = input()
sells = float(input())
commission = -1

if city_name == 'Sofia':
    if 0 <= sells <= 500:
        commission = sells * 0.05
    elif 500 < sells <= 1000:
        commission = sells * 0.07
    elif 1000 < sells <= 10000:
        commission = sells * 0.08
    elif sells > 10000:
        commission = sells * 0.12
elif city_name == 'Varna':
    if 0 <= sells <= 500:
        commission = sells * 0.045
    elif 500 < sells <= 1000:
        commission = sells * 0.075
    elif 1000 < sells <= 10000:
        commission = sells * 0.10
    elif sells > 10000:
        commission = sells * 0.13
elif city_name == 'Plovdiv':
    if 0 <= sells <= 500:
        commission = sells * 0.055
    elif 500 < sells <= 1000:
        commission = sells * 0.08
    elif 1000 < sells <= 10000:
        commission = sells * 0.12
    elif sells > 10000:
        commission = sells * 0.145

if commission != -1:
    print(f'{commission:.2f}')
else:
    print('error')
