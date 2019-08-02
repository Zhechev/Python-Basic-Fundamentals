installments_num = int(input())
sum = 0

while installments_num > 0:
    installment = float(input())
    if installment < 0:
        print('Invalid operation!')
        break
    sum += installment
    print(f'Increase: {installment:.2f}')
    installments_num -= 1

print(f'Total: {sum:.2f}')
