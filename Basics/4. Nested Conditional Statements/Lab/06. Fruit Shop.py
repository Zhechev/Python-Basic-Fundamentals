fruit = input()
day = input()
quantity = float(input())
price = -1

week_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
weekends = ['Saturday', 'Sunday']

week_days_price = {'banana': '2.50', 'apple': '1.20', 'orange': '0.85', 'grapefruit': '1.45', 'kiwi': '2.70', 'pineapple': '5.50', 'grapes': '3.85'}
weekends_price = {'banana': '2.70', 'apple': '1.25', 'orange': '0.90', 'grapefruit': '1.60', 'kiwi': '3.00', 'pineapple': '5.60', 'grapes': '4.20'}

if day in week_days and fruit in week_days_price:
    price = quantity * float(week_days_price[fruit])
elif day in weekends and fruit in weekends_price:
    price = quantity * float(weekends_price[fruit])

if price != -1:
    print(f'{price:.2f}')
else:
    print('error')
