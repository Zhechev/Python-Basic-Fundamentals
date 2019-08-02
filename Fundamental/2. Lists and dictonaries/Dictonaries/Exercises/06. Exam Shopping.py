dict_stocks = {}

while True:
    command = input()

    if command == 'shopping time':
        break

    product_parts = command.split(' ')
    product_name = product_parts[1]
    product_quantity = int(product_parts[2])

    if product_name in dict_stocks:
        dict_stocks[product_name] += product_quantity
    else:
        dict_stocks[product_name] = product_quantity

while True:
    command = input()

    if command == 'exam time':
        break

    product_parts = command.split(' ')
    product_name = product_parts[1]
    quantity_purchase = int(product_parts[2])

    if product_name in dict_stocks:
        if dict_stocks[product_name] <= 0:
            print(f'{product_name} out of stock')
        else:
            dict_stocks[product_name] -= quantity_purchase
    else:
        print(f'{product_name} doesn\'t exist')

for product, quantity in dict_stocks.items():
    if int(quantity) > 0:
        print(f'{product} -> {quantity}')
